# Refactor/canonicalize_event_windows.py
import os
import sys
from pathlib import Path
from typing import Optional, Tuple

from neo4j import GraphDatabase
from neo4j.exceptions import AuthError, ServiceUnavailable

# --- Try project helper first (db.py) ---------------------------------------
def _import_project_driver():
    """
    Try to import get_neo4j_driver from the repo's db.py, adding common roots
    to sys.path if needed. Returns a driver or raises ImportError.
    """
    try:
        from db import get_neo4j_driver  # noqa
        return get_neo4j_driver()
    except Exception:
        # Try adding repo root two levels up from this file (…/annals-of-the-world/)
        here = Path(__file__).resolve()
        candidates = [
            here.parent.parent,                 # repo root if script in Refactor/
            here.parent.parent.parent,          # just in case
            Path("/home/manasa151/annals-of-the-world"),  # your absolute repo path
        ]
        for c in candidates:
            if str(c) not in sys.path and c.exists():
                sys.path.insert(0, str(c))
                try:
                    from db import get_neo4j_driver  # noqa
                    return get_neo4j_driver()
                except Exception:
                    continue
        raise ImportError("Could not import get_neo4j_driver from db.py")


# --- Env-based auth fallback (mirrors asia_periods_patch style) -------------
def _load_env():
    try:
        # Optional .env support
        from dotenv import load_dotenv
        load_dotenv()
    except Exception:
        pass  # it's fine if python-dotenv isn't installed

def _parse_auth_from_env() -> Tuple[str, str, str, Optional[str]]:
    """
    Pulls Neo4j connection info from environment variables with generous fallbacks.
    Returns (uri, user, password, database).
    """
    uri = (
        os.getenv("NEO4J_URI")
        or os.getenv("BOLT_URI")
        or "bolt://localhost:7687"
    )
    # Support NEO4J_AUTH="user/password"
    auth_combo = os.getenv("NEO4J_AUTH")
    user = (
        os.getenv("NEO4J_USER")
        or os.getenv("NEO4J_USERNAME")
        or os.getenv("BOLT_USER")
        or (auth_combo.split("/", 1)[0] if auth_combo and "/" in auth_combo else None)
        or "neo4j"
    )
    password = (
        os.getenv("NEO4J_PASSWORD")
        or os.getenv("NEO4J_PASS")
        or os.getenv("BOLT_PASSWORD")
        or (auth_combo.split("/", 1)[1] if auth_combo and "/" in auth_combo else None)
        or "neo4j"
    )
    database = os.getenv("NEO4J_DATABASE") or None
    return uri, user, password, database

def _build_driver_from_env():
    _load_env()
    uri, user, password, database = _parse_auth_from_env()
    driver = GraphDatabase.driver(uri, auth=(user, password))
    return driver, database, uri, user


# --- Cypher ---------------------------------------------------------------
Q_CREATE_CONSTRAINT = """
CREATE CONSTRAINT eventwindow_slug_unique IF NOT EXISTS
FOR (w:EventWindow) REQUIRE w.slug IS UNIQUE;
"""

Q_COUNTS = """
MATCH (w:EventWindow)-[:OCCURS_DURING]->(:Period)
RETURN w.slug AS window, count(*) AS links
ORDER BY links DESC, window;
"""

Q_CANONICALIZE = """
WITH $renames AS renames
UNWIND renames AS m
MATCH (old:EventWindow {slug:m.from})
MERGE (nw:EventWindow {slug:m.to})
ON CREATE SET
  nw.name   = m.name,
  nw.region = 'Asia'
SET
  nw.name   = coalesce(nw.name, old.name),
  nw.region = coalesce(nw.region, old.region, 'Asia')
WITH old, nw
CALL {
  WITH old, nw
  MATCH (old)-[r:OCCURS_DURING]->(p:Period)
  MERGE (nw)-[nr:OCCURS_DURING]->(p)
  ON CREATE SET nr.framework = coalesce(r.framework, 'Event Context')
  SET nr += properties(r)    // Neo4j 5+ way to copy rel props
  DELETE r
  RETURN count(*) AS moved_out
}
CALL {
  WITH old, nw
  MATCH (p:Period)-[r:OCCURS_DURING]->(old)
  MERGE (p)-[nr:OCCURS_DURING]->(nw)
  ON CREATE SET nr.framework = coalesce(r.framework, 'Event Context')
  SET nr += properties(r)
  DELETE r
  RETURN count(*) AS moved_in
}
WITH old
DETACH DELETE old
RETURN 'ok' AS done;
"""

Q_LINGERING = """
MATCH (w:EventWindow)
WHERE w.slug IN ['world-war-i-asia','world-war-ii-asia','decolonization-asia']
RETURN w.slug AS duplicate_present;
"""

RENAMES = [
    {"from": "world-war-i-asia",    "to": "ww1-asia",             "name": "World War I — Asia-Pacific"},
    {"from": "world-war-ii-asia",   "to": "ww2-asia",             "name": "World War II — Asia-Pacific"},
    {"from": "decolonization-asia", "to": "asian-decolonization", "name": "Decolonization in Asia"},
]
CANONICAL = ["ww1-asia", "ww2-asia", "asian-decolonization"]


# --- Helpers --------------------------------------------------------------
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

def run_read(session, q, **params):
    return session.run(q, **params).data()

def run_write(session, q, **params):
    return session.run(q, **params).data()


# --- Main -----------------------------------------------------------------
def main():
    # 1) Build driver (db.py first, then env fallback)
    driver = None
    database = None
    using_env = False
    uri = None
    user = None

    try:
        driver = _import_project_driver()
    except ImportError:
        using_env = True
        driver, database, uri, user = _build_driver_from_env()

    # 2) Verify connectivity (and catch auth issues clearly)
    try:
        driver.verify_connectivity()
    except AuthError as e:
        print("❌ Neo4j authentication failed.")
        if using_env:
            print("   Checked env vars. Current settings:")
            print(f"   URI: {uri}")
            print(f"   USER: {user}")
            print("   PASS: (hidden)")
            print("   Tip: set NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD (or NEO4J_AUTH='user/password').")
        else:
            print("   Tried using project db.get_neo4j_driver().")
            print("   Tip: confirm credentials in db.py or fall back to env vars.")
        raise

    except ServiceUnavailable as e:
        print("❌ Could not reach Neo4j service. Is it running and is the URI correct?")
        if using_env and uri:
            print(f"   URI tried: {uri}")
        raise

    # 3) Run canonicalization
    sess_kwargs = {"database": database} if database else {}
    with driver.session(**sess_kwargs) as session:
        # constraint
        session.execute_write(lambda tx: tx.run(Q_CREATE_CONSTRAINT))

        print("Before (window → links):")
        rows = session.execute_read(lambda tx: tx.run(Q_COUNTS).data())
        print_table(rows, ["window", "links"])

        print("\nCanonicalizing duplicate EventWindows…")
        session.execute_write(lambda tx: tx.run(Q_CANONICALIZE, renames=RENAMES))

        print("\nAfter (window → links):")
        rows = session.execute_read(lambda tx: tx.run(Q_COUNTS).data())
        print_table(rows, ["window", "links"])

        lingering = session.execute_read(lambda tx: tx.run(Q_LINGERING).data())
        if lingering:
            print("\n⚠️ Still found duplicate-form slugs:")
            print_table(lingering, ["duplicate_present"])
        else:
            print("\n✅ No lingering duplicate-form slugs. Canonical windows present:")
            print(", ".join(CANONICAL))

    driver.close()


if __name__ == "__main__":
    main()
