"""
run_pipeline.py — Orchestrate the triage → enrich → validate gates.

Modes:
    triage        — run gate_triage only
    validate      — run gate_validate only (promotes ready entities to clean)
    enrich        — run gate_enrich once (one LLM batch)
    full          — triage → enrich → validate (one cycle)
    loop          — full, repeated N times (or until KPI target reached)
    status        — print KPI dashboard from existing reports

Examples:
    python3 scripts/pipeline/run_pipeline.py triage
    python3 scripts/pipeline/run_pipeline.py full --count 25 --model gemini
    python3 scripts/pipeline/run_pipeline.py loop --cycles 5 --count 50
    python3 scripts/pipeline/run_pipeline.py status
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from scripts.pipeline.pipeline_state import REPO_ROOT, _now, _atomic_write  # noqa: E402
from scripts.pipeline import gate_triage, gate_enrich, gate_validate  # noqa: E402

PIPELINE_DIR = REPO_ROOT / "data" / "pipeline"
STATUS_FILE = PIPELINE_DIR / "pipeline_status.json"


def _load_report(name: str) -> dict:
    path = PIPELINE_DIR / f"{name}_report.json"
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text())
    except Exception:
        return {}


def _count_clean() -> int:
    clean_dir = PIPELINE_DIR / "clean"
    if not clean_dir.exists():
        return 0
    return sum(1 for _ in clean_dir.rglob("*.json"))


def _count_rejected() -> int:
    rej_dir = PIPELINE_DIR / "rejected"
    if not rej_dir.exists():
        return 0
    return sum(1 for _ in rej_dir.rglob("*.json"))


def cmd_status() -> dict:
    triage = _load_report("triage")
    validate = _load_report("validate")
    enrich = _load_report("enrich")
    status = {
        "generatedAt": _now(),
        "clean": _count_clean(),
        "rejected": _count_rejected(),
        "triage": {
            "lastRun": triage.get("generatedAt"),
            "counts": triage.get("counts"),
            "byReason": triage.get("byReason"),
        },
        "validate": {
            "lastRun": validate.get("generatedAt"),
            "counts": validate.get("counts"),
            "byReason": validate.get("byReason"),
        },
        "enrich": {
            "lastRun": enrich.get("generatedAt"),
            "selected": enrich.get("selected"),
            "model": enrich.get("model"),
            "exitCode": enrich.get("enricherExitCode"),
        },
    }
    _atomic_write(STATUS_FILE, status)
    print(json.dumps(status, indent=2))
    return status


def cmd_full(count: int, model: str, dry_run: bool) -> None:
    print("=" * 60)
    print("[pipeline] FULL CYCLE — triage → enrich → validate")
    print("=" * 60)
    print("\n--- STAGE 1: TRIAGE ---")
    gate_triage.run(dry_run=dry_run)
    print("\n--- STAGE 2: ENRICH ---")
    gate_enrich.run(count=count, model=model, dry_run=dry_run)
    print("\n--- STAGE 3: VALIDATE ---")
    gate_validate.run(dry_run=dry_run)
    print("\n--- STATUS ---")
    cmd_status()


def cmd_loop(cycles: int, count: int, model: str, target_clean: int | None) -> None:
    for i in range(1, cycles + 1):
        print(f"\n{'#' * 60}\n# CYCLE {i}/{cycles}\n{'#' * 60}")
        cmd_full(count=count, model=model, dry_run=False)
        clean = _count_clean()
        if target_clean and clean >= target_clean:
            print(f"\n[pipeline] target reached: {clean} >= {target_clean}, stopping loop")
            return
        time.sleep(2)


def main():
    p = argparse.ArgumentParser(description="Pipeline orchestrator")
    sub = p.add_subparsers(dest="mode", required=True)

    sub.add_parser("triage")
    sub.add_parser("validate")
    sub.add_parser("status")

    pe = sub.add_parser("enrich")
    pe.add_argument("--count", type=int, default=25)
    pe.add_argument("--model", default="gemini", choices=["gemini", "openai", "ollama"])
    pe.add_argument("--dry-run", action="store_true")

    pf = sub.add_parser("full")
    pf.add_argument("--count", type=int, default=25)
    pf.add_argument("--model", default="gemini", choices=["gemini", "openai", "ollama"])
    pf.add_argument("--dry-run", action="store_true")

    pl = sub.add_parser("loop")
    pl.add_argument("--cycles", type=int, default=5)
    pl.add_argument("--count", type=int, default=25)
    pl.add_argument("--model", default="gemini", choices=["gemini", "openai", "ollama"])
    pl.add_argument("--target-clean", type=int, default=None,
                    help="Stop loop early if clean count reaches this")

    args = p.parse_args()
    if args.mode == "triage":
        gate_triage.run()
    elif args.mode == "validate":
        gate_validate.run()
    elif args.mode == "status":
        cmd_status()
    elif args.mode == "enrich":
        gate_enrich.run(count=args.count, model=args.model, dry_run=args.dry_run)
    elif args.mode == "full":
        cmd_full(count=args.count, model=args.model, dry_run=args.dry_run)
    elif args.mode == "loop":
        cmd_loop(cycles=args.cycles, count=args.count, model=args.model,
                 target_clean=args.target_clean)


if __name__ == "__main__":
    main()
