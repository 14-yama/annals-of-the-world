#!/usr/bin/env python3
"""Clean up `data/Relationships/relationships.English_Reformation.json` by
- Backing up the original file
- Removing duplicate relationships (key: TYPE + start_ref + end_ref)
- Prefer records that use slugs over numeric ids when duplicates exist
- Reassign sequential `id` values starting at 1

Usage: python3 scripts/cleanup_relationships_dedupe.py
"""
import json
from pathlib import Path
import shutil
import datetime

P = Path('data/Relationships/relationships.English_Reformation.json')
if not P.exists():
    print('Target file not found:', P)
    raise SystemExit(1)

bak = P.with_suffix('.bak.' + datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ'))
shutil.copy2(P, bak)
print('Backup created:', bak)

data = json.load(open(P, 'r', encoding='utf-8'))
rels = data.get('relationships', [])
print('Original relationships count:', len(rels))

# helper to produce normalized ref
def ref_for(r, which):
    slug = r.get(f'{which}_slug')
    if slug:
        return ('slug', slug)
    # numeric ids may be present as start_id/end_id or start/end
    for alt in (f'{which}_id', which, f'{which}Id'):
        if alt in r and r.get(alt) is not None:
            return ('id', str(r.get(alt)))
    return ('none', '')

# dedupe preferring slug-based records
seen = {}
order = []
for r in rels:
    typ = (r.get('type') or '').upper()
    s_kind, s_val = ref_for(r, 'start')
    e_kind, e_val = ref_for(r, 'end')
    key = (typ, s_val if s_kind=='slug' or s_kind=='id' else s_val, e_val if e_kind in ('slug','id') else e_val)
    # if not seen, record
    if key not in seen:
        seen[key] = r
        order.append(key)
    else:
        # prefer slug-bearing record
        existing = seen[key]
        # if existing has id refs and new has slug refs -> replace
        ex_s_slug = existing.get('start_slug') is not None
        ex_e_slug = existing.get('end_slug') is not None
        new_s_slug = r.get('start_slug') is not None
        new_e_slug = r.get('end_slug') is not None
        # if new has at least one slug and existing has none, prefer new
        if (new_s_slug or new_e_slug) and not (ex_s_slug or ex_e_slug):
            seen[key] = r
        # otherwise keep existing

unique = [seen[k] for k in order]

# Normalize: if record has slug for start/end, remove numeric id fields to prefer slugs
for r in unique:
    if r.get('start_slug') and 'start_id' in r:
        r.pop('start_id', None)
    if r.get('end_slug') and 'end_id' in r:
        r.pop('end_id', None)

# reassign ids sequentially
for i, r in enumerate(unique, start=1):
    r['id'] = i

new_data = data.copy()
new_data['relationships'] = unique

with open(P, 'w', encoding='utf-8') as f:
    json.dump(new_data, f, ensure_ascii=False, indent=2)

print('Wrote cleaned file:', P)
print('Cleaned relationships count:', len(unique))
print('Backup is at:', bak)
