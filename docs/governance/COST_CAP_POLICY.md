# Cost Cap Policy — Appwrite Pro Plan

> Effective immediately. All automated operations must respect the Pro plan budget.

## 1. Plan Limits (Monthly)

| Resource        | Pro Plan Limit | Alert Threshold (70%) |
| --------------- | -------------: | --------------------: |
| Database Reads  |      1,800,000 |             1,260,000 |
| Database Writes |        750,000 |               525,000 |
| Executions      |      3,500,000 |             2,450,000 |
| Storage         |         150 GB |                105 GB |
| Bandwidth       |           2 TB |                1.4 TB |

**Base cost:** $25/month. Overage rate: ~$0.60 per million database reads.

## 2. Architecture

### Usage Tracker

A document in the `stats_cache` collection (ID: `usage_tracker`) tracks cumulative monthly reads and writes. Every gated cloud function checks this document before executing.

```
{
  "month": "2025-06",
  "totalReads": 450000,
  "totalWrites": 12000,
  "lastFunction": "stats-counter",
  "lastUpdated": "2025-06-15T10:30:00Z"
}
```

The tracker auto-resets when the month changes.

### Budget Gate Logic

All **scheduled** cloud functions call `checkUsageBudget()` from `functions/_shared/helpers.js`:

1. Read the `usage_tracker` document (1 read)
2. If `totalReads > 70%` of monthly limit → **skip execution**, return `{ skipped: true, reason }`
3. If within budget → proceed, then call `trackUsage()` to update the counter

**Manual invocations bypass the gate** — the curator can always trigger a function when needed.

### Gated Functions

| Function             | Schedule       | Estimated Reads/Run | Gate                |
| -------------------- | -------------- | ------------------: | ------------------- |
| stats-counter        | 10 min         |            ~392,000 | ✅                  |
| audit-completeness   | 10 min         |            ~392,000 | ✅                  |
| audit-consistency    | 30 min         |            ~392,000 | ✅                  |
| audit-orphans        | Daily          |            ~400,000 | ✅                  |
| audit-duplicates     | Weekly         |            ~392,000 | ✅                  |
| audit-classification | Daily          |            ~392,000 | ✅                  |
| ai-enrichment        | 4 hours        |             ~50,000 | ✅                  |
| enrichment-queue     | 6 hours        |            ~392,000 | ✅                  |
| backup-export        | Weekly         |            ~400,000 | ✅                  |
| entity-sync          | Event-driven   |           ~10/event | No gate (low cost)  |
| entity-random        | HTTP on-demand |            ~25/call | No gate (on-demand) |

### GitHub Actions

| Workflow             | Previous Trigger   | Current State                                   |
| -------------------- | ------------------ | ----------------------------------------------- |
| ai-enrichment.yml    | Cron every 6 hours | **Disabled** — manual `workflow_dispatch` only  |
| sync-to-appwrite.yml | Push to main       | **Disabled** — manual with `confirm: YES` input |
| ci.yml               | Push/PR            | Unchanged (no Appwrite cost)                    |

## 3. Frontend Optimizations

| Optimization                            | Savings                      |
| --------------------------------------- | ---------------------------- |
| Search collapsed from 5-7 queries to 2  | ~60-70% reduction per search |
| `fetchLabelCounts()` cached (5 min TTL) | 8 queries → 0 on cache hit   |
| `fetchTotalCount()` cached (5 min TTL)  | 1 query → 0 on cache hit     |
| `useGlobalCounts` reads `stats_cache`   | 1 read vs 392K full scan     |

## 4. Curator Alerts

When any function is **skipped due to budget**, the response includes:

```json
{
  "skipped": true,
  "reason": "⚠️ BUDGET ALERT: Database reads at 72% of monthly Pro plan limit (1,296,000 / 1,800,000). Scheduled run skipped to prevent overage charges. Use manual invocation to override."
}
```

### What to Do When Budget Alert Fires

1. **Do not panic** — scheduled runs are paused, not broken
2. **Check Appwrite Console** → Usage tab for actual billing numbers
3. **If you need a specific audit**, invoke the function manually (manual runs bypass the gate)
4. **Wait for month reset** — the tracker resets automatically on the 1st
5. **Reduce frequency** — if alerts fire early in the month, consider reducing cron intervals in `appwrite.json`

## 5. Cost Projection

With all gates active and frontend caching:

| Scenario                                 | Est. Monthly Reads |   Est. Cost |
| ---------------------------------------- | -----------------: | ----------: |
| All crons disabled, frontend only        |            ~50,000 |  $25 (base) |
| Light curation (2-3 manual audits/month) |         ~1,200,000 |  $25 (base) |
| Moderate curation (daily manual audits)  |         ~1,700,000 |  $25 (base) |
| Budget gate triggers (70% threshold)     |         ≤1,260,000 |  $25 (base) |
| **Previous month (no caps)**             |    **186,000,000** | **$135.58** |

## 6. Reactivating Automated Schedules

When the project scales beyond Pro plan limits (e.g., upgraded to Scale plan):

1. Update `PRO_PLAN_LIMITS` in `functions/_shared/helpers.js`
2. Uncomment cron schedules in `.github/workflows/ai-enrichment.yml`
3. Uncomment push trigger in `.github/workflows/sync-to-appwrite.yml`
4. Consider raising `ALERT_THRESHOLD` from 0.70 to 0.85
