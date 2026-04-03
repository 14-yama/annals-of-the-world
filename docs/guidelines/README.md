# Guidelines — Annals of the World

This folder contains human-readable governance, schema, and curator guidance for the project. Use this index to navigate the curator and developer docs.

Mandate
- All contributors MUST use only relationship verbs defined in `relations_vocabulary.md`.
- Any change to verbs, interaction rules, schema, or cluster semantics MUST follow `CONTRIBUTING.md` and be recorded in `governance/audit_log.md`.

Contents

## Core Classification & Schema
- [call_number_subject_heading_system.md](./call_number_subject_heading_system.md) — international call number & subject heading system (core classification guide)
- [classification.md](./classification.md) — call-number taxonomy and corpus registry
- [features_by_version.md](./features_by_version.md) — versioned feature timeline (v1 → v5)
- [schema.md](./schema.md) — v4 schema reference and example Cypher

## Cluster & Container Management
- [global_cluster_management.md](./global_cluster_management.md) — **NEW** comprehensive guide for managing clusters at all levels (continent → region → country → thematic)
- [cluster_hierarchy.md](./cluster_hierarchy.md) — cross-domain cluster hierarchy design (Reformations, Weapons, etc.)

## Geographic & Naming
- [geo_naming.md](./geo_naming.md) — geographic naming conventions (place name changes over time)

## Curator Workflows
- [curator_workflow.md](./curator_workflow.md) — curator workflow detailed steps
- [curator_runbook.md](./curator_runbook.md) — one-page curator checklist and provenance snippets
- [audit_queries.md](./audit_queries.md) — runnable Cypher QA checks (diagnostics)

## Crosswalks & Matrices
- [crosswalk_crm_prov.md](./crosswalk_crm_prov.md) — CRM/PROV → Neo4j verb crosswalk
- [framework_matrix.md](./framework_matrix.md) — Active-voice framework→verb matrix
- [node_interaction_matrix.md](./node_interaction_matrix.md) — node type interaction rules

## Data Ingestion & Wikidata
- [wikidata_fetch_guide.md](./wikidata_fetch_guide.md) — Wikidata SPARQL fetch methodology (People, Institutions, Places)

Recommended first reads

1. [curator_runbook.md](./curator_runbook.md) — short checklist for everyday curation
2. [global_cluster_management.md](./global_cluster_management.md) — understand the cluster hierarchy
3. [audit_queries.md](./audit_queries.md) — run these queries before publishing a cluster
4. [schema.md](./schema.md) — authoritative node/relationship shapes and constraints

Related lookups

- [node-relationship-vocabulary.md](./node-relationship-vocabulary.md)
- [node_interaction_matrix.md](./node_interaction_matrix.md)
- Geo registry: [geo-registry/README.md](../../geo-registry/README.md)
- Governance: [Policy](../governance/GOVERNANCE.md) • [Audit Log](../governance/audit_log.md)
