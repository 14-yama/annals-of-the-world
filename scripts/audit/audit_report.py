#!/usr/bin/env python3
"""
Audit Report Generator

Master script that runs all audit checks and produces a unified report.
Designed to be called from CI or as a cron job.

Usage:
    python audit_report.py              # Full audit
    python audit_report.py --quick      # Quick sample audit (200 entities)

Output: reports/audit_report_YYYY-MM-DD.json
"""

import json
import sys
import time
from datetime import date
from pathlib import Path
from collections import Counter

from config import (
    get_client, doc_field, parse_details,
    LABELS, ERAS, DATABASE_ID, COLLECTION_ID,
)

REPORT_DIR = Path(__file__).resolve().parent.parent.parent / "reports"

QUALITY_DIMS = [
    "relationships", "causes", "effects", "frameworks",
    "places", "texts", "image", "wikidata", "summary",
]


def score_entity(doc: dict) -> dict:
    details = parse_details(doc)
    missing = []
    rels = details.get("relationships", [])
    if not rels:
        missing.append("relationships")
    if not details.get("causes"):
        missing.append("causes")
    if not details.get("effects"):
        missing.append("effects")
    if not (doc_field(doc, "frameworks") or []):
        missing.append("frameworks")
    if not details.get("places"):
        missing.append("places")
    if not details.get("texts"):
        missing.append("texts")
    if not doc_field(doc, "imageUrl"):
        missing.append("image")
    if not doc_field(doc, "wikidataQid"):
        missing.append("wikidata")
    if len(doc_field(doc, "summary", "") or "") < 50:
        missing.append("summary")

    return {
        "slug": doc_field(doc, "slug", ""),
        "name": doc_field(doc, "name", ""),
        "label": doc_field(doc, "label", ""),
        "era": doc_field(doc, "era", ""),
        "importance": doc_field(doc, "importanceScore", 0),
        "score": len(QUALITY_DIMS) - len(missing),
        "missing": missing,
        "relCount": len(rels),
    }


def main():
    from appwrite.query import Query

    quick = "--quick" in sys.argv
    sample_per_label = 25 if quick else 100
    label_str = "quick" if quick else "full"

    _, db = get_client()
    started = time.time()
    print(f"Running {label_str} audit ({sample_per_label}/label)…\n")

    # ── 1. Population counts ──
    print("Phase 1: Counting entities…")
    counts = {}
    total = 0
    for label in LABELS:
        res = db.list_documents(
            DATABASE_ID, COLLECTION_ID,
            queries=[Query.equal("label", label), Query.limit(1)],
        )
        c = res["total"] if isinstance(res, dict) else res.total
        counts[label] = c
        total += c
        print(f"  {label:15s}: {c:>6,}")
    print(f"  {'TOTAL':15s}: {total:>6,}\n")

    era_counts = {}
    for era in ERAS:
        res = db.list_documents(
            DATABASE_ID, COLLECTION_ID,
            queries=[Query.equal("era", era), Query.limit(1)],
        )
        era_counts[era] = res["total"] if isinstance(res, dict) else res.total

    # ── 2. Sample completeness ──
    print("Phase 2: Scoring completeness sample…")
    all_docs = []
    for label in LABELS:
        res = db.list_documents(
            DATABASE_ID, COLLECTION_ID,
            queries=[Query.equal("label", label), Query.limit(sample_per_label)],
        )
        docs = res["documents"] if isinstance(res, dict) else res.documents
        all_docs.extend(docs)

    results = [score_entity(d) for d in all_docs]
    avg_score = sum(r["score"] for r in results) / len(results) if results else 0

    dim_coverage = {}
    for dim in QUALITY_DIMS:
        filled = sum(1 for r in results if dim not in r["missing"])
        dim_coverage[dim] = round(filled / len(results) * 100, 1) if results else 0

    orphan_rate = sum(1 for r in results if r["relCount"] == 0) / len(results) * 100 if results else 0

    critical = [r for r in results if (r["importance"] or 0) >= 5 and r["score"] < 5]
    critical.sort(key=lambda r: -(r["importance"] or 0))

    score_dist = dict(Counter(r["score"] for r in results))

    # ── 3. Era consistency ──
    print("Phase 3: Era consistency…")
    no_era = db.list_documents(
        DATABASE_ID, COLLECTION_ID, queries=[Query.equal("era", ""), Query.limit(1)]
    )
    no_era_count = no_era["total"] if isinstance(no_era, dict) else no_era.total

    no_div = db.list_documents(
        DATABASE_ID, COLLECTION_ID, queries=[Query.equal("eraDivisionCode", ""), Query.limit(1)]
    )
    no_div_count = no_div["total"] if isinstance(no_div, dict) else no_div.total

    elapsed = round(time.time() - started, 1)

    # ── Build report ──
    report = {
        "date": str(date.today()),
        "mode": label_str,
        "elapsed_sec": elapsed,
        "population": {
            "total": total,
            "by_label": counts,
            "by_era": era_counts,
        },
        "completeness": {
            "sample_size": len(results),
            "avg_score": round(avg_score, 2),
            "dim_coverage_pct": dim_coverage,
            "orphan_rate_pct": round(orphan_rate, 1),
            "score_distribution": score_dist,
        },
        "critical": {
            "count": len(critical),
            "entities": critical[:30],
        },
        "era_consistency": {
            "no_era": no_era_count,
            "no_division_code": no_div_count,
        },
        "health_grade": _grade(avg_score, orphan_rate, no_era_count + no_div_count),
    }

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    outpath = REPORT_DIR / f"audit_report_{date.today()}.json"
    outpath.write_text(json.dumps(report, indent=2))
    print(f"\nReport written: {outpath}  ({elapsed}s)")
    print(f"  Health Grade: {report['health_grade']}")
    print(f"  Average score: {avg_score:.2f}/9")
    print(f"  Orphan rate: {orphan_rate:.1f}%")
    print(f"  Critical entities: {len(critical)}")


def _grade(avg_score: float, orphan_pct: float, era_issues: int) -> str:
    """Compute a letter grade from audit metrics."""
    points = avg_score * 10  # 0-90
    if orphan_pct > 50:
        points -= 30
    elif orphan_pct > 20:
        points -= 15
    if era_issues > 1000:
        points -= 20
    elif era_issues > 100:
        points -= 10

    if points >= 75:
        return "A"
    if points >= 60:
        return "B"
    if points >= 45:
        return "C"
    if points >= 30:
        return "D"
    return "F"


if __name__ == "__main__":
    main()
