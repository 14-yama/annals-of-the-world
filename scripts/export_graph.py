"""
Export graph data to CSV/JSON for analysis or backup.
"""

from neo4j import GraphDatabase
import csv
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env.local'))
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "neo4j")

NODES_OUT = os.path.join(os.path.dirname(__file__), '../data/nodes_export.csv')
RELATIONSHIPS_OUT = os.path.join(os.path.dirname(__file__), '../data/relationships_export.csv')
if __name__ == "__main__":
    main()
