#!/usr/bin/env python3
"""Purge all nodes and relationships from the Neo4j database.

This is a destructive admin utility. It connects to the Neo4j
instance configured via environment variables and deletes the entire
property graph (nodes and relationships).

Environment variables:
  NEO4J_URI      - Bolt URI, e.g. bolt://localhost:7687
  NEO4J_USER     - Username, e.g. neo4j
  NEO4J_PASSWORD - Password

Usage:
  python admin/purge_neo4j_graph.py

You will be asked to confirm before deletion unless the environment
variable FORCE_PURGE=yes is set.
"""
import os
import sys

from neo4j import GraphDatabase


def get_driver():
    uri = os.environ.get("NEO4J_URI", "bolt://localhost:7687")
    user = os.environ.get("NEO4J_USER", "neo4j")
    password = os.environ.get("NEO4J_PASSWORD")

    if not password:
        print("NEO4J_PASSWORD environment variable is required.")
        sys.exit(1)

    return GraphDatabase.driver(uri, auth=(user, password))


def purge_all(tx):
    # Detach delete to remove relationships and nodes in one step
    tx.run("MATCH (n) DETACH DELETE n")


def main():
    force = os.environ.get("FORCE_PURGE", "no").lower() in {"yes", "true", "1"}

    if not force:
        print("WARNING: This will delete ALL nodes and relationships in Neo4j.")
        resp = input("Type 'DELETE' to proceed: ").strip()
        if resp != "DELETE":
            print("Aborted.")
            return

    driver = get_driver()
    try:
        with driver.session() as session:
            session.execute_write(purge_all)
        print("All nodes and relationships deleted.")
    finally:
        driver.close()


if __name__ == "__main__":
    main()
