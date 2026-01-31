#!/usr/bin/env python3
"""Auto-generate conservative relationships and build an orphan triage report.

Behavior:
- Loads nodes from data/Nodes/nodes.*.json and relationships from data/Relationships/*.json
- Applies a small, conservative mapping of suggested relationships when both slugs exist.
- Appends new relationships to the English_Reformation relationships file (if not already present).
- Recomputes orphans and writes a Markdown report at data/orphan_report.md and updates data/orphan_nodes.csv.
"""
import json
import glob
import os
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(ROOT, 'data')
NODES_GLOB = os.path.join(DATA_DIR, 'Nodes', 'nodes.*.json')
REL_DIR = os.path.join(DATA_DIR, 'Relationships')
REL_FILE = os.path.join(REL_DIR, 'relationships.English_Reformation.json')
ORPHAN_CSV = os.path.join(DATA_DIR, 'orphan_nodes.csv')
ORPHAN_MD = os.path.join(DATA_DIR, 'orphan_report.md')

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def main():
    # load nodes
    node_files = sorted(glob.glob(NODES_GLOB))
    slug_index = {}  # slug -> (file, id)
    slug_to_obj = {}
    for nf in node_files:
        data = load_json(nf)
        for n in data.get('nodes', []):
            slug = n.get('slug')
            if not slug:
                continue
            slug_index[slug] = (nf, n.get('id'))
            slug_to_obj[slug] = n

    # load relationships (English only for appending)
    rels_data = load_json(REL_FILE)
    rels = rels_data.get('relationships', [])
    existing_pairs = set((r.get('start_slug'), r.get('end_slug'), r.get('type')) for r in rels)
    max_id = max((r.get('id') or 0) for r in rels) if rels else 0

    # conservative mapping: (start_slug, end_slug, type, description)
    mapping = [
        ("book_of_common_prayer_1552", "thomas_cranmer", "AUTHORED", "Thomas Cranmer authored the Book of Common Prayer (1552)"),
        ("bishops_bible_1568", "church_of_england", "AUTHORIZED_BY", "Bishops' Bible (1568) authorized by the Church of England"),
        ("book_of_homilies_1547", "church_of_england", "AUTHORIZED_BY", "Book of Homilies (1547) authorized by the Church of England"),
        ("book_of_homilies_1571", "church_of_england", "AUTHORIZED_BY", "Book of Homilies (1571) authorized by the Church of England"),
        ("society_of_jesus", "jesuit_mission_1580s", "ORGANIZES", "Society of Jesus organized Jesuit mission (1580s)"),
        ("society_of_jesus", "jesuit_mission_in_england", "ORGANIZES", "Society of Jesus organized Jesuit mission in England"),
        ("english_seminaries_douai_rheims", "douai", "OCCURS_IN", "English seminaries (Douai/Rheims) based at Douai"),
        ("execution_of_mary_queen_of_scots_1587", "mary_queen_of_scots", "INVOLVES", "Execution involves Mary, Queen of Scots")
    ]

    # Expanded conservative mapping: add more obvious, low-risk pairs.
    # These will only be appended when both slugs exist in the node files and
    # when the exact (start,end,type) triple is not already present.
    mapping += [
        ("william_tyndale", "english_bible_translation", "AUTHORED", "William Tyndale authored early English Bible translations"),
        ("william_tyndale", "english_bible_translation_movement", "AUTHORED", "William Tyndale authored or led efforts around English Bible translation"),
        ("miles_coverdale", "english_bible_translation", "ENDORSES", "Miles Coverdale endorses and edits English Bible translations"),
        ("miles_coverdale", "great_bible_1539", "EDITED", "Miles Coverdale contributed to the Great Bible (editorial role)"),
        ("john_foxe", "acts_and_monuments_1563", "AUTHORED", "John Foxe authored Acts and Monuments"),
        ("geneva_bible_1560", "english_bible_translation", "TRANSMITS", "Geneva Bible (1560) transmits English Bible translation variants"),
        ("book_of_common_prayer_1549", "thomas_cranmer", "AUTHORED", "Thomas Cranmer authored the Book of Common Prayer (1549)"),
        ("parish_bible_installations", "canterbury", "OCCURS_IN", "Parish Bible installations take place in Canterbury and other dioceses"),
        ("pilgrimage_of_grace_1536", "york", "OCCURS_IN", "Pilgrimage of Grace (1536) occurs in York"),
        ("annulment_proceedings", "rome", "OCCURS_IN", "Annulment proceedings involve diplomatic and curial processes in Rome"),
        ("act_of_supremacy_1534", "london", "OCCURS_IN", "Act of Supremacy (1534) associated with London")
    ]

    # Another small conservative batch: universities -> cities, events -> cities,
    # institutions -> cities, and canonical authorization links.
    mapping += [
        ("university_of_cambridge", "cambridge", "OCCURS_IN", "University of Cambridge is located in Cambridge"),
        ("university_of_oxford", "oxford", "OCCURS_IN", "University of Oxford is located in Oxford"),
        ("oxford_martyrs_1555_1556", "oxford", "OCCURS_IN", "Oxford Martyrs events occur in Oxford"),
        ("star_chamber", "london", "OCCURS_IN", "Star Chamber proceedings centered in London"),
        ("privy_council", "london", "OCCURS_IN", "Privy Council activities centered in London"),
        ("act_of_supremacy_1559", "london", "OCCURS_IN", "Act of Supremacy (1559) associated with London"),
        ("act_of_uniformity_1559", "london", "OCCURS_IN", "Act of Uniformity (1559) associated with London"),
        ("thirty_nine_articles_1563", "church_of_england", "AUTHORIZED_BY", "Thirty-Nine Articles (1563) authorized by the Church of England")
    ]

    added = []
    for start, end, typ, desc in mapping:
        if start in slug_index and end in slug_index:
            if (start, end, typ) in existing_pairs:
                continue
            max_id += 1
            newrel = {
                "id": max_id,
                "start_slug": start,
                "end_slug": end,
                "type": typ,
                "description": desc,
                "status": "PROPOSED",
                "evidence_url": None,
                "citation_style": None,
                "page_refs": None,
                "source_note": None
            }
            rels.append(newrel)
            existing_pairs.add((start, end, typ))
            added.append(newrel)

    if added:
        rels_data['relationships'] = rels
        save_json(REL_FILE, rels_data)

    # recompute orphans
    referenced = set()
    # read all relationships files for references
    for rf in sorted(glob.glob(os.path.join(REL_DIR, 'relationships.*.json'))):
        rd = load_json(rf)
        for r in rd.get('relationships', []):
            for fld in ('start_slug', 'end_slug'):
                v = r.get(fld)
                if v:
                    referenced.add(v)

    # build orphan grouping by cluster
    clusters = defaultdict(list)
    for slug, (nf, nid) in sorted(slug_index.items()):
        if slug not in referenced:
            # cluster name
            cluster = load_json(nf).get('_meta', {}).get('cluster') or os.path.basename(nf)
            suggested = ''
            # if mapping added for this slug, note it
            for rel in added:
                if rel['start_slug'] == slug or rel['end_slug'] == slug:
                    suggested = f"Added relationship: {rel['start_slug']} -[{rel['type']}]-> {rel['end_slug']}"
            clusters[cluster].append({'id': nid, 'slug': slug, 'file': os.path.relpath(nf, ROOT), 'suggested': suggested})

    # write orphan CSV
    import csv
    with open(ORPHAN_CSV, 'w', newline='', encoding='utf-8') as cf:
        w = csv.writer(cf)
        w.writerow(['cluster','file','id','slug','suggested_action'])
        for cluster, items in clusters.items():
            for it in items:
                w.writerow([cluster, it['file'], it['id'], it['slug'], it['suggested']])

    # write markdown report
    lines = []
    lines.append('# Orphan Nodes Triage Report')
    lines.append('Generated by scripts/autogen_relationships_and_report.py')
    lines.append('')
    if added:
        lines.append('## Auto-added conservative relationships')
        lines.append('')
        for r in added:
            lines.append(f"- id {r['id']}: `{r['start_slug']}` -[{r['type']}]-> `{r['end_slug']}` — {r['description']}")
        lines.append('')

    for cluster, items in sorted(clusters.items()):
        lines.append(f"## Cluster: {cluster} — orphan count: {len(items)}")
        lines.append('')
        lines.append('| id | slug | file | suggested_action |')
        lines.append('|---:|---|---|---|')
        for it in items:
            suggested = it['suggested'] or ''
            lines.append(f"| {it['id']} | `{it['slug']}` | {it['file']} | {suggested} |")
        lines.append('')

    with open(ORPHAN_MD, 'w', encoding='utf-8') as mf:
        mf.write('\n'.join(lines))

    print(f'Added {len(added)} relationships and wrote orphan report to {ORPHAN_MD} (CSV: {ORPHAN_CSV})')

if __name__ == '__main__':
    main()
