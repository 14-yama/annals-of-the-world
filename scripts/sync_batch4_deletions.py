#!/usr/bin/env python3
"""
Complete sync: delete ALL remaining duplicates from Appwrite.
Reads deleted files from git diff output.
"""
import json, hashlib, time, urllib.request, urllib.error, subprocess, os, re

ENDPOINT = "https://fra.cloud.appwrite.io/v1"
PROJECT  = "66509ba7003618a05af6"
DB       = "annals_world_db"
API_KEY  = "standard_a5dc3fada7d64812f42510400b8dab6d43ee3cca0417d0074cc71fd75ed6ac8db18a1d1e20446aab2e05d5be7d27d1908117fca2c79f3181e34e9f5e3a680e5f399e3e786387e9ccf2234c09ea45ffabad96c817457bf3549059b445433a80783ac03dac408185e8d6ccc46521f0dcae60dd15ffe73eddca9db4001a146ea3fd"
COLLECTION = "entities"

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

def delete_doc(doc_id):
    url = f"{ENDPOINT}/databases/{DB}/collections/{COLLECTION}/documents/{doc_id}"
    req = urllib.request.Request(url, headers=headers(), method="DELETE")
    try:
        with urllib.request.urlopen(req) as r: return True
    except urllib.error.HTTPError as e:
        if e.code == 404: return None  # Already gone
        err = e.read().decode()
        print(f"    DELETE ERROR: {e.code} {err[:200]}")
        return False

# Get all deleted files from git diff
result = subprocess.run(
    ["git", "diff", "--name-only", "--diff-filter=D", "--", "data/appwrite-export/entities/"],
    capture_output=True, text=True
)

deleted_files = [l.strip() for l in result.stdout.strip().split("\n") if l.strip()]
print(f"Found {len(deleted_files)} deleted entity files")

# Extract slugs from filenames
# Format: data/appwrite-export/entities/XXX-Class-XXX/XXXslug.json
# Slug is filename minus the leading class digits
slugs_to_delete = []
for f in deleted_files:
    basename = os.path.basename(f).replace(".json", "")
    # Remove leading digits (class number prefix)
    slug = re.sub(r"^\d+", "", basename).lstrip("-")
    if slug:
        slugs_to_delete.append(slug)

print(f"Extracted {len(slugs_to_delete)} slugs to delete")

del_ok = 0
del_skip = 0
del_fail = 0

for slug in slugs_to_delete:
    # Try slug as document ID first, then hash
    doc_id_hash = slug_to_id(slug)
    found = False
    for did in [slug, doc_id_hash]:
        existing = get_doc(did)
        if existing:
            result = delete_doc(did)
            if result:
                print(f"  DEL {slug} (id={did})")
                del_ok += 1
            elif result is None:
                del_skip += 1
            else:
                del_fail += 1
            found = True
            break
        time.sleep(0.05)
    if not found:
        # Try with underscores too (some docs might use underscore variant)
        uscore = slug.replace("-", "_")
        for did in [uscore, slug_to_id(uscore)]:
            existing = get_doc(did)
            if existing:
                result = delete_doc(did)
                if result:
                    print(f"  DEL {slug} as {did}")
                    del_ok += 1
                elif result is None:
                    del_skip += 1
                else:
                    del_fail += 1
                found = True
                break
            time.sleep(0.05)
    if not found:
        del_skip += 1
        # Not necessarily an error — the first sync may have already deleted it
    time.sleep(0.1)

print(f"\n=== DELETION COMPLETE ===")
print(f"Deleted: {del_ok}, Already gone: {del_skip}, Failed: {del_fail}")
