#!/usr/bin/env python3
"""Validate governance fields on nodes and run a lightweight ingest audit.

Checks performed:
- For every node in data/Nodes/nodes.*.json, ensure required governance fields exist and have roughly correct types:
  required: slug (str), status (one of PROPOSED, REVIEWED, APPROVED), workflow_stage (str), created_at (ISO string), created_by (str), governance_version (int)
- Report nodes missing fields or with invalid values.
- Run an orphan-node audit: nodes that are not referenced by any relationship (start/end) across data/Relationships/*.json.

Exits with code 0 on no governance errors (orphans allowed but reported). Non-zero if governance errors found.
"""
import glob
import json
import os
import sys
from datetime import datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(ROOT, 'data')
NODES_GLOB = os.path.join(DATA_DIR, 'Nodes', 'nodes.*.json')
REL_GLOB = os.path.join(DATA_DIR, 'Relationships', 'relationships.*.json')

VALID_STATUSES = {'PROPOSED', 'REVIEWED', 'APPROVED'}

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def parse_iso(dt_str):
    if not isinstance(dt_str, str):
        raise ValueError('not a string')
    # handle trailing Z
    try:
        if dt_str.endswith('Z'):
            dt_str = dt_str[:-1] + '+00:00'
        return datetime.fromisoformat(dt_str)
    except Exception as e:
        raise

def main():
    node_files = sorted(glob.glob(NODES_GLOB))
    rel_files = sorted(glob.glob(REL_GLOB))
    if not node_files:
        print('No node files found; aborting')
        return 2

    governance_errors = []
    slug_to_node = {}  # slug -> (file, id)
    total_nodes = 0
    for nf in node_files:
        data = load_json(nf)
        nodes = data.get('nodes', [])
        for n in nodes:
            total_nodes += 1
            slug = n.get('slug')
            nid = n.get('id')
            slug_to_node.setdefault(slug, []).append((nf, nid))
            # check required fields
            missing = []
            if not slug or not isinstance(slug, str):
                missing.append('slug')
            status = n.get('status')
            if status not in VALID_STATUSES:
                missing.append('status')
            if 'workflow_stage' not in n or not isinstance(n.get('workflow_stage'), str):
                missing.append('workflow_stage')
            if 'created_at' not in n:
                missing.append('created_at')
            else:
                try:
                    parse_iso(n.get('created_at'))
                except Exception:
                    missing.append('created_at(iso)')
            if 'created_by' not in n or not isinstance(n.get('created_by'), str):
                missing.append('created_by')
            if 'governance_version' not in n or not isinstance(n.get('governance_version'), int):
                missing.append('governance_version')

            if missing:
                governance_errors.append({'file': nf, 'id': nid, 'slug': slug, 'missing': missing})

    # collect referenced slugs from relationships
    referenced = set()
    total_rels = 0
    for rf in rel_files:
        rdata = load_json(rf)
        for r in rdata.get('relationships', []):
            total_rels += 1
            for fld in ('start_slug', 'end_slug'):
                val = r.get(fld)
                if val:
                    referenced.add(val)

    # find orphan nodes (not referenced anywhere)
    node_slugs = set([s for s in slug_to_node.keys() if s])
    orphans = sorted(list(node_slugs - referenced))

    # Report
    print('\nGovernance validation report')
    print('--------------------------------')
    print(f'Node files checked: {len(node_files)}; Total nodes: {total_nodes}')
    print(f'Relationship files checked: {len(rel_files)}; Total relationships: {total_rels}')
    print()

    if governance_errors:
        print('Governance issues found:')
        for e in governance_errors:
            relpath = os.path.relpath(e['file'], ROOT)
            print(f" - file: {relpath}, id: {e['id']}, slug: {e['slug']}, problems: {', '.join(e['missing'])}")
        print()
    else:
        print('No governance field issues detected.')

    print('\nOrphan node audit')
    print('-------------------')
    print(f'Total node slugs: {len(node_slugs)}; referenced slugs: {len(referenced)}')
    print(f'Orphan node count: {len(orphans)}')
    # show a short sample (up to 40) of orphans so maintainers can triage
    for s in orphans[:40]:
        entries = slug_to_node.get(s, [])
        for fn, nid in entries:
            print(f'  - slug: {s}, file: {os.path.relpath(fn, ROOT)}, id: {nid}')

    # Exit code: non-zero if governance errors exist
    if governance_errors:
        print('\nFAIL: governance errors detected')
        return 1
    else:
        print('\nPASS: governance checks passed (orphans reported for triage)')
        return 0

if __name__ == '__main__':
    sys.exit(main())
