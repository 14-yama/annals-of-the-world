#!/usr/bin/env bash
# auto_pull.sh — Watch GitHub for changes and pull them locally.
# Run once: `bash scripts/auto_pull.sh`
# Runs forever in background; Ctrl-C to stop.

set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
BRANCH="${1:-$(git -C "$REPO_DIR" branch --show-current)}"
INTERVAL="${2:-60}"   # seconds between pulls

echo "Auto-pull: watching $BRANCH every ${INTERVAL}s — Ctrl-C to stop"

while true; do
  cd "$REPO_DIR"
  BEFORE=$(git rev-parse HEAD)
  git fetch origin "$BRANCH" --quiet 2>&1 || true
  AFTER=$(git rev-parse "origin/$BRANCH")

  if [ "$BEFORE" != "$AFTER" ]; then
    echo "[$(date +%H:%M:%S)] New commits from GitHub — pulling..."
    git pull --ff-only origin "$BRANCH" && echo "  → now at $(git rev-parse --short HEAD)"
  fi

  sleep "$INTERVAL"
done
