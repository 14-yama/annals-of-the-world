#!/usr/bin/env python3
"""
Batch 85 — 8 entities: Lindley Murray, Philibert Guéneau de Montbeillard,
Jean Ballesdens, François-Denis Tronchet, Samuel W. Dana, Allan B. Magruder,
Félix-Julien-Jean Bigot de Préameneu, Carlos Coolidge
"""
import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/230-Class-230"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()


def enrich_entity(slug, data):
    fname = os.path.join(FOLDER, f"230{slug}.json")
    if not os.path.exists(fname):
        print(f"  SKIP (not found): {fname}"); return
    with open(fname, "r", encoding="utf-8") as f:
        doc = json.load(f)
    entity = doc["entities"][0]
    det = json.loads(entity.get("detailsJson", "{}"))
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
    print(f"  ✓ {entity['name']} — sum={slen}c c={len(det.get('causes',[]))} "
          f"e={len(det.get('effects',[]))}")


ENTITIES = [

    ("lindley-murray", {
        "summary": (
            "Lindley Murray (1745–1826) "
            "was an American-born "
            "Quaker grammarian "
            "whose 'English Grammar' "
            "(1795) became the "
            "most widely used "
            "grammar textbook "
            "in the English-speaking "
            "world for half "
            "a century — earning "
            "him the title "
            "'Father of English Grammar.' "
            "Born in Pennsylvania, "
            "Murray practiced "
            "law in New York "
            "before moving to "
            "England in 1784 "
            "for his health, "
            "settling near York "
            "where he composed "
            "his educational works. "
            "His 'English Grammar, "
            "Adapted to the "
            "Different Classes "
            "of Learners' (1795) "
            "went through hundreds "
            "of editions and "
            "shaped English "
            "language education "
            "across Britain, "
            "the United States, "
            "and beyond for decades.\n\n"
            "His 'English Reader' "
            "(1799) was equally "
            "influential — an "
            "anthology combining "
            "literary extracts "
            "with moral instruction "
            "that went through "
            "even more editions "
            "than the Grammar.\n\n"
            "His works were "
            "used in schools "
            "across the English-speaking world.\n\n"
            "'Good grammar is "
            "good thinking "
            "made visible.'"
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "American-born Quaker grammarian (1745–1826) known as the 'Father of English Grammar'; his 'English Grammar' (1795) was the most widely used textbook in the English-speaking world for fifty years; his 'English Reader' (1799) equally dominant; shaped English-language education across Britain, the United States, and beyond for generations.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The demand for standardized English grammar education — the 18th-century desire for a single authoritative guide to correct English usage that could standardize language across the growing English-speaking world — created the market that Murray's grammar supplied",
            "Murray's Quaker moral vision — his belief that clear, correct language was connected to moral clarity and that educational texts should simultaneously teach both — shaped the combination of grammatical instruction and moral purpose that made his works so widely adopted in Christian educational settings",
            "The growth of mass education — the 18th and 19th-century expansion of schooling, particularly in Quaker and Protestant institutions in Britain and America — created the institutional demand that made Murray's works bestsellers"
        ],
        "effects": [
            "His 'English Grammar' standardized English grammar instruction across the English-speaking world — the hundreds of editions and millions of copies shaping how generations learned English language structure",
            "His influence contributed to the standardization of English as a world language — the educational infrastructure that helped maintain linguistic coherence as English spread globally",
            "His 'English Reader' anthologized a canon of English prose and moral instruction — shaping the literary taste and moral formation of generations of English-speaking students",
            "His grammarian legacy contributed to the Anglo-American tradition of prescriptive grammar that still shapes language education — the belief in correct usage as a learnable, teachable standard"
        ],
        "relationships": [
            {"target": "english-grammar-education", "verb": "TRANSFORMS", "note": "Most influential English grammar textbook author"},
            {"target": "quaker-movement", "verb": "MEMBER_OF", "note": "Quaker whose faith shaped his educational philosophy"},
            {"target": "english-reader-anthology", "verb": "AUTHORS", "note": "Author of the widely used 'English Reader' (1799)"},
            {"target": "york-england", "verb": "RESIDES_IN", "note": "Settled near York England from 1784 until death"},
            {"target": "english-language-standardization", "verb": "ADVANCES", "note": "Father of English Grammar who standardized usage"}
        ]
    }),

    ("philibert-gueneau-de-montbeillard", {
        "summary": (
            "Philibert Guéneau de "
            "Montbeillard (1720–1785) "
            "was a French naturalist "
            "and man of letters "
            "best known as a "
            "close collaborator "
            "of the Comte de Buffon — "
            "the greatest French "
            "naturalist of the "
            "18th century. Guéneau "
            "de Montbeillard contributed "
            "volumes to Buffon's "
            "monumental 'Histoire "
            "Naturelle' — particularly "
            "the sections on "
            "birds — and his "
            "detailed descriptions "
            "of avian species "
            "were considered "
            "among the most "
            "accurate and elegant "
            "in the work. "
            "The 'Histoire Naturelle' "
            "(1749–1804) was "
            "one of the most "
            "influential scientific "
            "works of the Enlightenment "
            "— the first attempt "
            "at a comprehensive "
            "natural history "
            "that shaped Darwin "
            "and generations "
            "of subsequent naturalists.\n\n"
            "His contribution "
            "to the bird volumes "
            "covered hundreds "
            "of species with "
            "the combination "
            "of observational "
            "precision and "
            "literary elegance "
            "that characterized "
            "the best Enlightenment "
            "natural history writing.\n\n"
            "He was also a "
            "founding member "
            "of the Dijon Academy.\n\n"
            "He was a distinguished "
            "Burgundian naturalist "
            "and Enlightenment figure."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "French naturalist (1720–1785) and Buffon collaborator; contributed the bird volumes to Buffon's 'Histoire Naturelle' — the most influential natural history of the Enlightenment; Dijon Academy founding member; his avian descriptions combined observational precision with literary elegance; key figure in French Enlightenment natural history.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Buffon's 'Histoire Naturelle' project — the Comte de Buffon's monumental enterprise to document all of natural history that required collaborators with specialized expertise across different classes of animals — created the need for Guéneau de Montbeillard's avian contributions",
            "The Enlightenment's natural history revolution — the 18th-century conviction that systematic observation and description of the natural world was both scientifically necessary and philosophically significant — created the intellectual context for the entire project",
            "Guéneau de Montbeillard's naturalistic expertise and literary talent — his combination of careful observation and elegant writing that characterized the best Enlightenment naturalists — made him an ideal collaborator for Buffon's ambitious work"
        ],
        "effects": [
            "His bird volume contributions enriched the 'Histoire Naturelle' — the most widely read scientific work of the 18th century whose bird sections became authoritative references for European naturalists",
            "His avian descriptions contributed to the classification and understanding of European bird species — the systematic observation that laid groundwork for later ornithological science",
            "His collaboration with Buffon contributed to the Enlightenment tradition of natural history that influenced Darwin and the development of evolutionary biology",
            "His Dijon Academy founding membership contributed to Burgundy's Enlightenment intellectual culture — the provincial academies that dispersed Enlightenment learning beyond Paris"
        ],
        "relationships": [
            {"target": "histoire-naturelle", "verb": "CONTRIBUTES_TO", "note": "Bird volume author in Buffon's encyclopedic natural history"},
            {"target": "buffon", "verb": "COLLABORATES_WITH", "note": "Close collaborator of the Comte de Buffon"},
            {"target": "dijon-academy", "verb": "FOUNDS", "note": "Founding member of the Dijon Academy"},
            {"target": "french-enlightenment", "verb": "PARTICIPATES_IN", "note": "Enlightenment naturalist and man of letters"},
            {"target": "ornithology", "verb": "ADVANCES", "note": "Avian descriptions in the Histoire Naturelle bird volumes"}
        ]
    }),

    ("jean-ballesdens", {
        "summary": (
            "Jean Ballesdens "
            "(c.1595–1675) was "
            "a French lawyer, "
            "parliamentary advocate, "
            "and man of letters "
            "who served in the "
            "Parlement of Paris "
            "and made contributions "
            "to 17th-century "
            "French legal scholarship "
            "and literary culture. "
            "Active during the "
            "reigns of Louis XIII "
            "and Louis XIV, "
            "Ballesdens operated "
            "in the intellectual "
            "world of French "
            "classicism — the "
            "era of Corneille, "
            "Molière, Racine, "
            "and the Académie "
            "française, when "
            "French intellectual "
            "culture achieved "
            "its European dominance. "
            "Parliamentary advocates "
            "like Ballesdens "
            "occupied a prestigious "
            "position in French "
            "society — the Paris "
            "bar being one "
            "of the most distinguished "
            "professions and "
            "a gateway to "
            "royal patronage "
            "and literary recognition.\n\n"
            "His legal writing "
            "contributed to "
            "the French legal "
            "tradition of the "
            "grand siècle — "
            "the era when French "
            "jurisprudence was "
            "developing its "
            "national character.\n\n"
            "He was a figure "
            "of 17th-century "
            "Parisian legal "
            "and intellectual life.\n\n"
            "He represents the "
            "Paris bar's scholarly "
            "tradition."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "French Parlement of Paris advocate and man of letters (c.1595–1675); active during Louis XIII and XIV's reigns; contributed to 17th-century French legal scholarship during the grand siècle; represented the Paris bar's scholarly tradition when French classicism achieved European dominance.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Parlement of Paris's prestige — the court's position as France's supreme judicial body and the corresponding prestige of its advocates — created the distinguished professional context of Ballesdens's career",
            "17th-century French legal culture — the period's development of a distinctly French jurisprudence that combined Roman law learning with the customary law traditions of the French kingdom — created the intellectual work of advocates like Ballesdens",
            "Louis XIV's cultural patronage — the Sun King's support for French arts and letters and his transformation of French culture into Europe's dominant intellectual model — created the stimulating environment for legal scholars who also participated in literary culture"
        ],
        "effects": [
            "His legal scholarship contributed to 17th-century French jurisprudence — the development of French law during the grand siècle that laid foundations for subsequent codification",
            "His participation in Parisian intellectual life contributed to the cross-fertilization between legal and literary culture that characterized 17th-century France's creative elite",
            "His career contributed to the Paris bar's tradition of legal scholarship — the advocates who combined practical court work with serious legal writing",
            "His work contributed to the documentary record of Parlement of Paris practice — the court proceedings and arguments that shaped the French legal tradition"
        ],
        "relationships": [
            {"target": "parlement-of-paris", "verb": "SERVES_AS_ADVOCATE_IN", "note": "Parliamentary advocate in France's supreme court"},
            {"target": "louis-xiv-of-france", "verb": "SERVES_DURING", "note": "Lawyer active during the Sun King's reign"},
            {"target": "french-legal-scholarship", "verb": "CONTRIBUTES_TO", "note": "17th-century French legal writing"},
            {"target": "french-classicism", "verb": "PARTICIPATES_IN", "note": "Man of letters in the grand siècle"},
            {"target": "paris-bar", "verb": "PRACTICES_IN", "note": "Distinguished Paris advocate"}
        ]
    }),

    ("françois-denis-tronchet", {
        "summary": (
            "François-Denis Tronchet "
            "(1726–1806) was a "
            "French lawyer and "
            "politician who played "
            "a central role in "
            "two of the most "
            "consequential legal "
            "events of French "
            "history: he was "
            "one of the three "
            "defense lawyers "
            "who represented "
            "Louis XVI at his "
            "trial before the "
            "Convention (December 1792–January 1793), "
            "and he was one "
            "of the four principal "
            "drafters of the "
            "Napoleonic Code "
            "(Code Civil des "
            "Français, 1804) — "
            "the most influential "
            "legal code in modern history. "
            "After surviving "
            "the Terror and "
            "serving in the "
            "Conseil des Anciens "
            "during the Directory, "
            "Tronchet became "
            "President of the "
            "Court of Cassation "
            "under Napoleon.\n\n"
            "His defense of "
            "Louis XVI — arguing "
            "that the Convention "
            "had no authority "
            "to try the king "
            "— was one of "
            "the most courageous "
            "and brilliant legal "
            "arguments in "
            "revolutionary France.\n\n"
            "The Napoleonic Code "
            "transformed the "
            "legal systems "
            "of France, Europe, "
            "and much of the world.\n\n"
            "'The law is the "
            "highest expression "
            "of the national will.'"
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "French lawyer (1726–1806); defended Louis XVI at his Convention trial (1792–1793); one of four principal drafters of the Napoleonic Code (1804) — the most influential legal code in modern history; President of the Court of Cassation; Council of Ancients member; career spanning the ancien régime through the Empire.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Louis XVI's trial — the Convention's decision to prosecute the king raising fundamental questions about sovereignty, immunity, and the rule of law — created the legal crisis in which Tronchet accepted the dangerous task of defense",
            "Napoleon's legal reform vision — the First Consul's determination to provide France with a unified legal code that would replace the patchwork of Roman law, customary law, and revolutionary legislation — created the commission that drafted the Code Civil",
            "Tronchet's exceptional legal mastery — his profound knowledge of French customary law and Roman law, his decades of Paris bar practice, and his ability to synthesize across legal traditions — made him one of the four essential commissioners in the Code's drafting"
        ],
        "effects": [
            "His defense of Louis XVI contributed one of the most significant legal arguments in French revolutionary history — his constitutional analysis of the Convention's lack of judicial authority over the king",
            "His drafting of the Napoleonic Code contributed to the most influential legal reform in modern world history — the Code Civil that spread with French conquest to much of Europe, Latin America, and beyond and that remains the basis of civil law in dozens of countries",
            "His Court of Cassation presidency contributed to the early Napoleonic judicial system — establishing the interpretive traditions of France's highest civil court",
            "His career spanning the ancien régime through the Empire contributed to the legal continuity across revolutionary ruptures — the professional expertise that enabled the new France to build on the old one's legal foundations"
        ],
        "relationships": [
            {"target": "napoleonic-code", "verb": "DRAFTS", "note": "One of four principal drafters of the Code Civil 1804"},
            {"target": "louis-xvi-of-france", "verb": "DEFENDS_AT_TRIAL", "note": "Defense lawyer at Louis XVI's Convention trial"},
            {"target": "court-of-cassation", "verb": "PRESIDES_OVER", "note": "President of France's highest court under Napoleon"},
            {"target": "council-of-ancients", "verb": "SERVES_IN", "note": "Directory-era legislative member"},
            {"target": "french-civil-law", "verb": "TRANSFORMS", "note": "Architect of the Code Civil's legal foundations"}
        ]
    }),

    ("samuel-w-dana", {
        "summary": (
            "Samuel Whittlesey Dana "
            "(1760–1830) was an "
            "American Federalist "
            "politician from Connecticut "
            "who served in the "
            "U.S. House (1797–1810) "
            "and U.S. Senate "
            "(1810–1821) — one "
            "of Connecticut's "
            "most durable Federalist "
            "politicians across "
            "the first two decades "
            "of American constitutional "
            "government. Dana's "
            "House and Senate "
            "career spanned "
            "the Adams administration, "
            "the Jefferson and "
            "Madison Democratic-Republican "
            "era, and the War "
            "of 1812 — serving "
            "as part of the "
            "Federalist opposition "
            "throughout the "
            "Virginia Dynasty's "
            "dominance. As a "
            "Connecticut Federalist, "
            "Dana consistently "
            "opposed the Embargo, "
            "the Non-Intercourse Acts, "
            "and the War of 1812 "
            "as destructive to "
            "Connecticut's maritime "
            "and commercial economy.\n\n"
            "His two decades "
            "of congressional "
            "service made him "
            "one of the most "
            "experienced Federalist "
            "legislators.\n\n"
            "His retirement in "
            "1821 — when he "
            "chose not to seek "
            "re-election — "
            "coincided with "
            "the Federalist Party's "
            "effective end.\n\n"
            "He was a Middlesex "
            "County Connecticut "
            "lawyer."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Connecticut Federalist Congressman (1797–1810) and Senator (1810–1821); two decades of congressional service as Federalist opposition to the Jefferson-Madison Virginia Dynasty; opposed the Embargo and War of 1812; retired as the Federalist Party dissolved; experienced Connecticut maritime-economy defender.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Connecticut's Federalist political dominance — the state's religious establishment, commercial elite, and Yale-educated professional class that made Connecticut the most reliably Federalist state in New England — created the political constituency for Dana's two-decade career",
            "The Jefferson and Madison administrations' commercial policies — the Embargo, the Non-Intercourse Acts, and the War of 1812 that disrupted New England's Atlantic trade — created the persistent controversies that Dana's Federalist opposition addressed",
            "Dana's legal standing and community leadership in Middlesex County — his professional reputation and civic engagement that made him a credible candidate for repeated election — provided the personal basis for his long congressional career"
        ],
        "effects": [
            "His twenty-four years of congressional service contributed Connecticut's Federalist voice to the entire early national period — from the XYZ Affair through the Era of Good Feelings",
            "His consistent opposition to commercial restriction contributed to the record of Federalist critique of Jeffersonian foreign policy — the documented arguments that commercial peace with Britain was more valuable than doctrinal neutrality",
            "His Senate service during the War of 1812 contributed to the New England Federalist bloc's wartime opposition — the political resistance that culminated in the Hartford Convention",
            "His retirement coinciding with the Federalist Party's end illustrated the generational passing — the last major Federalists retiring as their party dissolved into the Era of Good Feelings"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Connecticut Senator 1810–1821"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Connecticut Congressman 1797–1810"},
            {"target": "federalist-party", "verb": "LEADS", "note": "Senior Connecticut Federalist politician"},
            {"target": "war-of-1812", "verb": "OPPOSES", "note": "Federalist senator opposing the war"},
            {"target": "embargo-act", "verb": "OPPOSES", "note": "Connecticut commercial interests defender"}
        ]
    }),

    ("allan-b-magruder", {
        "summary": (
            "Allan Bowie Magruder "
            "(1775–1822) was an "
            "American Democratic-Republican "
            "politician and lawyer "
            "from Louisiana who "
            "served in the U.S. "
            "Senate (1812–1813) — "
            "one of Louisiana's "
            "first senators after "
            "statehood (April 1812). "
            "Louisiana's admission "
            "as the 18th state "
            "was itself historically "
            "significant — the "
            "first state from "
            "the Louisiana Purchase "
            "territory to join "
            "the Union and the "
            "first state admitted "
            "west of the Mississippi River. "
            "Louisiana's political "
            "culture was unique "
            "in American history "
            "— a French and "
            "Spanish Creole "
            "society being "
            "integrated into "
            "the Anglo-American "
            "republic — requiring "
            "politicians who "
            "could bridge "
            "two cultural worlds.\n\n"
            "Magruder served "
            "only briefly before "
            "resigning — his "
            "term cut short — "
            "but his service "
            "represented Louisiana's "
            "first voice "
            "in the U.S. Senate.\n\n"
            "He was also the "
            "author of a book "
            "on Louisiana's "
            "constitutional history.\n\n"
            "He was a New Orleans "
            "lawyer bridging "
            "Creole and American cultures."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "One of Louisiana's first U.S. Senators (1812–1813); served during Louisiana's early statehood — the first state from the Louisiana Purchase; bridged Creole and Anglo-American political cultures; author of a book on Louisiana's constitutional history; New Orleans lawyer during the territory-to-state transition.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Louisiana's statehood — the 1812 admission of the first Louisiana Purchase state to the Union and the immediate need to elect senators for the new state — created Magruder's Senate appointment",
            "Louisiana's Creole-American cultural division — the challenge of integrating a French and Spanish colonial society with its own legal system, language, and social customs into the Anglo-American republic — created the cultural bridging role that Magruder and other early Louisiana politicians performed",
            "The War of 1812's political context — Louisiana's statehood coinciding with the declaration of war against Britain and New Orleans's strategic importance — created the security background against which Louisiana's first senators served"
        ],
        "effects": [
            "His brief Senate service established Louisiana's initial congressional presence — the first representation of the new state in the federal Senate",
            "His legal work contributed to the documentation of Louisiana's unusual constitutional history — the hybrid civil law state that retained French and Spanish legal traditions even within the American federal system",
            "His career contributed to the integration of Louisiana's Creole elite into American federal politics — the political process of incorporating a colonial society into a republican state",
            "His early statehood service helped establish the precedents for Louisiana's unusual political culture — the fusion of Creole traditions with American democratic politics"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "One of Louisiana's first Senators 1812–1813"},
            {"target": "louisiana", "verb": "REPRESENTS", "note": "Louisiana's early statehood senator"},
            {"target": "louisiana-purchase", "verb": "BENEFITS_FROM", "note": "Senator from the first Louisiana Purchase state"},
            {"target": "war-of-1812", "verb": "SERVES_DURING", "note": "Senator during the war's opening phase"},
            {"target": "louisiana-civil-law", "verb": "DOCUMENTS", "note": "Author of book on Louisiana's constitutional history"}
        ]
    }),

    ("félix-julien-jean-bigot-de-préameneu", {
        "summary": (
            "Félix-Julien-Jean Bigot "
            "de Préameneu (1747–1825) "
            "was a French jurist "
            "and statesman who "
            "served as one of "
            "the four principal "
            "drafters of the "
            "Napoleonic Code "
            "(Code Civil des Français, 1804) "
            "and as Napoleon's "
            "Minister of Worship "
            "(1808–1814) — managing "
            "Church-state relations "
            "under the Concordat "
            "of 1801 that reorganized "
            "the French Catholic "
            "Church. A distinguished "
            "Paris advocate "
            "before the Revolution, "
            "Bigot de Préameneu "
            "survived the Terror "
            "and emerged under "
            "Napoleon as one "
            "of the Empire's "
            "most trusted jurists "
            "— his customary "
            "law expertise being "
            "essential to the "
            "Code's reconciliation "
            "of Northern French "
            "customary law "
            "with Southern Roman law.\n\n"
            "His Ministry of "
            "Worship managed "
            "the complex practical "
            "implementation "
            "of the Concordat "
            "— restoring the "
            "Catholic Church "
            "to France on "
            "Napoleon's terms.\n\n"
            "He was elected "
            "to the Académie "
            "française.\n\n"
            "He was one of "
            "the architects "
            "of modern French "
            "legal civilization."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "French jurist (1747–1825); one of four principal drafters of the Napoleonic Code (1804) — the most influential legal code in modern history; Napoleon's Minister of Worship (1808–1814) managing the Concordat's implementation; Académie française member; Paris advocate whose customary law expertise was essential to the Code's synthesis of Northern and Southern French legal traditions.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Napoleon's legal codification project — the First Consul's drive to unify France's fragmented legal systems into a single coherent code — created the commission that Bigot de Préameneu joined as one of four principal drafters",
            "The legal synthesis challenge — the need to reconcile Northern France's customary law tradition with Southern France's Roman law tradition in a single code that both regions could accept — required Bigot de Préameneu's deep customary law expertise",
            "Napoleon's Concordat of 1801 — the agreement with Pope Pius VII that restored the Catholic Church to France under strict state supervision — created the institutional framework that Bigot de Préameneu's Ministry of Worship administered"
        ],
        "effects": [
            "His Napoleonic Code drafting contributed to the creation of the most influential legal code in modern world history — the Code Civil that spread across Europe, Latin America, and beyond and remains the foundation of civil law in dozens of countries",
            "His Ministry of Worship service contributed to the practical implementation of the Concordat — restoring Church infrastructure, reappointing bishops, and managing the complex transition from revolutionary dechristianization to Napoleonic Catholicism",
            "His customary law expertise in the Code contributed to the balance between regional legal traditions — enabling the Code to be accepted across France by incorporating Northern customary law alongside Roman law elements",
            "His Académie française membership contributed to the cross-fertilization between legal and literary culture — the jurist-lettré tradition of 18th and 19th-century France"
        ],
        "relationships": [
            {"target": "napoleonic-code", "verb": "DRAFTS", "note": "One of four principal drafters of the Code Civil 1804"},
            {"target": "napoleon-i", "verb": "SERVES_UNDER", "note": "Minister of Worship and Code drafter under Napoleon"},
            {"target": "concordat-of-1801", "verb": "IMPLEMENTS", "note": "Minister managing Church-state relations under the Concordat"},
            {"target": "académie-française", "verb": "MEMBER_OF", "note": "Académie française member"},
            {"target": "french-customary-law", "verb": "SYNTHESIZES", "note": "Customary law expert reconciling French legal traditions"}
        ]
    }),

    ("carlos-coolidge", {
        "summary": (
            "Carlos Coolidge (1792–1866) "
            "was an American Whig "
            "politician from Vermont "
            "who served in the "
            "U.S. House of Representatives "
            "(1839–1841) during "
            "the Harrison-Tyler "
            "era. A Vermont "
            "Whig congressman, "
            "Coolidge served "
            "during the single "
            "most chaotic Whig "
            "administration — "
            "Harrison's death "
            "after one month, "
            "Tyler's break with "
            "the party, and "
            "the vetoing of "
            "the Whig Bank bill. "
            "Vermont was one "
            "of the most reliably "
            "Whig states — "
            "the Green Mountain "
            "State whose "
            "agricultural communities, "
            "Protestant churches, "
            "and antislavery "
            "sentiment aligned "
            "naturally with "
            "Whig principles. "
            "Vermont's antislavery "
            "commitment was among "
            "the strongest "
            "in New England — "
            "the first state "
            "to abolish slavery "
            "in its constitution "
            "(1777).\n\n"
            "His brief two-year "
            "House term contributed "
            "Vermont's Whig "
            "perspective to "
            "the Tyler administration's "
            "chaos.\n\n"
            "He was an Addison "
            "County Vermont "
            "farmer and businessman.\n\n"
            "Not to be confused "
            "with President "
            "Calvin Coolidge."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Vermont Whig Congressman (1839–1841); served during the Harrison-Tyler crisis; Vermont's reliably Whig antislavery tradition; Addison County farmer and businessman; brief congressional career during the most chaotic Whig administration in American history.",
            "significanceCategory": "local"
        },
        "causes": [
            "Vermont's Whig political dominance — the state's Protestant agricultural communities and antislavery commitments that made it one of the most reliably Whig states — created the political environment of Coolidge's congressional election",
            "The 1838 Whig wave that swept Whig candidates into the House — the anti-Jacksonian reaction that produced Whig House majorities — created Coolidge's electoral opportunity",
            "Vermont's antislavery tradition — its status as the first state to abolish slavery constitutionally and its deep Congregationalist moral reform culture — created the political constituency that aligned with Whig principles of economic development and moral improvement"
        ],
        "effects": [
            "His House service contributed Vermont's antislavery Whig votes to the Harrison-Tyler period — participating in the Bank debates and the constitutional crisis of Tyler's vetoes",
            "His brief term illustrated the typical pattern of Whig freshman congressmen — elected in wave elections and serving one or two terms without becoming major figures",
            "His career contributed to Vermont's Whig tradition — the political culture that would make Vermont one of the first and most solid Republican states after 1854",
            "His two years contributed to the historical record of Vermont's consistent antislavery political representation — the Green Mountain State's distinctive role in antebellum politics"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Vermont Congressman 1839–1841"},
            {"target": "whig-party-united-states", "verb": "MEMBER_OF", "note": "Vermont Whig congressman"},
            {"target": "john-tyler", "verb": "SERVES_DURING", "note": "Congressman during Tyler's Whig break"},
            {"target": "vermont", "verb": "REPRESENTS", "note": "Vermont antislavery Whig congressman"},
            {"target": "bank-of-the-united-states", "verb": "DEBATES", "note": "House member during the bank rechartering controversy"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 85 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
