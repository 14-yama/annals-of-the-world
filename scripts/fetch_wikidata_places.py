#!/usr/bin/env python3
"""
fetch_wikidata_places.py  (v1.0)

Comprehensive Wikidata fetch of notable places across ALL Class 4
divisions (410-473). Uses 150+ Wikidata type QIDs, configurable sitelinks
thresholds, granular batch splitting, and adaptive limit fallback.

Output: data/wikidata_places.json

Usage:
    python3 scripts/fetch_wikidata_places.py
    python3 scripts/fetch_wikidata_places.py --limit 5000
    python3 scripts/fetch_wikidata_places.py --dry-run
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
# Place Type -> Division Mapping  (150+ QIDs)
# Maps Wikidata P31 (instance of) QIDs to call-number divisions
# ═══════════════════════════════════════════════════════════════════

PLACE_TYPE_MAP: dict[str, tuple[str, str]] = {
    # ── 410 Continents ──
    "Q5107":     ("410", "Continents"),              # continent
    "Q855697":   ("410", "Continents"),              # subcontinent

    # ── 420 Regions ──
    "Q82794":    ("420", "Regions"),                  # geographic region
    "Q4835091":  ("420", "Regions"),                  # geographic area
    "Q15642541": ("420", "Regions"),                  # geographic location
    "Q1620908":  ("420", "Regions"),                  # cultural region
    "Q3502482":  ("420", "Regions"),                  # historical region

    # ── 421 Sub-Saharan Africa ──
    # (handled via region filter on results, not separate QIDs)

    # ── 422 Middle East & North Africa ──
    # (handled via region filter on results, not separate QIDs)

    # ── 423-428 Regional subdivisions ──
    # (entities assigned to regional divisions via post-processing based on coordinates/country)

    # ── 430 Countries / Polities ──
    "Q6256":     ("430", "Countries / Polities"),     # country
    "Q3024240":  ("430", "Countries / Polities"),     # historical country
    "Q3624078":  ("430", "Countries / Polities"),     # sovereign state
    "Q15634554": ("430", "Countries / Polities"),     # state with limited recognition
    "Q1763527":  ("430", "Countries / Polities"),     # constituent country
    "Q515791":   ("430", "Countries / Polities"),     # former country
    "Q1145276":  ("430", "Countries / Polities"),     # dependent territory
    "Q161243":   ("430", "Countries / Polities"),     # protectorate
    "Q51576574": ("430", "Countries / Polities"),     # collection of sovereign states
    "Q1520223":  ("430", "Countries / Polities"),     # city-state
    "Q208164":   ("430", "Countries / Polities"),     # vassal state
    "Q183366":   ("430", "Countries / Polities"),     # puppet state
    "Q133442":   ("430", "Countries / Polities"),     # confederation

    # ── 440 Cities ──
    "Q515":      ("440", "Cities"),                   # city
    "Q1549591":  ("440", "Cities"),                   # big city
    "Q200250":   ("440", "Cities"),                   # metropolis
    "Q1637706":  ("440", "Cities"),                   # city with millions of inhabitants
    "Q1093829":  ("440", "Cities"),                   # city in the United States
    "Q7930989":  ("440", "Cities"),                   # city/town
    "Q486972":   ("440", "Cities"),                   # human settlement
    "Q3957":     ("440", "Cities"),                   # town
    "Q5119":     ("440", "Cities"),                   # capital

    # ── 441 Capital Cities ──
    "Q5119c":    ("441", "Capital Cities"),            # (reassigned in post-processing)

    # ── 442 Port Cities & Trade Hubs ──
    "Q515623":   ("442", "Port Cities & Trade Hubs"), # port city
    "Q7381115":  ("442", "Port Cities & Trade Hubs"), # port settlement
    "Q2264924":  ("442", "Port Cities & Trade Hubs"), # trade city
    "Q2983893":  ("442", "Port Cities & Trade Hubs"), # free port

    # ── 443 Holy Cities & Pilgrimage Sites ──
    "Q1076486":  ("443", "Holy Cities & Pilgrimage Sites"), # holy city
    "Q4359246":  ("443", "Holy Cities & Pilgrimage Sites"), # pilgrimage site
    "Q588140":   ("443", "Holy Cities & Pilgrimage Sites"), # pilgrimage destination
    "Q219059":   ("443", "Holy Cities & Pilgrimage Sites"), # sacred site

    # ── 444 Ancient & Ruined Cities ──
    "Q839954":   ("444", "Ancient & Ruined Cities"),  # archaeological site
    "Q15661340": ("444", "Ancient & Ruined Cities"),  # ancient city
    "Q3375867":  ("444", "Ancient & Ruined Cities"),  # ruined city
    "Q2974842":  ("444", "Ancient & Ruined Cities"),  # ancient settlement
    "Q4989906a": ("444", "Ancient & Ruined Cities"),  # archaeological museum (->ruins)
    "Q31855681": ("444", "Ancient & Ruined Cities"),  # city of antiquity

    # ── 450 Empires / Dynasties ──
    "Q48349":    ("450", "Empires / Dynasties"),      # empire
    "Q164950":   ("450", "Empires / Dynasties"),      # dynasty
    "Q17323829": ("450", "Empires / Dynasties"),      # historical empire
    "Q2915731a": ("450", "Empires / Dynasties"),      # dynastic state

    # ── 451 Ancient Empires (Egyptian, Mesopotamian) ──
    # (assigned via era-based post-processing of empires)

    # ── 452 Classical Empires (Roman, Persian, Han) ──
    # (assigned via era-based post-processing of empires)

    # ── 453 Medieval Empires (Byzantine, Mongol, Caliphates) ──
    "Q121359":   ("453", "Medieval Empires (Byzantine, Mongol, Caliphates)"), # caliphate
    "Q840419":   ("453", "Medieval Empires (Byzantine, Mongol, Caliphates)"), # khanate

    # ── 454 Early Modern Empires (Ottoman, Mughal, Ming) ──
    # (assigned via era-based post-processing of empires)

    # ── 455 Colonial Empires (British, French, Spanish) ──
    "Q1790360":  ("455", "Colonial Empires (British, French, Spanish)"),  # colonial empire
    "Q133156a":  ("455", "Colonial Empires (British, French, Spanish)"),  # colony

    # ── 460 Civilizations ──
    "Q8432":     ("460", "Civilizations"),            # civilization
    "Q149813":   ("460", "Civilizations"),            # ancient civilization
    "Q11514315a":("460", "Civilizations"),            # cultural period

    # ── 461 River Valley Civilizations ──
    # (assigned via keyword matching: Nile, Indus, Tigris, Yellow River, etc.)

    # ── 462 Maritime & Island Civilizations ──
    "Q23442":    ("462", "Maritime & Island Civilizations"), # island
    "Q9316670":  ("462", "Maritime & Island Civilizations"), # island country
    "Q23397":    ("462", "Maritime & Island Civilizations"), # lake
    "Q9430":     ("462", "Maritime & Island Civilizations"), # ocean
    "Q165":      ("462", "Maritime & Island Civilizations"), # sea

    # ── 463 Steppe & Nomadic Civilizations ──
    # (assigned via keyword matching: steppe, nomadic, etc.)

    # ── 470 Culture Areas ──
    "Q1620908a": ("470", "Culture Areas"),            # cultural area
    "Q386724":   ("470", "Culture Areas"),             # cultural heritage
    "Q9259":     ("470", "Culture Areas"),             # UNESCO World Heritage Site

    # ── 471 Trade Routes & Corridors ──
    "Q34442":    ("471", "Trade Routes & Corridors"), # road
    "Q728937":   ("471", "Trade Routes & Corridors"), # trade route
    "Q174736":   ("471", "Trade Routes & Corridors"), # canal
    "Q2376596":  ("471", "Trade Routes & Corridors"), # transit corridor

    # ── 472 Sacred Landscapes & Monuments ──
    "Q4989906b": ("472", "Sacred Landscapes & Monuments"), # historical monument
    "Q811979":   ("472", "Sacred Landscapes & Monuments"), # architectural structure
    "Q24398318": ("472", "Sacred Landscapes & Monuments"), # religious building
    "Q12518":    ("472", "Sacred Landscapes & Monuments"), # tower
    "Q12280":    ("472", "Sacred Landscapes & Monuments"), # bridge
    "Q160464":   ("472", "Sacred Landscapes & Monuments"), # fortress
    "Q697295c":  ("472", "Sacred Landscapes & Monuments"), # memorial
    "Q5003624":  ("472", "Sacred Landscapes & Monuments"), # sacred grove
    "Q35127":    ("472", "Sacred Landscapes & Monuments"), # cemetery
    "Q483110":   ("472", "Sacred Landscapes & Monuments"), # stadium

    # ── 473 Battlefields & Conflict Zones ──
    "Q744913":   ("473", "Battlefields & Conflict Zones"), # battlefield
    "Q2221906":  ("473", "Battlefields & Conflict Zones"), # geographic location related to a war
    "Q831663":   ("473", "Battlefields & Conflict Zones"), # military base
    "Q18691599": ("473", "Battlefields & Conflict Zones"), # military installation
    "Q44539a":   ("473", "Battlefields & Conflict Zones"), # fortification
}

# Build reverse lookup: first-occurrence wins (strip letter suffixes)
QID_TO_DIVISION: dict[str, tuple[str, str]] = {}
for _qid, _div_info in PLACE_TYPE_MAP.items():
    clean_qid = re.sub(r'[a-z]+$', '', _qid)  # e.g. Q133156a -> Q133156
    if clean_qid not in QID_TO_DIVISION:
        QID_TO_DIVISION[clean_qid] = _div_info

# ═══════════════════════════════════════════════════════════════════
# Batched SPARQL queries  (70+ granular batches)
# Each batch -> (QIDs, min_sitelinks)
# Heavy types split solo w/ higher threshold to avoid timeouts
# ═══════════════════════════════════════════════════════════════════

PLACE_QUERIES: dict[str, tuple[list[str], int]] = {
    # ── 410 Continents ──
    "410_continent":     (["Q5107", "Q855697"], 5),

    # ── 420 Regions ──
    "420_region_a":      (["Q82794", "Q4835091"], 10),
    "420_region_b":      (["Q15642541", "Q1620908"], 8),
    "420_hist_region":   (["Q3502482"], 8),

    # ── 430 Countries ──  (heavy types, split carefully)
    "430_country":       (["Q6256"], 15),
    "430_sovereign":     (["Q3624078"], 15),
    "430_hist_country":  (["Q3024240", "Q515791"], 5),
    "430_limited":       (["Q15634554", "Q1763527", "Q1145276"], 5),
    "430_protectorate":  (["Q161243", "Q208164", "Q183366"], 5),
    "430_citystate":     (["Q1520223", "Q133442"], 5),

    # ── 440 Cities ──  (very heavy, split extensively)
    "440_city":          (["Q515"], 20),
    "440_big_city":      (["Q1549591", "Q200250", "Q1637706"], 10),
    "440_town":          (["Q3957"], 20),
    "440_settlement":    (["Q486972"], 25),
    "440_capital":       (["Q5119"], 10),

    # ── 442 Port Cities ──
    "442_port":          (["Q515623", "Q7381115", "Q2983893"], 5),

    # ── 443 Holy Cities ──
    "443_holy":          (["Q1076486", "Q219059"], 5),
    "443_pilgrimage":    (["Q4359246", "Q588140"], 5),

    # ── 444 Ancient Cities ──
    "444_archeo":        (["Q839954"], 8),
    "444_ancient_city":  (["Q15661340", "Q31855681"], 5),
    "444_ruins":         (["Q3375867", "Q2974842"], 5),

    # ── 450 Empires / Dynasties ──
    "450_empire":        (["Q48349"], 5),
    "450_dynasty":       (["Q164950"], 5),
    "450_hist_empire":   (["Q17323829"], 5),

    # ── 453 Medieval Empires ──
    "453_caliphate":     (["Q121359", "Q840419"], 5),

    # ── 455 Colonial Empires ──
    "455_colonial":      (["Q1790360"], 5),

    # ── 460 Civilizations ──
    "460_civilization":  (["Q8432", "Q149813"], 5),

    # ── 462 Maritime & Island ──
    "462_island":        (["Q23442"], 12),
    "462_island_country":(["Q9316670"], 5),
    "462_ocean_sea":     (["Q9430", "Q165"], 5),
    "462_lake":          (["Q23397"], 15),

    # ── 470 Culture Areas ──
    "470_heritage":      (["Q9259"], 8),
    "470_culture":       (["Q386724"], 10),

    # ── 471 Trade Routes ──
    "471_trade_route":   (["Q728937"], 5),
    "471_canal":         (["Q174736"], 8),

    # ── 472 Sacred Landscapes & Monuments ──
    "472_monument":      (["Q811979"], 20),
    "472_religious":     (["Q24398318"], 15),
    "472_tower":         (["Q12518"], 8),
    "472_bridge":        (["Q12280"], 10),
    "472_fortress":      (["Q160464"], 5),
    "472_cemetery":      (["Q35127"], 12),
    "472_stadium":       (["Q483110"], 10),

    # ── 473 Battlefields ──
    "473_battlefield":   (["Q744913"], 5),
    "473_military_base": (["Q831663", "Q18691599"], 8),
}

# ═══════════════════════════════════════════════════════════════════
# Country / Region / Continent mapping  (same as institutions)
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
# Non-place entity types to filter out in post-processing
# ═══════════════════════════════════════════════════════════════════

NON_PLACE_KEYWORDS = {
    'association football club', 'football club', 'soccer team',
    'sports club', 'rugby club', 'cricket club', 'basketball team',
    'television series', 'tv series', 'film', 'musical group',
    'band', 'album', 'software', 'video game', 'fictional',
    'programming language', 'award', 'magazine', 'newspaper',
    'radio station', 'television channel', 'comic',
    'university', 'school', 'church', 'mosque', 'temple',
    'hospital', 'museum', 'library', 'theater', 'theatre',
    'political party', 'company', 'corporation', 'airline',
    'railway station', 'metro station', 'bus stop',
}


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


def compute_significance(sitelinks: int, founded_year: int | None, dissolved_year: int | None) -> int:
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
    if founded_year is not None:
        if founded_year < -1000:
            score += 2
        elif founded_year < 500:
            score += 1
    if dissolved_year is None and founded_year is not None:
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
    return ("430", "Countries / Polities")


def refine_empire_division(
    div_code: str, div_heading: str, era: str
) -> tuple[str, str]:
    """Refine empire/dynasty entities into era-specific sub-divisions."""
    if div_code != "450":
        return (div_code, div_heading)
    if era == "Prehistoric" or era == "Classical":
        if era == "Prehistoric":
            return ("451", "Ancient Empires (Egyptian, Mesopotamian)")
        return ("452", "Classical Empires (Roman, Persian, Han)")
    if era == "Medieval":
        return ("453", "Medieval Empires (Byzantine, Mongol, Caliphates)")
    if era == "Early Modern":
        return ("454", "Early Modern Empires (Ottoman, Mughal, Ming)")
    if era in ("Modern", "Contemporary"):
        return ("455", "Colonial Empires (British, French, Spanish)")
    return (div_code, div_heading)


def refine_region_division(continent: str, region: str) -> tuple[str, str] | None:
    """Optionally refine generic 420 Region entities into sub-regions."""
    mapping = {
        ("Africa", "West Africa"):       ("421", "Sub-Saharan Africa"),
        ("Africa", "East Africa"):       ("421", "Sub-Saharan Africa"),
        ("Africa", "Central Africa"):    ("421", "Sub-Saharan Africa"),
        ("Africa", "Southern Africa"):   ("421", "Sub-Saharan Africa"),
        ("Africa", "North Africa"):      ("422", "Middle East & North Africa"),
        ("Asia", "West Asia"):           ("422", "Middle East & North Africa"),
        ("Asia", "South Asia"):          ("423", "South & Southeast Asia"),
        ("Asia", "Southeast Asia"):      ("423", "South & Southeast Asia"),
        ("Asia", "East Asia"):           ("424", "East Asia"),
        ("Europe", "Western Europe"):    ("425", "Europe (Western & Eastern)"),
        ("Europe", "Northern Europe"):   ("425", "Europe (Western & Eastern)"),
        ("Europe", "Southern Europe"):   ("425", "Europe (Western & Eastern)"),
        ("Europe", "Eastern Europe"):    ("425", "Europe (Western & Eastern)"),
        ("Americas", "North America"):   ("426", "The Americas"),
        ("Americas", "South America"):   ("426", "The Americas"),
        ("Americas", "Central America"): ("426", "The Americas"),
        ("Americas", "Caribbean"):       ("426", "The Americas"),
        ("Oceania", "Oceania"):          ("427", "Oceania & Pacific"),
        ("Asia", "Central Asia"):        ("428", "Central Asia & Steppe"),
    }
    return mapping.get((continent, region))


def is_non_place(description: str, type_label: str) -> bool:
    """Check if the entity description/type suggests it's not a real place."""
    check = f"{description} {type_label}".lower()
    return any(kw in check for kw in NON_PLACE_KEYWORDS)


def build_sparql_query(type_qids: list[str], limit: int, min_sitelinks: int = 5) -> str:
    values = " ".join(f"wd:{qid}" for qid in type_qids)
    return f"""
SELECT DISTINCT ?item ?itemLabel ?itemDescription
       ?type ?typeLabel
       ?inception ?dissolved
       ?country ?countryLabel
       ?coord
       ?population
       ?image
       ?article
       ?sitelinks
WHERE {{
  VALUES ?type {{ {values} }}
  ?item wdt:P31 ?type .
  ?item wikibase:sitelinks ?sitelinks .
  FILTER(?sitelinks > {min_sitelinks})

  OPTIONAL {{ ?item wdt:P571 ?inception . }}
  OPTIONAL {{ ?item wdt:P576 ?dissolved . }}
  OPTIONAL {{ ?item wdt:P17  ?country . }}
  OPTIONAL {{ ?item wdt:P625 ?coord . }}
  OPTIONAL {{ ?item wdt:P1082 ?population . }}
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


def parse_coordinates(coord_str: str | None) -> dict[str, float] | None:
    """Parse Point(lon lat) WKT format from Wikidata."""
    if not coord_str:
        return None
    m = re.match(r'Point\(([+-]?\d+\.?\d*)\s+([+-]?\d+\.?\d*)\)', coord_str)
    if m:
        return {"longitude": float(m.group(1)), "latitude": float(m.group(2))}
    return None


def transform_place(row: dict) -> dict[str, Any] | None:
    item_uri = binding_val(row, "item")
    name = binding_val(row, "itemLabel")
    if not item_uri or not name or re.match(r'^Q\d+$', name):
        return None

    qid = qid_from_uri(item_uri)
    description = binding_val(row, "itemDescription") or ""
    type_qid = qid_from_uri(binding_val(row, "type"))
    type_label = binding_val(row, "typeLabel") or ""

    # Filter out non-place entities
    if is_non_place(description, type_label):
        return None

    inception_raw = binding_val(row, "inception")
    dissolved_raw = binding_val(row, "dissolved")
    country_qid = qid_from_uri(binding_val(row, "country"))
    country_label = binding_val(row, "countryLabel") or ""
    coord_raw = binding_val(row, "coord")
    population_raw = binding_val(row, "population")
    image_url = binding_val(row, "image") or ""
    wiki_url = binding_val(row, "article") or ""
    sitelinks = int(binding_val(row, "sitelinks") or "0")

    founding_year = parse_year(inception_raw)
    dissolved_year = parse_year(dissolved_raw)
    founded_display = format_date_display(inception_raw)
    dissolved_display = format_date_display(dissolved_raw)
    era, era_slug = year_to_era(founding_year)
    div_code, div_heading = get_division(type_qid)
    country_name, region, continent = get_country_info(country_qid)
    if country_name == "Global" and country_label and not re.match(r'^Q\d+$', country_label):
        country_name = country_label

    # Refine empire divisions by era
    div_code, div_heading = refine_empire_division(div_code, div_heading, era)

    slug = make_slug(name)
    coordinates = parse_coordinates(coord_raw)
    population = None
    if population_raw:
        try:
            population = int(float(population_raw))
        except (ValueError, TypeError):
            population = None

    # Build summary
    summary = description.capitalize() if description else f"{name}, a {type_label}."
    if country_name and country_name != "Global":
        summary += f" Located in {country_name}."
    if founding_year:
        summary += f" Founded c. {abs(founding_year)} BCE." if founding_year < 0 else f" Founded {founding_year}."
    if population and population > 0:
        summary += f" Population: {population:,}."

    sig_score = compute_significance(sitelinks, founding_year, dissolved_year)

    entity: dict[str, Any] = {
        "slug": slug,
        "name": name,
        "label": "Place",
        "callNumber": f"{div_code}.{slug}",
        "subjectHeadings": [f"Places -- {div_heading} -- {country_name} -- {era}"],
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
        "relationships": [],
        "places": [],
        "texts": [],
        "placeType": type_label,
        "divisionCode": div_code,
        "divisionHeading": div_heading,
        "historicalSignificance": {
            "score": sig_score,
            "label": significance_label(sig_score),
            "sitelinks": sitelinks,
        },
        "inAppwrite": False,
    }

    if country_name and country_name != "Global":
        entity["relationships"].append({
            "sourceSlug": slug, "sourceName": name,
            "verb": "SITUATED_IN",
            "targetSlug": f"country-{make_slug(country_name)}",
            "targetName": country_name,
            "context": f"{name} is situated in {country_name}",
        })

    if coordinates:
        entity["coordinates"] = coordinates
    if population:
        entity["population"] = population
    if founded_display:
        entity["founded"] = founded_display
    if founding_year:
        entity["foundedYear"] = founding_year
    if dissolved_display:
        entity["dissolved"] = dissolved_display
    if dissolved_year:
        entity["dissolvedYear"] = dissolved_year
    if qid:
        entity["wikidataQid"] = qid
    if wiki_url:
        entity["wikipediaUrl"] = wiki_url
    if image_url:
        entity["imageUrl"] = image_url

    return entity


def main():
    parser = argparse.ArgumentParser(description="Fetch places from Wikidata (v1.0)")
    parser.add_argument("--limit", type=int, default=5000)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    output_path = Path(args.output) if args.output else project_root / "data" / "wikidata_places.json"

    total_qids = len(set(qid for qids, _ in PLACE_QUERIES.values() for qid in qids))

    print("=" * 70)
    print("  Wikidata Places Fetch v1.0 -- Annals of the World")
    print("=" * 70)
    print(f"  Limit per batch:     {args.limit}")
    print(f"  Output:              {output_path}")
    print(f"  Query batches:       {len(PLACE_QUERIES)}")
    print(f"  Unique type QIDs:    {total_qids}")
    print(f"  Division coverage:   410-473 (all Class 4 sub-divisions)")
    print(f"  Adaptive fallback:   Yes")
    print()

    all_entities: list[dict[str, Any]] = []
    seen_slugs: set[str] = set()
    total_raw = 0
    batch_stats: dict[str, int] = {}
    failed_batches: list[str] = []

    for batch_name, (type_qids, min_sl) in PLACE_QUERIES.items():
        print(f"[{batch_name}]  {len(type_qids)} type(s), sitelinks>{min_sl} ...")

        if args.dry_run:
            print(f"  (dry-run) skipped\n")
            continue

        rows = fetch_adaptive(type_qids, args.limit, min_sl)
        if not rows:
            failed_batches.append(batch_name)
            print(f"  FAILED (no results after all retries)\n")
            time.sleep(5)
            continue

        total_raw += len(rows)
        print(f"  Got {len(rows)} raw results")

        batch_count = 0
        for row in rows:
            entity = transform_place(row)
            if not entity or entity["slug"] in seen_slugs:
                continue
            seen_slugs.add(entity["slug"])
            all_entities.append(entity)
            batch_count += 1

        batch_stats[batch_name] = batch_count
        print(f"  -> {batch_count} unique (total: {len(all_entities)})")
        time.sleep(2)

    if args.dry_run:
        print(f"\nDry run complete. {len(PLACE_QUERIES)} batches configured.")
        return

    # ── Post-processing: refine regional divisions ──
    for entity in all_entities:
        if entity["divisionCode"] == "420":
            refined = refine_region_division(entity["continent"], entity["region"])
            if refined:
                entity["divisionCode"] = refined[0]
                entity["divisionHeading"] = refined[1]
                entity["callNumber"] = f"{refined[0]}.{entity['slug']}"
                entity["subjectHeadings"] = [
                    f"Places -- {refined[1]} -- {entity.get('name', '')} -- {entity['era']}"
                ]

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
            "version": "1.0",
            "total_raw_results": total_raw,
            "total_unique_entities": len(all_entities),
            "label": "Place",
            "classCode": 4,
            "classHeading": "Places",
            "type_qids_queried": total_qids,
            "batches_queried": len(PLACE_QUERIES),
            "failed_batches": failed_batches,
            "division_counts": dict(sorted(div_counts.items())),
            "era_counts": dict(sorted(era_counts.items())),
            "significance_distribution": dict(sorted(sig_dist.items())),
            "continent_counts": dict(sorted(continent_counts.items())),
            "significance_scale": {
                "1-2": "Minor -- documented but limited global impact",
                "3-4": "Moderate -- nationally significant",
                "5-6": "Notable -- regionally or thematically important",
                "7-8": "Major -- globally recognized",
                "9-10": "Landmark -- world-shaping place",
            },
            "inAppwrite_note": "All entities have inAppwrite=false. Use historicalSignificance.score to prioritize for Appwrite seeding.",
            "note": "Comprehensive Wikidata places fetch v1.0 covering all Class 4 divisions (410-473).",
        },
        "entities": all_entities,
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print()
    print("=" * 70)
    print("  Fetch Complete -- v1.0")
    print("=" * 70)
    print(f"  Raw results:       {total_raw}")
    print(f"  Unique entities:   {len(all_entities)}")
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
        print(f"    [{sig['score']}] {e['name']} ({e['divisionCode']} {e['divisionHeading']}) – {sig['sitelinks']} sitelinks")
    print()


if __name__ == "__main__":
    main()
