#!/usr/bin/env python3
"""
mark_recently_enriched_unsynced.py

Marks all entity files changed in the last N commits (before HEAD)
as _unsyncedEdits=True so sync_gateway --local will re-push them to Appwrite.

Usage: python3 scripts/mark_recently_enriched_unsynced.py [--commits=N]
Default: last 30 commits before HEAD (covers ~850 recent enrichments).
"""
import json, os, subprocess, sys
from datetime import datetime, timezone

ENTITIES_DIR = "data/appwrite-export/entities"
NOW = datetime.now(timezone.utc).isoformat()
EDITOR_ID = "re-sync-marker"

def get_changed_files(commits_back=30):
    """Get entity JSON files changed in the last N commits (before HEAD)."""
    try:
        # Get commit N back
        baseline = subprocess.check_output(
            ["git", "log", "--format=%H", f"-{commits_back+1}"],
            encoding="utf-8"
        ).strip().split("\n")
        if len(baseline) < commits_back + 1:
            baseline_commit = baseline[-1]
        else:
            baseline_commit = baseline[commits_back]
        print(f"Baseline commit ({commits_back} back): {baseline_commit[:12]}")
        # Files changed between baseline and HEAD
        out = subprocess.check_output(
            ["git", "diff", "--name-only", baseline_commit, "HEAD",
             "--", ENTITIES_DIR],
            encoding="utf-8"
        )
        files = [f.strip() for f in out.strip().split("\n") if f.strip().endswith(".json")]
        return files
    except Exception as e:
        print(f"ERROR getting git diff: {e}")
        return []

def mark_file(rel_path):
    """Set _unsyncedEdits=True on all entities in a JSON file."""
    path = rel_path if os.path.isabs(rel_path) else os.path.join(os.getcwd(), rel_path)
    if not os.path.exists(path):
        print(f"  SKIP (not found): {path}")
        return 0
    try:
        with open(path, "r", encoding="utf-8") as f:
            doc = json.load(f)
    except Exception as e:
        print(f"  SKIP (parse error): {path}: {e}")
        return 0

    changed = 0
    for entity in doc.get("entities", []):
        # Set top-level flag
        entity["_unsyncedEdits"] = True
        # Also set in detailsJson
        dj_raw = entity.get("detailsJson", "{}")
        try:
            dj = json.loads(dj_raw) if isinstance(dj_raw, str) else dj_raw
        except Exception:
            dj = {}
        # Add minimal _editLog entry so --local mode's editLog check also matches
        edit_log = dj.get("_editLog", [])
        edit_log.append({
            "timestamp": NOW,
            "editorId": EDITOR_ID,
            "field": "_resync",
            "oldValue": "",
            "newValue": "marked for re-sync to Appwrite"
        })
        dj["_editLog"] = edit_log
        dj["_unsyncedEdits"] = True
        entity["detailsJson"] = json.dumps(dj, ensure_ascii=False)
        changed += 1

    with open(path, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    return changed

def main():
    commits_back = 30
    for arg in sys.argv[1:]:
        if arg.startswith("--commits="):
            commits_back = int(arg.split("=")[1])

    print(f"=== mark_recently_enriched_unsynced.py (last {commits_back} commits) ===")
    files = get_changed_files(commits_back)
    print(f"Found {len(files)} changed entity files in last {commits_back} commits")

    total_entities = 0
    for rel_path in files:
        n = mark_file(rel_path)
        if n:
            total_entities += n

    print(f"\n✓ Marked {total_entities} entities in {len(files)} files as _unsyncedEdits=True")
    print("Now run:  env $(cat .env | grep -v '^#' | xargs) npx tsx scripts/sync_gateway.ts --local")

if __name__ == "__main__":
    main()
