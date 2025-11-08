#!/usr/bin/env python3
"""Update node descriptions in data/Nodes/nodes.json using docs/nodes/node-description.md

Conservative rules:
- If a node's description is missing, equals the node's name, or is very short, try to replace it.
- Prefer the curated description from `node-description.md` when available.
- Otherwise prefer `summary`, then `definition`.

Creates a timestamped backup and prints a short report (count + samples).
"""
import json
import shutil
import datetime
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent.parent
NODES_PATH = HERE / "data" / "Nodes" / "nodes.json"
DOC_PATH = HERE / "docs" / "nodes" / "node-description.md"

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def backup(path):
    ts = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    bp = path.with_suffix(f".bak.{ts}")
    shutil.copy2(path, bp)
    return bp

def parse_description_doc(path):
    mapping = {}
    if not path.exists():
        return mapping
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # table rows look like: | Miles_Coverdale | C | Editor/translator of English Bibles. | English_Reformation |
            if not line.startswith("|"):
                continue
            parts = [p.strip() for p in line.split("|")]
            # expect at least 4 columns: empty, Node, G/C, Description, ...
            if len(parts) < 4:
                continue
            node = parts[1]
            desc = parts[3]
            # skip header/separator rows
            if node.lower() in ("node", "---"):
                continue
            if re.match(r'^[-\s]+$', desc):
                continue
            if node:
                key = node.lower()
                mapping[key] = desc
    return mapping

def is_poor_description(node):
    name = (node.get("name") or "").strip()
    desc = (node.get("description") or "").strip()
    if not desc:
        return True
    # if description equals name (case-insensitive) or is very short < 15 chars
    if desc.lower() == name.lower():
        return True
    if len(desc) < 15:
        return True
    return False

def main():
    if not NODES_PATH.exists():
        print("nodes file not found")
        return 2
    data = load_json(NODES_PATH)
    nodes = data.get("nodes") or []

    mapping = parse_description_doc(DOC_PATH)

    bkp = backup(NODES_PATH)
    print(f"Backup created: {bkp}")

    updated = []
    for node in nodes:
        try:
            slug = node.get("slug") or ""
            key = slug.replace("-", "_").lower()
            if is_poor_description(node):
                # try mapping from doc
                mapped = mapping.get(key) or mapping.get(slug.lower())
                if mapped:
                    node["description"] = mapped
                    updated.append((slug, "from_doc"))
                    continue
                # try summary
                if node.get("summary") and len(node.get("summary")) >= 15:
                    node["description"] = node.get("summary")
                    updated.append((slug, "from_summary"))
                    continue
                # try definition
                if node.get("definition") and len(node.get("definition")) >= 15:
                    node["description"] = node.get("definition")
                    updated.append((slug, "from_definition"))
                    continue
                # fallback: leave as-is but mark
                # (We avoid writing trivial names as description)
        except Exception:
            continue

    if updated:
        data["nodes"] = nodes
        save_json(NODES_PATH, data)

    print(f"Processed {len(nodes)} nodes. Updated {len(updated)} nodes.")
    for s, reason in updated[:30]:
        print(f" - {s}: {reason}")

    return 0

if __name__ == '__main__':
    raise SystemExit(main())
