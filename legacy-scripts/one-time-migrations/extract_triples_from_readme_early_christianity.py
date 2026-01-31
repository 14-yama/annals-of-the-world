#!/usr/bin/env python3
"""Extract canonical triples like `(Subject) VERB (Object)` from README.md
and write them to data/Relationships/relationships.Early_Christianity.json

This parser balances nested parentheses to correctly capture slugs like
`Synoptic_Traditions_(source_strata)`.
"""
import json
from pathlib import Path
import shutil
import datetime

README = Path('docs/clusters/Early_Christianity/README.md')
OUT = Path('data/Relationships/relationships.Early_Christianity.json')

if not README.exists():
    print('README missing:', README)
    raise SystemExit(1)

text = README.read_text(encoding='utf-8')
lines = text.splitlines()

# helper to find balanced parenthesis content starting at index of '('
def extract_paren(s, start):
    assert s[start] == '('
    depth = 0
    i = start
    n = len(s)
    while i < n:
        if s[i] == '(':
            depth += 1
        elif s[i] == ')':
            depth -= 1
            if depth == 0:
                return s[start+1:i], i
        i += 1
    return None, -1

triples = []
for lineno, line in enumerate(lines, start=1):
    pos = 0
    L = len(line)
    while True:
        try:
            p = line.index('(', pos)
        except ValueError:
            break
        subj, endp = extract_paren(line, p)
        if endp == -1:
            break
        # Move after subject
        i = endp + 1
        # skip spaces
        while i < L and line[i].isspace():
            i += 1
        # collect verb token (letters, underscores, hyphens)
        verb_start = i
        while i < L and (line[i].isalpha() or line[i] == '_' or line[i] == '-' or line[i].isdigit()):
            i += 1
        verb = line[verb_start:i].strip()
        if not verb:
            pos = endp + 1
            continue
        # skip spaces
        while i < L and line[i].isspace():
            i += 1
        # next should be '('
        if i < L and line[i] == '(':
            obj, obj_end = extract_paren(line, i)
            if obj_end == -1:
                pos = i + 1
                continue
            triples.append({'line': lineno, 'subject': subj.strip(), 'verb': verb.strip().upper(), 'object': obj.strip(), 'raw': line.strip()})
            pos = obj_end + 1
        else:
            # Not a triple, move on
            pos = endp + 1

# Also handle lines that have triples not wrapped as (S) VERB (O) but like '(Paul) LEADS (Pauline_Mission_Journeys)' we've already captured.

# remove duplicates preserving order
seen = set()
unique = []
for t in triples:
    key = (t['verb'], t['subject'], t['object'])
    if key in seen:
        continue
    seen.add(key)
    unique.append(t)

# Build relationships list
rels = []
for i, t in enumerate(unique, start=1):
    rel = {
        'id': i,
        'start_slug': t['subject'],
        'end_slug': t['object'],
        'type': t['verb'],
        'description': f"{t['subject']} {t['verb']} {t['object']}",
        'status': 'PROPOSED',
        'evidence_url': None,
        'citation_style': None,
        'page_refs': None,
        'source_note': f"auto:extracted_from_readme_line_{t['line']}"
    }
    rels.append(rel)

# Merge with existing conservative relationships (like parent root/interfacing) to avoid losing them
if OUT.exists():
    existing = json.load(open(OUT,'r',encoding='utf-8'))
    exist_rels = existing.get('relationships', [])
    # start ids after existing count
    base = len(rels)
    # We'll append existing ones not already present
    for er in exist_rels:
        k = (er.get('type','').upper(), er.get('start_slug') or '', er.get('end_slug') or '')
        # check if present
        if k in seen:
            continue
        base += 1
        new = er.copy()
        new['id'] = base
        rels.append(new)
        seen.add(k)

# backup
bak = OUT.with_suffix('.bak.' + datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ'))
if OUT.exists():
    shutil.copy2(OUT, bak)
    print('Backed up', OUT, '->', bak)

out = {
    '_meta': {
        'cluster': 'Early_Christianity',
        'notes': 'All canonical triples extracted from README.md',
        'source': str(README)
    },
    'relationships': rels
}
OUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print('Extracted triples:', len(unique))
print('Wrote relationships:', len(rels))
print('Sample first 20:')
for r in rels[:20]:
    print('-', r['id'], r['start_slug'], r['type'], r['end_slug'])
