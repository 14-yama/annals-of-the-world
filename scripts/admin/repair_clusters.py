#!/usr/bin/env python3
"""Repair all clusters: create missing nodes, prune orphan relationships, ensure completeness.

This script:
1. Loads all nodes across all clusters into a global registry
2. For each cluster:
   - Identifies relationships referencing non-existent nodes
   - Creates stub nodes for missing references (with proper slugs)
   - Removes relationships that reference malformed/unparseable slugs
   - Ensures every node has at least one relationship (reports isolated nodes)
3. Writes clean production-ready files to data/Nodes/ and data/Relationships/
4. Produces a summary report

Usage:
  python3 repair_clusters.py [--dry-run]
"""

import argparse
import json
import re
import datetime
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[2]
NODES_DIR = ROOT / "data" / "Nodes"
REL_DIR = ROOT / "data" / "Relationships"
CLUSTERS_DIR = ROOT / "docs" / "clusters"

TIMESTAMP = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%MZ")


def slugify(text: str) -> str:
    """Convert text to a valid slug."""
    # Remove markdown links
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    # Remove special chars except underscores and hyphens
    text = re.sub(r'[^\w\s-]', '', text)
    # Replace spaces with underscores
    text = re.sub(r'\s+', '_', text.strip())
    return text


def is_valid_slug(slug: str) -> bool:
    """Check if slug is valid (no markdown, no descriptions)."""
    if not slug:
        return False
    # Reject markdown links
    if '[' in slug or ']' in slug or '(' in slug or ')' in slug:
        return False
    # Reject if it looks like a description (contains periods at end, very long)
    if slug.endswith('.') or len(slug) > 100:
        return False
    # Reject if contains pipe (likely a malformed _key)
    if '|' in slug:
        return False
    return True


def load_all_nodes() -> dict:
    """Load all nodes from all cluster files into a global registry."""
    global_nodes = {}  # slug -> node dict
    cluster_nodes = defaultdict(set)  # cluster -> set of slugs
    
    for p in sorted(NODES_DIR.iterdir()):
        if p.suffix != '.json' or 'bak' in p.name:
            continue
        try:
            data = json.loads(p.read_text(encoding='utf-8'))
        except Exception:
            continue
        
        cluster = data.get('_meta', {}).get('cluster', p.stem.replace('nodes.', ''))
        for n in data.get('nodes', []):
            slug = n.get('slug')
            if slug and is_valid_slug(slug):
                global_nodes[slug] = n
                cluster_nodes[cluster].add(slug)
    
    return global_nodes, cluster_nodes


def load_relationships_by_cluster() -> dict:
    """Load all relationships grouped by cluster."""
    cluster_rels = {}  # cluster -> list of (filename, rel_list, meta)
    
    for p in sorted(REL_DIR.iterdir()):
        if p.suffix != '.json' or 'bak' in p.name:
            continue
        try:
            data = json.loads(p.read_text(encoding='utf-8'))
        except Exception as e:
            print(f"Warning: Could not parse {p.name}: {e}")
            continue
        
        cluster = data.get('_meta', {}).get('cluster', p.stem.replace('relationships.', ''))
        rels = data.get('relationships', [])
        meta = data.get('_meta', {})
        
        if cluster not in cluster_rels:
            cluster_rels[cluster] = []
        cluster_rels[cluster].append((p.name, rels, meta, p))
    
    return cluster_rels


def get_cluster_list() -> list:
    """Get list of canonical cluster names from docs/clusters."""
    clusters = []
    if CLUSTERS_DIR.exists():
        for p in CLUSTERS_DIR.iterdir():
            if p.is_dir():
                clusters.append(p.name)
    return sorted(clusters)


def create_stub_node(slug: str, cluster: str) -> dict:
    """Create a stub node for a missing reference."""
    name = slug.replace('_', ' ')
    return {
        "slug": slug,
        "name": name,
        "label": "Idea",
        "status": "PROPOSED",
        "workflow_stage": "PROPOSED",
        "governance_version": 5,
        "created_at": TIMESTAMP,
        "created_by": "auto:repair_clusters",
        "lang": "en",
        "script": "Latn",
        "description": f"Auto-generated stub for {name} in {cluster} cluster"
    }


def repair_cluster(cluster: str, global_nodes: dict, cluster_rels: dict, dry_run: bool = True) -> dict:
    """Repair a single cluster: fix nodes and relationships."""
    report = {
        "cluster": cluster,
        "nodes_added": [],
        "nodes_fixed": [],
        "rels_removed": [],
        "rels_fixed": [],
        "isolated_nodes": [],
        "clean_node_count": 0,
        "clean_rel_count": 0,
    }
    
    # Load existing nodes for this cluster
    node_file = NODES_DIR / f"nodes.{cluster}.json"
    existing_nodes = {}
    existing_meta = {
        "cluster": cluster,
        "notes": f"Production-ready nodes for {cluster}",
        "registry": "docs/nodes/node-attribute-registry.md",
        "source": f"docs/clusters/{cluster}/README.md",
        "generated_at": TIMESTAMP,
        "generator": "scripts/admin/repair_clusters.py"
    }
    
    if node_file.exists():
        try:
            data = json.loads(node_file.read_text(encoding='utf-8'))
            existing_meta = data.get('_meta', existing_meta)
            for n in data.get('nodes', []):
                slug = n.get('slug')
                if slug and is_valid_slug(slug):
                    existing_nodes[slug] = n
        except Exception:
            pass
    
    # Collect all relationship files for this cluster
    rel_files = cluster_rels.get(cluster, [])
    all_rels = []
    rel_meta = {
        "cluster": cluster,
        "notes": f"Production-ready relationships for {cluster}",
        "registry": "docs/guidelines/node-relationship-vocabulary.md",
        "schema_doc": "docs/guidelines/schema.md",
        "source": f"docs/clusters/{cluster}/README.md",
        "generated_at": TIMESTAMP,
        "generator": "scripts/admin/repair_clusters.py"
    }
    
    for fname, rels, meta, fpath in rel_files:
        if meta:
            rel_meta = meta
        for r in rels:
            all_rels.append((fname, r))
    
    # Identify all referenced slugs
    referenced_slugs = set()
    clean_rels = []
    
    for fname, r in all_rels:
        start = r.get('start_slug', '')
        end = r.get('end_slug', '')
        rel_type = r.get('type', '')
        
        # Skip malformed relationships
        if not is_valid_slug(start):
            # Try to fix the slug
            fixed_start = slugify(start)
            if is_valid_slug(fixed_start) and fixed_start:
                r['start_slug'] = fixed_start
                start = fixed_start
                report['rels_fixed'].append(f"{fname}: fixed start_slug to {fixed_start}")
            else:
                report['rels_removed'].append(f"{fname}: invalid start_slug '{start[:50]}...'")
                continue
        
        if not is_valid_slug(end):
            fixed_end = slugify(end)
            if is_valid_slug(fixed_end) and fixed_end:
                r['end_slug'] = fixed_end
                end = fixed_end
                report['rels_fixed'].append(f"{fname}: fixed end_slug to {fixed_end}")
            else:
                report['rels_removed'].append(f"{fname}: invalid end_slug '{end[:50]}...'")
                continue
        
        # Skip if status is REMOVED
        if r.get('status') == 'REMOVED':
            continue
        
        # Update _key if needed
        if r.get('_key'):
            r['_key'] = f"{start}|{rel_type}|{end}"
        
        referenced_slugs.add(start)
        referenced_slugs.add(end)
        clean_rels.append(r)
    
    # Create stub nodes for missing references
    for slug in referenced_slugs:
        if slug not in global_nodes and slug not in existing_nodes:
            stub = create_stub_node(slug, cluster)
            existing_nodes[slug] = stub
            global_nodes[slug] = stub  # Add to global registry
            report['nodes_added'].append(slug)
    
    # Identify isolated nodes (nodes with no relationships)
    nodes_in_rels = set()
    for r in clean_rels:
        nodes_in_rels.add(r.get('start_slug'))
        nodes_in_rels.add(r.get('end_slug'))
    
    for slug in existing_nodes:
        if slug not in nodes_in_rels:
            report['isolated_nodes'].append(slug)
    
    # Deduplicate relationships by _key
    seen_keys = set()
    deduped_rels = []
    for r in clean_rels:
        key = r.get('_key', f"{r.get('start_slug')}|{r.get('type')}|{r.get('end_slug')}")
        if key not in seen_keys:
            seen_keys.add(key)
            deduped_rels.append(r)
    
    # Renumber relationship IDs
    for i, r in enumerate(deduped_rels, start=1):
        r['id'] = i
    
    report['clean_node_count'] = len(existing_nodes)
    report['clean_rel_count'] = len(deduped_rels)
    
    # Write clean files
    if not dry_run:
        # Write nodes
        clean_nodes_data = {
            "_meta": {
                **existing_meta,
                "generated_at": TIMESTAMP,
                "generator": "scripts/admin/repair_clusters.py"
            },
            "nodes": sorted(existing_nodes.values(), key=lambda x: x.get('slug', ''))
        }
        node_file.write_text(json.dumps(clean_nodes_data, ensure_ascii=False, indent=2), encoding='utf-8')
        
        # Write relationships (single canonical file per cluster)
        clean_rel_file = REL_DIR / f"relationships.{cluster}.json"
        clean_rels_data = {
            "_meta": {
                **rel_meta,
                "generated_at": TIMESTAMP,
                "generator": "scripts/admin/repair_clusters.py"
            },
            "relationships": deduped_rels
        }
        clean_rel_file.write_text(json.dumps(clean_rels_data, ensure_ascii=False, indent=2), encoding='utf-8')
    
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without writing')
    parser.add_argument('--cluster', type=str, help='Repair only a specific cluster')
    args = parser.parse_args()
    
    print("Loading all nodes...")
    global_nodes, cluster_nodes = load_all_nodes()
    print(f"  Loaded {len(global_nodes)} nodes across {len(cluster_nodes)} clusters")
    
    print("Loading all relationships...")
    cluster_rels = load_relationships_by_cluster()
    print(f"  Loaded relationships for {len(cluster_rels)} clusters")
    
    clusters = get_cluster_list()
    if args.cluster:
        clusters = [args.cluster] if args.cluster in clusters else []
    
    print(f"\nRepairing {len(clusters)} clusters...")
    
    all_reports = []
    total_nodes_added = 0
    total_rels_removed = 0
    total_rels_fixed = 0
    
    for cluster in clusters:
        print(f"\n{'='*60}")
        print(f"Cluster: {cluster}")
        print('='*60)
        
        report = repair_cluster(cluster, global_nodes, cluster_rels, dry_run=args.dry_run)
        all_reports.append(report)
        
        total_nodes_added += len(report['nodes_added'])
        total_rels_removed += len(report['rels_removed'])
        total_rels_fixed += len(report['rels_fixed'])
        
        print(f"  Nodes: {report['clean_node_count']} (added {len(report['nodes_added'])} stubs)")
        print(f"  Relationships: {report['clean_rel_count']} (removed {len(report['rels_removed'])}, fixed {len(report['rels_fixed'])})")
        if report['isolated_nodes']:
            print(f"  Isolated nodes (no edges): {len(report['isolated_nodes'])}")
        
        if report['nodes_added'][:5]:
            print(f"  Sample nodes added: {report['nodes_added'][:5]}")
        if report['rels_removed'][:3]:
            print(f"  Sample rels removed: {report['rels_removed'][:3]}")
    
    print(f"\n{'='*60}")
    print("SUMMARY")
    print('='*60)
    print(f"Clusters processed: {len(clusters)}")
    print(f"Total nodes added: {total_nodes_added}")
    print(f"Total relationships removed: {total_rels_removed}")
    print(f"Total relationships fixed: {total_rels_fixed}")
    
    if args.dry_run:
        print("\n[DRY-RUN] No files were modified.")
    else:
        print("\nClean production files written to data/Nodes/ and data/Relationships/")
    
    # Write summary report
    report_path = REL_DIR / "cluster_repair_report.md"
    lines = [
        "# Cluster Repair Report",
        f"\nGenerated: {TIMESTAMP}",
        f"\nMode: {'DRY-RUN' if args.dry_run else 'PRODUCTION'}",
        f"\n## Summary",
        f"- Clusters processed: {len(clusters)}",
        f"- Total nodes added: {total_nodes_added}",
        f"- Total relationships removed: {total_rels_removed}",
        f"- Total relationships fixed: {total_rels_fixed}",
        "\n## Per-Cluster Details\n"
    ]
    
    for r in all_reports:
        lines.append(f"### {r['cluster']}")
        lines.append(f"- Clean nodes: {r['clean_node_count']}")
        lines.append(f"- Clean relationships: {r['clean_rel_count']}")
        lines.append(f"- Nodes added: {len(r['nodes_added'])}")
        lines.append(f"- Relationships removed: {len(r['rels_removed'])}")
        lines.append(f"- Relationships fixed: {len(r['rels_fixed'])}")
        lines.append(f"- Isolated nodes: {len(r['isolated_nodes'])}")
        if r['nodes_added']:
            lines.append(f"- Added nodes: {', '.join(r['nodes_added'][:20])}" + ("..." if len(r['nodes_added']) > 20 else ""))
        lines.append("")
    
    report_path.write_text('\n'.join(lines), encoding='utf-8')
    print(f"\nReport written to: {report_path}")


if __name__ == '__main__':
    raise SystemExit(main())
