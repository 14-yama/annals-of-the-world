#!/usr/bin/env python3
"""
Batch 100 — 8 entities: Anthony New, Antoine Furetière, Antoine-Martin Chaumont
de la Galaizière, Antoine-Quentin Fouquier-Tinville, Antoine Roy,
Archibald Roane, Archibald Yell, Artemas Ward
"""
import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/230-Class-230"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()


def enrich(slug, data):
    fname = os.path.join(FOLDER, f"230{slug}.json")
    if not os.path.exists(fname):
        print(f"  SKIP: {fname}"); return
    with open(fname, "r", encoding="utf-8") as f:
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
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    slen = len(entity.get("summary", ""))
    print(f"  ✓ {entity['name']} — sum={slen}c c={len(det.get('causes',[]))} e={len(det.get('effects',[]))}")


ENTITIES = [

    ("anthony-new", {
        "summary": (
            "Anthony New (1747–1833) was an American Democratic-Republican "
            "politician from Virginia and Kentucky who served in the U.S. House "
            "across multiple terms (1793–1805 and 1811–1813 and 1817–1819). "
            "His career illustrated the pattern of the frontier politician who "
            "moved west with the expanding republic — he represented Virginia "
            "first and then Kentucky as settlement pushed into the interior. "
            "His congressional service spanned the critical decades of the "
            "early republic — the Federalist opposition years, the Jefferson "
            "presidency's domestic and foreign policy, the War of 1812, "
            "and the post-war nationalism that followed. He was a "
            "Jeffersonian Republican throughout — a consistent opponent "
            "of Federalist centralization.\n\n"
            "He was a Virginia and Kentucky Jeffersonian politician.\n\n"
            "He served in Congress across three decades of the early republic.\n\n"
            "He was the frontier Democrat who followed the republic westward."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Virginia and Kentucky Democratic-Republican congressman across multiple terms (1793–1805, 1811–1813, 1817–1819); frontier politician who moved west with the expanding republic; Jeffersonian Republican spanning the Federalist opposition years, Jefferson presidency, War of 1812, and post-war nationalism; consistent opponent of Federalist centralization.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Jefferson's Democratic-Republican coalition — the political movement opposing Federalist centralization — created the political identity that Anthony New embodied across three decades",
            "Kentucky's frontier political development — the state's rapid settlement and its Jeffersonian political culture — created the western political base from which New drew support",
            "The early republic's political oscillations — the Federalist era, the Jeffersonian revolution, the War of 1812, and post-war nationalism — created the shifting political landscape through which New's career navigated"
        ],
        "effects": [
            "His Virginia and Kentucky congressional service contributed to the Democratic-Republican coalition's strength in both the tidewater and frontier regions",
            "His long career contributed to the historical record of Jeffersonian Republican politics across three decades",
            "His frontier transition from Virginia to Kentucky contributed to the documentation of the expanding early republic's political patterns",
            "His War of 1812 service contributed Kentucky's frontier pro-war perspective to the wartime Congress"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Multi-term Virginia and Kentucky congressman 1793–1819"},
            {"target": "thomas-jefferson", "verb": "SUPPORTS", "note": "Consistent Jeffersonian Republican across three decades"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "Frontier Jeffersonian opponent of Federalist centralization"},
            {"target": "kentucky", "verb": "REPRESENTS", "note": "Moved west to represent Kentucky's frontier constituency"},
            {"target": "war-of-1812", "verb": "SERVES_DURING", "note": "Congressman during the War of 1812"}
        ]
    }),

    ("antoine-furetiere", {
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
    }),

    ("antoine-martin-chaumont-de-la-galaiziere", {
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
    }),

    ("antoine-quentin-fouquier-tinville", {
        "summary": (
            "Antoine-Quentin Fouquier-Tinville (1746–1795) was the Public "
            "Prosecutor of the Revolutionary Tribunal during the French "
            "Revolution's Reign of Terror (1793–1794) — the man most directly "
            "responsible for sending thousands of people to the guillotine. "
            "As the Tribunal's relentless prosecutor, Fouquier-Tinville "
            "processed the trials of Marie Antoinette, the Girondins, "
            "the Dantonists, and thousands of ordinary suspects with brutal "
            "efficiency. He treated the Revolutionary Tribunal as an "
            "administrative machine — minimal defense, predetermined verdicts, "
            "and maximum throughput. After Thermidor, he was tried and "
            "guillotined in 1795 — poetic justice for the man who had sent "
            "so many others to the same fate.\n\n"
            "'The accusation is the proof.' — his judicial philosophy.\n\n"
            "He was the Terror's most efficient instrument.\n\n"
            "He prosecuted Marie Antoinette and was himself guillotined."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Public Prosecutor of the Revolutionary Tribunal during the Reign of Terror (1793–1794); sent thousands to the guillotine including Marie Antoinette, the Girondins, and the Dantonists; treated the Tribunal as a bureaucratic death machine; himself guillotined after Thermidor in 1795; the most personally responsible individual for the Terror's judicial murders.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Revolutionary Tribunal's creation (March 1793) — the Jacobin Committee of Public Safety's instrument for political terror — created the institutional machinery that Fouquier-Tinville operated as public prosecutor",
            "The Committee of Public Safety's political terror — Robespierre and Saint-Just's systematic elimination of political opponents — created the political directives that Fouquier-Tinville translated into indictments and convictions",
            "The French Revolution's radical phase — the paranoid atmosphere of the Year Two in which conspiracy and counter-revolution were seen everywhere — created the judicial culture in which accusation could function as proof"
        ],
        "effects": [
            "His Revolutionary Tribunal prosecutions contributed directly to the Reign of Terror's death toll — the thousands guillotined through his efficient judicial machinery",
            "His prosecution of Marie Antoinette contributed to the most symbolic trial of the Terror — the execution of the former queen of France",
            "His own guillotining after Thermidor contributed to the Terror's self-destructive arc — the judge who became the judged",
            "His career contributed to the historical definition of judicial terror — the use of courts as instruments of political murder"
        ],
        "relationships": [
            {"target": "revolutionary-tribunal", "verb": "PROSECUTES_FOR", "note": "Public Prosecutor sending thousands to the guillotine 1793–1794"},
            {"target": "reign-of-terror", "verb": "IMPLEMENTS", "note": "The Terror's most efficient judicial instrument"},
            {"target": "marie-antoinette", "verb": "PROSECUTES", "note": "Prosecuted the former queen of France"},
            {"target": "thermidor-coup", "verb": "ARRESTED_AFTER", "note": "Tried and guillotined in 1795 after Thermidor"},
            {"target": "committee-of-public-safety", "verb": "EXECUTES_DIRECTIVES_OF", "note": "Translated Jacobin political terror into indictments"}
        ]
    }),

    ("antoine-roy", {
        "summary": (
            "Antoine Roy (1764–1847) was a French lawyer, politician, and "
            "financier who served as Minister of Finance of France under "
            "three different governments — the Restoration, the Hundred Days, "
            "and again under Louis XVIII. His financial expertise and "
            "political flexibility made him one of the most durable figures "
            "of the post-Revolutionary French political world. As finance "
            "minister, he worked to stabilize French public finances after "
            "the disruptions of the Revolution and Napoleonic wars — the "
            "enormous debts, the currency chaos, and the need to restore "
            "France's international credit. He was also a Peer of France "
            "and a member of the Chamber of Peers under the Restoration.\n\n"
            "His financial expertise connected the old regime's legal culture "
            "to the new constitutional monarchy's fiscal needs.\n\n"
            "He was a Restoration finance minister and Peer of France.\n\n"
            "He helped stabilize French finances after Napoleon."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "French Minister of Finance under three governments (Restoration, Hundred Days, Louis XVIII); worked to stabilize French public finances after the Revolution and Napoleonic wars; Peer of France and Chamber of Peers member under the Restoration; legal and financial expertise bridging old regime culture and constitutional monarchy; durable post-Revolutionary political figure.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The French Revolution's financial disruption — the enormous debts, currency chaos, and fiscal disorganization left by the Revolution and Napoleonic wars — created the stabilization challenges that Roy addressed as finance minister",
            "The Bourbon Restoration's need for fiscal credibility — the restored monarchy's requirement to establish France's international credit and governmental legitimacy — created the political demand for experienced financial expertise",
            "Roy's legal and financial background — his training as a lawyer with expertise in French financial law and public credit — created the professional qualifications that made him indispensable to multiple governments"
        ],
        "effects": [
            "His finance ministry work contributed to French fiscal stabilization after the Revolutionary and Napoleonic disruptions",
            "His service across multiple governments contributed to the Restoration's fiscal credibility and France's recovery of international credit",
            "His Chamber of Peers membership contributed to the Restoration's legislative institutions",
            "His career contributed to the model of the politically flexible technocrat who survived multiple French regime changes through indispensable expertise"
        ],
        "relationships": [
            {"target": "french-restoration", "verb": "SERVES_AS_FINANCE_MINISTER_UNDER", "note": "Multiple finance ministry appointments under Restoration governments"},
            {"target": "louis-xviii", "verb": "SERVES", "note": "Finance minister under Louis XVIII"},
            {"target": "chamber-of-peers", "verb": "SERVES_IN", "note": "Peer of France and Chamber of Peers member"},
            {"target": "hundred-days", "verb": "SERVES_DURING", "note": "Finance minister during Napoleon's Hundred Days"},
            {"target": "french-public-finance", "verb": "STABILIZES", "note": "Worked to restore French fiscal order after Revolution and Napoleon"}
        ]
    }),

    ("archibald-roane", {
        "summary": (
            "Archibald Roane (1759–1819) was an American Democratic-Republican "
            "politician and judge from Tennessee who served as the second "
            "Governor of Tennessee (1801–1803). His governorship came at a "
            "politically charged moment — he succeeded John Sevier and lost "
            "re-election to Sevier in 1803 in a bitter contest that involved "
            "a famous confrontation with a young Andrew Jackson. Jackson "
            "backed Roane politically but the personal animosities that "
            "characterized Tennessee's frontier politics produced the famous "
            "Sevier-Jackson conflict. Roane also served as a judge on the "
            "Tennessee Superior Court and the State Supreme Court, giving "
            "him a career that spanned the executive and judicial branches "
            "of Tennessee's early state government.\n\n"
            "He was a Washington County Tennessee lawyer.\n\n"
            "He was a frontier governor of early Tennessee.\n\n"
            "He was caught between Sevier and Jackson in Tennessee politics."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Second Governor of Tennessee (1801–1803); caught between John Sevier and Andrew Jackson in frontier Tennessee politics; Tennessee Superior Court and State Supreme Court judge; Washington County lawyer; served in both executive and judicial branches of Tennessee's early state government; lost 1803 re-election to Sevier in bitter frontier political contest.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Tennessee's frontier political culture — the state's fierce partisan rivalries, personal politics, and strong personalities like Sevier and Jackson — created the environment in which Roane's governorship and political fate were embedded",
            "Tennessee statehood (1796) — the young state's development of its governmental institutions — created the political offices and judicial positions that Roane held across his career",
            "Andrew Jackson's political rise — the young frontier lawyer and militia officer's entry into Tennessee politics — created the political alliances and conflicts that shaped Roane's career"
        ],
        "effects": [
            "His governorship contributed to Tennessee's early state executive tradition",
            "His judicial service contributed to Tennessee's development of its superior and supreme court institutions",
            "His political fate contributed to the historical record of the Sevier-Jackson rivalry that defined Tennessee's frontier politics",
            "His career contributed to the documentation of the early Tennessee political class"
        ],
        "relationships": [
            {"target": "tennessee", "verb": "GOVERNS", "note": "Second Governor of Tennessee 1801–1803"},
            {"target": "john-sevier", "verb": "SUCCEEDS_AND_LOSES_TO", "note": "Succeeded Sevier as governor then lost re-election to him 1803"},
            {"target": "andrew-jackson", "verb": "ALLIED_WITH", "note": "Jackson backed Roane in the Sevier-Jackson frontier rivalry"},
            {"target": "tennessee-supreme-court", "verb": "SERVES_ON", "note": "Tennessee Superior Court and State Supreme Court judge"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "Tennessee Jeffersonian Republican politician"}
        ]
    }),

    ("archibald-yell", {
        "summary": (
            "Archibald Yell (1797–1847) was an American Democratic politician "
            "from Arkansas who served as U.S. Representative (1836–1839 and "
            "1845–1846) and as Governor of Arkansas (1840–1844). He was one "
            "of the most colorful figures of Arkansas's early statehood — a "
            "frontier lawyer, judge, and politician who embodied the "
            "rough-hewn democratic culture of the antebellum southwestern "
            "frontier. He resigned his congressional seat in 1846 to serve "
            "in the Mexican-American War, commanding an Arkansas cavalry "
            "regiment. He was killed at the Battle of Buena Vista (1847) — "
            "dying in the charge that he led against Mexican lancers.\n\n"
            "His death in battle made him a hero of Arkansas's frontier tradition.\n\n"
            "He was the Arkansas governor who died at Buena Vista.\n\n"
            "'He rode into battle as he governed — full speed ahead.'"
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Arkansas Democratic congressman and Governor (1840–1844) who resigned his seat to serve in the Mexican-American War and was killed at the Battle of Buena Vista (1847); one of the most colorful figures of Arkansas's early statehood; frontier lawyer-judge-politician; Arkansas cavalry commander who died leading a charge against Mexican lancers.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Arkansas statehood (1836) — the frontier state's entry into the Union — created the political offices and institutions that Yell's career populated",
            "Manifest Destiny and the Mexican-American War — the expansionist ideology and the 1846 declaration of war against Mexico — created the military opportunity that Yell embraced, resigning his congressional seat to fight",
            "Arkansas's frontier democratic culture — the state's rough-hewn political tradition that valued military service and personal courage — created the ethos that made Yell's battlefield death heroic rather than tragic"
        ],
        "effects": [
            "His gubernatorial service contributed to Arkansas's early state governance and frontier political development",
            "His Mexican-American War service contributed to Arkansas's military presence in the war and to Polk's expansionist campaign",
            "His death at Buena Vista contributed to the mythology of Arkansas frontier heroism",
            "His career contributed to the documentation of the southwestern frontier politician who moved between law, politics, and military command"
        ],
        "relationships": [
            {"target": "arkansas", "verb": "GOVERNS", "note": "Governor of Arkansas 1840–1844"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Arkansas congressman 1836–1839 and 1845–1846"},
            {"target": "mexican-american-war", "verb": "DIES_FIGHTING_IN", "note": "Resigned seat to command Arkansas cavalry — killed at Buena Vista 1847"},
            {"target": "battle-of-buena-vista", "verb": "DIES_AT", "note": "Killed leading cavalry charge against Mexican lancers 1847"},
            {"target": "democratic-party-united-states", "verb": "MEMBER_OF", "note": "Arkansas Jacksonian Democrat"}
        ]
    }),

    ("artemas-ward", {
        "summary": (
            "Artemas Ward (1727–1800) was an American Revolutionary War general "
            "and Massachusetts politician who served as the first commanding "
            "general of the Continental Army before George Washington's arrival. "
            "When the Siege of Boston began in April 1775, Ward was the highest "
            "ranking American officer — he commanded the Massachusetts provincial "
            "forces that surrounded the British-held city until Washington arrived "
            "in July 1775 to take supreme command. Ward's command included the "
            "Battle of Bunker Hill (June 1775). He later served in the "
            "Continental Congress and in the U.S. House (1791–1795). "
            "His role as the first Continental commander — before Washington — "
            "places him among the founding generation's most important military figures.\n\n"
            "He was the general who commanded at Bunker Hill.\n\n"
            "He was Washington's predecessor as America's first army commander.\n\n"
            "'He held Boston's siege until Washington could come.'"
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "First commanding general of the Continental Army — commanded Massachusetts forces at the Siege of Boston before George Washington arrived July 1775; commanded at the Battle of Bunker Hill (June 1775); Continental Congress delegate and U.S. Congressman; Washington's immediate predecessor as supreme American commander; Shrewsbury Massachusetts Founding Father.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Battles of Lexington and Concord (April 1775) — the opening engagements of the Revolutionary War that triggered the Siege of Boston — created the military emergency in which Ward became the first Continental commanding officer",
            "Massachusetts's provincial military tradition — the colony's established militia system and Ward's senior rank in the provincial forces — created the command structure that made Ward the natural first commander",
            "The Continental Congress's need for military leadership — the new congress's decision to create a Continental Army and appoint Washington as commander-in-chief — created the handoff from Ward to Washington that defined the army's founding"
        ],
        "effects": [
            "His command at the Siege of Boston contributed to holding the American positions around the city until Washington arrived — the critical first months of the Continental Army's existence",
            "His presence at Bunker Hill contributed to the Battle's outcome — the first major engagement of the Revolutionary War",
            "His handoff to Washington contributed to the Continental Army's transition to unified national command",
            "His career contributed to the historical record of the founding generation's first military leadership — the men who held the line before Washington arrived"
        ],
        "relationships": [
            {"target": "continental-army", "verb": "COMMANDS", "note": "First commanding general before Washington's arrival July 1775"},
            {"target": "siege-of-boston", "verb": "COMMANDS_DURING", "note": "Commanded American forces surrounding British Boston April–July 1775"},
            {"target": "battle-of-bunker-hill", "verb": "COMMANDS_AT", "note": "Commanded at Bunker Hill June 1775"},
            {"target": "george-washington", "verb": "PRECEDES_AS_COMMANDER", "note": "Washington's immediate predecessor as supreme American commander"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Massachusetts congressman 1791–1795"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 100 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich(slug, data)
    print("Done.")
