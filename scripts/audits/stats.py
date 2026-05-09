#!/usr/bin/env python3
"""Stats — git-first.

Counts entities by label, era, continent, class. Writes to
`data/audit-reports/stats.json`. The sync gateway reads this when updating
the Appwrite `stats_cache` collection — replaces the stats-counter function.
"""
from __future__ import annotations

import datetime as dt
from collections import Counter

from scripts.audits import iter_entities, write_report


def main() -> None:
    by_label: Counter[str] = Counter()
    by_era: Counter[str] = Counter()
    by_continent: Counter[str] = Counter()
    by_class: Counter[str] = Counter()
    total = 0

    for ent in iter_entities():
        total += 1
        by_label[ent.get("label") or "Unknown"] += 1
        by_era[ent.get("era") or "Unknown"] += 1
        by_continent[ent.get("continent") or "Unknown"] += 1
        cn = ent.get("callNumber", "")
        if cn and cn[:1].isdigit():
            by_class[cn[:1]] += 1

    payload = {
        "generatedAt": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "git",
        "summary": {"entities": total},
        "total": total,
        "byLabel": dict(by_label.most_common()),
        "byEra": dict(by_era.most_common()),
        "byContinent": dict(by_continent.most_common()),
        "byClass": dict(by_class.most_common()),
    }
    out = write_report("stats", payload)
    print(f"stats: {total} entities → {out}")


if __name__ == "__main__":
    main()
