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

## Corpus Node Abbreviation
- C = Corpus (canonical grouping of texts, traditions, or cultural artifacts)

See: [Contributor Guide: Corpus](./contributor_guide_corpus.md) | [Node Interaction Matrix](./node_interaction_matrix.md)

## Corpus Node Verbs (Canonical)
- CONTAINS, INCLUDES, ORGANIZES, CANONIZES (C → T)
- DEFINES, EXEMPLIFIES, INFLUENCES (C → D)
- INFLUENCES (C → M)
- FRAMES (C → F)
- DOCUMENTS, BELONGS_TO (C ↔ V)
- SUBSUMES, SPLITS_INTO, IS_PART_OF (C ↔ C)

Example triples:
- (BIBLICAL_CORPUS) CONTAINS (Hebrew_Bible)
- (BIBLICAL_CORPUS) EXEMPLIFIES (Monotheism)
- (BIBLICAL_CORPUS) DOCUMENTS (Dead_Sea_Scrolls)
- (BIBLICAL_CORPUS) SUBSUMES (JUDAIC_RABBINIC_CORPUS)

## 3. Core Canon (High-Frequency)
| Verb | Semantics | Allowed (Subject→Object) | Notes / Disallow | Evidence Tier Guidance |
|------|-----------|--------------------------|------------------|------------------------|
| FRAMES | Lenses an interpretation (to Framework) | (Any content) → F | Only with explicit interpretive layer | B or D |
| OCCURS_IN | Event/Process location anchor | E → L | Single primary place per edge; replicate for multiplex locales | A |
| CAUSES | Direct causal contribution | E/T/D/M → E/D | Not for weak correlation | A or B |
| TRANSFORMS | Deep structural change | E/T/M → D/I/T | Provide before/after note | A or B |
| IS_PART_OF | Membership / part–whole relation | C/E/T → C/E/T | Use for structural/component membership only; not for causality or loose association | A |
| STANDARDIZES | Imposes uniform practice/text | I/P → D/T | Distinct from CANONIZES (status vs. uniformity) | A + B |
| CANONIZES | Confers canonical status | I/P → T/D | Only when formal recognition | A primary record |
| PRESERVES | Actively conserves text/practice | I/P → T/D | Use when continuity risk documented | A or B |
| DEFINES | Establishes doctrinal/textual definition | I/P/T → D/T | Use for councils, doctrinal formulae | A or B |
| SCHISMS_FROM | Formal separation / split | M/I → M/I | Must have structural or doctrinal rupture | A + B |
| RECONCILES_WITH | Restores communion/unity | M/I/P → M/I/P | Reciprocal edge optional; persons may reconcile post-conflict | A + B |
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
| MEETS_WITH | P ↔ P | In-person encounter/meeting | Neutral; use COLLABORATES_WITH if joint work is the point |
| BLESSES | P → P | Confers religious/ritual blessing on a person | Distinct from ORDAINS (office) and PARDONS (legal) |
| CURSES | P → P | Pronounces malediction against a person | Provide context/evidence; avoid sensational use |
| SERVES_IN | P → I | Member/official serving within an institution | Include role/tenure; distinct from LEADS |
| PETITIONS | P → I | Files a formal request to an institution | Include docket/ref if available |
| RESIGNS_FROM | P → I | Relinquishes office/membership in an institution | Include date/authority if formalized |
| AWARDS | I → P | Grants prize/decoration/honor | Include award name/date |
| HONORS | I → P | Confers non-monetary recognition/tribute | Use AWARDS when formal prize; HONORS for ceremonial |
| CENSURES | I → P | Issues formal reprimand without removal | Distinct from DISMISSES/DEPOSES |
| FINES | I → P | Imposes monetary penalty | Include instrument/reference |
| SUMMONS | I → P | Orders a person to appear (hearing/trial/council) | Provide writ/act citation |
| LICENSES | I → P | Grants license/permission to act | Include scope/term |
| ACCREDITS | I → P | Certifies competence/authority | Include accrediting body/scope |
| ANNOTATES | P → T | Adds notes/marginalia to a text | Distinct from COMMENTATES_ON (full commentary) |
| GLOSSES | P → T | Provides brief lexical/explanatory notes | Use ANNOTATES for broader notes |
| REDACTS | P/I → T | Substantively edits/structures a text | Use EDITS for edition work; REDACTS for content shaping |
| ILLUSTRATES | P → T | Creates visual artwork for a text/artifact | Provide medium/context |
| CENSORS | I → T | Removes/modifies content under authority | Distinct from BANS (prohibits entirely) |
| BANS | I → T/D/M/P | Prohibits circulation/possession | Provide decree/edict reference |
| APPROVES | I → T | Grants imprimatur/nihil obstat/official approval | Include approver/body |
| CITES | T → T | References another text without direct quotation | Distinct from QUOTES |
| ADAPTS | T → T | Transforms text for new context/genre | Provide target genre/context |
| PARAPHRASES | T → T | Restates content in different wording | Use sparingly; provide scope |
| ABROGATES | I → D | Formally repeals doctrine/norm | Provide abrogating instrument |
| RECRUITS | M → P | Enlists a person into a movement | Include role/status if relevant |
| EXPELS | M → P | Removes a person from a movement | Provide cause/context |
| INCITES | M → E | Agitates to spark a specific event | Use CAUSES for direct causation if warranted |
| WITNESSES | P → E | Person is present and observes/records an event | Provide evidence (memoir, deposition, report) |
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
| ADOPTS_AS_CHILD | P → P | Legal adoption creating parent–child tie | Distinct from PARENT_OF (biological); include legal context |
| ENDORSES | P → P | Publicly supports a person (office/teaching) | Person-targeted; for ideas use ADVOCATES/PROMOTES; include context |
| HEALS | P → P | Provides curative/medical/spiritual healing | Require explicit evidence; include method/context |
| TEACHES | P → P | Teacher → student relation | Optionally pair with STUDIES_UNDER |
| STUDIES_UNDER | P → P | Student → teacher relation | Optionally pair with TEACHES |
| ASSASSINATES | P → P | Targeted killing of a public/political/religious figure | Provide victim role/title; political/religious motive usually present |
| MURDERS | P → P | Unlawful killing with intent | Requires evidence of unlawfulness/intent; avoid for wartime combat |
| SUCCEEDS | P → P; I → I | Succeeds to office/role/lineage | Provide office/context in properties |
| MARRIES | P ↔ P | Marital tie (reciprocal) | Record one reciprocal edge or two directed edges consistently |
| COLLABORATES_WITH | P ↔ P | Works jointly on a specific text/event/project | Reciprocal; include target ref (text/event id) |
| CORRESPONDS_WITH | P ↔ P | Documented exchange of letters | Reciprocal; cite correspondence |
| DIVORCES | P ↔ P | Formal dissolution of marriage | Reciprocal; include date/jurisdiction |
| DEBATES | P ↔ P; P → D | Structured disputation | Use reciprocal edges sparingly |
| PROMULGATES | P/I → D/T | Formally publishes/enacts law/edict | Prefer CANONIZES for status decisions |
| PARTICIPATES_IN | P/I → E | General involvement in an event (non-organizer) | Avoid for organizers; use ORGANIZES/LEADS |
| LEADS | P/I → E/M | Directs or commands an event/movement | Distinct from ORGANIZES (planning) |
| APPOINTS | P/I → P | Selects a person for an office/role | Include office/term; distinct from INVESTS (installation) |
| INVESTS | P/I → P | Formally confers office/authority | Include ceremony/office; distinct from APPOINTS (selection) |
| DISMISSES | P/I → P | Removes from office via normal procedure | Include authority/reason; distinct from DEPOSES (coercive) |
| DEPOSES | P/I → P | Forcibly removes from high office | Extraordinary/coercive removal; include method/context |
| ORDAINS | P/I → P | Confers religious/clerical status | Include rite/order/see; use for religious office |
| EXCOMMUNICATES | P/I → P | Expels from religious communion | Include canon/act reference |
| PARDONS | P/I → P | Grants legal clemency | Include issuing authority/instrument |
| IMPRISONS | P/I → P | Places a person in custody | Include location/term |
| SPONSORS | P/I → P | Provides material/financial support to a person | Distinct from COMMISSIONS (I→T/E) |
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
| CONVICTS | I → P | Officially finds a person guilty | Include court/charge; distinct from SENTENCES (punishment) |
| ACQUITS | I → P | Officially finds a person not guilty | Include court/case reference |
| SENTENCES | I → P | Imposes punishment upon conviction | Include term/type; separate edges for IMPRISONS/FINES/EXECUTES |
| ELECTS | I → P | Selects via voting process | Distinct from APPOINTS (top-down selection) |
| EXILES | I → P | Expels a person from a territory | Include jurisdiction/term; distinct from IMPRISONS |
| INTERDICTS | I → L/I | Suspends rites/services in a realm or institution | Provide instrument/scope; place or institution target |
| SIGNS | P/I → T | Signs a treaty/edict/instrument | Provide instrument id/date; distinct from PUBLISHES |
| RATIFIES | P/I → T | Ratifies a previously signed instrument | Provide ratifying body/date; distinct from CANONIZES |
| MEDIATES | P/I → P/I | Facilitates settlement between parties | Use when acting as third-party; not a party to dispute |
| ARBITRATES | P/I → P/I | Issues binding decision between parties | Provide forum/award; distinct from MEDIATES |
| OBSERVES | P/I → D | Keeps an observance/commanded practice | Use for compliance/keeping; prefer PARTICIPATES_IN for general attendance; use LEADS for leadership |
| PRESCRIBES | I/D/T → D | Normatively mandates a ritual/observance | Cite source (council canons, legal code, liturgical rubrics) |
| DESCRIBES | T → D | Descriptive account of a ritual/observance | Not prescriptive; use PRESCRIBES when normative |
| DEDICATES | P/I → T/L/I | Formally dedicates object/place/institution | Canonical term for dedication; if sacral, record rite/instrument in properties (e.g., consecration_rite) |
| ANOINTS | P/I → P/T | Performs anointing on a person/object | Include oil/rite context; distinct from ORDAINS (office) |
| PURIFIES | P/I → P/T/L | Performs ritual purification | Specify rite/means; do not use for doctrinal purification |
| PILGRIMAGES_TO | P → L | Undertakes pilgrimage to a sacred place | Include date/route if available; distinct from DIFFUSES |
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
 - PERFORMS → PARTICIPATES_IN (use PARTICIPATES_IN for event instances) or OBSERVES (for ongoing practice)
 - OFFICIATES → PRESIDES_OVER or LEADS (use PRESIDES_OVER for procedural chairing; LEADS for directing)
 - CELEBRATES → PARTICIPATES_IN (event instance) or OBSERVES (feast as practice)
 - CONSECRATES → DEDICATES (use DEDICATES; include note if sacral consecration)

## 5. Deprecation & Synonym Policy
- If two verbs overlap >70% in intended use, mark one DEPRECATED in this file; reject new edges using it.
- Introduce new verb only via proposal record (add stub row + rationale + 1 example triple + evidence plan).

## 6. Evidence Annotation Rules

This project supports two complementary citation patterns:

- Relationship-level citation attributes (the source-of-truth in cluster relationship JSON): keep citations attached to the relationship object via fields like `evidence_slug`, `page_refs`, `citation_style`, and/or `evidence_url`.
- Evidence nodes + `DOCUMENTS` (the reusable graph view): create a reusable `(:Evidence {slug})` node and materialize `(Evidence)-[:DOCUMENTS]->(content)` during ingest/linking.

Use relationship-level attributes when:

- The citation is edge-specific (most citations are): the relationship object is where `page_refs` and any edge-scoped citation detail belongs.
- You are still triaging/collecting sources and don’t have a stable Evidence record yet.
- The source is a one-off URL or an ephemeral web page and you don’t expect to reuse it.
- You are citing something that isn’t worth curating as a reusable bibliographic record (e.g., a single quick reference).

Create an Evidence node (and use `evidence_slug`) when:

- The same source will be cited by multiple relationships and you want one canonical bibliographic record.
- The source is a stable publication/record (book, article, archival item) where reuse and discoverability matter.
- You want graph queries like “show me everything documented by this source” without depending on relationship JSON parsing.

When NOT to create an Evidence node (use relationship attributes / inline-only instead):

- The “citation” is actually a curator inference with no external source yet.
- The only available reference is unstable (temporary link, private note) and you don’t want to immortalize it as a record.
- The content is too granular/edge-specific to benefit from a reusable Evidence record (e.g., one relationship with one quick pointer).

Promotion heuristic:

- Inline property `evidence: "<Tier>: <short-ref>"` for single-use citations.
- Promote to an Evidence node when the same short-ref appears on ≥2 distinct edges across periods or node types.
- Optional property `evidence_detail` for page/folio; keep concise (e.g., "p. 47b–48a").

### DOCUMENTS (Evidence canonical verb)

- Definition: `DOCUMENTS` is the canonical Evidence→content verb. Use when an Evidence node (book, article, report, archival item) provides documentary support for a person, institution, text, doctrine, movement, or event.
- Semantics: A `:DOCUMENTS` edge asserts that the Evidence node contains, records, or attests to the factual or interpretive material relevant to the target node. Prefer active voice: the Evidence documents the content.
- Properties recommended on `DOCUMENTS` edges:
	- `page_refs` (string): precise page or folio range when applicable.
	- `cited_rel_id` or `relationship_id` (int): references the relationship object this citation supports, if relevant.
	- `note` (string): brief curator note or fragment description (optional).
- When to use:
	- Use `DOCUMENTS` when the source is reusable, bibliographic, or will be cited more than once.
	- Keep relationship-level `page_refs` (and other edge-scoped citation details) on the relationship object even when you also create an Evidence node; `DOCUMENTS` is a derived view, not the citation source-of-truth.
	- Prefer `evidence_url` (inline-only) when the reference is one-off, unstable, or not yet ready to be promoted into `data/Evidence/*.json`.

- When not to use:
	- Don’t use `DOCUMENTS` as a substitute for modeling the underlying domain relationship (e.g., `DECLARES`, `PROMULGATES`, `INFLUENCES`). `DOCUMENTS` is only for Evidence→content support.
	- Don’t create an Evidence node for every single edge by default; promote sources selectively when reuse/discoverability justify it.
- Example triples:

	- (evidence_Duffy_2009_Fires_of_Faith)-[:DOCUMENTS {page_refs:'23-44', cited_rel_id:47}]->(Lord_Protectorate)
	- (evidence_Duffy_2009_Fires_of_Faith)-[:DOCUMENTS {page_refs:'56-94', cited_rel_id:53}]->(Western_Rebellion_1549)

Notes:
- `DOCUMENTS` is the canonical Evidence→content verb; traverse “content → evidence” using incoming `DOCUMENTS` edges (i.e., `MATCH (e:Evidence)-[:DOCUMENTS]->(n)`), rather than maintaining a second inverse verb.
- Adding `isbn`, `doi`, or other identifier properties to `:Evidence` nodes is encouraged to improve discoverability and external linking.

Data modeling recommendation (source-of-truth):
- Keep citations centralized on the relationship objects in the cluster relationship JSON (e.g., `evidence_slug`, `page_refs`, `citation_style`).
- Materialize graph-level Evidence→content edges (`DOCUMENTS`) during ingest/linking as a derived view.
- Avoid maintaining a separate curated JSON file that lists all `DOCUMENTS` edges, because it duplicates the same facts and will drift from the relationship file over time.

Relationship JSON evidence fields (operational semantics):
- `evidence_slug`: preferred; points to a reusable Evidence record (see `data/Evidence/*.json`) and to a Neo4j `(:Evidence {slug})` node.
- `evidence_url`: inline-only citation URL (use when the citation is one-off or you do not yet have an Evidence node).
- `citation_style`: e.g. "Chicago 17".
- `page_refs`: page/folio range for the claim.
- `inline_evidence`: derived boolean; `true` when `evidence_url` is non-null.
- `evidence_node_present`: derived boolean; `true` when an `:Evidence` node with `evidence_slug` exists in Neo4j at the last status check.

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