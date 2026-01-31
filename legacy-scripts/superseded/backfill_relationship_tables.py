#!/usr/bin/env python3
"""Auto-insert relationship tables into cluster README files.

For each docs/clusters/*/README.md:
- Extract parent root and interface edges.
- Parse wiring lines of the form `(Slug) REL (Slug)`.
- Consolidate all edges into a Markdown table under a `### Relationships` heading.

Intended use: run once before generating relationship JSONs so that
`scripts/admin/generate_relationships_from_readmes.py` can read the
rich tables for every cluster.
"""
from __future__ import annotations

import re
import json
from pathlib import Path
from typing import List, Tuple

ROOT = Path(__file__).resolve().parents[1]
CLUSTERS_DIR = ROOT / "docs" / "clusters"
RELATIONSHIPS_DIR = ROOT / "data" / "Relationships"

EDGE_PATTERN = re.compile(r"^\s*-\s*\(([^)]+)\)\s+([A-Z_]+)\s+\(([^)]+)\)")
PARENT_PATTERN = re.compile(r"Parent root:\s*([^\(\n]+)")


def slug_phrase(slug: str) -> str:
    return slug.replace("_", " ").replace("-", " ")


def make_description(start: str, rel_type: str, end: str) -> str:
    verb = rel_type.lower().replace("_", " ")
    sentence = f"{slug_phrase(start)} {verb} {slug_phrase(end)}.".strip()
    return sentence


def gather_existing_table_edges(text: str) -> List[Tuple[str, str, str, str]]:
    lines = text.splitlines()
    in_section = False
    in_table = False
    edges: List[Tuple[str, str, str, str]] = []

    for line in lines:
        stripped = line.strip()
        if stripped.lower() == "### relationships":
            in_section = True
            in_table = False
            continue

        if not in_section:
            continue

        if stripped.startswith("### ") and stripped.lower() != "### relationships":
            break

        if not stripped.startswith("|"):
            continue

        parts = [p.strip() for p in stripped.split("|")[1:-1]]
        if not parts:
            continue

        if all(re.match(r"^-+$", p) for p in parts):
            in_table = True
            continue

        if parts[0].lower() in ("start", "") or not in_table:
            continue

        while len(parts) < 4:
            parts.append("")

        start, rel_type, end, desc = parts[:4]
        if start and rel_type and end:
            edges.append((start, rel_type, end, desc))

    return edges


def gather_relationship_json_edges(cluster_slug: str) -> List[Tuple[str, str, str, str]]:
    path = RELATIONSHIPS_DIR / f"relationships.{cluster_slug}.json"
    if not path.exists():
        return []

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

    edges: List[Tuple[str, str, str, str]] = []
    for rel in data.get("relationships", []):
        start = rel.get("start_slug")
        rel_type = rel.get("type")
        end = rel.get("end_slug")
        desc = rel.get("description", "")
        if start and rel_type and end:
            edges.append((start, rel_type, end, desc or ""))

    return edges


def gather_parent_edge(text: str, cluster_slug: str) -> List[Tuple[str, str, str, str]]:
    match = PARENT_PATTERN.search(text)
    if not match:
        return []
    parent = match.group(1).strip()
    desc = f"{slug_phrase(cluster_slug)} has parent root {slug_phrase(parent)}."
    return [(cluster_slug, "IS_PART_OF", parent, desc)]


def gather_interface_edges(text: str, cluster_slug: str) -> List[Tuple[str, str, str, str]]:
    edges: List[Tuple[str, str, str, str]] = []
    interfaces_section = False
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not interfaces_section:
            if re.search(r"Interfaces to other clusters", line, re.I):
                interfaces_section = True
            continue
        if not line:
            break
        match = re.match(r"-\s*([A-Za-z0-9_\-]+)", line)
        if match:
            target = match.group(1)
            desc = f"{slug_phrase(cluster_slug)} interfaces with {slug_phrase(target)}."
            edges.append((cluster_slug, "INTERFACES_WITH", target, desc))
    return edges


def gather_wiring_edges(text: str) -> List[Tuple[str, str, str, str]]:
    edges: List[Tuple[str, str, str, str]] = []
    for line in text.splitlines():
        match = EDGE_PATTERN.match(line)
        if not match:
            continue
        start, rel_type, end = (part.strip() for part in match.groups())
        desc = make_description(start, rel_type, end)
        edges.append((start, rel_type, end, desc))
    return edges


def remove_existing_table(lines: List[str]) -> List[str]:
    start_idx = None
    for idx, line in enumerate(lines):
        if line.strip().lower() == "### relationships":
            start_idx = idx
            break
    if start_idx is None:
        return lines
    end_idx = start_idx + 1
    while end_idx < len(lines):
        stripped = lines[end_idx].strip()
        if stripped.startswith("### ") or stripped.startswith("## "):
            break
        end_idx += 1
    return lines[:start_idx] + lines[end_idx:]


def render_table(edges: List[Tuple[str, str, str, str]]) -> List[str]:
    if not edges:
        return []
    rows = ["### Relationships", "",
            "_Auto-generated from wiring; edit freely for nuance._", "",
            "| Start | Type | End | Description |",
            "| ----- | ---- | --- | ----------- |"]
    for start, rel_type, end, desc in edges:
        safe_desc = desc.replace("|", "\\|")
        rows.append(f"| {start} | {rel_type} | {end} | {safe_desc} |")
    rows.append("")
    return rows


def prioritize_edges(edges: List[Tuple[str, str, str, str]], cluster_slug: str) -> List[Tuple[str, str, str, str]]:
    indexed = list(enumerate(edges))

    def sort_key(item):
        idx, (start, rel_type, _end, _desc) = item
        if start == cluster_slug and rel_type == "IS_PART_OF":
            return (0, idx)
        if start == cluster_slug and rel_type == "INTERFACES_WITH":
            return (1, idx)
        return (2, idx)

    indexed.sort(key=sort_key)
    return [edge for _, edge in indexed]


def insert_table(lines: List[str], table_lines: List[str]) -> List[str]:
    if not table_lines:
        return lines
    insert_idx = 1
    while insert_idx < len(lines) and lines[insert_idx].strip() == "":
        insert_idx += 1
    before = lines[:insert_idx]
    after = lines[insert_idx:]
    return before + table_lines + after


def process_readme(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    cluster_slug = path.parent.name

    edges = []
    seen = set()

    for edge in gather_existing_table_edges(text):
        if edge[:3] not in seen:
            edges.append(edge)
            seen.add(edge[:3])

    for edge in gather_relationship_json_edges(cluster_slug):
        if edge[:3] not in seen:
            edges.append(edge)
            seen.add(edge[:3])

    for edge in gather_parent_edge(text, cluster_slug):
        if edge[:3] not in seen:
            edges.append(edge)
            seen.add(edge[:3])

    for edge in gather_interface_edges(text, cluster_slug):
        if edge[:3] not in seen:
            edges.append(edge)
            seen.add(edge[:3])

    for edge in gather_wiring_edges(text):
        if edge[:3] not in seen:
            edges.append(edge)
            seen.add(edge[:3])

    if not edges:
        return False

    edges = prioritize_edges(edges, cluster_slug)

    lines = text.splitlines()
    lines = remove_existing_table(lines)
    new_lines = insert_table(lines, render_table(edges))
    new_text = "\n".join(new_lines)
    if not new_text.endswith("\n"):
        new_text += "\n"
    path.write_text(new_text, encoding="utf-8")
    return True


def main():
    if not CLUSTERS_DIR.exists():
        raise SystemExit(f"Clusters directory not found: {CLUSTERS_DIR}")

    readmes = sorted(CLUSTERS_DIR.glob("*/README.md"))
    updated = 0
    for readme in readmes:
        changed = process_readme(readme)
        if changed:
            print(f"Updated relationships table: {readme.relative_to(ROOT)}")
            updated += 1
    print(f"Done. Updated {updated}/{len(readmes)} cluster README files.")


if __name__ == "__main__":
    main()
