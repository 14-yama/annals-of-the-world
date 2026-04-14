#!/usr/bin/env python3
"""
Autonomous AI Entity Enrichment — Enriches weak entities using LLM APIs.

Reads from enrichment queue, calls LLM (Gemini free tier or OpenAI), validates
output against quality thresholds, writes enriched JSON, and syncs to Appwrite.

Usage:
    # Generate queue first
    python3 scripts/enrichment_queue.py

    # Dry run — preview 5 enrichments without writing
    python3 scripts/ai_enrich_autonomous.py --dry-run --count 5

    # Enrich 25 entities using Gemini (default, free tier)
    python3 scripts/ai_enrich_autonomous.py --count 25

    # Use OpenAI GPT-4o-mini instead
    python3 scripts/ai_enrich_autonomous.py --count 25 --model openai

    # Skip Appwrite sync (local files only)
    python3 scripts/ai_enrich_autonomous.py --count 10 --no-sync

Environment Variables:
    GEMINI_API_KEY   — Google Gemini API key (free tier: 1M tokens/day)
    OPENAI_API_KEY   — OpenAI API key (paid fallback)
    APPWRITE_API_KEY — Appwrite API key (for backend sync)
"""
import json
import os
import sys
import argparse
import time
import hashlib
import urllib.request
import urllib.error
import urllib.parse

# ═══════════════════════════════════════════════════════════
# Configuration
# ═══════════════════════════════════════════════════════════

BASE = "data/appwrite-export/entities"
QUEUE_FILE = "data/enrichment/queue.json"
REPORT_FILE = "data/enrichment/last_run.json"

APPWRITE_ENDPOINT = "https://fra.cloud.appwrite.io/v1"
APPWRITE_PROJECT = "66509ba7003618a05af6"
APPWRITE_DB = "annals_world_db"
APPWRITE_COLLECTION = "entities"

VALID_VERBS = sorted([
    "CAUSES", "INFLUENCES", "COLLABORATES_WITH", "PARTICIPATES_IN",
    "CREATES", "OCCURS_IN", "FRAMES", "DEFINES", "TRANSFORMS",
    "TRANSMITS", "SUCCEEDS", "CONTAINS", "OCCURS_DURING", "CANONIZES",
])

VALID_FRAMEWORKS = sorted([
    "CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS", "WORLD_SYSTEMS",
    "CULTURAL_TRANSMISSION", "COMPARATIVE_CIVILIZATIONS",
    "RELIGIOUS_INTERPRETATION", "FEMINIST_PERSPECTIVE", "MARXIST_ANALYSIS",
    "PSYCHOLOGICAL_ANALYSIS", "ENVIRONMENTAL_HISTORY",
    "POSTCOLONIAL_ANALYSIS", "SUBALTERN_STUDIES", "DIPLOMATIC_HISTORY",
    "ECONOMIC_ANALYSIS", "TECHNOLOGICAL_DETERMINISM", "LONGUE_DUREE",
])

# ═══════════════════════════════════════════════════════════
# Prompt Template
# ═══════════════════════════════════════════════════════════

PROMPT_TEMPLATE = """You are enriching entities for "Annals of the World," a scholarly historical knowledge graph spanning 72,000 years of human history from Prehistory to the Digital Age.

## Entity to Enrich
- Name: {name}
- Slug: {slug}
- Label: {label}
- Era: {era}
- Region: {region}
- Continent: {continent}
- Born: {born}
- Died: {died}
- Current Summary ({summary_len} chars): {current_summary}

## Quality Standards

Generate a scholarly yet engaging enrichment following these EXACT standards:

### Summary (800-1,300 characters)
- 3-4 paragraphs separated by \\n\\n
- Paragraph 1: Identity + dates + core significance (who, when, why they matter)
- Paragraph 2: Key achievements, events, or contributions (the "what happened")
- Paragraph 3: Impact, consequences, or legacy (the "so what")
- Paragraph 4 (optional): A vivid closing fact, quote, or lasting cultural footprint
- Include concrete dates, numbers, and named events — not vague generalities
- One memorable attributed quote per entity is encouraged (in single quotes)
- Tone: scholarly but engaging — avoid dry encyclopedia prose

### Causes (exactly 3)
Causal antecedents — conditions, events, or influences that led to this entity's significance.
Each should be a single concise sentence.

### Effects (exactly 3)
Consequent outcomes — what this entity caused, influenced, or left as legacy.
Each should be a single concise sentence.

### Relationships (exactly 5)
Each relationship MUST have ALL six fields:
- sourceSlug: kebab-case slug of source entity
- sourceName: full display name of source entity
- verb: MUST be one of [{valid_verbs}]
- targetSlug: kebab-case slug of target entity
- targetName: full display name of target entity
- context: one-sentence description of the specific relationship

Rules:
- At least 1 relationship must have {slug} as the TARGET (incoming influence)
- At least 1 must use OCCURS_IN with a real place slug
- Use real historical figures/events as targets (kebab-case slugs)
- Context should be specific with dates where possible

### Places (exactly 3)
Each with: name ("City, Country" format), role (1-3 word description like "Birthplace" or "Major battle")

### Subjects (8-10 items)
Topic tags. MUST include: the entity's country/region and primary field/domain.

### Frameworks (exactly 3)
Choose from: {valid_frameworks}

## Output
Return ONLY a valid JSON object with these exact keys — no markdown, no explanation:
{{"summary": "...", "causes": ["..."], "effects": ["..."], "relationships": [{{"sourceSlug": "...", "sourceName": "...", "verb": "...", "targetSlug": "...", "targetName": "...", "context": "..."}}], "places": [{{"name": "...", "role": "..."}}], "subjects": ["..."], "frameworks": ["..."]}}"""


# ═══════════════════════════════════════════════════════════
# LLM API Calls
# ═══════════════════════════════════════════════════════════

def call_gemini(prompt, api_key, model="gemini-1.5-flash"):
    """Call Google Gemini API. Free tier: 15 RPM, 1M tokens/day."""
    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/{model}"
        f":generateContent?key={api_key}"
    )
    body = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 4096,
            "responseMimeType": "application/json",
        },
    }).encode()
    req = urllib.request.Request(
        url, data=body, headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=90) as resp:
        data = json.loads(resp.read())

    text = data["candidates"][0]["content"]["parts"][0]["text"]
    return json.loads(text)


def call_openai(prompt, api_key, model="gpt-4o-mini"):
    """Call OpenAI API. Paid: ~$0.15/1M input, $0.60/1M output."""
    url = "https://api.openai.com/v1/chat/completions"
    body = json.dumps({
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a historical knowledge base enrichment assistant. "
                    "Return ONLY valid JSON matching the requested schema."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.7,
        "response_format": {"type": "json_object"},
    }).encode()
    req = urllib.request.Request(url, data=body, headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    })
    with urllib.request.urlopen(req, timeout=90) as resp:
        data = json.loads(resp.read())

    text = data["choices"][0]["message"]["content"]
    return json.loads(text)


# ═══════════════════════════════════════════════════════════
# Validation
# ═══════════════════════════════════════════════════════════

def validate_enrichment(result):
    """Validate LLM output against quality thresholds. Returns (ok, reason)."""
    if not isinstance(result, dict):
        return False, "response is not a JSON object"

    # Summary
    summary = result.get("summary", "")
    if not isinstance(summary, str) or len(summary) < 600:
        return False, f"summary too short ({len(summary) if isinstance(summary, str) else 0}c, need >= 600)"
    if len(summary) > 2000:
        return False, f"summary too long ({len(summary)}c, max 2000)"

    # Causes
    causes = result.get("causes", [])
    if not isinstance(causes, list) or len(causes) < 2:
        return False, f"insufficient causes ({len(causes) if isinstance(causes, list) else 0}, need >= 2)"

    # Effects
    effects = result.get("effects", [])
    if not isinstance(effects, list) or len(effects) < 2:
        return False, f"insufficient effects ({len(effects) if isinstance(effects, list) else 0}, need >= 2)"

    # Relationships
    rels = result.get("relationships", [])
    if not isinstance(rels, list) or len(rels) < 3:
        return False, f"insufficient relationships ({len(rels) if isinstance(rels, list) else 0}, need >= 3)"
    required_keys = {"sourceSlug", "sourceName", "verb", "targetSlug", "targetName", "context"}
    for i, rel in enumerate(rels):
        if not isinstance(rel, dict):
            return False, f"relationship[{i}] is not a dict"
        missing = required_keys - set(rel.keys())
        if missing:
            return False, f"relationship[{i}] missing keys: {missing}"
        verb = rel.get("verb", "")
        if verb not in VALID_VERBS:
            return False, f"relationship[{i}] invalid verb: '{verb}'"

    # Places
    places = result.get("places", [])
    if not isinstance(places, list) or len(places) < 2:
        return False, f"insufficient places ({len(places) if isinstance(places, list) else 0}, need >= 2)"

    # Subjects
    subjects = result.get("subjects", [])
    if not isinstance(subjects, list) or len(subjects) < 5:
        return False, f"insufficient subjects ({len(subjects) if isinstance(subjects, list) else 0}, need >= 5)"

    # Frameworks
    frameworks = result.get("frameworks", [])
    if not isinstance(frameworks, list) or len(frameworks) < 2:
        return False, f"insufficient frameworks ({len(frameworks) if isinstance(frameworks, list) else 0}, need >= 2)"
    for fw in frameworks:
        if fw not in VALID_FRAMEWORKS:
            return False, f"invalid framework: '{fw}'"

    return True, "ok"


# ═══════════════════════════════════════════════════════════
# Apply Enrichment to Local Files
# ═══════════════════════════════════════════════════════════

def apply_enrichment(filepath, slug, result):
    """Write enrichment data to the local entity JSON file."""
    with open(filepath, "r") as f:
        data = json.load(f)

    for entity in data.get("entities", []):
        if entity.get("slug") != slug:
            continue

        entity["summary"] = result["summary"]

        # Parse and update detailsJson
        dj = entity.get("detailsJson", "")
        if isinstance(dj, str) and dj:
            try:
                details = json.loads(dj)
            except (json.JSONDecodeError, ValueError):
                details = {}
        elif isinstance(dj, dict):
            details = dj
        else:
            details = {}

        details["causes"] = result.get("causes", [])
        details["effects"] = result.get("effects", [])
        details["relationships"] = result.get("relationships", [])
        details["places"] = result.get("places", [])
        entity["detailsJson"] = json.dumps(details, ensure_ascii=False)

        if result.get("subjects"):
            entity["subjects"] = result["subjects"]
        if result.get("frameworks"):
            entity["frameworks"] = result["frameworks"]

        break

    with open(filepath, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


# ═══════════════════════════════════════════════════════════
# Appwrite Sync
# ═══════════════════════════════════════════════════════════

def slug_to_id(slug):
    return hashlib.sha256(slug.encode()).hexdigest()[:20]


def appwrite_headers(api_key):
    return {
        "Content-Type": "application/json",
        "X-Appwrite-Project": APPWRITE_PROJECT,
        "X-Appwrite-Key": api_key,
    }


def sync_to_appwrite(slug, entity, api_key):
    """Update entity in Appwrite. Tries hash ID -> slug ID -> query lookup."""
    dj = entity.get("detailsJson", "")
    if isinstance(dj, dict):
        dj = json.dumps(dj, ensure_ascii=False)

    payload = {
        "slug": slug,
        "name": entity.get("name", ""),
        "label": entity.get("label", ""),
        "callNumber": entity.get("callNumber", ""),
        "era": entity.get("era", ""),
        "summary": entity.get("summary", ""),
        "continent": entity.get("continent", ""),
        "region": entity.get("region", ""),
        "subjects": entity.get("subjects", []),
        "subjectHeadings": entity.get("subjectHeadings", []),
        "detailsJson": dj,
    }

    headers_dict = appwrite_headers(api_key)
    body = json.dumps({"data": payload}).encode()
    base_url = f"{APPWRITE_ENDPOINT}/databases/{APPWRITE_DB}/collections/{APPWRITE_COLLECTION}/documents"

    # Strategy 1: Hash-based ID
    doc_id = slug_to_id(slug)
    try:
        req = urllib.request.Request(
            f"{base_url}/{doc_id}", data=body, headers=headers_dict, method="PATCH"
        )
        with urllib.request.urlopen(req):
            return True
    except urllib.error.HTTPError:
        pass

    # Strategy 2: Slug as ID
    try:
        req = urllib.request.Request(
            f"{base_url}/{slug}", data=body, headers=headers_dict, method="PATCH"
        )
        with urllib.request.urlopen(req):
            return True
    except urllib.error.HTTPError:
        pass

    # Strategy 3: Query by slug attribute (handles legacy sanitized IDs)
    try:
        q = json.dumps({"method": "equal", "attribute": "slug", "values": [slug]})
        search_url = f"{base_url}?queries[]={urllib.parse.quote(q)}"
        req = urllib.request.Request(search_url, headers=headers_dict)
        with urllib.request.urlopen(req) as r:
            search_data = json.loads(r.read())
            docs = search_data.get("documents", [])
            if docs:
                actual_id = docs[0]["$id"]
                req2 = urllib.request.Request(
                    f"{base_url}/{actual_id}", data=body,
                    headers=headers_dict, method="PATCH"
                )
                with urllib.request.urlopen(req2):
                    return True
    except (urllib.error.HTTPError, KeyError, json.JSONDecodeError):
        pass

    return False


# ═══════════════════════════════════════════════════════════
# Main Pipeline
# ═══════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Autonomous AI entity enrichment pipeline"
    )
    parser.add_argument(
        "--count", type=int, default=25,
        help="Number of entities to enrich (default: 25)",
    )
    parser.add_argument(
        "--model", choices=["gemini", "openai"], default="gemini",
        help="LLM provider (default: gemini — free tier)",
    )
    parser.add_argument(
        "--gemini-model", default="gemini-1.5-flash",
        help="Gemini model name (default: gemini-1.5-flash)",
    )
    parser.add_argument(
        "--openai-model", default="gpt-4o-mini",
        help="OpenAI model name (default: gpt-4o-mini)",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Preview enrichments without writing files or syncing",
    )
    parser.add_argument(
        "--queue", default=QUEUE_FILE,
        help="Queue file path (default: data/enrichment/queue.json)",
    )
    parser.add_argument(
        "--no-sync", action="store_true",
        help="Skip Appwrite sync (local files only)",
    )
    parser.add_argument(
        "--min-score", type=float, default=0,
        help="Minimum queue score to process (default: 0)",
    )
    parser.add_argument(
        "--retry", type=int, default=1,
        help="Max retries per entity on LLM/validation failure (default: 1)",
    )
    args = parser.parse_args()

    # ── Load API keys ──
    if args.model == "gemini":
        api_key = os.environ.get("GEMINI_API_KEY", "")
        if not api_key and not args.dry_run:
            print("ERROR: Set GEMINI_API_KEY environment variable")
            print("  Get free key: https://aistudio.google.com/apikey")
            sys.exit(1)
    else:
        api_key = os.environ.get("OPENAI_API_KEY", "")
        if not api_key and not args.dry_run:
            print("ERROR: Set OPENAI_API_KEY environment variable")
            sys.exit(1)

    appwrite_key = os.environ.get("APPWRITE_API_KEY", "")

    # ── Load queue ──
    if not os.path.exists(args.queue):
        print(f"Queue file not found: {args.queue}")
        print("Generate it first: python3 scripts/enrichment_queue.py")
        sys.exit(1)

    with open(args.queue) as f:
        queue_data = json.load(f)
    queue = queue_data.get("queue", [])

    if args.min_score > 0:
        queue = [e for e in queue if e["score"] >= args.min_score]

    batch = queue[:args.count]
    if not batch:
        print("No entities to enrich (queue empty or all filtered)")
        sys.exit(0)

    # ── Run enrichment ──
    print(f"{'=' * 60}")
    print(f"AI ENRICHMENT — {len(batch)} entities via {args.model}")
    print(f"{'=' * 60}")
    if args.dry_run:
        print("** DRY RUN — no files will be modified **\n")

    enriched = 0
    failed = 0
    synced = 0
    report = []

    for i, entry in enumerate(batch):
        slug = entry["slug"]
        filepath = entry["filepath"]
        print(f"\n[{i + 1}/{len(batch)}] {slug} (score={entry['score']}, {entry['summaryLength']}c)")

        # Load current entity from file
        try:
            with open(filepath) as f:
                file_data = json.load(f)
            entity = None
            for e in file_data.get("entities", []):
                if e.get("slug") == slug:
                    entity = e
                    break
            if not entity:
                print(f"  SKIP — slug '{slug}' not found in {filepath}")
                continue
        except Exception as ex:
            print(f"  SKIP — error loading file: {ex}")
            continue

        # Skip if already enriched (queue may be stale)
        current_len = len(entity.get("summary", "") or "")
        if current_len >= 800:
            print(f"  SKIP — already enriched ({current_len}c)")
            continue

        # Build prompt
        prompt = PROMPT_TEMPLATE.format(
            name=entity.get("name", ""),
            slug=slug,
            label=entity.get("label", ""),
            era=entity.get("era", "") or "unknown",
            region=entity.get("region", "") or "unknown",
            continent=entity.get("continent", "") or "unknown",
            born=entity.get("born", "") or "unknown",
            died=entity.get("died", "") or "unknown",
            summary_len=current_len,
            current_summary=(entity.get("summary", "") or "")[:500] or "(none)",
            valid_verbs=", ".join(VALID_VERBS),
            valid_frameworks=", ".join(VALID_FRAMEWORKS),
        )

        if args.dry_run:
            print(f"  DRY RUN — would call {args.model} with {len(prompt)} char prompt")
            enriched += 1
            report.append({"slug": slug, "status": "dry_run"})
            continue

        # Call LLM with retry
        result = None
        last_error = ""
        for attempt in range(args.retry + 1):
            try:
                if args.model == "gemini":
                    result = call_gemini(prompt, api_key, args.gemini_model)
                else:
                    result = call_openai(prompt, api_key, args.openai_model)

                # Validate
                ok, reason = validate_enrichment(result)
                if ok:
                    break
                else:
                    last_error = reason
                    result = None
                    if attempt < args.retry:
                        print(f"  RETRY ({attempt + 1}) — {reason}")
                        time.sleep(2)
            except Exception as ex:
                last_error = str(ex)
                result = None
                if attempt < args.retry:
                    print(f"  RETRY ({attempt + 1}) — {ex}")
                    time.sleep(3)

        if result is None:
            print(f"  FAILED — {last_error}")
            failed += 1
            report.append({"slug": slug, "status": "failed", "reason": last_error})
            time.sleep(2)
            continue

        new_len = len(result.get("summary", ""))
        print(f"  ENRICHED — {current_len}c -> {new_len}c")

        # Write to local JSON
        apply_enrichment(filepath, slug, result)

        # Sync to Appwrite
        if not args.no_sync and appwrite_key:
            with open(filepath) as f:
                updated_data = json.load(f)
            for e in updated_data.get("entities", []):
                if e.get("slug") == slug:
                    if sync_to_appwrite(slug, e, appwrite_key):
                        synced += 1
                    else:
                        print(f"  SYNC FAILED — Appwrite update unsuccessful")
                    break

        enriched += 1
        report.append({
            "slug": slug,
            "status": "enriched",
            "old_len": current_len,
            "new_len": new_len,
        })

        # Rate limiting: Gemini 15 RPM = 4s between; OpenAI faster
        delay = 4.5 if args.model == "gemini" else 1.5
        time.sleep(delay)

    # ── Summary ──
    print(f"\n{'=' * 60}")
    print(f"RESULTS: {enriched} enriched, {failed} failed, {synced} synced")
    print(f"{'=' * 60}")

    # Save run report
    os.makedirs(os.path.dirname(REPORT_FILE), exist_ok=True)
    with open(REPORT_FILE, "w") as f:
        json.dump(
            {
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "model": args.model,
                "count_requested": args.count,
                "enriched": enriched,
                "failed": failed,
                "synced": synced,
                "dry_run": args.dry_run,
                "entities": report,
            },
            f,
            indent=2,
        )
        f.write("\n")
    print(f"Report: {REPORT_FILE}")


if __name__ == "__main__":
    main()
