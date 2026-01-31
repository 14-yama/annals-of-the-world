#!/usr/bin/env python3
"""Query Neo4j and print the CENSORS relationship and linked Evidence node for demo.
"""
from __future__ import annotations
import os
from neo4j import GraphDatabase

uri = os.getenv('NEO4J_URI', 'bolt://localhost:7687')
user = os.getenv('NEO4J_USER', 'neo4j')
password = os.getenv('NEO4J_PASSWORD', 'neo4j')

driver = GraphDatabase.driver(uri, auth=(user, password))
with driver.session() as session:
    q = """
    MATCH (a {slug:'Roman_Catholic_Church'})-[r:CENSORS]->(b {slug:'Protestant_Doctrine_in_England'})
    OPTIONAL MATCH (e:Evidence)-[s:DOCUMENTS]->(a)
    OPTIONAL MATCH (e2:Evidence)-[t:DOCUMENTS]->(b)
    RETURN a.slug AS start, type(r) AS rel_type, b.slug AS end,
           r.description AS rel_description,
        collect(DISTINCT e.slug) AS evidence_from_start, collect(DISTINCT e.title) AS evidence_title,
        collect(DISTINCT e2.slug) AS evidence_from_end, collect(DISTINCT e2.title) AS evidence_title_end
    """
    rec = session.run(q).single()
    if not rec:
        print('No CENSORS relationship found between the two nodes')
    else:
        print('Start node:', rec['start'])
        print('Relationship:', rec['rel_type'])
        print('End node:', rec['end'])
        print('Rel description:', rec['rel_description'])
        print('Evidence from start node:', rec['evidence_from_start'])
        print('Evidence title:', rec['evidence_title'])
        print('Evidence from end node:', rec['evidence_from_end'])
        print('Evidence title (end):', rec['evidence_title_end'])
driver.close()
