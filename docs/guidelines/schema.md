# Schema Reference — v4 (Human-readable)

> **Last updated:** 2026-01-24

This file records the project's v4 schema in a compact, human-readable form: core labels, recommended properties, key relationship types (active-voice), and example constraints / indexes. Use this as the working schema reference for curators, ingesters, and developers.

---

## Core labels and purpose

- `:Idea` — Abstract concepts (e.g., Monotheism, Covenant, Meritocracy).
- `:Person` — Historical agents and figures (e.g., Abraham, Maimonides).
- `:Institution` — Organized bodies (e.g., Second Temple Priesthood, Zionist Congress).
- `:Place` — Geographic nodes (e.g., Jerusalem, Babylon, Alexandria). Represents stable physical locations; names are time-scoped via `:PlaceName`. See [Geographic Naming Conventions](./geo_naming.md).
- `:PlaceName` — Time-scoped name variant for a Place (e.g., Jebus → Jerusalem → Aelia Capitolina). Linked via `HAS_NAME`.
- `:Event` / `:EventWindow` — Historical occurrences or temporally bounded windows. See [Event Kind Vocabulary](../schema/event-kinds.md) for the canonical `kind` property values.
- `:Movement` — Social/religious/cultural trends (e.g., Rabbinic Judaism, Zionism).
- `:Artifact` / `:Text` — Material culture or texts (Dead Sea Scrolls, Masoretic Text).
- `:Evidence` — Primary sources & archaeological finds (Ketef Hinnom amulets).
- `:Corpus` — Canonical groupings (BIBLICAL_CORPUS, RABBINIC_CORPUS).
- `:Timeframe` — Parent nodes for eras (e.g., 920 Classical, 930 Medieval).
- `:Framework` — Interpretive lenses (Cause & Effect, Continuity & Change).
- `:Polity` — Time-scoped political entities (e.g., Kingdom of England, Ottoman Empire). Linked to Places via `GOVERNED_BY`.

---

## Recommended node properties (common)

- `id` — internal UUID or numeric id (optional if using `slug`)
- `slug` — canonical short-id (unique per label)
- `name` — human-friendly label
- `description` — short summary
- `category` — optional classifier (e.g., `philosopher`, `text-type`)
- `created_at`, `updated_at` — ISO8601 timestamps
- `created_by`, `modified_by`, `status_by` — provenance (curator email/agent)
- `status` — `PROPOSED`, `REVIEWED`, `PUBLISHED`, etc.
- `version` — integer version counter
- `is_generic` — boolean (for place/idea hubs)
- `class_number`, `division_code`, `call_number` — library-like classification (optional)
- `kind` — (**Event nodes only**) canonical event category (e.g., `Marriage`, `Council`, `Battle`). See [Event Kind Vocabulary](../schema/event-kinds.md).

For large-text fields use `description` and consider full-text indices rather than many properties.

---

## Generic vs Contextual nodes (policy banner)

Keep content nodes generic and free from time/place; add time and space through contextual support nodes and relationships.

- When `is_generic = true`
  - Use for timeless hubs: e.g., Place: "Egypt"; Idea: "Monotheism"; Text family: "Torah_Corpus".
  - `description` must be neutral and atemporal (no dates, regimes, or period‑specific claims). Examples are fine but not era‑bound.
  - Do not set `startYear`/`endYear`; do not duplicate the node by era/dynasty.
- When contextual (default)
  - Model era/state‑specific constructs as support nodes and connect them to the generic hub via edges:
    - `(:Event|:EventWindow)-[:OCCURS_IN]->(:Place)`
    - `(:EventWindow)-[:OCCURS_DURING]->(:Timeframe)`
    - `(:Institution)-[:ADMINISTERS|HOSTS]->(:Place)` or `(:Place)-[:CONTAINS]->(:Institution)` per vocabulary
- Naming & IDs
  - Generic slugs omit dates: `egypt`, `monotheism`, `torah_corpus`.
  - Contextual slugs carry scope/time: `ptolemaic_egypt_state`, `second_temple_destruction_70ce`.
- Example
  - Generic Place node: `(:Place {slug:'egypt', name:'Egypt', is_generic:true, description:'North‑East African region centered on the Nile; used as a timeless geographic hub across periods.'})`
  - Contextual nodes: `(:Institution {slug:'ptolemaic_kingdom', startYear:-305, endYear:-30})-[:ADMINISTERS]->(:Place {slug:'egypt'})` and `(:Event {slug:'octavian_conquest_30bce'})-[:OCCURS_IN]->(:Place {slug:'egypt'})`.
- Validation tips
  - If `is_generic = true`, block/flag `startYear`/`endYear` and year‑like tokens in `description`.
  - Period/place membership belongs to relationships (`OCCURS_IN`, `OCCURS_DURING`), not baked into node `slug`/`name`.

---

## Relationship types (active-voice — required)

Use active verbs. Relationship properties should include provenance metadata when applicable.

- `(:Event)-[:OCCURS_IN]->(:Place)`
- `(:Event)-[:OCCURS_AT]->(:Place)` (if precise site)
- `(:Event)-[:OCCURS_DURING]->(:Timeframe)`
- `(:Person)-[:INFLUENCES]->(:Idea)`
- `(:Person)-[:LEADS]->(:Institution)`
- `(:Person)-[:PARTICIPATES_IN {role}]->(:Event)`
- `(:Institution)-[:CODIFIES]->(:Text)`
- `(:EventWindow)-[:FRAMED_BY {citation_style,…}]->(:Framework)`
- `(:Evidence)-[:BELONGS_TO]->(:Corpus)`
- `(:Movement)-[:ARISES_FROM]->(:Event)`
- `(:Place)-[:CONTAINS]->(:Place)` (geo hierarchy)
- `(:Place)-[:CONTAINS]->(:Institution)`
- `(:Text)-[:CITES]->(:Text)`
- `(:Person)-[:AUTHOR_OF]->(:Text)`

**Geographic naming relationships** (see [geo_naming.md](./geo_naming.md)):
- `(:Place)-[:PREVIOUSLY_KNOWN_AS {startYear, endYear, is_primary, change_reason}]->(:PlaceName)` — authoritative, time-scoped name variants
- `(:Place)-[:ENDONYM]->(:PlaceName)` — optional, derived edge for current native/local names
- `(:Place)-[:EXONYM]->(:PlaceName)` — optional, derived edge for current foreign-language names
- `(:Place)-[:GOVERNED_BY {startYear, endYear}]->(:Polity)` — political sovereignty
- `(:Place)-[:LOCATED_IN]->(:Place)` — extinct place → modern container

Relationship properties (recommended for FRAMED_BY / evidence-carrying edges):
- `evidence_url` (stable DOI/URL)
- `citation_style` ("Chicago 17")
- `page_refs` (string or list)
- `source_note` (free text)
- `created_at`, `created_by`
- `r.deprecated` — boolean flag for deprecated edges

All relationship names must be active voice per governance rules (no `CONTROLLED_BY`, use `CONTROLS`).

---

## Constraints & indexes (examples)

These example Cypher statements are suggested to enforce uniqueness and speed common lookups.

CREATE CONSTRAINT statements (Neo4j 5+ syntax):

```
CREATE CONSTRAINT idea_slug_unique IF NOT EXISTS FOR (i:Idea) REQUIRE i.slug IS UNIQUE;
CREATE CONSTRAINT person_slug_unique IF NOT EXISTS FOR (p:Person) REQUIRE p.slug IS UNIQUE;
CREATE CONSTRAINT place_slug_unique IF NOT EXISTS FOR (pl:Place) REQUIRE pl.slug IS UNIQUE;
CREATE CONSTRAINT event_slug_unique IF NOT EXISTS FOR (e:Event) REQUIRE e.slug IS UNIQUE;
```

Indexes for fast filtering (example):

```
CREATE INDEX person_category_index IF NOT EXISTS FOR (p:Person) ON (p.category);
CREATE INDEX place_region_index IF NOT EXISTS FOR (pl:Place) ON (pl.region);
```

Keep constraint creation under the unified pipeline script (`scripts/seed_backend.py`).

---

## Time & chronology

- Store years as integers: BCE negative, CE positive (e.g., `-586` for 586 BCE) for numeric sortability and range queries.
- Use `Timeframe` nodes for eras and link content nodes with `OCCURS_DURING`.

### Timeframe nodes (Class 9 divisions)

Create canonical Timeframe nodes for temporal anchoring:

| Division | Slug | Name | Year Range |
|----------|------|------|------------|
| 910 | `910_Prehistoric` | Prehistoric | before 3000 BCE |
| 920 | `920_Classical` | Classical | 3000 BCE – 500 CE |
| 930 | `930_Medieval` | Medieval | 500 – 1500 CE |
| 940 | `940_Early_Modern` | Early Modern | 1500 – 1800 CE |
| 950 | `950_Modern` | Modern | 1800 – 1945 CE |
| 960 | `960_Contemporary` | Contemporary | 1945 CE – present |

Cypher setup:

```cypher
CREATE (t:Timeframe {slug: '910_Prehistoric', division: 910, name: 'Prehistoric', startYear: -10000000, endYear: -3000})
CREATE (t:Timeframe {slug: '920_Classical', division: 920, name: 'Classical', startYear: -3000, endYear: 500})
CREATE (t:Timeframe {slug: '930_Medieval', division: 930, name: 'Medieval', startYear: 500, endYear: 1500})
CREATE (t:Timeframe {slug: '940_Early_Modern', division: 940, name: 'Early Modern', startYear: 1500, endYear: 1800})
CREATE (t:Timeframe {slug: '950_Modern', division: 950, name: 'Modern', startYear: 1800, endYear: 1945})
CREATE (t:Timeframe {slug: '960_Contemporary', division: 960, name: 'Contemporary', startYear: 1945, endYear: 2100})

CREATE INDEX timeframe_division IF NOT EXISTS FOR (t:Timeframe) ON (t.division)
CREATE INDEX timeframe_slug IF NOT EXISTS FOR (t:Timeframe) ON (t.slug)
```

### OCCURS_DURING edges (best practice for scale)

For efficient temporal queries at 1M+ nodes, use explicit `OCCURS_DURING` edges to Timeframe nodes rather than inline relationship properties.

**Why explicit edges are faster:**
- Node property indexes are more performant than relationship property indexes
- Queries start from indexed Timeframe node and traverse outward
- Neo4j optimizes graph traversal patterns over property filtering
- Enables intersection queries (e.g., "institutions opposing persons in division 930")

**Pattern:**

```cypher
// Link any content node to its timeframe
(:Person)-[:OCCURS_DURING]->(:Timeframe)
(:Event)-[:OCCURS_DURING]->(:Timeframe)
(:Institution)-[:OCCURS_DURING]->(:Timeframe)
(:Movement)-[:OCCURS_DURING]->(:Timeframe)
(:Cluster)-[:OCCURS_DURING]->(:Timeframe)
```

**Example queries (efficient at scale):**

```cypher
// All clusters in Medieval period (division 930)
MATCH (t:Timeframe {division: 930})<-[:OCCURS_DURING]-(c:Cluster)
RETURN c.slug, c.name

// All events in Modern period (division 950)
MATCH (t:Timeframe {division: 950})<-[:OCCURS_DURING]-(e:Event)
RETURN e.slug, e.name, e.startYear

// Institutions opposing persons in Medieval period
MATCH (t:Timeframe {division: 930})<-[:OCCURS_DURING]-(i:Institution)
MATCH (t)<-[:OCCURS_DURING]-(p:Person)
MATCH (i)-[:OPPOSES]->(p)
RETURN i.slug, p.slug
```

**Seed file format:**

Include `timeframe_edges` array in relationship JSON files:

```json
{
  "_meta": { "cluster": "Example_Cluster" },
  "relationships": [ ... ],
  "timeframe_edges": [
    { "node_slug": "Henry_VIII", "timeframe_slug": "940_Early_Modern", "division": 940 },
    { "node_slug": "Act_of_Supremacy_1534", "timeframe_slug": "940_Early_Modern", "division": 940 }
  ]
}
```

Run `scripts/generate_timeframe_edges.py` to auto-generate timeframe_edges from cluster relationships.

---

## Provenance and evidence

- Every published relationship must have at least one `FRAMED_BY` edge or an attached `:Evidence` node.
- Evidence nodes should capture stable identifiers (DOI), URL, and human citation string.
- Maintain a strict citation schema: `citation_style`, `evidence_url`, `page_refs`, `source_note`.

---

## Example node and relationship (Cypher)

```
MERGE (p:Person {slug:'maimonides'})
  SET p.name='Maimonides', p.category='philosopher', p.status='PROPOSED', p.created_at=datetime()

MERGE (i:Idea {slug:'rationalism'})
  SET i.name='Rationalism'

MERGE (p)-[:INFLUENCES {created_at: datetime(), created_by:'curator@annals'}]->(i)
```

Add FRAMED_BY with citation:

```
MATCH (e:EventWindow {slug:'exodus-1'})
MATCH (f:Framework {slug:'cause-and-effect'})
MERGE (e)-[r:FRAMED_BY]->(f)
SET r.evidence_url='https://doi.org/…', r.citation_style='Chicago 17', r.page_refs='12-18'
```

---

## Geographic hierarchy (geo registry)

The backend includes a hierarchical geo registry as the **source of truth** for geographic queries.

### Hierarchy levels

All geographic entities are modeled as `:Place` nodes with a `kind` property:

```
(:Place {kind:"continent"}) -[:CONTAINS]-> (:Place {kind:"region"})
(:Place {kind:"region"})    -[:CONTAINS]-> (:Place {kind:"country"})
(:Place {kind:"country"})   -[:CONTAINS]-> (:Place {kind:"subnational"})
```

**Structure:**
- **6 Continents**: Africa, Americas, Asia, Europe, Oceania, Antarctica (kind="region")
- **22 Regions**: Northern Europe, Western Europe, Southern Asia, etc. (kind="region", UN M.49)
- **Countries**: seeded from the project registry (currently 196 in `docs/registry/iso3166_country_codes.md`) (kind="country")
- **Subnational Places**: england, london, westminster, etc. (linked via CONTAINS)

### Name variants (geo-registry)

For international best practice and queryability, place name variants are modeled in two layers:

- Denormalized: `Place.alt_names[]` (SKOS `altLabel` style; great for search)
- Canonical: `(:Place)-[:HAS_NAME]->(:PlaceName)` (time-scoped, used for historical accuracy)

The JSON source-of-truth lives under `geo-registry/` (see `geo-registry/README.md`).

### Seed command

```bash
python scripts/seed_backend.py --clusters English_Reformation
```

### Node shapes

**Continent/Region:**
```json
{ 
  "slug": "europe", 
  "name": "Europe", 
  "kind": "region",
  "region": "Europe",
  "category": "Place",
  "is_generic": true,
  "class_number": 4,
  "division_code": "400"
}
```

**Country:**
```json
{ 
  "slug": "united-kingdom", 
  "name": "United Kingdom", 
  "kind": "country",
  "region": "Europe",
  "category": "Place",
  "is_generic": true,
  "division_code": "430"
}
```

### Query patterns

**Events in a country:**
```cypher
MATCH (c:Place {slug: 'united-kingdom'})-[:CONTAINS*0..3]->(p:Place)
MATCH (e:Event)-[:OCCURS_IN]->(p)
RETURN e.name, p.name
```

**Events in a region:**
```cypher
MATCH (r:Place {name: 'Northern Europe', kind: 'region'})-[:CONTAINS*0..4]->(p:Place)
MATCH (e:Event)-[:OCCURS_IN]->(p)
RETURN e.name, p.name
```

**Events in a continent:**
```cypher
MATCH (c:Place {name: 'Europe'})-[:CONTAINS*0..5]->(p:Place)
MATCH (e:Event)-[:OCCURS_IN]->(p)
RETURN e.name, p.name
```

---

## Governance notes (short)

- Active voice only for relationships.
- No label explosion: prefer properties (`category`) over many small labels.
- Versioning: never silently overwrite — deprecate with `r.deprecated = true` and create new edges.
- Audit queries must detect missing `FRAMED_BY`, passive-voice relationships, and orphan nodes.

---

## Next steps (recommended)

- Add [docs/guidelines/audit_queries.md](./audit_queries.md) with ready-to-run Cypher for QA checks (missing FRAMED_BY, passive verbs, orphan nodes).
- Create `src/annals/models.py` with dataclasses or Pydantic models reflecting these node shapes.
- Add unit tests that verify constraint creation and a small integration test that runs sample MERGE + audit queries against a test Neo4j instance.

---

If you'd like, I can now:
- create `audit_queries.md` with 6-8 useful Cypher checks, or
- scaffold `src/annals/models.py` and a small test harness that validates the shapes.
