#!/usr/bin/env python3
"""Normalize cluster README relationship and node tables.

For each README in docs/clusters/*/README.md:
- Find the relationships table header (Start | Type | End | Description)
- Normalize it to include these columns:
  Start | Type | End | Description | Evidence URL | Citation Style (Chicago 17) | Page Refs | Source Note
- Ensure separator row matches 8 cols.
- For every relationship row, expand to 8 cols and set Citation Style to "Chicago 17" if empty.
- If a 'Node' row appears inside the relationships table (e.g. a row starting with '| Node |'), treat that and the following rows as Nodes:
  - Create a new section '### Nodes' and a 3-col table: Node | G/C | Description
  - Populate the nodes table from those rows (dropping extra citation columns)
- Preserve other content outside the tables.

This script is conservative: if a README lacks a relationships table the script will skip it.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
CLUSTERS = ROOT / 'docs' / 'clusters'

def process_readme(path: Path):
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines()
    out = []
    i = 0
    n = len(lines)
    changed = False

    # find relationships table header
    while i < n:
        line = lines[i]
        lower = line.strip().lower()
        if lower.startswith('| start | type | end | description'):
            # start processing table
            changed = True
            # write standardized header
            out.append('| Start | Type | End | Description | Evidence URL | Citation Style (Chicago 17) | Page Refs | Source Note |')
            out.append('| ----- | ---- | --- | ----------- | ------------ | ------------------------- | --------- | ----------- |')
            i += 1
            # iterate rows until non-table or marker for nodes
            while i < n:
                row = lines[i]
                if not row.strip().startswith('|'):
                    # end of table
                    break
                # detect if this is the embedded Node marker row
                # e.g. a row with first column 'Node' (case-insensitive)
                cols = [c.strip() for c in row.split('|')]
                # trim leading/trailing empties
                if cols and cols[0] == '':
                    cols = cols[1:]
                if cols and cols[-1] == '':
                    cols = cols[:-1]
                if len(cols) >= 1 and cols[0].lower() == 'node':
                    # stop relationships table and hand off to node table processing
                    break
                # otherwise, normalize relationship row to 8 columns
                # ensure at least 4 columns present
                if len(cols) < 4:
                    # preserve as-is (keep row)
                    i += 1
                    continue
                # expand to 8
                while len(cols) < 8:
                    cols.append('')
                # set citation style if empty
                if not cols[5]:
                    cols[5] = 'Chicago 17'
                # reconstruct
                new_row = '| ' + ' | '.join(cols) + ' |'
                out.append(new_row)
                i += 1
            # now i is at first non-table or node marker
            # continue outer loop without incrementing i (so next block is processed normally)
            continue
        else:
            out.append(line)
            i += 1
    # if change occurred, we may still need to extract Node rows that were inside old table
    if changed:
        # We'll now extract any lines that previously contained '| Node |' etc.
        # Simple pass: find the first occurrence of a line with '| Node |' or a line that is a node header variant
        final_text = '\n'.join(out) + '\n'
        # Now detect any remaining node rows still appearing in the text in older format
        # We'll search original text for the pattern '\n| Node |' and capture following table rows until a blank line
        node_block = []
        m = re.search(r"\n\|\s*Node\s*\|[\s\S]*?(?:\n\n|\n## |\Z)", text, flags=re.IGNORECASE)
        if m:
            block = m.group(0)
            # split into lines, skip the header if present
            blines = block.strip().splitlines()
            # remove any header/separator if present at start
            # find first real node row (skip header-like lines)
            node_rows = []
            for l in blines:
                if not l.strip().startswith('|'):
                    continue
                cols = [c.strip() for c in l.split('|')]
                if cols and cols[0] == '':
                    cols = cols[1:]
                if cols and cols[-1] == '':
                    cols = cols[:-1]
                # skip header row that starts with Node and possibly has G/C
                if len(cols) >= 2 and cols[0].lower() == 'node' and ('g/c' in cols[1].lower() or 'g' == cols[1].lower()):
                    continue
                # consider only rows where first column isn't empty
                if cols and cols[0]:
                    node_rows.append(cols)
            if node_rows:
                # build nodes section
                nodes_lines = []
                nodes_lines.append('')
                nodes_lines.append('### Nodes')
                nodes_lines.append('')
                nodes_lines.append('| Node | G/C | Description |')
                nodes_lines.append('| ----- | --- | ----------- |')
                for cols in node_rows:
                    # columns may have been extended with citation columns; we want only first 3
                    while len(cols) < 3:
                        cols.append('')
                    node_line = '| ' + ' | '.join(cols[:3]) + ' |'
                    nodes_lines.append(node_line)
                final_text = final_text + '\n'.join(nodes_lines) + '\n'
                # remove the original node block from final_text if it exists
                final_text = final_text.replace(block, '\n')
        # write back
        path.write_text(final_text, encoding='utf-8')
        return True
    return False


def main():
    readmes = sorted(CLUSTERS.glob('*/README.md'))
    updated = []
    for r in readmes:
        ok = process_readme(r)
        if ok:
            updated.append(str(r))
    print('Updated:', len(updated), 'files')
    for u in updated:
        print('-', u)

if __name__ == '__main__':
    main()
