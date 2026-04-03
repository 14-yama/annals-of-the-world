#!/usr/bin/env python3
"""
seed_wikidata_fast.py — Fast concurrent Appwrite seeder for Wikidata people.

Uses asyncio + aiohttp to seed entities concurrently (up to 50 concurrent requests).
Enriches entities with frameworks, causes, effects, relationships on-the-fly.
Optionally fetches Wikipedia summaries for richer overviews.

Usage:
  source .env && export APPWRITE_API_KEY
  python3 scripts/seed_wikidata_fast.py                          # full run, no wiki
  python3 scripts/seed_wikidata_fast.py --with-wiki --concurrency 20  # with wiki
  python3 scripts/seed_wikidata_fast.py --max 5000               # cap at 5k
  python3 scripts/seed_wikidata_fast.py --dry-run --max 5        # preview 5 enriched
"""

import argparse
import asyncio
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any

import aiohttp

# ── Project paths ──
PROJECT_ROOT = Path(__file__).resolve().parent.parent
MASTER_JSON  = PROJECT_ROOT / "data" / "wikidata_people.json"

# ── Appwrite config ──
ENDPOINT   = os.environ.get("VITE_APPWRITE_ENDPOINT", "https://fra.cloud.appwrite.io/v1")
PROJECT_ID = os.environ.get("VITE_APPWRITE_PROJECT_ID", "69cc45e3000d587ea5e6")
DATABASE_ID = os.environ.get("VITE_APPWRITE_DATABASE_ID", "annals_db")
API_KEY    = os.environ.get("APPWRITE_API_KEY", "")
COLLECTION = "entities"

# ── Concurrency / Rate ──
MAX_CONCURRENCY = 50
SAVE_EVERY      = 2000
WIKI_CONCURRENCY = 30
WIKI_API        = "https://en.wikipedia.org/api/rest_v1/page/summary/"

# ── Framework Assignment by Division ──
# (maps 3-digit division code → list of framework IDs)
DIV_FW: dict[str, list[str]] = {
    "201": ["CAUSE_AND_EFFECT","INNOVATION_AND_TECHNOLOGY"],
    "202": ["ECONOMIC_SYSTEMS","GEOPOLITICAL_LINKAGE"],
    "203": ["CAUSE_AND_EFFECT","CULTURAL_DIFFUSION"],
    "204": ["INNOVATION_AND_TECHNOLOGY","CAUSE_AND_EFFECT"],
    "205": ["CAUSE_AND_EFFECT","CULTURAL_DIFFUSION"],
    "210": ["DOCTRINE_DEVELOPMENT","CAUSE_AND_EFFECT"],
    "211": ["INNOVATION_AND_TECHNOLOGY","CAUSE_AND_EFFECT"],
    "212": ["DOCTRINE_DEVELOPMENT","CAUSE_AND_EFFECT"],
    "220": ["POLITICAL_SYSTEMS","GEOPOLITICAL_LINKAGE","CAUSE_AND_EFFECT"],
    "221": ["POLITICAL_SYSTEMS","EMPIRE_AND_COLONIALISM","GEOPOLITICAL_LINKAGE"],
    "222": ["POLITICAL_SYSTEMS","GEOPOLITICAL_LINKAGE"],
    "223": ["POLITICAL_SYSTEMS","ADAPTATION"],
    "230": ["LEGAL_INTERPRETATION","CAUSE_AND_EFFECT"],
    "231": ["LEGAL_INTERPRETATION","DOCTRINE_DEVELOPMENT"],
    "240": ["INNOVATION_AND_TECHNOLOGY","CAUSE_AND_EFFECT"],
    "241": ["INNOVATION_AND_TECHNOLOGY","CAUSE_AND_EFFECT"],
    "242": ["INNOVATION_AND_TECHNOLOGY","CAUSE_AND_EFFECT"],
    "243": ["INNOVATION_AND_TECHNOLOGY","ENVIRONMENTAL_HISTORY"],
    "250": ["COMPARATIVE_RELIGION","DOCTRINE_DEVELOPMENT","CULTURAL_DIFFUSION"],
    "251": ["COMPARATIVE_RELIGION","DOCTRINE_DEVELOPMENT"],
    "252": ["DOCTRINE_DEVELOPMENT","TEXTUAL_TRANSMISSION"],
    "253": ["COMPARATIVE_RELIGION","CULTURAL_DIFFUSION"],
    "260": ["CULTURAL_DIFFUSION","CAUSE_AND_EFFECT"],
    "261": ["TEXTUAL_TRANSMISSION","CULTURAL_DIFFUSION"],
    "262": ["TEXTUAL_TRANSMISSION","CULTURAL_DIFFUSION"],
    "263": ["CULTURAL_DIFFUSION","CAUSE_AND_EFFECT"],
    "264": ["CULTURAL_DIFFUSION","CAUSE_AND_EFFECT"],
    "265": ["INNOVATION_AND_TECHNOLOGY","CULTURAL_DIFFUSION"],
    "270": ["CAUSE_AND_EFFECT","CONFLICT_AND_RESOLUTION"],
    "271": ["CAUSE_AND_EFFECT","CONFLICT_AND_RESOLUTION"],
    "272": ["CAUSE_AND_EFFECT","CONFLICT_AND_RESOLUTION"],
    "273": ["ECONOMIC_SYSTEMS","CONFLICT_AND_RESOLUTION"],
    "280": ["CONFLICT_AND_RESOLUTION","GEOPOLITICAL_LINKAGE"],
    "281": ["CONFLICT_AND_RESOLUTION","GEOPOLITICAL_LINKAGE"],
    "282": ["CONFLICT_AND_RESOLUTION","GEOPOLITICAL_LINKAGE"],
    "283": ["CONFLICT_AND_RESOLUTION","GEOPOLITICAL_LINKAGE"],
    "290": ["CULTURAL_DIFFUSION","ENVIRONMENTAL_HISTORY","GEOPOLITICAL_LINKAGE"],
    "291": ["INNOVATION_AND_TECHNOLOGY","CAUSE_AND_EFFECT"],
    "292": ["INNOVATION_AND_TECHNOLOGY","ENVIRONMENTAL_HISTORY"],
    "293": ["INNOVATION_AND_TECHNOLOGY","CULTURAL_DIFFUSION"],
}

# ── Division headings ──
DIV_HEAD: dict[str, str] = {
    "201":"Educators & Academics","202":"Merchants & Economists",
    "203":"Athletes & Competitors","204":"Architects & Engineers",
    "205":"Journalists & Chroniclers","210":"Philosophers & Thinkers",
    "211":"Logicians & Mathematicians","212":"Ethicists & Moralists",
    "220":"Political Leaders","221":"Monarchs & Rulers",
    "222":"Heads of State & Government","223":"Tribal & Indigenous Leaders",
    "230":"Legal Figures","231":"Jurists & Legal Scholars",
    "240":"Scientists & Inventors","241":"Physicians & Medical Pioneers",
    "242":"Astronomers & Cosmologists","243":"Naturalists & Biologists",
    "250":"Religious Figures","251":"Prophets & Founders",
    "252":"Theologians & Scholars","253":"Missionaries",
    "260":"Artists & Writers","261":"Authors & Novelists",
    "262":"Poets & Playwrights","263":"Composers & Musicians",
    "264":"Painters & Sculptors","265":"Architects & Designers",
    "270":"Activists & Reformers","271":"Abolitionists",
    "272":"Suffragists & Feminists","273":"Labor Organizers",
    "280":"Military Leaders & Commanders","281":"Naval Commanders",
    "282":"Intelligence & Espionage","283":"Modern Military Commanders",
    "290":"Explorers & Navigators","291":"Space Explorers",
    "292":"Deep-Sea Explorers","293":"Cartographers",
}

# Primary verb per division
DIV_VERB: dict[str, tuple[str, str]] = {
    "201": ("TEACHES","Educational influence"), "202": ("TRADES","Commercial activity"),
    "203": ("COMPETES_IN","Athletic achievement"), "204": ("DESIGNS","Engineering achievement"),
    "205": ("REPORTS","Journalistic coverage"), "210": ("THEORIZES","Philosophical contribution"),
    "211": ("PROVES","Mathematical contribution"), "212": ("ADVOCATES","Ethical position"),
    "220": ("GOVERNS","Political leadership"), "221": ("RULES","Sovereign authority"),
    "222": ("LEADS","State leadership"), "223": ("LEADS","Tribal authority"),
    "230": ("ADJUDICATES","Legal ruling"), "231": ("INTERPRETS","Legal scholarship"),
    "240": ("DISCOVERS","Scientific discovery"), "241": ("TREATS","Medical advancement"),
    "242": ("OBSERVES","Astronomical observation"), "243": ("CLASSIFIES","Natural classification"),
    "250": ("PREACHES","Religious teaching"), "251": ("PROCLAIMS","Prophetic message"),
    "252": ("SYSTEMATIZES","Theological system"), "253": ("EVANGELIZES","Missionary work"),
    "260": ("CREATES","Artistic creation"), "261": ("PUBLISHES","Literary work"),
    "262": ("COMPOSES","Poetic work"), "263": ("COMPOSES","Musical composition"),
    "264": ("PAINTS","Visual art"), "265": ("DESIGNS","Design work"),
    "270": ("CAMPAIGNS","Reform activism"), "271": ("CAMPAIGNS","Abolition activism"),
    "272": ("CAMPAIGNS","Suffrage activism"), "273": ("ORGANIZES","Labor organizing"),
    "280": ("COMMANDS","Military command"), "281": ("COMMANDS","Naval command"),
    "282": ("INFILTRATES","Espionage operation"), "283": ("COMMANDS","Military command"),
    "290": ("EXPLORES","Exploration voyage"), "291": ("LAUNCHES","Space mission"),
    "292": ("DIVES","Deep-sea exploration"), "293": ("MAPS","Cartographic work"),
}

# Era context for causes/effects
ERA_CTX = {
    "Prehistoric": ("emergence of early civilizations and foundational human practices",
                    "laying groundwork for recorded human history and cultural transmission"),
    "Classical":   ("flourishing of philosophical inquiry, imperial expansion, and codification of law",
                    "enduring intellectual and institutional frameworks shaping subsequent civilizations"),
    "Medieval":    ("interplay of religious authority, feudal governance, and trade network expansion",
                    "synthesis of classical and religious thought informing Renaissance and Reformation"),
    "Early Modern":("age of exploration, printing revolution, and religious reformation",
                    "global exchange networks, modern state formation, and scientific revolution"),
    "Modern":      ("industrialization, imperial expansion, and democratic revolutions",
                    "mass society, world wars, and foundations of contemporary global order"),
    "Contemporary":("decolonization, technological revolution, and global interconnection",
                    "digital transformation, global governance challenges, and cultural globalization"),
}

# Domain cause/effect text per division
DIV_CAUSE: dict[str, str] = {
    "201":"Growth of educational institutions and scholarly traditions",
    "202":"Expansion of trade networks and commercial exchange",
    "203":"Development of competitive athletics and sporting traditions",
    "204":"Advancement of engineering knowledge and construction techniques",
    "205":"Rise of print media and public discourse",
    "210":"Ongoing philosophical inquiry and intellectual debate",
    "211":"Accumulation of mathematical knowledge and formal systems",
    "212":"Ongoing ethical inquiry and moral reflection",
    "220":"Political crises and power transitions requiring new leadership",
    "221":"Dynastic succession and sovereign authority traditions",
    "222":"Democratic movements and constitutional governance",
    "223":"Community governance traditions and indigenous leadership",
    "230":"Evolution of legal systems and jurisprudence",
    "231":"Development of legal scholarship and case law",
    "240":"Scientific curiosity and systematic investigation of nature",
    "241":"Medical challenges driving innovation in healing arts",
    "242":"Astronomical observations and cosmological questions",
    "243":"Exploration of natural world driving biological classification",
    "250":"Spiritual seeking and religious community formation",
    "251":"Prophetic calling and spiritual revelation",
    "252":"Theological debates and doctrinal development",
    "253":"Religious conviction driving cross-cultural mission",
    "260":"Artistic traditions and creative expression across cultures",
    "261":"Literary traditions and narrative storytelling",
    "262":"Poetic traditions and dramatic performance arts",
    "263":"Musical traditions and compositional innovation",
    "264":"Visual art traditions and aesthetic movements",
    "265":"Design traditions and architectural innovation",
    "270":"Social injustice and moral conviction driving reform",
    "271":"Moral opposition to slavery and human trafficking",
    "272":"Gender inequality driving women's rights movements",
    "273":"Worker exploitation and industrial conditions",
    "280":"Military conflicts and strategic necessities",
    "281":"Naval warfare and maritime strategy",
    "282":"Geopolitical tensions requiring intelligence operations",
    "283":"Modern warfare and technological military demands",
    "290":"Curiosity about unknown territories and navigation advances",
    "291":"Space race and technological competition",
    "292":"Oceanographic curiosity and deep-sea technology",
    "293":"Geographic knowledge gaps and mapping imperatives",
}
DIV_EFFECT: dict[str, str] = {
    "201":"Shaped intellectual traditions and educated future generations",
    "202":"Influenced economic patterns and commercial practices",
    "203":"Inspired sporting achievement and athletic culture",
    "204":"Left lasting engineering works and technical innovations",
    "205":"Shaped public opinion and historical record",
    "210":"Contributed philosophical ideas to ongoing intellectual discourse",
    "211":"Advanced mathematical knowledge used by subsequent scholars",
    "212":"Influenced ethical thought and moral frameworks",
    "220":"Shaped political institutions and governance practices",
    "221":"Established dynastic legacies and territorial boundaries",
    "222":"Influenced national policy and international relations",
    "223":"Preserved indigenous governance and cultural traditions",
    "230":"Shaped legal precedents and judicial practices",
    "231":"Advanced jurisprudential scholarship and legal theory",
    "240":"Advanced scientific knowledge and enabled new technologies",
    "241":"Improved medical practice and public health outcomes",
    "242":"Expanded astronomical understanding and cosmological models",
    "243":"Advanced biological classification and ecological understanding",
    "250":"Shaped religious practice and spiritual communities",
    "251":"Founded or reformed faith traditions",
    "252":"Developed theological frameworks influencing doctrine",
    "253":"Established religious communities in new regions",
    "260":"Enriched cultural heritage with lasting artistic works",
    "261":"Created literary works of enduring influence",
    "262":"Contributed poetry and drama to cultural canon",
    "263":"Created musical compositions of lasting significance",
    "264":"Produced visual artworks of cultural importance",
    "265":"Created architectural and design works shaping built environment",
    "270":"Advanced social reform and expanded civil liberties",
    "271":"Contributed to abolition of slavery and human rights",
    "272":"Advanced women's suffrage and gender equality",
    "273":"Improved labor conditions and worker protections",
    "280":"Determined military outcomes shaping geopolitical boundaries",
    "281":"Influenced naval strategy and maritime power dynamics",
    "282":"Shaped intelligence practices and national security",
    "283":"Influenced modern military doctrine and strategy",
    "290":"Expanded geographic knowledge and cultural exchange",
    "291":"Advanced space exploration and aerospace technology",
    "292":"Expanded deep-sea knowledge and marine science",
    "293":"Improved cartographic accuracy and geographic understanding",
}


# ─────────────────────────────────────────────────────────────────────
#  Enrichment (CPU-only — no network)
# ─────────────────────────────────────────────────────────────────────

def enrich(entity: dict, wiki_extract: str | None = None) -> dict:
    """Return enriched copy of the entity."""
    e = dict(entity)
    div = e["callNumber"][:3]
    name = e["name"]
    era = e.get("era", "")
    born = e.get("born", "")
    died = e.get("died", "")
    region = e.get("region", "")
    continent = e.get("continent", "")
    heading = DIV_HEAD.get(div, "Notable Figure")

    # ── Summary ──
    if wiki_extract and len(wiki_extract) > 60:
        summary = wiki_extract
        if len(summary) < 200:
            loc = f" based in {region}" if region and region != "Global" else (
                  f" based in {continent}" if continent and continent != "Global" else "")
            dt = f" ({born} – {died})" if born and died else (f" (b. {born})" if born else "")
            summary += f" {name} was a noted figure among {heading.lower()}{loc}{dt}, active during the {era} era."
    else:
        loc = f" from {region}" if region and region != "Global" else (
              f" from {continent}" if continent and continent != "Global" else "")
        dt = f" ({born} – {died})" if born and died else (f" (b. {born})" if born else "")
        parts = [f"{name}{dt} was a notable figure in the category of {heading.lower()}{loc}."]
        ctx = ERA_CTX.get(era)
        if ctx:
            parts.append(f"Active during the {era} era, a period characterized by {ctx[0]}.")
        places = e.get("places", [])
        if places:
            pn = [p["name"] for p in places if p.get("name")][:3]
            if pn:
                parts.append(f"Associated with {', '.join(pn)}.")
        vb = DIV_VERB.get(div)
        if vb:
            parts.append(f"Their work contributed to {vb[1].lower()} in the broader historical narrative.")
        summary = " ".join(parts)
    e["summary"] = summary[:9997] + "..." if len(summary) > 10000 else summary

    # ── Frameworks (2-4) ──
    fw = list(DIV_FW.get(div, ["CAUSE_AND_EFFECT"]))
    if era in ("Classical","Medieval") and "TEMPORAL_LINKAGE" not in fw:
        fw.append("TEMPORAL_LINKAGE")
    if era in ("Early Modern","Modern") and div in ("220","221","222","280","281","290"):
        if "EMPIRE_AND_COLONIALISM" not in fw:
            fw.append("EMPIRE_AND_COLONIALISM")
    e["frameworks"] = fw[:4]

    # ── Causes (2) ──
    causes = []
    ctx = ERA_CTX.get(era)
    if ctx:
        causes.append({"title": f"{era} era: {ctx[0][:80]}", "type": "EventWindow", "year": born or era})
    dc = DIV_CAUSE.get(div)
    if dc:
        causes.append({"title": dc, "type": "Idea", "year": born or ""})
    e["causes"] = causes[:2]

    # ── Effects (2) ──
    effects = []
    de = DIV_EFFECT.get(div)
    if de:
        effects.append({"title": de, "type": "Idea", "year": died or ""})
    if ctx:
        effects.append({"title": f"Contributed to {ctx[1][:80]}", "type": "Movement", "year": died or era})
    e["effects"] = effects[:2]

    # ── Relationships ──
    rels = list(e.get("relationships", []))
    vb = DIV_VERB.get(div)
    if vb:
        rels.append({
            "sourceSlug": e["slug"], "sourceName": name,
            "verb": vb[0],
            "targetSlug": f"field-{div}", "targetName": heading,
            "context": f"{name}: {vb[1]} in {heading.lower()}",
        })
    eraSlug = e.get("eraSlug", "")
    if era and eraSlug:
        rels.append({
            "sourceSlug": e["slug"], "sourceName": name,
            "verb": "OCCURS_DURING",
            "targetSlug": eraSlug, "targetName": f"{era} Era",
            "context": f"{name} was active during the {era} era",
        })
    for p in e.get("places", []):
        if p.get("role") == "Country" and p.get("slug"):
            rels.append({
                "sourceSlug": e["slug"], "sourceName": name,
                "verb": "SHAPES",
                "targetSlug": p["slug"], "targetName": p["name"],
                "context": f"{name} contributed to the historical development of {p['name']}",
            })
    e["relationships"] = rels

    # ── Texts ──
    texts = list(e.get("texts", []))
    if e.get("wikipediaUrl"):
        texts.append({"title": f"Wikipedia: {name}", "type": "Reference article", "slug": f"wikipedia-{e['slug']}"})
    e["texts"] = texts

    return e


# ─────────────────────────────────────────────────────────────────────
#  Appwrite document helpers
# ─────────────────────────────────────────────────────────────────────

def to_doc_id(slug: str) -> str:
    clean = re.sub(r"[^a-zA-Z0-9_-]", "_", slug)
    safe = re.sub(r"^[_-]+", "", clean)
    if 0 < len(safe) <= 36:
        return safe
    h = 5381
    for ch in slug:
        h = ((h << 5) + h + ord(ch)) & 0xFFFFFFFF
    hs = format(h, "x").ljust(8, "0")[:8]
    prefix = re.sub(r"[_-]+$", "", safe[:27])
    return (prefix + "_" + hs)[:36]


def to_doc(e: dict) -> dict:
    details = json.dumps({
        "tags": [],
        "externalLinks": [e["wikipediaUrl"]] if e.get("wikipediaUrl") else [],
        "thumbnailUrl": e.get("imageUrl") or None,
        "quote": None, "legacySummary": None,
        "causes": e.get("causes", []),
        "effects": e.get("effects", []),
        "relationships": e.get("relationships", []),
        "places": e.get("places", []),
        "texts": e.get("texts", []),
    }, ensure_ascii=False)
    s = e.get("summary", "")
    return {
        "slug": e["slug"], "name": e["name"], "label": e["label"],
        "callNumber": e["callNumber"],
        "summary": s[:9997]+"..." if len(s)>10000 else s,
        "era": e.get("era",""), "eraSlug": e.get("eraSlug",""),
        "region": e.get("region",""), "continent": e.get("continent",""),
        "status": e.get("status","Published"),
        "born": e.get("born") or None, "died": e.get("died") or None,
        "founded": None, "period": None,
        "startDate": e.get("born") or None, "endDate": e.get("died") or None,
        "subjectHeadings": e.get("subjectHeadings",[]),
        "subjects": e.get("subjects",[]),
        "frameworks": e.get("frameworks",[]),
        "altNames": [],
        "wikidataQid": e.get("wikidataQid") or None,
        "wikipediaUrl": e.get("wikipediaUrl") or None,
        "imageUrl": e.get("imageUrl") or None,
        "importanceScore": None,
        "detailsJson": details[:100000],
    }


# ─────────────────────────────────────────────────────────────────────
#  Async Wikipedia fetcher
# ─────────────────────────────────────────────────────────────────────

async def fetch_wiki(session: aiohttp.ClientSession, url: str) -> str | None:
    if not url:
        return None
    m = re.search(r"wikipedia\.org/wiki/(.+?)(?:\?|#|$)", url)
    if not m:
        return None
    import urllib.parse
    api_url = WIKI_API + urllib.parse.quote(m.group(1), safe="")
    try:
        async with session.get(api_url, timeout=aiohttp.ClientTimeout(total=10),
                               headers={"User-Agent": "AnnalsOfTheWorld/2.0"}) as resp:
            if resp.status == 200:
                d = await resp.json()
                ext = d.get("extract", "")
                return ext if len(ext) > 40 else None
    except Exception:
        pass
    return None


# ─────────────────────────────────────────────────────────────────────
#  Async Appwrite seeder
# ─────────────────────────────────────────────────────────────────────

async def create_doc(session: aiohttp.ClientSession, sem: asyncio.Semaphore,
                     doc_id: str, data: dict, attempt: int = 1) -> str:
    """Returns 'created', 'exists', or 'failed'."""
    url = f"{ENDPOINT}/databases/{DATABASE_ID}/collections/{COLLECTION}/documents"
    body = json.dumps({"documentId": doc_id, "data": data}, ensure_ascii=False)
    headers = {
        "Content-Type": "application/json",
        "X-Appwrite-Project": PROJECT_ID,
        "X-Appwrite-Key": API_KEY,
    }
    async with sem:
        try:
            async with session.post(url, data=body, headers=headers,
                                    timeout=aiohttp.ClientTimeout(total=30)) as resp:
                if resp.status in (200, 201):
                    return "created"
                if resp.status == 409:
                    return "exists"
                if resp.status == 429:
                    ra = int(resp.headers.get("Retry-After", "5"))
                    await asyncio.sleep(ra)
                    if attempt < 3:
                        return await create_doc(session, sem, doc_id, data, attempt + 1)
                if attempt < 3:
                    await asyncio.sleep(1.0 * attempt)
                    return await create_doc(session, sem, doc_id, data, attempt + 1)
                return "failed"
        except Exception:
            if attempt < 3:
                await asyncio.sleep(1.0 * attempt)
                return await create_doc(session, sem, doc_id, data, attempt + 1)
            return "failed"


async def run(args):
    print(f"Loading: {MASTER_JSON}")
    with open(MASTER_JSON, "r", encoding="utf-8") as f:
        master = json.load(f)

    all_ents = master["entities"]
    print(f"Total entities: {len(all_ents):,}")

    candidates = [e for e in all_ents if not e.get("inAppwrite")]
    print(f"Not in Appwrite: {len(candidates):,}")

    if args.skip:
        candidates = candidates[args.skip:]
        print(f"After skip {args.skip}: {len(candidates):,}")
    if args.max:
        candidates = candidates[:args.max]
        print(f"Capped at {args.max}: {len(candidates):,}")

    if not candidates:
        print("Nothing to seed.")
        return

    # Build index for updating master
    slug_idx: dict[str, dict] = {e["slug"]: e for e in all_ents}

    created = exists = failed = 0
    t0 = time.time()
    concurrency = args.concurrency

    if args.dry_run:
        print(f"\n=== DRY RUN ({len(candidates):,} entities) ===\n")
        for c in candidates[:5]:
            enriched = enrich(c)
            doc = to_doc(enriched)
            det = json.loads(doc["detailsJson"])
            print(f"  [{doc['callNumber']}] {doc['name']} ({doc['era']})")
            print(f"    Summary: {doc['summary'][:200]}...")
            print(f"    Frameworks: {doc['frameworks']}")
            print(f"    Causes: {len(det['causes'])} | Effects: {len(det['effects'])} "
                  f"| Rels: {len(det['relationships'])} | Places: {len(det['places'])} "
                  f"| Texts: {len(det['texts'])}")
            print()
        return

    sem = asyncio.Semaphore(concurrency)
    conn = aiohttp.TCPConnector(limit=concurrency + 10, ttl_dns_cache=300)

    async with aiohttp.ClientSession(connector=conn) as session:
        wiki_sem = asyncio.Semaphore(WIKI_CONCURRENCY) if args.with_wiki else None

        # Process in chunks for periodic saves
        chunk_size = SAVE_EVERY
        for chunk_start in range(0, len(candidates), chunk_size):
            chunk = candidates[chunk_start:chunk_start + chunk_size]

            # Optionally fetch wiki summaries for this chunk
            wiki_map: dict[str, str] = {}
            if args.with_wiki:
                async def _fetch_w(e):
                    async with wiki_sem:
                        ext = await fetch_wiki(session, e.get("wikipediaUrl",""))
                        if ext:
                            wiki_map[e["slug"]] = ext
                await asyncio.gather(*[_fetch_w(e) for e in chunk if e.get("wikipediaUrl")])

            # Enrich all
            enriched_list = [enrich(e, wiki_map.get(e["slug"])) for e in chunk]

            # Seed concurrently
            async def _seed(enriched):
                nonlocal created, exists, failed
                doc_id = to_doc_id(enriched["slug"])
                doc = to_doc(enriched)
                result = await create_doc(session, sem, doc_id, doc)
                # Update master
                src = slug_idx.get(enriched["slug"])
                if src:
                    src["summary"] = enriched["summary"]
                    src["frameworks"] = enriched["frameworks"]
                    src["causes"] = enriched["causes"]
                    src["effects"] = enriched["effects"]
                    src["relationships"] = enriched["relationships"]
                    src["texts"] = enriched["texts"]
                    if result in ("created", "exists"):
                        src["inAppwrite"] = True
                if result == "created":
                    created += 1
                elif result == "exists":
                    exists += 1
                else:
                    failed += 1

            await asyncio.gather(*[_seed(e) for e in enriched_list])

            # Progress
            done = min(chunk_start + chunk_size, len(candidates))
            elapsed = time.time() - t0
            rate = done / elapsed if elapsed > 0 else 0
            eta = (len(candidates) - done) / rate / 60 if rate > 0 else 0
            print(f"  [{done:,}/{len(candidates):,}] created={created:,} exists={exists:,} "
                  f"failed={failed:,} rate={rate:.0f}/s ETA={eta:.1f}min")

            # Save periodically
            with open(MASTER_JSON, "w", encoding="utf-8") as f:
                json.dump(master, f, ensure_ascii=False)

    # Final save (with indentation for readability)
    with open(MASTER_JSON, "w", encoding="utf-8") as f:
        json.dump(master, f, indent=2, ensure_ascii=False)

    elapsed = time.time() - t0
    in_aw = sum(1 for e in all_ents if e.get("inAppwrite"))
    not_aw = sum(1 for e in all_ents if not e.get("inAppwrite"))
    print(f"\n=== Complete ({elapsed/60:.1f} min) ===")
    print(f"  Created:  {created:,}")
    print(f"  Existed:  {exists:,}")
    print(f"  Failed:   {failed:,}")
    print(f"  Now in Appwrite: {in_aw:,}")
    print(f"  NOT in Appwrite: {not_aw:,}")
    print(f"  Rate: {(created+exists)/elapsed:.0f} docs/s")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--concurrency", type=int, default=MAX_CONCURRENCY)
    parser.add_argument("--skip", type=int, default=0)
    parser.add_argument("--max", type=int, default=0)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--with-wiki", action="store_true", help="Fetch Wikipedia summaries")
    args = parser.parse_args()

    if not args.dry_run and not API_KEY:
        print("ERROR: Set APPWRITE_API_KEY (or use --dry-run)")
        sys.exit(1)

    asyncio.run(run(args))


if __name__ == "__main__":
    main()
