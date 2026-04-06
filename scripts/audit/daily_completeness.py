#!/usr/bin/env python3
"""
Daily Completeness Audit

Scores a sample (default 500) of entities on 9 quality dimensions:
  relationships, causes, effects, frameworks, places, texts, image, wikidata, summary

Outputs JSON report: reports/daily_completeness_YYYY-MM-DD.json
"""

import json
import sys
from datetime import date
from pathlib import Path
from collections import Counter

from config import (
    get_client, fetch_all, doc_field, parse_details,
    LABELS, ERAS, DATABASE_ID, COLLECTION_ID,
)

QUALITY_DIMS = [
    "relationships", "causes", "effects", "frameworks",
    "places", "texts", "image", "wikidata", "summary",
]

REPORT_DIR = Path(__file__).resolve().parent.parent.parent / "reports"


def score_entity(doc: dict) -> dict:
    """Score a single entity on all 9 dimensions. Returns result dict."""
    details = parse_details(doc)
    slug = doc_field(doc, "slug", "")
    name = doc_field(doc, "name", "")
    label = doc_field(doc, "label", "")
    era = doc_field(doc, "era", "")
    importance = doc_field(doc, "importanceScore", 0)

    rels = details.get("relationships", [])
    causes = details.get("causes", [])
    effects = details.get("effects", [])
    frameworks = doc_field(doc, "frameworks", []) or []
    places = details.get("places", [])
    texts = details.get("texts", [])
    image = doc_field(doc, "imageUrl", "")
    wikidata = doc_field(doc, "wikidataQid", "")
    summary = doc_field(doc, "summary", "")

    missing = []
    if not rels:
        missing.append("relationships")
    if not causes:
        missing.append("causes")
    if not effects:
        missing.append("effects")
    if not frameworks:
        missing.append("frameworks")
    if not places:
        missing.append("places")
    if not texts:
        missing.append("texts")
    if not image:
        missing.append("image")
    if not wikidata:
        missing.append("wikidata")
    if len(summary or "") < 50:
        missing.append("summary")

    return {
        "slug": slug,
        "name": name,
        "label": label,
        "era": era,
        "importance": importance,
        "score": len(QUALITY_DIMS) - len(missing),
        "missing": missing,
        "relCount": len(rels),
    }


def main(sample_size: int = 500):
    from appwrite.query import Query

    _, db = get_client()
    print(f"Fetching {sample_size} entity sample…")

    docs = []
    # Sample across labels evenly
    per_label = max(sample_size // len(LABELS), 10)
    for label in LABELS:
        res = db.list_documents(
            DATABASE_ID, COLLECTION_ID,
            queries=[Query.equal("label", label), Query.limit(per_label)],
        )
        batch = res["documents"] if isinstance(res, dict) else res.documents
        docs.extend(batch)

    print(f"Scoring {len(docs)} entities…")
    results = [score_entity(d) for d in docs]

    # Aggregates
    total = len(results)
    avg_score = sum(r["score"] for r in results) / total if total else 0
    by_label = {}
    for label in LABELS:
        subset = [r for r in results if r["label"] == label]
        if subset:
            by_label[label] = {
                "count": len(subset),
                "avg_score": round(sum(r["score"] for r in subset) / len(subset), 2),
                "orphans": sum(1 for r in subset if r["relCount"] == 0),
            }

    dim_coverage = {}
    for dim in QUALITY_DIMS:
        filled = sum(1 for r in results if dim not in r["missing"])
        dim_coverage[dim] = round(filled / total * 100, 1) if total else 0

    critical = [r for r in results if r["importance"] >= 5 and r["score"] < 5]
    critical.sort(key=lambda r: -r["importance"])

    report = {
        "date": str(date.today()),
        "sample_size": total,
        "avg_score": round(avg_score, 2),
        "by_label": by_label,
        "dim_coverage_pct": dim_coverage,
        "critical_count": len(critical),
        "critical_entities": critical[:50],
        "score_distribution": dict(Counter(r["score"] for r in results)),
    }

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    outpath = REPORT_DIR / f"daily_completeness_{date.today()}.json"
    outpath.write_text(json.dumps(report, indent=2))
    print(f"Report written: {outpath}")
    print(f"  Average score: {avg_score:.2f}/9  |  Critical: {len(critical)}")
    for dim, pct in dim_coverage.items():
        print(f"  {dim:15s}: {pct:5.1f}%")


if __name__ == "__main__":
    size = int(sys.argv[1]) if len(sys.argv) > 1 else 500
    main(size)
