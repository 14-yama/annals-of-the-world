# Appwrite Export — Local Entity Repository

This directory contains the local backup/export of Appwrite backend entities,
organised by the Annals Dewey Decimal-inspired classification system.

## Structure

```
entities/
  0-Ideas-Core/         Class 0: Core ideas & philosophical constructs
  1-Ideas-Other/        Class 1: Secondary ideas, theories, doctrines
  2-People/             Class 2: All people (40 divisions)
    220-Political-Leaders/
    240-Scientists-Inventors/
    250-Religious-Figures/
    280-Military-Leaders-Commanders/
    ...
  3-Institutions/       Class 3: Organisations, governments, bodies
  4-Places/             Class 4: Geographic entities
  5-Events/             Class 5: Historical events & event windows
  6-Movements/          Class 6: Social, political, religious movements
  7-Artifacts-Texts/    Class 7: Written works, artifacts
  8-Evidence/           Class 8: Scholarly evidence & sources
  9-Timeframes/         Class 9: Chronological frameworks & eras

relationships.json      All inter-entity relationships
evidence.json           Evidence documents
media.json              Media references
timeline_entries.json   Timeline events
audit_log.json          Edit audit trail
manifest.json           Export metadata & timestamps
```

## Usage

### Export from Appwrite

```bash
APPWRITE_API_KEY=<key> npx tsx scripts/sync_appwrite_to_repo.ts
```

### Import to Appwrite

```bash
# Dry run (preview only)
APPWRITE_API_KEY=<key> npx tsx scripts/sync_repo_to_appwrite.ts --dry-run

# Full import (skip existing)
APPWRITE_API_KEY=<key> npx tsx scripts/sync_repo_to_appwrite.ts

# Force overwrite existing
APPWRITE_API_KEY=<key> npx tsx scripts/sync_repo_to_appwrite.ts --force
```

## Source of Truth

**Appwrite is the live, canonical source of truth.** These JSON files are the
backup/sync copy. When running `sync_appwrite_to_repo.ts`, this directory is
refreshed with the latest Appwrite state.

To restore from backup: run `sync_repo_to_appwrite.ts` with `--force`.
