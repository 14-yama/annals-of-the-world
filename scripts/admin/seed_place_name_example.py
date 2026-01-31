#!/usr/bin/env python3
"""Seed a small, meaningful example showing PlaceName (historical names) linked to a stable Place.

Creates:
- Place: Jerusalem (stable identity)
- PlaceName variants: Jebus, Jerusalem (Hebrew), Aelia Capitolina, Jerusalem (modern)
- People: David, Hadrian
- Institutions: Kingdom of Israel, Roman Empire
- Events: David captures Jebus; Hadrian renames Jerusalem

Key pattern:
- Events attach to (:Place {slug: ...}) via [:OCCURS_IN]
- Historical names attach via (:Place)-[:HAS_NAME]->(:PlaceName)

By default this script prints Cypher (dry-run). Use --run to write to Neo4j.

Usage:
  python scripts/admin/seed_place_name_example.py
  python scripts/admin/seed_place_name_example.py --run
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from db import get_neo4j_driver


CYTHER_SEED = dedent(
    """
    // ----------------------------
    // Stable Place identity
    // ----------------------------
    MERGE (p:Place {slug:"jerusalem"})
    SET p.name = "Jerusalem",
        p.kind = "city",
        p.wikidata_id = "Q1218";

    // ----------------------------
    // PlaceName variants (time-scoped)
    // ----------------------------
    MERGE (n1:PlaceName {slug:"jebus"})
    SET n1.name="Jebus", n1.lang="und", n1.script="Latn", n1.startYear=-3000, n1.endYear=-1000;

    MERGE (n2:PlaceName {slug:"jerusalem_he"})
    SET n2.name="Jerusalem", n2.lang="he", n2.script="Latn", n2.startYear=-1000, n2.endYear=135;

    MERGE (n3:PlaceName {slug:"aelia-capitolina"})
    SET n3.name="Aelia Capitolina", n3.lang="la", n3.script="Latn", n3.startYear=135, n3.endYear=638;

    MERGE (n4:PlaceName {slug:"jerusalem_modern"})
    SET n4.name="Jerusalem", n4.lang="en", n4.script="Latn", n4.startYear=638;
    // Note: omit endYear entirely for "present" instead of setting endYear=null

    // ----------------------------
    // HAS_NAME edges (MERGE then SET — safe even when endYear is missing)
    // ----------------------------
    MERGE (p)-[r1:HAS_NAME]->(n1)
    SET r1.startYear = n1.startYear,
        r1.endYear   = n1.endYear;

    MERGE (p)-[r2:HAS_NAME]->(n2)
    SET r2.startYear = n2.startYear,
        r2.endYear   = n2.endYear;

    MERGE (p)-[r3:HAS_NAME]->(n3)
    SET r3.startYear = n3.startYear,
        r3.endYear   = n3.endYear;

    MERGE (p)-[r4:HAS_NAME]->(n4)
    SET r4.startYear  = n4.startYear,
        r4.is_primary = true;

    // ----------------------------
    // Add a few meaningful nodes
    // ----------------------------
    MERGE (d:Person {slug:"david"})
    SET d.name="David";

    MERGE (h:Person {slug:"hadrian"})
    SET h.name="Hadrian";

    MERGE (k:Institution {slug:"kingdom-of-israel"})
    SET k.name="Kingdom of Israel";

    MERGE (re:Institution {slug:"roman-empire"})
    SET re.name="Roman Empire";

    // ----------------------------
    // Events that always point to the stable Place
    // ----------------------------
    MERGE (e1:Event {slug:"david-captures-jebus"})
    SET e1.name="David captures Jebus",
        e1.kind="War",
        e1.startYear=-1000;

    MERGE (e2:Event {slug:"hadrian-renames-jerusalem_135"})
    SET e2.name="Hadrian renames Jerusalem (Aelia Capitolina)",
        e2.kind="Decree",
        e2.startYear=135;

    MERGE (e1)-[:OCCURS_IN]->(p);
    MERGE (e2)-[:OCCURS_IN]->(p);

    // Participation / institutional context
    MERGE (d)-[:PARTICIPATES_IN {role:"leader"}]->(e1);
    MERGE (h)-[:PARTICIPATES_IN {role:"emperor"}]->(e2);

    MERGE (d)-[:LEADS]->(k);
    MERGE (h)-[:LEADS]->(re);

    // Optional: tie institutions to the events (using verbs already common in the graph)
    MERGE (k)-[:ORGANIZES]->(e1);
    MERGE (re)-[:PROMULGATES]->(e2);
    """
).strip()


Q_EVENTS_BY_HISTORIC_NAME = dedent(
    """
    // "Show events when it was called Jebus"
    MATCH (pn:PlaceName {name:"Jebus"})<-[:HAS_NAME]-(p:Place)
    MATCH (e:Event)-[:OCCURS_IN]->(p)
    WHERE e.startYear IS NULL
       OR pn.startYear IS NULL
       OR (e.startYear >= pn.startYear AND (pn.endYear IS NULL OR e.startYear < pn.endYear))
    RETURN pn.name AS historic_name, p.slug AS place_slug, p.name AS place_name, e.slug AS event_slug, e.name AS event_name, e.startYear AS year
    ORDER BY year;
    """
).strip()


Q_GRAPH_PATH = dedent(
    """
    // Visualization path: PlaceName -> Place -> Events
    MATCH path = (pn:PlaceName {name:"Jebus"})<-[:HAS_NAME]-(p:Place)<-[:OCCURS_IN]-(e:Event)
    RETURN path
    LIMIT 25;
    """
).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Seed PlaceName example (Jerusalem/Jebus).")
    parser.add_argument("--run", action="store_true", help="Execute against Neo4j (default is dry-run printing Cypher)")
    args = parser.parse_args()

    print("\n=== PlaceName Example Seed (Jerusalem/Jebus) ===\n")

    if not args.run:
        print("--- SEED CYPHER (copy/paste into Neo4j Browser) ---\n")
        print(CYTHER_SEED)
        print("\n--- QUERY: events by historic name ---\n")
        print(Q_EVENTS_BY_HISTORIC_NAME)
        print("\n--- QUERY: visualization path ---\n")
        print(Q_GRAPH_PATH)
        print("\n(dry-run) Not writing to Neo4j. Re-run with --run to execute.\n")
        return 0

    driver = get_neo4j_driver()
    try:
        with driver.session() as session:
            # Neo4j server expects a single statement per run; split the seed script
            statements = [s.strip() for s in CYTHER_SEED.split(';') if s.strip()]
            for stmt in statements:
                session.run(stmt)
            rows = list(session.run(Q_EVENTS_BY_HISTORIC_NAME))

        print("Wrote example data to Neo4j.")
        print("\nSample result: events resolved from historic name 'Jebus'\n")
        for r in rows:
            print(f"- {r['historic_name']} -> {r['place_name']} :: {r['event_name']} ({r.get('year')})")
        return 0
    finally:
        driver.close()


if __name__ == "__main__":
    raise SystemExit(main())
