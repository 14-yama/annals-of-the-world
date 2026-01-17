Seeding without Evidence nodes
=================================

Reason
------

Curators prefer inline citations for clarity when navigating the graph. Creating :Evidence nodes and their linking edges can clutter the visual graph and make relationship structure harder to read at a glance. Until we decide to restore Evidence nodes, follow the instructions below to seed the project without creating Evidence nodes or evidence-link edges.

How to seed without Evidence nodes
---------------------------------

- Seed nodes and relationships as usual, but do NOT run the evidence ingestion or linking steps.

- Example commands (cluster = English_Reformation):

  - Seed nodes & relationships only:

    `python scripts/admin/seed_neo4j_from_clusters.py --clusters English_Reformation`

  - Do NOT run these two scripts when you want to exclude Evidence nodes:

    `python scripts/ingest_evidence_nodes.py --cluster English_Reformation`

    `python scripts/link_evidence_to_entities.py --cluster English_Reformation --mode documents`

Notes
-----

- Relationships in `data/Relationships/*.json` that include `evidence_slug` or `evidence_url` will remain as inline citation metadata in the JSON files; omitting Evidence ingestion means there will be no :Evidence nodes or DOCUMENTS edges in the DB.

- If you later decide to restore Evidence nodes, run the ingestion and linking scripts above — they will create/merge :Evidence nodes and DOCUMENTS edges without re-seeding nodes/relationships.

- If you want a persistent flag or CLI option to toggle Evidence ingestion during seeding, I can add a `--skip-evidence` flag to the seeder script; say the word and I'll implement it.

History
-------

Created: 2026-01-17 — Added to support curator preference for inline citations.
