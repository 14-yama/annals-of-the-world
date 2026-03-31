## Features by Version
This project tracks schema and governance evolution by version.

### v1 — Foundations
- class.division.id: Librarian-style classification (0–9 classes).
- Core node labels: `Idea`, `Person`, `Institution`, `Place`, `Event`, `Movement`, `Artifact`/`Text`, `Evidence`.
- Authoritative citations (seeded): Chicago-style required; emphasis on peer-reviewed/scholarly sources.
- Corpus discipline tiers: Primary / Peer-reviewed / Scholarly press / Institutional.
- Active voice relationships required.

### v2 — Structured Schema
- Node properties: `name`, `slug`, `definition`, `category`, `context`, `place_type`.
- Place subtypes: `Civilization`, `Tribe`, `Country`, `Region`.
- Idea categories enumerated (Political, Legal, Scientific, etc.).
- Evidence nodes separated from per-edge citations: Evidence = reusable nodes; Citation = per-relationship property.
- Chronology: negative years for BCE; prefer numeric comparisons and range queries.
- Hygiene: constraints + `MERGE` instead of `CREATE` to avoid duplicates.
- Generic vs Contextual: generic timeless hubs (e.g., `Rome`) vs contextual instances (e.g., `Roman Empire 27 BCE–476 CE`).

### v3 — Framework Tags & Historian Lenses
- Historian frameworks introduced (Cause & Effect, Continuity & Change, Cultural Diffusion, Precedent, Symbolism, Influence, Conflict, Temporal Linkage, Economic Systems, Political Systems, Comparative Religion, Empire & Colonialism, Environmental History, Innovation & Technology — 16 total).
- Framework tags initially attached as relationship properties (pre-v4).
- Extended framework registry for politics and institutional analysis.

### v4 — Current Operating Standard
- `EventWindow`: canonical time-bound events with `startYear`, `endYear`.
- Epoch/Era/Period hierarchy: `(:Period)-[:OCCURS_DURING]->(:Era)-[:OCCURS_DURING]->(:Epoch)`.
- Frameworks become first-class nodes: `(:EventWindow)-[:FRAMED_BY {citation}]->(:Framework)`.
- Evidence & citation policy:
  - Required on every `FRAMED_BY` edge.
  - Must include stable DOI/URL, page refs, and a `source_note`.
  - `citation_style` standardized to Chicago 17.
## Features by Version

This document summarizes schema and governance changes across versions (v1 → v5) and the resulting operating standards.

---

### v1 — Foundations

- `class.division.id`: librarian-style classification (0–9 classes).
- Core node labels: `Idea`, `Person`, `Institution`, `Place`, `Event`, `Movement`, `Artifact`/`Text`, `Evidence`.
- Authoritative citations required (Chicago 17 preferred); corpus tiers from Primary → Institutional.
- Enforce active-voice relationships (verb-first labels).

---

### v2 — Structured Schema

- Canonical node properties: `name`, `slug`, `definition`, `category`, `context`, `place_type`.
- Place subtypes: `Civilization`, `Tribe`, `Country`, `Region`.
- Evidence modeled as reusable `:Evidence` nodes; citations stored as per-edge properties.
- Chronology: numeric years (negative for BCE); use `chron_key` for deterministic ordering.
- Hygiene: uniqueness constraints and `MERGE` usage to avoid duplicates.

---

### v3 — Framework Tags & Historian Lenses

- Introduced historian frameworks (Cause & Effect, Continuity & Change, Cultural Diffusion, Influence, Conflict, Temporal Linkage, Economic Systems, Political Systems, Comparative Religion, Empire & Colonialism, Environmental History, Innovation & Technology — 16 total).
- Initially implemented as relationship properties; registry expanded for analysis domains.

---

### v4 — Current Operating Standard

- `EventWindow` as the canonical time-bound event with `startYear`/`endYear`.
- Epoch/Era/Period hierarchy: `(:Period)-[:OCCURS_DURING]->(:Era)-[:OCCURS_DURING]->(:Epoch)`.
- Frameworks are first-class nodes: `(:EventWindow)-[:FRAMED_BY {citation}]->(:Framework)`.
- Citation policy for `FRAMED_BY`: include DOI/URL, page refs, and `source_note`; use Chicago 17.
- Data hygiene: uniqueness constraints, `startYear <= endYear`, relationship fingerprinting, `chron_key` ordering.

---

### v5 — Proposals & Extensions (planned)

- Governance workflow: `Propose → Cite → Frame → Place → Review → Publish → Version`.
- CIDOC CRM E39 Agent alignment (unify `Person` & `Institution` as `Agent`).
- Configurable citation coverage checks (e.g., require Primary + Peer-reviewed for critical edges).
- Evidence corpus tagging: `PRIMARY_CORPUS`, `PEER_REVIEWED`, `SCHOLARLY_PRESS`, `INSTITUTIONAL_REPORTS`.

---

## Master Feature List (concise)

- Classification: `class.division.id` call numbers.
- Chronology: `chron_key` (integer YYYYMMDD) and negative years for BCE.
- Evidence model: `:Evidence` nodes + per-edge citations (Chicago 17 policy).
- Frameworks: historian frameworks as first-class nodes (v4+).
- Agents: E39 Agent alignment (v5 proposal).
- Relationships: active-voice, verb-first, semantically normalized.
- Event hierarchy: `Epoch → Era → Period → EventWindow`.
- Governance & hygiene: uniqueness constraints, temporal sanity, relationship fingerprinting.
- QA: coverage audits, anachronism scans, passive-voice detection.

---

## Corpus model (concise)

- Corpus tiers (`Evidence.corpus_tier`): A — Primary, B — Peer-reviewed, C — Scholarly press, D — Institutional (E/F optional).
- Model `(:Corpus)` and link evidence via `(:Evidence)-[:BELONGS_TO]->(:Corpus)`.
- Keep corpora focused on primary traditions; modern monographs/journals belong to B–D.

