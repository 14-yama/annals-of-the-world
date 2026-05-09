#!/usr/bin/env python3
"""
Backfill Historical Significance — git-first bot.

Adds `historicalSignificance` to entities that have a rich summary (≥600c)
but are missing the significance rating. Calls Gemini to score:
  - significanceScore: 1–10
  - significanceNarrative: 1–2 sentence explanation
  - significanceCategory: world-changing | continental | regional | local

Writes JSON changes to the local repo only. sync_gateway pushes to Appwrite.

Usage:
    python3 scripts/backfill_significance.py --count 50
    python3 scripts/backfill_significance.py --count 10 --dry-run
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ENTITIES_DIR = REPO_ROOT / "data" / "appwrite-export" / "entities"
REPORT_FILE  = REPO_ROOT / "data" / "enrichment" / "significance_run.json"
DASH_REPORT  = REPO_ROOT / "data" / "audit-reports" / "significance_run.json"

EDITOR_ID = "backfill-significance-bot:gemini"

CATEGORIES = ["world-changing", "continental", "regional", "local"]

PROMPT = """\
You are a historical significance evaluator for "Annals of the World," a scholarly knowledge graph.

## Entity
- Name: {name}
- Label: {label}
- Era: {era}
- Region: {region}
- Summary: {summary}

## Task
Rate this entity's historical importance and return ONLY a valid JSON object:

{{
  "significanceScore": <integer 1-10>,
  "significanceNarrative": "<1-2 sentence specific explanation of why it matters, with real consequences/numbers>",
  "significanceCategory": "<exactly one of: world-changing | continental | regional | local>"
}}

## Score Guidelines
- 10: Changed entire trajectory of human civilization (e.g. Islam, printing press, French Revolution)
- 8-9: Shaped a continent or defined a major era (Napoleon, Mongol Empire, Black Death)
- 6-7: Significant regional or thematic impact (important battle, major inventor, key institution)
- 4-5: Notable but limited scope (secondary ruler, regional movement, specialist text)
- 1-3: Local or minor interest only

Rules:
- Be honest and calibrated — most entities score 4-6
- The narrative MUST be specific: name real consequences, numbers, or successor events
- Return ONLY the JSON object, no markdown, no explanation"""


def load_dotenv():
    env_path = REPO_ROOT / ".env"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#') or '=' not in line:
                    continue
                key, _, val = line.partition('=')
                key = key.strip(); val = val.strip()
                if key and key not in os.environ:
                    os.environ[key] = val


def _parse_llm_json(text: str) -> dict:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Try extracting JSON block
        s = text.find('{')
        e = text.rfind('}')
        if s >= 0 and e > s:
            return json.loads(text[s:e+1])
        raise


def call_gemini(prompt: str, api_key: str) -> dict:
    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"gemini-2.5-flash:generateContent?key={api_key}"
    )
    body = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.3,
            "maxOutputTokens": 512,
            "responseMimeType": "application/json",
        },
    }).encode()
    req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"})
    for backoff in [0, 15, 30, 60]:
        if backoff:
            print(f"    Rate limited — waiting {backoff}s...")
            time.sleep(backoff)
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.loads(resp.read())
            text = data["candidates"][0]["content"]["parts"][0]["text"]
            return _parse_llm_json(text)
        except urllib.error.HTTPError as e:
            if e.code in (429, 503):
                continue
            raise
    raise RuntimeError("Gemini API exhausted retries")


OLLAMA_BASE = os.environ.get("OLLAMA_HOST", "http://localhost:11434")

def call_ollama(prompt: str, model: str = "llama3.2:3b") -> dict:
    """Call local Ollama for unlimited, quota-free inference."""
    url = f"{OLLAMA_BASE}/api/generate"
    body = json.dumps({
        "model": model,
        "prompt": prompt,
        "format": "json",
        "stream": False,
        "options": {"temperature": 0.3, "num_predict": 512},
    }).encode()
    req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read())
        text = data.get("response", "")
        return _parse_llm_json(text)
    except Exception as e:
        raise RuntimeError(f"Ollama error: {e}") from e


def call_llm(prompt: str, model_backend: str, api_key: str = "", ollama_model: str = "llama3.2:3b") -> dict:
    """Unified LLM call — dispatches to Gemini or Ollama."""
    if model_backend == "ollama":
        return call_ollama(prompt, ollama_model)
    return call_gemini(prompt, api_key)


def validate(result: dict) -> tuple[bool, str]:
    score = result.get("significanceScore")
    if not isinstance(score, (int, float)) or not (1 <= int(score) <= 10):
        return False, f"invalid significanceScore: {score!r}"
    narr = result.get("significanceNarrative", "")
    if not isinstance(narr, str) or len(narr) < 40:
        return False, f"narrative too short ({len(narr)}c)"
    cat = result.get("significanceCategory", "")
    if cat not in CATEGORIES:
        return False, f"invalid category: {cat!r}"
    return True, "ok"


def iter_entity_files():
    for path in ENTITIES_DIR.rglob("*.json"):
        yield path


def build_queue(limit: int) -> list[dict]:
    """Find enriched entities missing historicalSignificance, ranked by importanceScore."""
    queue = []
    for path in iter_entity_files():
        try:
            data = json.load(open(path))
        except Exception:
            continue
        entities = data.get("entities", [])
        for ent in entities:
            summary = ent.get("summary", "") or ""
            if len(summary) < 600:
                continue  # skip stubs — not worth rating
            dj = {}
            if ent.get("detailsJson"):
                try:
                    dj = json.loads(ent["detailsJson"])
                except Exception:
                    pass
            # Skip if already has significance
            if ent.get("historicalSignificance") or dj.get("historicalSignificance"):
                continue
            queue.append({
                "slug": ent.get("slug", ""),
                "name": ent.get("name", ent.get("slug", "")),
                "label": ent.get("label", ""),
                "era": ent.get("era", ""),
                "region": ent.get("region", ""),
                "importanceScore": int(ent.get("importanceScore") or 0),
                "summary": summary,
                "filepath": str(path),
            })
    # Rank: highest importanceScore first
    queue.sort(key=lambda x: -x["importanceScore"])
    return queue[:limit]


def apply_significance(entry: dict, result: dict, dry_run: bool) -> bool:
    path = Path(entry["filepath"])
    try:
        data = json.load(open(path))
    except Exception as e:
        print(f"    ERROR reading {path}: {e}")
        return False

    changed = False
    for ent in data.get("entities", []):
        if ent.get("slug") != entry["slug"]:
            continue
        hs = {
            "significanceScore": int(result["significanceScore"]),
            "significanceNarrative": result["significanceNarrative"].strip(),
            "significanceCategory": result["significanceCategory"],
        }
        ent["historicalSignificance"] = hs
        # Also write into detailsJson
        dj = {}
        if ent.get("detailsJson"):
            try:
                dj = json.loads(ent["detailsJson"])
            except Exception:
                pass
        dj["historicalSignificance"] = hs
        # Log the edit
        edit_log = dj.get("_editLog") or []
        if not isinstance(edit_log, list):
            edit_log = []
        edit_log.append({
            "editorId": EDITOR_ID,
            "field": "historicalSignificance",
            "oldValue": "",
            "newValue": json.dumps(hs),
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        })
        dj["_editLog"] = edit_log[-50:]
        dj["_unsyncedEdits"] = True
        ent["detailsJson"] = json.dumps(dj, ensure_ascii=False)
        changed = True
        break

    if changed and not dry_run:
        with open(path, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write("\n")
    return changed


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Backfill historical significance scores")
    parser.add_argument("--count", type=int, default=50, help="Max entities to process")
    parser.add_argument("--dry-run", action="store_true", help="Preview — no file changes")
    parser.add_argument(
        "--model", choices=["gemini", "ollama"], default="gemini",
        help="LLM backend: 'gemini' (cloud, 15 RPM limit) or 'ollama' (local, unlimited)",
    )
    parser.add_argument(
        "--ollama-model", default="llama3.2:3b",
        help="Ollama model name (default: llama3.2:3b). Use llama3.1:8b for higher quality.",
    )
    args = parser.parse_args()

    api_key = ""
    if args.model == "gemini":
        api_key = os.environ.get("GEMINI_API_KEY", "")
        if not api_key:
            print("ERROR: GEMINI_API_KEY not set (or use --model ollama for local AI)", file=sys.stderr)
            sys.exit(1)
    elif args.model == "ollama":
        # Verify Ollama is running
        try:
            urllib.request.urlopen(f"{OLLAMA_BASE}/api/tags", timeout=5)
        except Exception:
            print(f"ERROR: Ollama not running at {OLLAMA_BASE}. Start with: ollama serve", file=sys.stderr)
            sys.exit(1)

    model_label = f"{args.model}{'/' + args.ollama_model if args.model == 'ollama' else ''}"
    print(f"{'='*60}")
    print(f"SIGNIFICANCE BACKFILL — up to {args.count} entities via {model_label}")
    if args.model == "ollama":
        print(f"  LOCAL MODE — no API quota, unlimited speed")
    if args.dry_run:
        print("  DRY RUN — no files will be written")
    print(f"{'='*60}")

    print("Building queue...")
    queue = build_queue(args.count)
    print(f"Found {len(queue)} enriched entities needing significance rating")

    enriched = 0
    failed = 0
    results_log = []

    for i, entry in enumerate(queue):
        slug = entry["slug"]
        print(f"\n[{i+1}/{len(queue)}] {slug} (importance={entry['importanceScore']})")

        prompt = PROMPT.format(
            name=entry["name"],
            label=entry["label"],
            era=entry["era"],
            region=entry["region"],
            summary=entry["summary"][:800],  # cap for token efficiency
        )

        try:
            result = call_llm(prompt, args.model, api_key, args.ollama_model)
            ok, reason = validate(result)
            if not ok:
                print(f"  REJECTED — {reason}")
                failed += 1
                results_log.append({"slug": slug, "status": "rejected", "reason": reason})
                continue

            if apply_significance(entry, result, args.dry_run):
                score = result["significanceScore"]
                cat = result["significanceCategory"]
                print(f"  SCORED — {score}/10 ({cat}): {result['significanceNarrative'][:80]}...")
                enriched += 1
                results_log.append({"slug": slug, "status": "ok", "score": score, "category": cat})
            else:
                print(f"  SKIPPED — entity not found in file")
                failed += 1

        except Exception as e:
            print(f"  ERROR — {e}")
            failed += 1
            results_log.append({"slug": slug, "status": "error", "reason": str(e)})

        # Rate limiting: Gemini = 4s, Ollama = no wait (local, no quota)
        if args.model == "gemini" and i < len(queue) - 1:
            time.sleep(4)

    print(f"\n{'='*60}")
    print(f"RESULTS: {enriched} scored, {failed} failed")
    print(f"{'='*60}")

    # Write report
    report = {
        "generatedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "model": "gemini-2.5-flash",
        "count_requested": args.count,
        "enriched": enriched,
        "failed": failed,
        "dry_run": args.dry_run,
        "results": results_log,
        "summary": {
            "entities_scored": enriched,
            "failed": failed,
        },
    }
    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(REPORT_FILE, "w") as f:
        json.dump(report, f, indent=2)
    # Mirror to audit-reports/ so the dashboard can pick it up
    dash = {"generatedAt": report["generatedAt"], "summary": report["summary"]}
    DASH_REPORT.parent.mkdir(parents=True, exist_ok=True)
    with open(DASH_REPORT, "w") as f:
        json.dump(dash, f, indent=2)
    print(f"Report: {REPORT_FILE}")


if __name__ == "__main__":
    main()
