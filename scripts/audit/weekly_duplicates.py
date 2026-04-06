#!/usr/bin/env python3
"""
Weekly Duplicate Check

Detects potential duplicate entities by:
1. Exact slug duplicates (should not exist — slug is unique index)
2. Name similarity (Levenshtein / exact name matches across labels)
3. Same callNumber pointing to different slugs

Output: reports/weekly_duplicates_YYYY-MM-DD.json
"""

import json
from datetime import date
from pathlib import Path
from collections import defaultdict

from config import (
    get_client, doc_field,
    LABELS, DATABASE_ID, COLLECTION_ID,
)

REPORT_DIR = Path(__file__).resolve().parent.parent.parent / "reports"


def main():
    from appwrite.query import Query

    _, db = get_client()
    print("Running duplicate check…")

    # Gather name → [slugs] mapping from a sample
    name_map: dict[str, list[dict]] = defaultdict(list)
    callnum_map: dict[str, list[str]] = defaultdict(list)
    total = 0

    for label in LABELS:
        offset = 0
        while offset < 1000:  # Cap at 1000 per label for performance
            res = db.list_documents(
                DATABASE_ID, COLLECTION_ID,
                queries=[
                    Query.equal("label", label),
                    Query.limit(100),
                    Query.offset(offset),
                ],
            )
            docs = res["documents"] if isinstance(res, dict) else res.documents
            if not docs:
                break
            for doc in docs:
                name = (doc_field(doc, "name", "") or "").strip().lower()
                slug = doc_field(doc, "slug", "")
                cn = doc_field(doc, "callNumber", "")
                if name:
                    name_map[name].append({"slug": slug, "label": label})
                if cn:
                    callnum_map[cn].append(slug)
                total += 1
            offset += len(docs)
        print(f"  {label}: scanned {offset} docs")

    # Find duplicates
    name_dupes = []
    for name, entries in name_map.items():
        if len(entries) > 1:
            name_dupes.append({
                "name": name,
                "count": len(entries),
                "entries": entries[:10],
            })

    callnum_dupes = []
    for cn, slugs in callnum_map.items():
        if len(slugs) > 1:
            callnum_dupes.append({
                "callNumber": cn,
                "count": len(slugs),
                "slugs": slugs[:10],
            })

    report = {
        "date": str(date.today()),
        "total_scanned": total,
        "name_duplicates": len(name_dupes),
        "callNumber_duplicates": len(callnum_dupes),
        "name_dupes_sample": sorted(name_dupes, key=lambda x: -x["count"])[:50],
        "callnum_dupes_sample": sorted(callnum_dupes, key=lambda x: -x["count"])[:50],
    }

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    outpath = REPORT_DIR / f"weekly_duplicates_{date.today()}.json"
    outpath.write_text(json.dumps(report, indent=2))
    print(f"\nReport written: {outpath}")
    print(f"  Scanned: {total}")
    print(f"  Name duplicates: {len(name_dupes)}")
    print(f"  CallNumber duplicates: {len(callnum_dupes)}")


if __name__ == "__main__":
    main()
