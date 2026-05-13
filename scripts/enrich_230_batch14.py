#!/usr/bin/env python3
"""
Batch 14 — 8 entities: Sisamnes, Otanes, Lawrence Booth, John H. Knox,
Tessa Khan, Muhammad ibn Wasi' al-Azdi, Tariq ibn Amr, Francesco Accolti
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
          f"e={len(det.get('effects',[]))} r={len(det.get('relationships',[]))}")


ENTITIES = [

    # 1 — Sisamnes (fl. c. 525 BCE)
    ("sisamnes", {
        "summary": (
            "Sisamnes (fl. c. 525 BCE) was an Achaemenid Persian royal judge whose execution by the Persian king "
            "Cambyses II became one of antiquity's most powerful moral exempla of judicial corruption and its consequences. "
            "As recorded by Herodotus in the Histories (5.25), Sisamnes served as one of the royal judges of Persia — "
            "the senior jurists appointed directly by the Great King to administer the law of the Achaemenid empire. "
            "He accepted a bribe to render an unjust verdict, and when Cambyses discovered the corruption, the king's "
            "response was both immediate and spectacularly symbolic.\n\n"
            "Cambyses had Sisamnes arrested, sentenced to death, and — most significantly — commanded that his skin be "
            "stripped from his body after execution, cut into strips, and used to re-upholster the judgment seat from "
            "which Sisamnes had dispensed corrupt justice. Cambyses then appointed Sisamnes's own son Otanes as the "
            "new judge, requiring him to sit upon the throne upholstered with his father's skin as a permanent "
            "reminder of the fate awaiting a corrupt judge. The punishment transformed the seat of justice itself "
            "into a monument to judicial accountability.\n\n"
            "The story became one of the most celebrated moral exempla of antiquity, transmitted through Herodotus "
            "into the entire Western literary tradition. It was depicted in one of the most famous paintings of "
            "the Northern Renaissance: Gerard David's diptych 'The Judgment of Cambyses' (c. 1498), commissioned "
            "by the city of Bruges for its town hall as a warning to magistrates. In medieval and Renaissance "
            "Europe, the story of Sisamnes was repeatedly cited in legal and ethical treatises as the ultimate "
            "warning against bribery and corruption in judges.\n\n"
            "'The seat from which he had sold justice became, by the king's command, upholstered with his own "
            "skin.' No story in ancient history delivered a starker lesson about the cost of judicial corruption."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "The archetypal ancient narrative of judicial corruption and punishment, preserved by Herodotus and immortalized in Gerard David's 1498 Bruges diptych 'The Judgment of Cambyses' — a warning to judges cited through the entire Western legal tradition.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Achaemenid empire's system of royal judges dependent on the Great King's appointment made them simultaneously powerful and vulnerable to accusations of corruption",
            "The absence of independent judicial oversight in the Persian imperial system meant that judicial corruption, once discovered, had to be punished with maximal royal force",
            "The culture of exemplary royal punishment in the Achaemenid empire — designed to demonstrate royal power and deter similar offenses — shaped Cambyses's spectacular response"
        ],
        "effects": [
            "His execution and flaying was recorded by Herodotus as a moral exemplum that transmitted into the entire Western literary and legal tradition",
            "His son Otanes was appointed in his place, sitting on a throne upholstered with his father's skin — establishing one of history's most vivid reminders of judicial accountability",
            "Gerard David's 'Judgment of Cambyses' diptych (c. 1498) for the Bruges town hall used Sisamnes's story as a visual warning to magistrates, becoming one of the most famous Northern Renaissance judicial artworks",
            "The story was cited in Renaissance and early modern legal treatises on judicial ethics as the quintessential example of the consequences of bribery"
        ],
        "relationships": [
            {"entity": "Cambyses II of Persia", "relationship": "PUNISHED_BY", "note": "Cambyses had Sisamnes flayed alive for accepting a bribe, using his skin to upholster the judgment seat"},
            {"entity": "Otanes (son of Sisamnes)", "relationship": "FATHER_OF", "note": "His son Otanes was appointed as his replacement judge and made to sit on the throne covered with his father's skin"},
            {"entity": "Herodotus", "relationship": "DOCUMENTED_BY", "note": "Herodotus recorded the story in the Histories (5.25), through which it entered Western literary tradition"},
            {"entity": "Gerard David", "relationship": "DEPICTED_BY", "note": "Gerard David's diptych 'The Judgment of Cambyses' (c. 1498) for Bruges town hall depicted Sisamnes's flaying as a warning to magistrates"},
            {"entity": "Achaemenid Persian legal system", "relationship": "SERVED_WITHIN", "note": "Served as a royal judge within the Achaemenid imperial legal system appointed directly by the Great King"}
        ]
    }),

    # 2 — Otanes, son of Sisamnes (fl. c. 525–490 BCE)
    ("otanes", {
        "summary": (
            "Otanes, son of Sisamnes (fl. c. 525–490 BCE), was an Achaemenid Persian judge and later Satrap of Ionia "
            "who occupied a uniquely symbolic position in the history of judicial ethics: appointed by King Cambyses II "
            "to replace his own father Sisamnes — whom Cambyses had executed for judicial corruption and had flayed, "
            "using his skin to upholster the very judgment seat Otanes would occupy. Whether as a punishment, a test, "
            "or both, Otanes served as judge while sitting on a throne covered with his father's skin, a daily reminder "
            "of the fate awaiting a corrupt magistrate.\n\n"
            "Herodotus records Otanes's appointment in Histories 5.25 as the immediate consequence of his father's "
            "execution, noting that Cambyses explicitly told Otanes to remember how he came to sit in judgment. "
            "Despite this origin, Otanes did not disappear from Persian politics: he subsequently rose to become "
            "one of the prominent military and administrative figures of the Achaemenid empire under Darius I. "
            "He served as Satrap of Ionia (the western coast of Anatolia) around 513–490 BCE, commanding Persian "
            "forces in the Aegean and participating in the suppression of Greek islands in the period before "
            "the Ionian Revolt.\n\n"
            "Herodotus also describes Otanes's campaigns in the Aegean — the conquest of Byzantium, Chalcedon, "
            "and other island and coastal cities — as exceptionally harsh, establishing a reputation for brutality "
            "that contributed to the growing Greek resentment of Persian rule that eventually erupted in the Ionian "
            "Revolt (499–494 BCE). He was recalled and replaced as satrap before the revolt began.\n\n"
            "Otanes embodies the paradox of a man who rose to power through the spectacle of his father's punishment "
            "and then exercised that power in ways that contributed to the revolt against it. His life connects "
            "the moral drama of judicial corruption to the geopolitical drama of the Persian-Greek conflict."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Appointed judge by Cambyses II to replace his executed father Sisamnes — made to sit on a throne upholstered with his father's skin — then rose to become Satrap of Ionia whose harsh governance contributed to the conditions for the Ionian Revolt.",
            "significanceCategory": "regional"
        },
        "causes": [
            "His father Sisamnes's execution by Cambyses II for corruption directly created his appointment as royal judge under the most symbolically charged circumstances in Persian legal history",
            "Darius I's reorganization of the Achaemenid satrapal system promoted Otanes to the strategically vital position of Satrap of Ionia",
            "The Achaemenid empire's westward expansion into the Aegean required a satrap capable of both military command and coastal administration"
        ],
        "effects": [
            "His occupancy of the judgment seat upholstered with his father's skin became one of the most powerful visual symbols of judicial accountability in ancient legal culture",
            "As Satrap of Ionia, his harsh governance of Aegean Greek cities contributed to the conditions that produced the Ionian Revolt (499–494 BCE)",
            "The Herodotean narrative connecting Sisamnes's corruption to Otanes's appointment and Ionian service created a morally complex story that influenced Western accounts of justice and its consequences",
            "His replacement before the Ionian Revolt suggests Persian awareness that his governance was contributing to instability in the region"
        ],
        "relationships": [
            {"entity": "Sisamnes", "relationship": "SON_OF", "note": "Appointed judge by Cambyses II to replace his father Sisamnes after Sisamnes was executed for corruption"},
            {"entity": "Cambyses II of Persia", "relationship": "APPOINTED_BY", "note": "Cambyses appointed Otanes judge, making him sit on a throne upholstered with his father's skin"},
            {"entity": "Darius I of Persia", "relationship": "SERVED_UNDER", "note": "Served as Satrap of Ionia under Darius I, commanding Persian forces in the Aegean"},
            {"entity": "Ionian Revolt", "relationship": "CONTRIBUTED_TO_CONDITIONS_FOR", "note": "His harsh governance as Satrap of Ionia was one of the conditions that contributed to the Ionian Revolt (499–494 BCE)"},
            {"entity": "Herodotus", "relationship": "DOCUMENTED_BY", "note": "Herodotus recorded both the story of Sisamnes and Otanes's subsequent career in the Histories"}
        ]
    }),

    # 3 — Lawrence Booth (c. 1420–1480)
    ("lawrence-booth", {
        "summary": (
            "Lawrence Booth (c. 1420–1480) was an English bishop, statesman, and Archbishop of York whose career "
            "spanned the most turbulent decades of the Wars of the Roses, combining royal service as Lord Chancellor "
            "under Henry VI with episcopal administration of two of England's most important sees. Born into a "
            "Lancashire family with clerical connections, he was educated at Cambridge (Pembroke Hall) and rose "
            "through royal service to become one of the leading ecclesiastical administrators of 15th-century England.\n\n"
            "Booth served as Keeper of the Privy Seal from 1451 before being appointed Lord Chancellor of England "
            "(1456–1460) under Henry VI — the highest legal office in the realm. During these years of intense "
            "factional conflict between the Lancastrian crown and the Yorkist magnates, he was appointed Bishop "
            "of Durham in 1457, a see of exceptional importance because the Bishop of Durham held unique palatinate "
            "powers: in County Durham he exercised virtually royal authority, with his own courts, mint, and "
            "military obligations for the northern border. This combination of the Lord Chancellorship with the "
            "Durham palatinate made Booth one of the most powerful men in England during the last years of "
            "Henry VI's effective rule.\n\n"
            "After Edward IV's victory (1461), Booth retained his position as Bishop of Durham, navigating the "
            "political transition with sufficient skill to serve under Yorkist rule despite his Lancastrian "
            "background. He was eventually translated to the Archbishopric of York (1476), the second most "
            "senior ecclesiastical office in England, which he held until his death in 1480. His two decades "
            "as Bishop of Durham saw significant administrative development of the palatinate, and his "
            "translation to York was recognition of his distinguished episcopal career.\n\n"
            "His career illustrated both the immense power available to English prelate-politicians in the "
            "15th century and the skill required to survive the dynastic reversals of the Wars of the Roses."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Lord Chancellor of England under Henry VI and Bishop of Durham — a combination of the highest legal office with the most powerful palatinate in England — Booth was a central figure in the Lancastrian government during the Wars of the Roses.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Henry VI's reliance on ecclesiastical administrators as Lord Chancellors created the path for Booth's appointment to both the chancellorship and the key northern see of Durham",
            "The Wars of the Roses' factional conflict between Lancastrian and Yorkist magnates made the loyalty of powerful prince-bishops like Durham critical to royal governance",
            "Cambridge education and royal service through the Privy Seal gave Booth the administrative credentials for rapid advancement"
        ],
        "effects": [
            "Combined the Lord Chancellorship (1456–1460) with the Bishopric of Durham's palatinate powers, creating one of the most concentrated accumulations of legal and administrative authority in 15th-century England",
            "Governed the Durham palatinate for nearly two decades (1457–1476), developing its administrative institutions and northern border defense",
            "His survival of the Lancastrian-to-Yorkist transition and eventual elevation to Archbishop of York demonstrated the relative stability of senior English episcopal positions even through dynastic revolution",
            "Participated in the governance of England during the critical final years of effective Lancastrian rule before the Yorkist consolidation"
        ],
        "relationships": [
            {"entity": "Henry VI of England", "relationship": "SERVED", "note": "Served Henry VI as Keeper of the Privy Seal and Lord Chancellor (1456–1460)"},
            {"entity": "Bishopric of Durham", "relationship": "LED", "note": "Bishop of Durham (1457–1476), exercising unique palatinate powers in northern England"},
            {"entity": "Archbishopric of York", "relationship": "LED", "note": "Archbishop of York (1476–1480), the second most senior ecclesiastical office in England"},
            {"entity": "Edward IV of England", "relationship": "SURVIVED_TRANSITION_UNDER", "note": "Retained episcopal office after Edward IV's Yorkist victory (1461) despite his Lancastrian background"},
            {"entity": "Wars of the Roses", "relationship": "NAVIGATED", "note": "His career spanned the central decades of the Wars of the Roses, serving both Lancastrian and Yorkist regimes"}
        ]
    }),

    # 4 — John H. Knox (contemporary)
    ("john-h-knox", {
        "summary": (
            "John H. Knox (b. c. 1961) is a Professor of International Law at Wake Forest University School of Law "
            "and served as the inaugural United Nations Special Rapporteur on Human Rights and the Environment "
            "(2012–2018) — the first person appointed by the UN Human Rights Council to investigate and define the "
            "relationship between environmental protection and international human rights law. His six-year mandate "
            "produced a body of scholarly and policy work that helped transform the conceptual and legal foundations "
            "of environmental governance worldwide.\n\n"
            "During his tenure as Special Rapporteur, Knox produced a series of landmark reports mapping the "
            "obligations that human rights law places on states with respect to environmental protection — "
            "including the rights to life, health, food, water, and a healthy environment. He catalogued state "
            "environmental obligations as including three categories: procedural obligations (to assess impacts, "
            "share information, enable participation), substantive obligations (to protect against harmful environmental "
            "conditions), and framework obligations (to establish legal frameworks protecting the environment). "
            "These reports were endorsed by the UN Human Rights Council and influenced both national laws and "
            "international negotiations.\n\n"
            "His work contributed directly to one of the landmark developments in 21st-century international law: "
            "the United Nations General Assembly's recognition in July 2022 of the right to a clean, healthy, and "
            "sustainable environment as a universal human right — a resolution that built on the conceptual foundation "
            "Knox had laid during his UN mandate. Before his UN appointment, Knox had written extensively on the "
            "relationship between trade agreements and environmental law, particularly focusing on the intersection "
            "of the WTO legal regime with environmental regulation.\n\n"
            "'He gave human rights law a grammar for talking about the planet.' Knox's UN reports created the "
            "intellectual architecture for a generation of climate litigation and environmental rights advocacy."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "As the inaugural UN Special Rapporteur on Human Rights and the Environment (2012–2018), Knox created the conceptual framework that led to the 2022 UN General Assembly recognition of the right to a clean, healthy, and sustainable environment as a universal human right.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The growing recognition within the UN human rights system that environmental degradation threatens the realization of fundamental human rights created the mandate for the Special Rapporteur position Knox was appointed to fill",
            "Decades of scholarly work and advocacy connecting environmental protection to human rights law provided the intellectual foundation that Knox systematized in his UN reports",
            "The accelerating climate crisis and biodiversity loss in the 2010s created political urgency for establishing human rights obligations of states with respect to environmental protection"
        ],
        "effects": [
            "His mandate reports created the framework of state environmental obligations under human rights law — procedural, substantive, and framework duties — that has been adopted by human rights bodies worldwide",
            "His work contributed directly to the 2022 UN General Assembly resolution recognizing the right to a clean, healthy, and sustainable environment as a universal human right",
            "His scholarly framework has been cited in climate litigation cases worldwide, providing the legal foundations for arguments that governments have human rights obligations to address climate change",
            "His reporting established the institutional precedent of the Special Rapporteur role that was renewed and continued by his successor David Boyd"
        ],
        "relationships": [
            {"entity": "United Nations Human Rights Council", "relationship": "APPOINTED_BY", "note": "Appointed as inaugural UN Special Rapporteur on Human Rights and the Environment by the UN Human Rights Council (2012)"},
            {"entity": "Wake Forest University", "relationship": "AFFILIATED_WITH", "note": "Professor of International Law at Wake Forest University School of Law"},
            {"entity": "UN General Assembly Resolution (2022)", "relationship": "INFLUENCED", "note": "His mandate contributed to the 2022 UNGA resolution recognizing the right to a clean, healthy environment"},
            {"entity": "David Boyd", "relationship": "PRECEDED", "note": "David Boyd succeeded Knox as UN Special Rapporteur on Human Rights and the Environment in 2018"},
            {"entity": "Climate litigation movement", "relationship": "INFLUENCED", "note": "His framework reports provided legal foundations cited in climate litigation cases worldwide"}
        ]
    }),

    # 5 — Tessa Khan (contemporary)
    ("tessa-khan", {
        "summary": (
            "Tessa Khan (b. c. 1980s) is a British barrister and environmental human rights lawyer who co-founded "
            "and leads the Climate Litigation Network (CLN), one of the most influential organizations in the "
            "rapidly growing field of strategic climate litigation. Working at the intersection of international "
            "human rights law and climate science, she has become one of the leading figures in the movement to "
            "use courts as tools for enforcing climate action obligations — a field that has expanded dramatically "
            "since the Dutch Supreme Court's landmark Urgenda ruling (2019).\n\n"
            "The Climate Litigation Network, which Khan co-founded with other senior climate lawyers, provides "
            "legal support, expertise, and coordination to climate cases being litigated in national and "
            "international courts worldwide. The CLN operates on the principle that climate change constitutes a "
            "violation of human rights and that courts can and should hold governments accountable for inadequate "
            "climate policies. This approach builds on the framework of state environmental obligations developed "
            "in international human rights law and applies it through domestic and regional courts.\n\n"
            "Khan has been involved in or has supported numerous high-profile climate cases, including litigation "
            "against fossil fuel companies and governments across multiple jurisdictions. She has argued that "
            "states have binding legal obligations to protect their citizens from climate harm and that these "
            "obligations are enforceable in courts of law. Her work has contributed to a growing body of case "
            "law establishing that climate inaction is legally actionable — a shift with profound implications "
            "for climate governance.\n\n"
            "'Climate litigation is not a last resort; it is the accountability mechanism that democracy "
            "requires when legislatures fail.' Khan's work has helped transform courts from observers to "
            "participants in the global climate governance system."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Co-founder of the Climate Litigation Network and a leading advocate for strategic climate litigation as an accountability mechanism; her work has contributed to a growing body of case law holding governments legally responsible for climate inaction.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The failure of legislative and diplomatic processes to deliver adequate climate action created demand for alternative accountability mechanisms, particularly judicial enforcement",
            "The Dutch Supreme Court's Urgenda ruling (2019) demonstrated the viability of using human rights law to compel government climate action and inspired a global wave of similar litigation",
            "The development of international human rights frameworks on the environment provided the legal foundation for arguments that climate inaction violates human rights"
        ],
        "effects": [
            "The Climate Litigation Network she co-founded has supported and coordinated climate cases across multiple jurisdictions, contributing to the global expansion of climate litigation",
            "Her work has helped build the legal theories and evidentiary standards that make climate litigation viable in national and regional courts",
            "She has contributed to establishing climate litigation as a recognized field of international law practice, training a new generation of climate lawyers",
            "Her advocacy has contributed to the growing body of judicial decisions holding governments legally accountable for climate policies, with implications for climate governance worldwide"
        ],
        "relationships": [
            {"entity": "Climate Litigation Network", "relationship": "CO-FOUNDED", "note": "Co-founded and leads the Climate Litigation Network, which supports strategic climate litigation worldwide"},
            {"entity": "Urgenda v. Netherlands", "relationship": "INSPIRED_BY", "note": "The landmark Urgenda ruling (2019) demonstrated the viability of human rights climate litigation that Khan's work builds on"},
            {"entity": "Human rights and environment framework", "relationship": "APPLIES", "note": "Her litigation work applies the international human rights framework for environmental protection to climate cases"},
            {"entity": "Climate litigation movement", "relationship": "LEADS", "note": "One of the leading practitioners and advocates for strategic climate litigation as a global accountability mechanism"},
            {"entity": "UK Bar", "relationship": "MEMBER_OF", "note": "A British barrister bringing combined expertise in international human rights law and climate science to litigation"}
        ]
    }),

    # 6 — Muhammad ibn Wasi' al-Azdi (660–740 CE)
    ("muhammad-lbn-wasi-al-azdi", {
        "summary": (
            "Muhammad ibn Wasi' al-Azdi (c. 660–740 CE) was a prominent tabi'i — a member of the generation who "
            "followed the Companions of the Prophet Muhammad — renowned across the early Islamic world as a hadith "
            "scholar, judge (qadi), ascetic (zahid), and soldier whose combined spiritual authority and military "
            "service under the Umayyad caliphate made him one of the most admired figures of the early Islamic "
            "piety movement (zuhd). Born in Basra, a major center of early Islamic scholarship, he studied "
            "hadith from companions and senior tabi'in including Anas ibn Malik.\n\n"
            "Ibn Wasi' served as a soldier in the Umayyad campaigns in Central Asia under the general Qutayba "
            "ibn Muslim (died 715 CE), participating in the Muslim conquests of Transoxiana (modern Uzbekistan "
            "and Tajikistan). This combination of military service in the expansion of the Islamic world with "
            "simultaneous scholarly and spiritual distinction was characteristic of the early tabi'i generation, "
            "in which religious authority, legal scholarship, and jihad were understood as complementary aspects "
            "of a righteous life. He also served as a qadi in Basra under Umayyad administration.\n\n"
            "His most celebrated saying — 'I never saw anything without seeing Allah therein' — became one of "
            "the most widely quoted statements in later Sufi mystical literature, interpreted as expressing "
            "a vision of divine immanence in all created things. Later Sufis, especially in the tradition of "
            "contemplative mysticism (tafakkur), cited his saying as an anticipation of the Sufi doctrine of "
            "divine presence in the world. His combination of legal-hadith learning with intense personal piety "
            "made him a model for the later tradition of the scholar-saint in Sunni Islam.\n\n"
            "'He looked at every created thing and saw God's face.' Ibn Wasi' al-Azdi's mystical saying and "
            "ascetic example were transmitted through Sufi chains of transmission for over a millennium."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "A leading tabi'i hadith scholar, judge, and ascetic whose celebrated saying 'I never saw anything without seeing Allah therein' became foundational in Sufi mystical literature; his combination of scholarship, piety, and military service exemplified the early Islamic ideal.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Basra's position as a major center of early Islamic hadith scholarship and ascetic piety provided the intellectual environment for ibn Wasi''s formation as a scholar and mystic",
            "The Umayyad caliphate's military campaigns in Central Asia under Qutayba ibn Muslim brought ibn Wasi' into active military service alongside his scholarly career",
            "The early Islamic zuhd (asceticism) movement — which valued renunciation of worldly pleasure and intense personal piety — shaped his spiritual orientation and public reputation"
        ],
        "effects": [
            "His saying 'I never saw anything without seeing Allah therein' became one of the most cited statements in Sufi mystical literature, interpreted as expressing divine immanence",
            "His model of the scholar-soldier-ascetic influenced the development of the Sunni scholar-saint tradition, combining legal authority with spiritual distinction",
            "His hadith transmissions were incorporated into the major collections (including through chains citing Anas ibn Malik) and preserved as part of the early Islamic hadith corpus",
            "Later Sufi masters cited him as an anticipatory figure in the tradition of mystical contemplation (tafakkur) of divine presence in creation"
        ],
        "relationships": [
            {"entity": "Anas ibn Malik", "relationship": "STUDIED_UNDER", "note": "Studied hadith from Anas ibn Malik, one of the most senior Companions of the Prophet and a key transmitter of hadith in Basra"},
            {"entity": "Qutayba ibn Muslim", "relationship": "SERVED_UNDER", "note": "Served as a soldier in Qutayba's Central Asian campaigns expanding the Islamic world into Transoxiana"},
            {"entity": "Umayyad Caliphate", "relationship": "SERVED_UNDER", "note": "Served as qadi in Basra under Umayyad administration alongside his military service"},
            {"entity": "Sufi mystical tradition", "relationship": "INFLUENCED", "note": "His saying about seeing Allah in all things was foundational in later Sufi mystical literature and the contemplative tradition"},
            {"entity": "Zuhd (Islamic asceticism) movement", "relationship": "EXEMPLIFIED", "note": "One of the most admired figures in the early Islamic asceticism movement combining scholarship, piety, and renunciation"}
        ]
    }),

    # 7 — Tariq ibn Amr (fl. 691–693 CE)
    ("tariq-ibn-amr", {
        "summary": (
            "Tariq ibn Amr al-'Amawi (fl. 691–693 CE) was an Umayyad military commander, governor, and political "
            "operative who played an important role in the consolidation of Umayyad power during the Second Fitna "
            "— the civil war that wracked the early Islamic caliphate from 680 to 692 CE. A mawla (freedman and "
            "client) of Caliph Uthman ibn Affan, he entered the service of the Umayyad Caliph Abd al-Malik ibn "
            "Marwan as the caliph worked to reunify the Islamic world after the devastating civil conflict.\n\n"
            "His most politically consequential action was his role in the elimination of Amr ibn Sa'id al-Ashdaq "
            "(died 689 CE), a prominent Umayyad cousin who had been a claimant to the caliphate and a persistent "
            "rival of Abd al-Malik. Amr ibn Sa'id had been a governor of Egypt and Mecca under Muawiya I and had "
            "briefly seized power in Damascus; his continued existence represented an ongoing threat to Abd "
            "al-Malik's consolidation of Umayyad rule. Tariq ibn Amr participated in the events leading to "
            "Amr ibn Sa'id's capture and execution, thereby serving Abd al-Malik in eliminating a dangerous "
            "rival claimant.\n\n"
            "He subsequently served as Umayyad governor of Medina (691/92–693 CE), one of the most politically "
            "sensitive posts in the early Islamic world — Medina was the city of the Prophet and the Companions, "
            "whose opinion carried immense religious authority, and governing it required both political skill "
            "and religious legitimacy. His tenure represented Abd al-Malik's effort to extend direct Umayyad "
            "administrative control over the holy cities.\n\n"
            "His career illustrates the role played by loyal mawali and military commanders in the consolidation "
            "of Umayyad caliphal authority during the crucial transition from civil war to unified imperial rule "
            "under Abd al-Malik."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Umayyad military operative and governor of Medina who aided Abd al-Malik ibn Marwan's consolidation of power during the Second Fitna, including participation in the elimination of the rival claimant Amr ibn Sa'id al-Ashdaq.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Second Fitna (680–692 CE) created a period of intense factional conflict within the Umayyad dynasty, requiring Abd al-Malik to rely on loyal mawali commanders to eliminate rival claimants",
            "Tariq's status as a mawla of Uthman connected him to the Umayyad dynasty's foundational legitimacy and made him a useful political instrument for Abd al-Malik",
            "Abd al-Malik's program of administrative consolidation after the Second Fitna required reliable governors for sensitive posts like Medina"
        ],
        "effects": [
            "His role in the elimination of Amr ibn Sa'id al-Ashdaq aided Abd al-Malik's consolidation of sole Umayyad authority over the caliphate",
            "His governorship of Medina (691/92–693) represented Umayyad extension of direct administrative control over the most symbolically significant city in early Islam",
            "His career demonstrated the important role played by mawali (clients and freedmen) in Umayyad political and military administration",
            "His tenure contributed to the stabilization of Umayyad authority in the Hijaz following the civil wars of the Second Fitna"
        ],
        "relationships": [
            {"entity": "Abd al-Malik ibn Marwan", "relationship": "SERVED", "note": "Served as a loyal military commander and political operative for Caliph Abd al-Malik during the consolidation of Umayyad power"},
            {"entity": "Caliph Uthman ibn Affan", "relationship": "MAWLA_OF", "note": "Was a freedman (mawla) of Caliph Uthman, connecting him to the Umayyad dynasty's founding generation"},
            {"entity": "Amr ibn Sa'id al-Ashdaq", "relationship": "OPPOSED", "note": "Participated in the events leading to the capture and execution of the Umayyad rival claimant Amr ibn Sa'id"},
            {"entity": "Medina", "relationship": "GOVERNED", "note": "Served as Umayyad governor of Medina (691/92–693 CE), one of the most politically sensitive posts in early Islam"},
            {"entity": "Second Fitna", "relationship": "PARTICIPATED_IN", "note": "Played a role in the Umayyad side of the Second Fitna civil war (680–692 CE)"}
        ]
    }),

    # 8 — Francesco Accolti (c. 1416–1484)
    ("francesco-accolti", {
        "summary": (
            "Francesco Accolti (c. 1416–1484), also known as Francesco d'Arezzo, was an Italian jurist of "
            "remarkable versatility whose career in academic law combined with Italian humanist culture to "
            "produce one of the most prominent civil lawyers of the Quattrocento. The younger brother of "
            "Benedetto Accolti — the humanist historian and Chancellor of Florence — Francesco taught "
            "jurisprudence at the University of Bologna (1440–1445) and subsequently at Ferrara, Siena, "
            "and Pisa, accumulating the experience of the itinerant professor-jurist that characterized "
            "the academic careers of the Italian Renaissance legal profession.\n\n"
            "His legal expertise placed him in high demand as a practical consultant to princes, cities, and "
            "the papacy. He issued legal opinions (consilia) on major cases of the period, and his civil "
            "law teaching covered the core texts of the ius commune — the shared Roman and canon law "
            "tradition that governed educated legal practice across European Christendom. His academic "
            "reputation was sufficiently distinguished that he was called Francesco d'Arezzo in recognition "
            "of his Tuscan origins, following the Italian humanist custom of identifying scholars by their "
            "city of origin.\n\n"
            "The Accolti family represented an important intersection between the humanist culture of "
            "15th-century Tuscany and the legal profession. While his brother Benedetto made his reputation "
            "in humanist history and Florentine chancellery, Francesco pursued the academic and consultative "
            "legal career, and his son Bernardo Accolti became a famous improvisatore poet at the Italian "
            "courts — illustrating the cultural range of a prominent Arezzo family whose members moved "
            "fluently between law, letters, and courtly entertainment.\n\n"
            "'He taught law to a generation that also wanted beauty from its learning.' Accolti embodied the "
            "Renaissance ideal of the jurist-humanist who combined legal rigor with cultural distinction."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "A prominent Italian civil law professor who taught at Bologna, Ferrara, Siena, and Pisa, and provided legal consilia to princes and popes; a member of the distinguished Accolti family that combined legal and humanist culture in 15th-century Tuscany.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Italian university system's tradition of itinerant law professors — who moved between universities offering higher salaries — structured Francesco Accolti's career across multiple major cities",
            "The ius commune legal tradition's dominance across European Christendom created sustained demand for trained civil and canon lawyers like Accolti throughout Italy",
            "The humanist culture of 15th-century Tuscany, centered on Florence and Arezzo, shaped the intellectual environment in which the Accolti family combined legal and literary distinction"
        ],
        "effects": [
            "Trained a generation of lawyers at Bologna, Ferrara, Siena, and Pisa who carried the ius commune tradition of civil law into the second half of the 15th century",
            "His legal consilia provided practical legal guidance to princes, cities, and the papacy on major cases of the period, influencing the application of law in significant disputes",
            "As part of the Accolti family network, contributed to the distinctive Tuscan synthesis of legal expertise and humanist culture that characterized Italian intellectual life",
            "His son Bernardo Accolti (the famous improvisatore poet) represented the cultural range of the family — illustrating how legal families could produce both legal professionals and courtly entertainers"
        ],
        "relationships": [
            {"entity": "Benedetto Accolti", "relationship": "BROTHER_OF", "note": "His brother Benedetto was the humanist historian and Chancellor of Florence who shared the family's blend of legal and literary culture"},
            {"entity": "University of Bologna", "relationship": "TAUGHT_AT", "note": "Professed jurisprudence at Bologna from 1440 to 1445 before moving to other universities"},
            {"entity": "University of Pisa", "relationship": "TAUGHT_AT", "note": "Among the universities where Accolti taught civil law during his itinerant academic career"},
            {"entity": "Bernardo Accolti", "relationship": "FATHER_OF", "note": "His son Bernardo became the famous improvisatore poet celebrated at Italian Renaissance courts"},
            {"entity": "Ius commune tradition", "relationship": "TAUGHT", "note": "His teaching covered the core texts of the ius commune — the shared Roman and canon law system governing European legal practice"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 14)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
