#!/usr/bin/env python3
"""Fix-up: enrich the Vivien entity using dynamic slug detection."""
import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/230-Class-230"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()

actual_slug = None
for f in os.listdir(FOLDER):
    if "vivien" in f.lower():
        actual_slug = f[3:-5]
        break

if not actual_slug:
    print("ERROR: Vivien file not found"); exit(1)

fname = os.path.join(FOLDER, f"230{actual_slug}.json")
with open(fname, "r", encoding="utf-8") as f:
    doc = json.load(f)
entity = doc["entities"][0]
det = json.loads(entity.get("detailsJson", "{}"))
edit_log = det.get("_editLog", [])

summary = (
    "Alexandre-François Vivien (1799–1854) was a French lawyer, "
    "legal scholar, and politician who served as Minister of "
    "the Interior (1848) and made important contributions "
    "to the development of French administrative law. "
    "His 'Études administratives' (1845) was one of the "
    "founding texts of modern French administrative law — "
    "the field governing relations between the state and citizens.\n\n"
    "Vivien served during the turbulent year of 1848 — "
    "the February Revolution that overthrew Louis-Philippe, "
    "the proclamation of the Second Republic, and the "
    "June Days uprising. His Interior Ministry service "
    "placed him at the center of the Second Republic's "
    "early governance.\n\n"
    "Administrative law — the French system of separate "
    "courts to adjudicate state-citizen disputes — is "
    "one of France's most distinctive legal contributions "
    "to global governance. Vivien's treatise provided "
    "its intellectual foundations alongside his ministerial experience.\n\n"
    "He was also a Councillor of State — the dual role "
    "of practitioner and scholar that made French "
    "administrative law scholarship particularly authoritative."
)

causes = [
    "The development of French administrative law — the legal tradition separating "
    "judicial review of state action from ordinary civil courts that France pioneered "
    "— created the scholarly field to which Vivien contributed foundational texts",
    "The 1848 Revolution's political upheaval — the February Revolution, Second "
    "Republic, and June Days that created the political context for Vivien's "
    "Interior Ministry appointment — placed the administrative law scholar at "
    "the center of executive governance",
    "Vivien's Conseil d'État expertise — his deep knowledge of the administrative "
    "court system that adjudicated state-citizen disputes — gave him both the "
    "scholarly tools for his treatise and the practical experience for ministerial service"
]

effects = [
    "His 'Études administratives' contributed to the intellectual foundations "
    "of French administrative law — providing the systematic theoretical framework "
    "for a distinctive French legal tradition",
    "His Interior Ministry service contributed to the governance of the Second "
    "Republic's critical early months — managing the state apparatus during "
    "the revolutionary transition",
    "His administrative law scholarship influenced subsequent generations of "
    "French legal scholars — the tradition of systematic analysis of the "
    "administrative state that shaped comparative administrative law globally",
    "France's administrative law tradition that Vivien helped establish "
    "contributed to the global model — the system adopted or adapted by many "
    "countries as an alternative to common-law judicial review"
]

relationships = [
    {"target": "french-ministry-of-interior", "verb": "LEADS",
     "note": "Minister of the Interior 1848"},
    {"target": "french-second-republic", "verb": "SERVES_IN",
     "note": "Minister during the 1848 revolutionary republic"},
    {"target": "french-administrative-law", "verb": "FOUNDS",
     "note": "Author of 'Études administratives' — founding administrative law text"},
    {"target": "conseil-detat-france", "verb": "SERVES_IN",
     "note": "Councillor of State with administrative court expertise"},
    {"target": "revolution-of-1848-france", "verb": "SERVES_DURING",
     "note": "Interior Minister during the February Revolution"}
]

hs = {
    "significanceScore": 8,
    "significanceNarrative": (
        "French Minister of the Interior (1848) and founding administrative law scholar; "
        "his 'Études administratives' (1845) was a founding text of French administrative law; "
        "served during the 1848 Revolution and early Second Republic; Councillor of State; "
        "France's administrative law tradition is one of its most distinctive global contributions."
    ),
    "significanceCategory": "continental"
}

for field, val in [("summary", summary), ("importanceScore", 6), ("historicalSignificance", hs)]:
    old = entity.get(field)
    entity[field] = val
    edit_log.append({"timestamp": NOW, "editorId": EDITOR_ID, "field": field,
                     "oldValue": str(old)[:300], "newValue": str(val)[:300]})

for field, val in [("causes", causes), ("effects", effects), ("relationships", relationships)]:
    old = det.get(field, [])
    det[field] = val
    edit_log.append({"timestamp": NOW, "editorId": EDITOR_ID, "field": field,
                     "oldValue": json.dumps(old)[:300], "newValue": json.dumps(val)[:300]})

det["_editLog"] = edit_log
det["_unsyncedEdits"] = True
entity["_unsyncedEdits"] = True
entity["detailsJson"] = json.dumps(det, ensure_ascii=False)

with open(fname, "w", encoding="utf-8") as f:
    json.dump(doc, f, indent=2, ensure_ascii=False)

slen = len(entity.get("summary", ""))
print(f"✓ {entity['name']} — sum={slen}c c={len(causes)} e={len(effects)}")
print(f"  slug used: {actual_slug}")
