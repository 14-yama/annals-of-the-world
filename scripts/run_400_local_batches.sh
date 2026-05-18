#!/usr/bin/env bash
# VS Code Batch 10–59: 50 batches × 8 entities = 400 entities via Ollama (local).
# Uses the local LLM (zero cloud cost, zero rate limit). Watchdog will sync.
#
# Behaviour:
#   - Loops 50 times
#   - Each iteration: regenerate queue, enrich 8 entities, log result
#   - On any single-batch failure: log, sleep 30s, continue (no hard stop)
#   - Total wall clock ~3-4h (8 entities × ~4s/call × 50 batches)
#
# Output:
#   /tmp/batch_run.log         — line per batch (timestamp, batch#, status)
#   data/enrichment/last_run.json — overwritten each batch (used by UI)
#   data/appwrite-export/entities/...  — files marked _unsyncedEdits=true
#
# Run:  bash scripts/run_400_local_batches.sh
set -u

cd "$(dirname "$0")/.."

TOTAL_BATCHES=50
BATCH_SIZE=8
LOG=/tmp/batch_run_$(date +%Y%m%d_%H%M).log
START_TS=$(date +%s)

echo "═══════════════════════════════════════════════════════════" | tee -a "$LOG"
echo " 50 × 8 = 400-entity local Ollama enrichment run            " | tee -a "$LOG"
echo " Started: $(date -u +%FT%TZ)                                " | tee -a "$LOG"
echo " Log:     $LOG                                              " | tee -a "$LOG"
echo "═══════════════════════════════════════════════════════════" | tee -a "$LOG"

SUCCESS=0
FAIL=0
TOTAL_ENRICHED=0

for i in $(seq 1 $TOTAL_BATCHES); do
  BATCH_START=$(date +%s)
  echo "" | tee -a "$LOG"
  echo "── Batch $i / $TOTAL_BATCHES ──────────────── $(date -u +%T)" | tee -a "$LOG"

  # Regenerate queue (so we pick fresh weak entities each batch)
  python3 scripts/enrichment_queue.py --limit 300 >/dev/null 2>&1 || \
    echo "  ⚠ queue regen failed (continuing with stale queue)" | tee -a "$LOG"

  # Enrich (each Ollama call ~2-3 min on CPU; 8 entities ~16-24 min)
  if PYTHONUNBUFFERED=1 timeout 2400 python3 -u scripts/ai_enrich_autonomous.py \
       --count "$BATCH_SIZE" --model ollama --retry 2 --lenient \
       >> "$LOG" 2>&1; then
    ENRICHED=$(python3 -c "import json; d=json.load(open('data/enrichment/last_run.json')); print(d.get('enriched',0))" 2>/dev/null || echo 0)
    TOTAL_ENRICHED=$((TOTAL_ENRICHED + ENRICHED))
    SUCCESS=$((SUCCESS + 1))
    BATCH_TIME=$(( $(date +%s) - BATCH_START ))
    echo "  ✓ Batch $i: $ENRICHED enriched in ${BATCH_TIME}s · total: $TOTAL_ENRICHED" | tee -a "$LOG"
  else
    FAIL=$((FAIL + 1))
    echo "  ✗ Batch $i failed (will continue)" | tee -a "$LOG"
    sleep 30
  fi

  # Brief pause to let watchdog/sync_gateway breathe
  sleep 5
done

ELAPSED=$(( $(date +%s) - START_TS ))
echo "" | tee -a "$LOG"
echo "═══════════════════════════════════════════════════════════" | tee -a "$LOG"
echo " Run complete: $SUCCESS ok / $FAIL fail / $TOTAL_ENRICHED entities" | tee -a "$LOG"
echo " Elapsed: ${ELAPSED}s ($((ELAPSED / 60)) min)" | tee -a "$LOG"
echo "═══════════════════════════════════════════════════════════" | tee -a "$LOG"

echo ""
echo "Run done. Watchdog/sync_gateway will push to Appwrite."
