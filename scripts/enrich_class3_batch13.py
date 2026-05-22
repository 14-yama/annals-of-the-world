#!/usr/bin/env python3
"""
Batch 13 — 8 entities (Class 340): Religious Orders & Communities
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/340-Class-340"
FILE_PREFIX = "340"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()


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

    ("jesuits", {
        "summary": (
            "The Society of Jesus (Jesuits, est. 1540) is a Catholic religious order founded by St. Ignatius of Loyola and six companions at Paris — approved by Pope Paul III in the bull Regimini Militantis Ecclesiae — and is the world's largest Catholic male religious order with approximately 15,000 members globally. Created as the intellectual vanguard of the Counter-Reformation, the Jesuits are perhaps the most influential educational institution in human history: in 500 years, they established 1,000+ schools, colleges, and universities across five continents, educating hundreds of world leaders, scientists, and artists.\n\n"
            "The Jesuits' Constitutions — Loyola's systematic guide to Jesuit formation, emphasising mental prayer (the Spiritual Exercises), intellectual discipline, adaptability ('accommodation'), and world engagement — created a new religious identity: the 'contemplative in action', simultaneously devoted to God and engaged in the world. The Jesuit missionary project — from Francis Xavier's missions in Japan (1549) to Matteo Ricci's scientific mission to China's imperial court (1582–1610) to the Paraguay Reductions (1610–1767) — was the most ambitious Christian missionary programme in history.\n\n"
            "The Jesuits were suppressed by Pope Clement XIV (1773) under pressure from Bourbon Catholic monarchies who resented Jesuit independence — restored by Pope Pius VII (1814). Their 41-year suppression (during which only Prussia and Russia maintained Jesuit institutions) demonstrated both their political power and the limits of papal and monarchical tolerance for an order of exceptional intelligence and independence."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Catholic religious order (est. 1540); Counter-Reformation intellectual vanguard; 1,000+ schools and universities globally; Matteo Ricci's China mission; Paraguay Reductions; suppressed 1773–1814 by Bourbon monarchies; the most influential educational institution in history; Pope Francis is a Jesuit.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Protestant Reformation (1517) created the Catholic crisis that made the Society of Jesus necessary — the Jesuits were Loyola's response to Protestantism's intellectual challenge, designed to provide Catholic Europe with educated clergy who could compete with Protestant theological sophistication",
            "Ignatius of Loyola's personal spiritual transformation — from Basque soldier wounded at Pamplona (1521) to mystic-intellectual — created the distinctive spirituality of the Spiritual Exercises that became the Jesuit order's foundation and training system",
            "Pope Paul III's support for the Society of Jesus (1540) reflected his recognition that the Council of Trent and institutional reform alone were insufficient to reverse Protestantism — an educated, mobile, socially engaged religious order was needed"
        ],
        "effects": [
            "The Jesuit education system — 1,000+ schools, colleges, and universities across five continents — is the most extensive private educational network in history, producing graduates including René Descartes, Voltaire, James Joyce, Jorge Luis Borges, Alfred Hitchcock, Pope Francis, and hundreds of world leaders",
            "Matteo Ricci's Jesuit mission to China (1582–1610) — presenting Western science, mathematics, and cartography to the Chinese imperial court as a form of cultural evangelism — was the first sustained intellectual encounter between Chinese and European civilisations, influencing Chinese scientific and intellectual development",
            "The Jesuit Paraguay Reductions (1610–1767) — Jesuit-governed communities of Guaraní people in the Río de la Plata region — were the most systematically organised experiment in indigenous social reorganisation in colonial America, admired by Enlightenment thinkers as a model utopia",
            "The Jesuit suppression (1773) — demanded by Bourbon monarchies who resented Jesuit political independence — left Western education and Catholic intellectual life severely weakened for 40 years, demonstrating that the Counter-Reformation's most powerful intellectual force could be destroyed by royal-papal political pressure"
        ],
        "relationships": [
            {"entity": "Ignatius of Loyola", "relationship": "FOUNDED_BY", "note": "Ignatius of Loyola founded the Society of Jesus (1540) — his Spiritual Exercises providing the Jesuit formation system"},
            {"entity": "Counter-Reformation", "relationship": "INTELLECTUAL_VANGUARD_OF", "note": "The Jesuits were created as the Counter-Reformation's intellectual response to Protestantism — the most effective instrument of Catholic renewal"},
            {"entity": "Matteo Ricci", "relationship": "MOST_CELEBRATED_MISSIONARY_OF", "note": "Ricci's China mission (1582–1610) was the most ambitious Jesuit cultural enterprise — the first sustained intellectual encounter between Chinese and European civilisations"},
            {"entity": "Paraguay Reductions (1610–1767)", "relationship": "CREATED_AND_GOVERNED", "note": "The Jesuits created and governed the Paraguay Reductions — the most systematically organised experiment in indigenous social reorganisation in colonial America"},
            {"entity": "Pope Clement XIV (suppression 1773)", "relationship": "SUPPRESSED_BY", "note": "Pope Clement XIV suppressed the Jesuits (1773) under Bourbon pressure — a 41-year suppression that demonstrated the limits of papal tolerance for Jesuit independence"}
        ],
    }),

    ("franciscans", {
        "summary": (
            "The Order of Friars Minor (Franciscans, est. 1209) is a Catholic mendicant religious order founded by St. Francis of Assisi — the most beloved saint in Western Christianity — and is one of the three largest Catholic religious orders globally. Francis's founding vision — radical poverty, preaching, and service to the poor, modelled on his literal reading of the Gospels — created the first 'mendicant' (begging) order: friars who owned nothing individually or collectively and lived by alms and manual labour, a radical departure from the wealth of Benedictine monasteries.\n\n"
            "The Franciscan movement shaped medieval European culture profoundly: Franciscan theologians (Duns Scotus, William of Ockham, Roger Bacon) contributed to the foundations of scholasticism and empirical science; the Franciscan missions in the Americas (from 1524) were the primary vehicle of Spanish colonial evangelisation; the Franciscan promotion of vernacular devotional culture — mystery plays, the stations of the cross, the Christmas crèche — shaped popular Catholic practice globally.\n\n"
            "The 'poverty controversy' that split the Franciscan order in the 14th century — the Spirituals' insistence on absolute poverty versus the Conventuals' accommodation of institutional ownership — was one of the most significant theological controversies of the medieval church, engaging popes and emperors and influencing debates about property, poverty, and power that resonated into the Reformation."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Catholic mendicant order (est. 1209); St. Francis of Assisi — most beloved saint in Western Christianity; first mendicant order; Franciscan theologians (Duns Scotus, William of Ockham) shaped scholasticism and empirical science; Franciscan missions primary vehicle of Spanish colonial evangelisation in the Americas.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Francis of Assisi's personal conversion — from wealthy merchant's son to ascetic preacher, triggered by his experience of poverty, illness, and mystical encounter — created the radical evangelical vision that inspired thousands of followers and the institutional order",
            "The 12th–13th century evangelical awakening — a widespread desire for apostolic poverty and Gospel-centred Christianity across Europe — created the social demand for a new form of religious life that Francis's order answered",
            "Pope Innocent III's approval of Francis's Rule (1209) — giving institutional sanction to a movement that could otherwise have been condemned as heretical (as Catharism was) — integrated the evangelical poverty movement into the Catholic Church rather than allowing it to become a heterodox force"
        ],
        "effects": [
            "The Franciscan missions in Spanish America (1524–) — establishing missions from Mexico to California to Florida — were the primary vehicle of Spanish colonial evangelisation, creating the mission chain (California missions) that shaped the American Southwest's cultural identity",
            "Franciscan theologians William of Ockham (nominalism) and Roger Bacon (empiricism, experimental method) made foundational contributions to medieval philosophy and early science — Bacon's insistence on observation and experiment anticipating the Scientific Revolution by 300 years",
            "The Franciscan promotion of vernacular devotional culture — mystery plays, the stations of the cross, the Christmas crèche (invented by Francis at Greccio, 1223) — shaped popular Catholic religious practice globally, making the Franciscans the most significant influence on Catholic popular piety",
            "The poverty controversy (1317–1323) — Pope John XXII's condemnation of Franciscan absolute poverty — drove William of Ockham to the court of Holy Roman Emperor Louis IV and produced polemical texts on papal authority and property that influenced later Protestant arguments"
        ],
        "relationships": [
            {"entity": "St. Francis of Assisi", "relationship": "FOUNDED_BY", "note": "St. Francis of Assisi founded the Order of Friars Minor (1209) — his radical poverty vision creating the first mendicant order"},
            {"entity": "Spanish colonial missions in the Americas", "relationship": "PRIMARY_VEHICLE_OF", "note": "Franciscan missions were the primary vehicle of Spanish colonial evangelisation in the Americas — from Mexico to California"},
            {"entity": "William of Ockham", "relationship": "PRODUCED_FOUNDATIONAL_PHILOSOPHER", "note": "Ockham's nominalism — developed within the Franciscan intellectual tradition — was foundational to medieval philosophy and ultimately to empiricism"},
            {"entity": "Christmas crèche", "relationship": "INVENTED", "note": "St. Francis invented the Christmas crèche at Greccio (1223) — the Franciscan contribution to popular Catholic practice that spread globally"},
            {"entity": "Poverty controversy (1317–1323)", "relationship": "DIVIDED_BY", "note": "The papal condemnation of absolute Franciscan poverty split the order and drove William of Ockham to produce polemical texts influencing later Protestant arguments"}
        ],
    }),

    ("dominicans", {
        "summary": (
            "The Order of Preachers (Dominicans, est. 1216) is a Catholic mendicant religious order founded by St. Dominic de Guzmán — established to combat heresy through preaching and scholarship — and one of the most intellectually significant religious orders in Western Christianity. Founded with the explicit mission of preaching (hence 'Order of Preachers') and combating the Cathar heresy in southern France, the Dominicans became the intellectual backbone of medieval Catholic theology: their most celebrated member, Thomas Aquinas, produced the Summa Theologica (1265–1274) — the systematic synthesis of Christian theology and Aristotelian philosophy that defined Catholic intellectual life for 500 years.\n\n"
            "The Dominican intellectual tradition — combining rigorous Aristotelian philosophy with Catholic theology — created the Scholastic method that dominated European universities from the 13th to 16th centuries. Albert the Great (Albertus Magnus), Thomas Aquinas's teacher, applied Aristotelian natural philosophy to every domain of human knowledge; Meister Eckhart developed the mystical theology of the Rhineland mystics; Catherine of Siena's letters to Pope Gregory XI contributed to ending the Avignon papacy.\n\n"
            "The Dominicans' most controversial role was as the primary administrators of the Inquisition: established by Pope Gregory IX (1231) to combat heresy through examination, imprisonment, and in extreme cases execution, the Inquisition's Dominican administrators are the most contested figures in the order's history. The Spanish Inquisition (est. 1478) — formally separate but staffed largely by Dominicans — executed an estimated 3,000–5,000 people over 350 years."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Catholic mendicant order (est. 1216); Order of Preachers combating heresy through scholarship; Thomas Aquinas (Summa Theologica) defined Catholic intellectual life for 500 years; Albert the Great; primary Inquisition administrators; Bartolomé de las Casas championed indigenous rights in the Americas.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Cathar heresy in southern France — a dualist Christian sect rejecting the material world and the Catholic Church's authority — created the crisis that motivated Dominic de Guzmán to found a preaching order capable of combating heresy through argument rather than violence alone",
            "Pope Innocent III's recognition that the Cathar heresy could not be suppressed by crusade alone (the Albigensian Crusade, 1209–1229, was brutal but inconclusive) created the need for educated preachers who could engage heretics intellectually",
            "The 13th-century recovery of Aristotle's works — through Arabic translations from Spain — created a philosophical crisis in European universities that the Dominicans (particularly Thomas Aquinas) were positioned to resolve through the Scholastic synthesis of Aristotle and Christian theology"
        ],
        "effects": [
            "Thomas Aquinas's Summa Theologica (1265–1274) — the systematic synthesis of Christian theology and Aristotelian philosophy — defined Catholic intellectual life for 500 years and remains the authoritative statement of Catholic doctrine, making Aquinas's work the most consequential theological text in Western Christianity",
            "The Dominican administration of the medieval Inquisition — examining suspected heretics, imposing penances, and in extreme cases handing over to secular authorities for execution — is the most contested aspect of medieval Catholic history and shapes perceptions of the Church's relationship with intellectual dissent",
            "Bartolomé de las Casas's Dominican advocacy for indigenous rights in Spanish America — his 'A Short Account of the Destruction of the Indies' (1542) and his debates with Juan Ginés de Sepúlveda — was the first systematic European argument for indigenous rights and influenced the New Laws of 1542 limiting the encomienda system",
            "Albert the Great (Albertus Magnus) — applying Aristotelian natural philosophy to every domain of human knowledge — was a foundational figure in the development of medieval natural science, making the Dominican intellectual tradition central to the origins of Western science"
        ],
        "relationships": [
            {"entity": "St. Dominic de Guzmán", "relationship": "FOUNDED_BY", "note": "Dominic founded the Order of Preachers (1216) to combat Cathar heresy through preaching and scholarship"},
            {"entity": "Thomas Aquinas", "relationship": "MOST_CELEBRATED_THEOLOGIAN_OF", "note": "Aquinas — Dominican friar — wrote the Summa Theologica (1265–1274), defining Catholic intellectual life for 500 years"},
            {"entity": "Medieval Inquisition", "relationship": "PRIMARY_ADMINISTRATORS_OF", "note": "Dominicans were the primary administrators of the medieval Inquisition — the most controversial aspect of Dominican history"},
            {"entity": "Bartolomé de las Casas", "relationship": "CHAMPIONED_INDIGENOUS_RIGHTS_THROUGH", "note": "Las Casas — Dominican friar — made the first systematic European argument for indigenous rights in Spanish America"},
            {"entity": "Scholasticism", "relationship": "INTELLECTUAL_BACKBONE_OF", "note": "The Dominican intellectual tradition created Scholasticism — the dominant method of European university education from the 13th to 16th centuries"}
        ],
    }),

    ("benedictines", {
        "summary": (
            "The Order of Saint Benedict (Benedictines, est. c.529 CE) is a Catholic monastic order founded on the Rule of Saint Benedict — the most influential document in Western monasticism — which established the principles of communal religious life ('ora et labora', pray and work) that shaped European civilisation during the Middle Ages. Founded by Benedict of Nursia at Monte Cassino (c.529 CE), the Benedictine tradition spread across Europe through its daughter abbeys, providing the primary institutions of education, agriculture, hospitality, and intellectual life during the 'Dark Ages' following the Roman Empire's collapse.\n\n"
            "The Benedictine monasteries were the civilisational infrastructure of early medieval Europe: they preserved classical learning (copying manuscripts in their scriptoria), pioneered new agricultural techniques (clearing forests, draining swamps, developing viticulture), established the first systematic hospitals and hospitality networks, and educated the clergymen who administered both Church and state. Without Benedictine monasticism, the intellectual heritage of Greece and Rome would likely have been largely lost to Western Europe.\n\n"
            "The Rule of Saint Benedict — with its balanced schedule of prayer, work, and reading, its emphasis on stability (monks remain in one community for life), obedience, and conversatio morum (ongoing conversion) — created the institutional model that all subsequent Western monastic orders adapted. Benedictine reform movements (Cluny, c.910; Cistercians, 1098; Camaldolese, 1023) repeatedly renewed Christian monasticism across the medieval period."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Western monasticism's foundational order (est. c.529); the Rule of Saint Benedict is the most influential document in Western monasticism; Benedictine monasteries preserved classical learning, pioneered agriculture, and were early medieval Europe's civilisational infrastructure; patron saint of Europe.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Roman Empire's collapse in Western Europe (476 CE) — destroying the institutional infrastructure of education, administration, and culture — created the civilisational void that Benedictine monasteries filled, providing the institutional continuity that preserved Roman and Christian intellectual heritage",
            "Benedict of Nursia's personal experience of communal monasticism — his study of earlier monastic rules (particularly the Rule of the Master) and his 30 years of monastic leadership at Monte Cassino — produced the balanced, humane, and practical Rule that proved far more sustainable than earlier ascetic extremism",
            "Pope Gregory the Great's 'Life of Saint Benedict' (Dialogues, Book II, c.594) — which publicised Benedict's life and Rule — was the primary vehicle for Benedictine monasticism's spread, making Gregory's patronage essential to the Benedictine tradition's European diffusion"
        ],
        "effects": [
            "Benedictine scriptoria preserved the classical heritage of Greece and Rome — monks copying manuscripts including Virgil, Cicero, Plato, and Aristotle — providing the textual transmission that made the Renaissance recovery of classical learning possible",
            "Benedictine agriculture — clearing forests, draining swamps, developing viticulture and brewing, and pioneering crop rotation — was the primary force in the agricultural transformation of Northern and Central Europe in the early medieval period",
            "The Benedictine educational network — abbey schools providing the primary education for clergy, administrators, and noble sons — was the dominant educational system in Western Europe from the 6th to the 12th centuries, before the rise of urban cathedral schools and universities",
            "Benedictine reform movements (Cluniac reform, c.910; Cistercian reform, 1098) — periodically renewing Benedictine observance by returning to stricter adherence to the Rule — were the primary engines of Catholic church reform in the medieval period, influencing the papacy and the entire church"
        ],
        "relationships": [
            {"entity": "St. Benedict of Nursia", "relationship": "FOUNDED_BY", "note": "Benedict of Nursia wrote the Rule (c.529) and established Monte Cassino — the foundational text and institution of Western monasticism"},
            {"entity": "Rule of Saint Benedict", "relationship": "GOVERNED_BY", "note": "The Rule of Saint Benedict — the most influential document in Western monasticism — governs the Benedictine order's daily life"},
            {"entity": "Monte Cassino Abbey", "relationship": "MOTHER_HOUSE_OF", "note": "Monte Cassino (est. c.529) is the Benedictine order's mother house — founded by Benedict himself"},
            {"entity": "Cluniac reform (c.910)", "relationship": "RENEWED_BY", "note": "The Cluniac reform movement renewed Benedictine observance and extended Benedictine influence across Europe"},
            {"entity": "European civilisation (medieval)", "relationship": "CIVILISATIONAL_INFRASTRUCTURE_PROVIDED_FOR", "note": "Benedictine monasteries were early medieval Europe's civilisational infrastructure — preserving classical learning, pioneering agriculture, and educating its leaders"}
        ],
    }),

    ("al-azhar-university", {
        "summary": (
            "Al-Azhar (الأزهر, est. 970/972 CE) is the world's oldest continuously operating university and the most important institution in Sunni Islamic scholarship — a mosque-university complex in Cairo founded by the Fatimid caliph al-Mu'izz li-Din Allah that has served for over 1,000 years as the pre-eminent authority on Islamic theology, jurisprudence, and education. Named 'The Resplendent' (al-azhar), it was originally a Shi'a institution under the Fatimids but became the centre of Sunni learning under Saladin (12th century) and has remained so since.\n\n"
            "Al-Azhar's intellectual authority extends across the 1.8 billion-person Sunni Muslim world: its fatwas (religious legal opinions) and curriculum are regarded as authoritative by Muslims from Morocco to Indonesia. Its graduates include religious scholars, judges, politicians, and intellectual leaders across 50+ Muslim-majority countries. Al-Azhar's position on controversial issues — suicide bombing, interfaith dialogue, women's rights in Islamic law, relations with non-Muslim governments — shapes Islamic practice and discourse globally.\n\n"
            "Al-Azhar's relationship with the Egyptian state has been complex: the Khedive Muhammad Ali's educational reforms (1820s) reduced its influence; Nasser nationalised it (1961); and successive Egyptian governments have both used Al-Azhar's religious authority for political legitimation and sought to control it. Grand Imam Ahmad al-Tayyeb's leadership (from 2010) has focused on interfaith dialogue, most notably the Abu Dhabi Declaration (2019) with Pope Francis on human fraternity."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's oldest continuously operating university (est. 970 CE); the pre-eminent Sunni Islamic scholarly authority; its fatwas shape practice across 1.8 billion Muslims; 1,000+ years of continuous operation; Al-Tayyeb's Abu Dhabi Declaration (2019) with Pope Francis is the most significant Islamic-Christian dialogue document of the 21st century.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Fatimid caliphate's founding of Cairo (970 CE) and their desire for an institution that would propagate Ismaili Shi'a Islam — as a counterweight to Abbasid Sunni Baghdad — created the mosque-university complex whose longevity and intellectual prestige would far outlast its Fatimid founders",
            "The Islamic intellectual tradition's integration of theology, jurisprudence (fiqh), Quran interpretation (tafsir), and hadith studies into a systematic educational curriculum created the content that Al-Azhar taught and preserved across millennia",
            "Saladin's (Salah al-Din's) transformation of Al-Azhar from Fatimid Shi'a to Sunni institution (1171) — suppressing the Fatimid caliphate and converting Al-Azhar to Shafi'i Sunni jurisprudence — established the Sunni character that has made it the pre-eminent authority for 1.8 billion Sunni Muslims"
        ],
        "effects": [
            "Al-Azhar's curriculum — Islamic theology, Quran, hadith, jurisprudence, Arabic — has shaped the education of Islamic scholars across 50+ Muslim-majority countries for 1,000 years, making it the primary vehicle of Sunni Islamic intellectual continuity",
            "Al-Azhar's fatwa authority — its religious legal opinions on everything from banking to bioethics to political violence — shapes Islamic practice globally, with each Grand Imam's positions on contemporary issues closely watched by 1.8 billion Muslims",
            "Nasser's nationalisation of Al-Azhar (1961) — making its faculty state employees and introducing secular disciplines — is the paradigmatic case of the tension between state control and religious scholarly independence in Muslim-majority countries",
            "Grand Imam al-Tayyeb's Abu Dhabi Declaration with Pope Francis (2019) — asserting human fraternity and opposing violence in the name of religion — is the most significant Islamic-Christian dialogue document of the 21st century, reflecting Al-Azhar's unique authority to speak for Sunni Islam"
        ],
        "relationships": [
            {"entity": "Fatimid Caliphate", "relationship": "FOUNDED_BY", "note": "Al-Azhar was founded by the Fatimid caliph al-Mu'izz (970/972 CE) — originally as a Shi'a institution"},
            {"entity": "Saladin (Salah al-Din)", "relationship": "CONVERTED_TO_SUNNI_INSTITUTION_BY", "note": "Saladin converted Al-Azhar to Sunni (Shafi'i) Islam (1171) — establishing the Sunni character that has persisted for 850 years"},
            {"entity": "Sunni Islam", "relationship": "PRE-EMINENT_SCHOLARLY_AUTHORITY_FOR", "note": "Al-Azhar is the pre-eminent authority for Sunni Islamic scholarship — its fatwas and curriculum shape practice across 1.8 billion Muslims"},
            {"entity": "Abu Dhabi Declaration (2019)", "relationship": "CO-SIGNATORY_OF", "note": "Grand Imam al-Tayyeb co-signed the Abu Dhabi Declaration with Pope Francis — the most significant Islamic-Christian dialogue document of the 21st century"},
            {"entity": "Gamal Abdel Nasser", "relationship": "NATIONALISED_BY", "note": "Nasser nationalised Al-Azhar (1961) — making its scholars state employees and introducing secular disciplines"}
        ],
    }),

    ("african-methodist-episcopal-church", {
        "summary": (
            "The African Methodist Episcopal Church (AME Church, est. 1816) is the oldest independent Protestant denomination founded by African Americans — established in Philadelphia by Bishop Richard Allen as an act of resistance against the racial segregation that had forced Black worshippers out of St. George's Methodist Church. The AME Church's founding is one of the most significant acts of institutional self-determination in African American history: it created an independent Black institution — governed, financed, and led entirely by Black Americans — two decades before emancipation.\n\n"
            "The AME Church played a central role in African American life across three centuries: its churches were 'freedom churches' that organised resistance to slavery (Denmark Vesey's conspiracy, 1822, was organised partly through an AME church), provided education when public schools excluded Black children, and served as the organisational infrastructure of the Civil Rights Movement (Martin Luther King Jr. was trained in the AME tradition). Its membership grew from a handful of Philadelphia worshippers (1816) to 2.5+ million members in 7,000 congregations globally.\n\n"
            "The AME Church's theology — combining Methodist evangelical Christianity with the Black liberation tradition — has been one of the most politically engaged in American Christianity. It has consistently opposed racial injustice, and the 2015 massacre at Emanuel AME Church in Charleston (nine worshippers killed by a white supremacist) focused global attention on racial violence in America."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Oldest independent Black Protestant denomination (est. 1816); Richard Allen's founding was a foundational act of African American institutional self-determination; AME churches organised antislavery resistance; Civil Rights Movement infrastructure; 2015 Charleston massacre focused global attention on racial violence; 2.5M members globally.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The racial segregation of Philadelphia's St. George's Methodist Church — where Black worshippers were physically removed from their knees during prayer in 1792 — created the immediate provocation that led Richard Allen and Absalom Jones to establish independent Black congregations",
            "The institutional exclusion of Black Americans from White-controlled churches — limiting their leadership, governance, and doctrinal authority — created the structural motivation for establishing an entirely independent denomination governed by Black Christians",
            "Richard Allen's evangelical conviction — that Christianity demanded both spiritual and social liberation — created the theological framework that united the AME Church's religious mission with its commitment to racial justice and African American dignity"
        ],
        "effects": [
            "The AME Church created the model of the independent Black institution — governed, financed, and led by African Americans — that became foundational to African American civil society, inspiring the creation of Black colleges (HBCUs), newspapers, mutual aid societies, and political organisations",
            "AME churches served as 'freedom churches' — centres of antislavery resistance, education, and community organisation — during slavery and Reconstruction, and as the primary organisational infrastructure of the Civil Rights Movement a century later",
            "The AME Church's Wilberforce University (est. 1856) — the first private historically Black university — pioneered higher education for African Americans, making the AME Church foundational to the HBCU tradition",
            "The 2015 Emanuel AME Church massacre in Charleston (nine Black worshippers killed by Dylann Roof) — and the survivors' response of forgiveness and continued activism — became a defining moment in American racial history, focusing global attention on White supremacist violence"
        ],
        "relationships": [
            {"entity": "Richard Allen", "relationship": "FOUNDED_BY", "note": "Richard Allen founded the AME Church (1816) in Philadelphia — an act of racial self-determination that created the oldest independent Black Protestant denomination"},
            {"entity": "African American Civil Rights Movement", "relationship": "ORGANISATIONAL_INFRASTRUCTURE_PROVIDED_FOR", "note": "AME churches were primary organisational infrastructure for the Civil Rights Movement — Martin Luther King Jr. was trained in the AME tradition"},
            {"entity": "Historically Black Colleges and Universities (HBCUs)", "relationship": "PIONEERED_WITH_WILBERFORCE_UNIVERSITY", "note": "AME's Wilberforce University (1856) was the first private HBCU — pioneering higher education for African Americans"},
            {"entity": "Emanuel AME Church massacre (2015)", "relationship": "LOCATION_OF_DEFINING_RACIAL_VIOLENCE_TRAGEDY", "note": "The 2015 Charleston massacre (nine worshippers killed by Dylann Roof) focused global attention on White supremacist violence in America"},
            {"entity": "American abolitionism", "relationship": "INSTITUTIONAL_BACKBONE_OF", "note": "AME churches organised antislavery resistance — Denmark Vesey's conspiracy (1822) was partly organised through AME networks"}
        ],
    }),

    ("shaolin-monastery", {
        "summary": (
            "Shaolin Monastery (少林寺, est. 495 CE) is a Buddhist monastery on Mount Song in Henan Province, China — the birthplace of Chan (Zen) Buddhism and the origin of Chinese martial arts (Kung Fu) — one of the most culturally influential religious institutions in Asian history. Founded during the Northern Wei Dynasty by the Indian monk Buddhabhadra, Shaolin became legendary through the story of Bodhidharma (Damo) — the semi-mythical Indian Buddhist patriarch who (in the 6th century tradition) established Chan Buddhism at Shaolin and introduced physical exercises to strengthen monks for meditation, founding the Shaolin martial arts tradition.\n\n"
            "The Shaolin martial tradition — Shaolin Kung Fu — developed over 1,500 years as a synthesis of Buddhist spiritual discipline, Daoist physical cultivation, and military combat techniques, and became the foundational influence on virtually all East Asian martial arts: Wing Chun, Tai Chi, Judo, Karate, Tae Kwondo, and hundreds of other martial styles trace some lineage to Shaolin. The monastery's warrior monks (Shaolin sengbing) were historically significant in Chinese military history: they famously assisted the Tang emperor Taizong (627 CE) and participated in numerous dynasties' military campaigns.\n\n"
            "Shaolin's cultural reach extended far beyond martial arts: Chan Buddhism (transmitted from Shaolin to Japan as Zen) became the most influential Buddhist school in East Asia, profoundly shaping Japanese culture, aesthetics, and philosophy. The monastery was destroyed and rebuilt multiple times — most devastatingly by the Qing (1647) and by warlord Shi Yousan (1928) — but has survived to become both a living monastic community and a global cultural icon."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Birthplace of Chan (Zen) Buddhism and Chinese martial arts (est. 495 CE); Bodhidharma's legendary founding; 1,500-year martial arts tradition; foundational influence on all East Asian martial arts; Chan Buddhism transformed Japanese culture as Zen; multiple destructions and rebuildings demonstrate institutional resilience.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Northern Wei Emperor Xiaowen's patronage of Buddhism — building Shaolin Monastery for the Indian monk Buddhabhadra to translate sutras — created the institutional foundation that would sustain 1,500 years of continuous monastic and martial tradition",
            "Bodhidharma's (traditional) introduction of Chan Buddhist meditation — with its emphasis on direct experience rather than textual study — created the distinctive Buddhist practice that made Shaolin the fountainhead of the Chan/Zen tradition that transformed East Asian culture",
            "The synthesis of Buddhist spiritual discipline, Daoist physical cultivation, and practical combat techniques — developed over centuries as Shaolin monks faced real security threats — created the Shaolin Kung Fu tradition that became the foundation of virtually all East Asian martial arts"
        ],
        "effects": [
            "Chan Buddhism — originating at Shaolin and transmitted to Japan as Zen — profoundly influenced Japanese culture: Zen aesthetics shaped Japanese gardens, tea ceremony, archery, sword arts, poetry (haiku), and architectural design, making Shaolin the ultimate origin of Japan's most distinctive cultural contributions",
            "Shaolin Kung Fu's foundational influence on East Asian martial arts — Wing Chun, Tai Chi, Karate, Judo, Tae Kwondo all trace some lineage to Shaolin traditions — makes Shaolin the most influential single institution in the history of Asian martial culture",
            "Shaolin's warrior monk tradition — demonstrated in the Tang Dynasty rescue of Emperor Taizong (627 CE) — gave religious martial arts a legitimate historical precedent that shaped the martial monk tradition across East Asia",
            "Shaolin's 20th–21st century global cultural reach — through martial arts films (Bruce Lee's popularisation, Shaolin Temple (1982) starring Jet Li, the Wu-Tang Clan's Shaolin mythology) — has made it one of the most globally recognised cultural institutions of any religious tradition"
        ],
        "relationships": [
            {"entity": "Chan Buddhism (Zen)", "relationship": "BIRTHPLACE_OF", "note": "Shaolin Monastery is the birthplace of Chan Buddhism — transmitted to Japan as Zen, profoundly shaping East Asian culture"},
            {"entity": "Bodhidharma (Damo)", "relationship": "FOUNDING_PATRIARCH_OF_CHAN_TRADITION_AT", "note": "Bodhidharma's legendary arrival at Shaolin established the Chan Buddhist tradition and (in tradition) the Shaolin martial arts"},
            {"entity": "Chinese martial arts (Kung Fu)", "relationship": "ORIGIN_OF", "note": "Shaolin Kung Fu is the foundational tradition of virtually all East Asian martial arts — Wing Chun, Tai Chi, Karate, Judo, Tae Kwondo trace some lineage here"},
            {"entity": "Japanese Zen Buddhism", "relationship": "ZEN_TRANSMISSION_SOURCE_FOR", "note": "Chan Buddhism's transmission from Shaolin to Japan as Zen profoundly shaped Japanese culture — aesthetics, tea ceremony, sword arts, haiku"},
            {"entity": "Tang Emperor Taizong", "relationship": "ASSISTED_BY_WARRIOR_MONKS_IN_CAMPAIGN_OF", "note": "Shaolin warrior monks assisted Emperor Taizong (627 CE) — giving the warrior monk tradition historical legitimacy"}
        ],
    }),

    ("lutheran-church", {
        "summary": (
            "The Lutheran Church is the oldest and largest denomination of Protestant Christianity — with approximately 80 million members in 145 countries — founded on the theological insights of Martin Luther, whose Ninety-Five Theses (1517) launched the Protestant Reformation. Luther's doctrine of justification by faith alone (sola fide), scriptural authority alone (sola scriptura), and the priesthood of all believers (eliminating the distinction between clergy and laity) constituted the most consequential religious revolution in the history of Western Christianity, breaking the 1,000-year monopoly of the Roman Catholic Church in Western Europe.\n\n"
            "The Lutheran Reformation reshaped not only religion but European culture and politics: Luther's German Bible (1534) standardised the German language; Lutheran schools (Melanchthon's Gymnasium system) pioneered universal education; Lutheran theology's emphasis on individual Bible reading promoted literacy across Northern Europe; and the Peace of Augsburg (1555) — establishing cuius regio, eius religio (the prince's religion determines the state's religion) — created the framework of territorial religious pluralism that eventually evolved into modern religious freedom.\n\n"
            "Lutheranism became the state religion of Scandinavia, much of Germany, and the Baltic states — shaping the social-democratic, egalitarian, and high-literacy cultures of these societies. Max Weber's argument in 'The Protestant Ethic and the Spirit of Capitalism' (1905) — that Lutheran (and Calvinist) theology's emphasis on vocation, frugality, and work created the cultural preconditions for capitalism — is the most influential thesis in the sociology of religion."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Oldest Protestant denomination (est. 1517 with Luther's 95 Theses); 80 million members; the Protestant Reformation broke the Catholic Church's 1,000-year Western monopoly; Luther's German Bible standardised German; Lutheranism shaped Scandinavian social democracy; Weber's Protestant Ethic thesis links Lutheranism to capitalism's origins.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Catholic Church's sale of indulgences — permitting the purchase of remission from punishment for sin — provided the specific corruption that Luther's Ninety-Five Theses attacked, but the deeper cause was the Church's institutional failure to reform its financial exploitation of Christian devotion",
            "The printing press (Gutenberg, c.1440) — which multiplied Luther's pamphlets across Germany within weeks — created the technological condition that made the Reformation irreversible, since previous reform movements (Hus, Wycliffe) had been suppressed before they could achieve mass communication",
            "Northern European political structures — German princes' desire for independence from Rome, their motivation to seize Church property, and their resentment of financial flows to Rome — created the political protection that allowed Luther to survive the Church's condemnation (Edict of Worms, 1521)"
        ],
        "effects": [
            "The Protestant Reformation broke the Catholic Church's 1,000-year monopoly in Western Europe — establishing religious pluralism, national churches, and the principle that individual conscience takes precedence over institutional religious authority, creating the foundational conditions for modern religious freedom",
            "Luther's German Bible (1534) standardised the High German dialect that became modern German — making Luther the most important figure in the history of the German language and demonstrating that Bible translation into vernacular languages was itself a cultural revolution",
            "The Lutheran emphasis on universal literacy — reading the Bible was a religious obligation, requiring mass education — pioneered universal schooling, particularly in Scandinavia, where Lutheran countries developed the highest literacy rates in the world and ultimately the social-democratic welfare states",
            "Weber's Protestant Ethic thesis (1905) — arguing that Lutheran and Calvinist theology created the cultural preconditions for capitalism — is the most influential thesis in the sociology of religion, shaping the debate about culture, religion, and economic development for over a century"
        ],
        "relationships": [
            {"entity": "Martin Luther", "relationship": "FOUNDED_ON_THEOLOGY_OF", "note": "Luther's sola fide, sola scriptura, and Ninety-Five Theses (1517) founded Lutheranism — the first Protestant denomination"},
            {"entity": "Protestant Reformation", "relationship": "ORIGIN_DENOMINATION_OF", "note": "Lutheranism is the origin denomination of the Protestant Reformation — breaking the Catholic Church's 1,000-year Western monopoly"},
            {"entity": "Peace of Augsburg (1555)", "relationship": "TERRITORIAL_LEGAL_FRAMEWORK_ESTABLISHED_BY", "note": "The Peace of Augsburg (cuius regio, eius religio) gave Lutheranism legal standing in the Holy Roman Empire — the first European religious pluralism settlement"},
            {"entity": "Scandinavian social democracy", "relationship": "CULTURAL_FOUNDATION_PROVIDED_FOR", "note": "Lutheranism's egalitarianism, literacy emphasis, and work ethic shaped Scandinavian social democracy — the world's most successful welfare state model"},
            {"entity": "German language", "relationship": "STANDARDISED_BY_LUTHER_BIBLE_TRANSLATION", "note": "Luther's German Bible (1534) standardised modern German — making Luther the most important figure in German linguistic history"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 13 — {len(ENTITIES)} entities (Class 340: Religious Orders & Communities)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
