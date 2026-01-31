"""scripts/ingest_nodes.py

Small, resilient importer for nodes from JSON or CSV seed files into Neo4j.

Behavior
- Default input: `data/Nodes/nodes.json` (preferred). Falls back to `data/Nodes/nodes.csv`.
- For each record: MERGE node by `slug` and label (specified in `label` field).
- Sets/overwrites properties with the record's keys (except internal `id`).

Usage:
    python scripts/ingest_nodes.py [path/to/nodes.json|.csv]

This script expects the `.env.local` file at repo root with NEO4J_URI/USER/PASSWORD.
"""

import os
import sys
import json
import csv
from typing import Dict, Any, List

from dotenv import load_dotenv
from neo4j import GraphDatabase


load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env.local'))
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "neo4j")


def read_json(path: str) -> List[Dict[str, Any]]:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        # Support two shapes:
        # 1) An array of node objects (legacy)
        # 2) An object with a `_meta` and `nodes` array (preferred): {"_meta": {...}, "nodes": [...]}
        if isinstance(data, dict) and 'nodes' in data:
            return data['nodes']
        if isinstance(data, list):
            return data
        raise ValueError(f"Unsupported JSON structure in {path}")


def read_csv(path: str) -> List[Dict[str, Any]]:
    rows = []
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            # Convert empty strings to None, leave arrays as comma-separated strings for now
            cleaned = {k: (v if v != '' else None) for k, v in r.items()}
            rows.append(cleaned)
    return rows


def connect():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    return driver


def upsert_node(tx, label: str, slug: str, props: Dict[str, Any]):
    # Remove keys we don't want as properties
    props = {k: v for k, v in props.items() if k not in ('id', 'label')}

    # Use MERGE on slug to keep identity stable
    cypher = f"MERGE (n:`{label}` {{slug: $slug}}) SET n += $props RETURN n.slug AS slug"
    result = tx.run(cypher, slug=slug, props=props)
    return result.single()


def ingest(records: List[Dict[str, Any]]):
    driver = connect()
    created = 0
    updated = 0
    with driver.session() as session:
        for rec in records:
            label = rec.get('label') or rec.get('type') or 'Thing'
            slug = rec.get('slug')
            if not slug:
                print("Skipping record without slug:", rec)
                continue
            # Ensure label is a safe string (no spaces)
            label = str(label).replace(' ', '_')

            # Use execute_write (modern driver API) to run our upsert
            res = session.execute_write(upsert_node, label, slug, rec)
            if res:
                created += 1
    driver.close()
    print(f"Ingested {created} node records (by slug).")


def main(argv=None):
    argv = argv or sys.argv[1:]
    # Prefer the consolidated per-cluster split or canonical nodes file under data/Nodes
    default_json = os.path.join(os.path.dirname(__file__), '../data/Nodes/nodes.json')
    # legacy fallback
    default_csv = os.path.join(os.path.dirname(__file__), '../data/Nodes/nodes.csv')

    path = argv[0] if argv else (default_json if os.path.exists(default_json) else default_csv)

    if not os.path.exists(path):
        print(f"Input file not found: {path}")
        sys.exit(2)

    if path.lower().endswith('.json'):
        records = read_json(path)
    else:
        records = read_csv(path)

    print(f"Read {len(records)} records from {path}")
    ingest(records)


if __name__ == '__main__':
    main()
