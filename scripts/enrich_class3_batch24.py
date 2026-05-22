#!/usr/bin/env python3
"""
Batch 24 — 8 entities (Class 341): Historic Churches & Cathedrals — Europe & Africa
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()
FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/341-Class-341"
FILE_PREFIX = "341"


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

    ("hagia-irene", {
        "summary": (
            "Hagia Irene (Ἁγία Εἰρήνη, Church of Holy Peace, est. 4th century CE — current structure 6th century) in Istanbul (Constantinople), Turkey, is the oldest surviving church building in Constantinople and one of the oldest Christian churches in continuous existence — predating the more famous Hagia Sophia by two centuries. Built on the site of an earlier pagan temple and first mentioned in the 4th century, the current structure dates to a rebuilding by Emperor Justinian I following its destruction in the Nika Revolt (532 CE) — and thus shares its construction date with the great Hagia Sophia next door.\n\n"
            "Hagia Irene served as the cathedral of Constantinople before the construction of Hagia Sophia — making it the original mother church of Eastern Christianity — and was the site of the Second Ecumenical Council (381 CE), which definitively condemned Arianism, affirmed the Nicene Creed's description of the Holy Spirit, and established Trinitarian orthodoxy as the theological foundation of all subsequent Christianity. Unlike Hagia Sophia, Hagia Irene was never converted to a mosque after the Ottoman conquest of Constantinople (1453) — instead serving as an imperial armoury and museum.\n\n"
            "The church's austere interior — remarkable for the absence of figurative mosaic decoration, with only a large cross in the apse — reflects its post-iconoclasm form (it was redesigned during the iconoclasm controversy), making it an important document of Byzantine theological debates about religious imagery. Hagia Irene now serves as a concert hall for the Istanbul Music Festival — its superb acoustics and historic atmosphere making it one of the most celebrated concert venues in Turkey."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Oldest surviving church in Constantinople (est. 4th century CE, current structure 6th century); predates Hagia Sophia by two centuries; original cathedral of Constantinople before Hagia Sophia; site of Second Ecumenical Council (381 CE) that definitively condemned Arianism and established Trinitarian orthodoxy; never converted to mosque after 1453; austere iconoclasm-era interior; now used as concert hall.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Constantinople's status as the new capital of the Roman Empire (founded 330 CE) required a cathedral commensurate with the imperial city's importance — creating the patronage for a series of large churches, of which Hagia Irene was the first",
            "The Nika Revolt of 532 CE — which destroyed Hagia Irene and the original Hagia Sophia — created the occasion for Justinian I's reconstruction of both churches simultaneously, making them a paired architectural achievement",
            "The iconoclasm controversy (726–843 CE) — which destroyed figurative religious imagery throughout the Byzantine Empire — left Hagia Irene with the austere interior (cross in apse, no figurative mosaics) that distinguishes it from all other major Byzantine churches"
        ],
        "effects": [
            "The Second Ecumenical Council held at Hagia Irene (381 CE) — definitively condemning Arianism and affirming the Nicene-Constantinopolitan Creed — established the theological foundation of Trinitarian Christianity that all subsequent Christian churches share, making Hagia Irene a site of the most consequential doctrinal decision in Christian history",
            "Hagia Irene's survival as a non-religious space after the Ottoman conquest (1453) — serving as an armoury rather than a mosque — means that it preserves its Byzantine Christian spatial character without the disruptions of mosque conversion, making it a unique witness to early Byzantine church design",
            "The church's iconoclasm-era interior — the large cross in the apse replacing the figurative mosaic programme destroyed by iconoclasts — is the best-surviving example of iconoclast church decoration, providing irreplaceable evidence of the Byzantine visual culture during the theological controversy over religious images",
            "The use of Hagia Irene as a concert hall has made its superb acoustic space one of the most celebrated performance venues in Istanbul, demonstrating the adaptive reuse of ancient religious architecture in contemporary cultural life"
        ],
        "relationships": [
            {"entity": "Second Ecumenical Council (Constantinople, 381 CE)", "relationship": "SITE_OF_THE", "note": "The Second Ecumenical Council — definitively condemning Arianism and affirming the Nicene-Constantinopolitan Creed — was held at Hagia Irene"},
            {"entity": "Emperor Justinian I", "relationship": "REBUILT_CURRENT_STRUCTURE_BY", "note": "Justinian I rebuilt Hagia Irene (532 CE) alongside Hagia Sophia after both were destroyed in the Nika Revolt"},
            {"entity": "Hagia Sophia (Constantinople)", "relationship": "PREDECESSOR_CATHEDRAL_TO", "note": "Hagia Irene served as the cathedral of Constantinople before the construction of Hagia Sophia — the original mother church of Eastern Christianity"},
            {"entity": "Byzantine iconoclasm controversy (726–843 CE)", "relationship": "ARCHITECTURAL_EVIDENCE_OF", "note": "The austere cross-in-apse interior — the result of iconoclast redesign — makes Hagia Irene the best surviving example of iconoclast church decoration"},
            {"entity": "Istanbul Music Festival (Hagia Irene concerts)", "relationship": "CONCERT_HALL_FOR", "note": "Hagia Irene's superb acoustics make it one of the most celebrated concert venues in Turkey — an ancient church repurposed as a cultural space"}
        ],
    }),

    ("florence-baptistery", {
        "summary": (
            "The Florence Baptistery (Battistero di San Giovanni, est. 4th–5th century CE, current octagonal structure 11th–13th century) in Florence, Italy, is the most celebrated baptistery in Christendom — famous above all for Lorenzo Ghiberti's bronze doors on the east portal (1425–1452), which Michelangelo called 'the Gates of Paradise'. The Baptistery's three pairs of bronze doors — by Andrea Pisano (south, 1330–1336) and Ghiberti (north, 1403–1424; east, 1425–1452) — constitute the most celebrated programme of figurative bronze relief sculpture in Western art history.\n\n"
            "The Baptistery was the religious centre of medieval Florence — the place where every Florentine citizen was baptised, including Dante Alighieri (baptised 1266) and the entire Medici family. Its white and green marble octagonal exterior — built in the Florentine Romanesque style (11th–13th centuries) — influenced the subsequent development of Renaissance architecture through its geometric clarity and classical proportions. Filippo Brunelleschi used the Baptistery's proportions in his studies for the Florence Cathedral dome (1420–1436) and as the subject for his pioneering experiments in linear perspective (c.1420).\n\n"
            "The famous doors competition of 1401–1402 — won by Lorenzo Ghiberti against Filippo Brunelleschi — is traditionally cited as the founding event of the Florentine Renaissance: the competition demonstrated that sculptural and artistic genius could attract civic patronage on a competitive basis, establishing the institutional framework of Renaissance artistic culture."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Most celebrated baptistery in Christendom (est. 4th–5th century CE, current structure 11th–13th century); Ghiberti's 'Gates of Paradise' (1425–1452) — Michelangelo's phrase; bronze doors competition (1401–1402) — founding event of Florentine Renaissance; Dante Alighieri baptised here (1266); Brunelleschi's perspective experiments used Baptistery; white-green marble influenced Renaissance architecture.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Florence's civic pride and its role as the leading commercial city of medieval Italy created a wealthy merchant class — organised through the wool guild (Arte di Calimala) that funded the Baptistery — whose competitive patronage drove the commissioning of the most ambitious programme of figurative bronze sculpture in medieval Europe",
            "The 1401–1402 competition for the north doors — between Ghiberti, Brunelleschi, Donatello, and four other sculptors — reflected the Florentine guilds' determination to commission the best possible work through open competition, creating the institutional model of competitive artistic patronage that defined Renaissance culture",
            "The Baptistery's position as the sole religious building in Florence where all citizens were baptised — making it the spiritual starting point of every Florentine life — gave it a civic and devotional significance that justified the extraordinary investment in its bronze doors"
        ],
        "effects": [
            "Lorenzo Ghiberti's 'Gates of Paradise' (1425–1452) — ten gilded bronze panels depicting Old Testament scenes in deep spatial relief, using linear perspective for the first time in a large-scale sculptural programme — established the visual language of the Florentine Renaissance and influenced every subsequent generation of European sculptors",
            "The 1401–1402 doors competition — Ghiberti's victory over Brunelleschi — redirected Brunelleschi from sculpture to architecture, producing the greatest architect of the Renaissance whose Florentine Cathedral dome (1420–1436) and other buildings transformed European architectural history",
            "Brunelleschi's use of the Baptistery as the subject for his perspective experiments (c.1420) — demonstrating the mathematical rules of linear perspective through a painted panel of the Baptistery that the viewer compared to its reflection in a mirror — makes the Baptistery the literal site of the invention of perspectival representation that shaped European art for 500 years",
            "The Baptistery's white and green marble geometry — one of the earliest surviving large-scale Florentine buildings — influenced the development of the Florentine Romanesque style that shaped 15th-century Renaissance architecture's preference for geometric clarity and classical proportion"
        ],
        "relationships": [
            {"entity": "Lorenzo Ghiberti", "relationship": "CREATOR_OF_GATES_OF_PARADISE_FOR", "note": "Ghiberti's 'Gates of Paradise' (1425–1452) — 10 gilded bronze panels with perspectival depth — are the supreme achievement of Renaissance bronze relief sculpture"},
            {"entity": "Florentine Renaissance (15th century)", "relationship": "FOUNDING_COMPETITION_SITE_OF", "note": "The 1401–1402 doors competition — traditionally cited as the founding event of the Florentine Renaissance — demonstrated competitive artistic patronage"},
            {"entity": "Filippo Brunelleschi", "relationship": "REDIRECTED_CAREER_OF", "note": "Brunelleschi's loss in the doors competition redirected him to architecture — producing the Florence Cathedral dome and the invention of perspective"},
            {"entity": "Dante Alighieri", "relationship": "BAPTISM_SITE_OF", "note": "Dante was baptised at the Florence Baptistery (1266) — which he called 'my beautiful San Giovanni' in the Divine Comedy"},
            {"entity": "Linear perspective (c.1420 invention)", "relationship": "SUBJECT_OF_FOUNDING_DEMONSTRATION_OF", "note": "Brunelleschi used the Baptistery as the subject for his perspectival panel (c.1420) — the founding demonstration of linear perspective in European art"}
        ],
    }),

    ("albi-cathedral", {
        "summary": (
            "Albi Cathedral (Cathédrale Sainte-Cécile d'Albi, est. 1282–1480 CE) in Albi, France, is the largest brick cathedral in the world — a fortress-church of extraordinary visual power, built by the Catholic Church in the aftermath of the Albigensian Crusade (1209–1229) as a monument of triumphant orthodoxy over the Cathar heresy that had been the dominant religion of the region. The cathedral's design — resembling a fortified castle more than a church, with no transepts, a single massive nave, cylindrical buttress towers, and a defended entrance — embodies the violence of the crusade and the Church's determination to assert its authority over a region it had recently conquered.\n\n"
            "The Albigensian Crusade — called by Pope Innocent III against the Cathar population of Languedoc — was the most brutal religious war in medieval Europe before the Reformation, involving the massacre of thousands of civilians (most notoriously at Béziers in 1209, where the Cistercian legate allegedly said 'Kill them all; God will recognise his own') and the destruction of a distinctive Occitan culture. Albi Cathedral was built on the ruins of the Cathar-sympathetic culture of the Languedoc as an architectural assertion of Catholic triumphalism.\n\n"
            "The cathedral's interior is a visual masterpiece: the entire surface — vault, walls, columns — is covered in a continuous programme of 15th-century Italian-influenced frescoes (the Judgement fresco on the west wall is the largest medieval fresco in France), creating a total environment of unprecedented intensity. The Albi Cathedral and Old Town are a UNESCO World Heritage Site (2010)."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Largest brick cathedral in world (est. 1282–1480 CE); built as monument of Catholic triumphalism after Albigensian Crusade (1209–1229); fortress-church architecture embodies religious violence; built on ruins of Cathar-sympathetic Occitan culture; largest medieval fresco in France on west wall; UNESCO World Heritage Site (2010); embodies politics of medieval heresy and crusade.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Albigensian Crusade (1209–1229) — called by Pope Innocent III to exterminate Catharism in Languedoc — destroyed the Cathar population and created the political vacuum that the Catholic Church filled through the Inquisition and the construction of fortress-churches asserting Catholic authority",
            "The decision to build a cathedral that looked like a fortress — with cylindrical buttress towers, a defended entrance porch, and no transepts — reflected the determination of Albi's Bishop Bernard de Castanet and his successors to create a building that expressed military as much as spiritual power over a recently conquered population",
            "The Italian influence on the cathedral's fresco programme — reflecting the Avignon papacy's (1309–1377) Italian connections and the flourishing of Italian fresco painting at the same time — brought the most advanced European painting tradition to this fortress-church in southern France"
        ],
        "effects": [
            "Albi Cathedral's fortress-church architecture created a new building type — the cathedral as military and religious monument simultaneously — that influenced subsequent ecclesiastical construction in regions contested by religious conflict",
            "The Albigensian Crusade's destruction of Catharism and Occitan culture — with the cathedral as its architectural memorial — constitutes one of the most complete religious and cultural destructions in medieval European history, eliminating a dualist Christian theology and a vernacular literary culture (troubadour poetry) simultaneously",
            "The cathedral's large-scale fresco programme — bringing Italian Renaissance painting techniques north to France — created a model for total interior decoration that influenced subsequent French Gothic cathedral interiors",
            "The UNESCO inscription of Albi Cathedral and Old Town (2010) has made the fortress-church one of the most visited medieval buildings in southern France, transforming its history from a monument of religious violence into a UNESCO cultural heritage landmark"
        ],
        "relationships": [
            {"entity": "Albigensian Crusade (1209–1229)", "relationship": "BUILT_AS_MONUMENT_OF_CATHOLIC_TRIUMPH_OVER", "note": "The cathedral was built (from 1282) by the Catholic Church as architectural assertion of its triumph over Catharism after the Albigensian Crusade"},
            {"entity": "Catharism (Cathar heresy)", "relationship": "BUILT_ON_RUINS_OF_CULTURE_OF", "note": "Albi Cathedral was built on the ruins of the Cathar-sympathetic Occitan culture that the Albigensian Crusade destroyed"},
            {"entity": "Bishop Bernard de Castanet", "relationship": "COMMISSIONED_FORTRESS-DESIGN_BY", "note": "Bishop Bernard de Castanet — Inquisitor of the region — commissioned the fortress-church design expressing both military and spiritual Catholic authority"},
            {"entity": "Largest medieval fresco in France", "relationship": "CONTAINS_THE", "note": "The west wall Judgement fresco — the largest medieval fresco in France — is covered across the interior in a continuous 15th-century fresco programme"},
            {"entity": "UNESCO World Heritage (Albi Episcopal City)", "relationship": "INSCRIBED_AS_PART_OF", "note": "Albi Cathedral and Old Town were inscribed as UNESCO World Heritage in 2010"}
        ],
    }),

    ("cathedral-of-trier", {
        "summary": (
            "Trier Cathedral (Dom St. Peter, Hoher Dom zu Trier, est. 4th century CE, current structure 11th–13th century) in Trier, Germany, is the oldest cathedral in Germany — built on the site of the palace of Helen, mother of Emperor Constantine I, who converted the palace into the first Christian cathedral in the Roman Empire (c.310 CE). The cathedral's history spans more than 1,700 years of continuous Christian use, making it one of the longest-continuously-operating cathedral buildings in the world.\n\n"
            "The cathedral's extraordinary archaeological depth — Roman walls from Constantine's original construction (early 4th century CE) are still visible in the existing fabric, integrated into the Romanesque cathedral built by Archbishop Poppo of Babenberg (1035–1047) — makes it a layered monument to the entire history of Western Christianity. Trier's role as the capital of the Western Roman Empire (from 286 CE under Maximian) and subsequently as the residence of Constantine I created the patronage for the first generation of Constantinian Christian buildings in Europe.\n\n"
            "The cathedral's most celebrated treasure is the Holy Robe (Heiliger Rock) — the seamless tunic of Jesus, said to have been brought to Trier by Helen — which is displayed for pilgrimage on rare occasions (most recently 2012, attracting 500,000 pilgrims). The Cathedral of Trier, together with the Liebfrauenkirche (c.1230) immediately adjacent — one of the earliest Gothic churches in Germany — forms a pair inscribed as UNESCO World Heritage (1986)."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Oldest cathedral in Germany (est. 4th century CE, built on site of Helen's palace c.310 CE); 1,700+ years of continuous Christian use; Roman walls from Constantine's original building still visible; Trier was capital of Western Roman Empire from 286 CE; Holy Robe relic (seamless tunic of Jesus) — pilgrimage destination; adjacent Liebfrauenkirche is one of earliest Gothic churches in Germany; UNESCO World Heritage (1986).",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Emperor Constantine I's conversion of his mother Helen's palace in Trier into the first Christian cathedral in the Roman Empire (c.310 CE) — before the dedication of the Lateran Basilica in Rome (312 CE) — created the foundation of the oldest cathedral site in Germany",
            "Trier's status as the capital of the Western Roman Empire (from 286 CE) — and subsequently as the primary residence of Constantine I — meant that it was the first city in the empire where imperial Christian patronage created a large-scale cathedral",
            "Archbishop Poppo of Babenberg's Romanesque rebuilding (1035–1047) — incorporating the surviving Roman walls from Constantine's original cathedral — created the structure that forms the core of the existing cathedral, establishing Trier's claim as the site of the oldest continuous cathedral in Germany"
        ],
        "effects": [
            "The Cathedral of Trier's archaeological depth — with Roman walls from Constantine's palace visible in the current Romanesque and Gothic fabric — makes it the most complete architectural palimpsest of the entire history of Western Christianity, from the first decade of imperial Christian patronage to the present",
            "The Holy Robe pilgrimage — which drew 500,000 pilgrims to Trier in 2012 — maintains Trier's role as a major Catholic pilgrimage destination in the Rhineland, keeping alive a tradition of pilgrimage to the relic of Christ's seamless tunic that dates to Helen's bringing the robe to Trier in the 4th century",
            "The Liebfrauenkirche (c.1230) immediately adjacent — one of the earliest pure Gothic churches in Germany, built over the older Roman south basilica of Constantine's cathedral complex — makes the Cathedral-Liebfrauenkirche pair the most important architectural ensemble in the Rhineland for the history of Gothic architecture",
            "Trier's extraordinary concentration of Roman and early Christian monuments — the Cathedral, the Porta Nigra, the Aula Palatina, the Roman amphitheatre — makes it the site with the best-preserved evidence of Constantine's Christian empire in northern Europe"
        ],
        "relationships": [
            {"entity": "Constantine I (Roman Emperor)", "relationship": "ORIGINAL_SITE_CREATED_BY", "note": "Constantine I converted his mother Helen's palace into the first Christian cathedral in the Roman Empire (c.310 CE) — the origin of Trier Cathedral"},
            {"entity": "Helen (Helena, mother of Constantine)", "relationship": "PALACE_OF_CONVERTED_INTO_CATHEDRAL_BY", "note": "Helen's palace in Trier was the site of the first Christian cathedral in the Roman Empire — and she is credited with bringing the Holy Robe relic"},
            {"entity": "Holy Robe of Trier (Heiliger Rock)", "relationship": "HOUSES_THE_RELIC_OF", "note": "The Holy Robe — the seamless tunic of Jesus — is the cathedral's primary relic, drawing 500,000 pilgrims in 2012"},
            {"entity": "Liebfrauenkirche Trier (c.1230)", "relationship": "PAIRED_WITH_AS_UNESCO_SITE", "note": "The Liebfrauenkirche — one of the earliest Gothic churches in Germany — and the Cathedral form a UNESCO World Heritage pair (1986)"},
            {"entity": "UNESCO World Heritage (Roman Monuments of Trier)", "relationship": "INSCRIBED_AS_PART_OF", "note": "The Trier Cathedral is part of the Roman Monuments, Cathedral, and Liebfrauenkirche UNESCO inscription (1986)"}
        ],
    }),

    ("erfurt-cathedral", {
        "summary": (
            "Erfurt Cathedral (Dom St. Marien, est. 8th century CE, current Gothic structure 12th–14th century) in Erfurt, Germany, is the cathedral where Martin Luther was ordained as a priest (1507 CE) — and thus one of the most historically significant buildings in the Protestant Reformation. Erfurt was the most important city in Luther's life before his transformation at Wittenberg: he studied at the University of Erfurt (the most distinguished university in Germany in 1501), became an Augustinian friar at the Erfurt monastery (1505), was ordained priest at Erfurt Cathedral (1507), and said his first mass there, before departing for Wittenberg in 1511.\n\n"
            "The cathedral occupies a dramatic hilltop position above the Domplatz — a vast cathedral square that is the largest open space in any German city — and is reached by a monumental staircase of 70 steps. The cathedral and the adjacent Severikirche stand as a paired Gothic ensemble on the hilltop, creating the most impressive cathedral skyline in central Germany. The cathedral's most celebrated treasure is the Gloriosa bell (1497) — the largest free-swinging medieval bell in the world, with a weight of 11.5 tonnes — which strikes only on the most solemn occasions.\n\n"
            "The cathedral's stained glass windows (14th–15th century) — among the best-preserved medieval glass in Germany — include the famous 'Man of Sorrows' window and a programme of figures that constitutes the most complete surviving Gothic stained glass cycle in Thuringia."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Cathedral where Martin Luther was ordained priest (1507 CE); Luther studied at University of Erfurt (1501), became Augustinian friar in Erfurt (1505), said first mass here; Gloriosa bell (1497) — largest free-swinging medieval bell in world (11.5 tonnes); dramatic hilltop position above Germany's largest cathedral square; best-preserved Gothic stained glass cycle in Thuringia.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Erfurt's position as the most important city in Thuringia — a major trading centre and the seat of one of Germany's most distinguished universities (founded 1392) — made it the natural destination for Martin Luther's university studies (1501) and his entry into the Augustinian order (1505)",
            "Luther's spiritual crisis during a thunderstorm (1505) — his vow to become a friar if he survived, and his subsequent entry into the Augustinian monastery in Erfurt — turned the cathedral into the site of his priestly ordination and first mass, making it the institutional starting point of the man who would split Western Christianity",
            "The hilltop position of the cathedral and Severikirche — on the Domhügel above the Domplatz — reflects the medieval urban planning of Erfurt, which created a monumental religious precinct dominating the commercial city below"
        ],
        "effects": [
            "Erfurt Cathedral's role in Martin Luther's formation — university education, Augustinian vows, priestly ordination, first mass — means that it was the institutional context in which the young Luther developed the deep Catholic piety and theological education that would later fuel his reform critique",
            "The Gloriosa bell (1497) — the largest free-swinging medieval bell in the world — became one of the most celebrated medieval craft objects in Germany, a monument to late medieval metalworking achievement that is rung only on the most solemn occasions",
            "The cathedral's Gothic stained glass cycle (14th–15th century) — the most complete surviving in Thuringia — provides irreplaceable visual evidence of late medieval devotional imagery in central Germany, preserving a programme that would have been destroyed in other churches during the Reformation's iconoclasm",
            "The cathedral square (Domplatz) below — the largest cathedral square in Germany — continues to host major public events, including the annual Domplatz Christmas market (one of Germany's most visited) and public concerts, making the cathedral a centre of Erfurt civic life"
        ],
        "relationships": [
            {"entity": "Martin Luther", "relationship": "PRIESTLY_ORDINATION_SITE_OF", "note": "Luther was ordained priest at Erfurt Cathedral (1507) and said his first mass there — part of his Erfurt formation before departing for Wittenberg (1511)"},
            {"entity": "Augustinian Monastery of Erfurt", "relationship": "PAIRED_WITH_AS_LUTHER_FORMATION_SITE", "note": "The Augustinian monastery in Erfurt — where Luther took his vows (1505) — and the cathedral are the two buildings central to Luther's religious formation"},
            {"entity": "University of Erfurt (est. 1392)", "relationship": "CATHEDRAL_CITY_OF_LUTHER'S_UNIVERSITY", "note": "Luther studied at the University of Erfurt (1501–1505) — the most distinguished university in Germany at the time"},
            {"entity": "Gloriosa bell (1497, 11.5 tonnes)", "relationship": "HOUSES_THE_LARGEST_FREE-SWINGING_MEDIEVAL_BELL", "note": "The Gloriosa (1497) — the largest free-swinging medieval bell in the world — is rung only on the most solemn occasions"},
            {"entity": "Protestant Reformation (1517–1648)", "relationship": "KEY_FORMATION_SITE_OF_FOUNDER_OF", "note": "Erfurt Cathedral is one of the key buildings in the formation of Martin Luther — the man who initiated the Protestant Reformation"}
        ],
    }),

    ("naumburg-cathedral", {
        "summary": (
            "Naumburg Cathedral (Dom St. Peter und Paul, Naumburger Dom, est. c.1028 CE, current structure 12th–13th century) in Naumburg, Germany, is one of the most important Gothic cathedrals in Central Europe — celebrated above all for the 12 founder sculptures in the West Choir (c.1240–1260 CE) created by the anonymous 'Naumburg Master', who produced the most naturalistic figurative sculpture in all of medieval European art. The Naumburg Master's sculptures — particularly the figures of Uta of Naumburg and Ekkehard II — are the first portraits in medieval sculpture to convey genuine individual psychological character.\n\n"
            "The Naumburg Master's 12 donor figures — depicting the benefactors of the original cathedral, sculpted two centuries after their deaths — are extraordinary for their individuality and expressive power: Uta of Naumburg (her cape pulled across her face, her eyes cast sideways in a private interior look) has been called the most beautiful woman in German art history and is the most reproduced medieval sculpture in Germany. The Passion Reliefs on the choir screen — depicting Christ's Passion in narrative relief panels — are equally revolutionary, using dramatic foreshortening and emotional intensity that anticipates Italian Proto-Renaissance sculpture by 30 years.\n\n"
            "Naumburg Cathedral was inscribed as a UNESCO World Heritage Site in 2018 — in the same inscription as the Cathedral of Merseburg, the Collegiate Church of Zeitz, and the Collegiate Church of Naumburg — as 'Naumburg Cathedral and the High Medieval Cultural Landscape of the Rivers Saale and Unstrut'."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Most important Gothic cathedral for medieval sculpture (est. c.1028 CE, current structure 12th–13th century); 12 founder sculptures by the 'Naumburg Master' (c.1240–1260 CE) — most naturalistic medieval sculpture in Europe; Uta of Naumburg — 'most beautiful woman in German art history'; first portraits in medieval sculpture with genuine psychological character; UNESCO World Heritage (2018).",
            "significanceCategory": "continental"
        },
        "causes": [
            "The founding of the cathedral (c.1028 CE) by Bishop Hildeward of Zeitz — relocating the bishopric to Naumburg — created the institutional basis for the subsequent development of the cathedral that would become the site of the Naumburg Master's revolutionary sculptures",
            "The decision of the cathedral's chapter to commission donor sculptures (c.1240–1260 CE) depicting the 12 benefactors of the original cathedral — long dead, with no portraits to work from — freed the Naumburg Master from the constraints of portrait likeness, enabling him to invent psychological character rather than record physical appearance",
            "The influence of French Gothic cathedral sculpture (particularly Chartres and Reims) — transmitted to Germany through the trading networks of the High Medieval period — provided the formal vocabulary that the Naumburg Master transformed into the naturalistic style that has no precedent in Northern European sculpture"
        ],
        "effects": [
            "The Naumburg Master's founder sculptures (c.1240–1260) established the first tradition of psychologically individualised sculpture in medieval Europe, anticipating the Proto-Renaissance naturalism of Giovanni Pisano (Italy, c.1280) and Claus Sluter (Netherlands, c.1395) by decades",
            "Uta of Naumburg — the most reproduced medieval sculpture in Germany — became the defining image of medieval female beauty and dignity in the German cultural imagination, inspiring homages from Albrecht Dürer and Georg Trakl to Fritz Lang's portrayal of a Naumburg-inspired figure in 'Die Nibelungen' (1924)",
            "The Naumburg Master's Passion Reliefs on the choir screen — with their dramatic foreshortening, emotional intensity, and narrative fluency — influenced the subsequent development of German Gothic relief sculpture, establishing Thuringia as a centre of sculptural innovation",
            "The UNESCO inscription (2018) connecting Naumburg Cathedral with the High Medieval cultural landscape of the Saale and Unstrut rivers established the regional context of cathedral culture in Saxony-Anhalt, highlighting the extraordinary concentration of Romanesque and Gothic monuments in this region"
        ],
        "relationships": [
            {"entity": "Naumburg Master (anonymous sculptor, c.1240–1260)", "relationship": "SUPREME_ARTISTIC_ACHIEVEMENT_CREATED_BY", "note": "The Naumburg Master's 12 founder sculptures are the most naturalistic and psychologically individual medieval sculptures in Europe"},
            {"entity": "Uta of Naumburg (founder sculpture)", "relationship": "MOST_CELEBRATED_SCULPTURE_IS", "note": "Uta — with her cape across her face, her private sideways gaze — is 'the most beautiful woman in German art history' and the most reproduced medieval sculpture in Germany"},
            {"entity": "Gothic cathedral sculpture (Chartres, Reims)", "relationship": "TRANSFORMED_FRENCH_TRADITION_OF", "note": "The Naumburg Master transformed the French Gothic sculptural vocabulary into a new naturalistic style with no precedent in Northern European sculpture"},
            {"entity": "Fritz Lang's 'Die Nibelungen' (1924)", "relationship": "ARTISTIC_INSPIRATION_FOR", "note": "Uta of Naumburg inspired Fritz Lang's portrayal of Kriemhild in 'Die Nibelungen' — an example of medieval sculpture's influence on 20th-century cinema"},
            {"entity": "UNESCO World Heritage (Naumburg Cathedral, 2018)", "relationship": "INSCRIBED_AS_PART_OF", "note": "UNESCO inscription (2018) — 'Naumburg Cathedral and the High Medieval Cultural Landscape of the Rivers Saale and Unstrut'"}
        ],
    }),

    ("ulm-minster", {
        "summary": (
            "Ulm Minster (Ulmer Münster, est. 1377 CE — spire completed 1890) in Ulm, Germany, has the tallest church steeple in the world — 161.5 metres — and is a Protestant church (since 1531) that was built as a Catholic church by the citizens of Ulm using their own funds, independently of ecclesiastical patronage, over more than 500 years. The minster's spire — begun in 1392, work interrupted in 1543, resumed in 1844, and finally completed in 1890 — required 513 years from laying of foundation stone to completion of the steeple, making it one of the most protracted building campaigns in architectural history.\n\n"
            "The minster is a civic church — built and owned by the city of Ulm rather than the Catholic Church — and thus represents the extraordinary civic pride of a medieval German free imperial city. Its capacity for 20,000 worshippers, its 5-naved interior with the longest nave in Germany (123 metres), and its three-aisled choir with intricate late Gothic vaulting make it one of the largest Gothic churches in Europe. The choir stalls (1469–1474) by Jörg Syrlin the Elder — 89 carved wooden stalls with figures representing pagan Greek and Roman philosophers alongside Christian saints — are the greatest German Gothic woodcarving achievement.\n\n"
            "Albert Einstein was born in Ulm in 1879 — nine years before the spire was completed — creating a biographical connection between the world's tallest church spire and the man who would transform humanity's understanding of space and time."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "World's tallest church steeple at 161.5m (est. 1377 CE, spire completed 1890); Protestant church since 1531; 513-year building campaign; civic church built by citizens of Ulm — not ecclesiastical patrons; 20,000-worshipper capacity; choir stalls (1469–1474) by Jörg Syrlin — greatest German Gothic woodcarving; Albert Einstein born in Ulm (1879), 9 years before spire completed.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The extraordinary wealth and civic pride of Ulm — a free imperial city whose merchants and guild masters organised a building campaign independent of ecclesiastical patronage — created the unique model of a citizen-funded cathedral that took 513 years to complete",
            "The medieval tradition of competition among German cities for the tallest church steeple — Cologne, Vienna, and Strasbourg all had ambitions to build the world's tallest — drove Ulm to design a steeple of unprecedented height, though the 16th-century interruption meant that the world record was achieved only in 1890",
            "The Reformation (Ulm adopted Lutheranism in 1531) — which stopped the steeple's construction and transferred the church to Protestant use — created the anomaly of a Protestant church with a Gothic spire designed by Catholic master builders, resumed and completed by 19th-century neo-Gothic architects"
        ],
        "effects": [
            "The completion of the Ulm Minster spire (1890) — achieving at 161.5 metres the title of world's tallest structure for several years before being surpassed by the Eiffel Tower (1889, 300m) and later by steel towers — made Ulm momentarily the site of the world's most ambitious built structure",
            "The choir stalls (1469–1474) by Jörg Syrlin — depicting pagan philosophers (Ptolemy, Virgil, Cicero) alongside Christian saints — represent the most sophisticated integration of humanist classical culture into Gothic sacred art, anticipating the Renaissance fusion of classical and Christian traditions",
            "The civic model of the Ulm Minster — built and owned by citizens, not the church — established a precedent for the relationship between civic and religious identity in German Protestant cities, becoming the model for subsequent German Protestant parish church building",
            "Albert Einstein's birth in Ulm (1879) — with the world's tallest steeple being completed during his childhood — created a biographical connection between the city of the world's tallest church and the discoverer of general relativity that has made Ulm a site of both architectural and scientific pilgrimage"
        ],
        "relationships": [
            {"entity": "City of Ulm (free imperial city)", "relationship": "BUILT_AND_OWNED_BY_THE", "note": "Ulm Minster was built entirely by citizen funds as a civic church — not by the Catholic Church — representing extraordinary municipal pride"},
            {"entity": "World's tallest church steeple (161.5m)", "relationship": "HOLDS_RECORD_AS_THE", "note": "The 161.5m spire — completed 1890 after a 513-year building campaign — is the tallest church steeple in the world"},
            {"entity": "Jörg Syrlin the Elder (choir stalls, 1469–1474)", "relationship": "GREATEST_WOODCARVING_ACHIEVEMENT_BY", "note": "Syrlin's 89 carved choir stalls — integrating pagan philosophers with Christian saints — are the greatest German Gothic woodcarving achievement"},
            {"entity": "Protestant Reformation (Ulm, 1531)", "relationship": "CONVERTED_TO_PROTESTANT_USE_BY", "note": "Ulm adopted Lutheranism in 1531 — stopping the steeple's construction and transferring the civic church to Protestant use"},
            {"entity": "Albert Einstein", "relationship": "BIRTHPLACE_CITY_OF", "note": "Einstein was born in Ulm in 1879 — 9 years before the world's tallest steeple was completed in his birth city"}
        ],
    }),

    ("abuna-yemata-guh", {
        "summary": (
            "Abuna Yemata Guh (est. 5th–6th century CE) in the Tigray region of Ethiopia is the most inaccessible ancient church in the world — a rock-hewn cave church carved into a sheer cliff face at an altitude of approximately 2,580 metres, accessible only by a 45-minute barefoot climb up a nearly vertical rock face and across narrow ledges with sheer drops of hundreds of metres. The church — dedicated to one of the Nine Saints, the Syrian missionaries who evangelised Ethiopia in the 5th–6th centuries — is entirely carved from the rock of the cliff, with no external walls.\n\n"
            "The church's interior is covered in extraordinary 5th–6th century frescoes — among the oldest Christian frescoes in the world — depicting the Apostles, the Virgin and Child, and scenes from the New Testament in a style that combines Byzantine iconographic convention with distinctively Ethiopian stylistic elements (the characteristic large eyes and frontal gaze of Ethiopian icon tradition). The frescoes are in remarkable condition, preserved by the dry climate and the inaccessibility of the site that has prevented vandalism and mass tourism.\n\n"
            "Abuna Yemata Guh is one of hundreds of rock-hewn churches in the Tigray region — a tradition of church-building that began in the 5th–6th centuries and continued into the medieval period, producing a landscape of sacred architecture entirely hidden within the cliffs. The churches of Lalibela (12th–13th centuries, UNESCO World Heritage) are the most celebrated examples of Ethiopian rock-hewn architecture, but the Tigray churches are older and in many cases more remote."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Most inaccessible ancient church in world (est. 5th–6th century CE); rock-hewn cave church carved into cliff face at 2,580m; accessible only by barefoot climb up nearly vertical rock; among oldest Christian frescoes in world — remarkable condition; one of hundreds of Tigray rock-hewn churches; Ethiopian rock-hewn church tradition begun by Nine Saints (Syrian missionaries, 5th–6th centuries); distinctive Ethiopian-Byzantine fresco style.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Nine Saints — Syrian missionaries who came to Ethiopia in the 5th–6th centuries and retreated to caves and remote cliffs for prayer and ascetic practice — created the tradition of rock-hewn cave churches in the Tigray highlands, carving church spaces into the natural rock rather than constructing freestanding buildings",
            "The Ethiopian tradition of sacred geography — understanding particularly remote, high, and difficult places as closer to God — drove the location of Abuna Yemata Guh at a point accessible only to those willing to undertake a genuinely dangerous climb, creating a physical pilgrimage that mirrors the spiritual challenge",
            "The dry climate of the Tigray highlands — combined with the inaccessibility of the site — created the preservation conditions for frescoes painted 1,400–1,500 years ago to survive in their original colours and composition"
        ],
        "effects": [
            "Abuna Yemata Guh's rock-hewn frescoes (5th–6th century CE) — among the oldest surviving Christian frescoes in the world, in remarkable condition — constitute an irreplaceable visual record of early Ethiopian Christian iconographic tradition",
            "The Tigray rock-hewn church tradition — of which Abuna Yemata Guh is the oldest and most inaccessible example — represents the most geographically dramatic programme of sacred architecture in the world, transforming the Tigray highland cliffs into a landscape of hidden Christian worship",
            "The church's function as an active pilgrimage site — with barefoot climbers from the surrounding community making the dangerous ascent for services — maintains a living tradition of Christian devotion in an unbroken 1,500-year chain from the church's founding to the present",
            "The international discovery of Abuna Yemata Guh by photographers and travel writers in the 21st century — and its subsequent reputation as one of the most dramatically located ancient buildings in the world — has made it a symbol of the extraordinary depth and remoteness of Ethiopian Christian heritage"
        ],
        "relationships": [
            {"entity": "Abuna Yemata (one of the Nine Saints)", "relationship": "DEDICATED_TO_AND_NAMED_FOR", "note": "The church is dedicated to Abuna Yemata — one of the Nine Saints, the Syrian missionaries who evangelised Ethiopia in the 5th–6th centuries"},
            {"entity": "Nine Saints (Syrian missionaries, Ethiopia)", "relationship": "PART_OF_CHURCH-BUILDING_TRADITION_ESTABLISHED_BY", "note": "The Nine Saints established the rock-hewn church tradition of Tigray — carving cave churches into remote cliffs for ascetic retreat and worship"},
            {"entity": "Tigray rock-hewn churches (Tigray, Ethiopia)", "relationship": "OLDEST_AND_MOST_INACCESSIBLE_OF_THE", "note": "Abuna Yemata Guh is the oldest and most inaccessible of the hundreds of rock-hewn churches carved into the Tigray highland cliffs"},
            {"entity": "Ethiopian Orthodox Tewahedo Church", "relationship": "SACRED_PILGRIMAGE_SITE_OF_THE", "note": "The church remains an active pilgrimage site for the Ethiopian Orthodox Tewahedo Church — with worshippers making the dangerous barefoot ascent for services"},
            {"entity": "Lalibela rock-hewn churches (12th–13th century)", "relationship": "OLDER_PRECURSOR_TRADITION_OF", "note": "The Tigray rock-hewn church tradition (including Abuna Yemata Guh) precedes and inspired the more famous Lalibela churches (12th–13th centuries)"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 24 — {len(ENTITIES)} entities (Class 341: Historic Churches & Cathedrals — Europe & Africa)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
