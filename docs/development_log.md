# Development Log — Annals of the World

> This log tracks major development milestones, schema changes, and infrastructure updates.

---

## Update — 2026-01-24T19:45:00Z (most recent)

### Geographic Naming Conventions

Added comprehensive guideline for handling place names that change over time.

**New documentation:** [docs/guidelines/geo_naming.md](./guidelines/geo_naming.md)

**Key schema additions:**
- `:PlaceName` — Time-scoped name variant nodes
- `:Polity` — Time-scoped political entities
- `(:Place)-[:HAS_NAME {startYear, endYear}]->(:PlaceName)`
- `(:Place)-[:GOVERNED_BY {startYear, endYear}]->(:Polity)`

**Naming change categories standardized:**
1. Conquest/political takeover (Jebus → Jerusalem, Constantinople → Istanbul)
2. Regime change (St. Petersburg → Leningrad → St. Petersburg)
3. Decolonization (Bombay → Mumbai, Ceylon → Sri Lanka)
4. Exonyms vs endonyms (Deutschland vs Germany)
5. Script/transliteration variants (Beijing vs Peking)
6. Extinct/ancient places (Babylon, Troy, Carthage)
7. Border changes (place stays, country changes)
8. City mergers/administrative changes

**External ID standards:**
- `wikidata_id` — Universal (all places)
- `geonames_id` — Modern places
- `pleiades_id` — Ancient/classical places

---

## Update — 2026-01-24T19:15:00Z

### Major Infrastructure Overhaul

**1. Unified Seeding Pipeline** (`scripts/seed_backend.py`)

Created a single-entry-point script for all backend seeding operations:
- Step 1: Apply 38 constraints and indexes
- Step 2: Seed geo registry (6 continents, 22 regions, 198 countries)
- Step 3: Seed cluster data (nodes, relationships, edge arrays)
- Step 4: Link cluster places to geo hierarchy
- Step 5: Post-seed validation

Usage:
```bash
python scripts/seed_backend.py --clusters English_Reformation
python scripts/seed_backend.py --dry-run  # Preview without changes
```

**2. Geographic Hierarchy Integration** (`geo_registry.py`)

- Seeded hierarchical geo registry as source of truth for geographic queries
- Structure: Continent → Region → Country → Subnational
- Linked UK subnational places (England, Westminster, London, etc.) to hierarchy
- Enables queries like "all events in Europe" via traversal

**3. Event Modeling Enhancements**

- Added `kind` property to Event nodes (25 canonical values)
- Added `Event.kind` index for efficient filtering
- Backfilled `OCCURS_IN` edges for Events via `place_edges` array
- Marriage-as-Event migration: MARRIES → Marriage Event + PARTICIPATES_IN

**4. Legacy Script Cleanup**

Archived 39 scripts to `legacy-scripts/`:
- `one-time-migrations/`: Completed schema migrations
- `superseded/`: Replaced by unified pipeline
- `utilities/`: Unused utilities

Retained 27 active scripts in `scripts/` and `scripts/admin/`.

**5. Documentation Updates**

- Updated `docs/guidelines/schema.md` with geo hierarchy section
- Added `legacy-scripts/README.md` documenting archived scripts
- Updated constraint/index examples for Neo4j 5+ syntax

### Current Backend State

```
Production cluster: English_Reformation
- Nodes: 186
- Relationships: 425
- Timeframe edges: 187
- FRAMED_BY edges: 423
- Place edges: 46

Geo hierarchy:
- Continents: 6
- Regions: 22
- Countries: 198
- UK subnational: 9 (linked)

Post-seed validation:
- Events missing kind: 0
- Events missing OCCURS_DURING: 0
- Events missing OCCURS_IN: 0
```

### Next Steps

1. Expand to additional clusters (Early_Christianity, etc.)
2. Add curator tooling for event kind assignment
3. Implement place linking for non-UK clusters
4. Create automated validation reports

---

## Update — 2025-12-XX (English Reformation Curation)

- Expanded English_Reformation cluster significantly
- Normalized relationships to active-voice verbs
- Added Chicago 17 citation_style to all relationships
- Filled node definitions and descriptions
- Added comprehensive timeframe_edges and framed_by_edges

---

## Update — 2025-10-04T03:36:16Z

- Added [docs/guidelines/relations_vocabulary.md](./guidelines/relations_vocabulary.md) (canonical verbs, evidence rules, QA snippets).
- Added [docs/guidelines/historian_framework.md](./guidelines/historian_framework.md) (framework provenance, FRAMED_BY rules, evidence promotion).
- Added [docs/guidelines/framework_matrix.md](./guidelines/framework_matrix.md) (tabular framework→verb matrix).
- Added [docs/guidelines/crosswalk_crm_prov.md](./guidelines/crosswalk_crm_prov.md) (CIDOC-CRM / PROV crosswalk guidance).
- Added [docs/guidelines/audit_queries.md](./guidelines/audit_queries.md) (runnable Cypher QA checks) and created `scripts/` task plan for `run_audits.py`.
- Enriched [docs/guidelines/hebrew_cluster.md](./guidelines/hebrew_cluster.md) with logic alignment guide, relationship templates, and links to vocabulary.
- Created links across docs for easier navigation and fixed plain filename references to Markdown links.

Notes: these are governance and pattern updates; no domain content from other clusters was imported—only structural rules and curator workflows.


Summary

- The project is undergoing a schema refactor to move core code into `src/annals`, standardize node shapes, and centralize migration and audit tooling.

Lessons learned

- ChatGPT vs GitHub Copilot: ChatGPT proved valuable for high-level brainstorming, documentation drafts, and generating design prose; GitHub Copilot (IDE assistant) is more useful for inline code completion and quick scaffolding inside the editor. Both have complementary strengths and are useful in different phases of development.

- MCP importance: adopting an MCP-style pattern (Model Context Protocol / small model-serving layer) reduces manual coding by centralizing schema-to-code generation, validation, and small translation tasks. An MCP layer helps keep imports and schema migrations consistent and reduces repetitive boilerplate across scripts.

What changed in this sprint

- Created `src/annals` package and moved/refactored helper scripts.
- Added `docs/guidelines/*` artifacts: audit queries, curator runbook, CRM/PROV crosswalk, framework matrix, features_by_version, classification, and summary.
- Added [docs/summary.md](./summary.md) and TOC link in `README.md`.

Next steps

- Scaffold `src/annals/models.py` (Pydantic/dataclasses) to lock down node shapes.
- Implement `scripts/run_audits.py` to run [docs/guidelines/audit_queries.md](./guidelines/audit_queries.md) and write reports.
- Add a small MCP server scaffold to automate schema-driven codegen and validation.

Notes

- Keep secrets out of the repo and rotate any credentials committed during early testing.

---

## Update — 2025-10-03T22:26:00Z (appendix)

New governance and curator artifacts added this sprint (summary):

- [docs/guidelines/relations_vocabulary.md](./guidelines/relations_vocabulary.md) — Canonical, auditable verb list with allowed node-type pairs, evidence annotation rules, deprecation policy, and Cypher QA snippets.
- [docs/guidelines/historian_framework.md](./guidelines/historian_framework.md) — Historian framework guide for `Framework` nodes, `FRAMED_BY` semantics, evidence promotion rules (inline → :Evidence), and curator workflow for framing and provenance.
- [docs/guidelines/framework_matrix.md](./guidelines/framework_matrix.md) — Tabular mapping of interpretive frameworks to recommended active-voice verbs (CAUSES, DIFFUSES, TRANSMITS, CANONIZES, etc.).
- [docs/guidelines/crosswalk_crm_prov.md](./guidelines/crosswalk_crm_prov.md) — CIDOC-CRM / W3C PROV crosswalk showing how to translate provenance records into the project's node/edge patterns.
- [docs/guidelines/audit_queries.md](./guidelines/audit_queries.md) — Runnable Cypher checks for QA (missing FRAMED_BY, orphan nodes, passive verbs, duplicate slugs, call-number mismatches). Script scaffolding planned: `scripts/run_audits.py`.
- [docs/guidelines/hebrew_cluster.md](./guidelines/hebrew_cluster.md) — Enriched with logic alignment guide, relationships templates, relationship node-type matrices, and curated example triples; linked to the relations vocabulary.
- [docs/guidelines/README.md](./guidelines/README.md) — updated index listing the above artifacts.

Actions performed

- Converted many inline backtick references to active Markdown links across docs for easier navigation and publication.
- Created framework matrix table for curator lookup (more readable than bullets).
- Added QA snippets and governance rules to reduce verb drift and ensure evidence promotion.

Next practical tasks (prioritized)

1. Normalize existing relationship labels in all cluster files to the canonical verbs (UPPER_SNAKE_CASE) and run the passive-verb audit.
2. Implement `scripts/run_audits.py` to run `audit_queries.md` and export JSON reports in `reports/`.
3. Generate seed CSV templates (nodes + rels) for `class 9` from `hebrew_cluster.md` scaffold.
4. Promote multi-use sources (e.g., Dead Sea Scrolls publications, Septuagint critical editions) to `:Evidence` nodes and update edges.
5. Create curator onboarding checklist and PR templates for promoting inline citations to `:Evidence`.

Notes & Rationale

- The recent additions are intentionally pattern-only when borrowing the gun cluster's logic: no domain content from that cluster was imported, only structural and governance patterns (evidence tiers, active-voice verbs, framework lens usage, promotion rules).
- These governance docs reduce ad-hoc curation and make it easier to automate QA and ingestion while preserving scholarly traceability.

NOTE: Going forward, all appended log entries will include an ISO8601 timestamp in UTC (e.g., `YYYY-MM-DDTHH:MM:SSZ`) immediately after the word "Update" to ensure precise provenance of documentation changes.
