#!/usr/bin/env python3
"""
Batch 6: 8 polities from 430-Class-430
San Marino, Mali, Bhutan, Grenada, Guinea-Bissau,
Marshall Islands, Guyana, Ethiopia.
subjectHeadings always written as list (Appwrite schema requirement).
"""
import json, os, glob, unicodedata
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/430-Class-430"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()

ENRICHMENTS = {
    "san-marino": {
        "summary": (
            "San Marino is a landlocked microstate enclaved within central Italy, "
            "widely regarded as the world's oldest surviving republic, with a founding "
            "tradition tracing to 301 CE when the Christian stonemason Marinus of Rab "
            "fled Roman persecution and established a monastic community on Monte Titano. "
            "It covers just 61 km² and has a population of around 34,000, yet has maintained "
            "unbroken self-governance through the medieval period, the age of Italian "
            "city-states, Napoleonic invasion, and two world wars.\n\n"
            "The republic's constitution — or at least its institutional core — dates to "
            "the Statutes of 1600, making it among the oldest surviving written constitutions. "
            "The government is headed by two Captains Regent elected every six months from "
            "the Grand and General Council, a dual-executive arrangement designed to prevent "
            "tyranny that has operated without interruption for over 700 years. San Marino "
            "famously declined to accept Napoleon's offer of territorial expansion in 1797, "
            "and it sheltered thousands of refugees — including Jews — during World War II.\n\n"
            "Recognised by the Congress of Vienna (1815) and later admitted to the United "
            "Nations in 1992, San Marino stands as proof that a tiny community can maintain "
            "sovereignty through diplomacy, neutrality, and institutional resilience across "
            "seventeen centuries of turbulent Italian history."
        ),
        "causes": [
            {"title": "Roman persecution of Christians in the 3rd century drove Marinus and his community to seek refuge on the defensible heights of Monte Titano", "type": "EventWindow", "year": "c. 257–305 CE, Italy"},
            {"title": "Monte Titano's steep terrain provided natural fortification, allowing the community to resist assimilation by surrounding powers", "type": "Place", "year": "301 CE onwards, San Marino"},
            {"title": "Diplomatic skill — particularly San Marino's offer of asylum — repeatedly earned goodwill from larger powers that might otherwise have absorbed it", "type": "Idea", "year": "c. 1200–1800, Europe"},
        ],
        "effects": [
            {"title": "Statutes of 1600 became one of the world's oldest surviving written constitutional documents, influencing ideas of republican governance", "type": "Text", "year": "1600, San Marino"},
            {"title": "Dual Captain-Regent system — two co-equal executives with 6-month terms — became a model studied by early modern republican theorists", "type": "Institution", "year": "c. 1243–present, San Marino"},
            {"title": "San Marino's survival inspired Italian republicans, including Garibaldi who sheltered there after the fall of the Roman Republic in 1849", "type": "EventWindow", "year": "1849, San Marino"},
            {"title": "UN membership in 1992 confirmed that sovereign statehood is not size-dependent, reinforcing the international legal principle of self-determination", "type": "Idea", "year": "1992, New York"},
        ],
        "relationships": [
            {"targetSlug": "roman-empire", "verb": "INFLUENCES", "note": "San Marino emerged as a refuge from Roman imperial religious persecution"},
            {"targetSlug": "italian-unification", "verb": "INFLUENCES", "note": "San Marino remained independent throughout the Risorgimento and served as a refuge for Garibaldi"},
            {"targetSlug": "napoleon-i", "verb": "INFLUENCES", "note": "Napoleon offered to expand San Marino's territory in 1797; San Marino declined, preserving its independence"},
            {"targetSlug": "pope-innocent-iv", "verb": "INFLUENCES", "note": "Papal confirmation of San Marino's independence in 1291 was crucial to its long-term survival"},
        ],
        "places": ["Monte Titano, San Marino"],
        "subjects": ["San Marino", "Republic", "Microstate", "Italy", "Medieval Europe", "Constitutional History", "Oldest Republic"],
        "subjectHeadings": ["Polity — Republic — San Marino — Classical"],
        "frameworks": ["constitutional-history", "political-history"],
        "era": "Classical",
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "San Marino is the world's oldest surviving republic, a living demonstration that a tiny community can maintain sovereignty across 17 centuries through institutional resilience, diplomatic neutrality, and fortuitous geography.",
            "significanceCategory": "world-changing"
        },
    },
    "mali": {
        "summary": (
            "Mali (officially the Republic of Mali) is a landlocked West African nation and "
            "the heir to three of the medieval world's greatest empires — the Ghana Empire "
            "(c. 700–1200), the Mali Empire (1235–1600), and the Songhai Empire (1375–1591) "
            "— which together controlled trans-Saharan gold-salt trade routes and produced "
            "the legendary wealth of Mansa Musa, the richest individual in recorded history.\n\n"
            "The Mali Empire at its 14th-century peak stretched across 1.2 million km² from "
            "the Atlantic coast to the Niger bend, encompassing the great intellectual centres "
            "of Timbuktu and Djenné. Mansa Musa's 1324 hajj to Mecca — during which his "
            "entourage distributed so much gold in Cairo that it depressed Egyptian gold prices "
            "for a decade — introduced sub-Saharan Africa's wealth to the Mediterranean world. "
            "The Sankore mosque and university at Timbuktu housed over 25,000 students and a "
            "library of some 700,000 manuscripts.\n\n"
            "Modern Mali gained independence from France in 1960. Despite abundant mineral "
            "wealth, it has struggled with repeated coups, Tuareg insurgencies, and since 2012 "
            "a jihadist insurgency that has displaced millions and made the Sahel one of the "
            "world's most active conflict zones. The preservation of Timbuktu's manuscripts — "
            "many secretly evacuated during the 2012 Islamist occupation — remains one of the "
            "world's great ongoing heritage rescue efforts."
        ),
        "causes": [
            {"title": "Trans-Saharan gold-salt trade routes through the western Sudan created the economic foundation for the succession of great empires centered on modern Mali", "type": "EventWindow", "year": "c. 700–1600, West Africa"},
            {"title": "Niger River system provided agricultural surplus and communications infrastructure for large-scale state formation", "type": "Place", "year": "c. 1200 BCE–present, West Africa"},
            {"title": "French colonial penetration of West Africa from the 1880s dismantled the last indigenous polities and imposed boundaries cutting across ethnic and trading networks", "type": "EventWindow", "year": "1880–1960, West Africa"},
        ],
        "effects": [
            {"title": "Mali Empire under Mansa Musa became the wealthiest polity in the medieval world, introducing West African gold wealth to the wider Islamic world and Europe", "type": "Institution", "year": "c. 1312–1337, West Africa"},
            {"title": "Timbuktu became one of the world's greatest medieval centres of Islamic scholarship, housing up to 700,000 manuscripts", "type": "Institution", "year": "c. 1300–1600, West Africa"},
            {"title": "Independence from France in 1960 launched the modern era; repeated military coups since 1968 have made Mali a case study in postcolonial institutional fragility", "type": "EventWindow", "year": "1960–present, Mali"},
            {"title": "Sahel jihadist insurgency (2012–present) has spread from northern Mali across six countries, becoming one of the world's most severe humanitarian crises", "type": "EventWindow", "year": "2012–present, West Africa"},
        ],
        "relationships": [
            {"targetSlug": "mansa-musa", "verb": "INFLUENCES", "note": "Mansa Musa was the Mali Empire's greatest ruler, whose hajj broadcast West African wealth to the world"},
            {"targetSlug": "timbuktu", "verb": "OCCURS_IN", "note": "Timbuktu — the great intellectual centre of the Mali and Songhai empires — lies in modern Mali"},
            {"targetSlug": "trans-saharan-trade", "verb": "INFLUENCES", "note": "Trans-Saharan gold-salt trade was the economic foundation of all three great Malian empires"},
            {"targetSlug": "songhai-empire", "verb": "INFLUENCES", "note": "The Songhai Empire succeeded the Mali Empire and controlled the same Niger bend territory"},
            {"targetSlug": "french-west-africa", "verb": "INFLUENCES", "note": "French colonial rule 1880–1960 reshaped Mali's borders and economy, generating legacies that persist today"},
        ],
        "places": ["Bamako, Mali", "Timbuktu, Mali", "Niger River, West Africa"],
        "subjects": ["Mali", "West Africa", "Mali Empire", "Mansa Musa", "Timbuktu", "Trans-Saharan Trade", "Sahel", "Independence"],
        "subjectHeadings": ["Polity — State — Mali — Contemporary"],
        "frameworks": ["world-systems", "postcolonial-history"],
        "era": "Contemporary",
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Mali is the heir to the medieval world's wealthiest empire and one of the greatest centres of Islamic scholarship; its ongoing fragility is a central case study in postcolonial state failure and Sahel instability.",
            "significanceCategory": "continental"
        },
    },
    "bhutan": {
        "summary": (
            "Bhutan (officially the Kingdom of Bhutan) is a small Himalayan monarchy "
            "sandwiched between India and China that has never been colonised, maintaining "
            "its sovereignty and distinctive Vajrayana Buddhist culture across centuries of "
            "geopolitical turbulence. It is also the birthplace of the concept of Gross "
            "National Happiness (GNH) — a development philosophy that explicitly rejects "
            "GDP as the measure of a nation's wellbeing.\n\n"
            "Bhutan's political unification was achieved by the Zhabdrung Ngawang Namgyal, "
            "a Tibetan Buddhist lama who fled to Bhutan in 1616 and consolidated its "
            "monasteries, legal system, and military defences into a theocratic state. "
            "The Wangchuck dynasty assumed power in 1907 and navigated British colonial "
            "pressures while preserving sovereignty. King Jigme Singye Wangchuck popularised "
            "GNH in the 1970s as an alternative development metric measuring spiritual "
            "wellbeing, cultural preservation, environmental sustainability, and good "
            "governance — a framework that influenced the UN's Human Development Index "
            "approach and sustainable development goals.\n\n"
            "Bhutan opened to television and internet only in 1999, and maintained a strict "
            "tourist policy limiting visitors to protect cultural integrity. It became a "
            "constitutional monarchy in 2008 — one of the world's most recent democratic "
            "transitions — and is noted for being the world's only carbon-negative country."
        ),
        "causes": [
            {"title": "Zhabdrung Ngawang Namgyal's flight from Tibet in 1616 and his subsequent unification of Bhutan under Vajrayana Buddhism created the state's theocratic-political identity", "type": "Person", "year": "1616–1651, Bhutan"},
            {"title": "Himalayan geography isolated Bhutan from colonial penetration that absorbed its neighbours Nepal and Sikkim", "type": "Place", "year": "c. 1800–1949, Bhutan"},
            {"title": "Treaty of Sinchula (1865) with Britain after the Duar War defined Bhutan's relationship with colonial India, preserving internal autonomy at the cost of some border territory", "type": "EventWindow", "year": "1865, Bhutan"},
        ],
        "effects": [
            {"title": "Gross National Happiness (GNH) framework introduced by Bhutan as alternative to GDP became globally influential in sustainable development discourse", "type": "Idea", "year": "1972–present, Global"},
            {"title": "Bhutan's policy of controlled tourism and cultural preservation became a model for small nations protecting heritage from mass tourism", "type": "Idea", "year": "1974–present, Bhutan"},
            {"title": "Constitutional monarchy transition (2008) completed Bhutan's evolution from absolute theocracy to modern democratic governance", "type": "EventWindow", "year": "2008, Bhutan"},
            {"title": "Carbon-negative status through 72% forest cover and hydroelectric export makes Bhutan a reference point in climate policy discussions", "type": "Idea", "year": "c. 1990–present, Global"},
        ],
        "relationships": [
            {"targetSlug": "tibet", "verb": "INFLUENCES", "note": "Bhutan's founding culture came from Tibetan Buddhism; the Zhabdrung fled Tibet to establish Bhutan"},
            {"targetSlug": "india", "verb": "INFLUENCES", "note": "Bhutan's foreign policy is managed largely through India under treaties from 1949 and 2007"},
            {"targetSlug": "united-nations", "verb": "INFLUENCES", "note": "Bhutan's GNH framework influenced the UN's approach to the Human Development Index and SDGs"},
            {"targetSlug": "gross-national-happiness", "verb": "CAUSES", "note": "Bhutan originated and systematised the GNH development framework"},
        ],
        "places": ["Thimphu, Bhutan", "Himalayas, Asia"],
        "subjects": ["Bhutan", "Himalaya", "Buddhism", "Gross National Happiness", "Monarchy", "South Asia", "Sustainable Development"],
        "subjectHeadings": ["Polity — Monarchy — Bhutan — Contemporary"],
        "frameworks": ["political-history", "environmental-history"],
        "era": "Contemporary",
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Bhutan is the only Himalayan nation never colonised and the inventor of Gross National Happiness — a development philosophy now influencing global sustainability policy — making it a uniquely influential microstate for its size.",
            "significanceCategory": "continental"
        },
    },
    "grenada": {
        "summary": (
            "Grenada is a Caribbean island nation known as the 'Spice Isle' for its production "
            "of nutmeg and mace, and infamous as the site of the 1983 US military intervention "
            "— Operation Urgent Fury — the first significant American military action since "
            "Vietnam, which triggered an international crisis and set precedents for Cold War "
            "unilateralism.\n\n"
            "Colonised by France in 1649 and ceded to Britain after the Seven Years' War (1763), "
            "Grenada gained independence in 1974 under the autocratic Eric Gairy. In 1979, "
            "Maurice Bishop's Marxist New Jewel Movement (NJM) seized power in a bloodless coup "
            "and aligned Grenada with Cuba and the Soviet Union. In October 1983, a faction "
            "within the NJM murdered Bishop and seized power; the Reagan administration used "
            "the coup as justification to invade with 7,000 troops, removing the regime within "
            "days. The intervention was condemned by the UN General Assembly (108–9) and by "
            "Britain, a NATO ally — yet it succeeded in restoring elected government and "
            "demonstrated US willingness to use military force in its Caribbean 'backyard.'\n\n"
            "Today Grenada is a stable parliamentary democracy and major nutmeg exporter. "
            "The 1983 intervention continues to generate debate about the legality of "
            "humanitarian intervention and the limits of sovereignty."
        ),
        "causes": [
            {"title": "Cold War competition in the Caribbean created the geopolitical tension that made Grenada's Cuban alignment politically intolerable to Washington", "type": "EventWindow", "year": "1979–1983, Caribbean"},
            {"title": "Maurice Bishop's 1979 NJM revolution aligned Grenada with Cuba and the Soviet Union, triggering US concern over a communist Caribbean chain", "type": "EventWindow", "year": "1979, Grenada"},
            {"title": "Internal NJM coup murdering Maurice Bishop on 19 October 1983 provided the immediate pretext for US intervention", "type": "EventWindow", "year": "1983, Grenada"},
        ],
        "effects": [
            {"title": "Operation Urgent Fury (1983) was the first major US combat deployment since Vietnam, restoring American military confidence after the 'Vietnam syndrome'", "type": "EventWindow", "year": "1983, Grenada"},
            {"title": "UN General Assembly condemnation (108–9) highlighted the tension between state sovereignty and great-power intervention in international law", "type": "EventWindow", "year": "1983, New York"},
            {"title": "Grenada precedent contributed to the Reagan Doctrine framework justifying US rollback of Soviet-aligned governments in the developing world", "type": "Idea", "year": "1983–1989, USA"},
        ],
        "relationships": [
            {"targetSlug": "ronald-reagan", "verb": "INFLUENCES", "note": "The Reagan administration ordered Operation Urgent Fury in October 1983"},
            {"targetSlug": "cold-war", "verb": "INFLUENCES", "note": "Grenada's crisis was a direct product of Cold War Caribbean geopolitics"},
            {"targetSlug": "cuba", "verb": "INFLUENCES", "note": "Cuban construction workers and military advisers on Grenada were cited in US justification for the invasion"},
            {"targetSlug": "united-nations", "verb": "INFLUENCES", "note": "The UNGA condemned the US invasion 108-9, a major diplomatic embarrassment for Washington"},
        ],
        "places": ["St. George's, Grenada", "Caribbean Sea"],
        "subjects": ["Grenada", "Caribbean", "Cold War", "US Military Intervention", "Operation Urgent Fury", "Latin America", "Sovereignty"],
        "subjectHeadings": ["Polity — State — Grenada — Contemporary"],
        "frameworks": ["political-history", "cold-war-history"],
        "era": "Contemporary",
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Grenada's 1983 US invasion was the defining Cold War Caribbean intervention — the first major American military action since Vietnam and a still-contested precedent for humanitarian intervention vs. sovereignty.",
            "significanceCategory": "continental"
        },
    },
    "guinea-bissau": {
        "summary": (
            "Guinea-Bissau is a small West African state and a former Portuguese colony whose "
            "independence struggle, led by Amílcar Cabral and the PAIGC liberation movement, "
            "became one of the most theoretically sophisticated anti-colonial movements of the "
            "20th century — inspiring liberation movements across three continents.\n\n"
            "Amílcar Cabral (1924–1973) founded the African Party for the Independence of "
            "Guinea and Cape Verde (PAIGC) in 1956 and launched an armed insurgency in 1963 "
            "that by 1968 had liberated two-thirds of the territory from Portuguese control. "
            "Cabral's writings — particularly 'Return to the Source' and 'National Liberation "
            "and Culture' — are seminal texts in anti-colonial theory, arguing that culture "
            "is the most powerful weapon of resistance. He was assassinated in January 1973, "
            "months before independence. Guinea-Bissau declared independence in September 1973 "
            "and was recognised internationally after Portugal's Carnation Revolution (1974) "
            "overthrew the Salazar regime.\n\n"
            "Since independence, Guinea-Bissau has endured nine coups in 50 years and is "
            "classified as a fragile state, heavily dependent on cashew nut exports and "
            "entangled in West African drug trafficking networks. It stands as a painful "
            "reminder that political independence does not automatically produce stable "
            "post-colonial institutions."
        ),
        "causes": [
            {"title": "Portuguese Estado Novo regime's refusal to grant autonomy to its African colonies forced liberation movements to turn to armed struggle in the 1960s", "type": "EventWindow", "year": "1956–1963, Guinea-Bissau"},
            {"title": "Amílcar Cabral's intellectual and organisational genius in building a mass liberation movement across ethnic lines was the decisive factor in PAIGC's success", "type": "Person", "year": "1956–1973, Guinea-Bissau"},
            {"title": "Cold War support from the USSR, China, and Cuba gave PAIGC weapons, training, and diplomatic recognition", "type": "EventWindow", "year": "1963–1974, Guinea-Bissau"},
        ],
        "effects": [
            {"title": "Portuguese Carnation Revolution (April 1974) was partly caused by the cost and demoralisation of Guinea-Bissau's protracted liberation war", "type": "EventWindow", "year": "1974, Portugal"},
            {"title": "Cabral's anti-colonial writings became foundational texts in postcolonial studies, influencing Frantz Fanon's readers across Africa, Asia, and Latin America", "type": "Text", "year": "1963–present, Global"},
            {"title": "Guinea-Bissau's post-independence instability — nine coups in 50 years — became a reference case for the structural fragility of small postcolonial states", "type": "EventWindow", "year": "1974–present, West Africa"},
        ],
        "relationships": [
            {"targetSlug": "amilcar-cabral", "verb": "INFLUENCES", "note": "Amílcar Cabral founded PAIGC and led the liberation struggle that created Guinea-Bissau"},
            {"targetSlug": "portugal", "verb": "INFLUENCES", "note": "Portuguese colonial rule shaped Guinea-Bissau's economy, borders, and the liberation war that ended it"},
            {"targetSlug": "carnation-revolution", "verb": "CAUSES", "note": "Guinea-Bissau's unwinnable liberation war was a major cause of the Portuguese Carnation Revolution"},
            {"targetSlug": "cape-verde", "verb": "INFLUENCES", "note": "Guinea-Bissau and Cape Verde were linked under the PAIGC and briefly considered federation after independence"},
        ],
        "places": ["Bissau, Guinea-Bissau", "West Africa"],
        "subjects": ["Guinea-Bissau", "West Africa", "Decolonization", "Amílcar Cabral", "PAIGC", "Anti-Colonialism", "Portuguese Empire"],
        "subjectHeadings": ["Polity — State — Guinea-Bissau — Contemporary"],
        "frameworks": ["postcolonial-history", "political-history"],
        "era": "Contemporary",
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Guinea-Bissau's liberation struggle, led by the theorist-revolutionary Amílcar Cabral, was one of the most intellectually significant anti-colonial movements of the 20th century and its war helped topple the Portuguese dictatorship.",
            "significanceCategory": "continental"
        },
    },
    "marshall-islands": {
        "summary": (
            "The Marshall Islands is a Pacific microstate of 29 atolls and 5 isolated islands "
            "that carries a history disproportionate to its size — as the site of 67 US nuclear "
            "weapons tests between 1946 and 1958, including the largest US thermonuclear "
            "detonation ever (Castle Bravo, 15 megatons, 1954), it is among the most "
            "heavily irradiated places on Earth.\n\n"
            "Under Japanese mandate after World War I and the scene of intense US-Japanese "
            "combat during World War II (the Battle of Kwajalein, 1944), the Marshall Islands "
            "became a US Trust Territory in 1947. The Bikini and Enewetak atolls were "
            "designated as the Pacific Proving Ground and their inhabitants forcibly relocated. "
            "Castle Bravo (1 March 1954) unexpectedly spread radioactive fallout over 7,000 "
            "square miles, contaminating 23 Japanese fishermen aboard the Lucky Dragon and "
            "triggering international outrage that directly accelerated the Partial Nuclear "
            "Test Ban Treaty (1963).\n\n"
            "The Marshall Islands achieved Compact of Free Association with the United States "
            "in 1986 and full UN membership in 1991. It remains on the front line of climate "
            "change: at an average elevation of two metres above sea level, it faces existential "
            "threat from rising seas, making it one of the world's most vocal advocates for "
            "aggressive emissions reduction."
        ),
        "causes": [
            {"title": "US strategic monopoly on the Pacific after World War II made the Marshall Islands the logical site for nuclear testing far from populated areas", "type": "EventWindow", "year": "1945–1946, Pacific"},
            {"title": "Cold War nuclear competition with the Soviet Union drove the US to test progressively larger thermonuclear devices at Bikini and Enewetak", "type": "EventWindow", "year": "1946–1958, Pacific"},
        ],
        "effects": [
            {"title": "Castle Bravo (1954) contaminated 7,000 sq miles and the Lucky Dragon crew, generating global anti-nuclear protests and accelerating the 1963 Test Ban Treaty", "type": "EventWindow", "year": "1954, Pacific"},
            {"title": "Bikini Atoll declared uninhabitable; its residents never permanently returned — becoming the first nuclear refugees in history", "type": "Place", "year": "1946–present, Bikini Atoll"},
            {"title": "Marshall Islands' climate advocacy has given it outsized influence in UNFCCC negotiations relative to its tiny size and population", "type": "EventWindow", "year": "1990–present, Global"},
            {"title": "Partial Nuclear Test Ban Treaty (1963) was partly driven by the Castle Bravo fallout controversy to which Marshall Islands was central", "type": "Text", "year": "1963, Moscow"},
        ],
        "relationships": [
            {"targetSlug": "bikini-atoll", "verb": "OCCURS_IN", "note": "Bikini Atoll in the Marshall Islands was the main site of US nuclear tests 1946–1958"},
            {"targetSlug": "nuclear-weapons", "verb": "INFLUENCES", "note": "67 US nuclear tests transformed the Marshall Islands' history and ecology"},
            {"targetSlug": "partial-nuclear-test-ban-treaty", "verb": "CAUSES", "note": "Castle Bravo fallout was a catalyst for the 1963 Test Ban Treaty"},
            {"targetSlug": "climate-change", "verb": "INFLUENCES", "note": "Sea-level rise threatens to submerge the Marshall Islands, making it a frontline climate advocacy nation"},
        ],
        "places": ["Majuro, Marshall Islands", "Bikini Atoll, Pacific", "Pacific Ocean"],
        "subjects": ["Marshall Islands", "Nuclear Testing", "Bikini Atoll", "Pacific", "Cold War", "Castle Bravo", "Climate Change"],
        "subjectHeadings": ["Polity — State — Marshall Islands — Contemporary"],
        "frameworks": ["cold-war-history", "environmental-history"],
        "era": "Contemporary",
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "The Marshall Islands bore the full force of 67 US nuclear tests — including the world's largest — and now faces existential erasure from rising seas: a nation defined by two civilisational catastrophes it did not cause.",
            "significanceCategory": "continental"
        },
    },
    "guyana": {
        "summary": (
            "Guyana is the only English-speaking country in South America, a former British "
            "colony that gained independence in 1966 and has since navigated sharp ethnic "
            "divisions between its Indo-Guyanese and Afro-Guyanese communities, legacies "
            "of sugar plantation slavery and indentured labour. In 2015, the discovery of "
            "one of the world's largest offshore oil deposits transformed its geopolitical "
            "importance almost overnight.\n\n"
            "The colony of British Guiana was built on sugarcane plantations that imported "
            "enslaved Africans until abolition (1834), then recruited over 230,000 indentured "
            "labourers from India between 1838 and 1917. This demographic split — roughly "
            "40% Indo-Guyanese, 30% Afro-Guyanese — created persistent political polarisation "
            "that shaped independence politics. Cheddi Jagan's PPP (Indo-Guyanese base) and "
            "Forbes Burnham's PNC (Afro-Guyanese base) competed through electoral manipulation, "
            "nationalisation, and authoritarian rule through the 1970s–1980s.\n\n"
            "The 2015 offshore oil discovery by ExxonMobil — ultimately over 10 billion barrels "
            "in the Stabroek Block — gave Guyana the world's highest GDP growth rate in "
            "2022 (62%) and is reshaping its economy and regional influence. It now faces the "
            "classic 'resource curse' challenge: converting windfall petroleum revenues into "
            "durable human development."
        ),
        "causes": [
            {"title": "Sugar plantation economy built on enslaved African labour created Guyana's foundational demographic and social structure", "type": "EventWindow", "year": "c. 1620–1834, Guyana"},
            {"title": "Post-emancipation labour shortage led to mass Indian indenture 1838–1917, creating the Indo-Guyanese majority community", "type": "EventWindow", "year": "1838–1917, Guyana"},
            {"title": "ExxonMobil's 2015 Liza oil discovery in the Stabroek offshore block opened one of the world's largest new oil provinces", "type": "EventWindow", "year": "2015, Guyana"},
        ],
        "effects": [
            {"title": "Ethnic political polarisation between Indo- and Afro-Guyanese communities produced decades of electoral manipulation and contested governance", "type": "EventWindow", "year": "1953–present, Guyana"},
            {"title": "Offshore oil production (from 2019) gave Guyana 62% GDP growth in 2022 — the highest in the world — transforming its regional standing", "type": "EventWindow", "year": "2019–present, Guyana"},
            {"title": "Venezuela's territorial claim to 70% of Guyana (Essequibo region) intensified after oil discovery, creating a potential major territorial dispute", "type": "EventWindow", "year": "2023–present, South America"},
        ],
        "relationships": [
            {"targetSlug": "british-empire", "verb": "INFLUENCES", "note": "British colonial rule shaped Guyana's plantation economy, indentured labour system, and post-independence borders"},
            {"targetSlug": "india", "verb": "INFLUENCES", "note": "Over 230,000 Indian indentured labourers came to Guyana 1838–1917, creating its largest ethnic community"},
            {"targetSlug": "venezuela", "verb": "INFLUENCES", "note": "Venezuela claims the Essequibo region (70% of Guyana), a dispute intensified by oil discovery"},
            {"targetSlug": "exxonmobil", "verb": "INFLUENCES", "note": "ExxonMobil's Stabroek Block discovery transformed Guyana into one of the world's fastest-growing oil producers"},
        ],
        "places": ["Georgetown, Guyana", "South America", "Atlantic Ocean"],
        "subjects": ["Guyana", "South America", "Caribbean", "Oil Discovery", "Decolonization", "Indentured Labour", "Venezuela Dispute"],
        "subjectHeadings": ["Polity — State — Guyana — Contemporary"],
        "frameworks": ["postcolonial-history", "economic-history"],
        "era": "Contemporary",
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Guyana's trajectory — from plantation slavery to indentured labour to postcolonial polarisation to sudden oil-wealth — encapsulates the full arc of Atlantic colonial history, and its Essequibo dispute may become South America's defining territorial conflict.",
            "significanceCategory": "continental"
        },
    },
    "ethiopia": {
        "summary": (
            "Ethiopia is one of the world's oldest nations, the only African country never "
            "formally colonised (defeating Italy at the Battle of Adwa in 1896), and the seat "
            "of an imperial dynasty — the Solomonic line — that claimed direct descent from "
            "King Solomon and the Queen of Sheba and ruled with brief interruptions from "
            "1270 until 1974.\n\n"
            "Home to one of the earliest hominid fossils (Lucy/Australopithecus afarensis, "
            "3.2 million years old), the Aksumite Empire (c. 100–940 CE) — one of antiquity's "
            "four great powers alongside Rome, Persia, and China — and the first African kingdom "
            "to adopt Christianity (c. 330 CE), Ethiopia is a civilisation of extraordinary "
            "antiquity. Emperor Haile Selassie's impassioned League of Nations speech (1936) "
            "following Italy's gas-attack invasion became a defining moment in anti-colonial "
            "history and made Ethiopia a symbol of African resistance to imperialism.\n\n"
            "The 1974 Derg revolution overthrew Selassie, leading to Mengistu's Marxist Red "
            "Terror that killed hundreds of thousands. The current federal structure under the "
            "EPRDF (now Prosperity Party) is under severe stress from the Tigray War "
            "(2020–2022), which caused what the UN called the world's worst humanitarian "
            "crisis. With 126 million people, Ethiopia is Africa's second most populous "
            "nation and the horn of Africa's dominant power."
        ),
        "causes": [
            {"title": "Aksumite Empire's Red Sea commercial power gave Ethiopia early access to Christianity and trade networks connecting India, Arabia, and the Mediterranean", "type": "Institution", "year": "c. 100–350 CE, Ethiopia"},
            {"title": "Battle of Adwa (1896) — decisive Ethiopian victory over Italy — preserved sovereignty when virtually all of Africa was being colonised", "type": "EventWindow", "year": "1896, Adwa"},
            {"title": "Cold War superpower patronage shaped Ethiopia's post-1960 politics — first US backing of Haile Selassie, then Soviet backing of the Derg", "type": "EventWindow", "year": "1950–1991, Ethiopia"},
        ],
        "effects": [
            {"title": "Battle of Adwa (1896) inspired Pan-African and anti-colonial movements worldwide as proof that African states could defeat European colonisers", "type": "EventWindow", "year": "1896–present, Africa"},
            {"title": "Haile Selassie's League of Nations speech (1936) became a landmark in anti-imperial rhetoric and made Ethiopia central to Pan-Africanism", "type": "EventWindow", "year": "1936, Geneva"},
            {"title": "Tigray War (2020–2022) killed an estimated 300,000–500,000 people — one of the deadliest conflicts of the 21st century — and shook confidence in Ethiopia's federal model", "type": "EventWindow", "year": "2020–2022, Ethiopia"},
            {"title": "Grand Ethiopian Renaissance Dam (GERD) on the Blue Nile has become a major source of tension with Egypt and Sudan over Nile water rights", "type": "Institution", "year": "2011–present, Ethiopia"},
        ],
        "relationships": [
            {"targetSlug": "haile-selassie", "verb": "INFLUENCES", "note": "Haile Selassie ruled Ethiopia 1930–1974 and made it a symbol of African sovereignty"},
            {"targetSlug": "aksumite-empire", "verb": "INFLUENCES", "note": "The Aksumite Empire was Ethiopia's first great state and gave it early Christianity"},
            {"targetSlug": "battle-of-adwa", "verb": "INFLUENCES", "note": "Ethiopia's 1896 victory over Italy at Adwa made it the symbol of African resistance to colonialism"},
            {"targetSlug": "african-union", "verb": "INFLUENCES", "note": "Ethiopia hosts the African Union headquarters in Addis Ababa, reflecting its symbolic centrality to African unity"},
            {"targetSlug": "tigray-conflict", "verb": "INFLUENCES", "note": "The Tigray War 2020–2022 was one of the deadliest conflicts of the 21st century"},
        ],
        "places": ["Addis Ababa, Ethiopia", "Horn of Africa"],
        "subjects": ["Ethiopia", "Africa", "Horn of Africa", "Battle of Adwa", "Haile Selassie", "Aksumite Empire", "Pan-Africanism"],
        "subjectHeadings": ["Polity — State — Ethiopia — Contemporary"],
        "frameworks": ["postcolonial-history", "political-history"],
        "era": "Contemporary",
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Ethiopia is the symbol of African resistance to colonialism, the seat of one of antiquity's great empires, and — with 126 million people and the African Union on its soil — the Horn of Africa's defining civilisation.",
            "significanceCategory": "continental"
        },
    },
}


# ── helpers ──────────────────────────────────────────────────────────────────

import unicodedata


def _norm(s: str) -> str:
    table = str.maketrans({
        'ł': 'l', 'Ł': 'L', 'ø': 'o', 'Ø': 'O', 'ð': 'd', 'Ð': 'D',
        'þ': 'th', 'ß': 'ss', 'æ': 'ae', 'Æ': 'Ae', 'đ': 'd', 'Đ': 'D',
        'ħ': 'h', 'Ħ': 'H', 'ı': 'i', 'ü': 'u', 'Ü': 'U', 'ö': 'o', 'Ö': 'O',
        'ä': 'a', 'Ä': 'A', 'é': 'e', 'É': 'E', 'è': 'e', 'È': 'E', 'ê': 'e',
        'ó': 'o', 'Ó': 'O', 'ñ': 'n', 'Ñ': 'N', 'í': 'i', 'Í': 'I', 'á': 'a',
        'Á': 'A', 'ú': 'u', 'Ú': 'U', 'ã': 'a', 'õ': 'o', 'ç': 'c', 'Ç': 'C',
        'ș': 's', 'ț': 't', 'ř': 'r', 'š': 's', 'č': 'c', 'ž': 'z', 'ý': 'y',
        'ń': 'n', 'ś': 's', 'ź': 'z', 'ż': 'z', 'ą': 'a', 'ę': 'e',
    })
    s = s.translate(table)
    return unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode("ascii").lower()


def find_file(slug: str) -> str | None:
    direct = os.path.join(FOLDER, f"430{slug}.json")
    if os.path.exists(direct):
        return direct
    norm_slug = _norm(slug)
    for fname in os.listdir(FOLDER):
        if fname.endswith(".json") and fname.startswith("430"):
            if _norm(fname[3:-5]) == norm_slug:
                return os.path.join(FOLDER, fname)
    return None


def apply_enrichment(slug: str, enrichment: dict) -> bool:
    path = find_file(slug)
    if not path:
        print(f"  SKIP {slug} — file not found")
        return False
    with open(path) as fh:
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
    with open(path, "w") as fh:
        json.dump(doc, fh, indent=2, ensure_ascii=False)
    print(f"  OK  {slug:42}  {len(old_summary)}c → {len(entity.get('summary','') or '')}c")
    return True


def main():
    print(f"Enriching {len(ENRICHMENTS)} entities in 430-Class-430 (Batch 6 — Polities)...")
    ok = fail = 0
    for slug, enrichment in ENRICHMENTS.items():
        if apply_enrichment(slug, enrichment):
            ok += 1
        else:
            fail += 1
    print(f"\nDone: {ok} enriched, {fail} skipped.")


if __name__ == "__main__":
    main()
