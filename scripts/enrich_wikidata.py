#!/usr/bin/env python3
"""
Wikidata JSON Enrichment & Housekeeping Script
===============================================

Tasks:
1. Pretty-print all wikidata JSON files
2. Enrich hollow/generic summaries with richer descriptions
3. Clean up timeframes JSON — move dynasties -> institutions, arch styles -> ideas
4. Split people JSON into smaller division-based files
5. Add missing v2 attributes (thumbnailUrl, importanceScore, altNames, etc.)
6. Verify all entities have meaningful summaries

Usage:
    python3 scripts/enrich_wikidata.py
"""

import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

# ─── Configuration ────────────────────────────────────────────────────────
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
OUTPUT_DIR = DATA_DIR  # write back in place

# People split output directory
PEOPLE_SPLIT_DIR = DATA_DIR / "people"

# Division headings for people (Class 2)
PEOPLE_DIVISIONS = {
    "201": "Educators & Academics",
    "202": "Merchants & Economists",
    "203": "Athletes & Competitors",
    "204": "Architects & Engineers",
    "205": "Journalists & Chroniclers",
    "210": "Philosophers & Thinkers",
    "211": "Logicians & Mathematicians",
    "212": "Ethicists & Moralists",
    "220": "Political Leaders",
    "221": "Monarchs & Rulers",
    "222": "Heads of State & Government",
    "223": "Tribal & Indigenous Leaders",
    "230": "Legal Figures",
    "231": "Jurists & Legal Scholars",
    "240": "Scientists & Inventors",
    "241": "Physicians & Medical Pioneers",
    "242": "Astronomers & Cosmologists",
    "243": "Naturalists & Biologists",
    "250": "Religious Figures",
    "251": "Prophets & Founders",
    "252": "Theologians & Scholars",
    "253": "Missionaries",
    "260": "Artists & Writers",
    "261": "Authors & Novelists",
    "262": "Poets & Playwrights",
    "263": "Composers & Musicians",
    "264": "Painters & Sculptors",
    "265": "Architects & Designers",
    "270": "Activists & Reformers",
    "271": "Abolitionists",
    "272": "Suffragists & Feminists",
    "273": "Labor Organizers",
    "280": "Military Leaders & Commanders",
    "281": "Naval Commanders",
    "282": "Intelligence & Espionage",
    "283": "Modern Military Commanders",
    "290": "Explorers & Navigators",
    "291": "Space Explorers",
    "292": "Deep-Sea Explorers",
    "293": "Cartographers",
}

# Division groupings for file splitting (group sub-divisions under parent)
PEOPLE_DIVISION_GROUPS = {
    "educators": ["201"],
    "merchants-economists": ["202"],
    "athletes": ["203"],
    "architects-engineers": ["204"],
    "journalists": ["205"],
    "philosophers": ["210", "211", "212"],
    "political-leaders": ["220", "221", "222", "223"],
    "legal-figures": ["230", "231"],
    "scientists": ["240", "241", "242", "243"],
    "religious-figures": ["250", "251", "252", "253"],
    "artists-writers": ["260", "261", "262", "263", "264", "265"],
    "activists": ["270", "271", "272", "273"],
    "military": ["280", "281", "282", "283"],
    "explorers": ["290", "291", "292", "293"],
}

# Maximum file size target for GitHub (< 100MB, aim for ~50MB)
MAX_FILE_SIZE_MB = 50


# ─── Summary Enrichment Templates ─────────────────────────────────────────

def is_hollow_summary(summary: str) -> bool:
    """Detect template-like, generic, or hollow summaries."""
    if not summary or len(summary.strip()) < 20:
        return True

    hollow_patterns = [
        r"^.{1,30}\s+Associated with\s+",
        r"^.{1,30}\s+Based in\s+",
        r"^.{1,30}\s+From\s+\w+\.\s*Dating to",
        r"^.{1,30}\s+Part of\s+",
        r"^.{1,50}\s+Born in\s+\w+\.\s*\(",
        r"^.{1,50}\s+Active during the\s+\w+\s+era\.$",
        r"^.{1,30}\s+is a\s+\w+\s+(based|located|from)\s+in\s+",
        r"^.{1,50}\s+Occurred in\s+\w+\.$",
        r"^.{1,50}\s+Founded/began:",
        r"^Human settlement\s+",
        r"^Archaeological site in\s+\w+\s+",
        r"originating in\s+\w+\s+organization",
    ]

    for pattern in hollow_patterns:
        if re.search(pattern, summary, re.IGNORECASE):
            return True

    # Very short summaries with just role + location
    words = summary.split()
    if len(words) < 15 and any(
        w in summary.lower() for w in ["associated with", "based in", "from ", "born in"]
    ):
        return True

    return False


def enrich_person_summary(entity: dict) -> str:
    """Generate a richer summary for a Person entity."""
    name = entity.get("name", "")
    summary = entity.get("summary", "")
    era = entity.get("era", "")
    division = entity.get("divisionHeading", "")
    born = entity.get("born", "")
    died = entity.get("died", "")
    continent = entity.get("continent", "")
    region = entity.get("region", "")
    frameworks = entity.get("frameworks", [])
    subjects = entity.get("subjects", [])
    sig = entity.get("historicalSignificance", {})
    sig_label = sig.get("label", "")
    sig_score = sig.get("score", 0)
    causes = entity.get("causes", [])
    effects = entity.get("effects", [])
    places = entity.get("places", [])

    # If summary is already rich (>150 chars and not hollow), keep it
    if len(summary) > 150 and not is_hollow_summary(summary):
        return summary

    # Extract role from existing short summary
    role = ""
    if summary:
        # Try to extract role before "Born in" or "Associated with"
        role_match = re.match(r"^(.+?)(?:\s+Born in|\s+Associated with|\s+Based in|\s+From\b|\.\s*\()", summary)
        if role_match:
            role = role_match.group(1).strip().rstrip(".")

    if not role and division:
        role = division.lower()

    # Build era context
    era_phrase = f"the {era} era" if era else "history"

    # Build date range
    date_phrase = ""
    if born and died:
        date_phrase = f" ({born} – {died})"
    elif born:
        date_phrase = f" (b. {born})"

    # Build location context
    location = ""
    if places:
        place_names = [p.get("name", "") for p in places if p.get("name")]
        if place_names:
            location = f" in {place_names[0]}"
    elif continent and continent != "Global":
        location = f" in {continent}"

    # Build significance phrase
    sig_phrase = ""
    if sig_score >= 8:
        sig_phrase = f", recognized as a landmark figure in {era_phrase}"
    elif sig_score >= 6:
        sig_phrase = f", a notable figure of {era_phrase}"
    elif sig_score >= 4:
        sig_phrase = f" who made significant contributions during {era_phrase}"
    else:
        sig_phrase = f" active during {era_phrase}"

    # Build framework context
    framework_phrases = []
    fw_map = {
        "CAUSE_AND_EFFECT": "causality and historical consequence",
        "POLITICAL_SYSTEMS": "political systems and governance",
        "EMPIRE_AND_COLONIALISM": "empire and colonial dynamics",
        "MILITARY_STRATEGY": "military strategy and conflict",
        "ECONOMIC_SYSTEMS": "economic development and trade",
        "RELIGIOUS_AND_THEOLOGICAL": "religious and theological thought",
        "SCIENTIFIC_REVOLUTION": "scientific inquiry and discovery",
        "CULTURAL_EXCHANGE": "cultural exchange and diffusion",
        "SOCIAL_MOVEMENTS": "social reform and movements",
        "TECHNOLOGICAL_CHANGE": "technological innovation",
        "ENVIRONMENTAL_HISTORY": "environmental and ecological history",
        "GENDER_AND_POWER": "gender dynamics and power",
        "GEOPOLITICAL_LINKAGE": "geopolitical linkage and diplomacy",
        "LEGAL_EVOLUTION": "legal evolution and jurisprudence",
        "INTELLECTUAL_HISTORY": "intellectual history and philosophy",
        "DEMOGRAPHIC_SHIFTS": "demographic change and migration",
    }
    for fw in frameworks[:2]:
        if fw in fw_map:
            framework_phrases.append(fw_map[fw])

    # Build effects/legacy phrase
    legacy_phrase = ""
    if effects:
        effect_titles = [e.get("title", "") for e in effects[:2] if isinstance(e, dict)]
        if effect_titles and effect_titles[0]:
            legacy_phrase = f" {effect_titles[0].rstrip('.')}."

    # Assemble enriched summary
    parts = []
    if role:
        parts.append(f"{name} was a {role}{location}{date_phrase}{sig_phrase}.")
    else:
        parts.append(f"{name} was a historical figure{location}{date_phrase}{sig_phrase}.")

    if framework_phrases:
        parts.append(
            f"Their work intersected with {' and '.join(framework_phrases)}."
        )

    if legacy_phrase:
        parts.append(legacy_phrase)

    return " ".join(parts)


def enrich_institution_summary(entity: dict) -> str:
    """Generate a richer summary for an Institution entity."""
    name = entity.get("name", "")
    summary = entity.get("summary", "")
    era = entity.get("era", "")
    inst_type = entity.get("institutionType", "")
    founded = entity.get("founded", "")
    dissolved = entity.get("dissolved", "")
    headquarters = entity.get("headquarters", "")
    continent = entity.get("continent", "")
    is_active = entity.get("isActive", False)
    division = entity.get("divisionHeading", "")
    frameworks = entity.get("frameworks", [])
    sig = entity.get("historicalSignificance", {})
    sig_score = sig.get("score", 0)
    effects = entity.get("effects", [])

    if len(summary) > 150 and not is_hollow_summary(summary):
        return summary

    # Build type description
    type_phrase = inst_type or division or "institution"

    # Build location
    location = ""
    if headquarters:
        location = f" headquartered in {headquarters}"
    elif continent and continent != "Global":
        location = f" based in {continent}"

    # Build date context
    date_phrase = ""
    if founded and dissolved:
        date_phrase = f", founded in {founded} and dissolved in {dissolved}"
    elif founded:
        status = "active since" if is_active else "founded in"
        date_phrase = f", {status} {founded}"

    # Build significance
    sig_phrase = ""
    if sig_score >= 7:
        sig_phrase = f" It played a major role in shaping {era} history."
    elif sig_score >= 4:
        sig_phrase = f" It contributed significantly to the institutional landscape of the {era} era."

    # Build effects/legacy
    legacy = ""
    if effects:
        effect_titles = [e.get("title", "") for e in effects[:1] if isinstance(e, dict)]
        if effect_titles and effect_titles[0]:
            legacy = f" Its legacy includes: {effect_titles[0].rstrip('.')}."

    return f"{name} is a {type_phrase}{location}{date_phrase}.{sig_phrase}{legacy}"


def enrich_event_summary(entity: dict) -> str:
    """Generate a richer summary for an EventWindow entity."""
    name = entity.get("name", "")
    summary = entity.get("summary", "")
    era = entity.get("era", "")
    event_type = entity.get("eventType", "")
    start_year = entity.get("startYear", "")
    end_year = entity.get("endYear", "")
    continent = entity.get("continent", "")
    division = entity.get("divisionHeading", "")
    sig = entity.get("historicalSignificance", {})
    sig_score = sig.get("score", 0)
    causes = entity.get("causes", [])
    effects = entity.get("effects", [])
    places = entity.get("places", [])

    if len(summary) > 150 and not is_hollow_summary(summary):
        return summary

    type_phrase = event_type or division or "historical event"
    location = ""
    if places:
        pnames = [p.get("name", "") for p in places if p.get("name")]
        if pnames:
            location = f" in {pnames[0]}"
    elif continent and continent != "Global":
        location = f" in {continent}"

    date_phrase = ""
    if start_year and end_year:
        date_phrase = f" ({start_year} – {end_year})"
    elif start_year:
        date_phrase = f" ({start_year})"

    sig_phrase = ""
    if sig_score >= 7:
        sig_phrase = f", a landmark event of the {era} era"
    elif sig_score >= 4:
        sig_phrase = f", a significant occurrence during the {era} era"

    cause_phrase = ""
    if causes:
        cause_titles = [c.get("title", "") for c in causes[:1] if isinstance(c, dict)]
        if cause_titles and cause_titles[0]:
            cause_phrase = f" It arose from {cause_titles[0].rstrip('.').lower()}."

    effect_phrase = ""
    if effects:
        effect_titles = [e.get("title", "") for e in effects[:1] if isinstance(e, dict)]
        if effect_titles and effect_titles[0]:
            effect_phrase = f" Its consequences included {effect_titles[0].rstrip('.').lower()}."

    return f"{name} was a {type_phrase}{location}{date_phrase}{sig_phrase}.{cause_phrase}{effect_phrase}"


def enrich_movement_summary(entity: dict) -> str:
    """Generate a richer summary for a Movement entity."""
    name = entity.get("name", "")
    summary = entity.get("summary", "")
    era = entity.get("era", "")
    mov_type = entity.get("movementType", "")
    start_year = entity.get("startYear", "")
    end_year = entity.get("endYear", "")
    continent = entity.get("continent", "")
    division = entity.get("divisionHeading", "")
    sig = entity.get("historicalSignificance", {})
    sig_score = sig.get("score", 0)
    effects = entity.get("effects", [])

    if len(summary) > 150 and not is_hollow_summary(summary):
        return summary

    type_phrase = mov_type or division or "movement"
    location = ""
    if continent and continent != "Global":
        location = f" originating in {continent}"

    date_phrase = ""
    if start_year and end_year:
        date_phrase = f", active from {start_year} to {end_year}"
    elif start_year:
        date_phrase = f", emerging around {start_year}"

    sig_phrase = ""
    if sig_score >= 7:
        sig_phrase = f" It was a major force in {era} history."
    elif sig_score >= 4:
        sig_phrase = f" It shaped the {era} landscape in significant ways."

    effect_phrase = ""
    if effects:
        effect_titles = [e.get("title", "") for e in effects[:1] if isinstance(e, dict)]
        if effect_titles and effect_titles[0]:
            effect_phrase = f" Its impact included {effect_titles[0].rstrip('.').lower()}."

    return f"{name} was a {type_phrase}{location}{date_phrase}.{sig_phrase}{effect_phrase}"


def enrich_place_summary(entity: dict) -> str:
    """Generate a richer summary for a Place entity."""
    name = entity.get("name", "")
    summary = entity.get("summary", "")
    place_type = entity.get("placeType", "")
    founded = entity.get("founded", "")
    continent = entity.get("continent", "")
    region = entity.get("region", "")
    population = entity.get("population", "")
    division = entity.get("divisionHeading", "")
    sig = entity.get("historicalSignificance", {})
    sig_score = sig.get("score", 0)
    effects = entity.get("effects", [])

    if len(summary) > 150 and not is_hollow_summary(summary):
        return summary

    type_phrase = place_type or division or "place"
    location = ""
    if region and region != "Global":
        location = f" in {region}"
    elif continent and continent != "Global":
        location = f" in {continent}"

    date_phrase = ""
    if founded:
        date_phrase = f", established around {founded}"

    pop_phrase = ""
    if population:
        pop_phrase = f" with a population of approximately {population:,}" if isinstance(population, int) else ""

    sig_phrase = ""
    if sig_score >= 7:
        sig_phrase = " It has played a pivotal role in regional and global history."
    elif sig_score >= 4:
        sig_phrase = " It holds notable historical significance."

    return f"{name} is a {type_phrase}{location}{date_phrase}{pop_phrase}.{sig_phrase}"


def enrich_idea_summary(entity: dict) -> str:
    """Generate a richer summary for an Idea entity."""
    name = entity.get("name", "")
    summary = entity.get("summary", "")
    idea_type = entity.get("ideaType", "")
    origin_date = entity.get("originDate", "")
    founder = entity.get("founder", "")
    continent = entity.get("continent", "")
    division = entity.get("divisionHeading", "")
    sig = entity.get("historicalSignificance", {})
    sig_score = sig.get("score", 0)
    effects = entity.get("effects", [])

    if len(summary) > 150 and not is_hollow_summary(summary):
        return summary

    type_phrase = idea_type or division or "concept"
    location = ""
    if continent and continent != "Global":
        location = f" with origins in {continent}"

    date_phrase = ""
    if origin_date:
        date_phrase = f", emerging around {origin_date}"

    founder_phrase = ""
    if founder:
        founder_phrase = f" Attributed to or associated with {founder}."

    sig_phrase = ""
    if sig_score >= 7:
        sig_phrase = " It fundamentally shaped intellectual and practical discourse across civilizations."
    elif sig_score >= 4:
        sig_phrase = " It contributed meaningfully to the evolution of thought and practice."

    effect_phrase = ""
    if effects:
        effect_titles = [e.get("title", "") for e in effects[:1] if isinstance(e, dict)]
        if effect_titles and effect_titles[0]:
            effect_phrase = f" Its influence extended to {effect_titles[0].rstrip('.').lower()}."

    return f"{name} is a {type_phrase}{location}{date_phrase}.{founder_phrase}{sig_phrase}{effect_phrase}"


def enrich_artifact_summary(entity: dict) -> str:
    """Generate a richer summary for an artifact/text entity."""
    name = entity.get("name", "")
    summary = entity.get("summary", "")
    art_type = entity.get("artifactType", "")
    created = entity.get("created", "")
    creator = entity.get("creator", "")
    continent = entity.get("continent", "")
    division = entity.get("divisionHeading", "")
    sig = entity.get("historicalSignificance", {})
    sig_score = sig.get("score", 0)

    if len(summary) > 150 and not is_hollow_summary(summary):
        return summary

    type_phrase = art_type or division or "artifact"
    location = ""
    if continent and continent != "Global":
        location = f" from {continent}"

    date_phrase = ""
    if created:
        date_phrase = f", dating to {created}"

    creator_phrase = ""
    if creator:
        creator_phrase = f" Created by {creator}."

    sig_phrase = ""
    if sig_score >= 7:
        sig_phrase = " It is considered a landmark work of historical and cultural significance."
    elif sig_score >= 4:
        sig_phrase = " It holds notable significance in its field."

    return f"{name} is a {type_phrase}{location}{date_phrase}.{creator_phrase}{sig_phrase}"


def enrich_evidence_summary(entity: dict) -> str:
    """Generate a richer summary for an Evidence entity."""
    name = entity.get("name", "")
    summary = entity.get("summary", "")
    ev_type = entity.get("evidenceType", "")
    ev_tier = entity.get("evidenceTier", "")
    ev_tier_label = entity.get("evidenceTierLabel", "")
    created = entity.get("created", "")
    continent = entity.get("continent", "")
    division = entity.get("divisionHeading", "")
    sig = entity.get("historicalSignificance", {})
    sig_score = sig.get("score", 0)

    if len(summary) > 150 and not is_hollow_summary(summary):
        return summary

    type_phrase = ev_type or division or "evidence source"
    location = ""
    if continent and continent != "Global":
        location = f" from {continent}"

    date_phrase = ""
    if created:
        date_phrase = f", dating to {created}"

    tier_phrase = ""
    if ev_tier_label:
        tier_phrase = f" Classified as {ev_tier_label} evidence (Tier {ev_tier})."
    elif ev_tier:
        tier_phrase = f" Classified as Tier {ev_tier} evidence."

    sig_phrase = ""
    if sig_score >= 7:
        sig_phrase = " It provides critical primary evidence for understanding the period."
    elif sig_score >= 4:
        sig_phrase = " It contributes valuable historical evidence."

    return f"{name} is a {type_phrase}{location}{date_phrase}.{tier_phrase}{sig_phrase}"


def enrich_timeframe_summary(entity: dict) -> str:
    """Generate a richer summary for a Timeframe entity."""
    name = entity.get("name", "")
    summary = entity.get("summary", "")
    tf_type = entity.get("timeframeType", "")
    start_date = entity.get("startDate", "")
    end_date = entity.get("endDate", "")
    continent = entity.get("continent", "")
    division = entity.get("divisionHeading", "")
    sig = entity.get("historicalSignificance", {})
    sig_score = sig.get("score", 0)

    if len(summary) > 150 and not is_hollow_summary(summary):
        return summary

    type_phrase = tf_type or division or "historical period"
    location = ""
    if continent and continent != "Global":
        location = f" primarily associated with {continent}"

    date_phrase = ""
    if start_date and end_date:
        date_phrase = f", spanning from {start_date} to {end_date}"
    elif start_date:
        date_phrase = f", beginning around {start_date}"

    sig_phrase = ""
    if sig_score >= 7:
        sig_phrase = " It represents a pivotal era that fundamentally transformed human civilization."
    elif sig_score >= 4:
        sig_phrase = " It marks a significant chapter in the development of human societies."

    return f"{name} is a {type_phrase}{location}{date_phrase}.{sig_phrase}"


# ─── v2 Attribute Enrichment ─────────────────────────────────────────────

def add_missing_v2_attributes(entity: dict) -> dict:
    """Add missing backend v2 attributes to an entity."""
    # thumbnailUrl: derive from imageUrl if available
    if "thumbnailUrl" not in entity:
        img = entity.get("imageUrl", "")
        if img and "wikimedia" in img.lower():
            # Create thumbnail URL from Wikimedia Commons
            entity["thumbnailUrl"] = img.replace("/commons/", "/commons/thumb/") + "/200px-thumbnail.jpg" if "/commons/" in img else ""
        else:
            entity["thumbnailUrl"] = ""

    # importanceScore: derive from historicalSignificance if available
    if "importanceScore" not in entity:
        sig = entity.get("historicalSignificance", {})
        entity["importanceScore"] = sig.get("score", 1)

    # altNames: empty array as placeholder
    if "altNames" not in entity:
        entity["altNames"] = []

    # externalLinks: build from wikidataQid and wikipediaUrl
    if "externalLinks" not in entity:
        links = []
        qid = entity.get("wikidataQid", "")
        wiki_url = entity.get("wikipediaUrl", "")
        if qid:
            links.append(f"https://www.wikidata.org/wiki/{qid}")
        if wiki_url:
            links.append(wiki_url)
        entity["externalLinks"] = links

    # tags: derive from subjects and frameworks
    if "tags" not in entity:
        tags = []
        for s in entity.get("subjects", [])[:5]:
            if s and len(s) < 50:
                tags.append(s)
        for fw in entity.get("frameworks", [])[:3]:
            tag = fw.lower().replace("_", "-")
            tags.append(tag)
        entity["tags"] = tags

    # quote: empty string placeholder
    if "quote" not in entity:
        entity["quote"] = ""

    # legacySummary: empty string placeholder
    if "legacySummary" not in entity:
        entity["legacySummary"] = ""

    return entity


# ─── Timeframe Cleanup ────────────────────────────────────────────────────

def classify_timeframe_entity(entity: dict) -> str:
    """
    Determine the proper JSON file for a timeframe entity.
    Returns: 'timeframes', 'institutions', 'ideas', 'movements', 'events'
    """
    subjects = entity.get("subjects", [])
    name = entity.get("name", "").lower()
    summary = (entity.get("summary", "") or "").lower()

    # Dynasties -> Institutions
    if "dynasty" in subjects or "dynasty" in name or "dynasty" in summary:
        return "institutions"

    # Architectural styles -> Ideas  
    if "architectural style" in subjects or "architecture" in name.split()[-1:]:
        return "ideas"

    # Everything else stays as timeframe (archaeological cultures, periods, etc.)
    return "timeframes"


def relabel_dynasty_as_institution(entity: dict) -> dict:
    """Convert a dynasty timeframe entity to an Institution."""
    entity["label"] = "Institution"

    # Remap call number from 9xx to 3xx (Institutions)
    old_code = entity.get("divisionCode", "")
    entity["divisionCode"] = "312"  # Monarchies & Royal Courts
    entity["divisionHeading"] = "Monarchies & Royal Courts"

    slug = entity.get("slug", "")
    entity["callNumber"] = f"312.{slug}"

    # Update subject headings
    entity["subjectHeadings"] = [
        f"Institution — Monarchies & Royal Courts — {entity.get('continent', 'Global')} — {entity.get('era', '')}"
    ]

    # Add institution-specific fields
    entity["institutionType"] = "dynasty"
    entity["isActive"] = False
    if "startDate" in entity:
        entity["founded"] = entity.pop("startDate", "")
    if "startYear" in entity:
        entity["foundedYear"] = entity.pop("startYear", "")
    if "endDate" in entity:
        entity["dissolved"] = entity.pop("endDate", "")
    if "endYear" in entity:
        entity["dissolvedYear"] = entity.pop("endYear", "")

    # Remove timeframe-specific fields
    entity.pop("timeframeType", None)

    return entity


def relabel_archstyle_as_idea(entity: dict) -> dict:
    """Convert an architectural style timeframe entity to an Idea."""
    entity["label"] = "Idea"

    slug = entity.get("slug", "")
    entity["divisionCode"] = "170"  # Artistic & Aesthetic Movements
    entity["divisionHeading"] = "Artistic & Aesthetic Movements"
    entity["callNumber"] = f"170.{slug}"

    entity["subjectHeadings"] = [
        f"Idea — Artistic & Aesthetic Movements — {entity.get('continent', 'Global')} — {entity.get('era', '')}"
    ]

    # Add idea-specific fields
    entity["ideaType"] = "architectural style"
    entity["ideaClass"] = 1
    entity["ideaClassHeading"] = "Ideas – Other Theories"
    if "startDate" in entity:
        entity["originDate"] = entity.pop("startDate", "")
    if "startYear" in entity:
        entity["originYear"] = entity.pop("startYear", "")

    # Remove timeframe-specific fields
    entity.pop("timeframeType", None)
    entity.pop("endDate", None)
    entity.pop("endYear", None)

    return entity


# ─── Main Processing ─────────────────────────────────────────────────────

def load_json(filepath: Path) -> dict:
    """Load a JSON file."""
    print(f"  Loading {filepath.name}...", end=" ", flush=True)
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    count = len(data.get("entities", []))
    print(f"{count:,} entities")
    return data


def save_json_pretty(filepath: Path, data: dict) -> None:
    """Save as pretty-printed JSON."""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    size_mb = filepath.stat().st_size / (1024 * 1024)
    print(f"  Saved {filepath.name} ({size_mb:.1f} MB)")


def process_timeframes() -> tuple[list, list, list]:
    """
    Process timeframes JSON:
    - Keep legitimate timeframes
    - Extract dynasties -> return for institutions
    - Extract architectural styles -> return for ideas
    """
    print("\n═══ Processing Timeframes ═══")
    data = load_json(DATA_DIR / "wikidata_timeframes.json")
    entities = data["entities"]

    keep_timeframes = []
    to_institutions = []
    to_ideas = []

    for e in entities:
        dest = classify_timeframe_entity(e)
        if dest == "institutions":
            to_institutions.append(relabel_dynasty_as_institution(e))
        elif dest == "ideas":
            to_ideas.append(relabel_archstyle_as_idea(e))
        else:
            keep_timeframes.append(e)

    print(f"  Kept as Timeframe: {len(keep_timeframes)}")
    print(f"  Moved to Institutions (dynasties): {len(to_institutions)}")
    print(f"  Moved to Ideas (architectural styles): {len(to_ideas)}")

    return keep_timeframes, to_institutions, to_ideas


def enrich_entities(entities: list, label: str, enricher) -> tuple[list, int]:
    """Enrich hollow summaries in a list of entities."""
    enriched_count = 0
    for e in entities:
        old_summary = e.get("summary", "")
        if is_hollow_summary(old_summary):
            new_summary = enricher(e)
            if new_summary != old_summary:
                e["summary"] = new_summary
                e["enrichedSummary"] = True
                enriched_count += 1

        # Add missing v2 attributes
        add_missing_v2_attributes(e)

    return entities, enriched_count


def split_people_json(data: dict) -> dict[str, dict]:
    """
    Split wikidata_people.json into smaller files grouped by division.
    Returns dict of filename -> data dict.
    """
    print("\n═══ Splitting People JSON ═══")
    entities = data["entities"]
    meta = data["_meta"]

    # Group entities by division group
    groups: dict[str, list] = defaultdict(list)
    ungrouped = []

    # Build reverse map: divisionCode -> group key
    code_to_group = {}
    for group_key, codes in PEOPLE_DIVISION_GROUPS.items():
        for code in codes:
            code_to_group[code] = group_key

    for e in entities:
        div_code = e.get("divisionCode", "")
        group_key = code_to_group.get(div_code, None)
        if group_key:
            groups[group_key].append(e)
        else:
            ungrouped.append(e)

    # Put ungrouped into "other"
    if ungrouped:
        groups["other"] = ungrouped

    # Check if any group is too large and needs sub-splitting
    result = {}
    for group_key, group_entities in sorted(groups.items()):
        # Estimate file size (rough: ~2KB per entity when pretty-printed)
        est_size_mb = len(group_entities) * 2.0 / 1024
        
        if est_size_mb > MAX_FILE_SIZE_MB:
            # Split further by era
            era_groups: dict[str, list] = defaultdict(list)
            for e in group_entities:
                era = e.get("era", "Unknown")
                era_groups[era].append(e)
            
            for era_key, era_entities in sorted(era_groups.items()):
                era_slug = era_key.lower().replace(" ", "-").replace("/", "-")
                filename = f"wikidata_people_{group_key}_{era_slug}"
                sub_meta = {
                    **meta,
                    "split_group": group_key,
                    "split_era": era_key,
                    "entity_count": len(era_entities),
                }
                result[filename] = {"_meta": sub_meta, "entities": era_entities}
        else:
            filename = f"wikidata_people_{group_key}"
            sub_meta = {
                **meta,
                "split_group": group_key,
                "entity_count": len(group_entities),
            }
            result[filename] = {"_meta": sub_meta, "entities": group_entities}

    print(f"  Split into {len(result)} files:")
    for fname, fdata in sorted(result.items()):
        print(f"    {fname}.json: {len(fdata['entities']):,} entities")

    return result


def main():
    print("╔═══════════════════════════════════════════════════╗")
    print("║  Wikidata JSON Enrichment & Housekeeping Script  ║")
    print("╚═══════════════════════════════════════════════════╝")

    # ── Step 1: Process timeframes (extract dynasties & arch styles) ──
    timeframe_entities, dynasty_entities, archstyle_entities = process_timeframes()

    # ── Step 2: Load all other JSON files ──
    print("\n═══ Loading JSON Files ═══")
    files = {
        "artifacts": load_json(DATA_DIR / "wikidata_artifacts.json"),
        "events": load_json(DATA_DIR / "wikidata_events.json"),
        "evidence": load_json(DATA_DIR / "wikidata_evidence.json"),
        "ideas": load_json(DATA_DIR / "wikidata_ideas.json"),
        "institutions": load_json(DATA_DIR / "wikidata_institutions.json"),
        "movements": load_json(DATA_DIR / "wikidata_movements.json"),
        "places": load_json(DATA_DIR / "wikidata_places.json"),
        "people": load_json(DATA_DIR / "wikidata_people.json"),
    }

    # ── Step 3: Merge timeframe extractions ──
    print("\n═══ Merging Timeframe Extractions ═══")
    
    # Add dynasties to institutions
    existing_inst_slugs = {e["slug"] for e in files["institutions"]["entities"]}
    new_dynasties = [e for e in dynasty_entities if e["slug"] not in existing_inst_slugs]
    files["institutions"]["entities"].extend(new_dynasties)
    print(f"  Added {len(new_dynasties)} dynasty entities to institutions (skipped {len(dynasty_entities) - len(new_dynasties)} duplicates)")

    # Add architectural styles to ideas
    existing_idea_slugs = {e["slug"] for e in files["ideas"]["entities"]}
    new_archstyles = [e for e in archstyle_entities if e["slug"] not in existing_idea_slugs]
    files["ideas"]["entities"].extend(new_archstyles)
    print(f"  Added {len(new_archstyles)} architectural style entities to ideas (skipped {len(archstyle_entities) - len(new_archstyles)} duplicates)")

    # ── Step 4: Enrich summaries across all files ──
    print("\n═══ Enriching Summaries ═══")

    enrichers = {
        "artifacts": ("Text", enrich_artifact_summary),
        "events": ("EventWindow", enrich_event_summary),
        "evidence": ("Evidence", enrich_evidence_summary),
        "ideas": ("Idea", enrich_idea_summary),
        "institutions": ("Institution", enrich_institution_summary),
        "movements": ("Movement", enrich_movement_summary),
        "places": ("Place", enrich_place_summary),
        "people": ("Person", enrich_person_summary),
    }

    total_enriched = 0
    for key, (label, enricher) in enrichers.items():
        entities = files[key]["entities"]
        entities, count = enrich_entities(entities, label, enricher)
        files[key]["entities"] = entities
        total_enriched += count
        print(f"  {key}: enriched {count:,} / {len(entities):,} summaries")

    # Enrich timeframes too
    timeframe_enriched = 0
    for e in timeframe_entities:
        old = e.get("summary", "")
        if is_hollow_summary(old):
            e["summary"] = enrich_timeframe_summary(e)
            e["enrichedSummary"] = True
            timeframe_enriched += 1
        add_missing_v2_attributes(e)
    total_enriched += timeframe_enriched
    print(f"  timeframes: enriched {timeframe_enriched:,} / {len(timeframe_entities):,} summaries")

    print(f"\n  Total summaries enriched: {total_enriched:,}")

    # ── Step 5: Save timeframes (cleaned) ──
    print("\n═══ Saving Cleaned Timeframes ═══")
    tf_meta = load_json(DATA_DIR / "wikidata_timeframes.json")["_meta"]
    tf_meta["entity_count"] = len(timeframe_entities)
    tf_meta["note"] = (
        f"Cleaned timeframes. Removed {len(dynasty_entities)} dynasties "
        f"(moved to institutions) and {len(archstyle_entities)} architectural "
        f"styles (moved to ideas). {len(timeframe_entities)} legitimate "
        "timeframes remain."
    )
    save_json_pretty(
        OUTPUT_DIR / "wikidata_timeframes.json",
        {"_meta": tf_meta, "entities": timeframe_entities},
    )

    # ── Step 6: Save all enriched non-people files ──
    print("\n═══ Saving Enriched Files ═══")
    for key in ["artifacts", "events", "evidence", "ideas", "institutions", "movements", "places"]:
        data = files[key]
        # Update meta
        if "_meta" in data:
            data["_meta"]["enrichment_note"] = (
                f"Enriched with v2 attributes and improved summaries. "
                f"Generated by enrich_wikidata.py."
            )
            data["_meta"]["entity_count"] = len(data["entities"])
        save_json_pretty(OUTPUT_DIR / f"wikidata_{key}.json", data)

    # ── Step 7: Split people JSON ──
    print("\n═══ Splitting People JSON ═══")
    people_data = files["people"]

    # Update meta
    if "_meta" in people_data:
        people_data["_meta"]["enrichment_note"] = (
            "Enriched with v2 attributes and improved summaries. "
            "Split into division-based files for GitHub upload."
        )

    split_files = split_people_json(people_data)

    # Create people directory
    PEOPLE_SPLIT_DIR.mkdir(exist_ok=True)

    for filename, fdata in sorted(split_files.items()):
        save_json_pretty(PEOPLE_SPLIT_DIR / f"{filename}.json", fdata)

    # Save a manifest/index file for the people directory
    manifest = {
        "_meta": {
            "description": "Index of split people JSON files by division group",
            "total_entities": len(people_data["entities"]),
            "total_files": len(split_files),
            "generated_by": "enrich_wikidata.py",
        },
        "files": {
            fname: {
                "entity_count": len(fdata["entities"]),
                "group": fdata["_meta"].get("split_group", ""),
                "era": fdata["_meta"].get("split_era", ""),
            }
            for fname, fdata in sorted(split_files.items())
        },
    }
    save_json_pretty(PEOPLE_SPLIT_DIR / "_manifest.json", manifest)

    # Also save the full people file pretty-printed (for backward compat)
    print("\n  Also saving full wikidata_people.json (pretty-printed)...")
    save_json_pretty(OUTPUT_DIR / "wikidata_people.json", people_data)

    # ── Step 8: Summary Report ──
    print("\n╔═══════════════════════════════════════════════════╗")
    print("║                 ENRICHMENT REPORT                ║")
    print("╠═══════════════════════════════════════════════════╣")
    print(f"║  Total summaries enriched:     {total_enriched:>10,}        ║")
    print(f"║  Dynasties → Institutions:     {len(dynasty_entities):>10,}        ║")
    print(f"║  Arch styles → Ideas:          {len(archstyle_entities):>10,}        ║")
    print(f"║  People split files:           {len(split_files):>10,}        ║")
    print(f"║  All JSON files pretty-printed               ✓  ║")
    print(f"║  v2 attributes added                         ✓  ║")
    print("╚═══════════════════════════════════════════════════╝")


if __name__ == "__main__":
    main()
