# Curator Audit System Guide

> Reference for the Annals of the World automated and manual audit infrastructure.

## Overview

The audit system provides:
1. **Edit Governance** — Per-field change tracking with curator identity
2. **Automated Audits** — Scheduled Appwrite Cloud Functions for data quality
3. **Backup/Sync** — Bidirectional sync between Appwrite and local JSON

---

## 1. Edit Audit Trail

### How It Works

Every edit made through the curator interface is logged to the `audit_log` Appwrite collection.

| Field | Description |
|-------|-------------|
| `entityId` | Appwrite document ID of the edited entity |
| `entitySlug` | Entity slug for human-readable identification |
| `entityName` | Entity display name at time of edit |
| `action` | `update`, `create`, `delete`, or `batch` |
| `field` | Specific field that changed (e.g. `summary`, `era`) |
| `oldValue` | Previous value (up to 10,000 chars) |
| `newValue` | New value after edit |
| `editorId` | Curator who made the change |
| `editorNote` | Optional note explaining the change |
| `timestamp` | ISO 8601 timestamp |
| `sessionId` | Browser session UUID (groups edits from one session) |

### Viewing the Audit Log

Navigate to **`/curator/audit/log`** in the application.

Features:
- **Filter by entity** — Search by slug
- **Filter by editor** — See all edits by a specific curator
- **Filter by action** — Show only updates, creates, etc.
- **Sort by timestamp** — Most recent first
- **CSV Export** — Download the current filtered view
- **Stats cards** — Total entries, update count, active editors, latest edit

### Curator Identity

On first edit, curators are prompted for their name. This is stored in `localStorage` and included in all subsequent audit entries for that browser session.

---

## 2. Automated Audit Functions

Five Appwrite Cloud Functions run on scheduled cron jobs:

### audit-completeness (Daily, 02:00 UTC)

Scans every entity and scores it on 9 quality dimensions:
- Relationships, Causes, Effects, Frameworks, Places, Texts
- Image URL, Wikidata QID, Summary (≥50 characters)

**Output:** Score distribution (0–9), missing field counts, low-score entities.

### audit-orphans (Daily, 03:00 UTC)

Detects entities with zero relationships:
- Checks the `relationships` collection for connected slugs
- Also checks entity's own `detailsJson.relationships` array
- Groups orphans by label type

### audit-duplicates (Weekly, Sunday 04:00 UTC)

Fuzzy duplicate detection using Levenshtein distance:
- Normalises names (lowercase, strip punctuation)
- Compares within same label type
- 85% similarity threshold
- Reports exact and fuzzy matches

### audit-consistency (Daily, 05:00 UTC)

Validates data integrity rules:
- Era ↔ eraDivisionCode consistency
- callNumber format (`Class.Division.Slug`)
- Required fields (slug, name, label, callNumber)
- Slug format (lowercase, hyphenated)
- Canonical era and label values
- Duplicate slug detection

### backup-export (Weekly, Sunday 00:00 UTC)

Exports all collections to JSON files in Appwrite Storage:
- entities, relationships, evidence, media, timeline_entries, audit_log
- Each file includes `_meta` with collection name, timestamp, count
- Stored in `backups` bucket

### Deploying Functions

```bash
# Install Appwrite CLI
npm install -g appwrite-cli

# Login
appwrite login

# Deploy all functions
appwrite deploy function

# Deploy a single function
appwrite deploy function --functionId=audit-completeness
```

### Environment Variables (set in Appwrite Console)

| Variable | Description |
|----------|-------------|
| `APPWRITE_ENDPOINT` | API endpoint (defaults to `https://fra.cloud.appwrite.io/v1`) |
| `APPWRITE_API_KEY` | Server API key with `databases.read` + `databases.write` |
| `APPWRITE_DATABASE_ID` | Database ID (defaults to `annals_db`) |

---

## 3. Backup & Sync

### Export: Appwrite → Repo

```bash
APPWRITE_API_KEY=<key> npx tsx scripts/sync_appwrite_to_repo.ts
```

Creates `data/appwrite-export/` with class-based folder structure:
```
entities/
  0-Ideas-Core/
  2-People/
    220.json   # Political Leaders division
    240.json   # Scientists & Inventors division
  ...
relationships.json
evidence.json
manifest.json
```

Flags:
- `--entities-only` — Skip non-entity collections
- `--collection=X` — Export only one collection

### Import: Repo → Appwrite

```bash
# Preview
APPWRITE_API_KEY=<key> npx tsx scripts/sync_repo_to_appwrite.ts --dry-run

# Execute (skip existing)
APPWRITE_API_KEY=<key> npx tsx scripts/sync_repo_to_appwrite.ts

# Force overwrite
APPWRITE_API_KEY=<key> npx tsx scripts/sync_repo_to_appwrite.ts --force
```

---

## 4. Curator UI Features

### Shuffle Mode

Toggle random entity ordering in DivisionDetail view:
- Uses server-side random offset + Fisher-Yates shuffle within page
- Persisted to localStorage
- Useful for reviewing entities across the full dataset

### Accurate Entity Counts

ClassHub and DivisionDetail use cursor-based pagination to get accurate totals (bypasses Appwrite's 5,000 `res.total` cap).

### Server-Side Sorting

Sort by importance score, name, or era with server-side `Query.orderDesc/orderAsc` for consistent results across pages.
