# main.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
from db import get_neo4j_driver

import csv


CSV_PATH = "data/Politics/Deployable Code/Political_Systems_and_Governance.v1.csv"

def create_idea_nodes(driver, csv_path):
    with open(csv_path, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        with driver.session() as session:
            for row in reader:
                session.write_transaction(create_idea_node, row)

def create_idea_node(tx, row):
    tx.run("""
        MERGE (i:Idea {slug: $slug})
        SET i.name = $name,
            i.definition = $definition,
            i.category = $category
    """, slug=row['slug'], name=row['name'], definition=row['definition'], category=row['category'])

if __name__ == "__main__":
    driver = get_neo4j_driver()
    create_idea_nodes(driver, CSV_PATH)
    print("✅ Node population complete.")
