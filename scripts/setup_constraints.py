from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def create_constraints():
    constraints = [
        # IDEA NODE CONSTRAINTS
        "CREATE CONSTRAINT idea_name_unique IF NOT EXISTS FOR (i:Idea) REQUIRE i.name IS UNIQUE",
        "CREATE CONSTRAINT idea_slug_unique IF NOT EXISTS FOR (i:Idea) REQUIRE i.slug IS UNIQUE",
        "CREATE INDEX idea_category_index IF NOT EXISTS FOR (i:Idea) ON (i.category)",

        # PERSON NODE CONSTRAINTS (example)
        "CREATE CONSTRAINT person_name_unique IF NOT EXISTS FOR (p:Person) REQUIRE p.name IS UNIQUE",
        "CREATE CONSTRAINT person_slug_unique IF NOT EXISTS FOR (p:Person) REQUIRE p.slug IS UNIQUE",

        # EVENT NODE CONSTRAINTS (example)
        "CREATE CONSTRAINT event_name_unique IF NOT EXISTS FOR (e:Event) REQUIRE e.name IS UNIQUE",
        "CREATE CONSTRAINT event_slug_unique IF NOT EXISTS FOR (e:Event) REQUIRE e.slug IS UNIQUE",

        # PLACE NODE CONSTRAINTS
        "CREATE CONSTRAINT place_name_unique IF NOT EXISTS FOR (pl:Place) REQUIRE pl.name IS UNIQUE",
        "CREATE CONSTRAINT place_slug_unique IF NOT EXISTS FOR (pl:Place) REQUIRE pl.slug IS UNIQUE",

        # INSTITUTION NODE CONSTRAINTS
        "CREATE CONSTRAINT institution_name_unique IF NOT EXISTS FOR (inst:Institution) REQUIRE inst.name IS UNIQUE",
        "CREATE CONSTRAINT institution_slug_unique IF NOT EXISTS FOR (inst:Institution) REQUIRE inst.slug IS UNIQUE",

        # MOVEMENT NODE CONSTRAINTS
        "CREATE CONSTRAINT movement_name_unique IF NOT EXISTS FOR (m:Movement) REQUIRE m.name IS UNIQUE",
        "CREATE CONSTRAINT movement_slug_unique IF NOT EXISTS FOR (m:Movement) REQUIRE m.slug IS UNIQUE",

        # ARTIFACT NODE CONSTRAINTS
        "CREATE CONSTRAINT artifact_name_unique IF NOT EXISTS FOR (a:Artifact) REQUIRE a.name IS UNIQUE",
        "CREATE CONSTRAINT artifact_slug_unique IF NOT EXISTS FOR (a:Artifact) REQUIRE a.slug IS UNIQUE",
    ]

    with driver.session() as session:
        for query in constraints:
            print(f"Applying: {query}")
            session.run(query)

    print("✅ All constraints applied successfully.")

if __name__ == "__main__":
    create_constraints()
