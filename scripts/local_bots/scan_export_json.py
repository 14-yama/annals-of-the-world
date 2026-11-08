#!/usr/bin/env python3
"""
Preflight scan of data/appwrite-export for git conflict markers / invalid JSON.

Usage:
  python3 scripts/local_bots/scan_export_json.py
  python3 scripts/local_bots/scan_export_json.py --fix
  python3 scripts/local_bots/scan_export_json.py --export data/appwrite-export --backup data/backups/cloud-20261107

Exit codes:
  0 — clean (or all poison files fixed with --fix)
  1 — poison files remain
  2 — usage / path error
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CONFLICT_MARKERS = ("<<<<<<<", "=======", ">>>>>>>")


def newest_cloud_backup(backups_root: Path) -> Path | None:
    if not backups_root.is_dir():
        return None
    dirs = sorted(
        [p for p in backups_root.iterdir() if p.is_dir() and p.name.startswith("cloud-")],
        key=lambda p: p.name,
    )
    return dirs[-1] if dirs else None


def classify(path: Path) -> str | None:
    try:
        raw = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        return f"unreadable: {exc}"
    for marker in CONFLICT_MARKERS:
        if marker in raw:
            return f"git conflict marker: {marker}"
    try:
        json.loads(raw)
    except json.JSONDecodeError as exc:
        return f"invalid JSON: {exc}"
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan Annals export JSON for poison files")
    parser.add_argument(
        "--export",
        default=str(REPO / "data" / "appwrite-export"),
        help="Export root (default: data/appwrite-export)",
    )
    parser.add_argument(
        "--backup",
        default="",
        help="Backup root for --fix (default: newest data/backups/cloud-*)",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Copy matching relative paths from backup over poison export files",
    )
    parser.add_argument(
        "--entities-only",
        action="store_true",
        help="Only scan entities/**/*.json",
    )
    args = parser.parse_args()

    export_root = Path(args.export).resolve()
    if not export_root.is_dir():
        print(f"ERROR: export not found: {export_root}", file=sys.stderr)
        return 2

    backup_root: Path | None = None
    if args.fix:
        if args.backup:
            backup_root = Path(args.backup).resolve()
        else:
            backup_root = newest_cloud_backup(REPO / "data" / "backups")
        if not backup_root or not backup_root.is_dir():
            print("ERROR: --fix requires a backup dir (ANNALS cloud backup)", file=sys.stderr)
            return 2
        print(f"Backup: {backup_root}")

    patterns = ["entities/**/*.json"] if args.entities_only else ["**/*.json"]
    files: list[Path] = []
    for pattern in patterns:
        files.extend(sorted(export_root.glob(pattern)))
    # de-dupe
    files = sorted(set(files))

    poison: list[tuple[Path, str]] = []
    for path in files:
        reason = classify(path)
        if reason:
            poison.append((path, reason))

    print(f"Scanned {len(files)} JSON files under {export_root}")
    if not poison:
        print("Clean — no conflict markers or invalid JSON.")
        return 0

    print(f"Poison: {len(poison)}")
    fixed = 0
    remaining = 0
    for path, reason in poison:
        rel = path.relative_to(export_root)
        print(f"  {rel}: {reason}")
        if not args.fix or backup_root is None:
            remaining += 1
            continue
        src = backup_root / rel
        if not src.is_file():
            print(f"    [no backup] {src}")
            remaining += 1
            continue
        src_reason = classify(src)
        if src_reason:
            print(f"    [backup also bad] {src_reason}")
            remaining += 1
            continue
        path.write_bytes(src.read_bytes())
        print(f"    [fixed] restored from backup")
        fixed += 1

    if args.fix:
        print(f"Fixed {fixed}; remaining {remaining}")
    return 0 if remaining == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
