#!/usr/bin/env python3
"""
Batch 5: Normalize all underscore slugs to kebab-case.
- Scans all entity JSON files
- Converts underscores → hyphens in slug field
- Updates callNumber, detailsJson relationship slugs, and filename
- Syncs changes to Appwrite (delete old doc, create with new slug)
"""
import json, glob, os, re, hashlib, time, shutil, urllib.request, urllib.error

ENDPOINT = "https://fra.cloud.appwrite.io/v1"
PROJECT  = "66509ba7003618a05af6"
DB       = "annals_world_db"
API_KEY  = "standard_a5dc3fada7d64812f42510400b8dab6d43ee3cca0417d0074cc71fd75ed6ac8db18a1d1e20446aab2e05d5be7d27d1908117fca2c79f3181e34e9f5e3a680e5f399e3e786387e9ccf2234c09ea45ffabad96c817457bf3549059b445433a80783ac03dac408185e8d6ccc46521f0dcae60dd15ffe73eddca9db4001a146ea3fd"
COLLECTION = "entities"
BASE = "data/appwrite-export/entities"

DRY_RUN = False  # Set True to preview without writing
SYNC_APPWRITE = True  # Set False to skip Appwrite sync

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
    except urllib.error.HTTPError:
        return None

def delete_doc(doc_id):
    url = f"{ENDPOINT}/databases/{DB}/collections/{COLLECTION}/documents/{doc_id}"
    req = urllib.request.Request(url, headers=headers(), method="DELETE")
    try:
        with urllib.request.urlopen(req) as r: return True
    except urllib.error.HTTPError:
        return False

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

def normalize_slug(slug):
    """Convert underscore slug to kebab-case per slug_naming_convention.md"""
    s = slug.lower().strip()
    s = re.sub(r'[_\s]+', '-', s)      # underscore/space → hyphen
    s = re.sub(r'-+', '-', s)           # collapse multiple hyphens
    s = s.strip('-')
    return s

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

# ═══ PHASE 1: Scan for underscore slugs ═══
print("=== PHASE 1: Scanning for underscore slugs ===")

files = glob.glob(f"{BASE}/**/*.json", recursive=True)
print(f"Total files: {len(files)}")

# First pass: build slug→file index to check for conflicts
all_slugs = set()
underscore_files = []

for f in files:
    try:
        with open(f) as fh:
            d = json.load(fh)
        e = d["entities"][0]
        slug = e["slug"]
        all_slugs.add(slug)
        if "_" in slug:
            new_slug = normalize_slug(slug)
            underscore_files.append((f, d, slug, new_slug))
    except Exception as ex:
        pass

print(f"Found {len(underscore_files)} entities with underscore slugs")

# Check for conflicts (new slug already exists as a different entity)
conflicts = []
safe_to_fix = []
for f, d, old_slug, new_slug in underscore_files:
    if new_slug in all_slugs and new_slug != old_slug:
        # Conflict: the hyphenated version already exists
        conflicts.append((old_slug, new_slug))
    else:
        safe_to_fix.append((f, d, old_slug, new_slug))

print(f"Safe to fix: {len(safe_to_fix)}")
print(f"Conflicts (hyphen version exists): {len(conflicts)}")

if conflicts:
    print("\nConflicts (will be DELETED as duplicates):")
    for old, new in conflicts[:20]:
        print(f"  {old} → {new} (already exists)")
    if len(conflicts) > 20:
        print(f"  ... and {len(conflicts) - 20} more")

# ═══ PHASE 2: Fix local JSON files ═══
print("\n=== PHASE 2: Fixing local JSON files ===")

fixed = 0
deleted_conflicts = 0

# Fix safe renames
for f, d, old_slug, new_slug in safe_to_fix:
    e = d["entities"][0]

    # Update slug
    e["slug"] = new_slug

    # Update callNumber if it contains the old slug
    if "callNumber" in e and old_slug in (e.get("callNumber") or ""):
        e["callNumber"] = e["callNumber"].replace(old_slug, new_slug)

    # Update detailsJson relationship slugs
    dj = e.get("detailsJson", "")
    if isinstance(dj, str) and dj:
        try:
            details = json.loads(dj)
        except json.JSONDecodeError:
            details = {}
    elif isinstance(dj, dict):
        details = dj
    else:
        details = {}

    if details:
        # Fix sourceSlug/targetSlug in relationships
        for rel in details.get("relationships", []):
            if rel.get("sourceSlug") == old_slug:
                rel["sourceSlug"] = new_slug
            if rel.get("targetSlug") == old_slug:
                rel["targetSlug"] = new_slug
        e["detailsJson"] = json.dumps(details, ensure_ascii=False)

    # Update _meta divisionCode
    if "_meta" in d:
        dc = d["_meta"].get("divisionCode", "")
        if old_slug in dc:
            d["_meta"]["divisionCode"] = dc.replace(old_slug, new_slug)

    # Update $id if it matches old slug
    if e.get("$id") == old_slug:
        e["$id"] = new_slug

    if not DRY_RUN:
        # Write updated content
        with open(f, "w") as fh:
            json.dump(d, fh, indent=2, ensure_ascii=False)
            fh.write("\n")

        # Rename file if filename contains old slug
        dirname = os.path.dirname(f)
        basename = os.path.basename(f)
        if old_slug in basename:
            new_basename = basename.replace(old_slug, new_slug)
            new_path = os.path.join(dirname, new_basename)
            if f != new_path and not os.path.exists(new_path):
                os.rename(f, new_path)

    fixed += 1
    if fixed <= 10:
        print(f"  FIX {old_slug} → {new_slug}")
    elif fixed == 11:
        print(f"  ... fixing remaining {len(safe_to_fix) - 10} silently ...")

# Delete conflict files (underscore version is a duplicate of existing hyphen version)
for old_slug, new_slug in conflicts:
    for f, d, s, ns in underscore_files:
        if s == old_slug:
            if not DRY_RUN:
                os.remove(f)
            deleted_conflicts += 1
            break

print(f"\nFixed: {fixed} slugs normalized")
print(f"Deleted: {deleted_conflicts} conflict duplicates")

# ═══ PHASE 3: Sync to Appwrite ═══
if SYNC_APPWRITE and not DRY_RUN:
    print("\n=== PHASE 3: Syncing to Appwrite ===")

    # Delete old underscore docs from Appwrite
    appwrite_deleted = 0
    appwrite_created = 0
    appwrite_failed = 0

    # Process safe renames: delete old, create/update new
    for i, (f, d, old_slug, new_slug) in enumerate(safe_to_fix):
        # Delete old document (try slug as ID, then hash)
        for old_id in [old_slug, slug_to_id(old_slug)]:
            if get_doc(old_id):
                delete_doc(old_id)
                appwrite_deleted += 1
                break

        # Re-read the fixed file to get updated content
        # Find the renamed file
        dirname = os.path.dirname(f)
        basename = os.path.basename(f)
        if old_slug in basename:
            new_basename = basename.replace(old_slug, new_slug)
            actual_path = os.path.join(dirname, new_basename)
        else:
            actual_path = f

        if os.path.exists(actual_path):
            with open(actual_path) as fh:
                updated = json.load(fh)
            e = updated["entities"][0]
            data = entity_to_appwrite(e)
            new_id = slug_to_id(new_slug)

            # Check if new slug doc already exists
            existing = get_doc(new_id) or get_doc(new_slug)
            if existing:
                doc_id = new_id if get_doc(new_id) else new_slug
                if update_doc(doc_id, data):
                    appwrite_created += 1
                else:
                    appwrite_failed += 1
            else:
                if create_doc(new_id, data):
                    appwrite_created += 1
                else:
                    appwrite_failed += 1

        if (i + 1) % 50 == 0:
            print(f"  Progress: {i+1}/{len(safe_to_fix)}")
        time.sleep(0.1)  # Rate limit

    # Delete conflict duplicates from Appwrite too
    for old_slug, new_slug in conflicts:
        for old_id in [old_slug, slug_to_id(old_slug)]:
            if get_doc(old_id):
                delete_doc(old_id)
                appwrite_deleted += 1
                break
        time.sleep(0.1)

    print(f"\nAppwrite: {appwrite_deleted} deleted, {appwrite_created} created/updated, {appwrite_failed} failed")

# ═══ SUMMARY ═══
remaining = len(glob.glob(f"{BASE}/**/*.json", recursive=True))
print(f"\n=== BATCH 5 COMPLETE ===")
print(f"Slugs normalized: {fixed}")
print(f"Conflict duplicates removed: {deleted_conflicts}")
print(f"Remaining entity files: {remaining}")
