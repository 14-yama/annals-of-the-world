#!/usr/bin/env python3
"""
enrich_people_json.py — Comprehensive enrichment of wikidata_people.json

1. Adds divisionCode & divisionHeading from callNumber
2. Adds historicalSignificance (score, label, sitelinks proxy)
3. Enriches summaries with era context, geographic detail, field contributions
4. Audits & fixes division assignments based on subject/summary keywords
5. Recomputes _meta statistics
"""

import json
import re
import time
from collections import Counter
from pathlib import Path

# ═══════════════════════════════════════════════════════════════════
# Division definitions (Class 2 — People)
# ═══════════════════════════════════════════════════════════════════

DIVISION_MAP: dict[str, str] = {
    "200": "People",
    "201": "Writers & Intellectuals",
    "202": "Performers & Entertainers",
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

# ═══════════════════════════════════════════════════════════════════
# Era context strings for enriched summaries
# ═══════════════════════════════════════════════════════════════════

ERA_CONTEXT: dict[str, str] = {
    "Prehistoric": (
        "during the Prehistoric era, a time when early human civilizations "
        "established foundational practices in agriculture, tool-making, "
        "and communal governance that shaped the trajectory of human history"
    ),
    "Classical": (
        "during the Classical era (3000 BCE–500 CE), an age of philosophical "
        "inquiry, imperial expansion, legal codification, and the birth of "
        "written traditions across Mediterranean, Asian, and African civilizations"
    ),
    "Medieval": (
        "during the Medieval era (500–1500 CE), a period defined by the interplay "
        "of religious authority and feudal governance, the rise of scholasticism, "
        "and cross-civilizational exchange along the Silk Road and maritime trade routes"
    ),
    "Early Modern": (
        "during the Early Modern era (1500–1800 CE), a transformative period "
        "of global exploration, religious reformation, Enlightenment thought, "
        "the scientific revolution, and the expansion of colonial empires"
    ),
    "Modern": (
        "during the Modern era (1800–1945 CE), a period of industrialization, "
        "democratic revolutions, imperial competition, world wars, and the rise "
        "of mass communication that reshaped global political and social order"
    ),
    "Contemporary": (
        "during the Contemporary era (1945–present), an age of decolonization, "
        "Cold War geopolitics, digital revolution, globalization, and emerging "
        "challenges in human rights, environmentalism, and technological ethics"
    ),
}

# ═══════════════════════════════════════════════════════════════════
# Division-specific contribution phrases
# ═══════════════════════════════════════════════════════════════════

DIVISION_CONTRIBUTIONS: dict[str, str] = {
    "201": "literary and intellectual discourse, shaping how ideas were recorded and transmitted",
    "202": "performing arts and entertainment, influencing cultural expression and public imagination",
    "203": "competitive athletics, embodying human physical achievement and international sportsmanship",
    "204": "architectural and engineering innovation, transforming built environments and infrastructure",
    "205": "journalism and chronicle-keeping, documenting events for posterity and shaping public discourse",
    "210": "philosophical thought and intellectual inquiry, advancing humanity's understanding of existence, knowledge, and ethics",
    "211": "mathematical logic and formal reasoning, building the foundations of scientific and computational thinking",
    "212": "ethical theory and moral philosophy, guiding societal norms and frameworks for justice",
    "220": "political leadership and statecraft, shaping governance systems and national destinies",
    "221": "sovereign rule and dynastic governance, influencing territorial boundaries and cultural identity",
    "222": "executive leadership and international diplomacy, directing policy and state affairs",
    "223": "indigenous governance and tribal leadership, preserving and adapting communal traditions",
    "230": "legal theory and jurisprudence, establishing frameworks for justice and civil order",
    "231": "legal scholarship and judicial interpretation, advancing the codification of law",
    "240": "scientific discovery and invention, expanding knowledge of the natural world and developing new technologies",
    "241": "medical science and healing, advancing public health, surgical technique, and disease prevention",
    "242": "astronomical observation and cosmological theory, deepening understanding of celestial phenomena",
    "243": "natural history and biological science, cataloging life forms and illuminating evolutionary processes",
    "250": "religious leadership and spiritual guidance, shaping faith traditions and moral communities",
    "251": "prophetic vision and religious founding, establishing new spiritual movements and sacred texts",
    "252": "theological scholarship and doctrinal development, interpreting sacred texts and shaping religious thought",
    "253": "missionary work and evangelism, spreading religious traditions across cultural and geographic boundaries",
    "260": "artistic creation and literary expression, enriching cultural heritage and humanistic understanding",
    "261": "prose fiction and narrative literature, exploring human experience through storytelling",
    "262": "poetry and dramatic arts, giving voice to emotional depth and cultural aspiration",
    "263": "musical composition and performance, creating works that define cultural movements and human emotion",
    "264": "painting, sculpture, and visual arts, producing iconic works that capture the human experience",
    "265": "architectural and design innovation, shaping aesthetic movements and functional spaces",
    "270": "social activism and reform, challenging injustice and advancing human rights",
    "271": "abolitionist advocacy, fighting to end slavery and forced labor",
    "272": "suffrage and feminist advocacy, expanding political rights and gender equality",
    "273": "labor organizing and workers' rights, improving conditions and collective bargaining power",
    "280": "military command and strategic leadership, directing forces in conflicts that shaped borders and nations",
    "281": "naval command and maritime strategy, exerting power across oceans and trade routes",
    "282": "intelligence and espionage, operating in the covert dimensions of statecraft and warfare",
    "283": "modern military command, leading forces in the complex theaters of industrialized war",
    "290": "exploration and navigation, pushing the boundaries of the known world",
    "291": "space exploration, venturing beyond Earth and expanding humanity's cosmic frontier",
    "292": "deep-sea exploration, revealing the mysteries of ocean depths",
    "293": "cartography and geographic mapping, charting the physical world for navigation and governance",
}

# ═══════════════════════════════════════════════════════════════════
# Region context
# ═══════════════════════════════════════════════════════════════════

REGION_CONTEXT: dict[str, str] = {
    "North America": "within the cultural and political landscape of North America",
    "South America": "within the diverse societies and transformative movements of South America",
    "Central America": "in the dynamic civilizations and crossroads of Central America",
    "Caribbean": "amid the colonial histories and cultural synthesis of the Caribbean",
    "Northern Europe": "in the intellectual and maritime traditions of Northern Europe",
    "Western Europe": "within the political and cultural heartlands of Western Europe",
    "Southern Europe": "in the Mediterranean cradle of Southern European civilization",
    "Eastern Europe": "across the contested and transformative terrain of Eastern Europe",
    "East Asia": "in the enduring civilizations and philosophical traditions of East Asia",
    "South Asia": "in the diverse spiritual and political traditions of South Asia",
    "Southeast Asia": "within the maritime kingdoms and cultural exchanges of Southeast Asia",
    "West Asia": "in the ancient civilizations and crossroads of West Asia",
    "Central Asia": "along the Silk Road corridors and nomadic traditions of Central Asia",
    "North Africa": "in the ancient Nilotic and Saharan civilizations of North Africa",
    "West Africa": "within the rich kingdoms and oral traditions of West Africa",
    "East Africa": "in the trade networks and diverse cultures of East Africa",
    "Southern Africa": "across the ecological and cultural diversity of Southern Africa",
    "Oceania": "in the navigational traditions and island cultures of Oceania",
    "Global": "",
}

# ═══════════════════════════════════════════════════════════════════
# Division audit: keyword-based correction
# ═══════════════════════════════════════════════════════════════════

AUDIT_KEYWORDS: dict[str, list[tuple[list[str], str]]] = {
    # If someone in 203 (Athletes) has these keywords, maybe they belong elsewhere
    "reclassify": [
        # Writers mislabeled
        (["novelist", "author", "literary", "book", "fiction"], "261"),
        (["poet", "verse", "sonnet", "poem"], "262"),
        (["journalist", "reporter", "editor", "newspaper"], "205"),
        # Scientists mislabeled
        (["physicist", "quantum", "relativity"], "240"),
        (["astronomer", "telescope", "observatory", "comet", "celestial"], "242"),
        (["biologist", "botanist", "naturalist", "taxonomy", "species"], "243"),
        (["physician", "surgeon", "medical doctor", "pathologist"], "241"),
        # Military mislabeled
        (["admiral", "fleet", "naval"], "281"),
        (["spy", "intelligence agent", "espionage"], "282"),
        # Explorer mislabeled
        (["astronaut", "cosmonaut", "spaceflight"], "291"),
        (["cartographer", "map-maker", "surveyor"], "293"),
        # Activist mislabeled
        (["abolitionist", "anti-slavery"], "271"),
        (["suffragist", "feminist", "women's rights"], "272"),
        (["labor leader", "union organizer", "trade union"], "273"),
    ]
}


def extract_division(call_number: str) -> str:
    """Extract 3-digit division code from call number like '221.bull'."""
    if "." in call_number:
        return call_number.split(".")[0]
    return call_number[:3]


def parse_birth_year(born_str: str | None) -> int | None:
    """Parse birth year from various formats."""
    if not born_str:
        return None
    # Match ISO date: 1879-12-14
    m = re.match(r'^(\d{4})-\d{2}-\d{2}', born_str)
    if m:
        return int(m.group(1))
    # Match "3500 BCE"
    m = re.match(r'^(\d+)\s*BCE', born_str)
    if m:
        return -int(m.group(1))
    # Match "123 CE" or just year
    m = re.match(r'^(\d+)\s*(?:CE)?', born_str)
    if m:
        return int(m.group(1))
    return None


def compute_significance(entity: dict) -> dict:
    """
    Compute historicalSignificance using era-anchored scoring.
    Since people JSON lacks sitelinks, era antiquity is the primary
    discriminator (older = rarer = more significant), supplemented
    by data-richness signals.

    Era base:  Prehistoric 7, Classical 6, Medieval 5,
               Early Modern 4, Modern 3, Contemporary 2

    Framework bonus:  4+ → +2,  3 → +1
    Data quality:     Wikipedia + born + 3 rels → +1,  places → +1
    """
    era = entity.get("era", "Contemporary")

    # Era-anchored base score
    era_scores = {
        "Prehistoric": 7,
        "Classical": 6,
        "Medieval": 5,
        "Early Modern": 4,
        "Modern": 3,
        "Contemporary": 2,
    }
    score = era_scores.get(era, 2)

    # Framework richness
    fw_count = len(entity.get("frameworks", []))
    if fw_count >= 4:
        score += 2
    elif fw_count >= 3:
        score += 1

    # Data completeness
    has_wiki = bool(entity.get("wikipediaUrl"))
    has_born = bool(entity.get("born"))
    has_full_rels = len(entity.get("relationships", [])) >= 3
    if has_wiki and has_born and has_full_rels:
        score += 1
    if entity.get("places"):
        score += 1

    score = max(1, min(10, score))

    if score >= 9:
        label = "Landmark"
    elif score >= 7:
        label = "Major"
    elif score >= 5:
        label = "Notable"
    elif score >= 3:
        label = "Moderate"
    else:
        label = "Minor"

    return {"score": score, "label": label}


def audit_division(entity: dict, div_code: str) -> str:
    """
    Check if entity might be mislabeled and suggest correction.
    Uses summary + subjects keywords.
    """
    text = (
        entity.get("summary", "").lower() + " " +
        " ".join(entity.get("subjects", [])).lower()
    )

    for keywords, target_div in AUDIT_KEYWORDS["reclassify"]:
        if any(kw in text for kw in keywords):
            # Only reclassify if the current division is a generic parent
            # Don't reclassify if already in a specific sub-division
            current_int = int(div_code)
            target_int = int(target_div)
            # Only reclassify from parent to child (e.g., 260→261)
            parent = (current_int // 10) * 10
            target_parent = (target_int // 10) * 10
            if parent == target_parent and current_int == parent:
                return target_div
    return div_code


def extract_birth_location(born_str: str | None) -> str:
    """Extract location from birth string like '1879-12-14, Speyer'."""
    if not born_str:
        return ""
    parts = born_str.split(", ", 1)
    if len(parts) > 1:
        return parts[1].strip()
    return ""


def enrich_summary(entity: dict, div_code: str, div_heading: str) -> str:
    """
    Build a rich, contextual summary for a person entity.
    Preserves original Wikipedia/Wikidata descriptions where present.
    """
    name = entity["name"]
    summary = entity.get("summary", "")
    era = entity.get("era", "Classical")
    region = entity.get("region", "Global")
    born = entity.get("born", "")
    subjects = entity.get("subjects", [])

    birth_year = parse_birth_year(born)
    birth_location = extract_birth_location(born)

    # Check if summary is already rich (Wikipedia-sourced, not template)
    is_template = "was a notable figure in the category of" in summary
    has_wiki_content = (
        not is_template and
        len(summary) > 100 and
        "notable figure" not in summary.lower()
    )

    era_ctx = ERA_CONTEXT.get(era, "")
    region_ctx = REGION_CONTEXT.get(region, "")
    contribution = DIVISION_CONTRIBUTIONS.get(div_code, "their field of specialization")

    if has_wiki_content:
        # Already has good content — append contextual enrichment
        enrichment_parts = []

        # Add era context if not already mentioned
        if era.lower() not in summary.lower():
            enrichment_parts.append(
                f"Active {era_ctx}."
            )

        # Add contribution context
        enrichment_parts.append(
            f"Their legacy endures in the domain of {contribution}."
        )

        if enrichment_parts:
            enriched = summary.rstrip(". ") + ". " + " ".join(enrichment_parts)
        else:
            enriched = summary
    else:
        # Template or thin summary — build rich one
        parts = []

        # Opening with name and role
        if birth_year and birth_location:
            if birth_year < 0:
                parts.append(
                    f"{name} (born c. {abs(birth_year)} BCE, {birth_location}) "
                    f"was a distinguished {div_heading.lower()}"
                )
            else:
                parts.append(
                    f"{name} (born {abs(birth_year)}, {birth_location}) "
                    f"was a distinguished {div_heading.lower()}"
                )
        elif birth_year:
            if birth_year < 0:
                parts.append(
                    f"{name} (c. {abs(birth_year)} BCE) "
                    f"was a distinguished {div_heading.lower()}"
                )
            else:
                parts.append(
                    f"{name} (b. {abs(birth_year)}) "
                    f"was a distinguished {div_heading.lower()}"
                )
        elif birth_location:
            parts.append(
                f"{name}, from {birth_location}, "
                f"was a distinguished {div_heading.lower()}"
            )
        else:
            parts.append(
                f"{name} was a distinguished {div_heading.lower()}"
            )

        # Era context
        parts.append(f"who was active {era_ctx}")

        # Region context
        if region_ctx:
            parts[1] += f", {region_ctx}"

        # Contribution
        parts.append(
            f"Their work contributed to {contribution}"
        )

        # Assemble
        enriched = parts[0] + " " + parts[1] + ". " + parts[2] + "."

        # If original had any useful extra detail beyond template, try to preserve it
        if is_template:
            # Extract anything after the template pattern
            m = re.search(
                r"(?:broader historical (?:context|narrative)|codification of law)\.(.*)",
                summary,
                re.DOTALL
            )
            if m and m.group(1).strip():
                extra = m.group(1).strip()
                if len(extra) > 20:
                    enriched += " " + extra

    return enriched[:9900]


def main():
    root = Path(__file__).resolve().parent.parent
    people_path = root / "data" / "wikidata_people.json"

    print("=" * 70)
    print("  People JSON Enrichment — Annals of the World")
    print("=" * 70)

    print("\nLoading wikidata_people.json ...")
    with open(people_path, encoding="utf-8") as f:
        data = json.load(f)

    entities = data["entities"]
    print(f"  Loaded {len(entities)} entities")

    # ── Stats tracking ──
    enriched_count = 0
    division_fixes = 0
    sig_dist = Counter()
    div_counts = Counter()
    era_counts = Counter()
    continent_counts = Counter()

    print("\nEnriching entities ...")
    for i, entity in enumerate(entities):
        # 1. Extract divisionCode & divisionHeading
        cn = entity.get("callNumber", "200.unknown")
        div_code = extract_division(cn)

        # 2. Audit division assignment
        new_div = audit_division(entity, div_code)
        if new_div != div_code:
            old_div = div_code
            div_code = new_div
            # Update callNumber
            slug = entity["slug"]
            entity["callNumber"] = f"{div_code}.{slug}"
            # Update subjectHeadings
            new_heading = DIVISION_MAP.get(div_code, "People")
            entity["subjectHeadings"] = [
                f"People — {new_heading} — "
                f"{entity.get('region', 'Global')} — {entity.get('era', 'Classical')}"
            ]
            entity["subjects"] = [new_heading]
            division_fixes += 1

        div_heading = DIVISION_MAP.get(div_code, "People")

        # 3. Add divisionCode & divisionHeading
        entity["divisionCode"] = div_code
        entity["divisionHeading"] = div_heading

        # 4. Compute historicalSignificance
        entity["historicalSignificance"] = compute_significance(entity)

        # 5. Enrich summary
        old_summary = entity.get("summary", "")
        entity["summary"] = enrich_summary(entity, div_code, div_heading)
        if entity["summary"] != old_summary:
            enriched_count += 1

        # Track stats
        sig_dist[entity["historicalSignificance"]["label"]] += 1
        div_counts[div_code] += 1
        era_counts[entity.get("era", "Unknown")] += 1
        continent_counts[entity.get("continent", "Global")] += 1

        if (i + 1) % 50000 == 0:
            print(f"  Processed {i + 1}/{len(entities)} ...")

    print(f"\n  Enriched summaries: {enriched_count}")
    print(f"  Division fixes: {division_fixes}")

    # ── Recompute _meta ──
    print("\nRecomputing _meta ...")
    data["_meta"]["version"] = "3.0"
    data["_meta"]["generated"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    data["_meta"]["total_unique_entities"] = len(entities)
    data["_meta"]["division_counts"] = dict(sorted(div_counts.items()))
    data["_meta"]["era_counts"] = dict(sorted(era_counts.items()))
    data["_meta"]["continent_counts"] = dict(sorted(continent_counts.items()))
    data["_meta"]["significance_distribution"] = dict(sorted(sig_dist.items()))
    data["_meta"]["enrichment_stats"] = {
        "summaries_enriched": enriched_count,
        "divisions_fixed": division_fixes,
        "fields_added": ["divisionCode", "divisionHeading", "historicalSignificance"],
    }
    data["_meta"]["note"] = (
        "Comprehensive Wikidata people fetch v3.0 with enriched summaries, "
        "historicalSignificance scoring, divisionCode/divisionHeading fields, "
        "and audited division assignments. Covers all 38 Class 2 Person divisions."
    )

    # ── Write ──
    print(f"\nWriting enriched data to {people_path} ...")
    with open(people_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    size_mb = people_path.stat().st_size / (1024 * 1024)
    print(f"  Written: {size_mb:.1f} MB")
    print(f"  Total entities: {len(entities)}")

    # ── Summary ──
    print("\n" + "=" * 70)
    print("  Enrichment Complete")
    print("=" * 70)

    print(f"\n  Division counts:")
    for d in sorted(div_counts.keys()):
        print(f"    {d} ({DIVISION_MAP.get(d, '?')}): {div_counts[d]}")

    print(f"\n  Era counts:")
    for e in sorted(era_counts.keys()):
        print(f"    {e}: {era_counts[e]}")

    print(f"\n  Significance distribution:")
    for s in sorted(sig_dist.keys()):
        print(f"    {s}: {sig_dist[s]}")

    print(f"\n  Continent counts:")
    for c in sorted(continent_counts.keys()):
        print(f"    {c}: {continent_counts[c]}")


if __name__ == "__main__":
    main()
