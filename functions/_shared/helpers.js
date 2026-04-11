/**
 * Shared helpers for Appwrite Functions.
 * Each function copies this file into its own src/ at deploy time,
 * or you can symlink it.
 */
const sdk = require('node-appwrite');

const DATABASE_ID = process.env.APPWRITE_DATABASE_ID || 'annals_db';

function initClient() {
  const client = new sdk.Client();
  client
    .setEndpoint(process.env.APPWRITE_ENDPOINT || 'https://fra.cloud.appwrite.io/v1')
    .setProject(process.env.APPWRITE_FUNCTION_PROJECT_ID)
    .setKey(process.env.APPWRITE_API_KEY);
  return client;
}

/**
 * Paginate through ALL documents in a collection matching the given queries.
 * Returns an array of all documents.
 */
async function paginateAll(databases, collectionId, extraQueries = [], selectFields = null) {
  const PAGE = 100;
  const all = [];
  let cursor = undefined;

  while (true) {
    const q = [...extraQueries, sdk.Query.limit(PAGE)];
    if (selectFields) q.push(sdk.Query.select(selectFields));
    if (cursor) q.push(sdk.Query.cursorAfter(cursor));

    const res = await databases.listDocuments(DATABASE_ID, collectionId, q);
    all.push(...res.documents);

    if (res.documents.length < PAGE) break;
    cursor = res.documents[res.documents.length - 1].$id;
  }

  return all;
}

module.exports = { initClient, paginateAll, DATABASE_ID, sdk };
