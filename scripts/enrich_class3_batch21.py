#!/usr/bin/env python3
"""
Batch 21 — 8 entities (Class 341): Famous European Cathedrals
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

    ("aachen-cathedral", {
        "summary": (
            "Aachen Cathedral (Aachener Dom, Palatine Chapel est. 792–805 CE; cathedral complex completed 14th century) in Aachen, Germany, is the oldest cathedral in Northern Europe — built by the Emperor Charlemagne as his imperial chapel and the place of coronation for 30 German kings and 12 German queens between 936 and 1531 CE. The Palatine Chapel (Pfalzkapelle) — the octagonal core of the cathedral, constructed 792–805 CE — is the supreme surviving example of Carolingian architecture and the building that gave architectural form to Charlemagne's ambition to revive the Roman Empire in the West.\n\n"
            "The Palatine Chapel's design was directly inspired by the Byzantine church of San Vitale in Ravenna (526–547 CE) — at the instruction of Charlemagne, who sought to create a building worthy of his imperial ambitions by drawing on the architectural traditions of the Eastern Roman Empire. The octagonal plan, the two-storey ambulatory, the mosaics (mostly 19th-century restorations), and the throne of Charlemagne on the upper gallery — from which the Emperor watched Mass — survive as the most complete Carolingian interior in existence.\n\n"
            "Aachen Cathedral was the first site to be inscribed as a UNESCO World Heritage Site in Germany (1978) and holds the shrine of Charlemagne — the Karlsschrein (1215 CE), a gilded reliquary containing his bones that was the primary pilgrimage destination in medieval Germany. Charlemagne was canonised by the antipope Paschal III in 1165 CE, and his cult centred on Aachen made the cathedral the most politically significant religious site in the Holy Roman Empire."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Oldest cathedral in Northern Europe (Palatine Chapel est. 792–805 CE); built by Charlemagne as his imperial chapel; coronation site for 30 German kings and 12 German queens (936–1531); supreme example of Carolingian architecture; inspired by San Vitale Ravenna; contains Charlemagne's Karlsschrein reliquary; first UNESCO World Heritage site in Germany (1978).",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Charlemagne's ambition to build an imperial capital worthy of his revived Western Roman Empire drove the construction of the Palatine Chapel (792–805 CE) — his personal chapel, throne room in heaven, and the architectural symbol of Carolingian imperial power",
            "The direct inspiration from San Vitale in Ravenna — a Byzantine church that Charlemagne visited and admired — created the architectural brief for a building that expressed the fusion of Roman Christian imperial tradition with Frankish military power",
            "The tradition of German kings being crowned at Aachen — established by Otto I (936 CE) as the first post-Carolingian coronation there — created a liturgical and political tradition that locked the cathedral into German royal history for 600 years"
        ],
        "effects": [
            "Aachen Cathedral's Palatine Chapel established the architectural programme of Carolingian imperial church-building that influenced cathedral and palace chapel design across the Holy Roman Empire for three centuries",
            "The coronation tradition at Aachen (936–1531, 30 kings) created the political geography of the Holy Roman Empire — a geography centred on Charlemagne's memory and Aachen's sacred status — giving the cathedral a dynastic significance unmatched by any other German church",
            "The Karlsschrein (1215 CE) — the gilded reliquary of Charlemagne — made Aachen the primary pilgrimage destination in medieval Germany, attracting pilgrims from across the Holy Roman Empire and creating the economic basis for Aachen's medieval prosperity",
            "Aachen's designation as the first UNESCO World Heritage Site in Germany (1978) established it as Germany's primary architectural heritage symbol — the country's most internationally recognised religious building"
        ],
        "relationships": [
            {"entity": "Charlemagne (Emperor of the Carolingian Empire)", "relationship": "BUILT_BY_AND_BURIAL_SITE_OF", "note": "Charlemagne built the Palatine Chapel (792–805 CE) as his imperial chapel and is buried in the Karlsschrein reliquary within the cathedral"},
            {"entity": "San Vitale (Ravenna, Italy)", "relationship": "ARCHITECTURALLY_INSPIRED_BY", "note": "The Palatine Chapel's octagonal design was directly inspired by San Vitale — Charlemagne sought to match Byzantine imperial architecture"},
            {"entity": "German royal coronations (936–1531)", "relationship": "CORONATION_SITE_FOR_30_GERMAN_KINGS_IN", "note": "Aachen was the coronation site for 30 German kings and 12 queens — the primary royal ritual space of the Holy Roman Empire"},
            {"entity": "Karlsschrein reliquary (1215 CE)", "relationship": "HOUSES_THE", "note": "The Karlsschrein — gilded reliquary of Charlemagne — made Aachen the primary pilgrimage destination in medieval Germany"},
            {"entity": "UNESCO World Heritage (Germany)", "relationship": "FIRST_SITE_IN_GERMANY_TO_BE_INSCRIBED_AS", "note": "Aachen Cathedral was the first UNESCO World Heritage Site inscribed in Germany (1978)"}
        ],
    }),

    ("florence-cathedral", {
        "summary": (
            "Florence Cathedral (Cattedrale di Santa Maria del Fiore, begun 1296 CE; dome completed 1436 CE) in Florence, Italy, is the defining monument of the Italian Renaissance and home to the most celebrated architectural feat of the early Renaissance: Filippo Brunelleschi's dome (1420–1436), which remains the largest masonry dome in the world and the first major dome built in Western architecture since the Pantheon (125 CE) — a gap of nearly 1,300 years. Brunelleschi's solution to the engineering problem of raising a dome 55 metres wide and 91 metres high without the use of a temporary wooden centring (which would have required more timber than was available in all of Tuscany) was the defining invention of Renaissance architecture.\n\n"
            "The cathedral's construction spans 140 years: Arnolfo di Cambio began the Gothic structure (1296), Andrea Pisano and Francesco Talenti continued it through the 14th century, and Brunelleschi completed the dome (1420–1436). The dome's innovative double-shell construction — an inner and outer shell connected by herringbone brickwork and a series of internal ribs — solved the structural problem that no medieval builder had been able to resolve. Giorgio Vasari called it 'a feat of engineering that people today find it hard to imagine could have been achieved by the genius of man.'\n\n"
            "The cathedral complex — including the Baptistery of San Giovanni (11th century, with Ghiberti's famous 'Gates of Paradise', 1425–1452), Giotto's Campanile (begun 1334), and the dome — forms the most concentrated ensemble of early Renaissance architecture and art in the world. Michelangelo studied the baptistery doors, Leonardo da Vinci was baptised in the baptistery, and generations of Renaissance artists found the cathedral complex their primary school of architectural and artistic education."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Brunelleschi's dome (1420–1436) — largest masonry dome in the world; first major dome since the Pantheon (1,300-year gap); double-shell construction without wooden centring; begun 1296; Ghiberti's 'Gates of Paradise' in Baptistery; Giotto's Campanile; Michelangelo studied here; most concentrated early Renaissance architectural ensemble in the world.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Florentine commune's decision (1296) to build a cathedral that would 'surpass anything yet built by the Greeks or Romans' — set as a constitutional ambition — created the extraordinary 140-year construction programme that culminated in Brunelleschi's dome",
            "Brunelleschi's invention of single-point perspective (1413–1415) and his study of Roman architectural structures — particularly the Pantheon — provided the intellectual framework for solving the dome's structural problem without a wooden centring",
            "The patronage of the Arte della Lana (wool guild) — the wealthiest Florentine guild, responsible for maintaining the cathedral — provided the financial resources for Brunelleschi's unprecedented construction programme"
        ],
        "effects": [
            "Brunelleschi's dome was the defining invention of Renaissance architecture — establishing that modern builders could surpass the Romans using rational mathematical analysis rather than medieval trial and error, inaugurating the architectural culture of the Renaissance",
            "The dome's double-shell construction and herringbone brickwork established engineering principles that influenced dome construction across Europe for 500 years — most directly influencing Michelangelo's St Peter's dome (1590s) and Wren's St Paul's dome (1710s)",
            "The cathedral complex — Baptistery, Campanile, Cathedral, dome — created the supreme ensemble of early Renaissance art and architecture, making Florence the school of European painting, sculpture, and architecture for two centuries",
            "The dome's completion (1436) was consecrated by Pope Eugenius IV in a ceremony attended by the Council of Florence — the theological council attempting to reunite Eastern and Western Christianity — making it a monument to both architectural and religious ambition at the height of early Renaissance humanism"
        ],
        "relationships": [
            {"entity": "Filippo Brunelleschi", "relationship": "DOME_DESIGNED_AND_BUILT_BY", "note": "Brunelleschi's dome (1420–1436) — the largest masonry dome in the world — was the defining architectural feat of the early Renaissance"},
            {"entity": "Italian Renaissance architecture", "relationship": "FOUNDING_MONUMENT_OF", "note": "The Florence Cathedral dome established that modern builders could surpass the Romans — inaugurating the architectural culture of the Renaissance"},
            {"entity": "Baptistery of San Giovanni (Ghiberti's Gates of Paradise)", "relationship": "ADJOINING_COMPLEX_WITH", "note": "The Baptistery's 'Gates of Paradise' (1425–1452) and the Cathedral form the most concentrated early Renaissance ensemble in the world"},
            {"entity": "Giotto di Bondone (Giotto's Campanile)", "relationship": "CAMPANILE_BEGUN_BY", "note": "Giotto began the Campanile (1334) — the cathedral's bell tower — as one of the finest examples of Italian Gothic decoration"},
            {"entity": "Michelangelo Buonarroti", "relationship": "FORMATIVE_STUDY_SITE_FOR", "note": "Michelangelo studied Ghiberti's Baptistery doors and Brunelleschi's dome — the Cathedral complex was his primary architectural school"}
        ],
    }),

    ("milan-cathedral", {
        "summary": (
            "Milan Cathedral (Duomo di Milano, Cattedrale Metropolitana di Santa Maria Nascente, begun 1386 CE; facade completed 1965 CE) in Milan, Italy, is the largest Gothic cathedral in the world by floor area (11,700 m²), the third largest church building in the world (after St Peter's Basilica and the Seville Cathedral), and the most extravagant Gothic building in Italy — a monument to 600 years of continuous construction, with 3,400 statues, 135 spires (the tallest at 108.5 metres), and a gilded copper Madonna atop the central spire (Madonnina, 1774) that has been the symbol of Milan for 250 years.\n\n"
            "The Duomo was commissioned by Gian Galeazzo Visconti (1386) — the ruler of Milan who sought to build a cathedral that would demonstrate Milan's wealth and cultural ambition equal to any Italian city. The cathedral's unique architectural style — combining northern Gothic forms (flying buttresses, pointed arches, tracery windows) with Italian decorative richness — created what critics call 'Flamboyant Gothic' or 'Rayonnant Gothic' adapted for Italian conditions. The construction employed craftsmen from Germany, France, and across Italy, with major architectural disputes conducted in writing — creating the first surviving corpus of architectural debates in European history.\n\n"
            "The roof terrace — accessible to the public — is one of the most spectacular architectural walks in Europe: a forest of pinnacles, spires, and statues at close quarters, with views across Milan to the Alps on clear days. The cathedral was the site of Napoleon's self-coronation as King of Italy (1805), which he performed personally — placing the Iron Crown on his own head — in imitation of Charlemagne."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Largest Gothic cathedral in world by floor area (begun 1386 CE); 3,400 statues, 135 spires, 600 years of construction; Madonnina — symbol of Milan since 1774; site of Napoleon's self-coronation as King of Italy (1805); first surviving corpus of architectural debates in European history; largest church in Italy.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Gian Galeazzo Visconti's ambition to build a cathedral demonstrating Milan's cultural and economic parity with other Italian cities (1386) — and his willingness to commit marble from the Candoglia quarries in perpetuity to the project — created the financial and political foundation for 600 years of continuous construction",
            "The theological requirement to build a cathedral that could accommodate the entire population of medieval Milan during major liturgical ceremonies drove the extraordinary scale of the building — creating the largest Gothic floor plan in the world",
            "The employment of craftsmen from Germany, France, and across Italy — each with different Gothic building traditions — created the architectural disputes that produced the first surviving written corpus of architectural theory in European history"
        ],
        "effects": [
            "The Milan Cathedral's 600-year construction — from 1386 to 1965 (facade completion) — is the longest continuous cathedral construction in history, making it a monument to the sustained institutional commitment of the Fabbrica del Duomo (the organisation responsible for the cathedral's construction and maintenance since 1387)",
            "The Madonnina (1774) — the gilded copper Madonna atop the central spire — became the symbol of Milan, embedded in Milanese identity to the extent that a Milanese proverb says 'she watches over us' (La Madunina), and no building in Milan was allowed to be taller until the Pirelli Tower (1958)",
            "The written architectural debates of the Milan Cathedral construction — preserving disputes between Italian and northern Gothic approaches — are the earliest surviving written discourse on architectural theory in European history, anticipating Alberti's systematic architectural treatise",
            "Napoleon's self-coronation at the Milan Cathedral (1805) — placing the Iron Crown of Italy on his own head — was one of the most politically theatrical acts of the Napoleonic era, deliberately invoking Charlemagne's coronation as a precedent for Napoleon's European empire"
        ],
        "relationships": [
            {"entity": "Gian Galeazzo Visconti (Duke of Milan)", "relationship": "COMMISSIONED_BY", "note": "Visconti commissioned the Duomo (1386) and dedicated the Candoglia marble quarries to it in perpetuity — the financial foundation for 600 years of construction"},
            {"entity": "Napoleon Bonaparte (King of Italy)", "relationship": "SELF-CORONATION_SITE_OF", "note": "Napoleon placed the Iron Crown of Italy on his own head at the Duomo (1805) — invoking Charlemagne in one of the era's most theatrical acts"},
            {"entity": "Fabbrica del Duomo (est. 1387)", "relationship": "CONTINUOUSLY_MANAGED_BY", "note": "The Fabbrica del Duomo has managed the cathedral's construction and maintenance since 1387 — one of the oldest continuously operating institutions in Italy"},
            {"entity": "European Gothic architectural debates", "relationship": "ORIGIN_OF_FIRST_WRITTEN_CORPUS_OF", "note": "The construction debates (Italian vs northern Gothic approaches) are the earliest surviving written architectural theory discourse in Europe"},
            {"entity": "Madonnina (symbol of Milan)", "relationship": "SUPPORTS_THE", "note": "The Madonnina (1774) atop the central spire has been the symbol of Milan for 250 years — no building was allowed taller until 1958"}
        ],
    }),

    ("seville-cathedral", {
        "summary": (
            "Seville Cathedral (Catedral de Sevilla, formally Catedral de Santa María de la Sede, begun 1402 CE; completed 1519 CE) in Seville, Spain, is the largest Gothic cathedral in the world by interior volume, the largest cathedral in the world by area (11,520 m² under the vault), and the third-largest church in the world. Built on the site of the Almohad Great Mosque of Seville (12th century) — incorporating the mosque's minaret (La Giralda, now the cathedral's bell tower) and its ablution courtyard (now the Patio de los Naranjos, Court of the Oranges) — the cathedral is the supreme monument to the Christian Reconquista and the transformation of Islamic sacred space into Christian holy ground.\n\n"
            "The cathedral canons who commissioned the building reportedly declared: 'Let us build a church so beautiful and so grand that those who see it finished will think we were mad.' Their ambition produced a building of extraordinary scale: five naves, 80 chapels, and the tallest Gothic nave vault in Spain (at 36 metres). The Giralda tower — the mosque minaret converted to a bell tower — at 98 metres is one of the most celebrated architectural transformations of Islamic into Christian architecture in the world.\n\n"
            "Seville Cathedral is the burial site of Christopher Columbus — whose remains (reportedly) rest in an elaborate 19th-century tomb near the south entrance — making it a monument to the Age of Discovery as well as the Reconquista. The cathedral houses the world's largest golden altarpiece (Retablo Mayor, 1482–1564), covering 20 metres × 18 metres, with 44 carved relief panels of gilded wood depicting scenes from the life of Christ and the Virgin Mary."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Largest Gothic cathedral in world by interior volume (begun 1402 CE); built on site of Almohad Great Mosque — supreme monument to the Reconquista; La Giralda (mosque minaret converted to bell tower); burial site of Christopher Columbus; world's largest golden altarpiece (Retablo Mayor); declared UNESCO World Heritage (1987).",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Christian Reconquista's capture of Seville (1248) — and the conversion of the Almohad Great Mosque into a cathedral — established the religious landscape that the new cathedral (1402) would ultimately replace while deliberately incorporating the Islamic Giralda minaret as a trophy of Christian victory",
            "The Castilian crown's desire to demonstrate the permanence and supremacy of Christian rule in Seville — a former Muslim city — drove the decision to build the largest possible Gothic cathedral as the definitive statement of Christian cultural and religious supremacy",
            "Christopher Columbus's connection to Seville — as the port through which the Americas were colonised — and his burial request to be interred in the cathedral created the symbolic connection between the cathedral and the Spanish Age of Discovery"
        ],
        "effects": [
            "Seville Cathedral's scale — the largest Gothic building in the world by interior volume — established it as the physical monument to Castilian royal power in the south of Spain, consolidating the Reconquista's permanence in architectural form for 600 years",
            "The transformation of the Almohad Great Mosque into a cathedral — incorporating the Giralda minaret as a bell tower and the ablution courtyard as the Patio de los Naranjos — is the most celebrated example of 'cultural overwriting' in Iberian architectural history, and a model for subsequent cathedral-over-mosque transformations in Latin America",
            "The burial of Christopher Columbus at Seville Cathedral (officially; the authenticity of the remains is disputed) made it the symbolic home of the Age of Discovery — connecting the Reconquista's completion with the beginning of the Spanish colonial empire",
            "The Retablo Mayor (1482–1564) — 20m × 18m, 44 gilded relief panels — is the largest altarpiece in the world and the supreme example of late Gothic/early Renaissance decorative woodcarving in Spain"
        ],
        "relationships": [
            {"entity": "Almohad Great Mosque of Seville (12th century)", "relationship": "BUILT_ON_SITE_OF", "note": "The cathedral replaced the Almohad mosque (1402) — incorporating the Giralda minaret and Patio de los Naranjos as Christian spaces"},
            {"entity": "Christopher Columbus", "relationship": "CLAIMED_BURIAL_SITE_OF", "note": "Columbus's tomb in the cathedral connects the Reconquista's completion to the beginning of the Spanish colonial Age of Discovery"},
            {"entity": "La Giralda (former minaret)", "relationship": "INCORPORATES_CONVERTED", "note": "La Giralda — the Almohad mosque's 98m minaret (12th century) — converted to the cathedral's bell tower; most celebrated Islamic-to-Christian architectural transformation"},
            {"entity": "Retablo Mayor (1482–1564)", "relationship": "HOUSES_THE_WORLD'S_LARGEST", "note": "The Retablo Mayor — 20m × 18m, 44 gilded panels — is the largest altarpiece in the world"},
            {"entity": "UNESCO World Heritage (Seville)", "relationship": "INSCRIBED_AS", "note": "The Seville Cathedral, Alcázar and Archivo de Indias are a UNESCO World Heritage Site (1987)"}
        ],
    }),

    ("st-pauls-cathedral", {
        "summary": (
            "St Paul's Cathedral (Cathedral Church of Saint Paul, current building est. 1675–1710 CE) in London, England, is the masterpiece of Sir Christopher Wren — the supreme achievement of English Baroque architecture and the building that defined London's skyline for 250 years. The present cathedral replaced Old St Paul's, which was destroyed in the Great Fire of London (1666). Wren's revolutionary design — rejected twice by the cathedral authorities before a compromise 'Warrant Design' was accepted — ultimately produced a building that owes more to Italian Baroque than English Gothic, with a dome (111 metres) inspired by St Peter's Basilica in Rome.\n\n"
            "The dome of St Paul's — the second-largest cathedral dome in the world after St Peter's — houses the Whispering Gallery (30 metres above the floor), where a whisper against the dome's wall can be heard on the opposite side, 34 metres away. The Stone Gallery (53 metres) and the Golden Gallery (85 metres) offer successive views over London. Wren was the first architect to be buried in the building he designed (his tomb bears the inscription 'Lector, si monumentum requiris, circumspice' — 'Reader, if you seek his monument, look around you').\n\n"
            "St Paul's Cathedral's place in British history is unmatched by any other church: the funerals of Admiral Nelson (1806), the Duke of Wellington (1852), Sir Winston Churchill (1965), and Margaret Thatcher (2013) were held here; the wedding of Prince Charles and Lady Diana Spencer (1981) was watched by 750 million television viewers; and the cathedral's survival during the London Blitz (1940–1941) — with the iconic photograph of the dome rising through the smoke of burning London — became the defining symbol of British wartime defiance."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Masterpiece of Christopher Wren (est. 1675–1710 CE); second-largest cathedral dome in world (111m); replaced Old St Paul's destroyed in Great Fire of London (1666); funerals of Nelson, Wellington, Churchill, Thatcher; wedding of Prince Charles and Diana (750m TV viewers); dome rising through Blitz smoke — defining symbol of British wartime defiance; Wren buried in his own building.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Great Fire of London (1666) — which destroyed Old St Paul's along with 87 other London churches — created both the opportunity and the obligation to rebuild the cathedral that had dominated London's skyline for 600 years",
            "Christopher Wren's mathematical and scientific education (astronomy, physics, geometry) — he was Savilian Professor of Astronomy at Oxford before becoming an architect — gave him the technical tools to design a dome without precedent in English architecture",
            "The clash between Wren's Baroque vision (the rejected Great Model and Warrant designs) and the cathedral chapter's conservative preference for Gothic forms produced the compromise design that ultimately allowed Wren sufficient creative freedom to produce his masterpiece"
        ],
        "effects": [
            "St Paul's dome (111 metres) dominated London's skyline for 250 years — creating the urban horizon that generations of Londoners accepted as the natural shape of their city — until the skyscraper era of the 1960s",
            "The survival of St Paul's through the London Blitz (1940–1941) — photographed rising through clouds of smoke as the city burned around it — created the defining image of British wartime resilience, making it the most powerful architectural symbol of the Second World War in Britain",
            "St Paul's became the primary ceremonial space of the British state — funerals of national heroes, royal weddings, thanksgiving services — making it the church of British national identity across 250 years of British history",
            "Wren's triple-shell dome construction — an inner brick cone, a timber outer dome with lead covering, and a stone lantern — solved the structural problem of combining an external silhouette (large dome) with an internal aesthetic (intimate space) in a way that Michelangelo's St Peter's could not, influencing subsequent dome design across Europe and America"
        ],
        "relationships": [
            {"entity": "Christopher Wren", "relationship": "DESIGNED_AND_BURIED_IN", "note": "Wren's masterpiece (1675–1710); he is buried in the crypt with the inscription 'if you seek his monument, look around you'"},
            {"entity": "Great Fire of London (1666)", "relationship": "REBUILT_AFTER_DESTRUCTION_BY", "note": "The Great Fire destroyed Old St Paul's — creating the occasion for Wren's revolutionary Baroque replacement"},
            {"entity": "London Blitz (1940–1941)", "relationship": "SURVIVED_AND_SYMBOLISED_RESISTANCE_TO", "note": "The dome rising through Blitz smoke became the defining image of British wartime defiance"},
            {"entity": "Winston Churchill state funeral (1965)", "relationship": "SITE_OF", "note": "Churchill's funeral at St Paul's (1965) — along with Nelson, Wellington, and Thatcher — established it as the ceremonial stage of British national history"},
            {"entity": "St Peter's Basilica (Rome)", "relationship": "DOME_INSPIRED_BY", "note": "Wren's dome (111m) was inspired by Michelangelo's St Peter's, but solved the triple-shell problem differently and more elegantly"}
        ],
    }),

    ("cathedral-of-santiago-de-compostela", {
        "summary": (
            "The Cathedral of Santiago de Compostela (Catedral de Santiago de Compostela, est. 1075–1211 CE; Baroque facade 1738–1750) in Galicia, northwest Spain, is the claimed burial site of the apostle James (Santiago) and the destination of the Camino de Santiago — the most important Christian pilgrimage route of the medieval world. The cathedral's Baroque Obradoiro facade (1738–1750, by Fernando de Casas Novoa) — twin towers rising above the medieval plaza — is the defining image of Spanish Baroque architecture and one of the most celebrated architectural facades in the world.\n\n"
            "The medieval Camino de Santiago network — roads converging on the cathedral from across Europe (the French Way, the Aragonese Way, the Portuguese Way, the Via de la Plata) — created the infrastructure of medieval European pilgrimage: the hospices, hospitals, churches, and bridges built along the routes became the model for European charitable and hospitality institutions. Over 300,000 pilgrims completed the Camino in 2019 from 180 countries, making it simultaneously the world's most important medieval pilgrimage and a major modern spiritual tourism phenomenon.\n\n"
            "The cathedral's botafumeiro — a massive silver-plated incense burner (botafumeiro, 53 kg) suspended from the dome and swung on a 70-metre arc through the transept by eight red-robed tiraboleiros during major liturgical celebrations — is the most dramatic liturgical spectacle in Christian worship, originating in the medieval need to fumigate crowds of arriving pilgrims. The cathedral has been a UNESCO World Heritage Site since 1985."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Claimed burial site of Apostle James; destination of the Camino de Santiago (most important medieval Christian pilgrimage); Baroque Obradoiro facade (1738–1750); 300,000+ pilgrims from 180 countries in 2019; botafumeiro — most dramatic liturgical spectacle in Christianity; created medieval European pilgrimage infrastructure; UNESCO World Heritage (1985).",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The c.830 CE discovery of what was declared to be the tomb of the Apostle James in Galicia — under King Alfonso II of Asturias — created the theological and political foundation for the most important pilgrimage in medieval Western Christianity, attracting papal endorsement and royal patronage across Europe",
            "Pope Callixtus II's granting of Holy Year status (Año Santo Compostelano) when the feast day of St James (25 July) falls on a Sunday created a recurring incentive for mass pilgrimage that has structured the Camino's rhythm for 900 years",
            "The political investment of the Reconquista in the Santiago cult — St James invoked as 'Santiago Matamoros' (Moor-slayer) in battle — gave the pilgrimage a militant religious dimension that mobilised resources across medieval Christian Europe for centuries"
        ],
        "effects": [
            "The Camino de Santiago network — converging routes from France, Portugal, England, and across Spain — created the most extensive medieval European charitable and hospitality infrastructure: pilgrim hospitals, hospices, bridges, churches, and markets that became the foundation of European social institutions",
            "The cultural exchange along the Camino — carrying Romanesque and Gothic architectural styles, musical traditions, and intellectual ideas from France and Italy into Iberia — was one of the primary conduits through which European cultural innovations crossed the Pyrenees into Spain",
            "The modern Camino revival (from the 1980s, growing from 2,500 annual completions in 1986 to 347,000 in 2019) is one of the most remarkable spiritual tourism revivals in the modern world, demonstrating the continued capacity of medieval pilgrimage traditions to address contemporary needs for meaning and physical challenge",
            "The botafumeiro tradition — the 53kg incense burner swung on a 70-metre arc by eight tiraboleiros — is the most theatrical act of Christian liturgical worship and has been the defining experiential memory of Santiago pilgrimage since the medieval period"
        ],
        "relationships": [
            {"entity": "Camino de Santiago pilgrimage network", "relationship": "DESTINATION_OF_THE", "note": "The cathedral is the destination of the world's most important medieval Christian pilgrimage — 300,000+ modern annual completions from 180 countries"},
            {"entity": "Apostle James (Santiago)", "relationship": "CLAIMED_BURIAL_SITE_OF", "note": "The tomb of St James — discovered c.830 CE — is the theological foundation of the entire pilgrimage tradition"},
            {"entity": "Medieval European pilgrimage infrastructure", "relationship": "NETWORK_OF_HOSPICES_AND_HOSPITALS_CENTRED_ON", "note": "The Camino network created the most extensive medieval European charitable and hospitality infrastructure"},
            {"entity": "Botafumeiro (53kg incense burner)", "relationship": "THEATRICAL_LITURGICAL_CENTREPIECE_OF", "note": "The botafumeiro — swung on a 70m arc by eight tiraboleiros — is the most dramatic liturgical spectacle in Christian worship"},
            {"entity": "UNESCO World Heritage (Santiago de Compostela)", "relationship": "INSCRIBED_AS", "note": "The Old Town of Santiago de Compostela was inscribed as UNESCO World Heritage in 1985"}
        ],
    }),

    ("basilica-of-saint-denis", {
        "summary": (
            "Basilica of Saint-Denis (Basilique royale de Saint-Denis, est. 1135–1144 CE; extended 13th century) in Saint-Denis, near Paris, is the first Gothic building in the world — the building in which Gothic architecture was invented by Abbot Suger of Saint-Denis between 1135 and 1144, whose deliberate application of pointed arches, ribbed vaulting, and stained glass windows to create a unified spatial effect of 'divine light' established the architectural language that would define European sacred architecture for 400 years.\n\n"
            "Abbot Suger's theological programme — expressed in his treatises 'De Administratione' and 'De Consecratione' — held that the beauty of material things could elevate the mind toward the divine, and that the church should therefore be as beautiful as possible. His design for the new choir (1140–1144) — with its novel arrangement of thin columns, large stained glass windows, ribbed vaults, and pointed arches flooding the space with coloured light — was the direct architectural realisation of his theology. 'The noble brightness of the sacred windows,' Suger wrote, 'will illumine my benighted mind.'\n\n"
            "The Basilica of Saint-Denis is also the royal necropolis of France — the burial site of virtually all French kings from the 10th century onward, including Clovis I, Dagobert I, Charles Martel, Louis IX (Saint Louis), Francis I, Henry II, and Catherine de Medici. During the French Revolution (1793), the royal tombs were desecrated and the bones thrown into mass graves — later collected and reinterred by Louis XVIII. The basilica is a UNESCO World Heritage Site."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "First Gothic building in the world (est. 1135–1144 CE); Gothic architecture invented by Abbot Suger as theological programme of 'divine light'; pointed arches, ribbed vaulting, stained glass combined for first time; royal necropolis of France — burial site of virtually all French kings; royal tombs desecrated during French Revolution (1793); UNESCO World Heritage.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Abbot Suger's theology of divine light — derived from the Pseudo-Dionysian tradition that identified light with the divine essence — created the intellectual framework for designing a church that would transform material beauty (coloured light) into spiritual illumination",
            "Suger's access to royal patronage (as advisor to Kings Louis VI and Louis VII of France) provided the financial resources for the architectural experiment that produced the world's first Gothic building",
            "The structural problem of combining large windows with stone vaulting — which required new solutions (pointed arches to control thrust, ribbed vaulting to direct forces) — was solved by Suger's workshop, creating the structural vocabulary that Gothic architecture would deploy for 400 years"
        ],
        "effects": [
            "The Basilica of Saint-Denis established the architectural language of Gothic — pointed arches, ribbed vaults, flying buttresses, large stained glass windows — that defined European sacred architecture from 1144 to the 16th century, producing hundreds of the world's most celebrated buildings",
            "Abbot Suger's written treatises — the first architect's written account of the design and construction of a specific building in European history — established a tradition of architectural self-documentation that influenced subsequent architectural practice and theory",
            "The royal necropolis function — burying virtually all French kings in Saint-Denis from Clovis I onward — made the basilica the dynastic memory of France, its desecration in 1793 (bones thrown into mass graves) one of the most symbolically violent acts of the French Revolution",
            "Gothic architecture's subsequent spread across Europe — from France to England, Germany, Spain, Italy, and Poland — was the direct consequence of Saint-Denis's invention: the building style that invented at Saint-Denis produced Canterbury Cathedral, Cologne Cathedral, Chartres, Reims, Salisbury, and hundreds more"
        ],
        "relationships": [
            {"entity": "Gothic architecture", "relationship": "BIRTHPLACE_OF", "note": "Saint-Denis (1135–1144) is the first Gothic building in the world — where pointed arches, ribbed vaults, and stained glass were first combined into a unified spatial experience"},
            {"entity": "Abbot Suger of Saint-Denis", "relationship": "DESIGNED_BY", "note": "Suger's theology of divine light drove the architectural innovations of the new choir (1140–1144) — the birth of Gothic"},
            {"entity": "Royal necropolis of France", "relationship": "PRIMARY_SITE_OF", "note": "Virtually all French kings from Clovis I onward were buried at Saint-Denis — the dynastic memory of the French monarchy"},
            {"entity": "French Revolution (1793)", "relationship": "ROYAL_TOMBS_DESECRATED_DURING", "note": "The desecration of royal tombs (1793) — bones thrown into mass graves — was one of the most symbolically violent acts of the Revolution"},
            {"entity": "European Gothic cathedrals (Chartres, Reims, Canterbury, Cologne)", "relationship": "ARCHITECTURAL_ORIGIN_OF", "note": "Saint-Denis's invention of Gothic directly spawned Chartres, Reims, Canterbury, Cologne, and hundreds of Gothic cathedrals across Europe"}
        ],
    }),

    ("cathedral-of-magdeburg", {
        "summary": (
            "Magdeburg Cathedral (Hoher Dom zu Magdeburg, Cathedral of Saints Catherine and Maurice, original est. 937 CE; current Gothic structure 1209–1520 CE) in Magdeburg, Germany, is the oldest Gothic cathedral in Germany — begun in 1209, a full generation before Cologne Cathedral (1248) — and was the seat of Archbishop Adalbert, the Apostle of the Slavs, making it the primary religious centre for the Christianisation of Eastern Europe in the 10th century. The cathedral was commissioned by Emperor Otto I as the principal church of his empire, and his tomb (946 CE) makes it an imperial mausoleum of the highest significance.\n\n"
            "The original Ottonian cathedral (937 CE) — built by Emperor Otto I at Magdeburg, the most eastward reach of the Carolingian civilisational sphere — was the gateway through which Christianity, Roman culture, and German institutional power entered Eastern Europe. The subsequent Gothic reconstruction (1209–1520) incorporated the 10th-century crypt and Ottonian foundations, making the cathedral a physical record of German religious history from its Ottonian origins to the Reformation.\n\n"
            "The cathedral contains a notable collection of Romanesque and early Gothic sculpture, including the 13th-century tomb of Queen Editha of England (first wife of Otto I) — the wife of a Saxon king who became Empress of Germany — and the extraordinary bronze doors donated by Archbishop Gero (969 CE), the oldest surviving bronze doors in Germany. The city of Magdeburg and its cathedral were devastated in 1631 during the Thirty Years' War (the sack of Magdeburg), when 20,000 civilians were massacred — the worst single atrocity of the war."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Oldest Gothic cathedral in Germany (Gothic structure from 1209 CE); original Ottonian structure 937 CE by Emperor Otto I; tomb of Otto I — first Holy Roman Emperor; seat of the Christianisation of Eastern Europe; tomb of Queen Editha of England; oldest surviving bronze doors in Germany; city devastated in 1631 (sack of Magdeburg — worst Thirty Years' War atrocity, 20,000 civilians killed).",
            "significanceCategory": "continental"
        },
        "causes": [
            "Emperor Otto I's decision to establish Magdeburg as the eastern outpost of his empire and the centre for the Christianisation of the Slavic peoples drove the construction of the cathedral (937 CE) as the ecclesiastical anchor of German eastward expansion",
            "The archbishopric of Magdeburg — established specifically to support the Christianisation of Eastern Europe — made the cathedral the institutional centre of one of the most significant religious missions in European history",
            "The 13th-century decision to rebuild the Ottonian cathedral in the new Gothic style (from 1209) — beginning before Cologne Cathedral (1248) — made Magdeburg the site of the oldest Gothic cathedral in Germany"
        ],
        "effects": [
            "The Archbishopric of Magdeburg — centred on the cathedral — was the institutional base from which Christianity spread into Eastern Europe (Poland, Bohemia, Hungary, and beyond), making the cathedral the origin point of Central European Christian civilisation",
            "Emperor Otto I's tomb in the cathedral makes it one of the most historically significant imperial burial sites in Germany — the resting place of the ruler who consolidated the German kingdom into the Holy Roman Empire",
            "The sack of Magdeburg (1631) — the worst single atrocity of the Thirty Years' War (20,000 civilians massacred) — brought a new term into European consciousness: 'Magdeburg' became a byword for the total destruction of a city in wartime, and the cathedral's survival amid the ruins was taken as a sign of divine protection",
            "Queen Editha's tomb (13th century, replacing an earlier one) — the burial of an English princess who became Germany's first empress — embodies the international dynastic connections of the Ottonian empire and makes Magdeburg Cathedral a node in Anglo-German medieval history"
        ],
        "relationships": [
            {"entity": "Emperor Otto I (Holy Roman Emperor)", "relationship": "FOUNDED_BY_AND_TOMB_OF", "note": "Otto I commissioned the original cathedral (937 CE) and is buried there — his tomb makes it the most important Ottonian imperial burial site"},
            {"entity": "Christianisation of Eastern Europe (10th century)", "relationship": "PRIMARY_INSTITUTIONAL_BASE_OF", "note": "The Archbishopric of Magdeburg was the centre from which Christianity spread into Poland, Bohemia, and Hungary"},
            {"entity": "Oldest Gothic cathedral in Germany", "relationship": "IS_THE", "note": "Gothic construction began at Magdeburg in 1209 — a generation before Cologne Cathedral (1248) — making it the oldest Gothic cathedral in Germany"},
            {"entity": "Sack of Magdeburg (1631)", "relationship": "SURVIVED_THE", "note": "20,000 civilians were massacred in 1631 — the worst single atrocity of the Thirty Years' War — but the cathedral survived"},
            {"entity": "Queen Editha of England (first wife of Otto I)", "relationship": "TOMB_OF", "note": "Editha's 13th-century tomb — the English princess who became Germany's first empress — embodies Ottonian international dynastic connections"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 21 — {len(ENTITIES)} entities (Class 341: Famous European Cathedrals)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
