#!/usr/bin/env python3
"""
Ingest edge arrays from relationship JSON files into Neo4j.

This script ingests the following edge arrays:
- timeframe_edges: OCCURS_DURING relationships to Timeframe nodes
- framed_by_edges: FRAMED_BY relationships to Framework nodes
- place_edges: OCCURS_IN relationships to Place nodes

Usage:
    python scripts/ingest_edge_arrays.py English_Reformation
    python scripts/ingest_edge_arrays.py --all
    python scripts/ingest_edge_arrays.py --all --edge-type framed_by
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Any

from dotenv import load_dotenv

# Load environment
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env.local'))
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "neo4j")


def get_driver():
    """Create Neo4j driver."""
    from neo4j import GraphDatabase
    return GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))


def ingest_timeframe_edges(session, edges: List[Dict]) -> int:
    """Ingest OCCURS_DURING edges to Timeframe nodes.

    Supports both historical shapes:
    - {node_slug, timeframe_slug, division, timeframe_name}
    - {node_slug, timeframe_division}
    """
    created = 0
    for edge in edges:
        node_slug = edge.get("node_slug")
        timeframe_slug = edge.get("timeframe_slug")
        division = edge.get("division") or edge.get("timeframe_division")
        timeframe_name = edge.get("timeframe_name")

        if not node_slug:
            continue

        # Ensure Timeframe exists (MERGE by slug when available).
        if timeframe_slug:
            session.run(
                """
                MERGE (t:Timeframe {slug: $slug})
                ON CREATE SET t.created_at = datetime()
                SET t.division = coalesce($division, t.division),
                    t.name = coalesce($name, t.name)
                """,
                slug=timeframe_slug,
                division=division,
                name=timeframe_name,
            )

        # Create edge, matching Timeframe by slug when possible.
        if timeframe_slug:
            result = session.run(
                """
                MATCH (n) WHERE n.slug = $node_slug
                MATCH (t:Timeframe {slug: $tf_slug})
                MERGE (n)-[r:OCCURS_DURING]->(t)
                ON CREATE SET r.created_at = datetime()
                SET r.division = coalesce($division, r.division)
                RETURN count(r) as created
                """,
                node_slug=node_slug,
                tf_slug=timeframe_slug,
                division=division,
            )
        elif division is not None:
            # Fallback for older datasets that only provide a division.
            session.run(
                """
                MERGE (t:Timeframe {division: $division})
                ON CREATE SET t.created_at = datetime()
                """,
                division=division,
            )
            result = session.run(
                """
                MATCH (n) WHERE n.slug = $node_slug
                MATCH (t:Timeframe {division: $division})
                MERGE (n)-[r:OCCURS_DURING]->(t)
                ON CREATE SET r.created_at = datetime()
                RETURN count(r) as created
                """,
                node_slug=node_slug,
                division=division,
            )
        else:
            continue

        record = result.single()
        if record and record["created"] > 0:
            created += 1

    return created


def ingest_framed_by_edges(session, edges: List[Dict], relationships: List[Dict]) -> int:
    """Ingest FRAMED_BY edges linking relationships to Framework nodes.
    
    Since Neo4j doesn't allow relationships on relationships directly,
    we create edges from the start node of each relationship to the Framework.
    
    Required properties on FRAMED_BY (per schema constraints):
    - citation_style
    - evidence_url
    - page_refs
    - source_note
    """
    created = 0
    
    # Build relationship_id -> relationship lookup
    rel_lookup = {}
    for rel in relationships:
        rel_id = rel.get("id")
        if rel_id:
            rel_lookup[rel_id] = rel
    
    for edge in edges:
        rel_id = edge.get("relationship_id")
        framework_slug = edge.get("framework_slug")
        
        if not rel_id or not framework_slug:
            continue
        
        # Get the relationship's start and end nodes
        rel = rel_lookup.get(rel_id)
        if not rel:
            continue
        
        start_slug = rel.get("start_slug")
        end_slug = rel.get("end_slug")
        
        if not start_slug or not end_slug:
            continue
        
        # Get evidence from the relationship if available
        evidence_slug = rel.get("evidence_slug", "evidence_Haigh_1993_English_Reformations")
        evidence_url = f"data/Evidence/{evidence_slug}.json"
        page_refs = rel.get("page_refs", "passim")
        source_note = f"Framing relationship between {start_slug} and {end_slug}"
        
        # Create FRAMED_BY from start node to Framework
        # Use CREATE after checking for existence, to ensure all properties are set atomically
        try:
            result = session.run("""
                MATCH (n) WHERE n.slug = $start_slug
                MATCH (f:Framework {slug: $framework_slug})
                OPTIONAL MATCH (n)-[existing:FRAMED_BY {context_end: $end_slug}]->(f)
                WITH n, f, existing
                WHERE existing IS NULL
                CREATE (n)-[r:FRAMED_BY {
                    context_end: $end_slug,
                    created_at: datetime(), 
                    relationship_id: $rel_id,
                    citation_style: 'Chicago 17',
                    evidence_url: $evidence_url,
                    page_refs: $page_refs,
                    source_note: $source_note
                }]->(f)
                RETURN count(r) as created
            """, start_slug=start_slug, end_slug=end_slug, 
                framework_slug=framework_slug, rel_id=rel_id,
                evidence_url=evidence_url, page_refs=page_refs, source_note=source_note)
            
            record = result.single()
            if record and record["created"] > 0:
                created += 1
        except Exception as e:
            # Skip edges that fail due to constraints or missing nodes
            pass
    
    return created


def ingest_place_edges(session, edges: List[Dict]) -> int:
    """Ingest OCCURS_IN edges to Place nodes."""
    created = 0
    for edge in edges:
        node_slug = edge.get("node_slug")
        place_slug = edge.get("place_slug")
        
        if not node_slug or not place_slug:
            continue
        
        # MERGE to avoid duplicates
        result = session.run("""
            MATCH (n) WHERE n.slug = $node_slug
            MATCH (p:Place {slug: $place_slug})
            MERGE (n)-[r:OCCURS_IN]->(p)
            ON CREATE SET r.created_at = datetime()
            RETURN count(r) as created
        """, node_slug=node_slug, place_slug=place_slug)
        
        record = result.single()
        if record and record["created"] > 0:
            created += 1
    
    return created


def ensure_framework_nodes(session) -> int:
    """Ensure Framework nodes exist for FRAMED_BY edges."""
    frameworks = [
        {"slug": "cause_and_effect", "name": "Cause and Effect", "description": "Causal relationships between historical events and phenomena"},
        {"slug": "cultural_diffusion", "name": "Cultural Diffusion", "description": "Spread of ideas, practices, and innovations across cultures"},
        {"slug": "continuity_and_change", "name": "Continuity and Change", "description": "Patterns of persistence and transformation over time"},
        {"slug": "conflict_and_cooperation", "name": "Conflict and Cooperation", "description": "Opposition and alliance dynamics between actors"},
        {"slug": "spatial_analysis", "name": "Spatial Analysis", "description": "Geographic and spatial dimensions of historical events"},
        {"slug": "intellectual_history", "name": "Intellectual History", "description": "Development and transmission of ideas and texts"},
        {"slug": "political_analysis", "name": "Political Analysis", "description": "Power structures, governance, and political dynamics"},
        {"slug": "historical_context", "name": "Historical Context", "description": "General historical situating and background"},
    ]
    
    created = 0
    for fw in frameworks:
        result = session.run("""
            MERGE (f:Framework {slug: $slug})
            ON CREATE SET f.name = $name, f.description = $description, f.created_at = datetime()
            RETURN count(f) as created
        """, **fw)
        record = result.single()
        if record and record["created"] > 0:
            created += 1
    
    return created


def ensure_place_nodes(session, place_slugs: List[str]) -> int:
    """Ensure Place nodes exist for OCCURS_IN edges."""
    # Basic place definitions
    place_defs = {
        "England": {"name": "England", "description": "Kingdom of England"},
        "London": {"name": "London", "description": "Capital city of England"},
        "Westminster": {"name": "Westminster", "description": "Political center of England"},
        "Oxford": {"name": "Oxford", "description": "University city in England"},
        "Canterbury": {"name": "Canterbury", "description": "Seat of the Archbishop of Canterbury"},
        "Northern_England": {"name": "Northern England", "description": "Northern regions of England"},
        "Cornwall": {"name": "Cornwall", "description": "County in southwest England"},
        "Norfolk": {"name": "Norfolk", "description": "County in East Anglia"},
        "Kent": {"name": "Kent", "description": "County in southeast England"},
    }
    
    created = 0
    for slug in place_slugs:
        place = place_defs.get(slug, {"name": slug.replace("_", " "), "description": f"Place: {slug}"})
        result = session.run("""
            MERGE (p:Place {slug: $slug})
            ON CREATE SET p.name = $name, p.description = $description, p.created_at = datetime()
            RETURN count(p) as created
        """, slug=slug, **place)
        record = result.single()
        if record and record["created"] > 0:
            created += 1
    
    return created


def process_cluster(cluster_name: str, edge_types: List[str] = None):
    """Process a cluster's edge arrays."""
    base_path = Path(__file__).parent.parent
    rels_path = base_path / "data" / "Relationships" / f"relationships.{cluster_name}.json"
    
    if not rels_path.exists():
        print(f"Error: Relationships file not found: {rels_path}")
        return
    
    # Load data
    with open(rels_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    driver = get_driver()
    
    try:
        with driver.session() as session:
            print(f"Processing cluster: {cluster_name}")
            print("=" * 50)
            
            # Ensure Framework nodes exist
            if not edge_types or "framed_by" in edge_types:
                fw_created = ensure_framework_nodes(session)
                print(f"Framework nodes created/verified: {fw_created}")
            
            # Ensure Place nodes exist
            place_edges = data.get("place_edges", [])
            if place_edges and (not edge_types or "place" in edge_types):
                place_slugs = list(set(pe.get("place_slug") for pe in place_edges if pe.get("place_slug")))
                place_created = ensure_place_nodes(session, place_slugs)
                print(f"Place nodes created/verified: {place_created}")
            
            # Ingest timeframe edges
            if not edge_types or "timeframe" in edge_types:
                tf_edges = data.get("timeframe_edges", [])
                tf_created = ingest_timeframe_edges(session, tf_edges)
                print(f"Timeframe edges (OCCURS_DURING): {tf_created} created (total in file: {len(tf_edges)})")
            
            # Ingest framed_by edges
            if not edge_types or "framed_by" in edge_types:
                fb_edges = data.get("framed_by_edges", [])
                relationships = data.get("relationships", [])
                fb_created = ingest_framed_by_edges(session, fb_edges, relationships)
                print(f"FRAMED_BY edges: {fb_created} created (total in file: {len(fb_edges)})")
            
            # Ingest place edges
            if not edge_types or "place" in edge_types:
                pl_edges = data.get("place_edges", [])
                pl_created = ingest_place_edges(session, pl_edges)
                print(f"Place edges (OCCURS_IN): {pl_created} created (total in file: {len(pl_edges)})")
    
    finally:
        driver.close()


def list_clusters() -> List[str]:
    """List all available clusters."""
    base_path = Path(__file__).parent.parent / "data" / "Relationships"
    clusters = []
    for f in base_path.glob("relationships.*.json"):
        cluster = f.stem.replace("relationships.", "")
        clusters.append(cluster)
    return sorted(clusters)


def main():
    parser = argparse.ArgumentParser(
        description="Ingest edge arrays from relationship JSON files into Neo4j."
    )
    parser.add_argument("cluster", nargs="?", help="Cluster name (e.g., English_Reformation)")
    parser.add_argument("--all", action="store_true", help="Process all clusters")
    parser.add_argument("--edge-type", choices=["timeframe", "framed_by", "place"],
                       action="append", dest="edge_types",
                       help="Only process specific edge types (can be repeated)")
    parser.add_argument("--list", action="store_true", help="List available clusters")
    
    args = parser.parse_args()
    
    if args.list:
        clusters = list_clusters()
        print("Available clusters:")
        for c in clusters:
            print(f"  {c}")
        return
    
    if args.all:
        clusters = list_clusters()
        for cluster in clusters:
            process_cluster(cluster, args.edge_types)
            print()
    elif args.cluster:
        process_cluster(args.cluster, args.edge_types)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
