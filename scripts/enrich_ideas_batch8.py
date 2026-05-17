#!/usr/bin/env python3
"""
Batch 8: 8 ideas, movements and institutions from multiple class folders.
Entities: sufism, world-trade-organization, african-union,
          indian-ocean-trade-network, age-of-sail, portuguese-age-of-discovery,
          microsoft, cern.
subjectHeadings always written as list (Appwrite schema requirement).
"""
import json, os, glob, unicodedata
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()

# Each entry: slug → {enrichment dict, file_path}
FILE_MAP = {
    "sufism":                       "data/appwrite-export/entities/340-Class-340/340sufism.json",
    "world-trade-organization":     "data/appwrite-export/entities/370-Class-370/370world-trade-organization.json",
    "african-union":                "data/appwrite-export/entities/370-Class-370/370african-union.json",
    "indian-ocean-trade-network":   "data/appwrite-export/entities/682-Class-682/682indian-ocean-trade-network.json",
    "age-of-sail":                  "data/appwrite-export/entities/682-Class-682/682age-of-sail.json",
    "portuguese-age-of-discovery":  "data/appwrite-export/entities/682-Class-682/682portuguese-age-of-discovery.json",
    "microsoft":                    "data/appwrite-export/entities/330-Class-330/330microsoft.json",
    "cern":                         "data/appwrite-export/entities/370-Class-370/370cern.json",
}

ENRICHMENTS = {
    "sufism": {
        "summary": (
            "Sufism (Arabic: Tasawwuf) is the mystical dimension of Islam — an inward "
            "spiritual path emphasising direct personal experience of the divine, purification "
            "of the soul, and love of God — that emerged in the 8th century CE as a reaction "
            "against the perceived worldliness of the early Umayyad caliphate and became the "
            "primary vehicle by which Islam spread into Sub-Saharan Africa, South Asia, "
            "Central Asia, and Southeast Asia.\n\n"
            "Sufi orders (tariqas), founded around revered masters (shaykhs), developed "
            "distinctive devotional practices: dhikr (rhythmic remembrance of God), sama "
            "(sacred music and poetry), and in some orders the whirling meditation of the "
            "Mevlevi dervishes founded by Jalal al-Din Rumi (1207–1273). Rumi's Masnavi "
            "and the poetry of Hafez and Ibn Arabi represent the peak of Islamic mystical "
            "literature — beloved not just by Muslims but by readers worldwide. Major orders "
            "include the Qadiri, Naqshbandi, Chishti, and Mevlevi tariqas, each with millions "
            "of followers today.\n\n"
            "Sufism played a pivotal role in the peaceful spread of Islam through merchants "
            "and wandering dervishes rather than conquest — particularly in West Africa, "
            "Bengal, and the Indonesian archipelago. It generated fierce opposition from "
            "Salafi and Wahhabi reform movements from the 18th century onwards and remains "
            "a major fault line within contemporary Islam."
        ),
        "causes": [
            {"title": "Early Islamic expansion and the luxury of Umayyad court life prompted a counter-movement of ascetic piety among devout Muslims in the 8th century", "type": "EventWindow", "year": "c. 750 CE, Middle East"},
            {"title": "Influence of Christian monasticism, Neoplatonist philosophy, and Persian Zoroastrian mysticism provided intellectual frameworks for Islamic inward spirituality", "type": "Idea", "year": "c. 700–900 CE, Middle East"},
        ],
        "effects": [
            {"title": "Sufi missionaries spread Islam peacefully to Sub-Saharan Africa, Bengal, Central Asia, and Southeast Asia, making Sufism the main vehicle of Islamic globalisation", "type": "Movement", "year": "c. 1000–1700, Global"},
            {"title": "Rumi's Masnavi and the poetry of Hafez became world literature, translated into hundreds of languages and among the most widely read poetry in the world today", "type": "Text", "year": "c. 1250–present, Global"},
            {"title": "Sufi orders built dense networks of lodges (khanqahs) that served as hostels, schools, and community centres across the Muslim world — the social infrastructure of Islamic society", "type": "Institution", "year": "c. 900–present, Global"},
            {"title": "Wahhabi and Salafi reform movements from 18th century onwards defined themselves partly in opposition to Sufi 'innovations', creating an intra-Islamic theological fault line that persists", "type": "Movement", "year": "c. 1744–present, Global"},
        ],
        "relationships": [
            {"targetSlug": "rumi", "verb": "INFLUENCES", "note": "Rumi founded the Mevlevi Sufi order and wrote the Masnavi — Sufism's most celebrated mystical text"},
            {"targetSlug": "islam", "verb": "INFLUENCES", "note": "Sufism is the mystical tradition within Islam, shaping its spiritual and cultural life for 1,200 years"},
            {"targetSlug": "ibn-arabi", "verb": "INFLUENCES", "note": "Ibn Arabi's philosophical Sufism (wahdat al-wujud) shaped Sufi intellectual tradition across the Islamic world"},
            {"targetSlug": "wahhabism", "verb": "INFLUENCES", "note": "Wahhabism arose partly as a reaction against Sufi 'innovations' and saint veneration"},
        ],
        "places": ["Baghdad, Iraq", "Konya, Turkey", "Global"],
        "subjects": ["Sufism", "Islam", "Mysticism", "Rumi", "Spirituality", "Islamic Culture", "Tariqas"],
        "subjectHeadings": ["Idea — Mysticism — Global — Medieval"],
        "frameworks": ["religious-history", "cultural-history"],
        "era": "Medieval",
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Sufism is the mystical heart of Islam and its most effective missionary force — spreading the faith peacefully across three continents and producing the world's most widely read mystical poetry in Rumi and Hafez.",
            "significanceCategory": "world-changing"
        },
    },
    "world-trade-organization": {
        "summary": (
            "The World Trade Organization (WTO) is an intergovernmental body established in "
            "1995 that succeeded the GATT (General Agreement on Tariffs and Trade, 1947) as "
            "the principal multilateral framework for regulating international trade. "
            "With 164 member states representing 98% of world trade, it sets the rules by "
            "which nations buy and sell from each other, adjudicates trade disputes, and "
            "negotiates new trade agreements.\n\n"
            "The WTO's Dispute Settlement Body (DSB) is one of the most active international "
            "legal forums in the world, having handled over 600 cases since 1995. Its "
            "most-favoured-nation (MFN) and national treatment principles — obliging members "
            "to offer the same trade terms to all members — have been the backbone of post-"
            "war trade liberalisation. The organisation's crowning achievement remains the "
            "Uruguay Round agreements (1994) that created it, expanding GATT disciplines "
            "from goods to services (GATS) and intellectual property (TRIPS).\n\n"
            "The WTO's credibility has been challenged by the failure of the Doha Development "
            "Round (launched 2001, effectively stalled since 2008), by US blocking of "
            "Appellate Body judge appointments (2019), and by the rise of bilateral and "
            "regional trade agreements that bypass its multilateral framework. China's 2001 "
            "accession — the most complex in WTO history — has generated persistent disputes "
            "about state capitalism and the organisation's adequacy for 21st-century trade."
        ),
        "causes": [
            {"title": "GATT (1947) provided 47 years of tariff reduction experience that required an upgraded institution with binding dispute settlement to manage 1990s trade volumes", "type": "Institution", "year": "1947–1994, Global"},
            {"title": "Uruguay Round (1986–1994) negotiations expanded trade rules to services and intellectual property and created the institutional architecture of the WTO", "type": "EventWindow", "year": "1986–1994, Global"},
        ],
        "effects": [
            {"title": "WTO membership drove unprecedented global trade growth — world merchandise trade increased from $6 trillion in 1995 to over $25 trillion by 2022", "type": "EventWindow", "year": "1995–2022, Global"},
            {"title": "Dispute Settlement Body handled 600+ cases, creating a de facto body of international trade law that constrains even the world's largest economies", "type": "Institution", "year": "1995–present, Global"},
            {"title": "China's 2001 WTO accession integrated the world's most populous nation into the rules-based trade system, accelerating its economic rise and generating structural tensions", "type": "EventWindow", "year": "2001–present, Global"},
            {"title": "US blockage of Appellate Body (2019–present) created a constitutional crisis for the WTO and signalled great-power disillusionment with multilateral rules-based order", "type": "EventWindow", "year": "2019–present, Global"},
        ],
        "relationships": [
            {"targetSlug": "gatt", "verb": "INFLUENCES", "note": "The WTO succeeded and institutionalised GATT, inheriting 47 years of tariff negotiation precedents"},
            {"targetSlug": "globalization", "verb": "CAUSES", "note": "The WTO's tariff reduction and rules framework was a primary driver of post-1995 economic globalisation"},
            {"targetSlug": "china", "verb": "INFLUENCES", "note": "China's 2001 WTO accession was the most consequential single membership in the organisation's history"},
            {"targetSlug": "united-states", "verb": "INFLUENCES", "note": "The US designed the WTO but has also been its most disruptive recent challenger, blocking the Appellate Body"},
        ],
        "places": ["Geneva, Switzerland", "Global"],
        "subjects": ["World Trade Organization", "International Trade", "Globalization", "Geneva", "GATT", "Trade Policy"],
        "subjectHeadings": ["Institution — International Organization — Global — Contemporary"],
        "frameworks": ["economic-history", "world-systems"],
        "era": "Contemporary",
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "The WTO is the constitutional framework for $25 trillion in annual world trade — the multilateral rules engine that drove post-Cold War economic globalisation and is now being stress-tested by US-China rivalry.",
            "significanceCategory": "world-changing"
        },
    },
    "african-union": {
        "summary": (
            "The African Union (AU) is a continental organisation of 55 member states founded "
            "in 2002 as the successor to the Organisation of African Unity (OAU, 1963–2002). "
            "Modelled loosely on the European Union, the AU seeks to promote political "
            "integration, economic development, peace, and security across Africa — a "
            "continent of 1.4 billion people in 55 diverse nations.\n\n"
            "The AU's Constitutive Act (2000) made a historic break from the OAU's principle "
            "of non-interference by permitting intervention in member states in cases of war "
            "crimes, genocide, or crimes against humanity — a major evolution in African "
            "sovereignty norms. Its institutions include the AU Commission (Addis Ababa), "
            "the Pan-African Parliament, the African Court on Human and Peoples' Rights, "
            "and the African Peace and Security Architecture (APSA). The AU's African "
            "Continental Free Trade Area (AfCFTA, 2021) is the world's largest free trade "
            "area by number of participating countries.\n\n"
            "The AU faces significant institutional challenges: chronic underfunding (only "
            "25% of its budget comes from member states, the rest from external donors), "
            "limited enforcement capacity, and the political challenge that 20+ member states "
            "have experienced coups or unconstitutional changes of government since 2000. "
            "Nevertheless, it has deployed peacekeeping missions in Somalia, Sudan, and the "
            "Central African Republic and represents Africa's most ambitious attempt at "
            "continental governance."
        ),
        "causes": [
            {"title": "OAU's failure to prevent African conflicts and humanitarian crises in the 1990s (Rwanda genocide, Congo wars, Somalia collapse) demonstrated the need for a more robust continental body", "type": "Institution", "year": "1963–2001, Africa"},
            {"title": "Muammar Gaddafi's sustained advocacy for an African Union modelled on the EU provided the political momentum to replace the OAU in 2002", "type": "Person", "year": "1999–2002, Africa"},
        ],
        "effects": [
            {"title": "AU Constitutive Act's right of intervention in cases of genocide/war crimes created a new norm of conditional sovereignty in Africa, marking a departure from colonial-era non-interference", "type": "Text", "year": "2000, Africa"},
            {"title": "African Continental Free Trade Area (AfCFTA, 2021) created a single African market of 1.4 billion people — the world's largest by country count", "type": "Institution", "year": "2021, Africa"},
            {"title": "AU peacekeeping missions (AMISOM in Somalia, AMIS in Darfur) established African multilateral security responses where the UN was unable or unwilling to act", "type": "EventWindow", "year": "2004–present, Africa"},
        ],
        "relationships": [
            {"targetSlug": "organisation-of-african-unity", "verb": "INFLUENCES", "note": "The AU replaced the OAU in 2002, inheriting its institutions but adopting a more interventionist mandate"},
            {"targetSlug": "ethiopia", "verb": "INFLUENCES", "note": "Ethiopia hosts the AU headquarters in Addis Ababa — reflecting its symbolic centrality to Pan-African unity"},
            {"targetSlug": "pan-africanism", "verb": "INFLUENCES", "note": "The AU is the institutional embodiment of Pan-Africanism first articulated by Kwame Nkrumah and others in the 1950s"},
            {"targetSlug": "african-continental-free-trade-area", "verb": "CAUSES", "note": "The AU negotiated and launched the AfCFTA — the world's largest free trade area by participant count"},
        ],
        "places": ["Addis Ababa, Ethiopia", "Africa"],
        "subjects": ["African Union", "Africa", "Pan-Africanism", "International Organization", "Peacekeeping", "Continental Integration"],
        "subjectHeadings": ["Institution — International Organization — Africa — Contemporary"],
        "frameworks": ["postcolonial-history", "political-history"],
        "era": "Contemporary",
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "The African Union is the institutional embodiment of Pan-Africanism, the author of the world's largest free trade area, and the continent's primary — if still imperfect — platform for collective security and continental governance.",
            "significanceCategory": "continental"
        },
    },
    "indian-ocean-trade-network": {
        "summary": (
            "The Indian Ocean Trade Network was one of the ancient and medieval world's "
            "most extensive and durable commercial systems — a web of sea routes connecting "
            "East Africa, the Arabian Peninsula, the Indian subcontinent, Southeast Asia, "
            "and China that moved spices, silk, cotton, ivory, gold, and ceramics for at "
            "least 2,000 years before the Portuguese disruption of 1497–1510.\n\n"
            "Uniquely among pre-modern trade networks, it was driven by monsoon winds — the "
            "southwest monsoon (June–September) carried ships from Arabia and Africa to India "
            "and Southeast Asia; the northeast monsoon (November–March) carried them back. "
            "This predictable seasonal rhythm enabled annual trading cycles without the need "
            "for oars or large crews, making it more efficient than overland routes. Arab, "
            "Indian, Malay, Swahili, and Chinese merchants all operated within it; Islam "
            "spread along its routes from the 9th century onwards, carried by Arab and Indian "
            "Muslim merchants.\n\n"
            "The network built the Swahili city-states of East Africa (Kilwa, Mombasa, "
            "Zanzibar), funded medieval South Indian kingdoms, connected Song Dynasty China's "
            "export industries to Mediterranean luxury markets, and distributed Southeast "
            "Asian spices — cloves, nutmeg, pepper — that drove European exploration. "
            "Vasco da Gama's 1497 voyage used captured Arab navigational knowledge to "
            "break into the network, ultimately transforming it into the colonial trading "
            "system."
        ),
        "causes": [
            {"title": "Indian Ocean monsoon wind system — predictable and reversing — created the physical infrastructure for regular long-distance sailing without the need for oars or large crews", "type": "Idea", "year": "c. 2000 BCE–present, Indian Ocean"},
            {"title": "Demand for Indian Ocean luxury goods (spices, silk, cotton) in Rome, Arabia, and China drove merchants to develop regular commercial routes from the 1st century BCE", "type": "EventWindow", "year": "c. 100 BCE–100 CE, Global"},
        ],
        "effects": [
            {"title": "Islam spread via Indian Ocean trade routes from the 9th century, reaching East Africa, South India, and Southeast Asia centuries before any military conquest", "type": "Movement", "year": "c. 900–1500 CE, Indian Ocean"},
            {"title": "Swahili city-states (Kilwa, Mombasa, Zanzibar) emerged as wealthy entrepôts on the East African coast, creating a distinctive Swahili synthesis of African and Islamic culture", "type": "Institution", "year": "c. 900–1500 CE, East Africa"},
            {"title": "European demand for Indian Ocean spices drove the Age of Exploration — Portuguese, Spanish, Dutch, and English expansion that reshaped the world after 1492", "type": "Movement", "year": "c. 1415–1600, Global"},
            {"title": "Vasco da Gama's 1497–99 voyage, using captured Arab navigational charts, broke the Arab-Indian monopoly and began European domination of Indian Ocean trade", "type": "EventWindow", "year": "1497–1499, Indian Ocean"},
        ],
        "relationships": [
            {"targetSlug": "vasco-da-gama", "verb": "INFLUENCES", "note": "Vasco da Gama's 1497 voyage broke the Arab-Indian trade monopoly and began European domination of the Indian Ocean"},
            {"targetSlug": "arab-slave-trade", "verb": "INFLUENCES", "note": "The Indian Ocean network facilitated the Arab slave trade from East Africa alongside its commercial commodities"},
            {"targetSlug": "swahili-coast", "verb": "INFLUENCES", "note": "Swahili city-states were built on Indian Ocean trade wealth and blended African, Arab, and Indian cultures"},
            {"targetSlug": "spice-trade", "verb": "INFLUENCES", "note": "Indian Ocean spice routes were the origin and economic engine of the entire pre-modern long-distance trade system"},
        ],
        "places": ["Indian Ocean", "East Africa", "Arabian Sea", "Bay of Bengal"],
        "subjects": ["Indian Ocean Trade", "Maritime Trade", "Spice Trade", "Islam", "East Africa", "Swahili", "Monsoon"],
        "subjectHeadings": ["Movement — Trade Network — Indian Ocean — Classical"],
        "frameworks": ["world-systems", "economic-history"],
        "era": "Classical",
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "The Indian Ocean Trade Network was the ancient world's most efficient commercial system — the monsoon's predictable winds making it the original engine of globalisation, carrying Islam, spices, and ideas across half the world for 2,000 years.",
            "significanceCategory": "world-changing"
        },
    },
    "age-of-sail": {
        "summary": (
            "The Age of Sail was the period — roughly 1571 to 1862 — during which wind-powered "
            "sailing ships reached their technological peak and dominated world naval power, "
            "global commerce, and European imperial expansion. It was bounded at one end by "
            "the Battle of Lepanto (1571), the last great Mediterranean galley battle, and at "
            "the other by the transition to steam propulsion after the American Civil War.\n\n"
            "During this period, European powers built ocean-going warships capable of "
            "circling the globe, carrying hundreds of cannons, and projecting force to every "
            "inhabited coastline on Earth. The defining vessel was the 'ship of the line' — "
            "a three-masted warship carrying 60–120 guns on two or three decks. Nelson's "
            "victory at Trafalgar (1805) with 27 ships against 33 Franco-Spanish vessels "
            "established British naval supremacy that lasted until World War I. The East India "
            "companies of England, the Netherlands, and France used Age of Sail shipping to "
            "build the world's first global corporations and the trading empires that "
            "dominated the Indian Ocean and the Atlantic.\n\n"
            "The Age of Sail enabled the Atlantic slave trade (12 million Africans transported "
            "1500–1900), the Columbian Exchange of crops and diseases, and the European "
            "colonisation of the Americas, Africa, and Asia that created the modern world's "
            "economic and political geography."
        ),
        "causes": [
            {"title": "Portuguese and Spanish development of the caravel and carrack in the 15th century created ocean-going vessels capable of sailing against the wind and carrying heavy armament", "type": "Idea", "year": "c. 1420–1500, Europe"},
            {"title": "Lateen sail, magnetic compass, and astrolabe navigation combined to make open-ocean navigation predictable enough for commercial round-trip voyages", "type": "Idea", "year": "c. 1300–1500, Europe"},
        ],
        "effects": [
            {"title": "European colonial empires — Spanish, Portuguese, Dutch, British, French — were built entirely on Age of Sail logistics, making it the enabling technology of global colonialism", "type": "EventWindow", "year": "c. 1492–1800, Global"},
            {"title": "Battle of Trafalgar (1805) established British naval supremacy that translated into 'Pax Britannica' — a century of British-regulated global maritime commerce", "type": "EventWindow", "year": "1805, Atlantic Ocean"},
            {"title": "Atlantic slave trade transported 12 million Africans to the Americas using Age of Sail vessels, creating the African diaspora and the plantation economies of the New World", "type": "EventWindow", "year": "c. 1500–1867, Atlantic Ocean"},
            {"title": "Steam propulsion (paddle steamers from 1819, screw propeller from 1836) made the Age of Sail obsolete by the 1860s, ending 300 years of wind-power naval supremacy", "type": "Idea", "year": "c. 1819–1862, Global"},
        ],
        "relationships": [
            {"targetSlug": "battle-of-trafalgar", "verb": "INFLUENCES", "note": "Trafalgar (1805) was the Age of Sail's defining naval battle, establishing British supremacy for a century"},
            {"targetSlug": "atlantic-slave-trade", "verb": "INFLUENCES", "note": "Age of Sail ships were the instrument of the Atlantic slave trade, transporting 12 million Africans"},
            {"targetSlug": "british-empire", "verb": "INFLUENCES", "note": "The British Empire's global reach depended entirely on Age of Sail naval and commercial supremacy"},
            {"targetSlug": "east-india-company", "verb": "INFLUENCES", "note": "The English and Dutch East India Companies used Age of Sail ships to build the first global corporations"},
        ],
        "places": ["Atlantic Ocean", "Pacific Ocean", "Indian Ocean", "Europe"],
        "subjects": ["Age of Sail", "Naval History", "Maritime", "British Empire", "Colonialism", "Slave Trade", "Trade"],
        "subjectHeadings": ["Movement — Maritime Era — Global — Early Modern"],
        "frameworks": ["world-systems", "military-history"],
        "era": "Early Modern",
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "The Age of Sail was the enabling technology of European global domination — its warships and merchant vessels created the colonial empires, the Atlantic slave trade, and the globalised world economy that define the modern era.",
            "significanceCategory": "world-changing"
        },
    },
    "portuguese-age-of-discovery": {
        "summary": (
            "The Portuguese Age of Discovery (c. 1415–1543) was the century-long programme "
            "of systematic maritime exploration initiated by Prince Henry the Navigator and "
            "pursued by successive Portuguese monarchs that opened the Atlantic coast of "
            "Africa, rounded the Cape of Good Hope, reached India (Vasco da Gama, 1497), "
            "Brazil (Cabral, 1500), and the Spice Islands (Magellan's crew, 1522) — the most "
            "concentrated burst of geographical knowledge acquisition in recorded history.\n\n"
            "Beginning with the capture of Ceuta (1415), Portugal systematically pushed south "
            "along the African coast, establishing a series of trading posts and fortresses. "
            "Bartolomeu Dias rounded the Cape of Good Hope in 1488; Vasco da Gama reached "
            "Calicut in 1498 using captured Arab navigational charts, destroying the Arab-"
            "Indian spice trade monopoly. The Treaty of Tordesillas (1494), dividing the "
            "non-Christian world between Portugal and Spain, made Portugal master of Africa, "
            "Asia, and Brazil.\n\n"
            "Portugal built the first global maritime empire — Estado da India — connecting "
            "Lisbon, Goa, Malacca, and Macau with a network of fortresses and trading posts "
            "that extracted Asian spices, African slaves, and Brazilian timber. By the late "
            "16th century, the Dutch and English had copied and supplanted Portugal's methods, "
            "but its cartographic, navigational, and linguistic legacy (Portuguese remains an "
            "official language across four continents) endures."
        ),
        "causes": [
            {"title": "Prince Henry the Navigator's systematic programme of maritime exploration, funding cartographers, navigators, and shipbuilders at Sagres, created the institutional infrastructure of discovery", "type": "Person", "year": "1415–1460, Portugal"},
            {"title": "Portuguese demand for a direct sea route to Asian spices — bypassing Arab and Venetian intermediaries — was the primary commercial motive for Atlantic exploration", "type": "EventWindow", "year": "c. 1400–1500, Portugal"},
        ],
        "effects": [
            {"title": "Vasco da Gama's 1497–99 voyage to India destroyed the Arab-Indian spice trade monopoly and permanently shifted global commercial geography from land to sea routes", "type": "EventWindow", "year": "1497–1499, Indian Ocean"},
            {"title": "Treaty of Tordesillas (1494) divided the non-Christian world between Portugal and Spain, establishing the first global imperial partition and making Portugal master of Africa and Asia", "type": "Text", "year": "1494, Tordesillas"},
            {"title": "Estado da India — Portugal's Asian trading empire — connected four continents through a network of fortresses and trading posts, creating the world's first global commercial network", "type": "Institution", "year": "c. 1500–1650, Global"},
            {"title": "Portuguese language and Catholic mission spread to four continents; today Portuguese is spoken by 260 million people as a direct legacy of the Age of Discovery", "type": "Movement", "year": "c. 1500–present, Global"},
        ],
        "relationships": [
            {"targetSlug": "vasco-da-gama", "verb": "INFLUENCES", "note": "Vasco da Gama's 1498 voyage to India was the crowning achievement of the Portuguese Age of Discovery"},
            {"targetSlug": "henry-the-navigator", "verb": "INFLUENCES", "note": "Prince Henry the Navigator initiated and systematised the Portuguese programme of exploration"},
            {"targetSlug": "treaty-of-tordesillas", "verb": "CAUSES", "note": "Portuguese discoveries led directly to the 1494 Tordesillas division of the world between Portugal and Spain"},
            {"targetSlug": "spice-trade", "verb": "INFLUENCES", "note": "Portuguese discovery of the Cape route destroyed the Arab-Venetian spice trade monopoly"},
        ],
        "places": ["Lisbon, Portugal", "Cape of Good Hope, South Africa", "Indian Ocean", "Atlantic Ocean"],
        "subjects": ["Portugal", "Age of Discovery", "Maritime Exploration", "Vasco da Gama", "Spice Trade", "Colonialism"],
        "subjectHeadings": ["Movement — Maritime Exploration — Portugal — Medieval"],
        "frameworks": ["world-systems", "political-history"],
        "era": "Medieval",
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "The Portuguese Age of Discovery opened the world's first global sea trading network — a 130-year programme of systematic exploration that permanently shifted world trade from land to sea and laid the foundation for European global empire.",
            "significanceCategory": "world-changing"
        },
    },
    "microsoft": {
        "summary": (
            "Microsoft Corporation is an American multinational technology company founded "
            "in 1975 by Bill Gates and Paul Allen in Albuquerque, New Mexico, that became "
            "the world's largest software company and, in 2024, the world's most valuable "
            "publicly traded company. Its operating system MS-DOS (1981) and its successor "
            "Windows (1985–present) placed a personal computer on virtually every office "
            "desk and home in the developed world — the most impactful consumer software "
            "platform in history.\n\n"
            "Microsoft's key strategic move was the non-exclusive licensing of MS-DOS to "
            "IBM in 1981, allowing Microsoft to sell the same operating system to all PC "
            "manufacturers — a decision that made it the de facto standard while IBM's "
            "hardware was commoditised. Windows 95 (released to midnight queues worldwide) "
            "launched the GUI era for mass consumers. Microsoft Office — Word, Excel, "
            "PowerPoint — became the universal business productivity suite, generating "
            "billions in annual licensing revenue. Internet Explorer's bundling with Windows "
            "in 1995 triggered the antitrust case US v. Microsoft (1998–2001).\n\n"
            "Under CEO Satya Nadella (2014–present), Microsoft shifted to cloud computing "
            "(Azure, now the world's second-largest cloud platform), open-source contributions, "
            "and acquired LinkedIn (2016), GitHub (2018), and Activision Blizzard (2023). "
            "Its 2023 investment in OpenAI placed it at the centre of the AI revolution."
        ),
        "causes": [
            {"title": "IBM's 1980 decision to outsource the operating system for its Personal Computer gave Microsoft the contract that made it the de facto global OS standard", "type": "Institution", "year": "1980, USA"},
            {"title": "Bill Gates and Paul Allen's insight that software, not hardware, would be the profitable layer of personal computing drove Microsoft's strategy from its founding", "type": "Person", "year": "1975, USA"},
        ],
        "effects": [
            {"title": "MS-DOS and Windows placed a Microsoft operating system on over 90% of the world's personal computers, making it the dominant computing infrastructure of the late 20th century", "type": "Idea", "year": "1981–2000, Global"},
            {"title": "Microsoft Office became the world's universal business productivity suite, making Word, Excel, and PowerPoint the standard tools of knowledge work globally", "type": "Institution", "year": "1989–present, Global"},
            {"title": "US v. Microsoft antitrust case (1998–2001) was a landmark in regulating technology monopolies, shaping how competition law applies to digital platform dominance", "type": "EventWindow", "year": "1998–2001, USA"},
            {"title": "Microsoft's $13 billion investment in OpenAI (2019–2023) positioned it as the leading enterprise AI platform, integrating generative AI into Office, Windows, and Azure", "type": "EventWindow", "year": "2019–present, Global"},
        ],
        "relationships": [
            {"targetSlug": "bill-gates", "verb": "INFLUENCES", "note": "Bill Gates co-founded Microsoft and led it to become the world's most valuable software company"},
            {"targetSlug": "ibm", "verb": "INFLUENCES", "note": "IBM's 1981 PC contract gave Microsoft the OS monopoly that defined its first 30 years"},
            {"targetSlug": "openai", "verb": "INFLUENCES", "note": "Microsoft's $13 billion investment in OpenAI placed it at the centre of the 2023 AI revolution"},
            {"targetSlug": "personal-computer", "verb": "INFLUENCES", "note": "Microsoft's operating systems and productivity software defined the personal computing era"},
        ],
        "places": ["Redmond, Washington, USA", "Global"],
        "subjects": ["Microsoft", "Technology", "Software", "Bill Gates", "Windows", "Cloud Computing", "AI"],
        "subjectHeadings": ["Institution — Technology Company — USA — Contemporary"],
        "frameworks": ["economic-history", "technological-history"],
        "era": "Contemporary",
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Microsoft placed computing on every desk on Earth, made software the world's most valuable asset class, and is now central to the AI revolution — the most impactful software company in history by reach and economic value.",
            "significanceCategory": "world-changing"
        },
    },
    "cern": {
        "summary": (
            "CERN (Conseil Européen pour la Recherche Nucléaire) is the European Organization "
            "for Nuclear Research, established in 1954 near Geneva on the Swiss-French border "
            "as post-war Europe's most ambitious scientific collaboration — and the home of "
            "the world's largest machine, the Large Hadron Collider (LHC), a 27 km circular "
            "particle accelerator used to recreate conditions microseconds after the Big Bang.\n\n"
            "CERN's practical impact extends far beyond particle physics. Tim Berners-Lee "
            "invented the World Wide Web at CERN in 1989 — proposing it as a way to share "
            "data between particle physics experiments — in what became the most transformative "
            "incidental invention in the history of science. The LHC's 2012 discovery of the "
            "Higgs boson — the final missing particle in the Standard Model, first theorised "
            "in 1964 — was the most celebrated experimental physics result of the 21st century.\n\n"
            "CERN operates as a model of international scientific governance: 23 member states "
            "contribute to its €1.3 billion annual budget, and thousands of physicists from "
            "over 100 countries work on its experiments. It pioneered the computing "
            "infrastructure — the grid — that allowed particle data to be processed globally, "
            "a precursor to cloud computing. Its antimatter research and precision "
            "measurements continue to probe the foundations of physics."
        ),
        "causes": [
            {"title": "Post-WWII European scientific leaders argued that no single European nation could afford the large accelerators needed for nuclear physics research — requiring a collective institution", "type": "EventWindow", "year": "1949–1954, Europe"},
            {"title": "Cold War nuclear competition created political willingness to fund particle accelerators as symbols of scientific prestige alongside their research value", "type": "EventWindow", "year": "1950–1960, Europe"},
        ],
        "effects": [
            {"title": "Tim Berners-Lee invented the World Wide Web at CERN in 1989, creating the internet's most used application layer and transforming global communications", "type": "Person", "year": "1989, CERN"},
            {"title": "Discovery of the Higgs boson (2012) completed the Standard Model of particle physics — the most rigorously tested theory in science — after a 50-year search", "type": "EventWindow", "year": "2012, CERN"},
            {"title": "CERN's computing grid became a model for distributed scientific computing and influenced the development of cloud computing infrastructure", "type": "Idea", "year": "c. 2000–present, Global"},
            {"title": "CERN's success as 23-nation scientific collaboration demonstrated that large-scale peaceful international scientific cooperation could work even across Cold War divisions", "type": "Institution", "year": "1954–present, Europe"},
        ],
        "relationships": [
            {"targetSlug": "tim-berners-lee", "verb": "INFLUENCES", "note": "Tim Berners-Lee invented the World Wide Web at CERN in 1989 to share particle physics data"},
            {"targetSlug": "higgs-boson", "verb": "CAUSES", "note": "CERN's Large Hadron Collider discovered the Higgs boson in 2012, completing the Standard Model"},
            {"targetSlug": "large-hadron-collider", "verb": "INFLUENCES", "note": "The LHC is CERN's flagship instrument — a 27 km accelerator operating at the energy frontier"},
            {"targetSlug": "world-wide-web", "verb": "CAUSES", "note": "The World Wide Web was invented at CERN, making it the birthplace of the internet's defining application"},
        ],
        "places": ["Geneva, Switzerland", "France", "Europe"],
        "subjects": ["CERN", "Particle Physics", "Large Hadron Collider", "World Wide Web", "Science", "Geneva", "Higgs Boson"],
        "subjectHeadings": ["Institution — Research Organization — Europe — Contemporary"],
        "frameworks": ["intellectual-history", "technological-history"],
        "era": "Contemporary",
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "CERN is where the World Wide Web was invented and where the Higgs boson was found — a 23-nation scientific collaboration that has produced two of the most consequential discoveries of the 20th and 21st centuries.",
            "significanceCategory": "world-changing"
        },
    },
}


# ── helpers ──────────────────────────────────────────────────────────────────

def apply_enrichment(slug: str, enrichment: dict, fpath: str) -> bool:
    abs_path = os.path.join(
        "/home/manasa151/annals-of-the-world",
        fpath
    )
    if not os.path.exists(abs_path):
        print(f"  SKIP {slug} — file not found at {abs_path}")
        return False
    with open(abs_path) as fh:
        doc = json.load(fh)
    entities = doc.get("entities", [])
    if not entities:
        print(f"  SKIP {slug} — empty entities array")
        return False
    entity = entities[0]
    old_summary = entity.get("summary") or ""
    edit_log = entity.get("_editLog") or []
    for field, new_val in enrichment.items():
        old_val = entity.get(field)
        if old_val != new_val:
            edit_log.append({"field": field, "old": old_val, "new": new_val,
                              "editor": EDITOR_ID, "ts": NOW})
        entity[field] = new_val
    entity["_unsyncedEdits"] = True
    entity["_editLog"] = edit_log
    entity["status"] = "enriched"
    doc["entities"] = [entity]
    with open(abs_path, "w") as fh:
        json.dump(doc, fh, indent=2, ensure_ascii=False)
    print(f"  OK  {slug:42}  {len(old_summary)}c → {len(entity.get('summary','') or '')}c")
    return True


def main():
    print(f"Enriching {len(ENRICHMENTS)} entities (Batch 8 — Ideas/Movements/Institutions)...")
    ok = fail = 0
    for slug, enrichment in ENRICHMENTS.items():
        fpath = FILE_MAP[slug]
        if apply_enrichment(slug, enrichment, fpath):
            ok += 1
        else:
            fail += 1
    print(f"\nDone: {ok} enriched, {fail} skipped.")


if __name__ == "__main__":
    main()
