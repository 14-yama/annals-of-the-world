#!/usr/bin/env python3
"""
Batch 17 — 8 entities (Class 342): Great Mosques continued
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
            "The Mosque of Ibn Tulun (مسجد ابن طولون, est. 876–879 CE) in Cairo is the oldest mosque in Cairo surviving in its original form and a masterwork of Abbasid Islamic architecture — built by Ahmad ibn Tulun, the semi-autonomous governor who founded the Tulunid dynasty, in a deliberate echo of the Great Mosque of Samarra where he had grown up at the Abbasid court. The mosque's distinctive helical minaret — the only spiral minaret in Egypt — is modelled on Samarra's famous minaret and declares ibn Tulun's Abbasid cultural allegiances.\n\n"
            "The mosque's vast courtyard (162 × 140 metres) is surrounded by three arcaded ziyadas (outer enclosures). The pointed arches in the arcade — among the earliest surviving examples in Islamic architecture — are structurally significant: the pointed arch allows higher, more slender arches than the semicircular arch, a principle that Gothic architecture later independently developed (or possibly transmitted from Islamic sources) to transform European cathedral building.\n\n"
            "The mosque survived 1,145 years largely intact — converted to a caravanserai, hospital, and stables at various times — and was meticulously restored by Khedive Hussein Kamel in 1918. Its 128 ancient columns reused from Roman and Byzantine buildings across North Africa create a physical bricolage of conquered civilisations in service of the new faith. Remarkably well preserved, it remains an active mosque in Cairo's Sayyida Zaynab district."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Oldest Cairo mosque in original form (est. 876–879 CE); Abbasid architectural masterwork; unique helical minaret; early surviving pointed arches (with implications for Gothic architecture origins); 1,145 years largely intact; primary evidence for Tulunid architecture.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Ahmad ibn Tulun's semi-autonomous rule of Egypt (868–884 CE) — accumulating tax revenues without remitting them to the Abbasid caliphate — gave him the financial resources to build a mosque of exceptional scale as an expression of his quasi-independent power",
            "Ibn Tulun's formation in Samarra (the Abbasid capital in Iraq) — where he grew up at court — gave him direct experience of the Great Mosque of Samarra's grandeur, motivating his desire to recreate that scale and aesthetic in his Egyptian capital al-Qata'i",
            "The decision to build on Jabal Yashkur hill — separate from the existing urban fabric of Fustat — allowed ibn Tulun to create a completely new administrative and religious complex without constraints of the existing city"
        ],
        "effects": [
            "The mosque's pointed arches — among the earliest surviving examples in Islamic architecture — demonstrate that the pointed arch was present in the Islamic world before its widespread adoption in Gothic architecture, contributing to scholarly debate about the transmission of this crucial structural innovation from Islamic to European building practice",
            "The mosque's 1,145-year survival largely intact provides the most complete surviving example of Tulunid Abbasid architecture, filling a gap in the architectural record otherwise lost with the Abbasid buildings of Samarra (most of which no longer survive)",
            "The 128 reused Roman and Byzantine columns in the prayer hall create a unique archaeological record of North Africa's pre-Islamic built environment — many columns come from buildings that no longer exist, making the mosque the primary surviving evidence for Roman and Byzantine North African architectural heritage",
            "The 1918 restoration by Khedive Hussein Kamel — scientifically removing later additions and restoring the original Abbasid fabric — established a standard for Islamic architectural restoration that influenced subsequent conservation projects in Egypt"
        ],
        "relationships": [
            {"entity": "Ahmad ibn Tulun", "relationship": "BUILT_BY", "note": "Ibn Tulun built the mosque (876–879 CE) as an expression of his quasi-independent power and Abbasid cultural formation"},
            {"entity": "Great Mosque of Samarra", "relationship": "HELICAL_MINARET_MODELLED_ON", "note": "The spiral minaret references the Great Mosque of Samarra — ibn Tulun's cultural touchstone from the Abbasid court"},
            {"entity": "Pointed arch (Islamic/Gothic architecture)", "relationship": "EARLY_SURVIVING_EXAMPLE_OF", "note": "The Ibn Tulun Mosque's pointed arches (876–879 CE) are among the earliest surviving examples — relevant to the debate about Gothic architecture's origins"},
            {"entity": "Islamic Cairo (UNESCO)", "relationship": "KEY_MONUMENT_OF", "note": "The mosque is a primary monument in Islamic Cairo's UNESCO World Heritage area"},
            {"entity": "Tulunid dynasty", "relationship": "PRIMARY_ARCHITECTURAL_MONUMENT_OF", "note": "The most complete surviving monument of the Tulunid dynasty — filling the gap left by the destruction of Samarra's Abbasid buildings"}
        ],
    }),

    ("mosque-madrassa-of-sultan-hassan", {
        "summary": (
            "The Mosque-Madrassa of Sultan Hassan (مجمع السلطان حسن, est. 1356–1363) in Cairo is the grandest Mamluk religious complex ever built — commissioned by the teenage Sultan Hassan in a period of acute crisis, when the Black Death had killed up to 40% of Egypt's population, providing him with vast confiscated orphans' estates and abandoned real estate as building funds. The complex teaches all four Sunni legal schools (madhabs) simultaneously in four iwans arranged around a central courtyard, embodying the Mamluk conception of comprehensive Islamic learning.\n\n"
            "The scale is extraordinary: the main iwan (prayer hall) is the largest of any madrassa-mosque in the Islamic world; the total area is approximately 7,906 square metres; the portal — 38 metres high — is one of the most dramatic entrance sequences in Islamic architecture; the bronze door (5 metres high, brought from the Mongol-era city of Tabriz) is the largest medieval bronze door in the world. These proportions reflect a building that was designed not merely to surpass but to overwhelm.\n\n"
            "Sultan Hassan was assassinated in 1361 before the complex's completion, and his body was never found — so the northeast mausoleum, built to contain his tomb, remained empty. Despite this, the complex is universally regarded as the supreme achievement of Mamluk architecture. Its visual impact on Cairo's skyline — the massive muqarnas portal visible across the city — established the standard for Mamluk architectural ambition that subsequent sultans attempted to match."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Grandest Mamluk religious complex (est. 1356–1363); Black Death orphan estates funded construction; world's largest medieval bronze door; 38-metre portal; teaches all four Sunni madhabs; Sultan Hassan assassinated before completion — empty tomb; supreme achievement of Mamluk architecture.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Black Death (1347–1349) devastated Egypt — killing up to 40% of the population — but paradoxically provided Sultan Hassan with building funds: confiscated estates of plague victims with no heirs, vacant properties, and a redirected orphans' welfare fund",
            "Sultan Hassan's desire to create a monument that would eclipse all previous Mamluk architectural achievements — despite his youth and political instability (deposed, reinstated, then assassinated) — drove the extreme scale ambition",
            "The Mamluk tradition of mosque-madrassa complexes teaching all four Sunni legal schools simultaneously created the institutional brief that the Sultan Hassan complex took to its most ambitious extreme"
        ],
        "effects": [
            "The Sultan Hassan complex established the scale and ambition of Mamluk architectural patronage that subsequent sultans (Barquq, Qaytbay, al-Ghuri) attempted to match, driving the extraordinary flowering of Mamluk architecture in 14th–16th century Cairo",
            "Teaching all four Sunni madhabs simultaneously — Hanafi, Maliki, Shafi'i, and Hanbali, each in its own iwan — embodied a model of Islamic pluralism within Sunni orthodoxy that influenced subsequent Islamic educational institutions",
            "The bronze door from Tabriz — the world's largest medieval bronze door — was a trophy displaying Mamluk power over the Ilkhanid Mongols, demonstrating how architectural elements functioned as political statements in Mamluk court culture",
            "The complex's visual impact — the massive muqarnas portal and twin minarets visible across Cairo — established a standard of grandeur that defined the Mamluk approach to monumental architecture and shaped Cairo's built environment for centuries"
        ],
        "relationships": [
            {"entity": "Sultan Hassan", "relationship": "COMMISSIONED_BY", "note": "Teenage Sultan Hassan commissioned the complex (1356–1363) — assassinated before completion, body never found, the tomb remains empty"},
            {"entity": "Black Death in Egypt (1347–1349)", "relationship": "PARADOXICALLY_FUNDED_BY", "note": "The Black Death provided the building funds through confiscated estates, vacant properties, and redirected orphan welfare funds"},
            {"entity": "Mamluk architecture (Cairo)", "relationship": "SUPREME_ACHIEVEMENT_OF", "note": "The Sultan Hassan complex is the supreme achievement of Mamluk architecture — establishing the standard for subsequent Cairo mosque-madrassas"},
            {"entity": "Four Sunni madhabs", "relationship": "SIMULTANEOUSLY_TEACHES_IN_FOUR_IWANS", "note": "Teaching all four Sunni legal schools simultaneously — each in its own iwan — embodies Mamluk Islamic pluralism within Sunni orthodoxy"},
            {"entity": "Ilkhanid Mongols (Tabriz)", "relationship": "BRONZE_DOOR_TROPHY_BROUGHT_FROM", "note": "The world's largest medieval bronze door — brought from Tabriz — displayed Mamluk triumph over the Ilkhanid Mongols"}
        ],
    }),

    ("great-mosque-of-kairouan", {
        "summary": (
            "The Great Mosque of Kairouan (مسجد عقبة, Mosque of Uqba, est. 670 CE, rebuilt 836 CE) in Kairouan, Tunisia, is the oldest mosque in the Maghreb and one of the oldest continuously functioning mosques in the world — founded by Uqba ibn Nafi, the Umayyad general who conquered North Africa, as the spiritual centre of the first Arab-Muslim city established in the Maghreb. Some Islamic traditions designate Kairouan the fourth holiest site in Islam, and it was the primary institution through which Islam spread across North Africa to Spain and sub-Saharan Africa.\n\n"
            "The mosque's hypostyle hall contains 128 ancient columns reused from Roman and Byzantine buildings across North Africa — from Carthage, Sfax, Sousse, and other ancient cities — creating a physical bricolage of conquered civilisations in service of the new faith. The minaret (built 836 CE) is the oldest surviving minaret in the world and the prototype for the square-plan minarets of North Africa and Andalusia, including the Koutoubia in Marrakesh, the Hassan Tower in Rabat, and the Giralda in Seville.\n\n"
            "Kairouan became the capital of the Aghlabid emirate (800–909 CE), which conquered Sicily and raided the Italian peninsula. The city's theological tradition influenced Al-Azhar's founding curriculum. The mosque was declared a UNESCO World Heritage Site in 1988, and its Maliki legal tradition — the dominant school of North Africa and West Africa — has shaped Islamic practice across the Sahel and sub-Saharan Africa for 1,200 years."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Oldest mosque in the Maghreb (est. 670 CE); fourth holiest site in Islam (some traditions); primary vehicle of Islam's spread to North Africa, Spain, and sub-Saharan Africa; oldest surviving minaret in the world (836 CE); 128 reused Roman/Byzantine columns; prototype for all North African and Andalusian square minarets.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Uqba ibn Nafi's Umayyad conquest of North Africa (670 CE) required establishing a Muslim city (Kairouan) and a mosque to serve as the spiritual centre of the new Islamic territory",
            "The Maghreb's rich pre-existing built environment — vast quantities of ancient building materials from Carthage, Sfax, and other Roman cities — provided the columns, capitals, and stone that filled the mosque's hypostyle hall",
            "The Aghlabid emirate's patronage of Kairouan (800–909 CE) — rebuilding the mosque in its current form (836 CE) and making Kairouan the intellectual capital of North African Islam — gave the mosque the architectural and institutional permanence that has sustained it for 1,200 years"
        ],
        "effects": [
            "The Great Mosque of Kairouan was the primary institution through which Islam spread to Berber North Africa — its Maliki legal tradition shaping Islamic practice across the Sahel and sub-Saharan Africa for twelve centuries",
            "The minaret (836 CE) — the oldest surviving minaret in the world — established the square-plan minaret as the architectural prototype for North Africa and Andalusia: the Koutoubia in Marrakesh, the Hassan Tower in Rabat, and the Giralda in Seville all derive from this prototype",
            "Kairouan's theological tradition influenced Al-Azhar's founding curriculum, creating a direct intellectual lineage between the oldest Maghrebi mosque and the pre-eminent Sunni Islamic university",
            "The 128 reused Roman and Byzantine columns create a unique archaeological record of North Africa's pre-Islamic built environment — many from buildings no longer standing, making the mosque the primary surviving evidence for Roman and Byzantine North African architectural heritage"
        ],
        "relationships": [
            {"entity": "Uqba ibn Nafi", "relationship": "FOUNDED_BY", "note": "Uqba ibn Nafi founded the mosque (670 CE) and the city of Kairouan — the first Arab-Muslim city in the Maghreb"},
            {"entity": "Islam in North Africa and Spain", "relationship": "PRIMARY_TRANSMISSION_INSTITUTION_OF", "note": "The Great Mosque was the primary institution transmitting Islam to Berber North Africa and ultimately to Spain and sub-Saharan Africa"},
            {"entity": "Oldest surviving minaret (836 CE)", "relationship": "CONTAINS", "note": "The mosque's minaret (836 CE) is the oldest surviving minaret — prototype for all North African and Andalusian square minarets"},
            {"entity": "Koutoubia Mosque (Marrakesh)", "relationship": "ARCHITECTURAL_PROTOTYPE_FOR", "note": "The Kairouan minaret was the prototype for the Koutoubia in Marrakesh, the Hassan Tower in Rabat, and the Giralda in Seville"},
            {"entity": "Al-Azhar University", "relationship": "THEOLOGICAL_TRADITION_INFLUENCED_CURRICULUM_OF", "note": "Kairouan's theological tradition influenced Al-Azhar's founding curriculum — linking the oldest Maghrebi mosque to the pre-eminent Sunni university"}
        ],
    }),

    ("al-azhar-mosque", {
        "summary": (
            "Al-Azhar Mosque (الجامع الأزهر, est. 970–972 CE) in Cairo is the mosque attached to Al-Azhar University — one of the oldest continuously operating universities in the world — and serves both as an active congregational mosque and as the prayer hall for Sunni Islam's pre-eminent scholarly institution. Founded by the Fatimid general Jawhar al-Siqilli one year after the Fatimid conquest of Egypt, it was the first mosque built in the new Fatimid capital of Cairo, its name (The Resplendent) reflecting the Fatimid caliph's vision for his new dynasty.\n\n"
            "Al-Azhar's architectural history spans 1,050+ years: the small Fatimid original was continuously enlarged by Fatimid, Ayyubid, Mamluk, and Ottoman rulers, with five minarets from five different centuries creating a visual chronicle of Islamic minaret design. Saladin converted it from Ismaili Shi'a to Sunni Shafi'i institution (1171) — removing the Fatimid call to prayer — establishing the Sunni identity that has made it Islam's pre-eminent authority for 850 years.\n\n"
            "The mosque's pulpit — where the Grand Imam delivers the Friday khutba — has been the platform for 1,050 years of Sunni Islamic scholarly pronouncements, shaping practice across 1.8 billion Muslims globally. Nasser nationalised Al-Azhar in 1961 — transforming its scholars from independent religious authorities into government employees — a transformation that represents the paradigmatic case of state co-optation of Islamic religious authority in the modern era."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Mosque of the world's pre-eminent Sunni Islamic university (est. 970–972 CE); first mosque built in Cairo; 1,050+ years; 5 minarets from 5 centuries; Saladin's Sunni conversion (1171); Grand Imam's Friday khutba platform; Nasser's 1961 nationalisation transformed scholars into state employees.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Fatimid conquest of Egypt (969 CE) and the founding of Cairo required a mosque as the city's first Friday prayer space — al-Azhar was built in the first year of Cairo's existence",
            "The Fatimid caliphate's Ismaili Shi'a identity — their desire to create an institution propagating Ismaili theology as a counterweight to Abbasid Sunni Baghdad — motivated the mosque-university complex whose longevity would outlast its founders by a millennium",
            "Saladin's conversion of Al-Azhar from Ismaili Shi'a to Sunni Shafi'i (1171) — removing the Fatimid call to prayer — established the Sunni identity that has made it the pre-eminent Sunni authority for 850 years"
        ],
        "effects": [
            "Al-Azhar Mosque's pulpit — used by the Grand Imam for the Friday khutba — has been the platform for 1,050 years of Sunni Islamic scholarly pronouncements, including fatwas on contemporary issues that shape practice across 1.8 billion Muslims globally",
            "The five minarets from five centuries — each in the dominant style of its period — make Al-Azhar Mosque a unique architectural chronicle of Islamic minaret design from Fatimid to Ottoman",
            "Nasser's nationalisation of Al-Azhar (1961) — transforming the mosque-university's scholars into government employees — is the paradigmatic case of state co-optation of Islamic religious authority, with profound implications for the independence of Islamic scholarship in Muslim-majority states",
            "Al-Azhar Mosque's location in historic Cairo's Fatimid street grid — flanked by the Khan el-Khalili bazaar — makes it the spiritual and spatial centre of Islamic Cairo's UNESCO World Heritage area"
        ],
        "relationships": [
            {"entity": "Al-Azhar University", "relationship": "MOSQUE_AND_PRAYER_SPACE_OF", "note": "Al-Azhar Mosque is the prayer hall and Friday sermon space for the world's pre-eminent Sunni Islamic university"},
            {"entity": "Fatimid Caliphate", "relationship": "FOUNDED_BY", "note": "The Fatimids founded Al-Azhar Mosque (970–972 CE) as Cairo's first mosque — originally Ismaili Shi'a"},
            {"entity": "Saladin (Salah al-Din)", "relationship": "CONVERTED_TO_SUNNI_INSTITUTION_BY", "note": "Saladin converted Al-Azhar from Ismaili Shi'a to Sunni Shafi'i (1171) — establishing the Sunni identity that persists today"},
            {"entity": "Grand Imam of Al-Azhar", "relationship": "FRIDAY_SERMON_DELIVERED_AT_PULPIT_OF", "note": "The Grand Imam's Friday khutba at Al-Azhar is the most significant pulpit platform in Sunni Islam"},
            {"entity": "Gamal Abdel Nasser", "relationship": "NATIONALISED_INSTITUTION_OF_BY", "note": "Nasser nationalised Al-Azhar (1961) — transforming scholars into state employees, the paradigmatic modern case of state co-optation of Islamic religious authority"}
        ],
    }),

    ("great-mosque-of-kufa", {
        "summary": (
            "The Great Mosque of Kufa (مسجد الكوفة الكبير, est. 637–638 CE) in Kufa, Iraq, is one of the oldest mosques in the world and the most historically significant mosque of early Islamic political history — the administrative-religious centre of the Islamic caliphate under Caliph Ali ibn Abi Talib (656–661 CE), and the site of Ali's assassination (661 CE) that definitively split Islam into the Sunni and Shia traditions. For Shia Muslims, it is among the holiest sites on earth.\n\n"
            "Kufa was the first major city built by Arab Muslim conquerors in Iraq (637–638 CE) — chosen as the administrative capital of the early caliphate under Ali. The Great Mosque served as the centre of the entire Islamic empire during this period. The assassination of Caliph Ali at the mosque's mihrab (prayer niche) on the 19th of Ramadan 661 CE — struck by the Kharijite Ibn Muljam's poisoned sword during the dawn prayer — was the defining trauma of early Islamic history.\n\n"
            "In 680 CE, the mosque was also the scene of events leading to the Battle of Karbala: Muslim ibn Aqil, Husayn ibn Ali's envoy, made his doomed last stand near the mosque before the Kufan population — who had invited Husayn — abandoned him to the Umayyad governor. The sense of betrayal that event created has defined Shia political theology for 1,400 years. The mosque draws millions of Shia pilgrims annually during Ramadan and the Muharram mourning season."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "One of the world's oldest mosques (est. 637–638 CE); administrative centre of the Islamic caliphate under Ali; Ali assassinated at its mihrab (661 CE) — the event splitting Islam into Sunni and Shia; Karbala prelude events here (680 CE); primary Shia pilgrimage site; millions of annual pilgrims.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Arab Muslim conquest of Iraq (637 CE) required establishing a garrison city (Kufa) and mosque as the administrative-religious centre of the new territory — Kufa's strategic position between desert and fertile crescent made it the natural choice",
            "Caliph Ali's choice of Kufa as his capital (656 CE) — moving the caliphate's seat from Medina to Iraq — made the Great Mosque of Kufa the administrative centre of the entire Islamic empire, raising its political and religious significance to the highest level",
            "The concentration of early Muslim political crises in Kufa — the First Fitna, Ali's caliphate, the Kharijite emergence, and Ali's assassination — created the mosque's extraordinary density of historical associations sacred to Shia Islam"
        ],
        "effects": [
            "The assassination of Caliph Ali at the mosque's mihrab (661 CE) — dying two days after being struck by Ibn Muljam's poisoned sword during the dawn prayer — definitively split the Islamic community between Sunni acceptance of Muawiya's caliphate and Shia commitment to Ali's line",
            "The events at Kufa in 680 CE — the Kufan invitation to Husayn, Muslim ibn Aqil's doomed uprising, and the community's betrayal — created the narrative of Shia martyrdom and political abandonment that has shaped Shia political theology and practice for 1,400 years",
            "The Great Mosque of Kufa's status as a primary Shia pilgrimage site — drawing millions of pilgrims annually during Ramadan and the Muharram mourning season — makes it a major centre of Shia religious and political expression, particularly significant for Iraqi Shia identity",
            "Kufa's role as the origin of the Kufic script — the angular Arabic calligraphic style used for the earliest Quran manuscripts — connects the mosque's historical context to the development of the Arabic written tradition"
        ],
        "relationships": [
            {"entity": "Ali ibn Abi Talib", "relationship": "SITE_OF_ASSASSINATION_OF", "note": "Caliph Ali was assassinated at the mosque's mihrab (661 CE) — struck during the dawn prayer — the event that split Islam into Sunni and Shia"},
            {"entity": "Sunni-Shia split", "relationship": "SITE_ASSOCIATED_WITH_DEFINING_TRAUMA_OF", "note": "Ali's assassination (661 CE) and the Karbala prelude events (680 CE) at Kufa are the defining traumas of the Sunni-Shia split"},
            {"entity": "Battle of Karbala (680 CE)", "relationship": "PRELUDE_EVENTS_OCCURRED_AT", "note": "Muslim ibn Aqil's stand at Kufa and the Kufans' betrayal are integral to the Karbala narrative"},
            {"entity": "Shia pilgrimage tradition", "relationship": "PRIMARY_SITE_OF", "note": "One of the primary Shia pilgrimage destinations — millions visit annually during Ramadan and Muharram"},
            {"entity": "Kufic script (Arabic calligraphy)", "relationship": "CITY_THAT_GAVE_NAME_TO", "note": "The Kufic Arabic script — used for the earliest Quran manuscripts — takes its name from Kufa, reflecting the city's role in early Islamic intellectual history"}
        ],
    }),

    ("great-mosque-of-aleppo", {
        "summary": (
            "The Great Mosque of Aleppo (الجامع الأموي في حلب, Umayyad Mosque of Aleppo, est. 715 CE, minaret 1090 CE) is one of the most historically significant mosques of the medieval Islamic world — founded by Caliph al-Walid I (who also built the Umayyad Mosque in Damascus) on the site of a Byzantine cathedral — with a 45-metre Seljuk minaret (completed 1090 CE) that was among the most celebrated Islamic minarets of the medieval period. In 2013, during the Syrian Civil War, the 900-year-old minaret was destroyed — becoming a global symbol of the war's cultural devastation.\n\n"
            "Aleppo was among the most important cities in the medieval Islamic world — a major Silk Road trade hub, a centre of Islamic scholarship, and a Crusader-era political flashpoint — and the Great Mosque was its spiritual centre for 1,300 years. The mosque's Mamluk courtyard, with carved fountain canopy of exceptional workmanship, and the elegant Seljuk minaret — prototype for subsequent Syrian minarets — made it one of the great achievements of medieval Syrian Islamic architecture.\n\n"
            "The mosque's partial destruction in the Syrian Civil War — the Battle of Aleppo (2012–2016) devastated the UNESCO World Heritage Old City, the world's most concentrated ensemble of medieval Islamic urban architecture — prompted global outrage and raised urgent questions about the protection of cultural heritage in armed conflict. Whether Syrian government or opposition forces destroyed the minaret remains disputed. The mosque's fate encapsulates the broader tragedy of Syria's extraordinary cultural heritage."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Major medieval Islamic mosque (est. 715 CE); 45-metre Seljuk minaret (1090 CE) celebrated as the finest Syrian minaret; spiritual centre of Aleppo for 1,300 years; minaret destroyed in the Syrian Civil War (2013) — global symbol of cultural heritage destruction; Aleppo Old City UNESCO World Heritage.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Caliph al-Walid I's mosque-building programme — which also produced the Umayyad Mosque in Damascus — drove the conversion of Aleppo's Byzantine cathedral site into a congregational mosque",
            "Aleppo's position as a major Silk Road trade city — between the Mediterranean coast and Mesopotamia — created the commercial wealth that sustained the mosque's successive construction campaigns and funded the extraordinary Seljuk minaret (1090 CE)",
            "The Syrian Civil War (2011–) and specifically the Battle of Aleppo (2012–2016) brought the mosque into the conflict zone, resulting in the destruction of the 900-year-old minaret in 2013 during fighting for control of the Old City"
        ],
        "effects": [
            "The Seljuk minaret (1090 CE) — 45 metres, with elaborate carved stone decoration — established the visual vocabulary of Syrian Islamic minarets, influencing subsequent mosque construction across Syria and the Levant",
            "The minaret's destruction (2013) — condemned by UNESCO as 'an irreversible loss to humanity' — became a global symbol of the Syrian Civil War's devastation, mobilising international conservation organisations and raising awareness of the systematic destruction of Syria's Islamic heritage",
            "The Battle of Aleppo's devastation of the UNESCO World Heritage Old City — the world's most concentrated ensemble of medieval Islamic urban architecture — prompted major revisions to international humanitarian law regarding the protection of cultural heritage in armed conflict",
            "The mosque's fate illustrated the vulnerability of the world's greatest concentrations of Islamic architectural heritage to modern warfare — leading to new UNESCO conventions and international Red Cross protocols for cultural heritage protection"
        ],
        "relationships": [
            {"entity": "Caliph al-Walid I", "relationship": "FOUNDED_BY", "note": "Al-Walid I founded the mosque (715 CE) — the same caliph who built the Umayyad Mosque in Damascus"},
            {"entity": "Aleppo (medieval Islamic city)", "relationship": "SPIRITUAL_CENTRE_OF", "note": "The mosque served as Aleppo's spiritual centre for 1,300 years — through Crusader, Mongol, Ottoman, and modern periods"},
            {"entity": "Syrian Civil War (2011–)", "relationship": "MINARET_DESTROYED_DURING", "note": "The 900-year-old Seljuk minaret was destroyed in 2013 during the Battle of Aleppo — condemned by UNESCO as irreversible cultural loss"},
            {"entity": "Aleppo Old City (UNESCO)", "relationship": "CENTREPIECE_OF", "note": "The mosque is the centrepiece of Aleppo's UNESCO World Heritage Old City — devastated in the 2012–2016 battle"},
            {"entity": "Syrian Islamic architectural heritage", "relationship": "PRIMARY_SYMBOL_OF_DESTRUCTION_OF", "note": "The damaged mosque became a global symbol of the Syrian Civil War's systematic destruction of Syria's exceptional medieval Islamic heritage"}
        ],
    }),

    ("great-mosque-of-touba", {
        "summary": (
            "The Great Mosque of Touba (Grande Mosquée de Touba, est. 1887, completed 1963) in Touba, Senegal, is the largest mosque in sub-Saharan Africa and the holiest site of the Mouride Brotherhood (Muridiyya) — the most powerful Sufi order in Senegal, with 4–6 million adherents. Founded by Sheikh Amadou Bamba Mbacké (1853–1927), the Mouride Brotherhood represents one of the most successful examples of African Islamic self-determination, having resisted French colonial control while creating a distinct Senegalese form of Islamic practice rooted in work, prayer, and devotion to the founding sheikh.\n\n"
            "The mosque's minaret — the Tour de Lamp, at 87 metres — is the tallest structure in West Africa. The complex is the site of the annual Grand Magal of Touba, a pilgrimage drawing over 3 million Mouride followers from around the world — the second largest annual Islamic gathering in Africa after the Hajj. During the Magal, the entire city of Touba — which is governed by the mosque and the Mouridiyya organisation — is closed to non-Muslims and alcohol.\n\n"
            "The Mouride Brotherhood's extraordinary economic networks — extending from Senegal to Italy, France, the United States, and across West Africa — make the Great Mosque of Touba the spiritual centre of one of the most globally dispersed African diasporic communities. The mosque and the Mouridiyya represent a model of African Islamic self-governance in which the religious authority of the sheikh provides social services, dispute resolution, and economic organisation independent of the state."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Largest mosque in sub-Saharan Africa; holiest site of the Mouride Brotherhood (4–6 million adherents); 87-metre minaret — tallest structure in West Africa; Grand Magal draws 3 million annual pilgrims; Mouridiyya model of African Islamic self-governance; global Mouride diaspora networks.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Sheikh Amadou Bamba's founding of the Mouride Brotherhood in 1887 — a Sufi order emphasising work, prayer, and devotion to the sheikh — created the religious movement that built and maintains the Great Mosque as its spiritual centre",
            "French colonial efforts to suppress and exile Amadou Bamba (exiled to Gabon 1895–1902, then Mauritania 1903–1907) paradoxically strengthened his authority — his calm resistance to French power was interpreted by followers as miraculous, vastly increasing his following and motivating the construction of Touba as an Islamic city beyond colonial control",
            "The Mouride Brotherhood's economic model — followers (talibés) providing labour for the order's groundnut farming operations — created the financial resources that built and expanded the mosque complex across the 20th century"
        ],
        "effects": [
            "The Grand Magal of Touba — drawing over 3 million pilgrims annually — is the second largest annual Islamic gathering in Africa and one of the world's largest religious pilgrimages, demonstrating the Mouride Brotherhood's extraordinary organisational capacity and its members' devotion",
            "The Mouride Brotherhood's global diaspora networks — Mouride traders and merchants operate from New York to Milan to Dakar — have created one of Africa's most powerful economic communities, with the Great Mosque serving as the spiritual anchor for a globalised African Islamic identity",
            "Touba's governance model — the mosque and Mouridiyya organisation providing social services, dispute resolution, and economic organisation independent of the Senegalese state — represents an alternative model of Islamic governance that challenges the assumption that Islamic authority and state authority must be integrated",
            "The mosque's extraordinary scale and the Grand Magal's size demonstrate that African Islamic institutions can match or exceed Middle Eastern Islamic institutions in scale and significance — challenging the marginalisation of sub-Saharan African Islam in global Islamic discourse"
        ],
        "relationships": [
            {"entity": "Mouride Brotherhood (Muridiyya)", "relationship": "SPIRITUAL_CENTRE_OF", "note": "The mosque is the holiest site of the Mouride Brotherhood — 4–6 million adherents, the most powerful Sufi order in Senegal"},
            {"entity": "Sheikh Amadou Bamba Mbacké", "relationship": "FOUNDED_BY", "note": "Amadou Bamba founded the Mouride Brotherhood (1887) and initiated the construction of the Great Mosque — his resistance to French colonial exile vastly expanded the order"},
            {"entity": "Grand Magal of Touba", "relationship": "SITE_OF_ANNUAL_PILGRIMAGE", "note": "The Grand Magal draws 3 million+ annual pilgrims — the second largest annual Islamic gathering in Africa"},
            {"entity": "Mouride global diaspora", "relationship": "SPIRITUAL_ANCHOR_OF", "note": "The mosque anchors the global Mouride diaspora — traders and merchants from New York to Milan who maintain devotion to Touba"},
            {"entity": "African Islamic self-governance", "relationship": "PRIMARY_MODEL_OF", "note": "Touba's governance — mosque and Mouridiyya providing social services independent of the state — represents a distinctive model of African Islamic self-governance"}
        ],
    }),

    ("abu-hanifa-mosque", {
        "summary": (
            "The Abu Hanifa Mosque (مسجد الإمام أبو حنيفة, est. modern structure 1960s, on ancient site) in Baghdad's Adhamiyah district is one of the holiest sites in Sunni Islam — built over the tomb of Abu Hanifa al-Nu'man (699–767 CE), the founder of the Hanafi legal school (madhab), which is the largest Sunni legal school by number of adherents (followed by approximately 45% of Sunni Muslims globally, including most of Turkey, South Asia, Central Asia, and much of the Arab world). The mosque is the most important Sunni shrine in Iraq.\n\n"
            "Abu Hanifa's significance in Islamic jurisprudence is difficult to overstate: he was the first systematic thinker in Islamic legal theory, developing the principle of qiyas (analogical reasoning) and istihsan (juristic preference) as tools for deriving legal rulings from the Quran and Sunnah in novel situations — transforming Islamic law from a collection of case-by-case rulings into a systematic science. His school (the Hanafi madhab) became the official legal school of the Ottoman Empire and remains the dominant legal tradition across the former Ottoman territories.\n\n"
            "The mosque's location in Baghdad's Adhamiyah district — a predominantly Sunni neighbourhood — made it a flashpoint during the sectarian violence following the 2003 US invasion of Iraq. In April 2003, Saddam Hussein was reported to have made his last public appearance in Adhamiyah near the mosque, and the neighbourhood saw fierce resistance to US forces. The mosque remains a potent symbol of Sunni Iraqi identity."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Tomb of Abu Hanifa al-Nu'man (699–767 CE) — founder of the Hanafi legal school followed by 45% of Sunni Muslims globally; most important Sunni shrine in Iraq; Abu Hanifa's development of qiyas and istihsan transformed Islamic law into a systematic science; official legal school of the Ottoman Empire; sectarian flashpoint after 2003 Iraq invasion.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Abu Hanifa al-Nu'man's death in Baghdad (767 CE) — reportedly in Abbasid custody after refusing to accept the position of chief qadi — and his burial in Adhamiyah created a tomb that became a pilgrimage destination for his students and followers",
            "The Hanafi madhab's adoption as the official legal school of the Ottoman Empire (14th century onward) gave Abu Hanifa's legal tradition institutional backing across the largest Islamic empire, ensuring the mosque-tomb's permanent significance as the founding site of the Ottoman legal tradition",
            "The 2003 US invasion of Iraq and the subsequent sectarian violence between Sunni and Shia communities — in which Adhamiyah became a Sunni enclave during the worst of the sectarian conflict (2006–2007) — gave the Abu Hanifa Mosque renewed political and symbolic significance as the centre of Sunni Iraqi identity"
        ],
        "effects": [
            "The Abu Hanifa Mosque's status as the tomb of the founder of the world's largest Sunni legal school makes it a pilgrimage site for millions of Muslims from Turkey, South Asia, Central Asia, and the Arab world — who regard Abu Hanifa's tomb as a site of blessing (baraka)",
            "The Hanafi madhab's position as the official legal school of the Ottoman Empire meant that the Abu Hanifa Mosque's significance extended across the entire Ottoman world — from the Balkans to Arabia — creating a global network of Hanafi institutions ultimately traceable to Baghdad",
            "The mosque's role as a flashpoint during the 2003–2007 Iraqi sectarian conflict — in which the Adhamiyah neighbourhood became a heavily fortified Sunni enclave — illustrates how religious sites become political symbols in sectarian conflicts, with the mosque's protection a matter of Sunni communal pride",
            "Abu Hanifa's jurisprudential innovations — qiyas (analogical reasoning) and istihsan (juristic preference) — which the mosque commemorates, transformed Islamic law from case-by-case rulings into a systematic science, with implications for every legal decision made in the 45% of Muslim-majority countries that follow Hanafi law"
        ],
        "relationships": [
            {"entity": "Abu Hanifa al-Nu'man", "relationship": "HOUSES_TOMB_OF", "note": "The mosque is built over the tomb of Abu Hanifa (699–767 CE) — founder of the Hanafi madhab, the world's largest Sunni legal school"},
            {"entity": "Hanafi legal school (madhab)", "relationship": "FOUNDING_SITE_OF", "note": "The mosque marks the death and burial place of the founder of the Hanafi school — followed by approximately 45% of Sunni Muslims globally"},
            {"entity": "Ottoman Empire (legal system)", "relationship": "OFFICIAL_SCHOOL_FOUNDER_COMMEMORATED_AT", "note": "The Hanafi madhab was the official legal school of the Ottoman Empire — tracing its authority back to Abu Hanifa's tomb in Baghdad"},
            {"entity": "Sunni Iraqi identity (post-2003)", "relationship": "SYMBOL_AND_CENTRE_OF", "note": "The mosque became a potent symbol of Sunni Iraqi identity during the sectarian violence of the 2003–2007 period"},
            {"entity": "Islamic jurisprudence (fiqh)", "relationship": "BIRTH_SITE_OF_SYSTEMATIC", "note": "Abu Hanifa's innovations — qiyas and istihsan — transformed Islamic law from case-by-case rulings into a systematic science, commemorated at his tomb"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 17 — {len(ENTITIES)} entities (Class 342: Great Mosques continued)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
