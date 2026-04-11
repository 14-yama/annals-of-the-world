/**
 * Entity Random — Server-side random entity selection
 *
 * Returns N random entities from the database using cursor-based
 * random sampling. Works at any scale (392k+ entities).
 *
 * Query parameters (via request body JSON):
 *   - limit: Number of entities to return (default: 25, max: 100)
 *   - label: Optional filter by entity label (e.g. "Person")
 *   - era: Optional filter by era
 *   - continent: Optional filter by continent
 *   - callNumberPrefix: Optional filter by Dewey class/division prefix
 */
const sdk = require('node-appwrite');

const DATABASE_ID = process.env.APPWRITE_DATABASE_ID || 'annals_db';
const STATS_COLLECTION = 'stats_cache';

module.exports = async ({ req, res, log, error }) => {
  const client = new sdk.Client();
  client
    .setEndpoint(process.env.APPWRITE_ENDPOINT || 'https://fra.cloud.appwrite.io/v1')
    .setProject(process.env.APPWRITE_FUNCTION_PROJECT_ID)
    .setKey(process.env.APPWRITE_API_KEY);

  const databases = new sdk.Databases(client);

  try {
    // Parse parameters
    var params = {};
    try { params = JSON.parse(req.body || '{}'); } catch (_) { params = {}; }

    var limit = Math.min(Math.max(parseInt(params.limit) || 25, 1), 100);
    var labelFilter = params.label || null;
    var eraFilter = params.era || null;
    var continentFilter = params.continent || null;
    var callNumberPrefix = params.callNumberPrefix || null;

    // Build filter queries
    var filterQueries = [];
    if (labelFilter) filterQueries.push(sdk.Query.equal('label', labelFilter));
    if (eraFilter) filterQueries.push(sdk.Query.equal('era', eraFilter));
    if (continentFilter) filterQueries.push(sdk.Query.equal('continent', continentFilter));
    if (callNumberPrefix) filterQueries.push(sdk.Query.startsWith('callNumber', callNumberPrefix));

    // Get pool size from latest stats_cache row (or quick count)
    var poolSize = 0;
    try {
      if (filterQueries.length === 0) {
        var statsRows = await databases.listDocuments(DATABASE_ID, STATS_COLLECTION, [
          sdk.Query.orderDesc('updatedAt'),
          sdk.Query.limit(1),
        ]);
        if (statsRows.documents.length > 0) {
          poolSize = statsRows.documents[0].total;
        }
      }
    } catch (_) { /* no stats cache */ }

    if (poolSize === 0) {
      var countRes = await databases.listDocuments(DATABASE_ID, 'entities', [
        ...filterQueries, sdk.Query.limit(1),
      ]);
      poolSize = countRes.total; // may cap at 5000, acceptable for random
    }

    if (poolSize === 0) {
      return res.json({ entities: [], total: 0 });
    }

    // Generate random entities using cursor-based sampling
    // Strategy: pick random 2-digit callNumber prefixes then offset within
    var entities = [];
    var seen = new Set();
    var effectiveLimit = Math.min(limit, poolSize);
    var maxAttempts = effectiveLimit * 4;
    var attempts = 0;

    while (entities.length < effectiveLimit && attempts < maxAttempts) {
      attempts++;
      try {
        // Random 2-digit callNumber prefix (00-99)
        var prefix = String(Math.floor(Math.random() * 100)).padStart(2, '0');
        var q = [...filterQueries, sdk.Query.startsWith('callNumber', prefix)];

        // Get count for this prefix (capped at 5000 but fine for offset)
        var prefixRes = await databases.listDocuments(DATABASE_ID, 'entities', [
          ...q, sdk.Query.limit(1),
        ]);
        if (prefixRes.total === 0) continue;

        var maxOffset = Math.min(prefixRes.total - 1, 4999);
        var offset = Math.floor(Math.random() * (maxOffset + 1));

        var result = await databases.listDocuments(DATABASE_ID, 'entities', [
          ...q, sdk.Query.limit(1), sdk.Query.offset(offset),
        ]);

        if (result.documents.length > 0) {
          var doc = result.documents[0];
          if (!seen.has(doc.$id)) {
            seen.add(doc.$id);
            entities.push(mapEntity(doc));
          }
        }
      } catch (_) {
        // skip failed attempt
      }
    }

    log('Returned ' + entities.length + ' random entities from pool of ' + poolSize);

    return res.json({
      entities: entities,
      total: poolSize,
      limit: effectiveLimit,
    });

  } catch (err) {
    error('Entity random failed: ' + err.message);
    return res.json({ error: err.message }, 500);
  }
};

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
