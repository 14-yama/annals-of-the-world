# Local Docker Appwrite (Mac Mini)

Local Appwrite is the **UI + bot sync target**. Cloud is a one-way source of old documents during staged merge.

## URLs

| What | URL |
|------|-----|
| Console | http://localhost:8080/console/ |
| API | http://localhost:8080/v1 |
| Vite UI | http://localhost:5173/ |

Runtime: **Colima** + Docker Compose under [`docker/appwrite/`](../../docker/appwrite/).

## Console login

Local root admin (created at install):

- Email: `annals-local@localhost.dev`
- Password: `AnnalsLocal2026!`

Open http://localhost:8080/console/ and sign in with those credentials.

### GitHub OAuth (optional)

`gh` was not logged in on this host when the stack was cut over, so GitHub OAuth was **not** auto-wired. To use your GitHub login:

1. Create a GitHub OAuth App (Settings → Developer settings → OAuth Apps):
   - Homepage: `http://localhost:8080`
   - Authorization callback URL: `http://localhost:8080/v1/account/sessions/oauth2/callback/github`
2. In Appwrite Console → project **Annals of the World** → Auth → Settings → GitHub:
   - paste Client ID / Client Secret
   - enable the provider
3. Do **not** put your GitHub password in repo files or chat.

Until OAuth is configured, use the local admin email/password above.

## Project

| Field | Value |
|-------|-------|
| Project ID | `annals-local` |
| Project name | Annals of the World |
| Database ID | `annals_world_db` |
| Web platforms | `localhost`, `127.0.0.1` |

Secrets live in gitignored files:

- `ui/.env` — Vite client + server key for local
- `.env` — script defaults for local
- `~/.config/annals/env` — LaunchAgent / bot shared env
- `.env.cloud-merge` — cloud read + local write for staged merge
- `docker/appwrite/.env` — Appwrite stack secrets

## Start / stop stack

```bash
export DOCKER_HOST="unix://${HOME}/.colima/docker.sock"
colima status || colima start --cpu 4 --memory 8 --disk 60
cd docker/appwrite && docker compose up -d
# open console
open http://localhost:8080/console/
```

## Data flow

1. Bots write git JSON under `data/appwrite-export/` with `_unsyncedEdits`.
2. `sync_gateway.ts --local` upserts to **local** Appwrite only.
3. Cron `merge_cloud_to_local_appwrite.ts` create-if-missing from cloud → local (never overwrites local-only / dirty docs).
4. New local docs are **not** pushed to cloud.

## Cutover flag

`data/governance/platform-local-bots.json` → `meta.appwrite_cutover.employ_bots`.

- `false` — enrich / significance / sync / push / edges-extract stay paused
- `true` — those bots may run (still gated by Superstack blackouts + 1 LLM lane)

```bash
bash scripts/local_bots/ctl.sh status
bash scripts/local_bots/ctl.sh gate
```

## Seed / merge ops

**Bulk fill path (preferred):** git export → local create-if-missing, then cloud side-path backup for delta/audit. Do **not** blind-overwrite `data/appwrite-export/` from cloud (preserves `_unsyncedEdits`).

- Cloud backup dir: `data/backups/cloud-YYYYMMDD/` (gitignored)
- Seed cursor: `data/governance/seed_local_cursor.json`
- `seed-local`: every 10 min, `--max=5000 --fast`
- `merge-cloud` / `merge-cloud-audit`: **delta-only** every 6h (small `--max`); unload during bulk seed if they contend on `network_write`

```bash
# Cloud backup to side path (does not clobber live export)
set -a && source .env.cloud-merge && set +a
export VITE_APPWRITE_ENDPOINT="$CLOUD_APPWRITE_ENDPOINT"
export VITE_APPWRITE_PROJECT_ID="$CLOUD_APPWRITE_PROJECT_ID"
export VITE_APPWRITE_DATABASE_ID="$CLOUD_APPWRITE_DATABASE_ID"
export APPWRITE_API_KEY="$CLOUD_APPWRITE_API_KEY"
npx tsx scripts/sync_appwrite_to_repo.ts --out=data/backups/cloud-$(date +%Y%m%d)

# Aggressive git → local seed (create-if-missing; cursor advances)
set -a && source .env && set +a
npx tsx scripts/sync_repo_to_appwrite.ts --max=50000 --fast --collection=entities

# Import side-path backup create-if-missing (entities / audit_log)
npx tsx scripts/sync_repo_to_appwrite.ts --source=data/backups/cloud-YYYYMMDD --max=5000 --fast --collection=entities
npx tsx scripts/sync_repo_to_appwrite.ts --source=data/backups/cloud-YYYYMMDD --collection=audit_log --fast

# Live cloud → local delta (small)
npx tsx scripts/merge_cloud_to_local_appwrite.ts --max=100 --collection=entities
# cursor: data/governance/cloud_merge_cursor.json
```

## What to do next (human)

1. Open http://localhost:8080/console/ and sign in with the local admin email/password above.
2. Confirm project **Annals of the World** (`annals-local`) and database `annals_world_db`.
3. Open http://localhost:5173/ — UI should read local Appwrite.
4. Optional: add GitHub OAuth (see above) after `gh auth login`, then enable GitHub under Auth → Settings.
5. Watch bots: `bash scripts/local_bots/ctl.sh status` and `bash scripts/local_bots/ctl.sh logs enrich`.
