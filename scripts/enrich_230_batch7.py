#!/usr/bin/env python3
"""
Batch 7: Diverse legal/administrative figures across medieval Europe, Byzantium,
Song China, and the Norse world.
"""

import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/230-Class-230"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()

ENRICHMENTS = {
    "osmund": {
        "summary": (
            "Saint Osmund (c. 1038–1099) was a Norman nobleman who became Bishop of "
            "Salisbury (1078–1099) under William the Conqueror and William Rufus — one of "
            "the most able ecclesiastical administrators in post-Conquest England. Born in "
            "Normandy, he accompanied the Conqueror to England in 1066 and rose rapidly "
            "in royal service as a chancellor, playing a key role in compiling Domesday "
            "Book (1086). His appointment to Salisbury gave him one of England's largest "
            "and most recently reorganized sees, and he threw himself into the task of "
            "building a cathedral church and organizing its chapter with unusual system "
            "and care.\n\n"
            "Osmund's most enduring contribution to English religious history was his "
            "organization and systematization of the Sarum Use — the liturgical rite of "
            "Salisbury Cathedral. Precisely what Osmund created and what later tradition "
            "attributed to him remains debated by liturgical historians, but the Sarum "
            "Use, whether largely his creation or subsequently attributed to his authority, "
            "became the dominant liturgical rite of pre-Reformation England, used in most "
            "English dioceses and exported to Wales, Ireland, and Portugal. When Henry VIII "
            "sought to impose liturgical uniformity in 1547–1549, it was the Sarum Use that "
            "the first Book of Common Prayer replaced. Osmund also built the cathedral "
            "library at Salisbury, copied manuscripts himself, and established the "
            "constitution and statutes of the cathedral chapter — creating an institutional "
            "model copied by later English cathedrals.\n\n"
            "Osmund was canonized in 1457 by Pope Calixtus III after a long and difficult "
            "process stretching back to 1228 — the delays reflecting political rather than "
            "sanctity-related objections. His feast is December 4. 'He spared himself "
            "neither in writing, dictating, or binding books,' wrote William of Malmesbury, "
            "capturing the unusual personal scholarly engagement of this bishop-administrator."
        ),
        "causes": [
            {
                "title": "William the Conqueror's need for trusted Norman administrators in the reorganized English church created the opening for Osmund's episcopal appointment",
                "type": "Person",
                "year": "1066–1078, England"
            },
            {
                "title": "The newly reorganized diocese of Salisbury required a bishop capable of building its institutional foundations — chapter, statutes, library, and liturgy — from scratch",
                "type": "Institution",
                "year": "1078, Salisbury"
            },
            {
                "title": "The fragmented liturgical diversity of English dioceses created a practical need for standardization; Osmund's Sarum Use filled this need so effectively it spread beyond Salisbury",
                "type": "Institution",
                "year": "c. 1078–1099, England"
            }
        ],
        "effects": [
            {
                "title": "The Sarum Use became the dominant liturgical rite of pre-Reformation England, used in most English dioceses and exported to Wales, Ireland, and Portugal",
                "type": "Institution",
                "year": "c. 1080–1547, England"
            },
            {
                "title": "The first Book of Common Prayer (1549) replaced the Sarum Use with a unified national English liturgy, making Osmund's rite the template the Reformation superseded",
                "type": "Text",
                "year": "1549, England"
            },
            {
                "title": "Osmund's cathedral chapter constitution became a model for later English cathedral chapters, shaping the governance of English cathedrals for centuries",
                "type": "Institution",
                "year": "c. 1078–present, England"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "osmund",
                "sourceName": "Osmund",
                "verb": "SERVED_UNDER",
                "targetSlug": "william-the-conqueror",
                "targetName": "William the Conqueror",
                "context": "Osmund served William I as chancellor and helped compile Domesday Book before his appointment as Bishop of Salisbury"
            },
            {
                "sourceSlug": "osmund",
                "sourceName": "Osmund",
                "verb": "ESTABLISHED",
                "targetSlug": "sarum-use",
                "targetName": "Sarum Use",
                "context": "Osmund organized the liturgical rite of Salisbury Cathedral — the Sarum Use — which became the dominant liturgical rite of pre-Reformation England"
            },
            {
                "sourceSlug": "osmund",
                "sourceName": "Osmund",
                "verb": "CONTRIBUTED_TO",
                "targetSlug": "domesday-book",
                "targetName": "Domesday Book",
                "context": "As William's chancellor, Osmund is credited with playing a key role in the compilation of Domesday Book (1086)"
            },
            {
                "sourceSlug": "osmund",
                "sourceName": "Osmund",
                "verb": "CANONIZED_BY",
                "targetSlug": "pope-calixtus-iii",
                "targetName": "Pope Calixtus III",
                "context": "After a canonization process lasting over two centuries (1228–1457), Osmund was formally canonized by Calixtus III in 1457"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Osmund's organization of the Sarum Use — the dominant liturgical rite of pre-Reformation England — and his model cathedral chapter constitution gave him an institutional influence on English religious life that lasted nearly five centuries, until the Book of Common Prayer replaced his liturgy at the Reformation.",
            "significanceCategory": "regional"
        },
        "importanceScore": 8
    },

    "john-alcock": {
        "summary": (
            "John Alcock (c. 1430–1500) was Bishop of Worcester, Bishop of Ely, and Lord "
            "Chancellor of England — a career spanning the turbulent decades of the Wars "
            "of the Roses and the early Tudors that combined royal judicial service with "
            "a deep commitment to education and ecclesiastical reform. Born in Beverley, "
            "Yorkshire, he was educated at Cambridge and rose through royal service under "
            "Edward IV, becoming Bishop of Rochester (1472) and then Worcester (1476) "
            "before his translation to Ely (1486) under Henry VII.\n\n"
            "Alcock served as Lord Chancellor twice — briefly under Edward IV and more "
            "substantially under the young Henry VII — and as a royal tutor to the "
            "short-lived Prince Edward (later briefly Edward V). His most enduring legacy "
            "is the foundation of Jesus College, Cambridge, in 1496 — achieved by suppressing "
            "the decayed nunnery of St Radegund's and converting its buildings to educational "
            "use. This was one of the earliest English suppressions of a failed religious house "
            "in favor of educational purposes, prefiguring the pattern of the later dissolution. "
            "Alcock was a prolific preacher whose printed sermons — including 'The Hill of "
            "Perfection' and 'Spousage of a Virgin to Christ' — were among the earliest "
            "English printed religious texts.\n\n"
            "A notable Renaissance figure in the English church, Alcock combined Gothic "
            "architectural patronage (he rebuilt sections of Ely Cathedral) with humanist "
            "intellectual interests. He was one of Henry VII's trusted episcopal administrators "
            "in the period of early Tudor consolidation, and his foundation of Jesus College "
            "gave Cambridge one of its most distinctive institutions — the college taking "
            "a rooster (cock) as its emblem in a pun on its founder's name."
        ),
        "causes": [
            {
                "title": "Henry VII's need for trusted episcopal administrators to stabilize royal government after the Wars of the Roses drove Alcock's repeated appointment to royal service",
                "type": "Person",
                "year": "1485–1500, England"
            },
            {
                "title": "The decay and failure of St Radegund's nunnery created the opportunity and legal justification for Alcock to suppress it and redirect its endowment to education",
                "type": "Institution",
                "year": "c. 1490–1496, Cambridge"
            },
            {
                "title": "The humanist reform tradition that valued education as a vehicle for religious and civic renewal gave Alcock the intellectual framework for converting a failed nunnery into a Cambridge college",
                "type": "Idea",
                "year": "c. 1480–1496, England"
            }
        ],
        "effects": [
            {
                "title": "Jesus College Cambridge (founded 1496) became one of Cambridge's most distinctive institutions and a major center of learning — surviving to the present day",
                "type": "Institution",
                "year": "1496–present, Cambridge"
            },
            {
                "title": "Alcock's suppression of a decayed nunnery to fund a college prefigured the pattern of the dissolution of the monasteries under Henry VIII by four decades",
                "type": "Idea",
                "year": "1496–1536, England"
            },
            {
                "title": "Alcock's printed sermons were among the earliest English printed devotional texts, contributing to the emerging print culture of religious vernacular literature",
                "type": "Text",
                "year": "c. 1486–1500, England"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "john-alcock",
                "sourceName": "John Alcock",
                "verb": "FOUNDED",
                "targetSlug": "jesus-college-cambridge",
                "targetName": "Jesus College, Cambridge",
                "context": "Alcock founded Jesus College in 1496 by suppressing the decayed nunnery of St Radegund's and converting its buildings and endowment to education"
            },
            {
                "sourceSlug": "john-alcock",
                "sourceName": "John Alcock",
                "verb": "SERVED_UNDER",
                "targetSlug": "henry-vii-of-england",
                "targetName": "Henry VII of England",
                "context": "Alcock served Henry VII as Lord Chancellor and trusted episcopal administrator during the early Tudor consolidation"
            },
            {
                "sourceSlug": "john-alcock",
                "sourceName": "John Alcock",
                "verb": "TUTORED",
                "targetSlug": "edward-v-of-england",
                "targetName": "Edward V",
                "context": "Alcock tutored the young Prince Edward who briefly became Edward V before his disappearance in the Tower in 1483"
            },
            {
                "sourceSlug": "john-alcock",
                "sourceName": "John Alcock",
                "verb": "BISHOP_OF",
                "targetSlug": "bishopric-of-ely",
                "targetName": "Bishopric of Ely",
                "context": "Alcock served as Bishop of Ely from 1486 until his death in 1500, undertaking major building works at Ely Cathedral"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "John Alcock's founding of Jesus College Cambridge — by suppressing a failed nunnery and redirecting its endowment to education — prefigured the dissolution of the monasteries by four decades and created one of Cambridge's most distinctive colleges, while his role as Lord Chancellor and royal administrator placed him at the center of early Tudor governance.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "leopold-iii-of-bebenburg": {
        "summary": (
            "Lupold of Bebenburg (c. 1297–1363), also called Leopold III or Lupold of Bebenburg, "
            "was a German canonist, Bishop of Bamberg (1353–1363), and the most important "
            "political-legal theorist of the Holy Roman Empire in the mid-14th century. "
            "Born to a Franconian noble family, he studied canon and civil law at Bologna, "
            "returning to a career in ecclesiastical and imperial administration that "
            "eventually culminated in his episcopal appointment. His legal scholarship, "
            "however, was his most enduring contribution.\n\n"
            "Lupold's central work, De Iuribus Regni et Imperii Romani (On the Rights of "
            "the Kingdom and the Roman Empire, c. 1340), written at a moment of intense "
            "conflict between Louis IV (the Bavarian) and Pope John XXII over imperial "
            "authority, argued that the German king derived his authority not from papal "
            "coronation but from election by the German princes alone. He developed a "
            "systematic argument that the German king was fully emperor from the moment "
            "of his election, without requiring papal confirmation — a position that "
            "directly challenged the papal theory of imperial authority that had structured "
            "German constitutional thinking for a century. This argument, grounded in "
            "historical evidence about earlier emperors and canon law principles, was "
            "taken up and incorporated into the Golden Bull of 1356 — the constitutional "
            "charter of the Holy Roman Empire.\n\n"
            "Lupold also wrote Tractatulus de zelo et studio principum Alemannie (c. 1340) "
            "defending German princes' right to act without papal license. His work "
            "synthesized canon law methodology with a political argument for imperial "
            "independence that became foundational for German constitutional thought, "
            "influencing Marsilius of Padua's reception in Germany and eventually "
            "feeding into the Reformation's arguments about secular authority."
        ),
        "causes": [
            {
                "title": "The conflict between Holy Roman Emperor Louis IV (the Bavarian) and Pope John XXII over imperial authority created the political crisis that drove Lupold's systematic constitutional argument",
                "type": "EventWindow",
                "year": "c. 1323–1340, Holy Roman Empire"
            },
            {
                "title": "Lupold's training in canon law at Bologna gave him the methodological tools to make a legally sophisticated case for imperial independence from papal authority",
                "type": "Institution",
                "year": "c. 1315–1325, Bologna"
            },
            {
                "title": "The German princes' desire to assert the sufficiency of their election against papal claims to confirm the emperor provided Lupold with both political backing and a constitutional framework",
                "type": "Institution",
                "year": "c. 1338–1340, Holy Roman Empire"
            }
        ],
        "effects": [
            {
                "title": "The arguments of De Iuribus Regni et Imperii were incorporated into the Golden Bull of 1356, the constitutional charter of the Holy Roman Empire, which established election-based imperial legitimacy",
                "type": "Text",
                "year": "1356, Holy Roman Empire"
            },
            {
                "title": "Lupold's argument that the emperor required no papal confirmation influenced the Reformation's case for secular authority independent of Rome",
                "type": "Idea",
                "year": "1340–1520, Germany"
            },
            {
                "title": "German constitutional thought about imperial authority drew on Lupold's historical arguments throughout the late medieval and early modern period",
                "type": "Idea",
                "year": "1340–1555, Holy Roman Empire"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "leopold-iii-of-bebenburg",
                "sourceName": "Lupold of Bebenburg",
                "verb": "AUTHORED",
                "targetSlug": "de-iuribus-regni-et-imperii",
                "targetName": "De Iuribus Regni et Imperii Romani",
                "context": "Lupold's c. 1340 treatise argued that the German king derived imperial authority from election alone, without requiring papal coronation"
            },
            {
                "sourceSlug": "leopold-iii-of-bebenburg",
                "sourceName": "Lupold of Bebenburg",
                "verb": "INFLUENCED",
                "targetSlug": "golden-bull-1356",
                "targetName": "Golden Bull of 1356",
                "context": "Lupold's arguments about election-based imperial legitimacy were incorporated into the Golden Bull, the constitutional charter of the Holy Roman Empire"
            },
            {
                "sourceSlug": "leopold-iii-of-bebenburg",
                "sourceName": "Lupold of Bebenburg",
                "verb": "SUPPORTED",
                "targetSlug": "louis-iv-holy-roman-emperor",
                "targetName": "Louis IV, Holy Roman Emperor",
                "context": "Lupold's De Iuribus was written in support of Louis IV's constitutional position against Pope John XXII's papal claims"
            },
            {
                "sourceSlug": "leopold-iii-of-bebenburg",
                "sourceName": "Lupold of Bebenburg",
                "verb": "BISHOP_OF",
                "targetSlug": "bishopric-of-bamberg",
                "targetName": "Bishopric of Bamberg",
                "context": "Lupold served as Bishop of Bamberg from 1353 until his death in 1363"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Lupold of Bebenburg's De Iuribus Regni et Imperii — arguing that imperial authority derived from election alone, requiring no papal confirmation — provided the intellectual foundation for the Golden Bull of 1356 and shaped German constitutional thought about secular authority from the mid-14th century through the Reformation.",
            "significanceCategory": "continental"
        },
        "importanceScore": 8
    },

    "haukr-erlendsson": {
        "summary": (
            "Haukr Erlendsson (c. 1265–1334) was an Icelandic nobleman, lawman (lögmaðr) "
            "of Iceland and Norway, and one of the most significant intellectual figures "
            "of medieval Norse culture. As a senior royal official — he served as lawman "
            "in Norway and Iceland at different periods under King Hákon V of Norway — "
            "he was deeply embedded in the legal and administrative structures of the "
            "Norwegian-Icelandic realm. But his lasting importance rests on his role as "
            "the compiler of the Hauksbók (Haukr's Book), a major medieval Icelandic "
            "manuscript anthology that he assembled and partly wrote himself.\n\n"
            "The Hauksbók (now partially preserved in three fragments in Copenhagen) is "
            "a remarkable miscellany that illustrates the breadth of Haukr's intellectual "
            "interests: it contains Landnámabók (the settlement book of Iceland), Eiríks "
            "saga rauða (Eirik the Red's Saga, including the first account of the Norse "
            "discovery of North America), Völuspá (the great Old Norse cosmological poem), "
            "scientific and geographical texts, a version of the Arthurian tradition, "
            "genealogical records of Haukr's own family, and mathematical texts. "
            "Haukr personally wrote portions of the manuscript in his own hand, and "
            "commissioned scribes to copy others.\n\n"
            "The Hauksbók's inclusion of Eiríks saga rauða makes it one of the two "
            "primary manuscript witnesses to the Norse discovery of North America — giving "
            "Haukr an unexpected significance in the historiography of world exploration. "
            "His career as both a practicing legal administrator and a scholarly manuscript "
            "compiler represents the combination of active governance and intellectual "
            "culture that characterized the Icelandic literary tradition at its peak, "
            "before the Black Death and later political disruptions ended the great "
            "age of saga compilation."
        ),
        "causes": [
            {
                "title": "The Icelandic tradition of lawmen as both judicial administrators and keepers of historical and legal tradition gave Haukr both the authority and the motivation to compile the Hauksbók",
                "type": "Institution",
                "year": "c. 1270–1334, Iceland"
            },
            {
                "title": "The late 13th-century florescence of Icelandic manuscript production — the era of large codex compilations — provided the context and scribal resources for Haukr's anthology",
                "type": "Institution",
                "year": "c. 1270–1340, Iceland and Norway"
            },
            {
                "title": "Haukr's personal genealogical interest in documenting his descent from Eirik the Red's expedition created his motivation for including Eiríks saga rauða in the compilation",
                "type": "Person",
                "year": "c. 1300–1310, Iceland"
            }
        ],
        "effects": [
            {
                "title": "The Hauksbók preserves Eiríks saga rauða — one of the two primary manuscript witnesses to the Norse discovery of North America — giving Haukr a key role in the historiography of exploration",
                "type": "Text",
                "year": "c. 1300–1334, Iceland"
            },
            {
                "title": "The Hauksbók's version of Landnámabók is one of the primary sources for the settlement history of Iceland, preserving genealogical and geographical data available nowhere else",
                "type": "Text",
                "year": "c. 1300–1334, Iceland"
            },
            {
                "title": "The Hauksbók's inclusion of scientific, cosmological, and Arthurian texts documents the breadth of Norse intellectual culture in the early 14th century",
                "type": "Text",
                "year": "c. 1300–1334, Iceland"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "haukr-erlendsson",
                "sourceName": "Haukr Erlendsson",
                "verb": "COMPILED",
                "targetSlug": "hauksbók",
                "targetName": "Hauksbók",
                "context": "Haukr compiled and partly wrote the Hauksbók, the major medieval Icelandic manuscript anthology preserving Eiríks saga rauða, Landnámabók, and Völuspá"
            },
            {
                "sourceSlug": "haukr-erlendsson",
                "sourceName": "Haukr Erlendsson",
                "verb": "SERVED_UNDER",
                "targetSlug": "haakon-v-of-norway",
                "targetName": "Hákon V of Norway",
                "context": "Haukr served as lawman of Iceland and Norway under Hákon V, combining royal legal administration with his scholarly pursuits"
            },
            {
                "sourceSlug": "haukr-erlendsson",
                "sourceName": "Haukr Erlendsson",
                "verb": "PRESERVED",
                "targetSlug": "eiriks-saga-rauda",
                "targetName": "Eiríks saga rauða",
                "context": "The Hauksbók preserves one of the two primary manuscripts of Eiríks saga rauða, the account of the Norse discovery of North America"
            },
            {
                "sourceSlug": "haukr-erlendsson",
                "sourceName": "Haukr Erlendsson",
                "verb": "SERVED_AS",
                "targetSlug": "lawman-of-iceland",
                "targetName": "Lawman of Iceland",
                "context": "Haukr served as lögmaðr (lawman) of Iceland, one of the highest judicial offices in the Norse legal system"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Haukr Erlendsson's Hauksbók — which he partly wrote in his own hand — is one of the great medieval Icelandic codex compilations, preserving key texts for the Norse discovery of North America, Icelandic settlement history, and Old Norse cosmological poetry, making him a crucial figure in the transmission of Norse literary and historical culture.",
            "significanceCategory": "regional"
        },
        "importanceScore": 8
    },

    "johann-of-schwarzenberg": {
        "summary": (
            "Johann von Schwarzenberg (1463–1528) was a Franconian imperial knight, "
            "chamberlain to the Prince-Bishop of Bamberg, and the most important legal "
            "reformer in late medieval German criminal law. His Bambergische "
            "Halsgerichtsordnung (Bamberg Criminal Court Ordinance, 1507) — known simply "
            "as the Bambergensis — was the first systematic codification of criminal "
            "procedure and criminal law in the German-speaking world, and it served as "
            "the direct model for the Carolina (the Constitutio Criminalis Carolina, "
            "1532), the imperial criminal code that governed criminal justice across the "
            "Holy Roman Empire for the next two centuries.\n\n"
            "Schwarzenberg's practical legal reform was driven by his horror at the "
            "arbitrary cruelty of contemporary German criminal justice: the widespread "
            "use of torture to extract confessions, the lack of procedural safeguards, "
            "and the inconsistency of punishments. The Bambergensis introduced systematic "
            "rules for the use of evidence and torture (limiting torture to cases where "
            "there was already strong circumstantial evidence), required judges to give "
            "reasons for their decisions, and established a hierarchy of offenses and "
            "punishments grounded in Roman law principles. These were radical reforms for "
            "their time.\n\n"
            "A Lutheran sympathizer from early in the Reformation, Schwarzenberg also "
            "wrote vernacular religious satires attacking clerical abuses, and he "
            "corresponded with Ulrich von Hutten. His combination of legal reform and "
            "Protestant sympathy links him to the broad humanist and reforming culture of "
            "early 16th-century Germany. His Bambergensis circulated widely across German "
            "territories before being adopted, with modifications, as the basis of the "
            "Carolina — ensuring that his procedural reforms became the foundation of "
            "imperial criminal justice. He died before the Carolina's promulgation but "
            "is rightly regarded as its intellectual progenitor."
        ),
        "causes": [
            {
                "title": "The arbitrary and cruel criminal justice practices of late medieval German courts — arbitrary torture, inconsistent punishments, no procedural rules — created the demand for systematic reform",
                "type": "Institution",
                "year": "c. 1480–1507, Holy Roman Empire"
            },
            {
                "title": "The humanist revival of Roman law provided Schwarzenberg with both the methodological framework and the substantive criminal law principles for the Bambergensis",
                "type": "Idea",
                "year": "c. 1490–1507, Germany"
            },
            {
                "title": "Schwarzenberg's position as chamberlain to the Prince-Bishop of Bamberg gave him the authority and access to impose his legal reforms on one of Germany's most important ecclesiastical territories",
                "type": "Institution",
                "year": "c. 1500–1507, Bamberg"
            }
        ],
        "effects": [
            {
                "title": "The Bambergensis (1507) was the first systematic codification of criminal procedure in the German-speaking world, introducing evidence-based limits on torture and consistent punishments",
                "type": "Text",
                "year": "1507, Bamberg"
            },
            {
                "title": "The Carolina (1532) — the imperial criminal code that governed the Holy Roman Empire for two centuries — was modeled directly on Schwarzenberg's Bambergensis",
                "type": "Text",
                "year": "1532, Holy Roman Empire"
            },
            {
                "title": "The procedural safeguards Schwarzenberg introduced — requiring evidence before torture, giving reasons for decisions — represented the first step toward due process in German criminal law",
                "type": "Idea",
                "year": "1507–1532, Holy Roman Empire"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "johann-of-schwarzenberg",
                "sourceName": "Johann von Schwarzenberg",
                "verb": "AUTHORED",
                "targetSlug": "bambergische-halsgerichtsordnung",
                "targetName": "Bambergische Halsgerichtsordnung (Bambergensis)",
                "context": "Schwarzenberg's 1507 Bambergensis was the first systematic codification of German criminal procedure and law"
            },
            {
                "sourceSlug": "johann-of-schwarzenberg",
                "sourceName": "Johann von Schwarzenberg",
                "verb": "INFLUENCED",
                "targetSlug": "constitutio-criminalis-carolina",
                "targetName": "Constitutio Criminalis Carolina (1532)",
                "context": "The Carolina — the imperial criminal code of the Holy Roman Empire — was modeled directly on Schwarzenberg's Bambergensis"
            },
            {
                "sourceSlug": "johann-of-schwarzenberg",
                "sourceName": "Johann von Schwarzenberg",
                "verb": "CORRESPONDED_WITH",
                "targetSlug": "ulrich-von-hutten",
                "targetName": "Ulrich von Hutten",
                "context": "Schwarzenberg corresponded with the humanist polemicist Ulrich von Hutten, sharing his reforming and Protestant-sympathizing outlook"
            },
            {
                "sourceSlug": "johann-of-schwarzenberg",
                "sourceName": "Johann von Schwarzenberg",
                "verb": "INFLUENCED",
                "targetSlug": "german-criminal-law",
                "targetName": "German Criminal Law",
                "context": "Schwarzenberg's procedural reforms — evidence requirements before torture, consistent punishments — shaped German criminal law through the Carolina for two centuries"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Johann von Schwarzenberg's Bambergensis (1507) — the first systematic codification of German criminal procedure — served as the direct model for the Carolina (1532), the imperial criminal code that governed criminal justice across the Holy Roman Empire for two centuries, making Schwarzenberg the intellectual progenitor of early modern German criminal law.",
            "significanceCategory": "continental"
        },
        "importanceScore": 8
    },

    "kou-zhun": {
        "summary": (
            "Kou Zhun (寇準, 961–1023 CE), courtesy name Pingzhong, was a Song Dynasty "
            "chancellor and statesman who played a decisive role in one of East Asia's "
            "most consequential diplomatic negotiations: the Chanyuan Treaty (澶淵之盟, "
            "1005 CE) between the Song Empire and the Liao (Khitan) Empire, which "
            "established a durable peace between China's two great powers for over a century.\n\n"
            "Kou Zhun rose rapidly in the early Song bureaucracy, known for his blunt "
            "speech, political courage, and refusal to flatter. He served under Emperors "
            "Taizong and Zhenzong, and in 1004, when the Liao launched a massive invasion "
            "southward that reached the Yellow River at Chanzhou (澶州), Kou famously "
            "pressured the irresolute Emperor Zhenzong to personally lead the army to "
            "the front — arguing that only the emperor's presence could inspire the troops "
            "and avert defeat. The imperial appearance did indeed stabilize Song resistance. "
            "Kou then negotiated the Chanyuan Treaty: the Song would pay annual tribute "
            "to Liao (100,000 taels of silver and 200,000 bolts of silk), while Liao "
            "recognized Song as an equal ('brother state') rather than subordinate.\n\n"
            "The Chanyuan Treaty was immediately controversial: critics argued Kou had "
            "conceded too much tribute. But historians have consistently vindicated him — "
            "the treaty ended a ruinous war and inaugurated 120 years of peace between "
            "Song and Liao. Kou was later demoted by court factionalists who resented "
            "his influence, and died in exile in Leizhou. He is remembered as one of the "
            "great statesman-patriots of the Song, vindicated by history's judgment of "
            "the treaty he negotiated."
        ),
        "causes": [
            {
                "title": "The Liao invasion of 1004 — the largest Khitan military incursion into Song territory — created the military crisis that required Kou Zhun's decisive diplomatic and political response",
                "type": "EventWindow",
                "year": "1004, Song Empire"
            },
            {
                "title": "Emperor Zhenzong's irresolution and inclination to flee created the need for Kou Zhun's famous insistence that the emperor lead the army personally to Chanzhou",
                "type": "Person",
                "year": "1004, Chanzhou"
            },
            {
                "title": "Both Song and Liao were exhausted by decades of intermittent warfare; the military stalemate at Chanzhou created the conditions for a negotiated peace",
                "type": "EventWindow",
                "year": "979–1004, East Asia"
            }
        ],
        "effects": [
            {
                "title": "The Chanyuan Treaty (1005) established 120 years of peace between Song and Liao, allowing both empires to consolidate and prosper without frontier warfare",
                "type": "EventWindow",
                "year": "1005–1125, East Asia"
            },
            {
                "title": "The treaty's annual tribute structure — silver and silk — set the model for subsequent Song diplomatic relations with frontier powers, including the later Jurchen Jin",
                "type": "Institution",
                "year": "1005–1127, East Asia"
            },
            {
                "title": "Kou's precedent of pressuring an emperor to appear at the front became a celebrated example of a minister's duty to give the monarch unwelcome but necessary counsel",
                "type": "Idea",
                "year": "1005 CE – present, China"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "kou-zhun",
                "sourceName": "Kou Zhun",
                "verb": "NEGOTIATED",
                "targetSlug": "chanyuan-treaty",
                "targetName": "Chanyuan Treaty (1005)",
                "context": "Kou Zhun negotiated the Chanyuan Treaty — Song's 120-year peace with the Liao — at Chanzhou in 1005"
            },
            {
                "sourceSlug": "kou-zhun",
                "sourceName": "Kou Zhun",
                "verb": "SERVED_UNDER",
                "targetSlug": "emperor-zhenzong-of-song",
                "targetName": "Emperor Zhenzong of Song",
                "context": "Kou served Emperor Zhenzong, famously pressuring him to appear personally at the Chanzhou front during the Liao invasion"
            },
            {
                "sourceSlug": "kou-zhun",
                "sourceName": "Kou Zhun",
                "verb": "OPPOSED_BY",
                "targetSlug": "song-court-factionalists",
                "targetName": "Song Court Factionalists",
                "context": "Kou was eventually demoted and exiled to Leizhou by court factionalists who resented his political influence and credit for the treaty"
            },
            {
                "sourceSlug": "kou-zhun",
                "sourceName": "Kou Zhun",
                "verb": "ESTABLISHED_PEACE_WITH",
                "targetSlug": "liao-dynasty",
                "targetName": "Liao Dynasty",
                "context": "The Chanyuan Treaty Kou negotiated established Song-Liao relations on a basis of equal-state tributes that sustained peace for 120 years"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Kou Zhun's negotiation of the Chanyuan Treaty (1005) — establishing 120 years of peace between Song China and the Liao Empire — was one of East Asia's most consequential diplomatic achievements, demonstrating how tribute-based peace could be more strategically valuable than endless frontier war.",
            "significanceCategory": "continental"
        },
        "importanceScore": 8
    },

    "christopher-of-mytilene": {
        "summary": (
            "Christopher of Mytilene (c. 1000–1050 CE) was a Byzantine judge (krites), "
            "court official, and poet who produced some of the most witty and socially "
            "observant verse in the middle Byzantine period. A native of the island of "
            "Lesbos (Mytilene), he pursued a career in Byzantine imperial administration "
            "and the judiciary while simultaneously cultivating his literary reputation "
            "through the composition of epigrammatic verse in the classical tradition. "
            "He held various administrative offices in the provinces and the capital "
            "during the reigns of emperors Basil II and his successors.\n\n"
            "Christopher's surviving poetry — some 145 epigrams and occasional poems "
            "preserved in manuscripts — offers a remarkably vivid window onto Byzantine "
            "court culture, bureaucratic life, and social relations in the 11th century. "
            "His poems satirize corrupt judges and dishonest administrators (including, "
            "with self-deprecating wit, himself), celebrate literary friendships, mock "
            "pretentious learned men, describe the bureaucratic frustrations of provincial "
            "administration, and commemorate the deaths of colleagues. They are written "
            "in the learned classical Greek style characteristic of Byzantine literary "
            "culture, but animated by genuine observation of the world around him.\n\n"
            "His poem on the calendar — describing the twelve months — has been widely "
            "quoted as evidence of Byzantine agricultural and social life. His satirical "
            "verses on judicial corruption are among the most direct evidence of Byzantine "
            "legal culture's internal self-criticism. Christopher is increasingly "
            "recognized as one of the most interesting minor literary figures of the "
            "middle Byzantine period, whose work provides irreplaceable testimony about "
            "the texture of educated Byzantine life."
        ),
        "causes": [
            {
                "title": "The Byzantine tradition of literate judge-officials who combined legal and administrative careers with classical literary cultivation created the context for Christopher's dual career",
                "type": "Institution",
                "year": "c. 950–1050, Byzantium"
            },
            {
                "title": "The 11th-century florescence of Byzantine learned culture under the Macedonian dynasty gave Christopher both the education and the audience for his epigrammatic poetry",
                "type": "Institution",
                "year": "c. 1000–1050, Constantinople"
            },
            {
                "title": "The real experience of Byzantine provincial administration — its corruption, bureaucratic frustrations, and social dynamics — gave Christopher his most vivid literary material",
                "type": "Institution",
                "year": "c. 1020–1050, Byzantium"
            }
        ],
        "effects": [
            {
                "title": "Christopher's 145 surviving epigrams provide irreplaceable evidence of Byzantine court culture, bureaucratic life, and social observation in the 11th century",
                "type": "Text",
                "year": "c. 1025–1050, Byzantium"
            },
            {
                "title": "His satirical verses on judicial corruption document the internal Byzantine critique of legal administration, providing evidence unavailable in official sources",
                "type": "Idea",
                "year": "c. 1025–1050, Byzantium"
            },
            {
                "title": "His calendar poem is one of the most-cited descriptions of Byzantine agricultural and social life across the twelve months",
                "type": "Text",
                "year": "c. 1025–1050, Byzantium"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "christopher-of-mytilene",
                "sourceName": "Christopher of Mytilene",
                "verb": "SERVED_UNDER",
                "targetSlug": "basil-ii-of-byzantium",
                "targetName": "Basil II of Byzantium",
                "context": "Christopher began his administrative career during the reign of Basil II (the Bulgar-Slayer) and continued under his successors"
            },
            {
                "sourceSlug": "christopher-of-mytilene",
                "sourceName": "Christopher of Mytilene",
                "verb": "CONTEMPORARY_OF",
                "targetSlug": "michael-psellos",
                "targetName": "Michael Psellos",
                "context": "Christopher was a slightly older contemporary of Michael Psellos and part of the same learned Byzantine cultural milieu"
            },
            {
                "sourceSlug": "christopher-of-mytilene",
                "sourceName": "Christopher of Mytilene",
                "verb": "WORKED_IN",
                "targetSlug": "byzantine-judiciary",
                "targetName": "Byzantine Judiciary",
                "context": "Christopher served as a krites (judge) in Byzantine provincial administration, the professional context that informed his satirical poetry"
            },
            {
                "sourceSlug": "christopher-of-mytilene",
                "sourceName": "Christopher of Mytilene",
                "verb": "COMPOSED",
                "targetSlug": "byzantine-epigrams",
                "targetName": "Byzantine Epigrams",
                "context": "Christopher's 145 surviving epigrams are among the most vivid documents of Byzantine court and legal culture in the 11th century"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Christopher of Mytilene's surviving epigrams — witty, satirical observations on Byzantine legal corruption, court life, and social dynamics — provide irreplaceable testimony about the texture of educated Byzantine judicial culture in the 11th century, making him one of the most interesting minor literary-legal figures of the middle Byzantine period.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "falco-of-benevento": {
        "summary": (
            "Falco of Benevento (c. 1070/1080–c. 1144) was a Norman-Italian chronicler "
            "and notary of the city of Benevento whose Chronicon Beneventanum (Chronicle "
            "of Benevento) is the primary narrative source for the political and religious "
            "history of Benevento from 1102 to 1139 — a period of intense conflict "
            "between the papacy, the Norman rulers of southern Italy, and the city's own "
            "population. A professional notary in the city's legal administration, Falco "
            "wrote with an unusual directness and emotional engagement, his chronicle "
            "documenting the events of his own lifetime from the perspective of a citizen "
            "who experienced them directly.\n\n"
            "Benevento in this period was a papal enclave within the Norman kingdom of "
            "southern Italy — a territory directly subject to the Pope, not to any secular "
            "ruler. This gave Falco a distinctive vantage point: his chronicle records "
            "in vivid detail the struggles between the papacy and Norman rulers including "
            "Roger II of Sicily, the political violence and factional conflicts within "
            "the city itself, the impact of crusading movement on southern Italian "
            "society, and the lived experience of sieges, famines, and popular unrest. "
            "He wrote in a relatively plain Latin that occasionally lapses into the "
            "vernacular — suggesting a readership of educated townsmen rather than monastic "
            "scholars.\n\n"
            "Falco's chronicle is particularly valuable for its account of the Norman "
            "consolidation of southern Italy and Sicily under Roger II — a political "
            "transformation that Falco observed from the perspective of a city caught "
            "between papal and Norman power. His eyewitness accounts of sieges, diplomatic "
            "negotiations, popular assemblies, and civic violence make the Chronicon "
            "Beneventanum one of the most important urban chronicles of 12th-century Italy."
        ),
        "causes": [
            {
                "title": "Benevento's unique status as a papal enclave within the Norman kingdom placed Falco at the intersection of papal, Norman, and civic politics that generated his chronicle's rich material",
                "type": "Institution",
                "year": "c. 1080–1140, Benevento"
            },
            {
                "title": "The Norman conquest and consolidation of southern Italy created the political upheaval that motivated a civic notary to document the events of his own lifetime",
                "type": "EventWindow",
                "year": "c. 1095–1139, southern Italy"
            },
            {
                "title": "Falco's professional training as a notary gave him the literacy, legal precision, and documentary instincts that made him an unusually detailed chronicler",
                "type": "Institution",
                "year": "c. 1090–1140, Benevento"
            }
        ],
        "effects": [
            {
                "title": "The Chronicon Beneventanum is the primary narrative source for Benevento's history from 1102 to 1139, preserving eyewitness accounts of sieges, diplomacy, and civic conflict",
                "type": "Text",
                "year": "c. 1102–1139, Benevento"
            },
            {
                "title": "Falco's chronicle provides the most detailed civic perspective on the Norman consolidation of southern Italy under Roger II available in any contemporary source",
                "type": "Text",
                "year": "c. 1127–1139, southern Italy"
            },
            {
                "title": "The chronicle's relatively plain, vernacular-inflected Latin documents the linguistic transition in southern Italy from pure Latin to the emerging Italian vernacular",
                "type": "Text",
                "year": "c. 1102–1139, southern Italy"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "falco-of-benevento",
                "sourceName": "Falco of Benevento",
                "verb": "AUTHORED",
                "targetSlug": "chronicon-beneventanum",
                "targetName": "Chronicon Beneventanum",
                "context": "Falco's chronicle covering 1102–1139 is the primary source for Benevento's history during the Norman consolidation of southern Italy"
            },
            {
                "sourceSlug": "falco-of-benevento",
                "sourceName": "Falco of Benevento",
                "verb": "RECORDED",
                "targetSlug": "roger-ii-of-sicily",
                "targetName": "Roger II of Sicily",
                "context": "Falco's chronicle documents Roger II's Norman consolidation of southern Italy from Benevento's perspective as a papal enclave resisting Norman domination"
            },
            {
                "sourceSlug": "falco-of-benevento",
                "sourceName": "Falco of Benevento",
                "verb": "WITNESSED",
                "targetSlug": "papal-norman-conflicts",
                "targetName": "Papal-Norman Conflicts in Southern Italy",
                "context": "As a citizen and notary of papal Benevento, Falco was an eyewitness to the conflicts between the papacy and Norman rulers that he chronicled"
            },
            {
                "sourceSlug": "falco-of-benevento",
                "sourceName": "Falco of Benevento",
                "verb": "WORKED_IN",
                "targetSlug": "benevento-notariate",
                "targetName": "Benevento Notariate",
                "context": "Falco's professional career as a civic notary in Benevento gave him the legal literacy and documentary training that informed his chronicling"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Falco of Benevento's Chronicon Beneventanum — the eyewitness chronicle of a civic notary at the intersection of papal and Norman power in 12th-century southern Italy — is the primary narrative source for the Norman consolidation of southern Italy and the most detailed urban chronicle of its period in the region.",
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
    print(f"Enriching {len(ENRICHMENTS)} entities (Batch 7: diverse medieval legal/admin)...")
    for slug, data in ENRICHMENTS.items():
        enrich_entity(slug, data)
    print("\nDone.")
