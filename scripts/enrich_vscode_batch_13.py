#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 13 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: ush, julius-of-novara, aeacides-of-epirus, magnus-felix-ennodius,
          paphnutius-of-thebes, titus-of-bostra, international-monetary-fund,
          thorfinn-of-hamar
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-13-may2026"

ENRICHMENTS = {

"ush": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221ush.json",
  "slug": "ush",
  "data": {
    "summary": "Ush (also transcribed as Ush or Uš; fl. c. 2450 BCE) was a ruler (ensi, governor-king) of Umma — one of the city-states of ancient Sumer in what is now southern Iraq — who became infamous in Sumerian historical tradition for a military aggression against the neighbouring city-state of Lagash that is among the earliest recorded acts of international relations involving formal treaty violation. The conflict between Umma and Lagash over the 'Gu-edena' (the sacred field boundary zone between the two cities) was one of the most persistent disputes in early Sumerian history — a border conflict whose sequence of events was recorded by the Lagashite kings and that provides some of the earliest evidence for interstate diplomacy, treaty obligations, and military conflict in human history.\n\nAccording to the Lagashite royal inscriptions — particularly those of Enmetena (c. 2400 BCE) and Uru-inimgina (c. 2350 BCE) — Ush of Umma violated the boundary established by the god Enlil between Lagash and Umma (the boundary marker erected by an earlier peace settlement) and invaded the Gu-edena, removing Lagash's boundary stelae and plundering the territory. This act of treaty violation and aggressive expansion set off a series of wars between Umma and Lagash that continued for generations. Ush is thus presented in the Lagashite sources as the initiator of a fundamental violation of divine order — a king who crossed the boundary established by the gods themselves.\n\nThe historical significance of Ush lies primarily in the context of the earliest documented interstate conflicts in history. The Lagash-Umma wars represent the earliest surviving evidence of systematic interstate warfare, formal diplomatic boundaries, treaty obligations, and the concept of a just war fought to recover violated territory — themes that would recur throughout human history. Ush himself, as the initiator of the violation, is the villainous counterpart in a narrative that the Lagashite tradition used to justify their own subsequent military actions.",
    "causes": [
      "The competition between adjacent Sumerian city-states for agricultural land and water rights in the fertile but limited alluvial plain of southern Mesopotamia — particularly the Gu-edena boundary zone between Umma and Lagash — created the persistent territorial tension that Ush's aggression escalated into open warfare.",
      "The weakness or absence of effective supraregional authority in early Dynastic Sumer (c. 2900–2350 BCE) — the period of city-state competition before the Akkadian unification — meant that boundary disputes could only be resolved through military force or diplomacy backed by the authority of the major temples and their patron deities.",
      "Ush's calculation that military advantage favoured Umma in this period — the specific political and military balance of power between the two city-states that made aggressive expansion seem feasible — motivated the border violation that the Lagashite tradition condemned and that set off generations of conflict."
    ],
    "effects": [
      "Ush's violation of the Lagash-Umma boundary initiated a cycle of warfare that lasted for several generations — the Lagash-Umma wars that are documented in the royal inscriptions of multiple Lagashite kings and that constitute some of the earliest surviving evidence for interstate military conflict.",
      "The Lagashite tradition of recording and justifying their wars against Umma — partly as responses to Ush's original violation — produced some of the earliest surviving historical inscriptions that go beyond mere dynastic records to provide narrative accounts of military and diplomatic events.",
      "The concept embedded in the Lagashite responses to Ush — that Umma had violated a divinely established boundary and that Lagash's wars were just wars of restitution — contributed to the development of early conceptions of just war and legitimate military action in the ancient Near Eastern tradition."
    ],
    "relationships": [
      {"sourceSlug": "ush", "sourceName": "Ush of Umma", "verb": "ATTACKS", "targetSlug": "lagash", "targetName": "Lagash (City-State)", "context": "Ush's violation of the boundary between Umma and Lagash — removing Lagash's boundary stelae and invading the Gu-edena — initiated the Lagash-Umma wars that are among the earliest documented interstate conflicts in history."},
      {"sourceSlug": "ush", "sourceName": "Ush of Umma", "verb": "RULES", "targetSlug": "umma", "targetName": "Umma (Sumerian City-State)", "context": "Ush was ensi (ruler/governor) of Umma — the Sumerian city-state whose competition with Lagash over the Gu-edena boundary zone is documented in the earliest surviving historical inscriptions."},
      {"sourceSlug": "early-dynastic-sumer", "sourceName": "Early Dynastic Sumer", "verb": "PRODUCES", "targetSlug": "ush", "targetName": "Ush of Umma", "context": "Ush's career exemplifies the interstate competition of Early Dynastic Sumer (c. 2900–2350 BCE) — the period of Sumerian city-state rivalry before Akkadian unification that produced the earliest evidence for organised warfare and interstate diplomacy."}
    ],
    "places": [
      {"name": "Umma (Tell Jokha, southern Iraq)", "role": "The Sumerian city-state of which Ush was ruler — one of the most powerful early Sumerian city-states and Lagash's primary rival"},
      {"name": "Lagash (Tell al-Hiba, southern Iraq)", "role": "The city-state against whose territory Ush directed his aggression — the source of the inscriptions that record Ush's violation and preserve his name in history"},
      {"name": "Gu-edena (boundary zone, southern Mesopotamia)", "role": "The disputed agricultural territory between Umma and Lagash — the 'sacred field' whose boundary Ush violated, initiating the Lagash-Umma wars"}
    ],
    "subjects": ["Ancient Sumer", "Mesopotamian History", "Classical Era", "Ancient Near East", "Ancient Warfare", "Ancient History", "City-States", "Early Civilisation"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 5,
      "significanceNarrative": "Ush of Umma (c. 2450 BCE) was the Sumerian ruler whose violation of the Lagash-Umma boundary initiated one of the earliest documented interstate wars in history — the Lagash-Umma conflicts recorded in royal inscriptions that provide the earliest evidence for formal treaties, boundary markers, and justified warfare. His aggression is preserved in Lagashite tradition as the archetypal act of treaty violation that launched generations of conflict.",
      "significanceCategory": "local"
    }
  }
},

"julius-of-novara": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250julius-of-novara.json",
  "slug": "julius-of-novara",
  "data": {
    "summary": "Julius of Novara (died c. 390 CE) was a Christian martyr venerated in the Catholic and Eastern Orthodox traditions — a deacon or priest of Novara (Roman Novaria, in the Piedmont region of northern Italy) who is commemorated as having suffered martyrdom in the late 4th century CE. Julius is also closely associated in hagiographic tradition with his brother Julius of Domodossola (or Julius of Castello), and the two brothers are sometimes conflated or distinguished depending on the source; the tradition of Julius and Julian of Domodossola, who evangelised the Val d'Ossola (the Ossola valley in the Alps) in the late 4th century, overlaps significantly with the Julius of Novara tradition.\n\nThe historical evidence for Julius of Novara is thin: his veneration rests primarily on local hagiographic tradition, the record in the Roman Martyrology, and the church dedications in the Novara and Ossola regions that bear his name. He is associated with a period — the late 4th century CE in the western Roman Empire — when Christianity was undergoing its rapid transition from persecuted minority to state religion (after the Edict of Milan in 313 CE and Theodosius I's establishment of Christianity as the sole state religion in 380 CE). The 'martyrdom' attributed to Julius of Novara may reflect either a genuine persecution (the Arian controversies of the mid-4th century produced violence against Nicene Christians in parts of the empire) or later hagiographic elaboration of what may originally have been a confessor tradition.\n\nJulius of Novara's cult was centred in the Novara region and the Val d'Ossola — an Alpine corridor of significant importance for trans-Alpine communication between northern Italy and the Swiss/German territories. His feast day is celebrated on 31 January in the Roman Martyrology.",
    "causes": [
      "The rapid Christianisation of the Roman Empire following Constantine's conversion and the Edict of Milan (313 CE) created both the opportunity for Christian missionary activity in previously under-evangelised Alpine regions and the context of religious controversy (Arianism vs Nicene orthodoxy) within which the martyrdom attributed to Julius may have occurred.",
      "The Val d'Ossola's position as an important Alpine transit route — connecting the Po plain of northern Italy with trans-Alpine routes to Switzerland and Germany — made it a significant corridor for both commercial traffic and cultural/religious transmission, providing the context for the evangelisation activities attributed to Julius and his associates.",
      "The late 4th century church's active programme of organising local Christian communities and appointing clergy in the towns and rural areas of the western empire created the institutional framework within which figures like Julius of Novara operated."
    ],
    "effects": [
      "The cult of Julius of Novara contributed to the Christianisation of the Piedmont and Val d'Ossola regions — his veneration as a local martyr provided a sacred focus for Christian community formation in the Alpine zone between northern Italy and the trans-Alpine territories.",
      "The church dedications and local cult associated with Julius of Novara preserved the memory of early Christian communities in the Novara region, contributing to the documentary record of late antique Christianisation in northern Italy.",
      "Julius's commemoration in the Roman Martyrology ensured his perpetual liturgical recognition within the Catholic tradition — embedding the memory of early Alpine Christian communities in the universal church's calendar of saints."
    ],
    "relationships": [
      {"sourceSlug": "julius-of-novara", "sourceName": "Julius of Novara", "verb": "EVANGELISES", "targetSlug": "val-dossola", "targetName": "Val d'Ossola, Alpine Region", "context": "Julius and his associates are credited with evangelising the Val d'Ossola and the Novara region — Alpine territories that became early centres of northern Italian Christianity."},
      {"sourceSlug": "early-christianity", "sourceName": "Early Christianity", "verb": "PRODUCES", "targetSlug": "julius-of-novara", "targetName": "Julius of Novara", "context": "Julius of Novara was a product of the late 4th century CE Christianisation of the Roman Empire — the period of rapid Christian expansion into previously under-evangelised regions following Constantine's conversion."},
      {"sourceSlug": "julius-of-novara", "sourceName": "Julius of Novara", "verb": "VENERATED_AS", "targetSlug": "christian-martyrs", "targetName": "Christian Martyrs (Late Antique)", "context": "Julius of Novara's veneration as a martyr placed him in the tradition of late antique Christian saints whose cult helped to Christianise local communities and establish sacred geography in post-Roman Europe."}
    ],
    "places": [
      {"name": "Novara (Novaria), Piedmont, Italy", "role": "The Roman city associated with Julius's ecclesiastical career — the episcopal centre of the region and the focus of his cult"},
      {"name": "Val d'Ossola, Piedmont Alps, Italy", "role": "The Alpine valley associated with Julius's evangelising activity — an important trans-Alpine corridor where his cult was centred"}
    ],
    "subjects": ["Early Christianity", "Christian Martyrs", "Classical Era", "Italy", "Late Antique Church", "4th Century CE", "Northern Italy", "Saints"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 3,
      "significanceNarrative": "Julius of Novara was a late 4th-century Christian martyr venerated in the Novara and Val d'Ossola regions of northern Italy — a local saint whose cult contributed to the Christianisation of the Alpine territories. His historical evidence is thin, resting primarily on local hagiographic tradition and the Roman Martyrology.",
      "significanceCategory": "local"
    }
  }
},

"aeacides-of-epirus": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221aeacides-of-epirus.json",
  "slug": "aeacides-of-epirus",
  "data": {
    "summary": "Aeacides of Epirus (died 312 BCE) was King of Epirus in northwestern Greece (modern Albania/northwestern Greece) — father of Pyrrhus of Epirus, one of antiquity's greatest generals, and a significant figure in the turbulent Successor (Diadochi) politics that followed Alexander the Great's death in 323 BCE. Aeacides ruled Epirus from approximately 330 BCE until his death in 312 BCE, navigating the complex and shifting alliances of the early Diadochi period that followed Alexander's death and attempting to maintain Epirote independence and power amid the competing claims of Cassander, Antigonus, and other successors.\n\nAeacides was a member of the Aeacid dynasty — the royal house of Epirus that traced its lineage back to Achilles's son Neoptolemus (and thus to Aeacus, the father of Achilles), making them, in Greek royal genealogical tradition, distant kin of Alexander the Great (whose mother Olympias was an Epirote princess of the same Aeacid dynasty). This genealogical connection — and the fact that Olympias herself sought refuge in Epirus — drew Aeacides into the Macedonian succession struggles. He was a supporter of Olympias and the claims of Alexander IV (Alexander the Great's posthumous son by Roxane) against Cassander, who had seized effective control of Macedonia.\n\nAeacides's support for Olympias brought him into direct military conflict with Cassander — and the Epirote people, exhausted by the costs of these Macedonian political adventures, revolted against him, expelling Aeacides and replacing him with a different ruler. Aeacides fought to regain his kingdom and was killed in battle in 312 BCE, leaving his young son Pyrrhus to eventually recover the Epirote throne and build the extraordinary military career that would make Epirus temporarily one of the major powers of the Mediterranean world.",
    "causes": [
      "The Diadochi succession crisis following Alexander the Great's death (323 BCE) — the competition among his generals for control of his empire — drew Aeacides into the Macedonian power struggles through his genealogical connection to the Aeacid dynasty and his support for Olympias and Alexander IV.",
      "The Epirote kingdom's proximity to Macedonia and its genealogical and political ties to the Macedonian royal house (through Olympias) made Epirus inevitably involved in the Macedonian succession — Aeacides could not remain neutral when his own dynasty's claims and family connections were at stake.",
      "The costs of Aeacides's military involvement in Macedonian politics — the campaigns that exhausted Epirote resources — alienated his own people, producing the popular revolt that expelled him and directly caused his death in the campaign to recover his kingdom."
    ],
    "effects": [
      "Aeacides's death left his young son Pyrrhus temporarily without a kingdom — Pyrrhus spent years in exile at the Ptolemaic court in Egypt before recovering Epirus and building the military career that made him one of antiquity's greatest generals (the 'Pyrrhic victory' concept derives from his campaigns in Italy and Sicily).",
      "The Epirote revolt against Aeacides illustrated the tension between dynastic political adventurism and the interests of the subject population — a tension that would recur in Epirote history and that shaped the limits of royal power even in the Hellenistic kingdoms.",
      "Aeacides's career contributed to the consolidation of the post-Alexandrian Diadochi settlement by demonstrating the costs of small kingdoms supporting losing sides in the succession struggles — a lesson that shaped subsequent Epirote policy under Pyrrhus."
    ],
    "relationships": [
      {"sourceSlug": "aeacides-of-epirus", "sourceName": "Aeacides of Epirus", "verb": "PARENT_OF", "targetSlug": "pyrrhus-of-epirus", "targetName": "Pyrrhus of Epirus", "context": "Aeacides was the father of Pyrrhus of Epirus — antiquity's great general whose campaigns in Italy and Sicily (279–275 BCE) against Rome introduced the concept of 'Pyrrhic victory'."},
      {"sourceSlug": "cassander-of-macedon", "sourceName": "Cassander of Macedon", "verb": "DEFEATS", "targetSlug": "aeacides-of-epirus", "targetName": "Aeacides of Epirus", "context": "Aeacides's support for Olympias against Cassander brought him into conflict with Cassander — the Macedonian regent whose forces ultimately contributed to Aeacides's expulsion and death."},
      {"sourceSlug": "diadochi", "sourceName": "Wars of the Diadochi", "verb": "ENGULFS", "targetSlug": "aeacides-of-epirus", "targetName": "Aeacides of Epirus", "context": "The Diadochi succession crisis drew Aeacides into the Macedonian power struggles — illustrating how even small neighbouring kingdoms were inevitably sucked into the post-Alexandrian conflicts."}
    ],
    "places": [
      {"name": "Epirus (northwestern Greece / southern Albania)", "role": "Aeacides's kingdom — the mountainous region between Macedonia and the Ionian Sea whose Aeacid dynasty was his realm and whose people revolted against him"},
      {"name": "Macedonia", "role": "The focus of the Diadochi power struggles that drew Aeacides into fatal conflict — the kingdom whose succession crisis dominated Greek politics after Alexander's death"}
    ],
    "subjects": ["Hellenistic History", "Epirus", "Classical Era", "Ancient Greece", "Diadochi", "Ancient History", "Greek Kingdoms", "Classical Greece"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 5,
      "significanceNarrative": "Aeacides of Epirus was King of Epirus (c. 330–312 BCE), father of Pyrrhus of Epirus (antiquity's great general), and a significant figure in the Diadochi succession struggles following Alexander the Great's death. His support for Olympias against Cassander led to his expulsion and death, leaving young Pyrrhus in exile — an absence that shaped Pyrrhus's extraordinary subsequent career.",
      "significanceCategory": "local"
    }
  }
},

"magnus-felix-ennodius": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250magnus-felix-ennodius.json",
  "slug": "magnus-felix-ennodius",
  "data": {
    "summary": "Magnus Felix Ennodius (c. 473/474–521 CE) was a Gallic-born Latin poet, rhetorician, and bishop — Bishop of Pavia (Ticinum) from 514 CE until his death — one of the most significant Latin literary figures of the Ostrogothic kingdom of Italy and a major source for the intellectual culture of the late antique West. His literary output was extensive and diverse: panegyrics, epigrams, letters, hagiographic lives (including a vita of Epiphanius of Pavia, his predecessor), and most notably the 'Panegyricus dictus Theoderico' — a formal panegyric in praise of Theoderic the Great, the Ostrogothic king who ruled Italy from 493 to 526 CE.\n\nEnnodius is particularly important as a source for the intellectual culture of the Ostrogothic court — a court that attempted to maintain and patronise the Roman literary tradition under Germanic rulership, and whose cultural programme (associated with figures like Cassiodorus and Boethius as well as Ennodius) is one of the most fascinating examples of cultural transmission in late antiquity. Ennodius's panegyric of Theoderic (507 CE) is valuable both as a literary text and as a political document — an example of the rhetoric of legitimate kingship that Ennodius crafted for a Germanic ruler who sought Roman cultural legitimation.\n\nEnnodius also played a significant diplomatic role: he was sent twice (515 and 517 CE) to Constantinople on behalf of the papacy in the Acacian Schism negotiations — the dispute between Rome and Constantinople over the Monophysite controversy that had divided the churches since 484 CE. These diplomatic missions — the 'Legatio prima et secunda' — illustrated the role of senior Italian bishops as diplomatic intermediaries between the papacy and the Byzantine court in the politically complex world of the early 6th century. Despite his efforts, the schism was only resolved after his missions, in 519 CE.",
    "causes": [
      "The Ostrogothic kingdom's cultural programme — Theoderic the Great's attempt to govern Italy by maintaining Roman administrative and cultural traditions while accommodating Gothic military power — created the patronage environment in which Ennodius's literary career flourished.",
      "The Gallic-Roman literary tradition — the tradition of Latin rhetoric, poetry, and letter-writing that had been cultivated by the aristocracy of southern Gaul (Ausonius, Sidonius Apollinaris, Claudian) — provided the intellectual formation that Ennodius brought to his episcopal and literary career in Italy.",
      "The Acacian Schism (484–519 CE) — the dispute between Rome and Constantinople over Zeno's Henotikon and its accommodation of Monophysitism — created the diplomatic crisis that brought Ennodius to Constantinople as a papal legate and gave his career its most politically significant dimension."
    ],
    "effects": [
      "Ennodius's panegyric of Theoderic is one of the most important primary sources for the early Ostrogothic kingdom's cultural politics — his rhetorical construction of Theoderic as a legitimate heir to Roman imperial tradition contributed to the cultural programme by which the Ostrogoths sought Roman acceptance of their rule.",
      "Ennodius's vita of Epiphanius of Pavia — the 'Life of Bishop Epiphanius' — is one of the most important hagiographic texts of the late 5th century, providing vivid evidence for the role of Italian bishops as diplomatic negotiators in the period of the Germanic migrations.",
      "Ennodius's Latin literary output contributed to the survival and continuation of the classical Latin rhetorical tradition into the 6th century — his work, alongside that of Cassiodorus and Boethius, represents the final flowering of Roman Latin culture before the disruptions of the Gothic Wars (535–554 CE)."
    ],
    "relationships": [
      {"sourceSlug": "magnus-felix-ennodius", "sourceName": "Magnus Felix Ennodius", "verb": "SERVES", "targetSlug": "theoderic-the-great", "targetName": "Theoderic the Great", "context": "Ennodius composed the 'Panegyricus' (507 CE) praising Theoderic and served as a key cultural figure in the Ostrogothic court's programme of maintaining Roman literary traditions under Germanic rule."},
      {"sourceSlug": "magnus-felix-ennodius", "sourceName": "Magnus Felix Ennodius", "verb": "NEGOTIATES", "targetSlug": "acacian-schism", "targetName": "Acacian Schism (484–519 CE)", "context": "Ennodius was sent twice (515, 517 CE) to Constantinople as papal legate in the Acacian Schism negotiations — representing Rome's attempt to resolve the church division over Monophysitism."},
      {"sourceSlug": "ostrogothic-kingdom", "sourceName": "Ostrogothic Kingdom of Italy", "verb": "PATRONISES", "targetSlug": "magnus-felix-ennodius", "targetName": "Magnus Felix Ennodius", "context": "The Ostrogothic cultural programme — Theoderic's support for Roman literary traditions — provided the patronage environment within which Ennodius's literary career flourished."}
    ],
    "places": [
      {"name": "Pavia (Ticinum), Italy", "role": "Ennodius's episcopal see (514–521 CE) — the city in the Po valley that was an important administrative centre of the Ostrogothic kingdom"},
      {"name": "Constantinople", "role": "The destination of Ennodius's papal diplomatic missions (515, 517 CE) — the Byzantine capital where he negotiated over the Acacian Schism"}
    ],
    "subjects": ["Late Antique Literature", "Ostrogothic Kingdom", "Classical Era", "Italy", "Late Roman Church", "Latin Literature", "6th Century CE", "Patristics"],
    "frameworks": ["CULTURAL_TRANSMISSION", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Magnus Felix Ennodius was the bishop-poet of late antique Italy whose panegyric of Theoderic the Great (507 CE) is a key source for the Ostrogothic cultural programme, and whose papal diplomatic missions to Constantinople (515, 517 CE) illuminate the Acacian Schism. He represents the Gallic-Roman literary tradition's final flowering in the Ostrogothic court — alongside Cassiodorus and Boethius, a crucial figure of cultural transmission between antiquity and the Middle Ages.",
      "significanceCategory": "regional"
    }
  }
},

"paphnutius-of-thebes": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250paphnutius-of-thebes.json",
  "slug": "paphnutius-of-thebes",
  "data": {
    "summary": "Paphnutius of Thebes (c. 260–360 CE; died c. 360 CE) was an Egyptian bishop and confessor — Bishop of a diocese in the Thebaid (Upper Egypt) — who was one of the most venerated figures of the early desert monastic and confessorial tradition and an important participant in the Council of Nicaea (325 CE). He is described in ancient sources as having suffered under Diocletian's persecution (c. 303–312 CE): his right eye was gouged out and his left knee disabled — mutilations that made him a 'confessor' (one who confessed the faith under persecution without dying) of the highest status. When Constantine saw him at Nicaea, the emperor is reported to have kissed his mutilated eye socket in a gesture of veneration.\n\nPaphnutius is best known in church history for an intervention at the Council of Nicaea regarding clerical celibacy — though the historicity and interpretation of this episode is contested. According to the historian Socrates Scholasticus and others, when a proposal was made at Nicaea to require strict celibacy from all clergy (mandating that those already married must separate from their wives), Paphnutius rose and argued against compulsory clerical celibacy — proposing instead that those clergy already married before ordination should be allowed to remain with their wives, while those unmarried at ordination should remain celibate. This intervention, attributed to a celibate monk-bishop himself, is one of the earliest documented debates on clerical celibacy in church history, though the historical reliability of the account (found primarily in Socrates and Sozomen writing c. 150 years later) has been questioned.\n\nPaphnutius was a devoted disciple of Anthony the Great — the founder of Christian monasticism — and his career bridges the desert monastic tradition and the institutional episcopal church. He participated in the post-Nicene theological struggles and was associated with Athanasius of Alexandria in the Arian controversy.",
    "causes": [
      "The Diocletianic persecution (303–312 CE) — the last major Roman imperial persecution of Christianity — produced the confessor status that gave Paphnutius his exceptional prestige at Nicaea and in the early church, his physical mutilations serving as permanent badges of his faithfulness under torture.",
      "The Egyptian desert monastic movement — inspired by Anthony the Great, whose disciple Paphnutius was — created the specific spiritual tradition that formed Paphnutius's character and gave him the ascetic credibility that made his intervention at Nicaea on clerical celibacy particularly compelling.",
      "The Council of Nicaea (325 CE) — the first ecumenical council convened by Constantine to resolve the Arian controversy — brought together bishops from across the empire and created the forum in which Paphnutius's intervention on clerical celibacy (whether historical or legendary) was preserved in church tradition."
    ],
    "effects": [
      "The tradition of Paphnutius's intervention at Nicaea on clerical celibacy — whether historical or legendary — became an important reference point in subsequent debates about the clergy's marital status, particularly in the East-West discussions about mandatory celibacy.",
      "Paphnutius's association with Anthony the Great and his position at the intersection of the desert monastic tradition and the institutional episcopal church contributed to the growing influence of monasticism on episcopal culture in the 4th century Alexandrian church.",
      "The reported veneration of Paphnutius by Constantine — who kissed his mutilated eye socket — illustrates the extraordinary prestige of the confessors in the post-Constantinian church, and the symbolic significance of physical suffering for the faith as a marker of spiritual authority."
    ],
    "relationships": [
      {"sourceSlug": "paphnutius-of-thebes", "sourceName": "Paphnutius of Thebes", "verb": "DISCIPLE_OF", "targetSlug": "anthony-the-great", "targetName": "Anthony the Great", "context": "Paphnutius was a devoted disciple of Anthony the Great — the founder of Christian monasticism — and his episcopal career reflects the intersection of the desert monastic tradition and the institutional church."},
      {"sourceSlug": "council-of-nicaea", "sourceName": "Council of Nicaea (325 CE)", "verb": "FEATURES", "targetSlug": "paphnutius-of-thebes", "targetName": "Paphnutius of Thebes", "context": "Paphnutius participated in the Council of Nicaea (325 CE) — his intervention on clerical celibacy (attributed by Socrates Scholasticus) is one of the most discussed episodes of the council."},
      {"sourceSlug": "diocletianic-persecution", "sourceName": "Diocletianic Persecution (303–312 CE)", "verb": "SHAPES", "targetSlug": "paphnutius-of-thebes", "targetName": "Paphnutius of Thebes", "context": "Paphnutius's mutilation under Diocletian's persecution — his gouged eye and disabled knee — gave him confessor status and the extraordinary prestige that made Constantine venerate him at Nicaea."}
    ],
    "places": [
      {"name": "Thebaid (Upper Egypt)", "role": "The region of Paphnutius's diocese — the heartland of Egyptian Christian monasticism and the desert tradition associated with Anthony the Great"},
      {"name": "Nicaea (modern Iznik, Turkey)", "role": "The site of the First Council of Nicaea (325 CE) — where Paphnutius's intervention on clerical celibacy was (reportedly) made and where Constantine venerated him"}
    ],
    "subjects": ["Early Christianity", "Desert Monasticism", "Classical Era", "Egypt", "Church Councils", "4th Century CE", "Ancient Church", "Celibacy Controversy"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Paphnutius of Thebes was the Egyptian confessor-bishop who — mutilated under Diocletian's persecution — became one of the most venerated figures at the Council of Nicaea (325 CE), where Constantine reportedly kissed his empty eye socket. His traditional intervention on clerical celibacy became a major reference point in East-West debates on priestly marriage. A disciple of Anthony the Great, he bridges the desert monastic and episcopal traditions of 4th-century Egyptian Christianity.",
      "significanceCategory": "regional"
    }
  }
},

"titus-of-bostra": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250titus-of-bostra.json",
  "slug": "titus-of-bostra",
  "data": {
    "summary": "Titus of Bostra (died c. 378 CE) was Bishop of Bostra in the Roman province of Arabia (modern Busra al-Sham in southern Syria) — one of the significant anti-Manichaean theologians of the 4th century CE and the author of a major refutation of Manichaeism titled 'Contra Manichaeos' ('Against the Manichaeans'). His episcopal career falls in the reign of Julian the Apostate (361–363 CE), who reportedly required the bishops to refrain from proselytising their own congregations and who wrote letters to the people of Bostra (a pagan-majority city) criticising Titus for exciting the citizens against Julian's restoration of paganism.\n\nTitus of Bostra's 'Contra Manichaeos' — written in Greek and surviving substantially in the original as well as in a Syriac translation — is one of the most important early Christian refutations of Manichaean theology. Manichaeism (the dualistic religion founded by the Babylonian prophet Mani in the 3rd century CE) was one of the most significant religious competitors of early Christianity, offering an alternative universal religion that explained the problem of evil through a cosmic dualism of Light and Darkness. Titus's 'Contra Manichaeos' engaged Manichaean theology systematically — addressing its cosmology, its use of scriptural texts, and its ethical claims — and demonstrated a sophisticated knowledge of Manichaean teaching that made it a more effective refutation than many earlier Christian polemics.\n\nThe 'Contra Manichaeos' is also significant as a source for Manichaean beliefs themselves: like many heresiological texts, it preserves information about the teachings it refutes that might otherwise be lost. Titus's work was known to and used by later anti-Manichaean writers, and it contributed to the anti-Manichaean tradition that Augustine of Hippo would most famously continue in the late 4th–early 5th century.",
    "causes": [
      "The spread of Manichaeism into the eastern Roman Empire — particularly into the provinces of Syria, Arabia, and Egypt — created the theological challenge that prompted Titus to write the 'Contra Manichaeos', providing the immediate intellectual stimulus for his major surviving work.",
      "Bostra's position as the capital of the Roman province of Arabia — an important commercial and administrative centre on the major caravan route between Arabia and the Mediterranean — made it a meeting point of diverse religious traditions, including Manichaean communities, creating the local pastoral context for Titus's anti-Manichaean engagement.",
      "Julian the Apostate's religious policy (361–363 CE) — his attempt to restore traditional paganism and marginalise Christianity — created the political crisis that brought Titus into direct conflict with the emperor and illustrated the vulnerability of Christian bishops in the period of the Apostate's brief reign."
    ],
    "effects": [
      "Titus's 'Contra Manichaeos' became one of the standard references in the anti-Manichaean tradition — its systematic engagement with Manichaean theology influenced subsequent Christian refutations and contributed to the intellectual armoury of the growing anti-Manichaean polemic.",
      "The text's survival in Greek and Syriac preserves important evidence for Manichaean beliefs as they were understood in the Roman East in the mid-4th century — a valuable source for the history of Manichaeism that complements the direct Manichaean texts discovered in the 20th century.",
      "Julian the Apostate's letter to the people of Bostra criticising Titus — preserved in Julian's collected letters — provides one of the most vivid examples of the pagan emperor's anti-Christian policy and the specific mechanism (encouraging popular discontent) by which Julian sought to undermine episcopal authority."
    ],
    "relationships": [
      {"sourceSlug": "titus-of-bostra", "sourceName": "Titus of Bostra", "verb": "REFUTES", "targetSlug": "manichaeism", "targetName": "Manichaeism", "context": "Titus's 'Contra Manichaeos' was one of the most systematic 4th-century Christian refutations of Manichaean theology — engaging its cosmology, scriptural interpretation, and ethics in a scholarly polemic."},
      {"sourceSlug": "julian-the-apostate", "sourceName": "Julian the Apostate", "verb": "OPPOSES", "targetSlug": "titus-of-bostra", "targetName": "Titus of Bostra", "context": "Julian wrote letters to the people of Bostra criticising Titus for his treatment of pagans and pagan worship — one of the most direct examples of Julian's policy of marginalising Christian episcopal authority."},
      {"sourceSlug": "anti-manichaean-tradition", "sourceName": "Anti-Manichaean Christian Tradition", "verb": "INCLUDES", "targetSlug": "titus-of-bostra", "targetName": "Titus of Bostra", "context": "Titus's 'Contra Manichaeos' was a founding text of the anti-Manichaean tradition in Christian theology — influencing later refutations including those of Augustine of Hippo."}
    ],
    "places": [
      {"name": "Bostra (Busra al-Sham, southern Syria)", "role": "Titus's diocese — the capital of the Roman province of Arabia, an important caravan city where diverse religious traditions including Manichaeism were present"},
      {"name": "Province of Arabia, Eastern Roman Empire", "role": "The regional context of Titus's episcopate — a frontier province where Christianity, paganism, Judaism, and Manichaeism competed for adherents"}
    ],
    "subjects": ["Early Christianity", "Manichaeism", "Classical Era", "Syria", "Late Antique Theology", "4th Century CE", "Anti-Heretical Literature", "Church Fathers"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Titus of Bostra was the 4th-century Bishop of Bostra (Roman Arabia) whose 'Contra Manichaeos' was one of the most important systematic refutations of Manichaean theology in early Christian literature. His work contributed to the anti-Manichaean tradition that Augustine continued, and Julian the Apostate's letter criticising him is one of the most vivid examples of the pagan emperor's anti-Christian policy.",
      "significanceCategory": "regional"
    }
  }
},

"international-monetary-fund": {
  "filepath": "data/appwrite-export/entities/370-Class-370/370international-monetary-fund.json",
  "slug": "international-monetary-fund",
  "data": {
    "summary": "The International Monetary Fund (IMF) is an international organisation of 190 member countries established in 1944 at the Bretton Woods Conference — the landmark post-World War II financial summit in Bretton Woods, New Hampshire, that created the framework of the modern international monetary system. The IMF came into formal existence in December 1945 and began financial operations in 1947. Headquartered in Washington, D.C., the IMF's stated purpose is to foster global monetary cooperation, secure financial stability, facilitate international trade, promote high employment and sustainable economic growth, and reduce poverty around the world. It is one of the two major Bretton Woods institutions (along with the World Bank) that have shaped the global financial architecture since 1945.\n\nThe IMF operates as a lender of last resort for countries facing balance-of-payments crises — nations that cannot pay their international debts or maintain their currency's value in international markets. Member countries contribute quotas (proportional to their economic size) that form the Fund's lending resources. When a country requires IMF assistance, it negotiates a 'programme' — a package of loans conditional on economic reforms (known as 'conditionality') that the IMF deems necessary for financial stabilisation. The structural adjustment programmes that the IMF required of borrowing countries — particularly in the developing world during the 1980s and 1990s — typically included currency devaluation, fiscal austerity, trade liberalisation, and privatisation of state enterprises.\n\nThe IMF has been one of the most influential and contested institutions in modern international economics. Its advocates credit it with preventing financial contagion, managing debt crises, and promoting the market-oriented policies that underpinned the growth of the global economy. Its critics — from the left and the right — argue that IMF conditionality programmes have imposed unnecessary austerity on poor countries, undermined national sovereignty, and served the interests of creditor nations and international finance capital rather than the populations of debtor countries.",
    "causes": [
      "The interwar experience of competitive devaluations, trade wars, and financial instability (including the Great Depression's international dimension) demonstrated the need for an international institution to manage currency stability and balance-of-payments adjustment — the foundational lesson that motivated the Bretton Woods architects Keynes and White to design the IMF.",
      "The Bretton Woods Conference (July 1944) — convened by the Allied powers while WWII was still ongoing to plan the post-war international economic order — created the political and institutional framework within which the IMF was designed and agreed upon, reflecting the US and UK's determination to prevent the economic nationalism of the 1930s from recurring.",
      "The Cold War's geopolitical logic — in which the US sought to build a stable, open international economic order that would integrate non-communist nations and counter Soviet-bloc economic models — provided the political will to fund and sustain the IMF as a global financial institution."
    ],
    "effects": [
      "The IMF's management of successive currency crises and debt emergencies — from the Latin American debt crisis (1980s) through the Asian financial crisis (1997–1998) to the European sovereign debt crisis (2010–2015) — has made it the central institution of international financial crisis management, shaping the terms on which countries can access international credit.",
      "IMF structural adjustment programmes (SAPs) of the 1980s–1990s — requiring austerity, devaluation, and liberalisation as conditions for loans — had profound effects on the economies and social structures of dozens of developing countries in Africa, Latin America, and Asia, producing both economic stabilisation and severe social costs that remain subjects of intense debate.",
      "The IMF's regular surveillance of member economies — its 'Article IV consultations' and public reporting — has made it a major force shaping the terms of global economic policy discourse, as its assessments influence market perceptions, credit ratings, and the policy choices of member governments even absent lending programmes."
    ],
    "relationships": [
      {"sourceSlug": "international-monetary-fund", "sourceName": "International Monetary Fund", "verb": "EMERGES_FROM", "targetSlug": "bretton-woods-conference", "targetName": "Bretton Woods Conference (1944)", "context": "The IMF was created at the Bretton Woods Conference (1944) — the landmark post-WWII summit that designed the modern international monetary system, alongside the World Bank."},
      {"sourceSlug": "international-monetary-fund", "sourceName": "International Monetary Fund", "verb": "SHAPES", "targetSlug": "global-financial-system", "targetName": "Global Financial System", "context": "The IMF is a central institution of the global financial architecture — managing currency crises, providing conditional loans, and setting the terms of international financial stabilisation for its 190 member countries."},
      {"sourceSlug": "structural-adjustment", "sourceName": "Structural Adjustment Programmes", "verb": "IMPLEMENTS", "targetSlug": "international-monetary-fund", "targetName": "International Monetary Fund", "context": "IMF conditionality — the structural adjustment requirements attached to its loans — was the primary mechanism through which the IMF imposed market-oriented economic reforms on borrowing countries in the 1980s–2000s."}
    ],
    "places": [
      {"name": "Washington, D.C., USA", "role": "Headquarters of the IMF — the American capital whose location reflects the dominant role of the United States in the post-1945 international monetary system"},
      {"name": "Bretton Woods, New Hampshire, USA", "role": "Site of the 1944 conference that created the IMF — whose name is synonymous with the post-war international economic order that the Fund was designed to sustain"}
    ],
    "subjects": ["International Finance", "Global Institutions", "Modern Era", "Economics", "Cold War", "Modern History", "Bretton Woods", "Development Economics"],
    "frameworks": ["WORLD_SYSTEMS", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The International Monetary Fund is one of the foundational institutions of the modern global financial order — created at Bretton Woods (1944) to prevent the currency wars and financial instability of the 1930s from recurring. As the lender of last resort for sovereign debt crises and the primary enforcer of market-oriented conditionality, the IMF has shaped the economic policies of dozens of countries across the developing and developed world, making it one of the most influential (and contested) institutions of the post-WWII international order.",
      "significanceCategory": "world-changing"
    }
  }
},

"thorfinn-of-hamar": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250thorfinn-of-hamar.json",
  "slug": "thorfinn-of-hamar",
  "data": {
    "summary": "Thorfinn of Hamar (also Torfinn; died 8 January 1285) was Bishop of Hamar in Norway from approximately 1264 until his death in 1285 — a Norwegian medieval bishop known primarily for his defence of the rights and privileges of the Norwegian church against the encroachments of the Norwegian crown in the disputes over church-state relations that dominated Norwegian ecclesiastical politics in the late 13th century. His career falls in the period of the consolidation of the Norwegian medieval kingdom under Haakon IV Haakonsson and his successors — a period in which the Norwegian church was simultaneously strengthening its institutional independence (through the Concordat of Tønsberg, 1277) and facing royal resistance to clerical privileges.\n\nThorfinn of Hamar is best known in Norwegian church history for his role in the Sættargjerd (the Concordat of Tønsberg, 1277) — the agreement between the Norwegian church and King Magnus Lagabøte (Magnus the Law-Mender) that confirmed extensive ecclesiastical privileges including clerical exemption from royal courts, the church's right to its own legal system, and the free election of bishops. Thorfinn was among the bishops who negotiated and were parties to this concordat, which represented the high-water mark of Norwegian ecclesiastical independence and was modelled on the developments of canon law and church-state relations in Western Europe (particularly the English and Continental examples of clerical privilege following the Gregorian Reform).\n\nIn addition to his political significance, Thorfinn of Hamar is venerated locally as a saint — his holiness was attributed primarily to his ascetic life, his charitable work, and his defence of the poor against powerful interests. He died on pilgrimage to Rome in 1285, and his remains were subsequently venerated at Hamar. His local cult was never formally canonised but represents the pattern of episcopal holiness associated with the defence of ecclesiastical independence in the medieval Norwegian church.",
    "causes": [
      "The Gregorian Reform tradition and the broader 12th–13th century development of canon law and clerical privilege in Western Europe — which established the principle of clerical exemption from secular courts and episcopal independence from royal appointment — provided the theological and legal framework within which Thorfinn and the Norwegian bishops claimed their privileges.",
      "The consolidation of Norwegian royal power under the Haakon IV dynasty — and the Norwegian crown's assertion of administrative control over church appointments and revenues — created the church-state tensions that Thorfinn and his fellow bishops resisted, ultimately producing the Concordat of Tønsberg.",
      "The broader development of Norwegian ecclesiastical life in the 13th century — including the strengthening of the Nidaros archbishopric (founded 1152), the formalisation of Norwegian canon law, and the growing integration of Norway into the broader Latin church's legal culture — gave the Norwegian bishops the institutional resources to negotiate effectively with the crown."
    ],
    "effects": [
      "Thorfinn's participation in the Concordat of Tønsberg (Sættargjerd, 1277) contributed to the most significant formal affirmation of Norwegian ecclesiastical independence in the medieval period — an agreement that, though subsequently contested and eroded by the crown, established important precedents for Norwegian church-state relations.",
      "The veneration of Thorfinn as a local saint — associated with his pilgrimage death at Rome and his charitable reputation — contributed to the culture of episcopal holiness in medieval Norway, reinforcing the association between the defence of church rights and personal sanctity.",
      "Thorfinn's career illustrates the broader pattern of 13th-century European church-state conflict — the tension between growing royal administrative consolidation and the ecclesiastical privilege tradition of the Gregorian Reform that played out in different forms across England, France, the Empire, and Scandinavia."
    ],
    "relationships": [
      {"sourceSlug": "thorfinn-of-hamar", "sourceName": "Thorfinn of Hamar", "verb": "PARTICIPATES_IN", "targetSlug": "concordat-of-tonsberg", "targetName": "Concordat of Tønsberg (Sættargjerd, 1277)", "context": "Thorfinn was among the Norwegian bishops who negotiated and were parties to the Sættargjerd (1277) — the concordat with King Magnus Lagabøte that confirmed Norwegian ecclesiastical privileges."},
      {"sourceSlug": "gregorian-reform", "sourceName": "Gregorian Reform", "verb": "INSPIRES", "targetSlug": "thorfinn-of-hamar", "targetName": "Thorfinn of Hamar", "context": "The Gregorian Reform tradition of clerical privilege and episcopal independence provided the theological and legal framework for Thorfinn's defence of Norwegian church rights against royal encroachment."},
      {"sourceSlug": "medieval-norwegian-church", "sourceName": "Medieval Norwegian Church", "verb": "PRODUCES", "targetSlug": "thorfinn-of-hamar", "targetName": "Thorfinn of Hamar", "context": "Thorfinn was a product of the 13th-century Norwegian church's institutional strengthening — a bishop whose career exemplifies the growing confidence and legal sophistication of the Norwegian episcopate."}
    ],
    "places": [
      {"name": "Hamar, Norway", "role": "Thorfinn's diocese — the medieval Norwegian bishopric whose interests he represented in the Sættargjerd negotiations and whose people venerated him as a local saint"},
      {"name": "Rome, Papal States", "role": "The destination of Thorfinn's fatal pilgrimage — where he died in 1285, adding the pilgrimage death to the hagiographic elements of his cult"}
    ],
    "subjects": ["Medieval Church", "Norwegian History", "Classical Era", "Norway", "Medieval Church-State Relations", "Medieval History", "Scandinavia", "Medieval Saints"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 5,
      "significanceNarrative": "Thorfinn of Hamar was the 13th-century Norwegian bishop who participated in the Sættargjerd (Concordat of Tønsberg, 1277) — the high-water mark of Norwegian ecclesiastical independence. Venerated locally as a saint after his pilgrimage death in Rome (1285), his career exemplifies the 13th-century pattern of episcopal defence of Gregorian Reform privileges against royal consolidation across medieval Europe.",
      "significanceCategory": "local"
    }
  }
}

}  # end ENRICHMENTS


def get_entity(filepath, slug):
    with open(filepath) as f:
        data = json.load(f)
    for e in data.get("entities", []):
        if e.get("slug") == slug:
            return e, data
    return None, data

def apply_enrichment(filepath, slug, enrichment_data, dry_run=False):
    entity, data = get_entity(filepath, slug)
    if entity is None:
        print(f"  ERROR: slug '{slug}' not found in {filepath}")
        return False
    raw = entity.get("detailsJson", "{}")
    details = raw if isinstance(raw, dict) else json.loads(raw or "{}")
    old_len = len(details.get("summary", "") or "")
    if old_len >= 800:
        print(f"  SKIP — already enriched ({old_len}c)")
        return False
    if dry_run:
        print(f"  DRY RUN — would enrich {old_len}c → {len(enrichment_data.get('summary',''))}c")
        return True
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    for k, v in enrichment_data.items():
        details[k] = v
    edit_log = details.get("_editLog", [])
    edit_log.append({"field": "summary", "editorId": EDITOR_ID, "sessionId": SESSION_ID,
                     "timestamp": now, "oldValue": "", "newValue": enrichment_data.get("summary","")[:200] + "…"})
    details["_editLog"] = edit_log
    entity["detailsJson"] = details
    entity["_unsyncedEdits"] = True
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  ENRICHED — {old_len}c → {len(enrichment_data.get('summary',''))}c")
    return True

def main():
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("** DRY RUN **\n")
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    enriched = skipped = errors = 0
    for slug, spec in ENRICHMENTS.items():
        fp = os.path.join(repo_root, spec["filepath"])
        print(f"\n[{slug}]")
        if not os.path.exists(fp):
            print(f"  ERROR: not found: {fp}")
            errors += 1
            continue
        ok = apply_enrichment(fp, slug, spec["data"], dry_run=dry_run)
        if ok: enriched += 1
        else: skipped += 1
    print(f"\n{'='*60}\nRESULTS: {enriched} enriched, {skipped} skipped, {errors} errors")

if __name__ == "__main__":
    main()
