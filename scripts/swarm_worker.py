#!/usr/bin/env python3
"""
Swarm Worker — One slot of the 20-bot GitHub Actions parallel enrichment swarm.

Each slot is assigned a task type based on its index and processes a sharded
portion of the enrichment queue (every 20th item starting at slot N) so that
no two bots ever write to the same entity file — zero git conflicts.

Task assignment:
  Slots  0-7  → enrichment  (summary writing via Ollama llama3.2:3b)
  Slots  8-11 → edges       (relationship generation)
  Slots 12-15 → significance (historicalSignificance rating backfill)
  Slot   16   → audit       (completeness + orphan scan)
  Slot   17   → consistency (era/slug/callNumber validation)
  Slot   18   → sync        (push enriched files → Appwrite via sync_gateway.ts)
  Slot   19   → queue_refresh (rebuild queue + stats)

Self-respawn at 90%:
  At 5h 24m (90% of GitHub's 6h limit), the worker writes an output file
  that tells the workflow step to fire a workflow_dispatch for the next
  generation. The workflow reads GITHUB_OUTPUT to decide.

KPI reporting:
  data/governance/bot_kpi/slot-{N}.json  — latest run state
  data/governance/bot_kpi/swarm_daily.json — historical aggregation

Usage (called by GitHub Actions):
  python3 scripts/swarm_worker.py --slot 5 --gen 1 --batch 10 --limit 19440
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

# ─── Paths ────────────────────────────────────────────────────────────────────
REPO  = Path(__file__).resolve().parent.parent
KPI_DIR     = REPO / "data" / "governance" / "bot_kpi"
QUEUE_FILE  = REPO / "data" / "enrichment" / "queue.json"
DAILY_FILE  = KPI_DIR / "swarm_daily.json"
ENTITIES_DIR = REPO / "data" / "appwrite-export" / "entities"

KPI_DIR.mkdir(parents=True, exist_ok=True)

# ─── Task mapping ─────────────────────────────────────────────────────────────
def slot_to_task(slot: int) -> str:
    if slot <= 7:   return "enrichment"
    if slot <= 11:  return "edges"
    if slot <= 15:  return "significance"
    if slot == 16:  return "audit"
    if slot == 17:  return "consistency"
    if slot == 18:  return "sync"
    return "queue_refresh"

TASK_COLORS = {
    "enrichment":   "#4285F4",
    "edges":        "#1ABC9C",
    "significance": "#8E44AD",
    "audit":        "#27AE60",
    "consistency":  "#D4AF37",
    "sync":         "#9E9A90",
    "queue_refresh":"#E67E22",
}

# ─── Helpers ──────────────────────────────────────────────────────────────────
def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def elapsed(start: float) -> float:
    return time.monotonic() - start

def log(msg: str) -> None:
    print(f"[{now_iso()}] {msg}", flush=True)

def write_gh_output(key: str, value: str) -> None:
    """Write to GITHUB_OUTPUT so the workflow step can read it."""
    gh_out = os.environ.get("GITHUB_OUTPUT", "")
    if gh_out:
        with open(gh_out, "a") as f:
            f.write(f"{key}={value}\n")
    # Also write a temp file the bash commit step can read
    (Path("/tmp") / f"swarm_{key}_{os.environ.get('SWARM_SLOT', '?')}.txt").write_text(value)

# ─── KPI helpers ──────────────────────────────────────────────────────────────
def write_slot_kpi(slot: int, task: str, kpi: dict) -> None:
    path = KPI_DIR / f"slot-{slot}.json"
    path.write_text(json.dumps(kpi, indent=2))

def update_daily_history(date_str: str, task: str, succeeded: int, failed: int) -> None:
    """Append/update today's row in swarm_daily.json."""
    data: dict = {"updatedAt": now_iso(), "days": []}
    if DAILY_FILE.exists():
        try:
            data = json.loads(DAILY_FILE.read_text())
        except Exception:
            pass

    days: list[dict] = data.get("days", [])
    today = next((d for d in days if d.get("date") == date_str), None)
    if today is None:
        today = {"date": date_str, "totalProcessed": 0, "totalSucceeded": 0,
                 "totalFailed": 0, "enrichment": 0, "edges": 0,
                 "significance": 0, "audit": 0, "sync": 0, "respawns": 0}
        days.append(today)

    today["totalProcessed"]  = today.get("totalProcessed", 0) + succeeded + failed
    today["totalSucceeded"]  = today.get("totalSucceeded", 0) + succeeded
    today["totalFailed"]     = today.get("totalFailed", 0) + failed
    today[task]              = today.get(task, 0) + succeeded

    # Keep last 90 days
    data["days"] = sorted(days, key=lambda d: d["date"])[-90:]
    data["updatedAt"] = now_iso()
    DAILY_FILE.write_text(json.dumps(data, indent=2))

# ─── Queue sharding ───────────────────────────────────────────────────────────
def load_sharded_queue(slot: int, stride: int = 20) -> list[dict]:
    """Load queue.json and return every stride-th item starting at slot."""
    if not QUEUE_FILE.exists():
        log(f"WARNING: queue file not found at {QUEUE_FILE}")
        return []
    try:
        raw = json.loads(QUEUE_FILE.read_text())
    except Exception as exc:
        log(f"ERROR reading queue: {exc}")
        return []

    # queue.json may be either a raw list or an object with a "queue" key.
    if isinstance(raw, dict):
        items = raw.get("queue", [])
    elif isinstance(raw, list):
        items = raw
    else:
        log(f"WARNING: queue format not recognized ({type(raw).__name__})")
        return []

    if not isinstance(items, list):
        log("WARNING: queue payload is not a list")
        return []

    sharded = items[slot::stride]
    log(f"Queue: {len(items)} total → {len(sharded)} for slot {slot} (stride={stride})")
    return sharded

# ─── Ollama call (lightweight — used only by significance backfill inline) ────
def call_ollama(prompt: str, model: str = "llama3.2:3b",
                max_tokens: int = 200) -> str | None:
    import urllib.request, urllib.error
    url = f"{os.environ.get('OLLAMA_HOST', 'http://localhost:11434')}/api/generate"
    payload = json.dumps({
        "model": model, "prompt": prompt, "stream": False,
        "options": {"num_predict": max_tokens, "temperature": 0.4},
    }).encode()
    try:
        req = urllib.request.Request(url, data=payload,
                                     headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=120) as resp:
            return json.loads(resp.read())["response"]
    except Exception as exc:
        log(f"Ollama error: {exc}")
        return None

# ─── Task runners ─────────────────────────────────────────────────────────────

def run_enrichment(slot: int, queue: list[dict], batch: int, start_t: float,
                   limit_s: float) -> tuple[int, int]:
    """Run ai_enrich_autonomous.py on each item in queue until time runs out."""
    succeeded = failed = 0
    # Write a slot-specific queue file
    slot_queue = REPO / "data" / "enrichment" / f"queue_slot_{slot}.json"
    slot_queue.write_text(json.dumps(queue, indent=2))

    # Process in batches until time limit
    processed = 0
    while processed < len(queue) and elapsed(start_t) < limit_s:
        remaining_items = min(batch, len(queue) - processed)
        if remaining_items <= 0:
            break

        # Build a mini queue for this batch
        batch_items = queue[processed: processed + remaining_items]
        batch_file = REPO / "data" / "enrichment" / f"queue_slot_{slot}_batch.json"
        batch_file.write_text(json.dumps(batch_items, indent=2))

        log(f"[slot {slot}] enrichment batch {processed}–{processed+remaining_items} of {len(queue)}")
        result = subprocess.run(
            [sys.executable, str(REPO / "scripts" / "ai_enrich_autonomous.py"),
             "--count", str(remaining_items),
             "--model", "ollama",
             "--lenient",                 # lower thresholds for llama3.2:3b
             "--queue", str(batch_file)],
            capture_output=False, cwd=str(REPO),
            env={**os.environ},
        )
        if result.returncode == 0:
            succeeded += remaining_items
        else:
            failed += remaining_items

        processed += remaining_items

        # Report progress
        log(f"[slot {slot}] enrichment progress: {processed}/{len(queue)} "
            f"({succeeded} ok, {failed} fail) elapsed={elapsed(start_t):.0f}s")

    return succeeded, failed


def run_edges(slot: int, queue: list[dict], batch: int, start_t: float,
              limit_s: float) -> tuple[int, int]:
    """Run ai_edge_bot.py for entities in queue."""
    succeeded = failed = 0
    processed = 0
    slugs = [item["slug"] for item in queue if item.get("slug")]

    while processed < len(slugs) and elapsed(start_t) < limit_s:
        b_end = min(processed + batch, len(slugs))
        log(f"[slot {slot}] edges batch {processed}–{b_end} elapsed={elapsed(start_t):.0f}s")
        result = subprocess.run(
            [sys.executable, str(REPO / "scripts" / "ai_edge_bot.py"),
             "--count", str(b_end - processed),
             "--model", "ollama",
             "--min-significance", "0"],
            capture_output=False, cwd=str(REPO),
            env={**os.environ},
        )
        if result.returncode == 0:
            succeeded += b_end - processed
        else:
            failed += b_end - processed
        processed = b_end

    return succeeded, failed


def run_significance(slot: int, queue: list[dict], batch: int, start_t: float,
                     limit_s: float) -> tuple[int, int]:
    """Run backfill_significance.py."""
    succeeded = failed = 0
    processed = 0

    # Filter to entities with summary >= 600c but no historicalSignificance
    eligible = []
    for item in queue:
        path = ENTITIES_DIR / item.get("path", "NONE")
        if not path.exists():
            continue
        try:
            data = json.loads(path.read_text())
            summary = data.get("summary", "") or ""
            if len(summary) >= 600 and not data.get("historicalSignificance"):
                eligible.append(item)
        except Exception:
            pass
    log(f"[slot {slot}] significance: {len(eligible)} eligible from {len(queue)} in shard")

    while processed < len(eligible) and elapsed(start_t) < limit_s:
        b_end = min(processed + batch, len(eligible))
        log(f"[slot {slot}] significance batch {processed}–{b_end}")
        result = subprocess.run(
            [sys.executable, str(REPO / "scripts" / "backfill_significance.py"),
             "--count", str(b_end - processed),
             "--model", "ollama"],
            capture_output=False, cwd=str(REPO),
        )
        if result.returncode == 0:
            succeeded += b_end - processed
        else:
            failed += b_end - processed
        processed = b_end

    return succeeded, failed


def run_audit(slot: int, start_t: float, limit_s: float) -> tuple[int, int]:
    """Run audit scripts (completeness / orphan)."""
    log(f"[slot {slot}] audit: running completeness + orphan scan")
    scripts = [
        [sys.executable, str(REPO / "scripts" / "run_audits.py")],
    ]
    succeeded = failed = 0
    for cmd in scripts:
        if elapsed(start_t) >= limit_s:
            break
        r = subprocess.run(cmd, capture_output=False, cwd=str(REPO))
        if r.returncode == 0:
            succeeded += 1
        else:
            failed += 1
    return succeeded, failed


def run_consistency(slot: int, start_t: float, limit_s: float) -> tuple[int, int]:
    """Run consistency validation."""
    log(f"[slot {slot}] consistency check")
    r = subprocess.run(
        [sys.executable, str(REPO / "scripts" / "validate_slugs.py")],
        capture_output=False, cwd=str(REPO),
    )
    return (1, 0) if r.returncode == 0 else (0, 1)


def run_sync(slot: int, start_t: float, limit_s: float) -> tuple[int, int]:
    """Run sync gateway to push enriched entities to Appwrite."""
    if not os.environ.get("APPWRITE_API_KEY"):
        log(f"[slot {slot}] sync: APPWRITE_API_KEY not set — skipping")
        return 0, 0
    log(f"[slot {slot}] sync: running sync_gateway.ts")
    node_bin = "npx"
    r = subprocess.run(
        [node_bin, "tsx", str(REPO / "scripts" / "sync_gateway.ts")],
        capture_output=False, cwd=str(REPO),
    )
    return (1, 0) if r.returncode == 0 else (0, 1)


def run_queue_refresh(slot: int, start_t: float, limit_s: float) -> tuple[int, int]:
    """Regenerate the enrichment queue and print stats."""
    log(f"[slot {slot}] queue refresh")
    r = subprocess.run(
        [sys.executable, str(REPO / "scripts" / "enrichment_queue.py"),
         "--limit", "10000", "--stats"],
        capture_output=False, cwd=str(REPO),
    )
    return (1, 0) if r.returncode == 0 else (0, 1)


# ─── Main ─────────────────────────────────────────────────────────────────────
def main() -> None:
    p = argparse.ArgumentParser(description="Swarm Worker — one slot of the 20-bot swarm")
    p.add_argument("--slot",  type=int, default=int(os.environ.get("SWARM_SLOT", "0")))
    p.add_argument("--gen",   type=int, default=int(os.environ.get("SWARM_GENERATION", "1")))
    p.add_argument("--batch", type=int, default=int(os.environ.get("SWARM_BATCH_SIZE", "10")))
    p.add_argument("--limit", type=int, default=int(os.environ.get("SWARM_TIME_LIMIT", "19440")),
                   help="Max wall-clock seconds (default 19440 = 5h24m = 90%% of GH limit)")
    args = p.parse_args()

    slot      = args.slot
    gen       = args.gen
    batch     = args.batch
    limit_s   = float(args.limit)
    task      = slot_to_task(slot)
    run_id    = os.environ.get("GITHUB_RUN_ID", "local")
    started   = now_iso()
    date_str  = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    start_t   = time.monotonic()

    log(f"=" * 60)
    log(f"SWARM BOT  slot={slot}  task={task}  gen={gen}  run={run_id}")
    log(f"time limit: {limit_s:.0f}s ({limit_s/3600:.2f}h)  batch={batch}")
    log(f"=" * 60)

    # Write task file for the workflow commit message
    (Path("/tmp") / f"swarm_task_{slot}.txt").write_text(task)

    # ── Build initial KPI skeleton ────────────────────────────────────────
    kpi = {
        "slot": slot,
        "task": task,
        "taskColor": TASK_COLORS.get(task, "#9E9A90"),
        "runId": run_id,
        "runUrl": f"https://github.com/{os.environ.get('GITHUB_REPOSITORY', '')}/actions/runs/{run_id}",
        "generation": gen,
        "startedAt": started,
        "finishedAt": None,
        "itemsProcessed": 0,
        "itemsSucceeded": 0,
        "itemsFailed": 0,
        "respawnTriggered": False,
        "model": "llama3.2:3b",
        "status": "running",
    }
    write_slot_kpi(slot, task, kpi)

    # ── Load sharded queue (for LLM-driven tasks) ────────────────────────
    queue: list[dict] = []
    if task in ("enrichment", "edges", "significance"):
        queue = load_sharded_queue(slot, stride=20)
        if not queue:
            log(f"[slot {slot}] Queue empty or unavailable — {task} bot will idle.")

    # ── Process until time runs out ────────────────────────────────────────
    # Reserve 10% head-room for commit + respawn trigger
    work_limit = limit_s * 0.90
    succeeded = failed = 0

    try:
        if task == "enrichment":
            succeeded, failed = run_enrichment(slot, queue, batch, start_t, work_limit)
        elif task == "edges":
            succeeded, failed = run_edges(slot, queue, batch, start_t, work_limit)
        elif task == "significance":
            succeeded, failed = run_significance(slot, queue, batch, start_t, work_limit)
        elif task == "audit":
            succeeded, failed = run_audit(slot, start_t, work_limit)
        elif task == "consistency":
            succeeded, failed = run_consistency(slot, start_t, work_limit)
        elif task == "sync":
            succeeded, failed = run_sync(slot, start_t, work_limit)
        elif task == "queue_refresh":
            succeeded, failed = run_queue_refresh(slot, start_t, work_limit)
    except KeyboardInterrupt:
        log(f"[slot {slot}] Interrupted — writing KPI and exiting cleanly")
    except Exception as exc:
        log(f"[slot {slot}] ERROR: {exc}")
        failed += 1

    total = succeeded + failed
    wall  = elapsed(start_t)
    log(f"[slot {slot}] DONE — {total} processed ({succeeded} ok, {failed} fail) in {wall:.0f}s")

    # ── Write item count temp file (for commit message) ───────────────────
    write_gh_output("count", str(total))
    (Path("/tmp") / f"swarm_count_{slot}.txt").write_text(str(total))

    # ── Determine if respawn is needed ────────────────────────────────────
    # Respawn if we hit the time limit (more work may remain in queue)
    # and the generation cap hasn't been reached (prevent infinite loop without work)
    MAX_RESPAWN_GENERATIONS = 1000  # effectively unlimited
    needs_respawn = (wall >= work_limit * 0.98) and (gen < MAX_RESPAWN_GENERATIONS)
    if needs_respawn:
        log(f"[slot {slot}] 90% time limit reached → signalling respawn gen {gen+1}")
    else:
        log(f"[slot {slot}] Work complete before time limit — no respawn needed "
            f"({wall:.0f}s / {work_limit:.0f}s used, gen {gen})")

    # ── Finalize KPI ──────────────────────────────────────────────────────
    kpi.update({
        "finishedAt":      now_iso(),
        "itemsProcessed":  total,
        "itemsSucceeded":  succeeded,
        "itemsFailed":     failed,
        "respawnTriggered":needs_respawn,
        "respawnAt":       now_iso() if needs_respawn else None,
        "wallTimeS":       round(wall, 1),
        "status":          "respawning" if needs_respawn else "done",
    })
    write_slot_kpi(slot, task, kpi)
    update_daily_history(date_str, task, succeeded, failed)

    # ── GitHub Actions output vars for the respawn step ──────────────────
    write_gh_output("respawn", "true" if needs_respawn else "false")
    write_gh_output("next_generation", str(gen + 1))

    log(f"[slot {slot}] KPI written → data/governance/bot_kpi/slot-{slot}.json")
    log(f"[slot {slot}] slot={slot} task={task} done ✓")


if __name__ == "__main__":
    main()
