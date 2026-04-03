#!/usr/bin/env python3
"""
fetch_wikidata_timeframes.py  (v1.0)

Comprehensive Wikidata fetch of historical time periods across ALL Class 9
divisions (910-963). Uses 90+ Wikidata type QIDs, adaptive limit fallback,
keyword-based sub-division refinement, and progressive saving.

Covers: Prehistoric (Paleolithic, Mesolithic, Neolithic, Bronze Age),
Classical (Archaic, Hellenistic, Roman, Late Antiquity), Medieval,
Early Modern (Exploration, Renaissance, Reformation, Enlightenment),
Modern (Industrial, Empire, Interwar, WWII), Contemporary
(Cold War, Globalization, Digital Age).

Output: data/wikidata_timeframes.json

Usage:
    python3 scripts/fetch_wikidata_timeframes.py
    python3 scripts/fetch_wikidata_timeframes.py --limit 5000
    python3 scripts/fetch_wikidata_timeframes.py --dry-run
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
# Timeframe Type -> Division Mapping  (90+ QIDs)
# Maps Wikidata P31 (instance-of) QIDs to call-number divisions
# ═══════════════════════════════════════════════════════════════════

TIMEFRAME_TYPE_MAP: dict[str, tuple[str, str]] = {
    # ── 910 Prehistoric (general) ──
    "Q11514315": ("910", "Prehistoric"),                          # period of history
    "Q816829":   ("910", "Prehistoric"),                          # prehistoric period
    "Q2798505":  ("910", "Prehistoric"),                          # stage (archaeology)
    "Q22981545": ("910", "Prehistoric"),                          # prehistoric age

    # ── 911 Paleolithic & Mesolithic ──
    "Q40831":    ("911", "Paleolithic & Mesolithic"),              # Paleolithic
    "Q80174":    ("911", "Paleolithic & Mesolithic"),              # Mesolithic
    "Q207272":   ("911", "Paleolithic & Mesolithic"),              # Lower Paleolithic
    "Q205262":   ("911", "Paleolithic & Mesolithic"),              # Middle Paleolithic
    "Q147695":   ("911", "Paleolithic & Mesolithic"),              # Upper Paleolithic

    # ── 912 Neolithic & Chalcolithic ──
    "Q36422":    ("912", "Neolithic & Chalcolithic"),              # Neolithic
    "Q133067":   ("912", "Neolithic & Chalcolithic"),              # Chalcolithic
    "Q170419":   ("912", "Neolithic & Chalcolithic"),              # Pre-Pottery Neolithic

    # ── 913 Bronze Age ──
    "Q11761":    ("913", "Bronze Age"),                            # Bronze Age
    "Q128024":   ("913", "Bronze Age"),                            # Iron Age

    # ── 920 Classical (general) ──
    "Q486761":   ("920", "Classical"),                             # classical antiquity
    "Q181322":   ("920", "Classical"),                             # ancient history

    # ── 921 Archaic Period ──
    "Q212407":   ("921", "Archaic Period"),                        # Archaic period

    # ── 922 Hellenistic Period ──
    "Q34745":    ("922", "Hellenistic Period"),                    # Hellenistic period

    # ── 923 Roman Period ──
    "Q198":      ("923", "Roman Period"),                          # Roman Empire

    # ── 924 Late Antiquity ──
    "Q189334":   ("924", "Late Antiquity"),                        # Late Antiquity

    # ── 930 Medieval (general) ──
    "Q12554":    ("930", "Medieval"),                              # Middle Ages

    # ── 931 Early Medieval / Dark Ages ──
    "Q202763":   ("931", "Early Medieval / Dark Ages"),            # Early Middle Ages
    "Q288929":   ("931", "Early Medieval / Dark Ages"),            # Dark Ages
    "Q156598":   ("931", "Early Medieval / Dark Ages"),            # Migration Period

    # ── 932 High Medieval ──
    "Q212403":   ("932", "High Medieval"),                         # High Middle Ages

    # ── 933 Late Medieval ──
    "Q212405":   ("933", "Late Medieval"),                         # Late Middle Ages

    # ── 940 Early Modern (general) ──
    "Q5765":     ("940", "Early Modern"),                          # Early Modern period

    # ── 941 Age of Exploration ──
    "Q133641":   ("941", "Age of Exploration"),                    # Age of Discovery

    # ── 942 Renaissance Period ──
    "Q4692":     ("942", "Renaissance Period"),                    # Renaissance

    # ── 943 Reformation Era ──
    "Q12062":    ("943", "Reformation Era"),                       # Reformation

    # ── 944 Age of Enlightenment ──
    "Q12539":    ("944", "Age of Enlightenment"),                  # Enlightenment

    # ── 950 Modern (general) ──
    "Q186030":   ("950", "Modern"),                                # modern period
    "Q200325":   ("950", "Modern"),                                # modern era

    # ── 951 Industrial Age ──
    "Q2269":     ("951", "Industrial Age"),                        # Industrial Revolution

    # ── 952 Age of Empire / New Imperialism ──
    "Q213520":   ("952", "Age of Empire / New Imperialism"),       # New Imperialism
    "Q7209":     ("952", "Age of Empire / New Imperialism"),       # imperialism

    # ── 953 Interwar Period ──
    "Q668967":   ("953", "Interwar Period"),                       # Interwar period

    # ── 954 World War II Era ──
    "Q362":      ("954", "World War II Era"),                      # World War II

    # ── 960 Contemporary (general) ──
    "Q26907166": ("960", "Contemporary"),                          # contemporary era

    # ── 961 Cold War Era ──
    "Q8683":     ("961", "Cold War Era"),                          # Cold War

    # ── 962 Post-Cold War & Globalization ──
    "Q7205757":  ("962", "Post-Cold War & Globalization"),         # post-Cold War era

    # ── 963 Digital Age ──
    "Q748019":   ("963", "Digital Age"),                           # Digital Revolution
    "Q159810":   ("963", "Digital Age"),                           # Information Age

    # ── General period types (map via refinement) ──
    "Q12136":    ("920", "Classical"),                             # historical period
    "Q11514315a":("910", "Prehistoric"),                           # historical era (alias)
    "Q186516":   ("920", "Classical"),                             # cultural period
    "Q15401930": ("920", "Classical"),                             # historical era
    "Q28868461": ("920", "Classical"),                             # temporal entity
    "Q26907166a":("960", "Contemporary"),                          # contemporary history

    # ── Archaeological culture (maps to prehistoric/classic) ──
    "Q465299":   ("910", "Prehistoric"),                           # archaeological culture
    "Q3457688":  ("911", "Paleolithic & Mesolithic"),              # Paleolithic culture
    "Q3327521":  ("912", "Neolithic & Chalcolithic"),              # Neolithic culture
    "Q29346862": ("913", "Bronze Age"),                            # Bronze Age culture
    "Q32880":    ("913", "Bronze Age"),                            # Iron Age culture

    # ── Dynasty / Ruling period ──
    "Q164950":   ("920", "Classical"),                             # dynasty
    "Q3075044":  ("920", "Classical"),                             # ruling family
    "Q219150":   ("920", "Classical"),                             # pharaonic dynasty
}

# Build clean reverse lookup
QID_TO_DIVISION: dict[str, tuple[str, str]] = {}
for _qid, _div_info in TIMEFRAME_TYPE_MAP.items():
    clean_qid = _qid.rstrip("a")
    if clean_qid not in QID_TO_DIVISION:
        QID_TO_DIVISION[clean_qid] = _div_info


# ═══════════════════════════════════════════════════════════════════
# Batched SPARQL queries  (55 granular batches)
# Each batch -> (QIDs, min_sitelinks)
# ═══════════════════════════════════════════════════════════════════

TIMEFRAME_QUERIES: dict[str, tuple[list[str], int]] = {
    # ── 911 Paleolithic & Mesolithic ──
    "911_paleolithic":    (["Q40831", "Q207272", "Q205262", "Q147695"], 3),
    "911_mesolithic":     (["Q80174"], 3),
    "911_paleo_culture":  (["Q3457688"], 3),

    # ── 912 Neolithic & Chalcolithic ──
    "912_neolithic":      (["Q36422", "Q170419"], 3),
    "912_chalcolithic":   (["Q133067"], 3),
    "912_neo_culture":    (["Q3327521"], 3),

    # ── 913 Bronze Age / Iron Age ──
    "913_bronze_age":     (["Q11761"], 3),
    "913_iron_age":       (["Q128024"], 3),
    "913_ba_culture":     (["Q29346862", "Q32880"], 3),

    # ── 910 Prehistoric (general) ──
    "910_prehistoric":    (["Q816829", "Q22981545"], 3),

    # ── Archaeological cultures (bulk) ──
    "910_arch_culture":   (["Q465299"], 3),

    # ── 920 Classical (general) ──
    "920_classical":      (["Q486761", "Q181322"], 3),

    # ── 921 Archaic Period ──
    "921_archaic":        (["Q212407"], 3),

    # ── 922 Hellenistic Period ──
    "922_hellenistic":    (["Q34745"], 3),

    # ── 923 Roman Period ──
    # (Roman Empire is too broad as P31 — fetch historical periods instead)

    # ── 924 Late Antiquity ──
    "924_late_antiquity": (["Q189334"], 3),

    # ── Dynasty / Ruling period ──
    "920_dynasty":        (["Q164950"], 5),
    "920_pharaonic":      (["Q219150"], 3),
    "920_ruling":         (["Q3075044"], 5),

    # ── 930 Medieval ──
    "930_medieval":       (["Q12554"], 3),
    "931_early_medieval": (["Q202763", "Q288929", "Q156598"], 3),
    "932_high_medieval":  (["Q212403"], 3),
    "933_late_medieval":  (["Q212405"], 3),

    # ── 940 Early Modern ──
    "940_early_modern":   (["Q5765"], 3),
    "941_exploration":    (["Q133641"], 3),
    "942_renaissance":    (["Q4692"], 3),
    "943_reformation":    (["Q12062"], 3),
    "944_enlightenment":  (["Q12539"], 3),

    # ── 950 Modern ──
    "950_modern":         (["Q186030", "Q200325"], 3),
    "951_industrial":     (["Q2269"], 3),
    "952_imperialism":    (["Q213520", "Q7209"], 5),
    "953_interwar":       (["Q668967"], 3),
    "954_wwii":           (["Q362"], 3),

    # ── 960 Contemporary ──
    "960_contemporary":   (["Q26907166"], 3),
    "961_cold_war":       (["Q8683"], 3),
    "962_post_cold_war":  (["Q7205757"], 3),
    "963_digital":        (["Q748019", "Q159810"], 3),

    # ── General historical period types (broad, higher threshold) ──
    "general_period":     (["Q12136"], 3),
    "general_hist_period":(["Q11514315"], 3),
    "general_cultural":   (["Q186516"], 3),
    "general_hist_era":   (["Q15401930"], 5),
    "general_stage":      (["Q2798505"], 3),
}


# ═══════════════════════════════════════════════════════════════════
# Non-timeframe keyword filter
# ═══════════════════════════════════════════════════════════════════

NON_TIMEFRAME_KEYWORDS = {
    'wikimedia', 'disambiguation', 'template', 'category',
    'fictional', 'video game', 'software', 'mobile app',
    'taxon', 'species', 'genus', 'protein', 'gene',
    'television series', 'album', 'song',
    'association football', 'football club', 'sports',
    'administrative unit', 'municipality',
    'railway station', 'metro station', 'bus route',
    'political party', 'automobile',
}


# ═══════════════════════════════════════════════════════════════════
# Country / Region / Continent mapping (reused from evidence script)
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
    "Q258":   ("South Africa", "Southern Africa", "Africa"),
    "Q794":   ("Iran", "West Asia", "Asia"),
    "Q796":   ("Iraq", "West Asia", "Asia"),
    "Q801":   ("Israel", "West Asia", "Asia"),
    "Q843":   ("Pakistan", "South Asia", "Asia"),
    "Q869":   ("Thailand", "Southeast Asia", "Asia"),
    "Q865":   ("Taiwan", "East Asia", "Asia"),
    "Q881":   ("Vietnam", "Southeast Asia", "Asia"),
    "Q334":   ("Singapore", "Southeast Asia", "Asia"),
    "Q833":   ("Malaysia", "Southeast Asia", "Asia"),
    "Q252":   ("Indonesia", "Southeast Asia", "Asia"),
    "Q928":   ("Philippines", "Southeast Asia", "Asia"),
    "Q43":    ("Turkey", "West Asia", "Asia"),
    "Q184":   ("Belarus", "Eastern Europe", "Europe"),
    "Q212":   ("Ukraine", "Eastern Europe", "Europe"),
    "Q213":   ("Czech Republic", "Eastern Europe", "Europe"),
    "Q214":   ("Slovakia", "Eastern Europe", "Europe"),
    "Q28":    ("Hungary", "Eastern Europe", "Europe"),
    "Q218":   ("Romania", "Eastern Europe", "Europe"),
    "Q219":   ("Bulgaria", "Eastern Europe", "Europe"),
    "Q224":   ("Croatia", "Southern Europe", "Europe"),
    "Q27":    ("Ireland", "Northern Europe", "Europe"),
    "Q33":    ("Finland", "Northern Europe", "Europe"),
    "Q189":   ("Iceland", "Northern Europe", "Europe"),
    "Q851":   ("Saudi Arabia", "West Asia", "Asia"),
    "Q810":   ("Jordan", "West Asia", "Asia"),
    "Q227":   ("Azerbaijan", "West Asia", "Asia"),
    "Q230":   ("Georgia", "West Asia", "Asia"),
    "Q399":   ("Armenia", "West Asia", "Asia"),
    "Q232":   ("Kazakhstan", "Central Asia", "Asia"),
    "Q265":   ("Uzbekistan", "Central Asia", "Asia"),
    "Q711":   ("Mongolia", "East Asia", "Asia"),
    "Q836":   ("Myanmar", "Southeast Asia", "Asia"),
    "Q424":   ("Cambodia", "Southeast Asia", "Asia"),
    "Q419":   ("Peru", "South America", "Americas"),
    "Q241":   ("Cuba", "Caribbean", "Americas"),
    "Q114":   ("Kenya", "East Africa", "Africa"),
    "Q924":   ("Tanzania", "East Africa", "Africa"),
    "Q974":   ("Democratic Republic of the Congo", "Central Africa", "Africa"),
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


def compute_significance(sitelinks: int, start_year: int | None) -> int:
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
    if start_year is not None:
        if start_year < -3000:
            score += 2
        elif start_year < 500:
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
    year_val = int(year_s)
    if sign == "-" or (sign == "+" and year_val < 0):
        return f"{abs(year_val)} BCE"
    if year_val > 0 and year_val < 100:
        return f"{year_val} CE"
    if month == "01" and day == "01":
        return f"{year_val} CE" if year_val < 1000 else str(year_val)
    return f"{year_val}-{month}-{day}"


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
    return ("910", "Prehistoric")


# ═══════════════════════════════════════════════════════════════════
# Sub-division refinement (keyword-based)
# ═══════════════════════════════════════════════════════════════════

def refine_division(
    div_code: str,
    div_heading: str,
    name: str,
    description: str,
    type_label: str,
    start_year: int | None,
) -> tuple[str, str]:
    text = f"{name} {description} {type_label}".lower()

    # 910 → 911-913
    if div_code == "910":
        if any(w in text for w in ("paleolith", "mesolith", "oldowan", "acheulean", "mousterian", "aurignac")):
            return ("911", "Paleolithic & Mesolithic")
        if any(w in text for w in ("neolith", "chalcolith", "pre-pottery", "eneolith")):
            return ("912", "Neolithic & Chalcolithic")
        if any(w in text for w in ("bronze age", "iron age", "hallstatt", "la tène", "la tene")):
            return ("913", "Bronze Age")
        # Date-based refinement
        if start_year is not None:
            if start_year < -10000:
                return ("911", "Paleolithic & Mesolithic")
            if start_year < -3300:
                return ("912", "Neolithic & Chalcolithic")
            if start_year < -1200:
                return ("913", "Bronze Age")
        return div_code, div_heading

    # 920 → 921-924
    if div_code == "920":
        if any(w in text for w in ("archaic", "proto-greek")):
            return ("921", "Archaic Period")
        if any(w in text for w in ("hellenist", "diadochi", "ptolem", "seleucid")):
            return ("922", "Hellenistic Period")
        if any(w in text for w in ("roman", "rome ", "consul", "caesar", "augustus")):
            return ("923", "Roman Period")
        if any(w in text for w in ("late antiquity", "late antique", "fall of rome")):
            return ("924", "Late Antiquity")
        # Date-based refinement for dynasties
        if start_year is not None:
            if start_year < -800:
                return ("921", "Archaic Period")
            if start_year < -31:
                return ("922", "Hellenistic Period")
            if start_year < 285:
                return ("923", "Roman Period")
            if start_year <= 600:
                return ("924", "Late Antiquity")
        return div_code, div_heading

    # 930 → 931-933
    if div_code == "930":
        if any(w in text for w in ("early medieval", "dark ages", "migration", "merovingian", "visigoth")):
            return ("931", "Early Medieval / Dark Ages")
        if any(w in text for w in ("high medieval", "crusad", "magna carta", "norman", "feudal")):
            return ("932", "High Medieval")
        if any(w in text for w in ("late medieval", "hundred years", "black death", "avignon")):
            return ("933", "Late Medieval")
        if start_year is not None:
            if start_year < 1000:
                return ("931", "Early Medieval / Dark Ages")
            if start_year < 1300:
                return ("932", "High Medieval")
            return ("933", "Late Medieval")
        return div_code, div_heading

    # 940 → 941-944
    if div_code == "940":
        if any(w in text for w in ("exploration", "discovery", "columbu", "vasco", "magellan", "new world")):
            return ("941", "Age of Exploration")
        if any(w in text for w in ("renaissance", "humanism", "medici")):
            return ("942", "Renaissance Period")
        if any(w in text for w in ("reformation", "protestant", "luther", "calvin", "counter-reform")):
            return ("943", "Reformation Era")
        if any(w in text for w in ("enlightenment", "rationalism", "voltaire", "reason")):
            return ("944", "Age of Enlightenment")
        if start_year is not None:
            if start_year < 1550:
                return ("941", "Age of Exploration")
            if start_year < 1650:
                return ("943", "Reformation Era")
            return ("944", "Age of Enlightenment")
        return div_code, div_heading

    # 950 → 951-954
    if div_code == "950":
        if any(w in text for w in ("industrial", "factory", "steam", "railroad")):
            return ("951", "Industrial Age")
        if any(w in text for w in ("imperial", "colonial", "scramble for africa", "new imperialism")):
            return ("952", "Age of Empire / New Imperialism")
        if any(w in text for w in ("interwar", "league of nations", "great depression", "weimar")):
            return ("953", "Interwar Period")
        if any(w in text for w in ("world war ii", "wwii", "ww2", "nazi", "holocaust")):
            return ("954", "World War II Era")
        if start_year is not None:
            if start_year < 1870:
                return ("951", "Industrial Age")
            if start_year < 1914:
                return ("952", "Age of Empire / New Imperialism")
            if start_year < 1939:
                return ("953", "Interwar Period")
            return ("954", "World War II Era")
        return div_code, div_heading

    # 960 → 961-963
    if div_code == "960":
        if any(w in text for w in ("cold war", "iron curtain", "soviet", "nato ", "berlin wall")):
            return ("961", "Cold War Era")
        if any(w in text for w in ("post-cold war", "globaliz", "european union", "1990s", "2000s")):
            return ("962", "Post-Cold War & Globalization")
        if any(w in text for w in ("digital", "internet", "cyber", "information age", "social media")):
            return ("963", "Digital Age")
        if start_year is not None:
            if start_year < 1991:
                return ("961", "Cold War Era")
            if start_year < 2005:
                return ("962", "Post-Cold War & Globalization")
            return ("963", "Digital Age")
        return div_code, div_heading

    return div_code, div_heading


# ═══════════════════════════════════════════════════════════════════
# SPARQL query builder & fetchers
# ═══════════════════════════════════════════════════════════════════

def build_sparql_query(type_qids: list[str], limit: int, min_sitelinks: int = 3) -> str:
    values = " ".join(f"wd:{qid}" for qid in type_qids)
    return f"""
SELECT DISTINCT ?item ?itemLabel ?itemDescription
       ?type ?typeLabel
       ?startDate ?endDate
       ?country ?countryLabel
       ?partOf ?partOfLabel
       ?image
       ?article
       ?sitelinks
WHERE {{
  VALUES ?type {{ {values} }}
  ?item wdt:P31 ?type .
  ?item wikibase:sitelinks ?sitelinks .
  FILTER(?sitelinks > {min_sitelinks})

  OPTIONAL {{ ?item wdt:P580 ?startDate . }}
  OPTIONAL {{ ?item wdt:P582 ?endDate . }}
  OPTIONAL {{ ?item wdt:P571 ?startDate2 . }}
  OPTIONAL {{ ?item wdt:P17  ?country . }}
  OPTIONAL {{ ?item wdt:P361 ?partOf . }}
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

def transform_timeframe(row: dict) -> dict[str, Any] | None:
    item_uri = binding_val(row, "item")
    name = binding_val(row, "itemLabel")
    if not item_uri or not name or re.match(r'^Q\d+$', name):
        return None

    qid = qid_from_uri(item_uri)
    description = binding_val(row, "itemDescription") or ""
    type_qid = qid_from_uri(binding_val(row, "type"))
    type_label = binding_val(row, "typeLabel") or ""
    start_raw = binding_val(row, "startDate")
    end_raw = binding_val(row, "endDate")
    country_qid = qid_from_uri(binding_val(row, "country"))
    country_label = binding_val(row, "countryLabel") or ""
    part_of_label = binding_val(row, "partOfLabel") or ""
    image_url = binding_val(row, "image") or ""
    wiki_url = binding_val(row, "article") or ""
    sitelinks = int(binding_val(row, "sitelinks") or "0")

    # Filter non-timeframe entities
    desc_lower = description.lower()
    if any(kw in desc_lower for kw in NON_TIMEFRAME_KEYWORDS):
        return None
    if part_of_label and re.match(r'^Q\d+$', part_of_label):
        part_of_label = ""

    start_year = parse_year(start_raw)
    end_year = parse_year(end_raw)
    start_display = format_date_display(start_raw)
    end_display = format_date_display(end_raw)
    era, era_slug = year_to_era(start_year)
    div_code, div_heading = get_division(type_qid)
    country_name, region, continent = get_country_info(country_qid)
    if country_name == "Global" and country_label and not re.match(r'^Q\d+$', country_label):
        country_name = country_label

    # Refine parent divisions to sub-divisions
    div_code, div_heading = refine_division(div_code, div_heading, name, description, type_label, start_year)

    slug = make_slug(name)

    # Build summary
    summary = description.capitalize() if description else f"{name}, a historical {type_label}."
    if part_of_label:
        summary += f" Part of {part_of_label}."
    if country_name != "Global":
        summary += f" Associated with {country_name}."
    if start_display or end_display:
        date_range = ""
        if start_display and end_display:
            date_range = f" ({start_display} – {end_display})"
        elif start_display:
            date_range = f" (from {start_display})"
        elif end_display:
            date_range = f" (until {end_display})"
        summary += date_range

    sig_score = compute_significance(sitelinks, start_year)

    entity: dict[str, Any] = {
        "slug": slug,
        "name": name,
        "label": "Timeframe",
        "callNumber": f"{div_code}.{slug}",
        "subjectHeadings": [f"Timeframe -- {div_heading} -- {country_name} -- {era}"],
        "subjects": [s for s in [country_name, type_label, continent, div_heading] if s and s != "Global"],
        "summary": summary[:9900],
        "era": era,
        "eraSlug": era_slug,
        "region": region,
        "continent": continent,
        "status": "Published",
        "frameworks": ["PERIODIZATION"],
        "causes": [],
        "effects": [],
        "relationships": [],
        "places": [],
        "texts": [],
        "timeframeType": type_label,
        "divisionCode": div_code,
        "divisionHeading": div_heading,
        "historicalSignificance": {
            "score": sig_score,
            "label": significance_label(sig_score),
            "sitelinks": sitelinks,
        },
        "inAppwrite": False,
    }

    if start_display:
        entity["startDate"] = start_display
    if start_year is not None:
        entity["startYear"] = start_year
    if end_display:
        entity["endDate"] = end_display
    if end_year is not None:
        entity["endYear"] = end_year
    if country_name and country_name != "Global":
        entity["relationships"].append({
            "sourceSlug": slug, "sourceName": name,
            "verb": "OCCURS_IN",
            "targetSlug": f"country-{make_slug(country_name)}",
            "targetName": country_name,
            "context": f"{name} in {country_name}",
        })
        entity["places"].append({"name": country_name, "role": "Country"})
    if part_of_label:
        entity["relationships"].append({
            "sourceSlug": slug, "sourceName": name,
            "verb": "PART_OF",
            "targetSlug": make_slug(part_of_label),
            "targetName": part_of_label,
            "context": f"{name} is part of {part_of_label}",
        })
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
    parser = argparse.ArgumentParser(description="Fetch timeframes from Wikidata (v1.0)")
    parser.add_argument("--limit", type=int, default=5000)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    output_path = Path(args.output) if args.output else project_root / "data" / "wikidata_timeframes.json"

    total_qids = len(set(qid for qids, _ in TIMEFRAME_QUERIES.values() for qid in qids))

    print("=" * 70)
    print("  Wikidata Timeframes Fetch v1.0 -- Annals of the World")
    print("=" * 70)
    print(f"  Limit per batch:     {args.limit}")
    print(f"  Output:              {output_path}")
    print(f"  Query batches:       {len(TIMEFRAME_QUERIES)}")
    print(f"  Unique type QIDs:    {total_qids}")
    print(f"  Division coverage:   910-963 (all Class 9 sub-divisions)")
    print(f"  Adaptive fallback:   Yes")
    print(f"  Progressive save:    Every 5 batches")
    print()

    all_entities: list[dict[str, Any]] = []
    seen_slugs: set[str] = set()
    total_raw = 0
    batch_idx = 0

    for batch_name, (type_qids, min_sl) in TIMEFRAME_QUERIES.items():
        batch_idx += 1
        print(f"[{batch_idx}/{len(TIMEFRAME_QUERIES)}] {batch_name}  "
              f"{len(type_qids)} type(s), sitelinks>{min_sl} ...")

        if args.dry_run:
            print(f"  (dry-run) skipped\n")
            continue

        rows = fetch_adaptive(type_qids, args.limit, min_sl)
        total_raw += len(rows)
        print(f"  Got {len(rows)} raw results")

        batch_count = 0
        for row in rows:
            entity = transform_timeframe(row)
            if not entity or entity["slug"] in seen_slugs:
                continue
            seen_slugs.add(entity["slug"])
            all_entities.append(entity)
            batch_count += 1

        print(f"  -> {batch_count} unique (total: {len(all_entities)})")

        if batch_idx % 5 == 0:
            save_progress(all_entities, output_path, total_raw)

        time.sleep(2)

    if args.dry_run:
        print("\nDry run complete.")
        print(f"  Would query {len(TIMEFRAME_QUERIES)} batches with {total_qids} unique QIDs")
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
            "label": "Timeframe",
            "classCode": 9,
            "classHeading": "Timeframes",
            "type_qids_queried": total_qids,
            "batches_queried": len(TIMEFRAME_QUERIES),
            "division_counts": dict(sorted(div_counts.items())),
            "era_counts": dict(sorted(era_counts.items())),
            "significance_distribution": dict(sorted(sig_dist.items())),
            "continent_counts": dict(sorted(continent_counts.items())),
            "note": "Comprehensive Wikidata timeframes fetch v1.0 covering all Class 9 divisions (910-963).",
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
        print(f"    {i:2d}. [{sig['score']:2d} {sig['label']:>8s}] {e['name']} ({e['era']})")


if __name__ == "__main__":
    main()
