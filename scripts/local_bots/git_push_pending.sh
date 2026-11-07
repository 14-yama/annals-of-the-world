#!/usr/bin/env bash
# Commit + push pending Annals enrichment/entity/audit changes.
# Does not print .env secrets. Soft-noops when the tree is clean.
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$REPO_DIR"

export GIT_AUTHOR_NAME="${GIT_AUTHOR_NAME:-Annals Local Bot}"
export GIT_AUTHOR_EMAIL="${GIT_AUTHOR_EMAIL:-local-bot@annals-of-the-world.bot}"
export GIT_COMMITTER_NAME="${GIT_COMMITTER_NAME:-Annals Local Bot}"
export GIT_COMMITTER_EMAIL="${GIT_COMMITTER_EMAIL:-local-bot@annals-of-the-world.bot}"

pending="$(git status --porcelain -- data/appwrite-export/ data/enrichment/ data/governance/ data/audit-reports/ 2>/dev/null | wc -l | tr -d ' ')"
if [[ "${pending}" == "0" ]]; then
  echo "[push] nothing pending"
  exit 0
fi

echo "[push] staging ${pending} dirty paths under data/"
git add data/appwrite-export/ data/enrichment/ data/governance/ data/audit-reports/ 2>/dev/null || true

if git diff --cached --quiet; then
  echo "[push] nothing staged after add"
  exit 0
fi

entities="$(git diff --cached --name-only -- data/appwrite-export/entities/ | wc -l | tr -d ' ')"
edges="$(git diff --cached --name-only -- data/appwrite-export/edges/ | wc -l | tr -d ' ')"
msg="feat(data): local-bot push — ${entities} entities, ${edges} edges

Automated Mac Mini local-bot commit."

git commit -m "$msg" || {
  echo "[push] commit skipped/failed"
  exit 0
}

if git push; then
  echo "[push] ok — pushed entities=${entities} edges=${edges}"
else
  echo "[push] git push failed — check credentials (no secrets logged)"
  exit 1
fi
