#!/usr/bin/env python3
import json
import glob
import os
import csv

ROOT = os.path.dirname(os.path.dirname(__file__))
NODES_GLOB = os.path.join(ROOT, 'data', 'Nodes', '*.json')
REL_FILE = os.path.join(ROOT, 'data', 'Relationships', 'relationships.json')
OUT_CSV = os.path.join(ROOT, 'data', 'orphan_relationship_slugs.csv')


def collect_node_slugs():
    slugs = set()
    files = glob.glob(NODES_GLOB)
    for p in files:
        try:
            with open(p, 'r', encoding='utf-8') as fh:
                doc = json.load(fh)
        except Exception:
            # skip non-json or unreadable files
            continue
        # doc may be {"nodes": [...]} or an array of nodes
        candidates = []
        if isinstance(doc, dict):
            if 'nodes' in doc and isinstance(doc['nodes'], list):
                candidates = doc['nodes']
            else:
                # maybe dict of slug -> node or single node
                # collect any dict values that look like nodes
                for v in doc.values():
                    if isinstance(v, dict) and 'slug' in v:
                        candidates.append(v)
        elif isinstance(doc, list):
            candidates = doc
        for n in candidates:
            if not isinstance(n, dict):
                continue
            s = n.get('slug') or n.get('id') or n.get('name')
            if s:
                slugs.add(str(s).strip().lower())
    return slugs


def collect_relationship_slugs():
    with open(REL_FILE, 'r', encoding='utf-8') as fh:
        reldoc = json.load(fh)
    rels = reldoc.get('relationships', [])
    referenced = []
    for r in rels:
        rid = r.get('id')
        for key in ('start_slug', 'end_slug'):
            if key in r and r[key]:
                referenced.append((rid, key, str(r[key]).strip().lower(), r.get('description')))
    return referenced


def main():
    node_slugs = collect_node_slugs()
    referenced = collect_relationship_slugs()

    missing = {}
    for rid, key, slug, desc in referenced:
        if slug not in node_slugs:
            info = missing.setdefault(slug, {'roles': set(), 'rels': set(), 'examples': []})
            role = 'start' if key == 'start_slug' else 'end'
            info['roles'].add(role)
            info['rels'].add(str(rid) if rid is not None else 'unknown')
            if desc:
                info['examples'].append(desc)

    # write CSV
    with open(OUT_CSV, 'w', encoding='utf-8', newline='') as csvf:
        writer = csv.writer(csvf)
        writer.writerow(['slug','roles','relationship_ids','example_descriptions'])
        for slug, info in sorted(missing.items()):
            writer.writerow([
                slug,
                ';'.join(sorted(info['roles'])),
                ';'.join(sorted(info['rels'])),
                ' | '.join(info['examples'][:3])
            ])

    print(f"Found {len(missing)} missing slugs referenced by relationships. CSV: {OUT_CSV}")

if __name__ == '__main__':
    main()
