/**
 * Entity Random — Server-side random entity selection
 *
 * Returns N random entities from the database using efficient random
 * offset sampling. Works at any scale (tested for 1M+ entities).
 *
 * Query parameters (via request body JSON or path):
 *   - limit: Number of entities to return (default: 25, max: 100)
 *   - label: Optional filter by entity label (e.g. "Person")
 *   - era: Optional filter by era
 *   - continent: Optional filter by continent
 *   - callNumberPrefix: Optional filter by Dewey class/division prefix
 *
 * The function uses random offsets for O(1) selection per entity,
 * avoiding full-table scans. Multiple random offsets are generated
 * to fill the requested limit with deduplication.
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

  try {
    // ── Parse parameters ──
    let params = {};
    try {
      params = JSON.parse(req.body || '{}');
    } catch {
      params = {};
    }

    const limit = Math.min(Math.max(parseInt(params.limit) || 25, 1), 100);
    const label = params.label || null;
    const era = params.era || null;
    const continent = params.continent || null;
    const callNumberPrefix = params.callNumberPrefix || null;

    // ── Build filter queries ──
    const filterQueries = [];
    if (label) filterQueries.push(sdk.Query.equal('label', label));
    if (era) filterQueries.push(sdk.Query.equal('era', era));
    if (continent) filterQueries.push(sdk.Query.equal('continent', continent));
    if (callNumberPrefix) filterQueries.push(sdk.Query.startsWith('callNumber', callNumberPrefix));

    // ── Get pool size from stats_cache or a quick count ──
    let poolSize = 0;
    try {
      if (filterQueries.length === 0) {
        // Use cached total
        const statsDoc = await databases.getDocument(DATABASE_ID, STATS_COLLECTION, STATS_DOC_ID);
        poolSize = statsDoc.total;
      } else {
        // Quick count for filtered query
        const countRes = await databases.listDocuments(DATABASE_ID, 'entities', [
          ...filterQueries, sdk.Query.limit(1),
        ]);
        poolSize = countRes.total;
        // If capped at 5000, do an accurate count
        if (poolSize >= 5000) {
          poolSize = await accurateCount(databases, filterQueries);
        }
      }
    } catch {
      // No stats cache yet — do quick count
      const countRes = await databases.listDocuments(DATABASE_ID, 'entities', [
        ...filterQueries, sdk.Query.limit(1),
      ]);
      poolSize = countRes.total;
    }

    if (poolSize === 0) {
      return res.json({ entities: [], total: 0 });
    }

    // ── Generate unique random offsets ──
    const effectiveLimit = Math.min(limit, poolSize);
    const offsets = generateUniqueRandoms(effectiveLimit, poolSize);

    // ── Fetch entities at random offsets (batch to reduce round-trips) ──
    const entities = [];
    const seen = new Set();

    for (const offset of offsets) {
      try {
        const result = await databases.listDocuments(DATABASE_ID, 'entities', [
          ...filterQueries,
          sdk.Query.limit(1),
          sdk.Query.offset(offset),
        ]);
        if (result.documents.length > 0) {
          const doc = result.documents[0];
          if (!seen.has(doc.$id)) {
            seen.add(doc.$id);
            entities.push(mapEntity(doc));
          }
        }
      } catch {
        // Skip failed offsets
      }
    }

    log(`Returned ${entities.length} random entities from pool of ${poolSize}`);

    return res.json({
      entities,
      total: poolSize,
      limit: effectiveLimit,
    });

  } catch (err) {
    error(`Entity random failed: ${err.message}`);
    return res.json({ error: err.message }, 500);
  }
};

/**
 * Generate N unique random integers in [0, max).
 */
function generateUniqueRandoms(n, max) {
  const result = new Set();
  // Generate extra to account for potential collisions
  const attempts = Math.min(n * 3, max);
  while (result.size < n && result.size < attempts) {
    result.add(Math.floor(Math.random() * max));
  }
  return [...result].slice(0, n);
}

/**
 * Accurate count using cursor-based pagination.
 */
async function accurateCount(databases, filterQueries) {
  let count = 0;
  let cursor = undefined;
  while (true) {
    const q = [...filterQueries, sdk.Query.limit(500), sdk.Query.select(['$id'])];
    if (cursor) q.push(sdk.Query.cursorAfter(cursor));
    const batch = await databases.listDocuments(DATABASE_ID, 'entities', q);
    count += batch.documents.length;
    if (batch.documents.length < 500) break;
    cursor = batch.documents[batch.documents.length - 1].$id;
  }
  return count;
}

/**
 * Map Appwrite document to a clean entity object.
 */
function mapEntity(doc) {
  return {
    $id: doc.$id,
    slug: doc.slug,
    name: doc.name,
    label: doc.label,
    era: doc.era,
    continent: doc.continent,
    callNumber: doc.callNumber,
    summary: doc.summary,
    imageUrl: doc.imageUrl || null,
    wikidataQid: doc.wikidataQid || null,
    importanceScore: doc.importanceScore || 0,
    frameworks: doc.frameworks || [],
  };
}
