## Annals of the World — Project Summary

Short purpose

Build a scholarly, auditable historical knowledge graph (Neo4j) that models ideas, people, places, events, institutions, texts/artifacts, movements, and evidence across time and space for rigorous, cross‑civilizational analysis.

Core elements

- Nodes: `Idea`, `Person`, `Institution`, `Place`, `Event`/`EventWindow`, `Movement`, `Artifact`/`Text`, `Evidence`, `Corpus`, `Framework`, `Timeframe`.
- Relationships: active-voice, verb-first (e.g., `INFLUENCES`, `OCCURRED_IN`, `FRAMED_BY`).
- Classification: `class.division.id` call numbers for faceted discovery.

Evidence & citation policy

- Evidence-first: `:Evidence` nodes are reusable; critical interpretive edges (especially `FRAMED_BY`) must include citation metadata.
- Required fields on `FRAMED_BY`: `citation_style` (Chicago 17), `evidence_url`/DOI, `page_refs`, and `source_note`.

Chronology & ordering

- Use numeric years (negative for BCE). 
- Represent time-bound events with `EventWindow` nodes (`startYear`, `endYear`).
- Use `chron_key` (integer YYYYMMDD) for deterministic ordering and UI rendering.

Governance & workflow

- Curator workflow: Propose → Cite → Frame → Place → Review → Publish → Version.
- Governance rules: uniqueness constraints per label, relationship fingerprinting to avoid duplicates, RFC process for adding frameworks or major schema changes, and no silent overwrite of published data.

QA, ingestion, and scale

- Ingestion: prefer `MERGE` to reduce duplicates; enforce constraints where possible.
- QA checks: audit queries for missing `FRAMED_BY`, passive-voice relationship names, temporal sanity, and corpus coverage.
- Sharding strategy: partition/serve data by `Timeframe`/era for scalability.

Data sources

| Dataset | Entities | Source | File |
|---------|----------|--------|------|
| Annals Catalog | 16,505 | Hand-curated + auto-generated | `ui/src/data/catalog/index.ts` |
| Wikidata People | 238,466 | Wikidata SPARQL (131 occupation QIDs) | `data/wikidata_people.json` |
| Wikidata Institutions | 36,738 | Wikidata SPARQL (213 type QIDs) | `data/wikidata_institutions.json` |
| Geo-Registry | 199 countries | ISO + manual curation | `geo-registry/places/countries/` |

Where to read more

- Schema & implementation notes: [docs/guidelines/schema.md](./guidelines/schema.md)
- Curator workflow: [docs/guidelines/workflow.md](./guidelines/workflow.md)
- Classification & call numbers: [docs/guidelines/classification.md](./guidelines/classification.md)
- International call number & subject heading system: [docs/guidelines/call_number_subject_heading_system.md](./guidelines/call_number_subject_heading_system.md)
- Feature timeline: [docs/guidelines/features_by_version.md](./guidelines/features_by_version.md)
- Wikidata fetch methodology: [docs/guidelines/wikidata_fetch_guide.md](./guidelines/wikidata_fetch_guide.md)

Next options

- I can add [docs/guidelines/README.md](./guidelines/README.md) as a guidelines index, or create [docs/guidelines/audit_queries.md](./guidelines/audit_queries.md) with runnable Cypher checks. Tell me which to do next.

