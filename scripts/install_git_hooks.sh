#!/usr/bin/env bash
# Installs Annals git hooks into .git/hooks/.
# Run once per clone: bash scripts/install_git_hooks.sh
set -e
REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

mkdir -p .git/hooks
cp scripts/git-hooks/pre-push .git/hooks/pre-push
chmod +x .git/hooks/pre-push

echo "✓ Installed pre-push hook (validates GitHub Actions YAML)"
echo "✓ To bypass once: git push --no-verify"
