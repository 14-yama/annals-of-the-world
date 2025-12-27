#!/usr/bin/env python3
"""Normalize per-cluster node JSON files under data/Nodes/

This script:
- Iterates all JSON files in `data/Nodes/` (skips backups)
- Normalizes node `label` values to canonical labels (e.g., Concept -> Idea)
- Ensures governance defaults: status, workflow_stage, governance_version, created_at, created_by
- Ensures `definition` exists for Idea/Institution/Movement and `description` exists for Person/Place/Text/Event/Artifact/Evidence
- Creates timestamped backups before writing changes

Usage:
  python3 scripts/admin/normalize_nodes_all_clusters.py [--dry-run]
"""
import json
import shutil
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NODES_DIR = ROOT / "data" / "Nodes"

CANONICAL_LABELS = {
    "person": "Person",
    "institution": "Institution",
    "movement": "Movement",
    "event": "Event",
    "place": "Place",
    "text": "Text",
    "artifact": "Artifact",
    "evidence": "Evidence",
    "corpus": "Corpus",
    "timeframe": "Timeframe",
    "framework": "Framework",
    "idea": "Idea",
    "concept": "Idea",
}

DEFS_LABELS = {"Idea", "Institution", "Movement"}
DESC_LABELS = {"Person", "Place", "Text", "Event", "Artifact", "Evidence"}


def backup(path: Path) -> Path:
    ts = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    bkp = path.with_suffix(path.suffix + f".bak.{ts}")
    shutil.copy2(path, bkp)
    return bkp


def first_nonempty(node, *keys):
    for k in keys:
        v = node.get(k)
        if v is not None and v != "":
            return v
    return None


def load_cluster_readme_mappings(readme_path: Path) -> dict:
    """Parse cluster README to extract groupings like 'Persons (P): A; B; C' and return slug->label map."""
    text = readme_path.read_text(encoding='utf-8')
    lines = text.splitlines()
    mapping = {}

    # group name -> canonical label
    group_map = {
        'persons': 'Person',
        'institutions': 'Institution',
        'texts': 'Text',
        'movements': 'Movement',
        'events': 'Event',
        'places': 'Place',
        'periods': 'Timeframe',
    }

    import re

    # pattern for inline group lines like '- Persons (P): Henry_VIII; Catherine_of_Aragon;'
    grp_re = re.compile(r'^[\-\*\s]*?(?P<group>Persons|Institutions|Texts|Movements|Events|Places|Periods)\s*\([^)]*\):\s*(?P<items>.+)$', re.IGNORECASE)

    for ln in lines:
        m = grp_re.match(ln.strip())
        if not m:
            continue
        group = m.group('group').lower()
        items = m.group('items')
        # split by semicolon or comma
        parts = [p.strip() for p in re.split(r'[;|,]', items) if p.strip()]
        for p in parts:
            # extract slug-like token (allow underscores, hyphens, alphanum)
            slug_match = re.search(r'([A-Za-z0-9_\-\(\)]+)', p)
            if not slug_match:
                continue
            slug = slug_match.group(1).strip()
            # normalize trailing parentheses removal if present
            slug = slug.strip()
            label = group_map.get(group, None)
            if label:
                mapping[slug] = label

    # also try to parse simple Nodes table (| Node | G/C | ...)
    table_start = None
    for i, ln in enumerate(lines):
        if ln.strip().lower().startswith('| node |'):
            table_start = i
            break
    if table_start is not None:
        # process subsequent table rows
        for ln in lines[table_start+1:]:
            if not ln.strip().startswith('|'):
                break
            cols = [c.strip() for c in ln.split('|')[1:]]
            if not cols:
                continue
            slug = cols[0]
            if slug and slug != '-----':
                # if mapping doesn't already have it, leave label detection to normalizer
                if slug not in mapping:
                    # attempt to infer label from G/C column if present (cols[1])
                    gcol = cols[1] if len(cols) > 1 else ''
                    if gcol:
                        # Interpret codes: C -> Idea, P -> Person, I -> Institution, T -> Text, M -> Movement, E -> Event, L -> Place
                        code_map = {'c': 'Idea', 'p': 'Person', 'i': 'Institution', 't': 'Text', 'm': 'Movement', 'e': 'Event', 'l': 'Place'}
                        code = gcol.strip().lower()
                        if code in code_map:
                            mapping[slug] = code_map[code]

    return mapping


def normalize_node(node):
    changes = []

    # Standardize label
    raw_label = (node.get("label") or node.get("type") or "").strip()
    key = raw_label.lower()
    new_label = CANONICAL_LABELS.get(key)
    if not new_label:
        # If no label or unknown, default to Idea
        if not raw_label:
            new_label = "Idea"
            changes.append("label: missing -> Idea")
        else:
            # Preserve unknown but normalize capitalization
            new_label = raw_label.capitalize()
            if new_label != raw_label:
                changes.append(f"label: {raw_label} -> {new_label}")

    if node.get("label") != new_label:
        node["label"] = new_label
        if f"label: set -> {new_label}" not in changes:
            changes.append(f"label_set:{new_label}")

    label = node.get("label")

    # Governance defaults
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
        node["created_at"] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%MZ")
        changes.append("created_at=default")
    if "created_by" not in node:
        node["created_by"] = "auto_normalizer"
        changes.append("created_by=auto_normalizer")

    # Label-driven fields
    if label in DEFS_LABELS:
        if not node.get("definition"):
            src = first_nonempty(node, "description", "summary", "name")
            if src:
                node["definition"] = src
                changes.append("definition_filled")
    elif label in DESC_LABELS:
        if not node.get("description"):
            src = first_nonempty(node, "definition", "summary", "name")
            if src:
                node["description"] = src
                changes.append("description_filled")

    return changes


def process_file(path: Path, dry_run: bool = False):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Skipping {path.name}: parse error: {e}")
        return {"file": path.name, "error": str(e)}

    # attempt to load README cluster mapping to prefer canonical labels
    cluster = None
    m = path.name
    if m.startswith('nodes.') and m.endswith('.json'):
        cluster = m.replace('nodes.', '').replace('.json', '')
    cluster_map = {}
    if cluster:
        cluster_readme = Path(ROOT) / 'docs' / 'clusters' / cluster / 'README.md'
        if cluster_readme.exists():
            try:
                cluster_map = load_cluster_readme_mappings(cluster_readme)
            except Exception:
                cluster_map = {}

    nodes = data.get("nodes") or []
    total = len(nodes)
    changed_count = 0
    unknown_labels = set()
    samples = []

    for node in nodes:
        before = node.get("label")
        # if README provides a label for this slug, force it
        slug = node.get('slug')
        if slug and slug in cluster_map:
            target = cluster_map[slug]
            # map to canonical if possible
            mapped = CANONICAL_LABELS.get(target.lower(), target)
            if node.get('label') != mapped:
                node['label'] = mapped
                # ensure we still apply other normalizations
        changes = normalize_node(node)
        if changes:
            changed_count += 1
            samples.append({"slug": node.get("slug"), "changes": changes})
        # record any label not in canonical set
        lab = node.get("label")
        if lab and lab not in CANONICAL_LABELS.values():
            unknown_labels.add(lab)

    if changed_count and not dry_run:
        bkp = backup(path)
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"{path.name}: updated {changed_count}/{total} nodes (backup: {bkp.name})")
    elif changed_count:
        print(f"{path.name}: would update {changed_count}/{total} nodes (dry-run)")
    else:
        print(f"{path.name}: no changes needed ({total} nodes)")

    return {"file": path.name, "total": total, "changed": changed_count, "unknown_labels": sorted(list(unknown_labels)), "samples": samples[:5]}


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Show changes without writing")
    args = parser.parse_args()

    if not NODES_DIR.exists():
        print("Nodes directory not found; aborting.")
        return 1

    reports = []
    for p in sorted(NODES_DIR.iterdir()):
        if p.suffix != '.json' or 'bak' in p.name:
            continue
        r = process_file(p, dry_run=args.dry_run)
        reports.append(r)

    # Summary
    total_files = len(reports)
    total_changed = sum(r.get('changed', 0) for r in reports if isinstance(r, dict))
    total_nodes = sum(r.get('total', 0) for r in reports if isinstance(r, dict))
    print(f"\nSummary: processed {total_files} files, {total_changed} nodes changed of {total_nodes} total nodes")
    # show files with unknown labels
    files_with_unknowns = [r for r in reports if r.get('unknown_labels')]
    if files_with_unknowns:
        print("Files with non-canonical labels:")
        for r in files_with_unknowns:
            print(f" - {r['file']}: {', '.join(r['unknown_labels'])}")

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
