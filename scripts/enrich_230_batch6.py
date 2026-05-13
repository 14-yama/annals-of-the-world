#!/usr/bin/env python3
"""
Batch 6: Cross-cultural legal figures — Maliki jurisprudence, Tudor legal writers,
French humanism, Protestant natural law, and Roman Stoic lawyers.
"""

import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/230-Class-230"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()

ENRICHMENTS = {
    "sahnun": {
        "summary": (
            "Sahnun ibn Said ibn Habib al-Tanukhi (776–854 CE) was the most influential "
            "Maliki jurist of North Africa, whose monumental al-Mudawwana al-Kubra "
            "(The Great Compilation) became — and remains — the foundational legal text "
            "of the Maliki school of Islamic law in the western Muslim world. Born in "
            "Qayrawan (in modern Tunisia), he traveled to Medina to study under Ibn "
            "al-Qasim al-Ataki, the leading student of Malik ibn Anas himself, and "
            "brought the Madinan legal tradition to North Africa in an authoritative written form.\n\n"
            "The Mudawwana was not Sahnun's original composition but rather a reworking "
            "and systematic organization of the Asadiyya — a compilation by Ibn al-Qasim "
            "of questions posed by the Kufan jurist al-Asad ibn al-Furat — combined with "
            "new questions Sahnun himself put to Ibn al-Qasim. The work covers the full "
            "range of fiqh (Islamic jurisprudence): worship, contracts, family law, "
            "inheritance, criminal law, and judicial procedure. Its organization, authority, "
            "and comprehensiveness made it the definitive reference of the Maliki school "
            "throughout North Africa, Muslim Spain (al-Andalus), sub-Saharan West Africa, "
            "and subsequently East Africa — a reach that continues to the present day.\n\n"
            "Sahnun served as qadi (judge) of Qayrawan from approximately 847 until his "
            "death, one of the most important judicial appointments in North Africa. "
            "His career as a judge was marked by fierce independence from political "
            "pressure — he reportedly defied the Aghlabid rulers on questions of law "
            "and was known for austere personal piety. The Mudawwana's influence across "
            "the western Islamic world over twelve centuries makes Sahnun one of the "
            "most consequential jurists in the history of Islamic law."
        ),
        "causes": [
            {
                "title": "The need to transmit the authentic Madinan legal tradition of Malik ibn Anas to North Africa in a systematic written form drove Sahnun's scholarly journey to Medina",
                "type": "Institution",
                "year": "c. 795–810, Medina"
            },
            {
                "title": "The existing Asadiyya compilation was incomplete and contested; Sahnun's revision created a more authoritative and comprehensive text for the Maliki school",
                "type": "Text",
                "year": "c. 790–820, North Africa"
            },
            {
                "title": "Qayrawan's position as the intellectual and political capital of Aghlabid North Africa made it the natural center for systematizing the Maliki legal tradition in the region",
                "type": "Institution",
                "year": "c. 800–854, Qayrawan"
            }
        ],
        "effects": [
            {
                "title": "Al-Mudawwana al-Kubra became the foundational text of the Maliki school across North Africa, West Africa, Muslim Spain, and East Africa — a legal authority sustained for twelve centuries",
                "type": "Text",
                "year": "c. 820 CE – present"
            },
            {
                "title": "Sahnun's qadiat of Qayrawan established a model of judicial independence from political pressure that became an ideal of Islamic jurisprudential ethics",
                "type": "Institution",
                "year": "c. 847–854, Qayrawan"
            },
            {
                "title": "The Maliki school's dominance across the Maghreb and West Africa — sustained by the Mudawwana — shapes Islamic legal practice in those regions to the present day",
                "type": "Movement",
                "year": "9th century CE – present"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "sahnun",
                "sourceName": "Sahnun",
                "verb": "AUTHORED",
                "targetSlug": "al-mudawwana-al-kubra",
                "targetName": "Al-Mudawwana al-Kubra",
                "context": "Sahnun compiled and revised the Mudawwana — the foundational text of Maliki jurisprudence — based on Ibn al-Qasim's transmissions from Malik ibn Anas"
            },
            {
                "sourceSlug": "sahnun",
                "sourceName": "Sahnun",
                "verb": "STUDIED_UNDER",
                "targetSlug": "ibn-al-qasim",
                "targetName": "Ibn al-Qasim al-Ataki",
                "context": "Sahnun traveled to Medina to study under Ibn al-Qasim, Malik's leading student, and brought his legal transmissions back to North Africa"
            },
            {
                "sourceSlug": "sahnun",
                "sourceName": "Sahnun",
                "verb": "TRANSMITTED",
                "targetSlug": "maliki-school",
                "targetName": "Maliki School of Islamic Law",
                "context": "Sahnun was the principal transmitter of Maliki jurisprudence to North Africa; his Mudawwana remains the school's foundational text in the western Islamic world"
            },
            {
                "sourceSlug": "sahnun",
                "sourceName": "Sahnun",
                "verb": "SERVED_AS",
                "targetSlug": "qadi-of-qayrawan",
                "targetName": "Qadi of Qayrawan",
                "context": "Sahnun served as the qadi (chief judge) of Qayrawan from c. 847 until his death in 854, the most senior judicial position in Aghlabid North Africa"
            },
            {
                "sourceSlug": "sahnun",
                "sourceName": "Sahnun",
                "verb": "INFLUENCED",
                "targetSlug": "west-african-islamic-law",
                "targetName": "West African Islamic Law",
                "context": "The Mudawwana's dominance in North Africa spread through trade networks to shape Islamic legal practice across the Sahel and West Africa"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Sahnun's al-Mudawwana al-Kubra — the systematic compilation of Maliki jurisprudence — has governed Islamic legal practice across North Africa, Muslim Spain, and West Africa for twelve centuries, making him one of the most consequential jurists in the history of Islamic law.",
            "significanceCategory": "continental"
        },
        "importanceScore": 7
    },

    "anthony-fitzherbert": {
        "summary": (
            "Sir Anthony Fitzherbert (1470–1538) was an English judge of the Court of Common "
            "Pleas (from 1522) and the author of La Graunde Abridgement (1514–1516) — the "
            "first printed abridgment of English common law cases — a monumental three-volume "
            "compilation of cases from the Year Books organized by subject that became an "
            "indispensable reference for common law practitioners for decades. Together with "
            "his Natura Brevium (writs) and Diversité de Courtz (court types), Fitzherbert "
            "produced the first systematic printed guides to English legal practice, transforming "
            "the profession's working tools in the era of the printing press.\n\n"
            "Born into a Derbyshire gentry family and trained in the law, Fitzherbert was "
            "called to the bar and built a successful practice before his appointment to the "
            "bench. His Abridgement was an enormous undertaking: the Year Books — the "
            "manuscript records of oral pleading in medieval English courts — had never been "
            "systematically organized. Fitzherbert excerpted and arranged thousands of cases "
            "under alphabetical subject headings, giving practitioners for the first time a "
            "subject-accessible index to the existing law. The work was printed by Richard "
            "Pynson and ran to multiple editions, its authority lasting well into the "
            "Elizabethan era.\n\n"
            "A work attributed to his brother John Fitzherbert, the Boke of Husbandry (1523) "
            "— the earliest printed treatise on English farming — was for centuries mistakenly "
            "attributed to Anthony, inflating his literary reputation. On the bench, Fitzherbert "
            "served as a justice of assize across the northern circuits in the difficult years "
            "of the break with Rome, dying in 1538 having just lived through the dissolution "
            "of the monasteries he had likely grown up revering."
        ),
        "causes": [
            {
                "title": "The introduction of the printing press to England made the publication of practical legal reference works economically viable for the first time",
                "type": "Idea",
                "year": "c. 1475–1510, England"
            },
            {
                "title": "The Year Books' manuscript tradition of unorganized oral pleading records created a practical need for systematic printed subject-accessible abridgments",
                "type": "Institution",
                "year": "c. 1270–1510, England"
            },
            {
                "title": "The expanding class of professionally trained common lawyers required reliable printed reference works as the courts' business grew in complexity and volume",
                "type": "Institution",
                "year": "c. 1480–1520, England"
            }
        ],
        "effects": [
            {
                "title": "La Graunde Abridgement (1514–1516) gave common law practitioners the first printed subject-indexed reference to the Year Book case law, transforming legal research",
                "type": "Text",
                "year": "1514–1516, London"
            },
            {
                "title": "Fitzherbert's Natura Brevium became the standard practitioner's guide to common law writs, running through numerous editions over the next century",
                "type": "Text",
                "year": "c. 1534, England"
            },
            {
                "title": "The Abridgement model Fitzherbert pioneered was continued by his successors — notably Robert Brooke (1568) — shaping the genre of English legal reference literature for over a century",
                "type": "Idea",
                "year": "1514–1600, England"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "anthony-fitzherbert",
                "sourceName": "Anthony Fitzherbert",
                "verb": "AUTHORED",
                "targetSlug": "la-graunde-abridgement",
                "targetName": "La Graunde Abridgement",
                "context": "Fitzherbert's three-volume Abridgement (1514–1516) was the first printed subject-indexed compilation of English common law cases"
            },
            {
                "sourceSlug": "anthony-fitzherbert",
                "sourceName": "Anthony Fitzherbert",
                "verb": "AUTHORED",
                "targetSlug": "natura-brevium-fitzherbert",
                "targetName": "Natura Brevium",
                "context": "Fitzherbert's guide to common law writs became the standard practitioner's reference for the English writ system"
            },
            {
                "sourceSlug": "anthony-fitzherbert",
                "sourceName": "Anthony Fitzherbert",
                "verb": "SERVED_ON",
                "targetSlug": "court-of-common-pleas",
                "targetName": "Court of Common Pleas",
                "context": "Fitzherbert served as a justice of Common Pleas from 1522 until his death in 1538"
            },
            {
                "sourceSlug": "anthony-fitzherbert",
                "sourceName": "Anthony Fitzherbert",
                "verb": "INFLUENCED",
                "targetSlug": "edward-coke",
                "targetName": "Edward Coke",
                "context": "Coke's Institutes built on Fitzherbert's Abridgement tradition and cited his work extensively"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Anthony Fitzherbert's La Graunde Abridgement — the first printed subject-indexed compilation of English case law — transformed legal practice in Tudor England by giving practitioners accessible reference to the accumulated Year Book tradition, pioneering the genre of legal abridgments that continued through Coke's generation.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "barthélemy-de-chasseneuz": {
        "summary": (
            "Barthélemy de Chasseneuz (1480–1541) was a French jurist, President of the "
            "Parlement of Provence, and legal humanist whose career bridged scholastic and "
            "Renaissance approaches to law. Born at Issy-l'Évêque in Burgundy, he studied "
            "law at Bologna — then Europe's greatest law school — returning to France to "
            "practice and eventually sit on the Parlement of Provence, the highest regional "
            "court in southern France. His legal career combined successful advocacy, "
            "judicial service, and prolific scholarly writing.\n\n"
            "Chasseneuz is most memorably associated with an early episode in his career "
            "when, representing the village of Autun before an ecclesiastical court, he "
            "successfully obtained an adjournment in a case against rats accused of "
            "destroying the local grain harvest. His argument was procedurally ingenious: "
            "the summons could not have been adequately served on the rats because they "
            "lived in dispersed villages across a wide area; and the rats could not be "
            "expected to appear in court while exposed to mortal danger from cats along "
            "the road. The case — however fanciful its factual basis — demonstrated "
            "sophisticated procedural reasoning applied to an absurd situation, and has "
            "fascinated legal historians and philosophers as an early example of the logic "
            "of legal procedure applied universally.\n\n"
            "Chasseneuz's major scholarly work, the Catalogus Gloriae Mundi (Catalogue of "
            "the World's Glory, 1529), was an encyclopedic ranking of all beings and "
            "dignities in the created order — from God and angels down through kings, "
            "priests, lawyers, craftsmen, and animals. A monument of late medieval "
            "encyclopedism, it blended theology, jurisprudence, and social commentary "
            "in the humanist tradition. His Consuetudines Ducatus Burgundiae (1517) "
            "was an authoritative commentary on Burgundian customary law."
        ),
        "causes": [
            {
                "title": "The tradition of ecclesiastical courts prosecuting animals for harm caused to human crops or persons — widespread in medieval Europe — created the legal theater of the Autun rat trial",
                "type": "Institution",
                "year": "c. 1480–1522, Burgundy"
            },
            {
                "title": "Bologna's rigorous legal training gave Chasseneuz the procedural sophistication to transform an absurd factual situation into a vehicle for serious procedural argument",
                "type": "Institution",
                "year": "c. 1500–1510, Bologna"
            },
            {
                "title": "The humanist encyclopedic tradition of categorizing and ranking all of creation provided the intellectual framework for the Catalogus Gloriae Mundi",
                "type": "Idea",
                "year": "c. 1510–1529, France"
            }
        ],
        "effects": [
            {
                "title": "The Autun rat trial became a celebrated legal anecdote illustrating both the rigor of procedural law and its potential absurdity when applied without common sense",
                "type": "Idea",
                "year": "c. 1510 – present"
            },
            {
                "title": "Catalogus Gloriae Mundi (1529) preserved a comprehensive late medieval taxonomy of social and cosmic hierarchy, becoming an important source for Renaissance intellectual history",
                "type": "Text",
                "year": "1529, Lyon"
            },
            {
                "title": "Consuetudines Ducatus Burgundiae (1517) provided an authoritative systematization of Burgundian customary law at a critical moment of legal codification",
                "type": "Text",
                "year": "1517, Burgundy"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "barthélemy-de-chasseneuz",
                "sourceName": "Barthélemy de Chasseneuz",
                "verb": "ARGUED",
                "targetSlug": "autun-rat-trial",
                "targetName": "Autun Rat Trial",
                "context": "Chasseneuz successfully obtained an adjournment in the Autun rat trial by arguing that the rats had not been properly summoned and could not safely travel to court"
            },
            {
                "sourceSlug": "barthélemy-de-chasseneuz",
                "sourceName": "Barthélemy de Chasseneuz",
                "verb": "AUTHORED",
                "targetSlug": "catalogus-gloriae-mundi",
                "targetName": "Catalogus Gloriae Mundi",
                "context": "Chasseneuz's 1529 encyclopedic ranking of all dignities from God to animals is a major document of late medieval cosmological jurisprudence"
            },
            {
                "sourceSlug": "barthélemy-de-chasseneuz",
                "sourceName": "Barthélemy de Chasseneuz",
                "verb": "SERVED_ON",
                "targetSlug": "parlement-of-provence",
                "targetName": "Parlement of Provence",
                "context": "Chasseneuz served as President of the Parlement of Provence, the highest regional court of southern France"
            },
            {
                "sourceSlug": "barthélemy-de-chasseneuz",
                "sourceName": "Barthélemy de Chasseneuz",
                "verb": "STUDIED_AT",
                "targetSlug": "university-of-bologna",
                "targetName": "University of Bologna",
                "context": "Chasseneuz studied law at Bologna, then Europe's premier law school, before returning to practice in Burgundy"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Barthélemy de Chasseneuz's Autun rat trial — a virtuoso exercise in procedural argument applied to an absurd situation — became one of legal history's most famous anecdotes, while his Catalogus Gloriae Mundi preserved the most comprehensive late medieval taxonomy of social and cosmic hierarchy.",
            "significanceCategory": "regional"
        },
        "importanceScore": 8
    },

    "johann-oldendorp": {
        "summary": (
            "Johann Oldendorp (c. 1480/1486–1567) was a German jurist, professor of law, "
            "and one of the earliest Protestant thinkers to articulate a systematic theory "
            "of natural law from an explicitly Lutheran perspective. A student at Rostock "
            "and subsequently professor at Rostock, Marburg, and Frankfurt an der Oder, "
            "he lived through the entirety of the German Reformation and participated in "
            "the theological debates surrounding Luther's movement as both a jurist and "
            "a civic humanist.\n\n"
            "Oldendorp's most significant intellectual contribution was his attempt to "
            "reconfigure natural law theory on Protestant foundations. Medieval natural "
            "law had derived from Aquinas's synthesis of Aristotle and scripture, locating "
            "natural law within the hierarchical framework of the Catholic Church. "
            "Oldendorp, in works including Isagoge iuris naturalis, gentium et civilis "
            "(Introduction to Natural, International, and Civil Law, 1539) and "
            "Wat billich und recht ys (What Is Fair and Right, 1529), argued that natural "
            "law derived from the light of reason that God had implanted in all human beings — "
            "an argument that grounded legal obligation in universal human reason rather "
            "than in ecclesiastical authority. This Protestant natural law contributed to "
            "the broader trajectory that would lead from Grotius to Pufendorf and eventually "
            "to Enlightenment natural rights theory.\n\n"
            "Oldendorp also played a practical civic role: he advised the city of Hamburg "
            "and other north German cities on legal matters, contributed to the codification "
            "of north German urban law, and wrote extensively on the relationship between "
            "positive law and equity (aequitas) — arguing that mechanical application of "
            "the letter of the law without reference to justice was a form of injustice. "
            "His blend of humanism, Lutheranism, and systematic jurisprudence made him "
            "an important transitional figure in the development of early modern legal thought."
        ),
        "causes": [
            {
                "title": "The Lutheran Reformation's rejection of papal and ecclesiastical authority over law required Protestant jurists to ground legal obligation in non-ecclesiastical foundations",
                "type": "Movement",
                "year": "1517–1540, Germany"
            },
            {
                "title": "Northern European legal humanism's revival of Roman law texts provided Oldendorp with classical sources for a systematized natural law theory",
                "type": "Idea",
                "year": "c. 1510–1539, Germany"
            },
            {
                "title": "North German cities' need for systematic legal guidance on civic governance drove Oldendorp's practical engagement with urban law and equity",
                "type": "Institution",
                "year": "c. 1520–1550, Hamburg and north Germany"
            }
        ],
        "effects": [
            {
                "title": "Oldendorp's Protestant natural law theory contributed to the trajectory from Lutheran jurisprudence through Grotius and Pufendorf to Enlightenment natural rights",
                "type": "Idea",
                "year": "1529–1650, Europe"
            },
            {
                "title": "Isagoge iuris naturalis (1539) was an early systematic Protestant contribution to natural law jurisprudence, grounding legal obligation in universal human reason",
                "type": "Text",
                "year": "1539, Cologne"
            },
            {
                "title": "His equity jurisprudence — arguing for justice over mechanical letter-of-the-law application — influenced the development of German equitable principles in early modern law",
                "type": "Idea",
                "year": "c. 1529–1567, Germany"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "johann-oldendorp",
                "sourceName": "Johann Oldendorp",
                "verb": "AUTHORED",
                "targetSlug": "isagoge-iuris-naturalis",
                "targetName": "Isagoge iuris naturalis, gentium et civilis (1539)",
                "context": "Oldendorp's 1539 Introduction to Natural Law was an early systematic Protestant contribution to natural law jurisprudence"
            },
            {
                "sourceSlug": "johann-oldendorp",
                "sourceName": "Johann Oldendorp",
                "verb": "CHAMPIONED",
                "targetSlug": "protestant-natural-law",
                "targetName": "Protestant Natural Law",
                "context": "Oldendorp grounded legal obligation in reason implanted by God rather than ecclesiastical authority, pioneering Protestant natural law theory"
            },
            {
                "sourceSlug": "johann-oldendorp",
                "sourceName": "Johann Oldendorp",
                "verb": "CONTEMPORARY_OF",
                "targetSlug": "martin-luther",
                "targetName": "Martin Luther",
                "context": "Oldendorp was a Lutheran sympathizer who adapted legal theory to the Protestant Reformation's rejection of papal authority"
            },
            {
                "sourceSlug": "johann-oldendorp",
                "sourceName": "Johann Oldendorp",
                "verb": "INFLUENCED",
                "targetSlug": "hugo-grotius",
                "targetName": "Hugo Grotius",
                "context": "Oldendorp's Protestant natural law theory contributed to the tradition of secular natural law developed by Grotius in De Jure Belli ac Pacis (1625)"
            },
            {
                "sourceSlug": "johann-oldendorp",
                "sourceName": "Johann Oldendorp",
                "verb": "TAUGHT_AT",
                "targetSlug": "university-of-marburg",
                "targetName": "University of Marburg",
                "context": "Oldendorp held the chair of law at Marburg, one of the first Protestant universities, contributing to the formation of Lutheran legal education"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Johann Oldendorp's systematic Protestant natural law theory — grounding legal obligation in God-given human reason rather than church authority — was a formative contribution to the trajectory that led from Lutheran jurisprudence through Grotius to the Enlightenment natural rights tradition.",
            "significanceCategory": "continental"
        },
        "importanceScore": 7
    }
}


def enrich_entity(slug, data):
    fname = os.path.join(FOLDER, f"230{slug}.json")
    if not os.path.exists(fname):
        print(f"  SKIP (not found): {fname}")
        return
    with open(fname, "r", encoding="utf-8") as f:
        doc = json.load(f)
    entity = doc["entities"][0]
    det = json.loads(entity.get("detailsJson", "{}"))
    edit_log = det.get("_editLog", [])
    updated = []

    for field in ("summary", "importanceScore", "historicalSignificance"):
        if field in data:
            old = entity.get(field)
            entity[field] = data[field]
            edit_log.append({"timestamp": NOW, "editorId": EDITOR_ID, "field": field,
                             "oldValue": str(old)[:300], "newValue": str(data[field])[:300]})
            updated.append(field)

    for field in ("causes", "effects", "relationships"):
        if field in data:
            old = det.get(field, [])
            det[field] = data[field]
            edit_log.append({"timestamp": NOW, "editorId": EDITOR_ID, "field": field,
                             "oldValue": json.dumps(old)[:300], "newValue": json.dumps(data[field])[:300]})
            updated.append(field)

    det["_editLog"] = edit_log
    det["_unsyncedEdits"] = True
    entity["_unsyncedEdits"] = True
    entity["detailsJson"] = json.dumps(det, ensure_ascii=False)
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)

    slen = len(entity.get("summary", ""))
    print(f"  ✓ {entity['name']} — sum={slen}c c={len(det.get('causes',[]))} "
          f"e={len(det.get('effects',[]))} r={len(det.get('relationships',[]))}")


if __name__ == "__main__":
    print(f"Enriching {len(ENRICHMENTS)} entities (Batch 6: cross-cultural legal)...")
    for slug, data in ENRICHMENTS.items():
        enrich_entity(slug, data)
    print("\nDone.")
