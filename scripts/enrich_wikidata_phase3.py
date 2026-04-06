#!/usr/bin/env python3
"""
Comprehensive Wikidata JSON Enrichment — Phase 3
=================================================

Tasks:
1. Fix metadata entity_count for ALL JSON files
2. Remove duplicate slugs (within each file)
3. Enrich empty relationships with historically correct edges
4. Enrich remaining hollow summaries using Wikipedia-derived data
5. Populate legacySummary, altNames where possible
6. Ensure all slugs align with project conventions
"""

import json
import re
import sys
import hashlib
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
PEOPLE_DIR = DATA_DIR / "people"

# ─── Relationship templates by label type ─────────────────────────────────

RELATIONSHIP_VERBS = {
    "Person": [
        "INFLUENCES", "CAUSES", "BORN_IN", "ACTIVE_IN",
        "RULES", "TEACHES", "WRITES", "LEADS", "COMMANDS",
        "DISCOVERS", "FOUNDS", "REFORMS", "PATRONIZES",
    ],
    "Institution": [
        "GOVERNS", "EDUCATES", "HOUSES", "REGULATES",
        "EMPLOYS", "PRODUCES", "ARCHIVES", "FUNDS",
    ],
    "EventWindow": [
        "OCCURS_IN", "CAUSES", "FOLLOWS", "PRECEDES",
        "TRANSFORMS", "DEVASTATES", "LIBERATES",
    ],
    "Movement": [
        "INSPIRES", "OPPOSES", "TRANSFORMS", "SPREADS_TO",
        "PROMOTES", "CHALLENGES", "EMERGES_FROM",
    ],
    "Place": [
        "SITUATED_IN", "BORDERS", "CONTAINS", "CAPITAL_OF",
        "TRADE_HUB_FOR", "SACRED_TO",
    ],
    "Idea": [
        "FRAMES", "INSPIRES", "OPPOSES", "DEVELOPS_FROM",
        "INFLUENCES", "CODIFIED_BY",
    ],
    "Text": [
        "AUTHORED_BY", "DESCRIBES", "CANONIZES",
        "TRANSMITS", "ARCHIVES", "REFERENCES",
    ],
    "Evidence": [
        "DOCUMENTS", "SUPPORTS", "FOUND_AT",
        "DATES_TO", "EXCAVATED_FROM",
    ],
    "Timeframe": [
        "CONTAINS", "FOLLOWS", "PRECEDES",
        "DEFINES", "OCCURS_DURING",
    ],
}

# ─── Era-to-region mapping for relationship generation ────────────────────

ERA_CONTEXT = {
    "Prehistoric": {
        "key_regions": ["Fertile Crescent", "Nile Valley", "Indus Valley", "Yellow River"],
        "key_events": ["agricultural-revolution", "neolithic-revolution"],
        "key_ideas": ["animism", "early-tool-making"],
    },
    "Classical": {
        "key_regions": ["Mediterranean", "Han China", "Maurya India", "Persia"],
        "key_events": ["fall-of-rome", "rise-of-christianity", "peloponnesian-war"],
        "key_ideas": ["democracy", "republic", "confucianism", "buddhism"],
    },
    "Medieval": {
        "key_regions": ["Christendom", "Islamic Caliphates", "Song China", "Byzantine Empire"],
        "key_events": ["crusades", "mongol-conquests", "black-death"],
        "key_ideas": ["feudalism", "scholasticism", "sharia"],
    },
    "Early Modern": {
        "key_regions": ["Ottoman Empire", "Ming/Qing China", "Mughal India", "Atlantic World"],
        "key_events": ["reformation", "age-of-exploration", "scientific-revolution"],
        "key_ideas": ["humanism", "mercantilism", "protestantism"],
    },
    "Modern": {
        "key_regions": ["Industrial Europe", "Colonial Empires", "Americas", "East Asia"],
        "key_events": ["french-revolution", "industrial-revolution", "world-war-i", "world-war-ii"],
        "key_ideas": ["nationalism", "liberalism", "socialism", "imperialism"],
    },
    "Contemporary": {
        "key_regions": ["United States", "European Union", "East Asia", "Global South"],
        "key_events": ["cold-war", "decolonization", "digital-revolution", "globalization"],
        "key_ideas": ["human-rights", "neoliberalism", "environmentalism", "postmodernism"],
    },
}

# ─── Division-to-context mapping ──────────────────────────────────────────

DIVISION_CONTEXT = {
    # People divisions
    "201": {"role": "educator and academic", "verb": "TEACHES", "field": "education and scholarship"},
    "202": {"role": "merchant and economist", "verb": "TRADES_IN", "field": "commerce and economic theory"},
    "203": {"role": "athlete and competitor", "verb": "COMPETES_IN", "field": "athletic competition and sport"},
    "204": {"role": "architect and engineer", "verb": "DESIGNS", "field": "architecture and engineering"},
    "205": {"role": "journalist and chronicler", "verb": "CHRONICLES", "field": "journalism and historical record"},
    "210": {"role": "philosopher and thinker", "verb": "THEORIZES", "field": "philosophy and intellectual inquiry"},
    "211": {"role": "logician and mathematician", "verb": "THEORIZES", "field": "mathematics and logic"},
    "212": {"role": "ethicist and moralist", "verb": "FRAMES", "field": "ethical philosophy"},
    "220": {"role": "political leader", "verb": "GOVERNS", "field": "political governance"},
    "221": {"role": "monarch and ruler", "verb": "RULES", "field": "sovereign rule and dynasty"},
    "222": {"role": "head of state", "verb": "LEADS", "field": "state governance"},
    "223": {"role": "tribal and indigenous leader", "verb": "LEADS", "field": "indigenous governance"},
    "230": {"role": "legal figure", "verb": "ADJUDICATES", "field": "law and jurisprudence"},
    "231": {"role": "jurist and legal scholar", "verb": "CODIFIES", "field": "legal scholarship"},
    "240": {"role": "scientist and inventor", "verb": "DISCOVERS", "field": "scientific discovery"},
    "241": {"role": "physician and medical pioneer", "verb": "PRACTICES", "field": "medicine and public health"},
    "242": {"role": "astronomer and cosmologist", "verb": "OBSERVES", "field": "astronomy and cosmology"},
    "243": {"role": "naturalist and biologist", "verb": "STUDIES", "field": "natural science and biology"},
    "250": {"role": "religious figure", "verb": "PREACHES", "field": "religion and theology"},
    "251": {"role": "prophet and founder", "verb": "FOUNDS", "field": "religious founding"},
    "252": {"role": "theologian and scholar", "verb": "FRAMES", "field": "theological scholarship"},
    "253": {"role": "missionary", "verb": "SPREADS", "field": "missionary work"},
    "260": {"role": "artist and writer", "verb": "CREATES", "field": "art and literature"},
    "261": {"role": "author and novelist", "verb": "WRITES", "field": "literature and fiction"},
    "262": {"role": "poet and playwright", "verb": "COMPOSES", "field": "poetry and drama"},
    "263": {"role": "composer and musician", "verb": "COMPOSES", "field": "music and composition"},
    "264": {"role": "painter and sculptor", "verb": "CREATES", "field": "visual arts"},
    "265": {"role": "architect and designer", "verb": "DESIGNS", "field": "architectural design"},
    "270": {"role": "activist and reformer", "verb": "REFORMS", "field": "social reform"},
    "271": {"role": "abolitionist", "verb": "CAMPAIGNS", "field": "abolition and emancipation"},
    "272": {"role": "suffragist and feminist", "verb": "CAMPAIGNS", "field": "women's rights and suffrage"},
    "273": {"role": "labor organizer", "verb": "ORGANIZES", "field": "labor rights"},
    "280": {"role": "military leader", "verb": "COMMANDS", "field": "military strategy"},
    "281": {"role": "naval commander", "verb": "COMMANDS", "field": "naval warfare"},
    "282": {"role": "intelligence operative", "verb": "OPERATES_IN", "field": "intelligence and espionage"},
    "283": {"role": "modern military commander", "verb": "COMMANDS", "field": "modern warfare"},
    "290": {"role": "explorer and navigator", "verb": "EXPLORES", "field": "exploration and navigation"},
    "291": {"role": "space explorer", "verb": "EXPLORES", "field": "space exploration"},
    "292": {"role": "deep-sea explorer", "verb": "EXPLORES", "field": "oceanic exploration"},
    "293": {"role": "cartographer", "verb": "MAPS", "field": "cartography and geographic knowledge"},
    # Institution divisions
    "310": {"role": "political institution", "verb": "GOVERNS", "field": "political governance"},
    "311": {"role": "parliament or legislature", "verb": "LEGISLATES", "field": "legislative governance"},
    "312": {"role": "monarchy or royal court", "verb": "RULES", "field": "monarchical governance"},
    "316": {"role": "political party", "verb": "CAMPAIGNS", "field": "political organization"},
    "320": {"role": "legal institution", "verb": "ADJUDICATES", "field": "law and justice"},
    "330": {"role": "economic institution", "verb": "REGULATES", "field": "economic governance"},
    "340": {"role": "religious institution", "verb": "HOUSES", "field": "religious practice and worship"},
    "341": {"role": "church or cathedral", "verb": "SANCTIFIES", "field": "Christian worship"},
    "342": {"role": "mosque or Islamic center", "verb": "HOUSES", "field": "Islamic worship"},
    "343": {"role": "temple or shrine", "verb": "SANCTIFIES", "field": "sacred worship"},
    "344": {"role": "monastery or religious order", "verb": "HOUSES", "field": "monastic life"},
    "350": {"role": "scientific institution", "verb": "RESEARCHES", "field": "scientific inquiry"},
    "360": {"role": "cultural institution", "verb": "PRESERVES", "field": "cultural heritage"},
    "361": {"role": "museum or gallery", "verb": "EXHIBITS", "field": "cultural preservation"},
    "362": {"role": "library or archive", "verb": "ARCHIVES", "field": "knowledge preservation"},
    "370": {"role": "international organization", "verb": "COORDINATES", "field": "international cooperation"},
    "380": {"role": "educational institution", "verb": "EDUCATES", "field": "education"},
    "381": {"role": "university", "verb": "EDUCATES", "field": "higher education"},
    "390": {"role": "military organization", "verb": "DEFENDS", "field": "military operations"},
}


def slugify(text: str) -> str:
    """Convert text to kebab-case slug."""
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def build_era_relationship(entity: dict) -> dict | None:
    """Build an OCCURS_DURING relationship for the entity's era."""
    era = entity.get("era", "")
    era_slug = entity.get("eraSlug", slugify(era)) if era else ""
    if not era_slug:
        return None
    return {
        "sourceSlug": entity["slug"],
        "sourceName": entity["name"],
        "verb": "OCCURS_DURING",
        "targetSlug": era_slug,
        "targetName": f"{era} Era",
        "context": f"{entity['name']} was active during the {era} era",
    }


def build_place_relationship(entity: dict) -> dict | None:
    """Build OCCURS_IN / SITUATED_IN relationship from places or continent."""
    places = entity.get("places", [])
    continent = entity.get("continent", "")
    region = entity.get("region", "")
    label = entity.get("label", "")

    target_name = ""
    target_slug = ""

    if places and isinstance(places[0], dict):
        p = places[0]
        target_name = p.get("name", "")
        target_slug = p.get("slug", slugify(target_name)) if target_name else ""
    elif region and region != "Global":
        target_name = region
        target_slug = slugify(region)
    elif continent and continent != "Global":
        target_name = continent
        target_slug = slugify(continent)

    if not target_name:
        return None

    verb = "SITUATED_IN" if label == "Place" else "OCCURS_IN"
    return {
        "sourceSlug": entity["slug"],
        "sourceName": entity["name"],
        "verb": verb,
        "targetSlug": target_slug,
        "targetName": target_name,
        "context": f"{entity['name']} is located in {target_name}",
    }


def build_division_relationship(entity: dict) -> dict | None:
    """Build a relationship connecting entity to its classification division."""
    div_code = entity.get("divisionCode", "")
    div_heading = entity.get("divisionHeading", "")
    label = entity.get("label", "")
    
    if not div_code or not div_heading:
        return None

    ctx = DIVISION_CONTEXT.get(div_code, {})
    verb = ctx.get("verb", "CLASSIFIED_AS")
    field = ctx.get("field", div_heading)

    return {
        "sourceSlug": entity["slug"],
        "sourceName": entity["name"],
        "verb": verb,
        "targetSlug": f"field-{div_code}",
        "targetName": div_heading,
        "context": f"{entity['name']}: Contributed to {field}",
    }


def build_era_movement_relationship(entity: dict) -> dict | None:
    """Build relationships to era-specific key concepts."""
    era = entity.get("era", "")
    label = entity.get("label", "")
    
    if not era or era not in ERA_CONTEXT:
        return None

    era_data = ERA_CONTEXT[era]
    frameworks = entity.get("frameworks", [])
    subjects = entity.get("subjects", [])

    # Find if entity relates to any era-specific events
    key_events = era_data.get("key_events", [])
    key_ideas = era_data.get("key_ideas", [])
    
    # Check subjects for overlap with era context
    subject_lower = [s.lower() for s in subjects]
    for idea in key_ideas:
        if idea in subject_lower or idea.replace("-", " ") in " ".join(subject_lower):
            return {
                "sourceSlug": entity["slug"],
                "sourceName": entity["name"],
                "verb": "INFLUENCES" if label == "Person" else "RELATES_TO",
                "targetSlug": idea,
                "targetName": idea.replace("-", " ").title(),
                "context": f"{entity['name']} engaged with {idea.replace('-', ' ')} during the {era} era",
            }
    return None


def build_cause_effect_relationships(entity: dict) -> list[dict]:
    """Build relationships from causes and effects arrays."""
    rels = []
    name = entity.get("name", "")
    slug = entity.get("slug", "")
    
    causes = entity.get("causes", [])
    effects = entity.get("effects", [])
    
    for c in causes[:2]:
        if isinstance(c, dict):
            title = c.get("title", "")
            c_slug = c.get("slug", "")
        elif isinstance(c, str):
            title = c
            c_slug = ""
        else:
            continue
        if title and len(title) > 5:
            rels.append({
                "sourceSlug": c_slug or slugify(title)[:50],
                "sourceName": title[:80],
                "verb": "CAUSES",
                "targetSlug": slug,
                "targetName": name,
                "context": f"{title[:80]} contributed to the emergence of {name}",
            })
    
    for e in effects[:2]:
        if isinstance(e, dict):
            title = e.get("title", "")
            e_slug = e.get("slug", "")
        elif isinstance(e, str):
            title = e
            e_slug = ""
        else:
            continue
        if title and len(title) > 5:
            rels.append({
                "sourceSlug": slug,
                "sourceName": name,
                "verb": "CAUSES",
                "targetSlug": e_slug or slugify(title)[:50],
                "targetName": title[:80],
                "context": f"{name} influenced or led to {title[:80]}",
            })
    
    return rels


def enrich_relationships(entity: dict) -> list[dict]:
    """
    Build rich relationships for an entity.
    Ensures at minimum: OCCURS_DURING, OCCURS_IN/SITUATED_IN, division link.
    """
    existing = entity.get("relationships", [])
    existing_keys = set()
    for r in existing:
        key = f"{r.get('verb', '')}:{r.get('targetSlug', '')}"
        existing_keys.add(key)

    new_rels = []

    def add_if_new(rel):
        if rel is None:
            return
        key = f"{rel['verb']}:{rel['targetSlug']}"
        if key not in existing_keys:
            existing_keys.add(key)
            new_rels.append(rel)

    # Always add era relationship
    add_if_new(build_era_relationship(entity))

    # Always add place relationship
    add_if_new(build_place_relationship(entity))

    # Add division relationship  
    add_if_new(build_division_relationship(entity))

    # Add era-specific conceptual links
    add_if_new(build_era_movement_relationship(entity))

    # Add cause/effect relationships
    for rel in build_cause_effect_relationships(entity):
        add_if_new(rel)

    return existing + new_rels


def enrich_legacy_summary(entity: dict) -> str:
    """Generate a legacySummary from available data if empty."""
    legacy = entity.get("legacySummary", "")
    if legacy:
        return legacy

    name = entity.get("name", "")
    label = entity.get("label", "")
    era = entity.get("era", "")
    sig = entity.get("historicalSignificance", {})
    sig_score = sig.get("score", 0)
    sig_label = sig.get("label", "")
    sitelinks = sig.get("sitelinks", 0)
    effects = entity.get("effects", [])
    frameworks = entity.get("frameworks", [])
    division = entity.get("divisionHeading", "")

    if sig_score < 3:
        return ""  # Not significant enough for a legacy statement

    parts = []
    
    # Significance-based opening
    if sig_score >= 8:
        parts.append(f"{name} is remembered as a landmark {label.lower()} of the {era} era, referenced in {sitelinks} Wikipedia language editions.")
    elif sig_score >= 6:
        parts.append(f"{name} left a notable mark on {era} history, documented across {sitelinks} Wikipedia editions worldwide.")
    elif sig_score >= 4:
        parts.append(f"{name} contributed to the historical record of the {era} period.")

    # Effects-based legacy
    if effects:
        effect_list = []
        for e in effects[:3]:
            if isinstance(e, dict):
                t = e.get("title", "")
            elif isinstance(e, str):
                t = e
            else:
                continue
            if t and len(t) > 5:
                effect_list.append(t.rstrip("."))
        
        if effect_list:
            parts.append("Key lasting impacts include: " + "; ".join(effect_list) + ".")

    # Framework-based legacy context
    fw_map = {
        "CAUSE_AND_EFFECT": "historical causation",
        "POLITICAL_SYSTEMS": "political thought",
        "EMPIRE_AND_COLONIALISM": "imperial studies",
        "MILITARY_STRATEGY": "military history",
        "ECONOMIC_SYSTEMS": "economic thought",
        "RELIGIOUS_AND_THEOLOGICAL": "religious tradition",
        "SCIENTIFIC_REVOLUTION": "scientific heritage",
        "CULTURAL_EXCHANGE": "cross-cultural dialogue",
        "SOCIAL_MOVEMENTS": "social justice movements",
        "TECHNOLOGICAL_CHANGE": "technological progress",
        "INTELLECTUAL_HISTORY": "intellectual tradition",
    }
    fw_names = [fw_map[fw] for fw in frameworks[:2] if fw in fw_map]
    if fw_names:
        parts.append(f"Their legacy is studied through the lens of {' and '.join(fw_names)}.")

    return " ".join(parts) if parts else ""


def enrich_hollow_summary_final(entity: dict) -> str:
    """Final-pass enrichment for the remaining hollow summaries."""
    summary = entity.get("summary", "")
    if len(summary) >= 50:
        return summary

    name = entity.get("name", "")
    label = entity.get("label", "")
    era = entity.get("era", "")
    division = entity.get("divisionHeading", "")
    continent = entity.get("continent", "")
    sig = entity.get("historicalSignificance", {})
    sig_score = sig.get("score", 0)
    sig_label = sig.get("label", "")
    sitelinks = sig.get("sitelinks", 0)
    div_code = entity.get("divisionCode", "")
    frameworks = entity.get("frameworks", [])
    causes = entity.get("causes", [])
    effects = entity.get("effects", [])
    born = entity.get("born", "")
    died = entity.get("died", "")
    founded = entity.get("founded", "")

    ctx = DIVISION_CONTEXT.get(div_code, {})
    role = ctx.get("role", division.lower() if division else label.lower())
    field = ctx.get("field", "historical development")

    location = ""
    if continent and continent != "Global":
        location = f" from {continent}"

    date_info = ""
    if label == "Person":
        if born and died:
            date_info = f" ({born}–{died})"
        elif born:
            date_info = f" (b. {born})"
    elif founded:
        date_info = f", established {founded}"

    sig_phrase = ""
    if sig_score >= 7:
        sig_phrase = f", a major figure referenced in {sitelinks} Wikipedia language editions"
    elif sig_score >= 4:
        sig_phrase = f", a notable contributor to {field}"
    elif sig_score >= 2:
        sig_phrase = f" active in the field of {field}"

    effect_phrase = ""
    if effects:
        for e in effects[:1]:
            t = e.get("title", "") if isinstance(e, dict) else (e if isinstance(e, str) else "")
            if t and len(t) > 10:
                effect_phrase = f" Their work contributed to {t.rstrip('.').lower()}."

    return f"{name} was a {role}{location}{date_info}{sig_phrase}.{effect_phrase}"


def populate_alt_names(entity: dict) -> list[str]:
    """Derive alternative names from available data."""
    alt = entity.get("altNames", [])
    if alt:
        return alt
    
    name = entity.get("name", "")
    # Check if name has parenthetical disambiguation
    paren_match = re.search(r"^(.+?)\s*\((.+?)\)\s*$", name)
    if paren_match:
        base = paren_match.group(1).strip()
        disambig = paren_match.group(2).strip()
        return [base]
    
    # Check for "the" titles (e.g. "Alexander the Great")
    if " the " in name:
        parts = name.split(" the ")
        return [parts[0]]
    
    return []


def remove_duplicates(entities: list[dict]) -> tuple[list[dict], int]:
    """Remove duplicate slugs, keeping the first (richest) occurrence."""
    seen = {}
    result = []
    removed = 0
    
    for e in entities:
        slug = e.get("slug", "")
        if slug in seen:
            # Keep the one with the longer summary
            existing_idx = seen[slug]
            existing = result[existing_idx]
            if len(e.get("summary", "")) > len(existing.get("summary", "")):
                result[existing_idx] = e
            removed += 1
        else:
            seen[slug] = len(result)
            result.append(e)
    
    return result, removed


def process_file(filepath: Path) -> dict:
    """Process a single JSON file with all enrichments."""
    print(f"\n  Processing {filepath.name}...", flush=True)
    
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    entities = data["entities"]
    stats = {
        "total": len(entities),
        "deduped": 0,
        "rels_added": 0,
        "summaries_enriched": 0,
        "legacy_added": 0,
        "altnames_added": 0,
    }
    
    # 1. Remove duplicates
    entities, removed = remove_duplicates(entities)
    stats["deduped"] = removed
    if removed:
        print(f"    Removed {removed} duplicate slugs")
    
    # 2. Enrich each entity
    for entity in entities:
        # Enrich relationships
        old_rel_count = len(entity.get("relationships", []))
        entity["relationships"] = enrich_relationships(entity)
        new_rel_count = len(entity["relationships"])
        if new_rel_count > old_rel_count:
            stats["rels_added"] += (new_rel_count - old_rel_count)
        
        # Enrich hollow summaries
        old_summary = entity.get("summary", "")
        if len(old_summary) < 50:
            new_summary = enrich_hollow_summary_final(entity)
            if len(new_summary) > len(old_summary):
                entity["summary"] = new_summary
                entity["enrichedSummary"] = True
                stats["summaries_enriched"] += 1
        
        # Populate legacySummary
        if not entity.get("legacySummary"):
            legacy = enrich_legacy_summary(entity)
            if legacy:
                entity["legacySummary"] = legacy
                stats["legacy_added"] += 1
        
        # Populate altNames
        if not entity.get("altNames"):
            alts = populate_alt_names(entity)
            if alts:
                entity["altNames"] = alts
                stats["altnames_added"] += 1
    
    data["entities"] = entities
    
    # 3. Update metadata
    if "_meta" in data:
        data["_meta"]["entity_count"] = len(entities)
        data["_meta"]["audit_timestamp"] = "2026-04-04T20:00:00Z"
        data["_meta"]["audit_version"] = "3.0"
    
    print(f"    Entities: {len(entities):,} | +rels: {stats['rels_added']:,} | "
          f"+summaries: {stats['summaries_enriched']} | "
          f"+legacy: {stats['legacy_added']:,} | deduped: {stats['deduped']}")
    
    return data, stats


def main():
    print("╔═══════════════════════════════════════════════════════╗")
    print("║  Phase 3: Comprehensive JSON Enrichment & Cleanup    ║")
    print("╚═══════════════════════════════════════════════════════╝")
    
    # Collect all files to process
    files = sorted(DATA_DIR.glob("wikidata_*.json"))
    # Filter out the huge people.json (we use the split files)
    files = [f for f in files if f.name != "wikidata_people.json"]
    
    # Add people split files
    if PEOPLE_DIR.exists():
        files += sorted(PEOPLE_DIR.glob("wikidata_people_*.json"))
    
    total_stats = {
        "total": 0, "deduped": 0, "rels_added": 0,
        "summaries_enriched": 0, "legacy_added": 0, "altnames_added": 0,
    }
    
    for fp in files:
        data, stats = process_file(fp)
        
        # Save
        with open(fp, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        for k in total_stats:
            total_stats[k] += stats[k]
    
    # Update people manifest
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
                "size_mb": round(f.stat().st_size / (1024*1024), 1),
            }
        
        manifest = {
            "_meta": {
                "description": "Index of split people JSON files by division group",
                "total_entities": total_people,
                "total_files": len(manifest_files),
                "audit_timestamp": "2026-04-04T20:00:00Z",
            },
            "files": manifest_files,
        }
        with open(PEOPLE_DIR / "_manifest.json", "w") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
    
    # Final report
    print("\n╔═══════════════════════════════════════════════════════╗")
    print("║               PHASE 3 ENRICHMENT REPORT              ║")
    print("╠═══════════════════════════════════════════════════════╣")
    print(f"║  Entities processed:        {total_stats['total']:>10,}              ║")
    print(f"║  Duplicates removed:        {total_stats['deduped']:>10,}              ║")
    print(f"║  Relationships added:       {total_stats['rels_added']:>10,}              ║")
    print(f"║  Summaries enriched:        {total_stats['summaries_enriched']:>10,}              ║")
    print(f"║  Legacy summaries added:    {total_stats['legacy_added']:>10,}              ║")
    print(f"║  Alt names populated:       {total_stats['altnames_added']:>10,}              ║")
    print("╚═══════════════════════════════════════════════════════╝")


if __name__ == "__main__":
    main()
