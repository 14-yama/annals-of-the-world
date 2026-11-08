#!/bin/zsh
# Stop a runaway com.annals.stats-cache facet scan (missing-$id cursor bug),
# install the fixed LaunchAgent schedule (twice hourly), truncate the log.
# Enrich bots are left alone.
set -euo pipefail
UID_NUM=$(id -u)
LABEL=com.annals.stats-cache
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
DEST="$HOME/Library/LaunchAgents/${LABEL}.plist"
FIXED="$REPO/data/governance/launchd-plists/${LABEL}.plist"
LOG="$HOME/Library/Logs/annals-bots/stats-cache.log"
CHECKPOINT="$REPO/data/governance/stats_cache_progress.json"

echo "[stop] bootout ${LABEL}"
launchctl bootout "gui/${UID_NUM}/${LABEL}" 2>/dev/null || true
# Kill any leftover node/tsx refresh process
pkill -f 'refresh_local_stats_cache' 2>/dev/null || true
sleep 1

if [[ -f "$FIXED" ]]; then
  echo "[stop] install fixed plist from $FIXED"
  cp "$FIXED" "$DEST"
  launchctl bootstrap "gui/${UID_NUM}" "$DEST" 2>/dev/null || launchctl load -w "$DEST" 2>/dev/null || true
  launchctl enable "gui/${UID_NUM}/${LABEL}" 2>/dev/null || true
fi

if [[ -f "$CHECKPOINT" ]]; then
  echo "[stop] removing corrupt checkpoint"
  rm -f "$CHECKPOINT"
fi

if [[ -f "$LOG" ]]; then
  echo "[stop] truncating log ($(wc -c < "$LOG") bytes)"
  tail -n 200 "$LOG" > /tmp/stats-cache-tail.log
  cp /tmp/stats-cache-tail.log "$LOG"
fi

# Also refresh sync plist if present (*/5 cadence)
SYNC_FIXED="$REPO/data/governance/launchd-plists/com.annals.sync.plist"
SYNC_DEST="$HOME/Library/LaunchAgents/com.annals.sync.plist"
if [[ -f "$SYNC_FIXED" ]]; then
  echo "[stop] refreshing sync LaunchAgent (*/5)"
  launchctl bootout "gui/${UID_NUM}/com.annals.sync" 2>/dev/null || true
  cp "$SYNC_FIXED" "$SYNC_DEST"
  launchctl bootstrap "gui/${UID_NUM}" "$SYNC_DEST" 2>/dev/null || true
  launchctl enable "gui/${UID_NUM}/com.annals.sync" 2>/dev/null || true
fi

echo "[stop] status:"
launchctl print "gui/${UID_NUM}/${LABEL}" 2>&1 | awk '/state =|pid =|runs =|last exit/{print}' || true
bash "$REPO/scripts/local_bots/ctl.sh" status 2>&1 | rg 'stats-cache|sync |enrich ' || true
echo "[stop] done — next stats-cache run uses fixed \$id cursor + twice-hourly calendar."
