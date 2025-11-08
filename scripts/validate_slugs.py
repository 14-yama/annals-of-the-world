#!/usr/bin/env python3
"""Validate slugs across per-cluster node files and relationships.

Checks performed:
- Loads all files matching data/Nodes/nodes.*.json and collects node slugs.
- Detects duplicate slugs across files.
- Loads all relationship files under data/Relationships/relationships.*.json and verifies
  that every start_slug and end_slug resolves to a node slug.

Exits with code 0 on success (no missing slugs and no duplicates). Non-zero on issues.
"""
import json
import glob
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(ROOT, 'data')
NODES_GLOB = os.path.join(DATA_DIR, 'Nodes', 'nodes.*.json')
REL_GLOB = os.path.join(DATA_DIR, 'Relationships', 'relationships.*.json')

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    node_files = sorted(glob.glob(NODES_GLOB))
    if not node_files:
        print('No node files found matching', NODES_GLOB)
        return 2

    slug_index = {}  # slug -> list of (file, id)
    total_nodes = 0
    for nf in node_files:
        try:
            data = load_json(nf)
        except Exception as e:
            print(f'ERROR: failed to load {nf}: {e}')
            return 3
        nodes = data.get('nodes', [])
        for n in nodes:
            total_nodes += 1
            slug = n.get('slug')
            nid = n.get('id')
            if not slug:
                # record nodes without slugs under an explicit key
                slug = '<MISSING_SLUG>'
            slug_index.setdefault(slug, []).append((nf, nid))

    duplicates = {s: v for s, v in slug_index.items() if len(v) > 1}

    # Relationships
    rel_files = sorted(glob.glob(REL_GLOB))
    missing = []  # tuples: (rel_file, rel_id, missing_slug, field)
    total_rels = 0
    for rf in rel_files:
        try:
            rdata = load_json(rf)
        except Exception as e:
            print(f'ERROR: failed to load {rf}: {e}')
            return 4
        rels = rdata.get('relationships', [])
        for r in rels:
            total_rels += 1
            rid = r.get('id')
            for fld in ('start_slug', 'end_slug'):
                val = r.get(fld)
                if val is None:
                    missing.append((rf, rid, None, fld))
                elif val not in slug_index:
                    missing.append((rf, rid, val, fld))

    # Report
    print('Validation report')
    print('-----------------')
    print(f'Node files checked: {len(node_files)}')
    print(f'Total nodes indexed: {total_nodes}')
    print(f'Relationship files checked: {len(rel_files)}')
    print(f'Total relationships checked: {total_rels}')
    print()

    ok = True
    if duplicates:
        ok = False
        print('Duplicate slugs detected:')
        for s, entries in duplicates.items():
            print(f'  slug: {s}')
            for fn, nid in entries:
                print(f'    - file: {os.path.relpath(fn, ROOT)}, id: {nid}')
        print()

    if missing:
        ok = False
        print('Missing or unresolved slugs found in relationships:')
        for rf, rid, slug, fld in missing:
            rel_path = os.path.relpath(rf, ROOT)
            print(f'  rel_file: {rel_path}, rel_id: {rid}, field: {fld}, value: {slug}')
        print()

    if ok:
        print('PASS: No duplicate slugs and all relationship slugs resolved.')
        return 0
    else:
        print('FAIL: Issues detected. See details above.')
        return 1

if __name__ == '__main__':
    sys.exit(main())
