#!/usr/bin/env python3
"""
Batch 06 — 8 entities (Class 312): Amorian Dynasty, Antigonid Dynasty,
Antipatrid Dynasty, Arghun Dynasty, Agiads, Aeacidae, Afrasiab Dynasty, Annazids
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/312-Class-312"
FILE_PREFIX = "312"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()


def enrich_entity(slug, data):
    fname = os.path.join(FOLDER, f"{FILE_PREFIX}{slug}.json")
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
    print(f"  ✓ {entity['name']} — sum={slen}c c={len(det.get('causes', []))} e={len(det.get('effects', []))}")


ENTITIES = [

    ("amorian-dynasty", {
        "summary": (
            "The Amorian dynasty (820–867 CE), also called the Phrygian dynasty, was a Byzantine imperial house that ruled the Eastern Roman Empire during a period of military recovery, iconoclasm's final phase, and significant theological controversy. Founded by Michael II the Stammerer — an Anatolian general of humble origin from Amorion in Phrygia — the dynasty produced three emperors: Michael II (820–829), Theophilos (829–842), and Michael III (842–867).\n\n"
            "Theophilos was the last iconoclast emperor — his death in 842 was followed by the 'Triumph of Orthodoxy' under his wife Empress Theodora and the restoration of icon veneration, celebrated to this day as the Feast of Orthodoxy in the Eastern Orthodox Church (first Sunday of Lent). Theophilos also built the Bryas Palace and commissioned cultural works, presenting himself as a Byzantine philosopher-king in the tradition of Marcus Aurelius. His reign was marked by wars against the Arabs — he sacked Zapetra (837 CE) but suffered the catastrophic Arab sack of Amorion (838 CE).\n\n"
            "Michael III, known to later Byzantine tradition as 'the Drunkard', was the dynasty's final emperor — assassinated by his favourite Basil the Macedonian (867 CE), who founded the Macedonian dynasty that would bring Byzantium to its medieval zenith. Michael III's reign saw the Christianisation of the Slavs through the Cyrillo-Methodian mission (863 CE) — one of the most consequential cultural events in European history."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Byzantine dynasty (820–867); Theophilos was the last iconoclast emperor — his death triggered the 'Triumph of Orthodoxy' (842); Michael III's reign saw the Cyrillo-Methodian mission (863) that Christianised the Slavs; ended when Basil the Macedonian murdered Michael III and founded the Macedonian dynasty.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Michael II's victory in the civil war against Leo V the Armenian (820) — who had restored iconoclasm — brought a general of Anatolian peasant origin to the throne, continuing the iconoclast policy but in a more moderate form",
            "The Anatolian military aristocracy's political power — demonstrated by Michael II's and Theophilos's origins as Phrygian generals — reflected the shift of Byzantine power toward Anatolian military themes that characterised the middle Byzantine period",
            "The theological controversy over iconoclasm — dividing the Byzantine court, clergy, and populace — created the political instability that made the transition from the Amorian to the Macedonian dynasty possible through assassination"
        ],
        "effects": [
            "The 'Triumph of Orthodoxy' (843 CE) — the restoration of icon veneration under Empress Theodora following Theophilos's death — ended the Byzantine iconoclast controversy and established the theological position that defines Eastern Orthodox Christianity's visual culture to this day",
            "The Cyrillo-Methodian mission to the Slavs (863 CE) — authorised during Michael III's reign — created the Glagolitic/Cyrillic alphabet and began the Christianisation of Slavic peoples, one of the most consequential cultural transformations in European history",
            "The Arab sack of Amorion (838 CE) — capturing and executing 42 Byzantine officers — produced a major martyrology in Byzantine hagiography and exemplified the persistent Arab threat to Anatolia that shaped Byzantine military strategy",
            "Basil the Macedonian's assassination of Michael III (867 CE) and his founding of the Macedonian dynasty created the political framework that led to Byzantium's 10th-century golden age under Basil II"
        ],
        "relationships": [
            {"entity": "Michael II the Stammerer", "relationship": "FOUNDED_BY", "note": "Michael II (820–829) founded the Amorian dynasty after killing Leo V the Armenian in a palace coup"},
            {"entity": "Theophilos (Emperor)", "relationship": "MOST_SIGNIFICANT_RULER_OF", "note": "Theophilos (829–842) was the last iconoclast emperor — his death triggered the Triumph of Orthodoxy"},
            {"entity": "Triumph of Orthodoxy (843 CE)", "relationship": "TRIGGERED_BY_DEATH_OF_LAST_EMPEROR_OF", "note": "The Triumph of Orthodoxy (843) — restoring icon veneration — was triggered by Theophilos's death and implemented by Empress Theodora"},
            {"entity": "Cyrillo-Methodian mission", "relationship": "REIGN_AUTHORISED", "note": "The mission to the Slavs (863 CE) was authorised during Michael III's reign — beginning the Christianisation of Slavic peoples and the creation of the Cyrillic alphabet"},
            {"entity": "Basil I the Macedonian", "relationship": "DYNASTY_ENDED_BY_ASSASSINATION_BY", "note": "Basil I murdered Michael III (867 CE) and founded the Macedonian dynasty — which brought Byzantium to its medieval zenith"}
        ],
    }),

    ("antipatrid-dynasty", {
        "summary": (
            "The Antipatrid dynasty was a Macedonian ruling house that briefly controlled Macedon during the Wars of the Diadochi following Alexander the Great's death. The dynasty's founder was Antipater — Alexander's regent of Macedon during the Persian campaign — whose political skill maintained Macedonian control of Greece during Alexander's absence. His son Cassander became the most powerful Macedonian figure of the early Diadochi period (321–297 BCE), controlling Macedon and Greece and famously ordering the execution of Alexander's mother Olympias, his wife Roxana, and his son Alexander IV.\n\n"
            "Cassander's role in eliminating the Argead royal family made him one of the most controversial figures of the Diadochi period. By murdering Alexander IV (the last legitimate Argead heir) in 310/309 BCE, Cassander effectively ended the Argead dynasty and cleared the way for the successor kings to claim royal titles without reference to Alexander's bloodline. Cassander himself took the title of King of Macedon in 305 BCE.\n\n"
            "The Antipatrid dynasty was short-lived: after Cassander's death (297 BCE), his sons fought each other and within a few years Demetrius Poliorcetes seized Macedon. The dynasty's historical significance lies primarily in Cassander's decisive role in eliminating the Argead bloodline — the act that definitively closed the era of Alexander and opened the Hellenistic period of fully independent successor kingdoms."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Macedonian dynasty of the Diadochi period; Cassander (d. 297 BCE) eliminated the last Argead heirs — Alexander IV and Roxana — definitively ending Alexander's dynasty; this act opened the Hellenistic period of independent successor kingdoms claiming rule without Argead legitimacy.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Antipater's position as Alexander's regent in Macedon — maintaining control of Greece during the Persian campaign and suppressing the Lamian War (323–322 BCE) that followed Alexander's death — gave his family the institutional base to become a major Diadochi power",
            "Cassander's personal ambition and the political logic of the Diadochi wars — where any claimant to Alexander's legacy who left the Argead bloodline alive was vulnerable to challenge — drove the systematic elimination of Alexander's family",
            "The lack of a clear successor arrangement by Alexander — his famous last words reportedly 'to the strongest' — created the free-for-all competition that made the Antipatrids' elimination of the Argead line politically rational if morally brutal"
        ],
        "effects": [
            "Cassander's elimination of Alexander IV (310/309 BCE) — the last legitimate Argead heir — ended the Argead dynasty and definitively closed the era of Alexander, opening the fully independent Hellenistic kingdoms",
            "The founding of Thessaloniki by Cassander (315 BCE) — named after his wife Thessalonike, Alexander's half-sister — created a city that became one of the most important in the Byzantine Empire and modern Greece",
            "Cassander's construction of Cassandreia (316 BCE) — built on the site of ancient Potidaea — created a significant Macedonian city whose history continued through the Byzantine and Ottoman periods",
            "The collapse of the Antipatrid dynasty after Cassander's death (297 BCE) and the subsequent chaos that brought Demetrius Poliorcetes to the throne accelerated Macedon's political instability in the early 3rd century BCE"
        ],
        "relationships": [
            {"entity": "Antipater", "relationship": "FOUNDED_BY", "note": "Antipater — Alexander's regent in Macedon — founded the dynasty, though his son Cassander is its most historically significant figure"},
            {"entity": "Cassander of Macedon", "relationship": "MOST_POWERFUL_RULER_OF", "note": "Cassander eliminated the last Argead heirs and took the title King of Macedon (305 BCE)"},
            {"entity": "Alexander IV of Macedon", "relationship": "ARGEAD_HEIR_ELIMINATED_BY", "note": "Cassander ordered the murder of Alexander IV (310/309 BCE) — the last Argead heir — definitively ending Alexander's bloodline"},
            {"entity": "Thessaloniki", "relationship": "FOUNDED", "note": "Cassander founded Thessaloniki (315 BCE) — named after his wife — which became one of the most important cities of the Byzantine Empire"},
            {"entity": "Argead dynasty", "relationship": "ELIMINATED_LAST_HEIRS_OF", "note": "The Antipatrids' elimination of Roxana, Olympias, and Alexander IV effectively ended the Argead dynasty and opened the Hellenistic period"}
        ],
    }),

    ("arghun-dynasty", {
        "summary": (
            "The Arghunids (c. 1519–1591) were a Timurid-origin dynasty that ruled Sindh and parts of the lower Indus Valley in what is now Pakistan and Afghanistan. The dynasty was founded by Shah Beg Arghun, who conquered Sindh from the Samma dynasty (1519) and established the Arghunid capital at Thatta — a major city of the lower Indus that became a centre of Sindhi art, literature, and trade. The Arghunids were nominally subjects of the Timurid-Mughal empire but maintained practical independence.\n\n"
            "The Arghunid period is important for Sindhi cultural history: Thatta under the Arghunids developed as a centre of Sindhi poetry, Islamic scholarship, and the distinctive Sindhi architectural tradition exemplified by the Makli necropolis — the UNESCO World Heritage Site outside Thatta that contains some of the most elaborate medieval funerary monuments in South Asia. The Makli monuments, built by Arghunid and subsequent Tarkhani rulers, represent the finest achievement of Sindhi Islamic architecture.\n\n"
            "The Arghunids were succeeded by the Tarkhani dynasty (c. 1556–1591) — also of Timurid origin — before the region was absorbed into the Mughal Empire under Akbar (1591). The two dynasties are often grouped as the 'Arghun-Tarkhan' period, representing the last independent phase of Sindhi history before Mughal incorporation."
        ),
        "importanceScore": 5,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Timurid-origin dynasty ruling Sindh (c. 1519–1556); capital Thatta was a centre of Sindhi poetry and Islamic scholarship; their funerary monuments at the Makli necropolis (UNESCO World Heritage Site) are the finest achievement of Sindhi Islamic architecture.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The decline of the Samma dynasty's military power and the political fragmentation of the lower Indus Valley created the opening for Shah Beg Arghun's conquest of Sindh (1519)",
            "The Timurid tradition of administrative sophistication and cultural patronage — which Shah Beg Arghun's family brought from Kandahar — created the framework for the Arghunids' cultural florescence at Thatta",
            "Thatta's strategic position at the mouth of the Indus — controlling access to the river's trade routes and the Arabian Sea trade — made it a commercially wealthy capital that could sustain cultural patronage"
        ],
        "effects": [
            "The Makli necropolis — built by Arghunid and Tarkhani rulers near Thatta — is one of the largest necropolises in the world and contains some of South Asia's most elaborate funerary monuments, designated a UNESCO World Heritage Site (1981)",
            "The Arghunid/Tarkhani period established Thatta as a centre of Sindhi Islamic scholarship and architecture — a tradition that survived Mughal incorporation and continued to produce distinctive Sindhi cultural achievements",
            "The Mughal absorption of Sindh under Akbar (1591) integrated the lower Indus Valley into the Mughal administrative system — ending the dynasty's independence but connecting Sindh to the broader Mughal cultural sphere",
            "The Arghunid administrative precedents in Sindh — tax systems, irrigation management, urban organisation — provided the framework that the Mughals built upon in governing one of South Asia's most agriculturally productive regions"
        ],
        "relationships": [
            {"entity": "Shah Beg Arghun", "relationship": "FOUNDED_BY", "note": "Shah Beg Arghun conquered Sindh (1519) from the Samma dynasty and founded the Arghunid ruling house"},
            {"entity": "Makli necropolis", "relationship": "CONSTRUCTED_FUNERARY_MONUMENTS_AT", "note": "The Arghunids built elaborate funerary monuments at Makli — a UNESCO World Heritage Site representing the finest achievement of Sindhi Islamic architecture"},
            {"entity": "Thatta", "relationship": "CAPITAL_OF", "note": "Thatta on the lower Indus was the Arghunid capital — a centre of Sindhi poetry, scholarship, and trade"},
            {"entity": "Mughal Empire", "relationship": "TERRITORY_ABSORBED_INTO", "note": "Sindh was absorbed into the Mughal Empire under Akbar (1591) — ending the Arghunid/Tarkhani period of independent rule"},
            {"entity": "Tarkhani dynasty", "relationship": "SUCCEEDED_BY", "note": "The Tarkhani dynasty (c. 1556–1591) succeeded the Arghunids in Sindh, continuing the Timurid-origin ruling tradition before Mughal absorption"}
        ],
    }),

    ("agiads", {
        "summary": (
            "The Agiads were one of the two royal houses of ancient Sparta — the senior of the two dynasties (the other being the Eurypontids) that jointly ruled the Spartan state in its unique system of dual kingship. The Agiad dynasty traced its legendary foundation to Agis I, a descendant of Heracles, and the historical dynasty spanned from approximately the 9th century BCE to the Roman conquest of Greece. The most celebrated Agiad kings were Cleomenes I (r. c. 520–490 BCE) — the dominant Spartan statesman of his era who expelled the Pisistratid tyrants from Athens — and Leonidas I, the hero of Thermopylae.\n\n"
            "Leonidas I's stand at Thermopylae (480 BCE) — commanding 300 Spartans and roughly 7,000 allied Greeks against the Persian invasion of Xerxes — is the most celebrated military sacrifice in Western history. Leonidas's death with his 300 Spartans at Thermopylae became the defining symbol of military courage, self-sacrifice, and resistance against overwhelming odds, shaping Western military ethics and the mythology of Spartan virtue.\n\n"
            "The last significant Agiad king was Cleomenes III (r. 235–222 BCE), who attempted a social revolution — cancelling debts, redistributing land, and expanding Spartan citizenship — to restore Sparta's military power. His defeat at Sellasia (222 BCE) by the Macedonian Antigonid Antigonus III Doson ended Spartan independence. The Agiad dynasty continued in a ceremonial capacity under Roman suzerainty until the 1st century CE."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Senior royal house of ancient Sparta; Leonidas I's stand at Thermopylae (480 BCE) with 300 Spartans is the most celebrated military sacrifice in Western history; Cleomenes I expelled the Athenian Pisistratids; Cleomenes III attempted a revolutionary social reform to restore Sparta's military power.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Sparta's unique dual monarchy — the Agiads as senior house, the Eurypontids as junior — emerged from the original conquest of the Peloponnese by two Heraclid brothers, and the system survived because it balanced royal power with the ephors (magistrates) and Gerousia (council of elders)",
            "Sparta's military-social system (the agoge training, the helot agricultural base, the peer warrior culture) created the conditions in which royal prestige depended entirely on military leadership — making the Agiad kings primarily military commanders rather than administrative rulers",
            "The Persian Wars (499–479 BCE) placed Sparta at the centre of Greek politics — making the Agiad king the nominal commander of the Greek alliance and elevating Leonidas's sacrifice at Thermopylae into the defining moment of Greek civilisational identity"
        ],
        "effects": [
            "Leonidas I's stand at Thermopylae (480 BCE) became the foundational myth of Western military virtue — inspiring the concept of the military's duty to sacrifice for the state, cited in military ethics from Plutarch to modern special forces culture",
            "Cleomenes I's expulsion of the Pisistratids from Athens (510 BCE) — at Spartan initiative — created the conditions for Athenian democracy (Cleisthenes' reforms, 508 BCE), making Sparta inadvertently the midwife of Athenian democratic culture",
            "Cleomenes III's social revolution (235–222 BCE) — cancelling debts and redistributing land — was the most radical domestic reform in classical Greek politics and provided a model for later Hellenistic social revolutionaries",
            "The Agiad dynasty's dual monarchy model — balancing hereditary kingship with elective magistrates and an oligarchic council — was studied by Aristotle in the Politics as a 'mixed constitution' and influenced subsequent political theory"
        ],
        "relationships": [
            {"entity": "Leonidas I of Sparta", "relationship": "MOST_CELEBRATED_RULER_OF", "note": "Leonidas I's stand at Thermopylae (480 BCE) with 300 Spartans is the most celebrated military sacrifice in Western history"},
            {"entity": "Battle of Thermopylae (480 BCE)", "relationship": "AGIAD_KING_DIED_AT", "note": "Leonidas I's death at Thermopylae — holding the pass against Xerxes' Persian army — became the defining symbol of military sacrifice"},
            {"entity": "Cleomenes I of Sparta", "relationship": "DOMINANT_STATESMAN_OF_ERA_OF", "note": "Cleomenes I (c. 520–490 BCE) expelled the Pisistratid tyrants from Athens — inadvertently enabling Athenian democracy"},
            {"entity": "Sparta", "relationship": "SENIOR_ROYAL_HOUSE_OF", "note": "The Agiads were the senior of Sparta's two royal houses — providing military commanders and statesmen across five centuries"},
            {"entity": "Cleomenes III of Sparta", "relationship": "LAST_GREAT_RULER_OF", "note": "Cleomenes III's attempted social revolution (235–222 BCE) — cancelling debts, redistributing land — was the last significant Agiad effort to restore Sparta's military power"}
        ],
    }),

    ("aeacidae", {
        "summary": (
            "The Aeacidae were the royal dynasty of ancient Epirus — a kingdom in northwestern Greece (modern northwestern Greece and southern Albania) — claiming descent from Achilles through the mythological hero Aeacus. The dynasty's most celebrated member was Pyrrhus of Epirus (r. 306–302, 297–272 BCE) — one of the ancient world's greatest generals, whose Italian campaigns (280–275 BCE) gave the English language the term 'Pyrrhic victory'.\n\n"
            "Pyrrhus of Epirus invaded southern Italy (280 BCE) at the invitation of the Tarentines to fight Rome — winning the battles of Heraclea (280 BCE) and Asculum (279 BCE) but at such devastating cost to his own army that his alleged remark 'One more such victory and I am undone' became proverbial. Pyrrhus was the only general of the classical era to achieve battlefield victories against Roman legions in Italy, and Hannibal Barca reportedly called him the greatest general in history (ranking him above even Alexander the Great).\n\n"
            "The Aeacidae dynasty ruled Epirus until the Roman destruction of Epirus (168 BCE) following Perseus's defeat at Pydna — a punitive campaign that enslaved approximately 150,000 Epirote people and destroyed 70 cities. The dynasty thus ended with one of the most brutal acts of Roman collective punishment in the Republican period, making Epirus a cautionary example of resistance to Roman power."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Royal dynasty of ancient Epirus; Pyrrhus of Epirus (one of antiquity's greatest generals) gave English the term 'Pyrrhic victory' through his Italian campaigns (280–275 BCE); Hannibal called Pyrrhus the world's greatest general; Rome destroyed Epirus (168 BCE), enslaving 150,000.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Epirus's geographic position — between the Macedonian sphere to the east and the Adriatic to the west — gave it strategic importance and enabled the Aeacidae to play Rome and Macedon off against each other",
            "Pyrrhus's military genius — he was Alexander the Great's second cousin and saw himself as Alexander's heir — and his ambition to recreate an Alexandrian western empire drew him into the Italian campaigns that produced the Pyrrhic victories",
            "Tarentum's invitation to Pyrrhus (280 BCE) — seeking a protector against Roman expansion in southern Italy — provided the diplomatic framework for the first Greek military challenge to Roman power in Italy"
        ],
        "effects": [
            "Pyrrhus's Italian campaigns (280–275 BCE) gave the English language 'Pyrrhic victory' — a triumph so costly that it amounts to defeat — one of antiquity's most enduring contributions to the vocabulary of political and military analysis",
            "The battles of Heraclea and Asculum demonstrated that Roman legions were vulnerable to Hellenistic-style phalanx and elephant tactics — lessons that Rome absorbed and adapted, developing the tactical flexibility that would eventually conquer the Hellenistic world",
            "Rome's punishment of Epirus after Pydna (168 BCE) — enslaving approximately 150,000 people, destroying 70 cities — was one of the most devastating acts of collective punishment in the Republican period and demonstrated the consequences of opposing Rome",
            "Pyrrhus's career — winning every battle but losing every war — became the ancient world's most discussed example of strategic failure despite tactical brilliance, studied by Polybius, Livy, and subsequently Clausewitz and modern strategists"
        ],
        "relationships": [
            {"entity": "Pyrrhus of Epirus", "relationship": "GREATEST_RULER_OF", "note": "Pyrrhus — the greatest Aeacid king — gave English 'Pyrrhic victory' through his devastating Italian campaigns against Rome (280–275 BCE)"},
            {"entity": "Battle of Heraclea (280 BCE)", "relationship": "PYRRHIC_VICTORY_AT", "note": "Pyrrhus defeated the Romans at Heraclea (280 BCE) but at devastating cost — the first of the 'Pyrrhic victories'"},
            {"entity": "Roman Republic", "relationship": "MILITARILY_CHALLENGED_AND_ULTIMATELY_DEFEATED_BY", "note": "The Aeacidae challenged Rome through Pyrrhus's Italian campaigns — before Rome destroyed Epirus in 168 BCE as punishment for supporting Perseus"},
            {"entity": "Hannibal Barca", "relationship": "NAMED_GREATEST_GENERAL_BY", "note": "Hannibal reportedly ranked Pyrrhus as the world's greatest general — above even Alexander the Great — in his conversation with Scipio Africanus"},
            {"entity": "Epirus", "relationship": "RULING_DYNASTY_OF", "note": "The Aeacidae ruled Epirus from approximately the 4th century BCE until Rome's destruction of Epirus in 168 BCE"}
        ],
    }),

    ("anscarids", {
        "summary": (
            "The Anscarids (also Anscarians or House of Ivrea) were a medieval Italian noble house that played a significant role in the political turbulence of 10th-century Italy. The dynasty descended from Anscar I of Ivrea (d. c. 902), a Frankish nobleman who became Margrave of Ivrea in northwestern Italy. The house's most politically prominent members were Berengar I of Italy (r. 888–924), who became King of Italy and Holy Roman Emperor (emperor 915–924), and his grandson Berengar II (r. 949–963), who attempted to consolidate Italian royal power before being overthrown by Otto I of Germany.\n\n"
            "The Anscarids' significance lies in their role during the period of Italian political fragmentation following the collapse of Carolingian central authority. Berengar I was the last 'Italian' Holy Roman Emperor — subsequent emperors were German — and his reign represents the final attempt to maintain an independent Italian kingdom within the Carolingian framework. Berengar II's overthrow by Otto I in 963 CE marked the definitive beginning of German imperial control over Italy that would shape European politics for the following three centuries.\n\n"
            "The dynasty also produced Adelaide of Italy — Berengar II's daughter-in-law who fled his imprisonment to become the wife of Otto I and subsequently Holy Roman Empress. Adelaide was later canonised (1097) and is venerated as a saint in the Catholic Church. The Anscarids' political collapse thus paradoxically produced one of the most influential women of medieval Europe."
        ),
        "importanceScore": 5,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Medieval Italian noble house; Berengar I was the last 'Italian' Holy Roman Emperor (915–924); Berengar II's overthrow by Otto I (963) began German imperial control of Italy; the dynasty produced Adelaide of Italy — Holy Roman Empress and Catholic saint.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The collapse of Carolingian central authority in the late 9th century — following the deposition of Charles the Fat (887) — created the power vacuum in Italy that allowed regional nobles like Anscar I and his descendants to seize the Italian kingship",
            "Berengar I's military success against the Magyars (Magyar raids devastated northern Italy in the late 9th–10th centuries) gave him the military prestige needed to claim the Italian throne and eventually the imperial title",
            "The absence of a strong German royal power during the late Carolingian period — and the subsequent Ottonian revival's focus northward initially — gave Italian nobles a window of opportunity to build their own kingdom"
        ],
        "effects": [
            "Berengar I's reign (888–924) as the last native Italian holder of the imperial title established a precedent of Italian royal independence that Italian communes and city-states would invoke in their conflicts with German emperors for the following three centuries",
            "Otto I's defeat of Berengar II (963 CE) and his assumption of the Italian crown definitively integrated Italy into the Holy Roman Empire — beginning the centuries-long conflict between German emperors and Italian popes and communes",
            "Adelaide of Italy's marriage to Otto I — facilitated by her flight from Berengar II's imprisonment — made her Holy Roman Empress and one of the most politically influential women of the 10th century, canonised in 1097",
            "The Anscarid collapse contributed to Italy's political fragmentation — the absence of a unified Italian state — that characterised Italian history until the Risorgimento (1861), with direct consequences for the peninsula's vulnerability to subsequent invasions"
        ],
        "relationships": [
            {"entity": "Berengar I of Italy", "relationship": "MOST_POWERFUL_RULER_OF", "note": "Berengar I (r. 888–924) was the last native Italian Holy Roman Emperor — his reign the final attempt to maintain Italian independence within the Carolingian framework"},
            {"entity": "Otto I, Holy Roman Emperor", "relationship": "BERENGAR_II_OVERTHROWN_BY", "note": "Otto I's defeat of Berengar II (963 CE) ended Anscarid power and began German imperial dominance of Italy"},
            {"entity": "Adelaide of Italy", "relationship": "PRODUCED", "note": "The Anscarids produced Adelaide of Italy — Holy Roman Empress, wife of Otto I, and Catholic saint (canonised 1097)"},
            {"entity": "Holy Roman Empire", "relationship": "LAST_NATIVE_ITALIAN_RULERS_OF", "note": "The Anscarids were the last Italian (rather than German) holders of the imperial title before Otto I definitively Germanised the empire"},
            {"entity": "Carolingian Empire", "relationship": "SUCCESSORS_TO_IN_ITALY", "note": "The Anscarids emerged from the collapse of Carolingian authority in Italy — representing the transition from Carolingian to Ottonian/German imperial power"}
        ],
    }),

    ("annazids", {
        "summary": (
            "The Annazids (990–1117 CE) were a Kurdish Muslim dynasty that ruled the Sharazur region — a fertile plain in the Zagros mountain foothills of what is now northern Iraq and western Iran — during the Buyid period. Founded by Abu al-Shawk Muhammad ibn Annaz, the dynasty emerged in the fragmented political landscape of the post-Abbasid provincial system and maintained regional independence for over a century despite the competing pressures of the Buyid, Marwanid, and later Seljuk powers.\n\n"
            "The Annazids are historically significant as one of the earliest documented Kurdish dynasties, providing evidence for Kurdish political organisation and regional autonomy prior to the Seljuk period. Like other smaller dynasties of the period — the Marwanids, Hasanwayhids, and Rawwadids — they represent the florescence of local, often ethnically distinct ruling houses in the spaces between the great empires of the 10th–11th centuries.\n\n"
            "The Annazid dynasty ended when the Seljuk Empire absorbed their territory in the early 12th century, integrating the Sharazur region into the broader Seljuk administrative system. Their rule is known primarily from numismatic evidence and brief mentions in contemporary chronicles."
        ),
        "importanceScore": 4,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Kurdish Muslim dynasty ruling Sharazur in the Zagros foothills (990–1117); one of the earliest documented Kurdish dynasties; evidence of Kurdish political organisation in the Buyid period before Seljuk absorption; known primarily from numismatic evidence.",
            "significanceCategory": "local"
        },
        "causes": [
            "The fragmentation of the Abbasid Caliphate's provincial authority in the 10th century — with Buyid Persian domination of Baghdad reducing the caliph to a figurehead — created the political conditions in which Kurdish tribal leaders could assert regional dynasties",
            "The Sharazur plain's agricultural productivity and its strategic position at the junction of major routes between Mesopotamia and Iran gave the local ruling family the resources to build a viable regional state",
            "The competition between Buyid, Byzantine, and emerging Seljuk powers created a strategic ambiguity that small dynasties like the Annazids could exploit — playing powers off against each other to maintain independence"
        ],
        "effects": [
            "The Annazid dynasty provides one of the earliest documented examples of Kurdish political autonomy — evidence for Kurdish dynastic governance predating the better-documented medieval Kurdish dynasties like the Ayyubids",
            "The numismatic evidence from Annazid rule contributes to our knowledge of the monetary systems, titulary, and political claims of minor regional dynasties in the Buyid period — important for understanding the local political culture of medieval Iraq and Iran",
            "The Seljuk absorption of the Annazid territories integrated the Zagros foothills into the Seljuk administrative system — beginning the process by which Kurdish tribal regions became subjects of successive Turkic empires",
            "The Annazids exemplify the pattern of 'intermediate dynasties' — Kurdish, Dailamite, and Arab — that filled the political space between the great empires of the 10th–12th centuries, demonstrating the persistence of local power structures"
        ],
        "relationships": [
            {"entity": "Abu al-Shawk Muhammad ibn Annaz", "relationship": "FOUNDED_BY", "note": "Abu al-Shawk Muhammad ibn Annaz founded the Annazid dynasty in the Sharazur region in 990 CE"},
            {"entity": "Buyid dynasty", "relationship": "CONTEMPORARY_WITH_AND_SUBORDINATE_NEIGHBOUR_OF", "note": "The Annazids emerged in the Buyid period — operating in the fragmented political space created by Buyid dominance of the Abbasid caliphate"},
            {"entity": "Seljuk Empire", "relationship": "TERRITORY_ABSORBED_INTO", "note": "The Seljuk Empire absorbed Annazid territories in the early 12th century, ending the dynasty's regional independence"},
            {"entity": "Kurdish history", "relationship": "EARLY_DYNASTIC_EVIDENCE_FOR", "note": "The Annazids are one of the earliest documented Kurdish dynasties — evidence for Kurdish political organisation before the Seljuk period"},
            {"entity": "Sharazur", "relationship": "RULING_DYNASTY_OF", "note": "The Annazids ruled the Sharazur plain in the Zagros foothills — a fertile agricultural region between Mesopotamia and Iran"}
        ],
    }),

    ("abhira", {
        "summary": (
            "The Abhiras were an ancient South Asian tribal people — possibly of semi-nomadic pastoral origin — who established regional power in parts of western and central India during the early centuries CE. Several Abhira kings are attested in inscriptions and puranic genealogies, ruling in the Nasik-Pune region and parts of Gujarat and Rajasthan after the decline of the Satavahana dynasty. A line of Abhira kings is listed in the Puranas as ruling Nasik (c. 3rd century CE), and Abhira governors are mentioned in Satavahana inscriptions.\n\n"
            "The Abhiras' historical significance is debated: while they left no great monuments or texts, their inscriptional presence in post-Satavahana western India indicates they were one of several tribal groups who filled regional power vacuums as the classical dynasties declined. Their relationship to later communities — some scholars have proposed connections to the Ahir (herding caste) communities of modern India — remains a subject of historical and anthropological debate.\n\n"
            "The Abhiras represent the broader phenomenon of tribal and pastoral peoples who periodically established regional kingdoms in South Asian history — groups that appear in inscriptions and literary sources but left limited archaeological evidence, making their full history difficult to reconstruct."
        ),
        "importanceScore": 3,
        "historicalSignificance": {
            "significanceScore": 3,
            "significanceNarrative": "Ancient South Asian tribal dynasty (c. 3rd century CE) attested in inscriptions and puranic genealogies; ruled parts of western India after Satavahana decline; their possible connection to the modern Ahir herding communities is a subject of scholarly debate.",
            "significanceCategory": "local"
        },
        "causes": [
            "The decline of the Satavahana dynasty in the 3rd century CE created regional power vacuums in western and central India that tribal groups like the Abhiras — with established pastoral networks and warrior traditions — could fill",
            "The Abhiras' pastoral mobility and military organisation — typical of semi-nomadic herding communities — gave them military advantages over settled agricultural populations in the fluid political environment of the post-Satavahana period",
            "The puranic tradition's interest in cataloguing all known dynasties — including minor tribal kingdoms — preserved the Abhiras in historical memory despite their limited epigraphic legacy"
        ],
        "effects": [
            "The Abhira period in western India represents a transitional phase between the Satavahana classical period and the Vakataka and Gupta imperial consolidations — a period of regional fragmentation that has been little studied relative to the major dynasties",
            "The possible genealogical connection between the Abhiras and the modern Ahir communities (one of India's largest pastoral castes) — if accepted — would make the Abhiras an important reference point for the deep history of pastoral communities in South Asia",
            "The Abhira inscriptional evidence contributes to the limited body of epigraphic sources for 3rd-century western India — providing data points for the political geography of the period",
            "The Abhiras exemplify the 'middle kingdoms' problem of South Asian historiography — the difficulty of reconstructing the history of regional powers that left limited evidence compared to the major imperial dynasties"
        ],
        "relationships": [
            {"entity": "Satavahana dynasty", "relationship": "EMERGED_AFTER_DECLINE_OF", "note": "The Abhiras filled regional power vacuums in western India after the Satavahana dynasty's decline in the 3rd century CE"},
            {"entity": "Nasik (Nashik)", "relationship": "REGIONAL_CAPITAL_OF", "note": "Puranic genealogies record Abhira kings ruling the Nasik region of Maharashtra"},
            {"entity": "Ahir communities", "relationship": "POSSIBLY_ANCESTRAL_TO", "note": "Some scholars propose a genealogical connection between the ancient Abhiras and the modern Ahir herding communities — a debated historical claim"},
            {"entity": "Vakataka dynasty", "relationship": "REGION_SUBSEQUENTLY_RULED_BY", "note": "The Vakataka dynasty subsequently consolidated the regions where the Abhiras had exercised power in western and central India"},
            {"entity": "Puranas", "relationship": "DYNASTIC_LISTS_PRESERVED_IN", "note": "The Abhira kings are preserved in puranic genealogical lists — one of the primary sources for this obscure dynasty"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 06 — {len(ENTITIES)} entities (Class 312: Byzantine, Macedonian, Central Asian & Regional Dynasties)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
