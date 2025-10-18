# Schema Reference — v4 (Human-readable)

This file records the project's v4 schema in a compact, human-readable form: core labels, recommended properties, key relationship types (active-voice), and example constraints / indexes. Use this as the working schema reference for curators, ingesters, and developers.

---

## Core labels and purpose

- `:Idea` — Abstract concepts (e.g., Monotheism, Covenant, Meritocracy).
- `:Person` — Historical agents and figures (e.g., Abraham, Maimonides).
- `:Institution` — Organized bodies (e.g., Second Temple Priesthood, Zionist Congress).
- `:Place` — Geographic nodes (e.g., Jerusalem, Babylon, Alexandria).
- `:Event` / `:EventWindow` — Historical occurrences or temporally bounded windows.
- `:Movement` — Social/religious/cultural trends (e.g., Rabbinic Judaism, Zionism).
- `:Artifact` / `:Text` — Material culture or texts (Dead Sea Scrolls, Masoretic Text).
- `:Evidence` — Primary sources & archaeological finds (Ketef Hinnom amulets).
- `:Corpus` — Canonical groupings (BIBLICAL_CORPUS, RABBINIC_CORPUS).
- `:Timeframe` — Parent nodes for eras (e.g., 920 Classical, 930 Medieval).
- `:Framework` — Interpretive lenses (Cause & Effect, Continuity & Change).

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

- `(:Event)-[:OCCURRED_IN]->(:Place)`
- `(:Event)-[:OCCURRED_AT]->(:Place)` (if precise site)
- `(:Person)-[:INFLUENCES]->(:Idea)`
- `(:Person)-[:LEADS]->(:Institution)`
- `(:Institution)-[:CODIFIES]->(:Text)`
- `(:EventWindow)-[:FRAMED_BY {citation_style,…}]->(:Framework)`
- `(:Evidence)-[:BELONGS_TO]->(:Corpus)`
- `(:Movement)-[:ARISES_FROM]->(:Event)`
- `(:Place)-[:CONTAINS]->(:Institution)`
- `(:Text)-[:CITES]->(:Text)`
- `(:Person)-[:AUTHOR_OF]->(:Text)`

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

Keep constraint creation under a single migration script (`scripts/migrate_schema.py` or `setup_constraints.py`).

---

## Time & chronology

- Store years as integers: BCE negative, CE positive (e.g., `-586` for 586 BCE) for numeric sortability and range queries.
- Use `Timeframe` nodes for eras and link `EventWindow` nodes with `OCCURS_DURING`.

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
