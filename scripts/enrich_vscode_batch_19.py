#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 19 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: procopius, map, neferka, arsinoe-i, gondulphus-of-metz,
          non, gospel-of-mark, nomus
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-19-may2026"

ENRICHMENTS = {

"procopius": {
  "filepath": "data/appwrite-export/entities/205-Class-205/205procopius.json",
  "slug": "procopius",
  "data": {
    "summary": "Procopius of Caesarea (Greek: Προκόπιος Καισαρεύς; c. 500–565 CE) was the most important historian of the 6th-century Byzantine Empire — the principal eyewitness chronicler of the reign of the Emperor Justinian I (527–565 CE) and the reconquest campaigns of the general Belisarius, whose staff officer Procopius served for many years. He is the essential source for understanding one of the most dramatic eras in Byzantine history: Justinian's attempt to reconquer the Western Roman Empire, the great plague of 541–549 CE, the religious controversies of the period, and the social and political life of Constantinople.\n\nProcopius wrote in three major works that together present a remarkably complex portrait of the age. His 'Wars' (Bella) in eight books provides a detailed military history of the Justinianic campaigns against the Persians, the Vandals in North Africa (534 CE), and the Ostrogoths in Italy (535–554 CE) — a narrative that, while officially celebratory, provides detailed and often critical accounts of military decisions and their consequences. His 'Buildings' (Peri ktismaton) is a panegyric account of Justinian's vast building programme, including the Hagia Sophia (completed 537 CE), presented as evidence of imperial greatness. But his most sensational work is the 'Secret History' (Anekdota) — a brutal, libellous, and often scabrous exposé of Justinian, the Empress Theodora, Belisarius, and his wife Antonina, written (apparently) for posthumous publication and revealing the bitter disillusionment of a court insider who had witnessed the gap between the official narrative and the reality of Byzantine court politics.\n\nProcopius's works are indispensable for 6th-century history, but they also pose complex interpretive challenges: how to reconcile the laudatory 'Buildings' with the vicious 'Secret History' written by the same author; how much of the 'Secret History's' scandalous material reflects historical fact versus personal animus; and how a single author could produce such radically different accounts of the same people and events.",
    "causes": [
      "Procopius's service as a legal secretary and advisor (assessor) to Belisarius — the greatest Byzantine general of the age — gave him a uniquely privileged eyewitness position at the heart of the major military campaigns of Justinian's reign, providing the first-hand observations that make the 'Wars' so valuable as a historical source.",
      "The extraordinary scope and ambition of Justinian's programme — the reconquest campaigns that temporarily recovered North Africa, Italy, and parts of Spain; the vast building programme including Hagia Sophia; the Corpus Juris Civilis (529 CE); and the religious controversies of the Three Chapters and the Monophysite dispute — created an era of exceptional historical significance that demanded chronicling.",
      "The culture of classical Greek historiography — the tradition of Thucydides and Herodotus that Procopius consciously modelled himself on — shaped his methodology: his claim to write as an eyewitness, his inclusion of speeches, his attention to causation, and his overall analytical approach all reflect his deep immersion in the classical historical tradition."
    ],
    "effects": [
      "Procopius's 'Wars' remains the primary narrative source for the Justinianic reconquest — without it, our knowledge of the campaigns against the Vandals, Ostrogoths, and Persians would be reduced to fragmentary archaeological and administrative evidence. It is irreplaceable for reconstructing the military and political history of the 6th-century Mediterranean.",
      "The 'Secret History's' exposure of court corruption and Theodora's alleged sexual past created an image of Justinian as a demon-emperor and Theodora as a licentious schemer that has profoundly influenced historical and popular perceptions of the Byzantine court — a negative image so compelling that it has shaped how Byzantine civilisation has been depicted even in modern popular culture.",
      "Procopius's account of the Plague of Justinian (541–549 CE) — the first detailed description of bubonic plague in Western literature — is an invaluable source for understanding the pandemic that may have killed 25–50 million people and contributed to the failure of Justinian's reconquest programme."
    ],
    "relationships": [
      {"sourceSlug": "procopius", "sourceName": "Procopius of Caesarea", "verb": "CHRONICLES", "targetSlug": "justinian-i", "targetName": "Justinian I (Emperor, 527–565 CE)", "context": "Procopius wrote three works about Justinian's reign — the laudatory 'Wars' and 'Buildings' and the savage 'Secret History' — which together make him the essential source for one of Byzantium's most consequential emperors."},
      {"sourceSlug": "procopius", "sourceName": "Procopius", "verb": "SERVES", "targetSlug": "belisarius", "targetName": "Belisarius (Byzantine general)", "context": "Procopius served as legal secretary and advisor to Belisarius — giving him direct eyewitness access to the major campaigns of Justinian's reign that he chronicled in the 'Wars'."},
      {"sourceSlug": "procopius", "sourceName": "Procopius", "verb": "RECORDS", "targetSlug": "plague-of-justinian", "targetName": "Plague of Justinian (541–549 CE)", "context": "Procopius provides the most detailed contemporary account of the Justinianic plague — the first pandemic description of bubonic plague that killed tens of millions across the Mediterranean world."}
    ],
    "places": [
      {"name": "Caesarea Maritima (modern Israel), Constantinople (Byzantine Empire)", "role": "Procopius's origin city and his base of activity — the Palestinian port city where he was born and Constantinople where he worked as a court official and historian"},
      {"name": "North Africa, Italy, Persia, Constantinople (Justinianic theatre)", "role": "The geographic range of his eyewitness observations — the battlefields and courts across which he accompanied Belisarius and from which he drew the material for the 'Wars'"}
    ],
    "subjects": ["Byzantine History", "Late Antiquity", "Classical Era", "Historiography", "Justinian Era", "Byzantine Literature", "6th Century CE", "Ancient History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Procopius of Caesarea (c. 500–565 CE) is the most important historian of the 6th-century Byzantine Empire — the primary eyewitness source for Justinian's reconquest campaigns, the construction of Hagia Sophia, and the Justinianic Plague. His three works — the 'Wars', 'Buildings', and scandalous 'Secret History' — together constitute the essential documentation of one of the most dramatic eras in Byzantine history and make him one of the indispensable historians of Late Antiquity.",
      "significanceCategory": "highly-significant"
    }
  }
},

"map": {
  "filepath": "data/appwrite-export/entities/173-Class-173/173map.json",
  "slug": "map",
  "data": {
    "summary": "A map is a symbolic, schematic representation of spatial information — a graphic depiction of selected features of a physical, social, or conceptual territory, using symbols, lines, colours, and scale conventions to communicate geographic, topographic, political, or thematic information about a portion of the world or of a conceptual space. Maps are one of the oldest forms of human graphic communication, with archaeological evidence for spatial representation going back to c. 25,000 BCE (cave paintings with territorial markings) and the earliest known geographic maps from ancient Mesopotamia (clay tablets, c. 2300 BCE) and ancient Egypt. They are fundamental tools of navigation, governance, military strategy, trade, and the organisation of human knowledge about the world.\n\nThe history of cartography — the art and science of map-making — spans the ancient world's geographical imagination (Ptolemy's 'Geographia', c. 150 CE, which systematised the mapping of the known world with latitude and longitude) through the Islamic golden age's refinements (al-Idrisi's world map, 1154 CE) to the revolutionary cartographic transformations of the Age of Discovery (the Portolan charts of the 13th–15th centuries; Waldseemüller's 1507 world map, the first to name 'America'; Mercator's projection, 1569, which made global navigation calculation possible) to the modern era of satellite cartography, GIS systems, and digital mapping. Each era's characteristic maps reflect its technical capabilities, geographic knowledge, political power structures, and conceptual assumptions about the world.\n\nBeyond geographic maps, the concept of mapping has extended into every domain of human knowledge: anatomical maps (the body as territory), genetic maps (the genome), weather maps, concept maps, social network maps, and the metaphorical use of 'mapping' as a cognitive and analytical tool. The map is not just a tool — it is a representation that constructs reality as much as it describes it, selecting, simplifying, and projecting a particular perspective that inevitably reflects the values, priorities, and power of its makers.",
    "causes": [
      "The universal human need to navigate, orient, and communicate spatial information — to share knowledge of where resources, dangers, routes, and boundaries lie — drove the independent development of map-making in multiple human cultures from the earliest prehistoric times.",
      "The rise of complex societies with states, territories, taxation, and large-scale trade networks — requiring systematic knowledge of political boundaries, routes, and resources across large areas — created the institutional demand for cartographic standardisation that produced the major geographic mapping traditions of the ancient world.",
      "The Age of Discovery (15th–17th centuries) — European maritime exploration of Africa, Asia, and the Americas — created the practical need for accurate sea charts and world maps that drove the most rapid cartographic innovation in history, producing the modern world map as a total representation of the entire globe."
    ],
    "effects": [
      "Mercator's projection (1569) — which distorts the relative size of landmasses to preserve angles, making it suitable for navigation — became the standard world map in Western cartography and embedded a particular visual representation of the world (with Europe at the centre, and high-latitude regions artificially enlarged) that shaped Western geographical imagination for centuries.",
      "The development of accurate geographic knowledge through cartography was essential to the European colonial project — the mapping of Africa, Asia, and the Americas preceded and facilitated colonisation, and the act of naming, bounding, and representing territories on maps was itself an exercise of the power to claim and possess them.",
      "Digital mapping — GPS navigation, satellite imagery, Google Maps, GIS systems — has transformed the relationship between humans and spatial knowledge, making accurate geographic information universally accessible, enabling real-time navigation, and creating new forms of spatial analysis that are fundamental to modern urban planning, logistics, environmental management, and military intelligence."
    ],
    "relationships": [
      {"sourceSlug": "map", "sourceName": "Map (Cartography)", "verb": "PRODUCED_BY", "targetSlug": "ptolemy", "targetName": "Ptolemy (Geographia, c. 150 CE)", "context": "Ptolemy's Geographia systematised the ancient world's geographic knowledge — its system of latitude, longitude, and map projection established the framework of scientific cartography that shaped mapping for 1500 years."},
      {"sourceSlug": "mercator", "sourceName": "Gerardus Mercator (1512–1594)", "verb": "CREATES", "targetSlug": "map", "targetName": "Mercator Projection World Map (1569)", "context": "Mercator's cylindrical projection map — preserving compass bearing angles — became the dominant Western world map and embedded a particular visual representation of the globe that shaped geographic imagination for centuries."},
      {"sourceSlug": "map", "sourceName": "Map", "verb": "ENABLES", "targetSlug": "age-of-discovery", "targetName": "European Age of Discovery (15th–17th centuries)", "context": "The Portolan sea charts and world maps of the 14th–16th centuries enabled European maritime exploration — cartographic knowledge was both a product of exploration and a tool that made further exploration possible."}
    ],
    "places": [
      {"name": "Global (universal)", "role": "Maps are universal tools present in every human culture — the geographic scope of cartographic representation is the entire world and beyond"},
      {"name": "Mesopotamia, Egypt, Greece, Islamic World, Europe (historical centres)", "role": "The successive centres of major cartographic innovation — from ancient Babylonian clay tablets through Ptolemy and al-Idrisi to Renaissance European cartography"}
    ],
    "subjects": ["Cartography", "Geography", "Classical Era", "Navigation", "Science", "History of Knowledge", "Exploration", "Technology"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "WORLD_SYSTEMS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "Maps are fundamental tools of human civilisation — present in every culture, essential to navigation, governance, military strategy, and trade, and one of the oldest forms of graphic communication. The history of cartography — from Ptolemy's Geographia to Mercator's projection to GPS digital mapping — reflects humanity's evolving knowledge of the world and its capacity to represent, navigate, and organise spatial reality. Maps construct as much as they describe, making cartography inseparable from the exercise of power.",
      "significanceCategory": "world-changing"
    }
  }
},

"neferka": {
  "filepath": "data/appwrite-export/entities/220-Class-220/220neferka.json",
  "slug": "neferka",
  "data": {
    "summary": "Neferka was an ancient Egyptian pharaoh of uncertain date and affiliation — likely a ruler of either the late Old Kingdom or the First Intermediate Period (c. 2200–2050 BCE), a turbulent era of political fragmentation and decentralisation following the collapse of the 6th Dynasty and the central power of the Old Kingdom. The name Neferka (Egyptian: 'Perfect is the Ka' or 'Beautiful is the Spirit') was borne by several individuals in ancient Egyptian history, and the identification of the pharaoh Neferka requires careful attention to the specific evidence available — primarily scarabs, seal impressions, and occasional mentions in later king lists.\n\nThe Old Kingdom's collapse (c. 2180 BCE) — triggered by a combination of climate change (severe drought and reduced Nile floods), administrative overreach, rising power of provincial governors (nomarchs), and possibly volcanic activity — created the First Intermediate Period (c. 2180–2055 BCE), a time of multiple competing kingdoms and local dynasties in both Upper and Lower Egypt before the Eleventh Dynasty's Mentuhotep II reunified Egypt. The historical record for rulers in this period is fragmentary and often contradictory, making precise chronology and even the identification of individual pharaohs uncertain.\n\nNeferka's place in Egyptian history — whether as a minor ruler of the late Old Kingdom, a local pharaoh of the First Intermediate Period, or a figure from another period entirely — illustrates the challenges historians and Egyptologists face in reconstructing the complete sequence of ancient Egyptian rulers. The Egyptian king lists (Turin Canon, Abydos King List, Saqqara King List) provide the framework for reconstructing this history, but they are incomplete, inconsistent with each other, and sometimes list figures who cannot yet be confirmed archaeologically.",
    "causes": [
      "The collapse of the Old Kingdom's centralised administration and the fragmentation of political authority into competing regional powers during the First Intermediate Period created the conditions in which minor pharaohs like Neferka could hold local power without achieving the pan-Egyptian sovereignty of the great Old Kingdom rulers.",
      "Climate change in the late 3rd millennium BCE — the 4.2 kiloyear event, a prolonged drought that reduced Nile flooding and agricultural productivity — is identified by many Egyptologists as a major contributing factor to the Old Kingdom's collapse, creating the political vacuum in which multiple competing rulers emerged.",
      "The tradition of royal titulary in ancient Egypt — the formal system of throne names and epithets that provided the ideological framework for pharaonic power — produced names like Neferka that were adopted by multiple rulers across different periods, creating the identification challenges that complicate modern historical reconstruction."
    ],
    "effects": [
      "The existence of rulers like Neferka in the fragmentary record of the First Intermediate Period demonstrates the depth of Egypt's political fragmentation after the Old Kingdom's collapse — periods during which as many as 70 kings may have reigned in rapid succession (as suggested by the Turin Canon) over limited territories.",
      "The archaeological and textual evidence for minor pharaohs like Neferka — primarily scarabs and seal impressions — reflects the disrupted administrative systems of the First Intermediate Period, when royal authority was fragmentary and the monumental building programme of the Old Kingdom had largely ceased.",
      "The eventual reunification of Egypt under Mentuhotep II (c. 2055 BCE) and the restoration of central authority — establishing the Middle Kingdom — was made possible by the progressive consolidation of power among competing regional rulers, of which figures like Neferka represent the fragmented starting point."
    ],
    "relationships": [
      {"sourceSlug": "neferka", "sourceName": "Neferka", "verb": "RULES_DURING", "targetSlug": "first-intermediate-period", "targetName": "First Intermediate Period (c. 2180–2055 BCE)", "context": "Neferka was likely a ruler of the fragmented First Intermediate Period — the era of political disintegration that followed the Old Kingdom's collapse and preceded the Middle Kingdom's reunification."},
      {"sourceSlug": "old-kingdom-collapse", "sourceName": "Old Kingdom Collapse (c. 2180 BCE)", "verb": "CREATES", "targetSlug": "neferka", "targetName": "Minor Pharaohs like Neferka", "context": "The collapse of Old Kingdom central authority created the political conditions — multiple competing local dynasties — in which figures like Neferka held pharaonic titles without pan-Egyptian sovereignty."},
      {"sourceSlug": "turin-canon", "sourceName": "Turin Canon (Egyptian King List)", "verb": "RECORDS", "targetSlug": "neferka", "targetName": "Neferka (among First Intermediate Period rulers)", "context": "The Turin Canon — the most complete ancient Egyptian king list — provides the primary textual framework for identifying First Intermediate Period rulers including figures like Neferka."}
    ],
    "places": [
      {"name": "Egypt (Upper and/or Lower)", "role": "The territory over which Neferka held pharaonic authority — likely a limited regional power in the fragmented political landscape of the First Intermediate Period"},
      {"name": "Nile Valley (ancient Egypt)", "role": "The geographic context of ancient Egyptian civilisation — the narrow strip of cultivated land along the Nile that supported the extraordinary civilisation within which all Egyptian pharaohs, major or minor, operated"}
    ],
    "subjects": ["Ancient Egypt", "Egyptian Pharaohs", "Classical Era", "First Intermediate Period", "Egyptology", "Ancient History", "Old Kingdom", "3rd Millennium BCE"],
    "frameworks": ["STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 2,
      "significanceNarrative": "Neferka was a minor ancient Egyptian pharaoh — likely of the First Intermediate Period (c. 2180–2055 BCE) — whose existence is known primarily from scarabs and seal impressions. His significance lies in representing the extraordinary political fragmentation of post-Old Kingdom Egypt, a period of multiple competing local dynasties that the ancient king lists enumerate but that archaeology can only partially reconstruct.",
      "significanceCategory": "local"
    }
  }
},

"arsinoe-i": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221arsinoe-i.json",
  "slug": "arsinoe-i",
  "data": {
    "summary": "Arsinoe I (Greek: Ἀρσινόη; c. 305–after 274 BCE) was the first wife of Ptolemy II Philadelphus, king of Ptolemaic Egypt (reigned 283–246 BCE), and the daughter of Lysimachus, king of Thrace — making her a princess of the post-Alexander Macedonian successor kingdoms (the Diadochi states). She was queen of Egypt until c. 274 BCE, when she was accused of conspiring against her husband and exiled to Coptos in Upper Egypt. After her exile, Ptolemy II married his own full sister, Arsinoe II — one of the most remarkable women of the Hellenistic world — in the incestuous royal marriage that shocked the Greek world but which the Ptolemies adopted from ancient Egyptian pharaonic tradition.\n\nArsinoe I's marriage to Ptolemy II had produced three children who would be significant figures in the subsequent Ptolemaic dynasty: the future Ptolemy III Euergetes (the third Ptolemaic king, who would rule 246–222 BCE), Lysimachus (named for his maternal grandfather), and Berenice (who married Antiochus II of the Seleucid Empire in the peace settlement that ended the Syrian War). Her displacement by Arsinoe II and her exile represent the brutal dynastic politics of the Ptolemaic court — a pattern of court intrigue, accusations of conspiracy, and the subordination of individual women to the strategic marriage policies of the dynasty that would characterise Ptolemaic history.\n\nArsinoe I's significance lies partly in her own position as a Diadochi-era royal figure and partly in her role as the mother of Ptolemy III and as the predecessor to the extraordinary Arsinoe II — whose deification after her death (c. 268 BCE) as the goddess Philadelphus established a pattern of royal female cult that would be developed by subsequent Ptolemaic queens.",
    "causes": [
      "The post-Alexander Macedonian practice of diplomatic marriages between the Diadochi (successor) kingdoms — using royal daughters as political instruments to cement alliances between competing dynasties — brought Arsinoe I to Egypt as the bride of Ptolemy II, sealing the connection between the Ptolemaic kingdom of Egypt and Lysimachus's Thracian kingdom.",
      "The complex and violent succession politics of the early Ptolemaic dynasty — in which multiple claimants competed for the throne and court factions plotted against each other — created the environment in which Arsinoe I could be accused of conspiracy and exiled, regardless of the actual truth of the charges.",
      "Ptolemy II's subsequent marriage to his sister Arsinoe II — a union justified ideologically by reference to the divine marriages of Osiris and Isis and the traditional Egyptian pharaonic practice — required the elimination (through exile rather than execution) of the first wife, making Arsinoe I's disgrace a political necessity for the new dynastic ideology."
    ],
    "effects": [
      "Arsinoe I's children — particularly Ptolemy III Euergetes — continued the Ptolemaic dynasty after Ptolemy II's death, making her the matrilineal ancestor of the third Ptolemaic king and the subsequent rulers of one of the most significant Hellenistic states.",
      "Her exile and replacement by Arsinoe II established a precedent for the powerful role of royal women in the Ptolemaic court — both as political victims of dynastic manoeuvring and (in Arsinoe II's case) as active political participants whose influence shaped royal policy.",
      "The contrast between Arsinoe I's exile and Arsinoe II's subsequent deification illustrates the extraordinary variability of royal women's fates in the Hellenistic world — the same political system that destroyed one queen elevated another to divine status."
    ],
    "relationships": [
      {"sourceSlug": "arsinoe-i", "sourceName": "Arsinoe I", "verb": "MARRIED_TO", "targetSlug": "ptolemy-ii-philadelphus", "targetName": "Ptolemy II Philadelphus", "context": "Arsinoe I was the first wife of Ptolemy II — the Ptolemaic king of Egypt — until her exile c. 274 BCE on charges of conspiracy and his subsequent marriage to his sister Arsinoe II."},
      {"sourceSlug": "arsinoe-i", "sourceName": "Arsinoe I", "verb": "MOTHER_OF", "targetSlug": "ptolemy-iii-euergetes", "targetName": "Ptolemy III Euergetes", "context": "Arsinoe I was the mother of Ptolemy III — the third Ptolemaic king — making her the matrilineal link in the dynasty's succession from Ptolemy II to Ptolemy III."},
      {"sourceSlug": "arsinoe-ii", "sourceName": "Arsinoe II (the deified queen)", "verb": "REPLACES", "targetSlug": "arsinoe-i", "targetName": "Arsinoe I (exiled queen)", "context": "Arsinoe II — sister of Ptolemy II — displaced Arsinoe I as queen of Egypt after the latter's exile, establishing the sibling-marriage practice that the Ptolemies would continue."}
    ],
    "places": [
      {"name": "Alexandria, Egypt (Ptolemaic court)", "role": "Arsinoe I's royal residence as queen — the Ptolemaic capital where she held court and raised her children before her exile to Upper Egypt"},
      {"name": "Coptos (Qift), Upper Egypt", "role": "Arsinoe I's place of exile — the city in Upper Egypt where she was sent after being accused of conspiracy against Ptolemy II"}
    ],
    "subjects": ["Hellenistic History", "Ancient Egypt", "Classical Era", "Ptolemaic Dynasty", "Ancient Women", "Greek History", "Macedonian Successors", "3rd Century BCE"],
    "frameworks": ["STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 4,
      "significanceNarrative": "Arsinoe I (c. 305–after 274 BCE) was the first wife of Ptolemy II Philadelphus and mother of Ptolemy III Euergetes — exiled c. 274 BCE when Ptolemy II married his sister Arsinoe II in the incestuous royal union that shocked the Greek world. Her story illustrates the brutal dynastic politics of the Ptolemaic court and the role of royal women as instruments and victims of Hellenistic diplomatic marriage strategy.",
      "significanceCategory": "regional"
    }
  }
},

"gondulphus-of-metz": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250gondulphus-of-metz.json",
  "slug": "gondulphus-of-metz",
  "data": {
    "summary": "Gondulphus of Metz (died 10 September 823 CE) was a bishop of Metz — one of the most ancient and prestigious episcopal sees in the Frankish Empire, located in the Lorraine region of what is now northeastern France — during the reign of the Emperor Louis the Pious (813–840 CE), the son and successor of Charlemagne. He is venerated as a saint in the Catholic Church, with his feast day observed on 10 September. Metz's bishopric had been among the most important in the Carolingian realm: it was the see from which the great bishop Chrodegang (742–766 CE) had issued his influential 'Rule of Canons' — the Regula Canonicorum that reformed cathedral chapters across the Frankish church — and Metz maintained its prestige as a liturgical and musical centre throughout the Carolingian period.\n\nGondulphus's episcopate falls in the reign of Louis the Pious — a period of Carolingian ecclesiastical reform, the continuing implementation of the Carolingian Renaissance's educational and liturgical programmes, and the beginning of the internal political tensions within the Carolingian dynasty (the revolts of Louis's sons, the civil war between the sons that would eventually partition the Carolingian Empire at Verdun in 843 CE). The Carolingian reform programme — which sought to standardise church organisation, liturgical practice, and clerical education across the Frankish realm — made the role of bishops like Gondulphus important as local agents of reform implementation.\n\nHis significance lies primarily in his position as a bishop of a major Carolingian see during the high point of Carolingian ecclesiastical culture, and his local veneration as a saint reflects the pattern of episcopal holiness that was recognised in the Frankish church — the combination of pastoral care, ecclesiastical administration, and personal piety that the Carolingian reform programme sought to promote in its bishops.",
    "causes": [
      "The Carolingian Reform programme — initiated by Charlemagne and continued under Louis the Pious — required bishops of major sees like Metz to implement standardised liturgical practices, educational reforms (cathedral schools), and canonical regulations, giving men like Gondulphus their historical significance as agents of this transformation.",
      "Metz's special prestige in the Carolingian church — rooted in Chrodegang's influential canonical reforms, its role as a centre of liturgical music (the Metz chant tradition), and its strategic location in the Lotharingian heartland of the Carolingian Empire — made the bishopric of Metz a prestigious appointment whose holders were important figures in Carolingian ecclesiastical politics.",
      "The Carolingian tradition of episcopal canonisation — the recognition of bishops who had served their sees with pastoral distinction as local saints — reflected the high value placed on episcopal holiness in Carolingian religious culture and the role of the bishop as spiritual father of his community."
    ],
    "effects": [
      "Gondulphus's tenure as bishop contributed to the continuity of Metz's role as a major ecclesiastical and cultural centre in the Carolingian Empire — maintaining the institutional infrastructure of the see's cathedral chapter, schools, and liturgical traditions through the turbulent later years of Louis the Pious's reign.",
      "His veneration as a saint provided the see of Metz with another figure in its rich hagiographic tradition — adding to the series of holy bishops whose cults expressed the continuous sacred character of one of the Frankish church's most prestigious episcopal sees.",
      "The Carolingian episcopal culture of which Gondulphus was a part — combining administrative reform with pastoral care and liturgical standardisation — was one of the most consequential institutional developments of medieval European history, creating the framework of the medieval church's relationship between secular and ecclesiastical authority."
    ],
    "relationships": [
      {"sourceSlug": "gondulphus-of-metz", "sourceName": "Gondulphus of Metz", "verb": "LEADS", "targetSlug": "diocese-of-metz", "targetName": "Diocese of Metz", "context": "Gondulphus served as Bishop of Metz — one of the most prestigious episcopal sees in the Carolingian Empire, whose reforms under Chrodegang had made it a model for the entire Frankish church."},
      {"sourceSlug": "louis-the-pious", "sourceName": "Louis the Pious (Emperor, 813–840 CE)", "verb": "CONTEXTUALISES", "targetSlug": "gondulphus-of-metz", "targetName": "Gondulphus of Metz", "context": "Gondulphus served as bishop during Louis the Pious's reign — the period of Carolingian ecclesiastical reform and the beginning of the dynastic tensions that would partition the Carolingian Empire."},
      {"sourceSlug": "chrodegang-of-metz", "sourceName": "Chrodegang of Metz (742–766 CE)", "verb": "PRECEDES", "targetSlug": "gondulphus-of-metz", "targetName": "Gondulphus of Metz", "context": "Chrodegang's canonical reforms had made Metz a model episcopal see — Gondulphus was one of his successors inheriting a see whose prestige and institutional traditions made it one of the Carolingian church's most important centres."}
    ],
    "places": [
      {"name": "Metz, Lorraine (Carolingian Empire, modern France)", "role": "Gondulphus's episcopal city — the prestigious Lorraine see that was one of the most important in the Carolingian church, known for its liturgical traditions and canonical reforms"},
      {"name": "Carolingian Empire (Lorraine heartland)", "role": "The broader political context — the Carolingian Empire at the height of its ecclesiastical reform programme under Louis the Pious"}
    ],
    "subjects": ["Carolingian History", "Medieval Church", "Classical Era", "Frankish History", "Saints", "Medieval History", "Lorraine", "9th Century CE"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 3,
      "significanceNarrative": "Gondulphus of Metz (died 823 CE) was a bishop of one of the most prestigious sees in the Carolingian Empire — serving at Metz during the reign of Louis the Pious, when Carolingian ecclesiastical reform was at its height. His local veneration as a saint reflects the high value placed on episcopal holiness in Carolingian religious culture and his contribution to the institutional continuity of the important Metz see.",
      "significanceCategory": "local"
    }
  }
},

"non": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250non.json",
  "slug": "non",
  "data": {
    "summary": "Non (also Nonna, Nonita; c. 5th century CE, died c. 600 CE) was a Welsh saint — venerated in both Wales and Brittany — who is traditionally identified as the mother of Saint David (Dewi Sant), the patron saint of Wales (c. 500–589 CE). Her feast day is observed on 3 March in the Catholic Church and in the Welsh and Breton traditions. She is one of the relatively rare female saints of the early Celtic Christian tradition who achieved widespread veneration — her cult centred in the southwest of Wales (Pembrokeshire), particularly at the chapel of St. Non's near St. David's, Pembrokeshire, which is associated with the site of David's birth.\n\nAccording to hagiographic tradition, Non was a nun who was raped by a local chieftain (in some versions identified as Sant, king of Ceredigion) and conceived David — whose birth was accompanied by miraculous signs including a great storm and a radiant light. After David's birth, Non is said to have adopted a life of religious penance and holiness, eventually travelling to Brittany (northwest France) where she established a religious community and died. The chapel at St. Non's Bay, with its holy well (traditionally the well that sprang at David's birth), remains a pilgrimage site.\n\nNon's story illustrates several characteristic features of early Celtic Christian hagiography: the association of sanctity with miraculous birth circumstances, the pattern of holy women in the early Welsh Christian tradition, the close connection between the Welsh and Breton churches (reflecting the historical migration of Celtic peoples from Britain to Armorica in the 5th–6th centuries), and the use of well-cult sites as foci of religious devotion in the Celtic Christian landscape.",
    "causes": [
      "The development of the Celtic Christian tradition in Wales in the 5th–6th centuries CE — a distinctive form of Christianity characterised by monastic communities, scholarly learning, peregrinatio, and a rich tradition of saint cults — created the religious context in which figures like Non became venerated as holy women.",
      "Non's identity as the mother of Saint David — the patron saint of Wales — was the primary driver of her own veneration: the holiness of the son reflected back on the mother, and her cult was in large part a devotional expression of the veneration of David himself and the sacred geography associated with his birth.",
      "The cultural and religious connections between Wales and Brittany — reflecting the migration of Celtic-speaking peoples from Britain to Armorica (Brittany) in the 5th–6th centuries — created the dual Welsh-Breton character of Non's cult, with her veneration in both regions reflecting these deep historical connections."
    ],
    "effects": [
      "Non's cult — particularly the chapel and holy well at St. Non's Bay near St. David's — contributed to the sacred geography of Pembrokeshire as a centre of Welsh Christian pilgrimage, with St. David's Cathedral and its associated sites constituting one of the most important pilgrimage destinations in medieval Wales.",
      "Non's story, as told in the 'Life of Saint David' (Rhigyfarch's Vita Davidis, c. 1090 CE), established the narrative of miraculous origins that framed the biography of Wales's patron saint — the holy mother whose own sanctity pre-figured and enabled her son's extraordinary vocation.",
      "Non's Breton veneration — her cult at the church of Dirinon in Brittany, where she is said to have died — reflects the broader pattern of cross-channel saint cults that connected the Celtic Christian communities of Wales, Brittany, Cornwall, and Ireland, demonstrating the significant cultural unity of the Atlantic Celtic world in the early medieval period."
    ],
    "relationships": [
      {"sourceSlug": "non", "sourceName": "Saint Non", "verb": "MOTHER_OF", "targetSlug": "saint-david", "targetName": "Saint David (Dewi Sant, patron saint of Wales)", "context": "Non's primary significance in hagiographic tradition is as the mother of Saint David — Wales's patron saint — whose miraculous birth was associated with Non's holiness."},
      {"sourceSlug": "welsh-christian-tradition", "sourceName": "Celtic Christian Tradition (Wales, 5th–6th century)", "verb": "PRODUCES", "targetSlug": "non", "targetName": "Saint Non", "context": "Non was a product of the early Welsh Celtic Christian tradition — a period of intense religious activity, monastic foundation, and saint-cult formation that shaped Welsh Christian identity for centuries."},
      {"sourceSlug": "non", "sourceName": "Saint Non", "verb": "VENERATED_IN", "targetSlug": "brittany", "targetName": "Brittany (Breton Christian tradition)", "context": "Non is venerated in both Wales and Brittany — reflecting the historical migrations of Celtic peoples from Britain to Armorica that created the deep connections between the Welsh and Breton churches."}
    ],
    "places": [
      {"name": "St. Non's Bay, Pembrokeshire, Wales", "role": "The primary site of Non's cult — the chapel and holy well near St. David's traditionally associated with the site of David's miraculous birth"},
      {"name": "Brittany (Armorica), France", "role": "The secondary site of Non's veneration — where she is said to have travelled and died, with her cult at Dirinon in Brittany reflecting the Celtic church's cross-channel connections"}
    ],
    "subjects": ["Celtic Christianity", "Welsh History", "Classical Era", "Saints", "Medieval Wales", "Female Saints", "Early Medieval History", "Brittany"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 4,
      "significanceNarrative": "Saint Non (c. 5th century–c. 600 CE) was a Welsh saint venerated as the mother of Saint David, patron saint of Wales — her cult at St. Non's Bay, Pembrokeshire, is one of the sacred sites associated with the birth of Wales's patron saint. Her dual Welsh-Breton veneration reflects the historical connections between the Celtic Christian communities of Britain and Brittany, and she represents the important tradition of female sanctity in the early Celtic church.",
      "significanceCategory": "regional"
    }
  }
},

"gospel-of-mark": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780gospel-of-mark.json",
  "slug": "gospel-of-mark",
  "data": {
    "summary": "The Gospel of Mark is the second book of the New Testament and is generally considered the earliest of the four canonical Gospels — composed probably c. 65–70 CE, likely in Rome or Syria, shortly before or during the First Jewish-Roman War (66–73 CE). It is the shortest of the four Gospels (16 chapters, approximately 11,000 words in Greek) and is characterised by its urgent, fast-paced narrative style — its characteristic Greek word euthys ('immediately') occurs about 40 times — and its focus on the actions and miracles of Jesus rather than on extended teaching discourses.\n\nScholarly consensus in modern New Testament studies holds that Mark was the first Gospel written (the 'Markan Priority' thesis, developed in the 19th century and now dominant) and that both Matthew and Luke used Mark as a primary source, incorporating approximately 90% of Mark's material while expanding it with additional teaching material (the Q source) and their own special traditions. This relationship — the 'Two-Source Hypothesis' — is the dominant solution to the 'Synoptic Problem' (the question of how the three synoptic Gospels relate to each other). Mark's priority makes it the foundation of the synoptic tradition and the earliest narrative we have of Jesus's life, ministry, death, and resurrection.\n\nThe Gospel of Mark opens with John the Baptist and Jesus's baptism (no birth narrative, unlike Matthew and Luke), presents Jesus's Galilean ministry of healing and exorcism, and culminates in the passion narrative — the account of Jesus's final week in Jerusalem, his arrest, trial, crucifixion, and resurrection — which takes up approximately one-third of the entire Gospel. Mark's portrayal of Jesus emphasises his humanity, emotional responses (anger, compassion, distress), and the disciples' failure to understand his mission ('Messianic Secret') — a more complex and ambiguous Christology than some later theological developments might suggest.",
    "causes": [
      "The death of the eyewitness generation — Peter (executed c. 64–68 CE), Paul (c. 64–68 CE), and James (62 CE) — and the urgency of preserving the oral traditions of Jesus's life and teaching before they were lost, combined with the crisis of the First Jewish-Roman War, likely motivated the composition of the first written Gospel.",
      "The developing early Christian community's need for a narrative account of Jesus's life that could serve as a basis for proclamation (kerygma), instruction of new converts, and liturgical use — a need that oral tradition alone could not fully meet in the growing and geographically dispersed churches of the 60s CE.",
      "The specific crisis of the Jewish-Roman War (66–73 CE) and its theological challenges — what did the destruction of the Temple (70 CE) mean for a Jewish messianic movement? — shaped the theological concerns of Mark's narrative, particularly its apocalyptic discourse (Mark 13) and its focus on suffering and the cross."
    ],
    "effects": [
      "Mark's Gospel as the first written narrative of Jesus created the genre of Gospel literature — providing the narrative template (ministry in Galilee → journey to Jerusalem → passion and resurrection) that Matthew and Luke followed and that John responded to in his very different theological Gospel.",
      "The Markan Priority — the scholarly consensus that Mark was the first Gospel and the source for Matthew and Luke — makes Mark the foundation of our earliest historical knowledge of Jesus, giving its particular portrait of Jesus (his humanity, the 'Messianic Secret', the disciples' misunderstanding) foundational importance for historical Jesus studies.",
      "Mark's passion narrative — the detailed account of Jesus's final week, arrest, trials before Pilate and the Sanhedrin, crucifixion, and resurrection — became the central liturgical text of Christian Holy Week observance and shaped the theological understanding of Jesus's death as redemptive that is central to Christian soteriology."
    ],
    "relationships": [
      {"sourceSlug": "gospel-of-mark", "sourceName": "Gospel of Mark", "verb": "SOURCES", "targetSlug": "gospel-of-matthew", "targetName": "Gospel of Matthew", "context": "Under the dominant Two-Source Hypothesis, Matthew used Mark as its primary narrative source — incorporating approximately 90% of Mark's material while adding the Sermon on the Mount and other teaching collections."},
      {"sourceSlug": "gospel-of-mark", "sourceName": "Gospel of Mark", "verb": "SOURCES", "targetSlug": "gospel-of-luke", "targetName": "Gospel of Luke", "context": "Luke also used Mark as a primary source — incorporating its narrative framework while adding the distinctive Lukan material including the nativity story and the Prodigal Son parable."},
      {"sourceSlug": "first-jewish-roman-war", "sourceName": "First Jewish-Roman War (66–73 CE)", "verb": "CONTEXTUALISES", "targetSlug": "gospel-of-mark", "targetName": "Gospel of Mark (c. 65–70 CE)", "context": "The crisis of the Jewish-Roman War — its threat to the eyewitness generation and the theological challenge of the Temple's destruction — likely provided the urgency that drove the composition of the first Gospel."}
    ],
    "places": [
      {"name": "Rome or Syria (probable composition site)", "role": "The likely place of Mark's composition — either the Roman church in the aftermath of Nero's persecution (64 CE) or a Syrian Christian community, both contexts in which the first Gospel literature emerged"},
      {"name": "Galilee and Jerusalem, Palestine (narrative setting)", "role": "The geographic setting of Mark's narrative — Jesus's Galilean ministry and the Jerusalem passion narrative that together constitute the Gospel's structure"}
    ],
    "subjects": ["Early Christianity", "New Testament", "Classical Era", "Biblical Studies", "Christian Texts", "Religious Literature", "1st Century CE", "Jesus"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Gospel of Mark (c. 65–70 CE) is the earliest of the four canonical Gospels — the first written narrative of Jesus's life, ministry, death, and resurrection, and the primary source from which both Matthew and Luke drew their accounts (Markan Priority). As the foundation of the synoptic Gospel tradition, Mark's portrait of Jesus is indispensable for historical Jesus studies and shaped the liturgical and theological heart of Christianity — the passion narrative — that has been central to Christian worship for two millennia.",
      "significanceCategory": "world-changing"
    }
  }
},

"nomus": {
  "filepath": "data/appwrite-export/entities/220-Class-220/220nomus.json",
  "slug": "nomus",
  "data": {
    "summary": "Nomus (died c. 450 CE) was a high-ranking official of the Eastern Roman (Byzantine) Empire — a powerful bureaucrat who served as magister officiorum (Master of Offices) and later held other senior positions at the court of the Emperor Theodosius II (reigned 408–450 CE) and possibly under Marcian (reigned 450–457 CE). The magister officiorum was one of the most powerful positions in the late Roman bureaucracy — controlling the imperial chancery, the scholae palatinae (palace guards), the cursus publicus (imperial postal system), and the frontier fortifications. Nomus was thus a man of extraordinary administrative influence in one of the most turbulent decades of the late Western and Eastern Roman empires.\n\nNomus's career spans the period of Attila the Hun's greatest threat to the Roman world: the massive Hunnic invasions of the Balkans (441–443 CE, 447–449 CE) that devastated Eastern Roman territory, forced huge tribute payments, and brought Roman ambassadors — including the historian Priscus, whose account of his visit to Attila's court is one of the most remarkable documents of late antiquity — to negotiate at the Hunnic court. Nomus himself was involved in the diplomatic management of the Hunnic crisis — he was part of the extensive Byzantine diplomatic apparatus that sought to manage Attila through tribute, gifts, and negotiation while the Eastern Empire lacked the military capacity to defeat him in the field.\n\nNomus also played a role in religious politics: the reign of Theodosius II was marked by the great Christological controversies of the Nestorian dispute and the Council of Ephesus (431 CE), and the court's religious policies significantly shaped his career context. He represents the class of powerful civilian bureaucrats who effectively ran the Eastern Roman state during the 5th century — men whose administrative competence was indispensable to an empire under constant military pressure.",
    "causes": [
      "The late Roman Empire's increasing reliance on civilian bureaucrats to manage the complexity of imperial administration — taxation, diplomacy, military logistics, and provincial governance — created the conditions in which a skilled administrator like Nomus could rise to the most powerful offices of state.",
      "The Hunnic threat under Attila — which dominated Eastern Roman foreign policy from the 440s onwards — created the urgent need for effective diplomatic management and tribute negotiation, bringing skilled officials like Nomus to the forefront of imperial strategy.",
      "The Eastern Roman Empire's relative survival compared to the Western Empire's collapse — enabled in part by its stronger economic base, more defensible geography, and more competent bureaucratic administration — was a systemic achievement to which efficient officials like Nomus contributed, making competent administration existentially important."
    ],
    "effects": [
      "Nomus's diplomatic management of the Hunnic crisis — as part of the Byzantine apparatus that negotiated with Attila and paid massive tribute — was part of the strategy that kept the Eastern Empire from the Western Empire's fate of political collapse, even if at enormous financial and territorial cost.",
      "The Byzantine bureaucratic tradition — the class of powerful, literate civil servants like Nomus who ran the empire's administration — was one of the most important institutional inheritances of the late Roman Empire, providing the administrative continuity that allowed Byzantium to survive and function for a millennium after Rome's fall.",
      "Nomus's career illustrates the extraordinary complexity of late Roman court politics — the intersection of military crisis, religious controversy, dynastic competition, and bureaucratic power that characterised the reign of Theodosius II and shaped the trajectory of the Eastern Empire into the 5th century."
    ],
    "relationships": [
      {"sourceSlug": "nomus", "sourceName": "Nomus", "verb": "SERVES", "targetSlug": "theodosius-ii", "targetName": "Theodosius II (Eastern Emperor, 408–450 CE)", "context": "Nomus was one of the most powerful bureaucrats at the court of Theodosius II — serving as magister officiorum and playing a key role in the diplomatic management of the Hunnic crisis."},
      {"sourceSlug": "attila-the-hun", "sourceName": "Attila the Hun", "verb": "CONFRONTS", "targetSlug": "nomus", "targetName": "Nomus (Byzantine diplomatic apparatus)", "context": "Nomus was part of the Byzantine diplomatic machinery that managed the Hunnic threat under Attila — negotiating tribute payments and attempting to manage the most dangerous external threat the Eastern Empire faced in the 5th century."},
      {"sourceSlug": "byzantine-bureaucracy", "sourceName": "Late Roman/Byzantine Civil Service", "verb": "EXEMPLIFIED_BY", "targetSlug": "nomus", "targetName": "Nomus (magister officiorum)", "context": "Nomus exemplifies the class of powerful civilian administrators who effectively ran the Eastern Roman state — the bureaucratic tradition that was one of Byzantium's most important institutional inheritances from the Roman Empire."}
    ],
    "places": [
      {"name": "Constantinople (Eastern Roman Empire)", "role": "The court and capital where Nomus served — the administrative centre of the Eastern Roman Empire from which he exercised his power as magister officiorum"},
      {"name": "Balkans/Danube frontier (Hunnic theatre)", "role": "The diplomatic and military context of much of Nomus's work — the Balkan frontier devastated by Hunnic invasions that he helped manage through diplomacy and tribute"}
    ],
    "subjects": ["Byzantine Empire", "Late Roman History", "Classical Era", "Late Antiquity", "Roman Administration", "Hunnic Wars", "5th Century CE", "Eastern Roman Empire"],
    "frameworks": ["STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 4,
      "significanceNarrative": "Nomus was a powerful Byzantine bureaucrat — serving as magister officiorum under Theodosius II and playing a role in the diplomatic management of the Hunnic threat under Attila. His career exemplifies the class of civilian administrators who effectively ran the Eastern Roman state in the 5th century and whose institutional competence was part of why the Eastern Empire survived when the Western Empire collapsed.",
      "significanceCategory": "regional"
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
