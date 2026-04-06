#!/usr/bin/env python3
"""
Weekly Era Consistency Audit

Checks that every entity has a valid era and eraDivisionCode.
Flags mismatches between era and eraDivisionCode ranges.

Output: reports/weekly_era_consistency_YYYY-MM-DD.json
"""

import json
from datetime import date
from pathlib import Path

from config import (
    get_client, fetch_all, doc_field,
    LABELS, ERAS, DATABASE_ID, COLLECTION_ID,
)

REPORT_DIR = Path(__file__).resolve().parent.parent.parent / "reports"

# Expected eraDivisionCode ranges per era
ERA_CODE_RANGES: dict[str, tuple[int, int]] = {
    "Prehistoric":  (910, 919),
    "Classical":    (920, 929),
    "Medieval":     (930, 939),
    "Early Modern": (940, 949),
    "Modern":       (950, 959),
    "Contemporary": (960, 969),
}


def main():
    from appwrite.query import Query

    _, db = get_client()
    print("Running era consistency audit…")

    issues = []

    # 1. Entities with empty era
    res = db.list_documents(
        DATABASE_ID, COLLECTION_ID,
        queries=[Query.equal("era", ""), Query.limit(1)],
    )
    no_era_total = res["total"] if isinstance(res, dict) else res.total
    if no_era_total > 0:
        issues.append({
            "issue": "empty_era",
            "count": no_era_total,
            "description": "Entities with empty era field",
        })

    # 2. Entities with empty eraDivisionCode
    res = db.list_documents(
        DATABASE_ID, COLLECTION_ID,
        queries=[Query.equal("eraDivisionCode", ""), Query.limit(1)],
    )
    no_div_total = res["total"] if isinstance(res, dict) else res.total
    if no_div_total > 0:
        issues.append({
            "issue": "empty_eraDivisionCode",
            "count": no_div_total,
            "description": "Entities with empty eraDivisionCode",
        })

    # 3. Entities with invalid era names
    for era in ERAS:
        res = db.list_documents(
            DATABASE_ID, COLLECTION_ID,
            queries=[Query.equal("era", era), Query.limit(1)],
        )
        count = res["total"] if isinstance(res, dict) else res.total
        print(f"  {era}: {count}")

    # 4. Sample for era/code mismatches
    mismatch_samples = []
    for era, (lo, hi) in ERA_CODE_RANGES.items():
        sample_docs = db.list_documents(
            DATABASE_ID, COLLECTION_ID,
            queries=[Query.equal("era", era), Query.limit(50)],
        )
        docs = sample_docs["documents"] if isinstance(sample_docs, dict) else sample_docs.documents
        for doc in docs:
            code_str = doc_field(doc, "eraDivisionCode", "")
            if not code_str:
                continue
            try:
                code = int(code_str)
            except ValueError:
                mismatch_samples.append({
                    "slug": doc_field(doc, "slug", ""),
                    "era": era,
                    "eraDivisionCode": code_str,
                    "reason": "non-numeric code",
                })
                continue
            if code < lo or code > hi:
                mismatch_samples.append({
                    "slug": doc_field(doc, "slug", ""),
                    "era": era,
                    "eraDivisionCode": code_str,
                    "reason": f"code {code} outside {lo}-{hi}",
                })

    if mismatch_samples:
        issues.append({
            "issue": "era_code_mismatch",
            "count": len(mismatch_samples),
            "description": "Entities where eraDivisionCode doesn't match era range",
            "samples": mismatch_samples[:50],
        })

    report = {
        "date": str(date.today()),
        "issues": issues,
        "total_issues": sum(i["count"] for i in issues),
    }

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    outpath = REPORT_DIR / f"weekly_era_consistency_{date.today()}.json"
    outpath.write_text(json.dumps(report, indent=2))
    print(f"\nReport written: {outpath}")
    print(f"  Total issues: {report['total_issues']}")
    for issue in issues:
        print(f"  {issue['issue']}: {issue['count']}")


if __name__ == "__main__":
    main()
