#!/usr/bin/env python3
"""
Batch 45 — 8 entities (Class 362): Famous Historic Libraries
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()
FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/362-Class-362"
FILE_PREFIX = "362"


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
    print(f"  \u2713 {entity['name']} \u2014 sum={slen}c c={len(det.get('causes', []))} e={len(det.get('effects', []))}")


ENTITIES = [

    ("bodleian-library", {
        "summary": (
            "The Bodleian Library (est. 1602, Oxford — the main research library of the University of Oxford, refounded and expanded by Sir Thomas Bodley after the medieval Duke Humphrey's Library) is one of the oldest and most important libraries in Europe — holding 13+ million printed items, 80,000+ manuscripts, and constituting one of six legal deposit libraries in the United Kingdom, entitled to receive a copy of every book published in Britain. The Bodleian's Duke Humphrey's Library (1488) — with its chained books, medieval ceiling, and atmospheric reading alcoves — is one of the most recognisable academic spaces in the world, having served as Hogwarts Library in the Harry Potter films.\n\n"
            "The library traces its origins to Duke Humphrey of Gloucester's donation of 281 manuscripts to the University of Oxford in 1444 — creating the first significant academic library collection in England. The library was stripped and effectively destroyed during the Reformation (the books sold or burned as 'superstitious'), and refounded by Sir Thomas Bodley (1602), a diplomat who invested his personal fortune and devoted the last 17 years of his life to creating a library that would be 'a common Benefit to all Strangers and Subjects.' Bodley's Gentleman's Agreement with the Stationers' Company (1610) — requiring a copy of every book registered to be sent to the Bodleian — was the prototype for legal deposit.\n\n"
            "The Bodleian's collections include the Magna Carta (one of four surviving originals), the Gutenberg Bible, Shakespeare's First Folio (multiple copies), and the first edition of Newton's Principia Mathematica — making it simultaneously one of the world's greatest research libraries and one of the world's most important archives of Western civilisation."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "One of oldest and most important libraries in Europe (est. 1602, Oxford, Sir Thomas Bodley); 13+ million printed items, 80,000+ manuscripts; one of six UK legal deposit libraries; Duke Humphrey's Library (1488) — Hogwarts Library in Harry Potter; Magna Carta (one of four originals), Gutenberg Bible, Shakespeare's First Folio, Newton's Principia; Bodley's Gentleman's Agreement with Stationers' Company (1610) — prototype for legal deposit; stripped during Reformation, refounded 1602; 'common benefit to all strangers and subjects'.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Duke Humphrey of Gloucester's donation of 281 manuscripts (1444) — the first significant academic library collection in England — established the institutional basis that was stripped during the Reformation and later refounded by Bodley",
            "Sir Thomas Bodley's decision to invest his personal fortune and diplomatic connections in refounding the Oxford library (1598–1602) — driven by his conviction that England needed a great university library comparable to those of the Italian Renaissance — created the Bodleian as a permanent institution with both royal patronage and legal deposit rights",
            "Bodley's Gentleman's Agreement with the Stationers' Company (1610) — requiring a copy of every registered book to be deposited — was the prototype for the legal deposit system that eventually became statutory (1710 Copyright Act), making the Bodleian one of the world's earliest copyright deposit libraries"
        ],
        "effects": [
            "The Bodleian's legal deposit status — extended to statutory requirement by the Copyright Act (1710) and its successors — means that the library has received a copy of virtually every book published in Britain for 400 years, creating the most comprehensive archive of British printed culture in existence",
            "The Bodleian's role as a research resource for Oxford scholars — from Francis Bacon and John Locke to T.S. Eliot and J.R.R. Tolkien — has made it the institutional context for a significant proportion of the greatest works of English literature, science, and scholarship of the past four centuries",
            "The Bodleian's digitisation programme — making millions of its rare manuscripts and printed books available online — has democratised access to materials previously available only to scholars who could travel to Oxford, fundamentally changing the research landscape for humanities scholars worldwide",
            "Duke Humphrey's Library's use as the Hogwarts Library set in the Harry Potter films — reaching a global audience of hundreds of millions — has made it one of the most recognised academic spaces in the world, demonstrating how cultural reuse can transform a medieval library into a global landmark"
        ],
        "relationships": [
            {"entity": "Sir Thomas Bodley (1598–1602 refounding, personal fortune invested)", "relationship": "REFOUNDED_AND_ENDOWED_BY", "note": "Bodley's personal investment and diplomatic connections created the Bodleian as a permanent institution — his Gentleman's Agreement with the Stationers' Company was the prototype for legal deposit"},
            {"entity": "Stationers' Company Gentleman's Agreement (1610, prototype legal deposit)", "relationship": "LEGAL_DEPOSIT_RIGHTS_ESTABLISHED_BY_THE", "note": "Bodley's 1610 agreement requiring a copy of every registered book was the prototype for statutory copyright deposit — making the Bodleian one of the world's earliest copyright libraries"},
            {"entity": "Magna Carta (one of four surviving originals held at Bodleian)", "relationship": "CUSTODIAN_OF_ONE_OF_THE_FOUR_SURVIVING_ORIGINALS_OF_THE", "note": "The Bodleian holds one of the four surviving original Magna Carta manuscripts, making it a custodian of one of the most consequential constitutional documents in history"},
            {"entity": "Harry Potter films (Hogwarts Library set in Duke Humphrey's Library)", "relationship": "ARCHITECTURE_GLOBALLY_RECOGNISED_AS_THE_FICTIONAL_HOGWARTS_LIBRARY_THROUGH_THE", "note": "Duke Humphrey's Library's use as the Harry Potter Hogwarts Library has made it one of the world's most recognised academic spaces"},
            {"entity": "Duke Humphrey of Gloucester (1444 manuscript donation, library origins)", "relationship": "INSTITUTIONAL_ORIGINS_IN_THE_MANUSCRIPT_DONATION_OF", "note": "Duke Humphrey's 1444 donation of 281 manuscripts — the first significant academic library collection in England — established the institutional precursor to the Bodleian"}
        ],
    }),

    ("house-of-wisdom", {
        "summary": (
            "The House of Wisdom (Bayt al-Hikma — est. c. 830 CE, Baghdad, under Caliph Al-Ma'mun of the Abbasid Caliphate) was the greatest intellectual institution of the medieval Islamic world — the translation and research centre that preserved and transmitted Greek, Persian, and Indian knowledge to the Islamic world and eventually to medieval Europe, and the institutional home of the Islamic Golden Age's most significant scientific and mathematical achievements. The House of Wisdom's translation movement — converting Greek philosophical, scientific, and medical texts into Arabic — was the most consequential act of knowledge transfer in the history of civilisation before the printing press.\n\n"
            "The House of Wisdom was established under Caliph Harun al-Rashid (c. 790 CE) and significantly expanded under Al-Ma'mun (r. 813–833 CE), who sent expeditions to Byzantium to collect Greek manuscripts and hired the greatest translators of the age — Hunayn ibn Ishaq, the Banu Musa brothers, Al-Kindi — to translate Aristotle, Plato, Euclid, Archimedes, Ptolemy, and Galen into Arabic. Al-Ma'mun's support was motivated by both intellectual conviction and political calculation — Islamic learning's superiority over Byzantine Christianity was a tool of ideological competition.\n\n"
            "The House of Wisdom's scholars produced original contributions beyond translation: Al-Khwarizmi developed algebra (al-jabr) and introduced the Hindu-Arabic numeral system to the Islamic world; Al-Kindi developed cryptanalysis; Al-Biruni pioneered comparative religion; Ibn al-Haytham (working later, in Cairo) developed optics. The Mongol destruction of Baghdad (1258) — when the Tigris reportedly ran black with ink from the destroyed manuscripts — ended the House of Wisdom and the Abbasid Caliphate simultaneously."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Greatest intellectual institution of medieval Islamic world (est. c. 830 CE, Baghdad, Caliph Al-Ma'mun, Abbasid Caliphate); most consequential knowledge transfer in history before printing press; Greek, Persian, Indian texts translated into Arabic; Al-Khwarizmi (algebra, Hindu-Arabic numerals), Al-Kindi (cryptanalysis), Hunayn ibn Ishaq (medicine), Banu Musa brothers, Al-Biruni; Mongol destruction of Baghdad (1258) — 'Tigris ran black with ink'; institutional home of Islamic Golden Age; Greek philosophy/science preserved and transmitted to medieval Europe.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Abbasid Caliphate's intellectual policy — particularly under Al-Ma'mun, who made the acquisition and translation of Greek scientific texts a state priority — created the institutional and financial support for the translation movement, driven by both intellectual enthusiasm and the political desire to demonstrate Islamic civilisation's superiority",
            "The availability of Greek manuscripts in Byzantine libraries and in the libraries of Eastern Christian scholars — particularly the Syriac-speaking translators who could work directly from Greek and had kept Greek learning alive in the centuries after the fall of Rome — provided the raw material that the House of Wisdom's scholars translated into Arabic",
            "The Islamic world's commercial and bureaucratic need for practical mathematics, astronomy, and medicine — creating demand for the Greek scientific and mathematical heritage — drove the translation movement's priority on practical disciplines alongside philosophical texts"
        ],
        "effects": [
            "The House of Wisdom's translation movement — preserving and developing Greek philosophy, mathematics, and science in Arabic when much of Europe had lost direct access to the Greek originals — created the Arabic scholarly corpus that was retranslated into Latin in the 12th-century Renaissance of the Western universities (Toledo, Sicily), transmitting Greek learning to medieval European scholarship",
            "Al-Khwarizmi's algebra (al-jabr wa al-muqabala, c. 820 CE) — developed at the House of Wisdom — is the founding text of modern algebra, with the word 'algebra' derived from al-jabr and the word 'algorithm' derived from Al-Khwarizmi's name, making the House of Wisdom the institutional origin of two foundational concepts in modern mathematics and computing",
            "The Mongol destruction of the House of Wisdom and Baghdad (1258) — with the reported destruction of hundreds of thousands of manuscripts in the Tigris — was one of the most catastrophic losses of knowledge in history, ending the Islamic Golden Age and permanently depriving scholarship of texts that have never been recovered",
            "The House of Wisdom's model — a state-supported institution combining translation, original research, and the collection of manuscripts from multiple civilisations — became the conceptual template for later intellectual institutions: the libraries of Renaissance Florence, the European royal academies, and ultimately the modern research university"
        ],
        "relationships": [
            {"entity": "Caliph Al-Ma'mun (r. 813–833 CE, institutional expansion, translation policy)", "relationship": "MOST_SIGNIFICANT_INSTITUTIONAL_PATRON_AND_DEVELOPER_WAS", "note": "Al-Ma'mun's state support for the translation of Greek texts — and his expeditions to Byzantium for manuscripts — created the institutional conditions for the Islamic Golden Age"},
            {"entity": "Al-Khwarizmi (algebra, Hindu-Arabic numerals, 'algorithm' etymology)", "relationship": "INSTITUTIONAL_HOME_OF_THE_FOUNDING_WORK_OF_MODERN_ALGEBRA_AND_MATHEMATICAL_COMPUTING_BY", "note": "Al-Khwarizmi's algebra — developed at the House of Wisdom — is the founding text of modern algebra, with 'algebra' and 'algorithm' both derived from his work"},
            {"entity": "Mongol destruction of Baghdad (1258, 'Tigris ran black with ink')", "relationship": "DESTROYED_BY_THE", "note": "The Mongol sack of Baghdad — reportedly turning the Tigris black with manuscript ink — ended the House of Wisdom and the Abbasid Caliphate simultaneously, destroying one of history's greatest knowledge repositories"},
            {"entity": "12th-century Latin translation movement (Toledo, Sicily, Greek texts retransmitted to Europe)", "relationship": "SOURCE_OF_THE_ARABIC_SCHOLARLY_CORPUS_RETRANSLATED_INTO_LATIN_IN_THE", "note": "The House of Wisdom's Arabic translations were retranslated into Latin in 12th-century Toledo and Sicily, transmitting Greek learning to medieval European scholarship"},
            {"entity": "Hunayn ibn Ishaq (chief translator, medicine, philosophy, Galen)", "relationship": "GREATEST_TRANSLATOR_AND_CHIEF_SCHOLAR_WAS", "note": "Hunayn ibn Ishaq's translations of Galen, Aristotle, and Hippocrates into Arabic were the primary vehicle for Greek medical and philosophical knowledge entering the Islamic world"}
        ],
    }),

    ("bodleian-library", {
        "summary": ("DUPLICATE_PLACEHOLDER"), "importanceScore": 1,
        "historicalSignificance": {"significanceScore": 1, "significanceNarrative": "placeholder", "significanceCategory": "local"},
        "causes": [], "effects": [], "relationships": [],
    }),

    ("beinecke-rare-book-manuscript-library", {
        "summary": (
            "The Beinecke Rare Book and Manuscript Library (est. 1963, Yale University, New Haven, Connecticut — designed by Gordon Bunshaft of Skidmore, Owings & Merrill) is the world's largest library building dedicated entirely to rare books and manuscripts — holding 1 million+ volumes, 500,000+ manuscript pages, and some of the most significant rare books in existence: the Gutenberg Bible, the Vinland Map (disputed), Thomas More's handwritten copy of Utopia, and the Voynich Manuscript (the world's most extensively studied and still undeciphered medieval codex). The building itself — translucent marble panels over a steel frame, with no external windows — is one of the masterpieces of mid-century modernist architecture.\n\n"
            "The Beinecke was founded by a gift from the Beinecke family (Edwin, Frederick, and Walter Beinecke) to Yale University, and opened in 1963. Gordon Bunshaft's design — a six-story underground stack surrounded by a four-story above-ground cube of translucent marble panels that filter light to protect rare materials — is the primary example of how modernist architecture adapted to the conservation needs of rare book collections, replacing traditional skylights with a light-diffusing system that eliminates ultraviolet radiation.\n\n"
            "The Beinecke's Gutenberg Bible (c. 1455) — one of 48 known surviving copies of the world's first printed book — and its Voynich Manuscript (c. 1404–1438, 240 pages of unidentified script and botanical illustrations never deciphered despite decades of cryptanalysis) have made it simultaneously one of the most important research libraries and one of the most publicly recognisable through the enduring mystery of the undeciphered codex."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "World's largest library dedicated entirely to rare books and manuscripts (est. 1963, Yale, Gordon Bunshaft design); 1M+ volumes, 500,000+ manuscript pages; Gutenberg Bible (one of 48 known copies), Voynich Manuscript (most extensively studied undeciphered medieval codex), Thomas More's Utopia in his handwriting; translucent marble panels — no external windows, UV-filtering light; mid-century modernist architecture masterpiece; Beinecke family gift to Yale 1963.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Yale University's recognition that its growing rare book collections required a purpose-built conservation environment — with controlled temperature, humidity, and light levels — drove the decision to commission a dedicated rare book library building rather than continuing to store rare materials in the regular library stacks",
            "The Beinecke family's philanthropic commitment to Yale — Edwin, Frederick, and Walter Beinecke's gift providing the funding for both building and collections — created the institutional and financial basis for what became the world's largest dedicated rare book library",
            "Gordon Bunshaft's architectural innovation — the translucent marble panel solution for filtered natural light without UV radiation — solved the fundamental conservation challenge of rare book libraries (light access vs. preservation) in a way that became the model for subsequent special collections buildings"
        ],
        "effects": [
            "The Beinecke's concentration of rare books and manuscripts — providing scholars with access to primary sources from across the history of Western learning — has made it one of the most important centres for humanities research in the United States, attracting scholars who need access to materials unavailable elsewhere",
            "The Voynich Manuscript's presence at the Beinecke — and the library's digitisation of the entire codex for free online access — has made it the most publicly engaged rare book library in the world, with millions of people attempting decipherment as a global intellectual puzzle, demonstrating how open access to digitised rare materials can transform public engagement with scholarship",
            "Gordon Bunshaft's Beinecke design — which has been widely recognised as one of the finest American library buildings of the 20th century — became the architectural template for subsequent rare book libraries, demonstrating how conservation requirements can drive architectural innovation",
            "The Beinecke's acquisition policy — systematically collecting the primary sources of American and European literary history — has assembled collections that support research in areas from the Harlem Renaissance to Medieval European literature, making Yale's Beinecke one of the primary institutions for literary and historical scholarship"
        ],
        "relationships": [
            {"entity": "Voynich Manuscript (most extensively studied undeciphered medieval codex)", "relationship": "PRIMARY_CUSTODIAN_AND_DIGITISER_OF_THE", "note": "The Beinecke's digitisation of the Voynich Manuscript has made it the most publicly engaged rare book in history, with millions attempting decipherment worldwide"},
            {"entity": "Gutenberg Bible (c. 1455, one of 48 known copies, world's first printed book)", "relationship": "CUSTODIAN_OF_ONE_OF_THE_48_KNOWN_COPIES_OF_THE", "note": "The Beinecke's Gutenberg Bible — one of 48 known copies of the world's first printed book — is the most significant item in its collection"},
            {"entity": "Gordon Bunshaft / Skidmore Owings Merrill (1963 building design, translucent marble)", "relationship": "ARCHITECTURAL_MASTERPIECE_DESIGNED_BY", "note": "Bunshaft's translucent marble panel design — filtering UV radiation without eliminating natural light — is the defining architectural solution for rare book conservation"},
            {"entity": "Yale University (institutional home, Beinecke family gift)", "relationship": "INSTITUTION_OF_WHICH_IT_IS_THE_RARE_BOOK_LIBRARY_AT", "note": "Yale's rare book needs — and the Beinecke family's philanthropic gift — created the world's largest dedicated rare book library"},
            {"entity": "Thomas More's Utopia manuscript (handwritten copy)", "relationship": "CUSTODIAN_OF_THE_AUTHOR'S_HANDWRITTEN_COPY_OF", "note": "The Beinecke's possession of Thomas More's handwritten Utopia manuscript makes it a custodian of the primary physical trace of one of the most influential political texts in Western history"}
        ],
    }),

    ("biblioteca-medicea-laurenziana", {
        "summary": (
            "The Biblioteca Medicea Laurenziana (Laurentian Library, est. 1571, Florence — founded by the Medici family, designed by Michelangelo, housing the most important collection of Greek and Latin manuscripts ever assembled) is the world's most architecturally significant library building and one of the most consequential repositories of classical manuscripts in existence. The library holds 11,000+ manuscripts — including the oldest manuscript of Virgil's works, the oldest manuscript of Tacitus, and extensive Greek philosophical, mathematical, and literary manuscripts — and Michelangelo's vestibule and reading room (1524–1568) is one of the masterpieces of Italian Mannerist architecture.\n\n"
            "The Laurentian Library was founded on the Medici collection assembled by Cosimo de' Medici and Lorenzo de' Medici (the Magnificent) — the most important private book collection of the Renaissance — through the purchase of Greek manuscripts brought to Italy by Byzantine scholars fleeing the Ottoman conquest of Constantinople (1453). The collection was originally open to scholars at the Medici palace, became public in 1571 under Cosimo I de' Medici, and was installed in the purpose-built Michelangelo building at San Lorenzo.\n\n"
            "Michelangelo's vestibule design — with the extraordinary carved staircase (the final design executed by Bartolomeo Ammannati from Michelangelo's clay model), the architectural deployment of columns recessed into the walls (used structurally without support), and the reading room's pietra serena floor and ceiling — is the foundational text of Mannerist architecture and the most significant piece of Renaissance architectural innovation."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's most architecturally significant library (est. 1571, Florence, Medici family, Michelangelo design); 11,000+ manuscripts; oldest manuscript of Virgil, oldest manuscript of Tacitus, extensive Greek philosophical/mathematical manuscripts; Medici collection assembled via Byzantine scholars fleeing Ottoman conquest of Constantinople (1453); Cosimo and Lorenzo de' Medici (the Magnificent) collectors; Michelangelo's vestibule and staircase — foundational text of Mannerist architecture; opened to public 1571 under Cosimo I.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Ottoman conquest of Constantinople (1453) — which drove Greek scholars and their manuscripts westward to Italy — provided the Medici family with the opportunity to acquire the largest collection of Greek manuscripts ever assembled in private hands, creating the core of the Laurentian Library's Greek manuscript holdings",
            "The Medici family's patronage of Renaissance humanism — Cosimo de' Medici's founding of the Platonic Academy and Lorenzo de' Medici's systematic collection of classical manuscripts — created the intellectual and political motivation for building the greatest Renaissance library, as a demonstration of Florentine cultural leadership",
            "Pope Clement VII's commission of Michelangelo (1523) to design the new library building at San Lorenzo — connecting the library to the Medici family's dynastic mausoleum — created the architectural opportunity that produced the Mannerist masterpiece"
        ],
        "effects": [
            "The Laurentian Library's Greek manuscripts — including texts that would otherwise have been lost — provided Renaissance scholars with direct access to Plato, Aristotle, Euclid, Archimedes, and other Greek authors, contributing to the Renaissance's transformation of European intellectual life and the development of humanism",
            "Michelangelo's vestibule — with its columns used purely decoratively (embedded in the walls without structural load), its complex wall articulation, and the extraordinary carved staircase — created the architectural vocabulary of Mannerism, influencing all subsequent Italian and European architecture through its demonstration that classical elements could be used in non-classical ways",
            "The library's founding model — a private collection made public, in a purpose-built architectural setting that treated the library building as a work of art — became the template for subsequent great libraries, from the Bodleian to the Bibliothèque nationale de France, establishing the library as both a scholarly resource and a cultural monument",
            "The oldest manuscript of Tacitus's Annals (held at the Laurentian) — which is the primary source for the history of the Julio-Claudian emperors — means that much of what historians know about the reigns of Tiberius, Caligula, Claudius, and Nero depends on the survival of this single manuscript in the Medici collection"
        ],
        "relationships": [
            {"entity": "Lorenzo de' Medici 'the Magnificent' (primary manuscript collector)", "relationship": "COLLECTIONS_ASSEMBLED_PRIMARILY_THROUGH_THE_PATRONAGE_OF", "note": "Lorenzo's systematic collection of classical manuscripts — enabled by the Byzantine scholars' westward migration after 1453 — created the Laurentian Library's intellectual core"},
            {"entity": "Michelangelo (vestibule and staircase design, Mannerist architecture masterpiece)", "relationship": "ARCHITECTURAL_DESIGN_OF_VESTIBULE_AND_READING_ROOM_BY", "note": "Michelangelo's vestibule — with its Mannerist column treatment and extraordinary staircase — is the foundational text of Mannerist architecture"},
            {"entity": "Ottoman conquest of Constantinople (1453, Byzantine scholars west, manuscript migration)", "relationship": "COLLECTION_OF_GREEK_MANUSCRIPTS_ASSEMBLED_THROUGH_THE_WESTWARD_MIGRATION_FOLLOWING_THE", "note": "The 1453 Ottoman conquest drove Byzantine scholars with Greek manuscripts to Italy — providing the Medici with the greatest collection of Greek manuscripts ever assembled in private hands"},
            {"entity": "Tacitus Annals (oldest manuscript at Laurentian, primary source for Julio-Claudian history)", "relationship": "CUSTODIAN_OF_THE_OLDEST_SURVIVING_MANUSCRIPT_OF", "note": "The Laurentian holds the oldest Tacitus manuscript — making it the custodian of the primary source for the history of Tiberius, Caligula, Claudius, and Nero"},
            {"entity": "Platonic Academy Florence (Cosimo de' Medici, Renaissance humanism context)", "relationship": "LIBRARY_COMPONENT_OF_THE_MEDICI_CULTURAL_PROGRAMME_THAT_INCLUDED_THE", "note": "The Laurentian Library and the Platonic Academy were complementary components of the Medici cultural programme that drove the Florentine Renaissance"}
        ],
    }),

    ("bibliotheca-corviniana", {
        "summary": (
            "The Bibliotheca Corviniana (est. c. 1460s–1490, Buda — the royal library of King Matthias Corvinus of Hungary, established at the Royal Palace of Buda and regarded as the second most important library in 15th-century Europe after the Vatican Library) was the finest Renaissance library outside Italy — holding 2,000–3,000 illuminated manuscripts in the most extensive collection of illuminated Corvini codices in the world, assembled by Matthias from the greatest scriptoria of Florence and the Italian humanist centres. The Bibliotheca Corviniana is a UNESCO Memory of the World (inscribed 2005).\n\n"
            "The library was assembled by King Matthias Corvinus (r. 1458–1490) — the most powerful Renaissance monarch north of the Alps, whose court at Buda was the primary centre for Renaissance humanism outside Italy — through purchases from the Florentine book trade (particularly the Vespasiano da Bisticci workshop), gifts from Pope Sixtus IV, and the work of the Florentine illuminator Attavante degli Attavanti, who produced some of the finest illuminated manuscripts in the collection.\n\n"
            "The library's dispersal after Matthias's death (1490) — when the books were seized by the Ottoman conquest of Buda (1526) and distributed to Istanbul, Vienna, and other European centres — is one of the most consequential dispersals of a Renaissance library. The surviving Corvini codices (approximately 220 identified worldwide) are held in 47 institutions across 13 countries, making the Bibliotheca Corviniana the most globally dispersed of all great Renaissance libraries."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Finest Renaissance library outside Italy (est. 1460s–1490, Buda, King Matthias Corvinus of Hungary); 2,000–3,000 illuminated manuscripts; UNESCO Memory of the World (2005); second most important 15th-century European library after Vatican; Vespasiano da Bisticci workshop (Florence), Attavante degli Attavanti illuminations; primary Renaissance humanism centre north of Alps; dispersal after 1490 death and 1526 Ottoman conquest of Buda; 220 surviving Corvini codices in 47 institutions across 13 countries — most globally dispersed Renaissance library.",
            "significanceCategory": "continental"
        },
        "causes": [
            "King Matthias Corvinus's ambition to establish the most magnificent Renaissance court north of the Alps — competing with the Italian city-states for cultural prestige and the status of enlightened Renaissance monarchy — drove the systematic acquisition of illuminated manuscripts from Florence's finest workshops",
            "The Florentine book trade's commercial infrastructure — particularly Vespasiano da Bisticci's workshop, which supplied books to Federico da Montefeltro, Pope Nicholas V, and Cosimo de' Medici as well as Matthias — provided the supply chain for assembling a major Renaissance library far from Italy's manuscript production centres",
            "Matthias's political relationship with Pope Sixtus IV and his military reputation (the victories against the Ottoman Empire that earned the epithet 'Corvinus' and gave the library its name) created the diplomatic network through which manuscripts and scholars flowed to Buda"
        ],
        "effects": [
            "The Bibliotheca Corviniana's role as the primary transmission point for Renaissance humanism into Central Europe — bringing Florentine humanism, classical scholarship, and illuminated manuscript culture to Hungary, Bohemia, Poland, and the Holy Roman Empire — made it the institutional vehicle for the spread of the Italian Renaissance beyond the Alps",
            "The Ottoman conquest of Buda (1526) and the dispersal of the Corvini codices to Istanbul, Vienna, and across Europe — while destroying the institutional unity of the library — paradoxically preserved more manuscripts than if they had remained in a single vulnerable location, with surviving codices in 47 institutions providing evidence of Renaissance manuscript culture across Europe",
            "The UNESCO inscription of the Bibliotheca Corviniana (2005) — as a Memory of the World for the scattered manuscripts rather than a single physical collection — established a new model for recognising dispersed historical collections as unified cultural heritage, with implications for other scattered manuscript and archival collections worldwide",
            "Matthias Corvinus's library model — a Renaissance monarch investing systematically in manuscript culture as a tool of political legitimacy and cultural prestige — influenced subsequent Central European rulers' cultural programmes, helping to establish the tradition of royal and aristocratic library patronage in the region"
        ],
        "relationships": [
            {"entity": "King Matthias Corvinus (r. 1458–1490, founder, most powerful Renaissance monarch north of Alps)", "relationship": "ESTABLISHED_AND_DEFINED_BY_THE_PATRONAGE_OF", "note": "Matthias's ambition to establish the most magnificent Renaissance court north of the Alps drove the systematic acquisition of illuminated manuscripts from Florence's finest workshops"},
            {"entity": "Vespasiano da Bisticci (Florentine book workshop, primary manuscript supplier)", "relationship": "MANUSCRIPTS_PRIMARILY_SUPPLIED_THROUGH_THE_WORKSHOP_OF", "note": "Bisticci's workshop — which also supplied Federico da Montefeltro and Cosimo de' Medici — was the primary commercial vehicle for assembling the Corvini collection"},
            {"entity": "Ottoman conquest of Buda (1526, dispersal of Corvini codices to Istanbul, Vienna)", "relationship": "INSTITUTIONAL_COHERENCE_DESTROYED_BY_THE", "note": "The 1526 Ottoman conquest's dispersal of the Corvini codices to Istanbul, Vienna, and elsewhere made the Bibliotheca Corviniana the most globally dispersed Renaissance library"},
            {"entity": "UNESCO Memory of the World (2005, scattered manuscripts as unified heritage)", "relationship": "INSCRIBED_AS_A", "note": "The UNESCO inscription — for scattered manuscripts in 47 institutions across 13 countries — established a new model for recognising dispersed historical collections as unified cultural heritage"},
            {"entity": "Attavante degli Attavanti (Florence, finest illuminated manuscripts in collection)", "relationship": "FINEST_ILLUMINATED_MANUSCRIPTS_PRODUCED_BY_THE_FLORENTINE_ARTIST", "note": "Attavante's illuminated Corvini codices — among the finest illuminated manuscripts of the Italian Renaissance — define the aesthetic standard of the collection"}
        ],
    }),

    ("biblioteca-joanina", {
        "summary": (
            "The Biblioteca Joanina (est. 1724, University of Coimbra, Portugal — built on the orders of King John V of Portugal and named in his honour) is one of the most spectacular Baroque library buildings in the world — a three-story hall library with gilded woodwork, trompe-l'oeil painted ceilings, and elaborately decorated bookcases that has been described as the most beautiful library in the world. The library holds 250,000+ volumes from the 16th–18th centuries, and its architecture — Chinese-influenced lacquered wood, ornate gilded carvings, and the extraordinary painted vault — represents the apex of Portuguese Baroque decorative arts.\n\n"
            "King John V commissioned the library as part of his programme of transforming the University of Coimbra — Portugal's oldest and most important university (founded 1290) — into a world-class institution comparable to the great European universities. The library was built 1717–1728 in the former Paço das Escolas (Palace of Schools), with three interconnected rooms of progressively greater decorative richness, the innermost room — the Sala Grande — being one of the most elaborately decorated interior spaces in Portugal.\n\n"
            "The Biblioteca Joanina is famous not only for its architectural beauty but for its resident colony of bats — which emerge at dusk to eat the insects that would otherwise damage the books, protected by the library staff as a form of natural conservation. The bats sleep in the library's bat boxes during the day and protect the collection at night, creating one of the most unusual conservation partnerships in the history of libraries."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "One of world's most spectacular Baroque library buildings (est. 1724, University of Coimbra Portugal, King John V); three-story hall library; gilded woodwork, trompe-l'oeil ceilings, Chinese-influenced lacquered bookcases; 250,000+ volumes (16th–18th centuries); described as 'world's most beautiful library'; University of Coimbra (founded 1290, Portugal's oldest university); resident bat colony — natural conservation; apex of Portuguese Baroque decorative arts; part of UNESCO World Heritage Site (University of Coimbra, 2013).",
            "significanceCategory": "continental"
        },
        "causes": [
            "King John V's cultural programme — transforming the University of Coimbra into a world-class institution to match Portugal's wealth from Brazilian gold and diamond exports — drove the commission of a library building that would demonstrate Portuguese cultural achievement at the height of Portuguese colonial wealth",
            "The University of Coimbra's institutional needs — holding the expanding collections of scientific, legal, and humanist texts acquired through Portugal's position as a major power in the Age of Exploration — required a purpose-built library of sufficient size and quality to house and protect the collections",
            "The Portuguese Baroque decorative tradition — combining Chinese lacquerwork (reflecting Portugal's trade relationships with Asia) with European Baroque woodworking and gilding — provided the aesthetic vocabulary for the Joanina's extraordinary interior, which synthesises the global reach of Portugal's empire with the European courtly tradition"
        ],
        "effects": [
            "The Biblioteca Joanina's architectural model — a three-story hall library with progressively more elaborate decorative treatment, combining Chinese lacquerwork with European Baroque gilding — influenced subsequent Baroque library designs across Europe and became the most recognised example of the Baroque hall library tradition",
            "The library's bat colony — protected as natural conservation agents that eat paper-damaging insects — has become both a genuine conservation practice and one of the most widely reported unusual library facts, making the Joanina one of the most publicly recognisable libraries in the world through its combination of architectural beauty and natural history",
            "The University of Coimbra's UNESCO World Heritage inscription (2013) — which included the Biblioteca Joanina — recognised the library as part of a broader architectural and intellectual heritage that makes the Alta Universitária one of Portugal's most significant cultural landscapes",
            "The Joanina's 250,000 volumes from the 16th–18th centuries — including significant holdings on the Age of Exploration, natural history, and early modern science — make it one of the most important primary source collections for the history of Portugal's imperial and scientific achievements"
        ],
        "relationships": [
            {"entity": "King John V of Portugal (patron, Brazilian gold wealth, cultural programme)", "relationship": "COMMISSIONED_AND_NAMED_AFTER", "note": "John V's cultural programme — funded by Brazilian gold and diamond exports — drove the commission of the library as a demonstration of Portuguese cultural achievement"},
            {"entity": "University of Coimbra (founded 1290, Portugal's oldest university, UNESCO WHS 2013)", "relationship": "LIBRARY_OF_AND_COMPONENT_OF_THE_UNESCO_WHS_OF_THE", "note": "The Joanina — part of the University of Coimbra's UNESCO World Heritage Site — serves Portugal's oldest and most important university"},
            {"entity": "Resident bat colony (natural conservation, paper-insect predation)", "relationship": "PROTECTED_BY_A_RESIDENT_BAT_COLONY_THAT_PROVIDES_NATURAL_CONSERVATION_OF_THE", "note": "The Joanina's protected bat colony — eating paper-damaging insects at night — is one of the most unusual conservation practices in library history"},
            {"entity": "Portuguese Baroque decorative arts (Chinese lacquerwork, gilding, global empire aesthetic)", "relationship": "APEX_EXAMPLE_OF_THE", "note": "The Joanina's combination of Chinese lacquerwork and European Baroque gilding — reflecting Portugal's global trade connections — is the apex of Portuguese Baroque decorative arts"},
            {"entity": "Brazilian gold exports (18th-century wealth funding John V's cultural programme)", "relationship": "CONSTRUCTION_FUNDED_BY_THE_WEALTH_FROM", "note": "The Brazilian gold and diamond exports that made John V one of Europe's wealthiest monarchs funded the Joanina's extraordinary decorative programme"}
        ],
    }),

    ("library-of-trinity-college-dublin", {
        "summary": (
            "The Library of Trinity College Dublin (est. 1592, Dublin — the library of Trinity College Dublin, Ireland's oldest university, and a legal deposit library for publications in the UK and Ireland) is home to the Book of Kells (c. 800 CE) — the most elaborately decorated manuscript of the four Gospels in existence and the most-visited artefact in Ireland, attracting 500,000+ visitors annually — and the Long Room (built 1712–1732), one of the world's most magnificent library reading rooms and the inspiration for the library interior in the Star Wars films. The library holds 6 million+ items including 500,000+ books printed before 1900.\n\n"
            "Trinity College Dublin was founded in 1592 by Queen Elizabeth I — the only constituent college of the proposed University of Dublin (which never received its second college), making it both the founding college and the university itself. The library's legal deposit rights (dating from 1801) entitle it to receive a copy of every book published in Britain and Ireland — a right that has made its collection one of the most comprehensive archives of Irish and British printed culture.\n\n"
            "The Book of Kells — created around 800 CE by Columban monks, probably at Iona and brought to Kells for safekeeping during Viking raids — is the most elaborately decorated Insular manuscript in existence, with 680 vellum pages of Latin Gospels decorated with extraordinary interlace patterns, zoomorphic designs, and miniature portraits. The Book of Kells's miniature of the 'Chi Rho' page — the opening of St Matthew's account of the nativity — is considered the most detailed and complex single page of any medieval manuscript."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Ireland's oldest university library (est. 1592, Dublin, Queen Elizabeth I); home of the Book of Kells (c. 800 CE — most elaborately decorated Gospel manuscript, 500,000+ visitors/year); Long Room (1712–1732, inspiration for Star Wars library set); 6 million+ items, 500,000+ pre-1900 books; legal deposit rights (1801) for UK and Ireland; Book of Kells Chi Rho page — most detailed and complex single page of any medieval manuscript; Columban monks, Iona origins, Viking raids; only constituent college of University of Dublin.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Queen Elizabeth I's founding of Trinity College Dublin (1592) — as part of the Protestant Reformation's educational strategy in Ireland, providing a Protestant university to train the Irish clergy and professional class — created the institutional home for what would become Ireland's most important library",
            "The Columban monks' creation of the Book of Kells (c. 800 CE) — and its transfer from the monastery of Iona to Kells for safekeeping during the Viking raids of the 9th century — preserved one of the greatest works of medieval art, which eventually came to Trinity College Dublin as the most important item in its collections",
            "The Library's legal deposit rights (1801, confirmed and extended by the Copyright Act) — entitling it to receive a copy of every book published in Britain and Ireland — created the ongoing acquisition mechanism that has made it one of the most comprehensive archives of printed culture in the British Isles"
        ],
        "effects": [
            "The Book of Kells's permanent loan to Trinity College Dublin — and its display in the Old Library's 'Turning Darkness into Light' exhibition — has made the library the most visited cultural site in Ireland, with 500,000+ visitors annually, generating significant economic activity for Dublin and making the Book of Kells Ireland's most important cultural tourism asset",
            "The Long Room's iconic interior — barrel-vaulted ceiling, marble busts of scholars, and 200,000+ of the library's oldest volumes lining the shelves — has become one of the most recognisable library interiors in the world through its use as the inspiration for the Jedi Archives in the Star Wars films, reaching a global audience of billions",
            "Trinity College Dublin's role as the repository of Irish national memory — holding the 1916 Proclamation of the Irish Republic, the oldest surviving Irish manuscript (Lebor na hUidre, c. 1100 CE), and the comprehensive collection of Irish literary archives — makes it the primary institutional custodian of Irish cultural and political heritage",
            "The Library's digitisation of the Book of Kells — making high-resolution images of all 680 pages available online — has transformed scholarly access to one of the world's greatest medieval manuscripts, enabling textual and art-historical analysis that was impossible when physical access was required"
        ],
        "relationships": [
            {"entity": "Book of Kells (c. 800 CE, most elaborately decorated Gospel manuscript)", "relationship": "PRIMARY_CUSTODIAN_AND_DISPLAY_INSTITUTION_OF_THE", "note": "The Book of Kells — Ireland's most visited cultural artefact, 500,000+ visitors/year — is the defining item in Trinity College Dublin's library"},
            {"entity": "Long Room (1712–1732, Star Wars Jedi Archives inspiration)", "relationship": "CONTAINS_THE_ICONIC_READING_ROOM_RECOGNISED_GLOBALLY_AS_THE_INSPIRATION_FOR_THE", "note": "The Long Room's use as the inspiration for the Star Wars Jedi Archives has made it one of the world's most recognisable library interiors"},
            {"entity": "Queen Elizabeth I (Trinity College Dublin founder, 1592, Protestant educational strategy)", "relationship": "INSTITUTIONAL_FOUNDATION_ESTABLISHED_BY", "note": "Elizabeth I's 1592 founding of Trinity — as part of Protestant educational strategy in Ireland — created the institutional home for the Book of Kells and Ireland's most important library"},
            {"entity": "Columban monks / Iona monastery (Book of Kells creators, Viking raid context)", "relationship": "MOST_PRECIOUS_COLLECTION_ITEM_CREATED_BY", "note": "The Columban monks' creation of the Book of Kells at Iona and its transfer to Kells during Viking raids preserved one of the greatest works of medieval art"},
            {"entity": "1916 Proclamation of the Irish Republic (held at Trinity, Irish national memory)", "relationship": "CUSTODIAN_OF_THE_FOUNDATIONAL_DOCUMENT_OF_THE_MODERN_IRISH_STATE", "note": "Trinity holds the 1916 Proclamation — making it a custodian of both Ireland's oldest manuscripts and its modern founding document"}
        ],
    }),

    ("national-library-of-finland", {
        "summary": (
            "The National Library of Finland (Kansalliskirjasto — est. 1640 as the Library of the Royal Academy of Turku, becoming the national library with Finland's independence in 1917; located in Helsinki, housed in a neoclassical building designed by Carl Ludwig Engel and completed 1844) is the oldest and largest scientific library in Finland — holding 3 million+ items including the most extensive collection of materials published in Finland from the 17th century to the present, the primary national archives of Finnish printed culture, and significant medieval manuscript collections including the Codex Abboensis (c. 1335) — Finland's oldest surviving codex.\n\n"
            "The library's origins in the Royal Academy of Turku (founded 1640 — Finland's first university under Swedish rule) gave it the same legal deposit status that shaped the Bodleian and the British Library, ensuring it received a copy of every book published in the Swedish realm. When Finland became a Russian Grand Duchy (1809) and the capital moved from Turku to Helsinki (1828), the library followed — installed in the new neoclassical capital's finest public building, Carl Ludwig Engel's magnificent domed reading hall, which remains one of the finest examples of Finnish Empire-style architecture.\n\n"
            "The National Library of Finland became an independent institution within the University of Helsinki in 2006, and its digitisation programme — making Finnish newspapers, journals, and books freely available through the National Digital Library — has made Finland one of the world's leaders in open-access digitisation of national printed heritage. The library's Fennica database is the definitive national bibliography of Finland."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Oldest and largest scientific library in Finland (est. 1640, Royal Academy of Turku; national library from 1917 independence); Carl Ludwig Engel neoclassical building (1844, Helsinki, Empire-style domed reading hall); 3M+ items; Codex Abboensis (c. 1335 — Finland's oldest codex); Finnish printed culture from 17th century; legal deposit rights from Swedish Royal Academy period; Russian Grand Duchy period (1809) — capital move Turku to Helsinki (1828); Fennica national bibliography; leading open-access digitisation of national printed heritage.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The founding of the Royal Academy of Turku (1640) — the first university in Finland under Swedish rule — created the institutional home for the library that would become the national library, with legal deposit rights ensuring the systematic collection of Finnish printed culture from the earliest period of printing in the region",
            "Finland's transition from Swedish to Russian rule (1809) and the establishment of Helsinki as the new capital (1812) — followed by the relocation of the university and library from Turku to Helsinki (1828) — created both the institutional continuity and the architectural opportunity for Carl Ludwig Engel's neoclassical library building",
            "Finnish independence (1917) and the creation of the Finnish national state — requiring a national library to curate and preserve Finland's cultural heritage — transformed the university library into a national institution, creating the mandate for comprehensive collection and preservation of Finnish printed culture"
        ],
        "effects": [
            "The National Library of Finland's comprehensive collection of Finnish printed culture — from the first Finnish-language printed books of the 16th century to contemporary digital publications — provides the primary archive for the development of Finnish language, literature, and intellectual life, making it the foundation of Finnish cultural heritage scholarship",
            "Finland's open-access digitisation programme — one of the world's most advanced national digitisation initiatives — has made millions of items of Finnish printed heritage freely available online, positioning Finland as a global model for open-access national library digitisation and establishing the principle that national printed heritage should be freely accessible to all citizens",
            "Carl Ludwig Engel's neoclassical library building — part of his comprehensive design of Helsinki's Senate Square, which defined the architectural character of the Finnish capital — made the library a permanent component of one of the finest examples of 19th-century neoclassical urban planning in Europe",
            "The library's Fennica database — the definitive national bibliography of Finland — provides the authoritative catalogue of all Finnish publications, serving as the foundational reference tool for Finnish scholarship, publishing, and cultural heritage documentation"
        ],
        "relationships": [
            {"entity": "Royal Academy of Turku (1640, first Finnish university, library origins)", "relationship": "INSTITUTIONAL_ORIGINS_IN_THE_LIBRARY_OF_THE", "note": "The library's founding in the Royal Academy of Turku (1640) — with legal deposit rights under Swedish rule — created the institutional foundation of Finland's national library"},
            {"entity": "Carl Ludwig Engel (neoclassical building design, 1844, Helsinki Senate Square)", "relationship": "HOUSED_IN_A_NEOCLASSICAL_BUILDING_DESIGNED_BY", "note": "Engel's neoclassical building — part of his comprehensive design of Helsinki's Senate Square — made the library a landmark of Finnish imperial architecture"},
            {"entity": "Finnish independence (1917, transformation from university to national library)", "relationship": "TRANSFORMED_INTO_A_NATIONAL_INSTITUTION_BY", "note": "Finnish independence created the mandate for a national library to curate Finland's cultural heritage — transforming the university library into a national institution"},
            {"entity": "National Digital Library of Finland (open-access digitisation, global model)", "relationship": "PRIMARY_SOURCE_INSTITUTION_OF_THE", "note": "Finland's open-access digitisation programme — one of the world's most advanced — has positioned the National Library as a global model for national printed heritage accessibility"},
            {"entity": "Codex Abboensis (c. 1335, Finland's oldest surviving codex)", "relationship": "CUSTODIAN_OF_FINLAND'S_OLDEST_SURVIVING_CODEX", "note": "The Codex Abboensis — Finland's oldest surviving manuscript — is the most historically significant item in the National Library's medieval holdings"}
        ],
    }),

]

# Remove the duplicate placeholder entry
ENTITIES = [(s, d) for s, d in ENTITIES if d.get("summary") != "DUPLICATE_PLACEHOLDER"]

if __name__ == "__main__":
    print(f"Batch 45 — {len(ENTITIES)} entities (Class 362: Famous Historic Libraries)")
    for slug, data in ENTITIES:
        print(f"\n\u2192 {slug}")
        enrich_entity(slug, data)
    print("\n\u2713 Done")
