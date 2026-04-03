#!/usr/bin/env python3
"""
seed_wikidata_to_appwrite.py

Reads the master data/wikidata_people.json, enriches each entity with:
  - Rich multi-sentence summaries (via Wikipedia REST API)
  - Multiple interpretive frameworks (mapped from division + keywords)
  - Causes, effects (inferred from era/domain context)
  - Richer relationships (OCCURS_IN + domain-relevant INFLUENCES/SHAPES)
  - Places, texts

Then seeds to Appwrite as documents in the `entities` collection.
Updates `inAppwrite` flag in the master JSON on success.

Usage:
  source .env && export APPWRITE_API_KEY
  python3 scripts/seed_wikidata_to_appwrite.py
  python3 scripts/seed_wikidata_to_appwrite.py --batch-size 50 --skip 0
  python3 scripts/seed_wikidata_to_appwrite.py --dry-run
  python3 scripts/seed_wikidata_to_appwrite.py --enrich-only  # just enrich, no Appwrite
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

# ── Config ──
PROJECT_ROOT = Path(__file__).resolve().parent.parent
MASTER_JSON  = PROJECT_ROOT / "data" / "wikidata_people.json"
ENDPOINT     = os.environ.get("VITE_APPWRITE_ENDPOINT", "https://fra.cloud.appwrite.io/v1")
PROJECT_ID   = os.environ.get("VITE_APPWRITE_PROJECT_ID", "69cc45e3000d587ea5e6")
DATABASE_ID  = os.environ.get("VITE_APPWRITE_DATABASE_ID", "annals_db")
API_KEY      = os.environ.get("APPWRITE_API_KEY", "")
COLLECTION   = "entities"

BATCH_SIZE   = 50
RETRY_LIMIT  = 3
RETRY_DELAY  = 1.0  # seconds
SAVE_EVERY   = 500  # save master JSON every N entities

# Wikipedia REST API for summaries
WIKI_API = "https://en.wikipedia.org/api/rest_v1/page/summary/"

# ── Framework Assignment by Division + Keywords ──
DIVISION_FRAMEWORKS: dict[str, list[str]] = {
    "201": ["CAUSE_AND_EFFECT", "INNOVATION_AND_TECHNOLOGY"],              # Educators
    "202": ["ECONOMIC_SYSTEMS", "GEOPOLITICAL_LINKAGE"],                    # Merchants
    "203": ["CAUSE_AND_EFFECT", "CULTURAL_DIFFUSION"],                      # Athletes
    "204": ["INNOVATION_AND_TECHNOLOGY", "CAUSE_AND_EFFECT"],               # Engineers
    "205": ["CAUSE_AND_EFFECT", "CULTURAL_DIFFUSION"],                      # Journalists
    "210": ["DOCTRINE_DEVELOPMENT", "CAUSE_AND_EFFECT"],                    # Philosophers
    "211": ["INNOVATION_AND_TECHNOLOGY", "CAUSE_AND_EFFECT"],               # Mathematicians
    "212": ["DOCTRINE_DEVELOPMENT", "CAUSE_AND_EFFECT"],                    # Ethicists
    "220": ["POLITICAL_SYSTEMS", "GEOPOLITICAL_LINKAGE", "CAUSE_AND_EFFECT"],  # Political Leaders
    "221": ["POLITICAL_SYSTEMS", "EMPIRE_AND_COLONIALISM", "GEOPOLITICAL_LINKAGE"],  # Monarchs
    "222": ["POLITICAL_SYSTEMS", "GEOPOLITICAL_LINKAGE"],                    # Heads of State
    "223": ["POLITICAL_SYSTEMS", "ADAPTATION"],                              # Tribal Leaders
    "230": ["LEGAL_INTERPRETATION", "CAUSE_AND_EFFECT"],                     # Legal Figures
    "231": ["LEGAL_INTERPRETATION", "DOCTRINE_DEVELOPMENT"],                 # Jurists
    "240": ["INNOVATION_AND_TECHNOLOGY", "CAUSE_AND_EFFECT"],                # Scientists
    "241": ["INNOVATION_AND_TECHNOLOGY", "CAUSE_AND_EFFECT"],                # Physicians
    "242": ["INNOVATION_AND_TECHNOLOGY", "CAUSE_AND_EFFECT"],                # Astronomers
    "243": ["INNOVATION_AND_TECHNOLOGY", "ENVIRONMENTAL_HISTORY"],           # Naturalists
    "250": ["COMPARATIVE_RELIGION", "DOCTRINE_DEVELOPMENT", "CULTURAL_DIFFUSION"],  # Religious
    "251": ["COMPARATIVE_RELIGION", "DOCTRINE_DEVELOPMENT"],                  # Prophets
    "252": ["DOCTRINE_DEVELOPMENT", "TEXTUAL_TRANSMISSION"],                  # Theologians
    "253": ["COMPARATIVE_RELIGION", "CULTURAL_DIFFUSION"],                    # Missionaries
    "260": ["CULTURAL_DIFFUSION", "CAUSE_AND_EFFECT"],                        # Artists
    "261": ["TEXTUAL_TRANSMISSION", "CULTURAL_DIFFUSION"],                    # Authors
    "262": ["TEXTUAL_TRANSMISSION", "CULTURAL_DIFFUSION"],                    # Poets
    "263": ["CULTURAL_DIFFUSION", "CAUSE_AND_EFFECT"],                        # Composers
    "264": ["CULTURAL_DIFFUSION", "CAUSE_AND_EFFECT"],                        # Painters
    "265": ["INNOVATION_AND_TECHNOLOGY", "CULTURAL_DIFFUSION"],               # Designers
    "270": ["CAUSE_AND_EFFECT", "CONFLICT_AND_RESOLUTION"],                   # Activists
    "271": ["CAUSE_AND_EFFECT", "CONFLICT_AND_RESOLUTION"],                   # Abolitionists
    "272": ["CAUSE_AND_EFFECT", "CONFLICT_AND_RESOLUTION"],                   # Suffragists
    "273": ["ECONOMIC_SYSTEMS", "CONFLICT_AND_RESOLUTION"],                   # Labor Leaders
    "280": ["CONFLICT_AND_RESOLUTION", "GEOPOLITICAL_LINKAGE"],               # Military
    "281": ["CONFLICT_AND_RESOLUTION", "GEOPOLITICAL_LINKAGE"],               # Naval
    "282": ["CONFLICT_AND_RESOLUTION", "GEOPOLITICAL_LINKAGE"],               # Intelligence
    "283": ["CONFLICT_AND_RESOLUTION", "GEOPOLITICAL_LINKAGE"],               # Modern Military
    "290": ["CULTURAL_DIFFUSION", "ENVIRONMENTAL_HISTORY", "GEOPOLITICAL_LINKAGE"],  # Explorers
    "291": ["INNOVATION_AND_TECHNOLOGY", "CAUSE_AND_EFFECT"],                  # Space Explorers
    "292": ["INNOVATION_AND_TECHNOLOGY", "ENVIRONMENTAL_HISTORY"],             # Deep-Sea
    "293": ["INNOVATION_AND_TECHNOLOGY", "CULTURAL_DIFFUSION"],                # Cartographers
}

# ── Division headings for relationship & cause/effect generation ──
DIVISION_HEADINGS: dict[str, str] = {
    "201": "Educators & Academics", "202": "Merchants & Economists",
    "203": "Athletes & Competitors", "204": "Architects & Engineers",
    "205": "Journalists & Chroniclers", "210": "Philosophers & Thinkers",
    "211": "Logicians & Mathematicians", "212": "Ethicists & Moralists",
    "220": "Political Leaders", "221": "Monarchs & Rulers",
    "222": "Heads of State & Government", "223": "Tribal & Indigenous Leaders",
    "230": "Legal Figures", "231": "Jurists & Legal Scholars",
    "240": "Scientists & Inventors", "241": "Physicians & Medical Pioneers",
    "242": "Astronomers & Cosmologists", "243": "Naturalists & Biologists",
    "250": "Religious Figures", "251": "Prophets & Founders",
    "252": "Theologians & Scholars", "253": "Missionaries",
    "260": "Artists & Writers", "261": "Authors & Novelists",
    "262": "Poets & Playwrights", "263": "Composers & Musicians",
    "264": "Painters & Sculptors", "265": "Architects & Designers",
    "270": "Activists & Reformers", "271": "Abolitionists",
    "272": "Suffragists & Feminists", "273": "Labor Organizers",
    "280": "Military Leaders & Commanders", "281": "Naval Commanders",
    "282": "Intelligence & Espionage", "283": "Modern Military Commanders",
    "290": "Explorers & Navigators", "291": "Space Explorers",
    "292": "Deep-Sea Explorers", "293": "Cartographers",
}

# Domain verbs for richer relationships by division
DIVISION_VERBS: dict[str, list[tuple[str, str]]] = {
    "201": [("TEACHES", "Educational influence"), ("DEVELOPS", "Pedagogical contribution")],
    "202": [("TRADES", "Commercial activity"), ("FINANCES", "Economic influence")],
    "203": [("COMPETES_IN", "Athletic achievement"), ("REPRESENTS", "Sporting representation")],
    "204": [("DESIGNS", "Engineering achievement"), ("CONSTRUCTS", "Built contribution")],
    "205": [("REPORTS", "Journalistic coverage"), ("CHRONICLES", "Historical reporting")],
    "210": [("THEORIZES", "Philosophical contribution"), ("INFLUENCES", "Intellectual influence")],
    "211": [("PROVES", "Mathematical contribution"), ("DEVELOPS", "Formal system")],
    "212": [("ADVOCATES", "Ethical position"), ("INFLUENCES", "Moral influence")],
    "220": [("GOVERNS", "Political leadership"), ("ENACTS", "Policy implementation")],
    "221": [("RULES", "Sovereign authority"), ("FOUNDS", "Dynastic establishment")],
    "222": [("LEADS", "State leadership"), ("REFORMS", "Governance reform")],
    "223": [("LEADS", "Tribal authority"), ("UNITES", "Community leadership")],
    "230": [("ADJUDICATES", "Legal ruling"), ("CODIFIES", "Legal framework")],
    "231": [("INTERPRETS", "Legal scholarship"), ("CODIFIES", "Jurisprudence")],
    "240": [("DISCOVERS", "Scientific discovery"), ("INVENTS", "Technological innovation")],
    "241": [("TREATS", "Medical advancement"), ("PIONEERS", "Medical innovation")],
    "242": [("OBSERVES", "Astronomical observation"), ("CALCULATES", "Celestial computation")],
    "243": [("CLASSIFIES", "Natural classification"), ("DOCUMENTS", "Biological documentation")],
    "250": [("PREACHES", "Religious teaching"), ("FOUNDS", "Religious establishment")],
    "251": [("PROCLAIMS", "Prophetic message"), ("FOUNDS", "Faith tradition")],
    "252": [("SYSTEMATIZES", "Theological system"), ("DEFENDS", "Doctrinal position")],
    "253": [("EVANGELIZES", "Missionary work"), ("CONVERTS", "Religious conversion")],
    "260": [("CREATES", "Artistic creation"), ("INFLUENCES", "Artistic influence")],
    "261": [("PUBLISHES", "Literary work"), ("NARRATES", "Storytelling")],
    "262": [("COMPOSES", "Poetic work"), ("PERFORMS", "Dramatic performance")],
    "263": [("COMPOSES", "Musical composition"), ("PERFORMS", "Musical performance")],
    "264": [("PAINTS", "Visual art"), ("SCULPTS", "Sculptural work")],
    "265": [("DESIGNS", "Design work"), ("CONCEIVES", "Architectural vision")],
    "270": [("CAMPAIGNS", "Reform activism"), ("ORGANIZES", "Social movement")],
    "271": [("CAMPAIGNS", "Abolition activism"), ("LIBERATES", "Emancipation effort")],
    "272": [("CAMPAIGNS", "Suffrage activism"), ("ADVOCATES", "Women's rights")],
    "273": [("ORGANIZES", "Labor organizing"), ("STRIKES", "Industrial action")],
    "280": [("COMMANDS", "Military command"), ("CONQUERS", "Military conquest")],
    "281": [("COMMANDS", "Naval command"), ("BLOCKADES", "Naval strategy")],
    "282": [("INFILTRATES", "Espionage operation"), ("ANALYZES", "Intelligence analysis")],
    "283": [("COMMANDS", "Military command"), ("STRATEGIZES", "Military strategy")],
    "290": [("EXPLORES", "Exploration voyage"), ("MAPS", "Geographic mapping")],
    "291": [("LAUNCHES", "Space mission"), ("ORBITS", "Space exploration")],
    "292": [("DIVES", "Deep-sea exploration"), ("DISCOVERS", "Underwater discovery")],
    "293": [("MAPS", "Cartographic work"), ("SURVEYS", "Geographic survey")],
}

# Era-specific context for causes/effects
ERA_CONTEXT: dict[str, dict[str, str]] = {
    "Prehistoric": {
        "cause": "emergence of early civilizations and development of foundational human practices",
        "effect": "laying groundwork for recorded human history and cultural transmission",
    },
    "Classical": {
        "cause": "flourishing of philosophical inquiry, imperial expansion, and codification of law",
        "effect": "enduring intellectual and institutional frameworks that shaped subsequent civilizations",
    },
    "Medieval": {
        "cause": "interplay of religious authority, feudal governance, and trade network expansion",
        "effect": "synthesis of classical and religious thought informing Renaissance and Reformation",
    },
    "Early Modern": {
        "cause": "age of exploration, printing revolution, and religious reformation",
        "effect": "global exchange networks, modern state formation, and scientific revolution",
    },
    "Modern": {
        "cause": "industrialization, imperial expansion, and democratic revolutions",
        "effect": "mass society, world wars, and foundations of contemporary global order",
    },
    "Contemporary": {
        "cause": "decolonization, technological revolution, and global interconnection",
        "effect": "digital transformation, global governance challenges, and cultural globalization",
    },
}


# ── Wikipedia Summary Fetcher ──
def fetch_wiki_summary(wikipedia_url: str) -> str | None:
    """Fetch extract summary from Wikipedia REST API. Returns description or None."""
    if not wikipedia_url:
        return None
    # Extract article title from URL
    # https://en.wikipedia.org/wiki/Albert_Einstein → Albert_Einstein
    match = re.search(r"wikipedia\.org/wiki/(.+?)(?:\?|#|$)", wikipedia_url)
    if not match:
        return None
    title = match.group(1)
    url = WIKI_API + urllib.parse.quote(title, safe="")
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "AnnalsOfTheWorld/2.0 (scholarly-project; contact@annals.dev)",
            "Accept": "application/json",
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            extract = data.get("extract", "")
            if extract and len(extract) > 40:
                return extract.strip()
    except Exception:
        pass
    return None


# ── Enrichment Functions ──

def enrich_summary(entity: dict, wiki_extract: str | None) -> str:
    """Build a rich multi-sentence summary."""
    name = entity["name"]
    div = entity["callNumber"][:3]
    heading = DIVISION_HEADINGS.get(div, "Notable Figure")
    era = entity.get("era", "")
    born = entity.get("born", "")
    died = entity.get("died", "")
    continent = entity.get("continent", "")
    region = entity.get("region", "")

    # Use Wikipedia extract if available
    if wiki_extract and len(wiki_extract) > 60:
        summary = wiki_extract
        # Append era/domain context if not already rich enough
        if len(summary) < 200:
            location_part = ""
            if region and region != "Global":
                location_part = f" based in {region}"
            elif continent and continent != "Global":
                location_part = f" based in {continent}"
            dates_part = ""
            if born and died:
                dates_part = f" ({born} – {died})"
            elif born:
                dates_part = f" (b. {born})"
            summary += f" {name} was a noted figure among {heading.lower()}{location_part}{dates_part}, active during the {era} era."
        return summary[:9997] + "..." if len(summary) > 10000 else summary

    # Build synthetic summary from available data
    parts = []

    # Opening
    location_part = ""
    if region and region != "Global":
        location_part = f" from {region}"
    elif continent and continent != "Global":
        location_part = f" from {continent}"

    dates_part = ""
    if born and died:
        dates_part = f" ({born} – {died})"
    elif born:
        dates_part = f" (b. {born})"

    parts.append(f"{name}{dates_part} was a notable figure in the category of {heading.lower()}{location_part}.")

    # Era context
    era_ctx = ERA_CONTEXT.get(era, {})
    if era_ctx:
        parts.append(f"Active during the {era} era, a period characterized by {era_ctx.get('cause', 'significant historical developments')}.")

    # Places context
    places = entity.get("places", [])
    if places:
        place_names = [p["name"] for p in places if p.get("name")]
        if place_names:
            parts.append(f"Associated with {', '.join(place_names[:3])}.")

    # Domain contribution
    domain_verbs = DIVISION_VERBS.get(div, [])
    if domain_verbs:
        verb_desc = domain_verbs[0][1]  # first verb's context
        parts.append(f"Their work contributed to {verb_desc.lower()} in the broader historical narrative.")

    result = " ".join(parts)
    return result[:9997] + "..." if len(result) > 10000 else result


def assign_frameworks(entity: dict) -> list[str]:
    """Assign 2-3 interpretive frameworks based on division, era, and content."""
    div = entity["callNumber"][:3]
    frameworks = list(DIVISION_FRAMEWORKS.get(div, ["CAUSE_AND_EFFECT"]))

    # Add era-specific frameworks
    era = entity.get("era", "")
    if era in ("Classical", "Medieval") and "TEMPORAL_LINKAGE" not in frameworks:
        frameworks.append("TEMPORAL_LINKAGE")
    if era in ("Early Modern", "Modern") and "EMPIRE_AND_COLONIALISM" not in frameworks:
        if div in ("220", "221", "222", "280", "281", "290"):
            frameworks.append("EMPIRE_AND_COLONIALISM")

    # Cap at 4 frameworks
    return frameworks[:4]


def build_causes(entity: dict) -> list[dict]:
    """Generate 1-2 causal antecedents from era and domain context."""
    div = entity["callNumber"][:3]
    era = entity.get("era", "")
    heading = DIVISION_HEADINGS.get(div, "Notable Figures")
    era_ctx = ERA_CONTEXT.get(era, {})
    causes = []

    if era_ctx:
        causes.append({
            "title": f"{era} era: {era_ctx['cause'][:80]}",
            "type": "EventWindow",
            "year": entity.get("born", era),
        })

    # Domain-specific cause
    domain_causes: dict[str, str] = {
        "201": "Growth of educational institutions and scholarly traditions",
        "202": "Expansion of trade networks and commercial exchange",
        "203": "Development of competitive athletics and sporting traditions",
        "204": "Advancement of engineering knowledge and construction techniques",
        "205": "Rise of print media and public discourse",
        "210": "Ongoing philosophical inquiry and intellectual debate",
        "211": "Accumulation of mathematical knowledge and formal systems",
        "220": "Political crises and power transitions requiring new leadership",
        "221": "Dynastic succession and sovereign authority traditions",
        "222": "Democratic movements and constitutional governance",
        "230": "Evolution of legal systems and jurisprudence",
        "240": "Scientific curiosity and systematic investigation of nature",
        "241": "Medical challenges driving innovation in healing arts",
        "242": "Astronomical observations and cosmological questions",
        "243": "Exploration of natural world driving biological classification",
        "250": "Spiritual seeking and religious community formation",
        "252": "Theological debates and doctrinal development",
        "253": "Religious conviction driving cross-cultural mission",
        "260": "Artistic traditions and creative expression across cultures",
        "261": "Literary traditions and narrative storytelling",
        "262": "Poetic traditions and dramatic performance arts",
        "263": "Musical traditions and compositional innovation",
        "264": "Visual art traditions and aesthetic movements",
        "265": "Design traditions and architectural innovation",
        "270": "Social injustice and moral conviction driving reform",
        "273": "Worker exploitation and industrial conditions",
        "280": "Military conflicts and strategic necessities",
        "281": "Naval warfare and maritime strategy",
        "290": "Curiosity about unknown territories and navigation advances",
        "291": "Space race and technological competition",
        "293": "Geographic knowledge gaps and mapping imperatives",
    }
    if div in domain_causes:
        causes.append({
            "title": domain_causes[div],
            "type": "Idea",
            "year": entity.get("born", ""),
        })

    return causes[:2]


def build_effects(entity: dict) -> list[dict]:
    """Generate 1-2 consequent outcomes from era and domain context."""
    div = entity["callNumber"][:3]
    era = entity.get("era", "")
    heading = DIVISION_HEADINGS.get(div, "Notable Figures")
    era_ctx = ERA_CONTEXT.get(era, {})
    effects = []

    # Domain-specific effect
    domain_effects: dict[str, str] = {
        "201": "Shaped intellectual traditions and educated future generations",
        "202": "Influenced economic patterns and commercial practices",
        "203": "Inspired sporting achievement and athletic culture",
        "204": "Left lasting engineering works and technical innovations",
        "205": "Shaped public opinion and historical record",
        "210": "Contributed philosophical ideas to ongoing intellectual discourse",
        "211": "Advanced mathematical knowledge used by subsequent scholars",
        "220": "Shaped political institutions and governance practices",
        "221": "Established dynastic legacies and territorial boundaries",
        "222": "Influenced national policy and international relations",
        "230": "Shaped legal precedents and judicial practices",
        "240": "Advanced scientific knowledge and enabled new technologies",
        "241": "Improved medical practice and public health outcomes",
        "242": "Expanded astronomical understanding and cosmological models",
        "243": "Advanced biological classification and ecological understanding",
        "250": "Shaped religious practice and spiritual communities",
        "252": "Developed theological frameworks influencing doctrine",
        "253": "Established religious communities in new regions",
        "260": "Enriched cultural heritage with lasting artistic works",
        "261": "Created literary works of enduring influence",
        "262": "Contributed poetry and drama to cultural canon",
        "263": "Created musical compositions of lasting significance",
        "264": "Produced visual artworks of cultural importance",
        "265": "Created architectural and design works shaping built environment",
        "270": "Advanced social reform and expanded civil liberties",
        "273": "Improved labor conditions and worker protections",
        "280": "Determined military outcomes shaping geopolitical boundaries",
        "281": "Influenced naval strategy and maritime power dynamics",
        "290": "Expanded geographic knowledge and cultural exchange",
        "291": "Advanced space exploration and aerospace technology",
        "293": "Improved cartographic accuracy and geographic understanding",
    }

    if div in domain_effects:
        effects.append({
            "title": domain_effects[div],
            "type": "Idea",
            "year": entity.get("died", ""),
        })

    if era_ctx:
        effects.append({
            "title": f"Contributed to {era_ctx['effect'][:80]}",
            "type": "Movement",
            "year": entity.get("died", era),
        })

    return effects[:2]


def build_relationships(entity: dict) -> list[dict]:
    """Build richer relationships from domain, places, and era."""
    rels = []
    slug = entity["slug"]
    name = entity["name"]
    div = entity["callNumber"][:3]

    # Keep existing OCCURS_IN relationships
    for r in entity.get("relationships", []):
        rels.append(r)

    # Add domain-specific verb relationships
    verbs = DIVISION_VERBS.get(div, [])
    heading = DIVISION_HEADINGS.get(div, "their field")
    if verbs:
        verb, context = verbs[0]
        rels.append({
            "sourceSlug": slug,
            "sourceName": name,
            "verb": verb,
            "targetSlug": f"field-{div}",
            "targetName": heading,
            "context": f"{name}: {context} in {heading.lower()}",
        })

    # Era-level relationship
    era = entity.get("era", "")
    era_slug = entity.get("eraSlug", "")
    if era and era_slug:
        rels.append({
            "sourceSlug": slug,
            "sourceName": name,
            "verb": "OCCURS_DURING",
            "targetSlug": era_slug,
            "targetName": f"{era} Era",
            "context": f"{name} was active during the {era} era",
        })

    # Places relationships (add INFLUENCES for birthplace/country)
    places = entity.get("places", [])
    for p in places:
        p_name = p.get("name", "")
        p_slug = p.get("slug", "")
        p_role = p.get("role", "")
        if p_name and p_role == "Country" and p_slug:
            # Already has OCCURS_IN from original data, add SHAPES
            rels.append({
                "sourceSlug": slug,
                "sourceName": name,
                "verb": "SHAPES",
                "targetSlug": p_slug,
                "targetName": p_name,
                "context": f"{name} contributed to the historical development of {p_name}",
            })

    return rels


def build_texts(entity: dict) -> list[dict]:
    """Build text references from domain context."""
    div = entity["callNumber"][:3]
    texts = list(entity.get("texts", []))

    # Add Wikipedia as a reference text if available
    wiki_url = entity.get("wikipediaUrl", "")
    if wiki_url:
        texts.append({
            "title": f"Wikipedia: {entity['name']}",
            "type": "Reference article",
            "slug": f"wikipedia-{entity['slug']}",
        })

    return texts


def enrich_entity(entity: dict, wiki_extract: str | None) -> dict:
    """Fully enrich an entity for Appwrite seeding."""
    enriched = dict(entity)

    # Rich summary
    enriched["summary"] = enrich_summary(entity, wiki_extract)

    # Frameworks
    enriched["frameworks"] = assign_frameworks(entity)

    # Causes & Effects
    enriched["causes"] = build_causes(entity)
    enriched["effects"] = build_effects(entity)

    # Relationships
    enriched["relationships"] = build_relationships(entity)

    # Texts
    enriched["texts"] = build_texts(entity)

    return enriched


# ── Appwrite Document Creation ──

def to_doc_id(slug: str) -> str:
    """Generate deterministic document ID from slug (matching migrate_to_appwrite.ts)."""
    clean = re.sub(r"[^a-zA-Z0-9_-]", "_", slug)
    safe = re.sub(r"^[_-]+", "", clean)
    if 0 < len(safe) <= 36:
        return safe
    # Long slugs: first 27 chars + '_' + 8-char hash
    h = 5381
    for ch in slug:
        h = ((h << 5) + h + ord(ch)) & 0xFFFFFFFF
    hash_str = format(h, "x").ljust(8, "0")[:8]
    prefix = re.sub(r"[_-]+$", "", safe[:27])
    return (prefix + "_" + hash_str)[:36]


def truncate(s: str | None, max_len: int) -> str:
    if not s:
        return ""
    return s[:max_len - 3] + "..." if len(s) > max_len else s


def to_appwrite_document(entity: dict) -> dict:
    """Transform enriched entity to Appwrite document shape."""
    e = entity
    details_json = json.dumps({
        "tags": [],
        "externalLinks": [e.get("wikipediaUrl", "")] if e.get("wikipediaUrl") else [],
        "thumbnailUrl": e.get("imageUrl") or None,
        "quote": None,
        "legacySummary": None,
        "causes": e.get("causes", []),
        "effects": e.get("effects", []),
        "relationships": e.get("relationships", []),
        "places": e.get("places", []),
        "texts": e.get("texts", []),
    }, ensure_ascii=False)

    return {
        "slug": e["slug"],
        "name": e["name"],
        "label": e["label"],
        "callNumber": e["callNumber"],
        "summary": truncate(e.get("summary", ""), 10000),
        "era": e.get("era", ""),
        "eraSlug": e.get("eraSlug", ""),
        "region": e.get("region", ""),
        "continent": e.get("continent", ""),
        "status": e.get("status", "Published"),
        "born": e.get("born") or None,
        "died": e.get("died") or None,
        "founded": None,
        "period": None,
        "startDate": e.get("born") or None,
        "endDate": e.get("died") or None,
        "subjectHeadings": e.get("subjectHeadings", []),
        "subjects": e.get("subjects", []),
        "frameworks": e.get("frameworks", []),
        "altNames": [],
        "wikidataQid": e.get("wikidataQid") or None,
        "wikipediaUrl": e.get("wikipediaUrl") or None,
        "imageUrl": e.get("imageUrl") or None,
        "importanceScore": None,
        "detailsJson": truncate(details_json, 100000),
    }


def appwrite_create(doc_id: str, data: dict, attempt: int = 1) -> str:
    """Create document in Appwrite. Returns 'created', 'exists', or 'failed'."""
    url = f"{ENDPOINT}/databases/{DATABASE_ID}/collections/{COLLECTION}/documents"
    body = json.dumps({
        "documentId": doc_id,
        "data": data,
    }, ensure_ascii=False).encode("utf-8")

    req = urllib.request.Request(url, data=body, method="POST", headers={
        "Content-Type": "application/json",
        "X-Appwrite-Project": PROJECT_ID,
        "X-Appwrite-Key": API_KEY,
    })

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return "created"
    except urllib.error.HTTPError as e:
        if e.code == 409:
            return "exists"
        if e.code == 429:
            # Rate limited — wait and retry
            retry_after = int(e.headers.get("Retry-After", "5"))
            time.sleep(retry_after)
            if attempt < RETRY_LIMIT:
                return appwrite_create(doc_id, data, attempt + 1)
        if attempt < RETRY_LIMIT:
            time.sleep(RETRY_DELAY * attempt)
            return appwrite_create(doc_id, data, attempt + 1)
        return "failed"
    except Exception:
        if attempt < RETRY_LIMIT:
            time.sleep(RETRY_DELAY * attempt)
            return appwrite_create(doc_id, data, attempt + 1)
        return "failed"


# ── Batch Wikipedia Fetcher ──

def fetch_wiki_batch(entities: list[dict], max_per_second: int = 50) -> dict[str, str]:
    """Fetch Wikipedia summaries for a batch of entities. Returns slug → extract dict."""
    results: dict[str, str] = {}
    delay = 1.0 / max_per_second  # respect rate limits

    for entity in entities:
        wiki_url = entity.get("wikipediaUrl", "")
        if wiki_url:
            extract = fetch_wiki_summary(wiki_url)
            if extract:
                results[entity["slug"]] = extract
            time.sleep(delay)

    return results


# ── Main ──

def main():
    parser = argparse.ArgumentParser(description="Seed Wikidata people to Appwrite")
    parser.add_argument("--batch-size", type=int, default=BATCH_SIZE)
    parser.add_argument("--skip", type=int, default=0, help="Skip first N entities")
    parser.add_argument("--max", type=int, default=0, help="Max entities to process (0=all)")
    parser.add_argument("--dry-run", action="store_true", help="Enrich + print, no Appwrite")
    parser.add_argument("--enrich-only", action="store_true", help="Enrich JSON only, no Appwrite")
    parser.add_argument("--no-wiki", action="store_true", help="Skip Wikipedia API calls")
    args = parser.parse_args()

    if not args.dry_run and not args.enrich_only and not API_KEY:
        print("ERROR: Set APPWRITE_API_KEY env var (or use --dry-run / --enrich-only)")
        sys.exit(1)

    print(f"Loading master dataset: {MASTER_JSON}")
    with open(MASTER_JSON, encoding="utf-8") as f:
        master = json.load(f)

    all_entities = master["entities"]
    print(f"Total entities: {len(all_entities):,}")

    # Filter to only not-in-Appwrite entities
    candidates = [e for e in all_entities if not e.get("inAppwrite")]
    print(f"Not in Appwrite: {len(candidates):,}")

    # Apply skip/max
    if args.skip:
        candidates = candidates[args.skip:]
        print(f"After skip {args.skip}: {len(candidates):,}")
    if args.max:
        candidates = candidates[:args.max]
        print(f"Capped at max {args.max}: {len(candidates):,}")

    if args.dry_run:
        # Show 3 enriched samples
        print("\n=== DRY RUN — showing 3 enriched samples ===\n")
        for entity in candidates[:3]:
            wiki_extract = None
            if not args.no_wiki and entity.get("wikipediaUrl"):
                wiki_extract = fetch_wiki_summary(entity["wikipediaUrl"])
            enriched = enrich_entity(entity, wiki_extract)
            doc = to_appwrite_document(enriched)
            print(f"  [{doc['callNumber']}] {doc['name']} ({doc['era']})")
            print(f"  Summary: {doc['summary'][:200]}...")
            print(f"  Frameworks: {doc['frameworks']}")
            details = json.loads(doc["detailsJson"])
            print(f"  Causes: {len(details['causes'])}")
            print(f"  Effects: {len(details['effects'])}")
            print(f"  Relationships: {len(details['relationships'])}")
            print(f"  Places: {len(details['places'])}")
            print(f"  Texts: {len(details['texts'])}")
            print()
        print(f"Would process {len(candidates):,} entities total")
        return

    # ── Process in batches ──
    created = 0
    exists = 0
    failed = 0
    enriched_count = 0
    entity_map = {e["slug"]: e for e in all_entities}  # for fast flag updates
    start_time = time.time()

    print(f"\n{'Enriching' if args.enrich_only else 'Enriching + seeding'} {len(candidates):,} entities...")
    print(f"  Batch size: {args.batch_size}")
    print(f"  Wikipedia API: {'disabled' if args.no_wiki else 'enabled'}")
    if not args.enrich_only:
        print(f"  Appwrite: {ENDPOINT}")
    print()

    for batch_start in range(0, len(candidates), args.batch_size):
        batch = candidates[batch_start:batch_start + args.batch_size]

        # Fetch Wikipedia summaries for batch
        wiki_extracts: dict[str, str] = {}
        if not args.no_wiki:
            for entity in batch:
                wiki_url = entity.get("wikipediaUrl", "")
                if wiki_url:
                    extract = fetch_wiki_summary(wiki_url)
                    if extract:
                        wiki_extracts[entity["slug"]] = extract
                    time.sleep(0.02)  # 50 req/sec max

        # Enrich + seed each entity
        for entity in batch:
            slug = entity["slug"]
            wiki_extract = wiki_extracts.get(slug)
            enriched = enrich_entity(entity, wiki_extract)
            enriched_count += 1

            # Update entity in master list
            idx_entity = entity_map[slug]
            idx_entity["summary"] = enriched["summary"]
            idx_entity["frameworks"] = enriched["frameworks"]
            idx_entity["causes"] = enriched["causes"]
            idx_entity["effects"] = enriched["effects"]
            idx_entity["relationships"] = enriched["relationships"]
            idx_entity["texts"] = enriched["texts"]

            if not args.enrich_only:
                doc_id = to_doc_id(slug)
                doc = to_appwrite_document(enriched)
                result = appwrite_create(doc_id, doc)

                if result == "created":
                    created += 1
                    idx_entity["inAppwrite"] = True
                elif result == "exists":
                    exists += 1
                    idx_entity["inAppwrite"] = True
                else:
                    failed += 1
            else:
                # Enrich-only: mark flag as if seeded
                pass

        # Progress
        progress = min(batch_start + args.batch_size, len(candidates))
        elapsed = time.time() - start_time
        rate = progress / elapsed if elapsed > 0 else 0
        eta_seconds = (len(candidates) - progress) / rate if rate > 0 else 0
        eta_min = eta_seconds / 60

        if progress % SAVE_EVERY == 0 or progress == len(candidates):
            if not args.enrich_only:
                print(f"  [{progress:,}/{len(candidates):,}] created={created} exists={exists} failed={failed} "
                      f"rate={rate:.1f}/s ETA={eta_min:.0f}min")
            else:
                print(f"  [{progress:,}/{len(candidates):,}] enriched={enriched_count} "
                      f"rate={rate:.1f}/s ETA={eta_min:.0f}min")

            # Save master JSON periodically
            with open(MASTER_JSON, "w", encoding="utf-8") as f:
                json.dump(master, f, indent=2, ensure_ascii=False)

        # Rate limit between batches
        if not args.enrich_only:
            time.sleep(0.2)

    # Final save
    with open(MASTER_JSON, "w", encoding="utf-8") as f:
        json.dump(master, f, indent=2, ensure_ascii=False)

    elapsed = time.time() - start_time

    print(f"\n=== Complete ({elapsed/60:.1f} min) ===")
    print(f"  Enriched: {enriched_count:,}")
    if not args.enrich_only:
        print(f"  Created:  {created:,}")
        print(f"  Existed:  {exists:,}")
        print(f"  Failed:   {failed:,}")
    print(f"  Master JSON saved: {MASTER_JSON}")

    # Count updated flags
    in_appwrite = sum(1 for e in all_entities if e.get("inAppwrite"))
    not_in = sum(1 for e in all_entities if not e.get("inAppwrite"))
    print(f"  Now in Appwrite: {in_appwrite:,}")
    print(f"  Still NOT in Appwrite: {not_in:,}")


if __name__ == "__main__":
    main()
