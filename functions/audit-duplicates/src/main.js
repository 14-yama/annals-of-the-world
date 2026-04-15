/**
 * Audit Duplicates Function
 *
 * Detects potential duplicate entities by comparing normalised names
 * within the same label type. Uses trigram similarity for fuzzy matching.
 *
 * Schedule: Weekly on Sunday at 04:00 UTC
 */
const sdk = require('node-appwrite');

const DATABASE_ID = process.env.APPWRITE_DATABASE_ID || 'annals_db';

/**
 * Simple Levenshtein distance implementation.
 */
function levenshtein(a, b) {
  const m = a.length, n = b.length;
  if (m === 0) return n;
  if (n === 0) return m;

  const dp = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
  for (let i = 0; i <= m; i++) dp[i][0] = i;
  for (let j = 0; j <= n; j++) dp[0][j] = j;

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      dp[i][j] = a[i - 1] === b[j - 1]
        ? dp[i - 1][j - 1]
        : 1 + Math.min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]);
    }
  }
  return dp[m][n];
}

function normaliseName(name) {
  return (name || '')
    .toLowerCase()
    .replace(/[^a-z0-9\s]/g, '')
    .replace(/\s+/g, ' ')
    .trim();
}

/**
 * Normalise slug: underscore → hyphen, lowercase.
 */
function normaliseSlug(slug) {
  return (slug || '').toLowerCase().replace(/_/g, '-');
}

module.exports = async ({ req, res, log, error }) => {
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

  log('Starting duplicate detection...');

  const PAGE = 100;
  let cursor = undefined;
  const entitiesByLabel = {};  // label -> [{slug, name, normName}]

  try {
    // Step 1: Load all entities (just slug, name, label)
    while (true) {
      const q = [
        sdk.Query.select(['slug', 'name', 'label']),
        sdk.Query.limit(PAGE),
      ];
      if (cursor) q.push(sdk.Query.cursorAfter(cursor));

      const batch = await databases.listDocuments(DATABASE_ID, 'entities', q);
      if (batch.documents.length === 0) break;

      for (const doc of batch.documents) {
        const label = doc.label || 'Unknown';
        if (!entitiesByLabel[label]) entitiesByLabel[label] = [];
        entitiesByLabel[label].push({
          slug: doc.slug,
          name: doc.name,
          normName: normaliseName(doc.name),
        });
      }

      cursor = batch.documents[batch.documents.length - 1].$id;
    }

    const totalEntities = Object.values(entitiesByLabel).reduce((s, arr) => s + arr.length, 0);
    log(`Loaded ${totalEntities} entities across ${Object.keys(entitiesByLabel).length} labels`);

    // Step 1b: Detect slug variant duplicates (underscore vs hyphen)
    const slugVariantPairs = [];
    const allEntities = Object.values(entitiesByLabel).flat();
    const slugMap = new Map(); // normalised slug → first entity
    for (const entity of allEntities) {
      const norm = normaliseSlug(entity.slug);
      if (slugMap.has(norm)) {
        const existing = slugMap.get(norm);
        if (existing.slug !== entity.slug) {
          slugVariantPairs.push({
            label: 'cross-label',
            entityA: { slug: existing.slug, name: existing.name },
            entityB: { slug: entity.slug, name: entity.name },
            similarity: 1.0,
            type: 'slug-variant',
          });
        }
      } else {
        slugMap.set(norm, entity);
      }
    }
    log(`Found ${slugVariantPairs.length} slug variant pairs (underscore/hyphen)`);

    // Step 2: Compare names within each label group
    const duplicatePairs = [];
    const THRESHOLD = 0.85;  // 85% similarity

    for (const [label, entities] of Object.entries(entitiesByLabel)) {
      // Skip very large groups (>5000) to avoid O(n²) explosion
      if (entities.length > 5000) {
        log(`Skipping ${label} (${entities.length} entities — too large for pairwise comparison)`);
        continue;
      }

      for (let i = 0; i < entities.length; i++) {
        for (let j = i + 1; j < entities.length; j++) {
          const a = entities[i].normName;
          const b = entities[j].normName;

          if (!a || !b) continue;
          if (a === b) {
            // Exact duplicate
            duplicatePairs.push({
              label,
              entityA: { slug: entities[i].slug, name: entities[i].name },
              entityB: { slug: entities[j].slug, name: entities[j].name },
              similarity: 1.0,
              type: 'exact',
            });
            continue;
          }

          // Only compare names of similar length (optimisation)
          const maxLen = Math.max(a.length, b.length);
          if (Math.abs(a.length - b.length) > maxLen * 0.3) continue;

          const dist = levenshtein(a, b);
          const similarity = 1 - dist / maxLen;

          if (similarity >= THRESHOLD) {
            duplicatePairs.push({
              label,
              entityA: { slug: entities[i].slug, name: entities[i].name },
              entityB: { slug: entities[j].slug, name: entities[j].name },
              similarity: Number(similarity.toFixed(3)),
              type: 'fuzzy',
            });
          }
        }

        // Progress reporting for large groups
        if (i > 0 && i % 500 === 0) {
          log(`${label}: compared ${i}/${entities.length} entities, found ${duplicatePairs.length} pairs`);
        }
      }
    }

    // Sort by similarity descending
    duplicatePairs.sort((a, b) => b.similarity - a.similarity);

    // Merge slug variant pairs into the results
    const allPairs = [...slugVariantPairs, ...duplicatePairs];
    allPairs.sort((a, b) => b.similarity - a.similarity);

    const report = {
      timestamp: new Date().toISOString(),
      totalEntities,
      totalDuplicatePairs: allPairs.length,
      exactDuplicates: allPairs.filter(p => p.type === 'exact').length,
      fuzzyDuplicates: allPairs.filter(p => p.type === 'fuzzy').length,
      slugVariants: slugVariantPairs.length,
      topPairs: allPairs.slice(0, 200),
    };

    log(`Duplicate scan complete: ${allPairs.length} potential pairs found`);
    log(`Exact: ${report.exactDuplicates}, Fuzzy: ${report.fuzzyDuplicates}, Slug variants: ${report.slugVariants}`);

    // ── Track usage for cost cap ──
    try {
      const estReads = totalEntities + 5;
      if (helpers?.trackUsage) await helpers.trackUsage(databases, estReads, 0, 'audit-duplicates', log);
    } catch (e) { log(`trackUsage error: ${e.message}`); }

    return res.json(report);
  } catch (err) {
    error(`Duplicate scan failed: ${err.message}`);
    return res.json({ error: err.message }, 500);
  }
};
