# README -> Graph Data Workflow

This playbook covers how to take curated cluster README files and regenerate the canonical JSON payloads in `data/Nodes/` and `data/Relationships/`.

## 1. Curate README tables
- Keep the node tables under each `####` section accurate; they drive `nodes.<cluster>.json`.
- Run `python3 scripts/backfill_relationship_tables.py` whenever wiring bullet lists change. The script regenerates the `### Relationships` table, preserves any manual descriptions that already exist, and inserts a single note (`_Auto-generated from wiring; edit freely for nuance._`) instead of repeating boilerplate in every row.
- Skim the regenerated table for tone and clarity. Edit any row descriptions directly in the table if nuance is needed.

## 2. Generate per-cluster node JSON
```
python3 scripts/generate_nodes_from_readmes.py
```
- Creates `data/Nodes/nodes.<cluster>.json` with registry-compliant attributes.
- Each file receives a timestamped backup before being overwritten.
- The aggregate placeholder at `data/Nodes/nodes.json` exists so downstream tooling always finds a file; replace it with a real aggregate dump when we decide on the merge strategy.

## 3. Generate per-cluster relationship JSON
```
python3 scripts/generate_relationships_from_readmes.py
```
- Reads the refreshed `### Relationships` tables plus any `Parent root` / `Interfaces` sections.
- Writes `data/Relationships/relationships.<cluster>.json` and backs up the previous version.
- Automatically runs the node and relationship normalizers. The node normalizer now no-ops (exit code 0) if `data/Nodes/nodes.json` is still just the stub.

## 4. Verify outputs
- Spot-check a couple of generated JSON files (nodes + relationships) for each cluster touched in this pass.
- Run `git status` to confirm only the expected README and JSON files changed.
- Commit with a message that captures both the README edits and regenerated data, e.g. `Update English_Reformation wiring and regen data`.

Following this sequence keeps README tables, JSON exports, and schema normalizers in sync with minimal manual effort.
