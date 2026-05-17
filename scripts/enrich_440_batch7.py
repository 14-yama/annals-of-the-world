#!/usr/bin/env python3
"""
Batch 7: 8 cities from 440-Class-440
edirne, nazareth, adana, nakhchivan, chengdu, timbuktu, agrigento, gibraltar.
subjectHeadings always written as list (Appwrite schema requirement).
"""
import json, os, glob, unicodedata
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/440-Class-440"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()

ENRICHMENTS = {
    "edirne": {
        "summary": (
            "Edirne (ancient Adrianople, Turkish Edirne) is a city in north-western Turkey "
            "at the junction of the Tunca and Maritsa rivers and was the Ottoman Empire's "
            "second capital (1363–1453) before Mehmed II conquered Constantinople — giving it "
            "a concentration of imperial mosques and monuments that rivals Istanbul for "
            "architectural splendour.\n\n"
            "Founded as Hadrianopolis by Emperor Hadrian (c. 125 CE), the city witnessed "
            "the Battle of Adrianople (378 CE), one of antiquity's most consequential defeats: "
            "the Visigoth cavalry annihilated a Roman army and killed Emperor Valens, "
            "shattering the myth of Roman military invincibility and opening the Balkans to "
            "Germanic settlement. Under the Ottomans, Edirne became the staging ground for "
            "European campaigns; the Selimiye Mosque (1575), designed by Sinan and considered "
            "his masterpiece, stands here and is a UNESCO World Heritage Site.\n\n"
            "Edirne was the scene of intense fighting during the Balkan Wars (1912–13) and "
            "World War I, exchanged between Turkey and Greece during the Greco-Turkish War "
            "(1919–1922), and is today Turkey's gateway to Europe. Its Kırkpınar oil-wrestling "
            "festival, held annually since at least 1346, is a candidate for the world's "
            "oldest continuously held sporting event."
        ),
        "causes": [
            {"title": "Battle of Adrianople (378 CE) — Visigoths defeated Roman Emperor Valens — was fought at the city and shattered Roman military dominance of the Balkans", "type": "EventWindow", "year": "378 CE, Adrianople"},
            {"title": "Ottoman capture of Adrianople (1363) made it the empire's European capital for 90 years before the fall of Constantinople", "type": "EventWindow", "year": "1363, Adrianople"},
            {"title": "Mimar Sinan chose Edirne as the site for his acknowledged masterpiece, the Selimiye Mosque, reflecting its imperial status", "type": "Person", "year": "1568–1575, Edirne"},
        ],
        "effects": [
            {"title": "Battle of Adrianople (378 CE) caused the Roman Empire's demographic opening to Gothic settlement — an early trigger of the Western Roman Empire's eventual dissolution", "type": "EventWindow", "year": "378 CE, Balkans"},
            {"title": "Selimiye Mosque (1575) became Sinan's declared masterpiece and is considered the pinnacle of Ottoman classical architecture", "type": "Institution", "year": "1575, Edirne"},
            {"title": "Edirne's role as Ottoman launch pad for Balkan campaigns made it the gateway between Asia and Europe for six centuries of imperial history", "type": "Place", "year": "1363–1913, Balkans"},
        ],
        "relationships": [
            {"targetSlug": "battle-of-adrianople", "verb": "OCCURS_IN", "note": "The 378 CE Battle of Adrianople was fought on the city's outskirts and ended Roman Balkan dominance"},
            {"targetSlug": "ottoman-empire", "verb": "INFLUENCES", "note": "Edirne served as the Ottoman capital 1363–1453 before the fall of Constantinople"},
            {"targetSlug": "sinan", "verb": "INFLUENCES", "note": "Mimar Sinan built the Selimiye Mosque in Edirne — his declared masterpiece"},
            {"targetSlug": "constantine-i", "verb": "INFLUENCES", "note": "Edirne (Adrianople) was one of the key Balkan cities contested during Constantine's rise to power"},
        ],
        "places": ["Edirne, Turkey", "Balkans, Europe"],
        "subjects": ["Edirne", "Turkey", "Balkans", "Ottoman Empire", "Battle of Adrianople", "Sinan", "Architecture"],
        "subjectHeadings": ["Place — City — Turkey — Classical"],
        "frameworks": ["political-history", "cultural-history"],
        "era": "Classical",
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Edirne was capital of the Ottoman Empire before Constantinople, site of Rome's most consequential military defeat in 378 CE, and home to Sinan's architectural masterpiece — a city that three times reshaped the history of Europe.",
            "significanceCategory": "continental"
        },
    },
    "nazareth": {
        "summary": (
            "Nazareth is a city in the lower Galilee region of northern Israel, known primarily "
            "as the hometown of Jesus of Nazareth, whose life and teachings here before his "
            "public ministry gave rise to Christianity — the world's largest religion with "
            "2.4 billion adherents.\n\n"
            "A small town in 1st-century Roman-controlled Galilee, Nazareth is mentioned "
            "repeatedly in the New Testament as the place where Jesus grew up, where the "
            "Annunciation occurred, and where he was rejected after returning to preach "
            "('A prophet is not accepted in his hometown'). Archaeological evidence confirms "
            "continuous occupation from the Middle Bronze Age. The city became a major "
            "Christian pilgrimage centre in the Byzantine period; the Basilica of the "
            "Annunciation (completed 1969) marks the traditional site of the Archangel "
            "Gabriel's appearance to Mary.\n\n"
            "Today Nazareth is Israel's largest Arab city with about 80,000 residents, "
            "predominantly Arab Christian and Muslim. It sits at the intersection of Israeli-"
            "Arab tensions and serves as both a living city and a major site for Christian "
            "pilgrimage, drawing over a million visitors annually from around the world."
        ),
        "causes": [
            {"title": "Jesus of Nazareth's upbringing in the town gave it its defining historical significance — without this, Nazareth would be an unremarkable Galilean village", "type": "Person", "year": "c. 6 BCE–26 CE, Nazareth"},
            {"title": "Byzantine imperial promotion of Christian holy sites (4th century CE) brought pilgrims to Nazareth and funded church construction", "type": "EventWindow", "year": "c. 326–640 CE, Nazareth"},
        ],
        "effects": [
            {"title": "As Jesus' hometown, Nazareth became one of Christianity's holiest sites, drawing pilgrims across 2,000 years and shaping the city's social and economic life", "type": "Place", "year": "c. 30 CE–present, Nazareth"},
            {"title": "The Basilica of the Annunciation (1969), built over the Grotto of the Annunciation, is the largest church in the Middle East and a major pilgrimage focus", "type": "Institution", "year": "1969, Nazareth"},
            {"title": "Nazareth's Arab-Christian majority makes it an unusual lens for examining the coexistence of religious heritage, Arab identity, and Israeli statehood", "type": "Place", "year": "1948–present, Israel"},
        ],
        "relationships": [
            {"targetSlug": "jesus-of-nazareth", "verb": "INFLUENCES", "note": "Nazareth is Jesus' hometown — the source of his common epithet and a central site in Christian history"},
            {"targetSlug": "christianity", "verb": "INFLUENCES", "note": "Nazareth's status as Jesus' home made it one of Christianity's foundational holy places"},
            {"targetSlug": "roman-empire", "verb": "INFLUENCES", "note": "Nazareth was in Roman-controlled Galilee during Jesus' lifetime"},
            {"targetSlug": "basilica-of-the-annunciation", "verb": "OCCURS_IN", "note": "The Basilica of the Annunciation in Nazareth marks the traditional site of Gabriel's visit to Mary"},
        ],
        "places": ["Nazareth, Israel", "Galilee, Israel"],
        "subjects": ["Nazareth", "Israel", "Jesus", "Christianity", "Holy Land", "Pilgrimage", "Galilee"],
        "subjectHeadings": ["Place — City — Israel — Classical"],
        "frameworks": ["religious-history", "cultural-history"],
        "era": "Classical",
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Nazareth's significance rests entirely — and enormously — on its role as the hometown of Jesus, making it one of the most spiritually charged places on Earth and a pilgrimage destination for 2,000 years.",
            "significanceCategory": "world-changing"
        },
    },
    "adana": {
        "summary": (
            "Adana is Turkey's fifth-largest city, situated on the fertile Çukurova plain of "
            "southern Anatolia, and one of the oldest continuously inhabited cities in the "
            "world — settled from at least the 13th century BCE and mentioned in Hittite texts. "
            "It sits astride the Seyhan River at the entrance to the Cilician Gates, the "
            "mountain pass through the Taurus range that was the principal land route between "
            "Anatolia and the Levant for thousands of years.\n\n"
            "Adana was successively controlled by the Hittites, Assyrians, Persians, "
            "Alexander the Great, Rome, Byzantium, Arab caliphates, Armenian Cilicia, "
            "the Crusaders, Mamluks, Ramadanids, and Ottomans — each layer visible in its "
            "archaeological and architectural record. The Ottoman-era Stone Bridge (Taşköprü) "
            "spanning the Seyhan was originally built by Emperor Hadrian and has been "
            "continuously used for nearly 2,000 years. The Adana Massacres of 1909 — in "
            "which some 15,000–30,000 Armenians were killed — were a precursor to the "
            "Armenian Genocide of 1915.\n\n"
            "Today Adana is an industrial and agricultural hub famous for its distinctive "
            "kebab cuisine and as a centre of Turkish cotton production. It hosts İncirlik "
            "Air Base, a key NATO installation used in operations across the Middle East."
        ),
        "causes": [
            {"title": "Position on the Seyhan River at the Cilician Gates made Adana the unavoidable gateway between Anatolia and the Levant for 3,000 years", "type": "Place", "year": "c. 1300 BCE–present, Turkey"},
            {"title": "Çukurova plain's agricultural fertility made Adana a natural centre of settlement and tax collection for successive imperial powers", "type": "Place", "year": "c. 1300 BCE–present, Turkey"},
        ],
        "effects": [
            {"title": "Adana Massacres (1909) killed 15,000–30,000 Armenians and served as a rehearsal for the systematic Armenian Genocide of 1915", "type": "EventWindow", "year": "1909, Adana"},
            {"title": "İncirlik Air Base has been a critical NATO installation used in operations against Iraq, Syria, and elsewhere since 1954", "type": "Institution", "year": "1954–present, Adana"},
            {"title": "Adana's role as the gateway to the Cilician Gates shaped the routes of Alexander the Great's campaign, the Crusades, and medieval trade", "type": "Place", "year": "c. 333 BCE–1291 CE, Levant"},
        ],
        "relationships": [
            {"targetSlug": "hittite-empire", "verb": "INFLUENCES", "note": "Adana was an important Hittite city mentioned in texts from the 13th century BCE"},
            {"targetSlug": "alexander-the-great", "verb": "INFLUENCES", "note": "Alexander passed through Adana via the Cilician Gates during his Persian campaign"},
            {"targetSlug": "armenian-genocide", "verb": "INFLUENCES", "note": "The 1909 Adana Massacres prefigured the 1915 Armenian Genocide"},
            {"targetSlug": "ottoman-empire", "verb": "INFLUENCES", "note": "Adana was a major Ottoman city from 1515 until the empire's dissolution"},
        ],
        "places": ["Adana, Turkey", "Cilicia, Turkey", "Taurus Mountains, Turkey"],
        "subjects": ["Adana", "Turkey", "Anatolia", "Cilicia", "Armenian Massacre", "NATO", "Hittites"],
        "subjectHeadings": ["Place — City — Turkey — Prehistoric"],
        "frameworks": ["political-history", "cultural-history"],
        "era": "Prehistoric",
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Adana has been the strategic gateway between Anatolia and the Levant for 3,000 years — traversed by Hittites, Alexander, Crusaders, and today NATO forces — and was the site of the 1909 Armenian massacres that foreshadowed genocide.",
            "significanceCategory": "regional"
        },
    },
    "nakhchivan": {
        "summary": (
            "Nakhchivan is an exclave of Azerbaijan separated from the main territory by "
            "Armenian-controlled land, with a history stretching to the Bronze Age. Its name "
            "is traditionally connected to the biblical Noah, and legend claims it as the "
            "site of Noah's tomb; more concretely, it was the capital of the Araxena satrapy "
            "under the Median and Achaemenid Empires and an important Silk Road stopping point.\n\n"
            "Nakhchivan city was a significant medieval Islamic centre with a distinctive "
            "12th-century architectural tradition exemplified by the Momine Khatun Mausoleum "
            "(1186), designed by the architect Ajami and considered a masterpiece of medieval "
            "Islamic architecture, influencing later mausoleum design across the region. The "
            "exclave changed hands between Persia, Russia, and newly-formed Soviet republics "
            "through the 20th century. It was assigned to Soviet Azerbaijan in 1921, with "
            "Armenian-majority Nagorno-Karabakh separately assigned to Azerbaijan — creating "
            "the territorial knot that exploded in the 1988–1994 and 2020–2023 Karabakh Wars.\n\n"
            "Nakhchivan's physical separation from Azerbaijan creates a geopolitical dependency "
            "on Turkey and Iran for supply, and recent Azerbaijani demands for an "
            "extraterritorial Zangezur corridor connecting Nakhchivan to Azerbaijan through "
            "Armenia is a live flashpoint in South Caucasus geopolitics."
        ),
        "causes": [
            {"title": "Location on the Araxes River made Nakhchivan a natural crossing point between Iran and the South Caucasus, attracting successive imperial powers", "type": "Place", "year": "c. 2000 BCE–present, South Caucasus"},
            {"title": "Soviet nationalities policy in 1921 assigned Nakhchivan to Azerbaijan as an exclave and Nagorno-Karabakh separately, creating the territorial disputes of the 20th century", "type": "EventWindow", "year": "1921, South Caucasus"},
        ],
        "effects": [
            {"title": "Momine Khatun Mausoleum (1186) became one of medieval Islamic architecture's masterpieces, influencing mausoleum design across the region", "type": "Institution", "year": "1186, Nakhchivan"},
            {"title": "Nakhchivan's exclave status created structural dependency on Turkey (through Iran) for all goods and energy, making the Zangezur Corridor question a live territorial dispute", "type": "Place", "year": "1991–present, South Caucasus"},
            {"title": "The Azerbaijan-Armenia territorial dispute over Karabakh was inextricably linked to Nakhchivan's exclave geography, driving two wars and a regional geopolitical realignment", "type": "EventWindow", "year": "1988–2023, South Caucasus"},
        ],
        "relationships": [
            {"targetSlug": "azerbaijan", "verb": "OCCURS_IN", "note": "Nakhchivan is an exclave of Azerbaijan, separated from it by Armenian territory"},
            {"targetSlug": "armenia", "verb": "INFLUENCES", "note": "Armenia surrounds Nakhchivan's connection to Azerbaijan, making relations the central geopolitical issue"},
            {"targetSlug": "persian-empire", "verb": "INFLUENCES", "note": "Nakhchivan was capital of the Achaemenid satrapy of Araxena and later part of successive Persian empires"},
            {"targetSlug": "silk-road", "verb": "INFLUENCES", "note": "Nakhchivan was an important Silk Road stopping point connecting the South Caucasus to Iran and beyond"},
        ],
        "places": ["Nakhchivan, Azerbaijan", "Araxes River, South Caucasus"],
        "subjects": ["Nakhchivan", "Azerbaijan", "South Caucasus", "Exclave", "Islamic Architecture", "Silk Road", "Armenia"],
        "subjectHeadings": ["Place — City — Azerbaijan — Classical"],
        "frameworks": ["political-history", "cultural-history"],
        "era": "Classical",
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Nakhchivan's exclave geography, Silk Road heritage, and medieval Islamic architecture make it a compressed lens on South Caucasus history; its disconnection from Azerbaijan remains a live geopolitical flashpoint.",
            "significanceCategory": "regional"
        },
    },
    "chengdu": {
        "summary": (
            "Chengdu is the capital of China's Sichuan province and one of the country's "
            "oldest continuously inhabited cities, the political and economic centre of the "
            "Sichuan basin for over 2,300 years since the Qin state absorbed the Shu kingdom "
            "in 316 BCE. It is China's most stable major city — never the capital of a "
            "unified China, yet always wealthy enough to sustain art, culture, and philosophy "
            "independent of dynastic upheavals in the north and east.\n\n"
            "The poet Du Fu (712–770 CE), among China's most celebrated, spent four years in "
            "Chengdu during the An Lushan Rebellion; his 'thatched cottage' there is now "
            "China's most visited literary heritage site. The Jinsha site (c. 1200–650 BCE) "
            "and Sanxingdui (c. 1600 BCE) — uncovered near Chengdu — revealed a sophisticated "
            "Bronze Age civilisation entirely separate from Yellow River culture, rewriting "
            "Chinese prehistory. The city pioneered the world's first paper money (jiaozi) in "
            "the Northern Song dynasty (c. 960 CE) and the world's first known irrigation "
            "system still in operation — the Dujiangyan, built 256 BCE, still waters "
            "5,300 km² of farmland.\n\n"
            "Today Chengdu (21 million people) is China's tech hub in the west, home to "
            "Intel, Dell, and hundreds of multinationals, and internationally known as "
            "the home of China's giant panda breeding programme."
        ),
        "causes": [
            {"title": "Sichuan basin's extraordinary agricultural fertility — irrigated by the Dujiangyan system from 256 BCE — supported urban wealth independent of northern Chinese political cycles", "type": "Place", "year": "256 BCE–present, Chengdu"},
            {"title": "Qin conquest of the Shu kingdom (316 BCE) integrated Chengdu into Chinese imperial governance while preserving its distinct Sichuan culture", "type": "EventWindow", "year": "316 BCE, Sichuan"},
        ],
        "effects": [
            {"title": "Dujiangyan irrigation system (256 BCE) has continuously watered 5,300 km² of farmland for 2,280 years, making it the world's oldest large-scale hydraulic engineering project still in operation", "type": "Institution", "year": "256 BCE–present, Sichuan"},
            {"title": "Sanxingdui and Jinsha discoveries revealed a sophisticated independent Bronze Age civilisation in Sichuan, fundamentally revising the model of Chinese civilisational origins", "type": "EventWindow", "year": "1986–2021, Sichuan"},
            {"title": "World's first paper money (jiaozi) issued in Chengdu c. 960 CE revolutionised commerce by replacing heavy coins with portable currency", "type": "Idea", "year": "c. 960 CE, Chengdu"},
        ],
        "relationships": [
            {"targetSlug": "qin-dynasty", "verb": "INFLUENCES", "note": "The Qin absorbed Chengdu in 316 BCE, integrating Sichuan into imperial China"},
            {"targetSlug": "du-fu", "verb": "INFLUENCES", "note": "Du Fu wrote many of his most celebrated poems during his Chengdu years 759–763 CE"},
            {"targetSlug": "sanxingdui", "verb": "OCCURS_IN", "note": "The Sanxingdui Bronze Age site near Chengdu revealed an independent ancient civilisation"},
            {"targetSlug": "silk-road", "verb": "INFLUENCES", "note": "Chengdu was a key node on the southern Silk Road connecting China to Southeast Asia and India"},
        ],
        "places": ["Chengdu, China", "Sichuan, China"],
        "subjects": ["Chengdu", "China", "Sichuan", "Du Fu", "Dujiangyan", "Sanxingdui", "Paper Money"],
        "subjectHeadings": ["Place — City — China — Classical"],
        "frameworks": ["cultural-history", "economic-history"],
        "era": "Classical",
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Chengdu pioneered paper money, built the world's oldest functioning irrigation system, hid a Bronze Age civilisation that rewrote Chinese prehistory, and sheltered China's greatest poet — a city whose innovations quietly shaped global history.",
            "significanceCategory": "continental"
        },
    },
    "timbuktu": {
        "summary": (
            "Timbuktu (Tombouctou) is a city in northern Mali on the southern edge of the "
            "Sahara Desert that served as the intellectual and spiritual capital of West "
            "Africa's greatest medieval empires — the Mali and Songhai — and at its 15th-century "
            "peak was home to 25,000 students and a collection of some 700,000 manuscripts, "
            "making it one of the most important centres of Islamic scholarship in the world.\n\n"
            "Founded c. 1100 CE as a seasonal Tuareg camp on the Niger bend, Timbuktu grew "
            "into a major trans-Saharan trade entrepôt under the Mali Empire and reached its "
            "zenith under the Songhai (1464–1591). The Sankore mosque and madrasa, the "
            "Djinguereber mosque (1327, built by Mansa Musa's Andalusian architect), and "
            "dozens of smaller madrasas educated scholars across the Islamic world in Quranic "
            "studies, law, astronomy, mathematics, and history. After Moroccan conquest in "
            "1591 scattered its scholars and sacked its libraries, Timbuktu entered a long "
            "decline. By the 19th century, European explorers treated it as a mythical city "
            "of gold.\n\n"
            "During the 2012 jihadist occupation, thousands of manuscripts were secretly "
            "evacuated to Bamako, becoming one of the world's most celebrated heritage rescue "
            "operations. UNESCO designated Timbuktu a World Heritage Site in 1988; its "
            "earthen mosques were damaged by jihadists in 2012–13 and are being restored."
        ),
        "causes": [
            {"title": "Position at the Niger bend — the intersection of Saharan caravan routes and Niger river navigation — made Timbuktu the unavoidable entrepôt between the Sahara and West Africa", "type": "Place", "year": "c. 1100–1600, Mali"},
            {"title": "Mali Empire's gold wealth, and particularly Mansa Musa's patronage after his 1324 hajj, funded mosque construction and attracted scholars from across the Islamic world", "type": "Person", "year": "1312–1337, Mali"},
        ],
        "effects": [
            {"title": "Sankore University became one of the medieval world's great academic institutions, training scholars who disseminated West African Islamic learning across the Sahara", "type": "Institution", "year": "c. 1400–1591, Timbuktu"},
            {"title": "Timbuktu's 700,000 manuscripts represent the largest surviving corpus of sub-Saharan African scholarly writing — the foundation of African intellectual history", "type": "Text", "year": "c. 1200–present, Timbuktu"},
            {"title": "Moroccan conquest (1591) ended Timbuktu's golden age and dispersed its scholar community, marking the effective end of the medieval West African intellectual tradition", "type": "EventWindow", "year": "1591, Timbuktu"},
            {"title": "2012 manuscript evacuation rescued over 300,000 documents from jihadist destruction, demonstrating the fragility of the world's most remote documentary heritage", "type": "EventWindow", "year": "2012, Timbuktu"},
        ],
        "relationships": [
            {"targetSlug": "mansa-musa", "verb": "INFLUENCES", "note": "Mansa Musa funded the Djinguereber mosque and patronised Timbuktu's scholars after his 1324 hajj"},
            {"targetSlug": "mali-empire", "verb": "INFLUENCES", "note": "Timbuktu flourished as the intellectual centre of the Mali Empire 13th–15th centuries"},
            {"targetSlug": "songhai-empire", "verb": "INFLUENCES", "note": "Timbuktu reached its peak under the Songhai Empire before the 1591 Moroccan conquest"},
            {"targetSlug": "trans-saharan-trade", "verb": "INFLUENCES", "note": "Trans-Saharan gold-salt trade made Timbuktu the pivot of West African commerce"},
        ],
        "places": ["Timbuktu, Mali", "Niger River, West Africa", "Sahara Desert, Africa"],
        "subjects": ["Timbuktu", "Mali", "West Africa", "Islamic Scholarship", "Mansa Musa", "Sahara", "Manuscripts"],
        "subjectHeadings": ["Place — City — Mali — Medieval"],
        "frameworks": ["intellectual-history", "cultural-history"],
        "era": "Medieval",
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Timbuktu was the Oxford of medieval West Africa — a city of 25,000 students and 700,000 manuscripts whose destruction and rescue encapsulates the vulnerability of the world's most remote intellectual heritage.",
            "significanceCategory": "continental"
        },
    },
    "agrigento": {
        "summary": (
            "Agrigento (ancient Akragas) is a city on the southern coast of Sicily that was "
            "one of the leading cities of the ancient Greek world — at its 5th-century BCE "
            "peak the third-largest Greek polis after Athens and Syracuse — and possesses "
            "the finest collection of Doric Greek temples outside of Athens, concentrated in "
            "the Valley of the Temples (UNESCO World Heritage Site).\n\n"
            "Founded as a Rhodian-Cretan colony c. 582 BCE, Akragas flourished under the "
            "tyrant Theron (488–472 BCE), who allied with Syracuse to defeat the Carthaginian "
            "army at the Battle of Himera (480 BCE) — fought the same day as Salamis. At its "
            "height the city had 200,000 inhabitants and began seven temples, including the "
            "Temple of Olympian Zeus — intended to be the largest Doric temple ever built — "
            "using Carthaginian prisoners of war as labour. The philosopher Empedocles "
            "(c. 490–430 BCE) was a native son; his four-element theory of matter (earth, "
            "water, fire, air) dominated Western natural philosophy for 2,000 years.\n\n"
            "Devastated by Carthage in 406 BCE, contested between Rome and Carthage, and "
            "several times looted of its art by Roman governors (Cicero prosecuted Verres for "
            "theft), Agrigento's ruins survive in extraordinary condition. Modern Agrigento "
            "is a mid-sized Sicilian city still overshadowed by its ancient past."
        ),
        "causes": [
            {"title": "Greek colonial expansion in the 7th–6th centuries BCE spread city-states across the Mediterranean and led to the founding of Akragas as a Rhodian-Cretan colony c. 582 BCE", "type": "EventWindow", "year": "c. 582 BCE, Sicily"},
            {"title": "Battle of Himera (480 BCE) — simultaneous with Salamis — shattered Carthaginian power in Sicily and opened a generation of peace that allowed Akragas to flourish", "type": "EventWindow", "year": "480 BCE, Sicily"},
        ],
        "effects": [
            {"title": "Valley of the Temples contains seven Doric temples in the finest state of preservation outside Greece, making Agrigento Sicily's most important archaeological site", "type": "Place", "year": "c. 510–430 BCE, Agrigento"},
            {"title": "Empedocles' four-element theory (earth, water, fire, air) became the foundational model of Western natural philosophy for 2,000 years until the Scientific Revolution", "type": "Idea", "year": "c. 460 BCE, Agrigento"},
            {"title": "Cicero's prosecution of Verres for the theft of Akragas' artworks became a landmark in Roman legal history and the concept of art as heritage", "type": "EventWindow", "year": "70 BCE, Rome"},
        ],
        "relationships": [
            {"targetSlug": "empedocles", "verb": "INFLUENCES", "note": "Empedocles, originator of the four-element theory, was born and worked in Akragas"},
            {"targetSlug": "carthage", "verb": "INFLUENCES", "note": "Carthage sacked Akragas in 406 BCE, ending its golden age"},
            {"targetSlug": "roman-republic", "verb": "INFLUENCES", "note": "Rome conquered Akragas in 210 BCE; Cicero prosecuted the Roman governor Verres for looting its art"},
            {"targetSlug": "greek-colonization", "verb": "INFLUENCES", "note": "Agrigento was founded as a Greek colony c. 582 BCE during the great age of Greek colonial expansion"},
        ],
        "places": ["Agrigento, Sicily, Italy", "Mediterranean Sea"],
        "subjects": ["Agrigento", "Sicily", "Ancient Greece", "Doric Architecture", "Empedocles", "Carthage", "Magna Graecia"],
        "subjectHeadings": ["Place — City — Italy — Classical"],
        "frameworks": ["cultural-history", "intellectual-history"],
        "era": "Classical",
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Agrigento was the third-greatest city in the ancient Greek world, birthplace of the four-element theory that shaped Western science for 2,000 years, and possesses the best-preserved Doric temples outside Athens.",
            "significanceCategory": "continental"
        },
    },
    "gibraltar": {
        "summary": (
            "Gibraltar is a British Overseas Territory at the southern tip of the Iberian "
            "Peninsula controlling the narrow strait — just 14 km wide — between the Atlantic "
            "Ocean and the Mediterranean Sea, one of the most strategically vital maritime "
            "chokepoints in the world. The Rock of Gibraltar was one of antiquity's 'Pillars "
            "of Hercules' — the mythological boundary of the known world.\n\n"
            "Captured by a combined Anglo-Dutch force in 1704 during the War of the Spanish "
            "Succession, Gibraltar was formally ceded to Britain in the Treaty of Utrecht "
            "(1713) and has been British ever since despite Spain's persistent territorial "
            "claim. The Rock's fortifications — augmented through the Napoleonic Wars and "
            "World War II (when a network of 34 miles of tunnels was excavated) — made it "
            "nearly impregnable; it survived four major sieges, including the Great Siege "
            "(1779–1783), the longest in British history.\n\n"
            "Gibraltar's Barbary macaques, the only wild primates in Europe, are legendary: "
            "British folklore holds that if the macaques leave, Gibraltar will revert to "
            "Spain. Churchill ordered their population topped up in 1944 when numbers fell "
            "dangerously low. Gibraltar's status remains unresolved after Brexit complicated "
            "its Schengen-border relationship with Spain — a persistent thorn in UK-Spain "
            "relations."
        ),
        "causes": [
            {"title": "Gibraltar's position at the Atlantic-Mediterranean chokepoint gave it military and commercial value far exceeding its tiny 6.7 km² area", "type": "Place", "year": "c. 700 BCE–present, Gibraltar"},
            {"title": "War of the Spanish Succession (1701–1714) provided the opportunity for Anglo-Dutch capture of Gibraltar in 1704 and its cession to Britain at Utrecht", "type": "EventWindow", "year": "1704, Gibraltar"},
        ],
        "effects": [
            {"title": "British control of Gibraltar (1713–present) gave the Royal Navy a strategic Atlantic-Mediterranean gateway that was central to British imperial sea power for 250 years", "type": "Institution", "year": "1713–present, Gibraltar"},
            {"title": "Great Siege (1779–1783) — the longest siege in British military history — saw the garrison hold out for 3 years and 7 months against Spain and France", "type": "EventWindow", "year": "1779–1783, Gibraltar"},
            {"title": "Brexit (2016–2020) threatened Gibraltar's open-border relationship with Spain, reopening the sovereignty question and generating diplomatic complications that remain unresolved", "type": "EventWindow", "year": "2016–present, Gibraltar"},
        ],
        "relationships": [
            {"targetSlug": "british-empire", "verb": "INFLUENCES", "note": "Gibraltar has been a British possession since 1704, central to Royal Navy Mediterranean strategy"},
            {"targetSlug": "spain", "verb": "INFLUENCES", "note": "Spain has claimed Gibraltar since the Treaty of Utrecht and periodically closed the border"},
            {"targetSlug": "treaty-of-utrecht", "verb": "INFLUENCES", "note": "The 1713 Treaty of Utrecht formally ceded Gibraltar to Britain in perpetuity"},
            {"targetSlug": "nato", "verb": "INFLUENCES", "note": "Gibraltar hosts a major NATO naval base and monitoring station at the Atlantic-Mediterranean junction"},
        ],
        "places": ["Gibraltar", "Strait of Gibraltar, Europe", "Iberian Peninsula, Europe"],
        "subjects": ["Gibraltar", "Britain", "Spain", "Strait of Gibraltar", "Naval Power", "Sovereignty Dispute", "Mediterranean"],
        "subjectHeadings": ["Place — City — Gibraltar — Early Modern"],
        "frameworks": ["political-history", "military-history"],
        "era": "Early Modern",
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Gibraltar commands the world's most strategically vital sea lane and has been the object of one of the longest-running sovereignty disputes in history — its 6.7 km² have mattered more to British imperial strategy than most entire nations.",
            "significanceCategory": "continental"
        },
    },
}


# ── helpers ──────────────────────────────────────────────────────────────────

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
    direct = os.path.join(FOLDER, f"440{slug}.json")
    if os.path.exists(direct):
        return direct
    norm_slug = _norm(slug)
    for fname in os.listdir(FOLDER):
        if fname.endswith(".json") and fname.startswith("440"):
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
    print(f"Enriching {len(ENRICHMENTS)} entities in 440-Class-440 (Batch 7 — Cities)...")
    ok = fail = 0
    for slug, enrichment in ENRICHMENTS.items():
        if apply_enrichment(slug, enrichment):
            ok += 1
        else:
            fail += 1
    print(f"\nDone: {ok} enriched, {fail} skipped.")


if __name__ == "__main__":
    main()
