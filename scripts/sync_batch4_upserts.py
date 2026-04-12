#!/usr/bin/env python3
"""
Re-upsert all batch 4 enriched + new entities to Appwrite.
Fixes entities that were accidentally deleted by the deletion sync.
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
        if e.code in (400, 404): return None
        raise

def create_doc(doc_id, data):
    url = f"{ENDPOINT}/databases/{DB}/collections/{COLLECTION}/documents"
    body = json.dumps({"documentId": doc_id, "data": data}).encode()
    req = urllib.request.Request(url, data=body, headers=headers(), method="POST")
    try:
        with urllib.request.urlopen(req) as r: return True
    except urllib.error.HTTPError as e:
        err = e.read().decode()
        print(f"    CREATE ERROR: {e.code} {err[:200]}")
        return False

def update_doc(doc_id, data):
    url = f"{ENDPOINT}/databases/{DB}/collections/{COLLECTION}/documents/{doc_id}"
    body = json.dumps({"data": data}).encode()
    req = urllib.request.Request(url, data=body, headers=headers(), method="PATCH")
    try:
        with urllib.request.urlopen(req) as r: return True
    except urllib.error.HTTPError as e:
        err = e.read().decode()
        print(f"    UPDATE ERROR: {e.code} {err[:200]}")
        return False

def entity_to_appwrite(e):
    dj = e.get("detailsJson", {})
    if isinstance(dj, dict):
        dj = json.dumps(dj, ensure_ascii=False)
    return {
        "slug": e["slug"],
        "name": e["name"],
        "label": e.get("label", ""),
        "callNumber": e.get("callNumber", ""),
        "era": e.get("era", ""),
        "summary": e.get("summary", ""),
        "continent": e.get("continent", ""),
        "region": e.get("region", ""),
        "subjects": e.get("subjects", []),
        "subjectHeadings": e.get("subjectHeadings", []),
        "detailsJson": dj,
    }

# All entities that need to be in Appwrite from batch 4
upsert_slugs = [
    # 26 enriched
    "alan-turing", "ada-lovelace", "archimedes", "marie-curie", "otto-von-bismarck",
    "vladimir-lenin", "neil-armstrong", "rembrandt", "thomas-hobbes",
    "jean-jacques-rousseau", "michelangelo", "leo-tolstoy", "deng-xiaoping",
    "vasco-da-gama", "james-cook", "roald-amundsen", "zheng-he", "francis-bacon",
    "erasmus", "john-calvin", "florence-nightingale", "thomas-edison", "wright-brothers",
    "frederick-douglass", "ibn-battuta", "tim-berners-lee",
    # 5 new + 2 reclassified
    "dante-alighieri", "fyodor-dostoevsky", "rosa-parks", "queen-elizabeth-ii",
    "pope-john-paul-ii", "artaxiad-dynasty-of-armenia", "bani-yas-island",
]

# Build slug→file index (only scan once)
print("Building file index...")
slug_to_file = {}
for f in glob.glob(f"{BASE}/**/*.json", recursive=True):
    try:
        with open(f) as fh:
            d = json.load(fh)
        e = d["entities"][0]
        norm_slug = e["slug"].replace("_", "-")
        slug_to_file[norm_slug] = f
    except:
        pass
print(f"Indexed {len(slug_to_file)} entities")

ok = 0
fail = 0

for slug in upsert_slugs:
    f = slug_to_file.get(slug)
    if not f:
        print(f"  NOT FOUND: {slug}")
        fail += 1
        continue

    with open(f) as fh:
        d = json.load(fh)
    e = d["entities"][0]
    data = entity_to_appwrite(e)
    doc_id = slug_to_id(e["slug"])

    # Check if exists (try hash then slug)
    existing = get_doc(doc_id)
    if existing is None:
        existing = get_doc(e["slug"])
        if existing:
            doc_id = e["slug"]

    if existing:
        if update_doc(doc_id, data):
            print(f"  UPD {slug}")
            ok += 1
        else:
            fail += 1
    else:
        if create_doc(doc_id, data):
            print(f"  NEW {slug}")
            ok += 1
        else:
            fail += 1
    time.sleep(0.15)

print(f"\n=== UPSERT COMPLETE: {ok} ok, {fail} failed ===")
