#!/usr/bin/env python3
"""
fix_wikidata_divisions.py

Fixes the division assignments for entities that were incorrectly assigned to
division 220 due to the SPARQL bug. Re-queries Wikidata for occupations in
batches and reassigns divisions.

Usage:
    python3 scripts/fix_wikidata_divisions.py
"""

import json
import re
import time
from pathlib import Path
from typing import Any

import requests

from fetch_wikidata_people import (
    SPARQL_ENDPOINT,
    USER_AGENT,
    QID_TO_DIVISION,
    make_slug,
)

# Additional QID → division mapping for occupations not in the original map
EXTRA_DIVISIONS: dict[str, tuple[str, str]] = {
    "Q2066131":  ("203", "Athletes & Sports Figures"),       # athlete
    "Q16533":    ("230", "Legal Figures"),                    # judge
}


def batch_fetch_occupations(person_qids: list[str], batch_size: int = 150
                            ) -> dict[str, list[str]]:
    """Query Wikidata for occupations of known person QIDs in batches."""
    result: dict[str, list[str]] = {}

    for i in range(0, len(person_qids), batch_size):
        batch = person_qids[i:i + batch_size]
        values = " ".join(f"wd:{qid}" for qid in batch)
        query = f"""
SELECT ?person ?occupation WHERE {{
  VALUES ?person {{ {values} }}
  ?person wdt:P106 ?occupation .
}}
"""
        headers = {
            "User-Agent": USER_AGENT,
            "Accept": "application/sparql-results+json",
        }
        for attempt in range(3):
            try:
                resp = requests.get(
                    SPARQL_ENDPOINT,
                    params={"query": query, "format": "json"},
                    headers=headers,
                    timeout=120,
                )
                if resp.status_code in (429, 502, 504):
                    wait = 15 * (attempt + 1)
                    print(f"  Server error {resp.status_code}, retrying in {wait}s...")
                    time.sleep(wait)
                    continue
                resp.raise_for_status()
                bindings = resp.json()["results"]["bindings"]
                for row in bindings:
                    p_uri = row["person"]["value"]
                    o_uri = row["occupation"]["value"]
                    p_qid = re.search(r'(Q\d+)$', p_uri)
                    o_qid = re.search(r'(Q\d+)$', o_uri)
                    if p_qid and o_qid:
                        pid = p_qid.group(1)
                        if pid not in result:
                            result[pid] = []
                        result[pid].append(o_qid.group(1))
                break
            except requests.exceptions.RequestException as e:
                print(f"  Batch fetch error (attempt {attempt + 1}): {e}")
                time.sleep(10 * (attempt + 1))

        print(f"  Fetched occupations for batch {i // batch_size + 1} "
              f"({len(batch)} persons)")
        time.sleep(2)

    return result


def best_division(occupation_qids: list[str]) -> tuple[str, str] | None:
    """Pick the best-matching division from a list of occupation QIDs."""
    # Merge extra mappings
    combined = {**QID_TO_DIVISION, **EXTRA_DIVISIONS}
    for qid in occupation_qids:
        if qid in combined:
            return combined[qid]
    return None


def main():
    project_root = Path(__file__).resolve().parent.parent
    json_path = project_root / "data" / "wikidata_people.json"

    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)

    entities = data["entities"]
    print(f"Loaded {len(entities)} entities")

    # Find entities that need division re-assignment
    # These are entities with division 220 that have a wikidataQid
    # (the original 1,005 entities had correct divisions; the 1,376 retry entities have div 220)
    needs_fix = [e for e in entities
                 if e.get("callNumber", "").startswith("220.")
                 and e.get("wikidataQid")]

    print(f"Entities in division 220: {len(needs_fix)}")

    if not needs_fix:
        print("Nothing to fix.")
        return

    # Get their QIDs
    qids = [e["wikidataQid"] for e in needs_fix]
    print(f"Fetching occupations for {len(qids)} persons...")

    occupations = batch_fetch_occupations(qids)
    print(f"Got occupations for {len(occupations)} persons")

    # Re-assign divisions
    fixes = 0
    fix_counts: dict[str, int] = {}
    for entity in entities:
        qid = entity.get("wikidataQid")
        if not qid or not entity["callNumber"].startswith("220."):
            continue
        occs = occupations.get(qid, [])
        new_div = best_division(occs)
        if new_div and new_div[0] != "220":
            old_div = entity["callNumber"][:3]
            entity["callNumber"] = f"{new_div[0]}.{entity['slug']}"
            entity["subjectHeadings"] = [
                h.replace("Political Leaders", new_div[1])
                for h in entity.get("subjectHeadings", [])
            ]
            fixes += 1
            fix_counts[new_div[0]] = fix_counts.get(new_div[0], 0) + 1

    print(f"\nRe-assigned {fixes} entities to correct divisions:")
    for div, count in sorted(fix_counts.items()):
        print(f"  {div}: {count}")

    # Recompute meta stats
    div_counts: dict[str, int] = {}
    era_counts: dict[str, int] = {}
    for e in entities:
        div = e["callNumber"][:3]
        div_counts[div] = div_counts.get(div, 0) + 1
        era_counts[e["era"]] = era_counts.get(e["era"], 0) + 1

    data["_meta"]["total_unique_entities"] = len(entities)
    data["_meta"]["division_counts"] = dict(sorted(div_counts.items()))
    data["_meta"]["era_counts"] = dict(sorted(era_counts.items()))
    data["_meta"]["note"] += " Division-corrected."

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\nFinal division distribution:")
    for div, count in sorted(div_counts.items()):
        print(f"  {div}: {count}")
    print(f"\nTotal: {len(entities)} entities")
    print(f"Saved to {json_path}")


if __name__ == "__main__":
    main()
