#!/usr/bin/env python3
"""
Batch 04 — 8 entities (Class 312): Abbasids, Achaemenid Dynasty, Argead Dynasty,
Almohad Caliphate, Ahom Dynasty, Ajuran Empire, Aghlabids, Adal Sultanate
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

    ("abbasids", {
        "summary": (
            "The Abbasid Caliphate (750–1258 CE) was the third Islamic caliphate and the longest-lived, ruling from Baghdad over the Islamic world at the height of its civilisational power. The Abbasids came to power through the Abbasid Revolution (747–750), overthrowing the Umayyad dynasty in a movement that mobilised non-Arab Muslims — particularly Persians — who had been marginalised under the Arab-dominated Umayyad system. The dynasty's founder, As-Saffah, established the caliphate; his brother Al-Mansur founded Baghdad (762 CE), the Round City that became the largest city in the world.\n\n"
            "The Abbasid Golden Age (c. 750–1000 CE) under caliphs including Harun al-Rashid and Al-Ma'mun was one of the greatest eras of intellectual and cultural florescence in history. The House of Wisdom (Bayt al-Hikma) in Baghdad translated Greek, Persian, and Indian texts into Arabic and generated original contributions in mathematics, astronomy, medicine, philosophy, and literature. Algebra, the concept of zero in positional notation, and trigonometry all reached the medieval West through Abbasid scholarship. The court of Harun al-Rashid was immortalised in the Thousand and One Nights.\n\n"
            "The Caliphate fragmented politically from the 9th century as provincial dynasties asserted autonomy, but Baghdad remained the spiritual centre of Sunni Islam. The Mongol sack of Baghdad (1258) — killing the last Abbasid caliph Al-Musta'sim — ended 500 years of caliphal succession and traumatised the Islamic world, marking the symbolic end of the classical Islamic civilisation."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Third Islamic caliphate (750–1258); founded Baghdad; presided over the Islamic Golden Age; the House of Wisdom transmitted Greek, Persian, and Indian knowledge to the medieval West; the Mongol sack of Baghdad (1258) ended the caliphate and traumatised the Islamic world.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Umayyad Caliphate's discrimination against non-Arab Muslims — particularly Persians and mawali (clients) who were denied equal status despite conversion — created the broad coalition that the Abbasid Revolution mobilised",
            "The Abbasid claim to descent from Muhammad's uncle Abbas gave them the religious legitimacy to overthrow the Umayyads — whose legitimacy had been undermined by the Battle of Karbala (680) and their perceived impiety",
            "The Persian administrative and cultural heritage — channelled through the Khurasani armies and Iranian bureaucrats who provided the Abbasids' governing capacity — gave the new dynasty both military power and administrative sophistication"
        ],
        "effects": [
            "The Abbasid Golden Age (c. 750–1000 CE) transmitted the intellectual heritage of Greece, Persia, and India to the medieval West — algebra, trigonometry, medicine, optics, and philosophy — providing the knowledge base for the European Renaissance",
            "Baghdad under the Abbasids became the largest city in the world (c. 800 CE, population ~1 million) and the commercial and intellectual hub of the Silk Road network, shaping trade patterns from Spain to China",
            "The Abbasid model of multicultural Islamic governance — incorporating Persian bureaucratic traditions, Greek rational philosophy, and Islamic jurisprudence — became the template for subsequent Islamic dynasties from the Fatimids to the Ottomans",
            "The Mongol sack of Baghdad (1258) — killing approximately 200,000 people and destroying the House of Wisdom — was the catastrophic rupture of the classical Islamic world, redirecting Islamic civilisation's centre from the Middle East to Cairo and subsequently Istanbul"
        ],
        "relationships": [
            {"entity": "Baghdad", "relationship": "FOUNDED_CAPITAL_AT", "note": "Al-Mansur founded Baghdad (762 CE) as the Abbasid capital — the Round City that became the largest city in the world"},
            {"entity": "House of Wisdom (Bayt al-Hikma)", "relationship": "ESTABLISHED", "note": "The Abbasids established the House of Wisdom — the translation and research institution that transmitted Greek, Persian, and Indian knowledge to the Islamic world"},
            {"entity": "Harun al-Rashid", "relationship": "GOLDEN_AGE_PRESIDED_OVER_BY", "note": "Harun al-Rashid's reign (786–809 CE) represented the Abbasid Golden Age — immortalised in the Thousand and One Nights"},
            {"entity": "Mongol Empire", "relationship": "DESTROYED_BY", "note": "The Mongol army under Hulagu Khan sacked Baghdad (1258) — killing the last caliph Al-Musta'sim and ending 500 years of Abbasid rule"},
            {"entity": "Islamic Golden Age", "relationship": "PRESIDED_OVER", "note": "The Abbasid Caliphate presided over the Islamic Golden Age — the era of greatest intellectual and cultural achievement in medieval Islamic civilisation"}
        ],
    }),

    ("achaemenid-dynasty", {
        "summary": (
            "The Achaemenid dynasty (c. 550–330 BCE) founded and ruled the first Persian Empire — the largest empire the ancient world had yet seen, stretching from the Aegean Sea and Egypt in the west to the Indus River in the east and encompassing roughly 44% of the global population at its peak under Darius I. The dynasty was founded by Cyrus II (Cyrus the Great), whose conquest of Media, Lydia, and Babylon (539 BCE) created the first world empire and whose Cylinder — proclaiming freedom of religion and protection of conquered peoples — is often cited as the world's first human rights declaration.\n\n"
            "The Achaemenid administrative system was a revolution in imperial governance: the empire was divided into twenty satraps (provinces) each governed by a satrap (governor) answerable to the king, connected by the Royal Road (2,700 km from Susa to Sardis) and the Persian postal system (angarium). This infrastructure of roads, messengers, and standardised coinage enabled governance at a continental scale. Darius I standardised weights, measures, and coinage, and began the construction of Persepolis — the ceremonial capital whose ruins remain one of the ancient world's most spectacular monuments.\n\n"
            "The Persian Wars (499–449 BCE) against Greece — Marathon, Thermopylae, Salamis, Plataea — shaped the Western historical narrative of democracy versus despotism. The dynasty ended when Alexander the Great defeated Darius III at Issus (333 BCE) and Gaugamela (331 BCE) and burned Persepolis — but Alexander adopted Achaemenid administrative structures and court ceremonial, recognising that the Persian imperial system was the most sophisticated governance model of the ancient world."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "First world empire (c. 550–330 BCE); largest empire the ancient world had seen; Cyrus's Cylinder is cited as world's first human rights declaration; the satrapy system pioneered provincial governance; its administrative model influenced Alexander and all subsequent Persian dynasties.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Cyrus II's military genius and diplomatic skill — uniting the Persian and Median tribes, then conquering Lydia and Babylon — created the empire within a decade of his rebellion against the Median king Astyages (550 BCE)",
            "Cyrus's policy of tolerance toward conquered peoples — restoring deported populations, supporting local religious practices, and allowing the Jews to return from Babylonian captivity — created a model of multi-ethnic imperial governance that generated loyalty rather than rebellion",
            "The resource base of the Near East — Mesopotamian agriculture, Lydian gold, Egyptian grain — provided the wealth and manpower that allowed the empire to sustain its continental administration and military"
        ],
        "effects": [
            "The Achaemenid satrapy system — provincial governance by appointed governors connected by roads, postal systems, and standardised administration — pioneered the model of territorial empire that all subsequent empires from Alexander to the Ottomans adapted",
            "Cyrus's liberation of the Jewish exiles from Babylon (539 BCE) and his permission to rebuild the Temple in Jerusalem — recorded in the Hebrew Bible (Ezra-Nehemiah) — fundamentally shaped Jewish theology about exile, return, and the relationship between God and foreign rulers",
            "The Persian Wars (490–479 BCE) — however their outcome is interpreted — produced the Athenian confidence that fuelled the classical period's cultural explosion, and created the 'East vs. West' civilisational narrative that has structured Western historical consciousness",
            "Alexander's adoption of Achaemenid administrative structures, court ceremonial, and dress after Gaugamela established the Persian imperial model as the universal template for Hellenistic kingship — transmitting it to Rome, Byzantium, and the Islamic caliphates"
        ],
        "relationships": [
            {"entity": "Cyrus the Great", "relationship": "FOUNDED_BY", "note": "Cyrus II founded the Achaemenid Empire (c. 550 BCE) through the conquest of Media, Lydia, and Babylon"},
            {"entity": "Cyrus Cylinder", "relationship": "ISSUED", "note": "Cyrus issued the Cylinder after conquering Babylon — proclaiming freedom of religion and protecting deported peoples, cited as the world's first human rights declaration"},
            {"entity": "Darius I", "relationship": "ADMINISTRATIVE_SYSTEM_COMPLETED_BY", "note": "Darius I systematised the satrapy administration, standardised coinage, and built the Royal Road — completing the Achaemenid governance revolution"},
            {"entity": "Alexander the Great", "relationship": "CONQUERED_AND_ADMINISTRATION_ADOPTED_BY", "note": "Alexander defeated Darius III (333–331 BCE) and burned Persepolis but adopted Achaemenid administrative structures — the highest tribute to the system's sophistication"},
            {"entity": "Battle of Marathon (490 BCE)", "relationship": "PERSIAN_FORCE_DEFEATED_AT", "note": "The Persian defeat at Marathon (490 BCE) was the Achaemenid Empire's first major setback — beginning the Persian Wars that shaped Western historical consciousness"}
        ],
    }),

    ("argead-dynasty", {
        "summary": (
            "The Argead dynasty was the royal house of ancient Macedon that produced Philip II and Alexander the Great — the two rulers who transformed Macedonia from a peripheral Greek kingdom into the centre of the largest empire the Western world had yet seen. Tracing their lineage from Argos in the Peloponnese (hence 'Argead'), the dynasty had ruled Macedon since approximately the 7th century BCE, but remained a regional power until Philip II's military and administrative reforms (359–336 BCE) transformed the Macedonian army into the most powerful fighting force in the ancient world.\n\n"
            "Philip II's introduction of the Macedonian phalanx — a 16-man-deep infantry formation with 18-foot sarissas — combined with the companion cavalry (hetairoi) and siege technology created the combined-arms system that proved unstoppable at Chaeronea (338 BCE), where Philip defeated the Greek city-states and established Macedonian hegemony. His assassination (336 BCE) brought his 20-year-old son Alexander to the throne, who within thirteen years conquered Persia, Egypt, Central Asia, and northwestern India.\n\n"
            "The Argead dynasty ended with Alexander's death (323 BCE) and the murder of his successors — his posthumous son Alexander IV and half-brother Philip III — in the wars of the Diadochi. But Alexander's conquests created the Hellenistic world: three centuries of Greek-language civilisation from the Mediterranean to the Indus, whose cultural fusion produced the conditions for Christianity, the transmission of Greek philosophy to Rome, and ultimately Western civilisation."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Royal house of Philip II and Alexander the Great; Philip's military reforms created the unstoppable Macedonian phalanx; Alexander's conquests (336–323 BCE) created the Hellenistic world — three centuries of Greek civilisation from the Mediterranean to the Indus that shaped Christianity and Western culture.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Macedonia's marginal position in the Greek world — dismissed as semi-barbarous by Athens and Sparta — created the military necessity that drove Philip II's transformation of a feudal levy into a professional standing army with revolutionary tactical innovations",
            "The Macedonian geography — a fertile plain surrounded by hostile tribes requiring constant military readiness — produced a warrior culture and cavalry tradition that Philip II refined into the hetairoi (companion cavalry), the finest heavy cavalry of the ancient world",
            "Philip II's diplomatic genius — marriages, alliances, bribery, and strategic timing — neutralised potential coalitions until he was ready to strike, creating the political conditions for Alexander's subsequently unobstructed eastern campaign"
        ],
        "effects": [
            "Alexander's conquests (334–323 BCE) spread Greek language, culture, and institutions from Egypt to the Indus Valley — creating the Hellenistic world in which Greek became the lingua franca of the educated classes, enabling the cross-cultural synthesis from which early Christianity and Neoplatonism emerged",
            "The Macedonian phalanx and combined-arms system introduced by Philip II and perfected by Alexander became the template for Hellenistic and subsequently Roman military organisation — shaping warfare across the ancient Mediterranean for three centuries",
            "Alexander's founding of Alexandria (331 BCE) — and the dozens of cities he named after himself — created an urban network that anchored Hellenistic civilisation across the Near East, with Alexandria becoming the greatest city of the ancient world and home of the Library",
            "The wars of the Diadochi (successor wars, 323–281 BCE) — fought by Alexander's generals over the Argead inheritance — produced the three Hellenistic kingdoms (Seleucid, Ptolemaic, Antigonid) that shaped the political geography of the ancient world for the following century"
        ],
        "relationships": [
            {"entity": "Philip II of Macedon", "relationship": "PRODUCED", "note": "Philip II (r. 359–336 BCE) transformed Macedonia into a military superpower through the Macedonian phalanx and companion cavalry"},
            {"entity": "Alexander the Great", "relationship": "GREATEST_RULER_OF", "note": "Alexander (r. 336–323 BCE) created the largest empire the Western world had seen — from Greece to northwestern India"},
            {"entity": "Battle of Chaeronea (338 BCE)", "relationship": "ESTABLISHED_GREEK_HEGEMONY_AT", "note": "Philip II's victory at Chaeronea (338 BCE) ended Greek city-state independence and established Macedonian hegemony over Greece"},
            {"entity": "Hellenistic world", "relationship": "CREATED_BY_CONQUESTS_OF", "note": "Alexander's conquests created the Hellenistic world — three centuries of Greek-language civilisation from the Mediterranean to the Indus"},
            {"entity": "Alexandria, Egypt", "relationship": "FOUNDED", "note": "Alexander founded Alexandria (331 BCE) — which became the ancient world's greatest city, home of the Library and the Pharos lighthouse"}
        ],
    }),

    ("almohad-caliphate", {
        "summary": (
            "The Almohad Caliphate (Arabic: al-Muwahhidun, 'those who affirm divine unity') was a Berber Muslim empire that ruled North Africa and Al-Andalus (Muslim Iberia) from approximately 1121 to 1269. Founded by Ibn Tumart — a Moroccan scholar who studied in Baghdad and Córdoba and returned with a Berber reform movement emphasising strict monotheism and Islamic law — the Almohads overthrew the Almoravid dynasty, conquered Morocco, and crossed to Iberia to create a trans-Mediterranean empire that at its peak controlled territory from the Atlantic to Tripolitania.\n\n"
            "The Almohad court in Marrakesh and Seville was a centre of Islamic philosophy: Ibn Rushd (Averroes) — whose commentaries on Aristotle transformed medieval European philosophy — and Ibn Tufayl were Almohad court philosophers. Maimonides, the greatest medieval Jewish philosopher, grew up under Almohad rule (and fled its intolerance). The Almohad synthesis of Berber military power, Maliki legal tradition, and rational philosophy created one of the medieval world's most intellectually productive environments.\n\n"
            "The Almohad defeat at Las Navas de Tolosa (1212) — a joint Castilian-Aragonese-Portuguese-Navarrese crusading army — began the Reconquista's decisive phase, leading to the fall of Córdoba (1236) and Seville (1248) and reducing Muslim Iberia to the Emirate of Granada. The Almohad collapse in North Africa by 1269 ended the last Berber universal caliphate."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Berber Muslim empire ruling North Africa and Al-Andalus (1121–1269); court philosophers included Averroes (Ibn Rushd), whose Aristotle commentaries transformed European scholasticism; defeat at Las Navas de Tolosa (1212) triggered the decisive Reconquista phase.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Ibn Tumart's reform movement — emphasising strict monotheism (tawhid) and condemning the Almoravids' Maliki legalism as idolatrous — created the ideological framework that mobilised the Atlas Berber tribes against the established dynasty",
            "The Almoravid dynasty's military weakness after decades of campaigning — combined with the fiscal pressures of maintaining both a North African empire and Al-Andalus — created the military opportunity for the Almohad mountain tribes to advance",
            "The prestige of Baghdad Islamic scholarship — which Ibn Tumart had absorbed during his studies — gave his movement the intellectual credentials to claim that only the Almohads were truly upholding Islam, delegitimising the Almoravids"
        ],
        "effects": [
            "Averroes (Ibn Rushd, 1126–1198) — the greatest Almohad court philosopher — produced the commentaries on Aristotle that, translated into Latin, provided medieval European scholars with their primary access to Aristotelian philosophy, triggering the 12th-century Renaissance and influencing Thomas Aquinas",
            "The defeat at Las Navas de Tolosa (1212) shattered Almohad military dominance in Iberia and opened the Reconquista's decisive phase — leading to the fall of Córdoba (1236), Jaén (1246), and Seville (1248) and reducing Muslim Iberia to the Kingdom of Granada",
            "The Almohad persecution of Jews and Christians — forcing conversion or exile — produced the Jewish diaspora from Al-Andalus that carried Iberian Jewish culture (including Maimonides' family) to the Maghreb, Egypt, and the Ottoman Empire",
            "The Almohad political fragmentation into successor dynasties (Hafsids, Zayyanids, Marinids) shaped North Africa's political geography for the following three centuries and established the regional patterns that would confront the Ottoman Empire"
        ],
        "relationships": [
            {"entity": "Ibn Tumart", "relationship": "FOUNDED_BY", "note": "Ibn Tumart founded the Almohad movement in the Atlas Mountains — mobilising Berber tribes against the Almoravids"},
            {"entity": "Ibn Rushd (Averroes)", "relationship": "COURT_PHILOSOPHER_OF", "note": "Averroes served as Almohad court philosopher — producing the Aristotle commentaries that transformed medieval European philosophy"},
            {"entity": "Battle of Las Navas de Tolosa (1212)", "relationship": "DECISIVE_MILITARY_DEFEAT_AT", "note": "The Almohad defeat at Las Navas de Tolosa (1212) began the decisive Reconquista phase that ended Muslim rule over most of Iberia"},
            {"entity": "Maimonides", "relationship": "GREW_UP_UNDER_RULE_OF", "note": "Maimonides grew up in Almohad Córdoba — his family fleeing forced conversion to settle in Egypt, where he wrote the Guide for the Perplexed"},
            {"entity": "Reconquista", "relationship": "DEFEAT_ACCELERATED", "note": "The Almohad collapse after Las Navas de Tolosa (1212) accelerated the Reconquista — leading to the fall of Córdoba (1236) and Seville (1248)"}
        ],
    }),

    ("ahom-dynasty", {
        "summary": (
            "The Ahom kingdom (1228–1826) was a Southeast Asian-origin monarchy that ruled the Brahmaputra Valley (modern Assam) for nearly six centuries — making it one of the longest-lasting dynasties in South Asian history. Founded by Sukaphaa, a Shan prince from what is now Myanmar who crossed the Patkai mountains in 1228, the Ahom kingdom successfully resisted Mughal expansion for over a century — repelling seventeen Mughal military expeditions and defeating the Mughals at the Battle of Saraighat (1671) under General Lachit Borphukan, one of the most celebrated military victories in Indian history.\n\n"
            "The Ahom administrative system — the paik system, which assigned labour obligations to households rather than taxing income — was remarkably efficient for revenue collection and public works, enabling the construction of extensive dykes, irrigation networks, and public granaries across the Brahmaputra Valley. The Ahom kings adopted Hinduism while preserving their own religious traditions, creating a syncretic court culture that combined Shan, Assamese, and Hindu elements.\n\n"
            "The kingdom was weakened by the Moamoria Rebellion (1769–1805) and finally conquered by the Burmese (1817–1819) before becoming part of British India by the Treaty of Yandabo (1826). The Ahom legacy — particularly the Battle of Saraighat — is central to Assamese national identity: Lachit Borphukan's statue stands in Assam's capital and the battle date is Assam's Heroes' Day."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Southeast Asian-origin dynasty that ruled Assam for 600 years (1228–1826); repelled 17 Mughal expeditions; the Battle of Saraighat (1671) under Lachit Borphukan was one of the most celebrated military victories in Indian history; the Ahom legacy is central to Assamese national identity.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Sukaphaa's migration from the Shan plateau with 9,000 followers (1228) brought a disciplined, hierarchically organised military force that could dominate the politically fragmented chieftaincies of the Brahmaputra Valley",
            "The Brahmaputra Valley's geographic isolation — surrounded by mountains, jungle, and the great river — made it difficult to conquer but also limited Ahom expansion, creating a stable polity focused on intensive development of its core territory",
            "The Ahom paik labour system — assigning military and public works obligations to households — provided efficient mobilisation of manpower for both warfare and agricultural infrastructure without requiring the cash taxation that burdened most South Asian kingdoms"
        ],
        "effects": [
            "The Ahom's 17-time repulsion of Mughal invasions demonstrated that the Mughal Empire's northeastern expansion had its limits — preserving the Brahmaputra Valley's distinct ethnic, cultural, and religious character separate from the Mughal cultural sphere",
            "The Battle of Saraighat (1671) under Lachit Borphukan — using river warfare, tactical brilliance, and familiarity with the Brahmaputra's geography to defeat a much larger Mughal naval force — is celebrated as India's greatest river battle and remains central to Assamese identity",
            "The Ahom kingdom's 600-year administration produced a distinctive Assamese culture — a synthesis of Shan, indigenous Tibeto-Burman, and Hindu elements — that survived the kingdom's fall and provides the cultural foundation of modern Assamese identity",
            "The Treaty of Yandabo (1826) — by which Assam was ceded to the British East India Company after the First Anglo-Burmese War — incorporated Ahom territories into British India, eventually making Assam a critical tea-producing province"
        ],
        "relationships": [
            {"entity": "Sukaphaa", "relationship": "FOUNDED_BY", "note": "Sukaphaa crossed the Patkai mountains in 1228 to found the Ahom kingdom in the Brahmaputra Valley"},
            {"entity": "Battle of Saraighat (1671)", "relationship": "DEFENDED_KINGDOM_AT", "note": "General Lachit Borphukan's victory at Saraighat (1671) repelled the Mughal naval invasion — celebrated as India's greatest river battle"},
            {"entity": "Mughal Empire", "relationship": "REPELLED_17_INVASIONS_OF", "note": "The Ahom kingdom successfully repelled seventeen Mughal military expeditions over more than a century — one of the most sustained defences against Mughal expansion"},
            {"entity": "British East India Company", "relationship": "TERRITORY_ABSORBED_BY", "note": "Ahom territories were absorbed into British India by the Treaty of Yandabo (1826) after the First Anglo-Burmese War"},
            {"entity": "Assamese culture and identity", "relationship": "CULTURAL_FOUNDATION_OF", "note": "The 600-year Ahom kingdom created the distinctive Assamese cultural synthesis that underlies modern Assamese national identity"}
        ],
    }),

    ("ajuran-empire", {
        "summary": (
            "The Ajuran Sultanate (c. 1200–1700 CE) was a Somali Muslim state that ruled much of the Horn of Africa from its centre in the Jubba and Shabelle river valleys. At its peak (c. 1300–1600 CE), the Ajuran controlled a vast territory encompassing modern southern Somalia, the Ogaden region of Ethiopia, and parts of northeastern Kenya — making it one of the most powerful polities in the Indian Ocean world. The sultanate's prosperity was built on hydraulic engineering: the Ajuran constructed stone wells, cisterns, and underground irrigation systems whose ruins remain visible and functional in southern Somalia.\n\n"
            "The Ajuran successfully resisted Portuguese colonisation attempts in the early 16th century — a period when Portugal was establishing trading posts along the East African coast — and repelled Ottoman-supported Oromo migrations that threatened the state's core territories. The Ajuran's international trade connections — documented by Arab, Chinese, and Portuguese sources — included spices, ivory, livestock, and gold reaching the Persian Gulf, India, and China via the Indian Ocean trade network.\n\n"
            "The Ajuran Sultanate fragmented in the late 17th century as a result of clan rebellions and the rise of successor sultanates (the Geledi, Hobyo, and Majeerteen sultanates). Its legacy — particularly its hydraulic engineering and its successful resistance to Portuguese expansion — is a source of pride in Somali historiography and has influenced postcolonial Somali national identity."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Somali Muslim sultanate that ruled the Horn of Africa (c. 1200–1700); built stone wells and irrigation systems still visible today; resisted Portuguese colonisation; connected to Indian Ocean trade reaching Persia, India, and China; its resistance to colonialism is central to Somali historical pride.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Islam's introduction to the Somali coast through Indian Ocean trade routes (7th–10th centuries) provided the ideological cohesion and trade networks that enabled the Ajuran clans to build a politically unified sultanate",
            "The Jubba and Shabelle river valleys' agricultural productivity — rare in the arid Horn of Africa — provided the food surplus that sustained the Ajuran's urban centres and military, and the Ajuran's hydraulic engineering expertise maximised this advantage",
            "The Indian Ocean trade boom (12th–16th centuries) — connecting East Africa to the Persian Gulf, India, and China — generated the commercial wealth that financed the Ajuran state and made its ports strategically valuable"
        ],
        "effects": [
            "The Ajuran's stone well and cistern network — some still functional after 700 years — transformed the carrying capacity of southern Somalia's semi-arid interior, enabling permanent settlement and grazing patterns that persist to the present",
            "The Ajuran's resistance to Portuguese expansion in the early 16th century preserved the Horn of Africa's Islamic trade networks from Portuguese disruption — maintaining the Indian Ocean trade routes that sustained East African coastal civilisation",
            "The Ajuran Sultanate's legacy shaped the political geography of the successor sultanates — the Geledi, Hobyo, and Majeerteen — that governed the Somali coast until colonial partition in the late 19th century",
            "The Ajuran's documented trade connections (Arab, Chinese, and Portuguese sources) provide the primary historical evidence for medieval Somali civilisation's international integration — countering colonial-era narratives of Somali isolation"
        ],
        "relationships": [
            {"entity": "Indian Ocean trade network", "relationship": "CONNECTED_TO", "note": "The Ajuran was integrated into the Indian Ocean trade network — exporting livestock, ivory, and gold to the Persian Gulf, India, and China"},
            {"entity": "Portuguese Empire", "relationship": "RESISTED_COLONIAL_EXPANSION_OF", "note": "The Ajuran successfully resisted Portuguese colonisation attempts in the early 16th century — preserving the Horn of Africa's Islamic trade networks"},
            {"entity": "Horn of Africa", "relationship": "DOMINANT_POWER_OF", "note": "At its peak (c. 1300–1600), the Ajuran was the dominant power of the Horn of Africa — controlling modern southern Somalia, Ogaden, and parts of Kenya"},
            {"entity": "Somali national identity", "relationship": "HISTORICAL_FOUNDATION_FOR", "note": "The Ajuran's hydraulic engineering legacy and resistance to colonialism are central to Somali historical pride and postcolonial national identity"},
            {"entity": "Geledi Sultanate", "relationship": "SUCCEEDED_BY", "note": "The Geledi Sultanate was one of the successor states that emerged from the Ajuran's 17th-century fragmentation"}
        ],
    }),

    ("aghlabids", {
        "summary": (
            "The Aghlabid dynasty (800–909 CE) was an Arab Muslim dynasty that ruled Ifriqiya (modern Tunisia and eastern Algeria) as nominally autonomous vassals of the Abbasid Caliphate. Founded by Ibrahim ibn al-Aghlab after he secured the Abbasid caliph's recognition in 800 CE, the dynasty made Kairouan (in modern Tunisia) one of the great cities of the Islamic world — a centre of scholarship, architecture, and Maliki legal tradition whose Great Mosque remains one of the most important monuments of early Islamic architecture.\n\n"
            "The Aghlabids' greatest achievement was the conquest of Sicily (827–902 CE) — a century-long campaign that transformed the island into an Emirate of Sicily that became one of the medieval world's most remarkable multicultural societies. Aghlabid Sicily combined Arab, Byzantine, and Norman cultures and transmitted Arab science, mathematics, and agricultural techniques (including citrus cultivation and sophisticated irrigation) to the European West. The Aghlabids also raided the Italian coast, sacking Rome's basilicas (846 CE) in a raid that shocked Christendom.\n\n"
            "The Aghlabid dynasty was overthrown by the Fatimid caliphate (909 CE), whose Ismaili missionaries had undermined its legitimacy. But their century of rule had permanently established Islam in North Africa's agricultural interior and created the Islamic architectural tradition of the Maghreb."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Arab dynasty ruling Ifriqiya (800–909); conquered Sicily (827–902) creating a multicultural emirate that transmitted Arab science to the European West; built Kairouan's Great Mosque; raided Rome (846); created the architectural tradition of the Maghreb.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Ibrahim ibn al-Aghlab's military consolidation of Ifriqiya — ending the cycle of Berber rebellions and Arab tribal conflicts that had plagued the region — and his negotiation of autonomous governance from the Abbasid caliph created stable conditions for the dynasty",
            "The Byzantine weakness in Sicily and southern Italy — demonstrated by the fall of Palermo (831) and Syracuse (878) — made the island vulnerable to systematic Aghlabid conquest over the 9th century",
            "Kairouan's established status as the Islamic capital of North Africa provided the religious legitimacy and intellectual resources that the Aghlabids cultivated to establish their authority"
        ],
        "effects": [
            "Aghlabid Sicily (827–1072) became one of the medieval world's most culturally productive societies — Arab, Byzantine, and Norman cultures producing scientific, literary, and agricultural innovations that transmitted Arab knowledge to Latin Europe",
            "The Arab agricultural revolution introduced to Sicily and southern Italy — citrus, cotton, sugarcane, hard wheat (durum), and sophisticated irrigation — permanently transformed the agriculture of the Mediterranean basin",
            "The Aghlabid sack of Rome's basilicas (846 CE) — though not Rome itself — shocked Latin Christendom and contributed to the construction of the Leonine Wall around the Vatican by Pope Leo IV",
            "The Great Mosque of Kairouan — built by the Aghlabids — became the model for North African mosque architecture and one of the most important surviving monuments of early Islam"
        ],
        "relationships": [
            {"entity": "Abbasid Caliphate", "relationship": "NOMINALLY_VASSAL_TO", "note": "The Aghlabids ruled as nominally autonomous vassals of the Abbasid Caliphate — paying an annual tribute to Baghdad"},
            {"entity": "Emirate of Sicily", "relationship": "ESTABLISHED_THROUGH_CONQUEST", "note": "The Aghlabids conquered Sicily (827–902) and established the Emirate of Sicily — one of the medieval world's most remarkable multicultural societies"},
            {"entity": "Great Mosque of Kairouan", "relationship": "BUILT", "note": "The Aghlabids built the Great Mosque of Kairouan — the model for North African mosque architecture and one of Islam's most important early monuments"},
            {"entity": "Fatimid Caliphate", "relationship": "OVERTHROWN_BY", "note": "The Fatimid caliphate — whose Ismaili missionaries had undermined Aghlabid legitimacy — overthrew the dynasty in 909 CE"},
            {"entity": "Arab agricultural revolution", "relationship": "TRANSMITTED_TO_EUROPE_VIA_SICILY", "note": "The Aghlabids introduced Arab agricultural innovations — citrus, cotton, durum wheat, sophisticated irrigation — to Sicily and thereby to medieval Europe"}
        ],
    }),

    ("adal-sultanate", {
        "summary": (
            "The Adal Sultanate (c. 1415–1577 CE) was a Somali Muslim state based in the Horn of Africa that became the primary Islamic power contesting the Christian Ethiopian Empire for control of the region. At its most powerful under Ahmad ibn Ibrahim al-Ghazi ('Ahmad Grañ', 'Ahmad the Left-Handed'), Adal launched a devastating jihad against the Ethiopian Empire (1529–1543) that came close to destroying the centuries-old Christian kingdom and overturning the entire religious and political order of the Horn of Africa.\n\n"
            "Ahmad Grañ's campaign (1529–1543) — armed with Ottoman firearms and allied with Ottoman support — conquered approximately three-quarters of the Ethiopian Empire, forced Emperor Lebna Dengel to flee, and destroyed numerous ancient churches and monasteries including the Church of Our Lady Mary of Zion in Axum. The Ethiopian Empire was only saved by a Portuguese expeditionary force of 400 musketeers under Christóvão da Gama (son of Vasco da Gama), whose firearms helped defeat and kill Ahmad Grañ at the Battle of Wayna Daga (1543).\n\n"
            "The conflict represented a microcosm of global religious-political struggles: Ottoman firearms and Islamic expansion versus Portuguese-supported Christian monarchy. The Adal Sultanate declined after Ahmad Grañ's death and was eventually destroyed by the Oromo migrations. Its brief conquest of Ethiopia left permanent cultural marks — mosque construction, the destruction of ancient Christian monuments — and the conflict's memory shapes Ethiopian-Somali relations to the present."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Somali Muslim sultanate whose Ahmad Grañ nearly destroyed the Ethiopian Empire (1529–43); Ottoman-armed jihad conquered three-quarters of Ethiopia; the conflict ended only with Portuguese military intervention — making it a proxy of the global Ottoman-Habsburg-Portuguese rivalry.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The conflict between the expanding Muslim sultanates of the Somali coast and the Christian Ethiopian Empire — both competing for control of the trade routes and tributary peoples of the Horn — made armed confrontation strategically inevitable",
            "Ahmad Grañ's military genius and his access to Ottoman firearms — which gave his forces a decisive technological advantage over Ethiopian cavalry — transformed what had been a regional conflict into a near-existential threat to the Ethiopian Empire",
            "The Ethiopian Empire's internal weaknesses — factional conflicts among the nobility, overtaxation of peripheral populations, and the challenge of governing a vast highland empire with limited communications — created the vulnerability that Ahmad Grañ exploited"
        ],
        "effects": [
            "Ahmad Grañ's conquest of three-quarters of Ethiopia (1529–1543) destroyed hundreds of ancient churches and monasteries — including irreplaceable manuscripts, relics, and the oldest Christian monuments in sub-Saharan Africa — a cultural catastrophe that permanently altered Ethiopia's religious landscape",
            "The Portuguese military intervention (1541–1543) — 400 musketeers under Christóvão da Gama — was decisive in defeating Ahmad Grañ at Wayna Daga (1543), establishing a precedent of European military involvement in African affairs that prefigured the colonial era",
            "The 16-year conflict depopulated large areas of highland Ethiopia and shattered the political structures of the Ethiopian Empire — requiring a century of reconstruction and permanently altering Ethiopia's ethnic and religious demography through Oromo migrations",
            "The conflict embedded a permanent memory of Islamic-Christian confrontation in both Ethiopian and Somali identity — shaping religious and ethnic tensions in the Horn of Africa that persist to the present, including the Ogaden conflicts"
        ],
        "relationships": [
            {"entity": "Ahmad ibn Ibrahim al-Ghazi (Ahmad Grañ)", "relationship": "GREATEST_MILITARY_LEADER_OF", "note": "Ahmad Grañ's jihad (1529–43) conquered three-quarters of the Ethiopian Empire — the sultanate's most consequential military campaign"},
            {"entity": "Ethiopian Empire", "relationship": "MILITARILY_DEVASTATED", "note": "The Adal Sultanate under Ahmad Grañ conquered three-quarters of Ethiopia (1529–43), nearly destroying the ancient Christian kingdom"},
            {"entity": "Ottoman Empire", "relationship": "ARMED_AND_SUPPORTED_BY", "note": "The Ottomans provided firearms and support to Adal — making the conflict a proxy of the global Ottoman-Portuguese rivalry"},
            {"entity": "Portugal", "relationship": "MILITARY_INTERVENTION_AGAINST_BY", "note": "A Portuguese expeditionary force (400 musketeers) under Christóvão da Gama helped defeat and kill Ahmad Grañ at Wayna Daga (1543)"},
            {"entity": "Battle of Wayna Daga (1543)", "relationship": "DECISIVE_DEFEAT_AT", "note": "Ahmad Grañ's death at Wayna Daga (1543) ended Adal's conquests and began the sultanate's decline"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 04 — {len(ENTITIES)} entities (Class 312: Islamic & Ancient Dynasties)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
