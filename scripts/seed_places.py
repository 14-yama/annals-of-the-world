"""Seed places (continents -> regions -> countries) into Neo4j.

This is a refactor of the previous `arua.py` seeder moved into `scripts/`.
"""
from neo4j import GraphDatabase
from datetime import datetime
import os

# Credentials are expected in environment or .env
URI = os.getenv("NEO4J_URI", "neo4j+s://e7860001.databases.neo4j.io")
USER = os.getenv("NEO4J_USER", "e7860001")
PASSWORD = os.getenv("NEO4J_PASSWORD", "")

# -------------------- Data --------------------
CONTINENTS = ["Africa","Americas","Antarctica","Asia","Europe","Oceania"]


def slugify(text: str) -> str:
    t = (text or "").strip()
    return t.replace(" ", "-").replace("/", "-").replace("_", "-").lower()


def now_iso() -> str:
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"


C_CONSTRAINTS = """
CREATE CONSTRAINT place_slug_unique IF NOT EXISTS
FOR (n:Place) REQUIRE n.slug IS UNIQUE;

CREATE INDEX place_region_slug_idx IF NOT EXISTS
FOR (n:Place) ON (n.region, n.slug);
"""


C_UPSERT = """
MERGE (p:Place {slug: $slug})
ON CREATE SET
  p.name=$name, p.kind=$kind, p.region=$region, p.category='Place',
  p.is_generic=true, p.class_number=4,
  p.division_code=$division_code, p.call_number=$call_number,
  p.status=$status, p.intl_status=$intl_status,
  p.created_at=$ts, p.updated_at=$ts,
  p.created_by='seed@annals', p.modified_by='seed@annals',
  p.status_by='seed@annals', p.version=1
ON MATCH SET
  p.name=coalesce($name,p.name),
  p.region=coalesce($region,p.region),
  p.updated_at=$ts
RETURN p.slug AS slug
"""

C_CONTAINS = """
MATCH (a:Place {slug:$a}), (b:Place {slug:$b})
MERGE (a)-[:CONTAINS]->(b)
"""


def upsert_place(tx, *, name: str, kind: str, region: str, division_code: str, status="PROPOSED", intl_status="NEEDS_REVIEW"):
    slug = slugify(name)
    call = f"4.{division_code}-{slug}"
    tx.run(C_UPSERT, slug=slug, name=name, kind=kind, region=region,
           division_code=division_code, call_number=call,
           status=status, intl_status=intl_status, ts=now_iso())
    return slug


def seed(tx):
    tx.run(C_CONSTRAINTS)
    for cont in CONTINENTS:
        upsert_place(tx, name=cont, kind="region", region=cont,
                     division_code="400", status="PROPOSED", intl_status="ALIGNED")


def main():
    driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))
    with driver.session() as sess:
        sess.execute_write(seed)
    driver.close()


if __name__ == "__main__":
    main()
