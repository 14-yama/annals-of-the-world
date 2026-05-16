#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 26 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: diary-of-anne-frank, eclogues, edda, babylonian-chronicles,
          bayeux-tapestry, a-christmas-carol, a-clockwork-orange, cypria
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-26-may2026"

ENRICHMENTS = {

"diary-of-anne-frank": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780diary-of-anne-frank.json",
  "slug": "diary-of-anne-frank",
  "data": {
    "summary": "The Diary of a Young Girl (Dutch: Het Achterhuis, 'The Secret Annex'), commonly known as The Diary of Anne Frank, is the personal diary of Annelies Marie Frank (1929–1945), a German-born Jewish girl who hid with her family in a concealed set of rooms (the Secret Annex, 'Achterhuis') in a warehouse at Prinsengracht 263 in Amsterdam from 6 July 1942 to 4 August 1944 — when they were discovered by the Gestapo and deported to Nazi concentration camps. Anne Frank wrote the diary between 12 June 1942 and 1 August 1944 in Dutch, initially in a red-and-white plaid autograph book, later in loose sheets; it was recovered from the Secret Annex after the arrest by Miep Gies (one of the helpers) and preserved. Anne died of typhus at Bergen-Belsen concentration camp in February or March 1945, weeks before the camp's liberation. Her father Otto Frank — the only member of the family to survive — had the diary published in 1947 as Het Achterhuis, translated into English in 1952, and subsequently into over 70 languages.\n\nThe Diary is one of the most widely read books in the world — over 35 million copies sold, translated into more than 70 languages — and the most widely read first-hand account of the Holocaust. Anne writes with remarkable intelligence, emotional depth, and literary self-awareness about life in hiding (the claustrophobia, the tensions, the fear, the daily routines), her developing inner life and intellectual ambitions, her first experience of love (with Peter van Pels), and her determined belief in human goodness despite the evidence around her — her famous last lines before arrest: 'I keep my ideals, because in spite of everything I still believe that people are really good at heart.' The combination of its intimate, personal voice, its historical testimony, and Anne's tragic fate have made the Diary one of the most powerful documents of the 20th century.\n\nThe Diary of Anne Frank has had enormous cultural impact — the Broadway play (1955, Pulitzer Prize) and film (1959) gave it a global audience; it has been a foundational text of Holocaust education in schools worldwide; and Anne Frank's face has become the most widely recognised symbol of the Holocaust's child victims — a humanising counterweight to the impersonal scale of six million deaths.",
    "causes": [
      "The Nazi occupation of the Netherlands (May 1940) and the progressive implementation of anti-Jewish measures — the requirement to wear the yellow star, the curfews, the deportations — created the conditions of terror that drove the Frank family and others into hiding in July 1942.",
      "Anne Frank's own literary ambitions and personality — she had kept diaries from her 13th birthday (June 1942) and after hearing a Dutch radio broadcast in March 1944 urging people to preserve diaries and letters as historical testimony, she began rewriting her diary entries with publication in mind, creating the literary self-consciousness that distinguishes it from a simple private diary.",
      "Otto Frank's decision after liberation to have the diary published — in the face of Anne's explicit wish that it be published one day — and his lifetime dedication to preserving her memory (he lived until 1980) were the immediate human causes of the diary's transformation from private manuscript to world classic."
    ],
    "effects": [
      "The Diary of Anne Frank became the central text of Holocaust education worldwide — used in schools across Europe, the United States, and Japan to humanise the Holocaust through individual testimony, it has introduced the history of the Holocaust to generations of schoolchildren who might otherwise have encountered it only through impersonal statistics.",
      "Anne Frank's Secret Annex at Prinsengracht 263, Amsterdam — preserved as the Anne Frank House museum (opened 1960) — has become one of the most visited museums in the Netherlands and one of the major sites of Holocaust memory in Europe, with over a million visitors annually.",
      "The Diary's global reach — 35 million copies, 70+ languages — and its cultural translations (the Broadway play, the films, the educational programmes) have made Anne Frank the most widely recognised individual victim of the Holocaust, her face and story serving as the primary humanising image of a genocide that can otherwise seem incomprehensibly large in scale."
    ],
    "relationships": [
      {"sourceSlug": "anne-frank", "sourceName": "Anne Frank (1929–1945)", "verb": "AUTHORS", "targetSlug": "diary-of-anne-frank", "targetName": "The Diary of Anne Frank (1942–1944)", "context": "Anne Frank wrote the diary in the Secret Annex in Amsterdam between June 1942 and August 1944, writing with increasing literary self-consciousness after hearing a radio broadcast urging people to preserve diaries as historical testimony."},
      {"sourceSlug": "diary-of-anne-frank", "sourceName": "The Diary of Anne Frank", "verb": "DOCUMENTS", "targetSlug": "the-holocaust", "targetName": "The Holocaust (Jewish persecution in occupied Netherlands)", "context": "The Diary is the most widely read first-hand account of the Holocaust — documenting the experience of Jewish life in hiding under Nazi occupation from a teenage girl's intimate perspective."},
      {"sourceSlug": "otto-frank", "sourceName": "Otto Frank (1889–1980)", "verb": "PRESERVES_AND_PUBLISHES", "targetSlug": "diary-of-anne-frank", "targetName": "The Diary of Anne Frank (1947 first publication)", "context": "Otto Frank — the only member of the Secret Annex group to survive — recovered the diary from Miep Gies and had it published in 1947, dedicating the rest of his life to preserving Anne's memory."}
    ],
    "places": [
      {"name": "Amsterdam, Netherlands — Secret Annex, Prinsengracht 263 (6 July 1942 – 4 August 1944)", "role": "The location of the diary's composition — the hidden rooms in which Anne Frank and seven others lived in hiding for over two years, now the Anne Frank House museum"},
      {"name": "Bergen-Belsen concentration camp (February/March 1945)", "role": "The site of Anne Frank's death from typhus — weeks before the camp's liberation by British forces in April 1945"}
    ],
    "subjects": ["Holocaust", "Modern Era", "World War II", "Netherlands", "Autobiography", "Jewish History", "20th Century", "Holocaust Education"],
    "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Diary of Anne Frank (1942–1944, published 1947) is the most widely read first-hand account of the Holocaust — 35 million copies in 70+ languages — and the defining humanising document of the genocide, making Anne Frank the most recognised individual victim of the Holocaust. As the central text of Holocaust education worldwide, it has introduced generations of schoolchildren to the history of the Holocaust through intimate personal testimony.",
      "significanceCategory": "world-changing"
    }
  }
},

"eclogues": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780eclogues.json",
  "slug": "eclogues",
  "data": {
    "summary": "The Eclogues (Latin: Eclogae, also known as the Bucolics or Bucolica) are a collection of ten pastoral poems by the Roman poet Virgil (Publius Vergilius Maro, 70–19 BCE), composed c. 42–39 BCE — the first major work of Virgil's career, and the foundational texts of the Western pastoral tradition from Theocritus through Renaissance poetry to the modern day. The Eclogues adapt and transform the Greek pastoral poetry of Theocritus (the Idylls, c. 270 BCE) into a Roman literary mode — the idealised shepherds of Arcadia (a mountainous region of Greece that Virgil transformed into a literary topos of perfect rural simplicity and beauty) speak of their loves, their sorrows, and the political upheavals of their world in highly polished Latin verse of extraordinary beauty. The famous 'Messianic Eclogue' (Eclogue IV) — with its prophecy of a coming child who will inaugurate a new golden age — was read in late antiquity and the Middle Ages as a pagan prophecy of the birth of Christ, giving Virgil a unique status as a poet whose inspired verse had foretold the Incarnation.\n\nVirgil wrote the Eclogues during one of the most violent periods of Roman history — the civil wars following the assassination of Julius Caesar (44 BCE), the land confiscations that dispossessed Italian farmers to settle veterans of the Triumvirs' armies, and the final conflict between Octavian and Mark Antony. The pastoral world of the Eclogues is haunted by these political realities — the beautiful Arcadian world is shadowed by the threat of exile, confiscation, and violence, making the Eclogues simultaneously an idealisation of pastoral beauty and a lament for its political vulnerability. Eclogue I — in which the shepherd Tityrus (often identified with Virgil) has been saved from land confiscation by the favour of a young man in Rome (identified as Octavian/Augustus), while his friend Meliboeus must go into exile — is a poem about the fragility of the pastoral world in the face of historical power.\n\nThe Eclogues' influence on Western literature is vast: they established the pastoral as a major literary mode (practised by Dante, Petrarch, Boccaccio, Spenser's Shepheardes Calender, Milton's Lycidas, Pope's pastorals); the imaginary 'Arcadia' became one of Western culture's defining topoi for idealised, innocent simplicity; and the Messianic Eclogue's central position in medieval and Renaissance Christian culture gave Virgil a unique theological prestige.",
    "causes": [
      "The political crisis of the Roman civil wars (44–31 BCE) — particularly the land confiscations by which the Triumvirs rewarded their veterans by dispossessing Italian farmers — provided both the political backdrop of the Eclogues (the threat to the pastoral world) and Virgil's personal motivation (his family farm near Mantua was among those confiscated, though later restored).",
      "Theocritus's Greek Idylls (c. 270 BCE) — the pioneering pastoral poems of the Hellenistic period, set among the shepherds of Sicily and Cos — provided the literary model that Virgil adapted and Romanised, transforming the Greek 'bucolic' tradition into the Latin 'pastoral' that would dominate Western European poetry for over a millennium.",
      "The patronage of Gaius Cilnius Maecenas — Octavian's literary adviser who brought Virgil into the literary circle that would later produce the Georgics and the Aeneid — gave Virgil both the political protection and the literary encouragement within which the Eclogues were composed and shaped for a politically sophisticated Roman audience."
    ],
    "effects": [
      "The Eclogues established the pastoral as a major literary genre in Western literature — the highly conventionalised mode of idealised rural poetry whose shepherds speak of love, loss, and artistic competition was practised by virtually every major poet from Dante and Petrarch through Spenser, Sidney, Shakespeare (As You Like It), Milton, and Pope.",
      "Virgil's 'Arcadia' — the imaginary perfect landscape of the Eclogues — became one of the defining topoi of Western art and literature: a symbol of innocent, peaceful simplicity outside the corruptions of civilisation, whose influence runs from Sannazaro's Arcadia (1504) through Poussin's paintings ('Et in Arcadia ego') to the modern pastoral tradition.",
      "The Messianic Eclogue's (Eclogue IV) remarkable prophecy of a coming age of peace and a miraculous child — interpreted by Constantine, Lactantius, and medieval tradition as a pagan prophecy of Christ — gave Virgil unique theological authority in medieval Christian culture, making him a guide figure for Dante in the Divine Comedy."
    ],
    "relationships": [
      {"sourceSlug": "virgil", "sourceName": "Virgil (70–19 BCE)", "verb": "AUTHORS", "targetSlug": "eclogues", "targetName": "Eclogues (c. 42–39 BCE)", "context": "Virgil wrote the Eclogues as his first major poetic work — an adaptation of Theocritean pastoral into Latin, composed during the violent years of the post-Caesarian civil wars."},
      {"sourceSlug": "eclogues", "sourceName": "Eclogues", "verb": "FOUNDS", "targetSlug": "pastoral-tradition", "targetName": "Western pastoral literary tradition", "context": "The Eclogues established the pastoral as a major Western literary genre — the highly conventionalised mode of idealised rural poetry practised by Dante, Petrarch, Spenser, Milton, and countless others."},
      {"sourceSlug": "eclogues", "sourceName": "Eclogues (Eclogue IV)", "verb": "INFLUENCES", "targetSlug": "dante-alighieri", "targetName": "Dante (Divine Comedy — Virgil as guide)", "context": "The Messianic Eclogue's interpretation as a pagan prophecy of Christ gave Virgil his unique theological authority in medieval Christian culture — the reason Dante chose Virgil as his guide through Hell and Purgatory in the Divine Comedy."}
    ],
    "places": [
      {"name": "Mantua and Rome, Italy (c. 42–39 BCE, composition)", "role": "The context of composition — Virgil writing in the Po Valley and at Rome during the violent years of the Triumviral land confiscations and civil wars"},
      {"name": "Arcadia (literary topos — Greece transformed into ideal pastoral landscape)", "role": "The imaginary setting of the Eclogues — Virgil's transformation of the Greek region of Arcadia into the Western pastoral tradition's defining literary landscape"}
    ],
    "subjects": ["Roman Literature", "Classical Era", "Ancient Rome", "Pastoral Poetry", "Latin Literature", "Virgil", "Poetry", "Western Literary Tradition"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Eclogues (Virgil, c. 42–39 BCE) founded the Western pastoral literary tradition — establishing the highly conventionalised mode of idealised rural poetry practised by Dante, Petrarch, Spenser, Milton, and countless others. The Messianic Eclogue's medieval interpretation as a prophecy of Christ gave Virgil unique theological authority in Christian culture, making him Dante's guide through Hell and Purgatory in the Divine Comedy.",
      "significanceCategory": "highly-significant"
    }
  }
},

"edda": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780edda.json",
  "slug": "edda",
  "data": {
    "summary": "The Eddas are two collections of Old Norse literature that together constitute the primary written sources for Norse mythology and the foundations of Germanic mythology more broadly — the Poetic Edda (also called the Elder Edda), an anonymous collection of Old Norse poems preserved in the Codex Regius manuscript (c. 1270 CE, but containing material believed to date from c. 800–1100 CE), and the Prose Edda (Snorra Edda), written c. 1220 CE by the Icelandic chieftain, historian, and poet Snorri Sturluson (1179–1241 CE) as a handbook of Norse mythology and a guide to traditional Skaldic poetry. Together they preserve the mythology of the Norse gods (Odin, Thor, Freya, Loki, Baldr) and the cosmology of the Nine Worlds, Yggdrasil, Ragnarök, and the creation and destruction of the universe that form the most elaborate body of pre-Christian Germanic mythological narrative to survive.\n\nThe Poetic Edda's poems include the Völuspá ('Prophecy of the Seeress') — the cosmological poem describing the creation and destruction of the world, from the primordial void through the current age of gods and men to the final battle of Ragnarök and the renewal of the world — and the Hávamál ('Sayings of the High One'), a collection of practical wisdom attributed to Odin that includes the account of Odin's sacrifice of himself on Yggdrasil to obtain the runes. The Prose Edda's Gylfaginning ('The Fooling of Gylfi') is a systematic account of Norse mythology from the creation through Ragnarök, told as a dialogue between a Swedish king and three mysterious figures who are revealed to be Odin in disguise.\n\nThe Eddas' cultural significance extends far beyond medieval Scandinavian studies — Richard Wagner's Ring cycle (Der Ring des Nibelungen, 1876) drew on both Edda traditions and the Nibelungenlied for its mythological framework; J.R.R. Tolkien's Middle-earth mythology (the Silmarillion, The Lord of the Rings) is profoundly indebted to Eddic cosmology and narrative; and the Norse mythology of the Eddas has shaped the global popular mythology of 'fantasy' narrative in ways that make it one of the most culturally productive bodies of mythological material in modern global culture.",
    "causes": [
      "The Christianisation of Scandinavia (10th–12th centuries) — which threatened to extinguish the pre-Christian Norse mythological tradition — created the urgent preservation context within which the Eddic poems were written down, with Snorri Sturluson consciously preserving mythological knowledge that was becoming culturally marginal in Christian Iceland.",
      "The Icelandic literary culture of the 12th–13th centuries — the 'Saga Age' of extraordinary Old Norse prose and poetry — provided the intellectual environment and the manuscript culture within which both the Poetic Edda (recorded in the Codex Regius, c. 1270) and Snorri's Prose Edda were compiled and preserved.",
      "Snorri Sturluson's practical purpose in writing the Prose Edda — as a handbook for Skaldic poets who needed to understand the mythological allusions (kennings) of the traditional poetic tradition — gave the Prose Edda its didactic form and ensured that it preserved mythological material in an accessible systematic form."
    ],
    "effects": [
      "The Eddas are the primary written sources for Norse mythology — without them, the cosmology of the Nine Worlds, the myths of Odin, Thor, Loki, and Baldr, and the narrative of Ragnarök would survive only in fragmentary form. Their preservation in 13th-century Iceland is the reason the Norse mythological tradition remains recoverable.",
      "Richard Wagner's Ring cycle (1876) — drawn primarily from the Eddas and the Nibelungenlied — brought Norse-Germanic mythology to the centre of European high culture, and through Wagner's influence on Romanticism, Tolkien, and fantasy mythology, the Eddas have shaped global popular culture far more than any other body of pre-Christian European mythology.",
      "J.R.R. Tolkien's Middle-earth — the most influential mythology of 20th-century popular culture — is profoundly indebted to Eddic cosmology: the Nine Worlds became Tolkien's cosmological framework, the Dwarves of the Hobbit are named from the Völuspá's dwarf catalogue, and the mythology of the Silmarillion reflects deep engagement with Eddic narrative patterns."
    ],
    "relationships": [
      {"sourceSlug": "snorri-sturluson", "sourceName": "Snorri Sturluson (1179–1241 CE)", "verb": "AUTHORS", "targetSlug": "edda", "targetName": "Prose Edda (c. 1220 CE)", "context": "Snorri Sturluson wrote the Prose Edda as a handbook of Norse mythology and Skaldic poetic technique — preserving systematic accounts of Norse cosmology and mythology in a Christianised Iceland where the tradition was becoming culturally marginal."},
      {"sourceSlug": "edda", "sourceName": "Poetic Edda / Prose Edda", "verb": "PRESERVES", "targetSlug": "norse-mythology", "targetName": "Norse mythology (Odin, Thor, Ragnarök)", "context": "The Eddas are the primary written sources for Norse mythology — without them, the cosmology of the Nine Worlds and the narrative of Ragnarök would survive only fragmentarily."},
      {"sourceSlug": "edda", "sourceName": "Eddas", "verb": "INFLUENCES", "targetSlug": "jrr-tolkien", "targetName": "J.R.R. Tolkien's Middle-earth mythology", "context": "Tolkien's Middle-earth mythology is profoundly indebted to Eddic cosmology — the Nine Worlds, the dwarf names from the Völuspá, and the mythological framework of the Silmarillion all reflect deep engagement with the Eddas."}
    ],
    "places": [
      {"name": "Iceland (13th century CE, manuscript compilation)", "role": "The place of preservation — Christian Iceland, where the Poetic Edda was recorded in the Codex Regius (c. 1270) and Snorri Sturluson wrote the Prose Edda, preserving a pre-Christian Norse tradition"},
      {"name": "Scandinavia and Germanic world (pre-Christian Norse culture, c. 800–1100 CE, oral origins)", "role": "The cultural origin of the Eddic material — the pre-Christian Norse world whose myths and cosmology the Eddas preserve"}
    ],
    "subjects": ["Norse Mythology", "Medieval Literature", "Medieval Era", "Old Norse", "Germanic Mythology", "Iceland", "Fantasy Literature", "Snorri Sturluson"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Eddas (Prose Edda c. 1220 CE; Poetic Edda recorded c. 1270 CE) are the primary written sources for Norse mythology — without them the cosmology of Odin, Thor, Ragnarök, and the Nine Worlds would survive only fragmentarily. Their influence on Wagner's Ring cycle, Tolkien's Middle-earth, and the global popular mythology of fantasy narrative makes them among the most culturally productive bodies of mythological material in modern global culture.",
      "significanceCategory": "world-changing"
    }
  }
},

"babylonian-chronicles": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781babylonian-chronicles.json",
  "slug": "babylonian-chronicles",
  "data": {
    "summary": "The Babylonian Chronicles are a series of cuneiform tablets recording the history of Babylonia and the ancient Near East from the 8th century BCE to the 1st century CE — the most important primary source for the political history of Mesopotamia during this period, recording year by year the major events of the reigns of Babylonian, Assyrian, Chaldean, and later Persian, Macedonian, Seleucid, and Parthian rulers: military campaigns, accession of kings, omens, eclipses, floods, and economic conditions. Excavated primarily from Babylon and Nippur and held in the British Museum and other institutions, they were written by scribes of the Esagila (the temple of Marduk in Babylon) and represent the official Babylonian record of historical events.\n\nThe Babylonian Chronicles' historical significance is immense — they contain the only contemporary written account of the fall of Nineveh (612 BCE), the decisive event that ended Assyrian power in the ancient Near East; they provide the closest contemporary evidence for the Fall of Jerusalem to Nebuchadnezzar II (597 BCE) and the deportation of the Judean population to Babylon (the Babylonian Captivity); they record the fall of Babylon to Cyrus the Great (539 BCE) in the 'Cyrus Chronicle'; and they are the only Babylonian source for the campaigns and deaths of several Seleucid and Parthian kings. The 'Chronicle of the Market Prices' and the astronomical diaries that overlap with the Chronicles provide unique economic and astronomical data for ancient Mesopotamia.\n\nThe Chronicles also provide the absolute chronological anchors for the chronology of the ancient Near East — astronomical observations (eclipses, planetary positions) recorded in the Chronicles and associated texts can be precisely dated by modern astronomical calculation, providing the fixed points from which the dates of ancient Near Eastern dynasties and events are calculated. Without the Babylonian Chronicles, our chronology of the ancient world would be considerably less precise.",
    "causes": [
      "The Babylonian scribal tradition — the cuneiform writing system and the institution of temple scribes at the Esagila in Babylon — provided the technical means and the institutional continuity for maintaining systematic annual records from the 8th century BCE through the Hellenistic and Parthian periods.",
      "The political interest of successive rulers in Babylonia — Babylonian, Assyrian, Chaldean, Persian, Macedonian, Seleucid, and Parthian — in maintaining the legitimacy conferred by Babylonian religious tradition (particularly the New Year ceremony and the touching of Bel-Marduk's hands) created the institutional continuity that sustained chronicle-writing through multiple regime changes.",
      "The Babylonian astronomical tradition — the systematic observation of celestial phenomena (eclipses, planetary positions, lunar cycles) conducted by temple astronomers — produced the astronomical diaries that are closely related to the Chronicles, providing both the astronomical data and the annalistic framework that shaped the Chronicles' structure."
    ],
    "effects": [
      "The Babylonian Chronicles provide the primary chronological framework for ancient Near Eastern history — the astronomical observations they record allow modern historians to calculate the precise dates of Babylonian, Assyrian, and Persian reigns, creating the absolute chronological anchors from which the dates of events throughout the ancient Near East are derived.",
      "The Chronicles' records of the fall of Nineveh (612 BCE), the fall of Jerusalem (597 BCE), and the fall of Babylon to Cyrus (539 BCE) provide the closest thing to contemporary external evidence for events that are also documented in the Hebrew Bible — allowing historians to correlate and calibrate the Biblical account with independent Babylonian evidence.",
      "The survival of the Babylonian Chronicles in the British Museum (excavated in the 19th century) and other collections — and their progressive decipherment and publication by Assyriologists in the 20th century — transformed the precision of ancient Near Eastern chronology and contributed to the broader project of correlating the histories of the ancient civilisations of the Mediterranean and Middle East."
    ],
    "relationships": [
      {"sourceSlug": "babylonian-chronicles", "sourceName": "Babylonian Chronicles", "verb": "DOCUMENTS", "targetSlug": "fall-of-nineveh", "targetName": "Fall of Nineveh (612 BCE)", "context": "The Babylonian Chronicles contain the only contemporary written account of the fall of Nineveh to the combined forces of Babylon and Media — the event that ended Assyrian hegemony in the ancient Near East."},
      {"sourceSlug": "babylonian-chronicles", "sourceName": "Babylonian Chronicles", "verb": "RECORDS", "targetSlug": "babylonian-captivity", "targetName": "Fall of Jerusalem and Babylonian Captivity (597 BCE)", "context": "The Chronicles record Nebuchadnezzar II's capture of Jerusalem and deportation of the Judean population — providing the closest external evidence for the Biblical Babylonian Captivity."},
      {"sourceSlug": "babylonian-chronicles", "sourceName": "Babylonian Chronicles", "verb": "DOCUMENTS", "targetSlug": "cyrus-the-great", "targetName": "Cyrus the Great's conquest of Babylon (539 BCE)", "context": "The 'Cyrus Chronicle' records the fall of Babylon to Cyrus the Great — a key event in ancient Near Eastern history corroborated by the Cyrus Cylinder and the Hebrew Bible."}
    ],
    "places": [
      {"name": "Babylon, Mesopotamia (8th century BCE – 1st century CE, compilation)", "role": "The location of the Esagila — the temple of Marduk where Babylonian scribes maintained the Chronicles — and the city whose history they primarily record"},
      {"name": "British Museum and other institutions (modern preservation)", "role": "The main repository of surviving Chronicle tablets — excavated from Babylon and Nippur in the 19th century and held primarily in the British Museum"}
    ],
    "subjects": ["Ancient Mesopotamia", "Classical Era", "Babylonia", "Cuneiform", "Historiography", "Ancient Near East", "Chronology", "Epigraphy"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Babylonian Chronicles (8th century BCE – 1st century CE) are the primary written source for the political history of Mesopotamia — recording the fall of Nineveh, the fall of Jerusalem, and the conquest by Cyrus, and providing the astronomical observations that create the absolute chronological anchors for the entire ancient Near Eastern chronological framework. Without them, our chronology of the ancient world would be considerably less precise.",
      "significanceCategory": "world-changing"
    }
  }
},

"bayeux-tapestry": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781bayeux-tapestry.json",
  "slug": "bayeux-tapestry",
  "data": {
    "summary": "The Bayeux Tapestry is a remarkable embroidered cloth of 70 metres (230 feet) in length and approximately 50 cm in width, depicting the events leading to the Norman Conquest of England in 1066 and culminating in the Battle of Hastings — created c. 1070–1080 CE, probably commissioned by Odo of Bayeux (William the Conqueror's half-brother and Bishop of Bayeux) and worked in wool on linen using the Opus Anglicanum (English embroidery) technique. It is the primary visual source for the Norman Conquest and one of the most extraordinary primary sources in medieval history — a sequential narrative told in 58 scenes with Latin captions, depicting Harold Godwinson's visit to Normandy, his oath to William, the English succession crisis, William's invasion preparations, the crossing of the Channel, and the Battle of Hastings culminating in Harold's death. It is currently displayed in Bayeux, Normandy, and is a UNESCO Memory of the World.\n\nThe Bayeux Tapestry is unique among medieval historical documents — its sequential pictorial narrative, resembling a graphic novel or a comic strip, combines imagery with brief Latin captions to tell the story of the Conquest from a perspective sympathetic to the Norman viewpoint (Harold's oath to William is presented as sacrilegious perjury, justifying William's invasion). Its detailed depictions of Norman and English arms, armour, ships, and military tactics make it the single most important visual source for the material culture of 11th-century northern Europe; and its famous image of Harold struck in the eye by an arrow at Hastings — traditional since at least the 12th century, though the identification of the figure with Harold is debated — is one of the most iconic images in English history.\n\nThe Tapestry survived the French Revolution intact (it had been used briefly to cover military wagons), and its extraordinary state of preservation — more than 900 years old — combined with its narrative richness and visual detail make it one of the most studied objects in medieval history. It was briefly shown to Napoleon in 1803 as part of his invasion preparations, and the French government's periodic consideration of lending it to England has been a diplomatic issue.",
    "causes": [
      "The Norman Conquest of England (1066) — William the Conqueror's victory at Hastings and the revolutionary transformation of English politics, culture, and language that followed — created the need for a commemorative and legitimising narrative of the events that gave William his kingdom, which the Tapestry's commission by Odo of Bayeux provided.",
      "Odo of Bayeux's role as the probable commissioner — William's powerful half-brother, Bishop of Bayeux and Earl of Kent, who had his own cathedral to furnish and political interests in legitimising the Conquest — gave the Tapestry its probable original display context (the nave of Bayeux Cathedral) and its Norman-sympathetic political viewpoint.",
      "The Opus Anglicanum tradition — the extraordinary English embroidery technique whose products were among the most prized luxury goods in medieval Europe — provided the technical expertise for the Tapestry's creation, suggesting it was made in England (probably Canterbury) by English embroiderers working under Norman direction."
    ],
    "effects": [
      "The Bayeux Tapestry is the primary visual source for the Norman Conquest and for the material culture of 11th-century northern Europe — its detailed depictions of Norman and English arms, armour, ships, cavalry tactics, and daily life are irreplaceable evidence for historians, archaeologists, and military historians of the period.",
      "The Tapestry's iconic imagery — Harold's oath to William, the Halley's Comet scene, and the death of Harold at Hastings — has shaped the visual imagination of English history since the 19th century, when it was first widely reproduced and studied, becoming one of the defining images of the Norman Conquest in popular historical consciousness.",
      "The Tapestry's survival provides a model of medieval narrative art that has influenced interpretations of medieval visual culture and the development of the graphic narrative tradition — its sequential pictorial storytelling technique has been compared to the modern comic strip and graphic novel."
    ],
    "relationships": [
      {"sourceSlug": "odo-of-bayeux", "sourceName": "Odo of Bayeux (c. 1036–1097)", "verb": "COMMISSIONS", "targetSlug": "bayeux-tapestry", "targetName": "Bayeux Tapestry (c. 1070–1080 CE)", "context": "Odo of Bayeux — William the Conqueror's half-brother — is the most likely commissioner of the Tapestry, probably for display in the nave of his Bayeux Cathedral."},
      {"sourceSlug": "bayeux-tapestry", "sourceName": "Bayeux Tapestry", "verb": "DOCUMENTS", "targetSlug": "battle-of-hastings", "targetName": "Battle of Hastings (14 October 1066)", "context": "The Tapestry's climactic scenes depict the Battle of Hastings — including the death of Harold Godwinson — making it the primary visual source for this decisive engagement."},
      {"sourceSlug": "bayeux-tapestry", "sourceName": "Bayeux Tapestry", "verb": "DEPICTS", "targetSlug": "william-the-conqueror", "targetName": "William the Conqueror (r. 1066–1087)", "context": "William is one of the central figures of the Tapestry's narrative — presented as the rightful claimant to the English throne whose invasion was justified by Harold's perjury."}
    ],
    "places": [
      {"name": "Canterbury, England (c. 1070–1080 CE, probable creation)", "role": "The probable place of the Tapestry's creation — English embroiderers of the Opus Anglicanum tradition, likely working in Canterbury under Norman direction"},
      {"name": "Bayeux, Normandy, France (current location, Bayeux Museum)", "role": "The probable original display location (Bayeux Cathedral) and current home of the Tapestry — displayed in the Musée de la Tapisserie de Bayeux"}
    ],
    "subjects": ["Norman Conquest", "Medieval History", "Medieval Era", "England", "Art History", "Epigraphy", "Military History", "11th Century"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Bayeux Tapestry (c. 1070–1080 CE) is the primary visual source for the Norman Conquest of England — its 70-metre sequential narrative of Harold's oath, William's invasion, and the Battle of Hastings provides irreplaceable visual evidence for the material culture, arms, and tactics of 11th-century northern Europe, and its iconic imagery has shaped the visual imagination of English history.",
      "significanceCategory": "highly-significant"
    }
  }
},

"a-christmas-carol": {
  "filepath": "data/appwrite-export/entities/783-Class-783/783a-christmas-carol.json",
  "slug": "a-christmas-carol",
  "data": {
    "summary": "A Christmas Carol in Prose, Being a Ghost Story of Christmas is the novella by Charles Dickens (1812–1870), published by Chapman & Hall on 19 December 1843 — one of the most widely read and culturally influential works of English literature, which single-handedly revived and transformed the English celebration of Christmas and created many of the popular traditions (the emphasis on family, generosity, and festive warmth) that define Christmas culture in the English-speaking world to this day. In five 'Staves', the miserly moneylender Ebenezer Scrooge is visited by the ghost of his dead business partner Jacob Marley and three Spirits (of Christmas Past, Present, and Yet to Come), who show him the poverty and joy of those around him, the happiness of his own past, and the bleak future that awaits him if he does not change — producing in Scrooge the complete moral transformation from cold-hearted miser to generous benefactor that has made his name a byword for both miserliness (Scrooge) and redemption.\n\nDickens wrote A Christmas Carol in six weeks in the autumn of 1843, in part driven by anger at a government report on child labour in factories (the Second Report of the Children's Employment Commission, 1842) — the Cratchit family and especially Tiny Tim (with his potentially fatal illness — almost certainly tuberculosis or rickets) represent the working poor of industrialising London whose condition Dickens sought to bring before middle-class readers. The novella's moral argument — that the wealthy have a direct social responsibility to the poor, and that Christmas is the proper occasion for the renewal of social bonds across class barriers — is a central expression of Victorian social reformism and of Dickens's lifelong campaign against poverty and inequality.\n\nA Christmas Carol's cultural influence has been extraordinary — it has never been out of print since 1843; it has been adapted into hundreds of stage, film, and television versions (including the celebrated 1951 film with Alastair Sim); and its language has entered popular culture ('Bah! Humbug!', 'God bless us, every one!'). Dickens himself gave public readings of the Carol that were among the most celebrated events of the Victorian literary world.",
    "causes": [
      "Dickens's social conscience and his rage at the conditions of the industrial working poor — specifically his reaction to the Second Report of the Children's Employment Commission (1842), which documented the exploitation of child labour in factories and mines — gave A Christmas Carol its reformist moral urgency and the specificity of the Cratchit family's poverty.",
      "The Victorian commercial crisis and cultural anxiety about Christmas — Christmas had declined as a public celebration in England in the early 19th century, and the revived 'Victorian Christmas' (the Christmas tree introduced by Prince Albert in 1840; the Christmas card invented in 1843) was taking shape precisely as Dickens wrote — giving A Christmas Carol both its cultural moment and its transformative role.",
      "Dickens's personal financial pressures in autumn 1843 — his previous novel Martin Chuzzlewit had sold poorly, his American trip had been expensive, and he needed a quick, commercially viable project — drove the six-week composition of the Carol and the decision to publish it as an illustrated gift book at a price accessible to a wide readership."
    ],
    "effects": [
      "A Christmas Carol transformed the English celebration of Christmas — its emphasis on family warmth, generosity to the poor, festive food and drink, and communal joy contributed to creating the 'Victorian Christmas' that became the dominant model of Anglo-American Christmas culture, superseding the more religious and less commercial traditions of earlier English Christmases.",
      "The character of Scrooge — the miser transformed by supernatural intervention into a generous benefactor — became one of the most familiar archetypes in English literature: 'a scrooge' entered the English language as a synonym for miser, and the Carol's narrative of moral redemption through confrontation with one's past and future became a template for countless subsequent stories.",
      "Dickens's public readings of A Christmas Carol (from 1853 and particularly in his reading tours of the 1860s) were among the most celebrated events of the Victorian literary world — his dramatic performance of Scrooge's transformation moved audiences to tears and laughter and contributed to the development of the literary reading tour as a form of popular cultural entertainment."
    ],
    "relationships": [
      {"sourceSlug": "charles-dickens", "sourceName": "Charles Dickens (1812–1870)", "verb": "AUTHORS", "targetSlug": "a-christmas-carol", "targetName": "A Christmas Carol (1843)", "context": "Dickens wrote A Christmas Carol in six weeks in autumn 1843 — driven by social anger at child labour and financial pressure, and publishing it as an illustrated gift book at Christmas."},
      {"sourceSlug": "a-christmas-carol", "sourceName": "A Christmas Carol", "verb": "TRANSFORMS", "targetSlug": "christmas-tradition", "targetName": "Victorian and Anglo-American Christmas tradition", "context": "A Christmas Carol's emphasis on family, generosity, and festive warmth contributed to creating the 'Victorian Christmas' that became the dominant model of Anglo-American Christmas culture."},
      {"sourceSlug": "a-christmas-carol", "sourceName": "A Christmas Carol", "verb": "RESPONDS_TO", "targetSlug": "industrial-revolution", "targetName": "Industrial poverty in Victorian England", "context": "The Cratchit family's poverty — and Scrooge's miserliness as a moral critique of laissez-faire capitalism — directly responds to the conditions of the industrial working poor that Dickens documented throughout his career."}
    ],
    "places": [
      {"name": "London, England (1843, composition and setting)", "role": "The context of composition and the setting of the novella — Victorian London, with its fog, poverty, and festive contrast between merchant wealth and working-class hardship"},
      {"name": "English-speaking world (global cultural influence)", "role": "The sphere of A Christmas Carol's cultural influence — shaping the Christmas traditions of Britain, the United States, Canada, Australia, and wherever English popular culture has spread"}
    ],
    "subjects": ["English Literature", "Modern Era", "Victorian Literature", "Social Reform", "Christmas", "Charles Dickens", "19th Century", "Cultural History"],
    "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "A Christmas Carol (Dickens, 1843) is one of the most culturally influential works of English literature — it transformed the English celebration of Christmas, creating many of the traditions (family warmth, generosity to the poor, festive communal joy) that define the Anglo-American Christmas to this day. Scrooge's moral redemption became one of English literature's most familiar archetypes, and the novella has never been out of print in 180 years.",
      "significanceCategory": "world-changing"
    }
  }
},

"a-clockwork-orange": {
  "filepath": "data/appwrite-export/entities/783-Class-783/783a-clockwork-orange.json",
  "slug": "a-clockwork-orange",
  "data": {
    "summary": "A Clockwork Orange is the dystopian novel by Anthony Burgess (1917–1993), published in 1962 — a compressed masterpiece of English dystopian fiction and one of the most linguistically innovative English novels of the 20th century, narrated in 'Nadsat', a youth slang invented by Burgess blending Cockney English, Russian, and Romany. The narrator-protagonist Alex DeLarge, a 15-year-old gang leader in a near-future authoritarian Britain, commits ultra-violence (rape, murder, robbery) with his 'droogs' (gang), is imprisoned, undergoes the Ludovico Technique (a fictional aversion therapy that conditions him to feel sick at the thought of violence), is released into a society that finds him useless without his free will, and ultimately — in Burgess's preferred 21-chapter version — chooses to grow out of violence. The novel's central philosophical argument is about free will: a human being who cannot choose evil is not fully human, and a state that removes the capacity for evil removes the capacity for good — the 'clockwork orange' of the title, a mechanical thing with the appearance of organic life.\n\nBurgess wrote A Clockwork Orange in three weeks in 1962, partly in response to a traumatic wartime experience (his wife was beaten and raped by four AWOL American soldiers in 1944, causing a miscarriage) and partly as a philosophical novel about free will, state power, and the definition of humanity. The American edition published in 1962 (and the Stanley Kubrick film of 1971, one of the most controversial and celebrated films in cinema history) omitted the 21st chapter in which Alex chooses to abandon violence — presenting a bleaker conclusion. Kubrick's film, with its ultra-stylised violence, classical music, and Nadsat narration, was banned in the UK (at Kubrick's own request) from 1973 to 1999 and became one of the most influential and imitated films in cinema history.\n\nA Clockwork Orange's cultural significance extends beyond its literary merit — its debate about free will and behaviour modification anticipated later controversies over aversion therapy, drug treatment of prisoners, and the ethics of state-sponsored rehabilitation; and its invented Nadsat language is one of the most remarkable achievements of linguistic worldbuilding in English fiction.",
    "causes": [
      "Burgess's personal traumatic experience — his wife's assault by AWOL American soldiers in 1944 and the consequent miscarriage — gave A Clockwork Orange its visceral immediacy and its philosophical seriousness, as Burgess processed both the reality of human violence and the question of how a civilised society should respond to it.",
      "The early 1960s British social context — the emergence of youth subcultures (Mods, Rockers, Teddy Boys) with their territorial gang violence, the anxiety about juvenile delinquency, and the early development of behaviour therapy as a treatment for criminal behaviour — gave A Clockwork Orange its immediate social context and its speculative extrapolation.",
      "The tradition of English dystopian fiction — Huxley's Brave New World (1932) and Orwell's Nineteen Eighty-Four (1949), both of which A Clockwork Orange engages — provided the literary framework within which Burgess's own dystopian vision of state-enforced pacification and the elimination of free choice could be situated."
    ],
    "effects": [
      "Stanley Kubrick's 1971 film adaptation — controversial for its stylised depiction of violence and its classical music score (Beethoven's Ninth Symphony) — became one of the most influential and imitated films in cinema history, shaping the visual language of dystopian cinema and the representation of ultra-violence, and was withdrawn from UK distribution for 27 years (1973–1999) at Kubrick's own request.",
      "A Clockwork Orange's philosophical argument about free will and behaviour modification anticipated real debates about aversion therapy, chemical castration of sex offenders, and drug treatment of violent prisoners — the Ludovico Technique's fictional ethics became a touchstone in bioethical discussions of state-coerced behaviour change.",
      "Nadsat — Burgess's invented youth slang blending Cockney, Russian, and Romany — is one of the most remarkable achievements of linguistic worldbuilding in English fiction, influencing the science fiction tradition of invented languages and demonstrating that a novel can use a partially opaque linguistic medium to immerse the reader in a character's perspective."
    ],
    "relationships": [
      {"sourceSlug": "anthony-burgess", "sourceName": "Anthony Burgess (1917–1993)", "verb": "AUTHORS", "targetSlug": "a-clockwork-orange", "targetName": "A Clockwork Orange (1962)", "context": "Burgess wrote A Clockwork Orange in three weeks in 1962 — a compressed philosophical novel about free will, state power, and the definition of humanity, driven by personal trauma and social anxiety."},
      {"sourceSlug": "a-clockwork-orange", "sourceName": "A Clockwork Orange", "verb": "ADAPTED_INTO", "targetSlug": "stanley-kubrick", "targetName": "Stanley Kubrick's film A Clockwork Orange (1971)", "context": "Kubrick's adaptation — one of the most controversial films in cinema history — used the American 20-chapter version, omitting Burgess's resolution, and was voluntarily withdrawn from UK distribution for 27 years."},
      {"sourceSlug": "a-clockwork-orange", "sourceName": "A Clockwork Orange", "verb": "INFLUENCED_BY", "targetSlug": "nineteen-eighty-four", "targetName": "George Orwell's Nineteen Eighty-Four (1949)", "context": "A Clockwork Orange engages with the Orwellian dystopian tradition — sharing the theme of state control of the individual and the suppression of natural impulses — while arguing, against Orwell's Big Brother, that the human soul can resist totalitarian conditioning through the persistence of free will."}
    ],
    "places": [
      {"name": "England (early 1960s setting and composition)", "role": "The near-future Britain of the novel — an extrapolation of early 1960s British youth gang culture into a dystopian authoritarian state"},
      {"name": "United Kingdom and United States (cultural impact, 1962–present)", "role": "The primary sphere of A Clockwork Orange's cultural reception — particularly after Kubrick's film brought it to global attention"}
    ],
    "subjects": ["English Literature", "Modern Era", "Dystopian Fiction", "Philosophy", "20th Century", "Film", "Free Will", "Youth Culture"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "A Clockwork Orange (Burgess, 1962) is a compressed masterpiece of English dystopian fiction — its philosophical argument about free will and state-coerced behaviour modification anticipated real bioethical controversies, and Kubrick's 1971 film adaptation became one of the most influential and controversial films in cinema history. Burgess's invented Nadsat language remains one of the most remarkable achievements of linguistic worldbuilding in English fiction.",
      "significanceCategory": "highly-significant"
    }
  }
},

"cypria": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782cypria.json",
  "slug": "cypria",
  "data": {
    "summary": "The Cypria (Greek: Κύπρια) is one of the lost epics of the ancient Greek Epic Cycle — the group of archaic Greek poems that collectively narrated the mythological history of the Trojan War, from the origins of the conflict through to the heroes' returns home. The Cypria covered the events leading up to the Trojan War proper — the wedding of Peleus and Thetis (at which the golden apple 'for the fairest' was thrown by Eris, the goddess of discord, beginning the chain of events culminating in the Trojan War), the Judgement of Paris (in which Paris chose Aphrodite over Hera and Athena, winning Helen), the abduction of Helen, the Greek expedition to Troy and its early campaigns — ending where Homer's Iliad begins (with the quarrel between Achilles and Agamemnon over Briseis). Attributed in antiquity to Stasinus of Cyprus (hence 'Cypria'), the poem is now lost, surviving only in a prose summary (diegesis) preserved by the 5th-century CE philosopher Proclus in his Chrestomathy, and in approximately 30 fragmentary quotations in later ancient writers.\n\nThe Cypria occupied a central position in the ancient Greek mythological imagination — together with the Iliad, the Aithiopis, the Little Iliad, the Iliou Persis, the Nostoi, and the Odyssey, it formed the narrative backbone of the Trojan War cycle that was among the most performed and referenced bodies of mythology in ancient Greek and Roman culture. Plato (Republic) objected to the Cypria's account of Zeus deliberately causing the Trojan War to reduce the burden of overpopulation on the earth — a divine utilitarian calculation that Plato found ethically unacceptable. Aristotle (Poetics) used the contrast between the Cypria (which, unlike Homer, told the whole Trojan War story) and the Iliad (which focused on a single episode) to illustrate the principle of unified action in tragedy.\n\nThe loss of the Cypria and other Epic Cycle poems is one of the most significant losses of ancient Greek literature — the existence of the summary in Proclus allows scholars to reconstruct the narratives, but the poems themselves (and the literary quality of their telling) are irretrievably gone. The Cypria's narrative content — the Judgement of Paris, the abduction of Helen, the sacrifice of Iphigenia — survived primarily through its influence on Athenian tragedy (Aeschylus's Oresteia begins with the fall of Troy; Euripides's Iphigenia in Aulis deals with the sacrifice) rather than through the poem itself.",
    "causes": [
      "The ancient Greek oral epic tradition — the tradition of hexameter poetry performed by bards (aoidoi) at aristocratic courts and public festivals — produced not only the Iliad and Odyssey but a larger Epic Cycle of poems covering the entire mythological history of the Trojan War, of which the Cypria was the opening episode covering the war's origins.",
      "The Greek mythological imagination's need to narrate the complete Trojan War — from its supernatural origins (the golden apple, the Judgement of Paris, Zeus's plan) through to the heroes' returns — created the Epic Cycle as a complementary body of narrative that filled in the mythological history before, between, and after the Iliad and Odyssey.",
      "The Athenian tragic tradition's engagement with the Trojan War cycle — Aeschylus, Sophocles, and Euripides all drew heavily on the Cypria's mythological content (particularly the sacrifice of Iphigenia, the abduction of Helen, and the divine machinery of the war's beginning) — gave the Cypria's narrative a second life in the canonical dramatic tradition."
    ],
    "effects": [
      "The Cypria's narrative content — the Judgement of Paris, the abduction of Helen, the assembly of the Greek fleet at Aulis, and the sacrifice of Iphigenia — was the primary mythological source for the most famous episodes of the Athenian tragic tradition: Euripides's Iphigenia in Aulis and Iphigenia among the Taurians, Aeschylus's Agamemnon, and the entire cycle of plays dealing with the events before the Iliad begins.",
      "Aristotle's use of the contrast between the Cypria (episodic narrative of the whole war) and the Iliad (unified action focused on Achilles's wrath) in the Poetics to illustrate the principle of unified action made the Cypria a foundational reference point in the theory of narrative — the negative example that clarified what Homer's genius consisted in.",
      "The loss of the Cypria (and of most of the Epic Cycle) represents one of the great lacunae of ancient Greek literature — its survival only in Proclus's summary has shaped all subsequent scholarship on the Trojan War mythology, making the reconstruction of the full Epic Cycle one of the enduring projects of classical philology."
    ],
    "relationships": [
      {"sourceSlug": "cypria", "sourceName": "Cypria (lost epic, attributed to Stasinus of Cyprus)", "verb": "PART_OF", "targetSlug": "epic-cycle", "targetName": "Greek Epic Cycle (archaic hexameter epic)", "context": "The Cypria is the opening poem of the Epic Cycle — the group of archaic Greek epics that collectively narrated the mythological history of the Trojan War before, during, and after the Iliad."},
      {"sourceSlug": "cypria", "sourceName": "Cypria", "verb": "PRECEDES", "targetSlug": "iliad", "targetName": "Homer's Iliad", "context": "The Cypria ended where the Iliad begins — with the quarrel between Achilles and Agamemnon over Briseis — making it the mythological prequel to the Iliad in the Epic Cycle's narrative sequence."},
      {"sourceSlug": "cypria", "sourceName": "Cypria (mythological content)", "verb": "SOURCES", "targetSlug": "euripides", "targetName": "Euripides's Iphigenia at Aulis and tragic tradition", "context": "The Cypria's account of the sacrifice of Iphigenia, the Judgement of Paris, and the abduction of Helen was the mythological source for several of the most celebrated Athenian tragedies, particularly Euripides's Iphigenia plays."}
    ],
    "places": [
      {"name": "Ancient Greece (archaic period, c. 7th–6th century BCE, probable composition)", "role": "The probable historical context of the Cypria's composition — the archaic period of Greek oral-derived hexameter epic, attributed to a poet from Cyprus"},
      {"name": "Alexandria and late antiquity (manuscript tradition, preservation in Proclus)", "role": "The context of the Cypria's survival — the Alexandrian scholars who collected and studied the Epic Cycle, and Proclus (5th century CE) whose prose summary is our primary source"}
    ],
    "subjects": ["Greek Literature", "Classical Era", "Ancient Greece", "Epic Poetry", "Mythology", "Trojan War", "Lost Texts", "Classical Philology"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "The Cypria (lost archaic Greek epic, c. 7th–6th century BCE) was the opening poem of the Epic Cycle — narrating the mythological origins of the Trojan War (the Judgement of Paris, the abduction of Helen, the sacrifice of Iphigenia) that were the primary source for Athenian tragedy. Its survival only in Proclus's summary represents one of the major lacunae of ancient Greek literature, and Aristotle's use of the Cypria in the Poetics made it foundational to the theory of narrative unity.",
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
