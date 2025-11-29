#!/usr/bin/env python3
"""Merge data/Relationships/relationships.json into
data/Relationships/relationships.English_Reformation.json, remove duplicates,
reassign ids sequentially, and back up previous cluster file.

Deduplication key: (type, start_ref, end_ref) where start_ref is start_slug if present else 'id:<start_id>'

Usage: python3 scripts/migrate_relationships_to_cluster.py
"""
import json
from pathlib import Path
import shutil

SRC = Path('data/Relationships/relationships.json')
TGT = Path('data/Relationships/relationships.English_Reformation.json')
TGT_BAK = TGT.with_suffix('.bak')

if not SRC.exists():
    print('Source relationships file not found:', SRC)
    raise SystemExit(1)

src = json.load(open(SRC,'r',encoding='utf-8'))
src_rels = src.get('relationships', [])

# load target if exists
if TGT.exists():
    tgt = json.load(open(TGT,'r',encoding='utf-8'))
    tgt_rels = tgt.get('relationships', [])
    # backup target
    shutil.copy2(TGT, TGT_BAK)
    print('Backed up existing target to', TGT_BAK)
else:
    tgt_rels = []

# combine lists, prefer entries from source first then target (to keep slug-based)
combined = src_rels + tgt_rels

seen = set()
unique = []
for r in combined:
    typ = (r.get('type') or '').upper()
    # determine start ref
    if 'start_slug' in r:
        sref = f"slug:{r.get('start_slug')}"
    elif 'start_id' in r:
        sref = f"id:{r.get('start_id')}"
    else:
        sref = 'none'
    if 'end_slug' in r:
        eref = f"slug:{r.get('end_slug')}"
    elif 'end_id' in r:
        eref = f"id:{r.get('end_id')}"
    else:
        eref = 'none'
    key = (typ, sref, eref)
    if key in seen:
        continue
    seen.add(key)
    unique.append(r)

# reassign ids sequentially starting at 1
for i, r in enumerate(unique, start=1):
    r['id'] = i
    # remove numeric start_id/end_id if slugs are present to prefer slug-based references
    if 'start_slug' in r and 'start_id' in r:
        r.pop('start_id', None)
    if 'end_slug' in r and 'end_id' in r:
        r.pop('end_id', None)

out = {
    '_meta': {
        'cluster': 'English_Reformation',
        'notes': 'Merged from relationships.json; deduplicated and ids reassigned by scripts/migrate_relationships_to_cluster.py',
        'registry': src.get('_meta', {}).get('registry'),
        'schema_doc': src.get('_meta', {}).get('schema_doc'),
    },
    'relationships': unique
}

with open(TGT, 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print('Wrote merged file to', TGT)
print('Total relationships (unique):', len(unique))
print('Sample first 5 ids:', [r['id'] for r in unique[:5]])
