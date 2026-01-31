#!/usr/bin/env python3
"""Materialize Evidence↔Entity links from a cluster relationships file.

Primary model:
- Create `:DOCUMENTS` relationships from Evidence nodes to entity nodes for every
    relationship object that contains `evidence_slug`.

Legacy/optional:
- `:SUPPORTED_BY` can be created as an inverse convenience edge, but the project
    is standardizing on `:DOCUMENTS` as the canonical Evidence→content verb.

Usage:
    python scripts/link_evidence_to_entities.py --cluster English_Reformation --mode documents
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

def load_env():
    env = ROOT / '.env.local'
    if env.exists():
        load_dotenv(env)

def read_relationships(cluster: str) -> list[dict]:
    path = RELS_DIR / f'relationships.{cluster}.json'
    if not path.exists():
        raise SystemExit(f'Relationships file not found: {path}')
    payload = json.loads(path.read_text(encoding='utf-8'))
    rels = payload.get('relationships', []) if isinstance(payload, dict) else payload
    return rels

def link_entities(rels: list[dict], uri: str, user: str, password: str):
    if GraphDatabase is None:
        raise SystemExit('neo4j driver not installed in environment')
    driver = GraphDatabase.driver(uri, auth=(user, password))
    created = 0
    warnings = []
    try:
        with driver.session() as session:
            for r in rels:
                evid_slug = r.get('evidence_slug')
                if not evid_slug:
                    continue
                rel_id = r.get('id')
                start = r.get('start_slug')
                end = r.get('end_slug')
                params = {
                    'evid': evid_slug,
                    'start': start,
                    'end': end,
                    'rel_id': rel_id,
                }

                # Ensure evidence node exists
                res = session.run("MATCH (e:Evidence {slug:$evid}) RETURN e", evid=evid_slug)
                if not res.peek():
                    warnings.append(f'No Evidence node for slug {evid_slug} (rel id {rel_id})')
                    continue

                # Link start node -> Evidence
                if start:
                    q = (
                        "MATCH (n {slug:$start}), (e:Evidence {slug:$evid})"
                        " MERGE (n)-[r:SUPPORTED_BY {relationship_id:$rel_id}]->(e)"
                        " RETURN count(r) as c"
                    )
                    rec = session.run(q, **params).single()
                    if rec and rec['c'] > 0:
                        created += rec['c']
                    else:
                        created += 1

                # Link end node -> Evidence
                if end:
                    q = (
                        "MATCH (n {slug:$end}), (e:Evidence {slug:$evid})"
                        " MERGE (n)-[r:SUPPORTED_BY {relationship_id:$rel_id}]->(e)"
                        " RETURN count(r) as c"
                    )
                    rec = session.run(q, **params).single()
                    if rec and rec['c'] > 0:
                        created += rec['c']
                    else:
                        created += 1

    finally:
        driver.close()
    return created, warnings


def link_entities_mode(rels: list[dict], uri: str, user: str, password: str, mode: str):
    """Create evidence linkage edges.

    mode:
    - supported_by: (Entity)-[:SUPPORTED_BY {relationship_id, page_refs?}]->(Evidence)  (legacy)
    - documents: (Evidence)-[:DOCUMENTS {cited_rel_id, relationship_id, page_refs?}]->(Entity)
      - both: create both edge directions
    """

    if GraphDatabase is None:
        raise SystemExit('neo4j driver not installed in environment')
    if mode not in {'supported_by', 'documents', 'both'}:
        raise SystemExit(f'Invalid mode: {mode}')

    driver = GraphDatabase.driver(uri, auth=(user, password))
    created = 0
    warnings: list[str] = []
    try:
        with driver.session() as session:
            for rel in rels:
                evid_slug = rel.get('evidence_slug')
                if not evid_slug:
                    continue

                rel_id = rel.get('id')
                start = rel.get('start_slug')
                end = rel.get('end_slug')
                page_refs = rel.get('page_refs')
                params = {
                    'evid': evid_slug,
                    'start': start,
                    'end': end,
                    'rel_id': rel_id,
                    'cited_rel_id': rel_id,
                    'relationship_id': rel_id,
                    'page_refs': page_refs,
                }

                # Ensure evidence node exists
                res = session.run("MATCH (e:Evidence {slug:$evid}) RETURN e", evid=evid_slug)
                if not res.peek():
                    warnings.append(f'No Evidence node for slug {evid_slug} (rel id {rel_id})')
                    continue

                def _link_supported_by(entity_slug: str | None):
                    nonlocal created
                    if not entity_slug:
                        return
                    q = (
                        "MATCH (n {slug:$entity}), (e:Evidence {slug:$evid})"
                        " MERGE (n)-[r:SUPPORTED_BY {relationship_id:$rel_id}]->(e)"
                        " SET r.page_refs = $page_refs"
                        " RETURN count(r) as c"
                    )
                    rec = session.run(q, entity=entity_slug, **params).single()
                    if rec and rec['c'] > 0:
                        created += rec['c']
                    else:
                        created += 1

                def _link_documents(entity_slug: str | None):
                    nonlocal created
                    if not entity_slug:
                        return
                    q = (
                        "MATCH (n {slug:$entity}), (e:Evidence {slug:$evid})"
                        " MERGE (e)-[r:DOCUMENTS {cited_rel_id:$cited_rel_id}]->(n)"
                        " SET r.page_refs = $page_refs, r.relationship_id = $relationship_id"
                        " RETURN count(r) as c"
                    )
                    rec = session.run(q, entity=entity_slug, **params).single()
                    if rec and rec['c'] > 0:
                        created += rec['c']
                    else:
                        created += 1

                if mode in {'supported_by', 'both'}:
                    _link_supported_by(start)
                    _link_supported_by(end)

                if mode in {'documents', 'both'}:
                    _link_documents(start)
                    _link_documents(end)

    finally:
        driver.close()

    return created, warnings

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cluster', required=True)
    parser.add_argument(
        '--mode',
        default='documents',
        choices=['supported_by', 'documents', 'both'],
        help='Which evidence linkage edge(s) to create.'
    )
    args = parser.parse_args()

    load_env()
    uri = os.getenv('NEO4J_URI', 'bolt://localhost:7687')
    user = os.getenv('NEO4J_USER', 'neo4j')
    password = os.getenv('NEO4J_PASSWORD', 'neo4j')

    rels = read_relationships(args.cluster)
    total_with_evidence = sum(1 for r in rels if r.get('evidence_slug'))
    print(f'Found {total_with_evidence} relationships with evidence_slug in cluster {args.cluster}')

    created, warnings = link_entities_mode(rels, uri, user, password, args.mode)
    print(f'Created or merged {created} evidence linkage relationships (mode={args.mode})')
    if warnings:
        print('Warnings:')
        for w in warnings:
            print('-', w)

if __name__ == '__main__':
    main()
