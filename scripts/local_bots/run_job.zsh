#!/bin/zsh
# launchd entrypoint for Annals local bots.
# Loads repo .env without printing values, then runs dispatch_bot.py.
set -euo pipefail
unsetopt xtrace 2>/dev/null || true

repo_root="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$repo_root"

export PATH="/opt/homebrew/bin:${HOME}/.local/bin:/usr/bin:/bin:/usr/sbin:/sbin:${PATH:-}"
export PYTHONUNBUFFERED=1

bot_id=""
if [[ "${1:-}" == "--bot-id" ]]; then
  bot_id="${2:-}"
  shift 2
fi
if [[ -z "$bot_id" ]]; then
  echo "run_job.zsh: missing --bot-id" >&2
  exit 64
fi

# Shared env (~/.config/annals/env) — no secrets required for most bots
shared_env="${HOME}/.config/annals/env"
if [[ -f "$shared_env" ]]; then
  set -a
  # shellcheck disable=SC1090
  source "$shared_env"
  set +a
fi

# Repo .env — load keys into env without echoing values
env_file="${repo_root}/.env"
if [[ -f "$env_file" ]]; then
  while IFS= read -r line || [[ -n "$line" ]]; do
    line="${line%$'\r'}"
    [[ "$line" =~ ^[[:space:]]*$ ]] && continue
    [[ "$line" =~ ^[[:space:]]*# ]] && continue
    line="${line#export }"
    [[ "$line" == *=* ]] || continue
    key="${line%%=*}"
    value="${line#*=}"
    key="${key#"${key%%[![:space:]]*}"}"
    key="${key%"${key##*[![:space:]]}"}"
    [[ "$key" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]] || continue
    if [[ "$value" == \"*\" && "$value" == *\" ]]; then
      value="${value[2,-2]}"
    elif [[ "$value" == \'*\' && "$value" == *\' ]]; then
      value="${value[2,-2]}"
    fi
    export "${key}=${value}"
  done < "$env_file"
fi

python_bin="python3"
if [[ -x "${repo_root}/.venv/bin/python3" ]]; then
  python_bin="${repo_root}/.venv/bin/python3"
fi

echo "[annals-launchd] start $(date '+%Y-%m-%d %H:%M:%S %Z') bot=${bot_id}"
"${python_bin}" "${repo_root}/scripts/local_bots/dispatch_bot.py" --bot-id "${bot_id}"
job_rc=$?
echo "[annals-launchd] end $(date '+%Y-%m-%d %H:%M:%S %Z') bot=${bot_id} status=${job_rc}"
exit "${job_rc}"
