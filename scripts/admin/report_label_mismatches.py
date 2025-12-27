#!/usr/bin/env python3
"""Report mismatches between data/Nodes/*.json labels and docs/clusters/<cluster>/README.md groupings.

Outputs a CSV-like report: cluster,slug,json_label,readme_label
"""
import json
from pathlib import Path
from scripts.admin.normalize_nodes_all_clusters import load_cluster_readme_mappings

ROOT = Path(__file__).resolve().parents[2]
NODES_DIR = ROOT / 'data' / 'Nodes'


def normalize_slug(s: str) -> str:
    return s.strip()


def main():
    rows = []
    for p in sorted(NODES_DIR.iterdir()):
        if p.suffix != '.json' or 'bak' in p.name:
            continue
        try:
            data = json.loads(p.read_text(encoding='utf-8'))
        except Exception as e:
            print(f"Skipping {p.name}: parse error: {e}")
            continue

        cluster = p.name.replace('nodes.', '').replace('.json', '')
        readme = ROOT / 'docs' / 'clusters' / cluster / 'README.md'
        mapping = {}
        if readme.exists():
            try:
                mapping = load_cluster_readme_mappings(readme)
            except Exception:
                mapping = {}

        for n in data.get('nodes', []):
            slug = normalize_slug(n.get('slug') or '')
            jl = n.get('label') or ''
            rl = mapping.get(slug, '')
            if rl and rl != jl:
                rows.append((cluster, slug, jl, rl))

    if not rows:
        print('No mismatches found: JSON labels align with README groupings.')
        return 0

    print('cluster,slug,json_label,readme_label')
    for r in rows:
        print(','.join(r))
    print(f'\nTotal mismatches: {len(rows)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
