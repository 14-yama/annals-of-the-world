#!/usr/bin/env python3
"""
VS Code Model Enrichment — Batch 25 (8 entities)
Authored by Claude Sonnet 4.6 via GitHub Copilot — May 16, 2026

Entities: de-rerum-natura, crito, al-muwaa, de-administrando-imperio,
          akbarnama, a-brief-history-of-time, digenes-akritas,
          dialogue-concerning-heresies-1529
"""

import json, os, sys, time

EDITOR_ID = "claude-sonnet-4.6·cloud·GH#vscode"
SESSION_ID = "vscode-batch-25-may2026"

ENRICHMENTS = {

"de-rerum-natura": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780de-rerum-natura.json",
  "slug": "de-rerum-natura",
  "data": {
    "summary": "De Rerum Natura ('On the Nature of Things') is the philosophical poem in six books by the Roman poet Titus Lucretius Carus (c. 99–55 BCE), written in dactylic hexameter and addressed to the aristocratic patron Gaius Memmius — the most systematic and complete surviving exposition of Epicurean philosophy in antiquity, and one of the most extraordinary works of Latin literature. In approximately 7,400 lines, Lucretius expounds the Epicurean atomic theory (derived from Democritus and Epicurus): that the universe consists entirely of void and atoms (infinitely small, indestructible particles of matter) in perpetual motion; that the gods exist but are entirely indifferent to human affairs; that the soul is material and mortal (dissolving with the body at death); that death is therefore nothing to fear; and that the purpose of philosophy is the achievement of ataraxia (tranquility of mind) through the rational understanding of nature and the liberation from the fear of death and divine punishment.\n\nLucretius wrote De Rerum Natura with passionate intellectual conviction and extraordinary poetic power — his poem opens with the famous invocation to Venus as the generative force of nature, and his arguments are illustrated with some of the most vivid and memorable passages in Latin poetry: the description of the Epicurean sage Epicurus breaking through the 'flaming walls of the world' to understand the nature of the cosmos; the meditation on the 'plague of Athens' (taken from Thucydides) that closes the poem; and the great analysis of human civilisation's development from primitive origins in Book 5, which anticipates the Enlightenment's secular account of cultural progress. The poem was apparently left unfinished at Lucretius's death (tradition says he died by suicide after being driven mad by a love potion).\n\nDe Rerum Natura was lost during the medieval period and recovered in 1417 by the humanist Poggio Bracciolini in a German monastery — the rediscovery described in Stephen Greenblatt's The Swerve (2011). Its influence on Renaissance and early modern thought — on Machiavelli (who copied the poem by hand), on Giordano Bruno's infinite universe, on Galileo's materialism, and on the Enlightenment's secular, materialist philosophy — was transformative: the text's ancient atomist, anti-theological materialism gave early modern natural philosophers a classical authority for their break with Aristotelian physics and Christian cosmology.",
    "causes": [
      "Epicurean philosophy's programme of liberating humans from the fear of death and divine punishment through rational understanding of nature — Epicurus's argument that atomic theory removes the basis for religious fear by showing the soul is mortal and the gods indifferent — gave Lucretius his philosophical mission: to spread Epicurean enlightenment in Latin.",
      "The political crisis of the late Roman Republic — the violence, civil wars, and popular religious credulity that Lucretius saw around him — gave his philosophical project its urgency: the liberation of humanity from religio (religious superstition, literally 'binding') was for Lucretius a social as well as individual good, cutting the roots of the violence and cruelty done in religion's name.",
      "The tradition of didactic hexameter poetry — Hesiod's Works and Days, Empedocles's On Nature — provided Lucretius with the literary form within which to present philosophical content: the poem form made the abstract doctrines of Epicurean physics accessible and memorable, and Lucretius's invocation of the Muse acknowledged that he was bringing Greek philosophy into the Latin literary tradition."
    ],
    "effects": [
      "Poggio Bracciolini's rediscovery of De Rerum Natura in 1417 — introducing the complete text to the Renaissance — was, as Stephen Greenblatt has argued, a transformative moment in Western intellectual history: Lucretius's ancient atomist materialism gave Renaissance natural philosophers a classical authority for challenging Aristotelian physics and Christian cosmology.",
      "Lucretius's atomic theory and secular account of the universe's origin and operation influenced Galileo's physics, Gassendi's revival of atomism, Newton's corpuscular theory, and ultimately the development of modern atomic theory — an ancient philosophical framework that proved scientifically productive when rehabilitated in the early modern period.",
      "The poem's secular, materialist account of human civilisation's development from primitive origins (Book 5) — anticipating the Enlightenment's stadial theory of history — influenced Enlightenment thinkers from Montaigne and Giordano Bruno through Voltaire and Diderot, contributing to the intellectual framework of secular progress that underpins modern Western thought."
    ],
    "relationships": [
      {"sourceSlug": "lucretius", "sourceName": "Lucretius (c. 99–55 BCE)", "verb": "AUTHORS", "targetSlug": "de-rerum-natura", "targetName": "De Rerum Natura (c. 60 BCE)", "context": "Lucretius wrote De Rerum Natura as a passionate exposition of Epicurean philosophy — apparently leaving it unfinished at his death, with the final form we have perhaps due to Cicero's editorial care."},
      {"sourceSlug": "de-rerum-natura", "sourceName": "De Rerum Natura", "verb": "REDISCOVERED_BY", "targetSlug": "poggio-bracciolini", "targetName": "Poggio Bracciolini (1417)", "context": "Poggio Bracciolini's discovery of a manuscript of De Rerum Natura in a German monastery in 1417 reintroduced the complete text to Europe after its medieval disappearance — a rediscovery that significantly influenced Renaissance natural philosophy."},
      {"sourceSlug": "epicurus", "sourceName": "Epicurus (341–270 BCE)", "verb": "FOUNDS_PHILOSOPHY_OF", "targetSlug": "de-rerum-natura", "targetName": "De Rerum Natura", "context": "De Rerum Natura is the fullest surviving exposition of Epicurus's atomic theory and ethical philosophy — Lucretius's poem transmitted Epicurean physics to the Renaissance through the Latin literary tradition."}
    ],
    "places": [
      {"name": "Rome (c. 60 BCE, composition)", "role": "The context of composition — Lucretius writing in the late Republic, addressing his patron Memmius with a philosophical poem designed to liberate Roman aristocrats from religio"},
      {"name": "European intellectual tradition (1417 rediscovery, Renaissance–Enlightenment)", "role": "The sphere of De Rerum Natura's influence after Poggio's rediscovery — from Renaissance Neoplatonism and Galileo through the French Encyclopédistes and the modern scientific tradition"}
    ],
    "subjects": ["Roman Philosophy", "Classical Era", "Epicureanism", "Ancient Rome", "Atomic Theory", "Latin Literature", "Materialism", "Natural Philosophy"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 9,
      "significanceNarrative": "De Rerum Natura (Lucretius, c. 60 BCE) is the most complete surviving exposition of ancient Epicurean atomic philosophy — a work whose medieval disappearance and 1417 rediscovery by Poggio Bracciolini gave Renaissance natural philosophers a classical authority for challenging Aristotelian physics and Christian cosmology. Its influence on Galileo, Gassendi's revival of atomism, and Enlightenment secular materialism makes it one of the most consequential texts in the history of Western natural philosophy.",
      "significanceCategory": "world-changing"
    }
  }
},

"crito": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780crito.json",
  "slug": "crito",
  "data": {
    "summary": "The Crito is a short philosophical dialogue by Plato (c. 428–348 BCE), written c. 395 BCE as part of his early Socratic dialogues — set in the days after Socrates's condemnation by the Athenian jury and before his execution (399 BCE), depicting a conversation between Socrates and his wealthy friend Crito in the prison cell. Crito has arranged for Socrates's escape from prison and urges him to flee to safety; Socrates declines to escape, arguing that to do so would be unjust — a violation of his lifelong commitment to Athens, the laws, and the principle that one should never do wrong even in response to wrong done to one. The dialogue is a foundational text in political philosophy and legal theory, posing the central questions of civic obligation, the duty to obey the law, the social contract, and the limits of individual conscience against collective authority.\n\nSocrates's refusal in the Crito takes the form of an imagined speech by the personified 'Laws of Athens', who argue that Socrates has implicitly accepted a social contract with Athens by choosing to live there his entire adult life; that the Laws are like parents who raised him and whom he owes filial loyalty; and that an unjust act (breaking the laws by escaping) cannot be justified by the injustice done to him (the unjust verdict). The argument is remarkable for its principled consistency — Socrates has spent his life arguing that it is worse to do wrong than to suffer wrong, and the Crito dramatises his living out that principle at the cost of his life. The dialogue also presents the tension between obedience to law and individual moral conscience that remains one of the central problems of political philosophy.\n\nThe Crito is one of the most frequently read Platonic dialogues in philosophical education precisely because its central argument — when, if ever, is civil disobedience justified? — is perennially relevant and directly confronts the question of the individual's relationship to the state. Thoreau's 'Civil Disobedience' (1849), Gandhi's satyagraha, and Martin Luther King's Letter from Birmingham Jail all engage with the tradition the Crito establishes.",
    "causes": [
      "Socrates's trial and conviction by the Athenian jury (399 BCE) — on charges of impiety and corrupting the youth, in the politically charged aftermath of Athens's defeat in the Peloponnesian War and the Thirty Tyrants' oligarchic interlude — was the dramatic context that made the Crito's question of civic obligation urgent and personal.",
      "Plato's deepening philosophical project in the early dialogues — the series of conversations exploring Socratic ethics (Euthyphro, Apology, Crito, Phaedo) as a connected narrative of Socrates's last days — gave the Crito its place as the dialogue that depicts Socrates's ethical decision in the interval between conviction and death.",
      "Athenian legal culture and its democratic institutions — which Socrates himself had used throughout his life (serving as a soldier, participating in the assembly, fulfilling civic duties) — provided the basis for his argument that his continued residence in Athens represented a tacit acceptance of its legal authority."
    ],
    "effects": [
      "The Crito established the philosophical tradition of asking whether civic obligation requires obedience to laws one believes unjust — and whether individual conscience can override collective legal authority — a tradition that runs through Cicero's De Re Publica, Aquinas's theory of unjust laws, Locke's right to resistance, and 19th–20th century civil disobedience theory.",
      "Thoreau's 'Resistance to Civil Government' (later 'Civil Disobedience', 1849) — the foundational text of modern civil disobedience theory — explicitly grapples with the Socratic framework: is an individual morally bound to obey laws that violate conscience? Thoreau, Gandhi, and King all answer differently than Socrates, but all define their positions in relation to his.",
      "The Crito's imagined speech of the Laws — its social contract argument that living in a city implicitly constitutes acceptance of its authority — is one of the earliest formulations of social contract theory, anticipating Hobbes, Locke, and Rousseau's more systematic treatments of the contractual basis of political obligation."
    ],
    "relationships": [
      {"sourceSlug": "plato", "sourceName": "Plato (c. 428–348 BCE)", "verb": "AUTHORS", "targetSlug": "crito", "targetName": "Crito (c. 395 BCE)", "context": "Plato wrote the Crito as part of his early Socratic dialogues — a dramatic recreation of Socrates's philosophical decision to refuse escape and accept execution."},
      {"sourceSlug": "socrates", "sourceName": "Socrates (469–399 BCE)", "verb": "DEPICTED_IN", "targetSlug": "crito", "targetName": "Crito", "context": "The Crito depicts Socrates in his prison cell declining to escape, arguing that civic obligation requires acceptance of the Laws of Athens even when those laws are applied unjustly."},
      {"sourceSlug": "crito", "sourceName": "Crito", "verb": "INFLUENCES", "targetSlug": "henry-david-thoreau", "targetName": "Henry David Thoreau ('Civil Disobedience', 1849)", "context": "Thoreau's theory of civil disobedience — the individual's right to refuse obedience to unjust laws — explicitly grapples with the Socratic tradition, reversing Socrates's conclusion while inheriting his framework."}
    ],
    "places": [
      {"name": "Athens (prison of Socrates, 399 BCE)", "role": "The dramatic setting of the Crito — Socrates's prison cell, where Crito visits him the morning before his execution with the offer of escape"},
      {"name": "Western political philosophy (ongoing influence)", "role": "The sphere of the Crito's influence — the foundational text for the tradition of civic obligation and civil disobedience theory that runs through Aquinas, Locke, Thoreau, Gandhi, and King"}
    ],
    "subjects": ["Greek Philosophy", "Classical Era", "Political Philosophy", "Socrates", "Athens", "Ancient Greece", "Ethics", "Legal Theory"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Crito (Plato, c. 395 BCE) is the foundational text of the philosophical tradition addressing civic obligation and civil disobedience — posing the question of whether an individual is morally bound to obey laws believed unjust. Socrates's principled refusal to escape prison and his social contract argument for accepting the Laws of Athens established the framework within which Thoreau, Gandhi, and Martin Luther King defined their theories of justified civil disobedience.",
      "significanceCategory": "highly-significant"
    }
  }
},

"al-muwaa": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780al-muwa\u1e6d\u1e6da\u02bc.json",
  "slug": "al-muwaa",
  "data": {
    "summary": "Al-Muwaṭṭaʼ (Arabic: الموطأ, 'The Well-Trodden Path' or 'The Established Path') is the foundational legal and hadith compilation of Malik ibn Anas (c. 711–795 CE) — the founder of the Maliki school of Sunni Islamic jurisprudence and the Imam of Medina, the city of the Prophet. Compiled in Medina over a period of approximately 40 years and completed c. 795 CE, the Muwaṭṭaʼ is the oldest surviving complete compilation of Islamic legal traditions and one of the most authoritative sources of Islamic law — predating al-Bukhari's Sahih (c. 870 CE) by three-quarters of a century and representing a crucial stage in the development of the Islamic legal tradition when the oral transmission of Prophetic practice was being systematically recorded. It arranges Islamic legal norms by subject matter (prayer, fasting, marriage, commercial transactions, inheritance, criminal law) and supports each ruling with Hadith (reports of the Prophet's sayings and actions) and the practice of the Companions and the people of Medina (the 'Medinan consensus' that is a distinctive feature of Maliki jurisprudence).\n\nMalik ibn Anas occupied a unique position in Islamic scholarship — as the leading scholar of Medina, the city of the Prophet and the Companions, he was the authoritative transmitter of what the Prophet's own community had actually practised, and the Muwaṭṭaʼ reflects his conviction that the living practice of Medina was a more reliable guide to the Sunnah than the individual Hadith circulating throughout the empire. The 'Medinan consensus' (ijma' ahl al-Madina) as a source of legal authority is the distinctive feature that separates the Maliki school from the other three Sunni law schools (Hanafi, Shafi'i, Hanbali), which rely primarily on individual Hadith.\n\nThe Muwaṭṭaʼ's historical significance extends beyond its legal content — it is a primary source for the practice of the early Muslim community of Medina in the 7th–8th centuries, preserving reports of Companions and Successors that are irreplaceable for the historical understanding of early Islam. The Maliki school it founded became dominant in North and West Africa, and the Muwaṭṭaʼ remains the foundational text of Maliki jurisprudence, studied in Islamic institutions across the Maghreb, Sahel, and sub-Saharan Africa to the present day.",
    "causes": [
      "The rapid geographic and demographic expansion of the Islamic world in the 7th–8th centuries — from Arabia to Spain, Central Asia, and India — created an urgent need for systematic legal guidance that could be applied across the empire's diverse regional customs, driving the project of Hadith collection and legal codification that the Muwaṭṭaʼ represents.",
      "Malik's conviction that the living practice of the Prophet's own city of Medina — preserved in the continuous tradition of the community that had lived alongside the Prophet and Companions — was the most reliable guide to authentic Islamic practice, which gave the Muwaṭṭaʼ its distinctive Medinan consensus principle and its particular authority.",
      "The Abbasid caliphate's patronage of Islamic scholarship — the Caliph Harun al-Rashid reportedly asked Malik to compile the Muwaṭṭaʼ as a universal legal code for the empire — provided institutional support for Malik's project, though the various regional law schools that developed meant the empire never adopted a single legal code."
    ],
    "effects": [
      "The Muwaṭṭaʼ founded the Maliki school of Islamic jurisprudence — one of the four major Sunni law schools — which became dominant in North Africa, West Africa, the Sahel, and parts of Arabia and Spain, making it the legal framework for Muslim communities across a vast geographic area.",
      "Malik's systematisation of Islamic legal norms by subject matter — combined with supporting Hadith and Medinan practice — established the methodological model for subsequent Islamic legal compilations, influencing the organisation and method of al-Shafi'i's Risala (the founding text of Islamic legal theory) and the other major Hadith collections.",
      "The Muwaṭṭaʼ's preservation of Hadith and reports from Companions and Successors in Medina makes it an irreplaceable primary source for the history of early Islam — its collection of traditions predating al-Bukhari by nearly a century is of unique historical and religious value for Islamic scholarship."
    ],
    "relationships": [
      {"sourceSlug": "malik-ibn-anas", "sourceName": "Malik ibn Anas (c. 711–795 CE)", "verb": "AUTHORS", "targetSlug": "al-muwaa", "targetName": "Al-Muwaṭṭaʼ (c. 795 CE)", "context": "Malik compiled the Muwaṭṭaʼ over approximately 40 years in Medina — the oldest surviving complete Islamic legal compilation and the foundational text of the Maliki school."},
      {"sourceSlug": "al-muwaa", "sourceName": "Al-Muwaṭṭaʼ", "verb": "FOUNDS", "targetSlug": "maliki-school", "targetName": "Maliki school of Islamic jurisprudence", "context": "The Muwaṭṭaʼ is the foundational text of the Maliki school — one of the four major Sunni law schools, dominant in North and West Africa."},
      {"sourceSlug": "al-muwaa", "sourceName": "Al-Muwaṭṭaʼ", "verb": "PREDATES", "targetSlug": "al-kutub-al-sittah", "targetName": "Al-Kutub al-Sittah (the Six Books of Hadith)", "context": "The Muwaṭṭaʼ (c. 795 CE) predates al-Bukhari's Sahih (c. 870 CE) and the other Five Books by three-quarters of a century — an earlier systematic record of Islamic legal traditions that influenced all subsequent Hadith compilation."}
    ],
    "places": [
      {"name": "Medina, Arabia (c. 750–795 CE, compilation)", "role": "The city of composition and the source of the Muwaṭṭaʼ's distinctive authority — Medina as the city of the Prophet and the Companions, whose living practice Malik regarded as the most reliable guide to authentic Islam"},
      {"name": "North Africa, West Africa, Spain (Maliki school dominance)", "role": "The geographic sphere of the Maliki school's dominance — from the Maghreb to the Sahel and sub-Saharan Africa, where the Muwaṭṭaʼ remains the foundational legal text"}
    ],
    "subjects": ["Islamic Law", "Classical Era", "Hadith", "Maliki School", "Islamic Scholarship", "Early Islam", "North Africa", "Religious Texts"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "Al-Muwaṭṭaʼ (Malik ibn Anas, c. 795 CE) is the oldest surviving complete compilation of Islamic legal traditions — predating al-Bukhari by nearly a century — and the foundational text of the Maliki school of Islamic jurisprudence, dominant in North and West Africa. Its distinctive principle of Medinan consensus and its systematic arrangement of legal norms by subject matter established the methodological model for subsequent Islamic legal scholarship.",
      "significanceCategory": "highly-significant"
    }
  }
},

"de-administrando-imperio": {
  "filepath": "data/appwrite-export/entities/780-Class-780/780de-administrando-imperio.json",
  "slug": "de-administrando-imperio",
  "data": {
    "summary": "De Administrando Imperio ('On the Governance of the Empire') is the confidential political manual written by the Byzantine Emperor Constantine VII Porphyrogennetos (r. 913–959 CE) for his son and heir Romanos II — a remarkable compilation of political intelligence, diplomatic guidance, historical ethnography, and administrative advice covering the empire's relations with its neighbours (the Bulgars, Rus', Khazars, Pechenegs, Franks, Arabs, and others), the origin legends and customs of the peoples bordering the empire, and the principles of Byzantine diplomacy and statecraft. Written c. 948–952 CE in accessible (non-classical) Greek, it was intended as a private imperial handbook rather than a public literary work, and its candid assessment of political realities, its detailed ethnographic descriptions of peoples beyond the empire's borders, and its frank discussion of diplomatic tactics make it one of the most extraordinary primary sources for 10th-century European and Central Asian history.\n\nConstantine VII was the most scholarly of Byzantine emperors — a major patron of literary and intellectual culture who compiled the Basilika (law codes), the De Ceremoniis (a detailed description of Byzantine court ceremonies), the De Thematibus (on the provinces), and the De Administrando Imperio as part of a systematic programme of encyclopaedic knowledge compilation. The DAI is a composite work drawing on earlier sources (now lost) and contemporary reports from ambassadors and travellers, and its unique value lies in its preservation of material available nowhere else: the origin legend of the Rus', the customs of the Khazars, the geography of the Danubian region, the history of Byzantine-Arab relations, and the arguments to be deployed in diplomatic negotiations with various peoples.\n\nFor historians of early medieval Europe, the Byzantine Empire, and Central Asia, De Administrando Imperio is an irreplaceable primary source — the only extended Byzantine account of the peoples of Eastern Europe (the Rus', the Bulgars, the Pechenegs, the Hungarians) at the critical period of their formation, and a unique window into Byzantine imperial thinking about geopolitics, diplomacy, and the management of peripheral peoples.",
    "causes": [
      "Constantine VII's encyclopaedic intellectual project — his systematic programme of compiling and preserving the administrative, ceremonial, geographical, and historical knowledge that an emperor needed — gave De Administrando Imperio its context as one of several imperial compendia designed to transmit practical imperial knowledge to the next generation.",
      "The complexity of Byzantine diplomacy in the 10th century — managing simultaneous relations with the Bulgars (periodic wars and peace negotiations), the Rus' (trading relations and the threat of their raids), the Khazars (declining from ally to nuisance), the Arabs (perpetual warfare on the eastern frontier), and the Frankish and Papal powers of the West — required a systematic handbook of the kind the DAI provides.",
      "The Byzantine practice of employing foreign peoples as foederati and diplomatic pawns — playing neighbours against each other, using honorary titles and gifts, deploying agents and missionaries — created a sophisticated system of 'soft power' management whose principles the DAI codifies for Constantine's heir."
    ],
    "effects": [
      "De Administrando Imperio is the primary Byzantine source for the history of the peoples of Eastern Europe in the 10th century — the Rus' (the Varangian traders-warriors who founded the Kievan Rus' state), the Bulgars, the Khazars, the Pechenegs, and the Hungarians — making it an irreplaceable primary source for the formative period of medieval Eastern European history.",
      "The DAI's detailed account of Byzantine diplomatic strategy — the system of honorary titles, gifts, missionary activity, and the manipulation of peripheral peoples against each other — illuminates the mechanisms by which the Byzantine Empire maintained its position as the dominant power in Eastern Europe and the Middle East despite its military limitations, providing one of the most sophisticated accounts of medieval 'soft power'.",
      "De Administrando Imperio's ethnographic material — its descriptions of the customs, origin legends, and settlements of the Rus', Khazars, Pechenegs, and others — is sometimes the only surviving primary source for these peoples in this period, making it indispensable for archaeologists, historians, and linguists working on the early history of Eastern Europe."
    ],
    "relationships": [
      {"sourceSlug": "constantine-vii-porphyrogennetos", "sourceName": "Constantine VII Porphyrogennetos (r. 913–959 CE)", "verb": "AUTHORS", "targetSlug": "de-administrando-imperio", "targetName": "De Administrando Imperio (c. 948–952 CE)", "context": "Constantine VII wrote the DAI as a confidential political handbook for his son Romanos II — one of several encyclopaedic compendia in his systematic programme of preserving imperial knowledge."},
      {"sourceSlug": "de-administrando-imperio", "sourceName": "De Administrando Imperio", "verb": "DOCUMENTS", "targetSlug": "kievan-rus", "targetName": "Kievan Rus' (early history, Varangian trade routes)", "context": "The DAI is a primary source for the early history of the Rus' — the Varangian traders-warriors who founded the Kievan Rus' state — providing the Byzantine perspective on the Dnieper trade route and the Rus' raids."},
      {"sourceSlug": "de-administrando-imperio", "sourceName": "De Administrando Imperio", "verb": "DESCRIBES", "targetSlug": "byzantine-empire", "targetName": "Byzantine diplomatic system (10th century)", "context": "The DAI codifies Byzantine imperial diplomacy — the system of honorary titles, marriages, gifts, and the manipulation of peripheral peoples that maintained Byzantine hegemony across Eastern Europe and the Middle East."}
    ],
    "places": [
      {"name": "Constantinople, Byzantine Empire (c. 948–952 CE)", "role": "The place of composition — the Byzantine imperial palace, where Constantine VII compiled the DAI as a confidential political handbook for his son"},
      {"name": "Eastern Europe, Central Asia, and Middle East (geographic scope)", "role": "The geographic scope of the DAI's diplomatic intelligence — covering the Rus', Bulgars, Pechenegs, Khazars, Arabs, Franks, and others in the Byzantine Empire's geopolitical sphere"}
    ],
    "subjects": ["Byzantine History", "Medieval History", "Medieval Era", "Political Theory", "Diplomacy", "Eastern Europe", "Byzantine Empire", "Historiography"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "WORLD_SYSTEMS"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "De Administrando Imperio (Constantine VII Porphyrogennetos, c. 948–952 CE) is a unique Byzantine imperial political handbook — its candid ethnographic descriptions of the Rus', Bulgars, Khazars, and Pechenegs make it the primary source for the formative period of Eastern European medieval history, and its codification of Byzantine diplomatic strategy is one of the most sophisticated accounts of medieval imperial 'soft power' management.",
      "significanceCategory": "significant"
    }
  }
},

"akbarnama": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781akbarnama.json",
  "slug": "akbarnama",
  "data": {
    "summary": "The Akbarnama ('Book of Akbar') is the official biography and history of the Mughal Emperor Akbar the Great (r. 1556–1605), written by Abu'l-Fazl ibn Mubarak (1551–1602) — Akbar's court historian, adviser, and intimate friend — on Akbar's own commission. Written in ornate Persian prose with elaborate imagery and symbolism between c. 1590–1596 CE, it comprises three volumes: the first covering the genealogy of Timur's line and the reigns of Babur and Humayun (drawing on earlier sources); the second and third covering Akbar's own reign in extraordinary detail, year by year; and the Ain-i-Akbari (Acts of Akbar) — a statistical and administrative survey of the Mughal Empire that provides an unparalleled picture of Mughal government, economy, culture, and society. The Akbarnama is the most comprehensive and detailed source for Mughal history under Akbar and one of the greatest works of Islamic historical literature.\n\nAbul Fazl wrote the Akbarnama not merely as a political chronicle but as a theological and philosophical statement — Akbar is portrayed as a semi-divine world ruler (Padshah) whose justice illuminates the universe, in a deliberate appropriation of Persian imperial and Sufi mystical imagery that was part of Akbar's project of constructing a universal imperial ideology (Din-i-Ilahi) transcending the sectarian divisions of the empire's diverse subjects. The Ain-i-Akbari (the third volume), which surveys the provinces, revenues, agricultural practices, weights and measures, military organisation, artisanal production, and religious and intellectual life of the empire, is a unique statistical and administrative record of extraordinary value for historians of Mughal India.\n\nThe Akbarnama was richly illustrated — the Mughal imperial workshops produced multiple illustrated manuscripts, and the surviving illustrated copies (particularly the Akbarnama in the Victoria and Albert Museum, London, c. 1590–1598) are among the greatest works of Mughal painting, depicting battle scenes, court ceremonies, and episodes from Akbar's life in a distinctive style combining Persian, Indian, and European artistic elements. The Akbarnama is thus simultaneously a literary, historical, administrative, and artistic monument of Mughal civilisation.",
    "causes": [
      "Akbar's political project of constructing a universal Mughal imperial ideology — transcending the religious divisions between his Hindu, Muslim, Jain, and Zoroastrian subjects — required a historical and biographical narrative that presented Akbar's rule as divinely legitimated and universally beneficial, which the Akbarnama's theological and philosophical framing provided.",
      "The Mughal literary tradition of royal biography (padshahname, literally 'King's Book') — drawn from the Persian imperial literary tradition that went back through the Timurids to the great Persian epics — gave Abul Fazl his literary model and his audience: Persian was the prestige literary language of the Mughal court and of the educated elite across the Islamic world.",
      "Abul Fazl's own intellectual framework — his Sufi background, his neo-Platonic cosmology, his conviction that Akbar embodied a synthesis of the 'perfect man' concept from Islamic mysticism — gave the Akbarnama its theological depth and its portrait of Akbar as a semi-divine world ruler whose justice reflected divine illumination."
    ],
    "effects": [
      "The Akbarnama (and particularly the Ain-i-Akbari) is the primary source for the administrative, economic, and cultural history of Mughal India under Akbar — its detailed surveys of provincial revenues, land measurement, agricultural production, and population provide the empirical foundation for all modern historical analysis of the Mughal economy.",
      "The Ain-i-Akbari's account of the Mughal Empire's internal organisation — its administrative provinces, revenue system (the zabti system of land revenue assessment), military organisation, and the intellectual and cultural life of the court — is an irreplaceable document for the political history of 16th-century India and for the comparative history of early modern empires.",
      "The illustrated Akbarnama manuscripts are among the greatest achievements of Mughal painting — a synthesis of Persian, Indian, and European artistic influences commissioned by one of history's greatest art patrons, representing a distinctive moment in world art history in which three great artistic traditions merged in the context of Mughal imperial patronage."
    ],
    "relationships": [
      {"sourceSlug": "abul-fazl", "sourceName": "Abu'l-Fazl ibn Mubarak (1551–1602)", "verb": "AUTHORS", "targetSlug": "akbarnama", "targetName": "Akbarnama (c. 1590–1596 CE)", "context": "Abul Fazl wrote the Akbarnama on Akbar's commission — a comprehensive biography and history presenting Akbar as a universal, semi-divine world ruler."},
      {"sourceSlug": "akbar-the-great", "sourceName": "Akbar the Great (r. 1556–1605)", "verb": "SUBJECT_AND_PATRON_OF", "targetSlug": "akbarnama", "targetName": "Akbarnama", "context": "Akbar both commissioned and is the subject of the Akbarnama — the work's theological portrayal of Akbar as a divinely illuminated world ruler was part of his broader project of constructing a universal Mughal imperial ideology."},
      {"sourceSlug": "akbarnama", "sourceName": "Akbarnama", "verb": "INCLUDES", "targetSlug": "ain-i-akbari", "targetName": "Ain-i-Akbari (Acts of Akbar)", "context": "The Ain-i-Akbari — the third volume of the Akbarnama — is a statistical survey of the Mughal Empire that provides an unparalleled record of Mughal governance, economy, and society."}
    ],
    "places": [
      {"name": "Mughal Empire (Agra/Fatehpur Sikri, c. 1590–1596 CE)", "role": "The context of composition — the Mughal imperial court under Akbar, whose itinerant court moved between Agra, Fatehpur Sikri, and other capitals"},
      {"name": "India, Pakistan, Afghanistan (Mughal Empire, 1556–1605)", "role": "The geographic scope of Akbar's empire — the Akbarnama's historical and administrative record covers the entire Mughal domain from Kabul to Bengal"}
    ],
    "subjects": ["Mughal History", "Early Modern Era", "India", "Islamic Literature", "Biography", "Persian Literature", "Mughal Art", "Imperial History"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "RELIGIOUS_INTERPRETATION"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "The Akbarnama (Abul Fazl, c. 1590–1596 CE) is the primary source for the history of the Mughal Empire under Akbar — its comprehensive biographical narrative, its administrative survey (the Ain-i-Akbari), and its magnificent illustrated manuscripts make it simultaneously the major literary, historical, and artistic monument of Mughal civilisation. The Ain-i-Akbari's unique statistical record of the empire's economy and administration is indispensable for modern historians of Mughal India.",
      "significanceCategory": "highly-significant"
    }
  }
},

"a-brief-history-of-time": {
  "filepath": "data/appwrite-export/entities/781-Class-781/781a-brief-history-of-time.json",
  "slug": "a-brief-history-of-time",
  "data": {
    "summary": "A Brief History of Time: From the Big Bang to Black Holes is the popular science book by the theoretical physicist Stephen Hawking (1942–2018), published by Bantam Books on 1 April 1988. One of the most successful popular science books ever published — selling over 25 million copies, translated into more than 40 languages, and spending 237 weeks on the Sunday Times bestseller list (a record) — it brought the concepts of modern cosmology (the Big Bang, black holes, spacetime, quantum gravity, the arrow of time, the possibility of a complete unified theory of physics) to a global popular audience with clarity, wit, and accessible prose that made it the defining popular science text of the late 20th century. Hawking's personal story — writing and speaking from a wheelchair, dictating through a computer due to motor neurone disease — gave the book an additional moral and intellectual resonance that contributed to its enormous cultural impact.\n\nA Brief History of Time covers the development of scientific understanding of the universe from Aristotle and Ptolemy through Newton, Einstein, and the development of quantum mechanics, to the contemporary challenges of cosmology and particle physics. Its central themes include: the Big Bang as the origin of spacetime itself (not an explosion within pre-existing space, but the beginning of space and time); black holes as regions where spacetime curvature becomes infinite (and Hawking's own major contribution — that black holes emit thermal radiation through quantum effects, 'Hawking radiation'); the arrow of time and why time seems to flow only in one direction; and the 'grand unified theory' that might combine quantum mechanics and general relativity. Hawking's famous closing question — 'Why does the universe go to all the trouble of existing?' — gestures toward the philosophical and theological implications of a complete physical theory.\n\nThe book's cultural significance extends far beyond its scientific content — it established popular science writing as a major publishing genre, inspired a generation of scientists and science communicators, and made Hawking into one of the most recognisable intellectual figures of the 20th century, a symbol of the power of pure thought to transcend physical limitation.",
    "causes": [
      "The revolution in theoretical cosmology in the 1960s–1980s — Hawking and Penrose's singularity theorems, the development of inflationary cosmology, the discovery of cosmic microwave background radiation, and Hawking's own 1974 discovery of black hole radiation — created a wealth of new cosmological results that had never been presented to a popular audience.",
      "Hawking's progressive motor neurone disease — which had confined him to a wheelchair since the early 1970s and eventually left him unable to speak except through a speech synthesiser — gave him the time and the motivation to write for a popular audience, and his extraordinary intellectual productivity despite his disability created the compelling personal narrative that the book became.",
      "The publishing landscape of the 1980s — the growth of popular science writing as a genre (Carl Sagan's Cosmos, 1980; James Gleick's Chaos, 1987) — created the readership and the publishing infrastructure within which A Brief History of Time could reach a mass audience."
    ],
    "effects": [
      "A Brief History of Time transformed popular science publishing — its extraordinary commercial success (25 million copies) demonstrated that a serious treatment of cutting-edge physics could reach a global mass audience, inspiring a generation of popular science writers (Brian Greene, Michio Kaku, Neil deGrasse Tyson) and establishing popular science as a major publishing genre.",
      "The book made Stephen Hawking into the world's most famous scientist since Einstein — a cultural icon whose combination of extraordinary intellectual achievement and personal courage became one of the defining images of late 20th-century intellectual life, inspiring millions of people with disabilities and contributing to public understanding of the importance of theoretical physics.",
      "A Brief History of Time's contribution to public understanding of the Big Bang, black holes, and quantum gravity — combined with its closing philosophical questions about the nature of time, the origin of the universe, and the possibility of a 'theory of everything' — shaped a generation's scientific imagination and contributed to the cultural authority of cosmological science in the late 20th and early 21st centuries."
    ],
    "relationships": [
      {"sourceSlug": "stephen-hawking", "sourceName": "Stephen Hawking (1942–2018)", "verb": "AUTHORS", "targetSlug": "a-brief-history-of-time", "targetName": "A Brief History of Time (1988)", "context": "Hawking wrote A Brief History of Time to explain modern cosmology to a popular audience — a project shaped by his extraordinary intellectual productivity alongside his progressive motor neurone disease."},
      {"sourceSlug": "a-brief-history-of-time", "sourceName": "A Brief History of Time", "verb": "POPULARISES", "targetSlug": "black-holes", "targetName": "Black holes and Hawking radiation", "context": "A Brief History of Time brought Hawking's own major scientific contribution — the theoretical discovery that black holes emit thermal radiation (Hawking radiation, 1974) — to a global popular audience."},
      {"sourceSlug": "a-brief-history-of-time", "sourceName": "A Brief History of Time", "verb": "INFLUENCES", "targetSlug": "popular-science-genre", "targetName": "Popular science publishing (1990s–2020s)", "context": "A Brief History of Time's extraordinary commercial success established popular science as a major publishing genre — inspiring a generation of science communicators and demonstrating that serious physics could reach a mass audience."}
    ],
    "places": [
      {"name": "Cambridge, England (1988, publication)", "role": "The academic home of Hawking — Cambridge University, where he held the Lucasian Chair of Mathematics (Newton's chair) from 1979–2009, and where A Brief History of Time was written"},
      {"name": "Global (25 million copies, 40+ languages)", "role": "The worldwide reach of A Brief History of Time — one of the most widely read popular science books in history, translated into over 40 languages and read by a global audience"}
    ],
    "subjects": ["Physics", "Modern Era", "Cosmology", "Popular Science", "20th Century", "Astrophysics", "Black Holes", "Stephen Hawking"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 8,
      "significanceNarrative": "A Brief History of Time (Hawking, 1988) transformed popular science publishing — its 25 million copies and 237-week Sunday Times bestseller record demonstrated that cutting-edge theoretical physics could reach a global mass audience, establishing popular science as a major genre and making Hawking the world's most famous scientist since Einstein. Its contribution to public understanding of the Big Bang, black holes, and quantum gravity shaped a generation's scientific imagination.",
      "significanceCategory": "highly-significant"
    }
  }
},

"digenes-akritas": {
  "filepath": "data/appwrite-export/entities/782-Class-782/782digenes-akritas.json",
  "slug": "digenes-akritas",
  "data": {
    "summary": "Digenes Akritas (Greek: Διγενής Ἀκρίτης, 'Double-born Borderer') is the Byzantine Greek epic poem — surviving in multiple manuscript versions of varying length and date (the earliest complete versions c. 11th–12th century CE, with core material possibly going back to the 9th–10th century) — that narrates the legendary exploits of a border hero of mixed Christian-Greek and Arab-Muslim parentage on the eastern frontier of the Byzantine Empire. The poem's hero, Basil Digenes Akritas, is born of a Byzantine aristocratic mother and an Arab emir who converted to Christianity; he grows up to be the greatest of the akritai (border warriors) defending the Byzantine-Arab frontier, famous for his superhuman strength, his beauty, his love story with Eudokia (whom he abducts in traditional epic fashion), his battles with monsters and brigands, and his death in his magnificent palace on the Euphrates. The poem preserves folk traditions of the Byzantine frontier culture and is the primary monument of medieval Greek oral-derived epic.\n\nDigenes Akritas is significant both as a literary monument and as a historical source — it preserves traditions of the Byzantine-Arab frontier world of the 9th–10th centuries (the period of Byzantine reconquest of Cilicia, Anatolia, and Syria under the Macedonian emperors), and its hero's dual identity as both Greek-Christian and Arab-Islamic reflects the cultural contact zone of the Anatolian frontier. The poem belongs to a tradition of akritika (border songs) that circulated orally in the frontier regions and were eventually recorded in multiple manuscript versions that show considerable variation — making Digenes Akritas a fascinating example of medieval oral-formulaic poetry preserved in literate form.\n\nThe poem's afterlife is remarkable — the Digenes tradition spread from Byzantium to Cyprus, to the Slavic world (a Slavic version exists), and to the Greek oral tradition where akritic songs continued to be sung into the 19th century. Its hero became one of the defining figures of the Greek literary imagination, and the poem's themes of heroic border warfare, conversion, love, and the hero's solitary death influenced the 19th-century Greek national imagination and the neo-Hellenic literary tradition.",
    "causes": [
      "The Byzantine-Arab frontier warfare of the 9th–10th centuries — the period of Byzantine reconquest of Cilicia, Northern Syria, and parts of Anatolia under Nikephoros Phokas, John Tzimiskes, and Basil II — created the historical context of border heroism that the Digenes poem reflects and celebrates.",
      "The cultural contact zone of the Byzantine-Arab frontier — where Greek Christians and Arab Muslims lived, fought, traded, and intermarried across the Taurus and Euphrates frontier — produced the distinctive cultural hybrid of the akritai (border warriors) and the poem's hero's dual identity as both Greek-Christian and Arab-Muslim by birth.",
      "The oral tradition of akritika (border songs) — folk poetry celebrating the exploits of frontier warriors against Arab raiders, bandits, and supernatural opponents — provided the oral-formulaic material from which the learned written versions of the Digenes poem were compiled, representing the transition from oral to literate epic tradition characteristic of many medieval epics."
    ],
    "effects": [
      "Digenes Akritas is the primary monument of medieval Greek heroic poetry — the Byzantine equivalent of the Iliad or the Chanson de Roland — and its preservation in multiple manuscript versions provides scholars with a unique case study in the transmission and transformation of oral heroic poetry into written form.",
      "The Digenes tradition spread throughout the Eastern Mediterranean and the Slavic world — influencing Byzantine, Cypriot, and eventually neo-Hellenic oral and literary traditions — and the akritic folk songs that descended from it were recorded by Greek folklorists in the 19th century as part of the construction of modern Greek national cultural identity.",
      "The poem's portrait of frontier warfare and cultural mixing on the Byzantine-Arab border provides historians with rare glimpses of the social world of the Byzantine-Arab frontier — the practices, values, and cultural negotiations of a contact zone that standard Byzantine court history tends to obscure."
    ],
    "relationships": [
      {"sourceSlug": "digenes-akritas", "sourceName": "Digenes Akritas (c. 9th–12th century CE)", "verb": "BELONGS_TO", "targetSlug": "byzantine-literature", "targetName": "Byzantine Greek literary tradition", "context": "Digenes Akritas is the primary monument of Byzantine heroic epic — a work at the junction of oral folk tradition and learned literary compilation, the Byzantine equivalent of the Western European chansons de geste."},
      {"sourceSlug": "digenes-akritas", "sourceName": "Digenes Akritas", "verb": "REFLECTS", "targetSlug": "byzantine-arab-wars", "targetName": "Byzantine-Arab frontier (9th–10th century CE)", "context": "The poem's historical background is the Byzantine-Arab frontier warfare of the 9th–10th centuries — the period of the Byzantine reconquest of Anatolia and Syria that produced the akritai (border warrior) tradition."},
      {"sourceSlug": "digenes-akritas", "sourceName": "Digenes Akritas", "verb": "INFLUENCES", "targetSlug": "greek-national-poetry", "targetName": "Modern Greek national literature (akritic folk songs)", "context": "The akritic folk song tradition descended from Digenes Akritas was recorded by 19th-century Greek folklorists and became part of the construction of modern Greek national cultural identity."}
    ],
    "places": [
      {"name": "Byzantine-Arab frontier, Anatolia and Cappadocia (9th–10th century CE, historical setting)", "role": "The frontier world the poem reflects — the contact zone between Byzantine and Arab civilisations in eastern Anatolia, where the akritai (border warriors) guarded the imperial frontier"},
      {"name": "Byzantine Empire and Eastern Mediterranean (manuscript tradition, 11th–14th century)", "role": "The geographic spread of the Digenes manuscript tradition — from Constantinople and the Aegean to Cyprus and the Slavic world"}
    ],
    "subjects": ["Byzantine Literature", "Medieval Literature", "Medieval Era", "Byzantine Empire", "Epic Poetry", "Greek Literature", "Byzantine-Arab Wars", "Frontier Culture"],
    "frameworks": ["STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "Digenes Akritas (c. 9th–12th century CE) is the primary monument of Byzantine heroic epic — a work at the junction of oral folk tradition and learned literary compilation that preserves traditions of the Byzantine-Arab frontier and the cultural hybrid of the akritai (border warriors). The akritic folk song tradition descended from it was recorded in the 19th century and became part of modern Greek national cultural identity.",
      "significanceCategory": "significant"
    }
  }
},

"dialogue-concerning-heresies-1529": {
  "filepath": "data/appwrite-export/entities/785-Class-785/785dialogue-concerning-heresies-1529.json",
  "slug": "dialogue-concerning-heresies-1529",
  "data": {
    "summary": "A Dialogue of Comfort Against Tribulation is a devotional work written by Sir Thomas More (1478–1535) in the Tower of London in 1534–1535 — during his imprisonment by Henry VIII for refusing to take the Oath of Supremacy recognising the king as head of the Church of England — and published posthumously in 1553. However, the entity listed here, 'Dialogue Concerning Heresies' (1529), refers to More's earlier polemical work — A Dialogue Concerning Heresies and Matters of Religion (1529) — one of the most important English-language responses to the Protestant Reformation and to William Tyndale's English New Testament (1526).\n\nThe Dialogue Concerning Heresies (1529) is written as a conversation between Thomas More and 'a Messenger' (a young man sympathetic to Lutheranism), in which More defends the authority of the Catholic Church and its traditions against the Protestant arguments for Scripture alone (sola scriptura) and attacks the heresies of Luther, Tyndale, and the English reformers. It was the first major English prose work of religious controversy — one of the earliest substantial prose debates of the Reformation in English — and its defence of the authority of the Church's unwritten tradition against the Protestant appeal to Scripture alone articulates the central Catholic position in the Reformation controversy with unusual clarity and vigour. More was at this time Henry VIII's Lord Chancellor and the most powerful layman in England, and his willingness to use his pen in defence of the old faith gave the Dialogue exceptional political and cultural weight.\n\nThe Dialogue is also significant for its discussion of the English Bible question — More's opposition to Tyndale's English New Testament, which he argues is dangerously mistranslated to promote heresy, is a central concern of the later books. This controversy was itself historically pivotal: the debate over the vernacular Bible was one of the defining issues of the English Reformation, and More's position (that vernacular scripture could lead to heresy without proper ecclesiastical guidance) was overtaken by events within a decade when Henry VIII authorised the Great Bible (1539).",
    "causes": [
      "The rapid spread of Lutheran ideas and Tyndale's English New Testament in England in the 1520s — circulated in contraband copies and preached by Cambridge scholars influenced by the Continental Reformation — created the immediate Protestant challenge to which the Dialogue Concerning Heresies was More's response as Lord Chancellor and the lay champion of orthodox Catholicism.",
      "Henry VIII's own orthodox Catholicism (he had received the title 'Defender of the Faith' from Pope Leo X in 1521 for his anti-Luther Assertio Septem Sacramentorum) and his use of Thomas More as Lord Chancellor to suppress Protestant heresy — creating the political and institutional context within which More's polemical works had state authority behind them.",
      "The English Reformation controversy's specific focus on vernacular scripture — Tyndale's 1526 New Testament's strategic translation choices (using 'congregation' for 'church', 'senior' for 'priest', 'love' for 'charity') that shifted the theological valence of key terms — gave More's Dialogue its central polemical target and its significance for the English Bible question."
    ],
    "effects": [
      "The Dialogue Concerning Heresies was the opening shot in the English Reformation's pamphlet war — the series of polemical exchanges between More and Tyndale (answered by Tyndale's Answer to More, 1531) that defined the terms of the English Reformation controversy and established Protestant and Catholic positions in English prose.",
      "More's arguments for the authority of unwritten Church tradition against sola scriptura — and his attack on Tyndale's translation — were rendered historically moot by the English Reformation's progress under Henry VIII (the Break with Rome, 1534; the Royal Injunctions of 1538 requiring English Bibles in churches), making the Dialogue a record of the Catholic position that was overwhelmed by events.",
      "The Dialogue Concerning Heresies is a significant monument in the history of English prose — as one of the first extended works of English-language theological controversy, it contributed to the development of the English argumentative prose style that would be refined by Tyndale himself, Cranmer, and the Elizabethan controversialists."
    ],
    "relationships": [
      {"sourceSlug": "thomas-more", "sourceName": "Thomas More (1478–1535)", "verb": "AUTHORS", "targetSlug": "dialogue-concerning-heresies-1529", "targetName": "A Dialogue Concerning Heresies (1529)", "context": "More wrote the Dialogue Concerning Heresies as Lord Chancellor — his first major English-language defence of Catholic orthodoxy against the Protestant Reformation and Tyndale's English New Testament."},
      {"sourceSlug": "dialogue-concerning-heresies-1529", "sourceName": "Dialogue Concerning Heresies", "verb": "RESPONDS_TO", "targetSlug": "william-tyndale", "targetName": "William Tyndale (English New Testament, 1526)", "context": "Tyndale's 1526 English New Testament — and its strategic translation choices promoting Protestant theology — was the primary target of More's Dialogue, which attacked both the translation's accuracy and the Protestant principle of sola scriptura."},
      {"sourceSlug": "dialogue-concerning-heresies-1529", "sourceName": "Dialogue Concerning Heresies", "verb": "CONTEXTUALISED_BY", "targetSlug": "english-reformation", "targetName": "English Reformation (1520s–1550s)", "context": "The Dialogue was written at the opening of the English Reformation — More as Lord Chancellor defending Catholic orthodoxy against the incoming Protestant tide — and its positions were rendered politically moot by Henry VIII's Break with Rome five years later."}
    ],
    "places": [
      {"name": "London, England (1529, composition and publication)", "role": "The context of composition — Thomas More as Lord Chancellor in London, defending Catholic orthodoxy at the moment of the English Reformation's first impact"},
      {"name": "England (English Reformation context, 1520s–1550s)", "role": "The historical sphere of the Dialogue's significance — the first generation of the English Reformation, in which the controversy over vernacular scripture and Church authority shaped the trajectory of English religion"}
    ],
    "subjects": ["English Reformation", "Early Modern Era", "Catholic Church", "Thomas More", "Protestantism", "English Literature", "Religious Controversy", "16th Century"],
    "frameworks": ["RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"],
    "historicalSignificance": {
      "significanceScore": 7,
      "significanceNarrative": "A Dialogue Concerning Heresies (Thomas More, 1529) is the first major English-language response to the Protestant Reformation — a comprehensive Catholic defence of Church tradition against sola scriptura and Tyndale's English New Testament, written when More was at the peak of his political power as Lord Chancellor. It opened the English Reformation's pamphlet war with Tyndale and is a significant monument in the history of English argumentative prose.",
      "significanceCategory": "significant"
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
