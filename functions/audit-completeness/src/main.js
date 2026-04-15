/**
 * Audit Completeness + Stats Counter (dual-purpose function)
 *
 * MODE 1 — Stats Only (default, every 10 min):
 *   Fast cursor-based count of all entities by label, era, continent, class.
 *   Writes results to `stats_cache` collection for instant frontend reads.
 *   Selects only 5 lightweight fields — completes in ~15-30s for 40K entities.
 *
 * MODE 2 — Full Audit (manual or param `mode=audit`):
 *   Scans all entities and scores each on 9 quality dimensions.
 *   Also writes stats_cache as a side effect.
 *
 * Trigger: Schedule every 10 min + callable from frontend
 * Execute: ["any"] — frontend can invoke for on-demand refresh
 */
const sdk = require('node-appwrite');

const DATABASE_ID = process.env.APPWRITE_DATABASE_ID || 'annals_db';
const STATS_COLLECTION = 'stats_cache';
const STATS_DOC_ID = 'global';

module.exports = async ({ req, res, log, error }) => {
  const client = new sdk.Client();
  client
    .setEndpoint(process.env.APPWRITE_ENDPOINT || 'https://fra.cloud.appwrite.io/v1')
    .setProject(process.env.APPWRITE_FUNCTION_PROJECT_ID)
    .setKey(process.env.APPWRITE_API_KEY);

  const databases = new sdk.Databases(client);

  // ── COST CAP: Full scan costs ~392K reads. Skip if over budget. ──
  const isScheduled = !req.body || req.body === '{}';
  let helpers;
  try { helpers = require('./helpers'); } catch {}

  if (isScheduled && helpers?.checkUsageBudget) {
    try {
      const budget = await helpers.checkUsageBudget(databases, log);
      if (!budget.allowed) {
        return res.json({ skipped: true, reason: budget.reason });
      }
    } catch (e) { log(`Usage check error: ${e.message}`); }
  }

  // Determine mode from request body
  let mode = 'stats';
  try {
    const body = JSON.parse(req.body || '{}');
    if (body.mode === 'audit') mode = 'audit';
  } catch { /* default to stats */ }

  const startTime = Date.now();

  if (mode === 'stats') {
    return await runStatsOnly(databases, res, log, error, startTime);
  } else {
    return await runFullAudit(databases, res, log, error, startTime);
  }
};

/* ══════════════════════════════════════════════════════════════════
 * MODE 1: Stats Only — Lightweight counting
 * ══════════════════════════════════════════════════════════════════ */
async function runStatsOnly(databases, res, log, error, startTime) {
  log('Running stats counter (lightweight mode)...');

  try {
    await ensureStatsCollection(databases, log);

    const PAGE = 500;
    let cursor = undefined;
    let total = 0;
    const byLabel = {};
    const byEra = {};
    const byContinent = {};
    const byClass = {};

    while (true) {
      const queries = [
        sdk.Query.limit(PAGE),
        sdk.Query.select(['$id', 'label', 'era', 'continent', 'callNumber']),
      ];
      if (cursor) queries.push(sdk.Query.cursorAfter(cursor));

      const batch = await databases.listDocuments(DATABASE_ID, 'entities', queries);
      if (batch.documents.length === 0) break;

      for (const doc of batch.documents) {
        total++;
        const label = doc.label || 'Unknown';
        const era = doc.era || 'Unknown';
        const continent = doc.continent || 'Unknown';
        const cn = doc.callNumber || '';
        const classDigit = cn.charAt(0);

        byLabel[label] = (byLabel[label] || 0) + 1;
        byEra[era] = (byEra[era] || 0) + 1;
        byContinent[continent] = (byContinent[continent] || 0) + 1;
        if (classDigit >= '0' && classDigit <= '9') {
          byClass[classDigit] = (byClass[classDigit] || 0) + 1;
        }
      }

      cursor = batch.documents[batch.documents.length - 1].$id;
      if (total % 10000 < PAGE) log(`  Counted ${total}...`);
    }

    const computeTimeMs = Date.now() - startTime;
    log(`Stats complete: ${total} entities in ${(computeTimeMs / 1000).toFixed(1)}s`);

    // Write to stats_cache
    const stats = {
      total,
      byLabel: JSON.stringify(byLabel),
      byEra: JSON.stringify(byEra),
      byContinent: JSON.stringify(byContinent),
      byClass: JSON.stringify(byClass),
      updatedAt: new Date().toISOString(),
      computeTimeMs,
    };
    await upsertStats(databases, stats, log);

    // ── Track usage for cost cap ──
    try {
      const estReads = total + 30;
      if (helpers?.trackUsage) await helpers.trackUsage(databases, estReads, 1, 'audit-completeness-stats', log);
    } catch (e) { log(`trackUsage error: ${e.message}`); }

    return res.json({ total, byLabel, byEra, byContinent, byClass, updatedAt: stats.updatedAt, computeTimeMs });

  } catch (err) {
    error(`Stats counter failed: ${err.message}`);
    return res.json({ error: err.message }, 500);
  }
}

/* ══════════════════════════════════════════════════════════════════
 * MODE 2: Full Audit — Quality scoring + stats
 * ══════════════════════════════════════════════════════════════════ */
async function runFullAudit(databases, res, log, error, startTime) {
  log('Running full completeness audit...');

  try {
    await ensureStatsCollection(databases, log);

    const PAGE = 100;
    let cursor = undefined;
    let totalEntities = 0;
    const scoreDist = { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0 };
    const missingCounts = {
      relationships: 0, causes: 0, effects: 0, frameworks: 0,
      places: 0, texts: 0, image: 0, wikidata: 0, summary: 0,
    };
    const labelCounts = {};
    const eraCounts = {};
    const continentCounts = {};
    const classCounts = {};
    const lowScoreEntities = [];

    while (true) {
      const queries = [sdk.Query.limit(PAGE)];
      if (cursor) queries.push(sdk.Query.cursorAfter(cursor));

      const batch = await databases.listDocuments(DATABASE_ID, 'entities', queries);
      if (batch.documents.length === 0) break;

      for (const doc of batch.documents) {
        totalEntities++;

        const details = doc.detailsJson ? JSON.parse(doc.detailsJson) : {};
        const rels = details.relationships || [];
        const causes = details.causes || [];
        const effects = details.effects || [];
        const places = details.places || [];
        const texts = details.texts || [];
        const frameworks = doc.frameworks || [];

        let score = 0;
        if (rels.length > 0) score++; else missingCounts.relationships++;
        if (causes.length > 0) score++; else missingCounts.causes++;
        if (effects.length > 0) score++; else missingCounts.effects++;
        if (frameworks.length > 0) score++; else missingCounts.frameworks++;
        if (places.length > 0) score++; else missingCounts.places++;
        if (texts.length > 0) score++; else missingCounts.texts++;
        if (doc.imageUrl) score++; else missingCounts.image++;
        if (doc.wikidataQid) score++; else missingCounts.wikidata++;
        if ((doc.summary || '').length >= 50) score++; else missingCounts.summary++;

        scoreDist[score] = (scoreDist[score] || 0) + 1;

        // Track counts for stats_cache
        const label = doc.label || 'Unknown';
        const era = doc.era || 'Unknown';
        const continent = doc.continent || 'Unknown';
        const cn = doc.callNumber || '';
        const classDigit = cn.charAt(0);

        labelCounts[label] = (labelCounts[label] || 0) + 1;
        eraCounts[era] = (eraCounts[era] || 0) + 1;
        continentCounts[continent] = (continentCounts[continent] || 0) + 1;
        if (classDigit >= '0' && classDigit <= '9') {
          classCounts[classDigit] = (classCounts[classDigit] || 0) + 1;
        }

        if (score < 3) {
          lowScoreEntities.push({ slug: doc.slug, name: doc.name, score, label, era });
        }
      }

      cursor = batch.documents[batch.documents.length - 1].$id;
      if (totalEntities % 1000 === 0) log(`  Processed ${totalEntities}...`);
    }

    // Write stats_cache as side effect
    const computeTimeMs = Date.now() - startTime;
    const stats = {
      total: totalEntities,
      byLabel: JSON.stringify(labelCounts),
      byEra: JSON.stringify(eraCounts),
      byContinent: JSON.stringify(continentCounts),
      byClass: JSON.stringify(classCounts),
      updatedAt: new Date().toISOString(),
      computeTimeMs,
    };
    await upsertStats(databases, stats, log);

    // Calculate average score
    let totalScore = 0;
    for (const [s, count] of Object.entries(scoreDist)) {
      totalScore += Number(s) * count;
    }
    const avgScore = totalEntities > 0 ? (totalScore / totalEntities).toFixed(2) : '0';

    const report = {
      timestamp: new Date().toISOString(),
      totalEntities,
      averageScore: Number(avgScore),
      scoreDistribution: scoreDist,
      missingFieldCounts: missingCounts,
      byLabel: labelCounts,
      byEra: eraCounts,
      byContinent: continentCounts,
      byClass: classCounts,
      lowScoreCount: lowScoreEntities.length,
      sampleLowScore: lowScoreEntities.slice(0, 50),
      computeTimeMs,
    };

    log(`Audit complete: ${totalEntities} entities, avg score ${avgScore}/9, ${(computeTimeMs / 1000).toFixed(1)}s`);

    // ── Track usage for cost cap ──
    try {
      const estReads = totalEntities + 5;
      if (helpers?.trackUsage) await helpers.trackUsage(databases, estReads, 1, 'audit-completeness-audit', log);
    } catch (e) { log(`trackUsage error: ${e.message}`); }

    return res.json(report);

  } catch (err) {
    error(`Audit failed: ${err.message}`);
    return res.json({ error: err.message }, 500);
  }
}

/* ══════════════════════════════════════════════════════════════════
 * Helpers
 * ══════════════════════════════════════════════════════════════════ */

async function upsertStats(databases, stats, log) {
  try {
    await databases.updateDocument(DATABASE_ID, STATS_COLLECTION, STATS_DOC_ID, stats);
    log('Updated stats_cache document');
  } catch {
    try {
      await databases.createDocument(DATABASE_ID, STATS_COLLECTION, STATS_DOC_ID, stats);
      log('Created stats_cache document');
    } catch (e) {
      log(`Warning: could not write stats_cache: ${e.message}`);
    }
  }
}

async function ensureStatsCollection(databases, log) {
  try {
    await databases.getCollection(DATABASE_ID, STATS_COLLECTION);
    return;
  } catch {
    log('Creating stats_cache collection...');
  }

  await databases.createCollection(
    DATABASE_ID,
    STATS_COLLECTION,
    'Stats Cache',
    [sdk.Permission.read(sdk.Role.any())],
    false
  );

  await Promise.all([
    databases.createIntegerAttribute(DATABASE_ID, STATS_COLLECTION, 'total', true),
    databases.createStringAttribute(DATABASE_ID, STATS_COLLECTION, 'byLabel', 4000, true),
    databases.createStringAttribute(DATABASE_ID, STATS_COLLECTION, 'byEra', 2000, true),
    databases.createStringAttribute(DATABASE_ID, STATS_COLLECTION, 'byContinent', 2000, true),
    databases.createStringAttribute(DATABASE_ID, STATS_COLLECTION, 'byClass', 1000, true),
    databases.createStringAttribute(DATABASE_ID, STATS_COLLECTION, 'updatedAt', 64, true),
    databases.createIntegerAttribute(DATABASE_ID, STATS_COLLECTION, 'computeTimeMs', false),
  ]);

  // Wait for attributes to become available
  await new Promise(resolve => setTimeout(resolve, 3000));
  log('stats_cache collection created');
}
