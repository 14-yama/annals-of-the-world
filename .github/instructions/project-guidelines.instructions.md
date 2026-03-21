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
  components/       # Reusable UI components
    DataCards.tsx    # StatCard, InsightCard, DataTable, SectionHeading
    Layout.tsx       # Sidebar + top bar chrome
    InteractiveMap.tsx
    Timeline.tsx
    QuizEngine.tsx
    ...
  pages/            # Route-level page components
    Home.tsx
    AfricaDashboard.tsx
    AsiaDashboard.tsx
    EuropeDashboard.tsx
    AmericasDashboard.tsx
    OceaniaDashboard.tsx
    EraExplorer.tsx
    EraDetail.tsx
    GraphExplorer.tsx
    Quiz.tsx
    About.tsx
    CatalogPage.tsx   # Browsable catalog with advanced search & filters
    EntityPage.tsx     # 3-column Library of Alexandria entity detail
    ...
  data/             # Static data files (JSON/TS)
    entityTypes.ts  # Entity, NodeLabel, relationship interfaces
    catalog/        # Entity catalog (Dewey-style call numbers)
      index.ts      # Central merger + Map-based lookups
      prehistoric.ts
      classical.ts
      medieval.ts
      earlyModern.ts
      modern.ts
      contemporary.ts
      reformation.ts  # Reformation cluster entities
    continents/     # Per-continent skeleton data
    eras/           # Per-era data and imagery metadata
    quizzes/        # Quiz question banks
  types/            # Shared TypeScript types
    index.ts        # Core domain types
  constants/        # App-wide constants
    callNumbers.ts  # Dewey-style classification (10 classes, 48+ divisions)
    eras.ts
    regions.ts
    continents.ts
    frameworks.ts   # Historical frameworks from docs/
  hooks/            # Custom React hooks
  utils/            # Helper functions
  theme.ts          # Chakra system theme
  App.tsx           # Root router
  main.tsx          # Entry point
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
| Classical / Ancient    | 3,000 BCE – 500 CE  | #8B4513 | 920      |
| Medieval               | 500 – 1500 CE       | #A67C2E | 930      |
| Early Modern           | 1500 – 1800 CE      | #C5963A | 940      |
| Modern                 | 1800 – 1945 CE      | #4A90D9 | 950      |
| Contemporary           | 1945 CE – Present   | #6B3FA0 | 960      |

---

## Continent Coverage

| Continent | Status     | Countries | Data Points       |
| --------- | ---------- | --------- | ----------------- |
| Africa    | Enhanced   | 55        | 319/country       |
| Asia      | Enhanced   | 48        | 180 event windows |
| Europe    | Skeleton   | 44        | Basic profiles    |
| Americas  | Skeleton   | 35        | Basic profiles    |
| Oceania   | Skeleton   | 14        | Basic profiles    |

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

## Catalog & Search Architecture

### Entity Catalog

The catalog uses a Dewey Decimal-inspired call number system:
- **Format:** `Class.Division.Slug` (e.g., `220.06-julius-caesar`)
- **10 Classes (0-9):** Ideas, Theories, People, Institutions, Places,
  Events, Movements, Texts, Evidence, Timeframes
- **48+ Divisions:** Further categorization under each class
- **Data files:** 6 era modules + reformation module in `ui/src/data/catalog/`
- **Index:** Central merger with Map-based O(1) lookups by slug or call number

### Advanced Search

- **Autocomplete typeahead:** Debounced fuzzy search with dropdown results
- **Multi-field matching:** name, call number, subjects, summary, era, label,
  continent, region, frameworks
- **Filters:** Era, Label/Type, Continent, Framework (combinable)
- **Layered drill-down:** Class → Division → Entity; Era → Type → Entity
- **Breadcrumb navigation:** Clickable path segments for filtered views

### Data Sources

- **Static catalog:** `ui/src/data/catalog/*.ts` — hand-curated entities
- **Reformation clusters:** `data/Nodes/nodes.*.json` — 12+ reformation clusters
- **Geo-registry:** `geo-registry/places/countries/*/index.json` — 199 country profiles
- **Phase 2:** Neo4j-backed dynamic queries for 1M+ node scale
