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

## Process
- Proposals are filed as issues titled `Verb Proposal: <VERB>` with definition, allowed pairs, examples, and evidence plan.
- Upon approval, maintainers update `relations_vocabulary.md` and synchronize `node_interaction_matrix.md` and affected cluster docs.
- This log captures the date, changes, rationale, and touched files for transparency.

## References
- Source of truth: `docs/guidelines/relations_vocabulary.md`
- Interaction pairs: `docs/guidelines/node_interaction_matrix.md`
- Example usage: `docs/guidelines/hebrew_cluster.md`
