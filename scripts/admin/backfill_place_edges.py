#!/usr/bin/env python3
"""Backfill place_edges (OCCURS_IN) for a cluster.

English_Reformation is currently the only production-ready cluster.
This script ensures every Event node in the cluster has a corresponding
entry in the relationship file's `place_edges` array.

Heuristic rules (slug-based) are applied first; otherwise we default to
`England`.

Usage:
  python scripts/admin/backfill_place_edges.py English_Reformation
  python scripts/admin/backfill_place_edges.py English_Reformation --ingest

Ingest mode uses the existing cluster seeder to ingest only place edge arrays.
"""

from __future__ import annotations

import argparse
import json
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set

ROOT = Path(__file__).resolve().parents[2]
NODES_DIR = ROOT / "data" / "Nodes"
RELS_DIR = ROOT / "data" / "Relationships"


PLACE_RULES: Sequence[tuple[str, str]] = (
    ("Westminster", "Westminster"),
    ("London", "London"),
    ("Oxford", "Oxford"),
    ("Canterbury", "Canterbury"),
    ("Northern_England", "Northern_England"),
    ("Cornwall", "Cornwall"),
    ("Norfolk", "Norfolk"),
    ("Kent", "Kent"),
)


def load_json(path: Path) -> Dict:
    return json.loads(path.read_text(encoding="utf-8"))


def iter_event_slugs(nodes_payload: Dict) -> List[str]:
    nodes = nodes_payload.get("nodes") if isinstance(nodes_payload, dict) else nodes_payload
    if not isinstance(nodes, list):
        return []
    slugs: List[str] = []
    for node in nodes:
        if not isinstance(node, dict):
            continue
        label = (node.get("label") or node.get("type") or "").strip()
        if label != "Event":
            continue
        slug = node.get("slug")
        if slug:
            slugs.append(slug)
    return sorted(set(slugs))


def choose_place_slug(event_slug: str) -> str:
    for needle, place_slug in PLACE_RULES:
        if needle in event_slug:
            return place_slug
    return "England"


def upsert_place_edges(rels_payload: Dict, event_slugs: Iterable[str]) -> int:
    place_edges = rels_payload.get("place_edges")
    if place_edges is None:
        place_edges = []
    if not isinstance(place_edges, list):
        raise ValueError("relationships payload has non-list place_edges")

    existing: Set[str] = set()
    for edge in place_edges:
        if isinstance(edge, dict) and edge.get("node_slug"):
            existing.add(edge["node_slug"])

    now = datetime.now(timezone.utc).isoformat()
    added = 0
    for slug in event_slugs:
        if slug in existing:
            continue
        place_edges.append(
            {
                "node_slug": slug,
                "place_slug": choose_place_slug(slug),
                "relationship_type": "OCCURS_IN",
                "created_at": now,
                "created_by": "backfill_place_edges.py",
            }
        )
        existing.add(slug)
        added += 1

    rels_payload["place_edges"] = place_edges
    rels_payload.setdefault("_meta", {})["place_edges_backfilled_at"] = now
    rels_payload.setdefault("_meta", {})["place_edges_backfill_script"] = "scripts/admin/backfill_place_edges.py"
    return added


def stable_dump(payload: Dict) -> str:
    # Keep a stable, readable output without re-ordering existing dict keys too aggressively.
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def run_ingest(cluster: str) -> int:
    import subprocess

    cmd = [
        "python",
        "scripts/admin/seed_neo4j_from_clusters.py",
        "--clusters",
        cluster,
        "--skip-nodes",
        "--skip-relationships",
        "--ingest-edge-arrays",
        "--edge-type",
        "place",
    ]
    return subprocess.call(cmd, cwd=str(ROOT))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cluster", help="Cluster slug (e.g., English_Reformation)")
    parser.add_argument("--ingest", action="store_true", help="Also ingest place_edges into Neo4j")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    cluster = args.cluster

    nodes_path = NODES_DIR / f"nodes.{cluster}.json"
    rels_path = RELS_DIR / f"relationships.{cluster}.json"

    if not nodes_path.exists():
        raise SystemExit(f"Missing nodes file: {nodes_path}")
    if not rels_path.exists():
        raise SystemExit(f"Missing relationships file: {rels_path}")

    nodes_payload = load_json(nodes_path)
    rels_payload = load_json(rels_path)

    event_slugs = iter_event_slugs(nodes_payload)
    if not event_slugs:
        print(f"No Event nodes found in {nodes_path}")
        return 1

    added = upsert_place_edges(rels_payload, event_slugs)
    rels_path.write_text(stable_dump(rels_payload), encoding="utf-8")

    print(f"{cluster}: added {added} place_edges (Event count: {len(event_slugs)})")

    if args.ingest:
        rc = run_ingest(cluster)
        if rc != 0:
            print("Ingest failed")
            return rc
        print("Ingest complete")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
