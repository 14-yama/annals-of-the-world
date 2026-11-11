#!/usr/bin/env python3
"""
Reusable Composer enrichment apply harness.

Reads claim meta JSON + enrichment payloads JSON, writes via
ai_enrich_autonomous.apply_enrichment, updates run logs / audit log,
releases claims. Does NOT touch Ollama slots.
"""
from __future__ import annotations

import argparse
import json
import socket
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import ai_enrich_autonomous as enrich  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--claims", required=True, help="Claim meta JSON path")
    ap.add_argument("--payloads", required=True, help="Enrichment payloads JSON {slug: payload}")
    ap.add_argument("--session-id", required=True)
    ap.add_argument("--report", default=str(ROOT / "data/enrichment/composer_agent_run.json"))
    args = ap.parse_args()

    editor_id = f"composer·local·{socket.gethostname()}"
    enrich.EDITOR_ID = editor_id

    claims_meta = json.loads(Path(args.claims).read_text())
    claimed = {c["slug"]: c for c in claims_meta.get("claimed", [])}
    payloads = json.loads(Path(args.payloads).read_text())

    ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    results = []
    enriched = failed = skipped = 0

    for slug, payload in payloads.items():
        info = claimed.get(slug)
        if not info:
            print(f"SKIP {slug}: not in claim meta")
            skipped += 1
            results.append({"slug": slug, "status": "skipped", "reason": "not_claimed"})
            continue

        filepath = ROOT / info["filepath"]
        with open(filepath) as f:
            data = json.load(f)
        entity = next(e for e in data["entities"] if e.get("slug") == slug)
        old_len = len(entity.get("summary") or "")
        if old_len >= 800:
            print(f"SKIP {slug}: already {old_len}c")
            enrich.release_claim_slug(slug)
            skipped += 1
            results.append({"slug": slug, "status": "skipped", "old_len": old_len, "reason": "already_enriched"})
            continue

        ok, reason = enrich.validate_enrichment(payload, lenient=False)
        if not ok:
            ok, reason = enrich.validate_enrichment(payload, lenient=True)
        if not ok:
            print(f"FAIL {slug}: validation {reason}")
            failed += 1
            results.append({"slug": slug, "status": "failed", "old_len": old_len, "reason": reason})
            enrich.release_claim_slug(slug)
            continue

        enrich.apply_enrichment(str(filepath), slug, payload)
        new_len = len(payload["summary"])
        print(f"OK   {slug}: {old_len} → {new_len}")
        enriched += 1
        results.append({"slug": slug, "status": "enriched", "old_len": old_len, "new_len": new_len})
        enrich.release_claim_slug(slug)

    # Release any claims we held but did not process
    for slug in claimed:
        if slug not in payloads:
            enrich.release_claim_slug(slug)

    run = {
        "timestamp": ts,
        "model": editor_id,
        "sessionId": args.session_id,
        "count_requested": len(payloads),
        "enriched": enriched,
        "failed": failed,
        "skipped": skipped,
        "dry_run": False,
        "entities": results,
        "note": "Composer/agent batch; no Ollama. Wrote via ai_enrich_autonomous.apply_enrichment.",
    }
    report_path = Path(args.report)
    report_path.write_text(json.dumps(run, indent=2) + "\n")
    (ROOT / "data/enrichment/last_run.json").write_text(json.dumps(run, indent=2) + "\n")
    enrich.update_audit_log(run)
    print(f"\nDONE enriched={enriched} failed={failed} skipped={skipped}")
    print(f"Report: {report_path}")


if __name__ == "__main__":
    main()
