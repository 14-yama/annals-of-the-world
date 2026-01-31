#!/usr/bin/env python3
"""Relabel nodes with `label: "Concept"` to `label: "Idea"` across per-cluster node files.

Backs up each modified file to `*.bak.<TS>` before writing.

Usage:
  python3 scripts/admin/fix_labels_concept_to_idea.py [--dry-run]
"""
import json
import shutil
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NODES_DIR = ROOT / "data" / "Nodes"


def backup(path: Path) -> Path:
    ts = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    bkp = path.with_suffix(path.suffix + f".bak.{ts}")
    shutil.copy2(path, bkp)
    return bkp


def fix_file(path: Path, dry_run: bool = False):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"Skipping {path.name}: failed to parse JSON: {exc}")
        return 0

    nodes = data.get("nodes") or []
    changed = 0
    for n in nodes:
        if n.get("label") == "Concept":
            n["label"] = "Idea"
            changed += 1

    if changed:
        print(f"{path.name}: {changed} nodes relabeled Concept -> Idea")
        if not dry_run:
            bkp = backup(path)
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"  Backup saved: {bkp.name}")
    return changed


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Show changes without writing")
    args = parser.parse_args()

    if not NODES_DIR.exists():
        print("Nodes directory not found; aborting.")
        return 1

    total_changed = 0
    files_processed = 0

    for p in sorted(NODES_DIR.iterdir()):
        if p.suffix != '.json' or 'bak' in p.name:
            continue
        files_processed += 1
        total_changed += fix_file(p, dry_run=args.dry_run)

    print(f"Processed {files_processed} files. Total nodes relabeled: {total_changed}")
    if args.dry_run:
        print("Dry-run: no files were modified.")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
