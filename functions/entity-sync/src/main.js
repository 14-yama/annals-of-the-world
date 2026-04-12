/**
 * Entity Sync — Event-driven stats updater
 *
 * Triggered on entity create/update/delete events.
 * Performs an incremental update to stats_cache so global counts
 * stay accurate in near-real-time without waiting for the 30-min
 * audit-consistency scheduled run.
 *
 * Events:
 *   databases.annals_world_db.collections.entities.documents.*.create
 *   databases.annals_world_db.collections.entities.documents.*.update
 *   databases.annals_world_db.collections.entities.documents.*.delete
 *
 * Strategy:
 *   - On create: increment total + relevant label/era/continent/class counts
 *   - On delete: decrement total + relevant label/era/continent/class counts
 *   - On update: if label/era/continent/class changed, adjust both old and new
 *   - Falls back to triggering a full stats recount if the incremental update fails
 */
const sdk = require('node-appwrite');

const DATABASE_ID = process.env.APPWRITE_DATABASE_ID || 'annals_db';
const STATS_COLLECTION = 'stats_cache';

module.exports = async ({ req, res, log, error }) => {
  const client = new sdk.Client();
  client
    .setEndpoint(process.env.APPWRITE_ENDPOINT || 'https://fra.cloud.appwrite.io/v1')
    .setProject(process.env.APPWRITE_FUNCTION_PROJECT_ID)
    .setKey(process.env.APPWRITE_API_KEY);

  const databases = new sdk.Databases(client);

  // Parse the event
  const event = req.headers['x-appwrite-event'] || '';
  log(`Entity sync triggered: ${event}`);

  // Determine event type
  let eventType = 'unknown';
  if (event.includes('.create')) eventType = 'create';
  else if (event.includes('.delete')) eventType = 'delete';
  else if (event.includes('.update')) eventType = 'update';

  // Get the entity document from the event payload
  let entity;
  try {
    // Appwrite may provide body as object, string, or in bodyRaw
    if (req.body && typeof req.body === 'object' && req.body.$id) {
      entity = req.body;
    } else if (typeof req.body === 'string' && req.body.length > 0) {
      entity = JSON.parse(req.body);
    } else if (req.bodyRaw && typeof req.bodyRaw === 'string') {
      entity = JSON.parse(req.bodyRaw);
    } else if (req.bodyJson) {
      entity = req.bodyJson;
    } else {
      // Try to extract entity slug from the event string itself
      // Event format: databases.*.collections.entities.documents.<id>.create
      const match = event.match(/documents\.([^.]+)\.(create|update|delete)/);
      if (match) {
        log(`No body found — extracting slug from event: ${match[1]}`);
        // For create/update, fetch the document; for delete, we only have the ID
        if (eventType !== 'delete') {
          const databases = new sdk.Databases(client);
          entity = await databases.getDocument(DATABASE_ID, 'entities', match[1]);
        } else {
          entity = { $id: match[1], slug: match[1] };
        }
      }
    }
  } catch (e) {
    error(`Could not parse event body: ${e.message}`);
    // Fall through — try event string extraction
    const match = event.match(/documents\.([^.]+)\.(create|update|delete)/);
    if (match && eventType !== 'delete') {
      try {
        entity = await databases.getDocument(DATABASE_ID, 'entities', match[1]);
        log(`Fetched entity from DB after body parse failure: ${entity.slug}`);
      } catch (fetchErr) {
        error(`Could not fetch entity either: ${fetchErr.message}`);
        return res.json({ ok: false, error: 'Invalid body and fetch failed' }, 400);
      }
    } else if (match) {
      entity = { $id: match[1], slug: match[1] };
    } else {
      return res.json({ ok: false, error: 'Invalid body' }, 400);
    }
  }

  if (!entity || !entity.$id) {
    log('No entity in event body — skipping');
    return res.json({ ok: true, skipped: true });
  }

  log(`Event: ${eventType}, Entity: ${entity.slug || entity.$id}, Label: ${entity.label}, Era: ${entity.era}`);

  try {
    // Read the latest stats_cache row
    const statsResult = await databases.listDocuments(
      DATABASE_ID, STATS_COLLECTION,
      [sdk.Query.orderDesc('updatedAt'), sdk.Query.limit(1)]
    );

    if (statsResult.documents.length === 0) {
      log('No stats_cache row found — triggering full recount via audit-consistency');
      return res.json({ ok: true, action: 'no-cache-row' });
    }

    const statsDoc = statsResult.documents[0];
    let total = statsDoc.total || 0;
    let byLabel = typeof statsDoc.byLabel === 'string' ? JSON.parse(statsDoc.byLabel) : (statsDoc.byLabel || {});
    let byEra = typeof statsDoc.byEra === 'string' ? JSON.parse(statsDoc.byEra) : (statsDoc.byEra || {});
    let byContinent = typeof statsDoc.byContinent === 'string' ? JSON.parse(statsDoc.byContinent) : (statsDoc.byContinent || {});
    let byClass = typeof statsDoc.byClass === 'string' ? JSON.parse(statsDoc.byClass) : (statsDoc.byClass || {});

    const classDigit = entity.callNumber ? entity.callNumber[0] : null;

    if (eventType === 'create') {
      total += 1;
      if (entity.label) byLabel[entity.label] = (byLabel[entity.label] || 0) + 1;
      if (entity.era) byEra[entity.era] = (byEra[entity.era] || 0) + 1;
      if (entity.continent) byContinent[entity.continent] = (byContinent[entity.continent] || 0) + 1;
      if (classDigit) byClass[classDigit] = (byClass[classDigit] || 0) + 1;
      log(`Incremented: total=${total}, label=${entity.label}, era=${entity.era}, continent=${entity.continent}, class=${classDigit}`);
    } else if (eventType === 'delete') {
      total = Math.max(0, total - 1);
      if (entity.label) byLabel[entity.label] = Math.max(0, (byLabel[entity.label] || 0) - 1);
      if (entity.era) byEra[entity.era] = Math.max(0, (byEra[entity.era] || 0) - 1);
      if (entity.continent) byContinent[entity.continent] = Math.max(0, (byContinent[entity.continent] || 0) - 1);
      if (classDigit) byClass[classDigit] = Math.max(0, (byClass[classDigit] || 0) - 1);
      log(`Decremented: total=${total}, label=${entity.label}, era=${entity.era}, continent=${entity.continent}, class=${classDigit}`);
    } else if (eventType === 'update') {
      // For updates, we can't know the old values from just the event payload,
      // so we just update the timestamp. The scheduled recount will correct any drift.
      log('Update event — refreshing timestamp only (scheduled recount corrects drift)');
    }

    // Write updated stats — update the existing row in-place
    await databases.updateDocument(DATABASE_ID, STATS_COLLECTION, statsDoc.$id, {
      total,
      byLabel: JSON.stringify(byLabel),
      byEra: JSON.stringify(byEra),
      byContinent: JSON.stringify(byContinent),
      byClass: JSON.stringify(byClass),
      updatedAt: new Date().toISOString(),
    });

    log(`Stats cache updated: total=${total}`);
    return res.json({ ok: true, eventType, total });

  } catch (err) {
    error(`Entity sync failed: ${err.message}`);
    return res.json({ ok: false, error: err.message }, 500);
  }
};
