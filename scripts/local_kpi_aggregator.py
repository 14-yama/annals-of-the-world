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
# All Ollama enrich waiter shards (a–e) must be listed or last-hour under-counts.
OLLAMA_ENRICH_BOTS = (
    "enrich", "enrich-b", "enrich-c", "enrich-d", "enrich-e",
)
ENRICHMENT_TASKS = frozenset({
    *OLLAMA_ENRICH_BOTS,
    "significance",
    "enrich-grok", "enrich-grok-b", "significance-grok",
})
# Infrastructure / ops — shown separately so sync/merge don't inflate enrich KPIs.
OPS_TASKS = frozenset({
    "sync", "merge-cloud", "merge-cloud-audit", "seed-local", "push",
    "queue", "kpi", "stats-cache", "healthcheck", "bot-server",
    "edges-extract", "edges-extract-b", "edges-grok",
})

# Rolling window used for "current enrichment rate" (entities/hour).
RATE_LOOKBACK_MINUTES = 30

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

    if task in (*OLLAMA_ENRICH_BOTS, "enrich-grok", "enrich-grok-b"):
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


def _parse_pos_wall(stamp: str) -> datetime | None:
    """Parse 'YYYY-MM-DD HH:MM:SS' log wall clock as America/Port_of_Spain → UTC."""
    try:
        naive = datetime.strptime(stamp.strip(), "%Y-%m-%d %H:%M:%S")
        return naive.replace(tzinfo=POS_TZ).astimezone(timezone.utc)
    except ValueError:
        return None


def _iso_z(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def collect_launchd_log_events(
    seen_keys: set[str],
    prior_events: list[dict],
    now: datetime | None = None,
) -> list[dict]:
    """
    Parse ~/Library/Logs/annals-bots/enrich*.log (+ significance) for RESULTS
    and mid-batch ENRICHED tallies.

    LaunchAgents often don't write local_bot_status.json, so without this
    enrich/sig looks like 0 while logs show real work. Finished batches are
    attributed at *finish* time (not start) so long --count 32 jobs still land
    in the last-hour window. Open batches contribute in-progress ENRICHED
    counts so live work is visible before RESULTS.
    """
    now = now or datetime.now(timezone.utc)
    out: list[dict] = []
    specs = (
        ("enrich", "enrich.log", "enriched"),
        ("enrich-b", "enrich-b.log", "enriched"),
        ("enrich-c", "enrich-c.log", "enriched"),
        ("enrich-d", "enrich-d.log", "enriched"),
        ("enrich-e", "enrich-e.log", "enriched"),
        ("enrich-grok", "enrich-grok.log", "enriched"),
        ("enrich-grok-b", "enrich-grok-b.log", "enriched"),
        ("significance", "significance.log", "scored"),
        ("significance-grok", "significance-grok.log", "scored"),
        ("edges-extract", "edges-extract.log", "edges"),
        ("edges-grok", "edges-grok.log", "edges"),
    )
    launchd_start_re = re.compile(
        r"\[annals-launchd\] start (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})"
    )
    launchd_end_re = re.compile(
        r"\[annals-launchd\] end (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})"
    )
    dispatch_start_re = re.compile(r"\[dispatch\] start ([^\s:]+):")
    dispatch_done_re = re.compile(
        r"\[dispatch\] done ([^\s]+) status=(\d+) elapsed=(\d+)s"
    )

    for task, fname, kind in specs:
        path = LOG_DIR / fname
        if not path.exists():
            continue
        try:
            text = path.read_text(errors="replace")
        except Exception:
            continue

        if kind == "enriched":
            result_re = re.compile(r"RESULTS:\s*(\d+)\s+enriched")
            success_line_re = re.compile(r"^\s*ENRICHED\b")
        elif kind == "scored":
            result_re = re.compile(r"RESULTS:\s*(\d+)\s+scored")
            success_line_re = re.compile(r"^\s*(?:SCORED|UPDATED)\b")
        else:
            result_re = re.compile(r"(?:Wrote|saved|new edges|accepted)[^\d]*(\d+)", re.I)
            success_line_re = None

        last_launchd_start: datetime | None = None
        dispatch_start: datetime | None = None
        dispatch_active = False
        pending_result: tuple[int, datetime | None] | None = None  # (n, start)
        mid_successes = 0

        def emit_finished(processed: int, started: datetime | None, finished: datetime) -> None:
            nonlocal pending_result
            at = finished
            eid = f"launchd:{task}:{_iso_z(started or finished)}:{processed}:fin"
            if eid in seen_keys:
                return
            minute = at.strftime("%Y-%m-%dT%H:%M")
            if any(
                e.get("task") == task
                and e.get("source") == "local_bot_status"
                and str(e.get("at", ""))[:16] == minute
                for e in prior_events
            ):
                return
            seen_keys.add(eid)
            out.append({
                "at": _iso_z(at),
                "task": task,
                "processed": processed,
                "jobs": 1,
                "done": 1,
                "error": 0,
                "source": "launchd_log",
                "id": eid,
                "startedAt": _iso_z(started) if started else None,
            })

        for line in text.splitlines():
            sm = launchd_start_re.search(line)
            if sm:
                last_launchd_start = _parse_pos_wall(sm.group(1))
                continue

            em = launchd_end_re.search(line)
            if em and pending_result is not None:
                finished = _parse_pos_wall(em.group(1)) or now
                n, started = pending_result
                emit_finished(n, started, finished)
                pending_result = None
                dispatch_active = False
                mid_successes = 0
                continue

            dm = dispatch_start_re.search(line)
            if dm and dm.group(1) == task:
                # Flush any orphan pending result at previous dispatch start.
                if pending_result is not None:
                    n, started = pending_result
                    emit_finished(n, started, started or now)
                    pending_result = None
                dispatch_start = last_launchd_start or now
                dispatch_active = True
                mid_successes = 0
                continue

            rm = result_re.search(line)
            if rm and dispatch_active:
                pending_result = (int(rm.group(1)), dispatch_start)
                continue

            done_m = dispatch_done_re.search(line)
            if done_m and done_m.group(1) == task:
                elapsed = int(done_m.group(3))
                if pending_result is not None:
                    n, started = pending_result
                    finished = (started + timedelta(seconds=elapsed)) if started else now
                    emit_finished(n, started, finished)
                    pending_result = None
                dispatch_active = False
                mid_successes = 0
                continue

            if dispatch_active and success_line_re and success_line_re.search(line):
                mid_successes += 1

        # Orphan RESULTS without end/done — still count at best-known finish.
        if pending_result is not None:
            n, started = pending_result
            emit_finished(n, started, now)
            pending_result = None

        # In-flight batch: count ENRICHED/SCORED lines so last-hour isn't 0 mid-run.
        if dispatch_active and mid_successes > 0:
            started = dispatch_start or now
            eid = f"launchd:{task}:{_iso_z(started)}:inflight:{mid_successes}"
            if eid not in seen_keys:
                seen_keys.add(eid)
                out.append({
                    "at": _iso_z(now),
                    "task": task,
                    "processed": mid_successes,
                    "jobs": 1,
                    "done": 0,
                    "error": 0,
                    "source": "launchd_log_inflight",
                    "id": eid,
                    "startedAt": _iso_z(started),
                    "inflight": True,
                })
    return out


def build_enrich_live(sot: dict, now: datetime | None = None) -> dict:
    """
    Live enrich desk snapshot for Curator KPI chips.

    Rate formula:
      entities/hour = (ENRICHED in last RATE_LOOKBACK_MINUTES) × (60 / lookback)
    where ENRICHED = finished RESULTS for batches overlapping the lookback
    plus in-flight ENRICHED log lines on open batches.
    """
    now = now or datetime.now(timezone.utc)
    cutoff = now - timedelta(minutes=RATE_LOOKBACK_MINUTES)

    bots = sot.get("bots") if isinstance(sot.get("bots"), list) else []
    configured: list[dict] = []
    for bot in bots:
        if not isinstance(bot, dict):
            continue
        bid = str(bot.get("id") or "")
        if bid not in OLLAMA_ENRICH_BOTS:
            continue
        sched = bot.get("schedule") if isinstance(bot.get("schedule"), dict) else {}
        enabled = bot.get("status") == "active" and sched.get("enabled") is not False
        note = str(sched.get("note") or "")
        shard_m = re.search(r"shard\s+(\d+/\d+)", note, flags=re.I)
        configured.append({
            "id": bid,
            "enabled": enabled,
            "label": (bot.get("launchd") or {}).get("label") or f"com.annals.{bid}",
            "shard": shard_m.group(1) if shard_m else None,
        })

    launchd_start_re = re.compile(
        r"\[annals-launchd\] start (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})"
    )
    dispatch_start_re = re.compile(r"\[dispatch\] start ([^\s:]+):")
    dispatch_done_re = re.compile(
        r"\[dispatch\] done ([^\s]+) status=\d+ elapsed=(\d+)s"
    )
    results_re = re.compile(r"RESULTS:\s*(\d+)\s+enriched(?:,\s*(\d+)\s+failed)?")
    enriched_line_re = re.compile(r"^\s*ENRICHED\b")
    shard_re = re.compile(r"--shard\s+(\d+/\d+)")

    live: list[dict] = []
    waiting: list[dict] = []
    last_batches: list[dict] = []
    enriched_in_lookback = 0
    failed_in_lookback = 0

    for cfg in configured:
        task = cfg["id"]
        path = LOG_DIR / f"{task}.log"
        state = {
            "id": task,
            "label": cfg["label"],
            "shard": cfg["shard"],
            "status": "disabled",
            "inflightEnriched": 0,
            "lastBatchEnriched": None,
            "lastBatchFailed": None,
            "lastBatchAt": None,
            "dispatchStartedAt": None,
        }
        if not cfg["enabled"]:
            continue
        if not path.exists():
            state["status"] = "waiting"
            waiting.append(state)
            continue
        try:
            text = path.read_text(errors="replace")
        except Exception:
            state["status"] = "waiting"
            waiting.append(state)
            continue

        last_launchd_start: datetime | None = None
        dispatch_start: datetime | None = None
        dispatch_active = False
        mid_enriched = 0
        pending_result: tuple[int, int] | None = None  # ok, fail
        batch_shard = cfg["shard"]
        recent_ok = 0
        recent_fail = 0

        for line in text.splitlines():
            sm = launchd_start_re.search(line)
            if sm:
                last_launchd_start = _parse_pos_wall(sm.group(1))
                continue

            dm = dispatch_start_re.search(line)
            if dm and dm.group(1) == task:
                dispatch_start = last_launchd_start
                dispatch_active = True
                mid_enriched = 0
                pending_result = None
                sm2 = shard_re.search(line)
                if sm2:
                    batch_shard = sm2.group(1)
                continue

            if dispatch_active and enriched_line_re.search(line):
                mid_enriched += 1
                continue

            rm = results_re.search(line)
            if rm and dispatch_active:
                pending_result = (int(rm.group(1)), int(rm.group(2) or 0))
                continue

            done_m = dispatch_done_re.search(line)
            if done_m and done_m.group(1) == task and dispatch_active:
                elapsed = int(done_m.group(2))
                started = dispatch_start
                finished = (started + timedelta(seconds=elapsed)) if started else now
                ok, fail = pending_result if pending_result else (mid_enriched, 0)
                if finished >= cutoff or (started and started >= cutoff):
                    recent_ok += ok
                    recent_fail += fail
                state["lastBatchEnriched"] = ok
                state["lastBatchFailed"] = fail
                state["lastBatchAt"] = _iso_z(finished)
                dispatch_active = False
                mid_enriched = 0
                pending_result = None
                continue

        if dispatch_active:
            state["status"] = "live"
            state["inflightEnriched"] = mid_enriched
            state["dispatchStartedAt"] = _iso_z(dispatch_start) if dispatch_start else None
            state["shard"] = batch_shard or state["shard"]
            recent_ok += mid_enriched
            live.append(state)
        else:
            state["status"] = "waiting"
            waiting.append(state)

        enriched_in_lookback += recent_ok
        failed_in_lookback += recent_fail
        if state.get("lastBatchAt") is not None:
            last_batches.append({
                "id": task,
                "enriched": state.get("lastBatchEnriched"),
                "failed": state.get("lastBatchFailed"),
                "at": state.get("lastBatchAt"),
                "ok": (state.get("lastBatchFailed") or 0) == 0
                and (state.get("lastBatchEnriched") or 0) > 0,
            })

    sig_path = LOG_DIR / "significance.log"
    sig_status = "unknown"
    sig_last_at = None
    sig_inflight = False
    if sig_path.exists():
        try:
            sig_text = sig_path.read_text(errors="replace")
            starts = list(re.finditer(r"\[dispatch\] start significance:", sig_text))
            dones = list(re.finditer(r"\[dispatch\] done significance", sig_text))
            if starts:
                sig_inflight = not dones or dones[-1].start() < starts[-1].start()
                sig_status = "live" if sig_inflight else "waiting"
            ends = list(re.finditer(
                r"\[annals-launchd\] end (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*bot=significance",
                sig_text,
            ))
            if ends:
                parsed = _parse_pos_wall(ends[-1].group(1))
                if parsed:
                    sig_last_at = _iso_z(parsed)
        except Exception:
            pass

    queue = load_json(ENRICH_DIR / "queue.json")
    queue_backlog = None
    queue_generated = None
    if isinstance(queue, dict):
        # Prefer full thin count; fall back to written queue length (may be capped).
        queue_backlog = queue.get("needingEnrichment")
        if queue_backlog is None:
            queue_backlog = queue.get("thinRemaining")
        if queue_backlog is None:
            queue_backlog = queue.get("count")
        queue_generated = queue.get("generated")

    hours = RATE_LOOKBACK_MINUTES / 60.0
    rate = round(enriched_in_lookback / hours, 1) if hours > 0 else 0.0
    scale = int(60 / RATE_LOOKBACK_MINUTES) if RATE_LOOKBACK_MINUTES else 0
    enabled_n = sum(1 for c in configured if c["enabled"])

    return {
        "updatedAt": _iso_z(now),
        "updatedAtAst": now.astimezone(POS_TZ).strftime("%Y-%m-%d %H:%M:%S AST"),
        "timezone": "America/Port_of_Spain",
        "enrichBotsConfigured": enabled_n,
        "enrichBotsLive": len(live),
        "enrichBotsWaiting": len(waiting),
        "enrichBotsTotal": len(configured),
        "liveLabels": [x["id"] for x in live],
        "waitingLabels": [x["id"] for x in waiting],
        "live": live,
        "waiting": waiting,
        "ratePerHour": rate,
        "rateLookbackMinutes": RATE_LOOKBACK_MINUTES,
        "rateFormula": (
            f"(ENRICHED in last {RATE_LOOKBACK_MINUTES}m incl. in-flight) × {scale}"
        ),
        "enrichedInLookback": enriched_in_lookback,
        "failedInLookback": failed_in_lookback,
        "lastBatches": sorted(
            last_batches, key=lambda b: b.get("at") or "", reverse=True
        )[:8],
        "significanceStatus": sig_status,
        "significanceInflight": sig_inflight,
        "significanceLastAt": sig_last_at,
        "queueBacklog": queue_backlog,
        "queueGeneratedAt": queue_generated,
        "shardsLive": sorted({x.get("shard") for x in live if x.get("shard")}),
    }


def build_corpus_progress(enrich_live: dict | None = None) -> dict:
    """
    Edited-vs-left breakdown for curator KPIs.

    - entitiesTotal: stats_cache entity corpus (~392k)
    - enrichedApprox / thinRemaining: summary≥800 heuristic from queue.json
    - auditTotal: field-level audit_log rows (NOT unique entities)
    - ratePerHour: live enrich desk rate
    """
    stats = load_json(GOV_DIR / "stats_cache.json")
    stats = stats if isinstance(stats, dict) else {}
    queue = load_json(ENRICH_DIR / "queue.json")
    queue = queue if isinstance(queue, dict) else {}

    entities_total = int(
        stats.get("total")
        or queue.get("total_scanned")
        or 0
    )
    needing = queue.get("needingEnrichment")
    if needing is None:
        needing = queue.get("thinRemaining")
    truncated = bool(queue.get("queueTruncated"))
    if needing is None:
        needing = queue.get("count")
        # Historical queue.json only stored the capped list length.
        cap = queue.get("queueCappedAt") or queue.get("count")
        if needing is not None and cap is not None and int(needing) >= int(cap):
            truncated = True

    needing_n = int(needing) if needing is not None else None
    enriched = queue.get("enrichedApprox")
    enriched_is_upper_bound = False
    if enriched is None and entities_total and needing_n is not None:
        # When queue.json was truncated at --limit, needing_n is a lower bound on
        # thin → enrichedApprox is only an upper bound until full needingEnrichment lands.
        enriched = max(0, entities_total - needing_n)
        enriched_is_upper_bound = truncated
    enriched_n = int(enriched) if enriched is not None else None
    if queue.get("needingEnrichment") is not None:
        enriched_is_upper_bound = False

    pct = queue.get("pctEnriched")
    if pct is None and entities_total and enriched_n is not None:
        pct = round(100.0 * enriched_n / entities_total, 2)

    audit_total = stats.get("auditTotal")
    audit_n = int(audit_total) if audit_total is not None else None
    rate = None
    if isinstance(enrich_live, dict) and enrich_live.get("ratePerHour") is not None:
        rate = enrich_live.get("ratePerHour")

    note = (
        "Enriched ≈ entities with summary ≥ 800 chars. "
        "Thin remaining = summary < 800 (enrichment queue heuristic). "
        "auditTotal counts field-level audit_log rows (one enrich ≈ 5–7 rows), "
        "not unique entities."
    )
    if truncated:
        note += (
            " Queue file was truncated at --limit — thinRemaining is a lower bound "
            "and enriched≈ is an upper bound until the next full queue refresh "
            "writes needingEnrichment."
        )

    return {
        "updatedAt": now_iso(),
        "updatedAtAst": datetime.now(POS_TZ).strftime("%Y-%m-%d %H:%M:%S AST"),
        "entitiesTotal": entities_total or None,
        "enrichedApprox": enriched_n,
        "enrichedIsUpperBound": enriched_is_upper_bound,
        "thinRemaining": needing_n,
        "thinIsLowerBound": truncated,
        "pctEnriched": pct,
        "queueBacklog": needing_n,
        "queueWritten": queue.get("count"),
        "queueTruncated": truncated,
        "enrichHeuristic": queue.get("enrichHeuristic") or "summary_len >= 800",
        "thinBreakdown": queue.get("thinBreakdown"),
        "ratePerHour": rate,
        "auditTotal": audit_n,
        "auditTotalNote": (
            "Field-level UPDATE rows in audit_log — not unique enriched entities."
        ),
        "queueGeneratedAt": queue.get("generated"),
        "note": note,
    }


def patch_stats_cache_corpus(progress: dict) -> None:
    """Merge corpus enrichment progress into stats_cache without wiping auditTotal."""
    payload = {
        "enrichmentProgress": {
            "entitiesTotal": progress.get("entitiesTotal"),
            "enrichedApprox": progress.get("enrichedApprox"),
            "thinRemaining": progress.get("thinRemaining"),
            "pctEnriched": progress.get("pctEnriched"),
            "ratePerHour": progress.get("ratePerHour"),
            "auditTotal": progress.get("auditTotal"),
            "updatedAt": progress.get("updatedAt"),
            "note": progress.get("note"),
        }
    }
    for rel in (
        GOV_DIR / "stats_cache.json",
        PUBLIC_GOV / "stats_cache.json",
    ):
        if not rel.exists():
            continue
        try:
            data = json.loads(rel.read_text())
            if not isinstance(data, dict):
                continue
            data.update(payload)
            # Never drop auditTotal if somehow absent from read
            rel.write_text(json.dumps(data, indent=2) + "\n")
        except Exception:
            continue


def _read_ollama_num_parallel() -> int | None:
    """Best-effort read of OLLAMA_NUM_PARALLEL from brew LaunchAgent (no secrets)."""
    plist = Path.home() / "Library" / "LaunchAgents" / "sh.brew.ollama.plist"
    if not plist.exists():
        return None
    try:
        import subprocess
        out = subprocess.check_output(
            ["plutil", "-extract", "EnvironmentVariables.OLLAMA_NUM_PARALLEL", "raw", str(plist)],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
        return int(out) if out.isdigit() else None
    except Exception:
        return None


def build_parallel_capacity(sot: dict, enrich_live: dict) -> dict:
    """
    Actual parallel capacity from live SoT + Ollama LaunchAgent.
    Gate (max_concurrent_llm) and server (OLLAMA_NUM_PARALLEL) can differ —
    effective LLM parallel is the min of the two when both are known.
    """
    conc = sot.get("concurrency") if isinstance(sot.get("concurrency"), dict) else {}
    lanes = conc.get("lanes") if isinstance(conc.get("lanes"), dict) else {}
    max_llm = int(conc.get("max_concurrent_llm") or 1)
    max_grok = int(conc.get("max_concurrent_grok") or 0)
    max_heavy = int(conc.get("max_concurrent_heavy_scan") or 1)
    serialize = bool(conc.get("serialize_enrich_vs_significance"))
    ollama_parallel = _read_ollama_num_parallel()
    effective_llm = min(max_llm, ollama_parallel) if ollama_parallel else max_llm

    bots = sot.get("bots") if isinstance(sot.get("bots"), list) else []
    active_by_lane: dict[str, list[str]] = {}
    enrich_labels: list[str] = []
    for bot in bots:
        if not isinstance(bot, dict):
            continue
        bid = str(bot.get("id") or "")
        sched = bot.get("schedule") if isinstance(bot.get("schedule"), dict) else {}
        if bot.get("status") != "active" or sched.get("enabled") is False:
            continue
        lane = str(bot.get("lane") or "none")
        active_by_lane.setdefault(lane, []).append(bid)
        if bid in OLLAMA_ENRICH_BOTS:
            enrich_labels.append(bid)

    return {
        "maxConcurrentLlm": max_llm,
        "maxConcurrentGrok": max_grok,
        "ollamaNumParallel": ollama_parallel,
        "effectiveLlmParallel": effective_llm,
        "effectiveNote": (
            f"Annals gate allows {max_llm} Ollama gens; "
            + (
                f"Ollama server OLLAMA_NUM_PARALLEL={ollama_parallel}; "
                f"effective = {effective_llm}."
                if ollama_parallel is not None
                else "OLLAMA_NUM_PARALLEL unknown — using SoT gate."
            )
        ),
        "enrichWaitersConfigured": len(enrich_labels),
        "enrichWaitersLive": int(enrich_live.get("enrichBotsLive") or 0),
        "serializeEnrichVsSignificance": serialize,
        "maxConcurrentHeavyScan": max_heavy,
        "lanes": {
            lid: {
                "description": str(desc),
                "activeBots": active_by_lane.get(lid, []),
                "activeCount": len(active_by_lane.get(lid, [])),
                "maxParallel": (
                    effective_llm if lid == "ollama"
                    else (max_grok if lid == "grok"
                    else (max_heavy if lid == "heavy_scan"
                    else (len(active_by_lane.get(lid, [])) or 1)))
                ),
            }
            for lid, desc in lanes.items()
        },
        "laneNotes": [
            f"Ollama LLM: up to {effective_llm} parallel (SoT {max_llm}"
            + (f", OLLAMA_NUM_PARALLEL {ollama_parallel}" if ollama_parallel is not None else "")
            + f"); {len(enrich_labels)} enrich waiters + significance share slots"
            + (" (sig serialized vs enrich)" if serialize else " (sig may share free slots)"),
            "Edges: no-LLM — can run beside Ollama",
            "Light (queue/kpi/stats/push): parallel with other light work",
            f"Heavy scan (audits): max {max_heavy} at a time",
            "Network write (sync/seed/merge): Appwrite writes; typically one lock at a time",
        ],
    }


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
    now = datetime.now(timezone.utc)
    events.extend(collect_launchd_log_events(seen_keys, events, now=now))

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
        # ai_enrich writes local wall clock with a Z suffix — prefer mtime when
        # the stamped "UTC" is >2h behind the file's real mtime.
        try:
            mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
        except OSError:
            mtime = None
        if mtime and (at is None or abs((mtime - at).total_seconds()) > 7200):
            at = mtime
        if not at:
            continue
        processed = _artifact_success_count(data, success_keys)
        if processed <= 0:
            continue
        eid = f"artifact:{name}:{at.strftime('%Y%m%d%H%M%S')}"
        if eid in seen_keys:
            continue
        # Skip if a job of same task already covers this minute (avoid double-count)
        minute = at.strftime("%Y-%m-%dT%H:%M")
        if any(
            e["task"] == task
            and e["source"] in ("local_bot_status", "launchd_log", "launchd_log_inflight")
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
        "Headline counts are enrich + significance successes only "
        "(finished RESULTS + mid-batch ENRICHED tallies). "
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
    enrich_live = build_enrich_live(sot)
    parallel = build_parallel_capacity(sot, enrich_live)
    corpus = build_corpus_progress(enrich_live)
    patch_stats_cache_corpus(corpus)
    print(
        f"[local_kpi_aggregator] Corpus "
        f"enriched≈{corpus.get('enrichedApprox')} / {corpus.get('entitiesTotal')} "
        f"({corpus.get('pctEnriched')}%) · thin={corpus.get('thinRemaining')} · "
        f"auditTotal={corpus.get('auditTotal')} · rate={corpus.get('ratePerHour')}/hr"
    )
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
    print(
        f"[local_kpi_aggregator] Enrich live "
        f"{enrich_live.get('enrichBotsLive')}/{enrich_live.get('enrichBotsConfigured')} "
        f"rate={enrich_live.get('ratePerHour')}/hr "
        f"effectiveLlmParallel={parallel.get('effectiveLlmParallel')}"
    )

    kpi = {
        "updatedAt": now_iso(),
        "updatedAtAst": enrich_live.get("updatedAtAst"),
        "source": "local-mac-mini",
        "labelPrefix": (sot.get("meta") or {}).get("label_prefix", "com.annals."),
        "llmProvider": "ollama+grok",
        "totalJobsAllTime": len([j for j in jobs if j.get("status") in ("done", "error")]),
        "rosterCount": len(roster),
        "roster": roster,
        "firstEntryDate": volume.get("firstEntryDate"),
        "processedVolume": volume,
        "enrichLive": enrich_live,
        "parallelCapacity": parallel,
        "corpusProgress": corpus,
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
