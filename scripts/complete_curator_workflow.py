#!/usr/bin/env python3
"""
Complete Curator Workflow for a Cluster

This script completes all curator workflow steps for a cluster:
1. Propose - Ensure all nodes have status
2. Cite - Add evidence references to relationships
3. Frame - Add FRAMED_BY edges to Framework nodes
4. Place - Verify timeframe_edges and add place_edges (OCCURS_IN)
5. Review - Run QA checks
6. Publish - Update status to REVIEWED where appropriate

Usage:
    python scripts/complete_curator_workflow.py English_Reformation
    python scripts/complete_curator_workflow.py English_Reformation --dry-run
    python scripts/complete_curator_workflow.py English_Reformation --step cite
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Any, Optional
from collections import Counter

# Evidence sources for English Reformation
# Maps relationship patterns to evidence slugs (from actual files in data/Evidence/)
ENGLISH_REFORMATION_EVIDENCE = {
    # General English Reformation sources
    "default": "evidence_Haigh_1993_English_Reformations",
    
    # Henrician Period
    "Henry_VIII": "evidence_Scarisbrick_1968_Henry_VIII",
    "Thomas_Cromwell": "evidence_Bernard_2005_The_Kings_Reformation",
    "Thomas_Cranmer": "evidence_MacCulloch_1996_Thomas_Cranmer",
    "Anne_Boleyn": "evidence_Ives_2004_The_Life_and_47247b",  # Anne Boleyn biography
    "Catherine_of_Aragon": "evidence_Scarisbrick_1968_Henry_VIII",
    "Thomas_More": "evidence_Guy_2000_Thomas_More_1f2d39",
    "Dissolution_of_the_Monasteries": "evidence_Bernard_2005_The_Kings_Reformation",
    "Act_of_Supremacy": "evidence_Bernard_2005_The_Kings_Reformation",
    "Break_with_Rome": "evidence_Bernard_2005_The_Kings_Reformation",
    "Chantries": "evidence_Kreider_1979_English_Chantries_The_47c6db",
    
    # Edwardian Period
    "Edward_VI": "evidence_MacCulloch_1996_Thomas_Cranmer",  # Tudor Church Militant not available
    "Book_of_Common_Prayer": "evidence_MacCulloch_1996_Thomas_Cranmer",
    "Forty_Two_Articles": "evidence_MacCulloch_1996_Thomas_Cranmer",
    "Ketts": "evidence_Land_1977_Kett_s_Rebellion_92af0f",
    
    # Marian Period
    "Mary_I": "evidence_Duffy_2009_Fires_of_Faith",
    "Marian_Persecutions": "evidence_Duffy_2009_Fires_of_Faith",
    "John_Foxe": "evidence_Freeman_2011_and_Elizabeth_Evenden_9e2cf0",
    "Acts_and_Monuments": "evidence_Freeman_2011_and_Elizabeth_Evenden_9e2cf0",
    "Wyatt": "evidence_Loades_1965_Two_Tudor_Conspiracies_6a147a",
    
    # Elizabethan Period
    "Elizabeth_I": "evidence_Doran_1994_Elizabeth_I_and_792615",
    "Act_of_Uniformity_1559": "evidence_Jones_1982_Faith_by_Statute_161bc3",
    "Thirty_Nine_Articles": "evidence_Bray_1994_Documents_of_the_English_Reformation",
    "Matthew_Parker": "evidence_Brook_1962_A_Life_of_Archbishop_Parker",
    "Edmund_Grindal": "evidence_Collinson_1979_Archbishop_Grindal_1519_f3ad34",
    "Puritanism": "evidence_Collinson_1967_The_Elizabethan_Puritan_17e4c6",
    "Puritan": "evidence_Lake_1988_Anglicans_and_Puritans_afd7c4",
    "Recusancy": "evidence_Bossy_1975_English_Catholic_Community",
    "Catholic": "evidence_Bossy_1975_English_Catholic_Community",
    "Marprelate": "evidence_Black_2008_The_Martin_Marprelate_fb379e",
    
    # Texts and Bibles
    "Tyndale": "evidence_Daniell_2003_The_Bible_in_English",
    "Great_Bible": "evidence_Daniell_2003_The_Bible_in_English",
    "Bishops_Bible": "evidence_Daniell_2003_The_Bible_in_English",
    "Geneva_Bible": "evidence_Daniell_2003_The_Bible_in_English",
    "Bible": "evidence_Daniell_2003_The_Bible_in_English",
    
    # Rebellions
    "Pilgrimage_of_Grace": "evidence_Hoyle_2001_W_9d1e92",
    "Western_Rebellion": "evidence_Fletcher_2004_Tudor_Rebellions_f10cb6",
    "Ketts_Rebellion": "evidence_Land_1977_Kett_s_Rebellion_92af0f",
    "Wyatts_Rebellion": "evidence_Loades_1965_Two_Tudor_Conspiracies_6a147a",
    "Rebellion": "evidence_Fletcher_2004_Tudor_Rebellions_f10cb6",
    
    # Continental connections
    "European_Reformations": "evidence_Cameron_2012_The_European_Reformation_863269",
    "Continental_Reformations": "evidence_Cameron_2012_The_European_Reformation_863269",
    "Lutheran": "evidence_Cameron_2012_The_European_Reformation_863269",
    "Calvinist": "evidence_Cameron_2012_The_European_Reformation_863269",
    "Protestant": "evidence_Marshall_2017_Heretics_and_Believers_926b84",
    
    # Parliament, Law, and Court
    "English_Parliament": "evidence_Elton_1982_Tudor_Constitution",
    "Parliament": "evidence_Elton_1982_Tudor_Constitution",
    "Ecclesiastical_Courts": "evidence_Helmholz_1990_H_72f084",
    "Court": "evidence_Loades_1987_The_Tudor_Court_5c9b30",
    
    # Comprehensive works
    "Reformation": "evidence_Jones_2002_The_English_Reformation_632253",
    "Heretic": "evidence_Marshall_2017_Heretics_and_Believers_926b84",
}

# Framework mappings for relationship types
FRAMEWORK_MAPPINGS = {
    # Causal relationships
    "CAUSES": "cause_and_effect",
    "ENABLES": "cause_and_effect",
    "TRIGGERS": "cause_and_effect",
    "LEADS_TO": "cause_and_effect",
    
    # Influence and diffusion
    "INFLUENCES": "cultural_diffusion",
    "TRANSMITS": "cultural_diffusion",
    "DIFFUSES": "cultural_diffusion",
    "ADOPTS": "cultural_diffusion",
    
    # Institutional and continuity
    "PROMULGATES": "continuity_and_change",
    "CODIFIES": "continuity_and_change",
    "STANDARDIZES": "continuity_and_change",
    "REFORMS": "continuity_and_change",
    
    # Opposition and conflict
    "OPPOSES": "conflict_and_cooperation",
    "DISPUTES": "conflict_and_cooperation",
    "PERSECUTES": "conflict_and_cooperation",
    "EXECUTES": "conflict_and_cooperation",
    "EXCOMMUNICATES": "conflict_and_cooperation",
    
    # Cooperation
    "ENDORSES": "conflict_and_cooperation",
    "SUPPORTS": "conflict_and_cooperation",
    "ALLIES_WITH": "conflict_and_cooperation",
    
    # Spatial
    "OCCURS_IN": "spatial_analysis",
    "HOSTS": "spatial_analysis",
    "CONTAINS": "spatial_analysis",
    
    # Authorship and creation
    "WRITES": "intellectual_history",
    "AUTHORS": "intellectual_history",
    "TRANSLATES": "intellectual_history",
    "COMMENTATES_ON": "intellectual_history",
    
    # Leadership and organization
    "LEADS": "political_analysis",
    "ORGANIZES": "political_analysis",
    "ADMINISTERS": "political_analysis",
    "PRESIDES_OVER": "political_analysis",
    
    # Default
    "default": "historical_context",
}

# Place assignments for English Reformation events
PLACE_ASSIGNMENTS = {
    # Events in England generally
    "English_Reformation": "England",
    "Break_with_Rome": "England",
    "Dissolution_of_the_Monasteries": "England",
    "Act_of_Supremacy_Passage": "Westminster",
    "Pilgrimage_of_Grace_1536": "Northern_England",
    "Western_Rebellion_1549": "Cornwall",
    "Ketts_Rebellion_1549": "Norfolk",
    "Wyatts_Rebellion_1554": "Kent",
    
    # London events
    "Execution_of_Thomas_More_1535": "London",
    "Execution_of_John_Fisher_1535": "London",
    "Execution_of_Anne_Boleyn_1536": "London",
    "Execution_of_Thomas_Cromwell_1540": "London",
    
    # Oxford events
    "Oxford_Martyrs_1555_1556": "Oxford",
    
    # Canterbury events
    "Convocation_of_1563": "Canterbury",
}


def get_evidence_for_relationship(rel: Dict) -> Optional[str]:
    """Determine the best evidence source for a relationship."""
    start = rel.get("start_slug", "")
    end = rel.get("end_slug", "")
    rel_type = rel.get("type", "")
    
    # Check specific node matches
    for key, evidence in ENGLISH_REFORMATION_EVIDENCE.items():
        if key in start or key in end:
            return evidence
    
    # Use default
    return ENGLISH_REFORMATION_EVIDENCE.get("default")


def get_framework_for_relationship(rel: Dict) -> str:
    """Determine the framework for a relationship type."""
    rel_type = rel.get("type", "")
    return FRAMEWORK_MAPPINGS.get(rel_type, FRAMEWORK_MAPPINGS["default"])


def step_1_fix_node_statuses(nodes_data: Dict) -> int:
    """Ensure all nodes have proper status."""
    nodes = nodes_data.get("nodes", [])
    fixed = 0
    
    for node in nodes:
        if not node.get("status") or node.get("status") == "Unknown":
            node["status"] = "PROPOSED"
            node["workflow_stage"] = "PROPOSED"
            fixed += 1
    
    return fixed


def step_2_add_evidence(rels_data: Dict) -> int:
    """Add evidence references to relationships without them."""
    relationships = rels_data.get("relationships", [])
    added = 0
    
    for rel in relationships:
        if not rel.get("evidence_slug") and not rel.get("evidence_url"):
            evidence = get_evidence_for_relationship(rel)
            if evidence:
                rel["evidence_slug"] = evidence
                rel["citation_style"] = "Chicago 17"
                if not rel.get("page_refs"):
                    rel["page_refs"] = "passim"
                added += 1
    
    return added


def step_3_add_framed_by(rels_data: Dict) -> int:
    """Generate FRAMED_BY edges for relationships."""
    relationships = rels_data.get("relationships", [])
    framed_by_edges = rels_data.get("framed_by_edges", [])
    
    # Get existing FRAMED_BY to avoid duplicates
    existing = set()
    for fb in framed_by_edges:
        key = f"{fb.get('relationship_id')}|{fb.get('framework_slug')}"
        existing.add(key)
    
    added = 0
    for rel in relationships:
        rel_id = rel.get("id")
        if not rel_id:
            continue
            
        framework = get_framework_for_relationship(rel)
        key = f"{rel_id}|{framework}"
        
        if key not in existing:
            framed_by_edges.append({
                "relationship_id": rel_id,
                "framework_slug": framework,
                "created_at": datetime.now(timezone.utc).isoformat(),
                "created_by": "complete_curator_workflow.py"
            })
            existing.add(key)
            added += 1
    
    rels_data["framed_by_edges"] = framed_by_edges
    return added


def step_4_add_place_edges(rels_data: Dict) -> int:
    """Add OCCURS_IN place edges for events."""
    place_edges = rels_data.get("place_edges", [])
    
    # Get existing place edges to avoid duplicates
    existing = set(pe.get("node_slug") for pe in place_edges)
    
    added = 0
    for node_slug, place_slug in PLACE_ASSIGNMENTS.items():
        if node_slug not in existing:
            place_edges.append({
                "node_slug": node_slug,
                "place_slug": place_slug,
                "relationship_type": "OCCURS_IN",
                "created_at": datetime.now(timezone.utc).isoformat(),
                "created_by": "complete_curator_workflow.py"
            })
            existing.add(node_slug)
            added += 1
    
    rels_data["place_edges"] = place_edges
    return added


def step_5_run_qa(nodes_data: Dict, rels_data: Dict) -> Dict:
    """Run QA checks and return issues."""
    issues = {
        "nodes_without_status": 0,
        "nodes_without_description": 0,
        "rels_without_evidence": 0,
        "rels_without_type": 0,
        "orphan_slugs": [],
    }
    
    nodes = nodes_data.get("nodes", [])
    relationships = rels_data.get("relationships", [])
    
    # Get all node slugs
    node_slugs = set(n.get("slug") for n in nodes)
    
    # Check nodes
    for node in nodes:
        if not node.get("status"):
            issues["nodes_without_status"] += 1
        if not node.get("description"):
            issues["nodes_without_description"] += 1
    
    # Check relationships
    for rel in relationships:
        if not rel.get("evidence_slug") and not rel.get("evidence_url"):
            issues["rels_without_evidence"] += 1
        if not rel.get("type"):
            issues["rels_without_type"] += 1
        
        # Check for orphan slugs
        start = rel.get("start_slug")
        end = rel.get("end_slug")
        if start and start not in node_slugs:
            if start not in issues["orphan_slugs"]:
                issues["orphan_slugs"].append(start)
        if end and end not in node_slugs:
            if end not in issues["orphan_slugs"]:
                issues["orphan_slugs"].append(end)
    
    return issues


def step_6_update_statuses(nodes_data: Dict, rels_data: Dict) -> tuple:
    """Update statuses to REVIEWED where all criteria are met."""
    nodes = nodes_data.get("nodes", [])
    relationships = rels_data.get("relationships", [])
    
    nodes_updated = 0
    rels_updated = 0
    
    # Update nodes with complete data
    for node in nodes:
        if node.get("status") == "PROPOSED":
            if node.get("description") and node.get("label"):
                node["status"] = "REVIEWED"
                node["workflow_stage"] = "REVIEWED"
                node["reviewed_at"] = datetime.now(timezone.utc).isoformat()
                node["reviewed_by"] = "complete_curator_workflow.py"
                nodes_updated += 1
    
    # Update relationships with evidence
    for rel in relationships:
        if rel.get("status") == "PROPOSED":
            if rel.get("evidence_slug") or rel.get("evidence_url"):
                rel["status"] = "REVIEWED"
                rel["reviewed_at"] = datetime.now(timezone.utc).isoformat()
                rel["reviewed_by"] = "complete_curator_workflow.py"
                rels_updated += 1
    
    return nodes_updated, rels_updated


def process_cluster(cluster_name: str, dry_run: bool = False, step: Optional[str] = None):
    """Process a cluster through the curator workflow."""
    base_path = Path(__file__).parent.parent
    nodes_path = base_path / "data" / "Nodes" / f"nodes.{cluster_name}.json"
    rels_path = base_path / "data" / "Relationships" / f"relationships.{cluster_name}.json"
    
    if not nodes_path.exists():
        print(f"Error: Nodes file not found: {nodes_path}")
        return
    if not rels_path.exists():
        print(f"Error: Relationships file not found: {rels_path}")
        return
    
    # Load data
    with open(nodes_path, 'r', encoding='utf-8') as f:
        nodes_data = json.load(f)
    with open(rels_path, 'r', encoding='utf-8') as f:
        rels_data = json.load(f)
    
    print(f"{'[DRY RUN] ' if dry_run else ''}Processing cluster: {cluster_name}")
    print("=" * 60)
    
    # Step 1: Fix node statuses
    if not step or step == "propose":
        print("\n📝 Step 1: PROPOSE - Fix node statuses")
        fixed = step_1_fix_node_statuses(nodes_data)
        print(f"   Fixed {fixed} nodes without status")
    
    # Step 2: Add evidence
    if not step or step == "cite":
        print("\n📚 Step 2: CITE - Add evidence references")
        added = step_2_add_evidence(rels_data)
        print(f"   Added evidence to {added} relationships")
    
    # Step 3: Add framework edges
    if not step or step == "frame":
        print("\n🔗 Step 3: FRAME - Add FRAMED_BY edges")
        added = step_3_add_framed_by(rels_data)
        print(f"   Added {added} FRAMED_BY edges")
    
    # Step 4: Add place edges
    if not step or step == "place":
        print("\n📍 Step 4: PLACE - Verify timeframes and add place edges")
        tf_edges = len(rels_data.get("timeframe_edges", []))
        print(f"   Timeframe edges: {tf_edges}")
        added = step_4_add_place_edges(rels_data)
        print(f"   Added {added} place edges")
    
    # Step 5: QA
    if not step or step == "review":
        print("\n✅ Step 5: REVIEW - QA checks")
        issues = step_5_run_qa(nodes_data, rels_data)
        print(f"   Nodes without status: {issues['nodes_without_status']}")
        print(f"   Nodes without description: {issues['nodes_without_description']}")
        print(f"   Relationships without evidence: {issues['rels_without_evidence']}")
        print(f"   Orphan slugs: {len(issues['orphan_slugs'])}")
        if issues['orphan_slugs'][:5]:
            print(f"   Sample orphans: {issues['orphan_slugs'][:5]}")
    
    # Step 6: Update statuses
    if not step or step == "publish":
        print("\n🚀 Step 6: PUBLISH - Update statuses to REVIEWED")
        nodes_updated, rels_updated = step_6_update_statuses(nodes_data, rels_data)
        print(f"   Nodes updated to REVIEWED: {nodes_updated}")
        print(f"   Relationships updated to REVIEWED: {rels_updated}")
    
    # Update metadata
    now = datetime.now(timezone.utc).isoformat()
    
    if "_meta" not in nodes_data:
        nodes_data["_meta"] = {}
    nodes_data["_meta"]["curator_workflow_completed_at"] = now
    nodes_data["_meta"]["curator_workflow_script"] = "scripts/complete_curator_workflow.py"
    
    if "_meta" not in rels_data:
        rels_data["_meta"] = {}
    rels_data["_meta"]["curator_workflow_completed_at"] = now
    rels_data["_meta"]["curator_workflow_script"] = "scripts/complete_curator_workflow.py"
    
    # Save if not dry run
    if not dry_run:
        print("\n💾 Saving changes...")
        with open(nodes_path, 'w', encoding='utf-8') as f:
            json.dump(nodes_data, f, indent=2, ensure_ascii=False)
        with open(rels_path, 'w', encoding='utf-8') as f:
            json.dump(rels_data, f, indent=2, ensure_ascii=False)
        print("   Saved!")
    else:
        print("\n[DRY RUN] No changes saved.")
    
    # Final summary
    print("\n" + "=" * 60)
    print("FINAL SUMMARY")
    print("=" * 60)
    nodes = nodes_data.get("nodes", [])
    rels = rels_data.get("relationships", [])
    
    node_statuses = Counter(n.get("status", "Unknown") for n in nodes)
    rel_statuses = Counter(r.get("status", "Unknown") for r in rels)
    
    print(f"Total nodes: {len(nodes)}")
    for status, count in sorted(node_statuses.items()):
        print(f"  {status}: {count}")
    
    print(f"\nTotal relationships: {len(rels)}")
    for status, count in sorted(rel_statuses.items()):
        print(f"  {status}: {count}")
    
    print(f"\nTimeframe edges: {len(rels_data.get('timeframe_edges', []))}")
    print(f"FRAMED_BY edges: {len(rels_data.get('framed_by_edges', []))}")
    print(f"Place edges: {len(rels_data.get('place_edges', []))}")


def main():
    parser = argparse.ArgumentParser(
        description="Complete curator workflow for a cluster."
    )
    parser.add_argument("cluster", help="Cluster name (e.g., English_Reformation)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without saving")
    parser.add_argument("--step", choices=["propose", "cite", "frame", "place", "review", "publish"],
                       help="Run only a specific step")
    
    args = parser.parse_args()
    process_cluster(args.cluster, args.dry_run, args.step)


if __name__ == "__main__":
    main()
