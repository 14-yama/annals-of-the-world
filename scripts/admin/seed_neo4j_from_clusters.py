#!/usr/bin/env python3
"""Seed Neo4j from per-cluster node and relationship JSON files.

This utility walks `data/Nodes/nodes.<cluster>.json` and
`data/Relationships/relationships.<cluster>.json` files, then upserts
all records into Neo4j. It is intentionally conservative: nodes are
loaded before relationships, it skips malformed records, and it can run
in a dry-run mode for planning.

Example:
    python admin/seed_neo4j_from_clusters.py --clusters English_Reformation
    python admin/seed_neo4j_from_clusters.py --dry-run
"""
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Sequence

try:
    from dotenv import load_dotenv
except Exception:  # pragma: no cover - optional dev dependency
    def load_dotenv(*args, **kwargs):
        return None
try:
    from neo4j import GraphDatabase, Driver
except Exception:  # pragma: no cover - allow running dry-run without neo4j installed
    GraphDatabase = None
    Driver = None

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_ENV = ROOT / ".env.local"
NODES_DIR = ROOT / "data" / "Nodes"
RELS_DIR = ROOT / "data" / "Relationships"

NODE_PATTERN = re.compile(r"^nodes\.(?P<cluster>.+)\.json$")
REL_PATTERN = re.compile(r"^relationships\.(?P<cluster>.+)\.json$")


def load_env(env_file: Path) -> None:
    """Load environment variables so Neo4j credentials are available."""
    if env_file.exists():
        load_dotenv(env_file)
    else:
        # Fallback to any env already present
        load_dotenv()


def discover_clusters() -> Dict[str, Dict[str, Optional[Path]]]:
    """Return mapping of cluster slug to node/relationship file paths."""
    clusters: Dict[str, Dict[str, Optional[Path]]] = {}

    for path in NODES_DIR.glob("nodes.*.json"):
        match = NODE_PATTERN.match(path.name)
        if not match:
            continue
        cluster = match.group("cluster")
        clusters.setdefault(cluster, {}).setdefault("nodes", path)

    for path in RELS_DIR.glob("relationships.*.json"):
        match = REL_PATTERN.match(path.name)
        if not match:
            continue
        cluster = match.group("cluster")
        clusters.setdefault(cluster, {}).setdefault("relationships", path)

    return clusters


def load_nodes(path: Path) -> List[Dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, dict):
        nodes = payload.get("nodes")
        if nodes is None:
            raise ValueError(f"JSON {path} missing 'nodes' array")
        return list(nodes)
    if isinstance(payload, list):
        return list(payload)
    raise ValueError(f"Unsupported JSON shape in {path}")


def load_relationships(path: Path) -> List[Dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, dict):
        rels = payload.get("relationships")
        if rels is None:
            raise ValueError(f"JSON {path} missing 'relationships' array")
        return list(rels)
    if isinstance(payload, list):
        return list(payload)
    raise ValueError(f"Unsupported JSON shape in {path}")


def sanitize_label(value: Optional[str]) -> str:
    return (value or "Concept").strip().replace(" ", "_")


def sanitize_rel_type(value: Optional[str]) -> str:
    base = (value or "RELATED_TO").strip().replace("-", "_")
    base = re.sub(r"\s+", "_", base)
    return base.upper() or "RELATED_TO"


class ClusterSeeder:
    def __init__(self, uri: str, user: str, password: str, dry_run: bool = False):
        self.uri = uri
        self.user = user
        self.password = password
        self.dry_run = dry_run
        # Delay / guard driver creation so we can provide a clear error
        # message when the `neo4j` package isn't installed. In dry-run
        # mode no driver is required.
        self.driver: Optional[Driver]
        if dry_run:
            self.driver = None
        else:
            if GraphDatabase is None:
                raise SystemExit(
                    "neo4j Python driver not found. Install the 'neo4j' package or run with --dry-run."
                )
            self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self) -> None:
        if self.driver:
            self.driver.close()

    # ---- node ingestion -------------------------------------------------
    def ingest_nodes(self, cluster: str, nodes: Sequence[Dict]) -> int:
        if not nodes:
            return 0
        if self.dry_run:
            print(f"[dry-run] Would ingest {len(nodes)} nodes for {cluster}")
            return len(nodes)

        assert self.driver
        ingested = 0
        with self.driver.session() as session:
            for node in nodes:
                slug = node.get("slug")
                if not slug:
                    print(f"Skipping node without slug in {cluster}: {node}")
                    continue
                label = sanitize_label(node.get("label") or node.get("type"))
                props = {
                    k: v for k, v in node.items()
                    if k not in {"id", "label", "type"}
                }
                session.execute_write(self._merge_node, label, slug, props)
                ingested += 1
        return ingested

    @staticmethod
    def _merge_node(tx, label: str, slug: str, props: Dict) -> None:
        cypher = f"MERGE (n:`{label}` {{slug: $slug}}) SET n += $props"
        tx.run(cypher, slug=slug, props=props)

    # ---- relationship ingestion ----------------------------------------
    def ingest_relationships(self, cluster: str, rels: Sequence[Dict]) -> int:
        if not rels:
            return 0
        if self.dry_run:
            print(f"[dry-run] Would ingest {len(rels)} relationships for {cluster}")
            return len(rels)

        assert self.driver
        ingested = 0
        with self.driver.session() as session:
            for rel in rels:
                start_slug = rel.get("start_slug")
                end_slug = rel.get("end_slug")
                if not start_slug or not end_slug:
                    print(f"Skipping relationship without start/end slug in {cluster}: {rel}")
                    continue
                rel_type = sanitize_rel_type(rel.get("type"))
                props = {
                    k: v for k, v in rel.items()
                    if k not in {"id", "start_slug", "end_slug", "type"}
                }
                session.execute_write(
                    self._merge_relationship,
                    rel_type,
                    start_slug,
                    end_slug,
                    props,
                )
                ingested += 1
        return ingested

    @staticmethod
    def _merge_relationship(tx, rel_type: str, start_slug: str, end_slug: str, props: Dict) -> None:
        cypher = (
            f"MATCH (start {{slug: $start_slug}}) "
            f"MATCH (end {{slug: $end_slug}}) "
            f"MERGE (start)-[rel:`{rel_type}`]->(end) "
            f"SET rel = $props"
        )
        tx.run(
            cypher,
            start_slug=start_slug,
            end_slug=end_slug,
            props=props,
        )


# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--clusters",
        nargs="+",
        help="Optional list of cluster slugs to seed (default: all discovered)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print actions without writing to Neo4j",
    )
    parser.add_argument(
        "--skip-nodes",
        action="store_true",
        help="Skip node ingestion",
    )
    parser.add_argument(
        "--skip-relationships",
        action="store_true",
        help="Skip relationship ingestion",
    )
    parser.add_argument(
        "--env-file",
        default=str(DEFAULT_ENV),
        help="Path to .env-style file with NEO4J_URI/USER/PASSWORD (default: .env.local)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    env_file = Path(args.env_file)
    load_env(env_file)

    uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    user = os.getenv("NEO4J_USER", "neo4j")
    password = os.getenv("NEO4J_PASSWORD", "neo4j")

    clusters = discover_clusters()
    # Diagnostic help: if discovery fails, print resolved paths so we can
    # understand why the script isn't seeing the files on the user's machine.
    if not clusters:
        print("No per-cluster JSON files found under data/Nodes or data/Relationships.")
        try:
            print("DEBUG: script resolved paths:")
            print(f"  __file__ -> {Path(__file__).resolve()}")
            print(f"  cwd -> {Path.cwd()}")
            print(f"  ROOT -> {ROOT}")
            print(f"  NODES_DIR -> {NODES_DIR} (exists={NODES_DIR.exists()})")
            if NODES_DIR.exists():
                print("  sample node files:", [p.name for p in sorted(NODES_DIR.glob('nodes.*.json'))][:10])
            print(f"  RELS_DIR -> {RELS_DIR} (exists={RELS_DIR.exists()})")
            if RELS_DIR.exists():
                print("  sample rel files:", [p.name for p in sorted(RELS_DIR.glob('relationships.*.json'))][:10])
        except Exception as exc:  # pragma: no cover - best effort diagnostics
            print("DEBUG: failed to print diagnostic info:", exc)
        return 1

    selected = args.clusters or sorted(clusters.keys())
    missing = [c for c in selected if c not in clusters]
    if missing:
        print("Warning: no files found for cluster(s):", ", ".join(missing))
    ordered = [c for c in selected if c in clusters]

    if not ordered:
        print("No valid clusters selected.")
        return 1

    seeder = ClusterSeeder(uri, user, password, dry_run=args.dry_run)
    total_nodes = 0
    total_rels = 0

    try:
        if not args.skip_nodes:
            for cluster in ordered:
                path = clusters[cluster].get("nodes")
                if path is None:
                    print(f"No node file for {cluster}; skipping nodes")
                    continue
                nodes = load_nodes(path)
                count = seeder.ingest_nodes(cluster, nodes)
                total_nodes += count
                print(f"Cluster {cluster}: ingested {count} nodes")
        else:
            print("Skipping node ingestion per flag.")

        if not args.skip_relationships:
            for cluster in ordered:
                path = clusters[cluster].get("relationships")
                if path is None:
                    print(f"No relationship file for {cluster}; skipping relationships")
                    continue
                rels = load_relationships(path)
                count = seeder.ingest_relationships(cluster, rels)
                total_rels += count
                print(f"Cluster {cluster}: ingested {count} relationships")
        else:
            print("Skipping relationship ingestion per flag.")
    finally:
        seeder.close()

    print("\nSummary:")
    print(f"  Clusters processed: {len(ordered)}")
    print(f"  Nodes ingested: {total_nodes}")
    print(f"  Relationships ingested: {total_rels}")
    if args.dry_run:
        print("(Dry-run mode: no changes were written.)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
