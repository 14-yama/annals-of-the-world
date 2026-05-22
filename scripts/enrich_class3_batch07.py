#!/usr/bin/env python3
"""
Batch 07 — 8 entities (Class 312): Afrighids, Alids, Ahmadilis, 
Angkorian Khmer Empire, Artuqids, Arpad Dynasty, Artaxiad Dynasty, Arsacid Dynasty
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

    ("afrighids", {
        "summary": (
            "The Afrighids were the ruling dynasty of ancient Khwarezm — a region along the lower Amu Darya (Oxus) river in what is now Uzbekistan and Turkmenistan — one of the oldest continuously inhabited agricultural oases of Central Asia. The dynasty's origins are traced to the 3rd century CE, though the chronology is uncertain; they ruled for over 700 years until the Arab Muslim conquest of Khwarezm (c. 712 CE) under the Umayyad general Qutayba ibn Muslim. The Afrighid capital was at Kath (or Al-Fil), and later at Jurjaniyya.\n\n"
            "The Afrighid period is a crucial chapter in Central Asian history: Khwarezm was one of the great agricultural civilisations of the ancient world, fed by the Amu Darya's irrigation canals and positioned on the Silk Road trade routes connecting Iran, Central Asia, and the Eurasian steppe. The Afrighids maintained this sophisticated agricultural and urban civilisation for centuries despite pressure from nomadic steppe peoples and the Sassanid Persian Empire.\n\n"
            "The Arab conquest of Khwarezm (712 CE) ended Afrighid independence and integrated the region into the Islamic world. Subsequent Islamic scholarship preserved Khwarezmian knowledge — the great medieval scholar Al-Biruni (973–1048) was born in Khwarezm and drew on the region's pre-Islamic intellectual tradition in his encyclopaedic works on history, astronomy, and mathematics."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Ancient dynasty of Khwarezm (c. 3rd–8th century CE); one of Central Asia's oldest continuous ruling houses; maintained Khwarezm's sophisticated irrigation-based civilisation for 700+ years; Arab conquest (712 CE) integrated the region into Islam; Al-Biruni (born in Khwarezm) preserved its pre-Islamic intellectual heritage.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Khwarezm's position on the lower Amu Darya — one of the few reliable water sources in the Central Asian desert — created a stable agricultural civilisation that could support a regional dynasty for centuries",
            "The Afrighids' ability to negotiate the competing pressures of Sassanid Persian imperialism, nomadic steppe incursions, and Silk Road commercial networks — playing each off against the others — allowed the dynasty's remarkable longevity",
            "Khwarezm's geographic isolation — surrounded by desert and the Aral Sea — made it difficult to conquer and easy to defend, providing a natural protective buffer that reinforced Afrighid longevity"
        ],
        "effects": [
            "The Arab conquest of Khwarezm (712 CE) integrated the region into the Islamic cultural sphere — beginning the process that would produce major Islamic scholars including Al-Biruni (born 973 CE) and Al-Khwarizmi (born c. 780 CE, whose name gave us 'algorithm')",
            "The Afrighid period's agricultural infrastructure — the elaborate canal systems of the Khwarezm oasis — sustained the region's population density and formed the basis of the medieval Khwarezmid Empire's economic power",
            "Al-Khwarizmi — whose name derives from 'Khwarezm' — was born after the Arab conquest but in the region shaped by the Afrighid agricultural and intellectual tradition; his algebra text (c. 820 CE) gave mathematics its most transformative medieval contribution",
            "The Afrighids exemplify the pattern of oasis civilisations that maintained sophisticated cultures on the margins of the great empires — demonstrating how geographic niches can support long-lasting, culturally significant polities"
        ],
        "relationships": [
            {"entity": "Khwarezm", "relationship": "RULING_DYNASTY_OF", "note": "The Afrighids ruled Khwarezm — the lower Amu Darya oasis — for over 700 years, one of the longest-lasting regional dynasties in Central Asia"},
            {"entity": "Umayyad Caliphate", "relationship": "CONQUERED_BY", "note": "The Umayyad general Qutayba ibn Muslim conquered Khwarezm (c. 712 CE) — ending Afrighid independence and integrating the region into the Islamic world"},
            {"entity": "Al-Biruni", "relationship": "KHWAREZMIAN_CULTURAL_TRADITION_PRESERVED_BY", "note": "Al-Biruni (973–1048), born in Khwarezm, drew on the region's pre-Islamic intellectual tradition in his encyclopaedic scientific works"},
            {"entity": "Al-Khwarizmi", "relationship": "CULTURAL_REGION_THAT_PRODUCED", "note": "Al-Khwarizmi ('from Khwarezm', c. 780–850 CE) gave algebra its foundational text — his name giving English 'algorithm'"},
            {"entity": "Silk Road", "relationship": "CONTROLLED_KHWAREZMIAN_SECTION_OF", "note": "The Afrighids controlled Khwarezm's section of the Silk Road — a key trade junction between Iran, Central Asia, and the Eurasian steppe"}
        ],
    }),

    ("alids", {
        "summary": (
            "The Alids were the descendants of Ali ibn Abi Talib — the Prophet Muhammad's cousin and son-in-law — who formed one of Islam's most politically significant genealogical groups. The Alid claim to leadership of the Muslim community was the theological foundation of Shia Islam: the belief that religious and political authority (the Imamate) rightfully belonged to Ali and his descendants through Fatima (Muhammad's daughter). The Alids' tragic political history — from Ali's assassination (661 CE) to Hussein's martyrdom at Karbala (680 CE) — shaped Shia theology, ritual, and political culture across fourteen centuries.\n\n"
            "Numerous Alid dynasties established regional rule across the Islamic world: the Zaydis in Yemen (897 CE — ongoing as the Houthi movement's ideological ancestors), the Idrisids in Morocco (788–974), the Fatimid Caliphate in North Africa and Egypt (909–1171), and various Imami and Zaydi Alid principalities in Iran, Iraq, and the Arabian Peninsula. The Sharifs of Mecca — keepers of the holy cities — were also Alids, as were the Moroccan Alawi dynasty (still reigning).\n\n"
            "The Alid genealogical claim — descent from the Prophet through Ali and Fatima — remained politically potent across the entire Islamic world, providing legitimacy for ruling dynasties from Morocco to Central Asia. No other kinship group in Islamic history has been more politically significant."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Descendants of Ali ibn Abi Talib whose claim to Islamic leadership is the foundation of Shia Islam; Alid dynasties ruled from Morocco to Yemen to Egypt; the Alawi dynasty (Morocco) and Hashemite dynasty (Jordan) are living Alid ruling houses; Karbala (680 CE) shaped 14 centuries of Shia theology and ritual.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Ali ibn Abi Talib's unique position — cousin and son-in-law of Muhammad, father of Hasan and Hussein, one of the first converts — gave his descendants the most direct possible claim to prophetic lineage within the early Islamic community",
            "Ali's assassination (661 CE) and the subsequent Umayyad suppression of Alid political aspirations created a martyrology — culminating in Karbala (680 CE) — that transformed Alid genealogical identity into the foundational narrative of Shia religious consciousness",
            "The widespread sympathy for the Alid cause across the Islamic world — particularly among non-Arab Muslims who resented Umayyad Arab privilege — provided the social base that Alid claimants repeatedly mobilised for political and religious movements"
        ],
        "effects": [
            "The Alid martyrology — Ali's assassination (661), Hassan's poisoning (670), Hussein's massacre at Karbala (680) — became the theological narrative of Shia Islam, shaping the ritual calendar (Muharram/Ashura), theology of redemptive suffering, and political resistance culture of Shia communities across 14 centuries",
            "Alid dynasties shaped the political geography of the Islamic world: the Idrisids Islamised Morocco (788 CE), the Fatimids built Cairo and Al-Azhar (969–975 CE), and the Zaydi Imamate created Yemen's distinctive political culture",
            "The Alid genealogical claim remained politically potent into the modern era: the Hashemite dynasty (descendants of the Sharifs of Mecca) rules Jordan; the Moroccan Alawi dynasty (also Alid) has ruled since 1631; Iran's Islamic Republic uses Alid legitimacy as ideological foundation",
            "The Fatimid Caliphate's founding of Al-Azhar University (970 CE) in Cairo — as an Alid/Ismaili institution that subsequently became Sunni — created the most influential centre of Islamic learning in the world, still operating"
        ],
        "relationships": [
            {"entity": "Ali ibn Abi Talib", "relationship": "DESCENDANTS_OF", "note": "The Alids are all descendants of Ali ibn Abi Talib — the Prophet Muhammad's cousin and son-in-law"},
            {"entity": "Battle of Karbala (680 CE)", "relationship": "FOUNDATIONAL_TRAUMA_NARRATIVE_OF", "note": "Hussein ibn Ali's martyrdom at Karbala (680 CE) is the foundational trauma of Shia Islam — shaping Alid political identity across 14 centuries"},
            {"entity": "Fatimid Caliphate", "relationship": "MOST_POWERFUL_ALID_DYNASTY_WAS", "note": "The Fatimid Caliphate (909–1171) — ruling North Africa and Egypt — was the most powerful Alid dynasty, founding Cairo and Al-Azhar"},
            {"entity": "Shia Islam", "relationship": "FOUNDATIONAL_GENEALOGICAL_CLAIM_OF", "note": "The Alid genealogical claim — descent from Ali and Fatima — is the theological foundation of Shia Islam's Imamate doctrine"},
            {"entity": "Alawi dynasty of Morocco", "relationship": "LIVING_ALID_RULING_HOUSE", "note": "The Moroccan Alawi dynasty (ruling since 1631) is a living Alid dynasty — currently represented by King Mohammed VI"}
        ],
    }),

    ("ahmadilis", {
        "summary": (
            "The Ahmadilis were a Kurdish Muslim dynasty that ruled Maragha — a city in the Tabriz region of northwestern Iran (Azerbaijan province) — from the mid-11th to the early 13th century CE. Founded by Ahmadil ibn Ibrahim, a Kurdish military commander who received Maragha as a fief from the Seljuk sultan, the dynasty maintained local autonomy under nominal Seljuk suzerainty. Maragha under the Ahmadilis was a prosperous regional centre on the trade routes between Iran, the Caucasus, and Anatolia.\n\n"
            "The Ahmadilis are historically notable as one of several Kurdish dynasties that established regional power under Seljuk overlordship — alongside the Marwanids, Hasanwayhids, and Annazids — demonstrating the broader pattern of Kurdish tribal leadership translating military service to nomadic Turkic empires into regional hereditary rule. The dynasty's most significant ruler was Qarategin (or Aq-Sunqur), who maintained Maragha's prosperity in the early 12th century.\n\n"
            "The Ahmadilid dynasty ended when the Atabeg of Azerbaijan absorbed Maragha in the early 13th century. Maragha subsequently became famous as the site of the Maragha Observatory — built by Hulagu Khan's astronomer Nasir al-Din Tusi (1259–1265) — one of the greatest astronomical observatories of the medieval world, whose planetary models prefigured Copernicus."
        ),
        "importanceScore": 4,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Kurdish dynasty ruling Maragha, Azerbaijan (mid-11th to early 13th century); one of several Kurdish Seljuk-period regional dynasties; Maragha subsequently housed the great Maragha Observatory (1259) whose astronomical models prefigured Copernicus.",
            "significanceCategory": "local"
        },
        "causes": [
            "Ahmadil ibn Ibrahim's military service to the Seljuk sultans — typical of how Kurdish tribal leaders translated military loyalty into regional governance rights — secured Maragha as a hereditary fief for the dynasty",
            "Maragha's strategic position on the trade routes connecting Iran, the Caucasus, and Anatolia gave the city commercial wealth that sustained the Ahmadili court",
            "The Seljuk system of granting autonomous provincial rule to loyal commanders in exchange for military service — extended to both Turkic and Kurdish leaders — created the political framework that made the Ahmadilis viable"
        ],
        "effects": [
            "Maragha's development under the Ahmadilis as a regional centre contributed to the urban infrastructure and scholarly tradition that later made it the natural site for the Maragha Observatory (1259) — a world-historical institution",
            "The Ahmadilid dynasty exemplifies the Kurdish pattern of military service to Turkic overlords translating into regional autonomy — a template that continued through the Ayyubids (Saladin's dynasty) and beyond",
            "The absorption of Maragha into the Atabeg of Azerbaijan's territory contributed to the political consolidation of Azerbaijan that preceded the Mongol invasion — the context in which the Maragha Observatory was subsequently built",
            "The Ahmadilis provide inscriptional and numismatic evidence for Kurdish dynastic governance in the Seljuk period — contributing to the limited body of sources for Kurdish political history before the Ayyubid era"
        ],
        "relationships": [
            {"entity": "Ahmadil ibn Ibrahim", "relationship": "FOUNDED_BY", "note": "Ahmadil ibn Ibrahim — a Kurdish Seljuk military commander — founded the dynasty after receiving Maragha as a hereditary fief"},
            {"entity": "Seljuk Empire", "relationship": "NOMINAL_VASSALS_OF", "note": "The Ahmadilis ruled Maragha under nominal Seljuk suzerainty — a Kurdish regional dynasty within the Seljuk provincial system"},
            {"entity": "Maragha", "relationship": "RULING_DYNASTY_OF", "note": "The Ahmadilis ruled Maragha — a city in Azerbaijan province, Iran — for approximately 150 years"},
            {"entity": "Maragha Observatory", "relationship": "CITY_SUBSEQUENTLY_HOSTED", "note": "Maragha (after the Ahmadili period) hosted the great Maragha Observatory (1259–65) — built by Nasir al-Din Tusi under Mongol patronage, whose planetary models prefigured Copernicus"},
            {"entity": "Kurdish dynasties (Seljuk period)", "relationship": "PART_OF_PATTERN_OF", "note": "The Ahmadilis were one of several Kurdish dynasties (alongside Marwanids, Hasanwayhids, Annazids) that established regional rule under Seljuk overlordship"}
        ],
    }),

    ("angkorian-khmer-empire", {
        "summary": (
            "The Khmer Empire (802–1431 CE), based at Angkor in what is now northwestern Cambodia, was the largest empire in the history of Southeast Asia — at its peak under Suryavarman II (r. 1113–1145) controlling territory encompassing modern Cambodia, Thailand, Laos, and parts of Vietnam and Myanmar. Founded by Jayavarman II, who declared himself a devaraja (god-king) at Phnom Kulen in 802 CE, the empire built the most spectacular complex of religious monuments in the world — the temples of Angkor, including Angkor Wat (the largest religious structure on earth) and the Bayon.\n\n"
            "The Khmer Empire's hydraulic engineering was its defining civilisational achievement: the Angkorian engineers built one of the ancient world's most sophisticated water management systems — a network of reservoirs (baray), canals, and irrigation channels covering hundreds of square kilometres that enabled intensive wet-rice agriculture supporting a population of up to one million in the Angkor metropolitan area. This was the largest pre-industrial city on earth.\n\n"
            "Angkor Wat — built by Suryavarman II as a Hindu temple to Vishnu, later converted to Buddhist worship — is the single largest religious monument ever built, covering 1.6 square kilometres. Its construction required the quarrying and transport of 5–10 million sandstone blocks from a quarry 35 km away. The empire's decline from the 13th century — caused by climate change, hydraulic system failure, and Thai military pressure — culminated in the Siamese (Thai) sack of Angkor (1431)."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Largest empire in Southeast Asian history (802–1431); built Angkor Wat — the world's largest religious monument; hydraulic engineering supported a city of up to 1 million people — the largest pre-industrial urban agglomeration; its collapse is a canonical case study in hydraulic civilisation failure.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Jayavarman II's devaraja cult — declaring himself a god-king at Phnom Kulen (802 CE) — unified the fragmented Khmer chieftaincies under a single cosmological political order, providing the ideological framework for centralised imperial expansion",
            "The Mekong Delta and Tonle Sap lake system's extraordinary ecological productivity — the Tonle Sap is the world's largest inland fishery — provided the food base for the large population that built and maintained the Angkorian monuments and army",
            "The Khmer hydraulic engineers' ability to manage the extreme annual variation in water availability — storing monsoon water in massive reservoirs for dry-season irrigation — enabled the intensive wet-rice agriculture that supported Angkor's million-person population"
        ],
        "effects": [
            "Angkor Wat's construction (c. 1113–1150 CE) created the world's largest religious monument — covering 1.6 km² — demonstrating the extraordinary mobilising power of the Khmer devaraja system and providing the cultural symbol of modern Cambodia (on the national flag)",
            "The Khmer Empire's cultural sphere — Angkorian Hinduism, Sanskrit inscriptions, temple architecture — spread across Southeast Asia, shaping the artistic traditions of Thailand, Laos, Vietnam, and Indonesia for the following millennium",
            "The Angkorian hydraulic system's collapse — caused by extended droughts revealed by tree-ring data (14th–15th centuries) combined with system damage from Siamese invasions — is a canonical example of how hydraulic civilisation collapse can produce rapid urban depopulation",
            "The 'mystery' of Angkor's abandonment captivated European explorers (Henri Mouhot rediscovered Angkor Wat in 1860) and generated the modern archaeological study of Southeast Asian civilisations, fundamentally reshaping Western understanding of Asian historical achievement"
        ],
        "relationships": [
            {"entity": "Jayavarman II", "relationship": "FOUNDED_BY", "note": "Jayavarman II declared himself devaraja (god-king) at Phnom Kulen (802 CE) — founding the Khmer Empire"},
            {"entity": "Angkor Wat", "relationship": "BUILT_GREATEST_MONUMENT", "note": "Suryavarman II built Angkor Wat (c. 1113–1150) — the world's largest religious monument, covering 1.6 km²"},
            {"entity": "Suryavarman II", "relationship": "GREATEST_BUILDER_OF", "note": "Suryavarman II (r. 1113–1145) built Angkor Wat and presided over the empire's greatest territorial extent"},
            {"entity": "Siamese (Thai) armies", "relationship": "CAPITAL_SACKED_BY", "note": "Siamese forces sacked Angkor (1431) — ending the empire's Angkorian phase and beginning the abandonment of the city"},
            {"entity": "Tonle Sap lake", "relationship": "ECOLOGICAL_FOOD_BASE_PROVIDED_BY", "note": "The Tonle Sap — the world's largest inland fishery — provided the protein base for Angkor's million-person population"}
        ],
    }),

    ("artuqids", {
        "summary": (
            "The Artuqids were a Turkoman dynasty that ruled parts of southeastern Anatolia, northern Mesopotamia, and the Jazira (Upper Tigris region) from approximately 1101 to 1409 CE. Named after their founder Artuk ibn Eksük — a Oghuz Turkoman commander under the Seljuk sultans — the dynasty established three branches: the Sokmenids of Hasankeyf (1102–1231), the Balakids of Mardin (1104–1409), and the branch of Harput (c. 1185–1234). The dynasty ruled during the Crusading period and interacted extensively with both Crusader states and the Ayyubid sultanate.\n\n"
            "The Artuqids are famous for commissioning two remarkable medieval texts: 'Al-Jazari's Book of Knowledge of Ingenious Mechanical Devices' (1206) — dedicated to the Artuqid sultan of Diyarbakır — was the most comprehensive mechanical engineering manual of the medieval world, describing 50 mechanical devices including water clocks, automata, and pumping machines whose designs directly influenced European mechanical engineering. The Artuqid coins are also notable for depicting ancient Greek, Byzantine, and Seljuk iconographic elements in a remarkable syncretic numismatic tradition.\n\n"
            "The Artuqid dynasty survived longer than most Anatolian Turkish dynasties — outlasting the Crusader states, the Ayyubids, and the Mongol invasion's first wave — before finally being absorbed into the expanding Timurid and Black Sheep Turcoman powers in the 14th–15th centuries."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Turkoman dynasty of southeastern Anatolia and northern Mesopotamia (1101–1409); patron of Al-Jazari's 'Book of Ingenious Mechanical Devices' (1206) — the medieval world's most comprehensive mechanical engineering manual; syncretic coinage; survived the Crusades, Ayyubids, and Mongol invasion.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Seljuk Empire's grant of Diyarbakır and the Jazira region to Artuk ibn Eksük as a fief — in recognition of his military service — provided the territorial base for the dynasty's establishment",
            "The political fragmentation of the Jazira region following the First Crusade (1099) and the subsequent Crusader-Muslim conflict created a strategic environment in which small, militarily capable dynasties like the Artuqids could survive by balancing between the major powers",
            "The Artuqids' geographic position — between the Crusader states, the Byzantine Empire, the Ayyubid sultanate, and successive Mongol-era powers — gave them the diplomatic flexibility to survive through alliances and tribute payments"
        ],
        "effects": [
            "Al-Jazari's mechanical treatise (1206) — commissioned by the Artuqid sultan — described 50 mechanical devices including water clocks, automata, and water pumps, and its Latin translations influenced European mechanical engineering and were used by Renaissance engineers",
            "The Artuqid coinage — combining Greek, Byzantine, Christian, and Islamic iconographic elements — provides the finest medieval evidence for syncretic visual culture at the intersection of Christian and Islamic civilisations",
            "Hasankeyf — the Artuqid Sokmenid capital — remained one of southeastern Turkey's most historically significant sites, with spectacular cliff-carved monuments, until its partial submersion by the Ilısu Dam (2019) — a significant loss of cultural heritage",
            "The Artuqid dynasty's century of interaction with the Crusader states — sometimes allied, sometimes at war — demonstrates the complex, pragmatic relationships between Muslim and Christian polities in the medieval Levant, contradicting simplistic narratives of permanent religious warfare"
        ],
        "relationships": [
            {"entity": "Al-Jazari", "relationship": "COMMISSIONED_GREATEST_MECHANICAL_TREATISE_FROM", "note": "The Artuqid sultan of Diyarbakır commissioned Al-Jazari's 'Book of Ingenious Mechanical Devices' (1206) — the medieval world's most comprehensive mechanical engineering manual"},
            {"entity": "Hasankeyf", "relationship": "CAPITAL_OF_SOKMENID_BRANCH", "note": "Hasankeyf was the Artuqid Sokmenid branch's capital — its spectacular cliff monuments partially submerged by the Ilısu Dam (2019)"},
            {"entity": "Seljuk Empire", "relationship": "FOUNDED_AS_FIEF_OF", "note": "Artuk ibn Eksük received Diyarbakır as a Seljuk fief — establishing the dynasty's territorial base"},
            {"entity": "Ayyubid dynasty", "relationship": "NEIGHBOURING_POWER_AND_RIVAL", "note": "The Artuqids and Ayyubids were neighbouring powers in the Jazira — competing and cooperating in the complex political landscape of the Crusading period"},
            {"entity": "Crusader states", "relationship": "NEGOTIATED_AND_FOUGHT_WITH", "note": "The Artuqids' pragmatic relationships with the Crusader states — sometimes allied, sometimes at war — exemplify the complex Muslim-Christian diplomacy of the medieval Levant"}
        ],
    }),

    ("arpad-dynasty", {
        "summary": (
            "The Árpád dynasty (c. 895–1301) was the founding royal house of Hungary — the Magyar dynasty that led the Hungarian conquest of the Carpathian Basin (895 CE), converted Hungary to Christianity, and built it into a major Central European kingdom. Founded by Grand Prince Árpád, who led the seven Magyar tribes across the Carpathians in 895 CE, the dynasty produced Hungary's first king, Stephen I (r. 1000–1038), who Christianised Hungary, established the Church, and organised the kingdom on a Western feudal model — for which he was canonised (1083).\n\n"
            "The Árpáds were one of medieval Europe's most politically successful dynasties: they repelled Holy Roman Emperor Conrad II's invasion (1030), fought the Mongol invasion (the Battle of Mohi, 1241, was a devastating defeat, but Hungary was rebuilt), produced numerous canonised saints within the royal family, and established Hungary's distinctive legal and constitutional traditions including the Golden Bull (1222) — often compared to Magna Carta — issued by King Andrew II, limiting royal power.\n\n"
            "The dynasty's last male-line member, Andrew III, died in 1301. The Árpád period — spanning 400 years — established the foundations of Hungarian statehood, law, Church, and national identity that persisted through the Ottoman occupation, Habsburg rule, and to the present. Stephen I's crown (the Holy Crown of Hungary) remains the supreme symbol of Hungarian statehood."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Founding royal house of Hungary (c. 895–1301); Árpád led the Magyar conquest (895 CE); Stephen I Christianised Hungary (1000) and was canonised; the Golden Bull (1222) limited royal power; 400 years of Árpád rule established Hungary's statehood, Church, law, and national identity.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Frankish Empire's weakness after Charlemagne — and the political vacuum in the Carpathian Basin following the Moravian state's collapse — created the opportunity for Árpád's Magyar confederation to occupy the Pannonian plain permanently (895 CE)",
            "Stephen I's decision to seek a royal crown from Pope Sylvester II (1000 CE) — rather than from the Holy Roman Emperor — aligned Hungary with the papacy and the Western Church, integrating it into Latin Christendom on terms that preserved Hungarian independence from German domination",
            "The Magyar tribes' transition from nomadic raiding (9th century Magyar raids devastated Germany, France, and Italy) to settled agriculture — facilitated by the Carpathian Basin's agricultural productivity — created the preconditions for Stephen I's Christian kingdom"
        ],
        "effects": [
            "Stephen I's Christianisation of Hungary (1000–1038) — establishing episcopal sees, monasteries, and the parochial system — created the institutional Church that became the primary vehicle of Hungarian literacy, law, and cultural continuity through the subsequent centuries",
            "The Golden Bull (1222) — limiting royal power, guaranteeing noble rights, and establishing the right of armed resistance against illegal royal actions — was one of medieval Europe's most important constitutional documents, comparable to Magna Carta",
            "Hungary's survival of the Mongol invasion (Battle of Mohi, 1241) — the Mongols withdrew in 1242 following Ögedei Khan's death — preserved Central European Christianity and established Hungary as a bulwark against nomadic incursions",
            "The Árpád dynasty's 400-year rule created the territorial, institutional, and cultural foundations of the Kingdom of Hungary that survived Ottoman occupation (1526–1699), Habsburg rule (1699–1918), and continues to shape modern Hungarian national identity"
        ],
        "relationships": [
            {"entity": "Árpád", "relationship": "FOUNDED_BY", "note": "Grand Prince Árpád led the Magyar conquest of the Carpathian Basin (895 CE) — founding the dynasty"},
            {"entity": "Stephen I of Hungary (Saint Stephen)", "relationship": "CHRISTIANISED_HUNGARY_UNDER", "note": "Stephen I (r. 1000–1038) Christianised Hungary, established its Church, and was canonised — the dynasty's most significant ruler"},
            {"entity": "Golden Bull (1222)", "relationship": "ISSUED", "note": "King Andrew II issued the Golden Bull (1222) — limiting royal power and guaranteeing noble rights, comparable to Magna Carta"},
            {"entity": "Holy Crown of Hungary", "relationship": "SYMBOL_OF_ROYAL_AUTHORITY_ESTABLISHED_BY", "note": "The Holy Crown — received by Stephen I from Pope Sylvester II (1000 CE) — became the supreme symbol of Hungarian statehood"},
            {"entity": "Battle of Mohi (1241)", "relationship": "KINGDOM_SURVIVED_MONGOL_INVASION_AT", "note": "The Mongol defeat at Mohi (1241) devastated Hungary — but the Mongol withdrawal (1242) preserved the Árpád kingdom and Central European Christianity"}
        ],
    }),

    ("artaxiad-dynasty", {
        "summary": (
            "The Artaxiad dynasty (189 BCE – 12 CE) was the ruling house of ancient Armenia — a kingdom that occupied the highland plateau between the Black Sea, the Caspian, and Mesopotamia, positioned at the crossroads of the Roman and Parthian empires. Founded by Artaxias I after the collapse of the Seleucid Empire's control of the region, the dynasty produced its greatest ruler in Tigranes II 'the Great' (r. 95–55 BCE), who briefly created the largest state in the Near East — controlling Armenia, Syria, Cilicia, Pontus, and parts of Mesopotamia and the Caucasus.\n\n"
            "Tigranes II's empire at its peak (around 80 BCE) stretched from the Caspian Sea to Egypt's border and from the Euphrates to the Mediterranean — making him the most powerful monarch in the Near East since Alexander. He founded a new capital, Tigranocerta, on the model of a Hellenistic city. But his alliance with Mithridates VI of Pontus — his father-in-law — drew him into conflict with Rome: Lucullus and then Pompey defeated him, reducing Armenia to a client kingdom (66 BCE).\n\n"
            "The Artaxiad dynasty ended when the Roman emperor Augustus deposed the last Artaxiad king Tigranes IV (c. 12 CE) and installed the Arsacid Vonones I — beginning centuries of competition between Rome and Parthia for control of the Armenian buffer state. Armenia's buffer position between great empires became its defining geopolitical characteristic through the Byzantine, Sassanid, Arab, Byzantine, and Seljuk periods."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Armenian ruling dynasty (189 BCE–12 CE); Tigranes II 'the Great' briefly created the largest Near Eastern empire since Alexander; Armenia as a Roman-Parthian buffer state — a geopolitical pattern that defined Armenian history for the following millennium.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The fragmentation of the Seleucid Empire in the 2nd century BCE — after the Seleucids' defeat by Rome and their wars with the Maccabees and Parthians — created the opportunity for Artaxias I, a former Seleucid satrap, to declare Armenian independence",
            "Tigranes II's marriage alliance with Mithridates VI of Pontus — the most powerful opponent of Roman expansion in the East — gave him the political partnership that enabled his brief imperial expansion",
            "Armenia's geographic position — highland plateau inaccessible to the great empires' cavalry — made it a natural refuge for an independent state that could exploit the rivalry between the surrounding powers"
        ],
        "effects": [
            "Tigranes II's empire (83–69 BCE) demonstrated that a secondary Near Eastern power could briefly challenge Rome — his temporary control of Syria and Mesopotamia showed the limits of Roman power east of the Euphrates",
            "Pompey's reorganisation of the Near East (66–63 BCE) — following his defeat of Tigranes — created the provincial structure of Roman Syria and established Armenia as a buffer client kingdom, a geopolitical arrangement that persisted for four centuries",
            "Armenia's buffer position between Rome/Byzantium and Parthia/Sassanid Persia shaped Armenian history for a millennium — producing a distinctive culture that absorbed Greek, Persian, and Syriac Christian influences while maintaining its own language, alphabet, and Church",
            "The Armenian Apostolic Church (founded by Gregory the Illuminator, 301 CE) — establishing Armenia as the world's first Christian state — was the cultural monument of the post-Artaxiad period, defining Armenian civilisation through every subsequent occupation"
        ],
        "relationships": [
            {"entity": "Tigranes II of Armenia (the Great)", "relationship": "GREATEST_RULER_OF", "note": "Tigranes II (r. 95–55 BCE) briefly created the largest Near Eastern empire since Alexander — stretching from the Caspian to Egypt's border"},
            {"entity": "Mithridates VI of Pontus", "relationship": "ALLIED_WITH_THROUGH_MARRIAGE", "note": "Tigranes II's marriage to Mithridates VI's daughter allied the two greatest Eastern opponents of Roman expansion"},
            {"entity": "Pompey the Great", "relationship": "DEFEATED_AND_REDUCED_TO_CLIENT_STATUS_BY", "note": "Pompey defeated Tigranes II (66 BCE) and reduced Armenia to a Roman client kingdom — ending the Artaxiad imperial moment"},
            {"entity": "Armenian Apostolic Church", "relationship": "KINGDOM_THAT_PRECEDED_FOUNDING_OF", "note": "The Artaxiad kingdom preceded the Armenian Apostolic Church (301 CE) — Armenia's first Christian state, which defined Armenian civilisation"},
            {"entity": "Tigranocerta", "relationship": "FOUNDED_HELLENISTIC_CAPITAL_AT", "note": "Tigranes II founded Tigranocerta — a Hellenistic-model capital that symbolised his imperial ambitions before it was destroyed by Lucullus (69 BCE)"}
        ],
    }),

    ("arsacid-dynasty", {
        "summary": (
            "The Arsacid dynasty (c. 247 BCE – 224 CE) was the ruling house of the Parthian Empire — the great Iranian power that controlled the Iranian plateau and Mesopotamia for nearly 500 years, contested the Near East with Rome, and preserved the Persian imperial tradition between the Achaemenid and Sassanid periods. Founded by Arsaces I after he led the Parni nomadic tribe in a revolt against the Seleucid satrap of Parthia, the dynasty eventually controlled an empire stretching from the Euphrates to the Indus.\n\n"
            "The Arsacid Parthians were the principal eastern adversary of the Roman Republic and Empire — a geopolitical rivalry that shaped the history of the Near East for four centuries. The Parthian defeat of Crassus at Carrhae (53 BCE) — killing one of Rome's richest men and 20,000 soldiers in the worst Roman military disaster since Cannae — permanently established the Euphrates as the boundary between the Roman and Parthian worlds. Augustus recognised this reality by negotiating the return of the Carrhae standards (20 BCE) — a diplomatic triumph he presented as a victory.\n\n"
            "The Arsacid dynasty ended when Ardashir I — the founder of the Sassanid dynasty — defeated and killed the last Arsacid king Artabanus IV in 224 CE. The Sassanids presented themselves as restoring the Achaemenid Persian tradition that the 'foreign' (originally nomadic) Arsacids had interrupted — though the Arsacids had in fact thoroughly Iranised and become the primary vehicle of Iranian imperial culture between the Achaemenid and Sassanid periods."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Iranian dynasty ruling the Parthian Empire (c. 247 BCE–224 CE); principal eastern adversary of Rome for four centuries; Battle of Carrhae (53 BCE) — Rome's worst defeat since Cannae — permanently established the Euphrates boundary; preserved the Persian imperial tradition between Achaemenid and Sassanid eras.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Arsaces I's revolt against the Seleucid satrap of Parthia (c. 247 BCE) — exploiting Seleucid weakness during their wars with the Ptolemies and their loss of Bactria — established the Parthian kingdom in the power vacuum created by Seleucid imperial overextension",
            "The Parthian military system — horse-archery (the 'Parthian shot') and cataphract heavy cavalry — gave them a decisive tactical advantage in the open terrain of the Iranian plateau and Mesopotamia, enabling the conquest of the Seleucid empire's eastern provinces",
            "Mithridates I's conquests (171–138 BCE) — absorbing Media, Mesopotamia, and Elam from the Seleucids — transformed the Parthian kingdom into a world empire, establishing the dynasty's position as the primary successor to the Achaemenid Persian tradition"
        ],
        "effects": [
            "The Battle of Carrhae (53 BCE) — where Parthian cataphracts and horse-archers destroyed Crassus's legions — was one of Rome's most consequential military defeats, permanently establishing the Euphrates as the boundary between the Roman and Parthian worlds",
            "The Arsacid dynasty's preservation of the Iranian imperial tradition — the administrative structures, zoroastrian religious institutions, and royal iconography of the Achaemenid period — transmitted Persian civilisation across the Hellenistic interlude to the Sassanid revival",
            "The Parthian Empire's role as a Silk Road intermediary — taxing the overland trade between the Roman Empire and China — made it one of the wealthiest states of the ancient world and gave its rulers the resources to maintain their military challenge to Rome",
            "The Arsacid branch in Armenia (the Armenian Arsacids) continued to rule after the Parthian dynasty's fall (224 CE) — eventually converting to Christianity (301 CE) and creating the Armenian Apostolic Church, making Armenia the world's first Christian state"
        ],
        "relationships": [
            {"entity": "Arsaces I", "relationship": "FOUNDED_BY", "note": "Arsaces I (c. 247 BCE) led the Parni nomadic revolt against the Seleucid satrap — founding the Parthian kingdom"},
            {"entity": "Battle of Carrhae (53 BCE)", "relationship": "DECISIVE_VICTORY_AT", "note": "The Parthian defeat of Crassus at Carrhae (53 BCE) — Rome's worst defeat since Cannae — permanently established the Euphrates boundary"},
            {"entity": "Roman Republic/Empire", "relationship": "PRINCIPAL_EASTERN_ADVERSARY_OF", "note": "The Arsacid Parthians contested the Near East with Rome for four centuries — a geopolitical rivalry that shaped the ancient world's history"},
            {"entity": "Sassanid dynasty", "relationship": "OVERTHROWN_AND_SUCCEEDED_BY", "note": "Ardashir I (founder of the Sassanids) defeated and killed Artabanus IV (224 CE) — ending the Arsacid dynasty and beginning the Sassanid Persian Empire"},
            {"entity": "Silk Road", "relationship": "CONTROLLED_IRANIAN_SECTION_OF", "note": "The Arsacid Parthians controlled the Silk Road's Iranian section — acting as intermediaries between Rome and China and accumulating enormous commercial wealth"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 07 — {len(ENTITIES)} entities (Class 312: Central Asian, Armenian & Turkoman Dynasties)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
