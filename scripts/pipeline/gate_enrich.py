"""
gate_enrich.py — Second gate: dispatch triaged entities to the LLM enricher.

Wraps the existing `scripts/ai_enrich_autonomous.py` so that:
  1. Only entities in state='triaged' with attempts<MAX are eligible.
  2. Selected entities are marked 'in-flight' (claim) before the LLM runs.
  3. After enrichment, state is reset to 'triaged' (validate will re-check) and
     attempts is incremented.
  4. Output the existing pipeline expects (`data/enrichment/queue.json`) is
     produced, then `ai_enrich_autonomous.py` is invoked as a subprocess.

Usage:
    python3 scripts/pipeline/gate_enrich.py --count 25
    python3 scripts/pipeline/gate_enrich.py --count 25 --model ollama
    python3 scripts/pipeline/gate_enrich.py --count 25 --dry-run
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from scripts.pipeline.pipeline_state import (  # noqa: E402
    REPO_ROOT,
    EntityRecord,
    iter_entities,
    set_state,
    _now,
    _atomic_write,
)

QUEUE_FILE = REPO_ROOT / "data" / "enrichment" / "queue.json"
REPORT_FILE = REPO_ROOT / "data" / "pipeline" / "enrich_report.json"
ENRICH_SCRIPT = REPO_ROOT / "scripts" / "ai_enrich_autonomous.py"
MAX_ENRICH_ATTEMPTS = 3


def _weakness_score(rec: EntityRecord) -> float:
    """Higher = needs more work and is worth enriching. Mirrors enrichment_queue logic."""
    summary_len = len(rec.summary or "")
    if summary_len >= 800:
        return 0.0
    weakness = max(0.0, (800 - summary_len) / 800 * 50)

    causes = rec.details.get("causes") or []
    effects = rec.details.get("effects") or []
    rels = rec.details.get("relationships") or []

    if not causes: weakness += 6
    if not effects: weakness += 6
    if len(rels) < 3: weakness += 8

    # Boost by importance — high-importance weak entities take priority
    weakness += rec.importance_score * 2

    # Penalty for already-tried attempts
    attempts = int(rec.pipeline_state.get("attempts") or 0)
    weakness -= attempts * 15

    return weakness


def select_candidates(count: int) -> list[EntityRecord]:
    """Pick top-N triaged entities ranked by weakness score."""
    print(f"[enrich] scanning triaged entities (need top {count})…", flush=True)
    scored: list[tuple[float, EntityRecord]] = []
    scanned = 0
    for rec in iter_entities(state_filter={"triaged"}):
        scanned += 1
        attempts = int(rec.pipeline_state.get("attempts") or 0)
        if attempts >= MAX_ENRICH_ATTEMPTS:
            continue
        score = _weakness_score(rec)
        if score <= 0:
            continue  # already strong; validate gate will promote
        scored.append((score, rec))
    scored.sort(key=lambda x: -x[0])
    top = [rec for _, rec in scored[:count]]
    print(f"[enrich] scanned {scanned:,} triaged, picked top {len(top)} by weakness", flush=True)
    return top


def write_queue(records: list[EntityRecord]) -> None:
    """Produce queue.json in the shape ai_enrich_autonomous.py expects."""
    queue = []
    for rec in records:
        queue.append({
            "slug": rec.slug,
            "filepath": str(rec.file_path),  # ai_enrich_autonomous needs this
            "label": rec.label,
            "name": rec.name or rec.raw.get("name") or rec.slug,
            "callNumber": rec.raw.get("callNumber"),
            "era": rec.raw.get("era"),
            "summary": rec.summary,
            "importanceScore": rec.importance_score,
            "wikidataQid": rec.wikidata_qid,
            "score": _weakness_score(rec),
        })
    QUEUE_FILE.parent.mkdir(parents=True, exist_ok=True)
    _atomic_write(QUEUE_FILE, {
        "generatedAt": _now(),
        "source": "gate_enrich.py",
        "count": len(queue),
        "queue": queue,  # ai_enrich_autonomous expects key "queue", not "entities"
    })
    print(f"[enrich] wrote queue: {QUEUE_FILE} ({len(queue)} entities)", flush=True)


def claim_records(records: list[EntityRecord]) -> None:
    """Mark each selected entity as in-flight (atomic, increments attempts)."""
    for rec in records:
        set_state(rec, "in-flight", gate="enrich",
                  reason="claimed-for-llm",
                  extra={"queuedAt": _now()})


def release_records(records: list[EntityRecord]) -> None:
    """After LLM run, drop back to triaged so validate can re-check."""
    for rec in records:
        # Re-read fresh state since the enricher may have updated other fields
        set_state(rec, "triaged", gate="enrich",
                  reason="llm-completed")


def invoke_enricher(count: int, model: str, dry_run: bool) -> int:
    """Run the existing autonomous enricher. Returns its exit code."""
    cmd = [
        sys.executable, str(ENRICH_SCRIPT),
        "--count", str(count),
        "--model", model,
    ]
    if dry_run:
        cmd.append("--dry-run")
    print(f"[enrich] invoking: {' '.join(cmd)}", flush=True)
    started = time.time()
    proc = subprocess.run(cmd, cwd=str(REPO_ROOT))
    print(f"[enrich] enricher exited {proc.returncode} after {time.time()-started:.1f}s", flush=True)
    return proc.returncode


def run(count: int, model: str, dry_run: bool) -> dict:
    started = time.time()
    records = select_candidates(count)
    if not records:
        print("[enrich] nothing to enrich — queue empty", flush=True)
        return {"selected": 0, "elapsed": 0}

    if not dry_run:
        claim_records(records)
    write_queue(records)

    exit_code = invoke_enricher(count, model, dry_run)

    if not dry_run:
        release_records(records)

    summary = {
        "generatedAt": _now(),
        "selected": len(records),
        "model": model,
        "dryRun": dry_run,
        "enricherExitCode": exit_code,
        "elapsedSec": round(time.time() - started, 1),
    }
    _atomic_write(REPORT_FILE, summary)
    print(f"\n[enrich] complete — {summary}", flush=True)
    return summary


def main():
    p = argparse.ArgumentParser(description="Enrichment gate — dispatch triaged entities to LLM")
    p.add_argument("--count", type=int, default=25, help="Number of entities to enrich this run")
    p.add_argument("--model", default="gemini", choices=["gemini", "openai", "ollama"])
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    run(count=args.count, model=args.model, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
