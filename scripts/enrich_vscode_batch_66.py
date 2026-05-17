#!/usr/bin/env python3
"""
Batch 66 — James Ussher (full), Jesus Christ (expanded), + 6 more entities.
Session ID: vscode-batch-66-may2026
Editor: claude-sonnet-4.6·cloud·GH#vscode
"""
import json
import os
import copy
from datetime import datetime, timezone

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-66-may2026"
NOW = datetime.now(timezone.utc).isoformat()

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENTITIES_DIR = os.path.join(ROOT, "data", "appwrite-export", "entities")


def load_entity(file_path: str) -> tuple[dict, dict, list]:
    """Load entity file, return (file_data, entity_obj, entities_list)."""
    with open(file_path) as f:
        d = json.load(f)
    entities = d.get("entities", [d])
    return d, entities[0] if entities else {}, entities


def save_entity(file_path: str, file_data: dict, entities: list):
    """Save entity file with entities list."""
    file_data["entities"] = entities
    with open(file_path, "w") as f:
        json.dump(file_data, f, indent=2, ensure_ascii=False)


def add_edit_log(dj: dict, changes: list[dict]) -> dict:
    """Add entries to _editLog in detailsJson."""
    el = dj.get("_editLog", [])
    for c in changes:
        el.append({
            "field": c["field"],
            "old": c.get("old", ""),
            "new": c.get("new", ""),
            "editedBy": EDITOR_ID,
            "editedAt": NOW,
            "sessionId": SESSION_ID,
        })
    dj["_editLog"] = el
    return dj


# ─────────────────────────────────────────────────────────
# ENTITY 1: James Ussher — Full enrichment
# ─────────────────────────────────────────────────────────

USSHER_PATH = os.path.join(ENTITIES_DIR, "205-Class-205", "205james-ussher.json")

USSHER_SUMMARY = (
    "James Ussher (1581–1656) was the Church of Ireland Archbishop of Armagh and one of "
    "the most erudite scholars of the seventeenth century. His magnum opus, *Annales "
    "Veteris Testamenti* (1650), presented a comprehensive biblical chronology that placed "
    "Creation at nightfall preceding Sunday, October 23, 4004 BCE — a date so precisely "
    "argued and so widely accepted that it was printed in the margins of the King James "
    "Bible for two centuries. Born in Dublin and educated at Trinity College Dublin, which "
    "he helped co-found at age eighteen, Ussher combined mastery of Hebrew, Greek, Latin, "
    "Arabic, and Syriac with access to manuscript collections across Europe and the "
    "Near East.\n\n"
    "Throughout his career Ussher served both as a leading theologian of Reformed "
    "Protestantism and as a loyal servant of the English crown. He drafted the Irish "
    "Articles of 1615 — the first confessional standard to explicitly endorse "
    "predestinarian Calvinist doctrine — which later influenced the Westminster Confession. "
    "His *Britannicarum Ecclesiarum Antiquitates* (1639) argued that the ancient Irish "
    "church predated Roman authority, lending scholarly weight to Anglican claims of "
    "apostolic independence. Despite his royalist sympathies, Oliver Cromwell "
    "respected Ussher so highly that he ordered a state funeral at Westminster Abbey in "
    "1656 — an extraordinary honour for a Church of Ireland archbishop in Puritan London.\n\n"
    "Ussher's chronology shaped Western intellectual culture for over two hundred years. "
    "By anchoring every Old Testament event to a precise year, he created the first "
    "systematic framework for universal history — a direct ancestor of the historical "
    "timelines that underpin modern historiography. Geologists and biologists of the "
    "eighteenth and nineteenth centuries (including Lyell and Darwin) were acutely "
    "aware they were dismantling Ussher's framework as they built the deep-time paradigm. "
    "His donated manuscript collection enriched the Bodleian Library at Oxford, and his "
    "correspondence network with Francis Bacon, Brian Walton, and continental scholars "
    "made him a central node of the Republic of Letters.\n\n"
    "'The Scripture chronology being so clear and evident,' Ussher wrote, 'I could not "
    "but wonder that any man of learning should question it.' That confidence exemplifies "
    "the seventeenth-century conviction that biblical philology and universal history were "
    "the same discipline — a synthesis Ussher brought to its highest expression."
)

USSHER_CAUSES = [
    "Protestant Reformation placed a premium on direct engagement with Hebrew and Greek scripture, creating demand for precise biblical chronology",
    "Trinity College Dublin's founding (1592) created Ireland's first centre for Oriental language study, which Ussher both catalysed and exploited",
    "The Thirty Years' War (1618–1648) made the confessional identity of Protestant churches an urgent political as well as theological question",
    "Archbishop Laud's ceremonialist reforms within the Church of England pushed Reformed churchmen to codify their Calvinist doctrinal position",
    "The Scaligerian revolution in chronology (De emendatione temporum, 1583) established the scholarly framework that Ussher refined into a biblical system",
]

USSHER_EFFECTS = [
    "The Ussher chronology was printed in the margins of the Authorized King James Bible from 1701, making 4004 BCE the de facto date of Creation for English-speaking Protestantism for two centuries",
    "The Irish Articles (1615) directly influenced the Westminster Confession (1647), the confessional standard of Reformed churches worldwide",
    "His manuscript collection, donated to the Bodleian Library and Trinity College Dublin, preserved rare Syriac, Arabic, and early Irish texts that survive nowhere else",
    "Geological and biological scientists from Hutton (1788) to Darwin (1859) explicitly framed their deep-time discoveries as refutations of Ussher, demonstrating the enduring cultural authority of his framework",
    "His argument for apostolic independence of the Irish church contributed to the theological self-understanding of Anglicanism as distinct from both Rome and Geneva",
    "His network of European scholarly correspondence modelled the Republic of Letters style of knowledge exchange that shaped early modern science",
]

USSHER_RELATIONSHIPS = [
    {"verb": "INFLUENCES", "targetSlug": "westminster-confession", "targetName": "Westminster Confession", "context": "Ussher's Irish Articles (1615) provided the theological template for the Westminster Confession of Faith (1647)"},
    {"verb": "INFLUENCES", "targetSlug": "king-james-bible", "targetName": "King James Bible", "context": "Ussher's 4004 BCE creation date was inserted in KJV margins from 1701, shaping two centuries of Protestant biblical interpretation"},
    {"verb": "INFLUENCES", "targetSlug": "charles-darwin", "targetName": "Charles Darwin", "context": "Darwin explicitly invoked and rejected Ussher's chronology to frame the deep-time argument in On the Origin of Species"},
    {"verb": "INFLUENCES", "targetSlug": "charles-lyell", "targetName": "Charles Lyell", "context": "Lyell's Principles of Geology (1830–33) was understood as a direct challenge to Ussher's biblical timescale"},
    {"verb": "OCCURS_IN", "targetSlug": "trinity-college-dublin", "targetName": "Trinity College Dublin", "context": "Ussher was among the original fellows at Trinity College Dublin's founding (1592) and later its Chancellor"},
    {"verb": "INFLUENCES", "targetSlug": "oliver-cromwell", "targetName": "Oliver Cromwell", "context": "Cromwell ordered Ussher a full state funeral at Westminster Abbey (1656), acknowledging him as a national scholar despite religious differences"},
    {"verb": "INFLUENCES", "targetSlug": "francis-bacon", "targetName": "Francis Bacon", "context": "Ussher and Bacon maintained an extensive correspondence on philosophy, chronology, and the organisation of knowledge"},
    {"verb": "INFLUENCES", "targetSlug": "protestant-reformation", "targetName": "Protestant Reformation", "context": "Ussher's Irish Articles were the first national confession of faith to codify high-Calvinist predestinarianism in Reformed Protestantism"},
    {"verb": "INFLUENCES", "targetSlug": "scientific-revolution", "targetName": "Scientific Revolution", "context": "Ussher's systematic biblical chronology was part of the same encyclopaedic impulse that drove early modern natural philosophy"},
    {"verb": "TRANSMITS", "targetSlug": "bodleian-library", "targetName": "Bodleian Library", "context": "Ussher donated his extensive manuscript collection (including rare Syriac and Irish texts) to the Bodleian Library at Oxford"},
    {"verb": "INFLUENCES", "targetSlug": "anglican-church", "targetName": "Anglican Church", "context": "His Britannicarum Ecclesiarum Antiquitates (1639) grounded Anglican claims of apostolic independence in historical scholarship"},
    {"verb": "OCCURS_DURING", "targetSlug": "early-modern-1500-1800", "targetName": "Early Modern Era", "context": "Ussher's career (1581–1656) epitomises the Early Modern synthesis of humanist philology, confessional theology, and universal history"},
]

USSHER_PLACES = [
    {"name": "Dublin, Ireland", "role": "birthplace and centre of Ussher's ecclesiastical career as Archbishop of Armagh"},
    {"name": "Westminster Abbey, London", "role": "site of Ussher's state funeral ordered by Cromwell in 1656"},
    {"name": "Oxford, England", "role": "Ussher donated his manuscript collection to the Bodleian Library here"},
    {"name": "Armagh, Ireland", "role": "seat of his archbishopric (Church of Ireland Province of Armagh)"},
    {"name": "Trinity College Dublin", "role": "co-founded 1592; Ussher served as Chancellor and donated his personal library"},
]

USSHER_TEXTS = [
    {"slug": "annales-veteris-testamenti", "name": "Annales Veteris Testamenti", "year": "1650", "role": "primary work establishing biblical chronology with Creation at 4004 BCE"},
    {"slug": "annalium-pars-posterior", "name": "Annalium Pars Posterior", "year": "1654", "role": "continuation of the Annales from Solomon to the New Testament period"},
    {"slug": "britannicarum-ecclesiarum-antiquitates", "name": "Britannicarum Ecclesiarum Antiquitates", "year": "1639", "role": "historical argument for apostolic independence of the Irish church predating Roman authority"},
    {"slug": "irish-articles-1615", "name": "Irish Articles", "year": "1615", "role": "Calvinist confession of faith drafted by Ussher that influenced the Westminster Confession"},
]

USSHER_TIMELINE = [
    {"year": "1581", "event": "Born in Dublin, Ireland, to a wealthy Anglo-Irish family on January 4"},
    {"year": "1594", "event": "Enrolled at Trinity College Dublin at age thirteen, just two years after its founding"},
    {"year": "1601", "event": "Ordained as a Church of Ireland deacon; began assembling his vast manuscript collection"},
    {"year": "1615", "event": "Drafted the Irish Articles — the first explicitly Calvinist national confession of faith in the British Isles"},
    {"year": "1625", "event": "Appointed Archbishop of Armagh, the senior position in the Church of Ireland"},
    {"year": "1639", "event": "Published Britannicarum Ecclesiarum Antiquitates, arguing the ancient Irish church's apostolic independence"},
    {"year": "1647", "event": "The Westminster Confession, partly modelled on Ussher's Irish Articles, adopted by the Westminster Assembly"},
    {"year": "1650", "event": "Published Annales Veteris Testamenti, placing Creation at nightfall before October 23, 4004 BCE"},
    {"year": "1654", "event": "Published Annalium Pars Posterior, the New Testament continuation of the Annales chronology"},
    {"year": "1656", "event": "Died at Reigate, Surrey; given a state funeral at Westminster Abbey by Oliver Cromwell"},
    {"year": "1701", "event": "The Ussher chronology was first printed in the margins of the Authorized (King James) Bible, establishing 4004 BCE for Protestant generations"},
]

USSHER_EVIDENCE = [
    {"tier": "A", "citation": "Ussher, James. Annales Veteris Testamenti, a Prima Mundi Origine Deducti. London, 1650."},
    {"tier": "B", "citation": "Gould, Stephen Jay. 'Fall in the House of Ussher.' Natural History, November 1991. Scholarly reassessment of Ussher's methodology."},
    {"tier": "B", "citation": "Barr, James. 'Why the World Was Created in 4004 BC: Archbishop Ussher and Biblical Chronology.' Bulletin of the John Rylands Library 67 (1985): 575–608."},
    {"tier": "C", "citation": "Wikipedia contributors. 'James Ussher.' Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/wiki/James_Ussher"},
]


def enrich_ussher():
    print("Enriching James Ussher...")
    file_data, entity, entities = load_entity(USSHER_PATH)

    dj = entity.get("detailsJson", {}) or {}
    if isinstance(dj, str):
        try:
            dj = json.loads(dj)
        except Exception:
            dj = {}
    dj = dict(dj)  # shallow copy

    changes = []

    # Summary
    old_summary = entity.get("summary", "") or ""
    entity["summary"] = USSHER_SUMMARY
    changes.append({"field": "summary", "old": f"(len={len(old_summary)})", "new": f"(len={len(USSHER_SUMMARY)})"})

    # Born
    entity["born"] = "1581-01-04"
    changes.append({"field": "born", "old": entity.get("born", ""), "new": "1581-01-04"})

    # Died
    entity["died"] = "1656-03-21"

    # continent / region
    entity["continent"] = "Europe"
    entity["region"] = "Western Europe"

    # importanceScore
    entity["importanceScore"] = 7
    changes.append({"field": "importanceScore", "old": str(entity.get("importanceScore", "")), "new": "7"})

    # subjectHeadings
    entity["subjectHeadings"] = ["James Ussher — Biblical Scholarship — Ireland — Early Modern"]
    entity["subjects"] = [
        "Ireland", "biblical chronology", "Archbishop of Armagh", "Church of Ireland",
        "Protestant Reformation", "Early Modern Europe", "chronology", "theology",
        "historical scholarship", "Trinity College Dublin"
    ]

    # frameworks
    entity["frameworks"] = [
        "RELIGIOUS_THOUGHT", "INTELLECTUAL_HISTORY", "REFORMATION_AND_CONFESSIONALISM",
        "CAUSE_AND_EFFECT", "IDEAS_AND_WORLDVIEWS", "PRINT_CULTURE_AND_KNOWLEDGE"
    ]
    changes.append({"field": "frameworks", "old": "[]", "new": str(entity["frameworks"])})

    # quote
    entity["quote"] = "'The Scripture chronology being so clear and evident, I could not but wonder that any man of learning should question it.' — James Ussher, Annales Veteris Testamenti (1650)"

    # thumbnailUrl
    entity["thumbnailUrl"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/James_Ussher_by_Sir_Peter_Lely.jpg/440px-James_Ussher_by_Sir_Peter_Lely.jpg"
    entity["wikipediaUrl"] = "https://en.wikipedia.org/wiki/James_Ussher"

    # detailsJson updates
    dj["causes"] = USSHER_CAUSES
    dj["effects"] = USSHER_EFFECTS
    dj["relationships"] = USSHER_RELATIONSHIPS
    dj["places"] = USSHER_PLACES
    dj["texts"] = USSHER_TEXTS
    dj["timeline"] = USSHER_TIMELINE
    dj["evidence"] = USSHER_EVIDENCE
    dj["historicalSignificance"] = {
        "significanceScore": 8,
        "significanceCategory": "continental",
        "significanceNarrative": (
            "James Ussher shaped the intellectual landscape of the Protestant world for two centuries. "
            "His biblical chronology — printed in KJV margins from 1701 — made 4004 BCE the de facto "
            "creation date for English-speaking Christianity, and his Irish Articles influenced Reformed "
            "confessional theology worldwide. Scientists from Hutton to Darwin measured their deep-time "
            "discoveries against Ussher's framework, giving his work an unintended role in the scientific "
            "revolution. He remains the most significant biblical scholar produced by Ireland."
        ),
    }
    dj["quote"] = entity["quote"]
    dj["frameworks"] = entity["frameworks"]
    dj["sessionId"] = SESSION_ID
    dj["enrichedBy"] = EDITOR_ID
    dj["enrichedAt"] = NOW

    dj = add_edit_log(dj, changes)

    entity["detailsJson"] = dj
    entity["_unsyncedEdits"] = True

    print(f"  summary: {len(USSHER_SUMMARY)}c | rels: {len(USSHER_RELATIONSHIPS)} | causes: {len(USSHER_CAUSES)} | effects: {len(USSHER_EFFECTS)}")
    save_entity(USSHER_PATH, file_data, entities)
    print(f"  Saved: {USSHER_PATH}")


# ─────────────────────────────────────────────────────────
# ENTITY 2: Jesus Christ — Expanded enrichment
# ─────────────────────────────────────────────────────────

JESUS_PATH = os.path.join(ENTITIES_DIR, "201-Class-201", "201jesus-christ.json")

JESUS_ADDITIONAL_RELATIONSHIPS = [
    {"verb": "INFLUENCES", "targetSlug": "new-testament", "targetName": "New Testament", "context": "The New Testament is entirely devoted to the life, teachings, death, and resurrection of Jesus — the foundational document of Christianity"},
    {"verb": "INFLUENCES", "targetSlug": "paul-the-apostle", "targetName": "Paul the Apostle", "context": "Paul's theological reinterpretation of Jesus's death and resurrection (epistles c. 50–60 CE) defined Christian doctrine for millennia"},
    {"verb": "INFLUENCES", "targetSlug": "roman-catholic-church", "targetName": "Roman Catholic Church", "context": "The institutional Catholic Church regards itself as the body of Christ and the continuation of his mission on earth"},
    {"verb": "INFLUENCES", "targetSlug": "protestant-reformation", "targetName": "Protestant Reformation", "context": "Luther, Calvin, and the reformers claimed to restore the original teaching of Jesus against institutional corruption"},
    {"verb": "INFLUENCES", "targetSlug": "constantine-i", "targetName": "Constantine I", "context": "Constantine's conversion (312 CE) and the Edict of Milan (313 CE) made Christianity the tolerated — then dominant — religion of the Roman Empire"},
    {"verb": "INFLUENCES", "targetSlug": "crusades", "targetName": "The Crusades", "context": "The Crusades (1096–1291) were launched to recover Jerusalem, the site of Jesus's death and resurrection, from Muslim rule"},
    {"verb": "INFLUENCES", "targetSlug": "islamic-tradition", "targetName": "Islamic Tradition", "context": "Islam venerates Jesus (Isa) as a major prophet and the Messiah (though not divine), drawing on the same prophetic lineage"},
    {"verb": "INFLUENCES", "targetSlug": "western-calendar", "targetName": "Western Calendar (AD/BC system)", "context": "The Gregorian calendar divides history into BC/AD based on the estimated year of Jesus's birth, structuring global timekeeping"},
    {"verb": "INFLUENCES", "targetSlug": "renaissance-art", "targetName": "Renaissance Art", "context": "The life and passion of Jesus Christ was the primary subject of European art from the Byzantine era through the Renaissance"},
    {"verb": "INFLUENCES", "targetSlug": "liberation-theology", "targetName": "Liberation Theology", "context": "20th-century liberation theologians drew on Jesus's ministry to the poor and marginalised as a mandate for social justice"},
]

JESUS_TEXTS = [
    {"slug": "gospel-of-matthew", "name": "Gospel of Matthew", "year": "c. 80–90 CE", "role": "First canonical gospel, emphasizing Jesus as the fulfilment of Jewish prophecy and the new Moses"},
    {"slug": "gospel-of-mark", "name": "Gospel of Mark", "year": "c. 65–70 CE", "role": "Oldest canonical gospel, presenting Jesus as a miracle-worker and suffering servant"},
    {"slug": "gospel-of-luke", "name": "Gospel of Luke", "year": "c. 80–90 CE", "role": "Emphasizes Jesus's compassion for the poor and marginalised; includes the parables of the Good Samaritan and Prodigal Son"},
    {"slug": "gospel-of-john", "name": "Gospel of John", "year": "c. 90–110 CE", "role": "Theological gospel identifying Jesus as the divine Logos ('In the beginning was the Word')"},
    {"slug": "new-testament", "name": "New Testament", "year": "c. 50–110 CE", "role": "The 27-book collection that records Jesus's life (gospels), the early church (Acts), and theological interpretation (epistles, Revelation)"},
    {"slug": "didache", "name": "Didache", "year": "c. 50–120 CE", "role": "One of the earliest Christian texts, preserving Jesus's moral teachings (Two Ways) in a liturgical manual"},
]

JESUS_TIMELINE = [
    {"year": "c. 4 BCE", "event": "Birth of Jesus of Nazareth in Judea; traditionally dated to Bethlehem during the reign of Herod the Great"},
    {"year": "c. 6–7 CE", "event": "Jesus's visit to the Jerusalem Temple at age twelve; first recorded episode of his life beyond infancy"},
    {"year": "c. 27–29 CE", "event": "Baptism by John the Baptist in the Jordan River; the beginning of Jesus's public ministry"},
    {"year": "c. 27–30 CE", "event": "Sermon on the Mount delivered; teaching the Beatitudes, the Lord's Prayer, and the ethical core of Christian morality"},
    {"year": "c. 27–30 CE", "event": "Jesus selects the Twelve Apostles, establishing the leadership structure of the early church"},
    {"year": "c. 30 CE", "event": "Triumphal entry into Jerusalem; Last Supper with the Twelve (institution of the Eucharist)"},
    {"year": "c. 30–33 CE", "event": "Crucifixion under Pontius Pilate; buried in a rock tomb outside Jerusalem"},
    {"year": "c. 30–33 CE", "event": "Resurrection on the third day (Easter Sunday) — the theological centre of Christian faith"},
    {"year": "c. 30–33 CE", "event": "Ascension into heaven forty days after the Resurrection; Pentecost (descent of the Holy Spirit) follows fifty days after Easter"},
    {"year": "c. 50–64 CE", "event": "Paul's epistles written; Jesus reinterpreted as cosmic saviour, his death as atonement — forming systematic Christology"},
    {"year": "c. 65–110 CE", "event": "Four canonical Gospels written, fixing the narrative tradition of Jesus's life for subsequent Christianity"},
]

JESUS_EVIDENCE = [
    {"tier": "A", "citation": "The Four Gospels (Matthew, Mark, Luke, John), New Testament, c. 65–110 CE. Primary narrative sources for Jesus's life."},
    {"tier": "A", "citation": "Paul's Epistles (1 Thessalonians, Galatians, 1 Corinthians, etc.), c. 50–60 CE. Earliest surviving Christian documents; Paul knew eyewitnesses."},
    {"tier": "B", "citation": "Tacitus, Annals XV.44, c. 116 CE. Roman historian confirms execution of 'Christus' under Pontius Pilate."},
    {"tier": "B", "citation": "Josephus, Antiquities XX.9.1, c. 93 CE. Jewish historian mentions 'Jesus who was called Christ' in context of James's execution."},
    {"tier": "C", "citation": "Meier, John P. A Marginal Jew: Rethinking the Historical Jesus. 4 vols. New York: Doubleday/Yale, 1991–2009. Standard modern historical-critical study."},
    {"tier": "C", "citation": "Crossan, John Dominic. The Historical Jesus: The Life of a Mediterranean Jewish Peasant. San Francisco: Harper, 1991."},
]

JESUS_ADDITIONAL_FRAMEWORKS = [
    "CIVILIZATIONAL_TRANSFORMATION",
    "EMPIRE_AND_COLONIALISM",
    "GENDER_AND_SOCIAL_STRUCTURES",
    "CAUSE_AND_EFFECT",
    "IDEAS_AND_WORLDVIEWS",
    "DIFFUSION_AND_EXCHANGE",
    "PRINT_CULTURE_AND_KNOWLEDGE",
]


def enrich_jesus():
    print("Expanding Jesus Christ enrichment...")
    file_data, entity, entities = load_entity(JESUS_PATH)

    dj = entity.get("detailsJson", {}) or {}
    if isinstance(dj, str):
        try:
            dj = json.loads(dj)
        except Exception:
            dj = {}
    dj = dict(dj)

    changes = []

    # Extend relationships (merge with existing, avoid dupes by targetSlug)
    existing_rels = dj.get("relationships", [])
    existing_slugs = {r.get("targetSlug") for r in existing_rels}
    new_rels = [r for r in JESUS_ADDITIONAL_RELATIONSHIPS if r["targetSlug"] not in existing_slugs]
    dj["relationships"] = existing_rels + new_rels
    changes.append({"field": "relationships", "old": f"(count={len(existing_rels)})", "new": f"(count={len(dj['relationships'])})"})

    # Add texts
    dj["texts"] = JESUS_TEXTS
    changes.append({"field": "texts", "old": "[]", "new": f"(count={len(JESUS_TEXTS)})"})

    # Add timeline
    dj["timeline"] = JESUS_TIMELINE
    changes.append({"field": "timeline", "old": "[]", "new": f"(count={len(JESUS_TIMELINE)})"})

    # Add evidence
    dj["evidence"] = JESUS_EVIDENCE
    changes.append({"field": "evidence", "old": "[]", "new": f"(count={len(JESUS_EVIDENCE)})"})

    # Expand frameworks
    existing_fw = dj.get("frameworks", [])
    merged_fw = list(dict.fromkeys(existing_fw + JESUS_ADDITIONAL_FRAMEWORKS))
    dj["frameworks"] = merged_fw
    entity["frameworks"] = merged_fw
    changes.append({"field": "frameworks", "old": str(existing_fw), "new": str(merged_fw)})

    # Add places if not present
    if not dj.get("places"):
        dj["places"] = [
            {"name": "Bethlehem, Judea", "role": "traditional birthplace"},
            {"name": "Nazareth, Galilee", "role": "hometown where Jesus grew up; 'Jesus of Nazareth'"},
            {"name": "Jerusalem, Judea", "role": "site of the Last Supper, crucifixion, resurrection, and ascension"},
            {"name": "Jordan River, Judea", "role": "site of Jesus's baptism by John the Baptist"},
            {"name": "Sea of Galilee", "role": "region of most of Jesus's public ministry and miracle accounts"},
        ]
        changes.append({"field": "places", "old": "[]", "new": "(count=5)"})

    # Add born / died
    entity["born"] = "c. 4 BCE"
    entity["died"] = "c. 30-33 CE"

    # subjectHeadings
    entity["subjectHeadings"] = ["Jesus Christ — Christianity — Ancient Judea — Classical Era"]
    entity["subjects"] = [
        "Christianity", "Judaism", "religion", "salvation", "Christology",
        "New Testament", "Roman Empire", "Galilee", "Jerusalem", "prophet"
    ]

    dj["sessionId"] = SESSION_ID
    dj["enrichedBy"] = EDITOR_ID
    dj["enrichedAt"] = NOW

    dj = add_edit_log(dj, changes)
    entity["detailsJson"] = dj
    entity["_unsyncedEdits"] = True

    print(f"  rels: {len(dj['relationships'])} | texts: {len(JESUS_TEXTS)} | timeline: {len(JESUS_TIMELINE)} | evidence: {len(JESUS_EVIDENCE)}")
    save_entity(JESUS_PATH, file_data, entities)
    print(f"  Saved: {JESUS_PATH}")


# ─────────────────────────────────────────────────────────
# ENTITY 3: Ramesses II
# ─────────────────────────────────────────────────────────

RAMESSES_PATH = os.path.join(ENTITIES_DIR, "221-Class-221", "221ramesses-ii.json")


def enrich_ramesses():
    if not os.path.exists(RAMESSES_PATH):
        print(f"  SKIP (file not found): {RAMESSES_PATH}")
        return
    print("Enriching Ramesses II...")
    file_data, entity, entities = load_entity(RAMESSES_PATH)

    if len(entity.get("summary", "") or "") > 600:
        print(f"  Already enriched (summary={len(entity.get('summary',''))}c), skipping.")
        return

    summary = (
        "Ramesses II (c. 1303–1213 BCE), called Ramesses the Great, was the third pharaoh of "
        "the Nineteenth Dynasty of Egypt and one of antiquity's most powerful rulers. Reigning "
        "for approximately sixty-six years (c. 1279–1213 BCE), he outlived twelve crown princes "
        "and fathered an estimated ninety to one hundred children. His reign represented the "
        "zenith of Egyptian imperial power, military prestige, and monumental building.\n\n"
        "His greatest military campaign was the Battle of Kadesh (c. 1274 BCE) against the "
        "Hittite Empire under Muwatalli II — one of the earliest battles in recorded history "
        "for which tactical details survive. Though neither side achieved a decisive victory, "
        "Ramesses proclaimed it a triumphant success, commissioning enormous reliefs at Abu "
        "Simbel, the Ramesseum, and Karnak. It ultimately led to the Egyptian–Hittite peace "
        "treaty (c. 1259 BCE), the world's oldest surviving international peace agreement, "
        "preserved in both Egyptian hieroglyphics and Akkadian cuneiform.\n\n"
        "Ramesses was the pre-eminent builder of ancient Egypt, constructing or completing the "
        "temples at Abu Simbel, Luxor, Abydos, and Pi-Ramesses (his new Delta capital). His "
        "colossal statues and cartouches were so pervasive that later pharaohs appropriated many "
        "of them. Many scholars identify him as the 'Pharaoh of the Exodus', though the "
        "historical evidence remains debated. His mummy, discovered in the Deir el-Bahari cache "
        "in 1881, is one of the best-preserved in the Egyptian Museum, Cairo."
    )

    dj = entity.get("detailsJson", {}) or {}
    if isinstance(dj, str):
        try:
            dj = json.loads(dj)
        except Exception:
            dj = {}
    dj = dict(dj)

    entity["summary"] = summary
    entity["born"] = "c. 1303 BCE"
    entity["died"] = "c. 1213 BCE"
    entity["importanceScore"] = 9
    entity["continent"] = "Africa"
    entity["region"] = "North Africa"
    entity["frameworks"] = ["EMPIRE_AND_COLONIALISM", "RELIGIOUS_THOUGHT", "CAUSE_AND_EFFECT", "IDEAS_AND_WORLDVIEWS"]
    entity["subjectHeadings"] = ["Ramesses II — Ancient Egypt — North Africa — Classical Era"]
    entity["subjects"] = ["Egypt", "pharaoh", "New Kingdom", "Battle of Kadesh", "Abu Simbel", "Exodus", "ancient Near East", "Hittites"]

    dj["causes"] = [
        "The expulsion of the Hyksos (c. 1550 BCE) created the Egyptian New Kingdom imperial tradition that Ramesses inherited and extended",
        "The rise of the Hittite Empire in Anatolia created a rival power that threatened Egyptian control of Canaan and Syria",
        "The Egyptian religious system invested pharaohs with divine status (as sons of Ra), giving rulers unlimited authority to mobilise resources for war and building",
    ]
    dj["effects"] = [
        "The Egyptian-Hittite peace treaty (c. 1259 BCE) established the model of international diplomacy confirmed by written treaty, influencing Near Eastern statecraft",
        "Abu Simbel and the Ramesseum became the defining images of Egyptian imperial grandeur, shaping perceptions of ancient Egypt into the modern era",
        "Ramesses' reign established a precedent for prolonged one-man rule that subsequent pharaohs struggled to match, contributing to dynastic instability after his death",
        "His identification as the pharaoh of the biblical Exodus, though unverified, gave his reign central importance in the Abrahamic religious traditions",
    ]
    dj["relationships"] = [
        {"verb": "INFLUENCES", "targetSlug": "hittite-empire", "targetName": "Hittite Empire", "context": "The Egyptian-Hittite peace treaty (c. 1259 BCE) after Kadesh is the world's oldest surviving international treaty"},
        {"verb": "INFLUENCES", "targetSlug": "ancient-egypt", "targetName": "Ancient Egypt", "context": "Ramesses II personifies New Kingdom Egypt at its height; his 66-year reign set architectural and imperial benchmarks for all successors"},
        {"verb": "OCCURS_IN", "targetSlug": "abu-simbel", "targetName": "Abu Simbel", "context": "Ramesses commissioned the two massive rock-cut temples at Abu Simbel, featuring four 20-metre statues of himself"},
        {"verb": "INFLUENCES", "targetSlug": "biblical-exodus", "targetName": "Exodus (Biblical)", "context": "Many scholars identify Ramesses II as the pharaoh of the Exodus narrative (Exodus 1–15)"},
        {"verb": "INFLUENCES", "targetSlug": "mesopotamian-civilizations", "targetName": "Mesopotamian Civilizations", "context": "Egyptian-Hittite diplomacy shaped Near Eastern power balance during the Bronze Age"},
    ]
    dj["historicalSignificance"] = {
        "significanceScore": 9,
        "significanceCategory": "world-changing",
        "significanceNarrative": "Ramesses II produced the world's first international peace treaty, built some of antiquity's greatest monuments, and became — through his association with the Exodus — one of the most recognisable names in all of human history.",
    }
    dj["places"] = [
        {"name": "Thebes (Luxor), Egypt", "role": "capital of New Kingdom Egypt and site of major Ramesside temples"},
        {"name": "Abu Simbel, Nubia", "role": "site of Ramesses' two great rock-cut temples"},
        {"name": "Pi-Ramesses (Qantir), Egypt", "role": "Ramesses' new Delta capital, one of the largest cities of the ancient world"},
        {"name": "Kadesh, Syria", "role": "site of the famous battle against the Hittites (c. 1274 BCE)"},
    ]
    dj["sessionId"] = SESSION_ID
    dj["enrichedBy"] = EDITOR_ID
    dj["enrichedAt"] = NOW

    entity["detailsJson"] = dj
    entity["_unsyncedEdits"] = True
    save_entity(RAMESSES_PATH, file_data, entities)
    print(f"  Saved. summary={len(summary)}c | rels={len(dj['relationships'])}")


# ─────────────────────────────────────────────────────────
# ENTITY 4: Peter the Great
# ─────────────────────────────────────────────────────────

def find_entity_file(slug_fragment: str) -> str | None:
    for root, dirs, files in os.walk(ENTITIES_DIR):
        for fname in files:
            if slug_fragment in fname:
                return os.path.join(root, fname)
    return None


def enrich_simple(slug: str, name: str, summary: str, born: str, died: str,
                  continent: str, region: str, score: int, causes: list, effects: list,
                  rels: list, places: list, frameworks: list, subjects: list,
                  sig_narrative: str, sig_category: str):
    path = find_entity_file(slug)
    if not path:
        print(f"  SKIP (file not found for slug: {slug})")
        return
    print(f"Enriching {name}...")
    file_data, entity, entities = load_entity(path)

    if len(entity.get("summary", "") or "") > 600:
        print(f"  Already enriched (summary={len(entity.get('summary',''))}c), skipping.")
        return

    dj = entity.get("detailsJson", {}) or {}
    if isinstance(dj, str):
        try:
            dj = json.loads(dj)
        except Exception:
            dj = {}
    dj = dict(dj)

    entity["summary"] = summary
    if born:
        entity["born"] = born
    if died:
        entity["died"] = died
    entity["importanceScore"] = score
    entity["continent"] = continent
    entity["region"] = region
    entity["frameworks"] = frameworks
    entity["subjectHeadings"] = [f"{name} — {subjects[0]} — {continent} — Early Modern"]
    entity["subjects"] = subjects

    dj["causes"] = causes
    dj["effects"] = effects
    dj["relationships"] = rels
    dj["places"] = places
    dj["historicalSignificance"] = {
        "significanceScore": score,
        "significanceCategory": sig_category,
        "significanceNarrative": sig_narrative,
    }
    dj["sessionId"] = SESSION_ID
    dj["enrichedBy"] = EDITOR_ID
    dj["enrichedAt"] = NOW

    entity["detailsJson"] = dj
    entity["_unsyncedEdits"] = True
    save_entity(path, file_data, entities)
    print(f"  Saved {path}. summary={len(summary)}c | rels={len(rels)}")


# ─────────────────────────────────────────────────────────
# ENTITY 5: Constantine I
# ─────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    enrich_ussher()
    enrich_jesus()
    enrich_ramesses()

    # Peter the Great
    enrich_simple(
        slug="peter-the-great",
        name="Peter the Great",
        summary=(
            "Peter I of Russia (1672–1725), known as Peter the Great, was the Tsar and later "
            "Emperor of Russia who transformed a backward medieval tsardom into a modern "
            "European great power in the space of four decades. Driven by an insatiable curiosity "
            "about Western technology, Peter famously travelled incognito through Western Europe in "
            "1697–98 as part of the 'Grand Embassy', working in Dutch shipyards and visiting English "
            "workshops, returning with hundreds of foreign specialists to staff his new army, navy, "
            "and bureaucracy.\n\n"
            "Peter's modernisation programme reshaped every aspect of Russian life: he built the "
            "Baltic fleet from nothing, founded the city of Saint Petersburg as Russia's 'window to "
            "Europe' (1703), reorganised the government on Western models, abolished the patriarchate "
            "and brought the Russian Orthodox Church under state control, introduced the Julian "
            "calendar, and required the nobility to shave their beards and adopt Western dress. "
            "His victory over Charles XII of Sweden at the Battle of Poltava (1709) shattered Swedish "
            "hegemony in Northern Europe and established Russia as the region's dominant power.\n\n"
            "Peter's legacy is dual-edged: he accelerated Russia's military and administrative power "
            "at the cost of crushing serfdom further into the peasantry, suppressing traditional "
            "culture, and destroying opponents with extreme brutality — including his own son Alexei. "
            "Nevertheless, his creation of the Russian Empire set the template for subsequent "
            "Russian rulers from Catherine the Great to Stalin: a state that modernises by decree "
            "from above."
        ),
        born="1672-06-09",
        died="1725-02-08",
        continent="Europe",
        region="Eastern Europe",
        score=9,
        causes=[
            "The Time of Troubles (1598–1613) and subsequent Romanov consolidation created a centralised autocracy ready for top-down reform",
            "Russia's military defeats against Sweden in the Great Northern War's early phase revealed fatal technological and organisational backwardness",
            "The Ottoman and Polish threats on Russia's southern and western borders created urgent demand for a modernised military",
        ],
        effects=[
            "Saint Petersburg became Russia's imperial capital and a major European cultural centre for two centuries",
            "The Battle of Poltava (1709) ended Swedish Baltic dominance and made Russia the preeminent power of northern Europe",
            "Peter's administrative and military reforms provided the institutional framework that sustained the Russian Empire until 1917",
            "The subordination of the Orthodox Church to the state under Peter's Holy Synod model persisted until the 1917 revolution",
        ],
        rels=[
            {"verb": "INFLUENCES", "targetSlug": "catherine-the-great", "targetName": "Catherine the Great", "context": "Catherine continued and extended Peter's Westernisation programme, ruling with his blueprint for over thirty years"},
            {"verb": "INFLUENCES", "targetSlug": "charles-xii-of-sweden", "targetName": "Charles XII of Sweden", "context": "Peter's victory over Charles XII at Poltava (1709) ended Swedish great-power status and inaugurated the Russian imperial era"},
            {"verb": "INFLUENCES", "targetSlug": "russian-empire", "targetName": "Russian Empire", "context": "Peter transformed the Tsardom of Muscovy into the Russian Empire (1721), a title he adopted after victory in the Great Northern War"},
            {"verb": "INFLUENCES", "targetSlug": "enlightenment", "targetName": "Enlightenment", "context": "Peter introduced Enlightenment rationalism and scientific institutions to Russia, founding the Saint Petersburg Academy of Sciences"},
            {"verb": "INFLUENCES", "targetSlug": "ottoman-empire", "targetName": "Ottoman Empire", "context": "Peter's campaigns against the Ottomans sought access to the Black Sea, initiating the Russo-Ottoman rivalry that lasted centuries"},
            {"verb": "OCCURS_IN", "targetSlug": "saint-petersburg", "targetName": "Saint Petersburg", "context": "Peter founded Saint Petersburg in 1703 as Russia's capital and symbolic gateway to Europe"},
        ],
        places=[
            {"name": "Moscow, Russia", "role": "birthplace and original seat of Tsarist power"},
            {"name": "Saint Petersburg, Russia", "role": "city founded by Peter in 1703; imperial capital 1712–1917"},
            {"name": "Poltava, Ukraine", "role": "site of the decisive 1709 battle that ended Swedish hegemony"},
        ],
        frameworks=["EMPIRE_AND_COLONIALISM", "MODERNISATION_AND_STATE_BUILDING", "CAUSE_AND_EFFECT", "DIFFUSION_AND_EXCHANGE", "IDEAS_AND_WORLDVIEWS"],
        subjects=["Russia", "modernisation", "Russian Empire", "Saint Petersburg", "Great Northern War", "Enlightenment", "absolutism", "Orthodox Church"],
        sig_narrative="Peter the Great single-handedly redirected Russia's trajectory from a medieval Orthodox tsardom to a modern European empire, winning great-power status at Poltava and founding the administrative-military state that defined Russia until 1917.",
        sig_category="world-changing",
    )

    # Louis XIV of France
    enrich_simple(
        slug="louis-xiv-of-france",
        name="Louis XIV of France",
        summary=(
            "Louis XIV (1638–1715), known as the Sun King, was King of France for seventy-two "
            "years (1643–1715) — the longest verified reign of any major European monarch. His "
            "personal rule after 1661 made France the dominant European power of the seventeenth "
            "century and established Versailles as the model for absolutist court culture across "
            "the continent. His famous declaration 'L'état, c'est moi' ('I am the state') "
            "encapsulated the absolutist theory of sovereignty he embodied.\n\n"
            "Louis transformed the French court by constructing the Palace of Versailles, "
            "physically relocating his nobles from their provincial power bases to a gilded cage "
            "of court ritual and ceremonial, neutralising the aristocratic threat to royal authority "
            "that had nearly destroyed the monarchy during his childhood (the Fronde, 1648–53). "
            "His wars — the Dutch War, the Nine Years' War, and the War of the Spanish Succession — "
            "reshaped European borders but ultimately exhausted France's treasury and left "
            "Louis's successor with staggering debts. His revocation of the Edict of Nantes (1685) "
            "expelled 200,000 Huguenots, exporting skilled artisans and intellectuals to England, "
            "Prussia, and the Netherlands.\n\n"
            "Louis's cultural legacy rivals his political impact. He was the patron of Molière, "
            "Racine, and Lully; the Académie française flourished under royal subsidy; French "
            "became the language of European diplomacy and culture. Versailles was copied from "
            "Schönbrunn to Peterhof. His reign defined European baroque civilisation and the model "
            "of the centralised nation-state."
        ),
        born="1638-09-05",
        died="1715-09-01",
        continent="Europe",
        region="Western Europe",
        score=9,
        causes=[
            "The Fronde rebellions (1648–53) traumatised the young Louis and taught him that the nobility had to be controlled through proximity and ceremony rather than force",
            "Cardinal Mazarin's tutelage gave Louis a thorough education in European power politics and the mechanisms of absolutist governance",
            "France's emergence as the largest population and most productive agricultural economy in Europe gave Louis the demographic base to fund his ambitions",
        ],
        effects=[
            "The Palace of Versailles established the architectural and social template for European absolutist courts from Vienna to Saint Petersburg",
            "The Revocation of the Edict of Nantes (1685) expelled France's Protestant skilled class, enriching England, Prussia, and the Netherlands at France's expense",
            "The War of the Spanish Succession (1701–14) and the Treaty of Utrecht established the modern principle of maintaining a balance of power in Europe",
            "French became and remained the language of European diplomacy, science, and elite culture until the twentieth century",
        ],
        rels=[
            {"verb": "INFLUENCES", "targetSlug": "versailles", "targetName": "Palace of Versailles", "context": "Louis XIV transformed Versailles from a hunting lodge into the greatest palace in Europe and the symbol of absolute monarchy"},
            {"verb": "INFLUENCES", "targetSlug": "peter-the-great", "targetName": "Peter the Great", "context": "Peter the Great modelled his Saint Petersburg and court culture partly on Louis's Versailles"},
            {"verb": "INFLUENCES", "targetSlug": "protestant-reformation", "targetName": "Protestant Reformation (Huguenots)", "context": "Louis's Revocation of the Edict of Nantes expelled 200,000 Huguenots, reshaping Protestant communities across Europe"},
            {"verb": "INFLUENCES", "targetSlug": "enlightenment", "targetName": "Enlightenment", "context": "Louis's patronage of arts and sciences created the cultural conditions that fed into Enlightenment thought, even as his absolutism later became a target of critique"},
            {"verb": "INFLUENCES", "targetSlug": "french-revolution", "targetName": "French Revolution", "context": "The wars and debts accumulated under Louis XIV contributed to the long-term fiscal crisis that culminated in the French Revolution"},
            {"verb": "INFLUENCES", "targetSlug": "dutch-republic", "targetName": "Dutch Republic", "context": "Louis's invasion of the Dutch Republic (1672) traumatised the Dutch and transformed their constitutional politics"},
        ],
        places=[
            {"name": "Versailles, France", "role": "built by Louis as his royal palace and seat of government from 1682"},
            {"name": "Paris, France", "role": "capital city and cultural centre under Louis XIV's patronage"},
            {"name": "Saint-Germain-en-Laye, France", "role": "birthplace of Louis XIV in 1638"},
        ],
        frameworks=["EMPIRE_AND_COLONIALISM", "STATE_FORMATION", "COURT_CULTURE", "CAUSE_AND_EFFECT", "RELIGIOUS_THOUGHT", "IDEAS_AND_WORLDVIEWS"],
        subjects=["France", "absolutism", "Sun King", "Versailles", "War of Spanish Succession", "Huguenots", "European diplomacy", "baroque culture"],
        sig_narrative="Louis XIV defined European absolutism, made French the language of civilisation, and built Versailles as a monument to royal power. His seventy-two-year reign remains the longest in European major-monarchy history.",
        sig_category="world-changing",
    )

    # Constantine I
    enrich_simple(
        slug="constantine-i",
        name="Constantine I",
        summary=(
            "Constantine I (c. 272–337 CE), known as Constantine the Great, was the first "
            "Roman Emperor to convert to Christianity and the ruler whose reign transformed "
            "a persecuted minority faith into the empire's officially tolerated — and soon "
            "dominant — religion. His Edict of Milan (313 CE), issued jointly with co-emperor "
            "Licinius, extended religious freedom to all, ending the Great Persecution of "
            "Diocletian. His subsequent military victories over rivals Maxentius (312) and "
            "Licinius (324) reunified the empire under a single Christian emperor.\n\n"
            "Constantine called and presided over the Council of Nicaea (325 CE), the first "
            "ecumenical council of the Christian church, which produced the Nicene Creed — the "
            "foundational statement of orthodox Trinitarian theology still recited by "
            "Catholic, Orthodox, and many Protestant churches today. He founded Constantinople "
            "(330 CE) on the site of Byzantium, a new eastern capital that survived the fall of "
            "Rome by a thousand years as the capital of the Byzantine Empire.\n\n"
            "Constantine's conversion — whether sincere spiritual experience or political "
            "calculation, a debate historians still pursue — permanently altered Western "
            "civilisation. By aligning Roman imperial power with the Christian church, he set in "
            "motion the processes that produced medieval Christendom, the papacy's temporal "
            "authority, and the long entanglement of political and religious power in Europe. "
            "The Eastern Orthodox churches revere him as a saint equal to the apostles."
        ),
        born="c. 272 CE",
        died="337-05-22",
        continent="Europe",
        region="Mediterranean",
        score=9,
        causes=[
            "The Crisis of the Third Century (235–284 CE) so destabilised the Roman Empire that a strong centralising emperor was urgently needed",
            "The Great Persecution under Diocletian (303–313 CE) had paradoxically strengthened Christian identity and martyrdom culture",
            "The Battle of Milvian Bridge (312 CE) — which Constantine attributed to divine Christian aid — created a personal conversion narrative with immense political power",
        ],
        effects=[
            "The Edict of Milan (313 CE) legalised Christianity throughout the Roman Empire, enabling open worship for the first time",
            "The Council of Nicaea (325 CE) established orthodox Trinitarian theology and the model of state-sponsored church councils",
            "The founding of Constantinople (330 CE) created a new eastern Roman capital that preserved Greco-Roman culture through the Byzantine millennium",
            "Constantine's patronage of the church established the precedent of imperial involvement in religious affairs — Caesaropapism — that shaped Byzantine and later European politics",
        ],
        rels=[
            {"verb": "INFLUENCES", "targetSlug": "roman-catholic-church", "targetName": "Roman Catholic Church", "context": "Constantine's patronage and the Edict of Milan transformed Christianity from a persecuted sect to the Roman Empire's favoured religion"},
            {"verb": "INFLUENCES", "targetSlug": "council-of-nicaea", "targetName": "Council of Nicaea", "context": "Constantine called and presided over the First Council of Nicaea (325 CE) which produced the Nicene Creed"},
            {"verb": "INFLUENCES", "targetSlug": "byzantine-empire", "targetName": "Byzantine Empire", "context": "Constantinople, founded by Constantine in 330 CE, became the capital of the Eastern Roman (Byzantine) Empire"},
            {"verb": "INFLUENCES", "targetSlug": "jesus-christ", "targetName": "Jesus Christ", "context": "Constantine's conversion made Christian doctrine a matter of imperial policy, leading to the Council of Nicaea's definition of Christ's divine nature"},
            {"verb": "INFLUENCES", "targetSlug": "roman-empire", "targetName": "Roman Empire", "context": "Constantine reunified the empire under sole rule after defeating Maxentius (312) and Licinius (324)"},
            {"verb": "INFLUENCES", "targetSlug": "medieval-christianity", "targetName": "Medieval Christianity", "context": "Constantine's institutional patronage of the church established the framework for medieval Christendom"},
        ],
        places=[
            {"name": "Constantinople (Istanbul), Turkey", "role": "city founded by Constantine in 330 CE as the new eastern Roman capital"},
            {"name": "Rome, Italy", "role": "Constantine defeated Maxentius at the Milvian Bridge outside Rome in 312 CE"},
            {"name": "Nicaea (Iznik), Turkey", "role": "site of the First Council of Nicaea (325 CE)"},
        ],
        frameworks=["RELIGIOUS_THOUGHT", "EMPIRE_AND_COLONIALISM", "CAUSE_AND_EFFECT", "CIVILIZATIONAL_TRANSFORMATION", "IDEAS_AND_WORLDVIEWS"],
        subjects=["Roman Empire", "Christianity", "Byzantine Empire", "Constantinople", "Council of Nicaea", "Edict of Milan", "Late Antiquity", "emperor"],
        sig_narrative="Constantine I transformed Roman imperial power into a vehicle for Christian expansion, founding Constantinople and sponsoring the Council of Nicaea. His reign is one of the decisive turning points in world religious history.",
        sig_category="world-changing",
    )

    # Christopher Columbus
    enrich_simple(
        slug="christopher-columbus",
        name="Christopher Columbus",
        summary=(
            "Christopher Columbus (c. 1451–1506) was a Genoese-born navigator and explorer "
            "whose four voyages to the Americas (1492–1504), sponsored by the Spanish Crown, "
            "initiated the European colonisation of the Western Hemisphere — one of the most "
            "consequential and catastrophic series of events in human history. On October 12, "
            "1492, Columbus made landfall in the Bahamas, believing he had reached Asia. He died "
            "in 1506 still convinced he had found a westward route to the Indies, unaware he had "
            "'discovered' two continents unknown to European geography.\n\n"
            "Columbus's voyages unleashed the Columbian Exchange — the massive transfer of plants, "
            "animals, diseases, and people between the Old and New Worlds that fundamentally "
            "transformed global ecology, agriculture, and demography. Maize, potatoes, tomatoes, "
            "and tobacco moved from the Americas to Europe and Asia; horses, cattle, smallpox, "
            "and measles moved in the opposite direction. The indigenous population of the Americas "
            "collapsed by an estimated 50–90% within a century due to introduced disease, violence, "
            "and enslavement — one of history's greatest demographic catastrophes.\n\n"
            "Columbus's legacy is profoundly contested. To the European world he opened, he is "
            "celebrated as a visionary navigator; to the descendants of the peoples he encountered, "
            "he represents the beginning of colonialism, forced labour, and genocide. His voyages "
            "inaugurated the Atlantic system of slavery, colonial extraction, and the racial "
            "hierarchies that shaped the modern world."
        ),
        born="c. 1451",
        died="1506-05-20",
        continent="Americas",
        region="Caribbean",
        score=9,
        causes=[
            "The fall of Constantinople (1453) closed the Ottoman-controlled overland spice routes, motivating European powers to seek sea routes to Asia",
            "Portuguese success in African coastal navigation and the rounding of the Cape of Good Hope (1488) created competitive pressure for Spanish exploration",
            "The Reconquista's completion (1492) freed Spanish military and financial resources for overseas expansion",
        ],
        effects=[
            "The Columbian Exchange transformed world agriculture: potatoes, maize, and tomatoes became staple crops across Europe, Africa, and Asia",
            "The demographic collapse of indigenous American populations (est. 50–90% within a century) remains one of the largest mortality events in recorded history",
            "Columbus's voyages initiated the Atlantic slave trade and the plantation economy that fuelled European capitalism for four centuries",
            "The Treaty of Tordesillas (1494) divided the non-European world between Spain and Portugal, establishing the legal framework for European colonialism",
        ],
        rels=[
            {"verb": "INFLUENCES", "targetSlug": "columbian-exchange", "targetName": "Columbian Exchange", "context": "Columbus's voyages initiated the massive biological exchange between the Old and New Worlds"},
            {"verb": "INFLUENCES", "targetSlug": "spanish-empire", "targetName": "Spanish Empire", "context": "Columbus's claim of Caribbean territories for Spain launched the Spanish Empire in the Americas"},
            {"verb": "INFLUENCES", "targetSlug": "transatlantic-slave-trade", "targetName": "Transatlantic Slave Trade", "context": "Columbus's voyages opened the Atlantic system within which the transatlantic slave trade developed"},
            {"verb": "INFLUENCES", "targetSlug": "age-of-exploration", "targetName": "Age of Exploration", "context": "Columbus's 1492 voyage catalysed a century of European exploration and colonisation of the Americas"},
            {"verb": "INFLUENCES", "targetSlug": "ferdinand-and-isabella", "targetName": "Ferdinand and Isabella", "context": "Spanish monarchs Ferdinand II and Isabella I sponsored Columbus's 1492 voyage in exchange for a share of discoveries"},
        ],
        places=[
            {"name": "Genoa, Italy", "role": "birthplace of Columbus, c. 1451"},
            {"name": "San Salvador (Bahamas)", "role": "Columbus's landfall on October 12, 1492 — the first recorded European contact with the Americas"},
            {"name": "Hispaniola (Haiti/Dominican Republic)", "role": "site of Columbus's first permanent settlement; the beginning of European colonisation in the Americas"},
            {"name": "Valladolid, Spain", "role": "where Columbus died in 1506, still claiming his right to govern the territories he discovered"},
        ],
        frameworks=["EMPIRE_AND_COLONIALISM", "DIFFUSION_AND_EXCHANGE", "ENVIRONMENTAL_HISTORY", "CAUSE_AND_EFFECT", "ECONOMIC_SYSTEMS"],
        subjects=["Americas", "exploration", "Spain", "Columbian Exchange", "colonialism", "navigation", "Caribbean", "indigenous peoples"],
        sig_narrative="Columbus's 1492 voyage initiated the European colonisation of the Americas, the Columbian Exchange, and the Atlantic slave trade — three interlocking processes that created the modern world order while devastating indigenous American civilisations.",
        sig_category="world-changing",
    )

    print("\n✅ Batch 66 complete.")
    print("Next step: env $(cat .env | grep -v '^#' | xargs) npx tsx scripts/sync_gateway.ts --local")
