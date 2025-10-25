Thank you for contributing to Annals of the World — this file explains how to file issues, propose changes, and submit pull requests.

Governance mandate (read first)
- Strict adherence to the relationship verb source of truth is required. Use only verbs in `docs/guidelines/relations_vocabulary.md`.
- Any change to verbs, interaction rules, schema, or cluster semantics must follow this CONTRIBUTING guide and be recorded in `docs/governance/audit_log.md`.
- PRs that introduce non-canonical verbs or skip audit entries will not be merged.

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
	See [call_number_subject_heading_system.md](docs/guidelines/call_number_subject_heading_system.md) for the classification and call number system.

5) Data contributions (seed CSVs)
- Put seed CSVs in `data/` and reference the corresponding guideline file (e.g., `docs/guidelines/hebrew_cluster.md`).
- Include a small README or manifest describing source, license, and evidence provenance.

5a) Relationship verbs (source of truth)
- You MUST use only verbs listed in `docs/guidelines/relations_vocabulary.md` (Core + Supplementary). That file is the single source of truth.
- To propose a new verb or change semantics/allowed pairs, open an issue titled `Verb Proposal: <VERB>` and include definition, allowed pairs, example triples, and an evidence plan. A curator will review and update the vocabulary if accepted.
- PRs using verbs not defined in the vocabulary will be rejected or asked to normalize before review.

5b) Governance & decision records
- You MUST read the governance policy: `docs/governance/GOVERNANCE.md`.
- All accepted changes MUST be logged in `docs/governance/audit_log.md` with date, category, rationale, and touched files. If your PR triggers a governance change, include the draft audit entry in the PR description; maintainers will finalize it on merge.

5c) Sensitive verbs policy (P→P lethal outcomes)
- When using KILLS, MURDERS, ASSASSINATES, or EXECUTES:
	- Provide contextual properties (e.g., `context:"battle/self-defense/political"`, `victim_role`, `legal_authority`).
	- Supply Tier A/B evidence where possible; summarize ambiguity in `evidence_detail` if contested.
	- Prefer EXECUTES as I→P when carried out by an institution; include authority/source.
	- New edge patterns or semantics changes require an issue and an audit log entry upon merge.

Pre-PR compliance checklist
- [ ] All relationship labels are present in `relations_vocabulary.md`.
- [ ] If proposing a new/changed verb, there is a linked `Verb Proposal: <VERB>` issue.
- [ ] If governance docs (vocabulary/matrix/schema/cluster semantics) are changed, a matching entry is added to `docs/governance/audit_log.md`.
- [ ] Audit queries pass locally or have a rationale for exceptions.

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
