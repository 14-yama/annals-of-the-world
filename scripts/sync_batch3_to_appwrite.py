#!/usr/bin/env python3
"""
Targeted sync: push batch-3 enriched + new entities to Appwrite.
Also syncs classification fixes (moved files with corrected callNumbers).
"""
import json, hashlib, time, urllib.request, urllib.error, glob, os

ENDPOINT = "https://fra.cloud.appwrite.io/v1"
PROJECT  = "66509ba7003618a05af6"
DB       = "annals_world_db"
API_KEY  = "standard_a5dc3fada7d64812f42510400b8dab6d43ee3cca0417d0074cc71fd75ed6ac8db18a1d1e20446aab2e05d5be7d27d1908117fca2c79f3181e34e9f5e3a680e5f399e3e786387e9ccf2234c09ea45ffabad96c817457bf3549059b445433a80783ac03dac408185e8d6ccc46521f0dcae60dd15ffe73eddca9db4001a146ea3fd"
COLLECTION = "entities"
BASE = "data/appwrite-export/entities"

def slug_to_id(slug):
    return hashlib.sha256(slug.encode()).hexdigest()[:20]

def headers():
    return {
        "Content-Type": "application/json",
        "X-Appwrite-Project": PROJECT,
        "X-Appwrite-Key": API_KEY,
    }

def get_doc(doc_id):
    url = f"{ENDPOINT}/databases/{DB}/collections/{COLLECTION}/documents/{doc_id}"
    req = urllib.request.Request(url, headers=headers())
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise

def create_doc(doc_id, data):
    url = f"{ENDPOINT}/databases/{DB}/collections/{COLLECTION}/documents"
    body = json.dumps({"documentId": doc_id, "data": data}).encode()
    req = urllib.request.Request(url, data=body, headers=headers(), method="POST")
    try:
        with urllib.request.urlopen(req) as r:
            return True
    except urllib.error.HTTPError as e:
        err = e.read().decode()
        print(f"    CREATE ERROR: {e.code} {err[:200]}")
        return False

def update_doc(doc_id, data):
    url = f"{ENDPOINT}/databases/{DB}/collections/{COLLECTION}/documents/{doc_id}"
    body = json.dumps({"data": data}).encode()
    req = urllib.request.Request(url, data=body, headers=headers(), method="PATCH")
    try:
        with urllib.request.urlopen(req) as r:
            return True
    except urllib.error.HTTPError as e:
        err = e.read().decode()
        print(f"    UPDATE ERROR: {e.code} {err[:200]}")
        return False

def clean_payload(entity):
    """Remove Appwrite metadata fields from payload."""
    skip = {"$id","$createdAt","$updatedAt","$databaseId","$collectionId","$permissions"}
    payload = {}
    for k, v in entity.items():
        if k in skip:
            continue
        # Stringify detailsJson if dict
        if k == "detailsJson" and isinstance(v, dict):
            payload[k] = json.dumps(v, ensure_ascii=False)
        else:
            payload[k] = v
    return payload

# ─── Target slugs ───

ENRICHED_SLUGS = [
    "pythagoras", "ramesses-ii", "hammurabi", "peter-the-great",
    "suleiman-the-magnificent", "joseph-stalin", "mao-zedong", "voltaire",
    "immanuel-kant", "rumi", "avicenna", "ibn-khaldun", "akbar", "tamerlane",
    "william-the-conqueror", "thomas-aquinas", "al-khwarizmi",
    "henry-viii-of-england", "louis-xiv-of-france", "theodore-roosevelt",
]

NEW_SLUGS = [
    "adolf-hitler", "catherine-the-great", "che-guevara", "elizabeth-i",
    "franklin-d-roosevelt", "nefertiti", "rene-descartes",
    "richard-the-lionheart", "simon-bolivar", "tutankhamun", "kublai-khan",
    "guru-nanak-dev",
]

ALL_SLUGS = set(ENRICHED_SLUGS + NEW_SLUGS)

# ─── Find files ───
slug_to_file = {}
for f in glob.glob(f"{BASE}/**/*.json", recursive=True):
    try:
        with open(f) as fh:
            data = json.load(fh)
        slug = data["entities"][0].get("slug", "")
        if slug in ALL_SLUGS:
            slug_to_file[slug] = f
    except:
        pass

print(f"Found {len(slug_to_file)}/{len(ALL_SLUGS)} target entities in repo\n")

created = 0
updated = 0
failed = 0

for slug in sorted(ALL_SLUGS):
    if slug not in slug_to_file:
        print(f"  SKIP {slug} — not found in repo")
        failed += 1
        continue
    
    with open(slug_to_file[slug]) as fh:
        data = json.load(fh)
    entity = data["entities"][0]
    
    # Use $id if present, else hash
    doc_id = entity.get("$id") or slug_to_id(slug)
    payload = clean_payload(entity)
    
    # Check if exists in Appwrite
    existing = get_doc(doc_id)
    
    if existing:
        ok = update_doc(doc_id, payload)
        if ok:
            updated += 1
            print(f"  UPDATED {slug} ({doc_id[:12]}…)")
        else:
            failed += 1
    else:
        # Also try slug as doc_id (some were created that way)
        existing2 = get_doc(slug) if doc_id != slug else None
        if existing2:
            ok = update_doc(slug, payload)
            if ok:
                updated += 1
                print(f"  UPDATED {slug} (slug-id)")
            else:
                failed += 1
        else:
            ok = create_doc(doc_id, payload)
            if ok:
                created += 1
                print(f"  CREATED {slug} ({doc_id[:12]}…)")
            else:
                failed += 1
    
    time.sleep(0.1)  # rate limit

print(f"\nDone: {created} created, {updated} updated, {failed} failed")
