#!/usr/bin/env python3
"""Batch normalizer for data/nodes.json

This script finds nodes missing either 'definition' or 'description' depending on label
and updates them in manageable batches. It also renames 'aliases' -> 'alt_names' (merging
if necessary) and applies minimal governance defaults when missing. A timestamped backup
is created before the first write and before each batch write.

Usage: python3 scripts/normalize_nodes_batch.py [--batch-size N]

Default batch size: 20
"""
import json
import shutil
import datetime
import argparse
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
NODES_PATH = HERE / "data" / "nodes.json"

DEFS_LABELS = {"institution", "movement", "idea"}
DESC_LABELS = {"person", "place", "text", "event", "artifact", "evidence"}

def load_nodes(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_nodes(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def backup(path):
    ts = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    backup_path = path.with_suffix(f".bak.{ts}")
    shutil.copy2(path, backup_path)
    return backup_path

def first_nonempty(*keys, node=None):
    for k in keys:
        v = node.get(k) if node is not None else None
        if v is not None and v != "":
            return v
    return None

def normalize_node(node):
    changes = []

    # aliases -> alt_names
    if "aliases" in node:
        aliases = node.pop("aliases") or []
        if "alt_names" in node and node.get("alt_names"):
            existing = node.get("alt_names") or []
            merged = list(dict.fromkeys(existing + aliases))
            node["alt_names"] = merged
            changes.append("aliases->alt_names(merged)")
        else:
            node["alt_names"] = aliases
            changes.append("aliases->alt_names")

    label = (node.get("label") or "").lower()

    # governance defaults
    if "status" not in node:
        node["status"] = "PROPOSED"
        changes.append("status=PROPOSED")
    if "workflow_stage" not in node:
        node["workflow_stage"] = "PROPOSED"
        changes.append("workflow_stage=PROPOSED")
    if "governance_version" not in node:
        node["governance_version"] = 5
        changes.append("governance_version=5")
    if "created_at" not in node:
        node["created_at"] = "2025-11-01T00:00Z"
        changes.append("created_at=default")
    if "created_by" not in node:
        node["created_by"] = "auto_normalizer"
        changes.append("created_by=auto_normalizer")

    # label-driven definition/description rules
    if label in DEFS_LABELS:
        if not node.get("definition"):
            src = first_nonempty("description", "summary", "name", node=node)
            if src:
                node["definition"] = src if isinstance(src, str) else str(src)
                changes.append("definition_filled")
    elif label in DESC_LABELS:
        if not node.get("description"):
            src = first_nonempty("definition", "summary", "name", node=node)
            if src:
                node["description"] = src if isinstance(src, str) else str(src)
                changes.append("description_filled")

    return changes

def find_nodes_to_update(nodes):
    idxs = []
    for i, node in enumerate(nodes):
        label = (node.get("label") or "").lower()
        needs = False
        if label in DEFS_LABELS and not node.get("definition"):
            needs = True
        if label in DESC_LABELS and not node.get("description"):
            needs = True
        if "aliases" in node:
            needs = True
        if needs:
            idxs.append(i)
    return idxs

def process_in_batches(nodes, idxs, batch_size=20):
    total = len(idxs)
    updated_total = 0
    batch_no = 0
    for start in range(0, total, batch_size):
        batch_no += 1
        end = min(start + batch_size, total)
        batch_idxs = idxs[start:end]
        print(f"Processing batch {batch_no}: nodes {start+1}–{end} of {total} (count={len(batch_idxs)})")

        # backup before writing this batch
        bkp = backup(NODES_PATH)
        print(f" Backup created: {bkp}")

        batch_changes = []
        for i in batch_idxs:
            node = nodes[i]
            changes = normalize_node(node)
            if changes:
                updated_total += 1
                batch_changes.append({"slug": node.get("slug"), "changes": changes})

        # write after each batch so updates are incremental and reviewable
        save_nodes(NODES_PATH, {"_meta": data.get("_meta"), "nodes": nodes})

        print(f" Batch {batch_no} updated {len(batch_changes)} nodes")
        for c in batch_changes:
            print(f"  - {c['slug']}: {', '.join(c['changes'])}")

    print(f"Done. Updated {updated_total} nodes across {batch_no} batches.")
    return updated_total

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-size", type=int, default=20, help="Nodes per batch")
    args = parser.parse_args()

    if not NODES_PATH.exists():
        print(f"nodes file not found: {NODES_PATH}")
        raise SystemExit(2)

    data = load_nodes(NODES_PATH)
    nodes = data.get("nodes") or []

    to_update = find_nodes_to_update(nodes)
    if not to_update:
        print("No nodes require updates. Nothing to do.")
        raise SystemExit(0)

    print(f"Found {len(to_update)} nodes needing normalization. Batch size: {args.batch_size}")
    updated = process_in_batches(nodes, to_update, batch_size=args.batch_size)
    raise SystemExit(0 if updated >= 0 else 1)
