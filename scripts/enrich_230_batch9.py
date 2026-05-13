#!/usr/bin/env python3
"""
Batch 9: Roman emperor Macrinus (first non-senator emperor/jurist), Roman flamen Martialis
Lucius Cornelius Lentulus Niger, Old Kingdom Egyptian vizier Minkhaf I, Wars of the Roses
Edmund Earl of Rutland, Teutonic Order chronicler Johann von Posilge, Tudor treasurer
John Dynham 1st Baron Dynham, Scottish lord James Hamilton 1st Lord Hamilton, Song Dynasty
incorruptible judge Bao Zheng.
"""

import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/230-Class-230"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()

ENRICHMENTS = {
    "macrinus": {
        "summary": (
            "Marcus Opellius Macrinus (c. 165–218 CE) was Roman Emperor from April 217 "
            "to June 218 CE — notable as the first emperor who had not been a senator "
            "before his accession, and the first from Mauretania (modern Algeria), "
            "an African province outside the traditional Roman elite. A self-made man "
            "who rose through legal expertise and equestrian service, Macrinus had "
            "served as the Praetorian prefect — the commander of the imperial guard "
            "and effectively the emperor's deputy — under the erratic emperor Caracalla.\n\n"
            "Macrinus came to power by organizing Caracalla's assassination in 217 CE, "
            "having received warning that Caracalla intended to have him killed. He was "
            "proclaimed emperor by the Praetorians in the field in Mesopotamia — "
            "a precedent-setting military coup. His reign was marked by difficult "
            "military challenges: he had to negotiate a peace with the Parthians "
            "under unfavorable conditions, paying a large indemnity. He also attempted "
            "to restore fiscal discipline by reducing the extravagant pay increases "
            "Caracalla had granted the legions — which made him deeply unpopular with "
            "the troops. In 218 CE, the Syrian legions proclaimed the young Elagabalus "
            "(presented as Caracalla's illegitimate son) as emperor; Macrinus was "
            "defeated at the Battle of Antioch, fled, was captured in Asia Minor, and "
            "was executed.\n\n"
            "Before his political rise, Macrinus had served as a jurist in Rome's "
            "imperial administration — one of the last emperors whose background was "
            "legal rather than purely military. His brief reign presaged the military "
            "emperors of the crisis of the third century and demonstrated both the "
            "possibilities and the fragility of power for men who rose outside the "
            "traditional senatorial aristocracy."
        ),
        "causes": [
            {
                "title": "Macrinus's fear of Caracalla's rumored intention to have him killed drove him to organize the emperor's assassination, the immediate cause of his accession",
                "type": "Person",
                "year": "217 CE, Mesopotamia"
            },
            {
                "title": "His prior legal expertise and equestrian administrative career made Macrinus an unusual figure — a jurist-turned-military commander — at the head of the Praetorian Guard",
                "type": "Institution",
                "year": "c. 200–217 CE, Rome"
            },
            {
                "title": "The Roman practice of military proclamation of emperors — which had grown more common in the 3rd century — enabled Macrinus to be raised to the purple without senatorial legitimation",
                "type": "Institution",
                "year": "217 CE, Roman Empire"
            }
        ],
        "effects": [
            {
                "title": "Macrinus was the first emperor from the equestrian order and from Mauretania — his reign opened the door to the eventual dominance of military-provincial emperors in the Crisis of the Third Century",
                "type": "Idea",
                "year": "217–235 CE, Roman Empire"
            },
            {
                "title": "His defeat at the Battle of Antioch by the forces of Elagabalus established a precedent for provincial legions overthrowing emperors — a pattern that would dominate 3rd-century Rome",
                "type": "EventWindow",
                "year": "218 CE, Syria"
            },
            {
                "title": "His attempt to restore fiscal discipline by reducing army pay — which led to his overthrow — illustrated the impossible bind of emperors dependent on the legions' loyalty while needing financial restraint",
                "type": "Idea",
                "year": "217–218 CE, Roman Empire"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "macrinus",
                "sourceName": "Macrinus",
                "verb": "ASSASSINATED",
                "targetSlug": "caracalla",
                "targetName": "Caracalla",
                "context": "Macrinus organized the assassination of Emperor Caracalla in 217 CE to prevent his own execution"
            },
            {
                "sourceSlug": "macrinus",
                "sourceName": "Macrinus",
                "verb": "DEFEATED_BY",
                "targetSlug": "elagabalus",
                "targetName": "Elagabalus",
                "context": "Macrinus was overthrown by the Syrian legions supporting Elagabalus at the Battle of Antioch in 218 CE"
            },
            {
                "sourceSlug": "macrinus",
                "sourceName": "Macrinus",
                "verb": "PRECEDED",
                "targetSlug": "severan-dynasty",
                "targetName": "Severan Dynasty",
                "context": "Macrinus briefly interrupted the Severan dynasty's rule, being preceded by Caracalla and succeeded by Elagabalus"
            },
            {
                "sourceSlug": "macrinus",
                "sourceName": "Macrinus",
                "verb": "TRAINED_AS",
                "targetSlug": "roman-jurisprudence",
                "targetName": "Roman Jurisprudence",
                "context": "Macrinus was a trained jurist before his political-military career, one of the last emperors whose background was legal expertise"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Macrinus was the first Roman emperor from outside the senatorial order and the first from Africa, a precedent-setting figure whose brief reign (217-218 CE) opened the era of military emperors from the provinces and foreshadowed the Crisis of the Third Century that would transform the Roman Empire.",
            "significanceCategory": "continental"
        },
        "importanceScore": 8
    },

    "lucius-cornelius-lentulus-niger": {
        "summary": (
            "Lucius Cornelius Lentulus Niger (fl. c. 63–56 BCE) was a Roman aristocrat "
            "of the ancient Cornelii Lentuli family who served as flamen Martialis — "
            "the dedicated priest of Mars, one of the oldest and most prestigious of "
            "Rome's great priesthoods — during the turbulent late Republic. The flaminate "
            "of Mars was one of three flamines maiores (great flamens) whose religious "
            "obligations dated to the regal period of Rome and required extraordinary "
            "ritual observance. The flamen Martialis could not leave Italy, was bound "
            "by extensive taboos, and could not hold public office that required "
            "military command — creating significant tension in a system where "
            "political advancement typically required military service.\n\n"
            "Lentulus Niger is attested in Cicero's correspondence — he appears in "
            "letters from around 63-56 BCE — and his career illustrates the peculiar "
            "constitutional friction between the archaic religious obligations of the "
            "great flamens and the demands of late Republican political competition. "
            "His designation as a possible proconsul created a legal puzzle: could "
            "a flamen Martialis accept a provincial command? The conflict between "
            "religious law (ius sacrum) and civil law (ius civile) was never fully "
            "resolved, and such cases forced the Senate and pontiffs to make "
            "ad hoc rulings that advanced the development of Roman constitutional law.\n\n"
            "Members of the Cornelii Lentuli were prominent in the late Republic — "
            "including the Catilinarian conspirator Publius Cornelius Lentulus Sura — "
            "and Lucius Niger's priestly role placed him at the intersection of the "
            "traditional Roman religious constitution and the political upheavals of the "
            "era of Pompey and Caesar. His case is a window into how ancient Roman "
            "religious obligations constrained and shaped political careers even as the "
            "Republic's institutions were under structural strain."
        ),
        "causes": [
            {
                "title": "The ancient Roman flaminate of Mars required extraordinary ritual observance — including restrictions on travel and political office — that created legal tensions with late Republican political life",
                "type": "Institution",
                "year": "c. 63–56 BCE, Rome"
            },
            {
                "title": "Lentulus Niger came from one of Rome's great patrician families (Cornelii Lentuli), whose traditional claims to prestige included the great priesthoods",
                "type": "Institution",
                "year": "c. 63 BCE, Rome"
            },
            {
                "title": "The political turbulence of the late Republic — including the Catilinarian conspiracy, the triumvirate of Caesar, Pompey, and Crassus — created a context in which even priestly figures were drawn into political conflicts",
                "type": "EventWindow",
                "year": "63–56 BCE, Rome"
            }
        ],
        "effects": [
            {
                "title": "Lentulus Niger's case illustrated the tension between the ancient ius sacrum (sacred law) and the demands of late Republican politics, contributing to the evolution of Roman constitutional law",
                "type": "Idea",
                "year": "c. 63–56 BCE, Rome"
            },
            {
                "title": "The legal questions raised by his possible provincial command and the conflicting obligations of the flaminate advanced Senate and pontifical jurisprudence on the status of the great priests",
                "type": "Institution",
                "year": "c. 56 BCE, Rome"
            },
            {
                "title": "As one of Cicero's correspondents, Lentulus Niger is preserved in the historical record as a minor but documented figure in the intellectual-social networks of the late Republic",
                "type": "Person",
                "year": "c. 63–56 BCE, Rome"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "lucius-cornelius-lentulus-niger",
                "sourceName": "Lucius Cornelius Lentulus Niger",
                "verb": "HELD_ROLE",
                "targetSlug": "flamen-martialis",
                "targetName": "Flamen Martialis (Priest of Mars)",
                "context": "Lentulus Niger served as flamen Martialis, the dedicated priest of Mars, one of Rome's oldest and most prestigious priesthoods"
            },
            {
                "sourceSlug": "lucius-cornelius-lentulus-niger",
                "sourceName": "Lucius Cornelius Lentulus Niger",
                "verb": "CORRESPONDED_WITH",
                "targetSlug": "cicero",
                "targetName": "Marcus Tullius Cicero",
                "context": "Lentulus Niger appears in Cicero's letters as an acquaintance in the late Republican social-political network"
            },
            {
                "sourceSlug": "lucius-cornelius-lentulus-niger",
                "sourceName": "Lucius Cornelius Lentulus Niger",
                "verb": "MEMBER_OF",
                "targetSlug": "cornelii-lentuli",
                "targetName": "Cornelii Lentuli (patrician family)",
                "context": "Lentulus Niger belonged to the Cornelii Lentuli, one of Rome's great patrician families prominent in the late Republic"
            },
            {
                "sourceSlug": "lucius-cornelius-lentulus-niger",
                "sourceName": "Lucius Cornelius Lentulus Niger",
                "verb": "SUBJECT_TO",
                "targetSlug": "roman-sacred-law",
                "targetName": "Roman Sacred Law (Ius Sacrum)",
                "context": "As flamen Martialis, Lentulus Niger was bound by the ancient Roman sacred law that restricted the great flamens from travel, military service, and certain political offices"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "As flamen Martialis in the turbulent late Republic, Lucius Cornelius Lentulus Niger exemplifies the tension between Rome's archaic religious constitution and its increasingly professional political system — a legal-constitutional conflict whose resolution advanced Roman jurisprudence at a critical period of the Republic's transformation.",
            "significanceCategory": "continental"
        },
        "importanceScore": 8
    },

    "minkhaf-i": {
        "summary": (
            "Minkhaf I (fl. c. 2550 BCE) was a son of Pharaoh Khufu — builder of the "
            "Great Pyramid at Giza — who served as a high official of the Egyptian Old "
            "Kingdom during the 4th Dynasty. As a royal prince, he held the title of "
            "vizier (tjaty), the highest administrative office in the Egyptian state "
            "below the pharaoh, responsible for overseeing royal estates, the judiciary, "
            "public works, taxation, and the royal mortuary cult. His mastaba tomb — "
            "a large flat-roofed rectangular funerary structure — was built in the "
            "Western Cemetery adjacent to the Great Pyramid, reflecting his status "
            "as a senior royal son.\n\n"
            "Minkhaf I's career falls within the extraordinarily concentrated royal "
            "building activity of the early 4th Dynasty — the period of Sneferu, Khufu, "
            "and Khafre — when the Egyptian state mobilized the largest organized "
            "construction effort in history. The vizier was the key administrative "
            "coordinator of these projects: managing the thousands of workers, "
            "overseeing the quarrying and transport of stone, and ensuring the "
            "provisioning and housing of the workforce. While direct textual evidence "
            "for Minkhaf I's specific duties is limited, the titles preserved in his "
            "tomb — standard for royal princes serving as senior court officials — "
            "provide the framework for understanding his role.\n\n"
            "The 4th Dynasty vizierate was typically held by close royal relatives, "
            "creating a system in which the highest administrative office was a "
            "family monopoly concentrating political power among the pharaoh's sons "
            "and brothers. Minkhaf I was part of this pattern — his tomb's proximity "
            "to the Great Pyramid speaks to the intimate connection between royal "
            "family, state administration, and the afterlife ideology that defined "
            "Old Kingdom Egypt's political culture."
        ),
        "causes": [
            {
                "title": "The massive administrative demands of Khufu's great pyramid project required trusted royal princes in high administrative offices like the vizierate",
                "type": "Institution",
                "year": "c. 2551–2528 BCE, Egypt"
            },
            {
                "title": "The 4th Dynasty Egyptian state's practice of concentrating the vizierate among close royal relatives placed Khufu's sons like Minkhaf I in the highest administrative roles",
                "type": "Institution",
                "year": "c. 2575–2465 BCE, Egypt"
            },
            {
                "title": "Old Kingdom Egypt's integration of royal mortuary ideology with state administration made high officials also the managers of the royal cult — ensuring Minkhaf I's role in both life and death",
                "type": "Idea",
                "year": "c. 2550 BCE, Egypt"
            }
        ],
        "effects": [
            {
                "title": "Minkhaf I's tomb in the Western Cemetery adjacent to the Great Pyramid preserves evidence of the administrative structure of Khufu's government and the titles held by senior royal sons",
                "type": "Evidence",
                "year": "c. 2550 BCE, Giza"
            },
            {
                "title": "The pattern of family-dominated vizierates established in the early 4th Dynasty would continue through the Old Kingdom, shaping Egyptian administrative culture for centuries",
                "type": "Institution",
                "year": "c. 2550–2100 BCE, Egypt"
            },
            {
                "title": "The physical evidence of royal sons' tombs clustered around the Great Pyramid — including Minkhaf I's mastaba — is a key archaeological source for understanding 4th Dynasty court structure",
                "type": "Evidence",
                "year": "c. 2550 BCE – present, Giza plateau"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "minkhaf-i",
                "sourceName": "Minkhaf I",
                "verb": "SON_OF",
                "targetSlug": "khufu",
                "targetName": "Pharaoh Khufu",
                "context": "Minkhaf I was a son of Pharaoh Khufu (Cheops), builder of the Great Pyramid, and served as a high official in Khufu's administration"
            },
            {
                "sourceSlug": "minkhaf-i",
                "sourceName": "Minkhaf I",
                "verb": "HELD_ROLE",
                "targetSlug": "vizier-of-egypt",
                "targetName": "Vizier (Tjaty) of Egypt",
                "context": "Minkhaf I held the title of vizier (tjaty), the highest administrative office in the Old Kingdom Egyptian state below the pharaoh"
            },
            {
                "sourceSlug": "minkhaf-i",
                "sourceName": "Minkhaf I",
                "verb": "BURIED_AT",
                "targetSlug": "giza-necropolis",
                "targetName": "Giza Necropolis",
                "context": "Minkhaf I's mastaba tomb was built in the Western Cemetery adjacent to the Great Pyramid, reflecting his status as a senior royal son"
            },
            {
                "sourceSlug": "minkhaf-i",
                "sourceName": "Minkhaf I",
                "verb": "MEMBER_OF",
                "targetSlug": "4th-dynasty-egypt",
                "targetName": "Egyptian 4th Dynasty",
                "context": "Minkhaf I was part of the 4th Dynasty royal family during the era of the great pyramid builders"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Minkhaf I, as a vizier and son of Khufu, represents the 4th Dynasty system of royal family administrative control at the apex of Egypt's pyramid-building era — his tomb at Giza providing archaeological evidence of the court hierarchy that coordinated the largest construction project in ancient history.",
            "significanceCategory": "continental"
        },
        "importanceScore": 8
    },

    "edmund-earl-of-rutland": {
        "summary": (
            "Edmund, Earl of Rutland (17 May 1443 – 30 December 1460) was the second "
            "son of Richard, Duke of York — the Yorkist claimant to the English throne — "
            "and Cecily Neville. His death at the age of 17 at the Battle of Wakefield, "
            "fleeing with his tutor Sir Robert Aspall while attempting to escape across "
            "the bridge over the River Calder, became one of the most dramatically "
            "charged incidents of the Wars of the Roses. According to later (possibly "
            "embellished) accounts, he was killed by Lord Clifford of Skipton, who "
            "refused to spare him despite his youth — making the act a byword for "
            "Lancastrian ruthlessness in Yorkist propaganda.\n\n"
            "Edmund's death occurred alongside his father Richard, Duke of York, who "
            "was also killed at Wakefield — a catastrophic double blow to the Yorkist "
            "cause. Edmund had been created Earl of Rutland in 1446 as an infant, "
            "and had accompanied his father to Ireland (1459–1460) during the period "
            "when the Yorkist lords fled England after the Rout of Ludford Bridge. "
            "He returned with his father in late 1460 for the final campaign that "
            "ended in Wakefield. His death and his father's, rather than destroying "
            "the Yorkist cause, galvanized his elder brother Edward (later Edward IV) "
            "and the Earl of Warwick to intensify their campaign.\n\n"
            "Shakespeare immortalized Edmund in Henry VI, Part 3, depicting his death "
            "as a scene of pathetic innocence murdered by a monster. While modern "
            "scholarship questions the dramatic version, Edmund became a symbol in "
            "the Yorkist myth of Lancastrian treachery — helping justify the Yorkist "
            "military campaign and Edward IV's eventual seizure of the throne in 1461."
        ),
        "causes": [
            {
                "title": "Edmund was born into the Yorkist dynastic conflict: as a son of Richard, Duke of York, he was automatically a target for Lancastrian forces",
                "type": "Person",
                "year": "1443–1460, England"
            },
            {
                "title": "The Battle of Wakefield (30 December 1460) — a Lancastrian ambush of the Yorkist forces at Sandal Castle — resulted in the military defeat that cost Edmund his life",
                "type": "EventWindow",
                "year": "1460, Yorkshire"
            },
            {
                "title": "The Lancastrian policy of aggressive pursuit after Wakefield — exemplified by Lord Clifford's reported execution of Edmund — was part of a deliberate strategy to eliminate the Yorkist leadership",
                "type": "Institution",
                "year": "1460, northern England"
            }
        ],
        "effects": [
            {
                "title": "Edmund's death at Wakefield alongside his father galvanized his elder brother Edward (future Edward IV) and the Earl of Warwick to intensify the Yorkist campaign",
                "type": "EventWindow",
                "year": "1460–1461, England"
            },
            {
                "title": "The deaths of Edmund and his father at Wakefield became central to Yorkist propaganda about Lancastrian ruthlessness, helping justify Edward IV's seizure of the throne in 1461",
                "type": "Idea",
                "year": "1461, England"
            },
            {
                "title": "Shakespeare's dramatic portrayal of Edmund's death in Henry VI, Part 3 cemented the episode in English cultural memory as an emblem of youthful innocence destroyed by civil war",
                "type": "Text",
                "year": "1590–1591, England"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "edmund-earl-of-rutland",
                "sourceName": "Edmund, Earl of Rutland",
                "verb": "SON_OF",
                "targetSlug": "richard-duke-of-york",
                "targetName": "Richard, Duke of York",
                "context": "Edmund was the second son of Richard, Duke of York — the Yorkist claimant who was killed alongside him at Wakefield"
            },
            {
                "sourceSlug": "edmund-earl-of-rutland",
                "sourceName": "Edmund, Earl of Rutland",
                "verb": "BROTHER_OF",
                "targetSlug": "edward-iv-of-england",
                "targetName": "Edward IV of England",
                "context": "Edmund's elder brother Edward became Edward IV after the Yorkist triumph in 1461, avenging Edmund's and their father's deaths at Wakefield"
            },
            {
                "sourceSlug": "edmund-earl-of-rutland",
                "sourceName": "Edmund, Earl of Rutland",
                "verb": "KILLED_AT",
                "targetSlug": "battle-of-wakefield",
                "targetName": "Battle of Wakefield (1460)",
                "context": "Edmund was killed at the Battle of Wakefield on 30 December 1460, at age 17, reportedly by Lord Clifford while attempting to flee"
            },
            {
                "sourceSlug": "edmund-earl-of-rutland",
                "sourceName": "Edmund, Earl of Rutland",
                "verb": "DRAMATIZED_IN",
                "targetSlug": "henry-vi-part-3-shakespeare",
                "targetName": "Henry VI, Part 3 (Shakespeare)",
                "context": "Shakespeare dramatized Edmund's death in Henry VI, Part 3, depicting it as an emblematic scene of Lancastrian ruthlessness killing an innocent youth"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Edmund, Earl of Rutland's death at Wakefield at age 17 — alongside his father Richard, Duke of York — was a pivot point of the Wars of the Roses: it destroyed immediate Yorkist leadership while galvanizing Edward IV's drive for the throne, and became a powerful symbol of civil war's human cost memorialized by Shakespeare.",
            "significanceCategory": "continental"
        },
        "importanceScore": 8
    },

    "johann-von-posilge": {
        "summary": (
            "Johann von Posilge (c. 1350–1405) was a German ecclesiastic in the service "
            "of the Teutonic Order who authored the Chronik des Landes Preussen "
            "(Chronicle of the Land of Prussia) — one of the most important medieval "
            "German chronicles of Eastern Europe and an indispensable source for the "
            "history of the Teutonic Knights, the Baltic Crusade, and the emergence "
            "of Poland-Lithuania as a regional power in the late 14th and early 15th "
            "centuries. He was an official of the Teutonic Order's territorial "
            "administration in Prussia.\n\n"
            "The Chronicle covers the years approximately 1360 to 1419 (though Posilge "
            "died in 1405 and later sections were continued by others). It provides "
            "detailed narrative accounts of the Teutonic Order's military campaigns "
            "against Lithuania and Poland, internal Prussian affairs, relations with "
            "the German princes and the papacy, and the great crisis of the Order's "
            "decline — culminating in the Battle of Tannenberg (Grunwald) in 1410, "
            "when a Polish-Lithuanian-Tartar army decisively defeated the Teutonic "
            "Knights, killing the Grand Master Ulrich von Jungingen and destroying "
            "the Order's military dominance. While Posilge did not live to describe "
            "Tannenberg, the framework his Chronicle created became the foundation "
            "for later accounts of this pivotal battle.\n\n"
            "Posilge wrote in Middle High German (with some Latin passages) and drew "
            "on official Teutonic Order records, his own observations, and the "
            "oral accounts of contemporaries. His Chronicle is notable for its "
            "relative frankness about the Order's difficulties and the social "
            "conditions in Prussia — including peasant unrest, economic tensions, "
            "and the politics of Baltic urban communities. It remains an essential "
            "source for scholars of the Teutonic Order and the political history "
            "of late medieval Eastern Europe."
        ),
        "causes": [
            {
                "title": "The Teutonic Order's territorial administration in Prussia required documentary and chronicle keeping to maintain institutional memory of military campaigns, legal arrangements, and political relations",
                "type": "Institution",
                "year": "c. 1350–1405, Prussia"
            },
            {
                "title": "The dramatic escalation of the conflict between the Teutonic Order and the united Polish-Lithuanian state in the late 14th century made chronicle documentation of military and diplomatic events urgent",
                "type": "EventWindow",
                "year": "c. 1386–1410, Eastern Europe"
            },
            {
                "title": "Posilge's position as an administrative official of the Teutonic Order gave him access to official records and insider knowledge of the Order's decisions and campaigns",
                "type": "Institution",
                "year": "c. 1350–1405, Teutonic Prussia"
            }
        ],
        "effects": [
            {
                "title": "Posilge's Chronicle is an indispensable primary source for the political and military history of the Teutonic Order, Poland-Lithuania, and Baltic Prussia in the late 14th and early 15th centuries",
                "type": "Text",
                "year": "c. 1405 – present, Eastern European historiography"
            },
            {
                "title": "The Chronicle's framework provided the foundation for subsequent accounts of the Battle of Tannenberg (1410), the most consequential defeat of the Teutonic Order",
                "type": "EventWindow",
                "year": "1410 – present, historical scholarship"
            },
            {
                "title": "Posilge's relatively frank account of Prussian social conditions and the Order's internal difficulties gives historians access to the perspective of the Teutonic Order's administrative class",
                "type": "Idea",
                "year": "c. 1360–1419, scholarly use"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "johann-von-posilge",
                "sourceName": "Johann von Posilge",
                "verb": "AUTHORED",
                "targetSlug": "chronik-des-landes-preussen",
                "targetName": "Chronik des Landes Preussen",
                "context": "Posilge's Chronicle of the Land of Prussia is an essential primary source for the Teutonic Order's history and late medieval Eastern European politics"
            },
            {
                "sourceSlug": "johann-von-posilge",
                "sourceName": "Johann von Posilge",
                "verb": "SERVED",
                "targetSlug": "teutonic-order",
                "targetName": "Teutonic Order",
                "context": "Posilge was an administrative official of the Teutonic Order's Prussian territory, giving him insider access to the Order's records and decision-making"
            },
            {
                "sourceSlug": "johann-von-posilge",
                "sourceName": "Johann von Posilge",
                "verb": "DOCUMENTED",
                "targetSlug": "battle-of-tannenberg-1410",
                "targetName": "Battle of Tannenberg (Grunwald) (1410)",
                "context": "While Posilge died before Tannenberg, his Chronicle provided the historical framework and narrative momentum leading up to the Teutonic Order's greatest defeat"
            },
            {
                "sourceSlug": "johann-von-posilge",
                "sourceName": "Johann von Posilge",
                "verb": "DOCUMENTED",
                "targetSlug": "teutonic-knights-lithuanian-wars",
                "targetName": "Teutonic Order-Lithuanian Wars",
                "context": "The Chronicle is a primary source for the Teutonic Order's military campaigns against Lithuania in the late 14th century"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Johann von Posilge's Chronik des Landes Preussen is an indispensable primary source for the Teutonic Order's history in the era of its greatest military power and eventual decline — providing the most detailed insider account of Baltic Crusade politics in the generation leading to the decisive Battle of Tannenberg (1410).",
            "significanceCategory": "continental"
        },
        "importanceScore": 8
    },

    "john-dynham-1st-baron-dynham": {
        "summary": (
            "John Dynham, 1st Baron Dynham (c. 1433–1501) was a loyal Devonshire nobleman "
            "who served the English crown across three dynasties — Lancastrian, Yorkist, "
            "and Tudor — ultimately reaching the office of Lord High Treasurer of England "
            "(1486–1501), which he held under both Richard III and Henry VII. His career "
            "combined military service in the Wars of the Roses, naval command in the "
            "Channel, and long financial stewardship of the English crown — making him "
            "one of the most durable royal servants of the late 15th century.\n\n"
            "Dynham had come to Edward IV's attention through loyal service in the West "
            "Country during the Lancastrian-Yorkist conflicts of the 1460s. He was "
            "created 1st Baron Dynham in 1467. He served as Captain of Calais — the "
            "English crown's most important continental possession — and commanded "
            "English naval forces in operations against France. His greatest office "
            "was Lord High Treasurer, which he administered for fifteen years through "
            "the turbulent dynastic transition from Richard III to Henry VII, and "
            "through the early Tudor period. He oversaw royal finances during the "
            "critical years of Henry VII's government consolidation, including the "
            "prosecution of Lambert Simnel's rebellion (1487) and the various Yorkist "
            "pretender crises of the 1490s.\n\n"
            "Dynham died in 1501 without male heirs, so the barony became extinct. "
            "His remarkable ability to serve Yorkist and Tudor monarchs alike — at "
            "a moment when loyalty to either dynasty often meant death at the hands "
            "of the other — reflects both his political skill and the pragmatic "
            "approach of administrators who made themselves indispensable through "
            "technical expertise rather than dynastic commitment. He was buried at "
            "Sutton Bingham, Somerset."
        ),
        "causes": [
            {
                "title": "Dynham's early loyal service to Edward IV in the Wars of the Roses earned him the barony and the trust that gave him access to the highest offices",
                "type": "EventWindow",
                "year": "c. 1460–1467, England"
            },
            {
                "title": "His expertise in naval and financial administration — as Captain of Calais and as a royal financier — made him invaluable to monarchs who needed competent technical administrators",
                "type": "Institution",
                "year": "c. 1467–1501, England"
            },
            {
                "title": "The political chaos of the Wars of the Roses created opportunities for capable provincial noblemen to rise through demonstrated administrative ability rather than dynastic rank",
                "type": "EventWindow",
                "year": "c. 1460–1485, England"
            }
        ],
        "effects": [
            {
                "title": "As Lord High Treasurer under Henry VII for 15 years, Dynham provided crucial administrative continuity in royal finance during the critical early Tudor consolidation of government",
                "type": "Institution",
                "year": "1486–1501, England"
            },
            {
                "title": "His management of royal finances helped Henry VII develop the methods of financial control that would make the early Tudor crown unusually solvent",
                "type": "Institution",
                "year": "1486–1501, England"
            },
            {
                "title": "His career as a loyalist who served Yorkist and Tudor crowns alike established a model of technocratic royal service that Henry VII would rely on — preferring administrators over magnates",
                "type": "Idea",
                "year": "1485–1501, England"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "john-dynham-1st-baron-dynham",
                "sourceName": "John Dynham, 1st Baron Dynham",
                "verb": "SERVED_UNDER",
                "targetSlug": "henry-vii-of-england",
                "targetName": "Henry VII of England",
                "context": "Dynham served Henry VII as Lord High Treasurer from 1486 until his death in 1501, providing crucial administrative continuity during the Tudor consolidation"
            },
            {
                "sourceSlug": "john-dynham-1st-baron-dynham",
                "sourceName": "John Dynham, 1st Baron Dynham",
                "verb": "SERVED_UNDER",
                "targetSlug": "edward-iv-of-england",
                "targetName": "Edward IV of England",
                "context": "Dynham's early career was built on loyal service to Edward IV, who created him 1st Baron Dynham in 1467"
            },
            {
                "sourceSlug": "john-dynham-1st-baron-dynham",
                "sourceName": "John Dynham, 1st Baron Dynham",
                "verb": "COMMANDED",
                "targetSlug": "captaincy-of-calais",
                "targetName": "Captaincy of Calais",
                "context": "Dynham served as Captain of Calais, overseeing England's most important continental possession"
            },
            {
                "sourceSlug": "john-dynham-1st-baron-dynham",
                "sourceName": "John Dynham, 1st Baron Dynham",
                "verb": "HELD_OFFICE",
                "targetSlug": "lord-high-treasurer-of-england",
                "targetName": "Lord High Treasurer of England",
                "context": "Dynham was Lord High Treasurer from 1486 to 1501, serving under both Richard III and Henry VII"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "John Dynham's 15-year tenure as Lord High Treasurer under Henry VII — spanning the transition from Yorkist to Tudor government — made him a key figure in the administrative continuity that enabled the early Tudor crown to establish financial discipline and solvent government after the Wars of the Roses.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "james-hamilton-1st-lord-hamilton": {
        "summary": (
            "James Hamilton, 1st Lord Hamilton (c. 1415–1479) was a Scottish nobleman "
            "whose marriage to Princess Mary Stewart — daughter of James II of Scotland — "
            "established the House of Hamilton as one of Scotland's greatest noble "
            "dynasties and gave his descendants a near-royal claim to the Scottish "
            "throne that would make them politically significant for centuries. "
            "He was created Lord Hamilton by James II of Scotland in 1445, rewarded "
            "for his political loyalty and military service.\n\n"
            "Hamilton's importance lies primarily in his dynastic position: his marriage "
            "to Mary Stewart (the king's daughter) in 1474 — after the annulment of "
            "his earlier marriages — brought the royal blood of the House of Stewart "
            "into the Hamilton line. Their son James Hamilton, 1st Earl of Arran, "
            "would be one of the most powerful figures in 16th-century Scotland, "
            "and the Hamiltons would repeatedly find themselves as the heirs presumptive "
            "to the Scottish crown — most prominently in the period of Mary, Queen of "
            "Scots. The Hamilton claim to the Scottish succession was a recurring "
            "feature of Scottish politics for more than a century after his death.\n\n"
            "James Hamilton 1st Lord Hamilton served James II and James III of Scotland "
            "in various military and administrative capacities, participating in the "
            "border conflicts that characterized Scottish-English relations in the mid-15th "
            "century. His creation as lord reflected the James II's policy of building "
            "a new noble affinity to replace the power of the Black Douglases, whom "
            "James II had destroyed in the 1450s. Hamilton was part of the generation "
            "of 'new men' elevated by the crown to fill the power vacuum left by the "
            "Douglases' fall."
        ),
        "causes": [
            {
                "title": "James II's destruction of the Black Douglas affinity in the 1450s created a political vacuum that the king filled by elevating loyal new lords, including Hamilton",
                "type": "EventWindow",
                "year": "c. 1452–1460, Scotland"
            },
            {
                "title": "Hamilton's royal marriage to Princess Mary Stewart (daughter of James II) established the dynastic connection that gave the House of Hamilton its near-royal status",
                "type": "Person",
                "year": "c. 1474, Scotland"
            },
            {
                "title": "The Scottish crown's need for reliable military and political supporters in the west of Scotland created the context for Hamilton's elevation to the peerage in 1445",
                "type": "Institution",
                "year": "1445, Scotland"
            }
        ],
        "effects": [
            {
                "title": "Hamilton's marriage to Mary Stewart created the dynastic basis for the House of Hamilton's near-royal claim — making his descendants heirs presumptive to the Scottish throne in the 16th century",
                "type": "Institution",
                "year": "c. 1479–1600, Scotland"
            },
            {
                "title": "His son James Hamilton, 1st Earl of Arran, became one of the most powerful Scottish magnates of the early 16th century, exercising effective regency control during James V's minority",
                "type": "Person",
                "year": "c. 1500–1550, Scotland"
            },
            {
                "title": "The House of Hamilton became the principal Protestant noble dynasty of 16th-century Scotland, shaping the religious and political conflicts of the Reformation period in Scotland",
                "type": "Movement",
                "year": "c. 1550–1700, Scotland"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "james-hamilton-1st-lord-hamilton",
                "sourceName": "James Hamilton, 1st Lord Hamilton",
                "verb": "MARRIED",
                "targetSlug": "mary-stewart-princess-of-scotland",
                "targetName": "Princess Mary Stewart of Scotland",
                "context": "Hamilton's marriage to Mary Stewart (daughter of James II) established the royal connection that made the Hamiltons heirs presumptive to the Scottish throne"
            },
            {
                "sourceSlug": "james-hamilton-1st-lord-hamilton",
                "sourceName": "James Hamilton, 1st Lord Hamilton",
                "verb": "SERVED_UNDER",
                "targetSlug": "james-ii-of-scotland",
                "targetName": "James II of Scotland",
                "context": "Hamilton was elevated to Lord Hamilton by James II as part of the king's creation of a new noble affinity after destroying the Black Douglases"
            },
            {
                "sourceSlug": "james-hamilton-1st-lord-hamilton",
                "sourceName": "James Hamilton, 1st Lord Hamilton",
                "verb": "FOUNDED",
                "targetSlug": "house-of-hamilton",
                "targetName": "House of Hamilton",
                "context": "James Hamilton established the House of Hamilton as one of Scotland's greatest noble dynasties through his marriage to Mary Stewart"
            },
            {
                "sourceSlug": "james-hamilton-1st-lord-hamilton",
                "sourceName": "James Hamilton, 1st Lord Hamilton",
                "verb": "FATHER_OF",
                "targetSlug": "james-hamilton-1st-earl-of-arran",
                "targetName": "James Hamilton, 1st Earl of Arran",
                "context": "His son James Hamilton became 1st Earl of Arran and one of the most powerful Scottish magnates of the early 16th century"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "James Hamilton, 1st Lord Hamilton's marriage to Princess Mary Stewart established the House of Hamilton as Scotland's second royal family — his descendants becoming heirs presumptive to the Scottish throne and major actors in the religious and dynastic conflicts of 16th-century Scotland, making him the dynastic founder of one of history's most politically significant noble houses.",
            "significanceCategory": "regional"
        },
        "importanceScore": 7
    },

    "bao-zheng": {
        "summary": (
            "Bao Zheng (包拯, 999–1062 CE) — known as 'Justice Bao' (包公, Bāo Gōng) — "
            "was a Song Dynasty official who became the most celebrated symbol of "
            "incorruptible justice and impartial governance in Chinese history and culture. "
            "As prefect of Kaifeng (the Song capital) and a senior court official, "
            "he acquired a legendary reputation for prosecuting powerful officials "
            "and imperial relatives without fear, refusing bribes absolutely, and "
            "adjudicating cases with scrupulous fairness. Born in Hefei (Anhui Province), "
            "he served the Song court under Emperor Renzong.\n\n"
            "Bao's historical career included service in multiple provincial posts "
            "before his appointment as Prefect of Kaifeng in 1056 — where his "
            "administration became a byword for accessibility and fairness. He "
            "opened the court gates to allow ordinary citizens to present cases "
            "directly, rather than going through intermediaries who charged fees. "
            "He successfully prosecuted a cousin of Empress Guo for corruption "
            "and repeatedly memorialized the emperor against the abuses of "
            "powerful families. He served in high advisory roles including "
            "the Bureau of Military Affairs and was known for the quality of "
            "his policy memorials on financial reform, military readiness, and "
            "administrative integrity.\n\n"
            "After his death, Bao Zheng was elevated through folklore, theatre, "
            "and popular fiction into a semi-mythical judge-hero who could try "
            "the living and the dead, and whose rulings were beyond appeal even "
            "by the emperor. The dramatic cycle of 'Judge Bao' stories — hundreds "
            "of plays, novels, and case collections — made him one of the most "
            "recognized figures in Chinese popular culture across nearly a millennium. "
            "He remains in modern China an icon of judicial integrity, featured in "
            "countless TV dramas, and his face — traditionally depicted as jet black "
            "with a crescent moon birthmark on his forehead — is one of Chinese "
            "culture's most recognizable symbols of justice."
        ),
        "causes": [
            {
                "title": "The Song Dynasty's sophisticated examination-based bureaucracy created the career path for talented commoner-officials like Bao Zheng to rise to high office on the basis of merit and integrity",
                "type": "Institution",
                "year": "960–1062 CE, Song China"
            },
            {
                "title": "Bao's personal commitment to Confucian principles of governance — loyalty, integrity, and impartiality — drove his exceptional resistance to corruption in a culture where official conduct was theorized but often compromised",
                "type": "Idea",
                "year": "c. 1019–1062 CE, China"
            },
            {
                "title": "The Song Dynasty's chronic problems of bureaucratic corruption, especially among officials connected to imperial relatives and powerful families, created the political context in which Bao's incorruptibility appeared extraordinary",
                "type": "Institution",
                "year": "c. 1000–1062 CE, Kaifeng"
            }
        ],
        "effects": [
            {
                "title": "Bao Zheng became the paradigmatic symbol of judicial integrity in Chinese culture — an ideal of impartial governance that has remained politically resonant for nearly a millennium",
                "type": "Idea",
                "year": "1062 CE – present, China"
            },
            {
                "title": "The 'Judge Bao' dramatic tradition — hundreds of plays and case stories — became one of the most productive fictional cycles in Chinese popular literature, continuously reinterpreted across dynasties",
                "type": "Text",
                "year": "c. 13th century – present, China"
            },
            {
                "title": "Bao's model of accessible justice — opening court directly to ordinary citizens — became an aspirational standard in Chinese administrative discourse and reform proposals",
                "type": "Idea",
                "year": "1062 CE – 20th century, China"
            }
        ],
        "relationships": [
            {
                "sourceSlug": "bao-zheng",
                "sourceName": "Bao Zheng",
                "verb": "SERVED_UNDER",
                "targetSlug": "emperor-renzong-song",
                "targetName": "Emperor Renzong of Song",
                "context": "Bao Zheng served Emperor Renzong as Prefect of Kaifeng and senior court official, acquiring his legendary reputation during this reign"
            },
            {
                "sourceSlug": "bao-zheng",
                "sourceName": "Bao Zheng",
                "verb": "PROSECUTED",
                "targetSlug": "imperial-relatives-song",
                "targetName": "Imperial Relatives (Song Dynasty)",
                "context": "Bao famously prosecuted imperial relatives and powerful officials without fear of retribution, including a cousin of Empress Guo"
            },
            {
                "sourceSlug": "bao-zheng",
                "sourceName": "Bao Zheng",
                "verb": "EMBODIED",
                "targetSlug": "confucian-ideal-of-just-governance",
                "targetName": "Confucian Ideal of Just Governance",
                "context": "Bao Zheng's career and posthumous legend embody the Confucian ideal of the official who serves justice rather than personal gain or factional loyalty"
            },
            {
                "sourceSlug": "bao-zheng",
                "sourceName": "Bao Zheng",
                "verb": "INSPIRED",
                "targetSlug": "judge-bao-dramatic-tradition",
                "targetName": "Judge Bao Dramatic Tradition (Chinese popular culture)",
                "context": "After his death, Bao became the subject of hundreds of plays, stories, and novels forming one of the richest cycles in Chinese popular culture"
            }
        ],
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Bao Zheng's career as Prefect of Kaifeng gave Chinese culture its most powerful image of judicial integrity — 'Justice Bao' — whose posthumous legend in drama, fiction, and popular memory has shaped Chinese ideas about just governance for nearly a thousand years and remains culturally alive today.",
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
    print(f"Enriching {len(ENRICHMENTS)} entities (Batch 9: ancient/medieval/Song Dynasty)...")
    for slug, data in ENRICHMENTS.items():
        enrich_entity(slug, data)
    print("\nDone.")
