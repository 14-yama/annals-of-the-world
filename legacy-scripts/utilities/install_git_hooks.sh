#!/usr/bin/env bash
# Install git hooks (local copy) to run normalization before commit.
# Usage: `bash scripts/install_git_hooks.sh`

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HOOKS_DIR="$ROOT_DIR/.git/hooks"
PRECOMMIT="$HOOKS_DIR/pre-commit"

if [ ! -d "$ROOT_DIR/.git" ]; then
  echo "No .git directory found in project root; run this from the repo workspace." >&2
  exit 1
fi

cat > "$PRECOMMIT" <<'HOOK'
#!/usr/bin/env bash
set -euo pipefail
echo "Running project normalizers before commit..."
python3 scripts/normalize_all.py
HOOK

chmod +x "$PRECOMMIT"
echo "Installed pre-commit hook to $PRECOMMIT"
