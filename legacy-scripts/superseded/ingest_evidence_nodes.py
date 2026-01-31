#!/usr/bin/env python3
"""Ingest Evidence JSON files referenced by a cluster's relationships into Neo4j as `:Evidence` nodes.

Usage:
  python scripts/ingest_evidence_nodes.py --cluster seed_examples_english_reformation
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
EVIDENCE_DIR = ROOT / 'data' / 'Evidence'
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

def find_evidence_slugs_for_cluster(cluster: str) -> set:
    rels_path = RELS_DIR / f'relationships.{cluster}.json'
    if not rels_path.exists():
        raise SystemExit(f"Relationships file not found: {rels_path}")
    payload = json.loads(rels_path.read_text(encoding='utf-8'))
    rels = payload.get('relationships', []) if isinstance(payload, dict) else payload
    slugs = {normalize_evidence_slug(r.get('evidence_slug')) for r in rels if r.get('evidence_slug')}
    return {s for s in slugs if s}

def load_evidence_by_slug(slug: str) -> dict | None:
    slug = normalize_evidence_slug(slug) or slug
    # search evidence files for matching slug field
    for path in sorted(EVIDENCE_DIR.glob('*.json')):
        try:
            data = json.loads(path.read_text(encoding='utf-8'))
        except Exception:
            continue
        if data.get('slug') == slug or path.stem == slug:
            return data
    return None

def ingest_into_neo4j(records: list[dict], uri: str, user: str, password: str):
    if GraphDatabase is None:
        raise SystemExit("neo4j driver not installed")
    driver = GraphDatabase.driver(uri, auth=(user, password))
    try:
        with driver.session() as session:
            for rec in records:
                slug = rec.pop('slug', None)
                if not slug:
                    continue
                props = {k: v for k, v in rec.items() if v is not None}
                cypher = "MERGE (e:Evidence {slug: $slug}) SET e += $props"
                session.run(cypher, slug=slug, props=props)
    finally:
        driver.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cluster', required=True)
    args = parser.parse_args()

    load_env()
    uri = os.getenv('NEO4J_URI', 'bolt://localhost:7687')
    user = os.getenv('NEO4J_USER', 'neo4j')
    password = os.getenv('NEO4J_PASSWORD', 'neo4j')

    slugs = find_evidence_slugs_for_cluster(args.cluster)
    if not slugs:
        print('No evidence_slug references found for cluster', args.cluster)
        return

    records = []
    for slug in sorted(slugs):
        rec = load_evidence_by_slug(slug)
        if rec is None:
            print('Warning: no evidence file found for slug', slug)
            continue
        records.append(rec)

    if not records:
        print('No evidence records to ingest')
        return

    print(f'Ingesting {len(records)} evidence nodes into {uri} as user {user}')
    ingest_into_neo4j(records, uri, user, password)
    print('Done')

if __name__ == '__main__':
    main()
