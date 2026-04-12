/**
 * Stats Counter + Audit Consistency (dual-purpose function)
 *
 * MODE 1 — Stats (default, every 10 min):
 *   Accurate entity count using cursor-based pagination per label (parallel).
 *   Writes a new row to `stats_cache` collection (append, not overwrite).
 *   Frontend reads the latest row by updatedAt desc.
 *
 * MODE 2 — Consistency Audit (`{ mode: "consistency" }`):
 *   Full data integrity validation (era codes, slugs, labels, etc.)
 *   Also appends stats_cache row as a side effect.
 *
 * MODE 3 — Full Audit (`{ mode: "audit" }`):
 *   Quality scoring on 9 dimensions + stats_cache append.
 *
 * Schedule: Every 10 minutes (stats mode)
 * Execute: ["any"] — frontend can invoke for on-demand refresh
 */
const sdk = require('node-appwrite');

const DATABASE_ID = process.env.APPWRITE_DATABASE_ID || 'annals_db';
const STATS_COLLECTION = 'stats_cache';

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
 * MODE 1: Stats Only — Accurate cursor-based counting per label (parallel)
 * Each label is counted via cursor pagination in parallel.
 * Era/continent/class counts use cursor pagination within each label.
 * Writes a NEW row to stats_cache (append, not overwrite).
 * ══════════════════════════════════════════════════════════════════ */
const ALL_CONTINENTS = [
  'Africa', 'Asia', 'Europe', 'Americas', 'Oceania', 'Antarctica',
  'North America', 'South America', 'Global', 'Cross-Regional',
];

async function runStatsOnly(databases, res, log, error, startTime) {
  log('Running stats counter (hybrid: cursor for totals, quick for breakdowns)...');

  try {
    /**
     * Quick count using res.total (capped at 5000 by Appwrite).
     */
    async function quickCount(queries) {
      const r = await databases.listDocuments(DATABASE_ID, 'entities', [
        ...queries, sdk.Query.select(['$id']), sdk.Query.limit(1),
      ]);
      return r.total;
    }

    /**
     * Accurate count using cursor pagination at 5000/page.
     * Only fetches $id to minimize data. Used only for capped labels.
     */
    async function cursorCount(queries) {
      let count = 0;
      let cursor;
      while (true) {
        const q = [
          ...queries,
          sdk.Query.select(['$id']),
          sdk.Query.limit(5000),
        ];
        if (cursor) q.push(sdk.Query.cursorAfter(cursor));
        const batch = await databases.listDocuments(DATABASE_ID, 'entities', q);
        if (batch.documents.length === 0) break;
        count += batch.documents.length;
        cursor = batch.documents[batch.documents.length - 1].$id;
        if (batch.documents.length < 5000) break; // last page
      }
      return count;
    }

    // Count each label: quickCount first, cursorCount if capped
    const byLabel = {};
    let total = 0;

    for (const label of VALID_LABELS) {
      const q = [sdk.Query.equal('label', label)];
      let count = await quickCount(q);
      if (count >= 5000) {
        count = await cursorCount(q);
      }
      if (count > 0) byLabel[label] = count;
      total += count;
      log(`  ${label}: ${count}${count >= 5000 ? ' (cursor)' : ''}`);
    }

    // Breakdowns: quickCount first, cursorCount if capped (>= 5000)
    async function hybridCount(queries) {
      let c = await quickCount(queries);
      if (c >= 5000) c = await cursorCount(queries);
      return c;
    }

    const byEra = {};
    for (const era of VALID_ERAS) {
      const c = await hybridCount([sdk.Query.equal('era', era)]);
      if (c > 0) byEra[era] = c;
      log(`  era/${era}: ${c}`);
    }

    const byContinent = {};
    for (const cont of ALL_CONTINENTS) {
      const c = await hybridCount([sdk.Query.equal('continent', cont)]);
      if (c > 0) byContinent[cont] = c;
      log(`  cont/${cont}: ${c}`);
    }

    const byClass = {};
    for (let d = 0; d <= 9; d++) {
      const c = await hybridCount([sdk.Query.startsWith('callNumber', String(d))]);
      if (c > 0) byClass[String(d)] = c;
      log(`  class/${d}: ${c}`);
    }

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
    await appendStats(databases, stats, log);

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
      underscoreSlug: [], stubSummary: [],
    };
    const slugSet = new Set();
    const normalizedSlugMap = new Map(); // normalized → first doc $id (detect _/- variants)
    const duplicateSlugs = [];

    // Stub summary patterns — auto-generated or meaningless overviews
    const STUB_PATTERNS = [
      /^a notable figure associated with/i,
      /^notable .{0,20} associated with/i,
      /^leader of [A-Z]/,
      /^[A-Z][a-z]+ (?:of|in|from) [A-Z]/,  // "Battle of X" name-only
    ];
    const STUB_MAX_LENGTH = 80;

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
        // Detect underscore slugs (should be kebab-case per slug_naming_convention.md)
        if (slug && slug.includes('_')) {
          issues.underscoreSlug.push({ ...entry, slug, suggested: slug.replace(/_/g, '-') });
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
        // Stub summary detection
        const summary = doc.summary || '';
        if (summary.length > 0 && summary.length <= STUB_MAX_LENGTH) {
          issues.stubSummary.push({ ...entry, summaryLength: summary.length, preview: summary.slice(0, 60) });
        } else if (summary.length > 0 && STUB_PATTERNS.some(p => p.test(summary))) {
          issues.stubSummary.push({ ...entry, summaryLength: summary.length, preview: summary.slice(0, 60), pattern: 'auto-generated' });
        }
        if (slug) {
          if (slugSet.has(slug)) duplicateSlugs.push({ slug, $id: doc.$id });
          else slugSet.add(slug);
          // Track normalized slug variants (underscore→hyphen) to detect soft duplicates
          const normalizedSlug = slug.replace(/_/g, '-');
          if (normalizedSlugMap.has(normalizedSlug) && normalizedSlugMap.get(normalizedSlug) !== doc.$id) {
            issues.duplicateSlug.push({ slug, $id: doc.$id, variant: normalizedSlug, existingId: normalizedSlugMap.get(normalizedSlug) });
          } else {
            normalizedSlugMap.set(normalizedSlug, doc.$id);
          }
        }
      }

      cursor = batch.documents[batch.documents.length - 1].$id;
      if (totalEntities % 1000 === 0) log(`  Checked ${totalEntities}...`);
    }

    issues.duplicateSlug = duplicateSlugs;

    // Write stats_cache as side effect
    const computeTimeMs = Date.now() - startTime;
    await appendStats(databases, {
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
    await appendStats(databases, {
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

/**
 * Append a new stats row to stats_cache (never overwrite).
 * Each row gets a unique ID. Frontend reads the latest by updatedAt desc.
 * Also prune old rows to keep collection lean (keep latest 50).
 */
async function appendStats(databases, stats, log) {
  try {
    await databases.createDocument(
      DATABASE_ID, STATS_COLLECTION, sdk.ID.unique(), stats
    );
    log('Appended new stats_cache row');

    // Prune: keep only latest 50 rows
    try {
      const old = await databases.listDocuments(DATABASE_ID, STATS_COLLECTION, [
        sdk.Query.orderDesc('updatedAt'),
        sdk.Query.offset(50),
        sdk.Query.limit(100),
        sdk.Query.select(['$id']),
      ]);
      for (const doc of old.documents) {
        await databases.deleteDocument(DATABASE_ID, STATS_COLLECTION, doc.$id);
      }
      if (old.documents.length > 0) {
        log(`Pruned ${old.documents.length} old stats rows`);
      }
    } catch { /* pruning is best-effort */ }
  } catch (e) {
    log(`Warning: could not append stats_cache: ${e.message}`);
  }
}


