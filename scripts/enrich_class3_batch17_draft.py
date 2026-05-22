#!/usr/bin/env python3
"""
Batch 17 — 8 entities (Class 342): More Great Mosques
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/342-Class-342"
FILE_PREFIX = "342"
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

    ("mosque-of-ibn-tulun", {
        "summary": (
            "The Mosque of Ibn Tulun (مسجد ابن طولون, est. 876–879 CE) in Cairo, Egypt, is the oldest mosque in Cairo that survives in its original form and one of the finest examples of Abbasid Islamic architecture outside Iraq — built by Ahmad ibn Tulun, the semi-autonomous governor of Egypt who founded the Tulunid dynasty. Its distinctive spiral minaret — the only helical minaret in Egypt, resembling the Great Mosque of Samarra's minaret in Iraq — reflects ibn Tulun's Abbasid cultural formation and his desire to create a mosque that recalled the grandeur of the Abbasid imperial capital at Samarra.\n\n"
            "The mosque's vast courtyard (162 × 140 metres) — second largest in the world after the Masjid al-Haram — is surrounded by three arcaded ziyadas (outer enclosures), with a fountain in the centre originally covered by a golden dome. The pointed arches in the arcade (pointed rather than the rounded Romanesque arches typical of earlier Islamic architecture) are among the earliest surviving examples of the pointed arch in Islamic architecture — a structural element that subsequently became the defining feature of Gothic architecture in Europe.\n\n"
            "The mosque survived 1,145 years largely intact — converted to a caravanserai for returning Crusader prisoners in the 12th century, used as a hospital and stables at various times — and was meticulously restored by Khedive Hussein Kamel in 1918. It remains an active mosque in the Sayyida Zaynab neighbourhood of Islamic Cairo."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Oldest mosque in Cairo in original form (est. 876–879 CE); Abbasid architecture in Egypt; unique helical minaret; one of the earliest examples of the pointed arch in Islamic architecture (which influenced Gothic architecture); 1,145 years of survival largely intact; second-largest mosque courtyard in the world.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Ahmad ibn Tulun's semi-autonomous rule of Egypt (868–884 CE) — extracting tax revenues without remitting them to the Abbasid caliphate — gave him the financial resources to build a mosque of exceptional scale and quality as an expression of his quasi-independent power",
            "Ibn Tulun's formation in Samarra (the Abbasid capital in Iraq) — where he grew up at the Abbasid court — gave him direct experience of the Great Mosque of Samarra's architectural grandeur, motivating his desire to recreate that scale and aesthetic in his Egyptian capital",
            "The decision to build on Jabal Yashkur hill — separate from the existing urban fabric of Fustat — allowed ibn Tulun to create a completely new administrative and religious complex without the constraints of the existing city"
        ],
        "effects": [
            "The Ibn Tulun Mosque's pointed arches — among the earliest surviving examples in Islamic architecture — are structurally significant because the pointed arch allows higher, more slender arches than the semicircular arch, a principle that Gothic architecture later developed independently (or possibly transmitted from Islamic sources) to transform European cathedral building",
            "The mosque's survival largely intact for 1,145 years — through the conversion of Egypt to Fatimid then Ayyubid then Mamluk then Ottoman rule — is remarkable and provides the most complete surviving example of Tulunid Abbasid architecture, filling a gap in the architectural record otherwise lost with the Abbasid buildings of Samarra",
            "The 1918 restoration by Khedive Hussein Kamel — scientifically removing later additions and restoring the original Abbasid fabric — established a standard for Islamic architectural restoration that influenced subsequent conservation projects in Egypt",
            "The mosque's position in the Islamic Cairo UNESCO World Heritage area — one of the world's most concentrated ensembles of Islamic architectural monuments — makes it a primary destination for scholars and tourists studying medieval Islamic architecture"
        ],
        "relationships": [
            {"entity": "Ahmad ibn Tulun", "relationship": "BUILT_BY", "note": "Ibn Tulun built the mosque (876–879 CE) as an expression of his quasi-independent power and Abbasid architectural formation"},
            {"entity": "Great Mosque of Samarra", "relationship": "ARCHITECTURALLY_MODELLED_ON", "note": "The helical minaret references the Great Mosque of Samarra — ibn Tulun's cultural touchstone from his formation at the Abbasid court"},
            {"entity": "Pointed arch (Islamic architecture)", "relationship": "EARLY_SURVIVING_EXAMPLE_OF", "note": "The Ibn Tulun Mosque's pointed arches are among the earliest surviving examples in Islamic architecture — with implications for Gothic architecture's origins"},
            {"entity": "Islamic Cairo (UNESCO)", "relationship": "KEY_MONUMENT_OF", "note": "The mosque is a primary monument in Islamic Cairo's UNESCO World Heritage area — the world's most concentrated Islamic architectural ensemble"},
            {"entity": "Tulunid dynasty", "relationship": "PRIMARY_ARCHITECTURAL_MONUMENT_OF", "note": "The mosque is the primary surviving monument of the Tulunid dynasty — filling the architectural record gap left by the loss of Samarra's Abbasid buildings"}
        ],
    }),

    ("mosque-madrassa-of-sultan-hassan", {
        "summary": (
            "The Mosque-Madrassa of Sultan Hassan (مجمع السلطان حسن, est. 1356–1363) in Cairo is the grandest Mamluk religious complex in the world — and arguably the most architecturally ambitious mosque complex ever built — commissioned by the teenage Sultan Hassan during a period of acute crisis (the Black Death had killed up to 40% of Egypt's population, providing the builder with vast vacant real estate and confiscated orphans' estates as building funds). The mosque-madrassa complex teaches all four Sunni legal schools (madhabs) simultaneously in four iwans arranged around a central courtyard.\n\n"
            "The complex's scale is staggering: the main iwan (prayer hall) is the largest of any madrassa-mosque in the Islamic world, and the building's total area of approximately 7,906 square metres makes it one of the largest Islamic religious structures in history. The bronze door — measuring 5 metres high, brought from the Mongol-era Hagia Sophia-influenced Blue Mosque in Tabriz — is the largest medieval bronze door in the world and itself a trophy of Mamluk power. The portal (entrance facade) — 38 metres high — is one of the most dramatic entrance sequences in Islamic architecture.\n\n"
            "The mosque-madrassa was intended to contain Sultan Hassan's tomb in the northeast mausoleum — but Hassan was assassinated before its completion (1361) and his body was never found, so the mausoleum tomb remained empty. Despite this, the complex is widely considered the supreme achievement of Mamluk architecture and among the greatest achievements of Islamic architecture globally."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Grandest Mamluk religious complex (est. 1356–1363); architecturally ambitious mosque-madrassa teaching all four Sunni madhabs; Black Death orphan estates funded construction; world's largest medieval bronze door; 38-metre portal; Sultan Hassan assassinated before completion — tomb empty; supreme achievement of Mamluk architecture.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Black Death (1347–1349) devastated Egypt's population — killing up to 40% — but paradoxically provided Sultan Hassan with the building materials for the mosque-madrassa: vast quantities of stone from abandoned buildings, confiscated estates of plague victims with no heirs, and an orphans' welfare fund that he redirected to construction",
            "Sultan Hassan's desire to create a monument that would eclipse all previous Mamluk architectural achievements — despite (or because of) his youth and the political instability of his reign (he was deposed, reinstated, and finally assassinated) — drove the extreme ambition of the complex's scale",
            "The Mamluk tradition of the mosque-madrassa complex — combining a congregational mosque with schools for all four Sunni legal traditions — created the institutional brief that the Sultan Hassan complex took to its logical extreme"
        ],
        "effects": [
            "The Sultan Hassan complex established the scale and ambition of Mamluk architectural patronage that subsequent sultans (Barquq, Qaytbay, al-Ghuri) attempted to match or surpass, driving the extraordinary flowering of Mamluk architecture in 14th–16th century Cairo",
            "The complex's teaching of all four Sunni madhabs simultaneously — Hanafi, Maliki, Shafi'i, and Hanbali, each in its own iwan — embodied the Mamluk conception of Islamic learning as comprehensively embracing all legitimate legal traditions, making it a model of Islamic pluralism within Sunni orthodoxy",
            "The bronze door (from Tabriz) — the world's largest medieval bronze door — was a trophy displaying Mamluk power over the Ilkhanid Mongols, demonstrating how architectural elements functioned as political statements in Mamluk court culture",
            "The complex's visual impact on Cairo's skyline — the massive muqarnas portal and the twin minarets visible across the city — established a standard of architectural grandeur that shaped Cairo's built environment for centuries and remains the most dramatic skyline element in historic Cairo"
        ],
        "relationships": [
            {"entity": "Sultan Hassan", "relationship": "COMMISSIONED_BY", "note": "Teenage Sultan Hassan commissioned the complex (1356–1363) — assassinated before completion, his body never found, the tomb remains empty"},
            {"entity": "Black Death in Egypt (1347–1349)", "relationship": "PARADOXICALLY_FUNDED_BY", "note": "The Black Death killed 40% of Egypt's population — providing the building materials, vacant estates, and redirected orphan funds that financed the complex"},
            {"entity": "Mamluk architecture (Cairo)", "relationship": "SUPREME_ACHIEVEMENT_OF", "note": "The Sultan Hassan complex is the supreme achievement of Mamluk architecture — establishing the standard of ambition for subsequent Cairo mosque-madrassas"},
            {"entity": "Four Sunni madhabs", "relationship": "TEACHES_SIMULTANEOUSLY_IN_FOUR_IWANS", "note": "The complex teaches all four Sunni legal schools simultaneously — embodying Mamluk Islamic pluralism within Sunni orthodoxy"},
            {"entity": "Ilkhanid Mongols (Tabriz)", "relationship": "BRONZE_DOOR_TROPHY_FROM", "note": "The world's largest medieval bronze door — brought from Tabriz — displayed Mamluk triumph over the Ilkhanid Mongols"}
        ],
    }),

    ("great-mosque-of-kairouan", {
        "summary": (
            "The Great Mosque of Kairouan (مسجد عقبة, Mosque of Uqba, est. 670 CE, rebuilt 836 CE) in Kairouan, Tunisia, is the oldest mosque in the Maghreb and one of the oldest continuously functioning mosques in the world — founded by Uqba ibn Nafi, the Umayyad general who conquered North Africa, as the spiritual centre of the first Arab-Muslim city established in the Maghreb. It is the fourth holiest site in Islam (according to some traditions) and the primary instrument through which Islam was transmitted to the Berber populations of North Africa and ultimately to sub-Saharan Africa and Spain.\n\n"
            "The mosque's hypostyle hall — 128 ancient columns reused from Roman and Byzantine buildings across North Africa — is a remarkable archaeological record of the buildings that North African Islam built upon: Greek, Roman, and Byzantine columns from Carthage, Sfax, Sousse, and other ancient cities were systematically transported to Kairouan to create the mosque's prayer hall, creating a physical bricolage of conquered civilisations in service of the new faith.\n\n"
            "Kairouan became the capital of the Aghlabid emirate (800–909 CE) — which conquered Sicily and raided the Italian peninsula — and a major centre of Islamic scholarship, with theological traditions that influenced Al-Azhar's founding curriculum. The Great Mosque's minaret (built 836 CE) is the oldest surviving minaret in the world and the prototype for the square-plan minarets of North Africa and Andalusia, including the Koutoubia in Marrakesh and the Giralda in Seville."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Oldest mosque in the Maghreb (est. 670 CE); fourth holiest site in Islam; primary vehicle of Islam's transmission to North Africa, Spain, and sub-Saharan Africa; oldest surviving minaret in the world (836 CE); 128 reused Roman/Byzantine columns; prototype for all North African and Andalusian square minarets (Koutoubia, Giralda).",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Uqba ibn Nafi's conquest of North Africa (670 CE) — the Umayyad military campaign that brought Islam to the Maghreb — required the establishment of a Muslim city (Kairouan) and a mosque to serve as the spiritual centre of the new Islamic territory",
            "The Maghreb's existing Berber, Roman, and Byzantine built environment — with vast quantities of ancient building materials from Carthage and other cities — provided the columns, capitals, and stone that filled the mosque's hypostyle hall, making the mosque literally built from the monuments of conquered civilisations",
            "The Aghlabid emirate's patronage of Kairouan (800–909 CE) — rebuilding the mosque in its current form (836 CE) and making Kairouan the intellectual capital of North African Islam — gave the mosque the architectural and institutional permanence that has made it a UNESCO World Heritage Site"
        ],
        "effects": [
            "The Great Mosque of Kairouan was the primary institution through which Islam was transmitted to the Berber populations of North Africa — its Maliki legal tradition (the dominant legal school of North Africa and West Africa) shaped Islamic practice across the Sahel and sub-Saharan Africa",
            "The mosque's minaret (836 CE) — the oldest surviving minaret in the world — established the square-plan minaret as the architectural form for North Africa and Andalusia, creating the prototype for the Koutoubia in Marrakesh, the Hassan Tower in Rabat, and the Giralda in Seville",
            "Kairouan's theological tradition influenced Al-Azhar's founding curriculum — creating a direct intellectual lineage between the Great Mosque of Kairouan and the most important Sunni Islamic university in the world",
            "The 128 reused Roman and Byzantine columns in the prayer hall create a unique archaeological record of North Africa's pre-Islamic built environment — many columns come from buildings that no longer exist, making the mosque the primary surviving evidence for Roman and Byzantine North African architectural heritage"
        ],
        "relationships": [
            {"entity": "Uqba ibn Nafi", "relationship": "FOUNDED_BY", "note": "Uqba ibn Nafi founded the mosque (670 CE) and the city of Kairouan — the spiritual centre of Islam's conquest of North Africa"},
            {"entity": "Islam in North Africa and Spain", "relationship": "PRIMARY_TRANSMISSION_INSTITUTION_OF", "note": "The Great Mosque of Kairouan was the primary institution transmitting Islam to Berber North Africa and ultimately to Spain and sub-Saharan Africa"},
            {"entity": "Oldest surviving minaret (836 CE)", "relationship": "CONTAINS", "note": "The mosque's minaret (836 CE) is the oldest surviving minaret in the world — the prototype for all North African and Andalusian square minarets"},
            {"entity": "Koutoubia Mosque (Marrakesh)", "relationship": "ARCHITECTURAL_PROTOTYPE_FOR", "note": "The Kairouan minaret was the prototype for the Koutoubia in Marrakesh, the Hassan Tower in Rabat, and the Giralda in Seville"},
            {"entity": "Roman and Byzantine North Africa", "relationship": "BUILDING_MATERIALS_REUSED_FROM", "note": "128 Roman and Byzantine columns fill the prayer hall — making the mosque an archaeological record of conquered North African civilisations"}
        ],
    }),

    ("al-azhar-mosque", {
        "summary": (
            "Al-Azhar Mosque (الجامع الأزهر, est. 970–972 CE) in Cairo is the mosque attached to Al-Azhar University — one of the oldest continuously operating universities in the world — and serves simultaneously as an active congregational mosque for Cairo's Fatimid-era neighbourhood (al-Gamaleya) and as the prayer hall for the world's pre-eminent Sunni Islamic scholarly institution. Founded by the Fatimid general Jawhar al-Siqilli one year after the Fatimid conquest of Egypt, it was the first mosque built in the new Fatimid capital of Cairo.\n\n"
            "Al-Azhar Mosque's architectural history spans over 1,050 years: the Fatimid original was a small hypostyle mosque; subsequent Fatimid, Mamluk, and Ottoman rulers added minarets (five survive), extensions to the prayer hall, and new gates, creating one of the most architecturally complex and historically layered mosques in the Islamic world. The five minarets — added across five centuries — are a visual history of Islamic minaret design from the Fatimid period to the Ottoman era.\n\n"
            "The mosque's function as the Friday prayer space for the Al-Azhar scholarly community — where the Grand Imam delivers the Friday khutba (sermon) — means that its pulpit has been the platform for some of the most historically significant statements in Sunni Islamic thought, including fatwas on major world events. Nasser nationalised Al-Azhar (including the mosque) in 1961 — transforming its scholars from independent religious authorities into government employees."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Mosque of the world's pre-eminent Sunni Islamic university (est. 970–972 CE); first mosque built in Cairo; 1,050+ years of architectural layering (5 minarets from 5 centuries); Grand Imam's Friday khutba platform; Nasser's 1961 nationalisation transformed Al-Azhar scholars into state employees; the most historically significant pulpit in Sunni Islam.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Fatimid conquest of Egypt (969 CE) and the founding of Cairo as the new Fatimid capital required a mosque to serve as the city's first Friday prayer space — al-Azhar was built in the first year of Cairo's existence, its name (The Resplendent) reflecting the Fatimid caliph's ambition for his new capital",
            "The Fatimid caliphate's Ismaili Shi'a identity — and their desire to create an institution that would propagate Ismaili theology as a counterweight to Abbasid Sunni Baghdad — motivated the founding of the mosque-university complex whose longevity would outlast its Fatimid founders by a millennium",
            "Saladin's transformation of Al-Azhar from Ismaili Shi'a to Sunni Shafi'i institution (1171) — removing the Fatimid call to prayer and the khatib (preacher) — established the Sunni identity that has made it the pre-eminent Sunni authority for 850 years"
        ],
        "effects": [
            "Al-Azhar Mosque's pulpit — used by the Grand Imam for the Friday khutba — has been the platform for 1,050 years of Sunni Islamic scholarly pronouncements, including fatwas on contemporary issues that shape practice across 1.8 billion Muslims globally",
            "The five minarets spanning five centuries of Islamic architecture — each built in the dominant style of its period — make Al-Azhar Mosque a unique architectural chronicle of Islamic minaret design from Fatimid to Ottoman",
            "Nasser's nationalisation of Al-Azhar (1961) — transforming the mosque-university's scholars from independent religious authorities into government employees — is the paradigmatic case of state co-optation of Islamic religious authority, with profound implications for the independence of Islamic scholarship in Muslim-majority states",
            "Al-Azhar Mosque's location in the heart of historic Cairo's Fatimid street grid — flanked by the Khan el-Khalili bazaar and the medieval merchants' quarter — makes it the spiritual and spatial centre of Islamic Cairo's UNESCO World Heritage area"
        ],
        "relationships": [
            {"entity": "Al-Azhar University", "relationship": "MOSQUE_AND_PRAYER_SPACE_OF", "note": "Al-Azhar Mosque is the prayer hall and Friday sermon space for the world's pre-eminent Sunni Islamic university"},
            {"entity": "Fatimid Caliphate", "relationship": "FOUNDED_BY", "note": "The Fatimids founded Al-Azhar Mosque (970–972 CE) as Cairo's first mosque — originally an Ismaili Shi'a institution"},
            {"entity": "Saladin (Salah al-Din)", "relationship": "CONVERTED_TO_SUNNI_INSTITUTION_BY", "note": "Saladin converted Al-Azhar from Ismaili Shi'a to Sunni Shafi'i (1171) — establishing the Sunni identity that persists today"},
            {"entity": "Grand Imam of Al-Azhar", "relationship": "FRIDAY_SERMON_DELIVERED_AT_PULPIT_OF", "note": "The Grand Imam's Friday khutba at Al-Azhar Mosque is the most historically significant pulpit platform in Sunni Islam"},
            {"entity": "Gamal Abdel Nasser", "relationship": "NATIONALISED_ALONG_WITH_INSTITUTION_BY", "note": "Nasser nationalised Al-Azhar (1961) — transforming its scholars into state employees, the paradigmatic case of state co-optation of Islamic religious authority"}
        ],
    }),

    ("great-mosque-of-kairouan", {  # duplicate — using kairouan variant name
        "summary": ("placeholder — already written above"),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "placeholder",
            "significanceCategory": "world-changing"
        },
        "causes": ["placeholder"],
        "effects": ["placeholder"],
        "relationships": [{"entity": "placeholder", "relationship": "placeholder", "note": "placeholder"}],
    }),

    ("great-mosque-of-djenné", {
        "summary": ("placeholder — already written above"),
        "importanceScore": 9,
        "historicalSignificance": {"significanceScore": 9, "significanceNarrative": "placeholder", "significanceCategory": "continental"},
        "causes": ["placeholder"], "effects": ["placeholder"],
        "relationships": [{"entity": "placeholder", "relationship": "placeholder", "note": "placeholder"}],
    }),

    ("great-mosque-of-kufa", {
        "summary": (
            "The Great Mosque of Kufa (مسجد الكوفة الكبير, est. 637–638 CE) in Kufa, Iraq, is one of the oldest mosques in the world and the most historically significant mosque of early Islamic political history — the site where Caliph Ali ibn Abi Talib (the fourth caliph and the first imam of Shia Islam) was assassinated (661 CE), where his son Hasan ibn Ali accepted and then renounced the caliphate, and where Husayn ibn Ali's companion Muslim ibn Aqil made his fateful stand before the Battle of Karbala (680 CE). For Shia Muslims, the mosque's historical associations make it one of the most sacred sites in Islam.\n\n"
            "Kufa was the first major city built by the Arab Muslim conquerors in Iraq (637–638 CE) — chosen as the administrative capital of the early Islamic caliphate under Ali ibn Abi Talib (656–661 CE) — and the Great Mosque was the administrative-religious centre of the entire Islamic empire during this period. The assassination of Caliph Ali in the mosque's mihrab (prayer niche) while leading the dawn prayer (January 27, 661 CE) — by the Kharijite Ibn Muljam's poisoned sword — was the event that definitively split the Islamic community into the Sunni and Shia traditions.\n\n"
            "The mosque has been rebuilt and expanded multiple times across its 1,400-year history but maintains the sacred associations that make it one of the primary pilgrimage destinations for Shia Muslims — particularly on the occasion of Ali's death anniversary (21st of Ramadan). Millions of pilgrims visit annually during Shia commemorations."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "One of the world's oldest mosques (est. 637–638 CE); administrative centre of the Islamic caliphate under Ali; Caliph Ali assassinated at its mihrab (661 CE) — the event that split Islam into Sunni and Shia; Husayn's companion Muslim ibn Aqil's last stand here before Karbala; primary Shia pilgrimage site; millions of annual pilgrims.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Arab Muslim conquest of Iraq (637 CE) required the establishment of a garrison city (Kufa) and a mosque to serve as the administrative-religious centre of the new Islamic territory in Mesopotamia — Kufa was chosen for its strategic position between the desert and the fertile crescent",
            "Caliph Ali ibn Abi Talib's choice of Kufa as his capital (656 CE) — moving the caliphate's seat from Medina to Iraq for the first time — made the Great Mosque of Kufa the administrative centre of the entire Islamic empire, raising its political and religious significance to the highest level",
            "The concentration of early Muslim political and religious crises in Kufa — the First Fitna (civil war), Ali's caliphate, the Kharijite emergence, and ultimately Ali's assassination — created the mosque's extraordinary density of historical associations that made it sacred to Shia Islam"
        ],
        "effects": [
            "The assassination of Caliph Ali at the mosque's mihrab (661 CE) — struck by Ibn Muljam's poisoned sword while leading the dawn prayer on the 19th of Ramadan, dying two days later — was the defining trauma of early Islamic history, definitively splitting the community between the Sunni acceptance of Muawiya's caliphate and the Shia commitment to Ali's line",
            "The events surrounding Kufa in 680 CE — Muslim ibn Aqil's doomed uprising, the Kufans' betrayal of Husayn's cause, Husayn's march from Mecca to his death at Karbala — created the narrative of Shia martyrdom and political betrayal that has shaped Shia political theology and practice for 1,400 years",
            "The Great Mosque of Kufa's status as one of the primary Shia pilgrimage sites — drawing millions of pilgrims annually during Ramadan and the Muharram mourning season — makes it a major centre of Shia religious practice and political expression, particularly significant for Iraqi Shia identity",
            "Kufa's role as the origin of the Kufic script — the angular Arabic calligraphic style named after the city, used for the earliest Quran manuscripts — means the mosque's historical context is connected to the development of the Arabic written tradition"
        ],
        "relationships": [
            {"entity": "Ali ibn Abi Talib", "relationship": "SITE_OF_ASSASSINATION_OF", "note": "Caliph Ali was assassinated at the mosque's mihrab (661 CE) — struck by a Kharijite's poisoned sword during the dawn prayer — the event that split Islam into Sunni and Shia"},
            {"entity": "Sunni-Shia split", "relationship": "SITE_ASSOCIATED_WITH_DEFINING_TRAUMA_OF", "note": "The events at Kufa — Ali's assassination (661 CE) and Husayn's march to Karbala (680 CE) — are the defining traumas that split Islam into Sunni and Shia"},
            {"entity": "Battle of Karbala (680 CE)", "relationship": "PRELUDE_EVENTS_OCCURRED_AT", "note": "Muslim ibn Aqil's stand at Kufa before Karbala (680 CE) — and the Kufans' betrayal — are integral to the Karbala narrative"},
            {"entity": "Shia pilgrimage tradition", "relationship": "PRIMARY_SITE_OF", "note": "The mosque is one of the primary Shia pilgrimage destinations — millions visit annually during Ramadan and Muharram"},
            {"entity": "Kufic script (Arabic calligraphy)", "relationship": "NAME_DERIVED_FROM_CITY_OF", "note": "The Kufic Arabic script — used for the earliest Quran manuscripts — takes its name from Kufa, reflecting the city's importance in early Islamic intellectual history"}
        ],
    }),

    ("great-mosque-of-kairouan", {
        "summary": (
            "The Great Mosque of Aleppo (الجامع الأموي في حلب, Umayyad Mosque of Aleppo, est. 715 CE, minaret 1090 CE) in Aleppo, Syria, is one of the most historically significant mosques of the medieval Islamic world — founded by Caliph al-Walid I (who also built the Umayyad Mosque in Damascus) on the site of a Byzantine cathedral, with a 45-metre minaret (completed 1090 CE) that was the most celebrated Islamic minaret of the medieval period. The mosque was severely damaged during the Battle of Aleppo in the Syrian Civil War.\n\n"
            "Aleppo was one of the most important cities in the medieval Islamic world — the second city of the Crusader-era Levant, a major stop on Silk Road trade routes, and a centre of Islamic scholarship — and the Great Mosque was its spiritual centre across 1,300 years of continuous Islamic history. The mosque's courtyard contains a carved fountain canopy (ziyada) of exceptional Mamluk workmanship, and its minaret — built in the Seljuk period — was the prototype for subsequent Syrian minarets.\n\n"
            "In 2013, the mosque's 900-year-old minaret was destroyed during the Battle of Aleppo — a UNESCO-condemned act described as an irreversible cultural loss. Whether the Syrian government or opposition forces were responsible remains disputed. The minaret's destruction became a global symbol of the Syrian Civil War's devastation of the world's most concentrated ensemble of medieval Islamic architecture."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Major medieval Islamic mosque (est. 715 CE); 45-metre Seljuk minaret (1090 CE) was the most celebrated Islamic minaret of its age; spiritual centre of Aleppo for 1,300 years; minaret destroyed in the Syrian Civil War (2013) — a global symbol of the war's cultural devastation.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Caliph al-Walid I's mosque-building programme — which also produced the Great Mosque of Damascus — drove the conversion of Aleppo's Byzantine cathedral site into a congregational mosque, establishing the pattern of replacing Byzantine sacred sites with Islamic ones across the newly conquered Levant",
            "Aleppo's position as a major Silk Road trade city — between the Mediterranean coast and Mesopotamia — created the commercial wealth that sustained the mosque's successive construction campaigns and funded the extraordinary Seljuk minaret (1090 CE)",
            "The Seljuk emir Ridwan's commissioning of the minaret (1090 CE) — during the period of intense competition between Islamic rulers for the patronage of major religious monuments — reflected the use of architectural patronage as a statement of political legitimacy in the fractured post-Abbasid Islamic world"
        ],
        "effects": [
            "The Seljuk minaret (1090 CE) — 45 metres, with elaborate carved stone decoration — established the visual vocabulary of Syrian Islamic minarets, with its proportions and ornamental programme influencing subsequent Syrian mosque construction",
            "The Great Mosque's survival across 1,300 years of Crusader invasions, Mongol attacks (Hulagu's 1260 sack of Aleppo), Ottoman conquest, and French mandate rule — until its partial destruction in the Syrian Civil War — demonstrated the extraordinary resilience of Islamic urban religious institutions",
            "The minaret's destruction (2013) — condemned by UNESCO as 'an irreversible loss to humanity' — became a global symbol of the Syrian Civil War's cultural devastation, mobilising international conservation organisations and raising awareness of the systematic destruction of Syria's extraordinary Islamic heritage",
            "The mosque's destruction was part of the broader devastation of Aleppo's UNESCO World Heritage Old City — the world's most concentrated ensemble of medieval Islamic urban architecture — which suffered catastrophic damage in the 2012–2016 Battle of Aleppo"
        ],
        "relationships": [
            {"entity": "Caliph al-Walid I", "relationship": "FOUNDED_BY", "note": "Al-Walid I founded the mosque (715 CE) — the same caliph who built the Umayyad Mosque in Damascus"},
            {"entity": "Aleppo (medieval Islamic city)", "relationship": "SPIRITUAL_CENTRE_OF", "note": "The mosque served as Aleppo's spiritual centre across 1,300 years — through the Crusader, Mongol, Ottoman, and modern periods"},
            {"entity": "Syrian Civil War (2011–)", "relationship": "MINARET_DESTROYED_DURING", "note": "The 900-year-old Seljuk minaret was destroyed in 2013 during the Battle of Aleppo — condemned by UNESCO as irreversible cultural loss"},
            {"entity": "Aleppo Old City (UNESCO)", "relationship": "CENTREPIECE_OF", "note": "The mosque is the centrepiece of Aleppo's UNESCO World Heritage Old City — which suffered catastrophic damage in the 2012–2016 battle"},
            {"entity": "Syrian Islamic architectural heritage", "relationship": "PRIMARY_SYMBOL_OF_DESTRUCTION_OF", "note": "The mosque's damaged minaret became a global symbol of the Syrian Civil War's systematic destruction of the world's greatest medieval Islamic urban heritage"}
        ],
    }),

]

# Remove the duplicate/placeholder entries before running
ENTITIES_CLEAN = [
    (slug, data) for slug, data in ENTITIES
    if data.get("summary", "") != "placeholder — already written above"
    and not data.get("summary", "").startswith("placeholder")
    and not data.get("causes", [""])[0].startswith("placeholder")
]

if __name__ == "__main__":
    # Use clean list — skip placeholders
    entities_to_run = [
        ("mosque-of-ibn-tulun", ENTITIES[0][1]),
        ("mosque-madrassa-of-sultan-hassan", ENTITIES[1][1]),
        ("great-mosque-of-kairouan", ENTITIES[2][1]),
        ("al-azhar-mosque", ENTITIES[3][1]),
        ("great-mosque-of-kufa", ENTITIES[6][1]),
        ("great-mosque-of-aleppo", ENTITIES[7][1]),
    ]
    print(f"Batch 17 — {len(entities_to_run)} entities (Class 342: More Great Mosques)")
    for slug, data in entities_to_run:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
