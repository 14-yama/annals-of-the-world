#!/usr/bin/env bash
# VS Code Batch: 50 batches × 20 entities = 1000 entities via Ollama (local).
# Uses the local LLM (zero cloud cost, zero rate limit). Watchdog will sync.
#
# Speed improvements over v1:
#   - Batch size 8 → 20 (more entities per run, same per-entity Ollama speed)
#   - Queue regen skipped if queue.json < 30 min old (saves 30s × 50 = 25 min)
#   - --retry 1 (was 2) — fail faster on bad entities, try more new ones instead
#   - sleep 5 → 1 between batches
#   - timeout 3600s per batch (20 entities × ~150s avg = ~50 min; cap is safe)
#
# Output:
#   /tmp/batch_run_YYYYMMDD_HHMM.log   — per-entity progress (unbuffered)
#   data/enrichment/last_run.json      — overwritten each batch (used by UI)
#   data/appwrite-export/entities/...  — files marked _unsyncedEdits=true
#
# Run:  bash scripts/run_400_local_batches.sh
set -u

cd "$(dirname "$0")/.."

TOTAL_BATCHES=50
BATCH_SIZE=20
QUEUE_TTL=1800   # seconds before queue.json is considered stale (30 min)
LOG=/tmp/batch_run_$(date +%Y%m%d_%H%M).log
START_TS=$(date +%s)

echo "═══════════════════════════════════════════════════════════" | tee -a "$LOG"
echo " 50 × 20 = 1000-entity local Ollama enrichment run          " | tee -a "$LOG"
echo " Started: $(date -u +%FT%TZ)                                " | tee -a "$LOG"
echo " Log:     $LOG                                              " | tee -a "$LOG"
echo "═══════════════════════════════════════════════════════════" | tee -a "$LOG"

SUCCESS=0
FAIL=0
TOTAL_ENRICHED=0

# Regen queue once at start
echo "  → Generating initial queue..." | tee -a "$LOG"
python3 scripts/enrichment_queue.py --limit 2000 >/dev/null 2>&1 || \
  echo "  ⚠ initial queue regen failed" | tee -a "$LOG"
QUEUE_REGEN_TS=$(date +%s)

for i in $(seq 1 $TOTAL_BATCHES); do
  BATCH_START=$(date +%s)
  echo "" | tee -a "$LOG"
  echo "── Batch $i / $TOTAL_BATCHES ──────────────── $(date -u +%T)" | tee -a "$LOG"

  # Only regen queue if stale (> 30 min old)
  QUEUE_AGE=$(( $(date +%s) - QUEUE_REGEN_TS ))
  if [ "$QUEUE_AGE" -gt "$QUEUE_TTL" ]; then
    echo "  → Queue stale (${QUEUE_AGE}s) — regenerating..." | tee -a "$LOG"
    python3 scripts/enrichment_queue.py --limit 2000 >/dev/null 2>&1 || \
      echo "  ⚠ queue regen failed (continuing with stale queue)" | tee -a "$LOG"
    QUEUE_REGEN_TS=$(date +%s)
  fi

  # Enrich — 20 entities, 1 retry (fail fast), 60-min cap
  if PYTHONUNBUFFERED=1 timeout 3600 python3 -u scripts/ai_enrich_autonomous.py \
       --count "$BATCH_SIZE" --model ollama --retry 1 --lenient \
       >> "$LOG" 2>&1; then
    ENRICHED=$(python3 -c "import json; d=json.load(open('data/enrichment/last_run.json')); print(d.get('enriched',0))" 2>/dev/null || echo 0)
    TOTAL_ENRICHED=$((TOTAL_ENRICHED + ENRICHED))
    SUCCESS=$((SUCCESS + 1))
    BATCH_TIME=$(( $(date +%s) - BATCH_START ))
    echo "  ✓ Batch $i: $ENRICHED enriched in ${BATCH_TIME}s · total: $TOTAL_ENRICHED" | tee -a "$LOG"
  else
    FAIL=$((FAIL + 1))
    echo "  ✗ Batch $i failed (will continue)" | tee -a "$LOG"
    sleep 15
  fi

  # Minimal pause between batches
  sleep 1
done

ELAPSED=$(( $(date +%s) - START_TS ))
echo "" | tee -a "$LOG"
echo "═══════════════════════════════════════════════════════════" | tee -a "$LOG"
echo " Run complete: $SUCCESS ok / $FAIL fail / $TOTAL_ENRICHED entities" | tee -a "$LOG"
echo " Elapsed: ${ELAPSED}s ($((ELAPSED / 60)) min)" | tee -a "$LOG"
echo "═══════════════════════════════════════════════════════════" | tee -a "$LOG"

echo ""
echo "Run done. Watchdog/sync_gateway will push to Appwrite."
