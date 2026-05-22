#!/usr/bin/env bash
# ═══════════════════════════════════════════════════════════
# VS Code / GitHub Models enrichment — Class 3 + Class 7
# 350 Class-3 (Institutions) + 150 Class-7 (Artifacts & Texts)
# = 500 entities total via gpt-4o-mini (free with GitHub Copilot)
# Batch size 10 · ~5s/entity · ~50s/batch
# ═══════════════════════════════════════════════════════════
set -euo pipefail

BATCH_SIZE=10
CLASS3_QUEUE="data/enrichment/queue_class3.json"
CLASS7_QUEUE="data/enrichment/queue_class7.json"
LOG="/tmp/vscode_class_$(date +%Y%m%d_%H%M).log"
TOTAL_CLASS3=350
TOTAL_CLASS7=150

echo "═══════════════════════════════════════════════════════════"
echo " VS Code GitHub Models enrichment"
echo " Class 3 (Institutions): ${TOTAL_CLASS3} entities"
echo " Class 7 (Artifacts): ${TOTAL_CLASS7} entities"
echo " Total: $((TOTAL_CLASS3 + TOTAL_CLASS7)) · Batch size: ${BATCH_SIZE}"
echo " Log: ${LOG}"
echo " Started: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "═══════════════════════════════════════════════════════════"

export PYTHONUNBUFFERED=1
export GH_TOKEN
GH_TOKEN=$(gh auth token 2>/dev/null || echo "")

if [ -z "$GH_TOKEN" ]; then
  echo "ERROR: No GitHub token. Run: gh auth login"
  exit 1
fi

run_batch() {
  local queue="$1"
  local count="$2"
  local label="$3"
  local batches=$(( (count + BATCH_SIZE - 1) / BATCH_SIZE ))
  local processed=0
  local enriched=0

  echo ""
  echo "━━━ ${label}: ${batches} batches of ${BATCH_SIZE} (${count} total) ━━━"

  for ((b=1; b<=batches; b++)); do
    local remaining=$((count - processed))
    local this_batch=$((remaining < BATCH_SIZE ? remaining : BATCH_SIZE))
    local start_time=$(date +%s)

    echo ""
    echo "── ${label} Batch ${b}/${batches} ──── $(date -u +%H:%M:%S)"
    echo "   Queue: ${queue} | count=${this_batch}"

    if timeout 180 python3 -u scripts/ai_enrich_autonomous.py \
        --model github \
        --github-model gpt-4o-mini \
        --queue "${queue}" \
        --count "${this_batch}" \
        --min-score 0 \
        --retry 1 2>&1; then
      local elapsed=$(( $(date +%s) - start_time ))
      processed=$((processed + this_batch))
      echo "   ✓ Batch ${b} done in ${elapsed}s (${processed}/${count} processed)"
    else
      echo "   ⚠ Batch ${b} exited non-zero — continuing"
      processed=$((processed + this_batch))
    fi

    # Brief pause between batches (GitHub Models rate limit buffer)
    sleep 2
  done
}

# Phase 1: Class 3 (Institutions) — 350 entities
run_batch "$CLASS3_QUEUE" "$TOTAL_CLASS3" "Class-3"

# Phase 2: Class 7 (Artifacts & Texts) — 150 entities
run_batch "$CLASS7_QUEUE" "$TOTAL_CLASS7" "Class-7"

echo ""
echo "═══════════════════════════════════════════════════════════"
echo " DONE — all 500 entities processed"
echo " Finished: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "═══════════════════════════════════════════════════════════"
