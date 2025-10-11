---
title: Project Governance — Annals of the World
status: ACTIVE
version: 0.1
summary: How decisions are proposed, reviewed, and recorded for schemas, relationship verbs, and documentation.
---

# Governance Policy

This document explains how we make decisions about the data model, relationship verbs, schemas, and documentation.

## Scope
- Relationship verbs (source of truth; semantics and allowed pairs)
- Interaction matrix (allowed node-type pairs, example triples)
- Schema and constraints for nodes/relationships
- Curator workflow and evidence standards
- Cluster normalization and content governance
- Documentation structure, navigation, and governance artifacts

## Authorities (single sources of truth)
- Verbs Canon: docs/guidelines/relations_vocabulary.md
- Interaction Rules: docs/guidelines/node_interaction_matrix.md
- Schema Reference: docs/guidelines/schema.md
- Curator Workflow: docs/guidelines/workflow.md and curator_runbook.md
- Decision Records: docs/governance/audit_log.md

## Roles
- Maintainers: approve proposals, publish releases, keep docs current.
- Curators: propose/normalize verbs, seed clusters, run audits, attach evidence.
- Contributors: file issues/PRs, improve docs, add data following the workflow.

## Decision Process
1) Proposal
- Open an issue with a clear title, e.g., "Verb Proposal: <VERB>" or "Schema Proposal: <TOPIC>".
- Include problem statement, rationale, minimal examples, and impact on existing data.

2) Discussion & Review
- Maintainers and curators discuss trade-offs and check impact on the canon and matrix.
- For verbs: confirm semantics, allowed node-type pairs, and examples.

3) Decision & Merge
- If accepted, update the relevant authority files (vocabulary/matrix/schema/workflow/cluster docs).
- Record a concise entry in docs/governance/audit_log.md (date, category, what changed, why, files touched).

4) Follow-up
- Normalize any drift in clusters to the new canon.
- If breaking, provide deprecation guidance or migration notes.

## Versioning & Releases
- Use the version fields in each authority doc (e.g., relations_vocabulary.md v0.2).
- Group related accepted proposals into a minor version bump.
- Summarize notable changes in a release note (docs/development_log.md or GitHub Releases), linking to audit entries.

## Compliance & QA
- Run audit queries in docs/guidelines/audit_queries.md before publishing.
- Keep relationship labels in active voice; avoid synonyms outside the canon.
- Validate clusters adhere to the interaction matrix and verb canon before merge.
- Periodically scan for non-whitelisted verbs and fix or deprecate.

## Contacts
- See CONTRIBUTING.md for how to reach maintainers and request curator privileges.

