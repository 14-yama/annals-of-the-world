#!/usr/bin/env python3
"""
fetch_wikidata_all_people.py

Comprehensive Wikidata fetch — queries EVERY Class 2 Person division with
exhaustive occupation QIDs, lower sitelinks threshold, high limits, and
pagination. Then compares against the Appwrite backend and flags new people.

Output: data/wikidata_people.json  (overwrites)

Usage:
    python3 scripts/fetch_wikidata_all_people.py
    python3 scripts/fetch_wikidata_all_people.py --min-sitelinks 10
    python3 scripts/fetch_wikidata_all_people.py --skip-appwrite
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any

import requests

# ── Constants ──
SPARQL_ENDPOINT = "https://query.wikidata.org/sparql"
USER_AGENT = "AnnalsOfTheWorld/2.0 (https://github.com/annals-of-the-world; contact@annals.dev)"

APPWRITE_ENDPOINT = os.getenv("VITE_APPWRITE_ENDPOINT", "https://fra.cloud.appwrite.io/v1")
APPWRITE_PROJECT  = os.getenv("VITE_APPWRITE_PROJECT_ID", "69cc45e3000d587ea5e6")
APPWRITE_DB       = os.getenv("VITE_APPWRITE_DATABASE_ID", "annals_db")
APPWRITE_KEY      = os.getenv("APPWRITE_API_KEY", "")

# ── Comprehensive occupation → division mapping ──
# Each entry: (division_code, division_heading, [list of Wikidata occupation QIDs])
DIVISION_OCCUPATIONS: list[tuple[str, str, list[str]]] = [
    # 201 Educators & Academics
    ("201", "Educators & Academics", [
        "Q1622272",   # university teacher
        "Q37226",     # teacher
        "Q121594",    # professor
        "Q1231865",   # pedagogist
    ]),
    # 202 Merchants & Economists
    ("202", "Merchants & Economists", [
        "Q188094",    # economist
        "Q131524",    # entrepreneur
        "Q215536",    # merchant
        "Q43845",     # businessperson
        "Q806798",    # banker
    ]),
    # 203 Athletes & Competitors
    ("203", "Athletes & Competitors", [
        "Q2066131",   # athlete
        "Q937857",    # association football player
        "Q10843263",  # professional boxer
        "Q14089670",  # rugby player
        "Q19204627",  # American football player
        "Q3665646",   # basketball player
        "Q10871364",  # baseball player
        "Q13381376",  # track and field athlete
        "Q15117302",  # cricket player
        "Q10833314",  # tennis player
        "Q18515558",  # ice hockey player
        "Q11774891",  # chess player
        "Q11338576",  # Olympic athlete
    ]),
    # 204 Architects & Engineers
    ("204", "Architects & Engineers", [
        "Q81096",     # engineer
        "Q42973",     # architect
        "Q13582652",  # civil engineer
        "Q4773904",   # structural engineer
        "Q1150070",   # electrical engineer
        "Q15995642",  # mechanical engineer
    ]),
    # 205 Journalists & Chroniclers
    ("205", "Journalists & Chroniclers", [
        "Q1930187",   # journalist
        "Q201788",    # historian
        "Q10873124",  # chronicler
        "Q4263842",   # columnist
        "Q1086863",   # news presenter
        "Q947873",    # television presenter
    ]),
    # 210 Philosophers & Thinkers
    ("210", "Philosophers & Thinkers", [
        "Q4964182",   # philosopher
    ]),
    # 211 Logicians & Mathematicians
    ("211", "Logicians & Mathematicians", [
        "Q170790",    # mathematician
        "Q2374149",   # logician
        "Q2487799",   # statistician
    ]),
    # 212 Ethicists & Moralists
    ("212", "Ethicists & Moralists", [
        "Q15895020",  # ethicist
    ]),
    # 220 Political Leaders
    ("220", "Political Leaders", [
        "Q82955",     # politician
        "Q372436",    # statesman
        "Q193391",    # diplomat
    ]),
    # 221 Monarchs & Rulers
    ("221", "Monarchs & Rulers", [
        "Q116",       # monarch
        "Q12097",     # emperor
        "Q30461",     # president (historical heads of state)
        "Q7380726",   # ruler
        "Q19546",     # pope
        "Q43292",     # sultan
        "Q14565199",  # emir
        "Q22808320",  # sovereign
    ]),
    # 222 Heads of State & Government
    ("222", "Heads of State & Government", [
        "Q14915627",  # head of government
        "Q1553195",   # head of state
        "Q16517080",  # governor
        "Q484876",    # prime minister (as position held)
    ]),
    # 223 Tribal & Indigenous Leaders
    ("223", "Tribal & Indigenous Leaders", [
        "Q3894943",   # chief
    ]),
    # 230 Legal Figures
    ("230", "Legal Figures", [
        "Q40348",     # lawyer
        "Q16533",     # judge
    ]),
    # 231 Jurists & Legal Scholars
    ("231", "Jurists & Legal Scholars", [
        "Q185351",    # jurist
    ]),
    # 240 Scientists & Inventors
    ("240", "Scientists & Inventors", [
        "Q901",       # scientist
        "Q205375",    # inventor
        "Q169470",    # physicist
        "Q593644",    # chemist
        "Q520549",    # geologist
        "Q131512",    # geographer
    ]),
    # 241 Physicians & Medical Pioneers
    ("241", "Physicians & Medical Pioneers", [
        "Q39631",     # physician
        "Q774306",    # surgeon
        "Q2640827",   # pharmacist
        "Q15924224",  # psychiatrist
        "Q14467526",  # pathologist
        "Q212980",    # psychologist
    ]),
    # 242 Astronomers & Cosmologists
    ("242", "Astronomers & Cosmologists", [
        "Q11063",     # astronomer
        "Q16009966",  # astrophysicist
        "Q15975914",  # cosmologist
    ]),
    # 243 Naturalists & Biologists
    ("243", "Naturalists & Biologists", [
        "Q864503",    # biologist
        "Q18805",     # naturalist
        "Q420",       # botanist
        "Q350979",    # zoologist
        "Q736786",    # entomologist
        "Q18123885",  # ecologist
    ]),
    # 250 Religious Figures
    ("250", "Religious Figures", [
        "Q42603",     # priest
        "Q191808",    # bishop
        "Q955464",    # religious leader
        "Q250867",    # Catholic priest
        "Q211423",    # clergyperson
        "Q177826",    # imam
        "Q43275",     # rabbi
    ]),
    # 251 Prophets & Founders
    ("251", "Prophets & Founders", [
        "Q3502482",   # prophet
    ]),
    # 252 Theologians & Scholars
    ("252", "Theologians & Scholars", [
        "Q1234713",   # theologian
        "Q13418253",  # biblical scholar
    ]),
    # 253 Missionaries
    ("253", "Missionaries", [
        "Q219477",    # missionary
    ]),
    # 260 Artists & Writers
    ("260", "Artists & Writers", [
        "Q483501",    # artist
        "Q36180",     # writer
    ]),
    # 261 Authors & Novelists
    ("261", "Authors & Novelists", [
        "Q6625963",   # novelist
        "Q482980",    # author
        "Q4853732",   # screenwriter
    ]),
    # 262 Poets & Playwrights
    ("262", "Poets & Playwrights", [
        "Q49757",     # poet
        "Q214917",    # playwright
        "Q15077007",  # lyricist
    ]),
    # 263 Composers & Musicians
    ("263", "Composers & Musicians", [
        "Q36834",     # composer
        "Q639669",    # musician
        "Q177220",    # singer
        "Q855091",    # guitarist
        "Q386854",    # pianist
    ]),
    # 264 Painters & Sculptors
    ("264", "Painters & Sculptors", [
        "Q1028181",   # painter
        "Q1281618",   # sculptor
        "Q644687",    # illustrator
        "Q33231",     # photographer
    ]),
    # 265 Architects & Designers
    ("265", "Architects & Designers", [
        "Q5322166",   # industrial designer
        "Q1792450",   # fashion designer
        "Q9017214",   # graphic designer
    ]),
    # 270 Activists & Reformers
    ("270", "Activists & Reformers", [
        "Q15253558",  # activist
        "Q13235160",  # reformer
        "Q14886050",  # human rights activist
    ]),
    # 271 Abolitionists
    ("271", "Abolitionists", [
        "Q16513225",  # abolitionist
    ]),
    # 272 Suffragists & Feminists
    ("272", "Suffragists & Feminists", [
        "Q18576582",  # suffragist
        "Q2113543",   # feminist
    ]),
    # 273 Labor Organizers
    ("273", "Labor Organizers", [
        "Q15627169",  # trade unionist
    ]),
    # 280 Military Leaders & Commanders
    ("280", "Military Leaders & Commanders", [
        "Q189290",    # military officer
        "Q4991371",   # military commander
        "Q47064",     # military leader
    ]),
    # 281 Naval Commanders
    ("281", "Naval Commanders", [
        "Q10669499",  # naval officer
        "Q2148765",   # admiral
    ]),
    # 282 Intelligence & Espionage
    ("282", "Intelligence & Espionage", [
        "Q9352089",   # spy
        "Q15978655",  # intelligence officer
    ]),
    # 283 Modern Military Commanders
    ("283", "Modern Military Commanders", [
        "Q10669499",  # reuse naval + filter by era later
    ]),
    # 290 Explorers & Navigators
    ("290", "Explorers & Navigators", [
        "Q11900058",  # explorer
        "Q2125610",   # navigator
    ]),
    # 291 Space Explorers
    ("291", "Space Explorers", [
        "Q11631",     # astronaut
        "Q13582652",  # cosmonaut
    ]),
    # 292 Deep-Sea Explorers
    ("292", "Deep-Sea Explorers", [
        "Q5765944",   # oceanographer
    ]),
    # 293 Cartographers
    ("293", "Cartographers", [
        "Q1734662",   # cartographer
    ]),
]

# ── Country / Region / Continent mapping ──
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
    "Q230":   ("Georgia", "West Asia", "Asia"),
    "Q399":   ("Armenia", "West Asia", "Asia"),
    "Q227":   ("Azerbaijan", "West Asia", "Asia"),
    "Q232":   ("Kazakhstan", "Central Asia", "Asia"),
    "Q813":   ("Kyrgyzstan", "Central Asia", "Asia"),
    "Q863":   ("Tajikistan", "Central Asia", "Asia"),
    "Q265":   ("Uzbekistan", "Central Asia", "Asia"),
    "Q924":   ("Tanzania", "East Africa", "Africa"),
    "Q1009":  ("Cameroon", "Central Africa", "Africa"),
    "Q1000":  ("Gabon", "Central Africa", "Africa"),
    "Q958":   ("Eritrea", "East Africa", "Africa"),
    "Q1049":  ("Sudan", "East Africa", "Africa"),
    "Q1036":  ("Uganda", "East Africa", "Africa"),
    "Q951":   ("Malawi", "East Africa", "Africa"),
    "Q948":   ("Tunisia", "North Africa", "Africa"),
    "Q977":   ("Djibouti", "East Africa", "Africa"),
    "Q1045":  ("Somalia", "East Africa", "Africa"),
    "Q986":   ("Libya", "North Africa", "Africa"),
    "Q1020":  ("Senegal", "West Africa", "Africa"),
    "Q733":   ("Paraguay", "South America", "Americas"),
    "Q750":   ("Bolivia", "South America", "Americas"),
    "Q717":   ("Venezuela", "South America", "Americas"),
    "Q800":   ("Costa Rica", "Central America", "Americas"),
    "Q774":   ("Guatemala", "Central America", "Americas"),
    "Q783":   ("Honduras", "Central America", "Americas"),
    "Q792":   ("El Salvador", "Central America", "Americas"),
    "Q811":   ("Nicaragua", "Central America", "Americas"),
    "Q804":   ("Panama", "Central America", "Americas"),
    "Q241":   ("Cuba", "Caribbean", "Americas"),
    "Q790":   ("Haiti", "Caribbean", "Americas"),
    "Q786":   ("Dominican Republic", "Caribbean", "Americas"),
    "Q734":   ("Guyana", "South America", "Americas"),
    "Q730":   ("Suriname", "South America", "Americas"),
    "Q736":   ("Ecuador", "South America", "Americas"),
    "Q419":   ("Peru", "South America", "Americas"),
    "Q77":    ("Uruguay", "South America", "Americas"),
    "Q691":   ("Papua New Guinea", "Oceania", "Oceania"),
    "Q712":   ("Fiji", "Oceania", "Oceania"),
}

DEFAULT_GEO = ("Global", "Global", "Global")


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


def parse_year(date_str: str | None) -> int | None:
    if not date_str:
        return None
    m = re.match(r'^([+-]?\d+)', date_str)
    if m:
        return int(m.group(1))
    return None


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


def binding_val(row: dict, key: str) -> str | None:
    b = row.get(key)
    if b and "value" in b:
        return b["value"]
    return None


def qid_from_uri(uri: str | None) -> str | None:
    if not uri:
        return None
    m = re.search(r'(Q\d+)$', uri)
    return m.group(1) if m else None


# ── SPARQL ──

def build_query(occupation_qid: str, limit: int, offset: int, min_sitelinks: int) -> str:
    """Minimal SPARQL for speed — one occupation at a time."""
    return f"""
SELECT DISTINCT ?person ?personLabel ?personDescription
       ?birthDate ?deathDate
       ?birthPlaceLabel
       ?countryOfCitizenship
       ?article
WHERE {{
  VALUES ?occupation {{ wd:{occupation_qid} }}
  ?person wdt:P106 ?occupation .
  ?person wdt:P31 wd:Q5 .
  ?person wikibase:sitelinks ?sl .
  FILTER(?sl > {min_sitelinks})

  OPTIONAL {{ ?person wdt:P569 ?birthDate . }}
  OPTIONAL {{ ?person wdt:P570 ?deathDate . }}
  OPTIONAL {{ ?person wdt:P19 ?birthPlace . }}
  OPTIONAL {{ ?person wdt:P27 ?countryOfCitizenship . }}
  OPTIONAL {{
    ?article schema:about ?person ;
             schema:isPartOf <https://en.wikipedia.org/> .
  }}

  SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en" . }}
}}
ORDER BY DESC(?sl)
LIMIT {limit}
OFFSET {offset}
"""


def fetch_sparql(query: str, retries: int = 4) -> list[dict]:
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
                wait = min(120, 20 * (attempt + 1))
                print(f"    Rate limited, waiting {wait}s...")
                time.sleep(wait)
                continue
            if resp.status_code in (502, 504):
                wait = 25 * (attempt + 1)
                print(f"    Server {resp.status_code} (attempt {attempt + 1}/{retries}), waiting {wait}s...")
                time.sleep(wait)
                continue
            resp.raise_for_status()
            return resp.json()["results"]["bindings"]
        except requests.exceptions.RequestException as e:
            print(f"    Error (attempt {attempt + 1}/{retries}): {e}")
            if attempt < retries - 1:
                time.sleep(15 * (attempt + 1))
    return []


def transform_person(row: dict, div_code: str, div_heading: str) -> dict | None:
    person_uri = binding_val(row, "person")
    name = binding_val(row, "personLabel")
    if not person_uri or not name:
        return None
    if re.match(r'^Q\d+$', name):
        return None

    qid = qid_from_uri(person_uri)
    description = binding_val(row, "personDescription") or ""
    birth_date_raw = binding_val(row, "birthDate")
    death_date_raw = binding_val(row, "deathDate")
    birth_place = binding_val(row, "birthPlaceLabel") or ""
    country_qid = qid_from_uri(binding_val(row, "countryOfCitizenship"))
    wiki_url = binding_val(row, "article") or ""

    birth_year = parse_year(birth_date_raw)
    death_year = parse_year(death_date_raw)
    born_display = format_date_display(birth_date_raw)
    died_display = format_date_display(death_date_raw)
    if birth_place and born_display:
        born_display = f"{born_display}, {birth_place}"

    era, era_slug = year_to_era(birth_year)
    country_name, region, continent = get_country_info(country_qid)
    slug = make_slug(name)

    summary = description.capitalize() if description else f"{name}, {div_heading.lower()}."
    if birth_place:
        summary += f" Born in {birth_place}."
    if birth_year and death_year:
        if birth_year < 0:
            summary += f" ({abs(birth_year)} BCE – {abs(death_year)} {'BCE' if death_year < 0 else 'CE'})."
        else:
            summary += f" ({birth_year} – {death_year})."
    elif birth_year:
        if birth_year < 0:
            summary += f" (b. {abs(birth_year)} BCE)."
        else:
            summary += f" (b. {birth_year})."

    entity: dict[str, Any] = {
        "slug": slug,
        "name": name,
        "label": "Person",
        "callNumber": f"{div_code}.{slug}",
        "subjectHeadings": [f"People — {div_heading} — {country_name} — {era}"],
        "subjects": [s for s in [country_name, div_heading, continent] if s and s != "Global"],
        "summary": summary[:9900],
        "era": era,
        "eraSlug": era_slug,
        "region": region,
        "continent": continent,
        "status": "Published",
        "frameworks": ["CAUSE_AND_EFFECT"],
        "causes": [],
        "effects": [],
        "relationships": [
            {
                "sourceSlug": slug,
                "sourceName": name,
                "verb": "OCCURS_IN",
                "targetSlug": f"country-{make_slug(country_name)}" if country_name != "Global" else "",
                "targetName": country_name,
                "context": f"{name} associated with {country_name}",
            }
        ] if country_name != "Global" else [],
        "places": [],
        "texts": [],
        "inAppwrite": False,  # Will be updated after Appwrite comparison
    }

    if born_display:
        entity["born"] = born_display
    if died_display:
        entity["died"] = died_display
    if birth_place:
        entity["places"].append({"name": birth_place, "role": "Birth place"})
    if country_name and country_name != "Global":
        entity["places"].append({"name": country_name, "role": "Country"})
    if qid:
        entity["wikidataQid"] = qid
    if wiki_url:
        entity["wikipediaUrl"] = wiki_url

    return entity


# ── Appwrite integration ──

def fetch_appwrite_person_slugs() -> set[str]:
    """Fetch all Person entity slugs from Appwrite backend."""
    if not APPWRITE_KEY:
        print("  No APPWRITE_API_KEY — skipping Appwrite comparison")
        return set()

    slugs: set[str] = set()
    url = f"{APPWRITE_ENDPOINT}/databases/{APPWRITE_DB}/collections/entities/documents"
    headers = {
        "X-Appwrite-Project": APPWRITE_PROJECT,
        "X-Appwrite-Key": APPWRITE_KEY,
        "Content-Type": "application/json",
    }

    # Paginate through all Person entities
    cursor = None
    page = 0
    while True:
        params: list[str] = [
            'queries[]=' + json.dumps({"method": "equal", "attribute": "label", "values": ["Person"]}),
            'queries[]=' + json.dumps({"method": "limit", "values": [100]}),
            'queries[]=' + json.dumps({"method": "select", "values": ["slug"]}),
        ]
        if cursor:
            params.append(
                'queries[]=' + json.dumps({"method": "cursorAfter", "values": [cursor]})
            )

        try:
            resp = requests.get(
                url + "?" + "&".join(params),
                headers=headers,
                timeout=30,
            )
            resp.raise_for_status()
            data = resp.json()
            docs = data.get("documents", [])
            if not docs:
                break
            for doc in docs:
                s = doc.get("slug")
                if s:
                    slugs.add(s)
            cursor = docs[-1]["$id"]
            page += 1
            if page % 10 == 0:
                print(f"    Fetched {len(slugs)} Appwrite slugs so far...")
        except requests.exceptions.RequestException as e:
            print(f"    Appwrite error (page {page}): {e}")
            break

    return slugs


def fetch_all_appwrite_slugs() -> set[str]:
    """Fetch ALL entity slugs from Appwrite (not just Person)."""
    if not APPWRITE_KEY:
        print("  No APPWRITE_API_KEY — skipping Appwrite comparison")
        return set()

    slugs: set[str] = set()
    url = f"{APPWRITE_ENDPOINT}/databases/{APPWRITE_DB}/collections/entities/documents"
    headers = {
        "X-Appwrite-Project": APPWRITE_PROJECT,
        "X-Appwrite-Key": APPWRITE_KEY,
        "Content-Type": "application/json",
    }

    cursor = None
    page = 0
    while True:
        params: list[str] = [
            'queries[]=' + json.dumps({"method": "limit", "values": [100]}),
            'queries[]=' + json.dumps({"method": "select", "values": ["slug", "label"]}),
        ]
        if cursor:
            params.append(
                'queries[]=' + json.dumps({"method": "cursorAfter", "values": [cursor]})
            )

        try:
            resp = requests.get(
                url + "?" + "&".join(params),
                headers=headers,
                timeout=30,
            )
            resp.raise_for_status()
            data = resp.json()
            docs = data.get("documents", [])
            if not docs:
                break
            for doc in docs:
                s = doc.get("slug")
                if s:
                    slugs.add(s)
            cursor = docs[-1]["$id"]
            page += 1
            if page % 50 == 0:
                print(f"    Fetched {len(slugs)} Appwrite slugs...")
        except requests.exceptions.RequestException as e:
            print(f"    Appwrite error (page {page}): {e}")
            break

    return slugs


# ── Main ──

def main():
    parser = argparse.ArgumentParser(description="Comprehensive Wikidata people fetch")
    parser.add_argument("--limit", type=int, default=5000,
                        help="Max results per occupation query page (default: 5000)")
    parser.add_argument("--min-sitelinks", type=int, default=5,
                        help="Min Wikipedia sitelinks for notability (default: 5)")
    parser.add_argument("--skip-appwrite", action="store_true",
                        help="Skip Appwrite comparison")
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    output_path = Path(args.output) if args.output else project_root / "data" / "wikidata_people.json"

    # Count total occupation queries
    total_qids = sum(len(occ[2]) for occ in DIVISION_OCCUPATIONS)

    print("=" * 70)
    print("Wikidata Comprehensive People Fetch — Annals of the World")
    print("=" * 70)
    print(f"  Divisions: {len(DIVISION_OCCUPATIONS)}")
    print(f"  Occupation QIDs: {total_qids}")
    print(f"  Limit per page: {args.limit}")
    print(f"  Min sitelinks: {args.min_sitelinks}")
    print(f"  Output: {output_path}")
    print()

    all_entities: list[dict] = []
    seen_slugs: set[str] = set()
    seen_qids: set[str] = set()
    total_raw = 0
    division_stats: dict[str, dict[str, int]] = {}
    qid_count = 0

    for div_code, div_heading, occupation_qids in DIVISION_OCCUPATIONS:
        div_total = 0
        print(f"\n[{div_code}] {div_heading}")
        print(f"  Occupation QIDs: {len(occupation_qids)}")

        for occ_qid in occupation_qids:
            qid_count += 1
            offset = 0
            page = 0
            occ_total = 0

            while True:
                query = build_query(occ_qid, args.limit, offset, args.min_sitelinks)
                print(f"  wd:{occ_qid} page {page} (offset {offset})...", end=" ", flush=True)

                rows = fetch_sparql(query)
                raw_count = len(rows)
                total_raw += raw_count

                batch_count = 0
                for row in rows:
                    entity = transform_person(row, div_code, div_heading)
                    if not entity:
                        continue
                    # Dedup by slug AND Wikidata QID
                    wqid = entity.get("wikidataQid", "")
                    if entity["slug"] in seen_slugs:
                        continue
                    if wqid and wqid in seen_qids:
                        continue
                    seen_slugs.add(entity["slug"])
                    if wqid:
                        seen_qids.add(wqid)
                    all_entities.append(entity)
                    batch_count += 1

                print(f"{raw_count} raw → {batch_count} new")
                occ_total += batch_count
                div_total += batch_count

                # Paginate if we got a full page
                if raw_count >= args.limit:
                    offset += args.limit
                    page += 1
                    time.sleep(2)
                else:
                    break

            # Polite delay between occupation queries
            time.sleep(2)

        division_stats[div_code] = {
            "heading": div_heading,
            "count": div_total,
        }
        print(f"  ── Division {div_code} total: {div_total}")

    # Sort by era then name
    era_order = {"Prehistoric": 0, "Classical": 1, "Medieval": 2, "Early Modern": 3, "Modern": 4, "Contemporary": 5}
    all_entities.sort(key=lambda e: (era_order.get(e["era"], 9), e["name"]))

    # ── Appwrite comparison ──
    appwrite_slugs: set[str] = set()
    appwrite_person_count = 0
    appwrite_total_count = 0

    if not args.skip_appwrite:
        print("\n" + "=" * 70)
        print("Comparing with Appwrite backend...")
        print("=" * 70)

        appwrite_slugs = fetch_all_appwrite_slugs()
        appwrite_total_count = len(appwrite_slugs)
        print(f"  Total Appwrite entities: {appwrite_total_count}")

        # Count Person entities in Appwrite
        appwrite_person_slugs = fetch_appwrite_person_slugs()
        appwrite_person_count = len(appwrite_person_slugs)
        print(f"  Appwrite Person entities: {appwrite_person_count}")

        # Flag each Wikidata entity
        in_count = 0
        not_in_count = 0
        for entity in all_entities:
            if entity["slug"] in appwrite_slugs:
                entity["inAppwrite"] = True
                in_count += 1
            else:
                entity["inAppwrite"] = False
                not_in_count += 1

        print(f"  Wikidata people already in Appwrite: {in_count}")
        print(f"  Wikidata people NOT in Appwrite: {not_in_count}")

    # ── Build stats ──
    div_counts: dict[str, int] = {}
    era_counts: dict[str, int] = {}
    continent_counts: dict[str, int] = {}
    in_appwrite_count = sum(1 for e in all_entities if e.get("inAppwrite"))
    not_in_appwrite_count = sum(1 for e in all_entities if not e.get("inAppwrite"))

    for e in all_entities:
        div = e["callNumber"][:3]
        div_counts[div] = div_counts.get(div, 0) + 1
        era_counts[e["era"]] = era_counts.get(e["era"], 0) + 1
        continent_counts[e["continent"]] = continent_counts.get(e["continent"], 0) + 1

    # Write JSON
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_data = {
        "_meta": {
            "source": "Wikidata SPARQL (query.wikidata.org)",
            "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "version": "2.0",
            "min_sitelinks": args.min_sitelinks,
            "total_raw_results": total_raw,
            "total_unique_entities": len(all_entities),
            "occupation_qids_queried": total_qids,
            "divisions_queried": len(DIVISION_OCCUPATIONS),
            "division_counts": dict(sorted(div_counts.items())),
            "era_counts": dict(sorted(era_counts.items())),
            "continent_counts": dict(sorted(continent_counts.items())),
            "appwrite_comparison": {
                "appwrite_total_entities": appwrite_total_count,
                "appwrite_person_entities": appwrite_person_count,
                "wikidata_in_appwrite": in_appwrite_count,
                "wikidata_not_in_appwrite": not_in_appwrite_count,
                "wikidata_coverage_pct": round(
                    in_appwrite_count / len(all_entities) * 100, 1
                ) if all_entities else 0,
            },
            "note": (
                "Comprehensive Wikidata people fetch covering all 38 Class 2 Person divisions. "
                "Each entity has inAppwrite flag indicating presence in the Appwrite backend. "
                "Aligned with Annals call number system (callNumbers.ts)."
            ),
        },
        "entities": all_entities,
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    # ── Summary ──
    print("\n" + "=" * 70)
    print("FETCH COMPLETE")
    print("=" * 70)
    print(f"  Total raw SPARQL results:    {total_raw:,}")
    print(f"  Total unique entities:       {len(all_entities):,}")
    print(f"  Occupation QIDs queried:     {total_qids}")
    print(f"  Divisions with data:         {len(div_counts)}")
    print(f"  Output:                      {output_path}")
    print()
    print("  ── By Division ──")
    for div in sorted(div_counts):
        heading = division_stats.get(div, {}).get("heading", "")
        print(f"    {div} {heading:.<40s} {div_counts[div]:>5,}")
    print()
    print("  ── By Era ──")
    for era in ["Prehistoric", "Classical", "Medieval", "Early Modern", "Modern", "Contemporary"]:
        print(f"    {era:.<30s} {era_counts.get(era, 0):>6,}")
    print()
    print("  ── By Continent ──")
    for cont, count in sorted(continent_counts.items(), key=lambda x: -x[1]):
        print(f"    {cont:.<30s} {count:>6,}")
    print()
    if not args.skip_appwrite:
        print("  ── Appwrite Comparison ──")
        print(f"    Appwrite total entities:   {appwrite_total_count:,}")
        print(f"    Appwrite Person entities:  {appwrite_person_count:,}")
        print(f"    Wikidata → in Appwrite:    {in_appwrite_count:,}")
        print(f"    Wikidata → NOT in Appwrite: {not_in_appwrite_count:,}")
    print()


if __name__ == "__main__":
    main()
