"""Run audit queries and write a JSON report.

This script is tolerant if the neo4j driver is not installed or no DB is configured.
It loads a hard-coded set of queries (kept small) mirroring `docs/guidelines/audit_queries.md`.
"""
import json
from datetime import datetime
from pathlib import Path

QUERIES = {
    "missing_framed_by": "MATCH (e:EventWindow) WHERE NOT (e)-[:FRAMED_BY]->() RETURN count(e) AS missing",
    "temporal_sanity": "MATCH (e:EventWindow) WHERE e.startYear IS NOT NULL AND e.endYear IS NOT NULL AND e.startYear > e.endYear RETURN e.slug AS event, e.startYear AS start, e.endYear AS end LIMIT 50",
    "duplicate_slugs": "MATCH (n) WHERE exists(n.slug) WITH n.slug AS slug, collect(n) AS nodes, size(collect(n)) AS cnt WHERE cnt > 1 RETURN slug, cnt LIMIT 50",
}


def run():
    try:
        from neo4j import GraphDatabase
    except Exception:
        print("neo4j driver not installed or import failed. Install 'neo4j' package and set NEO4J_URI/USER/PASSWORD in env to run audits.")
        return

    uri = "bolt://localhost:7687"
    user = None
    password = None
    # Try to read from env
    import os

    uri = os.getenv("NEO4J_URI", uri)
    user = os.getenv("NEO4J_USER")
    password = os.getenv("NEO4J_PASSWORD")

    auth = (user, password) if user and password else None
    driver = GraphDatabase.driver(uri, auth=auth) if auth else GraphDatabase.driver(uri)

    results = {}
    with driver.session() as session:
        for name, q in QUERIES.items():
            try:
                res = session.run(q)
                rows = [r.data() for r in res]
                results[name] = rows
            except Exception as exc:
                results[name] = {"error": str(exc)}

    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    out = Path("reports")
    out.mkdir(exist_ok=True)
    fp = out / f"audit-{ts}.json"
    fp.write_text(json.dumps({"generated": ts, "results": results}, indent=2))
    print(f"Wrote audit report to {fp}")


if __name__ == "__main__":
    run()
