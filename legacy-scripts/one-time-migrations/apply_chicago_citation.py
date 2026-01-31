#!/usr/bin/env python3
"""Script: set citation_style to 'Chicago 17' for relationships JSON files.
Targets: data/Relationships/relationships.English_Reformation.json
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
RELS = ROOT / "data" / "Relationships" / "relationships.English_Reformation.json"

print(f"Loading {RELS}")

data = json.loads(RELS.read_text(encoding="utf-8"))
rels = data.get("relationships", [])
changed = 0
for r in rels:
    if r.get("citation_style") is None or r.get("citation_style") == "":
        r["citation_style"] = "Chicago 17"
        changed += 1

if changed:
    RELS.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

print(f"Updated {changed} relationships with citation_style='Chicago 17'.")
