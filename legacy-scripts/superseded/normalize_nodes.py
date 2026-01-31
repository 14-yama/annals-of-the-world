#!/usr/bin/env python3
"""Conservative normalizer for data/Nodes/nodes.json

Idempotent, safe changes:
- rename 'aliases' -> 'alt_names' (merge when both exist)
- for labels Institution/Movement/Idea: ensure 'definition' exists (copy from description/summary/name)
- for labels Person/Place/Text/Event/Artifact/Evidence: ensure 'description' exists (copy from definition/summary/name)
- set minimal governance defaults when missing: status, workflow_stage, governance_version, created_at, created_by

Creates a timestamped backup of the original file before writing.
Prints a summary of counts and a few sample changed nodes.
"""
import json
import shutil
import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
NODES_PATH = HERE / "data" / "Nodes" / "nodes.json"

DEFS_LABELS = {"institution", "movement", "idea"}
DESC_LABELS = {"person", "place", "text", "event", "artifact", "evidence"}

def load_nodes(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_nodes(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=False)

def backup(path):
    ts = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    backup_path = path.with_suffix(f".bak.{ts}")
    shutil.copy2(path, backup_path)
    return backup_path

def first_nonempty(*keys, node=None):
    for k in keys:
        v = node.get(k)
        if v is not None and v != "":
            return v
    return None

def normalize_node(node):
    changed = []

    # aliases -> alt_names
    if "aliases" in node:
        aliases = node.pop("aliases")
        if aliases is None:
            aliases = []
        # if alt_names exists, merge
        if "alt_names" in node and node.get("alt_names"):
            existing = node.get("alt_names") or []
            merged = list(dict.fromkeys(existing + aliases))
            node["alt_names"] = merged
            changed.append("aliases->alt_names(merged)")
        else:
            node["alt_names"] = aliases
            changed.append("aliases->alt_names")

    label = (node.get("label") or "").lower()

    # governance defaults
    if "status" not in node:
        node["status"] = "PROPOSED"
        changed.append("status=PROPOSED")
    if "workflow_stage" not in node:
        node["workflow_stage"] = "PROPOSED"
        changed.append("workflow_stage=PROPOSED")
    if "governance_version" not in node:
        node["governance_version"] = 5
        changed.append("governance_version=5")
    if "created_at" not in node:
        node["created_at"] = "2025-11-01T00:00Z"
        changed.append("created_at=default")
    if "created_by" not in node:
        node["created_by"] = "auto_normalizer"
        changed.append("created_by=auto_normalizer")

    # label-driven definition/description rules
    if label in DEFS_LABELS:
        if not node.get("definition"):
            src = first_nonempty("description", "summary", "name", node=node)
            if src:
                node["definition"] = (src if isinstance(src, str) else str(src))
                changed.append("definition_filled")
    elif label in DESC_LABELS:
        if not node.get("description"):
            src = first_nonempty("definition", "summary", "name", node=node)
            if src:
                node["description"] = (src if isinstance(src, str) else str(src))
                changed.append("description_filled")

    return changed

def main():
    if not NODES_PATH.exists():
        print(f"nodes file not found: {NODES_PATH} (skipping)")
        return 0

    data = load_nodes(NODES_PATH)
    nodes = data.get("nodes") or []

    # backup
    bkp = backup(NODES_PATH)
    print(f"Backup created: {bkp}")

    total = len(nodes)
    updated = 0
    samples = []

    for node in nodes:
        changes = normalize_node(node)
        if changes:
            updated += 1
            samples.append({"slug": node.get("slug"), "changes": changes})

    # write back
    data["nodes"] = nodes
    save_nodes(NODES_PATH, data)

    print(f"Processed {total} nodes. Updated: {updated}")
    if updated:
        print("Sample updates (up to 10):")
        for s in samples[:10]:
            print(f" - {s['slug']}: {', '.join(s['changes'])}")

    return 0

if __name__ == '__main__':
    raise SystemExit(main())
