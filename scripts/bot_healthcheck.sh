#!/usr/bin/env bash
# bot_healthcheck.sh — Failsafe restart for the Annals local bot server.
#
# Run via cron every 5 minutes:
#   */5 * * * * /home/manasa151/annals-of-the-world/scripts/bot_healthcheck.sh >> /tmp/bot_healthcheck.log 2>&1
#
# What it does:
#   1. Checks if local_bot_server.py is responding on port 7474
#   2. If not: kills any stale process and restarts it
#   3. Writes status to /tmp/bot_healthcheck.log

set -euo pipefail

REPO="/home/manasa151/annals-of-the-world"
SCRIPT="$REPO/scripts/local_bot_server.py"
PYTHON="$REPO/.venv/bin/python3"
LOG="/tmp/local_bot_server.log"
PID_FILE="/tmp/local_bot_server.pid"
PORT=7474
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# ── Health check ──────────────────────────────────────────────────────────────
if curl -sf --max-time 5 "http://localhost:${PORT}/health" > /dev/null 2>&1; then
    echo "[$TIMESTAMP] [ok] local_bot_server healthy on port ${PORT}"
    exit 0
fi

echo "[$TIMESTAMP] [warn] local_bot_server not responding — restarting..."

# ── Kill any stale processes ──────────────────────────────────────────────────
if [[ -f "$PID_FILE" ]]; then
    OLD_PID=$(cat "$PID_FILE" 2>/dev/null || echo "")
    if [[ -n "$OLD_PID" ]] && kill -0 "$OLD_PID" 2>/dev/null; then
        echo "[$TIMESTAMP] Killing stale PID $OLD_PID"
        kill "$OLD_PID" 2>/dev/null || true
        sleep 2
    fi
    rm -f "$PID_FILE"
fi

# Also kill any orphaned python3 local_bot_server processes
pkill -f "local_bot_server.py" 2>/dev/null || true
sleep 1

# ── Restart in background ─────────────────────────────────────────────────────
cd "$REPO"
source .env 2>/dev/null || true  # load env vars if .env exists

nohup env PYTHONUNBUFFERED=1 "$PYTHON" "$SCRIPT" >> "$LOG" 2>&1 &
NEW_PID=$!
echo "$NEW_PID" > "$PID_FILE"

echo "[$TIMESTAMP] [restart] local_bot_server started as PID $NEW_PID"

# ── Verify it came up ─────────────────────────────────────────────────────────
sleep 5
if curl -sf --max-time 5 "http://localhost:${PORT}/health" > /dev/null 2>&1; then
    echo "[$TIMESTAMP] [ok] local_bot_server confirmed healthy after restart"
else
    echo "[$TIMESTAMP] [error] local_bot_server failed to start — check $LOG"
    exit 1
fi
