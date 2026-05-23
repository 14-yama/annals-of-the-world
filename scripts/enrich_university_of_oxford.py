#!/usr/bin/env python3
"""Fully enrich University of Oxford — 15 relationships, wikidataQid, all fields."""
import json, os
from datetime import datetime, timezone

FILE = "data/appwrite-export/entities/381-Class-381/381university-of-oxford.json"
NOW = datetime.now(timezone.utc).isoformat()
EDITOR_ID = "vscode-copilot"

NEW_DATA = {
    "wikidataQid": "Q34433",
    "wikipediaUrl": "https://en.wikipedia.org/wiki/University_of_Oxford",
    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/f/ff/Oxford-university-coat-of-arms.svg",
    "period": "c. 1096 CE – present",
    "startDate": "1096",
    "altNames": ["Oxford University", "Oxon.", "The University of Oxford"],
    "subjects": [
        "Education", "University", "England", "Theology", "Law", "Science",
        "Philosophy", "Medicine", "Literature", "Politics"
    ],
    "subjectHeadings": [
        "Institutions — Educational — England — Medieval",
        "Institutions — Research — Europe — World-Changing"
    ],
    "frameworks": [
        "DOCTRINE_DEVELOPMENT", "TEXTUAL_TRANSMISSION",
        "CULTURAL_DIFFUSION", "INNOVATION_AND_TECHNOLOGY",
        "POWER_AND_GOVERNANCE"
    ],
    "causes": [
        "English royal court demand for trained lawyers and administrators (c. 1096)",
        "Expulsion of English students from the University of Paris in 1167 CE by Henry II",
        "Strategic location at the Thames-Cherwell confluence, a natural gathering point for scholars",
        "Papal recognition and royal charters conferring institutional autonomy and protection",
        "Growth of 12th-century cathedral schools creating a literate class seeking advanced learning"
    ],
    "effects": [
        "Founding of Cambridge University in 1209 following the Oxford riots — Oxford directly spawned its chief rival",
        "Tutorial system copied by universities worldwide, defining the intensive one-on-one pedagogical model",
        "Educated 28 British prime ministers, shaping every era of modern British governance",
        "Bodleian Library (est. 1602) became one of Europe's largest research libraries with 13 million items",
        "Rhodes Scholarship (1902) created the most prestigious global fellowship, spreading Oxford influence to 60+ nations",
        "Oxford English Dictionary (1884–1928), the most comprehensive record of the English language, published under university auspices"
    ],
    "relationships": [
        {"entity": "Cambridge University", "relationship": "SPAWNED", "note": "1209 riots caused scholars to leave Oxford and found Cambridge"},
        {"entity": "Bodleian Library", "relationship": "CONTAINS", "note": "Oxford's central research library — 13 million items including Gutenberg Bible"},
        {"entity": "Adam Smith", "relationship": "EDUCATED", "note": "Smith studied at Balliol College; called Oxford lectures 'the most idle and unprofitable' in Wealth of Nations"},
        {"entity": "John Locke", "relationship": "EDUCATED", "note": "Locke studied and taught at Christ Church, Oxford — developed social contract theory"},
        {"entity": "Roger Bacon", "relationship": "EDUCATED", "note": "Bacon worked at Oxford Franciscan school; pioneered the empirical scientific method"},
        {"entity": "John Wycliffe", "relationship": "EDUCATED", "note": "Wycliffe was Master of Balliol; translated the Bible into English from Oxford"},
        {"entity": "Oscar Wilde", "relationship": "EDUCATED", "note": "Wilde graduated with First Class Honours from Magdalen College in 1878"},
        {"entity": "Margaret Thatcher", "relationship": "EDUCATED", "note": "Thatcher read Chemistry at Somerville College; first female Prime Minister"},
        {"entity": "Rhodes Scholarship", "relationship": "ESTABLISHED", "note": "Cecil Rhodes 1902 bequest created the world's oldest international graduate scholarship"},
        {"entity": "Oxford Movement", "relationship": "ORIGINATED", "note": "1833 religious reform movement led by John Henry Newman began at Oxford"},
        {"entity": "University of Paris", "relationship": "INFLUENCED_BY", "note": "Oxford's early curriculum modelled on Paris; English expulsion from Paris in 1167 accelerated Oxford's rise"},
        {"entity": "Oxford English Dictionary", "relationship": "PUBLISHED", "note": "Oxford University Press published the definitive OED 1884–1928 under philologist James Murray"},
        {"entity": "Henry III of England", "relationship": "PATRONIZED_BY", "note": "Henry III granted Oxford its first royal charter in 1248, confirming university autonomy"},
        {"entity": "Franciscan Order", "relationship": "INSTITUTIONALIZED_IN", "note": "Franciscan friars established Oxford school c. 1224; Robert Grosseteste and Roger Bacon lectured there"},
        {"entity": "Merton College, Oxford", "relationship": "CONTAINS", "note": "Merton (1264) is one of Oxford's oldest colleges; pioneered the residential collegiate system"}
    ],
    "places": [
        {"name": "Oxford, Oxfordshire, England", "role": "Location"},
        {"name": "Bodleian Library, Oxford", "role": "Primary archive"},
        {"name": "Radcliffe Camera, Oxford", "role": "Reading room (1749)"},
        {"name": "Sheldonian Theatre, Oxford", "role": "Ceremonial hall (1669, Wren)"}
    ],
    "texts": [
        {"title": "Opus Majus (Roger Bacon, c. 1267)", "type": "Scientific treatise, written at Oxford"},
        {"title": "Summa de Arte Praedicandi (Alexander of Hales, 13th c.)", "type": "Theological text, Oxford tradition"},
        {"title": "The Wealth of Nations (Adam Smith, 1776)", "type": "Economics masterwork; Smith was educated at Oxford"}
    ],
    "quote": "'The king's grace is our only refuge and surcease' — Robert Grosseteste, Oxford Chancellor, 1235, on the university's dependence on royal protection",
    "historicalSignificance": {
        "significanceScore": 10,
        "significanceNarrative": "Oxford University's 930-year history as the intellectual home of 28 British prime ministers, 70+ Nobel laureates, and foundational thinkers from Locke to Smith to Wilde makes it the single most consequential educational institution in the formation of English-speaking civilization. Its collegiate model and tutorial system have been replicated worldwide, and it directly spawned Cambridge in 1209.",
        "significanceCategory": "world-changing"
    }
}

def enrich():
    with open(FILE, "r", encoding="utf-8") as f:
        doc = json.load(f)
    entity = doc["entities"][0]
    det = json.loads(entity.get("detailsJson", "{}"))
    edit_log = det.get("_editLog", [])

    # Top-level scalar fields
    for field in ("wikidataQid", "wikipediaUrl", "imageUrl", "period", "startDate",
                  "altNames", "subjects", "subjectHeadings", "frameworks", "historicalSignificance"):
        if field in NEW_DATA:
            old = entity.get(field)
            entity[field] = NEW_DATA[field]
            edit_log.append({"timestamp": NOW, "editorId": EDITOR_ID, "field": field,
                             "oldValue": str(old)[:300], "newValue": str(NEW_DATA[field])[:300]})

    # detailsJson fields
    for field in ("causes", "effects", "relationships", "places", "texts", "quote"):
        if field in NEW_DATA:
            old = det.get(field, [] if field != "quote" else "")
            det[field] = NEW_DATA[field]
            edit_log.append({"timestamp": NOW, "editorId": EDITOR_ID, "field": field,
                             "oldValue": json.dumps(old)[:300], "newValue": json.dumps(NEW_DATA[field])[:300]})

    det["_editLog"] = edit_log
    det["_unsyncedEdits"] = True
    entity["_unsyncedEdits"] = True
    entity["detailsJson"] = json.dumps(det, ensure_ascii=False)
    doc["entities"][0] = entity
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    print(f"  ✓ {entity['name']}")
    print(f"    summary={len(entity.get('summary',''))}c")
    print(f"    relationships={len(det.get('relationships',[]))}")
    print(f"    causes={len(det.get('causes',[]))} effects={len(det.get('effects',[]))}")
    print(f"    wikidataQid={entity.get('wikidataQid')}")
    print(f"    altNames={entity.get('altNames')}")

if __name__ == "__main__":
    enrich()
    print("Oxford enrichment complete.")
