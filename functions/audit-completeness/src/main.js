/**
 * Audit Completeness Function
 *
 * Scans all entities and scores each on 9 quality dimensions:
 *   1. relationships  2. causes  3. effects  4. frameworks
 *   5. places  6. texts/evidence  7. image  8. wikidata  9. summary
 *
 * Produces a summary report and optionally updates importanceScore.
 *
 * Schedule: Daily at 02:00 UTC
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

  log('Starting completeness audit...');

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
  const lowScoreEntities = [];  // entities with score < 3

  try {
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

        // Track by label and era
        const label = doc.label || 'Unknown';
        const era = doc.era || 'Unknown';
        labelCounts[label] = (labelCounts[label] || 0) + 1;
        eraCounts[era] = (eraCounts[era] || 0) + 1;

        if (score < 3) {
          lowScoreEntities.push({
            slug: doc.slug,
            name: doc.name,
            score,
            label,
            era,
          });
        }
      }

      cursor = batch.documents[batch.documents.length - 1].$id;

      if (totalEntities % 1000 === 0) {
        log(`Processed ${totalEntities} entities...`);
      }
    }

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
      lowScoreCount: lowScoreEntities.length,
      sampleLowScore: lowScoreEntities.slice(0, 50),
    };

    log(`Audit complete: ${totalEntities} entities, avg score ${avgScore}/9`);
    log(`Missing: rels=${missingCounts.relationships}, causes=${missingCounts.causes}, effects=${missingCounts.effects}`);
    log(`Low score (<3): ${lowScoreEntities.length} entities`);

    return res.json(report);
  } catch (err) {
    error(`Audit failed: ${err.message}`);
    return res.json({ error: err.message }, 500);
  }
};
