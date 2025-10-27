# seed_places_inline.py
# Seeding Continents → Regions → Countries with Canonical Attribute Registry
# Neo4j 5 / Aura compatible. No APOC. No env/CLI.

from neo4j import GraphDatabase
from datetime import datetime

# -------------------- Aura credentials (inline) --------------------
# ❗ Replace <YOUR-AURA-ENDPOINT> with your Aura host (neo4j+s://...databases.neo4j.io)
# ❗ If you hardcode a password, rotate it afterwards.
URI      = "neo4j+s://e7860001.databases.neo4j.io"
USER     = "e7860001"
PASSWORD = "MmS8BbqX1_qgs7ayqoq2GJr7MWj8fLRV7ldaRP_B-9Y"

# -------------------- Data --------------------
# ISO 3166-1 Country Code Registry
# See: docs/registry/iso3166_country_codes.md for the full list of country codes.
# Use this registry to validate Place node 'iso' property and ensure standardized country references.
CONTINENTS = ["Africa","Americas","Antarctica","Asia","Europe","Oceania"]

HIER = {
    "Oceania": {
        "Melanesia": ["Fiji","Papua New Guinea","Solomon Islands","Vanuatu"],
        "Micronesia": ["Kiribati","Nauru","Palau","Marshall Islands","Micronesia"],
        "Polynesia": ["Samoa","Tonga","Tuvalu"],
        "Australia & New Zealand": ["Australia","New Zealand"],
    },
    "Europe": {
        "Northern Europe": ["Denmark","Finland","Iceland","Norway","Sweden","Ireland","United Kingdom","Estonia","Latvia","Lithuania"],
        "Western Europe":  ["Austria","Belgium","France","Germany","Liechtenstein","Luxembourg","Monaco","Netherlands","Switzerland"],
        "Eastern Europe":  ["Belarus","Bulgaria","Czechia","Hungary","Moldova","Poland","Romania","Russia","Slovakia","Ukraine"],
        "Southern Europe": ["Albania","Andorra","Bosnia & Herzegovina","Croatia","Greece","Italy","Kosovo","Malta","Montenegro",
                             "North Macedonia","Portugal","San Marino","Serbia","Slovenia","Spain","Holy See"],
    },
    "Americas": {
        "North America":   ["Canada","United States","Mexico"],
        "Central America": ["Belize","Costa Rica","El Salvador","Guatemala","Honduras","Nicaragua","Panama"],
        "Caribbean":       ["Antigua and Barbuda","Bahamas","Barbados","Cuba","Dominica","Dominican Republic","Grenada","Haiti","Jamaica",
                            "Saint Kitts and Nevis","Saint Lucia","Saint Vincent and the Grenadines","Trinidad and Tobago"],
        "South America":   ["Argentina","Bolivia","Brazil","Chile","Colombia","Ecuador","Guyana","Paraguay","Peru","Suriname","Uruguay","Venezuela"],
    },
    "Africa": {
        "North Africa":   ["Algeria","Egypt","Libya","Morocco","Sudan","Tunisia","Western Sahara"],
        "West Africa":    ["Benin","Burkina Faso","Cabo Verde","Côte d’Ivoire","Gambia","Ghana","Guinea","Guinea-Bissau","Liberia",
                           "Mali","Mauritania","Niger","Nigeria","Senegal","Sierra Leone","Togo"],
        "Central Africa": ["Cameroon","Central African Republic","Chad","Congo","DR Congo","Equatorial Guinea","Gabon","São Tomé and Príncipe"],
        "East Africa":    ["Burundi","Comoros","Djibouti","Eritrea","Ethiopia","Kenya","Madagascar","Malawi","Mauritius","Mozambique",
                           "Rwanda","Seychelles","Somalia","South Sudan","Tanzania","Uganda","Zambia","Zimbabwe"],
        "Southern Africa":["Botswana","Eswatini","Lesotho","Namibia","South Africa","Angola"],
    },
    "Asia": {
        "West Asia":    ["Armenia","Azerbaijan","Bahrain","Cyprus","Georgia","Iran","Iraq","Israel","Jordan","Kuwait","Lebanon",
                         "Oman","Qatar","Saudi Arabia","Syria","Türkiye","United Arab Emirates","Yemen"],
        "Central Asia": ["Kazakhstan","Kyrgyzstan","Tajikistan","Turkmenistan","Uzbekistan"],
        "South Asia":   ["Afghanistan","Bangladesh","Bhutan","India","Maldives","Nepal","Pakistan","Sri Lanka"],
        "Southeast Asia":["Brunei","Cambodia","Indonesia","Laos","Malaysia","Myanmar","Philippines","Singapore","Thailand","Timor-Leste","Vietnam"],
        "East Asia":    ["China","Japan","Mongolia","North Korea","South Korea","Taiwan","Hong Kong","Macau"],
    },
    # Antarctica: no children
}

# -------------------- Helpers --------------------
def slugify(text: str) -> str:
    t = (text or "").strip()
    return t.replace(" ", "-").replace("/", "-").replace("_", "-").lower()

def now_iso() -> str:
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"

# -------------------- Cypher --------------------
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

# -------------------- Seeding --------------------
def upsert_place(tx, *, name: str, kind: str, region: str, division_code: str, status="PROPOSED", intl_status="NEEDS_REVIEW"):
    slug = slugify(name)
    call = f"4.{division_code}-{slug}"
    tx.run(C_UPSERT, slug=slug, name=name, kind=kind, region=region,
           division_code=division_code, call_number=call,
           status=status, intl_status=intl_status, ts=now_iso())
    return slug

def seed(tx):
    # 1) constraints
    tx.run(C_CONSTRAINTS)

    # 2) continents (treated as macro-regions)
    for cont in CONTINENTS:
        upsert_place(tx, name=cont, kind="region", region=cont,
                     division_code="400", status="PROPOSED", intl_status="ALIGNED")

    # 3) regions & countries
    for continent, regions in HIER.items():
        cont_slug = slugify(continent)
        for rname, countries in regions.items():
            rslug = upsert_place(tx, name=rname, kind="region", region=continent,
                                 division_code="410", intl_status="ALIGNED")
            tx.run(C_CONTAINS, a=cont_slug, b=rslug)
            for cname in countries:
                pslug = upsert_place(tx, name=cname, kind="country", region=continent,
                                     division_code="430", intl_status="NEEDS_REVIEW")
                tx.run(C_CONTAINS, a=rslug, b=pslug)

    # 4) Antarctica housekeeping
    a_slug = slugify("Antarctica")
    tx.run("""
        MATCH (c:Place {slug:$s})
        SET  c.kind='region', c.region='Antarctica', c.intl_status='ALIGNED', c.updated_at=$ts
    """, s=a_slug, ts=now_iso())

def main():
    driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))
    with driver.session() as sess:
        info = sess.run("CALL db.info() YIELD version RETURN version").single()
        print(f"Connected to Neo4j {info['version']} @ {URI}")
        sess.execute_write(seed)
        res = sess.run("""
            MATCH (c:Place {kind:'region'})-[:CONTAINS]->(r:Place {kind:'region'})-[:CONTAINS]->(p:Place {kind:'country'})
            RETURN count(DISTINCT c) AS continents, count(DISTINCT r) AS regions, count(DISTINCT p) AS countries
        """).single()
        print(f"Seeded: {res['continents']} continents, {res['regions']} regions, {res['countries']} countries.")
    driver.close()

if __name__ == "__main__":
    main()
