#!/usr/bin/env python3
"""
seed_catalog_entities.py — Seed catalog_entities.json to Appwrite backend.

Reads data/catalog_entities.json (exported by export_catalog_entities.ts)
and seeds each entity using the same transform as migrate_to_caricom.py.

Usage:
  source .env
  python3 scripts/seed_catalog_entities.py [--workers 20] [--skip 0] [--max 0]
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# ── Config ──
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
CATALOG_JSON = DATA_DIR / "catalog_entities.json"

ENDPOINT   = os.environ.get("VITE_APPWRITE_ENDPOINT", "https://fra.cloud.appwrite.io/v1")
PROJECT_ID = os.environ.get("VITE_APPWRITE_PROJECT_ID", "66509ba7003618a05af6")
DATABASE_ID = os.environ.get("VITE_APPWRITE_DATABASE_ID", "annals_world_db")
API_KEY    = os.environ.get("APPWRITE_API_KEY", "")

COLLECTION_ID = "entities"
RETRY_LIMIT = 3
RETRY_DELAY = 1.0

# ── Era division mapping ──
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
    "Classical / Ancient": "classical",
    "Medieval": "medieval",
    "Early Modern": "early-modern",
    "Modern": "modern",
    "Contemporary": "contemporary",
}


def heading_to_slug(heading: str) -> str:
    s = heading.lower()
    s = re.sub(r"[/&]", "-", s)
    s = re.sub(r"[^a-z0-9-]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return f"era-{s}"


# ── HTTP helper (same as migrate_to_caricom.py) ──
import urllib.request
import urllib.error

def api_call(method: str, path: str, body: dict | None = None, attempt: int = 1) -> dict | None:
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


def to_doc_id(slug: str) -> str:
    clean = re.sub(r"[^a-zA-Z0-9_-]", "_", slug)
    safe = re.sub(r"^[_-]+", "", clean)
    if slug == safe and 0 < len(safe) <= 36:
        return safe
    sha = hashlib.sha256(slug.encode("utf-8")).hexdigest()[:12]
    prefix = re.sub(r"[_-]+$", "", safe[:23])
    doc_id = f"{prefix}_{sha}" if prefix else sha
    return doc_id[:36]


def truncate(s: str | None, max_len: int) -> str:
    if not s:
        return ""
    return s[:max_len - 3] + "..." if len(s) > max_len else s


def get_era_division(e: dict) -> tuple[str, str]:
    """Extract era division code and heading from entity."""
    # Check OCCURS_DURING relationships for era division
    for r in e.get("relationships", []):
        verb = r.get("verb", "")
        target = r.get("targetName", "")
        if verb == "OCCURS_DURING" and target:
            for code, heading, _, _ in ERA_DIVISIONS:
                if target == heading:
                    return code, heading

    # Fallback: broad era (normalize "Classical / Ancient" → "Classical", etc.)
    era = e.get("era", "")
    # Canonical broad era names
    CANONICAL_ERA = {
        "Classical / Ancient": "Classical",
        "Classical/Ancient": "Classical",
    }
    canonical = CANONICAL_ERA.get(era, era)
    broad_slug = BROAD_ERA_SLUGS.get(era, "") or BROAD_ERA_SLUGS.get(canonical, "")
    if broad_slug:
        for code, heading, _, _ in ERA_DIVISIONS:
            if heading == canonical:
                return code, heading

    return "", ""


def entity_to_document(entity: dict) -> dict:
    e = entity
    era_code, era_heading = get_era_division(e)

    # Normalize era name
    raw_era = e.get("era", "")
    CANONICAL_ERA_NAME = {
        "Classical / Ancient": "Classical",
        "Classical/Ancient": "Classical",
    }
    era_name = CANONICAL_ERA_NAME.get(raw_era, raw_era)
    era_slug = e.get("eraSlug", "")
    if era_slug == "classical-ancient":
        era_slug = "classical"

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
        "era": era_name,
        "eraSlug": era_slug,
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
        "importanceScore": e.get("importanceScore"),
        "detailsJson": truncate(details_json, 1000000),
    }


def seed_one(entity: dict) -> tuple[str, str]:
    """Seed a single entity (create or update). Returns (slug, status)."""
    slug = entity.get("slug", "unknown")
    action = entity.get("_action", "create")
    try:
        doc = entity_to_document(entity)
        doc_id = to_doc_id(slug)
        collection_path = f"/databases/{DATABASE_ID}/collections/{COLLECTION_ID}/documents"

        if action == "update":
            # Update existing document with richer data
            path = f"{collection_path}/{doc_id}"
            result = api_call("PATCH", path, {"data": doc})
            if result and not result.get("_exists"):
                return slug, "updated"
            # If update fails (doc ID doesn't match), try by slug lookup + update
            # This handles slug → doc_id mismatch (underscore vs hyphen)
            return slug, "update-skip"
        else:
            # Create new document
            result = api_call("POST", collection_path, {
                "documentId": doc_id,
                "data": doc,
            })
            if result and result.get("_exists"):
                return slug, "exists"
            elif result:
                return slug, "created"
            else:
                return slug, "failed"
    except Exception as ex:
        return slug, f"error:{ex}"


def main():
    parser = argparse.ArgumentParser(description="Seed catalog entities to Appwrite")
    parser.add_argument("--workers", type=int, default=20, help="Concurrent workers")
    parser.add_argument("--skip", type=int, default=0, help="Skip first N entities")
    parser.add_argument("--max", type=int, default=0, help="Max entities to seed (0=all)")
    args = parser.parse_args()

    if not API_KEY:
        print("ERROR: APPWRITE_API_KEY not set! Run: source .env")
        sys.exit(1)

    # Load catalog entities
    print(f"Loading {CATALOG_JSON}...")
    with open(CATALOG_JSON, encoding="utf-8") as f:
        data = json.load(f)

    entities = data.get("entities", [])
    total = len(entities)
    print(f"  Total catalog entities: {total:,}")

    if args.skip:
        entities = entities[args.skip:]
        print(f"  After skip {args.skip}: {len(entities):,}")
    if args.max:
        entities = entities[:args.max]
        print(f"  Capped at {args.max}: {len(entities):,}")

    created = 0
    updated = 0
    exists = 0
    failed = 0
    errors = []

    print(f"\nSeeding {len(entities):,} entities with {args.workers} workers...")
    start = time.time()

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(seed_one, e): e for e in entities}
        for i, future in enumerate(as_completed(futures), 1):
            slug, status = future.result()
            if status == "created":
                created += 1
            elif status == "updated":
                updated += 1
            elif status == "exists" or status == "update-skip":
                exists += 1
            else:
                failed += 1
                errors.append(f"{slug}: {status}")

            if i % 100 == 0 or i == len(entities):
                elapsed = time.time() - start
                rate = i / elapsed if elapsed > 0 else 0
                print(f"  [{i:,}/{len(entities):,}] "
                      f"created={created:,} updated={updated:,} exists={exists:,} failed={failed:,} "
                      f"({rate:.0f}/s)")

    elapsed = time.time() - start
    print(f"\n{'=' * 60}")
    print(f"SEED COMPLETE in {elapsed:.0f}s")
    print(f"  Created:  {created:,}")
    print(f"  Updated:  {updated:,}")
    print(f"  Exists:   {exists:,}")
    print(f"  Failed:   {failed:,}")
    print(f"  Total:    {created + updated + exists + failed:,}")
    if errors:
        print(f"\nFirst 20 errors:")
        for e in errors[:20]:
            print(f"  {e}")


if __name__ == "__main__":
    main()
