#!/usr/bin/env bash
# install_local_services.sh — One-time setup for local 24/7 bot stack.
#
# What this does:
#   1. Installs systemd user units (local_bot_server + daemon loop)
#   2. Enables and starts the units so they survive reboots
#   3. Installs a cron watchdog as belt-and-suspenders backup
#   4. Creates the required directories
#   5. Writes ~/.config/annals/env as a shared env file
#
# Usage:
#   bash scripts/install_local_services.sh
#   bash scripts/install_local_services.sh --uninstall  (remove everything)

set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SYSTEMD_USER_DIR="$HOME/.config/systemd/user"
CRON_TAG="annals-watchdog"

BLUE='\033[0;34m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'
RED='\033[0;31m'; NC='\033[0m'

info()    { echo -e "${BLUE}[install]${NC} $*"; }
success() { echo -e "${GREEN}[ok]${NC} $*"; }
warn()    { echo -e "${YELLOW}[warn]${NC} $*"; }
error()   { echo -e "${RED}[error]${NC} $*"; exit 1; }

UNINSTALL=0
for arg in "$@"; do [[ "$arg" == "--uninstall" ]] && UNINSTALL=1; done

# ─── Uninstall path ───────────────────────────────────────────────────────────
if [[ $UNINSTALL -eq 1 ]]; then
    info "Removing Annals local bot services…"
    systemctl --user stop  annals-local-bot-server.service annals-local-bots.service 2>/dev/null || true
    systemctl --user disable annals-local-bot-server.service annals-local-bots.service 2>/dev/null || true
    rm -f "$SYSTEMD_USER_DIR/annals-local-bot-server.service"
    rm -f "$SYSTEMD_USER_DIR/annals-local-bots.service"
    # Remove cron entry
    crontab -l 2>/dev/null | grep -v "$CRON_TAG" | crontab - || true
    success "Uninstalled. Run 'systemctl --user daemon-reload' to confirm."
    exit 0
fi

# ─── Pre-flight checks ────────────────────────────────────────────────────────
info "Pre-flight checks…"
command -v python3 > /dev/null || error "python3 not found"
command -v systemctl > /dev/null || warn "systemctl not found — systemd units will be skipped"

# ─── Create directories ───────────────────────────────────────────────────────
mkdir -p "$SYSTEMD_USER_DIR"
mkdir -p "$HOME/.config/annals"
mkdir -p /tmp/annals-bots
mkdir -p "$REPO_DIR/data/governance/bot_kpi"

# ─── Write shared env config ──────────────────────────────────────────────────
ENV_FILE="$HOME/.config/annals/env"
if [[ ! -f "$ENV_FILE" ]]; then
    info "Writing $ENV_FILE (shared env for all bot services)"
    cat > "$ENV_FILE" << 'EOF'
# Annals local bot configuration
# Edit these values to tune behaviour

ENRICH_COUNT=5           # entities per enrichment cycle
SIG_COUNT=5              # entities per significance cycle
INTERVAL=30              # minutes between cycles
OLLAMA_MODEL=llama3.2:3b # Ollama model to use
OLLAMA_HOST=http://localhost:11434
LOG_DIR=/tmp
EOF
    success "Created $ENV_FILE"
else
    info "$ENV_FILE already exists — skipping"
fi

# ─── Install systemd units ────────────────────────────────────────────────────
if command -v systemctl > /dev/null; then
    info "Installing systemd user units…"

    # Unit 1: bot server (API on port 7474)
    sed "s|/home/manasa151/annals-of-the-world|$REPO_DIR|g" \
        "$REPO_DIR/scripts/annals-local-bot-server.service" \
        > "$SYSTEMD_USER_DIR/annals-local-bot-server.service"

    # Unit 2: daemon loop (24/7 enrichment)
    sed "s|/home/manasa151/annals-of-the-world|$REPO_DIR|g" \
        "$REPO_DIR/scripts/annals-local-bots.service" \
        > "$SYSTEMD_USER_DIR/annals-local-bots.service"

    # Patch WorkingDirectory in both units
    for unit_file in \
        "$SYSTEMD_USER_DIR/annals-local-bot-server.service" \
        "$SYSTEMD_USER_DIR/annals-local-bots.service"; do
        sed -i "s|WorkingDirectory=.*|WorkingDirectory=$REPO_DIR|g" "$unit_file"
        # Add EnvironmentFile line if not present
        if ! grep -q "EnvironmentFile" "$unit_file"; then
            sed -i "/\[Service\]/a EnvironmentFile=-$ENV_FILE" "$unit_file"
        fi
    done

    systemctl --user daemon-reload

    for unit in annals-local-bot-server.service annals-local-bots.service; do
        systemctl --user enable "$unit" 2>/dev/null && success "Enabled  $unit" || warn "Could not enable $unit"
        systemctl --user restart "$unit" 2>/dev/null && success "Restarted $unit" || warn "Could not restart $unit (Ollama may not be running yet)"
    done

    # Enable linger so units survive user logout
    loginctl enable-linger "$(whoami)" 2>/dev/null && \
        success "Linger enabled — services survive logout/reboot" || \
        warn "Could not enable linger (you may need to log in to activate services after reboot)"
else
    warn "systemctl not available — skipping systemd unit installation"
fi

# ─── Install cron watchdog ────────────────────────────────────────────────────
info "Installing cron watchdog (runs every 5 minutes)…"
chmod +x "$REPO_DIR/scripts/local_bot_cron_watchdog.sh"

CRON_LINE="*/5 * * * * $REPO_DIR/scripts/local_bot_cron_watchdog.sh >> /tmp/annals-watchdog.log 2>&1  # $CRON_TAG"

# Remove old entry if exists, then add fresh
( crontab -l 2>/dev/null | grep -v "$CRON_TAG" ; echo "$CRON_LINE" ) | crontab -
success "Cron watchdog installed"

echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}  Annals local bot stack installed successfully!${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════${NC}"
echo ""
echo "  Bot server (port 7474):  systemctl --user status annals-local-bot-server"
echo "  Daemon loop:             systemctl --user status annals-local-bots"
echo "  Cron watchdog:           crontab -l | grep annals"
echo "  Watchdog log:            tail -f /tmp/annals-watchdog.log"
echo "  Daemon log:              tail -f /tmp/annals-daemon.log"
echo ""
echo "  Config:                  $ENV_FILE"
echo ""
