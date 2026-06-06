#!/usr/bin/env bash
# local_bot_cron_watchdog.sh — Belt-and-suspenders guardian for the local bot stack.
#
# Runs every 5 minutes via cron to ensure:
#   1. local_bot_server.py (port 7474) is alive — restarts if not
#   2. local_bot_daemon.sh loop (24/7 enrichment) is alive — restarts if not
#   3. Ollama service is running — restarts if not
#
# Install (run once):
#   bash scripts/install_local_services.sh
#
# Crontab entry (added automatically by install_local_services.sh):
#   */5 * * * * /path/to/scripts/local_bot_cron_watchdog.sh >> /tmp/annals-watchdog.log 2>&1

set -euo pipefail

# ── Config ────────────────────────────────────────────────────────────────────
REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
LOG_DIR="${LOG_DIR:-/tmp}"
LOG_FILE="$LOG_DIR/annals-watchdog.log"
VENV="$REPO_DIR/.venv"
OLLAMA_BIN="$HOME/.local/bin/ollama"
PID_DIR="/tmp/annals-bots"
mkdir -p "$PID_DIR"

# ── Logging ───────────────────────────────────────────────────────────────────
log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] [watchdog] $*"; }

# ── Activate venv ─────────────────────────────────────────────────────────────
PYTHON="python3"
if [ -f "$VENV/bin/activate" ]; then
    source "$VENV/bin/activate"
    PYTHON="$VENV/bin/python3"
fi
export PATH="$HOME/.local/bin:$PATH"
export LD_LIBRARY_PATH="$HOME/.local/lib/ollama:${LD_LIBRARY_PATH:-}"

# Load .env
if [ -f "$REPO_DIR/.env" ]; then
    set -a; source "$REPO_DIR/.env"; set +a
fi

# ── 1. Ensure Ollama is running ───────────────────────────────────────────────
ensure_ollama() {
    if curl -sf http://localhost:11434/api/tags > /dev/null 2>&1; then
        return 0  # already up
    fi
    log "Ollama not responding — attempting restart"
    if systemctl --user is-active ollama.service > /dev/null 2>&1; then
        systemctl --user restart ollama.service
        sleep 3
    elif [ -x "$OLLAMA_BIN" ]; then
        nohup "$OLLAMA_BIN" serve >> "$LOG_DIR/annals-ollama.log" 2>&1 &
        sleep 5
    else
        log "WARNING: Ollama not found — enrichment bots will use Gemini fallback"
        return 1
    fi

    # Wait up to 30s
    for i in $(seq 1 6); do
        sleep 5
        if curl -sf http://localhost:11434/api/tags > /dev/null 2>&1; then
            log "Ollama back online"
            return 0
        fi
    done
    log "ERROR: Ollama did not come back online after 30s"
    return 1
}

# ── 2. Ensure local_bot_server.py (port 7474) is running ──────────────────────
ensure_bot_server() {
    local PID_FILE="$PID_DIR/bot_server.pid"

    # Check if process is alive
    if [ -f "$PID_FILE" ]; then
        local PID
        PID=$(cat "$PID_FILE")
        if kill -0 "$PID" 2>/dev/null; then
            return 0  # running
        fi
        log "bot_server.py PID $PID is dead — restarting"
    else
        # Check by port
        if lsof -i :7474 -sTCP:LISTEN > /dev/null 2>&1; then
            return 0  # something is listening on 7474
        fi
        log "No process on port 7474 — starting bot server"
    fi

    nohup "$PYTHON" "$REPO_DIR/scripts/local_bot_server.py" \
        >> "$LOG_DIR/annals-bot-server.log" 2>&1 &
    echo $! > "$PID_FILE"
    sleep 2
    log "bot_server.py started (PID $(cat "$PID_FILE"))"
}

# ── 3. Ensure local_bot_daemon.sh loop is running ────────────────────────────
ensure_daemon_loop() {
    local PID_FILE="$PID_DIR/daemon_loop.pid"

    if [ -f "$PID_FILE" ]; then
        local PID
        PID=$(cat "$PID_FILE")
        if kill -0 "$PID" 2>/dev/null; then
            return 0  # running
        fi
        log "daemon_loop PID $PID is dead — restarting"
    else
        # Check by process name
        if pgrep -f "local_bot_daemon.sh" > /dev/null 2>&1; then
            return 0
        fi
        log "local_bot_daemon.sh not running — starting it"
    fi

    export ENRICH_COUNT="${ENRICH_COUNT:-5}"
    export SIG_COUNT="${SIG_COUNT:-5}"
    export INTERVAL="${INTERVAL:-30}"
    export OLLAMA_MODEL="${OLLAMA_MODEL:-llama3.2:3b}"

    nohup bash "$REPO_DIR/scripts/local_bot_daemon.sh" \
        >> "$LOG_DIR/annals-daemon.log" 2>&1 &
    echo $! > "$PID_FILE"
    sleep 1
    log "local_bot_daemon.sh started (PID $(cat "$PID_FILE"))"
}

# ── 4. Optional: try systemd units first (preferred over raw processes) ───────
try_systemd_units() {
    # Prefer systemd if available (more reliable than raw PIDs)
    if ! systemctl --user list-units > /dev/null 2>&1; then
        return 1  # no systemd user session
    fi

    local needs_daemon_relay=0
    for unit in annals-local-bot-server.service annals-local-bots.service; do
        if systemctl --user is-enabled "$unit" > /dev/null 2>&1; then
            if ! systemctl --user is-active "$unit" > /dev/null 2>&1; then
                log "systemd unit $unit is inactive — restarting"
                systemctl --user restart "$unit" || true
            fi
            needs_daemon_relay=1
        fi
    done
    return $needs_daemon_relay
}

# ── Main ──────────────────────────────────────────────────────────────────────
log "Watchdog check starting"

ensure_ollama || true

# Try systemd first; fall back to direct process management
if ! try_systemd_units; then
    ensure_bot_server
    ensure_daemon_loop
fi

log "Watchdog check complete"
