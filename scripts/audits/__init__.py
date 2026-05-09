"""Shared helpers for git-first audit bots.

All bots read from `data/appwrite-export/entities/` and write reports to
`data/audit-reports/`. Zero Appwrite reads.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Generator

REPO_ROOT = Path(__file__).resolve().parents[2]
ENTITIES_DIR = REPO_ROOT / "data" / "appwrite-export" / "entities"
REPORTS_DIR = REPO_ROOT / "data" / "audit-reports"

LABELS = [
    "Idea", "Person", "Place", "EventWindow", "Institution", "Movement",
    "Text", "Evidence", "Corpus", "Framework", "Timeframe", "Polity",
]
ERAS = [
    "Prehistoric", "Classical", "Medieval", "Early Modern", "Modern",
    "Contemporary",
]
ERA_CODE_RANGES = {
    "Prehistoric":  (910, 919),
    "Classical":    (920, 929),
    "Medieval":     (930, 939),
    "Early Modern": (940, 949),
    "Modern":       (950, 959),
    "Contemporary": (960, 969),
}


def iter_entity_files() -> Generator[Path, None, None]:
    """Yield every entity JSON file under data/appwrite-export/entities/."""
    if not ENTITIES_DIR.exists():
        return
    for path in ENTITIES_DIR.rglob("*.json"):
        yield path


def iter_entities() -> Generator[dict[str, Any], None, None]:
    """Yield every entity record from every JSON file."""
    for path in iter_entity_files():
        try:
            with path.open("r", encoding="utf-8") as fh:
                data = json.load(fh)
        except (OSError, json.JSONDecodeError):
            continue
        entities = data.get("entities") if isinstance(data, dict) else None
        if not isinstance(entities, list):
            continue
        for ent in entities:
            if isinstance(ent, dict):
                yield ent


def parse_details(entity: dict[str, Any]) -> dict[str, Any]:
    """detailsJson is a stringified JSON blob; parse safely."""
    raw = entity.get("detailsJson")
    if isinstance(raw, dict):
        return raw
    if isinstance(raw, str) and raw:
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return {}
    return {}


def write_report(name: str, payload: dict[str, Any]) -> Path:
    """Write a report JSON to data/audit-reports/{name}.json. Returns path."""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    out = REPORTS_DIR / f"{name}.json"
    with out.open("w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False, sort_keys=False)
    return out
