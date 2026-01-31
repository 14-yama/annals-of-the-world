#!/usr/bin/env python3
"""Normalize the relationships markdown table in a cluster README and
ensure every row has the citation columns, setting Citation Style to
'Chicago 17' where empty.

Targets: docs/clusters/English_Reformation/README.md
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "docs" / "clusters" / "English_Reformation" / "README.md"
print(f"Processing {README}")
text = README.read_text(encoding="utf-8")
lines = text.splitlines()
out_lines = []
in_table = False
header_seen = False

for i, line in enumerate(lines):
    if not in_table:
        out_lines.append(line)
        # identify table header by Start | Type | End | Description
        if line.strip().lower().startswith("| start | type | end | description"):
            in_table = True
            header_seen = True
            # replace header with 8-column header (Citation Style column named)
            out_lines[-1] = "| Start | Type | End | Description | Evidence URL | Citation Style (Chicago 17) | Page Refs | Source Note |"
            # next line should be separator, we'll handle in next iteration
    else:
        # inside table: continue until a blank line or a line not starting with '|'
        if not line.strip() or not line.lstrip().startswith("|"):
            in_table = False
            out_lines.append(line)
            continue

        # handle separator row like | --- | --- | ... |
        if set(line.strip()) <= set("|- :"):
            # produce a separator with 8 columns
            sep = "| ----- | ---- | --- | ----------- | ------------ | ------------------------- | --------- | ----------- |"
            out_lines.append(sep)
            continue

        # normal table row: split into columns
        parts = [p.strip() for p in line.split("|")]
        # split produces leading and trailing empty strings because of leading/trailing '|'
        # keep interior columns
        if parts and parts[0] == "":
            parts = parts[1:]
        if parts and parts[-1] == "":
            parts = parts[:-1]

        # parts is list of current columns; we want 8 columns
        # ensure length >=4 (Start,Type,End,Description) otherwise skip
        if len(parts) < 4:
            # preserve as-is
            out_lines.append(line)
            continue

        # Expand to required 8 columns
        while len(parts) < 8:
            parts.append("")

        # set Citation Style column (index 5 -> 6th column if 0-based) if empty
        # Column order: 0=Start,1=Type,2=End,3=Description,4=Evidence URL,5=Citation Style,6=Page Refs,7=Source Note
        if not parts[5]:
            parts[5] = "Chicago 17"

        # Reconstruct the row with a single space padding
        new_row = "| " + " | ".join(parts) + " |"
        out_lines.append(new_row)

# write back
new_text = "\n".join(out_lines) + "\n"
README.write_text(new_text, encoding="utf-8")
print("README table normalized and Citation Style filled.")
