# Development Log — Annals of the World

> This log tracks major development milestones, schema changes, and infrastructure updates.

---

## Update — 2025-07-18 (most recent)

### Comprehensive Backend Audit & Normalization

#### 1. Backend Audit Summary (40,220 entities)

- **Slug uniqueness:** Verified — Appwrite's `slug_idx` unique index prevents duplicates.
- **Entity counts by label:** Person 5,000+, Idea 5,000+, Institution 5,000+, Place 5,000+, EventWindow 5,000+, Movement 5,000+, Text 5,000+, Evidence 4,229, Timeframe 991.
- **Field completeness:** All entities have era, eraSlug, eraDivisionCode, continent, region, summary, callNumber, detailsJson, frameworks.
- **Era distribution:** 6 canonical eras verified (Prehistoric: 731, Classical, Medieval, Early Modern, Modern, Contemporary — all 5,000+).

#### 2. Era Normalization — "Classical / Ancient" → "Classical"

- **Root cause:** 4 topic data files (architecture.ts, languages.ts, medicine.ts, weapons.ts) used legacy `era: "Classical / Ancient"` label → propagated through topicConverter.ts → exported to catalog_entities.json → seeded to backend with empty eraDivisionCode.
- **Backend fix:** 136 entities patched via Python script:
  - 130 entities: era="Classical / Ancient" → era="Classical", eraDivisionCode="920"
  - 6 broad-era Timeframes: assigned broad codes (910, 920, 930, 940, 950, 960)
  - **Post-fix verification:** 0 remaining empty eraDivisionCode, 0 remaining "Classical / Ancient" era.
- **Source code fix:** Normalized "Classical / Ancient" → "Classical" across 10 files:
  - `ui/src/data/` — architecture.ts, languages.ts, medicine.ts, weapons.ts
  - `ui/src/data/catalog/` — topicConverter.ts, topicEntities.ts, classical.ts, enrichmentData.ts
  - `ui/src/data/catalog/corpuses/` — scienceTech.ts
  - `ui/src/pages/DocsPage.tsx` — Eras glossary entry
- **Seed script fix:** `scripts/seed_catalog_entities.py` — added CANONICAL_ERA normalization so "Classical / Ancient" maps to "Classical" in both `get_era_division()` and `entity_to_document()`.

#### 3. Search Ranking Optimization

- Added `nameRelevance()` scoring to `entityService.ts` — exact match (100), prefix (80), all-words-present (60), substring (50), partial (30).
- Applied `scoreMatch` re-ranking in `AdvancedSearch.tsx` for autocomplete results.
- Verified: julius caesar, aristotle, roman empire, university of oxford, democracy, empire all rank #1.

#### 4. Entity Enrichment
- Empire entity enriched: 8 relationships, 5 causes, 5 effects, 5 frameworks (score 10).
- 56 entities at quality score 10, 2,039 at score 9, 5,000+ at score 8.

#### 5. Documentation & Repo Hygiene
- Updated `.gitignore` for large data files (data/people/, catalog_entities.json, wikidata parts).
- Updated project-guidelines.instructions.md: era framework, entity counts (40,000+).
- Updated docs/ROADMAP.md: current scope reflects Appwrite backend.
- Updated docs/guidelines/international_conventions.md: era naming normalized.
- Updated slug_naming_convention.md.

---

## Update — 2026-04-02

### Wikidata Institutions Dataset, Expanded Verbs, Fetch Guide

#### 1. Wikidata Institutions Fetch

- Created `scripts/fetch_wikidata_institutions.py` (v2.0) — comprehensive SPARQL-based fetch
  script covering all 36 Institution divisions (310–394)
- **213 unique Wikidata type QIDs** across **76 batches** with adaptive limit fallback
- Raw fetch: 68,503 results → 51,943 unique entities after deduplication
- Post-cleanup (v2.1): **36,738 clean entities** after removing 15,205 non-institutions
  (TV series, football clubs, county seats, parks, etc.) and reclassifying 1,653 entities
- Output: `data/wikidata_institutions.json`
- Top divisions: Universities (4,006), Churches (5,979), Museums (4,484), Media (3,339),
  Religious Orgs (2,779), Political Parties (2,106), Mosques (2,116), Theaters (2,038)

#### 2. Expanded Relationship Verbs (27 new)

Added 27 new verbs to support expanded Institution (Class 3) and Place (Class 4) divisions:

- **Institutional governance (19):** GOVERNS, LEGISLATES, ADMINISTERS, ADJUDICATES, FUNDS,
  TRAINS, ACCREDITS, COMMANDS, DEPLOYS, PATROLS, CURATES, EXHIBITS, BROADCASTS, ENROLLS,
  HEALS, WORSHIPS_AT, ALLIES_WITH, TRADES_WITH, OCCUPIES
- **Place-centric (8):** CONTAINS, BORDERS, SITUATED_IN, CAPITAL_OF, GATEWAY_TO,
  SACRED_TO, RULED_BY, CONTROLS

Updated in: `docs/guidelines/node-relationship-vocabulary.md` (§4b),
`docs/guidelines/node_interaction_matrix.md` (I→/L→ sections + Quick Pair Matrix),
`ui/src/pages/DocsPage.tsx` (VERB_GLOSSARY + CLASSIFICATION_ENTRIES)

#### 3. Wikidata Fetch Guide

- Created `docs/guidelines/wikidata_fetch_guide.md` — developer reference for full-coverage
  Wikidata fetches using SPARQL. Covers QID mapping, batch strategy, adaptive fallback,
  sitelinks thresholds, post-fetch cleanup, `historicalSignificance` scoring, and
  `inAppwrite` flag conventions.

#### 4. DocsPage Classification Corrections

- Updated CLASSIFICATION_ENTRIES in DocsPage.tsx to match actual `callNumbers.ts` divisions
  for Classes 3–7 (Institution, Place, Event, Movement, Artifact/Text)

---

## Update — 2026-03-31

### Appwrite Backend, Model Harmonization, Division Expansion, Entity Page Enhancements

Major infrastructure upgrade adding a backend layer, harmonizing data models, and dramatically
expanding the call number classification system.

#### 1. Appwrite Backend Setup

- Installed **Appwrite Web SDK v16.1.0** in `ui/` (v24 had broken ESM with Vite 5)
- Created `ui/src/lib/appwrite.ts` — Client, Account, Databases, Storage singletons
- Created `ui/src/services/entityService.ts` — Hybrid data layer (Appwrite → static catalog fallback)
  - `USE_APPWRITE = false` flag; flip to `true` once collections are seeded
  - Functions: `fetchEntity()`, `fetchEntities()`, `searchEntities()`, `fetchEvidence()`, `fetchMedia()`, `fetchTimeline()`
- Defined 8 collections: `entities`, `relationships`, `causes_effects`, `places`, `texts`, `evidence`, `media`, `timeline_entries`
- Created `scripts/migrate_to_appwrite.ts` — Migration script to seed all 11,000+ entities to Appwrite Cloud
  - Uses `node-appwrite` server SDK (v19.1.0)
  - Supports DRY_RUN mode, batched concurrent writes, retry logic
  - Nested arrays (causes, effects, relationships, places, texts) stored as JSON strings
- Appwrite Cloud project: `69cc45e3000d587ea5e6` on `fra.cloud.appwrite.io`
- Env vars: `VITE_APPWRITE_ENDPOINT`, `VITE_APPWRITE_PROJECT_ID`, `VITE_APPWRITE_DATABASE_ID` in `ui/.env`

#### 2. Data Model Harmonization

**TypeScript Entity interface** (`ui/src/data/entityTypes.ts`) — 10 new v2 optional fields:
- `wikidataQid`, `wikipediaUrl`, `imageUrl`, `thumbnailUrl`, `importanceScore`
- `altNames`, `externalLinks`, `tags`, `quote`, `legacySummary`

**Python Pydantic models** (`src/annals/models.py`) — 4 new sub-models + 12+ new fields:
- Sub-models: `CauseEffect`, `Relationship`, `PlaceRef`, `TextRef`
- New BaseNode fields: `summary`, `subjects`, `era`, `era_slug`, `region`, `continent`, `frameworks`, `wikipedia_url`, `image_url`, `thumbnail_url`, `tags`, `quote`, `legacy_summary`
- Person model: added `born: Optional[str]`, `died: Optional[str]`

#### 3. Call Number Division Expansion

Expanded from **101 divisions → 282 sub-divisions** across all 10 classes:

| Class | Heading                  | Before | After |
|-------|--------------------------|--------|-------|
| 0     | Ideas – Core             | 3      | 20    |
| 1     | Ideas – Other Theories   | 7      | 39    |
| 2     | People                   | 9      | 39    |
| 3     | Institutions             | 9      | 43    |
| 4     | Places                   | 7      | 31    |
| 5     | Events                   | 9      | 43    |
| 6     | Movements                | 8      | 40    |
| 7     | Artifacts & Texts        | 8      | 38    |
| 8     | Evidence                 | 5      | 20    |
| 9     | Timeframes               | 6      | 22    |

Key new sub-divisions include:
- **Class 0:** Democracy & Republicanism (011), Natural Law Theory (024), International Law (035)
- **Class 1:** Marxism (113), Astronomy & Cosmology (122), Computing & Digital (136), Mysticism (144)
- **Class 3:** Parliaments (311), Central Banks (331), UN System (371), Universities (381)
- **Class 4:** Sub-Saharan Africa (421), River Valley Civilizations (461), Battlefields (473)
- **Class 5:** World Wars (514), Church Councils (571), Epidemics (583), Economic Crises (592)
- **Class 6:** Nationalism (611), Abolition (621), Protestant Reformation (631), Renaissance (641)
- **Class 7:** Hebrew Bible (731), Quran (733), Paintings (761), Weapons & Armor (772)
- **Class 8:** Inscriptions (811), Excavation Reports (831), Census Data (841)
- **Class 9:** Paleolithic (911), Hellenistic (922), Age of Exploration (941), Cold War Era (961)

Helper functions (`getDivisionHeading`, `getCallNumberBreadcrumbs`) support parent-fallback
for sub-divisions.

#### 4. Entity Page Enhancements

Extended EntityPage from **6 → 10 tabs**:
- New tabs: **Timeline**, **Evidence**, **Media**, **Legacy**
- Created 3 new components:
  - `ui/src/components/EntityTimeline.tsx` — Vertical chronological lifeline
  - `ui/src/components/EntityGallery.tsx` — Media gallery with lightbox
  - `ui/src/components/EntityLegacy.tsx` — Legacy & Influence reverse-lookup
- Overview tab enhanced: alt names display, quote blockquote, Wikidata/Wikipedia badges

#### 5. New Service Layer Types

`ui/src/services/entityService.ts` exports:
- `EvidenceRecord` — id, entitySlug, title, author, year, tier, citation
- `MediaRecord` — id, entitySlug, url, alt, credit, category, caption
- `TimelineEntry` — id, entitySlug, year, endYear, title, description, significance

---

## Update — 2026-03-06

### Frontend: "The Chrononauticum" — React + Chakra UI v3

Launched the Annals of the World frontend application honoring James Ussher's 1650 masterwork.

**Design Philosophy:** Ancient Library (Alexandria aesthetic) meets Temporal Wormhole (Star Trek-inspired portal navigation). "Papyrus & Cosmos" color palette — parchment tones, aged gold accents, serif typography (Cormorant Garamond, Cinzel) for scholarly weight, Inter for body text.

**Pages created:**
- **Library Foyer** (`/`) — Landing page with hero stats, continent cards, jaw-dropping data numbers
- **Africa Dashboard** (`/continents/africa`) — Full 55-country analysis with comparative tables, hidden patterns, regional breakdowns
- **Asia Dashboard** (`/continents/asia`) — 48-country analysis with 180 event windows, Five Asias breakdown, filterable event categories
- **Era Explorer** (`/explore`) — Era/region selector with temporal portal animation (8 epochs, 14 regions)
- **About** (`/about`) — Ussher biography, project mission, roadmap visualization, graph schema display

**Technical stack:** React 18, Vite 5, Chakra UI v3, React Router v6, Lucide icons, Framer Motion, Cormorant Garamond + Inter + Cinzel fonts.

**New analysis:** `analyses/Asia_Continent_Analysis.md` — 48-country deep analysis mirroring the African analysis format. Hidden patterns: Asian Return (not rise), Semiconductor Chokepoint, Youth-Age Collision, Water Wars, AI Triad.

**New docs:** `docs/FRONTEND_PROPOSAL.md` — Complete design proposal with color tokens, typography, iconography, information architecture, data pipeline strategy, and phased delivery plan.

**Chakra MCP:** Configured `.vscode/mcp.json` for Chakra UI MCP integration. API key stored in `ui/.env`.

---

## Update — 2026-01-24T19:45:00Z

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
