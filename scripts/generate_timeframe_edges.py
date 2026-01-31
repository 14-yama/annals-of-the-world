#!/usr/bin/env python3
"""
Generate timeframe_edges for relationship cluster files.

This script reads relationship JSON files from data/Relationships/ and generates
OCCURS_DURING edges linking all unique node slugs to their appropriate Timeframe node.

Usage:
    python scripts/generate_timeframe_edges.py                    # Process all clusters
    python scripts/generate_timeframe_edges.py English_Reformation  # Process single cluster
    python scripts/generate_timeframe_edges.py --dry-run          # Preview without writing
    python scripts/generate_timeframe_edges.py --ingest           # Also ingest to Neo4j

Timeframe Divisions (Class 9):
    910 - Prehistoric (before -3000)
    920 - Classical (-3000 to 70)
    930 - Medieval (70 to 1500)
    940 - Early Modern (1500 to 1800)
    950 - Modern (1800 to 1945)
    960 - Contemporary (1945 to present)
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# Cluster-to-Timeframe mapping
# Maps cluster names to their primary timeframe division
CLUSTER_TIMEFRAME_MAP = {
    # Reformation clusters (1500-1800 = Early Modern = 940)
    "English_Reformation": 940,
    "German_Reformation": 940,
    "French_Reformation": 940,
    "Swiss_Reformation": 940,
    "Scottish_Reformation": 940,
    "Dutch_Reformation": 940,
    "Scandinavian_Reformations": 940,
    "Polish_Lithuanian_Reformation": 940,
    "Bohemian_Moravian_Reformation": 940,
    "Radical_Reformation": 940,
    "Catholic_Reformation": 940,
    "European_Reformations": 940,
    "Reformations": 940,
    
    # Hebrew/Biblical clusters (spans multiple periods)
    "Hebrew_Tradition": 920,  # Classical (primary), but spans 910-960
    "hebrew_tradition": 920,
    
    # Early Christianity (Classical/Medieval transition)
    "Early_Christianity": 920,  # Classical period primarily
    
    # Jewish-Islamic Exchange (Medieval)
    "Jewish-Islamic_Exchange": 930,
}

# Timeframe node definitions
TIMEFRAMES = {
    910: {"slug": "910_Prehistoric", "name": "Prehistoric", "startYear": -10000000, "endYear": -3000},
    920: {"slug": "920_Classical", "name": "Classical", "startYear": -3000, "endYear": 70},
    930: {"slug": "930_Medieval", "name": "Medieval", "startYear": 70, "endYear": 1500},
    940: {"slug": "940_Early_Modern", "name": "Early Modern", "startYear": 1500, "endYear": 1800},
    950: {"slug": "950_Modern", "name": "Modern", "startYear": 1800, "endYear": 1945},
    960: {"slug": "960_Contemporary", "name": "Contemporary", "startYear": 1945, "endYear": 2100},
}

# Node slug overrides for specific timeframes (when node belongs to different era than cluster)
NODE_TIMEFRAME_OVERRIDES = {
    # Hebrew Tradition spans multiple eras
    "Adam": 910, "Eve": 910, "Noah": 910, "Abraham": 910, "Isaac": 910, "Jacob": 910, "Joseph": 910,
    "Moses": 920, "Joshua": 920, "David": 920, "Solomon": 920,
    "Maimonides": 930, "Rashi": 930,
    "Spinoza": 940,
    # Add more specific overrides as needed
}


def get_relationships_dir() -> Path:
    """Get the data/Relationships directory path."""
    script_dir = Path(__file__).parent
    return script_dir.parent / "data" / "Relationships"


def get_timeframe_for_node(node_slug: str, cluster_name: str) -> int:
    """
    Determine the timeframe division for a node.
    
    Priority:
    1. NODE_TIMEFRAME_OVERRIDES (specific node overrides)
    2. CLUSTER_TIMEFRAME_MAP (cluster default)
    3. Default to 940 (Early Modern) if unknown
    """
    # Check for specific node override
    if node_slug in NODE_TIMEFRAME_OVERRIDES:
        return NODE_TIMEFRAME_OVERRIDES[node_slug]
    
    # Use cluster default
    return CLUSTER_TIMEFRAME_MAP.get(cluster_name, 940)


def extract_unique_slugs(relationships: list) -> set:
    """Extract all unique node slugs from relationships."""
    slugs = set()
    for rel in relationships:
        if "start_slug" in rel and rel["start_slug"]:
            slugs.add(rel["start_slug"])
        if "end_slug" in rel and rel["end_slug"]:
            slugs.add(rel["end_slug"])
    return slugs


def generate_timeframe_edges(relationships: list, cluster_name: str) -> list:
    """
    Generate timeframe_edges array for a cluster.
    
    Returns list of dicts with node_slug, timeframe_slug, division.
    """
    slugs = extract_unique_slugs(relationships)
    edges = []
    
    for slug in sorted(slugs):
        division = get_timeframe_for_node(slug, cluster_name)
        timeframe_info = TIMEFRAMES[division]
        
        edges.append({
            "node_slug": slug,
            "timeframe_slug": timeframe_info["slug"],
            "division": division,
            "timeframe_name": timeframe_info["name"]
        })
    
    return edges


def process_cluster_file(filepath: Path, dry_run: bool = False) -> dict:
    """
    Process a single relationship JSON file and add timeframe_edges.
    
    Returns dict with stats about the processing.
    """
    stats = {
        "filepath": str(filepath),
        "cluster": None,
        "relationships_count": 0,
        "unique_slugs": 0,
        "timeframe_edges_generated": 0,
        "status": "success"
    }
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        stats["status"] = f"JSON parse error: {e}"
        return stats
    except Exception as e:
        stats["status"] = f"Read error: {e}"
        return stats
    
    # Get cluster name from _meta or filename
    cluster_name = None
    if "_meta" in data and "cluster" in data["_meta"]:
        cluster_name = data["_meta"]["cluster"]
    else:
        # Extract from filename: relationships.English_Reformation.json -> English_Reformation
        filename = filepath.stem
        if filename.startswith("relationships."):
            cluster_name = filename.replace("relationships.", "")
    
    stats["cluster"] = cluster_name
    
    if not cluster_name:
        stats["status"] = "Could not determine cluster name"
        return stats
    
    # Get relationships
    relationships = data.get("relationships", [])
    stats["relationships_count"] = len(relationships)
    
    if not relationships:
        stats["status"] = "No relationships found"
        return stats
    
    # Generate timeframe edges
    timeframe_edges = generate_timeframe_edges(relationships, cluster_name)
    stats["unique_slugs"] = len(timeframe_edges)
    stats["timeframe_edges_generated"] = len(timeframe_edges)
    
    if dry_run:
        stats["status"] = "dry-run (not written)"
        return stats
    
    # Update the data with timeframe_edges
    data["timeframe_edges"] = timeframe_edges
    
    # Update _meta
    if "_meta" not in data:
        data["_meta"] = {}
    data["_meta"]["timeframe_edges_generated_at"] = datetime.now(timezone.utc).isoformat()
    data["_meta"]["timeframe_edges_generator"] = "scripts/generate_timeframe_edges.py"
    
    # Write back
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        stats["status"] = "success"
    except Exception as e:
        stats["status"] = f"Write error: {e}"
    
    return stats


def ingest_timeframe_edges_to_neo4j(filepath: Path) -> dict:
    """
    Ingest timeframe_edges from a file into Neo4j.
    
    Returns dict with ingestion stats.
    """
    stats = {
        "filepath": str(filepath),
        "edges_ingested": 0,
        "timeframes_created": 0,
        "status": "success"
    }
    
    # Try multiple import paths
    get_neo4j_driver = None
    try:
        from scripts.db import get_neo4j_driver
    except ImportError:
        pass
    
    if get_neo4j_driver is None:
        try:
            from db import get_neo4j_driver
        except ImportError:
            pass
    
    if get_neo4j_driver is None:
        try:
            # Direct import with path manipulation
            import importlib.util
            db_path = Path(__file__).parent / "db.py"
            spec = importlib.util.spec_from_file_location("db", db_path)
            db_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(db_module)
            get_neo4j_driver = db_module.get_neo4j_driver
        except Exception as e:
            stats["status"] = f"Could not import db module: {e}"
            return stats
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        stats["status"] = f"Read error: {e}"
        return stats
    
    timeframe_edges = data.get("timeframe_edges", [])
    if not timeframe_edges:
        stats["status"] = "No timeframe_edges to ingest"
        return stats
    
    # First ensure Timeframe nodes exist
    create_timeframes_cypher = """
    UNWIND $timeframes AS tf
    MERGE (t:Timeframe {slug: tf.slug})
    SET t.division = tf.division,
        t.name = tf.name,
        t.startYear = tf.startYear,
        t.endYear = tf.endYear
    RETURN count(t) AS timeframes_created
    """
    
    # Create OCCURS_DURING edges
    create_edges_cypher = """
    UNWIND $edges AS edge
    MATCH (n {slug: edge.node_slug})
    MATCH (t:Timeframe {slug: edge.timeframe_slug})
    MERGE (n)-[r:OCCURS_DURING]->(t)
    SET r.division = edge.division,
        r.created_at = datetime(),
        r.created_by = 'generate_timeframe_edges.py'
    RETURN count(r) AS edges_created
    """
    
    try:
        driver = get_neo4j_driver()
        with driver.session() as session:
            # Create Timeframe nodes
            timeframes_list = [
                {"slug": tf["slug"], "division": div, "name": tf["name"], 
                 "startYear": tf["startYear"], "endYear": tf["endYear"]}
                for div, tf in TIMEFRAMES.items()
            ]
            result = session.run(create_timeframes_cypher, timeframes=timeframes_list)
            record = result.single()
            stats["timeframes_created"] = record["timeframes_created"] if record else 0
            
            # Create edges
            result = session.run(create_edges_cypher, edges=timeframe_edges)
            record = result.single()
            stats["edges_ingested"] = record["edges_created"] if record else 0
            
        driver.close()
            
    except Exception as e:
        stats["status"] = f"Neo4j error: {e}"
    
    return stats


def main():
    parser = argparse.ArgumentParser(
        description="Generate timeframe_edges for relationship cluster files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        "cluster",
        nargs="?",
        help="Cluster name to process (e.g., English_Reformation). If omitted, processes all clusters."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without writing to files."
    )
    parser.add_argument(
        "--ingest",
        action="store_true",
        help="Also ingest timeframe_edges to Neo4j after generating."
    )
    parser.add_argument(
        "--list-clusters",
        action="store_true",
        help="List all available cluster files and exit."
    )
    
    args = parser.parse_args()
    
    rel_dir = get_relationships_dir()
    
    if not rel_dir.exists():
        print(f"Error: Relationships directory not found: {rel_dir}")
        sys.exit(1)
    
    # Find all relationship files
    rel_files = list(rel_dir.glob("relationships.*.json"))
    
    if args.list_clusters:
        print("Available cluster files:")
        for f in sorted(rel_files):
            cluster = f.stem.replace("relationships.", "")
            division = CLUSTER_TIMEFRAME_MAP.get(cluster, "unknown")
            print(f"  {cluster} -> division {division}")
        sys.exit(0)
    
    # Filter to specific cluster if provided
    if args.cluster:
        target_filename = f"relationships.{args.cluster}.json"
        rel_files = [f for f in rel_files if f.name == target_filename]
        if not rel_files:
            print(f"Error: Cluster file not found: {target_filename}")
            print(f"Available files in {rel_dir}:")
            for f in sorted(rel_dir.glob("relationships.*.json")):
                print(f"  {f.name}")
            sys.exit(1)
    
    # Process files
    print(f"{'[DRY RUN] ' if args.dry_run else ''}Processing {len(rel_files)} cluster file(s)...\n")
    
    all_stats = []
    for filepath in sorted(rel_files):
        print(f"Processing: {filepath.name}")
        stats = process_cluster_file(filepath, dry_run=args.dry_run)
        all_stats.append(stats)
        
        print(f"  Cluster: {stats['cluster']}")
        print(f"  Relationships: {stats['relationships_count']}")
        print(f"  Unique slugs: {stats['unique_slugs']}")
        print(f"  Timeframe edges: {stats['timeframe_edges_generated']}")
        print(f"  Status: {stats['status']}")
        
        # Ingest to Neo4j if requested
        if args.ingest and stats['status'] == 'success' and not args.dry_run:
            print("  Ingesting to Neo4j...")
            ingest_stats = ingest_timeframe_edges_to_neo4j(filepath)
            print(f"  Neo4j edges created: {ingest_stats['edges_ingested']}")
            print(f"  Neo4j status: {ingest_stats['status']}")
        
        print()
    
    # Summary
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    total_edges = sum(s["timeframe_edges_generated"] for s in all_stats)
    successful = sum(1 for s in all_stats if s["status"] == "success" or "dry-run" in s["status"])
    print(f"Files processed: {len(all_stats)}")
    print(f"Successful: {successful}")
    print(f"Total timeframe edges generated: {total_edges}")
    
    if args.dry_run:
        print("\n[DRY RUN] No files were modified. Run without --dry-run to apply changes.")


if __name__ == "__main__":
    main()
