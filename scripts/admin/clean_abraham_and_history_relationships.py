#!/usr/bin/env python3
"""Clean project relationships:

- Remove numeric-ID relationships from `relationships.slugs_from_history.json` (these use start_id/end_id).
- Remove any relationships referencing the slug 'abraham' (case-insensitive).
- Remove the node with slug 'Abraham' from `nodes.Hebrew_Tradition.json`.

Backups are written before modification.
"""
from pathlib import Path
import json
import shutil

ROOT = Path(__file__).resolve().parents[2]
REL_DIR = ROOT / 'data' / 'Relationships'
NODES_DIR = ROOT / 'data' / 'Nodes'
BACKUP_DIR = REL_DIR / 'back_ups'
BACKUP_DIR.mkdir(parents=True, exist_ok=True)


def load_json(p: Path):
    return json.loads(p.read_text(encoding='utf-8'))


def write_json(p: Path, data):
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def clean_slugs_from_history():
    p = REL_DIR / 'relationships.slugs_from_history.json'
    if not p.exists():
        print('No slugs_from_history file found; skipping')
        return
    print('Cleaning', p)
    bak = BACKUP_DIR / f'relationships.slugs_from_history.json.bak'
    shutil.copy2(p, bak)
    data = load_json(p)
    rels = data.get('relationships', [])
    cleaned = [r for r in rels if 'start_slug' in r and 'end_slug' in r]
    removed = len(rels) - len(cleaned)
    data['relationships'] = cleaned
    write_json(p, data)
    print(f'Removed {removed} numeric-id relationships from {p.name}')


def remove_abraham_relationships():
    # remove any relationship referencing slug 'abraham' (case-insensitive)
    for p in sorted(REL_DIR.iterdir()):
        if p.suffix != '.json':
            continue
        if p.name.startswith('back_ups'):
            continue
        data = load_json(p)
        rels = data.get('relationships', [])
        new_rels = []
        removed = 0
        for r in rels:
            s = (r.get('start_slug') or '').lower()
            e = (r.get('end_slug') or '').lower()
            if s == 'abraham' or e == 'abraham':
                removed += 1
                continue
            new_rels.append(r)
        if removed:
            bak = BACKUP_DIR / f'{p.name}.bak'
            shutil.copy2(p, bak)
            data['relationships'] = new_rels
            write_json(p, data)
            print(f'Removed {removed} Abraham relationships from {p.name}')


def remove_abraham_node():
    p = NODES_DIR / 'nodes.Hebrew_Tradition.json'
    if not p.exists():
        print('No Hebrew nodes file; skipping node removal')
        return
    data = load_json(p)
    nodes = data.get('nodes', [])
    new_nodes = [n for n in nodes if (n.get('slug') or '').lower() != 'abraham']
    removed = len(nodes) - len(new_nodes)
    if removed:
        bak = BACKUP_DIR / 'nodes.Hebrew_Tradition.json.bak'
        shutil.copy2(p, bak)
        data['nodes'] = new_nodes
        write_json(p, data)
        print(f'Removed {removed} Abraham node(s) from nodes.Hebrew_Tradition.json')
    else:
        print('No Abraham node found in nodes.Hebrew_Tradition.json')


def main():
    clean_slugs_from_history()
    remove_abraham_relationships()
    remove_abraham_node()


if __name__ == '__main__':
    main()
