#!/usr/bin/env python3
"""Orphans audit — git-first.

Finds entities with zero relationships in `detailsJson.relationships`.
Replaces functions/audit-orphans/.
"""
from __future__ import annotations

import datetime as dt
from collections import Counter
from typing import Any

from scripts.audits import iter_entities, parse_details, write_report


def main() -> None:
    orphans: list[dict[str, Any]] = []
    by_label: Counter[str] = Counter()
    by_era: Counter[str] = Counter()
    total = 0

    for ent in iter_entities():
        total += 1
        details = parse_details(ent)
        rels = details.get("relationships") or []
        if isinstance(rels, list) and len(rels) == 0:
            label = ent.get("label") or "Unknown"
            era = ent.get("era") or "Unknown"
            by_label[label] += 1
            by_era[era] += 1
            orphans.append({
                "slug": ent.get("slug", ""),
                "name": ent.get("name", ""),
                "label": label,
                "era": era,
                "callNumber": ent.get("callNumber", ""),
                "importance": ent.get("importanceScore", 0),
            })

    orphans.sort(key=lambda r: -(r["importance"] or 0))
    payload = {
        "generatedAt": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "git",
        "summary": {"orphans": len(orphans), "scanned": total},
        "totalScanned": total,
        "orphanCount": len(orphans),
        "orphanRate": round(len(orphans) / total * 100, 2) if total else 0.0,
        "byLabel": dict(by_label.most_common()),
        "byEra": dict(by_era.most_common()),
        "topOrphans": orphans[:500],
    }
    out = write_report("orphans", payload)
    print(f"orphans: {len(orphans)}/{total} entities have no relationships → {out}")


if __name__ == "__main__":
    main()
