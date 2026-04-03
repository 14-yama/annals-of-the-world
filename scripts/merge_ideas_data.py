#!/usr/bin/env python3
"""
merge_ideas_data.py — One-time script to merge wikidata_ideas_other.json
into wikidata_ideas.json and produce a single consolidated file.

Strategy:
  - Keep ALL Class 0 entities from ideas.json (3,136)
  - For Class 1: union entities from both files, deduplicate by slug
    (ideas_other wins for duplicates — newer, richer data)
  - Preserve division 151 entities from original (ideas_other has 0)
  - Recompute _meta statistics
  - Write back to data/wikidata_ideas.json
"""

import json
import time
from collections import Counter
from pathlib import Path


def main():
    root = Path(__file__).resolve().parent.parent
    ideas_path = root / "data" / "wikidata_ideas.json"
    other_path = root / "data" / "wikidata_ideas_other.json"

    print("Loading wikidata_ideas.json ...")
    with open(ideas_path, encoding="utf-8") as f:
        ideas_data = json.load(f)

    print("Loading wikidata_ideas_other.json ...")
    with open(other_path, encoding="utf-8") as f:
        other_data = json.load(f)

    ideas_entities = ideas_data["entities"]
    other_entities = other_data["entities"]

    print(f"  ideas.json:       {len(ideas_entities)} entities")
    print(f"  ideas_other.json: {len(other_entities)} entities")

    # Separate Class 0 and Class 1 from original
    class0 = [e for e in ideas_entities if e.get("ideaClass") == 0]
    class1_orig = [e for e in ideas_entities if e.get("ideaClass") == 1]

    print(f"  Class 0 (original): {len(class0)}")
    print(f"  Class 1 (original): {len(class1_orig)}")
    print(f"  Class 1 (other):    {len(other_entities)}")

    # Build slug map for Class 1: ideas_other wins, then backfill from original
    class1_map: dict[str, dict] = {}

    # Load original Class 1 first
    for e in class1_orig:
        slug = e["slug"]
        class1_map[slug] = e

    # Overlay ideas_other (newer, richer) — overwrites duplicates
    overwritten = 0
    new_from_other = 0
    for e in other_entities:
        slug = e["slug"]
        if slug in class1_map:
            overwritten += 1
        else:
            new_from_other += 1
        class1_map[slug] = e

    print(f"\n  Class 1 merge stats:")
    print(f"    Slugs from original kept (unique): {len(class1_orig) - overwritten}")
    print(f"    Slugs overwritten by other:        {overwritten}")
    print(f"    New slugs from other:              {new_from_other}")
    print(f"    Total Class 1 merged:              {len(class1_map)}")

    # Combine
    merged = class0 + sorted(class1_map.values(),
                              key=lambda e: (int(e.get("divisionCode", "110")), e.get("name", "")))

    print(f"\n  Total merged entities: {len(merged)}")

    # Compute statistics
    div_counts = Counter(e["callNumber"][:3] for e in merged)
    era_counts = Counter(e.get("era", "Unknown") for e in merged)
    sig_dist = Counter(e.get("historicalSignificance", {}).get("label", "Unknown") for e in merged)
    continent_counts = Counter(e.get("continent", "Global") for e in merged)
    class_counts = Counter(str(e.get("ideaClass", 0)) for e in merged)

    # Division breakdown for display
    print(f"\n  Division breakdown:")
    for div in sorted(div_counts.keys()):
        print(f"    {div}: {div_counts[div]}")

    # Build output
    output = {
        "_meta": {
            "source": "Wikidata SPARQL (query.wikidata.org)",
            "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "version": "2.0",
            "total_unique_entities": len(merged),
            "label": "Idea",
            "classCodes": [0, 1],
            "classHeadings": [
                "Ideas – Core Categories",
                "Ideas – Other Theories",
            ],
            "class_counts": dict(sorted(class_counts.items())),
            "division_counts": dict(sorted(div_counts.items())),
            "era_counts": dict(sorted(era_counts.items())),
            "significance_distribution": dict(sorted(sig_dist.items())),
            "continent_counts": dict(sorted(continent_counts.items())),
            "note": (
                "Consolidated ideas data v2.0. Merged from original "
                "wikidata_ideas.json (9,878 entities: 3,136 Class 0 + "
                "6,742 Class 1) and wikidata_ideas_other.json (18,476 "
                "Class 1 entities). Deduplicated by slug with "
                "ideas_other winning for overlapping Class 1 slugs."
            ),
        },
        "entities": merged,
    }

    # Write
    print(f"\nWriting merged data to {ideas_path} ...")
    with open(ideas_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    size_mb = ideas_path.stat().st_size / (1024 * 1024)
    print(f"  Written: {size_mb:.1f} MB")
    print(f"  Total entities: {len(merged)}")
    print(f"  Class 0: {class_counts.get('0', 0)}")
    print(f"  Class 1: {class_counts.get('1', 0)}")
    print("\nDone! You can now safely delete wikidata_ideas_other.json")


if __name__ == "__main__":
    main()
