"""
Shared configuration for Annals audit scripts.
Reads Appwrite credentials from environment / .env file.
"""

import os
import json
from pathlib import Path

# ── Load .env from ui/ if available ──
_env_path = Path(__file__).resolve().parent.parent.parent / "ui" / ".env"
if _env_path.exists():
    for line in _env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, val = line.partition("=")
            os.environ.setdefault(key.strip(), val.strip())

ENDPOINT = os.environ.get("VITE_APPWRITE_ENDPOINT", "https://fra.cloud.appwrite.io/v1")
PROJECT_ID = os.environ.get("VITE_APPWRITE_PROJECT_ID", "66509ba7003618a05af6")
DATABASE_ID = os.environ.get("VITE_APPWRITE_DATABASE_ID", "annals_world_db")
API_KEY = os.environ.get("APPWRITE_API_KEY", "")
COLLECTION_ID = "entities"

LABELS = ["Person", "Idea", "Institution", "Place", "EventWindow",
          "Movement", "Text", "Evidence", "Timeframe"]
ERAS = ["Prehistoric", "Classical", "Medieval", "Early Modern",
        "Modern", "Contemporary"]


def get_client():
    """Return configured Appwrite client + Databases service."""
    from appwrite.client import Client
    from appwrite.services.databases import Databases

    client = Client()
    client.set_endpoint(ENDPOINT)
    client.set_project(PROJECT_ID)
    client.set_key(API_KEY)
    return client, Databases(client)


def fetch_all(db, queries, *, batch=100):
    """Paginate through all matching documents."""
    from appwrite.query import Query as Q

    offset = 0
    docs = []
    while True:
        res = db.list_documents(
            DATABASE_ID, COLLECTION_ID,
            queries=queries + [Q.limit(batch), Q.offset(offset)],
        )
        batch_docs = res["documents"] if isinstance(res, dict) else res.documents
        if not batch_docs:
            break
        docs.extend(batch_docs)
        offset += len(batch_docs)
    return docs


def doc_field(doc, field, default=None):
    """Safe field access for dict or object."""
    if isinstance(doc, dict):
        return doc.get(field, default)
    return getattr(doc, field, default)


def parse_details(doc):
    """Parse detailsJson from a document."""
    raw = doc_field(doc, "detailsJson", "{}")
    return json.loads(raw) if raw else {}
