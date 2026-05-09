#!/usr/bin/env python3
"""
Local Bot Server — General's Command Post.

HTTP API server (port 7474) that lets the Curator UI trigger enrichment bots
on local hardware using Ollama models. No cloud quotas consumed.

Think of it as the General's forward command: the UI is the battle map,
this server dispatches local reinforcements where needed most.

Model Assignments (by job quality requirements):
  enrich       → llama3.2:3b (fast bulk) or specify --model for quality runs
  significance → llama3.2:3b (structured short task, perfect fit)
  queue        → No LLM needed (pure scoring logic)
  sync         → No LLM needed (TypeScript gateway)
  audit bots   → No LLM needed (pure data analysis)

Endpoints:
  GET  /health                 — Health check + Ollama status
  GET  /bots/status            — All running jobs status
  GET  /bots/models            — Available Ollama models
  POST /bots/enrich            — Run AI enrichment (body: {count, model})
  POST /bots/significance      — Run significance backfill
  POST /bots/queue             — Regenerate enrichment queue
  POST /bots/sync              — Run sync gateway
  POST /bots/all               — Dispatch all bots concurrently
  POST /bots/stop              — Stop all running local bots

Usage:
    python3 scripts/local_bot_server.py
    python3 scripts/local_bot_server.py --port 7474
"""
from __future__ import annotations

import argparse
import json
import os
import signal
import subprocess
import sys
import threading
import time
import traceback
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Optional

# ─── Paths ────────────────────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = REPO_ROOT / "scripts"
STATUS_FILE = REPO_ROOT / "data" / "enrichment" / "local_bot_status.json"
STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)

OLLAMA_BASE = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
GITHUB_REPO = os.environ.get("GITHUB_REPO", "14-yama/annals-of-the-world")

# ─── Job Registry ─────────────────────────────────────────────────────────────
_lock = threading.Lock()
_jobs: dict[str, dict] = {}   # job_id → {bot, status, pid, started, log, count}


def _new_job(bot: str, count: int = 10, model: str = "llama3.2:3b") -> str:
    job_id = f"{bot}-{int(time.time())}"
    with _lock:
        _jobs[job_id] = {
            "job_id": job_id,
            "bot": bot,
            "status": "queued",
            "model": model,
            "count": count,
            "pid": None,
            "started": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "finished": None,
            "log": [],
            "exitCode": None,
        }
    _flush_status()
    return job_id


def _update_job(job_id: str, **kwargs):
    with _lock:
        if job_id in _jobs:
            _jobs[job_id].update(kwargs)
    _flush_status()


def _flush_status():
    """Write job registry to disk so the UI can poll it."""
    try:
        with _lock:
            snapshot = {k: {**v} for k, v in _jobs.items()}
        STATUS_FILE.write_text(json.dumps(snapshot, indent=2))
    except Exception:
        pass


def get_all_status() -> dict:
    with _lock:
        return {k: {**v} for k, v in _jobs.items()}


# ─── Ollama Helpers ───────────────────────────────────────────────────────────

def ollama_health() -> dict:
    """Check if Ollama is running and return available models."""
    try:
        req = urllib.request.Request(f"{OLLAMA_BASE}/api/tags")
        with urllib.request.urlopen(req, timeout=5) as r:
            data = json.loads(r.read())
        models = [m["name"] for m in data.get("models", [])]
        return {"running": True, "models": models}
    except Exception as e:
        return {"running": False, "models": [], "error": str(e)}


def ollama_ps() -> dict:
    """Return currently-running Ollama model inferences (/api/ps)."""
    try:
        req = urllib.request.Request(f"{OLLAMA_BASE}/api/ps")
        with urllib.request.urlopen(req, timeout=5) as r:
            data = json.loads(r.read())
        return {"running": True, "models": data.get("models", [])}
    except Exception as e:
        return {"running": False, "models": [], "error": str(e)}


def sprint_stats() -> dict:
    """Summarise completed work in the last 24 hours from the job registry."""
    cutoff = time.time() - 86400
    total_entities = 0
    by_bot: dict[str, int] = {}
    with _lock:
        for job in _jobs.values():
            if job["status"] != "done":
                continue
            try:
                started_ts = time.mktime(time.strptime(job["started"], "%Y-%m-%dT%H:%M:%SZ"))
            except Exception:
                continue
            if started_ts < cutoff:
                continue
            c = job.get("count", 0) or 0
            total_entities += c
            bot = job.get("bot", "unknown")
            by_bot[bot] = by_bot.get(bot, 0) + c
    return {
        "window": "last_24h",
        "totalEntitiesProcessed": total_entities,
        "byBot": by_bot,
        "completedJobs": sum(
            1 for j in _jobs.values()
            if j["status"] == "done"
        ),
    }


# ─── Bot Runner ───────────────────────────────────────────────────────────────

def _run_subprocess(job_id: str, cmd: list[str], env: dict | None = None):
    """Run a bot script in a subprocess; stream its stdout to the job log."""
    _update_job(job_id, status="running")
    log: list[str] = []
    try:
        merged_env = {**os.environ}
        if env:
            merged_env.update(env)

        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            cwd=str(REPO_ROOT),
            env=merged_env,
        )
        _update_job(job_id, pid=proc.pid)

        for line in proc.stdout:  # type: ignore[union-attr]
            line = line.rstrip()
            log.append(line)
            # Keep last 200 lines in memory
            if len(log) > 200:
                log = log[-200:]
            _update_job(job_id, log=log)

        proc.wait()
        _update_job(
            job_id,
            status="done" if proc.returncode == 0 else "error",
            exitCode=proc.returncode,
            finished=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            log=log,
        )
    except Exception as exc:
        _update_job(
            job_id,
            status="error",
            log=log + [f"Exception: {exc}", traceback.format_exc()],
            finished=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        )


def dispatch_enrich(count: int = 20, model: str = "ollama") -> str:
    """Dispatch AI enrichment bot locally."""
    job_id = _new_job("enrich", count=count, model=model)
    cmd = [sys.executable, str(SCRIPTS / "ai_enrich_autonomous.py"),
           "--count", str(count), "--model", model]
    t = threading.Thread(target=_run_subprocess, args=(job_id, cmd), daemon=True)
    t.start()
    return job_id


def dispatch_significance(count: int = 50, model: str = "ollama") -> str:
    """Dispatch significance backfill bot locally."""
    job_id = _new_job("significance", count=count, model=model)
    cmd = [sys.executable, str(SCRIPTS / "backfill_significance.py"),
           "--count", str(count), "--model", model]
    t = threading.Thread(target=_run_subprocess, args=(job_id, cmd), daemon=True)
    t.start()
    return job_id


def dispatch_queue() -> str:
    """Regenerate enrichment queue (no LLM needed)."""
    job_id = _new_job("queue", count=0, model="none")
    cmd = [sys.executable, str(SCRIPTS / "enrichment_queue.py")]
    t = threading.Thread(target=_run_subprocess, args=(job_id, cmd), daemon=True)
    t.start()
    return job_id


def dispatch_sync(max_entities: int = 50) -> str:
    """Run sync gateway (push local JSON → Appwrite)."""
    job_id = _new_job("sync", count=max_entities, model="none")

    def _run_sync(jid):
        _update_job(jid, status="running")
        log = []
        try:
            env = {**os.environ}
            # Load .env manually
            env_file = REPO_ROOT / ".env"
            if env_file.exists():
                for line in env_file.read_text().splitlines():
                    line = line.strip()
                    if not line or line.startswith("#") or "=" not in line:
                        continue
                    k, _, v = line.partition("=")
                    env[k.strip()] = v.strip()

            proc = subprocess.Popen(
                ["npx", "tsx", "scripts/sync_gateway.ts", f"--max={max_entities}"],
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                text=True, cwd=str(REPO_ROOT), env=env,
            )
            _update_job(jid, pid=proc.pid)
            for line in proc.stdout:  # type: ignore[union-attr]
                line = line.rstrip()
                log.append(line)
                if len(log) > 200:
                    log = log[-200:]
                _update_job(jid, log=log)
            proc.wait()
            _update_job(jid,
                status="done" if proc.returncode == 0 else "error",
                exitCode=proc.returncode,
                finished=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                log=log,
            )
        except Exception as exc:
            _update_job(jid, status="error",
                log=log + [str(exc)],
                finished=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))

    t = threading.Thread(target=_run_sync, args=(job_id,), daemon=True)
    t.start()
    return job_id


def dispatch_all(enrich_count: int = 20, sig_count: int = 50) -> list[str]:
    """
    Assist All — deploy all local reinforcements concurrently.
    Like a general sending troops to every front simultaneously.
    """
    jobs = []
    # Queue first (no LLM, fast)
    jobs.append(dispatch_queue())
    # Then enrich + significance in parallel (both use Ollama)
    jobs.append(dispatch_enrich(count=enrich_count, model="ollama"))
    jobs.append(dispatch_significance(count=sig_count, model="ollama"))
    # Sync last (30s delay to let enrichments write files)
    def _delayed_sync():
        time.sleep(30)
        dispatch_sync(max_entities=50)
    threading.Thread(target=_delayed_sync, daemon=True).start()
    return jobs


def stop_all() -> list[str]:
    """Kill all running local bot processes."""
    stopped = []
    with _lock:
        for job_id, job in _jobs.items():
            if job["status"] == "running" and job.get("pid"):
                try:
                    os.kill(job["pid"], signal.SIGTERM)
                    job["status"] = "stopped"
                    job["finished"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
                    stopped.append(job_id)
                except ProcessLookupError:
                    pass
    _flush_status()
    return stopped


# ─── Git + GitHub Helpers ─────────────────────────────────────────────────────

def git_pending_count() -> dict:
    """Return count of uncommitted local entity/edge changes ready to push."""
    try:
        result = subprocess.run(
            ["git", "status", "--short", "--", "data/appwrite-export/"],
            cwd=str(REPO_ROOT), capture_output=True, text=True, timeout=15,
        )
        lines = [l for l in result.stdout.splitlines() if l.strip()]
        entity_lines = [l for l in lines if "entities/" in l]
        edge_lines = [l for l in lines if "edges/" in l]
        return {
            "total": len(lines),
            "entities": len(entity_lines),
            "edges": len(edge_lines),
            "hasPending": len(lines) > 0,
        }
    except Exception as e:
        return {"total": 0, "entities": 0, "edges": 0, "hasPending": False, "error": str(e)}


def github_actions_status() -> list[dict]:
    """
    Return GitHub Actions workflow run statuses.
    Primary: read data/governance/last_github_runs.json (written by GH Actions workflows).
    Fallback: GitHub API (requires GITHUB_TOKEN for private repos).
    """
    # Primary: local file written by GH Actions commit step
    runs_file = REPO_ROOT / "data" / "governance" / "last_github_runs.json"
    if runs_file.exists():
        try:
            data = json.loads(runs_file.read_text())
            return data if isinstance(data, list) else data.get("runs", [])
        except Exception:
            pass

    # Fallback: GitHub API (works for public repos or with GITHUB_TOKEN)
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        return []  # private repo, no token — UI hides the panel gracefully
    headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28",
               "Authorization": f"Bearer {token}"}
    try:
        url = f"https://api.github.com/repos/{GITHUB_REPO}/actions/runs?per_page=20"
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
        runs = data.get("workflow_runs", [])
        seen: dict[str, dict] = {}
        for run in runs:
            name = run.get("name", "")
            if name not in seen:
                seen[name] = {
                    "name": name,
                    "status": run.get("status", ""),
                    "conclusion": run.get("conclusion"),
                    "runId": run.get("id"),
                    "startedAt": run.get("run_started_at"),
                    "updatedAt": run.get("updated_at"),
                    "htmlUrl": run.get("html_url", ""),
                    "triggeredBy": run.get("event", ""),
                }
        return list(seen.values())
    except Exception:
        return []


def dispatch_git_push(message: str = "") -> str:
    """Commit all local enrichment changes and push to git (triggers GH Actions sync)."""
    job_id = _new_job("git-push", count=0, model="none")

    def _run(jid: str):
        _update_job(jid, status="running")
        log: list[str] = []

        def _log(msg: str):
            log.append(msg)
            _update_job(jid, log=log[-200:])

        try:
            pending = git_pending_count()
            _log(f"Pending files: {pending['entities']} entities, {pending['edges']} edges ({pending['total']} total)")
            if not pending["hasPending"]:
                _log("Nothing to commit — working tree clean.")
                _update_job(jid, status="done", exitCode=0,
                            finished=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
                return

            commit_msg = message or (
                f"feat(enrich): local Ollama enrichments — "
                f"{pending['entities']} entities, {pending['edges']} edges"
            )

            # git add
            _log("git add data/appwrite-export/ ...")
            r = subprocess.run(
                ["git", "add", "data/appwrite-export/", "data/enrichment/", "data/governance/"],
                cwd=str(REPO_ROOT), capture_output=True, text=True, timeout=30,
            )
            if r.returncode != 0:
                _log(f"git add failed: {r.stderr}")
                _update_job(jid, status="error", exitCode=r.returncode,
                            finished=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
                return

            # git commit
            _log(f"git commit -m \"{commit_msg}\"")
            env = {**os.environ, "GIT_AUTHOR_NAME": "Annals Local Bot", "GIT_AUTHOR_EMAIL": "local-bot@annals-of-the-world.bot",
                   "GIT_COMMITTER_NAME": "Annals Local Bot", "GIT_COMMITTER_EMAIL": "local-bot@annals-of-the-world.bot"}
            r = subprocess.run(
                ["git", "commit", "-m", commit_msg],
                cwd=str(REPO_ROOT), capture_output=True, text=True, timeout=30, env=env,
            )
            _log(r.stdout.strip() or r.stderr.strip())
            if r.returncode != 0 and "nothing to commit" not in r.stdout + r.stderr:
                _log(f"git commit failed: {r.stderr}")
                _update_job(jid, status="error", exitCode=r.returncode,
                            finished=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
                return

            # git push
            _log("git push ...")
            r = subprocess.run(
                ["git", "push"],
                cwd=str(REPO_ROOT), capture_output=True, text=True, timeout=60, env=env,
            )
            _log(r.stdout.strip() or r.stderr.strip())
            if r.returncode != 0:
                _log(f"git push failed — check SSH/HTTPS credentials: {r.stderr}")
                _update_job(jid, status="error", exitCode=r.returncode,
                            finished=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
                return

            _log(f"✓ Pushed {pending['total']} files → GitHub → GH Actions sync will push to Appwrite")
            _update_job(jid, status="done", exitCode=0, count=pending["total"],
                        finished=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
        except Exception as exc:
            _update_job(jid, status="error",
                        log=log + [f"Exception: {exc}", traceback.format_exc()],
                        finished=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))

    t = threading.Thread(target=_run, args=(job_id,), daemon=True)
    t.start()
    return job_id


def dispatch_sync_and_push(max_entities: int = 100) -> str:
    """
    Concurrent two-step: push direct to Appwrite via sync_gateway.ts, THEN
    git commit+push so the repo stays in sync with cloud.
    """
    job_id = _new_job("sync-push", count=max_entities, model="none")

    def _run(jid: str):
        # Step 1: direct Appwrite sync
        sync_jid = dispatch_sync(max_entities=max_entities)
        # Wait for sync to finish
        while True:
            with _lock:
                sync_status = _jobs.get(sync_jid, {}).get("status", "done")
            if sync_status in ("done", "error", "stopped"):
                break
            time.sleep(2)
        # Step 2: git commit+push
        dispatch_git_push()
        _update_job(jid, status="done", exitCode=0,
                    finished=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))

    t = threading.Thread(target=_run, args=(job_id,), daemon=True)
    t.start()
    return job_id


def dispatch_all(enrich_count: int = 20, sig_count: int = 50, auto_push: bool = True) -> list[str]:
    """
    Assist All — deploy all local reinforcements concurrently.
    Runs: queue scan → enrich + significance (parallel) → sync to Appwrite → git push.
    Local (Ollama) and cloud (GitHub Actions) can run simultaneously — safe because
    each writes to separate entity files; merge conflicts are handled by sync_gateway.
    """
    jobs = []
    # Queue first (no LLM, fast)
    jobs.append(dispatch_queue())
    # Then enrich + significance in parallel (both use Ollama)
    enrich_jid = dispatch_enrich(count=enrich_count, model="ollama")
    sig_jid = dispatch_significance(count=sig_count, model="ollama")
    jobs.extend([enrich_jid, sig_jid])

    if auto_push:
        def _delayed_sync_push():
            # Wait for both bots to finish
            for jid in [enrich_jid, sig_jid]:
                while True:
                    with _lock:
                        s = _jobs.get(jid, {}).get("status", "done")
                    if s in ("done", "error", "stopped"):
                        break
                    time.sleep(5)
            # Push direct to Appwrite first
            sync_jid = dispatch_sync(max_entities=max(enrich_count, 50))
            with _lock:
                jobs.append(sync_jid)
            # Wait for sync
            while True:
                with _lock:
                    s = _jobs.get(sync_jid, {}).get("status", "done")
                if s in ("done", "error", "stopped"):
                    break
                time.sleep(2)
            # Then git push to keep repo in sync + trigger GH Actions
            push_jid = dispatch_git_push()
            with _lock:
                jobs.append(push_jid)

        threading.Thread(target=_delayed_sync_push, daemon=True).start()

    return jobs


# ─── HTTP Handler ─────────────────────────────────────────────────────────────

CORS_HEADERS = {
    "Access-Control-Allow-Origin": "http://localhost:5173",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
}


class BotHandler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):  # silence default access log
        pass

    def _send(self, status: int, body: dict):
        payload = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        for k, v in CORS_HEADERS.items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(payload)

    def _body(self) -> dict:
        length = int(self.headers.get("Content-Length", 0))
        if length:
            try:
                return json.loads(self.rfile.read(length))
            except (json.JSONDecodeError, ValueError):
                return {}
        return {}

    def do_OPTIONS(self):
        self.send_response(204)
        for k, v in CORS_HEADERS.items():
            self.send_header(k, v)
        self.end_headers()

    def do_GET(self):
        path = self.path.split("?")[0]

        if path == "/health":
            ollama = ollama_health()
            self._send(200, {
                "status": "ok",
                "ollama": ollama,
                "activeJobs": sum(1 for j in _jobs.values() if j["status"] == "running"),
            })

        elif path == "/bots/status":
            self._send(200, get_all_status())

        elif path == "/bots/models":
            info = ollama_health()
            self._send(200, {"models": info.get("models", []), "running": info.get("running", False)})

        elif path == "/ollama/ps":
            self._send(200, ollama_ps())

        elif path == "/ollama/models":
            self._send(200, ollama_health())

        elif path == "/stats":
            self._send(200, sprint_stats())

        elif path == "/git/pending":
            self._send(200, git_pending_count())

        elif path == "/github/status":
            self._send(200, {"runs": github_actions_status()})

        else:
            self._send(404, {"error": f"unknown path {path}"})

    def do_POST(self):
        path = self.path.split("?")[0]
        body = self._body()

        if path == "/bots/enrich":
            count = min(int(body.get("count", 20)), 100)   # cap at 100 — local only
            # SAFETY: always "ollama" from the local server — never calls cloud APIs
            model = "ollama"
            job_id = dispatch_enrich(count=count, model=model)
            self._send(202, {"jobId": job_id, "bot": "enrich", "count": count, "model": model})

        elif path == "/bots/significance":
            count = min(int(body.get("count", 50)), 200)   # cap at 200 — local only
            model = "ollama"
            job_id = dispatch_significance(count=count, model=model)
            self._send(202, {"jobId": job_id, "bot": "significance", "count": count, "model": model})

        elif path == "/bots/queue":
            job_id = dispatch_queue()
            self._send(202, {"jobId": job_id, "bot": "queue"})

        elif path == "/bots/sync":
            max_e = int(body.get("max", 50))
            job_id = dispatch_sync(max_entities=max_e)
            self._send(202, {"jobId": job_id, "bot": "sync", "max": max_e})

        elif path == "/bots/push":
            msg = body.get("message", "")
            job_id = dispatch_git_push(message=msg)
            self._send(202, {"jobId": job_id, "bot": "git-push"})

        elif path == "/bots/sync-and-push":
            max_e = int(body.get("max", 100))
            job_id = dispatch_sync_and_push(max_entities=max_e)
            self._send(202, {"jobId": job_id, "bot": "sync-push", "max": max_e})

        elif path == "/bots/all":
            enrich_count = int(body.get("enrichCount", 20))
            sig_count = int(body.get("sigCount", 50))
            auto_push = bool(body.get("autoPush", True))
            jobs = dispatch_all(enrich_count=enrich_count, sig_count=sig_count, auto_push=auto_push)
            self._send(202, {"jobIds": jobs, "message": "All local bots deployed — auto-push enabled", "autoPush": auto_push})

        elif path == "/bots/stop":
            stopped = stop_all()
            self._send(200, {"stopped": stopped, "count": len(stopped)})

        else:
            self._send(404, {"error": f"unknown path {path}"})


# ─── Entry Point ──────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Local Bot Server — port 7474")
    parser.add_argument("--port", type=int, default=7474)
    args = parser.parse_args()

    # Load .env
    env_file = REPO_ROOT / ".env"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            k = k.strip(); v = v.strip()
            if k and k not in os.environ:
                os.environ[k] = v

    ollama_info = ollama_health()
    print(f"╔══════════════════════════════════════════════════╗")
    print(f"║     ANNALS LOCAL BOT SERVER — Port {args.port}        ║")
    print(f"╚══════════════════════════════════════════════════╝")
    print(f"  Ollama: {'✓ running' if ollama_info['running'] else '✗ offline'}")
    if ollama_info.get("models"):
        print(f"  Models: {', '.join(ollama_info['models'])}")
    print(f"  Listening on http://localhost:{args.port}")
    print(f"  CORS: http://localhost:5173")
    print(f"  Endpoints: /health /bots/status /bots/enrich /bots/significance")
    print(f"             /bots/queue /bots/sync /bots/all /bots/stop")
    print()

    server = HTTPServer(("localhost", args.port), BotHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down local bot server...")
        stop_all()


if __name__ == "__main__":
    main()
