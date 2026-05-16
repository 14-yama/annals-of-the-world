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


def _load_status():
    """Restore job registry from disk on startup so historical stats survive restarts."""
    if not STATUS_FILE.exists():
        return
    try:
        data = json.loads(STATUS_FILE.read_text())
        if not isinstance(data, dict):
            return
        # Prune jobs older than 31 days to cap file growth
        cutoff = time.time() - 86400 * 31
        pruned = {}
        for k, v in data.items():
            try:
                ts = time.mktime(time.strptime(v.get("started", ""), "%Y-%m-%dT%H:%M:%SZ"))
                if ts >= cutoff:
                    pruned[k] = v
            except Exception:
                pruned[k] = v  # keep entries with unparseable timestamps
        with _lock:
            _jobs.update(pruned)
        print(f"[status] Restored {len(pruned)} jobs from disk ({len(data) - len(pruned)} pruned >31d)")
    except Exception as e:
        print(f"[status] Could not restore status from disk: {e}")


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
    """
    Rich analytics over all jobs in the registry.
    Returns daily/weekly/monthly breakdowns, action type counts, top bots,
    and editor attribution so the UI can display comprehensive bot stats.
    """
    now = time.time()
    windows = {
        "last_24h": now - 86400,
        "last_7d":  now - 86400 * 7,
        "last_30d": now - 86400 * 30,
    }

    # Counters per time window
    totals:       dict[str, int] = {w: 0 for w in windows}
    by_bot:       dict[str, dict[str, int]] = {w: {} for w in windows}
    by_action:    dict[str, dict[str, int]] = {w: {} for w in windows}
    by_day:       dict[str, dict[str, int]] = {}      # "YYYY-MM-DD" → {bot: count}
    completed_jobs: dict[str, int] = {w: 0 for w in windows}
    failed_jobs:    dict[str, int] = {w: 0 for w in windows}
    top_performers: dict[str, int] = {}  # bot → total entities all-time

    # Infer "action" from bot name
    def _bot_to_action(bot: str) -> str:
        b = bot.lower()
        if "enrich" in b:
            return "entity_enrich"
        if "significance" in b or "sig" in b:
            return "historicalSignificance"
        if "queue" in b:
            return "queue_scan"
        if "sync" in b:
            return "appwrite_sync"
        if "push" in b:
            return "git_push"
        return "other"

    with _lock:
        for job in _jobs.values():
            try:
                started_ts = time.mktime(
                    time.strptime(job["started"], "%Y-%m-%dT%H:%M:%SZ")
                )
            except Exception:
                continue

            c = job.get("count", 0) or 0
            bot = job.get("bot", "unknown")
            action = _bot_to_action(bot)
            day_key = time.strftime("%Y-%m-%d", time.gmtime(started_ts))
            status = job.get("status", "")

            # All-time top performers
            top_performers[bot] = top_performers.get(bot, 0) + c

            # Per-day breakdown (all history)
            if day_key not in by_day:
                by_day[day_key] = {}
            by_day[day_key][bot] = by_day[day_key].get(bot, 0) + c

            # Per-window counters
            for w, cutoff in windows.items():
                if started_ts < cutoff:
                    continue
                totals[w] += c
                by_bot[w][bot] = by_bot[w].get(bot, 0) + c
                by_action[w][action] = by_action[w].get(action, 0) + c
                if status == "done":
                    completed_jobs[w] += 1
                elif status == "error":
                    failed_jobs[w] += 1

    # Sort top performers descending
    ranked = sorted(top_performers.items(), key=lambda x: x[1], reverse=True)

    # Active editors derived from running/recent jobs
    active_editors: list[dict] = []
    cutoff_active = now - 3600  # last hour
    with _lock:
        for job in _jobs.values():
            try:
                started_ts = time.mktime(
                    time.strptime(job["started"], "%Y-%m-%dT%H:%M:%SZ")
                )
            except Exception:
                continue
            if started_ts >= cutoff_active or job.get("status") == "running":
                model = job.get("model", "unknown")
                env = "local"  # all jobs here are local
                active_editors.append({
                    "editorId": f"ollama/{model}·local",
                    "bot": job.get("bot"),
                    "status": job.get("status"),
                    "since": job.get("started"),
                    "env": env,
                })

    return {
        "windows": {
            "last_24h": {
                "totalEntities": totals["last_24h"],
                "byBot": by_bot["last_24h"],
                "byAction": by_action["last_24h"],
                "completedJobs": completed_jobs["last_24h"],
                "failedJobs": failed_jobs["last_24h"],
            },
            "last_7d": {
                "totalEntities": totals["last_7d"],
                "byBot": by_bot["last_7d"],
                "byAction": by_action["last_7d"],
                "completedJobs": completed_jobs["last_7d"],
                "failedJobs": failed_jobs["last_7d"],
            },
            "last_30d": {
                "totalEntities": totals["last_30d"],
                "byBot": by_bot["last_30d"],
                "byAction": by_action["last_30d"],
                "completedJobs": completed_jobs["last_30d"],
                "failedJobs": failed_jobs["last_30d"],
            },
        },
        "byDay": by_day,
        "topPerformers": [{"bot": b, "total": t} for b, t in ranked[:10]],
        "activeEditors": active_editors,
        # Legacy fields kept for backward compat
        "window": "last_24h",
        "totalEntitiesProcessed": totals["last_24h"],
        "byBot": by_bot["last_24h"],
        "completedJobs": completed_jobs["last_24h"],
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


def dispatch_enrich(count: int = 20, model: str = "ollama",
                    queue: Optional[str] = None, lenient: bool = True) -> str:
    """Dispatch AI enrichment bot locally."""
    job_id = _new_job("enrich", count=count, model=model)
    cmd = [sys.executable, str(SCRIPTS / "ai_enrich_autonomous.py"),
           "--count", str(count), "--model", model]
    if queue:
        cmd += ["--queue", queue]
    if lenient:
        cmd.append("--lenient")
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


def dispatch_sync(max_entities: int = 50, local_mode: bool = False) -> str:
    """
    Run sync_gateway.ts → push entity JSON to Appwrite + emit audit_log rows.

    local_mode=True passes --local to sync_gateway, which scans files with
    _unsyncedEdits:true instead of using git diff. Use this when enrichments
    are written to disk but not yet git-committed (the normal local-bot path).
    After --local sync completes, always follow up with dispatch_git_push() so
    the cleared _editLog state is committed back to git.
    """
    job_id = _new_job("sync", count=max_entities, model="none")

    def _run_sync(jid):
        _update_job(jid, status="running")
        log: list[str] = []
        try:
            env = {**os.environ}
            env_file = REPO_ROOT / ".env"
            if env_file.exists():
                for line in env_file.read_text().splitlines():
                    line = line.strip()
                    if not line or line.startswith("#") or "=" not in line:
                        continue
                    k, _, v = line.partition("=")
                    env[k.strip()] = v.strip()

            cmd = ["npx", "tsx", "scripts/sync_gateway.ts", f"--max={max_entities}"]
            if local_mode:
                cmd.append("--local")

            proc = subprocess.Popen(
                cmd,
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


def _wait_for_job(jid: str, poll_interval: float = 3.0):
    """Block until job jid reaches a terminal state."""
    while True:
        with _lock:
            s = _jobs.get(jid, {}).get("status", "done")
        if s in ("done", "error", "stopped"):
            return s
        time.sleep(poll_interval)


def _auto_sync_chain(bot_jids: list[str], max_entities: int = 100):
    """
    Called in a background thread after enrich/significance jobs complete.
    Mirrors the GitHub Actions pipeline:
      1. Wait for all bot jobs to finish
      2. --local sync → Appwrite (reads _unsyncedEdits files directly)
      3. git commit + push (saves cleared _editLog + triggers GH Actions for any remaining)

    This makes local bots fully autonomous — no human needed to push.
    """
    for jid in bot_jids:
        _wait_for_job(jid)

    # Step 1: sync dirty files → Appwrite (--local mode reads _unsyncedEdits)
    sync_jid = dispatch_sync(max_entities=max_entities, local_mode=True)
    _wait_for_job(sync_jid)

    # Step 2: git commit + push (commits cleared _editLog + any new enrichments)
    push_jid = dispatch_git_push()
    _wait_for_job(push_jid)


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


def _trigger_cloud_enrichment(branch: str = "clean/audit-system"):
    """
    Trigger the cloud AI enrichment workflow via GitHub Actions workflow_dispatch.
    Only runs if GITHUB_TOKEN is set in environment. Safe to call after every
    local push — GitHub Actions deduplicates runs if already in progress.
    """
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        return  # no token = local-only mode, skip silently
    url = f"https://api.github.com/repos/{GITHUB_REPO}/actions/workflows/ai-enrichment.yml/dispatches"
    payload = json.dumps({"ref": branch}).encode()
    headers_gh = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "Content-Type": "application/json",
    }
    try:
        req = urllib.request.Request(url, data=payload, headers=headers_gh, method="POST")
        with urllib.request.urlopen(req, timeout=10):
            print(f"[github] Triggered ai-enrichment.yml on {branch} via workflow_dispatch")
    except Exception as e:
        print(f"[github] Could not trigger cloud workflow: {e}")


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
            # Optionally trigger cloud enrichment on GitHub Actions (needs GITHUB_TOKEN)
            threading.Thread(target=_trigger_cloud_enrichment, daemon=True).start()
        except Exception as exc:
            _update_job(jid, status="error",
                        log=log + [f"Exception: {exc}", traceback.format_exc()],
                        finished=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))

    t = threading.Thread(target=_run, args=(job_id,), daemon=True)
    t.start()
    return job_id



def dispatch_sync_and_push(max_entities: int = 100) -> str:
    """
    Local Appwrite sync + git push.
    Uses --local mode (reads _unsyncedEdits files) then commits cleared state to git.
    This is the autonomous completion step for local bots.
    """
    job_id = _new_job("sync-push", count=max_entities, model="none")

    def _run(jid: str):
        _update_job(jid, status="running")
        # Step 1: local-mode sync → Appwrite (reads dirty _unsyncedEdits files)
        sync_jid = dispatch_sync(max_entities=max_entities, local_mode=True)
        _wait_for_job(sync_jid)
        # Step 2: git commit+push (cleared _editLog + new enrichments)
        push_jid = dispatch_git_push()
        _wait_for_job(push_jid)
        _update_job(jid, status="done", exitCode=0,
                    finished=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))

    t = threading.Thread(target=_run, args=(job_id,), daemon=True)
    t.start()
    return job_id


def dispatch_all(enrich_count: int = 20, sig_count: int = 50, auto_push: bool = True) -> list[str]:
    """
    Assist All — mirrors GitHub Actions pipeline locally.
    Flow: queue → enrich + significance (parallel, Ollama) → --local sync → Appwrite
          → git commit+push → GH Actions picks up any overflow.

    Safe to run concurrently with GitHub Actions cloud bots. Each targets
    different entity files. Merge conflicts resolved by sync_gateway.
    """
    jobs: list[str] = []
    jobs.append(dispatch_queue())
    enrich_jid = dispatch_enrich(count=enrich_count, model="ollama", lenient=True)
    sig_jid = dispatch_significance(count=sig_count, model="ollama")
    jobs.extend([enrich_jid, sig_jid])

    if auto_push:
        chain_jids = [enrich_jid, sig_jid]
        t = threading.Thread(
            target=_auto_sync_chain,
            args=(chain_jids, max(enrich_count * 3, 100)),
            daemon=True,
        )
        t.start()

    return jobs


# ─── Autonomous Watchdog ───────────────────────────────────────────────────────
# Background thread that periodically checks for:
#  1. Uncommitted dirty enrichments (written to disk but not git-committed)
#     → runs --local sync → Appwrite → git commit+push
# This ensures bots are fully autonomous even if they crash mid-run.

_watchdog_running = False

def _watchdog_loop(interval_seconds: int = 300):
    """
    Autonomous watchdog: every `interval_seconds` (default 5 min),
    check for dirty enrichments and sync them without human intervention.
    Same behaviour as GitHub Actions sync-gateway: always-on, zero human touch.
    """
    global _watchdog_running
    _watchdog_running = True
    print(f"[watchdog] Started — scanning every {interval_seconds}s for dirty enrichments")
    while _watchdog_running:
        time.sleep(interval_seconds)
        # Skip if any sync/push job is already running
        with _lock:
            busy = any(j["status"] == "running" and j["bot"] in ("sync", "sync-push", "git-push")
                       for j in _jobs.values())
        if busy:
            continue
        # Check for _unsyncedEdits files
        dirty_count = _count_dirty_files()
        if dirty_count > 0:
            print(f"[watchdog] Found {dirty_count} dirty files — launching autonomous sync+push")
            sync_jid = dispatch_sync(max_entities=200, local_mode=True)
            _wait_for_job(sync_jid)
            dispatch_git_push(message=f"feat(enrich): watchdog auto-push — {dirty_count} local enrichments")


def _count_dirty_files() -> int:
    """Count entity files with _unsyncedEdits:true in detailsJson."""
    count = 0
    if not (REPO_ROOT / "data" / "appwrite-export" / "entities").exists():
        return 0
    try:
        for p in (REPO_ROOT / "data" / "appwrite-export" / "entities").rglob("*.json"):
            try:
                data = json.loads(p.read_text())
                for ent in data.get("entities", []):
                    dj_raw = ent.get("detailsJson", "")
                    if isinstance(dj_raw, str) and dj_raw:
                        try:
                            dj = json.loads(dj_raw)
                            if dj.get("_unsyncedEdits") or (isinstance(dj.get("_editLog"), list) and dj["_editLog"]):
                                count += 1
                                break
                        except Exception:
                            pass
            except Exception:
                pass
    except Exception:
        pass
    return count


def start_watchdog(interval_seconds: int = 300):
    t = threading.Thread(target=_watchdog_loop, args=(interval_seconds,), daemon=True)
    t.start()



# CORS allows any localhost port so the UI works on :5173, :5174, etc.
_CORS_BASE = {
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
}


def _cors_origin(request_origin: str) -> str:
    """Allow any http://localhost:<port> origin."""
    if request_origin and request_origin.startswith("http://localhost:"):
        return request_origin
    return "http://localhost:5173"   # safe fallback


class BotHandler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):  # silence default access log
        pass

    def _cors_headers(self) -> dict:
        origin = self.headers.get("Origin", "http://localhost:5173")
        return {"Access-Control-Allow-Origin": _cors_origin(origin), **_CORS_BASE}

    def _send(self, status: int, body: dict):
        payload = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        for k, v in self._cors_headers().items():
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
        for k, v in self._cors_headers().items():
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
            queue = body.get("queue") or None   # e.g. "data/enrichment/queue_ollama_a.json"
            lenient = bool(body.get("lenient", True))
            job_id = dispatch_enrich(count=count, model=model, queue=queue, lenient=lenient)
            self._send(202, {"jobId": job_id, "bot": "enrich", "count": count, "model": model, "queue": queue, "lenient": lenient})

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

    # Restore historical job data from disk so 24h/7d/30d stats survive restarts
    _load_status()

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
    print(f"  CORS: any http://localhost:* origin (works on any Vite port)")
    print(f"  Endpoints: /health /bots/status /bots/enrich /bots/significance")
    print(f"             /bots/queue /bots/sync /bots/all /bots/stop")
    print(f"  Watchdog: auto-sync every 5 min (autonomous — no human needed)")
    print()

    # Start autonomous watchdog — checks for dirty enrichments every 5 minutes
    # and syncs them to Appwrite without human intervention (mirrors GH Actions)
    start_watchdog(interval_seconds=300)

    server = HTTPServer(("localhost", args.port), BotHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down local bot server...")
        stop_all()


if __name__ == "__main__":
    main()
