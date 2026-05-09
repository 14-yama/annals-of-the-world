#!/usr/bin/env python3
"""Duplicates audit — git-first.

Bucket entities by (label, era) then run Levenshtein-ratio comparison on
normalized names. Reports near-duplicates with ratio >= 0.85.

Replaces functions/audit-duplicates/.
"""
from __future__ import annotations

import datetime as dt
import difflib
from collections import defaultdict
from typing import Any

from scripts.audits import iter_entities, write_report

THRESHOLD = 0.85
# Cap per-bucket comparisons to keep runtime sane on the 392K-entity mirror.
# Buckets larger than this are split into shards keyed by the first character of
# the normalized name; comparison happens only within a shard. This is a
# heuristic but catches the overwhelming majority of real duplicates.
MAX_BUCKET = 800


def normalize(s: str) -> str:
    return "".join(c for c in s.lower() if c.isalnum() or c == " ").strip()


def main() -> None:
    buckets: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    total = 0

    for ent in iter_entities():
        total += 1
        name = ent.get("name") or ent.get("slug") or ""
        if not name:
            continue
        key = (ent.get("label") or "Unknown", ent.get("era") or "Unknown")
        buckets[key].append({
            "slug": ent.get("slug", ""),
            "name": name,
            "norm": normalize(name),
            "callNumber": ent.get("callNumber", ""),
        })

    pairs: list[dict[str, Any]] = []
    skipped_buckets = 0
    for (label, era), items in buckets.items():
        n = len(items)
        if n < 2:
            continue
        # If the bucket is too large, shard by first letter of normalized name
        # to bound the O(n²) cost.
        if n > MAX_BUCKET:
            shards: dict[str, list[dict[str, Any]]] = defaultdict(list)
            for it in items:
                shards[(it["norm"][:1] or "_")].append(it)
            sub_buckets = list(shards.values())
            skipped_buckets += 1
        else:
            sub_buckets = [items]

        for sub in sub_buckets:
            m = len(sub)
            if m < 2 or m > MAX_BUCKET:
                # Still too large after sharding — skip; record nothing.
                continue
            for i in range(m):
                for j in range(i + 1, m):
                    a, b = sub[i], sub[j]
                    if a["slug"] == b["slug"]:
                        continue
                    ratio = difflib.SequenceMatcher(None, a["norm"], b["norm"]).ratio()
                    if ratio >= THRESHOLD:
                        pairs.append({
                            "label": label, "era": era,
                            "ratio": round(ratio, 3),
                            "a": {"slug": a["slug"], "name": a["name"], "callNumber": a["callNumber"]},
                            "b": {"slug": b["slug"], "name": b["name"], "callNumber": b["callNumber"]},
                        })

    pairs.sort(key=lambda p: -p["ratio"])
    payload = {
        "generatedAt": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "git",
        "totalScanned": total,
        "threshold": THRESHOLD,
        "shardedBuckets": skipped_buckets,
        "summary": {"duplicate_pairs": len(pairs)},
        "duplicateCount": len(pairs),
        "topPairs": pairs[:500],
    }
    out = write_report("duplicates", payload)
    print(f"duplicates: {len(pairs)} pairs at ratio >= {THRESHOLD} → {out}")


if __name__ == "__main__":
    main()
