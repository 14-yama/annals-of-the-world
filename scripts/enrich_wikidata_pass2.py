#!/usr/bin/env python3
"""
Second-pass enrichment for remaining hollow summaries.
Catches patterns that slipped through the first pass.
"""

import json
import re
import sys
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def is_still_hollow(s: str) -> bool:
    """More aggressive hollow detection."""
    if not s or len(s.strip()) < 40:
        return True
    s = s.strip()
    patterns = [
        r"Associated with\s+\w+",
        r"is a [a-z ]{1,40} based in \w+",
        r"is a [a-z ]{1,40} from \w+\.",
        r"is a [a-z ]{1,40} in \w+\.",
        r"is a [a-z ]{1,40}, dating to",
        r"is a [a-z ]{1,40}\.$",
        r"Active during the \w+ era\.$",
        r"originating in [a-z ]+\.",
        r"^[A-Z].{5,40} in [a-z]+, [a-z ]+ (Headquartered|Founded|Active)",
        r"^[A-Z].{5,40} Headquartered in \w+\. Founded \d+\.$",
    ]
    for p in patterns:
        if re.search(p, s, re.IGNORECASE):
            return True
    return False


def enrich_v2(entity: dict) -> str:
    """More aggressive enrichment using all available data."""
    name = entity.get("name", "")
    label = entity.get("label", "")
    summary = entity.get("summary", "")
    era = entity.get("era", "")
    continent = entity.get("continent", "")
    region = entity.get("region", "")
    division = entity.get("divisionHeading", "")
    sig = entity.get("historicalSignificance", {})
    sig_score = sig.get("score", 0)
    sig_label = sig.get("label", "")
    sitelinks = sig.get("sitelinks", 0)
    frameworks = entity.get("frameworks", [])
    subjects = entity.get("subjects", [])
    causes = entity.get("causes", [])
    effects = entity.get("effects", [])
    places = entity.get("places", [])

    # Extract useful info from existing summary
    existing_info = ""
    if summary:
        # Remove template parts, keep any real content
        cleaned = re.sub(
            r"(Associated with|Based in|From|Headquartered in|Active during the|Dating to|Founded|Born in|Occurred in)[^.]*\.",
            "",
            summary,
        ).strip()
        if cleaned and len(cleaned) > 10 and cleaned != name:
            existing_info = cleaned.rstrip(".")

    # Type-specific enrichment
    type_specific = ""
    if label == "Institution":
        inst_type = entity.get("institutionType", "") or division or "institution"
        hq = entity.get("headquarters", "")
        founded = entity.get("founded", "") or entity.get("foundedYear", "")
        loc = f" in {hq}" if hq else (f" in {continent}" if continent != "Global" else "")
        date = f", established in {founded}" if founded else ""
        type_specific = f"{name} is a {inst_type}{loc}{date}."

    elif label == "Movement":
        mov_type = entity.get("movementType", "") or division or "movement"
        # Fix the "originating in X organization" bug
        if mov_type and mov_type == summary.lower().split("originating in ")[-1].rstrip(". "):
            mov_type = division or "social and cultural movement"
        start = entity.get("startYear", "")
        loc = f" that emerged in {continent}" if continent != "Global" else ""
        date = f" around {start}" if start else ""
        type_specific = f"{name} was a {mov_type}{loc}{date}."

    elif label == "Text" or label == "Artifact":
        art_type = entity.get("artifactType", "") or division or "text"
        created = entity.get("created", "") or entity.get("createdYear", "")
        creator = entity.get("creator", "")
        loc = f" from {continent}" if continent != "Global" else ""
        date = f", created circa {created}" if created else ""
        author = f" by {creator}" if creator else ""
        type_specific = f"{name} is a {art_type}{loc}{author}{date}."

    elif label == "Evidence":
        ev_type = entity.get("evidenceType", "") or "evidence source"
        ev_tier = entity.get("evidenceTier", "")
        tier_label = entity.get("evidenceTierLabel", "")
        loc = f" from {continent}" if continent != "Global" else ""
        tier = f" Classified as Tier {ev_tier} ({tier_label}) evidence." if ev_tier else ""
        type_specific = f"{name} is a {ev_type}{loc}.{tier}"

    elif label == "Idea":
        idea_type = entity.get("ideaType", "") or division or "concept"
        origin = entity.get("originDate", "") or entity.get("originYear", "")
        founder = entity.get("founder", "")
        loc = f" with roots in {continent}" if continent != "Global" else ""
        date = f", arising around {origin}" if origin else ""
        auth = f" Attributed to {founder}." if founder else ""
        type_specific = f"{name} is a {idea_type}{loc}{date}.{auth}"

    elif label == "Place":
        place_type = entity.get("placeType", "") or division or "location"
        founded = entity.get("founded", "")
        pop = entity.get("population", "")
        loc = f" in {region}" if region and region != "Global" else (f" in {continent}" if continent != "Global" else "")
        date = f", established around {founded}" if founded else ""
        type_specific = f"{name} is a {place_type}{loc}{date}."

    elif label == "EventWindow":
        ev_type = entity.get("eventType", "") or division or "event"
        start = entity.get("startYear", "")
        end = entity.get("endYear", "")
        loc = f" in {continent}" if continent != "Global" else ""
        date = ""
        if start and end:
            date = f" ({start}–{end})"
        elif start:
            date = f" ({start})"
        type_specific = f"{name} was a {ev_type}{loc}{date}."

    elif label == "Timeframe":
        tf_type = entity.get("timeframeType", "") or "historical period"
        start = entity.get("startDate", "") or entity.get("startYear", "")
        end = entity.get("endDate", "") or entity.get("endYear", "")
        loc = f" associated with {continent}" if continent != "Global" else ""
        date = ""
        if start and end:
            date = f", spanning {start} to {end}"
        elif start:
            date = f", beginning around {start}"
        type_specific = f"{name} is a {tf_type}{loc}{date}."

    elif label == "Person":
        div = division or "historical figure"
        born = entity.get("born", "")
        died = entity.get("died", "")
        loc = ""
        if places:
            pn = [p.get("name", "") for p in places if p.get("name")]
            if pn:
                loc = f" from {pn[0]}"
        elif continent != "Global":
            loc = f" from {continent}"
        date = ""
        if born and died:
            date = f" ({born}–{died})"
        elif born:
            date = f" (b. {born})"
        type_specific = f"{name} was a {div.lower()}{loc}{date}."

    else:
        type_specific = f"{name} is a historical entity from the {era} era."

    # Build significance context
    sig_context = ""
    if sig_score >= 8:
        sig_context = f" Recognized as a landmark figure with global significance (referenced in {sitelinks} Wikipedia editions)."
    elif sig_score >= 6:
        sig_context = f" Holds notable historical significance, documented across {sitelinks} language editions of Wikipedia."
    elif sig_score >= 4:
        sig_context = f" A moderately significant entity in the historical record."

    # Build framework context
    fw_context = ""
    fw_map = {
        "CAUSE_AND_EFFECT": "cause-and-effect analysis",
        "POLITICAL_SYSTEMS": "political systems",
        "EMPIRE_AND_COLONIALISM": "imperial and colonial studies",
        "MILITARY_STRATEGY": "military history",
        "ECONOMIC_SYSTEMS": "economic history",
        "RELIGIOUS_AND_THEOLOGICAL": "religious history",
        "SCIENTIFIC_REVOLUTION": "the history of science",
        "CULTURAL_EXCHANGE": "cultural exchange",
        "SOCIAL_MOVEMENTS": "social movement theory",
        "TECHNOLOGICAL_CHANGE": "technology and innovation",
        "ENVIRONMENTAL_HISTORY": "environmental history",
        "GENDER_AND_POWER": "gender studies",
        "GEOPOLITICAL_LINKAGE": "geopolitics",
        "LEGAL_EVOLUTION": "legal history",
        "INTELLECTUAL_HISTORY": "intellectual history",
        "DEMOGRAPHIC_SHIFTS": "demographic studies",
    }
    fw_names = [fw_map.get(fw, "") for fw in frameworks[:2] if fw in fw_map]
    if fw_names:
        fw_context = f" Relevant to {' and '.join(fw_names)}."

    # Build effects/legacy
    legacy = ""
    if effects:
        eff_titles = [e.get("title", "") for e in effects[:1] if isinstance(e, dict) and e.get("title")]
        if eff_titles:
            legacy = f" Its legacy: {eff_titles[0].rstrip('.')}."

    # Assemble
    parts = []
    if existing_info and existing_info != name:
        parts.append(existing_info + ".")
    parts.append(type_specific)
    if sig_context:
        parts.append(sig_context)
    if fw_context:
        parts.append(fw_context)
    if legacy and len(" ".join(parts)) < 300:
        parts.append(legacy)

    result = " ".join(parts).replace("  ", " ").replace("..", ".")
    return result


def process_file(filepath: Path) -> int:
    """Process a single JSON file, enriching hollow summaries."""
    print(f"  Processing {filepath.name}...", end=" ", flush=True)
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    entities = data["entities"]
    enriched = 0
    for e in entities:
        old = e.get("summary", "")
        if is_still_hollow(old):
            new_summary = enrich_v2(e)
            if new_summary and new_summary != old and len(new_summary) > len(old):
                e["summary"] = new_summary
                e["enrichedSummary"] = True
                enriched += 1

    if enriched > 0:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"{enriched} enriched")
    return enriched


def main():
    print("═══ Second-Pass Enrichment ═══\n")

    # All JSON files to process
    files = sorted(DATA_DIR.glob("wikidata_*.json"))
    # Also process people split files
    people_dir = DATA_DIR / "people"
    if people_dir.exists():
        files.extend(sorted(people_dir.glob("wikidata_people_*.json")))

    total = 0
    for fp in files:
        total += process_file(fp)

    print(f"\n  Total second-pass enrichments: {total:,}")


if __name__ == "__main__":
    main()
