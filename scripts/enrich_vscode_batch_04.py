#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 04 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: empire, assyrian-empire, charlotte-guillard, john-of-rokycan,
          guala-bicchieri, cristoforo-landino, peter-shafirov, pantaenus
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-04-may2026"

ENRICHMENTS = {

"empire": {
  "filepath": "data/appwrite-export/entities/012-Class-012/012empire.json",
  "slug": "empire",
  "data": {
    "summary": "Empire — as a political form — is the organisation of diverse peoples, territories, and polities under a single sovereign power that typically exercises authority beyond the borders of the dominant ethnic or political core. The word derives from the Latin 'imperium' (command, authority), formalised in Rome's transformation from republic to principate under Augustus in 27 BCE, but the imperial form far predates this Latin coinage: the Akkadian Empire under Sargon of Akkad (c. 2334 BCE) is the first documented example in which a single ruler claimed sovereignty over multiple city-states and ethnic groups across a contiguous territory.\n\nHistorically, empires have been the dominant organisational form of large-scale human society. The Achaemenid Persian Empire (550–330 BCE) administered 50 million people across 5.5 million square kilometres using a sophisticated system of satrapies, royal roads, and a lingua franca (Aramaic) — representing perhaps 44% of the world's population at its peak. The Roman Empire (27 BCE–476 CE in the West; 1453 in the East) unified the Mediterranean world under a single legal system, currency, and network of roads that persisted as the skeleton of European civilisation long after the empire's fall. The Mongol Empire (1206–1368) became the largest contiguous land empire in history at 24 million km², connecting Eurasia from Korea to Hungary under the Pax Mongolica. The British Empire (1583–1997) at its peak controlled 24% of the world's land and 23% of the global population — the largest empire in history by territorial extent.\n\nThe concept of empire encodes a fundamental tension: between the order, infrastructure, and legal frameworks that large-scale administration provides (roads, currency, law, trade routes) and the violence, displacement, and cultural destruction through which empires are built and maintained. Postcolonial scholars since Frantz Fanon and Edward Said have documented how empire's material legacies — from the borders drawn by European colonial administrators to the economic dependencies created by colonial extraction — continue to shape global inequality in the 21st century. The 20th century saw both the climax (British, French, Dutch, Belgian empires at their height) and the collapse of formal empires as decolonisation movements dismantled colonial structures after World War II.",
    "causes": [
      "Agricultural surplus economies created the material conditions for large-scale state formation: the ability to feed professional armies, scribal bureaucracies, and administrative hierarchies without the entire population being engaged in subsistence production.",
      "Military technology asymmetries — chariots in the Bronze Age, iron weapons in the Classical era, gunpowder artillery in the Early Modern period — repeatedly enabled technologically superior groups to subordinate larger populations.",
      "Trade route control provided the economic logic for imperial expansion: empires from Persia to Rome to the British East India Company were built on the extraction of surplus from the territories they connected and administered."
    ],
    "effects": [
      "Empires created the infrastructure of civilisation — roads, legal systems, currencies, scripts, and religious frameworks — that outlasted their political forms: Roman law underlies every Western legal system; Persian administrative models were adopted by Alexander, the Seleucids, the Parthians, and the Sassanids in succession.",
      "Imperial connectivity produced the most significant episodes of cultural and biological exchange in history — the Silk Road under the Pax Mongolica, the Columbian Exchange under Spanish and Portuguese empire, the global circulation of crops, diseases, languages, and religions under European colonial empires.",
      "Decolonisation movements (1945–1980) dissolved formal empire but left structural legacies — arbitrary borders, export-commodity economies, language hierarchies, ethnic conflict — that postcolonial states continue to negotiate in the 21st century."
    ],
    "relationships": [
      {"sourceSlug": "empire", "sourceName": "Empire", "verb": "DEFINES", "targetSlug": "roman-empire", "targetName": "Roman Empire", "context": "The Roman Empire is the paradigmatic case from which the Latin 'imperium' gave the concept its name and provided the template for subsequent Western ideas of universal sovereign authority."},
      {"sourceSlug": "empire", "sourceName": "Empire", "verb": "DEFINES", "targetSlug": "british-empire", "targetName": "British Empire", "context": "The British Empire was the largest empire in history by territorial extent, ruling 24% of the world's land at its 1920s peak and shaping the modern world's political geography through its decolonisation."},
      {"sourceSlug": "empire", "sourceName": "Empire", "verb": "DEFINES", "targetSlug": "mongol-empire", "targetName": "Mongol Empire", "context": "The Mongol Empire (1206–1368) was the largest contiguous land empire in history, connecting Eurasia and enabling the Pax Mongolica that facilitated unprecedented trade and cultural exchange."},
      {"sourceSlug": "empire", "sourceName": "Empire", "verb": "INFLUENCES", "targetSlug": "postcolonial-analysis", "targetName": "Postcolonial Theory", "context": "Postcolonial scholarship — Fanon, Said, Spivak — theorises how imperial structures created enduring asymmetries of power, knowledge, and economic development that persist after formal decolonisation."},
      {"sourceSlug": "sargon-of-akkad", "sourceName": "Sargon of Akkad", "verb": "CREATES", "targetSlug": "empire", "targetName": "Empire", "context": "Sargon of Akkad (c. 2334 BCE) created the first documented empire by conquering the Sumerian city-states and unifying Mesopotamia under a single sovereign — the founding instance of the imperial form."}
    ],
    "places": [
      {"name": "Rome, Italy", "role": "The city whose 'imperium' gave empire its name and whose political model defined Western conceptions of universal sovereign authority"},
      {"name": "Persepolis, Iran", "role": "Ceremonial capital of the Achaemenid Empire, which at its peak in 480 BCE administered 44% of the world's population across 5.5 million km²"},
      {"name": "London, England", "role": "Capital of the British Empire — the largest empire in history — whose decolonisation after 1945 reshaped the modern world's political map"}
    ],
    "subjects": ["Political Theory", "World History", "Imperialism", "Colonialism", "State Formation", "Global History", "Classical Era", "Ideas", "Power and Authority"],
    "frameworks": ["WORLD_SYSTEMS", "POSTCOLONIAL_ANALYSIS", "STRUCTURAL_ANALYSIS", "LONGUE_DUREE"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "Empire is the dominant political form of recorded history — from the Akkadian Empire of 2334 BCE to the British Empire's collapse in the 20th century. Empires created the roads, laws, currencies, religions, and linguistic frameworks that constitute the shared infrastructure of civilisation. The question of how empires are built, maintained, and what they leave behind defines much of world history and remains central to understanding contemporary global inequality.",
      "significanceCategory": "world-changing"
    }
  }
},

"assyrian-empire": {
  "filepath": "data/appwrite-export/entities/430-Class-430/430assyrian-empire.json",
  "slug": "assyrian-empire",
  "data": {
    "summary": "The Assyrian Empire — more precisely the Neo-Assyrian Empire (911–609 BCE) — was the first true world empire in the ancient Near East: a military superpower that at its height under Esarhaddon and Ashurbanipal (680–627 BCE) dominated territory from Egypt and the Levant through Mesopotamia to western Iran, imposing centralised administration, systematic tribute extraction, and unprecedented mass deportation on subject peoples. The Assyrians built the ancient world's first professional standing army, equipped with iron weapons, siege engines, and cavalry, and employed terror — mass execution, impalement, city destruction — as a deliberate instrument of imperial policy, recorded in graphic detail on their palace wall reliefs.\n\nThe Neo-Assyrian state was also a centre of extraordinary intellectual achievement. Ashurbanipal's library at Nineveh — discovered in 1853 and now in the British Museum — contained over 30,000 clay tablets representing the most systematic collection of Mesopotamian knowledge in antiquity: astronomical observations, medical texts, omen literature, the Gilgamesh Epic, and royal annals. This library is the primary source for our knowledge of Babylonian and Sumerian literature and science. Assyrian administrative innovation — the use of Aramaic as a lingua franca across a multilingual empire, the postal relay system, the royal road network, the provincial governor system — directly influenced the subsequent Persian Achaemenid Empire and, through it, Alexander the Great's administrative methods.\n\nThe empire's fall was as dramatic as its rise. An alliance of the Babylonians under Nabopolassar and the Medes under Cyaxares sacked Nineveh in 612 BCE, fulfilling the prophecy in the Hebrew Bible (Nahum 3:7: 'Nineveh is laid waste: who will bemoan her?'). Within three years the entire Assyrian state had ceased to exist — the fastest and most complete collapse of a major ancient empire on record. The ruins of Nineveh, Nimrud, and Khorsabad in modern Iraq have been systematically damaged by ISIL since 2015, making Ashurbanipal's library tablets in the British Museum the primary surviving record of a civilisation.",
    "causes": [
      "Iron Age metallurgy gave Assyria decisive military advantage over Bronze Age polities: iron weapons were cheaper, harder, and more widely available than bronze, enabling the creation of a large professional army that no neighbouring state could match.",
      "Assyria's geographic position at the Tigris-Euphrates junction — the crossroads of Near Eastern trade routes — gave it both the economic surplus to sustain a professional military state and the strategic motivation to control surrounding territories.",
      "The collapse of the Late Bronze Age international system around 1200 BCE eliminated the major competing powers (Hittites, Mycenaean Greece, Egypt's New Kingdom) and created the political vacuum into which Assyrian expansionism moved during the 10th–9th centuries BCE."
    ],
    "effects": [
      "Assyrian administrative innovations — the provincial governor system, Aramaic lingua franca, royal road network, and systematic deportation as population management — were directly inherited by the Achaemenid Persian Empire, which applied them across an even larger territory.",
      "Ashurbanipal's library at Nineveh preserved the majority of surviving Mesopotamian literature and scientific knowledge; without it, the Epic of Gilgamesh, the astronomical canon, and most Babylonian omen texts would be entirely unknown.",
      "Assyrian mass deportations — including the Northern Kingdom of Israel (722 BCE, the 'Ten Lost Tribes') — permanently reshaped the ethnic and religious geography of the Near East and generated the Biblical literature that became foundational to Jewish, Christian, and Islamic tradition."
    ],
    "relationships": [
      {"sourceSlug": "assyrian-empire", "sourceName": "Assyrian Empire", "verb": "PRODUCES", "targetSlug": "ashurbanipals-library", "targetName": "Ashurbanipal's Library", "context": "Ashurbanipal's library at Nineveh (c. 650 BCE) contained 30,000+ clay tablets — the ancient world's most comprehensive archive and the primary source for Mesopotamian literature and science."},
      {"sourceSlug": "assyrian-empire", "sourceName": "Assyrian Empire", "verb": "INFLUENCES", "targetSlug": "achaemenid-empire", "targetName": "Achaemenid Persian Empire", "context": "The Persians inherited Assyrian administrative structures — provincial governors (satraps), the royal road network, Aramaic as administrative language — when Cyrus the Great absorbed former Assyrian territories."},
      {"sourceSlug": "assyrian-empire", "sourceName": "Assyrian Empire", "verb": "CAUSES", "targetSlug": "babylonian-captivity", "targetName": "Babylonian Captivity", "context": "The Assyrian deportation of the Northern Kingdom of Israel in 722 BCE (the 'Ten Lost Tribes') and subsequent Babylonian deportation of Judah (586 BCE) created the diaspora conditions that shaped the Hebrew Bible."},
      {"sourceSlug": "medes", "sourceName": "Medes", "verb": "DESTROYS", "targetSlug": "assyrian-empire", "targetName": "Assyrian Empire", "context": "A Median-Babylonian alliance sacked Nineveh in 612 BCE, destroying the Assyrian heartland and ending the empire within three years — the fastest collapse of a major ancient empire."},
      {"sourceSlug": "ashurbanipal", "sourceName": "Ashurbanipal", "verb": "DEFINES", "targetSlug": "assyrian-empire", "targetName": "Assyrian Empire", "context": "Ashurbanipal (r. 668–627 BCE) represented the apogee of Assyrian power — ruling from Egypt to Iran — while simultaneously commissioning the library that preserved Mesopotamian civilisation's intellectual legacy."}
    ],
    "places": [
      {"name": "Nineveh, Iraq", "role": "Capital of the Neo-Assyrian Empire; site of Ashurbanipal's library; sacked by the Medes and Babylonians in 612 BCE"},
      {"name": "Nimrud, Iraq", "role": "Earlier Assyrian capital under Ashurnasirpal II; site of extraordinary palace reliefs and ivory carvings"},
      {"name": "Israel/Palestine", "role": "Subject territory conquered by Sargon II in 722 BCE; deportation of the Northern Kingdom generated the 'Ten Lost Tribes' tradition"}
    ],
    "subjects": ["Ancient History", "Military History", "Mesopotamia", "Archaeology", "State Formation", "Near East", "Classical Era", "Imperialism"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT", "WORLD_SYSTEMS"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Neo-Assyrian Empire was the ancient world's first genuine superpower — the template for all subsequent Near Eastern empires. Its administrative innovations (provincial governors, Aramaic lingua franca, royal roads) were inherited by Persia, Alexander, and Rome. Ashurbanipal's library preserved Mesopotamian civilisation's intellectual heritage; without it, the Epic of Gilgamesh and most Babylonian literature would be lost. Its deportation of Israel's Northern Kingdom in 722 BCE generated biblical traditions that shaped three world religions.",
      "significanceCategory": "world-changing"
    }
  }
},

"charlotte-guillard": {
  "filepath": "data/appwrite-export/entities/202-Class-202/202charlotte-guillard.json",
  "slug": "charlotte-guillard",
  "data": {
    "summary": "Charlotte Guillard (c. 1485–1557) was the first and most significant female master printer in France — a woman who operated one of the most prestigious printing houses in Paris for over three decades and who independently managed a commercially and intellectually elite publishing enterprise at a time when women were legally barred from most trades. She ran the Soleil d'Or (Golden Sun) printing house in the Rue Saint-Jacques — the heart of Paris's book trade — first as the widow of her first husband Berthold Rembolt, then after 1519 as the independent proprietor, and finally in partnership with her second husband Claude Chevallon. After Chevallon's death in 1537, she ran the press alone for the final twenty years of her active career, producing some of the finest scholarly typography of 16th-century France.\n\nGuillard's press specialised in the high-end scholarly market: patristic texts, Greek and Latin classics, legal works, and theological commentaries. Her editions of the Church Fathers — Origen, Cyprian, Tertullian, John Chrysostom — were produced to the highest typographic and editorial standards, using quality paper, elegant typefaces, and scholarly apparatus. Her press printed for the Collège de France and worked with leading humanist scholars of the Paris establishment, including Guillaume Budé. At a moment when France was navigating the turbulence of the early Reformation, Guillard's patristic programme aligned her with the Erasmian reform current — a scholarly Catholicism that sought renewal through textual scholarship rather than Lutheran rupture.\n\nThe historical recovery of Charlotte Guillard's career in the 20th century transformed the history of early printing: she demonstrated that women were not merely passive inheritors of husbands' print shops but active, commercially sophisticated operators who shaped the intellectual programme of their presses. Her long independent career — two decades as sole proprietor after Chevallon's death — makes her exceptional even among the significant group of 16th-century widow-printers.",
    "causes": [
      "The Parisian printing trade's guild structure allowed widows to inherit and continue their husbands' businesses, providing the legal opening through which Charlotte first inherited Rembolt's press and later operated independently — a narrow but real space within an otherwise male-dominated trade.",
      "The expansion of the humanist scholarly book market in 16th-century Paris created demand for high-quality editions of Greek, Latin, and patristic texts that required both commercial acumen and scholarly judgment — skills that Charlotte demonstrably possessed.",
      "The death of Claude Chevallon in 1537, combined with Charlotte's twenty years of operational experience, gave her both the necessity and the competence to run the Soleil d'Or independently — her subsequent two decades of sole proprietorship were the most distinctive phase of her career."
    ],
    "effects": [
      "Charlotte Guillard's press produced some of the finest scholarly editions of the French Renaissance, contributing to the humanist programme of editing and distributing patristic and classical texts that shaped Catholic reform in France before the Council of Trent.",
      "Her career became a key example in 20th-century feminist historiography of printing and publishing, demonstrating that women's participation in the early book trade was substantive and commercially independent, not merely nominal or auxiliary.",
      "Her association with the Collège de France and leading humanists helped establish the Rue Saint-Jacques as the centre of serious scholarly publishing in Paris — a typographic geography that persisted for centuries."
    ],
    "relationships": [
      {"sourceSlug": "charlotte-guillard", "sourceName": "Charlotte Guillard", "verb": "PRODUCES", "targetSlug": "patristic-literature", "targetName": "Patristic Literature", "context": "Guillard's press produced scholarly editions of Origen, Cyprian, Tertullian, and John Chrysostom — patristic texts central to the humanist Catholic reform programme of 16th-century France."},
      {"sourceSlug": "charlotte-guillard", "sourceName": "Charlotte Guillard", "verb": "OCCURS_IN", "targetSlug": "french-renaissance", "targetName": "French Renaissance", "context": "Guillard operated during the height of French humanism, working with scholars connected to the Collège de France and aligning her press with the Erasmian reform tradition."},
      {"sourceSlug": "gutenberg-press", "sourceName": "Printing Press", "verb": "ENABLES", "targetSlug": "charlotte-guillard", "targetName": "Charlotte Guillard", "context": "The printing press, introduced to Paris in 1470, created the industry in which Guillard built her career — transforming manuscript culture into a commercial book trade accessible to women as well as men through guild widow-rights."}
    ],
    "places": [
      {"name": "Paris, France (Rue Saint-Jacques)", "role": "Location of the Soleil d'Or press — the centre of Paris's scholarly book trade — where Guillard operated for over thirty years"},
      {"name": "France", "role": "The broader context of French humanism and early Reformation pressure that shaped Guillard's patristic publishing programme"}
    ],
    "subjects": ["Women's History", "Early Modern History", "Publishing", "Printing", "France", "Humanism", "Book Trade", "Medieval Era", "Feminist History"],
    "frameworks": ["FEMINIST_PERSPECTIVE", "CULTURAL_TRANSMISSION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Charlotte Guillard was the first female master printer in France and the most significant woman in the early European print trade — operating one of Paris's most prestigious scholarly presses for over three decades, including twenty years as sole proprietor. Her career demonstrates that women could be commercially sophisticated and intellectually ambitious agents in the early book trade, challenging the assumption that the print revolution was exclusively a male project.",
      "significanceCategory": "highly-significant"
    }
  }
},

"john-of-rokycan": {
  "filepath": "data/appwrite-export/entities/210-Class-210/210john-of-rokycan.json",
  "slug": "john-of-rokycan",
  "data": {
    "summary": "Jan Rokycana (c. 1396–1471) was the elected Archbishop of Prague and the spiritual and political leader of the Hussite Utraquist church in Bohemia for over four decades — a man who walked the impossible tightrope between the radical Hussites who had won Bohemia's religious independence and the Catholic Church that refused to recognise either him or the Compactata of Basel (1436) that granted Bohemians communion in both kinds (sub utraque specie). He was elected Archbishop by the Bohemian Diet in 1435 but never received papal confirmation, remaining an elected-but-unconfirmed archbishop for the last thirty-six years of his life — a perpetual thorn in Rome's side and a symbol of Bohemia's anomalous status as a semi-heretical kingdom tolerated within Christendom.\n\nRokycana's theological position was characteristically Czech: a moderate reformism that insisted on utraquism (communion in both kinds for the laity), preaching in Czech, and clerical reform, but rejected the more radical Taborite positions on the Eucharist, clerical celibacy, and purgatory. He was a brilliant preacher whose vernacular Czech sermons drew enormous congregations to the Týn Church in Prague. His long episcopal career — from the Council of Basel negotiations to the reign of King George of Poděbrady (whom he crowned and counselled) — made him the effective head of an independent national church decades before the Lutheran Reformation created institutional precedents for such a thing.\n\nRokycana's most consequential act may have been his influence on a young Bohemian nobleman: Peter Chelčický's radical pacifism and Rokycana's own moderate reform sermons together inspired the founding of the Unity of Brethren (Unitas Fratrum) in 1457, a community that eventually evolved into the Moravian Church — one of the oldest Protestant denominations — and profoundly influenced the 18th-century Evangelical revival through Count Zinzendorf's Herrnhut community.",
    "causes": [
      "The Council of Basel's Compactata (1436) acknowledged Bohemian utraquism but the papacy's subsequent repudiation of the Compactata left Rokycana's position in permanent canonical ambiguity — elected archbishop by Bohemians, rejected by Rome — making him the focal point of Bohemia's anomalous religious situation.",
      "The Hussite Wars (1419–1434) had established Bohemia's military capacity to resist Catholic suppression, creating the political space for a generation of Hussite religious leaders like Rokycana to consolidate a de facto independent church despite papal non-recognition.",
      "King George of Poděbrady's rise to power in Bohemia (1458–1471) provided Rokycana with royal political protection that allowed him to function as de facto archbishop despite Rome's refusal to confirm him."
    ],
    "effects": [
      "Rokycana's sermons and the intellectual atmosphere of his Prague church inspired the founding of the Unity of Brethren (Unitas Fratrum) in 1457 — the ancestor of the Moravian Church — making him an indirect founder of one of the oldest surviving Protestant denominations.",
      "Rokycana's thirty-six-year tenure as unconfirmed archbishop established the practical model of a national church operating outside papal jurisdiction decades before Luther, demonstrating that an organised Christian community could sustain itself without Roman confirmation.",
      "The Unity of Brethren that Rokycana indirectly inspired influenced John Wesley's Methodism in the 18th century and John Amos Comenius's educational philosophy — making Rokycana a distant but traceable ancestor of both Protestant Pietism and modern educational reform."
    ],
    "relationships": [
      {"sourceSlug": "jan-hus", "sourceName": "Jan Hus", "verb": "INSPIRES", "targetSlug": "john-of-rokycan", "targetName": "Jan Rokycana", "context": "Hus's martyrdom at Constance (1415) and his theological reform programme were the direct inspiration for Rokycana's lifelong commitment to Hussite utraquism and vernacular preaching."},
      {"sourceSlug": "john-of-rokycan", "sourceName": "Jan Rokycana", "verb": "INFLUENCES", "targetSlug": "unity-of-brethren", "targetName": "Unity of Brethren", "context": "Rokycana's reform preaching, combined with Peter Chelčický's radical pacifism, inspired the founding of the Unity of Brethren (Unitas Fratrum) in 1457 — the ancestor of the Moravian Church."},
      {"sourceSlug": "unity-of-brethren", "sourceName": "Unity of Brethren", "verb": "INFLUENCES", "targetSlug": "protestant-reformation", "targetName": "Protestant Reformation", "context": "The Unity of Brethren founded in Rokycana's orbit was a proto-Protestant denomination that predated the Lutheran Reformation and influenced subsequent Evangelical and Pietist movements."},
      {"sourceSlug": "council-of-basel", "sourceName": "Council of Basel", "verb": "DEFINES", "targetSlug": "john-of-rokycan", "targetName": "Jan Rokycana", "context": "The Council of Basel's Compactata (1436) created the legal framework for Rokycana's anomalous position — recognised by Bohemia, rejected by Rome — that defined his entire episcopal career."}
    ],
    "places": [
      {"name": "Prague, Bohemia (Czech Republic)", "role": "Centre of Rokycana's ministry; Týn Church was his primary pulpit and St Vitus Cathedral his seat as elected archbishop"},
      {"name": "Basel, Switzerland", "role": "Site of the Council that negotiated the Compactata recognising Bohemian utraquism — the ecclesiastical settlement Rokycana spent his career defending"}
    ],
    "subjects": ["Medieval Theology", "Religious Reform", "Medieval History", "Bohemia", "Central Europe", "Church History", "Hussite Movement", "Medieval Era"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Jan Rokycana led the Hussite Utraquist church for forty years as an unconfirmed archbishop — demonstrating that a national church could operate outside papal jurisdiction a full eighty years before Luther. His influence directly generated the Unity of Brethren (1457), ancestor of the Moravian Church, and his example was a critical link in the intellectual chain from the Hussite movement to the Protestant Reformation.",
      "significanceCategory": "highly-significant"
    }
  }
},

"guala-bicchieri": {
  "filepath": "data/appwrite-export/entities/220-Class-220/220guala-bicchieri.json",
  "slug": "guala-bicchieri",
  "data": {
    "summary": "Guala Bicchieri (c. 1150–1227) was an Italian cardinal and papal legate whose career represents the intersection of ecclesiastical diplomacy, crusade organisation, and constitutional history at a critical moment in medieval Europe. Born in Vercelli in northern Italy, he served Pope Innocent III and Pope Honorius III with exceptional effectiveness across a thirty-year career as the papacy's most trusted negotiator in the contentious politics of France, England, and the Albigensian Crusade. His most consequential appointment came in 1216, when Honorius III sent him to England as papal legate to support the nine-year-old King Henry III and the royalist cause against the First Barons' War.\n\nGuala's tenure in England (1216–1219) coincided with one of the most critical moments in English constitutional history. He arrived immediately after King John's death (October 1216) and personally presided over the coronation of the child Henry III. Crucially, it was under Guala's authority and co-signature that the revised Magna Carta of 1216 — and its even more significant 1217 reissue — were promulgated. While William Marshal provided the military leadership against the rebel barons and their French allies, Guala provided the ecclesiastical legitimation: he excommunicated the rebel barons, placed England under interdict against Louis of France, and co-sealed the charters that entrenched Magna Carta as a permanent constitutional document rather than a failed peace treaty. Without Guala's intervention, Magna Carta might have remained a one-time concession; his reissues transformed it into a constitutional precedent.\n\nAfter his English legation, Guala returned to Italy and founded the Abbey of Sant'Andrea in Vercelli in 1219 — a major Augustinian house built partly with English revenues, still standing and housing Guala's tomb. He attended the Fourth Lateran Council, served in the Albigensian Crusade, and died in 1227 as a senior figure of the 13th-century Church.",
    "causes": [
      "King John's catastrophic loss of the baronial confidence that produced the original Magna Carta (1215) and his death in October 1216 left England with a nine-year-old king and a baronial rebellion supported by French invasion — creating the emergency that required papal intervention.",
      "The papacy's feudal overlordship of England — John had submitted England as a papal fief to Innocent III in 1213 to resolve the interdict crisis — gave Guala the formal authority to intervene in English politics and claim co-authority over the Magna Carta reissues.",
      "Pope Honorius III's trust in Guala as his most experienced diplomatic operative, built through previous legations in France and against the Albigensian heretics, made him the natural choice for the politically complex English appointment."
    ],
    "effects": [
      "Guala's co-signature and ecclesiastical authority legitimised the 1216 and 1217 reissues of Magna Carta, transforming what had been a failed peace treaty between John and his barons into a repeatable constitutional document — the foundation of English constitutional law.",
      "The resolution of the First Barons' War under Guala's legation established Henry III's throne, which provided the stability under which English common law, parliamentary institutions, and judicial independence developed through the 13th century.",
      "Guala's foundation of Sant'Andrea in Vercelli (1219), modelled partly on English Gothic architecture he had encountered during his legation, was an early vehicle for the transmission of English Gothic style to Italy."
    ],
    "relationships": [
      {"sourceSlug": "guala-bicchieri", "sourceName": "Guala Bicchieri", "verb": "DEFINES", "targetSlug": "magna-carta", "targetName": "Magna Carta", "context": "Guala co-signed and legitimised the 1216 and 1217 reissues of Magna Carta that transformed it from a failed baronial peace treaty into a permanent constitutional document."},
      {"sourceSlug": "guala-bicchieri", "sourceName": "Guala Bicchieri", "verb": "OCCURS_IN", "targetSlug": "first-barons-war", "targetName": "First Barons' War", "context": "Guala served as papal legate throughout the First Barons' War (1215–1217), excommunicating rebel barons and providing ecclesiastical authority to the royalist cause led by William Marshal."},
      {"sourceSlug": "pope-honorius-iii", "sourceName": "Pope Honorius III", "verb": "SENDS", "targetSlug": "guala-bicchieri", "targetName": "Guala Bicchieri", "context": "Honorius III appointed Guala as papal legate to England in 1216, trusting him to stabilise the kingdom after John's death and protect Henry III's claim against baronial and French challenge."}
    ],
    "places": [
      {"name": "England", "role": "Theatre of Guala's legation (1216–1219); where he co-signed the Magna Carta reissues that established its constitutional permanence"},
      {"name": "Vercelli, Italy", "role": "Guala's hometown and site of the Abbey of Sant'Andrea he founded in 1219, partly with English revenues from his legation"},
      {"name": "Rome / Avignon", "role": "Base of the papal curia from which Guala operated across his legations to France, England, and the Albigensian territories"}
    ],
    "subjects": ["Medieval History", "Constitutional History", "Church History", "England", "Papal Diplomacy", "Medieval Era", "Law", "Italy"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "DIPLOMATIC_HISTORY", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Guala Bicchieri's co-signing of the 1216 and 1217 Magna Carta reissues under his authority as papal legate was the act that transformed Magna Carta from a failed one-time concession into a constitutional precedent. Without Guala's ecclesiastical legitimation of the post-John regency, the document that became the foundation of English constitutional law might have remained a historical footnote.",
      "significanceCategory": "highly-significant"
    }
  }
},

"cristoforo-landino": {
  "filepath": "data/appwrite-export/entities/210-Class-210/210cristoforo-landino.json",
  "slug": "cristoforo-landino",
  "data": {
    "summary": "Cristoforo Landino (1424–1498) was a Florentine humanist, poet, and professor whose career at the University of Florence made him one of the central intellectual figures of Laurentian Florence — the circle around Lorenzo de' Medici that represented the high-water mark of Italian Renaissance humanism. A professor of rhetoric and poetics at the Studio Fiorentino for over four decades, Landino was both a practising poet and a theorist of literature who bridged Platonic philosophy, Virgilian allegory, and vernacular Italian poetry with unusual range. He is best known for his monumental commentary on Dante's Divina Commedia (1481) and his Italian translation of Pliny's Natural History.\n\nLandino's 'Disputationes Camaldulenses' (c. 1474) — a philosophical dialogue set in the Camaldolese monastery above Florence — presents Platonic discussions of the contemplative versus active life featuring Lorenzo de' Medici, Leon Battista Alberti, and other luminaries of the Florentine circle. The work synthesises Neoplatonic philosophy, Virgilian allegory, and Ciceronian rhetoric into a distinctively Florentine humanist vision of the good life, and is one of the finest examples of the dialogue form in Renaissance literature. His commentary on Virgil's Aeneid interpreted the poem as a Neoplatonic allegory of the soul's ascent — an approach that influenced subsequent allegorical literary criticism.\n\nLandino's Dante commentary of 1481 — illustrated by Sandro Botticelli in its first printed edition — established the interpretive framework for reading Dante as a philosophical and theological poet rather than merely a political or historical one. This edition was one of the great achievements of early Italian printing, combining Landino's scholarly apparatus with Botticelli's engraved maps of Hell. Through his teaching, commentary, and dialogue writing, Landino transmitted Florentine Neoplatonism to subsequent generations of Italian and European humanists.",
    "causes": [
      "The Medici patronage system in 15th-century Florence created the economic and intellectual conditions for humanist scholars like Landino to pursue careers combining university teaching, private tutoring of elite families, and original scholarship without purely commercial constraint.",
      "The arrival of Greek scholars in Florence after the Council of Florence (1439) — including Gemistos Plethon — catalysed the Platonic Academy and the Neoplatonic synthesis that Landino absorbed and transmitted through his teaching and commentaries.",
      "The development of Italian printing after 1465 gave Landino's scholarship unprecedented reach: his Dante commentary of 1481 was one of the first great illustrated printed books, combining humanist scholarship with the new medium in a way that transformed commentary from manuscript culture to print culture."
    ],
    "effects": [
      "Landino's 1481 Dante commentary established the Neoplatonic and allegorical reading of the Commedia that dominated Dante scholarship for centuries, shaping how educated Europeans understood Italy's greatest vernacular poem.",
      "His translations of Pliny's Natural History and other Latin classics into elegant Italian contributed to the development of Italian as a language of learning — a process that accelerated the shift from Latin to vernacular intellectual discourse in the 16th century.",
      "Through his students at the Studio Fiorentino over four decades and his dialogue literature representing the Medicean circle, Landino transmitted the synthesis of Platonic philosophy, classical rhetoric, and Italian vernacular culture that defined Florentine Renaissance humanism to subsequent European scholarship."
    ],
    "relationships": [
      {"sourceSlug": "cristoforo-landino", "sourceName": "Cristoforo Landino", "verb": "PRODUCES", "targetSlug": "dante-commentary-1481", "targetName": "Dante Commentary (1481)", "context": "Landino's illustrated Dante commentary (1481), with engravings by Botticelli, established the Neoplatonic interpretive framework for the Commedia and was a landmark of early Italian printing."},
      {"sourceSlug": "cristoforo-landino", "sourceName": "Cristoforo Landino", "verb": "OCCURS_IN", "targetSlug": "florentine-renaissance", "targetName": "Florentine Renaissance", "context": "Landino was a central figure in Laurentian Florence's intellectual circle, contributing to the Platonic Academy discussions and representing the humanism of Lorenzo de' Medici's court."},
      {"sourceSlug": "marsilio-ficino", "sourceName": "Marsilio Ficino", "verb": "INFLUENCES", "targetSlug": "cristoforo-landino", "targetName": "Cristoforo Landino", "context": "Ficino's Neoplatonic translations and philosophy provided the philosophical framework that Landino applied in his commentaries on Virgil and Dante and his 'Disputationes Camaldulenses'."},
      {"sourceSlug": "dante-alighieri", "sourceName": "Dante Alighieri", "verb": "INSPIRES", "targetSlug": "cristoforo-landino", "targetName": "Cristoforo Landino", "context": "Landino's most influential work was his 1481 commentary on Dante's Commedia, which shaped Dante reception in Italy and Europe for generations."}
    ],
    "places": [
      {"name": "Florence, Italy", "role": "Landino's home city; site of his forty-year professorship at the Studio Fiorentino and the Medici cultural circle"},
      {"name": "Camaldoli Monastery, Tuscany", "role": "Setting of Landino's 'Disputationes Camaldulenses' (c. 1474) — his major philosophical dialogue representing Florentine Neoplatonism"}
    ],
    "subjects": ["Renaissance Humanism", "Italian History", "Philosophy", "Literature", "Medieval Era", "Florence", "Neoplatonism", "Classics", "Publishing"],
    "frameworks": ["CULTURAL_TRANSMISSION", "STRUCTURAL_ANALYSIS", "RELIGIOUS_INTERPRETATION"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Cristoforo Landino was one of the central professors and commentators of Laurentian Florence, whose forty-year career at the Studio Fiorentino transmitted Florentine Neoplatonism to several generations. His 1481 Dante commentary — illustrated by Botticelli — established the dominant interpretive framework for the Commedia and was a landmark of early Italian printing, shaping how Dante was read across Europe.",
      "significanceCategory": "significant"
    }
  }
},

"peter-shafirov": {
  "filepath": "data/appwrite-export/entities/220-Class-220/220peter-shafirov.json",
  "slug": "peter-shafirov",
  "data": {
    "summary": "Peter Shafirov (1669–1739) was Russia's first professional diplomat and a key architect of Peter the Great's foreign policy transformation — a man who rose from a Jewish merchant family to become Vice Chancellor of Russia and the empire's most sophisticated negotiator in an era when Russian diplomacy was being reinvented from scratch. Born in Smolensk into a converted Jewish family (his father had converted to Orthodox Christianity), Shafirov entered the Chancellery of Foreign Affairs and demonstrated an exceptional gift for languages and negotiation that brought him to Peter the Great's personal attention. He became Peter's chief translator, then his diplomatic agent, and ultimately the second most powerful figure in Russian foreign policy after the reforming tsar himself.\n\nShafirov's greatest test came at the Pruth River disaster of 1711, when Peter's army was surrounded by a vastly superior Ottoman force after an ill-advised campaign into Moldavia. With Peter literally at the Ottomans' mercy, it was Shafirov who negotiated Russia's way out: offering substantial concessions including the return of Azov, agreeing to dismantle newly built Black Sea fortresses, and promising non-interference in Polish affairs. He himself remained behind as a hostage in Constantinople to guarantee the treaty's fulfilment — living in the Ottoman capital for two years while Peter returned to rebuild. The negotiations at Pruth saved Peter's army and preserved Russia's capacity to continue the Great Northern War against Sweden.\n\nShafirov authored 'A Discourse Concerning the Just Reasons Which His Tsarish Majesty Peter I Had for Beginning the War Against the Swedish King Charles XII' (1717) — the first Russian work of political theory in the European natural law tradition, demonstrating that Russia was now a participant in European political discourse rather than a peripheral object of it. He later fell victim to court politics, was sentenced to death (commuted to Siberian exile), returned to favour under Peter II and Anna Ivanovna, and died in 1739 as President of the Commerce Collegium.",
    "causes": [
      "Peter the Great's modernisation programme explicitly required European-style diplomacy — permanent embassies, multilingual envoys, knowledge of international law and protocol — that Russia previously lacked, creating demand for exactly the talents Shafirov possessed.",
      "Shafirov's multilingual abilities (Russian, German, Dutch, Polish, and sufficient Turkish for negotiation) and his experience in the Foreign Affairs Chancellery from the 1690s onward gave him the specific competences that Peter needed for his European diplomatic revolution.",
      "The Great Northern War (1700–1721) forced Russia into sustained diplomatic engagement with every major European power simultaneously, creating the conditions under which a professional diplomat like Shafirov could rise to unprecedented influence."
    ],
    "effects": [
      "Shafirov's Pruth negotiations (1711) saved Peter's army from destruction and preserved the Great Northern War's strategic situation — Russia went on to defeat Sweden at the Battle of Gangut (1714) and negotiate the Treaty of Nystad (1721) that made Russia a Baltic power.",
      "His 1717 political treatise introduced natural law argumentation into Russian political discourse, contributing to the westernisation of Russian political culture and establishing a tradition of Russian engagement with European legal and political theory.",
      "Shafirov's career demonstrated that Peter's meritocratic system could elevate individuals of non-noble and non-Orthodox origin to the highest levels of state service — a model that, even if imperfectly applied, represented a significant departure from Muscovite social practice."
    ],
    "relationships": [
      {"sourceSlug": "peter-shafirov", "sourceName": "Peter Shafirov", "verb": "SERVES", "targetSlug": "peter-the-great", "targetName": "Peter the Great", "context": "Shafirov was Peter the Great's chief diplomatic operative and Vice Chancellor, serving as the tsar's principal foreign policy instrument across two decades of European warfare and negotiation."},
      {"sourceSlug": "peter-shafirov", "sourceName": "Peter Shafirov", "verb": "CAUSES", "targetSlug": "treaty-of-pruth", "targetName": "Treaty of the Pruth (1711)", "context": "Shafirov negotiated Russia's escape from the Pruth encirclement, offering himself as an Ottoman hostage and securing terms that allowed Peter's army to withdraw intact."},
      {"sourceSlug": "great-northern-war", "sourceName": "Great Northern War", "verb": "CREATES", "targetSlug": "peter-shafirov", "targetName": "Peter Shafirov", "context": "The Great Northern War's diplomatic demands — negotiating with Sweden, the Ottoman Empire, Poland, Prussia, and England simultaneously — created the conditions for Shafirov's rise to diplomatic prominence."}
    ],
    "places": [
      {"name": "Constantinople (Istanbul), Turkey", "role": "Where Shafirov lived as an Ottoman hostage 1711–1714, guaranteeing the Treaty of Pruth — the most dramatic episode of his diplomatic career"},
      {"name": "St Petersburg, Russia", "role": "Capital of Peter the Great's new Russia, centre of Shafirov's diplomatic activity and the Foreign Affairs apparatus he helped build"},
      {"name": "Pruth River, Moldova", "role": "Site of the 1711 military disaster where Peter's army was surrounded and Shafirov's negotiating genius saved Russia from catastrophic defeat"}
    ],
    "subjects": ["Early Modern History", "Russia", "Diplomacy", "Political Theory", "Early Modern Era", "Jewish History", "Peter the Great", "Ottoman Empire"],
    "frameworks": ["DIPLOMATIC_HISTORY", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Peter Shafirov was Russia's first professional diplomat and the architect of Peter the Great's foreign policy transformation. His negotiation of the Treaty of Pruth (1711) — conducted while Peter's army was surrounded — saved Russia from catastrophic defeat and preserved the strategic situation that led to the Treaty of Nystad (1721), which made Russia a European Baltic power. His 1717 political treatise introduced natural law theory into Russian political discourse.",
      "significanceCategory": "significant"
    }
  }
},

"pantaenus": {
  "filepath": "data/appwrite-export/entities/210-Class-210/210pantaenus.json",
  "slug": "pantaenus",
  "data": {
    "summary": "Pantaenus of Alexandria (died c. 200 CE) was a Stoic philosopher turned Christian theologian who founded or substantially organised the Catechetical School of Alexandria — arguably the first institution of Christian higher learning in the world and the prototype of all subsequent Christian theological education. A Sicilian by birth who had studied Stoic philosophy before converting to Christianity, Pantaenus established in Alexandria around 180 CE a school that taught Christianity not as a simple faith for the uneducated but as a sophisticated intellectual tradition capable of engaging — and surpassing — the Greek philosophical heritage. The school he organised became the training ground for the most intellectually significant Christian thinkers of the 2nd–4th centuries.\n\nPantaenus himself wrote nothing that survives, and our knowledge of him comes almost entirely from later accounts by Clement of Alexandria and Eusebius of Caesarea. What these accounts establish is his role as the teacher of Clement — the first Christian theologian to seriously engage Platonic philosophy — and his status as the model of a scholar who had mastered secular learning before dedicating it to Christian interpretation. Eusebius records that Pantaenus undertook a missionary journey to India ('the land of the Blessed') where he reportedly found Christians using a Hebrew Gospel of Matthew that Bartholomew the Apostle had left there — an account whose historicity is uncertain but which indicates the geographic reach of Pantaenus's intellectual world.\n\nThe Alexandrian school that Pantaenus founded went on to produce Clement of Alexandria, Origen, Didymus the Blind, and Cyril of Alexandria — the most sophisticated Christian theological tradition in the ancient world, which synthesised Platonic metaphysics, Neoplatonic emanationism, and biblical interpretation into the Catholic theological synthesis that Aquinas would inherit in the medieval period. In this sense, Pantaenus stands at the origin of the entire tradition of Christian systematic theology.",
    "causes": [
      "Alexandria's position as the intellectual capital of the Hellenistic and Roman world — home to the Library of Alexandria, major philosophical schools, and the largest Jewish diaspora community — provided both the intellectual resources and the diverse audience for a sophisticated Christian educational enterprise.",
      "The challenge of Gnosticism — which offered intellectually sophisticated alternatives to mainstream Christianity with complex cosmologies and philosophical frameworks — created pressure on Christian teachers to develop equally rigorous theological education to compete for educated converts.",
      "Pantaenus's personal background as a Stoic philosopher gave him the intellectual formation and institutional experience of running a philosophical school, which he applied to the organisation of Christian catechetical instruction at a higher level than had previously existed."
    ],
    "effects": [
      "The Catechetical School of Alexandria produced Clement and Origen — the two most intellectually significant Christian theologians before Augustine — whose syntheses of Platonic philosophy and biblical interpretation established the framework for all subsequent Eastern and Western Christian theology.",
      "The Alexandrian synthesis of Greek philosophy and Christian theology that Pantaenus initiated became the dominant tradition of Christian intellectual life, influencing the Cappadocian Fathers, Pseudo-Dionysius, Augustine, and through Aquinas the entire scholastic tradition.",
      "The institutional model of the Alexandrian school — a Christian centre of higher learning engaging secular philosophy — became the prototype for medieval cathedral schools and ultimately European universities, making Pantaenus a distant ancestor of the Western university tradition."
    ],
    "relationships": [
      {"sourceSlug": "pantaenus", "sourceName": "Pantaenus", "verb": "CREATES", "targetSlug": "catechetical-school-of-alexandria", "targetName": "Catechetical School of Alexandria", "context": "Pantaenus founded or substantially organised the Alexandrian catechetical school around 180 CE — the first institution of systematic Christian higher education and prototype of later Christian theological schools."},
      {"sourceSlug": "pantaenus", "sourceName": "Pantaenus", "verb": "TEACHES", "targetSlug": "clement-of-alexandria", "targetName": "Clement of Alexandria", "context": "Pantaenus was Clement's teacher, transmitting the tradition of engaging Greek philosophy for Christian purposes that Clement developed into the first major synthesis of Platonic and Christian thought."},
      {"sourceSlug": "clement-of-alexandria", "sourceName": "Clement of Alexandria", "verb": "INFLUENCES", "targetSlug": "origen", "targetName": "Origen", "context": "Clement succeeded Pantaenus at the Alexandrian school and taught Origen, creating a three-generation chain of theological development from Pantaenus through Clement to Origen."},
      {"sourceSlug": "alexandrian-school", "sourceName": "Catechetical School", "verb": "INFLUENCES", "targetSlug": "christian-theology", "targetName": "Christian Systematic Theology", "context": "The theological tradition Pantaenus initiated produced the Platonic-Christian synthesis that shaped Eastern Orthodoxy, Augustinian theology, and through scholasticism the entire Western theological tradition."}
    ],
    "places": [
      {"name": "Alexandria, Egypt", "role": "Site of the Catechetical School that Pantaenus founded — the intellectual capital of the Hellenistic world and ideal environment for Christian higher education"},
      {"name": "India", "role": "Destination of Pantaenus's reported missionary journey where Eusebius claims he found a Hebrew Gospel of Matthew left by the Apostle Bartholomew"}
    ],
    "subjects": ["Early Church History", "Christian Theology", "Ancient History", "Philosophy", "Education", "Alexandria", "Classical Era", "Intellectual History"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "CULTURAL_TRANSMISSION", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Pantaenus founded the Catechetical School of Alexandria — the first institution of Christian higher learning — and was teacher to Clement of Alexandria, whose student Origen became the most influential biblical scholar of antiquity. The intellectual tradition Pantaenus initiated produced the Platonic-Christian synthesis that underlies all subsequent Eastern and Western Christian theology, making him the founding figure of systematic Christian education.",
      "significanceCategory": "highly-significant"
    }
  }
}

}  # end ENRICHMENTS

# ─────────────────────────────────────────────────────────────────────────────
# Runtime (same as batch 02/03)
# ─────────────────────────────────────────────────────────────────────────────

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
