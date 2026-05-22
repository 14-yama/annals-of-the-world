#!/usr/bin/env python3
"""
Batch 14 — 8 entities (Class 340): Religious Orders (continued)
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

    ("knights-templar", {
        "summary": (
            "The Knights Templar (Order of Solomon's Temple, est. 1119) was a Catholic military order founded by Hugh de Payens to protect Christian pilgrims in the Holy Land after the First Crusade — and grew within two centuries into the most powerful military, financial, and landowning organisation in medieval Europe before its spectacular suppression by Philip IV of France (1307) and Pope Clement V (1312). The Templars created the first international banking system: their network of commanderies across Europe and the Middle East allowed pilgrims to deposit assets in one location and withdraw them in another — inventing the letter of credit and the modern concept of the bank transfer.\n\n"
            "The Templars' military role in the Crusades — defending the Latin Kingdom of Jerusalem, garrisoning castles, and fighting in every major battle from the Battle of Montgisard (1177) to the Fall of Acre (1291) — made them the elite military force of the Crusader states. Their simultaneous role as financiers to European monarchs — the French Crown was heavily indebted to the Templars — made them politically dangerous and financially vulnerable to royal confiscation.\n\n"
            "The Templar suppression (1307–1312) — Philip IV's mass arrests, torture-extracted confessions of heresy, and Pope Clement V's dissolution of the order — is one of medieval history's most dramatic institutional destructions. The fate of the Templar treasure (never found), the last Grand Master Jacques de Molay's burning at the stake (1314) and his alleged curse on Philip IV and Clement V (both died within a year), and the conspiracy theories surrounding the Templars have made them the most mythology-laden institution in Western esoteric tradition."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Medieval military-banking order (est. 1119); invented the letter of credit and the international banking transfer; primary Crusade military force; suppressed 1307 by Philip IV (debt motivation); Jacques de Molay's burning (1314) and alleged curse; the most mythology-laden institution in Western esoteric tradition.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The First Crusade's conquest of Jerusalem (1099) created the logistical problem of protecting the thousands of pilgrims who now travelled from Europe to the Holy Land — the highways were dangerous, and pilgrims were routinely robbed and killed — creating the need for a permanent military force dedicated to pilgrim protection",
            "The Catholic Church's evolving doctrine of the 'just war' and 'holy war' — developing the concept that killing in defence of Christian holy places was not sinful but meritorious — provided the theological framework that allowed the Templars to combine the monastic religious life with military violence",
            "The financial needs of the Crusader states — permanently short of revenue and men — created the demand for a military order that could maintain standing forces, garrison castles, and provide the financial infrastructure of the Latin East"
        ],
        "effects": [
            "The Templar banking system — network of commanderies across Europe and the Middle East, letters of credit, asset transfer between locations — invented the institutional mechanisms of international banking: the letter of credit, the bank transfer, and the concept of trusted institutional intermediaries in financial transactions",
            "The Templar suppression (1307–1312) — driven largely by Philip IV's desire to cancel his debts and seize Templar assets — is the paradigmatic case of sovereign debt default through institutional destruction, demonstrating that even the most powerful non-state institutions are vulnerable to royal-papal political coordination",
            "The Templar legends — the lost treasure, de Molay's curse, secret initiations, and alleged Gnostic beliefs — became the foundation of Western esoteric tradition, inspiring Freemasonry (which claimed Templar descent), Dan Brown's 'The Da Vinci Code', and centuries of conspiracy literature",
            "The Hospitallers' inheritance of Templar properties (1312) — and their subsequent defence of Rhodes (1309–1522) and Malta (siege, 1565) — demonstrated that the military-monastic model survived the Templars' destruction, with the Hospitallers becoming the more durable of the two orders"
        ],
        "relationships": [
            {"entity": "Hugh de Payens", "relationship": "FOUNDED_BY", "note": "Hugh de Payens co-founded the Knights Templar (1119) with eight knights — creating the first Christian military order"},
            {"entity": "Crusader states (Latin East)", "relationship": "PRIMARY_MILITARY_DEFENDERS_OF", "note": "The Templars were the primary military force of the Crusader states — garrisoning castles and fighting every major battle from Montgisard (1177) to Acre (1291)"},
            {"entity": "Medieval international banking", "relationship": "INVENTED_FOUNDATIONAL_INSTRUMENTS_OF", "note": "Templar commanderies invented the letter of credit and international bank transfer — the foundational mechanisms of modern banking"},
            {"entity": "Philip IV of France", "relationship": "SUPPRESSED_BY", "note": "Philip IV suppressed the Templars (1307) to cancel his debts and seize their assets — the most dramatic institutional destruction in medieval history"},
            {"entity": "Jacques de Molay", "relationship": "LAST_GRAND_MASTER_BURNED_AT_STAKE", "note": "De Molay's burning (1314) and alleged curse on Philip IV and Clement V (both died within a year) became the origin of Templar mythology"}
        ],
    }),

    ("salvation-army", {
        "summary": (
            "The Salvation Army (est. 1865) is an international Protestant Christian church and charitable organisation founded by William Booth in London's East End — one of the most impoverished urban neighbourhoods in Victorian Britain — that became the most globally extensive Christian social welfare organisation, operating in 131 countries and providing social services (food banks, homeless shelters, disaster relief, addiction recovery, anti-trafficking programmes) to millions annually. Booth's founding vision — 'Soup, Soap, and Salvation' — integrated evangelical Christianity with direct material assistance, creating an institutional model that influenced the development of the modern welfare state.\n\n"
            "The Salvation Army's military organisational structure — commissioners, generals, soldiers, flags, and brass bands — was a deliberate appropriation of military imagery to mobilise working-class Christians in the 'war against poverty and sin'. Its brass band tradition — taking music from the tavern and redirecting it to street evangelism — created a distinctive cultural identity that made it the most visually and audibly recognisable charitable organisation in the world.\n\n"
            "William Booth's daughter-in-law Florence Booth and Bramwell Booth's work exposing child prostitution in London — through journalist W.T. Stead's 'The Maiden Tribute of Modern Babylon' (1885) — led directly to the Criminal Law Amendment Act (1885), raising the age of consent from 13 to 16. The Salvation Army's anti-trafficking work, begun in the 1880s, continues today as a global programme."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Christian social welfare organisation (est. 1865); operates in 131 countries; foundational influence on the modern welfare state concept ('Soup, Soap, Salvation'); 1885 anti-trafficking campaign led to the Criminal Law Amendment Act (raised age of consent from 13 to 16); the most globally extensive Christian charitable organisation.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The extreme poverty of Victorian London's East End — overcrowded tenements, child labour, alcoholism, prostitution — confronted William Booth with the inadequacy of conventional church charity and motivated the creation of an organisation that combined evangelical preaching with direct material assistance",
            "Victorian evangelical Christianity's conviction that the poor were both spiritually lost and materially suffering — and that addressing both simultaneously was the Christian duty — provided the theological framework for the Salvation Army's integration of evangelism and social service",
            "The failure of existing churches to reach the urban working class — who were alienated from middle-class church culture — motivated Booth's use of military organisation, brass bands, and street-level engagement to create a Christianity that working-class Londoners would accept"
        ],
        "effects": [
            "The Salvation Army's model — evangelical Christianity integrated with systematic social welfare — influenced the development of the modern welfare state concept, demonstrating that organised social intervention could address urban poverty more effectively than either charity or poor law relief alone",
            "The 1885 'Maiden Tribute' campaign — in which W.T. Stead and the Salvation Army exposed child prostitution in London — led directly to the Criminal Law Amendment Act (1885), raising the age of consent from 13 to 16 and making child procurement a serious criminal offence",
            "The Salvation Army's global expansion — 131 countries, disaster relief operations, food banks, homeless shelters — made it the most extensive Christian social service network in history, providing welfare services in countries where government provision is minimal",
            "The Salvation Army's anti-trafficking programme — begun in the 1880s — became one of the most significant anti-trafficking operations globally, identifying and rehabilitating thousands of trafficking victims annually"
        ],
        "relationships": [
            {"entity": "William Booth", "relationship": "FOUNDED_BY", "note": "William Booth founded the Salvation Army (1865) in London's East End — combining evangelical Christianity with systematic social welfare"},
            {"entity": "Victorian urban poverty", "relationship": "DIRECT_RESPONSE_TO", "note": "The Salvation Army was a direct institutional response to the extreme poverty of Victorian London's East End"},
            {"entity": "Criminal Law Amendment Act (1885)", "relationship": "CAMPAIGN_CONTRIBUTED_TO_PASSAGE_OF", "note": "The Salvation Army's 1885 anti-trafficking campaign led to the Act raising the age of consent from 13 to 16"},
            {"entity": "Modern welfare state", "relationship": "FOUNDATIONAL_MODEL_FOR", "note": "The Salvation Army's 'Soup, Soap, Salvation' model demonstrated that systematic social intervention could address urban poverty — influencing welfare state development"},
            {"entity": "Anti-trafficking movement", "relationship": "PIONEERED_INSTITUTIONAL_RESPONSE_TO", "note": "Salvation Army anti-trafficking work (1880s–present) is one of the most significant institutional responses to human trafficking globally"}
        ],
    }),

    ("opus-dei", {
        "summary": (
            "Opus Dei (Work of God, est. 1928) is a Catholic institution founded by St. Josemaría Escrivá in Madrid that promotes the sanctification of ordinary work — the theological idea that any honest work performed in union with God's will is a path to holiness — and has approximately 90,000 members globally in 90 countries. Its unique canonical status as a 'personal prelature' (granted by Pope John Paul II in 1982) gives it a structure independent of local bishops, with its own jurisdiction over its members' spiritual formation.\n\n"
            "Opus Dei's influence is disproportionate to its size: its members include prominent politicians, business leaders, academics, journalists, and professionals across the world, and its emphasis on professional excellence combined with Catholic devotion has made it especially influential in right-of-centre Catholic political and intellectual circles. The organisation operates universities, business schools, and media outlets globally, and its members have held senior positions in Spanish, Latin American, Italian, and Filipino governments.\n\n"
            "Opus Dei is the most controversial institution in contemporary Catholicism: critics allege cultlike recruitment practices, psychological pressure, corporal mortification, and disproportionate influence in the Catholic Church and in politics. Its most dramatic moments include the torture and murder of Jesuits (and others) in El Salvador by military officers with Opus Dei connections, and Dan Brown's 'The Da Vinci Code' (2003) — which portrayed an Opus Dei assassin — selling 80 million copies globally."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Catholic personal prelature (est. 1928); 90,000 members in 90 countries; disproportionate political influence through professional-class members; first personal prelature in Catholic history (1982); most controversial institution in contemporary Catholicism; Dan Brown's portrayal reached 80 million readers.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Josemaría Escrivá's mystical insight (October 2, 1928) — experiencing the vocation to sanctify ordinary work — created the theological vision that ordinary professional and domestic work could be a path to holiness, distinguishing Opus Dei from monastic spirituality's separation from the world",
            "The secularisation of Spanish society in the early 20th century — and the perceived failure of conventional Catholic practice to engage educated professional Catholics — motivated Escrivá's creation of a lay organisation that integrated Catholic devotion with professional excellence",
            "Pope John Paul II's personal affinity with Opus Dei's theological vision — particularly the emphasis on lay vocation and professional holiness — led to Escrivá's beatification (1992), canonisation (2002), and Opus Dei's unprecedented personal prelature status (1982)"
        ],
        "effects": [
            "Opus Dei's influence in Catholic intellectual, professional, and political circles — its members in senior government, academic, media, and business positions — gives the organisation disproportionate influence in right-of-centre Catholic political culture globally",
            "Opus Dei universities (University of Navarra, Strathmore University) and business schools (IESE Business School) are ranked among the best in their countries, demonstrating the organisation's success in combining Catholic identity with academic excellence",
            "The controversies around Opus Dei — allegations of cultlike recruitment, psychological pressure, and corporal mortification — have made it the focus of the most intense debate about the boundaries of acceptable religious practice in contemporary Catholicism",
            "Dan Brown's 'The Da Vinci Code' (2003) — portraying an Opus Dei assassin — reached 80 million readers and shaped popular perception of Opus Dei globally, demonstrating the power of fiction to shape institutional reputation"
        ],
        "relationships": [
            {"entity": "Josemaría Escrivá", "relationship": "FOUNDED_BY", "note": "Escrivá founded Opus Dei (1928) — canonised by Pope John Paul II (2002)"},
            {"entity": "Pope John Paul II", "relationship": "GRANTED_PERSONAL_PRELATURE_STATUS_BY", "note": "John Paul II granted Opus Dei personal prelature status (1982) — unprecedented in Catholic history — and canonised Escrivá (2002)"},
            {"entity": "The Da Vinci Code (Dan Brown, 2003)", "relationship": "DEPICTED_IN", "note": "Dan Brown's The Da Vinci Code (80 million copies) portrayed an Opus Dei assassin — shaping popular perception of the institution globally"},
            {"entity": "University of Navarra", "relationship": "OPERATES", "note": "Opus Dei operates the University of Navarra (Spain) — one of the most respected Catholic universities in the world"},
            {"entity": "Contemporary Catholic conservatism", "relationship": "INTELLECTUAL_AND_INSTITUTIONAL_CENTRE_OF", "note": "Opus Dei is a primary institutional centre of right-of-centre Catholic intellectual and political culture globally"}
        ],
    }),

    ("cistercians", {
        "summary": (
            "The Cistercians (Order of Cîteaux, est. 1098) are a Catholic monastic order founded at Cîteaux Abbey in Burgundy by Robert of Molesme — a Benedictine reform movement that sought to return to the strict literal observance of the Rule of Saint Benedict — and became one of the most historically consequential religious orders in medieval European history through their role in agricultural development, architectural innovation, and technological diffusion across the continent. At their 12th-century peak, the Cistercians operated 500+ abbeys across Europe.\n\n"
            "St. Bernard of Clairvaux — who joined the order in 1113 and founded Clairvaux Abbey (1115) — became the most powerful churchman of the 12th century: his preaching launched the Second Crusade (1147), his theology defined the mystical tradition of affective devotion, and his political interventions settled papal schisms and condemned Peter Abelard. Bernard's influence made Clairvaux, not Cîteaux, the effective centre of the order, and his 700 letters are among the most important documents of 12th-century European politics.\n\n"
            "The Cistercian monasteries were engines of medieval agricultural and technological development: their lay brother (conversi) system allowed monasteries to manage large agricultural estates; they developed water mills, drained marshes, cleared forests, bred improved sheep (for the English wool trade), and introduced new crops and cultivation techniques across Europe. Cistercian monasteries were among medieval Europe's most technologically sophisticated institutions — proto-industrial enterprises centuries before industrialisation."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Benedictine reform order (est. 1098); 500+ abbeys at 12th-century peak; St. Bernard of Clairvaux launched the Second Crusade and was the most powerful churchman of his age; Cistercian monasteries were medieval Europe's primary engines of agricultural and technological development; Cistercian Gothic architecture spread across Europe.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The perceived laxity of Benedictine observance in the 11th century — wealthy monasteries like Cluny were accused of abandoning manual labour, strict poverty, and the literal Rule — motivated the Cistercian founders' desire to establish a monastery that literally observed the Rule of Saint Benedict",
            "The 12th-century European population growth and agricultural expansion created demand for the reclamation of marginal land (forests, marshes) that Cistercian monasteries — with their lay brother labour force and organisational capacity — were ideally positioned to develop",
            "Pope Eugenius III's papacy (1145–1153) — a former Cistercian monk himself — provided the papal support that gave Cistercian expansion institutional momentum, with Bernard of Clairvaux wielding extraordinary influence as the pope's former mentor"
        ],
        "effects": [
            "Cistercian agricultural development — draining marshes, clearing forests, introducing water mills, breeding improved sheep — was a primary driver of medieval European agricultural expansion, with Cistercian estates among the most productive and technologically advanced in the continent",
            "St. Bernard's preaching of the Second Crusade (1147) — the most compelling single act of crusade recruitment in history — demonstrates the extraordinary political power that Cistercian moral authority conferred, and Bernard's letters are among the most important documents of 12th-century European politics",
            "Cistercian Gothic architecture — the 'Cistercian style' of austere, functional Gothic pioneered at abbeys like Fontenay and Rievaulx — was one of the most influential architectural movements of the medieval period, spreading Gothic construction techniques across Europe",
            "The Cistercian wool trade — English Cistercian monasteries breeding improved sheep and exporting wool to Flemish weavers — was a foundational element of the medieval English economy, connecting English monasteries to the continent's most advanced textile industry"
        ],
        "relationships": [
            {"entity": "St. Bernard of Clairvaux", "relationship": "MOST_POWERFUL_FIGURE_OF_WHOSE_INFLUENCE_DEFINED", "note": "Bernard of Clairvaux — the most powerful churchman of the 12th century — launched the Second Crusade and defined the Cistercian order's spiritual and political influence"},
            {"entity": "Cîteaux Abbey", "relationship": "FOUNDED_AT", "note": "The Cistercians were founded at Cîteaux Abbey (1098) by Robert of Molesme — the 'mother house' of the order"},
            {"entity": "Second Crusade (1147)", "relationship": "PREACHED_BY_KEY_FIGURE_OF", "note": "Bernard of Clairvaux's preaching launched the Second Crusade — demonstrating the extraordinary political power of Cistercian moral authority"},
            {"entity": "Medieval European agriculture", "relationship": "PRIMARY_ENGINE_OF_DEVELOPMENT_OF", "note": "Cistercian monasteries were primary drivers of medieval agricultural expansion — draining marshes, clearing forests, introducing water mills"},
            {"entity": "Gothic architecture", "relationship": "SPREAD_ACROSS_EUROPE_THROUGH", "note": "Cistercian austere Gothic architecture — pioneered at Fontenay, Rievaulx — was among the most influential medieval architectural movements"}
        ],
    }),

    ("augustinians", {
        "summary": (
            "The Augustinians (Order of Saint Augustine, formally unified 1244) are a Catholic mendicant religious order drawing inspiration from the Rule of Saint Augustine — one of Christianity's most psychologically sophisticated spiritual guides — and include among their most celebrated members Martin Luther (an Augustinian friar before his break with Rome) and Gregor Mendel (whose pea plant experiments in the Augustinian monastery at Brno founded modern genetics). The order emerged from a papal unification of several groups of Augustinian hermits across Italy, producing the 'Great Union' of 1244 under Pope Innocent IV.\n\n"
            "The Augustinian intellectual tradition — rooted in Augustine of Hippo's emphasis on grace, divine illumination, and the inner life — produced some of the most important figures in Western thought: Martin Luther's Augustinian formation was central to his theology of grace and his eventual break with Rome; the mystical theologian Thomas of Villanova (1488–1555) applied Augustinian theology to pastoral care; and Gregor Mendel's monastic environment at St. Thomas's Abbey, Brno, provided the intellectual space for his foundational genetics research (1856–1863).\n\n"
            "The Augustinians were active missionaries in the Spanish Americas and the Philippines — Augustinian missionaries arrived in Mexico (1533) and the Philippines (1565), establishing the first Christian parishes in both territories. The Augustinian church of San Agustín in Manila (est. 1607) is the oldest stone church in the Philippines and a UNESCO World Heritage Site."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Catholic order (unified 1244); Martin Luther was an Augustinian friar (his theology of grace rooted in Augustinian formation); Gregor Mendel conducted foundational genetics research at Augustinian monastery in Brno; Augustinian missionaries first in Philippines (1565); Rule of St. Augustine influenced 6 Catholic orders.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Pope Innocent IV's 'Great Union' (1244) — merging several Italian groups of Augustinian hermits into a single mendicant order — provided the institutional consolidation that gave the Augustinians the scale and organisation to become a major force in Catholic life",
            "Augustine of Hippo's Rule — emphasising community life, prayer, study, and service, with particular attention to the inner life and the psychology of spiritual growth — provided an attractive alternative to the more severe monastic rules and attracted intellectually inclined recruits",
            "The Catholic Church's mendicant turn of the 13th century — the papal encouragement of poverty-committed preaching orders as a response to heresy and urbanisation — created the institutional model that the Augustinians adapted, distinguishing them from purely contemplative monasteries"
        ],
        "effects": [
            "Martin Luther's Augustinian formation — his novitiate at Erfurt (1505), his deep immersion in Augustine's theology of grace and sin — was the intellectual foundation for his theology of justification by faith alone, making the Augustinian order the incubator of the Protestant Reformation",
            "Gregor Mendel's experimental genetics research (1856–1863) at St. Thomas's Abbey, Brno — counting pea plant trait inheritance across generations — founded modern genetics, and the monastery's intellectual culture provided the education and laboratory space that made his pioneering work possible",
            "Augustinian missionaries' establishment of the first Christian parishes in the Philippines (1565) made them foundational to Filipino Christianity — the Philippines is now the third-largest Catholic country in the world, and Augustinian churches are central to Filipino cultural heritage",
            "The Rule of Saint Augustine's influence extends far beyond the Augustinian order — it was adopted by the Dominicans, Premonstratensians, Norbertines, Ursulines, and dozens of other orders, making Augustine the most widely followed rule-giver in the Catholic tradition after Benedict"
        ],
        "relationships": [
            {"entity": "Martin Luther", "relationship": "NOVICE_AND_FRIAR_OF", "note": "Luther's Augustinian formation (1505–1521) was the intellectual foundation for his theology of grace — and thus for the Protestant Reformation"},
            {"entity": "Gregor Mendel", "relationship": "CONDUCTED_FOUNDATIONAL_GENETICS_RESEARCH_AS_MEMBER_OF", "note": "Mendel's pea plant experiments at St. Thomas's Abbey, Brno (1856–1863) founded modern genetics — conducted in an Augustinian monastic setting"},
            {"entity": "Protestant Reformation", "relationship": "INCUBATED_THROUGH_FORMATION_OF_KEY_FIGURE", "note": "The Augustinian order incubated Martin Luther — making Augustinian theology of grace central to the Protestant Reformation's origin"},
            {"entity": "Philippines", "relationship": "FIRST_MISSIONARIES_IN", "note": "Augustinian missionaries arrived in the Philippines (1565) — establishing the first Christian parishes in the archipelago that is now the world's third-largest Catholic country"},
            {"entity": "Rule of Saint Augustine", "relationship": "GOVERNED_BY_AND_SPREAD", "note": "The Rule of Saint Augustine governs the order and was adopted by six other Catholic orders — making it the second most widely followed rule after the Rule of Saint Benedict"}
        ],
    }),

    ("carmelites", {
        "summary": (
            "The Carmelites (Order of Brothers of the Blessed Virgin Mary of Mount Carmel, est. c.1150 CE) are a Catholic mendicant religious order with origins on Mount Carmel (in present-day Israel) — claimed as the spiritual lineage of the prophet Elijah — and produced two of the most profound mystical theologians in Western Christianity: St. John of the Cross and St. Teresa of Ávila. The Discalced (barefoot) Carmelite reform founded by Teresa and John in 16th-century Spain is the most significant internal reform movement of the Catholic Reformation.\n\n"
            "Teresa of Ávila's mystical writings — 'The Interior Castle' (1577), 'The Way of Perfection' (1566) — are the most systematic and psychologically rich accounts of contemplative prayer in the Western mystical tradition. Her analysis of prayer as a progression through seven 'mansions' of increasing intimacy with God created the framework that Catholic spiritual direction has used for 500 years. In 1970, she became the first woman declared a Doctor of the Church.\n\n"
            "John of the Cross's poetry and theological commentaries — 'The Dark Night of the Soul', 'The Ascent of Mount Carmel' — are among the greatest mystical poetry in the Spanish language and the most profound theological analysis of the experience of spiritual desolation in Western Christianity. His concept of the 'dark night of the soul' — the experience of God's apparent absence in the spiritual journey — is the most widely known concept from the Western mystical tradition."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Catholic mendicant order (est. c.1150 CE); Teresa of Ávila and John of the Cross produced the most profound mystical theology in Western Christianity; Teresa — first woman Doctor of the Church (1970); 'The Dark Night of the Soul' is the most widely known concept from Western mysticism; Discalced Carmelite reform was the most significant internal reform of the Catholic Reformation.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The 12th-century Crusader presence in the Holy Land — which brought Western Christians into contact with the hermitic tradition on Mount Carmel — created the impetus for a group of Latin hermits to establish a community seeking to live the contemplative life in the tradition of Elijah",
            "The Catholic Church's 16th-century crisis — the Protestant Reformation's challenge and the internal moral corruption that had motivated it — created the context for the Discalced Carmelite reform, which sought to renew contemplative religious life as a response to the crisis",
            "Teresa of Ávila's mystical experiences — beginning in her 40s, after 20 years of relatively lukewarm religious life — provided the personal transformation that motivated her reforming mission and the mystical writings that gave the Carmelite tradition its distinctive theological depth"
        ],
        "effects": [
            "Teresa of Ávila's mystical writings — the most systematic and psychologically rich accounts of contemplative prayer in Western Christianity — provided the framework for Catholic spiritual direction for 500 years, and her declaration as Doctor of the Church (1970) recognised women's authority in Catholic theology",
            "John of the Cross's concept of the 'dark night of the soul' — the experience of divine absence in the spiritual journey, which paradoxically deepens spiritual growth — became the most widely known and applied concept from the Western mystical tradition, used by psychologists, theologians, and spiritual directors globally",
            "The Discalced Carmelite reform — Teresa and John's renewal of Carmelite contemplative life — was the most significant internal Catholic reform movement of the 16th century, demonstrating that contemplative depth was a viable Catholic response to the Protestant challenge",
            "Edith Stein (Sr. Teresa Benedicta of the Cross) — a Jewish philosopher who converted to Catholicism, became a Carmelite nun, and was killed at Auschwitz (1942) — canonised (1998) as both martyr and Doctor of the Church, became a symbol of the interface between Judaism, Christianity, and the Holocaust"
        ],
        "relationships": [
            {"entity": "St. Teresa of Ávila", "relationship": "MOST_CELEBRATED_MYSTIC_THEOLOGIAN_OF", "note": "Teresa's 'Interior Castle' and 'Way of Perfection' are the most systematic accounts of contemplative prayer in Western Christianity — she became the first woman Doctor of the Church (1970)"},
            {"entity": "St. John of the Cross", "relationship": "PRODUCED_PROFOUND_MYSTICAL_POET_AND_THEOLOGIAN", "note": "John's 'Dark Night of the Soul' and 'Ascent of Mount Carmel' are among the greatest Spanish mystical poetry and the most profound analysis of spiritual desolation"},
            {"entity": "Discalced Carmelite reform (16th c.)", "relationship": "ORIGIN_ORDER_OF", "note": "The Discalced Carmelite reform — founded by Teresa and John — was the most significant internal Catholic reform of the 16th century"},
            {"entity": "Edith Stein (St. Teresa Benedicta)", "relationship": "CANONISED_MARTYR_MEMBER_OF", "note": "Edith Stein — Jewish philosopher, Carmelite nun, Auschwitz martyr — became a symbol of the interface between Judaism, Christianity, and the Holocaust"},
            {"entity": "Catholic mystical tradition", "relationship": "DEFINING_SCHOOL_OF", "note": "Carmelite spirituality (Teresa, John) is the defining school of Catholic mystical theology — shaping Catholic contemplative practice globally"}
        ],
    }),

    ("salvation-army-international", {
        "summary": (
            "The Quakers (Religious Society of Friends, est. 1652) are a Christian denomination founded by George Fox in northern England — historically distinguished by their rejection of all formal sacraments, ordained clergy, and creedal statements, believing that every person has 'that of God' (the Inner Light) within them that can be directly experienced without priestly mediation. This radical egalitarianism — denying the authority of priests, refusing to doff hats to social superiors, using 'thee/thou' with all persons regardless of rank — made the early Quakers among the most socially radical Christians in history.\n\n"
            "Quakers' historical influence far exceeds their small numbers (approximately 380,000 worldwide): they were foundational to American abolitionism (Anthony Benezet, John Woolman); founded Pennsylvania as a 'Holy Experiment' (William Penn's Frame of Government, 1682) — the first government explicitly guaranteeing freedom of conscience; pioneered prison reform (Elizabeth Fry); and Quaker businesses (Barclays Bank, Lloyds Bank, Cadbury, Rowntree, Clarks shoes) pioneered fair wages, non-exploitative labour practices, and social welfare — making Quaker business ethics a foundational influence on the concept of corporate social responsibility.\n\n"
            "Quakers were awarded the Nobel Peace Prize (1947) for their relief work in both World Wars — feeding civilians on both sides of the conflict, regardless of nationality. Their consistent pacifism, exemplified in their testimony against war, made them the most sustained institutional advocate for peace in modern Western history."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Religious Society of Friends (est. 1652); radical egalitarianism; foundational to American abolitionism; William Penn's Pennsylvania was the first government guaranteeing freedom of conscience; Nobel Peace Prize (1947); Quaker businesses pioneered corporate social responsibility; consistent pacifism — most sustained institutional advocate for peace in Western history.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "George Fox's spiritual crisis and breakthrough (1652) — his experience on Pendle Hill of the 'ocean of light and love' that overcame the 'ocean of darkness' — created the theological vision of universal inner light that became the Quaker doctrine, rejecting all external religious authority in favour of direct divine experience",
            "The English Civil War's (1642–1651) disruption of established religion — the collapse of Church of England authority, the proliferation of radical Protestant sects (Levellers, Diggers, Ranters) — created the social space for Quaker radicalism, which might have been suppressed in a more stable religious environment",
            "Quaker mutual support networks — which allowed the movement to survive persecution (Quaker Act 1662, conventicle acts) — demonstrated that egalitarian, non-hierarchical community organisation could sustain religious identity under adversity, shaping the movement's characteristic institutional resilience"
        ],
        "effects": [
            "Quaker abolitionism — Anthony Benezet's 'Observations on the Inslaving' (1759), John Woolman's 'Some Considerations' (1754), the Philadelphia Yearly Meeting's 1776 requirement that all Quakers manumit enslaved people — made Quakers the first organised religious group to condemn slavery, foundational to American abolitionism",
            "William Penn's Pennsylvania (1682) — with its Frame of Government guaranteeing freedom of conscience, fair dealing with Native Americans, and representative assembly — was the most liberal government in the colonial world and a direct precursor to the First Amendment's religious freedom guarantees",
            "Quaker business ethics — Barclays Bank, Lloyds Bank, Cadbury, Rowntree, Clarks — pioneering fair wages, non-exploitative labour, and honest trading practices created the model for corporate social responsibility, demonstrating that business could be conducted ethically and profitably simultaneously",
            "The American Friends Service Committee and British Friends Service Council were jointly awarded the Nobel Peace Prize (1947) for their relief work in both World Wars — feeding German civilians after WWI and providing relief on both sides in WWII — demonstrating consistent pacifist witness regardless of national interest"
        ],
        "relationships": [
            {"entity": "George Fox", "relationship": "FOUNDED_BY", "note": "George Fox founded the Religious Society of Friends (1652) on Pendle Hill — his vision of universal inner light creating Quakerism's radical egalitarianism"},
            {"entity": "William Penn", "relationship": "MOST_INFLUENTIAL_POLITICAL_QUAKER", "note": "Penn's Pennsylvania (1682) — the first government explicitly guaranteeing freedom of conscience — was the most important Quaker political achievement"},
            {"entity": "American abolitionism", "relationship": "FOUNDATIONAL_TO", "note": "Quakers (Benezet, Woolman, Philadelphia Yearly Meeting 1776) were the first organised religious group to condemn slavery — foundational to American abolitionism"},
            {"entity": "Nobel Peace Prize (1947)", "relationship": "AWARDED_TO", "note": "The AFSC and BFSC received the Nobel Peace Prize (1947) for consistent relief work on both sides of both World Wars"},
            {"entity": "Corporate social responsibility", "relationship": "PIONEERED_MODEL_FOR_THROUGH_QUAKER_BUSINESSES", "note": "Quaker businesses (Barclays, Cadbury, Rowntree) pioneered fair wages and ethical trading — the foundational model of corporate social responsibility"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 14 — {len(ENTITIES)} entities (Class 340: Religious Orders continued)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
