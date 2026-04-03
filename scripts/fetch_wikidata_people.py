#!/usr/bin/env python3
"""
fetch_wikidata_people.py

Fetches notable historical figures from the Wikidata SPARQL endpoint and maps
them into the Annals of the World entity schema (Person label, Class 2 divisions).

Output: data/wikidata_people.json  —  ready for catalog integration.

Usage:
    python3 scripts/fetch_wikidata_people.py
    python3 scripts/fetch_wikidata_people.py --limit 500
    python3 scripts/fetch_wikidata_people.py --dry-run
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

# ── Wikidata SPARQL endpoint ──
SPARQL_ENDPOINT = "https://query.wikidata.org/sparql"
USER_AGENT = "AnnalsOfTheWorld/1.0 (https://github.com/annals-of-the-world; contact@annals.dev)"

# ── Occupation → Division mapping ──
# Maps Wikidata occupation QIDs to our call number divisions
OCCUPATION_DIVISION_MAP: dict[str, tuple[str, str]] = {
    # 210 Philosophers & Thinkers
    "Q4964182":  ("210", "Philosophers & Thinkers"),          # philosopher
    "Q36180":    ("210", "Philosophers & Thinkers"),          # writer (general → philosopher bucket for thinkers)

    # 211 Logicians & Mathematicians
    "Q170790":   ("211", "Logicians & Mathematicians"),       # mathematician
    "Q2374149":  ("211", "Logicians & Mathematicians"),       # logician

    # 220 Political Leaders
    "Q82955":    ("220", "Political Leaders"),                # politician
    "Q372436":   ("220", "Political Leaders"),                # statesman

    # 221 Monarchs & Rulers
    "Q116":      ("221", "Monarchs & Rulers"),                # monarch
    "Q22808320": ("221", "Monarchs & Rulers"),               # sovereign
    "Q12097":    ("221", "Monarchs & Rulers"),                # emperor
    "Q30461":    ("221", "Monarchs & Rulers"),                # president (historical heads of state)

    # 222 Heads of State & Government
    "Q14915627": ("222", "Heads of State & Government"),      # head of government
    "Q1553195":  ("222", "Heads of State & Government"),      # head of state

    # 230 Legal Figures
    "Q185351":   ("230", "Legal Figures"),                    # jurist
    "Q16533":    ("230", "Legal Figures"),                    # judge
    "Q40348":    ("230", "Legal Figures"),                    # lawyer

    # 240 Scientists & Inventors
    "Q901":      ("240", "Scientists & Inventors"),           # scientist
    "Q205375":   ("240", "Scientists & Inventors"),           # inventor
    "Q593644":   ("240", "Scientists & Inventors"),           # chemist
    "Q169470":   ("240", "Scientists & Inventors"),           # physicist
    "Q11063":    ("240", "Scientists & Inventors"),           # astronomer
    "Q81096":    ("240", "Scientists & Inventors"),           # engineer

    # 241 Physicians & Medical Pioneers
    "Q39631":    ("241", "Physicians & Medical Pioneers"),    # physician
    "Q774306":   ("241", "Physicians & Medical Pioneers"),    # surgeon

    # 242 Astronomers & Cosmologists
    "Q11063":    ("242", "Astronomers & Cosmologists"),       # astronomer (override)

    # 243 Naturalists & Biologists
    "Q864503":   ("243", "Naturalists & Biologists"),         # biologist
    "Q18805":    ("243", "Naturalists & Biologists"),         # naturalist

    # 250 Religious Figures
    "Q42603":    ("250", "Religious Figures"),                # priest
    "Q191808":   ("250", "Religious Figures"),                # bishop
    "Q47064":    ("250", "Religious Figures"),                # pope (also religious figure)
    "Q955464":   ("250", "Religious Figures"),                # religious figure

    # 251 Prophets & Founders
    # (manually curated, not fetched by occupation)

    # 252 Theologians & Scholars
    "Q1234713":  ("252", "Theologians & Scholars"),           # theologian

    # 260 Artists & Writers
    "Q483501":   ("260", "Artists & Writers"),                # artist

    # 261 Authors & Novelists
    "Q6625963":  ("261", "Authors & Novelists"),              # novelist
    "Q482980":   ("261", "Authors & Novelists"),              # author

    # 262 Poets & Playwrights
    "Q49757":    ("262", "Poets & Playwrights"),              # poet
    "Q214917":   ("262", "Poets & Playwrights"),              # playwright

    # 263 Composers & Musicians
    "Q36834":    ("263", "Composers & Musicians"),            # composer
    "Q639669":   ("263", "Composers & Musicians"),            # musician

    # 264 Painters & Sculptors
    "Q1028181":  ("264", "Painters & Sculptors"),             # painter
    "Q1281618":  ("264", "Painters & Sculptors"),             # sculptor

    # 265 Architects & Designers
    "Q42973":    ("265", "Architects & Designers"),           # architect

    # 270 Activists & Reformers
    "Q15253558": ("270", "Activists & Reformers"),            # activist
    "Q13235160": ("270", "Activists & Reformers"),            # reformer

    # 280 Military Leaders & Commanders
    "Q47064":    ("280", "Military Leaders & Commanders"),    # military leader (general)
    "Q189290":   ("280", "Military Leaders & Commanders"),    # military officer
    "Q4991371":  ("280", "Military Leaders & Commanders"),    # military commander

    # 290 Explorers & Navigators
    "Q11900058": ("290", "Explorers & Navigators"),           # explorer
    "Q2125610":  ("290", "Explorers & Navigators"),           # navigator

    # 201 Educators & Academics
    "Q1622272":  ("201", "Educators & Academics"),            # university teacher

    # 202 Merchants & Economists
    "Q188094":   ("202", "Merchants & Economists"),           # economist

    # 204 Architects & Engineers
    "Q81096":    ("204", "Architects & Engineers"),            # engineer

    # 203 Athletes & Sports Figures
    "Q2066131":  ("203", "Athletes & Sports Figures"),        # athlete

    # 205 Journalists & Chroniclers
    "Q1930187":  ("205", "Journalists & Chroniclers"),        # journalist
    "Q10873124": ("205", "Journalists & Chroniclers"),        # chronicler
    "Q201788":   ("205", "Journalists & Chroniclers"),        # historian
}

# Reverse: preferred QID → division (first occurrence wins)
QID_TO_DIVISION: dict[str, tuple[str, str]] = {}
for qid, div_info in OCCUPATION_DIVISION_MAP.items():
    if qid not in QID_TO_DIVISION:
        QID_TO_DIVISION[qid] = div_info

# ── Country / Region / Continent mapping from Wikidata country QIDs ──
# Maps commonly occurring country QIDs to (region, continent) tuples.
COUNTRY_INFO: dict[str, tuple[str, str, str]] = {
    # (country_name, region, continent)
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
}

# Fallback for unknown countries
DEFAULT_GEO = ("Global", "Global", "Global")


def get_country_info(country_qid: str | None) -> tuple[str, str, str]:
    """Return (country_name, region, continent) for a Wikidata Q-ID."""
    if not country_qid:
        return DEFAULT_GEO
    return COUNTRY_INFO.get(country_qid, DEFAULT_GEO)


# ── Era mapping from year ──
def year_to_era(year: int | None) -> tuple[str, str]:
    """Map a birth year to (era, eraSlug)."""
    if year is None:
        return ("Classical", "classical")  # safe default for historical figures
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
    """Parse Wikidata date string like '+1642-12-25T00:00:00Z' or '-0469-01-01T00:00:00Z'."""
    if not date_str:
        return None
    m = re.match(r'^([+-]?\d+)', date_str)
    if m:
        return int(m.group(1))
    return None


def format_date_display(date_str: str | None) -> str:
    """Format Wikidata date for display: '1642-12-25' or '469 BCE'."""
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
        # Likely just the year
        return f"{year} CE" if year < 1000 else str(year)
    return f"{year}-{month}-{day}"


def make_slug(name: str) -> str:
    """Convert a name to a slug."""
    slug = name.lower().strip()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')[:80]


# ── SPARQL queries ──
# We query for notable people by occupation category, fetching birth/death dates,
# description, country of citizenship, and occupation.
# Batched by occupation to stay within Wikidata query limits.

OCCUPATION_QUERIES: dict[str, list[str]] = {
    # Division code → list of occupation QIDs
    "220-222": ["Q82955", "Q372436", "Q116", "Q12097"],        # Political leaders, monarchs
    "210":     ["Q4964182"],                                      # Philosophers
    "240-243": ["Q901", "Q205375", "Q169470", "Q593644", "Q864503", "Q11063", "Q81096"],  # Scientists
    "241":     ["Q39631", "Q774306"],                             # Physicians
    "250-253": ["Q42603", "Q191808", "Q1234713"],                 # Religious figures
    "260-265": ["Q483501", "Q6625963", "Q49757", "Q214917", "Q36834", "Q1028181", "Q42973"],  # Artists, writers
    "270":     ["Q15253558"],                                      # Activists
    "280":     ["Q189290", "Q4991371"],                            # Military leaders
    "290":     ["Q11900058", "Q2125610"],                          # Explorers
    "230":     ["Q185351", "Q40348"],                              # Legal figures
    "202":     ["Q188094"],                                        # Economists
    "205":     ["Q201788", "Q1930187"],                            # Historians, journalists
    "211":     ["Q170790"],                                        # Mathematicians
}


def build_sparql_query(occupation_qids: list[str], limit: int = 300) -> str:
    """Build SPARQL query for a batch of occupation Q-IDs."""
    values = " ".join(f"wd:{qid}" for qid in occupation_qids)
    return f"""
SELECT DISTINCT ?person ?personLabel ?personDescription
       ?birthDate ?deathDate
       ?birthPlaceLabel ?deathPlaceLabel
       ?countryOfCitizenship
       ?occupation ?occupationLabel
       ?image
       ?article
WHERE {{
  VALUES ?occupation {{ {values} }}
  ?person wdt:P106 ?occupation .
  ?person wdt:P31 wd:Q5 .          # Must be a human
  ?person wikibase:sitelinks ?sitelinks .
  FILTER(?sitelinks > 20)           # Notable (20+ Wikipedia articles)

  OPTIONAL {{ ?person wdt:P569 ?birthDate . }}
  OPTIONAL {{ ?person wdt:P570 ?deathDate . }}
  OPTIONAL {{ ?person wdt:P19 ?birthPlace . }}
  OPTIONAL {{ ?person wdt:P20 ?deathPlace . }}
  OPTIONAL {{ ?person wdt:P27 ?countryOfCitizenship . }}
  OPTIONAL {{ ?person wdt:P18 ?image . }}
  OPTIONAL {{
    ?article schema:about ?person ;
             schema:isPartOf <https://en.wikipedia.org/> .
  }}

  SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en" . }}
}}
ORDER BY DESC(?sitelinks)
LIMIT {limit}
"""


def fetch_sparql(query: str, retries: int = 3) -> list[dict[str, Any]]:
    """Execute a SPARQL query against Wikidata."""
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
                timeout=120,
            )
            if resp.status_code == 429:
                wait = min(60, 10 * (attempt + 1))
                print(f"  Rate limited, waiting {wait}s...")
                time.sleep(wait)
                continue
            resp.raise_for_status()
            return resp.json()["results"]["bindings"]
        except requests.exceptions.RequestException as e:
            print(f"  Request error (attempt {attempt + 1}): {e}")
            if attempt < retries - 1:
                time.sleep(5 * (attempt + 1))
    return []


def qid_from_uri(uri: str | None) -> str | None:
    """Extract Q-ID from a Wikidata URI."""
    if not uri:
        return None
    m = re.search(r'(Q\d+)$', uri)
    return m.group(1) if m else None


def get_division(occupation_qid: str | None) -> tuple[str, str]:
    """Map occupation QID to (division_code, division_heading)."""
    if occupation_qid and occupation_qid in QID_TO_DIVISION:
        return QID_TO_DIVISION[occupation_qid]
    return ("220", "Political Leaders")  # default fallback


def binding_val(row: dict, key: str) -> str | None:
    """Safely extract value from SPARQL binding."""
    b = row.get(key)
    if b and "value" in b:
        return b["value"]
    return None


def transform_person(row: dict) -> dict[str, Any] | None:
    """Transform a SPARQL result row into an Annals Entity dict."""
    person_uri = binding_val(row, "person")
    name = binding_val(row, "personLabel")
    if not person_uri or not name:
        return None

    # Skip entries where label is the QID (no English label)
    if re.match(r'^Q\d+$', name):
        return None

    qid = qid_from_uri(person_uri)
    description = binding_val(row, "personDescription") or ""
    birth_date_raw = binding_val(row, "birthDate")
    death_date_raw = binding_val(row, "deathDate")
    birth_place = binding_val(row, "birthPlaceLabel") or ""
    death_place = binding_val(row, "deathPlaceLabel") or ""
    country_qid = qid_from_uri(binding_val(row, "countryOfCitizenship"))
    occupation_qid = qid_from_uri(binding_val(row, "occupation"))
    occupation_label = binding_val(row, "occupationLabel") or ""
    image_url = binding_val(row, "image") or ""
    wiki_url = binding_val(row, "article") or ""

    # Parse dates
    birth_year = parse_year(birth_date_raw)
    death_year = parse_year(death_date_raw)
    born_display = format_date_display(birth_date_raw)
    died_display = format_date_display(death_date_raw)
    if birth_place and born_display:
        born_display = f"{born_display}, {birth_place}"
    if death_place and died_display:
        died_display = f"{died_display}, {death_place}"

    # Era from birth year
    era, era_slug = year_to_era(birth_year)

    # Division from occupation
    div_code, div_heading = get_division(occupation_qid)

    # Country / Region / Continent
    country_name, region, continent = get_country_info(country_qid)

    # Build slug
    slug = make_slug(name)

    # Build summary
    summary = description.capitalize() if description else f"{name}, {occupation_label}."
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

    # Build entity
    entity: dict[str, Any] = {
        "slug": slug,
        "name": name,
        "label": "Person",
        "callNumber": f"{div_code}.{slug}",
        "subjectHeadings": [f"People — {div_heading} — {country_name} — {era}"],
        "subjects": [s for s in [country_name, occupation_label, continent] if s and s != "Global"],
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
        ],
        "places": [],
        "texts": [],
    }

    # Optional fields
    if born_display:
        entity["born"] = born_display
    if died_display:
        entity["died"] = died_display
    if birth_place:
        entity["places"].append({"name": birth_place, "role": "Birth place"})
    if death_place and death_place != birth_place:
        entity["places"].append({"name": death_place, "role": "Death place"})
    if country_name and country_name != "Global":
        entity["places"].append({"name": country_name, "role": "Country"})

    # Wikidata metadata
    if qid:
        entity["wikidataQid"] = qid
    if wiki_url:
        entity["wikipediaUrl"] = wiki_url
    if image_url:
        entity["imageUrl"] = image_url

    return entity


def main():
    parser = argparse.ArgumentParser(description="Fetch notable people from Wikidata")
    parser.add_argument("--limit", type=int, default=200,
                        help="Max results per occupation batch (default: 200)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print SPARQL queries without executing")
    parser.add_argument("--output", type=str, default=None,
                        help="Output JSON file path")
    args = parser.parse_args()

    # Output path
    project_root = Path(__file__).resolve().parent.parent
    output_path = Path(args.output) if args.output else project_root / "data" / "wikidata_people.json"

    print("=" * 60)
    print("Wikidata People Fetch — Annals of the World")
    print("=" * 60)
    print(f"  Limit per batch: {args.limit}")
    print(f"  Output: {output_path}")
    print(f"  Occupation batches: {len(OCCUPATION_QUERIES)}")
    print()

    all_entities: list[dict[str, Any]] = []
    seen_slugs: set[str] = set()
    total_raw = 0

    for batch_name, occ_qids in OCCUPATION_QUERIES.items():
        print(f"[{batch_name}] Querying {len(occ_qids)} occupation(s)...")
        query = build_sparql_query(occ_qids, limit=args.limit)

        if args.dry_run:
            print(f"  (dry-run) SPARQL query for {batch_name}:")
            print(query[:200] + "...\n")
            continue

        rows = fetch_sparql(query)
        total_raw += len(rows)
        print(f"  Got {len(rows)} raw results")

        batch_count = 0
        for row in rows:
            entity = transform_person(row)
            if not entity:
                continue
            # Deduplicate by slug
            if entity["slug"] in seen_slugs:
                continue
            seen_slugs.add(entity["slug"])
            all_entities.append(entity)
            batch_count += 1

        print(f"  → {batch_count} unique entities added")
        # Be polite to Wikidata
        time.sleep(2)

    if args.dry_run:
        print("Dry run complete — no data fetched.")
        return

    # Sort by era then name
    era_order = {"Prehistoric": 0, "Classical": 1, "Medieval": 2, "Early Modern": 3, "Modern": 4, "Contemporary": 5}
    all_entities.sort(key=lambda e: (era_order.get(e["era"], 9), e["name"]))

    # Division stats
    div_counts: dict[str, int] = {}
    era_counts: dict[str, int] = {}
    for e in all_entities:
        div = e["callNumber"][:3]
        div_counts[div] = div_counts.get(div, 0) + 1
        era_counts[e["era"]] = era_counts.get(e["era"], 0) + 1

    # Write JSON
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_data = {
        "_meta": {
            "source": "Wikidata SPARQL (query.wikidata.org)",
            "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "total_raw_results": total_raw,
            "total_unique_entities": len(all_entities),
            "division_counts": dict(sorted(div_counts.items())),
            "era_counts": dict(sorted(era_counts.items())),
            "note": "Each entity follows the Annals of the World Entity schema (Person label, Class 2 divisions)",
        },
        "entities": all_entities,
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print()
    print("=" * 60)
    print("Fetch Complete")
    print("=" * 60)
    print(f"  Raw results: {total_raw}")
    print(f"  Unique entities: {len(all_entities)}")
    print(f"  Output: {output_path}")
    print()
    print("  By division:")
    for div, count in sorted(div_counts.items()):
        print(f"    {div}: {count}")
    print()
    print("  By era:")
    for era, count in sorted(era_counts.items(), key=lambda x: era_order.get(x[0], 9)):
        print(f"    {era}: {count}")


if __name__ == "__main__":
    main()
