"""
Ingest relationships from CSV/JSON into Neo4j, enforcing schema.
"""
from neo4j import GraphDatabase
import csv

import csv
from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env.local'))
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "neo4j")

CSV_PATH = os.path.join(os.path.dirname(__file__), '../data/relationships.csv')
    main()
