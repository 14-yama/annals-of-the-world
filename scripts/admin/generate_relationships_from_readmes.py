#!/usr/bin/env python3
"""Generate cluster relationship JSONs from cluster README files.

Scans all `docs/clusters/*/README.md` files, extracts conservative
cluster-level relationships (parent root and interfaces to other
clusters), and writes `data/Relationships/relationships.<Cluster>.json`.
After generation, runs the normalizers to align attributes with the
relationship schema.

This is the canonical generator; older scripts have been renamed to
delegate here.
"""

import re
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CLUSTERS_DIR = ROOT / 'docs' / 'clusters'


def parse_relationships_from_readme(readme_path: Path, cluster_slug: str):
    """Extract relationships from a README.

    Includes parent roots (IS_PART_OF), interfaces (INTERFACES_WITH), and
    rows from a `### Relationships` Markdown table.
    """

    text = readme_path.read_text(encoding='utf-8')
    lines = text.splitlines()

    parent_root = None
    interfaces = []

    m = re.search(r'Parent root:\s*([^\(\n]+)', text)
    if m:
        parent_root = m.group(1).strip()

    interfaces_section = False
    for line in lines:
        if re.search(r'Interfaces to other clusters', line, re.I):
            interfaces_section = True
            continue
        if interfaces_section:
            if not line.strip():
                break
            m2 = re.match(r'-\s*([A-Za-z0-9_\-]+)', line.strip())
            if m2:
                interfaces.append(m2.group(1).strip())

    rels = []
    next_id = 1

    if parent_root:
        rels.append(
            {
                'id': next_id,
                'start_slug': cluster_slug,
                'end_slug': parent_root.strip(),
                'type': 'IS_PART_OF',
                'description': f"{cluster_slug} has parent root {parent_root}",
                'status': 'PROPOSED',
                'evidence_url': None,
                'citation_style': None,
                'page_refs': None,
                'source_note': 'auto:from_readme',
            }
        )
        next_id += 1

    for iface in interfaces:
        rels.append(
            {
                'id': next_id,
                'start_slug': cluster_slug,
                'end_slug': iface,
                'type': 'INTERFACES_WITH',
                'description': f"{cluster_slug} interfaces with {iface}",
                'status': 'PROPOSED',
                'evidence_url': None,
                'citation_style': None,
                'page_refs': None,
                'source_note': 'auto:from_readme',
            }
        )
        next_id += 1

    in_rel_section = False
    in_table = False

    for line in lines:
        if re.match(r'^###\s+Relationships\s*$', line.strip(), re.I):
            in_rel_section = True
            in_table = False
            continue

        if not in_rel_section:
            continue

        if re.match(r'^###\s+[^#]', line) and not re.match(r'^###\s+Relationships\s*$', line.strip(), re.I):
            break

        stripped = line.strip()
        if not stripped:
            continue

        if stripped.startswith('|'):
            parts = [p.strip() for p in stripped.split('|')[1:-1]]
            if not parts:
                continue
            if all(re.match(r'^-+$', p) for p in parts):
                in_table = True
                continue
            if parts[0].lower() in ('start', ''):
                continue
            if not in_table:
                continue

            while len(parts) < 4:
                parts.append('')

            start_slug = parts[0].strip()
            rel_type = parts[1].strip()
            end_slug = parts[2].strip()
            desc = parts[3].strip() or None

            if not (start_slug and rel_type and end_slug):
                continue

            rels.append(
                {
                    'id': next_id,
                    'start_slug': start_slug,
                    'end_slug': end_slug,
                    'type': rel_type,
                    'description': desc or f"{start_slug} {rel_type} {end_slug}",
                    'status': 'PROPOSED',
                    'evidence_url': None,
                    'citation_style': None,
                    'page_refs': None,
                    'source_note': 'auto:from_readme:relationships_table',
                }
            )
            next_id += 1

    return rels


def write_relationships(cluster_slug: str, rels: list, readme_path: Path):
    tgt = ROOT / 'data' / 'Relationships' / f'relationships.{cluster_slug}.json'
    if tgt.exists():
        bak = tgt.with_suffix('.bak.' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'))
        shutil.copy2(tgt, bak)
        print(f'Backed up {tgt.name} -> {bak.name}')

    out = {
        '_meta': {
            'cluster': cluster_slug,
            'notes': 'Auto-generated conservative relationships from README.md',
            'registry': 'docs/guidelines/node-relationship-vocabulary.md',
            'schema_doc': 'docs/guidelines/schema.md',
            'source': str(readme_path.relative_to(ROOT)),
            'generated_at': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%MZ'),
            'generator': 'scripts/admin/generate_relationships_from_readmes.py',
        },
        'relationships': rels,
    }

    tgt.parent.mkdir(parents=True, exist_ok=True)
    with open(tgt, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f'Wrote {tgt.name} with {len(rels)} relationships')
    if rels:
        print('Sample:', rels[:5])
    else:
        print('No parent root or interfaces found; wrote empty relationships list.')


def run_normalizers():
    node_norm = ROOT / 'scripts' / 'normalize_nodes.py'
    rel_norm = ROOT / 'scripts' / 'normalize_relationships.py'

    def _run(cmd):
        print(f"Running normalizer: {' '.join(cmd)}")
        try:
            res = subprocess.run(cmd, check=False, capture_output=True, text=True)
        except FileNotFoundError:
            print(f"  Command not found: {cmd[0]}")
            return 127
        if res.stdout.strip():
            print(res.stdout.strip())
        if res.stderr.strip():
            print(res.stderr.strip())
        return res.returncode

    exit_code = 0

    if node_norm.exists():
        code = _run(['python3', str(node_norm)])
        if code != 0:
            print(f"Node normalizer exited with {code}")
            exit_code = code
    else:
        print(f"Node normalizer not found at {node_norm}; skipping.")

    if rel_norm.exists():
        code = _run(['python3', str(rel_norm)])
        if code != 0 and exit_code == 0:
            print(f"Relationship normalizer exited with {code}")
            exit_code = code
    else:
        print(f"Relationship normalizer not found at {rel_norm}; skipping.")

    return exit_code


def main():
    if not CLUSTERS_DIR.exists():
        print(f'Clusters directory not found: {CLUSTERS_DIR}')
        raise SystemExit(1)

    readmes = sorted((p for p in CLUSTERS_DIR.glob('*/README.md') if p.is_file()))
    if not readmes:
        print(f'No cluster READMEs found under {CLUSTERS_DIR}')
        raise SystemExit(1)

    print(f'Found {len(readmes)} cluster READMEs')
    print('=' * 60)

    total_rels = 0
    processed = 0
    errors = []

    for readme in readmes:
        cluster_slug = readme.parent.name
        try:
            print(f'\nProcessing: {cluster_slug}')
            rels = parse_relationships_from_readme(readme, cluster_slug)
            write_relationships(cluster_slug, rels, readme)
            total_rels += len(rels)
            processed += 1
        except Exception as e:
            error_msg = f'Error processing {cluster_slug}: {e}'
            print(error_msg)
            errors.append(error_msg)

    print('\n' + '=' * 60)
    print('Generation summary:')
    print(f'  Processed clusters: {processed}/{len(readmes)}')
    print(f'  Total relationships generated: {total_rels}')
    if errors:
        print(f'  Errors during generation: {len(errors)}')
        for err in errors:
            print(f'    - {err}')
    else:
        print('  ✓ All clusters generated successfully')

    print('\nRunning normalizers to align with schema attributes...')
    norm_code = run_normalizers()
    if norm_code != 0:
        print(f'Normalizers completed with non-zero exit code: {norm_code}')
    else:
        print('✓ Normalizers completed successfully')


if __name__ == '__main__':
    main()
