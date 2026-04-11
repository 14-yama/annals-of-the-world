/**
 * Audit Consistency Function
 *
 * Validates data integrity rules across all entities:
 *   1. Era ↔ eraDivisionCode consistency
 *   2. callNumber format (Class.Division.Slug)
 *   3. Required fields presence (slug, name, label, callNumber)
 *   4. Slug format conventions (lowercase, hyphenated)
 *   5. Era values are canonical
 *   6. Label values are canonical
 *
 * Schedule: Daily at 05:00 UTC
 */
const sdk = require('node-appwrite');

const DATABASE_ID = process.env.APPWRITE_DATABASE_ID || 'annals_db';

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

  log('Starting consistency audit...');

  const PAGE = 100;
  let cursor = undefined;
  let totalEntities = 0;

  const issues = {
    missingSlug: [],
    missingName: [],
    missingLabel: [],
    missingCallNumber: [],
    invalidSlugFormat: [],
    invalidCallNumberFormat: [],
    invalidEra: [],
    invalidLabel: [],
    eraDivisionMismatch: [],
    missingEra: [],
    duplicateSlug: [],
  };

  const slugSet = new Set();
  const duplicateSlugs = [];

  try {
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
        const eraDivisionCode = doc.eraDivisionCode || '';

        const entry = { slug, name: name.slice(0, 60), $id: doc.$id };

        // 1. Required fields
        if (!slug) issues.missingSlug.push(entry);
        if (!name) issues.missingName.push(entry);
        if (!label) issues.missingLabel.push(entry);
        if (!callNumber) issues.missingCallNumber.push(entry);

        // 2. Slug format: lowercase, hyphenated, no spaces
        if (slug && !/^[a-z0-9][a-z0-9-]*[a-z0-9]$/.test(slug) && slug.length > 1) {
          issues.invalidSlugFormat.push({ ...entry, slug });
        }

        // 3. CallNumber format: digit(s).digit(s).slug
        if (callNumber && !/^\d{1,3}\.\d{2,3}\./.test(callNumber)) {
          issues.invalidCallNumberFormat.push({ ...entry, callNumber });
        }

        // 4. Era validation
        if (!era) {
          issues.missingEra.push(entry);
        } else if (!VALID_ERAS.includes(era)) {
          issues.invalidEra.push({ ...entry, era });
        }

        // 5. Label validation
        if (label && !VALID_LABELS.includes(label)) {
          issues.invalidLabel.push({ ...entry, label });
        }

        // 6. Era ↔ eraDivisionCode consistency
        if (era && eraDivisionCode) {
          const validDivisions = ERA_DIVISION_MAP[era];
          if (validDivisions && !validDivisions.includes(eraDivisionCode)) {
            issues.eraDivisionMismatch.push({
              ...entry,
              era,
              eraDivisionCode,
              expected: validDivisions.join(', '),
            });
          }
        }

        // 7. Duplicate slug detection
        if (slug) {
          if (slugSet.has(slug)) {
            duplicateSlugs.push({ slug, $id: doc.$id });
          } else {
            slugSet.add(slug);
          }
        }
      }

      cursor = batch.documents[batch.documents.length - 1].$id;

      if (totalEntities % 1000 === 0) {
        log(`Checked ${totalEntities} entities...`);
      }
    }

    issues.duplicateSlug = duplicateSlugs;

    // Count totals
    const totalIssues = Object.values(issues).reduce((sum, arr) => sum + arr.length, 0);

    const report = {
      timestamp: new Date().toISOString(),
      totalEntities,
      totalIssues,
      issueCounts: Object.fromEntries(
        Object.entries(issues).map(([key, arr]) => [key, arr.length]),
      ),
      // Include up to 50 samples per issue type
      issues: Object.fromEntries(
        Object.entries(issues).map(([key, arr]) => [key, arr.slice(0, 50)]),
      ),
    };

    log(`Consistency audit complete: ${totalEntities} entities, ${totalIssues} issues found`);
    for (const [key, arr] of Object.entries(issues)) {
      if (arr.length > 0) log(`  ${key}: ${arr.length}`);
    }

    return res.json(report);
  } catch (err) {
    error(`Consistency audit failed: ${err.message}`);
    return res.json({ error: err.message }, 500);
  }
};
