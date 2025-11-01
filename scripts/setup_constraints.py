from neo4j import GraphDatabase
import os

from dotenv import load_dotenv
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env.local'))

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
        "CREATE INDEX idea_status_index IF NOT EXISTS FOR (i:Idea) ON (i.status)",
        "CREATE INDEX idea_timeframe_index IF NOT EXISTS FOR (i:Idea) ON (i.timeframe)",

        # PERSON NODE CONSTRAINTS
        "CREATE CONSTRAINT person_name_unique IF NOT EXISTS FOR (p:Person) REQUIRE p.name IS UNIQUE",
        "CREATE CONSTRAINT person_slug_unique IF NOT EXISTS FOR (p:Person) REQUIRE p.slug IS UNIQUE",
        "CREATE INDEX person_category_index IF NOT EXISTS FOR (p:Person) ON (p.category)",
        "CREATE INDEX person_status_index IF NOT EXISTS FOR (p:Person) ON (p.status)",
        "CREATE INDEX person_timeframe_index IF NOT EXISTS FOR (p:Person) ON (p.timeframe)",

        # EVENT NODE CONSTRAINTS
        "CREATE CONSTRAINT event_name_unique IF NOT EXISTS FOR (e:Event) REQUIRE e.name IS UNIQUE",
        "CREATE CONSTRAINT event_slug_unique IF NOT EXISTS FOR (e:Event) REQUIRE e.slug IS UNIQUE",
        "CREATE INDEX event_category_index IF NOT EXISTS FOR (e:Event) ON (e.category)",
        "CREATE INDEX event_status_index IF NOT EXISTS FOR (e:Event) ON (e.status)",
        "CREATE INDEX event_timeframe_index IF NOT EXISTS FOR (e:Event) ON (e.timeframe)",

        # PLACE NODE CONSTRAINTS
        "CREATE CONSTRAINT place_name_unique IF NOT EXISTS FOR (pl:Place) REQUIRE pl.name IS UNIQUE",
        "CREATE CONSTRAINT place_slug_unique IF NOT EXISTS FOR (pl:Place) REQUIRE pl.slug IS UNIQUE",
        "CREATE INDEX place_category_index IF NOT EXISTS FOR (pl:Place) ON (pl.category)",
        "CREATE INDEX place_status_index IF NOT EXISTS FOR (pl:Place) ON (pl.status)",
        "CREATE INDEX place_timeframe_index IF NOT EXISTS FOR (pl:Place) ON (pl.timeframe)",

        # INSTITUTION NODE CONSTRAINTS
        "CREATE CONSTRAINT institution_name_unique IF NOT EXISTS FOR (inst:Institution) REQUIRE inst.name IS UNIQUE",
        "CREATE CONSTRAINT institution_slug_unique IF NOT EXISTS FOR (inst:Institution) REQUIRE inst.slug IS UNIQUE",
        "CREATE INDEX institution_category_index IF NOT EXISTS FOR (inst:Institution) ON (inst.category)",
        "CREATE INDEX institution_status_index IF NOT EXISTS FOR (inst:Institution) ON (inst.status)",
        "CREATE INDEX institution_timeframe_index IF NOT EXISTS FOR (inst:Institution) ON (inst.timeframe)",

        # MOVEMENT NODE CONSTRAINTS
        "CREATE CONSTRAINT movement_name_unique IF NOT EXISTS FOR (m:Movement) REQUIRE m.name IS UNIQUE",
        "CREATE CONSTRAINT movement_slug_unique IF NOT EXISTS FOR (m:Movement) REQUIRE m.slug IS UNIQUE",
        "CREATE INDEX movement_category_index IF NOT EXISTS FOR (m:Movement) ON (m.category)",
        "CREATE INDEX movement_status_index IF NOT EXISTS FOR (m:Movement) ON (m.status)",
        "CREATE INDEX movement_timeframe_index IF NOT EXISTS FOR (m:Movement) ON (m.timeframe)",

        # ARTIFACT NODE CONSTRAINTS
        "CREATE CONSTRAINT artifact_name_unique IF NOT EXISTS FOR (a:Artifact) REQUIRE a.name IS UNIQUE",
        "CREATE CONSTRAINT artifact_slug_unique IF NOT EXISTS FOR (a:Artifact) REQUIRE a.slug IS UNIQUE",
        "CREATE INDEX artifact_category_index IF NOT EXISTS FOR (a:Artifact) ON (a.category)",
        "CREATE INDEX artifact_status_index IF NOT EXISTS FOR (a:Artifact) ON (a.status)",
        "CREATE INDEX artifact_timeframe_index IF NOT EXISTS FOR (a:Artifact) ON (a.timeframe)",

        # RELATIONSHIP PROPERTY CONSTRAINTS (Neo4j 5+)
        "CREATE CONSTRAINT framed_by_citation_required IF NOT EXISTS FOR ()-[r:FRAMED_BY]-() REQUIRE r.citation_style IS NOT NULL",
        "CREATE CONSTRAINT framed_by_evidence_url_required IF NOT EXISTS FOR ()-[r:FRAMED_BY]-() REQUIRE r.evidence_url IS NOT NULL",
        "CREATE CONSTRAINT framed_by_page_refs_required IF NOT EXISTS FOR ()-[r:FRAMED_BY]-() REQUIRE r.page_refs IS NOT NULL",
        "CREATE CONSTRAINT framed_by_source_note_required IF NOT EXISTS FOR ()-[r:FRAMED_BY]-() REQUIRE r.source_note IS NOT NULL",
    ]

    with driver.session() as session:
        for query in constraints:
            print(f"Applying: {query}")
            session.run(query)

    print("✅ All constraints applied successfully.")

if __name__ == "__main__":
    create_constraints()
