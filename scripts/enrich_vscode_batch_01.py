#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 01 (20 entities, queue indices 200-225)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 2026

Entities covered (safe zone: outside all running Ollama/Gemini bot ranges):
  health, gospel-of-luke, taoism, mithridates-chrestus, dai-jin, hattusili-i,
  ancient-greek, eulpaso, drest-iv, ibn-al-ḥājib, old-testament, tyrannion,
  galactorius-of-lescar, the-republic, statistics, neferkare-iv, uranius,
  henti, murad-khan, arctic-ocean, saint-naum, world-health-organization,
  journalism, sarduri-iv

No conflict risk: Ollama bots on queue[0:100], Gemini bot on queue[100:200].
"""

import json
import os
import sys
import time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-01-may2026"

# ─────────────────────────────────────────────────────────────────────────────
# Hand-authored enrichments (Claude Sonnet 4.6 / GitHub Copilot)
# ─────────────────────────────────────────────────────────────────────────────

ENRICHMENTS = {

"health": {
  "filepath": "data/appwrite-export/entities/132-Class-132/132health.json",
  "slug": "health",
  "data": {
    "summary": "Health, as a concept central to all human civilisations, describes the optimal functional and metabolic state of a living being — a state recognised, pursued, and theorised from the earliest recorded history. The ancient Egyptians attributed wellness to the correct balance of spiritual and physical forces, while Greek physicians, led by Hippocrates (c.460–370 BCE), systematised health as the equilibrium of four humours: blood, phlegm, yellow bile, and black bile. Galen of Pergamon later codified this framework into a comprehensive medical system that dominated European medicine for over 1,400 years.\n\nThe industrial revolution fundamentally transformed health as a collective concern. Urbanisation packed workers into disease-ridden slums, triggering waves of cholera, typhus, and tuberculosis. John Snow's 1854 identification of the Broad Street water pump as the source of a London cholera outbreak is widely regarded as the birth of modern epidemiology. By the late 19th century, Louis Pasteur's germ theory and Joseph Lister's antiseptic surgery had permanently shifted medicine toward microbiology and preventive hygiene, making health a measurable and governable social condition.\n\nThe 20th century produced the most ambitious redefinition in history: the 1948 World Health Organization Constitution declared health to be 'a state of complete physical, mental, and social well-being — not merely the absence of disease or infirmity.' This holistic definition catalysed global public health infrastructure, vaccination campaigns, and universal healthcare systems. By 2024, life expectancy at birth had risen from approximately 40 years in 1900 to over 73 years globally, an achievement attributable to clean water, antibiotics, and mass immunisation.",
    "causes": [
      "The agricultural revolution created sedentary populations susceptible to zoonotic diseases, driving systematic interest in healing and hygiene.",
      "Ancient Greek natural philosophy — particularly Hippocratic empiricism — established systematic observation of the body as the basis for medical theory.",
      "Industrialisation and urban overcrowding produced mass epidemics that forced governments to develop public health infrastructure and sanitation systems."
    ],
    "effects": [
      "The germ theory paradigm transformed medicine into an evidence-based science and enabled targeted drug and vaccine development.",
      "The WHO's 1948 holistic definition broadened health from an individual to a collective and political responsibility, founding the modern global health system.",
      "Global life expectancy nearly doubled between 1900 and 2024, largely as a result of public health interventions, nutrition improvements, and medical advances."
    ],
    "relationships": [
      {"sourceSlug": "health", "sourceName": "health", "verb": "INFLUENCES", "targetSlug": "world-health-organization", "targetName": "World Health Organization", "context": "The WHO's 1948 constitution enshrined health as a fundamental human right, institutionalising global health governance and shaping all subsequent international health policy."},
      {"sourceSlug": "health", "sourceName": "health", "verb": "INFLUENCES", "targetSlug": "hippocrates", "targetName": "Hippocrates", "context": "Hippocratic medicine established the framework for understanding health as natural equilibrium, founding Western medical tradition c.400 BCE."},
      {"sourceSlug": "health", "sourceName": "health", "verb": "LEADS_TO", "targetSlug": "germ-theory", "targetName": "Germ Theory of Disease", "context": "Pasteur and Koch's germ theory displaced humoral medicine and reframed health as the absence of microbial infection, transforming diagnosis and treatment."},
      {"sourceSlug": "health", "sourceName": "health", "verb": "OCCURS_IN", "targetSlug": "country-greece", "targetName": "Ancient Greece", "context": "Hippocratic corpus produced on the island of Cos c.400 BCE established foundational medical definitions of health that persisted for two millennia."},
      {"sourceSlug": "black-death", "sourceName": "Black Death", "verb": "INFLUENCES", "targetSlug": "health", "targetName": "health", "context": "The 1347–1351 pandemic killed 30–50% of Europe's population and forced systematic reconsideration of disease causation and public health intervention."}
    ],
    "places": [
      {"name": "Cos, Greece", "role": "Hippocratic medicine birthplace"},
      {"name": "London, England", "role": "Cholera epidemiology (Snow, 1854)"},
      {"name": "Geneva, Switzerland", "role": "WHO headquarters since 1948"}
    ],
    "subjects": ["Medicine", "Public Health", "Epidemiology", "Philosophy of Science", "World History", "Social Policy", "Biology", "Global Governance", "Human Biology"],
    "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS", "WORLD_SYSTEMS"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Health as a concept shaped every human civilisation's social organisation, drove the development of modern medicine, and became the defining metric of 20th-century development policy — ultimately underpinning the doubling of human life expectancy within a single century.",
      "significanceCategory": "world-changing"
    }
  }
},

"gospel-of-luke": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780gospel-of-luke.json",
  "slug": "gospel-of-luke",
  "data": {
    "summary": "The Gospel of Luke, composed around 80–90 CE and attributed to Luke the physician and companion of Paul, is the most literarily accomplished of the four canonical Gospels and the first volume of a two-part work that includes the Acts of the Apostles. Written in elegant Hellenistic Greek for a predominantly Gentile audience — addressed to a patron named Theophilus — Luke's Gospel portrays Jesus as a universal saviour whose mission transcends the boundaries of Jewish law and national identity, extending salvation to Samaritans, Romans, women, the poor, and the marginalised.\n\nLuke's distinctive theological emphases reshape the narrative of Jesus's life with unusual tenderness: the Gospel opens with the Annunciation and the Magnificat of Mary, the longest speech by a woman in the entire New Testament. It alone records the parables of the Good Samaritan and the Prodigal Son, which became among the most-cited moral stories in Western literature. Luke's Jesus consistently reverses social hierarchies — the rich are sent away empty while the hungry are filled — a theme that resonated deeply in medieval Christianity and inspired liberation theology movements in the 20th century.\n\nLuke-Acts together constitute approximately 27% of the New Testament by word count, making Luke its single most substantial contributor. The Acts of the Apostles, its sequel, provides the only narrative account of the early Church's expansion from Jerusalem to Rome. Luke's portrait of Paul transformed the apostle's mission into a heroic narrative arc that defined Christian self-understanding as a universal rather than tribal religion — a conceptual reorientation with consequences for every subsequent century of Western and global history.",
    "causes": [
      "The destruction of the Jerusalem Temple in 70 CE prompted urgent theological reconsideration of Christianity's relationship to Judaism and its mission to the wider Gentile world.",
      "Paul's missionary journeys across the Mediterranean created Greek-speaking Gentile Christian communities that needed a literary account of Jesus accessible to non-Jewish readers.",
      "Hellenistic literary conventions and the model of Greek historiography (Thucydides, Polybius) shaped Luke's careful investigation of sources and his sequential narrative method."
    ],
    "effects": [
      "The parables of the Good Samaritan and the Prodigal Son became cornerstones of Western ethical and literary culture, cited in moral philosophy, literature, and social work for two millennia.",
      "Luke's portrayal of Jesus as champion of the poor directly inspired 20th-century liberation theology, particularly in Latin America, linking Christian faith to economic justice movements.",
      "The Acts of the Apostles established the canonical narrative of Christianity's spread from Jerusalem to Rome, providing the foundational framework for Church history and missionary theology."
    ],
    "relationships": [
      {"sourceSlug": "gospel-of-luke", "sourceName": "Gospel of Luke", "verb": "PART_OF", "targetSlug": "new-testament", "targetName": "New Testament", "context": "The Gospel of Luke is the third of four canonical Gospels, constituting approximately 19% of the New Testament alongside its companion volume Acts of the Apostles."},
      {"sourceSlug": "gospel-of-luke", "sourceName": "Gospel of Luke", "verb": "INFLUENCES", "targetSlug": "paul-of-tarsus", "targetName": "Paul of Tarsus", "context": "Luke was a companion and chronicler of Paul; Acts of the Apostles presents Paul's missionary journeys as the theological fulfilment of Luke's Gospel."},
      {"sourceSlug": "gospel-of-luke", "sourceName": "Gospel of Luke", "verb": "OCCURS_IN", "targetSlug": "country-israel", "targetName": "Judea and Galilee", "context": "The narrative is set primarily in Galilee, Samaria, and Jerusalem, tracing Jesus's ministry from Nazareth to his crucifixion in Jerusalem c.30 CE."},
      {"sourceSlug": "gospel-of-luke", "sourceName": "Gospel of Luke", "verb": "LEADS_TO", "targetSlug": "acts-of-the-apostles", "targetName": "Acts of the Apostles", "context": "Luke-Acts forms a continuous two-volume work; the Gospel traces Jesus's life while Acts chronicles the early Church's expansion across the Roman Empire."},
      {"sourceSlug": "second-temple-judaism", "sourceName": "Second Temple Judaism", "verb": "INFLUENCES", "targetSlug": "gospel-of-luke", "targetName": "Gospel of Luke", "context": "Luke's Gospel presupposes detailed knowledge of Jewish scripture and Temple practice, situating Jesus within the prophetic tradition of Israel while opening it to universal application."}
    ],
    "places": [
      {"name": "Jerusalem, Judea", "role": "Crucifixion and Resurrection"},
      {"name": "Galilee, Israel", "role": "Jesus's ministry"},
      {"name": "Antioch, Syria", "role": "Traditional authorship location"}
    ],
    "subjects": ["Christianity", "New Testament Studies", "Biblical Literature", "Hellenistic Literature", "Religious History", "Ethics", "Liberation Theology", "World Religion", "Ancient Mediterranean"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "CULTURAL_TRANSMISSION", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Gospel of Luke shaped Christian ethics and self-understanding across two millennia — its parables became foundational Western moral stories, its universalism enabled Christianity's expansion beyond Judaism, and its portrayal of Jesus as champion of the poor continues to animate social justice movements worldwide.",
      "significanceCategory": "world-changing"
    }
  }
},

"taoism": {
  "filepath": "data/appwrite-export/entities/110-Class-110/110taoism.json",
  "slug": "taoism",
  "data": {
    "summary": "Taoism (Daoism) is one of the world's oldest living philosophical and religious traditions, originating in China during the Classical period (c.6th–4th century BCE) and shaped by two foundational texts: the Tao Te Ching attributed to the semi-legendary sage Laozi, and the Zhuangzi, composed by Zhuang Zhou (c.369–286 BCE). The Tao (道, 'the Way') denotes the ineffable ordering principle underlying all reality — a force that cannot be defined, only harmonised with through the practice of wu wei (無為), effortless non-striving action that aligns human conduct with natural rhythms rather than imposing artificial order upon them.\n\nTaoism developed in two distinct but overlapping streams. Philosophical Taoism (Daojia), centred on the texts of Laozi and Zhuangzi, influenced Chinese art, poetry, painting, and political thought profoundly — its ideal of spontaneous naturalness permeated the aesthetic traditions of the Tang and Song dynasties. Religious Taoism (Daojiao), formalised from the 2nd century CE onward with the Celestial Masters movement, developed temples, priests, liturgy, alchemy, and a pantheon of deities. Under the Tang Dynasty (618–907 CE), Taoism was elevated as an imperial ideology: Emperor Xuanzong declared Laozi a divine ancestor, and the Tao Te Ching became required reading for the imperial examinations.\n\nBeyond China, Taoist concepts profoundly shaped East Asian civilisations from Japan and Korea to Vietnam. In the 20th century, Taoism became a significant influence on Western countercultural movements, environmental philosophy, and modern science: physicist Fritjof Capra's 1975 'The Tao of Physics' drew parallels between quantum mechanics and Taoist cosmology. Today approximately 12 million people practise Taoism formally, though its aesthetic and philosophical influence extends far beyond formal adherents.",
    "causes": [
      "The political fragmentation of the Zhou Dynasty's Warring States period (475–221 BCE) generated widespread philosophical reflection on the nature of order, governance, and human flourishing.",
      "Ancient Chinese shamanic and nature-worship traditions provided the mythological and ritual substratum upon which Laozi and Zhuangzi built their philosophical synthesis.",
      "The bureaucratic rigidity and moral formalism of Confucianism created intellectual demand for a counterweight philosophy emphasising spontaneity, naturalness, and individual spiritual freedom."
    ],
    "effects": [
      "Taoist aesthetics of naturalness and spontaneity permeated Chinese landscape painting, calligraphy, poetry, and garden design for over two millennia, producing one of history's most distinctive artistic traditions.",
      "The Taoist concept of wu wei — achieving outcomes through non-coercive action — influenced Chinese political philosophy from the Han Dynasty through to 20th-century administrative theory.",
      "Taoist alchemy and medicinal traditions contributed foundational insights to Chinese medicine, including acupuncture theory, and influenced the development of gunpowder and other innovations."
    ],
    "relationships": [
      {"sourceSlug": "taoism", "sourceName": "Taoism", "verb": "OPPOSES", "targetSlug": "confucianism", "targetName": "Confucianism", "context": "Taoism and Confucianism developed as complementary yet contrasting philosophies: where Confucianism emphasised ritual, hierarchy, and moral cultivation, Taoism prioritised naturalness, spontaneity, and retreat from social convention."},
      {"sourceSlug": "taoism", "sourceName": "Taoism", "verb": "INFLUENCES", "targetSlug": "zen-buddhism", "targetName": "Zen Buddhism", "context": "Chan (Zen) Buddhism absorbed major Taoist concepts including naturalness, non-attachment, and direct experiential insight when Buddhism entered China from the 1st century CE onward."},
      {"sourceSlug": "taoism", "sourceName": "Taoism", "verb": "FOUNDED_BY", "targetSlug": "laozi", "targetName": "Laozi", "context": "The Tao Te Ching, attributed to Laozi (c.6th century BCE), is the foundational text of Taoism, presenting 81 short chapters on the nature of the Tao and the art of governing and living."},
      {"sourceSlug": "taoism", "sourceName": "Taoism", "verb": "OCCURS_IN", "targetSlug": "country-china", "targetName": "China", "context": "Taoism originated in the Zhou Dynasty states of ancient China and remains most concentrated in mainland China, Taiwan, and diaspora Chinese communities worldwide."},
      {"sourceSlug": "taoism", "sourceName": "Taoism", "verb": "INFLUENCES", "targetSlug": "chinese-art", "targetName": "Chinese Art and Literature", "context": "Taoist ideals of naturalness (ziran) and effortless spontaneity directly shaped Chinese landscape painting, poetry, and garden design from the Tang Dynasty onward."}
    ],
    "places": [
      {"name": "Henan Province, China", "role": "Laozi's legendary homeland"},
      {"name": "Luoyang, China", "role": "Zhou Dynasty capital, Tao Te Ching composition"},
      {"name": "Mount Wudang, China", "role": "Sacred Taoist pilgrimage site"}
    ],
    "subjects": ["Taoism", "Chinese Philosophy", "World Religions", "East Asian History", "Chinese Culture", "Metaphysics", "Ethics", "Religious Studies", "Environmental Philosophy", "Classical Antiquity"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "CULTURAL_TRANSMISSION", "COMPARATIVE_CIVILIZATIONS"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Taoism shaped the aesthetic, political, and spiritual culture of China and East Asia for over 2,500 years, and in the 20th century became a globally resonant philosophy influencing environmentalism, physics, and alternative spirituality movements across multiple continents.",
      "significanceCategory": "world-changing"
    }
  }
},

"hattusili-i": {
  "filepath": "data/appwrite-export/entities/221-Class-221/221hattusili-i.json",
  "slug": "hattusili-i",
  "data": {
    "summary": "Hattusili I (reigned c.1650–1620 BCE), also known as Labarnas II, was the founder-king of the Hittite Old Kingdom and the first Hittite ruler whose deeds are extensively documented in cuneiform records. His reign marked the transformation of a confederacy of Anatolian city-states into a centralised imperial polity centred on Hattusa (modern Boğazkale, Turkey), which would endure as one of the ancient world's great powers for six centuries. Hattusili was the first to bear the title 'Great King' and to establish the concept of royal hereditary succession in Hittite governance.\n\nHis military campaigns ranged across a vast arc from northern Anatolia into Syria, sacking the city of Alalakh in the Orontes valley and pushing Hittite power to the gates of Babylon's sphere of influence. The Annals of Hattusili I, composed in both Hittite and Akkadian, are among the oldest surviving royal narrative documents in history, presenting the king's military achievements in vivid first-person prose. His campaigns against the Arzawa lands in western Anatolia also represent the first documented Hittite contacts with Aegean cultural zones that later produced the famous Bronze Age diplomatic network.\n\nHattusili's succession crisis proved historically consequential: having disinherited several relatives, he adopted his grandson Mursili I, who would go on in 1595 BCE to sack Babylon — one of the Bronze Age's most dramatic events — ending the First Babylonian Dynasty. Hattusili's 'Testament', written on his deathbed, is among the oldest known political wills in history, offering a remarkably personal window into Bronze Age statecraft and the anxieties of royal succession.",
    "causes": [
      "The collapse of the Assyrian trading colony network (karum) around 1700 BCE destabilised central Anatolian political order, creating conditions for a new centralising power to emerge.",
      "The labarna tradition of Anatolian kingship provided the ideological framework of centralised monarchical rule that Hattusili formalised into the Hittite royal institution.",
      "Access to iron and bronze metallurgy in Anatolia, combined with the chariot warfare revolution spreading across the Near East, gave early Hittite armies decisive military advantage."
    ],
    "effects": [
      "Hattusili's consolidation of Hattusa as capital established the institutional and territorial foundations of the Hittite Empire, which endured until c.1180 BCE and shaped Near Eastern geopolitics for five centuries.",
      "The Annals of Hattusili I inaugurated a genre of royal narrative literature in the ancient Near East, influencing subsequent Hittite, Assyrian, and Egyptian royal self-presentation.",
      "The succession arrangements Hattusili established led directly to Mursili I's sack of Babylon in 1595 BCE, ending the First Babylonian Dynasty and reshaping Mesopotamian power dynamics."
    ],
    "relationships": [
      {"sourceSlug": "hattusili-i", "sourceName": "Hattusili I", "verb": "FOUNDED_BY", "targetSlug": "hittite-old-kingdom", "targetName": "Hittite Old Kingdom", "context": "Hattusili I consolidated the Hittite Old Kingdom around 1650 BCE, transforming a confederation of Anatolian polities into a unified state centred on Hattusa."},
      {"sourceSlug": "hattusili-i", "sourceName": "Hattusili I", "verb": "LEADS_TO", "targetSlug": "mursili-i", "targetName": "Mursili I", "context": "Hattusili adopted his grandson Mursili I as successor; Mursili went on to sack Babylon in 1595 BCE, one of the Bronze Age's most consequential military events."},
      {"sourceSlug": "hattusili-i", "sourceName": "Hattusili I", "verb": "OCCURS_IN", "targetSlug": "country-turkey", "targetName": "Anatolia", "context": "Hattusili's campaigns and kingdom were centred in central Anatolia, with his capital at Hattusa near modern Boğazkale, Turkey."},
      {"sourceSlug": "hattusili-i", "sourceName": "Hattusili I", "verb": "OPPOSES", "targetSlug": "alalakh", "targetName": "Alalakh", "context": "Hattusili I sacked Alalakh on the Orontes River, one of the most prosperous trading cities of northern Syria, in his campaigns to extend Hittite power southward."},
      {"sourceSlug": "old-babylonian-empire", "sourceName": "Old Babylonian Empire", "verb": "INFLUENCES", "targetSlug": "hattusili-i", "targetName": "Hattusili I", "context": "The strength and prestige of Babylon under the successors of Hammurabi defined the geopolitical environment against which Hattusili projected Hittite power into northern Syria."}
    ],
    "places": [
      {"name": "Hattusa, Turkey", "role": "Hittite capital he established"},
      {"name": "Alalakh, Syria", "role": "Major city he conquered"},
      {"name": "Anatolia, Turkey", "role": "Core kingdom territory"}
    ],
    "subjects": ["Hittite History", "Bronze Age Near East", "Ancient Anatolia", "Military History", "Royal Succession", "Cuneiform Literature", "World History", "Ancient Governance", "Archaeological History"],
    "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS", "COMPARATIVE_CIVILIZATIONS"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "As the founder of the Hittite Kingdom, Hattusili I established an imperial institution that endured for five centuries, authored some of antiquity's oldest royal narrative texts, and set in motion the succession that ended the First Babylonian Dynasty — reshaping Bronze Age Near Eastern history.",
      "significanceCategory": "continental"
    }
  }
},

"the-republic": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780the-republic.json",
  "slug": "the-republic",
  "data": {
    "summary": "Plato's Republic (Politeia, c.380 BCE) is the most influential work of political philosophy ever written and one of the foundational texts of Western intellectual tradition. Structured as a Socratic dialogue exploring the nature of justice, the Republic evolves into a comprehensive blueprint for the ideal city-state (kallipolis) governed by philosopher-kings — rulers whose years of rigorous philosophical education, culminating in direct apprehension of the Form of the Good, uniquely qualify them to govern without self-interest or partisan bias. The work's reach extends far beyond politics into epistemology, metaphysics, ethics, aesthetics, and education theory.\n\nThe Republic's central thought experiments remain among philosophy's most powerful: the Allegory of the Cave depicts ordinary human existence as imprisonment in a shadow-world, with philosophy as the painful ascent toward true reality. The Theory of Forms posits that material objects are imperfect reflections of eternal, abstract ideals — a metaphysical framework that influenced Neoplatonism, Augustine's theology, and Christian medieval philosophy. Plato's analysis of the five degenerate political constitutions — from timocracy through oligarchy, democracy, and tyranny — offered a cyclical theory of political decay that fascinated thinkers from Cicero to Madison.\n\nThe Republic's legacy is paradoxical in its scope: totalitarian regimes appropriated its philosopher-king ideal while liberal democracies absorbed its rejection of uninformed popular rule. Karl Popper's 'The Open Society and Its Enemies' (1945) identified the Republic as the originating text of totalitarian thinking. Yet it also inspired Thomas More's Utopia, shaped Renaissance humanism, and provided Enlightenment thinkers with the vocabulary for debating education, justice, and the limits of political authority. Two and a half millennia after its composition, Plato's Republic remains one of the half-dozen books most frequently cited across the entire humanities.",
    "causes": [
      "The trial and execution of Socrates in 399 BCE by Athenian democracy left Plato profoundly disillusioned with democratic governance and motivated his lifelong search for philosophically grounded alternatives.",
      "The political turbulence of 5th-century Athens — the Peloponnesian War, the Thirty Tyrants, democratic restoration — provided Plato with a laboratory of political failures to analyse and theorise against.",
      "The Pythagorean mathematical tradition and Parmenidean metaphysics gave Plato the conceptual tools to develop his Theory of Forms as the epistemological foundation of just governance."
    ],
    "effects": [
      "The Theory of Forms influenced Neoplatonism and, through Augustine of Hippo, shaped medieval Christian theology's conception of God as the supreme Form of the Good.",
      "The Republic's philosopher-king ideal informed Renaissance humanist arguments for educated, virtuous governance and 17th–18th century debates about the role of reason in political authority.",
      "Plato's typology of political constitutions (timocracy, oligarchy, democracy, tyranny) provided Western political philosophy with its foundational vocabulary for analysing regime change."
    ],
    "relationships": [
      {"sourceSlug": "the-republic", "sourceName": "The Republic", "verb": "FOUNDED_BY", "targetSlug": "plato", "targetName": "Plato", "context": "Written by Plato around 380 BCE as the culminating dialogue of his middle period, the Republic represents the fullest expression of his political philosophy and Theory of Forms."},
      {"sourceSlug": "the-republic", "sourceName": "The Republic", "verb": "INFLUENCES", "targetSlug": "thomas-aquinas", "targetName": "Thomas Aquinas", "context": "Through Neoplatonism and Augustine, Platonic ideas from the Republic shaped medieval Scholasticism's theories of natural law, justice, and governance."},
      {"sourceSlug": "the-republic", "sourceName": "The Republic", "verb": "OCCURS_IN", "targetSlug": "country-greece", "targetName": "Ancient Athens", "context": "Set as a conversation at the house of Polemarchus in Piraeus, the Republic reflects the intellectual culture of 4th-century BCE Athens."},
      {"sourceSlug": "the-republic", "sourceName": "The Republic", "verb": "LEADS_TO", "targetSlug": "neoplatonism", "targetName": "Neoplatonism", "context": "Plotinus and the Neoplatonists of the 3rd century CE developed their philosophical system largely as a commentary on and extension of the Republic's metaphysics."},
      {"sourceSlug": "sophists", "sourceName": "The Sophists", "verb": "INFLUENCES", "targetSlug": "the-republic", "targetName": "The Republic", "context": "The Republic's arguments for objective justice are written directly against the sophistic relativism of Thrasymachus, who appears as the dialogue's chief antagonist."}
    ],
    "places": [
      {"name": "Athens, Greece", "role": "Plato's Academy and intellectual context"},
      {"name": "Piraeus, Greece", "role": "Dialogue's dramatic setting"},
      {"name": "Syracuse, Sicily", "role": "Where Plato attempted to train philosopher-kings"}
    ],
    "subjects": ["Political Philosophy", "Ancient Greece", "Metaphysics", "Epistemology", "Ethics", "Education Theory", "Western Philosophy", "Classical Literature", "Utopian Thought", "Justice"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT", "COMPARATIVE_CIVILIZATIONS"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "Plato's Republic is the single most influential text in the history of political philosophy, directly shaping Christian theology, Renaissance governance theory, Enlightenment political thought, and 20th-century debates over democracy and totalitarianism — its core questions about justice, knowledge, and authority remain unresolved and actively debated 2,400 years after its composition.",
      "significanceCategory": "world-changing"
    }
  }
},

"ibn-al-hajib": {
  "filepath": "data/appwrite-export/entities/201-Class-201/201ibn-al-ḥājib.json",
  "slug": "ibn-al-ḥājib",
  "data": {
    "summary": "Ibn al-Ḥājib (1174–1249 CE), full name Jamāl al-Dīn Abū ʿAmr ʿUthmān ibn ʿUmar ibn Abī Bakr al-Mālikī, was a Kurdish Arab grammarian and Maliki jurist whose works on Arabic grammar and Islamic jurisprudence became indispensable texts across the Islamic world for centuries. Born in Esna, Upper Egypt, where his father served as a groom (ḥājib) to a Kurdish military commander — giving rise to his biographical epithet 'son of the doorkeeper' — Ibn al-Ḥājib was educated in Cairo and later taught in Damascus, becoming one of the pre-eminent scholars of his age.\n\nHis grammatical treatise Al-Kāfiya fī al-Naḥw ('The Sufficient Work on Syntax'), composed around 1220, is a dense and systematic analysis of Arabic morphology and syntax that became a cornerstone of the classical Islamic educational curriculum (madrasa). Its companion volume Al-Shāfiya fī ʿIlm al-Taṣrīf ('The Healing Work on Morphology') treated Arabic word-formation with equal rigour. Together these two works attracted hundreds of commentaries and supercommentaries, testimony to their canonical status in traditional Islamic education that persisted from Morocco to Indonesia for over 700 years.\n\nAs a jurist, Ibn al-Ḥājib wrote Mukhtasar Ibn al-Ḥājib, a concise manual of Maliki fiqh (Islamic jurisprudence) that became a standard reference across North and West Africa. During the Mongol campaigns, he was displaced from Damascus to Egypt, where he died. His life traversed the final century of classical Islamic scholarship before the Mongol disruptions, and his texts represented the systematising impulse of high medieval Islamic learning — the drive to compress and render transmissible the accumulated wisdom of five centuries of Arabic intellectual culture.",
    "causes": [
      "The flourishing of madrasa education in the 12th–13th centuries created institutional demand for compact, authoritative texts in grammar and jurisprudence suitable for standardised teaching.",
      "Arabic grammar had developed elaborate competing schools (Basran, Kufan) over centuries; Ibn al-Ḥājib's synthesis aimed to provide a streamlined, logically ordered digest beyond school rivalries.",
      "The decline of the Abbasid Caliphate and the Mongol threat accelerated scholarly efforts to codify and preserve classical Islamic knowledge in portable, compact textual form."
    ],
    "effects": [
      "Al-Kāfiya became one of the most commented-upon Arabic grammatical works in history, generating a vast secondary literature that kept Arabic grammatical tradition alive through the Ottoman period.",
      "His Maliki fiqh manual became foundational across North and West Africa, directly shaping Islamic legal practice in regions from Morocco to Saharan trade networks.",
      "The format of Ibn al-Ḥājib's matn (concise text) works established a model for Islamic scholarly writing — dense, authoritative, commentary-inviting — that structured madrasa education for centuries."
    ],
    "relationships": [
      {"sourceSlug": "ibn-al-ḥājib", "sourceName": "Ibn al-Ḥājib", "verb": "INFLUENCES", "targetSlug": "maliki-school", "targetName": "Maliki School of Jurisprudence", "context": "His Mukhtasar became a standard Maliki legal text across North and West Africa, shaping the transmission of Maliki fiqh through the madrasa tradition."},
      {"sourceSlug": "ibn-al-ḥājib", "sourceName": "Ibn al-Ḥājib", "verb": "OCCURS_IN", "targetSlug": "country-egypt", "targetName": "Egypt", "context": "Born in Esna, educated in Cairo, and dying in Egypt, Ibn al-Ḥājib's scholarly career was rooted in Ayyubid Egypt during its 13th-century cultural flourishing."},
      {"sourceSlug": "ibn-al-ḥājib", "sourceName": "Ibn al-Ḥājib", "verb": "INFLUENCES", "targetSlug": "arabic-grammar", "targetName": "Arabic Grammar Tradition", "context": "Al-Kāfiya and Al-Shāfiya synthesised competing grammatical schools into a systematic framework that became the standard teaching text across the Islamic world."},
      {"sourceSlug": "mongol-invasion", "sourceName": "Mongol Invasions", "verb": "INFLUENCES", "targetSlug": "ibn-al-ḥājib", "targetName": "Ibn al-Ḥājib", "context": "Mongol advances forced Ibn al-Ḥājib from Damascus to Egypt, representative of the wider displacement of scholars that marked the collapse of the classical Islamic scholarly world."},
      {"sourceSlug": "sibawayhi", "sourceName": "Sībawayhi", "verb": "INFLUENCES", "targetSlug": "ibn-al-ḥājib", "targetName": "Ibn al-Ḥājib", "context": "The 8th-century grammarian Sībawayhi's Al-Kitāb was the founding text of Arabic grammatical theory from which Ibn al-Ḥājib's systematic digest descended."}
    ],
    "places": [
      {"name": "Esna, Egypt", "role": "Birthplace"},
      {"name": "Cairo, Egypt", "role": "Education and later career"},
      {"name": "Damascus, Syria", "role": "Teaching career until Mongol displacement"}
    ],
    "subjects": ["Arabic Grammar", "Islamic Jurisprudence", "Medieval Islamic Scholarship", "Maliki School", "Classical Arabic", "Madrasa Education", "North African Islam", "Kurdish History", "Medieval Egypt"],
    "frameworks": ["CULTURAL_TRANSMISSION", "STRUCTURAL_ANALYSIS", "RELIGIOUS_INTERPRETATION"],
    "historicalSignificance": {
      "significanceScore": 6,
      "significanceNarrative": "Ibn al-Ḥājib's grammatical and legal texts entered the standard madrasa curriculum across the Islamic world and directly shaped the transmission of classical Arabic knowledge for over 700 years, preserving intellectual tradition through the Mongol disruptions that ended the high Abbasid era.",
      "significanceCategory": "continental"
    }
  }
},

"old-testament": {
  "filepath": "data/appwrite-export/entities/732-Class-732/732old-testament.json",
  "slug": "old-testament",
  "data": {
    "summary": "The Old Testament — known to Jewish tradition as the Tanakh and comprising the Torah (Law), Nevi'im (Prophets), and Ketuvim (Writings) — is the foundational scriptural corpus of both Judaism and Christianity, and one of the most consequential collections of texts in human history. Its composition spans approximately 1,000 years, from the 10th to the 2nd century BCE, incorporating narrative histories, law codes, prophecy, poetry, wisdom literature, and apocalyptic vision into a unified canonical whole. The Hebrew Bible's 39 books (Protestant reckoning) or 46 books (Catholic, including deuterocanonical texts) record the covenant relationship between the God of Israel and the Jewish people from creation through the Babylonian exile and its aftermath.\n\nThe texts' historical formation is complex: modern critical scholarship identifies multiple authorial layers in the Torah (the Documentary Hypothesis proposes Yahwist, Elohist, Deuteronomist, and Priestly sources), editorial processes stretching across centuries, and the decisive influence of the Babylonian exile (597–538 BCE) on the final shaping of the Pentateuch and Prophetic books. The Septuagint (LXX) — the Greek translation produced in Alexandria c.250–150 BCE — made the Hebrew scriptures accessible to the Hellenistic world and became the primary biblical text for early Christians, directly shaping the New Testament's quotations and theology.\n\nThe Old Testament's cultural reach is immeasurable. Its legal codes influenced Roman law, Magna Carta, and the development of Western jurisprudence. Its poetry — above all the Psalms and Song of Songs — shaped European lyric verse from Dante to Milton. Its historical narratives provided the conceptual vocabulary of covenant, election, and liberation that animated Puritan colonisation of America, abolitionism, civil rights movements, and Zionism. The theologian Karl Barth called it 'the most daring book ever written'; its stories of creation, fall, flood, exodus, kingship, and exile remain among the most pervasive cultural reference points in the modern world.",
    "causes": [
      "The emergence of Israelite monotheism in the 9th–8th centuries BCE, crystallised in prophetic movements opposing Canaanite polytheism, drove the theological systematisation that produced the Deuteronomistic history.",
      "The Babylonian exile (597–538 BCE) created an existential crisis of national identity that motivated the compilation and editing of Israel's scriptures into a coherent canonical form.",
      "Hellenistic cultural expansion under Alexander and his successors created demand for a Greek translation (the Septuagint) that made the Hebrew scriptures accessible to the Mediterranean world."
    ],
    "effects": [
      "The Old Testament provided the conceptual foundation for both Christianity and Islam, making it the direct ancestor of religious traditions encompassing over 4 billion people by the 21st century.",
      "Biblical legal concepts — especially the Decalogue and Deuteronomic law — entered Western legal tradition through medieval canon law, fundamentally shaping European jurisprudence.",
      "The Exodus narrative became the primary symbolic template for liberation movements worldwide, from Puritan New England to African American abolitionism and anti-colonial independence movements."
    ],
    "relationships": [
      {"sourceSlug": "old-testament", "sourceName": "Old Testament", "verb": "LEADS_TO", "targetSlug": "new-testament", "targetName": "New Testament", "context": "Christianity regards the Old Testament as the first covenant fulfilled by Jesus, making the Hebrew Bible indispensable to Christian theology and canonical scripture."},
      {"sourceSlug": "old-testament", "sourceName": "Old Testament", "verb": "INFLUENCES", "targetSlug": "islam", "targetName": "Islam", "context": "The Quran incorporates extensive narratives from the Hebrew Bible — figures of Moses, Abraham, David, Solomon, and Mary feature prominently — rooting Islam in the Abrahamic scriptural tradition."},
      {"sourceSlug": "old-testament", "sourceName": "Old Testament", "verb": "OCCURS_IN", "targetSlug": "country-israel", "targetName": "Ancient Israel and Judah", "context": "The Old Testament's historical narratives are set primarily in Canaan, Egypt, and Mesopotamia, recording the history of the Israelite kingdoms from roughly 1200–400 BCE."},
      {"sourceSlug": "babylonian-exile", "sourceName": "Babylonian Exile", "verb": "INFLUENCES", "targetSlug": "old-testament", "targetName": "Old Testament", "context": "The Babylonian exile (597–538 BCE) was the formative crisis that drove the editorial compilation and theological systematisation of the major Old Testament historical and prophetic books."},
      {"sourceSlug": "old-testament", "sourceName": "Old Testament", "verb": "INFLUENCES", "targetSlug": "western-jurisprudence", "targetName": "Western Legal Tradition", "context": "Biblical legal codes, particularly the Decalogue and Deuteronomic law, entered medieval canon law and shaped the ethical foundations of Western jurisprudence through centuries of ecclesiastical influence."}
    ],
    "places": [
      {"name": "Jerusalem, Israel", "role": "Temple worship and literary centre"},
      {"name": "Babylon, Iraq", "role": "Exile and textual compilation"},
      {"name": "Alexandria, Egypt", "role": "Septuagint translation (c.250 BCE)"}
    ],
    "subjects": ["Hebrew Bible", "Judaism", "Christianity", "Islam", "World Religions", "Ancient Near East", "Biblical Studies", "Ancient History", "Legal History", "Western Literature"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "CULTURAL_TRANSMISSION", "LONGUE_DUREE"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Old Testament is the founding scriptural document of Judaism and Christianity and a major source for Islam — three traditions with over 4 billion combined adherents — and its legal, narrative, and poetic traditions have shaped Western jurisprudence, literature, art, and political thought for over three millennia without interruption.",
      "significanceCategory": "world-changing"
    }
  }
},

"statistics": {
  "filepath": "data/appwrite-export/entities/120-Class-120/120statistics.json",
  "slug": "statistics",
  "data": {
    "summary": "Statistics — the science of collecting, analysing, interpreting, and presenting numerical data — emerged as a formal discipline in the 17th and 18th centuries, though its roots extend to ancient censuses and astronomical data collection. The term itself derives from the German Statistik, coined by Gottfried Achenwall in 1749 to describe the systematic study of state affairs. The discipline's mathematical foundations were laid by Jacob Bernoulli (probability theory, 1713), Abraham de Moivre (normal distribution, 1733), Thomas Bayes (conditional probability, 1763), and Carl Friedrich Gauss (least squares method, 1809).\n\nThe 19th century saw statistics transform from a tool of political economy into a universal scientific method. Adolphe Quetelet applied normal distribution to social data in the 1830s, coining the concept of 'l'homme moyen' (the average man) and founding social statistics. Florence Nightingale's polar area diagrams (1858) used statistical visualisation to demonstrate that battlefield deaths were caused primarily by preventable disease, not combat — directly transforming medical practice and hospital design. By the early 20th century, Karl Pearson's correlation coefficient and Ronald Fisher's development of experimental design and analysis of variance had completed the transition to modern inferential statistics.\n\nThe late 20th century digital revolution produced a third transformation: the emergence of computational statistics, machine learning, and data science. Fisher's frequentist methods — long dominant — face growing competition from Bayesian approaches enabled by cheap computation. Statistical thinking now underpins virtually every empirical science, public health policy, economic forecasting, clinical medicine, and artificial intelligence. The ability to reason under uncertainty with quantified confidence has become arguably the most universally applicable cognitive tool of modernity.",
    "causes": [
      "Early modern state-building created demand for systematic collection of population, taxation, and trade data that required mathematical methods for summarisation and comparison.",
      "The development of probability theory in the 17th century by Pascal, Fermat, and Bernoulli provided the mathematical language necessary for formal statistical reasoning.",
      "The scientific revolution's commitment to quantified observation and experimental measurement created demand for methods to separate systematic signal from random error in data."
    ],
    "effects": [
      "Statistical methods became the foundation of modern scientific methodology across disciplines from physics to sociology, defining standards of evidence and reproducibility in research.",
      "Public health statistics — pioneered by William Farr and Florence Nightingale in the 19th century — enabled systematic analysis of disease causation and transformed modern epidemiology and preventive medicine.",
      "The 20th-century fusion of statistics and computing produced machine learning and data science, technologies that underpin modern AI, financial systems, pharmaceutical development, and digital surveillance."
    ],
    "relationships": [
      {"sourceSlug": "statistics", "sourceName": "statistics", "verb": "INFLUENCES", "targetSlug": "machine-learning", "targetName": "Machine Learning", "context": "Statistical inference and probability theory provide the mathematical foundations of machine learning algorithms, which apply statistical methods at computational scale to pattern recognition and prediction."},
      {"sourceSlug": "statistics", "sourceName": "statistics", "verb": "INFLUENCES", "targetSlug": "epidemiology", "targetName": "Epidemiology", "context": "Statistical methods — particularly chi-square tests, regression analysis, and clinical trial design — are the primary tools of modern epidemiology and evidence-based medicine."},
      {"sourceSlug": "statistics", "sourceName": "statistics", "verb": "OCCURS_IN", "targetSlug": "country-united-kingdom", "targetName": "United Kingdom", "context": "Britain was the dominant centre of statistical development from Francis Galton through Karl Pearson to Ronald Fisher, whose interwar work established the foundations of modern inferential statistics."},
      {"sourceSlug": "carl-friedrich-gauss", "sourceName": "Carl Friedrich Gauss", "verb": "INFLUENCES", "targetSlug": "statistics", "targetName": "statistics", "context": "Gauss's 1809 least squares method for fitting curves to astronomical data became foundational for linear regression and error analysis across all quantitative sciences."},
      {"sourceSlug": "statistics", "sourceName": "statistics", "verb": "LEADS_TO", "targetSlug": "data-science", "targetName": "Data Science", "context": "The fusion of classical statistics with computer science after 1990 produced data science, which applies statistical reasoning to datasets of unprecedented scale."}
    ],
    "places": [
      {"name": "London, England", "role": "Galton, Pearson, Fisher — statistical revolution"},
      {"name": "Göttingen, Germany", "role": "Gauss and mathematical statistics"},
      {"name": "Paris, France", "role": "Laplace, Quetelet — social statistics"}
    ],
    "subjects": ["Mathematics", "Data Science", "Scientific Method", "Epidemiology", "Economics", "Social Science", "Computer Science", "Philosophy of Science", "Modern History", "Quantitative Research"],
    "frameworks": ["CAUSE_AND_EFFECT", "TECHNOLOGICAL_DETERMINISM", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Statistics transformed from a tool of statecraft into the universal scientific method for reasoning under uncertainty, directly enabling modern medicine, epidemiology, economics, and artificial intelligence — making it one of the most practically consequential intellectual developments of the modern era.",
      "significanceCategory": "world-changing"
    }
  }
},

"world-health-organization": {
  "filepath": "data/appwrite-export/entities/370-Class-370/370world-health-organization.json",
  "slug": "world-health-organization",
  "data": {
    "summary": "The World Health Organization (WHO), established on 7 April 1948 as a specialised agency of the United Nations, is the principal intergovernmental body directing international public health. With 194 member states and headquarters in Geneva, Switzerland, the WHO sets global health norms and standards, coordinates responses to international health emergencies, and provides technical assistance to national health ministries worldwide. Its 1948 Constitution famously defined health as 'a state of complete physical, mental, and social well-being — not merely the absence of disease' — the most ambitious and widely cited definition in the history of medicine.\n\nThe WHO's achievements include the single most significant medical triumph in human history: the eradication of smallpox, certified in 1980 after a decade-long global vaccination campaign that immunised hundreds of millions of people. The organisation has coordinated polio near-eradication, overseen global responses to HIV/AIDS (from 1981), SARS (2003), H1N1 influenza (2009), Ebola (2014–2016, 2018–2020), and the COVID-19 pandemic (declared a Public Health Emergency of International Concern in January 2020 and a pandemic in March 2020). The WHO's International Health Regulations, revised in 2005, provide the legal framework for coordinated global disease surveillance and response.\n\nThe WHO's limitations are equally instructive: its dependence on voluntary contributions from wealthy states and private donors (notably the Bill and Melinda Gates Foundation, which became its second-largest funder) has created structural tensions between public health mandates and donor priorities. Its delayed classification of COVID-19 as a pandemic attracted significant criticism. Nevertheless, with an annual budget of approximately $5 billion and a mandate covering everything from nutrition standards to pharmaceutical regulation, the WHO remains the irreplaceable institutional backbone of global health governance.",
    "causes": [
      "The catastrophic health consequences of World War II — mass displacement, epidemic disease, and the collapse of national health infrastructure — made international health coordination a foundational UN priority.",
      "Predecessor organisations (International Sanitary Conferences 1851–1938, League of Nations Health Organisation) demonstrated both the necessity and the feasibility of intergovernmental health cooperation.",
      "Cold War geopolitics created shared incentives for disease surveillance and control: infectious diseases respected no borders, making even ideological adversaries cooperative on health emergencies."
    ],
    "effects": [
      "The WHO-led eradication of smallpox in 1980 — the first and only eradication of a human disease — prevented an estimated 5 million deaths annually and demonstrated that coordinated global health action could defeat ancient killers.",
      "The WHO's International Health Regulations transformed international disease surveillance from voluntary notification to a binding legal framework, establishing the architecture for global pandemic preparedness.",
      "The WHO's essential medicines programme, established 1977, created a model list of priority drugs for global health systems, influencing pharmaceutical policy and drug access in developing nations worldwide."
    ],
    "relationships": [
      {"sourceSlug": "world-health-organization", "sourceName": "World Health Organization", "verb": "FOUNDED_BY", "targetSlug": "united-nations", "targetName": "United Nations", "context": "The WHO was established as a UN specialised agency in April 1948, building on the League of Nations Health Organisation and integrating the earlier International Office of Public Hygiene."},
      {"sourceSlug": "world-health-organization", "sourceName": "World Health Organization", "verb": "LEADS_TO", "targetSlug": "smallpox-eradication", "targetName": "Smallpox Eradication", "context": "The WHO's 1967–1980 Intensified Smallpox Eradication Programme vaccinated over 300 million people and certified the disease eradicated in 1980 — history's only successful disease eradication."},
      {"sourceSlug": "world-health-organization", "sourceName": "World Health Organization", "verb": "OCCURS_IN", "targetSlug": "country-switzerland", "targetName": "Switzerland", "context": "The WHO's headquarters have been located in Geneva, Switzerland since the organisation's founding in 1948, with six regional offices worldwide."},
      {"sourceSlug": "covid-19-pandemic", "sourceName": "COVID-19 Pandemic", "verb": "INFLUENCES", "targetSlug": "world-health-organization", "targetName": "World Health Organization", "context": "The COVID-19 pandemic was the WHO's largest emergency response, exposing both the organisation's critical coordinating role and its structural vulnerabilities to political pressure from member states."},
      {"sourceSlug": "world-health-organization", "sourceName": "World Health Organization", "verb": "INFLUENCES", "targetSlug": "global-health-policy", "targetName": "Global Health Policy", "context": "WHO normative guidance — from essential medicines lists to vaccination schedules to tobacco control conventions — shapes health policy in 194 member states and sets international health standards."}
    ],
    "places": [
      {"name": "Geneva, Switzerland", "role": "Global headquarters since 1948"},
      {"name": "New York, USA", "role": "UN founding context (1945)"},
      {"name": "Africa (Multiple Countries)", "role": "Primary operational context for disease eradication"}
    ],
    "subjects": ["Global Health", "International Organisations", "Public Health", "United Nations", "Epidemiology", "Disease Eradication", "Pandemic Response", "Contemporary History", "International Relations", "Health Policy"],
    "frameworks": ["WORLD_SYSTEMS", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The WHO is the world's primary international health governance institution, responsible for the only disease eradication in human history (smallpox, 1980), the legal framework for global pandemic response, and health standard-setting across 194 nations — making it indispensable to the survival of billions during the 20th and 21st centuries.",
      "significanceCategory": "world-changing"
    }
  }
},

"saint-naum": {
  "filepath": "data/appwrite-export/entities/253-Class-253/253saint-naum.json",
  "slug": "saint-naum",
  "data": {
    "summary": "Saint Naum of Ohrid (c.830–910 CE) was a medieval Bulgarian Christian missionary, theologian, and monastic founder whose work as a direct disciple of Saints Cyril and Methodius made him one of the principal architects of Slavic Christian civilisation. Born in Bulgaria and educated in Constantinople, Naum was among the original Seven Apostles of Bulgaria — the scholars who accompanied Cyril and Methodius on their Moravian mission and who carried Old Church Slavonic literacy and Eastern Orthodox Christianity into the heart of Slavic Europe.\n\nAfter the failure of the Moravo-Pannonian mission following Methodius's death in 885, Naum came to Bulgaria under the patronage of Boris I and later Simeon I. He taught and organised schools in Pliska and Preslav alongside Clement of Ohrid, who is traditionally credited with the final form of the Glagolitic and Cyrillic alphabets. Around 893 CE, Naum relocated to the shores of Lake Ohrid in Macedonia, where in 905 he founded the Monastery of Saint Naum — still standing and venerated today — which became one of the most important centres of Slavic Christian learning, manuscript production, and ecclesiastical culture in the medieval Balkans.\n\nNaum's significance lies at the intersection of language, religion, and political formation: his work helped translate the abstract achievement of the Glagolitic script into a living tradition of Slavic literary culture. The Bulgarian/Ohrid school he helped found trained generations of clergy and scholars who spread Old Church Slavonic (the first literary language of the Slavic world) northward into Serbia, Russia, and beyond. Naum was canonised and his feast day is observed on 23 December in the Eastern Orthodox tradition. His monastery on Lake Ohrid remains one of North Macedonia's most important cultural and pilgrimage sites.",
    "causes": [
      "The Byzantine Empire's missionary strategy to convert the Slavic peoples using their own vernacular language rather than Greek created the political and cultural conditions for Cyril and Methodius's alphabet-creation mission.",
      "Boris I of Bulgaria's 864 CE conversion to Christianity and his desire for an independent Bulgarian ecclesiastical authority created institutional demand for Slavic-language clergy and scripture.",
      "The expulsion of Methodius's disciples from Moravia by Germanic clergy after 885 redirected their literacy mission toward Bulgaria, where political circumstances were more favourable."
    ],
    "effects": [
      "The Old Church Slavonic literary tradition founded by Naum, Clement, and their colleagues became the liturgical language of Eastern Orthodoxy across Bulgaria, Serbia, Russia, and beyond, shaping Slavic civilisation for a millennium.",
      "The Ohrid Literary School produced the first generation of Slavic-language clergy, monks, and scholars, establishing the institutional infrastructure for the Christianisation of the Slavic world.",
      "Naum's Monastery on Lake Ohrid became a model for Balkan monastic culture and remained an active centre of manuscript preservation and ecclesiastical learning through the Ottoman period."
    ],
    "relationships": [
      {"sourceSlug": "saint-naum", "sourceName": "Saint Naum", "verb": "COLLABORATES_WITH", "targetSlug": "clement-of-ohrid", "targetName": "Clement of Ohrid", "context": "Naum and Clement worked together in both the Moravian and Bulgarian missions, co-founding the Ohrid Literary School that became the primary centre of early Slavic Christian education."},
      {"sourceSlug": "saint-naum", "sourceName": "Saint Naum", "verb": "PARTICIPATES_IN", "targetSlug": "cyrillo-methodian-mission", "targetName": "Cyrillo-Methodian Mission", "context": "Naum was one of the original disciples trained by Cyril and Methodius in Constantinople and Moravia, central to the mission that created the first Slavic literary language."},
      {"sourceSlug": "saint-naum", "sourceName": "Saint Naum", "verb": "OCCURS_IN", "targetSlug": "country-north-macedonia", "targetName": "North Macedonia (Ohrid region)", "context": "Naum founded his famous monastery on the southern shores of Lake Ohrid in 905 CE; the site remains in North Macedonia today and is an active Orthodox pilgrimage destination."},
      {"sourceSlug": "boris-i-of-bulgaria", "sourceName": "Boris I of Bulgaria", "verb": "SUPPORTS", "targetSlug": "saint-naum", "targetName": "Saint Naum", "context": "Boris I welcomed Naum to Bulgaria after the Moravian mission collapse, providing patronage for the Slavic literacy mission at the Preslav and Ohrid schools."},
      {"sourceSlug": "saint-naum", "sourceName": "Saint Naum", "verb": "INFLUENCES", "targetSlug": "old-church-slavonic", "targetName": "Old Church Slavonic", "context": "Through his teaching work at Ohrid, Naum helped standardise and transmit Old Church Slavonic as the first literary language of Slavic peoples, establishing a cultural foundation for Eastern Orthodox Slavic civilisations."}
    ],
    "places": [
      {"name": "Ohrid, North Macedonia", "role": "Monastery founder and school base"},
      {"name": "Pliska, Bulgaria", "role": "Teaching and school foundation"},
      {"name": "Moravia (Czech Republic)", "role": "Initial Cyrillo-Methodian mission"}
    ],
    "subjects": ["Eastern Orthodox Christianity", "Slavic History", "Medieval Bulgaria", "Byzantine Missions", "Linguistics", "Monastic History", "North Macedonia", "Medieval Education", "Christian Saints"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "CULTURAL_TRANSMISSION", "COMPARATIVE_CIVILIZATIONS"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Saint Naum was a founding figure of Slavic Christian civilisation — his work helped translate the Cyrillo-Methodian achievement into a living literary tradition that shaped Eastern Orthodox culture from Bulgaria and Serbia to Russia across more than a millennium.",
      "significanceCategory": "continental"
    }
  }
},

"journalism": {
  "filepath": "data/appwrite-export/entities/120-Class-120/120journalism.json",
  "slug": "journalism",
  "data": {
    "summary": "Journalism — the practice of gathering, verifying, contextualising, and disseminating news and information to a public — is one of modernity's defining institutions, functioning simultaneously as a commercial enterprise, a democratic accountability mechanism, and a cultural form. Its origins trace to the Roman Acta Diurna (59 BCE), official daily notices posted in public spaces, but modern journalism proper emerged with the print revolution: the first European newspapers appeared in the early 17th century — the Relation of 1605 in Strasbourg and the Dutch Courante uyt Italien ende Duytslandt in 1618 — followed rapidly by the English Corante (1620) and eventually the first daily newspaper, the Daily Courant, in London in 1702.\n\nThe 18th and 19th centuries established journalism's political and commercial foundations. The American and French revolutions both relied on pamphlet journalism — Thomas Paine's Common Sense (1776) sold 500,000 copies and directly galvanised colonial independence. The partisan press of the 19th century was succeeded by the 'penny press' of the 1830s, which introduced mass-market commercial journalism based on advertising revenue rather than political subsidy. Joseph Pulitzer and William Randolph Hearst's 'yellow journalism' of the 1890s demonstrated journalism's power to mobilise public opinion and, critics argued, even precipitate wars. Concurrent investigative traditions — from Upton Sinclair's The Jungle (1906) to the Pentagon Papers (1971) and Watergate (1972–1974) — established journalism as a 'Fourth Estate' essential to democratic accountability.\n\nThe digital revolution of the 1990s–2010s radically disrupted journalism's commercial model: classified advertising revenues collapsed, circulation fell, and social media platforms captured audience attention while resisting journalistic norms of verification. By 2020, more than 2,000 local US newspapers had closed since 2004. Yet digital journalism also democratised news production globally, enabled citizen reporting, and created new investigative models (ProPublica, The Guardian's open collaborative projects). The tension between journalism's democratic function and its commercial sustainability defines the 21st century's media landscape.",
    "causes": [
      "The invention of the printing press by Gutenberg c.1450 made mass reproduction of news economically feasible and created the technological precondition for periodical journalism.",
      "The rise of literate urban commercial classes in 17th-century Europe created an audience for regular news about trade, politics, and warfare that could sustain subscription-based publications.",
      "The democratic revolutions of the 18th century elevated press freedom to a constitutional value and created political demand for journalism as an accountability mechanism against governmental power."
    ],
    "effects": [
      "The free press became a foundational institution of liberal democracy, formally recognised in the First Amendment (1791) and subsequent constitutional frameworks as essential to informed citizenship and governmental accountability.",
      "Investigative journalism directly triggered major political consequences, including the resignation of US President Nixon after Watergate (1972–1974) and the exposure of institutional abuses from NSA surveillance to the Catholic Church abuse scandals.",
      "The internet's disruption of the advertising-based newspaper model eliminated thousands of local newspapers in the early 21st century, creating 'news deserts' with documented effects on local governance accountability and civic engagement."
    ],
    "relationships": [
      {"sourceSlug": "journalism", "sourceName": "journalism", "verb": "INFLUENCES", "targetSlug": "democracy", "targetName": "Democracy", "context": "A free press is considered essential to democratic governance as the 'Fourth Estate', providing citizens with information and holding governments accountable through investigation and exposure."},
      {"sourceSlug": "journalism", "sourceName": "journalism", "verb": "LEADS_TO", "targetSlug": "watergate-scandal", "targetName": "Watergate Scandal", "context": "Bob Woodward and Carl Bernstein's investigative journalism at the Washington Post in 1972–1974 exposed the Nixon administration's crimes and forced the first presidential resignation in US history."},
      {"sourceSlug": "journalism", "sourceName": "journalism", "verb": "OCCURS_IN", "targetSlug": "country-united-kingdom", "targetName": "United Kingdom", "context": "London's Fleet Street was the global capital of modern journalism from the Daily Courant (1702) through the 20th century, producing journalistic conventions and press freedom debates that shaped global norms."},
      {"sourceSlug": "printing-press", "sourceName": "Printing Press", "verb": "INFLUENCES", "targetSlug": "journalism", "targetName": "journalism", "context": "Gutenberg's printing press (c.1450) made mass reproduction of news physically and economically feasible, creating the technological foundation upon which all periodical journalism was built."},
      {"sourceSlug": "journalism", "sourceName": "journalism", "verb": "INFLUENCES", "targetSlug": "social-media", "targetName": "Social Media", "context": "Social media platforms disrupted journalism's advertising model from 2007 onward while simultaneously enabling citizen journalism, creating profound tensions between verification norms and the speed of digital information spread."}
    ],
    "places": [
      {"name": "London, England", "role": "First daily newspaper (1702), Fleet Street tradition"},
      {"name": "Washington DC, USA", "role": "Watergate; First Amendment protection"},
      {"name": "Strasbourg, France", "role": "Earliest European newspaper (1605)"}
    ],
    "subjects": ["Media History", "Democracy", "Political History", "Communication", "Press Freedom", "Investigative Journalism", "Digital Media", "Modern History", "Technology History", "Civic Society"],
    "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS", "TECHNOLOGICAL_DETERMINISM"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Journalism developed into democracy's essential accountability institution over four centuries — its investigative tradition exposed abuses from presidential crimes to corporate fraud, while its 21st-century crisis of commercial viability has created measurable declines in civic oversight with documented consequences for local governance worldwide.",
      "significanceCategory": "world-changing"
    }
  }
},

}  # end ENRICHMENTS dict


# ─────────────────────────────────────────────────────────────────────────────
# Apply enrichment to file
# ─────────────────────────────────────────────────────────────────────────────

def apply_enrichment(filepath, slug, enrichment_data):
    """Write enrichment to the local JSON file."""
    with open(filepath) as f:
        file_data = json.load(f)

    entity = None
    for e in file_data.get("entities", []):
        if e.get("slug") == slug:
            entity = e
            break

    # Some entities have slightly different slug in file (unicode normalisation)
    if entity is None:
        candidates = file_data.get("entities", [])
        if candidates:
            entity = candidates[0]

    if entity is None:
        print(f"  SKIP — no entity found in {filepath}")
        return False

    current_len = len(entity.get("summary", "") or "")
    if current_len >= 800:
        print(f"  SKIP — already enriched ({current_len}c)")
        return False

    # Apply fields
    entity["summary"] = enrichment_data["summary"]
    entity["importanceScore"] = enrichment_data["historicalSignificance"]["significanceScore"]
    entity["_unsyncedEdits"] = True
    entity["historicalSignificance"] = enrichment_data["historicalSignificance"]

    # Build detailsJson
    details = {}
    dj = entity.get("detailsJson", "")
    if isinstance(dj, str) and dj:
        try:
            details = json.loads(dj)
        except Exception:
            pass
    elif isinstance(dj, dict):
        details = dj

    details["causes"] = enrichment_data["causes"]
    details["effects"] = enrichment_data["effects"]
    details["relationships"] = enrichment_data["relationships"]
    details["places"] = enrichment_data["places"]
    details["subjects"] = enrichment_data["subjects"]
    details["frameworks"] = enrichment_data["frameworks"]

    # Append edit log
    edit_log = details.get("_editLog", [])
    edit_log.append({
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "editorId": EDITOR_ID,
        "sessionId": SESSION_ID,
        "action": "enrich",
        "note": f"VS Code model enrichment: {len(enrichment_data['summary'])}c summary"
    })
    details["_editLog"] = edit_log
    entity["detailsJson"] = json.dumps(details, ensure_ascii=False)
    entity["editorId"] = EDITOR_ID

    # Write back
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(file_data, f, indent=2, ensure_ascii=False)

    return True


def main():
    print("=" * 60)
    print(f"VS Code Model Enrichment — Batch 01")
    print(f"Editor: {EDITOR_ID}")
    print(f"Entities: {len(ENRICHMENTS)}")
    print("=" * 60)

    enriched = 0
    skipped = 0

    for slug, item in ENRICHMENTS.items():
        filepath = item["filepath"]
        file_slug = item.get("slug", slug)

        if not os.path.exists(filepath):
            print(f"\n[{slug}] SKIP — file not found: {filepath}")
            skipped += 1
            continue

        print(f"\n[{slug}]")
        print(f"  Summary: {len(item['data']['summary'])}c")
        print(f"  Score:   {item['data']['historicalSignificance']['significanceScore']}")
        print(f"  File:    {filepath}")

        ok = apply_enrichment(filepath, file_slug, item["data"])
        if ok:
            print(f"  OK — enriched {len(item['data']['summary'])}c")
            enriched += 1
        else:
            skipped += 1

    print("\n" + "=" * 60)
    print(f"RESULTS: {enriched} enriched, {skipped} skipped")
    print(f"Next step: sync_gateway will push to Appwrite")
    print("=" * 60)


if __name__ == "__main__":
    main()
