# Autonomous Enrichment Pipeline — Governance & Policy

> Policy document for the AI-powered autonomous entity enrichment system.
> Curator sets criteria and thresholds; machines execute 24/7.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    CURATOR (Human)                           │
│  Sets policy, thresholds, approved entity pool, reviews     │
└─────────────────┬───────────────────────────────────────────┘
                  │ Policy files + queue config
                  ▼
┌─────────────────────────────────────────────────────────────┐
│              LAYER 1: AI ENRICHMENT ENGINE                   │
│  GitHub Actions cron (every 6h) + LLM API (Gemini/OpenAI)  │
│                                                             │
│  1. enrichment_queue.py → scans & ranks weak entities       │
│  2. ai_enrich_autonomous.py → calls LLM → validates →      │
│     writes JSON → syncs to Appwrite                         │
│  3. git commit → push                                       │
└─────────────────┬───────────────────────────────────────────┘
                  │ Direct API sync
                  ▼
┌─────────────────────────────────────────────────────────────┐
│              LAYER 2: QUALITY GATE                           │
│  Appwrite Cloud Functions (already running on schedule)     │
│                                                             │
│  - audit-consistency (every 30 min) → schema validation     │
│  - audit-duplicates (weekly) → fuzzy dedup                  │
│  - audit-orphans (daily) → relationship coverage            │
│  - audit-classification (daily) → Dewey code validation     │
└─────────────────┬───────────────────────────────────────────┘
                  │ Audit reports
                  ▼
┌─────────────────────────────────────────────────────────────┐
│              LAYER 3: CURATOR OVERRIDE                       │
│  Weekly review via /curator/audit/log or Appwrite console   │
│                                                             │
│  - Review AI enrichments (editorId: 'ai-enrichment-bot')   │
│  - Reject/edit poor quality enrichments                     │
│  - Adjust policy thresholds if needed                       │
│  - Add new entities to proposed pool                        │
└─────────────────────────────────────────────────────────────┘
```

---

## Pipeline Components

### 1. Enrichment Queue (`scripts/enrichment_queue.py`)

Scans all ~358K entity JSON files and scores each by weakness:

| Factor | Points | Description |
|--------|--------|-------------|
| Summary length | 0–50 | Shorter summary = higher score |
| Missing causes | 5 | No `detailsJson.causes` array |
| Missing effects | 5 | No `detailsJson.effects` array |
| Missing relationships | 5 | Fewer than 3 relationships |
| Missing places | 5 | No `detailsJson.places` array |
| Missing subjects | 5 | Fewer than 3 subject tags |
| Missing frameworks | 5 | Fewer than 2 frameworks |
| Stub pattern | 20 | Contains "a notable figure associated with..." |
| Importance multiplier | ×0.2–2.0 | `importanceScore / 5` scales total |

**Output:** `data/enrichment/queue.json` — sorted priority list (highest score first)

### 2. AI Enrichment Engine (`scripts/ai_enrich_autonomous.py`)

Reads queue, calls LLM, validates, writes, syncs:

- **Input:** Queue JSON + LLM API key
- **LLM Call:** Structured prompt with entity data + quality standards
- **Validation:** Rejects enrichments that fail schema/quality checks
- **Output:** Updated entity JSON files + Appwrite sync
- **Report:** `data/enrichment/last_run.json`

### 3. GitHub Actions Workflow (`.github/workflows/ai-enrichment.yml`)

- **Schedule:** Every 6 hours (`0 */6 * * *`)
- **Manual trigger:** `workflow_dispatch` with configurable count, model, dry-run
- **Flow:** Generate queue → Run enrichment → Commit changes → Push

---

## Quality Thresholds

Enrichments are **rejected** if they fail ANY of these checks:

| Check | Threshold | Rationale |
|-------|-----------|-----------|
| Summary length | ≥ 600 chars | Minimum viable scholarly narrative |
| Summary length | ≤ 2,000 chars | Prevent over-generation |
| Causes | ≥ 2 items | Minimum causal context |
| Effects | ≥ 2 items | Minimum consequential context |
| Relationships | ≥ 3 items | Minimum graph connectivity |
| Relationship schema | All 6 fields required | sourceSlug, sourceName, verb, targetSlug, targetName, context |
| Relationship verbs | Must be in approved list | 14 canonical verbs only |
| Places | ≥ 2 items | Geographic grounding |
| Subjects | ≥ 5 items | Topic coverage |
| Frameworks | ≥ 2 items, all valid | From 16 approved frameworks |

**On failure:** Entity is skipped for that run. Will be retried on next run.

---

## LLM Configuration

### Primary: Google Gemini 1.5 Flash (FREE)

| Parameter | Value |
|-----------|-------|
| Model | `gemini-1.5-flash` |
| Rate limit | 15 RPM (4s between calls) |
| Daily limit | 1M tokens (~500 entities/day) |
| Cost | **$0/month** |
| Temperature | 0.7 |
| Max output tokens | 4,096 |
| Response format | `application/json` (forced) |

### Fallback: OpenAI GPT-4o-mini (PAID)

| Parameter | Value |
|-----------|-------|
| Model | `gpt-4o-mini` |
| Rate limit | ~500 RPM |
| Cost | ~$0.15/1M input + $0.60/1M output |
| Estimated monthly | ~$15 at 500 entities/day |
| Temperature | 0.7 |
| Response format | `json_object` (forced) |

### API Keys (GitHub Actions Secrets)

| Secret | Required | Notes |
|--------|----------|-------|
| `GEMINI_API_KEY` | Yes (default) | Get free: https://aistudio.google.com/apikey |
| `OPENAI_API_KEY` | Optional | Only if using `--model openai` |
| `APPWRITE_API_KEY` | Yes | Already configured for sync-to-appwrite workflow |

---

## Batch Size & Schedule

| Parameter | Default | Rationale |
|-----------|---------|-----------|
| Entities per run | 25 | Conservative; avoids rate limits |
| Runs per day | 4 (every 6h) | 100 entities/day sustained |
| Rate limit delay | 4.5s (Gemini) / 1.5s (OpenAI) | Stays within API limits |
| Retry on failure | 1 attempt | Avoids wasted API calls on bad entities |
| Queue regeneration | Every run | Always uses fresh priority ranking |

### Projected Timeline

| Batch size | Entities/day | Time to clear 35K stubs | Monthly cost |
|------------|-------------|------------------------|--------------|
| 25/run × 4 | 100 | ~350 days | $0 (Gemini) |
| 50/run × 4 | 200 | ~175 days | $0 (Gemini) |
| 100/run × 4 | 400 | ~88 days | $0 (Gemini) |
| 125/run × 4 | 500 | ~71 days | $0 (Gemini, at daily limit) |

**Recommendation:** Start with 25/run, monitor quality, increase to 100/run after 1 week.

---

## Curator Review Process

### Weekly Review (15 minutes)

1. Visit `/curator/audit/log` or Appwrite Console
2. Filter by `editorId = 'ai-enrichment-bot'` (future: when audit logging added)
3. Spot-check 5–10 random AI-enriched entities
4. Flag any that need correction
5. Adjust thresholds in `ai_enrich_autonomous.py` if quality dips

### Monthly Review (30 minutes)

1. Run `python3 scripts/enrichment_queue.py --stats` to check remaining backlog
2. Review `data/enrichment/last_run.json` reports for failure patterns
3. Add new entities to proposed pool if gaps found
4. Consider increasing batch size if quality is stable

### Quality Rejection Criteria

Curator should **reject** AI enrichments that:
- Contain factual errors (wrong dates, wrong attribution)
- Confuse entities with similar names (e.g., wrong Henry, wrong Alexander)
- Generate anachronistic relationships
- Produce generic prose without specific dates/events
- Hallucinate non-existent historical events

---

## Safety & Controls

### Circuit Breakers

| Condition | Action |
|-----------|--------|
| > 50% failure rate in a run | Pipeline logs warning; curator review recommended |
| LLM API key expired/revoked | Pipeline exits with error code 1 |
| Appwrite sync failure | Entity still saved locally; sync retried next run |
| Git push failure | Changes preserved in working directory; manual push needed |

### Rollback

- All changes are git-committed with clear AI commit messages
- `git revert <commit>` to undo any bad batch
- Appwrite edits traceable via `audit_log` collection
- `sync_repo_to_appwrite.ts --force` to overwrite Appwrite from git

### What the Pipeline Does NOT Do

- Does not delete entities
- Does not modify entities already enriched (summary ≥ 800c)
- Does not create new entities (enrichment only — creation requires curator approval)
- Does not modify non-entity files
- Does not run without API keys configured

---

## Future Extensions

### Phase 2: New Entity Creation Pipeline
- `data/enrichment/proposed_entities.json` — curator-approved entity pool
- `scripts/propose_new_entities.py` — Wikidata SPARQL discovery
- Auto-create entities with `importanceScore >= 7` from Wikidata

### Phase 3: Appwrite-Native Function
- `functions/ai-enrichment/` — Appwrite Cloud Function
- Enriches directly in backend (no git round-trip)
- Schedule: every 4 hours

### Phase 4: Quality Monitoring Dashboard
- Real-time enrichment progress on frontend
- Quality score trends over time
- Failure pattern analysis

---

## Scripts Reference

| Script | Purpose | Runs |
|--------|---------|------|
| `scripts/enrichment_queue.py` | Scan & rank weak entities | Every pipeline run |
| `scripts/ai_enrich_autonomous.py` | LLM enrichment + validation + sync | Every pipeline run |
| `.github/workflows/ai-enrichment.yml` | Orchestrate pipeline on schedule | Every 6 hours |

## Files

| Path | Purpose |
|------|---------|
| `data/enrichment/queue.json` | Current priority queue (regenerated each run) |
| `data/enrichment/last_run.json` | Last enrichment run report |
| `data/enrichment/proposed_entities.json` | Entity creation pool (Phase 2) |
