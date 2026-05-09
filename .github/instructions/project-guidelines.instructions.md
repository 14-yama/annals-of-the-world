---
applyTo: "**"
---

# Annals of the World — Project Guidelines

## Vision

Annals of the World is a Neo4j-backed historical knowledge graph that models people,
ideas, places, events, institutions, texts, movements, and evidence across 72,000 years
of human history — from Prehistory to the Digital Age. The project honors Archbishop
James Ussher's 1650 *Annales Veteris Testamenti* using 21st-century data science.

**Goal:** 1,000,000 nodes, Wikimedia/Wikidata integration, scholarly auditability.

---

## Tech Stack

| Layer       | Technology                                                |
| ----------- | --------------------------------------------------------- |
| Frontend    | React 18, Vite 5, TypeScript strict                       |
| UI          | Chakra UI v3 (Papyrus & Cosmos theme)                     |
| Viz         | D3.js, React Simple Maps, Leaflet, Recharts, Canvas 2D    |
| Animations  | Framer Motion, CSS keyframes                              |
| Icons       | Lucide React                                              |
| Backend     | Python 3.12, Pydantic, Neo4j 5.10                         |
| Data        | Static JSON/CSV (MVP), Neo4j Cypher (Phase 2+)            |
| CI          | GitHub Actions (flake8, mypy, pytest)                      |
| License     | CC0 1.0 Universal (public domain)                         |

---

## File & Folder Conventions

### UI (`ui/src/`)

```
ui/src/
  App.tsx             # Root router (36+ routes)
  main.tsx            # Entry: React + Router + Chakra + Theme
  theme.ts            # Chakra system theme (Papyrus & Cosmos)

  components/         # 11 reusable UI components
    DataCards.tsx      # StatCard, InsightCard, DataTable, SectionHeading
    Layout.tsx         # Sidebar + top bar chrome
    AdvancedSearch.tsx # Fuzzy typeahead with filter dropdowns
    InteractiveMap.tsx # Choropleth & geographic visualization
    Timeline.tsx       # Chronological event visualization
    CausalChain.tsx    # Case study causal flow diagram
    SunburstChart.tsx  # Hierarchical sunburst visualization
    RadarChart.tsx     # Multi-dimensional radar chart
    QuizEngine.tsx     # Quiz Q&A interface
    CivilizationGallery.tsx # Era-based civilization showcase
    Breadcrumb.tsx     # Filtered view navigation

  pages/              # 34 route-level page components
    Home.tsx
    # Continent Dashboards (5)
    AfricaDashboard.tsx    # Enhanced — 55 nations, 319+ data points/country
    AsiaDashboard.tsx      # Enhanced — 48 nations, 180 event windows
    EuropeDashboard.tsx    # Enhanced — 44 nations
    AmericasDashboard.tsx  # Enhanced — 35 nations
    OceaniaDashboard.tsx   # Enhanced — 14 nations
    # Era & Exploration
    EraExplorer.tsx        # Browse eras with civilizations
    EraDetail.tsx          # Per-era deep dive
    GraphExplorer.tsx      # D3 force-directed knowledge graph
    CaseStudyExplorer.tsx  # Causal chain case studies
    HumanStory.tsx         # Human experience narratives
    # Catalog & Entity
    CatalogPage.tsx        # Browsable catalog with advanced search & filters
    EntityPage.tsx         # 3-column Library of Alexandria entity detail
    # Corpus
    CorpusHub.tsx          # Corpus overview & navigation
    BiblicalCorpusPage.tsx # Biblical corpus deep dive
    CorpusPage.tsx         # Generic corpus page (/corpus/:corpusSlug)
    # Topic Pages (13)
    WeaponsPage.tsx, LanguagesPage.tsx, ArchitecturePage.tsx,
    MedicinePage.tsx, AgriculturePage.tsx, NavigationPage.tsx,
    TribesPage.tsx, TransportationPage.tsx, ClothingPage.tsx,
    MarriagePage.tsx, CustomsPage.tsx, PunishmentPage.tsx, IdeasPage.tsx
    TopicsHub.tsx          # Topic index page
    # Documentation & Reference
    DocsPage.tsx           # Verb glossary, node types, evidence tiers, conventions
    QuizPage.tsx           # Interactive quizzes
    About.tsx              # Project about page
    Curator.tsx            # Curator workflow interface
    AuditLogViewer.tsx     # Edit audit trail viewer (/curator/audit/log)
    Triage.tsx             # Data triage tool
    Demo.tsx               # Entity page demo

  data/                # Static data files (JSON/TS)
    entityTypes.ts     # Entity, NodeLabel, relationship interfaces
    entities.ts        # Master entity array
    iso-numeric-map.ts # Country ISO codes
    reformations-graph.json # Reformation clusters
    # Topic data (20+ files)
    agriculture.ts, architecture.ts, clothing.ts, customs.ts,
    ideas.ts, languages.ts, marriage.ts, medicine.ts, navigation.ts,
    punishment.ts, trade-routes.ts, transportation.ts, tribes.ts, weapons.ts,
    world-diet.ts, world-languages.ts
    case-studies.ts    # Case study data
    quizzes.ts         # Quiz question banks
    timeline-events.ts # Timeline event data
    catalog/           # Entity catalog (Dewey-style call numbers)
      index.ts         # Central merger + Map-based O(1) lookups
      prehistoric.ts, classical.ts, medieval.ts, earlyModern.ts,
      modern.ts, contemporary.ts, biblical.ts, reformation.ts
      divisionEnrichment.ts  # Additional Dewey entities
      geoRegistry.ts         # Place/country entities
      topicConverter.ts, topicRegistry.ts, topicEntities.ts
      corpuses/        # 14 corpus entity files
        mesopotamian.ts, egyptianAncient.ts, judaicRabbinic.ts,
        graecoRoman.ts, canonLaw.ts, iranCentralAsia.ts,
        southSEAsia.ts, eastAsia.ts, africa.ts, americas.ts,
        europeBatch1.ts, europeBatch2.ts, scienceTech.ts, registry.ts

  types/               # Shared TypeScript types
    index.ts           # Core domain types (Entity, Era, GraphNode, etc.)

  constants/           # App-wide constants
    callNumbers.ts     # Dewey-style classification (10 classes, 81 divisions)
    eras.ts            # 6 era definitions with civilizations
    regions.ts         # Geographic regions
    continents.ts      # Continent profiles
    frameworks.ts      # 16 interpretive frameworks
```

### Backend (`src/annals/`)

```
src/annals/
  models.py         # Pydantic node models (BaseNode, Person, Place, etc.)
  config.py         # Neo4j connection config
  db.py             # Database driver helper
  validators.py     # QA validators (active voice, evidence checks)
```

### Data (`data/`)

```
data/
  Nodes/            # JSON node files per cluster
  Relationships/    # JSON relationship files per cluster
  Evidence/         # Scholarly source evidence files
```

---

## Coding Standards

### TypeScript / React

- **Strict mode** enforced via `tsconfig.json`
- **Named exports** preferred for components; default export only for page-level routes
- **Component naming:** PascalCase files and components
- **Props:** Define explicit interface types; avoid `any`
- **Hooks:** Prefix custom hooks with `use`
- **State:** Use React state + context; no external state libs for MVP
- **Styling:** Use Chakra UI tokens from theme.ts; avoid hardcoded hex except in
  theme definitions or one-off canvas/SVG rendering
- **Imports:** Group: React → third-party → local components → local data → types

### Python

- **PEP 8** enforced via flake8
- **Type hints** required; checked via mypy
- **Models:** Pydantic BaseModel for all data structures
- **Tests:** pytest in `tests/`

---

## Design System — "Papyrus & Cosmos"

### Color Palette

| Token     | Hex Range           | Usage                            |
| --------- | ------------------- | -------------------------------- |
| papyrus   | #FAF3E8 → #2C1810  | Page backgrounds, card surfaces  |
| cosmos    | #E8F0FE → #082340  | Portal animations, links         |
| era       | #FFF5EB → #1A0D04  | Era-specific accents             |
| gold      | #FDF8ED → #4A310D  | Headings, accent bars, highlights|

### Typography

| Role    | Font                          | Usage              |
| ------- | ----------------------------- | ------------------ |
| Heading | Cormorant Garamond            | Section headings   |
| Body    | Inter                         | Paragraph text     |
| Display | Cinzel                        | Hero titles, logos |
| Mono    | JetBrains Mono                | Code, slugs        |

### Component Patterns

- **StatCard** — Colored accent bar + large value + label
- **InsightCard** — Dot indicator + title + narrative insight + source
- **DataTable** — Dark header + striped rows + scrollable
- **SectionHeading** — Serif title + muted subtitle + golden underline

---

## Knowledge Graph Schema (v4)

### Core Labels (11)

Idea · Person · Place · EventWindow · Institution · Movement · Text ·
Evidence · Corpus · Framework · Timeframe · Polity

### Relationship Governance

- **Active voice only:** CAUSES, INFLUENCES, FRAMES, OCCURS_IN, DEFINES,
  TRANSFORMS, CANONIZES, TRANSMITS, CONTAINS, OCCURS_DURING
- **Evidence required:** All interpretive edges must include `FRAMED_BY` with
  `citation_style`, `evidence_url`, `page_refs`, `source_note`

### Curator Workflow (6 stages)

1. Propose → 2. Cite → 3. Frame → 4. Place → 5. Review → 6. Publish

---

## Visualization Guidelines

- **No basic bar charts** for primary data storytelling; use:
  - D3 force-directed graphs for knowledge graph
  - Choropleth maps (React Simple Maps / Leaflet) for geographic data
  - Sunburst / treemaps for hierarchical data
  - Sankey diagrams for flow/relationship data
  - Timeline visualizations for chronological data
  - Radar/spider charts for multi-dimensional comparisons
- **Canvas 2D** for large datasets (1000+ nodes)
- **SVG** for smaller, interactive visualizations
- **Accessibility:** All visualizations must have text alternatives

---

## Era Framework

| Era                    | Period              | Color   | Division |
| ---------------------- | ------------------- | ------- | -------- |
| Prehistoric            | Before 3,000 BCE    | #6B4D1B | 910      |
| Classical              | 3,000 BCE – 500 CE  | #8B4513 | 920      |
| Medieval               | 500 – 1500 CE       | #A67C2E | 930      |
| Early Modern           | 1500 – 1800 CE      | #C5963A | 940      |
| Modern                 | 1800 – 1945 CE      | #4A90D9 | 950      |
| Contemporary           | 1945 CE – Present   | #6B3FA0 | 960      |

---

## Continent Coverage

| Continent | Status     | Countries | Data Sections                                    |
| --------- | ---------- | --------- | ------------------------------------------------ |
| Africa    | Enhanced   | 55        | Stats, Demographics, Economic, Health, Freedom, Patterns, Regions |
| Asia      | Enhanced   | 48        | Stats, Continental, Wealth, Governance, Health, Events (180), Five Asias, Patterns |
| Europe    | Enhanced   | 44        | Stats, Demographics, Economic, Governance, EU, Health, Patterns, Regions |
| Americas  | Enhanced   | 35        | Stats, Demographics, Economic, Governance, Indigenous, Health, Patterns, Regions |
| Oceania   | Enhanced   | 14        | Stats, Demographics, Economic, Governance, Health, Environment, Navigation, Patterns, Regions |

---

## Commit & PR Conventions

- **Conventional Commits:** `feat(ui):`, `fix(graph):`, `docs:`, `chore:`
- **Branches:** `feat/`, `fix/`, `docs/`, `refactor/`
- **PRs:** Focused changes, link to issues, include screenshots for UI work
- **No force pushes** on shared branches
- **CI must pass** before merge (lint + typecheck + test)

---

## Testing

- **Python:** `pytest tests/` — unit tests for models, validators, scripts
- **UI:** Manual testing via dev server (automated tests planned Phase 2)
- **Data QA:** Cypher audit queries in `docs/guidelines/audit_queries.md`

---

## Security

- No secrets in code; use `.env` files (gitignored)
- Sanitize all user inputs in search/filter components
- CSP headers planned for production deployment
- CC0 license — no proprietary data restrictions

---

## Audit & Governance System

### Edit Audit Trail

All curator edits are logged to the `audit_log` Appwrite collection with per-field diffs:
- **Curator identity** tracked via `editorId` (localStorage + prompt)
- **Session tracking** via `sessionId` (crypto.randomUUID per browser session)
- **Per-field diffing** — each changed field gets its own audit entry with old/new values
- **Audit log viewer** at `/curator/audit/log` — filters, sort, CSV export, stats; uses **Appwrite Realtime WebSocket** subscription so new rows appear instantly (no polling)

### Appwrite Cloud Functions (5 automated audits)

| Function | Schedule | Purpose |
|----------|----------|---------|
| `audit-completeness` | Daily 02:00 UTC | Score entities on 9 quality dimensions |
| `audit-orphans` | Daily 03:00 UTC | Find entities with zero relationships |
| `audit-duplicates` | Weekly Sun 04:00 | Levenshtein fuzzy duplicate detection |
| `audit-consistency` | Daily 05:00 UTC | Validate era/division, callNumber, slugs |
| `backup-export` | Weekly Sun 00:00 | Export all collections to Appwrite Storage |

Functions are defined in `appwrite.json` and implemented in `functions/*/src/main.js`.

### Backup & Sync

- **Export:** `APPWRITE_API_KEY=<key> npx tsx scripts/sync_appwrite_to_repo.ts`
- **Import:** `APPWRITE_API_KEY=<key> npx tsx scripts/sync_repo_to_appwrite.ts [--dry-run] [--force]`
- **Export location:** `data/appwrite-export/entities/{classCode}-{className}/{divisionCode}.json`
- **Appwrite is the live source of truth;** JSON exports are the backup copy

### Deprecated Catalog

Entity data files moved from `ui/src/data/catalog/*.ts` to `ui/src/data/deprecated-catalog/`.
`catalog/index.ts` still works — imports redirect to deprecated-catalog. Existing script
imports are unaffected.

### Autonomous AI Enrichment Pipeline

Fully automated, **cloud-first** enrichment — no local machine required. All bots run on
GitHub Actions and commit directly to the GitHub repository. Appwrite is updated
automatically by the sync gateway workflow after each enrichment commit.

| Component | Path | Purpose |
|-----------|------|---------|
| Queue Scanner | `scripts/enrichment_queue.py` | Ranks entities by weakness score |
| AI Enrichment | `scripts/ai_enrich_autonomous.py` | Calls LLM + validates + writes JSON (git-first, no Appwrite calls) |
| Sync Gateway | `scripts/sync_gateway.ts` | Single Appwrite writer — reads git diff, upserts entities, emits audit_log rows |
| Enrichment Workflow | `.github/workflows/ai-enrichment.yml` | Cron every 6h + manual dispatch; commits enriched files + pushes to GitHub |
| Sync Workflow | `.github/workflows/sync-gateway.yml` | Auto-triggered by enrichment workflow completion + daily 07:00 UTC; commits budget/state |
| Policy Doc | `docs/governance/autonomous_enrichment.md` | Full governance & thresholds |

**Workflow chain (fully cloud, no local dependency):**
```
GitHub Actions (cron/manual)
  → enrichment_queue.py   (scans 392k entities, ranks by weakness)
  → ai_enrich_autonomous.py  (Gemini/OpenAI → validates → writes JSON)
  → git commit + git push  (changes land in GitHub repo)
  → sync-gateway workflow triggers automatically (workflow_run event)
  → sync_gateway.ts  (git diff → PATCH/POST Appwrite → emit audit_log rows)
  → git commit + git push  (budget.json + last_sync.json updated)
```

**Local development sync:** A systemd user service (`scripts/auto_pull.service`) runs
`scripts/auto_pull.sh` every 60s to `git fetch + pull --ff-only` from GitHub, so the
local machine stays in sync with cloud bot commits automatically.

**LLM Providers:**
- **Primary:** Google Gemini 2.5 Flash (free tier: 1M tokens/day, 15 RPM)
- **Fallback:** OpenAI GPT-4o-mini ($0.15/1M input, $0.60/1M output)

**Summary quality standards:**
- 3–4 paragraphs separated by `\n\n` (rendered as separate `<Text>` blocks in UI)
- 800–2,000 characters total (rich, vivid, scholarly — no placeholder stubs)
- Para 1: Identity + dates + significance; Para 2: What happened; Para 3: Legacy; Para 4 (optional): vivid closing fact/quote
- Validation gate rejects: summary <600c or >3000c (auto-trimmed at 2000c), <2 causes/effects, <3 relationships

**GitHub Secrets required:** `GEMINI_API_KEY`, `APPWRITE_API_KEY` (optional: `OPENAI_API_KEY`)

---

## Catalog & Search Architecture

### Annals Catalog — Single Source of Truth

The **Annals Catalog** (`ui/src/data/catalog/index.ts`) is the canonical, authoritative
record of all actors in the dataset. Every node documented in the project — whether from
the backend knowledge graph, geo-registry, corpus catalog, topic collections, or
hand-curated era files — **must** be represented in the Annals Catalog.

**Current count: 40,000+ entities across 6 canonical eras (backed by Appwrite).**

| Metric | Value |
| ------ | ----- |
| Total unique actors | 40,000+ |
| Eras | 6 (Prehistoric, Classical, Medieval, Early Modern, Modern, Contemporary) |
| Countries | 199 |
| Entity types | 8 (EventWindow, Person, Movement, Institution, Text, Idea, Place, Evidence) |
| Frameworks | 16 interpretive frameworks auto-assigned |

### Catalog Source Pipeline

All data sources feed **into** the Annals Catalog (not counted separately):

| Source | Pre-dedup Count | Module |
| ------ | --------------- | ------ |
| Geo-Registry (199 countries × 6 eras) | 9,380 | `catalog/geoRegistry.ts` — auto-generated by `scripts/generate_geo_catalog.py` |
| Topic Catalog (12 collections) | 622 | `catalog/topicEntities.ts` — weapons, tribes, languages, etc. |
| Hand-Curated Era Catalogs | 216 | `catalog/prehistoric.ts` through `catalog/contemporary.ts` |
| Division Enrichment | 114 | `catalog/divisionEnrichment.ts` |
| Biblical + Reformation | 119 | `catalog/biblical.ts`, `catalog/reformation.ts` |
| Corpus Catalog (13 collections) | 166 | `catalog/corpuses/*.ts` |
| Text Node Entities | 386 | `catalog/textNodes.ts` — auto-generated from actor text references |
| Wikidata People | 5,014 | `catalog/wikidataPeople.ts` — notable figures from Wikidata SPARQL |

After slug-based deduplication (hand-curated wins over auto-generated), the catalog
contains **40,000+ unique actors** (catalog + Wikidata enrichment).

### Adding New Nodes

When adding new nodes to the project:
1. **Geo-registry nodes:** Add to `geo-registry/places/countries/{slug}/index.json`,
   then regenerate: `python3 scripts/generate_geo_catalog.py`
2. **Hand-curated nodes:** Add directly to the appropriate era file in `ui/src/data/catalog/`
3. **Corpus nodes:** Add to the appropriate corpus file in `ui/src/data/catalog/corpuses/`
4. **Topic nodes:** Add to the topic data file in `ui/src/data/` (auto-converted)
5. **All new nodes automatically appear** in `ALL_CATALOG_ENTITIES` via `catalog/index.ts`

### Entity Quality Requirements

Every entity in the catalog must have:
- **`summary`** — A rich, concise overview (see Overview Writing Standards below)
- **`causes`** — At least 3 causal antecedents for major entities (1 minimum for minor)
- **`effects`** — At least 3 consequent outcomes for major entities (1 minimum for minor)
- **`relationships`** — Minimum edge count determined by `historicalSignificance.significanceScore`
  (see Significance → Edge Count Metric below)
- **`historicalSignificance`** — Required on all enriched entities (summary ≥ 600c):
  `{significanceScore: 1–10, significanceNarrative: string, significanceCategory: "world-changing"|"continental"|"regional"|"local"}`
- **`frameworks`** — At least 1 interpretive framework
- **`places`** — At least 1 place reference
- **`subjectHeadings`** — Hierarchical heading: `Label — Cluster — Country — Era`
- **`subjects`** — Country + topic tags (8–10 for major entities)

### Significance → Edge Count Metric

Every enriched entity **must** have a minimum number of graph edges proportional to its
historical significance. An entity like Albert Einstein (score 10) with only 2 edges is
a data quality failure — significance and connectivity must match.

| `significanceScore` | Category | Min Edges Required | Example entities |
|---|---|---|---|
| **9–10** | world-changing | **15** | Einstein, Islam, French Revolution, printing press |
| **7–8** | continental | **8** | Napoleon, Mongol Empire, Black Death, Roman Republic |
| **5–6** | regional | **4** | Major battles, key inventors, important institutions |
| **3–4** | local | **2** | Secondary rulers, regional movements, specialist texts |
| **1–2** | minor | **1** | Local events, footnote figures |
| unrated | — | **0** (no requirement) | Stubs awaiting enrichment |

**Enforcement:**
- `audit-consistency` bot flags under-edged entities as quality violations
- `enrichment_queue.py` applies a **2× priority multiplier** to entities where
  `current_edges < min_edges_required(significanceScore)`
- `ai_edge_bot.py` targets high-significance entities first when generating new edges
- The `EntityPage` UI shows an edge-completeness bar when `historicalSignificance` is present

**Validation helper** (TypeScript, used across UI):
```ts
export function minEdgesForScore(score: number): number {
  if (score >= 9) return 15;
  if (score >= 7) return 8;
  if (score >= 5) return 4;
  if (score >= 3) return 2;
  return 1;
}
```

### Overview Writing Standards

Entity summaries must follow these standards for readability and quality:

| Aspect | Guideline |
|--------|-----------|
| **Structure** | 3–4 paragraphs separated by `\n\n` (rendered as separate `<Text>` blocks) |
| **Length** | 800–1,300 characters total (rich but concise — never a wall of text) |
| **Paragraph 1** | Identity + dates + core significance (who, when, why they matter) |
| **Paragraph 2** | Key achievements, events, or contributions (the "what happened") |
| **Paragraph 3** | Impact, consequences, or legacy (the "so what") |
| **Paragraph 4** | (Optional) A vivid closing fact, quote, or lasting cultural footprint |
| **Tone** | Scholarly but engaging — avoid dry encyclopedia prose |
| **Specifics** | Include concrete dates, numbers, and named events (not vague generalities) |
| **Avoid** | Single-paragraph walls of text, placeholder summaries, slug-like descriptions |
| **Quotes** | One memorable quote per entity is encouraged (attributed, in single quotes) |

**Examples of good opening lines:**
- "Aristotle (384–322 BCE) was a Greek philosopher and polymath whose works constitute the first comprehensive system of Western philosophy."
- "Nelson Mandela (1918–2013) was a South African anti-apartheid revolutionary who served as the country's first Black president."

**Anti-patterns to avoid:**
- "A notable figure associated with X" (geo-registry auto-stub — must be replaced)
- Single paragraphs of 1,500+ characters with no breaks
- Summaries under 200 characters (indicates stub quality)

### Deduplication

The catalog index (`index.ts`) deduplicates by slug using first-occurrence-wins:
- Hand-curated entities load first → always win over auto-generated
- Geo-registry entities load last → yield to richer hand-curated versions
- Within geo-registry, duplicate slugs get country suffix (e.g., `independence-kenya`)

### Entity Catalog Call Numbers

The catalog uses a Dewey Decimal-inspired call number system:
- **Format:** `Class.Division.Slug` (e.g., `220.06-julius-caesar`)
- **10 Classes (0-9):** Ideas, Theories, People, Institutions, Places,
  Events, Movements, Texts, Evidence, Timeframes
- **81 Divisions:** Further categorization under each class
- **Data files:** 6 era modules + reformation + biblical modules in `ui/src/data/catalog/`
- **Corpus files:** 14 corpus entity files in `ui/src/data/catalog/corpuses/`
- **Index:** Central merger with Map-based O(1) lookups by slug or call number

### Advanced Search

- **Autocomplete typeahead:** Debounced fuzzy search with dropdown results
- **Multi-field matching:** name, call number, subjects, summary, era, label,
  continent, region, frameworks
- **Filters:** Era, Label/Type, Continent, Framework (combinable)
- **Layered drill-down:** Class → Division → Entity; Era → Type → Entity
- **Breadcrumb navigation:** Clickable path segments for filtered views

### Data Sources

- **Annals Catalog (source of truth):** `ui/src/data/catalog/index.ts` — 16,505 catalog actors + 24,000+ Wikidata entities = 40,000+ in Appwrite
- **Appwrite Backend:** 2,800 Person entities seeded (from 238,466 Wikidata people dataset)
- **Geo-registry JSON:** `geo-registry/places/countries/*/index.json` — 199 country profiles
- **Backend graph data:** `data/Nodes/*.json` — raw nodes for Neo4j seeding
- **Wikidata master dataset:** `data/wikidata_people.json` — 238,466 people (backend only, 289 MB)
- **Phase 2:** Neo4j-backed dynamic queries for 1M+ node scale

---

## Application Routes (36+)

| Route | Page | Purpose |
|-------|------|---------|
| `/` | Home | Landing page |
| `/continents/{name}` | *Dashboard | 5 continent dashboards |
| `/explore` | EraExplorer | Browse all eras |
| `/explore/:eraId` | EraDetail | Single era deep dive |
| `/catalog` | CatalogPage | Browsable catalog + search |
| `/cat/:callNumber` | CatalogPage | Filtered by Dewey class |
| `/entity/:slug` | EntityPage | 3-column entity detail |
| `/graph` | GraphExplorer | D3 force-directed graph |
| `/case-studies` | CaseStudyExplorer | Causal chain case studies |
| `/human-story` | HumanStory | Human experience narratives |
| `/corpus` | CorpusHub | Corpus overview |
| `/corpus/biblical` | BiblicalCorpusPage | Biblical corpus deep dive |
| `/corpus/:corpusSlug` | CorpusPage | Per-corpus page |
| `/topics` | TopicsHub | Topic index |
| `/{topicName}` | *Page | 13 topic pages |
| `/quiz` | QuizPage | Interactive quizzes |
| `/docs` | DocsPage | Documentation + glossary |
| `/about` | About | Project info |
| `/curator` | Curator | Curator workflow |
| `/triage` | Triage | Data triage tool |
| `/demo` | Demo | Entity page demo |

---

## Documentation Architecture

### In-App Documentation (DocsPage.tsx — `/docs`)

The DocsPage serves as the in-app reference with 4 tabbed sections:
- **Edge Glossary:** 55+ searchable relationship verbs (Core, Supplementary, Corpus tiers)
- **Node Types:** 10 core labels with descriptions and abbreviations
- **Evidence Tiers:** 6-tier hierarchy (A: Primary → F: Oral/Quantitative)
- **Conventions:** Call numbers, slugs, active voice, evidence requirements, era framework

### External Documentation (`docs/`)

| Directory | Purpose |
|-----------|---------|
| `docs/guidelines/` | 23 guideline files: schema, curator workflow, classification, conventions |
| `docs/governance/` | Decision authority, audit logs, APOC reference |
| `docs/schema/` | Event kinds, property enumerations |
| `docs/registry/` | Global cluster registry, ISO country codes |
| `docs/nodes/` | Node attribute registry, master node list, place name variants |
| `docs/clusters/` | 16 cluster directories (Reformation variants, Hebrew Tradition, etc.) |
| `docs/workflows/` | Curator workflow templates, readme-to-graph pipeline |
| `docs/case-studies/` | Case study index (content in cluster folders) |
