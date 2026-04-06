#!/usr/bin/env python3
"""
Phase 4: Comprehensive Cleanup & Standardization
=================================================

1. Fix OCCURS_DURING → exact era divisions from callNumbers.ts
2. Remove SITUATED_IN / geographic OCCURS_IN (places tab covers this)
3. Remove CLASSIFIED_AS with field-XXX (divisionCode field covers this)
4. Remove phantom cause/effect rels (sentence-derived, truncated, generic)
5. Standardize all entity slugs (em-dash dates, consistent prefixes)
6. Fix wrong era assignments (modern events marked "Classical", etc.)
7. Create Timeframe entities for all 28 callNumbers.ts class-9 divisions
8. Update metadata
"""

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
PEOPLE_DIR = DATA_DIR / "people"

# ─── Era Divisions from callNumbers.ts (class 9) ─────────────────────────

ERA_DIVISIONS = [
    {"code": "910", "heading": "Prehistoric",                    "slug": "era-prehistoric",              "startYear": -70000, "endYear": -3000},
    {"code": "911", "heading": "Paleolithic & Mesolithic",       "slug": "era-paleolithic-mesolithic",    "startYear": -70000, "endYear": -10000},
    {"code": "912", "heading": "Neolithic & Chalcolithic",       "slug": "era-neolithic-chalcolithic",    "startYear": -10000, "endYear": -3300},
    {"code": "913", "heading": "Bronze Age",                     "slug": "era-bronze-age",               "startYear": -3300,  "endYear": -1200},
    {"code": "920", "heading": "Classical",                      "slug": "era-classical",                "startYear": -3000,  "endYear": 500},
    {"code": "921", "heading": "Archaic Period",                 "slug": "era-archaic-period",           "startYear": -800,   "endYear": -480},
    {"code": "922", "heading": "Hellenistic Period",             "slug": "era-hellenistic-period",       "startYear": -323,   "endYear": -31},
    {"code": "923", "heading": "Roman Period",                   "slug": "era-roman-period",             "startYear": -31,    "endYear": 284},
    {"code": "924", "heading": "Late Antiquity",                 "slug": "era-late-antiquity",           "startYear": 284,    "endYear": 600},
    {"code": "930", "heading": "Medieval",                       "slug": "era-medieval",                 "startYear": 500,    "endYear": 1500},
    {"code": "931", "heading": "Early Medieval / Dark Ages",     "slug": "era-early-medieval",           "startYear": 500,    "endYear": 1000},
    {"code": "932", "heading": "High Medieval",                  "slug": "era-high-medieval",            "startYear": 1000,   "endYear": 1300},
    {"code": "933", "heading": "Late Medieval",                  "slug": "era-late-medieval",            "startYear": 1300,   "endYear": 1500},
    {"code": "940", "heading": "Early Modern",                   "slug": "era-early-modern",             "startYear": 1500,   "endYear": 1800},
    {"code": "941", "heading": "Age of Exploration",             "slug": "era-age-of-exploration",       "startYear": 1400,   "endYear": 1600},
    {"code": "942", "heading": "Renaissance Period",             "slug": "era-renaissance-period",       "startYear": 1400,   "endYear": 1600},
    {"code": "943", "heading": "Reformation Era",                "slug": "era-reformation-era",          "startYear": 1517,   "endYear": 1648},
    {"code": "944", "heading": "Age of Enlightenment",           "slug": "era-age-of-enlightenment",     "startYear": 1685,   "endYear": 1815},
    {"code": "950", "heading": "Modern",                         "slug": "era-modern",                   "startYear": 1800,   "endYear": 1945},
    {"code": "951", "heading": "Industrial Age",                 "slug": "era-industrial-age",           "startYear": 1760,   "endYear": 1840},
    {"code": "952", "heading": "Age of Empire / New Imperialism","slug": "era-age-of-empire",            "startYear": 1870,   "endYear": 1914},
    {"code": "953", "heading": "Interwar Period",                "slug": "era-interwar-period",          "startYear": 1918,   "endYear": 1939},
    {"code": "954", "heading": "World War II Era",               "slug": "era-world-war-ii-era",         "startYear": 1939,   "endYear": 1945},
    {"code": "960", "heading": "Contemporary",                   "slug": "era-contemporary",             "startYear": 1945,   "endYear": 2030},
    {"code": "961", "heading": "Cold War Era",                   "slug": "era-cold-war-era",             "startYear": 1947,   "endYear": 1991},
    {"code": "962", "heading": "Post-Cold War & Globalization",  "slug": "era-post-cold-war",            "startYear": 1991,   "endYear": 2001},
    {"code": "963", "heading": "Digital Age",                    "slug": "era-digital-age",              "startYear": 2001,   "endYear": 2030},
]

# Map broad era name → parent division code
BROAD_ERA_MAP = {
    "Prehistoric":  "910",
    "Classical":    "920",
    "Medieval":     "930",
    "Early Modern": "940",
    "Modern":       "950",
    "Contemporary": "960",
}

# Sub-divisions for each broad era (most specific first for matching)
ERA_SUB_DIVISIONS = {
    "910": ["911", "912", "913"],
    "920": ["921", "922", "923", "924"],
    "930": ["931", "932", "933"],
    "940": ["941", "942", "943", "944"],
    "950": ["951", "952", "953", "954"],
    "960": ["961", "962", "963"],
}

ERA_DIV_MAP = {d["code"]: d for d in ERA_DIVISIONS}

# ─── Generic / Phantom slug patterns to remove ───────────────────────────

PHANTOM_PATTERNS = [
    r"^influenced-subsequent-historical",
    r"^historical-forces-and-geopolitical",
    r"^intellectual-inquiry-and-cultural",
    r"^discontent-with-existing-authority",
    r"^social-inequality-and-political-grievances",
    r"^shaped-religious-practice",
    r"^contributed-to-enduring-intellectual",
    r"^transformed-political-and-social",
    r"^provided-material-evidence-for",
    r"^historical-activity-leaving-material",
    r"^advanced-scientific-knowledge-and-method",
    r"^created-enduring-works-that-shaped",
    r"^expanded-human-knowledge-of-the-natural",
    r"^shifted-economic-structures",
    r"^influenced-intellectual-traditions",
    r"^emergence-of-new-cultural-forms",
    r"^political-upheaval-and-instability",
    r"^religious-reform-and-doctrinal-debate",
    r"^technological-change-and-societal-adapt",
    r"^military-conquest-and-territorial-expan",
    r"^demographic-shifts-and-population",
    r"^economic-disruption-and-resource-competi",
    r"^cultural-exchange-and-intellectual-cross",
    r"^institutional-reform-and-bureaucratic",
    r"^environmental-change-and-resource-press",
    r"^artistic-innovation-and-stylistic-development",
]

PHANTOM_RE = re.compile("|".join(PHANTOM_PATTERNS))


def slugify(name: str) -> str:
    """Canonical slug from a display name — follows docs/guidelines/slug_naming_convention.md."""
    s = name.lower().strip()
    s = s.replace("\u2013", "-").replace("\u2014", "-")  # em/en-dash
    s = re.sub(r"\s*\([^)]*\)\s*", " ", s)  # Remove parentheticals
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"-+", "-", s)
    s = s.strip("-")
    return s[:80]


def extract_year(text: str) -> int | None:
    """Extract a year from a date string like '1904 CE', '350 BCE', '-800'."""
    if not text:
        return None
    # Direct integer field
    if isinstance(text, (int, float)):
        return int(text)
    text = str(text).strip()
    # "1200 BCE" or "1200 bce"
    m = re.search(r"(\d{1,5})\s*BCE", text, re.IGNORECASE)
    if m:
        return -int(m.group(1))
    # "1200 CE" or just "1200"
    m = re.search(r"(\d{3,4})\s*(?:CE|AD)?", text, re.IGNORECASE)
    if m:
        yr = int(m.group(1))
        if yr > 0:
            return yr
    return None


def get_best_year(entity: dict) -> int | None:
    """Get the best available year from an entity."""
    for field in ["startYear", "born", "founded", "date"]:
        val = entity.get(field)
        if val is not None and val != "":
            yr = extract_year(val)
            if yr is not None:
                return yr
    return None


def correct_era_from_year(year: int) -> str:
    """Return the correct broad era name for a given year."""
    if year < -3000:
        return "Prehistoric"
    elif year < 500:
        return "Classical"
    elif year < 1500:
        return "Medieval"
    elif year < 1800:
        return "Early Modern"
    elif year < 1945:
        return "Modern"
    else:
        return "Contemporary"


def get_specific_era_division(year: int, broad_era: str) -> dict:
    """
    Given a year and broad era, return the most specific sub-division.
    Falls back to the parent division if no sub-division matches.
    """
    parent_code = BROAD_ERA_MAP.get(broad_era, "920")
    sub_codes = ERA_SUB_DIVISIONS.get(parent_code, [])

    # Try to match a sub-division
    for code in sub_codes:
        div = ERA_DIV_MAP[code]
        if div["startYear"] <= year <= div["endYear"]:
            return div

    # Fallback to parent division
    return ERA_DIV_MAP[parent_code]


def is_phantom_slug(slug: str) -> bool:
    """Check if a slug is a phantom (sentence-derived non-entity)."""
    if PHANTOM_RE.search(slug):
        return True
    # Truncated at ~50 chars (ends mid-word)
    if len(slug) >= 48 and not slug.endswith(("s", "e", "d", "n", "y", "t", "r", "l", "a", "o", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")):
        return True
    # Very long slugs that look like sentences
    if len(slug) > 45 and slug.count("-") > 6:
        return True
    return False


def is_place_relationship(rel: dict) -> bool:
    """Check if a relationship is geographic (covered by places tab)."""
    verb = rel.get("verb", "")
    target_slug = rel.get("targetSlug", "")

    # SITUATED_IN always geographic
    if verb == "SITUATED_IN":
        return True

    # OCCURS_IN with country/region/continent target
    if verb == "OCCURS_IN":
        if target_slug.startswith("country-"):
            return True
        if target_slug.startswith("city-"):
            return True
        if target_slug.startswith("region-"):
            return True
        # Bare country names (check common ones)
        if target_slug in _COUNTRY_SLUGS:
            return True
        # Continent names
        if target_slug in ("africa", "asia", "europe", "north-america",
                           "south-america", "oceania", "antarctica",
                           "americas", "middle-east"):
            return True

    return False


def is_classified_as(rel: dict) -> bool:
    """Check if a relationship is a CLASSIFIED_AS field-XXX type."""
    return (rel.get("verb") == "CLASSIFIED_AS" or
            (rel.get("targetSlug", "").startswith("field-")))


def fix_slug(slug: str) -> str:
    """Fix common slug problems."""
    s = slug
    # Fix merged year ranges: 197475 → 1974-75, 19871989 → 1987-1989
    s = re.sub(r"^(\d{4})(\d{2,4})-", r"\1-\2-", s)
    # Fix en/em-dash remnants
    s = s.replace("\u2013", "-").replace("\u2014", "-")
    # Lowercase
    s = s.lower()
    # Remove special chars
    s = re.sub(r"[^a-z0-9-]", "", s)
    # Collapse hyphens
    s = re.sub(r"-+", "-", s)
    s = s.strip("-")
    return s[:80]


def build_occurs_during(entity: dict, year: int | None, era: str) -> dict | None:
    """Build an OCCURS_DURING relationship targeting the specific era division."""
    if not era:
        return None

    if year is not None:
        div = get_specific_era_division(year, era)
    else:
        parent_code = BROAD_ERA_MAP.get(era, "920")
        div = ERA_DIV_MAP.get(parent_code)

    if not div:
        return None

    return {
        "sourceSlug": entity["slug"],
        "sourceName": entity["name"],
        "verb": "OCCURS_DURING",
        "targetSlug": div["slug"],
        "targetName": div["heading"],
        "context": f"{entity['name']} is situated within the {div['heading']} ({div['code']})",
    }


# ─── Country slug set (bare names) ───────────────────────────────────────

_COUNTRY_SLUGS = {
    "afghanistan", "albania", "algeria", "andorra", "angola",
    "argentina", "armenia", "australia", "austria", "azerbaijan",
    "bahamas", "bahrain", "bangladesh", "barbados", "belarus",
    "belgium", "belize", "benin", "bhutan", "bolivia",
    "bosnia-and-herzegovina", "botswana", "brazil", "brunei", "bulgaria",
    "burkina-faso", "burundi", "cambodia", "cameroon", "canada",
    "cape-verde", "central-african-republic", "chad", "chile", "china",
    "colombia", "comoros", "congo", "costa-rica", "croatia",
    "cuba", "cyprus", "czech-republic", "czechia", "denmark",
    "djibouti", "dominica", "dominican-republic", "ecuador", "egypt",
    "el-salvador", "equatorial-guinea", "eritrea", "estonia", "eswatini",
    "ethiopia", "fiji", "finland", "france", "gabon",
    "gambia", "georgia", "germany", "ghana", "greece",
    "grenada", "guatemala", "guinea", "guinea-bissau", "guyana",
    "haiti", "honduras", "hungary", "iceland", "india",
    "indonesia", "iran", "iraq", "ireland", "israel",
    "italy", "ivory-coast", "jamaica", "japan", "jordan",
    "kazakhstan", "kenya", "kiribati", "kosovo", "kuwait",
    "kyrgyzstan", "laos", "latvia", "lebanon", "lesotho",
    "liberia", "libya", "liechtenstein", "lithuania", "luxembourg",
    "madagascar", "malawi", "malaysia", "maldives", "mali",
    "malta", "marshall-islands", "mauritania", "mauritius", "mexico",
    "micronesia", "moldova", "monaco", "mongolia", "montenegro",
    "morocco", "mozambique", "myanmar", "namibia", "nauru",
    "nepal", "netherlands", "new-zealand", "nicaragua", "niger",
    "nigeria", "north-korea", "north-macedonia", "norway", "oman",
    "pakistan", "palau", "palestine", "panama", "papua-new-guinea",
    "paraguay", "peru", "philippines", "poland", "portugal",
    "qatar", "romania", "russia", "rwanda", "saint-kitts-and-nevis",
    "saint-lucia", "saint-vincent", "samoa", "san-marino", "sao-tome-and-principe",
    "saudi-arabia", "senegal", "serbia", "seychelles", "sierra-leone",
    "singapore", "slovakia", "slovenia", "solomon-islands", "somalia",
    "south-africa", "south-korea", "south-sudan", "spain", "sri-lanka",
    "sudan", "suriname", "sweden", "switzerland", "syria",
    "taiwan", "tajikistan", "tanzania", "thailand", "timor-leste",
    "togo", "tonga", "trinidad-and-tobago", "tunisia", "turkey",
    "turkmenistan", "tuvalu", "uganda", "ukraine", "united-arab-emirates",
    "united-kingdom", "united-states", "uruguay", "uzbekistan", "vanuatu",
    "vatican-city", "venezuela", "vietnam", "yemen", "zambia", "zimbabwe",
    # Common historical/variant names
    "persia", "ottoman-empire", "byzantine-empire", "roman-empire",
    "holy-roman-empire", "soviet-union", "ussr", "prussia",
    "mesopotamia", "fertile-crescent", "levant", "anatolia",
    "hispania", "gaul", "britannia", "nubia", "kush",
    "south-korea", "north-korea",
}


def create_timeframe_entities() -> list[dict]:
    """Create Timeframe entities for all 28 era divisions from callNumbers.ts."""
    entities = []
    for div in ERA_DIVISIONS:
        start_label = f"{abs(div['startYear'])} {'BCE' if div['startYear'] < 0 else 'CE'}"
        end_label = f"{abs(div['endYear'])} {'BCE' if div['endYear'] < 0 else 'CE'}"

        # Determine parent era
        parent_code = div["code"][:2] + "0"
        parent_div = ERA_DIV_MAP.get(parent_code, {})
        parent_name = parent_div.get("heading", "")
        is_sub = div["code"] != parent_code

        entity = {
            "slug": div["slug"],
            "name": div["heading"],
            "label": "Timeframe",
            "callNumber": f"9{div['code'][1:]}.{div['slug']}",
            "subjectHeadings": [f"Timeframe — {div['heading']}"],
            "subjects": ["Timeframe", div["heading"]],
            "summary": (
                f"The {div['heading']} spans from approximately {start_label} to {end_label}. "
                f"{'It is a sub-period of the broader ' + parent_name + ' era. ' if is_sub else ''}"
                f"This timeframe classification follows the Annals of the World Dewey-style "
                f"system (division {div['code']})."
            ),
            "era": parent_name if is_sub else div["heading"],
            "eraSlug": parent_div.get("slug", div["slug"]) if is_sub else div["slug"],
            "region": "Global",
            "continent": "Global",
            "status": "Published",
            "frameworks": ["TEMPORAL_LINKAGE", "CAUSE_AND_EFFECT"],
            "causes": [],
            "effects": [],
            "relationships": [],
            "places": [],
            "texts": [],
            "divisionCode": div["code"],
            "divisionHeading": div["heading"],
            "historicalSignificance": {"score": 10, "label": "Landmark", "sitelinks": 100},
            "inAppwrite": False,
            "startYear": div["startYear"],
            "endYear": div["endYear"],
            "date": start_label,
            "endDate": end_label,
            "wikidataQid": "",
            "wikipediaUrl": "",
            "imageUrl": "",
            "thumbnailUrl": "",
            "importanceScore": 10,
            "altNames": [],
            "externalLinks": [],
            "tags": ["timeframe", "era", div["heading"].lower()],
            "quote": "",
            "legacySummary": f"The {div['heading']} is a foundational period in the Annals chronological framework, used to classify entities active from {start_label} to {end_label}.",
            "enrichedSummary": True,
        }

        # Add parent-child relationships for sub-periods
        if is_sub:
            entity["relationships"].append({
                "sourceSlug": div["slug"],
                "sourceName": div["heading"],
                "verb": "OCCURS_DURING",
                "targetSlug": parent_div.get("slug", ""),
                "targetName": parent_name,
                "context": f"{div['heading']} is a sub-period within the broader {parent_name} era",
            })

        entities.append(entity)

    return entities


def process_relationships(entity: dict, year: int | None, era: str) -> list[dict]:
    """
    Clean and rebuild the relationships array:
    - Remove place/geographic rels (places tab handles)
    - Remove CLASSIFIED_AS field-XXX (divisionCode handles)
    - Remove phantom cause/effect rels
    - Fix OCCURS_DURING to use specific era division
    """
    old_rels = entity.get("relationships", [])
    new_rels = []
    seen_keys = set()

    # 1) Build proper OCCURS_DURING
    od_rel = build_occurs_during(entity, year, era)
    if od_rel:
        key = f"{od_rel['verb']}:{od_rel['targetSlug']}"
        seen_keys.add(key)
        new_rels.append(od_rel)

    # 2) Filter existing rels
    for rel in old_rels:
        verb = rel.get("verb", "")
        target_slug = rel.get("targetSlug", "")
        source_slug = rel.get("sourceSlug", "")

        # Skip old OCCURS_DURING (replaced above)
        if verb == "OCCURS_DURING":
            continue

        # Skip geographic relationships
        if is_place_relationship(rel):
            continue

        # Skip CLASSIFIED_AS / field-XXX
        if is_classified_as(rel):
            continue

        # Skip phantom cause/effect slugs
        if verb == "CAUSES":
            if is_phantom_slug(target_slug) or is_phantom_slug(source_slug):
                continue

        # Deduplicate
        key = f"{verb}:{target_slug}"
        if key in seen_keys:
            continue
        seen_keys.add(key)

        # Fix slugs in the relationship
        rel["targetSlug"] = fix_slug(rel["targetSlug"])
        rel["sourceSlug"] = fix_slug(rel["sourceSlug"])

        new_rels.append(rel)

    return new_rels


def fix_entity_era(entity: dict) -> tuple[str, str]:
    """Fix era and eraSlug based on actual dates, return corrected values."""
    era = entity.get("era", "")
    year = get_best_year(entity)

    if year is not None:
        correct_era = correct_era_from_year(year)
        if correct_era != era and era:
            # Era is wrong — fix it
            era = correct_era

    era_slug = slugify(era) if era else ""
    return era, era_slug


def process_file(filepath: Path) -> tuple[dict, dict]:
    """Process a single JSON file with Phase 4 cleanup."""
    print(f"\n  Processing {filepath.name}...", flush=True)

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    entities = data["entities"]
    stats = {
        "total": len(entities),
        "era_fixed": 0,
        "rels_removed": 0,
        "rels_remaining": 0,
        "slugs_fixed": 0,
        "phantom_removed": 0,
    }

    for entity in entities:
        # 1) Fix slug
        old_slug = entity.get("slug", "")
        new_slug = fix_slug(old_slug)
        if new_slug != old_slug:
            entity["slug"] = new_slug
            stats["slugs_fixed"] += 1

        # 2) Fix era assignment
        old_era = entity.get("era", "")
        era, era_slug = fix_entity_era(entity)
        if era != old_era:
            entity["era"] = era
            entity["eraSlug"] = era_slug
            stats["era_fixed"] += 1
        elif not entity.get("eraSlug"):
            entity["eraSlug"] = era_slug

        # 3) Get year for specific era division
        year = get_best_year(entity)

        # 4) Clean & rebuild relationships
        old_count = len(entity.get("relationships", []))
        entity["relationships"] = process_relationships(entity, year, era)
        new_count = len(entity["relationships"])
        removed = old_count - new_count
        if removed > 0:
            stats["rels_removed"] += removed
        stats["rels_remaining"] += new_count

    # Update metadata
    if "_meta" in data:
        data["_meta"]["entity_count"] = len(entities)
        data["_meta"]["audit_timestamp"] = "2026-04-04T21:00:00Z"
        data["_meta"]["audit_version"] = "4.0"

    print(f"    Entities: {len(entities):,} | era_fixed: {stats['era_fixed']:,} | "
          f"rels_removed: {stats['rels_removed']:,} | rels_left: {stats['rels_remaining']:,} | "
          f"slugs_fixed: {stats['slugs_fixed']}")

    return data, stats


def main():
    print("╔═══════════════════════════════════════════════════════════╗")
    print("║  Phase 4: Cleanup, Era Divisions & Slug Standardization  ║")
    print("╚═══════════════════════════════════════════════════════════╝")

    # ── Step 1: Create Timeframe entities ──────────────────────────────
    print("\n[1/3] Creating Timeframe entities for all 28 era divisions...")
    tf_path = DATA_DIR / "wikidata_timeframes.json"
    with open(tf_path, "r", encoding="utf-8") as f:
        tf_data = json.load(f)

    existing_slugs = {e["slug"] for e in tf_data["entities"]}
    new_tf = create_timeframe_entities()
    added_tf = 0
    for tf in new_tf:
        if tf["slug"] not in existing_slugs:
            tf_data["entities"].append(tf)
            existing_slugs.add(tf["slug"])
            added_tf += 1

    print(f"  Added {added_tf} new Timeframe entities (28 divisions, {added_tf} were new)")

    # ── Step 2: Process all files ──────────────────────────────────────
    print("\n[2/3] Processing all JSON files...")

    files = sorted(DATA_DIR.glob("wikidata_*.json"))
    files = [f for f in files if f.name != "wikidata_people.json"]
    if PEOPLE_DIR.exists():
        files += sorted(PEOPLE_DIR.glob("wikidata_people_*.json"))

    total_stats = defaultdict(int)

    for fp in files:
        data, stats = process_file(fp)

        with open(fp, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        for k, v in stats.items():
            total_stats[k] += v

    # ── Step 3: Save updated timeframes ────────────────────────────────
    tf_data["_meta"]["entity_count"] = len(tf_data["entities"])
    tf_data["_meta"]["audit_timestamp"] = "2026-04-04T21:00:00Z"
    tf_data["_meta"]["audit_version"] = "4.0"

    with open(tf_path, "w", encoding="utf-8") as f:
        json.dump(tf_data, f, indent=2, ensure_ascii=False)

    # ── Step 4: Update people manifest ─────────────────────────────────
    if PEOPLE_DIR.exists():
        manifest_files = {}
        total_people = 0
        for f in sorted(PEOPLE_DIR.glob("wikidata_people_*.json")):
            with open(f) as fh:
                d = json.load(fh)
            count = len(d["entities"])
            total_people += count
            manifest_files[f.stem] = {
                "entity_count": count,
                "size_mb": round(f.stat().st_size / (1024 * 1024), 1),
            }
        manifest = {
            "_meta": {
                "description": "Index of split people JSON files by division group",
                "total_entities": total_people,
                "total_files": len(manifest_files),
                "audit_timestamp": "2026-04-04T21:00:00Z",
            },
            "files": manifest_files,
        }
        with open(PEOPLE_DIR / "_manifest.json", "w") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)

    # ── Final Report ───────────────────────────────────────────────────
    print("\n╔═══════════════════════════════════════════════════════════╗")
    print("║                 PHASE 4 CLEANUP REPORT                   ║")
    print("╠═══════════════════════════════════════════════════════════╣")
    print(f"║  Entities processed:           {total_stats['total']:>10,}              ║")
    print(f"║  Era assignments corrected:    {total_stats['era_fixed']:>10,}              ║")
    print(f"║  Relationships removed:        {total_stats['rels_removed']:>10,}              ║")
    print(f"║  Relationships remaining:      {total_stats['rels_remaining']:>10,}              ║")
    print(f"║  Slugs standardized:           {total_stats['slugs_fixed']:>10,}              ║")
    print(f"║  Timeframe entities added:     {added_tf:>10,}              ║")
    print("╚═══════════════════════════════════════════════════════════╝")


if __name__ == "__main__":
    main()
