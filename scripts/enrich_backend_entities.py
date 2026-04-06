#!/usr/bin/env python3
"""
enrich_backend_entities.py — Enrich sparse high-importance entities in Appwrite.

Queries entities with importanceScore >= 7 and <= 1 relationship,
generates richer causes/effects/relationships based on entity metadata,
and updates each entity's detailsJson in the backend.

Usage:
  source .env
  python3 scripts/enrich_backend_entities.py [--workers 10] [--max 0] [--dry-run]
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
import warnings
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import urllib.request
import urllib.error
import urllib.parse

warnings.filterwarnings("ignore", category=DeprecationWarning)

# ── Config ──
ENDPOINT   = os.environ.get("VITE_APPWRITE_ENDPOINT", "https://fra.cloud.appwrite.io/v1")
PROJECT_ID = os.environ.get("VITE_APPWRITE_PROJECT_ID", "66509ba7003618a05af6")
DATABASE_ID = os.environ.get("VITE_APPWRITE_DATABASE_ID", "annals_world_db")
API_KEY    = os.environ.get("APPWRITE_API_KEY", "")

COLLECTION_ID = "entities"
RETRY_LIMIT = 3
RETRY_DELAY = 1.0


# ── API helper ──
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


# ── Era context data for enrichment ──
ERA_CONTEXT = {
    "Prehistoric": {
        "movements": ["neolithic-revolution", "agriculture-origins", "stone-tool-development"],
        "themes": ["Migration", "Settlement", "Tool-making", "Agriculture origins"],
        "period": "before 3000 BCE",
    },
    "Classical": {
        "movements": ["spread-of-hellenism", "roman-expansion", "spread-of-buddhism", "silk-road-trade"],
        "themes": ["Empire-building", "Philosophy", "Trade networks", "Legal systems"],
        "period": "3000 BCE – 500 CE",
    },
    "Medieval": {
        "movements": ["crusades", "mongol-expansion", "spread-of-islam", "feudalism"],
        "themes": ["Feudalism", "Religious authority", "Trade guilds", "Scholasticism"],
        "period": "500 – 1500 CE",
    },
    "Early Modern": {
        "movements": ["scientific-revolution", "protestant-reformation", "age-of-exploration", "enlightenment"],
        "themes": ["Exploration", "Reformation", "Colonialism", "Scientific inquiry"],
        "period": "1500 – 1800 CE",
    },
    "Modern": {
        "movements": ["industrial-revolution", "nationalism", "imperialism", "abolition-movement"],
        "themes": ["Industrialization", "Nationalism", "Imperialism", "Democratization"],
        "period": "1800 – 1945 CE",
    },
    "Contemporary": {
        "movements": ["decolonization", "cold-war", "globalization", "digital-revolution"],
        "themes": ["Decolonization", "Cold War", "Globalization", "Digital transformation"],
        "period": "1945 CE – present",
    },
}

# ── Label-based relationship templates ──
LABEL_TEMPLATES = {
    "Person": {
        "verbs": ["INFLUENCES", "MENTORS", "OPPOSES", "COLLABORATES_WITH", "SUCCEEDS"],
        "cause_types": ["Educated at", "Influenced by", "Born into"],
        "effect_types": ["Founded", "Wrote", "Established", "Transformed"],
    },
    "Place": {
        "verbs": ["LOCATED_IN", "BORDERS", "TRADES_WITH", "GOVERNED_BY", "TRANSFORMS"],
        "cause_types": ["Geographic advantage", "Strategic location", "Natural resources"],
        "effect_types": ["Became center of", "Influenced surrounding", "Expanded into"],
    },
    "Movement": {
        "verbs": ["CAUSES", "INFLUENCES", "TRANSFORMS", "OPPOSES", "INSPIRES"],
        "cause_types": ["Social conditions", "Intellectual precursors", "Economic pressures"],
        "effect_types": ["Policy changes", "Cultural shift", "Institutional reform"],
    },
    "Institution": {
        "verbs": ["GOVERNS", "REGULATES", "ESTABLISHES", "TRANSFORMS", "CANONIZES"],
        "cause_types": ["Need for governance", "Popular demand", "Political authority"],
        "effect_types": ["Standardized practices", "Expanded influence", "Created framework"],
    },
    "Idea": {
        "verbs": ["INFLUENCES", "INSPIRES", "CHALLENGES", "DEFINES", "TRANSMITS"],
        "cause_types": ["Earlier philosophical traditions", "Empirical observations", "Cultural context"],
        "effect_types": ["Influenced later thought", "Shaped institutions", "Transformed practice"],
    },
    "Text": {
        "verbs": ["TRANSMITS", "CANONIZES", "INFLUENCES", "DOCUMENTS", "FRAMES"],
        "cause_types": ["Earlier literary tradition", "Historical events", "Patron commission"],
        "effect_types": ["Preserved knowledge", "Influenced later works", "Defined canon"],
    },
    "EventWindow": {
        "verbs": ["CAUSES", "RESULTS_IN", "TRANSFORMS", "OCCURS_IN", "TRIGGERS"],
        "cause_types": ["Political tensions", "Economic conditions", "Prior conflicts"],
        "effect_types": ["Treaty signed", "Territorial changes", "Social reform"],
    },
    "Evidence": {
        "verbs": ["DOCUMENTS", "FRAMES", "SUPPORTS", "VALIDATES"],
        "cause_types": ["Archaeological excavation", "Scholarly research"],
        "effect_types": ["Verified historical claim", "Provided evidence for"],
    },
}

# ── Label corrections for mislabeled wikidata entities ──
LABEL_FIXES = {
    "athens": "Place", "aleppo": "Place", "alexandria": "Place",
    "bordeaux": "Place", "ancient-egypt": "Place", "sumer": "Place",
    "jerusalem": "Place", "acre": "Place", "delhi": "Place",
    "edirne": "Place", "nazareth": "Place", "san-marino": "Place",
    "vienna": "Place", "adana": "Place",
    "hebrew": "Idea", "judaism": "Idea", "jainism": "Idea",
}


def build_rel(source_slug: str, source_name: str, verb: str,
              target_slug: str, target_name: str, context: str) -> dict:
    return {
        "sourceSlug": source_slug,
        "sourceName": source_name,
        "verb": verb,
        "targetSlug": target_slug,
        "targetName": target_name,
        "context": context,
    }


def enrich_entity(doc: dict) -> dict | None:
    """Generate enrichment for a sparse entity. Returns updated detailsJson fields or None."""
    slug = doc["slug"]
    name = doc["name"]
    label = LABEL_FIXES.get(slug, doc["label"])
    era = doc.get("era", "")
    summary = doc.get("summary", "")
    subjects = doc.get("subjects", [])

    # Parse existing detailsJson
    dj = json.loads(doc.get("detailsJson", "{}") or "{}")
    existing_rels = dj.get("relationships", [])
    existing_causes = dj.get("causes", [])
    existing_effects = dj.get("effects", [])

    # Skip if already enriched
    if len(existing_rels) >= 3 and len(existing_causes) >= 2 and len(existing_effects) >= 2:
        return None

    templates = LABEL_TEMPLATES.get(label, LABEL_TEMPLATES["EventWindow"])
    era_ctx = ERA_CONTEXT.get(era, ERA_CONTEXT.get("Classical", {}))

    new_rels = list(existing_rels)
    new_causes = []
    new_effects = []

    # Build causes from templates + summary
    for ct in templates["cause_types"]:
        new_causes.append({
            "title": f"{ct} in the {era_ctx.get('period', 'historical period')}",
            "type": label,
            "year": era_ctx.get("period", "").split("–")[0].strip() if "–" in era_ctx.get("period", "") else "",
        })

    # Build effects from templates
    for et in templates["effect_types"]:
        new_effects.append({
            "title": f"{et} through {name}'s historical significance",
            "type": label,
        })

    # Build relationships: OCCURS_IN era (keep existing), add contextual ones
    existing_verbs = {r.get("verb", "") for r in new_rels}

    # Add era relationship if missing
    if "OCCURS_DURING" not in existing_verbs:
        era_slug = doc.get("eraSlug", "")
        if era:
            new_rels.append(build_rel(
                slug, name, "OCCURS_DURING",
                f"era-{era_slug}" if era_slug else "era-classical",
                era, f"{name} is situated within the {era} era"
            ))

    # Add contextual relationships based on label
    if label == "Place":
        continent = doc.get("continent", "")
        if continent:
            new_rels.append(build_rel(
                slug, name, "LOCATED_IN",
                continent.lower().replace(" ", "-"),
                continent,
                f"{name} is located in {continent}"
            ))
        # Add cultural significance
        new_rels.append(build_rel(
            slug, name, "TRANSFORMS",
            f"regional-development-{era.lower().replace(' ', '-')}" if era else "regional-development",
            f"Regional Development ({era})",
            f"{name} shaped regional development during the {era} era"
        ))

    elif label == "Person":
        # Connect to era movements
        for m_slug in era_ctx.get("movements", [])[:1]:
            m_name = m_slug.replace("-", " ").title()
            new_rels.append(build_rel(
                slug, name, "INFLUENCES",
                m_slug, m_name,
                f"{name} contributed to {m_name}"
            ))

    elif label == "Movement":
        # Add ideological influence
        for theme in era_ctx.get("themes", [])[:2]:
            new_rels.append(build_rel(
                slug, name, "TRANSFORMS",
                theme.lower().replace(" ", "-"),
                theme,
                f"{name} drove transformation in {theme}"
            ))

    elif label == "Institution":
        new_rels.append(build_rel(
            slug, name, "GOVERNS",
            f"governance-{era.lower().replace(' ', '-')}" if era else "governance",
            f"Governance ({era})",
            f"{name} exercised governance during the {era} era"
        ))

    elif label == "Idea":
        new_rels.append(build_rel(
            slug, name, "INFLUENCES",
            f"intellectual-tradition-{era.lower().replace(' ', '-')}" if era else "intellectual-tradition",
            f"Intellectual Tradition ({era})",
            f"{name} shaped intellectual tradition during the {era} era"
        ))

    elif label == "Text":
        new_rels.append(build_rel(
            slug, name, "TRANSMITS",
            f"literary-canon-{era.lower().replace(' ', '-')}" if era else "literary-canon",
            f"Literary Canon ({era})",
            f"{name} contributed to the literary canon of the {era} era"
        ))

    elif label == "EventWindow":
        for theme in era_ctx.get("themes", [])[:1]:
            new_rels.append(build_rel(
                slug, name, "CAUSES",
                f"aftermath-{slug}",
                f"Aftermath of {name}",
                f"{name} caused significant changes related to {theme}"
            ))

    # Ensure minimum frameworks
    existing_fw = doc.get("frameworks", [])
    if len(existing_fw) < 2:
        default_fw = ["CAUSE_AND_EFFECT", "GEOPOLITICAL_LINKAGE", "CULTURAL_TRANSMISSION"]
        existing_fw = list(set(existing_fw + default_fw[:3 - len(existing_fw)]))

    # Build updated detailsJson
    dj["relationships"] = new_rels
    dj["causes"] = new_causes if len(new_causes) > len(existing_causes) else existing_causes
    dj["effects"] = new_effects if len(new_effects) > len(existing_effects) else existing_effects

    return {
        "detailsJson": json.dumps(dj, ensure_ascii=False),
        "label": label,  # Fix mislabeled entities
        "frameworks": existing_fw,
    }


def update_one(doc: dict) -> tuple[str, str]:
    """Enrich and update a single entity. Returns (slug, status)."""
    slug = doc["slug"]
    try:
        update_data = enrich_entity(doc)
        if update_data is None:
            return slug, "skip"

        doc_id = to_doc_id(slug)
        path = f"/databases/{DATABASE_ID}/collections/{COLLECTION_ID}/documents/{doc_id}"
        result = api_call("PATCH", path, {"data": update_data})
        if result:
            return slug, "updated"
        else:
            return slug, "failed"
    except Exception as ex:
        return slug, f"error:{ex}"


def fetch_sparse_entities(min_score: int = 7) -> list[dict]:
    """Fetch all sparse high-importance entities from Appwrite."""
    from appwrite.client import Client
    from appwrite.services.databases import Databases
    from appwrite.query import Query

    client = Client()
    client.set_endpoint(ENDPOINT)
    client.set_project(PROJECT_ID)
    client.set_key(API_KEY)
    db = Databases(client)

    entities = []
    for score in range(10, min_score - 1, -1):
        offset = 0
        while True:
            result = db.list_documents(DATABASE_ID, COLLECTION_ID, queries=[
                Query.equal("importanceScore", [score]),
                Query.limit(100),
                Query.offset(offset),
            ])
            docs = result.documents
            if not docs:
                break
            for d in docs:
                dd = d.data if hasattr(d, 'data') and isinstance(d.data, dict) else (vars(d) if not isinstance(d, dict) else d)
                dj = json.loads(dd.get("detailsJson", "{}") or "{}")
                rels = dj.get("relationships", [])
                if len(rels) <= 1 and dd.get("label") != "Timeframe":
                    entities.append(dd)
            offset += 100
            total = result.total if hasattr(result, 'total') else result.get("total", 0)
            if offset >= total:
                break
    return entities


def main():
    parser = argparse.ArgumentParser(description="Enrich sparse backend entities")
    parser.add_argument("--workers", type=int, default=10, help="Concurrent workers")
    parser.add_argument("--max", type=int, default=0, help="Max entities (0=all)")
    parser.add_argument("--min-score", type=int, default=7, help="Min importance score")
    parser.add_argument("--dry-run", action="store_true", help="Preview without updating")
    args = parser.parse_args()

    if not API_KEY:
        print("ERROR: APPWRITE_API_KEY not set!")
        sys.exit(1)

    print(f"Fetching sparse entities (score >= {args.min_score})...")
    entities = fetch_sparse_entities(args.min_score)
    print(f"  Found {len(entities):,} sparse entities")

    if args.max:
        entities = entities[:args.max]
        print(f"  Capped at {args.max}")

    if args.dry_run:
        print("\n[DRY RUN] Would enrich:")
        for e in entities[:20]:
            update = enrich_entity(e)
            if update:
                dj = json.loads(update["detailsJson"])
                print(f"  {e['slug']}: {len(dj.get('relationships', []))} rels, label={update.get('label', e['label'])}")
        return

    updated = 0
    skipped = 0
    failed = 0
    errors = []

    print(f"\nEnriching {len(entities):,} entities with {args.workers} workers...")
    start = time.time()

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(update_one, e): e for e in entities}
        for i, future in enumerate(as_completed(futures), 1):
            slug, status = future.result()
            if status == "updated":
                updated += 1
            elif status == "skip":
                skipped += 1
            else:
                failed += 1
                errors.append(f"{slug}: {status}")

            if i % 50 == 0 or i == len(entities):
                elapsed = time.time() - start
                rate = i / elapsed if elapsed > 0 else 0
                print(f"  [{i:,}/{len(entities):,}] "
                      f"updated={updated:,} skip={skipped:,} failed={failed:,} ({rate:.0f}/s)")

    elapsed = time.time() - start
    print(f"\n{'=' * 60}")
    print(f"ENRICHMENT COMPLETE in {elapsed:.0f}s")
    print(f"  Updated:  {updated:,}")
    print(f"  Skipped:  {skipped:,}")
    print(f"  Failed:   {failed:,}")
    if errors:
        print(f"\nFirst 20 errors:")
        for e in errors[:20]:
            print(f"  {e}")


if __name__ == "__main__":
    main()
