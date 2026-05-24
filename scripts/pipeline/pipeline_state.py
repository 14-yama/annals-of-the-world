"""
pipeline_state.py — Single source of truth for per-entity pipeline state.

State machine:
    pending     → never processed by any gate
    triaged     → passed triage gate, waiting for enrich
    in-flight   → enrich gate currently working on it (or about to retry)
    validated   → passed validate gate, written to entities_clean
    rejected    → failed any gate; reason recorded

State lives in two places:
1. Each entity JSON file gets `_pipelineState: { state, attempts, lastGate, lastReason, updatedAt }`
2. `data/governance/pipeline_state.json` aggregate counters (fast dashboard reads)

File locking via `fcntl` prevents two bots from picking the same entity.
"""
from __future__ import annotations

import fcntl
import json
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
ENTITIES_DIR = REPO_ROOT / "data" / "appwrite-export" / "entities"
STATE_FILE = REPO_ROOT / "data" / "governance" / "pipeline_state.json"
CLEAN_DIR = REPO_ROOT / "data" / "pipeline" / "clean"
REJECTED_DIR = REPO_ROOT / "data" / "pipeline" / "rejected"

VALID_STATES = {"pending", "triaged", "in-flight", "validated", "rejected"}


@dataclass
class EntityRecord:
    """Lightweight view of one entity from disk."""
    file_path: Path
    slug: str
    label: str
    name: str
    summary: str
    importance_score: int
    wikidata_qid: str | None
    details: dict
    pipeline_state: dict  # _pipelineState sub-object
    raw: dict             # full entity dict for mutation
    container: dict       # the file's top-level dict for writing back
    index_in_file: int    # which entity slot in container['entities']


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _safe_load(path: Path) -> dict | None:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return None


def _atomic_write(path: Path, data: dict) -> None:
    """Write JSON to a tmp file then rename — avoids partial writes if killed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, path)


def iter_entities(state_filter: set[str] | None = None,
                  limit: int | None = None) -> Iterator[EntityRecord]:
    """
    Yield entity records, optionally filtered by pipeline state.
    state_filter=None → all states (including missing _pipelineState).
    """
    count = 0
    for root, _, files in os.walk(ENTITIES_DIR):
        for fname in files:
            if not fname.endswith(".json"):
                continue
            path = Path(root) / fname
            container = _safe_load(path)
            if not container or "entities" not in container:
                continue
            for idx, e in enumerate(container["entities"]):
                if not isinstance(e, dict):
                    continue
                slug = e.get("slug") or ""
                if not slug:
                    continue
                ps = e.get("_pipelineState") or {"state": "pending", "attempts": 0}
                if state_filter and ps.get("state") not in state_filter:
                    continue
                summary = e.get("summary", "")
                if isinstance(summary, list):
                    summary = " ".join(str(s) for s in summary)
                details = {}
                dj = e.get("detailsJson")
                if isinstance(dj, str) and dj:
                    try:
                        details = json.loads(dj)
                    except json.JSONDecodeError:
                        details = {}
                elif isinstance(dj, dict):
                    details = dj
                yield EntityRecord(
                    file_path=path,
                    slug=slug,
                    label=e.get("label") or "",
                    name=e.get("name") or "",
                    summary=summary,
                    importance_score=int(e.get("importanceScore") or 0),
                    wikidata_qid=e.get("wikidataQid"),
                    details=details,
                    pipeline_state=ps,
                    raw=e,
                    container=container,
                    index_in_file=idx,
                )
                count += 1
                if limit and count >= limit:
                    return


def set_state(record: EntityRecord, state: str, *, gate: str,
              reason: str = "", extra: dict | None = None) -> None:
    """Update entity's _pipelineState and write file back atomically with lock."""
    if state not in VALID_STATES:
        raise ValueError(f"invalid state: {state}")
    # Acquire file lock on a sibling lock file so we don't conflict with readers
    lock_path = record.file_path.with_suffix(record.file_path.suffix + ".lock")
    with open(lock_path, "a+") as lock_fp:
        try:
            fcntl.flock(lock_fp.fileno(), fcntl.LOCK_EX)
            # Re-read to avoid trampling a concurrent writer
            container = _safe_load(record.file_path) or record.container
            if "entities" not in container or record.index_in_file >= len(container["entities"]):
                return
            entity = container["entities"][record.index_in_file]
            ps = entity.get("_pipelineState") or {"state": "pending", "attempts": 0}
            ps["state"] = state
            ps["lastGate"] = gate
            ps["lastReason"] = reason
            ps["updatedAt"] = _now()
            if state == "in-flight":
                ps["attempts"] = int(ps.get("attempts") or 0) + 1
            if extra:
                ps.update(extra)
            entity["_pipelineState"] = ps
            _atomic_write(record.file_path, container)
        finally:
            try:
                fcntl.flock(lock_fp.fileno(), fcntl.LOCK_UN)
            except Exception:
                pass
    try:
        lock_path.unlink()
    except OSError:
        pass


def claim_next_in_flight(state_to_claim: str = "triaged") -> EntityRecord | None:
    """
    Pop the next entity in `state_to_claim` and atomically move it to in-flight.
    Returns None if none available. Used by enrich workers to avoid double-pickup.
    """
    for rec in iter_entities(state_filter={state_to_claim}):
        # Re-check after lock
        lock_path = rec.file_path.with_suffix(rec.file_path.suffix + ".lock")
        with open(lock_path, "a+") as lock_fp:
            try:
                fcntl.flock(lock_fp.fileno(), fcntl.LOCK_EX)
                container = _safe_load(rec.file_path)
                if not container:
                    continue
                entity = container["entities"][rec.index_in_file]
                ps = entity.get("_pipelineState") or {}
                if ps.get("state") != state_to_claim:
                    continue  # someone else took it
                ps["state"] = "in-flight"
                ps["attempts"] = int(ps.get("attempts") or 0) + 1
                ps["lastGate"] = "enrich"
                ps["updatedAt"] = _now()
                entity["_pipelineState"] = ps
                _atomic_write(rec.file_path, container)
                rec.pipeline_state = ps
                rec.raw = entity
                rec.container = container
                return rec
            finally:
                try:
                    fcntl.flock(lock_fp.fileno(), fcntl.LOCK_UN)
                except Exception:
                    pass
        try:
            lock_path.unlink()
        except OSError:
            pass
    return None


def aggregate_counts() -> dict:
    """Walk all entities and return state counts. Slow — call from audit script."""
    counts = {s: 0 for s in VALID_STATES}
    counts["pending"] = 0  # ensure key exists
    total = 0
    by_label: dict[str, dict[str, int]] = {}
    for rec in iter_entities():
        total += 1
        state = rec.pipeline_state.get("state", "pending")
        counts[state] = counts.get(state, 0) + 1
        lbl = rec.label or "Unknown"
        if lbl not in by_label:
            by_label[lbl] = {s: 0 for s in VALID_STATES}
        by_label[lbl][state] = by_label[lbl].get(state, 0) + 1
    return {
        "generatedAt": _now(),
        "total": total,
        "counts": counts,
        "byLabel": by_label,
    }


def write_state_summary(summary: dict) -> None:
    _atomic_write(STATE_FILE, summary)
