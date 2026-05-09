#!/usr/bin/env python3
"""
AI Edge Bot — git-first relationship (edge) generator.

Reads enriched entities from data/appwrite-export/entities/, uses their
historicalSignificance scores to prioritise high-impact entities, then calls
Gemini to propose meaningful directed edges between entity pairs that share
the same era/region but don't already have an edge recorded.

Also extracts already-proposed relationships from detailsJson.relationships
and promotes them into standalone edge records.

Output:
  data/appwrite-export/edges/YYYY-MM-DD.json   — new edge records
  data/enrichment/edge_run.json                — run report

Edge record schema (matches Appwrite 'relationships' collection):
  {
    "$id":        "<sourceSlug>|<verb>|<targetSlug>",
    "entitySlug": "<sourceSlug>",
    "sourceSlug": "<sourceSlug>",
    "sourceName": "<source display name>",
    "verb":       "<CAUSES|INFLUENCES|...>",
    "targetSlug": "<targetSlug>",
    "targetName": "<target display name>",
    "context":    "<one-sentence description>"
  }

Usage:
    python3 scripts/ai_edge_bot.py --count 40
    python3 scripts/ai_edge_bot.py --count 20 --min-significance 6
    python3 scripts/ai_edge_bot.py --dry-run --count 10
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
from datetime import datetime, timezone

REPO_ROOT    = Path(__file__).resolve().parent.parent
ENTITIES_DIR = REPO_ROOT / "data" / "appwrite-export" / "entities"
EDGES_DIR    = REPO_ROOT / "data" / "appwrite-export" / "edges"
REPORT_FILE  = REPO_ROOT / "data" / "enrichment" / "edge_run.json"
DASH_REPORT  = REPO_ROOT / "data" / "audit-reports" / "edge_run.json"

EDITOR_ID = "ai-edge-bot:gemini"

VALID_VERBS = [
    "CAUSES", "INFLUENCES", "COLLABORATES_WITH", "PARTICIPATES_IN",
    "CREATES", "OCCURS_IN", "FRAMES", "DEFINES", "TRANSFORMS",
    "TRANSMITS", "SUCCEEDS", "CONTAINS", "OCCURS_DURING", "CANONIZES",
    "COMMANDS", "OPPOSES", "FUNDS", "LEADS", "REPORTS", "PUBLISHES",
    "INTERFACES_WITH",
]

PROMPT = """\
You are a historical knowledge graph edge generator for "Annals of the World."

## Task
Generate meaningful DIRECTED historical edges between these two entities.
Each edge represents a verifiable, specific historical relationship.

## Entity A
- Name: {name_a}
- Era: {era_a}
- Summary: {summary_a}

## Entity B
- Name: {name_b}
- Era: {era_b}
- Summary: {summary_b}

## Instructions
Propose 2–4 directed edges. Each edge must:
1. Be historically defensible with a specific, named consequence or interaction
2. Use only these verbs: {valid_verbs}
3. Have direction: source → target reflects WHO acted on WHOM
4. Context sentence must include a date or specific event reference

Return ONLY a JSON array (no markdown):
[
  {{
    "sourceSlug": "{slug_a}",
    "sourceName": "{name_a}",
    "verb": "CAUSES",
    "targetSlug": "{slug_b}",
    "targetName": "{name_b}",
    "context": "..."
  }}
]

Direction rule: source is the ACTOR/CAUSE, target is the RECIPIENT/EFFECT.
If no meaningful edges exist, return an empty array []."""


def load_dotenv():
    env_path = REPO_ROOT / ".env"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#') or '=' not in line:
                    continue
                k, _, v = line.partition('=')
                k = k.strip(); v = v.strip()
                if k and k not in os.environ:
                    os.environ[k] = v


def _parse_llm_json(text: str):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        s = text.find('[')
        e = text.rfind(']')
        if s >= 0 and e > s:
            return json.loads(text[s:e+1])
        raise


def call_gemini(prompt: str, api_key: str) -> list:
    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        "gemini-2.5-flash:generateContent?key=" + api_key
    )
    body = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.4,
            "maxOutputTokens": 1024,
            "responseMimeType": "application/json",
        },
    }).encode()
    req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"})
    for backoff in [0, 20, 45]:
        if backoff:
            print(f"    Rate limited — waiting {backoff}s...")
            time.sleep(backoff)
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.loads(resp.read())
            text = data["candidates"][0]["content"]["parts"][0]["text"]
            result = _parse_llm_json(text)
            return result if isinstance(result, list) else []
        except urllib.error.HTTPError as e:
            if e.code in (429, 503):
                continue
            raise
    raise RuntimeError("Gemini API exhausted retries")


def load_entities() -> dict[str, dict]:
    """Load all enriched entities indexed by slug."""
    index: dict[str, dict] = {}
    for path in ENTITIES_DIR.rglob("*.json"):
        try:
            data = json.load(open(path))
            for ent in data.get("entities", []):
                slug = ent.get("slug", "")
                if slug:
                    ent["_filepath"] = str(path)
                    index[slug] = ent
        except Exception:
            continue
    return index


def get_significance(ent: dict) -> int:
    """Return significanceScore from entity or detailsJson."""
    hs = ent.get("historicalSignificance")
    if isinstance(hs, dict):
        return int(hs.get("significanceScore", 0) or 0)
    # Fall back to importanceScore
    return int(ent.get("importanceScore") or 0)


def extract_proposed_edges(
    entity_index: dict[str, dict],
    min_importance: int = 6,
    max_per_run: int = 2000,
) -> list[dict]:
    """
    Extract relationships already proposed in detailsJson.relationships where
    BOTH endpoints exist in our index AND source entity has sufficient importance.
    Limited to max_per_run to keep file sizes git-friendly.
    """
    edges = []
    seen_keys: set[str] = set()

    # Sort entities by importance so we extract high-value edges first
    sorted_entities = sorted(
        entity_index.values(),
        key=lambda e: -int(e.get("importanceScore") or 0),
    )

    for ent in sorted_entities:
        if len(edges) >= max_per_run:
            break
        imp = int(ent.get("importanceScore") or 0)
        if imp < min_importance:
            continue  # skip low-importance stubs
        slug = ent.get("slug", "")
        dj_raw = ent.get("detailsJson", "") or ""
        if not dj_raw:
            continue
        try:
            dj = json.loads(dj_raw)
        except Exception:
            continue

        for rel in dj.get("relationships", []):
            src = rel.get("sourceSlug", "")
            verb = rel.get("verb", "")
            tgt = rel.get("targetSlug", "")
            if not (src and verb and tgt):
                continue
            if verb not in VALID_VERBS:
                continue
            # Only promote if at least one end exists in our entity index
            if tgt not in entity_index and src not in entity_index:
                continue
            key = f"{src}|{verb}|{tgt}"
            if key in seen_keys:
                continue
            seen_keys.add(key)
            edges.append({
                "$id": key,
                "entitySlug": slug,
                "sourceSlug": src,
                "sourceName": rel.get("sourceName", src),
                "verb": verb,
                "targetSlug": tgt,
                "targetName": rel.get("targetName", tgt),
                "context": rel.get("context", ""),
                "_source": "detailsJson",
            })
            if len(edges) >= max_per_run:
                break

    return edges


def build_candidate_pairs(
    entity_index: dict[str, dict],
    existing_edge_keys: set[str],
    min_significance: int,
    limit: int,
) -> list[tuple[dict, dict]]:
    """
    Find pairs of high-significance entities in the same era that don't
    already have an edge between them — these are Gemini discovery targets.
    """
    # Bucket by era
    by_era: dict[str, list[dict]] = {}
    for ent in entity_index.values():
        summary = ent.get("summary", "") or ""
        if len(summary) < 600:
            continue
        sig = get_significance(ent)
        if sig < min_significance:
            continue
        era = ent.get("era", "unknown")
        by_era.setdefault(era, []).append(ent)

    pairs = []
    for era, ents in by_era.items():
        # Sort by significance desc
        ents.sort(key=lambda e: -get_significance(e))
        top = ents[:20]  # top 20 per era
        # Generate pairs from top entities
        for i, a in enumerate(top):
            for b in top[i+1:]:
                slug_a = a.get("slug", "")
                slug_b = b.get("slug", "")
                if not slug_a or not slug_b:
                    continue
                # Skip if already have an edge either direction
                if any(
                    f"{slug_a}|{v}|{slug_b}" in existing_edge_keys or
                    f"{slug_b}|{v}|{slug_a}" in existing_edge_keys
                    for v in VALID_VERBS
                ):
                    continue
                pairs.append((a, b))
                if len(pairs) >= limit:
                    return pairs
    return pairs


def load_existing_edge_keys() -> set[str]:
    """Load all edge $id keys already recorded in data/appwrite-export/edges/."""
    keys: set[str] = set()
    if not EDGES_DIR.exists():
        return keys
    for path in EDGES_DIR.glob("*.json"):
        try:
            data = json.load(open(path))
            for edge in data.get("edges", []):
                key = edge.get("$id", "")
                if key:
                    keys.add(key)
        except Exception:
            continue
    return keys


def validate_edge(edge: dict) -> tuple[bool, str]:
    for field in ("sourceSlug", "verb", "targetSlug"):
        if not edge.get(field):
            return False, f"missing {field}"
    if edge["verb"] not in VALID_VERBS:
        return False, f"invalid verb: {edge['verb']!r}"
    if not edge.get("context"):
        return False, "empty context"
    return True, "ok"


def save_edges(edges: list[dict], dry_run: bool) -> str:
    """Write edges to dated JSON file. Returns filepath."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    out_path = EDGES_DIR / f"edges_{today}.json"
    EDGES_DIR.mkdir(parents=True, exist_ok=True)

    # Merge with existing file for today if present
    existing = []
    if out_path.exists():
        try:
            d = json.load(open(out_path))
            existing = d.get("edges", [])
        except Exception:
            pass

    existing_keys = {e.get("$id") for e in existing}
    new_edges = [e for e in edges if e.get("$id") not in existing_keys]

    all_edges = existing + new_edges
    if not dry_run:
        with open(out_path, "w") as f:
            json.dump({
                "generatedAt": datetime.now(timezone.utc).isoformat(),
                "editorId": EDITOR_ID,
                "edges": all_edges,
                "_unsyncedEdits": True,
            }, f, indent=2, ensure_ascii=False)
            f.write("\n")
    return str(out_path)


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="AI Edge Bot — generates entity relationship edges")
    parser.add_argument("--count", type=int, default=40, help="Max Gemini-generated edge pairs to attempt")
    parser.add_argument("--min-significance", type=int, default=5, help="Min significanceScore for Gemini pairs")
    parser.add_argument("--extract-only", action="store_true", help="Only extract from detailsJson, skip Gemini")
    parser.add_argument("--dry-run", action="store_true", help="Preview — no file changes")
    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY", "")
    if not api_key and not args.extract_only and not args.dry_run:
        print("ERROR: GEMINI_API_KEY not set (pass --extract-only for no-LLM mode)", file=sys.stderr)
        sys.exit(1)

    print("=" * 60)
    print(f"AI EDGE BOT — up to {args.count} pairs via Gemini")
    if args.extract_only:
        print("  MODE: extract-only (no Gemini calls)")
    if args.dry_run:
        print("  DRY RUN — no files written")
    print("=" * 60)

    print("\nLoading entity index...")
    entity_index = load_entities()
    print(f"Loaded {len(entity_index):,} entities")

    existing_keys = load_existing_edge_keys()
    print(f"Existing edge records: {len(existing_keys):,}")

    # Phase 1: Extract free edges from detailsJson
    print("\n[Phase 1] Extracting proposed edges from detailsJson...")
    proposed = extract_proposed_edges(entity_index, min_importance=6, max_per_run=min(args.count * 5, 2000))
    new_proposed = [e for e in proposed if e["$id"] not in existing_keys]
    print(f"  Found {len(proposed):,} proposed edges → {len(new_proposed):,} new")

    all_new_edges = list(new_proposed)
    edge_keys_this_run: set[str] = {e["$id"] for e in new_proposed}

    # Phase 2: Gemini cross-entity discovery
    gemini_generated = 0
    gemini_failed = 0

    if not args.extract_only and api_key:
        print(f"\n[Phase 2] Gemini cross-entity discovery (min_significance={args.min_significance})...")
        all_existing = existing_keys | edge_keys_this_run
        pairs = build_candidate_pairs(entity_index, all_existing, args.min_significance, args.count)
        print(f"  Candidate pairs: {len(pairs)}")

        for i, (ent_a, ent_b) in enumerate(pairs):
            slug_a = ent_a.get("slug", "")
            slug_b = ent_b.get("slug", "")
            sig_a = get_significance(ent_a)
            sig_b = get_significance(ent_b)
            era = ent_a.get("era", "")
            print(f"\n  [{i+1}/{len(pairs)}] {slug_a} × {slug_b} (sig {sig_a}/{sig_b}, {era})")

            prompt = PROMPT.format(
                slug_a=slug_a,
                name_a=ent_a.get("name", slug_a),
                era_a=ent_a.get("era", ""),
                summary_a=(ent_a.get("summary", "") or "")[:400],
                slug_b=slug_b,
                name_b=ent_b.get("name", slug_b),
                era_b=ent_b.get("era", ""),
                summary_b=(ent_b.get("summary", "") or "")[:400],
                valid_verbs=", ".join(VALID_VERBS),
            )

            try:
                raw_edges = call_gemini(prompt, api_key)
                accepted = 0
                for edge in raw_edges:
                    if not isinstance(edge, dict):
                        continue
                    # Fill in entitySlug
                    src = edge.get("sourceSlug", slug_a)
                    verb = edge.get("verb", "")
                    tgt = edge.get("targetSlug", slug_b)
                    key = f"{src}|{verb}|{tgt}"

                    ok, reason = validate_edge(edge)
                    if not ok:
                        print(f"    skip: {reason}")
                        continue
                    if key in edge_keys_this_run or key in existing_keys:
                        continue

                    edge["$id"] = key
                    edge["entitySlug"] = src
                    edge["_source"] = "gemini"
                    all_new_edges.append(edge)
                    edge_keys_this_run.add(key)
                    accepted += 1
                    gemini_generated += 1

                print(f"    → {accepted} edges accepted ({len(raw_edges)} proposed)")

            except Exception as e:
                print(f"    ERROR: {e}")
                gemini_failed += 1

            # Rate limit: 15 RPM free tier
            if i < len(pairs) - 1:
                time.sleep(4)

    # Save
    if all_new_edges:
        out_path = save_edges(all_new_edges, args.dry_run)
        print(f"\nSaved {len(all_new_edges)} edges to {out_path}")
    else:
        print("\nNo new edges to write.")

    # Report
    report = {
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "model": "gemini-2.5-flash",
        "count_requested": args.count,
        "extracted_from_detailsJson": len(new_proposed),
        "gemini_generated": gemini_generated,
        "gemini_failed": gemini_failed,
        "total_new_edges": len(all_new_edges),
        "dry_run": args.dry_run,
        "summary": {
            "new_edges": len(all_new_edges),
            "from_detailsJson": len(new_proposed),
            "from_gemini": gemini_generated,
        },
    }
    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not args.dry_run:
        with open(REPORT_FILE, "w") as f:
            json.dump(report, f, indent=2)
        # Also write to audit-reports/ so the dashboard can pick it up
        dash = {
            "generatedAt": report["generatedAt"],
            "summary": report["summary"],
        }
        DASH_REPORT.parent.mkdir(parents=True, exist_ok=True)
        with open(DASH_REPORT, "w") as f:
            json.dump(dash, f, indent=2)

    print("\n" + "=" * 60)
    print(f"RESULTS: {len(all_new_edges)} new edges ({len(new_proposed)} extracted, {gemini_generated} from Gemini)")
    print("=" * 60)
    print(f"Report: {REPORT_FILE}")


if __name__ == "__main__":
    main()
