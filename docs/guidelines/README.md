# Guidelines — Annals of the World

This folder contains human-readable governance, schema, and curator guidance for the project. Use this index to navigate the curator and developer docs.

Mandate
- All contributors MUST use only relationship verbs defined in `relations_vocabulary.md`.
- Any change to verbs, interaction rules, schema, or cluster semantics MUST follow `CONTRIBUTING.md` and be recorded in `governance/audit_log.md`.

Contents

- [classification.md](./classification.md) — call-number taxonomy and corpus registry
- [features_by_version.md](./features_by_version.md) — versioned feature timeline (v1 → v5)
- [schema.md](./schema.md) — v4 schema reference and example Cypher
- [workflow.md](./workflow.md) — curator workflow detailed steps
- [audit_queries.md](./audit_queries.md) — runnable Cypher QA checks (diagnostics)
- [curator_runbook.md](./curator_runbook.md) — one-page curator checklist and provenance snippets
- [crosswalk_crm_prov.md](./crosswalk_crm_prov.md) — CRM/PROV → Neo4j verb crosswalk
- [framework_matrix.md](./framework_matrix.md) — Active-voice framework→verb matrix

Recommended first reads

1. [curator_runbook.md](./curator_runbook.md) — short checklist for everyday curation
2. [audit_queries.md](./audit_queries.md) — run these queries before publishing a cluster
3. [schema.md](./schema.md) — authoritative node/relationship shapes and constraints

Related lookups

- [relations_vocabulary.md](./relations_vocabulary.md)
- [node_interaction_matrix.md](./node_interaction_matrix.md)
- Governance: [Policy](../governance/GOVERNANCE.md) • [Audit Log](../governance/audit_log.md)
