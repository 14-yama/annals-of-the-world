# Legacy Scripts Archive

> **Archived: 2026-01-24**

These scripts have been archived because they are either:
- One-time migrations that have been completed
- Superseded by the unified `seed_backend.py` pipeline
- Utilities no longer needed in the current workflow

## Directory Structure

```
legacy-scripts/
├── one-time-migrations/   # Completed schema/data migrations
├── superseded/            # Replaced by seed_backend.py
└── utilities/             # Unused utility scripts
```

## One-Time Migrations

Scripts that performed specific data transformations:

| Script | Original Purpose | Completed |
|--------|-----------------|-----------|
| `migrate_marriages_to_events.py` | Convert MARRIES → Marriage Events | 2025-01 |
| `migrate_relationships_to_cluster.py` | Merge legacy relationships.json | 2025-11 |
| `cleanup_relationships_dedupe.py` | Deduplicate English_Reformation | 2025-11 |
| `expand_english_reformation.py` | Major cluster expansion | 2025-12 |
| `fix_labels_concept_to_idea.py` | Relabel Concept → Idea | 2025-11 |
| `convert_includes_to_is_part_of.py` | Flip INCLUDES → IS_PART_OF | 2025-12 |
| `apply_chicago_citation.py` | Set citation_style fields | 2025-12 |
| `update_node_definitions.py` | Backfill node descriptions | 2025-12 |

## Superseded Scripts

Scripts replaced by `scripts/seed_backend.py`:

| Script | Replaced By |
|--------|-------------|
| `setup_constraints.py` | `seed_backend.py` Step 1 |
| `init_db.py` | `seed_backend.py` Step 1 |
| `seed_places.py` | `seed_backend.py` Step 2 + `geo_registry.py` |
| `ingest_nodes.py` | `seed_backend.py` Step 3 |
| `ingest_relationships.py` | `seed_backend.py` Step 3 |
| `ingest_edge_arrays.py` | `seed_backend.py` Step 3 |
| `normalize_nodes*.py` | `admin/normalize_nodes_all_clusters.py` |

## ⚠️ Do Not Use

These scripts are archived for reference only. Using them may:
- Create duplicate data
- Conflict with current schema
- Override production data

For backend seeding, use:
```bash
python scripts/seed_backend.py --clusters English_Reformation
```

## Recovery

If you need functionality from an archived script:
1. Check if `seed_backend.py` or an admin script already covers it
2. If not, copy the archived script back and adapt to current schema
3. Document the use case in `docs/development_log.md`
