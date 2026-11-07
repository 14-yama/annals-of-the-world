#!/usr/bin/env bash
# Annals local-bot control on macOS Mini.
#
#   bash scripts/local_bots/ctl.sh status
#   bash scripts/local_bots/ctl.sh start
#   bash scripts/local_bots/ctl.sh stop
#   bash scripts/local_bots/ctl.sh restart
#   bash scripts/local_bots/ctl.sh gate
#   bash scripts/local_bots/ctl.sh run <bot-id>
#   bash scripts/local_bots/ctl.sh logs [bot-id]
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
SOT="$REPO_DIR/data/governance/platform-local-bots.json"
LOG_DIR="${HOME}/Library/Logs/annals-bots"
UID_NUM="$(id -u)"
PREFIX="com.annals."

PYTHON="python3"
[[ -x "$REPO_DIR/.venv/bin/python3" ]] && PYTHON="$REPO_DIR/.venv/bin/python3"

list_labels() {
  "$PYTHON" - <<PY
import json
from pathlib import Path
sot = json.loads(Path("$SOT").read_text())
for b in sot.get("bots") or []:
    label = (b.get("launchd") or {}).get("label") or f"$PREFIX{b['id']}"
    print(label)
PY
}

cmd="${1:-status}"
shift || true

case "$cmd" in
  status)
    echo "=== Annals local bots (launchd) ==="
    while read -r label; do
      state="missing"
      if launchctl print "gui/${UID_NUM}/${label}" >/dev/null 2>&1; then
        state="$(launchctl print "gui/${UID_NUM}/${label}" 2>/dev/null | awk -F'= ' '/state =/{print $2; exit}')"
        state="${state:-loaded}"
      fi
      printf "  %-40s %s\n" "$label" "$state"
    done < <(list_labels)
    echo ""
    echo "=== Concurrency / Superstack blackout gate ==="
    "$PYTHON" "$REPO_DIR/scripts/local_bots/concurrency_gate.py" status
    echo ""
    echo "=== Protected Superstack scrapers (do not interrupt) ==="
    for label in com.caricom.media-daily-new-articles com.caricom.media-archive-backfill-listing; do
      state="missing"
      if launchctl print "gui/${UID_NUM}/${label}" >/dev/null 2>&1; then
        state="$(launchctl print "gui/${UID_NUM}/${label}" 2>/dev/null | awk -F'= ' '/state =/{print $2; exit}')"
        state="${state:-loaded}"
      fi
      printf "  %-40s %s\n" "$label" "$state"
    done
    ;;
  start)
    "$PYTHON" "$REPO_DIR/scripts/local_bots/install_mac_launch_agents.py"
    ;;
  stop)
    while read -r label; do
      echo "bootout $label"
      launchctl bootout "gui/${UID_NUM}/${label}" 2>/dev/null || true
    done < <(list_labels)
    ;;
  restart)
    bash "$0" stop
    bash "$0" start
    ;;
  uninstall)
    "$PYTHON" "$REPO_DIR/scripts/local_bots/install_mac_launch_agents.py" --uninstall
    ;;
  gate)
    "$PYTHON" "$REPO_DIR/scripts/local_bots/concurrency_gate.py" status
    ;;
  run)
    bot_id="${1:?bot-id required}"
    /bin/zsh "$REPO_DIR/scripts/local_bots/run_job.zsh" --bot-id "$bot_id"
    ;;
  logs)
    bot_id="${1:-}"
    mkdir -p "$LOG_DIR"
    if [[ -n "$bot_id" ]]; then
      tail -n 80 "$LOG_DIR/${bot_id}.log" 2>/dev/null || echo "no log yet: $LOG_DIR/${bot_id}.log"
    else
      ls -lt "$LOG_DIR" 2>/dev/null | head -20
    fi
    ;;
  *)
    echo "Usage: $0 {status|start|stop|restart|uninstall|gate|run <id>|logs [id]}"
    exit 2
    ;;
esac
