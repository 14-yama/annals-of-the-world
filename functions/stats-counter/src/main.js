/**
 * Stats Counter — Pre-computed entity statistics
 *
 * Counts every entity by label, era, continent, and Dewey class using
 * efficient server-side cursor pagination. Stores results in the
 * `stats_cache` collection so the frontend can read a single document
 * instead of doing hundreds of paginated API calls.
 *
 * Trigger: Schedule every 10 minutes + manual execution from frontend
 * Execution mode: Can be invoked synchronously — returns stats as JSON
 *
 * The function also supports GET requests: the frontend calls
 *   functions.createExecution('stats-counter')
 * and gets the full stats object in the response body.
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

  // ── COST CAP: Full pagination at 392K entities costs ~392K reads per run.
  // At every-10-min schedule = ~56M reads/month = $32 overage.
  // Gate: skip if over 70% of Pro plan read limit.
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

  log('Starting stats counter...');
  const startTime = Date.now();

  try {
    // ── Ensure stats_cache collection exists ──
    await ensureCollection(databases, log);

    // ── Count all entities via cursor pagination (select only needed fields) ──
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

        // By label
        const label = doc.label || 'Unknown';
        byLabel[label] = (byLabel[label] || 0) + 1;

        // By era
        const era = doc.era || 'Unknown';
        byEra[era] = (byEra[era] || 0) + 1;

        // By continent
        const continent = doc.continent || 'Unknown';
        byContinent[continent] = (byContinent[continent] || 0) + 1;

        // By Dewey class (first digit of callNumber)
        const cn = doc.callNumber || '';
        const classDigit = cn.charAt(0);
        if (classDigit >= '0' && classDigit <= '9') {
          byClass[classDigit] = (byClass[classDigit] || 0) + 1;
        }
      }

      cursor = batch.documents[batch.documents.length - 1].$id;

      // Log progress every 10K entities
      if (total % 10000 < PAGE) {
        log(`  Counted ${total} entities so far...`);
      }
    }

    const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
    log(`Counted ${total} entities in ${elapsed}s`);

    // ── Build stats payload ──
    const stats = {
      total,
      byLabel: JSON.stringify(byLabel),
      byEra: JSON.stringify(byEra),
      byContinent: JSON.stringify(byContinent),
      byClass: JSON.stringify(byClass),
      updatedAt: new Date().toISOString(),
      computeTimeMs: Date.now() - startTime,
    };

    // ── Upsert to stats_cache collection ──
    try {
      await databases.updateDocument(DATABASE_ID, STATS_COLLECTION, STATS_DOC_ID, stats);
      log('Updated stats_cache document');
    } catch {
      // Document doesn't exist yet — create it
      await databases.createDocument(DATABASE_ID, STATS_COLLECTION, STATS_DOC_ID, stats);
      log('Created stats_cache document');
    }

    // ── Return stats as response (for synchronous execution from frontend) ──
    const responseBody = {
      total,
      byLabel,
      byEra,
      byContinent,
      byClass,
      updatedAt: stats.updatedAt,
      computeTimeMs: stats.computeTimeMs,
    };

    log(`Stats counter complete: ${total} entities, ${Object.keys(byLabel).length} labels, ${Object.keys(byEra).length} eras`);

    return res.json(responseBody);

  } catch (err) {
    error(`Stats counter failed: ${err.message}`);
    return res.json({ error: err.message }, 500);
  }
};

/**
 * Ensure the stats_cache collection exists with the right attributes.
 * Self-bootstrapping: the function creates the collection on first run.
 */
async function ensureCollection(databases, log) {
  try {
    await databases.getCollection(DATABASE_ID, STATS_COLLECTION);
    return; // Already exists
  } catch {
    log('Creating stats_cache collection...');
  }

  // Create collection with "any" read access so frontend can read it
  await databases.createCollection(
    DATABASE_ID,
    STATS_COLLECTION,
    'Stats Cache',
    [sdk.Permission.read(sdk.Role.any())],
    false // not document-level permissions
  );

  // Create attributes
  const attrs = [
    databases.createIntegerAttribute(DATABASE_ID, STATS_COLLECTION, 'total', true),
    databases.createStringAttribute(DATABASE_ID, STATS_COLLECTION, 'byLabel', 4000, true),
    databases.createStringAttribute(DATABASE_ID, STATS_COLLECTION, 'byEra', 2000, true),
    databases.createStringAttribute(DATABASE_ID, STATS_COLLECTION, 'byContinent', 2000, true),
    databases.createStringAttribute(DATABASE_ID, STATS_COLLECTION, 'byClass', 1000, true),
    databases.createStringAttribute(DATABASE_ID, STATS_COLLECTION, 'updatedAt', 64, true),
    databases.createIntegerAttribute(DATABASE_ID, STATS_COLLECTION, 'computeTimeMs', false),
  ];

  await Promise.all(attrs);

  // Wait for attributes to be ready
  log('Waiting for attributes to be available...');
  await new Promise(resolve => setTimeout(resolve, 3000));

  log('stats_cache collection created');
}
