#!/usr/bin/env python3
"""
extract_wikidata_catalog.py

Extracts the top N most notable people per division from the comprehensive
data/wikidata_people.json into a smaller catalog-ready file for the frontend.

Prioritizes by:
  1. People NOT already in Appwrite (new nodes)
  2. Presence of Wikipedia URL (implies higher notability)
  3. Presence of born/died dates
  4. Presence of place data

Output: ui/src/data/wikidata_people.json  (small, catalog-ready)
Source: data/wikidata_people.json         (full 238K+ dataset)

Usage:
    python3 scripts/extract_wikidata_catalog.py
    python3 scripts/extract_wikidata_catalog.py --per-division 200
    python3 scripts/extract_wikidata_catalog.py --max-total 20000
"""

import argparse
import json
from pathlib import Path


def notability_score(entity: dict) -> int:
    """Higher = more notable / more complete data."""
    score = 0
    if entity.get("wikipediaUrl"):
        score += 10
    if entity.get("born"):
        score += 3
    if entity.get("died"):
        score += 2
    if entity.get("places"):
        score += len(entity["places"]) * 2
    if entity.get("continent") != "Global":
        score += 3
    if entity.get("summary", "").count(".") > 1:
        score += 2
    # Prefer people NOT in Appwrite (they're new additions)
    if not entity.get("inAppwrite"):
        score += 5
    return score


def main():
    parser = argparse.ArgumentParser(description="Extract top Wikidata people for catalog")
    parser.add_argument("--per-division", type=int, default=150,
                        help="Max entities per division (default: 150)")
    parser.add_argument("--max-total", type=int, default=15000,
                        help="Max total entities (default: 15000)")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    source = project_root / "data" / "wikidata_people.json"
    target = project_root / "ui" / "src" / "data" / "wikidata_people.json"

    print(f"Loading source: {source}")
    with open(source, encoding="utf-8") as f:
        data = json.load(f)

    all_entities = data["entities"]
    meta = data["_meta"]
    print(f"Full dataset: {len(all_entities):,} entities")

    # Group by division
    by_division: dict[str, list[dict]] = {}
    for e in all_entities:
        div = e["callNumber"][:3]
        by_division.setdefault(div, [])
        by_division[div].append(e)

    # Select top N per division by notability
    selected: list[dict] = []
    div_stats: dict[str, int] = {}

    for div in sorted(by_division.keys()):
        pool = by_division[div]
        pool.sort(key=notability_score, reverse=True)
        take = min(len(pool), args.per_division)
        batch = pool[:take]
        selected.extend(batch)
        div_stats[div] = take

    # Cap at max total if needed
    if len(selected) > args.max_total:
        selected.sort(key=notability_score, reverse=True)
        selected = selected[:args.max_total]
        # Recompute div_stats
        div_stats = {}
        for e in selected:
            div = e["callNumber"][:3]
            div_stats[div] = div_stats.get(div, 0) + 1

    # Sort by era then name
    era_order = {"Prehistoric": 0, "Classical": 1, "Medieval": 2,
                 "Early Modern": 3, "Modern": 4, "Contemporary": 5}
    selected.sort(key=lambda e: (era_order.get(e["era"], 9), e["name"]))

    # Recompute stats
    era_counts: dict[str, int] = {}
    continent_counts: dict[str, int] = {}
    in_appwrite = sum(1 for e in selected if e.get("inAppwrite"))
    not_in_appwrite = sum(1 for e in selected if not e.get("inAppwrite"))

    for e in selected:
        era_counts[e["era"]] = era_counts.get(e["era"], 0) + 1
        continent_counts[e["continent"]] = continent_counts.get(e["continent"], 0) + 1

    # Build output
    output_meta = {
        "source": "Wikidata SPARQL (query.wikidata.org) — filtered for catalog",
        "generated": meta.get("generated", ""),
        "version": "2.0-catalog",
        "full_dataset_size": len(all_entities),
        "catalog_size": len(selected),
        "per_division_limit": args.per_division,
        "min_sitelinks": meta.get("min_sitelinks", 5),
        "division_counts": dict(sorted(div_stats.items())),
        "era_counts": dict(sorted(era_counts.items())),
        "continent_counts": dict(sorted(continent_counts.items())),
        "appwrite_comparison": {
            "appwrite_total_entities": meta.get("appwrite_comparison", {}).get("appwrite_total_entities", 0),
            "appwrite_person_entities": meta.get("appwrite_comparison", {}).get("appwrite_person_entities", 0),
            "catalog_in_appwrite": in_appwrite,
            "catalog_not_in_appwrite": not_in_appwrite,
        },
        "note": (
            f"Catalog extract: top {args.per_division} most notable people per division "
            f"from {len(all_entities):,} total Wikidata people. Full dataset: data/wikidata_people.json"
        ),
    }

    output_data = {"_meta": output_meta, "entities": selected}

    target.parent.mkdir(parents=True, exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    size_mb = target.stat().st_size / (1024 * 1024)
    print(f"\nCatalog extract: {len(selected):,} entities")
    print(f"Output: {target} ({size_mb:.1f} MB)")
    print(f"\n  ── By Division ──")
    for div, count in sorted(div_stats.items()):
        print(f"    {div}: {count}")
    print(f"\n  In Appwrite: {in_appwrite}")
    print(f"  NOT in Appwrite: {not_in_appwrite}")


if __name__ == "__main__":
    main()
