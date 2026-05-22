#!/usr/bin/env python3
"""
Batch 16 — 8 entities (Class 342): Great Mosques of the Islamic World
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

    ("al-masjid-al-haram", {
        "summary": (
            "Masjid al-Haram (المسجد الحرام, The Sacred Mosque) in Mecca, Saudi Arabia, is the largest mosque in the world and the holiest site in Islam — enclosing the Kaaba, the cuboid structure that Muslims face in prayer five times daily, and the destination of the Hajj pilgrimage that every Muslim who is physically and financially able must make at least once in their lifetime. The mosque complex currently covers 356,800 square metres and can accommodate over 2 million worshippers simultaneously; during the annual Hajj, over 2.5 million pilgrims gather — the largest annual human gathering on earth.\n\n"
            "The Kaaba at the mosque's centre — a granite cube approximately 13.1 metres high, draped in the black Kiswa embroidered with Quranic verses — is regarded as the 'House of God' (Bayt Allah), the first place of worship established on earth according to Islamic tradition, built by Ibrahim (Abraham) and his son Ismail. The Black Stone (al-Hajar al-Aswad) embedded in the Kaaba's eastern corner — a pre-Islamic relic of uncertain origin, possibly meteoritic, venerated as a divine gift — is kissed or touched by pilgrims circumambulating the Kaaba in the Tawaf ritual.\n\n"
            "The mosque has been continuously expanded by successive Islamic rulers — the Umayyads, Abbasids, Ottomans, and Saudi monarchs — with the most radical expansions undertaken by the Saudi government since 1955, demolishing extensive Ottoman and medieval architecture to build the current reinforced concrete complex. Non-Muslims are forbidden from entering Mecca, making the Masjid al-Haram the most exclusive major religious site on earth."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Largest mosque and holiest site in Islam; the Kaaba is the point toward which 1.8 billion Muslims pray five times daily; the Hajj — 2.5 million pilgrims annually — is the largest annual human gathering on earth; the Black Stone is the most venerated relic in Islam; non-Muslims forbidden entry.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Islamic theology's designation of the Kaaba — according to the Quran, built by Ibrahim and Ismail — as the 'House of God' and the first place of worship established on earth created the theological mandate for the mosque that surrounds it to be the holiest site in Islam",
            "The Prophet Muhammad's conquest of Mecca (630 CE) and his destruction of the idols in the Kaaba — restoring it to monotheistic worship — established the mosque's centrality to the Islamic faith and the obligation of pilgrimage (Hajj) that has brought millions to Mecca annually for 1,400 years",
            "The Quran's command that Muslims face the Kaaba in prayer (2:144) — establishing the qibla (direction of prayer) — meant that the Masjid al-Haram became the symbolic centre of every Islamic act of worship globally, regardless of where the worshipper stood"
        ],
        "effects": [
            "The Hajj obligation — one of Islam's Five Pillars — creates the annual gathering of 2.5 million pilgrims at the Masjid al-Haram, the largest annual peaceful human gathering on earth, which has historically served as a pan-Islamic congress facilitating the exchange of ideas, goods, and diseases across the Islamic world",
            "The qibla direction — all Muslims facing Mecca in prayer five times daily — creates the physical expression of Islamic unity, with 1.8 billion people simultaneously oriented toward the Masjid al-Haram in the largest coordinated human ritual in history",
            "Saudi Arabia's custodianship of the Two Holy Mosques (Mecca and Medina) — which gives the Saudi royal family the title 'Custodian of the Two Holy Mosques' — is the primary source of the House of Saud's religious legitimacy and political authority in the Islamic world",
            "The 1979 seizure of the Grand Mosque by Juhayman al-Otaybi (November 20, 1979) — 400–500 armed men holding the mosque for two weeks — was one of the most dramatic crises in modern Islamic history, killing 270 people and shaking Saudi religious and political authority"
        ],
        "relationships": [
            {"entity": "Kaaba", "relationship": "ENCIRCLES_AND_PROTECTS", "note": "The Masjid al-Haram is built around the Kaaba — the 'House of God' that is the direction of Muslim prayer and the centre of the Hajj Tawaf ritual"},
            {"entity": "Hajj", "relationship": "PRIMARY_SITE_OF", "note": "The Hajj — Islam's fifth pillar, 2.5 million pilgrims annually — is performed at and around the Masjid al-Haram"},
            {"entity": "Saudi Arabia (House of Saud)", "relationship": "CUSTODIANSHIP_SOURCE_OF_RELIGIOUS_LEGITIMACY_FOR", "note": "Saudi Arabia's 'Custodian of the Two Holy Mosques' title — derived from control of the Masjid al-Haram — is the primary source of Saudi religious authority"},
            {"entity": "1979 Grand Mosque seizure", "relationship": "SITE_OF_CRISIS", "note": "Juhayman al-Otaybi's 1979 seizure of the Grand Mosque (270 killed) was one of the most dramatic crises in modern Islamic history"},
            {"entity": "Islamic prayer (Salah)", "relationship": "UNIVERSAL_ORIENTATION_POINT_OF", "note": "The Masjid al-Haram's Kaaba is the qibla — the point toward which 1.8 billion Muslims orient themselves in daily prayer"}
        ],
    }),

    ("al-aqsa-mosque", {
        "summary": (
            "Al-Aqsa Mosque (المسجد الأقصى, The Farthest Mosque) in Jerusalem is the third holiest site in Islam — on the Temple Mount (Haram al-Sharif), the most contested religious space on earth — where according to Islamic tradition the Prophet Muhammad was transported from Mecca during the Night Journey (Isra) and from where he ascended to heaven (Mi'raj). The mosque complex on the Temple Mount includes the al-Aqsa Mosque (the large silver-domed basilica building) and the Dome of the Rock (the golden-domed shrine over the Sacred Rock) — together forming the holiest Islamic complex outside Arabia.\n\n"
            "The Temple Mount's extraordinary religious density — the site of Solomon's Temple and the Second Temple (the holiest site in Judaism), the location of Jesus's teaching and the entry into Jerusalem (sacred in Christianity), and the site of the Night Journey (the third holiest site in Islam) — makes it the most contested religious space in human history. The al-Aqsa compound is administered by the Islamic Waqf, but Israel controls access — a division that has generated repeated violent conflicts.\n\n"
            "The 1969 arson attack on al-Aqsa by Australian Christian fundamentalist Denis Michael Rohan — which destroyed an 800-year-old Crusader-era pulpit (minbar) installed by Saladin — prompted the establishment of the Organisation of Islamic Cooperation (OIC), the largest inter-governmental Islamic body. The mosque's contested status is a permanent source of Israeli-Palestinian and broader Arab-Israeli tension."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Third holiest site in Islam; site of Muhammad's Night Journey and Ascension; the most contested religious space on earth (holy to Judaism, Christianity, and Islam); 1969 arson prompted founding of the OIC; Saladin's pulpit and Crusader mosque conversion; permanent source of Israeli-Palestinian conflict.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Prophet Muhammad's Night Journey (Isra wa Mi'raj, 621 CE) — his miraculous transport from Mecca to Jerusalem and ascent to heaven — established Jerusalem's sacred status in Islam, creating the theological foundation for al-Aqsa's third-holiest designation",
            "Caliph Omar ibn al-Khattab's conquest of Jerusalem (637 CE) and his construction of a simple mosque on the Temple Mount — on the site associated with the Night Journey — began the Islamic presence at al-Aqsa that has continued for 1,400 years",
            "The Crusader capture of Jerusalem (1099) and conversion of al-Aqsa into a Christian church (the Templum Solomonis, headquarters of the Knights Templar) — followed by Saladin's reconquest (1187) and the mosque's restoration as an Islamic house of worship — established the pattern of contested religious ownership that continues today"
        ],
        "effects": [
            "Al-Aqsa's status as the third holiest site in Islam makes it a constant symbol of Palestinian national identity and a rallying point for pan-Islamic solidarity — Ariel Sharon's provocative visit to the Temple Mount (September 2000) is widely credited as the trigger for the Second Intifada",
            "The 1969 arson (Denis Michael Rohan) — which destroyed the 800-year-old Saladin-era minbar — prompted Egyptian President Nasser to convene an Islamic summit that established the Organisation of Islamic Cooperation (OIC), the 57-member inter-governmental Islamic body, making the mosque's violation the direct cause of Islam's most important inter-state institution",
            "The contested administration of the Temple Mount — Islamic Waqf controls al-Aqsa while Israel controls overall access — has been a permanent source of Israeli-Palestinian conflict, with regular clashes between Israeli police and Palestinian worshippers generating international crises",
            "Al-Aqsa's gold dome and distinctive silhouette — the most recognisable image of Jerusalem globally — has made it the primary visual symbol of the Palestinian cause and of Islamic claims to Jerusalem in global political discourse"
        ],
        "relationships": [
            {"entity": "Temple Mount (Haram al-Sharif)", "relationship": "LOCATED_ON", "note": "Al-Aqsa is located on the Temple Mount — the most contested religious space on earth, holy to Judaism, Christianity, and Islam"},
            {"entity": "Night Journey (Isra wa Mi'raj)", "relationship": "SITE_ASSOCIATED_WITH", "note": "Al-Aqsa marks the site of Muhammad's Night Journey and Ascension — the theological basis for its third-holiest designation in Islam"},
            {"entity": "Organisation of Islamic Cooperation (OIC)", "relationship": "FOUNDING_PROVOKED_BY_ATTACK_ON", "note": "The 1969 arson at al-Aqsa prompted Nasser to convene the Islamic summit that founded the OIC — 57 member states"},
            {"entity": "Second Intifada (2000)", "relationship": "SHARON_VISIT_TRIGGERED", "note": "Ariel Sharon's visit to the Temple Mount (September 2000) triggered the Second Intifada — demonstrating al-Aqsa's status as a flashpoint for Israeli-Palestinian conflict"},
            {"entity": "Saladin (Salah al-Din)", "relationship": "RESTORED_AS_ISLAMIC_MOSQUE_BY", "note": "Saladin reconquered Jerusalem (1187) and restored al-Aqsa as a mosque — installing the magnificent minbar destroyed by arson in 1969"}
        ],
    }),

    ("dome-of-the-rock", {
        "summary": (
            "The Dome of the Rock (قبة الصخرة, Qubbat al-Sakhra, est. 691 CE) is an Islamic shrine in Jerusalem — built by Umayyad Caliph Abd al-Malik ibn Marwan — that stands over the Sacred Rock from which Muhammad is believed to have ascended to heaven during the Night Journey, and which Jewish tradition identifies as the Foundation Stone (Even HaShetiyah) upon which God created the world and where Abraham prepared to sacrifice Isaac. It is the oldest surviving Islamic monument and the finest example of early Islamic architecture.\n\n"
            "The Dome of the Rock's octagonal design and golden dome — visible from across Jerusalem — is the most recognised architectural image of the Islamic world and one of the most photographed buildings on earth. Its interior — covered in Quranic inscriptions in gold mosaic on blue backgrounds — contains the oldest datable Quranic inscriptions in existence and the most important early Islamic epigraphic programme. The inscriptions' theological content — repeatedly asserting Islamic monotheism and denying the Trinity — reflects Abd al-Malik's political and theological challenge to Byzantine Christianity.\n\n"
            "The Dome of the Rock was never designed as a mosque (there is no mihrab in the original structure) but as a commemorative shrine (mashhad) over the Sacred Rock — closer in function to a Christian martyrium or reliquary chapel than to a mosque. It has been continuously maintained for 1,333 years — surviving the Crusader conversion to a church (1099–1187), the Ottoman restoration, and the modern Israeli-Palestinian conflict."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Oldest surviving Islamic monument (est. 691 CE); finest early Islamic architecture; oldest datable Quranic inscriptions in existence; over the Sacred Rock (Islam's Night Journey ascent, Judaism's Foundation Stone, Abraham's sacrifice site); the most recognised Islamic architectural image globally; 1,333 years of continuous existence.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Caliph Abd al-Malik's political motivation — building a magnificent Islamic monument in Jerusalem to rival the Church of the Holy Sepulchre and assert Islamic supremacy over Christianity and Judaism — drove the Dome of the Rock's construction, making it as much a political as a religious statement",
            "The Sacred Rock's extraordinary religious importance — associated with Muhammad's Night Journey, with the Foundation Stone of Jewish creation theology, and with Abraham's near-sacrifice — created the mandate for an exceptional architectural response",
            "The Umayyad dynasty's programme of monumental architecture — the Dome of the Rock, the Great Mosque of Damascus — reflecting their desire to create an Islamic civilization that could compete aesthetically with the Byzantine and Sassanid empires they had conquered"
        ],
        "effects": [
            "The Dome of the Rock's Quranic inscriptions (691 CE) — the oldest datable Quranic text in existence in monumental form — are the primary surviving evidence for the early text of the Quran and for early Islamic theological formulations, making the building a priceless document of Islamic intellectual history",
            "The Dome of the Rock's architectural influence — its octagonal plan, golden dome, decorative mosaics — was the template for subsequent Islamic domed shrines from Central Asia to Morocco, establishing the vocabulary of Islamic monumental architecture for centuries",
            "The Crusaders' conversion of the Dome of the Rock into a Christian church (1099, renamed Templum Domini) and the Knights Templar's subsequent adoption of it as their symbol — the Templar seal shows two knights on one horse before the Dome — created one of the most enduring images in medieval Western iconography",
            "The Dome of the Rock's golden dome (gold-plated, restored 1993 at a cost of $8 million donated by King Hussein of Jordan) is the defining skyline image of Jerusalem — visible in countless photographs, films, and political images — making it the primary visual symbol of Jerusalem globally"
        ],
        "relationships": [
            {"entity": "Sacred Rock (Foundation Stone)", "relationship": "BUILT_OVER", "note": "The Dome of the Rock is built over the Sacred Rock — associated with Muhammad's Ascension, Jewish creation theology, and Abraham's near-sacrifice"},
            {"entity": "Caliph Abd al-Malik", "relationship": "COMMISSIONED_BY", "note": "Abd al-Malik built the Dome of the Rock (691 CE) as an Islamic monument to rival the Church of the Holy Sepulchre"},
            {"entity": "Early Quranic text", "relationship": "CONTAINS_OLDEST_DATABLE_INSCRIPTIONS_OF", "note": "The Dome's mosaic inscriptions (691 CE) are the oldest datable Quranic text in monumental form — priceless for early Islamic textual history"},
            {"entity": "Knights Templar", "relationship": "SEAL_IMAGE_BASED_ON", "note": "The Templars adopted the Dome of the Rock as their symbol after their conversion of it to a church (1099) — the Dome appears on the Templar seal"},
            {"entity": "Jerusalem's skyline identity", "relationship": "DEFINING_VISUAL_SYMBOL_OF", "note": "The Dome of the Rock's golden dome is the defining image of Jerusalem globally — the most recognised architectural image of the Islamic world"}
        ],
    }),

    ("umayyad-mosque", {
        "summary": (
            "The Umayyad Mosque (الجامع الأموي, Great Mosque of Damascus, est. 705–715 CE) in Damascus, Syria, is one of the oldest and holiest mosques in the world — built by Caliph al-Walid I on the site of a Roman Jupiter temple later converted to a Byzantine cathedral — and is the first imperial mosque of Islam, representing the high point of Umayyad architectural achievement. The mosque's integration of Byzantine mosaic technique with Islamic geometric and vegetal ornament created the foundational vocabulary of Islamic decorative arts.\n\n"
            "The Umayyad Mosque holds a unique position in Islamic eschatology: Jesus Christ is prophesied to descend at the mosque's white minaret (Minaret of Jesus / Isa) on the Day of Judgment — making it sacred not only to Muslims but eschatologically significant in the Islamic vision of the end times. The mosque also claims to contain the tomb of John the Baptist (Yahya ibn Zakariyya) — a gold reliquary holds what tradition identifies as his head — making it one of the few Islamic sites with direct Christian relic connection.\n\n"
            "Damascus was one of the most contested cities of the Syrian Civil War (2011–present), with the Umayyad Mosque heavily damaged in fighting. The mosque's mosaics — depicting a paradise landscape of jewelled trees and golden buildings beside rivers, with no human figures — are the most important surviving examples of early Islamic monumental mosaic and a unique record of how the early Islamic world envisioned the afterlife."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "One of the world's oldest and holiest mosques (est. 705–715 CE); first imperial mosque of Islam; built on Jupiter temple / Byzantine cathedral site; mosaic programme is the most important early Islamic decorative art; eschatological site for Christ's Second Coming; houses claimed tomb of John the Baptist; damaged in Syrian Civil War.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Caliph al-Walid I's ambition to create a mosque that would surpass all existing religious buildings — his reported statement that he wanted Muslims to feel their mosque was the greatest building in the world — drove the Umayyad Mosque's extraordinary construction, using Byzantine craftsmen and drawing on the full resources of the Umayyad caliphate",
            "Damascus's position as the capital of the Umayyad caliphate — the first great Islamic empire — made it the natural site for the most ambitious Islamic architectural statement, with the Caliph needing a mosque worthy of his imperial capital",
            "The pre-existing sacred site — Jupiter temple (1st century CE), then Cathedral of Saint John the Baptist (4th century CE), then shared Christian-Muslim space during early Islamic rule — created both the architectural infrastructure and the religious prestige that made the site ideal for the imperial mosque"
        ],
        "effects": [
            "The Umayyad Mosque's mosaics — depicting paradise as a landscape of jewelled trees, golden buildings, and rivers — established the vocabulary of Islamic decorative art, with their integration of Byzantine technique and Islamic content creating the synthesis that defined Islamic visual culture for centuries",
            "The mosque's architectural programme — prayer hall, covered arcades, vast courtyard, minarets — became the template for the congregational mosque throughout the Islamic world, establishing the elements that virtually every subsequent Friday mosque incorporated",
            "The Umayyad Mosque's eschatological significance — as the site of Christ's prophesied descent at the Second Coming — gives it a unique position in Islamic-Christian theology, representing one of the few specific places named in Islamic prophetic tradition for end-time events",
            "The mosque's survival (with damage) through the Syrian Civil War — despite fierce fighting in Damascus's Old City — made it a symbol of Syrian cultural resilience, with its preservation a stated priority of all conflict parties and international conservation organisations"
        ],
        "relationships": [
            {"entity": "Caliph al-Walid I", "relationship": "COMMISSIONED_BY", "note": "Al-Walid I built the Umayyad Mosque (705–715 CE) — the first imperial mosque of Islam, drawing on the full resources of the Umayyad caliphate"},
            {"entity": "Byzantine decorative arts", "relationship": "INTEGRATED_WITH_ISLAMIC_ORNAMENT_TO_CREATE", "note": "The mosque's mosaics — Byzantine technique, Islamic subject matter — created the foundational vocabulary of Islamic decorative arts"},
            {"entity": "John the Baptist", "relationship": "CLAIMED_TOMB_OF_HOUSED_IN", "note": "The mosque claims to house the tomb of John the Baptist (Yahya) — a gold reliquary with his head — creating a unique Islamic-Christian relic connection"},
            {"entity": "Islamic eschatology", "relationship": "PROPHESIED_SITE_OF_SECOND_COMING_IN", "note": "Islamic tradition prophesies that Jesus (Isa) will descend at the mosque's white Minaret of Jesus on the Day of Judgment"},
            {"entity": "Syrian Civil War (2011–)", "relationship": "DAMAGED_DURING", "note": "The Umayyad Mosque was damaged in fighting during the Syrian Civil War — its preservation a priority for international conservation efforts"}
        ],
    }),

    ("blue-mosque", {
        "summary": (
            "The Sultan Ahmed Mosque (Sultanahmet Camii, 'Blue Mosque', est. 1609–1616) in Istanbul is one of the finest examples of classical Ottoman architecture and the only mosque in Istanbul with six minarets — a detail that caused controversy because it equalled the number of minarets at the Masjid al-Haram in Mecca. Built by Sultan Ahmed I to reassert Ottoman piety and grandeur after a series of military setbacks, the mosque was decorated with over 20,000 İznik tiles (primarily in shades of blue and green) that gave it its popular name.\n\n"
            "The Blue Mosque is the last great mosque built by the classical Ottoman imperial tradition — combining the architectural legacy of Hagia Sophia (whose interior spatial arrangement directly influenced the Blue Mosque through Sinan's work) with the Ottoman mastery of domed space pioneered by the great architect Mimar Sinan. The architect Sedefkâr Mehmed Ağa — Sinan's student — created a mosque that attempts the impossible: matching Hagia Sophia's sublime spatial effect with an entirely Islamic aesthetic.\n\n"
            "The Blue Mosque remains an active place of worship — it is closed to tourists during prayer times — while simultaneously being Istanbul's most visited tourist site (3.5 million visitors annually) and the centrepiece of the UNESCO-listed Historic Areas of Istanbul. Its location directly across from Hagia Sophia — the two buildings facing each other across the Hippodrome — creates the most dramatic religious architectural confrontation in the world: Islam's finest mosque facing Christianity's greatest church."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Last great classical Ottoman imperial mosque (est. 1609–1616); only Istanbul mosque with six minarets; 20,000 İznik tiles; Sedefkâr Mehmed Ağa's masterwork; 3.5 million annual visitors; faces Hagia Sophia across the Hippodrome — the world's most dramatic religious architectural confrontation.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Sultan Ahmed I's desire to restore Ottoman imperial prestige — after military defeats against the Habsburgs (Peace of Zsitvatorok, 1606) and Safavids — drove the construction of a mosque of unprecedented grandeur, using the royal treasury in a display of divine favour and imperial confidence",
            "The Ottoman architectural tradition's continuous engagement with Hagia Sophia's challenge — each generation of architects seeking to equal or surpass the Byzantine dome — created the intellectual context for the Blue Mosque's attempt to match Hagia Sophia's spatial achievement using Islamic means",
            "The completion of Mimar Sinan's Ottoman mosque programme — Süleymaniye (1557), Selimiye (1574) — established the standard of excellence that Sedefkâr Mehmed Ağa had to engage with, creating the competitive context that produced the Blue Mosque's ambitious six-minaret programme"
        ],
        "effects": [
            "The Blue Mosque's six minarets — unprecedented for a mosque outside Mecca — caused the Ottoman court to send funds to add a seventh minaret to the Masjid al-Haram in Mecca, demonstrating how the mosque's architectural ambition created theological controversy",
            "The 20,000 İznik tiles decorating the Blue Mosque's interior — produced by the finest Turkish ceramic workshops at the peak of Ottoman İznik tile production — represent the largest and most important collection of İznik tiles in existence, preserving the record of Ottoman ceramic art at its height",
            "The Blue Mosque's continued use as an active mosque — closed during prayer times, with tourists required to remove shoes and women to cover their heads — models the balance between Islamic religious practice and global tourism that has become the standard approach for active mosques receiving millions of visitors",
            "The visual confrontation between the Blue Mosque and Hagia Sophia — separated by the ancient Hippodrome — has made the Istanbul skyline the most powerful architectural symbol of the East-West religious encounter, reproduced in millions of photographs and travel images annually"
        ],
        "relationships": [
            {"entity": "Sultan Ahmed I", "relationship": "COMMISSIONED_BY", "note": "Ahmed I commissioned the Blue Mosque (1609–1616) to restore Ottoman imperial prestige after military setbacks"},
            {"entity": "Hagia Sophia", "relationship": "CONFRONTS_ACROSS_THE_HIPPODROME", "note": "The Blue Mosque faces Hagia Sophia across the Hippodrome — the world's most dramatic architectural religious confrontation"},
            {"entity": "İznik tile tradition", "relationship": "HOUSES_LARGEST_COLLECTION_OF", "note": "20,000 İznik tiles in the Blue Mosque represent the largest and most important İznik tile collection — Ottoman ceramic art at its height"},
            {"entity": "Ottoman imperial architecture", "relationship": "LAST_GREAT_EXAMPLE_OF_CLASSICAL", "note": "The Blue Mosque is the last great classical Ottoman imperial mosque — Sedefkâr Mehmed Ağa's synthesis of Sinan's legacy"},
            {"entity": "Istanbul's UNESCO Historic Areas", "relationship": "CENTREPIECE_OF", "note": "The Blue Mosque is the centrepiece of Istanbul's UNESCO World Heritage Historic Areas — 3.5 million annual visitors"}
        ],
    }),

    ("suleymaniye-mosque", {
        "summary": (
            "The Süleymaniye Mosque (Süleymaniye Camii, est. 1550–1557) in Istanbul is the masterpiece of the greatest Ottoman architect, Mimar Sinan — built for Sultan Suleiman the Magnificent at the height of the Ottoman Empire's power and regarded as the most perfectly proportioned of all Ottoman imperial mosques. Sinan later described the Süleymaniye as his journeyman's work — reserving his claim to mastery for the Selimiye Mosque at Edirne (1574) — but the Süleymaniye's combination of architectural perfection, commanding hilltop position, and broader kulliye complex makes it the defining image of Ottoman Istanbul.\n\n"
            "The Süleymaniye is not merely a mosque but a kulliye — a complex including two madrasas (Islamic colleges), a hospital, a caravanserai, a Quran school, a soup kitchen, a bath, and eventually the tombs of Suleiman the Magnificent and his wife Hürrem Sultan. This comprehensive social welfare complex — providing education, healthcare, lodging, and food — embodies the Ottoman state's understanding of imperial beneficence and the mosque's role as the centre of a complete urban social programme.\n\n"
            "Mimar Sinan's structural innovation in the Süleymaniye — using the tension between the massive central dome and the four half-domes, the 138 windows that flood the interior with light, and the four exterior minarets — solved the aesthetic problem of translating Hagia Sophia's spatial grandeur into Islamic form. The acoustics, achieved through 64 pots embedded in the walls to absorb sound, were designed to make the human voice carry across the vast interior during prayer."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Mimar Sinan's masterwork for Suleiman the Magnificent (est. 1550–1557); defining image of Ottoman Istanbul; kulliye complex embodying Ottoman imperial social welfare; Sinan's structural innovations translating Hagia Sophia into Islamic form; tombs of Suleiman the Magnificent and Hürrem Sultan; acoustic pots innovation.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Suleiman the Magnificent's desire — at the Ottoman Empire's zenith, after his empire stretched from Hungary to the Persian Gulf — to create a mosque that would memorialise his reign and demonstrate Ottoman civilisational achievement created the political will for Mimar Sinan's most ambitious commission",
            "Mimar Sinan's 30 years of architectural development — including over 300 buildings across the Ottoman Empire — gave him the experience and confidence to attempt the architectural challenge of creating a mosque that equalled Hagia Sophia in spatial grandeur using Islamic structural means",
            "Ottoman imperial theology's identification of the sultan as the shadow of God on earth (zill Allah) — and the mosque as the architectural expression of this divine mandate — created the brief for a building of supreme quality that would express the Ottoman Empire's claim to universal Islamic sovereignty"
        ],
        "effects": [
            "The Süleymaniye's kulliye complex — madrasa, hospital, caravanserai, soup kitchen — became the template for the Ottoman imperial kulliye, with every subsequent Ottoman sultan competing to create more comprehensive complexes, creating the urban social welfare infrastructure of Ottoman cities",
            "Mimar Sinan's structural solutions in the Süleymaniye — dome-and-half-dome system, 138 windows, acoustic pots — were the technical innovations that the Blue Mosque's Sedefkâr Mehmed Ağa directly built upon, making the Süleymaniye the direct architectural ancestor of the next generation of Ottoman mosques",
            "The tombs of Suleiman the Magnificent and Hürrem Sultan (Roxelana) in the Süleymaniye's garden — the two most celebrated figures of the Ottoman golden age — make the mosque the primary memorial site for Ottoman imperial history",
            "The Süleymaniye's commanding hilltop position — visible from the Bosphorus and from much of Istanbul — established the mosque on the horizon as the dominant element in Istanbul's skyline, maintaining its visual primacy for 470 years"
        ],
        "relationships": [
            {"entity": "Mimar Sinan", "relationship": "DESIGNED_BY", "note": "Mimar Sinan designed the Süleymaniye (1550–1557) — calling it his 'journeyman's work' before his masterpiece the Selimiye"},
            {"entity": "Suleiman the Magnificent", "relationship": "COMMISSIONED_BY_AND_ENTOMBED_IN", "note": "Suleiman commissioned the Süleymaniye — and is entombed in its garden alongside his wife Hürrem Sultan"},
            {"entity": "Ottoman kulliye tradition", "relationship": "DEFINING_EXAMPLE_OF", "note": "The Süleymaniye kulliye — mosque, madrasas, hospital, caravanserai, soup kitchen — is the defining example of Ottoman imperial social welfare architecture"},
            {"entity": "Hagia Sophia", "relationship": "ARCHITECTURAL_CHALLENGE_RESPONDED_TO", "note": "Mimar Sinan's structural solutions in the Süleymaniye directly responded to Hagia Sophia's challenge — translating its spatial grandeur into Islamic form"},
            {"entity": "Blue Mosque", "relationship": "ARCHITECTURAL_DIRECT_ANCESTOR_OF", "note": "Sedefkâr Mehmed Ağa's Blue Mosque directly built upon Sinan's structural innovations in the Süleymaniye"}
        ],
    }),

    ("selimiye-mosque", {
        "summary": (
            "The Selimiye Mosque (Selimiye Camii, est. 1569–1574) in Edirne, Turkey, is the acknowledged masterpiece of Mimar Sinan — who designed it at age 80 and declared it his finest work — and is widely regarded as the peak achievement of Ottoman architecture. Sinan's claim was specific and architectural: the Selimiye's central dome (31.28 metres diameter) is slightly larger than Hagia Sophia's (31.24 metres) and Sinan saw its construction as the resolution of a 1,000-year architectural challenge — creating a dome as large as Hagia Sophia's within an entirely new structural system.\n\n"
            "The Selimiye's structural innovation is radical: the dome rests on eight piers rather than four, creating an octagonal support system that distributes the weight more efficiently than any previous large dome. The result is a dome that appears to float with extraordinary lightness, surrounded by 999 windows (by tradition) that flood the interior with natural light from every direction simultaneously. The four minarets — at 70.9 metres among the tallest in the world — frame the dome with exceptional elegance.\n\n"
            "Built for Sultan Selim II (Suleiman the Magnificent's son) in Edirne — the former Ottoman capital and second city of the empire — the Selimiye was Sinan's opportunity to build without the constraints of an existing urban site. The surrounding kulliye — six madrasas, a covered bazaar, a clock house, a library — completes the most ambitious Ottoman architectural ensemble outside Istanbul. A UNESCO World Heritage Site since 2011."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Mimar Sinan's self-declared masterpiece (est. 1569–1574); dome (31.28m) marginally larger than Hagia Sophia's (31.24m) — Sinan's resolution of 1,000-year architectural challenge; eight-pier structural system; 999 windows; UNESCO World Heritage (2011); the peak of Ottoman architectural achievement at the empire's zenith.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Mimar Sinan's lifelong architectural challenge — how to create a dome as large as Hagia Sophia within a new structural system that did not depend on the Byzantine pendentive-and-buttress approach — motivated his design of the eight-pier system that the Selimiye finally realised",
            "Sultan Selim II's commission — wanting a mosque in Edirne (his preferred city) that would surpass Suleiman's Süleymaniye — gave Sinan the imperial mandate and financial resources to build at the scale his ambition required",
            "Edirne's open site — unlike Istanbul's crowded hilltops — gave Sinan the freedom to design the Selimiye's relationship with the landscape without the constraints of existing urban fabric, allowing the freely-planned four-minaret composition"
        ],
        "effects": [
            "The Selimiye's eight-pier structural system — distributing the dome's weight more efficiently than any previous system — was a genuine structural innovation that influenced subsequent large-dome construction and demonstrated that the Ottoman architectural tradition had developed its own solutions to the engineering challenges that the Byzantine tradition had addressed differently",
            "Sinan's explicit claim that the Selimiye's dome surpassed Hagia Sophia's — at age 80, after a career of over 300 buildings — represents the Ottoman architectural tradition's self-conscious assertion of its own achievement, marking the moment Ottoman architecture declared independence from Byzantine precedent",
            "The Selimiye's UNESCO designation (2011) — recognising it as a masterpiece of human creative genius — gave the Ottoman architectural tradition its most authoritative international validation, positioning the Selimiye alongside Notre-Dame de Paris and Chartres as a universal cultural monument",
            "Edirne's identity — as the city of the Selimiye — demonstrates how a single architectural masterpiece can define a city's global significance, with Edirne otherwise a regional Turkish city but internationally known primarily through Sinan's mosque"
        ],
        "relationships": [
            {"entity": "Mimar Sinan", "relationship": "SELF-DECLARED_MASTERPIECE_BY", "note": "Sinan declared the Selimiye his finest work — designed at age 80, after 300 buildings, as the resolution of his architectural life's challenge"},
            {"entity": "Sultan Selim II", "relationship": "COMMISSIONED_BY", "note": "Selim II commissioned the Selimiye in Edirne — wanting a mosque surpassing his father Suleiman's Süleymaniye"},
            {"entity": "Hagia Sophia", "relationship": "DOME_EXPLICITLY_RESPONDS_TO_AND_EXCEEDS", "note": "Sinan designed the Selimiye to equal and exceed Hagia Sophia's dome — a 1,000-year architectural challenge resolved"},
            {"entity": "UNESCO World Heritage", "relationship": "INSCRIBED_AS", "note": "The Selimiye was inscribed as a UNESCO World Heritage Site (2011) — 'a masterpiece of human creative genius'"},
            {"entity": "Ottoman architectural tradition", "relationship": "PEAK_ACHIEVEMENT_OF", "note": "The Selimiye represents the peak of Ottoman architectural achievement — Sinan's structural innovations establishing Ottoman architecture's independence from Byzantine precedent"}
        ],
    }),

    ("great-mosque-of-djenné", {
        "summary": (
            "The Great Mosque of Djenné (Grande Mosquée de Djenné, rebuilt 1907 in traditional style) in Djenné, Mali, is the largest mud-brick (adobe) building in the world and the finest example of Sudano-Sahelian Islamic architecture — a building tradition that uses sun-dried mud brick (ferey) reinforced by wooden beams (toron) that project from the walls as both structural elements and scaffolding anchors during the annual replastering ceremony. The current structure was rebuilt in 1907 under French colonial direction but follows the form of the original 13th-century mosque.\n\n"
            "Djenné was founded c.800 CE and became one of the most important commercial and Islamic scholarly centres in sub-Saharan Africa — at the intersection of the trans-Saharan gold and salt trade routes — with its mosque the spiritual centre of a city that at its height housed major Quranic schools and was a waypoint for Muslim pilgrims crossing the Sahara to Mecca. The mosque's distinctive minarets, topped with ostrich eggs, and its 'bristling' facade created by the protruding toron gave it the most distinctive silhouette in West African Islamic architecture.\n\n"
            "The mosque's annual replastering (Crepissage de la Grande Mosquée) — a community festival in which the entire population of Djenné participates in applying new mud plaster to the mosque's exterior — is the most remarkable community maintenance ritual associated with any religious building in the world, and a UNESCO Intangible Cultural Heritage. A UNESCO World Heritage Site since 1988, the mosque has become the symbol of West African Islamic culture globally."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "World's largest mud-brick building; finest Sudano-Sahelian Islamic architecture; symbol of West African Islam; Djenné was a major trans-Saharan trade and Islamic scholarship centre; annual community replastering is UNESCO Intangible Cultural Heritage; UNESCO World Heritage Site (1988); the most distinctive mosque silhouette in Africa.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Djenné's position at the intersection of trans-Saharan trade routes — where gold and salt from West Africa met goods from North Africa and the Mediterranean — created the commercial wealth that financed the original 13th-century mosque and sustained its rebuilding across centuries",
            "The Sahel's lack of stone — the entire region is mud, sand, and laterite — forced the development of a mud-brick architectural tradition that the Great Mosque exemplifies, with the toron-reinforced ferey construction representing centuries of accumulated expertise in building with earth",
            "Islam's spread across sub-Saharan Africa via the trans-Saharan trade routes — Djenné converted to Islam c.1300 CE — created the religious motivation for constructing a mosque at the commercial and spiritual centre of the Western Sahel"
        ],
        "effects": [
            "The Great Mosque of Djenné became the symbol of West African Islamic culture globally — reproduced in countless books, films, and photographs — making it the primary visual icon of African Islamic architecture and demonstrating that the Islamic world's architectural tradition extends far beyond the Arab Middle East",
            "The annual Crepissage — community replastering festival — is the world's most remarkable community building-maintenance ritual, creating a living demonstration of the relationship between community solidarity, religious devotion, and architectural preservation",
            "Djenné's Great Mosque has influenced the development of a contemporary West African Islamic architectural movement — 'new Sudano-Sahelian' architecture — that seeks to develop modern Islamic buildings drawing on the mud-brick aesthetic rather than importing Middle Eastern mosque styles",
            "The mosque's UNESCO designation (1988) contributed to the global recognition of sub-Saharan African architectural heritage, challenging the assumption that Africa's historic architecture was limited to Egyptian and North African monuments"
        ],
        "relationships": [
            {"entity": "Trans-Saharan trade (West Africa)", "relationship": "SPIRITUAL_CENTRE_OF_CITY_ENRICHED_BY", "note": "Djenné's position at trans-Saharan trade routes created the wealth that built and maintains the mosque"},
            {"entity": "Sudano-Sahelian Islamic architecture", "relationship": "FINEST_EXAMPLE_OF", "note": "The Great Mosque is the finest example of the distinctive mud-brick Islamic architecture of the Western Sahel"},
            {"entity": "Crepissage (annual replastering)", "relationship": "MAINTAINED_BY", "note": "The annual community replastering festival — UNESCO Intangible Cultural Heritage — is the world's most remarkable architectural maintenance ritual"},
            {"entity": "West African Islam", "relationship": "PRIMARY_ARCHITECTURAL_SYMBOL_OF", "note": "The mosque is the global symbol of West African Islamic culture — demonstrating the geographic breadth of the Islamic architectural tradition"},
            {"entity": "UNESCO World Heritage", "relationship": "INSCRIBED_AS", "note": "Djenné's Great Mosque and the Old Towns of Djenné were inscribed as UNESCO World Heritage (1988)"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 16 — {len(ENTITIES)} entities (Class 342: Great Mosques)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
