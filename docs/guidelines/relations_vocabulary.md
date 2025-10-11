---
title: Relations Vocabulary (Class 9 Clusters)
status: DRAFT
version: 0.1
summary: Canonical active-voice edge verbs, semantics, allowed node-type pairs, and governance rules for Hebrew cluster (pattern aligned to prior methodology).
---

# Relations Vocabulary

Purpose: Provide a controlled, auditable verb set for active-voice relationships. Prevent synonym drift, ensure consistent analytics, and separate core semantic intents from specialized verbs.

Applies to: Hebrew cluster (class 9) and derivative sub-clusters using the same governance.

See also: Interaction Matrix for allowed node-type pairs and example triples — `interaction_matrix.md`.

## 1. Format Standard
- Edge labels: UPPER_SNAKE_CASE (preferred) or UPPER single word. (Temporary mixed usage from legacy examples acceptable until normalization pass.)
- Verbs express a single semantic action; no tense inflection.
- Property `verb` (duplicate of relationship type if needed for querying) optional; if present must equal label.

## 2. Node Type Abbreviations
P = Person | I = Institution | T = Text/Artifact | D = Doctrine/Idea | M = Movement | E = Event | L = Place | F = Framework lens | V = Evidence node.

## 3. Core Canon (High-Frequency)
| Verb | Semantics | Allowed (Subject→Object) | Notes / Disallow | Evidence Tier Guidance |
|------|-----------|--------------------------|------------------|------------------------|
| CAUSES | Direct causal contribution | E/T/D/M → E/D | Not for weak correlation | A or B |
| DIFFUSES | Spreads across geography/traditions | M/P/I → L/M/D/T | Must show transmission vector | A + B (or D for modern stats) |
| TRANSMITS | Conveys textual/ritual content | T/P/I → T/D/M | Use for copying/translation chains | A or B |
| CANONIZES | Confers canonical status | I/P → T/D | Only when formal recognition | A primary record |
| STANDARDIZES | Imposes uniform practice/text | I/P → D/T/Ritual | Distinct from CANONIZES (authority vs status) | A + B |
| INTERPRETS | Provides exegesis/theological reading | P/T → T/D | Use when producing commentary | A (commentary ms) or B |
| SYSTEMATIZES | Produces organized legal/doctrinal corpus | P/I → D/T | Large-scale synthetic work | B |
| TRANSLATES | Renders text language/script | P/I → T | Not for paraphrase; must have linguistic shift | A or B |
| ADOPTS | Takes up doctrine/practice | P/I/M → D/T | Distinct from STANDARDIZES (scope) | A or B |
| REJECTS | Formally repudiates | P/I/M → D/T | Needs explicit rejection evidence | A or B |
| INFLUENCES | Non-mechanical intellectual impact | P/I/T/D/M → P/I/T/D/M | Last-resort; specify stronger verb if possible | B |
| FRAMES | Lenses an interpretation (edge to Framework) | (Any content) → F | Only with explicit interpretive layer | B or D |
| OCCURS_IN | Event/Process location anchor | E → L | Single primary place per edge; replicate for multiplex locales | A |
| ESTABLISHES | Founds institution/practice | P/I → I/D | Not for minor reforms | A or B |
| PRESERVES | Actively conserves text/practice | I/P → T/D | Use when continuity risk documented | A or B |
| COMMENTATES_ON | Writes commentary/exegesis | P → T/D | More specific than INTERPRETS | A or B |
| SCHISMS_FROM | Formal separation / split | M/I → M/I | Must have structural or doctrinal rupture | A + B |
| RECONCILES_WITH | Restores communion/unity | M/I → M/I | Reciprocal edge optional | A + B |
| DECLARES | Announces formal status/event | P/I → E/D | Public proclamation | A |

## 4. Supplementary Verbs (Contextual)
| Verb | Use Case | Example Subject→Object | Constraint |
|------|---------|------------------------|-----------|
| PROPHESIES_DURING | Prophetic activity within event | P → E | Only for recognized prophetic figures |
| DELIVERS (LEGACY) | Provides covenant/law | P → D | Prefer CANONIZES / PROMULGATES later |
| DEBATES | Engages in structured disputation | P ↔ P / P → D | Use reciprocal edges sparingly |
| CRITIQUES | Critical evaluation of doctrine/text | P → D/T | Provide focus (which aspect) in note |
| ADVOCATES | Publicly supports movement/idea | P → M/D | Distinct from ESTABLISHES |
| DISTRIBUTES | Enables material/text dissemination | I/P → T | Supply scope (region) in property |
| ORGANIZES | Coordinates congress/campaign | P/I → E/M | Event node must exist |
| PROMOTES | Accelerates adoption without founding | P/I/M → D/T | Use metrics if available |
| PUBLISHES | Issues written work | P/I → T | Use only for first issuance |
| EDITS | Produces edited/redacted form | P/I → T | Include edition descriptor |
| COMMENTS_ON | (Alias of COMMENTATES_ON) | P → T/D | Prefer COMMENTATES_ON; deprecate alias |
| COLLABORATES_WITH | Joint action toward shared goal | P ↔ P | Provide project scope |
| SURVIVES | Persists through catastrophic event | P/I/T → E | Use sparingly (transformational events) |
| EXEMPLIFIES | Embodies idea/doctrine | E/P/T → D | Not generic; idea must be abstract node |
| TRANSFORMS | Deep structural change | E/T/M → D/I/T | Provide before/after note |
| ENABLES | Provides necessary precondition | T/I/P/E → T/D/M | Distinguish from CAUSES (indirect) |

## 5. Deprecation & Synonym Policy
- If two verbs overlap >70% in intended use, mark one DEPRECATED in this file; reject new edges using it.
- Introduce new verb only via proposal record (add stub row + rationale + 1 example triple + evidence plan).

## 6. Evidence Annotation Rules
- Inline property `evidence: "<Tier>: <short-ref>"` for single-use citations.
- Promote to Evidence node when same short-ref appears on ≥2 distinct edges across periods or node types.
- Optional property `evidence_detail` for page/folio; keep concise (e.g., "p. 47b–48a").

## 7. Validation Cypher Snippets (Reference)
Orphan verb check:
`MATCH ()-[r]->() WHERE r.verb IS NULL RETURN r LIMIT 20;`

Non-whitelisted verb check (adjust list):
`MATCH ()-[r]->() WHERE NOT type(r) IN ["CAUSES","DIFFUSES","TRANSMITS","CANONIZES","STANDARDIZES","INTERPRETS","SYSTEMATIZES","TRANSLATES","ADOPTS","REJECTS","INFLUENCES","FRAMES","OCCURS_IN","ESTABLISHES","PRESERVES","COMMENTATES_ON","SCHISMS_FROM","RECONCILES_WITH","DECLARES"] RETURN DISTINCT type(r);`

Promotion candidates:
`MATCH ()-[r]->() WITH r.evidence AS ev, count(*) AS c WHERE c > 1 AND ev CONTAINS ':' RETURN ev, c ORDER BY c DESC;`

Framework misuse:
`MATCH ()-[r]->(f:Framework) WHERE type(r) <> 'FRAMED_BY' RETURN r LIMIT 25;`

## 8. Change Log
- 0.1 Initial draft (core + supplementary verbs; governance + QA snippets).

## 9. TODO
- Normalize legacy mixed-case verbs to UPPER_SNAKE_CASE.
- Decide on PROMULGATES vs DELIVERS for covenant edges.
- Add per-verb disambiguation examples in annex (next revision).

---
End of file.