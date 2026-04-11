/**
 * Backup Export Function
 *
 * Exports entities split by Dewey class and division to small JSON files
 * in Appwrite Storage. Each file is <5MB, suitable for git commit after
 * downloading with sync_appwrite_to_repo.ts.
 *
 * Structure in storage:
 *   entities/{classDigit}-{className}/{division}.json
 *   {collectionId}.json
 *
 * Schedule: Weekly on Sunday at 00:00 UTC
 */
const sdk = require('node-appwrite');

const DATABASE_ID = process.env.APPWRITE_DATABASE_ID || 'annals_db';
const BACKUP_BUCKET = 'backups';

const DEWEY_CLASSES = {
  '0': 'Ideas-Core',
  '1': 'Ideas-Other',
  '2': 'People',
  '3': 'Institutions',
  '4': 'Places',
  '5': 'Events',
  '6': 'Movements',
  '7': 'Artifacts-Texts',
  '8': 'Evidence',
  '9': 'Timeframes',
};

const OTHER_COLLECTIONS = [
  'relationships',
  'evidence',
  'media',
  'timeline_entries',
];

/**
 * Upload JSON data as a file to Appwrite Storage.
 * Uses Buffer (Node-compatible) instead of Blob.
 */
async function uploadJson(storage, fileName, data) {
  const json = JSON.stringify(data);
  const buffer = Buffer.from(json, 'utf-8');
  await storage.createFile(
    BACKUP_BUCKET,
    sdk.ID.unique(),
    sdk.InputFile.fromBuffer(buffer, fileName),
  );
  return Math.round(buffer.length / 1024);
}

/**
 * Paginate through all documents matching queries.
 * Uses 5000/page for speed. Strips Appwrite metadata.
 */
async function fetchAll(databases, collectionId, queries) {
  const docs = [];
  let cursor;
  while (true) {
    const q = [...(queries || []), sdk.Query.limit(5000)];
    if (cursor) q.push(sdk.Query.cursorAfter(cursor));
    const batch = await databases.listDocuments(DATABASE_ID, collectionId, q);
    if (batch.documents.length === 0) break;
    for (const doc of batch.documents) {
      delete doc.$databaseId;
      delete doc.$collectionId;
      delete doc.$permissions;
      docs.push(doc);
    }
    cursor = batch.documents[batch.documents.length - 1].$id;
    if (batch.documents.length < 5000) break;
  }
  return docs;
}

module.exports = async ({ req, res, log, error }) => {
  const client = new sdk.Client();
  client
    .setEndpoint(process.env.APPWRITE_ENDPOINT || 'https://fra.cloud.appwrite.io/v1')
    .setProject(process.env.APPWRITE_FUNCTION_PROJECT_ID)
    .setKey(process.env.APPWRITE_API_KEY);

  const databases = new sdk.Databases(client);
  const storage = new sdk.Storage(client);

  const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
  log('Starting backup export — ' + timestamp);

  // Ensure backup bucket exists
  try {
    await storage.getBucket(BACKUP_BUCKET);
  } catch (_) {
    try {
      await storage.createBucket(BACKUP_BUCKET, 'Backups', [
        sdk.Permission.read(sdk.Role.any()),
      ]);
      log('Created backups bucket');
    } catch (err) {
      log('Bucket creation skipped: ' + err.message);
    }
  }

  const summary = { timestamp: timestamp, files: [], totalEntities: 0, errors: [] };

  // Export entities by Dewey class then division
  for (const [classDigit, className] of Object.entries(DEWEY_CLASSES)) {
    log('Exporting class ' + classDigit + ' (' + className + ')...');

    try {
      const allDocs = await fetchAll(databases, 'entities', [
        sdk.Query.startsWith('callNumber', classDigit),
      ]);

      if (allDocs.length === 0) {
        log('  Class ' + classDigit + ': 0 entities, skipping');
        continue;
      }

      // Group by division (first 2-3 digits before the dot)
      const byDivision = {};
      for (const doc of allDocs) {
        var cn = doc.callNumber || '';
        var divMatch = cn.match(/^(\d{2,3})\./);
        var division = divMatch ? divMatch[1] : classDigit + '00';
        if (!byDivision[division]) byDivision[division] = [];
        byDivision[division].push(doc);
      }

      // Upload each division as a separate file
      for (const [division, docs] of Object.entries(byDivision)) {
        var fileName = 'entities/' + classDigit + '-' + className + '/' + division + '.json';
        try {
          var sizeKB = await uploadJson(storage, fileName, {
            _meta: { class: classDigit, className: className, division: division, exportedAt: timestamp, count: docs.length },
            entities: docs,
          });
          summary.files.push({ fileName: fileName, count: docs.length, sizeKB: sizeKB });
          log('  ' + fileName + ': ' + docs.length + ' entities (' + sizeKB + 'KB)');
        } catch (uploadErr) {
          summary.errors.push({ fileName: fileName, error: uploadErr.message });
          log('  ' + fileName + ': upload failed — ' + uploadErr.message);
        }
      }

      summary.totalEntities += allDocs.length;
      log('  Class ' + classDigit + ': ' + allDocs.length + ' entities -> ' + Object.keys(byDivision).length + ' files');

    } catch (err) {
      summary.errors.push({ class: classDigit, error: err.message });
      log('  Class ' + classDigit + ': ERROR — ' + err.message);
    }
  }

  // Export other collections as single files
  for (const collectionId of OTHER_COLLECTIONS) {
    log('Exporting ' + collectionId + '...');

    try {
      var allDocs = await fetchAll(databases, collectionId);

      if (allDocs.length === 0) {
        log('  ' + collectionId + ': 0 docs, skipping');
        continue;
      }

      var fileName = collectionId + '.json';
      try {
        var sizeKB = await uploadJson(storage, fileName, {
          _meta: { collection: collectionId, exportedAt: timestamp, count: allDocs.length },
          documents: allDocs,
        });
        summary.files.push({ fileName: fileName, count: allDocs.length, sizeKB: sizeKB });
        log('  ' + collectionId + ': ' + allDocs.length + ' docs (' + sizeKB + 'KB)');
      } catch (uploadErr) {
        summary.errors.push({ fileName: fileName, error: uploadErr.message });
      }
    } catch (err) {
      summary.errors.push({ collection: collectionId, error: err.message });
      log('  ' + collectionId + ': ERROR — ' + err.message);
    }
  }

  log('Backup complete: ' + summary.totalEntities + ' entities across ' + summary.files.length + ' files');
  if (summary.errors.length) log('  ' + summary.errors.length + ' errors encountered');

  return res.json(summary);
};
