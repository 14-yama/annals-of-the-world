# Git-First Bot Architecture

> **Effective:** 2026-05-09
> **Replaces:** Per-bot Appwrite scans/writes that caused the $117 overrun
> in the Mar–Apr 2026 cycle.
>
> **One sentence:** Every bot reads from `data/appwrite-export/entities/` and
> writes to it. A single throttled GitHub Action — the **sync gateway** — is the
> only writer to Appwrite, gated by hard caps in `data/governance/budget.json`.

---

## Why

Each cloud function used to scan ~400K Appwrite documents per run. With 9 such
functions and per-entity writes from `ai-enrichment` retrying through three
fallback strategies, we hit ~130M reads/month and burned $117 on the Pro plan.

By moving every scan/write to GitHub Actions that walk a local git mirror
(`data/appwrite-export/`), the only Appwrite traffic is one daily delta-push
from the sync gateway. Scans cost $0.

---

## Components

```
                         CURATOR (sets policy)
                                 │
                                 ▼
                    data/governance/budget.json
                    data/governance/last_sync.json
                                 │
       ┌─────────────────────────┼──────────────────────────┐
       ▼                         ▼                          ▼
   AUDIT BOTS              AI ENRICHMENT BOT          (manual edits via UI)
   (5 GH workflows)        (1 GH workflow)
       │                         │
       └────── write JSON ──────►│◄────── write JSON ──────┘
                                 │
                 data/appwrite-export/entities/**/*.json
                                 │
                                 ▼
                        SYNC GATEWAY (1 GH workflow)
                                 │
                  ┌──────────────┼──────────────┐
                  ▼              ▼              ▼
           budget.json     git diff       audit_log
           (hard cap)     (delta only)    (replayed from _editLog[])
                                 │
                                 ▼
                            APPWRITE
                                 │
              ┌──────────────────┼─────────────────┐
              ▼                                    ▼
        Frontend reads              entity-random    entity-sync
        (cached, 30–60 min)         (live UI)        (event-driven)
```

---

## Bot inventory

### Retained Appwrite cloud functions (2)

| Function | Purpose | Why retained |
|----------|---------|--------------|
| `entity-random` | Powers the "Random entity" UI button | Live, low volume |
| `entity-sync` | Updates `stats_cache` on entity write events | Event-driven, low volume |

### Decommissioned cloud functions (9)

All have `enabled: false` and `schedule: ""` in [appwrite.json](../../appwrite.json).
Code is preserved on disk for reference, but they will never execute.

| Old function | Replacement |
|---|---|
| `audit-completeness` | [scripts/audits/completeness.py](../../scripts/audits/completeness.py) + audit-completeness.yml |
| `audit-orphans` | scripts/audits/orphans.py + audit-orphans.yml |
| `audit-consistency` | scripts/audits/consistency.py + audit-consistency.yml |
| `audit-duplicates` | scripts/audits/duplicates.py + audit-duplicates.yml |
| `audit-classification` | scripts/audits/classification.py + audit-classification.yml |
| `enrichment-queue` | scripts/enrichment_queue.py |
| `stats-counter` | scripts/audits/stats.py + audit-stats.yml |
| `backup-export` | The git repo IS the backup |
| `ai-enrichment` | scripts/ai_enrich_autonomous.py + ai-enrichment.yml |

### GitHub Actions workflows

| Workflow | Schedule | Writes to Appwrite? |
|----------|----------|---------------------|
| audit-stats.yml | Daily 01:00 UTC | No |
| audit-completeness.yml | Daily 02:00 UTC | No |
| audit-orphans.yml | Daily 03:00 UTC | No |
| audit-consistency.yml | Daily 04:00 UTC | No |
| audit-duplicates.yml | Weekly Sun 05:00 UTC | No |
| audit-classification.yml | Weekly Sun 06:00 UTC | No |
| ai-enrichment.yml | Every 6h | **No** (writes JSON + commits) |
| **sync-gateway.yml** | **Daily 07:00 UTC** | **Yes (only writer)** |

---

## Sync Gateway

`scripts/sync_gateway.ts` is the only writer to Appwrite.

### Flow per run
1. Load [data/governance/budget.json](../../data/governance/budget.json).
   Abort if `manualPause === true` or projected writes ≥ `hardStopPercent` of
   `monthlyWriteCap`.
2. Read `data/governance/last_sync.json` for `lastSyncedCommit`.
3. Compute changed entity files via `git diff --name-only --diff-filter=AMR
   <lastSyncedCommit> HEAD -- data/appwrite-export/entities/`.
4. For each entity in those files:
   - PATCH the entity document (or POST if 404).
   - Replay every `detailsJson._editLog[]` entry into the `audit_log`
     collection (one POST per field-change).
   - Clear `_editLog` and `_unsyncedEdits` from the local file.
   - Sleep `minMsBetweenWrites` between every write.
   - Stop early if `perRunWriteCap` reached.
5. Persist updated `budget.json` (incremented `writesUsed`) and
   `last_sync.json` (new commit SHA), commit them.

### Quota controls
- `monthlyReadCap` / `monthlyWriteCap` — soft monthly ceilings.
- `hardStopPercent` (default 80) — gateway aborts at this percentage.
- `perRunWriteCap` (default 500) — gateway stops after N writes per run.
- `minMsBetweenWrites` (default 250 ms) — rate limit between API calls.
- `manualPause` — set to `true` to halt all syncs without code changes.

### Override flags
- `--dry-run` — compute diff and print what would be written. Zero API calls.
- `--full` — ignore `last_sync.json`, sync everything (emergency rebuild).
- `--max=N` — temporary override of `perRunWriteCap`.

---

## Edit-log convention (`_editLog[]`)

Bots and curators record per-field changes inside `detailsJson._editLog[]`:

```json
{
  "timestamp": "2026-05-09T14:00:00Z",
  "editorId": "ai-enrichment-bot:gemini-2.5-flash",
  "field": "summary",
  "oldValue": "...",
  "newValue": "..."
}
```

Last 50 entries are kept per entity. The sync gateway replays each entry as an
`audit_log` row, then clears the array. This means audit history is built
**deterministically from git diffs**, not from per-bot writes.

---

## Curator workflow

| Action | Where | Frequency |
|--------|-------|-----------|
| Set monthly caps | `data/governance/budget.json` | Once / monthly tuning |
| Pause everything | Set `manualPause: true` in budget.json | Emergency |
| Review audit reports | `data/audit-reports/*.json` (committed daily) | Weekly |
| Review enrichments | git log on `data/appwrite-export/entities/` | Weekly |
| Adjust thresholds | `scripts/ai_enrich_autonomous.py` | As needed |
| Run sync manually | Trigger `sync-gateway.yml` from Actions tab | Ad hoc |

---

## Roll-out checklist

- [x] Phase 1 — disable all schedules in appwrite.json (no more crons hitting Appwrite)
- [x] Phase 2 — port 5 audits + stats to Python + GH Actions
- [x] Phase 3 — strip Appwrite writes from ai_enrich_autonomous.py; add `_editLog[]`
- [x] Phase 4 — sync_gateway.ts + sync-gateway.yml
- [x] Phase 6 — budget.json governance file
- [ ] Phase 5 — delete deprecated `functions/<name>/` folders (deferred — keep code on disk)
- [ ] Update `ui/src/pages/AuditLogViewer.tsx` to read `data/audit-reports/*.json`
- [ ] First end-to-end gateway run + verify cost telemetry

---

## See also

- [autonomous_enrichment.md](autonomous_enrichment.md) — original enrichment policy (largely superseded by this doc)
- [COST_CAP_POLICY.md](COST_CAP_POLICY.md) — June 2025 cost-cap fixes
- [data/audit-reports/README.md](../../data/audit-reports/README.md)
- [data/governance/budget.json](../../data/governance/budget.json)
