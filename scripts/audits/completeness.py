#!/usr/bin/env python3
"""Completeness audit — git-first.

Walks `data/appwrite-export/entities/` and scores each entity on 9 quality
dimensions. Writes `data/audit-reports/completeness.json`.

Replaces functions/audit-completeness/.
"""
from __future__ import annotations

import datetime as dt
from collections import Counter
from typing import Any

from scripts.audits import (
    iter_entities,
    parse_details,
    write_report,
    LABELS,
    ERAS,
)

DIMENSIONS = [
    "summary", "causes", "effects", "relationships",
    "places", "subjects", "frameworks", "subjectHeadings", "label",
]


def score_entity(entity: dict[str, Any]) -> dict[str, Any]:
    details = parse_details(entity)
    summary = entity.get("summary") or ""
    rels = details.get("relationships") or []
    rel_count = len(rels) if isinstance(rels, list) else 0

    missing: list[str] = []
    if len(summary) < 200:
        missing.append("summary")
    if not details.get("causes"):
        missing.append("causes")
    if not details.get("effects"):
        missing.append("effects")
    if rel_count < 3:
        missing.append("relationships")
    if not details.get("places"):
        missing.append("places")
    subjects = entity.get("subjects") or []
    if not isinstance(subjects, list) or len(subjects) < 3:
        missing.append("subjects")
    frameworks = entity.get("frameworks") or []
    if not isinstance(frameworks, list) or len(frameworks) < 1:
        missing.append("frameworks")
    headings = entity.get("subjectHeadings") or []
    if not isinstance(headings, list) or not headings:
        missing.append("subjectHeadings")
    if not entity.get("label"):
        missing.append("label")

    score = max(0, 10 - len(missing))
    return {
        "slug": entity.get("slug", ""),
        "name": entity.get("name", ""),
        "label": entity.get("label", ""),
        "era": entity.get("era", ""),
        "score": score,
        "missing": missing,
        "relCount": rel_count,
        "importance": entity.get("importanceScore", 0),
    }


def main() -> None:
    label_counts: Counter[str] = Counter()
    era_counts: Counter[str] = Counter()
    score_dist: Counter[int] = Counter()
    dim_missing: Counter[str] = Counter()
    total = 0
    sum_score = 0
    orphans = 0
    critical: list[dict[str, Any]] = []

    for ent in iter_entities():
        total += 1
        label_counts[ent.get("label") or "Unknown"] += 1
        era_counts[ent.get("era") or "Unknown"] += 1
        s = score_entity(ent)
        sum_score += s["score"]
        score_dist[s["score"]] += 1
        for m in s["missing"]:
            dim_missing[m] += 1
        if s["relCount"] == 0:
            orphans += 1
        if (s["importance"] or 0) >= 5 and s["score"] < 5:
            critical.append(s)

    critical.sort(key=lambda r: -(r["importance"] or 0))
    avg = round(sum_score / total, 2) if total else 0.0

    dim_coverage = {
        d: round((total - dim_missing[d]) / total * 100, 1) if total else 0.0
        for d in DIMENSIONS
    }

    payload = {
        "generatedAt": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "git",
        "summary": {"avg_score": avg, "critical": len(critical)},
        "total": total,
        "averageScore": avg,
        "scoreDistribution": dict(sorted(score_dist.items())),
        "byLabel": {l: label_counts.get(l, 0) for l in LABELS if label_counts.get(l)},
        "byEra": {e: era_counts.get(e, 0) for e in ERAS if era_counts.get(e)},
        "dimensionCoverage": dim_coverage,
        "orphanRate": round(orphans / total * 100, 2) if total else 0.0,
        "criticalCount": len(critical),
        "criticalTop100": critical[:100],
    }
    out = write_report("completeness", payload)
    print(f"completeness: scanned {total} entities, avg score {avg}, "
          f"{len(critical)} critical → {out}")


if __name__ == "__main__":
    main()
