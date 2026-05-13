#!/usr/bin/env python3
"""
Batch 10: Hanafi jurist Al-Marghinani (Al-Hidaya), Archbishop-Chancellor Hubert Walter,
canonist Giovanni d'Andrea, 'Bell-the-Cat' Archibald Douglas 5th Earl of Angus,
poisoned Cardinal Christopher Bainbridge, first humanist Lovato Lovati,
Christian Latin poet Arator, pre-Islamic Arab sage Aktham ibn Sayfi.
"""

import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/230-Class-230"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()

ENRICHMENTS = {
    "burhan-al-din-al-murghinani": {
        "summary": (
            "Burhān al-Dīn al-Marghīnānī (1135–1197 CE) — full name ʿAlī ibn Abī Bakr "
            "al-Marghīnānī — was a Hanafi jurist born in Marghinan in the Ferghana Valley "
            "(modern Uzbekistan) who wrote Al-Hidāya (The Guidance), one of the most "
            "consequential and enduring texts in Islamic jurisprudence. A foundational "
            "reference work of the Hanafi legal school, Al-Hidāya has been studied, "
            "copied, commented upon, and applied in legal systems across the Islamic "
            "world from the 12th century to the present — from the Ottoman courts "
            "to Mughal India's legal administration.\n\n"
            "Al-Hidāya (written after al-Marghīnānī's earlier Al-Bidāya) is structured "
            "as a systematic survey of Hanafi law covering worship, commercial "
            "transactions, family law (marriage, divorce, inheritance), criminal law "
            "(ḥudūd and qiṣāṣ), and constitutional matters. Its particular strength is "
            "its presentation of Hanafi positions alongside systematic comparison with "
            "the other major Sunni schools (Maliki, Shafi'i, Hanbali), with al-Marghīnānī "
            "providing the reasoning for Hanafi divergences. This comparative method "
            "made it an invaluable pedagogical tool and a foundational text for the "
            "training of Islamic judges and jurists across centuries. The Mughal "
            "emperor Aurangzeb's compilation of the Fatawa-e-Alamgiri drew directly "
            "on Al-Hidāya, and the text was translated into English by Charles Hamilton "
            "in 1791 for use in British colonial administration of Muslim communities.\n\n"
            "Al-Marghīnānī represents the peak of the Central Asian Hanafi tradition "
            "in the pre-Mongol era. His death came just a generation before the Mongol "
            "invasions would destroy the Transoxiana cultural world that had produced "
            "him. Al-Hidāya survived as the definitive portable Hanafi legal reference, "
            "transcending the destruction of the Mongol conquests to remain authoritative "
            "to this day in Islamic finance and family law."
        ),
        "causes": [
            {
                "title": "The Hanafi school's dominant position in Central Asia, Persia, and later the Ottoman and Mughal empires created strong demand for a comprehensive, pedagogically accessible Hanafi legal reference",
                "type": "Institution",
                "year": "c. 1100–1197, Central Asia"
            },
            {
                "title": "Al-Marghīnānī's earlier work Al-Bidāya provided the foundation that he subsequently expanded and refined into the more comprehensive Al-Hidāya",
                "type": "Text",
                "year": "c. 1160–1180, Ferghana Valley"
            },
            {
                "title": "The florescence of Islamic legal scholarship in 12th-century Transoxiana — centered on Samarkand and Bukhara — gave al-Marghīnānī access to the accumulated Hanafi legal tradition",
                "type": "Institution",
                "year": "12th century, Central Asia"
            }
        ],
        "effects": [
            {
                "title": "Al-Hidāya became the standard Hanafi legal reference across the Ottoman Empire, Mughal India, and Muslim Central Asia, shaping judicial decisions and legal education for centuries",
                "type": "Text",
                "year": "c. 1200 – present, Islamic world"
            },
            {
                "title": "Charles Hamilton's 1791 English translation of Al-Hidāya was used by British colonial administrators to govern Muslim communities, making al-Marghīnānī's work central to colonial-era Islamic law administration",
                "type": "Text",
                "year": "1791–20th century, British India"
            },
            {
                "title": "Al-Marghīnānī's comparative methodology — presenting Hanafi positions against other Sunni schools — established a model of comparative Islamic jurisprudence that influenced subsequent legal writing",
                "type": "Idea",
                "year": "c. 1200 – present, Islamic jurisprudence"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "burhan-al-din-al-murghinani",
                "sourceName": "Burhān al-Dīn al-Marghīnānī",
                "verb": "AUTHORED",
                "targetSlug": "al-hidaya",
                "targetName": "Al-Hidāya (The Guidance)",
                "context": "Al-Hidāya is al-Marghīnānī's magnum opus — the most authoritative Hanafi legal reference of the pre-modern Islamic world"
            },
            {
                "sourceSlug": "burhan-al-din-al-murghinani",
                "sourceName": "Burhān al-Dīn al-Marghīnānī",
                "verb": "SCHOOL_OF",
                "targetSlug": "hanafi-madhab",
                "targetName": "Hanafi Madhab",
                "context": "Al-Marghīnānī was the leading Hanafi jurist of 12th-century Central Asia, whose Al-Hidāya became the school's definitive reference work"
            },
            {
                "sourceSlug": "burhan-al-din-al-murghinani",
                "sourceName": "Burhān al-Dīn al-Marghīnānī",
                "verb": "INFLUENCED",
                "targetSlug": "fatawa-e-alamgiri",
                "targetName": "Fatawa-e-Alamgiri",
                "context": "The Mughal emperor Aurangzeb's Fatawa-e-Alamgiri, the most comprehensive codification of Islamic law in pre-modern India, drew directly on Al-Hidāya"
            },
            {
                "sourceSlug": "burhan-al-din-al-murghinani",
                "sourceName": "Burhān al-Dīn al-Marghīnānī",
                "verb": "BORN_IN",
                "targetSlug": "marghinan-ferghana-valley",
                "targetName": "Marghinan, Ferghana Valley",
                "context": "Born in Marghinan (modern Uzbekistan), al-Marghīnānī was shaped by the flourishing Hanafi legal culture of 12th-century Transoxiana"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Al-Marghīnānī's Al-Hidāya is one of the most consequential texts in Islamic legal history — the definitive Hanafi legal reference across the Ottoman and Mughal empires, still authoritative in Islamic finance and family law today, and the text used by British colonial administrators to govern Muslim communities in 19th-century India.",
            "significanceCategory": "continental"
        },
        "importanceScore": 7
    },

    "hubert-walter": {
        "summary": (
            "Hubert Walter (c. 1160–1205) was Archbishop of Canterbury, Lord Chancellor "
            "of England, and Chief Justiciar — the three most powerful offices in "
            "late 12th-century England — making him the dominant figure in English "
            "government for over a decade. He is considered one of the architects "
            "of the English common law administrative system: his administrative "
            "innovations during the reign of Richard I laid essential groundwork "
            "for the institutional development of English royal government.\n\n"
            "Hubert rose through service to his uncle, Ranulf de Glanvill (the Chief "
            "Justiciar who wrote the first treatise on English common law). He served "
            "Richard I on the Third Crusade (1190–1191) and was at the Siege of Acre. "
            "When Richard returned through Europe and was captured by Duke Leopold of "
            "Austria, it was Hubert Walter — by then Bishop of Salisbury — who organized "
            "much of the enormous ransom of 150,000 silver marks that secured Richard's "
            "release. As Chief Justiciar (1193–1198) he effectively governed England "
            "during Richard's absence, simultaneously serving as Archbishop of "
            "Canterbury from 1193. He also served King John as Lord Chancellor "
            "(1199–1205), and died in office just nine years before Magna Carta.\n\n"
            "Hubert Walter's administrative legacy includes the introduction of the "
            "coroner system (1194), the establishment of systematic record-keeping "
            "in royal courts (plea rolls), and the development of the Court of Common "
            "Pleas. These innovations gave English justice institutional continuity "
            "independent of the king's person — a crucial step toward a rule-of-law "
            "culture. He was one of the central figures in the development of English "
            "administrative government: the 'angevin administration' that made England "
            "the best-governed kingdom in 12th-century Europe."
        ),
        "causes": [
            {
                "title": "Richard I's prolonged absence from England on the Third Crusade and subsequent captivity created the necessity for a competent administrator capable of governing the realm in his name",
                "type": "EventWindow",
                "year": "1190–1194, England"
            },
            {
                "title": "Hubert Walter's training under Ranulf de Glanvill gave him deep expertise in English common law administration and royal court procedure",
                "type": "Person",
                "year": "c. 1180–1190, England"
            },
            {
                "title": "The Angevin system of royal administration — itinerant justices, plea rolls, and royal writs — created the infrastructure that Hubert Walter developed into more systematic institutional form",
                "type": "Institution",
                "year": "c. 1150–1193, England"
            }
        ],
        "effects": [
            {
                "title": "Hubert Walter's introduction of the coroner system (1194) and systematic plea rolls created institutional continuity in English justice that survived individual kings",
                "type": "Institution",
                "year": "1194 – present, England"
            },
            {
                "title": "His organization of Richard I's ransom — collecting 150,000 silver marks across England — was a remarkable administrative achievement that demonstrated the capacity of the Angevin government machine",
                "type": "EventWindow",
                "year": "1193–1194, England"
            },
            {
                "title": "His development of the Court of Common Pleas and systematic record-keeping of royal courts laid essential groundwork for the common law tradition that would culminate in Magna Carta and beyond",
                "type": "Institution",
                "year": "1193–1215, England"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "hubert-walter",
                "sourceName": "Hubert Walter",
                "verb": "SERVED_UNDER",
                "targetSlug": "richard-i-of-england",
                "targetName": "Richard I of England (the Lionheart)",
                "context": "Hubert Walter served Richard I as Chief Justiciar and Archbishop, effectively governing England during the king's absence on the Third Crusade and captivity"
            },
            {
                "sourceSlug": "hubert-walter",
                "sourceName": "Hubert Walter",
                "verb": "TRAINED_UNDER",
                "targetSlug": "ranulf-de-glanvill",
                "targetName": "Ranulf de Glanvill",
                "context": "Hubert Walter learned royal administration and common law under his uncle Ranulf de Glanvill, the author of the first English common law treatise"
            },
            {
                "sourceSlug": "hubert-walter",
                "sourceName": "Hubert Walter",
                "verb": "ESTABLISHED",
                "targetSlug": "coroner-system-england",
                "targetName": "Coroner System of England",
                "context": "Hubert Walter established the coroner system in 1194 — an enduring institution of English local justice that still exists"
            },
            {
                "sourceSlug": "hubert-walter",
                "sourceName": "Hubert Walter",
                "verb": "SERVED_UNDER",
                "targetSlug": "king-john-of-england",
                "targetName": "King John of England",
                "context": "Hubert Walter served King John as Lord Chancellor (1199–1205), continuing his administrative role through the dynastic transition"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Hubert Walter's administrative innovations as Chief Justiciar and Archbishop — coroner system, systematic plea rolls, Court of Common Pleas — created the institutional infrastructure of English common law administration, making him one of the key architects of the rule-of-law tradition that culminated in Magna Carta.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "giovanni-dandrea": {
        "summary": (
            "Giovanni d'Andrea (c. 1270–1348) was an Italian canonist, professor at the "
            "University of Bologna, and the most prominent canon lawyer of the early 14th "
            "century — praised by contemporaries as 'Fons et tuba iuris canonici' "
            "(Fountain and Trumpet of Canon Law). His extensive commentaries on the "
            "major papal decretal collections — especially his Novella in Decretales "
            "(on Gregory IX's Decretales) and Novella in Sextum (on the Liber Sextus) "
            "— became standard reference works for canon law throughout the late "
            "medieval period.\n\n"
            "Giovanni d'Andrea taught at Bologna for decades, training generations "
            "of canonists from across Europe. He was deeply involved in the major "
            "ecclesiastical controversies of his era — including the disputes over "
            "papal authority, the status of the Franciscans' poverty doctrine, and "
            "the Great Schism's precursors. He participated in discussions at the "
            "papal court at Avignon. He also wrote on procedure, marriage law, and "
            "the rights of ecclesiastical offices. A famous legend holds that his "
            "daughter Novella was so learned that she occasionally lectured in his "
            "place at the university, concealed behind a curtain to avoid distracting "
            "students with her beauty — a story that has resonated across centuries "
            "as an emblem of women's exclusion from formal academic authority.\n\n"
            "Giovanni d'Andrea died in the Black Death of 1348 — one of the countless "
            "casualties among Europe's intellectual elite that the plague devastated. "
            "His works remained the standard canon law commentaries for over a century "
            "and were among the first legal texts printed in the early era of the "
            "printing press, demonstrating their continuing authority. He stands as "
            "the bridge between the classical period of medieval canonistics (Innocent "
            "IV, Hostiensis) and the later Conciliarist debates."
        ),
        "causes": [
            {
                "title": "The University of Bologna's position as the center of canon law studies in medieval Europe gave Giovanni d'Andrea access to the finest legal education and the most prestigious platform for his scholarship",
                "type": "Institution",
                "year": "c. 1290–1348, Bologna"
            },
            {
                "title": "The proliferation of papal decretal collections (Gregory IX, Boniface VIII, Clement V) created ongoing demand for authoritative commentary and systematization that Giovanni d'Andrea supplied",
                "type": "Institution",
                "year": "c. 1300–1348, Catholic Church"
            },
            {
                "title": "The major ecclesiastical controversies of the early 14th century — Franciscan poverty, Boniface VIII vs. Philip IV, Avignon papacy — drew the leading canonists into intense scholarly and political engagement",
                "type": "EventWindow",
                "year": "c. 1300–1348, Europe"
            }
        ],
        "effects": [
            {
                "title": "Giovanni d'Andrea's Novella in Decretales and Novella in Sextum became the standard canon law commentaries, used across Europe until superseded by post-Trent reform",
                "type": "Text",
                "year": "c. 1350–1563, Catholic Church"
            },
            {
                "title": "His training of generations of canonists at Bologna spread his interpretive frameworks through the European church's legal-administrative system",
                "type": "Institution",
                "year": "c. 1300–1350, European church"
            },
            {
                "title": "The legend of his daughter Novella lecturing in his place became an influential emblem in discussions of women's access to higher education",
                "type": "Idea",
                "year": "c. 1348 – present, history of education"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "giovanni-dandrea",
                "sourceName": "Giovanni d'Andrea",
                "verb": "TAUGHT_AT",
                "targetSlug": "university-of-bologna",
                "targetName": "University of Bologna",
                "context": "Giovanni d'Andrea spent his career as a professor of canon law at Bologna, the world's leading center of legal studies"
            },
            {
                "sourceSlug": "giovanni-dandrea",
                "sourceName": "Giovanni d'Andrea",
                "verb": "AUTHORED",
                "targetSlug": "novella-in-decretales",
                "targetName": "Novella in Decretales",
                "context": "Giovanni's commentary on the Decretales of Gregory IX was the standard reference commentary for this major papal collection"
            },
            {
                "sourceSlug": "giovanni-dandrea",
                "sourceName": "Giovanni d'Andrea",
                "verb": "CALLED",
                "targetSlug": "canon-law-tradition",
                "targetName": "Canon Law Tradition",
                "context": "Giovanni was called 'Fons et tuba iuris canonici' (Fountain and Trumpet of Canon Law) by contemporaries, the highest accolade in medieval legal scholarship"
            },
            {
                "sourceSlug": "giovanni-dandrea",
                "sourceName": "Giovanni d'Andrea",
                "verb": "DIED_IN",
                "targetSlug": "black-death",
                "targetName": "Black Death (1347–1351)",
                "context": "Giovanni d'Andrea was among Europe's many leading intellectuals killed by the Black Death in 1348"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Giovanni d'Andrea's commentaries on the papal decretal collections became the standard canon law reference texts of late medieval Europe — earning him the title 'Fountain and Trumpet of Canon Law' — and his death in the Black Death was a symbolic moment in the plague's devastation of the European intellectual world.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "archibald-douglas-5th-earl-of-angus": {
        "summary": (
            "Archibald Douglas, 5th Earl of Angus (c. 1449–1514) — known as 'Bell-the-Cat' "
            "— was the dominant magnate of late 15th-century Scotland whose leadership of "
            "the aristocratic conspiracy at Lauder Bridge (1482) — in which James III's "
            "despised court favorites were hanged from the bridge — became one of the most "
            "celebrated episodes of baronial resistance to royal favorites in Scottish "
            "history. His nickname derived from his reported willingness to 'bell the cat' "
            "(do the dangerous task) when others hesitated.\n\n"
            "The Lauder Bridge conspiracy of 1482 was a turning point in the reign of "
            "James III of Scotland. The king's particular favor toward low-born "
            "courtiers — especially the architect Robert Cochrane, whom James had "
            "made Earl of Mar — had provoked deep resentment among the great nobles. "
            "As a Scottish army prepared to face an English invasion led by Richard "
            "Duke of Gloucester (the future Richard III), the nobles gathered at Lauder "
            "Bridge and, led by Archibald Douglas, hanged Cochrane and five other "
            "favorites from the bridge, then seized James III himself. The king was "
            "held briefly at Edinburgh Castle before being restored. The episode "
            "demonstrated the limits of royal power when the nobility united against "
            "royal favorites.\n\n"
            "Archibald Douglas subsequently led the rebellion that brought James IV "
            "to the throne after James III was killed at the Battle of Sauchieburn "
            "(1488). He served James IV in various capacities and remained a dominant "
            "figure in Scottish politics. He opposed the policies that led to Flodden "
            "(1513) — the catastrophic Scottish defeat by the English — but his warnings "
            "were ignored. He died in 1514, just after the disaster he had feared. His "
            "grandson Archibald Douglas, 6th Earl of Angus, would marry the widowed "
            "Queen Margaret, making the Angus Douglases quasi-royal."
        ),
        "causes": [
            {
                "title": "James III's promotion of low-born court favorites — particularly Robert Cochrane as Earl of Mar — to positions of power above the established nobility created intense baronial resentment",
                "type": "Person",
                "year": "c. 1475–1482, Scotland"
            },
            {
                "title": "The Douglas family's traditional position as the great power-brokers of Scottish nobility gave Archibald Douglas both the authority and the following to lead aristocratic opposition",
                "type": "Institution",
                "year": "c. 1430–1482, Scotland"
            },
            {
                "title": "The English invasion of 1482 — when Scottish nobles were assembled at Lauder Bridge — provided the military context and physical location for the baronial coup",
                "type": "EventWindow",
                "year": "1482, Scotland"
            }
        ],
        "effects": [
            {
                "title": "The Lauder Bridge conspiracy established a precedent that Scottish nobles could effectively discipline royal favorites through collective violence with apparent impunity",
                "type": "EventWindow",
                "year": "1482, Scotland"
            },
            {
                "title": "Archibald Douglas's support for James IV's rebellion against James III contributed to the king's death at Sauchieburn (1488) and the transition to James IV's reign",
                "type": "EventWindow",
                "year": "1488, Scotland"
            },
            {
                "title": "The 'Bell-the-Cat' nickname became a proverbial expression in English and Scottish culture for the brave person willing to undertake a dangerous task others fear",
                "type": "Idea",
                "year": "c. 1500 – present, English/Scottish culture"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "archibald-douglas-5th-earl-of-angus",
                "sourceName": "Archibald Douglas, 5th Earl of Angus",
                "verb": "LED",
                "targetSlug": "lauder-bridge-conspiracy",
                "targetName": "Lauder Bridge Conspiracy (1482)",
                "context": "Archibald Douglas led the Scottish nobles who hanged James III's favorites from Lauder Bridge in 1482, earning his 'Bell-the-Cat' nickname"
            },
            {
                "sourceSlug": "archibald-douglas-5th-earl-of-angus",
                "sourceName": "Archibald Douglas, 5th Earl of Angus",
                "verb": "OPPOSED",
                "targetSlug": "james-iii-of-scotland",
                "targetName": "James III of Scotland",
                "context": "Archibald Douglas led the baronial opposition to James III's court favorites and later supported the rebellion that ended in James III's death at Sauchieburn"
            },
            {
                "sourceSlug": "archibald-douglas-5th-earl-of-angus",
                "sourceName": "Archibald Douglas, 5th Earl of Angus",
                "verb": "SUPPORTED",
                "targetSlug": "james-iv-of-scotland",
                "targetName": "James IV of Scotland",
                "context": "After Sauchieburn, Archibald Douglas served James IV and was a major figure in the early part of his reign"
            },
            {
                "sourceSlug": "archibald-douglas-5th-earl-of-angus",
                "sourceName": "Archibald Douglas, 5th Earl of Angus",
                "verb": "MEMBER_OF",
                "targetSlug": "house-of-douglas",
                "targetName": "House of Douglas",
                "context": "Archibald Douglas was the dominant figure of the House of Douglas — Scotland's greatest noble dynasty — in the late 15th century"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Archibald Douglas 'Bell-the-Cat' — the leader of the Lauder Bridge conspiracy (1482) that hanged James III's court favorites — became the defining symbol of Scottish baronial power over royal favorites, and his involvement in the transition to James IV's reign shaped Scottish politics for a generation.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "christopher-bainbridge": {
        "summary": (
            "Christopher Bainbridge (c. 1462–1514) was Archbishop of York, Cardinal "
            "of the Roman Church, and English ambassador to Rome — whose poisoning by "
            "his own secretary in 1514 became one of the most sensational political "
            "scandals of early Tudor Rome and gave rise to accusations, never conclusively "
            "proven, that Cardinal Wolsey had orchestrated his death. He was one of "
            "Henry VIII's earliest great ambassadors, combining ecclesiastical authority "
            "with skilled diplomacy at the pontifical court.\n\n"
            "Bainbridge was a canon lawyer and administrator who rose through the "
            "English church hierarchy under Henry VII, becoming Archbishop of York in "
            "1508. Henry VIII appointed him English ambassador to Rome in 1509, where "
            "he served Pope Julius II in organizing the Holy League against France — "
            "including personally leading a contingent of forces in the field on the "
            "pope's behalf during the Italian Wars, an unusual role for an English "
            "cardinal. Pope Julius II created him cardinal in 1511, making him the "
            "most senior English churchman at the Roman court. He was a vigorous and "
            "effective diplomatist who built close personal relations with Julius II.\n\n"
            "In July 1514, Bainbridge died after being poisoned — his secretary "
            "Richard de la Rue confessed to the poisoning before himself dying in "
            "prison. The confessions implicated Cardinal Silvestro de' Gigli (another "
            "English representative at Rome) and, through him, accusations were "
            "directed at Cardinal Wolsey — Bainbridge's rival for influence over "
            "Henry VIII's ecclesiastical appointments. The case was never formally "
            "resolved. Bainbridge's death removed one of the potential rivals to "
            "Wolsey's rising dominance of English church-state affairs."
        ),
        "causes": [
            {
                "title": "Henry VIII's policy of projecting English diplomatic influence in Rome through a senior cardinal-ambassador created Bainbridge's position and power",
                "type": "Institution",
                "year": "1509–1514, Rome"
            },
            {
                "title": "The intense rivalry among English ecclesiastical representatives at Rome — particularly between Bainbridge and Silvestro de' Gigli — created the factional tensions from which his poisoning apparently arose",
                "type": "Person",
                "year": "1509–1514, Rome"
            },
            {
                "title": "The Italian Wars and Pope Julius II's aggressive military-diplomatic policy gave Bainbridge an unusually active role — including leading military forces — for a cardinal-ambassador",
                "type": "EventWindow",
                "year": "1510–1514, Italy"
            }
        ],
        "effects": [
            {
                "title": "Bainbridge's poisoning became a major diplomatic and ecclesiastical scandal, with the circumstances giving rise to accusations against Cardinal Wolsey that were never definitively resolved",
                "type": "EventWindow",
                "year": "1514, Rome"
            },
            {
                "title": "His death removed one of Wolsey's potential rivals for dominance of English ecclesiastical affairs, potentially accelerating Wolsey's rise to the highest position in the English church",
                "type": "Person",
                "year": "1514–1518, England"
            },
            {
                "title": "The case established a precedent for the dangerous intersection of Italian political intrigue and English ecclesiastical diplomacy that would recur in the Henrician Reformation",
                "type": "Idea",
                "year": "1514–1534, England"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "christopher-bainbridge",
                "sourceName": "Christopher Bainbridge",
                "verb": "SERVED_UNDER",
                "targetSlug": "henry-viii-of-england",
                "targetName": "Henry VIII of England",
                "context": "Bainbridge served as Henry VIII's ambassador to Rome and represented English interests at the papal court"
            },
            {
                "sourceSlug": "christopher-bainbridge",
                "sourceName": "Christopher Bainbridge",
                "verb": "ALLIED_WITH",
                "targetSlug": "pope-julius-ii",
                "targetName": "Pope Julius II",
                "context": "Bainbridge worked closely with Julius II, including participating in military operations on the pope's behalf during the Italian Wars"
            },
            {
                "sourceSlug": "christopher-bainbridge",
                "sourceName": "Christopher Bainbridge",
                "verb": "POISONED_BY",
                "targetSlug": "richard-de-la-rue",
                "targetName": "Richard de la Rue (secretary)",
                "context": "Bainbridge was poisoned by his own secretary Richard de la Rue in 1514, leading to accusations against Cardinal Silvestro de' Gigli and, by extension, Wolsey"
            },
            {
                "sourceSlug": "christopher-bainbridge",
                "sourceName": "Christopher Bainbridge",
                "verb": "RIVAL_OF",
                "targetSlug": "thomas-wolsey",
                "targetName": "Thomas Wolsey",
                "context": "Bainbridge was one of the potential rivals to Wolsey's rising dominance of English church affairs; the unproven accusations that Wolsey orchestrated his poisoning reflect this rivalry"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Christopher Bainbridge's poisoning in Rome in 1514 — with unproven accusations pointing toward Cardinal Wolsey — was one of the most sensational early Tudor political scandals, and his death by removing a potential rival to Wolsey may have accelerated the concentration of ecclesiastical power that set the stage for the English Reformation.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "lovato-lovati": {
        "summary": (
            "Lovato Lovati (1241–1309) was a Paduan notary, judge, and Latin poet who is "
            "regarded by many historians of Renaissance culture as the first Italian "
            "humanist — the scholar who pioneered the authentic recovery of classical "
            "Latin literature in a way that directly prefigured the humanist movement "
            "of the 14th and 15th centuries. Unlike the medieval scholars who read "
            "ancient Latin authors primarily for Christian allegory or rhetorical "
            "examples, Lovati studied them with historical and literary empathy — "
            "seeking to understand ancient Rome on its own terms.\n\n"
            "Lovati was a professional notary and judge at Padua — part of the "
            "educated urban professional class that was distinctive of 13th-century "
            "northern Italian communes. He assembled a remarkable library of classical "
            "Latin texts, made particular study of classical meter and prosody, and "
            "wrote Latin poetry in authentic classical meters — including Senecan "
            "tragic verse — that represented a sharp break from the rhythmic verse "
            "typical of medieval Latin poetry. His most celebrated scholarly act was "
            "the identification in 1283 of bones in a Paduan tomb as those of Antenor "
            "— the Trojan hero who, according to legend, founded Padua — an act of "
            "historical archaeology that mobilized ancient literary sources to "
            "authenticate a local civic myth.\n\n"
            "Lovati encouraged his student circle — including Albertino Mussato (who "
            "would become the first modern writer of Latin tragedy and the first "
            "person to receive a laurel crown for literature since antiquity) — in "
            "the study of classical texts. He corresponded with scholars across "
            "northern Italy about manuscript discoveries and philological questions. "
            "This network of scholarly exchange, centered on Padua, constituted the "
            "first self-conscious community of humanist learning and laid the ground "
            "from which Petrarch — who was born the year Lovati died — would build "
            "the full humanist movement."
        ),
        "causes": [
            {
                "title": "The prosperity and civic culture of 13th-century Padua — a wealthy commune with a university and an educated notarial class — created the social context for Lovati's unusual scholarly pursuits",
                "type": "Institution",
                "year": "c. 1260–1309, Padua"
            },
            {
                "title": "The University of Padua, founded in 1222, concentrated scholars and manuscripts in a city that became northern Italy's intellectual center — giving Lovati access to rare classical texts",
                "type": "Institution",
                "year": "c. 1260–1309, Padua"
            },
            {
                "title": "Lovati's professional position as a notary and judge gave him the legal-administrative training in precise reading and argument that he applied to classical texts",
                "type": "Institution",
                "year": "c. 1260–1309, Padua"
            }
        ],
        "effects": [
            {
                "title": "Lovati's encouragement of his student Albertino Mussato — who wrote the first Renaissance Latin tragedy (Ecerinis, 1315) and received the first modern laurel crown — directly influenced the early humanist movement",
                "type": "Person",
                "year": "c. 1290–1315, Padua"
            },
            {
                "title": "Lovati's pioneering use of classical literary sources for historical archaeology — identifying Antenor's 'tomb' in 1283 — established a humanist method that linked textual scholarship to physical remains",
                "type": "Idea",
                "year": "1283, Padua"
            },
            {
                "title": "The Paduan scholarly circle that Lovati anchored constituted the first self-conscious community of pre-humanist learning and provided the immediate context from which Petrarch would emerge",
                "type": "Movement",
                "year": "c. 1290–1340, northern Italy"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "lovato-lovati",
                "sourceName": "Lovato Lovati",
                "verb": "INFLUENCED",
                "targetSlug": "albertino-mussato",
                "targetName": "Albertino Mussato",
                "context": "Lovati mentored Mussato, who wrote the first Renaissance Latin tragedy and received the first modern laurel crown, directly inheriting Lovati's classical revival"
            },
            {
                "sourceSlug": "lovato-lovati",
                "sourceName": "Lovato Lovati",
                "verb": "FOUNDED",
                "targetSlug": "paduan-pre-humanism",
                "targetName": "Paduan Pre-Humanism",
                "context": "Lovati anchored the Paduan scholarly circle that constituted the first self-conscious community of humanist learning, directly anticipating Petrarch"
            },
            {
                "sourceSlug": "lovato-lovati",
                "sourceName": "Lovato Lovati",
                "verb": "IDENTIFIED",
                "targetSlug": "tomb-of-antenor-padua",
                "targetName": "Tomb of Antenor, Padua",
                "context": "In 1283, Lovati identified bones in a Paduan tomb as those of Antenor — the Trojan legendary founder of Padua — using classical literary sources to authenticate this civic myth"
            },
            {
                "sourceSlug": "lovato-lovati",
                "sourceName": "Lovato Lovati",
                "verb": "CONTEMPORARY_OF",
                "targetSlug": "petrarch",
                "targetName": "Petrarch",
                "context": "Petrarch was born in 1304, the year of Lovati's death — the symbolic hinge between Lovati's pre-humanism and the full humanist movement Petrarch would create"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Lovato Lovati — the first scholar to engage with classical Latin literature with genuinely humanist empathy and historical sensibility — is regarded as the first Italian humanist, whose Paduan scholarly circle provided the immediate intellectual context from which Petrarch and the Renaissance humanist movement would emerge.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "arator": {
        "summary": (
            "Arator (c. 490–c. 550 CE) was a Ligurian-born Latin poet and ecclesiastic "
            "who wrote Historia Apostolica — a verse paraphrase of the Acts of the "
            "Apostles in over 2,000 hexameter lines — which was one of the most "
            "celebrated and widely read Latin Christian poems of the early Middle Ages. "
            "His work represents the continuation of the late antique tradition of "
            "Christian biblical epic poetry that had flourished in the works of Prudentius, "
            "Sedulius, and Juvencus.\n\n"
            "Arator had an unusual dual career: he initially pursued a legal and "
            "administrative career in Ostrogothic Italy, studying under the bishop "
            "Ennodius of Pavia and rising to serve as a royal official. But after "
            "the Byzantine reconquest of Italy under Justinian's general Belisarius "
            "(535–540 CE), he entered the church and became sub-deacon of the church "
            "of Rome under Pope Vigilius. He dedicated his Historia Apostolica to "
            "Pope Vigilius in 544 CE. In a remarkable cultural event, the poem was "
            "read aloud — with repeated encores demanded by the audience — in the "
            "church of San Pietro in Vincoli in Rome over several days, with the "
            "pope and Roman clergy in attendance. This public reading was recorded "
            "in a dedicatory letter that accompanied the poem.\n\n"
            "Historia Apostolica was widely copied and studied throughout the early "
            "medieval period, particularly in the British Isles and Frankish Gaul "
            "where it served as a school text alongside Virgil. Arator's method of "
            "allegorical interpretation — finding spiritual meanings beneath the "
            "narrative surface — influenced the allegorical reading of scripture "
            "that would become central to medieval biblical exegesis. His poem "
            "transmitted the classical Latin hexameter tradition into the early "
            "medieval church and his work was among the texts that kept Virgilian "
            "metrics alive through the turbulent 6th and 7th centuries."
        ),
        "causes": [
            {
                "title": "The late antique tradition of Christian biblical epic poetry — Juvencus, Sedulius, Prudentius — provided Arator with his model and gave his work an established generic context",
                "type": "Text",
                "year": "c. 310–490 CE, Roman world"
            },
            {
                "title": "Arator's transition from royal official to church official during the Byzantine reconquest of Italy created the change of life context that drove his literary activity",
                "type": "EventWindow",
                "year": "535–544 CE, Italy"
            },
            {
                "title": "The church of Rome's continued support for Latin literary culture in the 6th century — even amid the collapse of the western empire — provided Arator with an audience and papal patronage",
                "type": "Institution",
                "year": "c. 540–550 CE, Rome"
            }
        ],
        "effects": [
            {
                "title": "Historia Apostolica was widely copied and used as a school text throughout early medieval Europe, transmitting classical Latin hexameter tradition into the Carolingian and post-Carolingian periods",
                "type": "Text",
                "year": "c. 550–900 CE, Western Europe"
            },
            {
                "title": "Arator's allegorical method of scriptural interpretation influenced the medieval exegetical tradition that read biblical narrative on multiple spiritual levels",
                "type": "Idea",
                "year": "c. 550–1200 CE, Western Christianity"
            },
            {
                "title": "The public reading of Historia Apostolica in San Pietro in Vincoli (544 CE) was one of the last great late antique literary events in Rome — a vivid testimony to the survival of literary culture amid political crisis",
                "type": "EventWindow",
                "year": "544 CE, Rome"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "arator",
                "sourceName": "Arator",
                "verb": "AUTHORED",
                "targetSlug": "historia-apostolica",
                "targetName": "Historia Apostolica",
                "context": "Arator's hexameter verse paraphrase of the Acts of the Apostles was one of the most celebrated Latin Christian poems of the early Middle Ages"
            },
            {
                "sourceSlug": "arator",
                "sourceName": "Arator",
                "verb": "DEDICATED_TO",
                "targetSlug": "pope-vigilius",
                "targetName": "Pope Vigilius",
                "context": "Arator dedicated Historia Apostolica to Pope Vigilius in 544 CE; the poem was read aloud to the pope and Roman clergy in San Pietro in Vincoli"
            },
            {
                "sourceSlug": "arator",
                "sourceName": "Arator",
                "verb": "MENTORED_BY",
                "targetSlug": "ennodius-of-pavia",
                "targetName": "Ennodius of Pavia",
                "context": "Arator was raised and educated under Bishop Ennodius of Pavia, who recognized his literary talent and oversaw his early education"
            },
            {
                "sourceSlug": "arator",
                "sourceName": "Arator",
                "verb": "INFLUENCED_BY",
                "targetSlug": "virgil",
                "targetName": "Virgil",
                "context": "Arator's hexameter verse technique drew on the Virgilian tradition, helping to transmit classical Latin metrics into the early medieval literary tradition"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Arator's Historia Apostolica — celebrated with a legendary public reading in Rome in 544 CE — was one of the most widely copied Latin Christian poems of early medieval Europe, transmitting classical hexameter tradition and allegorical scriptural method into the Carolingian world and preserving Latin literary culture through the turbulent 6th century.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "aktham-ibn-sayfi": {
        "summary": (
            "Aktham ibn Ṣayfī al-Tamīmī (fl. c. 570–630 CE) was a celebrated pre-Islamic "
            "Arab wise man (ḥakīm) and judge (ḥakam) from the Tamīm tribe of central "
            "Arabia — one of the most revered figures in the Arabic wisdom tradition. "
            "A patriarch and arbiter renowned for his shrewd counsel and his gift for "
            "pithy maxims (ḥikam), he was consulted by tribal leaders across Arabia "
            "as an authoritative judge in disputes of honor, blood money, and "
            "inheritance. His sayings circulated widely in the early Islamic "
            "literary tradition as examples of pre-Islamic Arab wisdom.\n\n"
            "Aktham's fame rested on his role as a ḥakam — an arbitration figure "
            "whose personal authority and recognized impartiality made his verdicts "
            "binding across tribal lines. In the pre-Islamic Arabian system, where "
            "no unified legal authority existed, such figures were essential for "
            "managing the conflicts of a segmentary tribal society. Aktham was "
            "proverbially associated with profound counsel about kinship, governance, "
            "and the human condition. One of his most famous sayings attributed to "
            "him: 'The best of conditions is that of a man with ample means who yet "
            "is thankful.' He was also reportedly addressed by the Prophet Muhammad, "
            "who sent him a letter or message inviting him to Islam near the end of "
            "Aktham's life — a tradition that placed him at the symbolic hinge between "
            "the pre-Islamic and Islamic periods.\n\n"
            "Aktham reportedly lived to an extraordinary age — Arab tradition credits "
            "him with nearly 300 years, a hyperbole that reflects his iconic status "
            "as the sage embodiment of the pre-Islamic wisdom tradition. He appears "
            "frequently in early Arabic adab (belles-lettres) literature as the "
            "paradigmatic ḥakīm whose maxims distilled the moral code of the "
            "Jāhiliyya (the pre-Islamic age of 'ignorance') — serving as a foil "
            "against which Islamic moral teaching could define itself."
        ),
        "causes": [
            {
                "title": "The tribal structure of pre-Islamic Arabia — in which no unified legal authority existed — created the role of the ḥakam (arbitration judge) whose personal authority bridged tribal conflicts",
                "type": "Institution",
                "year": "c. 570–630 CE, Arabia"
            },
            {
                "title": "The Tamīm tribe's central position in the networks of Arabian tribal politics gave Aktham a platform from which his wisdom could be heard and sought by leaders across Arabia",
                "type": "Institution",
                "year": "c. 570–630 CE, Arabia"
            },
            {
                "title": "The Arabic wisdom (ḥikma) tradition — in which celebrated maxims were attributed to tribal sages and preserved as moral guides — created the literary framework within which Aktham's sayings were transmitted",
                "type": "Idea",
                "year": "c. 500–700 CE, Arabia"
            }
        ],
        "effects": [
            {
                "title": "Aktham ibn Ṣayfī's maxims and judgments were preserved in early Islamic adab literature as paradigmatic examples of pre-Islamic Arab wisdom, shaping how Islamic writers understood the moral tradition they were inheriting and surpassing",
                "type": "Text",
                "year": "c. 640–900 CE, Islamic literature"
            },
            {
                "title": "His role as a ḥakam (tribal arbitration judge) became a model in early Islamic historical writing for the pre-Islamic system of justice that Islamic law was seen to replace and perfect",
                "type": "Idea",
                "year": "c. 640–900 CE, Islamic jurisprudence"
            },
            {
                "title": "The tradition that Aktham corresponded with the Prophet Muhammad placed him at the boundary between Jāhiliyya and Islam — a symbolic position that made his career important for early Islamic definitions of historical continuity and moral progress",
                "type": "Idea",
                "year": "c. 630 CE – Islamic historiography"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "aktham-ibn-sayfi",
                "sourceName": "Aktham ibn Ṣayfī",
                "verb": "MEMBER_OF",
                "targetSlug": "tamim-tribe",
                "targetName": "Tamīm Tribe",
                "context": "Aktham was the leading sage and judge of the Tamīm tribe — one of the great central Arabian tribes — whose prestige gave him authority across tribal Arabia"
            },
            {
                "sourceSlug": "aktham-ibn-sayfi",
                "sourceName": "Aktham ibn Ṣayfī",
                "verb": "PRESERVED_IN",
                "targetSlug": "early-arabic-adab-tradition",
                "targetName": "Early Arabic Adab (Belles-Lettres) Tradition",
                "context": "Aktham's maxims and sayings were preserved in early Islamic adab literature as paradigmatic examples of pre-Islamic Arab wisdom"
            },
            {
                "sourceSlug": "aktham-ibn-sayfi",
                "sourceName": "Aktham ibn Ṣayfī",
                "verb": "ADDRESSED_BY",
                "targetSlug": "muhammad",
                "targetName": "The Prophet Muhammad",
                "context": "Islamic tradition records that Muhammad sent Aktham a message near the end of his life, placing Aktham at the symbolic boundary between the pre-Islamic and Islamic periods"
            },
            {
                "sourceSlug": "aktham-ibn-sayfi",
                "sourceName": "Aktham ibn Ṣayfī",
                "verb": "EXEMPLIFIED",
                "targetSlug": "pre-islamic-wisdom-tradition",
                "targetName": "Pre-Islamic Wisdom (Ḥikma) Tradition",
                "context": "Aktham ibn Ṣayfī was the paradigmatic figure of the Arabian wisdom tradition — the ḥakīm whose maxims epitomized the moral culture of the Jāhiliyya"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Aktham ibn Ṣayfī — the most celebrated pre-Islamic Arab wise man and tribal judge — became through his preserved maxims the paradigmatic figure of the Jāhiliyya wisdom tradition in early Islamic literature, standing at the symbolic hinge between pre-Islamic Arabia and Islam itself.",
            "significanceCategory": "regional"
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
    print(f"Enriching {len(ENRICHMENTS)} entities (Batch 10)...")
    for slug, data in ENRICHMENTS.items():
        enrich_entity(slug, data)
    print("\nDone.")
