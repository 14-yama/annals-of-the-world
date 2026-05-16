#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 03 (8 high-priority entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities covered (from enrichment_queue top candidates, not in any bot queue):
  epic-of-gilgamesh, roman-republic, old-kingdom-of-egypt,
  prokop-the-great, dorotea-bucca, deng-xi,
  richard-fitzralph, katakalon-kekaumenos

No conflict risk: Gemini on queue[200:300], Ollama-A on queue[325:425], Ollama-B on queue[425:525].
"""

import json
import os
import sys
import time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-03-may2026"

# ─────────────────────────────────────────────────────────────────────────────
# Hand-authored enrichments (Claude Sonnet 4.6 / GitHub Copilot)
# ─────────────────────────────────────────────────────────────────────────────

ENRICHMENTS = {

"epic-of-gilgamesh": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782epic-of-gilgamesh.json",
  "slug": "epic-of-gilgamesh",
  "data": {
    "summary": "The Epic of Gilgamesh is the oldest surviving work of epic literature in the world, composed in Sumerian and Akkadian cuneiform on clay tablets in ancient Mesopotamia between approximately 2100 and 1200 BCE. The poem centres on Gilgamesh, the historical king of Uruk (c. 2700 BCE) who was two-thirds divine and one-third human, and his companion Enkidu — a wild man formed from clay who becomes his closest friend. Together they slay the monster Humbaba in the Cedar Forest and kill the Bull of Heaven, but Enkidu's subsequent death sends Gilgamesh on a desperate search for immortality that ends at the ends of the earth, where the flood survivor Utnapishtim reveals that death cannot be conquered.\n\nThe epic's most celebrated section — the Flood Narrative in Tablet XI — describes a divine deluge sent to destroy humanity, survived by Utnapishtim who built a boat and preserved all living creatures, a story strikingly parallel to the later Biblical account of Noah. This discovery by George Smith in 1872 at the British Museum caused a sensation, demonstrating for the first time that Hebrew scripture shared sources with older Near Eastern literature. The Standard Babylonian Version, compiled by the scholar-scribe Sîn-lēqi-unninni around 1200 BCE, is the most complete recension, preserved across twelve tablets found at Ashurbanipal's library in Nineveh (destroyed 612 BCE).\n\nThe epic's themes — friendship, hubris, the fear of death, the limits of heroism, and the search for meaning — remain startlingly contemporary. It influenced the Odyssey, the Book of Job, and countless subsequent works. Its rediscovery in the 19th century transformed the study of ancient history and comparative religion, proving that civilisation's deepest preoccupations — mortality, companionship, and legacy — precede the Hebrew Bible by over a millennium.",
    "causes": [
      "The emergence of Sumerian city-states along the Euphrates after 3500 BCE created the world's first complex literate culture with surplus resources to support scribal schools, royal court traditions, and the composition of long narrative poetry.",
      "The historical reign of Gilgamesh as king of Uruk (c. 2700 BCE) provided the nucleus for later mythologisation, as his city-building, military campaigns, and two-thirds divine ancestry were elaborated into a narrative exploring the human condition.",
      "The invention of cuneiform writing after 3400 BCE gave Mesopotamian scholars a durable medium for recording oral traditions, enabling heroic poetry to be codified, standardised, and transmitted across centuries and political dynasties."
    ],
    "effects": [
      "The Flood Narrative in Tablet XI directly parallels the Biblical story of Noah (Genesis 6–9), demonstrating that Hebrew scriptural traditions drew on older Near Eastern sources and profoundly influencing 19th-century biblical scholarship and comparative religious studies.",
      "The epic established foundational literary templates — the hero's journey, the loyal companion, the quest for immortality — that recur across Homer's Odyssey, Virgil's Aeneid, Dante's Inferno, and modern narrative traditions.",
      "George Smith's 1872 decipherment of the Flood Tablet from Ashurbanipal's Library at Nineveh triggered a revolution in Assyriology and archaeology, making the Epic of Gilgamesh the catalyst for systematic excavation of Mesopotamian sites."
    ],
    "relationships": [
      {"sourceSlug": "epic-of-gilgamesh", "sourceName": "Epic of Gilgamesh", "verb": "INFLUENCES", "targetSlug": "bible", "targetName": "Hebrew Bible", "context": "The Flood Narrative in Tablet XI (c. 1200 BCE) shares extraordinary parallels with the Noah story in Genesis, suggesting direct transmission of flood mythology from Mesopotamian to Hebrew literary tradition."},
      {"sourceSlug": "epic-of-gilgamesh", "sourceName": "Epic of Gilgamesh", "verb": "INFLUENCES", "targetSlug": "odyssey", "targetName": "Odyssey", "context": "Scholars have identified structural and thematic parallels between Gilgamesh's journey to Utnapishtim and Odysseus's wanderings, suggesting the epic influenced early Greek literary traditions."},
      {"sourceSlug": "uruk", "sourceName": "Uruk", "verb": "PRODUCES", "targetSlug": "epic-of-gilgamesh", "targetName": "Epic of Gilgamesh", "context": "Uruk, the world's first true city, was both the home city of the historical Gilgamesh and the setting of the epic's opening tablets describing its magnificent walls."},
      {"sourceSlug": "cuneiform", "sourceName": "Cuneiform Writing", "verb": "ENABLES", "targetSlug": "epic-of-gilgamesh", "targetName": "Epic of Gilgamesh", "context": "Cuneiform script, invented in Mesopotamia around 3400 BCE, was the medium on which the epic was recorded across twelve clay tablets, enabling its preservation and eventual decipherment."},
      {"sourceSlug": "ashurbanipal", "sourceName": "Ashurbanipal", "verb": "PRESERVES", "targetSlug": "epic-of-gilgamesh", "targetName": "Epic of Gilgamesh", "context": "The Standard Babylonian Version of the epic was found in Ashurbanipal's great library at Nineveh (c. 650 BCE), the most complete ancient archive ever discovered."}
    ],
    "places": [
      {"name": "Uruk, Iraq", "role": "City of Gilgamesh; setting of the epic's opening; site of the world's first urban civilisation"},
      {"name": "Nineveh, Iraq", "role": "Site of Ashurbanipal's library where the most complete version of the epic was found in 1853"},
      {"name": "Cedar Forest (Lebanon/Syria)", "role": "Mythological destination of Gilgamesh and Enkidu's first great adventure, slaying the monster Humbaba"}
    ],
    "subjects": ["Literature", "Mythology", "Ancient History", "Mesopotamia", "Religion", "Philosophy", "Archaeology", "Classical Era", "Writing", "Death and Immortality"],
    "frameworks": ["CULTURAL_TRANSMISSION", "COMPARATIVE_CIVILIZATIONS", "LONGUE_DUREE"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Epic of Gilgamesh is the oldest surviving work of epic literature, predating the Iliad by 1,500 years. Its rediscovery in 1872 transformed biblical scholarship by proving that Hebrew flood mythology derived from older Mesopotamian sources. Its themes of mortality, friendship, and the search for meaning established the foundational grammar of world literature.",
      "significanceCategory": "world-changing"
    }
  }
},

"roman-republic": {
  "filepath": "data/appwrite-export/entities/430-Class-430/430roman-republic.json",
  "slug": "roman-republic",
  "data": {
    "summary": "The Roman Republic (509–27 BCE) was the governing framework of Rome for nearly five centuries, established after the expulsion of the Etruscan king Tarquinius Superbus and ending when Octavian (Augustus) transformed it into the Roman Empire. It developed the world's most sophisticated pre-modern constitutional system: two annually elected consuls balanced by the Senate, the tribunes of the plebs with their power of veto, the census, the cursus honorum (the ladder of magistracies), and the principle — always contested — that no single man should hold permanent power. These innovations in separated authority, representative assembly, and popular sovereignty laid the constitutional groundwork for every subsequent Western republic.\n\nThe Republic's five centuries encompassed the Punic Wars against Carthage (264–146 BCE), the conquest of the Hellenistic East, the Social War that extended citizenship to all Italian allies, the land reform crises of the Gracchi brothers, and the violent succession of civil wars — Marius vs. Sulla, Caesar vs. Pompey — that finally shattered the Republican order. Julius Caesar's crossing of the Rubicon (49 BCE) and subsequent dictatorship, followed by his assassination on the Ides of March 44 BCE, set in motion the final civil wars between Octavian, Mark Antony, and the Liberators that ended Republican government altogether.\n\nThe Republic's legacy is inseparable from the founding documents of modern democracy. The American Founders drew explicitly on Roman Republican precedents: the Senate, the consulship, the notion of republican virtue, Cicero's political philosophy, and Polybius's theory of mixed constitutions all fed directly into the US Constitution of 1787. The French Revolutionary motto of 'liberté, égalité, fraternité' drew on Roman Republican ideals of civic participation. Every elected legislature, every system of checks and balances, every distinction between republic and monarchy owes something to Rome's five-century experiment.",
    "causes": [
      "The expulsion of the Etruscan king Tarquinius Superbus in 509 BCE, following the rape of Lucretia, catalysed the Roman aristocracy's establishment of a republic with annual elected consuls to prevent the return of monarchy.",
      "The threat of Carthage across two centuries of Punic Wars forced the Roman Republic to develop professional armies, provincial administration, and Mediterranean-scale logistics that both strengthened and ultimately militarised the state.",
      "Social inequality between patricians and plebeians produced the Conflict of the Orders (494–287 BCE), driving constitutional reforms — the tribunes, the Twelve Tables, the Lex Hortensia — that progressively democratised Roman governance while keeping aristocratic power intact."
    ],
    "effects": [
      "Roman Republican constitutional theory — the Senate, consular authority, tribunician veto, and Polybian mixed constitution — directly shaped the framers of the American Constitution in 1787, making it the most consequential political template in Western history.",
      "The Republic's expansion created the first unified Mediterranean political and legal space, spreading Latin language, Roman law, and urban planning across Europe, North Africa, and the Near East — a framework that persisted through the medieval period.",
      "The Republic's destruction in civil war became the paradigmatic cautionary tale: Cicero, the Gracchi, Caesar, and Augustus were the canonical examples invoked by every subsequent political theorist debating the fragility of republican institutions."
    ],
    "relationships": [
      {"sourceSlug": "roman-republic", "sourceName": "Roman Republic", "verb": "TRANSFORMS", "targetSlug": "roman-empire", "targetName": "Roman Empire", "context": "The Republic collapsed into the Empire when Octavian defeated Mark Antony at Actium (31 BCE) and assumed the title Augustus in 27 BCE, ending five centuries of Republican governance."},
      {"sourceSlug": "roman-republic", "sourceName": "Roman Republic", "verb": "INFLUENCES", "targetSlug": "united-states-constitution", "targetName": "US Constitution", "context": "The American Founding Fathers explicitly modelled the Senate, separation of powers, and concept of republican virtue on Roman Republican precedents, citing Cicero, Polybius, and Livy."},
      {"sourceSlug": "julius-caesar", "sourceName": "Julius Caesar", "verb": "DESTROYS", "targetSlug": "roman-republic", "targetName": "Roman Republic", "context": "Caesar's crossing of the Rubicon (49 BCE), military dictatorship, and assassination in 44 BCE triggered the final civil wars that ended Republican government."},
      {"sourceSlug": "cicero", "sourceName": "Cicero", "verb": "DEFINES", "targetSlug": "roman-republic", "targetName": "Roman Republic", "context": "Cicero's De Re Publica and De Legibus articulated the philosophical foundations of Republican governance and became canonical texts for all subsequent Western political thought."},
      {"sourceSlug": "roman-republic", "sourceName": "Roman Republic", "verb": "PRODUCES", "targetSlug": "roman-law", "targetName": "Roman Law", "context": "The Republic produced the Twelve Tables (450 BCE) and the evolving ius civile and ius gentium, the foundational legal corpus from which all Western legal systems descend."}
    ],
    "places": [
      {"name": "Rome, Italy", "role": "Capital of the Republic; site of the Senate, the Forum, and the institutions of Republican governance"},
      {"name": "Carthage, Tunisia", "role": "Rival power across three Punic Wars; its destruction in 146 BCE marked Rome's emergence as uncontested Mediterranean hegemon"},
      {"name": "Rubicon River, Italy", "role": "Boundary crossed by Julius Caesar in 49 BCE, triggering civil war and effectively ending the Republic"}
    ],
    "subjects": ["Politics", "Classical History", "Law", "Philosophy", "Military History", "Rome", "Mediterranean", "Democracy", "Constitutional Government", "Classical Era"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT", "COMPARATIVE_CIVILIZATIONS", "LONGUE_DUREE"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Roman Republic invented the constitutional tools of Western democracy — the Senate, separation of powers, elected magistracies, and the principle that no single man should hold permanent authority. Its five-century arc, from the expulsion of kings in 509 BCE to Augustus's coup in 27 BCE, became the master template for every subsequent political philosopher debating republican versus imperial governance, from Cicero to Montesquieu to the American Founding Fathers.",
      "significanceCategory": "world-changing"
    }
  }
},

"old-kingdom-of-egypt": {
  "filepath": "data/appwrite-export/entities/430-Class-430/430old-kingdom-of-egypt.json",
  "slug": "old-kingdom-of-egypt",
  "data": {
    "summary": "The Old Kingdom of Egypt (c. 2686–2181 BCE) was the first great age of Egyptian pyramid-building, state formation, and cultural achievement — the era in which ancient Egypt created the monumental visual language that would define its civilisation for three millennia. Spanning the Third through Sixth Dynasties, it was governed from Memphis and presided over by pharaohs who claimed divine kingship as incarnations of the falcon-god Horus in life and Osiris in death. This theological framework justified the mobilisation of the state's entire productive capacity for monumental construction, culminating in the Giza complex — the Great Pyramid of Khufu, Khafre's pyramid with its Sphinx, and Menkaure's pyramid — still the most recognisable architectural achievement in human history.\n\nThe administrative revolution of the Old Kingdom was as significant as its monuments. The pharaohs established a centralised bureaucracy of literate officials, standardised weights and measures, and a redistributive economy in which agricultural surpluses from the Nile Delta were channelled through royal granaries to pay workers, fund temples, and sustain an unprecedented degree of state coordination. The Pyramid Texts, inscribed in the burial chambers of the Fifth and Sixth Dynasty pharaohs, are the world's oldest religious literature — 800 spells ensuring the pharaoh's resurrection and journey through the afterlife.\n\nThe Old Kingdom ended with the First Intermediate Period (c. 2181–2055 BCE), triggered by a catastrophic multi-decade drought associated with a collapse of the Nile flood cycle around 2200 BCE. Provincial governors (nomarchs) seized power as central authority dissolved. The collapse is one of antiquity's earliest documented civilisational failures caused by climate change, studied today as a case study in the vulnerability of complex societies to environmental stress.",
    "causes": [
      "The unification of Upper and Lower Egypt under the First Dynasty (c. 3100 BCE) created the territorial and political foundation for the Old Kingdom's centralised pharaonic state, fusing the Red Crown of Lower Egypt and the White Crown of Upper Egypt into a single monarchy.",
      "The Nile's annual inundation deposited nutrient-rich silt across the floodplain, producing agricultural surpluses that sustained dense population and released the labour force required for pyramid construction without depleting subsistence production.",
      "The emergence of professional scribal bureaucracy and hieroglyphic writing under the Early Dynastic Period gave the Old Kingdom the administrative infrastructure to coordinate tens of thousands of workers, manage granary redistribution, and document royal decrees across a unified state."
    ],
    "effects": [
      "The pyramids and the Sphinx established Egypt's visual and architectural identity for 3,000 years, influencing Roman obelisks, Napoleonic Egyptian Revival architecture, and modern global tourism — the Great Pyramid remained the world's tallest man-made structure for 3,800 years until Lincoln Cathedral (1311 CE).",
      "The Pyramid Texts (c. 2400 BCE) established the first written theology in the world, encoding beliefs about resurrection, the afterlife, and divine kingship that evolved into the Book of the Dead and influenced later Egyptian, Greek, and early Christian religious concepts.",
      "The Old Kingdom's collapse into the First Intermediate Period became a foundational historical template: the breakdown of centralised order, the rise of regional powers, and the eventual reunification under the Middle Kingdom demonstrated the cyclical pattern of Egyptian dynastic history."
    ],
    "relationships": [
      {"sourceSlug": "old-kingdom-of-egypt", "sourceName": "Old Kingdom of Egypt", "verb": "PRODUCES", "targetSlug": "great-pyramid-of-giza", "targetName": "Great Pyramid of Giza", "context": "Pharaoh Khufu (Cheops) of the Fourth Dynasty built the Great Pyramid c. 2560 BCE, the largest and most precisely engineered pyramid, requiring the coordination of an estimated 20,000-30,000 workers."},
      {"sourceSlug": "old-kingdom-of-egypt", "sourceName": "Old Kingdom of Egypt", "verb": "PRODUCES", "targetSlug": "pyramid-texts", "targetName": "Pyramid Texts", "context": "The Pyramid Texts (c. 2400 BCE), inscribed in Fifth and Sixth Dynasty burial chambers, are the oldest surviving religious literature in the world, encoding Egyptian funerary theology."},
      {"sourceSlug": "old-kingdom-of-egypt", "sourceName": "Old Kingdom of Egypt", "verb": "TRANSFORMS", "targetSlug": "first-intermediate-period", "targetName": "First Intermediate Period", "context": "A prolonged drought around 2200 BCE collapsed the Nile flood cycle, caused famines, undermined pharaonic authority, and triggered the fragmentation of the Old Kingdom into regional powers."},
      {"sourceSlug": "khufu", "sourceName": "Khufu", "verb": "DEFINES", "targetSlug": "old-kingdom-of-egypt", "targetName": "Old Kingdom of Egypt", "context": "Khufu's construction of the Great Pyramid (c. 2560 BCE) represents the apogee of Old Kingdom centralised power and pyramid-building ambition."},
      {"sourceSlug": "old-kingdom-of-egypt", "sourceName": "Old Kingdom of Egypt", "verb": "INFLUENCES", "targetSlug": "ancient-egypt", "targetName": "Ancient Egyptian Civilisation", "context": "The Old Kingdom established the canonical forms of Egyptian kingship, art, architecture, and religious practice that defined Egyptian culture for the following 2,500 years."}
    ],
    "places": [
      {"name": "Memphis, Egypt", "role": "Administrative capital of the Old Kingdom and centre of pharaonic government throughout the Third through Sixth Dynasties"},
      {"name": "Giza, Egypt", "role": "Site of the pyramids of Khufu, Khafre, and Menkaure and the Great Sphinx — the defining monuments of the Old Kingdom"},
      {"name": "Saqqara, Egypt", "role": "Burial site of the Third Dynasty pharaohs including Djoser's Step Pyramid (c. 2650 BCE), the world's oldest large-scale stone structure"}
    ],
    "subjects": ["Ancient History", "Archaeology", "Architecture", "Religion", "Egypt", "Africa", "Classical Era", "State Formation", "Climate and Society"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "ENVIRONMENTAL_HISTORY", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Old Kingdom produced the Pyramids of Giza — the only surviving wonder of the ancient world — and the Pyramid Texts, the world's oldest religious literature. Its administrative and theological innovations defined Egyptian civilisation for 3,000 years. Its climate-induced collapse around 2200 BCE is one of the earliest documented examples of state failure caused by environmental change.",
      "significanceCategory": "world-changing"
    }
  }
},

"prokop-the-great": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250prokop-the-great.json",
  "slug": "prokop-the-great",
  "data": {
    "summary": "Prokop the Great (c. 1380–1434), born Prokop Holý ('the Holy' or 'the Bald'), was the most formidable military commander of the Hussite Wars (1419–1434) and the man who transformed the Hussite movement from a regional religious rebellion into a revolutionary military force capable of defeating every crusade Europe launched against Bohemia. A former priest and disciple of Jan Žižka, Prokop assumed command of the Taborite army after Žižka's death in 1424 and led it through an extraordinary decade of victories that humiliated five successive papal crusades.\n\nProkop perfected the wagon fortress (Wagenburg) tactics that Žižka had pioneered — mobile fortifications of armoured war wagons chained together into defensive perimeters, mounted with artillery and crossbowmen. Under his command these tactics evolved into an offensive instrument: the Hussite armies made five great 'spanilé jizdy' (beautiful rides) deep into Germany, Austria, Hungary, and Silesia between 1426 and 1433, ravaging the territories of crusade supporters and demonstrating that a revolutionary religious force armed with gunpowder weapons could operate beyond its home territory at continental scale. European powers found themselves unable to defeat the Hussites in open battle.\n\nProkop's downfall came from within: the ideological fragmentation of the Hussite movement between the moderate Utraquists and the radical Taborites led to the Battle of Lipany (1434), a civil war engagement in which the Utraquists and Bohemian nobility, allied with their former Catholic enemies, destroyed the Taborite army. Prokop died in the battle. His campaigns are studied as a pivotal early demonstration of how religious revolutionary movements armed with new technology can resist and defeat the military power of established Christian empire.",
    "causes": [
      "The martyrdom of Jan Hus at the Council of Constance in 1415, burned despite a safe-conduct promise, radicalised the Bohemian reform movement and transformed peaceful religious dissent into armed revolution against both the papacy and Holy Roman Emperor.",
      "Jan Žižka's tactical innovations with the wagon fortress (Wagenburg) gave the Hussite forces a battlefield system that neutralised the advantage of armoured cavalry, producing a series of stunning victories that attracted Prokop to military command.",
      "The repeated papal crusades (1420, 1421, 1422, 1427, 1431) failed to suppress the Hussite rebellion and instead provided Prokop with recurring opportunities to demonstrate Hussite military superiority, each victory strengthening the movement's legitimacy and territorial base."
    ],
    "effects": [
      "The five Hussite crusade victories under Prokop established that a religiously motivated popular army using wagon fortresses and gunpowder weapons could defeat feudal cavalry armies, influencing Swiss cantonal warfare and early modern military doctrine on the role of infantry and artillery.",
      "The Hussite Wars forced the Council of Basel to negotiate the Compactata of Basel (1436), which granted Bohemians the right to communion in both kinds (utraquism) — the first time the Catholic Church made a doctrinal concession to heresy under military pressure, a precedent that weakened papal authority before the Reformation.",
      "Prokop's revolutionary combination of religious ideology and military effectiveness became a template studied by subsequent reformers; the Hussite movement is considered a direct precursor to the Protestant Reformation of 1517."
    ],
    "relationships": [
      {"sourceSlug": "prokop-the-great", "sourceName": "Prokop the Great", "verb": "SUCCEEDS", "targetSlug": "jan-zizka", "targetName": "Jan Žižka", "context": "Prokop assumed command of the Taborite Hussite army after Jan Žižka's death from plague in 1424, inheriting his wagon fortress tactics and building on them to lead five victorious crusade campaigns."},
      {"sourceSlug": "jan-hus", "sourceName": "Jan Hus", "verb": "INSPIRES", "targetSlug": "prokop-the-great", "targetName": "Prokop the Great", "context": "Hus's martyrdom at Constance in 1415 was the founding trauma of the Hussite movement; Prokop's military campaigns were fought explicitly in defence of Hussite religious principles."},
      {"sourceSlug": "prokop-the-great", "sourceName": "Prokop the Great", "verb": "INFLUENCES", "targetSlug": "protestant-reformation", "targetName": "Protestant Reformation", "context": "The Hussite Wars demonstrated that reform movements could survive papal and imperial suppression through armed resistance; Luther explicitly cited the Hussites as precursors of his own reformation a century later."},
      {"sourceSlug": "council-of-basel", "sourceName": "Council of Basel", "verb": "RESPONDS_TO", "targetSlug": "prokop-the-great", "targetName": "Prokop the Great", "context": "The Council of Basel's Compactata (1436) conceding utraquism to Bohemia was a direct diplomatic response to the Hussite military victories Prokop had led; the Church negotiated because it could not win militarily."}
    ],
    "places": [
      {"name": "Bohemia (Czech Republic)", "role": "Homeland of the Hussite movement; theatre of Prokop's defensive campaigns against five papal crusades"},
      {"name": "Lipany, Czech Republic", "role": "Site of the 1434 civil battle where Prokop died and the Taborite faction was destroyed by an alliance of Utraquists and Bohemian nobility"},
      {"name": "Germany/Austria/Silesia", "role": "Territories raided during Prokop's five offensive 'beautiful rides' (1426–1433) that demonstrated Hussite power projection beyond Bohemia"}
    ],
    "subjects": ["Military History", "Religious Reform", "Medieval History", "Bohemia", "Central Europe", "Warfare", "Medieval Era", "Revolutionary Movements"],
    "frameworks": ["CAUSE_AND_EFFECT", "RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Prokop the Great led the Hussite armies to five consecutive victories over papal crusades, forcing the Council of Basel to make the first doctrinal concession to heresy in Church history. His tactical innovations with wagon fortresses and early artillery influenced the military revolution of the 16th century, and his movement is a direct precursor to the Protestant Reformation.",
      "significanceCategory": "highly-significant"
    }
  }
},

"dorotea-bucca": {
  "filepath": "data/appwrite-export/entities/241-Class-241/241dorotea-bucca.json",
  "slug": "dorotea-bucca",
  "data": {
    "summary": "Dorotea Bucca (c. 1360–1436) was a pioneering Italian physician and university professor at the University of Bologna — one of the world's oldest universities — and one of the very few women to hold a formal academic medical chair in the medieval period. Born into a distinguished academic family (her father Bartolomeo Bucca was himself a professor of medicine at Bologna), Dorotea succeeded him in the chair of medicine around 1390 and continued to teach publicly for over forty years. Her appointment was exceptional not merely for its gender but for its duration and formal recognition: she held a salaried professorship at a time when women were systematically excluded from nearly all academic institutions across Europe.\n\nBologna had a distinctive tradition of female scholars — Novella d'Andrea had lectured in canon law in the early 14th century, reportedly behind a screen to avoid distracting students with her beauty — but Dorotea Bucca was the most persistently documented female academic of the medieval period. She lectured on theoretical medicine (medicina theorica) and moral philosophy, subjects at the highest tier of the medieval university curriculum. Her students included both men and women, and her reputation drew attention from across northern Italy. Contemporary sources, including humanist correspondents, note her exceptional learning and eloquence.\n\nDorotea Bucca represents the narrow but real space that medieval Italian universities — more pragmatic and less clerically dominated than their French and English counterparts — occasionally opened for exceptional women of scholarly families. Her forty-year career demonstrates that female academic participation was not a modern invention but a historical reality, however exceptional, within specific institutional contexts — a fact that feminist historians recovered in the 20th century.",
    "causes": [
      "The University of Bologna's secular founding (1088 CE) and civic governance — unlike the clerically dominated universities of Paris and Oxford — created an institutional culture less rigidly exclusionary toward women, particularly those from established scholarly families.",
      "Dorotea's birth into the Bucca academic dynasty provided her with the private education, library access, and patronage networks that most women were systematically denied; her father Bartolomeo's professorship at Bologna was the direct gateway to her own academic appointment.",
      "The Italian humanist movement's revival of classical learning in the 14th–15th centuries created an intellectual climate that, for educated women of elite families, provided occasional pathways to public scholarly recognition absent elsewhere in Europe."
    ],
    "effects": [
      "Dorotea Bucca's forty-year professorship established an empirical precedent for female academic leadership that later feminist historians — particularly those recovering medieval women scholars in the 20th century — cited as evidence that women's intellectual exclusion was historical contingency, not natural order.",
      "Her career contributed to Bologna's distinctive reputation as a university willing to recognise female scholars, a tradition that influenced subsequent Italian universities and made northern Italy a relative centre of early modern women's academic participation compared to northern Europe.",
      "As a practitioner and teacher of medicine, Dorotea's clinical work and teaching contributed to the transmission of Galenic and Arabic medical knowledge through the Italian university system during the critical period between the Black Death and the anatomical revolution of Vesalius (1543)."
    ],
    "relationships": [
      {"sourceSlug": "dorotea-bucca", "sourceName": "Dorotea Bucca", "verb": "OCCURS_IN", "targetSlug": "university-of-bologna", "targetName": "University of Bologna", "context": "Dorotea held her chair of medicine at the University of Bologna, the world's oldest university (founded 1088), for approximately forty years from around 1390 to her death in 1436."},
      {"sourceSlug": "dorotea-bucca", "sourceName": "Dorotea Bucca", "verb": "INFLUENCES", "targetSlug": "history-of-women-in-medicine", "targetName": "History of Women in Medicine", "context": "Dorotea Bucca's documented professorship became a key historical example cited by 20th-century feminist historians and medical historians recovering women's contributions to academic medicine."},
      {"sourceSlug": "italian-humanism", "sourceName": "Italian Humanism", "verb": "ENABLES", "targetSlug": "dorotea-bucca", "targetName": "Dorotea Bucca", "context": "The humanist culture of 14th–15th century northern Italy created the intellectual context in which educated women of elite scholarly families could occasionally gain public academic recognition."}
    ],
    "places": [
      {"name": "Bologna, Italy", "role": "Site of the University of Bologna where Dorotea held her professorship in medicine for approximately forty years"},
      {"name": "Northern Italy", "role": "The broader cultural context of Italian humanism and civic universities that created the rare institutional opening for medieval female academics"}
    ],
    "subjects": ["Women's History", "Medieval History", "History of Medicine", "Academic History", "Italy", "Education", "Gender Studies", "Medieval Era"],
    "frameworks": ["FEMINIST_PERSPECTIVE", "STRUCTURAL_ANALYSIS", "CULTURAL_TRANSMISSION"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Dorotea Bucca's forty-year professorship at the University of Bologna (c. 1390–1436) makes her one of the most extensively documented female academics in medieval history. Her career demonstrates that female intellectual leadership was possible — if exceptional — within specific institutional contexts, and became a foundational example for 20th-century historians of women in science and medicine.",
      "significanceCategory": "highly-significant"
    }
  }
},

"deng-xi": {
  "filepath": "data/appwrite-export/entities/210-Class-210/210deng-xi.json",
  "slug": "deng-xi",
  "data": {
    "summary": "Deng Xi (c. 545–501 BCE) was a Chinese philosopher, jurist, and rhetorician of the state of Zheng during the Spring and Autumn Period, considered the founding figure of the School of Names (Mingjia) — one of the Hundred Schools of Thought that competed for dominance in pre-Qin intellectual life. He is remembered as the first Chinese thinker to systematise legal argumentation, sophistic debate, and the philosophy of language, earning comparison to the Greek Sophists of roughly the same era. The parallel development of analytic rhetoric in both Greece and China in the 5th century BCE represents one of the most striking instances of the 'axial age' convergence identified by Karl Jaspers.\n\nDeng Xi composed a legal code for Zheng on bamboo strips — the 'bamboo penal code' — which he distributed unofficially to litigants, providing ordinary citizens with the legal knowledge previously monopolised by aristocratic officials. He was famous for arguing both sides of any legal case with equal persuasiveness, exposing the constructed, contingent nature of legal reasoning in a way that outraged conservative Confucian officials who saw his methods as subversive of social order. The prime minister Zichan had him executed in 501 BCE, reportedly the same year Zichan died — though some texts suggest Zichan's successor Zi Tai carried out the execution.\n\nDeng Xi's posthumously collected works — the 'Dengxi zi' — survive in partial form and address the relationship between names and realities (zhengming), argumentation, and political philosophy. His execution for teaching that legal language was malleable rather than fixed represents an early case of the state suppressing philosophical sophistry as politically dangerous — a tension between open-ended inquiry and institutional authority that has recurred throughout intellectual history.",
    "causes": [
      "The collapse of Zhou royal authority during the Spring and Autumn Period created competitive multi-state politics in which Zheng and other states required sophisticated legal and diplomatic reasoning, creating demand for professional argumentation and legal expertise.",
      "The rise of literate non-aristocratic officials and merchants in Chinese city-states created a new audience for legal knowledge previously restricted to the hereditary elite, which Deng Xi addressed by distributing his bamboo penal code.",
      "The broader intellectual ferment of the Hundred Schools of Thought — driven by urbanisation, the breakdown of hereditary authority, and competition between states for talented advisors — provided the cultural context for radical philosophical innovation."
    ],
    "effects": [
      "Deng Xi established the School of Names (Mingjia) tradition that influenced later Chinese philosophy of language, particularly the work of Gongsun Long ('A white horse is not a horse') and the Mohist contributions to proto-logic in the 4th–3rd centuries BCE.",
      "His distribution of a written legal code to non-elite citizens was an early Chinese example of legal democratisation — making law legible to those it governed rather than keeping it as an aristocratic monopoly — a principle that recurred in Chinese legal reform movements.",
      "Deng Xi's execution for his sophistic legal arguments became a canonical case in Chinese intellectual history of the conflict between the free play of reasoning and state authority, cited in discussions of intellectual freedom and the role of the state in controlling thought."
    ],
    "relationships": [
      {"sourceSlug": "deng-xi", "sourceName": "Deng Xi", "verb": "CREATES", "targetSlug": "school-of-names", "targetName": "School of Names (Mingjia)", "context": "Deng Xi is regarded as the founding figure of the Mingjia (School of Names), which analysed the relationship between language, names, and reality in Chinese philosophy."},
      {"sourceSlug": "deng-xi", "sourceName": "Deng Xi", "verb": "INFLUENCES", "targetSlug": "gongsun-long", "targetName": "Gongsun Long", "context": "Gongsun Long's famous paradoxes ('A white horse is not a horse') build on the Mingjia tradition that Deng Xi founded, extending his analysis of names and reality."},
      {"sourceSlug": "zichan", "sourceName": "Zichan of Zheng", "verb": "CAUSES", "targetSlug": "deng-xi", "targetName": "Deng Xi", "context": "Zichan, prime minister of Zheng, ordered Deng Xi's execution in 501 BCE for his subversive legal teachings that undermined official authority by making argumentation a public skill."},
      {"sourceSlug": "hundred-schools-of-thought", "sourceName": "Hundred Schools of Thought", "verb": "CONTAINS", "targetSlug": "deng-xi", "targetName": "Deng Xi", "context": "Deng Xi was one of the earliest and most provocative figures in the Spring and Autumn Period intellectual explosion that produced Confucianism, Taoism, Legalism, and Mohism."}
    ],
    "places": [
      {"name": "State of Zheng, China", "role": "The state where Deng Xi lived and was executed, one of the smaller but culturally significant Spring and Autumn Period kingdoms"},
      {"name": "China (Spring and Autumn Period)", "role": "The broader context of multi-state competition and intellectual ferment that produced the Hundred Schools of Thought"}
    ],
    "subjects": ["Philosophy", "Ancient History", "China", "Law", "Language and Logic", "Classical Era", "Intellectual History", "Political Philosophy"],
    "frameworks": ["COMPARATIVE_CIVILIZATIONS", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Deng Xi founded the Chinese School of Names (Mingjia) and pioneered systematic legal argumentation in 5th-century BCE China — a parallel development to Greek Sophistry that Jaspers identified as part of the 'axial age' of simultaneous philosophical revolutions. His execution for sophistic teaching is an early case of the state suppressing open-ended philosophical reasoning as politically dangerous.",
      "significanceCategory": "significant"
    }
  }
},

"richard-fitzralph": {
  "filepath": "data/appwrite-export/entities/250-Class-250/250richard-fitzralph.json",
  "slug": "richard-fitzralph",
  "data": {
    "summary": "Richard FitzRalph (c. 1300–1360) was the Archbishop of Armagh and one of the most controversial theologians of the 14th century, whose doctrine of 'dominion by grace' (dominium per gratiam) — asserting that all rightful authority and property ownership depended on the holder being in a state of grace — became one of the most consequential theological time-bombs of the medieval period. Born in Dundalk, Ireland, FitzRalph studied and taught at Oxford, became Chancellor of the University, and rose to become Archbishop of Armagh in 1347. His intellectual trajectory took him from a respected mainstream scholastic theologian to a radical polemicist against the mendicant orders, particularly the Franciscans.\n\nHis major work 'De Pauperie Salvatoris' (On the Poverty of the Saviour, c. 1356) argued that the Franciscan claim to 'use without ownership' of property was a legal fiction, and that all property rights derived from divine grace — a position that, taken to its logical conclusion, implied that sinners and unbelievers had no rightful claim to authority or property. This doctrine was seized upon by John Wycliffe, FitzRalph's younger contemporary at Oxford, who radicalised it into the foundation of his attack on clerical wealth and papal authority. Through Wycliffe, FitzRalph's ideas fed directly into Lollardy, the Hussite movement, and ultimately the Protestant Reformation.\n\nFitzRalph was a preacher of extraordinary power — his Latin and English vernacular sermons survive in unusual quantity — and his campaign against the friars' privileges to hear confession and preach brought him to the papal court at Avignon in 1357, where he died in 1360 defending his case. He was widely revered in Ireland as 'Saint Richard of Dundalk' and unofficial veneration continued there despite Rome never canonising him.",
    "causes": [
      "The Franciscan poverty controversy, which had divided the Church since the 1310s with Pope John XXII's condemnation of absolute poverty, created the theological battlefield on which FitzRalph's attack on mendicant property claims was fought.",
      "FitzRalph's pastoral experience as Archbishop of Armagh — observing the mendicant orders undermining parish authority by offering cheap confession and burial — gave his abstract theological arguments concrete pastoral and economic stakes.",
      "Oxford's tradition of rigorous scholastic disputation and FitzRalph's own philosophical training in the Augustinian tradition provided the conceptual tools to develop the 'dominium per gratiam' doctrine into a systematic challenge to established ecclesiastical property arrangements."
    ],
    "effects": [
      "John Wycliffe directly adopted and radicalised FitzRalph's 'dominium per gratiam' doctrine in his 'De Dominio Divino' (c. 1375), using it to argue that corrupt clergy had no rightful authority — the theological foundation of Lollardy and the attack on clerical wealth that influenced the English Reformation.",
      "FitzRalph's vernacular preaching in English and Irish contributed to the tradition of reformist vernacular theology that Wycliffe's Bible translation and Lollard preaching developed, accelerating the transfer of religious authority from Latin clergy to literate laity.",
      "Through Wycliffe to Jan Hus, FitzRalph's ideas formed part of the intellectual chain running from 14th-century Oxford to the Hussite Wars to the Protestant Reformation — one of the most consequential intellectual transmissions in Christian history."
    ],
    "relationships": [
      {"sourceSlug": "richard-fitzralph", "sourceName": "Richard FitzRalph", "verb": "INFLUENCES", "targetSlug": "john-wycliffe", "targetName": "John Wycliffe", "context": "Wycliffe's 'De Dominio Divino' built directly on FitzRalph's 'dominium per gratiam' doctrine, radicalising it into an attack on clerical wealth and papal authority that launched the Lollard movement."},
      {"sourceSlug": "richard-fitzralph", "sourceName": "Richard FitzRalph", "verb": "CHALLENGES", "targetSlug": "franciscans", "targetName": "Franciscan Order", "context": "FitzRalph's 'De Pauperie Salvatoris' (1356) attacked Franciscan poverty claims as legal fiction, triggering a major ecclesiastical controversy that he pursued to the papal court at Avignon."},
      {"sourceSlug": "john-wycliffe", "sourceName": "John Wycliffe", "verb": "INFLUENCES", "targetSlug": "protestant-reformation", "targetName": "Protestant Reformation", "context": "The doctrinal chain from FitzRalph through Wycliffe to Hus to Luther represents one of the clearest intellectual genealogies connecting 14th-century Oxford to the 16th-century Reformation."}
    ],
    "places": [
      {"name": "Oxford, England", "role": "Where FitzRalph studied, taught, and served as Chancellor; the intellectual environment that shaped his scholastic theology"},
      {"name": "Armagh, Ireland", "role": "His archbishopric from 1347; his pastoral experience there shaped his campaign against mendicant privileges"},
      {"name": "Avignon, France", "role": "Where FitzRalph pleaded his case against the friars before the papal court and died in 1360"}
    ],
    "subjects": ["Medieval Theology", "Religious Reform", "Medieval History", "Ireland", "England", "Philosophy", "Church History", "Medieval Era"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Richard FitzRalph's 'dominium per gratiam' doctrine — that all legitimate authority depends on divine grace — was adopted and radicalised by John Wycliffe, whose Lollardy influenced Jan Hus, whose Hussitism influenced Luther. FitzRalph is thus a critical link in the intellectual chain from 14th-century Oxford to the Protestant Reformation, making him one of the most consequential theologians most people have never heard of.",
      "significanceCategory": "highly-significant"
    }
  }
},

"katakalon-kekaumenos": {
  "filepath": "data/appwrite-export/entities/205-Class-205/205katakalon-kekaumenos.json",
  "slug": "katakalon-kekaumenos",
  "data": {
    "summary": "Katakalon Kekaumenos (c. 1000–1065 CE) was one of Byzantium's most distinguished military commanders of the 11th century, a general who served under four emperors and whose career spanned the last great period of Byzantine military expansion before the catastrophic defeat at Manzikert (1071). Born into a distinguished Armenian-Byzantine aristocratic family in the eastern frontier regions, he rose through the military hierarchy to command Byzantine forces in Italy, the Balkans, and the eastern frontier against both the Seljuk Turks and Pecheneg nomads. He is most celebrated for his defence of Edessa against the Arab emir Shibl al-Dawla in 1031 and for his role in repelling the major Pecheneg invasion of 1048–1049.\n\nKatakalon Kekaumenos is probably identical with — or closely related to — the author of the 'Strategikon' (also called 'Varia' or 'Kekaumenos'), a remarkable Byzantine military and political handbook written around 1075–1078. If the identification is correct, the 'Strategikon' represents the hard-won practical wisdom of a frontline general: unsentimental advice to commanders on troop discipline, strategic deception, treatment of prisoners, management of provincial governors, and the behaviour of a loyal servant of the emperor. Its tone is cynical about court politics, protective of provincial autonomy, and deeply concerned with the treachery of colleagues — reflecting the factional instability of the 11th-century Byzantine state.\n\nHis military career intersected with the transformation of the Byzantine frontier: the Macedonian dynasty's aggressive eastern expansion had pushed Byzantine territory to its greatest extent since the 7th century, but the shift to an Armenian-recruited professional army, the neglect of the Anatolian themes (provincial military districts), and the succession crisis after 1056 set the conditions for Manzikert. Katakalon survived to see the empire begin its unravelling — a career that embodies both Byzantium's 11th-century zenith and the seeds of its subsequent decline.",
    "causes": [
      "The Macedonian dynasty's aggressive eastern military expansion in the late 10th century (under Nikephoros Phokas, John Tzimiskes, and Basil II) created a vast reconquered frontier in Armenia, Syria, and Bulgaria that required experienced commanders like Katakalon to defend and administer.",
      "The collapse of the Arab Hamdanid emirate of Aleppo and the rise of Seljuk Turkish pressure from Central Asia created new military threats on the eastern frontier that the Byzantine system met through commanders of Armenian descent familiar with the terrain and peoples of Anatolia.",
      "Byzantine court politics under the civilian emperors of the 1040s–1050s marginalised experienced frontier generals, creating the resentment and political conflict that punctuates Katakalon's career and which the 'Strategikon' reflects with bitter clarity."
    ],
    "effects": [
      "Katakalon's defence of Edessa in 1031 preserved one of Byzantium's most important eastern cities for another generation; its eventual fall to the Crusader states in 1098 and to Zengi in 1144 triggered the Second Crusade, underscoring the strategic importance of the position he had held.",
      "If Katakalon is the author of the 'Strategikon', he left the Byzantine military tradition one of its most practically detailed manuals — a text whose advice on counterinsurgency, negotiation, and provincial administration reflects hard operational experience and continues to be studied by historians of Byzantine warfare.",
      "Katakalon's career exemplifies the Armenian military aristocracy's critical role in 11th-century Byzantine power: their expertise, loyalty, and eventual marginalisation by civilian court factions was a structural factor in the military failure that led to Manzikert and the loss of Anatolia."
    ],
    "relationships": [
      {"sourceSlug": "katakalon-kekaumenos", "sourceName": "Katakalon Kekaumenos", "verb": "OCCURS_IN", "targetSlug": "byzantine-empire", "targetName": "Byzantine Empire", "context": "Katakalon served the Byzantine Empire for four decades under Emperors Romanos III, Michael IV, Constantine IX, and Isaac I Komnenos, commanding forces on all major fronts."},
      {"sourceSlug": "katakalon-kekaumenos", "sourceName": "Katakalon Kekaumenos", "verb": "CREATES", "targetSlug": "strategikon-kekaumenos", "targetName": "Strategikon (Kekaumenos)", "context": "The 'Strategikon' attributed to Kekaumenos (c. 1075–1078) is a practical military and political handbook that encapsulates the experience of a frontier commander disillusioned with court politics."},
      {"sourceSlug": "battle-of-manzikert", "sourceName": "Battle of Manzikert (1071)", "verb": "FOLLOWS", "targetSlug": "katakalon-kekaumenos", "targetName": "Katakalon Kekaumenos", "context": "Manzikert, fought six years after Katakalon's career peak, resulted from the systemic failures in Byzantine frontier defence and military governance that his 'Strategikon' implicitly diagnoses."},
      {"sourceSlug": "seljuk-turks", "sourceName": "Seljuk Turks", "verb": "CHALLENGES", "targetSlug": "katakalon-kekaumenos", "targetName": "Katakalon Kekaumenos", "context": "The expanding Seljuk Empire was the primary eastern military challenge Katakalon faced in the 1040s–1060s on the Anatolian frontier."}
    ],
    "places": [
      {"name": "Edessa (Şanlıurfa, Turkey)", "role": "Byzantine frontier city that Katakalon defended against the Arab emir Shibl al-Dawla in 1031 — one of his most celebrated victories"},
      {"name": "Balkans / Bulgaria", "role": "Theatre of Katakalon's operations against Pecheneg nomads in 1048–1049, repelling a major invasion that threatened the Danube frontier"},
      {"name": "Southern Italy", "role": "Where Katakalon commanded Byzantine forces against the Normans in the 1040s, part of the multi-front strategic challenge of mid-11th century Byzantium"}
    ],
    "subjects": ["Byzantine History", "Military History", "Medieval History", "Anatolia", "Near East", "Political Strategy", "Medieval Era"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "DIPLOMATIC_HISTORY", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Katakalon Kekaumenos was one of Byzantium's most capable 11th-century frontier commanders, and may be the author of the 'Strategikon' — a uniquely frank Byzantine military handbook that illuminates the practical realities of Byzantine warfare and the court politics that undermined imperial defence. His career sits at the fulcrum of Byzantine power, between the 10th-century zenith and the catastrophe of Manzikert.",
      "significanceCategory": "significant"
    }
  }
}

}  # end ENRICHMENTS

# ─────────────────────────────────────────────────────────────────────────────
# Runtime
# ─────────────────────────────────────────────────────────────────────────────

def get_entity_from_file(filepath, slug):
    """Load the entity dict from the file. Returns (entity_dict, all_data)."""
    with open(filepath) as f:
        data = json.load(f)
    entities = data.get("entities", [])
    for e in entities:
        if e.get("slug") == slug:
            return e, data
    return None, data


def apply_enrichment(filepath, slug, enrichment_data, dry_run=False):
    entity, data = get_entity_from_file(filepath, slug)
    if entity is None:
        print(f"  ERROR: slug '{slug}' not found in {filepath}")
        return False

    # Parse existing detailsJson
    raw_details = entity.get("detailsJson", "{}")
    if isinstance(raw_details, dict):
        details = raw_details
    else:
        details = json.loads(raw_details or "{}")

    old_summary_len = len(details.get("summary", "") or "")
    if old_summary_len >= 800:
        print(f"  SKIP — already enriched ({old_summary_len}c)")
        return False

    if dry_run:
        new_len = len(enrichment_data.get("summary", ""))
        print(f"  DRY RUN — would enrich {old_summary_len}c → {new_len}c")
        return True

    # Merge enrichment data into detailsJson
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    for key, val in enrichment_data.items():
        if key == "historicalSignificance":
            details["historicalSignificance"] = val
        else:
            details[key] = val

    # Build edit log entry
    edit_log = details.get("_editLog", [])
    edit_log.append({
        "field": "summary",
        "editorId": EDITOR_ID,
        "sessionId": SESSION_ID,
        "timestamp": now,
        "oldValue": "",
        "newValue": enrichment_data.get("summary", "")[:200] + "…"
    })
    details["_editLog"] = edit_log

    entity["detailsJson"] = details
    entity["_unsyncedEdits"] = True

    # Write back
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    new_len = len(enrichment_data.get("summary", ""))
    print(f"  ENRICHED — {old_summary_len}c → {new_len}c")
    return True


def main():
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("** DRY RUN — no files will be modified **\n")

    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    enriched = 0
    skipped = 0
    errors = 0

    for slug, spec in ENRICHMENTS.items():
        filepath = os.path.join(repo_root, spec["filepath"])
        print(f"\n[{slug}]")
        if not os.path.exists(filepath):
            print(f"  ERROR: file not found: {filepath}")
            errors += 1
            continue
        ok = apply_enrichment(filepath, slug, spec["data"], dry_run=dry_run)
        if ok:
            enriched += 1
        else:
            skipped += 1

    print(f"\n{'=' * 60}")
    print(f"RESULTS: {enriched} enriched, {skipped} skipped, {errors} errors")
    if not dry_run and enriched > 0:
        print(f"\nNext steps:")
        print(f"  1. Commit: git add data/appwrite-export/entities/ && git commit -m 'enrichment: vscode batch 03 — {enriched} entities'")
        print(f"  2. Sync:   APPWRITE_API_KEY=<key> npx tsx scripts/sync_gateway.ts --local")


if __name__ == "__main__":
    main()
