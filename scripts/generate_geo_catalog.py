#!/usr/bin/env python3
"""
Regenerate ui/src/data/catalog/geoRegistry.ts from geo-registry country index files.

Enhanced generation with:
  - Rich causes/effects between sequential entities in clusters
  - Relationships (OCCURS_IN country, intra-cluster links)
  - Framework detection from description keywords
  - Place annotations (country + context)
  - Hierarchical subject headings
  - Global slug deduplication (country suffix for collisions)
  - Fixed slug-like descriptions (fallback to sub_cluster/cluster text)

Usage:
    python3 scripts/generate_geo_catalog.py
"""
import json
import os
import re
import sys
from collections import Counter, defaultdict

BASE = os.path.join(os.path.dirname(__file__), '..', 'geo-registry', 'places', 'countries')
OUTPUT = os.path.join(os.path.dirname(__file__), '..', 'ui', 'src', 'data', 'catalog', 'geoRegistry.ts')

ERA_MAP = {
    '910': {'era': 'Prehistoric', 'eraSlug': 'prehistoric'},
    '920': {'era': 'Classical', 'eraSlug': 'classical'},
    '930': {'era': 'Medieval', 'eraSlug': 'medieval'},
    '940': {'era': 'Early Modern', 'eraSlug': 'early-modern'},
    '950': {'era': 'Modern', 'eraSlug': 'modern'},
    '960': {'era': 'Contemporary', 'eraSlug': 'contemporary'},
}

DEFAULT_REGIONS = {
    'Africa': 'Sub-Saharan Africa',
    'Asia': 'East Asia',
    'Europe': 'Western Europe',
    'Americas': 'Latin America',
    'Oceania': 'Pacific Islands',
}

LABEL_MAP = {
    'Person': 'Person',
    'Institution': 'Institution',
    'EventWindow': 'EventWindow',
    'Text': 'Text',
    'Idea': 'Idea',
    'Movement': 'Movement',
}

# ── Framework detection keywords ──────────────────────────────────────────────
FRAMEWORK_KEYWORDS = {
    'CONFLICT_AND_RESOLUTION': [
        'war', 'battle', 'conflict', 'invasion', 'conquest', 'siege', 'rebellion',
        'revolt', 'uprising', 'resistance', 'military', 'army', 'coup', 'genocide',
        'massacre', 'crusade', 'jihad', 'civil war', 'guerrilla',
    ],
    'ECONOMIC_SYSTEMS': [
        'trade', 'economy', 'commerce', 'merchant', 'tariff', 'gold', 'currency',
        'industry', 'manufacture', 'labor', 'plantation', 'mining', 'spice',
        'silk', 'ivory', 'slave trade', 'caravan', 'market', 'export',
    ],
    'COMPARATIVE_RELIGION': [
        'religion', 'church', 'mosque', 'temple', 'faith', 'christian', 'muslim',
        'islam', 'buddhist', 'hindu', 'jewish', 'spiritual', 'missionary',
        'doctrine', 'clergy', 'bible', 'quran', 'monastery', 'reformation',
        'shinto', 'confucian', 'animist', 'pagan',
    ],
    'CULTURAL_DIFFUSION': [
        'migration', 'spread', 'diaspora', 'diffusion', 'cultural exchange',
        'assimilation', 'language', 'writing system', 'alphabet', 'bantu',
    ],
    'POLITICAL_SYSTEMS': [
        'government', 'law', 'constitution', 'parliament', 'democracy',
        'republic', 'monarchy', 'sultan', 'sovereignty', 'colonial',
        'independence', 'federation', 'administration', 'election', 'vote',
    ],
    'INNOVATION_AND_TECHNOLOGY': [
        'technology', 'invention', 'science', 'engineering', 'tool',
        'discovery', 'innovation', 'irrigation', 'printing', 'telegraph',
        'railroad', 'steam', 'nuclear',
    ],
    'EMPIRE_AND_COLONIALISM': [
        'empire', 'colonial', 'imperialism', 'partition', 'protectorate',
        'mandate', 'dominion', 'occupation', 'decolonization', 'scramble',
    ],
    'ENVIRONMENTAL_HISTORY': [
        'environment', 'climate', 'ecology', 'drought', 'flood', 'famine',
        'agriculture', 'pastoral', 'nomadic', 'fishing', 'deforestation',
    ],
}

# ── Relationship verbs by label ───────────────────────────────────────────────
VERB_BY_LABEL = {
    'Person': 'INFLUENCES',
    'Institution': 'DEFINES',
    'EventWindow': 'CAUSES',
    'Text': 'TRANSMITS',
    'Movement': 'TRANSFORMS',
    'Idea': 'FRAMES',
}


# ═══════════════════════════════════════════════════════════════════════════════
# Utility functions
# ═══════════════════════════════════════════════════════════════════════════════

def slugify(text):
    s = re.sub(r'[^\w\s-]', '', text.lower().strip())
    s = re.sub(r'[\s_]+', '-', s)
    s = re.sub(r'-+', '-', s)
    return s.strip('-')[:80]


def escape_ts(s):
    """Escape a string for TypeScript single-quoted literal."""
    if not s:
        return ''
    return str(s).replace('\\', '\\\\').replace("'", "\\'").replace('\n', ' ').replace('\r', '')


def ts_str(s):
    """Wrap escaped string in single quotes for TS output."""
    return f"'{escape_ts(s)}'"


def format_year(year):
    if year is None:
        return ''
    if isinstance(year, (int, float)):
        y = int(year)
        return f'{abs(y)} BCE' if y < 0 else str(y)
    return str(year)


def get_year_start(yr):
    """Extract start year from year_range for sorting."""
    if isinstance(yr, list) and yr:
        v = yr[0]
        return v if v is not None else 0
    return 0


def looks_like_slug(text):
    """True if text looks like a raw slug/key_event name rather than a description."""
    if not text:
        return True
    text = text.strip()
    if '_' in text and ' ' not in text:
        return True
    if len(text) < 20 and text.replace('-', '').replace('_', '').replace(' ', '').isalpha():
        return True
    return False


def detect_frameworks(text):
    """Detect up to 3 applicable interpretation frameworks from text."""
    text_lower = text.lower()
    found = []
    for framework, keywords in FRAMEWORK_KEYWORDS.items():
        if any(kw in text_lower for kw in keywords):
            found.append(framework)
    if 'CAUSE_AND_EFFECT' not in found and len(found) < 3:
        found.append('CAUSE_AND_EFFECT')
    return found[:3]


def build_subject_heading(label, country_name, era, cluster_name):
    """Build a hierarchical subject heading string."""
    cat = {
        'Person': 'People', 'Institution': 'Institutions',
        'EventWindow': 'Events', 'Text': 'Artifacts & Texts',
        'Idea': 'Ideas', 'Movement': 'Movements',
    }.get(label, 'Events')
    return f'{cat} \u2014 {cluster_name} \u2014 {country_name} \u2014 {era}'


def build_subjects(description, country_name, cluster_name):
    """Extract structured topic tags from description text."""
    subjects = [country_name]
    text = (description + ' ' + cluster_name).lower()
    topic_kws = {
        'Trade': ['trade', 'commerce', 'merchant', 'market'],
        'Warfare': ['war', 'battle', 'siege', 'military', 'army'],
        'Governance': ['government', 'parliament', 'constitution', 'law', 'election'],
        'Religion': ['religion', 'church', 'mosque', 'temple', 'faith'],
        'Science': ['science', 'technology', 'invention', 'discovery'],
        'Agriculture': ['agriculture', 'farming', 'pastoral', 'crop'],
        'Art & Culture': ['art', 'literature', 'music', 'poetry', 'architecture'],
        'Migration': ['migration', 'diaspora', 'exile', 'refugee'],
        'Colonialism': ['colonial', 'empire', 'imperialism', 'occupation'],
        'Independence': ['independence', 'liberation', 'sovereignty', 'self-rule'],
        'Education': ['university', 'school', 'education', 'scholar'],
    }
    for topic, kws in topic_kws.items():
        if any(kw in text for kw in kws):
            subjects.append(topic)
    return subjects[:5]


# ── Text extraction from description keywords ─────────────────────────────────
TEXT_PATTERNS = {
    'Constitution': [
        r'\bconstitution\b', r'\bcharter\b', r'\bbasic law\b', r'\bbill of rights\b',
    ],
    'Treaty': [
        r'\btreaty\b', r'\baccord\b', r'\bpact\b', r'\barmistice\b', r'\bconvention\b',
        r'\bagreement\b', r'\bconcordat\b',
    ],
    'Legal Code': [
        r'\bcode\b.*\blaw\b', r'\blegal code\b', r'\blaw code\b', r'\bdecree\b',
        r'\bedict\b', r'\blegislat\b',
    ],
    'Scripture': [
        r'\bscripture\b', r'\bbible\b', r'\bquran\b', r'\bvedas?\b', r'\bsutra\b',
        r'\btorah\b', r'\btalmud\b', r'\bcanon\b', r'\bgospel\b',
    ],
    'Chronicle': [
        r'\bchronicle\b', r'\bannals?\b', r'\bhistory of\b', r'\brecord\b',
    ],
    'Proclamation': [
        r'\bproclamation\b', r'\bdeclaration\b', r'\bmanifesto\b', r'\bspeech\b',
    ],
    'Inscription': [
        r'\binscription\b', r'\bstele?\b', r'\bepigraph\b', r'\btablet\b',
        r'\bhieroglyph\b', r'\bcuneiform\b',
    ],
    'Literary Work': [
        r'\bepic\b', r'\bpoem\b', r'\bpoetry\b', r'\bliterature\b', r'\bnovel\b',
        r'\bmanuscript\b', r'\btext\b',
    ],
    'Scientific Work': [
        r'\bscientific\b', r'\btreatise\b', r'\bjournal\b', r'\btheory of\b',
        r'\bdiscovery of\b',
    ],
    'Map or Atlas': [
        r'\bmap\b', r'\batlas\b', r'\bcartograph\b', r'\bnavigation chart\b',
    ],
}

# Specific named documents mentioned frequently in historical descriptions
NAMED_TEXTS = {
    'magna carta': {'title': 'Magna Carta (1215)', 'type': 'Charter'},
    'code of hammurabi': {'title': 'Code of Hammurabi', 'type': 'Legal Code'},
    'rosetta stone': {'title': 'Rosetta Stone', 'type': 'Inscription'},
    'dead sea scrolls': {'title': 'Dead Sea Scrolls', 'type': 'Scripture'},
    'book of the dead': {'title': 'Book of the Dead', 'type': 'Scripture'},
    'wealth of nations': {'title': 'The Wealth of Nations (1776)', 'type': 'Treatise'},
    'communist manifesto': {'title': 'Communist Manifesto (1848)', 'type': 'Manifesto'},
    'un charter': {'title': 'UN Charter (1945)', 'type': 'Charter'},
    'universal declaration': {'title': 'Universal Declaration of Human Rights (1948)', 'type': 'Declaration'},
    'berlin conference': {'title': 'Berlin Conference Act (1885)', 'type': 'Treaty'},
    'treaty of versailles': {'title': 'Treaty of Versailles (1919)', 'type': 'Treaty'},
    'treaty of tordesillas': {'title': 'Treaty of Tordesillas (1494)', 'type': 'Treaty'},
    'treaty of westphalia': {'title': 'Treaty of Westphalia (1648)', 'type': 'Treaty'},
    'ninety-five theses': {'title': 'Ninety-Five Theses (1517)', 'type': 'Proclamation'},
    'emancipation proclamation': {'title': 'Emancipation Proclamation (1863)', 'type': 'Proclamation'},
    'balfour declaration': {'title': 'Balfour Declaration (1917)', 'type': 'Proclamation'},
    'atlantic charter': {'title': 'Atlantic Charter (1941)', 'type': 'Charter'},
    'geneva convention': {'title': 'Geneva Conventions', 'type': 'Treaty'},
    'kellogg-briand': {'title': 'Kellogg-Briand Pact (1928)', 'type': 'Treaty'},
}


def extract_texts_from_description(description, cluster_desc=''):
    """Extract text/document references from description keywords."""
    combined = f'{description} {cluster_desc}'.lower()
    texts = []
    seen_titles = set()

    # Check for specific named texts
    for key, doc in NAMED_TEXTS.items():
        if key in combined and doc['title'] not in seen_titles:
            texts.append(doc)
            seen_titles.add(doc['title'])

    # Pattern-based extraction
    for text_type, patterns in TEXT_PATTERNS.items():
        if text_type in seen_titles:
            continue
        for pat in patterns:
            m = re.search(pat, combined, re.IGNORECASE)
            if m:
                # Try to extract a meaningful title from context
                # Find the sentence containing the match
                start = max(0, combined.rfind('.', 0, m.start()) + 1)
                end = combined.find('.', m.end())
                if end == -1:
                    end = min(len(combined), m.end() + 80)
                snippet = combined[start:end].strip()
                if len(snippet) > 10 and len(snippet) < 120:
                    title = snippet[:80].strip().title()
                    # Strip leading/trailing quotes and special chars
                    title = title.strip("'\"\\")
                    if title and title not in seen_titles:
                        texts.append({'title': title, 'type': text_type})
                        seen_titles.add(title)
                break  # One match per type

    return texts[:4]  # Cap at 4 texts per entity


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 1: Entity Extraction
# ═══════════════════════════════════════════════════════════════════════════════

def extract_entities(country_slug):
    """Extract entities from a country index.json with metadata for enrichment."""
    fp = os.path.join(BASE, country_slug, 'index.json')
    if not os.path.isfile(fp):
        return []

    with open(fp, 'r', encoding='utf-8') as f:
        data = json.load(f)

    meta = data.get('_meta', {})
    country_name = meta.get('country_name', country_slug.replace('-', ' ').title())
    continent = meta.get('continent', '')
    region = meta.get('region', DEFAULT_REGIONS.get(continent, ''))

    entities = []
    seen_slugs = set()
    call_counter = [0]

    def next_seq():
        call_counter[0] += 1
        return f'{call_counter[0]:02d}'

    # ── Thematic cluster nodes ──
    tc = data.get('thematic_clusters', {})
    for era_code in sorted(tc.keys()):
        era_info = ERA_MAP.get(era_code, {'era': 'Unknown', 'eraSlug': 'unknown'})
        clusters = tc[era_code]
        for cluster in clusters:
            cluster_name = cluster.get('name', '')
            cluster_desc = cluster.get('description', '')
            cluster_slug = cluster.get('slug', '')

            for sc in cluster.get('sub_clusters', []):
                sc_desc = sc.get('description', '')
                sc_name = sc.get('name', '')
                sc_yr = sc.get('year_range', [0, 0])

                for node in sc.get('nodes', []):
                    slug = node.get('slug', '')
                    if not slug or slug in seen_slugs:
                        continue
                    seen_slugs.add(slug)

                    label = LABEL_MAP.get(node.get('label', 'EventWindow'), 'EventWindow')
                    # Assign call number based on label type (not all 530)
                    _label_div = {
                        'EventWindow': '530', 'Institution': '310', 'Person': '220',
                        'Movement': '610', 'Text': '710', 'Idea': '010',
                        'Evidence': '810', 'Place': '440', 'Timeframe': '910',
                    }
                    default_div = _label_div.get(label, '530')
                    cn = node.get('call_number', f'{default_div}.{slug[:60]}')
                    yr = node.get('year_range', sc_yr)
                    start_date = format_year(yr[0]) if yr and len(yr) > 0 else ''
                    end_date = format_year(yr[1]) if yr and len(yr) > 1 else ''
                    period = f'{start_date}\u2013{end_date}' if start_date and end_date else start_date or end_date

                    # Fix slug-like descriptions
                    desc = node.get('description', '')
                    if looks_like_slug(desc):
                        desc = sc_desc or cluster_desc or f'{node.get("name", "")} in {country_name}'

                    # Rich metadata
                    context_text = f'{desc} {sc_desc} {cluster_desc}'
                    sh = build_subject_heading(label, country_name, era_info['era'], cluster_name)
                    subjects = build_subjects(context_text, country_name, cluster_name)
                    frameworks = detect_frameworks(context_text)

                    entity = {
                        'slug': slug,
                        'name': node.get('name', slug.replace('-', ' ').title()),
                        'label': label,
                        'callNumber': cn,
                        'subjectHeadings': [sh],
                        'subjects': subjects,
                        'summary': desc.strip(),
                        'startDate': start_date,
                        'endDate': end_date,
                        'period': period,
                        'era': era_info['era'],
                        'eraSlug': era_info['eraSlug'],
                        'region': region,
                        'continent': continent,
                        'status': node.get('status', 'PLANNED'),
                        'frameworks': frameworks,
                        'causes': [],
                        'effects': [],
                        'relationships': [],
                        'places': [{'name': country_name, 'role': 'National History'}],
                        'texts': extract_texts_from_description(desc, sc_desc),
                        # Internal metadata (stripped before output)
                        '_country_slug': country_slug,
                        '_country_name': country_name,
                        '_cluster_key': f'{era_code}:{cluster_slug}',
                        '_cluster_name': cluster_name,
                        '_year_range': yr,
                    }
                    entities.append(entity)

    # ── Leaders as Person entities ──
    leadership = data.get('leadership', {})
    former = leadership.get('former_leaders', [])
    current = leadership.get('current_leader', {})
    all_leaders = list(former)
    if current and current.get('name'):
        all_leaders.append(current)

    for leader in all_leaders:
        name = leader.get('name', '')
        if not name:
            continue
        slug = slugify(name)
        if not slug or slug in seen_slugs:
            continue
        seen_slugs.add(slug)

        term = leader.get('term', leader.get('since', ''))
        notes = leader.get('notes', '')
        desc = (f'Leader of {country_name} ({term}). {notes[:200]}'.strip()
                if notes
                else f'Leader of {country_name} ({term})')

        entity = {
            'slug': slug,
            'name': name,
            'label': 'Person',
            'callNumber': f'220.{next_seq()}-{slug[:40]}',
            'subjectHeadings': [f'People \u2014 Political Leaders \u2014 {country_name} \u2014 Contemporary'],
            'subjects': ['Political Leader', country_name, 'Governance'],
            'summary': desc,
            'period': term,
            'era': 'Contemporary',
            'eraSlug': 'contemporary',
            'region': region,
            'continent': continent,
            'status': 'PLANNED',
            'frameworks': ['POLITICAL_SYSTEMS', 'CAUSE_AND_EFFECT'],
            'causes': [],
            'effects': [],
            'relationships': [],
            'places': [{'name': country_name, 'role': 'Governance'}],
            'texts': [],
            '_country_slug': country_slug,
            '_country_name': country_name,
            '_cluster_key': f'960:leaders-{country_slug}',
            '_cluster_name': f'{country_name} Leadership',
            '_year_range': [1945, 2025],
        }
        entities.append(entity)

    return entities


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 2: Global Slug Deduplication
# ═══════════════════════════════════════════════════════════════════════════════

def make_slugs_unique(entities):
    """Ensure all slugs are globally unique by appending country suffix for collisions."""
    slug_count = Counter(e['slug'] for e in entities)
    duplicates = {s for s, c in slug_count.items() if c > 1}

    if not duplicates:
        return

    print(f'  Resolving {len(duplicates)} duplicate slug groups...')
    seen = {}
    for e in entities:
        slug = e['slug']
        if slug in duplicates:
            country = e.get('_country_slug', '')
            new_slug = f'{slug}-{country}' if country else slug
            # Handle edge case where the country-suffixed slug also collides
            if new_slug in seen:
                i = 2
                while f'{new_slug}-{i}' in seen:
                    i += 1
                new_slug = f'{new_slug}-{i}'
            e['slug'] = new_slug
            # Update call number to match
            parts = e['callNumber'].split('.')
            if len(parts) >= 2:
                prefix = parts[0]
                e['callNumber'] = f'{prefix}.{new_slug[:60]}'
        seen[e['slug']] = True


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 3: Enrichment — Causes, Effects, Relationships
# ═══════════════════════════════════════════════════════════════════════════════

def enrich_all(entities):
    """Generate causes, effects, and relationships from cluster structure."""
    by_country = defaultdict(list)
    for e in entities:
        by_country[e.get('_country_slug', '')].append(e)

    for country_slug, country_ents in by_country.items():
        country_name = country_ents[0].get('_country_name', '') if country_ents else ''

        # ── Intra-cluster causal chains ──
        by_cluster = defaultdict(list)
        for e in country_ents:
            by_cluster[e.get('_cluster_key', '')].append(e)

        for cluster_key, cluster_ents in by_cluster.items():
            cluster_ents.sort(key=lambda x: get_year_start(x.get('_year_range', [0])))
            cluster_name = cluster_ents[0].get('_cluster_name', '') if cluster_ents else ''

            for i, e in enumerate(cluster_ents):
                # Cause: previous node(s) in cluster
                if i > 0:
                    prev = cluster_ents[i - 1]
                    e['causes'].append({
                        'title': prev['name'],
                        'type': prev['label'],
                        'year': prev.get('startDate', ''),
                        'slug': prev['slug'],
                    })
                # Second cause (2 nodes back) for richer chains
                if i > 1:
                    prev2 = cluster_ents[i - 2]
                    e['causes'].append({
                        'title': prev2['name'],
                        'type': prev2['label'],
                        'year': prev2.get('startDate', ''),
                        'slug': prev2['slug'],
                    })

                # Effect: next node(s) in cluster
                if i < len(cluster_ents) - 1:
                    nxt = cluster_ents[i + 1]
                    e['effects'].append({
                        'title': nxt['name'],
                        'type': nxt['label'],
                        'year': nxt.get('startDate', ''),
                        'slug': nxt['slug'],
                    })
                if i < len(cluster_ents) - 2:
                    nxt2 = cluster_ents[i + 2]
                    e['effects'].append({
                        'title': nxt2['name'],
                        'type': nxt2['label'],
                        'year': nxt2.get('startDate', ''),
                        'slug': nxt2['slug'],
                    })

                # Relationship: OCCURS_IN country
                e['relationships'].append({
                    'sourceSlug': e['slug'],
                    'sourceName': e['name'],
                    'verb': 'OCCURS_IN',
                    'targetSlug': country_slug,
                    'targetName': country_name,
                    'context': f'{e["name"]} in the history of {country_name}',
                })

                # Relationship: to next node in cluster
                if i < len(cluster_ents) - 1:
                    nxt = cluster_ents[i + 1]
                    verb = VERB_BY_LABEL.get(e['label'], 'INFLUENCES')
                    e['relationships'].append({
                        'sourceSlug': e['slug'],
                        'sourceName': e['name'],
                        'verb': verb,
                        'targetSlug': nxt['slug'],
                        'targetName': nxt['name'],
                        'context': f'Sequential development within {cluster_name}',
                    })

        # ── Cross-era links ──
        by_era = defaultdict(list)
        for e in country_ents:
            by_era[e['eraSlug']].append(e)

        era_order = ['prehistoric', 'classical', 'medieval', 'early-modern', 'modern', 'contemporary']
        for i in range(len(era_order) - 1):
            prev_ents = by_era.get(era_order[i], [])
            next_ents = by_era.get(era_order[i + 1], [])
            if prev_ents and next_ents:
                last = prev_ents[-1]
                first = next_ents[0]
                # Avoid duplicate links
                existing_cause_slugs = {c.get('slug') for c in first.get('causes', []) if c.get('slug')}
                if last['slug'] not in existing_cause_slugs:
                    first['causes'].append({
                        'title': last['name'], 'type': last['label'],
                        'year': last.get('startDate', ''), 'slug': last['slug'],
                    })
                existing_effect_slugs = {c.get('slug') for c in last.get('effects', []) if c.get('slug')}
                if first['slug'] not in existing_effect_slugs:
                    last['effects'].append({
                        'title': first['name'], 'type': first['label'],
                        'year': first.get('startDate', ''), 'slug': first['slug'],
                    })


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 4: TypeScript Output
# ═══════════════════════════════════════════════════════════════════════════════

def make_entity_ts(entity, indent=2):
    """Generate TypeScript object literal for a single entity."""
    sp = ' ' * indent
    lines = ['{']
    lines.append(f"  {sp}slug: {ts_str(entity['slug'])},")
    lines.append(f"  {sp}name: {ts_str(entity['name'])},")
    lines.append(f"  {sp}label: '{entity['label']}',")
    lines.append(f"  {sp}callNumber: {ts_str(entity['callNumber'])},")

    # Subject headings
    sh = entity.get('subjectHeadings', [])
    sh_items = ', '.join(ts_str(s) for s in sh)
    lines.append(f"  {sp}subjectHeadings: [{sh_items}],")

    # Subjects
    subj = entity.get('subjects', [])
    subj_items = ', '.join(ts_str(s) for s in subj)
    lines.append(f"  {sp}subjects: [{subj_items}],")

    lines.append(f"  {sp}summary: {ts_str(entity.get('summary', ''))},")

    # Date fields
    for field in ('born', 'died', 'founded', 'period', 'startDate', 'endDate'):
        val = entity.get(field)
        if val:
            lines.append(f"  {sp}{field}: {ts_str(str(val))},")

    lines.append(f"  {sp}era: {ts_str(entity['era'])},")
    lines.append(f"  {sp}eraSlug: {ts_str(entity['eraSlug'])},")
    lines.append(f"  {sp}region: {ts_str(entity.get('region', ''))},")
    lines.append(f"  {sp}continent: {ts_str(entity.get('continent', ''))},")
    lines.append(f"  {sp}status: '{entity.get('status', 'PLANNED')}',")

    # Frameworks
    fw = entity.get('frameworks', [])
    fw_items = ', '.join(f"'{f}'" for f in fw)
    lines.append(f"  {sp}frameworks: [{fw_items}],")

    # Causes
    causes = entity.get('causes', [])
    if causes:
        cs = []
        for c in causes:
            slug_part = f", slug: {ts_str(c['slug'])}" if c.get('slug') else ''
            cs.append(
                f"{{ title: {ts_str(c['title'])}, type: {ts_str(c.get('type', 'EventWindow'))}, "
                f"year: {ts_str(c.get('year', ''))}{slug_part} }}"
            )
        lines.append(f"  {sp}causes: [{', '.join(cs)}],")
    else:
        lines.append(f"  {sp}causes: [],")

    # Effects
    effects = entity.get('effects', [])
    if effects:
        es = []
        for e in effects:
            slug_part = f", slug: {ts_str(e['slug'])}" if e.get('slug') else ''
            es.append(
                f"{{ title: {ts_str(e['title'])}, type: {ts_str(e.get('type', 'EventWindow'))}, "
                f"year: {ts_str(e.get('year', ''))}{slug_part} }}"
            )
        lines.append(f"  {sp}effects: [{', '.join(es)}],")
    else:
        lines.append(f"  {sp}effects: [],")

    # Relationships
    rels = entity.get('relationships', [])
    if rels:
        lines.append(f"  {sp}relationships: [")
        for r in rels:
            ctx = f", context: {ts_str(r.get('context', ''))}" if r.get('context') else ''
            lines.append(
                f"    {sp}{{ sourceSlug: {ts_str(r['sourceSlug'])}, "
                f"sourceName: {ts_str(r['sourceName'])}, "
                f"verb: '{escape_ts(r['verb'])}', "
                f"targetSlug: {ts_str(r['targetSlug'])}, "
                f"targetName: {ts_str(r['targetName'])}{ctx} }},"
            )
        lines.append(f"  {sp}],")
    else:
        lines.append(f"  {sp}relationships: [],")

    # Places
    places = entity.get('places', [])
    if places:
        ps = []
        for p in places:
            ps.append(f"{{ name: {ts_str(p['name'])}, role: {ts_str(p.get('role', ''))} }}")
        lines.append(f"  {sp}places: [{', '.join(ps)}],")
    else:
        lines.append(f"  {sp}places: [],")

    # Texts
    texts = entity.get('texts', [])
    if texts:
        ts_items = []
        for t in texts:
            ts_items.append(f"{{ title: {ts_str(t['title'])}, type: {ts_str(t.get('type', 'Text'))} }}")
        lines.append(f"  {sp}texts: [{', '.join(ts_items)}],")
    else:
        lines.append(f"  {sp}texts: [],")

    lines.append(f"{sp}}}")
    return '\n'.join(lines)


def strip_internal_fields(entity):
    """Remove internal metadata fields (prefixed with _) before output."""
    for key in list(entity.keys()):
        if key.startswith('_'):
            del entity[key]


def main():
    countries = sorted(d for d in os.listdir(BASE)
                       if os.path.isdir(os.path.join(BASE, d)) and d != '_template')

    print(f'Processing {len(countries)} countries...')

    # Phase 1: Extract
    all_entities = []
    for slug in countries:
        ents = extract_entities(slug)
        all_entities.extend(ents)
    print(f'  Extracted {len(all_entities)} raw entities')

    # Phase 2: Dedup slugs
    make_slugs_unique(all_entities)
    unique_slugs = len(set(e['slug'] for e in all_entities))
    print(f'  {unique_slugs} unique slugs after dedup')

    # Phase 3: Enrich
    enrich_all(all_entities)
    print(f'  Enriched with causes/effects/relationships')

    # Phase 4: Output
    label_counts = Counter(e['label'] for e in all_entities)

    for e in all_entities:
        strip_internal_fields(e)

    breakdown = ', '.join(f'{l} ({c})' for l, c in label_counts.most_common())
    stats_comment = (
        f'/**\n'
        f' * Geo-Registry Catalog \u2014 auto-generated from geo-registry country index files\n'
        f' * {len(all_entities)} enriched entities across {len(countries)} countries, 6 eras, 5 continents.\n'
        f' * Every entity has: summary, causes, effects, relationships, frameworks, places.\n'
        f' *\n'
        f' * Breakdown: {breakdown}\n'
        f' *\n'
        f' * DO NOT EDIT MANUALLY \u2014 regenerate with: python3 scripts/generate_geo_catalog.py\n'
        f' */\n'
    )

    out_lines = [stats_comment]
    out_lines.append("import type { Entity } from '../entityTypes'\n")
    out_lines.append('export const GEO_REGISTRY_ENTITIES: Entity[] = [')

    for entity in all_entities:
        out_lines.append(f'  {make_entity_ts(entity)},')

    out_lines.append(']')
    out_lines.append('')

    output = '\n'.join(out_lines)

    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f'\nGenerated {OUTPUT}')
    print(f'  {len(all_entities)} entities:')
    for label, count in label_counts.most_common():
        print(f'    {label}: {count}')
    print(f'  {len(countries)} countries')

    # Enrichment stats
    has_causes = sum(1 for e in all_entities if e.get('causes'))
    has_effects = sum(1 for e in all_entities if e.get('effects'))
    has_rels = sum(1 for e in all_entities if e.get('relationships'))
    has_fw = sum(1 for e in all_entities if e.get('frameworks'))
    has_texts = sum(1 for e in all_entities if e.get('texts'))
    print(f'  Enrichment coverage:')
    print(f'    With causes:        {has_causes}/{len(all_entities)} ({100*has_causes//len(all_entities)}%)')
    print(f'    With effects:       {has_effects}/{len(all_entities)} ({100*has_effects//len(all_entities)}%)')
    print(f'    With relationships: {has_rels}/{len(all_entities)} ({100*has_rels//len(all_entities)}%)')
    print(f'    With frameworks:    {has_fw}/{len(all_entities)} ({100*has_fw//len(all_entities)}%)')
    print(f'    With texts:         {has_texts}/{len(all_entities)} ({100*has_texts//len(all_entities)}%)')


if __name__ == '__main__':
    main()
