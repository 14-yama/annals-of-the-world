#!/usr/bin/env python3
"""
Batch 34 — 8 entities (Class 312): Major Dynasties — Ming, Qing, Mughal, Ottoman, Byzantine
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()
FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/312-Class-312"
FILE_PREFIX = "312"


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

    ("ming-dynasty", {
        "summary": (
            "The Ming Dynasty (大明, Dà Míng, 1368–1644 CE, China — founded by Zhu Yuanzhang, the Hongwu Emperor) was one of the most powerful dynasties in Chinese history — ruling over the world's largest and wealthiest empire for 276 years, creating the Great Wall of China in its current form, dispatching the treasure fleet voyages of Zheng He (1405–1433), building the Forbidden City (1406–1420), and presiding over the most advanced agricultural and commercial economy in the world during the 15th and 16th centuries.\n\n"
            "Founded by the monk-turned-rebel Zhu Yuanzhang after the overthrow of the Mongol Yuan Dynasty, the Ming represented the restoration of Han Chinese rule after a century of Mongol domination. The Yongle Emperor (r. 1402–1424) moved the capital from Nanjing to Beijing and built the Forbidden City — the imperial palace complex that remains the world's largest collection of preserved ancient wooden structures. Zheng He's treasure fleet expeditions (1405–1433) reached East Africa, Persia, and Southeast Asia with fleets dwarfing anything in the contemporary West.\n\n"
            "The Ming's decline was caused by fiscal exhaustion from frontier defence costs, the 'Little Ice Age' agricultural crisis, the Wanli Emperor's political disengagement, peasant rebellions led by Li Zicheng, and the rising power of the Manchu (Later Jin/Qing) state to the northeast — culminating in the Chongzhen Emperor's suicide on Coal Hill (25 April 1644) and the Qing conquest."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "One of most powerful Chinese dynasties (1368–1644, 276 years); founded by monk-rebel Zhu Yuanzhang after overthrow of Mongol Yuan; Forbidden City (1406–1420); Great Wall in current form; Zheng He treasure fleet (1405–1433) — reached East Africa, Persia, SE Asia; world's largest/wealthiest empire 15th–16th centuries; declined through fiscal exhaustion, Little Ice Age, peasant rebellions, Manchu pressure; Chongzhen suicide (25 April 1644); Qing conquest.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Yuan Dynasty's mismanagement of China's agricultural economy — combined with floods, famines, and peasant rebellions (Red Turban Rebellion, 1351–1368) — created the conditions for the Ming's founding, as Zhu Yuanzhang rose from orphaned peasant to rebel leader to emperor",
            "The Great Wall's expansion and reconstruction during the Ming — driven by the persistent threat of Mongol raids and later Manchu expansion — absorbed enormous fiscal resources, accelerating the fiscal exhaustion that contributed to the dynasty's eventual decline",
            "The 'Little Ice Age' (16th–17th century) — which reduced agricultural yields across northern China and caused the famines that drove peasant rebellions — combined with the frontier defence costs and the Wanli Emperor's political disengagement to create the conditions for the dynasty's fall"
        ],
        "effects": [
            "Zheng He's treasure fleet expeditions (1405–1433) — the largest maritime expeditions in pre-modern history, with fleets of up to 300 ships and 28,000 men — demonstrated China's maritime capability but were subsequently halted by the Confucian bureaucracy, representing the most consequential road not taken in the history of globalisation",
            "The Forbidden City (1406–1420) — built by the Yongle Emperor as the imperial palace complex — remains the world's largest collection of preserved ancient wooden structures and the most powerful physical symbol of Chinese imperial power, shaping Chinese political culture and architecture for 600 years",
            "The Ming's promotion of Neo-Confucian orthodoxy — through the civil examination system's focus on the Four Books — shaped Chinese intellectual culture for 500 years, establishing the philosophical framework that defined Chinese elite identity through the Qing period and into the modern era",
            "The Ming's decline and fall — and the Qing conquest — established the historical template for the 'dynastic cycle' as it would play out in modern Chinese consciousness: the pattern of founding virtue, mid-dynasty prosperity, late-dynasty corruption, and peasant rebellion that shaped later analyses of Chinese history"
        ],
        "relationships": [
            {"entity": "Zhu Yuanzhang (Hongwu Emperor, founder)", "relationship": "FOUNDED_BY", "note": "Zhu Yuanzhang — who rose from orphaned peasant to rebel leader to emperor — founded the Ming (1368) after overthrowing the Mongol Yuan Dynasty"},
            {"entity": "Zheng He treasure fleet voyages (1405–1433)", "relationship": "DISPATCHED_THE_GREATEST_PRE-MODERN_MARITIME_EXPEDITIONS_IN_HISTORY", "note": "The Ming dispatched Zheng He's treasure fleets (1405–1433) — the largest maritime expeditions in pre-modern history, reaching East Africa and Persia"},
            {"entity": "Forbidden City (1406–1420, Beijing)", "relationship": "BUILT_THE", "note": "The Yongle Emperor built the Forbidden City (1406–1420) — the world's largest collection of preserved ancient wooden structures and the physical embodiment of Chinese imperial power"},
            {"entity": "Great Wall of China (current form)", "relationship": "CONSTRUCTED_THE_GREAT_WALL_IN_ITS_CURRENT_FORM_DURING", "note": "The Great Wall's current form — the stone and brick structure that is the iconic image of the Wall — was built primarily during the Ming Dynasty as a defence against Mongol and Manchu incursions"},
            {"entity": "Qing Dynasty (conquered Ming 1644)", "relationship": "CONQUERED_BY_AND_SUCCEEDED_BY_THE", "note": "The Qing (Manchu) conquest of the Ming (1644) — triggered by the peasant rebellion that drove the Chongzhen Emperor to suicide — established the last imperial dynasty"}
        ],
    }),

    ("qing-dynasty", {
        "summary": (
            "The Qing Dynasty (清朝, Qīng cháo, 1644–1912 CE, China — founded by the Manchu Aisin Gioro clan) was the last imperial dynasty of China and one of the largest empires in world history — at its peak controlling 14.7 million km² (including China proper, Manchuria, Mongolia, Tibet, Xinjiang, and Taiwan) and ruling 450 million people (one-third of the world's population) in 1850. The Qing's collapse in 1912 ended 2,132 years of Chinese imperial governance and inaugurated the tumultuous modern era.\n\n"
            "The Qing was established by the Manchu leader Hong Taiji (Abahai) and his predecessor Nurhaci — who built the Later Jin state in Manchuria — and conquered China in 1644 after the Ming collapse. The Kangxi, Yongzheng, and Qianlong emperors (r. 1661–1796) presided over the 'High Qing' — a period of extraordinary territorial expansion, economic growth, and cultural achievement that made the Qing the world's largest economy (holding ~30% of global GDP in 1820). The Qing court's patronage of Chinese arts, literature, and scholarship — combined with the Manchu emperors' adoption of Confucian governance — produced the great encyclopaedic projects of the 18th century.\n\n"
            "The Qing's decline was triggered by the Opium Wars (1839–1842, 1856–1860), the Taiping Rebellion (1850–1864, 20–30 million dead), the Boxer Rebellion (1899–1901), and the New Culture and Republican movements — culminating in the abdication of the Xuantong Emperor (Puyi) on 12 February 1912, ending imperial China."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Last imperial dynasty of China (1644–1912); largest empire in history at peak (14.7 million km²); 450 million people (one-third of world's population) in 1850; ~30% of global GDP in 1820; High Qing (Kangxi/Yongzheng/Qianlong emperors); Opium Wars (1839–1842, 1856–1860); Taiping Rebellion (20–30 million dead); Boxer Rebellion; Puyi abdication (12 February 1912) — ended 2,132 years of Chinese imperial governance.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Manchu state-building by Nurhaci and Hong Taiji — who transformed the Jurchen tribal confederation into the Later Jin/Qing state with a Chinese-style bureaucracy, Manchu military organisation (Eight Banners), and Mongol alliances — created the military and administrative machine that conquered China in 1644",
            "The Ming Dynasty's collapse — through peasant rebellion, fiscal exhaustion, and the Little Ice Age — created the power vacuum that allowed the Qing to enter Beijing (1644) initially as restorers of order, then as conquerors who established their own dynasty",
            "The Qing's 'Canton System' (1757–1842) — restricting Western trade to a single port — was intended to control the terms of engagement with Western commerce, but created the tensions over trade access that led to the Opium Wars and the 'Century of Humiliation'"
        ],
        "effects": [
            "The Opium Wars (1839–1842, 1856–1860) — triggered by the Qing's destruction of British opium stocks and Britain's military response — produced the Unequal Treaties, treaty ports, extraterritoriality, and the loss of Hong Kong, establishing the template for China's 'Century of Humiliation' and shaping Chinese national memory and foreign policy to this day",
            "The Taiping Rebellion (1850–1864) — one of the deadliest conflicts in human history (20–30 million dead), driven by a syncretic Christian-Chinese millenarian movement — devastated southern China's economy and population, weakened the Qing state, and accelerated the dynasty's decline",
            "The Qing's territorial legacy — establishing Chinese sovereignty over Xinjiang (1759), Tibet (nominal), Mongolia, and Manchuria — created the territorial boundaries that the People's Republic of China claims as its own, making the Qing's conquests the direct source of China's current territorial claims and border disputes",
            "The Qing's collapse (1912) and the Republic of China's founding — followed by the warlord period, the Nationalist-Communist civil war, and the Japanese invasion — established the 'Century of Humiliation' narrative that drives Chinese Communist Party foreign policy, making the Qing's decline the foundational trauma of modern Chinese political consciousness"
        ],
        "relationships": [
            {"entity": "Nurhaci and Hong Taiji (Manchu founding rulers)", "relationship": "FOUNDED_BY_THE_MANCHU_AISIN_GIORO_CLAN_OF", "note": "Nurhaci built the Eight Banners and Later Jin state; Hong Taiji renamed it Qing — together creating the military and administrative machine that conquered China (1644)"},
            {"entity": "Opium Wars (1839–1842, 1856–1860)", "relationship": "SUFFERED_THE_FIRST_DEFEATS_OF_THE_CENTURY_OF_HUMILIATION_IN_THE", "note": "The Opium Wars produced the Unequal Treaties and treaty ports — establishing the template for China's 'Century of Humiliation' and shaping Chinese political memory to this day"},
            {"entity": "Taiping Rebellion (1850–1864, 20–30 million dead)", "relationship": "DEVASTATED_BY_THE", "note": "The Taiping Rebellion — one of history's deadliest conflicts — killed 20–30 million people and accelerated the Qing's decline"},
            {"entity": "Kangxi, Yongzheng, and Qianlong emperors (High Qing)", "relationship": "REACHED_PEAK_UNDER", "note": "The High Qing (1661–1796) under Kangxi, Yongzheng, and Qianlong saw the empire's greatest territorial extent, economic peak (~30% of global GDP in 1820), and cultural achievement"},
            {"entity": "People's Republic of China (territorial claims)", "relationship": "QING'S TERRITORIAL CONQUESTS ARE THE DIRECT SOURCE OF THE PRC'S", "note": "The PRC's territorial claims — including Xinjiang, Tibet, and the 'one China' principle — are rooted in the Qing Dynasty's territorial inheritance"}
        ],
    }),

    ("mughal-dynasty", {
        "summary": (
            "The Mughal Empire (مغلیہ سلطنت, Mug̱ẖliyah Saltanat, 1526–1857 CE, India — founded by Babur after the Battle of Panipat) was the dominant power in the Indian subcontinent for three centuries — ruling over 150–200 million people at its peak (Aurangzeb's reign), controlling an economy that may have held 25% of global GDP in 1700, and producing the architectural, artistic, and cultural legacy that defines the most familiar image of pre-modern India. The Taj Mahal, Red Fort, Fatehpur Sikri, and the Mughal miniature painting tradition are its most enduring creations.\n\n"
            "Babur (great-great-great-grandson of Timur and descendant of Genghis Khan) founded the Mughal Empire at the First Battle of Panipat (1526), defeating Ibrahim Lodi. His son Humayun and especially his grandson Akbar the Great (r. 1556–1605) established the imperial system — Akbar's policy of religious syncretism (marrying Hindu Rajput princesses, employing Hindu administrators, patronising both Islamic and Hindu arts, abolishing the jizya poll tax on non-Muslims) created the template for a multi-religious Indian empire.\n\n"
            "The Mughal decline began under Aurangzeb (r. 1658–1707) — whose re-imposition of jizya, destruction of Hindu temples, and long Deccan wars exhausted the treasury — and accelerated through the Maratha Wars, Persian invasion of Nadir Shah (1739, sacking Delhi and removing the Peacock Throne), and the East India Company's steady conquest, until the last emperor Bahadur Shah Zafar II was deposed after the 1857 uprising."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Dominant power in Indian subcontinent (1526–1857); ~25% of global GDP at peak (1700); 150–200 million people under Aurangzeb; Taj Mahal, Red Fort, Fatehpur Sikri; Mughal miniature painting tradition; Babur founded after Panipat I (1526); Akbar's religious syncretism template; Aurangzeb's jizya reimposition — accelerated decline; Nadir Shah sacked Delhi (1739, removed Peacock Throne); Bahadur Shah Zafar II deposed after 1857 uprising.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Babur's military genius and the Timurid-Mongol combined arms tradition — using field artillery (acquired from Ottoman advisors) combined with cavalry tactics — gave the Mughal forces a decisive technological advantage over Ibrahim Lodi's traditional Indian army at Panipat (1526)",
            "Akbar's policy of religious syncretism — marrying Hindu Rajput princesses, employing Hindu and Muslim administrators equally, patronising both Islamic and Hindu arts, abolishing the jizya — built the cross-religious political coalition that made Mughal rule sustainable over a predominantly Hindu population",
            "The Indian subcontinent's extraordinarily productive agricultural and artisanal economy — producing cotton textiles, silk, indigo, spices, and luxury goods for the global market — generated the revenue that funded Mughal imperial ambitions and attracted European trading companies"
        ],
        "effects": [
            "The Taj Mahal (1632–1653) — built by Shah Jahan as a mausoleum for his wife Mumtaz Mahal — is the most recognised architectural achievement in Indian history, visited by 7–8 million people annually and listed among the Seven Wonders of the Modern World; it represents the apex of Mughal architectural achievement",
            "Akbar's religious syncretism — creating a multi-religious empire that integrated Hindu, Muslim, and Jain traditions — established the template for secular governance in the subcontinent that would inspire India's founders (Nehru, Gandhi, Ambedkar) when designing the postcolonial Indian state",
            "The Mughal Empire's decline and the power vacuum it left — filled by the Marathas, Sikhs, Afghans, and ultimately the British East India Company — created the political fragmentation that enabled British colonisation of the subcontinent, making the Mughal collapse the necessary precondition for British India",
            "The Peacock Throne — the most magnificent symbol of Mughal imperial power, removed by Nadir Shah (1739) and eventually incorporated into the Iranian crown jewels — represents the transfer of South Asian wealth to Persia that demonstrates the Mughal Empire's role as the primary source of South Asian imperial prestige"
        ],
        "relationships": [
            {"entity": "Babur (founder, Battle of Panipat I 1526)", "relationship": "FOUNDED_BY", "note": "Babur — Timurid-Mongol prince — founded the Mughal Empire at Panipat (1526) using field artillery that gave him a decisive advantage over Ibrahim Lodi"},
            {"entity": "Akbar the Great (r. 1556–1605)", "relationship": "ESTABLISHED_IMPERIAL_SYSTEM_AND_SYNCRETISM_UNDER", "note": "Akbar's religious syncretism and administrative genius established the Mughal imperial system — creating the multi-religious political coalition that made three centuries of Mughal rule possible"},
            {"entity": "Taj Mahal (1632–1653, Shah Jahan)", "relationship": "PRODUCED_THE_ICONIC", "note": "The Taj Mahal — built by Shah Jahan as Mumtaz Mahal's mausoleum — is the apex of Mughal architectural achievement and the most recognised monument in Indian history"},
            {"entity": "Aurangzeb (r. 1658–1707, reimposed jizya)", "relationship": "DECLINED_UNDER_THE_POLICIES_OF", "note": "Aurangzeb's reimposition of jizya, destruction of Hindu temples, and long Deccan wars alienated Hindu subjects and exhausted the treasury — accelerating Mughal decline"},
            {"entity": "British East India Company (eventual successor power)", "relationship": "POWER_VACUUM_AFTER_DECLINE_FILLED_BY_THE_MARATHAS_AND_ULTIMATELY_THE", "note": "The Mughal decline created the power vacuum that enabled British colonisation — making the Mughal collapse the necessary precondition for the British Raj"}
        ],
    }),

    ("ottoman-dynasty", {
        "summary": (
            "The Ottoman Dynasty (Osmanoğulları, c.1299–1922 CE, Anatolia and beyond — founded by Osman I) was the ruling house of the Ottoman Empire for over six centuries — the dynasty that conquered Constantinople (1453), united the Arab world under a single Muslim empire, ruled from Vienna to the Persian Gulf and from Morocco to the Caucasus, and survived as a state until 1922 when Mustafa Kemal Atatürk abolished the sultanate. The Ottomans were the preeminent Islamic power in the early modern world and the primary geopolitical counterweight to Habsburg Europe.\n\n"
            "The Ottoman state emerged from a small Anatolian frontier principality established by Osman I (c.1299) at Söğüt — a frontier zone between Byzantine and Mongol power where Islamic warriors (ghazis) gathered to raid Byzantine territory. Under Osman's successors, especially Mehmed I, Murad I, and Mehmed II, the Ottomans expanded from Anatolia into the Balkans, captured Constantinople (29 May 1453) — ending the Byzantine Empire and establishing Ottoman control of the critical Bosphorus — and built the most powerful military-administrative state in the early modern world.\n\n"
            "Suleiman the Magnificent (r. 1520–1566) — who besieged Vienna (1529), controlled the Mediterranean, patronised the greatest Ottoman architectural achievements, and promulgated the 'Kanun' legal code — represented the Ottoman apogee. The dynasty's decline began with the Battle of Lepanto (1571) and accelerated through successive military defeats by Austria and Russia, culminating in the WWI defeat, the Allied occupation of Istanbul, and Atatürk's abolition of the sultanate (1 November 1922)."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Ruling house of Ottoman Empire (c.1299–1922, 623 years); Osman I founded c.1299; Mehmed II conquered Constantinople (29 May 1453) — ended Byzantine Empire; Suleiman the Magnificent (r. 1520–1566) — besieged Vienna, controlled Mediterranean; united Arab world under single Muslim empire; ruled Vienna to Persian Gulf, Morocco to Caucasus; primary geopolitical counterweight to Habsburg Europe; Atatürk abolished sultanate (1 November 1922).",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The collapse of Mongol power in Anatolia (after Timur's defeat of Bayezid I at Ankara, 1402) and the Byzantine Empire's weakness — reduced to Constantinople and a few coastal territories after centuries of Crusader and Mongol attacks — created the power vacuum that allowed the Ottomans to expand in Anatolia and the Balkans",
            "Mehmed II's military genius and his use of the largest artillery pieces in the world (cast by the Hungarian cannon-founder Orban) to breach Constantinople's 1,000-year-old walls (1453) was the technological breakthrough that enabled the most consequential conquest in Islamic history",
            "The Ottoman devshirme system — the collection of Christian boys from Balkan populations who were converted, educated, and trained as Ottoman soldiers (Janissaries) and administrators — created a loyalty-based meritocracy independent of the Turkic tribal aristocracy, giving the Ottoman state an extraordinarily capable professional military and bureaucracy"
        ],
        "effects": [
            "The conquest of Constantinople (1453) — ending the Byzantine Empire and establishing Ottoman control of the Bosphorus — was one of the most consequential events in world history: closing the overland Silk Road to European commerce (driving Portugal and Spain to seek oceanic routes to Asia), triggering the Greek scholar diaspora to Italy (contributing to the Renaissance), and establishing Istanbul as the capital of the greatest Muslim empire",
            "The Ottoman Empire's control of the Arab world (from 1517 — conquest of Egypt and Syria, assumption of the Caliphate by Selim I) unified the core of the Islamic world for four centuries, shaping the political and religious landscape of the Middle East that persists to the present day",
            "Suleiman's patronage of Sinan — the greatest Ottoman architect, who designed the Süleymaniye Mosque (1550–1557) and Selimiye Mosque (1569–1575) — produced the greatest examples of Islamic architecture after the medieval period, defining Ottoman visual culture",
            "The Ottoman Empire's collapse (1918–1923) — and the post-WWI partition of its Arab territories between Britain and France (Sykes-Picot Agreement) — created the modern state boundaries of the Middle East, with consequences for Arab nationalism, Palestinian statehood, Iraqi politics, and Syrian civil war that continue to define the region"
        ],
        "relationships": [
            {"entity": "Mehmed II (conquest of Constantinople 29 May 1453)", "relationship": "REACHED_DEFINING_MOMENT_UNDER", "note": "Mehmed II's conquest of Constantinople (1453) — ending the Byzantine Empire — was the most consequential event in Ottoman history and one of the most significant in world history"},
            {"entity": "Suleiman the Magnificent (r. 1520–1566, apogee)", "relationship": "REACHED_APOGEE_UNDER", "note": "Suleiman's reign (1520–1566) — with his sieges of Vienna, Mediterranean dominance, legal codification, and architectural patronage — represented the Ottoman Empire at its greatest extent and power"},
            {"entity": "Byzantine Empire (ended 1453)", "relationship": "CONQUERED_AND_REPLACED_THE", "note": "The Ottoman conquest of Constantinople (1453) ended the Byzantine Empire — the successor state to the Roman Empire — and established Istanbul as the Ottoman capital"},
            {"entity": "Mustafa Kemal Atatürk (abolished sultanate 1922)", "relationship": "SULTANATE_ABOLISHED_BY", "note": "Atatürk's abolition of the sultanate (1 November 1922) ended the Ottoman dynasty — transforming the empire's remnant into the Turkish Republic"},
            {"entity": "Sykes-Picot Agreement (1916, partition of Arab territories)", "relationship": "PARTITION_OF_ITS_ARAB_TERRITORIES_BY_THE", "note": "The post-WWI Sykes-Picot partition of Ottoman Arab territories created the modern Middle East state system — with consequences that continue to define regional politics"}
        ],
    }),

    ("ottoman-caliphate", {
        "summary": (
            "The Ottoman Caliphate (Osmanlı Hilâfeti, 1517–1924 — assumed by Ottoman Sultan Selim I after conquest of Egypt; abolished by the Grand National Assembly of Turkey, 3 March 1924) was the last universally recognised Sunni Islamic caliphate — the religio-political office claiming succession to the Prophet Muhammad as leader of the Muslim community. The Ottoman Caliphate's abolition by Atatürk in 1924 was the most significant institutional change in Sunni Islam since the Mongol destruction of the Abbasid Caliphate (1258) and remains the most contested institutional question in modern Islamic political thought.\n\n"
            "The Ottoman claim to the Caliphate was formalised after Selim I's conquest of Egypt (1517) — defeating the Mamluk Sultanate and assuming the title of 'Servant of the Two Holy Mosques' (Khadim al-Haramayn al-Sharifayn). While the historical legitimacy of the Ottoman Caliphate was debated (the Ottomans were Turkish, not Arab, and not of the Quraysh tribe that Islamic tradition required), the practical reality of Ottoman military power and their custody of Mecca and Medina gave the claim de facto acceptance across the Sunni world.\n\n"
            "The Caliphate's abolition (1924) — and the failure of subsequent attempts to revive the institution (the 1924 and 1926 Islamic Congresses in Cairo and Mecca) — has left Sunni Islam without a universally recognised political authority, a vacuum that has been contested by Saudi Arabia, Egypt's Al-Azhar, and most recently the Islamic State's self-proclaimed 'Caliphate' (2014) — demonstrating the enduring significance of the caliphal institution in Islamic political imagination."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Last universally recognised Sunni Islamic caliphate (1517–1924); assumed by Selim I after conquest of Egypt (1517); 'Servant of Two Holy Mosques'; abolished by Atatürk's Grand National Assembly (3 March 1924) — most significant institutional change in Sunni Islam since Mongol destruction of Abbasid Caliphate (1258); 1924/1926 Cairo and Mecca Congresses failed to revive; vacancy exploited by ISIS's self-proclaimed Caliphate (2014); enduring contested absence in Sunni political thought.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Selim I's conquest of Egypt (1517) and the defeat of the Mamluk Sultanate — combined with the assumption of custody of Mecca and Medina — gave the Ottomans the practical religious authority that backed their claim to the Caliphate, regardless of questions about Qurayshi lineage",
            "The practical absence of any rival claimant with comparable political and military power — after the Mongol destruction of the Abbasid Caliphate (1258) and the failure of subsequent Abbasid shadow caliphates in Cairo — created the conditions for the Ottoman Caliphate's de facto acceptance",
            "Atatürk's secular nationalist programme — which sought to separate Turkish national identity from Islamic political authority and to create a modern secular republic — drove the decision to abolish the Caliphate (1924), separating the religious institution from Turkish state power"
        ],
        "effects": [
            "The abolition of the Ottoman Caliphate (3 March 1924) removed the one institution that had provided Sunni Islam with a single recognised political authority — creating the institutional vacuum that has driven debates about Islamic governance, political Islam, and the relationship between religion and state that continue to define Muslim-majority politics",
            "The 1924 and 1926 Islamic Congresses (Cairo and Mecca) — attempting to elect a new Caliph — failed to agree on a successor, demonstrating that the post-Ottoman Islamic world lacked the consensus mechanisms to recreate the Caliphate and confirming that the institution had ended with the Ottomans",
            "The Saudi Arabian claim to religious authority over Mecca and Medina — using their role as 'Custodians of the Two Holy Mosques' (the same title the Ottomans had held) — filled part of the prestige vacuum left by the Caliphate's abolition, contributing to Saudi Arabia's disproportionate influence in post-Ottoman Sunni Islam",
            "The Islamic State's self-proclaimed Caliphate (29 June 2014) — Abu Bakr al-Baghdadi's declaration of himself as Caliph Ibrahim — demonstrated the enduring power of the caliphal concept in Islamic political imagination: the proclamation immediately attracted 30,000+ fighters and generated the most significant geopolitical crisis of 2014–2019"
        ],
        "relationships": [
            {"entity": "Selim I (assumed Caliphate 1517)", "relationship": "FORMALLY_ASSUMED_BY_THE_OTTOMAN_DYNASTY_UNDER", "note": "Selim I assumed the Caliphate (1517) after conquering Egypt and the Mamluk Sultanate — taking the title 'Servant of the Two Holy Mosques'"},
            {"entity": "Abbasid Caliphate (destroyed by Mongols 1258)", "relationship": "SUCCESSOR_TO_THE", "note": "The Ottoman Caliphate succeeded — after a 259-year interregnum — the Abbasid Caliphate destroyed by the Mongols (1258) as the recognised Sunni Islamic political authority"},
            {"entity": "Mustafa Kemal Atatürk (abolished Caliphate 3 March 1924)", "relationship": "ABOLISHED_BY", "note": "Atatürk's Grand National Assembly abolished the Caliphate (3 March 1924) — the most significant institutional change in Sunni Islam since 1258"},
            {"entity": "Islamic State (ISIS, self-proclaimed Caliphate 2014)", "relationship": "CALIPHAL_VACUUM_EXPLOITED_BY_THE", "note": "ISIS's self-proclaimed Caliphate (2014) exploited the institutional vacuum left by the 1924 abolition — demonstrating the enduring power of the caliphal concept in Islamic political imagination"},
            {"entity": "Saudi Arabia (Custodian of Two Holy Mosques)", "relationship": "PRESTIGE_VACUUM_PARTLY_FILLED_BY", "note": "Saudi Arabia's claim to 'Custodian of the Two Holy Mosques' filled part of the Ottoman Caliphate's prestige vacuum — contributing to Saudi Arabia's disproportionate influence in post-Ottoman Sunni Islam"}
        ],
    }),

    ("byzantine-empire-under-the-macedonian-dynasty", {
        "summary": (
            "The Byzantine Empire under the Macedonian Dynasty (Μακεδονική δυναστεία, 867–1056 CE) — founded by Basil I, the Macedonian — was the 'Golden Age' of Byzantium: the period of the empire's greatest territorial recovery, cultural flowering, and missionary expansion after the centuries of losses to Islam and the iconoclast controversies. Under the Macedonian emperors — especially Basil I, Leo VI, Constantine VII Porphyrogennetos, Nikephoros Phokas, John I Tzimiskes, and Basil II Bulgaroktonos — Byzantium recovered Cilicia, northern Syria, and parts of Mesopotamia from the Abbasid Caliphate, converted the Slavs and Bulgars to Orthodox Christianity, and produced the encyclopaedic compilations that preserved classical Greek learning for posterity.\n\n"
            "Basil II 'Bulgar-Slayer' (r. 976–1025) — the greatest Macedonian emperor — defeated and blinded 15,000 Bulgarian soldiers after the Battle of Kleidion (1014), sending them home in groups of 100, each led by a one-eyed man — a psychological weapon of such brutality that Tsar Samuel died of shock. Under Basil II, Byzantium reached its greatest territorial extent since Justinian, with borders from the Danube to the Euphrates.\n\n"
            "The Macedonian Dynasty's cultural achievement — the 'Macedonian Renaissance' — produced the encyclopaedias of Constantine VII Porphyrogennetos, the Menologion, and the scholarship that preserved and transmitted the Greek classical tradition, laying the groundwork for the Byzantine intellectual tradition that would later influence Italian Renaissance humanism through the Greek diaspora."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Byzantine Golden Age (867–1056); Basil I founded Macedonian dynasty; Basil II 'Bulgar-Slayer' (r. 976–1025) — blinded 15,000 Bulgarian soldiers after Kleidion (1014); greatest Byzantine territorial extent since Justinian; recovered Cilicia, northern Syria, parts of Mesopotamia from Abbasid Caliphate; converted Slavs and Bulgars to Orthodox Christianity; 'Macedonian Renaissance' — encyclopaedias of Constantine VII; Cyril and Methodius mission (predates dynasty but shapes context).",
            "significanceCategory": "continental"
        },
        "causes": [
            "Basil I's coup against Emperor Michael III (867) — and his subsequent establishment of the Macedonian dynasty — occurred at a moment of Byzantine military recovery after the Arab threat had temporarily receded, providing the political stability and military capability for the reconquest campaigns that followed",
            "The weakening of the Abbasid Caliphate through internal succession conflicts (9th–10th centuries) — and the emergence of autonomous Hamdanid and Buyid dynasties that fragmented Islamic power — created the military opportunity for Byzantine territorial reconquest under Nikephoros Phokas and John I Tzimiskes",
            "The conversion of the Bulgarian Tsar Boris I (864) and the missions of Cyril and Methodius to the Slavs — which occurred in the generation before the Macedonian dynasty but shaped its missionary context — created the conditions for the Macedonian emperors' successful Christianisation of the Balkan Slavic world"
        ],
        "effects": [
            "Basil II's defeat and blinding of 15,000 Bulgarian soldiers after Kleidion (1014) — and the subsequent Bulgarian submission — established Byzantine supremacy in the Balkans for two generations, with the psychological impact so severe that Tsar Samuel reportedly died of shock upon seeing his blinded army",
            "The 'Macedonian Renaissance' — the encyclopaedic compilation of Constantine VII Porphyrogennetos (De Administrando Imperio, De Ceremoniis) — preserved a vast body of classical Greek scholarship, Byzantine administrative knowledge, and diplomatic intelligence that constitutes one of the most valuable sources for Byzantine history",
            "The conversion of Kievan Rus' under Vladimir I (988) — facilitated by the marriage alliance with Byzantine Princess Anna (sister of Basil II) — spread Orthodox Christianity to the East Slavic world, establishing the religious and cultural foundation of Russian civilisation that endures to the present day",
            "The Macedonian Dynasty's territorial recovery — bringing Byzantine borders to the Euphrates and the Danube — created the high-water mark against which all subsequent Byzantine decline would be measured, establishing Basil II's reign as the nostalgic Golden Age of Byzantine imperial imagination"
        ],
        "relationships": [
            {"entity": "Basil I (Macedonian, founder 867)", "relationship": "FOUNDED_BY", "note": "Basil I's coup (867) established the Macedonian dynasty at the beginning of Byzantium's Golden Age"},
            {"entity": "Basil II Bulgaroktonos (r. 976–1025)", "relationship": "REACHED_GREATEST_TERRITORIAL_EXTENT_AND_POWER_UNDER", "note": "Basil II's defeat of Bulgaria (1014) and expansion to the Euphrates established the greatest Byzantine territorial extent since Justinian"},
            {"entity": "Conversion of Kievan Rus' under Vladimir I (988)", "relationship": "FACILITATED_THE_DEFINING_CULTURAL_EVENT_OF_RUSSIAN_HISTORY", "note": "Basil II's sister Anna's marriage to Vladimir I (988) facilitated the Orthodox Christianisation of Kievan Rus' — the foundational event of Russian religious and cultural identity"},
            {"entity": "Constantine VII Porphyrogennetos (encyclopaedic compilations)", "relationship": "PRODUCED_THE_MACEDONIAN_RENAISSANCE_UNDER", "note": "Constantine VII's encyclopaedic compilations (De Administrando Imperio, De Ceremoniis) preserved classical scholarship and Byzantine administrative knowledge"},
            {"entity": "Abbasid Caliphate (territorial reconquest)", "relationship": "RECONQUERED_CILICIA_AND_NORTHERN_SYRIA_FROM_THE", "note": "The Macedonian emperors' campaigns against a weakening Abbasid Caliphate recovered Cilicia, northern Syria, and parts of Mesopotamia — reversing centuries of Byzantine losses"}
        ],
    }),

    ("byzantine-empire-under-the-komnenos-dynasty", {
        "summary": (
            "The Byzantine Empire under the Komnenian Dynasty (Κομνηνός, 1081–1185 CE) — founded by Alexios I Komnenos — was the period of Byzantine military recovery and diplomatic renaissance following the catastrophic defeat at Manzikert (1071) that had lost Asia Minor to the Seljuk Turks. The Komnenian emperors — Alexios I, John II, and Manuel I — used diplomacy, military reorganisation, and the First and Second Crusades to partially stabilise the empire and project Byzantine power across the Crusader states, Serbia, Hungary, and into Italy.\n\n"
            "Alexios I Komnenos (r. 1081–1118) inherited an empire that had lost Asia Minor, the Balkans to the Normans, and was facing simultaneous threats from Pechenegs, Seljuks, and Normans. His appeal to Pope Urban II for military assistance against the Seljuks — intended to produce a small body of Western mercenaries — instead triggered the First Crusade (1096), transforming Byzantine foreign policy for the next century. Alexios's daughter Anna Komnene wrote the Alexiad — the most important Byzantine historical work — as a defence of her father's reign.\n\n"
            "Manuel I Komnenos (r. 1143–1180) — who spoke Latin, adopted Western chivalric customs, and attempted to project Byzantine power into Italy and the Crusader states — represented the height of Komnenian diplomatic ambition, but his defeat at Myriokephalon (1176) by the Seljuks demonstrated that Byzantine territorial recovery in Asia Minor was not achievable, and his Western-oriented policies alienated the Byzantine elite."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Byzantine military recovery after Manzikert (1081–1185); Alexios I founded dynasty; Alexios I's appeal to Pope Urban II inadvertently triggered First Crusade (1096); Anna Komnene's Alexiad — most important Byzantine historical work; John II military campaigns; Manuel I — Western chivalric influence, defeat at Myriokephalon (1176); Komnenian diplomatic renaissance; partial stabilisation after catastrophic Seljuk conquest of Asia Minor.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Battle of Manzikert (1071) — in which the Seljuk Sultan Alp Arslan defeated and captured Emperor Romanos IV Diogenes — opened Asia Minor to Seljuk settlement and created the existential crisis that drove Alexios I's military and political revolution",
            "Alexios I's diplomatic genius — his ability to play off Normans, Seljuks, Crusaders, and Pechenegs against each other while rebuilding Byzantine military capability — created the strategic space for Komnenian recovery without the financial and manpower resources that the earlier Byzantine state had possessed",
            "The First Crusade's unexpected military success — capturing Antioch (1098) and Jerusalem (1099) against all odds — created the Crusader states that became Byzantine client territories and provided Byzantine diplomacy with new leverage over Western powers"
        ],
        "effects": [
            "Alexios I's appeal to Pope Urban II (1095) — intended to produce Western mercenaries for Byzantine service — instead triggered the First Crusade, with consequences that shaped the relationship between Eastern and Western Christianity, the Holy Land, and Islamic-Christian relations for centuries",
            "Anna Komnene's Alexiad — written after her failed conspiracy against her brother John II — is the most important Byzantine historical work: a sophisticated, literary account of the First Crusade from a Byzantine perspective that remains a primary historical source for the period",
            "The Komnenian system's reliance on pronoia (land grants) rather than a professional army — driven by fiscal constraints — transformed Byzantine military organisation and eventually weakened central authority, contributing to the fragmentation of power that made the empire vulnerable to the Fourth Crusade (1204)",
            "Manuel I's pro-Western policies — culminating in his defeat at Myriokephalon (1176) — demonstrated that Byzantium could not recover Asia Minor from the Seljuks and could not project power into Italy, setting the limits of Komnenian ambition and confirming the empire's reduced strategic position"
        ],
        "relationships": [
            {"entity": "Alexios I Komnenos (founder 1081)", "relationship": "FOUNDED_BY", "note": "Alexios I's coup (1081) established the Komnenian dynasty — and his appeal to Urban II inadvertently triggered the First Crusade"},
            {"entity": "First Crusade (1096–1099)", "relationship": "INADVERTENTLY_TRIGGERED_BY_ALEXIOS_IS_APPEAL_TO_POPE_URBAN_II", "note": "Alexios I's request for Western mercenaries against the Seljuks was answered with the full First Crusade — transforming Byzantine foreign policy for a century"},
            {"entity": "Anna Komnene (Alexiad)", "relationship": "PRODUCED_THE_MOST_IMPORTANT_BYZANTINE_HISTORICAL_WORK_IN_THE", "note": "Anna Komnene's Alexiad — a defence of her father Alexios I — is the most important Byzantine historical source for the First Crusade period"},
            {"entity": "Battle of Manzikert (1071, Seljuk conquest of Asia Minor)", "relationship": "FOUNDED_IN_RESPONSE_TO_THE_CRISIS_CAUSED_BY_THE", "note": "Alexios I's Komnenian dynasty was the political response to the existential crisis created by Manzikert (1071) and the Seljuk conquest of Asia Minor"},
            {"entity": "Fourth Crusade (1204, sack of Constantinople)", "relationship": "KOMNENIAN_STRUCTURAL_WEAKNESSES_CONTRIBUTED_TO_THE_VULNERABILITY_THAT_ENABLED_THE", "note": "The Komnenian reliance on pronoia rather than professional armies weakened central authority — contributing to the fragmentation that made Constantinople vulnerable to the Fourth Crusade (1204)"}
        ],
    }),

    ("byzantine-empire-under-the-palaiologos-dynasty", {
        "summary": (
            "The Byzantine Empire under the Palaiologos Dynasty (Παλαιολόγος, 1261–1453 CE) — founded by Michael VIII Palaiologos — was the final dynasty of the Byzantine Empire, presiding over two centuries of terminal decline from a small Anatolian rump state (after the Latin Empire, 1204–1261) to the Ottoman conquest of Constantinople (29 May 1453). The Palaiologos period is paradoxically one of the most intellectually and culturally productive in Byzantine history — the 'Palaiologos Renaissance' — even as the empire's political power reduced to a few cities.\n\n"
            "Michael VIII Palaiologos recaptured Constantinople from the Latin Empire (1261) — restoring Byzantine rule after 57 years of Latin occupation — but the 'restored' empire was a shadow of its former self: controlling only Constantinople, the Peloponnese, and parts of Greece, with its economy dominated by Genoese and Venetian merchants who had received commercial privileges in return for naval support. The Palaiologos emperors were in a permanent state of political bankruptcy — seeking Western military aid against the Ottomans in exchange for promises of church union (repeatedly made, never implemented) that their own Orthodox population rejected.\n\n"
            "The 'Palaiologos Renaissance' — the last flowering of Byzantine intellectual and artistic culture — produced the mosaics of the Chora Church, the scholarship of Gregory Palamas (Hesychasm), Plethon (neo-Platonic philosophy), and the Byzantine scholars whose exodus to Italy after 1453 brought Greek manuscripts and classical scholarship that fuelled the Italian Renaissance."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Final Byzantine dynasty (1261–1453); Michael VIII recaptured Constantinople from Latin Empire (1261); terminal decline from rump state to Ottoman conquest (29 May 1453); 'Palaiologos Renaissance' — Chora Church mosaics, Hesychasm (Gregory Palamas), Plethon; Byzantine scholars' exile to Italy — Greek manuscripts and learning fuelled Italian Renaissance; Constantine XI Palaiologos last emperor (died defending Constantinople); 2,000 years of continuous Roman-Byzantine state ended 29 May 1453.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Michael VIII Palaiologos's recapture of Constantinople from the Latin Empire (1261) — using the military alliance with Genoa against Venice — restored Byzantine rule but left the empire in a structurally weak position: economically dependent on Italian merchant republics and militarily unable to recover Asia Minor from the Ottomans",
            "The Ottoman Empire's systematic conquest of Byzantine territories throughout the 14th century — reducing Byzantium to Constantinople, Thessaloniki, and the Peloponnese by 1400 — created the inescapable strategic situation in which the empire had no path to survival without Western military intervention that was never forthcoming",
            "The theological controversy over Hesychasm — Gregory Palamas's mystical theology of divine energies, which split the Byzantine church between Palamite and anti-Palamite factions — paralysed Byzantine intellectual and political life at the moment when unified resistance to Ottoman expansion was most needed"
        ],
        "effects": [
            "The Ottoman conquest of Constantinople (29 May 1453) — in which Constantine XI Palaiologos died defending the city, and the Ottoman army under Mehmed II breached the Theodosian Walls — ended the Roman-Byzantine state that had existed in continuous form for 2,000 years, establishing one of the most symbolically significant dates in world history",
            "The Byzantine scholars' exodus to Italy — carrying Greek manuscripts, classical learning, and the Platonic philosophical tradition — provided the primary intellectual resources for the Italian Renaissance, with figures like Bessarion, George Gemistos Plethon, and later Janus Lascaris bringing the classical Greek tradition to Western humanists",
            "The 'Palaiologos Renaissance' — the mosaics of the Chora Church (Kariye Camii), the frescoes of Mistra, and the scholarship of Plethon and Scholarios — represented one of the last great creative periods of Byzantine art and learning, producing works that influenced both Byzantine Orthodox aesthetics and Italian Renaissance art",
            "The fall of Constantinople's psychological impact on Western Christendom — coming 20 years after the Council of Florence (1439) had attempted to reunite Eastern and Western Christianity — deepened the permanent fracture between Orthodox and Catholic Christianity and established the Ottoman Empire as the definitive successor to Byzantine power in the eastern Mediterranean"
        ],
        "relationships": [
            {"entity": "Michael VIII Palaiologos (founder 1261)", "relationship": "FOUNDED_BY", "note": "Michael VIII recaptured Constantinople from the Latin Empire (1261) — restoring Byzantine rule, though to a shadow of the empire's former extent and power"},
            {"entity": "Fall of Constantinople (29 May 1453)", "relationship": "ENDED_WITH_THE_CATASTROPHIC", "note": "The Ottoman conquest of Constantinople (29 May 1453) — in which the last emperor Constantine XI died defending the city — ended the 2,000-year Roman-Byzantine state"},
            {"entity": "Byzantine scholars' exile to Italy (Renaissance)", "relationship": "SOURCE_OF_THE_GREEK_MANUSCRIPTS_AND_SCHOLARSHIP_THAT_FUELLED_THE_ITALIAN_RENAISSANCE", "note": "Byzantine scholars carrying Greek manuscripts — Bessarion, Plethon, Lascaris — brought the classical Greek tradition to Italy, providing essential resources for the Italian Renaissance"},
            {"entity": "Chora Church mosaics and Palaiologos Renaissance", "relationship": "PRODUCED_THE_LAST_GREAT_CREATIVE_PERIOD_OF_BYZANTINE_ART", "note": "The Palaiologos Renaissance — Chora Church mosaics, Mistra frescoes, Plethon's neo-Platonism — was a final flowering of Byzantine culture amid political collapse"},
            {"entity": "Ottoman Empire (successor power)", "relationship": "CONQUERED_BY_AND_SUCCEEDED_IN_THE_EASTERN_MEDITERRANEAN_BY_THE", "note": "The Ottoman conquest (1453) established the Ottomans as the definitive successors to Byzantine power — making Istanbul the capital of the new Islamic empire"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 34 — {len(ENTITIES)} entities (Class 312: Major Dynasties)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
