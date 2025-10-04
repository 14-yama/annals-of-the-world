# Refactor/seed_eventwindows_master.py
import os
import sys
import csv
import argparse
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

from neo4j import GraphDatabase
from neo4j.exceptions import AuthError, ServiceUnavailable

# -------------------- driver bootstrap (db.py first, then env) --------------------
def _import_project_driver():
    """
    Try to import repo-local db.get_neo4j_driver() first; if that fails, fall back to env.
    """
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

# -------------------- Cypher (one statement per string) --------------------
BOOTSTRAP_STATEMENTS = [
    # EventWindow constraints / indexes
    "CREATE CONSTRAINT evw_slug_unique IF NOT EXISTS FOR (w:EventWindow) REQUIRE w.slug IS UNIQUE",
    "CREATE INDEX evw_region IF NOT EXISTS FOR (w:EventWindow) ON (w.region)",
    "CREATE INDEX evw_category IF NOT EXISTS FOR (w:EventWindow) ON (w.category)",
    "CREATE INDEX evw_scope IF NOT EXISTS FOR (w:EventWindow) ON (w.scope)",
    "CREATE INDEX evw_start IF NOT EXISTS FOR (w:EventWindow) ON (w.startYear)",
    "CREATE INDEX evw_end IF NOT EXISTS FOR (w:EventWindow) ON (w.endYear)",

    # Period expectations (we don't create periods here; just optimize lookups)
    "CREATE CONSTRAINT period_slug_unique IF NOT EXISTS FOR (p:Period) REQUIRE p.slug IS UNIQUE",
    "CREATE INDEX period_region IF NOT EXISTS FOR (p:Period) ON (p.region)",
    "CREATE INDEX period_start IF NOT EXISTS FOR (p:Period) ON (p.startYear)",
    "CREATE INDEX period_end IF NOT EXISTS FOR (p:Period) ON (p.endYear)",
]

Q_UPSERT_EVENTWINDOWS = """
UNWIND $rows AS r
WITH r
MERGE (w:EventWindow {slug: r.slug})
ON CREATE SET
  w.name      = r.name,
  w.startYear = toInteger(r.startYear),
  w.endYear   = CASE WHEN r.endYear IS NULL OR r.endYear = '' THEN NULL ELSE toInteger(r.endYear) END,
  w.region    = r.region,
  w.scope     = r.scope,
  w.category  = r.category
SET
  w.name      = coalesce(w.name, r.name),
  w.startYear = coalesce(w.startYear, toInteger(r.startYear)),
  w.endYear   = coalesce(w.endYear, CASE WHEN r.endYear IS NULL OR r.endYear = '' THEN NULL ELSE toInteger(r.endYear) END),
  w.region    = coalesce(w.region, r.region),
  w.scope     = coalesce(w.scope, r.scope),
  w.category  = coalesce(w.category, r.category)
RETURN w.slug AS slug
ORDER BY slug
"""

# Link EventWindow -> Period only within SAME region and time overlap
Q_LINK_OCCURS_DURING = """
UNWIND $slugs AS slug
MATCH (w:EventWindow {slug: slug})
MATCH (p:Period)
WHERE p.region = w.region
  AND w.startYear IS NOT NULL
  AND p.startYear IS NOT NULL
  AND coalesce(w.endYear, 9999) >= p.startYear
  AND coalesce(p.endYear, 9999) >= w.startYear
MERGE (w)-[r:OCCURS_DURING]->(p)
ON CREATE SET r.framework = 'Temporal Linkage'
RETURN slug AS event, count(p) AS linkedPeriods
ORDER BY event
"""

# EventWindow PRECEDES EventWindow — same region, chronological order
Q_LINK_PRECEDES = """
UNWIND $slugs AS slug
MATCH (a:EventWindow {slug: slug})
MATCH (b:EventWindow)
WHERE b.slug <> a.slug
  AND a.region = b.region
  AND a.startYear IS NOT NULL AND b.startYear IS NOT NULL
  AND coalesce(a.endYear, a.startYear) <= b.startYear
  // prevent dense cliques: don't duplicate if reverse or existing
  AND NOT (a)-[:PRECEDES]->(b)
MERGE (a)-[r:PRECEDES]->(b)
ON CREATE SET r.framework = 'Temporal Linkage'
RETURN slug AS fromSlug, count(*) AS created
ORDER BY fromSlug
"""

# Small helper queries
Q_COUNT_EVENTS = "MATCH (w:EventWindow) RETURN count(w) AS n"
Q_SAMPLE_EVENTS = "MATCH (w:EventWindow) RETURN w.slug AS slug, w.region AS region, w.startYear AS s, w.endYear AS e LIMIT 10"

# -------------------- CSV utils --------------------
REQUIRED_HEADERS = ["slug", "name", "startYear", "endYear", "region", "scope", "category"]

def read_csv_rows(csv_path: Path) -> List[Dict[str, Any]]:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found: {csv_path}")
    rows: List[Dict[str, Any]] = []
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=",")
        headers = [h.strip() for h in reader.fieldnames or []]
        missing = [h for h in REQUIRED_HEADERS if h not in headers]
        if missing:
            raise ValueError(f"CSV is missing required headers: {missing}\nFound: {headers}")
        for r in reader:
            # Normalize & strip
            clean = {k: (v.strip() if isinstance(v, str) else v) for k, v in r.items()}
            # Mild region normalization (optional; keep exact values otherwise)
            clean["region"] = clean.get("region") or "Asia"
            rows.append(clean)
    return rows

# -------------------- table printer --------------------
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
    parser = argparse.ArgumentParser(description="Seed EventWindows (master CSV) into Neo4j.")
    parser.add_argument("--csv", default="Asian-Event_Window/master-events.csv",
                        help="Path to CSV (default: Asian-Event_Window/master-events.csv)")
    # Flags default ON per your request
    parser.add_argument("--with-periods", action="store_true", default=True,
                        help="Link (:EventWindow)-[:OCCURS_DURING]->(:Period) within same region (default ON).")
    parser.add_argument("--no-periods", action="store_true", default=False,
                        help="Disable linking to Periods (overrides --with-periods).")
    parser.add_argument("--with-precedes", action="store_true", default=True,
                        help="Create PRECEDES links within same region (default ON).")
    parser.add_argument("--no-precedes", action="store_true", default=False,
                        help="Disable PRECEDES linking (overrides --with-precedes).")
    args = parser.parse_args()

    # Resolve toggles
    link_periods = args.with_periods and not args.no_periods
    link_precedes = args.with_precedes and not args.no_precedes

    # Build / import driver
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

    # load CSV
    csv_path = Path(args.csv)
    print(f"Reading CSV: {csv_path}")
    rows = read_csv_rows(csv_path)
    print(f"Loaded {len(rows)} rows.")

    sess_kwargs = {"database": database} if database else {}
    with driver.session(**sess_kwargs) as session:
        # bootstrap, one statement per run
        print("Bootstrapping constraints/indexes…")
        for stmt in BOOTSTRAP_STATEMENTS:
            session.execute_write(lambda tx, q=stmt: tx.run(q))

        # upsert windows
        print("Upserting :EventWindow nodes…")
        up_rows = session.execute_write(lambda tx: tx.run(
            Q_UPSERT_EVENTWINDOWS, rows=rows
        ).data())
        print_table(up_rows, ["slug"])

        # Optionals
        if link_periods:
            print("\nLinking OCCURS_DURING within same region & overlapping time…")
            slugs = [r["slug"] for r in up_rows]
            link_rows = session.execute_write(lambda tx: tx.run(
                Q_LINK_OCCURS_DURING, slugs=slugs
            ).data())
            print_table(link_rows, ["event", "linkedPeriods"])

        if link_precedes:
            print("\nLinking PRECEDES within same region (a.endYear <= b.startYear)…")
            slugs = [r["slug"] for r in up_rows]
            pr_rows = session.execute_write(lambda tx: tx.run(
                Q_LINK_PRECEDES, slugs=slugs
            ).data())
            print_table(pr_rows, ["fromSlug", "created"])

        # summary
        print("\nSummary:")
        c = session.execute_read(lambda tx: tx.run(Q_COUNT_EVENTS).data())
        print_table(c, ["n"])

        sample = session.execute_read(lambda tx: tx.run(Q_SAMPLE_EVENTS).data())
        print("\nSample :EventWindow rows:")
        print_table(sample, ["slug", "region", "s", "e"])

    driver.close()
    print("\n✅ Done.")

if __name__ == "__main__":
    main()
