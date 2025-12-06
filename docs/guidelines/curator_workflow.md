# Workflow Walkthrough — Active Voice, Class Nodes as Subjects

This document records the project workflow in active present tense, with class nodes (Person, Institution, EventWindow, Idea, Place, Artifact, etc.) acting as the grammatical subjects for every step. This follows the Active Relationship Standard and ensures no passive framing.

## Overview

Person proposes → Bot (Ingest Agent) validates → Graph records with provenance → Policy System audits → Institution publishes.

Each step below is written so that class nodes are the active subjects.

---

## 📘 1. Propose

- Person (Curator) proposes a new node (Idea, Person, EventWindow, Place, Institution, Artifact).
- Bot (Ingest Agent) validates schema (labels, categories, slugs, uniqueness) and prevents duplicates.
- Graph writes nodes and edges with provenance fields using MERGE.
- Policy System checks uniqueness, active-voice compliance, and node integrity.

---

## 📘 2. Cite

- Person (Curator) attaches a source (DOI, URL, book reference).
- Bot (Ingest Agent) normalizes the citation into Dublin Core fields and Chicago 17 style.
- Graph links nodes with `FRAMED_BY` edges carrying `evidence_url`, `citation_style`, `page_refs`, and `source_note`.
- Policy System audits citation validity and formatting.

---

## 📘 3. Frame

- Person (Curator) selects a framework (Cause & Effect, Precedent, Cultural Diffusion, etc.).
- Bot (Ingest Agent) resolves the framework from the registry of first-class nodes.
- EventWindow links to Framework with `FRAMED_BY` edges (each edge carries its own citation).
- Policy System monitors framework coverage to maintain interpretive balance.

---

## 📘 4. Place

- Person (Curator) assigns spatial and temporal anchors.
- EventWindow connects to Place with `OCCURRED_IN`.
- EventWindow connects to Era/Period with `OCCURS_DURING`.
- Bot (Ingest Agent) ensures that place resolution and temporal overlap rules hold.
- Policy System scans for missing or anomalous geographic or temporal links.

---

## 📘 5. Review

- Person (Curator) reviews nodes and relationships for accuracy and coherence.
- Bot (Ingest Agent) enforces active-voice only, validates paths, and prevents unintended joins.
- Graph accepts or rejects: accepted edges remain; rejected edges set `r.deprecated = true`.
- Policy System flags exceptions for curator attention.

---

## 📘 6. Version

- Person (Curator) proposes refinements or corrections.
- Graph supersedes relationships instead of overwriting.
- Graph marks prior edge `r.deprecated = true` and creates a new edge with updated evidence.
- Policy System generates a delta report to highlight changes.

---

## 📘 7. Publish

- Institution (Editorial Team) approves a batch of reviewed nodes and relationships.
- Graph snapshots the state and tags a release (`:Release {hash:...}`).
- Policy System publishes a health summary (citation density, framework balance, coverage).

---

## ✅ End Result (One-line)

Person proposes → EventWindow/Idea/Place/Institution anchors → Framework interprets → Graph preserves provenance → Institution publishes.

Every class node acts as an active subject, ensuring relationships and workflow remain in active present tense with no passive voice.

---

## Alignment with International Conventions (Short)

- Provenance & Versioning: modeled to match W3C PROV-O (Entities, Activities, Agents) and CIDOC CRM event-based versioning.
- Evidence & Citation: normalized to Dublin Core fields and Chicago 17 style; `FRAMED_BY` edges carry structured citation fields.
- Frameworks: first-class nodes (explicit, auditable, reusable), matching historiographic practice.
- Places & Chronology: `OCCURRED_IN` + `OCCURS_DURING`; BCE encoded as negative integers for numeric sortability.
- Relationships: active-voice, directed, semantic verbs only (no passive forms allowed).
- Review & Publication: peer review, versioning, and snapshot releases (hash-tagging) to mirror scholarly publishing.

---

## Workflow Explanation (Curator → Ingest Bot → Graph → QA/Policy)

This section restates the pipeline in operational terms:

1. Propose
- Curator submits an item via form or API.
- Ingest Bot validates schema and checks duplicates.
- Graph writes with MERGE and provenance.
- QA/Policy queues automated checks.

2. Cite
- Curator uploads source metadata.
- Ingest Bot normalizes citation.
- Graph adds `FRAMED_BY` edges with evidence fields.
- QA/Policy validates citation integrity.

3. Frame
- Curator selects frameworks.
- Ingest Bot resolves framework nodes.
- Graph links event windows to frameworks.
- QA/Policy monitors coverage.

4. Place
- Curator sets places and time bins.
- Ingest Bot resolves place and era overlaps.
- Graph writes `OCCURRED_IN` and `OCCURS_DURING`.
- QA/Policy checks for missing anchors.

5. Review
- Curator performs human review.
- Ingest Bot runs policy checks.
- Graph version-controls accepts/rejects writes.
- QA/Policy logs exceptions.

6. Version
- Curator proposes updates.
- Ingest Bot writes new relationships; Graph marks old ones deprecated.
- QA/Policy generates deltas.

7. Publish
- Curator/Editor approves a release.
- Ingest Bot snapshots state; Graph tags release.
- QA/Policy produces health summary.

---

## Next steps

- Add example Cypher audit queries to [docs/guidelines/audit_queries.md](./audit_queries.md).
- Produce a swimlane diagram (SVG) for the lifecycle and add it to this folder.
- Optionally recast relationship grammar (edge verbs) into the same active-voice, class-subject format.

---

If you want, I will also convert the relationship names into an active-voice, class-subject list and add audit query examples next.
