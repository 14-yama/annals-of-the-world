---
title: Historian Framework & Provenance Guide
status: DRAFT
summary: Guidance for treating Framework nodes and FRAMED_BY edges as first-class provenance lenses; evidence promotion; curator workflows; QA checks.
---

# Historian Framework & Provenance Guide

Purpose
- Provide curators and contributors with a compact, authoritative guide to how interpretive frameworks (Framework nodes) and per-edge provenance (FRAMED_BY / inline evidence) work in the project.

Audience
- Curators, data engineers seeding EventWindows, peer reviewers, and maintainers.

Why this matters
- Historical interpretation needs reproducible provenance. The historian framework makes interpretive lenses explicit and traceable. It reduces ambiguity when edges express causal or interpretive claims.

Key Concepts
- Framework (node): an interpretive lens (e.g., CAUSE_AND_EFFECT, CULTURAL_DIFFUSION) that explains why an edge exists or how to read an EventWindow.
- FRAMED_BY (edge): connects a content edge or EventWindow to a Framework node, with a citation that explains the interpretive choice.
- Evidence node (:Evidence): reusable bibliographic or institutional sources promoted from inline citations when reused.
- Inline evidence: single-use edge-specific citation kept as `evidence` property on the relationship.

Design Goals
1. Traceability: every interpretive claim should be traceable to one or more cites.
2. Reusability: promote frequently used sources to :Evidence nodes.
3. Minimal friction: support quick inline citations during curation; provide promotion tools for recurring citations.
4. Consistency: use [relations_vocabulary.md](./relations_vocabulary.md) for verbs and [hebrew_cluster.md](./hebrew_cluster.md) conventions for slugs/classification.

Recommended Node & Edge Patterns
- Content node: (:Person|:Event|:Text|:Movement|:Institution {slug, name, status:'PROPOSED', class:9, division:940})
- Evidence node: (:Evidence {slug, title, tier:'A'|'B'|'D', ref:'standard ref string', uri: optional})
- Edge with inline evidence:
  - (a)-[r:CAUSES {status:'PROPOSED', evidence:'A: Wujing Zongyao, fol. x'}]->(b)
- Edge plus framework:
  - (a)-[r:CAUSES {status:'PROPOSED', evidence:'B: Parker ch.3'}]->(b)
  - (r)-[:FRAMED_BY {lens:'CAUSE_AND_EFFECT', citation:'B: Parker ch.3'}]->(:Framework {slug:'CAUSE_AND_EFFECT'})

Promotion rules (practical)
1. If the same inline evidence string appears on ≥2 distinct edges, create an :Evidence node with a canonical slug and replace inline strings with reference to the Evidence node via a FRAMED_BY or ATTESTS edge.
2. For major reused works (Needham, Andrade, SIPRI), create :Evidence nodes proactively and reference them by slug in edges.
3. Keep inline evidence for archival shelfmarks, folio/page references, and one-off reports.

Curation workflow (quick)
1. Create content nodes (status: PROPOSED) with slug and minimal metadata.
2. Add edges using canonical verbs from [relations_vocabulary.md](./relations_vocabulary.md) and attach inline evidence if available.
3. When edge evidence repeats, promote to :Evidence and update edges to reference the promoted node.
4. Attach FRAMED_BY edges when an interpretive lens is applied (mandatory for causal/interpretive claims in published curated datasets).
5. Run QA queries (see below) and fix orphan nodes or inconsistent verbs.

QA Queries (run against Neo4j)
- Orphan nodes (no edges):
  MATCH (n) WHERE NOT (n)--() RETURN n LIMIT 100
- Inline evidence reuse candidates:
  MATCH ()-[r]->() WHERE exists(r.evidence) WITH r.evidence AS ev, count(*) AS c WHERE c > 1 RETURN ev, c ORDER BY c DESC
- Improper framework links:
  MATCH ()-[r]->(f:Framework) WHERE type(r) <> 'FRAMED_BY' RETURN r LIMIT 50
- Non-canonical verbs (adjust list):
  MATCH ()-[r]->() WHERE NOT type(r) IN ["CAUSES","DIFFUSES","TRANSMITS","CANONIZES","STANDARDIZES","INTERPRETS","SYSTEMATIZES","TRANSLATES","ADOPTS","REJECTS","INFLUENCES","FRAMES","OCCURS_IN","ESTABLISHES","PRESERVES","COMMENTATES_ON","SCHISMS_FROM","RECONCILES_WITH","DECLARES"] RETURN DISTINCT type(r)

Provenance best practices
- Always capture at least one evidence reference for causal/interpretive claims.
- Prefer primary sources (Tier A) when available, and add Tier B/D as contextual anchors.
- For contentious or ambiguous claims, include multiple FRAMED_BY edges to different frameworks or include multiple evidence refs.

Integration with Curator Registry Matrix
- The Curator Registry Matrix should include: Node slug | Relationship verb | Target slug | Framework slug(s) | Evidence (inline or Evidence slug) | Tier | Notes.
- This matrix becomes the importable CSV for seeding EventWindows and edges.

Onboarding (for new curators)
1. Read [hebrew_cluster.md](./hebrew_cluster.md) and [relations_vocabulary.md](./relations_vocabulary.md).
2. Use the example triples in [hebrew_cluster.md](./hebrew_cluster.md) as templates.
3. During initial edits, mark nodes as PROPOSED; senior curator reviews change status to VERIFIED.
4. For promotions to :Evidence nodes, open a small PR documenting sources and slug choices.

Governance & Change Control
- New Framework nodes: require a short proposal (1-paragraph) and 2 example edges showing use; approved by project curators.
- New verbs: use the proposal template in [docs/guidelines/relations_vocabulary.md](./relations_vocabulary.md) TODO.
- Promotion of inline evidence to :Evidence requires a curator sign-off PR.

Appendix: Example FRAMED_BY patterns
- Single-lens framing:
  (event)-[:CAUSES {status:'PROPOSED', evidence:'B: Doe 2005'}]->(idea)
  (event)-[:FRAMED_BY {lens:'CAUSE_AND_EFFECT', citation:'B: Doe 2005'}]->(:Framework {slug:'CAUSE_AND_EFFECT'})
- Multi-lens framing (competing interpretations):
  (event)-[:CAUSES {status:'PROPOSED', evidence:'A: Chronicle X p.21'}]->(idea)
  (event)-[:FRAMED_BY {lens:'CAUSE_AND_EFFECT', citation:'A: Chronicle X p.21'}]->(:Framework {slug:'CAUSE_AND_EFFECT'})
  (event)-[:FRAMED_BY {lens:'CULTURAL_DIFFUSION', citation:'B: Smith 2010'}]->(:Framework {slug:'CULTURAL_DIFFUSION'})

End of guide (draft). Feedback welcome; I can expand into templates and CSV examples on request.
