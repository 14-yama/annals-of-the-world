#!/usr/bin/env python3
"""
Batch 28 — 8 entities: Robert Trimble, Ahmad ibn Abi Du'ad, Louis-Joseph Papineau,
James Duane, Egbert Benson, Zinovios Valvis, Willard Hall, Benjamin Parke
editorId: vscode-copilot
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

    # 1 — Robert Trimble (SCOTUS Justice 1826–1828)
    ("robert-trimble", {
        "summary": (
            "Robert Trimble (1776–1828) was an American jurist from Kentucky who "
            "served as an Associate Justice of the United States Supreme Court from "
            "1826 until his sudden death in 1828 — a tenure of just over two years "
            "that nevertheless produced significant majority opinions under Chief Justice "
            "John Marshall and established him as a capable jurist who might have had "
            "a longer impact on American constitutional law had he lived. He was "
            "nominated by President John Quincy Adams — making him one of only two "
            "justices Adams appointed — and he was confirmed despite Senate opposition "
            "from Jacksonian Democrats who were already opposing Adams's appointments.\n\n"
            "Trimble's career before reaching the Supreme Court included service as "
            "a justice on the Kentucky Court of Appeals — Kentucky's highest court — "
            "and as the United States District Judge for the District of Kentucky "
            "(1817–1826), where he developed expertise in Kentucky land law and "
            "federal jurisdiction. His appointment to the Supreme Court reflected "
            "his established reputation in federal jurisprudence and his alignment "
            "with the nationalist constitutional philosophy of the Marshall Court.\n\n"
            "His most notable Supreme Court opinion was in Ogden v. Saunders (1827) — "
            "the famous case in which Chief Justice Marshall wrote his only constitutional "
            "dissent — where Trimble joined the majority in holding that state insolvency "
            "laws could apply to debts contracted after the law's enactment, limiting "
            "the Contracts Clause against state interference with existing contracts. "
            "His early death at 52 cut short a judicial career that showed considerable "
            "promise in the Marshall Court era.\n\n"
            "His death prompted President Jackson (who had just taken office) to "
            "nominate John McLean as his replacement — introducing a more Jacksonian "
            "justice into the Marshall Court."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Associate Justice of the US Supreme Court (1826–1828) nominated by John Quincy Adams; authored significant opinions including his participation in Ogden v. Saunders (1827); former Kentucky Court of Appeals justice and US District Judge; his brief tenure ended with his early death at 52.",
            "significanceCategory": "regional"
        },
        "causes": [
            "President John Quincy Adams's need for a Supreme Court nominee who shared the Marshall Court's nationalist constitutional philosophy — and Trimble's established reputation in Kentucky federal jurisprudence — led to his appointment",
            "His years as US District Judge for Kentucky (1817–1826) developed the federal judicial expertise and reputation that qualified him for Supreme Court appointment",
            "The Marshall Court's engagement with fundamental questions of federal versus state power — including the Contracts Clause cases — created the constitutional environment in which Trimble's brief tenure produced its most significant opinions"
        ],
        "effects": [
            "His majority opinion in Ogden v. Saunders (1827) — the case that produced Marshall's only constitutional dissent — established the principle that state insolvency laws could apply to debts contracted after the law's enactment, significantly limiting the Contracts Clause",
            "His early death created the opening for President Jackson to appoint John McLean — introducing a more politically Jacksonian voice into the Marshall Court and beginning the shift away from Marshall's nationalist constitutional hegemony",
            "His brief Supreme Court service demonstrated the potential impact of Adams's judicial appointments — and his death was a significant loss for the Adams constitutional nationalist tradition on the Court",
            "His Kentucky District Court tenure (1817–1826) contributed to the development of federal judicial authority in the western states during the critical formative period of American federal jurisdiction"
        ],
        "relationships": [
            {"entity": "John Quincy Adams (US President)", "relationship": "NOMINATED_BY", "note": "Nominated to the Supreme Court by President John Quincy Adams — one of only two justices Adams appointed"},
            {"entity": "Chief Justice John Marshall", "relationship": "SERVED_UNDER_ON_SUPREME_COURT", "note": "Served on the Marshall Court (1826–1828) — among the most consequential periods in American constitutional development"},
            {"entity": "Ogden v. Saunders (1827)", "relationship": "JOINED_MAJORITY_IN", "note": "Joined the majority in Ogden v. Saunders — the case that produced Marshall's only constitutional dissent — limiting the Contracts Clause"},
            {"entity": "US District Court (District of Kentucky)", "relationship": "DISTRICT_JUDGE_OF_1817-1826", "note": "Served as US District Judge for the District of Kentucky (1817–1826) — developing the federal jurisprudence that qualified him for SCOTUS"},
            {"entity": "John McLean (SCOTUS Justice)", "relationship": "REPLACED_ON_COURT_BY", "note": "His death prompted Jackson to appoint John McLean as his replacement — introducing a more Jacksonian voice into the Marshall Court"}
        ]
    }),

    # 2 — Ahmad ibn Abi Du'ad (Chief Qadi of the Abbasid Caliphate)
    ("ahmad-ibn-abi-duad", {
        "summary": (
            "Ahmad ibn Abi Du'ad (778–854 CE) was the most powerful judicial figure "
            "in the Abbasid Caliphate during the mid-9th century — serving as Chief "
            "Qadi (qadi al-qudat) under caliphs al-Mu'tasim and al-Wathiq, and as "
            "a towering champion of Mutazilite theology, which held that the Quran "
            "was created (not eternal) and that rational philosophy should govern "
            "Islamic theology. As Chief Qadi, he controlled the entire apparatus "
            "of Islamic jurisprudence in the caliphate — appointing and removing "
            "judges across the empire — and wielded a degree of judicial and "
            "theological power that no qadi before or after him matched.\n\n"
            "His most historically consequential role was as the chief administrator "
            "of the Mihna — the Abbasid theological inquisition (from Arabic: 'test' "
            "or 'trial') — initiated by Caliph al-Ma'mun in 833 CE and continued "
            "under al-Mu'tasim and al-Wathiq. The Mihna required Islamic scholars "
            "and judges to publicly declare that the Quran was created — the core "
            "Mutazilite position — or face imprisonment, torture, or removal from "
            "office. Ahmad ibn Abi Du'ad personally conducted many of the Mihna "
            "interrogations. His most famous encounter was with Ahmad ibn Hanbal — "
            "the great traditionalist jurist who refused to recant, endured imprisonment "
            "and flogging, and became the defining hero of Sunni resistance to "
            "Mutazilite rationalism and state theological coercion.\n\n"
            "When Caliph al-Mutawakkil ended the Mihna in 848–849 CE and reversed "
            "Mutazilite official doctrine, Ibn Abi Du'ad was dismissed and disgraced. "
            "He suffered a stroke around 848 that incapacitated him, and his family "
            "was stripped of much of its wealth. His fall was as complete as his "
            "earlier dominance had been total.\n\n"
            "His career represents the historical high-water mark of Mutazilite "
            "rationalist theology's attempt to impose itself through state power — "
            "and its decisive defeat by traditionalist Islamic scholarship."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Chief Qadi (qadi al-qudat) of the Abbasid Caliphate under al-Mu'tasim and al-Wathiq; principal administrator of the Mihna inquisition (833–848 CE); most powerful Mutazilite official in Islamic history; his confrontation with Ahmad ibn Hanbal became the defining moment in Sunni Islam's rejection of state theological coercion.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Abbasid caliphate's engagement with Greek rationalism and Mutazilite theology — championed by al-Ma'mun — created the theological-political program that elevated Ibn Abi Du'ad to the position of its chief judicial enforcer",
            "The Mihna inquisition's need for a powerful administrative figure capable of conducting theological interrogations across the empire — replacing judges who refused to comply — drove his appointment as Chief Qadi",
            "The tension between Mutazilite rationalism (theology based on Greek philosophical methods) and traditionalist hadith-based Islamic scholarship created the theological contest that the Mihna attempted to resolve by state coercion"
        ],
        "effects": [
            "His administration of the Mihna — and especially his famous interrogations of Ahmad ibn Hanbal — made him the chief villain in the Sunni traditionalist narrative of the Mihna crisis, cementing Ibn Hanbal's status as a hero of Sunni Islam",
            "The failure of the Mihna — symbolized by Ibn Hanbal's defiant refusal to recant — and Ibn Abi Du'ad's subsequent disgrace under al-Mutawakkil marked the decisive defeat of Mutazilite rationalism as an official Abbasid theology and its replacement by traditionalist Ash'arite and Hanbali theology",
            "Al-Mutawakkil's reversal of the Mihna and dismissal of Ibn Abi Du'ad in 848–849 represented one of the most complete theological reversals in Abbasid history — the state-sponsored rejection of state-sponsored rationalism",
            "His career established the maximum extent of the chief qadi's power in Islamic history — his role as sole controller of judicial appointments across the entire caliphate was never replicated after his fall"
        ],
        "relationships": [
            {"entity": "Ahmad ibn Hanbal (Hanbali founder)", "relationship": "CHIEF_INTERROGATOR_OF_DURING_MIHNA", "note": "Personally conducted the Mihna interrogations of Ahmad ibn Hanbal — whose refusal to recant became the defining moment in Sunni Islam's resistance to Mutazilite state coercion"},
            {"entity": "Abbasid Mihna inquisition (833–848 CE)", "relationship": "CHIEF_ADMINISTRATOR_OF", "note": "Principal administrator of the Mihna — the Abbasid theological inquisition requiring scholars to declare the Quran was created — under three caliphs"},
            {"entity": "Caliph al-Mu'tasim / Caliph al-Wathiq", "relationship": "CHIEF_QADI_UNDER", "note": "Served as Chief Qadi (qadi al-qudat) — controlling judicial appointments across the entire caliphate — under caliphs al-Mu'tasim and al-Wathiq"},
            {"entity": "Mutazilite theology (Islamic rationalism)", "relationship": "LEADING_STATE_CHAMPION_OF", "note": "The most powerful official proponent of Mutazilite theology — using state judicial power to enforce its doctrine that the Quran was created"},
            {"entity": "Caliph al-Mutawakkil (r. 847–861)", "relationship": "DISMISSED_AND_DISGRACED_BY", "note": "Al-Mutawakkil ended the Mihna in 848–849 and dismissed Ibn Abi Du'ad — stripping him and his family of power and wealth in one of the most complete political reversals in Abbasid history"}
        ]
    }),

    # 3 — Louis-Joseph Papineau
    ("louis-joseph-papineau", {
        "summary": (
            "Louis-Joseph Papineau (1786–1871) was a French-Canadian lawyer, politician, "
            "and revolutionary who led the Patriote movement for political reform in "
            "Lower Canada during the 1820s and 1830s and who commanded the unsuccessful "
            "Lower Canada Rebellion of 1837–1838 — the most significant armed uprising "
            "in Canadian history before Confederation, which brought to a head the "
            "confrontation between the French-Canadian majority in Lower Canada and "
            "the British colonial administration. Papineau was the most charismatic "
            "and influential French-Canadian political figure of the pre-Confederation "
            "era, shaping not only the Rebellion but the entire trajectory of "
            "French-Canadian political thought.\n\n"
            "As Speaker of the Legislative Assembly of Lower Canada (1815–1837) "
            "and leader of the Parti Patriote, Papineau pursued constitutional reform "
            "through the Assembly — demanding responsible government, control of "
            "revenues, and an elected legislative council — while simultaneously "
            "organizing grassroots boycotts of British goods. His Ninety-Two "
            "Resolutions (1834) — a comprehensive statement of French-Canadian "
            "grievances demanding fundamental constitutional change — was rejected "
            "by London, precipitating the final political crisis.\n\n"
            "When the colonial administration rejected reform and attempted to govern "
            "without Assembly approval of budgets, the Patriote movement escalated "
            "to armed resistance. The Battle of Saint-Denis (November 23, 1837) — "
            "an unexpected Patriote victory — was followed by the Battle of "
            "Saint-Charles and the Battle of Saint-Eustache, where British forces "
            "crushed the rebellion. Papineau fled to the United States and then "
            "France, where he remained in exile for nearly a decade.\n\n"
            "He later returned to Canada, served in the Legislature of the Province "
            "of Canada (1848–1854), and remained a powerful voice for French-Canadian "
            "nationalism until his death in 1871."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Leader of the Parti Patriote and the Lower Canada Rebellion of 1837–1838 — the most significant armed uprising in pre-Confederation Canadian history; Speaker of Lower Canada's Legislative Assembly (1815–1837); author of the Ninety-Two Resolutions; a defining figure of French-Canadian nationalism and Quebec political identity.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The constitutional tension between the French-Canadian majority in Lower Canada — controlling the elected Assembly — and the British-appointed executive and legislative councils created the political deadlock that Papineau led the Patriote movement to resolve",
            "London's rejection of the Ninety-Two Resolutions (1834) — the comprehensive statement of Patriote constitutional demands — and the subsequent Russell Resolutions (1837) authorizing the governor to govern without Assembly budget approval precipitated the armed rebellion",
            "The broader democratic and republican currents of the early 19th century — including the American and French revolutions as models — inspired the Patriote movement's vision of representative government and popular sovereignty"
        ],
        "effects": [
            "The Lower Canada Rebellion (1837–1838) — though a military failure — prompted the Durham Report (1839) and the Act of Union (1840) that merged Upper and Lower Canada, reshaping the constitutional structure of British North America",
            "His leadership of the Rebellion made him the defining hero and martyr figure of French-Canadian nationalism — whose legacy continued to shape Quebec political identity through the 20th century and the Quiet Revolution",
            "The Ninety-Two Resolutions he championed established the precedent of comprehensive constitutional demands from a colonial legislature — which influenced the trajectory of responsible government advocacy across British North America",
            "His exile (1837–1845) and the diaspora of Patriote leaders contributed to the dispersal of French-Canadian political talent and the transformation of the Patriote cause into the constitutional nationalism of the Confederation era"
        ],
        "relationships": [
            {"entity": "Lower Canada Rebellion (1837–1838)", "relationship": "LEADER_OF", "note": "Commanded the Patriote uprising — the most significant armed rebellion in pre-Confederation Canadian history — though he fled before the decisive battles"},
            {"entity": "Parti Patriote (Lower Canada)", "relationship": "LEADER_OF", "note": "Led the Parti Patriote — the French-Canadian reform party that dominated the Legislative Assembly of Lower Canada through the 1820s and 1830s"},
            {"entity": "Ninety-Two Resolutions (1834)", "relationship": "PRIMARY_AUTHOR_OF", "note": "Author of the Ninety-Two Resolutions — the comprehensive statement of French-Canadian constitutional grievances whose London rejection precipitated the Rebellion"},
            {"entity": "Durham Report (1839) / Act of Union (1840)", "relationship": "REBELLION_INDIRECTLY_CAUSED", "note": "The rebellion he led prompted Lord Durham's report and the Act of Union that merged Upper and Lower Canada — reshaping British North American constitutionalism"},
            {"entity": "French-Canadian nationalism / Quebec political identity", "relationship": "FOUNDING_FIGURE_OF", "note": "A founding hero of French-Canadian nationalism — whose legacy shaped Quebec political identity from the Rebellion through the Quiet Revolution"}
        ]
    }),

    # 4 — James Duane
    ("james-duane", {
        "summary": (
            "James Duane (1733–1797) was an American Founding Father, attorney, and "
            "jurist from New York who held an extraordinary range of offices during "
            "the Revolutionary and founding eras — serving as a delegate to the "
            "First and Second Continental Congresses, a member of the Congress of "
            "the Confederation, a New York State Senator, the 45th Mayor of New York "
            "City (and its first post-colonial mayor), and ultimately as a United "
            "States District Judge — one of the founding federal judges in the "
            "new American judicial system. His career made him one of the most "
            "broadly experienced figures in New York's founding generation.\n\n"
            "Duane was a conservative Whig — supporting independence but also "
            "concerned about the radical democratic implications of the Revolution. "
            "In the Continental Congress he was associated with the moderate faction "
            "that sought to maintain order and property rights amid the upheaval "
            "of independence. He helped draft several early congressional documents "
            "and contributed to the developing constitutional theory of the new "
            "nation, though he resisted the most radical implications of popular "
            "sovereignty.\n\n"
            "As the first post-colonial Mayor of New York City (1784–1789), he presided "
            "over the city's reconstruction after British occupation during the "
            "Revolutionary War — a period when New York was the largest city in "
            "America and a crucial commercial and financial center. The restoration "
            "of civilian government, the reintegration of Loyalist property questions, "
            "and the economic revival of the port city were the central challenges "
            "of his mayoralty.\n\n"
            "He was appointed one of the founding US District Judges for New York "
            "under the Judiciary Act of 1789 — serving until 1794."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "American Founding Father from New York — delegate to the First and Second Continental Congresses, New York State Senator, first post-colonial Mayor of New York City (1784–1789), and founding US District Judge under the Judiciary Act of 1789.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New York's central importance in American revolutionary politics — as the colony whose legislature was most closely divided between Patriot and Loyalist factions — created the political environment in which Duane's conservative Whig approach found its political niche",
            "The British occupation of New York City during the Revolutionary War and its subsequent liberation created the administrative reconstruction crisis that Duane's mayoralty had to manage",
            "The Judiciary Act of 1789's creation of the federal district court system created the judicial institution to which Duane was appointed as one of its founding judges"
        ],
        "effects": [
            "His mayoralty presided over New York City's reconstruction after British occupation — restoring civilian government to the most important commercial city in post-independence America",
            "His Continental Congress service contributed to the developing constitutional framework of the Articles of Confederation era — including the drafts and debates of early American national government",
            "His appointment as a founding US District Judge contributed to the establishment of the federal judicial system in New York — one of the most commercially important judicial districts in the new nation",
            "His conservative Whig approach to the Revolution — maintaining property rights and order amid democratic upheaval — contributed to the conservative strand of American founding-era constitutionalism"
        ],
        "relationships": [
            {"entity": "First and Second Continental Congresses", "relationship": "DELEGATE_TO", "note": "A delegate to both the First and Second Continental Congresses — contributing to the developing framework of American independence"},
            {"entity": "New York City (post-Revolutionary reconstruction)", "relationship": "FIRST_POST-COLONIAL_MAYOR_OF", "note": "45th Mayor of New York City and its first post-colonial mayor (1784–1789) — presiding over the city's reconstruction after British occupation"},
            {"entity": "US District Court (Southern District of New York)", "relationship": "FOUNDING_JUDGE_OF", "note": "Appointed as one of the founding US District Judges for New York under the Judiciary Act of 1789 — one of the first federal judges in the new American system"},
            {"entity": "Congress of the Confederation", "relationship": "MEMBER_OF", "note": "Served in the Congress of the Confederation — the national legislature under the Articles of Confederation"},
            {"entity": "New York State Senate", "relationship": "MEMBER_OF", "note": "Served in the New York State Senate — contributing to the state-level constitutional architecture of New York in the revolutionary era"}
        ]
    }),

    # 5 — Egbert Benson
    ("egbert-benson", {
        "summary": (
            "Egbert Benson (1746–1833) was an American lawyer, jurist, and Founding "
            "Father from New York who held an extraordinary range of foundational "
            "positions in the new American constitutional order — serving as the "
            "first Attorney General of New York State (1777–1789), as a delegate "
            "to the Continental Congress, as a participant in the Annapolis Convention "
            "(1786) that called the Constitutional Convention, as a member of the "
            "New York ratification convention (1788) where he supported the Constitution's "
            "adoption, and as an early member of the US House of Representatives "
            "(1789–1793). He was an intimate of Alexander Hamilton and a central "
            "figure in New York Federalist legal circles.\n\n"
            "As the first Attorney General of New York, Benson served during the "
            "tumultuous period from the Declaration of Independence through the "
            "Constitution's ratification — a time when New York's legal system "
            "was being entirely reconstructed from colonial to republican foundations. "
            "He helped draft New York's early statutes and played a key role in "
            "adapting English common law to the new republican legal environment.\n\n"
            "In the US House (1789–1793), he was a prominent Federalist — associated "
            "with Hamilton's financial program and the constitutional nationalist "
            "vision of a strong federal government. He later served as a Judge of "
            "the New York Supreme Court (1794–1801) and as Chief Judge of the US "
            "Circuit Court for the Second Circuit (1801–1802, briefly, until abolished "
            "by the Democratic-Republicans in 1802 as part of the Judiciary Act "
            "repeal controversy).\n\n"
            "His long career — from the Revolution through the Early Republic — "
            "made him one of the most experienced legal-political figures in New "
            "York's founding generation."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "First Attorney General of New York State (1777–1789); delegate to the Annapolis Convention (1786); member of the New York Constitutional ratification convention (1788); early US Representative; judge of the NY Supreme Court; intimate of Alexander Hamilton and central Federalist legal figure.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The American Revolution's creation of new state legal systems — requiring the reconstruction of colonial legal institutions on republican foundations — created the role of the first New York Attorney General that Benson filled",
            "The Annapolis Convention's call for the Constitutional Convention and the subsequent ratification struggle created the constitutional moments in which Benson participated as a committed Federalist",
            "His close association with Alexander Hamilton and the New York Federalist legal network placed him at the center of the constitutional nationalist movement that shaped the early republic"
        ],
        "effects": [
            "His tenure as the first New York Attorney General (1777–1789) helped establish the foundations of New York's republican legal system — adapting English common law to the new state constitution and statutory framework",
            "His participation in the Annapolis Convention contributed to the momentum that produced the Constitutional Convention — the Annapolis gathering was the direct predecessor of the Philadelphia convention",
            "His role in the New York ratification convention contributed to New York's narrow adoption of the Constitution — a critical victory for the Federalists, as New York was a major state that had significant Anti-Federalist opposition",
            "His early congressional service contributed to the Federalist legislative program in the First Congress — including support for Hamilton's financial plan and the establishment of the federal judiciary"
        ],
        "relationships": [
            {"entity": "New York State Attorney General (office)", "relationship": "FIRST_HOLDER_OF", "note": "First Attorney General of New York State (1777–1789) — established the office during the Revolutionary and early republican periods"},
            {"entity": "Annapolis Convention (1786)", "relationship": "DELEGATE_TO", "note": "Participated in the Annapolis Convention — the gathering that called the Constitutional Convention and set the stage for the Philadelphia convention"},
            {"entity": "Alexander Hamilton", "relationship": "INTIMATE_COLLEAGUE_OF", "note": "A close associate of Hamilton and a central figure in New York Federalist legal and political circles"},
            {"entity": "New York Constitutional Ratification Convention (1788)", "relationship": "FEDERALIST_DELEGATE_TO", "note": "Supported the Constitution's ratification in the New York convention — a critical Federalist victory in the most Anti-Federalist of the large states"},
            {"entity": "US House of Representatives (1st–3rd Congress)", "relationship": "FEDERALIST_MEMBER_OF", "note": "Served in the US House (1789–1793) as a Federalist — supporting Hamilton's financial program and the constitutional nationalist agenda of the early republic"}
        ]
    }),

    # 6 — Zinovios Valvis
    ("zinovios-valvis", {
        "summary": (
            "Zinovios Valvis (1800–1886) was a Greek lawyer and statesman who twice "
            "served as Prime Minister of Greece during the turbulent mid-19th century "
            "period of the kingdom's political development. Born in Missolonghi in "
            "1800 — the city that would become famous as the site of Lord Byron's "
            "death during the Greek War of Independence (1824) — he received a "
            "theological education at the Theological School of Halki before "
            "redirecting to law and completing his legal studies in Pisa, Italy. "
            "His academic trajectory from theology to law reflects the broader "
            "pattern of Greek educated elites who navigated between Ottoman-era "
            "Orthodox educational traditions and the European secular professional "
            "education of the 19th century.\n\n"
            "His political career unfolded within the constitutional monarchy of "
            "Greece — established after independence from the Ottoman Empire (1830) "
            "under the Bavarian King Otto and later restructured by the Constitution "
            "of 1843. Greek politics in the mid-19th century was characterized by "
            "intense factional struggle among the English, French, and Russian parties — "
            "each representing the competing great-power patrons of the new kingdom — "
            "and by the constitutional tension between royal prerogative and "
            "parliamentary government.\n\n"
            "Valvis served in multiple senior governmental positions, including as "
            "Minister of Justice and Foreign Minister, before his two terms as "
            "Prime Minister. His later life saw him fall on financial difficulty — "
            "a common fate for Greek politicians of his generation who lacked "
            "independent means — and he died in 1886 at the age of 86 after "
            "a career that had spanned the entire first half-century of Greek "
            "statehood.\n\n"
            "His career exemplifies the founding generation of Greek statesmen "
            "who built the institutions of the modern Greek state from the ruins "
            "of Ottoman governance."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Twice Prime Minister of Greece in the mid-19th century; also served as Minister of Justice and Foreign Minister; born in Missolonghi (the city of Byron's death); educated in theology at Halki and law in Pisa; a founding-generation Greek statesman of the constitutional monarchy era.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Greek independence from the Ottoman Empire (1830) and the subsequent establishment of a constitutional monarchy created the political institutions and factional struggles within which Valvis's ministerial and prime ministerial career developed",
            "The Constitution of 1843 — forced on King Otto by the revolution of that year — established the constitutional framework of parliamentary government in Greece that structured Valvis's political career",
            "His education in Italy (law at Pisa) and his prior theological training at Halki positioned him as a Greek statesman who combined Orthodox religious background with Western European professional credentials — the profile of the Greek founding political elite"
        ],
        "effects": [
            "His two terms as Prime Minister contributed to the governance and institutional development of the Greek constitutional monarchy during its formative decades — a period when the basic institutions of the modern Greek state were being established",
            "His ministerial roles — as Minister of Justice and Foreign Minister — contributed to the development of Greek judicial and diplomatic institutions in the first half-century of statehood",
            "His career exemplified the social profile of the Greek founding political elite — educated abroad in Western European law, returning to build institutions from Ottoman-era foundations — whose collective efforts established the modern Greek state",
            "His birth in Missolonghi — the city of the Greek War of Independence's most famous foreign martyr, Lord Byron — connected him personally to the revolutionary tradition that founded the Greek state"
        ],
        "relationships": [
            {"entity": "Kingdom of Greece (constitutional monarchy)", "relationship": "TWICE_PRIME_MINISTER_OF", "note": "Served as Prime Minister of Greece twice during the mid-19th century constitutional monarchy period"},
            {"entity": "Greek Ministry of Justice", "relationship": "MINISTER_OF", "note": "Served as Minister of Justice — contributing to the development of the Greek legal and judicial system"},
            {"entity": "Greek Ministry of Foreign Affairs", "relationship": "MINISTER_OF", "note": "Served as Foreign Minister — contributing to Greece's developing diplomatic relationships during the constitutional monarchy era"},
            {"entity": "Missolonghi (Greece)", "relationship": "BORN_IN", "note": "Born in Missolonghi in 1800 — the city that became famous as the site of Lord Byron's death (1824) during the Greek War of Independence"},
            {"entity": "Greek War of Independence (1821–1830)", "relationship": "CONTEMPORARY_AND_INHERITOR_OF", "note": "His political career was built on the independence that the War of Independence secured — he served as a statesman in the state the revolution founded"}
        ]
    }),

    # 7 — Willard Hall
    ("willard-hall", {
        "summary": (
            "Willard Hall (1780–1875) was a Delaware attorney, politician, and judge "
            "whose career spanned an extraordinary 95 years and encompassed the full "
            "arc of Delaware political and legal history from the early republic to "
            "the post-Civil War era. Born in Massachusetts and a graduate of Harvard "
            "(1799), Hall relocated to Delaware and established himself as one of "
            "Wilmington's leading lawyers before entering politics as a Democratic-Republican "
            "and later a Democrat — serving in the Delaware Senate, as a US Representative "
            "from Delaware, and as a United States District Judge for the District of "
            "Delaware (1823–1871) — a remarkable 48-year judicial tenure that made "
            "him one of the longest-serving federal judges in American history.\n\n"
            "Hall's 48-year tenure on the Delaware federal bench spanned from the "
            "Era of Good Feelings through the Civil War and Reconstruction — and "
            "his judicial decisions over that period reflected the profound "
            "constitutional transformations of 19th-century American law. As "
            "Delaware's only federal district judge for nearly half a century, "
            "he was responsible for the entire federal judicial administration "
            "of a state with a complex commercial, maritime, and (during the "
            "Civil War) border-state political identity.\n\n"
            "Outside the law, Hall served as the first President of the Delaware "
            "Historical Society — reflecting his broader civic and intellectual "
            "engagement with Delaware's history and culture. His longevity was "
            "remarkable: he was active on the federal bench into his 80s, and "
            "he lived to 95, making him one of the longest-lived federal judges "
            "of the 19th century.\n\n"
            "His career exemplifies the founding generation of American federal "
            "judges whose tenures bridged the entire span of 19th-century American "
            "constitutional development."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "US District Judge for Delaware for 48 years (1823–1871) — one of the longest judicial tenures in American history; first President of the Delaware Historical Society; Harvard graduate who became Delaware's leading federal judge through the Civil War era.",
            "significanceCategory": "regional"
        },
        "causes": [
            "His Harvard legal education and subsequent relocation to Delaware — a small state that offered significant professional opportunity for an able lawyer — established the foundation of his Delaware legal career",
            "The early American federal judicial system's small size — Delaware had only one federal district judge — created the conditions for his extraordinary concentration of federal judicial authority over the state",
            "His Democratic-Republican political connections provided the pathway to his 1823 appointment as US District Judge"
        ],
        "effects": [
            "His 48-year federal judicial tenure provided legal continuity for Delaware's federal courts across the most transformative period of American constitutional history — from the Marshall era through Reconstruction",
            "As the sole federal district judge in Delaware throughout his tenure, his decisions shaped the entire federal legal landscape of the state — in admiralty, commercial law, and the complex border-state legal questions of the Civil War era",
            "His founding of the Delaware Historical Society and service as its first President contributed to the preservation of Delaware's historical records and the development of a culture of historical scholarship in the state",
            "His longevity on the bench — active into his 80s — demonstrated that 19th-century federal judicial appointments were effectively life appointments with substantial institutional consequences for the states they served"
        ],
        "relationships": [
            {"entity": "US District Court (District of Delaware)", "relationship": "JUDGE_FOR_48_YEARS", "note": "Served as US District Judge for the District of Delaware for 48 years (1823–1871) — one of the longest federal judicial tenures in American history"},
            {"entity": "Delaware Historical Society", "relationship": "FIRST_PRESIDENT_OF", "note": "Served as the first President of the Delaware Historical Society — contributing to Delaware's historical scholarship and preservation of state records"},
            {"entity": "US House of Representatives (Delaware)", "relationship": "FORMER_MEMBER_OF", "note": "Served as a US Representative from Delaware before his appointment to the federal bench"},
            {"entity": "Delaware Senate", "relationship": "FORMER_MEMBER_OF", "note": "Served in the Delaware State Senate — building his political career before his federal judicial appointment"},
            {"entity": "Harvard College (Class of 1799)", "relationship": "ALUMNUS_OF", "note": "A Harvard graduate (1799) who relocated from Massachusetts to Delaware — establishing himself as Wilmington's leading lawyer before entering politics and then the federal bench"}
        ]
    }),

    # 8 — Benjamin Parke
    ("benjamin-parke", {
        "summary": (
            "Benjamin Parke (1777–1835) was an American lawyer, military officer, "
            "politician, and federal judge who played a foundational role in the "
            "territorial and early statehood legal and political institutions of "
            "Indiana — serving successively as the Indiana Territory's first Attorney "
            "General (1804–1808), as Indiana Territory's first delegate to the "
            "US Congress (1805–1808), as a treaty negotiator with Native American "
            "nations, and finally as a United States District Judge for the District "
            "of Indiana (1817–1835) — making him one of the founding judicial figures "
            "of the new state.\n\n"
            "Parke's territorial career unfolded under Governor William Henry Harrison — "
            "the future US president — who appointed Parke as territorial attorney "
            "general and relied on him for the legal and diplomatic work of territorial "
            "administration. Indiana Territory in the early 1800s was a contested "
            "frontier zone where American expansion, Native American sovereignty, "
            "and British influence (from Canada) intersected — and Parke's role as "
            "treaty negotiator placed him at the legal and diplomatic interface of "
            "this frontier.\n\n"
            "As Indiana's first territorial congressional delegate, he represented "
            "the Territory in Washington during the critical years when Indiana's "
            "territorial status, population growth, and eventual path to statehood "
            "were being negotiated — though territorial delegates could not vote "
            "in the full House. His appointment as US District Judge at Indiana's "
            "statehood (1816) made him the founding judge of the new state's "
            "federal court.\n\n"
            "Parke County, Indiana — named in his honor — preserves his memory "
            "as one of the state's founding legal and political figures."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "First Attorney General of Indiana Territory (1804–1808); first Indiana Territory congressional delegate (1805–1808); treaty negotiator with Native American nations; founding US District Judge for Indiana (1817–1835); Parke County, Indiana named in his honor.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Indiana Territory's early administrative organization — under Governor William Henry Harrison — required a territorial attorney general to handle the legal affairs of frontier governance, including treaty negotiation with Native American nations",
            "The US territorial system's provision for non-voting congressional delegates gave Parke his Washington representation role — allowing him to advocate for Indiana's territorial interests in Congress",
            "Indiana's attainment of statehood in 1816 required the appointment of founding federal judges for the new state's district court — making Parke the natural choice given his decade of territorial legal service"
        ],
        "effects": [
            "His role as Indiana Territory's first Attorney General established the foundational legal institutions of territorial governance — providing the legal framework within which the territory managed its affairs, processed land claims, and dealt with frontier legal questions",
            "His treaty negotiations with Native American nations contributed to the legal transformation of the Indiana frontier — the formal processes through which Native American land was ceded to American settlement",
            "His 18-year tenure as founding US District Judge for Indiana (1817–1835) established the federal judicial precedents and procedures for one of the fastest-growing states of the early 19th century",
            "Parke County, Indiana — named in his honor — reflects the territorial generation's practice of commemorating founding figures through county naming, preserving his significance in the state's institutional memory"
        ],
        "relationships": [
            {"entity": "William Henry Harrison (Indiana Territorial Governor)", "relationship": "SERVED_UNDER_AS_TERRITORIAL_AG", "note": "Indiana Territory's first Attorney General under Governor William Henry Harrison — who would later become the 9th US President"},
            {"entity": "US Congress (Indiana Territory delegate)", "relationship": "FIRST_TERRITORIAL_DELEGATE_FROM_INDIANA", "note": "Indiana Territory's first (non-voting) delegate to the US Congress (1805–1808) — representing territorial interests in Washington"},
            {"entity": "US District Court (District of Indiana)", "relationship": "FOUNDING_JUDGE_OF", "note": "Appointed founding US District Judge for Indiana at statehood (1817) — served until his death in 1835"},
            {"entity": "Native American treaty negotiations (Indiana)", "relationship": "NEGOTIATOR_IN", "note": "Served as a US treaty negotiator with Native American nations in Indiana Territory — the legal and diplomatic process of frontier land cession"},
            {"entity": "Parke County (Indiana)", "relationship": "NAMESAKE_OF", "note": "Parke County, Indiana was named in his honor — recognizing his foundational role in the state's territorial and early statehood institutions"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 28)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
