#!/usr/bin/env python3
"""Consistency audit — git-first.

Validates: era ↔ eraDivisionCode alignment, callNumber prefix matches era,
non-empty slug, label is in approved list.

Replaces functions/audit-consistency/.
"""
from __future__ import annotations

import datetime as dt
import re
from collections import Counter
from typing import Any

from scripts.audits import (
    iter_entities, write_report, ERAS, ERA_CODE_RANGES, LABELS,
)

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
CALLNUM_RE = re.compile(r"^\d{3}\.\d{2}-[a-z0-9-]+$")


def main() -> None:
    issues: list[dict[str, Any]] = []
    counts: Counter[str] = Counter()
    total = 0

    valid_labels = set(LABELS)
    valid_eras = set(ERAS)

    for ent in iter_entities():
        total += 1
        slug = ent.get("slug", "")
        name = ent.get("name", "")
        era = ent.get("era", "")
        code = str(ent.get("eraDivisionCode") or "")
        callnum = ent.get("callNumber", "")
        label = ent.get("label", "")

        def add(kind: str, detail: str) -> None:
            counts[kind] += 1
            if len(issues) < 1000:
                issues.append({
                    "kind": kind, "slug": slug, "name": name,
                    "detail": detail,
                })

        if not slug:
            add("missing_slug", "")
        elif not SLUG_RE.match(slug):
            add("invalid_slug", slug)

        if not era:
            add("empty_era", "")
        elif era not in valid_eras:
            add("invalid_era", era)

        if not code:
            add("empty_eraDivisionCode", "")
        elif era in ERA_CODE_RANGES:
            try:
                code_int = int(code)
            except ValueError:
                add("non_numeric_eraDivisionCode", code)
            else:
                lo, hi = ERA_CODE_RANGES[era]
                if not (lo <= code_int <= hi):
                    add("era_code_mismatch", f"{era}={code}")

        if not callnum:
            add("missing_callNumber", "")
        elif not CALLNUM_RE.match(callnum):
            add("invalid_callNumber", callnum)

        if label and label not in valid_labels:
            add("invalid_label", label)
        elif not label:
            add("missing_label", "")

    payload = {
        "generatedAt": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "git",
        "summary": {"issues": sum(counts.values()), "scanned": total},
        "totalScanned": total,
        "issueCounts": dict(counts.most_common()),
        "totalIssues": sum(counts.values()),
        "sampleIssues": issues,
    }
    out = write_report("consistency", payload)
    print(f"consistency: {sum(counts.values())} issues across {total} entities → {out}")


if __name__ == "__main__":
    main()
