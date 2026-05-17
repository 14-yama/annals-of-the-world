#!/usr/bin/env python3
"""Workflow helper — write/update data/governance/last_github_runs.json.

Called by .github/workflows/{ai-enrichment,sync-gateway,significance-backfill,bot-keepalive}.yml
to record the latest cloud run status for the OllamaMonitor UI.

Usage:
    python3 scripts/_workflow_write_run_status.py "<workflow display name>" [conclusion]

Env vars used: GITHUB_RUN_ID, GITHUB_REPOSITORY, GITHUB_EVENT_NAME
"""
from __future__ import annotations
import json, os, sys, time
from pathlib import Path


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: _workflow_write_run_status.py <name> [conclusion]", file=sys.stderr)
        return 1
    name = sys.argv[1]
    conclusion = sys.argv[2] if len(sys.argv) > 2 else "success"

    runs_file = Path("data/governance/last_github_runs.json")
    runs_file.parent.mkdir(parents=True, exist_ok=True)
    existing: list[dict] = []
    if runs_file.exists():
        try:
            data = json.loads(runs_file.read_text())
            existing = data.get("runs", []) if isinstance(data, dict) else (data or [])
        except Exception:
            existing = []

    run_id = os.environ.get("GITHUB_RUN_ID", "")
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    this_run = {
        "name": name,
        "status": "completed",
        "conclusion": conclusion,
        "runId": int(run_id) if run_id.isdigit() else 0,
        "startedAt": None,
        "updatedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "htmlUrl": f"https://github.com/{repo}/actions/runs/{run_id}" if repo and run_id else "",
        "triggeredBy": os.environ.get("GITHUB_EVENT_NAME", "schedule"),
    }
    # Replace any prior entry with same name
    existing = [r for r in existing if r.get("name") != name]
    existing.insert(0, this_run)
    runs_file.write_text(json.dumps(existing[:15], indent=2))
    print(f"[run-status] {name} → {conclusion} (run {run_id})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
