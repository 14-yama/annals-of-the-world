/**
 * Backup Export Function
 *
 * Exports all collections to JSON and stores them as Appwrite Storage files.
 * Creates a timestamped backup that can be downloaded from the console.
 *
 * Collections exported: entities, relationships, evidence, media,
 *   timeline_entries, audit_log
 *
 * Schedule: Weekly on Sunday at 00:00 UTC
 */
const sdk = require('node-appwrite');

const DATABASE_ID = process.env.APPWRITE_DATABASE_ID || 'annals_db';
const BACKUP_BUCKET = 'backups';

const COLLECTIONS_TO_EXPORT = [
  'entities',
  'relationships',
  'evidence',
  'media',
  'timeline_entries',
  'audit_log',
];

module.exports = async ({ req, res, log, error }) => {
  const client = new sdk.Client();
  client
    .setEndpoint(process.env.APPWRITE_ENDPOINT || 'https://fra.cloud.appwrite.io/v1')
    .setProject(process.env.APPWRITE_FUNCTION_PROJECT_ID)
    .setKey(process.env.APPWRITE_API_KEY);

  const databases = new sdk.Databases(client);
  const storage = new sdk.Storage(client);

  const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
  log(`Starting backup export — ${timestamp}`);

  // Ensure backup bucket exists
  try {
    await storage.getBucket(BACKUP_BUCKET);
  } catch {
    try {
      await storage.createBucket(BACKUP_BUCKET, 'Backups', [
        sdk.Permission.read(sdk.Role.team('admin')),
      ]);
      log('Created backups bucket');
    } catch (err) {
      log(`Bucket creation skipped: ${err.message}`);
    }
  }

  const summary = { timestamp, collections: {} };

  for (const collectionId of COLLECTIONS_TO_EXPORT) {
    log(`Exporting ${collectionId}...`);

    const PAGE = 100;
    let cursor = undefined;
    const allDocs = [];

    try {
      while (true) {
        const q = [sdk.Query.limit(PAGE)];
        if (cursor) q.push(sdk.Query.cursorAfter(cursor));

        const batch = await databases.listDocuments(DATABASE_ID, collectionId, q);
        if (batch.documents.length === 0) break;

        // Strip internal Appwrite metadata to reduce size
        for (const doc of batch.documents) {
          const clean = { ...doc };
          delete clean.$databaseId;
          delete clean.$collectionId;
          delete clean.$permissions;
          allDocs.push(clean);
        }

        cursor = batch.documents[batch.documents.length - 1].$id;
      }

      summary.collections[collectionId] = {
        count: allDocs.length,
        status: 'ok',
      };

      // Upload as JSON file to storage
      const json = JSON.stringify({
        _meta: {
          collection: collectionId,
          exportedAt: timestamp,
          count: allDocs.length,
        },
        documents: allDocs,
      });

      const fileName = `${collectionId}-${timestamp}.json`;
      const fileBlob = new Blob([json], { type: 'application/json' });

      try {
        const fileId = sdk.ID.unique();
        await storage.createFile(
          BACKUP_BUCKET,
          fileId,
          sdk.InputFile.fromBlob(fileBlob, fileName),
        );
        summary.collections[collectionId].fileId = fileId;
        summary.collections[collectionId].fileName = fileName;
        log(`  ${collectionId}: ${allDocs.length} docs → ${fileName}`);
      } catch (uploadErr) {
        // If storage upload fails, just log it
        summary.collections[collectionId].uploadError = uploadErr.message;
        log(`  ${collectionId}: ${allDocs.length} docs (upload failed: ${uploadErr.message})`);
      }
    } catch (err) {
      summary.collections[collectionId] = {
        count: 0,
        status: 'error',
        error: err.message,
      };
      log(`  ${collectionId}: ERROR — ${err.message}`);
    }
  }

  const totalDocs = Object.values(summary.collections).reduce(
    (sum, c) => sum + (c.count || 0), 0
  );

  log(`Backup complete: ${totalDocs} total documents across ${COLLECTIONS_TO_EXPORT.length} collections`);

  return res.json(summary);
};
