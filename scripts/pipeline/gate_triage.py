"""
gate_triage.py — First gate: filter out entities not worth LLM enrichment.

Rules (all reasons logged to _pipelineState.lastReason):
  REJECT:
    - duplicate-slug-lesser : another entity with same slug has more content
    - wikidata-stub-no-edges: importanceScore<3 AND no relationships AND summary<50c AND has wikidataQid
    - empty-stub           : no summary, no relationships, no causes/effects
    - slug-invalid         : missing or malformed slug

  PASS → state=triaged
    - Anything not rejected. Pre-existing high-quality entities go straight here
      and will be fast-tracked through validate (skipping enrich) by run_pipeline.

Output:
    - Updates _pipelineState in each entity file
    - Writes data/pipeline/triage_report.json with rejection breakdown
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from collections import defaultdict
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

# Allow lowercase ASCII + Unicode letters/marks/numbers + hyphens.
# Many catalog slugs include diacritics (e.g. "claude-lévi-strauss").
SLUG_RE = re.compile(r"^[\w][\w\-]{1,200}$", re.UNICODE)
REPORT_FILE = REPO_ROOT / "data" / "pipeline" / "triage_report.json"


def _content_score(rec: EntityRecord) -> int:
    """Bigger = more content. Used to pick winner among duplicate slugs."""
    summary_len = len(rec.summary or "")
    rels = len(rec.details.get("relationships") or [])
    causes = len(rec.details.get("causes") or [])
    effects = len(rec.details.get("effects") or [])
    return summary_len + (rels * 50) + (causes * 30) + (effects * 30) + (rec.importance_score * 20)


def _classify(rec: EntityRecord) -> tuple[str, str]:
    """Return (state, reason). state ∈ {'triaged', 'rejected'}."""
    if not rec.slug or not SLUG_RE.match(rec.slug):
        return "rejected", "slug-invalid"

    summary_len = len(rec.summary or "")
    rels = rec.details.get("relationships") or []
    causes = rec.details.get("causes") or []
    effects = rec.details.get("effects") or []
    has_hs = bool(rec.raw.get("historicalSignificance"))

    has_content = bool(rels or causes or effects or summary_len >= 50)
    if not has_content:
        return "rejected", "empty-stub"

    # Wikidata thin-stub: very common — has QID but minimal narrative.
    # The era/place auto-edges (rels=1-2) don't constitute real content.
    if (rec.wikidata_qid
            and summary_len < 200
            and len(rels) < 3
            and not causes
            and not effects
            and not has_hs
            and rec.importance_score < 5):
        return "rejected", "wikidata-thin-stub"

    # Orphan stub: no QID and basically empty narrative
    if (summary_len < 150
            and len(rels) < 2
            and not causes
            and not effects
            and not has_hs):
        return "rejected", "orphan-empty"

    # Anything else passes
    return "triaged", ""


def run(limit: int | None = None, dry_run: bool = False) -> dict:
    print(f"[triage] starting — REPO_ROOT={REPO_ROOT}", flush=True)
    started = time.time()

    # First pass: scan & group by slug to detect duplicates
    print("[triage] pass 1/2 — scanning for duplicate slugs…", flush=True)
    slug_owners: dict[str, tuple[Path, int, int]] = {}  # slug → (path, idx, score)
    scanned = 0
    for rec in iter_entities(limit=limit):
        scanned += 1
        if scanned % 50_000 == 0:
            print(f"  …scanned {scanned:,}", flush=True)
        score = _content_score(rec)
        prev = slug_owners.get(rec.slug)
        if prev is None or score > prev[2]:
            slug_owners[rec.slug] = (rec.file_path, rec.index_in_file, score)
    print(f"[triage] scanned {scanned:,} entities, {len(slug_owners):,} unique slugs", flush=True)

    # Second pass: classify + write state
    print("[triage] pass 2/2 — classifying & writing state…", flush=True)
    counts: dict[str, int] = defaultdict(int)
    by_reason: dict[str, int] = defaultdict(int)
    processed = 0

    for rec in iter_entities(limit=limit):
        processed += 1
        if processed % 25_000 == 0:
            elapsed = time.time() - started
            rate = processed / elapsed if elapsed > 0 else 0
            print(f"  …processed {processed:,} ({rate:.0f}/s) — pass={counts['triaged']:,} reject={counts['rejected']:,}", flush=True)

        # Skip if already enriched/validated/in-flight (idempotent).
        # Re-evaluate pending + triaged so tightened rules can demote stubs.
        existing_state = rec.pipeline_state.get("state", "pending")
        if existing_state in ("in-flight", "validated"):
            counts[existing_state] += 1
            continue

        # Duplicate slug: if this entity isn't the chosen owner, reject it
        owner = slug_owners.get(rec.slug)
        if owner and (owner[0] != rec.file_path or owner[1] != rec.index_in_file):
            new_state, reason = "rejected", "duplicate-slug-lesser"
        else:
            new_state, reason = _classify(rec)

        counts[new_state] += 1
        by_reason[reason or "pass"] += 1

        if not dry_run:
            set_state(rec, new_state, gate="triage", reason=reason)

    elapsed = time.time() - started
    summary = {
        "generatedAt": _now(),
        "elapsedSec": round(elapsed, 1),
        "scanned": scanned,
        "uniqueSlugs": len(slug_owners),
        "counts": dict(counts),
        "byReason": dict(by_reason),
        "dryRun": dry_run,
    }
    if not dry_run:
        _atomic_write(REPORT_FILE, summary)
    print(f"\n[triage] complete in {elapsed:.1f}s — {dict(counts)}", flush=True)
    print(f"[triage] rejection reasons: {dict(by_reason)}", flush=True)
    if not dry_run:
        print(f"[triage] report: {REPORT_FILE}", flush=True)
    return summary


def main():
    p = argparse.ArgumentParser(description="Triage gate — filter entities pre-LLM")
    p.add_argument("--limit", type=int, default=None, help="Cap entity scan (for testing)")
    p.add_argument("--dry-run", action="store_true", help="Classify but don't write state")
    args = p.parse_args()
    run(limit=args.limit, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
