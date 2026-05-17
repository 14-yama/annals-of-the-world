"""
Batch 67e: Create Early Modern era entities referenced by James Ussher.
- joseph-scaliger (Person, Class 205) — classical scholar whose chronology Ussher built on
- westminster-assembly (Institution, Class 350) — Puritan assembly Ussher engaged with
- republic-of-letters (Movement, Class 631) — the learned correspondence network
- james-i-of-england (Person, Class 205) — king who commissioned the KJV; Ussher's patron
- council-of-nicaea (EventWindow, Class 524) — ecumenical council defining Christian orthodoxy
"""
import json
import os
import datetime

NOW = datetime.datetime.utcnow().isoformat() + "+00:00"
EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-67-may2026"
BASE = os.path.join(os.path.dirname(__file__), "..", "data", "appwrite-export", "entities")


def make_entity_file(class_code: str, slug: str, name: str, label: str, era: str,
                     call_number: str, details: dict) -> dict:
    details.setdefault("sessionId", SESSION_ID)
    details.setdefault("enrichedBy", EDITOR_ID)
    details.setdefault("enrichedAt", NOW)
    if "_editLog" not in details:
        details["_editLog"] = []
    return {
        "_meta": {
            "classCode": class_code,
            "exportedAt": NOW,
            "source": "local-bot"
        },
        "entities": [{
            "slug": slug,
            "name": name,
            "label": label,
            "era": era,
            "callNumber": call_number,
            "_unsyncedEdits": True,
            "detailsJson": json.dumps(details, ensure_ascii=False)
        }]
    }


def save(class_code: str, filename: str, data: dict):
    dir_name = f"{class_code}-Class-{class_code}"
    dir_path = os.path.join(BASE, dir_name)
    os.makedirs(dir_path, exist_ok=True)
    path = os.path.join(dir_path, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  Saved: {path}")
    return path


# =============================================================================
# 1. JOSEPH SCALIGER
# =============================================================================
scaliger_details = {
    "summary": (
        "Joseph Justus Scaliger (1540–1609) was a Franco-Italian classical scholar and the founding father of "
        "modern historical chronology. Born in Agen, France, the son of the polymath Julius Caesar Scaliger, he "
        "mastered dozens of ancient languages including Hebrew, Arabic, Aramaic, Persian, and Ethiopian, enabling "
        "him to read primary sources across civilizations. His two works — De Emendatione Temporum (1583) and "
        "Thesaurus Temporum (1606) — revolutionized the dating of ancient history by synchronizing the calendrical "
        "systems of Greece, Rome, Egypt, Mesopotamia, and the Hebrew Bible.\n\n"
        "Scaliger's most lasting technical contribution was the Julian Period — a 7,980-year astronomical cycle "
        "beginning on January 1, 4713 BCE, created by multiplying the 28-year solar cycle, the 19-year Metonic "
        "cycle, and the 15-year indiction cycle. This Julian Day Number system is still used by astronomers and "
        "historians today for unambiguous date calculation. He was the first scholar to establish that Greek, Roman, "
        "and Near Eastern histories were part of a single synchronized timeline.\n\n"
        "James Ussher explicitly built on Scaliger's chronological method when constructing his own Annales Veteris "
        "Testamenti (1650). Both scholars worked within the same Calvinist scholarly network — the Republic of "
        "Letters — and shared the conviction that sacred history could be precisely dated through astronomical and "
        "philological rigor. Scaliger spent his last years as a professor at Leiden, where he attracted students "
        "from across Protestant Europe.\n\n"
        "'The greatest scholar in the world since the revival of learning.' — Isaac Casaubon on Scaliger"
    ),
    "causes": [
        "Training under his father Julius Caesar Scaliger in classical philology",
        "Huguenot connections giving him access to Protestant scholarly networks across Europe",
        "Mastery of Semitic languages opening Babylonian, Hebrew, and Egyptian chronological sources"
    ],
    "effects": [
        "Invention of the Julian Period — still used in astronomy for date calculation",
        "Synchronization of Greek, Roman, and Near Eastern chronologies into a single timeline",
        "Provided the methodological foundation that James Ussher used in the Annales Veteris Testamenti",
        "Established Leiden as the centre of philological scholarship in Protestant Europe"
    ],
    "relationships": [
        {"verb": "INFLUENCES", "targetSlug": "james-ussher", "targetName": "James Ussher",
         "context": "Ussher explicitly adopted Scaliger's chronological methods and Julian Period for the Annales"},
        {"verb": "INFLUENCES", "targetSlug": "republic-of-letters", "targetName": "Republic of Letters",
         "context": "Central figure in the pan-European scholarly correspondence network"},
        {"verb": "OCCURS_IN", "targetSlug": "leiden", "targetName": "Leiden",
         "context": "Professor at Leiden University 1593–1609"},
        {"verb": "OCCURS_DURING", "targetSlug": "early-modern-1500-1800", "targetName": "Early Modern Era",
         "context": "Active 1540–1609 during the peak of Renaissance philology and Reformation scholarship"},
        {"verb": "AUTHORS", "targetSlug": "de-emendatione-temporum", "targetName": "De Emendatione Temporum",
         "context": "1583 masterwork establishing universal chronology"},
        {"verb": "ENABLES", "targetSlug": "annales-veteris-testamenti", "targetName": "Annales Veteris Testamenti",
         "context": "Scaliger's methodology was the direct intellectual precursor to Ussher's Annales"}
    ],
    "texts": [
        {
            "title": "De Emendatione Temporum",
            "slug": "de-emendatione-temporum",
            "type": "scholarly",
            "year": "1583",
            "description": "Revolutionary work synchronizing ancient chronologies; introduced the Julian Period"
        },
        {
            "title": "Thesaurus Temporum",
            "slug": "thesaurus-temporum",
            "type": "scholarly",
            "year": "1606",
            "description": "Compilation and reconstruction of ancient chronological evidence"
        }
    ],
    "evidence": [
        {
            "tier": "A",
            "source": "De Emendatione Temporum (1583), Joseph Scaliger",
            "note": "Primary source establishing his chronological method and the Julian Period",
            "citationStyle": "title"
        },
        {
            "tier": "B",
            "source": "Anthony Grafton, Joseph Scaliger: A Study in the History of Classical Scholarship (1983)",
            "note": "Definitive modern scholarly biography of Scaliger",
            "citationStyle": "page"
        }
    ],
    "timeline": [
        {"year": "1540", "event": "Born in Agen, France, son of Julius Caesar Scaliger"},
        {"year": "1570s", "event": "Mastered Hebrew, Aramaic, Syriac, Arabic enabling access to Near Eastern chronologies"},
        {"year": "1583", "event": "Published De Emendatione Temporum — first synchronized universal chronology"},
        {"year": "1593", "event": "Appointed professor extraordinarius at Leiden University"},
        {"year": "1606", "event": "Published Thesaurus Temporum — reconstruction of ancient calendrical evidence"},
        {"year": "1609", "event": "Died in Leiden; his legacy directly shaped Ussher's Annales (1650)"}
    ],
    "places": [
        {"name": "Agen", "type": "birthplace"},
        {"name": "Leiden", "type": "place of work"}
    ],
    "quote": "The greatest scholar in the world since the revival of learning. — Isaac Casaubon on Scaliger",
    "frameworks": ["intellectual-history", "chronology", "philology", "scientific-revolution"],
    "historicalSignificance": {
        "significanceScore": 7,
        "significanceNarrative": "Scaliger invented the science of historical chronology — the framework that allows historians to place events from different ancient civilizations on a single timeline. His Julian Period is still used by astronomers today. Without Scaliger, Ussher's biblical chronology would have had no rigorous methodological foundation.",
        "significanceCategory": "continental"
    }
}
scaliger_data = make_entity_file("205", "joseph-scaliger", "Joseph Scaliger",
                                  "Person", "Early Modern", "205.joseph-scaliger", scaliger_details)
save("205", "205joseph-scaliger.json", scaliger_data)
print("Created joseph-scaliger: OK")


# =============================================================================
# 2. WESTMINSTER ASSEMBLY
# =============================================================================
westminster_assembly_details = {
    "summary": (
        "The Westminster Assembly (1643–1649) was a convocation of English, Scottish, and Irish theologians and "
        "parliamentarians convened by the Long Parliament during the English Civil War to restructure the Church of "
        "England along Reformed (Calvinist) lines. Meeting in Westminster Abbey's Jerusalem Chamber, it produced "
        "the most influential documents in English-speaking Presbyterianism: the Westminster Confession of Faith "
        "(1646), the Larger and Shorter Catechisms (1647), and the Directory for Public Worship (1645).\n\n"
        "The assembly had 121 English clergymen and 30 parliamentary laymen, supplemented by Scottish commissioners "
        "under the Solemn League and Covenant. James Ussher, Archbishop of Armagh, was invited but did not attend; "
        "however, his influence is visible throughout — the assembly's approach to church governance drew on "
        "Ussher's 'reduced episcopacy' proposals, and the Westminster Confession's theological structure aligns "
        "closely with Ussher's A Body of Divinity (1645).\n\n"
        "The Westminster Standards became the doctrinal foundation of Presbyterian churches worldwide, adopted by "
        "the Church of Scotland (1647) and later Presbyterian denominations across the United States (1789), "
        "Australia, Korea, and beyond. They remain the subordinate standard of the Church of Scotland today, "
        "representing the high-water mark of English Reformed theology.\n\n"
        "The assembly is a defining monument of the Puritan era — a moment when theology, politics, and military "
        "conflict intersected to produce documents still in use four centuries later."
    ),
    "causes": [
        "Long Parliament's need to define Reformed doctrine amid Civil War with Charles I",
        "Solemn League and Covenant (1643) requiring Presbyterian church governance in exchange for Scottish military aid",
        "Puritan dissatisfaction with the Elizabethan settlement and its episcopal structures"
    ],
    "effects": [
        "Westminster Confession of Faith (1646) — the defining creed of world Presbyterianism",
        "Westminster Shorter Catechism — still memorized by Presbyterian children worldwide",
        "Directory for Public Worship replacing the Book of Common Prayer in Scotland and Puritan England",
        "Doctrinal foundation for Presbyterian churches across the United States, Korea, Australia, and Africa"
    ],
    "relationships": [
        {"verb": "INFLUENCES", "targetSlug": "james-ussher", "targetName": "James Ussher",
         "context": "Ussher invited but did not attend; his reduced episcopacy proposal influenced assembly debate"},
        {"verb": "INFLUENCES", "targetSlug": "westminster-confession-of-faith", "targetName": "Westminster Confession",
         "context": "Produced the Westminster Confession as its primary doctrinal document"},
        {"verb": "INFLUENCES", "targetSlug": "protestant-reformation", "targetName": "Protestant Reformation",
         "context": "Represents the high point of English Reformed theology within the broader Reformation"},
        {"verb": "OCCURS_IN", "targetSlug": "london", "targetName": "London",
         "context": "Met in Westminster Abbey's Jerusalem Chamber, London, 1643–1649"},
        {"verb": "OCCURS_DURING", "targetSlug": "early-modern-1500-1800", "targetName": "Early Modern Era",
         "context": "Convened 1643–1649 during the English Civil War"}
    ],
    "texts": [
        {
            "title": "Westminster Confession of Faith",
            "slug": "westminster-confession-of-faith",
            "type": "confession",
            "year": "1646",
            "description": "Primary doctrinal document of the Westminster Assembly; still in use by Presbyterian denominations"
        },
        {
            "title": "Westminster Shorter Catechism",
            "slug": "westminster-shorter-catechism",
            "type": "catechism",
            "year": "1647",
            "description": "107-question catechism opening with 'What is the chief end of man?'"
        }
    ],
    "evidence": [
        {
            "tier": "A",
            "source": "Westminster Assembly Minutes (1643–1649), Dr. Williams' Library, London",
            "note": "Primary manuscript record of the assembly's proceedings",
            "citationStyle": "archive"
        },
        {
            "tier": "C",
            "source": "Robert Letham, The Westminster Assembly (2009)",
            "note": "Comprehensive modern scholarly history of the assembly",
            "citationStyle": "page"
        }
    ],
    "timeline": [
        {"year": "1643", "event": "Long Parliament convenes the Westminster Assembly; Solemn League and Covenant signed"},
        {"year": "1644", "event": "Scottish commissioners join; assembly restructured along Presbyterian lines"},
        {"year": "1645", "event": "Directory for Public Worship published; replaces Book of Common Prayer"},
        {"year": "1646", "event": "Westminster Confession of Faith approved by assembly"},
        {"year": "1647", "event": "Westminster Catechisms approved; Church of Scotland adopts the Confession"},
        {"year": "1649", "event": "Assembly's last formal session; Cromwellian government installed"}
    ],
    "places": [
        {"name": "London", "type": "location"},
        {"name": "Westminster", "type": "meeting place"}
    ],
    "frameworks": ["institutional-history", "reformation", "theology", "political-history"],
    "historicalSignificance": {
        "significanceScore": 7,
        "significanceNarrative": "The Westminster Assembly produced doctrinal standards that have governed Presbyterian worship and theology across five continents for nearly 400 years. The Westminster Confession is arguably the most influential Reformed confessional document in history, still binding on the Church of Scotland and dozens of Presbyterian denominations worldwide.",
        "significanceCategory": "continental"
    }
}
westminster_assembly_data = make_entity_file("350", "westminster-assembly", "Westminster Assembly",
                                              "Institution", "Early Modern", "350.westminster-assembly",
                                              westminster_assembly_details)
save("350", "350westminster-assembly.json", westminster_assembly_data)
print("Created westminster-assembly: OK")


# =============================================================================
# 3. REPUBLIC OF LETTERS
# =============================================================================
republic_details = {
    "summary": (
        "The Republic of Letters (Respublica Literaria) was an informal, trans-European intellectual community "
        "of scholars, scientists, theologians, and artists active from approximately the 1400s through the 1700s, "
        "bound together by correspondence in Latin. Transcending religious and national divisions, it created "
        "the world's first truly international knowledge-exchange network — a pre-digital internet of ideas. "
        "At its height, a single letter from Paris could be copied and circulated to scholars in Amsterdam, "
        "Florence, Prague, Istanbul, and London within months.\n\n"
        "Its central figures included Erasmus (its 'prince'), Scaliger, Grotius, Leibniz, Newton, Spinoza, "
        "Voltaire, and Locke. The network was maintained through book exchanges, manuscript loans, scholarly "
        "visits, and above all letters — thousands of which survive in European archives. James Ussher was "
        "an active correspondent within this network, sending and receiving letters on biblical chronology, "
        "patristics, and manuscript evidence with scholars across Protestant Europe.\n\n"
        "The Republic of Letters enabled the Scientific Revolution and the Enlightenment by providing a "
        "mechanism for rapid peer criticism and idea diffusion that no single nation or institution could "
        "provide. It dissolved natural philosophy into an international project, creating the conditions "
        "for Copernicus, Galileo, Kepler, and Newton to build incrementally on each other's work regardless "
        "of borders or confession.\n\n"
        "The Republic of Letters had no president, no secretary, no fixed address — only the shared "
        "commitment to learned correspondence and the exchange of ideas."
    ),
    "causes": [
        "Print culture (Gutenberg press, 1450s) enabling rapid reproduction and distribution of ideas",
        "Latin as a shared scholarly language transcending national boundaries",
        "Reformation fracturing of the Church, making pan-confessional intellectual exchange necessary"
    ],
    "effects": [
        "Enabled the Scientific Revolution by creating an international mechanism for rapid peer criticism",
        "Fostered the Enlightenment through networks connecting Voltaire, Locke, Leibniz, and Newton",
        "James Ussher's Annales Veteris Testamenti was circulated through this network for validation",
        "Pre-figured modern academic peer review and scientific journals"
    ],
    "relationships": [
        {"verb": "INFLUENCES", "targetSlug": "james-ussher", "targetName": "James Ussher",
         "context": "Ussher was an active participant; his Annales circulated widely through the network"},
        {"verb": "INFLUENCES", "targetSlug": "joseph-scaliger", "targetName": "Joseph Scaliger",
         "context": "Scaliger was a central node; Leiden under his influence became a hub of the Republic of Letters"},
        {"verb": "INFLUENCES", "targetSlug": "scientific-revolution", "targetName": "Scientific Revolution",
         "context": "The Republic of Letters provided the knowledge infrastructure that enabled the Scientific Revolution"},
        {"verb": "OCCURS_DURING", "targetSlug": "early-modern-1500-1800", "targetName": "Early Modern Era",
         "context": "Flourished c. 1400s–1700s; the defining intellectual network of early modernity"}
    ],
    "texts": [
        {
            "title": "Erasmus Correspondence",
            "slug": "erasmus-correspondence",
            "type": "correspondence",
            "year": "c. 1500–1536",
            "description": "Erasmus maintained over 3,000 letters with scholars across Europe — the backbone of the early Republic"
        }
    ],
    "evidence": [
        {
            "tier": "C",
            "source": "Anne Goldgar, Impolite Learning: Conduct and Community in the Republic of Letters (1995)",
            "note": "Definitive scholarly study of the Republic of Letters network and social norms",
            "citationStyle": "page"
        },
        {
            "tier": "C",
            "source": "Dena Goodman, The Republic of Letters: A Cultural History of the French Enlightenment (1994)",
            "note": "Analysis of the later, French-language phase of the network",
            "citationStyle": "page"
        }
    ],
    "timeline": [
        {"year": "c. 1400s", "event": "Humanist scholars begin systematic correspondence; Petrarch as forerunner"},
        {"year": "c. 1516", "event": "Erasmus publishes letters widely — becomes 'prince of the Republic of Letters'"},
        {"year": "c. 1580–1650", "event": "Peak phase: Scaliger, Grotius, Ussher, Mersenne, Peiresc at center of network"},
        {"year": "c. 1660", "event": "Formal scientific academies (Royal Society 1660, Académie des Sciences 1666) begin replacing letter networks"},
        {"year": "c. 1750", "event": "French philosophes repurpose the network for Enlightenment propaganda"},
        {"year": "c. 1800", "event": "National universities and journals replace the informal correspondence network"}
    ],
    "places": [
        {"name": "Leiden", "type": "hub (Scaliger, Grotius)"},
        {"name": "Paris", "type": "hub (Mersenne, later philosophes)"},
        {"name": "London", "type": "hub (Bacon, later Newton)"}
    ],
    "frameworks": ["intellectual-history", "knowledge-networks", "print-culture", "scientific-revolution"],
    "historicalSignificance": {
        "significanceScore": 8,
        "significanceNarrative": "The Republic of Letters was the infrastructure of early modern knowledge production — the mechanism by which the Renaissance, Reformation, Scientific Revolution, and Enlightenment ideas propagated across Europe. Without it, the collaborative intellectual breakthroughs of the 16th–18th centuries would have been slower, more fragmented, and more easily suppressed.",
        "significanceCategory": "continental"
    }
}
republic_data = make_entity_file("631", "republic-of-letters", "Republic of Letters",
                                  "Movement", "Early Modern", "631.republic-of-letters", republic_details)
save("631", "631republic-of-letters.json", republic_data)
print("Created republic-of-letters: OK")


# =============================================================================
# 4. JAMES I OF ENGLAND
# =============================================================================
james_i_details = {
    "summary": (
        "James VI of Scotland and I of England (1566–1625) was the first monarch to rule both England and Scotland, "
        "uniting the two crowns in 1603 upon the death of Elizabeth I. Son of Mary Queen of Scots, he was raised "
        "Presbyterian in Scotland before inheriting England's Anglican church, navigating between Calvinist theology "
        "and episcopal church governance for the rest of his reign. He was also the target of the Gunpowder Plot "
        "(1605), in which Catholic conspirators attempted to assassinate him and Parliament.\n\n"
        "James's most enduring legacy is the King James Bible (1611) — commissioned at the Hampton Court Conference "
        "(1604) in response to Puritan demands for a new translation. The result, produced by 54 scholars across "
        "seven panels, became the most read book in the English language and the standard of English prose for "
        "three centuries. James also commissioned James Ussher as Archbishop of Armagh (1625, technically his son "
        "Charles I completed the appointment) and used Ussher's Irish Articles (1615) as a model for English "
        "religious policy.\n\n"
        "James was a prolific writer — his Daemonologie (1597), The True Law of Free Monarchies (1598), and "
        "Basilikon Doron (1599) set out his theories of divine right kingship, witch trials, and the education of "
        "princes. His assertion that 'kings are not bound to give account of their actions but to God alone' set "
        "the ideological fault line that would lead to the English Civil War under his son Charles I.\n\n"
        "'No bishop, no king.' — James I's famous epigram at the Hampton Court Conference (1604)"
    ),
    "causes": [
        "Accession to Scottish throne as James VI in 1567 after Mary Queen of Scots' abdication",
        "Death of Elizabeth I in 1603 without heirs — James the closest Protestant heir",
        "Hampton Court Conference (1604) bringing Puritan demands for church reform to his attention"
    ],
    "effects": [
        "King James Bible (1611) — the most published book in history; standard of English prose for three centuries",
        "Union of the Crowns (1603) creating the political foundation for the Kingdom of Great Britain",
        "Gunpowder Plot (1605) hardening anti-Catholic sentiment and Protestant identity in England",
        "Divine right theory setting the ideological foundations for the English Civil War",
        "James Ussher elevated to Archbishop of Armagh with royal patronage"
    ],
    "relationships": [
        {"verb": "INFLUENCES", "targetSlug": "james-ussher", "targetName": "James Ussher",
         "context": "Patronized Ussher; the Irish Articles (1615) shaped by his interest in Calvinist theology"},
        {"verb": "ENABLES", "targetSlug": "king-james-bible", "targetName": "King James Bible",
         "context": "Commissioned the King James Bible at the Hampton Court Conference 1604"},
        {"verb": "INFLUENCES", "targetSlug": "protestant-reformation", "targetName": "Protestant Reformation",
         "context": "His KJV and church policies extended the Reformation settlement in England"},
        {"verb": "OCCURS_IN", "targetSlug": "london", "targetName": "London",
         "context": "Court of St James's; Hampton Court; Westminster"},
        {"verb": "OCCURS_DURING", "targetSlug": "early-modern-1500-1800", "targetName": "Early Modern Era",
         "context": "Reigned 1603–1625"}
    ],
    "texts": [
        {
            "title": "King James Bible",
            "slug": "king-james-bible",
            "type": "bible-translation",
            "year": "1611",
            "description": "Commissioned by James I; the most influential English translation of the Bible"
        },
        {
            "title": "Basilikon Doron",
            "slug": "basilikon-doron",
            "type": "political-treatise",
            "year": "1599",
            "description": "James's manual on the art of kingship, written for his son Prince Henry"
        }
    ],
    "evidence": [
        {
            "tier": "B",
            "source": "David Harris Willson, King James VI and I (1956)",
            "note": "Standard scholarly biography of James I",
            "citationStyle": "page"
        },
        {
            "tier": "B",
            "source": "Hampton Court Conference Minutes (1604), State Papers Domestic",
            "note": "Primary record of the conference commissioning the King James Bible",
            "citationStyle": "archive"
        }
    ],
    "timeline": [
        {"year": "1566", "event": "Born at Edinburgh Castle; son of Mary Queen of Scots"},
        {"year": "1567", "event": "Crowned James VI of Scotland after mother's forced abdication"},
        {"year": "1597", "event": "Published Daemonologie and supervised North Berwick witch trials"},
        {"year": "1603", "event": "Acceded to English throne as James I; Union of the Crowns"},
        {"year": "1604", "event": "Hampton Court Conference; commissioned the King James Bible"},
        {"year": "1605", "event": "Gunpowder Plot thwarted; November 5 becomes annual celebration"},
        {"year": "1611", "event": "King James Bible published — transforming English language and literacy"},
        {"year": "1615", "event": "Ussher's Irish Articles shaped by his Reformed theological preferences"},
        {"year": "1625", "event": "Died at Theobald's Park; succeeded by Charles I"}
    ],
    "places": [
        {"name": "Edinburgh", "type": "birthplace and early reign"},
        {"name": "London", "type": "court and later reign"}
    ],
    "quote": "No bishop, no king. — James I at the Hampton Court Conference (1604)",
    "frameworks": ["political-history", "reformation", "monarchy", "bible-translation"],
    "historicalSignificance": {
        "significanceScore": 8,
        "significanceNarrative": "James I's commissioning of the King James Bible is one of the most consequential acts of cultural patronage in history — producing the most printed, most quoted, most translated English text ever written. His union of the Scottish and English crowns created the political foundation of modern Britain. His divine right theories triggered the constitutional crisis that led to the English Civil War.",
        "significanceCategory": "world-changing"
    }
}
james_i_data = make_entity_file("205", "james-i-of-england", "James I of England",
                                 "Person", "Early Modern", "205.james-i-of-england", james_i_details)
save("205", "205james-i-of-england.json", james_i_data)
print("Created james-i-of-england: OK")


# =============================================================================
# 5. COUNCIL OF NICAEA
# =============================================================================
nicaea_details = {
    "summary": (
        "The First Council of Nicaea (325 CE) was the first ecumenical council of the Christian Church, convened "
        "by Emperor Constantine I at Nicaea (modern Iznik, Turkey) to resolve the Arian controversy — the dispute "
        "over whether Jesus Christ was co-eternal with God the Father or a created being. The council was attended "
        "by approximately 318 bishops from across the Roman Empire, from Britain to Persia, gathered in the most "
        "ambitious exercise of Christian consensus-building in history.\n\n"
        "The council's primary output was the Nicene Creed — a formal statement of Trinitarian theology asserting "
        "that Christ was 'of the same substance' (homoousios) as the Father. It also established a unified "
        "calculation of Easter (based on the spring equinox and lunar calendar), condemned Arianism as heresy, "
        "and set boundaries for clerical conduct and church governance. The council represented the first time "
        "state power (imperial Rome) was harnessed to enforce Christian doctrinal unity.\n\n"
        "The Council of Nicaea's theological decisions defined the orthodox Christianity that spread to Europe, "
        "the Americas, Africa, and Asia over the following 1,700 years. The Nicene Creed is still recited in "
        "Catholic, Orthodox, and most Protestant services worldwide. The concept of 'heresy' as a legal and "
        "theological category was effectively inaugurated at Nicaea.\n\n"
        "More bishops were present at Nicaea than at any council until Vatican II (1962–1965)."
    ),
    "causes": [
        "The Arian controversy: Arius of Alexandria teaching that the Son was created and subordinate to the Father",
        "Constantine I's political need for religious unity across the newly-Christianized empire",
        "Letters and synods failing to resolve the controversy locally — requiring an imperial intervention"
    ],
    "effects": [
        "Nicene Creed defining Trinitarian orthodoxy — still recited by billions of Christians worldwide",
        "Condemnation of Arianism as heresy, though Arianism survived and later converted Germanic tribes",
        "Standardization of Easter calculation across the empire",
        "Establishment of the precedent for ecumenical councils to define Christian doctrine",
        "Council of Constantinople (381) and Council of Chalcedon (451) built directly on Nicaea"
    ],
    "relationships": [
        {"verb": "INFLUENCES", "targetSlug": "jesus-christ", "targetName": "Jesus Christ",
         "context": "Formally defined the divine nature of Christ — the central theological claim about Jesus"},
        {"verb": "INFLUENCES", "targetSlug": "nicene-creed", "targetName": "Nicene Creed",
         "context": "Produced the Nicene Creed as the formal doctrinal statement of Trinitarian Christianity"},
        {"verb": "INFLUENCES", "targetSlug": "constantine-i", "targetName": "Constantine I",
         "context": "Convened and presided over by Constantine I; his first major act of Christian policy"},
        {"verb": "INFLUENCES", "targetSlug": "roman-catholic-church", "targetName": "Roman Catholic Church",
         "context": "Established the precedent for papal/episcopal authority to define doctrine"},
        {"verb": "INFLUENCES", "targetSlug": "early-church", "targetName": "Early Church",
         "context": "Transformed the early church from a diverse movement into an institutionalized orthodoxy"},
        {"verb": "OCCURS_IN", "targetSlug": "nicaea", "targetName": "Nicaea (modern Iznik, Turkey)",
         "context": "Met in the imperial palace at Nicaea, Bithynia"},
        {"verb": "OCCURS_DURING", "targetSlug": "classical-3000bce-500ce", "targetName": "Classical Era",
         "context": "Convened in 325 CE, one century before the fall of the Western Roman Empire"}
    ],
    "texts": [
        {
            "title": "Nicene Creed",
            "slug": "nicene-creed",
            "type": "creed",
            "year": "325 CE (expanded 381)",
            "description": "Primary doctrinal output of the council; still recited in Christian worship worldwide"
        }
    ],
    "evidence": [
        {
            "tier": "A",
            "source": "Eusebius of Caesarea, Life of Constantine, Book 3 (c. 336 CE)",
            "note": "Eyewitness account of the council by Eusebius, who was present",
            "citationStyle": "book:chapter"
        },
        {
            "tier": "A",
            "source": "Council canons and letter to the Alexandrian church (preserved in Greek and Latin)",
            "note": "Primary documentary record of the council's decisions",
            "citationStyle": "document"
        },
        {
            "tier": "C",
            "source": "Rowan Williams, Arius: Heresy and Tradition (1987)",
            "note": "Definitive modern analysis of the Arian controversy and Nicaea",
            "citationStyle": "page"
        }
    ],
    "timeline": [
        {"year": "c. 318 CE", "event": "Arius of Alexandria begins teaching Christ is a created being, subordinate to the Father"},
        {"year": "325 CE", "event": "Council of Nicaea convened by Constantine I; ~318 bishops attend"},
        {"year": "325 CE", "event": "Nicene Creed ratified; homoousios affirmed; Arianism condemned"},
        {"year": "325 CE", "event": "Easter calculation standardized based on spring equinox"},
        {"year": "335 CE", "event": "Arius partially rehabilitated by later synods; controversy continued"},
        {"year": "381 CE", "event": "Council of Constantinople expands the Nicene Creed to final form"},
        {"year": "451 CE", "event": "Council of Chalcedon further defines Christ's two natures"}
    ],
    "places": [
        {"name": "Nicaea", "type": "council location"},
        {"name": "Bithynia", "type": "province"}
    ],
    "frameworks": ["theological-history", "institution-building", "roman-empire", "religious-movements"],
    "historicalSignificance": {
        "significanceScore": 9,
        "significanceNarrative": "The Council of Nicaea is the most consequential ecclesiastical meeting in the history of Christianity. Its definition of Christ's divine nature, embedded in the Nicene Creed, has been recited by an estimated 2 billion Christians across 17 centuries. It inaugurated the tradition of ecumenical councils that continues to define Christian doctrine today.",
        "significanceCategory": "world-changing"
    }
}
nicaea_data = make_entity_file("524", "council-of-nicaea", "Council of Nicaea",
                                "EventWindow", "Classical", "524.council-of-nicaea", nicaea_details)
save("524", "524council-of-nicaea.json", nicaea_data)
print("Created council-of-nicaea: OK")


print("\nBatch 67e complete. Created: Joseph Scaliger, Westminster Assembly, Republic of Letters, James I of England, Council of Nicaea")
