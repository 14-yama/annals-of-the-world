#!/usr/bin/env bash
# local_bot_daemon.sh — 24/7 local enrichment bot loop.
#
# Runs enrichment + significance backfill on a schedule (every INTERVAL minutes).
# Designed to be managed by systemd (see scripts/annals-local-bots.service) so
# it persists even when VS Code / the browser are closed.
#
# The bot server (port 7474) MUST also be running so the Curator UI can observe
# these runs. Start it separately via annals-local-bot-server.service.
#
# Environment variables (can be set in ~/.config/annals/env or .env):
#   ENRICH_COUNT   — entities per enrichment run   (default: 5)
#   SIG_COUNT      — entities per significance run  (default: 5)
#   INTERVAL       — minutes between cycles         (default: 30)
#   OLLAMA_MODEL   — model to use                   (default: llama3.2:3b)

set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
LOG_DIR="${LOG_DIR:-/tmp}"
ENRICH_COUNT="${ENRICH_COUNT:-5}"
SIG_COUNT="${SIG_COUNT:-5}"
INTERVAL="${INTERVAL:-30}"
OLLAMA_MODEL="${OLLAMA_MODEL:-llama3.2:3b}"
VENV="$REPO_DIR/.venv"

# ── Activate venv if present ──
if [ -f "$VENV/bin/activate" ]; then
  source "$VENV/bin/activate"
fi

# ── Add Ollama to PATH ──
export PATH="$HOME/.local/bin:$PATH"
export LD_LIBRARY_PATH="$HOME/.local/lib/ollama:${LD_LIBRARY_PATH:-}"

# ── Load .env if present ──
ENV_FILE="$REPO_DIR/.env"
if [ -f "$ENV_FILE" ]; then
  set -a
  source "$ENV_FILE"
  set +a
fi

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"; }

wait_for_ollama() {
  local retries=12
  while [ $retries -gt 0 ]; do
    if curl -sf http://localhost:11434/api/tags > /dev/null 2>&1; then
      log "Ollama is up."
      return 0
    fi
    log "Waiting for Ollama… ($retries retries left)"
    sleep 5
    retries=$((retries - 1))
  done
  log "ERROR: Ollama not reachable after 60s — skipping this cycle."
  return 1
}

log "=== Local Bot Daemon starting ==="
log "  Repo:     $REPO_DIR"
log "  Model:    $OLLAMA_MODEL"
log "  Enrich:   $ENRICH_COUNT entities/cycle"
log "  Sig:      $SIG_COUNT entities/cycle"
log "  Interval: every ${INTERVAL}m"

cycle=0
while true; do
  cycle=$((cycle + 1))
  log "=== Cycle #$cycle ==="
  cd "$REPO_DIR"

  # ── 1. Regenerate queue ──
  log "Step 1/4: Regenerating enrichment queue..."
  python3 scripts/enrichment_queue.py --limit 500 >> "$LOG_DIR/annals-bot-queue.log" 2>&1 || true

  # ── 2. Enrich entities ──
  if wait_for_ollama; then
    log "Step 2/4: Enriching $ENRICH_COUNT entities via $OLLAMA_MODEL..."
    python3 scripts/ai_enrich_autonomous.py \
      --count "$ENRICH_COUNT" \
      --model ollama \
      --ollama-model "$OLLAMA_MODEL" \
      >> "$LOG_DIR/annals-bot-enrich.log" 2>&1 || true

    # ── 3. Significance backfill ──
    log "Step 3/4: Significance backfill ($SIG_COUNT entities)..."
    python3 scripts/backfill_significance.py \
      --count "$SIG_COUNT" \
      --model ollama \
      --ollama-model "$OLLAMA_MODEL" \
      >> "$LOG_DIR/annals-bot-significance.log" 2>&1 || true
  fi

  # ── 4. Aggregate local KPI (keeps the dashboard fresh) ──
  log "Step 4/5: Updating local KPI…"
  python3 scripts/local_kpi_aggregator.py >> "$LOG_DIR/annals-bot-kpi.log" 2>&1 || true

  # ── 5. Git commit + push (sync gateway runs in cloud after push) ──
  log "Step 5/5: Committing enriched files..."
  CHANGED=$(git diff --name-only data/appwrite-export/entities/ | wc -l)
  if [ "$CHANGED" -gt 0 ]; then
    git add data/appwrite-export/entities/ data/enrichment/ 2>/dev/null || true
    if ! git diff --cached --quiet; then
      git commit -m "feat(data): local-bot cycle #$cycle — ${CHANGED} entities enriched

Automated local Ollama enrichment ($OLLAMA_MODEL).
Cycle: $cycle | Enrich: $ENRICH_COUNT | Sig: $SIG_COUNT" || true
      git push origin clean/audit-system || true
      log "Pushed $CHANGED enriched files to GitHub."
    fi
  else
    log "No new entity files to commit this cycle."
  fi

  log "Cycle #$cycle done. Sleeping ${INTERVAL}m..."
  sleep $((INTERVAL * 60))
done
