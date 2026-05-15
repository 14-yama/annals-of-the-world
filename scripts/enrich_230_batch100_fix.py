#!/usr/bin/env python3
"""Fix Furetiere and Galaiziere (accented filenames skipped in batch 100)"""
import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/230-Class-230"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()

FIXES = {
    "furetiè": {
        "summary": (
            "Antoine Furetière (1619–1688) was a French novelist, lexicographer, "
            "and member of the Académie française who produced one of the most "
            "important French dictionaries of the 17th century — the Dictionnaire "
            "universel (published posthumously 1690). Furetière's dictionary "
            "project created a famous controversy: the Académie française was "
            "working on its own official French dictionary and expelled Furetière "
            "from the Academy in 1685 when he obtained a royal privilege for his "
            "competing dictionary. His Roman bourgeois (1666) — a satirical novel "
            "of Parisian bourgeois life — was an early example of realistic French "
            "fiction. His Dictionnaire universel, published in the Netherlands "
            "after his death, became the basis for the later Dictionnaire de Trévoux.\n\n"
            "'I made a dictionary because the Academy was too slow.'\n\n"
            "He was the lexicographer the Académie française expelled.\n\n"
            "His dictionary outlasted his expulsion."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "French lexicographer and novelist expelled from the Académie française for his competing Dictionnaire universel (1690); his dictionary became the basis for the Dictionnaire de Trévoux; Roman bourgeois (1666) — early realistic French fiction; created the famous Académie controversy over lexicographic privilege; key figure in 17th-century French lexicography.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Académie française's slow dictionary project — the Academy's decades-long work on its official French dictionary — created the competitive gap that Furetière filled with his own comprehensive lexicographic project",
            "Louis XIV's cultural patronage — the Sun King's support for French language standardization and literary culture — created the institutional context of royal privileges and Academy monopolies that Furetière challenged",
            "The 17th century's lexicographic revolution — the era's expansion of encyclopedic and dictionary projects across Europe — created the intellectual environment for Furetière's comprehensive dictionary work"
        ],
        "effects": [
            "His Dictionnaire universel contributed to French lexicography — the comprehensive dictionary that became the basis for the Dictionnaire de Trévoux",
            "His Académie expulsion contributed to the history of French literary and intellectual politics — the famous case of the expelled lexicographer",
            "His Roman bourgeois contributed to French literary history — an early example of realistic social fiction depicting Parisian bourgeois life",
            "His dictionary controversy contributed to the debate over lexicographic monopoly and the relationship between official institutions and independent scholars"
        ],
        "relationships": [
            {"target": "academie-francaise", "verb": "EXPELLED_FROM", "note": "Expelled 1685 for competing dictionary project"},
            {"target": "dictionnaire-universel", "verb": "CREATES", "note": "Comprehensive French dictionary published posthumously 1690"},
            {"target": "dictionnaire-de-trevoux", "verb": "PROVIDES_BASIS_FOR", "note": "Dictionnaire universel became basis for later Trévoux dictionary"},
            {"target": "roman-bourgeois", "verb": "WRITES", "note": "Satirical realistic novel of Parisian bourgeois life 1666"},
            {"target": "louis-xiv", "verb": "OPERATES_UNDER_PATRONAGE_OF", "note": "Royal privilege controversy over competing dictionary"}
        ]
    },
    "galaizièr": {
        "summary": (
            "Antoine-Martin Chaumont de la Galaizière (1697–1783) was a French "
            "royal administrator who served as Intendant of Lorraine "
            "(1737–1777) — one of the most important and longest provincial "
            "intendancies of 18th-century France. His appointment came during "
            "the reign of Stanisław Leszczyński — the former King of Poland "
            "who ruled Lorraine as a French vassal until his death in 1766, "
            "after which Lorraine was formally incorporated into France. "
            "As Intendant, Chaumont de la Galaizière was the real administrative "
            "power in Lorraine — managing royal finances, law, and administration "
            "while Stanisław enjoyed ceremonial sovereignty. His forty-year "
            "intendancy was one of the longest in French provincial history.\n\n"
            "He oversaw Lorraine's smooth transition from Leszczyński's "
            "personal rule to full French provincial status.\n\n"
            "He was the real ruler of Lorraine for forty years.\n\n"
            "He was the intendant who governed while a king played."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "French royal Intendant of Lorraine (1737–1777) — one of the longest intendancies in 18th-century France; real administrative power under Stanisław Leszczyński's ceremonial sovereignty; managed Lorraine's transition from Leszczyński's personal rule to full French incorporation after 1766; forty years as the effective governor of Lorraine.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Treaty of Vienna (1738) — which gave Lorraine to Stanisław Leszczyński as a French vassal with reversion to France on his death — created the political arrangement that required an intendant as the real administrative authority",
            "The French intendancy system — the royal administrative framework that placed intendants as the king's representative and effective governor in each province — created the institutional role that Chaumont de la Galaizière filled for forty years",
            "Stanisław Leszczyński's position as ceremonial sovereign — the former Polish king's role as a royal figurehead in Lorraine — created the administrative vacuum that the intendant needed to fill with real governance"
        ],
        "effects": [
            "His forty-year intendancy contributed to the effective administration of Lorraine during its transition from Polish ceremonial sovereignty to French incorporation",
            "His administrative management contributed to the smooth integration of Lorraine into the French provincial system after Stanisław's death in 1766",
            "His intendancy contributed to the historical record of the French royal administration's most important provincial postings",
            "His career contributed to the documentation of the 18th-century intendancy system's function as the real administrative power in French provinces"
        ],
        "relationships": [
            {"target": "lorraine", "verb": "ADMINISTERS_AS_INTENDANT", "note": "Royal Intendant of Lorraine 1737–1777 — forty years"},
            {"target": "stanislaw-leszczynski", "verb": "GOVERNS_UNDER", "note": "Real administrative power under Stanisław's ceremonial sovereignty"},
            {"target": "france", "verb": "SERVES_AS_ROYAL_ADMINISTRATOR_OF", "note": "French crown's real governor of Lorraine"},
            {"target": "french-intendancy-system", "verb": "EXEMPLIFIES", "note": "One of the longest and most important French provincial intendancies"},
            {"target": "lorraine-french-incorporation", "verb": "MANAGES", "note": "Oversaw Lorraine's transition to full French province after 1766"}
        ]
    },
}


def enrich_file(target, data):
    with open(target, "r", encoding="utf-8") as f:
        doc = json.load(f)
    entity = doc["entities"][0]
    dj = entity.get("detailsJson", "{}")
    det = json.loads(dj) if isinstance(dj, str) else dj
    edit_log = det.get("_editLog", [])
    for field in ("summary", "importanceScore", "historicalSignificance"):
        if field in data:
            old = entity.get(field)
            entity[field] = data[field]
            edit_log.append({"timestamp": NOW, "editorId": EDITOR_ID, "field": field,
                             "oldValue": str(old)[:300], "newValue": str(data[field])[:300]})
    for field in ("causes", "effects", "relationships"):
        if field in data:
            old = det.get(field, [])
            det[field] = data[field]
            edit_log.append({"timestamp": NOW, "editorId": EDITOR_ID, "field": field,
                             "oldValue": json.dumps(old)[:300], "newValue": json.dumps(data[field])[:300]})
    det["_editLog"] = edit_log
    det["_unsyncedEdits"] = True
    entity["_unsyncedEdits"] = True
    entity["detailsJson"] = json.dumps(det, ensure_ascii=False)
    with open(target, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    slen = len(entity.get("summary", ""))
    print(f"  ✓ {entity['name']} — sum={slen}c c={len(det.get('causes',[]))} e={len(det.get('effects',[]))}")


for keyword, data in FIXES.items():
    found = None
    for fname in os.listdir(FOLDER):
        if keyword.lower() in fname.lower():
            found = os.path.join(FOLDER, fname)
            print(f"Found: {fname}")
            break
    if not found:
        print(f"ERROR: no file found for keyword '{keyword}'")
    else:
        enrich_file(found, data)
