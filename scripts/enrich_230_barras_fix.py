#!/usr/bin/env python3
"""Fix for Paul Barras — dynamic slug scan"""
import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/230-Class-230"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()

# Find the actual file dynamically
target = None
for f in os.listdir(FOLDER):
    if "barras" in f.lower():
        target = os.path.join(FOLDER, f)
        print(f"Found: {f}")
        break

if not target:
    print("ERROR: Barras file not found"); exit(1)

with open(target, "r", encoding="utf-8") as f:
    doc = json.load(f)

entity = doc["entities"][0]
dj = entity.get("detailsJson", "{}")
det = json.loads(dj) if isinstance(dj, str) else dj
edit_log = det.get("_editLog", [])

summary = (
    "Paul François Jean Nicolas, Vicomte de Barras (1755–1829) was a "
    "French Revolutionary politician who became the dominant figure of "
    "the Directory period (1795–1799) — effectively the most powerful "
    "man in France for four years. A Provençal nobleman who embraced "
    "the Revolution, Barras participated in Thermidor (the coup against "
    "Robespierre in July 1794), helped end the Terror, and then as one "
    "of five Directors controlled the government that tried to stabilize "
    "France between the Terror and Napoleon. He was notorious for his "
    "personal corruption, his flamboyant lifestyle, and his patronage — "
    "he introduced Napoleon Bonaparte to Joséphine de Beauharnais and "
    "was instrumental in Bonaparte's early military career.\n\n"
    "Napoleon's coup of 18 Brumaire (November 1799) ended the Directory "
    "and forced Barras into permanent retirement — the man who had been "
    "France's dominant politician for years ended as a pensioned exile.\n\n"
    "He was the quintessential figure of the corrupt, cynical Directory.\n\n"
    "'Power is always for sale — the question is the price.'"
)

hs = {
    "significanceScore": 9,
    "significanceNarrative": "Dominant figure of the French Directory (1795–1799) — effectively France's most powerful man for four years; Thermidor coup participant who ended the Terror; introduced Napoleon to Joséphine; patronized Napoleon's early career; overthrown by Napoleon's 18 Brumaire coup; epitome of the corrupt, cynical Directory.",
    "significanceCategory": "continental"
}

causes = [
    "The French Revolution's radicalisation — the escalating violence of the Terror that alienated moderate revolutionaries — created the conditions for the Thermidor coup that Barras helped lead",
    "The Directory's institutional weakness — the five-man executive's structural vulnerabilities, the ongoing war with European coalitions, and France's economic exhaustion — created the political instability that Barras dominated through manipulation rather than principle",
    "Napoleon Bonaparte's ambition — the young Corsican general's military brilliance and political determination — created the force that ultimately overthrew Barras and the Directory at 18 Brumaire"
]

effects = [
    "His Thermidor participation contributed to ending the Terror — the coup that removed Robespierre and halted the guillotine's mass executions",
    "His Directory leadership contributed to France's post-Terror political stabilization — the corrupt but functional regime that held France together through four years of constitutional crisis",
    "His patronage of Napoleon contributed directly to one of history's most consequential careers — the military and romantic connections that launched Bonaparte's path to power",
    "His overthrow by Napoleon's 18 Brumaire coup contributed to the Directory's historical legacy as a failed experiment in republican governance"
]

relationships = [
    {"target": "french-directory", "verb": "LEADS", "note": "Dominant Director 1795–1799"},
    {"target": "thermidor-coup", "verb": "PARTICIPATES_IN", "note": "Co-led coup against Robespierre July 1794"},
    {"target": "napoleon-bonaparte", "verb": "PATRONIZES", "note": "Introduced Napoleon to Joséphine; patronized early career"},
    {"target": "reign-of-terror", "verb": "ENDS", "note": "Thermidor coup ended the Terror"},
    {"target": "coup-of-18-brumaire", "verb": "OVERTHROWN_BY", "note": "Napoleon's 1799 coup forced Barras into exile"}
]

for field, old, new in [
    ("summary", entity.get("summary"), summary),
    ("importanceScore", entity.get("importanceScore"), 6),
    ("historicalSignificance", entity.get("historicalSignificance"), hs),
]:
    entity[field] = new
    edit_log.append({"timestamp": NOW, "editorId": EDITOR_ID, "field": field,
                     "oldValue": str(old)[:300], "newValue": str(new)[:300]})

for field, val in [("causes", causes), ("effects", effects), ("relationships", relationships)]:
    old = det.get(field, [])
    det[field] = val
    edit_log.append({"timestamp": NOW, "editorId": EDITOR_ID, "field": field,
                     "oldValue": json.dumps(old)[:300], "newValue": json.dumps(val)[:300]})

det["_editLog"] = edit_log
det["_unsyncedEdits"] = True
entity["_unsyncedEdits"] = True
entity["detailsJson"] = json.dumps(det, ensure_ascii=False)

with open(target, "w", encoding="utf-8") as f:
    json.dump(doc, f, indent=2, ensure_ascii=False)

slen = len(entity.get("summary", ""))
print(f"✓ {entity['name']} — sum={slen}c c={len(causes)} e={len(effects)}")
