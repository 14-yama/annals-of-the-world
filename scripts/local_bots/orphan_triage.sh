#!/usr/bin/env bash
# Orphan triage helper — refresh CSV/HTML when legacy Nodes data exists,
# and ensure the git-first orphans audit report is present.
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$REPO_DIR"

PYTHON="python3"
if [[ -x "$REPO_DIR/.venv/bin/python3" ]]; then
  PYTHON="$REPO_DIR/.venv/bin/python3"
fi

echo "[orphan-triage] running git-first orphans audit"
"$PYTHON" -m scripts.audits.orphans || true

if ls data/Nodes/nodes.*.json >/dev/null 2>&1; then
  echo "[orphan-triage] exporting legacy orphan CSV"
  "$PYTHON" scripts/export_orphans_csv.py || true
  if [[ -f data/orphan_nodes.csv ]]; then
    echo "[orphan-triage] regenerating orphan_triage.html"
    "$PYTHON" scripts/generate_orphan_triage.py || true
  fi
else
  echo "[orphan-triage] no data/Nodes/*.json — skipping legacy CSV/HTML path"
  echo "[orphan-triage] see data/audit-reports/ for orphans audit output"
fi

echo "[orphan-triage] done"
