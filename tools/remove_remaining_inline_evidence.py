#!/usr/bin/env python3
import json
from pathlib import Path

REL_PATH = Path('data/Relationships/relationships.English_Reformation.json')

if not REL_PATH.exists():
    print('Relationships file not found:', REL_PATH)
    raise SystemExit(1)

with REL_PATH.open('r', encoding='utf-8') as f:
    data = json.load(f)

rels = data.get('relationships', [])
removed = 0
keep = 0
for rel in rels:
    # only remove if there is no evidence_slug
    if 'evidence_slug' not in rel:
        removed_any = False
        for key in ['evidence_url', 'source_note']:
            if key in rel:
                del rel[key]
                removed_any = True
        if removed_any:
            removed += 1
        else:
            keep += 1

# write backup
bak = REL_PATH.with_suffix('.json.inline-removed.bak')
REL_PATH.replace(bak)

with REL_PATH.open('w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f'Removed inline evidence fields from {removed} relationships.')
print(f'{keep} relationships had no inline fields and no evidence_slug.')
print('Backup saved as', bak)
