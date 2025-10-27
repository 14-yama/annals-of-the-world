# Project Workflow: Python, Cypher, and APOC Integration

This guide outlines best practices for managing the Annals of the World project using Python, Cypher, and APOC. It ensures robust, scalable, and maintainable graph operations, data ingestion, and governance.

---

## 1. Schema & Registry Setup
- Use Cypher migration files (`.cypher`) to define constraints, indexes, and seed core nodes (e.g., frameworks, corpus).
- Use APOC triggers for validation, audit logging, and derived fields.

## 2. Data Ingestion & Automation
- Use Python scripts (with the Neo4j driver) to ingest data, run batch operations, and orchestrate ETL pipelines.
- Python can call Cypher queries and APOC procedures, handle external data sources, and automate updates.

## 3. Advanced Graph Operations
- Use Cypher for querying, updating, and managing graph data.
- Use APOC for complex tasks: batch imports, periodic commits, custom triggers, and utility functions.

## 4. Governance & QA
- Use APOC triggers for enforcing active-voice relationships, temporal sanity, and evidence requirements.
- Use Python for reporting, audits, and integration with external systems.

---

## Recommended Hybrid Workflow

1. **Define schema and registry** in Cypher migration files and apply them to Neo4j.
2. **Seed core nodes** (frameworks, corpus, etc.) using Cypher and APOC.
3. **Automate data ingestion** and ETL with Python scripts, leveraging Cypher and APOC for graph operations.
4. **Enforce governance and QA** using APOC triggers and Python-based reporting/audits.
5. **Integrate external systems** and automate updates with Python orchestration.

---

## Example Usage

- Apply schema:
  ```bash
  cypher-shell -u neo4j -p yourpassword -f migrations/001_schema.cypher
  ```
- Seed frameworks:
  ```bash
  cypher-shell -u neo4j -p yourpassword -f migrations/framework-registry.cypher
  ```
- Ingest data:
  ```bash
  npm run start:demo
  # or
  python scripts/ingest.py
  ```
- Run QA checks and audits:
  - Use APOC triggers and Python scripts for validation and reporting.

---

## Why Use All Three?
- **Cypher**: Direct graph operations, schema, and migrations.
- **APOC**: Advanced procedures, triggers, and utilities.
- **Python**: Orchestration, automation, ETL, and integration.

This approach leverages the strengths of each tool for a flexible, auditable, and future-proof project.
