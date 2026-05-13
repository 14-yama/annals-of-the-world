#!/usr/bin/env python3
"""
Batch 12 — 8 entities: Cristóbal Vaca de Castro, Lancelotto Politi,
Michael de la Pole 1st Earl of Suffolk, Pierre du Bois, Muhassin al-Tanukhi,
Mem de Sá, Song Ci, Ranulf Flambard
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

    # 1 — Cristóbal Vaca de Castro (c. 1492–c. 1566)
    ("cristóbal-vaca-de-castro", {
        "summary": (
            "Cristóbal Vaca de Castro (c. 1492–c. 1566) was a Spanish colonial administrator, jurist, and Governor of Peru "
            "whose decisive leadership during Peru's first civil war established the legal and administrative foundations of "
            "Spanish colonial governance in South America. Born in Izagre in the Kingdom of León and trained in law at the "
            "University of Salamanca, he served as a judge (oidor) in the Council of Castile before Charles V dispatched him "
            "in 1540 to investigate abuses in Peru and mediate between the rival factions of Francisco Pizarro and Diego de "
            "Almagro the Elder.\n\n"
            "When Vaca de Castro arrived in 1541, Francisco Pizarro had already been assassinated by partisans of Diego de "
            "Almagro the Younger (El Mozo), who had seized control of Lima. Vaca de Castro mustered loyalist forces, marched "
            "to confront the rebels, and defeated El Mozo decisively at the Battle of Chupas (September 16, 1542) near "
            "Huamanga. El Mozo was captured and executed. Vaca de Castro's victory ended Peru's first civil war and allowed "
            "him to govern as the Crown's representative, implementing fiscal reforms, protecting indigenous communities "
            "from the worst encomendero abuses, and reasserting royal authority over the conquistador class.\n\n"
            "He governed Peru until the arrival of the first Viceroy, Blasco Núñez Vela, in 1544. He was subsequently "
            "returned to Spain under suspicion of fiscal misconduct, prosecuted, and imprisoned for years before being "
            "fully exonerated by the Council of the Indies. His tenure demonstrated that trained lawyers sent from Castile "
            "could impose legal order on the violent world of the conquistadors — establishing the template for Spanish "
            "colonial legalism in the Americas.\n\n"
            "'He came as a lawyer to a land of swords, and forced those swords to bend to the law.' Vaca de Castro's "
            "governorship remains a pivotal episode in the establishment of stable Spanish rule in the Andes."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Ended Peru's first civil war at the Battle of Chupas (1542), established Spanish colonial legal governance in the Andes, and demonstrated the Crown's capacity to impose legal order over the conquistador class.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Assassination of Francisco Pizarro (1541) by Almagrist partisans created a power vacuum in Peru requiring Crown intervention",
            "Diego de Almagro the Younger's seizure of Lima forced Charles V to send a trained jurist with gubernatorial authority",
            "Persistent conflicts between Pizarrist and Almagrist factions over encomiendas and colonial wealth required legal arbitration"
        ],
        "effects": [
            "Victory at the Battle of Chupas (1542) ended Peru's first civil war and eliminated the Almagrist faction as a political force",
            "Established Crown legal authority over the Peruvian encomendero class, beginning the transition from conquistador rule to colonial administration",
            "His governance model — trained jurist as colonial governor — became the template for subsequent Spanish colonial administration",
            "His prosecution and exoneration revealed the dangers of colonial governance and the tensions between the Council of the Indies and colonial officials"
        ],
        "relationships": [
            {"entity": "Charles V, Holy Roman Emperor", "relationship": "APPOINTED_BY", "note": "Charles V dispatched Vaca de Castro to investigate and mediate in Peru (1540)"},
            {"entity": "Diego de Almagro the Younger", "relationship": "DEFEATED", "note": "Defeated El Mozo at the Battle of Chupas (1542), ending the civil war"},
            {"entity": "Francisco Pizarro", "relationship": "SENT_TO_INVESTIGATE", "note": "Dispatched to mediate between Pizarro and the Almagristas before Pizarro's assassination"},
            {"entity": "Blasco Núñez Vela", "relationship": "PRECEDED", "note": "Governed Peru until Núñez Vela arrived as the first Viceroy (1544)"},
            {"entity": "Council of the Indies", "relationship": "ACCOUNTABLE_TO", "note": "Prosecuted and later exonerated by the Council of the Indies for alleged fiscal misconduct"}
        ]
    }),

    # 2 — Lancelotto Politi / Ambrogio Catarino Politi (1484–1553)
    ("lancelotto-politi", {
        "summary": (
            "Lancelotto Politi (1484–1553), known in religious life as Ambrogio Catarino Politi, was a Sienese Dominican "
            "theologian, canonist, and bishop who became one of the most prolific and combative Catholic controversialists "
            "of the Reformation era. Born into the Sienese legal patriciate and trained in both civil and canon law, he took "
            "Dominican vows around 1517 and immediately redirected his forensic legal mind to the theological controversies "
            "triggered by Martin Luther's challenge to Rome — publishing one of the earliest systematic Catholic refutations "
            "of Lutheran doctrine in his Apologia pro veritate catholicae et apostolicae fidei (1520).\n\n"
            "Politi was simultaneously a fierce opponent of Protestant Reformation and a provocative internal critic of "
            "Catholic scholasticism. He clashed with Cajetan over the interpretation of Aquinas on predestination, developing "
            "a distinctive theological position that gave more scope to human free will and divine universal salvific will than "
            "the strict Thomist mainstream would allow. This made him controversial within Catholicism as well as outside it — "
            "he was accused of semi-Pelagianism by some contemporaries. At the Council of Trent (1545–1563), in which he "
            "participated as one of the leading Dominican theologians, he contributed decisively to the sessions on grace, "
            "justification, original sin, and the authority of Scripture and Tradition.\n\n"
            "He was appointed Archbishop of Brindisi (1546) and later of Reggio Calabria, dying before the Council concluded. "
            "He was a prolific author — more than 30 major works — covering ecclesiology, mariology, the sacraments, and "
            "Scripture commentary, making him one of the most productive theological controversialists of his generation. "
            "He also wrote a significant commentary on Revelation that influenced later Catholic apocalyptic interpretation.\n\n"
            "'He was the hammer of heretics who questioned his own hammer.' Politi's willingness to challenge Cajetan and "
            "the Thomist consensus made him as controversial within Catholicism as outside it."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "One of the leading Catholic controversialists of the Reformation era, contributing to the Council of Trent's decrees on grace and justification while developing a distinctive non-Thomist theology of predestination that influenced Catholic anthropology.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Martin Luther's 95 Theses (1517) and subsequent challenge to Rome created the theological crisis that shaped Politi's entire career",
            "Dominican intellectual culture and his legal training gave Politi the forensic skills to engage in systematic theological controversy",
            "Pope Paul III's convening of the Council of Trent (1545) provided the institutional context for Politi's most influential theological contributions"
        ],
        "effects": [
            "Published one of the earliest Catholic systematic refutations of Lutheran doctrine (Apologia, 1520), influencing subsequent Counter-Reformation polemic",
            "His distinctive theology of grace and free will — challenging Cajetan's strict Thomism — contributed to ongoing debates that shaped post-Tridentine Catholic anthropology",
            "Contributed to the Council of Trent's decrees on original sin, justification, grace, and Scripture, among the most theologically significant conciliar texts of the 16th century",
            "His commentary on Revelation influenced Catholic apocalyptic interpretation through the Counter-Reformation period"
        ],
        "relationships": [
            {"entity": "Martin Luther", "relationship": "OPPOSED", "note": "Published the Apologia (1520), one of the earliest systematic Catholic refutations of Luther's theology"},
            {"entity": "Council of Trent", "relationship": "PARTICIPATED_IN", "note": "Contributed as a leading Dominican theologian to sessions on grace, justification, and Scripture"},
            {"entity": "Cajetan (Cardinal)", "relationship": "DISPUTED_WITH", "note": "Politi challenged Cajetan's strict Thomist interpretation of predestination, causing internal Catholic controversy"},
            {"entity": "Order of Preachers (Dominicans)", "relationship": "MEMBER_OF", "note": "Joined the Dominican Order c. 1517, taking the name Ambrogio Catarino"},
            {"entity": "Pope Paul III", "relationship": "APPOINTED_BY", "note": "Appointed Archbishop of Brindisi (1546) by Paul III during the Council of Trent"}
        ]
    }),

    # 3 — Michael de la Pole, 1st Earl of Suffolk (c. 1330–1389)
    ("michael-de-la-pole-1st-earl-of-suffolk", {
        "summary": (
            "Michael de la Pole, 1st Earl of Suffolk (c. 1330–1389) was an English financier, military commander, and Lord "
            "Chancellor of England whose 1386 parliamentary impeachment — one of the earliest in English history — marked a "
            "landmark in the development of ministerial accountability to Parliament. The son of William de la Pole, a Hull "
            "wool merchant banker of spectacular wealth, Michael parlayed his father's fortune and his own military service "
            "in the Hundred Years War into an unprecedented rise at the royal court of Richard II, culminating in his "
            "appointment as Lord Chancellor in 1383.\n\n"
            "Richard II created him Earl of Suffolk in 1385, rewarding a politician who had become the king's most trusted "
            "minister. His management of royal finances and foreign policy attracted growing hostility from a baronial "
            "faction led by the Duke of Gloucester and other magnates who accused him of enriching himself through misuse "
            "of royal funds and mismanaging the war against France. In 1386 Parliament — encouraged by the Lords Appellant — "
            "impeached him on charges of fiscal misconduct, misappropriation of funds meant for coastal defense, and abuse "
            "of his office for private gain. He was convicted, stripped of the chancellorship, and fined.\n\n"
            "Richard II pardoned him, but when the Lords Appellant raised armed rebellion against royal favorites in 1387–88, "
            "de la Pole fled to France. He died in Paris in 1389 before the political situation stabilized. His son Michael "
            "de la Pole, 2nd Earl of Suffolk subsequently restored the family's position. The 1386 impeachment established "
            "the principle that parliamentary accusation could remove a royal minister, a constitutional precedent of lasting "
            "importance in the development of parliamentary government and ministerial responsibility.\n\n"
            "His rise from merchant banking dynasty to royal earl illustrated how commercial wealth was transforming the "
            "English social and political order in the late 14th century."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "His 1386 parliamentary impeachment was one of the earliest uses of impeachment to remove a royal minister, establishing a constitutional precedent for ministerial accountability to Parliament.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Richard II's practice of governing through a small circle of trusted personal favorites created antagonism among the great magnates",
            "Lords Appellant's opposition to royal favorites, combined with Parliament's growing assertiveness, created the political coalition that drove the impeachment",
            "Military failures and fiscal strain in the Hundred Years War made de la Pole's management of royal finances politically vulnerable"
        ],
        "effects": [
            "The 1386 parliamentary impeachment established an early precedent for the constitutional principle that ministers are accountable to Parliament, not only to the Crown",
            "His forced removal from the chancellorship demonstrated the Lords Appellant's capacity to constrain royal governance without yet deposing the king",
            "His family's fortunes continued through his son, the 2nd Earl, who would play a central role in the Lancastrian-Yorkist conflict of the 15th century",
            "The impeachment contributed to the political crisis culminating in the Lords Appellant's domination of Richard II's court (1388)"
        ],
        "relationships": [
            {"entity": "Richard II of England", "relationship": "SERVED", "note": "Lord Chancellor and closest royal minister; created Earl of Suffolk by Richard II in 1385"},
            {"entity": "Thomas of Woodstock, Duke of Gloucester", "relationship": "OPPOSED_BY", "note": "Gloucester led the baronial faction that drove the impeachment"},
            {"entity": "Lords Appellant", "relationship": "IMPEACHED_BY", "note": "The Lords Appellant orchestrated de la Pole's parliamentary impeachment (1386)"},
            {"entity": "William de la Pole (merchant)", "relationship": "SON_OF", "note": "Son of William de la Pole, the Hull wool merchant banker whose wealth funded the family's political rise"},
            {"entity": "English Parliament", "relationship": "IMPEACHED_BY", "note": "Parliament convicted him of fiscal misconduct in 1386, the first effective use of parliamentary impeachment against a Chancellor"}
        ]
    }),

    # 4 — Pierre Dubois (c. 1255–c. 1321)
    ("pierre-du-bois", {
        "summary": (
            "Pierre Dubois (c. 1255–c. 1321) was a French lawyer, advocate, and political pamphleteer who produced some of the "
            "most radical and prescient proposals for European political reorganization of the medieval period. A student of "
            "Thomas Aquinas and Roger Bacon at Paris, he worked as an advocate at Coutances in Normandy and served as a "
            "publicist in the service of Philip IV (Philip the Fair) of France during the defining political crises of the "
            "early 14th century — Philip's conflict with Pope Boniface VIII and the suppression of the Knights Templar.\n\n"
            "His major work, De recuperatione Terre Sancte (c. 1306), ostensibly a treatise on recovering the Holy Land, was "
            "in practice a sweeping manifesto for the radical reorganization of European Christendom. He proposed the "
            "creation of a permanent council of European princes to arbitrate international disputes and prevent wars, "
            "compulsory secular education for both boys and girls (including training women as teachers, physicians, and "
            "missionaries), secularization of church properties to fund the crusade, subordination of papal temporal power "
            "to French royal hegemony, and French domination of a refashioned European order. These ideas anticipated the "
            "League of Nations, international arbitration, and the secularization of education by four to five centuries.\n\n"
            "Dubois also wrote pamphlets defending Philip IV against Boniface VIII during the Unam Sanctam controversy "
            "and against the Templars during their suppression (1307–1312). His work contributed to the articulation of "
            "French royal sovereignty against papal temporal claims — anticipating Gallicanism. Though his practical "
            "proposals were never implemented, his intellectual audacity made him a precursor of Enlightenment political "
            "philosophy and international legal theory.\n\n"
            "'He dreamed of a Europe governed by law and reason seven centuries before it became possible.' Dubois remains "
            "one of the most original political minds of the medieval period."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Proposed a permanent council of European states and compulsory education for women in De recuperatione Terre Sancte (c. 1306), anticipating international law, the League of Nations, and modern secular education by five centuries.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Philip IV's conflict with Pope Boniface VIII created the political context for Dubois's radical defense of French royal sovereignty against papal temporal power",
            "His studies under Roger Bacon exposed him to empiricist and reformist intellectual currents that informed his radical educational proposals",
            "The crisis of the Crusades — Jerusalem lost in 1291 — provided the ostensible framework (crusade recovery) within which he embedded his radical political proposals"
        ],
        "effects": [
            "De recuperatione Terre Sancte (c. 1306) articulated the first detailed proposal for a permanent council of European states for peaceful arbitration of international disputes",
            "His defense of French royal sovereignty against Boniface VIII contributed to the intellectual foundations of Gallicanism and the subordination of church to state",
            "His proposal for universal education of women and their training as professionals was among the most radical feminist arguments of medieval Europe",
            "His work was rediscovered in the 19th century and recognized as an anticipation of international law and the League of Nations concept"
        ],
        "relationships": [
            {"entity": "Philip IV of France", "relationship": "SERVED", "note": "Dubois served as a publicist and advocate for Philip IV in his conflict with the papacy"},
            {"entity": "Pope Boniface VIII", "relationship": "OPPOSED", "note": "Wrote pamphlets defending French royal sovereignty against Boniface VIII's Unam Sanctam (1302)"},
            {"entity": "Thomas Aquinas", "relationship": "STUDIED_UNDER", "note": "Attended Aquinas's lectures at Paris, absorbing the scholastic method he would adapt to political polemic"},
            {"entity": "Roger Bacon", "relationship": "STUDIED_UNDER", "note": "Bacon's empiricist and reformist thinking influenced Dubois's radical educational proposals"},
            {"entity": "Knights Templar", "relationship": "OPPOSED", "note": "Wrote pamphlets supporting Philip IV's suppression of the Templars (1307–1312)"}
        ]
    }),

    # 5 — Muhassin al-Tanukhi (939–994)
    ("muhassin-al-tanukhi", {
        "summary": (
            "Al-Muhassin ibn Ali al-Tanukhi (939–994 CE) was an Arab judge, man of letters, and anthologist of the Abbasid "
            "period whose literary works constitute an invaluable record of Abbasid court society, everyday life, and the "
            "cultural world of 10th-century Baghdad. Born in Basra, he served as a qadi (judge) in various cities of Iraq "
            "under the Buyid amirs who dominated the later Abbasid caliphate, combining a judicial career with prolific "
            "literary activity in the adab tradition of cultivated prose.\n\n"
            "His two major works established his reputation across the Islamic literary world. Al-Faraj ba'd al-Shidda "
            "('Relief after Distress') is an anthology of hundreds of stories illustrating the divine theme that God grants "
            "relief after tribulation — a consolatory collection drawn from personal experience, historical anecdote, "
            "judicial case, and folklore that became one of the most widely read works of classical Arabic prose. "
            "Nishwar al-Muhadara wa-Akhbar al-Mudhakara ('Table-Talk of a Mesopotamian Judge') is an encyclopedic "
            "collection of conversations, court anecdotes, judicial cases, and cultural observations from Abbasid Baghdad "
            "and Buyid Iraq, preserving firsthand and secondhand observations of extraordinary historical value.\n\n"
            "Al-Tanukhi's works are remarkable for their immediacy: he wrote with the authority of a practicing judge and "
            "social observer who recorded the texture of Abbasid life — the behavior of caliphs and merchants, the "
            "administration of justice, the experiences of prisoners, the lives of poets and scholars — with vivid personal "
            "detail. His Nishwar in particular is considered one of the essential sources for 10th-century Islamic "
            "social and cultural history.\n\n"
            "'He wrote as a judge who had seen everything human beings do to one another, and found in the recording a "
            "form of consolation.' Al-Tanukhi's anthologies remain essential reading for any student of Abbasid civilization."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "His Al-Faraj ba'd al-Shidda and Nishwar al-Muhadara are essential primary sources for 10th-century Abbasid and Buyid social and cultural history, combining literary elegance with judicial authority.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Buyid period's patronage of adab literary culture created the institutional and social environment for al-Tanukhi's literary career alongside his judicial duties",
            "The Abbasid tradition of judge-scholars combining legal practice with literary production (a tradition going back to Ibn Qutayba) shaped his dual career",
            "Personal experience of hardship and imprisonment informed the consolatory theme of Al-Faraj ba'd al-Shidda"
        ],
        "effects": [
            "Al-Faraj ba'd al-Shidda became one of the most widely copied and read works of classical Arabic prose, influencing the consolatory adab literary tradition",
            "Nishwar al-Muhadara preserved firsthand observations of 10th-century Abbasid court society, becoming an essential historical source",
            "His combination of judicial authority and literary production established a model for the judge-author that influenced subsequent Islamic adab writers",
            "His works were extensively cited and quoted by later encyclopedists including al-Tha'alibi and al-Suyuti"
        ],
        "relationships": [
            {"entity": "Buyid Dynasty", "relationship": "SERVED_UNDER", "note": "Served as qadi under Buyid amirs who controlled Baghdad and much of Iraq in the 10th century"},
            {"entity": "Abbasid Caliphate", "relationship": "OPERATED_WITHIN", "note": "His literary works document Abbasid court culture during the period of Buyid domination"},
            {"entity": "Adab literary tradition", "relationship": "CONTRIBUTED_TO", "note": "His Al-Faraj and Nishwar are major works in the classical Arabic adab tradition of cultivated prose"},
            {"entity": "Ali ibn al-Husayn al-Tanukhi (father)", "relationship": "SON_OF", "note": "His father Ali al-Tanukhi was also a judge and literary figure, from whom he inherited his career path"},
            {"entity": "Al-Tha'alibi", "relationship": "CITED_BY", "note": "Al-Tha'alibi and other encyclopedists extensively quoted and transmitted al-Tanukhi's anecdotes"}
        ]
    }),

    # 6 — Mem de Sá (c. 1500–1572)
    ("mem-de-sá", {
        "summary": (
            "Mem de Sá (c. 1500–1572) was a Portuguese jurist and colonial administrator who served as the third "
            "Governor-General of Brazil (1557–1572), the longest tenure of any colonial governor in Portuguese Brazil's "
            "history, during which he transformed a fragile coastal colony into a stable imperial possession by expelling "
            "French colonists, founding Rio de Janeiro, and forging a lasting alliance with the Jesuit missionaries who "
            "shaped Brazilian colonial culture. Born in Coimbra into a family of legal scholars and trained in law at "
            "Salamanca and Coimbra, he had served as a judge on Portugal's highest court before his appointment to Brazil.\n\n"
            "His most dramatic military accomplishment was the expulsion of the French colony of France Antarctique from "
            "Guanabara Bay (1560). The French Huguenot settlement, established by Admiral Nicolas Durand de Villegagnon "
            "in 1555 and supported by the Tupinambá people, had challenged Portuguese sovereignty over southern Brazil. "
            "Mem de Sá's naval assault in March 1560 destroyed the French fort, though the French and their indigenous "
            "allies continued to resist in the surrounding forests. The foundation of the city of Rio de Janeiro with his "
            "nephew Estácio de Sá in 1565 finally consolidated Portuguese control of the bay, and by 1567 the last French "
            "and Tupinambá resistance was suppressed.\n\n"
            "Mem de Sá governed in close partnership with the Jesuit missionaries, particularly José de Anchieta and "
            "Manuel da Nóbrega, relying on them to pacify and convert the Tupinambá and other peoples. Anchieta composed "
            "a Latin epic poem, De Gestis Mendi de Saa (c. 1563), in his honor — one of the earliest literary works "
            "composed in Brazil. He died in Salvador, Bahia, in 1572 after 15 years of governance.\n\n"
            "'He arrived as a judge of Portugal and remade an entire ocean-shore into a colony of it.' Mem de Sá's "
            "governorship established Rio de Janeiro and the Jesuit-colonial partnership that shaped Brazil for two centuries."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "As Governor-General for 15 years, he expelled French colonists from Guanabara Bay, co-founded Rio de Janeiro (1565), and established the Jesuit-colonial alliance that defined Brazilian colonial culture.",
            "significanceCategory": "continental"
        },
        "causes": [
            "French colonization of Guanabara Bay (France Antarctique, 1555) posed an existential threat to Portuguese sovereignty over southern Brazil that required military resolution",
            "Jesuit missionary activity in Brazil (beginning 1549) provided Mem de Sá with a network of indigenous-language speakers and diplomats essential to colonial governance",
            "King João III and later Sebastião I's commitment to colonial expansion empowered Mem de Sá with the resources and authority for long-term governance"
        ],
        "effects": [
            "Expelled the French colony of France Antarctique from Guanabara Bay (1560), securing Portuguese sovereignty over the region",
            "Co-founded Rio de Janeiro with his nephew Estácio de Sá in 1565, which became one of the most important cities in the Portuguese empire",
            "Consolidated the Jesuit-colonial partnership as the dominant model of indigenous policy in colonial Brazil",
            "José de Anchieta's De Gestis Mendi de Saa (c. 1563) is one of the earliest literary works composed in Brazil, celebrating Mem de Sá's campaigns"
        ],
        "relationships": [
            {"entity": "Estácio de Sá", "relationship": "CO-FOUNDED_WITH", "note": "Co-founded Rio de Janeiro with his nephew Estácio de Sá in 1565"},
            {"entity": "José de Anchieta", "relationship": "ALLIED_WITH", "note": "Worked in close partnership with Anchieta, who wrote De Gestis Mendi de Saa in his honor"},
            {"entity": "Nicolas Durand de Villegagnon", "relationship": "EXPELLED", "note": "Destroyed Villegagnon's France Antarctique settlement at Guanabara Bay in 1560"},
            {"entity": "Manuel da Nóbrega", "relationship": "ALLIED_WITH", "note": "Collaborated with Nóbrega on Jesuit indigenous policy throughout his governorship"},
            {"entity": "King Sebastião I of Portugal", "relationship": "SERVED", "note": "Served as Governor-General under both João III and Sebastião I of Portugal"}
        ]
    }),

    # 7 — Song Ci (1186–1249)
    ("song-ci", {
        "summary": (
            "Song Ci (1186–1249 CE) was a Chinese judge, physician, and forensic scientist of the Southern Song dynasty "
            "whose Xi Yuan Ji Lu ('The Washing Away of Wrongs,' 1247) is the world's first systematic treatise on forensic "
            "science, establishing methodologies for examining bodies and evidence in judicial investigations that remained "
            "in official use in China for six centuries and were translated across Asia and into European languages from the "
            "19th century onward. Born in Jianyang, Fujian Province, Song Ci studied Confucian classics and medicine before "
            "entering the Song bureaucracy, where he served across four decades as a prefect, judicial investigator, and "
            "administrator in several provinces.\n\n"
            "Xi Yuan Ji Lu — compiled from Song Ci's judicial experience and existing medical and legal literature — "
            "systematized forensic examination of corpses, wounds, bones, and injuries in ways that were unprecedented in "
            "their rigor and detail. It described: differentiation of drowning, strangulation, burning, and poisoning as "
            "causes of death; examination of bones for evidence of blunt force trauma; the use of vinegar-soaked silk "
            "umbrellas to examine bones in sunlight for fractures; insect evidence for estimating time of death (the "
            "famous fly-and-sickle case, often cited as the first recorded use of forensic entomology); and detailed "
            "diagrams of the body showing locations of vital points.\n\n"
            "The work was adopted as an official reference for Chinese magistrates — judicial investigators were required "
            "to consult it before concluding homicide cases — and was continuously reprinted, annotated, and revised in "
            "China, Korea, and Japan through the 19th century. It was translated into French by Briot in 1779 and into "
            "English and other European languages in the 19th century, influencing the development of Western forensic "
            "pathology. Song Ci is widely recognized as the father of forensic science.\n\n"
            "'Before he could judge, he had to understand the body as a witness.' Song Ci's systematic approach transformed "
            "the examination of the dead from inference into science."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Author of Xi Yuan Ji Lu (1247), the world's first systematic forensic science treatise, which was adopted as official Chinese judicial reference for six centuries and influenced the development of Western forensic pathology after translation.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Song dynasty judicial procedures required magistrates to personally examine bodies in homicide cases, creating institutional demand for systematic forensic methodology",
            "Song Ci's medical training alongside his judicial career gave him the interdisciplinary expertise to synthesize legal and anatomical knowledge",
            "Earlier Chinese forensic texts (e.g., the Tang Code provisions on wound examination) provided a foundation that Song Ci synthesized and greatly expanded"
        ],
        "effects": [
            "Xi Yuan Ji Lu (1247) became the official forensic reference for Chinese magistrates for six centuries, standardizing the examination of bodies in judicial investigations",
            "Its description of forensic entomology (using insect activity to estimate time of death) is the earliest systematic use of insects in criminal investigation recorded in any civilization",
            "Translated into French (1779), Dutch, English, and other languages, Song Ci's methods influenced the early development of Western forensic pathology",
            "The work was continuously reprinted and annotated in China, Korea, and Japan through the 19th century, shaping East Asian judicial medicine"
        ],
        "relationships": [
            {"entity": "Southern Song Dynasty", "relationship": "SERVED_UNDER", "note": "Served as a prefect and judicial administrator in the Southern Song bureaucracy for four decades"},
            {"entity": "Xi Yuan Ji Lu (The Washing Away of Wrongs)", "relationship": "AUTHORED", "note": "Compiled the world's first systematic forensic science treatise in 1247"},
            {"entity": "Chinese legal tradition", "relationship": "SYSTEMATIZED", "note": "Synthesized medical and legal knowledge into a standardized judicial investigation methodology"},
            {"entity": "East Asian judicial medicine", "relationship": "FOUNDED", "note": "His work became the standard forensic reference across China, Korea, and Japan for centuries"},
            {"entity": "European forensic pathology", "relationship": "INFLUENCED", "note": "Translated into French (1779) and subsequently into other European languages, contributing to Western forensic science development"}
        ]
    }),

    # 8 — Ranulf Flambard (c. 1060–1128)
    ("ranulf-flambard", {
        "summary": (
            "Ranulf Flambard (c. 1060–1128) was a Norman bishop and royal administrator whose career embodied both the "
            "formidable fiscal machinery of the Norman monarchy and the ecclesiastical ambitions of its leading ministers. "
            "The son of a Bayeux priest, he rose through royal service to become the most powerful official in England under "
            "William II (Rufus) — effectively the king's chief minister, controlling royal finance, justice, and the "
            "exploitation of royal rights with an efficiency and ruthlessness that made him the most hated man in England "
            "among barons, clergy, and common people alike.\n\n"
            "Flambard transformed the administration of England's feudal revenues. He kept vacant church estates and baronies "
            "in royal hands for as long as possible, maximized reliefs and aids, and applied a rigorous legal logic to "
            "extracting maximum revenue from the feudal system — methods that anticipated the financial administration of "
            "Henry II's Exchequer by several generations. He was rewarded with appointment as Bishop of Durham in 1099, a "
            "rich northern see, despite widespread objections to his notorious record of simony and abuse. When William II "
            "died in 1100, Henry I immediately imprisoned him in the Tower of London — the most prominent political prisoner "
            "of the new reign.\n\n"
            "In February 1101, Flambard staged the first recorded escape from the Tower of London: he had his supporters "
            "smuggle a rope into the tower concealed in a wine cask, threw a feast for his guards, and when they were drunk "
            "he descended the tower wall by rope and fled to Normandy, where he served Duke Robert Curthose against Henry I. "
            "He eventually reconciled with Henry and returned to Durham, where he governed his diocese, commissioned "
            "significant building works, and served as bishop until his death in 1128.\n\n"
            "'He squeezed the realm for William Rufus, escaped Henry's tower by rope, and died a bishop in his bed.' "
            "Flambard's career epitomized the dangerous intersection of royal administration and ecclesiastical ambition "
            "in Norman England."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Chief minister of William Rufus who developed Norman England's fiscal administration, and the first prisoner to escape from the Tower of London (1101) — a figure embodying the intersections of royal finance, church politics, and baronial resistance.",
            "significanceCategory": "regional"
        },
        "causes": [
            "William II (Rufus)'s aggressive exploitation of feudal revenues created institutional demand for a ruthless administrator willing to extract maximum income from royal rights",
            "The Norman Conquest's feudalization of England created the legal machinery — reliefs, aids, wardships, vacant sees — that Flambard systematically exploited",
            "Henry I's succession (1100) threatened all of William Rufus's former ministers with political reckoning, directly triggering Flambard's imprisonment and escape"
        ],
        "effects": [
            "His fiscal methods — maximizing income from vacant sees, reliefs, and feudal incidents — anticipated the systematized Exchequer administration developed under Henry I and Henry II",
            "His escape from the Tower of London in 1101 was the first recorded escape from that fortress, establishing its reputation as an escape-proof royal prison (which it proved not to be)",
            "His service to Robert Curthose after his escape contributed to the political instability that culminated in Henry I's defeat of Robert at the Battle of Tinchebray (1106)",
            "As Bishop of Durham, he commissioned architectural works and administered the diocese for nearly three decades after his reconciliation with Henry I"
        ],
        "relationships": [
            {"entity": "William II of England (Rufus)", "relationship": "SERVED", "note": "Served as chief minister and fiscal administrator under William Rufus throughout his reign (1087–1100)"},
            {"entity": "Henry I of England", "relationship": "IMPRISONED_BY", "note": "Henry I imprisoned Flambard in the Tower of London (1100) immediately after ascending the throne"},
            {"entity": "Tower of London", "relationship": "ESCAPED_FROM", "note": "First recorded prisoner to escape from the Tower of London (February 1101), using a rope smuggled in a wine cask"},
            {"entity": "Robert Curthose", "relationship": "ALLIED_WITH", "note": "After his escape, served Duke Robert of Normandy against Henry I before eventually reconciling with Henry"},
            {"entity": "Diocese of Durham", "relationship": "LED", "note": "Bishop of Durham (1099–1128), governing the diocese after his reconciliation with Henry I"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 12)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
