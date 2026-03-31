#!/usr/bin/env python3
"""
Populate sub_cluster.nodes arrays in geo-registry country index.json files.

For each sub_cluster, generates 3-8 typed nodes (Person, Institution,
EventWindow, Text, Idea, Movement) based on the sub_cluster's description,
key_events, and contextual era/theme data.

Usage:
    python3 scripts/populate_sub_cluster_nodes.py          # all countries
    python3 scripts/populate_sub_cluster_nodes.py germany   # single country
"""
import json
import os
import re
import sys
from datetime import datetime, timezone

BASE = os.path.join(os.path.dirname(__file__), '..', 'geo-registry', 'places', 'countries')

ERA_MAP = {
    '910': {'era': 'Prehistoric', 'eraSlug': 'prehistoric'},
    '920': {'era': 'Classical', 'eraSlug': 'classical'},
    '930': {'era': 'Medieval', 'eraSlug': 'medieval'},
    '940': {'era': 'Early Modern', 'eraSlug': 'early-modern'},
    '950': {'era': 'Modern', 'eraSlug': 'modern'},
    '960': {'era': 'Contemporary', 'eraSlug': 'contemporary'},
}

# Division codes -> label + call-number prefix
LABEL_DIVISIONS = {
    'Person':       {'division': '220', 'heading': 'Political Leaders'},
    'Institution':  {'division': '310', 'heading': 'Political Institutions'},
    'EventWindow':  {'division': '530', 'heading': 'Elections & Political Shifts'},
    'Text':         {'division': '710', 'heading': 'Constitutions & Charters'},
    'Idea':         {'division': '010', 'heading': 'Political Systems & Governance'},
    'Movement':     {'division': '610', 'heading': 'Political Movements'},
}

# Keyword patterns for label classification
TEXT_KEYWORDS = re.compile(
    r'\b(treaty|act\b|constitution|charter|code|edict|decree|bull|encyclical|'
    r'manifesto|proclamation|bible|quran|torah|vedas|sutra|magna carta|book|'
    r'chronicle|manuscript|theses|declaration|statute|concordat|accord|'
    r'protocol|covenant|petition|bill of rights|law\b|document|writing|'
    r'scripture|text|canon|codex|commedia|gospel|epistle|commentary|novel|'
    r'compendium|encyclopedia|thesis|pamphlet|catechism)\b', re.I)

INSTITUTION_KEYWORDS = re.compile(
    r'\b(church|university|empire|dynasty|parliament|kingdom|caliphate|'
    r'republic|council|court|academy|senate|assembly|guild|order|'
    r'sultanate|confederation|league|diocese|monastery|papacy|'
    r'corporation|company|bank|stock exchange|mint|trading post|'
    r'federation|commonwealth|congress|cabinet|bureau|ministry|'
    r'commission|agency|tribunal|hospital|school|college|library|'
    r'museum|observatory|temple|mosque|synagogue|cathedral|vatican|'
    r'united nations|nato|eu\b|oas|asean|opec|imf|world bank|'
    r'red cross|amnesty|ngo|foundation|institute|society)\b', re.I)

MOVEMENT_KEYWORDS = re.compile(
    r'\b(movement|revolution|uprising|revolt|rebellion|reform|'
    r'renaissance|enlightenment|awakening|nationalism|communism|'
    r'socialism|fascism|liberalism|conservatism|imperialism|'
    r'colonialism|decolonization|independence|abolition|suffrage|'
    r'civil rights|anti-apartheid|resistance|intifada|'
    r'perestroika|glasnost|spring|miracle|boom|wave|crusade|'
    r'jihad|reconquista|reformation|counter-reformation)\b', re.I)

IDEA_KEYWORDS = re.compile(
    r'\b(philosophy|theory|concept|doctrine|ideology|system|'
    r'principle|paradigm|framework|model|school of thought|'
    r'democracy|monarchy|theocracy|feudal|mercantil|capitalism|'
    r'marxism|utilitarianism|rationalism|empiricism|pragmatism|'
    r'existentialism|humanism|positivism|structuralism|nihilism|'
    r'confucianism|taoism|buddhism|hinduism|islam|christianity|'
    r'animism|shamanism|zoroastrianism|divine right|mandate of heaven|'
    r'social contract|natural law|separation of powers|rule of law)\b', re.I)

PERSON_KEYWORDS = re.compile(
    r'\b(king|queen|emperor|empress|pharaoh|sultan|caliph|'
    r'pope|archbishop|bishop|cardinal|patriarch|imam|'
    r'president|prime minister|chancellor|dictator|general|'
    r'admiral|commander|warrior|conqueror|prophet|saint|'
    r'philosopher|scientist|inventor|explorer|navigator|'
    r'writer|artist|composer|poet|architect|scholar|'
    r'monk|missionary|reformer|revolutionary|activist|'
    r'governor|viceroy|chief|tribal leader|warlord|shogun|daimyo)\b', re.I)

WAR_KEYWORDS = re.compile(
    r'\b(war|battle|siege|invasion|conquest|campaign|'
    r'massacre|genocide|bombing|assassination|coup|'
    r'occupation|annexation|partition|blockade|embargo)\b', re.I)

RELIGION_KEYWORDS = re.compile(
    r'\b(church|mosque|temple|cathedral|monastery|religious|'
    r'christianity|islam|buddhism|hinduism|judaism|'
    r'pope|bishop|imam|priest|monk|missionary|'
    r'scripture|bible|quran|torah|sutra|vedas)\b', re.I)

SCIENCE_KEYWORDS = re.compile(
    r'\b(scientific|discovery|invention|technology|innovation|'
    r'astronomy|medicine|mathematics|physics|chemistry|'
    r'observatory|laboratory|vaccine|theory|experiment)\b', re.I)

# Refined division assignment based on content
def get_division(label, text):
    """Return a more specific division code based on content keywords."""
    if label == 'Person':
        if RELIGION_KEYWORDS.search(text):
            return '250'  # Religious Figures
        if SCIENCE_KEYWORDS.search(text):
            return '240'  # Scientists & Inventors
        if re.search(r'\b(artist|writer|poet|composer|architect|painter)\b', text, re.I):
            return '260'  # Artists & Writers
        if re.search(r'\b(activist|reformer|abolitionist|suffrag)\b', text, re.I):
            return '270'  # Activists & Reformers
        if re.search(r'\b(philosopher|thinker|scholar|intellectual)\b', text, re.I):
            return '210'  # Philosophers & Thinkers
        return '220'  # Political Leaders (default)
    if label == 'Institution':
        if RELIGION_KEYWORDS.search(text):
            return '340'  # Religious Institutions
        if SCIENCE_KEYWORDS.search(text):
            return '350'  # Scientific Institutions
        if re.search(r'\b(university|school|college|academy|library|museum)\b', text, re.I):
            return '360'  # Cultural Institutions
        if re.search(r'\b(bank|company|corporation|trading|guild|exchange)\b', text, re.I):
            return '330'  # Economic Institutions
        if re.search(r'\b(court|tribunal|legal|judiciary)\b', text, re.I):
            return '320'  # Legal Institutions
        if re.search(r'\b(army|military|navy|defence|defense)\b', text, re.I):
            return '390'  # Military
        if re.search(r'\b(united nations|nato|eu\b|oas|asean|imf|world bank|international)\b', text, re.I):
            return '370'  # International
        return '310'  # Political Institutions (default)
    if label == 'EventWindow':
        if WAR_KEYWORDS.search(text):
            return '510'  # Wars & Conflicts
        if re.search(r'\b(revolution|uprising|revolt|rebellion)\b', text, re.I):
            return '520'  # Revolutions & Uprisings
        if SCIENCE_KEYWORDS.search(text):
            return '550'  # Scientific Discoveries
        if RELIGION_KEYWORDS.search(text):
            return '570'  # Religious Events
        if re.search(r'\b(climate|earthquake|flood|drought|hurricane|tsunami|famine)\b', text, re.I):
            return '580'  # Environmental Events
        return '530'  # Elections & Political Shifts (default)
    if label == 'Text':
        if re.search(r'\b(constitution|charter|bill of rights)\b', text, re.I):
            return '710'  # Constitutions & Charters
        if re.search(r'\b(code|law|statute|edict|decree)\b', text, re.I):
            return '720'  # Legal Codes
        if RELIGION_KEYWORDS.search(text):
            return '730'  # Religious Texts
        if re.search(r'\b(philosophy|philosophical|meditations|critique)\b', text, re.I):
            return '740'  # Philosophical Works
        if SCIENCE_KEYWORDS.search(text):
            return '750'  # Scientific Texts
        return '710'  # Default
    if label == 'Movement':
        if RELIGION_KEYWORDS.search(text):
            return '630'  # Religious Movements
        if re.search(r'\b(art|literary|cultural|renaissance|romantic)\b', text, re.I):
            return '640'  # Cultural Movements
        if SCIENCE_KEYWORDS.search(text):
            return '650'  # Scientific Movements
        if re.search(r'\b(social|civil rights|suffrage|abolition|equity)\b', text, re.I):
            return '620'  # Social Movements
        if re.search(r'\b(environmental|green|climate|ecological)\b', text, re.I):
            return '670'  # Environmental Movements
        return '610'  # Political Movements (default)
    if label == 'Idea':
        if RELIGION_KEYWORDS.search(text):
            return '140'  # Religious & Philosophical Concepts
        if re.search(r'\b(economic|mercantil|capitalism|socialism|marxism|trade|market)\b', text, re.I):
            return '110'  # Economic Theories
        if SCIENCE_KEYWORDS.search(text):
            return '120'  # Scientific Paradigms
        if re.search(r'\b(social|cultural)\b', text, re.I):
            return '150'  # Social & Cultural Theories
        if re.search(r'\b(environment|ecological|climate)\b', text, re.I):
            return '160'  # Environmental Ideas
        return '010'  # Political Systems & Governance (default)
    return '530'


def slugify(text):
    """Convert text to lowercase slug."""
    s = re.sub(r'[^\w\s-]', '', text.lower().strip())
    s = re.sub(r'[\s_]+', '-', s)
    s = re.sub(r'-+', '-', s)
    return s.strip('-')[:80]


def classify_event(text):
    """Determine the best label for a key_event string."""
    # Prioritize: Text > Institution > Movement > Idea > EventWindow
    if TEXT_KEYWORDS.search(text):
        return 'Text'
    if INSTITUTION_KEYWORDS.search(text):
        return 'Institution'
    if MOVEMENT_KEYWORDS.search(text):
        return 'Movement'
    if IDEA_KEYWORDS.search(text):
        return 'Idea'
    return 'EventWindow'


def extract_year(text):
    """Extract a year from text like 'Treaty of Westphalia (1648)' or 'founded 1534'."""
    # Match patterns like (1648), (c. 1200 BC), (962 CE), etc.
    m = re.search(r'\((?:c\.?\s*)?(\d{3,4})\s*(?:BC|BCE|CE|AD)?\)', text)
    if m:
        year = int(m.group(1))
        if re.search(r'BC|BCE', text[m.start():m.end()]):
            year = -year
        return year
    # Match "in 1648", "year 1534"
    m = re.search(r'\b(\d{4})\b', text)
    if m:
        year = int(m.group(1))
        if year < 2100:
            return year
    m = re.search(r'\b(\d{3})\b', text)
    if m:
        val = int(m.group(1))
        if 100 <= val <= 999:
            return val
    return None


def extract_year_range(text, sc_year_range):
    """Extract [start, end] year range from text, falling back to sub_cluster range."""
    year = extract_year(text)
    if year is not None:
        # Approximate: event ± small window
        return [year, min(year + 20, sc_year_range[1])] if year < sc_year_range[1] else [year - 10, year]
    return list(sc_year_range)


def clean_node_name(name):
    """Clean up a node name — remove leading conjunctions, prepositions, fragments."""
    # Remove leading articles, conjunctions, prepositions
    name = re.sub(r'^(?:and|or|the|of|in|at|on|to|from|with|by|for|a|an)\s+',
                  '', name, flags=re.I).strip()
    # Remove trailing conjunctions/prepositions
    name = re.sub(r'\s+(?:and|or|the|of|in|at|on|to|from|with|by|for)$',
                  '', name, flags=re.I).strip()
    # Capitalize first letter
    if name and name[0].islower():
        name = name[0].upper() + name[1:]
    return name


def is_valid_node_name(name, label):
    """Check if a node name is meaningful enough to create."""
    if not name or len(name) < 3:
        return False
    # Too generic for standalone nodes
    generics = {'System', 'Reform', 'Movement', 'Revolution', 'Empire', 'Kingdom',
                'Dynasty', 'Republic', 'Church', 'Council', 'Court', 'War',
                'Treaty', 'Invasion', 'Battle', 'Miracle', 'Crisis'}
    if name in generics:
        return False
    # Sentence fragments start with lowercase
    if name[0].islower() and label != 'Idea':
        return False
    # Too long = probably a sentence fragment
    if len(name) > 80:
        return False
    # Should have at least one capital letter (proper noun)
    if label in ('Person', 'Institution', 'Text') and not any(c.isupper() for c in name):
        return False
    return True


def make_node(slug, name, label, description, year_range, division=None, extra_text=''):
    """Create a node dict."""
    name = clean_node_name(name)
    if not is_valid_node_name(name, label):
        return None
    slug = slugify(name)
    if not slug:
        return None
    combined_text = f'{description} {extra_text}'
    div = division or get_division(label, combined_text)
    return {
        'slug': slug,
        'name': name,
        'label': label,
        'call_number': f'{div}.{slug[:40]}',
        'description': description[:300],
        'year_range': year_range,
        'status': 'PLANNED',
    }


def generate_nodes_for_sub_cluster(sc, era_code, country_name, continent, region):
    """Generate a list of typed nodes for a sub_cluster."""
    nodes = []
    seen_slugs = set()
    desc = sc.get('description', '')
    key_events = sc.get('key_events', [])
    yr = sc.get('year_range', [0, 0])
    sc_name = sc.get('name', '')
    combined_text = f'{sc_name} {desc} {" ".join(key_events)}'

    def _add(node):
        if node and node['slug'] not in seen_slugs:
            seen_slugs.add(node['slug'])
            nodes.append(node)

    # 1) Generate nodes from key_events
    for ke in key_events:
        # Clean up slug-style events like "Jamestown_Founded_1607"
        if '_' in ke and ' ' not in ke:
            clean_name = ke.replace('_', ' ')
        else:
            clean_name = ke

        # Remove year parenthetical for name
        display_name = re.sub(r'\s*\([^)]*\d{3,4}[^)]*\)\s*$', '', clean_name).strip()
        # Remove trailing dates like "– 962 CE"
        display_name = re.sub(r'\s*[–—-]\s*\d{3,4}\s*(?:BC|BCE|CE|AD)?\s*$', '', display_name).strip()
        if len(display_name) > 100:
            display_name = display_name[:97] + '...'

        label = classify_event(ke)
        event_yr = extract_year_range(ke, yr)
        div = get_division(label, ke)

        _add(make_node(
            slug=slugify(display_name),
            name=display_name,
            label=label,
            description=ke if ke != display_name else f'{display_name} — {country_name}',
            year_range=event_yr,
            division=div,
            extra_text=ke,
        ))

    # 2) Extract named entities from description

    # Institution extraction — look for proper-noun institutions
    for inst_name in _extract_institutions_from_text(desc):
        div = get_division('Institution', inst_name)
        _add(make_node(
            slug=slugify(inst_name),
            name=inst_name,
            label='Institution',
            description=f'{inst_name} — institution in {country_name}',
            year_range=list(yr),
            division=div,
            extra_text=desc,
        ))

    # Text extraction — look for named documents/treaties/texts
    for text_name in _extract_texts_from_text(desc):
        div = get_division('Text', text_name)
        _add(make_node(
            slug=slugify(text_name),
            name=text_name,
            label='Text',
            description=f'{text_name} — document related to {country_name}',
            year_range=list(yr),
            division=div,
            extra_text=desc,
        ))

    # Movement extraction — look for named movements
    for mov_name in _extract_movements_from_text(desc, sc_name):
        div = get_division('Movement', mov_name)
        _add(make_node(
            slug=slugify(mov_name),
            name=mov_name,
            label='Movement',
            description=f'{mov_name} in {country_name}',
            year_range=list(yr),
            division=div,
            extra_text=desc,
        ))

    # Idea extraction — look for named ideological concepts
    for idea_name in _extract_ideas_from_text(desc, sc_name):
        div = get_division('Idea', idea_name)
        _add(make_node(
            slug=slugify(idea_name),
            name=idea_name,
            label='Idea',
            description=f'{idea_name} — concept in {country_name}',
            year_range=list(yr),
            division=div,
            extra_text=desc,
        ))

    # 3) If we still have fewer than 2 nodes, add the sub_cluster itself as EventWindow
    if len(nodes) < 2:
        div = get_division('EventWindow', combined_text)
        _add(make_node(
            slug=slugify(sc_name),
            name=sc_name,
            label='EventWindow',
            description=desc[:300] if desc else f'{sc_name} — {country_name}',
            year_range=list(yr),
            division=div,
            extra_text=combined_text,
        ))

    # 4) Person extraction from description
    if not any(n['label'] == 'Person' for n in nodes):
        person_name = _extract_person_from_text(desc)
        if person_name:
            div = get_division('Person', desc)
            _add(make_node(
                slug=slugify(person_name),
                name=person_name,
                label='Person',
                description=f'{person_name} — historical figure of {country_name}',
                year_range=list(yr),
                division=div,
                extra_text=desc,
            ))

    return nodes


def _extract_institutions_from_text(text):
    """Extract properly-named institutions from text."""
    results = []
    # Pattern: "the X Empire", "X Dynasty", "Ottoman Empire", "Schmalkaldic League"
    patterns = [
        r'(?:the\s+)?([A-Z][\w\'-]+(?:\s+(?:of\s+)?[A-Z][\w\'-]+)*\s+(?:Empire|Dynasty|Kingdom|Republic|Confederation|League|Parliament|Court|Academy|University|Caliphate|Sultanate|Federation|Commonwealth|Congress|Senate|Assembly|Company|Church|Papacy|Patriarchate|Order|Guild|Bank|Mint|Monastery))',
        r'(?:the\s+)?((?:Holy\s+)?Roman\s+Empire|British\s+Parliament|East\s+India\s+Company|Dutch\s+East\s+India\s+Company|Hanseatic\s+League|Schmalkaldic\s+League|Grand\s+National\s+Assembly|Ottoman\s+Porte)',
    ]
    for pat in patterns:
        for m in re.finditer(pat, text):
            name = m.group(1).strip()
            if 4 < len(name) < 80:
                results.append(name)
    return results[:3]


def _extract_texts_from_text(text):
    """Extract named documents/treaties/texts from text."""
    results = []
    patterns = [
        # "Treaty of Westphalia", "Act of Supremacy", "Magna Carta"
        r'(?:the\s+)?([A-Z][\w\'-]+(?:\s+(?:of|de|di)\s+)?[\w\'-]+(?:\s+[\w\'-]+)*?\s+(?:Treaty|Act|Constitution|Charter|Code|Edict|Decree|Bull|Manifesto|Proclamation|Declaration|Statute|Concordat|Accord|Protocol|Covenant|Petition|Catechism|Theses))',
        r'(?:the\s+)?(Treaty\s+of\s+[A-Z][\w\'-]+(?:\s+[A-Z][\w\'-]+)*)',
        r'(?:the\s+)?(Act\s+of\s+[A-Z][\w\'-]+(?:\s+[A-Z][\w\'-]+)*)',
        r'(?:the\s+)?(Peace\s+of\s+[A-Z][\w\'-]+)',
        r'(?:the\s+)?(Edict\s+of\s+[A-Z][\w\'-]+)',
        r'(?:the\s+)?((?:Magna\s+Carta|Golden\s+Bull|Domesday\s+Book|Basic\s+Law|Bill\s+of\s+Rights|95\s+Theses|Enabling\s+Act|Basic\s+Treaty|Two\s+Plus\s+Four\s+Treaty))',
    ]
    for pat in patterns:
        for m in re.finditer(pat, text):
            name = m.group(1).strip()
            if 4 < len(name) < 80:
                results.append(name)
    return results[:2]


def _extract_movements_from_text(text, sc_name=''):
    """Extract named movements from text."""
    results = []
    patterns = [
        # "Protestant Reformation", "French Revolution", "Enlightenment"
        r'(?:the\s+)?([A-Z][\w\'-]+(?:\s+[A-Z][\w\'-]+)*\s+(?:Reformation|Revolution|Revolt|Uprising|Rebellion|Renaissance|Enlightenment|Awakening|Movement|Crusade|Reconquista|Intifada|Spring))',
        r'(?:the\s+)?((?:Decolonization|Nationalis[mt]|Abolitionist?\s+Movement|Suffrage\s+Movement|Civil\s+Rights\s+Movement|Anti-Apartheid\s+Movement|Pan-Africanism|Pan-Arabism|Zionism|Perestroika|Glasnost|Kulturkampf|Wirtschaftswunder))',
    ]
    for pat in patterns:
        for m in re.finditer(pat, text):
            name = m.group(1).strip()
            if 4 < len(name) < 80:
                results.append(name)

    # Also extract from sc_name if it mentions a movement
    if not results and MOVEMENT_KEYWORDS.search(sc_name):
        results.append(sc_name)

    return results[:2]


def _extract_ideas_from_text(text, sc_name=''):
    """Extract named ideological concepts from text."""
    results = []
    patterns = [
        r'(?:the\s+)?((?:Divine\s+Right|Mandate\s+of\s+Heaven|Social\s+Contract|Natural\s+Law|Separation\s+of\s+Powers|Rule\s+of\s+Law|Popular\s+Sovereignty|Manifest\s+Destiny))',
        r'(?:the\s+)?([A-Z][\w\'-]+(?:\s+[A-Z][\w\'-]+)*\s+(?:Doctrine|Philosophy|Ideology|System|Principle|Theory|Paradigm|Concept))',
    ]
    for pat in patterns:
        for m in re.finditer(pat, text):
            name = m.group(1).strip()
            if 4 < len(name) < 80:
                results.append(name)
    return results[:1]


def _extract_person_from_text(text):
    """Try to extract a person name from description text."""
    # Pattern: Capitalized Name (with optional "the Great", "I", "II", etc.)
    patterns = [
        # "Alexander the Great", "Frederick II"
        r'\b([A-Z][a-z]+(?:\s+(?:the\s+)?[A-Z][a-z]+){0,3}(?:\s+[IVX]{1,4})?)\b'
        r'(?:\s*(?:\'s|\'|\u2019s)?\s*(?:rule|reign|campaign|empire|kingdom|dynasty|invasion|conquest|reform|revolt))',
        # "King Henry VIII", "Emperor Justinian"
        r'\b(?:King|Queen|Emperor|Empress|Pharaoh|Sultan|Pope|Saint|Sir|Lord|General|Admiral|President|PM|Chancellor)\s+'
        r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,2}(?:\s+[IVX]{1,4})?)\b',
        # Simple: Two-word capitalized name followed by action verb
        r'\b([A-Z][a-z]{2,}(?:\s+(?:de\s+|von\s+|al-|el-|ibn\s+)?[A-Z][a-z]{2,}){1,2})\b'
        r'(?:\s+(?:led|ruled|founded|established|built|conquered|unified|defeated|proclaimed|created|wrote|published))',
    ]
    for pat in patterns:
        m = re.search(pat, text)
        if m:
            name = m.group(1).strip()
            # Filter out common non-person phrases
            skip = {'Roman Empire', 'Holy Roman', 'Ottoman Empire', 'Persian Empire',
                    'British Empire', 'Dutch East', 'East India', 'West Africa',
                    'North America', 'South America', 'New World', 'Old World',
                    'Middle East', 'Central Asia', 'World War', 'Cold War',
                    'First World', 'Second World', 'Third World', 'New Zealand',
                    'United States', 'United Kingdom', 'Saudi Arabia', 'South Africa',
                    'North Korea', 'South Korea', 'Sri Lanka', 'Costa Rica',
                    'Sierra Leone', 'Puerto Rico', 'Blitzkrieg', 'Holocaust',
                    'Renaissance', 'Enlightenment', 'Reformation', 'Crusade',
                    'Reconquista', 'Apartheid', 'Perestroika', 'Glasnost',
                    'Great Depression', 'Industrial Revolution', 'Iron Curtain',
                    'Berlin Wall', 'Silk Road', 'Scramble for Africa',
                    'Marshall Plan', 'New Deal', 'Arab Spring', 'World Bank',
                    'World Trade', 'Red Cross', 'Nobel Prize'}
            if name in skip or len(name) < 4:
                continue
            return name
    return None


def process_country(country_slug):
    """Process a single country, populating nodes in all sub_clusters."""
    fp = os.path.join(BASE, country_slug, 'index.json')
    if not os.path.isfile(fp):
        print(f'  SKIP {country_slug}: no index.json')
        return 0

    with open(fp, 'r', encoding='utf-8') as f:
        data = json.load(f)

    meta = data.get('_meta', {})
    country_name = meta.get('country_name', country_slug.replace('-', ' ').title())
    continent = meta.get('continent', '')
    region = meta.get('region', '')

    tc = data.get('thematic_clusters', {})
    total_new = 0

    for era_code, clusters in tc.items():
        for cluster in clusters:
            for sc in cluster.get('sub_clusters', []):
                existing = sc.get('nodes', [])
                if existing:
                    continue  # Don't overwrite existing nodes

                new_nodes = generate_nodes_for_sub_cluster(
                    sc, era_code, country_name, continent, region
                )
                sc['nodes'] = new_nodes
                total_new += len(new_nodes)

    # Update statistics
    stats = data.get('statistics', {})
    all_nodes = []
    for era_code, clusters in tc.items():
        for cluster in clusters:
            for sc in cluster.get('sub_clusters', []):
                all_nodes.extend(sc.get('nodes', []))
    stats['total_nodes'] = len(all_nodes)
    label_counts = {}
    for n in all_nodes:
        lbl = n.get('label', 'Unknown')
        label_counts[lbl] = label_counts.get(lbl, 0) + 1
    stats['nodes_by_label'] = label_counts
    stats['last_enriched'] = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    data['statistics'] = stats

    with open(fp, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return total_new


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else None

    if target:
        countries = [target]
    else:
        countries = sorted(d for d in os.listdir(BASE)
                           if os.path.isdir(os.path.join(BASE, d)) and d != '_template')

    grand_total = 0
    for i, slug in enumerate(countries, 1):
        count = process_country(slug)
        grand_total += count
        if i % 20 == 0 or i == len(countries):
            print(f'  [{i}/{len(countries)}] {slug}: +{count} nodes (running total: {grand_total})')

    print(f'\nDone. Generated {grand_total} nodes across {len(countries)} countries.')


if __name__ == '__main__':
    main()
