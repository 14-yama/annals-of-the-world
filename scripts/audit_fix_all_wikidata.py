#!/usr/bin/env python3
"""
Comprehensive audit & fix for ALL wikidata JSON files.

Fixes per file:
- artifacts: Add CREATED_IN/PRODUCED_IN verbs, fix OCCURS_IN context, populate causes/effects/texts
- events: Add OCCURS_IN where missing, add CAUSES/PRECEDED_BY, populate causes/effects/texts
- evidence: Fix OCCURS_IN context, add DOCUMENTS/ATTESTS_TO verbs, populate causes/effects/texts
- ideas: Add OCCURS_IN/ORIGINATES_IN where missing, populate causes/effects/texts
- institutions: Fix OCCURS_IN→SITUATED_IN for places, add ESTABLISHED_IN, populate causes/effects/texts
- movements: Add OCCURS_IN/ARISES_FROM where missing, populate causes/effects/texts
- places: Fix SITUATED_IN context, add CONTAINS, populate causes/effects/texts

Cross-cutting:
- Fix OCCURS_IN context strings to be descriptive
- Enrich texts attribute with Wikipedia reference
- Populate empty causes/effects
- Pretty-print all JSON
"""

import json
import os
import re
import sys
from collections import Counter

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

# ─── Country extraction for geo context ───
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
    'america': ('United States', 'North America', 'Americas'),
    'american': ('United States', 'North America', 'Americas'),
    'united states': ('United States', 'North America', 'Americas'),
    'mexico': ('Mexico', 'Central America', 'Americas'),
    'brazil': ('Brazil', 'South America', 'Americas'),
    'canada': ('Canada', 'North America', 'Americas'),
    'australia': ('Australia', 'Australasia', 'Oceania'),
    'mesoamerica': ('Mexico', 'Central America', 'Americas'),
    'morocco': ('Morocco', 'North Africa', 'Africa'),
    'tunisia': ('Tunisia', 'North Africa', 'Africa'),
    'algeria': ('Algeria', 'North Africa', 'Africa'),
    'ethiopia': ('Ethiopia', 'East Africa', 'Africa'),
    'nigeria': ('Nigeria', 'West Africa', 'Africa'),
    'vietnam': ('Vietnam', 'Southeast Asia', 'Asia'),
    'thailand': ('Thailand', 'Southeast Asia', 'Asia'),
    'indonesia': ('Indonesia', 'Southeast Asia', 'Asia'),
    'philippines': ('Philippines', 'Southeast Asia', 'Asia'),
    'malaysia': ('Malaysia', 'Southeast Asia', 'Asia'),
    'mongol': ('Mongolia', 'Central Asia', 'Asia'),
    'pakistan': ('Pakistan', 'South Asia', 'Asia'),
    'iraq': ('Iraq', 'Western Asia', 'Asia'),
    'israel': ('Israel', 'Western Asia', 'Asia'),
    'syria': ('Syria', 'Western Asia', 'Asia'),
    'jordan': ('Jordan', 'Western Asia', 'Asia'),
    'lebanon': ('Lebanon', 'Western Asia', 'Asia'),
    'poland': ('Poland', 'Eastern Europe', 'Europe'),
    'ireland': ('Ireland', 'Northern Europe', 'Europe'),
    'scotland': ('United Kingdom', 'Northern Europe', 'Europe'),
    'sweden': ('Sweden', 'Northern Europe', 'Europe'),
    'norway': ('Norway', 'Northern Europe', 'Europe'),
    'denmark': ('Denmark', 'Northern Europe', 'Europe'),
    'portugal': ('Portugal', 'Southern Europe', 'Europe'),
    'netherlands': ('Netherlands', 'Western Europe', 'Europe'),
    'austria': ('Austria', 'Western Europe', 'Europe'),
    'hungary': ('Hungary', 'Eastern Europe', 'Europe'),
    'switzerland': ('Switzerland', 'Western Europe', 'Europe'),
    'belgium': ('Belgium', 'Western Europe', 'Europe'),
    'argentina': ('Argentina', 'South America', 'Americas'),
    'chile': ('Chile', 'South America', 'Americas'),
    'colombia': ('Colombia', 'South America', 'Americas'),
    'peru': ('Peru', 'South America', 'Americas'),
    'south africa': ('South Africa', 'Southern Africa', 'Africa'),
    'kenya': ('Kenya', 'East Africa', 'Africa'),
    'ghana': ('Ghana', 'West Africa', 'Africa'),
    'tanzania': ('Tanzania', 'East Africa', 'Africa'),
    'sudan': ('Sudan', 'East Africa', 'Africa'),
    'croatia': ('Croatia', 'Southern Europe', 'Europe'),
    'serbia': ('Serbia', 'Southern Europe', 'Europe'),
    'czech': ('Czech Republic', 'Eastern Europe', 'Europe'),
    'romania': ('Romania', 'Eastern Europe', 'Europe'),
    'ukraine': ('Ukraine', 'Eastern Europe', 'Europe'),
    'finland': ('Finland', 'Northern Europe', 'Europe'),
    'new zealand': ('New Zealand', 'Australasia', 'Oceania'),
    'malta': ('Malta', 'Southern Europe', 'Europe'),
    'cyprus': ('Cyprus', 'Western Asia', 'Asia'),
    'cuba': ('Cuba', 'Caribbean', 'Americas'),
    'jamaica': ('Jamaica', 'Caribbean', 'Americas'),
    'haiti': ('Haiti', 'Caribbean', 'Americas'),
}

NON_COUNTRIES = {
    'Global', 'Unknown', '', 'Timeframe', 'Prehistoric', 'Classical',
    'Medieval', 'Early Modern', 'Modern', 'Contemporary',
    'archaeological culture', 'historical period', 'dynasty',
    'architectural style', 'periodization', 'temporal entity',
}


def extract_country(name, summary, subjects, places):
    """Extract country from entity data."""
    # First check places
    for p in places:
        if p.get('role') == 'Country' and p['name'] not in NON_COUNTRIES:
            return p['name']

    # Check subjects for country names
    for s in subjects:
        sl = s.lower()
        if sl in COUNTRY_PATTERNS:
            return COUNTRY_PATTERNS[sl][0]

    # Check name + summary
    text = (name + ' ' + summary).lower()
    for keyword, (country, region, continent) in COUNTRY_PATTERNS.items():
        if country and keyword in text:
            return country

    return None


def fix_occurs_in_context(rel, entity_name, entity_label):
    """Fix OCCURS_IN context to be descriptive."""
    target = rel.get('targetName', 'Unknown')
    if target in NON_COUNTRIES:
        return None  # Remove bad OCCURS_IN

    label_contexts = {
        'Text': f'{entity_name} is an artifact from {target}',
        'EventWindow': f'{entity_name} took place in {target}',
        'Evidence': f'{entity_name} is located in {target}',
        'Idea': f'{entity_name} originated in {target}',
        'Institution': f'{entity_name} is situated in {target}',
        'Movement': f'{entity_name} originated in {target}',
        'Place': f'{entity_name} is situated in {target}',
        'Timeframe': f'{entity_name} occurred in {target}',
        'Person': f'{entity_name} was active in {target}',
    }
    return label_contexts.get(entity_label, f'{entity_name} in {target}')


# ─── ARTIFACT-SPECIFIC ───

ARTIFACT_TYPE_VERBS = {
    'statue': 'CREATED_IN',
    'sculpture': 'CREATED_IN',
    'painting': 'CREATED_IN',
    'manuscript': 'AUTHORED_IN',
    'book': 'AUTHORED_IN',
    'text': 'AUTHORED_IN',
    'codex': 'AUTHORED_IN',
    'inscription': 'CREATED_IN',
    'treaty': 'SIGNED_IN',
    'law': 'LEGISLATED_IN',
    'building': 'BUILT_IN',
    'temple': 'BUILT_IN',
    'monument': 'BUILT_IN',
    'palace': 'BUILT_IN',
    'castle': 'BUILT_IN',
    'fortress': 'BUILT_IN',
    'church': 'BUILT_IN',
    'mosque': 'BUILT_IN',
    'cathedral': 'BUILT_IN',
    'ship': 'BUILT_IN',
    'bridge': 'BUILT_IN',
    'dam': 'BUILT_IN',
    'tunnel': 'BUILT_IN',
    'wall': 'BUILT_IN',
    'road': 'BUILT_IN',
    'railway': 'BUILT_IN',
    'railway station': 'BUILT_IN',
    'airport': 'BUILT_IN',
    'sports venue': 'BUILT_IN',
    'stadium': 'BUILT_IN',
    'arena': 'BUILT_IN',
    'tower': 'BUILT_IN',
    'lighthouse': 'BUILT_IN',
    'canal': 'BUILT_IN',
    'aqueduct': 'BUILT_IN',
    'tomb': 'BUILT_IN',
    'mausoleum': 'BUILT_IN',
    'pyramid': 'BUILT_IN',
    'amphitheater': 'BUILT_IN',
    'coin': 'MINTED_IN',
    'medal': 'CREATED_IN',
    'pottery': 'CREATED_IN',
    'vase': 'CREATED_IN',
    'tool': 'CREATED_IN',
    'weapon': 'CREATED_IN',
    'armor': 'CREATED_IN',
    'musical instrument': 'CREATED_IN',
    'film': 'PRODUCED_IN',
    'opera': 'PRODUCED_IN',
    'album': 'PRODUCED_IN',
    'song': 'COMPOSED_IN',
    'symphony': 'COMPOSED_IN',
    'anthem': 'COMPOSED_IN',
    'hymn': 'COMPOSED_IN',
    'flag': 'ADOPTED_IN',
    'map': 'CREATED_IN',
    'photograph': 'CREATED_IN',
    'textile': 'CREATED_IN',
    'tapestry': 'CREATED_IN',
    'mosaic': 'CREATED_IN',
    'fresco': 'CREATED_IN',
    'mural': 'CREATED_IN',
    'stained glass': 'CREATED_IN',
    'software': 'DEVELOPED_IN',
    'patent': 'FILED_IN',
    'newspaper': 'PUBLISHED_IN',
    'journal': 'PUBLISHED_IN',
    'magazine': 'PUBLISHED_IN',
}

ARTIFACT_CAUSES = {
    'statue': 'Artistic and cultural expression in sculptural tradition',
    'sculpture': 'Artistic and cultural expression in sculptural tradition',
    'painting': 'Artistic patronage and creative expression',
    'manuscript': 'Need to record, preserve, or transmit knowledge',
    'book': 'Need to record, preserve, or transmit knowledge',
    'text': 'Need to record, preserve, or transmit knowledge',
    'codex': 'Need to preserve and compile textual traditions',
    'inscription': 'Need to commemorate events or assert authority',
    'treaty': 'Diplomatic negotiation and conflict resolution',
    'law': 'Need for legal governance and social order',
    'building': 'Architectural need and societal development',
    'temple': 'Religious devotion and ritual practice',
    'monument': 'Commemoration of historical events or persons',
    'church': 'Christian worship and community formation',
    'mosque': 'Islamic worship and community formation',
    'cathedral': 'Episcopal authority and Christian worship',
    'coin': 'Economic exchange and monetary standardization',
    'tool': 'Technological innovation and practical need',
    'weapon': 'Military technology and defensive need',
    'film': 'Cultural storytelling and entertainment',
    'newspaper': 'Public information and civic discourse',
    'sports venue': 'Organized athletic competition and public entertainment',
    'stadium': 'Organized athletic competition and public entertainment',
    'railway station': 'Transportation infrastructure development',
    'airport': 'Aviation infrastructure development',
    'bridge': 'Transportation and infrastructure need',
    'dam': 'Water management and hydroelectric power generation',
    'canal': 'Trade route development and water management',
}

ARTIFACT_EFFECTS = {
    'statue': 'Influenced artistic traditions and cultural expression',
    'sculpture': 'Influenced artistic traditions and cultural expression',
    'painting': 'Contributed to artistic heritage and cultural identity',
    'manuscript': 'Preserved and transmitted knowledge across generations',
    'book': 'Spread ideas and influenced intellectual traditions',
    'text': 'Preserved and transmitted knowledge across generations',
    'codex': 'Preserved textual traditions for future scholarship',
    'inscription': 'Provided historical documentation and evidence',
    'treaty': 'Shaped diplomatic relations and territorial boundaries',
    'law': 'Established legal precedents and governance frameworks',
    'building': 'Shaped urban landscape and architectural tradition',
    'temple': 'Served as center of religious and cultural life',
    'monument': 'Preserved collective memory and cultural identity',
    'church': 'Anchored Christian communities and worship',
    'mosque': 'Anchored Islamic communities and worship',
    'coin': 'Facilitated economic exchange and trade',
    'tool': 'Advanced technological capability and productivity',
    'weapon': 'Influenced military strategy and power dynamics',
    'film': 'Shaped popular culture and public discourse',
    'newspaper': 'Informed public opinion and civic engagement',
    'sports venue': 'Promoted athletic competition and community gathering',
    'bridge': 'Connected communities and facilitated trade',
    'dam': 'Managed water resources and generated power',
    'canal': 'Facilitated trade and transportation',
}

# ─── EVENT-SPECIFIC ───

EVENT_TYPE_VERBS = {
    'war': ['OCCURS_IN', 'CAUSES'],
    'battle': ['OCCURS_IN', 'CAUSES'],
    'revolution': ['OCCURS_IN', 'CAUSES', 'TRANSFORMS'],
    'rebellion': ['OCCURS_IN', 'CAUSES'],
    'treaty': ['OCCURS_IN'],
    'earthquake': ['OCCURS_IN'],
    'natural disaster': ['OCCURS_IN'],
    'volcanic eruption': ['OCCURS_IN'],
    'flood': ['OCCURS_IN'],
    'famine': ['OCCURS_IN'],
    'epidemic': ['OCCURS_IN'],
    'pandemic': ['OCCURS_IN'],
    'election': ['OCCURS_IN'],
    'coronation': ['OCCURS_IN'],
    'assassination': ['OCCURS_IN'],
    'massacre': ['OCCURS_IN'],
    'genocide': ['OCCURS_IN'],
    'expedition': ['OCCURS_IN'],
    'discovery': ['OCCURS_IN'],
    'conference': ['OCCURS_IN'],
    'council': ['OCCURS_IN'],
    'siege': ['OCCURS_IN'],
    'coup': ['OCCURS_IN', 'CAUSES'],
    'independence': ['OCCURS_IN', 'CAUSES'],
    'annexation': ['OCCURS_IN'],
    'migration': ['OCCURS_IN'],
    'colonization': ['OCCURS_IN'],
    'civil war': ['OCCURS_IN', 'CAUSES'],
    'revolt': ['OCCURS_IN', 'CAUSES'],
    'protest': ['OCCURS_IN'],
    'strike': ['OCCURS_IN'],
}

EVENT_CAUSES = {
    'war': 'Geopolitical tensions and competing interests',
    'battle': 'Military campaign and strategic objectives',
    'revolution': 'Social inequality and political grievances',
    'rebellion': 'Discontent with existing authority',
    'treaty': 'Need for diplomatic resolution of conflict',
    'earthquake': 'Tectonic plate movement and seismic activity',
    'natural disaster': 'Natural environmental forces',
    'volcanic eruption': 'Geological volcanic activity',
    'flood': 'Extreme weather and hydrological conditions',
    'famine': 'Crop failure and food supply disruption',
    'epidemic': 'Pathogen transmission and public health conditions',
    'pandemic': 'Global pathogen spread and transmission',
    'election': 'Democratic governance and political succession',
    'coronation': 'Dynastic succession and political authority',
    'assassination': 'Political conflict and targeted violence',
    'massacre': 'Political violence and ethnic or religious conflict',
    'genocide': 'Ethnic, racial, or religious persecution',
    'expedition': 'Desire for exploration and territorial expansion',
    'discovery': 'Scientific inquiry and exploration',
    'conference': 'Need for multilateral diplomatic engagement',
    'council': 'Need for collective decision-making',
    'siege': 'Military strategy to capture fortified position',
    'coup': 'Military or political power seizure',
    'independence': 'National self-determination movement',
    'annexation': 'Territorial expansion by a state',
    'migration': 'Environmental, economic, or political pressures',
    'colonization': 'Imperial expansion and resource extraction',
    'civil war': 'Internal political divisions and power struggles',
    'revolt': 'Resistance to oppressive authority',
    'protest': 'Social grievances and demand for change',
    'strike': 'Labor disputes and workers\' rights demands',
}

EVENT_EFFECTS = {
    'war': 'Reshaped political boundaries and power dynamics',
    'battle': 'Determined military outcome and territorial control',
    'revolution': 'Transformed political and social structures',
    'rebellion': 'Challenged existing political authority',
    'treaty': 'Established new diplomatic framework and boundaries',
    'earthquake': 'Caused destruction and reshaped communities',
    'natural disaster': 'Disrupted communities and triggered recovery efforts',
    'volcanic eruption': 'Devastated local environment and communities',
    'flood': 'Destroyed infrastructure and affected agriculture',
    'famine': 'Caused mass suffering and population decline',
    'epidemic': 'Caused widespread illness and social disruption',
    'pandemic': 'Transformed public health and social institutions globally',
    'election': 'Determined political leadership and policy direction',
    'coronation': 'Established new sovereign authority',
    'assassination': 'Created political instability and succession crisis',
    'massacre': 'Inflicted collective trauma and international condemnation',
    'genocide': 'Destroyed communities and provoked international response',
    'expedition': 'Expanded geographic knowledge and territorial claims',
    'discovery': 'Advanced scientific understanding',
    'conference': 'Shaped international agreements and norms',
    'council': 'Produced institutional decisions and policies',
    'siege': 'Determined control of strategic position',
    'coup': 'Disrupted political order and governance',
    'independence': 'Established new sovereign state',
    'annexation': 'Expanded state territory and altered sovereignty',
    'migration': 'Transformed demographic and cultural landscapes',
    'colonization': 'Established colonial control over territories',
    'civil war': 'Divided and reconstructed political order',
    'revolt': 'Challenged and potentially reformed authority',
    'protest': 'Advanced social and political reform',
    'strike': 'Improved labor conditions and workers\' rights',
}

# ─── EVIDENCE-SPECIFIC ───

EVIDENCE_TYPE_VERBS = {
    'archaeological site': 'DOCUMENTS',
    'artifact': 'DOCUMENTS',
    'manuscript': 'ATTESTS_TO',
    'inscription': 'ATTESTS_TO',
    'text': 'ATTESTS_TO',
    'monument': 'DOCUMENTS',
    'fossil': 'DATES',
    'bone': 'DATES',
    'skeleton': 'DATES',
    'tool': 'DOCUMENTS',
    'pottery': 'DOCUMENTS',
    'coin': 'DOCUMENTS',
    'seal': 'DOCUMENTS',
    'tablet': 'ATTESTS_TO',
    'papyrus': 'ATTESTS_TO',
    'scroll': 'ATTESTS_TO',
    'chronicle': 'REPORTS',
    'codex': 'ATTESTS_TO',
    'stela': 'ATTESTS_TO',
    'sculpture': 'DOCUMENTS',
    'painting': 'DOCUMENTS',
    'mural': 'DOCUMENTS',
    'relief': 'DOCUMENTS',
    'temple': 'DOCUMENTS',
    'tomb': 'DOCUMENTS',
    'burial': 'DOCUMENTS',
    'cave': 'DOCUMENTS',
    'ruins': 'DOCUMENTS',
    'shipwreck': 'DOCUMENTS',
    'fortification': 'DOCUMENTS',
    'settlement': 'DOCUMENTS',
    'city': 'DOCUMENTS',
    'architectural ruin': 'DOCUMENTS',
}

# ─── IDEA-SPECIFIC ───

IDEA_TYPE_VERBS = {
    'philosophical concept': 'ORIGINATES_IN',
    'scientific theory': 'ORIGINATES_IN',
    'religious doctrine': 'ORIGINATES_IN',
    'political ideology': 'ORIGINATES_IN',
    'economic theory': 'ORIGINATES_IN',
    'legal doctrine': 'ORIGINATES_IN',
    'mathematical concept': 'ORIGINATES_IN',
    'artistic movement': 'ARISES_IN',
    'literary genre': 'ARISES_IN',
    'cultural practice': 'ORIGINATES_IN',
    'social theory': 'ORIGINATES_IN',
    'military strategy': 'ORIGINATES_IN',
    'technology': 'INVENTED_IN',
    'invention': 'INVENTED_IN',
    'academic discipline': 'ORIGINATES_IN',
}

# ─── INSTITUTION-SPECIFIC ───

INSTITUTION_TYPE_VERBS = {
    'government': 'GOVERNS',
    'university': 'SITUATED_IN',
    'school': 'SITUATED_IN',
    'library': 'SITUATED_IN',
    'museum': 'SITUATED_IN',
    'temple': 'SITUATED_IN',
    'church': 'SITUATED_IN',
    'mosque': 'SITUATED_IN',
    'monastery': 'SITUATED_IN',
    'hospital': 'SITUATED_IN',
    'court': 'SITUATED_IN',
    'parliament': 'SITUATED_IN',
    'military': 'SITUATED_IN',
    'bank': 'SITUATED_IN',
    'company': 'SITUATED_IN',
    'organization': 'SITUATED_IN',
    'corporation': 'SITUATED_IN',
    'empire': 'GOVERNS',
    'kingdom': 'GOVERNS',
    'state': 'GOVERNS',
    'colony': 'GOVERNS',
    'republic': 'GOVERNS',
    'dynasty': 'GOVERNS',
    'art museum': 'SITUATED_IN',
}

# ─── MOVEMENT-SPECIFIC ───

MOVEMENT_TYPE_VERBS = {
    'religious organization': 'ORIGINATES_IN',
    'religious movement': 'ORIGINATES_IN',
    'political movement': 'ORIGINATES_IN',
    'social movement': 'ORIGINATES_IN',
    'artistic movement': 'ORIGINATES_IN',
    'literary movement': 'ORIGINATES_IN',
    'philosophical movement': 'ORIGINATES_IN',
    'scientific movement': 'ORIGINATES_IN',
    'reform movement': 'ORIGINATES_IN',
    'revolutionary movement': 'ARISES_IN',
    'nationalist movement': 'ARISES_IN',
    'independence movement': 'ARISES_IN',
    'labor movement': 'ARISES_IN',
    'civil rights movement': 'ARISES_IN',
}


def make_text_entry(entity):
    """Create a texts array entry from Wikipedia data."""
    wp_url = entity.get('wikipediaUrl', '')
    name = entity['name']
    if wp_url:
        return {'title': f'Wikipedia: {name}', 'type': 'Reference article', 'slug': f'wikipedia-{entity["slug"]}'}
    return None


def get_generic_cause(label, name, summary):
    """Generate a cause based on entity label."""
    text = (name + ' ' + summary).lower()
    if label == 'Text':
        if any(k in text for k in ['treaty', 'agreement', 'convention']):
            return 'Diplomatic negotiation and international relations'
        if any(k in text for k in ['law', 'constitution', 'statute', 'decree']):
            return 'Legal and governance development'
        if any(k in text for k in ['religious', 'sacred', 'holy', 'church', 'temple']):
            return 'Religious devotion and spiritual expression'
        return 'Cultural, artistic, or intellectual creation'
    elif label == 'EventWindow':
        return 'Historical forces and geopolitical developments'
    elif label == 'Evidence':
        return 'Historical activity leaving material or documentary traces'
    elif label == 'Idea':
        if any(k in text for k in ['religion', 'faith', 'god', 'spiritual']):
            return 'Religious and spiritual inquiry'
        if any(k in text for k in ['science', 'theory', 'experiment']):
            return 'Scientific observation and intellectual inquiry'
        return 'Intellectual inquiry and cultural development'
    elif label == 'Institution':
        if any(k in text for k in ['university', 'school', 'academy']):
            return 'Educational need and knowledge advancement'
        if any(k in text for k in ['church', 'mosque', 'temple', 'monastery']):
            return 'Religious community formation and worship'
        if any(k in text for k in ['hospital', 'medical']):
            return 'Healthcare need and medical advancement'
        if any(k in text for k in ['military', 'army', 'navy', 'force']):
            return 'National defense and military organization'
        return 'Organizational need and institutional development'
    elif label == 'Movement':
        if any(k in text for k in ['religious', 'spiritual', 'faith']):
            return 'Religious reform and spiritual aspiration'
        if any(k in text for k in ['political', 'revolution', 'independence']):
            return 'Political grievances and desire for change'
        return 'Social, political, or cultural forces driving collective action'
    elif label == 'Place':
        if any(k in text for k in ['city', 'town', 'settlement']):
            return 'Human settlement and community formation'
        if any(k in text for k in ['river', 'mountain', 'lake', 'sea']):
            return 'Natural geographic formation'
        return 'Geographic and historical development'
    return 'Historical development'


def get_generic_effect(label, name, summary):
    """Generate an effect based on entity label."""
    text = (name + ' ' + summary).lower()
    if label == 'Text':
        if any(k in text for k in ['treaty', 'agreement']):
            return 'Shaped diplomatic relations and international order'
        return 'Contributed to cultural heritage and knowledge transmission'
    elif label == 'EventWindow':
        return 'Influenced subsequent historical developments'
    elif label == 'Evidence':
        return 'Provided material evidence for understanding historical periods'
    elif label == 'Idea':
        return 'Influenced intellectual traditions and cultural development'
    elif label == 'Institution':
        return 'Shaped institutional landscape and community development'
    elif label == 'Movement':
        return 'Influenced social, political, or cultural transformation'
    elif label == 'Place':
        return 'Served as a center of human activity and development'
    return 'Influenced subsequent historical developments'


def process_artifacts(data):
    """Audit and fix wikidata_artifacts.json."""
    ents = data['entities']
    stats = Counter()

    for e in ents:
        name = e['name']
        slug = e['slug']
        summary = e.get('summary', '')
        country = extract_country(name, summary, e.get('subjects', []), e.get('places', []))
        artifact_type = e.get('artifactType', '').lower()

        # Fix OCCURS_IN context and add type-specific verb
        new_rels = []
        has_occurs_in = False
        for r in e.get('relationships', []):
            if r['verb'] == 'OCCURS_IN':
                target = r.get('targetName', '')
                if target in NON_COUNTRIES:
                    stats['removed_bad_occurs_in'] += 1
                    continue
                # Fix context
                r['context'] = f'{name} is an artifact from {target}'
                has_occurs_in = True

                # Add type-specific verb
                specific_verb = ARTIFACT_TYPE_VERBS.get(artifact_type, 'CREATED_IN')
                new_rels.append({
                    'sourceSlug': slug, 'sourceName': name,
                    'verb': specific_verb,
                    'targetSlug': r['targetSlug'], 'targetName': target,
                    'context': f'{name} was {specific_verb.lower().replace("_", " ")} {target}'
                })
                stats['type_verb_added'] += 1
            new_rels.append(r)

        # Add OCCURS_IN if missing but have country
        if not has_occurs_in and country:
            country_slug = 'country-' + country.lower().replace(' ', '-').replace("'", '')
            new_rels.append({
                'sourceSlug': slug, 'sourceName': name,
                'verb': 'OCCURS_IN',
                'targetSlug': country_slug, 'targetName': country,
                'context': f'{name} is an artifact from {country}'
            })
            specific_verb = ARTIFACT_TYPE_VERBS.get(artifact_type, 'CREATED_IN')
            new_rels.append({
                'sourceSlug': slug, 'sourceName': name,
                'verb': specific_verb,
                'targetSlug': country_slug, 'targetName': country,
                'context': f'{name} was {specific_verb.lower().replace("_", " ")} {country}'
            })
            stats['occurs_in_added'] += 1

        e['relationships'] = new_rels

        # Causes/effects
        if not e.get('causes'):
            cause = ARTIFACT_CAUSES.get(artifact_type, get_generic_cause('Text', name, summary))
            e['causes'] = [cause]
            stats['causes_added'] += 1
        if not e.get('effects'):
            effect = ARTIFACT_EFFECTS.get(artifact_type, get_generic_effect('Text', name, summary))
            e['effects'] = [effect]
            stats['effects_added'] += 1

        # Texts
        if not e.get('texts'):
            t = make_text_entry(e)
            if t:
                e['texts'] = [t]
                stats['texts_added'] += 1

    return stats


def process_events(data):
    """Audit and fix wikidata_events.json."""
    ents = data['entities']
    stats = Counter()

    for e in ents:
        name = e['name']
        slug = e['slug']
        summary = e.get('summary', '')
        event_type = e.get('eventType', '').lower()
        country = extract_country(name, summary, e.get('subjects', []), e.get('places', []))

        # Fix existing rels
        new_rels = []
        has_occurs_in = False
        for r in e.get('relationships', []):
            if r['verb'] == 'OCCURS_IN':
                target = r.get('targetName', '')
                if target in NON_COUNTRIES:
                    stats['removed_bad_occurs_in'] += 1
                    continue
                r['context'] = f'{name} took place in {target}'
                has_occurs_in = True
            new_rels.append(r)

        # Add OCCURS_IN if missing
        if not has_occurs_in and country:
            country_slug = 'country-' + country.lower().replace(' ', '-').replace("'", '')
            new_rels.append({
                'sourceSlug': slug, 'sourceName': name,
                'verb': 'OCCURS_IN',
                'targetSlug': country_slug, 'targetName': country,
                'context': f'{name} took place in {country}'
            })
            stats['occurs_in_added'] += 1
            has_occurs_in = True

        # Add location from places if still no OCCURS_IN
        if not has_occurs_in:
            for p in e.get('places', []):
                pname = p.get('name', '')
                if pname and pname not in NON_COUNTRIES:
                    p_slug = pname.lower().replace(' ', '-').replace("'", '')
                    new_rels.append({
                        'sourceSlug': slug, 'sourceName': name,
                        'verb': 'OCCURS_IN',
                        'targetSlug': p_slug, 'targetName': pname,
                        'context': f'{name} took place in {pname}'
                    })
                    stats['occurs_in_from_places'] += 1
                    break

        e['relationships'] = new_rels

        # Causes/effects
        if not e.get('causes'):
            cause = EVENT_CAUSES.get(event_type, get_generic_cause('EventWindow', name, summary))
            e['causes'] = [cause]
            stats['causes_added'] += 1
        if not e.get('effects'):
            effect = EVENT_EFFECTS.get(event_type, get_generic_effect('EventWindow', name, summary))
            e['effects'] = [effect]
            stats['effects_added'] += 1

        # Texts
        if not e.get('texts'):
            t = make_text_entry(e)
            if t:
                e['texts'] = [t]
                stats['texts_added'] += 1

    return stats


def process_evidence(data):
    """Audit and fix wikidata_evidence.json."""
    ents = data['entities']
    stats = Counter()

    for e in ents:
        name = e['name']
        slug = e['slug']
        summary = e.get('summary', '')
        evidence_type = e.get('evidenceType', '').lower()
        country = extract_country(name, summary, e.get('subjects', []), e.get('places', []))

        new_rels = []
        has_occurs_in = False
        for r in e.get('relationships', []):
            if r['verb'] == 'OCCURS_IN':
                target = r.get('targetName', '')
                if target in NON_COUNTRIES:
                    stats['removed_bad_occurs_in'] += 1
                    continue
                r['context'] = f'{name} is located in {target}'
                has_occurs_in = True

                # Add evidence-specific verb
                ev_verb = EVIDENCE_TYPE_VERBS.get(evidence_type, 'DOCUMENTS')
                new_rels.append({
                    'sourceSlug': slug, 'sourceName': name,
                    'verb': ev_verb,
                    'targetSlug': f'{e.get("era", "classical").lower()}-era',
                    'targetName': f'{e.get("era", "Classical")} era',
                    'context': f'{name} {ev_verb.lower().replace("_", " ")} the {e.get("era", "Classical")} era in {target}'
                })
                stats['evidence_verb_added'] += 1
            new_rels.append(r)

        if not has_occurs_in and country:
            country_slug = 'country-' + country.lower().replace(' ', '-').replace("'", '')
            new_rels.append({
                'sourceSlug': slug, 'sourceName': name,
                'verb': 'OCCURS_IN',
                'targetSlug': country_slug, 'targetName': country,
                'context': f'{name} is located in {country}'
            })
            stats['occurs_in_added'] += 1

        e['relationships'] = new_rels

        # Causes/effects
        if not e.get('causes'):
            e['causes'] = [get_generic_cause('Evidence', name, summary)]
            stats['causes_added'] += 1
        if not e.get('effects'):
            e['effects'] = [get_generic_effect('Evidence', name, summary)]
            stats['effects_added'] += 1

        # Texts
        if not e.get('texts'):
            t = make_text_entry(e)
            if t:
                e['texts'] = [t]
                stats['texts_added'] += 1

    return stats


def process_ideas(data):
    """Audit and fix wikidata_ideas.json."""
    ents = data['entities']
    stats = Counter()

    for e in ents:
        name = e['name']
        slug = e['slug']
        summary = e.get('summary', '')
        idea_type = e.get('ideaType', '').lower()
        country = extract_country(name, summary, e.get('subjects', []), e.get('places', []))

        new_rels = []
        has_occurs_in = False
        for r in e.get('relationships', []):
            if r['verb'] == 'OCCURS_IN':
                target = r.get('targetName', '')
                if target in NON_COUNTRIES:
                    stats['removed_bad_occurs_in'] += 1
                    continue
                r['context'] = f'{name} originated in {target}'
                has_occurs_in = True
            new_rels.append(r)

        if not has_occurs_in and country:
            country_slug = 'country-' + country.lower().replace(' ', '-').replace("'", '')
            new_rels.append({
                'sourceSlug': slug, 'sourceName': name,
                'verb': 'OCCURS_IN',
                'targetSlug': country_slug, 'targetName': country,
                'context': f'{name} originated in {country}'
            })
            stats['occurs_in_added'] += 1

        e['relationships'] = new_rels

        # Causes/effects
        if not e.get('causes'):
            e['causes'] = [get_generic_cause('Idea', name, summary)]
            stats['causes_added'] += 1
        if not e.get('effects'):
            e['effects'] = [get_generic_effect('Idea', name, summary)]
            stats['effects_added'] += 1

        # Texts
        if not e.get('texts'):
            t = make_text_entry(e)
            if t:
                e['texts'] = [t]
                stats['texts_added'] += 1

    return stats


def process_institutions(data):
    """Audit and fix wikidata_institutions.json."""
    ents = data['entities']
    stats = Counter()

    for e in ents:
        name = e['name']
        slug = e['slug']
        summary = e.get('summary', '')
        inst_type = e.get('institutionType', '').lower()
        country = extract_country(name, summary, e.get('subjects', []), e.get('places', []))

        new_rels = []
        has_geo_rel = False
        for r in e.get('relationships', []):
            if r['verb'] == 'OCCURS_IN':
                target = r.get('targetName', '')
                if target in NON_COUNTRIES:
                    stats['removed_bad_occurs_in'] += 1
                    continue
                # For institutions, OCCURS_IN → SITUATED_IN
                r['verb'] = 'SITUATED_IN'
                r['context'] = f'{name} is situated in {target}'
                has_geo_rel = True
                stats['occurs_in_to_situated_in'] += 1

                # Add type-specific verb
                type_verb = INSTITUTION_TYPE_VERBS.get(inst_type, 'SITUATED_IN')
                if type_verb == 'GOVERNS':
                    new_rels.append({
                        'sourceSlug': slug, 'sourceName': name,
                        'verb': 'GOVERNS',
                        'targetSlug': r['targetSlug'], 'targetName': target,
                        'context': f'{name} governs {target}'
                    })
                    stats['governs_added'] += 1
            new_rels.append(r)

        if not has_geo_rel and country:
            country_slug = 'country-' + country.lower().replace(' ', '-').replace("'", '')
            new_rels.append({
                'sourceSlug': slug, 'sourceName': name,
                'verb': 'SITUATED_IN',
                'targetSlug': country_slug, 'targetName': country,
                'context': f'{name} is situated in {country}'
            })
            stats['situated_in_added'] += 1

        e['relationships'] = new_rels

        # Causes/effects
        if not e.get('causes'):
            e['causes'] = [get_generic_cause('Institution', name, summary)]
            stats['causes_added'] += 1
        if not e.get('effects'):
            e['effects'] = [get_generic_effect('Institution', name, summary)]
            stats['effects_added'] += 1

        # Texts
        if not e.get('texts'):
            t = make_text_entry(e)
            if t:
                e['texts'] = [t]
                stats['texts_added'] += 1

    return stats


def process_movements(data):
    """Audit and fix wikidata_movements.json."""
    ents = data['entities']
    stats = Counter()

    for e in ents:
        name = e['name']
        slug = e['slug']
        summary = e.get('summary', '')
        movement_type = e.get('movementType', '').lower()
        country = extract_country(name, summary, e.get('subjects', []), e.get('places', []))

        new_rels = []
        has_occurs_in = False
        for r in e.get('relationships', []):
            if r['verb'] == 'OCCURS_IN':
                target = r.get('targetName', '')
                if target in NON_COUNTRIES:
                    stats['removed_bad_occurs_in'] += 1
                    continue
                r['context'] = f'{name} originated in {target}'
                has_occurs_in = True
            new_rels.append(r)

        if not has_occurs_in and country:
            country_slug = 'country-' + country.lower().replace(' ', '-').replace("'", '')
            new_rels.append({
                'sourceSlug': slug, 'sourceName': name,
                'verb': 'OCCURS_IN',
                'targetSlug': country_slug, 'targetName': country,
                'context': f'{name} originated in {country}'
            })
            stats['occurs_in_added'] += 1

        e['relationships'] = new_rels

        # Causes/effects
        if not e.get('causes'):
            e['causes'] = [get_generic_cause('Movement', name, summary)]
            stats['causes_added'] += 1
        if not e.get('effects'):
            e['effects'] = [get_generic_effect('Movement', name, summary)]
            stats['effects_added'] += 1

        # Texts
        if not e.get('texts'):
            t = make_text_entry(e)
            if t:
                e['texts'] = [t]
                stats['texts_added'] += 1

    return stats


def process_places(data):
    """Audit and fix wikidata_places.json."""
    ents = data['entities']
    stats = Counter()

    for e in ents:
        name = e['name']
        slug = e['slug']
        summary = e.get('summary', '')
        country = extract_country(name, summary, e.get('subjects', []), e.get('places', []))

        new_rels = []
        has_geo_rel = False
        for r in e.get('relationships', []):
            if r['verb'] == 'SITUATED_IN':
                target = r.get('targetName', '')
                if target in NON_COUNTRIES:
                    stats['removed_bad_situated_in'] += 1
                    continue
                r['context'] = f'{name} is situated in {target}'
                has_geo_rel = True
            new_rels.append(r)

        if not has_geo_rel and country:
            country_slug = 'country-' + country.lower().replace(' ', '-').replace("'", '')
            new_rels.append({
                'sourceSlug': slug, 'sourceName': name,
                'verb': 'SITUATED_IN',
                'targetSlug': country_slug, 'targetName': country,
                'context': f'{name} is situated in {country}'
            })
            stats['situated_in_added'] += 1

        e['relationships'] = new_rels

        # Causes/effects
        if not e.get('causes'):
            e['causes'] = [get_generic_cause('Place', name, summary)]
            stats['causes_added'] += 1
        if not e.get('effects'):
            e['effects'] = [get_generic_effect('Place', name, summary)]
            stats['effects_added'] += 1

        # Texts
        if not e.get('texts'):
            t = make_text_entry(e)
            if t:
                e['texts'] = [t]
                stats['texts_added'] += 1

    return stats


# ─── MAIN ───

PROCESSORS = {
    'wikidata_artifacts.json': ('Text', process_artifacts),
    'wikidata_events.json': ('EventWindow', process_events),
    'wikidata_evidence.json': ('Evidence', process_evidence),
    'wikidata_ideas.json': ('Idea', process_ideas),
    'wikidata_institutions.json': ('Institution', process_institutions),
    'wikidata_movements.json': ('Movement', process_movements),
    'wikidata_places.json': ('Place', process_places),
}


def main():
    all_new_verbs = set()
    grand_stats = Counter()

    for fn, (label, processor) in PROCESSORS.items():
        path = os.path.join(DATA_DIR, fn)
        print(f'\n{"="*60}')
        print(f'  Processing {fn}...')
        print(f'{"="*60}')

        with open(path, 'r') as f:
            data = json.load(f)

        total = len(data['entities'])
        print(f'  Loaded {total:,} entities', flush=True)

        stats = processor(data)

        # Collect all verbs used
        verb_counts = Counter()
        for e in data['entities']:
            for r in e.get('relationships', []):
                v = r.get('verb', '?')
                verb_counts[v] += 1
                all_new_verbs.add(v)

        # Report
        print(f'  --- Stats ---')
        for k, v in stats.most_common():
            print(f'    {k:35s}: {v:>7}')
            grand_stats[k] += v

        print(f'  --- Verb Distribution ---')
        for v, c in verb_counts.most_common():
            print(f'    {v:30s}: {c:>7}')

        # Quality check
        no_rels = sum(1 for e in data['entities'] if not e.get('relationships'))
        no_causes = sum(1 for e in data['entities'] if not e.get('causes'))
        no_effects = sum(1 for e in data['entities'] if not e.get('effects'))
        no_texts = sum(1 for e in data['entities'] if not e.get('texts'))
        print(f'  --- Remaining Gaps ---')
        print(f'    No relationships: {no_rels:>7}/{total}')
        print(f'    No causes:        {no_causes:>7}/{total}')
        print(f'    No effects:       {no_effects:>7}/{total}')
        print(f'    No texts:         {no_texts:>7}/{total}')

        # Save
        with open(path, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        sz = os.path.getsize(path) / 1024 / 1024
        print(f'  Saved: {sz:.1f} MB')

    print(f'\n{"="*60}')
    print(f'  GRAND SUMMARY')
    print(f'{"="*60}')
    for k, v in grand_stats.most_common():
        print(f'  {k:35s}: {v:>9}')
    print(f'\n  All unique verbs across 7 files: {sorted(all_new_verbs)}')


if __name__ == '__main__':
    main()
