---
title: Relations Vocabulary (Class 9 Clusters)
status: DRAFT
version: 0.2
summary: Canonical active-voice edge verbs, semantics, allowed node-type pairs, and governance rules for Hebrew cluster (pattern aligned to prior methodology).
---

# Relations Vocabulary (Single Source of Truth)

Purpose: Provide a controlled, auditable verb set for active-voice relationships. Prevent synonym drift, ensure consistent analytics, and separate core semantic intents from specialized verbs. This file is the single source of truth for the project’s relationship verbs (Core + Supplementary).

Compliance
- You MUST select verbs from this file; PRs with non-canonical verbs will be requested to normalize.
- Changes to this file require an approved issue and MUST be recorded in `../governance/audit_log.md`.

Applies to: Hebrew cluster (class 9) and derivative sub-clusters using the same governance.

Curator workflow (verbs)
- Contributors must choose verbs from the Core or Supplementary lists in this file.
- To propose a new verb or change semantics/allowed pairs, open an issue titled "Verb Proposal: <VERB>" and include: (1) definition, (2) allowed pairs, (3) 1–2 example triples, (4) minimal evidence plan. The curator will review, decide, and update this file.
- Curators maintain this file as the canonical registry and will run normalization/audits to prevent synonym drift.

See also: Interaction Matrix for allowed node-type pairs and example triples — [node_interaction_matrix.md](./node_interaction_matrix.md) • Jump to: [Quick Pair Matrix](./node_interaction_matrix.md#quick-pair-matrix-overview). Governance: [Policy](../governance/GOVERNANCE.md) • [Audit Log](../governance/audit_log.md)

## 1. Format Standard
- Edge labels: UPPER_SNAKE_CASE (preferred) or UPPER single word. (Temporary mixed usage from legacy examples acceptable until normalization pass.)
- Verbs express a single semantic action; no tense inflection.
- Property `verb` (duplicate of relationship type if needed for querying) optional; if present must equal label.

## 2. Node Type Abbreviations
P = Person | I = Institution | T = Text/Artifact | D = Doctrine/Idea | M = Movement | E = Event | L = Place | F = Framework lens | V = Evidence node.

## 3. Core Canon (High-Frequency)
| Verb | Semantics | Allowed (Subject→Object) | Notes / Disallow | Evidence Tier Guidance |
|------|-----------|--------------------------|------------------|------------------------|
| FRAMES | Lenses an interpretation (to Framework) | (Any content) → F | Only with explicit interpretive layer | B or D |
| OCCURS_IN | Event/Process location anchor | E → L | Single primary place per edge; replicate for multiplex locales | A |
| CAUSES | Direct causal contribution | E/T/D/M → E/D | Not for weak correlation | A or B |
| TRANSFORMS | Deep structural change | E/T/M → D/I/T | Provide before/after note | A or B |
| STANDARDIZES | Imposes uniform practice/text | I/P → D/T | Distinct from CANONIZES (status vs. uniformity) | A + B |
| CANONIZES | Confers canonical status | I/P → T/D | Only when formal recognition | A primary record |
| PRESERVES | Actively conserves text/practice | I/P → T/D | Use when continuity risk documented | A or B |
| DEFINES | Establishes doctrinal/textual definition | I/P/T → D/T | Use for councils, doctrinal formulae | A or B |
| SCHISMS_FROM | Formal separation / split | M/I → M/I | Must have structural or doctrinal rupture | A + B |
| RECONCILES_WITH | Restores communion/unity | M/I → M/I | Reciprocal edge optional | A + B |
| DIFFUSES | Spreads across geography/traditions | M/P/I → L/M/D/T | Must show transmission vector | A + B (or D for modern stats) |
| COMMENTATES_ON | Writes a formal commentary on | P → T/D | More specific than INTERPRETS | A or B |
| DECLARES | Announces formal status/event | P/I → E/D | Public proclamation | A |
| ORGANIZES | Coordinates congress/campaign/event | P/I → E/M | Event node must exist | A or B |
| ESTABLISHES | Founds institution/practice | P/I → I/D | Not for minor reforms | A or B |
| TRANSLATES | Renders text language/script | P/I → T | Not for paraphrase; requires linguistic shift | A or B |
| AUTHORS | Creates an original text/work | P/I → T | Alias: WRITES | A or B |
| PUBLISHES | Issues a work publicly | P/I → T | First issuance; editions use EDITS | A or B |
| EDITS | Produces an edited/redacted form | P/I → T | Include edition descriptor | A or B |
| ADOPTS | Takes up doctrine/practice | P/I/M → D/T | Distinct from STANDARDIZES (scope) | A or B |
| REJECTS | Formally repudiates | P/I/M → D/T | Needs explicit rejection evidence | A or B |
| INFLUENCES | Non-mechanical intellectual impact | P/I/T/D/M → P/I/T/D/M | Prefer a more specific verb if possible | B |
| INTERPRETS | Provides exegesis/theological reading | P/T → T/D | Use for commentary/exegesis broadly | A (commentary ms) or B |
| ENABLES | Necessary precondition without direct causation | T/I/P/E → T/D/M/E | Distinguish from CAUSES (indirect) | A or B |
| TRANSMITS | Conveys textual/ritual content | T/P/I → T/D/M | Use for copying/translation chains | A or B |

## 4. Supplementary Verbs (Contextual / Specialized)
| Verb | Allowed (Subject→Object) | Use Case / Semantics | Constraint / Notes |
|------|---------------------------|----------------------|--------------------|
| USES | E/P/I → T | Uses artifact/text in activity | Distinct from DEPLOYS |
| IS_PART_OF | E/T → E/T | Membership/composition relation | Use for part–whole only (not causality) |
| PRECEDES | E/T → E/T | Temporal ordering | Use with chronological evidence |
| PARTNERS_WITH | I ↔ I | Institutional partnership | Reciprocal optional |
| COMPETES_WITH | I ↔ I/M | Institutional competition | Reciprocal optional |
| PRESIDES_OVER | I → E/P | Chairs or formally oversees | Use for councils, courts |
| REGULATES | I → I/M/P/T | Regulatory oversight | Provide policy/regulatory reference |
| ORDERS | I → P/E | Issues binding instruction | Distinct from DECLARES |
| PROHIBITS | I → T/D/M/P | Institutional prohibition | Provide decree/edict reference |
| COMMISSIONS | I → T/E | Institution commissions text/event | Provide commission record if possible |
| DEPLOYS | I/M/P → T/E | Operational/strategic use | For organized use (e.g., corps, offices) |
| SANCTIONS | I/P → E/D/T | Grants formal approval | Provide edict/act reference |
| DISTRIBUTES | I/P → T | Material/text dissemination | Supply scope (region) in property |
| IS_CENTER_OF | L → M/D | Place as recognized center | Use sparingly, provide source |
| HOSTS | L/I → E/P | Place/Institution hosts people/events | Avoid generic Place → X unless justified |
| ARISES_FROM | M → E | Movement emergence from event | Canonical for Movement genesis |
| EMERGES_FROM | M/T → E/D | Originates from prior event/idea | Prefer ARISES_FROM for Movement → Event |
| CRITIQUES | P → D/T | Critical evaluation of doctrine/text | Specify focus in note |
| PROPHESIES_DURING | P → E | Prophetic activity within event | Recognized prophetic figures only |
| SURVIVES | P → E | Endures/continues through an event | Use for survival through cataclysmic events |
| ADVOCATES | P → M/D | Public support of movement/idea | Distinct from ESTABLISHES |
| PARENT_OF | P → P | Genealogical parent → child | Directional; inverse can be CHILD_OF (if added later) |
| TEACHES | P → P | Teacher → student relation | Optionally pair with STUDIES_UNDER |
| STUDIES_UNDER | P → P | Student → teacher relation | Optionally pair with TEACHES |
| ASSASSINATES | P → P | Targeted killing of a public/political/religious figure | Provide victim role/title; political/religious motive usually present |
| MURDERS | P → P | Unlawful killing with intent | Requires evidence of unlawfulness/intent; avoid for wartime combat |
| SUCCEEDS | P → P; I → I | Succeeds to office/role/lineage | Provide office/context in properties |
| MARRIES | P ↔ P | Marital tie (reciprocal) | Record one reciprocal edge or two directed edges consistently |
| DEBATES | P ↔ P; P → D | Structured disputation | Use reciprocal edges sparingly |
| PROMULGATES | P/I → D/T | Formally publishes/enacts law/edict | Prefer CANONIZES for status decisions |
| PARTICIPATES_IN | P/I → E | General involvement in an event (non-organizer) | Avoid for organizers; use ORGANIZES/LEADS |
| LEADS | P/I → E/M | Directs or commands an event/movement | Distinct from ORGANIZES (planning) |
| EXECUTES | P/I → P | Carries out a formal capital punishment | Prefer I → P when by an institution; include legal authority in properties |
| COPIES | P/I → T | Scribal reproduction of a text | Provide source reference in properties |
| COMPILES | P/I → T | Anthologizes/assembles a text from sources | Provide compilation scope |
| INVENTS | P/I → T | Invents an artifact/technique | Provide invention evidence |
| DESIGNS | P/I → T | Designs an artifact/technique | Distinct from INVENTS |
| PRODUCES | P/I → T/E | Creates an artifact/text or produces an event | Prefer ORGANIZES for event planning |
| PROMOTES | P/I/M → D/T | Accelerates adoption without founding | Provide metric/note when possible |
| INTRODUCES | P/I/M → T/D/E | Introduces idea/tech/event to context | Provide vector/context |
| QUOTES | T → T | Text cites another text | Provide citation location |
| REFUTES | T → T/D | Text argues against | Provide citation location |
| SYMBOLIZES | T/E → D/M | Stands for/represents | Use when symbolic reading is explicit |
| EXEMPLIFIES | T/E/P → D | Concrete instance embodying an idea/doctrine | Provide the aspect exemplified |
| DATES | V → E/T | Evidence dates event/text | Evidence-only |
| REPORTS | V → E/T/D | Summarizes/aggregates | Evidence-only |
| DOCUMENTS | V → P/I/T/D/M/E | Evidence documents content | Evidence-only |
| VALIDATES | V → P/I/T/D/M/E | Confirms measurement/claim | Evidence-only |
| ATTRIBUTES | V → P/T/E | Evidence attributes authorship/date | Evidence-only; see evidence verbs |
| ATTESTS_TO | V → P/T/E/D | Evidence attests to content | Evidence-only |
| CORROBORATES | V → P/T/E/D | Evidence corroborates content | Evidence-only |
| PROVIDES | V → T/D/M/E | Supplies resource/context | Evidence-only |

// Person-to-Person Killing (Specialized — Sensitive)
| KILLS | P → P | Causes the death of another person (generic) | Provide context (e.g., battle, self-defense); prefer ASSASSINATES/EXECUTES/MURDERS when applicable |
| MURDERS | P → P | Unlawful killing with intent | Requires evidence of unlawfulness/intent; avoid for wartime combat |
| ASSASSINATES | P → P | Targeted killing of a public/political/religious figure | Provide victim role/title; political/religious motive usually present |
| EXECUTES | P/I → P | Carries out a formal capital punishment | Prefer I → P when by an institution; include legal authority in properties |

Aliases & Deprecations
- FOUNDS → ESTABLISHES (use ESTABLISHES)
- WRITES → AUTHORS (use AUTHORS)
- COMMENTS_ON → COMMENTATES_ON (use COMMENTATES_ON)
- SPREADS_VIA → DIFFUSES (use DIFFUSES)
- DELIVERS → PROMULGATES or CANONIZES (prefer PROMULGATES for law publication; CANONIZES for status)

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
`MATCH ()-[r]->() WHERE NOT type(r) IN [
	"CAUSES","ENABLES","TRANSFORMS","DIFFUSES","TRANSMITS","TRANSLATES",
	"INTERPRETS","COMMENTATES_ON","AUTHORS","PUBLISHES","EDITS","CANONIZES",
	"STANDARDIZES","DEFINES","ESTABLISHES","ORGANIZES","PRESERVES","ADOPTS",
	"REJECTS","INFLUENCES","FRAMES","OCCURS_IN","SCHISMS_FROM","RECONCILES_WITH",
	"DECLARES"
] RETURN DISTINCT type(r);`

Promotion candidates:
`MATCH ()-[r]->() WITH r.evidence AS ev, count(*) AS c WHERE c > 1 AND ev CONTAINS ':' RETURN ev, c ORDER BY c DESC;`

Framework misuse:
`MATCH ()-[r]->(f:Framework) WHERE type(r) <> 'FRAMED_BY' RETURN r LIMIT 25;`

## 8. Change Log
- 0.2 Expanded core canon (ENABLES, TRANSFORMS, AUTHORS, PUBLISHES, EDITS, DEFINES, ORGANIZES); expanded supplementary set (institutional, textual, temporal, evidence verbs); added aliases/deprecations; updated whitelist.
- 0.1 Initial draft (core + supplementary verbs; governance + QA snippets).

## 9. TODO
- Normalize legacy mixed-case verbs to UPPER_SNAKE_CASE.
- Decide on PROMULGATES vs DELIVERS for covenant edges.
- Add per-verb disambiguation examples in annex (next revision).

---
End of file.