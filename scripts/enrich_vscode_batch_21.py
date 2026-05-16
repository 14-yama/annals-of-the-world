#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 21 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: aesops-fables, allegory-of-the-cave, almagest, anabasis,
          a-vindication-of-the-rights-of-woman, act-of-supremacy-1534,
          aeneid, annales
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-21-may2026"

ENRICHMENTS = {

"aesops-fables": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780aesops-fables.json",
  "slug": "aesops-fables",
  "data": {
    "summary": "Aesop's Fables is the name given to a large collection of short moral tales attributed — largely by tradition rather than direct historical evidence — to Aesop (Greek: Αἴσωπος), a storyteller said to have lived in ancient Greece in the 6th century BCE, possibly of Phrygian, Thracian, Ethiopian, or slave origin. The fables are characterised by their brevity, their use of anthropomorphised animals (foxes, lions, hares, crows, wolves) as protagonists, and their explicit moral conclusions (the 'epimythium') — lessons about human character, the consequences of arrogance, cleverness vs. brute force, and the dangers of deception that are expressed through animal behaviour rather than direct moral preaching. The most famous include 'The Tortoise and the Hare' (patience overcomes speed), 'The Fox and the Grapes' (the sour grapes of rationalisation), 'The Boy Who Cried Wolf' (the cost of dishonesty), and 'The Ant and the Grasshopper' (preparation vs. improvidence).\n\nThe historical Aesop — if he existed — left no writings; the fables attributed to him were collected, elaborated, and retold by later writers. The earliest systematic Greek collections were by Demetrius of Phalerum (c. 300 BCE) and the Augustan poet Phaedrus (who versified them in Latin). The most influential medieval compilation was Babrius's Greek verse versions (2nd century CE). The Renaissance brought printed editions (Caxton, 1484; Aldus Manutius, 1505) that disseminated the fables across Europe. Jean de La Fontaine's Fables (1668–1694) transformed the tradition into high literary art, and the fables remain living parts of world literature — translated into virtually every language, used in children's education, and serving as the source of idiomatic expressions in dozens of languages.\n\nAesop's Fables represent one of the oldest surviving traditions of popular wisdom literature — a genre with parallels in ancient Mesopotamia (the 'Dialogue of Pessimism'), Egypt (animal fables in the Turin Papyrus), India (the Panchatantra, Jataka tales), and China. The fables' durability across 2,500 years of transmission testifies to the universality of the human situations they address and the power of the animal allegory as a vehicle for social and moral commentary.",
    "causes": [
      "The ancient Greek and Near Eastern tradition of wisdom literature — using short narrative forms (fables, proverbs, parables) to convey practical moral wisdom — provided the cultural context within which Aesop's Fables emerged and were accumulated over centuries.",
      "The social position of the fable as a form that could express criticism of the powerful through animal allegory — allowing commentary on tyranny, deception, and social hierarchy that would be dangerous to express directly — explains both its origins in oral storytelling traditions and its specific character (animals acting out human social situations).",
      "The ancient Greek educational tradition (paideia) — in which fables were used as basic reading and rhetoric exercises — ensured the preservation and transmission of the Aesopic corpus through the educational system, from ancient Greece through Byzantine Christianity and medieval Europe."
    ],
    "effects": [
      "Aesop's Fables entered virtually every European literary and educational tradition after the Middle Ages — through the Latin versions of Phaedrus, the medieval prose Romulus collections, Caxton's English print edition (1484), and La Fontaine's French verse masterpiece (1668–1694) — becoming one of the most widely translated and adapted texts in world literature.",
      "The fables contributed dozens of idiomatic expressions and proverbial wisdom to the major European languages: 'sour grapes', 'crying wolf', 'the grasshopper and the ant', 'the tortoise and the hare' — phrases that remain in common use across languages and cultures, demonstrating the deep penetration of the fables into everyday language.",
      "The Aesopic tradition of animal fable as social and political commentary — in which the behavior of anthropomorphised animals comments on human social structures, power, and moral failures — influenced genres from medieval beast epics (Reynard the Fox) through Orwell's Animal Farm (1945), establishing a lasting literary form for indirect social criticism."
    ],
    "relationships": [
      {"sourceSlug": "aesops-fables", "sourceName": "Aesop's Fables", "verb": "INFLUENCED", "targetSlug": "la-fontaine-fables", "targetName": "La Fontaine's Fables (1668–1694)", "context": "La Fontaine's verse Fables — the most celebrated literary transformation of the Aesopic tradition — drew directly on Aesop (via Phaedrus and the prose tradition) to create the masterwork of French Classical literature."},
      {"sourceSlug": "phaedrus-poet", "sourceName": "Phaedrus (Latin poet, 1st century CE)", "verb": "TRANSMITS", "targetSlug": "aesops-fables", "targetName": "Aesop's Fables (Latin transmission)", "context": "Phaedrus's Latin verse versions of Aesop were the primary vehicle for the fables' transmission into medieval European literary culture."},
      {"sourceSlug": "aesops-fables", "sourceName": "Aesop's Fables", "verb": "PARALLEL_TO", "targetSlug": "panchatantra", "targetName": "Panchatantra (Indian fable tradition)", "context": "The Panchatantra — the ancient Indian collection of animal fables with moral lessons — represents an independent parallel tradition of wisdom literature that shares the Aesopic form but developed independently, illustrating the cross-cultural appeal of the animal fable."}
    ],
    "places": [
      {"name": "Ancient Greece (6th–4th century BCE)", "role": "The origin point of the Aesopic tradition — the Greek oral and literary culture in which the fables were accumulated, collected, and first written down"},
      {"name": "Global (universal transmission)", "role": "The worldwide spread — the fables have been translated into virtually every language and remain part of the literary and educational tradition of every major culture"}
    ],
    "subjects": ["Ancient Literature", "Greek Culture", "Classical Era", "Moral Philosophy", "Oral Tradition", "World Literature", "Fables", "Children's Literature"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Aesop's Fables — the ancient Greek collection of animal fables attributed to a 6th century BCE storyteller — is one of the most widely translated and culturally persistent texts in world literature, transmitted across 2,500 years from ancient Greece through La Fontaine to modern children's education. The fables contributed dozens of idiomatic expressions to European languages and established the animal fable as a lasting vehicle for moral and social commentary, from medieval beast epics to Orwell's Animal Farm.",
      "significanceCategory": "world-changing"
    }
  }
},

"allegory-of-the-cave": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780allegory-of-the-cave.json",
  "slug": "allegory-of-the-cave",
  "data": {
    "summary": "The Allegory of the Cave (Greek: ἡ τοῦ σπηλαίου εἰκών) is a philosophical thought experiment presented by Plato in Book VII of the Republic (c. 375 BCE), in which he uses the image of prisoners chained in a cave watching shadows on a wall to illustrate his theory of knowledge (epistemology), his metaphysical distinction between appearance and reality (the Theory of Forms), and his political philosophy of philosopher-kings. The allegory is perhaps the single most influential passage in the history of Western philosophy, condensing into a vivid narrative the core of Platonic thought and providing a template for subsequent theories of enlightenment, education, and the philosopher's role in society.\n\nIn the allegory, prisoners chained from birth in an underground cave see only shadows cast on the wall before them by objects passing in front of a fire behind them — they mistake these shadows for reality. One prisoner is freed, turns toward the fire (painful for eyes accustomed to shadow), eventually climbs out of the cave into the sunlight, and comes to see the real world, including ultimately the sun itself. This journey represents the philosopher's ascent from opinion (doxa) and perception of sensible things to knowledge (episteme) and understanding of the intelligible Forms, with the sun representing the Form of the Good — the highest object of knowledge and the source of all being and truth. The freed philosopher who returns to the cave to guide the others will be disbelieved, ridiculed, and (as Plato implies) eventually killed — an allusion to Socrates's fate.\n\nThe Allegory of the Cave's influence is immeasurable: it shaped Neoplatonism (Plotinus's ascent of the soul), Christian mysticism (the soul's ascent to God), the Enlightenment's opposition of reason and superstition, Kant's distinction between phenomena and noumena, Marx's concept of ideology as false consciousness, and the contemporary discourse on virtual reality, media manipulation, and epistemic bubbles. Its core image — that what we take for reality may be mere shadow, that truth requires painful intellectual effort, and that those who achieve true understanding face persecution — is one of the foundational metaphors of Western intellectual culture.",
    "causes": [
      "Plato's reaction against the Sophist tradition — which taught that truth was relative and rhetoric was sufficient for political success — and his desire to provide a philosophical foundation for the Socratic conviction that there is objective truth that can be known through reason, not just perceived through the senses.",
      "The experience of Socrates's trial and death (399 BCE) — which demonstrated to Plato that Athenian democracy, guided by opinion rather than knowledge, could murder the most just man — provided the political urgency behind the Republic's argument for philosopher-kings and the Allegory's implicit critique of democratic epistemology.",
      "The Pythagorean mathematical tradition — which held that the deepest truths about reality were mathematical (abstract, intelligible) rather than sensory — provided Plato with the intellectual framework for distinguishing between the sensory world of appearance and the intelligible world of Forms."
    ],
    "effects": [
      "The Allegory of the Cave established the fundamental epistemological question of Western philosophy — the relationship between appearance and reality, sensation and reason, opinion and knowledge — that dominates philosophical debate from Aristotle through Descartes, Kant, and contemporary analytic and continental philosophy.",
      "The allegory's political dimension — the philosopher-king who alone has access to genuine knowledge and must (reluctantly) govern the cave — provided one of the foundational arguments for expert rule vs. democratic participation, shaping debates about political authority and epistemic legitimacy from ancient Athens to contemporary technocracy.",
      "The allegory's metaphor of enlightenment as painful escape from comfortable illusion entered Christian mysticism (the soul's ascent from the world of matter to God), Renaissance humanism, Enlightenment thinking, and contemporary media theory — making it one of the most generative single images in intellectual history, cited from Marx's false consciousness to Baudrillard's simulacra."
    ],
    "relationships": [
      {"sourceSlug": "allegory-of-the-cave", "sourceName": "Allegory of the Cave", "verb": "APPEARS_IN", "targetSlug": "platos-republic", "targetName": "Plato's Republic (c. 375 BCE)", "context": "The Allegory of the Cave appears in Book VII of the Republic — Plato's comprehensive philosophical dialogue on justice, knowledge, and the ideal state — as the central illustration of his epistemology and political philosophy."},
      {"sourceSlug": "plato", "sourceName": "Plato (428–348 BCE)", "verb": "CREATES", "targetSlug": "allegory-of-the-cave", "targetName": "Allegory of the Cave", "context": "Plato authored the allegory as the culminating illustration of the Republic's philosophical argument — drawing together his Theory of Forms, epistemology, and political philosophy in a single vivid narrative."},
      {"sourceSlug": "allegory-of-the-cave", "sourceName": "Allegory of the Cave", "verb": "INFLUENCES", "targetSlug": "neoplatonism", "targetName": "Neoplatonism (Plotinus, 3rd century CE)", "context": "The allegory's image of the soul's ascent from the world of shadows to the divine light was central to Neoplatonist philosophy — particularly Plotinus's mystical metaphysics of the soul's return to the One."}
    ],
    "places": [
      {"name": "Athens, Greece (4th century BCE)", "role": "The context of the Republic's composition — Plato's Academy in Athens, where this foundational philosophical text was written and taught"},
      {"name": "Global (universal intellectual tradition)", "role": "The worldwide influence — the Allegory is cited across every major philosophical, theological, and cultural tradition of the Western and increasingly global intellectual world"}
    ],
    "subjects": ["Philosophy", "Ancient Greece", "Classical Era", "Epistemology", "Plato", "Political Philosophy", "Western Philosophy", "Theory of Knowledge"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Allegory of the Cave (Republic VII, c. 375 BCE) is arguably the single most influential passage in Western philosophy — Plato's vivid narrative of prisoners mistaking shadows for reality, used to illustrate his Theory of Forms, epistemology, and political philosophy of philosopher-kings. Its core image (reality vs. appearance, the painful ascent to truth, the persecution of the enlightened) has shaped every major tradition of Western thought from Neoplatonism through Christian mysticism, Enlightenment epistemology, Marxist ideology critique, and contemporary media theory.",
      "significanceCategory": "world-changing"
    }
  }
},

"almagest": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780almagest.json",
  "slug": "almagest",
  "data": {
    "summary": "The Almagest (Arabic: المجسطي, al-Majisṭī, from Greek: Μεγάλη Σύνταξις, 'Great Compilation') is the comprehensive astronomical treatise written by the Alexandrian mathematician and astronomer Claudius Ptolemy (c. 100–170 CE), completed c. 150 CE. It is the most important astronomical text of antiquity and one of the most influential scientific works in history, remaining the authoritative reference for mathematical astronomy in the Islamic world and Latin Europe for over 1,400 years — until the Copernican Revolution of the 16th century replaced the geocentric Ptolemaic system with the heliocentric model.\n\nThe Almagest's core achievement is a complete mathematical model of all celestial motions as seen from a stationary Earth at the centre of the universe — an Earth-centred (geocentric) cosmology with the Sun, Moon, and five planets (Mercury, Venus, Mars, Jupiter, Saturn) moving in a complex system of circular orbits, epicycles, equants, and deferents, combined to reproduce the observed motions of celestial bodies with remarkable precision. The model was sufficient for predicting planetary positions, eclipses, and the rising and setting of stars with accuracy adequate for navigation, timekeeping, and horoscopic astrology for over a millennium. The Almagest also contains a star catalogue (listing 1,022 stars with coordinates and magnitudes), a comprehensive treatment of mathematical methods (including the first systematic table of trigonometric chords, equivalent to a sine table), and discussion of geography and cosmology.\n\nTransmitted through Arabic translations (the 9th century Arabic title al-Majisṭī — 'the Greatest' — gives the work its modern name) and then into Latin (the 12th century translation by Gerard of Cremona), the Almagest was the foundation of European astronomical education until Copernicus explicitly challenged it in De Revolutionibus (1543), Kepler replaced its circular orbits with ellipses (1609–1619), and Newton provided the gravitational mechanics (1687) that explained why the Copernican system worked. The Almagest thus represents both the pinnacle of ancient mathematical astronomy and the paradigm that the Scientific Revolution had to overthrow.",
    "causes": [
      "The Hellenistic scientific tradition — the program of mathematical description of nature that runs from Euclid through Hipparchus (whose star catalogue and trigonometric methods Ptolemy drew on heavily) — provided both the mathematical tools and the astronomical data that made the Almagest possible.",
      "The practical needs of the ancient world for accurate astronomical prediction — for calendar-making, navigation, religious festival timing, and particularly horoscopic astrology (which required knowing planetary positions at any past or future date) — created the demand for the comprehensive predictive system that the Almagest provided.",
      "The philosophical commitment of Greek astronomy (following Plato and Aristotle) to 'saving the appearances' through circular uniform motion — explaining the apparently irregular motions of the planets while preserving the philosophical principle that heavenly bodies must move in perfect circles — shaped the specific mathematical devices (epicycles, equants) that Ptolemy employed."
    ],
    "effects": [
      "The Almagest established the geocentric Ptolemaic model as the authoritative framework for astronomical understanding for over 1,400 years (from its composition c. 150 CE through Copernicus's De Revolutionibus, 1543) — making it the longest-lasting successful scientific paradigm in history, used by Islamic astronomers, medieval European universities, and navigators well into the 16th century.",
      "The Arabic translation of the Almagest and the Islamic commentary tradition (al-Battānī, Nasir al-Din al-Tusi) not only preserved the work through the European Dark Ages but substantially improved it — correcting errors, refining observations, and developing mathematical tools — before European translators carried it back to Latin Europe in the 12th century.",
      "By serving as the specific paradigm that the Copernican Revolution overthrew — Copernicus explicitly structured De Revolutionibus as a parallel text to the Almagest, retaining many of its mathematical tools while replacing geocentrism with heliocentrism — the Almagest defined the problem that the Scientific Revolution solved, making it a crucial conceptual anchor in the history of science."
    ],
    "relationships": [
      {"sourceSlug": "ptolemy", "sourceName": "Claudius Ptolemy (c. 100–170 CE)", "verb": "AUTHORS", "targetSlug": "almagest", "targetName": "Almagest (c. 150 CE)", "context": "Ptolemy was the author of the Almagest — composing the comprehensive mathematical synthesis of ancient astronomical knowledge that would remain authoritative for over 1,400 years."},
      {"sourceSlug": "almagest", "sourceName": "Almagest", "verb": "OVERTHROWN_BY", "targetSlug": "nicolaus-copernicus", "targetName": "Nicolaus Copernicus (De Revolutionibus, 1543)", "context": "Copernicus's De Revolutionibus — explicitly modelled on the Almagest's structure but replacing Ptolemy's geocentrism with heliocentrism — initiated the Copernican Revolution that ended the Almagest's 1,400-year reign as the authoritative astronomical text."},
      {"sourceSlug": "islamic-golden-age", "sourceName": "Islamic Golden Age (8th–13th centuries)", "verb": "PRESERVES", "targetSlug": "almagest", "targetName": "Almagest (Arabic transmission)", "context": "Islamic scholars translated, preserved, and substantially improved the Almagest — al-Battānī, Thabit ibn Qurra, and Nasir al-Din al-Tusi all worked with the text — before 12th century Latin translations carried it back to European universities."}
    ],
    "places": [
      {"name": "Alexandria, Egypt (Roman period, c. 150 CE)", "role": "The location of Ptolemy's work — the great scholarly centre of the ancient Mediterranean, where the Almagest was composed"},
      {"name": "Baghdad, Islamic Caliphate (9th century CE)", "role": "The hub of the Almagest's Arabic transmission — the Abbasid translation movement in Baghdad that preserved and improved the text before its return to Latin Europe"}
    ],
    "subjects": ["Astronomy", "Ancient Science", "Classical Era", "Mathematics", "Greek Learning", "History of Science", "Geocentrism", "Scientific Revolution"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Almagest (c. 150 CE) — Ptolemy's comprehensive mathematical model of geocentric astronomy — was the authoritative astronomical text for over 1,400 years, from ancient Alexandria through the Islamic Golden Age and medieval European universities until the Copernican Revolution (1543). It represents both the greatest achievement of ancient mathematical astronomy and the paradigm that defined the problem the Scientific Revolution had to solve — making it one of the most consequential scientific texts in history.",
      "significanceCategory": "world-changing"
    }
  }
},

"anabasis": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780anabasis.json",
  "slug": "anabasis",
  "data": {
    "summary": "The Anabasis (Greek: Ἀνάβασις, 'The March Upcountry' or 'The Expedition') is the narrative written by the Athenian historian and soldier Xenophon (c. 430–354 BCE), describing the doomed expedition of the Ten Thousand — a Greek mercenary army hired by Cyrus the Younger to seize the Persian throne from his brother Artaxerxes II — and the remarkable 1,500-mile retreat of the survivors through hostile territory in Asia Minor after Cyrus's death at the Battle of Cunaxa (401 BCE). It is one of the greatest adventure narratives of antiquity, a foundational text of Greek prose literature, and a military classic that directly influenced Alexander the Great's Persian campaigns and, through the centuries, countless subsequent military expeditions.\n\nAfter Cyrus was killed at Cunaxa and the Greek generals treacherously murdered by the Persians, the Ten Thousand found themselves stranded deep in Persia, surrounded by enemies, without leadership, supply lines, or guides. The soldiers elected new leaders (including Xenophon himself, despite being only a civilian volunteer), and under constant harassment by Persian forces, Kardouchian mountain peoples, and harsh terrain and weather, they fought their way northward to the Black Sea coast — the famous cry 'Thalatta! Thalatta!' ('The sea! The sea!') when the first men reached the crest and saw the Black Sea below them is one of the most celebrated moments in ancient literature.\n\nThe Anabasis's military significance is exceptional: Alexander the Great reportedly kept a copy annotated by Aristotle and used the expedition as proof that Greek armies could penetrate the Persian heartland. Napoleon cited it as a model of military leadership under adversity. It also provided the earliest sustained Greek ethnographic account of the peoples of Anatolia, Armenia, and the Black Sea coast, influencing Herodotean geography. Xenophon's account of democratic military decision-making — the soldiers voting on strategy, selecting leaders by merit — is also a remarkable document of Greek democratic practices in extremis.",
    "causes": [
      "Cyrus the Younger's ambition to seize the Persian throne from his brother Artaxerxes II — and his conviction that Greek mercenary hoplites were the finest soldiers in the world — led him to recruit the Ten Thousand Greeks whose subsequent ordeal Xenophon recorded.",
      "The Persian practice of using Greek mercenaries (exploiting Greece's endemic poverty, political instability, and the martial culture of the polis after the Peloponnesian War) meant that large numbers of Greek professional soldiers were available for hire in the Persian civil conflict, creating the conditions for the expedition.",
      "Xenophon's own participation in the expedition — as a young Athenian who joined Proxenus's contingent against Socrates's advice — and his central role in the retreat (elected as one of the generals after the original leaders were killed) gave him the direct experience and leadership perspective that makes the Anabasis a first-person narrative of unusual immediacy."
    ],
    "effects": [
      "The Anabasis demonstrated to the Greek world — and specifically to Philip II of Macedon and Alexander the Great — that a Greek army could penetrate deep into the Persian Empire and fight its way out against Persian opposition: Alexander reportedly said that Xenophon had shown him the road to Persia.",
      "The text became the foundational Greek military manual — studied by Alexander, by Scipio Africanus, by Julius Caesar, and by Napoleon — for its lessons in leadership under extreme adversity, democratic military organisation, and the maintenance of discipline and morale in a retreating army.",
      "The Anabasis's ethnographic passages — describing the Kardouchians (Kurds), the Mossynoikoi, the Chalybians, the Colchians, and many other peoples of Anatolia and the Black Sea coast — provided the most detailed Greek account of these regions and influenced the geographic and ethnographic understanding of northeastern Anatolia through the Byzantine period."
    ],
    "relationships": [
      {"sourceSlug": "xenophon", "sourceName": "Xenophon (c. 430–354 BCE)", "verb": "AUTHORS", "targetSlug": "anabasis", "targetName": "Anabasis", "context": "Xenophon was both the author and a principal subject of the Anabasis — his direct participation in the Ten Thousand's retreat gives the narrative its first-person authority."},
      {"sourceSlug": "anabasis", "sourceName": "Anabasis", "verb": "INSPIRES", "targetSlug": "alexander-the-great", "targetName": "Alexander the Great's Persian Campaigns (334–323 BCE)", "context": "Alexander studied the Anabasis as proof that Greek armies could penetrate the Persian heartland — it directly informed his strategic confidence in undertaking the conquest of Persia."},
      {"sourceSlug": "battle-of-cunaxa", "sourceName": "Battle of Cunaxa (401 BCE)", "verb": "INITIATES", "targetSlug": "anabasis", "targetName": "Anabasis (the retreat narrative)", "context": "Cyrus the Younger's death at Cunaxa transformed the Greek expedition from an offensive into a desperate 1,500-mile retreat — the ordeal that is the subject of Xenophon's narrative."}
    ],
    "places": [
      {"name": "Mesopotamia and Anatolia (401 BCE — the route of retreat)", "role": "The geographic setting of the Anabasis — the extraordinary 1,500-mile march from Cunaxa near Babylon to the Black Sea coast of ancient Trabzon (Trapezus)"},
      {"name": "Athens and the Greek world (literary reception)", "role": "The cultural context of the Anabasis's composition and reception — Xenophon wrote for a Greek audience that understood the military and political significance of the Ten Thousand's achievement"}
    ],
    "subjects": ["Ancient Greece", "Classical Era", "Military History", "Persian Empire", "Greek Literature", "Ancient History", "Xenophon", "10 Thousand"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Anabasis (c. 370 BCE) — Xenophon's account of the Ten Thousand's 1,500-mile retreat from Persia after Cunaxa (401 BCE) — is both a masterpiece of ancient Greek prose and one of the most militarily influential texts in history. Alexander the Great used it as his guide to Persian invasion; Napoleon cited it as a model of leadership under adversity; and the cry 'Thalatta! Thalatta!' ('The sea! The sea!') is one of the most celebrated moments in ancient literature.",
      "significanceCategory": "highly-significant"
    }
  }
},

"a-vindication-of-the-rights-of-woman": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781a-vindication-of-the-rights-of-woman.json",
  "slug": "a-vindication-of-the-rights-of-woman",
  "data": {
    "summary": "A Vindication of the Rights of Woman (1792) is the foundational feminist philosophical text by the English writer Mary Wollstonecraft (1759–1797), written as a direct response to Talleyrand's Report on Public Instruction (1791) which had proposed limiting women's education to domestic subjects. Published in London in 1792, it argues with passionate rationalism that women's apparent intellectual inferiority to men is the product not of natural incapacity but of their systematic exclusion from genuine education — that the same rational nature that Enlightenment thinkers attributed to men also exists in women, and that justice and social progress require extending to women the rights of reason, education, and civic participation.\n\nWollstonecraft's argument draws on the Enlightenment's own foundational principles against itself: if Locke and Rousseau are right that reason is the basis of human dignity and rights, then women — who possess reason as much as men — must be entitled to the same rights and education. Her particular fury is directed at Rousseau's Émile (1762), which prescribed for women (in its section on 'Sophie') an education designed to make them charming, obedient, and pleasing to men — Wollstonecraft argues that this system infantilises women, corrupts their reason, and ultimately harms both women and the men who must live with them. A society in which women are kept ignorant and dependent cannot be truly rational or just.\n\nA Vindication appeared a year after Wollstonecraft's A Vindication of the Rights of Men (1790, a reply to Burke's Reflections on the Revolution in France) and immediately before Mary Wollstonecraft's death in 1797 following the birth of her daughter Mary (later Mary Shelley, author of Frankenstein). The text was largely forgotten in the early 19th century — partly because of the scandal around Wollstonecraft's unconventional life (exposed by her husband William Godwin's memoir after her death) — before being rediscovered by 19th-century women's rights campaigners and becoming the foundational text of modern feminist theory.",
    "causes": [
      "The Enlightenment's articulation of natural rights (Locke), rational education (Rousseau), and universal human dignity — combined with the French Revolution's dramatic assertion of the rights of man — created both the intellectual framework and the immediate political context within which Wollstonecraft demanded that these principles be extended to women.",
      "Wollstonecraft's own experience as a woman who had to work (as governess, school teacher, writer) in a society that provided women virtually no respectable means of self-support — combined with her observation of the consequences of women's lack of education and economic independence — gave her argument its urgency and specificity.",
      "Rousseau's Émile (1762) — particularly its prescriptions for women's education ('Sophie's' section) — was the specific target Wollstonecraft was responding to: the most influential educational philosophy of the Enlightenment had explicitly argued for keeping women in dependence and ignorance, and Wollstonecraft's text is a point-by-point refutation."
    ],
    "effects": [
      "A Vindication of the Rights of Woman established the intellectual framework for the modern feminist movement — its argument that women's subordination is the product of unequal education rather than natural inferiority became the foundational claim of liberal feminism, repeated and developed by John Stuart Mill (The Subjection of Women, 1869), Millicent Fawcett, and the suffrage movements of the 19th and early 20th centuries.",
      "The text's rediscovery in the 19th century — particularly by the American women's rights movement (the Seneca Falls Declaration of 1848 echoes its language) and the British suffrage movement — made Wollstonecraft a foundational figure of feminist history, with the Vindication serving as the origin text of the tradition.",
      "The argument's impact extended beyond women's rights to the broader question of education and equality: Wollstonecraft's insistence that education, not nature, determines human capability became a central principle of progressive educational theory, influencing debates about class, race, and gender in education through the 20th century."
    ],
    "relationships": [
      {"sourceSlug": "mary-wollstonecraft", "sourceName": "Mary Wollstonecraft (1759–1797)", "verb": "AUTHORS", "targetSlug": "a-vindication-of-the-rights-of-woman", "targetName": "A Vindication of the Rights of Woman (1792)", "context": "Wollstonecraft wrote the Vindication in six weeks of intense composition in 1791–1792 — her masterwork and the foundational text of feminist political philosophy."},
      {"sourceSlug": "a-vindication-of-the-rights-of-woman", "sourceName": "A Vindication of the Rights of Woman", "verb": "REFUTES", "targetSlug": "rousseau-emile", "targetName": "Rousseau's Émile (1762)", "context": "The Vindication is in large part a sustained critique of Rousseau's Émile — specifically its prescription that women be educated to be pleasing and submissive rather than rational and independent."},
      {"sourceSlug": "a-vindication-of-the-rights-of-woman", "sourceName": "A Vindication of the Rights of Woman", "verb": "INFLUENCES", "targetSlug": "seneca-falls-declaration", "targetName": "Seneca Falls Declaration of Sentiments (1848)", "context": "The Seneca Falls Declaration — the founding document of American women's rights — draws on Wollstonecraft's arguments and language, marking the Vindication as a direct precursor to the 19th-century women's rights movement."}
    ],
    "places": [
      {"name": "London, England (1792)", "role": "The place of composition and publication — Wollstonecraft wrote the Vindication in London during the revolutionary period, in direct response to the debates ignited by the French Revolution"},
      {"name": "United States and Europe (19th–20th century feminist movements)", "role": "The geographic spread of the text's influence — the American suffrage movement, British feminism, and international women's rights campaigns all drew on the Vindication as their founding text"}
    ],
    "subjects": ["Feminism", "Political Philosophy", "Early Modern Era", "Women's Rights", "Enlightenment", "Education", "English Literature", "18th Century"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "A Vindication of the Rights of Woman (Mary Wollstonecraft, 1792) is the foundational text of modern feminism — the first systematic philosophical argument that women's subordination is the product of unequal education rather than natural inferiority, and that the Enlightenment's principles of reason and natural rights must apply equally to women. Its influence runs directly to the Seneca Falls Declaration (1848), the suffrage movements, and the entire tradition of liberal feminist political theory.",
      "significanceCategory": "world-changing"
    }
  }
},

"act-of-supremacy-1534": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781act-of-supremacy-1534.json",
  "slug": "act-of-supremacy-1534",
  "data": {
    "summary": "The Act of Supremacy (1534) was the parliamentary statute by which the English Parliament formally declared Henry VIII (r. 1509–1547) to be 'the only Supreme Head in Earth of the Church of England' — severing England's ecclesiastical connection to the papacy and establishing the Royal Supremacy that became the constitutional foundation of the Church of England. Passed by the Reformation Parliament on 3 November 1534, the Act completed the process Henry had begun with the Act in Restraint of Appeals (1533), which had cut off appeals from English church courts to Rome, and together they constituted the legal mechanism of the English Reformation — the transfer of supreme ecclesiastical authority from the Pope in Rome to the English monarch.\n\nThe immediate trigger was Henry VIII's desire for an annulment of his marriage to Catherine of Aragon (who had not produced a male heir) and the Pope's refusal to grant it — partly because Catherine was the aunt of the Holy Roman Emperor Charles V, who dominated Italy and intimidated the papacy. Unable to obtain the annulment through Rome, Henry worked with his chief minister Thomas Cromwell to use parliamentary legislation to declare the English church independent of papal authority. Thomas Cranmer, appointed Archbishop of Canterbury in 1533, annulled Henry's marriage to Catherine and validated his marriage to Anne Boleyn. The Act of Supremacy formalised the break and required an oath of supremacy from all subjects (clergy and eventually laity) acknowledging Henry as Supreme Head — those who refused, including Sir Thomas More (Lord Chancellor) and Bishop John Fisher, were executed for treason.\n\nThe Act of Supremacy's consequences were among the most far-reaching in English and world history: it created the Church of England as an institution separate from Rome, initiated the dissolution of the monasteries (1536–1541) and the transfer of their lands to the crown and gentry, sparked the religious controversies of the reign of Edward VI and Mary I that defined English Protestant identity, and permanently altered the constitutional relationship between church and state in England. The Anglican Church created by this Act became the mother church of the worldwide Anglican Communion.",
    "causes": [
      "Henry VIII's desire to annul his marriage to Catherine of Aragon — who had failed to produce a male heir despite multiple pregnancies — and Pope Clement VII's refusal to grant the annulment (under pressure from Catherine's nephew, Holy Roman Emperor Charles V) created the immediate political crisis that Henry resolved through the Royal Supremacy.",
      "Thomas Cromwell's constitutional innovation of using parliamentary legislation to resolve matters previously within ecclesiastical jurisdiction — making Parliament the instrument of the break with Rome — created the legal mechanism that allowed the Act of Supremacy to be passed with the authority of statute law rather than royal decree alone.",
      "The long-term weakening of clerical authority in England — through anticlericalism, Lollardy, and the growing wealth and power of the common law at the expense of canon law — created the structural conditions in which the English break with Rome was possible, even if the immediate trigger was Henry's matrimonial crisis."
    ],
    "effects": [
      "The Act of Supremacy created the Church of England as an institution permanently separate from Rome, establishing the pattern of national churches (Landeskirche) that spread across Protestant Europe and fundamentally restructuring the relationship between political and religious authority in the Western world.",
      "The dissolution of the monasteries (1536–1541) — the direct consequence of the Royal Supremacy and the confiscation of church property — was one of the largest transfers of wealth in English history, creating a new Protestant gentry landholding class that had a material stake in the Reformation and made any restoration of Catholicism economically disruptive.",
      "The requirement of the oath of supremacy — and the executions of Thomas More and John Fisher for refusing it — established the principle that the monarch's ecclesiastical authority could demand personal loyalty from subjects on pain of death, creating the martyrdom narratives (More and Fisher were eventually canonised) that shaped both Catholic and Protestant English identities for centuries."
    ],
    "relationships": [
      {"sourceSlug": "henry-viii-england", "sourceName": "Henry VIII (1491–1547)", "verb": "USES", "targetSlug": "act-of-supremacy-1534", "targetName": "Act of Supremacy (1534)", "context": "Henry VIII was the driving force behind the Act of Supremacy — his matrimonial crisis, personal authority, and political will (working through Cromwell and the Reformation Parliament) produced the Act."},
      {"sourceSlug": "act-of-supremacy-1534", "sourceName": "Act of Supremacy (1534)", "verb": "CREATES", "targetSlug": "church-of-england", "targetName": "Church of England", "context": "The Act of Supremacy is the foundational constitutional act of the Church of England — establishing the Royal Supremacy and the Church's independence from Rome."},
      {"sourceSlug": "thomas-more", "sourceName": "Thomas More (1478–1535)", "verb": "EXECUTED_FOR_REFUSING", "targetSlug": "act-of-supremacy-1534", "targetName": "Oath of Supremacy (Act of Supremacy)", "context": "Thomas More's refusal to swear the oath of supremacy — and his subsequent execution for treason in 1535 — is the most famous individual consequence of the Act and created one of the most celebrated martyrdom narratives of the English Reformation."}
    ],
    "places": [
      {"name": "Westminster, England (1534)", "role": "The place of legislation — the Reformation Parliament at Westminster passed the Act of Supremacy, making England's break with Rome a matter of English constitutional law"},
      {"name": "England (and the global Anglican Communion)", "role": "The primary sphere of consequence — England's church, state, and culture were transformed by the Act, and through the Anglican Communion, its effects spread globally"}
    ],
    "subjects": ["English Reformation", "Tudor England", "Early Modern Era", "Church and State", "Parliamentary History", "Christianity", "Political History", "Religious History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Act of Supremacy (1534) — declaring Henry VIII 'Supreme Head of the Church of England' — was the constitutional foundation of the English Reformation, severing England from Rome and creating the Church of England. Its consequences included the dissolution of the monasteries (one of the largest property transfers in English history), the executions of Thomas More and John Fisher, and the creation of the Anglican Church that became the mother institution of the worldwide Anglican Communion. It stands as one of the most consequential pieces of legislation in English history.",
      "significanceCategory": "world-changing"
    }
  }
},

"aeneid": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782aeneid.json",
  "slug": "aeneid",
  "data": {
    "summary": "The Aeneid (Latin: Aeneis) is the Latin epic poem composed by Virgil (Publius Vergilius Maro, 70–19 BCE) between approximately 29 BCE and his death in 19 BCE, left in an unfinished state at his death (Virgil reportedly asked for it to be destroyed; Augustus ordered it preserved). Twelve books long in hexameter verse — modelled on Homer's Iliad and Odyssey — it recounts the legendary journey of the Trojan hero Aeneas from the fall of Troy to his eventual settlement in Latium (central Italy), the region that would become Rome, thus providing a mythological founding narrative for the Roman people and the Julian dynasty to which Augustus Caesar claimed descent. It is widely regarded as the greatest work of Latin literature and one of the supreme achievements of world poetry.\n\nThe Aeneid's first six books follow Aeneas's wanderings (consciously parallel to Odysseus's journey in the Odyssey) — from Troy through Carthage (where Aeneas abandons Queen Dido, who kills herself in despair) to Sicily and finally to the Underworld, where the shade of his father Anchises shows him the future glory of Rome and the souls of the great Romans yet to be born. The second six books (parallel to the Iliad) recount the wars Aeneas must fight in Latium to establish his destined city — wars characterised by tragic heroism on both sides, ending with the morally ambiguous killing of the Italian hero Turnus. The poem's central tension — between fate (fatum) and human will, between pietas (duty to gods, family, and state) and personal desire — gives it a gravity and pathos that transcends its political function as Augustan propaganda.\n\nThe Aeneid's cultural influence is incalculable: it was the central text of Roman education (every educated Roman knew it by heart), the model for medieval Latin epic, the inspiration for Dante's Divine Comedy (where Virgil serves as Dante's guide through Hell and Purgatory), and a foundational text of Western literary culture that has been continuously read, translated, and adapted for over 2,000 years.",
    "causes": [
      "Augustus Caesar's need for a national epic that would legitimise his regime, connect the Julian dynasty to divine origins (through Aeneas, son of Venus, ancestor of Julius Caesar), and celebrate Rome's destined greatness — and his patronage of Virgil through Maecenas — provided both the political motivation and the material support for the Aeneid's composition.",
      "Virgil's long meditation on Roman identity — his earlier Eclogues and Georgics had already engaged with the relationship between Rome and its landscape, its past, and its political destiny — prepared him for the Aeneid's comprehensive mythological treatment of Roman origins and the costs of empire.",
      "The Homeric tradition — the Iliad and Odyssey's established framework of heroic epic — provided the form and many of the specific models (Aeneas as a second Odysseus in Books 1–6, a second Achilles in Books 7–12) that Virgil consciously drew on and transformed, creating a work that engaged in sustained dialogue with the Greek epic tradition."
    ],
    "effects": [
      "The Aeneid became the central text of Roman education — memorised by every schoolboy, quoted by every educated Roman, used as a vehicle for teaching Latin grammar and rhetoric — for the entire duration of the Roman Empire, making it the cultural foundation of Roman literary identity.",
      "Dante Alighieri's choice of Virgil as his guide through Hell and Purgatory in the Divine Comedy (c. 1308–1320) elevated the Aeneid to the status of the greatest pre-Christian poem in the Christian humanist tradition, ensuring its centrality to medieval and Renaissance culture and making it the bridge between classical antiquity and Christian Europe.",
      "The Aeneid's portrait of Dido — abandoned by Aeneas for reasons of fate and duty, dying by her own hand — became one of the most resonant figures in Western literature, inspiring Purcell's opera Dido and Aeneas (1689), Christopher Marlowe's Dido, Queen of Carthage, and countless other artistic treatments of the tragedy of love sacrificed to political necessity."
    ],
    "relationships": [
      {"sourceSlug": "virgil", "sourceName": "Virgil (70–19 BCE)", "verb": "AUTHORS", "targetSlug": "aeneid", "targetName": "Aeneid (29–19 BCE)", "context": "Virgil was the author of the Aeneid — commissioned in the context of Augustus's cultural program and worked on for the last decade of his life, left unfinished at his death."},
      {"sourceSlug": "augustus-caesar", "sourceName": "Augustus Caesar (63 BCE–14 CE)", "verb": "PATRONISES", "targetSlug": "aeneid", "targetName": "Aeneid (Augustan epic)", "context": "Augustus's patronage — through Maecenas and his direct interest in the project — was essential to the Aeneid, which served as the cultural and mythological legitimation of the Augustan regime."},
      {"sourceSlug": "aeneid", "sourceName": "Aeneid", "verb": "INSPIRES", "targetSlug": "dantes-divine-comedy", "targetName": "Dante's Divine Comedy (c. 1308–1320)", "context": "Dante chose Virgil as his guide through Hell and Purgatory in the Divine Comedy — the most important acknowledgement of the Aeneid's status as the supreme pre-Christian poem and the bridge between antiquity and medieval Christian culture."}
    ],
    "places": [
      {"name": "Rome (Augustan Italy, 29–19 BCE)", "role": "The context of composition — the Augustan Rome of cultural renovation and political consolidation, within which Virgil worked on the national epic"},
      {"name": "Global (Western literary tradition)", "role": "The sphere of influence — the Aeneid has been continuously read and adapted for over 2,000 years, remaining central to Western literary culture from Roman schoolrooms to contemporary translations"}
    ],
    "subjects": ["Latin Literature", "Ancient Rome", "Classical Era", "Epic Poetry", "Augustan Age", "Roman History", "World Literature", "Virgil"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "RELIGIOUS_INTERPRETATION"],
    "historicalSignificance": {
      "significanceScore": 10,
      "significanceNarrative": "The Aeneid (Virgil, 29–19 BCE) is widely regarded as the greatest work of Latin literature — Rome's national epic, connecting the Trojan Aeneas through the Julian dynasty to Augustus Caesar, and providing the foundational mythological narrative of Roman origins. The central text of Roman education for centuries, the model for Dante's choice of Virgil as guide in the Divine Comedy, and a continuous presence in Western literary culture for over 2,000 years, the Aeneid is one of the supreme achievements of world poetry.",
      "significanceCategory": "world-changing"
    }
  }
},

"annales": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782annales.json",
  "slug": "annales",
  "data": {
    "summary": "The Annals (Latin: Annales; full title: Ab excessu divi Augusti, 'From the Death of the Divine Augustus') is the major historical work of the Roman historian Publius Cornelius Tacitus (c. 56–120 CE), covering the history of the Roman Empire from the death of Augustus (14 CE) through the reigns of Tiberius, Caligula, Claudius, and Nero to 68 CE. Though originally comprising eighteen books, only books 1–4 and 5 (incomplete), 11–15, and 16 (incomplete) survive — roughly covering the reigns of Tiberius (books 1–6) and the latter part of Claudius's reign and most of Nero's (books 11–16). The Annals is regarded as one of the greatest historical works in the Western tradition — Tacitus's penetrating psychological analysis of power and tyranny, his terse and epgrammatic Latin prose, and his portrait of the Julio-Claudian dynasty under the distorting pressure of autocratic rule have made it a foundational text of political realism for two millennia.\n\nTacitus wrote in the tradition of Thucydides — interpreting events through the analysis of political psychology, power, and human nature rather than divine intervention — but with a distinctly Roman senatorial perspective: a profound sense of loss for the Roman Republic and bitter observation of how absolute power corrupts both the ruler (Tiberius, who retreats into paranoia and perversion) and the ruled (the senators who debase themselves in sycophancy and denunciation). The Annals contains some of the most vivid portrait-painting in ancient literature: Tiberius's grim suspicion, Claudius's odd mixture of scholarship and weakness, Nero's descent into murder and artistic megalomania, the Stoic resistance of Seneca and Thrasea Paetus, and the brilliant administrative careers of Germanicus and Corbulo.\n\nThe Annals' influence on Western political thought is immense: Machiavelli drew on Tacitus for his analysis of power, the 16th–17th century 'Tacitist' movement used him to analyse statecraft and tyranny, and Montesquieu, Gibbon, and the American Founders all read Tacitus as a guide to republican virtue and the dangers of imperial power. The work also contains the earliest pagan literary reference to Jesus Christ and the Christians ('Christians' named from 'Christus, who had undergone the death penalty in the reign of Tiberius, by sentence of the procurator Pontius Pilate', Annals 15.44).",
    "causes": [
      "The experience of the Roman senatorial class under the Flavian emperors (Domitian in particular) — which Tacitus himself lived through, observing the Senate's degradation and the execution of his political friends — gave him the bitter personal knowledge of tyranny that informs the Annals' analysis of the Julio-Claudian court.",
      "The end of Domitian's reign (96 CE) and the relative freedom of Nerva and Trajan's early years provided the political space within which Tacitus could write about the principate's origins with the critical distance that the Annals required — he explicitly notes at the opening that he is writing 'without anger and without partiality'.",
      "The Roman historiographical tradition — especially Thucydides (in the Greek tradition) and Livy, Sallust, and the lost historians of the Julio-Claudian period — provided both the forms and the immediate sources that Tacitus worked with, though he transformed the tradition through his distinctive psychological analysis and rhetorical style."
    ],
    "effects": [
      "The Annals established the dominant modern image of the Julio-Claudian emperors — particularly Tiberius (cold, suspicious, paranoid), Caligula (whom Tacitus barely covers but whose character was shaped by the broader context), Claudius (weak, manipulated by his wives and freedmen), and Nero (megalomaniacal, artistic, murderous) — an image that has shaped historical imagination from the Renaissance to I, Claudius (Robert Graves, 1934).",
      "The 16th–17th century 'Tacitist' political movement — in which humanists like Justus Lipsius, Francis Bacon, and others used Tacitus as a guide to understanding and surviving absolutist courts — made the Annals a central text of early modern political thought, influencing the development of both statecraft theory (Machiavelli's relationship to Tacitus) and republican political theory.",
      "The Annals' passage on the Christians (15.44) — describing Nero's persecution of Christians after the Great Fire of Rome (64 CE) and naming Jesus as the origin of the movement — is one of the most important non-Christian sources for early Christianity, used by historians to establish the historicity of Jesus and the early Christian community in Rome."
    ],
    "relationships": [
      {"sourceSlug": "tacitus", "sourceName": "Tacitus (c. 56–120 CE)", "verb": "AUTHORS", "targetSlug": "annales", "targetName": "Annals (Tacitus)", "context": "Tacitus was the author of the Annals — writing in the early 2nd century CE about the principate's origins and the Julio-Claudian dynasty's corruption of Roman republican values."},
      {"sourceSlug": "annales", "sourceName": "Annals (Tacitus)", "verb": "DESCRIBES", "targetSlug": "nero", "targetName": "Emperor Nero (r. 54–68 CE)", "context": "Tacitus's portrait of Nero in the Annals — his persecution of Christians, murder of his mother Agrippina, and megalomania — has shaped the dominant modern image of one of Rome's most notorious emperors."},
      {"sourceSlug": "annales", "sourceName": "Annals (Tacitus)", "verb": "INFLUENCES", "targetSlug": "machiavelli", "targetName": "Niccolò Machiavelli (1469–1527)", "context": "Machiavelli's political analysis in the Prince and Discourses draws heavily on Tacitus — using the Annals' account of imperial power and court politics as source material for his theories of political realism."}
    ],
    "places": [
      {"name": "Rome (early 2nd century CE)", "role": "The context of composition — Tacitus writing under Trajan's comparatively free reign about the principate's Julio-Claudian origins"},
      {"name": "European intellectual tradition (Renaissance onwards)", "role": "The sphere of influence — the Annals' reception by Renaissance humanists, early modern statesmen, and Enlightenment political thinkers made it a foundational text of Western political thought"}
    ],
    "subjects": ["Roman History", "Latin Literature", "Classical Era", "Ancient Rome", "Historiography", "Political Thought", "Julio-Claudian Dynasty", "Early Christianity"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "The Annals (Tacitus, early 2nd century CE) — the great historical analysis of the Julio-Claudian dynasty from Augustus's death to Nero's fall — is one of the supreme achievements of ancient historiography, combining penetrating psychological analysis of power with terse, epigrammatic prose. Its portraits of Tiberius, Claudius, and Nero have shaped historical imagination for two millennia; its 'Tacitist' reception in the Renaissance influenced early modern political thought; and its passage on the Christians (15.44) is one of the most important pagan sources for early Christianity.",
      "significanceCategory": "world-changing"
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
