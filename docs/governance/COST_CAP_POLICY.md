# Cost Cap Policy — Appwrite Pro Plan

> **Effective immediately.** All automated operations must respect the Pro plan budget.
> **Last updated:** June 2025. Next review: July 23, 2025 (start of billing cycle).

---

## 1. Billing & Plan Details

| Item                | Value                                        |
| ------------------- | -------------------------------------------- |
| **Plan**            | Appwrite Pro ($25/month base)                |
| **Billing cycle**   | 23rd of each month → 22nd of next month      |
| **Payment date**    | 22nd of each month                           |
| **Overage rate**    | ~$0.60 per million database reads beyond cap |
| **Project ID**      | `66509ba7003618a05af6`                       |
| **Database**        | `annals_db` / `annals_world_db`              |

### Monthly Resource Limits

| Resource        | Pro Plan Limit | Alert (70%) | Hard Cap (90%) |
| --------------- | -------------: | ----------: | -------------: |
| Database Reads  |      1,800,000 |   1,260,000 |      1,620,000 |
| Database Writes |        750,000 |     525,000 |        675,000 |
| Executions      |      3,500,000 |   2,450,000 |      3,150,000 |
| Storage         |         150 GB |      105 GB |         135 GB |
| Bandwidth       |           2 TB |      1.4 TB |          1.8 TB |

### Cost Incident Log

| Billing Cycle       | Reads Used  | Overage   | Root Cause                                          |
| -------------------- | ----------: | --------: | --------------------------------------------------- |
| Mar 23 – Apr 22 2026 | 198,000,000 | $117.60   | audit-consistency at */30 (130M+), broken trackUsage |
| Apr 23 – May 22 2026 | TBD         | TBD       | Fixes deployed — monitoring                         |

---

## 2. Architecture

### Usage Tracker

A document in the `stats_cache` collection (ID: `usage_tracker`) tracks cumulative
reads and writes for the **current billing cycle**. Every gated cloud function
checks this document before executing.

```json
{
  "readsUsed": 450000,
  "writesUsed": 12000,
  "cycleStart": "2025-06-23T00:00:00.000Z",
  "lastFunction": "ai-enrichment",
  "lastRunAt": "2025-06-25T10:30:00Z"
}
```

The tracker **auto-resets** when the billing cycle boundary (23rd of each month) is
detected by `getBillingCycleStart()` in `helpers.js`.

### Budget Gate Logic (Two Tiers)

All cloud functions call `checkUsageBudget()` from `functions/_shared/helpers.js`:

1. Read the `usage_tracker` document (1 read)
2. Check if billing cycle has reset → auto-reset tracker if new cycle
3. **Soft cap (70%):** Scheduled functions → skip. Manual invocations → allowed.
4. **Hard cap (90%):** ALL functions blocked, including manual. Only override with
   `USAGE_CAP_ENABLED=false` env var.
5. If within budget → proceed, then call `trackUsage()` to update the counter

### helpers.js Deployment

The shared `helpers.js` must be copied into each function's `src/` directory:

```bash
for fn in functions/*/src; do
  cp functions/_shared/helpers.js "$fn/helpers.js"
done
```

**CRITICAL:** Without this copy, `require('./helpers')` silently fails in try/catch
and the entire budget gate is bypassed. This was the root cause of the Mar–Apr 2026
$117.60 overrun.

### Gated Functions (Current Schedules)

| Function             | Schedule          | Est. Reads/Run | Monthly Reads | Gate  |
| -------------------- | ----------------- | -------------: | ------------: | ----- |
| audit-consistency    | **DISABLED**      |       ~400,000 |             0 | ✅    |
| audit-completeness   | on-demand only    |       ~400,000 |             0 | ✅    |
| stats-counter        | on-demand only    |       ~400,000 |             0 | ✅    |
| audit-orphans        | Weekly (Sun 03:00)|       ~800,000 |      ~200,000 | ✅    |
| audit-classification | Weekly (Sun 06:00)|       ~400,000 |      ~100,000 | ✅    |
| audit-duplicates     | 2×/month (1st,15th)|      ~400,000 |      ~100,000 | ✅    |
| enrichment-queue     | Weekly (Sun 00:00)|       ~400,000 |      ~100,000 | ✅    |
| backup-export        | 2×/month (1st,15th)|      ~400,000 |      ~100,000 | ✅    |
| ai-enrichment        | Every 4h          |          ~200  |       ~36,000 | ✅    |
| entity-sync          | Event-driven      |      ~10/event |       ~10,000 | No    |
| entity-random        | HTTP on-demand    |       ~25/call |        ~5,000 | No    |

**Projected monthly reads with current schedules: ~650,000 (36% of cap)**

### Read Budget Breakdown (Monthly Allocation)

| Category               | Allocated Reads | % of Cap |
| ---------------------- | --------------: | -------: |
| Scheduled functions    |        ~600,000 |      33% |
| Frontend traffic       |         ~50,000 |       3% |
| Manual curator audits  |        ~400,000 |      22% |
| **Reserve/headroom**   |    **~750,000** |  **42%** |
| **Total monthly cap**  |  **1,800,000**  | **100%** |

### GitHub Actions

| Workflow             | Previous Trigger   | Current State                                   |
| -------------------- | ------------------ | ----------------------------------------------- |
| ai-enrichment.yml    | Cron every 6 hours | **Disabled** — manual `workflow_dispatch` only   |
| sync-to-appwrite.yml | Push to main       | **Disabled** — manual with `confirm: YES` input  |
| ci.yml               | Push/PR            | Unchanged (no Appwrite cost)                     |

---

## 3. Frontend Optimizations

| Optimization                             | Impact                        |
| ---------------------------------------- | ----------------------------- |
| Search: 5-7 queries → 2 max              | ~60-70% reduction per search  |
| `fetchLabelCounts()` in-memory (30 min)  | 8 queries → 0 on cache hit   |
| `fetchTotalCount()` in-memory (30 min)   | 1 query → 0 on cache hit     |
| `useGlobalCounts` localStorage (60 min)  | 1 read vs 400K full scan     |
| `countAllDocuments` localStorage (24h)   | 1 read vs 4000+ API calls    |
| ClassHub/DivisionDetail cached counts    | Prevents re-pagination        |

---

## 4. Checks & Balances

### Automated Safeguards

1. **Budget gate** — `checkUsageBudget()` called at start of every function
2. **Usage tracking** — `trackUsage()` called at end of every function
3. **Billing cycle auto-reset** — tracker resets on the 23rd automatically
4. **Soft cap at 70%** — scheduled functions stop, manual still allowed
5. **Hard cap at 90%** — all functions stop until next billing cycle
6. **helpers.js copy verification** — each function's `src/` must contain helpers.js

### Manual Review Schedule

| When                  | Action                                              |
| --------------------- | --------------------------------------------------- |
| Weekly (every Sunday) | Check Appwrite Console → Usage tab                  |
| 15th of each month    | Midcycle review — project remaining reads to month end |
| 22nd of each month    | Pre-billing review — ensure no surprise overages     |
| 23rd of each month    | Verify tracker auto-reset for new billing cycle      |
| After any deployment  | Verify helpers.js is in all function src/ dirs       |

### Escalation Protocol

| Read Usage Level | Action                                              |
| :--------------: | --------------------------------------------------- |
|       < 50%      | Normal operations                                   |
|    50% – 70%     | Monitor weekly, no schedule changes needed           |
|    70% – 80%     | Soft cap fires. Disable any remaining scheduled scans |
|    80% – 90%     | Emergency: disable ALL schedules in appwrite.json    |
|      > 90%       | Hard cap fires. All functions blocked automatically  |

### Preventing Future Overruns

1. **Never set schedule to `*/N * * * *`** (every N minutes) for full-scan functions
2. **Always copy helpers.js** when adding new functions
3. **Always add `trackUsage()`** to new function code before the final `return`
4. **Test schedule math**: multiply reads/run × runs/month before deploying
5. **Use `Query.select()`** to minimize read costs when possible
6. **Use `stats_cache` collection** instead of full-scan recounting

---

## 5. Curator Alerts

When any function is **skipped due to budget**, the response includes:

```json
{
  "skipped": true,
  "reason": "CURATOR ALERT: Database reads at 72% of Pro limit. Scheduled function SKIPPED."
}
```

### What to Do When Budget Alert Fires

1. **Do not panic** — scheduled runs are paused, not broken
2. **Check Appwrite Console** → Usage tab for actual billing numbers
3. **If you need a specific audit**, invoke manually (if < 90%)
4. **Wait for cycle reset** — automatic on the 23rd
5. **Reduce frequency** — if alerts fire early, increase intervals in `appwrite.json`

---

## 6. Cost Projection

| Scenario                                 | Est. Monthly Reads |   Est. Cost |
| ---------------------------------------- | -----------------: | ----------: |
| All crons disabled, frontend only        |            ~50,000 |  $25 (base) |
| Current schedules (post-fix)             |          ~650,000  |  $25 (base) |
| Light curation (2-3 manual audits/month) |         ~1,250,000 |  $25 (base) |
| Moderate curation (daily manual audits)  |         ~1,700,000 |  $25 (base) |
| Budget gate triggers (70% threshold)     |         ≤1,260,000 |  $25 (base) |
| **Pre-fix (no caps, Mar–Apr 2026)**      |    **198,000,000** | **$142.60** |

---

## 7. Reactivating Automated Schedules

When the project scales beyond Pro plan limits (e.g., upgraded to Scale plan):

1. Update `PRO_PLAN_LIMITS` in `functions/_shared/helpers.js`
2. Re-copy helpers.js to all function directories
3. Uncomment cron schedules in `.github/workflows/ai-enrichment.yml`
4. Uncomment push trigger in `.github/workflows/sync-to-appwrite.yml`
5. Consider raising `ALERT_THRESHOLD` from 0.70 to 0.85
6. Re-enable `audit-consistency` schedule for real-time stats

---

## 8. AI Model Deployment Guide

### 24/7 Automated (Gemini via API)

| Task                    | Model               | Limit                | Schedule       |
| ----------------------- | -------------------- | -------------------- | -------------- |
| Entity enrichment       | Gemini 2.5 Flash     | Free: 1M tokens/day  | Every 4h       |
| Enrichment queue scan   | N/A (code only)      | N/A                  | Weekly         |
| Quality scoring         | Gemini 2.5 Flash     | 15 RPM free tier     | On enrichment  |

### In-House Models (Manual, No API Cost)

| Tier | Model               | Best For                                          |
| ---: | -------------------- | ------------------------------------------------- |
|    1 | Claude Opus 4.6      | Complex reasoning, architecture, multi-file edits |
|    2 | GPT-5 mini (FREE)    | General coding, documentation, analysis           |
|    3 | Claude Haiku 4.5     | Quick fixes, simple edits, code review            |
|    4 | Gemini 3 Flash       | Fast iteration, prototyping, data tasks           |

### Task Assignment Matrix

| Task Category                    | Primary Model     | Fallback          |
| -------------------------------- | ----------------- | ----------------- |
| Architecture & system design     | Claude Opus 4.6   | GPT-5 mini        |
| Multi-file refactoring           | Claude Opus 4.6   | GPT-5 mini        |
| Entity data enrichment (auto)    | Gemini 2.5 Flash  | GPT-4o-mini (API) |
| Documentation writing            | GPT-5 mini        | Claude Haiku 4.5  |
| Bug fixing & debugging           | Claude Opus 4.6   | Claude Haiku 4.5  |
| Data analysis & scripts          | GPT-5 mini        | Gemini 3 Flash    |
| Quick code review                | Claude Haiku 4.5  | Gemini 3 Flash    |
| Prototyping & exploration        | Gemini 3 Flash    | GPT-5 mini        |
| Cost/budget analysis             | Claude Opus 4.6   | GPT-5 mini        |
| Schema & Cypher queries          | Claude Opus 4.6   | GPT-5 mini        |

### What Gemini Can Do 24/7

While running autonomously within the free tier:

1. **Enrich weak entities** — fill in summaries, causes, effects, relationships
2. **Quality scoring** — validate enrichments against quality gate
3. **Generate relationship data** — create typed relationships between entities
4. **Expand stubs** — detect auto-generated geo-registry stubs and replace with rich narrative
5. **Cross-reference** — link entities across eras, continents, and topics
6. **Validate consistency** — check entity data quality during enrichment pipeline
