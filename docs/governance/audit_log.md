title: Governance Audit Log — Decisions & Changes
status: ACTIVE
version: 0.1
summary: Chronological record of curator/maintainer-approved governance decisions across verbs, interaction rules, cluster normalizations, and documentation.
---

# Governance Audit Log — Project Governance

Purpose: Track approved changes to the verb source of truth, interaction matrix, schemas, cluster normalizations, and documentation (including governance policy and navigation).

## Entries

2025-10-10 — Establish governance policy and wire documentation navigation [governance, docs]
- Added: docs/governance/GOVERNANCE.md — formal policy (authorities, roles, proposal→decision→audit flow).
- Linked governance across docs for discoverability:
  - README.md — Governance: Policy • Audit Log
  - docs/guidelines/README.md — Governance links
  - docs/guidelines/relations_vocabulary.md — Governance links
  - docs/guidelines/node_interaction_matrix.md — Governance links
  - CONTRIBUTING.md — Governance & decision records section
- Rationale: Centralize process and make audit trail visible.
- Breaking changes: None.

2025-10-10 — Align Interaction Matrix with vocabulary and expand examples [matrix]
- Updated: docs/guidelines/node_interaction_matrix.md — Quick Pair Matrix and per-section lists synced with vocabulary; removed SYSTEMATIZES; formalized PRECEDES/IS_PART_OF; trimmed evidence verbs.
- Rationale: Keep allowed pairs and examples in lockstep with the verb canon; remove drift.
- Breaking changes: None; minor example edits.

2025-10-10 — Normalize Hebrew cluster relationships and group-by-type sections [cluster]
- Updated: docs/guidelines/hebrew_cluster.md — Normalized verbs across timeframes to approved canon; grouped relationships by type; fixed ATTESTS_TO typo; introduced PARTICIPATES_IN, LEADS, PROMULGATES where appropriate.
- Rationale: Improve consistency and readability; adhere to single source of truth.
- Breaking changes: None; content semantics preserved, labels normalized.

2025-10-10 — Add targeted supplementary verbs for Hebrew cluster context
- Added verbs (Supplementary): PARTICIPATES_IN (P/I→E), LEADS (P/I→E/M), MARRIES (P↔P), PARENT_OF (P→P), SUCCEEDS (P→P; I→I), TEACHES (P→P), STUDIES_UNDER (P→P), PRODUCES (P/I→T/E), PROMULGATES (P/I→D/T), COPIES (P/I→T), COMPILES (P/I→T), EXEMPLIFIES (T/E/P→D).
- Rationale: Improve modeling of participation, leadership, genealogy, pedagogy, production, legal publication, and textual workflows in Hebrew cluster.
- Files updated:
  - relations_vocabulary.md — Supplementary verbs section expanded; alias note updated for DELIVERS→PROMULGATES.
  - node_interaction_matrix.md — Quick Pair Matrix and detailed sections updated to include new verbs across P/I/T/M rows.
  - hebrew_cluster.md — Timeframe relationship examples normalized to use only approved verbs; added PARTICIPATES_IN and LEADS where appropriate; PROMULGATES for Mosaic law.
- Breaking changes: None (all additions are supplementary; no removals). Minor example edits.
- Curator: jelton_mentore (proposed); applied by automation assistant per curator request.

2025-10-10 — Add SURVIVES supplementary verb and sync matrix/vocabulary [vocabulary, matrix]
- Added verb (Supplementary): SURVIVES (P→E) to relations_vocabulary.md.
- Updated node_interaction_matrix.md to reflect SURVIVES plus PARTICIPATES_IN and LEADS in P→E; expanded P↔P, P→T (COPIES, COMPILES), I→T (PRODUCES), I→D (PROMULGATES, PROHIBITS, SANCTIONS, REGULATES), and M→E (LEADS); removed lingering SYSTEMATIZES example.
- Rationale: Align source of truth with usage in 910 and ensure the matrix matches the accepted verbs.
- Breaking changes: None.

2025-10-11 — Add person-to-person killing verbs (supplementary) [vocabulary, matrix]
- Added verbs (Supplementary): KILLS (P→P), MURDERS (P→P), ASSASSINATES (P→P), EXECUTES (P/I→P) to relations_vocabulary.md with clear semantics and constraints.
- Updated node_interaction_matrix.md Quick Pair and P↔P sections to include these verbs under P interactions.
- Rationale: Model historical killings with appropriate specificity (generic vs. unlawful vs. political/religious vs. formal execution) while maintaining active-voice consistency.
- Constraints: Require contextual properties (e.g., victim role, legal authority, wartime context) and tiered evidence; prefer I→P for EXECUTES when institutional.
- Breaking changes: None.

2025-10-11 — Add non-overlapping person interaction verbs (supplementary) [vocabulary]
- Added verbs (Supplementary, Person interactions):
  - P → P: ADOPTS_AS_CHILD, ENDORSES, HEALS
  - P ↔ P: COLLABORATES_WITH, CORRESPONDS_WITH, DIVORCES
  - P/I → P: APPOINTS, INVESTS, DISMISSES, DEPOSES, ORDAINS, EXCOMMUNICATES, PARDONS, IMPRISONS, SPONSORS, EXECUTES (already present; repositioned within sorted table)
- Rationale: Cover common interpersonal, legal, and religious actions without overlapping existing semantics; maintain active-voice precision and evidenceability.
- Constraints & non-overlap notes:
  - APPOINTS (selection) vs INVESTS (installation);
  - DISMISSES (routine/legal) vs DEPOSES (extraordinary/coercive);
  - ORDAINS/EXCOMMUNICATES (religious) vs institutional APPOINTS/DISMISSES;
  - SPONSORS targets persons; COMMISSIONS targets texts/events;
  - ENDORSES targets persons; ideas use ADVOCATES/PROMOTES.
- Files updated:
  - docs/guidelines/relations_vocabulary.md — Supplementary table rows added; kept sorted by Allowed column.
- Breaking changes: None (additive only).

2025-10-11 — Sort vocabulary tables; clarify constraints; sync matrix and examples [vocabulary, matrix, docs]
- Updated: docs/guidelines/relations_vocabulary.md — Sorted Core and Supplementary tables by Allowed (Subject→Object); clarified semantics and constraints for lethal verbs (KILLS, MURDERS, ASSASSINATES, EXECUTES) and disambiguations (APPOINTS vs INVESTS, DISMISSES vs DEPOSES, ORDAINS/EXCOMMUNICATES vs APPOINTS/DISMISSES); repositioned EXECUTES under P/I→P.
- Updated: docs/guidelines/node_interaction_matrix.md — Synced P↔P and P/I→P rows to include newly accepted person-interaction verbs; expanded examples and Annex quick-pair index.
- Updated: docs/guidelines/hebrew_cluster.md — Ensured example edges use only canonical verbs and normalized section structure (nodes-first, one relationships block per period).
- Rationale: Maintain a single source of truth, improve readability and auditability, and ensure examples reflect the accepted canon.
- Breaking changes: None.

2025-10-18 — Add justice/selection/exile/interdict/treaty/dispute-resolution verbs; sync matrix [vocabulary, matrix]
- Added verbs (Supplementary):
  - Justice/selection/exile (I → P): CONVICTS, ACQUITS, SENTENCES, ELECTS, EXILES
  - Interdict (I → L/I): INTERDICTS
  - Treaty/instrument (P/I → T): SIGNS, RATIFIES
  - Dispute resolution (third-party) (P/I → P/I or ↔ I): MEDIATES, ARBITRATES
- Files updated:
  - docs/guidelines/relations_vocabulary.md — Added rows with semantics, allowed pairs, and constraints.
  - docs/guidelines/node_interaction_matrix.md — Synced Quick Pair Matrix, detailed sections (P→I, P→T, I↔I, I→P, I→T, I→L), and Annex index to reflect new verbs.
- Rationale: Cover justice workflows (trial, verdict, sentencing), selection via election, territorial exile and ecclesiastical interdict, formal instrument workflows (signing/ratification), and third‑party dispute resolution; maintain non-overlap with existing verbs.
- Guideline reference: CONTRIBUTING §5a (Verb Proposal workflow); §5c (Sensitive verbs policy) for EXILES/INTERDICTS when context is coercive.
- Breaking changes: None (additive; matrix updated as a view of canon).

## Process
- Proposals are filed as issues titled `Verb Proposal: <VERB>` with definition, allowed pairs, examples, and evidence plan.
- Upon approval, maintainers update `relations_vocabulary.md` and synchronize `node_interaction_matrix.md` and affected cluster docs.
- This log captures the date, changes, rationale, and touched files for transparency.

## References
- Source of truth: `docs/guidelines/relations_vocabulary.md`
- Interaction pairs: `docs/guidelines/node_interaction_matrix.md`
- Example usage: `docs/guidelines/hebrew_cluster.md`
