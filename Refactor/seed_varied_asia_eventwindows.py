# Refactor/seed_varied_asia_eventwindows.py
import os
import sys
from pathlib import Path
from typing import Optional, Tuple

from neo4j import GraphDatabase
from neo4j.exceptions import AuthError, ServiceUnavailable

# -------------------- driver bootstrap (db.py first, then env) --------------------
def _import_project_driver():
    try:
        from db import get_neo4j_driver  # repo helper
        return get_neo4j_driver()
    except Exception:
        here = Path(__file__).resolve()
        candidates = [
            here.parent.parent,  # repo root if script in Refactor/
            Path("/home/manasa151/annals-of-the-world"),
        ]
        for c in candidates:
            if c.exists() and str(c) not in sys.path:
                sys.path.insert(0, str(c))
                try:
                    from db import get_neo4j_driver
                    return get_neo4j_driver()
                except Exception:
                    pass
        raise

def _load_env():
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except Exception:
        pass

def _parse_auth_from_env():
    uri = os.getenv("NEO4J_URI") or os.getenv("BOLT_URI") or "bolt://localhost:7687"
    auth_combo = os.getenv("NEO4J_AUTH")
    user = (
        os.getenv("NEO4J_USER")
        or os.getenv("NEO4J_USERNAME")
        or os.getenv("BOLT_USER")
        or (auth_combo.split("/", 1)[0] if auth_combo and "/" in auth_combo else None)
        or "neo4j"
    )
    pw = (
        os.getenv("NEO4J_PASSWORD")
        or os.getenv("NEO4J_PASS")
        or os.getenv("BOLT_PASSWORD")
        or (auth_combo.split("/", 1)[1] if auth_combo and "/" in auth_combo else None)
        or "neo4j"
    )
    db = os.getenv("NEO4J_DATABASE") or None
    return uri, user, pw, db

def _build_driver_from_env():
    _load_env()
    uri, user, pw, db = _parse_auth_from_env()
    driver = GraphDatabase.driver(uri, auth=(user, pw))
    return driver, db, uri, user

# -------------------- data: varied scopes & times --------------------
ALL_ASIA_REGIONS = [
    "Central Asia",
    "East Asia",
    "South Asia",
    "Southeast Asia",
    "West Asia / Middle East",
    "North Asia / Siberia",
    "Caucasus",
]

EVENTS = [
    # Continent-wide
    dict(slug="asian-decolonization", name="Decolonization in Asia",
         startYear=1945, endYear=1975, scope="continent", all_asia=True, regions=[]),

    # Multi-region events
    dict(slug="ww1-asia", name="World War I — Asia-Pacific",
         startYear=1914, endYear=1918, scope="multi-region", all_asia=False,
         regions=["West Asia / Middle East", "South Asia", "East Asia", "Southeast Asia", "Central Asia", "Caucasus"]),
    dict(slug="ww2-asia", name="World War II — Asia-Pacific",
         startYear=1937, endYear=1945, scope="multi-region", all_asia=False,
         regions=["East Asia", "Southeast Asia", "South Asia", "West Asia / Middle East"]),
    dict(slug="mongol-conquests-asia", name="Mongol Conquests across Asia",
         startYear=1206, endYear=1368, scope="multi-region", all_asia=False,
         regions=["Central Asia", "East Asia", "South Asia", "West Asia / Middle East", "North Asia / Siberia"]),
    dict(slug="black-death-asia", name="Black Death in Asia",
         startYear=1346, endYear=1353, scope="multi-region", all_asia=False,
         regions=["West Asia / Middle East", "Central Asia", "East Asia", "South Asia"]),
    dict(slug="silk-road-flourishing-han-tang", name="Silk Road Flourishing (Han–Tang Era)",
         startYear=-130, endYear=750, scope="multi-region", all_asia=False,
         regions=["Central Asia", "East Asia", "West Asia / Middle East"]),
    dict(slug="timurid-expansion", name="Timurid Expansion",
         startYear=1370, endYear=1507, scope="multi-region", all_asia=False,
         regions=["Central Asia", "West Asia / Middle East", "South Asia"]),

    # Single-region anchors
    dict(slug="partition-of-india-1947", name="Partition of India",
         startYear=1947, endYear=1947, scope="region", all_asia=False,
         regions=["South Asia"]),
    dict(slug="bangladesh-war-of-independence-1971", name="Bangladesh War of Independence",
         startYear=1971, endYear=1971, scope="region", all_asia=False,
         regions=["South Asia"]),
    dict(slug="green-revolution-india", name="Green Revolution in India",
         startYear=1965, endYear=1990, scope="region", all_asia=False,
         regions=["South Asia"]),
    dict(slug="meiji-industrialization-east-asia", name="Meiji Industrialization",
         startYear=1868, endYear=1912, scope="region", all_asia=False,
         regions=["East Asia"]),
    dict(slug="opium-wars-east-asia", name="Opium Wars in East Asia",
         startYear=1839, endYear=1860, scope="region", all_asia=False,
         regions=["East Asia"]),
]

# -------------------- cypher --------------------
Q_CONSTRAINT = """
CREATE CONSTRAINT eventwindow_slug_unique IF NOT EXISTS
FOR (w:EventWindow) REQUIRE w.slug IS UNIQUE;
"""

Q_UPSERT_AND_LINK = """
UNWIND $events AS e
MERGE (w:EventWindow {slug:e.slug})
ON CREATE SET
  w.name      = e.name,
  w.region    = 'Asia',
  w.startYear = e.startYear,
  w.endYear   = e.endYear,
  w.scope     = e.scope
SET
  w.name      = coalesce(w.name, e.name),
  w.region    = coalesce(w.region, 'Asia'),
  w.startYear = coalesce(w.startYear, e.startYear),
  w.endYear   = coalesce(w.endYear, e.endYear),
  w.scope     = coalesce(w.scope, e.scope)
WITH w, e, CASE WHEN e.all_asia THEN $allRegions ELSE e.regions END AS targetRegions
CALL {
  WITH w, targetRegions
  MATCH (per:Period)
  WHERE per.region IN targetRegions
  MERGE (w)-[r:OCCURS_DURING]->(per)
  ON CREATE SET r.framework = 'Event Context'
  RETURN count(*) AS linked
}
RETURN e.slug AS window, linked
ORDER BY window;
"""

Q_COUNTS_BY_REGION = """
MATCH (w:EventWindow)-[:OCCURS_DURING]->(per:Period)
WHERE w.slug IN $slugs
RETURN w.slug AS window, per.region AS region, count(*) AS links
ORDER BY window, region;
"""

# optional: a compact graph query you can paste into Neo4j Browser
GRAPH_QUERY = """
MATCH p=(w:EventWindow)-[:OCCURS_DURING]->(per:Period)
WHERE w.slug IN $slugs
RETURN p
ORDER BY w.slug, per.region;
"""

# -------------------- run helpers --------------------
def print_table(rows, cols):
    if not rows:
        print("(no rows)")
        return
    widths = [max(len(str(r.get(c, ""))) for r in rows + [{c: c}]) for c in cols]
    fmt = " | ".join("{:<" + str(w) + "}" for w in widths)
    print(fmt.format(*cols))
    print("-+-".join("-" * w for w in widths))
    for r in rows:
        print(fmt.format(*[str(r.get(c, "")) for c in cols]))

# -------------------- main --------------------
def main():
    # driver
    using_env = False
    uri = user = None
    try:
        driver = _import_project_driver()
        database = None
    except Exception:
        using_env = True
        driver, database, uri, user = _build_driver_from_env()

    # connectivity check
    try:
        driver.verify_connectivity()
    except AuthError:
        print("❌ Authentication failed.")
        if using_env:
            print(f"   URI={uri} USER={user} (password hidden).")
        else:
            print("   Using db.py; verify credentials there or set env vars.")
        raise
    except ServiceUnavailable:
        print("❌ Neo4j unreachable. Check URI/port and that the DB is running.")
        if using_env and uri:
            print(f"   Tried URI: {uri}")
        raise

    sess_kwargs = {"database": database} if database else {}
    with driver.session(**sess_kwargs) as session:
        # ensure constraint
        session.execute_write(lambda tx: tx.run(Q_CONSTRAINT))

        # upsert + link
        print("Seeding EventWindows and linking to Periods…")
        rows = session.execute_write(lambda tx: tx.run(
            Q_UPSERT_AND_LINK,
            events=EVENTS,
            allRegions=ALL_ASIA_REGIONS,
        ).data())
        print_table(rows, ["window", "linked"])

        # summary by region
        print("\nLinks by region:")
        slugs = [e["slug"] for e in EVENTS]
        rows = session.execute_read(lambda tx: tx.run(
            Q_COUNTS_BY_REGION, slugs=slugs
        ).data())
        print_table(rows, ["window", "region", "links"])

        # print a ready-to-paste graph query
        print("\nPaste this into Neo4j Browser to view the graph:")
        slug_list = ", ".join(f"'{s}'" for s in slugs)
        print(
            GRAPH_QUERY.replace("$slugs", f"[{slug_list}]").strip()
        )

    driver.close()

if __name__ == "__main__":
    main()
