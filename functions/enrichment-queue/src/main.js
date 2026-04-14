/**
 * Enrichment Queue Scanner — Appwrite Cloud Function
 *
 * Scans all entities in the database, scores them by weakness, and stores
 * the priority queue in a `enrichment_queue` collection for the ai-enrichment
 * function to consume. Also provides live statistics.
 *
 * Schedule: Every 6 hours (0 *​/6 * * *)
 * Execute: ["any"] — can be invoked manually for on-demand stats
 *
 * Request body (optional):
 *   { "mode": "stats" }  — Return stats only, don't write queue
 *   { "limit": 500 }     — Max entities in queue (default: 500)
 */
const sdk = require('node-appwrite');

const DATABASE_ID = process.env.APPWRITE_DATABASE_ID || 'annals_world_db';
const ENTITIES_COLLECTION = 'entities';
const STATS_COLLECTION = 'stats_cache';

// Stub detection patterns
const STUB_PATTERNS = [
  'a notable figure associated with',
  'a significant event in the history of',
  'an important institution in',
  'a key development in',
  'a major movement in',
];

module.exports = async ({ req, res, log, error }) => {
  const startTime = Date.now();

  const client = new sdk.Client();
  client
    .setEndpoint(process.env.APPWRITE_ENDPOINT || 'https://fra.cloud.appwrite.io/v1')
    .setProject(process.env.APPWRITE_FUNCTION_PROJECT_ID)
    .setKey(process.env.APPWRITE_API_KEY);

  const databases = new sdk.Databases(client);

  // ── COST CAP: Full scan. Skip if over budget. ──
  const isScheduled = !req.body || req.body === '{}';
  let helpers;
  try { helpers = require('./helpers'); } catch {}
  if (isScheduled && helpers?.checkUsageBudget) {
    try {
      const budget = await helpers.checkUsageBudget(databases, log);
      if (!budget.allowed) return res.json({ skipped: true, reason: budget.reason });
    } catch (e) { log(`Usage check error: ${e.message}`); }
  }

  // Parse request
  let mode = 'full'; // 'full' = scan + queue, 'stats' = scan only
  let limit = 500;
  try {
    const body = JSON.parse(req.body || '{}');
    if (body.mode === 'stats') mode = 'stats';
    if (body.limit) limit = Math.min(parseInt(body.limit, 10), 2000);
  } catch { /* defaults */ }

  log(`Enrichment Queue Scanner: mode=${mode}, limit=${limit}`);

  // Scan entities in pages
  const PAGE = 500;
  let cursor = undefined;
  let totalScanned = 0;
  let stubs = 0;      // <200c
  let partials = 0;   // 200-600c
  let weak = 0;       // 600-800c
  let enriched = 0;   // >=800c
  const queue = [];

  const labelCounts = {};
  const eraCounts = {};

  while (true) {
    const queries = [
      sdk.Query.limit(PAGE),
      sdk.Query.select([
        '$id', 'slug', 'name', 'label', 'era', 'region', 'continent',
        'summary', 'subjects', 'frameworks', 'importanceScore',
      ]),
    ];
    if (cursor) queries.push(sdk.Query.cursorAfter(cursor));

    let batch;
    try {
      batch = await databases.listDocuments(DATABASE_ID, ENTITIES_COLLECTION, queries);
    } catch (err) {
      error(`Query error at offset ${totalScanned}: ${err.message}`);
      break;
    }

    if (!batch.documents || batch.documents.length === 0) break;

    for (const doc of batch.documents) {
      totalScanned++;
      const summary = doc.summary || '';
      const sLen = summary.length;
      const importance = doc.importanceScore || 1;
      const label = doc.label || 'Unknown';
      const era = doc.era || 'Unknown';

      // Count by category
      if (sLen < 200) stubs++;
      else if (sLen < 600) partials++;
      else if (sLen < 800) weak++;
      else enriched++;

      labelCounts[label] = (labelCounts[label] || 0) + (sLen < 800 ? 1 : 0);
      eraCounts[era] = (eraCounts[era] || 0) + (sLen < 800 ? 1 : 0);

      // Skip already enriched
      if (sLen >= 800) continue;

      // Score the entity
      const summaryScore = Math.max(0, (800 - sLen) / 800) * 50;

      // Check for stub patterns
      const lowerSummary = summary.toLowerCase();
      const isStub = STUB_PATTERNS.some(p => lowerSummary.includes(p));
      const stubBonus = isStub ? 20 : 0;

      // Missing fields penalty
      let missingFields = 0;
      if (!doc.subjects || doc.subjects.length < 3) missingFields++;
      if (!doc.frameworks || doc.frameworks.length < 2) missingFields++;

      const importanceMultiplier = importance / 5;
      const score = (summaryScore + stubBonus + missingFields * 5) * importanceMultiplier;

      if (score > 0) {
        queue.push({
          docId: doc.$id,
          slug: doc.slug,
          name: doc.name,
          label,
          era,
          summaryLength: sLen,
          importance,
          score: Math.round(score * 100) / 100,
        });
      }
    }

    cursor = batch.documents[batch.documents.length - 1].$id;
    if (batch.documents.length < PAGE) break;

    // Log progress every 10K
    if (totalScanned % 10000 < PAGE) {
      log(`  ...scanned ${totalScanned} entities`);
    }
  }

  // Sort by score descending
  queue.sort((a, b) => b.score - a.score);
  const topQueue = queue.slice(0, limit);

  const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);

  const result = {
    generated: new Date().toISOString(),
    elapsed: `${elapsed}s`,
    totalScanned,
    needsEnrichment: stubs + partials + weak,
    breakdown: {
      stubs,      // <200c
      partials,   // 200-600c
      weak,       // 600-800c
      enriched,   // >=800c
    },
    weakByLabel: labelCounts,
    weakByEra: eraCounts,
    queueSize: topQueue.length,
    top10: topQueue.slice(0, 10).map(e => `${e.slug} (${e.summaryLength}c, score=${e.score}, imp=${e.importance})`),
  };

  log(`Scan complete: ${totalScanned} total, ${stubs + partials + weak} need enrichment, queue=${topQueue.length}`);
  log(`  STUBs (<200c): ${stubs}`);
  log(`  PARTIALs (200-600c): ${partials}`);
  log(`  WEAK (600-800c): ${weak}`);
  log(`  ENRICHED (>=800c): ${enriched}`);

  // Write stats to stats_cache for frontend dashboard
  try {
    await databases.createDocument(DATABASE_ID, STATS_COLLECTION, sdk.ID.unique(), {
      type: 'enrichment_queue',
      data: JSON.stringify({
        totalScanned,
        stubs,
        partials,
        weak,
        enriched,
        queueSize: topQueue.length,
        topSlugs: topQueue.slice(0, 20).map(e => e.slug),
      }),
      updatedAt: new Date().toISOString(),
    });
  } catch {
    // stats_cache may not accept this schema — non-fatal
    log('Could not write to stats_cache (non-fatal)');
  }

  return res.json(result);
};
