#!/usr/bin/env python3
import json
import sys
from datetime import datetime
from copy import deepcopy

# Usage: python3 scripts/normalize_nodes_cluster.py [path/to/nodes.file]

PATH = sys.argv[1] if len(sys.argv) > 1 else 'data/Nodes/nodes.English_Reformation.json'
BACKUP = PATH + '.bak'

# Whitelist of allowed fields derived from the attribute registry
WHITELIST = {
    'id', 'label', 'slug', 'name', 'alt_names', 'aliases', 'definition', 'description',
    'category', 'class_number', 'division_code', 'call_number', 'subject_headings',
    'is_generic', 'status', 'intl_status', 'created_at', 'updated_at', 'created_by',
    'modified_by', 'status_by', 'version', 'corpus', 'lang', 'script',
    'startYear', 'endYear', 'chron_key', 'context', 'confidence_score',
    'birthYear', 'deathYear', 'titles', 'summary', 'significance', 'score', 'tags',
    'kind', 'region', 'wikidata_qid', 'importance_score', 'citation_count', 'review_status',
    'cultural_context', 'midYear', 'duration', 'geo', 'geo.lat', 'geo.lon', 'geo_precision',
    'license', 'workflow_stage', 'governance_version', 'display_label', 'era_ref',
    'has_geo', 'has_text', 'subject_headings'
}

# Labels for which we prefer a concise 'definition' (per registry guidance)
DEFINITION_PREFERRED_LABELS = {'Idea', 'Institution', 'Movement', 'Framework'}

now = datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'

with open(PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

orig = deepcopy(data)

nodes = data.get('nodes', [])
new_nodes = []

for n in nodes:
    new = {}
    # preserve id/label/slug/name where present
    for k in ('id', 'label', 'slug', 'name'):
        if k in n:
            new[k] = n[k]
    # copy whitelisted fields
    for k, v in n.items():
        if k in WHITELIST:
            new[k] = v
        # preserve nested geo object entirely if present
        elif k == 'geo' and isinstance(v, dict):
            new['geo'] = v
    # ensure status/workflow defaults
    if 'status' not in new:
        new['status'] = 'PROPOSED'
    if 'workflow_stage' not in new:
        new['workflow_stage'] = new.get('status')
    # governance/version defaults
    if 'version' not in new:
        new['version'] = 4
    if 'governance_version' not in new:
        new['governance_version'] = 5
    # provenance defaults
    if 'created_by' not in new:
        new['created_by'] = 'auto_import'
    if 'modified_by' not in new:
        new['modified_by'] = 'auto_import'
    if 'status_by' not in new:
        new['status_by'] = new.get('created_by')
    if 'created_at' not in new:
        new['created_at'] = now
    if 'updated_at' not in new:
        new['updated_at'] = now
    # copy summary -> description if description missing
    if 'description' not in new:
        if 'definition' in new and new.get('label') in ('Person','Place','Event','Artifact','Evidence'):
            # For those, prefer description; if only definition exists, copy it
            new['description'] = new['definition']
        elif 'summary' in new:
            new['description'] = new['summary']
        elif 'definition' in new and new.get('label') not in DEFINITION_PREFERRED_LABELS:
            new['description'] = new['definition']
    # ensure definition exists for label types that prefer definition
    if new.get('label') in DEFINITION_PREFERRED_LABELS and 'definition' not in new:
        if 'description' in new:
            # take the first sentence or whole description truncated
            new['definition'] = new['description'][:160]
        elif 'summary' in new:
            new['definition'] = new['summary'][:160]
    # compute midYear and duration from startYear/endYear if present
    try:
        sy = int(new['startYear']) if 'startYear' in new and isinstance(new['startYear'], (int, float, str)) else None
        ey = int(new['endYear']) if 'endYear' in new and isinstance(new['endYear'], (int, float, str)) else None
    except Exception:
        sy = ey = None
    if sy is not None and ey is not None:
        new['midYear'] = (sy + ey) // 2
        try:
            new['duration'] = ey - sy
        except Exception:
            pass
    # compute has_geo
    has_geo = False
    if 'geo' in new and isinstance(new['geo'], dict):
        lat = new['geo'].get('lat') or new['geo'].get('latitude')
        lon = new['geo'].get('lon') or new['geo'].get('longitude')
        if lat is not None or lon is not None:
            has_geo = True
    # also check top-level geo lat/lon if present
    if any(k in new for k in ('geo.lat','geo.lon')):
        has_geo = True
    new['has_geo'] = has_geo
    # derive has_text from lang/script presence
    new['has_text'] = bool(new.get('lang') or new.get('script'))
    # ensure tags is a list if present
    if 'tags' in new and new['tags'] is None:
        new['tags'] = []
    # finally, remove any keys not in whitelist plus the allowed top-level keys we created
    final = {}
    for k, v in new.items():
        # allow geo dict and any whitelisted entries
        if k == 'geo' or k in WHITELIST:
            final[k] = v
        # allow id/label even if not in WHITELIST
        elif k in ('id','label'):
            final[k] = v
    # keep order: id, label, slug, name, then rest
    ordered = {}
    for key in ('id','label','slug','name'):
        if key in final:
            ordered[key] = final[key]
    for key in sorted(final.keys()):
        if key not in ordered:
            ordered[key] = final[key]
    new_nodes.append(ordered)

# backup original
with open(BACKUP, 'w', encoding='utf-8') as f:
    json.dump(orig, f, indent=2, ensure_ascii=False)

# write normalized
out = {'_meta': data.get('_meta', {}), 'nodes': new_nodes}
with open(PATH, 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print('Wrote normalized file:', PATH)
print('Backup saved to:', BACKUP)
print('Original nodes:', len(nodes), '-> Normalized nodes:', len(new_nodes))
