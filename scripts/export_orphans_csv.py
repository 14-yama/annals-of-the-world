#!/usr/bin/env python3
"""Export orphan nodes (nodes not referenced by any relationship) to a CSV for triage."""
import csv
import glob
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(ROOT, 'data')
NODES_GLOB = os.path.join(DATA_DIR, 'Nodes', 'nodes.*.json')
REL_GLOB = os.path.join(DATA_DIR, 'Relationships', 'relationships.*.json')
OUT_CSV = os.path.join(DATA_DIR, 'orphan_nodes.csv')

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def cluster_from_path(p):
    # nodes.English_Reformation.json -> English_Reformation
    base = os.path.basename(p)
    if base.startswith('nodes.') and base.endswith('.json'):
        return base[len('nodes.'):-len('.json')]
    return base

def main():
    node_files = sorted(glob.glob(NODES_GLOB))
    rel_files = sorted(glob.glob(REL_GLOB))

    slug_to_entry = {}  # slug -> (cluster, file, id)
    for nf in node_files:
        data = load_json(nf)
        cluster = data.get('_meta', {}).get('cluster') or cluster_from_path(nf)
        for n in data.get('nodes', []):
            slug = n.get('slug')
            nid = n.get('id')
            slug_to_entry[slug] = (cluster, os.path.relpath(nf, ROOT), nid)

    referenced = set()
    for rf in rel_files:
        data = load_json(rf)
        for r in data.get('relationships', []):
            for fld in ('start_slug', 'end_slug'):
                v = r.get(fld)
                if v:
                    referenced.add(v)

    orphans = [ (s, slug_to_entry[s]) for s in sorted(slug_to_entry.keys()) if s not in referenced ]

    with open(OUT_CSV, 'w', newline='', encoding='utf-8') as csvf:
        w = csv.writer(csvf)
        w.writerow(['cluster','file','id','slug','suggested_action'])
        for slug, (cluster, file, nid) in orphans:
            w.writerow([cluster, file, nid, slug, ''])

    print(f'Wrote {len(orphans)} orphan rows to {OUT_CSV}')

if __name__ == '__main__':
    main()
