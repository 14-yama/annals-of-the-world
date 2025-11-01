# deploy_relationships.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
from db import get_neo4j_driver

import csv




CSV_FILE = "data/Politics/Deployable Code/political-idea-relationship v1.csv"

def create_relationships(driver, csv_file):
    with open(csv_file, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        with driver.session() as session:
            for row in reader:
                source = row["source_slug"].strip()
                relationship = row["relationship"].strip().upper().replace(" ", "_")
                target = row["target_slug"].strip()

                print(f"Creating: ({source}) -[:{relationship} {{framework: 'Idea Evolution'}}]-> ({target})")
                session.write_transaction(run_relationship_query, source, relationship, target)

def run_relationship_query(tx, source, relationship, target):
    query = f"""
    MATCH (a:Idea {{slug: $source_slug}})
    MATCH (b:Idea {{slug: $target_slug}})
    MERGE (a)-[r:{relationship} {{framework: "Idea Evolution"}}]->(b)
    """
    tx.run(query, source_slug=source, target_slug=target)

if __name__ == "__main__":
    driver = get_neo4j_driver()
    create_relationships(driver, CSV_FILE)
    print("✅ Relationship deployment complete.")
