#!/bin/zsh
# Durable cloud→local audit_log backfill loop.
# Resumes from data/governance/audit_backfill_cursor.json until done=true.
# Safe to re-run (create-if-missing / 409=skip). Does not touch enrich bots.
set -eu
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
LOG="${ANNALS_AUDIT_BACKFILL_LOG:-/tmp/annals-audit-backfill.log}"
PIDFILE="${ANNALS_AUDIT_BACKFILL_PID:-/tmp/annals-audit-backfill.pid}"
LOCKFILE="${ANNALS_AUDIT_BACKFILL_LOCK:-/tmp/annals-audit-backfill.lock}"
MAX="${ANNALS_AUDIT_BACKFILL_MAX:-3000}"
SLEEP_MS="${ANNALS_AUDIT_BACKFILL_SLEEP_MS:-2}"
PAUSE_S="${ANNALS_AUDIT_BACKFILL_PAUSE_S:-5}"

# Exclusive lock — prevents launchd + nohup double-starts racing the cursor.
# Prefer mkdir (atomic, no flock(1) dependency on macOS).
LOCKDIR="${LOCKFILE}.d"
if ! mkdir "$LOCKDIR" 2>/dev/null; then
  # Stale lock if holder pid is dead
  old_pid="$(cat "$PIDFILE" 2>/dev/null || true)"
  if [[ -n "${old_pid}" ]] && kill -0 "$old_pid" 2>/dev/null; then
    echo "[loop] already locked by pid=$old_pid — exit" | tee -a "$LOG"
    exit 0
  fi
  rmdir "$LOCKDIR" 2>/dev/null || true
  if ! mkdir "$LOCKDIR" 2>/dev/null; then
    echo "[loop] already locked by another worker — exit" | tee -a "$LOG"
    exit 0
  fi
fi
echo $$ > "$PIDFILE"
trap 'rm -f "$PIDFILE"; rmdir "$LOCKDIR" 2>/dev/null || true' EXIT

# Load local Appwrite env without printing secrets
if [[ -f "$ROOT/.env" ]]; then
  set -a
  # shellcheck disable=SC1091
  source "$ROOT/.env"
  set +a
fi
export PYTHONUNBUFFERED=1

echo "[loop] durable start $(date -u +%Y-%m-%dT%H:%M:%SZ) max=$MAX" | tee -a "$LOG"

while true; do
  done_flag="$(python3 - <<'PY'
import json, os
p = "data/governance/audit_backfill_cursor.json"
if not os.path.exists(p):
    print("0")
else:
    try:
        print("1" if json.load(open(p)).get("done") else "0")
    except Exception:
        print("0")
PY
)"
  if [[ "$done_flag" == "1" ]]; then
    echo "[loop] complete $(date -u +%Y-%m-%dT%H:%M:%SZ)" | tee -a "$LOG"
    break
  fi
  echo "[loop] start $(date -u +%H:%M:%S)" | tee -a "$LOG"
  set +e
  python3 -u "$ROOT/scripts/backfill_local_audit_log.py" --max="$MAX" --sleep-ms="$SLEEP_MS" --checkpoint=50 >>"$LOG" 2>&1
  code=$?
  set -e
  echo "[loop] exit=$code $(date -u +%H:%M:%S)" | tee -a "$LOG"
  # Brief pause so Python can release the ~300MB backup JSON before reload
  sleep "$PAUSE_S"
done
