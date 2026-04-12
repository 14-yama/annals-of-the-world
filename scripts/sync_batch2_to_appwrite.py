#!/usr/bin/env python3
"""Sync enriched and new entities to Appwrite."""
import json, os, sys, time
try:
    import requests
except ImportError:
    print("Installing requests...")
    os.system(f"{sys.executable} -m pip install requests -q")
    import requests

ENDPOINT = "https://fra.cloud.appwrite.io/v1"
PROJECT_ID = "66509ba7003618a05af6"
API_KEY = "standard_a5dc3fada7d64812f42510400b8dab6d43ee3cca0417d0074cc71fd75ed6ac8db18a1d1e20446aab2e05d5be7d27d1908117fca2c79f3181e34e9f5e3a680e5f399e3e786387e9ccf2234c09ea45ffabad96c817457bf3549059b445433a80783ac03dac408185e8d6ccc46521f0dcae60dd15ffe73eddca9db4001a146ea3fd"
DATABASE_ID = "annals_world_db"
COLLECTION_ID = "entities"

HEADERS = {
    "Content-Type": "application/json",
    "X-Appwrite-Project": PROJECT_ID,
    "X-Appwrite-Key": API_KEY,
}

# All files to sync
FILES = {
    # 29 paragraph-reformatted entities
    "jesus-christ": "data/appwrite-export/entities/201-Class-201/201jesus-christ.json",
    "muhammad": "data/appwrite-export/entities/251-Class-251/251muhammad.json",
    "julius-caesar": "data/appwrite-export/entities/221-Class-221/221julius-caesar.json",
    "aristotle": "data/appwrite-export/entities/210-Class-210/21004-aristotle.json",
    "plato": "data/appwrite-export/entities/210-Class-210/21003-plato.json",
    "socrates": "data/appwrite-export/entities/210-Class-210/21002-socrates.json",
    "augustus": "data/appwrite-export/entities/221-Class-221/221augustus.json",
    "cleopatra": "data/appwrite-export/entities/221-Class-221/221cleopatra.json",
    "genghis-khan": "data/appwrite-export/entities/280-Class-280/280genghis-khan.json",
    "martin-luther": "data/appwrite-export/entities/201-Class-201/201martin-luther.json",
    "galileo-galilei": "data/appwrite-export/entities/201-Class-201/201galileo-galilei.json",
    "albert-einstein": "data/appwrite-export/entities/240-Class-240/240albert-einstein.json",
    "ashoka": "data/appwrite-export/entities/221-Class-221/221ashoka.json",
    "nelson-mandela": "data/appwrite-export/entities/222-Class-222/222nelson-mandela.json",
    "nikola-tesla": "data/appwrite-export/entities/240-Class-240/240nikola-tesla.json",
    "winston-churchill": "data/appwrite-export/entities/222-Class-222/222winston-churchill.json",
    "abraham-lincoln": "data/appwrite-export/entities/222-Class-222/222abraham-lincoln.json",
    "george-washington": "data/appwrite-export/entities/222-Class-222/222george-washington.json",
    "charlemagne": "data/appwrite-export/entities/221-Class-221/221charlemagne.json",
    "saladin": "data/appwrite-export/entities/221-Class-221/221saladin.json",
    "mahatma-gandhi": "data/appwrite-export/entities/205-Class-205/205mahatma-gandhi.json",
    "martin-luther-king-jr": "data/appwrite-export/entities/204-Class-204/204martin-luther-king-jr.json",
    "zoroaster": "data/appwrite-export/entities/262-Class-262/262zoroaster.json",
    "abraham": "data/appwrite-export/entities/251-Class-251/251abraham.json",
    "homer": "data/appwrite-export/entities/260-Class-260/26001-homer.json",
    "cyrus-the-great": "data/appwrite-export/entities/251-Class-251/251cyrus-the-great.json",
    "moses": "data/appwrite-export/entities/251-Class-251/251moses.json",
    "buddha": "data/appwrite-export/entities/251-Class-251/251buddha.json",
    "confucius": "data/appwrite-export/entities/210-Class-210/21005-confucius.json",
    # 15 newly enriched entities
    "alexander-the-great": "data/appwrite-export/entities/221-Class-221/221alexander-the-great.json",
    "isaac-newton": "data/appwrite-export/entities/210-Class-210/210isaac-newton.json",
    "napoleon-italy": "data/appwrite-export/entities/220-Class-220/220napoleon-italy.json",
    "joan-of-arc": "data/appwrite-export/entities/204-Class-204/204joan-of-arc.json",
    "christopher-columbus": "data/appwrite-export/entities/240-Class-240/240christopher-columbus.json",
    "karl-marx": "data/appwrite-export/entities/202-Class-202/202karl-marx.json",
    "thomas-jefferson": "data/appwrite-export/entities/201-Class-201/201thomas-jefferson.json",
    "paul-the-apostle": "data/appwrite-export/entities/252-Class-252/252paul-the-apostle.json",
    "david": "data/appwrite-export/entities/762-Class-762/762david.json",
    "solomon": "data/appwrite-export/entities/221-Class-221/221solomon.json",
    "hannibal": "data/appwrite-export/entities/280-Class-280/280hannibal.json",
    "sun-tzu": "data/appwrite-export/entities/210-Class-210/210sun-tzu.json",
    "william-shakespeare": "data/appwrite-export/entities/262-Class-262/262william-shakespeare.json",
    "marco-polo": "data/appwrite-export/entities/202-Class-202/202marco-polo.json",
    "herodotus": "data/appwrite-export/entities/205-Class-205/205herodotus.json",
    # 6 brand new entities
    "constantine-i": "data/appwrite-export/entities/221-Class-221/221constantine-i.json",
    "attila": "data/appwrite-export/entities/280-Class-280/280attila.json",
    "copernicus": "data/appwrite-export/entities/210-Class-210/210copernicus.json",
    "machiavelli": "data/appwrite-export/entities/205-Class-205/205machiavelli.json",
    "queen-victoria": "data/appwrite-export/entities/222-Class-222/222queen-victoria.json",
    "sigmund-freud": "data/appwrite-export/entities/210-Class-210/210sigmund-freud.json",
}

# Fields to update in Appwrite
SYNC_FIELDS = [
    "slug", "name", "label", "callNumber", "summary", "era", "eraSlug",
    "region", "continent", "status", "period", "wikidataQid", "wikipediaUrl",
    "detailsJson", "subjectHeadings", "subjects", "frameworks", "altNames",
    "importanceScore",
]

def find_by_slug(slug):
    """Find entity by slug in Appwrite."""
    url = f"{ENDPOINT}/databases/{DATABASE_ID}/collections/{COLLECTION_ID}/documents"
    params = {"queries[]": [f'equal("slug", ["{slug}"])']}
    r = requests.get(url, headers=HEADERS, params=params)
    if r.status_code == 200:
        docs = r.json().get("documents", [])
        return docs[0] if docs else None
    return None

def update_doc(doc_id, data):
    """Update existing document."""
    url = f"{ENDPOINT}/databases/{DATABASE_ID}/collections/{COLLECTION_ID}/documents/{doc_id}"
    r = requests.patch(url, headers=HEADERS, json={"data": data})
    return r.status_code, r.text

def create_doc(doc_id, data):
    """Create new document."""
    url = f"{ENDPOINT}/databases/{DATABASE_ID}/collections/{COLLECTION_ID}/documents"
    r = requests.post(url, headers=HEADERS, json={"documentId": doc_id, "data": data})
    return r.status_code, r.text


ok = 0
fail = 0
created = 0

for slug, path in FILES.items():
    with open(path) as f:
        data = json.load(f)
    entity = data["entities"][0]

    payload = {}
    for field in SYNC_FIELDS:
        if field in entity and entity[field] is not None:
            payload[field] = entity[field]

    # Find in Appwrite
    doc = find_by_slug(slug)

    if doc:
        status, resp = update_doc(doc["$id"], payload)
        if status == 200:
            ok += 1
            print(f"  UPDATE {slug:30s} | {status}")
        else:
            fail += 1
            print(f"  FAIL   {slug:30s} | {status} | {resp[:120]}")
    else:
        # Create new document
        doc_id = f"enriched_{slug.replace('-', '_')}"
        status, resp = create_doc(doc_id, payload)
        if status in (200, 201):
            ok += 1
            created += 1
            print(f"  CREATE {slug:30s} | {status}")
        else:
            fail += 1
            print(f"  FAIL   {slug:30s} | {status} | {resp[:120]}")

    time.sleep(0.15)  # Rate limiting

print(f"\nDone: {ok} ok ({created} new), {fail} failed, {ok + fail} total")
