#!/usr/bin/env python3
"""Paged cursor count of Appwrite audit_log → stats_cache.auditTotal.

Appwrite 1.6 listDocuments.total hard-caps at 5000. Curator Audit Log reads
stats_cache.auditTotal instead. Uses JSON query objects (1.6 REST format).

Usage:
  python3 scripts/count_audit_total.py
"""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_env() -> None:
    for p in [ROOT / ".env", Path.home() / ".config/annals/env"]:
        if not p.exists():
            continue
        for line in p.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip("\"'"))


load_env()
KEY = os.environ.get("LOCAL_APPWRITE_API_KEY") or os.environ.get("APPWRITE_API_KEY") or ""
EP = (
    os.environ.get("LOCAL_APPWRITE_ENDPOINT")
    or os.environ.get("VITE_APPWRITE_ENDPOINT")
    or "http://localhost:8080/v1"
)
DB = (
    os.environ.get("LOCAL_APPWRITE_DATABASE_ID")
    or os.environ.get("VITE_APPWRITE_DATABASE_ID")
    or "annals_world_db"
)
PROJ = (
    os.environ.get("LOCAL_APPWRITE_PROJECT_ID")
    or os.environ.get("VITE_APPWRITE_PROJECT_ID")
    or "annals-local"
)
# Appwrite 1.6 accepts larger pages via JSON queries; keep portable-ish.
PAGE = int(os.environ.get("AUDIT_COUNT_PAGE", "500"))
PROGRESS = 5000

if not KEY:
    sys.exit("ERROR: APPWRITE API key missing")


def q(method: str, values: list) -> str:
    return json.dumps({"method": method, "values": values})


def list_page(cursor: str | None = None) -> dict:
    queries = [q("limit", [PAGE]), q("select", ["$id"])]
    if cursor:
        queries.append(q("cursorAfter", [cursor]))
    qs = "&".join("queries[]=" + urllib.parse.quote(item) for item in queries)
    url = f"{EP}/databases/{DB}/collections/audit_log/documents?{qs}"
    req = urllib.request.Request(
        url,
        headers={"X-Appwrite-Project": PROJ, "X-Appwrite-Key": KEY},
    )
    last_err: Exception | None = None
    for attempt in range(1, 6):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.loads(r.read().decode())
        except Exception as e:  # noqa: BLE001 — retry transient Appwrite/MariaDB blips
            last_err = e
            wait = min(2 ** attempt, 20)
            print(f"[audit-count] page error attempt {attempt}/5: {e}; sleep {wait}s", flush=True)
            time.sleep(wait)
    raise SystemExit(f"list_page failed after retries: {last_err}") from last_err


def patch_mirror(extra: dict) -> None:
    for rel in ["data/governance/stats_cache.json", "ui/public/governance/stats_cache.json"]:
        p = ROOT / rel
        data: dict = {}
        if p.exists():
            try:
                data = json.loads(p.read_text())
            except Exception:
                data = {}
        data.update(extra)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(data, indent=2) + "\n")


def patch_mirror_progress(total: int) -> None:
    """Write progressive counts without lowering a known-good completed total."""
    for rel in ["data/governance/stats_cache.json", "ui/public/governance/stats_cache.json"]:
        p = ROOT / rel
        data: dict = {}
        if p.exists():
            try:
                data = json.loads(p.read_text())
            except Exception:
                data = {}
        prev = int(data.get("auditTotal") or 0)
        prev_incomplete = bool(data.get("auditTotalIncomplete"))
        if prev > total and not prev_incomplete:
            # Keep the higher completed total; only annotate progress
            data["auditCountProgress"] = total
        else:
            data["auditTotal"] = total
            data["auditTotalIncomplete"] = True
        data["auditTotalUpdatedAt"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(data, indent=2) + "\n")


def main() -> None:
    print(f"[audit-count] endpoint={EP} project={PROJ} db={DB} page={PAGE}")
    started = time.time()
    total = 0
    cursor = None
    prev = None
    while True:
        page = list_page(cursor)
        docs = page.get("documents") or []
        if not docs:
            break
        total += len(docs)
        prev = cursor
        cursor = docs[-1]["$id"]
        if cursor == prev:
            print("[audit-count] cursor stuck — abort")
            break
        if total % PROGRESS < PAGE:
            elapsed = int((time.time() - started) * 1000)
            print(f"[audit-count] counted {total}… ({elapsed}ms)", flush=True)
            # Never clobber a higher completed auditTotal with a mid-count floor
            patch_mirror_progress(total)
        if len(docs) < PAGE:
            break
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    patch_mirror(
        {
            "auditTotal": total,
            "auditTotalUpdatedAt": now,
            "auditTotalIncomplete": False,
            "auditTotalNote": f"paged cursor count in {int((time.time() - started) * 1000)}ms",
        }
    )
    print(f"[audit-count] DONE total={total} ({int((time.time() - started) * 1000)}ms)")


if __name__ == "__main__":
    main()
