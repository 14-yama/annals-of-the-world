#!/usr/bin/env python3
"""
patch_movements_gaps.py

Fills 4 missing divisions in wikidata_movements.json with
manually-researched entries:
  626 Disability Rights & Inclusion
  651 Scientific Revolution
  652 Empiricism & Positivism
  682 Maritime Trade & Age of Sail

These divisions have no Wikidata P31-instantiable types; entries are
hand-curated from well-known historical movements and organisations.

Usage:
    python3 scripts/patch_movements_gaps.py
"""

import json
import time
from pathlib import Path


def make_entity(
    slug: str,
    name: str,
    div_code: str,
    div_heading: str,
    summary: str,
    era: str,
    era_slug: str,
    country: str,
    region: str,
    continent: str,
    start_year: int | None = None,
    end_year: int | None = None,
    qid: str | None = None,
    significance: int = 5,
) -> dict:
    sig_labels = {1: "Minor", 2: "Minor", 3: "Moderate", 4: "Moderate",
                  5: "Notable", 6: "Notable", 7: "Major", 8: "Major",
                  9: "Landmark", 10: "Landmark"}
    entity = {
        "slug": slug,
        "name": name,
        "label": "Movement",
        "callNumber": f"{div_code}.{slug}",
        "subjectHeadings": [f"Movements -- {div_heading} -- {country} -- {era}"],
        "subjects": [s for s in [country, continent, div_heading] if s and s != "Global"],
        "summary": summary,
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
        "movementType": "social movement",
        "divisionCode": div_code,
        "divisionHeading": div_heading,
        "historicalSignificance": {
            "score": significance,
            "label": sig_labels[significance],
            "sitelinks": 0,
        },
        "inAppwrite": False,
    }
    if start_year is not None:
        entity["startYear"] = start_year
    if end_year is not None:
        entity["endYear"] = end_year
    if qid:
        entity["wikidataQid"] = qid
    if country and country != "Global":
        entity["relationships"].append({
            "sourceSlug": slug, "sourceName": name,
            "verb": "OCCURS_IN",
            "targetSlug": f"country-{slug.split('-')[-1]}" if "-" in slug else "",
            "targetName": country,
            "context": f"{name} originated in {country}",
        })
        entity["places"].append({"name": country, "role": "Country"})
    return entity


GAP_ENTITIES = [
    # ── 626 Disability Rights & Inclusion ──
    make_entity(
        "independent-living-movement", "Independent Living Movement",
        "626", "Disability Rights & Inclusion",
        "Founded in the 1960s–70s by Ed Roberts and others at UC Berkeley, the Independent Living Movement asserted that people with disabilities should have control over their own lives. It led to the creation of Centers for Independent Living worldwide and influenced the Americans with Disabilities Act.",
        "Contemporary", "contemporary", "United States", "North America", "Americas",
        start_year=1962, qid="Q6017030", significance=7,
    ),
    make_entity(
        "disability-rights-movement", "Disability Rights Movement",
        "626", "Disability Rights & Inclusion",
        "A broad social movement advocating civil rights, equal opportunity, and anti-discrimination legislation for people with disabilities. Emerged in the 1960s, it secured landmark legislation including the ADA (1990), the UK Disability Discrimination Act (1995), and the UN Convention on the Rights of Persons with Disabilities (2006).",
        "Contemporary", "contemporary", "Global", "Global", "Global",
        start_year=1960, qid="Q50726037", significance=8,
    ),
    make_entity(
        "deaf-culture-movement", "Deaf Culture Movement",
        "626", "Disability Rights & Inclusion",
        "A cultural and political movement asserting the identity, language rights, and cultural heritage of Deaf communities. Advocates for sign language recognition, Deaf education, and the view of deafness as a cultural difference rather than a disability.",
        "Contemporary", "contemporary", "United States", "North America", "Americas",
        start_year=1960, qid="Q3462104", significance=6,
    ),
    make_entity(
        "neurodiversity-movement", "Neurodiversity Movement",
        "626", "Disability Rights & Inclusion",
        "A social movement that frames neurological differences such as autism, ADHD, and dyslexia as natural variations of the human genome rather than disorders to be cured. Coined by Judy Singer in 1998, it advocates for inclusion and accommodation.",
        "Contemporary", "contemporary", "Global", "Global", "Global",
        start_year=1998, qid="Q1758977", significance=6,
    ),
    make_entity(
        "adapt-disability-advocacy", "ADAPT (American Disabled for Attendant Programs Today)",
        "626", "Disability Rights & Inclusion",
        "A grassroots disability rights organization in the United States known for direct action protests. Founded in 1983 by Wade Blank, ADAPT campaigned for accessible public transit and community-based attendant services.",
        "Contemporary", "contemporary", "United States", "North America", "Americas",
        start_year=1983, qid="Q4651587", significance=5,
    ),
    make_entity(
        "section-504-sit-in", "Section 504 Sit-In",
        "626", "Disability Rights & Inclusion",
        "A 1977 sit-in at the San Francisco Federal Building, lasting 25 days, demanding enforcement of Section 504 of the Rehabilitation Act. Led by Judith Heumann and disability activists, it became the longest occupation of a federal building and a landmark in disability rights history.",
        "Contemporary", "contemporary", "United States", "North America", "Americas",
        start_year=1977, end_year=1977, significance=6,
    ),

    # ── 651 Scientific Revolution ──
    make_entity(
        "scientific-revolution", "Scientific Revolution",
        "651", "Scientific Revolution",
        "A period of major scientific transformation in Europe from roughly 1543 to 1687, with discoveries by Copernicus, Galileo, Kepler, and Newton fundamentally changing understanding of the natural world. Established the modern scientific method and institutions like the Royal Society.",
        "Early Modern", "early-modern", "Global", "Global", "Global",
        start_year=1543, end_year=1687, qid="Q18271", significance=10,
    ),
    make_entity(
        "copernican-revolution", "Copernican Revolution",
        "651", "Scientific Revolution",
        "The paradigm shift from the geocentric Ptolemaic model to the heliocentric model proposed by Nicolaus Copernicus in De revolutionibus orbium coelestium (1543). This revolution in astronomy transformed cosmology and laid the foundation for modern physics.",
        "Early Modern", "early-modern", "Poland", "Eastern Europe", "Europe",
        start_year=1543, qid="Q482543", significance=9,
    ),
    make_entity(
        "baconian-method", "Baconian Method",
        "651", "Scientific Revolution",
        "The empirical scientific method advocated by Francis Bacon in Novum Organum (1620), emphasizing observation, experimentation, and inductive reasoning. Bacon's framework became foundational for the Royal Society and modern experimental science.",
        "Early Modern", "early-modern", "United Kingdom", "Northern Europe", "Europe",
        start_year=1620, qid="Q16886049", significance=7,
    ),
    make_entity(
        "royal-society-movement", "Royal Society and Scientific Societies",
        "651", "Scientific Revolution",
        "The founding of the Royal Society of London (1660) and similar national academies across Europe represented the institutionalization of the scientific method. These societies promoted peer review, experimental replication, and the dissemination of knowledge.",
        "Early Modern", "early-modern", "United Kingdom", "Northern Europe", "Europe",
        start_year=1660, qid="Q123885", significance=8,
    ),
    make_entity(
        "mechanical-philosophy", "Mechanical Philosophy",
        "651", "Scientific Revolution",
        "A dominant intellectual movement of the 17th century that sought to explain all natural phenomena through matter and motion alone, rejecting Aristotelian forms. Key proponents included Descartes, Boyle, and Gassendi.",
        "Early Modern", "early-modern", "Global", "Global", "Global",
        start_year=1620, end_year=1700, qid="Q1706411", significance=7,
    ),

    # ── 652 Empiricism & Positivism ──
    make_entity(
        "british-empiricism", "British Empiricism",
        "652", "Empiricism & Positivism",
        "A philosophical tradition holding that knowledge comes primarily from sensory experience. Its principal figures — John Locke, George Berkeley, and David Hume — argued against innate ideas and shaped epistemology, political philosophy, and the scientific method.",
        "Early Modern", "early-modern", "United Kingdom", "Northern Europe", "Europe",
        start_year=1689, end_year=1776, qid="Q185404", significance=8,
    ),
    make_entity(
        "logical-positivism", "Logical Positivism (Vienna Circle)",
        "652", "Empiricism & Positivism",
        "A philosophical movement originating in 1920s Vienna that combined empiricism with formal logic. The Vienna Circle (Schlick, Carnap, Neurath) promoted the verification principle: only statements verifiable through observation or logic are meaningful. Deeply influenced analytic philosophy and the philosophy of science.",
        "Modern", "modern", "Austria", "Western Europe", "Europe",
        start_year=1924, end_year=1936, qid="Q131680", significance=8,
    ),
    make_entity(
        "positivism-comte", "Positivism (Auguste Comte)",
        "652", "Empiricism & Positivism",
        "A philosophical system founded by Auguste Comte in the 1830s, asserting that valid knowledge is found only in scientific observation. Comte's law of three stages (theological, metaphysical, positive) and his founding of sociology made positivism one of the most influential intellectual movements of the 19th century.",
        "Modern", "modern", "France", "Western Europe", "Europe",
        start_year=1830, qid="Q205985", significance=7,
    ),
    make_entity(
        "pragmatism", "Pragmatism",
        "652", "Empiricism & Positivism",
        "An American philosophical tradition founded by Charles Sanders Peirce, William James, and John Dewey in the late 19th century. Pragmatism evaluates ideas by their practical consequences and empirical outcomes, bridging empiricism and action.",
        "Modern", "modern", "United States", "North America", "Americas",
        start_year=1878, qid="Q271875", significance=7,
    ),
    make_entity(
        "logical-empiricism", "Logical Empiricism",
        "652", "Empiricism & Positivism",
        "A refinement of logical positivism developed by Hans Reichenbach, Carl Hempel, and Rudolf Carnap after emigrating from Europe to the United States. Relaxed the strict verification principle while maintaining commitment to empirical science and formal logic.",
        "Modern", "modern", "United States", "North America", "Americas",
        start_year=1936, qid="Q131680", significance=6,
    ),

    # ── 682 Maritime Trade & Age of Sail ──
    make_entity(
        "portuguese-age-of-discovery", "Portuguese Age of Discovery",
        "682", "Maritime Trade & Age of Sail",
        "Portugal's maritime exploration movement beginning with Prince Henry the Navigator in the early 15th century. Portuguese sailors charted the African coast, discovered the sea route to India (Vasco da Gama, 1498), and established a global trading empire connecting Europe, Africa, Asia, and Brazil.",
        "Early Modern", "early-modern", "Portugal", "Southern Europe", "Europe",
        start_year=1415, end_year=1543, qid="Q133602", significance=9,
    ),
    make_entity(
        "spanish-maritime-exploration", "Spanish Maritime Exploration",
        "682", "Maritime Trade & Age of Sail",
        "Spain's maritime expansion beginning with Columbus's 1492 voyage, establishing trade routes and colonial networks across the Americas, the Philippines, and the Pacific. The Manila Galleon trade (1565–1815) connected Asia to the Americas.",
        "Early Modern", "early-modern", "Spain", "Southern Europe", "Europe",
        start_year=1492, end_year=1815, significance=9,
    ),
    make_entity(
        "dutch-golden-age-trade", "Dutch Golden Age Maritime Trade",
        "682", "Maritime Trade & Age of Sail",
        "The Netherlands became the world's foremost maritime trading power in the 17th century through the Dutch East India Company (VOC) and Dutch West India Company. Dutch traders dominated the spice trade, established colonies, and pioneered financial instruments like stock exchanges.",
        "Early Modern", "early-modern", "Netherlands", "Western Europe", "Europe",
        start_year=1602, end_year=1700, qid="Q12541", significance=8,
    ),
    make_entity(
        "british-east-india-trade", "British East India Trade",
        "682", "Maritime Trade & Age of Sail",
        "The British East India Company (founded 1600) and the broader British maritime trade network that connected Britain to India, China, and Southeast Asia. By the 18th century, Britain controlled the world's largest maritime trading empire, fundamentally shaping global commerce.",
        "Early Modern", "early-modern", "United Kingdom", "Northern Europe", "Europe",
        start_year=1600, end_year=1874, qid="Q83164", significance=8,
    ),
    make_entity(
        "hanseatic-league-trade", "Hanseatic League Maritime Trade",
        "682", "Maritime Trade & Age of Sail",
        "A medieval confederation of merchant guilds and market towns in Northern Europe (13th–17th century). The Hanse dominated Baltic and North Sea trade, establishing trading posts from Novgorod to London and creating early forms of commercial law and diplomatic relations.",
        "Medieval", "medieval", "Germany", "Western Europe", "Europe",
        start_year=1200, end_year=1669, qid="Q38130", significance=8,
    ),
    make_entity(
        "indian-ocean-trade-network", "Indian Ocean Trade Network",
        "682", "Maritime Trade & Age of Sail",
        "A vast pre-modern maritime trade system connecting East Africa, the Arabian Peninsula, India, Southeast Asia, and China. Active since antiquity and peaking in the medieval period, it facilitated exchange of spices, textiles, precious metals, and cultural ideas across civilizations.",
        "Medieval", "medieval", "Global", "Global", "Global",
        start_year=-300, end_year=1500, qid="Q1235914", significance=9,
    ),
    make_entity(
        "age-of-sail", "Age of Sail",
        "682", "Maritime Trade & Age of Sail",
        "The period from the 16th to mid-19th century when international trade and naval warfare were dominated by sailing ships. Encompassing exploration, colonialism, piracy, and the transatlantic slave trade, it transformed global demographics, economies, and power structures.",
        "Early Modern", "early-modern", "Global", "Global", "Global",
        start_year=1500, end_year=1850, qid="Q173181", significance=9,
    ),
]


def main():
    project_root = Path(__file__).resolve().parent.parent
    movements_path = project_root / "data" / "wikidata_movements.json"

    if not movements_path.exists():
        print(f"ERROR: {movements_path} not found.")
        return

    with open(movements_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    existing_slugs = {e["slug"] for e in data["entities"]}
    print(f"Existing entities: {len(data['entities'])}")
    print(f"Existing slugs:    {len(existing_slugs)}")

    added = 0
    skipped = 0
    for entity in GAP_ENTITIES:
        if entity["slug"] in existing_slugs:
            print(f"  SKIP (dup): {entity['slug']}")
            skipped += 1
            continue
        data["entities"].append(entity)
        existing_slugs.add(entity["slug"])
        added += 1
        print(f"  ADD [{entity['divisionCode']}]: {entity['name']}")

    # Update _meta
    data["_meta"]["total_unique_entities"] = len(data["entities"])
    data["_meta"]["patched"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    data["_meta"]["gap_divisions_filled"] = ["626", "651", "652", "682"]
    data["_meta"]["note"] += " Gap divisions (626, 651, 652, 682) filled with hand-curated entries."

    # Recount divisions
    div_counts: dict[str, int] = {}
    for e in data["entities"]:
        div = e["callNumber"][:3]
        div_counts[div] = div_counts.get(div, 0) + 1
    data["_meta"]["division_counts"] = dict(sorted(div_counts.items()))

    # Write back
    with open(movements_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\nDone. Added: {added}, Skipped: {skipped}")
    print(f"Total entities: {len(data['entities'])}")
    print(f"\nGap division counts:")
    for div in ["626", "651", "652", "682"]:
        print(f"  {div}: {div_counts.get(div, 0)}")


if __name__ == "__main__":
    main()
