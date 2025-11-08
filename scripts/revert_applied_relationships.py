#!/usr/bin/env python3
"""Revert relationships added by scripts/apply_approved_decisions.py.

This script scans all files under data/Relationships and removes any
relationship records whose `source_note` matches the apply script's pattern
and whose timestamp falls within an optional range.

Usage:
  python scripts/revert_applied_relationships.py [--since ISO] [--until ISO] [--source-substr STR] [--apply]

Defaults:
  - source-substr: 'Applied by scripts/apply_approved_decisions.py'
  - dry-run by default (use --apply to write changes). Backups are created for
    any file that will be modified: relationships.<cluster>.json.bak.TIMESTAMP

Example:
  # preview removals since 2025-11-08T00:00:00
  python scripts/revert_applied_relationships.py --since 2025-11-08T00:00:00

  # actually remove and write files
  python scripts/revert_applied_relationships.py --since 2025-11-08T00:00:00 --apply

"""
import os
import re
import json
import glob
import argparse
import datetime
import sys
import shutil

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
REL_DIR = os.path.join(ROOT, 'data', 'Relationships')

# pattern to find ISO timestamp in source_note, e.g. '... on 2025-11-08T12:34:56.789012 UTC'
ISO_RE = re.compile(r'on\s+(?P<iso>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?)(?:\s*Z|\s*UTC)?')


def parse_iso(s):
    try:
        return datetime.datetime.fromisoformat(s)
    except Exception:
        # fallback: try removing trailing Z
        if s.endswith('Z'):
            return datetime.datetime.fromisoformat(s[:-1])
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--since', help='ISO timestamp (inclusive) to revert from, e.g. 2025-11-08T00:00:00')
    ap.add_argument('--until', help='ISO timestamp (inclusive) to revert until')
    ap.add_argument('--source-substr', default='Applied by scripts/apply_approved_decisions.py', help='Substring to match in source_note')
    ap.add_argument('--apply', action='store_true', help='Write changes to files (default dry-run)')
    ap.add_argument('--restore', help='Path to a backup file to restore (overwrites its target). Use absolute or relative path to a .bak file.')
    ap.add_argument('--yes', action='store_true', help='Skip interactive confirmation when restoring')
    args = ap.parse_args()

    since = parse_iso(args.since) if args.since else None
    until = parse_iso(args.until) if args.until else None

    files = sorted(glob.glob(os.path.join(REL_DIR, 'relationships.*.json')))
    total_removed = 0
    modified_files = []

    # If restore mode requested, copy chosen backup to original
    if args.restore:
        bak = args.restore
        if not os.path.exists(bak):
            print(f'Backup file not found: {bak}')
            return
        # infer original filename by stripping the .bak.* suffix
        if '.bak.' in bak:
            orig = bak.split('.bak.')[0]
        else:
            print('Backup filename does not follow expected .bak.TIMESTAMP pattern; please provide the target original file via --restore with correct file.')
            return
        print(f'Will restore backup {bak} -> {orig}')
        if not args.yes:
            if not sys.stdin.isatty():
                print('Non-interactive session detected; to restore pass --yes to confirm')
                return 2
            resp = input("Type 'yes' to proceed with restore: ").strip().lower()
            if resp != 'yes':
                print('Restore aborted by user.')
                return
        shutil.copy2(bak, orig)
        print(f'Restored {bak} -> {orig}')
        return

    for f in files:
        try:
            with open(f, 'r', encoding='utf-8') as fh:
                data = json.load(fh)
        except Exception:
            continue
        rels = data.get('relationships', [])
        keep = []
        removed = []
        for r in rels:
            src = r.get('source_note') or ''
            if args.source_substr in src:
                m = ISO_RE.search(src)
                ts = None
                if m:
                    ts = parse_iso(m.group('iso'))
                # decide removal if timestamp in range (or no timestamp and no bounds)
                remove = False
                if ts:
                    if since and ts < since:
                        remove = False
                    elif until and ts > until:
                        remove = False
                    else:
                        remove = True
                else:
                    # no timestamp: remove only if no bounds specified (explicit request)
                    if not since and not until:
                        remove = True
                if remove:
                    removed.append(r)
                    continue
            keep.append(r)

        if removed:
            total_removed += len(removed)
            modified_files.append((f, len(removed)))
            print(f'Found {len(removed)} to remove in {f}')
            for rr in removed[:5]:
                print('  -', rr.get('id'), rr.get('start_slug'), rr.get('type'), rr.get('end_slug'))
            if args.apply:
                bak = f + f'.bak.{datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")}'
                shutil.copy2(f, bak)
                data['relationships'] = keep
                with open(f, 'w', encoding='utf-8') as fh:
                    json.dump(data, fh, indent=2, ensure_ascii=False)
                print(f'Wrote updated file and backed up original to {bak}')
            else:
                print('Dry-run: not writing changes. Use --apply to remove these relationships.')

    print(f'Completed scan. Files modified: {len(modified_files)}; total relationships flagged for removal: {total_removed}')


if __name__ == '__main__':
    main()
