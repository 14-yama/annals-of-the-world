#!/usr/bin/env python3
"""
migrate_to_caricom.py — Migrate Annals of the World to CARICOM Connects Appwrite

Phase 1: Create database + collections (schema migration)
Phase 2: Clean wikipedia- slugs across all JSON files
Phase 3: Seed all entities to the new backend (batched, deduplicated)

Usage:
  source .env && export APPWRITE_API_KEY
  python3 scripts/migrate_to_caricom.py --phase schema     # Create DB + collections
  python3 scripts/migrate_to_caricom.py --phase clean       # Clean wiki slugs
  python3 scripts/migrate_to_caricom.py --phase seed        # Seed entities
  python3 scripts/migrate_to_caricom.py --phase all         # Run all phases
"""

import argparse
import glob
import hashlib
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# ── Config ──
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
PEOPLE_DIR = DATA_DIR / "people"

ENDPOINT   = os.environ.get("VITE_APPWRITE_ENDPOINT", "https://fra.cloud.appwrite.io/v1")
PROJECT_ID = os.environ.get("VITE_APPWRITE_PROJECT_ID", "66509ba7003618a05af6")
DATABASE_ID = os.environ.get("VITE_APPWRITE_DATABASE_ID", "annals_world_db")
API_KEY    = os.environ.get("APPWRITE_API_KEY", "")

RETRY_LIMIT = 3
RETRY_DELAY = 1.0
BATCH_PAUSE = 0.05  # 50ms between documents

# ── Era division mapping (from callNumbers.ts) ──
ERA_DIVISIONS = [
    ("910", "Prehistoric",              None,   -3000),
    ("911", "Paleolithic & Mesolithic",  None,   -10000),
    ("912", "Neolithic & Chalcolithic", -10000,  -3300),
    ("913", "Bronze Age",              -3300,   -1200),
    ("920", "Classical",               -3000,    500),
    ("921", "Archaic Period",           -800,   -480),
    ("922", "Hellenistic Period",       -323,    -31),
    ("923", "Roman Period",              -31,    476),
    ("924", "Late Antiquity",            250,    600),
    ("930", "Medieval",                  500,   1500),
    ("931", "Early Medieval / Dark Ages", 500,    1000),
    ("932", "High Medieval",            1000,   1300),
    ("933", "Late Medieval",            1300,   1500),
    ("940", "Early Modern",             1500,   1800),
    ("941", "Age of Exploration",       1400,   1600),
    ("942", "Renaissance Period",       1300,   1600),
    ("943", "Reformation Era",          1517,   1648),
    ("944", "Age of Enlightenment",     1685,   1815),
    ("950", "Modern",                   1800,   1945),
    ("951", "Industrial Age",           1760,   1840),
    ("952", "Age of Empire / New Imperialism", 1870, 1914),
    ("953", "Interwar Period",          1918,   1939),
    ("954", "World War II Era",         1939,   1945),
    ("960", "Contemporary",             1945,   None),
    ("961", "Cold War Era",             1947,   1991),
    ("962", "Post-Cold War & Globalization", 1991, 2001),
    ("963", "Digital Age",              2001,   None),
]

BROAD_ERA_SLUGS = {
    "Prehistoric": "prehistoric",
    "Classical": "classical",
    "Medieval": "medieval",
    "Early Modern": "early-modern",
    "Modern": "modern",
    "Contemporary": "contemporary",
}

# Sub-division slugs: heading → slug
def heading_to_slug(heading: str) -> str:
    s = heading.lower()
    s = re.sub(r"[/&]", "-", s)
    s = re.sub(r"[^a-z0-9-]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return f"era-{s}"


# ── HTTP helper ──
def api_call(method: str, path: str, body: dict | None = None, attempt: int = 1) -> dict | None:
    """Make authenticated Appwrite REST API call."""
    url = f"{ENDPOINT}{path}"
    data = json.dumps(body, ensure_ascii=False).encode("utf-8") if body else None

    req = urllib.request.Request(url, data=data, method=method, headers={
        "Content-Type": "application/json",
        "X-Appwrite-Project": PROJECT_ID,
        "X-Appwrite-Key": API_KEY,
    })

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body_text = e.read().decode("utf-8", errors="replace") if e.fp else ""
        if e.code == 409:
            return {"_exists": True}
        if e.code == 429:
            retry_after = int(e.headers.get("Retry-After", "5"))
            print(f"  Rate limited, waiting {retry_after}s...")
            time.sleep(retry_after)
            if attempt < RETRY_LIMIT:
                return api_call(method, path, json.loads(data.decode()) if data else None, attempt + 1)
        if attempt < RETRY_LIMIT:
            time.sleep(RETRY_DELAY * attempt)
            return api_call(method, path, json.loads(data.decode()) if data else None, attempt + 1)
        print(f"  ERROR {e.code}: {body_text[:200]}")
        return None
    except Exception as ex:
        if attempt < RETRY_LIMIT:
            time.sleep(RETRY_DELAY * attempt)
            return api_call(method, path, json.loads(data.decode()) if data else None, attempt + 1)
        print(f"  EXCEPTION: {ex}")
        return None


# =============================================================================
# PHASE 1: Schema Migration — Create DB + Collections
# =============================================================================

def phase_schema():
    """Create annals_world_db database and all collections with attributes."""
    print("\n" + "=" * 60)
    print("PHASE 1: Schema Migration")
    print("=" * 60)

    # Create database
    print(f"\nCreating database: {DATABASE_ID}")
    result = api_call("POST", "/databases", {
        "databaseId": DATABASE_ID,
        "name": "Annals of the World",
    })
    if result and result.get("_exists"):
        print("  Database already exists ✓")
    elif result:
        print(f"  Database created ✓ — {result.get('$id')}")
    else:
        print("  ERROR creating database!")
        return False

    # Collection definitions with attributes
    collections = {
        "entities": {
            "name": "Entities",
            "attributes": [
                ("string", "slug",           255,  True),
                ("string", "name",           500,  True),
                ("string", "label",          50,   True),
                ("string", "callNumber",     255,  True),
                ("string", "summary",        100000, False),
                ("string", "era",            50,   False),
                ("string", "eraSlug",        100,  False),
                ("string", "eraDivision",    100,  False),   # NEW: specific era sub-division
                ("string", "eraDivisionCode", 10,  False),   # NEW: e.g. "944"
                ("string", "region",         100,  False),
                ("string", "continent",      50,   False),
                ("string", "status",         30,   False),
                ("string", "born",           100,  False),
                ("string", "died",           100,  False),
                ("string", "founded",        100,  False),
                ("string", "period",         200,  False),
                ("string", "startDate",      100,  False),
                ("string", "endDate",        100,  False),
                ("string", "wikidataQid",    50,   False),
                ("string", "wikipediaUrl",   500,  False),
                ("string", "imageUrl",       1000, False),
                ("integer", "importanceScore", None, False),
                ("string", "detailsJson",    1000000, False),
            ],
            "array_attributes": [
                ("string", "subjectHeadings", 500, False),
                ("string", "subjects",       100, False),
                ("string", "frameworks",     100, False),
                ("string", "altNames",       200, False),
            ],
            "indexes": [
                ("slug_idx",     "unique",  ["slug"]),
                ("era_idx",      "key",     ["eraSlug"]),
                ("label_idx",    "key",     ["label"]),
                ("continent_idx", "key",    ["continent"]),
                ("name_search",  "fulltext", ["name"]),
                ("callnumber_idx", "key",   ["callNumber"]),
                ("eraDivisionCode_idx", "key", ["eraDivisionCode"]),
            ],
        },
        "relationships": {
            "name": "Relationships",
            "attributes": [
                ("string", "entitySlug",  255, True),
                ("string", "sourceSlug",  255, True),
                ("string", "sourceName",  500, False),
                ("string", "verb",        100, True),
                ("string", "targetSlug",  255, True),
                ("string", "targetName",  500, False),
                ("string", "context",     2000, False),
            ],
            "array_attributes": [],
            "indexes": [
                ("entity_idx",  "key", ["entitySlug"]),
                ("source_idx",  "key", ["sourceSlug"]),
                ("target_idx",  "key", ["targetSlug"]),
                ("verb_idx",    "key", ["verb"]),
            ],
        },
        "causes_effects": {
            "name": "Causes & Effects",
            "attributes": [
                ("string", "entitySlug", 255, True),
                ("string", "type",       20,  True),   # "cause" or "effect"
                ("string", "title",      500, True),
                ("string", "category",   50,  False),  # EventWindow, Idea, etc.
                ("string", "year",       50,  False),
            ],
            "array_attributes": [],
            "indexes": [
                ("entity_idx", "key", ["entitySlug"]),
                ("type_idx",   "key", ["type"]),
            ],
        },
        "places": {
            "name": "Places",
            "attributes": [
                ("string", "entitySlug", 255, True),
                ("string", "name",       300, True),
                ("string", "role",       100, False),
                ("string", "slug",       255, False),
            ],
            "array_attributes": [],
            "indexes": [
                ("entity_idx", "key", ["entitySlug"]),
            ],
        },
        "texts": {
            "name": "Texts",
            "attributes": [
                ("string", "entitySlug", 255, True),
                ("string", "title",      500, True),
                ("string", "type",       100, False),
                ("string", "slug",       255, False),
            ],
            "array_attributes": [],
            "indexes": [
                ("entity_idx", "key", ["entitySlug"]),
            ],
        },
        "evidence": {
            "name": "Evidence",
            "attributes": [
                ("string", "entitySlug", 255, True),
                ("string", "title",      500, True),
                ("string", "author",     300, False),
                ("integer", "year",      None, False),
                ("string", "doiOrUrl",   500, False),
                ("string", "tier",       10,  True),
                ("string", "citation",   2000, True),
                ("string", "sourceNote", 1000, False),
            ],
            "array_attributes": [],
            "indexes": [
                ("entity_idx", "key", ["entitySlug"]),
                ("tier_idx",   "key", ["tier"]),
            ],
        },
        "media": {
            "name": "Media",
            "attributes": [
                ("string", "entitySlug", 255, True),
                ("string", "fileId",     100, False),
                ("string", "url",        500, True),
                ("string", "alt",        500, True),
                ("string", "credit",     300, False),
                ("string", "category",   50,  True),
                ("string", "caption",    1000, False),
            ],
            "array_attributes": [],
            "indexes": [
                ("entity_idx", "key", ["entitySlug"]),
            ],
        },
        "timeline_entries": {
            "name": "Timeline Entries",
            "attributes": [
                ("string", "entitySlug",   255, True),
                ("integer", "year",        None, True),
                ("integer", "endYear",     None, False),
                ("string", "title",        500, True),
                ("string", "description",  2000, True),
                ("string", "significance", 20,  True),
            ],
            "array_attributes": [],
            "indexes": [
                ("entity_idx", "key", ["entitySlug"]),
                ("year_idx",   "key", ["year"]),
            ],
        },
    }

    for coll_id, spec in collections.items():
        print(f"\n  Creating collection: {coll_id} ({spec['name']})")
        result = api_call("POST", f"/databases/{DATABASE_ID}/collections", {
            "collectionId": coll_id,
            "name": spec["name"],
            "permissions": [
                'read("any")',         # Public read for the frontend
                'create("users")',
                'update("users")',
            ],
            "documentSecurity": False,
        })
        if result and result.get("_exists"):
            print(f"    Collection already exists ✓")
        elif result:
            print(f"    Created ✓")
        else:
            print(f"    ERROR creating collection!")
            continue

        # Create attributes
        for attr_spec in spec["attributes"]:
            attr_type = attr_spec[0]
            attr_key = attr_spec[1]

            if attr_type == "string":
                _, key, size, required = attr_spec
                body = {"key": key, "size": size, "required": required}
                path = f"/databases/{DATABASE_ID}/collections/{coll_id}/attributes/string"
            elif attr_type == "integer":
                _, key, _, required = attr_spec
                body = {"key": key, "required": required}
                path = f"/databases/{DATABASE_ID}/collections/{coll_id}/attributes/integer"
            else:
                continue

            r = api_call("POST", path, body)
            status = "✓" if r else "✗"
            exists = " (exists)" if r and r.get("_exists") else ""
            print(f"    attr {key}: {status}{exists}")
            time.sleep(0.3)  # Appwrite needs time between attribute creation

        # Create array attributes
        for arr_spec in spec.get("array_attributes", []):
            _, key, size, required = arr_spec
            body = {"key": key, "size": size, "required": required}
            path = f"/databases/{DATABASE_ID}/collections/{coll_id}/attributes/string"
            # Array attribute: use list=True
            body["array"] = True
            r = api_call("POST", path, body)
            status = "✓" if r else "✗"
            exists = " (exists)" if r and r.get("_exists") else ""
            print(f"    arr  {key}: {status}{exists}")
            time.sleep(0.3)

        # Wait for attributes to be available before creating indexes
        print(f"    Waiting for attributes to be available...")
        time.sleep(3)

        # Create indexes
        for idx_name, idx_type, idx_attrs in spec.get("indexes", []):
            body = {
                "key": idx_name,
                "type": idx_type,
                "attributes": idx_attrs,
            }
            r = api_call("POST", f"/databases/{DATABASE_ID}/collections/{coll_id}/indexes", body)
            status = "✓" if r else "✗"
            exists = " (exists)" if r and r.get("_exists") else ""
            print(f"    idx  {idx_name}: {status}{exists}")
            time.sleep(0.5)

    print("\n✅ Schema migration complete")
    return True


# =============================================================================
# PHASE 2: Clean wikipedia- slugs + duplicate detection
# =============================================================================

def clean_slug(slug: str) -> str:
    """Fix wikipedia- prefixed slugs and other known bad patterns."""
    # Remove wikipedia- prefix
    if slug.startswith("wikipedia-"):
        slug = slug[len("wikipedia-"):]
    # Remove wiki- prefix
    if slug.startswith("wiki-"):
        slug = slug[len("wiki-"):]
    # Fix em-dashes and en-dashes
    slug = slug.replace("–", "-").replace("—", "-")
    # Remove trailing dots
    slug = slug.rstrip(".")
    # Collapse multiple hyphens
    slug = re.sub(r"-+", "-", slug)
    return slug


def phase_clean():
    """Clean wikipedia- slugs and duplicates across all JSON files."""
    print("\n" + "=" * 60)
    print("PHASE 2: Clean Slugs & Deduplicate")
    print("=" * 60)

    json_files = sorted(glob.glob(str(DATA_DIR / "wikidata_*.json")))
    json_files += sorted(glob.glob(str(PEOPLE_DIR / "wikidata_people_*.json")))

    total_cleaned = 0
    total_wiki_slugs_fixed = 0
    total_text_slugs_fixed = 0
    all_slugs: dict[str, str] = {}  # slug → file for dedup tracking
    duplicates_removed = 0

    for filepath in json_files:
        path = Path(filepath)
        print(f"\n  Processing: {path.name}")

        with open(path, encoding="utf-8") as f:
            data = json.load(f)

        entities = data.get("entities", [])
        slug_set = set()
        cleaned_entities = []
        file_wiki_fixed = 0
        file_text_fixed = 0

        for entity in entities:
            old_slug = entity.get("slug", "")
            new_slug = clean_slug(old_slug)

            # Fix entity slug
            if new_slug != old_slug:
                entity["slug"] = new_slug
                file_wiki_fixed += 1
                # Also update callNumber if it contains old slug
                cn = entity.get("callNumber", "")
                if old_slug in cn:
                    entity["callNumber"] = cn.replace(old_slug, new_slug)

            # Fix slugs in relationships
            for rel in entity.get("relationships", []):
                for key in ("sourceSlug", "targetSlug"):
                    old = rel.get(key, "")
                    fixed = clean_slug(old)
                    if fixed != old:
                        rel[key] = fixed

                # Update sourceName/targetName refs if slug was the entity
                if rel.get("sourceSlug") == new_slug and rel.get("sourceName") != entity.get("name"):
                    rel["sourceName"] = entity.get("name", "")

            # Fix wikipedia- slugs in texts[] array
            for text in entity.get("texts", []):
                old_ts = text.get("slug", "")
                if old_ts.startswith("wikipedia-") or old_ts.startswith("wiki-"):
                    # Remove the wikipedia slug entirely — it's a reference link, not an entity
                    text["slug"] = clean_slug(old_ts)
                    file_text_fixed += 1

            # Deduplication by slug
            if new_slug in slug_set:
                duplicates_removed += 1
                continue
            slug_set.add(new_slug)

            # Cross-file dedup tracking
            if new_slug in all_slugs:
                # Skip duplicate — keep first occurrence
                duplicates_removed += 1
                continue
            all_slugs[new_slug] = path.name

            cleaned_entities.append(entity)

        data["entities"] = cleaned_entities
        # Update metadata count (handle both _meta and metadata keys)
        meta_key = "_meta" if "_meta" in data else "metadata" if "metadata" in data else None
        if meta_key:
            data[meta_key]["entityCount"] = len(cleaned_entities)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        total_wiki_slugs_fixed += file_wiki_fixed
        total_text_slugs_fixed += file_text_fixed
        total_cleaned += len(cleaned_entities)
        print(f"    Entities: {len(cleaned_entities)} | Slug fixes: {file_wiki_fixed} | Text fixes: {file_text_fixed}")

    print(f"\n  Total entities: {total_cleaned:,}")
    print(f"  Wiki slug fixes: {total_wiki_slugs_fixed:,}")
    print(f"  Text slug fixes: {total_text_slugs_fixed:,}")
    print(f"  Duplicates removed: {duplicates_removed:,}")
    print("✅ Slug cleanup complete")
    return total_cleaned


# =============================================================================
# PHASE 3: Seed entities to Appwrite
# =============================================================================

def get_era_division(entity: dict) -> tuple[str, str]:
    """Determine the specific era sub-division for an entity from its OCCURS_DURING relationship."""
    # First check existing relationships for OCCURS_DURING
    for rel in entity.get("relationships", []):
        if rel.get("verb") == "OCCURS_DURING":
            target = rel.get("targetSlug", "")
            target_name = rel.get("targetName", "")
            if target.startswith("era-"):
                # Look up the code from target
                for code, heading, _, _ in ERA_DIVISIONS:
                    if heading_to_slug(heading) == target:
                        return code, heading
            # Broad era match
            broad_era = entity.get("era", "")
            for code, heading, _, _ in ERA_DIVISIONS:
                if heading == broad_era:
                    return code, heading

    # Fallback: use broad era
    broad_era = entity.get("era", "")
    for code, heading, _, _ in ERA_DIVISIONS:
        slug = BROAD_ERA_SLUGS.get(heading)
        if slug and slug == entity.get("eraSlug"):
            return code, heading

    return "", ""


def to_doc_id(slug: str) -> str:
    """Generate deterministic document ID from slug (max 36 chars, Appwrite limit).
    Uses SHA-256 suffix for collision avoidance on non-ASCII or long slugs.
    """
    clean = re.sub(r"[^a-zA-Z0-9_-]", "_", slug)
    safe = re.sub(r"^[_-]+", "", clean)
    # If the slug is pure ASCII-safe and fits → use it directly (no hash needed)
    if slug == safe and 0 < len(safe) <= 36:
        return safe
    # Otherwise, use prefix + SHA-256 hash suffix for uniqueness
    sha = hashlib.sha256(slug.encode("utf-8")).hexdigest()[:12]
    prefix = re.sub(r"[_-]+$", "", safe[:23])
    doc_id = f"{prefix}_{sha}" if prefix else sha
    return doc_id[:36]


def truncate(s: str | None, max_len: int) -> str:
    if not s:
        return ""
    return s[:max_len - 3] + "..." if len(s) > max_len else s


def entity_to_document(entity: dict) -> dict:
    """Transform entity to Appwrite document shape."""
    e = entity
    era_code, era_heading = get_era_division(e)

    details = {
        "causes": e.get("causes", []),
        "effects": e.get("effects", []),
        "relationships": e.get("relationships", []),
        "places": e.get("places", []),
        "texts": e.get("texts", []),
        "externalLinks": e.get("externalLinks", []),
        "tags": e.get("tags", []),
        "thumbnailUrl": e.get("thumbnailUrl", ""),
        "quote": e.get("quote", ""),
        "legacySummary": e.get("legacySummary", ""),
    }
    details_json = json.dumps(details, ensure_ascii=False)

    return {
        "slug": e["slug"][:255],
        "name": truncate(e["name"], 500),
        "label": e.get("label", "Person")[:50],
        "callNumber": e.get("callNumber", "")[:255],
        "summary": truncate(e.get("summary", ""), 100000),
        "era": e.get("era", ""),
        "eraSlug": e.get("eraSlug", ""),
        "eraDivision": era_heading,
        "eraDivisionCode": era_code,
        "region": e.get("region", ""),
        "continent": e.get("continent", ""),
        "status": e.get("status", "Published"),
        "born": truncate(e.get("born") or "", 100) or None,
        "died": truncate(e.get("died") or "", 100) or None,
        "founded": truncate(e.get("founded") or "", 100) or None,
        "period": truncate(e.get("period") or "", 200) or None,
        "startDate": truncate(e.get("startDate") or e.get("born") or "", 100) or None,
        "endDate": truncate(e.get("endDate") or e.get("died") or "", 100) or None,
        "subjectHeadings": e.get("subjectHeadings", []),
        "subjects": e.get("subjects", []),
        "frameworks": e.get("frameworks", []),
        "altNames": e.get("altNames", []),
        "wikidataQid": e.get("wikidataQid") or None,
        "wikipediaUrl": truncate(e.get("wikipediaUrl") or "", 500) or None,
        "imageUrl": truncate(e.get("imageUrl") or e.get("thumbnailUrl") or "", 1000) or None,
        "importanceScore": e.get("importanceScore") or e.get("historicalSignificance", {}).get("score"),
        "detailsJson": truncate(details_json, 1000000),
    }


def phase_seed(skip: int = 0, max_entities: int = 0, batch_size: int = 100, workers: int = 20):
    """Seed all entities from JSON files to Appwrite (concurrent)."""
    print("\n" + "=" * 60)
    print("PHASE 3: Seed Entities to Appwrite")
    print("=" * 60)

    if not API_KEY:
        print("ERROR: APPWRITE_API_KEY not set!")
        return False

    # Gather all JSON files
    json_files = sorted(glob.glob(str(DATA_DIR / "wikidata_*.json")))
    json_files += sorted(glob.glob(str(PEOPLE_DIR / "wikidata_people_*.json")))

    # Load all entities
    all_entities = []
    seen_slugs = set()
    for filepath in json_files:
        path = Path(filepath)
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        for e in data.get("entities", []):
            slug = e.get("slug", "")
            if slug and slug not in seen_slugs:
                seen_slugs.add(slug)
                all_entities.append(e)

    print(f"  Total unique entities: {len(all_entities):,}")

    if skip:
        all_entities = all_entities[skip:]
        print(f"  After skip {skip}: {len(all_entities):,}")
    if max_entities:
        all_entities = all_entities[:max_entities]
        print(f"  Capped at {max_entities}: {len(all_entities):,}")

    created = 0
    exists = 0
    failed = 0
    total_done = 0
    start_time = time.time()

    def seed_one(entity):
        slug = entity["slug"]
        doc_id = to_doc_id(slug)
        doc_data = entity_to_document(entity)
        result = api_call("POST",
            f"/databases/{DATABASE_ID}/collections/entities/documents",
            {"documentId": doc_id, "data": doc_data})
        if result is None:
            return "failed"
        elif result.get("_exists"):
            return "exists"
        else:
            return "created"

    print(f"  Using {workers} concurrent workers")

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(seed_one, e): e for e in all_entities}
        for future in as_completed(futures):
            result = future.result()
            if result == "created":
                created += 1
            elif result == "exists":
                exists += 1
            else:
                failed += 1

            total_done += 1
            if total_done % 2000 == 0 or total_done == len(all_entities):
                elapsed = time.time() - start_time
                rate = total_done / elapsed if elapsed > 0 else 0
                print(f"  [{total_done:>7,}/{len(all_entities):,}] "
                      f"created={created:,} exists={exists:,} failed={failed:,} "
                      f"({rate:.0f}/s)")

    elapsed = time.time() - start_time
    print(f"\n  ✅ Seeding complete in {elapsed:.0f}s")
    print(f"  Created: {created:,}")
    print(f"  Existed: {exists:,}")
    print(f"  Failed:  {failed:,}")
    return True


# =============================================================================
# Main
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="Migrate Annals to CARICOM Appwrite")
    parser.add_argument("--phase", choices=["schema", "clean", "seed", "all"],
                        default="all", help="Which phase to run")
    parser.add_argument("--skip", type=int, default=0, help="Skip first N entities (seed)")
    parser.add_argument("--max", type=int, default=0, help="Max entities to seed (0=all)")
    parser.add_argument("--batch-size", type=int, default=100)
    parser.add_argument("--workers", type=int, default=20, help="Concurrent workers (seed)")
    args = parser.parse_args()

    if args.phase in ("schema", "all"):
        if not API_KEY:
            print("ERROR: Set APPWRITE_API_KEY environment variable")
            sys.exit(1)
        if not phase_schema():
            sys.exit(1)

    if args.phase in ("clean", "all"):
        phase_clean()

    if args.phase in ("seed", "all"):
        if not API_KEY:
            print("ERROR: Set APPWRITE_API_KEY environment variable")
            sys.exit(1)
        phase_seed(skip=args.skip, max_entities=args.max, batch_size=args.batch_size, workers=args.workers)


if __name__ == "__main__":
    main()
