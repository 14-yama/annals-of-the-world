# Annals of the World — Roadmap

This roadmap describes a practical path from the current scaffolded project to a sustainable, community-driven historical knowledge graph with a target of 1,000,000 nodes and an eventual, well governed contribution into the Wikimedia ecosystem (Wikidata/Wikipedia integration). It maps tech, governance, data, community, and outreach work into phased milestones and immediate next steps.

## 1. Vision
- Build a scholarly, auditable, multilingual historical knowledge graph (Neo4j) modelling people, ideas, places, events, texts, movements and evidence across time and space.
- Reach 1,000,000 high-quality nodes through staged ingestion, global contributions, and curated seed clusters.
- Publish and interoperate with Wikimedia projects (Wikidata, Wikipedia) as an open-source contribution to the global web of knowledge.

## 2. Current scope (short review)
- Code: `src/annals` (models, neo4j client, validators) — good starting library with Pydantic models.
- Docs: `docs/guidelines/*` — relations vocabulary, historian framework, audit queries, curator runbook, international conventions, cluster scaffolds (Hebrew cluster), framework matrix.
- Scripts: `scripts/run_audits.py`, `setup_constraints.py` — basic audit & constraints tooling.
- Seeds: `data/` and `Refactor/` contain CSV and cluster scaffolds.
- Status: governance-heavy scaffold, seed clusters drafted, audit plan present, no production MCP/service layer yet, CI/workflow and contributor onboarding are partial.

## 3. High-level strategy to 1M nodes
Phases are calibrated to a multi-year program. Exact durations depend on contributor bandwidth and resourcing.

### Phase 0 — Hygiene & Governance (0–2 months)
- Rotate and remove any credentials in the repo (`.env.local`); enforce `.gitignore` (do this now).
- Add LICENSE (recommend CC0 or CC-BY-SA for data; choose and document clearly) and [CONTRIBUTING.md](../CONTRIBUTING.md).
- Publish a short lint_checklist.md for curators and an ISSUE_TEMPLATE + PR_TEMPLATE.
- Wire basic CI to run `scripts/run_audits.py` (dry-run mode) and unit tests on PRs.

Key deliverables
- LICENSE, CONTRIBUTING, CODE_OF_CONDUCT, ISSUE/PR templates, minimal GH Actions for tests/audits.

### Phase 1 — Core infra & ingestion pipelines (2–8 months)
- Harden `src/annals` as a tiny package: add CLI entry points, `requirements.txt`/`pyproject.toml` and tests covering node creation/validation.
- Build ingestion pipeline patterns: per-cluster CSV → validation (Pydantic) → dry-run audit → commit transactionally to Neo4j.
- Create `scripts/normalize_verbs.py` and `scripts/promote_evidence.py` to implement governance rules automatically.
- Add schema / constraints bootstrapping (`setup_constraints.py`) and tests.

Key deliverables
- Deployable CLI ingestion tool, canonical seed CSVs for 3 clusters, automatic audit reports, seed import runbook.

### Phase 2 — Scale, API & curator tooling (6–18 months)
- Scaffold a small MCP-style service (containerized) that exposes safe admin endpoints (idempotent ops): promote-evidence, import-csv, run-audit, normalize-verbs.
- Build a lightweight web UI (or notebook-based curator dashboard) for curators to propose/verify nodes and evidence; use the MCP for backend calls.
- Implement contributor roles and audit trails: who changed what, when, why (store provenance metadata using W3C PROV patterns in nodes/edges).
- Add bulk ingestion optimizations (batching, parallelism) and benchmark for Neo4j instance sizing (consider Aura/Enterprise for scale).

Key deliverables
- MCP service + CLI client, curator dashboard prototype, provenance logging.

### Phase 3 — Community growth & federation (12–36 months)
- Open contributor outreach: run workshops, create curated onboarding projects (translate one curated cluster into many languages), build a contributors program.
- Create a governance board and editorial steering group for approval of new frameworks / verbs.
- Establish synchronization protocols & mapping to Wikidata: property and item crosswalks, RDF/JSON-LD exports, use Wikidata properties where feasible.
- Pilot automated export to Wikidata (or bot-guided proposals) for a small, vetted subset of nodes (e.g., canonical persons with strong evidence).

Key deliverables
- Contributor onboarding program, editorial governance, Wikidata crosswalk and pilot.

### Phase 4 — 1M nodes & Wikimedia contribution (24–60 months)
- Scale ingestion via partnerships (digital libraries, university projects, crowdsourced contributions) and curated bulk datasets (public-domain corpora, museum open collections).
- Mature integration with Wikidata: follow community norms, use bot accounts and community-approved import workflows, incremental contributions with high metadata and provenance.
- Maintain high-quality exports (CSV, JSON-LD, RDF) and embed stable URIs for nodes.

Key deliverables
- 1M node milestone, documented Wikidata import strategy, persistent public datasets and visualizations.

## 4. Technical pillars & recommendations
- Schema & validation
  - Keep `src/annals/models.py` authoritative; add robust validators and inline docs; include export mappings for Wikidata/RDF.
- Provenance & evidence
  - Make `FRAMED_BY` mandatory for interpretive edges in published data; store citation metadata and evidence node tiers (A/B/D).
- Ingestion patterns
  - CSV/TSV seeds validated via Pydantic; dry-run audits produce JSON reports; acceptance toggled with `--publish` flag.
- Performance & DB ops
  - For scale, use Neo4j Enterprise or Aura with appropriate memory and read replicas. Partitioning by `Timeframe` and time-based sharding helps query performance.
- APIs & service
  - MCP endpoints should be idempotent, authenticated, and produce audit logs. Expose both CLI and HTTP APIs.
- Interop
  - Provide JSON-LD and RDF exports, and a property/item crosswalk to Wikidata (map node labels & properties to WD properties where appropriate).

## 5. Community & Wikimedia strategy
- Licensing
  - Use a permissive, clear data license. Wikidata accepts CC0 data; choose license compatible with Wikimedia if you plan imports.
- Mapping & piloting
  - Start with a small pilot: pick 100 well-sourced person nodes (classical & medieval), map to Wikidata items, open a Discussion/Project on Wikimedia to propose the import and process.
- Community-first approach
  - Engage Wikidata community early: create a project page, discuss crosswalks, ask for bot approval and community review before any imports.
- Quality-first import
  - Only export nodes with high provenance (Tier A/B) for initial Wikidata proposals; include full citations and scriptable patches.

## 6. KPIs & milestones
- Security milestone: remove secrets from repo (0 weeks).
- Phase 1 milestone: CLI ingestion + 3 clusters seeded (3–6 months).
- Phase 2 milestone: MCP + curator dashboard + 100k nodes (6–18 months).
- Phase 3 milestone: active contributor base (50+ contributors), community governance (12–36 months).
- Phase 4 milestone: 1,000,000 nodes and Wikimedia pilot import (24–60 months).

## 7. Risks & mitigations
- Data quality risk: enforce strong QA (automated audits + editorial review); require Tier A evidence for public exports.
- Scaling risk: benchmark early, choose managed Neo4j hosting, and implement partitioning strategies.
- Community friction (Wikimedia): engage early, be transparent, and follow their import/quality rules.
- Legal/IP risk: ensure dataset licensing is compatible with Wikimedia and any third-party datasets.

## 8. Immediate next actions (first sprint)
1. Rotate credentials now; remove `.env.local` from repo and ensure `.gitignore` covers local env files.
2. Add LICENSE (recommend CC0 for maximal Wikimedia compatibility) and [CONTRIBUTING.md](../CONTRIBUTING.md).
3. Commit this roadmap as [docs/ROADMAP.md](./ROADMAP.md) and link it from [README.md](../README.md) and [docs/summary.md](./summary.md).
4. Create `docs/guidelines/lint_checklist.md` and a `scripts/normalize_verbs.py` report script.
5. Wire a CI job to run `scripts/run_audits.py` on PRs (dry-run mode) and surface results in PR checks.

## 9. Who to involve / roles
- Core maintainers: keep schema & toolchain consistent (`src/annals` owners).
- Editorial board: approve framework additions and large import decisions.
- Curators: domain experts adding curated clusters and evidence.
- Community managers: onboarding, Wikimedia liaison, contributor events.

---

If you want, I will:
- create `LICENSE` and `CONTRIBUTING.md` stubs and commit them,
- add `docs/guidelines/lint_checklist.md`, or
- scaffold `scripts/normalize_verbs.py` and a GH Action to run audits on PRs.

Tell me which immediate task to run next and I will execute it.
