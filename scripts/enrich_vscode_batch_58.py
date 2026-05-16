#!/usr/bin/env python3
"""
VS Code Enrichment Batch 58 — 8 Major Historical Persons
Florence Nightingale, Marie Curie, Al-Khwarizmi, Ibn Khaldun,
Akbar the Great, Catherine the Great, Archimedes, Dante Alighieri

EDITOR_ID:  claude-sonnet-4.6·cloud·GH#vscode
SESSION_ID: vscode-batch-58-may2026
"""

import json
import os
import sys
import copy
from datetime import datetime, timezone

DRY_RUN = "--dry-run" in sys.argv
EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-58-may2026"
SKIP_THRESHOLD = 800  # skip if summary already >= this length

ENRICHMENTS = [
    # ── 1. Florence Nightingale ──────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/201-Class-201/201florence-nightingale.json",
        "slug": "florence-nightingale",
        "era_correction": None,
        "data": {
            "summary": (
                "Florence Nightingale (1820–1910) was a British nurse, statistician, and social reformer who transformed medicine and established nursing as a respected profession. Born into a wealthy English family, she defied Victorian conventions to pursue a calling in healthcare, becoming the most celebrated nurse of the 19th century. Her work during the Crimean War (1853–1856) remains one of history's greatest demonstrations of evidence-based public health reform.\n\n"
                "Deployed to military hospitals in Scutari, Nightingale found catastrophic conditions—overcrowded wards, contaminated water, and rampant infection. Using meticulous data collection and her pioneering polar area diagrams (an early form of infographic), she proved that most soldier deaths resulted from preventable diseases rather than battle wounds. By implementing sanitation protocols, she reduced the hospital death rate from 42% to 2%—a triumph that made her the forerunner of evidence-based medicine.\n\n"
                "After the war, Nightingale founded the first professional nursing school at St Thomas' Hospital in London (1860) and spent decades lobbying for hospital design reform, military health improvements, and colonial public health in India. She was the first woman inducted into the Order of Merit (1907) and became the symbolic founder of modern healthcare systems worldwide.\n\n"
                "'The Lady with the Lamp' — as troops called her during nighttime ward rounds — left a legacy that extends from global nursing education to the modern discipline of medical statistics and hospital epidemiology."
            ),
            "causes": [
                "Crimean War (1853–1856) exposing catastrophic military hospital conditions",
                "Victorian England's negligence of nursing as a profession or science",
                "Statistical revolution in public health pioneered by William Farr",
                "Personal religious calling and financial independence enabling defiance of social norms",
            ],
            "effects": [
                "Foundation of modern professional nursing and nursing education",
                "Nightingale School of Nursing at St Thomas' Hospital (1860) — first in the world",
                "Evidence-based hospital design reform reducing infection mortality",
                "Pioneer of data visualization in public health (polar area charts)",
                "Reduction of Crimean hospital death rate from 42% to 2%",
                "Transformation of Indian colonial public health policy",
                "Standardization of hospital statistics and medical record-keeping",
            ],
            "relationships": [
                {"type": "OCCURS_IN", "target": "Crimean War", "targetSlug": "crimean-war", "note": "Theatre of her nursing reform"},
                {"type": "INFLUENCES", "target": "Nursing profession", "targetSlug": "nursing-profession", "note": "Founded modern nursing"},
                {"type": "INFLUENCES", "target": "Evidence-based medicine", "targetSlug": "evidence-based-medicine", "note": "Pioneered statistical approach to healthcare"},
                {"type": "INFLUENCES", "target": "Public health reform", "targetSlug": "public-health-reform", "note": "Transformed hospital sanitation standards"},
                {"type": "INFLUENCES", "target": "William Farr", "targetSlug": "william-farr", "note": "Collaborated on medical statistics"},
                {"type": "OCCURS_IN", "target": "Victorian Britain", "targetSlug": "victorian-britain", "note": "Social context of her reforms"},
                {"type": "INFLUENCES", "target": "Data visualization", "targetSlug": "data-visualization", "note": "Invented polar area diagram for mortality data"},
                {"type": "OCCURS_IN", "target": "Ottoman Empire", "targetSlug": "ottoman-empire", "note": "Scutari hospital located in Ottoman territory"},
                {"type": "INFLUENCES", "target": "British Army Medical Corps", "targetSlug": "british-army-medical-corps", "note": "Forced sanitation reform"},
                {"type": "INFLUENCES", "target": "International Red Cross", "targetSlug": "international-red-cross", "note": "Inspired parallel humanitarian medical movement"},
                {"type": "INFLUENCES", "target": "Mary Seacole", "targetSlug": "mary-seacole", "note": "Contemporary Crimean War nurse"},
                {"type": "INFLUENCES", "target": "India colonial health policy", "targetSlug": "india-colonial-health", "note": "Lobbied for sanitary improvements in India"},
                {"type": "INFLUENCES", "target": "Women in medicine", "targetSlug": "women-in-medicine", "note": "Opened doors for professional women in healthcare"},
                {"type": "INFLUENCES", "target": "Modern hospital design", "targetSlug": "modern-hospital-design", "note": "Notes on Nursing and hospital design standards"},
                {"type": "INFLUENCES", "target": "World Health Organization (WHO)", "targetSlug": "world-health-organization", "note": "Intellectual ancestor of global public health"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Florence Nightingale transformed nursing from menial service into a scientific profession and laid the foundations of modern hospital epidemiology, evidence-based medicine, and public health statistics — changes that have saved hundreds of millions of lives."
            },
            "quote": "'The very first requirement in a hospital is that it should do the sick no harm.' — Florence Nightingale",
            "places": ["London, England", "Scutari, Ottoman Empire (modern Istanbul)", "Florence, Italy (birthplace)"],
            "subjectHeadings": "Florence Nightingale — Public Health Reformers — United Kingdom — Modern",
            "subjects": ["United Kingdom", "nursing", "public health", "Crimean War", "statistics", "medicine", "women pioneers", "Victorian era", "hospital reform", "data visualization"],
            "frameworks": ["social-welfare", "feminist-history", "scientific-revolution"],
        }
    },

    # ── 2. Marie Curie ───────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/201-Class-201/201marie-curie.json",
        "slug": "marie-curie",
        "era_correction": None,
        "data": {
            "summary": (
                "Marie Curie (1867–1934) was a Polish-born physicist and chemist who became the first person — and the only woman — to win Nobel Prizes in two different scientific fields, fundamentally reshaping humanity's understanding of radioactivity and atomic structure. Born Maria Sklodowska in Warsaw under Russian occupation, she overcame poverty, gender discrimination, and political oppression to become one of history's greatest scientists.\n\n"
                "With her husband Pierre Curie, she isolated two new elements from pitchblende ore: polonium (1898, named for her occupied homeland) and radium (1898). Her Nobel Prize in Physics (1903) recognized this work on radioactivity — a term she coined; her Nobel Prize in Chemistry (1911) honored her isolation of pure radium. These discoveries proved that atoms could emit energy and transform, laying the groundwork for nuclear physics and quantum theory.\n\n"
                "During World War I, Curie developed mobile X-ray units ('petites Curies') that served field hospitals, directly saving tens of thousands of soldiers' lives. She also founded the Curie Institutes in Paris and Warsaw, which remain leading cancer research centers. Tragically, she died from aplastic anaemia caused by decades of radiation exposure — a hazard unknown in her time.\n\n"
                "Her legacy transcends science: she shattered gender barriers in academia at the highest level, inspiring generations of women scientists. As she said: 'Nothing in life is to be feared, it is only to be understood. Now is the time to understand more.'"
            ),
            "causes": [
                "Henri Becquerel's discovery of radioactivity (1896) opening new research domain",
                "Pierre Curie's partnership providing laboratory access and scientific collaboration",
                "Paris scientific community at the Sorbonne enabling rigorous research",
                "Determination to overcome systemic gender exclusion from European academia",
            ],
            "effects": [
                "Discovery of polonium and radium, two new chemical elements",
                "Coining the term 'radioactivity' and establishing it as a field of study",
                "Nobel Prize in Physics (1903) — first woman laureate",
                "Nobel Prize in Chemistry (1911) — only person to win in two sciences",
                "WWI mobile X-ray field hospitals saving tens of thousands of lives",
                "Foundation of Curie Institutes in Paris and Warsaw (cancer research)",
                "Inspiration for women's participation in science globally",
                "Nuclear physics and radiotherapy as medical treatment",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Nuclear physics", "targetSlug": "nuclear-physics", "note": "Foundational research on radioactivity"},
                {"type": "INFLUENCES", "target": "Pierre Curie", "targetSlug": "pierre-curie", "note": "Husband and scientific collaborator"},
                {"type": "INFLUENCES", "target": "Henri Becquerel", "targetSlug": "henri-becquerel", "note": "Shared Nobel Prize 1903"},
                {"type": "INFLUENCES", "target": "Radiotherapy", "targetSlug": "radiotherapy", "note": "Radium used in cancer treatment"},
                {"type": "OCCURS_IN", "target": "University of Paris (Sorbonne)", "targetSlug": "sorbonne", "note": "Primary research institution"},
                {"type": "INFLUENCES", "target": "Women in science", "targetSlug": "women-in-science", "note": "First woman professor at Sorbonne"},
                {"type": "INFLUENCES", "target": "World War I medicine", "targetSlug": "world-war-i-medicine", "note": "Developed petites Curies X-ray units"},
                {"type": "INFLUENCES", "target": "Curie Institute Paris", "targetSlug": "curie-institute-paris", "note": "Founded 1920"},
                {"type": "INFLUENCES", "target": "Albert Einstein", "targetSlug": "albert-einstein", "note": "Peer and Solvay Conference colleague"},
                {"type": "INFLUENCES", "target": "Ernest Rutherford", "targetSlug": "ernest-rutherford", "note": "Fellow pioneer of atomic structure"},
                {"type": "INFLUENCES", "target": "Irène Joliot-Curie", "targetSlug": "irene-joliot-curie", "note": "Daughter, also Nobel laureate in Chemistry"},
                {"type": "OCCURS_IN", "target": "Poland", "targetSlug": "poland", "note": "Birthplace, named polonium after it"},
                {"type": "OCCURS_IN", "target": "France", "targetSlug": "france", "note": "Country of scientific career"},
                {"type": "INFLUENCES", "target": "Quantum mechanics", "targetSlug": "quantum-mechanics", "note": "Radioactivity evidence for atomic energy levels"},
                {"type": "INFLUENCES", "target": "Periodic table", "targetSlug": "periodic-table", "note": "Added polonium and radium"},
            ],
            "historicalSignificance": {
                "significanceScore": 10,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Marie Curie's discovery of radioactivity and two new elements transformed physics and chemistry, enabled cancer radiotherapy, and remains one of the most important scientific breakthroughs in human history — achieved against extraordinary barriers of gender and class."
            },
            "quote": "'Nothing in life is to be feared, it is only to be understood. Now is the time to understand more, so that we may fear less.' — Marie Curie",
            "places": ["Warsaw, Poland", "Paris, France", "Sorbonne University", "Curie Institute"],
            "subjectHeadings": "Marie Curie — Scientists and Physicists — Poland/France — Modern",
            "subjects": ["Poland", "France", "nuclear physics", "radioactivity", "Nobel Prize", "chemistry", "physics", "women scientists", "World War I", "cancer research"],
            "frameworks": ["scientific-revolution", "feminist-history", "technological-change"],
        }
    },

    # ── 3. Al-Khwarizmi ──────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/213-Class-213/213al-khwarizmi.json",
        "slug": "al-khwarizmi",
        "era_correction": None,
        "data": {
            "summary": (
                "Al-Khwarizmi (c. 780–850 CE) was a Persian mathematician, astronomer, and scholar at the House of Wisdom in Baghdad whose works gave the world algebra, popularized the Hindu-Arabic numeral system, and introduced the concept of algorithms — making him arguably the most consequential mathematician in history. His latinized name, Algoritmi, is the direct etymological source of the word 'algorithm.'\n\n"
                "His landmark treatise, Al-Kitāb al-mukhtaṣar fī ḥisāb al-jabr wal-muqābala (c. 820 CE), established algebra as a systematic discipline. The word 'algebra' itself derives from al-jabr in the title. By expressing mathematical problems in general procedural terms rather than as geometric constructions, he gave mathematics a universal language applicable to trade, surveying, inheritance law, and astronomy.\n\n"
                "His astronomical tables (Zīj al-Sindhind) and treatise on Hindu numerals introduced Europe to the positional decimal system and zero as a placeholder — a conceptual revolution that made computation at scale possible. Translated into Latin by Adelard of Bath in the 12th century, his works entered European universities and transformed mathematics for five centuries.\n\n"
                "Without Al-Khwarizmi's transmission of decimal arithmetic and algebraic method, the Scientific Revolution, financial capitalism, computer science, and modern engineering would have been impossible. He is rightly called the 'Father of Algebra.'"
            ),
            "causes": [
                "Abbasid Caliphate's patronage of the House of Wisdom under Caliph al-Ma'mun",
                "Indian mathematical traditions (Brahmagupta's zero and decimal positional system)",
                "Greek geometric algebra traditions (Euclid, Diophantus) providing foundation",
                "Islamic commercial economy requiring practical arithmetic solutions",
            ],
            "effects": [
                "Founding of algebra as a systematic mathematical discipline",
                "Popularization of Hindu-Arabic numerals and decimal system in Islamic and later European science",
                "Introduction of zero as operational placeholder to Western mathematics",
                "Origin of the word 'algorithm' from his name",
                "Origin of the word 'algebra' from his treatise title (al-jabr)",
                "12th-century Latin translations enabling European mathematical revolution",
                "Foundations for calculus, computer science, and modern engineering",
            ],
            "relationships": [
                {"type": "OCCURS_IN", "target": "House of Wisdom", "targetSlug": "house-of-wisdom", "note": "Primary institution of scholarship"},
                {"type": "OCCURS_IN", "target": "Abbasid Caliphate", "targetSlug": "abbasid-caliphate", "note": "Political and intellectual context"},
                {"type": "INFLUENCES", "target": "Algebra", "targetSlug": "algebra", "note": "Foundational text — al-jabr"},
                {"type": "INFLUENCES", "target": "Algorithm (concept)", "targetSlug": "algorithm", "note": "Name became eponym for algorithms"},
                {"type": "INFLUENCES", "target": "Decimal number system", "targetSlug": "decimal-number-system", "note": "Transmitted Hindu-Arabic numerals to Islamic world"},
                {"type": "INFLUENCES", "target": "European medieval mathematics", "targetSlug": "european-mathematics-medieval", "note": "Latin translations shaped scholastic mathematics"},
                {"type": "INFLUENCES", "target": "Fibonacci", "targetSlug": "fibonacci", "note": "Fibonacci's Liber Abaci transmitted his numeral system to Europe"},
                {"type": "INFLUENCES", "target": "Brahmagupta", "targetSlug": "brahmagupta", "note": "Indian mathematician whose work Al-Khwarizmi synthesized"},
                {"type": "INFLUENCES", "target": "Computer science", "targetSlug": "computer-science", "note": "Algorithm concept is foundational to computing"},
                {"type": "INFLUENCES", "target": "Islamic Golden Age", "targetSlug": "islamic-golden-age", "note": "Central figure in the age of Islamic learning"},
                {"type": "OCCURS_IN", "target": "Baghdad", "targetSlug": "baghdad", "note": "City of scholarship and the House of Wisdom"},
                {"type": "INFLUENCES", "target": "Trigonometry", "targetSlug": "trigonometry", "note": "Contributed astronomical tables with trigonometric functions"},
                {"type": "INFLUENCES", "target": "Cartography", "targetSlug": "cartography", "note": "Revised Ptolemy's Geography with improved coordinates"},
                {"type": "INFLUENCES", "target": "Adelard of Bath", "targetSlug": "adelard-of-bath", "note": "12th-century translator of his astronomical tables"},
                {"type": "INFLUENCES", "target": "Scientific Revolution", "targetSlug": "scientific-revolution", "note": "Algebraic method enabled Copernicus, Kepler, Newton"},
            ],
            "historicalSignificance": {
                "significanceScore": 10,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Al-Khwarizmi gave the world algebra and algorithms — two concepts so fundamental to modern civilization that his name lives in the word 'algorithm' itself. Without his transmission of decimal arithmetic, computer science, the Scientific Revolution, and modern engineering would have been impossible."
            },
            "quote": "'When I consider what people generally want in calculating, I found that it always is a number.' — Al-Khwarizmi, Kitāb al-mukhtaṣar",
            "places": ["Baghdad, Iraq", "Khwarazm, Central Asia (modern Uzbekistan)"],
            "subjectHeadings": "Al-Khwarizmi — Mathematicians and Scientists — Islamic Golden Age — Medieval",
            "subjects": ["Iraq", "Uzbekistan", "mathematics", "algebra", "algorithms", "Islamic Golden Age", "House of Wisdom", "astronomy", "Abbasid Caliphate", "decimal system"],
            "frameworks": ["scientific-revolution", "intellectual-history", "transmission-of-knowledge"],
        }
    },

    # ── 4. Ibn Khaldun ───────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/202-Class-202/202ibn-khaldun.json",
        "slug": "ibn-khaldun",
        "era_correction": None,
        "data": {
            "summary": (
                "Ibn Khaldun (1332–1406) was a Tunisian-born Arab polymath, historian, and statesman whose Muqaddimah (1377) stands as the founding document of modern sociology, historiography, and the philosophy of history. Writing during the turbulent post-Black Death era of the Maghreb, he developed the first systematic theory of historical change based on observable social forces — a methodology centuries ahead of its time.\n\n"
                "The Muqaddimah ('Introduction to History') analyzed the rise and fall of civilizations through the concept of asabiyya — social cohesion, group solidarity, and shared purpose. Ibn Khaldun argued that nomadic societies develop strong asabiyya enabling them to conquer sedentary civilizations, but as conquerors settle and grow wealthy, their cohesion decays and new challengers replace them. This cyclical model anticipated Toynbee, Spengler, and modern structural sociology by five centuries.\n\n"
                "Beyond historiography, the Muqaddimah contains pioneering insights in economics (labor theory of value, supply and demand), political science, urban planning, and psychology. He recognized that excessive taxation destroys economies, that wealth accumulates through division of labor, and that urban complexity emerges from agriculture and trade — concepts not formalized in European thought until Adam Smith.\n\n"
                "Arnold Toynbee called it 'undoubtedly the greatest work of its kind that has ever yet been created by any mind.' The Muqaddimah remains a living text in social science curricula worldwide."
            ),
            "causes": [
                "Black Death (1347–1351) devastating North African and Middle Eastern societies",
                "Fragmentation and succession crises in Maghrebi dynasties (Hafsids, Marinids)",
                "Islamic historiographical tradition (al-Tabari, al-Masudi) providing intellectual lineage",
                "Personal experience of political upheaval across multiple courts",
            ],
            "effects": [
                "Founding of sociology as systematic study of social structures",
                "Muqaddimah (1377) — first scientific philosophy of history",
                "Asabiyya concept influencing modern theories of social cohesion and state formation",
                "Cyclical theory of civilization anticipating Toynbee and Spengler",
                "Economic observations anticipating Adam Smith's theory of labor and capital",
                "Influence on Ottoman historians (Kātib Çelebi) and later European social thinkers",
                "Modern sociology tracing its origins to his empirical methods",
            ],
            "relationships": [
                {"type": "INFLUENCES", "target": "Sociology (discipline)", "targetSlug": "sociology", "note": "Founding figure of sociological thought"},
                {"type": "INFLUENCES", "target": "Muqaddimah", "targetSlug": "muqaddimah", "note": "His masterwork — the first work of social science"},
                {"type": "OCCURS_IN", "target": "Tunisia", "targetSlug": "tunisia", "note": "Born in Tunis, 1332"},
                {"type": "OCCURS_IN", "target": "Egypt", "targetSlug": "egypt", "note": "Last years as Chief Maliki Judge in Cairo"},
                {"type": "INFLUENCES", "target": "Black Death", "targetSlug": "black-death", "note": "The plague's disruptions shaped his cyclical theory"},
                {"type": "INFLUENCES", "target": "Hafsid dynasty", "targetSlug": "hafsid-dynasty", "note": "Served at Hafsid court in Tunisia"},
                {"type": "INFLUENCES", "target": "Timur (Tamerlane)", "targetSlug": "tamerlane", "note": "Met Timur outside Damascus, 1401"},
                {"type": "INFLUENCES", "target": "Adam Smith", "targetSlug": "adam-smith", "note": "Economic theories on labor and taxation prefigured Wealth of Nations"},
                {"type": "INFLUENCES", "target": "Émile Durkheim", "targetSlug": "emile-durkheim", "note": "Asabiyya concept parallels social solidarity theory"},
                {"type": "INFLUENCES", "target": "Max Weber", "targetSlug": "max-weber", "note": "State formation and legitimacy analysis"},
                {"type": "INFLUENCES", "target": "Arnold Toynbee", "targetSlug": "arnold-toynbee", "note": "Called Muqaddimah greatest historical work ever"},
                {"type": "OCCURS_IN", "target": "Marinid dynasty", "targetSlug": "marinid-dynasty", "note": "Served at Moroccan Marinid court"},
                {"type": "INFLUENCES", "target": "Islamic historiography", "targetSlug": "islamic-historiography", "note": "Synthesized and transcended prior Muslim historical writing"},
                {"type": "INFLUENCES", "target": "Ottoman historiography", "targetSlug": "ottoman-historiography", "note": "Directly influenced Kātib Çelebi and Ottoman scholars"},
                {"type": "INFLUENCES", "target": "Cyclical theory of history", "targetSlug": "cyclical-history", "note": "Rise-and-fall civilization model"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Ibn Khaldun's Muqaddimah created sociology, pioneered the philosophy of history, and anticipated Adam Smith's economics by 400 years — the most intellectually advanced social theory produced anywhere in the world before the European Enlightenment."
            },
            "quote": "'He who finds a new path is a pathfinder, even if the trail has to be found again by others; and he who walks far ahead of his contemporaries is a leader, even though centuries elapse before he is understood.' — Ibn Khaldun",
            "places": ["Tunis, Tunisia", "Cairo, Egypt", "Fez, Morocco", "Seville, Spain"],
            "subjectHeadings": "Ibn Khaldun — Historians and Social Theorists — North Africa — Medieval",
            "subjects": ["Tunisia", "Egypt", "sociology", "historiography", "Islamic Golden Age", "Muqaddimah", "social theory", "political philosophy", "North Africa", "Black Death"],
            "frameworks": ["intellectual-history", "social-theory", "islamic-civilization"],
        }
    },

    # ── 5. Akbar the Great ───────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/221-Class-221/221akbar.json",
        "slug": "akbar",
        "era_correction": None,
        "data": {
            "summary": (
                "Akbar the Great (1542–1605) was the third and greatest Mughal Emperor of India, reigning from 1556 to 1605, who transformed a fragile dynasty into a vast and sophisticated empire encompassing most of the Indian subcontinent. Ascending the throne at thirteen after his father Humayun's sudden death, Akbar proved himself one of history's most gifted military commanders, administrators, and patrons of culture.\n\n"
                "Akbar's reign was defined by a series of brilliant innovations. He abolished the jizya tax on non-Muslims, promoted Hindus to the highest imperial offices, and forged marriage alliances with Rajput rulers — creating a composite Mughal-Rajput governing class unprecedented in Indian history. His administrative system, the Mansabdari, rationalized military ranks and revenue collection into a meritocratic imperial bureaucracy that governed 100 million people.\n\n"
                "He founded a new syncretic spiritual philosophy, the Din-i-Ilahi (Divine Faith), blending elements of Islam, Hinduism, Zoroastrianism, and Christianity in an attempt to create a universal religion. His court at Fatehpur Sikri became the greatest cultural center in the world, sponsoring miniature painting, poetry, music, and scholarship in Persian, Hindi, and Sanskrit.\n\n"
                "Akbar could not read or write but had a near-perfect memory and absorbed vast knowledge through listening. His religious tolerance, institutional creativity, and administrative genius made the Mughal Empire the wealthiest and most powerful state on earth during his lifetime."
            ),
            "causes": [
                "Humayun's reconquest of India restoring Mughal claim after Sur Empire interregnum",
                "Second Battle of Panipat (1556) — Bairam Khan's regency securing Akbar's throne",
                "Mughal military tradition of Timurid and Mongol cavalry warfare",
                "India's fragmented post-Sultanate political landscape enabling Mughal expansion",
            ],
            "effects": [
                "Consolidation of Mughal Empire across most of the Indian subcontinent",
                "Mansabdari administrative system — meritocratic imperial bureaucracy",
                "Abolition of jizya tax (1564) promoting religious tolerance",
                "Rajput alliances creating composite Hindu-Muslim governing class",
                "Din-i-Ilahi syncretic religious philosophy",
                "Fatehpur Sikri — architectural marvel and cultural capital",
                "Akbarnama and Ain-i-Akbari documenting Mughal governance and society",
            ],
            "relationships": [
                {"type": "OCCURS_IN", "target": "Mughal Empire", "targetSlug": "mughal-empire", "note": "Greatest Mughal Emperor"},
                {"type": "INFLUENCES", "target": "Mansabdari system", "targetSlug": "mansabdari-system", "note": "Administrative rank system he invented"},
                {"type": "INFLUENCES", "target": "Rajput kingdoms", "targetSlug": "rajput-kingdoms", "note": "Integrated Rajputs as Mughal allies through marriage"},
                {"type": "INFLUENCES", "target": "Din-i-Ilahi", "targetSlug": "din-i-ilahi", "note": "Syncretic religious philosophy he founded"},
                {"type": "INFLUENCES", "target": "Fatehpur Sikri", "targetSlug": "fatehpur-sikri", "note": "New capital city he built (1571)"},
                {"type": "INFLUENCES", "target": "Akbarnama", "targetSlug": "akbarnama", "note": "Official chronicle by Abul Fazl"},
                {"type": "INFLUENCES", "target": "Abul Fazl", "targetSlug": "abul-fazl", "note": "Court historian and close advisor"},
                {"type": "INFLUENCES", "target": "Mughal miniature painting", "targetSlug": "mughal-painting", "note": "Patronized fusion of Persian and Hindu artistic styles"},
                {"type": "OCCURS_IN", "target": "India", "targetSlug": "india", "note": "Ruled most of the Indian subcontinent"},
                {"type": "INFLUENCES", "target": "Humayun", "targetSlug": "humayun", "note": "Father and predecessor who retook India"},
                {"type": "INFLUENCES", "target": "Aurangzeb", "targetSlug": "aurangzeb", "note": "Great-grandson who reversed his religious tolerance"},
                {"type": "INFLUENCES", "target": "Birbal", "targetSlug": "birbal", "note": "Famous wit and advisor in the Navaratna council"},
                {"type": "INFLUENCES", "target": "Tansen", "targetSlug": "tansen", "note": "Greatest musician in the Navaratna — Mughal court music"},
                {"type": "INFLUENCES", "target": "Second Battle of Panipat", "targetSlug": "second-battle-of-panipat", "note": "Decisive victory securing Mughal power (1556)"},
                {"type": "INFLUENCES", "target": "Sikhism", "targetSlug": "sikhism", "note": "Granted land for Amritsar to the Sikh Guru"},
            ],
            "historicalSignificance": {
                "significanceScore": 9,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Akbar the Great built the wealthiest empire on earth and pioneered a model of multi-religious governance — religious tolerance, meritocratic bureaucracy, and cultural synthesis — that shaped South Asia's civilizational identity for centuries and still resonates in modern India."
            },
            "quote": "'A monarch should be ever intent on conquest, otherwise his neighbours rise in arms against him.' — Akbar the Great",
            "places": ["Agra, India", "Fatehpur Sikri, India", "Delhi, India", "Lahore, Pakistan"],
            "subjectHeadings": "Akbar the Great — Emperors and Rulers — India — Early Modern",
            "subjects": ["India", "Mughal Empire", "religious tolerance", "South Asia", "Islamic rule", "administration", "architecture", "Pakistan", "Persian culture", "Early Modern Asia"],
            "frameworks": ["empire-building", "religious-syncretism", "state-formation"],
        }
    },

    # ── 6. Catherine the Great ───────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/221-Class-221/221catherine-the-great.json",
        "slug": "catherine-the-great",
        "era_correction": None,
        "data": {
            "summary": (
                "Catherine the Great (1729–1796) was Empress of Russia from 1762 to 1796, the longest-reigning female ruler in Russian history, who transformed Russia into a major European power and presided over its greatest territorial expansion. Born a minor German princess (Sophie of Anhalt-Zerbst), she seized the throne in a palace coup after her husband Peter III alienated the military, and proceeded to become one of the most effective rulers of the 18th century.\n\n"
                "An ardent Enlightenment reader, Catherine corresponded with Voltaire, Diderot, and d'Alembert, positioning herself as a 'philosopher-queen' devoted to rational governance. She founded the Russian Academy of Sciences, established the first state-funded girls' school in Europe (Smolny Institute, 1764), built the Hermitage as a center of art collection, and introduced smallpox vaccination to Russia by having herself inoculated publicly.\n\n"
                "Her foreign policy was marked by dramatic expansion: Russia absorbed Crimea (1783), large portions of Poland (Three Partitions, 1772–1795), and vast territories from the Ottoman Empire. She crushed the Pugachev Rebellion (1773–1775), a massive serf uprising, and afterwards tightened serfdom — a contradiction between Enlightenment ideals and autocratic necessity that defined her reign.\n\n"
                "Her legacy is double-edged: she modernized Russia's institutions and culture while entrenching noble privilege and serf bondage. 'The Golden Age of the Russian Nobility' she presided over set the stage for 19th-century Russian literature and the eventual abolition crisis."
            ),
            "causes": [
                "Peter III's erratic rule and alienation of Russian military and nobility",
                "Palace coup of June 1762 bringing Catherine to power with Guards' support",
                "European Enlightenment providing ideological framework for reform",
                "Russian imperial ambition to expand into Black Sea and Polish territory",
            ],
            "effects": [
                "Territorial expansion: Crimea, Black Sea coast, portions of Poland",
                "Three Partitions of Poland (1772, 1793, 1795) eliminating Polish statehood",
                "Hermitage Museum — world-class art collection in St Petersburg",
                "Smolny Institute — first state-funded girls' school in Europe (1764)",
                "Russian Academy of Sciences expansion and cultural patronage",
                "Smallpox inoculation introduced to Russia by imperial example",
                "Tightening of serfdom after Pugachev Rebellion — paradox of Enlightened despotism",
            ],
            "relationships": [
                {"type": "OCCURS_IN", "target": "Russian Empire", "targetSlug": "russian-empire", "note": "Empress of Russia 1762–1796"},
                {"type": "INFLUENCES", "target": "Hermitage Museum", "targetSlug": "hermitage-museum", "note": "Founded as imperial art collection"},
                {"type": "INFLUENCES", "target": "Voltaire", "targetSlug": "voltaire", "note": "Corresponded extensively — Enlightenment intellectual exchange"},
                {"type": "INFLUENCES", "target": "Diderot", "targetSlug": "diderot", "note": "Invited him to St Petersburg; bought his library"},
                {"type": "INFLUENCES", "target": "Three Partitions of Poland", "targetSlug": "partitions-of-poland", "note": "Key architect of Poland's elimination"},
                {"type": "INFLUENCES", "target": "Crimean annexation 1783", "targetSlug": "crimea", "note": "Annexed Crimea from Ottomans (1783)"},
                {"type": "INFLUENCES", "target": "Ottoman Empire", "targetSlug": "ottoman-empire", "note": "Waged two successful Russo-Turkish wars"},
                {"type": "INFLUENCES", "target": "Pugachev Rebellion", "targetSlug": "pugachev-rebellion", "note": "Crushed 1773–1775 serf uprising"},
                {"type": "INFLUENCES", "target": "Potemkin", "targetSlug": "grigory-potemkin", "note": "Favorite statesman and military commander"},
                {"type": "INFLUENCES", "target": "Enlightened absolutism", "targetSlug": "enlightened-absolutism", "note": "Archetype of philosopher-queen"},
                {"type": "INFLUENCES", "target": "Peter the Great", "targetSlug": "peter-the-great", "note": "Model and predecessor — consciously emulated his westernization"},
                {"type": "INFLUENCES", "target": "Alexander I", "targetSlug": "alexander-i-of-russia", "note": "Grandson whom she personally educated"},
                {"type": "INFLUENCES", "target": "Smallpox vaccination", "targetSlug": "smallpox-vaccination", "note": "Publicly inoculated to promote vaccination in Russia"},
                {"type": "INFLUENCES", "target": "Russian literature Golden Age", "targetSlug": "russian-literature", "note": "Her cultural patronage laid groundwork for Pushkin's era"},
                {"type": "OCCURS_IN", "target": "St Petersburg", "targetSlug": "saint-petersburg", "note": "Capital and centre of her court"},
            ],
            "historicalSignificance": {
                "significanceScore": 8,
                "significanceCategory": "continental",
                "significanceNarrative": "Catherine the Great transformed Russia into a dominant European power, presided over its greatest territorial expansion, and modelled a fusion of Enlightenment ideals with autocratic governance that shaped Russian political culture for a century."
            },
            "quote": "'I shall be an autocrat: that's my trade. And the good Lord will forgive me: that's his.' — Catherine the Great",
            "places": ["St Petersburg, Russia", "Moscow, Russia", "Stettin, Prussia (modern Szczecin, Poland — birthplace)"],
            "subjectHeadings": "Catherine the Great — Monarchs and Rulers — Russia — Early Modern",
            "subjects": ["Russia", "Enlightenment", "empire", "European history", "women rulers", "Hermitage", "Poland", "Crimea", "Ottoman Empire", "serfdom"],
            "frameworks": ["empire-building", "enlightenment", "state-formation"],
        }
    },

    # ── 7. Archimedes ────────────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/240-Class-240/24001-archimedes.json",
        "slug": "archimedes",
        "era_correction": None,
        "data": {
            "summary": (
                "Archimedes of Syracuse (c. 287–212 BCE) was a Greek mathematician, physicist, engineer, and astronomer who stands as the greatest mathematician of antiquity and one of the greatest in all of human history. Working in Syracuse on the island of Sicily, he made foundational discoveries in geometry, hydrostatics, and mechanics that would not be surpassed for nearly two millennia.\n\n"
                "His mathematical achievements include precise approximations of pi, proofs of the areas and volumes of curved surfaces and solids (anticipating integral calculus by 1,800 years through his 'method of exhaustion'), and the discovery that a sphere inscribed in a cylinder has exactly two-thirds the volume and surface area of the cylinder. This last result he considered his greatest achievement and requested it be inscribed on his tomb.\n\n"
                "His physical discoveries include the principle of the lever ('Give me a place to stand and I will move the earth'), the principle of buoyancy (Archimedes' principle — water displaced equals weight of floating body), and the Archimedes screw for raising water. During the Roman siege of Syracuse (213–212 BCE), he designed ingenious war machines — cranes that capsized ships and burning mirrors — that held off the Roman fleet for two years.\n\n"
                "Killed by a Roman soldier during the sack of Syracuse, legend has him dying while absorbed in a geometric diagram. His works, preserved through Islamic and Byzantine transmission, directly inspired Galileo, Newton, and the birth of modern mathematical physics."
            ),
            "causes": [
                "Alexandrian mathematical tradition (Euclid, Eudoxus) providing foundational methods",
                "Syracusan court of Hiero II as patron enabling full-time research",
                "Greek philosophical tradition demanding rigorous geometric proof",
                "Practical needs of siege warfare stimulating mechanical invention",
            ],
            "effects": [
                "Method of exhaustion anticipating integral calculus (1,800 years before Newton/Leibniz)",
                "Archimedes' principle — foundation of hydrostatics",
                "Lever principle and mechanical advantage — foundation of classical mechanics",
                "Archimedes screw — still used for water and grain transport globally",
                "Pi approximated to 3.1408 < π < 3.1429 (most accurate until 15th century)",
                "War machines of Syracuse delaying Roman conquest of Sicily by two years",
                "Direct inspiration for Galileo, Newton, and mathematical physics",
            ],
            "relationships": [
                {"type": "OCCURS_IN", "target": "Syracuse, Sicily", "targetSlug": "syracuse-sicily", "note": "Birthplace and city of his work"},
                {"type": "OCCURS_IN", "target": "Ancient Greece", "targetSlug": "ancient-greece", "note": "Greek cultural context"},
                {"type": "INFLUENCES", "target": "Integral calculus", "targetSlug": "integral-calculus", "note": "Method of exhaustion anticipates calculus"},
                {"type": "INFLUENCES", "target": "Hydrostatics", "targetSlug": "hydrostatics", "note": "Archimedes' principle of buoyancy"},
                {"type": "INFLUENCES", "target": "Classical mechanics", "targetSlug": "classical-mechanics", "note": "Lever principle and mechanical advantage"},
                {"type": "INFLUENCES", "target": "Hiero II of Syracuse", "targetSlug": "hiero-ii", "note": "Royal patron and problem-poser (the crown)"},
                {"type": "INFLUENCES", "target": "Eratosthenes", "targetSlug": "eratosthenes", "note": "Corresponded in the 'Method' — mathematical dialogue"},
                {"type": "INFLUENCES", "target": "Euclid", "targetSlug": "euclid", "note": "Built on Euclidean geometry as foundation"},
                {"type": "INFLUENCES", "target": "Galileo Galilei", "targetSlug": "galileo-galilei", "note": "Directly inspired by Archimedes' methods"},
                {"type": "INFLUENCES", "target": "Isaac Newton", "targetSlug": "isaac-newton", "note": "Calculus drew on method of exhaustion"},
                {"type": "INFLUENCES", "target": "Archimedes screw", "targetSlug": "archimedes-screw", "note": "Hydraulic device still in worldwide use"},
                {"type": "OCCURS_IN", "target": "Siege of Syracuse (214–212 BCE)", "targetSlug": "siege-of-syracuse", "note": "Designed defensive war machines"},
                {"type": "INFLUENCES", "target": "Roman Republic", "targetSlug": "roman-republic", "note": "His machines resisted Roman conquest for two years"},
                {"type": "INFLUENCES", "target": "Alexandria Library", "targetSlug": "library-of-alexandria", "note": "Works archived and preserved there"},
                {"type": "INFLUENCES", "target": "Pi (mathematical constant)", "targetSlug": "pi-constant", "note": "First rigorous approximation of pi (3 10/71 to 3 1/7)"},
            ],
            "historicalSignificance": {
                "significanceScore": 10,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Archimedes was the greatest mathematician of antiquity and the founding figure of mathematical physics — his method of exhaustion anticipated calculus by 1,800 years, his principle of buoyancy underlies all fluid mechanics, and his genius directly inspired the Scientific Revolution."
            },
            "quote": "'Give me a place to stand on and I will move the earth.' — Archimedes (on the lever)",
            "places": ["Syracuse, Sicily", "Alexandria, Egypt"],
            "subjectHeadings": "Archimedes — Mathematicians and Scientists — Ancient Greece — Classical",
            "subjects": ["Greece", "Sicily", "mathematics", "physics", "geometry", "mechanics", "hydrostatics", "ancient science", "Classical era", "engineering"],
            "frameworks": ["scientific-revolution", "intellectual-history", "ancient-greece"],
        }
    },

    # ── 8. Dante Alighieri ───────────────────────────────────────────────────
    {
        "file": "data/appwrite-export/entities/260-Class-260/260dante-alighieri.json",
        "slug": "dante-alighieri",
        "era_correction": None,
        "data": {
            "summary": (
                "Dante Alighieri (1265–1321) was an Italian poet, philosopher, and political exile whose Divine Comedy is universally regarded as the greatest literary work of the Middle Ages and one of the supreme achievements of world literature. Born in Florence, he was shaped by the city's violent factional politics — the war between Black and White Guelphs — which led to his permanent exile in 1302 and the bitterness and cosmic ambition that permeates his masterpiece.\n\n"
                "The Divine Comedy (c. 1308–1321) narrates a journey through Hell (Inferno), Purgatory (Purgatorio), and Paradise (Paradiso), guided first by the Roman poet Virgil and then by his idealized beloved Beatrice. A vast synthesis of Scholastic theology, classical mythology, contemporary politics, and personal allegory, it places recognizable historical figures — popes, emperors, philosophers, and personal enemies — in eternal damnation or glory, a breathtaking act of literary judgment.\n\n"
                "Dante wrote in the Florentine Tuscan vernacular rather than Latin, a revolutionary choice that effectively created the Italian literary language and elevated the vernacular to the same dignity as classical Latin. His treatise De vulgari eloquentia argued explicitly for the literary dignity of common speech.\n\n"
                "'The father of the Italian language,' as Boccaccio called him, Dante transformed medieval literature, established the template for Italian national identity, and directly influenced Petrarch, Boccaccio, Milton, Chaucer, T.S. Eliot, and the entire tradition of visionary poetry."
            ),
            "causes": [
                "Florence's factional Guelph-Ghibelline civil war leading to his exile (1302)",
                "Scholastic philosophical tradition (Thomas Aquinas) as intellectual framework",
                "Virgil's Aeneid and Ovid's Metamorphoses as literary models",
                "Unrequited love for Beatrice Portinari as spiritual and poetic catalyst",
            ],
            "effects": [
                "Divine Comedy — summit of medieval literature and world canon",
                "Creation of the Italian literary language from Florentine Tuscan vernacular",
                "De vulgari eloquentia — first systematic argument for vernacular literary dignity",
                "Template for visionary journey literature (Milton's Paradise Lost, Blake's prophetic books)",
                "Italian national cultural identity anchored in Dante's language and vision",
                "Direct influence on Petrarch, Boccaccio, Chaucer, and European literature",
                "Standardization of literary Italian that persisted for 700 years",
            ],
            "relationships": [
                {"type": "OCCURS_IN", "target": "Florence", "targetSlug": "florence", "note": "Birthplace and source of political exile"},
                {"type": "INFLUENCES", "target": "Divine Comedy", "targetSlug": "divine-comedy", "note": "His masterwork — Inferno, Purgatorio, Paradiso"},
                {"type": "INFLUENCES", "target": "Italian language", "targetSlug": "italian-language", "note": "Father of literary Italian"},
                {"type": "INFLUENCES", "target": "Virgil", "targetSlug": "virgil", "note": "Guide through Hell and Purgatory in the Comedy"},
                {"type": "INFLUENCES", "target": "Beatrice Portinari", "targetSlug": "beatrice-portinari", "note": "Spiritual beloved and guide through Paradise"},
                {"type": "INFLUENCES", "target": "Thomas Aquinas", "targetSlug": "thomas-aquinas", "note": "Thomistic theology structures the Comedy's cosmology"},
                {"type": "INFLUENCES", "target": "Petrarch", "targetSlug": "petrarch", "note": "Successor and Italian literary tradition founder"},
                {"type": "INFLUENCES", "target": "Boccaccio", "targetSlug": "boccaccio", "note": "Wrote first Dante biography; called him 'il poeta'"},
                {"type": "INFLUENCES", "target": "Geoffrey Chaucer", "targetSlug": "geoffrey-chaucer", "note": "Directly influenced by Dante's vernacular model"},
                {"type": "INFLUENCES", "target": "John Milton", "targetSlug": "john-milton", "note": "Paradise Lost draws on Dante's cosmological framework"},
                {"type": "INFLUENCES", "target": "T.S. Eliot", "targetSlug": "t-s-eliot", "note": "Called Dante the most universal of poets"},
                {"type": "OCCURS_IN", "target": "Guelph-Ghibelline conflicts", "targetSlug": "guelph-ghibelline", "note": "Political context of exile that produced the Comedy"},
                {"type": "INFLUENCES", "target": "Renaissance humanism", "targetSlug": "renaissance-humanism", "note": "Vernacular elevation prepared ground for Renaissance"},
                {"type": "INFLUENCES", "target": "Catholic theology", "targetSlug": "catholic-theology", "note": "Comedy is the greatest artistic expression of medieval Catholicism"},
                {"type": "OCCURS_IN", "target": "Ravenna", "targetSlug": "ravenna", "note": "City of exile where he died and is buried"},
            ],
            "historicalSignificance": {
                "significanceScore": 10,
                "significanceCategory": "world-changing",
                "significanceNarrative": "Dante created the Italian language, wrote the greatest work of medieval literature, and produced a synthesis of Christian theology, classical learning, and contemporary politics so vast and precise that he is called simply 'the Supreme Poet' — his influence on Western literature has been continuous for 700 years."
            },
            "quote": "'Abandon all hope, ye who enter here.' — Dante Alighieri, Inferno, Canto III",
            "places": ["Florence, Italy", "Ravenna, Italy (exile and death)", "Verona, Italy (exile)"],
            "subjectHeadings": "Dante Alighieri — Poets and Writers — Italy — Medieval",
            "subjects": ["Italy", "poetry", "Italian language", "Medieval literature", "Divine Comedy", "Inferno", "Florence", "theology", "exile", "vernacular literature"],
            "frameworks": ["literary-history", "religious-thought", "intellectual-history"],
        }
    },
]

# ── Core writer ──────────────────────────────────────────────────────────────

def enrich_entity(file_path, slug, data, era_correction, dry_run=False):
    if not os.path.exists(file_path):
        return f"FILE NOT FOUND: {file_path}"

    with open(file_path, "r", encoding="utf-8") as f:
        doc = json.load(f)

    entities = doc.get("entities", [])
    target = next((e for e in entities if e.get("slug") == slug), None)
    if not target:
        return f"SLUG NOT FOUND: {slug} in {file_path}"

    current_summary = (target.get("detailsJson") or {}).get("summary", "")
    new_summary = data["summary"]

    if len(current_summary) >= SKIP_THRESHOLD:
        return f"SKIP {slug} (already {len(current_summary)}c)"

    if dry_run:
        return f"→ Enriching {slug}  (was {len(current_summary)}c → {len(new_summary)}c)"

    # Apply enrichment
    if "detailsJson" not in target or target["detailsJson"] is None:
        target["detailsJson"] = {}

    dj = target["detailsJson"]
    now = datetime.now(timezone.utc).isoformat()

    # Build edit log entries
    edit_log = dj.get("_editLog", [])
    for field in ["summary", "causes", "effects", "relationships", "historicalSignificance",
                  "quote", "places", "subjectHeadings", "subjects", "frameworks"]:
        if field in data:
            old_val = dj.get(field, None)
            new_val = data[field]
            if old_val != new_val:
                edit_log.append({
                    "field": field,
                    "oldValue": old_val,
                    "newValue": new_val if len(str(new_val)) < 200 else str(new_val)[:200] + "…",
                    "editorId": EDITOR_ID,
                    "sessionId": SESSION_ID,
                    "timestamp": now,
                })

    # Write new field values
    for field, value in data.items():
        dj[field] = value

    dj["_editLog"] = edit_log

    # Era correction
    if era_correction:
        target["era"] = era_correction

    # Mark for sync
    target["_unsyncedEdits"] = True

    # Write back
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)

    return f"✓ Saved {file_path}"


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    if DRY_RUN:
        print("=== DRY RUN — no files will be written ===\n")

    print(f"Batch 58 enrichment — {len(ENRICHMENTS)} entities\n")

    enriched, skipped, failed = 0, 0, 0
    for item in ENRICHMENTS:
        slug = item["slug"]
        print(f"[{slug}]")
        result = enrich_entity(
            item["file"], slug, item["data"],
            item.get("era_correction"), dry_run=DRY_RUN
        )
        print(f"  {result}")
        if "SKIP" in result:
            skipped += 1
        elif result.startswith("✓") or result.startswith("→"):
            enriched += 1
        else:
            failed += 1
            print(f"  ERROR: {result}")

    tag = "DRY RUN" if DRY_RUN else "DONE"
    print(f"\n{tag}: {enriched} enriched, {skipped} skipped, {failed} failed")
    if not DRY_RUN and enriched > 0:
        print("\nNext step: env $(cat .env | xargs) npx tsx scripts/sync_gateway.ts --local")


if __name__ == "__main__":
    main()
