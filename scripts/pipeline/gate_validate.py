"""
gate_validate.py — Third gate: promote enriched entities to entities_clean.

Rules (no LLM):
  PROMOTE → state=validated, written to data/pipeline/clean/{slug}.json
    - summary length 600–3000c
    - summary has ≥2 paragraphs (split on \n\n)
    - ≥1 cause and ≥1 effect
    - relationships count ≥ minEdgesForScore(significanceScore) — defaults to 3
    - has historicalSignificance (any score 1–10)
    - slug, label, era all present

  REJECT → state=rejected, written to data/pipeline/rejected/{slug}.json
    - enrich attempts ≥ 3 (chronic failure)

  DEFER (stay triaged) → needs enrich pass

Output:
    data/pipeline/clean/{slug}.json     — one row per promoted entity (Appwrite-ready)
    data/pipeline/rejected/{slug}.json  — one row per rejection with reason
    data/pipeline/validate_report.json  — counts + per-reason histogram
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from scripts.pipeline.pipeline_state import (  # noqa: E402
    REPO_ROOT,
    CLEAN_DIR,
    REJECTED_DIR,
    EntityRecord,
    iter_entities,
    set_state,
    _now,
    _atomic_write,
)

REPORT_FILE = REPO_ROOT / "data" / "pipeline" / "validate_report.json"
MAX_ENRICH_ATTEMPTS = 3


def min_edges_for_score(score: int | None) -> int:
    """Minimum relationship count per significance score.

    Calibrated to what ai_enrich_autonomous.py produces:
    - enricher targets exactly 5 relationships by default
    - score 9-10 entities (global significance) warrant more edges
    - floor lowered for score 7-8 to match enricher output
    """
    if not score:
        return 3
    if score >= 9: return 8
    if score >= 7: return 5
    if score >= 5: return 3
    if score >= 3: return 2
    return 1


def _paragraph_count(summary: str) -> int:
    return len([p for p in (summary or "").split("\n\n") if p.strip()])


def _validate(rec: EntityRecord) -> tuple[str, str, dict]:
    """Return (state, reason, gate_results)."""
    gate_results: dict = {}

    # Reject: chronic failure
    attempts = int(rec.pipeline_state.get("attempts") or 0)
    if attempts >= MAX_ENRICH_ATTEMPTS and rec.pipeline_state.get("lastGate") == "enrich":
        return "rejected", "max-attempts-exceeded", {"attempts": attempts}

    # Required fields
    if not rec.label:
        return "triaged", "missing-label", {}
    if not rec.raw.get("era"):
        return "triaged", "missing-era", {}

    # Summary quality
    s = rec.summary or ""
    if len(s) < 600:
        return "triaged", "summary-too-short", {"summaryLen": len(s)}
    if len(s) > 3000:
        return "triaged", "summary-too-long", {"summaryLen": len(s)}
    paras = _paragraph_count(s)
    if paras < 2:
        return "triaged", "summary-no-paragraphs", {"paragraphs": paras}
    gate_results["summaryLen"] = len(s)
    gate_results["paragraphs"] = paras

    # Causes & effects
    causes = rec.details.get("causes") or []
    effects = rec.details.get("effects") or []
    if len(causes) < 1:
        return "triaged", "missing-causes", {}
    if len(effects) < 1:
        return "triaged", "missing-effects", {}
    gate_results["causes"] = len(causes)
    gate_results["effects"] = len(effects)

    # Relationships
    rels = rec.details.get("relationships") or []
    hs = rec.raw.get("historicalSignificance") or {}
    if not hs:
        return "triaged", "missing-significance", {}
    score = hs.get("significanceScore") if isinstance(hs, dict) else None
    floor = min_edges_for_score(score)
    if len(rels) < floor:
        return "triaged", "edges-below-floor", {
            "rels": len(rels), "floor": floor, "score": score,
        }
    gate_results["relationships"] = len(rels)
    gate_results["edgeFloor"] = floor
    gate_results["significanceScore"] = score

    return "validated", "pass", gate_results


def _build_clean_row(rec: EntityRecord, gate_results: dict) -> dict:
    """Shape the row that will be stored in the clean output."""
    return {
        "slug": rec.slug,
        "label": rec.label,
        "name": rec.name or rec.raw.get("name") or rec.slug,
        "callNumber": rec.raw.get("callNumber"),
        "era": rec.raw.get("era"),
        "summary": rec.summary,
        "importanceScore": rec.importance_score,
        "wikidataQid": rec.wikidata_qid,
        "historicalSignificance": rec.raw.get("historicalSignificance"),
        "frameworks": rec.raw.get("frameworks"),
        "subjects": rec.raw.get("subjects"),
        "subjectHeadings": rec.raw.get("subjectHeadings"),
        "places": rec.details.get("places"),
        "texts": rec.details.get("texts"),
        "quote": rec.details.get("quote"),
        "causes": rec.details.get("causes"),
        "effects": rec.details.get("effects"),
        "relationships": rec.details.get("relationships"),
        "pipelineStatus": "promoted",
        "promotedAt": _now(),
        "gateResults": gate_results,
        "enrichmentVersion": 1,
        "sourceFile": str(rec.file_path.relative_to(REPO_ROOT)),
    }


def _build_reject_row(rec: EntityRecord, reason: str, extra: dict) -> dict:
    return {
        "slug": rec.slug,
        "label": rec.label,
        "callNumber": rec.raw.get("callNumber"),
        "era": rec.raw.get("era"),
        "rejectedAt": _now(),
        "reason": reason,
        "details": extra,
        "lastGate": rec.pipeline_state.get("lastGate") or "validate",
        "attempts": rec.pipeline_state.get("attempts") or 0,
        "sourceFile": str(rec.file_path.relative_to(REPO_ROOT)),
    }


def run(limit: int | None = None, dry_run: bool = False) -> dict:
    print(f"[validate] starting — limit={limit} dry_run={dry_run}", flush=True)
    started = time.time()

    CLEAN_DIR.mkdir(parents=True, exist_ok=True)
    REJECTED_DIR.mkdir(parents=True, exist_ok=True)

    counts: dict[str, int] = defaultdict(int)
    by_reason: dict[str, int] = defaultdict(int)
    processed = 0

    for rec in iter_entities(state_filter={"triaged", "in-flight"}, limit=limit):
        processed += 1
        if processed % 10_000 == 0:
            elapsed = time.time() - started
            rate = processed / elapsed if elapsed > 0 else 0
            print(f"  …processed {processed:,} ({rate:.0f}/s) — "
                  f"validated={counts['validated']:,} rejected={counts['rejected']:,} "
                  f"deferred={counts['triaged']:,}", flush=True)

        new_state, reason, gate_results = _validate(rec)
        counts[new_state] += 1
        by_reason[reason] += 1

        if dry_run:
            continue

        if new_state == "validated":
            row = _build_clean_row(rec, gate_results)
            shard = (rec.raw.get("callNumber") or "unknown").split(".")[0] or "unknown"
            out = CLEAN_DIR / shard / f"{rec.slug}.json"
            _atomic_write(out, row)
            set_state(rec, "validated", gate="validate", reason="pass",
                      extra={"gateResults": gate_results})
        elif new_state == "rejected":
            row = _build_reject_row(rec, reason, gate_results)
            shard = (rec.raw.get("callNumber") or "unknown").split(".")[0] or "unknown"
            out = REJECTED_DIR / shard / f"{rec.slug}.json"
            _atomic_write(out, row)
            set_state(rec, "rejected", gate="validate", reason=reason)
        else:
            # Stays triaged; just record why it didn't pass yet
            set_state(rec, "triaged", gate="validate", reason=reason)

    elapsed = time.time() - started
    summary = {
        "generatedAt": _now(),
        "elapsedSec": round(elapsed, 1),
        "processed": processed,
        "counts": dict(counts),
        "byReason": dict(by_reason),
        "dryRun": dry_run,
    }
    if not dry_run:
        _atomic_write(REPORT_FILE, summary)
    print(f"\n[validate] complete in {elapsed:.1f}s — {dict(counts)}", flush=True)
    print(f"[validate] reasons: {dict(by_reason)}", flush=True)
    if not dry_run:
        print(f"[validate] clean rows in: {CLEAN_DIR}", flush=True)
        print(f"[validate] rejected rows in: {REJECTED_DIR}", flush=True)
        print(f"[validate] report: {REPORT_FILE}", flush=True)
    return summary


def main():
    p = argparse.ArgumentParser(description="Validate gate — promote enriched entities to clean")
    p.add_argument("--limit", type=int, default=None)
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    run(limit=args.limit, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
