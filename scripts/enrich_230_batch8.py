#!/usr/bin/env python3
"""
Batch 8: Archbishop Simon Sudbury (Peasants' Revolt), Cardinal Henry Beaufort,
Crusader jurist John of Ibelin, Yemeni polymath Nashwān al-Ḥimyarī,
Spanish jurist Alfonso de Montalvo, Norman bishop Herfast,
Wars of the Roses magnate Richard Neville 5th Earl of Salisbury,
Polish bishop-canonist Piotr Wysz Radoliński.
"""

import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/230-Class-230"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()

ENRICHMENTS = {
    "simon-sudbury": {
        "summary": (
            "Simon Sudbury (c. 1316–1381) was Archbishop of Canterbury (1375–1381) and "
            "Lord Chancellor of England under Richard II — whose murder by rebels during "
            "the Peasants' Revolt of 1381 made him one of the most dramatic victims of "
            "popular violence in English medieval history. A canon lawyer trained at Paris, "
            "he had risen through episcopal service to become Bishop of London (1362) and "
            "then Archbishop, the highest ecclesiastical office in England.\n\n"
            "Sudbury served simultaneously as Lord Chancellor from 1380 to 1381 — a "
            "position that placed him in political leadership at the worst possible moment. "
            "The Poll Tax of 1381, levied at a flat rate per head, was deeply regressive "
            "and massively resented across England. When the Peasants' Revolt erupted in "
            "June 1381, Wat Tyler's rebels focused their fury on the architects of hated "
            "government policy. Sudbury, as both chancellor and archbishop, was a primary "
            "target. The rebels marched on London, entered the Tower of London, and found "
            "Sudbury at prayer in the Tower chapel. Dragged to Tower Hill, he was "
            "clumsily beheaded — a contemporary account suggests it took eight blows — "
            "and his head was displayed on London Bridge.\n\n"
            "Sudbury had actually tried to address some grievances: he had personally "
            "preached against the violence and attempted to negotiate. His execution "
            "shocked England and contributed to the rapid collapse of royal authority "
            "that briefly threatened Richard II's government. He had earlier played a "
            "role in the trial of John Wycliffe (1377) and was known as a capable "
            "if not brilliant ecclesiastical administrator. His skull, preserved at "
            "St Gregory's Church in Sudbury, Suffolk — his birthplace — remains on "
            "display today."
        ),
        "causes": [
            {
                "title": "The Poll Tax of 1381 — levied at a flat rate per head — was the immediate trigger for the Peasants' Revolt; as Lord Chancellor, Sudbury was associated with its implementation",
                "type": "EventWindow",
                "year": "1381, England"
            },
            {
                "title": "Sudbury's dual role as Lord Chancellor and Archbishop made him a symbol of the ecclesiastical-royal establishment that the rebels held responsible for exploitative taxation",
                "type": "Person",
                "year": "1380–1381, England"
            },
            {
                "title": "Sudbury's earlier role in the trial of John Wycliffe (1377) had associated him with the suppression of popular religious reform movements",
                "type": "EventWindow",
                "year": "1377, London"
            }
        ],
        "effects": [
            {
                "title": "Sudbury's murder during the Peasants' Revolt was the most dramatic incident in what temporarily threatened to overturn Richard II's government",
                "type": "EventWindow",
                "year": "1381, London"
            },
            {
                "title": "The vacancy of the archbishopric following Sudbury's murder led to William Courtenay's appointment — who pursued an aggressive anti-Lollard policy",
                "type": "Institution",
                "year": "1381, England"
            },
            {
                "title": "Sudbury's brutal death became a widely reported symbol of the dangers facing royal ministers during the Peasants' Revolt and was invoked in subsequent political discourse",
                "type": "Idea",
                "year": "1381–1400, England"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "simon-sudbury",
                "sourceName": "Simon Sudbury",
                "verb": "MURDERED_IN",
                "targetSlug": "peasants-revolt-1381",
                "targetName": "Peasants' Revolt (1381)",
                "context": "Sudbury was dragged from the Tower of London and beheaded on Tower Hill by Peasants' Revolt rebels on 14 June 1381"
            },
            {
                "sourceSlug": "simon-sudbury",
                "sourceName": "Simon Sudbury",
                "verb": "TRIED",
                "targetSlug": "john-wycliffe",
                "targetName": "John Wycliffe",
                "context": "Sudbury presided over the controversial trial of Wycliffe in 1377, which was interrupted by the intervention of John of Gaunt and never concluded"
            },
            {
                "sourceSlug": "simon-sudbury",
                "sourceName": "Simon Sudbury",
                "verb": "SERVED_UNDER",
                "targetSlug": "richard-ii-of-england",
                "targetName": "Richard II of England",
                "context": "Sudbury served Richard II as Lord Chancellor from 1380 until his execution in 1381"
            },
            {
                "sourceSlug": "simon-sudbury",
                "sourceName": "Simon Sudbury",
                "verb": "SUCCEEDED_BY",
                "targetSlug": "william-courtenay",
                "targetName": "William Courtenay",
                "context": "William Courtenay succeeded Sudbury as Archbishop of Canterbury and pursued an aggressive anti-Lollard program"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Simon Sudbury's murder during the Peasants' Revolt of 1381 — dragged from the Tower of London and clumsily beheaded — was the most dramatic individual act of the revolt and the most violent direct attack on the ecclesiastical-royal establishment in 14th-century England.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "henry-beaufort": {
        "summary": (
            "Henry Beaufort (c. 1375–1447) was Cardinal-Bishop of Winchester, three times "
            "Lord Chancellor of England, and for three decades one of the most powerful "
            "men in the realm — a figure who embodied the late medieval fusion of "
            "ecclesiastical wealth, royal patronage, and political ambition. The legitimated "
            "son of John of Gaunt (Duke of Lancaster) and Katherine Swynford, he was a "
            "half-brother of Henry IV and great-uncle of Henry VI, giving him the highest "
            "possible position in the royal family without the crown itself.\n\n"
            "Beaufort served as Lord Chancellor in 1403–1405, 1413–1417, and 1424–1426, "
            "exercising control of the great seal under three kings. He was an "
            "indefatigable financier of the Hundred Years' War, lending the crown "
            "enormous sums from his personal fortune and leveraging these loans for "
            "political influence — he was at times effectively banker to the English "
            "state. Created cardinal-priest in 1426 by Pope Martin V (over Henry V's "
            "objections — the king feared a cardinal's divided loyalty), Beaufort combined "
            "papal and English authority in one formidable person. He led a crusade "
            "against the Hussites in 1427–1428 and presided over the trial of Joan of "
            "Arc in 1431 in his capacity as the senior English ecclesiastic in France.\n\n"
            "Beaufort's great rivalry was with Humphrey, Duke of Gloucester, Henry V's "
            "surviving brother. The two factions — Beaufort and the peace party versus "
            "Gloucester and the war party — defined English politics throughout Henry VI's "
            "minority and early reign. Beaufort survived Gloucester's fall in 1447, "
            "dying just weeks after his rival. Shakespeare's Henry VI plays, though "
            "historically distorted, captured the essential truth of Beaufort's "
            "extraordinary, morally ambiguous career."
        ),
        "causes": [
            {
                "title": "Henry Beaufort's position as a legitimated royal bastard — son of John of Gaunt, half-brother of Henry IV — gave him both the wealth and royal connections to achieve the highest offices",
                "type": "Person",
                "year": "c. 1375–1400, England"
            },
            {
                "title": "The chronic financial shortage of the English crown during the Hundred Years' War created opportunities for wealthy magnates like Beaufort to exchange loans for political leverage",
                "type": "EventWindow",
                "year": "1415–1447, England and France"
            },
            {
                "title": "The factional politics of Henry VI's minority — between pro-war and pro-peace parties — placed Beaufort at the center of English political conflict for a generation",
                "type": "Institution",
                "year": "1422–1447, England"
            }
        ],
        "effects": [
            {
                "title": "Beaufort presided over the trial of Joan of Arc (1431), one of the most consequential judicial proceedings of the Hundred Years' War",
                "type": "EventWindow",
                "year": "1431, Rouen"
            },
            {
                "title": "Beaufort's enormous personal loans to the English crown made him the de facto banker of the Hundred Years' War, shaping English financial and foreign policy for decades",
                "type": "Institution",
                "year": "1415–1447, England"
            },
            {
                "title": "The Beaufort-Gloucester rivalry defined the factional politics that eventually contributed to the breakdown of Lancastrian government leading to the Wars of the Roses",
                "type": "EventWindow",
                "year": "1422–1461, England"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "henry-beaufort",
                "sourceName": "Henry Beaufort",
                "verb": "SERVED_UNDER",
                "targetSlug": "henry-v-of-england",
                "targetName": "Henry V of England",
                "context": "Beaufort served Henry V as Lord Chancellor and as the king's trusted ecclesiastical-diplomatic instrument, though Henry opposed his cardinalate"
            },
            {
                "sourceSlug": "henry-beaufort",
                "sourceName": "Henry Beaufort",
                "verb": "PRESIDED_OVER",
                "targetSlug": "trial-of-joan-of-arc",
                "targetName": "Trial of Joan of Arc",
                "context": "Beaufort presided as the senior English ecclesiastic at the trial of Joan of Arc in Rouen in 1431"
            },
            {
                "sourceSlug": "henry-beaufort",
                "sourceName": "Henry Beaufort",
                "verb": "RIVALED",
                "targetSlug": "humphrey-duke-of-gloucester",
                "targetName": "Humphrey, Duke of Gloucester",
                "context": "Beaufort's peace faction and Gloucester's war faction defined English politics through Henry VI's minority and early reign"
            },
            {
                "sourceSlug": "henry-beaufort",
                "sourceName": "Henry Beaufort",
                "verb": "SON_OF",
                "targetSlug": "john-of-gaunt",
                "targetName": "John of Gaunt",
                "context": "Beaufort was the legitimated son of John of Gaunt and Katherine Swynford, giving him royal blood and the vast Lancastrian network"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Henry Beaufort's triple tenure as Lord Chancellor, his personal financing of the Hundred Years' War, and his presidency at the trial of Joan of Arc made him one of the most powerful and consequential political-ecclesiastical figures of 15th-century England — a cardinal-statesman whose career spanned three reigns and shaped both war and peace policy.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "john-of-ibelin": {
        "summary": (
            "John of Ibelin, Count of Jaffa and Ascalon (c. 1215–1266), was the greatest "
            "legal scholar of the Crusader states — a nobleman-jurist of the Kingdom of "
            "Jerusalem whose Le Livre de Jean d'Ibelin (The Book of John of Ibelin) is "
            "the most comprehensive and authoritative legal treatise on the feudal law "
            "of the Crusader kingdom. The Ibelin family were the dominant noble dynasty "
            "of 13th-century Outremer, combining military power, political leadership, "
            "and legal scholarship in a way unparalleled in Crusader history.\n\n"
            "The Livre is a systematic exposition of the law and customs of the Kingdom "
            "of Jerusalem — its feudal obligations, the structure of the High Court, "
            "the laws of succession, the rights of liege lords and vassals, and the "
            "procedures of legal combat. Written in vernacular Old French, it reflected "
            "both the sophisticated legal culture of the Frankish settlers and the unique "
            "constitutional situation of a kingdom where the nobles had won enormous "
            "concessions from weak kings. John's treatise was the authoritative "
            "statement of the 'Assizes of Jerusalem' — the body of law claimed to "
            "derive from Godfrey of Bouillon's original legislation, though much was "
            "actually developed over the 12th and 13th centuries.\n\n"
            "John combined legal writing with active political and military life: he fought "
            "in multiple campaigns, served on the High Court, and navigated the "
            "extraordinarily complex politics of later 13th-century Outremer — including "
            "the conflicts surrounding Frederick II's crusade, the regency struggles, "
            "and the eventual loss of Jerusalem to Sultan Al-Kamil in 1244. The Livre "
            "was copied, quoted, and used as authoritative legal reference throughout "
            "the remainder of the Crusader period and remains the primary source for "
            "understanding the legal culture of the Latin East."
        ),
        "causes": [
            {
                "title": "The Kingdom of Jerusalem's unique constitutional situation — where powerful barons had won major concessions from weak kings — required a systematic legal framework to manage noble rights and royal authority",
                "type": "Institution",
                "year": "c. 1200–1250, Kingdom of Jerusalem"
            },
            {
                "title": "The Ibelin family's dominant political position gave John both the authority and the motivation to codify the feudal law in a way that protected baronial rights against royal encroachment",
                "type": "Person",
                "year": "c. 1215–1266, Outremer"
            },
            {
                "title": "Frederick II's 1229 crusade — which recovered Jerusalem by treaty rather than conquest and tried to reduce baronial autonomy — created the political crisis that made systematic legal codification urgent for the nobility",
                "type": "EventWindow",
                "year": "1229–1243, Kingdom of Jerusalem"
            }
        ],
        "effects": [
            {
                "title": "Le Livre de Jean d'Ibelin became the authoritative legal treatise on feudal law in the Crusader states, cited and used throughout the remainder of the Crusader period",
                "type": "Text",
                "year": "c. 1260–1290, Outremer"
            },
            {
                "title": "The Livre's codification of the Assizes of Jerusalem is the primary source for understanding the constitutional and legal culture of the Latin East",
                "type": "Text",
                "year": "1260 – present, historical scholarship"
            },
            {
                "title": "The Ibelin legal tradition influenced later Crusader legal writing in Cyprus, where the Ibelin family retained power after the fall of the mainland kingdom",
                "type": "Institution",
                "year": "1291–1400, Cyprus"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "john-of-ibelin",
                "sourceName": "John of Ibelin",
                "verb": "AUTHORED",
                "targetSlug": "livre-de-jean-dibelin",
                "targetName": "Le Livre de Jean d'Ibelin",
                "context": "John's Livre is the most comprehensive legal treatise on the feudal law of the Kingdom of Jerusalem and the primary source for the Assizes of Jerusalem"
            },
            {
                "sourceSlug": "john-of-ibelin",
                "sourceName": "John of Ibelin",
                "verb": "MEMBER_OF",
                "targetSlug": "ibelin-family",
                "targetName": "House of Ibelin",
                "context": "The Ibelin family were the dominant noble dynasty of 13th-century Outremer; John was Count of Jaffa and Ascalon and the family's greatest legal scholar"
            },
            {
                "sourceSlug": "john-of-ibelin",
                "sourceName": "John of Ibelin",
                "verb": "OPPOSED",
                "targetSlug": "frederick-ii-holy-roman-emperor",
                "targetName": "Frederick II, Holy Roman Emperor",
                "context": "The Ibelin family opposed Frederick II's attempts to reduce baronial autonomy during his 1229 crusade, using the legal traditions John subsequently codified to justify their resistance"
            },
            {
                "sourceSlug": "john-of-ibelin",
                "sourceName": "John of Ibelin",
                "verb": "CODIFIED",
                "targetSlug": "assizes-of-jerusalem",
                "targetName": "Assizes of Jerusalem",
                "context": "John's Livre is the primary codification of the body of feudal law known as the Assizes of Jerusalem"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "John of Ibelin's Le Livre de Jean d'Ibelin — the most comprehensive treatise on the feudal law of the Crusader states — is the primary source for understanding the legal and constitutional culture of the Latin East, codifying a unique experiment in Frankish feudal governance in the medieval Levant.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "nashwān-ibn-saʻīd-al-ḥimyarī": {
        "summary": (
            "Nashwān ibn Saʻīd al-Ḥimyarī (c. 1040–1178 CE) was a Yemeni poet, "
            "grammarian, lexicographer, historian, and theological controversialist — "
            "one of the most learned and prolific scholars of medieval Yemen, whose "
            "work preserves irreplaceable knowledge about pre-Islamic Arabian history, "
            "culture, and the Arabic language. He lived in a period of intense political "
            "and religious upheaval in Yemen, caught between Ismaili (Fatimid-linked) "
            "and Zaydi Shia factions and the remnants of Ḥimyarite dynastic tradition, "
            "and his writings reflect his engagement with all of these currents.\n\n"
            "Nashwān's greatest scholarly work is Shams al-ʿUlūm wa-dawāʾ kalām al-ʿArab "
            "min al-kulūm (The Sun of Knowledge, and the Cure for Arab Speech's Wounds) — "
            "a monumental Arabic encyclopedic lexicon arranged alphabetically by "
            "root, covering vocabulary, grammar, proverbs, genealogy, history, and "
            "natural history. It is one of the most comprehensive Arabic lexicographical "
            "works of the medieval period and an essential source for the study of "
            "classical Arabic. Nashwān also wrote Al-Qaṣīda al-Ḥimyariyya, a celebrated "
            "long poem about the ancient kings of Yemen (the Ḥimyarites), which is a "
            "major source for the pre-Islamic history of Arabia, and its commentary "
            "Muntakhabāt preserves detailed historical and genealogical traditions "
            "about the pre-Islamic South Arabian kingdoms.\n\n"
            "Nashwān was a controversial figure in his own time: his theological views "
            "— he defended a form of Mutazilite rationalism — brought him into conflict "
            "with the Zaydi imams of Yemen, and he engaged in polemical debates throughout "
            "his long life. His work's extraordinary range — from poetry to lexicography "
            "to political history to theology — made him the most important Yemeni "
            "intellectual figure of the 12th century and one of the most significant "
            "Arabic scholars of the medieval Islamic world."
        ),
        "causes": [
            {
                "title": "The richness of the pre-Islamic Ḥimyarite tradition in Yemen — a largely uncodified oral and inscriptional heritage — motivated Nashwān to compile and preserve it in literary Arabic",
                "type": "Institution",
                "year": "c. 1060–1178, Yemen"
            },
            {
                "title": "The linguistic diversity and rapid change of Arabic in the 12th century created a need for comprehensive lexicographical reference works of which Shams al-ʿUlūm is the most ambitious",
                "type": "Idea",
                "year": "c. 1100–1170, Yemen and Arabia"
            },
            {
                "title": "The theological controversies between Zaydi, Ismaili, and Mutazilite traditions in Yemen drove Nashwān's polemical writings and gave his scholarship its argumentative edge",
                "type": "Movement",
                "year": "c. 1060–1178, Yemen"
            }
        ],
        "effects": [
            {
                "title": "Shams al-ʿUlūm — Nashwān's encyclopedic Arabic lexicon — is an essential source for classical Arabic vocabulary, grammar, and the pre-Islamic Arabian heritage",
                "type": "Text",
                "year": "c. 1150–1178, Yemen"
            },
            {
                "title": "Al-Qaṣīda al-Ḥimyariyya and its commentary preserve the most detailed medieval account of the pre-Islamic kings of Yemen and the Ḥimyarite dynasty",
                "type": "Text",
                "year": "c. 1100–1178, Yemen"
            },
            {
                "title": "Nashwān's preservation of South Arabian oral traditions in literary Arabic ensured the survival of historical and linguistic knowledge about pre-Islamic Arabia available nowhere else",
                "type": "Idea",
                "year": "12th century CE – present"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "nashwān-ibn-saʻīd-al-ḥimyarī",
                "sourceName": "Nashwān ibn Saʻīd al-Ḥimyarī",
                "verb": "AUTHORED",
                "targetSlug": "shams-al-ulum",
                "targetName": "Shams al-ʿUlūm",
                "context": "Nashwān's encyclopedic Arabic lexicon is one of the most comprehensive medieval Arabic reference works and an essential source for classical Arabic studies"
            },
            {
                "sourceSlug": "nashwān-ibn-saʻīd-al-ḥimyarī",
                "sourceName": "Nashwān ibn Saʻīd al-Ḥimyarī",
                "verb": "AUTHORED",
                "targetSlug": "al-qasida-al-himyariyya",
                "targetName": "Al-Qaṣīda al-Ḥimyariyya",
                "context": "Nashwān's long poem on the pre-Islamic Ḥimyarite kings is the most detailed medieval account of Yemen's pre-Islamic royal heritage"
            },
            {
                "sourceSlug": "nashwān-ibn-saʻīd-al-ḥimyarī",
                "sourceName": "Nashwān ibn Saʻīd al-Ḥimyarī",
                "verb": "DEBATED",
                "targetSlug": "zaydi-imamate",
                "targetName": "Zaydi Imamate of Yemen",
                "context": "Nashwān engaged in ongoing theological polemic with the Zaydi imams of Yemen, defending Mutazilite rational theology"
            },
            {
                "sourceSlug": "nashwān-ibn-saʻīd-al-ḥimyarī",
                "sourceName": "Nashwān ibn Saʻīd al-Ḥimyarī",
                "verb": "PRESERVED",
                "targetSlug": "himyarite-tradition",
                "targetName": "Ḥimyarite Historical Tradition",
                "context": "Nashwān systematically preserved pre-Islamic South Arabian royal traditions that might otherwise have been lost"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Nashwān ibn Saʻīd al-Ḥimyarī's encyclopedic lexicon Shams al-ʿUlūm and his Al-Qaṣīda al-Ḥimyariyya are the most comprehensive medieval Arabic sources for classical Arabic vocabulary and pre-Islamic South Arabian history respectively — making him the most important Yemeni intellectual of the medieval Islamic world.",
            "significanceCategory": "continental"
        },
        "importanceScore": 8
    },

    "alfonso-díaz-de-montalvo": {
        "summary": (
            "Alfonso Díaz de Montalvo (c. 1405–1499) was a Spanish jurist, judge, and "
            "legal compiler whose two great compilations — the Fuero Real commentary "
            "(c. 1484) and the Ordenanzas Reales de Castilla (1484–1485) — were the "
            "first printed compilations of Castilian royal law and served as the "
            "primary legal reference for the Crown of Castile for almost a century. "
            "A judge of the Audiencia Real (the supreme royal court), Montalvo had "
            "direct knowledge of the accumulated body of Castilian law and the "
            "practical problems created by its dispersion across hundreds of "
            "separate royal ordinances.\n\n"
            "Montalvo compiled the Ordenanzas Reales de Castilla (Royal Ordinances "
            "of Castile) on commission from the Catholic Monarchs Ferdinand and Isabella, "
            "who recognized the urgent need to systematize the chaotic body of Castilian "
            "legislation accumulated over two centuries. His eight-volume compilation "
            "organized existing royal ordinances, fueros (local charters), and pragmatics "
            "into a coherent reference work — printed by Hagenbach in Toledo in 1484 — "
            "that gave royal judges, notaries, and legal practitioners for the first time "
            "a comprehensive, accessible guide to Castilian royal law. The Ordenanzas "
            "became the standard legal reference until the Nueva Recopilación of 1567 "
            "superseded it.\n\n"
            "Montalvo also produced an extensive gloss commentary on the Fuero Real — "
            "the old 13th-century Alfonsine code — explaining its provisions in light "
            "of subsequent royal legislation and Roman and canon law principles. He "
            "was an early adopter of the printing press for legal publication: his "
            "works were among the earliest printed legal texts in Spain. His combination "
            "of judicial experience, encyclopedic legal knowledge, and the printing "
            "press made him the creator of accessible, systematic Castilian legal "
            "reference literature at the dawn of Spain's imperial age."
        ),
        "causes": [
            {
                "title": "The Catholic Monarchs' project of royal centralization and legal unification required a systematic compilation of Castilian law to replace the chaotic accumulation of medieval ordinances",
                "type": "Institution",
                "year": "c. 1475–1485, Castile"
            },
            {
                "title": "The introduction of the printing press to Spain made the mass distribution of legal reference works economically viable for the first time",
                "type": "Idea",
                "year": "c. 1472–1484, Spain"
            },
            {
                "title": "Montalvo's position as a judge of the Audiencia Real gave him direct experience of the practical problems caused by the dispersion of Castilian law across hundreds of separate texts",
                "type": "Institution",
                "year": "c. 1460–1499, Castile"
            }
        ],
        "effects": [
            {
                "title": "Ordenanzas Reales de Castilla (1484–1485) was the first printed systematic compilation of Castilian royal law, serving as the primary legal reference for Castile until 1567",
                "type": "Text",
                "year": "1484–1567, Castile/Spain"
            },
            {
                "title": "Montalvo's legal works were among the earliest printed legal texts in Spain, establishing the print medium as the vehicle for legal publication and dissemination",
                "type": "Idea",
                "year": "1484–1500, Spain"
            },
            {
                "title": "The Ordenanzas provided the legal framework within which the Catholic Monarchs' centralizing reforms — including the Inquisition, Columbus's patent, and the expulsion of Jews — were formally grounded",
                "type": "Institution",
                "year": "1484–1492, Spain"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "alfonso-díaz-de-montalvo",
                "sourceName": "Alfonso Díaz de Montalvo",
                "verb": "COMPILED_FOR",
                "targetSlug": "ferdinand-and-isabella",
                "targetName": "Ferdinand and Isabella (Catholic Monarchs)",
                "context": "Montalvo compiled the Ordenanzas Reales on commission from Ferdinand and Isabella as part of their centralizing reform of Castilian governance"
            },
            {
                "sourceSlug": "alfonso-díaz-de-montalvo",
                "sourceName": "Alfonso Díaz de Montalvo",
                "verb": "AUTHORED",
                "targetSlug": "ordenanzas-reales-de-castilla",
                "targetName": "Ordenanzas Reales de Castilla",
                "context": "Montalvo's 1484–1485 compilation was the first printed systematic collection of Castilian royal ordinances and the standard legal reference for nearly a century"
            },
            {
                "sourceSlug": "alfonso-díaz-de-montalvo",
                "sourceName": "Alfonso Díaz de Montalvo",
                "verb": "SERVED_ON",
                "targetSlug": "audiencia-real-of-castile",
                "targetName": "Audiencia Real of Castile",
                "context": "Montalvo served as a judge of the Audiencia Real, the supreme royal court of Castile, giving him direct knowledge of Castilian legal practice"
            },
            {
                "sourceSlug": "alfonso-díaz-de-montalvo",
                "sourceName": "Alfonso Díaz de Montalvo",
                "verb": "INFLUENCED",
                "targetSlug": "nueva-recopilacion-1567",
                "targetName": "Nueva Recopilación (1567)",
                "context": "The Ordenanzas served as the primary legal reference until the Nueva Recopilación of 1567 superseded it, building on Montalvo's organizational framework"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Alfonso Díaz de Montalvo's Ordenanzas Reales de Castilla — the first printed systematic compilation of Castilian royal law — provided the legal framework for the Catholic Monarchs' centralizing reforms at the dawn of Spain's imperial age, serving as the primary Castilian legal reference for nearly a century.",
            "significanceCategory": "continental"
        },
        "importanceScore": 8
    },

    "herfast": {
        "summary": (
            "Herfast (d. c. 1084/1085) was a Norman churchman and royal administrator who "
            "served William the Conqueror as royal chancellor before his appointment as "
            "Bishop of Elmham (1070) — subsequently translated to the new see of Thetford "
            "(1075) as part of the Conqueror's reorganization of the English church. A "
            "figure at the intersection of Norman royal administration and the post-Conquest "
            "restructuring of the English episcopate, Herfast's career illustrates both "
            "the Norman pattern of appointing royal clerks to English bishoprics and the "
            "tensions this generated.\n\n"
            "Herfast was a controversial bishop: Lanfranc, the great Norman Archbishop "
            "of Canterbury, wrote to him criticizing his personal conduct — his fondness "
            "for dice and his administrative failures. More substantially, he was involved "
            "in the primacy dispute between Canterbury and York: he submitted to Lanfranc's "
            "authority as Archbishop of Canterbury rather than supporting York's claim to "
            "metropolitan authority over the northern and eastern dioceses. He also came "
            "into conflict with Herbert de Losinga (future Bishop of Norwich) over the "
            "monastery of Bury St Edmunds, which Herfast tried unsuccessfully to bring "
            "under episcopal control.\n\n"
            "Contemporary sources, particularly the monk-chroniclers who resented secular "
            "bishops, treated Herfast harshly — accusing him of ignorance and worldliness. "
            "But he was clearly an able royal administrator before his episcopal career, "
            "and his appointment to Elmham/Thetford reflected William's standard pattern "
            "of rewarding loyal chancery clerks with bishoprics. He was among the first "
            "generation of Norman bishops who replaced the English episcopal hierarchy "
            "after 1066 — part of the wholesale ecclesiastical transformation that "
            "accompanied the Conquest."
        ),
        "causes": [
            {
                "title": "William the Conqueror's policy of replacing English bishops with loyal Norman royal clerks created the pattern of appointments that brought Herfast to the English episcopate",
                "type": "Institution",
                "year": "1066–1075, England"
            },
            {
                "title": "The post-Conquest reorganization of the English church — moving sees to larger towns and imposing Norman administrative practices — drove the creation of the Thetford see",
                "type": "Institution",
                "year": "1070–1075, England"
            },
            {
                "title": "Herfast's service as royal chancellor gave him the administrative experience that made him useful to William as a bishop-administrator in East Anglia",
                "type": "Person",
                "year": "c. 1068–1070, England"
            }
        ],
        "effects": [
            {
                "title": "Herfast's submission to Lanfranc's Canterbury primacy contributed to the resolution of the Canterbury-York dispute in Canterbury's favor for the eastern dioceses",
                "type": "Institution",
                "year": "c. 1073–1075, England"
            },
            {
                "title": "His failed attempt to control Bury St Edmunds contributed to the growing independence of major English monasteries from episcopal oversight",
                "type": "Institution",
                "year": "c. 1075–1085, East Anglia"
            },
            {
                "title": "Herfast was part of the first generation of Norman bishops who irreversibly Normanized the English episcopate after the Conquest",
                "type": "Institution",
                "year": "1066–1090, England"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "herfast",
                "sourceName": "Herfast",
                "verb": "SERVED_UNDER",
                "targetSlug": "william-the-conqueror",
                "targetName": "William the Conqueror",
                "context": "Herfast served as royal chancellor under William I before his appointment as bishop, part of the Conqueror's pattern of rewarding loyal clerks with bishoprics"
            },
            {
                "sourceSlug": "herfast",
                "sourceName": "Herfast",
                "verb": "CRITICIZED_BY",
                "targetSlug": "lanfranc",
                "targetName": "Lanfranc of Canterbury",
                "context": "Lanfranc wrote to Herfast criticizing his personal conduct (dice-playing) and administrative failures as bishop"
            },
            {
                "sourceSlug": "herfast",
                "sourceName": "Herfast",
                "verb": "SUBMITTED_TO",
                "targetSlug": "lanfranc",
                "targetName": "Lanfranc of Canterbury",
                "context": "Herfast submitted to Lanfranc's authority as Archbishop of Canterbury in the primacy dispute, supporting Canterbury's claims against York"
            },
            {
                "sourceSlug": "herfast",
                "sourceName": "Herfast",
                "verb": "BISHOP_OF",
                "targetSlug": "bishopric-of-thetford",
                "targetName": "Bishopric of Thetford",
                "context": "Herfast was the first bishop of the newly created see of Thetford (from 1075), following the Norman policy of moving sees to larger towns"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Herfast, as royal chancellor turned Norman bishop, was part of the first generation that Normanized the English episcopal hierarchy after 1066 — a transformation that permanently changed English church governance. His involvement in the Canterbury-York primacy dispute contributed to its resolution in Canterbury's favor.",
            "significanceCategory": "local"
        },
        "importanceScore": 7
    },

    "richard-neville-5th-earl-of-salisbury": {
        "summary": (
            "Richard Neville, 5th Earl of Salisbury (1400–1460) was one of the most "
            "powerful magnates in 15th-century England and the senior Yorkist leader in "
            "the early phase of the Wars of the Roses — father of Richard Neville, the "
            "'Kingmaker' (16th Earl of Warwick), and one of the three figures who "
            "together constituted the Yorkist leadership that challenged the Lancastrian "
            "government of Henry VI. He served briefly as Lord Chancellor under Henry VI "
            "in 1454–1455 during the first protectorate of Richard Duke of York.\n\n"
            "Salisbury acquired his earldom through his mother Joan Beaufort (daughter "
            "of John of Gaunt), which gave him both high royal connections and the vast "
            "Neville inheritance. His lands in Yorkshire and the north made him one of "
            "the great magnates of the north of England. The feud between the Nevilles "
            "and the Percy family — which had deep roots in northern magnate rivalry — "
            "was one of the triggers of the Wars of the Roses, the Battle of Heworth "
            "Moor (1453) being an early violent encounter between their retinues.\n\n"
            "Salisbury fought at the First Battle of St Albans (1455) on the Yorkist side "
            "and at the Battle of Blore Heath (1459), where he won a significant Yorkist "
            "victory. After the Yorkist defeat at the Battle of Wakefield (December 1460), "
            "he was captured by Lancastrian forces and executed the following day — not "
            "on the battlefield but in a deliberate Lancastrian decision to remove him "
            "as a Yorkist leader. He died before his son Warwick and the Yorkist cause "
            "triumphed with the accession of Edward IV in 1461."
        ),
        "causes": [
            {
                "title": "The breakdown of Lancastrian royal authority under Henry VI's government created the factional vacuum that escalated the Neville-Percy feud into open warfare",
                "type": "Person",
                "year": "1450–1455, England"
            },
            {
                "title": "The long-standing northern England rivalry between the Neville and Percy families over land, influence, and political supremacy was a structural cause of the Wars of the Roses",
                "type": "Institution",
                "year": "c. 1420–1460, northern England"
            },
            {
                "title": "Salisbury's dynastic connections — son of the Beaufort line through his mother, father of the Kingmaker — placed him at the intersection of every major aristocratic network in England",
                "type": "Person",
                "year": "c. 1420–1460, England"
            }
        ],
        "effects": [
            {
                "title": "Salisbury's leadership of the Neville affinity in the early Wars of the Roses gave the Yorkist cause a powerful northern magnate base without which it could not have challenged Lancastrian power",
                "type": "EventWindow",
                "year": "1455–1460, England"
            },
            {
                "title": "His execution at Wakefield (1460) and his son Warwick's subsequent leadership cemented the Neville family as the kingmakers of the Yorkist triumph",
                "type": "EventWindow",
                "year": "1460–1461, England"
            },
            {
                "title": "Salisbury's tenure as Lord Chancellor during York's first protectorate (1454–1455) was a key moment in the constitutional conflict over royal authority in Henry VI's reign",
                "type": "Institution",
                "year": "1454–1455, England"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "richard-neville-5th-earl-of-salisbury",
                "sourceName": "Richard Neville, 5th Earl of Salisbury",
                "verb": "FATHER_OF",
                "targetSlug": "richard-neville-earl-of-warwick",
                "targetName": "Richard Neville, Earl of Warwick ('Kingmaker')",
                "context": "Salisbury was the father of Richard Neville the Kingmaker, the most powerful political figure of the Wars of the Roses"
            },
            {
                "sourceSlug": "richard-neville-5th-earl-of-salisbury",
                "sourceName": "Richard Neville, 5th Earl of Salisbury",
                "verb": "ALLIED_WITH",
                "targetSlug": "richard-duke-of-york",
                "targetName": "Richard, Duke of York",
                "context": "Salisbury allied with Richard of York against the Lancastrian government, forming the Yorkist coalition that launched the Wars of the Roses"
            },
            {
                "sourceSlug": "richard-neville-5th-earl-of-salisbury",
                "sourceName": "Richard Neville, 5th Earl of Salisbury",
                "verb": "FOUGHT_AT",
                "targetSlug": "first-battle-of-st-albans",
                "targetName": "First Battle of St Albans (1455)",
                "context": "Salisbury fought on the Yorkist side at the First Battle of St Albans, the opening battle of the Wars of the Roses"
            },
            {
                "sourceSlug": "richard-neville-5th-earl-of-salisbury",
                "sourceName": "Richard Neville, 5th Earl of Salisbury",
                "verb": "EXECUTED_AFTER",
                "targetSlug": "battle-of-wakefield",
                "targetName": "Battle of Wakefield (1460)",
                "context": "Salisbury was captured at Wakefield in December 1460 and executed the following day by Lancastrian forces"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Richard Neville, 5th Earl of Salisbury provided the powerful northern magnate base without which the Yorkist challenge to Lancastrian power in the Wars of the Roses could not have succeeded; as father of the Kingmaker and briefly Lord Chancellor, he was a central figure in the opening phase of the dynastic conflict that transformed England.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "piotr-wysz-radoliński": {
        "summary": (
            "Piotr Wysz Radoliński (c. 1354–1414) was a Polish bishop, canonist, and "
            "university rector who was one of the most eminent ecclesiastical figures of "
            "late medieval Poland. Educated in canon law at Padua, he served as the first "
            "rector of the restored Jagiellonian University of Kraków (1400–1401), as "
            "Bishop of Kraków (1392–1412), and as a Polish delegate to the Council of "
            "Pisa (1409) — the council that attempted to end the Great Schism by "
            "deposing both existing popes and electing a new one (resulting in three "
            "simultaneous claimants).\n\n"
            "Piotr's career intersected with several of the major events of his era. "
            "As Bishop of Kraków, he was one of the senior ecclesiastics at the Polish "
            "royal court under King Władysław II Jagiełło — the Lithuanian-born king "
            "who had converted to Christianity and united Poland and Lithuania. Piotr "
            "participated in the constitutional and ecclesiastical consolidation of the "
            "Jagiellonian dynasty, lending church authority to the new dynastic order. "
            "His legal training in canon law at Padua gave him the technical expertise "
            "for both episcopal administration and diplomatic service.\n\n"
            "His role in refounding the Jagiellonian University was particularly "
            "significant: the original University of Kraków (1364) had lapsed, and "
            "the 1400 refoundation — supported by Queen Jadwiga's personal treasures — "
            "was one of the formative intellectual events of Polish culture. As its "
            "first rector, Piotr helped establish the institution that would become "
            "Poland's premier university. He was transferred to the see of Poznań "
            "in 1412, ending his Kraków administration, and died in 1414, the year "
            "the Council of Constance began — the council that finally ended the "
            "Great Schism he had worked to resolve at Pisa."
        ),
        "causes": [
            {
                "title": "The Jagiellonian dynasty's need for canonically trained ecclesiastics to manage Poland's church administration and diplomatic relations with Rome created Piotr's importance",
                "type": "Institution",
                "year": "c. 1386–1412, Poland"
            },
            {
                "title": "Queen Jadwiga's personal sponsorship of the Jagiellonian University's refoundation in 1400 required a canonically trained bishop-rector to give the institution its initial shape",
                "type": "Institution",
                "year": "1400–1401, Kraków"
            },
            {
                "title": "The Great Schism (1378–1417) — which divided the Catholic Church between two competing popes — made the Council of Pisa and Piotr's participation in it a matter of urgent ecclesiastical diplomacy",
                "type": "EventWindow",
                "year": "1378–1409, Catholic Church"
            }
        ],
        "effects": [
            {
                "title": "Piotr's leadership as first rector of the refounded Jagiellonian University helped establish the institution that became Poland's premier university",
                "type": "Institution",
                "year": "1400–1414, Kraków"
            },
            {
                "title": "His participation in the Council of Pisa (1409) contributed to Poland's active engagement in the resolution of the Great Schism",
                "type": "EventWindow",
                "year": "1409, Pisa"
            },
            {
                "title": "Piotr's canonical legal training and episcopal authority provided legitimacy to the consolidation of the Jagiellonian dynasty's position in Poland and Lithuania",
                "type": "Institution",
                "year": "c. 1392–1412, Poland"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "piotr-wysz-radoliński",
                "sourceName": "Piotr Wysz Radoliński",
                "verb": "RECTOR_OF",
                "targetSlug": "jagiellonian-university",
                "targetName": "Jagiellonian University, Kraków",
                "context": "Piotr was the first rector of the refounded Jagiellonian University in 1400–1401, helping establish Poland's premier academic institution"
            },
            {
                "sourceSlug": "piotr-wysz-radoliński",
                "sourceName": "Piotr Wysz Radoliński",
                "verb": "SERVED_UNDER",
                "targetSlug": "wladyslaw-ii-jagiello",
                "targetName": "Władysław II Jagiełło",
                "context": "Piotr served as Bishop of Kraków under Władysław II Jagiełło, providing canonical legitimacy to the Jagiellonian dynasty's consolidation of Poland"
            },
            {
                "sourceSlug": "piotr-wysz-radoliński",
                "sourceName": "Piotr Wysz Radoliński",
                "verb": "PARTICIPATED_IN",
                "targetSlug": "council-of-pisa",
                "targetName": "Council of Pisa (1409)",
                "context": "Piotr represented Poland at the Council of Pisa, which attempted to end the Great Schism by deposing both existing popes and electing a new one"
            },
            {
                "sourceSlug": "piotr-wysz-radoliński",
                "sourceName": "Piotr Wysz Radoliński",
                "verb": "STUDIED_AT",
                "targetSlug": "university-of-padua",
                "targetName": "University of Padua",
                "context": "Piotr studied canon law at Padua, giving him the legal training that shaped his episcopal career and university rectorship"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Piotr Wysz Radoliński's career — as the first rector of the refounded Jagiellonian University, Bishop of Kraków under the Jagiellonian dynasty, and Polish delegate to the Council of Pisa — placed him at the intersection of the three great formative processes of late medieval Poland: academic culture, dynastic consolidation, and Great Schism diplomacy.",
            "significanceCategory": "continental"
        },
        "importanceScore": 8
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


if __name__ == "__main__":
    print(f"Enriching {len(ENRICHMENTS)} entities (Batch 8: medieval Europe/Islam/Asia)...")
    for slug, data in ENRICHMENTS.items():
        enrich_entity(slug, data)
    print("\nDone.")
