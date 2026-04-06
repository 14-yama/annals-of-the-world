#!/usr/bin/env python3
"""
Daily Orphan Audit

Finds entities with zero relationships in their detailsJson.
Samples across all labels and flags entities that are disconnected
from the knowledge graph.

Output: reports/daily_orphans_YYYY-MM-DD.json
"""

import json
import sys
from datetime import date
from pathlib import Path

from config import (
    get_client, doc_field, parse_details,
    LABELS, DATABASE_ID, COLLECTION_ID,
)

REPORT_DIR = Path(__file__).resolve().parent.parent.parent / "reports"


def main(sample_per_label: int = 100):
    from appwrite.query import Query

    _, db = get_client()
    print(f"Sampling {sample_per_label} entities per label for orphan check…")

    orphans = []
    total_sampled = 0

    for label in LABELS:
        res = db.list_documents(
            DATABASE_ID, COLLECTION_ID,
            queries=[Query.equal("label", label), Query.limit(sample_per_label)],
        )
        docs = res["documents"] if isinstance(res, dict) else res.documents
        total_sampled += len(docs)

        for doc in docs:
            details = parse_details(doc)
            rels = details.get("relationships", [])
            if len(rels) == 0:
                orphans.append({
                    "slug": doc_field(doc, "slug", ""),
                    "name": doc_field(doc, "name", ""),
                    "label": label,
                    "era": doc_field(doc, "era", ""),
                    "importance": doc_field(doc, "importanceScore", 0),
                    "callNumber": doc_field(doc, "callNumber", ""),
                })

    orphans.sort(key=lambda o: -(o.get("importance") or 0))

    by_label = {}
    for o in orphans:
        by_label.setdefault(o["label"], []).append(o["slug"])

    report = {
        "date": str(date.today()),
        "total_sampled": total_sampled,
        "orphan_count": len(orphans),
        "orphan_rate_pct": round(len(orphans) / total_sampled * 100, 1) if total_sampled else 0,
        "by_label": {k: len(v) for k, v in by_label.items()},
        "top_orphans": orphans[:100],
    }

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    outpath = REPORT_DIR / f"daily_orphans_{date.today()}.json"
    outpath.write_text(json.dumps(report, indent=2))
    print(f"Report written: {outpath}")
    print(f"  Sampled: {total_sampled}  |  Orphans: {len(orphans)} ({report['orphan_rate_pct']}%)")
    for label, count in sorted(by_label.items(), key=lambda x: -len(x[1])):
        print(f"  {label:15s}: {count}")


if __name__ == "__main__":
    per_label = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    main(per_label)
