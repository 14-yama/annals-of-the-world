/**
 * Audit Classification Function
 *
 * Monitors entity classification integrity:
 *   1. Duplicate detection — same slug in multiple divisions
 *   2. Label/class mismatch — entity label doesn't match its Dewey class
 *   3. Division misassignment — Person entities in wrong Person sub-division
 *   4. Cross-division duplicates — same name across different divisions
 *
 * Dewey Classification Rules:
 *   0xx/1xx = Ideas/Theories (label: Idea)
 *   2xx = People (label: Person)
 *   3xx = Institutions (label: Institution)
 *   4xx = Places (label: Place)
 *   5xx = Events (label: EventWindow)
 *   6xx = Movements (label: Movement)
 *   7xx = Texts/Artifacts (label: Text, Corpus)
 *   8xx = Evidence (label: Evidence)
 *   9xx = Timeframes (label: Timeframe)
 *
 * Schedule: Daily at 06:00 UTC
 */
const sdk = require('node-appwrite');

const DATABASE_ID = process.env.APPWRITE_DATABASE_ID || 'annals_db';

/* ═══════════════════════ Classification Rules ═══════════════════════ */

const LABEL_TO_VALID_CLASSES = {
  Idea:        [0, 1],
  Person:      [2],
  Institution: [3],
  Place:       [4],
  EventWindow: [5],
  Movement:    [6],
  Text:        [7],
  Corpus:      [7],
  Evidence:    [8],
  Timeframe:   [9],
  Framework:   [1],
  Polity:      [3, 4],
};

/**
 * Person sub-division rules. The correct sub-div depends on the person's role.
 * These keywords in summary/subjects help detect misclassification.
 */
const PERSON_DIV_HINTS = {
  220: { label: 'Political Leaders', keywords: ['president', 'prime minister', 'governor', 'leader', 'politician', 'statesman', 'chancellor'] },
  221: { label: 'Monarchs & Rulers', keywords: ['king', 'queen', 'emperor', 'empress', 'monarch', 'ruler', 'sultan', 'pharaoh', 'tsar', 'shah', 'caliph'] },
  222: { label: 'Heads of State', keywords: ['head of state', 'elected', 'prime minister'] },
  240: { label: 'Scientists', keywords: ['scientist', 'inventor', 'physicist', 'chemist', 'biologist'] },
  250: { label: 'Religious Figures', keywords: ['prophet', 'saint', 'pope', 'bishop', 'religious', 'apostle', 'missionary'] },
  260: { label: 'Artists & Writers', keywords: ['artist', 'writer', 'author', 'poet', 'painter', 'sculptor', 'composer', 'musician'] },
  280: { label: 'Military Leaders', keywords: ['general', 'admiral', 'commander', 'warrior', 'conqueror', 'military'] },
  290: { label: 'Explorers', keywords: ['explorer', 'navigator', 'expedition', 'cartographer', 'voyage'] },
};

/* ═══════════════════════ Helpers ═══════════════════════ */

function normaliseName(name) {
  return (name || '').toLowerCase().replace(/[^a-z0-9\s]/g, '').replace(/\s+/g, ' ').trim();
}

function getClassFromCall(callNumber) {
  if (!callNumber) return -1;
  const divStr = callNumber.split('.')[0];
  const digits = divStr.replace(/\D/g, '');
  return digits.length > 0 ? Math.floor(parseInt(digits) / 100) : -1;
}

function getDivFromCall(callNumber) {
  if (!callNumber) return -1;
  const divStr = callNumber.split('.')[0];
  const digits = divStr.replace(/\D/g, '');
  return digits.length > 0 ? parseInt(digits) : -1;
}

/* ═══════════════════════ Main ═══════════════════════ */

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

  const startTime = Date.now();

  log('Starting classification audit...');

  const PAGE = 100;
  let cursor = undefined;
  let totalEntities = 0;

  const issues = {
    labelClassMismatch: [],     // label doesn't match Dewey class
    duplicateSlugs: [],         // same slug appears twice
    crossDivDuplicates: [],     // same normalised name in different divisions
    personDivMismatch: [],      // Person in wrong sub-division (e.g., ruler in 260-Artists)
    geoStubInWrongDiv: [],      // auto-generated geo-registry stub in wrong division
  };

  const slugSet = new Set();
  const nameIndex = {};  // normName -> [{slug,callNumber,label,div}]

  try {
    /* ─── Step 1: Load all entities ─── */
    while (true) {
      const q = [
        sdk.Query.select(['$id', 'slug', 'name', 'label', 'callNumber', 'summary', 'subjects']),
        sdk.Query.limit(PAGE),
      ];
      if (cursor) q.push(sdk.Query.cursorAfter(cursor));

      const batch = await databases.listDocuments(DATABASE_ID, 'entities', q);
      if (batch.documents.length === 0) break;

      for (const doc of batch.documents) {
        totalEntities++;
        const { slug, name, label, callNumber, summary, subjects } = doc;
        const entityClass = getClassFromCall(callNumber);
        const div = getDivFromCall(callNumber);

        /* ─── Check 1: Label/class mismatch ─── */
        const validClasses = LABEL_TO_VALID_CLASSES[label];
        if (validClasses && entityClass >= 0 && !validClasses.includes(entityClass)) {
          issues.labelClassMismatch.push({
            slug, name, label, callNumber,
            actualClass: entityClass,
            expectedClasses: validClasses,
          });
        }

        /* ─── Check 2: Duplicate slugs ─── */
        if (slug) {
          if (slugSet.has(slug)) {
            issues.duplicateSlugs.push({ slug, name, callNumber });
          } else {
            slugSet.add(slug);
          }
        }

        /* ─── Check 3: Person sub-division mismatch ─── */
        if (label === 'Person' && div >= 200 && div < 300) {
          const text = ((summary || '') + ' ' + (subjects || []).join(' ')).toLowerCase();
          const isGeoStub = (summary || '').includes('notable figure in the history of');

          if (isGeoStub && div !== 220) {
            issues.geoStubInWrongDiv.push({
              slug, name, callNumber, currentDiv: div,
              suggestedDiv: 220,
              reason: 'Geo-registry auto-stub should be in 220 (Political Leaders)',
            });
          }

          // Check if a person is in 260 (Artists) but talks like a ruler
          if (!isGeoStub) {
            for (const [divCode, { label: divLabel, keywords }] of Object.entries(PERSON_DIV_HINTS)) {
              const hintDiv = parseInt(divCode);
              if (hintDiv === div) continue; // already in this division
              const mathces = keywords.filter(kw => text.includes(kw));
              if (mathces.length >= 2) {
                // Strong signal: 2+ keyword hits for a DIFFERENT division
                issues.personDivMismatch.push({
                  slug, name, callNumber, currentDiv: div,
                  suggestedDiv: hintDiv,
                  suggestedLabel: divLabel,
                  matchedKeywords: mathces,
                });
                break; // only report one suggestion per entity
              }
            }
          }
        }

        /* ─── Index for cross-div duplicate check ─── */
        const normName = normaliseName(name);
        if (normName) {
          if (!nameIndex[normName]) nameIndex[normName] = [];
          nameIndex[normName].push({ slug, callNumber, label, div });
        }
      }

      cursor = batch.documents[batch.documents.length - 1].$id;
      if (totalEntities % 5000 === 0) log(`  Scanned ${totalEntities}...`);
    }

    /* ─── Step 2: Cross-division duplicate check ─── */
    for (const [normName, entries] of Object.entries(nameIndex)) {
      if (entries.length < 2) continue;
      const divs = new Set(entries.map(e => e.div));
      if (divs.size > 1) {
        // Same normalised name, different divisions
        issues.crossDivDuplicates.push({
          name: normName,
          count: entries.length,
          divisions: [...divs].sort((a, b) => a - b),
          entries: entries.slice(0, 10), // cap to prevent huge payloads
        });
      }
    }

    const computeTimeMs = Date.now() - startTime;

    const report = {
      timestamp: new Date().toISOString(),
      totalEntities,
      computeTimeMs,
      summary: {
        labelClassMismatch: issues.labelClassMismatch.length,
        duplicateSlugs: issues.duplicateSlugs.length,
        crossDivDuplicates: issues.crossDivDuplicates.length,
        personDivMismatch: issues.personDivMismatch.length,
        geoStubInWrongDiv: issues.geoStubInWrongDiv.length,
        totalIssues:
          issues.labelClassMismatch.length +
          issues.duplicateSlugs.length +
          issues.crossDivDuplicates.length +
          issues.personDivMismatch.length +
          issues.geoStubInWrongDiv.length,
      },
      // Return first 100 of each for the report (full data available in logs)
      issues: {
        labelClassMismatch: issues.labelClassMismatch.slice(0, 100),
        duplicateSlugs: issues.duplicateSlugs.slice(0, 100),
        crossDivDuplicates: issues.crossDivDuplicates.slice(0, 100),
        personDivMismatch: issues.personDivMismatch.slice(0, 100),
        geoStubInWrongDiv: issues.geoStubInWrongDiv.slice(0, 100),
      },
    };

    log(`Classification audit complete: ${totalEntities} entities, ${report.summary.totalIssues} issues, ${(computeTimeMs / 1000).toFixed(1)}s`);
    log(`  Label/class mismatches: ${report.summary.labelClassMismatch}`);
    log(`  Duplicate slugs: ${report.summary.duplicateSlugs}`);
    log(`  Cross-div duplicates: ${report.summary.crossDivDuplicates}`);
    log(`  Person div mismatches: ${report.summary.personDivMismatch}`);
    log(`  Geo-stubs in wrong div: ${report.summary.geoStubInWrongDiv}`);

    return res.json(report);

  } catch (err) {
    error(`Classification audit failed: ${err.message}`);
    return res.json({ error: err.message }, 500);
  }
};
