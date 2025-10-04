# Development Log — Annals of the World

Date: 2025-10-03
Timestamp: 2025-10-04T03:35:44Z

## Update — 2025-10-04T03:36:16Z (most recent)

- Added `docs/guidelines/relations_vocabulary.md` (canonical verbs, evidence rules, QA snippets).
- Added `docs/guidelines/historian_framework.md` (framework provenance, FRAMED_BY rules, evidence promotion).
- Added `docs/guidelines/framework_matrix.md` (tabular framework→verb matrix).
- Added `docs/guidelines/crosswalk_crm_prov.md` (CIDOC-CRM / PROV crosswalk guidance).
- Added `docs/guidelines/audit_queries.md` (runnable Cypher QA checks) and created `scripts/` task plan for `run_audits.py`.
- Enriched `docs/guidelines/hebrew_cluster.md` with logic alignment guide, relationship templates, and links to vocabulary.
- Created links across docs for easier navigation and fixed plain filename references to Markdown links.

Notes: these are governance and pattern updates; no domain content from other clusters was imported—only structural rules and curator workflows.


Summary

- The project is undergoing a schema refactor to move core code into `src/annals`, standardize node shapes, and centralize migration and audit tooling.

Lessons learned

- ChatGPT vs GitHub Copilot: ChatGPT proved valuable for high-level brainstorming, documentation drafts, and generating design prose; GitHub Copilot (IDE assistant) is more useful for inline code completion and quick scaffolding inside the editor. Both have complementary strengths and are useful in different phases of development.

- MCP importance: adopting an MCP-style pattern (Model Context Protocol / small model-serving layer) reduces manual coding by centralizing schema-to-code generation, validation, and small translation tasks. An MCP layer helps keep imports and schema migrations consistent and reduces repetitive boilerplate across scripts.

What changed in this sprint

- Created `src/annals` package and moved/refactored helper scripts.
- Added `docs/guidelines/*` artifacts: audit queries, curator runbook, CRM/PROV crosswalk, framework matrix, features_by_version, classification, and summary.
- Added `docs/summary.md` and TOC link in `README.md`.

Next steps

- Scaffold `src/annals/models.py` (Pydantic/dataclasses) to lock down node shapes.
- Implement `scripts/run_audits.py` to run `docs/guidelines/audit_queries.md` and write reports.
- Add a small MCP server scaffold to automate schema-driven codegen and validation.

Notes

- Keep secrets out of the repo and rotate any credentials committed during early testing.

---

## Update — 2025-10-03T22:26:00Z (appendix)

New governance and curator artifacts added this sprint (summary):

- `docs/guidelines/relations_vocabulary.md` — Canonical, auditable verb list with allowed node-type pairs, evidence annotation rules, deprecation policy, and Cypher QA snippets.
- `docs/guidelines/historian_framework.md` — Historian framework guide for `Framework` nodes, `FRAMED_BY` semantics, evidence promotion rules (inline → :Evidence), and curator workflow for framing and provenance.
- `docs/guidelines/framework_matrix.md` — Tabular mapping of interpretive frameworks to recommended active-voice verbs (CAUSES, DIFFUSES, TRANSMITS, CANONIZES, etc.).
- `docs/guidelines/crosswalk_crm_prov.md` — CIDOC-CRM / W3C PROV crosswalk showing how to translate provenance records into the project's node/edge patterns.
- `docs/guidelines/audit_queries.md` — Runnable Cypher checks for QA (missing FRAMED_BY, orphan nodes, passive verbs, duplicate slugs, call-number mismatches). Script scaffolding planned: `scripts/run_audits.py`.
- `docs/guidelines/hebrew_cluster.md` — Enriched with logic alignment guide, relationships templates, relationship node-type matrices, and curated example triples; linked to the relations vocabulary.
- `docs/guidelines/README.md` — updated index listing the above artifacts.

Actions performed

- Converted many inline backtick references to active Markdown links across docs for easier navigation and publication.
- Created framework matrix table for curator lookup (more readable than bullets).
- Added QA snippets and governance rules to reduce verb drift and ensure evidence promotion.

Next practical tasks (prioritized)

1. Normalize existing relationship labels in all cluster files to the canonical verbs (UPPER_SNAKE_CASE) and run the passive-verb audit.
2. Implement `scripts/run_audits.py` to run `audit_queries.md` and export JSON reports in `reports/`.
3. Generate seed CSV templates (nodes + rels) for `class 9` from `hebrew_cluster.md` scaffold.
4. Promote multi-use sources (e.g., Dead Sea Scrolls publications, Septuagint critical editions) to `:Evidence` nodes and update edges.
5. Create curator onboarding checklist and PR templates for promoting inline citations to `:Evidence`.

Notes & Rationale

- The recent additions are intentionally pattern-only when borrowing the gun cluster's logic: no domain content from that cluster was imported, only structural and governance patterns (evidence tiers, active-voice verbs, framework lens usage, promotion rules).
- These governance docs reduce ad-hoc curation and make it easier to automate QA and ingestion while preserving scholarly traceability.

If you'd like, I can start task (1) and run a normalization pass across `docs/guidelines/hebrew_cluster.md` to align verbs with `relations_vocabulary.md`, then run the passive-verb audit and report results.

NOTE: Going forward, all appended log entries will include an ISO8601 timestamp in UTC (e.g., `YYYY-MM-DDTHH:MM:SSZ`) immediately after the word "Update" to ensure precise provenance of documentation changes.
