#!/usr/bin/env python3
"""
Batch 05 — 8 entities (Class 312): Abbasid Caliphate variants, Abbadid Dynasty,
Abgarid Dynasty, Abydos Dynasty, Afsharid Dynasty, Aghlabids (Indonesia region),
Al-Bu Said Dynasty, Alawi Dynasty
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

    ("abbadid-dynasty", {
        "summary": (
            "The Abbadid dynasty (1023–1091 CE) was an Arab Muslim ruling house of Seville (Ishbiliya) that emerged during the Taifa period — the fragmentation of the Umayyad Caliphate of Córdoba into competing petty kingdoms after its collapse in 1031. Under three rulers — Abu al-Qasim, Abbad al-Mu'tadid, and the celebrated Al-Mu'tamid ibn Abbad — the Abbadids made Seville the cultural and political capital of the most powerful Taifa kingdom, rivalling Córdoba in its literary and intellectual life.\n\n"
            "Al-Mu'tamid ibn Abbad (r. 1069–1091) was the greatest Abbadid ruler — a poet-king celebrated for his verses, his tragic fate, and his cultural patronage. His court attracted the finest poets, philosophers, and musicians of Islamic Iberia. Al-Mu'tamid ruled Seville at a time of increasing Christian military pressure from the north (Alfonso VI of Castile captured Toledo in 1085), and made the fateful decision to invite the Almoravid dynasty from North Africa to resist the Christian advance.\n\n"
            "The Almoravids defeated Alfonso VI at the Battle of Sagrajas (1086) but subsequently absorbed the Taifa kingdoms they had been invited to defend: Al-Mu'tamid was deposed in 1091 and exiled to Morocco, where he composed his most poignant verses in prison. His story — a poet-king who traded political freedom for military salvation, then lost both — became one of the most romantic narratives of Andalusian history."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Arab Taifa dynasty of Seville (1023–1091); Al-Mu'tamid was the greatest poet-king of Islamic Iberia; invited the Almoravids to resist Christian reconquest — only to be deposed by them; his tragic fate became one of the most celebrated narratives of Andalusian history.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The collapse of the Umayyad Caliphate of Córdoba (1031) into the Taifa ('party kings') period created the political vacuum that allowed the Abbadid family — originally judges of Seville — to seize power and establish a regional dynasty",
            "Seville's strategic position as the gateway between the Guadalquivir Valley and the Atlantic, combined with its agricultural wealth and existing urban infrastructure, made it the natural base for the most powerful Taifa kingdom",
            "The Christian kingdoms' military pressure from the north — culminating in Alfonso VI's capture of Toledo (1085) — created the existential threat that forced Al-Mu'tamid to invite the Almoravids, despite knowing the risk of losing his own independence"
        ],
        "effects": [
            "Al-Mu'tamid's invitation of the Almoravids (1086) was a pivotal moment in Iberian history: the Almoravid victory at Sagrajas temporarily halted the Reconquista but ultimately delivered the Taifa kingdoms into Almoravid control, ending the Taifa period",
            "Al-Mu'tamid's poems — composed in prison in Aghmat, Morocco — became among the most celebrated works of classical Arabic literature, establishing the romantic narrative of the exiled poet-king that influenced Arabic and Spanish literary traditions",
            "The Abbadid court's cultural florescence under Al-Mu'tamid — attracting Ibn Hazm, Ibn Zaydun, and other major poets — represented the apex of Taifa cultural achievement and the last flowering of independent Andalusian literary culture before Almoravid puritanism",
            "Al-Mu'tamid's famous choice — 'I would rather be a camel-driver in Africa than a swineherd in Castile' — when faced with the choice between Almoravid and Christian suzerainty became one of the most quoted statements of medieval Islamic political identity"
        ],
        "relationships": [
            {"entity": "Al-Mu'tamid ibn Abbad", "relationship": "GREATEST_RULER_OF", "note": "Al-Mu'tamid (r. 1069–1091) was the poet-king who made Seville the cultural apex of Islamic Iberia — and whose tragic exile is the dynasty's defining narrative"},
            {"entity": "Almoravid dynasty", "relationship": "INVITED_AND_THEN_DEPOSED_BY", "note": "Al-Mu'tamid invited the Almoravids (1086) to resist Alfonso VI — only to be deposed by them in 1091 and exiled to Morocco"},
            {"entity": "Taifa period", "relationship": "MOST_POWERFUL_KINGDOM_DURING", "note": "The Abbadid Seville was the most powerful Taifa kingdom — making the Abbadids the dominant force during the Taifa period"},
            {"entity": "Battle of Sagrajas (1086)", "relationship": "ALMORAVID_VICTORY_REQUESTED_BY", "note": "Al-Mu'tamid's invitation of the Almoravids led to the Battle of Sagrajas (1086) — temporarily halting the Reconquista"},
            {"entity": "Classical Arabic poetry", "relationship": "ADVANCED_BY_COURT_OF", "note": "Al-Mu'tamid's court attracted the finest poets of Islamic Iberia, producing a literary legacy that ranks among the highest achievements of classical Arabic poetry"}
        ],
    }),

    ("abgarid-dynasty", {
        "summary": (
            "The Abgarid dynasty (c. 132 BCE – 244 CE) was the ruling house of Osroene, a small buffer kingdom centred on Edessa (modern Şanlıurfa in southeastern Turkey) strategically positioned between the Roman and Parthian/Sassanid empires. For nearly four centuries the Abgarids navigated the treacherous politics of the great power rivalry — sometimes allied with Rome, sometimes with Parthia — maintaining their independence through diplomatic flexibility and the exploitation of their position as a commercial and cultural crossroads on the Silk Road.\n\n"
            "The Abgarids hold a unique place in Christian history: the tradition that Abgar V 'the Black' (r. c. 4 BCE–50 CE) exchanged letters with Jesus of Nazareth — preserved in Eusebius's Ecclesiastical History — made Edessa's claim to be the first Christian kingdom a powerful element of early Christian historiography. Though the correspondence is generally regarded as apocryphal, the Abgarid court's apparent early adoption of Christianity (by Abgar VIII or IX, c. 179–216 CE) may have made Osroene the first state with an officially Christian ruling dynasty — a claim that Eusebius and subsequent church historians took seriously.\n\n"
            "The dynasty ended when Emperor Caracalla of Rome arrested and executed Abgar IX during a visit to Rome (212 CE) and subsequently annexed Osroene as a direct Roman province (244 CE), ending the region's quasi-independence. Edessa subsequently became a major centre of Syriac Christianity and a city of enormous theological significance."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Ruling dynasty of Osroene/Edessa (c. 132 BCE–244 CE); the alleged correspondence of Abgar V with Jesus made Edessa's claim to be the first Christian kingdom historically significant; Abgar VIII may have been the first ruler with an officially Christian court; a buffer dynasty between Rome and Parthia for four centuries.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The collapse of the Seleucid Empire in the 2nd century BCE created the political vacuum that allowed the Abgarid family — of Arab-Aramaic origin — to establish control over Edessa and the surrounding region",
            "Edessa's geographic position on the main commercial route between the Mediterranean and Mesopotamia — and between the Roman and Parthian frontiers — made the city strategically valuable, giving the Abgarids diplomatic leverage with both great powers",
            "The region's mixed Aramaic, Greek, Arab, and later Christian culture created a cosmopolitan urban environment that made Edessa a natural centre of religious exchange — facilitating the adoption and development of early Christianity"
        ],
        "effects": [
            "The Abgar-Jesus correspondence tradition — whether historical or not — established Edessa's claim as the first Christian city and shaped the development of early Syriac Christianity, making Edessa a major centre of Christian theology and literature for the following centuries",
            "Edessa under and after the Abgarids became the cradle of Syriac Christianity — the tradition that produced the Peshitta (the Syriac Bible), the theologian Ephrem the Syrian, and the intellectual tradition that transmitted Greek philosophy to the Islamic world",
            "The Abgarids' ability to maintain independence as a buffer state between Rome and Parthia for nearly four centuries demonstrated that small states at the intersection of great power rivalries could survive through diplomatic skill, commercial wealth, and strategic ambiguity",
            "Caracalla's annexation of Osroene (c. 212–244 CE) eliminated the last independent buffer state between Rome and Parthia/Sassanid Persia, contributing to the increased direct confrontation between the empires that characterised the 3rd-century crisis"
        ],
        "relationships": [
            {"entity": "Abgar V of Osroene", "relationship": "MOST_FAMOUS_RULER_OF", "note": "Abgar V 'the Black' is the most historically noted Abgarid ruler due to the tradition of his correspondence with Jesus — preserved in Eusebius"},
            {"entity": "Roman Empire", "relationship": "NAVIGATED_RELATIONSHIP_WITH", "note": "The Abgarids maintained their independence by balancing between Rome and Parthia — until Caracalla annexed Osroene (c. 244 CE)"},
            {"entity": "Parthian Empire", "relationship": "NAVIGATED_RELATIONSHIP_WITH", "note": "The Abgarids alternated between Roman and Parthian alliance — exploiting great power rivalry to maintain buffer state independence"},
            {"entity": "Syriac Christianity", "relationship": "EARLIEST_OFFICIAL_PATRON_OF", "note": "Abgar VIII or IX may have adopted Christianity as an official court religion — making Osroene possibly the first state with a Christian ruling dynasty"},
            {"entity": "Edessa", "relationship": "CAPITAL_OF", "note": "Edessa (modern Şanlıurfa) was the Abgarid capital — a Silk Road crossroads that became one of early Christianity's most important intellectual centres"}
        ],
    }),

    ("abydos-dynasty", {
        "summary": (
            "The Abydos Dynasty was a minor ancient Egyptian royal house that briefly challenged the Hyksos occupation of Lower Egypt during the Second Intermediate Period (c. 1650–1550 BCE). Named after Abydos, the sacred city of Osiris in Upper Egypt where its inscriptions were found, the dynasty is known from only a handful of cartouches and scarabs — making it one of the most obscure and debated topics in Egyptology. Contemporary with the 17th Dynasty of Thebes and the Hyksos 15th Dynasty, it appears to have controlled a small territory in the Abydos-Thinis region of Middle Egypt.\n\n"
            "The Abydos Dynasty is significant primarily as evidence of the extreme political fragmentation of Egypt during the Second Intermediate Period — when the country was divided between the Hyksos (Lower Egypt), Theban Egyptians (Upper Egypt), and Nubian Kerma kingdom (southernmost Egypt/northern Sudan), with minor dynasties in between. The Theban 17th Dynasty under Seqenenre Tao, Kamose, and Ahmose I eventually reunified Egypt by expelling the Hyksos (c. 1550 BCE), beginning the New Kingdom.\n\n"
            "The Abydos Dynasty's obscurity — it may have been a local power acknowledging Hyksos overlordship, or a minor independent house — illustrates how limited our knowledge of Egyptian history becomes when inscriptional evidence is sparse. Its identification as a distinct dynasty (rather than a variant of the 17th) has been debated since the 1980s."
        ),
        "importanceScore": 4,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Minor ancient Egyptian dynasty of the Second Intermediate Period; evidence of Egypt's extreme political fragmentation c. 1650–1580 BCE; known from only a handful of cartouches; its existence illustrates the limits of Egyptian historical knowledge in the Hyksos period.",
            "significanceCategory": "local"
        },
        "causes": [
            "The Hyksos conquest of Lower Egypt (c. 1650 BCE) and the collapse of Middle Kingdom central authority created the political vacuum in which minor regional dynasties could assert local power — including the obscure Abydos Dynasty in the Abydos-Thinis region",
            "Abydos's status as Egypt's most sacred city — home of the Osiris cult and the royal necropolis — gave local rulers religious prestige that could justify political claims independent of military strength",
            "The extreme political fragmentation of the Second Intermediate Period, with Egypt divided among at least four distinct powers, created the conditions in which local rulers could briefly assert dynastic authority in the gaps between the major powers"
        ],
        "effects": [
            "The Abydos Dynasty's existence provides evidence for the extreme political fragmentation of Egypt during the Second Intermediate Period — a phase of weakness that the New Kingdom pharaohs would reference to justify their empire-building campaigns",
            "The Theban 17th Dynasty's eventual unification — absorbing or eliminating the Abydos Dynasty and expelling the Hyksos — established the New Kingdom political framework that produced the most powerful period of Egyptian imperial history",
            "The Abydos Dynasty's scarabs and inscriptions contribute to Egyptological knowledge of administrative and royal titulary during the Second Intermediate Period, providing evidence for continuities and breaks in Egyptian royal traditions",
            "The debate about the Abydos Dynasty's classification illustrates the challenges of ancient history when textual evidence is sparse — a methodological reference point in discussions of Egyptian dynastic historiography"
        ],
        "relationships": [
            {"entity": "Hyksos (15th Dynasty)", "relationship": "CONTEMPORARY_WITH_AND_POSSIBLY_SUBORDINATE_TO", "note": "The Abydos Dynasty may have been a minor power acknowledging Hyksos overlordship — operating in the space between Hyksos Lower Egypt and Theban Upper Egypt"},
            {"entity": "17th Dynasty of Thebes", "relationship": "CONTEMPORARY_WITH", "note": "The Abydos Dynasty was contemporary with the Theban 17th Dynasty that ultimately unified Egypt and expelled the Hyksos"},
            {"entity": "Second Intermediate Period", "relationship": "PRODUCT_OF_FRAGMENTATION_OF", "note": "The Abydos Dynasty emerged from the extreme political fragmentation of Egypt's Second Intermediate Period"},
            {"entity": "Abydos", "relationship": "CENTRED_ON", "note": "The dynasty is named after and centred on Abydos — Egypt's most sacred city as the site of the Osiris cult and royal necropolis"},
            {"entity": "New Kingdom Egypt", "relationship": "ABSORBED_INTO", "note": "Egypt's reunification under Ahmose I (c. 1550 BCE) absorbed the Abydos Dynasty into the New Kingdom — the most powerful period of Egyptian imperial history"}
        ],
    }),

    ("afsharid-dynasty", {
        "summary": (
            "The Afsharid dynasty (1736–1796) was a short-lived but militarily spectacular Iranian dynasty founded by Nader Shah — one of history's greatest military commanders — who rose from a slave and tribal leader to become the ruler of an empire stretching from the Caucasus to northern India. Nader Shah deposed the last Safavid shah in 1736 and proclaimed himself Shah of Iran, then embarked on a campaign of military expansion that included the sack of Delhi (1739), where he looted the treasures of the Mughal Empire — including the Peacock Throne and the Koh-i-Noor diamond — transferring a vast proportion of the Mughal Empire's accumulated wealth to Iran.\n\n"
            "Nader Shah's military genius lay in combined arms tactics, rapid strategic movement, and the use of siege artillery — techniques he used to defeat the Ottomans, Mughals, Russians, and Afghan tribes in succession. His army was arguably the most effective military force between the Ottoman siege of Vienna (1683) and Napoleon's campaigns. His sack of Delhi (March 1739) — killing approximately 20,000–30,000 of Delhi's inhabitants in a single day of massacres — was one of the 18th century's most traumatic events and effectively ended Mughal imperial power.\n\n"
            "Nader Shah's assassination (1747) — by his own commanders, fearful of his increasing paranoia and brutality — ended the dynasty's brief brilliance. His successors contested Iran's fragments until Ahmad Shah Durrani (himself a former commander of Nader Shah) established the Durrani Empire in Afghanistan, one of the lasting geopolitical consequences of the Afsharid era."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Iranian dynasty (1736–96) founded by Nader Shah — one of history's greatest commanders; sacked Delhi (1739) looting the Peacock Throne and Koh-i-Noor; effectively ended Mughal imperial power; his assassination (1747) triggered the creation of the Durrani Empire (Afghanistan).",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Safavid dynasty's collapse under Afghan invasions (1722) created the power vacuum that a military genius like Nader Shah — rising from Khorasan tribal origins — could exploit to seize control of Iran's leaderless armies",
            "The Afghan (Hotaki) occupation of Isfahan (1722–1729) and the chaos of multiple competing claimants gave Nader Shah both the pretext and the opportunity to present himself as Iran's liberator — gathering military support across the country",
            "Nader Shah's tactical innovations — using Afghani cavalry alongside Iranian infantry and incorporating European-style siege artillery — gave him military superiority over every opponent he faced, enabling the rapid conquests that defined his reign"
        ],
        "effects": [
            "The sack of Delhi (1739) transferred an estimated 700 million rupees in treasure from the Mughal treasury to Iran — including the Peacock Throne, the Koh-i-Noor diamond, and the Darya-ye Noor — and delivered a blow to Mughal prestige from which the empire never recovered",
            "Nader Shah's campaigns against the Ottomans forced the Treaty of Küçük Kaynarca's predecessor agreements and demonstrated that the Ottoman Empire was militarily vulnerable — contributing to the 18th-century consciousness of Ottoman decline",
            "Ahmad Shah Durrani — one of Nader Shah's commanders who used the chaos following his assassination to found the Durrani Empire (1747) — created Afghanistan as a modern state, a direct geopolitical consequence of the Afsharid era",
            "The Afsharid period's destruction of political stability across Iran and the Caucasus created the conditions for subsequent Russian and British imperial expansion — the 'Great Game' of the 19th century was partly a consequence of the power vacuum the Afsharids failed to fill permanently"
        ],
        "relationships": [
            {"entity": "Nader Shah", "relationship": "FOUNDED_BY", "note": "Nader Shah founded the Afsharid dynasty (1736) after deposing the last Safavid — and built it through spectacular military conquests"},
            {"entity": "Sack of Delhi (1739)", "relationship": "CONDUCTED", "note": "Nader Shah sacked Delhi (1739) — looting the Mughal treasury including the Peacock Throne and Koh-i-Noor diamond, transferring vast wealth to Iran"},
            {"entity": "Mughal Empire", "relationship": "FATALLY_WEAKENED_BY_INVASION_OF", "note": "Nader Shah's 1739 invasion and looting effectively ended Mughal imperial power — the empire never recovered its prestige or finances"},
            {"entity": "Ahmad Shah Durrani", "relationship": "FORMER_COMMANDER_WHO_FOUNDED_DURRANI_EMPIRE", "note": "Ahmad Shah Durrani — Nader Shah's former commander — used the chaos after Nader's assassination (1747) to found the Durrani Empire (Afghanistan)"},
            {"entity": "Koh-i-Noor diamond", "relationship": "LOOTED_FROM_MUGHAL_TREASURY", "note": "Nader Shah seized the Koh-i-Noor from the Mughal treasury in 1739 — beginning the diamond's journey through the Durrani, Sikh, and British empires to the present Crown Jewels"}
        ],
    }),

    ("al-bu-said-dynasty", {
        "summary": (
            "The Al Bu Said dynasty (1744–present) is the ruling house of Oman — the longest-reigning dynasty in the Arabian Peninsula and one of the oldest continuously ruling houses in the Islamic world. Founded by Ahmad ibn Said Al-Said after he expelled the Persian Afsharid occupation from Muscat and was elected imam (spiritual and temporal leader) by Omani tribal leaders in 1744, the dynasty has governed Oman for 280 years through its various political forms: the Imamate, the Sultanate, and the modern state.\n\n"
            "The Al Bu Said's most significant historical period was the 19th-century Omani maritime empire under Sultan Said bin Sultan (r. 1806–1856), who built Oman into the dominant commercial power of the western Indian Ocean — controlling the Zanzibar slave trade, the spice islands of the East African coast, ports in what is now Pakistan, and significant commercial interests in India. Said moved his court to Zanzibar (1840) and the empire he built was so extensive that after his death it was divided between his sons: one ruling Oman, one ruling Zanzibar — creating two distinct branches.\n\n"
            "The modern Sultanate under Qaboos bin Said (r. 1970–2020) was transformed from a medieval state into a modern country through oil revenues and Qaboos's personal vision. Oman under Qaboos developed a distinctive foreign policy of neutrality and mediation — maintaining relations with both Iran and Saudi Arabia, facilitating the Iran nuclear deal negotiations (2013), and serving as a backchannel between the US and Iran."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Ruling dynasty of Oman since 1744; built the 19th-century Omani maritime empire controlling the western Indian Ocean and East African coast; Sultan Qaboos (1970–2020) modernised Oman and created its distinctive neutral mediation foreign policy.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Persian Afsharid occupation of Muscat (1737–1744) and its exploitation of Omani commerce and trade created the political grievance that united the Omani tribes behind Ahmad ibn Said's leadership",
            "Oman's geography — a maritime trading nation with the finest natural harbours in the Arabian Peninsula and direct access to the Indian Ocean trade routes — made commercial dominance the natural ambition of an Omani dynasty",
            "The decline of Portuguese power in the Indian Ocean (17th century) and the subsequent weakness of Safavid Persian naval capacity created the strategic opening that Omani sultans exploited to build their maritime empire"
        ],
        "effects": [
            "The Omani maritime empire under Said bin Sultan (1806–1856) made Zanzibar the commercial hub of the western Indian Ocean — a trading centre for ivory, slaves, and spices whose legacy shaped East African history and demographics",
            "The division of Said bin Sultan's empire between his sons (1856) — Oman and Zanzibar — created two distinct states whose separation was formalised by British arbitration (Canning Award, 1861), establishing the modern political geography of both Oman and Zanzibar",
            "Sultan Qaboos's transformation of Oman (1970–2020) from a medieval sultanate — with only 3 schools, 10 km of paved roads, and 1 hospital in 1970 — into a modern state while maintaining its distinctive cultural character is one of the Gulf's most remarkable development stories",
            "Oman's mediation role under Qaboos — facilitating US-Iran backchannel communications and the framework for the Iran nuclear deal (JCPOA, 2015) — demonstrated that small Gulf states could exercise significant diplomatic leverage through strategic neutrality"
        ],
        "relationships": [
            {"entity": "Ahmad ibn Said Al-Said", "relationship": "FOUNDED_BY", "note": "Ahmad ibn Said founded the dynasty (1744) after expelling the Persian occupation — elected imam by Omani tribal leaders"},
            {"entity": "Said bin Sultan", "relationship": "MARITIME_EMPIRE_BUILT_BY", "note": "Said bin Sultan (r. 1806–1856) built the Omani maritime empire — controlling Zanzibar, the East African coast, and Indian Ocean trade routes"},
            {"entity": "Zanzibar", "relationship": "CONTROLLED_AS_CAPITAL_OF_MARITIME_EMPIRE", "note": "Said bin Sultan made Zanzibar his capital (1840) — the commercial hub of the western Indian Ocean and centre of the East African ivory and slave trades"},
            {"entity": "Sultan Qaboos bin Said", "relationship": "MODERNISED_OMAN_UNDER", "note": "Qaboos (r. 1970–2020) transformed Oman from a medieval state into a modern country while maintaining its distinctive foreign policy of neutrality"},
            {"entity": "Iran nuclear deal (JCPOA, 2015)", "relationship": "FACILITATED_NEGOTIATIONS_FOR", "note": "Oman under Qaboos facilitated the secret US-Iran negotiations (2013) that produced the framework for the JCPOA — demonstrating its unique mediation role"}
        ],
    }),

    ("alawi-dynasty", {
        "summary": (
            "The Alawi dynasty (also Alaouite; Arabic: العلويون) has ruled Morocco since 1631 — making it one of the world's longest-reigning dynasties and the oldest continuous ruling house in the Arab world. The Alaouites claim descent from the Prophet Muhammad through his grandson Hassan ibn Ali, giving them the sharifianic (prophetic lineage) religious legitimacy that has been the foundation of their authority for nearly four centuries. The dynasty was founded by Moulay Ali al-Sharif in Tafilalt (southeastern Morocco) and his son Moulay Rashid unified Morocco by 1666.\n\n"
            "The Alawi's greatest ruler was Moulay Ismail (r. 1672–1727), who built a centralised Moroccan state with a 150,000-strong standing army (including 30,000 Black African slave soldiers, the Black Guard), constructed the imperial city of Meknes, expelled the English from Tangier and the Spanish from Mahdiya, and established diplomatic relations with Louis XIV of France. Morocco under Moulay Ismail was briefly the strongest African state north of the Sahara.\n\n"
            "The dynasty survived French and Spanish protectorate rule (1912–1956), with Mohammed V's alliance with the independence movement making him the symbol of Moroccan nationalism. Mohammed VI (r. 1999–present) has pursued constitutional reform while maintaining the monarchy's pre-eminent position, and Morocco remains one of the Arab world's most politically stable states — making the Alawi dynasty one of the most remarkable examples of dynastic continuity in modern history."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Ruling dynasty of Morocco since 1631; sharifianic legitimacy through prophetic descent; Moulay Ismail (1672–1727) built Morocco's greatest centralised state; Mohammed V led independence from France (1956); Mohammed VI has maintained Morocco as one of the Arab world's most stable monarchies.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The collapse of the Saadian dynasty's central authority in the early 17th century — resulting in Morocco's fragmentation into competing tribal and regional powers — created the political vacuum that the Alawi sharifs of Tafilalt could fill by leveraging their religious prestige",
            "The Alawi claim to prophetic descent (sharifianic lineage) provided the religious legitimacy that enabled them to unite Morocco's diverse Berber and Arab tribal factions behind a single dynasty — the decisive political advantage over purely military claimants",
            "Moulay Rashid's military campaigns (1660s) — systematically defeating competing powers across Morocco, from the Dila'iyya religious confederation to urban factions in Fez and Marrakesh — unified the country under Alawi authority within a decade"
        ],
        "effects": [
            "Moulay Ismail's 55-year reign (1672–1727) created the most centralised Moroccan state since the Almohads — with a Black Guard standing army, the construction of Meknes as an imperial capital rivalling Versailles, and diplomatic engagement with European powers",
            "Morocco's status as the first nation to recognise the United States (1777) — through a letter of Sultan Mohammed III to the Continental Congress — established a diplomatic relationship that has made the US-Morocco Treaty of Peace and Friendship (1787) the oldest unbroken US treaty alliance",
            "Mohammed V's alliance with Morocco's independence movement — and his exile by France (1953) then triumphant return (1955) — made him the father of modern Morocco and established the pattern of activist monarchy that his successors have maintained",
            "The Alawi dynasty's survival through French and Spanish colonialism, Cold War realignments, and the Arab Spring (2011) — where constitutional reforms defused mass protests — demonstrates a remarkable capacity for adaptive monarchical governance"
        ],
        "relationships": [
            {"entity": "Moulay Ismail", "relationship": "GREATEST_RULER_OF", "note": "Moulay Ismail (r. 1672–1727) built Morocco's most centralised state — with the Black Guard army, the Meknes imperial city, and diplomatic relations with European powers"},
            {"entity": "Mohammed V of Morocco", "relationship": "INDEPENDENCE_ACHIEVED_BY", "note": "Mohammed V's leadership of the independence movement and his return from French exile (1955) created modern Morocco — making him the dynasty's most nationally venerated figure"},
            {"entity": "Mohammed VI of Morocco", "relationship": "CURRENT_RULER", "note": "Mohammed VI (r. 1999–present) has pursued constitutional reform while maintaining the Alawi monarchy's pre-eminent position in Moroccan politics"},
            {"entity": "Morocco", "relationship": "RULING_DYNASTY_OF", "note": "The Alawi dynasty has ruled Morocco since 1631 — nearly four centuries of dynastic continuity"},
            {"entity": "United States", "relationship": "FIRST_NATION_TO_RECOGNISE_AS_INDEPENDENT", "note": "Sultan Mohammed III of Morocco was among the first rulers to recognise US independence (1777) — producing the oldest unbroken US treaty alliance (1787)"}
        ],
    }),

    ("antigonid-dynasty", {
        "summary": (
            "The Antigonid dynasty (306–168 BCE) was the Macedonian royal house that ruled the Kingdom of Macedon following the Wars of the Diadochi — the struggle among Alexander the Great's successors for his empire. Founded by Antigonus I Monophthalmus ('the One-Eyed') and formally established by his son Demetrius I Poliorcetes ('the Besieger'), the dynasty controlled Macedon and dominated Greece for nearly 150 years — making it one of the three major successor kingdoms to Alexander's empire, alongside the Ptolemies (Egypt) and Seleucids (Asia).\n\n"
            "The Antigonids' most significant ruler was Antigonus III Doson and especially Philip V, whose alliance with Hannibal Barca of Carthage during the Second Punic War (Philip-Hannibal Treaty, 215 BCE) brought Rome into Greek affairs for the first time. Rome's subsequent victories over Philip V (Battle of Cynoscephalae, 197 BCE) and Perseus (Battle of Pydna, 168 BCE) ended Macedonian power and marked the moment when Rome definitively replaced Macedon as the dominant power of the Mediterranean world.\n\n"
            "The Antigonid period produced the cultural and intellectual life of Hellenistic Greece — Stoic and Epicurean philosophy flourished in Athens during Antigonid suzerainty, and the Antigonid court patronised scholarship and the arts. The dynasty's fall at Pydna (168 BCE) and the subsequent Roman organisation of Macedonia as a province (148 BCE) ended the last line of Alexander's successors."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Macedonian ruling dynasty (306–168 BCE); one of three major Hellenistic successor kingdoms; Philip V's alliance with Hannibal brought Rome into Greek affairs; defeated at Cynoscephalae (197 BCE) and Pydna (168 BCE) — Rome's victories that made it the Mediterranean's dominant power.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Antigonus I's attempt to reunite Alexander's empire under his own rule triggered the Wars of the Diadochi — and his defeat at Ipsus (301 BCE) established that no single successor could reunite the empire, producing the three-kingdom balance that defined the Hellenistic world",
            "Demetrius I Poliorcetes' capture of Macedon (294 BCE) established the dynasty's Macedonian territorial base — giving the Antigonids control of the Macedonian heartland and its famous army tradition",
            "The Macedonian kingdom's geographic position — between the Greek city-states to the south and the Danubian and Illyrian tribes to the north — required constant military activity that maintained the Macedonian military tradition and professional army"
        ],
        "effects": [
            "Philip V's Macedonian Wars against Rome (215–205, 200–197 BCE) — triggered by his alliance with Hannibal — brought Roman military power permanently into the Greek world, with Cynoscephalae (197 BCE) demonstrating that the Roman legion was superior to the Macedonian phalanx",
            "Perseus's defeat at Pydna (168 BCE) and his capture ended the Antigonid dynasty — Rome's subsequent organisation of Macedonia as a province (148 BCE) ended Greek political independence for the following two millennia",
            "The Antigonid period was the era of Hellenistic philosophy's florescence: the Stoic school of Zeno of Citium, the Epicurean school of Epicurus, and the Skeptic school of Pyrrho all developed under Antigonid Athens",
            "Antigonus Gonatas's cultivation of Stoic philosophy and his court's intellectual life established the model of Hellenistic royal patronage of philosophy that influenced the Ptolemaic and Seleucid courts and ultimately Roman aristocratic culture"
        ],
        "relationships": [
            {"entity": "Antigonus I Monophthalmus", "relationship": "FOUNDED_BY", "note": "Antigonus I — one of Alexander's most powerful generals — founded the dynasty, though he died at Ipsus (301 BCE) before consolidating Macedon"},
            {"entity": "Philip V of Macedon", "relationship": "KINGDOM_WEAKENED_BY_WARS_OF", "note": "Philip V's alliance with Hannibal and his subsequent defeats in the Macedonian Wars (215–197 BCE) fatally weakened the dynasty's power"},
            {"entity": "Battle of Pydna (168 BCE)", "relationship": "DYNASTY_ENDED_AT", "note": "Perseus's defeat by Aemilius Paullus at Pydna (168 BCE) ended the Antigonid dynasty and Macedonian independence"},
            {"entity": "Roman Republic", "relationship": "DEFEATED_AND_REPLACED_BY", "note": "Rome's victories at Cynoscephalae (197 BCE) and Pydna (168 BCE) replaced Macedon as the Mediterranean's dominant power"},
            {"entity": "Hellenistic philosophy", "relationship": "FLOURISHED_UNDER_PATRONAGE_OF", "note": "Stoic, Epicurean, and Skeptic philosophy flourished in Athens during the Antigonid period — the golden age of Hellenistic thought"}
        ],
    }),

    ("argead-dynasty", {
        "summary": (
            "The Argead dynasty was the royal house of ancient Macedon that produced Philip II and Alexander the Great — transforming Macedonia from a peripheral kingdom into the centre of the largest Western empire the ancient world had seen. Tracing their lineage to Argos in the Peloponnese, the Argeads had ruled Macedon since approximately the 7th century BCE. Philip II's reforms (359–336 BCE) — the Macedonian phalanx, companion cavalry, siege technology — created the combined-arms system that proved unstoppable at Chaeronea (338 BCE), establishing Macedonian hegemony over Greece.\n\n"
            "Philip's assassination (336 BCE) brought his 20-year-old son Alexander to the throne. In thirteen years Alexander conquered the Persian Empire, Egypt, Central Asia, and northwestern India — creating the largest empire the Western world had known, stretching from Greece to the Indus Valley. His founding of Alexandria (331 BCE) and 70+ cities named after himself created an urban network that anchored Hellenistic civilisation across the Near East. Alexander died in Babylon (323 BCE) at 32, leaving no clear successor.\n\n"
            "The Argead dynasty ended with the murder of Alexander's posthumous son Alexander IV and half-brother Philip III Arrhidaeus by the Diadochi (successor generals). But Alexander's conquests had already created the Hellenistic world — three centuries of Greek-language civilisation from the Mediterranean to the Indus — whose cultural synthesis produced the conditions for early Christianity, the transmission of Greek philosophy to Rome, and ultimately the Western intellectual tradition."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Royal house of Philip II and Alexander the Great; Philip's military revolution created the Macedonian phalanx; Alexander's conquests (336–323 BCE) created the Hellenistic world — Greek civilisation from the Mediterranean to the Indus that shaped Christianity, Roman culture, and the Western intellectual tradition.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Macedonia's marginal position in the Greek world — dismissed as semi-barbarous — created the military necessity that drove Philip II's transformation of a feudal levy into a professional standing army with revolutionary tactical innovations",
            "The Macedonian cavalry tradition — the finest heavy cavalry in the Greek world — gave Philip's combined-arms system its decisive striking power, used by Alexander to shatter every army he encountered",
            "Philip II's diplomatic genius — neutralising potential coalitions through marriages, bribes, and strategic timing — created the conditions for Alexander's unobstructed eastern campaign"
        ],
        "effects": [
            "Alexander's conquests spread Greek language, culture, and institutions from Egypt to the Indus Valley — creating the Hellenistic world in which Greek became the lingua franca of educated classes, enabling the cross-cultural synthesis from which early Christianity emerged",
            "The Macedonian phalanx and combined-arms system became the template for Hellenistic and Roman military organisation — shaping Mediterranean warfare for three centuries",
            "Alexander's founding of Alexandria (331 BCE) created the greatest city of the ancient world — home of the Library of Alexandria and the Pharos lighthouse, and the intellectual centre of Hellenistic and early Christian scholarship",
            "The wars of the Diadochi (Alexander's successors, 323–281 BCE) produced the three Hellenistic kingdoms — Seleucid, Ptolemaic, Antigonid — that shaped the political geography of the ancient world for the following two centuries"
        ],
        "relationships": [
            {"entity": "Philip II of Macedon", "relationship": "PRODUCED_GREATEST_MILITARY_REFORMER", "note": "Philip II (r. 359–336 BCE) transformed Macedonia into a military superpower — creating the phalanx and companion cavalry system"},
            {"entity": "Alexander the Great", "relationship": "GREATEST_RULER_OF", "note": "Alexander (r. 336–323 BCE) created the largest Western empire of the ancient world — from Greece to northwestern India — in thirteen years of conquest"},
            {"entity": "Battle of Chaeronea (338 BCE)", "relationship": "ESTABLISHED_GREEK_HEGEMONY_AT", "note": "Philip II's victory at Chaeronea (338 BCE) ended Greek city-state independence and established Macedonian hegemony"},
            {"entity": "Hellenistic world", "relationship": "CREATED_BY_CONQUESTS_OF", "note": "Alexander's conquests created the Hellenistic world — three centuries of Greek-language civilisation that shaped Christianity and Western culture"},
            {"entity": "Library of Alexandria", "relationship": "CITY_THAT_HOUSED_IT_FOUNDED_BY", "note": "Alexander founded Alexandria (331 BCE) — which became home of the Library of Alexandria, the ancient world's greatest centre of scholarship"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 05 — {len(ENTITIES)} entities (Class 312: Medieval & Ancient Dynasties)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
