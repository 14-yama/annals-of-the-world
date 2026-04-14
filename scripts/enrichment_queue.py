#!/usr/bin/env python3
"""
Enrichment Queue — Scans all entities and ranks by weakness for AI enrichment.

Outputs a priority-sorted JSON queue of entities needing enrichment.
Entities already enriched (summary >= 800c) are excluded.

Usage:
    python3 scripts/enrichment_queue.py                        # Generate queue
    python3 scripts/enrichment_queue.py --stats                # Stats only
    python3 scripts/enrichment_queue.py --min-importance 5     # Filter low-importance
    python3 scripts/enrichment_queue.py --limit 100            # Top 100 only
"""
import json
import os
import sys
import argparse
import time

BASE = "data/appwrite-export/entities"

STUB_PATTERNS = [
    "a notable figure associated with",
    "notable figure in",
    "associated with the",
    "a figure in",
    "a key figure",
    "an important figure",
    "a significant",
    "a prominent",
]


def score_entity(entity):
    """Score entity weakness. Higher = needs more work. 0 = already good."""
    summary = entity.get("summary", "") or ""
    summary_len = len(summary)

    # Already well-enriched — skip
    if summary_len >= 800:
        return 0.0

    # Parse detailsJson
    details = {}
    dj = entity.get("detailsJson", "")
    if isinstance(dj, str) and dj:
        try:
            details = json.loads(dj)
        except (json.JSONDecodeError, ValueError):
            pass
    elif isinstance(dj, dict):
        details = dj

    # Base weakness from summary length (0-50 points)
    if summary_len == 0:
        weakness = 50.0
    else:
        weakness = max(0, 800 - summary_len) / 800 * 50

    # Missing structured data (0-30 points, 5 per missing field)
    missing = 0
    if not details.get("causes"):
        missing += 1
    if not details.get("effects"):
        missing += 1
    rels = details.get("relationships", [])
    if not rels or len(rels) < 3:
        missing += 1
    if not details.get("places"):
        missing += 1
    if not entity.get("subjects") or len(entity.get("subjects", [])) < 3:
        missing += 1
    if not entity.get("frameworks") or len(entity.get("frameworks", [])) < 2:
        missing += 1
    weakness += missing * 5

    # Stub pattern detection (extra 20 points)
    summary_lower = summary.lower()
    for pattern in STUB_PATTERNS:
        if pattern in summary_lower:
            weakness += 20
            break

    # Scale by importance (higher importance = higher priority to fix)
    importance = entity.get("importanceScore", 1) or 1
    weakness *= importance / 5.0

    return round(weakness, 2)


def scan_entities(base_dir, min_importance=0):
    """Scan all entity JSON files and return scored queue."""
    queue = []
    total = 0
    skipped = 0
    errors = 0

    for root, _dirs, files in os.walk(base_dir):
        for fname in files:
            if not fname.endswith(".json"):
                continue
            filepath = os.path.join(root, fname)
            try:
                with open(filepath, "r") as f:
                    data = json.load(f)
                entities = data.get("entities", [])
                for entity in entities:
                    total += 1
                    slug = entity.get("slug", "")
                    if not slug:
                        continue

                    importance = entity.get("importanceScore", 1) or 1
                    if importance < min_importance:
                        skipped += 1
                        continue

                    score = score_entity(entity)
                    if score > 0:
                        queue.append({
                            "slug": slug,
                            "name": entity.get("name", ""),
                            "label": entity.get("label", ""),
                            "era": entity.get("era", ""),
                            "region": entity.get("region", ""),
                            "continent": entity.get("continent", ""),
                            "importanceScore": importance,
                            "summaryLength": len(entity.get("summary", "") or ""),
                            "score": score,
                            "filepath": filepath,
                        })
            except (json.JSONDecodeError, KeyError, OSError):
                errors += 1
                continue

    # Sort by score descending (highest priority first)
    queue.sort(key=lambda x: x["score"], reverse=True)

    return queue, total, skipped, errors


def main():
    parser = argparse.ArgumentParser(description="Generate enrichment priority queue")
    parser.add_argument(
        "--output", default="data/enrichment/queue.json",
        help="Output queue file path",
    )
    parser.add_argument(
        "--limit", type=int, default=5000,
        help="Max entities in output queue (default: 5000)",
    )
    parser.add_argument(
        "--min-importance", type=int, default=0,
        help="Minimum importanceScore filter (0 = all)",
    )
    parser.add_argument(
        "--stats", action="store_true",
        help="Print stats only, skip writing queue file",
    )
    args = parser.parse_args()

    print(f"Scanning entities in {BASE}...")
    start = time.time()
    queue, total, skipped, errors = scan_entities(BASE, args.min_importance)
    elapsed = time.time() - start

    print(f"Scanned {total:,} entities in {elapsed:.1f}s")
    if skipped:
        print(f"Skipped {skipped:,} (below min importance {args.min_importance})")
    if errors:
        print(f"Parse errors: {errors:,}")
    print(f"Entities needing enrichment: {len(queue):,}")

    # Stats breakdown
    stubs = sum(1 for e in queue if e["summaryLength"] < 200)
    partials = sum(1 for e in queue if 200 <= e["summaryLength"] < 600)
    weak = sum(1 for e in queue if 600 <= e["summaryLength"] < 800)

    print(f"\n  STUBs (<200c):       {stubs:,}")
    print(f"  PARTIALs (200-600c): {partials:,}")
    print(f"  WEAK (600-800c):     {weak:,}")

    if queue:
        print(f"\n  Top 10 highest priority:")
        for i, e in enumerate(queue[:10]):
            print(
                f"    {i+1}. {e['slug']}"
                f" — {e['summaryLength']}c, score={e['score']},"
                f" imp={e['importanceScore']}, {e['label']}"
            )

    if args.stats:
        return

    # Write queue
    output = queue[:args.limit]
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(
            {
                "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "total_scanned": total,
                "count": len(output),
                "queue": output,
            },
            f,
            indent=2,
        )
        f.write("\n")
    print(f"\nQueue written to {args.output} ({len(output):,} entities)")


if __name__ == "__main__":
    main()
