#!/usr/bin/env python3
"""
fetch_wikidata_artifacts.py  (v1.0)

Comprehensive Wikidata fetch of notable artifacts & texts across ALL Class 7
divisions (710-785). Uses 75+ Wikidata type QIDs, adaptive limit fallback,
keyword-based sub-division refinement, and progressive saving.

Covers: Constitutions, Legal Codes, Treaties, Religious Texts, Philosophical
Works, Scientific Texts, Paintings, Sculpture, Music, Architecture,
Technological Artifacts, Ships, Historical & Literary Texts.

Output: data/wikidata_artifacts.json

Usage:
    python3 scripts/fetch_wikidata_artifacts.py
    python3 scripts/fetch_wikidata_artifacts.py --limit 5000
    python3 scripts/fetch_wikidata_artifacts.py --dry-run
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
# Artifact/Text Type -> Division Mapping  (75+ QIDs)
# Maps Wikidata P31 (instance of) QIDs to call-number divisions
# ═══════════════════════════════════════════════════════════════════

ARTIFACT_TYPE_MAP: dict[str, tuple[str, str]] = {
    # ── 710 Constitutions & Charters ──
    "Q7755":      ("710", "Constitutions & Charters"),       # constitution
    "Q212687":    ("710", "Constitutions & Charters"),       # charter
    "Q104774":    ("710", "Constitutions & Charters"),       # national constitution

    # ── 712 Medieval Charters & Concordats ──
    "Q18668582":  ("712", "Medieval Charters & Concordats"), # concordat

    # ── 714 Declarations & Proclamations ──
    "Q131395":    ("714", "Declarations & Proclamations"),   # declaration
    "Q841039":    ("714", "Declarations & Proclamations"),   # proclamation

    # ── 720 Legal Codes ──
    "Q820655":    ("720", "Legal Codes"),                    # decree
    "Q1491746":   ("720", "Legal Codes"),                    # code of law

    # ── 724 International Treaties & Conventions ──
    "Q131569":    ("724", "International Treaties & Conventions"),  # treaty
    "Q93288":     ("724", "International Treaties & Conventions"),  # peace treaty
    "Q625298":    ("724", "International Treaties & Conventions"),  # armistice

    # ── 730 Religious Texts ──
    "Q179461":    ("730", "Religious Texts"),                # religious text
    "Q15921890":  ("730", "Religious Texts"),                # sacred text
    "Q5930":      ("730", "Religious Texts"),                # holy book

    # ── 740 Philosophical Works ──
    "Q36524":     ("740", "Philosophical Works"),            # philosophical work

    # ── 750 Scientific Texts ──
    "Q5292":      ("750", "Scientific Texts"),               # encyclopedia
    "Q386724":    ("750", "Scientific Texts"),               # textbook
    "Q41689629":  ("750", "Scientific Texts"),               # treatise

    # ── 761 Paintings & Visual Art ──
    "Q3305213":   ("761", "Paintings & Visual Art"),         # painting
    "Q17514":     ("761", "Paintings & Visual Art"),         # fresco
    "Q93184":     ("761", "Paintings & Visual Art"),         # drawing
    "Q18573970":  ("761", "Paintings & Visual Art"),         # mural
    "Q11060274":  ("761", "Paintings & Visual Art"),         # print
    "Q18761202":  ("761", "Paintings & Visual Art"),         # watercolor painting
    "Q132137":    ("761", "Paintings & Visual Art"),         # icon (religious art)
    "Q133067":    ("761", "Paintings & Visual Art"),         # mosaic
    "Q184296":    ("761", "Paintings & Visual Art"),         # tapestry

    # ── 762 Sculpture & Monuments ──
    "Q860861":    ("762", "Sculpture & Monuments"),          # sculpture
    "Q179700":    ("762", "Sculpture & Monuments"),          # statue
    "Q1076486":   ("762", "Sculpture & Monuments"),          # monument
    "Q928357":    ("762", "Sculpture & Monuments"),          # stele
    "Q220659":    ("762", "Sculpture & Monuments"),          # bust
    "Q17489160":  ("762", "Sculpture & Monuments"),          # relief

    # ── 763 Music & Compositions ──
    "Q207628":    ("763", "Music & Compositions"),           # musical composition
    "Q1344":      ("763", "Music & Compositions"),           # opera
    "Q564466":    ("763", "Music & Compositions"),           # symphony
    "Q188451":    ("763", "Music & Compositions"),           # concerto
    "Q131289":    ("763", "Music & Compositions"),           # cantata
    "Q116077":    ("763", "Music & Compositions"),           # sonata
    "Q131168":    ("763", "Music & Compositions"),           # oratorio

    # ── 764 Architecture & Built Works ──
    "Q16560":     ("764", "Architecture & Built Works"),     # palace
    "Q820477":    ("764", "Architecture & Built Works"),     # castle
    "Q751876":    ("764", "Architecture & Built Works"),     # château
    "Q12518":     ("764", "Architecture & Built Works"),     # tower
    "Q57821":     ("764", "Architecture & Built Works"),     # fortification
    "Q12280":     ("764", "Architecture & Built Works"),     # bridge
    "Q34627":     ("764", "Architecture & Built Works"),     # dam
    "Q839954":    ("764", "Architecture & Built Works"),     # archaeological site
    "Q151624":    ("764", "Architecture & Built Works"),     # amphitheatre
    "Q11303":     ("764", "Architecture & Built Works"),     # skyscraper
    "Q12516":     ("764", "Architecture & Built Works"),     # pyramid
    "Q474748":    ("764", "Architecture & Built Works"),     # aqueduct
    "Q39715":     ("764", "Architecture & Built Works"),     # lighthouse
    "Q1549591":   ("764", "Architecture & Built Works"),     # triumphal arch

    # ── 771 Tools & Instruments ──
    "Q2041172":   ("771", "Tools & Instruments"),            # scientific instrument
    "Q175263":    ("771", "Tools & Instruments"),            # invention

    # ── 772 Weapons & Armor ──
    "Q178550":    ("772", "Weapons & Armor"),                # firearm
    "Q12876":     ("772", "Weapons & Armor"),                # tank
    "Q182985":    ("772", "Weapons & Armor"),                # assault rifle

    # ── 773 Ships & Vehicles ──
    "Q11446":     ("773", "Ships & Vehicles"),               # ship
    "Q559026":    ("773", "Ships & Vehicles"),               # warship
    "Q697175":    ("773", "Ships & Vehicles"),               # sailing vessel
    "Q12019":     ("773", "Ships & Vehicles"),               # submarine
    "Q1229765":   ("773", "Ships & Vehicles"),               # ocean liner
    "Q11436":     ("773", "Ships & Vehicles"),               # aircraft

    # ── 774 Machines & Engines ──
    "Q11019":     ("774", "Machines & Engines"),             # machine

    # ── 780 Historical & Literary Texts (parent) ──
    "Q571":       ("780", "Historical & Literary Texts"),    # book
    "Q7725634":   ("780", "Historical & Literary Texts"),    # literary work
    "Q25379":     ("780", "Historical & Literary Texts"),    # play (theatre)

    # ── 782 Epic Poetry & Mythology ──
    "Q5185279":   ("782", "Epic Poetry & Mythology"),        # poem
    "Q37484":     ("782", "Epic Poetry & Mythology"),        # epic poem
    "Q12308638":  ("782", "Epic Poetry & Mythology"),        # epic

    # ── 783 Novels & Prose Fiction ──
    "Q8261":      ("783", "Novels & Prose Fiction"),         # novel
    "Q49084":     ("783", "Novels & Prose Fiction"),         # short story
    "Q1667921":   ("783", "Novels & Prose Fiction"),         # novella

    # ── 784 Travel Writing & Geography ──
    "Q80071":     ("784", "Travel Writing & Geography"),     # atlas

    # ── 785 Political & Polemical Texts ──
    "Q131539":    ("785", "Political & Polemical Texts"),    # essay
    "Q185698":    ("785", "Political & Polemical Texts"),    # manifesto
}

# Build reverse lookup: first-occurrence wins
QID_TO_DIVISION: dict[str, tuple[str, str]] = {}
for _qid, _div_info in ARTIFACT_TYPE_MAP.items():
    if _qid not in QID_TO_DIVISION:
        QID_TO_DIVISION[_qid] = _div_info


# ═══════════════════════════════════════════════════════════════════
# Batched SPARQL queries  (68 granular batches)
# Each batch -> (QIDs, min_sitelinks)
# Heavy types split solo w/ higher threshold to avoid timeouts
# Order: specific types FIRST, then broad catch-all types LAST
# ═══════════════════════════════════════════════════════════════════

ARTIFACT_QUERIES: dict[str, tuple[list[str], int]] = {
    # ── 710-714 Constitutions & Charters ──
    "710_constitution":   (["Q7755", "Q104774"], 5),
    "710_charter":        (["Q212687"], 5),
    "710_decree":         (["Q820655"], 5),
    "712_concordat":      (["Q18668582"], 5),
    "714_declaration":    (["Q131395", "Q841039"], 5),

    # ── 720-724 Legal Codes & Treaties ──
    "720_legal_code":     (["Q1491746"], 5),
    "724_treaty":         (["Q131569"], 5),
    "724_peace":          (["Q93288", "Q625298"], 5),

    # ── 730 Religious Texts ──
    "730_religious_a":    (["Q179461"], 5),
    "730_religious_b":    (["Q15921890", "Q5930"], 5),

    # ── 740 Philosophical Works ──
    "740_philosophy":     (["Q36524"], 5),

    # ── 750 Scientific Texts ──
    "750_encyclopedia":   (["Q5292"], 5),
    "750_textbook":       (["Q386724"], 10),
    "750_treatise":       (["Q41689629"], 5),

    # ── 761 Paintings & Visual Art ──
    "761_painting":       (["Q3305213"], 30),        # HUGE type — high threshold
    "761_fresco":         (["Q17514"], 5),
    "761_drawing":        (["Q93184"], 10),
    "761_mural":          (["Q18573970"], 5),
    "761_print":          (["Q11060274"], 5),
    "761_watercolor":     (["Q18761202"], 5),
    "761_icon":           (["Q132137"], 5),
    "761_mosaic":         (["Q133067"], 5),
    "761_tapestry":       (["Q184296"], 5),

    # ── 762 Sculpture & Monuments ──
    "762_sculpture":      (["Q860861"], 10),
    "762_statue":         (["Q179700"], 8),
    "762_monument":       (["Q1076486"], 5),
    "762_stele":          (["Q928357", "Q220659"], 5),
    "762_relief":         (["Q17489160"], 5),

    # ── 763 Music & Compositions ──
    "763_composition":    (["Q207628"], 30),          # HUGE type — high threshold
    "763_opera":          (["Q1344"], 10),
    "763_symphony":       (["Q564466"], 5),
    "763_concerto":       (["Q188451"], 5),
    "763_cantata":        (["Q131289"], 5),
    "763_sonata":         (["Q116077"], 5),
    "763_oratorio":       (["Q131168"], 5),

    # ── 764 Architecture & Built Works ──
    "764_palace":         (["Q16560"], 5),
    "764_castle":         (["Q820477"], 5),
    "764_chateau":        (["Q751876"], 5),
    "764_tower":          (["Q12518"], 5),
    "764_fort":           (["Q57821"], 5),
    "764_bridge":         (["Q12280"], 8),
    "764_dam":            (["Q34627"], 5),
    "764_arch_site":      (["Q839954"], 5),
    "764_amphitheater":   (["Q151624"], 5),
    "764_skyscraper":     (["Q11303"], 8),
    "764_pyramid":        (["Q12516"], 5),
    "764_aqueduct":       (["Q474748"], 5),
    "764_lighthouse":     (["Q39715"], 5),
    "764_triumphal":      (["Q1549591"], 5),

    # ── 771 Tools & Instruments ──
    "771_instrument":     (["Q2041172"], 5),
    "771_invention":      (["Q175263"], 12),

    # ── 772 Weapons & Armor ──
    "772_weapon":         (["Q178550", "Q12876", "Q182985"], 10),

    # ── 773 Ships & Vehicles ──
    "773_ship":           (["Q11446"], 10),
    "773_warship":        (["Q559026"], 8),
    "773_sailing":        (["Q697175", "Q1229765"], 5),
    "773_submarine":      (["Q12019"], 5),
    "773_aircraft":       (["Q11436"], 10),

    # ── 774 Machines & Engines ──
    "774_machine":        (["Q11019"], 15),

    # ── 782 Epic Poetry & Mythology (BEFORE broad book/literary) ──
    "782_poem":           (["Q5185279"], 10),
    "782_epic":           (["Q37484", "Q12308638"], 5),

    # ── 783 Novels & Prose Fiction (BEFORE broad book/literary) ──
    "783_novel":          (["Q8261"], 25),            # HUGE type — high threshold
    "783_short":          (["Q49084", "Q1667921"], 8),

    # ── 784 Travel Writing & Geography ──
    "784_atlas":          (["Q80071"], 5),

    # ── 785 Political & Polemical Texts ──
    "785_essay":          (["Q131539"], 10),
    "785_manifesto":      (["Q185698"], 5),

    # ── 780 Broad Literary (LAST — catch remaining books/plays) ──
    "780_play":           (["Q25379"], 10),
    "780_book":           (["Q571"], 40),             # ENORMOUS — only most notable
    "780_literary":       (["Q7725634"], 35),         # HUGE — only most notable
}


# ═══════════════════════════════════════════════════════════════════
# Non-artifact keyword filter
# ═══════════════════════════════════════════════════════════════════

NON_ARTIFACT_KEYWORDS = {
    'wikimedia', 'disambiguation', 'template', 'category',
    'fictional character', 'video game', 'software', 'mobile app',
    'taxon', 'species', 'genus', 'protein', 'gene',
    'administrative unit', 'municipality', 'district',
    'television series', 'tv series', 'podcast',
    'association football', 'football club', 'sports club',
    'political party', 'company', 'corporation',
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
# Helper functions
# ═══════════════════════════════════════════════════════════════════

def get_country_info(country_qid: str | None) -> tuple[str, str, str]:
    if not country_qid:
        return DEFAULT_GEO
    return COUNTRY_INFO.get(country_qid, DEFAULT_GEO)


def year_to_era(year: int | None) -> tuple[str, str]:
    if year is None:
        return ("Classical", "classical")
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


def compute_significance(sitelinks: int, creation_year: int | None) -> int:
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
    if creation_year is not None:
        if creation_year < -1000:
            score += 2
        elif creation_year < 500:
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
    return ("780", "Historical & Literary Texts")


# ═══════════════════════════════════════════════════════════════════
# Sub-division refinement
# Assigns parent-level divisions to specific sub-divisions using
# era, type, and keyword context.
# ═══════════════════════════════════════════════════════════════════

def refine_division(
    div_code: str,
    div_heading: str,
    era: str,
    type_label: str,
    name: str,
    description: str,
) -> tuple[str, str]:
    text = f"{name} {description} {type_label}".lower()

    # 710 → 711-714
    if div_code == "710":
        if any(w in text for w in ("declaration", "proclamation")):
            return ("714", "Declarations & Proclamations")
        if era in ("Prehistoric", "Classical"):
            return ("711", "Ancient Codes & Decrees")
        if era == "Medieval":
            return ("712", "Medieval Charters & Concordats")
        return ("713", "Modern Constitutions")

    # 720 → 721-723
    if div_code == "720":
        if any(w in text for w in ("canon", "church law", "religious law", "sharia", "halakha")):
            return ("722", "Canon & Religious Law Codes")
        if any(w in text for w in ("civil", "commercial", "criminal", "penal")):
            return ("723", "Civil & Commercial Codes")
        if era in ("Prehistoric", "Classical"):
            return ("721", "Ancient Legal Codes (Hammurabi, Roman)")
        return div_code, div_heading

    # 730 → 731-736
    if div_code == "730":
        if any(w in text for w in ("hebrew", "torah", "tanakh", "talmud", "mishnah", "midrash", "jewish")):
            return ("731", "Hebrew Bible & Torah")
        if any(w in text for w in ("christian", "new testament", "gospel", "patristic", "vulgate", "church father")):
            return ("732", "New Testament & Christian Texts")
        if any(w in text for w in ("quran", "islamic", "hadith", "muslim", "sura", "fiqh")):
            return ("733", "Quran & Islamic Texts")
        if any(w in text for w in ("veda", "upanishad", "hindu", "bhagavad", "mahabharata", "ramayana", "purana")):
            return ("734", "Vedas, Upanishads & Hindu Texts")
        if any(w in text for w in ("buddhist", "pali canon", "sutra", "tripitaka", "dharma", "jataka")):
            return ("735", "Buddhist Scriptures (Pali Canon, Sutras)")
        return ("736", "Other Sacred & Wisdom Texts")

    # 740 → 741-744
    if div_code == "740":
        if era in ("Prehistoric", "Classical"):
            return ("741", "Ancient Philosophy (Greek, Chinese)")
        if era == "Medieval":
            return ("742", "Medieval Scholastic Works")
        if era == "Early Modern":
            return ("743", "Enlightenment Philosophical Works")
        return ("744", "Modern & Contemporary Philosophy")

    # 750 → 751-754
    if div_code == "750":
        if any(w in text for w in ("mathematic", "geometry", "algebra", "arithmetic", "calculus", "number theory")):
            return ("751", "Mathematical Treatises")
        if any(w in text for w in ("natural history", "biology", "botany", "zoology", "evolution", "species")):
            return ("752", "Natural History & Biology Texts")
        if any(w in text for w in ("physics", "astronomy", "optic", "mechanic", "celestial", "planetary")):
            return ("753", "Physics & Astronomy Texts")
        if any(w in text for w in ("medic", "pharmac", "anatomy", "surgery", "healing", "pathology")):
            return ("754", "Medical & Pharmacological Texts")
        return div_code, div_heading

    # 780 → 781-785
    if div_code == "780":
        tl = type_label.lower()
        if tl in ("poem", "epic poem", "epic"):
            return ("782", "Epic Poetry & Mythology")
        if tl in ("novel", "short story", "novella"):
            return ("783", "Novels & Prose Fiction")
        if any(w in text for w in ("travel", "voyage", "geography", "atlas", "expedition")):
            return ("784", "Travel Writing & Geography")
        if any(w in text for w in ("political", "polemic", "manifesto", "pamphlet", "propaganda")):
            return ("785", "Political & Polemical Texts")
        if any(w in text for w in ("history", "chronicle", "annals", "historiograph")):
            return ("781", "Histories & Chronicles")
        if any(w in text for w in ("myth", "epic", "saga", "legend", "folklore")):
            return ("782", "Epic Poetry & Mythology")
        if any(w in text for w in ("novel", "fiction", "story", "romance")):
            return ("783", "Novels & Prose Fiction")
        return div_code, div_heading

    return div_code, div_heading


# ═══════════════════════════════════════════════════════════════════
# SPARQL query builder & fetchers
# ═══════════════════════════════════════════════════════════════════

def build_sparql_query(type_qids: list[str], limit: int, min_sitelinks: int = 5) -> str:
    values = " ".join(f"wd:{qid}" for qid in type_qids)
    return f"""
SELECT DISTINCT ?item ?itemLabel ?itemDescription
       ?type ?typeLabel
       ?inception
       ?country ?countryLabel
       ?creatorLabel
       ?authorLabel
       ?image
       ?article
       ?sitelinks
WHERE {{
  VALUES ?type {{ {values} }}
  ?item wdt:P31 ?type .
  ?item wikibase:sitelinks ?sitelinks .
  FILTER(?sitelinks > {min_sitelinks})

  OPTIONAL {{ ?item wdt:P571 ?inception . }}
  OPTIONAL {{ ?item wdt:P17  ?country . }}
  OPTIONAL {{ ?item wdt:P170 ?creator . }}
  OPTIONAL {{ ?item wdt:P50  ?author . }}
  OPTIONAL {{ ?item wdt:P18  ?image . }}
  OPTIONAL {{
    ?article schema:about ?item ;
             schema:isPartOf <https://en.wikipedia.org/> .
  }}

  SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en" . }}
}}
ORDER BY DESC(?sitelinks)
LIMIT {limit}
"""


def fetch_sparql(query: str, retries: int = 3) -> list[dict[str, Any]]:
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
                timeout=180,
            )
            if resp.status_code == 429:
                wait = min(90, 15 * (attempt + 1))
                print(f"    Rate limited, waiting {wait}s ...")
                time.sleep(wait)
                continue
            if resp.status_code in (500, 504):
                wait = 20 * (attempt + 1)
                print(f"    Server {resp.status_code} (attempt {attempt+1}), retrying in {wait}s ...")
                time.sleep(wait)
                continue
            resp.raise_for_status()
            return resp.json()["results"]["bindings"]
        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError):
            wait = 30 * (attempt + 1)
            print(f"    Timeout (attempt {attempt+1}), retrying in {wait}s ...")
            time.sleep(wait)
        except (ValueError, KeyError) as e:
            print(f"    Parse error (attempt {attempt+1}): {e}")
            if attempt < retries - 1:
                time.sleep(10)
        except requests.exceptions.RequestException as e:
            print(f"    Error (attempt {attempt+1}): {e}")
            if attempt < retries - 1:
                time.sleep(10 * (attempt + 1))
    return []


def fetch_adaptive(type_qids: list[str], target_limit: int, min_sl: int) -> list[dict[str, Any]]:
    """Try target limit; on failure halve until success."""
    limits = [target_limit]
    lim = target_limit
    while lim > 500:
        lim = lim // 2
        limits.append(lim)
    limits.append(500)

    for lim in limits:
        query = build_sparql_query(type_qids, limit=lim, min_sitelinks=min_sl)
        rows = fetch_sparql(query, retries=2)
        if rows:
            return rows
        if lim > 500:
            print(f"    Reducing limit: {lim} -> {lim // 2}")
    return []


# ═══════════════════════════════════════════════════════════════════
# Transform: SPARQL row -> Annals entity
# ═══════════════════════════════════════════════════════════════════

def transform_artifact(row: dict) -> dict[str, Any] | None:
    item_uri = binding_val(row, "item")
    name = binding_val(row, "itemLabel")
    if not item_uri or not name or re.match(r'^Q\d+$', name):
        return None

    qid = qid_from_uri(item_uri)
    description = binding_val(row, "itemDescription") or ""
    type_qid = qid_from_uri(binding_val(row, "type"))
    type_label = binding_val(row, "typeLabel") or ""
    inception_raw = binding_val(row, "inception")
    country_qid = qid_from_uri(binding_val(row, "country"))
    country_label = binding_val(row, "countryLabel") or ""
    creator_name = binding_val(row, "creatorLabel") or binding_val(row, "authorLabel") or ""
    image_url = binding_val(row, "image") or ""
    wiki_url = binding_val(row, "article") or ""
    sitelinks = int(binding_val(row, "sitelinks") or "0")

    # Filter non-artifact entities by keyword
    desc_lower = description.lower()
    if any(kw in desc_lower for kw in NON_ARTIFACT_KEYWORDS):
        return None
    # Filter creator/author fields that are raw QIDs
    if creator_name and re.match(r'^Q\d+$', creator_name):
        creator_name = ""

    creation_year = parse_year(inception_raw)
    created_display = format_date_display(inception_raw)
    era, era_slug = year_to_era(creation_year)
    div_code, div_heading = get_division(type_qid)
    country_name, region, continent = get_country_info(country_qid)
    if country_name == "Global" and country_label and not re.match(r'^Q\d+$', country_label):
        country_name = country_label

    # Refine parent divisions to sub-divisions
    div_code, div_heading = refine_division(div_code, div_heading, era, type_label, name, description)

    slug = make_slug(name)

    # Build summary
    summary = description.capitalize() if description else f"{name}, a {type_label}."
    if creator_name:
        summary += f" Created by {creator_name}."
    if country_name != "Global":
        summary += f" Associated with {country_name}."
    if creation_year:
        if creation_year < 0:
            summary += f" Dating to c. {abs(creation_year)} BCE."
        else:
            summary += f" Created c. {creation_year}."

    sig_score = compute_significance(sitelinks, creation_year)

    entity: dict[str, Any] = {
        "slug": slug,
        "name": name,
        "label": "Text",
        "callNumber": f"{div_code}.{slug}",
        "subjectHeadings": [f"Artifacts & Texts -- {div_heading} -- {country_name} -- {era}"],
        "subjects": [s for s in [country_name, type_label, continent, div_heading] if s and s != "Global"],
        "summary": summary[:9900],
        "era": era,
        "eraSlug": era_slug,
        "region": region,
        "continent": continent,
        "status": "Published",
        "frameworks": ["CAUSE_AND_EFFECT"],
        "causes": [],
        "effects": [],
        "relationships": [{
            "sourceSlug": slug, "sourceName": name,
            "verb": "OCCURS_IN",
            "targetSlug": f"country-{make_slug(country_name)}" if country_name != "Global" else "",
            "targetName": country_name,
            "context": f"{name} from {country_name}",
        }],
        "places": [],
        "texts": [],
        "artifactType": type_label,
        "divisionCode": div_code,
        "divisionHeading": div_heading,
        "historicalSignificance": {
            "score": sig_score,
            "label": significance_label(sig_score),
            "sitelinks": sitelinks,
        },
        "inAppwrite": False,
    }

    if created_display:
        entity["created"] = created_display
    if creation_year:
        entity["createdYear"] = creation_year
    if creator_name:
        entity["creator"] = creator_name
    if country_name and country_name != "Global":
        entity["places"].append({"name": country_name, "role": "Country"})
    if qid:
        entity["wikidataQid"] = qid
    if wiki_url:
        entity["wikipediaUrl"] = wiki_url
    if image_url:
        entity["imageUrl"] = image_url

    return entity


# ═══════════════════════════════════════════════════════════════════
# Progressive save helper
# ═══════════════════════════════════════════════════════════════════

def save_progress(entities: list[dict], output_path: Path, total_raw: int) -> None:
    """Save current progress to a temporary file."""
    progress_path = output_path.with_suffix(".progress.json")
    data = {
        "_meta": {
            "status": "in_progress",
            "total_raw_results": total_raw,
            "total_unique_entities": len(entities),
            "saved_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        },
        "entities": entities,
    }
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  [progress saved: {len(entities)} entities]")


# ═══════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="Fetch artifacts & texts from Wikidata (v1.0)")
    parser.add_argument("--limit", type=int, default=5000)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    output_path = Path(args.output) if args.output else project_root / "data" / "wikidata_artifacts.json"

    total_qids = len(set(qid for qids, _ in ARTIFACT_QUERIES.values() for qid in qids))

    print("=" * 70)
    print("  Wikidata Artifacts & Texts Fetch v1.0 -- Annals of the World")
    print("=" * 70)
    print(f"  Limit per batch:     {args.limit}")
    print(f"  Output:              {output_path}")
    print(f"  Query batches:       {len(ARTIFACT_QUERIES)}")
    print(f"  Unique type QIDs:    {total_qids}")
    print(f"  Division coverage:   710-785 (all Class 7 sub-divisions)")
    print(f"  Adaptive fallback:   Yes")
    print(f"  Progressive save:    Every 5 batches")
    print()

    all_entities: list[dict[str, Any]] = []
    seen_slugs: set[str] = set()
    total_raw = 0
    batch_stats: dict[str, int] = {}
    batch_idx = 0

    for batch_name, (type_qids, min_sl) in ARTIFACT_QUERIES.items():
        batch_idx += 1
        print(f"[{batch_idx}/{len(ARTIFACT_QUERIES)}] {batch_name}  "
              f"{len(type_qids)} type(s), sitelinks>{min_sl} ...")

        if args.dry_run:
            print(f"  (dry-run) skipped\n")
            continue

        rows = fetch_adaptive(type_qids, args.limit, min_sl)
        total_raw += len(rows)
        print(f"  Got {len(rows)} raw results")

        batch_count = 0
        for row in rows:
            entity = transform_artifact(row)
            if not entity or entity["slug"] in seen_slugs:
                continue
            seen_slugs.add(entity["slug"])
            all_entities.append(entity)
            batch_count += 1

        batch_stats[batch_name] = batch_count
        print(f"  -> {batch_count} unique (total: {len(all_entities)})")

        # Progressive save every 5 batches
        if batch_idx % 5 == 0:
            save_progress(all_entities, output_path, total_raw)

        time.sleep(2)

    if args.dry_run:
        print("\nDry run complete.")
        print(f"  Would query {len(ARTIFACT_QUERIES)} batches with {total_qids} unique QIDs")
        return

    # Sort by era, then name
    era_order = {"Prehistoric": 0, "Classical": 1, "Medieval": 2, "Early Modern": 3, "Modern": 4, "Contemporary": 5}
    all_entities.sort(key=lambda e: (era_order.get(e["era"], 9), e["name"]))

    # Compute statistics
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

    # Write final output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_data = {
        "_meta": {
            "source": "Wikidata SPARQL (query.wikidata.org)",
            "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "version": "1.0",
            "total_raw_results": total_raw,
            "total_unique_entities": len(all_entities),
            "label": "Text",
            "classCode": 7,
            "classHeading": "Artifacts & Texts",
            "type_qids_queried": total_qids,
            "batches_queried": len(ARTIFACT_QUERIES),
            "division_counts": dict(sorted(div_counts.items())),
            "era_counts": dict(sorted(era_counts.items())),
            "significance_distribution": dict(sorted(sig_dist.items())),
            "continent_counts": dict(sorted(continent_counts.items())),
            "significance_scale": {
                "1-2": "Minor -- documented but limited global impact",
                "3-4": "Moderate -- nationally significant",
                "5-6": "Notable -- regionally or thematically important",
                "7-8": "Major -- globally recognized",
                "9-10": "Landmark -- world-defining artifact or text",
            },
            "inAppwrite_note": "All entities have inAppwrite=false. Use historicalSignificance.score to prioritize for Appwrite seeding.",
            "note": "Comprehensive Wikidata artifacts & texts fetch v1.0 covering all Class 7 divisions (710-785).",
        },
        "entities": all_entities,
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    # Clean up progress file
    progress_path = output_path.with_suffix(".progress.json")
    if progress_path.exists():
        progress_path.unlink()

    # Print summary
    print()
    print("=" * 70)
    print("  Fetch Complete -- v1.0")
    print("=" * 70)
    print(f"  Raw results:       {total_raw}")
    print(f"  Unique entities:   {len(all_entities)}")
    print(f"  Output:            {output_path}")
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
    print("  Top 15 by historical significance:")
    for i, e in enumerate(top15, 1):
        sig = e["historicalSignificance"]
        print(f"    {i:2d}. [{sig['score']:2d} {sig['label']:>8s}] {e['name']}")


if __name__ == "__main__":
    main()
