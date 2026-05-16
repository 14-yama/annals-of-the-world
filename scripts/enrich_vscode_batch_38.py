#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 38 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: homeric-hymns, homage-to-catalonia,
          cyropaedia-xenophon, epic-of-king-gesar,
          epic-of-manas, anne-of-green-gables,
          borjgali, ordinary-language-philosophy
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-38-may2026"

ENRICHMENTS = {

"homeric-hymns": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780homeric-hymns.json",
  "slug": "homeric-hymns",
  "data": {
    "summary": "The Homeric Hymns are a collection of 33 ancient Greek hymns in dactylic hexameter attributed in antiquity to Homer — though modern scholarship recognises them as the work of various anonymous poets composed over a wide span of time (7th–5th centuries BCE, with some possibly earlier and the Hymn to Hermes perhaps as late as the 6th century BCE). The Hymns are addressed to the major Greek deities — the great hymns to Demeter, Apollo, Hermes, and Aphrodite are the longest and most significant, while the shorter hymns to Dionysus, Ares, Athena, Poseidon, and others vary in length from a few lines to several hundred. The Hymns served as preludes (prooimia) to epic recitation — bards would perform a hymn to the appropriate deity before reciting an epic narrative, inviting divine favour — and they preserve some of the earliest surviving extended narratives of Greek mythology.\n\nThe Homeric Hymn to Demeter (7th century BCE, approximately 495 lines) is the primary literary source for the myth of Persephone's abduction by Hades and Demeter's search for her daughter — the aetiological myth of the Eleusinian Mysteries (the most important mystery cult of ancient Greece) and the Greek explanation of the seasons (Persephone's annual return from the underworld brings spring; her annual descent brings winter). The Hymn to Demeter's detailed description of the Eleusinian rites — the wandering of Demeter, her reception at Eleusis, the institution of the Mysteries — makes it the most important literary source for our knowledge of the Eleusinian cult.\n\nThe Homeric Hymn to Apollo (two sections traditionally distinguished as the 'Delian' and 'Pythian' hymns) narrates the birth of Apollo on Delos and his establishment of the Delphic Oracle — making it the primary literary source for the foundation mythology of the two most important Apolline sanctuaries in the Greek world. The Hymn to Hermes (the most literary and sophisticated of the hymns) narrates the infant Hermes' invention of the lyre, his theft of Apollo's cattle, and the reconciliation of the two gods — a comic epic narrative that demonstrates the range of archaic Greek poetic technique.",
    "causes": [
      "The ancient Greek tradition of hymnic performance — the practice of bards reciting hymns to deities as preludes to epic performance, inviting divine favour before the main recitation — created the practical context and generic framework for the Homeric Hymns: they are functional liturgical preludes as well as literary poems.",
      "The major Panhellenic religious sanctuaries — Delos (Apollo's birthplace), Delphi (the Delphic Oracle), Eleusis (the Eleusinian Mysteries) — were the primary occasions and audiences for the longer hymns: hymns celebrating the deity's birth, mythological achievements, and the foundation of the sanctuary were composed for performance at the major festivals of these sanctuaries.",
      "The archaic Greek epic tradition's formulaic compositional technique — the same hexameter tradition and formulaic language as Homer's Iliad and Odyssey — provided the formal toolkit from which the Homeric Hymns were composed: their attribution to Homer reflects both the ancient sense that they belonged to the same literary tradition and modern scholars' recognition of their shared formulaic language."
    ],
    "effects": [
      "The Homeric Hymn to Demeter is the primary literary source for the myth of Persephone and the Eleusinian Mysteries — it has been fundamental to modern scholarly understanding of the Eleusinian cult and to the comparative study of dying-and-rising deity myths, and it has had an important afterlife in feminist scholarship (as a myth of mother-daughter separation and female power) and in poetry (Tennyson, Swinburne, H.D., Anne Carson).",
      "The Homeric Hymns as a corpus have been central to the reconstruction of archaic Greek mythology and religion — they preserve narratives of divine mythology (the birth of Apollo, Hermes' invention of the lyre, the Rape of Persephone, the birth of Dionysus) that are not found in Hesiod or Homer and that would otherwise be lost from the earliest stratum of Greek literary tradition.",
      "The Homeric Hymns' literary influence extends through the entire Western poetic tradition — their influence on the lyric hymnic tradition (Pindar, Callimachus, the Augustan Roman poets) and on the Renaissance and Romantic hymnic tradition (Chapman, Shelley's 'Hymn to Intellectual Beauty', Keats's 'Ode to Psyche') demonstrates their foundational role in Western poetry's engagement with divine subject matter."
    ],
    "relationships": [
      {"sourceSlug": "homeric-hymns", "sourceName": "Homeric Hymns (33 hymns, 7th–5th century BCE)", "verb": "ATTRIBUTED_TO", "targetSlug": "homer", "targetName": "Homer (Iliad, Odyssey tradition)", "context": "The Homeric Hymns were attributed in antiquity to Homer — their composition in the same dactylic hexameter tradition and formulaic language as the Homeric epics led ancient readers to see them as Homer's work, though modern scholarship recognises multiple anonymous authors."},
      {"sourceSlug": "homeric-hymns", "sourceName": "Homeric Hymns (Hymn to Demeter, Eleusinian Mysteries)", "verb": "SOURCES", "targetSlug": "eleusinian-mysteries", "targetName": "Eleusinian Mysteries (most important Greek mystery cult)", "context": "The Homeric Hymn to Demeter is the primary literary source for the myth of Persephone's abduction and the institution of the Eleusinian Mysteries — providing the foundational narrative for the most important mystery cult of ancient Greece."},
      {"sourceSlug": "homeric-hymns", "sourceName": "Homeric Hymns (Hymn to Apollo, Delphic Oracle)", "verb": "NARRATES_FOUNDING_OF", "targetSlug": "delphic-oracle", "targetName": "Delphic Oracle (Pythia, sanctuary of Apollo)", "context": "The Homeric Hymn to Apollo narrates the birth of Apollo on Delos and his establishment of the Delphic Oracle — the primary literary source for the foundation mythology of the two most important Apolline sanctuaries in Greece."}
    ],
    "places": [
      {"name": "Delos, Delphi, Eleusis (primary sanctuaries, hymnic occasions)", "role": "The major Panhellenic sanctuaries — Delos (Apollo's birthplace), Delphi (the Delphic Oracle), Eleusis (the Mysteries) — were the primary occasions for the longer Homeric Hymns, composed for performance at the major festivals of these sanctuaries"},
      {"name": "Ancient Greece (7th–5th century BCE, widespread composition and performance)", "role": "The Homeric Hymns were composed over a wide span of time (7th–5th centuries BCE) and geographical range in the Greek world — representing the diffuse archaic Greek poetic tradition of hymnic performance at Panhellenic sanctuaries"}
    ],
    "subjects": ["Ancient Greek Literature", "Ancient Era", "Greek Religion", "Greek Mythology", "Hexameter", "Archaic Greece", "Mystery Cults", "Homeric Tradition"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Homeric Hymns (7th–5th century BCE) are the primary literary sources for some of the most important Greek myths — the Hymn to Demeter for the Eleusinian Mysteries, the Hymn to Apollo for the foundation of the Delphic Oracle, the Hymn to Hermes for the invention of the lyre. As the earliest surviving extended Greek mythological narratives outside Homer and Hesiod, they are foundational for the study of archaic Greek religion and literature.",
      "significanceCategory": "highly-significant"
    }
  }
},

"homage-to-catalonia": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780homage-to-catalonia.json",
  "slug": "homage-to-catalonia",
  "data": {
    "summary": "Homage to Catalonia is a personal account of George Orwell's (1903–1950) participation in the Spanish Civil War (1936–1939), published on 25 April 1938 by Secker & Warburg — Orwell's direct testimony of his experience fighting for the POUM (Partido Obrero de Unificación Marxista, a Trotskyist-aligned anti-Stalinist militia) in Catalonia and Aragon, and his witness to the suppression of the POUM by the Soviet-aligned Spanish Communist Party in the Barcelona May Days of May 1937. Orwell joined the POUM militia in December 1936 after arriving in Barcelona, served on the Aragon front (described with vivid particularity: the cold, the lice, the boredom, the occasional violence), was shot through the throat by a Fascist sniper in May 1937, narrowly survived, and then had to flee Spain when the POUM was declared illegal and its leaders arrested as 'Trotskyist fascists' on Soviet orders.\n\nHomage to Catalonia is Orwell's most direct personal narrative and his most politically significant non-fiction — it is the primary literary document of the Spanish Civil War's internal politics: the suppression of the revolutionary left by the Soviet-aligned Communist Party as part of Stalin's project of controlling the Spanish Republic's military and politics. Orwell's first-hand account of the May Days — the street fighting in Barcelona between the POUM/anarchists and the Communist-backed Republican police — and his analysis of the Soviet manipulation of the Spanish Republic's politics directly shaped his subsequent political writing: the experience of seeing a genuine revolutionary movement destroyed by Stalinist manipulation was the direct precursor to Animal Farm (1945) and Nineteen Eighty-Four (1949), both of which are informed by the betrayal of the Spanish Revolution.\n\nHomage to Catalonia sold only 700 copies before going out of print, but was republished posthumously in 1952 and has since been recognised as one of the finest works of political reporting and personal narrative in the English language — Lionel Trilling's introduction to the 1952 American edition established Orwell as a major political writer.",
    "causes": [
      "Orwell's commitment to democratic socialism — and his journey to Spain to fight against fascism — placed him in the POUM militia (the anti-Stalinist left) rather than the Communist-aligned International Brigades, giving him the direct experience of the Spanish Revolution's internal politics that became the subject of Homage to Catalonia.",
      "The Soviet Union's role in the Spanish Republic — the provision of Soviet military aid in exchange for political control, and the GPU's direction of the Spanish Communist Party's suppression of the POUM and anarchist left — created the political context for Orwell's experience: the May Days and the POUM's suppression were the events that transformed his understanding of Stalinist communism.",
      "Orwell's background as a journalist and essayist — his commitment to clear, honest prose as a political tool — shaped the narrative and analytical method of Homage to Catalonia: the combination of vivid personal testimony with political analysis reflects his conviction that honest reporting was a form of political resistance."
    ],
    "effects": [
      "Homage to Catalonia directly shaped the political vision that produced Animal Farm and Nineteen Eighty-Four — Orwell's experience of seeing a revolutionary movement destroyed by Stalinist manipulation, language corrupted into propaganda, and truth suppressed by political authority provided the experiential foundation for his two greatest political fictions.",
      "Homage to Catalonia contributed to the Western left's growing disillusionment with Stalinist communism in the late 1930s and 1940s — alongside Arthur Koestler's Darkness at Noon (1940), it provided a vivid personal account of the Soviet manipulation of international communism that challenged the pro-Soviet sympathies of much of the Western left.",
      "Homage to Catalonia established the literary genre of the politically engaged war memoir — combining personal narrative with political analysis in clear, immediate prose — that influenced subsequent war writing and political journalism, including the tradition of embedded reporting that characterises late 20th-century war journalism."
    ],
    "relationships": [
      {"sourceSlug": "george-orwell", "sourceName": "George Orwell (1903–1950)", "verb": "AUTHORS", "targetSlug": "homage-to-catalonia", "targetName": "Homage to Catalonia (1938)", "context": "Orwell published Homage to Catalonia in 1938 — his direct testimony of fighting for the POUM militia in the Spanish Civil War and witnessing the Soviet-backed suppression of the revolutionary left in the May Days of 1937."},
      {"sourceSlug": "homage-to-catalonia", "sourceName": "Homage to Catalonia (Spanish Revolution, Stalinist suppression)", "verb": "PRECEDES", "targetSlug": "animal-farm", "targetName": "Animal Farm (Orwell, 1945)", "context": "Orwell's experience of the Stalinist suppression of the Spanish Revolution in Homage to Catalonia directly shaped Animal Farm — the fable of revolutionary betrayal that became his most widely read work."},
      {"sourceSlug": "homage-to-catalonia", "sourceName": "Homage to Catalonia (POUM, May Days)", "verb": "DOCUMENTS", "targetSlug": "spanish-civil-war", "targetName": "Spanish Civil War (1936–1939)", "context": "Homage to Catalonia is the primary literary document of the Spanish Civil War's internal politics — Orwell's first-hand account of the May Days and the POUM's suppression provides the most vivid personal testimony of the Soviet manipulation of the Spanish Republic."}
    ],
    "places": [
      {"name": "Barcelona and Aragon, Spain (1936–1937, Orwell's experience)", "role": "Barcelona — the revolutionary centre of Catalonia and the site of the May Days — and the Aragon front are the primary settings of Homage to Catalonia: Orwell served on the Aragon front and witnessed the May Days street fighting in Barcelona"},
      {"name": "London (Secker & Warburg, publication 1938; limited initial reception)", "role": "Homage to Catalonia was published in London in 1938 by Secker & Warburg — selling only 700 copies before going out of print, before its posthumous republication (1952) established Orwell as a major political writer"}
    ],
    "subjects": ["Spanish Civil War", "Modern Era", "George Orwell", "Political Writing", "Anti-Stalinism", "War Memoir", "20th Century", "Socialism"],
    "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Homage to Catalonia (Orwell, 1938) is the primary literary document of the Spanish Civil War's internal politics — Orwell's direct testimony of the Soviet-backed suppression of the revolutionary left. Its experience directly shaped Animal Farm and Nineteen Eighty-Four. As a pioneering work of politically engaged personal narrative, it established the genre of the politically committed war memoir and contributed to the Western left's disillusionment with Stalinist communism.",
      "significanceCategory": "highly-significant"
    }
  }
},

"cyropaedia-xenophon": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781cyropaedia-xenophon.json",
  "slug": "cyropaedia-xenophon",
  "data": {
    "summary": "The Cyropaedia (Greek: Κύρου παιδεία, Kyrou paideia, 'Education of Cyrus') is a partly historical, partly fictional biographical work by the Athenian historian and soldier Xenophon (c. 430–354 BCE), probably composed c. 370 BCE — a narrative of the life and education of Cyrus the Great (c. 600–530 BCE), founder of the Achaemenid Persian Empire, structured as an example of the ideal ruler and the ideal education that produces him. The Cyropaedia is one of the founding texts of the literary genre of the 'mirror for princes' (speculum principis) — books of instruction for rulers — and of the biographical novel as a literary form: it blends historical narrative with invented dialogue, speeches, and episodes to create a didactic portrait of the ideal monarch.\n\nThe Cyropaedia's Cyrus is not primarily an ethnographic or historical reconstruction of the historical Cyrus — Xenophon freely invented details and episodes to serve his didactic purposes — but an idealised portrait of the philosopher-king who combines military genius, political wisdom, justice, moderation, and the ability to inspire loyalty and admiration in subjects, allies, and enemies alike. The work's central preoccupation — how does one become a great ruler? what qualities and education are required? — places it in the tradition of Greek philosophical inquiry into the ideal polity and the ideal statesman, and its portrait of Cyrus as a ruler who governs through persuasion and love rather than force anticipates later theories of benevolent monarchy.\n\nThe Cyropaedia was enormously influential in antiquity and the Renaissance — Caesar and Scipio Africanus reportedly carried it on campaign; Cicero praised it as a model of virtue; Machiavelli discussed it in The Prince (comparing his own 'realistic' prince unfavourably with Xenophon's ideal); and it was widely read by Renaissance humanists as a manual of statecraft, influencing the tradition of the 'mirror for princes' that includes Erasmus's Education of a Christian Prince and the debates over ideal rulership in the 16th century.",
    "causes": [
      "Xenophon's Socratic education — his discipleship to Socrates and his engagement with the Socratic tradition of philosophical inquiry into virtue, justice, and the ideal human life — provided the philosophical framework of the Cyropaedia: the work is as much a philosophical meditation on virtue and education as it is a historical biography.",
      "The Athenian political crisis of the late 5th and early 4th centuries BCE — the failure of Athenian democracy and the rise of oligarchy, tyranny, and Macedonian power — created the context for Xenophon's interest in alternative models of government: his portraits of the Spartan kings (in the Agesilaus), the Persian Cyrus, and the ideal ruler in the Cyropaedia reflect his disillusionment with Athenian democratic politics.",
      "The Greek tradition of eulogistic biography and the 'education of the prince' genre — the intellectual context of 4th-century BCE Greek thought about the ideal ruler and the education required to produce him — provided the literary and philosophical models from which the Cyropaedia was constructed."
    ],
    "effects": [
      "The Cyropaedia's influence on the 'mirror for princes' genre — the tradition of didactic books of instruction for rulers — was foundational: it established the portrait of the ideal ruler as a biographical narrative with didactic intent, influencing Machiavelli's discussion of the Cyropaedia in The Prince, Erasmus's Education of a Christian Prince, and the tradition of Renaissance humanist political thought.",
      "The Cyropaedia's influence on Roman military and political culture — Caesar and Scipio Africanus reportedly kept it by their sides on campaign, and Cicero praised it as a model of virtue — demonstrates its role in transmitting Greek ideals of the philosopher-ruler to the Roman tradition of virtuous leadership.",
      "The Cyropaedia's contribution to the biographical novel as a literary form — its blend of historical narrative with invented dialogue, speeches, and episodes in the service of a didactic portrait — anticipates the novel as a literary genre and was recognised by ancient and Renaissance readers as an important innovation in the presentation of historical material."
    ],
    "relationships": [
      {"sourceSlug": "xenophon", "sourceName": "Xenophon (c. 430–354 BCE)", "verb": "AUTHORS", "targetSlug": "cyropaedia-xenophon", "targetName": "Cyropaedia (c. 370 BCE)", "context": "Xenophon composed the Cyropaedia as a didactic biographical narrative of Cyrus the Great — a portrait of the ideal ruler that was enormously influential in antiquity and the Renaissance as a model of virtuous statecraft."},
      {"sourceSlug": "cyropaedia-xenophon", "sourceName": "Cyropaedia (mirror for princes genre)", "verb": "INFLUENCES", "targetSlug": "the-prince-machiavelli", "targetName": "The Prince (Machiavelli, 1532)", "context": "Machiavelli discussed the Cyropaedia in The Prince — comparing his realistic prince unfavourably with Xenophon's idealised Cyrus — demonstrating the Cyropaedia's foundational role in the Renaissance 'mirror for princes' tradition."},
      {"sourceSlug": "cyropaedia-xenophon", "sourceName": "Cyropaedia (ideal ruler, Persian Empire)", "verb": "PORTRAYS", "targetSlug": "cyrus-the-great", "targetName": "Cyrus the Great (c. 600–530 BCE, Achaemenid founder)", "context": "The Cyropaedia's portrait of Cyrus the Great as the ideal philosopher-ruler — governing through persuasion and love rather than force — established Cyrus as the archetypal model of the benevolent monarch in Western political thought."}
    ],
    "places": [
      {"name": "Athens and Scillus (Xenophon's composition context, c. 370 BCE)", "role": "Xenophon composed the Cyropaedia during his retirement at Scillus (near Olympia), following his exile from Athens — a period of literary productivity in which he produced his major works of history, biography, and political philosophy"},
      {"name": "Renaissance Europe (wide circulation, influence on humanist political thought)", "role": "The Cyropaedia circulated widely in Renaissance Europe — read by humanists, princes, and military commanders as a manual of statecraft — influencing the tradition of the 'mirror for princes' and the debate over ideal rulership"}
    ],
    "subjects": ["Ancient Greek Literature", "Ancient Era", "Xenophon", "Political Philosophy", "Biography", "Persian Empire", "Cyrus the Great", "Statecraft"],
    "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The Cyropaedia (Xenophon, c. 370 BCE) is one of the founding texts of the 'mirror for princes' genre — a didactic biographical narrative of Cyrus the Great as the ideal ruler that was enormously influential in antiquity (Caesar, Cicero) and the Renaissance (Machiavelli, Erasmus). Its blend of history, invented dialogue, and didactic purpose anticipates the biographical novel, and its portrait of the philosopher-ruler governing through persuasion shaped Western political thought.",
      "significanceCategory": "significant"
    }
  }
},

"epic-of-king-gesar": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782epic-of-king-gesar.json",
  "slug": "epic-of-king-gesar",
  "data": {
    "summary": "The Epic of King Gesar (Tibetan: གེ་སར་རྒྱལ་པོ་, Gesar Gyelpo; Mongolian: Гэсэрийн тууль, Geseriyn tuul; also Geser) is the world's longest surviving epic poem — with more than one million verses in its extended versions, far exceeding the combined length of Homer's Iliad and Odyssey — performed and transmitted across Tibet, Mongolia, and adjacent Himalayan and Central Asian cultures over a period of approximately a thousand years (from c. 10th–11th century CE to the present). The epic narrates the life of the divine hero-king Gesar of Ling — a supernatural warrior king sent by the divine realm to conquer the demons and enemies of the dharma, unite the land, and establish a golden age of peace and justice — and encompasses his miraculous birth, his trials and contests for kingship, his thirty-plus military campaigns against demon-kings and human enemies, and his eventual departure from the human world. The epic's core narrative combines Tibetan Buddhist cosmology (Gesar as an emanation of Padmasambhava or Avalokitesvara) with the steppe heroic tradition of the Tibetan and Mongolian worlds.\n\nThe Epic of King Gesar is a living oral tradition — performed by specialist bards (grung-mkhan in Tibetan) who claim to receive the epic through visionary experience and dreams rather than deliberate memorisation, a tradition of inspired recitation unique in world epic literature. Gesar bards may perform for days, reciting episodes spontaneously in a state of trance-like inspiration, and different regions have different versions of the epic — the Tibetan, Mongolian, Buriat, Kalmyk, and other versions all have distinctive narrative traditions. The oral tradition is still active: in Tibet, the Gesar bards continue to perform, and the epic has been partially written down in a standardised Tibetan edition running to more than 120 volumes.\n\nThe Epic of King Gesar was inscribed on UNESCO's Representative List of the Intangible Cultural Heritage of Humanity in 2009 (jointly by China). As both the longest epic in the world and the primary monument of Tibetan and Mongolian literary and cultural tradition, it is one of the most extraordinary achievements of oral epic literature in human history.",
    "causes": [
      "The religious and political conditions of the Tibetan world in the 10th–11th centuries CE — the fragmentation of the Tibetan empire, the spread of Tibetan Buddhism, and the struggle against the persistence of pre-Buddhist traditions — created the cultural and political context for the emergence of the Gesar epic: a narrative that fused Buddhist cosmology (Gesar as emanation of a bodhisattva) with the pre-Buddhist Tibetan tradition of heroic kingship.",
      "The Central Asian steppe culture of heroic epic — the tradition of mounted warrior heroes, shamanistic inspired performance, and the celebration of the divine hero-king who defeats enemies and establishes cosmic order — provided the narrative and performative tradition from which the Gesar epic crystallised, fusing with Tibetan Buddhist content to create the distinctive Tibetan-Buddhist-epic synthesis.",
      "The extraordinary longevity of the Gesar oral tradition — its preservation across a thousand years and multiple cultures (Tibetan, Mongolian, Buriat, Kalmyk) through the practice of inspired visionary performance by specialist bards — reflects the deep cultural resonance of the Gesar figure across the Himalayan and Central Asian worlds."
    ],
    "effects": [
      "The Epic of King Gesar's inscription on UNESCO's Intangible Cultural Heritage list (2009) and the Chinese government's systematic collection of Gesar performances (the standardised Tibetan edition of more than 120 volumes) have created an unprecedented documentary record of the world's longest oral epic — preserving the living tradition while also transforming it through documentation.",
      "The Gesar epic's function as the primary monument of Tibetan national and cultural identity — particularly in the context of Tibet's political situation within China since 1950 — has given it extraordinary cultural and political significance as a symbol of Tibetan cultural continuity and resistance.",
      "The comparative study of the Gesar epic alongside the Mongolian Epic of Jangar and the Kyrgyz Epic of Manas — the three great epics of the Mongolian/Central Asian world — has contributed substantially to the academic study of Central Asian oral epic traditions and to the Parry-Lord oral-formulaic theory's extension to non-European contexts."
    ],
    "relationships": [
      {"sourceSlug": "epic-of-king-gesar", "sourceName": "Epic of King Gesar (world's longest epic)", "verb": "EMBODIES", "targetSlug": "tibetan-cultural-identity", "targetName": "Tibetan and Mongolian cultural identity", "context": "The Gesar epic is the primary monument of Tibetan and Mongolian literary and cultural tradition — the world's longest oral epic, performed across a thousand years, is the central expression of Tibetan-Buddhist-Mongol cultural identity."},
      {"sourceSlug": "epic-of-king-gesar", "sourceName": "Epic of King Gesar (oral tradition, inspired bards)", "verb": "PART_OF", "targetSlug": "central-asian-oral-epic", "targetName": "Central Asian oral epic tradition (Manas, Jangar, Gesar)", "context": "The Gesar epic is one of the three great epics of the Mongolian/Central Asian world — alongside the Kyrgyz Epic of Manas and the Kalmyk Epic of Jangar — performed by inspired specialist bards across Tibet, Mongolia, and adjacent regions."},
      {"sourceSlug": "epic-of-king-gesar", "sourceName": "Epic of King Gesar (UNESCO, 2009)", "verb": "INSCRIBED_ON", "targetSlug": "unesco-intangible-heritage", "targetName": "UNESCO Intangible Cultural Heritage of Humanity", "context": "The Epic of King Gesar was inscribed on UNESCO's Intangible Cultural Heritage list in 2009, recognising it as an extraordinary achievement of living oral epic tradition and stimulating systematic documentation."}
    ],
    "places": [
      {"name": "Tibet, Qinghai, and Sichuan (primary Gesar homeland)", "role": "The Tibetan plateau — particularly the Ling region in eastern Tibet (Kham/Amdo) — is the homeland of the Gesar epic, where the oral tradition is most deeply rooted and where Gesar bards continue to perform"},
      {"name": "Mongolia, Buryatia, and Kalmykia (Mongolian world traditions)", "role": "The Gesar epic has distinctive Mongolian, Buriat, and Kalmyk versions — spread across the Mongolian world through cultural contact with Tibet — each with its own narrative traditions while sharing the core hero-king narrative"}
    ],
    "subjects": ["Tibetan Literature", "Medieval Era", "Oral Epic", "Tibetan Buddhism", "Mongolian Culture", "Central Asian Literature", "UNESCO Heritage", "World's Longest Epic"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "RELIGIOUS_INTERPRETATION"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Epic of King Gesar is the world's longest surviving epic poem — with more than one million verses in its extended versions — and the primary monument of Tibetan and Mongolian cultural tradition. Performed by inspired bards across a thousand years from Tibet to Mongolia, it is a UNESCO Intangible Cultural Heritage and one of the most extraordinary achievements of oral epic literature in human history. Its function as a symbol of Tibetan cultural identity gives it exceptional significance.",
      "significanceCategory": "world-changing"
    }
  }
},

"epic-of-manas": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782epic-of-manas.json",
  "slug": "epic-of-manas",
  "data": {
    "summary": "The Epic of Manas (Kyrgyz: Манас дастаны, Manas dastany) is the national epic of the Kyrgyz people — an enormous cycle of oral heroic poetry narrating the life and deeds of the legendary hero Manas, his son Semetei, and his grandson Seitek (the so-called 'Manas trilogy'), performed by specialist bards called Manaschi (singular: Manaschi). The Manas epic is one of the three great epics of the Mongolian/Central Asian world alongside the Tibetan/Mongolian Epic of King Gesar and the Kalmyk Epic of Jangar, and is of extraordinary length — in its extended versions it is estimated at over 500,000 lines (approximately twenty times the length of Homer's Iliad), though the performed versions by different Manaschi vary enormously in scope. The Manas epic was inscribed on UNESCO's Representative List of the Intangible Cultural Heritage of Humanity in 2013.\n\nThe Manas epic narrates the legendary history of the Kyrgyz people — their migration, their resistance against the Kalmyk (Oirat) invaders, their search for a homeland, and the deeds of the hero Manas as their supreme military and spiritual leader. The epic's core themes — the unity of the Kyrgyz tribes under a heroic leader, the struggle against enemies threatening the survival of the Kyrgyz nation, and the establishment of the Kyrgyz homeland — gave the epic its extraordinary resonance as the primary vehicle of Kyrgyz national identity, particularly after the Kyrgyz conquest by Russia (1855–1876) and during the Soviet period.\n\nThe Manaschi tradition — the specialist bards who memorise and perform the Manas epic — is one of the most distinctive features of Kyrgyz oral epic culture. The great 19th-century Manaschi Sagynbay Orozbakovev and Sayakbai Karalaev are considered the most important performers of the tradition, with Karalaev's version (c. 1920–1970) running to approximately 500,000 lines and constituting the most extensive documented version of the epic. The Manas epic was first written down and studied systematically by the Russian explorer-scholar Wilhelm Radloff in 1869, who published extensive excerpts in his work on the Turkic oral tradition.",
    "causes": [
      "The nomadic warrior culture of the Kyrgyz people — their tradition of mounted warfare, tribal confederation, and heroic leadership — provided the cultural substrate from which the Manas epic crystallised over centuries of oral transmission, celebrating the values of courage, loyalty, and collective resistance to external enemies that defined Kyrgyz political culture.",
      "The Kyrgyz historical experience of the Kalmyk (Oirat) invasions and subsequent conflicts — which threatened the survival of the Kyrgyz as a distinct people in the 17th–18th centuries — provided the historical context for the epic's core narrative of Manas as the leader who unites the Kyrgyz tribes against the Kalmyk enemies, making the epic a vehicle of national memory and collective identity.",
      "The Kyrgyz experience of Russian conquest and Soviet rule — which created the political context for the Manas epic's function as a vehicle of Kyrgyz national identity and cultural resistance — gave the epic extraordinary cultural and political significance in the 19th and 20th centuries, as the primary monument of a suppressed or marginalised national culture."
    ],
    "effects": [
      "The Manas epic's UNESCO inscription (2013) and Kyrgyzstan's independence (1991) gave the epic its current status as the primary national symbol of the Kyrgyz Republic — it is featured on the national currency, in state ceremonies, and in the education system, and the great Manaschi performers (Sagynbay Orozbakovev, Sayakbai Karalaev) are treated as national heroes.",
      "Wilhelm Radloff's 1869 scholarly publication of Manas excerpts — the first systematic documentation of the epic — initiated the academic study of Central Asian oral epic traditions and contributed to the development of the comparative study of oral epic, which reached its culmination in Albert Lord's The Singer of Tales (1960).",
      "The Manas epic's celebration as the primary monument of Kyrgyz national identity — particularly after the independence of Kyrgyzstan in 1991 — contributed to the 'Manas 1000' celebrations of 1995, which marked the supposed millennium of the epic and established Manas as the founding symbol of the Kyrgyz national narrative."
    ],
    "relationships": [
      {"sourceSlug": "epic-of-manas", "sourceName": "Epic of Manas (Kyrgyz national epic)", "verb": "EMBODIES", "targetSlug": "kyrgyz-national-identity", "targetName": "Kyrgyz national identity and cultural heritage", "context": "The Manas epic is the primary monument of Kyrgyz national literature — the central expression of Kyrgyz cultural identity, particularly after Kyrgyz independence (1991) when Manas became the founding symbol of the national narrative."},
      {"sourceSlug": "epic-of-manas", "sourceName": "Epic of Manas (Manaschi tradition)", "verb": "PART_OF", "targetSlug": "central-asian-oral-epic", "targetName": "Central Asian oral epic tradition (Manas, Gesar, Jangar)", "context": "The Manas epic is one of the three great epics of the Central Asian/Mongolian world — performed by specialist Manaschi bards and constituting (in extended versions) one of the longest oral epics in the world."},
      {"sourceSlug": "epic-of-manas", "sourceName": "Epic of Manas (UNESCO 2013)", "verb": "INSCRIBED_ON", "targetSlug": "unesco-intangible-heritage", "targetName": "UNESCO Intangible Cultural Heritage of Humanity", "context": "The Epic of Manas was inscribed on UNESCO's Intangible Cultural Heritage list in 2013 — recognising it as an extraordinary achievement of living oral epic tradition and one of the primary monuments of Central Asian cultural heritage."}
    ],
    "places": [
      {"name": "Kyrgyzstan (primary Kyrgyz homeland, national symbol)", "role": "Kyrgyzstan is the homeland of the Manas epic — the Kyrgyz Republic has placed the epic at the centre of its national identity since independence (1991), featuring it on currency, in state ceremonies, and in education"},
      {"name": "Central Asia (historical Kyrgyz territory, nomadic steppe culture)", "role": "The Manas epic is rooted in the broader Central Asian nomadic steppe culture — its narrative of the Kyrgyz tribes' struggles reflects the historical geography of Central Asian nomadic politics"}
    ],
    "subjects": ["Kyrgyz Literature", "Medieval Era", "Oral Epic", "Central Asian Culture", "Nomadic Culture", "UNESCO Heritage", "Heroic Poetry", "Kyrgyzstan"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Epic of Manas (est. over 500,000 lines) is one of the longest oral epics in the world and the primary monument of Kyrgyz national identity — a UNESCO Intangible Cultural Heritage. The Manaschi performer tradition is one of the most distinctive oral epic traditions in existence. As the central symbol of the Kyrgyz Republic since independence (1991) and as the vehicle of Kyrgyz cultural memory across centuries of conquest and suppression, its significance is extraordinary.",
      "significanceCategory": "highly-significant"
    }
  }
},

"anne-of-green-gables": {
  "filepath": "data/appwrite-export/entities/783-Class-783/783anne-of-green-gables.json",
  "slug": "anne-of-green-gables",
  "data": {
    "summary": "Anne of Green Gables is a novel by Lucy Maud Montgomery (1874–1942), published on 13 June 1908 by L. C. Page & Company of Boston — one of the most beloved and internationally successful Canadian novels ever written, with over 50 million copies sold in translations into at least 36 languages, and the founding text of a series of eight Anne novels that follow Anne Shirley from orphaned childhood to married maturity. The novel follows the red-haired, imaginative, fiercely intelligent Anne Shirley — mistakenly sent to the middle-aged siblings Matthew and Marilla Cuthbert of Green Gables farm in Prince Edward Island in the expectation of a boy to help with farm work — who wins over her reluctant adoptive family and community through her irrepressible personality, her verbal brilliance, and her emotional warmth, eventually winning a scholarship to the Queen's Academy in Charlottetown.\n\nAnne of Green Gables was written from Montgomery's own experience of Prince Edward Island life — the rural landscape of PEI (which Montgomery described as 'the most beautiful place in the world'), the small-town social culture of Avonlea, and the aspiration toward education and self-improvement that characterised the lives of women in late 19th-century rural Canada. The novel's extraordinary success immediately upon publication — it went through six printings in its first year and made Montgomery an internationally known author — established it as a classic of children's literature and of Canadian literature, and transformed Prince Edward Island into a major literary tourism destination. Mark Twain praised it as 'the sweetest creation of child life yet written', and it was enormously popular in Japan, where the character of Anne became a cultural icon.\n\nAnne of Green Gables is a landmark in the representation of female intelligence and ambition in children's literature — Anne's passionate commitment to education, her verbal creativity, her refusal to accept the limitations placed on women, and her emotional courage established the template for the independent-minded, intellectually ambitious girl protagonist that influenced subsequent children's literature.",
    "causes": [
      "Lucy Maud Montgomery's own experience of Prince Edward Island life — her childhood in the rural landscape of PEI, her own aspiration toward education and writing as paths beyond the limited opportunities available to women in rural Canada, and her imaginative relationship with the Island's landscape — provided the autobiographical foundation of Anne of Green Gables.",
      "The late 19th-century expansion of education for women — the growing availability of secondary and higher education for women in Canada and other Western countries, and the cultural aspiration for female intellectual achievement that accompanied it — provided the social context for Anne's story: a girl whose intelligence and determination win her educational opportunities denied by her gender and social position.",
      "The publishing market for children's literature in the early 20th century — particularly the market for girls' fiction featuring independent, aspirational female protagonists (in the tradition of Louisa May Alcott's Little Women, 1868) — created the readership for which Anne of Green Gables was ideally suited."
    ],
    "effects": [
      "Anne of Green Gables transformed Prince Edward Island into a major literary tourism destination — the Green Gables farmhouse (now a national historic site in PEI National Park) and the broader 'Anne of Green Gables' heritage industry (museums, tours, annual festivals, the long-running musical adaptation) make the Anne connection the primary cultural marker of PEI's international identity.",
      "Anne of Green Gables's extraordinary popularity in Japan — where the character of Anne (known as Akage no An, 'Red-haired Anne') became a cultural icon, the novel a standard school text, and Japanese tourists the primary international visitors to PEI — is one of the most striking examples of cross-cultural literary adoption, studied by scholars of Japanese cultural history.",
      "Anne of Green Gables established the template for the independent-minded, intellectually ambitious girl protagonist in children's literature — its influence on subsequent girls' fiction (Pippi Longstocking, The Secret Garden, the Betsy-Tacy series) and on the broader representation of female intelligence and ambition in popular fiction has been substantial."
    ],
    "relationships": [
      {"sourceSlug": "lucy-maud-montgomery", "sourceName": "Lucy Maud Montgomery (1874–1942)", "verb": "AUTHORS", "targetSlug": "anne-of-green-gables", "targetName": "Anne of Green Gables (1908)", "context": "Montgomery published Anne of Green Gables in 1908 — the founding text of an eight-novel Anne Shirley series, one of the most beloved and internationally successful Canadian novels, with over 50 million copies sold."},
      {"sourceSlug": "anne-of-green-gables", "sourceName": "Anne of Green Gables (Prince Edward Island setting)", "verb": "TRANSFORMS", "targetSlug": "prince-edward-island", "targetName": "Prince Edward Island (literary tourism, Green Gables)", "context": "Anne of Green Gables transformed Prince Edward Island into a major literary tourism destination — the Green Gables farmhouse (now a national historic site) and the Anne heritage industry are the primary markers of PEI's international identity."},
      {"sourceSlug": "anne-of-green-gables", "sourceName": "Anne of Green Gables (Akage no An, Japanese cultural icon)", "verb": "ADOPTED_BY", "targetSlug": "japanese-culture", "targetName": "Japanese literary and cultural tradition", "context": "Anne of Green Gables became a cultural icon in Japan — where it has been a standard school text since the 1950s and Japanese tourists are the primary international visitors to Prince Edward Island."}
    ],
    "places": [
      {"name": "Prince Edward Island, Canada (setting, literary tourism)", "role": "Prince Edward Island is the setting of Anne of Green Gables — the Island's rural landscape and the Green Gables farmhouse have been transformed by the novel into a major literary tourism destination"},
      {"name": "Japan (primary international adoption, cultural icon)", "role": "Japan is the most remarkable international market for Anne of Green Gables — the novel became a cultural icon in Japan, a standard school text, and the inspiration for Japanese literary pilgrimage tourism to PEI"}
    ],
    "subjects": ["Canadian Literature", "Modern Era", "Lucy Maud Montgomery", "Children's Literature", "Female Protagonists", "20th Century", "Literary Tourism", "Girls' Fiction"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Anne of Green Gables (Montgomery, 1908) is one of the most internationally successful Canadian novels — over 50 million copies sold in 36 languages, with an extraordinary cultural impact in Japan. It established the template for the intellectually ambitious girl protagonist in children's literature and transformed Prince Edward Island into a global literary tourism destination. Its cross-cultural adoption — particularly in Japan — makes it a landmark in the global reach of children's literature.",
      "significanceCategory": "highly-significant"
    }
  }
},

"borjgali": {
  "filepath": "data/appwrite-export/entities/784-Class-784/784borjgali.json",
  "slug": "borjgali",
  "data": {
    "summary": "The Borjgali (Georgian: ბორჯღალი, Borjghali) is an ancient Georgian symbol — a seven-armed rotating sun wheel or solar disc, composed of seven curved or hooked arms radiating from a central point in a pinwheel/swastika-like rotating pattern — that has been a symbol of the sun, eternal motion, and the cycle of life in Georgian culture from ancient times. The symbol is found in Georgian church architecture (particularly in the carved stone reliefs of medieval Georgian churches such as the Jvari Monastery, 6th century, and the Svetitskhoveli Cathedral, 11th century), in medieval manuscripts, in Georgian folk art (textiles, jewellery, ceramics), and in archaeological artefacts from the Bronze Age cultures of the Caucasus. The Borjgali is one of the most distinctive symbols in Georgian cultural tradition — its seven-armed form (seven being a sacred number in Georgian cosmology and Christian symbolism) distinguishes it from other solar wheel symbols found across Eurasia.\n\nThe Borjgali appears most prominently in the context of Georgian Orthodox Christianity — the Church of Georgia adopted the symbol as a decorative element in its sacred architecture, integrating the pre-Christian solar symbolism with Christian theological content (Christ as the 'Sun of Righteousness', the eternal motion of divine providence). The symbol's appearance in the Jvari Monastery — one of the earliest surviving examples of Georgian sacred architecture and a UNESCO World Heritage Site — and in the carved stonework of the Svetitskhoveli Cathedral (the primary cathedral of Georgia, seat of the Catholicos-Patriarch of All Georgia) gives it its primary association with the Georgian Orthodox Church and Georgian national identity.\n\nThe Borjgali has been revived as a major symbol of Georgian national identity in the post-Soviet period (since 1991) — appearing on jewellery, clothing, tattoos, and official representations of Georgian cultural heritage. Its ancient origins, its Christian association, and its distinctive aesthetic form make it one of the most compelling national symbols in the Caucasus, and it is frequently used alongside the Georgian national flag (the Five Cross Flag) as a marker of Georgian cultural identity in the diaspora.",
    "causes": [
      "The ancient solar symbolism of the Caucasus cultures — the pre-Christian tradition of sun veneration in the ancient Georgian, Colchian, and Kartvelian cultures, reflected in solar wheel symbols found in Bronze Age and Iron Age artefacts from the Caucasus — provided the cultural substrate from which the Borjgali developed, fusing pre-Christian solar symbolism with medieval Christian theological content.",
      "The Georgian Orthodox Church's adoption of indigenous cultural symbols in its sacred architecture — the Jvari Monastery and Svetitskhoveli Cathedral's carved stonework incorporated Borjgali alongside Christian cross designs — created the primary context in which the symbol acquired its enduring religious and national significance.",
      "The Georgian national awakening of the 19th century — and the renewed emphasis on Georgian cultural heritage following the Soviet annexation of Georgia (1921) and Kyrgyz independence (1991) — created the conditions for the Borjgali's revival as a contemporary national identity marker, paralleling the revival of the Armenian Eternity Sign in the same period."
    ],
    "effects": [
      "The Borjgali's association with the medieval Georgian Orthodox Church — particularly its appearance in UNESCO World Heritage Sites (Jvari Monastery, Svetitskhoveli Cathedral, Gelati Academy) — has given it its primary resonance as a marker of Georgian cultural and religious identity: the symbol appears in the context of Georgian architecture that represents the zenith of Georgian medieval civilisation.",
      "The revival of the Borjgali as a contemporary national identity marker — particularly in the post-Soviet period — has made it one of the most widely used Georgian cultural symbols in the Georgian diaspora: it appears in Georgian community contexts worldwide as a connection to the homeland and a symbol of the continuity of Georgian civilisation.",
      "The Borjgali's distinctive seven-armed form — its aesthetic quality as a rotating sun wheel — has given it a notable presence in contemporary Georgian art, design, and tattooing culture, where it appears alongside the Georgian national flag as a marker of Georgian cultural pride."
    ],
    "relationships": [
      {"sourceSlug": "borjgali", "sourceName": "Borjgali (seven-armed sun wheel)", "verb": "APPEARS_IN", "targetSlug": "jvari-monastery", "targetName": "Jvari Monastery (6th century CE, UNESCO World Heritage)", "context": "The Borjgali appears in the carved stone reliefs of the Jvari Monastery — one of the earliest surviving examples of Georgian sacred architecture and a UNESCO World Heritage Site — giving it its primary association with the Georgian Orthodox tradition."},
      {"sourceSlug": "borjgali", "sourceName": "Borjgali (national identity symbol)", "verb": "SYMBOL_OF", "targetSlug": "georgian-national-identity", "targetName": "Georgian national identity and cultural heritage", "context": "The Borjgali has been revived as a major symbol of Georgian national identity in the post-Soviet period — appearing alongside the Georgian national flag as a marker of Georgian cultural identity in the homeland and diaspora."},
      {"sourceSlug": "borjgali", "sourceName": "Borjgali (pre-Christian solar symbolism)", "verb": "RELATED_TO", "targetSlug": "ancient-caucasian-religion", "targetName": "Ancient Caucasian religious and solar traditions", "context": "The Borjgali belongs to the ancient solar symbolism of Caucasus cultures — pre-Christian sun wheel symbols found in Bronze Age artefacts — fused with Georgian Orthodox Christian theological content in medieval sacred architecture."}
    ],
    "places": [
      {"name": "Georgia and historical Georgian territories (origin and primary context)", "role": "The Borjgali is rooted in the cultural tradition of the Georgian lands — appearing in ancient archaeological artefacts and medieval church architecture across Georgia, including the Jvari Monastery and Svetitskhoveli Cathedral"},
      {"name": "Georgian diaspora (global contemporary use)", "role": "The Borjgali is used by Georgian diaspora communities worldwide — particularly in Russia, the United States, and Europe — as a symbol of cultural identity and connection to the Georgian homeland"}
    ],
    "subjects": ["Georgian Culture", "Medieval Era", "National Symbols", "Georgian Christianity", "Visual Art", "Cultural Identity", "Caucasus", "Medieval Art"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "The Borjgali is one of the most distinctive symbols of Georgian cultural identity — a seven-armed solar wheel found in medieval Georgian church architecture (Jvari Monastery, Svetitskhoveli Cathedral, both UNESCO World Heritage Sites) and revived in the post-Soviet period as a national identity marker. Its ancient origins, Christian association, and aesthetic distinctiveness make it a compelling symbol of Georgian civilisational continuity.",
      "significanceCategory": "significant"
    }
  }
},

"ordinary-language-philosophy": {
  "filepath": "data/appwrite-export/entities/785-Class-785/785ordinary-language-philosophy.json",
  "slug": "ordinary-language-philosophy",
  "data": {
    "summary": "Ordinary language philosophy (also 'linguistic philosophy' or the 'Oxford Philosophy' movement) is a philosophical approach that dominated British philosophy, particularly at the University of Oxford, from approximately the late 1930s to the early 1960s — associated primarily with Gilbert Ryle (1900–1976), J. L. Austin (1911–1960), P. F. Strawson (1919–2006), and the later work of Ludwig Wittgenstein (1889–1951, particularly the Philosophical Investigations, 1953). The movement's central claim was that many traditional philosophical problems — questions about the existence of the external world, the nature of mental states, the problem of other minds, the analysis of knowledge and perception — arose from the systematic misuse of language: philosophers had taken words (like 'mind', 'know', 'perceive', 'cause') out of their ordinary contexts of use and forced them into frameworks that generated apparent paradoxes, when in fact the correct response was to attend carefully to how these words actually function in ordinary language.\n\nThe methodological core of ordinary language philosophy was close attention to the nuances of everyday linguistic use — Austin's 'linguistic phenomenology' (his preferred term) involved detailed analysis of the distinctions made by ordinary English speakers in contexts of action, perception, knowledge, and speech — producing the theory of speech acts (How to Do Things with Words, 1962, published posthumously from Austin's William James Lectures at Harvard, 1955). Austin distinguished between locutionary acts (the act of saying something), illocutionary acts (what one does in saying something: promising, warning, asserting, threatening), and perlocutionary acts (the effects of saying something), providing the foundational framework for what became philosophy of language and pragmatics.\n\nOrdinary language philosophy was the dominant mode of British academic philosophy in the 1940s–1960s and had a significant influence on philosophy of mind (Ryle's critique of Cartesian 'category mistakes' in The Concept of Mind, 1949), epistemology (Strawson's Individuals, 1959), and philosophy of language (Austin's speech act theory). Its decline from the mid-1960s — associated with the rise of formal semantics (Chomsky, Davidson) and the analytic philosophy's turn toward more formal methods — was followed by the absorption of speech act theory into linguistics and pragmatics.",
    "causes": [
      "Wittgenstein's late philosophy — his critique of the Tractatus Logico-Philosophicus's picture theory of meaning and his turn toward use-theory (meaning as use in a form of life) in the Philosophical Investigations — provided the foundational philosophical impulse of ordinary language philosophy: the idea that philosophical problems arise from misuse of language and can be dissolved by attending to ordinary linguistic practice.",
      "The reaction against logical positivism and the Tractatus tradition in British philosophy — the recognition that the formal logical analysis of language (Russell, early Wittgenstein, Vienna Circle) had not resolved but merely reformulated traditional philosophical problems — created the intellectual space for the ordinary language movement's alternative approach of attending to the nuances of everyday language.",
      "The Oxford tutorial tradition — the characteristic mode of philosophical education at Oxford, which developed analytical precision through intense one-on-one discussion of specific philosophical problems — provided the pedagogical context for the detailed, case-by-case analysis of ordinary language that characterised the Oxford philosophy movement."
    ],
    "effects": [
      "Austin's speech act theory — developed from his ordinary language analysis of performative utterances and the distinctions between locutionary, illocutionary, and perlocutionary acts — became foundational for the fields of philosophy of language, linguistics (pragmatics), and communication theory, with enormous influence on computational linguistics, natural language processing, and the theory of communication.",
      "Ryle's The Concept of Mind (1949) — his critique of the Cartesian 'ghost in the machine' and his analysis of mental concepts as categorical mistakes — was one of the most influential works of 20th-century philosophy of mind, shaping subsequent debates about behaviourism, functionalism, and the nature of mental states.",
      "Ordinary language philosophy's decline as a dominant programme — replaced by formal semantics, modal logic, and truth-conditional theories of meaning — was followed by the absorption of its most productive results (speech act theory, the analysis of performative utterances, the theory of conversational implicature of Grice) into linguistics, pragmatics, and philosophy of language."
    ],
    "relationships": [
      {"sourceSlug": "ordinary-language-philosophy", "sourceName": "Ordinary language philosophy (Oxford, 1940s–1960s)", "verb": "FOUNDED_ON", "targetSlug": "philosophical-investigations", "targetName": "Philosophical Investigations (Wittgenstein, 1953)", "context": "Wittgenstein's late philosophy — the use-theory of meaning in the Philosophical Investigations — provided the foundational philosophical impulse of ordinary language philosophy: the dissolution of philosophical problems through attention to ordinary linguistic practice."},
      {"sourceSlug": "ordinary-language-philosophy", "sourceName": "Ordinary language philosophy (speech act theory)", "verb": "PRODUCES", "targetSlug": "speech-act-theory", "targetName": "Speech act theory (Austin, How to Do Things with Words, 1962)", "context": "Austin's ordinary language analysis produced speech act theory — the foundational framework for philosophy of language, linguistics (pragmatics), and communication theory — which became one of the most influential innovations in 20th-century language theory."},
      {"sourceSlug": "ordinary-language-philosophy", "sourceName": "Ordinary language philosophy (Ryle, Concept of Mind)", "verb": "CHALLENGES", "targetSlug": "cartesian-dualism", "targetName": "Cartesian mind-body dualism (the 'ghost in the machine')", "context": "Ryle's The Concept of Mind (1949) — the ordinary language philosophy critique of Cartesian mind-body dualism as a category mistake — was one of the most influential arguments against substance dualism in 20th-century philosophy of mind."}
    ],
    "places": [
      {"name": "University of Oxford (primary institutional base, 1940s–1960s)", "role": "Oxford — particularly the Oxford philosophy department — was the primary institutional context of ordinary language philosophy: Austin, Ryle, Strawson, and Grice all taught at Oxford and developed the movement's characteristic methods"},
      {"name": "Cambridge (Wittgenstein's base, foundational influence)", "role": "Wittgenstein's late philosophy was developed at Cambridge — his lectures and the Philosophical Investigations provided the foundational impulse for ordinary language philosophy, though Wittgenstein remained distinct from the Oxford movement"}
    ],
    "subjects": ["Philosophy", "Modern Era", "Ludwig Wittgenstein", "J.L. Austin", "Philosophy of Language", "20th Century", "Oxford Philosophy", "Analytic Philosophy"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Ordinary language philosophy (Oxford, 1940s–1960s) is one of the most influential movements in 20th-century analytic philosophy — producing speech act theory (Austin), the critique of Cartesian dualism (Ryle), and contributions to epistemology (Strawson). Speech act theory became foundational for philosophy of language, linguistics (pragmatics), communication theory, and computational linguistics. Austin's distinction between locutionary, illocutionary, and perlocutionary acts remains one of the most productive frameworks in language theory.",
      "significanceCategory": "highly-significant"
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
