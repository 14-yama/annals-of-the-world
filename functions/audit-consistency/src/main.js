/**
 * Stats Counter + Audit Consistency (dual-purpose function)
 *
 * MODE 1 — Stats (default, every 10 min):
 *   Fast entity count by label, era, continent, and Dewey class.
 *   Writes to `stats_cache` collection for instant frontend reads.
 *   Selects only 5 lightweight fields — ~15-30s for 40K entities.
 *
 * MODE 2 — Consistency Audit (`{ mode: "consistency" }`):
 *   Full data integrity validation (era codes, slugs, labels, etc.)
 *   Also writes stats_cache as a side effect.
 *
 * MODE 3 — Full Audit (`{ mode: "audit" }`):
 *   Quality scoring on 9 dimensions + stats_cache update.
 *
 * Schedule: Every 10 minutes (stats mode)
 * Execute: ["any"] — frontend can invoke for on-demand refresh
 */
const sdk = require('node-appwrite');

const DATABASE_ID = process.env.APPWRITE_DATABASE_ID || 'annals_db';
const STATS_COLLECTION = 'stats_cache';
const STATS_DOC_ID = 'global';

const VALID_ERAS = ['Prehistoric', 'Classical', 'Medieval', 'Early Modern', 'Modern', 'Contemporary'];
const VALID_LABELS = ['Person', 'Idea', 'Institution', 'Place', 'EventWindow', 'Movement', 'Text', 'Evidence', 'Timeframe', 'Corpus'];

const ERA_DIVISION_MAP = {
  'Prehistoric': ['910', '911', '912'],
  'Classical': ['920', '921', '922', '923'],
  'Medieval': ['930', '931', '932', '933'],
  'Early Modern': ['940', '941', '942', '943'],
  'Modern': ['950', '951', '952', '953'],
  'Contemporary': ['960', '961', '962', '963'],
};

module.exports = async ({ req, res, log, error }) => {
  const client = new sdk.Client();
  client
    .setEndpoint(process.env.APPWRITE_ENDPOINT || 'https://fra.cloud.appwrite.io/v1')
    .setProject(process.env.APPWRITE_FUNCTION_PROJECT_ID)
    .setKey(process.env.APPWRITE_API_KEY);

  const databases = new sdk.Databases(client);

  // Determine mode from request body
  let mode = 'stats';
  try {
    const body = JSON.parse(req.body || '{}');
    if (body.mode === 'consistency') mode = 'consistency';
    else if (body.mode === 'audit') mode = 'audit';
  } catch { /* default to stats */ }

  const startTime = Date.now();

  if (mode === 'stats') {
    return await runStatsOnly(databases, res, log, error, startTime);
  } else if (mode === 'audit') {
    return await runFullAudit(databases, res, log, error, startTime);
  } else {
    return await runConsistencyAudit(databases, res, log, error, startTime);
  }
};

/* ══════════════════════════════════════════════════════════════════
 * MODE 1: Stats Only — Parallel filtered counts (default, every 10 min)
 * Uses parallel queries. For groups where all values are known enum values,
 * at most one value needs cursor counting (computed as total - sum_of_rest).
 * Completes in ~5-15s for 40K+ entities.
 * ══════════════════════════════════════════════════════════════════ */
async function runStatsOnly(databases, res, log, error, startTime) {
  log('Running stats counter (parallel mode)...');

  try {
    // Fast count helper using res.total (capped at 5000)
    const fastCount = async (filters) => {
      const r = await databases.listDocuments(DATABASE_ID, 'entities', [...filters, sdk.Query.limit(1)]);
      return r.total;
    };

    // Count by label — parallel (every entity has a label)
    const labelPromises = VALID_LABELS.map(async (label) => {
      const count = await fastCount([sdk.Query.equal('label', label)]);
      return [label, count];
    });

    // Count by era — parallel
    const eraPromises = VALID_ERAS.map(async (era) => {
      const count = await fastCount([sdk.Query.equal('era', era)]);
      return [era, count];
    });

    // Count by continent — parallel
    const CONTINENTS = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania', 'Antarctica'];
    const continentPromises = CONTINENTS.map(async (c) => {
      const count = await fastCount([sdk.Query.equal('continent', c)]);
      return [c, count];
    });

    // Count by Dewey class (0-9) — parallel
    const classPromises = Array.from({ length: 10 }, (_, i) => String(i)).map(async (digit) => {
      const count = await fastCount([sdk.Query.startsWith('callNumber', `${digit}`)]);
      return [digit, count];
    });

    // Execute all in parallel
    const [labelResults, eraResults, continentResults, classResults] = await Promise.all([
      Promise.all(labelPromises),
      Promise.all(eraPromises),
      Promise.all(continentPromises),
      Promise.all(classPromises),
    ]);

    // Compute accurate total as sum of all label counts
    // (every entity has exactly one label, so sum(labels) = total)
    const total = labelResults.reduce((s, [, n]) => s + n, 0);
    log(`Total entities: ${total} (sum of label counts)`);

    // For each group, fix capped values using known total
    const fixCapped = (results, groupTotal) => {
      const capped = results.filter(([, n]) => n >= 5000);
      const uncapped = results.filter(([, n]) => n < 5000);
      const uncappedSum = uncapped.reduce((s, [, n]) => s + n, 0);
      if (capped.length === 1 && groupTotal > 0) {
        capped[0][1] = groupTotal - uncappedSum;
      }
      return Object.fromEntries(results.filter(([, n]) => n > 0));
    };

    const byLabel = Object.fromEntries(labelResults.filter(([, n]) => n > 0));
    const byEra = fixCapped(eraResults, total);
    const byContinent = fixCapped(continentResults, total);
    const byClass = fixCapped(classResults, total);

    const computeTimeMs = Date.now() - startTime;
    log(`Stats complete: ${total} entities in ${(computeTimeMs / 1000).toFixed(1)}s`);

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

    return res.json({ total, byLabel, byEra, byContinent, byClass, updatedAt: stats.updatedAt, computeTimeMs });

  } catch (err) {
    error(`Stats counter failed: ${err.message}`);
    return res.json({ error: err.message }, 500);
  }
}

/* ══════════════════════════════════════════════════════════════════
 * MODE 2: Consistency Audit (on demand)
 * ══════════════════════════════════════════════════════════════════ */
async function runConsistencyAudit(databases, res, log, error, startTime) {
  log('Running consistency audit...');

  try {

    const PAGE = 100;
    let cursor = undefined;
    let totalEntities = 0;
    // Stats counters
    const byLabel = {};
    const byEra = {};
    const byContinent = {};
    const byClass = {};

    const issues = {
      missingSlug: [], missingName: [], missingLabel: [], missingCallNumber: [],
      invalidSlugFormat: [], invalidCallNumberFormat: [],
      invalidEra: [], invalidLabel: [], eraDivisionMismatch: [],
      missingEra: [], duplicateSlug: [],
    };
    const slugSet = new Set();
    const duplicateSlugs = [];

    while (true) {
      const q = [sdk.Query.limit(PAGE)];
      if (cursor) q.push(sdk.Query.cursorAfter(cursor));

      const batch = await databases.listDocuments(DATABASE_ID, 'entities', q);
      if (batch.documents.length === 0) break;

      for (const doc of batch.documents) {
        totalEntities++;
        const slug = doc.slug || '';
        const name = doc.name || '';
        const label = doc.label || '';
        const callNumber = doc.callNumber || '';
        const era = doc.era || '';
        const continent = doc.continent || 'Unknown';
        const eraDivisionCode = doc.eraDivisionCode || '';
        const classDigit = callNumber.charAt(0);

        // Stats tracking
        byLabel[label || 'Unknown'] = (byLabel[label || 'Unknown'] || 0) + 1;
        byEra[era || 'Unknown'] = (byEra[era || 'Unknown'] || 0) + 1;
        byContinent[continent] = (byContinent[continent] || 0) + 1;
        if (classDigit >= '0' && classDigit <= '9') {
          byClass[classDigit] = (byClass[classDigit] || 0) + 1;
        }

        const entry = { slug, name: name.slice(0, 60), $id: doc.$id };

        if (!slug) issues.missingSlug.push(entry);
        if (!name) issues.missingName.push(entry);
        if (!label) issues.missingLabel.push(entry);
        if (!callNumber) issues.missingCallNumber.push(entry);

        if (slug && !/^[a-z0-9][a-z0-9-]*[a-z0-9]$/.test(slug) && slug.length > 1) {
          issues.invalidSlugFormat.push({ ...entry, slug });
        }
        if (callNumber && !/^\d{1,3}\.\d{2,3}\./.test(callNumber)) {
          issues.invalidCallNumberFormat.push({ ...entry, callNumber });
        }
        if (!era) {
          issues.missingEra.push(entry);
        } else if (!VALID_ERAS.includes(era)) {
          issues.invalidEra.push({ ...entry, era });
        }
        if (label && !VALID_LABELS.includes(label)) {
          issues.invalidLabel.push({ ...entry, label });
        }
        if (era && eraDivisionCode) {
          const validDivisions = ERA_DIVISION_MAP[era];
          if (validDivisions && !validDivisions.includes(eraDivisionCode)) {
            issues.eraDivisionMismatch.push({ ...entry, era, eraDivisionCode, expected: validDivisions.join(', ') });
          }
        }
        if (slug) {
          if (slugSet.has(slug)) duplicateSlugs.push({ slug, $id: doc.$id });
          else slugSet.add(slug);
        }
      }

      cursor = batch.documents[batch.documents.length - 1].$id;
      if (totalEntities % 1000 === 0) log(`  Checked ${totalEntities}...`);
    }

    issues.duplicateSlug = duplicateSlugs;

    // Write stats_cache as side effect
    const computeTimeMs = Date.now() - startTime;
    await upsertStats(databases, {
      total: totalEntities,
      byLabel: JSON.stringify(byLabel),
      byEra: JSON.stringify(byEra),
      byContinent: JSON.stringify(byContinent),
      byClass: JSON.stringify(byClass),
      updatedAt: new Date().toISOString(),
      computeTimeMs,
    }, log);

    const totalIssues = Object.values(issues).reduce((sum, arr) => sum + arr.length, 0);

    const report = {
      timestamp: new Date().toISOString(),
      totalEntities,
      totalIssues,
      issueCounts: Object.fromEntries(Object.entries(issues).map(([k, a]) => [k, a.length])),
      issues: Object.fromEntries(Object.entries(issues).map(([k, a]) => [k, a.slice(0, 50)])),
      computeTimeMs,
    };

    log(`Consistency audit complete: ${totalEntities} entities, ${totalIssues} issues, ${(computeTimeMs / 1000).toFixed(1)}s`);
    return res.json(report);

  } catch (err) {
    error(`Consistency audit failed: ${err.message}`);
    return res.json({ error: err.message }, 500);
  }
}

/* ══════════════════════════════════════════════════════════════════
 * MODE 3: Full Quality Audit (on demand)
 * ══════════════════════════════════════════════════════════════════ */
async function runFullAudit(databases, res, log, error, startTime) {
  log('Running full completeness audit...');

  try {

    const PAGE = 100;
    let cursor = undefined;
    let totalEntities = 0;
    const scoreDist = { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0 };
    const missingCounts = {
      relationships: 0, causes: 0, effects: 0, frameworks: 0,
      places: 0, texts: 0, image: 0, wikidata: 0, summary: 0,
    };
    const byLabel = {};
    const byEra = {};
    const byContinent = {};
    const byClass = {};
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

        if (score < 3) lowScoreEntities.push({ slug: doc.slug, name: doc.name, score, label, era });
      }

      cursor = batch.documents[batch.documents.length - 1].$id;
      if (totalEntities % 1000 === 0) log(`  Processed ${totalEntities}...`);
    }

    const computeTimeMs = Date.now() - startTime;
    await upsertStats(databases, {
      total: totalEntities,
      byLabel: JSON.stringify(byLabel),
      byEra: JSON.stringify(byEra),
      byContinent: JSON.stringify(byContinent),
      byClass: JSON.stringify(byClass),
      updatedAt: new Date().toISOString(),
      computeTimeMs,
    }, log);

    let totalScore = 0;
    for (const [s, count] of Object.entries(scoreDist)) totalScore += Number(s) * count;
    const avgScore = totalEntities > 0 ? (totalScore / totalEntities).toFixed(2) : '0';

    log(`Audit complete: ${totalEntities} entities, avg score ${avgScore}/9, ${(computeTimeMs / 1000).toFixed(1)}s`);

    return res.json({
      timestamp: new Date().toISOString(),
      totalEntities, averageScore: Number(avgScore), scoreDistribution: scoreDist,
      missingFieldCounts: missingCounts, byLabel, byEra, byContinent, byClass,
      lowScoreCount: lowScoreEntities.length, sampleLowScore: lowScoreEntities.slice(0, 50), computeTimeMs,
    });

  } catch (err) {
    error(`Full audit failed: ${err.message}`);
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


