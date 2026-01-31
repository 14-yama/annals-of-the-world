"""
Initialize Neo4j database, constraints, and indexes.
Recommended foundation script for Annals of the World.
"""
from neo4j import GraphDatabase
import os

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

CONSTRAINTS = [
    # Example: "CREATE CONSTRAINT ON (n:Place) ASSERT n.iso_code IS UNIQUE"
]
INDEXES = [
    # Example: "CREATE INDEX ON :Event(window)"
]

def apply_constraints_and_indexes(driver):
    with driver.session() as session:
        for cypher in CONSTRAINTS + INDEXES:
            print(f"Applying: {cypher}")
            session.run(cypher)

def main():
    print("Connecting to Neo4j...")
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    apply_constraints_and_indexes(driver)
    print("Initialization complete.")

if __name__ == "__main__":
    main()
