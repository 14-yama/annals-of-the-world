#!/usr/bin/env python3
"""
fetch_wikidata_retry.py

Retries failed Wikidata batches (politicians 220-222, legal 230) using
single-occupation queries with a lighter SPARQL pattern to avoid timeouts.

Merges new results into the existing data/wikidata_people.json.

Usage:
    python3 scripts/fetch_wikidata_retry.py
    python3 scripts/fetch_wikidata_retry.py --limit 300
"""

import argparse
import json
import re
import time
from pathlib import Path
from typing import Any

import requests

# Reuse mappings from main script
from fetch_wikidata_people import (
    SPARQL_ENDPOINT,
    USER_AGENT,
    QID_TO_DIVISION,
    get_country_info,
    get_division,
    year_to_era,
    parse_year,
    format_date_display,
    make_slug,
    binding_val,
    qid_from_uri,
    transform_person,
)

# ── Batches that failed — split into individual occupation queries ──
RETRY_QUERIES: dict[str, list[str]] = {
    # Politicians — split from the combined 220-222 batch
    "220a-politicians":  ["Q82955"],      # politician
    "220b-statesmen":    ["Q372436"],     # statesman
    "221a-monarchs":     ["Q116"],        # monarch
    "221b-emperors":     ["Q12097"],      # emperor
    "222a-heads-govt":   ["Q14915627"],   # head of government
    "222b-heads-state":  ["Q1553195"],    # head of state
    "222c-presidents":   ["Q30461"],      # president
    # Legal — split
    "230a-jurists":      ["Q185351"],     # jurist
    "230b-lawyers":      ["Q40348"],      # lawyer
    "230c-judges":       ["Q16533"],      # judge
    # Also pick up educators and athletes that were not in original batches
    "201-educators":     ["Q1622272"],    # university teacher
    "203-athletes":      ["Q2066131"],    # athlete
}


def build_light_sparql(occupation_qid: str, limit: int = 300,
                       sitelink_min: int = 30) -> str:
    """Build a lighter SPARQL query — fewer OPTIONALs, higher sitelinks."""
    return f"""
SELECT DISTINCT ?person ?personLabel ?personDescription
       ?birthDate ?deathDate
       ?birthPlaceLabel
       ?countryOfCitizenship
       ?occupation ?occupationLabel
       ?article
WHERE {{
  VALUES ?occupation {{ wd:{occupation_qid} }}
  ?person wdt:P106 ?occupation .
  ?person wdt:P31 wd:Q5 .
  ?person wikibase:sitelinks ?sitelinks .
  FILTER(?sitelinks > {sitelink_min})

  OPTIONAL {{ ?person wdt:P569 ?birthDate . }}
  OPTIONAL {{ ?person wdt:P570 ?deathDate . }}
  OPTIONAL {{ ?person wdt:P19 ?birthPlace . }}
  OPTIONAL {{ ?person wdt:P27 ?countryOfCitizenship . }}
  OPTIONAL {{
    ?article schema:about ?person ;
             schema:isPartOf <https://en.wikipedia.org/> .
  }}

  SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en" . }}
}}
ORDER BY DESC(?sitelinks)
LIMIT {limit}
"""


def fetch_sparql_light(query: str, retries: int = 4) -> list[dict[str, Any]]:
    """Execute SPARQL with longer timeout and more retries."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/sparql-results+json",
    }
    for attempt in range(retries):
        try:
            resp = requests.get(
                SPARQL_ENDPOINT,
                params={"query": query, "format": "json"},
                headers=headers,
                timeout=180,
            )
            if resp.status_code == 429:
                wait = min(90, 15 * (attempt + 1))
                print(f"  Rate limited, waiting {wait}s...")
                time.sleep(wait)
                continue
            if resp.status_code in (502, 504):
                wait = 20 * (attempt + 1)
                print(f"  Server error {resp.status_code} (attempt {attempt + 1}), retrying in {wait}s...")
                time.sleep(wait)
                continue
            resp.raise_for_status()
            return resp.json()["results"]["bindings"]
        except requests.exceptions.RequestException as e:
            print(f"  Request error (attempt {attempt + 1}): {e}")
            if attempt < retries - 1:
                time.sleep(10 * (attempt + 1))
    return []


def main():
    parser = argparse.ArgumentParser(description="Retry failed Wikidata batches")
    parser.add_argument("--limit", type=int, default=300,
                        help="Max results per occupation query (default: 300)")
    parser.add_argument("--sitelinks", type=int, default=25,
                        help="Minimum sitelinks for notability (default: 25)")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    output_path = project_root / "data" / "wikidata_people.json"

    # Load existing data
    if output_path.exists():
        with open(output_path, encoding="utf-8") as f:
            existing = json.load(f)
        existing_entities = existing.get("entities", [])
        print(f"Loaded {len(existing_entities)} existing entities")
    else:
        existing_entities = []
        print("No existing file found, starting fresh")

    # Build set of existing slugs
    seen_slugs: set[str] = {e["slug"] for e in existing_entities}

    print()
    print("=" * 60)
    print("Wikidata Retry — Failed Batches")
    print("=" * 60)
    print(f"  Limit per query: {args.limit}")
    print(f"  Sitelinks threshold: {args.sitelinks}")
    print(f"  Retry batches: {len(RETRY_QUERIES)}")
    print()

    new_entities: list[dict[str, Any]] = []
    total_raw = 0

    for batch_name, occ_qids in RETRY_QUERIES.items():
        qid = occ_qids[0]
        print(f"[{batch_name}] Querying wd:{qid}...")
        query = build_light_sparql(qid, limit=args.limit, sitelink_min=args.sitelinks)
        rows = fetch_sparql_light(query)
        total_raw += len(rows)
        print(f"  Got {len(rows)} raw results")

        batch_count = 0
        for row in rows:
            entity = transform_person(row)
            if not entity:
                continue
            if entity["slug"] in seen_slugs:
                continue
            seen_slugs.add(entity["slug"])
            new_entities.append(entity)
            batch_count += 1

        print(f"  → {batch_count} new unique entities")
        # Polite delay between queries
        time.sleep(3)

    # Merge
    all_entities = existing_entities + new_entities
    era_order = {"Prehistoric": 0, "Classical": 1, "Medieval": 2,
                 "Early Modern": 3, "Modern": 4, "Contemporary": 5}
    all_entities.sort(key=lambda e: (era_order.get(e["era"], 9), e["name"]))

    # Recompute stats
    div_counts: dict[str, int] = {}
    era_counts: dict[str, int] = {}
    for e in all_entities:
        div = e["callNumber"][:3]
        div_counts[div] = div_counts.get(div, 0) + 1
        era_counts[e["era"]] = era_counts.get(e["era"], 0) + 1

    # Write merged JSON
    output_data = {
        "_meta": {
            "source": "Wikidata SPARQL (query.wikidata.org)",
            "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "total_raw_results": (existing.get("_meta", {}).get("total_raw_results", 0)
                                  if output_path.exists() else 0) + total_raw,
            "total_unique_entities": len(all_entities),
            "division_counts": dict(sorted(div_counts.items())),
            "era_counts": dict(sorted(era_counts.items())),
            "note": "Annals of the World Entity schema (Person label, Class 2 divisions). "
                    "Includes retry for politician/legal batches.",
        },
        "entities": all_entities,
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print()
    print("=" * 60)
    print("Retry Complete")
    print("=" * 60)
    print(f"  New raw results: {total_raw}")
    print(f"  New unique entities: {len(new_entities)}")
    print(f"  Total entities (merged): {len(all_entities)}")
    print(f"  Output: {output_path}")
    print()
    print("  New entities by division:")
    new_div: dict[str, int] = {}
    for e in new_entities:
        div = e["callNumber"][:3]
        new_div[div] = new_div.get(div, 0) + 1
    for div, count in sorted(new_div.items()):
        print(f"    {div}: {count}")


if __name__ == "__main__":
    main()
