#!/usr/bin/env python3
"""Migrate P↔P marriage edges into Marriage event nodes.

Project policy:
- Do NOT model marriage as a directional P→P relationship (it is symmetric and carries rich metadata).
- Model marriage as an :Event (kind="Marriage") and link spouses via PARTICIPATES_IN edges.

This script updates seed files (JSON) in-place:
- data/Relationships/relationships.<Cluster>.json: removes type=="MARRIES" relationships, adds PARTICIPATES_IN relationships to a Marriage event.
- data/Nodes/nodes.<Cluster>.json: adds new :Event nodes for the marriage events.
- Adds timeframe_edges for the Marriage events using the cluster’s dominant timeframe division.

Usage:
  python scripts/migrate_marriages_to_events.py English_Reformation --dry-run
  python scripts/migrate_marriages_to_events.py English_Reformation

Notes:
- Marriage event slugs are canonicalized by lexicographic spouse slug order:
    Marriage_<A>_<B> where A < B
  This prevents duplicates and avoids gendered direction rules.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


TIMEFRAMES: Dict[int, Dict[str, str]] = {
    910: {"slug": "910_Prehistoric", "name": "Prehistoric"},
    920: {"slug": "920_Classical", "name": "Classical"},
    930: {"slug": "930_Medieval", "name": "Medieval"},
    940: {"slug": "940_Early_Modern", "name": "Early Modern"},
    950: {"slug": "950_Modern", "name": "Modern"},
    960: {"slug": "960_Contemporary", "name": "Contemporary"},
}


@dataclass(frozen=True)
class MarriagePair:
    a: str
    b: str

    @staticmethod
    def from_slugs(s1: str, s2: str) -> "MarriagePair":
        if s1 <= s2:
            return MarriagePair(a=s1, b=s2)
        return MarriagePair(a=s2, b=s1)

    @property
    def event_slug(self) -> str:
        return f"Marriage_{self.a}_{self.b}"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, data: Dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def dominant_timeframe_division(rels_data: Dict[str, Any]) -> Optional[int]:
    tf = rels_data.get("timeframe_edges", [])
    if not isinstance(tf, list) or not tf:
        return None
    divisions = []
    for e in tf:
        if not isinstance(e, dict):
            continue
        d = e.get("division")
        if not isinstance(d, int):
            d = e.get("timeframe_division")
        if isinstance(d, int):
            divisions.append(d)
    divisions = [d for d in divisions if isinstance(d, int)]
    if not divisions:
        return None
    return Counter(divisions).most_common(1)[0][0]


def normalize_timeframe_edges(rels_data: Dict[str, Any]) -> None:
    tf = rels_data.get("timeframe_edges")
    if tf is None:
        return
    if not isinstance(tf, list):
        rels_data["timeframe_edges"] = []
        return

    for e in tf:
        if not isinstance(e, dict):
            continue
        # Normalize legacy key: timeframe_division -> division
        if "division" not in e and isinstance(e.get("timeframe_division"), int):
            e["division"] = e["timeframe_division"]
        if "timeframe_division" in e:
            e.pop("timeframe_division", None)

        division = e.get("division")
        if not isinstance(division, int) or division not in TIMEFRAMES:
            continue
        e.setdefault("timeframe_slug", TIMEFRAMES[division]["slug"])
        e.setdefault("timeframe_name", TIMEFRAMES[division]["name"])


def make_marriage_event_node(
    cluster: str,
    pair: MarriagePair,
    source_rel: Dict[str, Any],
) -> Dict[str, Any]:
    description = source_rel.get("description") or f"Marriage between {pair.a} and {pair.b}."
    return {
        "slug": pair.event_slug,
        "name": f"Marriage: {pair.a} × {pair.b}",
        "label": "Event",
        "kind": "Marriage",
        "cluster": cluster,
        "status": source_rel.get("status", "PROPOSED"),
        "workflow_stage": source_rel.get("status", "PROPOSED"),
        "created_at": utc_now_iso(),
        "created_by": "migrate_marriages_to_events.py",
        "description": description,
        # Preserve review metadata if present
        "reviewed_at": source_rel.get("reviewed_at"),
        "reviewed_by": source_rel.get("reviewed_by"),
    }


def make_participates_in_rel(
    rel_id: int,
    spouse_slug: str,
    marriage_event_slug: str,
    source_rel: Dict[str, Any],
) -> Dict[str, Any]:
    # Copy citation/evidence fields forward so the new edges remain evidence-backed.
    payload: Dict[str, Any] = {
        "id": rel_id,
        "start_slug": spouse_slug,
        "end_slug": marriage_event_slug,
        "type": "PARTICIPATES_IN",
        "role": "spouse",
        "description": f"{spouse_slug} participated as a spouse in {marriage_event_slug}.",
        "status": source_rel.get("status", "PROPOSED"),
        "evidence_url": source_rel.get("evidence_url"),
        "citation_style": source_rel.get("citation_style", "Chicago 17"),
        "page_refs": source_rel.get("page_refs", "passim"),
        "source_note": source_rel.get("source_note", "migrated: marriage-as-event"),
        "inline_evidence": source_rel.get("inline_evidence", False),
        "evidence_slug": source_rel.get("evidence_slug"),
        "reviewed_at": source_rel.get("reviewed_at"),
        "reviewed_by": source_rel.get("reviewed_by"),
    }
    return payload


def ensure_timeframe_edge(
    rels_data: Dict[str, Any],
    node_slug: str,
    division: int,
) -> bool:
    tf = rels_data.setdefault("timeframe_edges", [])
    if not isinstance(tf, list):
        rels_data["timeframe_edges"] = []
        tf = rels_data["timeframe_edges"]

    normalize_timeframe_edges(rels_data)

    existing = any(
        isinstance(e, dict)
        and e.get("node_slug") == node_slug
        and e.get("division") == division
        for e in tf
    )
    if existing:
        return False

    timeframe = TIMEFRAMES.get(division, {"slug": f"{division}_Unknown", "name": "Unknown"})
    tf.append({
        "node_slug": node_slug,
        "timeframe_slug": timeframe["slug"],
        "division": division,
        "timeframe_name": timeframe["name"],
    })
    return True


def migrate_cluster(cluster: str, dry_run: bool) -> None:
    repo = Path(__file__).resolve().parent.parent
    nodes_path = repo / "data" / "Nodes" / f"nodes.{cluster}.json"
    rels_path = repo / "data" / "Relationships" / f"relationships.{cluster}.json"

    if not nodes_path.exists():
        raise SystemExit(f"Nodes file not found: {nodes_path}")
    if not rels_path.exists():
        raise SystemExit(f"Relationships file not found: {rels_path}")

    nodes_data = load_json(nodes_path)
    rels_data = load_json(rels_path)

    if not isinstance(nodes_data, dict):
        raise SystemExit(f"Invalid nodes file format (expected object): {nodes_path}")
    if not isinstance(rels_data, dict):
        raise SystemExit(f"Invalid relationships file format (expected object): {rels_path}")

    nodes_raw = nodes_data.get("nodes", [])
    rels_raw = rels_data.get("relationships", [])
    if not isinstance(nodes_raw, list):
        raise SystemExit(f"Invalid nodes file format (expected nodes[] array): {nodes_path}")
    if not isinstance(rels_raw, list):
        raise SystemExit(f"Invalid relationships file format (expected relationships[] array): {rels_path}")

    nodes: List[Dict[str, Any]] = nodes_raw
    relationships: List[Dict[str, Any]] = rels_raw

    normalize_timeframe_edges(rels_data)

    marriages = [r for r in relationships if r.get("type") == "MARRIES"]
    if not marriages:
        print(f"No MARRIES relationships found in {cluster}; nothing to do.")
        return

    # Determine next relationship id.
    max_id = 0
    for r in relationships:
        rid = r.get("id")
        if isinstance(rid, int) and rid > max_id:
            max_id = rid

    # Determine dominant timeframe division for the cluster.
    division = dominant_timeframe_division(rels_data) or 940

    # Build marriage pairs; pick a canonical source_rel per pair (prefer one with a description).
    by_pair: Dict[MarriagePair, Dict[str, Any]] = {}
    for r in marriages:
        s1, s2 = r.get("start_slug"), r.get("end_slug")
        if not s1 or not s2:
            continue
        pair = MarriagePair.from_slugs(str(s1), str(s2))
        if pair not in by_pair:
            by_pair[pair] = r
        else:
            # Prefer one with a longer description.
            if len(str(r.get("description") or "")) > len(str(by_pair[pair].get("description") or "")):
                by_pair[pair] = r

    existing_node_slugs = {n.get("slug") for n in nodes if isinstance(n, dict)}

    added_nodes = 0
    added_rels = 0
    added_tf = 0

    # Remove all MARRIES relationships.
    relationships_kept = [r for r in relationships if r.get("type") != "MARRIES"]

    for pair, source_rel in sorted(by_pair.items(), key=lambda kv: kv[0].event_slug):
        event_slug = pair.event_slug

        # Add marriage event node if missing.
        if event_slug not in existing_node_slugs:
            nodes.append(make_marriage_event_node(cluster, pair, source_rel))
            existing_node_slugs.add(event_slug)
            added_nodes += 1

        # Add two PARTICIPATES_IN edges (spouse -> marriage_event).
        max_id += 1
        relationships_kept.append(make_participates_in_rel(max_id, pair.a, event_slug, source_rel))
        max_id += 1
        relationships_kept.append(make_participates_in_rel(max_id, pair.b, event_slug, source_rel))
        added_rels += 2

        # Add timeframe edge for the marriage event.
        if ensure_timeframe_edge(rels_data, event_slug, division):
            added_tf += 1

    # Update meta
    nodes_data.setdefault("_meta", {})["marriage_migration"] = {
        "migrated_at": utc_now_iso(),
        "script": "scripts/migrate_marriages_to_events.py",
        "cluster": cluster,
        "added_event_nodes": added_nodes,
        "added_participates_in_relationships": added_rels,
        "removed_marries_relationships": len(marriages),
    }
    rels_data.setdefault("_meta", {})["marriage_migration"] = nodes_data["_meta"]["marriage_migration"]

    rels_data["relationships"] = relationships_kept

    print(f"Cluster {cluster}:")
    print(f"  Removed MARRIES relationships: {len(marriages)}")
    print(f"  Added Marriage event nodes: {added_nodes}")
    print(f"  Added PARTICIPATES_IN relationships: {added_rels}")
    print(f"  Added timeframe_edges for marriages: {added_tf} (division {division})")

    if dry_run:
        print("[DRY RUN] No files written.")
        return

    write_json(nodes_path, nodes_data)
    write_json(rels_path, rels_data)


def main() -> None:
    parser = argparse.ArgumentParser(description="Migrate MARRIES edges to Marriage event modeling.")
    parser.add_argument("cluster", help="Cluster name (e.g., English_Reformation)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    migrate_cluster(args.cluster, args.dry_run)


if __name__ == "__main__":
    main()
