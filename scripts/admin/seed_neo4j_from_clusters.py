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
    python admin/seed_neo4j_from_clusters.py --clusters English_Reformation --ingest-edge-arrays
"""
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, TYPE_CHECKING

try:
    from dotenv import load_dotenv
except Exception:  # pragma: no cover - optional dev dependency
    def load_dotenv(*args, **kwargs) -> bool:
        return False
try:
    from neo4j import GraphDatabase, Driver
except Exception:  # pragma: no cover - allow running dry-run without neo4j installed
    GraphDatabase = None
    Driver = None

if TYPE_CHECKING:  # pragma: no cover
    from neo4j import Driver as Neo4jDriver
else:  # pragma: no cover
    Neo4jDriver = Any

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


def load_relationship_payload(path: Path) -> Dict:
    """Load relationship file and preserve any edge-array keys.

    Returns a dict with at least a 'relationships' key.
    """
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, dict):
        if "relationships" not in payload:
            raise ValueError(f"JSON {path} missing 'relationships' array")
        return payload
    if isinstance(payload, list):
        return {"relationships": list(payload)}
    raise ValueError(f"Unsupported JSON shape in {path}")


def sanitize_label(value: Optional[str]) -> str:
    return (value or "Idea").strip().replace(" ", "_")


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
        self.driver: Optional[Neo4jDriver]
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

    # ---- edge-array ingestion ----------------------------------------
    def ingest_edge_arrays(self, cluster: str, payload: Dict, edge_types: Optional[Sequence[str]] = None) -> Dict[str, int]:
        """Ingest edge arrays embedded in a relationships payload.

        Supported arrays:
        - timeframe_edges -> (n)-[:OCCURS_DURING]->(:Timeframe)
        - framed_by_edges -> (start)-[:FRAMED_BY {context_end, relationship_id,...}]->(:Framework)
        - place_edges -> (n)-[:OCCURS_IN]->(:Place)
        """
        results = {"timeframe": 0, "framed_by": 0, "place": 0}
        if self.dry_run:
            tf_count = len(payload.get("timeframe_edges", []) or [])
            fb_count = len(payload.get("framed_by_edges", []) or [])
            pl_count = len(payload.get("place_edges", []) or [])
            selected = set(edge_types or ["timeframe", "framed_by", "place"])
            if "timeframe" in selected and tf_count:
                print(f"[dry-run] Would ingest {tf_count} timeframe_edges for {cluster}")
                results["timeframe"] = tf_count
            if "framed_by" in selected and fb_count:
                print(f"[dry-run] Would ingest {fb_count} framed_by_edges for {cluster}")
                results["framed_by"] = fb_count
            if "place" in selected and pl_count:
                print(f"[dry-run] Would ingest {pl_count} place_edges for {cluster}")
                results["place"] = pl_count
            return results

        assert self.driver
        selected = set(edge_types or ["timeframe", "framed_by", "place"])
        with self.driver.session() as session:
            if "timeframe" in selected:
                tf_edges = payload.get("timeframe_edges") or []
                if tf_edges:
                    results["timeframe"] = session.execute_write(self._ingest_timeframe_edges, tf_edges)

            if "framed_by" in selected:
                fb_edges = payload.get("framed_by_edges") or []
                rels = payload.get("relationships") or []
                if fb_edges and rels:
                    derived = self._derive_framed_by_rows(fb_edges, rels)
                    if derived:
                        results["framed_by"] = session.execute_write(self._ingest_framed_by_edges, derived)

            if "place" in selected:
                pl_edges = payload.get("place_edges") or []
                if pl_edges:
                    results["place"] = session.execute_write(self._ingest_place_edges, pl_edges)

        return results

    @staticmethod
    def _ingest_timeframe_edges(tx, edges: Sequence[Dict]) -> int:
        # Ensure Timeframe nodes exist (MERGE by slug when available).
        timeframes = {}
        normalized = []
        for edge in edges:
            node_slug = edge.get("node_slug")
            tf_slug = edge.get("timeframe_slug")
            division = edge.get("division") or edge.get("timeframe_division")
            tf_name = edge.get("timeframe_name")
            if not node_slug:
                continue
            normalized.append(
                {
                    "node_slug": node_slug,
                    "tf_slug": tf_slug,
                    "division": division,
                }
            )
            if tf_slug:
                timeframes.setdefault(
                    tf_slug,
                    {"slug": tf_slug, "division": division, "name": tf_name},
                )

        if timeframes:
            tx.run(
                """
                UNWIND $timeframes AS tf
                MERGE (t:Timeframe {slug: tf.slug})
                ON CREATE SET t.created_at = datetime()
                SET t.division = coalesce(tf.division, t.division),
                    t.name = coalesce(tf.name, t.name)
                """,
                timeframes=list(timeframes.values()),
            )

        result = tx.run(
            """
            UNWIND $edges AS edge
            MATCH (n {slug: edge.node_slug})
            WITH n, edge
                        CALL (edge) {
                            WITH edge
                            WITH edge WHERE edge.tf_slug IS NOT NULL
                            MATCH (t:Timeframe {slug: edge.tf_slug})
                            RETURN t
                            UNION
                            WITH edge
                            WITH edge WHERE edge.tf_slug IS NULL AND edge.division IS NOT NULL
                            MERGE (t:Timeframe {division: edge.division})
                            ON CREATE SET t.created_at = datetime()
                            RETURN t
                        }
            MERGE (n)-[r:OCCURS_DURING]->(t)
            ON CREATE SET r.created_at = datetime()
            SET r.division = coalesce(edge.division, r.division)
            RETURN count(r) AS merged
            """,
            edges=normalized,
        )
        record = result.single()
        return int(record["merged"]) if record else 0

    @staticmethod
    def _derive_framed_by_rows(framed_by_edges: Sequence[Dict], relationships: Sequence[Dict]) -> List[Dict]:
        rel_lookup = {rel.get("id"): rel for rel in relationships if rel.get("id") is not None}
        rows: List[Dict] = []

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
                if evidence_slug:
                    evidence_url = f"data/Evidence/{evidence_slug}.json"
            if not evidence_url:
                # Must not be null due to FRAMED_BY property constraints.
                evidence_url = "data/Evidence/UNKNOWN.json"

            rows.append(
                {
                    "start_slug": start_slug,
                    "end_slug": end_slug,
                    "framework_slug": framework_slug,
                    "relationship_id": rel_id,
                    "citation_style": rel.get("citation_style") or "Chicago 17",
                    "evidence_url": evidence_url,
                    "page_refs": rel.get("page_refs") or "passim",
                    "source_note": f"Framing relationship between {start_slug} and {end_slug}",
                }
            )

        return rows

    @staticmethod
    def _ingest_framed_by_edges(tx, rows: Sequence[Dict]) -> int:
        # Ensure Framework nodes exist.
        frameworks = [
            {
                "slug": "cause_and_effect",
                "name": "Cause and Effect",
                "description": "Causal relationships between historical events and phenomena",
            },
            {
                "slug": "cultural_diffusion",
                "name": "Cultural Diffusion",
                "description": "Spread of ideas, practices, and innovations across cultures",
            },
            {
                "slug": "continuity_and_change",
                "name": "Continuity and Change",
                "description": "Patterns of persistence and transformation over time",
            },
            {
                "slug": "conflict_and_cooperation",
                "name": "Conflict and Cooperation",
                "description": "Opposition and alliance dynamics between actors",
            },
            {
                "slug": "spatial_analysis",
                "name": "Spatial Analysis",
                "description": "Geographic and spatial dimensions of historical events",
            },
            {
                "slug": "intellectual_history",
                "name": "Intellectual History",
                "description": "Development and transmission of ideas and texts",
            },
            {
                "slug": "political_analysis",
                "name": "Political Analysis",
                "description": "Power structures, governance, and political dynamics",
            },
            {
                "slug": "historical_context",
                "name": "Historical Context",
                "description": "General historical situating and background",
            },
        ]

        tx.run(
            """
            UNWIND $frameworks AS fw
            MERGE (f:Framework {slug: fw.slug})
            ON CREATE SET f.created_at = datetime()
            SET f.name = coalesce(fw.name, f.name),
                f.description = coalesce(fw.description, f.description)
            """,
            frameworks=frameworks,
        )

        result = tx.run(
            """
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
            """,
            rows=list(rows),
        )
        record = result.single()
        return int(record["merged"]) if record else 0

    @staticmethod
    def _ingest_place_edges(tx, edges: Sequence[Dict]) -> int:
        place_slugs = sorted({str(edge["place_slug"]) for edge in edges if edge.get("place_slug")})
        if place_slugs:
            tx.run(
                """
                UNWIND $places AS slug
                MERGE (p:Place {slug: slug})
                ON CREATE SET p.created_at = datetime(),
                              p.name = replace(slug, '_', ' '),
                              p.description = 'Place: ' + replace(slug, '_', ' ')
                """,
                places=place_slugs,
            )

        normalized = [
            {"node_slug": e.get("node_slug"), "place_slug": e.get("place_slug")}
            for e in edges
            if e.get("node_slug") and e.get("place_slug")
        ]
        result = tx.run(
            """
            UNWIND $edges AS edge
            MATCH (n {slug: edge.node_slug})
            MATCH (p:Place {slug: edge.place_slug})
            MERGE (n)-[r:OCCURS_IN]->(p)
            ON CREATE SET r.created_at = datetime()
            RETURN count(r) AS merged
            """,
            edges=normalized,
        )
        record = result.single()
        return int(record["merged"]) if record else 0

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
        "--ingest-edge-arrays",
        action="store_true",
        help="Also ingest timeframe_edges/framed_by_edges/place_edges from relationship files",
    )
    parser.add_argument(
        "--edge-type",
        choices=["timeframe", "framed_by", "place"],
        action="append",
        dest="edge_types",
        help="Only ingest specific edge array types (can be repeated; default: all)",
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
    total_edge_arrays = {"timeframe": 0, "framed_by": 0, "place": 0}

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

        for cluster in ordered:
            path = clusters[cluster].get("relationships")
            if path is None:
                print(f"No relationship file for {cluster}; skipping relationships")
                continue
            payload = load_relationship_payload(path)

            if not args.skip_relationships:
                rels = payload.get("relationships", [])
                count = seeder.ingest_relationships(cluster, rels)
                total_rels += count
                print(f"Cluster {cluster}: ingested {count} relationships")
            else:
                print(f"Skipping relationship ingestion for {cluster} per flag.")

            if args.ingest_edge_arrays:
                results = seeder.ingest_edge_arrays(cluster, payload, edge_types=args.edge_types)
                total_edge_arrays["timeframe"] += results.get("timeframe", 0)
                total_edge_arrays["framed_by"] += results.get("framed_by", 0)
                total_edge_arrays["place"] += results.get("place", 0)
                if any(results.values()):
                    print(
                        f"Cluster {cluster}: edge arrays ingested "
                        f"(timeframe={results['timeframe']}, framed_by={results['framed_by']}, place={results['place']})"
                    )
        if args.skip_relationships:
            print("Skipping relationship ingestion per flag.")
    finally:
        seeder.close()

    print("\nSummary:")
    print(f"  Clusters processed: {len(ordered)}")
    print(f"  Nodes ingested: {total_nodes}")
    print(f"  Relationships ingested: {total_rels}")
    if args.ingest_edge_arrays:
        print(
            "  Edge arrays ingested: "
            f"timeframe={total_edge_arrays['timeframe']}, "
            f"framed_by={total_edge_arrays['framed_by']}, "
            f"place={total_edge_arrays['place']}"
        )
    if args.dry_run:
        print("(Dry-run mode: no changes were written.)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
