#!/usr/bin/env python3
"""Generate Text catalog entities from text references in hand-curated files.

Reads all hand-curated catalog .ts files, extracts unique text references
from each entity's `texts: [...]` arrays, and generates corresponding
Text entities with proper call numbers, summaries, and relationships.

Output: ui/src/data/catalog/textNodes.ts
"""

import re
import os
import json
from collections import defaultdict

BASE = os.path.join(os.path.dirname(__file__), '..', 'ui', 'src', 'data', 'catalog')
OUTPUT = os.path.join(BASE, 'textNodes.ts')

# ── Division mapping: text type → call number division ──────────────

TYPE_TO_DIVISION = {
    # 710 – Constitutions & Charters
    'Constitution': '710', 'Charter': '710', 'Legal document': '710',
    'Political declaration': '710', 'International declaration': '710',
    'Legal charter': '710', 'Imperial charter': '710', 'Founding charter': '710',
    # 720 – Legal Codes
    'Legal code': '720', 'Legal statute': '720', 'Legal opinion': '720',
    'Legal transcript': '720', 'Legal decree': '720', 'Royal decree': '720',
    'Imperial decree': '720', 'Imperial edict': '720', 'Papal decree': '720',
    'Papal bull': '720', 'Church decree': '720', 'Executive order': '720',
    'Doctrinal code': '720',
    # 730 – Religious Texts
    'Scripture': '730', 'Epistle': '730', 'Apocalyptic literature': '730',
    'Sermon': '730', 'Devotional manual': '730', 'Liturgical text': '730',
    'Confessional document': '730', 'Theological treatise': '730',
    'Church history': '730', 'Early church manual': '730',
    'Hadith collection': '730', 'Rabbinic text': '730',
    'Religious manuscripts': '730', 'Biblical manuscript': '730',
    'Funerary text': '730', 'Funerary inscriptions': '730',
    'Mythological text': '730',
    # 740 – Philosophical Works
    'Philosophical treatise': '740', 'Philosophical dialogue': '740',
    'Philosophical oration': '740', 'Philosophical essay': '740',
    'Philosophical fragments': '740', 'Philosophical fragment': '740',
    'Political treatise': '740', 'Political manifesto': '740',
    'Political fiction': '740', 'Political essays': '740',
    'Political writings': '740', 'Political testament': '740',
    'Treatise': '740', 'Economic treatise': '740',
    'Anthropological study': '740', 'Anthropological essay': '740',
    'Historical analysis': '740', 'Historical chronicle': '740',
    'Historical database': '740',
    'Biography': '740', 'Biographical memoir': '740',
    'Biographical compendium': '740', 'Autobiography': '740',
    'Memoir': '740', 'Personal diary': '740', 'Correspondence': '740',
    'Letter': '740', 'Collected writings': '740',
    'Social study': '740', 'Environmental study': '740',
    'Environmental essay': '740', 'Environmental treatise': '740',
    'Economic analysis': '740', 'Technology treatise': '740',
    'Administrative treatise': '740', 'Administrative compendium': '740',
    # 750 – Scientific Texts
    'Scientific treatise': '750', 'Scientific paper': '750',
    'Scientific lecture': '750', 'Scientific notebook': '750',
    'Mathematical treatise': '750', 'Medical treatise': '750',
    'Geographical compendium': '750', 'Engineering treatise': '750',
    'Doctoral thesis': '750', 'Science treatise': '750',
    'Statistical report': '750', 'Economic dataset': '750',
    'Genetic study': '750',
    # 760 – Artworks
    'Artwork': '760', 'Art treatise': '760', 'Epic poem': '760',
    'Literary work': '760', 'Novel': '760', 'Poetry collection': '760',
    'Chanson de geste': '760', 'Saga': '760', 'Ancient epic': '760',
    'Oral tradition transcription': '760',
    # 770 – Technological Artifacts
    'Archaeological report': '770', 'Archaeological catalogue': '770',
    'Archaeological record': '770', 'Archaeological survey': '770',
    'Excavation report': '770', 'Geological report': '770',
    'Technical specification': '770', 'Technical proposal': '770',
    'Technical report': '770', 'Printed book': '770',
    'Historical communication': '770', 'Cartographic record': '770',
    'Maya manuscript': '770',
    # Fallback mappings
    'Treaty': '710', 'International treaty': '710',
    'International agreement': '710',
    'Proclamation': '710', 'Manifesto': '710',
    'Speech': '740', 'Chronicle': '740',
    'Journalistic account': '740', 'Narrative non-fiction': '740',
    'Report': '750', 'Government report': '750',
    'Investigative report': '750',
    'Travel chronicle': '740', 'Voyage journal': '740',
    'Encyclopedia': '750',
    'Census record': '770', 'Inscription': '770',
    'Royal inscription': '770', 'Trilingual inscription': '770',
    'Imperial inscription': '770', 'Ancient text': '730',
    'Royal annals': '740', 'Ancient chronicle': '740',
    'Military treatise': '740', 'Military chronicle': '740',
    'Diplomatic dispatch': '740',
    'Essay': '740',
    'Philosophical encyclopedia': '740',
}

# ── Era detection from text context ──────────────

ERA_MAP = {
    'prehistoric': ('Prehistoric', 'prehistoric'),
    'classical': ('Classical', 'classical'),
    'medieval': ('Medieval', 'medieval'),
    'earlyModern': ('Early Modern', 'early-modern'),
    'modern': ('Modern', 'modern'),
    'contemporary': ('Contemporary', 'contemporary'),
    'biblical': ('Classical', 'classical'),
    'reformation': ('Early Modern', 'early-modern'),
    'divisionEnrichment': ('Classical', 'classical'),  # fallback
}

# ── Framework detection based on text type ──────────────

def infer_frameworks(text_type: str) -> list[str]:
    div = TYPE_TO_DIVISION.get(text_type, '740')
    fws = ['TEXTUAL_TRANSMISSION']
    if div == '710':
        fws.append('LEGAL_INTERPRETATION')
    elif div == '720':
        fws.append('LEGAL_INTERPRETATION')
    elif div == '730':
        fws.extend(['DOCTRINE_DEVELOPMENT', 'RITUAL_STANDARDIZATION'])
    elif div == '740':
        fws.append('CULTURAL_DIFFUSION')
    elif div == '750':
        fws.append('INNOVATION_AND_TECHNOLOGY')
    elif div == '760':
        fws.append('CULTURAL_DIFFUSION')
    elif div == '770':
        fws.append('INNOVATION_AND_TECHNOLOGY')
    return fws


def slugify(title: str) -> str:
    """Convert a title to a slug."""
    s = title.lower()
    s = re.sub(r'[^a-z0-9\s]', '', s)
    s = re.sub(r'\s+', '_', s.strip())
    return s[:60]


def ts_str(s: str) -> str:
    """Wrap a value in single-quoted TS string with proper escaping."""
    return f"'{escape_ts(s)}'"


def escape_ts(s: str) -> str:
    if not s:
        return ''
    return str(s).replace('\\', '\\\\').replace("'", "\\'").replace('\u2018', "\\'").replace('\u2019', "\\'").replace('\u201c', '\\"').replace('\u201d', '\\"').replace('\n', ' ').replace('\r', '')


def extract_texts_from_file(filepath: str, source_key: str):
    """Parse a TS file and extract all text references with their parent entity context."""
    with open(filepath) as f:
        content = f.read()

    texts_found = []

    # Split into entity blocks by `  {` patterns (top-level array entries)
    blocks = re.split(r'\n  \{', content)

    for block in blocks[1:]:
        # Get entity slug, name, era info
        slug_m = re.search(r"slug:\s*'([^']+)'", block)
        name_m = re.search(r"name:\s*'([^']*(?:\\'[^']*)*)'", block)
        continent_m = re.search(r"continent:\s*'([^']+)'", block)
        region_m = re.search(r"region:\s*'([^']+)'", block)

        parent_slug = slug_m.group(1) if slug_m else ''
        parent_name = name_m.group(1).replace("\\'", "'") if name_m else ''
        continent = continent_m.group(1) if continent_m else 'Global'
        region = region_m.group(1) if region_m else 'Global'

        # Find texts array content
        texts_m = re.search(r'texts:\s*\[(.*?)\]', block, re.DOTALL)
        if not texts_m:
            continue
        texts_content = texts_m.group(1).strip()
        if not texts_content:
            continue

        # Parse individual text entries
        for entry_m in re.finditer(
            r"\{\s*title:\s*'((?:[^'\\]|\\.)*)'\s*,\s*type:\s*'((?:[^'\\]|\\.)*)'"
            r"(?:\s*,\s*year:\s*'([^']*)')?"
            r"(?:\s*,\s*slug:\s*'([^']*)')?\s*\}",
            texts_content
        ):
            title = entry_m.group(1).replace("\\'", "'")
            text_type = entry_m.group(2).replace("\\'", "'")
            year = entry_m.group(3) or ''
            text_slug = entry_m.group(4) or ''

            texts_found.append({
                'title': title,
                'type': text_type,
                'year': year,
                'slug': text_slug,
                'parent_slug': parent_slug,
                'parent_name': parent_name,
                'continent': continent,
                'region': region,
                'source_key': source_key,
            })

    return texts_found


def main():
    files = {
        'prehistoric': 'prehistoric.ts',
        'classical': 'classical.ts',
        'medieval': 'medieval.ts',
        'earlyModern': 'earlyModern.ts',
        'modern': 'modern.ts',
        'contemporary': 'contemporary.ts',
        'biblical': 'biblical.ts',
        'reformation': 'reformation.ts',
        'divisionEnrichment': 'divisionEnrichment.ts',
    }

    all_texts = []
    for key, fname in files.items():
        fpath = os.path.join(BASE, fname)
        if os.path.exists(fpath):
            texts = extract_texts_from_file(fpath, key)
            print(f"  {fname}: {len(texts)} text references")
            all_texts.extend(texts)

    print(f"\nTotal text references: {len(all_texts)}")

    # Deduplicate by title (first occurrence wins)
    seen_titles = set()
    unique_texts = []
    for t in all_texts:
        norm = t['title'].lower().strip()
        if norm not in seen_titles:
            seen_titles.add(norm)
            unique_texts.append(t)

    print(f"Unique texts: {len(unique_texts)}")

    # Build entities
    division_counters: dict[str, int] = defaultdict(int)
    entities = []

    for t in unique_texts:
        title = t['title']
        text_type = t['type']
        year = t['year']
        parent_slug = t['parent_slug']
        parent_name = t['parent_name']
        source_key = t['source_key']
        continent = t['continent']
        region = t['region']

        # Generate slug
        slug = t['slug'] if t['slug'] else slugify(title)
        if not slug:
            continue

        # Call number
        div = TYPE_TO_DIVISION.get(text_type, '740')
        division_counters[div] += 1
        call_number = f"{div}.{division_counters[div]:02d}-{slug.replace('_', '-')[:40]}"

        # Era
        era_name, era_slug = ERA_MAP.get(source_key, ('Classical', 'classical'))

        # Subject heading
        div_names = {
            '710': 'Constitutions & Charters',
            '720': 'Legal Codes',
            '730': 'Religious Texts',
            '740': 'Philosophical Works',
            '750': 'Scientific Texts',
            '760': 'Artworks',
            '770': 'Technological Artifacts',
        }
        div_heading = div_names.get(div, 'Texts')
        subject_heading = f"Artifacts & Texts — {div_heading} — {era_name}"

        # Summary
        year_str = f" ({year})" if year else ""
        summary = f"{title}{year_str} is a {text_type.lower()} "
        if parent_name:
            summary += f"associated with {parent_name}."
        else:
            summary += f"from the {era_name} era."

        # Frameworks
        frameworks = infer_frameworks(text_type)

        # Subjects
        subjects = [text_type, era_name]
        if continent != 'Global':
            subjects.append(continent)

        # Relationships
        rels = []
        if parent_slug:
            rels.append({
                'sourceSlug': slug,
                'sourceName': title,
                'verb': 'DEFINES',
                'targetSlug': parent_slug,
                'targetName': parent_name,
                'context': f'Text associated with {parent_name}',
            })

        # Period
        period = year if year else ''

        entities.append({
            'slug': slug,
            'name': title,
            'label': 'Text',
            'callNumber': call_number,
            'subjectHeadings': [subject_heading],
            'subjects': subjects,
            'summary': summary,
            'period': period,
            'era': era_name,
            'eraSlug': era_slug,
            'region': region,
            'continent': continent,
            'status': 'Published',
            'frameworks': frameworks,
            'causes': [],
            'effects': [],
            'relationships': rels,
            'places': [],
            'texts': [],
        })

    print(f"Generated {len(entities)} Text entities")

    # Division breakdown
    div_counts = defaultdict(int)
    for e in entities:
        cn = e['callNumber'][:3]
        div_counts[cn] += 1
    for d in sorted(div_counts):
        print(f"  {d}: {div_counts[d]}")

    # Write output
    lines = [
        "import type { Entity } from '../entityTypes'",
        "",
        "/**",
        " * Auto-generated Text entities from hand-curated actor text references.",
        f" * Generated: {len(entities)} unique Text nodes across 7xx call numbers.",
        " * Source: scripts/generate_text_entities.py",
        " */",
        f"export const TEXT_NODE_ENTITIES: Entity[] = [",
    ]

    for e in entities:
        sp = '  '
        parts = [
            f"  {{",
            f"  {sp}slug: '{escape_ts(e['slug'])}',",
            f"  {sp}name: '{escape_ts(e['name'])}',",
            f"  {sp}label: 'Text',",
            f"  {sp}callNumber: '{escape_ts(e['callNumber'])}',",
            f"  {sp}subjectHeadings: [{', '.join(ts_str(s) for s in e['subjectHeadings'])}],",
            f"  {sp}subjects: [{', '.join(ts_str(s) for s in e['subjects'])}],",
            f"  {sp}summary: '{escape_ts(e['summary'])}',",
        ]
        if e['period']:
            parts.append(f"  {sp}period: '{escape_ts(e['period'])}',")
        parts.extend([
            f"  {sp}era: '{escape_ts(e['era'])}',",
            f"  {sp}eraSlug: '{escape_ts(e['eraSlug'])}',",
            f"  {sp}region: '{escape_ts(e['region'])}',",
            f"  {sp}continent: '{escape_ts(e['continent'])}',",
            f"  {sp}status: 'Published',",
            f"  {sp}frameworks: [{', '.join(ts_str(f) for f in e['frameworks'])}],",
            f"  {sp}causes: [],",
            f"  {sp}effects: [],",
        ])

        # Relationships
        if e['relationships']:
            rel_items = []
            for r in e['relationships']:
                rel_items.append(
                    f"{{ sourceSlug: '{escape_ts(r['sourceSlug'])}', "
                    f"sourceName: '{escape_ts(r['sourceName'])}', "
                    f"verb: '{escape_ts(r['verb'])}', "
                    f"targetSlug: '{escape_ts(r['targetSlug'])}', "
                    f"targetName: '{escape_ts(r['targetName'])}', "
                    f"context: '{escape_ts(r['context'])}' }}"
                )
            parts.append(f"  {sp}relationships: [{', '.join(rel_items)}],")
        else:
            parts.append(f"  {sp}relationships: [],")

        parts.extend([
            f"  {sp}places: [],",
            f"  {sp}texts: [],",
            f"  }},",
        ])
        lines.append('\n'.join(parts))

    lines.append(']')
    lines.append('')

    # Write output
    ts_content = '\n'.join(lines)

    with open(OUTPUT, 'w') as f:
        f.write(ts_content)
        f.write('\n')

    print(f"\nWritten to {OUTPUT}")


if __name__ == '__main__':
    main()
