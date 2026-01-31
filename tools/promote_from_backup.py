#!/usr/bin/env python3
import json
import re
from pathlib import Path
import hashlib

BACKUP = Path('data/Relationships/relationships.English_Reformation.json.inline-removed.bak')
REL_PATH = Path('data/Relationships/relationships.English_Reformation.json')
EVIDENCE_DIR = Path('data/Evidence')
EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)

if not BACKUP.exists():
    print('Backup file not found:', BACKUP)
    raise SystemExit(1)
if not REL_PATH.exists():
    print('Relationships file not found:', REL_PATH)
    raise SystemExit(1)

with BACKUP.open('r', encoding='utf-8') as f:
    bak = json.load(f)
with REL_PATH.open('r', encoding='utf-8') as f:
    cur = json.load(f)

bak_rels = {r.get('id'): r for r in bak.get('relationships', [])}
cur_rels = {r.get('id'): r for r in cur.get('relationships', [])}

# collect unique inline citations from backup for relationships that lacked evidence_slug
unique = {}
for rid, rel in bak_rels.items():
    if 'evidence_slug' not in rel:
        src = rel.get('source_note')
        url = rel.get('evidence_url')
        if src or url:
            key = (src or '').strip() + '||' + (url or '').strip()
            if key not in unique:
                unique[key] = {'source_note': src, 'evidence_url': url, 'ids': []}
            unique[key]['ids'].append(rid)

if not unique:
    print('No inline citations found in backup to promote.')
    raise SystemExit(0)

created = 0
mapping = {}

def slugify_from_source(source_note):
    s = (source_note or '').strip()
    # try to extract author before first period
    author = None
    title = None
    year = None
    if '.' in s:
        parts = [p.strip() for p in s.split('.') if p.strip()]
        if parts:
            author = parts[0]
            if len(parts) > 1:
                title = parts[1]
    else:
        # fallback: first 60 chars
        title = s[:60]
    # find year
    m = re.search(r'(19|20)\d{2}', s)
    if m:
        year = m.group(0)
    # derive last name
    last = None
    if author:
        if ',' in author:
            last = author.split(',')[0].strip()
        else:
            last = author.split()[-1].strip()
    if not last:
        last = 'source'
    # short title token
    ttoken = ''
    if title:
        # take first alnum words
        toks = re.findall(r"[A-Za-z0-9]+", title)
        if toks:
            ttoken = '_'.join(toks[:3])
    # unique suffix
    h = hashlib.sha1(s.encode('utf-8')).hexdigest()[:6]
    parts = ['evidence', last]
    if year:
        parts.append(year)
    if ttoken:
        parts.append(ttoken)
    parts.append(h)
    slug = '_'.join(parts)
    # sanitize
    slug = re.sub(r'[^A-Za-z0-9_\-\.]+', '_', slug)
    return slug

for key, info in unique.items():
    src = info['source_note']
    url = info['evidence_url']
    ids = info['ids']
    slug = slugify_from_source(src or url or 'inline')
    filename = EVIDENCE_DIR / f'{slug}.json'
    # avoid overwriting if exists; if exists, use that slug
    if filename.exists():
        mapping[key] = filename.stem
        continue
    # attempt to build readable metadata
    author = None
    title = None
    year = None
    if src:
        if '.' in src:
            parts = [p.strip() for p in src.split('.') if p.strip()]
            author = parts[0]
            if len(parts) > 1:
                title = parts[1]
        else:
            title = src
        m = re.search(r'(19|20)\d{2}', src)
        if m:
            year = m.group(0)
    else:
        title = url
    data = {
        'slug': filename.stem,
        'title': title or '',
        'author': author or '',
        'year': int(year) if year else None,
        'publisher': '',
        'evidence_url': url or '',
        'citation_style': 'Chicago 17',
        'notes': 'Promoted from inline relationship source_note/evidence_url',
        'has_text': False
    }
    # write file
    with filename.open('w', encoding='utf-8') as f:
        json.dump({k: v for k, v in data.items() if v is not None and v != ''}, f, indent=2, ensure_ascii=False)
    created += 1
    mapping[key] = filename.stem

# now update current relationships for these ids
updated = 0
ids_updated = []
for key, info in unique.items():
    ids = info['ids']
    slug = mapping.get(key)
    for rid in ids:
        rel = cur_rels.get(rid)
        if rel is not None:
            # only add if not already has evidence_slug
            if 'evidence_slug' not in rel:
                rel['evidence_slug'] = slug
                updated += 1
                ids_updated.append(rid)

# write backup of current and save
bak2 = REL_PATH.with_suffix('.json.pre-evidence-promotion.bak')
REL_PATH.replace(bak2)
with REL_PATH.open('w', encoding='utf-8') as f:
    json.dump(cur, f, indent=2, ensure_ascii=False)

print(f'Created {created} evidence files.')
print(f'Added evidence_slug to {updated} relationships.')
print('Evidence mapping samples (up to 10):')
for i, (k, v) in enumerate(mapping.items()):
    if i >= 10: break
    sn, eu = k.split('||')
    print(' ', v, '-', sn[:80].replace('\n',' '), '|', eu)
print('Backup of previous relationships saved as', bak2)
print('Done')
