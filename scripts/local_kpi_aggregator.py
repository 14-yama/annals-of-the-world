#!/usr/bin/env python3
"""
Local KPI Aggregator — collects per-day/week/month stats from local bot runs.

Reads local_bot_status.json (written by local_bot_server.py) and produces
data/governance/bot_kpi/local_kpi.json with rolling time-window summaries.

Run automatically via cron or from the daemon loop. Also called by the
watchdog to keep the KPI file fresh.

Usage:
    python3 scripts/local_kpi_aggregator.py
    python3 scripts/local_kpi_aggregator.py --days 90  (keep N days of history)
"""
from __future__ import annotations

import argparse
import json
import os
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

REPO          = Path(__file__).resolve().parent.parent
STATUS_FILE   = REPO / "data" / "enrichment" / "local_bot_status.json"
KPI_OUT       = REPO / "data" / "governance" / "bot_kpi" / "local_kpi.json"
COMBINED_OUT  = REPO / "data" / "governance" / "bot_kpi" / "combined_kpi.json"
KPI_OUT.parent.mkdir(parents=True, exist_ok=True)


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_date(iso: str | None) -> datetime | None:
    if not iso:
        return None
    for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d"):
        try:
            return datetime.strptime(iso, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def load_local_jobs() -> list[dict]:
    if not STATUS_FILE.exists():
        return []
    try:
        raw = json.loads(STATUS_FILE.read_text())
        return list(raw.values()) if isinstance(raw, dict) else []
    except Exception:
        return []


def aggregate_jobs(jobs: list[dict], keep_days: int = 90) -> dict:
    """Build per-day aggregation from local job records."""
    cutoff = datetime.now(timezone.utc) - timedelta(days=keep_days)
    by_day: dict[str, dict] = {}

    for job in jobs:
        started = parse_date(job.get("started"))
        if not started or started < cutoff:
            continue
        if job.get("status") not in ("done", "error"):
            continue   # skip in-progress jobs

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

        task = job.get("bot", "unknown")
        d["byTask"][task] = d["byTask"].get(task, 0) + 1

    return dict(sorted(by_day.items()))


def window_summary(by_day: dict[str, dict], days: int) -> dict:
    """Sum stats over the last N days."""
    cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%d")
    total_jobs = done = errors = 0
    by_task: dict[str, int] = {}
    for day_str, row in by_day.items():
        if day_str < cutoff:
            continue
        total_jobs += row.get("totalJobs", 0)
        done       += row.get("doneJobs", 0)
        errors     += row.get("errorJobs", 0)
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
        combined.append({
            "date": date_str,
            # Local bot totals
            "localJobs":      local.get("totalJobs", 0),
            "localDone":      local.get("doneJobs", 0),
            "localErrors":    local.get("errorJobs", 0),
            "localByTask":    local.get("byTask", {}),
            # Cloud swarm totals
            "swarmProcessed": swarm.get("totalProcessed", 0),
            "swarmSucceeded": swarm.get("totalSucceeded", 0),
            "swarmFailed":    swarm.get("totalFailed", 0),
            "swarmEnrichment":swarm.get("enrichment", 0),
            "swarmEdges":     swarm.get("edges", 0),
            "swarmSignificance": swarm.get("significance", 0),
            "swarmRespawns":  swarm.get("respawns", 0),
            # Grand total
            "grandTotal": local.get("totalJobs", 0) + swarm.get("totalProcessed", 0),
        })
    return {
        "updatedAt": now_iso(),
        "days": combined[-90:],  # keep last 90 days
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--days", type=int, default=90, help="Days of history to keep")
    args = p.parse_args()

    print(f"[local_kpi_aggregator] Loading jobs from {STATUS_FILE}")
    jobs = load_local_jobs()
    print(f"[local_kpi_aggregator] {len(jobs)} job records found")

    by_day = aggregate_jobs(jobs, keep_days=args.days)

    kpi = {
        "updatedAt":  now_iso(),
        "totalJobsAllTime": len([j for j in jobs if j.get("status") in ("done", "error")]),
        "last24h":    window_summary(by_day, 1),
        "last7d":     window_summary(by_day, 7),
        "last30d":    window_summary(by_day, 30),
        "days":       list(by_day.values()),
    }

    KPI_OUT.write_text(json.dumps(kpi, indent=2))
    print(f"[local_kpi_aggregator] Written → {KPI_OUT}")

    # Build and write combined KPI
    swarm_days = load_swarm_daily()
    combined = build_combined_kpi(by_day, swarm_days)
    COMBINED_OUT.write_text(json.dumps(combined, indent=2))
    print(f"[local_kpi_aggregator] Combined KPI → {COMBINED_OUT}")
    print(f"[local_kpi_aggregator] {len(combined['days'])} days in combined timeline")


if __name__ == "__main__":
    main()
