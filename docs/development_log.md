# Development Log — Annals of the World

Date: 2025-10-03

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
