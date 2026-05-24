#!/usr/bin/env python3
"""
Autonomous AI Entity Enrichment — git-first.

Reads from enrichment queue, calls LLM (Gemini free tier or OpenAI), validates
output against quality thresholds, and writes enriched JSON to the local git
repo only. The sync_gateway script (scripts/sync_gateway.ts) is the single
writer to Appwrite, run separately. This avoids per-entity Appwrite writes
that previously caused cost overruns.

Usage:
    # Generate queue first
    python3 scripts/enrichment_queue.py

    # Dry run — preview 5 enrichments without writing
    python3 scripts/ai_enrich_autonomous.py --dry-run --count 5

    # Enrich 25 entities using Gemini (default, free tier)
    python3 scripts/ai_enrich_autonomous.py --count 25

    # Use OpenAI GPT-4o-mini instead
    python3 scripts/ai_enrich_autonomous.py --count 25 --model openai

Environment Variables:
    GEMINI_API_KEY — Google Gemini API key (free tier: 1M tokens/day)
    OPENAI_API_KEY — OpenAI API key (paid fallback)
"""
import json
import os
import sys
import argparse
import time
import urllib.request
import urllib.error
import urllib.parse


def load_dotenv():
    """Load .env file if present (no dependency needed)."""
    env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#') or '=' not in line:
                    continue
                key, _, value = line.partition('=')
                key = key.strip()
                value = value.strip()
                if key and key not in os.environ:
                    os.environ[key] = value


load_dotenv()

# ═══════════════════════════════════════════════════════════
# Configuration
# ═══════════════════════════════════════════════════════════

BASE = "data/appwrite-export/entities"
QUEUE_FILE = "data/enrichment/queue.json"
REPORT_FILE = "data/enrichment/last_run.json"

# EDITOR_ID is built dynamically after args are parsed (see build_editor_id())
# Format: "<model>·<env>·<host/run>" — readable in audit log filters
# Examples:
#   ollama/llama3.2:3b·local·myhost          (local Ollama bot)
#   gemini-2.5-flash·cloud·GH#12345678       (GitHub Actions cloud bot)
#   gpt-4o-mini·cloud·GH#12345678            (GitHub Actions, OpenAI)
EDITOR_ID = "ai-enrichment-bot:gemini-2.5-flash"   # overwritten in main()


def build_editor_id(model: str, model_name: str) -> str:
    """
    Build a human-readable editorId that survives into the audit log.
    Shows: model name, environment (local vs cloud), and run context.
    """
    import socket
    is_github = bool(os.environ.get("GITHUB_ACTIONS"))
    if model == "ollama":
        env = "local"
        context = socket.gethostname()
        return f"ollama/{model_name}\u00b7{env}\u00b7{context}"
    elif is_github:
        run_id = os.environ.get("GITHUB_RUN_ID", "?")
        repo = os.environ.get("GITHUB_REPOSITORY", "annals")
        env = "cloud"
        return f"{model_name}\u00b7{env}\u00b7GH#{run_id}"
    else:
        import socket
        env = "local"
        context = socket.gethostname()
        return f"{model_name}\u00b7{env}\u00b7{context}"

VALID_VERBS = sorted([
    "CAUSES", "INFLUENCES", "COLLABORATES_WITH", "PARTICIPATES_IN",
    "CREATES", "OCCURS_IN", "FRAMES", "DEFINES", "TRANSFORMS",
    "TRANSMITS", "SUCCEEDS", "CONTAINS", "OCCURS_DURING", "CANONIZES",
])

# Normalize common LLM verb variants to canonical form (handles tense/case mismatches)
_VERB_ALIASES: dict[str, str] = {
    # Past tense → present tense
    "CAUSED": "CAUSES", "INFLUENCED": "INFLUENCES",
    "CREATED": "CREATES", "DEFINED": "DEFINES", "TRANSFORMED": "TRANSFORMS",
    "TRANSMITTED": "TRANSMITS", "SUCCEEDED": "SUCCEEDS", "FRAMED": "FRAMES",
    "CANONIZED": "CANONIZES", "CONTAINED": "CONTAINS",
    # Alternate phrasings
    "LEADS_TO": "CAUSES", "LED_TO": "CAUSES", "RESULTED_IN": "CAUSES",
    "FOUNDS": "CREATES", "FOUNDED": "CREATES", "ESTABLISHED": "CREATES",
    "BUILDS": "CREATES", "BUILT": "CREATES",
    "AFFECTED": "INFLUENCES", "SHAPED": "INFLUENCES", "IMPACTS": "INFLUENCES",
    "TOOK_PLACE_IN": "OCCURS_IN", "HAPPENED_IN": "OCCURS_IN",
    "PRECEDED": "SUCCEEDS", "FOLLOWED": "SUCCEEDS",
    "SPREAD": "TRANSMITS", "SPREAD_TO": "TRANSMITS",
    "INCLUDES": "CONTAINS", "CONSISTED_OF": "CONTAINS",
    "ARTICULATES": "DEFINES", "DESCRIBES": "DEFINES",
    "MODIFIED": "TRANSFORMS", "CHANGED": "TRANSFORMS",
    "WORKED_WITH": "COLLABORATES_WITH", "ALLIED_WITH": "COLLABORATES_WITH",
    "JOINED": "PARTICIPATES_IN", "PARTICIPATED_IN": "PARTICIPATES_IN",
}


def _normalize_verb(verb: str) -> str:
    """Normalize an LLM-generated verb to the nearest canonical VALID_VERBS form.
    Falls back to INFLUENCES (generic causal link) when no mapping is found."""
    upper = verb.upper().replace(" ", "_").strip()
    if upper in VALID_VERBS:
        return upper
    mapped = _VERB_ALIASES.get(upper)
    if mapped:
        return mapped
    # Fuzzy keyword fallback — preserves meaning over hard failure
    if any(k in upper for k in ("FOUND", "CREAT", "BUILD", "BUILT", "ESTABL")):
        return "CREATES"
    if any(k in upper for k in ("DEFEAT", "CONQUER", "DESTROY", "ANNEX")):
        return "TRANSFORMS"
    if any(k in upper for k in ("PRECEDE", "REIGN_BEFORE", "SUCCEED")):
        return "SUCCEEDS"
    if any(k in upper for k in ("OCCUR", "TOOK_PLACE", "HAPPEN")):
        return "OCCURS_IN"
    if any(k in upper for k in ("SPREAD", "TRANSMIT", "PASS")):
        return "TRANSMITS"
    if any(k in upper for k in ("CONTAIN", "INCLUD", "CONSIST")):
        return "CONTAINS"
    if any(k in upper for k in ("DEFIN", "ARTICUL", "DESCRIB")):
        return "DEFINES"
    if any(k in upper for k in ("TRANSFORM", "CHANG", "MODIF", "ALTER")):
        return "TRANSFORMS"
    if any(k in upper for k in ("COLLAB", "ALLIED", "WORK_WITH")):
        return "COLLABORATES_WITH"
    if any(k in upper for k in ("PARTICIPAT", "JOIN")):
        return "PARTICIPATES_IN"
    return "INFLUENCES"  # generic fallback — better than failing the whole enrichment

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

PROMPT_TEMPLATE = """You are enriching entities for "Annals of the World," a scholarly historical knowledge graph spanning 72,000 years of human history from Prehistory to the Digital Age, inspired by Archbishop Ussher's 1650 Annales Veteris Testamenti.

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

Generate a RICH, SCHOLARLY, VIVID enrichment. You are writing for serious historians AND curious general readers. Every sentence must carry specific information — no filler, no vague generalities.

### Summary (800–2,000 characters — write to the upper end for major entities)
- 3–4 paragraphs separated by \\n\\n
- **Paragraph 1 — Identity & Significance**: Who/what is this? Concrete dates, geographic scope, and WHY it matters in the arc of world history. Name the key people, places, or forces involved. Open with a strong, specific sentence — not "X was an important..."
- **Paragraph 2 — What Happened**: The core events, achievements, mechanisms, or contributions. Use real names, numbers, dates, place names. What actually occurred? What did it produce or destroy?
- **Paragraph 3 — Legacy & Consequence**: What changed because of this? Who inherited it? How did it ripple forward in time? Connect it to what came next.
- **Paragraph 4 (optional but encouraged)**: One vivid, memorable closing — a striking statistic, a direct attributed quote (in single quotes), a lasting cultural footprint, or an ironic twist of history.
- Tone: scholarly but narratively engaging — imagine Simon Schama meets Wikipedia's best-sourced articles
- FORBIDDEN: opening with "X was a/an important/notable/significant", single-paragraph walls of text, placeholder phrases like "a key figure associated with"
- CRITICAL: Total characters MUST be between 800–2000. Count carefully.

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

### Historical Significance
Rate and describe this entity's historical importance in three dimensions:
- **significanceScore**: Integer 1–10. Guidelines:
  - 10: Changed the entire trajectory of human civilization (Alexander, Islam, printing press)
  - 8–9: Shaped a continent or major era (Napoleon, Mongol Empire, Black Death)
  - 6–7: Significant regional or thematic impact (a major battle, an important inventor)
  - 4–5: Notable but limited scope (a secondary ruler, a regional movement)
  - 1–3: Local, minor, or specialist interest
- **significanceNarrative**: 1–2 sentence plain-English explanation of WHY this entity matters historically. Must be specific — include real consequences, numbers, or successor events.
- **significanceCategory**: Exactly one of: "world-changing" | "continental" | "regional" | "local"

## Output
Return ONLY a valid JSON object with these exact keys — no markdown, no explanation:
{{"summary": "...", "causes": ["..."], "effects": ["..."], "relationships": [{{"sourceSlug": "...", "sourceName": "...", "verb": "...", "targetSlug": "...", "targetName": "...", "context": "..."}}], "places": [{{"name": "...", "role": "..."}}], "subjects": ["..."], "frameworks": ["..."], "historicalSignificance": {{"significanceScore": 7, "significanceNarrative": "...", "significanceCategory": "regional"}}}}"""


# ═══════════════════════════════════════════════════════════
# LLM API Calls
# ═══════════════════════════════════════════════════════════

def _parse_llm_json(text):
    """Parse JSON from LLM output, fixing literal newlines inside strings."""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    # Fix: escape literal newlines that are inside JSON string values
    fixed = []
    in_string = False
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == '\\' and in_string and i + 1 < len(text):
            fixed.append(ch)
            fixed.append(text[i + 1])
            i += 2
            continue
        if ch == '"':
            in_string = not in_string
        if ch == '\n' and in_string:
            fixed.append('\\n')
        else:
            fixed.append(ch)
        i += 1
    return json.loads(''.join(fixed))


def call_gemini(prompt, api_key, model="gemini-2.5-flash"):
    """Call Google Gemini API. Free tier: 500 RPD for 2.5-flash."""
    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/{model}"
        f":generateContent?key={api_key}"
    )
    body = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 16384,
            "responseMimeType": "application/json",
            "thinkingConfig": {"thinkingBudget": 1024},
        },
    }).encode()
    req = urllib.request.Request(
        url, data=body, headers={"Content-Type": "application/json"}
    )
    # Retry on 429/503 with exponential backoff
    for backoff in [0, 15, 30, 60]:
        if backoff:
            print(f"    Rate limited — waiting {backoff}s...")
            time.sleep(backoff)
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read())
            text = data["candidates"][0]["content"]["parts"][0]["text"]
            return _parse_llm_json(text)
        except urllib.error.HTTPError as e:
            if e.code in (429, 503):
                continue
            raise
    raise RuntimeError("Rate limited after 4 retries")


def call_github_models(prompt, token, model="gpt-4o-mini"):
    """Call GitHub Models API (free for Copilot users). OpenAI-compatible.
    Endpoint: https://models.inference.ai.azure.com
    Auth: GitHub personal access token or `gh auth token`.
    Rate limits: ~15 req/min (free), ~150 req/min (Copilot Pro)."""
    url = "https://models.inference.ai.azure.com/chat/completions"
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
        "max_tokens": 3000,
    }).encode()
    req = urllib.request.Request(url, data=body, headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    })
    with urllib.request.urlopen(req, timeout=90) as resp:
        data = json.loads(resp.read())
    text = data["choices"][0]["message"]["content"]
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


OLLAMA_BASE_ENRICH = os.environ.get("OLLAMA_HOST", "http://localhost:11434")

def _wait_for_ollama_free(url_base: str, max_wait: int = 600, poll: int = 15) -> bool:
    """Block until Ollama is not running a generation (or max_wait seconds pass).
    Uses /api/ps — if any model is loaded and running, wait.
    Returns True when free, False on timeout."""
    import urllib.error
    ps_url = f"{url_base}/api/ps"
    waited = 0
    while waited < max_wait:
        try:
            with urllib.request.urlopen(ps_url, timeout=5) as resp:
                ps = json.loads(resp.read())
            # models list in /api/ps — empty means nothing is generating
            models = ps.get("models", [])
            if not models:
                return True
            # If something IS loaded/running, wait a bit
            time.sleep(poll)
            waited += poll
        except Exception:
            # Can't connect at all — Ollama is down; wait for it
            time.sleep(poll)
            waited += poll
    return False  # timed out


def call_ollama(prompt, model="llama3.2:3b"):
    """Call local Ollama — no quota, no cost, runs on-device. Ideal for local power sessions.
    Waits for Ollama to be free before sending (prevents connection refused when
    two enrichment threads compete for the same single-threaded Ollama instance)."""
    url = f"{OLLAMA_BASE_ENRICH}/api/generate"
    # num_predict: 3000 tokens ≈ ~1750 words; enough for complete JSON enrichment on 3b models.
    # At ~8 tok/s on a Ryzen 5 CPU that's ~375s — within the 500s timeout.
    # Large models (7b+) can use 4096 without issue.
    is_small = "3b" in model or "1b" in model
    num_predict = 3000 if is_small else 4096
    body = json.dumps({
        "model": model,
        "prompt": prompt,
        "format": "json",
        "stream": False,
        "options": {"temperature": 0.7, "num_predict": num_predict, "num_ctx": 4096},
    }).encode()
    req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"})

    # Retry loop: if Ollama is busy/crashed, wait and retry (up to 3 attempts)
    last_err = None
    for attempt in range(3):
        if attempt > 0:
            wait = 20 * attempt  # 20s, then 40s
            time.sleep(wait)
        try:
            with urllib.request.urlopen(req, timeout=500) as resp:
                data = json.loads(resp.read())
            text = data.get("response", "")
            return _parse_llm_json(text)
        except Exception as e:
            last_err = e
            err_str = str(e)
            # Connection refused or remote closed = Ollama busy/restarting — wait and retry
            if "111" in err_str or "Connection refused" in err_str or "Remote end closed" in err_str:
                continue
            raise  # unexpected error — propagate immediately
    raise last_err


# ═══════════════════════════════════════════════════════════
# Validation
# ═══════════════════════════════════════════════════════════

def validate_enrichment(result, lenient: bool = False):
    """Validate LLM output against quality thresholds. Returns (ok, reason).
    Use lenient=True for small models (llama3.2:3b) that can't hit GPT-4 standards."""
    if not isinstance(result, dict):
        return False, "response is not a JSON object"

    # Adjusted thresholds
    min_summary  = 400 if lenient else 600
    min_causes   = 1   if lenient else 2
    min_effects  = 1   if lenient else 2
    min_rels     = 2   if lenient else 3
    min_places   = 1   if lenient else 2
    min_subjects = 3   if lenient else 5

    # Summary — accept 800-2000c; auto-trim at 2000 to keep complete paragraphs
    summary = result.get("summary", "")
    if not isinstance(summary, str) or len(summary) < min_summary:
        return False, f"summary too short ({len(summary) if isinstance(summary, str) else 0}c, need >= {min_summary})"
    if len(summary) > 2000:
        # Smart trim: keep complete paragraphs that fit under 2000c
        paragraphs = summary.split("\n\n")
        trimmed = ""
        for p in paragraphs:
            candidate = (trimmed + "\n\n" + p).strip() if trimmed else p
            if len(candidate) <= 2000:
                trimmed = candidate
            else:
                break
        if len(trimmed) >= 600:
            result["summary"] = trimmed
            summary = trimmed
        elif len(summary) > 3000:
            return False, f"summary too long ({len(summary)}c, max 3000)"

    # Causes
    causes = result.get("causes", [])
    if not isinstance(causes, list) or len(causes) < min_causes:
        return False, f"insufficient causes ({len(causes) if isinstance(causes, list) else 0}, need >= {min_causes})"

    # Effects
    effects = result.get("effects", [])
    if not isinstance(effects, list) or len(effects) < min_effects:
        return False, f"insufficient effects ({len(effects) if isinstance(effects, list) else 0}, need >= {min_effects})"

    # Relationships
    rels = result.get("relationships", [])
    if not isinstance(rels, list) or len(rels) < min_rels:
        return False, f"insufficient relationships ({len(rels) if isinstance(rels, list) else 0}, need >= {min_rels})"
    required_keys = {"sourceSlug", "sourceName", "verb", "targetSlug", "targetName", "context"}
    for i, rel in enumerate(rels):
        if not isinstance(rel, dict):
            return False, f"relationship[{i}] is not a dict"
        missing = required_keys - set(rel.keys())
        if missing:
            return False, f"relationship[{i}] missing keys: {missing}"
        verb = rel.get("verb", "")
        normalized = _normalize_verb(verb)
        if normalized != verb:
            rel["verb"] = normalized  # fix in-place
            verb = normalized
        if verb not in VALID_VERBS:
            return False, f"relationship[{i}] invalid verb: '{verb}'"

    # Places
    places = result.get("places", [])
    if not isinstance(places, list) or len(places) < min_places:
        return False, f"insufficient places ({len(places) if isinstance(places, list) else 0}, need >= {min_places})"

    # Subjects
    subjects = result.get("subjects", [])
    if not isinstance(subjects, list) or len(subjects) < min_subjects:
        return False, f"insufficient subjects ({len(subjects) if isinstance(subjects, list) else 0}, need >= {min_subjects})"

    # Frameworks — drop unknown values in-place rather than failing the whole enrichment
    frameworks = result.get("frameworks", [])
    if not isinstance(frameworks, list):
        return False, "frameworks is not a list"
    valid_fws = [fw for fw in frameworks if fw in VALID_FRAMEWORKS]
    if len(valid_fws) < 1:
        if lenient:
            valid_fws = ["CAUSE_AND_EFFECT"]  # default fallback in lenient mode
        else:
            return False, f"insufficient valid frameworks ({len(valid_fws)} after filtering, need >= 1)"
    result["frameworks"] = valid_fws  # silently drop unrecognised framework names

    return True, "ok"


# ═══════════════════════════════════════════════════════════
# Apply Enrichment to Local Files
# ═══════════════════════════════════════════════════════════

def _diff_field(old, new):
    """Return (changed, old_repr, new_repr) — JSON-comparable."""
    old_n = old if old is not None else ""
    new_n = new if new is not None else ""
    return (json.dumps(old_n, sort_keys=True) != json.dumps(new_n, sort_keys=True),
            old_n, new_n)


def apply_enrichment(filepath, slug, result):
    """Write enrichment data to the local entity JSON file and append a
    per-field _editLog[] inside detailsJson. The sync_gateway replays
    _editLog[] entries into Appwrite audit_log on its next run.
    """
    with open(filepath, "r") as f:
        data = json.load(f)

    timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ")

    for entity in data.get("entities", []):
        if entity.get("slug") != slug:
            continue

        # Parse current detailsJson
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

        # Compute diffs BEFORE mutating
        edit_log_entries = []
        old_summary = entity.get("summary", "") or ""
        if old_summary != result["summary"]:
            edit_log_entries.append({
                "timestamp": timestamp, "editorId": EDITOR_ID,
                "field": "summary",
                "oldValue": old_summary, "newValue": result["summary"],
            })

        for fname, new_val in (
            ("causes", result.get("causes", [])),
            ("effects", result.get("effects", [])),
            ("relationships", result.get("relationships", [])),
            ("places", result.get("places", [])),
        ):
            old_val = details.get(fname, [])
            changed, _, _ = _diff_field(old_val, new_val)
            if changed:
                edit_log_entries.append({
                    "timestamp": timestamp, "editorId": EDITOR_ID,
                    "field": f"detailsJson.{fname}",
                    "oldValue": old_val, "newValue": new_val,
                })

        if result.get("subjects"):
            old_val = entity.get("subjects", []) or []
            if json.dumps(sorted(old_val)) != json.dumps(sorted(result["subjects"])):
                edit_log_entries.append({
                    "timestamp": timestamp, "editorId": EDITOR_ID,
                    "field": "subjects",
                    "oldValue": old_val, "newValue": result["subjects"],
                })
        if result.get("frameworks"):
            old_val = entity.get("frameworks", []) or []
            if json.dumps(sorted(old_val)) != json.dumps(sorted(result["frameworks"])):
                edit_log_entries.append({
                    "timestamp": timestamp, "editorId": EDITOR_ID,
                    "field": "frameworks",
                    "oldValue": old_val, "newValue": result["frameworks"],
                })

        # Apply changes
        entity["summary"] = result["summary"]
        details["causes"] = result.get("causes", [])
        details["effects"] = result.get("effects", [])
        details["relationships"] = result.get("relationships", [])
        details["places"] = result.get("places", [])
        if result.get("subjects"):
            entity["subjects"] = result["subjects"]
        if result.get("frameworks"):
            entity["frameworks"] = result["frameworks"]
        # Historical significance — store on entity root + detailsJson
        if result.get("historicalSignificance"):
            hs = result["historicalSignificance"]
            if isinstance(hs, dict) and isinstance(hs.get("significanceScore"), (int, float)):
                entity["historicalSignificance"] = hs
                details["historicalSignificance"] = hs

        # Append edit log (last 50 entries kept)
        existing_log = details.get("_editLog") or []
        if not isinstance(existing_log, list):
            existing_log = []
        existing_log.extend(edit_log_entries)
        details["_editLog"] = existing_log[-50:]
        details["_unsyncedEdits"] = len(edit_log_entries) > 0 or details.get("_unsyncedEdits", False)

        # Track when this entity was last enriched by a bot (used for velocity stats)
        if edit_log_entries:
            entity["enrichedAt"] = timestamp

        entity["detailsJson"] = json.dumps(details, ensure_ascii=False)
        break

    with open(filepath, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


# ═══════════════════════════════════════════════════════════
# Auto Audit Log
# ═══════════════════════════════════════════════════════════

AUDIT_LOG = "docs/governance/backend_edit_log.md"


def update_audit_log(run_data):
    """Append enrichment run summary to the governance audit log."""
    if not os.path.exists(AUDIT_LOG):
        return

    ts = run_data["timestamp"]
    model = run_data["model"]
    enriched_list = [
        e for e in run_data.get("entities", []) if e["status"] == "enriched"
    ]
    if not enriched_list:
        return

    slugs = ", ".join(e["slug"] for e in enriched_list[:10])
    if len(enriched_list) > 10:
        slugs += f" ... +{len(enriched_list) - 10} more"

    entry = (
        f"\n### AI Enrichment — {ts}\n\n"
        f"- **Model:** {model}\n"
        f"- **Enriched:** {run_data['enriched']} | "
        f"**Failed:** {run_data['failed']}\n"
        f"- **Entities:** {slugs}\n"
    )

    with open(AUDIT_LOG, "a") as f:
        f.write(entry)

    print(f"Audit log updated: {AUDIT_LOG}")


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
        "--model", choices=["gemini", "openai", "ollama", "github"], default="gemini",
        help="LLM provider: gemini (free, 500 RPD), openai (paid), ollama (local, unlimited), github (free via Copilot/GH token)",
    )
    parser.add_argument(
        "--gemini-model", default="gemini-2.5-flash",
        help="Gemini model name (default: gemini-2.5-flash)",
    )
    parser.add_argument(
        "--openai-model", default="gpt-4o-mini",
        help="OpenAI model name (default: gpt-4o-mini)",
    )
    parser.add_argument(
        "--ollama-model", default="llama3.2:3b",
        help="Ollama model name (default: llama3.2:3b — runs locally, no quota)",
    )
    parser.add_argument(
        "--github-model", default="gpt-4o-mini",
        help="GitHub Models model name (default: gpt-4o-mini — free with Copilot)",
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
        "--min-score", type=float, default=0,
        help="Minimum queue score to process (default: 0)",
    )
    parser.add_argument(
        "--retry", type=int, default=1,
        help="Max retries per entity on LLM/validation failure (default: 1)",
    )
    parser.add_argument(
        "--lenient", action="store_true",
        help="Lower quality thresholds for small models (llama3.2:3b etc). "
             "Accepts: summary>=400c, causes>=1, effects>=1, relationships>=2, subjects>=3.",
    )
    args = parser.parse_args()

    # ── Load API keys ──
    if args.model == "gemini":
        api_key = os.environ.get("GEMINI_API_KEY", "")
        if not api_key and not args.dry_run:
            print("ERROR: Set GEMINI_API_KEY environment variable")
            print("  Get free key: https://aistudio.google.com/apikey")
            sys.exit(1)
    elif args.model == "ollama":
        api_key = ""
        # Verify Ollama is up
        try:
            urllib.request.urlopen(f"{OLLAMA_BASE_ENRICH}/api/tags", timeout=5)
        except Exception:
            print(f"ERROR: Ollama not running at {OLLAMA_BASE_ENRICH}. Start with: ollama serve")
            sys.exit(1)
    elif args.model == "github":
        import subprocess as _sp
        api_key = (os.environ.get("GITHUB_TOKEN") or
                   os.environ.get("GH_TOKEN") or
                   _sp.check_output(["gh", "auth", "token"], text=True).strip())
        if not api_key and not args.dry_run:
            print("ERROR: No GitHub token found. Run: gh auth login")
            sys.exit(1)
    else:
        api_key = os.environ.get("OPENAI_API_KEY", "")
        if not api_key and not args.dry_run:
            print("ERROR: Set OPENAI_API_KEY environment variable")
            sys.exit(1)

    # ── Build dynamic editor ID (identifies this bot run in audit log) ──
    global EDITOR_ID
    model_name = {
        "gemini": args.gemini_model,
        "openai": args.openai_model,
        "ollama": args.ollama_model,
        "github": args.github_model,
    }.get(args.model, args.model)
    EDITOR_ID = build_editor_id(args.model, model_name)
    print(f"Editor ID: {EDITOR_ID}")

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
    report = []

    for i, entry in enumerate(batch):
        slug = entry["slug"]
        filepath = entry["filepath"]
        print(f"\n[{i + 1}/{len(batch)}] {slug} (score={entry.get('score',0)}, {len(entry.get('summary',''))}c)")

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
                elif args.model == "ollama":
                    result = call_ollama(prompt, args.ollama_model)
                elif args.model == "github":
                    result = call_github_models(prompt, api_key, args.github_model)
                else:
                    result = call_openai(prompt, api_key, args.openai_model)

                # Validate
                ok, reason = validate_enrichment(result, lenient=args.lenient)
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

        # Write to local JSON (sync_gateway will push to Appwrite later)
        apply_enrichment(filepath, slug, result)

        enriched += 1
        report.append({
            "slug": slug,
            "status": "enriched",
            "old_len": current_len,
            "new_len": new_len,
        })

        # Rate limiting: Gemini = 4.5s, OpenAI = 1.5s, GitHub Models = 5s, Ollama = 0
        if args.model == "gemini":
            delay = 4.5
        elif args.model == "ollama":
            delay = 0  # local model — run as fast as the hardware allows
        elif args.model == "github":
            delay = 5.0  # ~12 req/min — safe within free tier 15 req/min limit
        else:
            delay = 1.5
        if delay > 0:
            time.sleep(delay)

    # ── Summary ──
    print(f"\n{'=' * 60}")
    print(f"RESULTS: {enriched} enriched, {failed} failed (sync_gateway pushes to Appwrite separately)")
    print(f"{'=' * 60}")

    # Save run report
    os.makedirs(os.path.dirname(REPORT_FILE), exist_ok=True)
    run_data = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "model": args.model,
        "count_requested": args.count,
        "enriched": enriched,
        "failed": failed,
        "dry_run": args.dry_run,
        "entities": report,
    }
    with open(REPORT_FILE, "w") as f:
        json.dump(run_data, f, indent=2)
        f.write("\n")
    print(f"Report: {REPORT_FILE}")

    # Auto-update audit log
    if not args.dry_run and enriched > 0:
        update_audit_log(run_data)


if __name__ == "__main__":
    main()
