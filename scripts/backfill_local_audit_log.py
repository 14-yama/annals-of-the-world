#!/usr/bin/env python3
"""
backfill_local_audit_log.py

Create-if-missing import of historical audit_log rows into local Appwrite
from cloud backup JSON (data/backups/cloud-*/audit_log.json).

Resumable via data/governance/audit_backfill_cursor.json.
Never overwrites existing local rows (POST → 409 = skip).

Usage:
  python3 scripts/backfill_local_audit_log.py
  python3 scripts/backfill_local_audit_log.py --max=20000
  python3 scripts/backfill_local_audit_log.py --reset-cursor
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

ROOT = Path(__file__).resolve().parents[1]
CURSOR = ROOT / "data" / "governance" / "audit_backfill_cursor.json"
ATTRS = {
    "entityId", "entitySlug", "entityName", "action", "field",
    "oldValue", "newValue", "editorId", "editorNote", "timestamp", "sessionId",
}


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        k, v = k.strip(), v.strip().strip("'").strip('"')
        if k and k not in os.environ:
            os.environ[k] = v


load_dotenv(ROOT / ".env")

ENDPOINT = (
    os.environ.get("LOCAL_APPWRITE_ENDPOINT")
    or os.environ.get("VITE_APPWRITE_ENDPOINT")
    or "http://localhost:8080/v1"
).rstrip("/")
PROJECT = (
    os.environ.get("LOCAL_APPWRITE_PROJECT_ID")
    or os.environ.get("VITE_APPWRITE_PROJECT_ID")
    or "annals-local"
)
DATABASE = (
    os.environ.get("LOCAL_APPWRITE_DATABASE_ID")
    or os.environ.get("VITE_APPWRITE_DATABASE_ID")
    or "annals_world_db"
)
KEY = os.environ.get("LOCAL_APPWRITE_API_KEY") or os.environ.get("APPWRITE_API_KEY") or ""


def headers() -> dict:
    return {
        "X-Appwrite-Project": PROJECT,
        "X-Appwrite-Key": KEY,
        "Content-Type": "application/json",
    }


def post_doc(doc_id: str, payload: dict) -> tuple[str, str]:
    """Returns (status, detail) where status is created|exists|failed."""
    url = f"{ENDPOINT}/databases/{DATABASE}/collections/audit_log/documents"
    body = json.dumps({
        "documentId": doc_id,
        "data": payload,
        "permissions": ['read("any")'],
    }).encode()
    r = urllib.request.Request(url, data=body, headers=headers(), method="POST")
    try:
        with urllib.request.urlopen(r, timeout=60) as resp:
            resp.read()
            return "created", str(resp.status)
    except urllib.error.HTTPError as e:
        raw = e.read().decode() if e.fp else ""
        if e.code == 409 or "already exists" in raw.lower():
            return "exists", "409"
        return "failed", f"{e.code}:{raw[:160]}"
    except Exception as e:
        return "failed", str(e)[:160]


def sanitize(doc: dict) -> dict:
    payload: dict = {}
    for k, v in doc.items():
        if k.startswith("$") or k.startswith("_"):
            continue
        if k not in ATTRS or v is None:
            continue
        payload[k] = v
    note = str(payload.get("editorNote") or "")
    if "backup-merged" not in note and "cloud-merged" not in note:
        payload["editorNote"] = f"{note} · backup-merged".strip(" ·") if note else "backup-merged"
    editor = str(payload.get("editorId") or "")
    if editor and "·cloud·" not in editor and "GH#" not in editor and "cloud" not in editor.lower():
        payload["editorId"] = f"{editor}·cloud·merged"
    for k, lim in (
        ("editorId", 128), ("editorNote", 1000), ("oldValue", 4000), ("newValue", 4000),
        ("sessionId", 128), ("entityId", 64), ("entitySlug", 200), ("entityName", 300),
        ("action", 32), ("field", 128), ("timestamp", 64),
    ):
        if isinstance(payload.get(k), str):
            payload[k] = payload[k][:lim]
    if not payload.get("timestamp"):
        payload["timestamp"] = doc.get("$createdAt") or time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    if not payload.get("action"):
        payload["action"] = "update"
    if not payload.get("field"):
        payload["field"] = "unknown"
    return payload


def find_source(explicit: str | None) -> Path:
    if explicit:
        p = Path(explicit)
        return p if p.is_absolute() else ROOT / p
    backups = sorted((ROOT / "data" / "backups").glob("cloud-*/audit_log.json"))
    if not backups:
        raise SystemExit("No data/backups/cloud-*/audit_log.json found")
    return backups[-1]


def read_cursor() -> dict:
    if not CURSOR.exists():
        return {"offset": 0, "created": 0, "skipped": 0, "failed": 0}
    try:
        return json.loads(CURSOR.read_text())
    except Exception:
        return {"offset": 0, "created": 0, "skipped": 0, "failed": 0}


def write_cursor(cur: dict) -> None:
    CURSOR.parent.mkdir(parents=True, exist_ok=True)
    cur["lastRunAt"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    CURSOR.write_text(json.dumps(cur, indent=2) + "\n")


def log(msg: str) -> None:
    print(msg, flush=True)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=4000)
    ap.add_argument("--source", type=str, default=None)
    ap.add_argument("--reset-cursor", action="store_true")
    ap.add_argument("--sleep-ms", type=int, default=5)
    ap.add_argument("--checkpoint", type=int, default=50, help="Cursor write every N attempts")
    args = ap.parse_args()

    if not KEY:
        print("ERROR: APPWRITE_API_KEY missing", file=sys.stderr)
        return 1

    source = find_source(args.source)
    log(f"[audit-backfill] {ENDPOINT} / {PROJECT} / {DATABASE}")
    log(f"[audit-backfill] source={source}")

    t0 = time.time()
    data = json.loads(source.read_text())
    docs = data.get("documents") or []
    log(f"[audit-backfill] loaded {len(docs)} in {time.time()-t0:.1f}s")

    cur = {"offset": 0, "created": 0, "skipped": 0, "failed": 0} if args.reset_cursor else read_cursor()
    if cur.get("source") and cur["source"] != str(source):
        cur = {"offset": 0, "created": 0, "skipped": 0, "failed": 0}
    cur["source"] = str(source)

    offset = int(cur.get("offset") or 0)
    created = int(cur.get("created") or 0)
    skipped = int(cur.get("skipped") or 0)
    failed = int(cur.get("failed") or 0)
    attempted = 0
    started = time.time()
    checkpoint = max(10, int(args.checkpoint))

    # Heartbeat immediately so a post-load kill still leaves a fresh lastRunAt.
    write_cursor({
        "offset": offset, "created": created, "skipped": skipped,
        "failed": failed, "source": str(source), "done": False,
        "phase": "running",
    })
    log(f"[audit-backfill] resume offset={offset}/{len(docs)} max={args.max}")

    while offset < len(docs) and attempted < args.max:
        doc = docs[offset]
        offset += 1
        attempted += 1
        doc_id = str(doc.get("$id") or "").strip()
        if not doc_id:
            failed += 1
            continue
        status, detail = post_doc(doc_id, sanitize(doc))
        if status == "created":
            created += 1
            if args.sleep_ms > 0:
                time.sleep(args.sleep_ms / 1000.0)
        elif status == "exists":
            skipped += 1
        else:
            failed += 1
            if failed <= 8 or failed % 100 == 0:
                log(f"[audit-backfill] fail {doc_id}: {detail}")

        if attempted % checkpoint == 0:
            write_cursor({
                "offset": offset, "created": created, "skipped": skipped,
                "failed": failed, "source": str(source), "done": False,
                "phase": "running",
            })
            rate = attempted / max(time.time() - started, 0.1)
            log(
                f"[audit-backfill] offset={offset}/{len(docs)} "
                f"created={created} skipped={skipped} failed={failed} "
                f"({rate:.0f}/s, {time.time()-started:.0f}s)"
            )

    done = offset >= len(docs)
    write_cursor({
        "offset": offset, "created": created, "skipped": skipped,
        "failed": failed, "source": str(source), "done": done,
        "phase": "complete" if done else "paused",
    })
    log(
        f"[audit-backfill] {'COMPLETE' if done else 'paused'} "
        f"offset={offset}/{len(docs)} created={created} skipped={skipped} "
        f"failed={failed} elapsed={time.time()-started:.0f}s"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
