#!/usr/bin/env python3
"""
audit_enrichment.py — Comprehensive enrichment audit across ALL entity files.

Scans data/appwrite-export/entities/ (all JSON files) without any Appwrite
read limits. Counts enriched vs stubs by class, division, and label.
Writes result to data/governance/enrichment_audit.json.

The push_enrichment_audit.ts script then syncs that JSON to the
`enrichment_audit` Appwrite collection (single document, updated in-place).

Usage:
    python3 scripts/audit_enrichment.py
    python3 scripts/audit_enrichment.py --verbose
"""
import json, os, sys, time
from pathlib import Path
from datetime import datetime, timezone, timedelta

ROOT = Path(__file__).parent.parent
ENTITIES_DIR = ROOT / "data" / "appwrite-export" / "entities"
OUTPUT_FILE  = ROOT / "data" / "governance" / "enrichment_audit.json"

VERBOSE = "--verbose" in sys.argv

# ── Enrichment thresholds ──────────────────────────────────────────────────
STUB_MAX_LEN   = 100    # summary < 100 chars → stub
WEAK_MAX_LEN   = 599    # 100–599 chars → weak
ENRICHED_MIN   = 600    # ≥ 600 chars → enriched
HQ_SUMMARY_MIN = 600    # high-quality requires summary ≥ 600

def min_edges_for_score(score: int) -> int:
    if score >= 9: return 15
    if score >= 7: return 8
    if score >= 5: return 4
    if score >= 3: return 2
    return 1

def classify_entity(entity: dict) -> dict:
    """Return enrichment classification for one entity dict."""
    summary = entity.get("summary", "") or ""
    if isinstance(summary, list):
        summary = " ".join(str(s) for s in summary)
    summary = str(summary)
    slen = len(summary.strip())

    det = {}
    try:
        raw_dj = entity.get("detailsJson", "") or ""
        if raw_dj:
            det = json.loads(raw_dj)
    except Exception:
        pass

    causes        = det.get("causes", []) or []
    effects       = det.get("effects", []) or []
    relationships = det.get("relationships", []) or []
    places        = det.get("places", []) or []
    texts         = det.get("texts", []) or []
    frameworks    = entity.get("frameworks", []) or []
    significance  = entity.get("historicalSignificance")

    has_summary     = slen >= ENRICHED_MIN
    has_causes      = len(causes) >= 1
    has_effects     = len(effects) >= 1
    has_edges       = len(relationships) >= 1
    has_places      = len(places) >= 1
    has_frameworks  = len(frameworks) >= 1
    has_significance = bool(significance)

    is_stub     = slen < STUB_MAX_LEN
    is_weak     = STUB_MAX_LEN <= slen < ENRICHED_MIN
    is_enriched = slen >= ENRICHED_MIN
    is_hq = (
        slen >= HQ_SUMMARY_MIN and
        len(causes) >= 1 and
        len(effects) >= 1 and
        len(relationships) >= 3 and
        bool(significance)
    )

    # Low-edge detection: enriched entity with significance but too few relationships
    low_edges = False
    sig_score = 0
    if significance and isinstance(significance, dict):
        sig_score = significance.get("significanceScore", 0) or 0
    elif significance:
        sig_score = 0
    if is_enriched and sig_score > 0:
        min_e = min_edges_for_score(sig_score)
        if len(relationships) < min_e:
            low_edges = True

    return {
        "is_stub": is_stub,
        "is_weak": is_weak,
        "is_enriched": is_enriched,
        "is_hq": is_hq,
        "low_edges": low_edges,
        "sig_score": sig_score,
        "has_summary": has_summary,
        "has_causes": has_causes,
        "has_effects": has_effects,
        "has_edges": has_edges,
        "has_places": has_places,
        "has_frameworks": has_frameworks,
        "has_significance": has_significance,
        "edge_count": len(relationships),
        "summary_len": slen,
        "label": entity.get("label", "Unknown") or "Unknown",
        "call_number": entity.get("callNumber", "") or "",
    }


def empty_bucket() -> dict:
    return {
        "total": 0, "enriched": 0, "highQuality": 0,
        "stubs": 0, "weak": 0, "lowEdges": 0,
        "hasSummary": 0, "hasCauses": 0, "hasEffects": 0,
        "hasEdges": 0, "hasPlaces": 0, "hasFrameworks": 0, "hasSignificance": 0,
    }

def add_to_bucket(bucket: dict, cls: dict):
    bucket["total"]          += 1
    bucket["enriched"]       += 1 if cls["is_enriched"] else 0
    bucket["highQuality"]    += 1 if cls["is_hq"] else 0
    bucket["stubs"]          += 1 if cls["is_stub"] else 0
    bucket["weak"]           += 1 if cls["is_weak"] else 0
    bucket["lowEdges"]       += 1 if cls["low_edges"] else 0
    bucket["hasSummary"]     += 1 if cls["has_summary"] else 0
    bucket["hasCauses"]      += 1 if cls["has_causes"] else 0
    bucket["hasEffects"]     += 1 if cls["has_effects"] else 0
    bucket["hasEdges"]       += 1 if cls["has_edges"] else 0
    bucket["hasPlaces"]      += 1 if cls["has_places"] else 0
    bucket["hasFrameworks"]  += 1 if cls["has_frameworks"] else 0
    bucket["hasSignificance"]+= 1 if cls["has_significance"] else 0


def main():
    start = time.time()
    print(f"Enrichment audit — scanning {ENTITIES_DIR}")

    if not ENTITIES_DIR.exists():
        print(f"ERROR: {ENTITIES_DIR} does not exist")
        sys.exit(1)

    overall   = empty_bucket()
    by_label  : dict[str, dict] = {}
    by_class  : dict[str, dict] = {}  # "0"–"9"
    by_division: dict[str, dict] = {}  # 3-digit prefix e.g. "381"
    sig_dist  : dict[str, int] = {}    # "1"–"10" → count
    total_files = 0
    total_entities = 0

    # Velocity tracking: count entities enriched in each period via enrichedAt field
    now = datetime.now(timezone.utc)
    cutoffs: dict[str, datetime] = {
        "24h":   now - timedelta(hours=24),
        "week":  now - timedelta(days=7),
        "month": now - timedelta(days=30),
    }
    velocity: dict[str, dict] = {
        p: {"entities_enriched": 0, "became_enriched": 0}
        for p in cutoffs
    }

    # Walk all entity JSON files
    for class_dir in sorted(ENTITIES_DIR.iterdir()):
        if not class_dir.is_dir():
            continue
        for fpath in sorted(class_dir.glob("*.json")):
            total_files += 1
            try:
                data = json.loads(fpath.read_text(encoding="utf-8"))
            except Exception as e:
                if VERBOSE:
                    print(f"  SKIP (parse error) {fpath.name}: {e}")
                continue

            entities = data.get("entities", [])
            for entity in entities:
                total_entities += 1
                cls = classify_entity(entity)

                # Overall
                add_to_bucket(overall, cls)

                # By label
                label = cls["label"]
                if label not in by_label:
                    by_label[label] = empty_bucket()
                add_to_bucket(by_label[label], cls)

                # By Dewey class (first digit of callNumber)
                cn = cls["call_number"]
                if cn:
                    class_digit = cn[0] if cn[0].isdigit() else "?"
                    if class_digit not in by_class:
                        by_class[class_digit] = empty_bucket()
                    add_to_bucket(by_class[class_digit], cls)

                    # By division (first 3 digits before the ".")
                    div_part = cn.split(".")[0] if "." in cn else cn[:3]
                    if len(div_part) == 3 and div_part.isdigit():
                        if div_part not in by_division:
                            by_division[div_part] = empty_bucket()
                        add_to_bucket(by_division[div_part], cls)

                # Significance distribution
                sc = cls["sig_score"]
                if sc > 0:
                    key = str(sc)
                    sig_dist[key] = sig_dist.get(key, 0) + 1

                # Velocity tracking — enrichedAt (set by ai_enrich_autonomous.py)
                enriched_at_str = entity.get("enrichedAt", "") or ""
                if enriched_at_str:
                    try:
                        enriched_dt = datetime.fromisoformat(
                            enriched_at_str.replace("Z", "+00:00")
                        )
                        for period, cutoff in cutoffs.items():
                            if enriched_dt >= cutoff:
                                velocity[period]["entities_enriched"] += 1
                                if cls["is_enriched"]:
                                    velocity[period]["became_enriched"] += 1
                    except Exception:
                        pass

        # Progress report every 50 directories
        if total_files % 2000 == 0 and VERBOSE:
            print(f"  … {total_files} files / {total_entities} entities scanned")

    elapsed_ms = int((time.time() - start) * 1000)
    generated_at = datetime.now(timezone.utc).isoformat()

    result = {
        "generatedAt": generated_at,
        "computeTimeMs": elapsed_ms,
        "filesScanned": total_files,
        "total": overall["total"],
        "enriched": overall["enriched"],
        "highQuality": overall["highQuality"],
        "stubs": overall["stubs"],
        "weak": overall["weak"],
        "lowEdges": overall["lowEdges"],
        "fieldCoverage": {
            "hasSummary":      overall["hasSummary"],
            "hasCauses":       overall["hasCauses"],
            "hasEffects":      overall["hasEffects"],
            "hasEdges":        overall["hasEdges"],
            "hasPlaces":       overall["hasPlaces"],
            "hasFrameworks":   overall["hasFrameworks"],
            "hasSignificance": overall["hasSignificance"],
        },
        "byLabel":        by_label,
        "byClass":        by_class,
        "byDivision":     by_division,
        "significanceDist": sig_dist,
        "velocity": velocity,
    }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"\n=== Enrichment Audit Complete ===")
    print(f"  Files scanned : {total_files:,}")
    print(f"  Total entities: {total_entities:,}")
    print(f"  Enriched (≥600c): {overall['enriched']:,} ({100*overall['enriched']//max(1,overall['total'])}%)")
    print(f"  High quality    : {overall['highQuality']:,} ({100*overall['highQuality']//max(1,overall['total'])}%)")
    print(f"  Weak (100-599c) : {overall['weak']:,}")
    print(f"  Stubs (<100c)   : {overall['stubs']:,} ({100*overall['stubs']//max(1,overall['total'])}%)")
    print(f"  Low edges       : {overall['lowEdges']:,}")
    print(f"  Time: {elapsed_ms}ms")
    print(f"  Output: {OUTPUT_FILE}")
    print(f"\n  Velocity (by enrichedAt field):")
    for period, v in velocity.items():
        print(f"    {period}: {v['entities_enriched']:,} entities touched, {v['became_enriched']:,} now enriched")

    # Print by-label breakdown
    print(f"\n  By Label:")
    for lbl, b in sorted(by_label.items(), key=lambda x: -x[1]["total"]):
        e_pct = 100*b["enriched"]//max(1,b["total"])
        print(f"    {lbl:20s} total={b['total']:6,}  enriched={b['enriched']:6,} ({e_pct:3d}%)  stubs={b['stubs']:6,}")


if __name__ == "__main__":
    main()
