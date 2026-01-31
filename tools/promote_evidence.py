#!/usr/bin/env python3
import json
from pathlib import Path

REL_PATH = Path('data/Relationships/relationships.English_Reformation.json')

mapping = {
    'Bray, Gerald': 'evidence.Bray_1994_Documents_of_the_English_Reformation',
    'Elton, G.R.': 'evidence.Elton_1982_Tudor_Constitution',
    'Daniell, David.': 'evidence.Daniell_2003_The_Bible_in_English',
    'Bernard, G.W.': 'evidence.Bernard_2005_The_Kings_Reformation',
    'Bossy, John.': 'evidence.Bossy_1975_English_Catholic_Community',
    'Scarisbrick, J.J.': 'evidence.Scarisbrick_1968_Henry_VIII',
    'Haigh, Christopher.': 'evidence.Haigh_1993_English_Reformations',
    'MacCulloch, Diarmaid.': 'evidence_MacCulloch_1996_Thomas_Cranmer',
    'Duffy, Eamon.': 'evidence.Duffy_2009_Fires_of_Faith'
}

if not REL_PATH.exists():
    print('Relationships file not found:', REL_PATH)
    raise SystemExit(1)

with REL_PATH.open('r', encoding='utf-8') as f:
    data = json.load(f)

relationships = data.get('relationships', [])
updated = 0
mapped_counts = {}
for rel in relationships:
    src = rel.get('source_note', '') or ''
    matched = None
    for key, slug in mapping.items():
        if key in src:
            matched = slug
            mapped_counts[slug] = mapped_counts.get(slug, 0) + 1
            break
    if matched:
        rel['evidence_slug'] = matched
        # remove inline fields
        if 'evidence_url' in rel:
            del rel['evidence_url']
        if 'source_note' in rel:
            del rel['source_note']
        updated += 1

# write backup
bak = REL_PATH.with_suffix('.json.bak')
REL_PATH.replace(bak)

with REL_PATH.open('w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f'Updated {updated} relationships to use evidence_slug.')
print('Mapped counts:')
for k, v in mapped_counts.items():
    print(' ', k, v)
print('Backup saved as', bak)
print('Done')
