#!/usr/bin/env python3
"""
Batch 19 — 8 entities (Class 343): More Temples + Class 341 Cathedrals
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()


def enrich_entity(folder, prefix, slug, data):
    fname = os.path.join(folder, f"{prefix}{slug}.json")
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


FOLDER_343 = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/343-Class-343"
FOLDER_341 = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/341-Class-341"

ENTITIES = [

    ("343", "mahabodhi-temple-bagan", {
        "summary": (
            "The Mahabodhi Temple at Bagan (မဟာဗောဓိစေတီ, est. c.1215 CE) in Bagan, Myanmar, is a replica of the Mahabodhi Temple at Bodh Gaya, India — built by King Htilominlo of the Pagan Empire as a testament to the Pagan Empire's close relationship with Indian Buddhism and its rulers' ability to replicate the holiest Buddhist site in Southeast Asia. The Bagan Mahabodhi is the most architecturally sophisticated Bodh Gaya replica in the Buddhist world, incorporating local Burmese decorative traditions while faithfully replicating the Indian original's pyramidal tower.\n\n"
            "Bagan (Pagan) at its peak (9th–13th centuries CE) was home to over 10,000 Buddhist temples, pagodas, and monasteries — the most concentrated assemblage of Buddhist architecture in the world — constructed over 200 years by successive Burmese kings in competitive religious patronage. The Mahabodhi Temple at Bagan stands among 3,000+ surviving structures in the Bagan Archaeological Zone, which was designated a UNESCO World Heritage Site in 2019.\n\n"
            "The temple was damaged by the 1975 earthquake and partially restored. As a deliberate replica of Bodh Gaya — the holiest site in Buddhism — the Bagan Mahabodhi reflects the profound influence of Indian Buddhist architectural traditions on Southeast Asian Buddhist practice, and demonstrates the aspiration of Southeast Asian Buddhist kings to bring the merit of pilgrimage to the holiest Indian sites closer to their subjects."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Most sophisticated Bodh Gaya replica in Southeast Asia (est. c.1215 CE); built by King Htilominlo of the Pagan Empire; one of 3,000+ surviving structures in the Bagan Archaeological Zone (UNESCO World Heritage 2019); demonstrates Indian Buddhist architectural influence on Southeast Asian Buddhist kingship.",
            "significanceCategory": "continental"
        },
        "causes": [
            "King Htilominlo's desire to build a replica of the holiest Buddhist site — Bodh Gaya — for Burmese pilgrims who could not undertake the long journey to India, creating a source of equivalent merit within the Pagan Empire",
            "The Pagan Empire's competitive tradition of royal Buddhist patronage — each king building more temples than the last — drove the construction of increasingly ambitious structures including the Mahabodhi replica",
            "The close trade and religious connections between the Pagan Empire and India — including direct contact with Bodh Gaya through Burmese pilgrims — provided the architectural knowledge needed to build a faithful replica"
        ],
        "effects": [
            "The Bagan Mahabodhi established a tradition of Bodh Gaya replicas in Southeast Asian Buddhist countries — subsequently imitated in Sri Lanka, Thailand, and Cambodia — creating a network of 'proxy pilgrimage' sites that brought the merit of India's holiest Buddhist sites within reach of Southeast Asian Buddhists",
            "The temple's survival in the Bagan Archaeological Zone — one of 3,000+ surviving structures — contributed to Bagan's designation as a UNESCO World Heritage Site (2019), one of the most important heritage recognitions in Southeast Asian history",
            "The architectural fusion visible in the Bagan Mahabodhi — Indian pyramidal tower form combined with Burmese decorative traditions — exemplifies the creative synthesis that characterises Southeast Asian Buddhist architecture at its most confident",
            "The 1975 earthquake's damage and subsequent restoration raised significant conservation debates about the appropriate methods for restoring ancient religious structures in active use"
        ],
        "relationships": [
            {"entity": "Mahabodhi Temple (Bodh Gaya)", "relationship": "REPLICA_OF", "note": "The Bagan Mahabodhi is a deliberate replica of Bodh Gaya — the holiest Buddhist site — built for Burmese pilgrims who could not reach India"},
            {"entity": "King Htilominlo (Pagan Empire)", "relationship": "COMMISSIONED_BY", "note": "Htilominlo built the replica (c.1215 CE) as an act of royal Buddhist patronage"},
            {"entity": "Bagan Archaeological Zone (UNESCO)", "relationship": "KEY_MONUMENT_OF", "note": "One of 3,000+ surviving structures in the Bagan UNESCO World Heritage Zone (2019)"},
            {"entity": "Pagan Empire (Myanmar)", "relationship": "ROYAL_PATRONAGE_TRADITION_WITHIN", "note": "The Bagan Mahabodhi is part of the Pagan Empire's competitive tradition of royal Buddhist temple patronage"},
            {"entity": "Indian Buddhist architectural influence (Southeast Asia)", "relationship": "PRIMARY_EXAMPLE_OF", "note": "The temple demonstrates profound Indian Buddhist architectural influence on Southeast Asian Buddhist kingship and practice"}
        ],
    }),

    ("341", "salisbury-cathedral", {
        "summary": (
            "Salisbury Cathedral (Cathedral Church of the Blessed Virgin Mary, est. 1220–1320 CE) in Salisbury, Wiltshire, is the finest example of Early English Gothic architecture and home to the tallest spire in Britain (123 metres) — which has stood for nearly 700 years without a supporting tower below, a feat of medieval structural engineering that baffled later architects. The cathedral was built in just 38 years (the main structure 1220–1258), giving it an architectural unity and stylistic coherence rare among English cathedrals.\n\n"
            "Salisbury Cathedral houses one of the four surviving copies of Magna Carta (1215) — the foundational document of constitutional liberty — in its Chapter House, making it simultaneously one of the great monuments of Gothic architecture and a primary shrine of democratic history. The Chapter House also contains the earliest surviving clock mechanism in the world (c.1386), still in working order.\n\n"
            "The cathedral's setting — in a water meadow surrounded by the River Avon, visible for miles across the Salisbury Plain — inspired John Constable's celebrated paintings (1820s), creating the most iconic image of English cathedral landscape. The cathedral's close — one of England's most complete medieval cathedral precincts — contains the Bishop's Palace, medieval canons' houses, and the 13th-century King's House, preserving an intact picture of medieval ecclesiastical urban life."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Finest Early English Gothic cathedral (est. 1220–1320 CE); tallest spire in Britain (123m, 700 years); one of four surviving Magna Carta copies; world's earliest surviving clock mechanism (c.1386); Constable's iconic landscape paintings; most architecturally unified English cathedral (built in 38 years).",
            "significanceCategory": "continental"
        },
        "causes": [
            "Bishop Richard Poore's decision to relocate the cathedral from the exposed hilltop of Old Sarum to the water meadow below (1220) — creating a completely new cathedral from scratch rather than rebuilding — gave Salisbury its exceptional architectural unity",
            "The rapid construction timeline (1220–1258) — unusually fast for a medieval cathedral — meant a single architectural vision was maintained throughout, producing the most stylistically coherent major Gothic cathedral in England",
            "The 14th-century addition of the spire (c.1320) — rising to 123 metres, the tallest in Britain — tested and eventually exceeded the structural limits of the supporting crossing tower, requiring continuous maintenance including the addition of iron strapping by Christopher Wren in the 17th century"
        ],
        "effects": [
            "Salisbury's spire — 123 metres, the tallest medieval stone spire in Britain — is the supreme achievement of English Gothic structural engineering, demonstrating that medieval builders could raise stone spires to heights that approached the physical limits of masonry construction",
            "The Magna Carta copy at Salisbury Cathedral — one of four surviving originals — makes it a shrine of constitutional history, visited by millions as the physical embodiment of the principle of constitutional liberty",
            "John Constable's paintings of Salisbury Cathedral (especially his 1831 'Salisbury Cathedral from the Meadows') created the defining image of English cathedral landscape, making Salisbury the most visually celebrated cathedral in English art history",
            "The cathedral's water meadow setting — and the preservation of its medieval close — has made Salisbury the model for the English cathedral town, with its spatial relationship between spire, close, and landscape defining how the English cathedral is understood globally"
        ],
        "relationships": [
            {"entity": "Magna Carta (1215)", "relationship": "HOUSES_ONE_OF_FOUR_SURVIVING_COPIES_OF", "note": "Salisbury Cathedral's Chapter House holds one of four surviving Magna Carta originals — a shrine of constitutional history"},
            {"entity": "Early English Gothic architecture", "relationship": "FINEST_EXAMPLE_OF", "note": "Salisbury is the finest example of the Early English Gothic style — its 38-year construction giving it unique stylistic unity"},
            {"entity": "John Constable (painter)", "relationship": "SUBJECT_OF_ICONIC_PAINTINGS_BY", "note": "Constable's Salisbury Cathedral paintings (1820s) created the defining image of English cathedral landscape"},
            {"entity": "Medieval clock mechanism (c.1386)", "relationship": "CONTAINS_WORLD'S_EARLIEST_SURVIVING", "note": "The cathedral's clock (c.1386) is the earliest surviving clock mechanism in the world — still in working order"},
            {"entity": "English cathedral tradition", "relationship": "DEFINING_ARCHITECTURAL_MODEL_OF", "note": "Salisbury's spire, close, and water meadow setting define the paradigmatic English cathedral landscape"}
        ],
    }),

    ("341", "lincoln-cathedral", {
        "summary": (
            "Lincoln Cathedral (Cathedral Church of the Blessed Virgin Mary of Lincoln, est. 1072–1311 CE) in Lincoln, England, was the tallest building in the world from 1311 until 1549 — when its central spire (160 metres) collapsed — holding the title of world's tallest structure for 238 years. For much of the medieval period it was the most visible symbol of English church power, dominating the landscape of Lincolnshire from its hilltop position with three towers visible for over 30 miles across the flat eastern plain.\n\n"
            "Lincoln Cathedral is a supreme example of Gothic architectural development across three centuries: the Norman original (William the Conqueror commissioned it), the Early English nave (1192–1250), the Angel Choir (1256–1280 — considered the supreme achievement of Decorated Gothic), and the central and west towers. The Angel Choir — containing 28 stone angels in the triforium arcade — is regarded as the finest example of 13th-century English Gothic stone carving.\n\n"
            "Lincoln also holds one of the four surviving copies of Magna Carta — displayed in the Lincoln Castle's Victorian prison building. The cathedral's medieval library contains one of the most important collections of medieval manuscripts in England, including the earliest surviving copy of a medieval English musical composition."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Tallest building in the world 1311–1549 (238 years); central spire 160m before collapse (1549); Norman commission by William the Conqueror; Angel Choir — supreme achievement of Decorated Gothic; holds one of four Magna Carta copies; supreme Gothic architectural development across three centuries.",
            "significanceCategory": "continental"
        },
        "causes": [
            "William the Conqueror's commission of the original Norman cathedral (1072) — as part of the broader Norman programme of replacing Saxon ecclesiastical institutions with Norman ones — established Lincoln as the seat of the largest English bishopric",
            "The Norman cathedral's partial collapse (1185 earthquake) and subsequent rebuilding under Bishop Hugh of Avalon (later canonised) — producing the innovative Lincoln Vault in the choir — launched Lincoln's distinctive contribution to Gothic structural experimentation",
            "The addition of the central and west towers in the 14th century — raising the central spire to 160 metres — created the world's tallest structure for 238 years, making Lincoln the supreme visual statement of English Gothic architectural ambition"
        ],
        "effects": [
            "Lincoln's central spire (1311–1549) held the title of world's tallest structure for 238 years — longer than any other medieval structure — making it the most visible monument to Gothic structural ambition in history",
            "The Angel Choir (1256–1280) — with its 28 stone angels in the triforium arcade and its intricate Decorated Gothic carving — established the highest standard of 13th-century English Gothic stone sculpture, influencing subsequent cathedral carving programmes across England",
            "Lincoln's innovative Lincoln Vault (c.1200) — one of the earliest English Gothic rib vaults with decorative non-structural ribs — was a key step in the development of the Decorated Gothic style that characterised English Gothic for a century",
            "Lincoln Cathedral's Magna Carta copy (1215) — displayed in Lincoln Castle — makes Lincoln one of four places in the world that house an original of the foundational constitutional document of English liberty"
        ],
        "relationships": [
            {"entity": "World's tallest building (1311–1549)", "relationship": "WAS_THE", "note": "Lincoln's central spire (160m) was the world's tallest structure from 1311 until its collapse in 1549 — 238 years"},
            {"entity": "William the Conqueror", "relationship": "ORIGINAL_COMMISSION_BY", "note": "William the Conqueror commissioned the original Norman cathedral (1072) as part of the Norman ecclesiastical transformation of England"},
            {"entity": "Angel Choir (Decorated Gothic)", "relationship": "CONTAINS_SUPREME_EXAMPLE_OF", "note": "The Angel Choir (1256–1280) — 28 stone angels in the triforium — is the supreme achievement of Decorated Gothic sculpture"},
            {"entity": "Magna Carta (1215)", "relationship": "HOLDS_ONE_OF_FOUR_SURVIVING_COPIES_OF", "note": "Lincoln holds one of four surviving Magna Carta originals — displayed in Lincoln Castle"},
            {"entity": "English Gothic architecture", "relationship": "KEY_INNOVATION_SITE_OF", "note": "Lincoln's innovative Lincoln Vault (c.1200) was a key step in the development of Decorated Gothic"}
        ],
    }),

    ("341", "wells-cathedral", {
        "summary": (
            "Wells Cathedral (Cathedral Church of Saint Andrew, est. 1175–1490 CE) in Wells, Somerset, is one of the most beautiful Gothic cathedrals in England — with the most spectacular medieval west facade in the country (featuring nearly 300 original medieval sculptures in a two-storey programme of Biblical, apostolic, and royal figures) and the unique 'scissor arches' (inverted strainer arches) at the crossing — the most elegant structural solution to a subsidence problem in medieval architecture.\n\n"
            "The Wells west front (1230–1240) — 45 metres wide and 30 metres high — is the largest sculptural programme on any medieval building in Britain: nearly 300 figures arranged in registers across the screen facade, depicting the resurrection of the dead, Old and New Testament figures, and ranks of angels. Though many figures are damaged, it remains the most complete programme of medieval English religious sculpture in existence and the closest English equivalent to the great French Gothic facade sculpture programmes.\n\n"
            "The scissor arches — inverted double arches inserted into the crossing c.1338 to prevent the crossing tower from collapsing under its own weight — are simultaneously a structural solution and an aesthetic achievement, their figure-of-eight form creating a visual spectacle that has been described as the most beautiful structural element in medieval architecture. Wells also contains the 15th-century astronomical clock, whose mounted knights joust each hour."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Most spectacular medieval west facade in England (est. 1175–1490 CE); 300 original medieval sculptures — largest sculptural programme on any British medieval building; unique scissor arches — the most beautiful structural solution in medieval architecture; 15th-century astronomical clock with jousting knights.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Bishop Reginald de Bohun's initiation of the new Gothic cathedral (1175) — abandoning the Romanesque style simultaneously developing at Canterbury and Winchester — made Wells the first fully Gothic cathedral in England",
            "The crossing tower's subsidence (c.1322–1338) — threatening the entire cathedral with collapse — forced the master mason William Joy to design the scissor arches, creating an emergency structural intervention that became the most celebrated aesthetic element of the cathedral",
            "The ambitious west facade's sculptural programme (1230–1240) — requiring the work of multiple specialist sculptors over a decade — reflected Wells's competition with the great French Gothic cathedrals and the English church's desire to create a facade matching Continental standards"
        ],
        "effects": [
            "The scissor arches at Wells — inserted c.1338 to prevent the crossing tower's collapse — are the most celebrated example of a structural emergency solution becoming an aesthetic masterpiece, demonstrating medieval architects' capacity to transform constraints into creative opportunities",
            "The west facade's nearly 300 sculptures — the most complete medieval sculptural programme in Britain — preserve an irreplaceable record of 13th-century English religious iconography and sculptural style at its most ambitious",
            "Wells's position as the first fully Gothic cathedral in England (1175) means it was the model for the English Gothic transition from Romanesque — influencing subsequent cathedral building across the country",
            "The astronomical clock (c.1390, mechanism c.1392) — with its jousting knights and 24-hour face — is one of the oldest working astronomical clocks in the world and a monument to the medieval integration of astronomical knowledge and religious architecture"
        ],
        "relationships": [
            {"entity": "English Gothic architecture", "relationship": "FIRST_FULLY_GOTHIC_CATHEDRAL_IN", "note": "Wells (from 1175) is the first fully Gothic cathedral in England — the model for the English transition from Romanesque"},
            {"entity": "Scissor arches (William Joy, c.1338)", "relationship": "CONTAINS_MOST_CELEBRATED_EXAMPLE_OF", "note": "The scissor arches — inserted to prevent collapse — are the most celebrated structural emergency turned aesthetic masterpiece in medieval architecture"},
            {"entity": "Medieval English sculpture", "relationship": "LARGEST_PROGRAMME_OF_ON_ANY_BRITISH_MEDIEVAL_BUILDING", "note": "The west facade's 300 sculptures are the largest sculptural programme on any medieval British building — most complete English medieval sculpture record"},
            {"entity": "Medieval astronomical clocks", "relationship": "ONE_OF_OLDEST_EXAMPLES_OF", "note": "The Wells astronomical clock (c.1390) is one of the oldest working astronomical clocks in the world"},
            {"entity": "Somerset cathedral landscape", "relationship": "SPIRITUAL_CENTRE_OF", "note": "Wells Cathedral is the spiritual centre of the smallest city in England, and one of the most beautifully sited medieval cathedrals in Europe"}
        ],
    }),

    ("341", "ely-cathedral", {
        "summary": (
            "Ely Cathedral (Cathedral Church of the Holy and Undivided Trinity, est. Norman structure c.1083–1340 CE) in Ely, Cambridgeshire, is one of the most architecturally spectacular medieval churches in England — dominated by its great octagonal lantern tower (1322–1342), the supreme achievement of medieval Gothic timber and stone engineering, which replaced the original Norman crossing tower after it collapsed in 1322. The 'Ship of the Fens' — as it is known for its dominating silhouette visible across the flat Cambridgeshire landscape — rises above the surrounding fens that made the Isle of Ely one of the most isolated sites in medieval England.\n\n"
            "The Octagon lantern — designed by the cathedral's sacrist Alan of Walsingham — is a feat of structural audacity: an octagonal stone base (20 metres across) supports a wooden lantern (the largest medieval wooden vault in existence) by means of eight massive oak timbers, each weighing 10 tonnes, arranged in a radial structure that has functioned for 680 years without failure. Medieval carpenters, not architects or engineers, solved what was then an unprecedented structural problem.\n\n"
            "Ely Cathedral also contains the Stained Glass Museum (the only dedicated stained glass museum in Britain), a Norman nave of exceptional quality, the 14th-century Lady Chapel (the largest medieval Lady Chapel in England), and the tomb of King Henry III's mother (Queen Joan), making it one of the most historically layered medieval buildings in England."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Octagonal lantern tower (1322–1342) — supreme achievement of medieval Gothic timber engineering; largest medieval wooden vault in existence; 8 oak timbers of 10 tonnes each, standing 680 years; 'Ship of the Fens'; Norman nave; largest medieval Lady Chapel in England; the most audacious structural solution in English Gothic.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The collapse of the original Norman crossing tower (1322) — during building works — created the structural challenge that Alan of Walsingham's octagonal lantern solution transformed into an architectural masterpiece",
            "Alan of Walsingham's decision to replace the collapsed tower with a 20-metre octagonal stone base supporting a timber lantern — rather than rebuilding a conventional four-sided tower — was the crucial creative decision that produced the most daring structural innovation in English Gothic",
            "The Isle of Ely's geographical isolation — surrounded by fens before the 17th-century drainage — concentrated enormous ecclesiastical wealth and ambition in a single cathedral, producing the resources needed for the extraordinary octagonal lantern construction"
        ],
        "effects": [
            "The Octagon lantern — the largest medieval wooden vault in existence, carried by eight 10-tonne oak timbers for 680 years — is the supreme achievement of medieval English timber engineering and demonstrates that medieval carpenters possessed structural intuitions that anticipated modern engineering principles",
            "The lantern's 14 painted medieval figures of Christ and the apostles — visible from below through the 28-metre void — create the most spectacular interior space in English Gothic architecture, transforming a structural problem into a spiritual experience",
            "The 'Ship of the Fens' silhouette — the octagonal tower and western transept visible across the flat Cambridgeshire landscape for 20 miles — created the defining landmark of the Fenland region for 680 years",
            "The Stained Glass Museum at Ely — the only dedicated stained glass museum in Britain — preserves examples of medieval glass from demolished or damaged churches across England, making Ely a repository of medieval visual culture"
        ],
        "relationships": [
            {"entity": "Alan of Walsingham", "relationship": "OCTAGONAL_LANTERN_DESIGNED_BY", "note": "Alan of Walsingham designed the Octagon lantern (1322–1342) — the most audacious structural innovation in English Gothic after the crossing tower collapse"},
            {"entity": "Medieval timber engineering", "relationship": "SUPREME_ACHIEVEMENT_OF", "note": "The Octagon's eight 10-tonne oak timbers supporting the largest medieval wooden vault — standing 680 years — is the supreme achievement of medieval timber engineering"},
            {"entity": "Norman ecclesiastical architecture (England)", "relationship": "IMPORTANT_EXAMPLE_OF", "note": "Ely's Norman nave is one of the finest examples of Norman ecclesiastical architecture in England"},
            {"entity": "Cambridgeshire Fenland landscape", "relationship": "DEFINING_LANDMARK_OF", "note": "The 'Ship of the Fens' — visible 20 miles across the flat Cambridgeshire landscape — has defined the region's identity for 680 years"},
            {"entity": "English stained glass tradition", "relationship": "PRIMARY_MUSEUM_OF", "note": "The Stained Glass Museum at Ely is the only dedicated stained glass museum in Britain — preserving medieval glass from across England"}
        ],
    }),

    ("341", "canterbury-cathedral", {
        "summary": (
            "Canterbury Cathedral (Cathedral and Metropolitan Church of Christ at Canterbury, est. Norman structure c.1070 CE) in Canterbury, Kent, is the mother church of the worldwide Anglican Communion — the seat of the Archbishop of Canterbury, spiritual leader of the 85 million-member global Anglican Communion — and the site of the most famous murder in English medieval history: the assassination of Archbishop Thomas Becket in 1170 CE, which transformed Canterbury into the primary pilgrimage destination in medieval England and inspired Geoffrey Chaucer's Canterbury Tales.\n\n"
            "Canterbury's architectural history spans a millennium: the Roman church (597 CE, St Augustine's first English cathedral), the Norman rebuild (1070s, under Archbishop Lanfranc), the Romanesque choir (1093–1130), the Gothic reconstruction after the 1174 fire (creating the first Gothic building in England), the Black Prince's Chantry, the 15th-century nave, and the Fan Vault of the Trinity Chapel. The Trinity Chapel — built to house Becket's shrine — attracted half a million pilgrims annually in the 14th century, making Canterbury one of the most visited sites in medieval Christendom.\n\n"
            "Thomas Becket's gold and jewel-encrusted shrine was destroyed by Henry VIII in 1538 (yielding 26 wagon-loads of treasure), and his remains were dispersed — but the Trinity Chapel's worn floor tiles, hollowed by a century of kneeling pilgrims, survive as the most eloquent physical evidence of medieval mass pilgrimage. UNESCO World Heritage Site since 1988."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Mother church of the worldwide Anglican Communion; seat of the Archbishop of Canterbury (spiritual leader of 85 million Anglicans); site of Thomas Becket's assassination (1170) — primary medieval English pilgrimage destination; inspired Chaucer's Canterbury Tales; first Gothic building in England (after 1174 fire); UNESCO World Heritage (1988).",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "St Augustine's arrival in Canterbury (597 CE) — sent by Pope Gregory I as a missionary to the Anglo-Saxons — established Canterbury as the seat of the first English archbishopric and the foundation of English Christianity",
            "Thomas Becket's assassination in the cathedral (29 December 1170) — ordered by Henry II in a rage ('Will no one rid me of this turbulent priest?') — created a martyr whose shrine became the most important pilgrimage destination in England, transforming Canterbury's economic and spiritual significance",
            "The 1174 fire's destruction of the choir — and the subsequent rebuilding by French master mason William of Sens — created the first Gothic building in England, making Canterbury the origin of English Gothic architecture"
        ],
        "effects": [
            "Thomas Becket's martyrdom and subsequent canonisation (1173) made Canterbury the primary English pilgrimage destination — attracting half a million pilgrims annually in the 14th century — and the cathedral's shrine the most lucrative religious institution in England until Henry VIII's dissolution",
            "Geoffrey Chaucer's Canterbury Tales (c.1387–1400) — framed as a pilgrimage journey from London to Canterbury — made the cathedral the literary symbol of medieval English society, immortalising the diversity of medieval English life in the most celebrated work of Middle English literature",
            "Canterbury's role as the seat of the Archbishop of Canterbury — who crowns English monarchs at Westminster Abbey and leads the worldwide Anglican Communion — gives it unparalleled institutional significance in the English religious and political constitution",
            "The destruction of Becket's shrine by Henry VIII (1538) — yielding 26 wagon-loads of treasure — was the most dramatic act of the English Reformation's assault on the cult of saints, symbolising the rupture between medieval Catholic and Protestant English religious identity"
        ],
        "relationships": [
            {"entity": "Anglican Communion", "relationship": "MOTHER_CHURCH_OF", "note": "Canterbury Cathedral is the mother church of the worldwide Anglican Communion — seat of the Archbishop of Canterbury, spiritual leader of 85 million members"},
            {"entity": "Thomas Becket", "relationship": "SITE_OF_ASSASSINATION_OF", "note": "Becket was murdered in the cathedral (1170) — creating England's most important medieval martyrdom and pilgrimage destination"},
            {"entity": "Geoffrey Chaucer (Canterbury Tales)", "relationship": "DESTINATION_OF_PILGRIMAGE_IN", "note": "The Canterbury Tales (c.1387–1400) frame the cathedral as the literary symbol of medieval English society"},
            {"entity": "English Gothic architecture", "relationship": "ORIGIN_OF", "note": "The Gothic reconstruction after 1174 — by William of Sens — created the first Gothic building in England"},
            {"entity": "Henry VIII's English Reformation", "relationship": "BECKET_SHRINE_DESTROYED_DURING", "note": "Henry VIII destroyed Becket's shrine (1538) — 26 wagon-loads of treasure — the most dramatic act of the Reformation's assault on saint veneration"}
        ],
    }),

    ("341", "winchester-cathedral", {
        "summary": (
            "Winchester Cathedral (Cathedral Church of the Holy Trinity, Saint Peter, Saint Paul and Saint Swithun, est. 1079–1530 CE) in Winchester, Hampshire, is the longest medieval cathedral in the world (556 metres interior length) and the burial place of some of the most significant figures in English history — including King Canute (Cnut), Queen Emma of Normandy, William Rufus (William II), and the novelist Jane Austen. For much of the early medieval period, Winchester was the capital of England, and the cathedral's importance in English history reflects this royal and administrative centrality.\n\n"
            "Winchester's Norman crypt (1079) is one of the most important Norman architectural spaces in England; the 14th-century nave is the supreme achievement of English Perpendicular Gothic; and the medieval chantry chapels of bishops and kings line the nave and choir in an extraordinary concentration of medieval memorial sculpture. The cathedral also claims the relics of St Swithun — the 9th-century Bishop of Winchester whose legend ('St Swithun's Day' rain prediction) remains the most widely known piece of English meteorological folklore.\n\n"
            "In the early 20th century, the cathedral nearly collapsed: its medieval foundations rested on waterlogged peat, which was drying and compressing. The diver William Walker (1906–1911) spent five years working in complete darkness in flooded tunnels beneath the cathedral, replacing the decayed foundations with concrete — one of the most extraordinary feats of industrial-era structural preservation."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Longest medieval cathedral in the world (556m); burial place of King Canute, Jane Austen, and English royalty; former capital city cathedral; Norman crypt; supreme Perpendicular Gothic nave; St Swithun's relics; William Walker's 1906–1911 underwater foundation rescue — one of the most extraordinary preservation feats in history.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Winchester's position as the capital of the Kingdom of Wessex and of early Norman England — the city where the Domesday Book was compiled and English royal treasuries were kept — created the political and financial resources for a cathedral of exceptional ambition",
            "The medieval burial tradition of English kings at Winchester — beginning with Canute's burial there in 1035 — established the cathedral as a royal mausoleum and political shrine",
            "The drying of the peat foundations (by the early 20th century) — threatening the entire structure — created the emergency that required William Walker's extraordinary five-year underwater rescue operation"
        ],
        "effects": [
            "Winchester's position as the longest medieval cathedral in the world reflects the extraordinary ambition of its Norman and Gothic builders — successive campaigns of construction across 450 years producing a building of unparalleled linear scale",
            "The concentration of royal burials at Winchester — Canute, Emma of Normandy, William Rufus — makes it the primary physical location of early Norman and Anglo-Danish royal history, a more important royal burial site than Westminster for the period 900–1100 CE",
            "William Walker's 1906–1911 underwater rescue — working in complete darkness in flooded tunnels, replacing decayed wooden foundations with 25,800 bags of concrete — is the most extraordinary feat of structural preservation in English architectural history",
            "Jane Austen's burial in Winchester Cathedral (1817) — her grave near the north aisle — has made Winchester a literary pilgrimage destination and transformed the cathedral's meaning for modern visitors"
        ],
        "relationships": [
            {"entity": "Early Norman England (Winchester as capital)", "relationship": "CATHEDRAL_OF_FORMER_CAPITAL_OF", "note": "Winchester was the capital of England under the Normans — the cathedral reflects this former royal and administrative centrality"},
            {"entity": "King Canute (Cnut)", "relationship": "BURIAL_PLACE_OF", "note": "Canute was buried at Winchester (1035) — one of the most important early English royal burials outside Westminster"},
            {"entity": "Jane Austen", "relationship": "BURIAL_SITE_OF", "note": "Jane Austen is buried in Winchester Cathedral (1817) — making it a major literary pilgrimage destination"},
            {"entity": "William Walker (diver)", "relationship": "FOUNDATIONS_RESCUED_BY", "note": "Walker spent 1906–1911 working underwater in complete darkness, replacing the decayed foundations — the most extraordinary preservation feat in English architectural history"},
            {"entity": "English Perpendicular Gothic", "relationship": "SUPREME_NAVE_EXAMPLE_OF", "note": "Winchester's 14th-century nave is the supreme achievement of English Perpendicular Gothic architecture"}
        ],
    }),

    ("341", "santiago-de-compostela", {
        "summary": (
            "Santiago de Compostela Cathedral (Catedral de Santiago de Compostela, est. 1075–1211 CE) in Galicia, northwest Spain, is the claimed burial site of the apostle St James (Santiago) and the destination of the Camino de Santiago (Way of St James) — the most important Christian pilgrimage route of the medieval world, attracting over 300,000 modern pilgrims annually from over 180 countries. The cathedral's baroque facade (Obradoiro, 1738–1750) — twin towers rising above the medieval plaza — is one of the most celebrated images of Spanish architecture globally.\n\n"
            "The medieval Camino de Santiago network — roads converging on Santiago from across Europe (the French Way, the English Way, the Portuguese Way, the Via de la Plata) — created the infrastructure of medieval pilgrimage: pilgrim hospitals, churches, bridges, and hospices built along the routes became the foundation of medieval European charitable and transport institutions. The pilgrimage's role in integrating medieval Europe economically, culturally, and religiously makes the Camino network one of the most important institutional structures of the medieval world.\n\n"
            "The cathedral's botafumeiro — the massive thurible (incense burner) weighing 53 kilograms, suspended from the nave ceiling and swung on a 20-metre arc during major liturgical celebrations by eight red-robed tiraboleiros — is the most spectacular liturgical object in Christian worship, its use originating in the need to fumigate the crowds of medieval pilgrims. UNESCO World Heritage since 1985."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Claimed burial site of the apostle St James; destination of the Camino de Santiago — most important medieval Christian pilgrimage route; 300,000+ modern annual pilgrims from 180 countries; created the medieval European pilgrimage infrastructure; baroque Obradoiro facade — defining image of Spanish architecture; botafumeiro — most spectacular liturgical object in Christian worship; UNESCO World Heritage (1985).",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The discovery (c.830 CE) of what was declared to be the tomb of the apostle James (Santiago) in Galicia — under the reign of King Alfonso II of Asturias — created the theological and political basis for the most important pilgrimage in medieval Western Christianity",
            "Pope Callixtus II's granting of Holy Year status (Año Santo Compostelano) to Santiago — when the feast day of St James (25 July) falls on a Sunday — created a recurring incentive for pilgrimage that has structured the Camino's rhythm for 900 years",
            "The political investment of the Reconquista in the Santiago cult — St James was invoked as 'Santiago Matamoros' (Moor-slayer) in battle — gave the pilgrimage a militant religious dimension that mobilised resources across medieval Christian Europe"
        ],
        "effects": [
            "The Camino de Santiago network — converging routes from France, Portugal, England, and across Spain — created the most extensive medieval European charitable and hospitality infrastructure: pilgrim hospitals, hospices, bridges, churches, and markets along the routes that became the foundation of European social institutions",
            "The cultural exchange along the Camino — carrying Romanesque and Gothic architectural styles, musical traditions, and intellectual ideas from France and Italy into Iberia — was one of the primary conduits through which European cultural innovations crossed the Pyrenees",
            "The modern Camino revival (from the 1980s onward) — growing from 2,500 annual pilgrims in 1986 to 300,000+ by 2019 — is one of the most remarkable religious revivals in the modern world, demonstrating the continued capacity of medieval pilgrimage traditions to address contemporary spiritual needs",
            "The botafumeiro tradition — the 53-kilogram incense burner swung on a 20-metre arc by eight tiraboleiros — is the most dramatic act of Christian liturgical symbolism and has been a defining image of Santiago worship since the 11th century"
        ],
        "relationships": [
            {"entity": "Camino de Santiago pilgrimage routes", "relationship": "DESTINATION_OF", "note": "Santiago Cathedral is the destination of the Camino — the most important medieval Christian pilgrimage route, 300,000+ modern annual pilgrims"},
            {"entity": "Apostle St James (Santiago)", "relationship": "CLAIMED_BURIAL_SITE_OF", "note": "The cathedral claims the tomb of the apostle James — the theological foundation of the entire pilgrimage tradition"},
            {"entity": "Medieval European pilgrimage infrastructure", "relationship": "NETWORK_CENTRED_ON", "note": "The Camino network — hospitals, hospices, bridges, churches — created the most extensive medieval European charitable infrastructure"},
            {"entity": "Botafumeiro (53kg thurible)", "relationship": "CONTAINS_MOST_SPECTACULAR_LITURGICAL_OBJECT_IN", "note": "The botafumeiro — 53kg, 20-metre arc — is the most spectacular liturgical object in Christian worship, swung by eight tiraboleiros"},
            {"entity": "UNESCO World Heritage", "relationship": "INSCRIBED_AS", "note": "Santiago de Compostela (Old Town) inscribed as UNESCO World Heritage (1985)"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 19 — {len(ENTITIES)} entities (Class 343 Temples + Class 341 Cathedrals)")
    for prefix, slug, data in ENTITIES:
        folder = FOLDER_343 if prefix == "343" else FOLDER_341
        print(f"\n→ [{prefix}] {slug}")
        enrich_entity(folder, prefix, slug, data)
    print("\n✓ Done")
