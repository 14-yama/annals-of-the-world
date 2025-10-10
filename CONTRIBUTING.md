Thank you for contributing to Annals of the World — this file explains how to file issues, propose changes, and submit pull requests.

1) Code of Conduct
- Be respectful and constructive. Please follow the project's Code of Conduct (add `CODE_OF_CONDUCT.md` if you want to formalize it).

2) Issues
- Use issues to report bugs, request features, or propose changes to the data model or guidelines.
- Provide a clear title, steps to reproduce (for bugs), and relevant files or snippets.

3) Pull Requests
- Fork the repository and create a feature branch with a clear name (e.g., `fix/normalize-verbs` or `feat/ingest-cli`).
- Keep changes small and focused. One logical change per PR.
- Include tests where applicable and run the existing tests locally before opening a PR.
- Link the PR to an issue if one exists.

4) Coding & style
- Python: follow PEP8 conventions. The codebase uses `src/annals` with Pydantic models; prefer type-safe changes.
- Tests: add unit tests to `tests/` for new functionality.
- Docs: update `docs/` when adding or changing governance rules, schemas, or guidelines.

5) Data contributions (seed CSVs)
- Put seed CSVs in `data/` and reference the corresponding guideline file (e.g., `docs/guidelines/hebrew_cluster.md`).
- Include a small README or manifest describing source, license, and evidence provenance.

6) Audits and dry-runs
- Use `scripts/run_audits.py` to run QA queries before publishing seed data. When possible, run with a test/dry-run Neo4j instance.

7) Tests & CI
- The repository should run unit tests and audit checks on PRs. If you add a GH Action, follow the existing CI pattern.

8) Licensing & provenance
- Data: the project recommends CC0 for data intended for Wikimedia interoperability; keep data provenance clear and attach evidence (Tier A/B/D) using the `:Evidence` node pattern.
- Code: include a permissive license for code (MIT or Apache-2.0) if desired — add a separate LICENSE-CODE file or indicate in this file.

9) Contact & maintainers
- Open an issue to request an invitation to the maintainer team, or to propose governance changes.

Thank you for improving Annals of the World — contributions that increase provenance, evidence quality, and cross-cultural coverage are especially welcome.
