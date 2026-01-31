#!/usr/bin/env python3
"""Remove mis-parsed node-table rows from relationship JSONs.

Some cluster README tables included Node rows inside the relationships
table. Those rows were parsed into relationship entries with type values
like "G", "C", or "G/C". Those are not canonical relationship verbs and
should be treated as node entries instead. This script conservatively
removes those rows from relationship files and makes backups.

Backups are written to the same directory with a `.bak.<TS>` suffix.
Run this script before any further normalization/ingest steps.
"""
from pathlib import Path
import json
from datetime import datetime, timezone


ROOT = Path(__file__).resolve().parents[2]
REL_DIR = ROOT / 'data' / 'Relationships'

TS = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
BAD_TYPES = {'G', 'C', 'G/C'}


def process_file(path: Path):
    with open(path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f"! Failed to parse {path}: {e}")
            return None

    rels = data.get('relationships')
    if not isinstance(rels, list):
        return None

    # count and filter
    original = len(rels)
    filtered = [r for r in rels if str(r.get('type') or '').strip() not in BAD_TYPES]
    removed = original - len(filtered)
    if removed <= 0:
        return {'file': str(path), 'removed': 0}

    # backup
    bak = path.with_suffix(path.suffix + f'.bak.{TS}')
    with open(bak, 'w', encoding='utf-8') as bf:
        json.dump(data, bf, ensure_ascii=False, indent=2)

    data['relationships'] = filtered
    with open(path, 'w', encoding='utf-8') as out:
        json.dump(data, out, ensure_ascii=False, indent=2)

    return {'file': str(path), 'removed': removed, 'backup': str(bak)}


def main():
    files = sorted(p for p in REL_DIR.glob('relationships.*.json') if p.is_file() and '.bak.' not in p.name)
    if not files:
        print('No relationship files found in', REL_DIR)
        return 0

    results = []
    for p in files:
        res = process_file(p)
        if res:
            results.append(res)

    print('\nCleanup summary:')
    total_removed = 0
    for r in results:
        print(f"- {r['file']}: removed={r['removed']} backup={r.get('backup')}")
        total_removed += r['removed']
    print(f'Total rows removed: {total_removed}')


if __name__ == '__main__':
    main()
