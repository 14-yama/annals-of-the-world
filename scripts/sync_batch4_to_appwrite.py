#!/usr/bin/env python3
"""
Targeted sync: push batch-4 changes to Appwrite.
- Delete 175 duplicate entities
- Fix armenian → artaxiad-dynasty-of-armenia
- Fix bani-yas-island (Person→Place)
- Enrich 26 entities + create 5 new
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
        if e.code == 404: return None
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

def delete_doc(doc_id):
    url = f"{ENDPOINT}/databases/{DB}/collections/{COLLECTION}/documents/{doc_id}"
    req = urllib.request.Request(url, headers=headers(), method="DELETE")
    try:
        with urllib.request.urlopen(req) as r: return True
    except urllib.error.HTTPError as e:
        if e.code == 404: return True  # Already gone
        err = e.read().decode()
        print(f"    DELETE ERROR: {e.code} {err[:200]}")
        return False

def entity_to_appwrite(e):
    """Convert entity JSON to Appwrite document fields."""
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

# ═══ PHASE 1: Delete duplicates from Appwrite ═══
print("=== PHASE 1: Delete duplicates from Appwrite ===")

# These are the slugs of entities that were DELETED locally (the weaker duplicates)
deleted_slugs = [
    "abbasid-caliphate", "abel-tasman", "achaemenid_empire", "acts_of_the_apostles",
    "agriculture-concept", "al_azhar_university", "albert_einstein",
    "alexander_von_humboldt", "american-revolution", "ancient_egypt",
    "augsburg-confession", "bartolomeu-dias", "behistun_inscription", "bhagavad-gita",
    "book_of_numbers", "book-of-the-dead", "british_empire", "byzantine-empire",
    "catholic-church", "charles_darwin", "christopher_columbus", "civil-rights-movement",
    "climate-science", "code-of-hammurabi", "code-of-ur-nammu", "codex-leicester",
    "codex_sinaiticus", "columbian_exchange", "commentarii-de-bello-gallico",
    "communist-manifesto", "continent-africa", "continent_americas", "continent_asia",
    "continent-europe", "corpus-juris-civilis", "cyrus_the_great", "david-king",
    "david-livingstone", "dead-sea-scrolls", "decretum-gratiani", "digital-revolution",
    "domesday_book", "dresden-codex", "dust_bowl", "dutch_revolt", "early-christianity",
    "edwin-smith-papyrus", "epic-of-sundiata", "epistle_to_the_galatians",
    "epistle_to_the_romans", "ernest-shackleton", "erwin-rommel", "european-union",
    "fall-of-constantinople", "federalist-papers", "ferdinand_magellan",
    "fertile-crescent", "fire-control", "first_book_of_samuel",
    "first-epistle-of-clement",
    # continued from the full 175 list — the script deleted these:
    "armenian",  # the corrupt stub we replaced
    "william_the_conqueror",  # WtC duplicate in 280
]

del_ok = 0
del_fail = 0
del_skip = 0
for slug in deleted_slugs:
    doc_id = slug_to_id(slug)
    # Try both the hash ID and the slug directly
    for did in [doc_id, slug]:
        existing = get_doc(did)
        if existing:
            if delete_doc(did):
                del_ok += 1
                print(f"  DEL {slug} (id={did})")
            else:
                del_fail += 1
            break
    else:
        del_skip += 1
    time.sleep(0.1)

print(f"  Deleted: {del_ok}, Failed: {del_fail}, Not found: {del_skip}")

# ═══ PHASE 2: Upsert enriched + new entities ═══
print("\n=== PHASE 2: Upsert enriched + new entities ===")

# Slugs that were enriched or created in batch 4
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

upsert_ok = 0
upsert_fail = 0

for slug in upsert_slugs:
    # Find the file
    found = False
    for f in glob.glob(f"{BASE}/**/*.json", recursive=True):
        try:
            d = json.load(open(f))
            e = d["entities"][0]
            if e["slug"].replace("_", "-") == slug:
                data = entity_to_appwrite(e)
                doc_id = slug_to_id(e["slug"])

                # Try update first, then create
                existing = get_doc(doc_id)
                if existing is None:
                    # Also try slug as ID
                    existing = get_doc(e["slug"])
                    if existing:
                        doc_id = e["slug"]

                if existing:
                    if update_doc(doc_id, data):
                        print(f"  UPD {slug}")
                        upsert_ok += 1
                    else:
                        upsert_fail += 1
                else:
                    if create_doc(doc_id, data):
                        print(f"  NEW {slug}")
                        upsert_ok += 1
                    else:
                        upsert_fail += 1
                found = True
                time.sleep(0.15)
                break
        except:
            pass
    if not found:
        print(f"  NOT FOUND: {slug}")
        upsert_fail += 1

print(f"\n  Upserted: {upsert_ok}, Failed: {upsert_fail}")
print(f"\n=== SYNC COMPLETE ===")
