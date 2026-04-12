#!/usr/bin/env python3
"""
Deduplicate entities: when the same entity exists with _ and - variants (or same
name in different divisions), keep the richer one and delete the weaker one.
Also fixes specific misclassifications: armenian, bani-yas-island, william_the_conqueror.
"""
import json, glob, os, shutil
from collections import defaultdict

BASE = "data/appwrite-export/entities"

def normalize(slug):
    return slug.lower().replace('_', '-').replace('--', '-').strip('-')

def richness_score(entity):
    """Score how enriched an entity is. Higher = keep."""
    s = len(entity.get("summary", ""))
    dj = entity.get("detailsJson", {})
    if isinstance(dj, str):
        try: dj = json.loads(dj)
        except: dj = {}
    rels = len(dj.get("relationships", [])) if isinstance(dj, dict) else 0
    causes = len(dj.get("causes", [])) if isinstance(dj, dict) else 0
    effects = len(dj.get("effects", [])) if isinstance(dj, dict) else 0
    para = entity.get("summary", "").count("\n\n")
    return s + (rels * 100) + (causes * 50) + (effects * 50) + (para * 200)

def safe_load(filepath):
    """Load JSON, skipping corrupt files."""
    try:
        with open(filepath) as f:
            return json.load(f)
    except (json.JSONDecodeError, UnicodeDecodeError, KeyError):
        return None

# ─── Phase 1: Specific fixes ───
print("=== PHASE 1: Specific fixes ===")
fixes_done = 0

# Fix 1: "armenian" in 221 — corrupt stub, not a person
armenian_file = f"{BASE}/221-Class-221/221armenian.json"
if os.path.exists(armenian_file):
    os.remove(armenian_file)
    new_entity = {
        "_meta": {"classCode": "523", "divisionCode": "523artaxiad-dynasty-of-armenia", "count": 1},
        "entities": [{
            "slug": "artaxiad-dynasty-of-armenia",
            "name": "Artaxiad Dynasty of Armenia",
            "label": "EventWindow",
            "callNumber": "523.artaxiad-dynasty-of-armenia",
            "era": "Classical",
            "summary": "The Artaxiad Dynasty (189 BCE\u201312 CE) ruled the Kingdom of Armenia at the height of its power. Under Tigranes the Great (95\u201355 BCE), Armenia became the largest state in the eastern Mediterranean, stretching from the Caspian Sea to the Mediterranean.\n\nTigranes was crowned 'King of Kings' and built the capital Tigranocerta (c. 83 BCE), but his empire collapsed after defeats by Roman generals Lucullus and Pompey (69\u201366 BCE). Armenia became a buffer state between Rome and Parthia.\n\nThe dynasty's legacy shaped Armenian national identity and its claim to historic territory.",
            "continent": "Asia", "region": "West Asia",
            "subjects": ["Armenia", "Classical History", "Tigranes the Great", "Artaxiad Dynasty", "West Asia"],
            "subjectHeadings": ["Events \u2014 Artaxiad Dynasty \u2014 Armenia \u2014 Classical"],
            "detailsJson": {
                "causes": ["Seleucid Empire decline after Treaty of Apamea", "Armenian independence movements under Artaxias I", "Tigranes' military genius and alliance with Mithridates VI"],
                "effects": ["Largest Armenian state in history stretching three seas", "Roman-Armenian rivalry lasting centuries", "Armenia became Rome-Parthia buffer state", "Foundation of Armenian national identity"],
                "relationships": [
                    {"sourceSlug": "artaxiad-dynasty-of-armenia", "sourceName": "Artaxiad Dynasty of Armenia", "verb": "OCCURS_IN", "targetSlug": "armenia", "targetName": "Armenia", "context": "The dynasty ruled Armenia for two centuries"},
                    {"sourceSlug": "artaxiad-dynasty-of-armenia", "sourceName": "Artaxiad Dynasty of Armenia", "verb": "INFLUENCES", "targetSlug": "roman-republic", "targetName": "Roman Republic", "context": "Roman campaigns under Lucullus and Pompey ended Armenian expansion"}
                ]
            }
        }]
    }
    new_dir = f"{BASE}/523-Class-523"
    os.makedirs(new_dir, exist_ok=True)
    with open(f"{new_dir}/523artaxiad-dynasty-of-armenia.json", 'w') as f:
        json.dump(new_entity, f, indent=2, ensure_ascii=False)
    print(f"  FIXED armenian \u2192 artaxiad-dynasty-of-armenia (221\u2192523, corrupt Person\u2192EventWindow)")
    fixes_done += 1

# Fix 2: bani-yas-island in 220 Person → should be Place 462
bani_file = f"{BASE}/220-Class-220/220bani-yas-island.json"
if os.path.exists(bani_file):
    d = safe_load(bani_file)
    if d and "entities" in d:
        e = d["entities"][0]
        e["label"] = "Place"
        e["callNumber"] = "462.bani-yas-island"
        d["entities"][0] = e
        d["_meta"]["classCode"] = "462"
        d["_meta"]["divisionCode"] = "462bani-yas-island"
        new_dir = f"{BASE}/462-Class-462"
        os.makedirs(new_dir, exist_ok=True)
        with open(f"{new_dir}/462bani-yas-island.json", 'w') as f:
            json.dump(d, f, indent=2, ensure_ascii=False)
        os.remove(bani_file)
        print(f"  FIXED bani-yas-island (220 Person \u2192 462 Place)")
        fixes_done += 1
    else:
        # Corrupt — just delete and create fresh
        os.remove(bani_file)
        new_entity = {
            "_meta": {"classCode": "462", "divisionCode": "462bani-yas-island", "count": 1},
            "entities": [{
                "slug": "bani-yas-island",
                "name": "Bani Yas Island",
                "label": "Place",
                "callNumber": "462.bani-yas-island",
                "era": "Classical",
                "summary": "Bani Yas Island is a natural island off the coast of Abu Dhabi in the Persian Gulf, historically significant as a strategic settlement and trading post. Archaeological evidence dates habitation to the late Stone Age.\n\nThe island served as a base for the Bani Yas tribal confederation, one of the most powerful groups in the lower Gulf region, from which Abu Dhabi's ruling Al Nahyan family descends.\n\nToday it is a nature reserve and luxury tourism destination, preserving both wildlife and archaeological heritage.",
                "continent": "Asia", "region": "West Asia",
                "subjects": ["Abu Dhabi", "Persian Gulf", "Bani Yas", "UAE", "Archaeology"],
                "subjectHeadings": ["Places \u2014 Bani Yas Island \u2014 UAE \u2014 Classical"],
                "detailsJson": {"causes": ["Strategic Persian Gulf position", "Freshwater availability on island"],
                               "effects": ["Base for Bani Yas confederation", "Origin of Al Nahyan dynasty"],
                               "relationships": []}
            }]
        }
        new_dir = f"{BASE}/462-Class-462"
        os.makedirs(new_dir, exist_ok=True)
        with open(f"{new_dir}/462bani-yas-island.json", 'w') as f:
            json.dump(new_entity, f, indent=2, ensure_ascii=False)
        print(f"  FIXED bani-yas-island (220 Person \u2192 462 Place, recreated)")
        fixes_done += 1

print(f"  Specific fixes: {fixes_done}")

# ─── Phase 2: Deduplicate normalized slugs ───
print("\n=== PHASE 2: Deduplicate normalized slugs ===")

norm_map = defaultdict(list)
corrupt_count = 0
for f in glob.glob(f"{BASE}/**/*.json", recursive=True):
    d = safe_load(f)
    if not d or "entities" not in d or not d["entities"]:
        corrupt_count += 1
        continue
    e = d["entities"][0]
    slug = e.get("slug", "")
    norm = normalize(slug)
    score = richness_score(e)
    norm_map[norm].append((slug, score, e.get("label",""), e.get("callNumber",""), f))

if corrupt_count:
    print(f"  Skipped {corrupt_count} corrupt/unreadable files")

dups = {n: entries for n, entries in norm_map.items() if len(entries) > 1}
print(f"  Found {len(dups)} normalized duplicate groups")

deleted = 0
kept = 0
delete_log = []

for norm, entries in sorted(dups.items()):
    entries.sort(key=lambda x: x[1], reverse=True)
    winner = entries[0]
    losers = entries[1:]
    for loser_slug, loser_score, loser_label, loser_call, loser_file in losers:
        if os.path.exists(loser_file):
            os.remove(loser_file)
            deleted += 1
            delete_log.append(f"  DEL {loser_slug:50s} ({loser_score:5d}pts) {loser_call} \u2014 kept {winner[0]} ({winner[1]:5d}pts)")
    kept += 1

for line in delete_log[:60]:
    print(line)
if len(delete_log) > 60:
    print(f"  ... and {len(delete_log) - 60} more")

print(f"\n  Kept: {kept} winners")
print(f"  Deleted: {deleted} duplicates")

# ─── Final count ───
remaining = sum(1 for _ in glob.glob(f"{BASE}/**/*.json", recursive=True))
print(f"\n=== TOTAL: {fixes_done} specific fixes, {deleted} duplicates removed ===")
print(f"=== Remaining entity files: {remaining} ===")
