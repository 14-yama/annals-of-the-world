#!/usr/bin/env python3
"""
Batch 5: Medieval English ecclesiastical & legal figures.
Enriches 8 key figures at the intersection of church law, royal administration,
and popular resistance in medieval and early modern England.
"""

import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/230-Class-230"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()

ENRICHMENTS = {
    "robert-de-beaumont-2nd-earl-of-leicester": {
        "summary": (
            "Robert de Beaumont, 2nd Earl of Leicester (c. 1104–1168) was the most powerful "
            "magnate-minister of Henry II's early reign, serving as Chief Justiciar of England "
            "from approximately 1154 to 1168 and acting as co-regent during Henry's absences "
            "in France. The twin brother of Waleran, Count of Meulan, Robert inherited one "
            "of England's greatest magnate fortunes and was a key member of the Anglo-Norman "
            "aristocracy that bridged the Norman Conquest's legacy and the emerging Angevin "
            "state.\n\n"
            "Robert had navigated the turbulent civil war (the Anarchy) between King Stephen "
            "and the Empress Matilda with characteristic skill, initially supporting Stephen "
            "before eventually backing the Angevin cause. When Henry II came to the throne "
            "in 1154, Leicester became one of his most trusted administrators. As Chief "
            "Justiciar — the highest judicial office in England — he presided over the "
            "royal courts, managed financial administration, and represented the king's "
            "authority throughout the realm. His tenure coincided with the critical early "
            "years of Henry's legal reforms: the introduction of the possessory assizes, "
            "the expansion of royal justice, and the confrontation with Thomas Becket over "
            "clerical immunities.\n\n"
            "Leicester's administrative role in this formative period of English common law "
            "makes him an important, if often overlooked, figure. As the royal officer most "
            "directly responsible for supervising the courts and justices that implemented "
            "Henry's legal reforms, he was present at the institutional creation of the "
            "English common law. He died in 1168, the year before Becket's murder, having "
            "spent fifteen years at the center of the most consequential legal revolution "
            "in English history."
        ),
        "causes": [
            {
                "title": "Henry II's determination to expand royal justice and create a systematic common law required a trusted magnate-administrator to manage the courts",
                "type": "Person",
                "year": "1154–1168, England"
            },
            {
                "title": "The Anarchy (1135–1154) had disrupted royal justice; Henry II's restoration required a powerful Chief Justiciar to reassert royal administrative authority",
                "type": "EventWindow",
                "year": "1135–1154, England"
            },
            {
                "title": "Leicester's vast inherited estates and dual Anglo-Norman identity made him a natural bridge between royal administration and the baronial class",
                "type": "Institution",
                "year": "c. 1118–1154, England and Normandy"
            }
        ],
        "effects": [
            {
                "title": "Leicester's 14-year tenure as Chief Justiciar supervised the early implementation of Henry II's possessory assizes and the expansion of royal courts",
                "type": "Institution",
                "year": "1154–1168, England"
            },
            {
                "title": "His administrative co-regency during Henry's French campaigns maintained English royal governance while the king was absent",
                "type": "Institution",
                "year": "1154–1168, England"
            },
            {
                "title": "The common law machinery he helped oversee became the institutional foundation of English legal culture for centuries",
                "type": "Idea",
                "year": "1154–present, England"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "robert-de-beaumont-2nd-earl-of-leicester",
                "sourceName": "Robert de Beaumont, 2nd Earl of Leicester",
                "verb": "SERVED_UNDER",
                "targetSlug": "henry-ii-of-england",
                "targetName": "Henry II of England",
                "context": "Leicester served as Chief Justiciar under Henry II from 1154 to 1168, overseeing the implementation of Henry's landmark legal reforms"
            },
            {
                "sourceSlug": "robert-de-beaumont-2nd-earl-of-leicester",
                "sourceName": "Robert de Beaumont, 2nd Earl of Leicester",
                "verb": "CONTEMPORARY_OF",
                "targetSlug": "thomas-becket",
                "targetName": "Thomas Becket",
                "context": "Leicester and Becket were both leading figures in Henry II's court during the same period; Leicester's death in 1168 preceded Becket's murder in 1170"
            },
            {
                "sourceSlug": "robert-de-beaumont-2nd-earl-of-leicester",
                "sourceName": "Robert de Beaumont, 2nd Earl of Leicester",
                "verb": "IMPLEMENTED",
                "targetSlug": "possessory-assizes",
                "targetName": "Possessory Assizes",
                "context": "As Chief Justiciar, Leicester supervised the courts that implemented Henry II's possessory assizes, which created the procedural core of the English common law"
            },
            {
                "sourceSlug": "robert-de-beaumont-2nd-earl-of-leicester",
                "sourceName": "Robert de Beaumont, 2nd Earl of Leicester",
                "verb": "TWIN_OF",
                "targetSlug": "waleran-of-meulan",
                "targetName": "Waleran, Count of Meulan",
                "context": "Robert and Waleran were twin sons of Robert de Beaumont, 1st Earl of Leicester; they divided the family's English and Norman estates"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Robert de Beaumont's 14 years as Chief Justiciar of England placed him at the helm of royal judicial administration during the formative years of Henry II's common law revolution — making him a key, if often unsung, institutional architect of the English legal system.",
            "significanceCategory": "regional"
        },
        "importanceScore": 8
    },

    "simon-langham": {
        "summary": (
            "Simon Langham (c. 1315–1376) was an English Benedictine monk who rose to become "
            "Lord Chancellor of England (1363–1367), Bishop of Ely (1362–1366), Archbishop "
            "of Canterbury (1366–1368), and eventually a cardinal of the Roman Church — a "
            "career trajectory from monastery to the highest offices of church and state "
            "that was remarkable even by medieval standards. A monk of Westminster Abbey "
            "who became its abbot in 1349, he was plucked from monastic administration "
            "by Edward III, who recognized his administrative abilities.\n\n"
            "As Lord Chancellor, Langham managed the great seal and presided over the "
            "Chancery during a period of ongoing conflict with France and internal political "
            "tensions. His appointment as Archbishop of Canterbury in 1366 brought him to "
            "the highest ecclesiastical office in England. However, his elevation to the "
            "cardinalate by Pope Urban V in 1368 created an immediate conflict with Edward III, "
            "who regarded the acceptance of a papal appointment without royal assent as "
            "a violation of the Statute of Provisors (1351). The king confiscated his "
            "temporalities and Langham resigned the archbishopric, going into exile at "
            "the papal court in Avignon.\n\n"
            "Langham spent his remaining years at Avignon as a cardinal, where he accumulated "
            "considerable wealth through the lucrative papal administrative culture. At his "
            "death in 1376, he left substantial bequests — including extensive funds — to "
            "Westminster Abbey, where he had begun his career and where his heart was "
            "eventually buried. His career illustrates the persistent tension in 14th-century "
            "England between royal control over the church through statutes like Provisors "
            "and the church's claims to autonomous appointment through papal authority."
        ),
        "causes": [
            {
                "title": "Edward III's need for able administrators able to manage complex legal and diplomatic affairs drove him to elevate talented churchmen to royal service",
                "type": "Person",
                "year": "1350–1368, England"
            },
            {
                "title": "Westminster Abbey's monastic culture of financial and administrative management trained Langham in the practical governance skills that transferred to royal chancellorship",
                "type": "Institution",
                "year": "c. 1335–1362, Westminster"
            },
            {
                "title": "The conflict between royal control of church appointments (Statute of Provisors, 1351) and papal provisions created the constitutional crisis that ended Langham's English career",
                "type": "Idea",
                "year": "1351–1368, England"
            }
        ],
        "effects": [
            {
                "title": "Langham's forced resignation over his cardinalate illustrated the practical operation of the Statute of Provisors and its enforcement against a sitting Archbishop",
                "type": "EventWindow",
                "year": "1368, England"
            },
            {
                "title": "His bequests to Westminster Abbey — including funds for manuscripts and building — contributed to the abbey's medieval intellectual and architectural heritage",
                "type": "Institution",
                "year": "1376, Westminster"
            },
            {
                "title": "His career trajectory from Benedictine abbot to Lord Chancellor to Cardinal exemplified the high medieval pattern of churchmen as royal administrators",
                "type": "Idea",
                "year": "c. 1349–1376, England"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "simon-langham",
                "sourceName": "Simon Langham",
                "verb": "SERVED_UNDER",
                "targetSlug": "edward-iii-of-england",
                "targetName": "Edward III of England",
                "context": "Langham served Edward III as Lord Chancellor 1363–1367 before his appointment as Archbishop of Canterbury"
            },
            {
                "sourceSlug": "simon-langham",
                "sourceName": "Simon Langham",
                "verb": "RESIGNED_FROM",
                "targetSlug": "archbishop-of-canterbury",
                "targetName": "Archbishop of Canterbury",
                "context": "Langham resigned the archbishopric in 1368 after Edward III confiscated his temporalities over his acceptance of a papal cardinalate"
            },
            {
                "sourceSlug": "simon-langham",
                "sourceName": "Simon Langham",
                "verb": "ABBOT_OF",
                "targetSlug": "westminster-abbey",
                "targetName": "Westminster Abbey",
                "context": "Langham was Abbot of Westminster from 1349 before his elevation to royal service; he returned his heart and substantial bequests to the abbey at his death"
            },
            {
                "sourceSlug": "simon-langham",
                "sourceName": "Simon Langham",
                "verb": "ELEVATED_BY",
                "targetSlug": "pope-urban-v",
                "targetName": "Pope Urban V",
                "context": "Urban V made Langham a cardinal in 1368, triggering the conflict with Edward III that ended his English ecclesiastical career"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Simon Langham's dramatic career — from Benedictine abbot to Lord Chancellor to Archbishop to cardinal in exile — illustrates the central tensions of 14th-century English church governance: between royal control via Provisors and papal appointment authority, and between monastic culture and royal administration.",
            "significanceCategory": "regional"
        },
        "importanceScore": 8
    },

    "john-kemp": {
        "summary": (
            "John Kemp (c. 1380–1454) was one of the dominant figures of 15th-century English "
            "ecclesiastical politics, serving as Archbishop of York (1425–1452), Archbishop "
            "of Canterbury (1452–1454), Lord Chancellor twice (1426–1432 and 1450–1454), "
            "and cardinal from 1439. His career spanned five decades of royal service under "
            "Henry V and Henry VI, during which he was consistently one of the most powerful "
            "men in the kingdom — a churchman who was also a consummate royal politician.\n\n"
            "Kemp served as Henry V's chancellor during the final phase of the Hundred Years' "
            "War and the negotiations that led to the Treaty of Troyes (1420). Under Henry VI's "
            "minority and then troubled reign, Kemp became a key figure in the factional "
            "politics that eventually led to the Wars of the Roses. As Chancellor in the "
            "1420s and again in the 1450s he managed the great seal through periods of "
            "intense political instability. His elevation to the cardinalate in 1439 by "
            "Pope Eugenius IV gave him additional prestige and papal diplomatic connections "
            "that he used throughout the complex ecclesiastical politics of the period.\n\n"
            "Kemp's translation from York to Canterbury in 1452 made him the senior "
            "ecclesiastic in England at a moment when the kingdom was sliding toward civil "
            "war. He died in March 1454, just as the first of the political crises that "
            "would ignite the Wars of the Roses reached their peak, and his death "
            "contributed to the power vacuum in Henry VI's government. He remains one "
            "of the most powerful pluralist churchmen in English medieval history — "
            "simultaneously holding the highest judicial office (Lord Chancellor) and "
            "the highest ecclesiastical offices in the land."
        ),
        "causes": [
            {
                "title": "Henry V's and then Henry VI's need for an experienced and politically skilled royal chancellor drove Kemp's long tenure in royal service",
                "type": "Person",
                "year": "1413–1454, England"
            },
            {
                "title": "The Hundred Years' War created demand for ecclesiastical diplomats with both legal expertise and church authority to negotiate with France and the papacy",
                "type": "EventWindow",
                "year": "1415–1453, England and France"
            },
            {
                "title": "The factionalism of Henry VI's court created opportunities for powerful churchmen who could claim neutrality above partisan conflict",
                "type": "Institution",
                "year": "1422–1454, England"
            }
        ],
        "effects": [
            {
                "title": "Kemp's death in March 1454 contributed to the power vacuum in Henry VI's government at the onset of the Wars of the Roses",
                "type": "EventWindow",
                "year": "1454, England"
            },
            {
                "title": "His dual service as Lord Chancellor and Archbishop of Canterbury/York exemplified the medieval fusion of church administration and royal governance",
                "type": "Institution",
                "year": "1426–1454, England"
            },
            {
                "title": "His cardinalate (1439) gave England a direct channel to the Curia during the complex church politics of the Council of Basel period",
                "type": "Institution",
                "year": "1439–1454, Rome/England"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "john-kemp",
                "sourceName": "John Kemp",
                "verb": "SERVED_UNDER",
                "targetSlug": "henry-vi-of-england",
                "targetName": "Henry VI of England",
                "context": "Kemp served Henry VI for three decades as Lord Chancellor and Archbishop, becoming one of the most powerful figures in the troubled Lancastrian government"
            },
            {
                "sourceSlug": "john-kemp",
                "sourceName": "John Kemp",
                "verb": "ELEVATED_TO",
                "targetSlug": "archbishop-of-canterbury",
                "targetName": "Archbishop of Canterbury",
                "context": "Kemp was translated from York to Canterbury in 1452, becoming the senior ecclesiastic in England at the onset of the Wars of the Roses"
            },
            {
                "sourceSlug": "john-kemp",
                "sourceName": "John Kemp",
                "verb": "NEGOTIATED",
                "targetSlug": "treaty-of-troyes",
                "targetName": "Treaty of Troyes",
                "context": "Kemp was involved as chancellor in the negotiations leading to the Treaty of Troyes (1420), which made Henry V heir to the French throne"
            },
            {
                "sourceSlug": "john-kemp",
                "sourceName": "John Kemp",
                "verb": "CONCURRENT_WITH",
                "targetSlug": "wars-of-the-roses",
                "targetName": "Wars of the Roses",
                "context": "Kemp's death in 1454 preceded the opening battles of the Wars of the Roses, leaving Henry VI's government critically weakened"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "John Kemp's five-decade career simultaneously at the heads of England's church and royal judiciary — Cardinal, Archbishop, Lord Chancellor — made him one of the most powerful pluralists in English medieval history, a central figure in both the Hundred Years' War diplomacy and the drift toward the Wars of the Roses.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "john-de-stratford": {
        "summary": (
            "John de Stratford (c. 1275–1348) was Archbishop of Canterbury (1333–1348) and "
            "Lord Chancellor of England twice — a career that combined the highest ecclesiastical "
            "and royal offices, and which culminated in one of the great constitutional "
            "confrontations of medieval England: a public clash with Edward III over ministerial "
            "accountability and the rights of peers to trial in Parliament.\n\n"
            "Stratford served Edward III as a trusted diplomat in the opening years of the "
            "Hundred Years' War, playing a key role in raising revenue and negotiating "
            "alliances. But in 1340–1341, when Edward returned from a disastrous campaign "
            "in Flanders furious at his ministers' failure to deliver promised funds, "
            "he blamed Stratford and sought to try him before a royal tribunal for financial "
            "malfeasance. Stratford, claiming benefit of clergy and the right of peers to "
            "trial in Parliament rather than before royal judges, withdrew to Canterbury "
            "Cathedral and engaged Edward in a pamphlet war — publishing letters defending "
            "himself and attacking the conduct of royal government. He compared himself "
            "explicitly to Thomas Becket, suggesting Edward was another tyrant threatening "
            "ecclesiastical liberty.\n\n"
            "The dispute was resolved by compromise: Stratford was vindicated by Parliament, "
            "and the crisis contributed to the 1341 parliamentary statute requiring ministers "
            "to be answerable to Parliament — an early step in the evolution of parliamentary "
            "accountability in England. Stratford survived the crisis and remained Archbishop "
            "until his death in 1348, the year the Black Death reached England, in which "
            "he was among the earliest prominent casualties."
        ),
        "causes": [
            {
                "title": "Edward III's military campaigns in France and Flanders required enormous financial resources that ministers struggled to provide, creating conditions for the 1340 crisis",
                "type": "EventWindow",
                "year": "1337–1341, England and France"
            },
            {
                "title": "The ambiguity of whether the Lord Chancellor could be held accountable to the king or only to Parliament created constitutional uncertainty that the Stratford crisis exposed",
                "type": "Idea",
                "year": "c. 1340, England"
            },
            {
                "title": "The precedent of Becket's resistance to Henry II gave Stratford both a model for ecclesiastical defiance and a rhetorical weapon in the pamphlet war",
                "type": "Person",
                "year": "1340, England"
            }
        ],
        "effects": [
            {
                "title": "The 1341 parliamentary statute requiring ministers to be answerable to Parliament was a direct outcome of the Stratford constitutional crisis",
                "type": "EventWindow",
                "year": "1341, England"
            },
            {
                "title": "Stratford's successful defense of the peer's right to parliamentary trial contributed to the developing doctrine of parliamentary accountability of royal ministers",
                "type": "Idea",
                "year": "1341, England"
            },
            {
                "title": "Stratford died in 1348, a prominent early victim of the Black Death whose death marked the devastation that plague was beginning to inflict on England's leadership",
                "type": "EventWindow",
                "year": "1348, England"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "john-de-stratford",
                "sourceName": "John de Stratford",
                "verb": "CLASHED_WITH",
                "targetSlug": "edward-iii-of-england",
                "targetName": "Edward III of England",
                "context": "Stratford and Edward III fought a public constitutional battle in 1340–1341 over ministerial accountability and trial by peers"
            },
            {
                "sourceSlug": "john-de-stratford",
                "sourceName": "John de Stratford",
                "verb": "APPEALED_TO",
                "targetSlug": "parliament-of-england",
                "targetName": "Parliament of England",
                "context": "Stratford insisted on his right as a peer to be tried before Parliament rather than a royal tribunal, contributing to parliamentary constitutional development"
            },
            {
                "sourceSlug": "john-de-stratford",
                "sourceName": "John de Stratford",
                "verb": "INVOKED",
                "targetSlug": "thomas-becket",
                "targetName": "Thomas Becket",
                "context": "Stratford explicitly compared himself to Becket in his published letters, portraying Edward III as a king threatening ecclesiastical liberty"
            },
            {
                "sourceSlug": "john-de-stratford",
                "sourceName": "John de Stratford",
                "verb": "KILLED_BY",
                "targetSlug": "black-death",
                "targetName": "Black Death",
                "context": "Stratford died in 1348, one of the prominent early English victims of the Black Death"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "John de Stratford's constitutional confrontation with Edward III in 1340–1341 — over ministerial accountability and the peer's right to parliamentary trial — contributed to an early evolution of parliamentary accountability for royal ministers, making it a small but significant moment in the development of English constitutional governance.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "stephen-gardiner": {
        "summary": (
            "Stephen Gardiner (c. 1495–1555) was Bishop of Winchester, Lord Chancellor of "
            "England under Mary I, and one of the most intellectually formidable and "
            "politically durable figures of the English Reformation. As a young canon lawyer "
            "trained at Cambridge, he rose rapidly in royal service as a diplomat and "
            "ecclesiastical administrator. He was among the principal draftsmen of the "
            "Act of Submission of the Clergy (1532), which subordinated the English church's "
            "legislative authority to the Crown — one of the key legislative building blocks "
            "of the Henrician Reformation. Yet he spent the subsequent decades defending "
            "Catholic doctrine even as he accepted royal supremacy, and his career embodied "
            "the impossible contradictions of the English church under the Tudors.\n\n"
            "Gardiner was imprisoned in the Tower under Edward VI (1547–1553) for refusing "
            "to accept Protestant liturgical reforms — a striking reversal for a man who had "
            "helped overthrow papal authority. Released by Mary I on her accession, he became "
            "Lord Chancellor and the dominant figure of her government. He worked to restore "
            "Catholic worship, oversaw the repeal of Henrician and Edwardian ecclesiastical "
            "legislation, and managed the parliamentary approval of Mary's marriage to Philip "
            "of Spain. He initially opposed the most extreme aspects of the Marian persecution "
            "of Protestants, preferring recantation to burning, but ultimately presided over "
            "the legal machinery of persecution. He died in November 1555, having witnessed "
            "the burning of Bishops Ridley and Latimer but before the most intense phase.\n\n"
            "Gardiner's De Vera Obedientia (1535, On True Obedience) — arguing for royal "
            "supremacy over the church — was an embarrassing text for him in his later "
            "Catholic phase, and Protestant polemicists republished it in 1553 to discredit him."
        ),
        "causes": [
            {
                "title": "Henry VIII's need for canonically trained diplomatic and legal advisers to manage the break with Rome created the opening for Gardiner's rise",
                "type": "Person",
                "year": "1527–1535, England"
            },
            {
                "title": "Gardiner's genuine theological conservatism — accepting royal supremacy while rejecting Protestant doctrine — created the irresolvable contradiction of his career",
                "type": "Idea",
                "year": "c. 1535–1555, England"
            },
            {
                "title": "Mary I's restoration created the conditions for Gardiner's rehabilitation and elevation to Lord Chancellor, allowing him to reverse the Protestant reforms he had resisted",
                "type": "EventWindow",
                "year": "1553, England"
            }
        ],
        "effects": [
            {
                "title": "The Act of Submission of the Clergy (1532), which Gardiner helped draft, made the English church's legislative power subordinate to the Crown",
                "type": "EventWindow",
                "year": "1532, England"
            },
            {
                "title": "As Mary's Lord Chancellor, Gardiner managed the legislative reversal of Henrician and Edwardian reforms, briefly restoring Catholic worship in England",
                "type": "EventWindow",
                "year": "1553–1555, England"
            },
            {
                "title": "De Vera Obedientia — his argument for royal supremacy — was reprinted by Protestants to humiliate him after his conversion back to Catholic advocacy",
                "type": "Text",
                "year": "1535/1553, England"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "stephen-gardiner",
                "sourceName": "Stephen Gardiner",
                "verb": "SERVED_UNDER",
                "targetSlug": "henry-viii-of-england",
                "targetName": "Henry VIII of England",
                "context": "Gardiner served Henry VIII as diplomat, bishop, and ecclesiastical lawyer through the entire decade of the Reformation's legislative phase"
            },
            {
                "sourceSlug": "stephen-gardiner",
                "sourceName": "Stephen Gardiner",
                "verb": "SERVED_UNDER",
                "targetSlug": "mary-i-of-england",
                "targetName": "Mary I of England",
                "context": "Gardiner served Mary I as Lord Chancellor 1553–1555, managing her Catholic restoration, the Spanish marriage, and the persecution of Protestants"
            },
            {
                "sourceSlug": "stephen-gardiner",
                "sourceName": "Stephen Gardiner",
                "verb": "IMPRISONED_BY",
                "targetSlug": "edward-vi-of-england",
                "targetName": "Edward VI of England",
                "context": "Gardiner was imprisoned in the Tower 1547–1553 under Edward VI for refusing to accept Protestant liturgical reforms"
            },
            {
                "sourceSlug": "stephen-gardiner",
                "sourceName": "Stephen Gardiner",
                "verb": "AUTHORED",
                "targetSlug": "de-vera-obedientia",
                "targetName": "De Vera Obedientia",
                "context": "Gardiner's 1535 treatise arguing for royal supremacy over the church was reprinted by Protestants in 1553 to discredit his Catholic stance under Mary"
            },
            {
                "sourceSlug": "stephen-gardiner",
                "sourceName": "Stephen Gardiner",
                "verb": "PRESIDED_OVER",
                "targetSlug": "marian-persecution",
                "targetName": "Marian Persecution of Protestants",
                "context": "As Lord Chancellor, Gardiner presided over the legal machinery of the Marian persecution, though he initially preferred recantation to burning"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Stephen Gardiner's career — helping create the Henrician Reformation's legal instruments, then becoming the Catholic conservative champion of Mary's restoration — encapsulates the contradictions of the English Reformation, making him one of its most psychologically complex and historically revealing figures.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "robert-aske": {
        "summary": (
            "Robert Aske (c. 1500–1537) was an English barrister of Gray's Inn who became "
            "the principal leader and ideological voice of the Pilgrimage of Grace — the "
            "largest rebellion in Tudor history, which marshalled 30,000–40,000 people "
            "across the north of England in the autumn of 1536 in protest against Henry VIII's "
            "dissolution of the monasteries, the break with Rome, and the government of "
            "Thomas Cromwell. The rebellion was distinguished by its explicitly religious "
            "character: the rebels wore badges of the Five Wounds of Christ and framed "
            "their movement as a 'pilgrimage' for the restoration of the true faith.\n\n"
            "Aske was a lawyer from a Yorkshire gentry family who was swept up in the "
            "rebellion almost by accident, initially forced to take the rebels' oath by a "
            "group of rebels he encountered while travelling. But he quickly became the "
            "movement's most articulate spokesperson and organizational leader, coordinating "
            "the march south, articulating the grievances in sophisticated petitions, and "
            "negotiating with the Duke of Norfolk on behalf of the rebels. Henry VIII, "
            "recognizing the rebellion's dangerous scale, invited Aske to court and seemingly "
            "promised to address grievances — including a parliament in the north and a "
            "general pardon. Aske, in good faith, persuaded the rebels to disperse.\n\n"
            "Henry's promises proved fraudulent. When a smaller subsequent rising gave him "
            "the pretext he needed, Henry arrested Aske and subjected him to a trial for "
            "treason. He was executed in chains — hung in a cage — in York in July 1537, "
            "one of the most prominent victims of Henry's brutal suppression of the north. "
            "The Pilgrimage of Grace's failure cleared the way for the dissolution of "
            "the remaining larger monasteries and the final elimination of Catholic "
            "institutional resistance to the Henrician Reformation."
        ),
        "causes": [
            {
                "title": "Henry VIII's dissolution of the smaller monasteries (1536) attacked northern England's economic, spiritual, and educational infrastructure, generating mass popular opposition",
                "type": "EventWindow",
                "year": "1536, England"
            },
            {
                "title": "The government of Thomas Cromwell was perceived in the north as imposing alien and heretical changes on the faith and social fabric of a conservative region",
                "type": "Person",
                "year": "1534–1536, England"
            },
            {
                "title": "Aske's legal training gave him the capacity to organize, articulate grievances in petition form, and negotiate with royal representatives",
                "type": "Person",
                "year": "c. 1520–1536, England"
            }
        ],
        "effects": [
            {
                "title": "Henry VIII used Aske's good-faith dispersal of the rebellion to execute him and suppress the north, clearing the way for dissolution of the larger monasteries",
                "type": "EventWindow",
                "year": "1537, England"
            },
            {
                "title": "The Pilgrimage of Grace's failure was the last major Catholic uprising against the Henrician Reformation; its suppression effectively ended organized armed Catholic resistance in England",
                "type": "EventWindow",
                "year": "1537, England"
            },
            {
                "title": "Aske's sophisticated petitions articulating the rebels' religious and economic grievances are major historical documents for understanding popular opposition to the Reformation",
                "type": "Text",
                "year": "1536, England"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "robert-aske",
                "sourceName": "Robert Aske",
                "verb": "LED",
                "targetSlug": "pilgrimage-of-grace",
                "targetName": "Pilgrimage of Grace",
                "context": "Aske was the principal leader of the Pilgrimage of Grace (1536), the largest rebellion of the Tudor period"
            },
            {
                "sourceSlug": "robert-aske",
                "sourceName": "Robert Aske",
                "verb": "OPPOSED",
                "targetSlug": "thomas-cromwell",
                "targetName": "Thomas Cromwell",
                "context": "The Pilgrimage of Grace targeted Cromwell's government as the source of heretical and oppressive changes; Aske's petitions demanded Cromwell's removal"
            },
            {
                "sourceSlug": "robert-aske",
                "sourceName": "Robert Aske",
                "verb": "NEGOTIATED_WITH",
                "targetSlug": "henry-viii-of-england",
                "targetName": "Henry VIII of England",
                "context": "Aske negotiated with Henry VIII and accepted his promises of redress in good faith, persuading the rebels to disperse — only to be arrested and executed when Henry broke his word"
            },
            {
                "sourceSlug": "robert-aske",
                "sourceName": "Robert Aske",
                "verb": "OPPOSED",
                "targetSlug": "dissolution-of-the-monasteries",
                "targetName": "Dissolution of the Monasteries",
                "context": "The Pilgrimage of Grace was primarily a protest against the dissolution of the monasteries and the destruction of northern England's religious life"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Robert Aske's leadership of the Pilgrimage of Grace — the largest Tudor rebellion — and his subsequent execution after Henry VIII's betrayal of his promises represent the high-water mark of popular Catholic resistance to the English Reformation and the brutal methods the crown was willing to use to suppress it.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "ivo-of-kermartin": {
        "summary": (
            "Ivo Hélory of Kermartin (1253–1303), commonly known as Saint Yves (Yvo, Ives, or "
            "Ivo), was a Breton priest, canonist, and judge-advocate who became the patron "
            "saint of lawyers, judges, and notaries. Born into the Breton minor nobility near "
            "Tréguier in Brittany, he received an extraordinary legal and theological "
            "education: he studied canon law under the canonist Guichard of Troyes at "
            "the University of Paris, then civil law at Orléans — one of Europe's premier "
            "law schools — before returning to Brittany to practice.\n\n"
            "Ivo served as an ecclesiastical judge-advocate (Official) in the courts of "
            "Rennes and then Tréguier, where he became renowned for dispensing justice with "
            "scrupulous impartiality, defending the poor and orphans without fee, and "
            "refusing bribes — virtues remarkable enough in his era to become the stuff "
            "of legend. He was ordained a priest in 1284 and eventually became rector of "
            "Trédrez and then Louannec, continuing to practice law on behalf of the "
            "disadvantaged from his rectory. He fasted rigorously, slept on a straw mat, "
            "and distributed his income to the poor — combining the careers of judge, "
            "lawyer, priest, and ascetic in a single medieval life.\n\n"
            "Ivo died in 1303 and was canonized by Pope Clement VI in 1347, the formal "
            "recognition of a cult that had already spread across Brittany and beyond. "
            "His feast day is May 19. He is remembered in the sardonic medieval rhyme "
            "that has followed lawyers ever since: 'Advocatus et non latro / res miranda "
            "populo' — 'A lawyer and not a thief: a thing wonderful to the people.' "
            "Trégnier Cathedral, where he is buried, became a pilgrimage site. He remains "
            "the patron of the legal profession across the Catholic world."
        ),
        "causes": [
            {
                "title": "The sophisticated canon law system of the 13th-century French church created a class of trained ecclesiastical judges who managed justice for ordinary people",
                "type": "Institution",
                "year": "c. 1200–1280, France"
            },
            {
                "title": "Ivo's elite legal education at Paris and Orléans gave him command of both canon and civil law, making him one of the most skilled advocates in Brittany",
                "type": "Institution",
                "year": "c. 1267–1280, Paris and Orléans"
            },
            {
                "title": "The prevalence of corruption and bias in medieval ecclesiastical courts made Ivo's incorruptibility genuinely remarkable and the foundation of his sanctity",
                "type": "Idea",
                "year": "c. 1280–1303, Brittany"
            }
        ],
        "effects": [
            {
                "title": "Ivo's canonization (1347) established him as the official patron of lawyers across the Catholic world, a status he retains today",
                "type": "Institution",
                "year": "1347, Avignon"
            },
            {
                "title": "His feast day (May 19) is celebrated by bar associations worldwide, particularly in France, Brittany, and Catholic legal traditions",
                "type": "Institution",
                "year": "1347–present, worldwide"
            },
            {
                "title": "The sardonic rhyme 'Advocatus et non latro' — 'A lawyer and not a thief' — testifies to both his reputation and the contemporary contempt for the legal profession",
                "type": "Idea",
                "year": "14th century, Europe"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "ivo-of-kermartin",
                "sourceName": "Ivo of Kermartin",
                "verb": "STUDIED_AT",
                "targetSlug": "university-of-paris",
                "targetName": "University of Paris",
                "context": "Ivo studied canon law in Paris under the canonist Guichard of Troyes before moving to Orléans for civil law"
            },
            {
                "sourceSlug": "ivo-of-kermartin",
                "sourceName": "Ivo of Kermartin",
                "verb": "PATRON_OF",
                "targetSlug": "legal-profession",
                "targetName": "Legal Profession",
                "context": "Ivo was canonized as the patron saint of lawyers, judges, and notaries — a status he retains across Catholic bar associations worldwide"
            },
            {
                "sourceSlug": "ivo-of-kermartin",
                "sourceName": "Ivo of Kermartin",
                "verb": "CANONIZED_BY",
                "targetSlug": "pope-clement-vi",
                "targetName": "Pope Clement VI",
                "context": "Clement VI canonized Ivo in 1347, formalizing a cult that had already spread across Brittany and the French legal world"
            },
            {
                "sourceSlug": "ivo-of-kermartin",
                "sourceName": "Ivo of Kermartin",
                "verb": "CHAMPIONED",
                "targetSlug": "rights-of-the-poor",
                "targetName": "Rights of the Poor",
                "context": "Ivo defended poor and orphaned litigants without fee throughout his career as ecclesiastical judge, becoming a model of legal advocacy for the powerless"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Ivo of Kermartin's combination of elite legal training, incorruptible practice, and advocacy for the poor earned him canonization as the patron saint of lawyers — a status that has made him the symbolic ideal of legal ethics for the Catholic legal tradition across seven centuries.",
            "significanceCategory": "continental"
        },
        "importanceScore": 8
    },

    "richard-rich-1st-baron-rich": {
        "summary": (
            "Richard Rich, 1st Baron Rich (c. 1496–1567) was an English lawyer and statesman "
            "whose career combined exceptional legal ability with exceptional moral flexibility — "
            "he served every Tudor monarch from Henry VIII to Elizabeth I and thrived through "
            "the most violent reversals of fortune in English history. A barrister of the "
            "Middle Temple, he rose to become Solicitor General (1533) and then the first "
            "Chancellor of the Court of Augmentations (1536), the body created to manage "
            "revenues from the dissolution of the monasteries. He served as Lord Chancellor "
            "of England under Edward VI (1547–1551), and was created Baron Rich in 1547.\n\n"
            "Rich is most infamous for his central role in the trials of Thomas More (1535) "
            "and Bishop John Fisher (1535). He provided the decisive perjured testimony that "
            "More had denied the royal supremacy to him in a private conversation — testimony "
            "More vehemently and publicly denied, arguing that Rich was not credible: 'In good "
            "faith, Mr Rich, I am sorrier for your perjury than for my own peril.' Rich's "
            "evidence, almost certainly fabricated, sealed More's conviction. He also "
            "personally participated in racking Anne Askew (1546) — a Protestant woman "
            "accused of heresy — reportedly alongside Thomas Wriothesley; contemporaries "
            "expressed shock that men of his rank would perform the torture themselves.\n\n"
            "In a final irony, Rich founded and endowed Felsted School in Essex (1564), "
            "a grammar school that survives today, and performed conspicuous acts of "
            "local charity in his later years — as if compensating, posthumously, for "
            "a career built on calculated betrayal. He is one of history's most striking "
            "examples of the Tudor servant who survived everything by serving whoever held power."
        ),
        "causes": [
            {
                "title": "Henry VIII's destruction of the traditional legal and ecclesiastical order created opportunities for ambitious lawyers willing to provide legal cover for politically necessary convictions",
                "type": "EventWindow",
                "year": "1533–1540, England"
            },
            {
                "title": "The Court of Augmentations — Rich's principal creation — emerged from the need to manage the enormous financial windfall of the dissolution",
                "type": "Institution",
                "year": "1536, England"
            },
            {
                "title": "Rich's exceptional political survival through four Tudor reigns reflected both his legal competence and his willingness to adapt his religious position to the monarch's",
                "type": "Person",
                "year": "1533–1567, England"
            }
        ],
        "effects": [
            {
                "title": "Rich's perjured testimony at Thomas More's trial in 1535 provided the legal basis for More's conviction and execution — one of the most consequential acts of judicial perjury in English history",
                "type": "EventWindow",
                "year": "1535, London"
            },
            {
                "title": "The Court of Augmentations, which Rich established and administered, managed the largest transfer of property in English history as monastic lands were sold off",
                "type": "Institution",
                "year": "1536–1547, England"
            },
            {
                "title": "Felsted School, founded by Rich in 1564, is his lasting positive legacy — still operating and educating students more than 450 years after his death",
                "type": "Institution",
                "year": "1564–present, Essex"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "richard-rich-1st-baron-rich",
                "sourceName": "Richard Rich",
                "verb": "TESTIFIED_AGAINST",
                "targetSlug": "thomas-more",
                "targetName": "Thomas More",
                "context": "Rich's perjured testimony at More's 1535 trial claimed More had privately denied the royal supremacy, providing the decisive evidence for his conviction"
            },
            {
                "sourceSlug": "richard-rich-1st-baron-rich",
                "sourceName": "Richard Rich",
                "verb": "ESTABLISHED",
                "targetSlug": "court-of-augmentations",
                "targetName": "Court of Augmentations",
                "context": "Rich was the first Chancellor of the Court of Augmentations (1536), created to manage the enormous revenues from the dissolution of the monasteries"
            },
            {
                "sourceSlug": "richard-rich-1st-baron-rich",
                "sourceName": "Richard Rich",
                "verb": "SERVED_UNDER",
                "targetSlug": "edward-vi-of-england",
                "targetName": "Edward VI of England",
                "context": "Rich served as Lord Chancellor of England 1547–1551 under the Protestant Edward VI, having previously served the Catholic Henry VIII"
            },
            {
                "sourceSlug": "richard-rich-1st-baron-rich",
                "sourceName": "Richard Rich",
                "verb": "TORTURED",
                "targetSlug": "anne-askew",
                "targetName": "Anne Askew",
                "context": "Rich reportedly personally racked the Protestant martyr Anne Askew in 1546, shocking contemporaries by his hands-on participation in torture"
            },
            {
                "sourceSlug": "richard-rich-1st-baron-rich",
                "sourceName": "Richard Rich",
                "verb": "FOUNDED",
                "targetSlug": "felsted-school",
                "targetName": "Felsted School",
                "context": "Rich founded Felsted School in Essex in 1564, his lasting charitable legacy and still-operating grammar school"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Richard Rich's perjured testimony at Thomas More's trial provided the decisive legal mechanism for one of the most famous judicial killings in English history; his establishment of the Court of Augmentations managed the largest property transfer in English medieval history; and his survival through four Tudor reigns makes him an exemplar of the amoral Tudor servant.",
            "significanceCategory": "regional"
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
    print(f"Enriching {len(ENRICHMENTS)} entities (Batch 5: medieval English ecclesiastical)...")
    for slug, data in ENRICHMENTS.items():
        enrich_entity(slug, data)
    print("\nDone.")
