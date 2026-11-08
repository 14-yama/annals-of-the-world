#!/usr/bin/env python3
"""
Local KPI Aggregator — collects per-day/week/month stats from local bot runs.

Reads local_bot_status.json (written by local_bot_server.py) plus the
platform-local-bots.json roster (com.annals.* LaunchAgents) and produces:
  data/governance/bot_kpi/local_kpi.json
  data/governance/bot_kpi/combined_kpi.json
and mirrors both (plus the SoT) into ui/public/governance for the Curator UI.

Superstack-style processed-volume windows (1h / week / month / YTD):
headline cards count enrich + significance *successes* only (ENRICHED / scored).
Sync / merge / queue are reported separately as opsProcessed so they cannot
inflate entity throughput. Calendar month/YTD use America/Port_of_Spain.

Usage:
    python3 scripts/local_kpi_aggregator.py
    python3 scripts/local_kpi_aggregator.py --days 90
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
from datetime import datetime, timezone, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

REPO = Path(__file__).resolve().parent.parent
STATUS_FILE = REPO / "data" / "enrichment" / "local_bot_status.json"
SOT_FILE = REPO / "data" / "governance" / "platform-local-bots.json"
KPI_OUT = REPO / "data" / "governance" / "bot_kpi" / "local_kpi.json"
COMBINED_OUT = REPO / "data" / "governance" / "bot_kpi" / "combined_kpi.json"
PUBLIC_GOV = REPO / "ui" / "public" / "governance"
PUBLIC_KPI = PUBLIC_GOV / "bot_kpi"
LOG_DIR = Path.home() / "Library" / "Logs" / "annals-bots"
AUDIT_DIR = REPO / "data" / "audit-reports"
ENRICH_DIR = REPO / "data" / "enrichment"
GOV_DIR = REPO / "data" / "governance"
POS_TZ = ZoneInfo("America/Port_of_Spain")

# HTTP bot-server historically used "git-push"; LaunchAgent id is "push"
TASK_ALIASES = {
    "git-push": "push",
    "sync-and-push": "push",
    "ollama-enrich": "enrich",
    "ollama-significance": "significance",
    "edges": "edges-extract",
}

# Headline "Processed volume" = real LLM entity work only.
ENRICHMENT_TASKS = frozenset({
    "enrich", "enrich-b", "enrich-c", "significance",
    "enrich-grok", "enrich-grok-b", "significance-grok",
})
# Infrastructure / ops — shown separately so sync/merge don't inflate enrich KPIs.
OPS_TASKS = frozenset({
    "sync", "merge-cloud", "merge-cloud-audit", "seed-local", "push",
    "queue", "kpi", "stats-cache", "healthcheck", "bot-server",
    "edges-extract", "edges-extract-b", "edges-grok",
})

# Audit report filename → bot task id
AUDIT_TASK_MAP = {
    "stats.json": "audit-stats",
    "completeness.json": "audit-completeness",
    "orphans.json": "audit-orphans",
    "consistency.json": "audit-consistency",
    "duplicates.json": "audit-duplicates",
    "classification.json": "audit-classification",
    "edge_run.json": "edges-extract",
    "significance_run.json": "significance",
}

# Superstack LocalBotsKpiPage windows adapted for Annals: 1h / week / month / YTD
VOLUME_WINDOWS = (
    {"id": "1h", "label": "Last hour", "kind": "rolling", "ms": 60 * 60 * 1000},
    {"id": "week", "label": "Last week", "kind": "rolling", "ms": 7 * 24 * 60 * 60 * 1000},
    {"id": "month", "label": "Month to date", "kind": "calendar_month"},
    {"id": "ytd", "label": "Year to date", "kind": "calendar_ytd"},
)


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_date(iso: str | None) -> datetime | None:
    if not iso:
        return None
    raw = str(iso).strip()
    for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d"):
        try:
            return datetime.strptime(raw.replace("+00:00", "Z"), fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    try:
        return datetime.fromisoformat(raw.replace("Z", "+00:00")).astimezone(timezone.utc)
    except Exception:
        return None


def normalize_task(task: str | None) -> str:
    raw = (task or "unknown").strip()
    return TASK_ALIASES.get(raw, raw)


def load_json(path: Path) -> dict | list | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text())
    except Exception:
        return None


def load_sot() -> dict:
    data = load_json(SOT_FILE)
    return data if isinstance(data, dict) else {"bots": [], "meta": {}}


def load_local_jobs() -> list[dict]:
    raw = load_json(STATUS_FILE)
    if isinstance(raw, dict):
        return list(raw.values())
    if isinstance(raw, list):
        return raw
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
            "usesGrok": bool(bot.get("uses_grok")),
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


def _job_log_text(job: dict) -> str:
    log = job.get("log")
    if isinstance(log, list):
        return "\n".join(str(x) for x in log)
    if isinstance(log, str):
        return log
    return ""


def job_processed_count(job: dict) -> int:
    """
    Honest success count for one finished job.

    Prefer actual successes from logs / result fields over requested --count
    or sync write caps (those previously inflated Processed volume with
    sync/merge bursts while enrich was at 0/hr).
    """
    task = normalize_task(job.get("bot"))
    text = _job_log_text(job)

    if task in ("enrich", "enrich-b", "enrich-c", "enrich-grok", "enrich-grok-b"):
        m = re.search(r"RESULTS:\s*(\d+)\s+enriched", text)
        if m:
            return int(m.group(1))
        enriched_lines = len(re.findall(r"^\s*ENRICHED\b", text, flags=re.M))
        if enriched_lines:
            return enriched_lines
        # Zero successes (all SKIP already enriched) must count as 0, not --count.
        if "SKIP — already enriched" in text or "RESULTS: 0 enriched" in text:
            return 0
        return 0

    if task in ("significance", "significance-grok"):
        m = re.search(r"RESULTS:\s*(\d+)\s+scored", text)
        if m:
            return int(m.group(1))
        if "Found 0 enriched entities needing significance" in text:
            return 0
        return 0

    if task == "sync":
        m = re.search(r'"entitiesUpserted"\s*:\s*(\d+)', text)
        if m:
            return int(m.group(1))
        return 0

    if task in ("merge-cloud", "merge-cloud-audit"):
        # Prefer docs actually created; never count skipped-as-existing as work.
        for pat in (
            r"\bcreated[=:\s]+(\d+)",
            r'"created"\s*:\s*(\d+)',
            r"Created\s+(\d+)",
        ):
            m = re.search(pat, text, flags=re.I)
            if m:
                return int(m.group(1))
        return 0

    if task == "queue":
        # One queue refresh = 1 ops unit (not the 1200–2500 candidate list size).
        return 1 if job.get("status") == "done" else 0

    if task in ("push", "kpi", "stats-cache", "healthcheck", "seed-local"):
        return 1 if job.get("status") == "done" else 0

    # Unknown bots: 1 unit per finished job — never trust requested batch size.
    return 1 if job.get("status") in ("done", "error") else 0


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
                "processed": 0,
                "byTask": {},
                "processedByTask": {},
            }
        d = by_day[date_str]
        d["totalJobs"] += 1
        processed = job_processed_count(job)
        d["processed"] += processed
        if job.get("status") == "done":
            d["doneJobs"] += 1
        else:
            d["errorJobs"] += 1

        task = normalize_task(job.get("bot"))
        d["byTask"][task] = d["byTask"].get(task, 0) + 1
        d["processedByTask"][task] = d["processedByTask"].get(task, 0) + processed

    return dict(sorted(by_day.items()))


def window_summary(by_day: dict[str, dict], days: int, roster_ids: list[str]) -> dict:
    """Sum stats over the last N days; always include known roster ids (0 ok)."""
    cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%d")
    total_jobs = done = errors = processed = 0
    by_task: dict[str, int] = {bid: 0 for bid in roster_ids}
    processed_by_task: dict[str, int] = {bid: 0 for bid in roster_ids}
    for day_str, row in by_day.items():
        if day_str < cutoff:
            continue
        total_jobs += row.get("totalJobs", 0)
        done += row.get("doneJobs", 0)
        errors += row.get("errorJobs", 0)
        processed += row.get("processed", 0)
        for task, cnt in row.get("byTask", {}).items():
            by_task[task] = by_task.get(task, 0) + cnt
        for task, cnt in row.get("processedByTask", {}).items():
            processed_by_task[task] = processed_by_task.get(task, 0) + cnt
    return {
        "windowDays": days,
        "totalJobs": total_jobs,
        "doneJobs": done,
        "errorJobs": errors,
        "processed": processed,
        "successRate": round(done / max(1, total_jobs) * 100, 1),
        "byTask": by_task,
        "processedByTask": processed_by_task,
    }


def _audit_processed(path: Path, data: dict) -> int:
    """
    Volume for an audit/run artifact.

    Full-corpus audit reports (stats/consistency/…) historically scanned ~392K
    file-export rows. Counting those as processed would drown Mini-track KPIs.
    Treat each audit pass as 1 ops unit unless it's a small incremental run
    with real success counters (edges / significance scored).
    """
    name = path.name
    if name in ("edge_run.json", "significance_run.json"):
        summary = data.get("summary") if isinstance(data.get("summary"), dict) else {}
        for key in ("entities_scored", "new_edges", "enriched", "scored"):
            val = summary.get(key)
            if isinstance(val, (int, float)) and val >= 0:
                # Prefer real success counters; allow 0 (honest empty run).
                if key in ("entities_scored", "new_edges", "enriched", "scored"):
                    if val > 0 or key in data or key in summary:
                        return int(val)
        for key in ("enriched", "total_new_edges", "scored"):
            val = data.get(key)
            if isinstance(val, (int, float)) and val > 0:
                return int(val)
        # Never fall back to count_requested — that was the inflation bug.
        return 0
    return 1


def _artifact_success_count(data: dict, success_keys: tuple[str, ...]) -> int:
    """Pick the first real success counter; never count_requested / attempted."""
    summary = data.get("summary") if isinstance(data.get("summary"), dict) else {}
    for key in success_keys:
        for src in (data, summary):
            val = src.get(key)
            if isinstance(val, (int, float)) and val >= 0 and key in src:
                return int(val)
    # entities list with status markers
    ents = data.get("entities")
    if isinstance(ents, list) and ents:
        ok = sum(
            1 for e in ents
            if isinstance(e, dict) and e.get("status") in ("enriched", "scored", "success", "ok")
        )
        if ok:
            return ok
    return 0


def collect_launchd_log_events(
    seen_keys: set[str],
    prior_events: list[dict],
) -> list[dict]:
    """
    Parse ~/Library/Logs/annals-bots/{enrich,enrich-b,significance}.log for
    RESULTS lines. LaunchAgents often don't write local_bot_status.json, so
    without this enrich/sig can look like 0 while logs show real work.
    """
    out: list[dict] = []
    specs = (
        ("enrich", "enrich.log", r"RESULTS:\s*(\d+)\s+enriched"),
        ("enrich-b", "enrich-b.log", r"RESULTS:\s*(\d+)\s+enriched"),
        ("enrich-c", "enrich-c.log", r"RESULTS:\s*(\d+)\s+enriched"),
        ("enrich-grok", "enrich-grok.log", r"RESULTS:\s*(\d+)\s+enriched"),
        ("enrich-grok-b", "enrich-grok-b.log", r"RESULTS:\s*(\d+)\s+enriched"),
        ("significance", "significance.log", r"RESULTS:\s*(\d+)\s+scored"),
        ("significance-grok", "significance-grok.log", r"RESULTS:\s*(\d+)\s+scored"),
        ("edges-extract", "edges-extract.log", r"(?:Wrote|saved|new edges)[^\d]*(\d+)"),
        ("edges-grok", "edges-grok.log", r"(?:Wrote|saved|new edges|accepted)[^\d]*(\d+)"),
    )
    start_re = re.compile(
        r"\[annals-launchd\] start (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) "
    )
    for task, fname, result_pat in specs:
        path = LOG_DIR / fname
        if not path.exists():
            continue
        try:
            text = path.read_text(errors="replace")
        except Exception:
            continue
        current_start: datetime | None = None
        for line in text.splitlines():
            sm = start_re.search(line)
            if sm:
                try:
                    # Logs are local AST wall clock without tz — treat as POS.
                    naive = datetime.strptime(sm.group(1), "%Y-%m-%d %H:%M:%S")
                    current_start = naive.replace(tzinfo=POS_TZ).astimezone(timezone.utc)
                except ValueError:
                    current_start = None
                continue
            rm = re.search(result_pat, line)
            if not rm or not current_start:
                continue
            processed = int(rm.group(1))
            eid = (
                f"launchd:{task}:{current_start.strftime('%Y%m%d%H%M%S')}:"
                f"{processed}"
            )
            if eid in seen_keys:
                continue
            # Skip if a status-file job already covers this minute (no double-count).
            minute = current_start.strftime("%Y-%m-%dT%H:%M")
            if any(
                e.get("task") == task
                and e.get("source") == "local_bot_status"
                and str(e.get("at", ""))[:16] == minute
                for e in prior_events
            ):
                continue
            seen_keys.add(eid)
            out.append({
                "at": current_start.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "task": task,
                "processed": processed,
                "jobs": 1,
                "done": 1,
                "error": 0,
                "source": "launchd_log",
                "id": eid,
            })
    return out


def collect_volume_events(jobs: list[dict]) -> list[dict]:
    """
    Authoritative processed-entry stream for Superstack-style windows.
    Primary: finished local_bot_status jobs.
    Secondary: audit/enrichment/governance artifacts (fills gaps + first-entry history).
    """
    events: list[dict] = []
    seen_keys: set[str] = set()

    for job in jobs:
        if job.get("status") not in ("done", "error"):
            continue
        started = parse_date(job.get("started")) or parse_date(job.get("finished"))
        if not started:
            continue
        task = normalize_task(job.get("bot"))
        key = f"job:{job.get('job_id') or started.isoformat()}:{task}"
        if key in seen_keys:
            continue
        seen_keys.add(key)
        events.append({
            "at": started.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "task": task,
            "processed": job_processed_count(job),
            "jobs": 1,
            "done": 1 if job.get("status") == "done" else 0,
            "error": 1 if job.get("status") == "error" else 0,
            "source": "local_bot_status",
            "id": key,
        })

    # Launchd logs — primary for enrich/sig successes when status JSON is sparse
    events.extend(collect_launchd_log_events(seen_keys, events))

    # Enrichment / significance / edge run snapshots (success counters only)
    for name, task, success_keys in (
        ("last_run.json", "enrich", ("enriched", "succeeded")),
        ("significance_run.json", "significance", ("scored", "enriched", "entities_scored")),
        ("edge_run.json", "edges-extract", ("total_new_edges", "new_edges", "gemini_generated")),
    ):
        path = ENRICH_DIR / name
        data = load_json(path)
        if not isinstance(data, dict):
            continue
        at = parse_date(
            data.get("timestamp") or data.get("generatedAt") or data.get("generated_at")
        )
        if not at:
            continue
        processed = _artifact_success_count(data, success_keys)
        eid = f"artifact:{name}:{at.strftime('%Y%m%d%H%M%S')}"
        if eid in seen_keys:
            continue
        # Skip if a job of same task already covers this minute (avoid double-count)
        minute = at.strftime("%Y-%m-%dT%H:%M")
        if any(
            e["task"] == task
            and e["source"] in ("local_bot_status", "launchd_log")
            and e["at"][:16] == minute
            for e in events
        ):
            continue
        seen_keys.add(eid)
        events.append({
            "at": at.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "task": task,
            "processed": processed,
            "jobs": 1,
            "done": 1,
            "error": 0,
            "source": "enrichment_artifact",
            "id": eid,
        })

    # Audit reports on disk
    if AUDIT_DIR.exists():
        for path in sorted(AUDIT_DIR.glob("*.json")):
            task = AUDIT_TASK_MAP.get(path.name)
            if not task:
                continue
            data = load_json(path)
            if not isinstance(data, dict):
                continue
            at = parse_date(data.get("generatedAt") or data.get("timestamp"))
            if not at:
                continue
            eid = f"audit:{path.name}:{at.strftime('%Y%m%d%H%M%S')}"
            if eid in seen_keys:
                continue
            seen_keys.add(eid)
            events.append({
                "at": at.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "task": task,
                "processed": _audit_processed(path, data),
                "jobs": 1,
                "done": 1,
                "error": 0,
                "source": "audit_report",
                "id": eid,
            })

    # Governance cursors / sync — ops only; created/upserted successes, never skips
    merge = load_json(GOV_DIR / "cloud_merge_cursor.json")
    if isinstance(merge, dict):
        at = parse_date(merge.get("lastRunAt"))
        if at:
            processed = int(merge.get("created") or 0)
            eid = f"gov:cloud_merge_cursor:{at.strftime('%Y%m%d%H%M%S')}"
            if eid not in seen_keys and not any(
                e["task"] == "merge-cloud" and e["source"] == "local_bot_status"
                and e["at"][:13] == at.strftime("%Y-%m-%dT%H")
                for e in events
            ):
                seen_keys.add(eid)
                events.append({
                    "at": at.strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "task": "merge-cloud",
                    "processed": processed,
                    "jobs": 1,
                    "done": 1 if int(merge.get("failed") or 0) == 0 else 0,
                    "error": 1 if int(merge.get("failed") or 0) > 0 else 0,
                    "source": "governance",
                    "id": eid,
                })

    sync = load_json(GOV_DIR / "last_sync.json")
    if isinstance(sync, dict):
        at = parse_date(sync.get("lastRunAt"))
        if at:
            stats = sync.get("lastRunStats") if isinstance(sync.get("lastRunStats"), dict) else {}
            processed = int(stats.get("entitiesUpserted") or 0)
            eid = f"gov:last_sync:{at.strftime('%Y%m%d%H%M%S')}"
            if eid not in seen_keys and not any(
                e["task"] == "sync" and e["source"] == "local_bot_status"
                and e["at"][:13] == at.strftime("%Y-%m-%dT%H")
                for e in events
            ):
                seen_keys.add(eid)
                events.append({
                    "at": at.strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "task": "sync",
                    "processed": processed,
                    "jobs": 1,
                    "done": 1 if sync.get("lastRunStatus") in (None, "ok", "success") else 0,
                    "error": 0 if sync.get("lastRunStatus") in (None, "ok", "success") else 1,
                    "source": "governance",
                    "id": eid,
                })

    # Queue refresh = 1 ops unit (not the candidate list size)
    queue = load_json(ENRICH_DIR / "queue.json")
    if isinstance(queue, dict):
        at = parse_date(queue.get("generated"))
        if at:
            eid = f"queue:{at.strftime('%Y%m%d%H%M%S')}"
            if eid not in seen_keys:
                seen_keys.add(eid)
                events.append({
                    "at": at.strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "task": "queue",
                    "processed": 1,
                    "jobs": 1,
                    "done": 1,
                    "error": 0,
                    "source": "enrichment_artifact",
                    "id": eid,
                })

    events.sort(key=lambda e: e["at"])
    return events


def first_entry_date(events: list[dict], jobs: list[dict]) -> datetime | None:
    """Earliest enrichment activity — don't let ops-only artifacts set firstEntry."""
    stamps: list[datetime] = []
    for e in events:
        if e.get("task") not in ENRICHMENT_TASKS:
            continue
        dt = parse_date(e.get("at"))
        if dt:
            stamps.append(dt)
    if not stamps:
        # Fall back to any event if enrichment history is empty
        for e in events:
            dt = parse_date(e.get("at"))
            if dt:
                stamps.append(dt)
    for job in jobs:
        if normalize_task(job.get("bot")) not in ENRICHMENT_TASKS:
            continue
        for key in ("started", "finished"):
            dt = parse_date(job.get(key))
            if dt:
                stamps.append(dt)
    return min(stamps) if stamps else None


def window_cutoff(spec: dict, now: datetime, first: datetime | None) -> datetime:
    """Calendar month/YTD use America/Port_of_Spain midnight; rolling uses UTC now."""
    if spec["kind"] == "rolling":
        start = now - timedelta(milliseconds=spec["ms"])
    elif spec["kind"] == "calendar_month":
        local = now.astimezone(POS_TZ)
        start_local = local.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        start = start_local.astimezone(timezone.utc)
    elif spec["kind"] == "calendar_ytd":
        local = now.astimezone(POS_TZ)
        start_local = local.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
        start = start_local.astimezone(timezone.utc)
    else:
        start = now - timedelta(days=1)
    if first and start < first:
        return first
    return start


def _event_category(task: str) -> str:
    if task in ENRICHMENT_TASKS:
        return "enrichment"
    if task in OPS_TASKS:
        return "ops"
    return "other"


def build_processed_volume(
    events: list[dict],
    roster_ids: list[str],
    first: datetime | None,
    now: datetime | None = None,
) -> dict:
    """
    Headline cards = enrich + significance successes only.
    Ops (sync/merge/queue/…) are reported separately so they cannot inflate
    the main Processed volume numbers.
    """
    now = now or datetime.now(timezone.utc)
    windows: list[dict] = []
    for spec in VOLUME_WINDOWS:
        start = window_cutoff(spec, now, first)
        in_window = [
            e for e in events
            if (dt := parse_date(e.get("at"))) and dt >= start
        ]
        by_task: dict[str, int] = {bid: 0 for bid in roster_ids}
        jobs_by_task: dict[str, int] = {bid: 0 for bid in roster_ids}
        by_category = {"enrichment": 0, "ops": 0, "other": 0}
        enrichment = enrichment_jobs = ops = ops_jobs = 0
        done = errors = 0

        for e in in_window:
            task = e["task"]
            n = int(e.get("processed") or 0)
            j = int(e.get("jobs") or 0)
            cat = _event_category(task)
            by_category[cat] = by_category.get(cat, 0) + n
            by_task[task] = by_task.get(task, 0) + n
            jobs_by_task[task] = jobs_by_task.get(task, 0) + j
            done += int(e.get("done") or 0)
            errors += int(e.get("error") or 0)
            if cat == "enrichment":
                enrichment += n
                enrichment_jobs += j
            elif cat == "ops":
                ops += n
                ops_jobs += j

        recorded = enrichment_jobs > 0 or enrichment > 0 or ops_jobs > 0
        windows.append({
            "id": spec["id"],
            "label": spec["label"],
            "kind": spec["kind"],
            "recorded": recorded,
            # Headline = enrichment work only (honest)
            "processed": enrichment,
            "jobs": enrichment_jobs,
            "enrichmentProcessed": enrichment,
            "enrichmentJobs": enrichment_jobs,
            "opsProcessed": ops,
            "opsJobs": ops_jobs,
            "doneJobs": done,
            "errorJobs": errors,
            "successRate": 100.0 if enrichment > 0 or enrichment_jobs > 0 else (
                round(done / max(1, ops_jobs) * 100, 1) if ops_jobs else 0.0
            ),
            "byTask": by_task,
            "jobsByTask": jobs_by_task,
            "byCategory": by_category,
            "metric": "enrichment",
            "metricNote": "enrich + significance entity successes",
            "windowStart": start.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "windowEnd": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "timezone": "America/Port_of_Spain",
        })

    oldest = events[0]["at"] if events else (first.strftime("%Y-%m-%dT%H:%M:%SZ") if first else None)
    history_note = (
        "Headline counts are enrich + significance successes only. "
        "Sync / merge / queue are shown as opsProcessed so they cannot inflate "
        "entity throughput. Calendar month/YTD use America/Port_of_Spain midnights."
    )
    if first:
        age_h = (now - first).total_seconds() / 3600
        if age_h < 36 * 24:
            history_note += (
                " History on disk is short — week/month/YTD only count from the "
                "first enrichment entry date."
            )

    enrich_all = sum(
        int(e.get("processed") or 0) for e in events if e.get("task") in ENRICHMENT_TASKS
    )
    ops_all = sum(
        int(e.get("processed") or 0) for e in events if e.get("task") in OPS_TASKS
    )

    return {
        "firstEntryDate": first.strftime("%Y-%m-%dT%H:%M:%SZ") if first else None,
        "oldestEventAt": oldest,
        "historyNote": history_note,
        "metric": "enrichment",
        "totalProcessedAllTime": enrich_all,
        "totalOpsProcessedAllTime": ops_all,
        "totalEvents": len(events),
        "windows": windows,
        "byId": {w["id"]: w for w in windows},
    }


def load_swarm_daily() -> list[dict]:
    swarm_file = REPO / "data" / "governance" / "bot_kpi" / "swarm_daily.json"
    data = load_json(swarm_file)
    if isinstance(data, dict):
        return data.get("days", []) or []
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
        local_processed_by_task = {
            normalize_task(k): v for k, v in (local.get("processedByTask") or {}).items()
        }
        combined.append({
            "date": date_str,
            "localJobs": local.get("totalJobs", 0),
            "localDone": local.get("doneJobs", 0),
            "localErrors": local.get("errorJobs", 0),
            "localProcessed": local.get("processed", 0),
            "localByTask": local_by_task,
            "localProcessedByTask": local_processed_by_task,
            # Cloud swarm kept for historical charts; Mini track is Ollama/local-first
            "swarmProcessed": swarm.get("totalProcessed", 0),
            "swarmSucceeded": swarm.get("totalSucceeded", 0),
            "swarmFailed": swarm.get("totalFailed", 0),
            "swarmEnrichment": swarm.get("enrichment", 0),
            "swarmEdges": swarm.get("edges", 0),
            "swarmSignificance": swarm.get("significance", 0),
            "swarmRespawns": swarm.get("respawns", 0),
            "grandTotal": local.get("processed", 0) + swarm.get("totalProcessed", 0),
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
    # Keep stats_cache mirror next to KPI so curator pages stay in sync
    _safe_mirror(
        REPO / "data" / "governance" / "stats_cache.json",
        PUBLIC_GOV / "stats_cache.json",
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
    events = collect_volume_events(jobs)
    first = first_entry_date(events, jobs)
    volume = build_processed_volume(events, roster_ids, first)
    print(
        f"[local_kpi_aggregator] Processed volume events={len(events)} "
        f"firstEntry={volume.get('firstEntryDate')} "
        f"allTime={volume.get('totalProcessedAllTime')}"
    )
    for w in volume.get("windows") or []:
        print(
            f"[local_kpi_aggregator]   {w['id']}: processed={w['processed']} "
            f"jobs={w['jobs']} recorded={w['recorded']}"
        )

    kpi = {
        "updatedAt": now_iso(),
        "source": "local-mac-mini",
        "labelPrefix": (sot.get("meta") or {}).get("label_prefix", "com.annals."),
        "llmProvider": "ollama+grok",
        "totalJobsAllTime": len([j for j in jobs if j.get("status") in ("done", "error")]),
        "rosterCount": len(roster),
        "roster": roster,
        "firstEntryDate": volume.get("firstEntryDate"),
        "processedVolume": volume,
        # Legacy day windows (kept for existing Bot KPI cards)
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
