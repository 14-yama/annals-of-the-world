/**
 * Audit Orphans Function
 *
 * Finds entities with zero relationships (neither source nor target in
 * the relationships collection, AND no relationships in detailsJson).
 *
 * Schedule: Daily at 03:00 UTC
 */
const sdk = require('node-appwrite');

const DATABASE_ID = process.env.APPWRITE_DATABASE_ID || 'annals_db';

module.exports = async ({ req, res, log, error }) => {
  const client = new sdk.Client();
  client
    .setEndpoint(process.env.APPWRITE_ENDPOINT || 'https://fra.cloud.appwrite.io/v1')
    .setProject(process.env.APPWRITE_FUNCTION_PROJECT_ID)
    .setKey(process.env.APPWRITE_API_KEY);

  const databases = new sdk.Databases(client);

  log('Starting orphan detection...');

  // Step 1: Collect all slugs that appear in the relationships collection
  const connectedSlugs = new Set();
  let cursor = undefined;
  const PAGE = 100;

  try {
    while (true) {
      const q = [
        sdk.Query.select(['sourceSlug', 'targetSlug']),
        sdk.Query.limit(PAGE),
      ];
      if (cursor) q.push(sdk.Query.cursorAfter(cursor));

      const batch = await databases.listDocuments(DATABASE_ID, 'relationships', q);
      if (batch.documents.length === 0) break;

      for (const doc of batch.documents) {
        if (doc.sourceSlug) connectedSlugs.add(doc.sourceSlug);
        if (doc.targetSlug) connectedSlugs.add(doc.targetSlug);
      }

      cursor = batch.documents[batch.documents.length - 1].$id;
    }

    log(`Found ${connectedSlugs.size} connected slugs in relationships collection`);

    // Step 2: Scan all entities and check for orphans
    cursor = undefined;
    let totalEntities = 0;
    const orphans = [];

    while (true) {
      const q = [sdk.Query.limit(PAGE)];
      if (cursor) q.push(sdk.Query.cursorAfter(cursor));

      const batch = await databases.listDocuments(DATABASE_ID, 'entities', q);
      if (batch.documents.length === 0) break;

      for (const doc of batch.documents) {
        totalEntities++;
        const slug = doc.slug;

        // Check relationships collection
        const inRelCollection = connectedSlugs.has(slug);

        // Check detailsJson relationships
        const details = doc.detailsJson ? JSON.parse(doc.detailsJson) : {};
        const embeddedRels = (details.relationships || []).length;

        if (!inRelCollection && embeddedRels === 0) {
          orphans.push({
            slug,
            name: doc.name,
            label: doc.label,
            era: doc.era,
            callNumber: doc.callNumber,
            importanceScore: doc.importanceScore || 0,
          });
        }
      }

      cursor = batch.documents[batch.documents.length - 1].$id;

      if (totalEntities % 1000 === 0) {
        log(`Scanned ${totalEntities} entities, found ${orphans.length} orphans so far...`);
      }
    }

    // Group orphans by label
    const byLabel = {};
    for (const o of orphans) {
      const label = o.label || 'Unknown';
      if (!byLabel[label]) byLabel[label] = [];
      byLabel[label].push(o);
    }

    const report = {
      timestamp: new Date().toISOString(),
      totalEntities,
      totalOrphans: orphans.length,
      orphanRate: totalEntities > 0 ? ((orphans.length / totalEntities) * 100).toFixed(2) + '%' : '0%',
      byLabel: Object.fromEntries(
        Object.entries(byLabel).map(([label, items]) => [label, items.length]),
      ),
      topOrphans: orphans
        .sort((a, b) => b.importanceScore - a.importanceScore)
        .slice(0, 100),
    };

    log(`Orphan scan complete: ${orphans.length}/${totalEntities} entities are orphans (${report.orphanRate})`);

    return res.json(report);
  } catch (err) {
    error(`Orphan scan failed: ${err.message}`);
    return res.json({ error: err.message }, 500);
  }
};
