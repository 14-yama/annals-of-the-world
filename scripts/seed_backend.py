#!/usr/bin/env python3
"""
Unified Backend Seeding Pipeline

This is the single entry point for seeding the Neo4j backend. It runs all
necessary setup steps in the correct sequence:

1. Setup constraints and indexes (setup_constraints.py)
2. Seed geo registry (continents, regions, countries) from geo_registry.py
3. Seed place registry (countries/cities/name variants) from geo-registry/places.json
4. Seed cluster data (nodes, relationships, edge arrays)
5. Link cluster places to geo hierarchy
6. Run post-seed validation

Usage:
    # Full production seed (English_Reformation only for now)
    python scripts/seed_backend.py

    # Dry-run mode
    python scripts/seed_backend.py --dry-run

    # Seed specific clusters (when ready)
    python scripts/seed_backend.py --clusters English_Reformation German_Reformation

    # Skip geo registry (if already seeded)
    python scripts/seed_backend.py --skip-geo

    # Skip constraints (if already applied)
    python scripts/seed_backend.py --skip-constraints

Author: Annals Project
Created: 2026-01-24
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Sequence

# Ensure project root is in path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

try:
    from dotenv import load_dotenv
    load_dotenv(ROOT / ".env.local")
except ImportError:
    pass

try:
    from neo4j import GraphDatabase
except ImportError:
    GraphDatabase = None

# ============================================================================
# Configuration
# ============================================================================

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "neo4j")

# Production-ready clusters (others need curation work first)
PRODUCTION_CLUSTERS = ["English_Reformation"]

NODES_DIR = ROOT / "data" / "Nodes"
RELS_DIR = ROOT / "data" / "Relationships"


# ============================================================================
# Step 1: Constraints and Indexes
# ============================================================================

CONSTRAINTS = [
    # Core node constraints
    "CREATE CONSTRAINT idea_name_unique IF NOT EXISTS FOR (i:Idea) REQUIRE i.name IS UNIQUE",
    "CREATE CONSTRAINT idea_slug_unique IF NOT EXISTS FOR (i:Idea) REQUIRE i.slug IS UNIQUE",
    "CREATE INDEX idea_category_index IF NOT EXISTS FOR (i:Idea) ON (i.category)",
    "CREATE INDEX idea_status_index IF NOT EXISTS FOR (i:Idea) ON (i.status)",

    "CREATE CONSTRAINT person_name_unique IF NOT EXISTS FOR (p:Person) REQUIRE p.name IS UNIQUE",
    "CREATE CONSTRAINT person_slug_unique IF NOT EXISTS FOR (p:Person) REQUIRE p.slug IS UNIQUE",
    "CREATE INDEX person_category_index IF NOT EXISTS FOR (p:Person) ON (p.category)",
    "CREATE INDEX person_status_index IF NOT EXISTS FOR (p:Person) ON (p.status)",

    "CREATE CONSTRAINT event_name_unique IF NOT EXISTS FOR (e:Event) REQUIRE e.name IS UNIQUE",
    "CREATE CONSTRAINT event_slug_unique IF NOT EXISTS FOR (e:Event) REQUIRE e.slug IS UNIQUE",
    "CREATE INDEX event_category_index IF NOT EXISTS FOR (e:Event) ON (e.category)",
    "CREATE INDEX event_status_index IF NOT EXISTS FOR (e:Event) ON (e.status)",
    "CREATE INDEX event_kind_index IF NOT EXISTS FOR (e:Event) ON (e.kind)",

    "CREATE CONSTRAINT place_slug_unique IF NOT EXISTS FOR (pl:Place) REQUIRE pl.slug IS UNIQUE",
    "CREATE INDEX place_name_index IF NOT EXISTS FOR (pl:Place) ON (pl.name)",
    "CREATE INDEX place_category_index IF NOT EXISTS FOR (pl:Place) ON (pl.category)",
    "CREATE INDEX place_status_index IF NOT EXISTS FOR (pl:Place) ON (pl.status)",
    "CREATE INDEX place_region_index IF NOT EXISTS FOR (pl:Place) ON (pl.region)",

    # PlaceName nodes (name variant registry)
    "CREATE CONSTRAINT place_name_slug_unique IF NOT EXISTS FOR (pn:PlaceName) REQUIRE pn.slug IS UNIQUE",
    "CREATE INDEX place_name_name_index IF NOT EXISTS FOR (pn:PlaceName) ON (pn.name)",
    "CREATE INDEX place_name_lang_index IF NOT EXISTS FOR (pn:PlaceName) ON (pn.lang)",

    "CREATE CONSTRAINT institution_name_unique IF NOT EXISTS FOR (inst:Institution) REQUIRE inst.name IS UNIQUE",
    "CREATE CONSTRAINT institution_slug_unique IF NOT EXISTS FOR (inst:Institution) REQUIRE inst.slug IS UNIQUE",
    "CREATE INDEX institution_category_index IF NOT EXISTS FOR (inst:Institution) ON (inst.category)",
    "CREATE INDEX institution_status_index IF NOT EXISTS FOR (inst:Institution) ON (inst.status)",

    "CREATE CONSTRAINT movement_name_unique IF NOT EXISTS FOR (m:Movement) REQUIRE m.name IS UNIQUE",
    "CREATE CONSTRAINT movement_slug_unique IF NOT EXISTS FOR (m:Movement) REQUIRE m.slug IS UNIQUE",
    "CREATE INDEX movement_category_index IF NOT EXISTS FOR (m:Movement) ON (m.category)",
    "CREATE INDEX movement_status_index IF NOT EXISTS FOR (m:Movement) ON (m.status)",

    "CREATE CONSTRAINT artifact_name_unique IF NOT EXISTS FOR (a:Artifact) REQUIRE a.name IS UNIQUE",
    "CREATE CONSTRAINT artifact_slug_unique IF NOT EXISTS FOR (a:Artifact) REQUIRE a.slug IS UNIQUE",
    "CREATE INDEX artifact_category_index IF NOT EXISTS FOR (a:Artifact) ON (a.category)",
    "CREATE INDEX artifact_status_index IF NOT EXISTS FOR (a:Artifact) ON (a.status)",

    # Lookup node constraints
    "CREATE CONSTRAINT timeframe_slug_unique IF NOT EXISTS FOR (t:Timeframe) REQUIRE t.slug IS UNIQUE",
    "CREATE CONSTRAINT timeframe_division_unique IF NOT EXISTS FOR (t:Timeframe) REQUIRE t.division IS UNIQUE",
    "CREATE INDEX timeframe_name_index IF NOT EXISTS FOR (t:Timeframe) ON (t.name)",

    "CREATE CONSTRAINT framework_slug_unique IF NOT EXISTS FOR (f:Framework) REQUIRE f.slug IS UNIQUE",

    # Relationship property constraints (FRAMED_BY)
    "CREATE CONSTRAINT framed_by_citation_required IF NOT EXISTS FOR ()-[r:FRAMED_BY]-() REQUIRE r.citation_style IS NOT NULL",
    "CREATE CONSTRAINT framed_by_evidence_url_required IF NOT EXISTS FOR ()-[r:FRAMED_BY]-() REQUIRE r.evidence_url IS NOT NULL",
    "CREATE CONSTRAINT framed_by_page_refs_required IF NOT EXISTS FOR ()-[r:FRAMED_BY]-() REQUIRE r.page_refs IS NOT NULL",
    "CREATE CONSTRAINT framed_by_source_note_required IF NOT EXISTS FOR ()-[r:FRAMED_BY]-() REQUIRE r.source_note IS NOT NULL",
]


def step_1_setup_constraints(session, dry_run: bool = False) -> int:
    """Apply all constraints and indexes."""
    print("\n" + "=" * 60)
    print("STEP 1: Setting up constraints and indexes")
    print("=" * 60)

    applied = 0
    for stmt in CONSTRAINTS:
        if dry_run:
            print(f"  [dry-run] Would apply: {stmt[:60]}...")
            applied += 1
        else:
            try:
                session.run(stmt)
                print(f"  ✓ {stmt[:60]}...")
                applied += 1
            except Exception as e:
                print(f"  ✗ Failed: {stmt[:60]}... ({e})")

    print(f"\nConstraints/indexes applied: {applied}")
    return applied


# ============================================================================
# Step 2: Geo Registry
# ============================================================================

# Import geo data from geo_registry.py
from geo_registry import CONTINENTS, HIER, slugify

GEO_UPSERT = """
MERGE (p:Place {slug: $slug})
ON CREATE SET
  p.name=$name, p.kind=$kind, p.region=$region, p.category='Place',
  p.is_generic=true, p.class_number=4,
  p.division_code=$division_code,
  p.status='PROPOSED', p.intl_status=$intl_status,
  p.created_at=$ts, p.updated_at=$ts,
  p.created_by='seed_backend.py', p.version=1
ON MATCH SET
  p.name=coalesce($name,p.name),
  p.region=coalesce($region,p.region),
  p.updated_at=$ts
RETURN p.slug AS slug
"""

GEO_CONTAINS = """
MATCH (a:Place {slug:$a}), (b:Place {slug:$b})
MERGE (a)-[:CONTAINS]->(b)
"""


def step_2_seed_geo_registry(session, dry_run: bool = False) -> Dict[str, int]:
    """Seed continents, regions, and countries."""
    print("\n" + "=" * 60)
    print("STEP 2: Seeding geo registry (continents, regions, countries)")
    print("=" * 60)

    stats = {"continents": 0, "regions": 0, "countries": 0}
    now = datetime.now(timezone.utc).isoformat(timespec="seconds") + "Z"

    if dry_run:
        stats["continents"] = len(CONTINENTS)
        stats["regions"] = sum(len(regions) for regions in HIER.values())
        stats["countries"] = sum(
            len(countries)
            for regions in HIER.values()
            for countries in regions.values()
        )
        print(f"  [dry-run] Would seed: {stats}")
        return stats

    # Seed continents
    for cont in CONTINENTS:
        slug = slugify(cont)
        session.run(GEO_UPSERT, slug=slug, name=cont, kind="region", region=cont,
                    division_code="400", intl_status="ALIGNED", ts=now)
        stats["continents"] += 1

    # Seed regions and countries
    for continent, regions in HIER.items():
        cont_slug = slugify(continent)
        for rname, countries in regions.items():
            rslug = slugify(rname)
            session.run(GEO_UPSERT, slug=rslug, name=rname, kind="region", region=continent,
                        division_code="410", intl_status="ALIGNED", ts=now)
            session.run(GEO_CONTAINS, a=cont_slug, b=rslug)
            stats["regions"] += 1

            for cname in countries:
                pslug = slugify(cname)
                session.run(GEO_UPSERT, slug=pslug, name=cname, kind="country", region=continent,
                            division_code="430", intl_status="NEEDS_REVIEW", ts=now)
                session.run(GEO_CONTAINS, a=rslug, b=pslug)
                stats["countries"] += 1

    print(f"  ✓ Continents: {stats['continents']}")
    print(f"  ✓ Regions: {stats['regions']}")
    print(f"  ✓ Countries: {stats['countries']}")
    return stats


def _load_seed_places_json_module():
    """Load geo-registry/scripts/seed_places_json.py as a module.

    The directory name contains a hyphen, so we can't import it as a normal package.
    """
    module_path = ROOT / "geo-registry" / "scripts" / "seed_places_json.py"
    spec = importlib.util.spec_from_file_location("seed_places_json", module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module from {module_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def step_2_seed_places_json(session, dry_run: bool = False) -> Dict[str, int]:
    """Seed Place nodes for countries/cities + PlaceName variants from geo-registry/places.json."""
    print("\n" + "=" * 60)
    print("STEP 2B: Seeding geo-registry/places.json (cities + name variants)")
    print("=" * 60)

    mod = _load_seed_places_json_module()
    places = mod.load_places()

    total_cities = sum(len(c.get("cities", {})) for c in places.values())
    total_extinct = sum(len(c.get("extinct_places", {})) for c in places.values())
    stats = {"countries": len(places), "cities": total_cities, "extinct": total_extinct}

    if dry_run:
        print(f"  [dry-run] Would seed from places.json: {stats}")
        return stats

    seeded = mod.seed_all(session, places)
    print(f"  ✓ Seeded from places.json: {seeded}")
    return seeded


# ============================================================================
# Step 3: Cluster Data (Nodes, Relationships, Edge Arrays)
# ============================================================================

def load_json(path: Path) -> Dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sanitize_label(value: Optional[str]) -> str:
    return (value or "Idea").strip().replace(" ", "_")


def step_3_seed_cluster_data(session, clusters: List[str], dry_run: bool = False) -> Dict[str, int]:
    """Seed nodes, relationships, and edge arrays for specified clusters."""
    print("\n" + "=" * 60)
    print("STEP 3: Seeding cluster data")
    print("=" * 60)

    stats = {"nodes": 0, "relationships": 0, "timeframe_edges": 0, "framed_by_edges": 0, "place_edges": 0}

    for cluster in clusters:
        print(f"\n  Processing: {cluster}")

        nodes_path = NODES_DIR / f"nodes.{cluster}.json"
        rels_path = RELS_DIR / f"relationships.{cluster}.json"

        # Load and seed nodes
        if nodes_path.exists():
            nodes_data = load_json(nodes_path)
            nodes = nodes_data.get("nodes", nodes_data) if isinstance(nodes_data, dict) else nodes_data
            if isinstance(nodes, list):
                for node in nodes:
                    slug = node.get("slug")
                    if not slug:
                        continue
                    label = sanitize_label(node.get("label") or node.get("type"))
                    props = {k: v for k, v in node.items() if k not in {"id", "label", "type"}}

                    if dry_run:
                        stats["nodes"] += 1
                    else:
                        cypher = f"MERGE (n:`{label}` {{slug: $slug}}) SET n += $props"
                        session.run(cypher, slug=slug, props=props)
                        stats["nodes"] += 1

                print(f"    ✓ Nodes: {len(nodes)}")
        else:
            print(f"    ⚠ No nodes file found")

        # Load and seed relationships + edge arrays
        if rels_path.exists():
            rels_data = load_json(rels_path)
            relationships = rels_data.get("relationships", [])

            # Seed relationships
            for rel in relationships:
                start_slug = rel.get("start_slug")
                end_slug = rel.get("end_slug")
                rel_type = (rel.get("type") or "RELATED_TO").upper().replace("-", "_").replace(" ", "_")
                if not start_slug or not end_slug:
                    continue
                props = {k: v for k, v in rel.items() if k not in {"id", "start_slug", "end_slug", "type"}}

                if dry_run:
                    stats["relationships"] += 1
                else:
                    cypher = (
                        f"MATCH (start {{slug: $start_slug}}) "
                        f"MATCH (end {{slug: $end_slug}}) "
                        f"MERGE (start)-[rel:`{rel_type}`]->(end) "
                        f"SET rel += $props"
                    )
                    session.run(cypher, start_slug=start_slug, end_slug=end_slug, props=props)
                    stats["relationships"] += 1

            print(f"    ✓ Relationships: {len(relationships)}")

            # Seed timeframe edges
            tf_edges = rels_data.get("timeframe_edges", [])
            if tf_edges:
                stats["timeframe_edges"] += _seed_timeframe_edges(session, tf_edges, dry_run)
                print(f"    ✓ Timeframe edges: {len(tf_edges)}")

            # Seed framed_by edges
            fb_edges = rels_data.get("framed_by_edges", [])
            if fb_edges:
                stats["framed_by_edges"] += _seed_framed_by_edges(session, fb_edges, relationships, dry_run)
                print(f"    ✓ FRAMED_BY edges: {len(fb_edges)}")

            # Seed place edges
            pl_edges = rels_data.get("place_edges", [])
            if pl_edges:
                stats["place_edges"] += _seed_place_edges(session, pl_edges, dry_run)
                print(f"    ✓ Place edges: {len(pl_edges)}")
        else:
            print(f"    ⚠ No relationships file found")

    return stats


def _seed_timeframe_edges(session, edges: List[Dict], dry_run: bool) -> int:
    """Seed OCCURS_DURING edges to Timeframe nodes."""
    if dry_run:
        return len(edges)

    # Ensure Timeframe nodes exist
    timeframes = {}
    for edge in edges:
        tf_slug = edge.get("timeframe_slug")
        division = edge.get("division")
        tf_name = edge.get("timeframe_name")
        if tf_slug:
            timeframes[tf_slug] = {"slug": tf_slug, "division": division, "name": tf_name}

    if timeframes:
        session.run("""
            UNWIND $timeframes AS tf
            MERGE (t:Timeframe {slug: tf.slug})
            ON CREATE SET t.created_at = datetime()
            SET t.division = coalesce(tf.division, t.division),
                t.name = coalesce(tf.name, t.name)
        """, timeframes=list(timeframes.values()))

    # Create edges
    normalized = [
        {"node_slug": e["node_slug"], "tf_slug": e.get("timeframe_slug"), "division": e.get("division")}
        for e in edges if e.get("node_slug")
    ]

    result = session.run("""
        UNWIND $edges AS edge
        MATCH (n {slug: edge.node_slug})
        MATCH (t:Timeframe {slug: edge.tf_slug})
        MERGE (n)-[r:OCCURS_DURING]->(t)
        ON CREATE SET r.created_at = datetime()
        SET r.division = coalesce(edge.division, r.division)
        RETURN count(r) AS merged
    """, edges=normalized)

    record = result.single()
    return int(record["merged"]) if record else 0


def _seed_framed_by_edges(session, framed_by_edges: List[Dict], relationships: List[Dict], dry_run: bool) -> int:
    """Seed FRAMED_BY edges to Framework nodes."""
    if dry_run:
        return len(framed_by_edges)

    # Ensure Framework nodes exist
    frameworks = [
        {"slug": "cause_and_effect", "name": "Cause and Effect"},
        {"slug": "cultural_diffusion", "name": "Cultural Diffusion"},
        {"slug": "continuity_and_change", "name": "Continuity and Change"},
        {"slug": "conflict_and_cooperation", "name": "Conflict and Cooperation"},
        {"slug": "spatial_analysis", "name": "Spatial Analysis"},
        {"slug": "intellectual_history", "name": "Intellectual History"},
        {"slug": "political_analysis", "name": "Political Analysis"},
        {"slug": "historical_context", "name": "Historical Context"},
    ]

    session.run("""
        UNWIND $frameworks AS fw
        MERGE (f:Framework {slug: fw.slug})
        ON CREATE SET f.created_at = datetime()
        SET f.name = coalesce(fw.name, f.name)
    """, frameworks=frameworks)

    # Build lookup
    rel_lookup = {rel.get("id"): rel for rel in relationships if rel.get("id") is not None}

    rows = []
    for edge in framed_by_edges:
        rel_id = edge.get("relationship_id")
        framework_slug = edge.get("framework_slug")
        if rel_id is None or not framework_slug:
            continue
        rel = rel_lookup.get(rel_id)
        if not rel:
            continue

        start_slug = rel.get("start_slug")
        end_slug = rel.get("end_slug")
        if not start_slug or not end_slug:
            continue

        evidence_url = rel.get("evidence_url")
        if not evidence_url:
            evidence_slug = rel.get("evidence_slug")
            evidence_url = f"data/Evidence/{evidence_slug}.json" if evidence_slug else "data/Evidence/UNKNOWN.json"

        rows.append({
            "start_slug": start_slug,
            "end_slug": end_slug,
            "framework_slug": framework_slug,
            "relationship_id": rel_id,
            "citation_style": rel.get("citation_style") or "Chicago 17",
            "evidence_url": evidence_url,
            "page_refs": rel.get("page_refs") or "passim",
            "source_note": f"Framing relationship between {start_slug} and {end_slug}",
        })

    if not rows:
        return 0

    result = session.run("""
        UNWIND $rows AS row
        MATCH (n {slug: row.start_slug})
        MATCH (f:Framework {slug: row.framework_slug})
        MERGE (n)-[r:FRAMED_BY {context_end: row.end_slug, relationship_id: row.relationship_id}]->(f)
        ON CREATE SET r.created_at = datetime()
        SET r.citation_style = row.citation_style,
            r.evidence_url = row.evidence_url,
            r.page_refs = row.page_refs,
            r.source_note = row.source_note
        RETURN count(r) AS merged
    """, rows=rows)

    record = result.single()
    return int(record["merged"]) if record else 0


def _seed_place_edges(session, edges: List[Dict], dry_run: bool) -> int:
    """Seed OCCURS_IN edges to Place nodes."""
    if dry_run:
        return len(edges)

    normalized = [
        {"node_slug": e["node_slug"], "place_slug": e["place_slug"]}
        for e in edges if e.get("node_slug") and e.get("place_slug")
    ]

    result = session.run("""
        UNWIND $edges AS edge
        MATCH (n {slug: edge.node_slug})
        MATCH (p:Place {slug: edge.place_slug})
        MERGE (n)-[r:OCCURS_IN]->(p)
        ON CREATE SET r.created_at = datetime()
        RETURN count(r) AS merged
    """, edges=normalized)

    record = result.single()
    return int(record["merged"]) if record else 0


# ============================================================================
# Step 4: Link Cluster Places to Geo Hierarchy
# ============================================================================

# UK subnational places from English_Reformation
UK_SUBNATIONAL = [
    ("England", "country-part", "The Kingdom of England"),
    ("Westminster", "city", "Political center of England"),
    ("London", "city", "Capital city of England"),
    ("Oxford", "city", "University city in England"),
    ("Canterbury", "city", "Seat of the Archbishop of Canterbury"),
    ("Northern_England", "region", "Northern regions of England"),
    ("Cornwall", "county", "County in southwest England"),
    ("Norfolk", "county", "County in East Anglia"),
    ("Kent", "county", "County in southeast England"),
]


def step_4_link_places_to_geo(session, dry_run: bool = False) -> int:
    """Link cluster places to the geo hierarchy."""
    print("\n" + "=" * 60)
    print("STEP 4: Linking cluster places to geo hierarchy")
    print("=" * 60)

    if dry_run:
        print(f"  [dry-run] Would link {len(UK_SUBNATIONAL)} UK subnational places")
        return len(UK_SUBNATIONAL)

    now = datetime.now(timezone.utc).isoformat(timespec="seconds") + "Z"
    linked = 0

    for pname, kind, desc in UK_SUBNATIONAL:
        slug = pname  # Keep original slug format
        # Update existing place and link to UK
        session.run("""
            MATCH (p:Place {slug: $slug})
            SET p.kind = $kind, p.region = 'Europe', p.updated_at = $ts
        """, slug=slug, kind=kind, ts=now)

        session.run("""
            MATCH (uk:Place {slug: 'united-kingdom'}), (p:Place {slug: $slug})
            MERGE (uk)-[:CONTAINS]->(p)
        """, slug=slug)

        print(f"    ✓ Linked {slug} -> united-kingdom")
        linked += 1

    return linked


# ============================================================================
# Step 5: Post-Seed Validation
# ============================================================================

def step_5_validate(session, dry_run: bool = False) -> Dict[str, int]:
    """Run post-seed validation queries."""
    print("\n" + "=" * 60)
    print("STEP 5: Post-seed validation")
    print("=" * 60)

    if dry_run:
        print("  [dry-run] Skipping validation")
        return {}

    validation = {}

    # Count nodes by label
    result = session.run("""
        MATCH (n)
        WITH labels(n)[0] AS label, count(*) AS cnt
        RETURN label, cnt ORDER BY cnt DESC
    """)
    print("\n  Node counts by label:")
    for r in result:
        print(f"    {r['label']}: {r['cnt']}")
        validation[f"nodes_{r['label']}"] = r["cnt"]

    # Events without kind
    result = session.run("MATCH (e:Event) WHERE e.kind IS NULL RETURN count(e) AS n").single()
    validation["events_missing_kind"] = result["n"]
    print(f"\n  Events missing kind: {result['n']}")

    # Events without OCCURS_DURING
    result = session.run("MATCH (e:Event) WHERE NOT (e)-[:OCCURS_DURING]->(:Timeframe) RETURN count(e) AS n").single()
    validation["events_missing_timeframe"] = result["n"]
    print(f"  Events missing OCCURS_DURING: {result['n']}")

    # Events without OCCURS_IN
    result = session.run("MATCH (e:Event) WHERE NOT (e)-[:OCCURS_IN]->(:Place) RETURN count(e) AS n").single()
    validation["events_missing_place"] = result["n"]
    print(f"  Events missing OCCURS_IN: {result['n']}")

    # Marriage event sanity check
    result = session.run("MATCH (e:Event {kind:'Marriage'}) RETURN count(e) AS n").single()
    validation["marriage_events"] = result["n"]
    result2 = session.run("MATCH (:Person)-[r:PARTICIPATES_IN {role:'spouse'}]->(:Event {kind:'Marriage'}) RETURN count(r) AS n").single()
    validation["spouse_participations"] = result2["n"]
    print(f"  Marriage events: {result['n']}, spouse participations: {result2['n']}")

    # Geo hierarchy check
    result = session.run("""
        MATCH (continent:Place)-[:CONTAINS*1..4]->(place:Place)<-[:OCCURS_IN]-(e:Event)
        WHERE NOT (:Place)-[:CONTAINS]->(continent)
        RETURN continent.slug AS continent, count(DISTINCT e) AS events
        ORDER BY events DESC LIMIT 5
    """)
    print("\n  Events by continent (top 5):")
    for r in result:
        print(f"    {r['continent']}: {r['events']}")

    return validation


# ============================================================================
# Main
# ============================================================================

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Unified backend seeding pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        "--clusters",
        nargs="+",
        default=PRODUCTION_CLUSTERS,
        help=f"Clusters to seed (default: {PRODUCTION_CLUSTERS})"
    )
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing to Neo4j")
    parser.add_argument("--skip-constraints", action="store_true", help="Skip constraint/index setup")
    parser.add_argument("--skip-geo", action="store_true", help="Skip geo registry seeding")
    parser.add_argument("--skip-places-json", action="store_true", help="Skip seeding geo-registry/places.json")
    parser.add_argument("--skip-link-places", action="store_true", help="Skip linking places to geo hierarchy")
    parser.add_argument("--skip-validation", action="store_true", help="Skip post-seed validation")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    print("=" * 60)
    print("ANNALS OF THE WORLD — Backend Seeding Pipeline")
    print("=" * 60)
    print(f"Clusters: {args.clusters}")
    print(f"Dry-run: {args.dry_run}")
    print(f"Started: {datetime.now(timezone.utc).isoformat()}")

    if GraphDatabase is None:
        print("\nERROR: neo4j package not installed")
        return 1

    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    try:
        with driver.session() as session:
            # Step 1: Constraints
            if not args.skip_constraints:
                step_1_setup_constraints(session, args.dry_run)

        # Steps 2-4 need separate sessions for schema vs data
        with driver.session() as session:
            # Step 2: Geo Registry
            if not args.skip_geo:
                step_2_seed_geo_registry(session, args.dry_run)

            # Step 2B: places.json (cities + name variants)
            if not args.skip_places_json:
                step_2_seed_places_json(session, args.dry_run)

            # Step 3: Cluster Data
            step_3_seed_cluster_data(session, args.clusters, args.dry_run)

            # Step 4: Link Places
            if not args.skip_link_places:
                step_4_link_places_to_geo(session, args.dry_run)

            # Step 5: Validation
            if not args.skip_validation:
                step_5_validate(session, args.dry_run)

    finally:
        driver.close()

    print("\n" + "=" * 60)
    print("Pipeline complete!")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())
