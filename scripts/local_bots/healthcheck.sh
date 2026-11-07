#!/usr/bin/env bash
# Annals local-bot healthcheck — launchd every 5 minutes.
# Ensures Ollama + bot-server (7474). Does NOT start the legacy monolithic
# local_bot_daemon.sh when discrete com.annals.* LaunchAgents are installed.
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
LOG_DIR="${LOG_DIR:-$HOME/Library/Logs/annals-bots}"
PID_DIR="/tmp/annals-bots"
PORT=7474
mkdir -p "$LOG_DIR" "$PID_DIR"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] [healthcheck] $*"; }

PYTHON="python3"
if [[ -f "$REPO_DIR/.venv/bin/activate" ]]; then
  # shellcheck disable=SC1091
  source "$REPO_DIR/.venv/bin/activate"
  PYTHON="$REPO_DIR/.venv/bin/python3"
fi
export PATH="$HOME/.local/bin:/opt/homebrew/bin:$PATH"

if [[ -f "$HOME/.config/annals/env" ]]; then
  set -a; # shellcheck disable=SC1090
  source "$HOME/.config/annals/env"; set +a
fi
if [[ -f "$REPO_DIR/.env" ]]; then
  set -a; # shellcheck disable=SC1090
  source "$REPO_DIR/.env"; set +a
fi

# ── Ollama ────────────────────────────────────────────────────────────────────
if ! curl -sf --max-time 3 http://localhost:11434/api/tags >/dev/null 2>&1; then
  log "Ollama not responding — attempting start"
  if [[ -x "$HOME/.local/bin/ollama" ]]; then
    nohup "$HOME/.local/bin/ollama" serve >>"$LOG_DIR/ollama.log" 2>&1 &
  elif command -v ollama >/dev/null 2>&1; then
    nohup ollama serve >>"$LOG_DIR/ollama.log" 2>&1 &
  else
    log "WARNING: ollama binary not found"
  fi
  sleep 3
fi

# ── Prefer launchd bot-server if loaded ───────────────────────────────────────
UID_NUM="$(id -u)"
if launchctl print "gui/${UID_NUM}/com.annals.bot-server" >/dev/null 2>&1; then
  if ! curl -sf --max-time 5 "http://localhost:${PORT}/health" >/dev/null 2>&1; then
    log "bot-server LaunchAgent loaded but /health failed — kickstart"
    launchctl kickstart -k "gui/${UID_NUM}/com.annals.bot-server" 2>/dev/null || true
    sleep 2
  else
    log "ok — bot-server healthy on :${PORT} (launchd)"
  fi
else
  # Fallback: manage process directly (pre-install / Linux)
  if ! curl -sf --max-time 5 "http://localhost:${PORT}/health" >/dev/null 2>&1; then
    log "bot-server not responding — restarting process"
    pkill -f "local_bot_server.py" 2>/dev/null || true
    sleep 1
    nohup "$PYTHON" "$REPO_DIR/scripts/local_bot_server.py" --port "$PORT" \
      >>"$LOG_DIR/bot-server.log" 2>&1 &
    echo $! >"$PID_DIR/bot_server.pid"
    sleep 2
    log "bot-server started pid=$(cat "$PID_DIR/bot_server.pid")"
  else
    log "ok — bot-server healthy on :${PORT}"
  fi
fi

# Deliberately do NOT start local_bot_daemon.sh — discrete enrich/significance
# LaunchAgents replace that loop on the Mac Mini.
exit 0
