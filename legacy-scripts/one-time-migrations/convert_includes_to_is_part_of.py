#!/usr/bin/env python3
"""Convert cluster-level INCLUDES relationships to IS_PART_OF (child -> parent).

Usage:
  python3 convert_includes_to_is_part_of.py [--dry-run]

This script:
 - reads cluster slugs from `docs/clusters/`
 - scans `data/Relationships/*.json` (ignores backup files)
 - for each relationship where `type` == "INCLUDES" and both `start_slug` and `end_slug`
   are cluster slugs, converts it to an `IS_PART_OF` relationship by swapping
   start/end and updating `type` and `_key`.
 - writes a `.bak.YYYYMMDDTHHMMSSZ` backup before modifying the file.
"""

import argparse
import json
import os
import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CLUSTERS_DIR = ROOT / "docs" / "clusters"
REL_DIR = ROOT / "data" / "Relationships"


def load_clusters():
    names = []
    if CLUSTERS_DIR.exists():
        for p in CLUSTERS_DIR.iterdir():
            if p.is_dir():
                names.append(p.name)
    return set(names)


def backup_file(path: Path):
    ts = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    bak = path.with_name(path.name + ".bak." + ts)
    bak.write_bytes(path.read_bytes())
    return bak


def process_file(path: Path, clusters: set, dry_run=True):
    changed = False
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    rels = data.get("relationships", [])
    converted = []
    for i, r in enumerate(rels):
        if r.get("type") == "INCLUDES":
            s = r.get("start_slug")
            e = r.get("end_slug")
            # Only convert when both ends are cluster slugs
            if s in clusters and e in clusters:
                converted.append((i, r))

    if not converted:
        return False, []

    if dry_run:
        return True, [(path, [(r[1].get("start_slug"), r[1].get("end_slug")) for r in converted])]

    # backup
    bak = backup_file(path)

    # perform conversions in-place
    for idx, rel in converted:
        old_s = rel.get("start_slug")
        old_e = rel.get("end_slug")
        rel["start_slug"] = old_e
        rel["end_slug"] = old_s
        rel["type"] = "IS_PART_OF"
        # update _key if present
        if rel.get("_key"):
            rel["_key"] = f"{rel['start_slug']}|IS_PART_OF|{rel['end_slug']}"
    # write file
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=False)

    return True, [(path, [(r[1].get("start_slug"), r[1].get("end_slug")) for r in converted])]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true", help="Show planned changes without writing")
    args = p.parse_args()

    clusters = load_clusters()
    if not clusters:
        print("No clusters found in docs/clusters; aborting.")
        return 2

    json_files = sorted([p for p in REL_DIR.iterdir() if p.suffix == ".json" and "bak" not in p.name and p.name != "cluster_tree_mermaid.md"])

    total_converted = 0
    plan = []
    for jf in json_files:
        ok, info = process_file(jf, clusters, dry_run=args.dry_run)
        if ok:
            # info is list of tuples
            plan.extend(info)
            total_converted += len(info)

    if args.dry_run:
        if not plan:
            print("Dry-run: no INCLUDES->IS_PART_OF conversions planned.")
        else:
            print("Dry-run: planned conversions:")
            for pth, items in plan:
                print(f"  File: {pth}")
                for s,e in items:
                    print(f"    {s} -> {e}  (will become {e} IS_PART_OF {s})")
        return 0

    print(f"Applied conversions to {len(plan)} files (backup created for each).")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
