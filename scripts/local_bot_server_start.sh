#!/usr/bin/env bash
# local_bot_server_start.sh — Start the local bot HTTP server (port 7474).
#
# Managed by annals-local-bot-server.service so it runs in the background
# even when VS Code is closed. The Curator UI connects to this server to
# display live bot status and trigger manual runs.

set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
VENV="$REPO_DIR/.venv"

if [ -f "$VENV/bin/activate" ]; then
  source "$VENV/bin/activate"
fi

export PATH="$HOME/.local/bin:$PATH"
export LD_LIBRARY_PATH="$HOME/.local/lib/ollama:${LD_LIBRARY_PATH:-}"

ENV_FILE="$REPO_DIR/.env"
if [ -f "$ENV_FILE" ]; then
  set -a
  source "$ENV_FILE"
  set +a
fi

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting local bot server on port 7474..."
cd "$REPO_DIR"
exec python3 scripts/local_bot_server.py --port 7474
