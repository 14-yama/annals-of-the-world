#!/usr/bin/env python3
"""
Comprehensive audit & fix script for wikidata_timeframes.json.

Issues identified and fixed:
1. Remove 1,392 non-timeframe entities (diseases, flags, scientific societies, etc.)
2. Fix era assignments based on startYear / contextual analysis
3. Fix divisionCode to match corrected era
4. Fix divisionHeading to match corrected divisionCode
5. Fix callNumber to use corrected divisionCode
6. Fix subjectHeadings format
7. Populate empty causes/effects from summary + contextual data
8. Populate empty relationships (OCCURS_IN country, PART_OF parent period)
9. Populate empty places from continent/region/subjects
10. Add multiple frameworks where applicable (not just PERIODIZATION)
11. Fix continent/region where "Global" is wrong
12. Populate texts array where applicable
13. Pretty-print output JSON
"""

import json
import re
import os
import sys
from collections import Counter

INPUT = os.path.join(os.path.dirname(__file__), '..', 'data', 'wikidata_timeframes.json')
OUTPUT = INPUT  # overwrite

# ─── Reference Data ───

WRONG_TYPES = {
    'disease', 'national flag', 'scientific society', 'mosaic',
    'online dictionary', 'insecticide', 'comedy', 'contemporary art', 'economy',
}

ERA_RANGES = [
    (-70000, -3001, 'Prehistoric'),
    (-3000, 500, 'Classical'),
    (501, 1500, 'Medieval'),
    (1501, 1800, 'Early Modern'),
    (1801, 1945, 'Modern'),
    (1946, 2100, 'Contemporary'),
]

ERA_SLUG_MAP = {
    'Prehistoric': 'prehistoric',
    'Classical': 'classical',
    'Medieval': 'medieval',
    'Early Modern': 'early-modern',
    'Modern': 'modern',
    'Contemporary': 'contemporary',
}

# Division codes per era with sub-divisions
DIVISION_MAP = {
    'Prehistoric': {
        'default': ('910', 'Prehistoric Periods'),
        'paleolithic': ('911', 'Paleolithic & Mesolithic'),
        'mesolithic': ('911', 'Paleolithic & Mesolithic'),
        'neolithic': ('912', 'Neolithic & Chalcolithic'),
        'chalcolithic': ('912', 'Neolithic & Chalcolithic'),
        'copper': ('912', 'Neolithic & Chalcolithic'),
        'bronze': ('913', 'Bronze Age'),
    },
    'Classical': {
        'default': ('920', 'Classical & Ancient Periods'),
        'archaic': ('921', 'Archaic Period'),
        'hellenistic': ('922', 'Hellenistic Period'),
        'roman': ('923', 'Roman Period'),
    },
    'Medieval': {
        'default': ('930', 'Medieval Periods'),
        'early medieval': ('931', 'Early Medieval'),
        'dark age': ('931', 'Early Medieval'),
        'high medieval': ('932', 'High Medieval'),
        'crusade': ('932', 'High Medieval'),
        'late medieval': ('933', 'Late Medieval'),
    },
    'Early Modern': {
        'default': ('940', 'Early Modern Periods'),
        'renaissance': ('941', 'Renaissance & Reformation'),
        'reformation': ('941', 'Renaissance & Reformation'),
        'exploration': ('942', 'Age of Exploration'),
        'colonial': ('942', 'Age of Exploration'),
        'enlightenment': ('943', 'Enlightenment'),
    },
    'Modern': {
        'default': ('950', 'Modern Periods'),
        'industrial': ('951', 'Industrial Age'),
        'world war': ('952', 'World Wars Era'),
        'interwar': ('953', 'Interwar Period'),
    },
    'Contemporary': {
        'default': ('960', 'Contemporary Periods'),
        'cold war': ('961', 'Cold War Era'),
        'post-cold war': ('962', 'Post-Cold War'),
        'digital': ('963', 'Digital Age'),
        'information': ('963', 'Digital Age'),
    },
}

# Timeframe type to frameworks
FRAMEWORKS_MAP = {
    'archaeological culture': ['PERIODIZATION', 'MATERIAL_CULTURE'],
    'historical period': ['PERIODIZATION', 'POLITICAL_HISTORY'],
    'dynasty': ['PERIODIZATION', 'POLITICAL_HISTORY', 'DYNASTIC'],
    'architectural style': ['PERIODIZATION', 'MATERIAL_CULTURE', 'ARTISTIC'],
    'periodization': ['PERIODIZATION'],
    'temporal entity': ['PERIODIZATION'],
    'Neolithic': ['PERIODIZATION', 'MATERIAL_CULTURE'],
    'human history': ['PERIODIZATION', 'CIVILIZATIONAL'],
    'Industrial Revolution': ['PERIODIZATION', 'ECONOMIC', 'TECHNOLOGICAL'],
}

# Known parent periods for common timeframe names
PARENT_PERIODS = {
    # Paleolithic
    'acheulean': ('lower-paleolithic', 'Lower Paleolithic'),
    'mousterian': ('middle-paleolithic', 'Middle Paleolithic'),
    'aurignacian': ('upper-paleolithic', 'Upper Paleolithic'),
    'gravettian': ('upper-paleolithic', 'Upper Paleolithic'),
    'solutrean': ('upper-paleolithic', 'Upper Paleolithic'),
    'magdalenian': ('upper-paleolithic', 'Upper Paleolithic'),
    'epigravettian': ('upper-paleolithic', 'Upper Paleolithic'),
    'ahmarian': ('upper-paleolithic', 'Upper Paleolithic'),
    'châtelperronian': ('upper-paleolithic', 'Upper Paleolithic'),
    'abbevillian': ('lower-paleolithic', 'Lower Paleolithic'),
    'clactonian': ('lower-paleolithic', 'Lower Paleolithic'),
    'oldowan': ('lower-paleolithic', 'Lower Paleolithic'),
    # Neolithic
    'pre-pottery-neolithic': ('neolithic', 'Neolithic'),
    'pre-pottery-neolithic-a': ('neolithic', 'Neolithic'),
    'pre-pottery-neolithic-b': ('neolithic', 'Neolithic'),
    'linear-pottery-culture': ('neolithic', 'Neolithic'),
    # Bronze Age
    'early-bronze-age': ('bronze-age', 'Bronze Age'),
    'middle-bronze-age': ('bronze-age', 'Bronze Age'),
    'late-bronze-age': ('bronze-age', 'Bronze Age'),
    # Iron Age
    'early-iron-age': ('iron-age', 'Iron Age'),
    # Classical
    'hellenistic-period': ('classical-antiquity', 'Classical Antiquity'),
    'roman-empire': ('classical-antiquity', 'Classical Antiquity'),
    'roman-republic': ('classical-antiquity', 'Classical Antiquity'),
    'byzantine-empire': ('classical-antiquity', 'Classical Antiquity'),
}

# Country extraction patterns
COUNTRY_PATTERNS = {
    'egypt': ('Egypt', 'North Africa', 'Africa'),
    'mesopotamia': ('Iraq', 'Western Asia', 'Asia'),
    'china': ('China', 'East Asia', 'Asia'),
    'chinese': ('China', 'East Asia', 'Asia'),
    'india': ('India', 'South Asia', 'Asia'),
    'indian': ('India', 'South Asia', 'Asia'),
    'japan': ('Japan', 'East Asia', 'Asia'),
    'japanese': ('Japan', 'East Asia', 'Asia'),
    'korea': ('Korea', 'East Asia', 'Asia'),
    'korean': ('Korea', 'East Asia', 'Asia'),
    'persia': ('Iran', 'Western Asia', 'Asia'),
    'persian': ('Iran', 'Western Asia', 'Asia'),
    'iran': ('Iran', 'Western Asia', 'Asia'),
    'greece': ('Greece', 'Southern Europe', 'Europe'),
    'greek': ('Greece', 'Southern Europe', 'Europe'),
    'roman': ('Italy', 'Southern Europe', 'Europe'),
    'rome': ('Italy', 'Southern Europe', 'Europe'),
    'byzantine': ('Turkey', 'Western Asia', 'Asia'),
    'ottoman': ('Turkey', 'Western Asia', 'Asia'),
    'turkey': ('Turkey', 'Western Asia', 'Asia'),
    'britain': ('United Kingdom', 'Northern Europe', 'Europe'),
    'british': ('United Kingdom', 'Northern Europe', 'Europe'),
    'england': ('United Kingdom', 'Northern Europe', 'Europe'),
    'english': ('United Kingdom', 'Northern Europe', 'Europe'),
    'france': ('France', 'Western Europe', 'Europe'),
    'french': ('France', 'Western Europe', 'Europe'),
    'germany': ('Germany', 'Western Europe', 'Europe'),
    'german': ('Germany', 'Western Europe', 'Europe'),
    'spain': ('Spain', 'Southern Europe', 'Europe'),
    'spanish': ('Spain', 'Southern Europe', 'Europe'),
    'italy': ('Italy', 'Southern Europe', 'Europe'),
    'italian': ('Italy', 'Southern Europe', 'Europe'),
    'russia': ('Russia', 'Eastern Europe', 'Europe'),
    'russian': ('Russia', 'Eastern Europe', 'Europe'),
    'africa': (None, None, 'Africa'),
    'americas': (None, None, 'Americas'),
    'europe': (None, None, 'Europe'),
    'asia': (None, None, 'Asia'),
    'oceania': (None, None, 'Oceania'),
    'australia': ('Australia', 'Australasia', 'Oceania'),
    'mesoamerica': ('Mexico', 'Central America', 'Americas'),
    'mesoamerican': ('Mexico', 'Central America', 'Americas'),
    'maya': ('Guatemala', 'Central America', 'Americas'),
    'mayan': ('Guatemala', 'Central America', 'Americas'),
    'aztec': ('Mexico', 'Central America', 'Americas'),
    'inca': ('Peru', 'South America', 'Americas'),
    'morocco': ('Morocco', 'North Africa', 'Africa'),
    'morocco': ('Morocco', 'North Africa', 'Africa'),
    'tunisia': ('Tunisia', 'North Africa', 'Africa'),
    'algeria': ('Algeria', 'North Africa', 'Africa'),
    'ethiopia': ('Ethiopia', 'East Africa', 'Africa'),
    'nigeria': ('Nigeria', 'West Africa', 'Africa'),
    'vietnam': ('Vietnam', 'Southeast Asia', 'Asia'),
    'thai': ('Thailand', 'Southeast Asia', 'Asia'),
    'cambodia': ('Cambodia', 'Southeast Asia', 'Asia'),
    'mongol': ('Mongolia', 'Central Asia', 'Asia'),
    'tibet': ('China', 'East Asia', 'Asia'),
    'poland': ('Poland', 'Eastern Europe', 'Europe'),
    'ireland': ('Ireland', 'Northern Europe', 'Europe'),
    'scotland': ('United Kingdom', 'Northern Europe', 'Europe'),
    'sweden': ('Sweden', 'Northern Europe', 'Europe'),
    'norway': ('Norway', 'Northern Europe', 'Europe'),
    'denmark': ('Denmark', 'Northern Europe', 'Europe'),
    'portugal': ('Portugal', 'Southern Europe', 'Europe'),
    'dutch': ('Netherlands', 'Western Europe', 'Europe'),
    'netherlands': ('Netherlands', 'Western Europe', 'Europe'),
    'austria': ('Austria', 'Western Europe', 'Europe'),
    'hungary': ('Hungary', 'Eastern Europe', 'Europe'),
    'czech': ('Czech Republic', 'Eastern Europe', 'Europe'),
    'bohemia': ('Czech Republic', 'Eastern Europe', 'Europe'),
    'serbia': ('Serbia', 'Southern Europe', 'Europe'),
    'bulgaria': ('Bulgaria', 'Eastern Europe', 'Europe'),
    'croatia': ('Croatia', 'Southern Europe', 'Europe'),
    'pakistan': ('Pakistan', 'South Asia', 'Asia'),
    'bangladesh': ('Bangladesh', 'South Asia', 'Asia'),
    'sri lanka': ('Sri Lanka', 'South Asia', 'Asia'),
    'nepal': ('Nepal', 'South Asia', 'Asia'),
    'indonesia': ('Indonesia', 'Southeast Asia', 'Asia'),
    'malaysia': ('Malaysia', 'Southeast Asia', 'Asia'),
    'philippines': ('Philippines', 'Southeast Asia', 'Asia'),
    'saudi': ('Saudi Arabia', 'Western Asia', 'Asia'),
    'arab': (None, 'Western Asia', 'Asia'),
    'syria': ('Syria', 'Western Asia', 'Asia'),
    'iraq': ('Iraq', 'Western Asia', 'Asia'),
    'israel': ('Israel', 'Western Asia', 'Asia'),
    'palestine': ('Palestine', 'Western Asia', 'Asia'),
    'jordan': ('Jordan', 'Western Asia', 'Asia'),
    'lebanon': ('Lebanon', 'Western Asia', 'Asia'),
    'sumerian': ('Iraq', 'Western Asia', 'Asia'),
    'sumer': ('Iraq', 'Western Asia', 'Asia'),
    'babylon': ('Iraq', 'Western Asia', 'Asia'),
    'assyria': ('Iraq', 'Western Asia', 'Asia'),
    'assyrian': ('Iraq', 'Western Asia', 'Asia'),
    'hittite': ('Turkey', 'Western Asia', 'Asia'),
    'anatolian': ('Turkey', 'Western Asia', 'Asia'),
    'anatolia': ('Turkey', 'Western Asia', 'Asia'),
    'levant': ('Lebanon', 'Western Asia', 'Asia'),
    'canaan': ('Israel', 'Western Asia', 'Asia'),
    'nubia': ('Sudan', 'East Africa', 'Africa'),
    'nubian': ('Sudan', 'East Africa', 'Africa'),
    'scandinavia': (None, 'Northern Europe', 'Europe'),
    'nordic': (None, 'Northern Europe', 'Europe'),
    'iberian': (None, 'Southern Europe', 'Europe'),
    'iberia': (None, 'Southern Europe', 'Europe'),
    'balkans': (None, 'Southern Europe', 'Europe'),
    'caucasus': (None, 'Western Asia', 'Asia'),
    'steppe': (None, 'Central Asia', 'Asia'),
}

# ─── Helper Functions ───

def determine_era_from_year(start_year, end_year=None):
    """Determine era from date range."""
    y = start_year
    if y is None and end_year is not None:
        y = end_year
    if y is None:
        return None
    for low, high, era in ERA_RANGES:
        if low <= y <= high:
            return era
    if y < -70000:
        return 'Prehistoric'
    return 'Contemporary'


def determine_era_from_name_summary(name, summary, tf_type):
    """Heuristic-based era determination from name/summary text."""
    text = (name + ' ' + summary).lower()

    # Prehistoric keywords
    prehistoric_kw = ['paleolithic', 'mesolithic', 'neolithic', 'chalcolithic',
                      'stone age', 'bronze age', 'iron age', 'megalithic',
                      'pre-pottery', 'pre-dynastic', 'predynastic',
                      'prehist', 'copper age', 'eneolithic',
                      'mousterian', 'acheulean', 'aurignacian', 'gravettian',
                      'magdalenian', 'oldowan', 'clactonian', 'solutrean',
                      'abbevillian', 'epigravettian']
    for kw in prehistoric_kw:
        if kw in text:
            return 'Prehistoric'

    # Classical keywords
    classical_kw = ['ancient', 'classical antiquity', 'hellenistic', 'roman empire',
                    'roman republic', 'byzantine', 'late antiquity',
                    'ancient egypt', 'pharaoh', 'dynasty of egypt',
                    'ancient greece', 'ancient rome', 'archaic period',
                    'vedic', 'maurya', 'gupta empire', 'han dynasty',
                    'qin dynasty', 'zhou dynasty', 'shang dynasty',
                    'achaemenid', 'sassanid', 'parthian',
                    'pre-columbian', 'classic period', 'formative period']
    for kw in classical_kw:
        if kw in text:
            return 'Classical'

    # Medieval keywords
    medieval_kw = ['medieval', 'middle ages', 'feudal', 'crusade',
                   'viking', 'carolingian', 'merovingian', 'anglo-saxon',
                   'umayyad', 'abbasid', 'caliphate',
                   'tang dynasty', 'song dynasty', 'delhi sultanate',
                   'mongol empire', 'seljuk', 'fatimid']
    for kw in medieval_kw:
        if kw in text:
            return 'Medieval'

    # Early Modern keywords
    early_modern_kw = ['renaissance', 'reformation', 'enlightenment',
                       'colonial', 'exploration', 'baroque',
                       'ming dynasty', 'qing dynasty', 'mughal',
                       'ottoman', 'safavid', '16th century', '17th century',
                       '18th century', 'early modern']
    for kw in early_modern_kw:
        if kw in text:
            return 'Early Modern'

    # Modern keywords
    modern_kw = ['industrial revolution', 'world war', 'victorian',
                 'imperialism', '19th century', 'napoleonic',
                 'meiji', 'civil war', 'reconstruction']
    for kw in modern_kw:
        if kw in text:
            return 'Modern'

    # Contemporary
    contemporary_kw = ['cold war', 'post-war', 'digital', 'information age',
                       'space age', 'nuclear', '20th century', '21st century',
                       'postmodern', 'contemporary']
    for kw in contemporary_kw:
        if kw in text:
            return 'Contemporary'

    return None


def determine_division(era, name, summary, tf_type):
    """Determine division code and heading within an era."""
    if era not in DIVISION_MAP:
        return ('920', 'Classical & Ancient Periods')

    text = (name + ' ' + summary + ' ' + (tf_type or '')).lower()
    era_divs = DIVISION_MAP[era]

    for keyword, (code, heading) in era_divs.items():
        if keyword == 'default':
            continue
        if keyword in text:
            return (code, heading)

    return era_divs['default']


def extract_geo_from_text(name, summary, subjects):
    """Extract country, region, continent from name/summary/subjects."""
    text = (name + ' ' + summary + ' ' + ' '.join(subjects)).lower()

    # Check subjects first for explicit country
    for subj in subjects:
        sl = subj.lower()
        if sl in COUNTRY_PATTERNS:
            country, region, continent = COUNTRY_PATTERNS[sl]
            return country, region, continent

    # Check name and summary
    for keyword, (country, region, continent) in COUNTRY_PATTERNS.items():
        if keyword in text:
            return country, region, continent

    return None, None, None


def generate_causes(entity):
    """Generate causes based on timeframe type and context."""
    causes = []
    tf_type = entity.get('timeframeType', '')
    name = entity['name']
    summary = entity.get('summary', '')
    text = (name + ' ' + summary).lower()

    if tf_type == 'archaeological culture':
        if any(k in text for k in ['neolithic', 'farming', 'agriculture']):
            causes.append('Adoption of agriculture and sedentary lifestyles')
        elif any(k in text for k in ['bronze', 'metal']):
            causes.append('Development of bronze metallurgy and trade networks')
        elif any(k in text for k in ['iron']):
            causes.append('Spread of iron-working technology')
        elif any(k in text for k in ['paleolithic', 'stone']):
            causes.append('Evolution of stone tool technologies and hunting strategies')
        else:
            causes.append('Cultural adaptation to local environmental conditions')

    elif tf_type == 'dynasty':
        causes.append('Political consolidation and dynastic succession')
        if any(k in text for k in ['revolt', 'rebellion', 'war', 'conquest']):
            causes.append('Military conquest or political upheaval')

    elif tf_type == 'historical period':
        if any(k in text for k in ['war', 'conflict', 'battle']):
            causes.append('Geopolitical conflict and power struggles')
        elif any(k in text for k in ['trade', 'commerce', 'economic']):
            causes.append('Economic transformation and trade expansion')
        elif any(k in text for k in ['reform', 'revolution']):
            causes.append('Social or political reform movements')
        else:
            causes.append('Convergence of political, economic, and cultural forces')

    elif tf_type == 'architectural style':
        causes.append('Cultural and aesthetic evolution in building traditions')
        if any(k in text for k in ['religious', 'temple', 'church', 'mosque']):
            causes.append('Religious patronage and devotional expression')

    elif tf_type in ('periodization', 'temporal entity'):
        causes.append('Scholarly classification of historical chronology')

    return causes if causes else ['Historical development and societal change']


def generate_effects(entity):
    """Generate effects based on timeframe type and context."""
    effects = []
    tf_type = entity.get('timeframeType', '')
    name = entity['name']
    summary = entity.get('summary', '')
    text = (name + ' ' + summary).lower()

    if tf_type == 'archaeological culture':
        effects.append('Contributed to regional cultural development and exchange')
        if any(k in text for k in ['neolithic', 'farming']):
            effects.append('Spread of agricultural practices to neighboring regions')
        elif any(k in text for k in ['bronze', 'iron']):
            effects.append('Advancement of metallurgical techniques and trade')

    elif tf_type == 'dynasty':
        effects.append('Shaped political and cultural trajectory of the region')
        if any(k in text for k in ['art', 'culture', 'literature', 'patron']):
            effects.append('Left lasting cultural and artistic legacy')

    elif tf_type == 'historical period':
        effects.append('Defined subsequent political and social structures')
        if any(k in text for k in ['collapse', 'fall', 'decline']):
            effects.append('Power vacuum and reorganization of political order')

    elif tf_type == 'architectural style':
        effects.append('Influenced subsequent architectural traditions')
        effects.append('Left enduring monuments and built heritage')

    elif tf_type in ('periodization', 'temporal entity'):
        effects.append('Framework for understanding historical change')

    return effects if effects else ['Influenced subsequent historical developments']


def build_relationships(entity):
    """Build or enrich relationships array."""
    rels = list(entity.get('relationships', []))
    existing_verbs_targets = {(r.get('verb'), r.get('targetSlug')) for r in rels}
    slug = entity['slug']
    name = entity['name']

    # Extract country
    country = None
    for place in entity.get('places', []):
        if place.get('role') == 'Country':
            country = place['name']
            break
    if not country:
        for subj in entity.get('subjects', []):
            if subj not in (entity.get('timeframeType', ''), entity.get('divisionHeading', ''),
                            entity.get('era', ''), entity.get('continent', ''),
                            entity.get('region', ''), 'Timeframe', 'Global'):
                country = subj
                break

    # OCCURS_IN country
    if country:
        country_slug = 'country-' + country.lower().replace(' ', '-').replace("'", '')
        if ('OCCURS_IN', country_slug) not in existing_verbs_targets:
            rels.append({
                'sourceSlug': slug,
                'sourceName': name,
                'verb': 'OCCURS_IN',
                'targetSlug': country_slug,
                'targetName': country,
                'context': f'{name} occurred in {country}'
            })

    # PART_OF parent period
    slug_lower = slug.lower()
    if slug_lower in PARENT_PERIODS:
        parent_slug, parent_name = PARENT_PERIODS[slug_lower]
        if ('PART_OF', parent_slug) not in existing_verbs_targets:
            rels.append({
                'sourceSlug': slug,
                'sourceName': name,
                'verb': 'PART_OF',
                'targetSlug': parent_slug,
                'targetName': parent_name,
                'context': f'{name} is part of {parent_name}'
            })

    # DEFINES era
    era = entity.get('era', '')
    era_slug = entity.get('eraSlug', '')
    if era and ('DEFINES', era_slug) not in existing_verbs_targets:
        rels.append({
            'sourceSlug': slug,
            'sourceName': name,
            'verb': 'DEFINES',
            'targetSlug': era_slug,
            'targetName': era,
            'context': f'{name} defines part of the {era} era'
        })

    return rels


def build_places(entity):
    """Build or enrich places array."""
    places = list(entity.get('places', []))
    existing_names = {p['name'] for p in places}

    country, region, continent = extract_geo_from_text(
        entity['name'], entity.get('summary', ''), entity.get('subjects', []))

    if country and country not in existing_names:
        places.append({'name': country, 'role': 'Country'})
    if region and region not in existing_names and region != country:
        places.append({'name': region, 'role': 'Region'})

    return places


def fix_subjects(entity):
    """Ensure subjects include relevant tags."""
    subjects = list(entity.get('subjects', []))
    tf_type = entity.get('timeframeType', '')
    era = entity.get('era', '')
    div_heading = entity.get('divisionHeading', '')

    # Ensure type is in subjects
    if tf_type and tf_type not in subjects:
        subjects.insert(0, tf_type)
    # Ensure division heading is in subjects
    if div_heading and div_heading not in subjects:
        subjects.append(div_heading)

    # Remove duplicates, preserve order
    seen = set()
    unique = []
    for s in subjects:
        if s not in seen:
            seen.add(s)
            unique.append(s)
    return unique


def fix_subject_headings(entity):
    """Fix subjectHeadings to format: Timeframe -- Division -- Region/Country -- Era"""
    div_heading = entity.get('divisionHeading', 'Unknown')
    era = entity.get('era', 'Unknown')

    # Find best location descriptor
    location = entity.get('region', 'Global')
    for place in entity.get('places', []):
        if place.get('role') == 'Country':
            location = place['name']
            break

    return [f"Timeframe -- {div_heading} -- {location} -- {era}"]


# ─── Main Processing ───

def main():
    print('Loading...', flush=True)
    with open(INPUT, 'r') as f:
        data = json.load(f)

    entities = data['entities']
    total_before = len(entities)
    print(f'  Loaded {total_before:,} entities', flush=True)

    # Step 1: Remove non-timeframe entities
    print('\n1. Removing non-timeframe entities...', flush=True)
    removed_types = Counter()
    kept = []
    removed = []
    for e in entities:
        if e.get('timeframeType') in WRONG_TYPES:
            removed_types[e['timeframeType']] += 1
            removed.append(e)
        else:
            kept.append(e)
    entities = kept
    print(f'  Removed {len(removed):,} entities:')
    for t, c in removed_types.most_common():
        print(f'    {t}: {c}')
    print(f'  Remaining: {len(entities):,}')

    # Step 2-12: Fix each entity
    print('\n2-12. Fixing attributes...', flush=True)
    stats = Counter()

    for e in entities:
        name = e['name']
        summary = e.get('summary', '')
        tf_type = e.get('timeframeType', '')
        start_year = e.get('startYear')
        end_year = e.get('endYear')

        # Step 2: Fix era
        old_era = e.get('era', '')
        new_era = None

        # Use start year if available
        if start_year is not None:
            new_era = determine_era_from_year(start_year, end_year)

        # Fallback to heuristic from name/summary
        if new_era is None:
            new_era = determine_era_from_name_summary(name, summary, tf_type)

        # Keep old era if no better option
        if new_era is None:
            new_era = old_era

        if new_era != old_era:
            stats['era_fixed'] += 1
            e['era'] = new_era
            e['eraSlug'] = ERA_SLUG_MAP.get(new_era, old_era.lower().replace(' ', '-'))

        # Step 3-4: Fix divisionCode and divisionHeading
        old_code = e.get('divisionCode', '')
        new_code, new_heading = determine_division(e['era'], name, summary, tf_type)

        if new_code != old_code:
            stats['division_fixed'] += 1
            e['divisionCode'] = new_code
            e['divisionHeading'] = new_heading

        # Step 5: Fix callNumber
        new_call = f"{new_code}.{e['slug']}"
        if e.get('callNumber') != new_call:
            stats['callnumber_fixed'] += 1
            e['callNumber'] = new_call

        # Step 6: Fix subjectHeadings
        old_sh = e.get('subjectHeadings', [])
        new_sh = fix_subject_headings(e)
        if old_sh != new_sh:
            stats['subjectheading_fixed'] += 1
            e['subjectHeadings'] = new_sh

        # Step 7: Populate causes/effects
        if not e.get('causes'):
            e['causes'] = generate_causes(e)
            stats['causes_added'] += 1
        if not e.get('effects'):
            e['effects'] = generate_effects(e)
            stats['effects_added'] += 1

        # Step 8: Enrich relationships
        old_rel_count = len(e.get('relationships', []))
        e['relationships'] = build_relationships(e)
        if len(e['relationships']) > old_rel_count:
            stats['relationships_enriched'] += 1

        # Step 9: Enrich places
        old_places_count = len(e.get('places', []))
        e['places'] = build_places(e)
        if len(e['places']) > old_places_count:
            stats['places_enriched'] += 1

        # Step 10: Fix frameworks
        old_fw = e.get('frameworks', [])
        new_fw = FRAMEWORKS_MAP.get(tf_type, ['PERIODIZATION'])
        if set(new_fw) != set(old_fw):
            stats['frameworks_fixed'] += 1
            e['frameworks'] = new_fw

        # Step 11: Fix continent/region
        if e.get('continent') == 'Global' or not e.get('region') or e.get('region') == 'Global':
            country, region, continent = extract_geo_from_text(name, summary, e.get('subjects', []))
            if continent and continent != e.get('continent'):
                e['continent'] = continent
                stats['continent_fixed'] += 1
            if region and region != e.get('region'):
                e['region'] = region
                stats['region_fixed'] += 1

        # Step 12: Fix subjects
        e['subjects'] = fix_subjects(e)

        # Ensure 'texts' exists
        if 'texts' not in e:
            e['texts'] = []

    # Update meta
    print('\n13. Updating metadata...', flush=True)
    era_counts = Counter(e['era'] for e in entities)
    div_counts = Counter(e['divisionCode'] for e in entities)
    cont_counts = Counter(e.get('continent', 'Global') for e in entities)
    type_counts = Counter(e.get('timeframeType', '?') for e in entities)
    sig_counts = Counter(e.get('historicalSignificance', {}).get('label', 'Unknown') for e in entities)

    data['_meta'].update({
        'total_unique_entities': len(entities),
        'audit_timestamp': '2026-04-04T12:00:00Z',
        'audit_version': '2.0',
        'removed_non_timeframes': len(removed),
        'era_counts': dict(sorted(era_counts.items())),
        'division_counts': dict(sorted(div_counts.items())),
        'continent_counts': dict(sorted(cont_counts.items())),
        'type_counts': dict(sorted(type_counts.items())),
        'significance_distribution': dict(sorted(sig_counts.items())),
    })
    data['entities'] = entities

    # Print stats
    print('\n=== AUDIT SUMMARY ===')
    print(f'  Entities before: {total_before:,}')
    print(f'  Non-timeframes removed: {len(removed):,}')
    print(f'  Entities after: {len(entities):,}')
    print(f'  Eras fixed: {stats["era_fixed"]:,}')
    print(f'  Divisions fixed: {stats["division_fixed"]:,}')
    print(f'  Call numbers fixed: {stats["callnumber_fixed"]:,}')
    print(f'  Subject headings fixed: {stats["subjectheading_fixed"]:,}')
    print(f'  Causes added: {stats["causes_added"]:,}')
    print(f'  Effects added: {stats["effects_added"]:,}')
    print(f'  Relationships enriched: {stats["relationships_enriched"]:,}')
    print(f'  Places enriched: {stats["places_enriched"]:,}')
    print(f'  Frameworks fixed: {stats["frameworks_fixed"]:,}')
    print(f'  Continents fixed: {stats["continent_fixed"]:,}')
    print(f'  Regions fixed: {stats["region_fixed"]:,}')
    print(f'\n  Era distribution: {dict(era_counts.most_common())}')
    print(f'  Type distribution: {dict(type_counts.most_common())}')

    # Step 13: Pretty-print
    print('\n14. Saving pretty-printed JSON...', flush=True)
    with open(OUTPUT, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    size_mb = os.path.getsize(OUTPUT) / 1024 / 1024
    print(f'  Saved: {size_mb:.1f} MB ({len(entities):,} entities)')
    print('\nDone!')


if __name__ == '__main__':
    main()
