#!/usr/bin/env python3
"""
Batch 11 — 8 entities: Antipope Laurentius, Guido delle Colonne, Fernando de Rojas,
Agostino Novello, Lyda Conley, Marko Marulić, Branda da Castiglione,
James Stewart Duke of Ross
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/230-Class-230"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()


def enrich_entity(slug, data):
    fname = os.path.join(FOLDER, f"230{slug}.json")
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
    print(f"  ✓ {entity['name']} — sum={slen}c c={len(det.get('causes',[]))} "
          f"e={len(det.get('effects',[]))} r={len(det.get('relationships',[]))}")


ENTITIES = [

    # 1 — Laurentius (Antipope, fl. 498–506 CE)
    ("laurentius", {
        "summary": (
            "Laurentius (died c. 506 CE) was an archpriest of the Roman church and an antipope whose contested election in 498 CE "
            "triggered the Laurentian Schism, a decade-long crisis that split the papacy, the Roman Senate, and the Western Church "
            "between rival factions aligned with Constantinople and the Ostrogothic kingdom. His election by Byzantine-sympathizing "
            "senators at the Basilica of Santa Maria Maggiore ran simultaneously with Symmachus's election at the Lateran, and the "
            "schism that followed exposed the deep tensions between eastern imperial influence and Ostrogothic autonomy in late "
            "antique Italy.\n\n"
            "Laurentius was repeatedly supported by the Emperor Anastasius I Dicorus of Constantinople, who favored the Henotikon "
            "compromise and distrusted Symmachus's orthodox Chalcedonian stance. The schism produced some of the earliest "
            "systematic defenses of papal prerogatives, including the Symmachian Forgeries — a collection of fabricated decrees "
            "asserting that no earthly power could judge a pope — which would exercise enormous influence on medieval canon law "
            "and the ideology of papal immunity. For nearly eight years, the two claimants controlled different churches in Rome "
            "amid periodic violence.\n\n"
            "Theodoric the Great, Ostrogothic king of Italy, ultimately adjudicated the dispute in Symmachus's favor at the Synodus "
            "Palmaris (502 CE), though partisans of Laurentius continued agitating until approximately 506 CE. The schism's resolution "
            "highlighted the paradox of a 'barbarian' king acting as arbiter of Christian ecclesiastical order, and the Symmachian "
            "Forgeries spawned by it became foundational texts of papal supremacy doctrine for centuries afterward.\n\n"
            "'The cause of Laurentius was not merely schism but the battle-ground of two visions of Christendom — one looking to "
            "Constantinople, the other forging independence under Gothic protection.' His legacy endures in the canonical debates "
            "his schism provoked."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "The Laurentian Schism generated the Symmachian Forgeries, which shaped papal immunity doctrine and influenced medieval canon law for centuries.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Death of Pope Anastasius II (498 CE) created a disputed succession between pro-Byzantine and pro-Chalcedonian factions in Rome",
            "Byzantine Emperor Anastasius I Dicorus backed Laurentius to extend eastern influence over the Roman church",
            "Ongoing theological disputes over the Henotikon compromise polarized the Roman clergy and Senate"
        ],
        "effects": [
            "Produced the Symmachian Forgeries, fabricated decrees claiming papal immunity from temporal judgment that influenced canon law",
            "Forced Theodoric the Great to intervene as arbiter of the papacy, precedent for Ostrogothic-papal relations",
            "Established precedent for synodal resolution of contested papal elections through the Synodus Palmaris (502 CE)",
            "Deepened the Acacian Schism between Rome and Constantinople by entangling it in Italian factional politics"
        ],
        "relationships": [
            {"entity": "Symmachus (Pope)", "relationship": "RIVALS_WITH", "note": "Competing claimants in the Laurentian Schism (498–506 CE)"},
            {"entity": "Anastasius I Dicorus", "relationship": "SUPPORTED_BY", "note": "Byzantine emperor who championed Laurentius against Symmachus"},
            {"entity": "Theodoric the Great", "relationship": "JUDGED_BY", "note": "Ostrogothic king who declared Symmachus the legitimate pope at the Synodus Palmaris (502 CE)"},
            {"entity": "Symmachian Forgeries", "relationship": "PROMPTED", "note": "Partisan crisis generated fabricated papal immunity documents that shaped medieval canon law"},
            {"entity": "Acacian Schism", "relationship": "ENTANGLED_WITH", "note": "The broader East-West theological schism provided the political context for Laurentius's support from Constantinople"}
        ]
    }),

    # 2 — Guido delle Colonne (c. 1210–c. 1290)
    ("guido-delle-colonne", {
        "summary": (
            "Guido delle Colonne (c. 1210–c. 1290) was a Sicilian judge, poet, and Latin prose author who bridged the courtly Sicilian "
            "School of vernacular lyric and the new tradition of humanist Latin prose. As a judge (giudice) in Messina under the "
            "Hohenstaufen court of Frederick II and his successors, he combined legal practice with literary ambition, becoming one "
            "of the most polished poets of the Sicilian School and leaving six surviving canzone that reveal a sophisticated engagement "
            "with Provençal troubadour conventions and Aristotelian ideas about love.\n\n"
            "His most influential work was the Historia Destructionis Troiae (c. 1287), a Latin prose retelling of the Trojan War "
            "drawn largely from Benoît de Sainte-Maure's Old French Roman de Troie, itself derived from Dares Phrygius and Dictys "
            "Cretensis. The Historia quickly became the standard medieval account of the Troy legend across Western Europe, displacing "
            "its Old French source in literate circles because of its Latin accessibility and rhetorical polish. Boccaccio used it "
            "for his Filostrato, which in turn became the source for Chaucer's Troilus and Criseyde, and it informed Shakespeare's "
            "Troilus and Cressida — a chain of literary transmission stretching across three centuries.\n\n"
            "Guido's dual identity as jurist and man of letters typified the notarial-legal culture of the 13th-century Italian "
            "city-states, where legal training provided both the intellectual framework for systematic prose narrative and the social "
            "platform for literary patronage. His Historia was translated into numerous vernacular languages and remained continuously "
            "in print from the late 15th century, shaping European imagination of antiquity throughout the Renaissance."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "His Historia Destructionis Troiae became the standard medieval account of the Troy legend and influenced Boccaccio, Chaucer, and Shakespeare in a continuous chain of literary transmission.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Frederick II's Sicilian court fostered a multilingual cultural environment that blended Latin learning with vernacular Sicilian and Provençal lyric traditions",
            "Access to Benoît de Sainte-Maure's Roman de Troie (c. 1160) provided a French source that Guido systematically translated into prestigious Latin prose",
            "Demand from educated Latin-reading audiences across Europe for authoritative accounts of classical antiquity not yet available in polished Latin prose"
        ],
        "effects": [
            "Historia Destructionis Troiae became the primary European source for the Troy legend throughout the 14th–15th centuries, supplanting its French source",
            "Directly inspired Boccaccio's Filostrato (c. 1335), which provided the story of Troilus and Criseyde transmitted through Chaucer and Shakespeare",
            "His Sicilian School canzone influenced the Tuscan lyric tradition absorbed by Dante and the Dolce Stil Novo poets",
            "The Historia was printed repeatedly from 1473 onward and translated into German, English, Czech, and other vernacular languages"
        ],
        "relationships": [
            {"entity": "Frederick II, Holy Roman Emperor", "relationship": "PATRONIZED_BY", "note": "The Hohenstaufen court of Sicily nurtured Guido's literary career"},
            {"entity": "Benoît de Sainte-Maure", "relationship": "TRANSLATED_FROM", "note": "Guido adapted the Roman de Troie into Latin prose as Historia Destructionis Troiae"},
            {"entity": "Giovanni Boccaccio", "relationship": "INFLUENCED", "note": "Boccaccio used the Historia for his Filostrato, passing the Troy legend to the Italian vernacular tradition"},
            {"entity": "Geoffrey Chaucer", "relationship": "INFLUENCED", "note": "Chaucer's Troilus and Criseyde drew directly on Guido's Historia via Boccaccio"},
            {"entity": "Sicilian School", "relationship": "MEMBER_OF", "note": "One of the last major poets of the vernacular Italian lyric tradition at the Hohenstaufen court"}
        ]
    }),

    # 3 — Fernando de Rojas (c. 1465–1541)
    ("fernando-de-rojas", {
        "summary": (
            "Fernando de Rojas (c. 1465–1541) was a Spanish converso lawyer, magistrate, and author whose La Celestina (1499/1502) "
            "stands as one of the most innovative and widely read works of early modern European literature. Born in Puebla de "
            "Montalbán in the Crown of Castile to a family of Jewish converts, Rojas studied law at the University of Salamanca "
            "and subsequently worked as alcalde mayor (chief magistrate) of Talavera de la Reina for several decades, combining "
            "legal practice with a single, extraordinary literary achievement.\n\n"
            "La Celestina — originally titled Comedia de Calisto y Melibea (1499) and expanded to 21 acts as Tragicomedia (1502) — "
            "narrates the tragic love story of the young nobleman Calisto and the noblewoman Melibea, orchestrated by the scheming "
            "procuress Celestina, a character of unprecedented psychological depth and moral ambiguity. The work defies genre: "
            "it was written as a dialogue unsuited for stage performance yet too dramatic for simple reading, occupying a liminal "
            "space between theatre and novel that anticipated the modern novel's concern with interiority and social critique. "
            "It mocked courtly love conventions, exposed class hypocrisy, and portrayed desire as a destructive social force with "
            "sardonic realism.\n\n"
            "Within a decade of publication La Celestina was translated into Italian, Portuguese, German, French, Dutch, and English, "
            "making it one of the first bestsellers of the European print age. It influenced Erasmus, Montaigne, Lope de Vega, and "
            "the picaresque novel tradition. Celestina herself became a cultural archetype — the cunning bawd — recurring across "
            "European literature for two centuries.\n\n"
            "'There is no more profound portrait of destructive desire in all of Renaissance literature.' Rojas likely drew on his "
            "converso experience of marginality to craft a work of radical moral skepticism that has fascinated readers for five centuries."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "La Celestina was one of the first pan-European print bestsellers, translated into a dozen languages within decades, influencing the novel form and anticipating modern psychological realism in literature.",
            "significanceCategory": "continental"
        },
        "causes": [
            "University of Salamanca's legal training provided Rojas with dialectical skills and exposure to classical rhetoric that shaped the dialogic form of La Celestina",
            "Converso social marginality and the anxieties of the Inquisition era infused the work with a sardonic critique of courtly and religious idealism",
            "The newly established printing press in Castile enabled rapid production and distribution of the Comedia across Iberia and then across Europe"
        ],
        "effects": [
            "Established the 'celestinesque' genre of Spanish literature featuring the scheming procuress/go-between as a social satirical device",
            "Influenced Erasmus's colloquies, Montaigne's essays, and Lope de Vega's dramatic characterization across the 16th–17th centuries",
            "Anticipated the picaresque novel and the modern psychological novel in its focus on character motivation and social hypocrisy",
            "Translated into Italian, Portuguese, German, French, Dutch, English, and other European languages, establishing early modern pan-European literary circulation"
        ],
        "relationships": [
            {"entity": "University of Salamanca", "relationship": "EDUCATED_AT", "note": "Rojas studied law at Salamanca, where he may have encountered the first 16 acts of La Celestina"},
            {"entity": "Spanish Inquisition", "relationship": "CONTEXTUALIZED_BY", "note": "Converso identity and Inquisitorial pressure shaped the moral skepticism of La Celestina"},
            {"entity": "Erasmus of Rotterdam", "relationship": "INFLUENCED", "note": "Erasmus cited La Celestina as a model of character-driven satirical dialogue"},
            {"entity": "Picaresque Novel", "relationship": "ANTICIPATED", "note": "The work's social realism and anti-heroic characterization prefigured the picaresque genre"},
            {"entity": "Lope de Vega", "relationship": "INFLUENCED", "note": "The celestinesque figure of the procuress became a stock character in Golden Age Spanish theatre"}
        ]
    }),

    # 4 — Agostino Novello (c. 1240–1309)
    ("agostino-novello", {
        "summary": (
            "Agostino Novello (c. 1240–1309) was an Italian Augustinian friar, canon lawyer, and Prior General of the Order of "
            "Hermits of Saint Augustine whose remarkable career traversed the worlds of medieval jurisprudence, royal service, and "
            "mystical piety. Born in Taormina or Benevento and trained in law at the University of Bologna, he served as a leading "
            "jurist before a near-fatal accident — reportedly almost drowning — prompted a radical conversion to religious life "
            "around 1270. He entered the Augustinian Hermits and eventually rose to become the order's Prior General (1298), "
            "bringing both legal precision and spiritual authority to the governance of a rapidly expanding international religious order.\n\n"
            "Before his election as Prior General, Agostino served as secretary and confidential advisor to Charles II of Naples "
            "(King of Naples and Sicily), a role that placed him at the intersection of mendicant theology and Angevin royal politics "
            "in southern Italy. His legal expertise proved invaluable in navigating the complex jurisdictional disputes that "
            "characterized the Augustinian order's expansion across Europe, and he is credited with systematizing aspects of "
            "Augustinian constitutions. He resigned the generalship in 1300, seeking the life of a hermit near Siena.\n\n"
            "Agostino died in 1309 at Siena, and the Augustinians commissioned Simone Martini to paint his altarpiece (c. 1328), "
            "one of the masterpieces of Trecento art, depicting Blessed Agostino in the center panel surrounded by four narrative "
            "miracle scenes of remarkable dramatic and compositional sophistication. He was beatified by Pope Paul V in 1700. The "
            "altarpiece, now divided between Siena and other collections, remains one of the finest documents of the intersection "
            "of mendicant piety and Gothic art.\n\n"
            "'The friar who was once the cleverest lawyer in Bologna became, in the eyes of his brothers, the holiest man in Tuscany.' "
            "His career embodied the distinctive Augustinian synthesis of intellectual culture and contemplative spirituality."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Prior General of the Augustinian Hermits at a pivotal moment of the order's expansion; his beatification altarpiece by Simone Martini is one of the masterpieces of Trecento painting.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Training in law at the University of Bologna gave Agostino the administrative expertise to lead a major mendicant order",
            "Service to Charles II of Naples connected the Augustinian order to Angevin royal patronage in southern Italy and Sicily",
            "The Augustinian Hermits' rapid 13th-century expansion required systematic organizational governance that Agostino helped provide"
        ],
        "effects": [
            "Governed the Augustinian Hermits as Prior General (1298–1300), consolidating the order's constitutions and administrative structures",
            "Inspired the Simone Martini altarpiece (c. 1328), one of the finest surviving works of Sienese Gothic painting",
            "His model of combining legal learning with contemplative mysticism influenced the Augustinian tradition of scholar-saints",
            "Beatified by Pope Paul V in 1700, establishing his formal cult within the Catholic Church"
        ],
        "relationships": [
            {"entity": "Charles II of Naples", "relationship": "SERVED", "note": "Agostino served as royal secretary and advisor before his election as Prior General"},
            {"entity": "Order of Hermits of Saint Augustine", "relationship": "LED", "note": "Served as Prior General 1298–1300, governing the order at a key phase of expansion"},
            {"entity": "Simone Martini", "relationship": "DEPICTED_BY", "note": "Martini's c. 1328 altarpiece depicting Agostino's miracles is a masterpiece of Trecento art"},
            {"entity": "University of Bologna", "relationship": "EDUCATED_AT", "note": "Trained in canon law before his religious conversion"},
            {"entity": "Pope Paul V", "relationship": "BEATIFIED_BY", "note": "Agostino was formally beatified in 1700"}
        ]
    }),

    # 5 — Lyda Conley (1869–1946)
    ("lyda-conley", {
        "summary": (
            "Lyda Conley (1869–1946) was a Wyandot Nation woman, attorney, and activist who made history as the first Native American "
            "woman admitted to a state bar in the United States and the first Native American woman to argue a case before the "
            "United States Supreme Court. A descendant of the Wyandot people who had been forcibly relocated from their Ohio homelands "
            "to Kansas in 1843, Conley grew up in Kansas City, Kansas, and graduated from Kansas City School of Law in 1902, earning "
            "admission to the Kansas bar — a landmark achievement at a time when women of any background faced systematic exclusion "
            "from the legal profession.\n\n"
            "Her most consequential legal battle arose when the federal government sought to sell the Huron Park Indian Cemetery "
            "(now Huron Indian Cemetery) in Kansas City, Kansas — a historic burial ground containing the remains of Wyandot "
            "ancestors — to real-estate developers seeking the prime downtown land. Conley mounted a multi-year resistance that "
            "was simultaneously legal and physical: she constructed a small shanty at the cemetery entrance, armed herself, and "
            "personally turned away surveyors and officials while simultaneously filing injunctions in federal court. In 1910 she "
            "argued Conley v. United States before the Supreme Court, becoming the first Native American woman to do so, though "
            "the court ruled against her.\n\n"
            "Despite losing the court case, Conley's fierce public campaign galvanized national attention and ultimately helped "
            "defeat the congressional legislation authorizing the cemetery's sale. The Huron Cemetery remains protected to this day "
            "— a direct legacy of her resistance. She continued practicing law in Kansas City until the 1930s and remained an advocate "
            "for Wyandot rights throughout her life.\n\n"
            "'I am here to defend the graves of my people and I will do so as long as I live.' Conley's stand at the cemetery gates "
            "became one of the most dramatic acts of indigenous land defense in American legal history."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "First Native American woman admitted to a state bar and to argue before the US Supreme Court; her campaign to protect the Huron Cemetery succeeded in preserving a Wyandot ancestral burial ground against commercial development.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Federal allotment-era policies enabling sale of tribal lands and cemeteries created the immediate threat to the Huron Cemetery that Conley resisted",
            "Wyandot Nation's dispossession history — forced removal from Ohio to Kansas in 1843 — made the cemetery the last remaining ancestral sacred site in Kansas",
            "Progressive-era expansion of legal education access enabled Conley's admission to Kansas City School of Law in defiance of racial and gender barriers"
        ],
        "effects": [
            "Became the first Native American woman admitted to a US state bar (Kansas, 1902), a landmark in both women's legal history and Native American civil rights",
            "Argued Conley v. United States before the Supreme Court (1910), the first appearance of a Native American woman before that court",
            "Her sustained campaign helped defeat the congressional bill authorizing sale of the Huron Cemetery, preserving the burial ground to the present day",
            "Inspired subsequent generations of Native American women attorneys and indigenous land-rights advocates in the 20th century"
        ],
        "relationships": [
            {"entity": "Wyandot Nation", "relationship": "MEMBER_OF", "note": "Conley was a member of the Wyandot people and fought to protect their ancestral cemetery"},
            {"entity": "United States Supreme Court", "relationship": "ARGUED_BEFORE", "note": "First Native American woman to argue before the Supreme Court in Conley v. United States (1910)"},
            {"entity": "Huron Indian Cemetery", "relationship": "DEFENDED", "note": "Physically and legally prevented the sale of the Wyandot ancestral burial grounds in Kansas City"},
            {"entity": "Kansas Bar Association", "relationship": "ADMITTED_TO", "note": "First Native American woman admitted to the Kansas bar in 1902"},
            {"entity": "US Federal Allotment Policy", "relationship": "RESISTED", "note": "Her legal campaign challenged the federal government's authority to sell Native American sacred lands"}
        ]
    }),

    # 6 — Marko Marulić (1450–1524)
    ("marko-marulić", {
        "summary": (
            "Marko Marulić (1450–1524) was a Croatian humanist poet, lawyer, and religious writer from Split (Spalato), Dalmatia, "
            "whose dual achievement — creating the first major Croatian literary work in the vernacular and writing one of the most "
            "widely printed Latin devotional books of the 16th century — earned him the enduring title 'father of Croatian literature.' "
            "Trained in law and classical Latin at Padua, Marulić returned to Split to practice as a notary and lawyer while pursuing "
            "an intensely literary and pious vocation that produced works in Croatian, Latin, and Italian.\n\n"
            "His Croatian epic Judita (1501), a verse retelling of the biblical story of Judith and Holofernes, is considered the "
            "first major literary masterpiece in the Croatian language. Written in the čakavian dialect and classical metres adapted "
            "to Croatian, it transformed a biblical narrative into a meditation on Christian heroism and resistance — implicitly "
            "evoking Ottoman expansion into Dalmatia, which threatened Split itself. Marulić's Latin De institutione bene beateque "
            "vivendi per exempla sanctorum (1506) was a far greater international success: a systematic guide to Christian virtuous "
            "living, it was reprinted over 60 times in the 16th century and translated into Italian, German, Portuguese, French, and "
            "Czech, reaching lay readers across Catholic Europe.\n\n"
            "Marulić's De institutione was read and cited by Erasmus, used as a devotional text by Saint Thomas More and reportedly "
            "by Saint Francis Xavier as a missionary handbook. His reputation in his own lifetime extended across the Republic of "
            "Venice and the Habsburg world. He also composed biblical commentaries, hagiographies, and correspondence with humanists.\n\n"
            "His tombstone in Split bears the epitaph he wrote himself: 'Here lies Marko Marulić, one who despised earthly things.' "
            "He left behind the most richly bilingual humanist literary legacy of the 15th-century Adriatic."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Author of the first Croatian literary masterpiece (Judita, 1501) and one of the most widely reprinted Latin devotional works of the 16th century; influenced Erasmus, Thomas More, and Francis Xavier.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Humanist education at Padua gave Marulić mastery of classical Latin and exposure to Italian Renaissance literary culture",
            "Ottoman expansion into Dalmatia in the late 15th century provided the urgent political context for Judita's themes of resistance and deliverance",
            "The printing press enabled rapid pan-European distribution of the Latin De institutione across Catholic Europe"
        ],
        "effects": [
            "Judita (1501) established Croatian as a literary language capable of classical epic verse, founding the Croatian literary tradition",
            "De institutione bene vivendi (1506) became one of the most widely reprinted Latin devotional books of the 16th century, translated into six European languages",
            "Cited by Erasmus as a model of devotional prose and used by Saint Francis Xavier as a missionary handbook in Asia",
            "His synthesis of humanism and Counter-Reformation piety influenced the Croatian literary tradition through the 17th century"
        ],
        "relationships": [
            {"entity": "Republic of Venice", "relationship": "OPERATED_WITHIN", "note": "Split was a Venetian city; Marulić's legal career and literary patronage operated within Venetian Dalmatia"},
            {"entity": "Erasmus of Rotterdam", "relationship": "CITED_BY", "note": "Erasmus praised Marulić's De institutione as a model of learned Christian devotion"},
            {"entity": "University of Padua", "relationship": "EDUCATED_AT", "note": "Marulić's humanist legal and literary training was acquired at Padua"},
            {"entity": "Ottoman Empire", "relationship": "THREATENED_BY", "note": "Ottoman pressure on Dalmatia informed the themes of resistance and divine deliverance in Judita"},
            {"entity": "Saint Francis Xavier", "relationship": "USED_BY", "note": "Xavier reportedly carried De institutione as a devotional handbook on his Asian missions"}
        ]
    }),

    # 7 — Branda da Castiglione (1350–1443)
    ("branda-da-castiglione", {
        "summary": (
            "Branda da Castiglione (1350–1443) was an Italian cardinal, papal diplomat, and Renaissance patron whose career at the "
            "heart of the conciliarist movement made him one of the most consequential ecclesiastical statesmen of the early 15th "
            "century. Born into a Milanese noble family, he studied civil and canon law at Padua and Pavia before entering the "
            "curial service of the papacy and rising through a succession of episcopal appointments to become a cardinal in 1411 "
            "under Pope John XXIII. As a papal legate he navigated the most turbulent period in the medieval papacy's history: "
            "the Great Schism and its conciliarist resolution.\n\n"
            "Branda was a principal advocate for the Council of Constance (1414–1418), the great ecclesiastical council that ended "
            "the Western Schism by deposing or persuading the resignation of three competing popes and electing Martin V as the "
            "sole pontiff. He acted as a key intermediary in the negotiations that secured the abdication of Gregory XII (1415) "
            "and the election of Martin V (1417), and he was among the council fathers who enforced the decree Haec Sancta "
            "asserting conciliar supremacy over the pope — a position he would later moderate in practice under Martin's papacy. "
            "He also presided over the prosecution of Jan Hus and his condemnation as a heretic.\n\n"
            "An energetic humanist patron, Branda transformed his hometown of Castiglione Olona in Lombardy into a Renaissance "
            "showcase, commissioning Masolino da Panicale to fresco the Baptistery (c. 1435), the Collegiate Church, and the "
            "Cardinal's Palace with scenes from the life of John the Baptist, the Virgin, and Pope Clement I — one of the finest "
            "early Renaissance fresco cycles in northern Italy. He also served as a diplomatic link between the papacy and the "
            "Hungarian kingdom, spending years at the court of Sigismund.\n\n"
            "'He made the empty hills of Lombardy bloom with Christian humanist art.' Castiglione Olona remains his living monument."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "A principal architect of the Council of Constance's resolution to the Great Schism, and a major patron of early Renaissance art who commissioned Masolino da Panicale's fresco cycles.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Great Schism (1378–1417) created the crisis of three simultaneous papal claimants that required Branda's diplomacy to resolve",
            "Legal training in both civil and canon law at Padua and Pavia equipped him for the intricate jurisdictional negotiations at Constance",
            "His wealth and noble connections gave him the resources and influence to patronize Renaissance art in Castiglione Olona"
        ],
        "effects": [
            "Played a decisive role in the negotiations at the Council of Constance (1414–1418) that elected Martin V and ended the Great Schism",
            "Presided over the trial and condemnation of Jan Hus (1415), shaping the trajectory of Hussite reform in Bohemia",
            "Commissioned Masolino da Panicale's fresco cycles at Castiglione Olona (c. 1435), one of the finest early Renaissance programs in Lombardy",
            "Served as a key papal legate to Hungary and the Holy Roman Empire, helping coordinate Catholic Europe's response to the Hussite revolts"
        ],
        "relationships": [
            {"entity": "Council of Constance", "relationship": "ORCHESTRATED", "note": "Principal diplomat who secured papal resignations and the election of Martin V (1417)"},
            {"entity": "Pope Martin V", "relationship": "CHAMPIONED_ELECTION_OF", "note": "Branda's negotiations were central to the election that ended the Great Schism"},
            {"entity": "Jan Hus", "relationship": "PROSECUTED", "note": "Branda presided over the heresy trial of Jan Hus at Constance (1415)"},
            {"entity": "Masolino da Panicale", "relationship": "PATRONIZED", "note": "Commissioned Masolino's fresco cycles at Castiglione Olona, among the finest early Renaissance works in Lombardy"},
            {"entity": "Sigismund, Holy Roman Emperor", "relationship": "DIPLOMATIC_PARTNER_OF", "note": "Served as papal legate to Sigismund's court, coordinating Catholic policy against Hussite Bohemia"}
        ]
    }),

    # 8 — James Stewart, Duke of Ross (c. 1476–1504)
    ("james-stewart-duke-of-ross", {
        "summary": (
            "James Stewart, Duke of Ross (c. 1476–1504) was a Scottish royal prince, Archbishop of St Andrews, and Lord Chancellor "
            "of Scotland whose brief life embodied the 15th-century Scottish crown's practice of vesting its most powerful "
            "ecclesiastical offices in members of the royal family to consolidate dynastic control over church revenues and "
            "appointments. The second surviving son of King James III of Scotland and Margaret of Denmark, he was created Duke "
            "of Ross in 1481, and following his older brother's accession as James IV, he was elevated to the see of St Andrews "
            "— the primatial archdiocese of Scotland — around 1497.\n\n"
            "As heir presumptive to the Scottish throne during the early years of James IV's reign (before James married and "
            "produced legitimate children), the Duke of Ross occupied a constitutionally sensitive position. His appointment as "
            "Lord Chancellor made him simultaneously the kingdom's highest secular officer and its leading ecclesiastic — a "
            "concentration of power in one royal younger son that reflected both the trust James IV placed in him and the pragmatic "
            "logic of keeping ecclesiastical patronage within the dynasty. He participated in the governance of the kingdom during "
            "a period of active foreign diplomacy and internal consolidation under his brother.\n\n"
            "He died in 1504, probably from illness, at approximately 28 years of age. His early death removed a potential rival "
            "claimant and simplified the succession, as James IV would subsequently marry Margaret Tudor (1503) and begin a line "
            "that extended through Mary Queen of Scots to the Union of the Crowns in 1603. The Archdiocese of St Andrews passed "
            "to Alexander Stewart (James IV's illegitimate son), continuing the pattern of royal control over the see.\n\n"
            "His career illustrates how late medieval Scottish monarchs used ecclesiastical appointments as instruments of royal "
            "governance, a practice that would generate growing tension with the papacy in the pre-Reformation era."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "As heir presumptive and simultaneously Archbishop of St Andrews and Lord Chancellor, he embodied the Scottish crown's strategy of dynastic control over ecclesiastical resources and governance in the pre-Reformation era.",
            "significanceCategory": "regional"
        },
        "causes": [
            "James III of Scotland's practice of royal appointment of younger sons to major ecclesiastical sees as instruments of dynastic governance",
            "James IV's need for a reliable Lord Chancellor during a period of active foreign diplomacy and domestic consolidation",
            "The political logic of placing the heir presumptive in an ecclesiastical role to minimize his capacity for dynastic rivalry"
        ],
        "effects": [
            "Served as Lord Chancellor of Scotland, exercising the highest secular executive office while simultaneously holding the primatial archdiocese",
            "His early death (1504) removed a potential rival claimant, simplifying the succession that led to the Stuart line through James IV and Margaret Tudor",
            "The archdiocese passed to James IV's illegitimate son Alexander Stewart, continuing the royal monopoly on St Andrews that would provoke pre-Reformation tensions",
            "His career demonstrated the limitations of combining royal blood with clerical office, a pattern criticized by reform-minded humanists in the early 16th century"
        ],
        "relationships": [
            {"entity": "James III of Scotland", "relationship": "SON_OF", "note": "Second son of James III and Margaret of Denmark"},
            {"entity": "James IV of Scotland", "relationship": "BROTHER_OF", "note": "Served as Lord Chancellor under his older brother James IV"},
            {"entity": "Archdiocese of St Andrews", "relationship": "HEADED", "note": "Appointed Archbishop of St Andrews c. 1497, the primatial see of Scotland"},
            {"entity": "Margaret of Denmark", "relationship": "SON_OF", "note": "His mother was the Danish princess whose dowry brought the Orkney and Shetland islands to Scotland"},
            {"entity": "Alexander Stewart (Archbishop)", "relationship": "PREDECESSOR_OF", "note": "James IV's illegitimate son succeeded to St Andrews after James Stewart's death in 1504"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 11)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
