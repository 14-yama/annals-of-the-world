#!/usr/bin/env python3
"""Orchestrate node and relationship normalization.

Runs the project's node and relationship normalizers across all cluster files.
Intended uses:
- Manual: `python3 scripts/normalize_all.py`
- Git hook: run before commit to ensure files are normalized.

The script is conservative: it only calls existing normalizer scripts if present
and prints a summary. It exits nonzero if any called normalizer returns nonzero.
"""

import subprocess
import shutil
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]


def run_cmd(cmd):
    print(f"Running: {' '.join(cmd)}")
    try:
        res = subprocess.run(cmd, check=False, capture_output=True, text=True)
    except FileNotFoundError:
        print(f"Command not found: {cmd[0]}")
        return 127, "cmd-not-found"
    print(res.stdout.strip())
    if res.stderr:
        print(res.stderr.strip())
    return res.returncode, res


def main():
    reports = []

    node_norm = ROOT / 'scripts' / 'normalize_nodes.py'
    rel_norm = ROOT / 'scripts' / 'normalize_relationships.py'

    # Run node normalizer if present
    if node_norm.exists():
        code, _ = run_cmd(['python3', str(node_norm)])
        reports.append(('nodes', str(node_norm), code))
    else:
        print(f"Node normalizer not found at {node_norm}; skipping nodes normalization.")
        reports.append(('nodes', str(node_norm), None))

    # Run relationship normalizer if present
    if rel_norm.exists():
        code, _ = run_cmd(['python3', str(rel_norm)])
        reports.append(('relationships', str(rel_norm), code))
    else:
        print(f"Relationship normalizer not found at {rel_norm}; skipping relationships normalization.")
        reports.append(('relationships', str(rel_norm), None))

    print('\nSummary:')
    exit_code = 0
    for name, path, code in reports:
        print(f"- {name}: script={path}, exit={code}")
        if isinstance(code, int) and code != 0:
            exit_code = code

    return exit_code


if __name__ == '__main__':
    sys.exit(main())
