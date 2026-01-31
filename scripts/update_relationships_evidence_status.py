#!/usr/bin/env python3
"""Update relationships.<cluster>.json to record whether evidence nodes exist in Neo4j
and whether relationships use inline evidence.

Adds two optional boolean fields to each relationship object:
- `evidence_node_present`: true if an `:Evidence` node with that slug exists in DB
- `inline_evidence`: true if the relationship has a non-null `evidence_url`

Usage:
  python scripts/update_relationships_evidence_status.py --cluster English_Reformation
"""
from __future__ import annotations
import json
import os
from pathlib import Path
import argparse

try:
    from dotenv import load_dotenv
except Exception:
    def load_dotenv(*args, **kwargs):
        return None

try:
    from neo4j import GraphDatabase
except Exception:
    GraphDatabase = None

ROOT = Path(__file__).resolve().parents[1]
RELS_DIR = ROOT / 'data' / 'Relationships'


def normalize_evidence_slug(slug: str | None) -> str | None:
    if not slug:
        return slug
    s = str(slug).strip()
    # Legacy format occasionally used in relationship JSON.
    if s.startswith('evidence.'):
        s = 'evidence_' + s[len('evidence.'):]
    return s

def load_env():
    env = ROOT / '.env.local'
    if env.exists():
        load_dotenv(env)

def read_relationships(cluster: str) -> dict:
    path = RELS_DIR / f'relationships.{cluster}.json'
    if not path.exists():
        raise SystemExit(f'Relationships file not found: {path}')
    return json.loads(path.read_text(encoding='utf-8'))

def write_relationships(cluster: str, payload: dict):
    path = RELS_DIR / f'relationships.{cluster}.json'
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding='utf-8')

def evidence_exists_in_db(slugs: set, uri: str, user: str, password: str) -> set:
    if GraphDatabase is None:
        raise SystemExit('neo4j driver not installed')
    driver = GraphDatabase.driver(uri, auth=(user, password))
    found = set()
    try:
        with driver.session() as session:
            for slug in sorted(slugs):
                rec = session.run('MATCH (e:Evidence {slug:$slug}) RETURN count(e) as c', slug=slug).single()
                if rec and rec['c'] and rec['c'] > 0:
                    found.add(slug)
    finally:
        driver.close()
    return found

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cluster', required=True)
    args = parser.parse_args()

    load_env()
    uri = os.getenv('NEO4J_URI', 'bolt://localhost:7687')
    user = os.getenv('NEO4J_USER', 'neo4j')
    password = os.getenv('NEO4J_PASSWORD', 'neo4j')

    payload = read_relationships(args.cluster)
    rels = payload.get('relationships', []) if isinstance(payload, dict) else payload

    # Canonicalize evidence_slug values in-place (safe normalization only).
    for r in rels:
        old = r.get('evidence_slug')
        new = normalize_evidence_slug(old)
        if old and new and old != new:
            r['evidence_slug'] = new

    slugs = {r.get('evidence_slug') for r in rels if r.get('evidence_slug')}
    slugs = {s for s in slugs if s}
    print(f'Checking {len(slugs)} evidence slugs in DB...')
    found = evidence_exists_in_db(slugs, uri, user, password)
    print(f'Found {len(found)} evidence nodes in DB')

    updated = 0
    for r in rels:
        changed = False
        evid = r.get('evidence_slug')
        if evid:
            present = evid in found
            if r.get('evidence_node_present') != present:
                r['evidence_node_present'] = present
                changed = True
        inline = r.get('evidence_url') is not None
        if r.get('inline_evidence') != inline:
            r['inline_evidence'] = inline
            changed = True
        if changed:
            updated += 1

    if updated:
        write_relationships(args.cluster, payload)
        print(f'Wrote updated relationships file with {updated} changes')
    else:
        print('No changes required')

if __name__ == '__main__':
    main()
