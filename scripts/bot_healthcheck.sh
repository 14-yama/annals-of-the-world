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
OLLAMA_BIN="$HOME/.local/bin/ollama"
ANOMALY_STATE="/tmp/bot_healthcheck.anomaly_state"
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# ── Ollama keepalive ──────────────────────────────────────────────────────────
if ! curl -sf --max-time 3 http://localhost:11434/api/tags > /dev/null 2>&1; then
    echo "[$TIMESTAMP] [warn] Ollama not responding — starting daemon"
    nohup "$OLLAMA_BIN" serve > /tmp/ollama.log 2>&1 &
    sleep 2
fi

# ── Silent-sync anomaly detection ─────────────────────────────────────────────
# If filesChanged > 0 but writesPerformed == 0 for two consecutive runs, force a sync.
LAST_SYNC="$REPO/data/governance/last_sync.json"
if [[ -f "$LAST_SYNC" ]]; then
    ANOMALY=$(python3 - <<'PY' 2>/dev/null || echo "0"
import json, pathlib
try:
    d = json.loads(pathlib.Path("/home/manasa151/annals-of-the-world/data/governance/last_sync.json").read_text())
    s = d.get("lastRunStats", {}) or {}
    fc = int(s.get("filesChanged", 0) or 0)
    wp = int(s.get("writesPerformed", 0) or 0)
    eu = int(s.get("entitiesUpserted", 0) or 0)
    print("1" if (fc > 0 and wp == 0 and eu == 0) else "0")
except Exception:
    print("0")
PY
)
    PREV=$(cat "$ANOMALY_STATE" 2>/dev/null || echo "0")
    if [[ "$ANOMALY" == "1" && "$PREV" == "1" ]]; then
        echo "[$TIMESTAMP] [ANOMALY] 2x silent-sync runs detected — forcing --local sync"
        cd "$REPO"
        set -a; [[ -f .env ]] && . .env; set +a
        timeout 600 npx tsx scripts/sync_gateway.ts --local --max=1000 2>&1 | tail -10
    fi
    echo "$ANOMALY" > "$ANOMALY_STATE"
fi

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
