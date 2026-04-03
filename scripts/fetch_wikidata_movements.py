#!/usr/bin/env python3
"""
fetch_wikidata_movements.py  (v3.0)

Comprehensive Wikidata fetch of movements across ALL Class 6 divisions
(610-683).  Uses instantiable Wikidata types (social movement, political
movement, art movement, political party, trade union, denomination, etc.)
then refines divisions via keyword matching on names/descriptions.

Avoids concept-level QIDs (anarchism, marxism, fascism, etc.) that are
never used as P31 types in Wikidata and cause expensive timeout failures.

v3 fixes: fast-fail retry logic, progressive saving, removed redundant
art-style subclass batches, added resistance/student/peace/reform types.

Output: data/wikidata_movements.json

Usage:
    python3 scripts/fetch_wikidata_movements.py
    python3 scripts/fetch_wikidata_movements.py --limit 5000
    python3 scripts/fetch_wikidata_movements.py --dry-run
"""

import argparse
import json
import re
import time
from pathlib import Path
from typing import Any

import requests

# ── Wikidata SPARQL endpoint ──
SPARQL_ENDPOINT = "https://query.wikidata.org/sparql"
USER_AGENT = (
    "AnnalsOfTheWorld/2.0 "
    "(https://github.com/annals-of-the-world; contact@annals.dev)"
)

# ═══════════════════════════════════════════════════════════════════
# Movement Type -> Division Mapping  (instantiable types ONLY)
# Maps Wikidata P31 QIDs to default call-number divisions.
# Keyword refinement post-assigns more specific divisions.
# ═══════════════════════════════════════════════════════════════════

MOVEMENT_TYPE_MAP: dict[str, tuple[str, str]] = {
    # ── Broad movement types (instantiable) ──
    "Q49773":     ("610", "Political Movements"),                  # political movement
    "Q2198855":   ("620", "Social Movements"),                     # social movement
    "Q5398426":   ("630", "Religious Movements"),                  # religious movement
    "Q58947":     ("640", "Cultural Movements"),                   # cultural movement
    "Q968159":    ("640", "Cultural Movements"),                   # intellectual movement
    "Q15936437":  ("640", "Cultural Movements"),                   # philosophical movement
    "Q3533467":   ("644", "Modernist & Avant-Garde Movements"),    # art movement
    "Q1266946":   ("644", "Modernist & Avant-Garde Movements"),    # literary movement
    "Q2738074":   ("620", "Social Movements"),                     # protest movement
    "Q1127759":   ("640", "Cultural Movements"),                   # cultural trend
    "Q101789024": ("670", "Environmental Movements"),              # environmental movement
    "Q178790":    ("624", "Labor & Workers' Rights"),              # labor movement
    "Q472311":    ("662", "Digital Revolution & Internet"),         # free software movement

    # ── Resistance / reform / peace (instantiable) ──
    "Q189833":    ("612", "Anti-Colonial & Decolonization"),       # resistance movement
    "Q45529":     ("620", "Social Movements"),                     # student movement
    "Q1781513":   ("620", "Social Movements"),                     # reform movement
    "Q83267":     ("620", "Social Movements"),                     # peace movement
    "Q3918409":   ("640", "Cultural Movements"),                   # school of thought
    "Q4504495":   ("644", "Modernist & Avant-Garde Movements"),    # school of painting
    "Q891723":    ("623", "Civil Rights & Racial Justice"),        # human rights movement -- REMOVED from batches (too polluted)

    # ── Political organizations (instantiable) ──
    "Q7278":      ("610", "Political Movements"),                  # political party
    "Q4358176":   ("610", "Political Movements"),                  # political organization
    "Q1153773":   ("610", "Political Movements"),                  # political faction

    # ── Liberation / independence (instantiable) ──
    "Q6501349":   ("611", "Nationalism & Nation-Building"),         # national liberation movement
    "Q1195942":   ("611", "Nationalism & Nation-Building"),         # national awakening

    # ── Labor (instantiable) ──
    "Q178706":    ("624", "Labor & Workers' Rights"),              # trade union
    "Q484652":    ("624", "Labor & Workers' Rights"),              # labor union
    "Q13417250":  ("624", "Labor & Workers' Rights"),              # trade union federation

    # ── Religious (instantiable) ──
    "Q193622":    ("630", "Religious Movements"),                  # religious denomination
    "Q879146":    ("631", "Protestant Reformation"),               # Christian denomination
    "Q1530022":   ("630", "Religious Movements"),                  # religious order
    "Q465603":    ("635", "New Religious Movements"),              # new religious movement
    "Q23955":     ("630", "Religious Movements"),                  # Christianity sect
    "Q1480166":   ("634", "Missionary & Evangelical Movements"),   # Christian mission

    # ── Art styles (instantiable as art movement subclasses) ──
    "Q166713":    ("644", "Modernist & Avant-Garde Movements"),    # surrealism
    "Q171379":    ("644", "Modernist & Avant-Garde Movements"),    # impressionism
    "Q40415":     ("644", "Modernist & Avant-Garde Movements"),    # expressionism
    "Q134560":    ("644", "Modernist & Avant-Garde Movements"),    # cubism
    "Q170292":    ("644", "Modernist & Avant-Garde Movements"),    # futurism (art)
    "Q34636":     ("644", "Modernist & Avant-Garde Movements"),    # constructivism
    "Q192612":    ("644", "Modernist & Avant-Garde Movements"),    # Art Nouveau
    "Q46805":     ("644", "Modernist & Avant-Garde Movements"),    # Art Deco
    "Q474263":    ("644", "Modernist & Avant-Garde Movements"),    # abstract expressionism
    "Q204820":    ("644", "Modernist & Avant-Garde Movements"),    # pop art
    "Q134165":    ("644", "Modernist & Avant-Garde Movements"),    # minimalism
    "Q157607":    ("644", "Modernist & Avant-Garde Movements"),    # realism
    "Q180089":    ("644", "Modernist & Avant-Garde Movements"),    # symbolism
    "Q8242":      ("644", "Modernist & Avant-Garde Movements"),    # Baroque
    "Q39631":     ("644", "Modernist & Avant-Garde Movements"),    # modernism
    "Q6034":      ("644", "Modernist & Avant-Garde Movements"),    # Dadaism
    "Q192517":    ("644", "Modernist & Avant-Garde Movements"),    # postmodernism
    "Q193563":    ("644", "Modernist & Avant-Garde Movements"),    # avant-garde
    "Q106043":    ("644", "Modernist & Avant-Garde Movements"),    # naturalism
    "Q134147":    ("644", "Modernist & Avant-Garde Movements"),    # Bauhaus
    "Q37068":     ("643", "Romanticism & Transcendentalism"),      # Romanticism

    # ── Scientific (instantiable) ──
    "Q11862829":  ("650", "Scientific Movements"),                 # academic discipline

    # ── Language (instantiable) ──
    "Q14819852":  ("645", "Vernacular & Language Movements"),      # language revival
}

# Build reverse lookup
QID_TO_DIVISION: dict[str, tuple[str, str]] = {}
for _qid, _div_info in MOVEMENT_TYPE_MAP.items():
    if _qid not in QID_TO_DIVISION:
        QID_TO_DIVISION[_qid] = _div_info

# ═══════════════════════════════════════════════════════════════════
# Keyword -> Division refinement rules
# Applied to name + description to assign specific divisions
# ═══════════════════════════════════════════════════════════════════

KEYWORD_DIVISION_RULES: list[tuple[list[str], str, str]] = [
    # 611 Nationalism
    (["nationalist", "nationalism", "nation-building", "national identity",
      "national self-determination", "irredentis", "separatist", "secessionist"],
     "611", "Nationalism & Nation-Building"),
    # 616 Pan-Movements (check before 611)
    (["pan-african", "pan-arab", "pan-slav", "pan-german", "pan-turk",
      "pan-islam", "pan-european", "pan-american"],
     "616", "Pan-Movements"),
    # 612 Anti-Colonial
    (["anti-colonial", "anticolonial", "decoloniz", "anti-imperial",
      "independence movement", "liberation movement", "freedom movement"],
     "612", "Anti-Colonial & Decolonization"),
    # 613 Communism & Socialism
    (["communist", "communism", "socialist", "socialism", "marxist",
      "marxism", "leninist", "leninism", "trotskyist", "maoist",
      "bolshevik", "anarchist", "anarchism", "anarcho", "syndicalist"],
     "613", "Communism & Socialism"),
    # 614 Fascism
    (["fascist", "fascism", "nazi", "nazism", "national socialist",
      "falangist", "totalitarian", "neo-fascist", "neofascist"],
     "614", "Fascism & Totalitarianism"),
    # 615 Liberalism
    (["liberal", "liberalism", "constitutionalist", "constitutionalism",
      "conservative", "conservatism", "libertarian", "neoliberal",
      "whig", "democratic party", "republican party"],
     "615", "Liberalism & Constitutionalism"),
    # 621 Abolition
    (["abolitio", "anti-slavery", "antislavery", "emancipation"],
     "621", "Abolition & Anti-Slavery"),
    # 622 Feminism
    (["feminist", "feminism", "suffrage", "women's rights",
      "women's movement", "suffragette", "gender equality"],
     "622", "Women's Suffrage & Feminism"),
    # 623 Civil Rights
    (["civil rights", "racial justice", "anti-racism", "antiracism",
      "black power", "anti-apartheid", "desegregation", "naacp"],
     "623", "Civil Rights & Racial Justice"),
    # 624 Labor
    (["labor movement", "labour movement", "trade union", "workers'",
      "working class", "syndicalism"],
     "624", "Labor & Workers' Rights"),
    # 625 LGBTQ+
    (["lgbt", "lgbtq", "gay rights", "same-sex", "queer",
      "homosexual rights", "pride movement", "stonewall"],
     "625", "LGBTQ+ Rights"),
    # 626 Disability
    (["disability rights", "disabled", "accessibility movement"],
     "626", "Disability Rights & Inclusion"),
    # 631 Protestant Reformation
    (["protestant", "lutheran", "calvinist", "methodist", "baptist",
      "presbyterian", "quaker", "mennonite", "anabaptist", "puritan",
      "huguenot"],
     "631", "Protestant Reformation"),
    # 632 Counter-Reformation
    (["counter-reformation", "jesuit", "tridentine", "catholic reform",
      "catholic revival"],
     "632", "Counter-Reformation & Catholic Revival"),
    # 633 Islamic Reform
    (["salafi", "wahhabi", "sufi", "sunni", "shia", "shi'a", "shiite",
      "islamic reform", "islamic revival", "islamist", "muslim brotherhood"],
     "633", "Islamic Reform & Revival"),
    # 634 Missionary
    (["missionary", "evangelism", "evangelical", "pentecostal",
      "christian mission", "gospel"],
     "634", "Missionary & Evangelical Movements"),
    # 635 New Religious
    (["new religious", "mormon", "latter-day", "bahá'í", "bahai",
      "scientolog", "unification church", "hare krishna", "raelian",
      "neo-pagan", "wicca", "sikh"],
     "635", "New Religious Movements"),
    # 641 Renaissance
    (["renaissance", "humanism", "humanist"],
     "641", "Renaissance & Humanism"),
    # 642 Enlightenment
    (["enlightenment", "rationalism", "rationalist", "empiricis",
      "positivis", "deism", "deist", "secularism", "secular"],
     "642", "Enlightenment & Rationalism"),
    # 643 Romanticism
    (["romantic", "romanticism", "transcendental"],
     "643", "Romanticism & Transcendentalism"),
    # 645 Language
    (["language movement", "language revival", "vernacular",
      "linguistic", "gaelic revival", "hebrew revival"],
     "645", "Vernacular & Language Movements"),
    # 651 Scientific Revolution
    (["scientific revolution", "paradigm shift", "copernican"],
     "651", "Scientific Revolution"),
    # 660 Technological
    (["technological", "mechanization", "automation"],
     "660", "Technological Movements"),
    # 661 Industrial
    (["industrial revolution", "industrializ"],
     "661", "Industrial Revolution"),
    # 662 Digital
    (["digital", "internet", "cyber", "open source", "open-source",
      "free software", "hacker", "cypherpunk"],
     "662", "Digital Revolution & Internet"),
    # 663 Green Tech
    (["renewable energy", "green tech", "sustainable", "solar energy",
      "wind energy", "clean energy"],
     "663", "Green Technology & Renewables"),
    # 670 Environmental
    (["environmental", "ecolog", "green movement", "earth day"],
     "670", "Environmental Movements"),
    # 671 Conservation
    (["conservation", "wilderness", "national park", "wildlife preserv"],
     "671", "Conservation & Wilderness Preservation"),
    # 672 Climate
    (["climate", "global warming", "carbon", "net zero",
      "fridays for future", "extinction rebellion"],
     "672", "Climate Action & Sustainability"),
    # 673 Animal Rights
    (["animal rights", "animal welfare", "vegan", "vegetarian",
      "anti-vivisection"],
     "673", "Animal Rights & Wildlife Protection"),
    # 680 Trade
    (["trade", "mercantil", "free trade", "protectionism"],
     "680", "Trade & Navigation Movements"),
    # 681 Silk Road
    (["silk road", "overland trade", "caravan"],
     "681", "Silk Road & Overland Trade"),
    # 682 Maritime
    (["maritime trade", "age of sail", "naval trade", "east india"],
     "682", "Maritime Trade & Age of Sail"),
    # 683 Globalization
    (["globaliz", "anti-globaliz", "alter-globaliz", "world trade"],
     "683", "Globalization & Free Trade"),
    # 652 Empiricism
    (["empiricis", "positivis", "logical positivis"],
     "652", "Empiricism & Positivism"),
    # 653 Open Science
    (["open science", "peer review", "open access", "open data"],
     "653", "Open Science & Peer Review"),
]

# ═══════════════════════════════════════════════════════════════════
# Batched SPARQL queries  (35 focused batches, instantiable types)
# Each batch -> (QIDs, min_sitelinks, use_subclass)
# ═══════════════════════════════════════════════════════════════════

MOVEMENT_QUERIES: dict[str, tuple] = {
    # ── Broad movement types ──
    "610_political_mov":  (["Q49773"], 3, False),                   # political movement
    "610_party":          (["Q7278"], 10, False),                   # political party
    "610_pol_org":        (["Q4358176", "Q1153773"], 5, False),     # political org/faction

    "611_liberation":     (["Q6501349"], 3, False),                 # national liberation movement
    "611_awakening":      (["Q1195942"], 3, False),                 # national awakening

    "620_social_mov":     (["Q2198855"], 3, False),                 # social movement
    "620_protest_mov":    (["Q2738074"], 3, False),                 # protest movement

    "624_labor_mov":      (["Q178790"], 3, False),                  # labor movement
    "624_trade_union":    (["Q178706"], 8, False),                  # trade union
    "624_labor_union":    (["Q484652"], 8, False),                  # labor union
    "624_union_fed":      (["Q13417250"], 5, False),                # trade union federation

    "630_religious_mov":  (["Q5398426"], 3, False),                 # religious movement
    "630_denomination":   (["Q193622"], 5, False),                  # religious denomination
    "630_chr_denom":      (["Q879146"], 5, False),                  # Christian denomination
    "630_order":          (["Q1530022"], 5, False),                 # religious order
    "630_sect":           (["Q23955"], 3, False),                   # Christianity sect
    "634_mission":        (["Q1480166"], 3, False),                 # Christian mission
    "635_nrm":            (["Q465603"], 3, False),                  # new religious movement

    "640_cultural_mov":   (["Q58947"], 3, False),                   # cultural movement
    "640_intellectual":   (["Q968159"], 3, False),                  # intellectual movement
    "640_philosophical":  (["Q15936437"], 3, False),                # philosophical movement

    "644_art_mov":        (["Q3533467"], 3, True),                  # art movement + subclasses
    "644_literary_mov":   (["Q1266946"], 3, True),                  # literary movement + subclasses

    "645_lang_revival":   (["Q14819852"], 3, False),                # language revival

    "650_discipline":     (["Q11862829"], 15, False),               # academic discipline

    "662_foss":           (["Q472311"], 3, False),                  # free software movement

    "670_env_mov":        (["Q101789024"], 3, False),               # environmental movement

    # ── Resistance / student / peace / reform (all instantiable) ──
    "612_resistance":     (["Q189833"], 3, False),                  # resistance movement
    "620_student":        (["Q45529"], 3, False),                   # student movement
    "620_reform":         (["Q1781513"], 3, False),                 # reform movement
    "620_peace":          (["Q83267"], 3, False),                   # peace movement
    "623_human_rights":   (["Q891723"], 30, False),                 # human rights movement (high sitelink filter)
    "640_school":         (["Q3918409"], 8, False),                 # school of thought
    "644_painting":       (["Q4504495"], 3, False),                 # school of painting
}

# ═══════════════════════════════════════════════════════════════════
# Country / Region / Continent mapping
# ═══════════════════════════════════════════════════════════════════

COUNTRY_INFO: dict[str, tuple[str, str, str]] = {
    "Q30":    ("United States", "North America", "Americas"),
    "Q145":   ("United Kingdom", "Northern Europe", "Europe"),
    "Q142":   ("France", "Western Europe", "Europe"),
    "Q183":   ("Germany", "Western Europe", "Europe"),
    "Q38":    ("Italy", "Southern Europe", "Europe"),
    "Q29":    ("Spain", "Southern Europe", "Europe"),
    "Q159":   ("Russia", "Eastern Europe", "Europe"),
    "Q148":   ("China", "East Asia", "Asia"),
    "Q668":   ("India", "South Asia", "Asia"),
    "Q17":    ("Japan", "East Asia", "Asia"),
    "Q884":   ("South Korea", "East Asia", "Asia"),
    "Q39":    ("Switzerland", "Western Europe", "Europe"),
    "Q40":    ("Austria", "Western Europe", "Europe"),
    "Q55":    ("Netherlands", "Western Europe", "Europe"),
    "Q36":    ("Poland", "Eastern Europe", "Europe"),
    "Q37":    ("Lithuania", "Northern Europe", "Europe"),
    "Q41":    ("Greece", "Southern Europe", "Europe"),
    "Q20":    ("Norway", "Northern Europe", "Europe"),
    "Q34":    ("Sweden", "Northern Europe", "Europe"),
    "Q35":    ("Denmark", "Northern Europe", "Europe"),
    "Q31":    ("Belgium", "Western Europe", "Europe"),
    "Q16":    ("Canada", "North America", "Americas"),
    "Q96":    ("Mexico", "Central America", "Americas"),
    "Q155":   ("Brazil", "South America", "Americas"),
    "Q414":   ("Argentina", "South America", "Americas"),
    "Q298":   ("Chile", "South America", "Americas"),
    "Q739":   ("Colombia", "South America", "Americas"),
    "Q45":    ("Portugal", "Southern Europe", "Europe"),
    "Q408":   ("Australia", "Oceania", "Oceania"),
    "Q664":   ("New Zealand", "Oceania", "Oceania"),
    "Q79":    ("Egypt", "North Africa", "Africa"),
    "Q262":   ("Algeria", "North Africa", "Africa"),
    "Q1028":  ("Morocco", "North Africa", "Africa"),
    "Q115":   ("Ethiopia", "East Africa", "Africa"),
    "Q1033":  ("Nigeria", "West Africa", "Africa"),
    "Q929":   ("Central African Republic", "Central Africa", "Africa"),
    "Q258":   ("South Africa", "Southern Africa", "Africa"),
    "Q794":   ("Iran", "West Asia", "Asia"),
    "Q796":   ("Iraq", "West Asia", "Asia"),
    "Q801":   ("Israel", "West Asia", "Asia"),
    "Q843":   ("Pakistan", "South Asia", "Asia"),
    "Q837":   ("Nepal", "South Asia", "Asia"),
    "Q869":   ("Thailand", "Southeast Asia", "Asia"),
    "Q865":   ("Taiwan", "East Asia", "Asia"),
    "Q423":   ("North Korea", "East Asia", "Asia"),
    "Q881":   ("Vietnam", "Southeast Asia", "Asia"),
    "Q334":   ("Singapore", "Southeast Asia", "Asia"),
    "Q833":   ("Malaysia", "Southeast Asia", "Asia"),
    "Q252":   ("Indonesia", "Southeast Asia", "Asia"),
    "Q928":   ("Philippines", "Southeast Asia", "Asia"),
    "Q854":   ("Sri Lanka", "South Asia", "Asia"),
    "Q817":   ("Kuwait", "West Asia", "Asia"),
    "Q846":   ("Qatar", "West Asia", "Asia"),
    "Q878":   ("United Arab Emirates", "West Asia", "Asia"),
    "Q874":   ("Turkmenistan", "Central Asia", "Asia"),
    "Q889":   ("Afghanistan", "South Asia", "Asia"),
    "Q184":   ("Belarus", "Eastern Europe", "Europe"),
    "Q212":   ("Ukraine", "Eastern Europe", "Europe"),
    "Q213":   ("Czech Republic", "Eastern Europe", "Europe"),
    "Q214":   ("Slovakia", "Eastern Europe", "Europe"),
    "Q28":    ("Hungary", "Eastern Europe", "Europe"),
    "Q218":   ("Romania", "Eastern Europe", "Europe"),
    "Q219":   ("Bulgaria", "Eastern Europe", "Europe"),
    "Q215":   ("Slovenia", "Southern Europe", "Europe"),
    "Q224":   ("Croatia", "Southern Europe", "Europe"),
    "Q225":   ("Bosnia and Herzegovina", "Southern Europe", "Europe"),
    "Q117":   ("Ghana", "West Africa", "Africa"),
    "Q114":   ("Kenya", "East Africa", "Africa"),
    "Q1032":  ("Niger", "West Africa", "Africa"),
    "Q912":   ("Mali", "West Africa", "Africa"),
    "Q657":   ("Chad", "Central Africa", "Africa"),
    "Q1005":  ("Gambia", "West Africa", "Africa"),
    "Q27":    ("Ireland", "Northern Europe", "Europe"),
    "Q33":    ("Finland", "Northern Europe", "Europe"),
    "Q32":    ("Luxembourg", "Western Europe", "Europe"),
    "Q189":   ("Iceland", "Northern Europe", "Europe"),
    "Q842":   ("Oman", "West Asia", "Asia"),
    "Q810":   ("Jordan", "West Asia", "Asia"),
    "Q805":   ("Yemen", "West Asia", "Asia"),
    "Q851":   ("Saudi Arabia", "West Asia", "Asia"),
    "Q43":    ("Turkey", "West Asia", "Asia"),
    "Q965":   ("Burkina Faso", "West Africa", "Africa"),
    "Q1011":  ("Cape Verde", "West Africa", "Africa"),
    "Q1029":  ("Mozambique", "East Africa", "Africa"),
    "Q1030":  ("Namibia", "Southern Africa", "Africa"),
    "Q1044":  ("Sierra Leone", "West Africa", "Africa"),
    "Q945":   ("Togo", "West Africa", "Africa"),
    "Q1006":  ("Guinea", "West Africa", "Africa"),
    "Q1007":  ("Guinea-Bissau", "West Africa", "Africa"),
    "Q1008":  ("Ivory Coast", "West Africa", "Africa"),
    "Q974":   ("Democratic Republic of the Congo", "Central Africa", "Africa"),
    "Q971":   ("Republic of the Congo", "Central Africa", "Africa"),
    "Q916":   ("Angola", "Southern Africa", "Africa"),
    "Q953":   ("Zambia", "East Africa", "Africa"),
    "Q954":   ("Zimbabwe", "East Africa", "Africa"),
    "Q924":   ("Tanzania", "East Africa", "Africa"),
    "Q1009":  ("Cameroon", "Central Africa", "Africa"),
    "Q1036":  ("Uganda", "East Africa", "Africa"),
    "Q1037":  ("Rwanda", "East Africa", "Africa"),
    "Q1020":  ("Senegal", "West Africa", "Africa"),
    "Q233":   ("Malta", "Southern Europe", "Europe"),
    "Q236":   ("Montenegro", "Southern Europe", "Europe"),
    "Q229":   ("Cyprus", "Southern Europe", "Europe"),
    "Q227":   ("Azerbaijan", "West Asia", "Asia"),
    "Q230":   ("Georgia", "West Asia", "Asia"),
    "Q399":   ("Armenia", "West Asia", "Asia"),
    "Q813":   ("Kyrgyzstan", "Central Asia", "Asia"),
    "Q863":   ("Tajikistan", "Central Asia", "Asia"),
    "Q265":   ("Uzbekistan", "Central Asia", "Asia"),
    "Q232":   ("Kazakhstan", "Central Asia", "Asia"),
    "Q711":   ("Mongolia", "East Asia", "Asia"),
    "Q836":   ("Myanmar", "Southeast Asia", "Asia"),
    "Q819":   ("Laos", "Southeast Asia", "Asia"),
    "Q424":   ("Cambodia", "Southeast Asia", "Asia"),
    "Q717":   ("Venezuela", "South America", "Americas"),
    "Q419":   ("Peru", "South America", "Americas"),
    "Q736":   ("Ecuador", "South America", "Americas"),
    "Q750":   ("Bolivia", "South America", "Americas"),
    "Q733":   ("Paraguay", "South America", "Americas"),
    "Q77":    ("Uruguay", "South America", "Americas"),
    "Q774":   ("Guatemala", "Central America", "Americas"),
    "Q783":   ("Honduras", "Central America", "Americas"),
    "Q792":   ("El Salvador", "Central America", "Americas"),
    "Q800":   ("Costa Rica", "Central America", "Americas"),
    "Q804":   ("Panama", "Central America", "Americas"),
    "Q786":   ("Dominican Republic", "Caribbean", "Americas"),
    "Q241":   ("Cuba", "Caribbean", "Americas"),
    "Q766":   ("Jamaica", "Caribbean", "Americas"),
    "Q228":   ("Andorra", "Southern Europe", "Europe"),
    "Q238":   ("San Marino", "Southern Europe", "Europe"),
    "Q237":   ("Vatican City", "Southern Europe", "Europe"),
    "Q347":   ("Liechtenstein", "Western Europe", "Europe"),
    "Q235":   ("Monaco", "Western Europe", "Europe"),
    "Q1246":  ("Kosovo", "Southern Europe", "Europe"),
    "Q221":   ("North Macedonia", "Southern Europe", "Europe"),
    "Q403":   ("Serbia", "Southern Europe", "Europe"),
    "Q986":   ("Eritrea", "East Africa", "Africa"),
    "Q960":   ("Benin", "West Africa", "Africa"),
    "Q1025":  ("Mauritania", "West Africa", "Africa"),
    "Q1027":  ("Mauritius", "East Africa", "Africa"),
    "Q1019":  ("Madagascar", "East Africa", "Africa"),
    "Q963":   ("Botswana", "Southern Africa", "Africa"),
    "Q1013":  ("Lesotho", "Southern Africa", "Africa"),
    "Q1050":  ("Eswatini", "Southern Africa", "Africa"),
    "Q967":   ("Burundi", "East Africa", "Africa"),
    "Q977":   ("Djibouti", "East Africa", "Africa"),
    "Q1000":  ("Gabon", "Central Africa", "Africa"),
    "Q1014":  ("Liberia", "West Africa", "Africa"),
    "Q1041":  ("Seychelles", "East Africa", "Africa"),
    "Q1045":  ("Somalia", "East Africa", "Africa"),
    "Q1049":  ("Sudan", "North Africa", "Africa"),
    "Q958":   ("South Sudan", "East Africa", "Africa"),
    "Q1023":  ("Malawi", "East Africa", "Africa"),
    "Q1035":  ("Tunisia", "North Africa", "Africa"),
    "Q1042":  ("Libya", "North Africa", "Africa"),
}

DEFAULT_GEO = ("Global", "Global", "Global")

# ═══════════════════════════════════════════════════════════════════
# Non-movement entity types to filter out
# ═══════════════════════════════════════════════════════════════════

NON_MOVEMENT_KEYWORDS = {
    # Sports
    'association football', 'football club', 'soccer',
    'sports club', 'athletic club', 'cricket club',
    'rugby club', 'basketball team', 'baseball team',
    'ice hockey', 'tennis', 'cycling team',
    # Entertainment
    'television series', 'tv series', 'film', 'video game',
    'album', 'song', 'musical group', 'band',
    'video game genre', 'music genre',
    'fictional', 'comic book', 'novel',
    'award', 'prize ceremony',
    # Technology / corporations
    'programming language', 'website', 'software application',
    'technology company', 'tech company', 'software company',
    'multinational corporation', 'conglomerate',
    'public company', 'privately held', 'subsidiary',
    'automobile manufacturer', 'car manufacturer', 'automaker',
    'airline', 'aircraft manufacturer',
    'pharmaceutical company', 'drug company',
    'energy company', 'oil company', 'oil and gas',
    'telecommunications company', 'telecom',
    'financial services', 'investment bank', 'commercial bank',
    'insurance company', 'consulting firm',
    'retail company', 'retailer', 'supermarket chain',
    'food company', 'beverage company', 'restaurant chain',
    'electronics company', 'semiconductor', 'chip manufacturer',
    'social media platform', 'search engine',
    'streaming service', 'e-commerce',
    'defense contractor', 'weapons manufacturer',
    'mining company', 'steel company', 'chemical company',
    'construction company', 'real estate company',
    # Media
    'magazine', 'newspaper', 'radio station',
    'television network', 'broadcasting',
    'news agency', 'wire service',
    # Government / IGO / administrative
    'administrative division', 'municipality', 'county',
    'intergovernmental organization', 'military alliance',
    'intelligence agency', 'law enforcement',
    'government agency', 'federal agency', 'regulatory body',
    'specialised agency', 'specialized agency',
    'international financial institution',
    'central bank', 'reserve bank',
    # Infrastructure
    'railway station', 'airport', 'highway',
    'bridge', 'dam', 'power plant',
    # Education (institutions, not movements)
    'university', 'college', 'school', 'academy',
    'research institute', 'laboratory',
    # Healthcare
    'hospital', 'medical center', 'health system',
    # Religion entities (not movements)
    'world religion', 'major religion',
    'indian religions', 'east asian religions', 'chinese philosophy',
    'abrahamic', 'dharmic religion',
    # IGOs / intergovernmental (specific)
    'intergovernmental', 'united nations system',
    'international court', 'world bank group',
    'supranational union', 'united nations agency',
    'international organization',
    # Major religions (concepts, not movements)
    'indian religion', 'chinese ethical', 'chinese origin',
    'philosophical tradition', 'abrahamic religion',
    'monotheistic religion', 'polytheistic',
    # Wiki / meta
    'wikipedia', 'wikimedia', 'wikidata', 'wikiproject',
}


def get_country_info(country_qid: str | None) -> tuple[str, str, str]:
    if not country_qid:
        return DEFAULT_GEO
    return COUNTRY_INFO.get(country_qid, DEFAULT_GEO)


def year_to_era(year: int | None) -> tuple[str, str]:
    if year is None:
        return ("Modern", "modern")
    if year < -3000:
        return ("Prehistoric", "prehistoric")
    if year <= 500:
        return ("Classical", "classical")
    if year <= 1500:
        return ("Medieval", "medieval")
    if year <= 1800:
        return ("Early Modern", "early-modern")
    if year <= 1945:
        return ("Modern", "modern")
    return ("Contemporary", "contemporary")


def compute_significance(sitelinks: int, year: int | None) -> int:
    if sitelinks >= 150:
        score = 8
    elif sitelinks >= 100:
        score = 7
    elif sitelinks >= 70:
        score = 6
    elif sitelinks >= 50:
        score = 5
    elif sitelinks >= 35:
        score = 4
    elif sitelinks >= 20:
        score = 3
    elif sitelinks >= 12:
        score = 2
    else:
        score = 1
    if year is not None:
        if year < -1000:
            score += 2
        elif year < 500:
            score += 1
    return max(1, min(10, score))


def significance_label(score: int) -> str:
    if score >= 9:
        return "Landmark"
    if score >= 7:
        return "Major"
    if score >= 5:
        return "Notable"
    if score >= 3:
        return "Moderate"
    return "Minor"


def parse_year(date_str: str | None) -> int | None:
    if not date_str:
        return None
    m = re.match(r'^([+-]?\d+)', date_str)
    return int(m.group(1)) if m else None


def format_date_display(date_str: str | None) -> str:
    if not date_str:
        return ""
    m = re.match(r'^([+-]?)(\d+)-(\d{2})-(\d{2})', date_str)
    if not m:
        return ""
    sign, year_s, month, day = m.groups()
    year = int(year_s)
    if sign == "-" or (sign == "+" and year < 0):
        return f"{abs(year)} BCE"
    if year > 0 and year < 100:
        return f"{year} CE"
    if month == "01" and day == "01":
        return f"{year} CE" if year < 1000 else str(year)
    return f"{year}-{month}-{day}"


def make_slug(name: str) -> str:
    slug = name.lower().strip()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')[:80]


def qid_from_uri(uri: str | None) -> str | None:
    if not uri:
        return None
    m = re.search(r'(Q\d+)$', uri)
    return m.group(1) if m else None


def binding_val(row: dict, key: str) -> str | None:
    b = row.get(key)
    return b["value"] if b and "value" in b else None


def get_division(type_qid: str | None) -> tuple[str, str]:
    if type_qid and type_qid in QID_TO_DIVISION:
        return QID_TO_DIVISION[type_qid]
    return ("620", "Social Movements")


def refine_division(name: str, description: str, default_div: str, default_heading: str) -> tuple[str, str]:
    """Use keyword rules to assign the most specific division possible."""
    check = f"{name} {description}".lower()
    for keywords, div_code, div_heading in KEYWORD_DIVISION_RULES:
        if any(kw in check for kw in keywords):
            return (div_code, div_heading)
    return (default_div, default_heading)


def is_non_movement(description: str, type_label: str) -> bool:
    check = f"{description} {type_label}".lower()
    return any(kw in check for kw in NON_MOVEMENT_KEYWORDS)


def build_sparql_query(type_qids: list[str], limit: int, min_sitelinks: int = 5, use_subclass: bool = False) -> str:
    values = " ".join(f"wd:{qid}" for qid in type_qids)
    type_match = "?item wdt:P31/wdt:P279* ?type ." if use_subclass else "?item wdt:P31 ?type ."
    return f"""
SELECT DISTINCT ?item ?itemLabel ?itemDescription
       ?type ?typeLabel
       ?country ?countryLabel
       ?locationLabel
       ?startTime ?endTime
       ?sitelinks
WHERE {{
  VALUES ?type {{ {values} }}
  {type_match}
  ?item wikibase:sitelinks ?sitelinks .
  FILTER(?sitelinks > {min_sitelinks})

  OPTIONAL {{ ?item wdt:P17  ?country . }}
  OPTIONAL {{ ?item wdt:P276 ?location . }}
  OPTIONAL {{ ?item wdt:P571 ?startTime . }}
  OPTIONAL {{ ?item wdt:P576 ?endTime . }}

  SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en" . }}
}}
ORDER BY DESC(?sitelinks)
LIMIT {limit}
"""


def fetch_sparql(query: str, retries: int = 2) -> list[dict[str, Any]]:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/sparql-results+json",
    }
    for attempt in range(retries):
        try:
            resp = requests.get(
                SPARQL_ENDPOINT,
                params={"query": query, "format": "json"},
                headers=headers,
                timeout=90,
            )
            if resp.status_code == 429:
                wait = min(60, 10 * (attempt + 1))
                print(f"    Rate limited, waiting {wait}s ...")
                time.sleep(wait)
                continue
            if resp.status_code in (500, 502, 504):
                wait = 8 * (attempt + 1)
                print(f"    Server {resp.status_code} (attempt {attempt+1}), retrying in {wait}s ...")
                time.sleep(wait)
                continue
            resp.raise_for_status()
            return resp.json()["results"]["bindings"]
        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError):
            wait = 10 * (attempt + 1)
            print(f"    Timeout (attempt {attempt+1}), retrying in {wait}s ...")
            time.sleep(wait)
        except (ValueError, KeyError) as e:
            print(f"    Parse error (attempt {attempt+1}): {e}")
            if attempt < retries - 1:
                time.sleep(5)
        except requests.exceptions.RequestException as e:
            print(f"    Error (attempt {attempt+1}): {e}")
            if attempt < retries - 1:
                time.sleep(5 * (attempt + 1))
    return []


def fetch_adaptive(type_qids: list[str], target_limit: int, min_sl: int, use_subclass: bool = False) -> list[dict[str, Any]]:
    # Try target limit, then halve once, then 500
    limits = [target_limit]
    if target_limit > 1000:
        limits.append(target_limit // 2)
    if target_limit > 500:
        limits.append(500)

    for lim in limits:
        query = build_sparql_query(type_qids, limit=lim, min_sitelinks=min_sl, use_subclass=use_subclass)
        rows = fetch_sparql(query, retries=2)
        if rows:
            return rows
        print(f"    Reducing limit: {lim} -> next")
    return []


def assign_framework(div_code: str) -> list[str]:
    frameworks = ["CAUSE_AND_EFFECT"]
    d = int(div_code)
    if 610 <= d <= 616:
        frameworks.append("POLITICAL_SYSTEMS")
    if 620 <= d <= 626:
        frameworks.append("SOCIAL_STRUCTURES")
    if 630 <= d <= 635:
        frameworks.append("RELIGIOUS_WORLDVIEWS")
    if 640 <= d <= 645:
        frameworks.append("CULTURAL_EXCHANGE")
    if 650 <= d <= 653:
        frameworks.append("SCIENTIFIC_PARADIGMS")
    if 660 <= d <= 663:
        frameworks.append("TECHNOLOGICAL_DETERMINISM")
    if 670 <= d <= 673:
        frameworks.append("ENVIRONMENTAL_DETERMINISM")
    if 680 <= d <= 683:
        frameworks.append("ECONOMIC_SYSTEMS")
    return frameworks


def transform_movement(row: dict) -> dict[str, Any] | None:
    item_uri = binding_val(row, "item")
    name = binding_val(row, "itemLabel")
    if not item_uri or not name or re.match(r'^Q\d+$', name):
        return None

    qid = qid_from_uri(item_uri)
    description = binding_val(row, "itemDescription") or ""
    type_qid = qid_from_uri(binding_val(row, "type"))
    type_label = binding_val(row, "typeLabel") or ""

    if is_non_movement(description, type_label):
        return None

    start_raw = binding_val(row, "startTime")
    end_raw = binding_val(row, "endTime")
    country_qid = qid_from_uri(binding_val(row, "country"))
    country_label = binding_val(row, "countryLabel") or ""
    location = binding_val(row, "locationLabel") or ""
    sitelinks = int(binding_val(row, "sitelinks") or "0")

    start_year = parse_year(start_raw)
    end_year = parse_year(end_raw)
    start_display = format_date_display(start_raw)
    end_display = format_date_display(end_raw)

    era, era_slug = year_to_era(start_year)

    # Get default division from type, then refine via keywords
    default_div, default_heading = get_division(type_qid)
    div_code, div_heading = refine_division(name, description, default_div, default_heading)

    country_name, region, continent = get_country_info(country_qid)
    if country_name == "Global" and country_label and not re.match(r'^Q\d+$', country_label):
        country_name = country_label

    slug = make_slug(name)

    summary = description.capitalize() if description else f"{name}, a {type_label}."
    if country_name and country_name != "Global":
        summary += f" Based in {country_name}."
    if start_display:
        summary += f" Founded/began: {start_display}."
    if end_display:
        summary += f" Ended: {end_display}."

    sig_score = compute_significance(sitelinks, start_year)
    frameworks = assign_framework(div_code)

    entity: dict[str, Any] = {
        "slug": slug,
        "name": name,
        "label": "Movement",
        "callNumber": f"{div_code}.{slug}",
        "subjectHeadings": [f"Movements -- {div_heading} -- {country_name} -- {era}"],
        "subjects": [s for s in [country_name, type_label, continent, div_heading] if s and s != "Global"],
        "summary": summary[:9900],
        "era": era,
        "eraSlug": era_slug,
        "region": region,
        "continent": continent,
        "status": "Published",
        "frameworks": frameworks,
        "causes": [],
        "effects": [],
        "relationships": [],
        "places": [],
        "texts": [],
        "movementType": type_label,
        "divisionCode": div_code,
        "divisionHeading": div_heading,
        "historicalSignificance": {
            "score": sig_score,
            "label": significance_label(sig_score),
            "sitelinks": sitelinks,
        },
        "inAppwrite": False,
    }

    if start_year is not None:
        entity["startYear"] = start_year
    if end_year is not None:
        entity["endYear"] = end_year
    if start_display:
        entity["date"] = start_display
    if end_display:
        entity["endDate"] = end_display

    if country_name and country_name != "Global":
        entity["relationships"].append({
            "sourceSlug": slug, "sourceName": name,
            "verb": "OCCURS_IN",
            "targetSlug": f"country-{make_slug(country_name)}",
            "targetName": country_name,
            "context": f"{name} originated in {country_name}",
        })
    if location and not re.match(r'^Q\d+$', location):
        entity["places"].append({"name": location, "role": "Origin"})
    if country_name and country_name != "Global":
        entity["places"].append({"name": country_name, "role": "Country"})

    if qid:
        entity["wikidataQid"] = qid

    return entity


def _save_progress(output_path: Path, entities: list, seen_slugs: set,
                   total_raw: int, all_qids: set, batch_stats: dict,
                   failed_batches: list, partial: bool = False) -> None:
    """Save current entities to a progress file (or final output)."""
    suffix = ".partial" if partial else ""
    path = Path(str(output_path) + suffix) if partial else output_path

    div_counts: dict[str, int] = {}
    era_counts: dict[str, int] = {}
    for e in entities:
        div = e["callNumber"][:3]
        div_counts[div] = div_counts.get(div, 0) + 1
        era_counts[e["era"]] = era_counts.get(e["era"], 0) + 1

    data = {
        "_meta": {
            "source": "Wikidata SPARQL (query.wikidata.org)",
            "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "version": "3.0" + ("-partial" if partial else ""),
            "total_raw_results": total_raw,
            "total_unique_entities": len(entities),
            "label": "Movement",
            "classCode": 6,
            "batches_completed": len(batch_stats),
            "failed_batches": failed_batches,
            "division_counts": dict(sorted(div_counts.items())),
            "era_counts": dict(sorted(era_counts.items())),
        },
        "entities": entities,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser(description="Fetch movements from Wikidata (v3.0)")
    parser.add_argument("--limit", type=int, default=5000)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    output_path = Path(args.output) if args.output else project_root / "data" / "wikidata_movements.json"

    all_qids = set()
    for batch in MOVEMENT_QUERIES.values():
        all_qids.update(batch[0])
    sc_count = sum(1 for b in MOVEMENT_QUERIES.values() if len(b) > 2 and b[2])

    print("=" * 70)
    print("  Wikidata Movements Fetch v3.0 -- Annals of the World")
    print("=" * 70)
    print(f"  Limit per batch:     {args.limit}")
    print(f"  Output:              {output_path}")
    print(f"  Query batches:       {len(MOVEMENT_QUERIES)} ({sc_count} with subclass traversal)")
    print(f"  Unique type QIDs:    {len(all_qids)}")
    print(f"  Division coverage:   610-683 (all Class 6 sub-divisions)")
    print(f"  Keyword refinement:  {len(KEYWORD_DIVISION_RULES)} division rule sets")
    print(f"  Adaptive fallback:   Yes")
    print()

    all_entities: list[dict[str, Any]] = []
    seen_slugs: set[str] = set()
    total_raw = 0
    batch_stats: dict[str, int] = {}
    failed_batches: list[str] = []

    for batch_name, batch_config in MOVEMENT_QUERIES.items():
        type_qids = batch_config[0]
        min_sl = batch_config[1]
        use_subclass = batch_config[2] if len(batch_config) > 2 else False
        sc_tag = " [SC]" if use_subclass else ""
        print(f"[{batch_name}]  {len(type_qids)} type(s), sitelinks>{min_sl}{sc_tag} ...")

        if args.dry_run:
            print(f"  (dry-run) skipped\n")
            continue

        rows = fetch_adaptive(type_qids, args.limit, min_sl, use_subclass)
        if not rows:
            failed_batches.append(batch_name)
            print(f"  FAILED (no results after all retries)\n")
            time.sleep(3)
            continue

        total_raw += len(rows)
        print(f"  Got {len(rows)} raw results")

        batch_count = 0
        for row in rows:
            entity = transform_movement(row)
            if not entity or entity["slug"] in seen_slugs:
                continue
            seen_slugs.add(entity["slug"])
            all_entities.append(entity)
            batch_count += 1

        batch_stats[batch_name] = batch_count
        print(f"  -> {batch_count} NEW (total: {len(all_entities)})")

        # Progressive save every 5 batches
        if len(batch_stats) % 5 == 0:
            _save_progress(output_path, all_entities, seen_slugs, total_raw,
                           all_qids, batch_stats, failed_batches, partial=True)
            print(f"  [saved progress: {len(all_entities)} entities]")

        time.sleep(2)

    if args.dry_run:
        print(f"\nDry run complete. {len(MOVEMENT_QUERIES)} batches configured.")
        return

    # ── Post-processing: re-apply keyword refinement on all entities ──
    print("\n  Post-processing: keyword-based division refinement...")
    refined_count = 0
    for entity in all_entities:
        old_div = entity["divisionCode"]
        new_div, new_heading = refine_division(
            entity["name"], entity.get("summary", ""),
            old_div, entity["divisionHeading"]
        )
        if new_div != old_div:
            entity["divisionCode"] = new_div
            entity["divisionHeading"] = new_heading
            entity["callNumber"] = f"{new_div}.{entity['slug']}"
            entity["subjectHeadings"] = [f"Movements -- {new_heading} -- {entity.get('continent', 'Global')} -- {entity.get('era', 'Modern')}"]
            entity["frameworks"] = assign_framework(new_div)
            refined_count += 1
    print(f"  Refined {refined_count} entities to more specific divisions")

    era_order = {"Prehistoric": 0, "Classical": 1, "Medieval": 2, "Early Modern": 3, "Modern": 4, "Contemporary": 5}
    all_entities.sort(key=lambda e: (era_order.get(e["era"], 9), e["name"]))

    div_counts: dict[str, int] = {}
    era_counts: dict[str, int] = {}
    sig_dist: dict[str, int] = {}
    continent_counts: dict[str, int] = {}
    for e in all_entities:
        div = e["callNumber"][:3]
        div_counts[div] = div_counts.get(div, 0) + 1
        era_counts[e["era"]] = era_counts.get(e["era"], 0) + 1
        sig_dist[e["historicalSignificance"]["label"]] = sig_dist.get(e["historicalSignificance"]["label"], 0) + 1
        ct = e.get("continent", "Global")
        continent_counts[ct] = continent_counts.get(ct, 0) + 1

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_data = {
        "_meta": {
            "source": "Wikidata SPARQL (query.wikidata.org)",
            "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "version": "3.0",
            "total_raw_results": total_raw,
            "total_unique_entities": len(all_entities),
            "label": "Movement",
            "classCode": 6,
            "classHeading": "Movements",
            "type_qids_queried": len(all_qids),
            "batches_queried": len(MOVEMENT_QUERIES),
            "failed_batches": failed_batches,
            "keyword_refined_count": refined_count,
            "division_counts": dict(sorted(div_counts.items())),
            "era_counts": dict(sorted(era_counts.items())),
            "significance_distribution": dict(sorted(sig_dist.items())),
            "continent_counts": dict(sorted(continent_counts.items())),
            "significance_scale": {
                "1-2": "Minor -- documented but limited global impact",
                "3-4": "Moderate -- nationally significant",
                "5-6": "Notable -- regionally or thematically important",
                "7-8": "Major -- globally recognized",
                "9-10": "Landmark -- world-shaping movement",
            },
            "inAppwrite_note": "All entities have inAppwrite=false.",
            "note": "Wikidata movements v3.0 — instantiable types + keyword division refinement + fast-fail retries, covering Class 6 divisions 610-683.",
        },
        "entities": all_entities,
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print()
    print("=" * 70)
    print("  Fetch Complete -- v3.0")
    print("=" * 70)
    print(f"  Raw results:       {total_raw}")
    print(f"  Unique entities:   {len(all_entities)}")
    print(f"  Keyword refined:   {refined_count}")
    print(f"  Output:            {output_path}")
    if failed_batches:
        print(f"  Failed batches:    {', '.join(failed_batches)}")
    print()
    print("  By division:")
    for div, count in sorted(div_counts.items()):
        print(f"    {div}: {count}")
    print()
    print("  By era:")
    for era_name, count in sorted(era_counts.items(), key=lambda x: era_order.get(x[0], 9)):
        print(f"    {era_name}: {count}")
    print()
    print("  By significance:")
    for label, count in sorted(sig_dist.items()):
        print(f"    {label}: {count}")
    print()
    print("  By continent:")
    for ct, count in sorted(continent_counts.items(), key=lambda x: -x[1]):
        print(f"    {ct}: {count}")
    print()

    top15 = sorted(all_entities, key=lambda e: (-e["historicalSignificance"]["score"], e["name"]))[:15]
    print("  Top 15 by significance:")
    for e in top15:
        sig = e["historicalSignificance"]
        print(f"    [{sig['score']}] {e['name']} ({e['divisionCode']} {e['divisionHeading']}) -- {sig['sitelinks']} sitelinks")
    print()


if __name__ == "__main__":
    main()
