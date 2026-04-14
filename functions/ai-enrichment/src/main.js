/**
 * AI Entity Enrichment — Appwrite Cloud Function
 *
 * Runs on Appwrite's cloud infrastructure 24/7 — no local machine needed.
 * Queries Appwrite for weak/stub entities, calls Gemini API to enrich them,
 * validates output, and updates entities directly in the database.
 *
 * Schedule: Every 4 hours (0 *​/4 * * *)
 * Also supports manual invocation via Appwrite Console or API.
 *
 * Environment Variables (set as function variables in Appwrite Console):
 *   GEMINI_API_KEY        — Google Gemini API key (free tier)
 *   APPWRITE_API_KEY      — Appwrite API key (auto-injected if using function key)
 *   ENRICHMENT_BATCH_SIZE — Entities per run (default: 20)
 *   ENRICHMENT_MODEL      — Gemini model (default: gemini-2.5-flash-lite)
 *
 * Request body (optional, for manual invocation):
 *   { "count": 20, "label": "Person", "minImportance": 5, "dryRun": false }
 */
const sdk = require('node-appwrite');

const DATABASE_ID = process.env.APPWRITE_DATABASE_ID || 'annals_world_db';
const ENTITIES_COLLECTION = 'entities';
const AUDIT_COLLECTION = 'audit_log';
const GEMINI_MODEL = process.env.ENRICHMENT_MODEL || 'gemini-2.5-flash';
const DEFAULT_BATCH = parseInt(process.env.ENRICHMENT_BATCH_SIZE || '20', 10);

// ═══════════════════════════════════════════════════════════
// Valid verbs and frameworks
// ═══════════════════════════════════════════════════════════

const VALID_VERBS = [
  'CANONIZES', 'CAUSES', 'COLLABORATES_WITH', 'CONTAINS', 'CREATES',
  'DEFINES', 'FRAMES', 'INFLUENCES', 'OCCURS_DURING', 'OCCURS_IN',
  'PARTICIPATES_IN', 'SUCCEEDS', 'TRANSFORMS', 'TRANSMITS',
];

const VALID_FRAMEWORKS = [
  'CAUSE_AND_EFFECT', 'COMPARATIVE_CIVILIZATIONS', 'CULTURAL_TRANSMISSION',
  'DIPLOMATIC_HISTORY', 'ECONOMIC_ANALYSIS', 'ENVIRONMENTAL_HISTORY',
  'FEMINIST_PERSPECTIVE', 'LONGUE_DUREE', 'MARXIST_ANALYSIS',
  'POSTCOLONIAL_ANALYSIS', 'PSYCHOLOGICAL_ANALYSIS', 'RELIGIOUS_INTERPRETATION',
  'STRUCTURAL_ANALYSIS', 'SUBALTERN_STUDIES', 'TECHNOLOGICAL_DETERMINISM',
  'WORLD_SYSTEMS',
];

// ═══════════════════════════════════════════════════════════
// Prompt Template
// ═══════════════════════════════════════════════════════════

function buildPrompt(entity) {
  const summary = entity.summary || '';
  const name = entity.name || entity.slug;
  return `You are enriching entities for "Annals of the World," a scholarly historical knowledge graph spanning 72,000 years of human history.

## Entity to Enrich
- Name: ${name}
- Slug: ${entity.slug}
- Label: ${entity.label || 'unknown'}
- Era: ${entity.era || 'unknown'}
- Region: ${entity.region || 'unknown'}
- Continent: ${entity.continent || 'unknown'}
- Born: ${entity.born || 'unknown'}
- Died: ${entity.died || 'unknown'}
- Current Summary (${summary.length} chars): ${summary.substring(0, 500) || '(none)'}

## Quality Standards

Generate a scholarly yet engaging enrichment following these EXACT standards:

### Summary (STRICTLY 800-1300 characters — HARD LIMIT)
- EXACTLY 3 paragraphs separated by \\n\\n
- Paragraph 1: Identity + dates + core significance
- Paragraph 2: Key achievements, events, contributions
- Paragraph 3: Impact, consequences, legacy
- Include concrete dates, numbers, named events — not vague generalities
- One memorable attributed quote encouraged (in single quotes)
- CRITICAL: The summary MUST be between 800-1300 characters total.

### Causes (exactly 3)
Causal antecedents — single concise sentences.

### Effects (exactly 3)
Consequent outcomes — single concise sentences.

### Relationships (exactly 5)
Each MUST have ALL six fields:
- sourceSlug, sourceName, verb, targetSlug, targetName, context
- verb MUST be one of: ${VALID_VERBS.join(', ')}
- At least 1 with ${entity.slug} as TARGET (incoming influence)
- At least 1 OCCURS_IN with a real place slug

### Places (exactly 3)
Each with: name ("City, Country"), role (1-3 words like "Birthplace")

### Subjects (8-10 items)
Topic tags including country/region and primary domain.

### Frameworks (exactly 3)
Choose from: ${VALID_FRAMEWORKS.join(', ')}

## Output
Return ONLY a valid JSON object:
{"summary": "...", "causes": ["..."], "effects": ["..."], "relationships": [{"sourceSlug": "...", "sourceName": "...", "verb": "...", "targetSlug": "...", "targetName": "...", "context": "..."}], "places": [{"name": "...", "role": "..."}], "subjects": ["..."], "frameworks": ["..."]}`;
}

// ═══════════════════════════════════════════════════════════
// Gemini API Call
// ═══════════════════════════════════════════════════════════

async function callGemini(prompt, apiKey) {
  const url = `https://generativelanguage.googleapis.com/v1beta/models/${GEMINI_MODEL}:generateContent?key=${apiKey}`;

  const body = JSON.stringify({
    contents: [{ parts: [{ text: prompt }] }],
    generationConfig: {
      temperature: 0.7,
      maxOutputTokens: 16384,
      responseMimeType: 'application/json',
      thinkingConfig: { thinkingBudget: 1024 },
    },
  });

  // Retry with backoff on 429 rate limit
  const delays = [0, 15000, 30000, 60000];
  for (const delay of delays) {
    if (delay > 0) await sleep(delay);

    const resp = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body,
    });

    if (resp.status === 429) continue;
    if (!resp.ok) {
      const errText = await resp.text();
      throw new Error(`Gemini ${resp.status}: ${errText.substring(0, 200)}`);
    }

    const data = await resp.json();
    const text = data.candidates?.[0]?.content?.parts?.[0]?.text;
    if (!text) throw new Error('Empty Gemini response');

    return JSON.parse(text);
  }

  throw new Error('Rate limited after 4 retries');
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// ═══════════════════════════════════════════════════════════
// Validation
// ═══════════════════════════════════════════════════════════

function validateEnrichment(result) {
  if (!result || typeof result !== 'object') return { ok: false, reason: 'not a JSON object' };

  // Summary — auto-trim if oversized
  let summary = result.summary || '';
  if (typeof summary !== 'string' || summary.length < 600)
    return { ok: false, reason: `summary too short (${summary.length}c, need >= 600)` };

  if (summary.length > 1300) {
    const paragraphs = summary.split('\n\n');
    let trimmed = '';
    for (const p of paragraphs) {
      const candidate = trimmed ? `${trimmed}\n\n${p}` : p;
      if (candidate.length <= 1300) { trimmed = candidate; } else break;
    }
    if (trimmed.length >= 600) {
      result.summary = trimmed;
    } else if (summary.length > 2500) {
      return { ok: false, reason: `summary too long (${summary.length}c)` };
    }
  }

  // Causes/Effects
  if (!Array.isArray(result.causes) || result.causes.length < 2)
    return { ok: false, reason: `insufficient causes` };
  if (!Array.isArray(result.effects) || result.effects.length < 2)
    return { ok: false, reason: `insufficient effects` };

  // Relationships
  const rels = result.relationships || [];
  if (!Array.isArray(rels) || rels.length < 3)
    return { ok: false, reason: `insufficient relationships` };

  const reqKeys = ['sourceSlug', 'sourceName', 'verb', 'targetSlug', 'targetName', 'context'];
  for (let i = 0; i < rels.length; i++) {
    const rel = rels[i];
    if (!rel || typeof rel !== 'object') return { ok: false, reason: `rel[${i}] not object` };
    for (const k of reqKeys) {
      if (!rel[k]) return { ok: false, reason: `rel[${i}] missing ${k}` };
    }
    if (!VALID_VERBS.includes(rel.verb))
      return { ok: false, reason: `rel[${i}] invalid verb: ${rel.verb}` };
  }

  // Places/Subjects
  if (!Array.isArray(result.places) || result.places.length < 2)
    return { ok: false, reason: `insufficient places` };
  if (!Array.isArray(result.subjects) || result.subjects.length < 5)
    return { ok: false, reason: `insufficient subjects` };

  // Frameworks
  if (!Array.isArray(result.frameworks) || result.frameworks.length < 2)
    return { ok: false, reason: `insufficient frameworks` };
  for (const fw of result.frameworks) {
    if (!VALID_FRAMEWORKS.includes(fw))
      return { ok: false, reason: `invalid framework: ${fw}` };
  }

  return { ok: true, reason: 'ok' };
}

// ═══════════════════════════════════════════════════════════
// Apply Enrichment to Appwrite Document
// ═══════════════════════════════════════════════════════════

async function applyEnrichment(databases, docId, entity, result) {
  // Parse existing detailsJson
  let details = {};
  try {
    if (entity.detailsJson) {
      details = typeof entity.detailsJson === 'string'
        ? JSON.parse(entity.detailsJson)
        : entity.detailsJson;
    }
  } catch { details = {}; }

  details.causes = result.causes || [];
  details.effects = result.effects || [];
  details.relationships = result.relationships || [];
  details.places = result.places || [];

  const updatePayload = {
    summary: result.summary,
    detailsJson: JSON.stringify(details),
  };

  if (result.subjects && result.subjects.length > 0) {
    updatePayload.subjects = result.subjects;
  }
  if (result.frameworks && result.frameworks.length > 0) {
    updatePayload.frameworks = result.frameworks;
  }

  await databases.updateDocument(DATABASE_ID, ENTITIES_COLLECTION, docId, updatePayload);
}

// ═══════════════════════════════════════════════════════════
// Audit Logging
// ═══════════════════════════════════════════════════════════

async function logAuditEntry(databases, slug, oldSummaryLen, newSummaryLen, model) {
  try {
    await databases.createDocument(DATABASE_ID, AUDIT_COLLECTION, sdk.ID.unique(), {
      entitySlug: slug,
      field: 'summary',
      oldValue: `[${oldSummaryLen}c stub/partial]`,
      newValue: `[${newSummaryLen}c AI-enriched]`,
      editorId: `ai-enrichment-bot:${model}`,
      sessionId: `cloud-fn-${Date.now()}`,
      timestamp: new Date().toISOString(),
    });
  } catch {
    // Audit log collection may not exist yet — non-fatal
  }
}

// ═══════════════════════════════════════════════════════════
// Find Weak Entities (replaces enrichment_queue.py for cloud)
// ═══════════════════════════════════════════════════════════

async function findWeakEntities(databases, count, labelFilter, minImportance, log) {
  const PAGE = 100;
  const weak = [];
  let cursor = undefined;
  let scanned = 0;

  // Paginate through entities looking for short summaries
  while (weak.length < count * 3) { // Fetch 3x to account for filtering
    const queries = [
      sdk.Query.limit(PAGE),
      sdk.Query.select([
        '$id', 'slug', 'name', 'label', 'era', 'region', 'continent',
        'born', 'died', 'summary', 'subjects', 'frameworks', 'detailsJson',
        'importanceScore',
      ]),
    ];

    if (labelFilter) {
      queries.push(sdk.Query.equal('label', labelFilter));
    }

    if (cursor) queries.push(sdk.Query.cursorAfter(cursor));

    let res;
    try {
      res = await databases.listDocuments(DATABASE_ID, ENTITIES_COLLECTION, queries);
    } catch (err) {
      log(`Query error: ${err.message}`);
      break;
    }

    if (!res.documents || res.documents.length === 0) break;

    for (const doc of res.documents) {
      scanned++;
      const summaryLen = (doc.summary || '').length;
      const importance = doc.importanceScore || 1;

      // Skip already enriched
      if (summaryLen >= 800) continue;
      // Skip below minimum importance
      if (importance < minImportance) continue;

      // Score: shorter summary = higher priority, higher importance = higher priority
      const summaryScore = Math.max(0, (800 - summaryLen) / 800) * 50;
      const importanceMultiplier = importance / 5;
      const score = summaryScore * importanceMultiplier;

      weak.push({ doc, score, summaryLen });
    }

    cursor = res.documents[res.documents.length - 1].$id;

    if (res.documents.length < PAGE) break;
    if (scanned >= 50000) break; // Safety cap
  }

  log(`Scanned ${scanned} entities, found ${weak.length} weak candidates`);

  // Sort by score descending, take top N
  weak.sort((a, b) => b.score - a.score);
  return weak.slice(0, count);
}

// ═══════════════════════════════════════════════════════════
// Main Function
// ═══════════════════════════════════════════════════════════

module.exports = async ({ req, res, log, error }) => {
  const startTime = Date.now();

  // ── COST CAP: Check usage budget before any work ──
  const { checkUsageBudget, trackUsage } = require('./helpers') || {};
  const isScheduled = !req.body || req.body === '{}';

  // Initialize Appwrite
  const client = new sdk.Client();
  client
    .setEndpoint(process.env.APPWRITE_ENDPOINT || 'https://fra.cloud.appwrite.io/v1')
    .setProject(process.env.APPWRITE_FUNCTION_PROJECT_ID)
    .setKey(process.env.APPWRITE_API_KEY);

  const databases = new sdk.Databases(client);

  // Usage gate — skip if over 70% of Pro plan limits (scheduled runs only)
  if (isScheduled && typeof checkUsageBudget === 'function') {
    try {
      const budget = await checkUsageBudget(databases, log);
      if (!budget.allowed) {
        return res.json({ skipped: true, reason: budget.reason });
      }
    } catch (e) { log(`Usage check error (non-fatal): ${e.message}`); }
  }

  // Get Gemini API key
  const geminiKey = process.env.GEMINI_API_KEY;
  if (!geminiKey) {
    error('GEMINI_API_KEY not set — configure it as a function variable in Appwrite Console');
    return res.json({ error: 'GEMINI_API_KEY not configured' }, 500);
  }

  // Parse request body for overrides
  let count = DEFAULT_BATCH;
  let labelFilter = null;
  let minImportance = 0;
  let dryRun = false;

  try {
    const body = JSON.parse(req.body || '{}');
    if (body.count) count = Math.min(parseInt(body.count, 10), 50); // Cap at 50
    if (body.label) labelFilter = body.label;
    if (body.minImportance) minImportance = parseInt(body.minImportance, 10);
    if (body.dryRun) dryRun = true;
  } catch { /* use defaults */ }

  log(`AI Enrichment starting: count=${count}, model=${GEMINI_MODEL}, label=${labelFilter || 'all'}, dryRun=${dryRun}`);

  // Find weak entities
  const candidates = await findWeakEntities(databases, count, labelFilter, minImportance, log);
  if (candidates.length === 0) {
    log('No weak entities found — all enriched or filtered out');
    return res.json({ message: 'No entities to enrich', scanned: 0, enriched: 0 });
  }

  log(`Found ${candidates.length} candidates for enrichment`);

  let enriched = 0;
  let failed = 0;
  let skipped = 0;
  const results = [];

  for (let i = 0; i < candidates.length; i++) {
    const { doc, score, summaryLen } = candidates[i];
    const slug = doc.slug;

    log(`[${i + 1}/${candidates.length}] ${slug} (score=${score.toFixed(1)}, ${summaryLen}c)`);

    if (dryRun) {
      results.push({ slug, status: 'dry_run', score });
      enriched++;
      continue;
    }

    // Build prompt and call Gemini
    try {
      const prompt = buildPrompt(doc);
      const result = await callGemini(prompt, geminiKey);

      // Validate
      const { ok, reason } = validateEnrichment(result);
      if (!ok) {
        log(`  FAILED validation: ${reason}`);
        failed++;
        results.push({ slug, status: 'failed', reason });
        await sleep(2000);
        continue;
      }

      const newLen = (result.summary || '').length;
      log(`  ENRICHED: ${summaryLen}c → ${newLen}c`);

      // Apply directly to Appwrite
      await applyEnrichment(databases, doc.$id, doc, result);

      // Audit log
      await logAuditEntry(databases, slug, summaryLen, newLen, GEMINI_MODEL);

      enriched++;
      results.push({ slug, status: 'enriched', oldLen: summaryLen, newLen });

      // Rate limit: ~4.5s between calls for Gemini free tier (15 RPM)
      await sleep(4500);

    } catch (err) {
      error(`  ERROR on ${slug}: ${err.message}`);
      failed++;
      results.push({ slug, status: 'error', reason: err.message });
      await sleep(5000);
    }
  }

  const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);

  const summary = {
    timestamp: new Date().toISOString(),
    model: GEMINI_MODEL,
    elapsed: `${elapsed}s`,
    requested: count,
    candidates: candidates.length,
    enriched,
    failed,
    skipped,
    dryRun,
    results,
  };

  log(`DONE: ${enriched} enriched, ${failed} failed in ${elapsed}s`);

  // ── Track usage: reads from scanning + writes from enrichments/audits ──
  if (typeof trackUsage === 'function') {
    const readsEstimate = candidates.length * 15 + 100; // select fields per candidate + scan
    const writesEstimate = enriched * 2; // 1 entity update + 1 audit log per enrichment
    try { await trackUsage(databases, readsEstimate, writesEstimate, 'ai-enrichment', log); } catch {}
  }

  return res.json(summary);
};
