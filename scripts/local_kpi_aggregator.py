#!/usr/bin/env python3
"""
Local KPI Aggregator — collects per-day/week/month stats from local bot runs.

Reads local_bot_status.json (written by local_bot_server.py) plus the
platform-local-bots.json roster (com.annals.* LaunchAgents) and produces:
  data/governance/bot_kpi/local_kpi.json
  data/governance/bot_kpi/combined_kpi.json
and mirrors both (plus the SoT) into ui/public/governance for the Curator UI.

Usage:
    python3 scripts/local_kpi_aggregator.py
    python3 scripts/local_kpi_aggregator.py --days 90
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
from datetime import datetime, timezone, timedelta
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
STATUS_FILE = REPO / "data" / "enrichment" / "local_bot_status.json"
SOT_FILE = REPO / "data" / "governance" / "platform-local-bots.json"
KPI_OUT = REPO / "data" / "governance" / "bot_kpi" / "local_kpi.json"
COMBINED_OUT = REPO / "data" / "governance" / "bot_kpi" / "combined_kpi.json"
PUBLIC_GOV = REPO / "ui" / "public" / "governance"
PUBLIC_KPI = PUBLIC_GOV / "bot_kpi"
LOG_DIR = Path.home() / "Library" / "Logs" / "annals-bots"

# HTTP bot-server historically used "git-push"; LaunchAgent id is "push"
TASK_ALIASES = {
    "git-push": "push",
    "sync-and-push": "push",
    "ollama-enrich": "enrich",
    "ollama-significance": "significance",
    "edges": "edges-extract",
}


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_date(iso: str | None) -> datetime | None:
    if not iso:
        return None
    for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d"):
        try:
            return datetime.strptime(iso.replace("+00:00", "Z"), fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    try:
        return datetime.fromisoformat(iso.replace("Z", "+00:00")).astimezone(timezone.utc)
    except Exception:
        return None


def normalize_task(task: str | None) -> str:
    raw = (task or "unknown").strip()
    return TASK_ALIASES.get(raw, raw)


def load_sot() -> dict:
    if not SOT_FILE.exists():
        return {"bots": [], "meta": {}}
    try:
        return json.loads(SOT_FILE.read_text())
    except Exception:
        return {"bots": [], "meta": {}}


def load_local_jobs() -> list[dict]:
    if not STATUS_FILE.exists():
        return []
    try:
        raw = json.loads(STATUS_FILE.read_text())
        return list(raw.values()) if isinstance(raw, dict) else []
    except Exception:
        return []


def log_mtime_iso(bot_id: str) -> str | None:
    path = LOG_DIR / f"{bot_id}.log"
    if not path.exists():
        return None
    try:
        ts = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
        return ts.strftime("%Y-%m-%dT%H:%M:%SZ")
    except Exception:
        return None


def roster_snapshot(sot: dict, jobs: list[dict]) -> list[dict]:
    """One row per com.annals.* bot: schedule + last seen job/log signal."""
    latest_by_bot: dict[str, dict] = {}
    for job in jobs:
        bot = normalize_task(job.get("bot"))
        started = parse_date(job.get("started"))
        prev = latest_by_bot.get(bot)
        prev_started = parse_date(prev.get("started")) if prev else None
        if not prev or (started and (not prev_started or started > prev_started)):
            latest_by_bot[bot] = job

    rows: list[dict] = []
    for bot in sot.get("bots") or []:
        bot_id = bot.get("id") or "unknown"
        sched = bot.get("schedule") or {}
        latest = latest_by_bot.get(bot_id)
        log_at = log_mtime_iso(bot_id)
        rows.append({
            "id": bot_id,
            "name": bot.get("name"),
            "status": bot.get("status", "active"),
            "lane": bot.get("lane"),
            "usesOllama": bool(bot.get("uses_ollama")),
            "cron": sched.get("cron") or sched.get("kind") or "",
            "scheduleEnabled": bool(sched.get("enabled", True)),
            "scheduleNote": sched.get("note"),
            "launchdLabel": (bot.get("launchd") or {}).get("label") or f"com.annals.{bot_id}",
            "lastJobStatus": (latest or {}).get("status"),
            "lastJobStarted": (latest or {}).get("started"),
            "lastJobFinished": (latest or {}).get("finished"),
            "lastLogAt": log_at,
        })
    return rows


def aggregate_jobs(jobs: list[dict], keep_days: int = 90) -> dict:
    """Build per-day aggregation from local job records."""
    cutoff = datetime.now(timezone.utc) - timedelta(days=keep_days)
    by_day: dict[str, dict] = {}

    for job in jobs:
        started = parse_date(job.get("started"))
        if not started or started < cutoff:
            continue
        if job.get("status") not in ("done", "error"):
            continue

        date_str = started.strftime("%Y-%m-%d")
        if date_str not in by_day:
            by_day[date_str] = {
                "date": date_str,
                "totalJobs": 0,
                "doneJobs": 0,
                "errorJobs": 0,
                "byTask": {},
            }
        d = by_day[date_str]
        d["totalJobs"] += 1
        if job.get("status") == "done":
            d["doneJobs"] += 1
        else:
            d["errorJobs"] += 1

        task = normalize_task(job.get("bot"))
        d["byTask"][task] = d["byTask"].get(task, 0) + 1

    return dict(sorted(by_day.items()))


def window_summary(by_day: dict[str, dict], days: int, roster_ids: list[str]) -> dict:
    """Sum stats over the last N days; always include known roster ids (0 ok)."""
    cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%d")
    total_jobs = done = errors = 0
    by_task: dict[str, int] = {bid: 0 for bid in roster_ids}
    for day_str, row in by_day.items():
        if day_str < cutoff:
            continue
        total_jobs += row.get("totalJobs", 0)
        done += row.get("doneJobs", 0)
        errors += row.get("errorJobs", 0)
        for task, cnt in row.get("byTask", {}).items():
            by_task[task] = by_task.get(task, 0) + cnt
    return {
        "windowDays": days,
        "totalJobs": total_jobs,
        "doneJobs": done,
        "errorJobs": errors,
        "successRate": round(done / max(1, total_jobs) * 100, 1),
        "byTask": by_task,
    }


def load_swarm_daily() -> list[dict]:
    swarm_file = REPO / "data" / "governance" / "bot_kpi" / "swarm_daily.json"
    if not swarm_file.exists():
        return []
    try:
        data = json.loads(swarm_file.read_text())
        return data.get("days", []) if isinstance(data, dict) else []
    except Exception:
        return []


def build_combined_kpi(local_by_day: dict[str, dict],
                       swarm_days: list[dict]) -> dict:
    """Merge local and cloud swarm KPIs into a single combined timeline."""
    all_dates: set[str] = set(local_by_day.keys()) | {d["date"] for d in swarm_days}
    swarm_by_date = {d["date"]: d for d in swarm_days}

    combined: list[dict] = []
    for date_str in sorted(all_dates):
        local = local_by_day.get(date_str, {})
        swarm = swarm_by_date.get(date_str, {})
        local_by_task = {
            normalize_task(k): v for k, v in (local.get("byTask") or {}).items()
        }
        combined.append({
            "date": date_str,
            "localJobs": local.get("totalJobs", 0),
            "localDone": local.get("doneJobs", 0),
            "localErrors": local.get("errorJobs", 0),
            "localByTask": local_by_task,
            # Cloud swarm kept for historical charts; Mini track is Ollama/local-first
            "swarmProcessed": swarm.get("totalProcessed", 0),
            "swarmSucceeded": swarm.get("totalSucceeded", 0),
            "swarmFailed": swarm.get("totalFailed", 0),
            "swarmEnrichment": swarm.get("enrichment", 0),
            "swarmEdges": swarm.get("edges", 0),
            "swarmSignificance": swarm.get("significance", 0),
            "swarmRespawns": swarm.get("respawns", 0),
            "grandTotal": local.get("totalJobs", 0) + swarm.get("totalProcessed", 0),
        })
    return {
        "updatedAt": now_iso(),
        "days": combined[-90:],
    }


def _safe_mirror(src: Path, dst: Path) -> None:
    """Copy unless src/dst are the same inode (symlink / hardlink layouts)."""
    if not src.exists():
        return
    try:
        if dst.exists() and src.resolve() == dst.resolve():
            return
    except Exception:
        pass
    dst.parent.mkdir(parents=True, exist_ok=True)
    try:
        shutil.copy2(src, dst)
    except shutil.SameFileError:
        return


def mirror_public(kpi: dict, combined: dict) -> None:
    PUBLIC_KPI.mkdir(parents=True, exist_ok=True)
    PUBLIC_GOV.mkdir(parents=True, exist_ok=True)
    (PUBLIC_KPI / "local_kpi.json").write_text(json.dumps(kpi, indent=2) + "\n")
    (PUBLIC_KPI / "combined_kpi.json").write_text(json.dumps(combined, indent=2) + "\n")
    _safe_mirror(SOT_FILE, PUBLIC_GOV / "platform-local-bots.json")
    _safe_mirror(
        REPO / "data" / "governance" / "cloud_merge_cursor.json",
        PUBLIC_GOV / "cloud_merge_cursor.json",
    )


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--days", type=int, default=90, help="Days of history to keep")
    args = p.parse_args()

    print(f"[local_kpi_aggregator] Loading jobs from {STATUS_FILE}")
    jobs = load_local_jobs()
    print(f"[local_kpi_aggregator] {len(jobs)} job records found")

    sot = load_sot()
    roster = roster_snapshot(sot, jobs)
    roster_ids = [r["id"] for r in roster]
    print(f"[local_kpi_aggregator] Roster: {len(roster)} com.annals.* bots")

    by_day = aggregate_jobs(jobs, keep_days=args.days)

    kpi = {
        "updatedAt": now_iso(),
        "source": "local-mac-mini",
        "labelPrefix": (sot.get("meta") or {}).get("label_prefix", "com.annals."),
        "llmProvider": "ollama",
        "totalJobsAllTime": len([j for j in jobs if j.get("status") in ("done", "error")]),
        "rosterCount": len(roster),
        "roster": roster,
        "last24h": window_summary(by_day, 1, roster_ids),
        "last7d": window_summary(by_day, 7, roster_ids),
        "last30d": window_summary(by_day, 30, roster_ids),
        "days": list(by_day.values()),
    }

    KPI_OUT.parent.mkdir(parents=True, exist_ok=True)
    KPI_OUT.write_text(json.dumps(kpi, indent=2) + "\n")
    print(f"[local_kpi_aggregator] Written → {KPI_OUT}")

    swarm_days = load_swarm_daily()
    combined = build_combined_kpi(by_day, swarm_days)
    COMBINED_OUT.write_text(json.dumps(combined, indent=2) + "\n")
    print(f"[local_kpi_aggregator] Combined KPI → {COMBINED_OUT}")
    print(f"[local_kpi_aggregator] {len(combined['days'])} days in combined timeline")

    mirror_public(kpi, combined)
    print(f"[local_kpi_aggregator] Mirrored → {PUBLIC_KPI}")


if __name__ == "__main__":
    main()
