#!/usr/bin/env python3
"""
Extract node description tables from cluster READMEs and build a consolidated
Global Node Registry (docs/nodes/registry.md).

Assumptions:
- Descriptions appear under section headers like:
  #### Root and Periods (D)
  #### Persons (P)
  #### Institutions (I)
  #### Texts/Artifacts (T)
  #### Movements (M)
  #### Events (E)
  #### Places (L)
- Each section contains a Markdown table with columns: Node | G/C | Description

This script is idempotent and safe if some clusters have no tables yet.
"""
from __future__ import annotations
import re
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[1]
CLUSTERS_DIR = ROOT / 'docs' / 'clusters'
REGISTRY_PATH = ROOT / 'docs' / 'nodes' / 'registry.md'

SECTION_TO_TYPE = {
    'Root and Periods': 'D',
    'Persons': 'P',
    'Institutions': 'I',
    'Texts/Artifacts': 'T',
    'Movements': 'M',
    'Events': 'E',
    'Places': 'L',
}

def parse_readme(readme_path: Path) -> List[Dict]:
    rows: List[Dict] = []
    if not readme_path.exists():
        return rows
    text = readme_path.read_text(encoding='utf-8')
    lines = text.splitlines()
    section = None
    for i, line in enumerate(lines):
        if line.startswith('#### '):
            title = line.strip('# ').strip()
            for key in SECTION_TO_TYPE.keys():
                if title.startswith(key):
                    section = key
                    break
            else:
                section = None
            continue
        if not section:
            continue
        if line.startswith('|'):
            # Skip header/separator
            if re.match(r'^\|\s*---', line):
                continue
            cells = [c.strip() for c in line.strip().split('|')[1:-1]]
            if len(cells) >= 3 and cells[0] and cells[0] != 'Node':
                node, gc, desc = cells[0], cells[1], cells[2]
                type_code = SECTION_TO_TYPE[section]
                is_generic = (gc.upper().startswith('G'))
                rows.append({
                    'node': node,
                    'type': type_code,
                    'g_c': 'G' if is_generic else 'C',
                    'description': desc,
                })
    return rows

def build_registry() -> List[Dict]:
    all_rows: Dict[str, Dict] = {}
    for readme in CLUSTERS_DIR.glob('**/README.md'):
        cluster_name = readme.parent.name
        rows = parse_readme(readme)
        for r in rows:
            key = (r['node'])
            if key not in all_rows:
                r['clusters'] = {cluster_name}
                all_rows[key] = r
            else:
                all_rows[key]['clusters'].add(cluster_name)
                # Prefer first description, but if empty use new one
                if not all_rows[key]['description'] and r['description']:
                    all_rows[key]['description'] = r['description']
                # If type differs across clusters (should not), keep earliest
    # Flatten clusters sets
    result = []
    for k in sorted(all_rows.keys(), key=lambda s: s.lower()):
        r = all_rows[k]
        r['clusters'] = ','.join(sorted(r['clusters']))
        result.append(r)
    return result

def write_registry(rows: List[Dict]):
    REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    lines: List[str] = []
    lines.append('# Global Node Registry')
    lines.append('')
    lines.append('Source of truth for node one‑line descriptions. Generated from cluster READMEs. Do not hand‑edit this file; edit cluster tables instead and re‑generate.')
    lines.append('')
    lines.append(f'Total nodes: {len(rows)}')
    lines.append('')

    # Group by type
    type_order = ['D', 'P', 'I', 'T', 'M', 'E', 'L']
    type_labels = {
        'D': 'Doctrines & Periods (D)',
        'P': 'Persons (P)',
        'I': 'Institutions (I)',
        'T': 'Texts/Artifacts (T)',
        'M': 'Movements (M)',
        'E': 'Events (E)',
        'L': 'Places (L)',
    }
    grouped: Dict[str, List[Dict]] = {k: [] for k in type_order}
    for r in rows:
        grouped.setdefault(r['type'], []).append(r)
    # Sort each group by node name (case-insensitive)
    for k in grouped:
        grouped[k].sort(key=lambda x: x['node'].lower())

    for t in type_order:
        if not grouped.get(t):
            continue
        lines.append(f'## {type_labels.get(t, t)}')
        lines.append('')
        lines.append(f'Count: {len(grouped[t])}')
        lines.append('')
        lines.append('| Node | G/C | Description | Clusters |')
        lines.append('| --- | --- | --- | --- |')
        for r in grouped[t]:
            node = r['node']
            gc = r['g_c']
            desc = r['description'].replace('|', '\\|') if r['description'] else ''
            clusters = r.get('clusters', '')
            lines.append(f'| {node} | {gc} | {desc} | {clusters} |')
        lines.append('')

    REGISTRY_PATH.write_text('\n'.join(lines) + '\n', encoding='utf-8')

if __name__ == '__main__':
    rows = build_registry()
    write_registry(rows)
    print(f'Wrote {len(rows)} nodes to {REGISTRY_PATH}')
