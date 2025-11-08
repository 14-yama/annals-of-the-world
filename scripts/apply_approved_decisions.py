#!/usr/bin/env python3
"""Apply approved triage decisions by appending relationships.

Usage:
  python scripts/apply_approved_decisions.py [--dry-run] [--decisions path] [--run-validators]

Behavior:
- Reads a decisions CSV (default: data/orphan_triage_decisions.csv)
- For rows where decision == 'approve' it will attempt to determine a relationship to add.
  Preferred sources (in order): explicit columns 'start_slug','end_slug','type', a
  'relationship' column (JSON or string), or the 'suggested_action' parsed by
  the autogen script (format: "Added relationship: start -[TYPE]-> end").
- In dry-run mode (default) the script prints proposed additions and exits without
  touching files. Use --apply to write changes. When writing, it will back up the
  relationships file before modifying it.
- If --run-validators is passed and changes were applied, the script will run
  `scripts/validate_slugs.py` and `scripts/validate_governance_and_audit.py` and
  print their outputs.

The script is conservative and skips any proposed relationship where either
slug is not present in the node files or the exact (start,end,type) triple
already exists in the target relationships file.
"""
import csv
import json
import os
import re
import glob
import argparse
import sys
import shutil
import datetime
import subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(ROOT, 'data')
NODES_GLOB = os.path.join(DATA_DIR, 'Nodes', 'nodes.*.json')
REL_DIR = os.path.join(DATA_DIR, 'Relationships')
DEFAULT_DECISIONS = os.path.join(DATA_DIR, 'orphan_triage_decisions.csv')


def load_slug_index():
    slug_index = {}
    for nf in sorted(glob.glob(NODES_GLOB)):
        try:
            with open(nf, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception:
            continue
        for n in data.get('nodes', []):
            slug = n.get('slug')
            if slug:
                slug_index[slug] = (nf, n.get('id'))
    return slug_index


def read_csv(path):
    rows = []
    with open(path, newline='', encoding='utf-8') as cf:
        r = csv.DictReader(cf)
        for row in r:
            rows.append(row)
    return rows


REL_SUGGEST_RE = re.compile(r'Added relationship:\s*`?(?P<start>[^`\s]+)`?\s*-\[(?P<type>[^\]]+)\]->\s*`?(?P<end>[^`\s]+)`?', re.IGNORECASE)


def parse_suggested_action(s):
    if not s:
        return None
    m = REL_SUGGEST_RE.search(s)
    if m:
        return m.group('start'), m.group('end'), m.group('type')
    # try a looser parse: start -[TYPE]-> end without backticks
    m2 = re.search(r'([^\s]+)\s*-\[([^\]]+)\]->\s*([^\s]+)', s)
    if m2:
        return m2.group(1), m2.group(3), m2.group(2)
    return None


def load_relationships_file(path):
    if not os.path.exists(path):
        return {'_meta': {'cluster': os.path.splitext(os.path.basename(path))[0].replace('relationships.', '')}, 'relationships': []}
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_relationships_file(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def determine_target_rel_file(cluster):
    # map cluster to relationships.<cluster>.json
    fname = f'relationships.{cluster}.json'
    return os.path.join(REL_DIR, fname)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--decisions', '-d', default=DEFAULT_DECISIONS)
    ap.add_argument('--apply', action='store_true', help='Write changes to files (default is dry-run)')
    ap.add_argument('--yes', action='store_true', help='Skip interactive confirmation (use with care)')
    ap.add_argument('--run-validators', action='store_true', help='Run validators after applying changes')
    args = ap.parse_args()

    if not os.path.exists(args.decisions):
        print(f'Decisions CSV not found at {args.decisions}. Export decisions from the UI first.')
        return 2

    slug_index = load_slug_index()
    rows = read_csv(args.decisions)

    to_add_by_file = {}  # rel_file -> list of new rel objects
    summary = []

    for r in rows:
        decision = (r.get('decision') or '').strip().lower()
        if decision != 'approve':
            continue
        cluster = r.get('cluster') or ''
        slug = r.get('slug') or ''

        # Try explicit columns first
        start = r.get('start_slug') or r.get('start') or ''
        end = r.get('end_slug') or r.get('end') or ''
        typ = r.get('type') or r.get('rel_type') or r.get('relationship_type') or ''

        # If relationship column exists and looks like JSON, try parse
        rel_col = r.get('relationship')
        if rel_col and not (start and end and typ):
            try:
                relj = json.loads(rel_col)
                start = start or relj.get('start_slug') or relj.get('start')
                end = end or relj.get('end_slug') or relj.get('end')
                typ = typ or relj.get('type')
            except Exception:
                # maybe string like start -[TYPE]-> end
                parsed = parse_suggested_action(rel_col)
                if parsed:
                    start, end, typ = parsed

        # fallback to suggested_action parsing
        if not (start and end and typ):
            parsed = parse_suggested_action(r.get('suggested_action') or '')
            if parsed:
                start, end, typ = parsed

        if not (start and end and typ):
            summary.append((slug, 'skipped', 'no relationship parsed'))
            continue

        # strip backticks if present
        start = start.strip().strip('`')
        end = end.strip().strip('`')
        typ = typ.strip()

        # ensure both slugs exist in index
        missing = []
        if start not in slug_index:
            missing.append(start)
        if end not in slug_index:
            missing.append(end)
        if missing:
            summary.append((slug, 'skipped', f'missing slug(s): {" ".join(missing)}'))
            continue

        # find target relationship file for cluster
        rel_file = determine_target_rel_file(cluster)
        rel_data = load_relationships_file(rel_file)
        rels = rel_data.get('relationships', [])
        existing = set((rr.get('start_slug'), rr.get('end_slug'), rr.get('type')) for rr in rels)

        if (start, end, typ) in existing:
            summary.append((slug, 'skipped', 'already exists'))
            continue

        # compute next id
        max_id = max((rr.get('id') or 0) for rr in rels) if rels else 0
        max_id += 1
        newrel = {
            'id': max_id,
            'start_slug': start,
            'end_slug': end,
            'type': typ,
            'description': f'Auto-applied from triage for {slug}',
            'status': 'PROPOSED',
            'evidence_url': None,
            'citation_style': None,
            'page_refs': None,
            'source_note': f'Applied by scripts/apply_approved_decisions.py on {datetime.datetime.utcnow().isoformat()} UTC'
        }

        to_add_by_file.setdefault(rel_file, {'rel_data': rel_data, 'new': []})
        to_add_by_file[rel_file]['new'].append(newrel)
        summary.append((slug, 'will_add', f'{start} -[{typ}]-> {end} -> {os.path.relpath(rel_file, ROOT)}'))

    # report and optionally apply
    if not to_add_by_file:
        print('No approved relationships to add.')
        return 0

    print('Proposed additions:')
    for s in summary:
        print(' -', s[0], s[1], s[2])

    if not args.apply:
        print('\nDry-run mode: no files modified. Rerun with --apply to write changes.')
        return 0

    # interactive confirmation unless --yes provided
    if not args.yes:
        if not sys.stdin.isatty():
            print('Non-interactive session detected; to apply changes pass --yes to confirm')
            return 2
        print('\nAbout to apply changes to the following files:')
        for rel_file in to_add_by_file:
            print(' -', rel_file)
        resp = input("Type 'yes' to proceed: ").strip().lower()
        if resp != 'yes':
            print('Aborted by user.')
            return 1

    # apply changes: backup files, append, save
    for rel_file, payload in to_add_by_file.items():
        bak = rel_file + f'.bak.{datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")}'
        if os.path.exists(rel_file):
            shutil.copy2(rel_file, bak)
            print(f'Backed up {rel_file} -> {bak}')
        else:
            # ensure directory exists
            os.makedirs(os.path.dirname(rel_file), exist_ok=True)
            print(f'Creating new relationships file {rel_file}')

        rd = payload['rel_data']
        rd.setdefault('relationships', [])
        rd['relationships'].extend(payload['new'])
        save_relationships_file(rel_file, rd)
        print(f'Wrote {len(payload["new"])} new relationships to {rel_file}')

    # optionally run validators
    if args.run_validators:
        print('\nRunning validators...')
        try:
            subprocess.run([os.path.join(ROOT, '.venv', 'bin', 'python'), os.path.join(ROOT, 'scripts', 'validate_slugs.py')], check=True)
        except Exception:
            # try system python
            subprocess.run(['python3', os.path.join(ROOT, 'scripts', 'validate_slugs.py')])
        try:
            subprocess.run([os.path.join(ROOT, '.venv', 'bin', 'python'), os.path.join(ROOT, 'scripts', 'validate_governance_and_audit.py')], check=True)
        except Exception:
            subprocess.run(['python3', os.path.join(ROOT, 'scripts', 'validate_governance_and_audit.py')])

    print('\nApply complete.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
