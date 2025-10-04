---
title: CRM/PROV → Neo4j Crosswalk
status: DRAFT
summary: A compact mapping between CIDOC-CRM / W3C PROV concepts and the project's active-voice Neo4j verbs and node shapes.
---

# CRM / PROV → Neo4j Crosswalk (summary)

Purpose: help curators translate archival and provenance concepts from CIDOC CRM and W3C PROV into the project's active-voice graph model.

High-level mapping (examples)
- PROV:Activity -> :Event / :EventWindow
  - Use Neo4j label `:EventWindow` for bounded historical processes; link to `:Framework` via `FRAMED_BY` for interpretation.
- PROV:Entity -> :Text | :Artifact | :Evidence
  - Attach `:Evidence` nodes for primary/reusable sources; use inline `evidence` for single-use refs.
- PROV:Agent -> :Person | :Institution
  - Use `:Person`/`:Institution` and active verbs (e.g., `ORGANIZES`, `PUBLISHES`, `ESTABLISHES`).
- PROV:wasGeneratedBy -> (Entity)-[:PUBLISHED_BY|:CREATED_BY]->(Agent)
  - Prefer `PUBLISHES` or `AUTHOR_OF` depending on directionality.
- PROV:used -> (Activity)-[:USES]->(Entity)
  - Map to `DEPLOYS`, `USES`, or `REFERENCES` (choose canonical verb per `relations_vocabulary.md`).
- PROV:wasDerivedFrom -> (Entity)-[:DERIVES_FROM]->(Entity)
  - Map to `TRANSLATES`, `ADAPTS`, or `TRANSMITS` depending on context.

Practical rules
- When migrating PROV datasets, favor explicit verbs from `relations_vocabulary.md` and add `FRAMED_BY` edges where interpretive choice is required.
- Capture PROV timestamps into node properties (`created_at`, `startYear`, `endYear`) and provenance nodes `:Provenance` where needed.
- Where PROV records multiple agents with roles, create `:Provenance` node(s) with role metadata and link with `:HAS_PROVENANCE`.

Example translation
- PROV:Entity (manuscript A) —wasGeneratedBy→ PROV:Activity (copying event) —wasAssociatedWith→ PROV:Agent (scribe X)

Neo4j pattern:
(:Text {slug:'manuscript-a'})-[:DERIVES_FROM {evidence:'A: shelfmark x'}]->(:Text {slug:'exemplar'})
(:Copying_Event {slug:'copying-123', startYear:1100})-[:OCCURRED_IN]->(:Place {slug:'yavneh'})
(:Scribe_X:Person)-[:PARTICIPATES_IN]->(:Copying_Event)

End of crosswalk (draft). Curators should adapt mappings to local PROV schema variations.
