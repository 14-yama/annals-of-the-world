/**
 * Shared helpers for Appwrite Functions.
 * Each function copies this file into its own src/ at deploy time,
 * or you can symlink it.
 */
const sdk = require('node-appwrite');

const DATABASE_ID = process.env.APPWRITE_DATABASE_ID || 'annals_db';

// ═══════════════════════════════════════════════════════════
// Appwrite Pro Plan Usage Caps
// ═══════════════════════════════════════════════════════════
// Set USAGE_CAP_ENABLED=false in function env vars to bypass.
// These thresholds are % of the Pro plan monthly allowance.
// When any threshold is exceeded, scheduled functions abort early
// and log a CURATOR ALERT. Manual invocations still run.

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
    const tracker = await databases.getDocument(DATABASE_ID, 'stats_cache', 'usage_tracker');
    const readsUsed   = tracker.readsUsed   || 0;
    const writesUsed  = tracker.writesUsed  || 0;

    const readPct  = readsUsed  / PRO_PLAN_LIMITS.DATABASE_READS;
    const writePct = writesUsed / PRO_PLAN_LIMITS.DATABASE_WRITES;

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
        cycleStart: new Date().toISOString(),
        lastFunction: '',
        lastRunAt: '',
      };
    }

    const newReads  = (tracker.readsUsed  || 0) + reads;
    const newWrites = (tracker.writesUsed || 0) + writes;

    const payload = {
      readsUsed:   newReads,
      writesUsed:  newWrites,
      lastFunction: functionName,
      lastRunAt:   new Date().toISOString(),
    };

    try {
      await databases.updateDocument(DATABASE_ID, 'stats_cache', 'usage_tracker', payload);
    } catch {
      await databases.createDocument(DATABASE_ID, 'stats_cache', 'usage_tracker', {
        ...payload,
        cycleStart: new Date().toISOString(),
      });
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
