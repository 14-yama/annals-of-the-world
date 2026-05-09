#!/usr/bin/env python3
"""Classification audit — git-first.

Validates Dewey-style call numbers (Class.Division-slug) and reports entities
in invalid classes/divisions, mismatches between callNumber prefix and the
folder it's stored in.

Replaces functions/audit-classification/.
"""
from __future__ import annotations

import datetime as dt
from collections import Counter
from pathlib import Path
from typing import Any

from scripts.audits import (
    ENTITIES_DIR, iter_entity_files, parse_details, write_report,
)
import json

VALID_CLASSES = set("0123456789")


def main() -> None:
    issues: list[dict[str, Any]] = []
    counts: Counter[str] = Counter()
    total = 0

    for path in iter_entity_files():
        rel = path.relative_to(ENTITIES_DIR)
        # rel like 014-Class-014/01401-theocracy-concept.json
        folder_class = rel.parts[0][:1] if rel.parts else ""
        try:
            with path.open("r", encoding="utf-8") as fh:
                data = json.load(fh)
        except (OSError, json.JSONDecodeError):
            counts["unparseable_file"] += 1
            continue
        for ent in data.get("entities", []):
            total += 1
            slug = ent.get("slug", "")
            callnum = ent.get("callNumber", "")
            if not callnum:
                counts["missing_callNumber"] += 1
                if len(issues) < 1000:
                    issues.append({"kind": "missing_callNumber", "slug": slug,
                                   "file": str(rel)})
                continue
            cls = callnum[:1]
            if cls not in VALID_CLASSES:
                counts["invalid_class"] += 1
                if len(issues) < 1000:
                    issues.append({"kind": "invalid_class", "slug": slug,
                                   "callNumber": callnum, "file": str(rel)})
            elif folder_class and cls != folder_class:
                counts["folder_class_mismatch"] += 1
                if len(issues) < 1000:
                    issues.append({"kind": "folder_class_mismatch", "slug": slug,
                                   "callNumber": callnum, "folder": folder_class,
                                   "file": str(rel)})

    payload = {
        "generatedAt": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "git",
        "summary": {"issues": sum(counts.values()), "scanned": total},
        "totalScanned": total,
        "issueCounts": dict(counts.most_common()),
        "totalIssues": sum(counts.values()),
        "sampleIssues": issues,
    }
    out = write_report("classification", payload)
    print(f"classification: {sum(counts.values())} issues across {total} entities → {out}")


if __name__ == "__main__":
    main()
