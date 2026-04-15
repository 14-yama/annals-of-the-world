/**
 * Shared helpers for Appwrite Functions.
 * Each function copies this file into its own src/ at deploy time.
 * Run: for fn in functions/[star]/src; do cp functions/_shared/helpers.js "$fn/helpers.js"; done
 */
const sdk = require('node-appwrite');

const DATABASE_ID = process.env.APPWRITE_DATABASE_ID || 'annals_world_db';

// ═══════════════════════════════════════════════════════════
// Appwrite Pro Plan — Billing & Usage Caps
// ═══════════════════════════════════════════════════════════
// Billing cycle: 23rd of each month → 22nd of next month
// Current plan: $25/month base (Pro)
// Overage: ~$0.60 per million reads beyond 1.8M
//
// Set USAGE_CAP_ENABLED=false in function env vars to bypass.

const BILLING_CYCLE_DAY = 23; // Billing cycle starts on the 23rd of each month

const PRO_PLAN_LIMITS = {
  DATABASE_READS:   1_800_000,  // 1.8M documents
  DATABASE_WRITES:    750_000,  // 750K operations
  EXECUTIONS:       3_500_000,  // 3.5M
  STORAGE_BYTES:  150 * 1e9,    // 150 GB
  BANDWIDTH_BYTES: 2 * 1e12,    // 2 TB
};

// Alert threshold — stop all scheduled work at 70% of monthly limit.
// Leaves 30% headroom for curator manual audits and frontend traffic.
const ALERT_THRESHOLD = parseFloat(process.env.USAGE_ALERT_THRESHOLD || '0.70');

// Hard cap — absolutely refuse to run at 90%, even for manual invocations
const HARD_CAP_THRESHOLD = parseFloat(process.env.USAGE_HARD_CAP || '0.90');

/**
 * Get the current billing cycle start date.
 * Cycle runs from the 23rd of month N to the 22nd of month N+1.
 */
function getBillingCycleStart() {
  const now = new Date();
  const year = now.getFullYear();
  const month = now.getMonth();
  const day = now.getDate();

  if (day >= BILLING_CYCLE_DAY) {
    return new Date(year, month, BILLING_CYCLE_DAY);
  } else {
    // We're before the 23rd, so cycle started last month
    return new Date(year, month - 1, BILLING_CYCLE_DAY);
  }
}

/**
 * Check if the usage tracker needs to be reset for a new billing cycle.
 */
function shouldResetTracker(tracker) {
  if (!tracker.cycleStart) return true;
  const cycleStart = new Date(tracker.cycleStart);
  const currentCycleStart = getBillingCycleStart();
  return cycleStart < currentCycleStart;
}

/**
 * Check if the current function execution should proceed.
 *
 * Reads usage from the `usage_tracker` document in stats_cache.
 * Each function increments reads/writes there after execution.
 *
 * Returns { allowed: true } or { allowed: false, reason: '...' }
 */
async function checkUsageBudget(databases, log) {
  // Bypass check if explicitly disabled
  if (process.env.USAGE_CAP_ENABLED === 'false') return { allowed: true };

  try {
    let tracker = await databases.getDocument(DATABASE_ID, 'stats_cache', 'usage_tracker');

    // Auto-reset at billing cycle boundary
    if (shouldResetTracker(tracker)) {
      log(`Billing cycle reset: new cycle started ${getBillingCycleStart().toISOString()}`);
      const resetPayload = {
        readsUsed: 0,
        writesUsed: 0,
        cycleStart: getBillingCycleStart().toISOString(),
        lastFunction: 'cycle-reset',
        lastRunAt: new Date().toISOString(),
      };
      await databases.updateDocument(DATABASE_ID, 'stats_cache', 'usage_tracker', resetPayload);
      return { allowed: true, readPct: 0, writePct: 0 };
    }

    const readsUsed   = tracker.readsUsed   || 0;
    const writesUsed  = tracker.writesUsed  || 0;

    const readPct  = readsUsed  / PRO_PLAN_LIMITS.DATABASE_READS;
    const writePct = writesUsed / PRO_PLAN_LIMITS.DATABASE_WRITES;

    // Hard cap — refuse even manual invocations
    if (readPct >= HARD_CAP_THRESHOLD) {
      const msg = `HARD CAP: Database reads at ${(readPct * 100).toFixed(1)}% of Pro limit (${readsUsed.toLocaleString()} / ${PRO_PLAN_LIMITS.DATABASE_READS.toLocaleString()}). ALL FUNCTIONS BLOCKED until cycle resets on the 23rd.`;
      log(msg);
      return { allowed: false, reason: msg };
    }

    if (readPct >= ALERT_THRESHOLD) {
      const msg = `CURATOR ALERT: Database reads at ${(readPct * 100).toFixed(1)}% of Pro limit (${readsUsed.toLocaleString()} / ${PRO_PLAN_LIMITS.DATABASE_READS.toLocaleString()}). Scheduled function SKIPPED. Run manually if needed.`;
      log(msg);
      return { allowed: false, reason: msg };
    }
    if (writePct >= ALERT_THRESHOLD) {
      const msg = `CURATOR ALERT: Database writes at ${(writePct * 100).toFixed(1)}% of Pro limit (${writesUsed.toLocaleString()} / ${PRO_PLAN_LIMITS.DATABASE_WRITES.toLocaleString()}). Scheduled function SKIPPED. Run manually if needed.`;
      log(msg);
      return { allowed: false, reason: msg };
    }

    return { allowed: true, readPct, writePct };
  } catch {
    // usage_tracker doesn't exist yet — allow execution and create it
    return { allowed: true, reason: 'tracker not found — first run' };
  }
}

/**
 * Increment usage counters after a function completes.
 * Call this at the end of every function run.
 */
async function trackUsage(databases, reads, writes, functionName, log) {
  try {
    let tracker;
    try {
      tracker = await databases.getDocument(DATABASE_ID, 'stats_cache', 'usage_tracker');
    } catch {
      // Create tracker on first run
      tracker = {
        readsUsed: 0,
        writesUsed: 0,
        cycleStart: getBillingCycleStart().toISOString(),
        lastFunction: '',
        lastRunAt: '',
      };
    }

    // Auto-reset if new billing cycle
    if (shouldResetTracker(tracker)) {
      log(`Billing cycle auto-reset in trackUsage`);
      tracker.readsUsed = 0;
      tracker.writesUsed = 0;
      tracker.cycleStart = getBillingCycleStart().toISOString();
    }

    const newReads  = (tracker.readsUsed  || 0) + reads;
    const newWrites = (tracker.writesUsed || 0) + writes;

    const payload = {
      readsUsed:   newReads,
      writesUsed:  newWrites,
      lastFunction: functionName,
      lastRunAt:   new Date().toISOString(),
      updatedAt:   new Date().toISOString(),
      cycleStart:  tracker.cycleStart || getBillingCycleStart().toISOString(),
    };

    try {
      await databases.updateDocument(DATABASE_ID, 'stats_cache', 'usage_tracker', payload);
    } catch {
      // On create, include required stats_cache schema fields with defaults
      const createPayload = {
        ...payload,
        total: tracker.total || 0,
        byLabel: tracker.byLabel || '{}',
        byEra: tracker.byEra || '{}',
        byContinent: tracker.byContinent || '{}',
        byClass: tracker.byClass || '{}',
      };
      await databases.createDocument(DATABASE_ID, 'stats_cache', 'usage_tracker', createPayload);
    }

    const readPct  = ((newReads / PRO_PLAN_LIMITS.DATABASE_READS) * 100).toFixed(1);
    const writePct = ((newWrites / PRO_PLAN_LIMITS.DATABASE_WRITES) * 100).toFixed(1);
    log(`Usage tracked: +${reads}R/+${writes}W | Total: ${newReads.toLocaleString()}R (${readPct}%) / ${newWrites.toLocaleString()}W (${writePct}%)`);
  } catch (err) {
    log(`Warning: usage tracking failed — ${err.message}`);
  }
}

function initClient() {
  const client = new sdk.Client();
  client
    .setEndpoint(process.env.APPWRITE_ENDPOINT || 'https://fra.cloud.appwrite.io/v1')
    .setProject(process.env.APPWRITE_FUNCTION_PROJECT_ID)
    .setKey(process.env.APPWRITE_API_KEY);
  return client;
}

/**
 * Paginate through ALL documents in a collection matching the given queries.
 * Returns an array of all documents.
 */
async function paginateAll(databases, collectionId, extraQueries = [], selectFields = null) {
  const PAGE = 100;
  const all = [];
  let cursor = undefined;

  while (true) {
    const q = [...extraQueries, sdk.Query.limit(PAGE)];
    if (selectFields) q.push(sdk.Query.select(selectFields));
    if (cursor) q.push(sdk.Query.cursorAfter(cursor));

    const res = await databases.listDocuments(DATABASE_ID, collectionId, q);
    all.push(...res.documents);

    if (res.documents.length < PAGE) break;
    cursor = res.documents[res.documents.length - 1].$id;
  }

  return all;
}

module.exports = {
  initClient, paginateAll, DATABASE_ID, sdk,
  PRO_PLAN_LIMITS, ALERT_THRESHOLD,
  checkUsageBudget, trackUsage,
};
