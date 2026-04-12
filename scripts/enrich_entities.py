#!/usr/bin/env python3
"""One-time script to enrich historically important entities with rich summaries,
causes, effects, and properly-formatted relationships."""

import json
import os

def slug_to_name(slug):
    MAP = {
        "abraham": "Abraham", "aaron": "Aaron", "aaronic-priesthood": "Aaronic Priesthood",
        "ark-of-the-covenant": "Ark of the Covenant", "torah": "Torah",
        "ancient-israel": "Ancient Israel", "book-of-exodus": "Book of Exodus",
        "ancient-egypt": "Ancient Egypt", "ashoka": "Ashoka", "confucius": "Confucius",
        "laozi": "Laozi", "ancient-india": "Ancient India", "buddha": "Buddha",
        "confucianism": "Confucianism", "ancient-china": "Ancient China",
        "socrates": "Socrates", "moses": "Moses", "dhammapada": "Dhammapada",
        "jesus-christ": "Jesus Christ", "muhammad": "Muhammad",
        "julius-caesar": "Julius Caesar", "aristotle": "Aristotle",
        "plato": "Plato", "augustus": "Augustus", "cleopatra": "Cleopatra VII",
        "genghis-khan": "Genghis Khan", "martin-luther": "Martin Luther",
        "galileo-galilei": "Galileo Galilei", "albert-einstein": "Albert Einstein",
        "zoroaster": "Zoroaster", "charlemagne": "Charlemagne",
        "saladin": "Saladin", "nelson-mandela": "Nelson Mandela",
        "nikola-tesla": "Nikola Tesla", "winston-churchill": "Winston Churchill",
        "abraham-lincoln": "Abraham Lincoln", "george-washington": "George Washington",
        "homer": "Homer", "hannibal": "Hannibal Barca",
        "joan-of-arc": "Joan of Arc", "christopher-columbus": "Christopher Columbus",
        "mahatma-gandhi": "Mahatma Gandhi", "martin-luther-king-jr": "Martin Luther King Jr.",
        "paul-the-apostle": "Paul the Apostle", "cyrus-the-great": "Cyrus the Great",
        "david": "King David", "solomon": "King Solomon", "sun-tzu": "Sun Tzu",
        "roman-republic": "Roman Republic", "roman-empire": "Roman Empire",
        "roman-senate": "Roman Senate", "pompey": "Pompey",
        "cleopatra": "Cleopatra VII", "mark-antony": "Mark Antony",
        "alexander-the-great": "Alexander the Great", "persian-empire": "Persian Empire",
        "han-dynasty": "Han Dynasty", "mongol-empire": "Mongol Empire",
        "ottoman-empire": "Ottoman Empire", "holy-roman-empire": "Holy Roman Empire",
        "catholic-church": "Catholic Church", "papacy": "Papacy",
        "reformation": "Protestant Reformation", "isaac-newton": "Isaac Newton",
        "copernicus": "Nicolaus Copernicus", "renaissance": "Renaissance",
        "french-revolution": "French Revolution", "apartheid": "Apartheid",
        "american-revolution": "American Revolution",
        "united-states-constitution": "United States Constitution",
        "declaration-of-independence": "Declaration of Independence",
        "united-nations": "United Nations", "world-war-ii": "World War II",
        "world-war-i": "World War I", "battle-of-britain": "Battle of Britain",
        "d-day": "D-Day", "nazi-germany": "Nazi Germany",
        "american-civil-war": "American Civil War", "emancipation-proclamation": "Emancipation Proclamation",
        "general-relativity": "General Relativity", "special-relativity": "Special Relativity",
        "quantum-mechanics": "Quantum Mechanics", "alternating-current": "Alternating Current",
        "thomas-edison": "Thomas Edison", "indian-independence-movement": "Indian Independence Movement",
        "civil-rights-movement": "Civil Rights Movement",
        "mecca": "Mecca", "medina": "Medina", "quran": "Quran",
        "achaemenid-empire": "Achaemenid Empire", "babylon": "Babylon",
        "ancient-greece": "Ancient Greece", "athens": "Athens",
        "iliad": "Iliad", "odyssey": "Odyssey",
        "republic-plato": "Republic (Plato)", "the-art-of-war": "The Art of War",
    }
    if slug in MAP:
        return MAP[slug]
    return slug.replace("-", " ").title()


def rel(source_slug, source_name, verb, target_slug, context):
    return {
        "sourceSlug": source_slug,
        "sourceName": source_name,
        "verb": verb,
        "targetSlug": target_slug,
        "targetName": slug_to_name(target_slug),
        "context": context
    }


# ============================================================
# ENRICHMENT DATA
# ============================================================

ENRICHMENTS = {

"jesus-christ": {
    "summary": "Jesus of Nazareth (c. 4 BCE \u2013 c. 30 CE) is the central figure of Christianity, acknowledged by over 2.4 billion adherents as the Son of God, the Messiah (Christ) prophesied in the Hebrew scriptures, and the incarnation of the divine Logos. Born in Bethlehem during the reign of Herod the Great, raised in Nazareth as a carpenter\u2019s son, he emerged at age 30 with a public ministry of teaching, healing, and radical reinterpretation of Jewish Law that lasted approximately three years. His Sermon on the Mount articulated the Beatitudes, the Lord\u2019s Prayer, and the ethic of enemy-love that would reshape Western moral philosophy. He selected twelve apostles, performed miracles attested by multiple independent traditions (Mark, Q, John, Paul), and proclaimed the Kingdom of God \u2014 a present-and-coming divine reign accessible to the poor, the outcast, and the repentant. His triumphal entry into Jerusalem, cleansing of the Temple, and Last Supper with disciples precipitated his arrest by the Sanhedrin, trial before Pontius Pilate, and crucifixion on Golgotha (c. 30 CE). His followers proclaimed his bodily resurrection on the third day \u2014 the foundational claim of Christianity \u2014 and his post-resurrection appearances to over 500 witnesses (1 Corinthians 15:6) launched the explosive growth of the early Church. Within three centuries, the faith he founded transformed from a persecuted Jewish sect into the official religion of the Roman Empire under Constantine (313 CE). The calendar itself pivots on his birth (Anno Domini). His teachings on forgiveness, the dignity of every human soul, sacrificial love, and the separation of religious and political authority (Render unto Caesar) shaped Western civilization\u2019s concepts of human rights, charity, education, and law. Islam honors him as the prophet Isa; Judaism acknowledges his historical impact; and secular historians rank him among the most influential figures who ever lived.",
    "died": "c. 30 CE, Jerusalem",
    "period": "c. 4 BCE \u2013 c. 30 CE",
    "wikidataQid": "Q302",
    "wikipediaUrl": "https://en.wikipedia.org/wiki/Jesus",
    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Spas_vsederzhitel_sinay.jpg",
    "causes": [
        "The Abrahamic covenant and Messianic prophecies of the Hebrew Bible (Isaiah 53, Micah 5:2, Daniel 9) created centuries of expectation for a divine deliverer",
        "Roman occupation of Judea and the resulting political-spiritual crisis among 1st-century Jews seeking liberation",
        "The theological preparation of Second Temple Judaism: synagogue worship, Pharisaic ethics, and apocalyptic literature"
    ],
    "effects": [
        "Founded Christianity, which became the world\u2019s largest religion (2.4 billion adherents) and the dominant cultural force in Western civilization for two millennia",
        "The resurrection proclamation launched the apostolic mission that spread from Jerusalem to Rome within 30 years, creating the early Church",
        "Constantine\u2019s Edict of Milan (313 CE) and Theodosius\u2019s decree (380 CE) made Christianity the state religion of the Roman Empire",
        "Jesus\u2019s teachings on human dignity, forgiveness, and charity gave rise to hospitals, universities, and the Western concept of human rights",
        "The Anno Domini calendar system, based on his birth, became the global standard for dating history",
        "His sacrifice theology (atonement) became the central doctrine distinguishing Christianity from Judaism and Islam"
    ],
    "relationships": [
        rel("jesus-christ", "Jesus Christ", "FULFILLS", "abraham", "Jesus as the 'seed of Abraham' through whom all nations would be blessed (Galatians 3:16)"),
        rel("jesus-christ", "Jesus Christ", "FULFILLS", "moses", "Jesus as the 'prophet like Moses' (Deuteronomy 18:15) \u2014 new covenant fulfilling the old"),
        rel("jesus-christ", "Jesus Christ", "FULFILLS", "david", "Jesus as the 'Son of David,' heir to the Davidic covenant of eternal kingship (2 Samuel 7)"),
        rel("jesus-christ", "Jesus Christ", "COMMISSIONS", "paul-the-apostle", "The risen Christ commissioned Paul on the Damascus road (Acts 9), launching Gentile Christianity"),
        rel("jesus-christ", "Jesus Christ", "INFLUENCES", "constantine-i", "Constantine\u2019s conversion (312 CE) made Christianity the dominant force in Roman politics"),
        rel("jesus-christ", "Jesus Christ", "OCCURS_IN", "ancient-israel", "Born in Bethlehem, raised in Nazareth, crucified in Jerusalem \u2014 all within Roman Judea"),
        rel("jesus-christ", "Jesus Christ", "PREFIGURES", "muhammad", "Islam honors Jesus (Isa) as a virgin-born prophet and Messiah; the Quran mentions him 25 times"),
    ],
    "subjectHeadings": ["People \u2014 Religious Founders \u2014 Palestine \u2014 Classical"],
    "subjects": ["Christianity", "Messiah", "Resurrection", "Crucifixion", "Kingdom of God", "Sermon on the Mount", "Incarnation", "Atonement", "Ancient Israel", "Roman Empire"],
    "frameworks": ["DOCTRINE_DEVELOPMENT", "CULTURAL_DIFFUSION", "CAUSE_AND_EFFECT", "ETHICAL_FRAMEWORK", "RELIGIOUS_INSTITUTIONS"],
},

"muhammad": {
    "summary": "Muhammad ibn Abdullah (c. 570\u2013632 CE) was the founder of Islam, regarded by 1.9 billion Muslims as the final prophet (Seal of the Prophets) in the Abrahamic tradition. Born in Mecca to the Quraysh tribe, orphaned early, and raised by his grandfather and uncle, he became a merchant known for exceptional honesty (al-Amin, \u2018the Trustworthy\u2019). At age 40, during meditation in the Cave of Hira, he received the first Quranic revelation from the angel Jibril (Gabriel): \u2018Recite, in the name of your Lord who created\u2019 (Surah 96:1). For 23 years he received revelations that were compiled into the Quran, Islam\u2019s holy scripture \u2014 a masterwork of Arabic prose that codified theology, law, ethics, and governance. Persecuted in Mecca, he led the Hijra (emigration) to Medina in 622 CE \u2014 the event that begins the Islamic calendar. In Medina, he established the Constitution of Medina (the first multi-religious civic charter), unified warring Arab tribes, and built a community (ummah) governed by divine law (Sharia). After the decisive Battle of Badr (624 CE) and the bloodless Conquest of Mecca (630 CE), he united the Arabian Peninsula under Islam. His Farewell Sermon articulated universal human equality, women\u2019s rights, and the sanctity of life. Within a century of his death, the Rashidun and Umayyad caliphates had spread Islam from Spain to Central Asia \u2014 the fastest territorial expansion of any religion in history. Muhammad\u2019s legacy encompasses religion, law, governance, military strategy, diplomacy, and social reform; Michael Hart\u2019s controversial ranking placed him first among the most influential people in history.",
    "died": "632 CE, Medina",
    "period": "c. 570\u2013632 CE",
    "wikidataQid": "Q9458",
    "wikipediaUrl": "https://en.wikipedia.org/wiki/Muhammad",
    "imageUrl": "",
    "causes": [
        "Pre-Islamic Arabian polytheism and tribal warfare created spiritual and social conditions ripe for a unifying monotheistic message",
        "The Abrahamic prophetic tradition (Judaism and Christianity) provided the theological framework that Muhammad built upon and completed",
        "Meccan trade routes connecting Byzantium, Persia, and Ethiopia exposed Arabia to monotheistic ideas and geopolitical tensions"
    ],
    "effects": [
        "Founded Islam, now the world\u2019s second-largest and fastest-growing religion with 1.9 billion adherents",
        "The Rashidun and Umayyad caliphates spread Islam from Spain to India within 100 years of his death \u2014 creating a civilization rivaling Rome",
        "The Quran standardized classical Arabic, making it the liturgical and literary language of over 400 million people",
        "Islamic scholarship preserved and transmitted Greek philosophy, medicine, and mathematics during the European Dark Ages",
        "Sharia law established comprehensive legal frameworks governing commerce, family, and governance across the Islamic world",
        "The Hajj pilgrimage to Mecca became the largest annual human gathering on Earth, unifying Muslims across all cultures"
    ],
    "relationships": [
        rel("muhammad", "Muhammad", "FULFILLS", "abraham", "Muslims trace Islam to Abraham\u2019s son Ishmael; Muhammad restored the monotheism of Ibrahim"),
        rel("muhammad", "Muhammad", "RECEIVES", "quran", "Received Quranic revelations from Jibril over 23 years (610\u2013632 CE)"),
        rel("muhammad", "Muhammad", "OCCURS_IN", "mecca", "Born in Mecca, received first revelations there, conquered it bloodlessly in 630 CE"),
        rel("muhammad", "Muhammad", "OCCURS_IN", "medina", "Established the first Islamic state in Medina after the Hijra (622 CE)"),
        rel("muhammad", "Muhammad", "INFLUENCES", "saladin", "Saladin modeled his chivalry and governance on Prophetic example during the Crusades"),
        rel("muhammad", "Muhammad", "CONTEMPORARY_OF", "jesus-christ", "Islam honors Jesus (Isa) as a prophet; Muhammad is regarded as the final prophet in the same tradition"),
    ],
    "subjectHeadings": ["People \u2014 Religious Founders \u2014 Arabia \u2014 Medieval"],
    "subjects": ["Islam", "Quran", "Prophet", "Mecca", "Medina", "Hijra", "Sharia", "Caliphate", "Arabia", "Monotheism"],
    "frameworks": ["DOCTRINE_DEVELOPMENT", "CULTURAL_DIFFUSION", "CAUSE_AND_EFFECT", "POLITICAL_SYSTEMS", "LEGAL_INTERPRETATION"],
},

"julius-caesar": {
    "summary": "Gaius Julius Caesar (100\u201344 BCE) was a Roman military commander, statesman, and dictator whose conquest of Gaul, crossing of the Rubicon, and centralization of power ended the Roman Republic and laid the foundation for the Roman Empire \u2014 the most enduring political entity in Western history. Born to the patrician gens Julia (which claimed descent from Venus), Caesar rose through the cursus honorum as quaestor, aedile, and pontifex maximus before securing the consulship (59 BCE) and forming the First Triumvirate with Pompey and Crassus. His Gallic Wars (58\u201350 BCE) conquered all of modern France, Belgium, and parts of Germany and Britain, adding vast territories and wealth to Rome while his Commentarii de Bello Gallico became a masterpiece of Latin prose. When the Senate ordered him to disband his army, Caesar crossed the Rubicon River (January 49 BCE) with the words \u2018alea iacta est\u2019 (the die is cast), triggering civil war. He defeated Pompey at Pharsalus (48 BCE), pursued him to Egypt where he allied with Cleopatra VII, and systematically crushed Pompeian resistance in Africa and Spain. Named dictator perpetuo (dictator in perpetuity) in February 44 BCE, he enacted sweeping reforms: the Julian calendar (basis of the modern Gregorian calendar), land redistribution, citizenship expansion, public works, and debt relief. His assassination by Brutus, Cassius, and 58 other senators on the Ides of March (15 March 44 BCE) \u2014 perhaps history\u2019s most famous political murder \u2014 triggered the wars that destroyed the Republic and elevated his adopted heir Octavian (Augustus) to become Rome\u2019s first emperor. The month of July bears his name.",
    "died": "44 BCE, Rome (Ides of March)",
    "period": "100\u201344 BCE",
    "wikidataQid": "Q1048",
    "wikipediaUrl": "https://en.wikipedia.org/wiki/Julius_Caesar",
    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/4/47/Caesar_Tusculum_Profil.jpg",
    "causes": [
        "The late Roman Republic\u2019s constitutional crisis \u2014 land inequality, army loyalty to commanders over Senate, and factional violence (Marius vs. Sulla) \u2014 created conditions for strongman rule",
        "The populares political movement seeking land reform and citizen rights gave Caesar his power base against the conservative optimates",
        "The First Triumvirate alliance with Pompey and Crassus provided the political leverage to secure Gaul\u2019s governorship and military command"
    ],
    "effects": [
        "Conquered Gaul, extending Roman territory to the Atlantic and English Channel and adding 3 million subjects to the Republic",
        "The crossing of the Rubicon (49 BCE) ended the Roman Republic\u2019s pretense of constitutional government and established the precedent for military dictatorship",
        "The Julian calendar reform (46 BCE) created the basis for the Gregorian calendar used worldwide today",
        "His assassination triggered the Final War of the Roman Republic, leading to Augustus and the Roman Empire (27 BCE)",
        "His literary works (De Bello Gallico) became foundational Latin texts studied for two millennia",
        "The title \u2018Caesar\u2019 became synonymous with supreme ruler \u2014 producing Kaiser (German) and Tsar (Russian)"
    ],
    "relationships": [
        rel("julius-caesar", "Julius Caesar", "CAUSES", "augustus", "Caesar\u2019s assassination and will made Octavian (Augustus) his heir, leading to the Roman Empire"),
        rel("julius-caesar", "Julius Caesar", "ALLIED_WITH", "cleopatra", "Caesar allied with and had a son (Caesarion) with Cleopatra VII during the Egyptian civil war (48 BCE)"),
        rel("julius-caesar", "Julius Caesar", "CONQUERS", "ancient-gaul", "Conquered all of Gaul in the Gallic Wars (58\u201350 BCE), extending Rome to the Atlantic"),
        rel("julius-caesar", "Julius Caesar", "OPPOSES", "pompey", "Defeated Pompey at Pharsalus (48 BCE) in the Roman Civil War"),
        rel("julius-caesar", "Julius Caesar", "OCCURS_IN", "roman-republic", "Served as consul, proconsul of Gaul, and dictator perpetuo of the Roman Republic"),
        rel("julius-caesar", "Julius Caesar", "DESCRIBED_IN", "de-bello-gallico", "His Commentarii de Bello Gallico is a first-person account of the Gallic Wars"),
    ],
    "subjectHeadings": ["People \u2014 Military & Political Leaders \u2014 Rome \u2014 Classical"],
    "subjects": ["Roman Republic", "Gallic Wars", "Rubicon", "Dictatorship", "Assassination", "Julian Calendar", "Latin Literature", "Ancient Rome", "Military Strategy", "Civil War"],
    "frameworks": ["POLITICAL_SYSTEMS", "CAUSE_AND_EFFECT", "MILITARY_HISTORY", "CULTURAL_DIFFUSION", "LEGAL_INTERPRETATION"],
},

"aristotle": {
    "summary": "Aristotle (384\u2013322 BCE) was a Greek philosopher and polymath whose works constitute the first comprehensive system of Western philosophy \u2014 encompassing logic, metaphysics, ethics, politics, biology, physics, rhetoric, and poetics. Born in Stagira, Macedonia, son of the physician Nicomachus (personal doctor to King Amyntas III), he entered Plato\u2019s Academy at age 17 and studied there for 20 years until Plato\u2019s death. After tutoring the young Alexander the Great (343\u2013335 BCE), he founded the Lyceum in Athens, where his school of \u2018Peripatetics\u2019 (named for their habit of walking while lecturing) became antiquity\u2019s premier research institution. Aristotle\u2019s Organon created formal logic \u2014 the syllogism remained the foundation of deductive reasoning for over 2,000 years until Frege\u2019s modern predicate logic (1879). His Nicomachean Ethics defined eudaimonia (human flourishing through virtuous activity) as the highest good. His Politics classified constitutions and argued that humans are \u2018political animals\u2019 (zoon politikon). His Physics and Metaphysics dominated natural philosophy until the Scientific Revolution. His biological works classified over 500 animal species through direct observation, making him the founder of zoology and comparative anatomy. His Poetics defined tragedy, catharsis, and the unities that governed Western drama for centuries. Transmitted to medieval Europe through Arabic translations (especially by Averroes and Avicenna), Aristotle\u2019s works were synthesized with Christian theology by Thomas Aquinas in the Summa Theologica, making him simply \u2018The Philosopher\u2019 in Scholastic thought. Dante called him \u2018the master of those who know.\u2019",
    "died": "322 BCE, Chalcis, Euboea",
    "period": "384\u2013322 BCE",
    "wikidataQid": "Q868",
    "wikipediaUrl": "https://en.wikipedia.org/wiki/Aristotle",
    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/a/ae/Aristotle_Altemps_Inv8575.jpg",
    "causes": [
        "Plato\u2019s Academy provided the intellectual foundation, but Aristotle\u2019s empirical temperament led him to develop a rival system grounded in observation rather than pure idealism",
        "The golden age of Athens (5th\u20134th century BCE) created unprecedented conditions for philosophical inquiry, debate, and institutional learning",
        "His father Nicomachus\u2019s medical background instilled a scientific, empirical approach to knowledge that distinguished Aristotle from purely speculative philosophers"
    ],
    "effects": [
        "Created formal logic (the syllogism), which remained the foundation of Western reasoning for over 2,000 years",
        "Founded the Lyceum, antiquity\u2019s premier research institution, pioneering systematic empirical investigation",
        "His biological classification of 500+ species founded zoology and comparative anatomy as scientific disciplines",
        "Thomas Aquinas\u2019s synthesis of Aristotelian philosophy with Christian theology became the intellectual framework of medieval Europe",
        "Arabic translations by Averroes and Avicenna preserved and transmitted his works during the Islamic Golden Age",
        "His Poetics defined Western literary criticism and dramatic theory from antiquity through the 18th century"
    ],
    "relationships": [
        rel("aristotle", "Aristotle", "STUDENT_OF", "plato", "Studied at Plato\u2019s Academy for 20 years (367\u2013347 BCE)"),
        rel("aristotle", "Aristotle", "TEACHES", "alexander-the-great", "Tutored Alexander of Macedon (343\u2013335 BCE), shaping the conqueror\u2019s intellectual horizons"),
        rel("aristotle", "Aristotle", "INFLUENCES", "socrates", "Built upon the Socratic method while rejecting Plato\u2019s Theory of Forms"),
        rel("aristotle", "Aristotle", "ESTABLISHES", "lyceum", "Founded the Lyceum in Athens (335 BCE), rivaling Plato\u2019s Academy"),
        rel("aristotle", "Aristotle", "OCCURS_IN", "ancient-greece", "Lived and taught in Athens, the intellectual capital of the ancient world"),
        rel("aristotle", "Aristotle", "INFLUENCES", "thomas-aquinas", "Aquinas\u2019s Summa Theologica synthesized Aristotelian philosophy with Christian theology"),
    ],
    "subjectHeadings": ["People \u2014 Philosophers & Thinkers \u2014 Greece \u2014 Classical"],
    "subjects": ["Philosophy", "Logic", "Ethics", "Politics", "Biology", "Metaphysics", "Rhetoric", "Poetics", "Ancient Greece", "Empiricism"],
    "frameworks": ["DOCTRINE_DEVELOPMENT", "CAUSE_AND_EFFECT", "INNOVATION_AND_TECHNOLOGY", "CULTURAL_DIFFUSION", "ETHICAL_FRAMEWORK"],
},

"plato": {
    "summary": "Plato (c. 428\u2013348 BCE) was an Athenian philosopher whose dialogues, Academy, and Theory of Forms established the foundation of Western philosophy, metaphysics, and political theory. Born to one of Athens\u2019s most aristocratic families (his mother Perictione was descended from Solon), he became Socrates\u2019s most brilliant student and spent 12 years under his tutelage until Socrates\u2019s execution in 399 BCE \u2014 an event that turned Plato from politics to philosophy. After traveling to Egypt, Italy, and Syracuse (where he unsuccessfully tried to create his ideal state), he founded the Academy in Athens (c. 387 BCE), the Western world\u2019s first institution of higher learning, which operated continuously for over 900 years until closed by Emperor Justinian in 529 CE. Plato\u2019s 36 dialogues \u2014 featuring Socrates as chief interlocutor \u2014 explored justice (Republic), love (Symposium), the immortality of the soul (Phaedo), knowledge (Theaetetus), and the nature of reality (Timaeus). His Theory of Forms posited that the physical world is a shadow of eternal, perfect Ideas (Forms), most famously illustrated in the Allegory of the Cave. The Republic outlined his vision of the ideal state governed by philosopher-kings, with the tripartite soul (reason, spirit, appetite) mirrored in three social classes. Alfred North Whitehead famously declared that \u2018the safest general characterization of the European philosophical tradition is that it consists of a series of footnotes to Plato.\u2019 His influence permeates Christian theology (through Neo-Platonism and Augustine), Islamic philosophy (al-Farabi\u2019s \u2018The Virtuous City\u2019), Renaissance humanism, and modern political theory.",
    "died": "c. 348 BCE, Athens",
    "period": "c. 428\u2013348 BCE",
    "wikidataQid": "Q859",
    "wikipediaUrl": "https://en.wikipedia.org/wiki/Plato",
    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/8/88/Plato_Silanion_Musei_Capitolini_MC1377.jpg",
    "causes": [
        "The execution of Socrates (399 BCE) by Athenian democracy disillusioned Plato with politics and drove him toward philosophical inquiry about justice and the ideal state",
        "The Athenian golden age and its democratic culture created the intellectual environment for sustained philosophical debate and public discourse",
        "Pythagorean mathematical philosophy (encountered during Plato\u2019s travels to southern Italy) deeply influenced his Theory of Forms and belief in abstract truth"
    ],
    "effects": [
        "Founded the Academy (c. 387 BCE), the Western world\u2019s first university, which operated for over 900 years",
        "The Theory of Forms became the basis of Western metaphysics, influencing Christian theology through Neo-Platonism and Augustine",
        "The Republic established political philosophy as a discipline and introduced the concept of the philosopher-king",
        "His dialogic method preserved Socratic philosophy and created Western literature\u2019s first philosophical dramas",
        "Neo-Platonism (Plotinus, 3rd century CE) transformed his ideas into a mystical system that influenced Christianity, Islam, and Judaism",
        "Renaissance humanism (Ficino\u2019s Platonic Academy in Florence) revived Platonic idealism and sparked the modern era"
    ],
    "relationships": [
        rel("plato", "Plato", "STUDENT_OF", "socrates", "Studied under Socrates for 12 years; Socrates\u2019s execution in 399 BCE transformed Plato\u2019s life"),
        rel("plato", "Plato", "TEACHES", "aristotle", "Aristotle studied at Plato\u2019s Academy for 20 years (367\u2013347 BCE)"),
        rel("plato", "Plato", "ESTABLISHES", "the-academy", "Founded the Academy in Athens (c. 387 BCE), the first institution of higher learning in the West"),
        rel("plato", "Plato", "AUTHORS", "republic-plato", "The Republic outlined the ideal state governed by philosopher-kings"),
        rel("plato", "Plato", "OCCURS_IN", "ancient-greece", "Lived and taught in Athens during the classical period"),
        rel("plato", "Plato", "INFLUENCES", "augustine-of-hippo", "Neo-Platonic philosophy profoundly shaped Augustine\u2019s Christian theology"),
    ],
    "subjectHeadings": ["People \u2014 Philosophers & Thinkers \u2014 Greece \u2014 Classical"],
    "subjects": ["Philosophy", "Theory of Forms", "Republic", "Academy", "Metaphysics", "Political Theory", "Allegory of the Cave", "Socratic Method", "Ancient Greece", "Athens"],
    "frameworks": ["DOCTRINE_DEVELOPMENT", "CAUSE_AND_EFFECT", "POLITICAL_SYSTEMS", "CULTURAL_DIFFUSION", "ETHICAL_FRAMEWORK"],
},

"socrates": {
    "summary": "Socrates (c. 470\u2013399 BCE) was an Athenian philosopher whose relentless questioning of assumptions, refusal to write, and voluntary death by hemlock made him the founding martyr of Western philosophy. Born to Sophroniscus (a stonemason) and Phaenarete (a midwife), he served with distinction as a hoplite at Potidaea, Delium, and Amphipolis. Rather than pursue wealth or political power, he spent his life in the agora engaging citizens in dialogue \u2014 the \u2018Socratic method\u2019 of cross-examination (elenchus) that exposed contradictions in conventional wisdom. He claimed to know only that he knew nothing (Socratic ignorance), and the Oracle at Delphi declared him the wisest man in Athens precisely because he alone recognized the limits of his knowledge. His insistence that \u2018the unexamined life is not worth living\u2019 and that virtue is knowledge (to know the good is to do the good) laid the ethical foundations of Western thought. Though he wrote nothing, his students Plato, Xenophon, and Aristophanes preserved his teachings in dialogues, memoirs, and comedy. In 399 BCE, Athens convicted him of impiety and corrupting the youth \u2014 likely political retribution for his associations with Alcibiades and Critias. He refused exile, drank the hemlock, and died surrounded by disciples (as depicted in Plato\u2019s Phaedo) \u2014 an act of principled civil disobedience that has inspired philosophers from Seneca to Martin Luther King Jr. His legacy: every subsequent Western philosopher either built upon or reacted against his method.",
    "died": "399 BCE, Athens (execution by hemlock)",
    "period": "c. 470\u2013399 BCE",
    "wikidataQid": "Q913",
    "wikipediaUrl": "https://en.wikipedia.org/wiki/Socrates",
    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/b/bc/Socrate_du_Louvre.jpg",
    "causes": [
        "The Athenian democratic culture of free speech (parrhesia) and public debate in the agora enabled Socrates\u2019s philosophical mission",
        "The Sophist movement\u2019s relativistic teachings provoked Socrates\u2019s counter-quest for absolute moral truth through dialectical inquiry",
        "The Oracle at Delphi\u2019s declaration that no one was wiser than Socrates launched his lifelong mission to test this claim through questioning"
    ],
    "effects": [
        "Created the Socratic method (elenchus), the foundation of Western pedagogy, legal cross-examination, and the scientific method of inquiry",
        "His execution (399 BCE) became the defining martyr narrative of Western philosophy, inspiring centuries of reflection on conscience vs. state authority",
        "Directly trained Plato, whose Academy and writings transmitted Socratic philosophy to all subsequent Western thought",
        "The Socratic schools (Cynics, Stoics, Skeptics, Megarians) branched from his teachings, creating the main currents of Hellenistic philosophy",
        "His concept of \u2018the examined life\u2019 established self-reflection as a core Western value \u2014 from Stoic meditation to modern psychotherapy",
        "Civil disobedience tradition: Socrates\u2019s refusal to flee inspired Thoreau, Gandhi, and Martin Luther King Jr."
    ],
    "relationships": [
        rel("socrates", "Socrates", "TEACHES", "plato", "Plato studied under Socrates for 12 years and immortalized him in 36 dialogues"),
        rel("socrates", "Socrates", "INFLUENCES", "aristotle", "Aristotle inherited the Socratic tradition through Plato\u2019s Academy"),
        rel("socrates", "Socrates", "CONTEMPORARY_OF", "confucius", "Both Axial Age ethical thinkers: Confucius died c. 479 BCE, Socrates born c. 470 BCE"),
        rel("socrates", "Socrates", "OCCURS_IN", "ancient-greece", "Lived and taught in Athens during the golden age and Peloponnesian War"),
        rel("socrates", "Socrates", "INFLUENCES", "mahatma-gandhi", "Gandhi\u2019s civil disobedience drew on Socrates\u2019s principled refusal to flee execution"),
        rel("socrates", "Socrates", "INFLUENCES", "martin-luther-king-jr", "King cited Socrates in \u2018Letter from Birmingham Jail\u2019 as a precedent for civil disobedience"),
    ],
    "subjectHeadings": ["People \u2014 Philosophers & Thinkers \u2014 Greece \u2014 Classical"],
    "subjects": ["Philosophy", "Socratic Method", "Ethics", "Dialectic", "Athens", "Ancient Greece", "Trial", "Civil Disobedience", "Elenchus", "Virtue"],
    "frameworks": ["DOCTRINE_DEVELOPMENT", "CAUSE_AND_EFFECT", "ETHICAL_FRAMEWORK", "SOCIAL_STRUCTURES", "CULTURAL_DIFFUSION"],
},

"augustus": {
    "summary": "Augustus (Gaius Octavius Thurinus, 63 BCE \u2013 14 CE), born Octavian, was the first Roman Emperor and founder of the Principate \u2014 the political system that governed the Roman world for over four centuries and laid the foundation for Western governance. Adopted posthumously as Julius Caesar\u2019s heir at age 18, he methodically defeated every rival: forming the Second Triumvirate with Mark Antony and Lepidus, proscribing 300 senators and 2,000 equestrians, defeating Brutus and Cassius at Philippi (42 BCE), and finally crushing Antony and Cleopatra at the Battle of Actium (31 BCE) \u2014 the naval engagement that ended the Roman Republic. In 27 BCE the Senate awarded him the title \u2018Augustus\u2019 (\u2018the Revered One\u2019), and he crafted a constitutional fiction: officially restoring the Republic while accumulating imperium, tribunicia potestas, and the role of pontifex maximus \u2014 effectively becoming sole ruler while maintaining Republican forms. His 41-year reign (27 BCE \u2013 14 CE) inaugurated the Pax Romana, two centuries of unprecedented peace, prosperity, and cultural achievement. He reformed taxation, established the Praetorian Guard, built a permanent professional army of 28 legions, created the vigiles (fire brigade) and urban cohorts (police), sponsored Virgil\u2019s Aeneid and Livy\u2019s histories, and transformed Rome from a city of brick into a city of marble. The Res Gestae Divi Augusti, his political autobiography inscribed on bronze tablets, is one of antiquity\u2019s most important documents. His legacy: the concept of a \u2018First Citizen\u2019 governing within constitutional forms \u2014 a model emulated by monarchs and dictators for two millennia. The month of August bears his name.",
    "died": "14 CE, Nola",
    "period": "63 BCE \u2013 14 CE",
    "wikidataQid": "Q1405",
    "wikipediaUrl": "https://en.wikipedia.org/wiki/Augustus",
    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Augustus_Bevilacqua_Glyptothek_Munich_317.jpg",
    "causes": [
        "Julius Caesar\u2019s assassination (44 BCE) and his adoption of Octavian as heir thrust the 18-year-old into the center of Roman power politics",
        "The century-long constitutional crisis of the late Roman Republic (Marius, Sulla, Pompey, Caesar) made one-man rule increasingly inevitable",
        "The Battle of Actium (31 BCE) eliminated Antony and Cleopatra as the last obstacles to Octavian\u2019s sole control"
    ],
    "effects": [
        "Founded the Roman Principate (27 BCE), the political system that governed the Mediterranean world for over 400 years",
        "Inaugurated the Pax Romana \u2014 two centuries of relative peace enabling unprecedented cultural, economic, and architectural achievement",
        "Transformed Rome from \u2018a city of brick to a city of marble\u2019 with massive building programs (Forum of Augustus, Ara Pacis, Pantheon commission)",
        "Established the professional standing army and administrative bureaucracy that became the template for European statecraft",
        "The Augustan literary golden age (Virgil, Horace, Ovid, Livy) produced Latin literature\u2019s greatest works",
        "Jesus of Nazareth was born during Augustus\u2019s reign (Luke 2:1) \u2014 the census that brought Mary and Joseph to Bethlehem"
    ],
    "relationships": [
        rel("augustus", "Augustus", "HEIR_OF", "julius-caesar", "Adopted as Caesar\u2019s heir in his will; avenged his assassination and inherited his political legacy"),
        rel("augustus", "Augustus", "DEFEATS", "mark-antony", "Defeated Antony and Cleopatra at the Battle of Actium (31 BCE)"),
        rel("augustus", "Augustus", "DEFEATS", "cleopatra", "Cleopatra\u2019s suicide after Actium ended the Ptolemaic dynasty and made Egypt a Roman province"),
        rel("augustus", "Augustus", "ESTABLISHES", "roman-empire", "Founded the Roman Empire/Principate system (27 BCE) that lasted over 400 years"),
        rel("augustus", "Augustus", "OCCURS_IN", "roman-republic", "Rose to power during the final decades of the Roman Republic"),
        rel("augustus", "Augustus", "CONTEMPORARY_OF", "jesus-christ", "Jesus was born during Augustus\u2019s census (Luke 2:1), connecting Christianity\u2019s origin to Roman imperial history"),
    ],
    "subjectHeadings": ["People \u2014 Emperors & Rulers \u2014 Rome \u2014 Classical"],
    "subjects": ["Roman Empire", "Principate", "Pax Romana", "Actium", "Augustus", "Imperial Rome", "Constitutional Reform", "Ancient Rome", "Military", "Administration"],
    "frameworks": ["POLITICAL_SYSTEMS", "CAUSE_AND_EFFECT", "MILITARY_HISTORY", "CULTURAL_DIFFUSION", "SOCIAL_STRUCTURES"],
},

"cleopatra": {
    "summary": "Cleopatra VII Philopator (69\u201330 BCE) was the last active ruler of the Ptolemaic Kingdom of Egypt, a polyglot diplomat, naval commander, and political strategist whose alliances with Julius Caesar and Mark Antony made her the most powerful woman in the ancient Mediterranean world. She was the first Ptolemaic ruler in 300 years to learn the Egyptian language (she spoke nine languages total) and deliberately cultivated her image as the living incarnation of the goddess Isis. Ascending the throne at 18 alongside her brother-husband Ptolemy XIII, she was deposed in a palace coup but restored to power after allying with Julius Caesar, who came to Egypt in pursuit of Pompey (48 BCE). She bore Caesar a son, Caesarion, and lived openly with him in Rome until his assassination (44 BCE). She then formed a political and romantic alliance with Mark Antony (41 BCE), who recognized their children as rulers of various eastern territories in the Donations of Alexandria (34 BCE) \u2014 a direct challenge to Rome. Their combined forces were crushed by Octavian at the Battle of Actium (31 BCE). Rather than be paraded in Octavian\u2019s triumph, she died by her own hand (tradition says by asp) on August 12, 30 BCE. With her death, the 3,000-year-old tradition of Egyptian pharaonic rule ended, and Egypt became a Roman province. Her legacy transcends history: she has been the subject of over 200 films, plays (Shakespeare\u2019s Antony and Cleopatra), operas, and novels \u2014 one of the most depicted women in world history.",
    "died": "30 BCE, Alexandria (suicide)",
    "period": "69\u201330 BCE",
    "wikidataQid": "Q635",
    "wikipediaUrl": "https://en.wikipedia.org/wiki/Cleopatra",
    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Kleopatra-VII.-Altes-Museum-Berlin1.jpg",
    "causes": [
        "The declining Ptolemaic dynasty needed a strong ruler to navigate between Rome\u2019s rival factions and preserve Egyptian independence",
        "Julius Caesar\u2019s arrival in Egypt (48 BCE) during the Roman civil war created the opportunity for an alliance that restored Cleopatra to power",
        "The strategic importance of Egypt\u2019s grain supply to Rome made its ruler a critical factor in Roman power politics"
    ],
    "effects": [
        "Her death (30 BCE) ended 3,000 years of pharaonic rule and made Egypt a Roman province \u2014 Rome\u2019s most valuable territory",
        "The Battle of Actium (31 BCE) ended the Roman Republic era and enabled Augustus to establish the Roman Empire",
        "Her image as a seductive foreign queen shaped Western stereotypes about women in power for two millennia",
        "Alexandrian scholarship continued under Roman rule partly due to the cultural institutions she patronized",
        "Shakespeare\u2019s Antony and Cleopatra (1607) and subsequent artistic depictions made her one of the most portrayed historical figures ever",
        "Her use of Egyptian religious imagery (Isis incarnation) demonstrated the political power of cultural identity in diplomacy"
    ],
    "relationships": [
        rel("cleopatra", "Cleopatra VII", "ALLIED_WITH", "julius-caesar", "Alliance with Caesar restored her to the Egyptian throne and produced their son Caesarion (47 BCE)"),
        rel("cleopatra", "Cleopatra VII", "ALLIED_WITH", "mark-antony", "Political and romantic alliance (41\u201330 BCE) that challenged Octavian\u2019s control of the Roman world"),
        rel("cleopatra", "Cleopatra VII", "OPPOSES", "augustus", "Defeated by Octavian at Actium (31 BCE); her suicide prevented his triumph"),
        rel("cleopatra", "Cleopatra VII", "RULES", "ancient-egypt", "Last active ruler of the Ptolemaic Kingdom, ending 3,000 years of pharaonic tradition"),
        rel("cleopatra", "Cleopatra VII", "OCCURS_IN", "alexandria", "Ruled from Alexandria, the Mediterranean\u2019s greatest cultural and commercial center"),
    ],
    "subjectHeadings": ["People \u2014 Monarchs & Rulers \u2014 Egypt \u2014 Classical"],
    "subjects": ["Ptolemaic Egypt", "Alexandria", "Roman Republic", "Actium", "Isis", "Diplomacy", "Ancient Egypt", "Female Rulers", "Mediterranean", "Hellenistic Period"],
    "frameworks": ["POLITICAL_SYSTEMS", "CAUSE_AND_EFFECT", "CULTURAL_DIFFUSION", "GENDER_AND_SOCIETY", "MILITARY_HISTORY"],
},

"genghis-khan": {
    "summary": "Genghis Khan (Temujin, c. 1162\u20131227 CE) was the founder of the Mongol Empire \u2014 the largest contiguous land empire in human history, stretching from Korea to Hungary and encompassing one-quarter of the world\u2019s population at its peak. Born as Temujin to a minor Mongol chieftain who was poisoned by rivals when the boy was nine, he endured kidnapping, enslavement, and betrayal before unifying the fractious Mongol and Turkic tribes through a combination of military genius, meritocratic promotion (replacing aristocratic privilege with ability-based advancement), and the Yasa \u2014 a legal code that imposed discipline, religious tolerance, diplomatic immunity, and a merit-based army structure unprecedented in steppe history. Proclaimed \u2018Genghis Khan\u2019 (Universal Ruler) in 1206, he systematically conquered the Tangut Xi Xia kingdom, the Jin Dynasty of northern China, the Khwarazmian Empire (devastating Samarkand, Bukhara, and Balkh), and raided as far as the Caucasus and Eastern Europe. His military innovations \u2014 decimal organization, composite bow cavalry, psychological warfare, intelligence networks, and siege engineering borrowed from conquered peoples \u2014 created the most effective fighting force of the medieval world. Though his conquests killed an estimated 40 million people (roughly 10% of the world\u2019s population), the resulting Pax Mongolica enabled the reopening of the Silk Road, direct contact between Europe and China, the transfer of gunpowder, printing, and the compass westward, and Marco Polo\u2019s famous journey. A 2003 genetic study estimated that approximately 16 million men alive today (0.5% of males globally) carry his Y-chromosome \u2014 making him possibly the most prolific progenitor in human history.",
    "died": "1227 CE",
    "period": "c. 1162\u20131227 CE",
    "wikidataQid": "Q720",
    "wikipediaUrl": "https://en.wikipedia.org/wiki/Genghis_Khan",
    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/3/35/YuanEmperorAlbumGenghisPortrait.jpg",
    "causes": [
        "The fragmented Mongolian steppe, with constant inter-tribal warfare and blood feuds, created conditions for a unifier who could transcend clan loyalties",
        "Temujin\u2019s personal hardships (father\u2019s murder, enslavement, betrayal by blood-brother Jamukha) forged his resilience and ruthless strategic thinking",
        "The weakness of neighboring empires (Jin Dynasty internal corruption, Khwarazmian diplomatic arrogance) created military opportunities"
    ],
    "effects": [
        "Created the largest contiguous land empire in history (24 million km\u00b2 at peak), connecting Europe, the Middle East, and East Asia",
        "The Pax Mongolica reopened the Silk Road, enabling unprecedented cultural, technological, and commercial exchange between East and West",
        "Facilitated the westward transfer of gunpowder, printing, and the compass \u2014 technologies that transformed European civilization",
        "An estimated 40 million deaths (10% of world population) \u2014 reshaping demographics across Eurasia and reducing global CO2 levels measurably",
        "The Yasa legal code established principles of religious tolerance, meritocracy, and diplomatic immunity across the empire",
        "Marco Polo\u2019s journey to Kublai Khan\u2019s court was made possible by Mongol unification, inspiring the European Age of Exploration"
    ],
    "relationships": [
        rel("genghis-khan", "Genghis Khan", "ESTABLISHES", "mongol-empire", "Founded the Mongol Empire (1206), which expanded to become the largest contiguous land empire ever"),
        rel("genghis-khan", "Genghis Khan", "CONQUERS", "khwarazmian-empire", "Destroyed the Khwarazmian Empire (1219\u20131221), devastating Central Asia\u2019s great cities"),
        rel("genghis-khan", "Genghis Khan", "ENABLES", "marco-polo", "The Pax Mongolica made Marco Polo\u2019s journey to China possible (1271\u20131295)"),
        rel("genghis-khan", "Genghis Khan", "INFLUENCES", "kublai-khan", "Grandson Kublai Khan completed China\u2019s conquest and founded the Yuan Dynasty"),
        rel("genghis-khan", "Genghis Khan", "OCCURS_IN", "mongolia", "United the Mongol tribes on the steppe and was proclaimed Universal Ruler at the Khuriltai of 1206"),
        rel("genghis-khan", "Genghis Khan", "TRANSFORMS", "silk-road", "Mongol Empire\u2019s Pax Mongolica reopened the Silk Road for centuries of East-West exchange"),
    ],
    "subjectHeadings": ["People \u2014 Conquerors & Military Leaders \u2014 Mongolia \u2014 Medieval"],
    "subjects": ["Mongol Empire", "Conquest", "Silk Road", "Pax Mongolica", "Yasa", "Steppe Warfare", "Medieval Asia", "Mongolia", "Central Asia", "Military Innovation"],
    "frameworks": ["MILITARY_HISTORY", "CAUSE_AND_EFFECT", "CULTURAL_DIFFUSION", "POLITICAL_SYSTEMS", "TRADE_AND_EXCHANGE"],
},

"martin-luther": {
    "summary": "Martin Luther (1483\u20131546) was a German Augustinian friar, theologian, and professor whose Ninety-Five Theses (1517), doctrine of justification by faith alone (sola fide), and translation of the Bible into German ignited the Protestant Reformation \u2014 the most consequential schism in Western Christianity and a catalyst for modern individualism, literacy, and political liberty. Born in Eisleben, Saxony, to a copper miner\u2019s family, Luther entered the Augustinian monastery at Erfurt after a terrifying lightning storm (1505) and was ordained in 1507. Tormented by the question of divine righteousness, he experienced his \u2018Tower Experience\u2019 (c. 1515) while studying Romans 1:17 \u2014 the revelation that salvation comes through faith, not works, upending 1,000 years of Catholic merit-based soteriology. On October 31, 1517, he posted the Ninety-Five Theses challenging the sale of indulgences, which spread across Europe within weeks thanks to Gutenberg\u2019s printing press. At the Diet of Worms (1521), he refused to recant before Emperor Charles V: \u2018Here I stand; I can do no other.\u2019 Protected by Frederick the Wise in Wartburg Castle, he translated the New Testament into German in just 11 weeks \u2014 a literary masterpiece that standardized the German language as Dante\u2019s Commedia had standardized Italian. Luther\u2019s writings (over 60 volumes) articulated the five solas (sola scriptura, sola fide, sola gratia, solus Christus, soli Deo gloria), catalyzed the formation of Lutheran, Reformed, and eventually all Protestant churches, and indirectly contributed to the Wars of Religion, the Peace of Westphalia (1648), the concept of sovereign nation-states, and the Enlightenment\u2019s emphasis on individual conscience.",
    "died": "1546 CE, Eisleben",
    "period": "1483\u20131546 CE",
    "wikidataQid": "Q9554",
    "wikipediaUrl": "https://en.wikipedia.org/wiki/Martin_Luther",
    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/9/95/Lucas_Cranach_d.%C3%84._-_Martin_Luther%2C_1528_%28Veste_Coburg%29.jpg",
    "causes": [
        "The sale of indulgences by Johann Tetzel (\u2018As soon as the coin in the coffer rings, the soul from purgatory springs\u2019) provoked Luther\u2019s theological protest",
        "The corruption and worldliness of the Renaissance papacy (Alexander VI, Julius II, Leo X) undermined the Church\u2019s moral authority",
        "Gutenberg\u2019s printing press (1440) enabled rapid dissemination of Luther\u2019s writings across Europe within weeks"
    ],
    "effects": [
        "Launched the Protestant Reformation, permanently splitting Western Christianity into Catholic and Protestant branches",
        "His German Bible translation standardized the German language and made Scripture directly accessible to laypeople",
        "The principle of sola scriptura elevated individual Bible reading and literacy, driving educational reform across Protestant Europe",
        "Contributed to the Wars of Religion (1524\u20131648) and the Peace of Westphalia, which established the modern system of sovereign nation-states",
        "The doctrine of the priesthood of all believers challenged hierarchical authority and contributed to democratic political thought",
        "Lutheran hymnody (\u2018A Mighty Fortress Is Our God\u2019) established congregational singing and influenced Bach, Protestant worship, and Western music"
    ],
    "relationships": [
        rel("martin-luther", "Martin Luther", "OPPOSES", "catholic-church", "His Ninety-Five Theses (1517) challenged papal authority and indulgence theology"),
        rel("martin-luther", "Martin Luther", "INFLUENCES", "john-calvin", "Luther\u2019s theology of grace directly influenced Calvin\u2019s Reformed theology"),
        rel("martin-luther", "Martin Luther", "ENABLED_BY", "johannes-gutenberg", "The printing press made Luther\u2019s writings the first mass-media phenomenon"),
        rel("martin-luther", "Martin Luther", "OCCURS_IN", "holy-roman-empire", "Lived, taught, and defied papal authority within the Holy Roman Empire"),
        rel("martin-luther", "Martin Luther", "ESTABLISHES", "reformation", "His protest launched the Protestant Reformation that reshaped Western civilization"),
        rel("martin-luther", "Martin Luther", "AUTHORS", "ninety-five-theses", "Posted the Ninety-Five Theses on October 31, 1517 \u2014 the symbolic start of the Reformation"),
    ],
    "subjectHeadings": ["People \u2014 Religious Reformers \u2014 Germany \u2014 Early Modern"],
    "subjects": ["Protestant Reformation", "Ninety-Five Theses", "Sola Fide", "Sola Scriptura", "German Bible", "Lutheranism", "Indulgences", "Worms", "Theology", "Germany"],
    "frameworks": ["DOCTRINE_DEVELOPMENT", "CAUSE_AND_EFFECT", "CULTURAL_DIFFUSION", "RELIGIOUS_INSTITUTIONS", "INNOVATION_AND_TECHNOLOGY"],
},

"galileo-galilei": {
    "summary": "Galileo Galilei (1564\u20131642) was an Italian astronomer, physicist, and mathematician whose telescopic observations, experimental method, and confrontation with the Catholic Church made him the \u2018father of modern observational astronomy,\u2019 the \u2018father of modern physics,\u2019 and the \u2018father of modern science\u2019 (Einstein). Born in Pisa, he discovered the isochrony of pendulums (allegedly timing a swinging chandelier in Pisa Cathedral with his pulse), developed the thermoscope, and held mathematics chairs at Pisa and Padua. In 1609, upon hearing of the Dutch spyglass, he built his own telescope (with 20\u00d7 magnification) and turned it skyward \u2014 discovering the four largest moons of Jupiter (Io, Europa, Ganymede, Callisto), the phases of Venus, sunspots, lunar craters, and the Milky Way\u2019s composition of individual stars. These observations, published in Sidereus Nuncius (1610), provided the first empirical evidence for Copernicus\u2019s heliocentric model and demolished the Aristotelian-Ptolemaic cosmology that had reigned for 1,400 years. His Dialogue Concerning the Two Chief World Systems (1632) presented heliocentrism so persuasively that the Roman Inquisition convicted him of \u2018vehement suspicion of heresy\u2019 (1633), forcing him to recant and placing him under house arrest for the remainder of his life. Legend holds that upon recanting he muttered \u2018Eppur si muove\u2019 (\u2018And yet it moves\u2019). During house arrest at Arcetri, though blind, he produced his greatest scientific work: Discourses and Mathematical Demonstrations Relating to Two New Sciences (1638), which laid the foundations of kinematics and material strength. The Vatican formally acknowledged its error in 1992. Stephen Hawking was born exactly 300 years after Galileo\u2019s death.",
    "died": "1642 CE, Arcetri",
    "period": "1564\u20131642 CE",
    "wikidataQid": "Q307",
    "wikipediaUrl": "https://en.wikipedia.org/wiki/Galileo_Galilei",
    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Justus_Sustermans_-_Portrait_of_Galileo_Galilei%2C_1636.jpg",
    "causes": [
        "Copernicus\u2019s De Revolutionibus (1543) proposed heliocentrism but lacked observational proof \u2014 Galileo\u2019s telescope provided it",
        "The Renaissance revival of empirical inquiry and mathematical natural philosophy created the intellectual environment for Galileo\u2019s work",
        "The invention of the Dutch spyglass (1608) gave Galileo the idea to build a superior telescope for astronomical observation"
    ],
    "effects": [
        "His telescopic discoveries provided the first empirical evidence for heliocentrism, ending 1,400 years of geocentric cosmology",
        "Founded modern experimental physics with his studies of motion, falling bodies, and projectile trajectories",
        "His conflict with the Inquisition (1633) became the defining symbol of the tension between science and religious authority",
        "Two New Sciences (1638) laid the groundwork for Newton\u2019s mechanics and the entire edifice of classical physics",
        "Discovery of Jupiter\u2019s moons proved that not all celestial bodies orbit Earth, undermining the geocentric model",
        "His insistence on mathematical description of nature (\u2018the book of nature is written in mathematics\u2019) established the methodology of modern science"
    ],
    "relationships": [
        rel("galileo-galilei", "Galileo Galilei", "VALIDATES", "copernicus", "Galileo\u2019s telescopic observations confirmed Copernicus\u2019s heliocentric model"),
        rel("galileo-galilei", "Galileo Galilei", "INFLUENCES", "isaac-newton", "Newton\u2019s laws of motion and universal gravitation built directly on Galileo\u2019s kinematics"),
        rel("galileo-galilei", "Galileo Galilei", "OPPOSES", "catholic-church", "The Inquisition convicted him of heresy (1633) for defending heliocentrism"),
        rel("galileo-galilei", "Galileo Galilei", "OCCURS_IN", "renaissance-italy", "Worked in Pisa, Padua, and Florence during the Italian Renaissance"),
        rel("galileo-galilei", "Galileo Galilei", "AUTHORS", "sidereus-nuncius", "Published Sidereus Nuncius (1610), announcing his groundbreaking telescopic discoveries"),
        rel("galileo-galilei", "Galileo Galilei", "CONTEMPORARY_OF", "william-shakespeare", "Both born in 1564: Galileo transformed science, Shakespeare transformed literature"),
    ],
    "subjectHeadings": ["People \u2014 Scientists & Inventors \u2014 Italy \u2014 Early Modern"],
    "subjects": ["Astronomy", "Physics", "Telescope", "Heliocentrism", "Scientific Revolution", "Inquisition", "Renaissance Italy", "Kinematics", "Mathematics", "Empiricism"],
    "frameworks": ["INNOVATION_AND_TECHNOLOGY", "CAUSE_AND_EFFECT", "DOCTRINE_DEVELOPMENT", "CULTURAL_DIFFUSION", "SCIENCE_AND_RELIGION"],
},

"albert-einstein": {
    "summary": "Albert Einstein (1879\u20131955) was a German-born theoretical physicist whose theories of special relativity (1905), general relativity (1915), and mass-energy equivalence (E=mc\u00b2) fundamentally reconceived space, time, gravity, and energy \u2014 making him the most influential physicist since Newton and arguably the most recognized scientist in human history. Born in Ulm, Germany, to a middle-class Jewish family, he showed early mathematical brilliance but struggled with the rigid German education system. While working as a patent clerk in Bern, Switzerland, he published four revolutionary papers in his annus mirabilis (1905): on the photoelectric effect (establishing the quantum nature of light, earning the 1921 Nobel Prize), Brownian motion (confirming atomic theory), special relativity (demolishing absolute space and time), and mass-energy equivalence. His general theory of relativity (1915) reimagined gravity not as a force but as the curvature of spacetime caused by mass \u2014 confirmed by Arthur Eddington\u2019s solar eclipse observations (1919), which made Einstein a global celebrity overnight. Fleeing Nazi Germany in 1933, he accepted a position at Princeton\u2019s Institute for Advanced Study. His 1939 letter to President Roosevelt warning of the possibility of atomic weapons helped launch the Manhattan Project, though Einstein himself played no role in building the bomb and later became a passionate advocate for nuclear disarmament and world government. His mass-energy equation underpins both nuclear energy and nuclear weapons. He spent his final decades pursuing a unified field theory \u2014 a quest unfulfilled but prophetically anticipating modern string theory and quantum gravity research. TIME magazine named him \u2018Person of the Century\u2019 (1999).",
    "died": "1955 CE, Princeton",
    "period": "1879\u20131955",
    "wikidataQid": "Q937",
    "wikipediaUrl": "https://en.wikipedia.org/wiki/Albert_Einstein",
    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Albert_Einstein_Head.jpg",
    "causes": [
        "Maxwell\u2019s electromagnetic theory and the failure of the Michelson-Morley experiment to detect the luminiferous aether created the crisis that special relativity resolved",
        "The quantum revolution initiated by Planck\u2019s radiation law (1900) set the stage for Einstein\u2019s photoelectric effect paper",
        "The Swiss patent office gave Einstein time for independent thought free from academic pressure, enabling his 1905 annus mirabilis"
    ],
    "effects": [
        "Special and general relativity replaced Newtonian mechanics as the framework for understanding space, time, and gravity",
        "E=mc\u00b2 revealed the equivalence of mass and energy, underpinning nuclear power and nuclear weapons",
        "His 1939 letter to Roosevelt contributed to the Manhattan Project, ushering in the atomic age",
        "The photoelectric effect paper established quantum mechanics and earned the 1921 Nobel Prize in Physics",
        "General relativity predicted gravitational lensing, black holes, and gravitational waves \u2014 all confirmed experimentally",
        "Named TIME Person of the Century (1999); \u2018Einstein\u2019 became synonymous with genius itself"
    ],
    "relationships": [
        rel("albert-einstein", "Albert Einstein", "BUILDS_ON", "isaac-newton", "Relativity superseded Newtonian mechanics while preserving it as a limiting case at low velocities"),
        rel("albert-einstein", "Albert Einstein", "INFLUENCES", "manhattan-project", "His 1939 letter to Roosevelt warning about atomic weapons helped initiate the Manhattan Project"),
        rel("albert-einstein", "Albert Einstein", "CONTEMPORARY_OF", "nikola-tesla", "Both revolutionized physics and technology in the early 20th century"),
        rel("albert-einstein", "Albert Einstein", "OCCURS_IN", "princeton", "Worked at the Institute for Advanced Study in Princeton from 1933 until his death (1955)"),
        rel("albert-einstein", "Albert Einstein", "FLEES", "nazi-germany", "Fled Germany in 1933 after the Nazi rise to power, renouncing his German citizenship"),
        rel("albert-einstein", "Albert Einstein", "AWARDED", "nobel-prize-physics", "Received the 1921 Nobel Prize in Physics for the photoelectric effect, not relativity"),
    ],
    "subjectHeadings": ["People \u2014 Scientists & Physicists \u2014 Germany/USA \u2014 Modern"],
    "subjects": ["Relativity", "E=mc\u00b2", "Quantum Mechanics", "Physics", "Nobel Prize", "Nuclear Energy", "Spacetime", "Gravity", "Princeton", "Photoelectric Effect"],
    "frameworks": ["INNOVATION_AND_TECHNOLOGY", "CAUSE_AND_EFFECT", "CULTURAL_DIFFUSION", "SCIENCE_AND_RELIGION", "ETHICAL_FRAMEWORK"],
},

"ashoka": {
    "summary": "Ashoka Maurya (c. 304\u2013232 BCE) was the third emperor of the Maurya Dynasty and ruler of the largest empire in Indian history \u2014 stretching from Afghanistan to Bangladesh. His transformation from a ruthless conqueror to a champion of non-violence and dharma after the devastating Kalinga War (c. 261 BCE) represents one of the most dramatic moral conversions in recorded history. Ashoka conquered Kalinga (modern Odisha) at a cost of 100,000 dead, 150,000 deported, and countless more destroyed \u2014 then, horrified by the carnage he had caused, embraced Buddhism and devoted the remaining 30 years of his reign to dhamma (righteousness). He erected the Edicts of Ashoka \u2014 over 30 rock and pillar inscriptions across the subcontinent, the oldest deciphered original texts of India \u2014 proclaiming religious tolerance, non-violence (ahimsa), vegetarianism, animal welfare, free hospitals, road-building, and care for the poor. He sent Buddhist missionaries to Sri Lanka (where his son Mahinda established Theravada Buddhism), Central Asia, Egypt, and Greece \u2014 the first systematic international missionary effort in history. His four-lion capital at Sarnath became the national emblem of India, and the Ashoka Chakra adorns the Indian flag. H.G. Wells wrote that \u2018amidst the tens of thousands of names of monarchs that crowd the columns of history, the name of Ashoka shines, and shines almost alone, a star.\u2019",
    "died": "c. 232 BCE",
    "period": "c. 304\u2013232 BCE",
    "wikidataQid": "Q731",
    "wikipediaUrl": "https://en.wikipedia.org/wiki/Ashoka",
    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Ashoka%27s_visit_to_the_Ramagrama_stupa_Sanchi_Stupa_1_Southern_gateway.jpg",
    "causes": [
        "The Maurya Empire\u2019s military expansion under Chandragupta and Bindusara created the territorial base that Ashoka inherited",
        "The catastrophic Kalinga War (c. 261 BCE) \u2014 100,000 killed \u2014 caused Ashoka\u2019s moral crisis and conversion to Buddhism",
        "Buddhist teachings on suffering, non-violence, and compassion provided the ethical framework for Ashoka\u2019s transformed governance"
    ],
    "effects": [
        "Transformed Buddhism from a regional Indian sect into an international religion through systematic missionary expeditions to Sri Lanka, Central Asia, and the Mediterranean",
        "The Edicts of Ashoka established the first documented human rights and animal welfare policies in world history",
        "His four-lion capital became India\u2019s national emblem; the Ashoka Chakra appears on the Indian flag",
        "Established free hospitals, veterinary clinics, and rest houses along major roads \u2014 the first state welfare system in recorded history",
        "His model of dharmic governance influenced subsequent Indian rulers and inspired modern figures including Mahatma Gandhi",
        "The Edicts are the oldest deciphered original texts of India, providing crucial historical evidence for the Maurya period"
    ],
    "relationships": [
        rel("ashoka", "Ashoka", "INFLUENCED_BY", "buddha", "Converted to Buddhism after the Kalinga War, becoming its greatest royal patron"),
        rel("ashoka", "Ashoka", "RULES", "maurya-empire", "Third emperor of the Maurya Dynasty, ruling the largest empire in Indian history"),
        rel("ashoka", "Ashoka", "OCCURS_IN", "ancient-india", "Ruled from Pataliputra over an empire spanning most of the Indian subcontinent"),
        rel("ashoka", "Ashoka", "INFLUENCES", "mahatma-gandhi", "Gandhi\u2019s philosophy of ahimsa (non-violence) drew on Ashoka\u2019s model of dharmic governance"),
        rel("ashoka", "Ashoka", "ESTABLISHES", "buddhist-missions", "Sent the first international Buddhist missionaries to Sri Lanka, Central Asia, Egypt, and Greece"),
    ],
    "subjectHeadings": ["People \u2014 Emperors & Rulers \u2014 India \u2014 Classical"],
    "subjects": ["Maurya Empire", "Buddhism", "Ahimsa", "Kalinga War", "Edicts of Ashoka", "Dharma", "Ancient India", "Non-Violence", "Missionary", "Welfare State"],
    "frameworks": ["POLITICAL_SYSTEMS", "CAUSE_AND_EFFECT", "DOCTRINE_DEVELOPMENT", "ETHICAL_FRAMEWORK", "CULTURAL_DIFFUSION"],
},

"nelson-mandela": {
    "summary": "Nelson Rolihlahla Mandela (1918\u20132013) was a South African anti-apartheid revolutionary, political prisoner, and statesman who served as South Africa\u2019s first Black president (1994\u20131999) \u2014 transforming a nation on the brink of racial civil war into a multiracial democracy through an unprecedented act of reconciliation. Born to the Thembu royal family in Mvezo, Eastern Cape, he studied law at the University of the Witwatersrand and joined the African National Congress (ANC) in 1944. As leader of the ANC\u2019s armed wing Umkhonto we Sizwe (\u2018Spear of the Nation\u2019), he organized sabotage campaigns against the apartheid regime. Arrested in 1962 and sentenced to life imprisonment at the Rivonia Trial (1964), he spent 27 years in prison \u2014 18 of them on Robben Island \u2014 yet emerged without bitterness, famously declaring: \u2018As I walked out the door toward the gate that would lead to my freedom, I knew if I didn\u2019t leave my bitterness and hatred behind, I\u2019d still be in prison.\u2019 Released on February 11, 1990 (watched by 600 million people worldwide), he negotiated with President F.W. de Klerk to dismantle apartheid, sharing the 1993 Nobel Peace Prize. As president, he established the Truth and Reconciliation Commission under Desmond Tutu \u2014 a revolutionary model of restorative justice that has since been adopted in over 40 countries. He wore the Springbok jersey at the 1995 Rugby World Cup, unifying a divided nation through sport. His Long Walk to Freedom became one of the most widely read autobiographies in history. He remains the world\u2019s most celebrated symbol of resistance to oppression and the power of forgiveness.",
    "died": "2013 CE, Johannesburg",
    "period": "1918\u20132013",
    "wikidataQid": "Q8023",
    "wikipediaUrl": "https://en.wikipedia.org/wiki/Nelson_Mandela",
    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/0/02/Nelson_Mandela_1994.jpg",
    "causes": [
        "The apartheid system (1948\u20131994) of racial segregation and white minority rule in South Africa created the conditions for resistance and revolution",
        "The Sharpeville massacre (1960) and banning of the ANC radicalized the movement toward armed resistance under Mandela\u2019s leadership",
        "International sanctions, divestment campaigns, and Cold War dynamics pressured the apartheid regime toward negotiation"
    ],
    "effects": [
        "Negotiated the peaceful end of apartheid (1990\u20131994), averting the widely predicted racial civil war in South Africa",
        "Became South Africa\u2019s first Black president (1994), establishing multiracial democracy through free elections",
        "The Truth and Reconciliation Commission pioneered restorative justice, adopted by over 40 countries since",
        "His 27-year imprisonment and subsequent forgiveness became the defining modern narrative of moral leadership and reconciliation",
        "Inspired global anti-apartheid solidarity and human rights movements, earning the 1993 Nobel Peace Prize",
        "South Africa\u2019s constitution (1996), shaped by his vision, is considered one of the most progressive in the world"
    ],
    "relationships": [
        rel("nelson-mandela", "Nelson Mandela", "OPPOSES", "apartheid", "Led the armed and political struggle against South Africa\u2019s apartheid regime for 50 years"),
        rel("nelson-mandela", "Nelson Mandela", "INFLUENCED_BY", "mahatma-gandhi", "Gandhi\u2019s early activism in South Africa (1893\u20131914) and non-violent philosophy influenced Mandela\u2019s trajectory"),
        rel("nelson-mandela", "Nelson Mandela", "INFLUENCED_BY", "martin-luther-king-jr", "King\u2019s civil rights movement and philosophy of non-violent resistance inspired Mandela\u2019s approach"),
        rel("nelson-mandela", "Nelson Mandela", "OCCURS_IN", "south-africa", "Born, imprisoned, and served as president of South Africa"),
        rel("nelson-mandela", "Nelson Mandela", "ESTABLISHES", "truth-and-reconciliation-commission", "Created the TRC (1996) as a restorative justice model for post-apartheid healing"),
        rel("nelson-mandela", "Nelson Mandela", "AWARDED", "nobel-peace-prize", "Shared the 1993 Nobel Peace Prize with F.W. de Klerk for negotiating the end of apartheid"),
    ],
    "subjectHeadings": ["People \u2014 Political Leaders \u2014 South Africa \u2014 Contemporary"],
    "subjects": ["Apartheid", "South Africa", "Human Rights", "Reconciliation", "ANC", "Robben Island", "Truth Commission", "Nobel Peace Prize", "Freedom", "Democracy"],
    "frameworks": ["POLITICAL_SYSTEMS", "CAUSE_AND_EFFECT", "ETHICAL_FRAMEWORK", "SOCIAL_STRUCTURES", "CULTURAL_DIFFUSION"],
},

"nikola-tesla": {
    "summary": "Nikola Tesla (1856\u20131943) was a Serbian-American inventor, electrical engineer, and futurist whose development of the alternating current (AC) polyphase power system, induction motor, and Tesla coil electrified the modern world and won the \u2018War of Currents\u2019 against Thomas Edison\u2019s direct current (DC) \u2014 one of the most consequential technological victories in history. Born in Smiljan, Austrian Empire (modern Croatia), to a Serbian Orthodox priest, Tesla experienced vivid visions and eidetic memory, claiming he could design entire machines in his mind before building them. After studying engineering in Graz and working for Continental Edison in Paris, he emigrated to the United States in 1884 with four cents in his pocket and a letter of introduction to Edison. Their partnership quickly soured over the AC vs. DC dispute. Tesla allied with George Westinghouse, and their AC system\u2019s triumph at the 1893 World\u2019s Columbian Exposition in Chicago and the Niagara Falls power station (1896) established AC as the global standard for electricity transmission. He held over 300 patents spanning radio (U.S. Supreme Court recognized his priority over Marconi in 1943), X-ray imaging, remote control, neon lighting, the rotating magnetic field, and early wireless communication. His Wardenclyffe Tower project envisioned worldwide wireless energy transmission \u2014 a concept decades ahead of its time. Despite his genius, he died nearly penniless in room 3327 of the New Yorker Hotel. The SI unit of magnetic flux density (tesla) bears his name, and TIME named him among the 100 most influential people of the 20th century. Elon Musk named Tesla, Inc. in his honor.",
    "died": "1943 CE, New York City",
    "period": "1856\u20131943",
    "wikidataQid": "Q9036",
    "wikipediaUrl": "https://en.wikipedia.org/wiki/Nikola_Tesla",
    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/7/79/Tesla_circa_1890.jpeg",
    "causes": [
        "The Second Industrial Revolution\u2019s demand for efficient long-distance electrical power transmission created the problem that AC solved",
        "Edison\u2019s DC system\u2019s limitation to short-distance transmission (within 1 mile of generating stations) created the opening for Tesla\u2019s superior AC technology",
        "Tesla\u2019s eidetic memory and ability to visualize complete machines mentally enabled his prolific invention rate"
    ],
    "effects": [
        "The AC polyphase power system became the global standard for electricity generation and transmission, electrifying the modern world",
        "Won the War of Currents against Edison\u2019s DC system, enabling long-distance power transmission that made modern cities possible",
        "Invented or laid groundwork for radio, remote control, X-ray imaging, neon lighting, and wireless communication",
        "The Niagara Falls hydroelectric power station (1896) demonstrated AC\u2019s viability and became the model for all subsequent power plants",
        "His 300+ patents across multiple fields made him one of the most prolific inventors in history",
        "The SI unit tesla (T) for magnetic flux density immortalizes his contribution to electromagnetism"
    ],
    "relationships": [
        rel("nikola-tesla", "Nikola Tesla", "OPPOSES", "thomas-edison", "The War of Currents: Tesla\u2019s AC system defeated Edison\u2019s DC system as the global electrical standard"),
        rel("nikola-tesla", "Nikola Tesla", "ALLIED_WITH", "george-westinghouse", "Westinghouse licensed Tesla\u2019s AC patents and funded the system that electrified America"),
        rel("nikola-tesla", "Nikola Tesla", "INFLUENCES", "alternating-current", "Developed the complete AC polyphase power system including generators, transformers, and motors"),
        rel("nikola-tesla", "Nikola Tesla", "OCCURS_IN", "united-states", "Immigrated to the US in 1884 and worked primarily in New York City"),
        rel("nikola-tesla", "Nikola Tesla", "INVENTS", "tesla-coil", "Invented the Tesla coil (1891), a resonant transformer circuit used in radio technology and scientific research"),
        rel("nikola-tesla", "Nikola Tesla", "CONTEMPORARY_OF", "albert-einstein", "Both transformed physics and technology in the early 20th century"),
    ],
    "subjectHeadings": ["People \u2014 Scientists & Inventors \u2014 Serbia/USA \u2014 Modern"],
    "subjects": ["Alternating Current", "Electricity", "War of Currents", "Invention", "Radio", "Tesla Coil", "Wireless", "Engineering", "Patents", "Electromagnetism"],
    "frameworks": ["INNOVATION_AND_TECHNOLOGY", "CAUSE_AND_EFFECT", "TRADE_AND_EXCHANGE", "CULTURAL_DIFFUSION", "SOCIAL_STRUCTURES"],
},

"winston-churchill": {
    "summary": "Sir Winston Leonard Spencer Churchill (1874\u20131965) was a British statesman, military officer, and author who served as Prime Minister of the United Kingdom during World War II (1940\u20131945) and again from 1951\u20131955 \u2014 widely regarded as the greatest wartime leader of the 20th century and the man who rallied the free world against Nazi tyranny when Britain stood alone. Born at Blenheim Palace to a politically prominent family, he served as a cavalry officer in India, Sudan, and South Africa (where he was captured and escaped during the Boer War, becoming a national hero). His political career spanned six decades: First Lord of the Admiralty (twice), Chancellor of the Exchequer, Home Secretary, and multiple cabinet positions. After a \u2018wilderness years\u2019 decade (1929\u20131939) warning against appeasing Hitler when few would listen, he became Prime Minister on May 10, 1940 \u2014 the day Germany invaded France. His wartime speeches (\u2018We shall fight on the beaches,\u2019 \u2018Their finest hour,\u2019 \u2018Never in the field of human conflict was so much owed by so many to so few\u2019) are among the most powerful oratory in the English language and sustained British morale during the Blitz, the Battle of Britain, and the darkest days of the war. He forged the Anglo-American alliance with Roosevelt, navigated the complex partnership with Stalin, and helped plan D-Day and the defeat of Nazi Germany. He coined the term \u2018Iron Curtain\u2019 in his Fulton speech (1946), defining the Cold War. He won the Nobel Prize in Literature (1953) for his six-volume The Second World War and A History of the English-Speaking Peoples. In a 2002 BBC poll, Britons voted him the Greatest Briton of all time.",
    "died": "1965 CE, London",
    "period": "1874\u20131965",
    "wikidataQid": "Q8016",
    "wikipediaUrl": "https://en.wikipedia.org/wiki/Winston_Churchill",
    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/b/bc/Sir_Winston_Churchill_-_19086236948.jpg",
    "causes": [
        "Neville Chamberlain\u2019s failed appeasement policy and the fall of Norway (1940) discredited the government and brought Churchill to power",
        "Churchill\u2019s decade of warnings against Nazi Germany (1929\u20131939) during his \u2018wilderness years\u2019 gave him unique credibility when war came",
        "Britain\u2019s imperial tradition of global leadership and naval power provided the institutional foundation for Churchill\u2019s wartime strategy"
    ],
    "effects": [
        "His wartime leadership sustained British resistance when the country stood alone against Nazi Germany (June 1940 \u2013 June 1941)",
        "Forged the Anglo-American \u2018Special Relationship\u2019 with Roosevelt that became the cornerstone of Western alliance strategy",
        "His \u2018Iron Curtain\u2019 speech (1946) defined the Cold War framework that shaped global politics for 45 years",
        "Won the Nobel Prize in Literature (1953), the only wartime PM to receive a major literary award",
        "His speeches set the gold standard for political oratory and crisis leadership communication",
        "Voted Greatest Briton (BBC 2002) and ranked among the most influential leaders in world history"
    ],
    "relationships": [
        rel("winston-churchill", "Winston Churchill", "OPPOSES", "nazi-germany", "Led Britain\u2019s resistance against Nazi Germany throughout World War II (1940\u20131945)"),
        rel("winston-churchill", "Winston Churchill", "ALLIED_WITH", "franklin-d-roosevelt", "Forged the Anglo-American alliance that became the foundation of the Allied war effort"),
        rel("winston-churchill", "Winston Churchill", "OCCURS_IN", "united-kingdom", "Served as British Prime Minister (1940\u20131945, 1951\u20131955) and Member of Parliament for 64 years"),
        rel("winston-churchill", "Winston Churchill", "SHAPES", "world-war-ii", "His leadership during WWII was decisive in the Allied victory over Nazi Germany"),
        rel("winston-churchill", "Winston Churchill", "DEFINES", "cold-war", "His \u2018Iron Curtain\u2019 speech at Fulton, Missouri (1946) defined the emerging Cold War"),
        rel("winston-churchill", "Winston Churchill", "AWARDED", "nobel-prize-literature", "Won the 1953 Nobel Prize in Literature for his historical and biographical works"),
    ],
    "subjectHeadings": ["People \u2014 Political Leaders \u2014 United Kingdom \u2014 Modern"],
    "subjects": ["World War II", "Battle of Britain", "Iron Curtain", "Cold War", "Oratory", "Nobel Prize", "British Empire", "D-Day", "Leadership", "United Kingdom"],
    "frameworks": ["POLITICAL_SYSTEMS", "CAUSE_AND_EFFECT", "MILITARY_HISTORY", "CULTURAL_DIFFUSION", "ETHICAL_FRAMEWORK"],
},

"abraham-lincoln": {
    "summary": "Abraham Lincoln (1809\u20131865) was the 16th President of the United States (1861\u20131865) who preserved the Union during the American Civil War, abolished slavery through the Emancipation Proclamation (1863) and the Thirteenth Amendment (1865), and redefined American democracy with the Gettysburg Address \u2014 making him, by scholarly consensus, the greatest American president. Born in a one-room log cabin in Kentucky, largely self-educated, he rose from rail-splitter to frontier lawyer to Illinois state legislator to U.S. congressman. His debates with Stephen Douglas (1858) over the expansion of slavery made him a national figure, and his election as the first Republican president (November 1860) triggered the secession of eleven Southern states and the formation of the Confederacy. He navigated the bloodiest conflict in American history (750,000 dead) with a combination of moral clarity, political cunning, and rhetorical genius. The Emancipation Proclamation (January 1, 1863) transformed the war from a struggle to preserve the Union into a crusade to end human bondage, freeing 3.5 million enslaved people and authorizing Black military service. His Gettysburg Address (November 19, 1863) \u2014 272 words delivered in under three minutes \u2014 remains the most quoted speech in American history, redefining the nation as \u2018conceived in liberty, and dedicated to the proposition that all men are created equal.\u2019 Assassinated by John Wilkes Booth at Ford\u2019s Theatre on April 14, 1865, five days after Lee\u2019s surrender, he became America\u2019s first martyred president. The Lincoln Memorial in Washington, D.C. stands as the republic\u2019s most sacred civic shrine.",
    "died": "1865 CE, Washington, D.C. (assassination)",
    "period": "1809\u20131865",
    "wikidataQid": "Q91",
    "wikipediaUrl": "https://en.wikipedia.org/wiki/Abraham_Lincoln",
    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/a/ab/Abraham_Lincoln_O-77_matte_collodion_print.jpg",
    "causes": [
        "The deepening sectional crisis over slavery\u2019s expansion (Missouri Compromise, Kansas-Nebraska Act, Dred Scott) polarized American politics",
        "Lincoln\u2019s moral conviction that slavery was wrong and his political skill in articulating this position won him the 1860 Republican nomination",
        "Southern secession after his election created the constitutional crisis that only civil war could resolve"
    ],
    "effects": [
        "Preserved the American Union by winning the Civil War (1861\u20131865), the bloodiest conflict in American history (750,000 dead)",
        "The Emancipation Proclamation (1863) and Thirteenth Amendment (1865) abolished slavery, freeing 4 million enslaved people",
        "The Gettysburg Address redefined American democracy as a commitment to equality, not merely constitutional union",
        "His assassination (April 14, 1865) made him America\u2019s first martyred president, elevating him to secular sainthood",
        "Established the precedent that the federal government could override state sovereignty on fundamental human rights",
        "Inspired subsequent civil rights leaders: Frederick Douglass, Martin Luther King Jr., and Barack Obama all invoked his legacy"
    ],
    "relationships": [
        rel("abraham-lincoln", "Abraham Lincoln", "PRESERVES", "united-states", "Preserved the American Union by winning the Civil War (1861\u20131865)"),
        rel("abraham-lincoln", "Abraham Lincoln", "ABOLISHES", "american-slavery", "Issued the Emancipation Proclamation (1863) and championed the Thirteenth Amendment"),
        rel("abraham-lincoln", "Abraham Lincoln", "OCCURS_IN", "american-civil-war", "Led the Union war effort as Commander-in-Chief throughout the Civil War"),
        rel("abraham-lincoln", "Abraham Lincoln", "INFLUENCES", "martin-luther-king-jr", "King delivered his \u2018I Have a Dream\u2019 speech at the Lincoln Memorial, explicitly invoking Lincoln\u2019s legacy"),
        rel("abraham-lincoln", "Abraham Lincoln", "PRECEDED_BY", "george-washington", "Washington founded the republic; Lincoln preserved it through its greatest crisis"),
        rel("abraham-lincoln", "Abraham Lincoln", "DELIVERS", "gettysburg-address", "The Gettysburg Address (1863) redefined American democracy in 272 words"),
    ],
    "subjectHeadings": ["People \u2014 Presidents & Political Leaders \u2014 USA \u2014 Modern"],
    "subjects": ["American Civil War", "Emancipation", "Slavery", "Gettysburg Address", "Union", "Republican Party", "Assassination", "Democracy", "United States", "Civil Rights"],
    "frameworks": ["POLITICAL_SYSTEMS", "CAUSE_AND_EFFECT", "ETHICAL_FRAMEWORK", "MILITARY_HISTORY", "SOCIAL_STRUCTURES"],
},

"george-washington": {
    "summary": "George Washington (1732\u20131799) was the Commander-in-Chief of the Continental Army during the American Revolution (1775\u20131783), president of the Constitutional Convention (1787), and first President of the United States (1789\u20131797) \u2014 the indispensable figure in the creation of the American republic. Born into Virginia\u2019s planter aristocracy, he gained military experience in the French and Indian War, where his Virginia Regiment\u2019s frontier service taught him both the limitations of colonial warfare and the value of guerrilla tactics. Appointed commander of the ragtag Continental Army in 1775, he held a nearly impossible position together through six brutal winters, devastating retreats, near-mutinies, and the freezing encampment at Valley Forge (1777\u201378). His strategic brilliance at Trenton (1776) and Yorktown (1781) \u2014 the latter with decisive French support \u2014 won American independence. His greatest act was not military but political: voluntarily relinquishing power twice. After the war, he returned to Mount Vernon rather than seize the dictatorship his popularity could have supported. After presiding over the Constitutional Convention, he served two presidential terms establishing precedents (the cabinet system, two-term limit, presidential address) that defined the office, then retired again \u2014 King George III reportedly called this the act of \u2018the greatest man in the world.\u2019 His Farewell Address (1796) warned against foreign entanglements and political factions. He freed his slaves in his will (the only slave-owning Founding Father to do so). Henry Lee\u2019s eulogy \u2014 \u2018First in war, first in peace, and first in the hearts of his countrymen\u2019 \u2014 remains the definitive tribute.",
    "died": "1799 CE, Mount Vernon",
    "period": "1732\u20131799",
    "wikidataQid": "Q23",
    "wikipediaUrl": "https://en.wikipedia.org/wiki/George_Washington",
    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/b/b6/Gilbert_Stuart_Williamstown_Portrait_of_George_Washington.jpg",
    "causes": [
        "British taxation without representation (Stamp Act, Townshend Acts, Tea Act) and colonial resistance created the conditions for revolution",
        "Enlightenment political philosophy (Locke, Montesquieu) provided the intellectual framework for self-governance that Washington embodied",
        "Washington\u2019s military reputation, unifying personal authority, and Virginia planter-class status made him the only figure capable of commanding colonial unity"
    ],
    "effects": [
        "Won American independence by defeating the British Empire\u2019s forces during the Revolutionary War (1775\u20131783)",
        "Voluntarily relinquished power twice, establishing the precedent of civilian control and peaceful transfer of power that defines American democracy",
        "As Constitutional Convention president, his prestige enabled ratification of the Constitution \u2014 the world\u2019s oldest active written constitution",
        "Established presidential precedents (cabinet, two-term tradition, inaugural address) that shaped the office for 230+ years",
        "His Farewell Address warning against factions and foreign alliances became a foundational American policy document",
        "The capital city (Washington, D.C.), one state, 31 counties, and countless institutions bear his name"
    ],
    "relationships": [
        rel("george-washington", "George Washington", "LEADS", "american-revolution", "Commanded the Continental Army to victory in the American Revolutionary War (1775\u20131783)"),
        rel("george-washington", "George Washington", "ESTABLISHES", "american-presidency", "First President of the United States (1789\u20131797), defining the office\u2019s precedents"),
        rel("george-washington", "George Washington", "PRESIDES", "constitutional-convention", "Presided over the Constitutional Convention (1787), lending his authority to the new Constitution"),
        rel("george-washington", "George Washington", "OCCURS_IN", "united-states", "Born in Virginia, led the Revolution, and served as president in Philadelphia and New York"),
        rel("george-washington", "George Washington", "CONTEMPORARY_OF", "thomas-jefferson", "Jefferson drafted the Declaration; Washington won the war and established the government it envisioned"),
        rel("george-washington", "George Washington", "SUCCEEDED_BY", "abraham-lincoln", "Washington founded the republic; Lincoln preserved it through the Civil War 65 years later"),
    ],
    "subjectHeadings": ["People \u2014 Presidents & Military Leaders \u2014 USA \u2014 Early Modern"],
    "subjects": ["American Revolution", "Constitution", "Presidency", "Continental Army", "Mount Vernon", "Founding Fathers", "Independence", "Democracy", "Virginia", "United States"],
    "frameworks": ["POLITICAL_SYSTEMS", "CAUSE_AND_EFFECT", "MILITARY_HISTORY", "ETHICAL_FRAMEWORK", "SOCIAL_STRUCTURES"],
},

"charlemagne": {
    "summary": "Charlemagne (Charles the Great, c. 747\u2013814 CE) was the King of the Franks (768), King of the Lombards (774), and Emperor of the Romans (800) \u2014 the first recognized emperor in Western Europe since the fall of Rome in 476 CE. His coronation by Pope Leo III on Christmas Day 800 CE in St. Peter\u2019s Basilica created the political entity that became the Holy Roman Empire and established the medieval template for the relationship between Church and State. Through 53 military campaigns, he united most of Western Europe under a single ruler for the first time since the Roman Empire: his realm encompassed modern France, Germany, the Low Countries, Switzerland, Austria, northern Italy, and northern Spain. His forced conversion of the pagan Saxons (thirty years of brutal conquest, 772\u2013804 CE) remains controversial \u2014 the massacre of 4,500 Saxon prisoners at Verden (782) being the darkest episode. Yet his Carolingian Renaissance revived learning, literacy, and the arts: he established palace schools under Alcuin of York, standardized Carolingian minuscule (the script that evolved into modern lowercase letters), mandated education for clergy, preserved classical texts in monastic scriptoria, and reformed weights, measures, and coinage across his empire. His administrative innovations \u2014 the missi dominici (traveling inspectors), county governance, and oath-based loyalty \u2014 became the foundation of medieval feudalism. Charlemagne is the common ancestor of virtually every European royal family and most Europeans of European descent. Napoleon called himself \u2018the Charlemagne of the modern era,\u2019 and the Charlemagne Prize (Karlspreis) remains Europe\u2019s most prestigious award for contributions to European unity.",
    "died": "814 CE, Aachen",
    "period": "c. 747\u2013814 CE",
    "wikidataQid": "Q3044",
    "wikipediaUrl": "https://en.wikipedia.org/wiki/Charlemagne",
    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/a/a3/Charlemagne-by-Durer.jpg",
    "causes": [
        "The vacuum of power in Western Europe after Rome\u2019s fall (476 CE) and the Merovingian decline created the opportunity for Carolingian ascendancy",
        "The Frankish-Papal alliance (Pepin\u2019s donation and protection of the Pope) provided mutual legitimacy and strategic cooperation",
        "The Islamic expansion into Iberia and the Avar/Saxon threats on the eastern frontier created urgent military imperatives for centralized Christian rule"
    ],
    "effects": [
        "United most of Western Europe under one ruler for the first time since Rome, creating the political foundation of medieval Christendom",
        "His coronation as Emperor (800 CE) established the concept of a Western Christian Empire separate from Byzantium",
        "The Carolingian Renaissance preserved classical learning through monastic scriptoria and palace schools",
        "Carolingian minuscule became the basis for modern lowercase letters in the Latin alphabet",
        "His administrative system (counties, missi dominici, oath-based loyalty) created the template for medieval feudalism",
        "The Treaty of Verdun (843) dividing his empire among grandsons created the political map of modern France, Germany, and Italy"
    ],
    "relationships": [
        rel("charlemagne", "Charlemagne", "CROWNED_BY", "papacy", "Pope Leo III crowned him Emperor of the Romans on Christmas Day 800 CE"),
        rel("charlemagne", "Charlemagne", "ESTABLISHES", "holy-roman-empire", "His coronation created the political entity that became the Holy Roman Empire"),
        rel("charlemagne", "Charlemagne", "OCCURS_IN", "frankish-empire", "Ruled the Frankish-Carolingian Empire from Aachen, his capital"),
        rel("charlemagne", "Charlemagne", "CONQUERS", "lombard-kingdom", "Conquered the Lombard Kingdom of Italy (774), adding it to Frankish territory"),
        rel("charlemagne", "Charlemagne", "REVIVES", "classical-learning", "The Carolingian Renaissance preserved classical texts and revived education across Western Europe"),
    ],
    "subjectHeadings": ["People \u2014 Emperors & Rulers \u2014 Francia \u2014 Medieval"],
    "subjects": ["Carolingian Empire", "Holy Roman Empire", "Medieval Europe", "Carolingian Renaissance", "Feudalism", "Papal Alliance", "Aachen", "Francia", "Christendom", "Education"],
    "frameworks": ["POLITICAL_SYSTEMS", "CAUSE_AND_EFFECT", "CULTURAL_DIFFUSION", "RELIGIOUS_INSTITUTIONS", "DOCTRINE_DEVELOPMENT"],
},

"saladin": {
    "summary": "Saladin (An-Nasir Salah ad-Din Yusuf ibn Ayyub, 1137\u20131193 CE) was a Kurdish Muslim sultan who founded the Ayyubid Dynasty, unified Egypt and Syria, and recaptured Jerusalem from the Crusaders in 1187 \u2014 becoming the most celebrated Muslim military leader of the medieval period and a byword for chivalry even among his Christian enemies. Born in Tikrit (modern Iraq) to a Kurdish military family serving the Zengid dynasty, he rose through the ranks in Egypt, where he overthrew the Fatimid Caliphate (1171) and established Sunni orthodoxy under Abbasid nominal authority. His strategic genius lay not merely in military conquest but in political unification: he spent over a decade assembling a coalition of Muslim territories from Egypt to Mesopotamia before turning against the Crusader states. The Battle of Hattin (July 4, 1187) \u2014 where he destroyed the combined Crusader army by cutting off their water supply \u2014 was one of the most decisive battles of the Middle Ages. He recaptured Jerusalem on October 2, 1187 (the anniversary of Muhammad\u2019s Night Journey), but unlike the Crusaders\u2019 massacre in 1099, he spared the civilian population \u2014 an act of mercy that stunned Christendom. His conduct during the Third Crusade (1189\u20131192) against Richard the Lionheart earned mutual respect: when Richard fell ill, Saladin sent his personal physician and fresh fruit. The treaty between them (1192) allowed Christian pilgrims access to Jerusalem while maintaining Muslim sovereignty. Dante placed Saladin among the virtuous pagans in Limbo (Inferno IV), and even the Crusader chronicles praised his honor, making him one of the rare figures revered equally by both sides of a religious conflict.",
    "died": "1193 CE, Damascus",
    "period": "1137\u20131193 CE",
    "wikidataQid": "Q182565",
    "wikipediaUrl": "https://en.wikipedia.org/wiki/Saladin",
    "imageUrl": "",
    "causes": [
        "The fragmentation of the Muslim Near East into rival dynasties and the failure of previous Muslim leaders to mount a unified response to the Crusades",
        "Nur ad-Din Zengi\u2019s call for jihad against the Crusaders and mentorship of Saladin\u2019s military career in Syria and Egypt",
        "The Crusader states\u2019 internal divisions and Reynald of Chatillon\u2019s provocations (caravan raids, threat to Mecca) provided the casus belli"
    ],
    "effects": [
        "Recaptured Jerusalem (1187) from the Crusaders after 88 years of Christian rule, transforming the geopolitics of the Near East",
        "His mercy toward Jerusalem\u2019s Christian population established a model of chivalric conduct admired across religious boundaries",
        "Founded the Ayyubid Dynasty, which ruled Egypt and Syria for 80 years and patronized Islamic scholarship and architecture",
        "Provoked the Third Crusade (1189\u20131192), drawing England\u2019s Richard I and France\u2019s Philip II to the Holy Land",
        "His unification of Egypt and Syria under Sunni authority restored Muslim military coherence in the Near East",
        "Became an enduring symbol of Muslim chivalry, invoked by leaders from Ottoman sultans to modern Arab nationalists"
    ],
    "relationships": [
        rel("saladin", "Saladin", "RECAPTURES", "jerusalem", "Recaptured Jerusalem from the Crusaders on October 2, 1187 after the Battle of Hattin"),
        rel("saladin", "Saladin", "OPPOSES", "richard-the-lionheart", "The Third Crusade: Saladin and Richard I fought to a diplomatic settlement (Treaty of Jaffa, 1192)"),
        rel("saladin", "Saladin", "ESTABLISHES", "ayyubid-dynasty", "Founded the Ayyubid Dynasty, ruling Egypt, Syria, Yemen, and the Hejaz"),
        rel("saladin", "Saladin", "OVERTHROWS", "fatimid-caliphate", "Ended the Fatimid Caliphate in Egypt (1171), restoring Sunni Islam under Abbasid authority"),
        rel("saladin", "Saladin", "INFLUENCED_BY", "muhammad", "Saladin\u2019s chivalry and compassion drew directly on the Prophet\u2019s example and Islamic ethics of warfare"),
    ],
    "subjectHeadings": ["People \u2014 Military & Political Leaders \u2014 Egypt/Syria \u2014 Medieval"],
    "subjects": ["Crusades", "Jerusalem", "Ayyubid Dynasty", "Battle of Hattin", "Chivalry", "Islamic History", "Egypt", "Syria", "Kurdistan", "Jihad"],
    "frameworks": ["MILITARY_HISTORY", "CAUSE_AND_EFFECT", "ETHICAL_FRAMEWORK", "POLITICAL_SYSTEMS", "CULTURAL_DIFFUSION"],
},

"mahatma-gandhi": {
    "summary": "Mohandas Karamchand Gandhi (1869\u20131948), known as Mahatma (\u2018Great Soul\u2019), was an Indian lawyer, anti-colonial nationalist, and political ethicist who led India\u2019s independence movement against British rule through non-violent civil disobedience (satyagraha) \u2014 a strategy that inspired civil rights and freedom movements worldwide. Born in Porbandar, Gujarat, to a merchant-caste family, he studied law in London and practiced in South Africa (1893\u20131914), where his encounters with racial discrimination transformed him from a timid barrister into a revolutionary. He developed satyagraha (\u2018truth-force\u2019) as a method of non-violent resistance, first against South African discrimination laws and then against British colonial rule in India. His campaigns \u2014 the Non-Cooperation Movement (1920\u201322), the Salt March (1930), and the Quit India Movement (1942) \u2014 mobilized millions of ordinary Indians through fasting, boycotts, and peaceful protest. The Salt March (March\u2013April 1930), a 240-mile walk to the sea to make salt in defiance of the British salt monopoly, became the most iconic act of civil disobedience in history. Gandhi\u2019s insistence on Hindu-Muslim unity, his campaigns against untouchability, and his vision of village self-sufficiency (swaraj) defined Indian nationalism not merely as political independence but as moral regeneration. Although he never held political office, his moral authority was decisive in negotiations leading to Indian independence (August 15, 1947). He was devastated by the partition of India and Pakistan and the resulting communal violence. On January 30, 1948, he was assassinated by Nathuram Godse, a Hindu nationalist. His philosophy of non-violent resistance directly influenced Martin Luther King Jr., Nelson Mandela, Cesar Chavez, and the Dalai Lama. The United Nations declared his birthday (October 2) the International Day of Non-Violence.",
    "died": "1948 CE, New Delhi (assassination)",
    "period": "1869\u20131948",
    "wikidataQid": "Q1001",
    "wikipediaUrl": "https://en.wikipedia.org/wiki/Mahatma_Gandhi",
    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Mahatma-Gandhi%2C_studio%2C_1931.jpg",
    "causes": [
        "British colonial exploitation of India (drain of wealth, de-industrialization, famines) created the material conditions for nationalist resistance",
        "Racial discrimination in South Africa (1893\u20131914) radicalized Gandhi and provided the laboratory for developing satyagraha",
        "Hindu, Jain, and Tolstoyan influences on non-violence (ahimsa) provided the ethical framework for Gandhi\u2019s unique political method"
    ],
    "effects": [
        "Led India to independence from British rule (August 15, 1947), ending 190 years of colonial domination",
        "Invented modern non-violent civil disobedience (satyagraha) as a practical method of political resistance adopted worldwide",
        "Directly inspired Martin Luther King Jr.\u2019s civil rights movement, Mandela\u2019s anti-apartheid struggle, and the Dalai Lama\u2019s Tibetan resistance",
        "The Salt March (1930) became the most iconic act of civil disobedience in history, demonstrating mass non-violent resistance\u2019s power",
        "His campaigns against untouchability helped transform Indian social attitudes toward caste discrimination",
        "October 2 (his birthday) is observed as the International Day of Non-Violence by the United Nations"
    ],
    "relationships": [
        rel("mahatma-gandhi", "Mahatma Gandhi", "LEADS", "indian-independence-movement", "Led India\u2019s independence movement through non-violent civil disobedience (1915\u20131947)"),
        rel("mahatma-gandhi", "Mahatma Gandhi", "INFLUENCES", "martin-luther-king-jr", "King studied Gandhi\u2019s methods and applied satyagraha to the American civil rights struggle"),
        rel("mahatma-gandhi", "Mahatma Gandhi", "INFLUENCES", "nelson-mandela", "Mandela acknowledged Gandhi\u2019s South African activism as a precursor to the anti-apartheid movement"),
        rel("mahatma-gandhi", "Mahatma Gandhi", "INFLUENCED_BY", "socrates", "Gandhi cited Socrates\u2019s acceptance of unjust punishment as a model for civil disobedience"),
        rel("mahatma-gandhi", "Mahatma Gandhi", "OCCURS_IN", "india", "Born in Gujarat, led independence movement across India, assassinated in New Delhi"),
        rel("mahatma-gandhi", "Mahatma Gandhi", "INFLUENCED_BY", "ashoka", "Gandhi\u2019s commitment to ahimsa drew on Ashoka\u2019s model of dharmic governance"),
    ],
    "subjectHeadings": ["People \u2014 Political Leaders \u2014 India \u2014 Modern"],
    "subjects": ["Non-Violence", "Satyagraha", "Indian Independence", "Civil Disobedience", "Salt March", "Ahimsa", "British Raj", "India", "Swaraj", "Peace"],
    "frameworks": ["POLITICAL_SYSTEMS", "CAUSE_AND_EFFECT", "ETHICAL_FRAMEWORK", "SOCIAL_STRUCTURES", "CULTURAL_DIFFUSION"],
},

"martin-luther-king-jr": {
    "summary": "Martin Luther King Jr. (1929\u20131968) was an American Baptist minister and activist who became the most visible leader of the American civil rights movement (1955\u20131968), whose philosophy of non-violent resistance, soaring oratory, and moral courage dismantled legal segregation in the United States and advanced the cause of racial equality worldwide. Born in Atlanta, Georgia, to a prominent Baptist family, he earned a doctorate in systematic theology from Boston University (1955) and became pastor of Dexter Avenue Baptist Church in Montgomery, Alabama. The Montgomery Bus Boycott (1955\u201356), triggered by Rosa Parks\u2019s refusal to surrender her seat, thrust the 26-year-old King into national leadership. Over the next decade, he led campaigns of non-violent resistance against segregation in Albany, Birmingham, Selma, and Chicago, was jailed 29 times, and survived multiple assassination attempts and a near-fatal stabbing. His \u2018Letter from Birmingham Jail\u2019 (1963) \u2014 one of the great documents of American moral philosophy \u2014 argued that injustice anywhere is a threat to justice everywhere. His \u2018I Have a Dream\u2019 speech at the March on Washington (August 28, 1963), delivered before 250,000 people at the Lincoln Memorial, is considered the greatest American speech of the 20th century. His leadership produced the Civil Rights Act (1964), which outlawed segregation, and the Voting Rights Act (1965), which guaranteed Black suffrage. He received the Nobel Peace Prize (1964) at age 35, the youngest recipient at that time. Assassinated in Memphis, Tennessee, on April 4, 1968, he became a martyr for human rights. The Martin Luther King Jr. Memorial on the National Mall and the federal holiday on the third Monday of January honor his legacy.",
    "died": "1968 CE, Memphis (assassination)",
    "period": "1929\u20131968",
    "wikidataQid": "Q8027",
    "wikipediaUrl": "https://en.wikipedia.org/wiki/Martin_Luther_King_Jr.",
    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/0/05/Martin_Luther_King%2C_Jr..jpg",
    "causes": [
        "Jim Crow segregation laws and systemic racial discrimination in the American South created intolerable conditions for Black Americans",
        "The Montgomery Bus Boycott (1955\u201356) thrust King into national leadership as the voice of non-violent resistance",
        "Gandhi\u2019s philosophy of satyagraha and the Black church tradition of prophetic preaching provided King\u2019s ethical and rhetorical framework"
    ],
    "effects": [
        "The Civil Rights Act (1964) outlawed segregation in public facilities, employment, and education across the United States",
        "The Voting Rights Act (1965) guaranteed Black suffrage, transforming American democracy and the political landscape of the South",
        "His \u2018I Have a Dream\u2019 speech became the defining statement of American racial justice and the most quoted speech of the 20th century",
        "His non-violent methodology inspired movements worldwide: anti-apartheid in South Africa, Solidarity in Poland, Tiananmen in China",
        "The federal Martin Luther King Jr. Day (third Monday of January) is the only American holiday honoring a private citizen",
        "His assassination galvanized passage of the Fair Housing Act (1968) and deepened America\u2019s ongoing reckoning with racism"
    ],
    "relationships": [
        rel("martin-luther-king-jr", "Martin Luther King Jr.", "INFLUENCED_BY", "mahatma-gandhi", "King studied Gandhi\u2019s satyagraha and applied non-violent resistance to the American civil rights struggle"),
        rel("martin-luther-king-jr", "Martin Luther King Jr.", "INFLUENCED_BY", "abraham-lincoln", "King delivered \u2018I Have a Dream\u2019 at the Lincoln Memorial, explicitly invoking the Emancipation Proclamation"),
        rel("martin-luther-king-jr", "Martin Luther King Jr.", "INFLUENCES", "nelson-mandela", "Mandela acknowledged King\u2019s non-violent philosophy as an influence on the anti-apartheid movement"),
        rel("martin-luther-king-jr", "Martin Luther King Jr.", "OCCURS_IN", "united-states", "Led the civil rights movement across the American South and nationally (1955\u20131968)"),
        rel("martin-luther-king-jr", "Martin Luther King Jr.", "LEADS", "civil-rights-movement", "Led the American civil rights movement from the Montgomery Bus Boycott to the Memphis sanitation strike"),
        rel("martin-luther-king-jr", "Martin Luther King Jr.", "AWARDED", "nobel-peace-prize", "Received the 1964 Nobel Peace Prize at age 35 for his non-violent civil rights leadership"),
    ],
    "subjectHeadings": ["People \u2014 Civil Rights Leaders \u2014 USA \u2014 Contemporary"],
    "subjects": ["Civil Rights", "Non-Violence", "Segregation", "I Have a Dream", "Birmingham", "Selma", "Voting Rights", "Montgomery", "Nobel Peace Prize", "United States"],
    "frameworks": ["POLITICAL_SYSTEMS", "CAUSE_AND_EFFECT", "ETHICAL_FRAMEWORK", "SOCIAL_STRUCTURES", "CULTURAL_DIFFUSION"],
},

"zoroaster": {
    "summary": "Zoroaster (Zarathustra, c. 1500\u20131000 BCE, possibly as early as 1700 BCE) was an ancient Iranian prophet and the founder of Zoroastrianism \u2014 the first major monotheistic (or dualistic) religion in history, whose concepts of heaven, hell, final judgment, angels, demons, a savior figure, and the cosmic struggle between good and evil profoundly influenced Judaism, Christianity, and Islam. Born in northeastern Iran (possibly Balkh or the Central Asian steppe), he received divine visions from Ahura Mazda (\u2018Wise Lord\u2019) and composed the Gathas \u2014 17 hymns forming the oldest part of the Avesta, Zoroastrianism\u2019s sacred scripture, and among the most ancient religious texts in any Indo-European language. Zoroaster radically reformed the existing Indo-Iranian polytheistic religion by elevating Ahura Mazda as the supreme deity locked in cosmic battle with Angra Mainyu (the Destructive Spirit), requiring each human to choose between asha (truth/righteousness) and druj (lie/chaos). This ethical dualism \u2014 the individual\u2019s free-will choice between good and evil with consequences in an afterlife \u2014 was revolutionary in its time. King Vishtaspa\u2019s conversion gave Zoroastrianism its first royal patron. Under the Achaemenid Empire (550\u2013330 BCE) of Cyrus the Great and Darius I, Zoroastrianism became the de facto state religion of the largest empire the world had yet seen. Its fire temples, priesthood (magi \u2014 whence \u2018magic\u2019), and ethical teachings spread from the Mediterranean to India. The religion\u2019s influence on the Abrahamic faiths is widely recognized by scholars: the Jewish concepts of angels, Satan, resurrection, and apocalyptic eschatology developed during and after the Babylonian exile (586\u2013538 BCE) under Persian rule, suggesting direct Zoroastrian influence. Today\u2019s Parsi community (primarily in Mumbai, India) and Iranian Zoroastrians preserve the faith of perhaps 100,000\u2013200,000 adherents.",
    "died": "c. 1000 BCE (traditional)",
    "period": "c. 1500\u20131000 BCE (traditional)",
    "wikidataQid": "Q42827",
    "wikipediaUrl": "https://en.wikipedia.org/wiki/Zoroaster",
    "imageUrl": "",
    "causes": [
        "The Indo-Iranian polytheistic religion\u2019s ritualism and moral ambiguity prompted Zoroaster\u2019s radical monotheistic reform",
        "Divine visions from Ahura Mazda commissioned Zoroaster to proclaim truth (asha) and combat the lie (druj)",
        "The pastoral nomadic society of the Central Asian steppe, with its stark contrasts between light and darkness, survival and destruction, shaped the dualistic worldview"
    ],
    "effects": [
        "Founded Zoroastrianism, the first major monotheistic/dualistic religion and the dominant faith of the Achaemenid, Parthian, and Sasanian empires",
        "Introduced concepts of heaven, hell, final judgment, resurrection, angels, and demons that directly influenced Judaism, Christianity, and Islam",
        "The ethical dualism (good vs. evil, truth vs. lie) established the moral framework that permeates Western religious thought",
        "The Achaemenid Empire\u2019s adoption of Zoroastrian tolerance influenced Cyrus the Great\u2019s policy of religious freedom (Cyrus Cylinder)",
        "The Magi priesthood gave the English language the word \u2018magic\u2019 and features in the Christian nativity narrative (the Three Wise Men)",
        "Influenced Manichaeism, Gnosticism, and Baha\u2019i Faith, making Zoroaster\u2019s ideas foundational to multiple world religions"
    ],
    "relationships": [
        rel("zoroaster", "Zoroaster", "ESTABLISHES", "zoroastrianism", "Founded Zoroastrianism, the world\u2019s first major monotheistic/dualistic religion"),
        rel("zoroaster", "Zoroaster", "INFLUENCES", "cyrus-the-great", "Cyrus the Great\u2019s policy of religious tolerance drew on Zoroastrian ethical principles"),
        rel("zoroaster", "Zoroaster", "INFLUENCES", "judaism", "Jewish concepts of Satan, angels, resurrection, and apocalypse developed under Persian-Zoroastrian influence"),
        rel("zoroaster", "Zoroaster", "AUTHORS", "gathas", "Composed the Gathas, the oldest and most sacred hymns of the Avesta"),
        rel("zoroaster", "Zoroaster", "OCCURS_IN", "ancient-iran", "Lived and preached in ancient Iran/Central Asia, the birthplace of Zoroastrianism"),
    ],
    "subjectHeadings": ["People \u2014 Religious Founders \u2014 Iran \u2014 Prehistoric"],
    "subjects": ["Zoroastrianism", "Ahura Mazda", "Gathas", "Avesta", "Dualism", "Monotheism", "Ancient Iran", "Magi", "Good vs Evil", "Achaemenid Empire"],
    "frameworks": ["DOCTRINE_DEVELOPMENT", "CAUSE_AND_EFFECT", "CULTURAL_DIFFUSION", "ETHICAL_FRAMEWORK", "RELIGIOUS_INSTITUTIONS"],
},

"abraham": {
    "summary": "Abraham (originally Abram, c. 2000\u20131800 BCE, traditional dating) is the founding patriarch of the three Abrahamic faiths \u2014 Judaism, Christianity, and Islam \u2014 making him the single most theologically consequential figure in the history of monotheism, father of a spiritual lineage claiming over 4 billion adherents (55% of humanity). Born in Ur of the Chaldees (southern Mesopotamia), he received God\u2019s call to \u2018go to a land I will show you\u2019 (Genesis 12:1), abandoning Mesopotamian polytheism for radical monotheism and a covenant that promised his descendants would become a great nation and a blessing to all the earth. He journeyed with his wife Sarah, nephew Lot, and household to Canaan, then to Egypt during famine, before settling at Hebron. God\u2019s covenant with Abraham (Genesis 15, 17) \u2014 promising land, descendants as numerous as the stars, and universal blessing \u2014 is the foundational narrative of biblical religion. The binding of Isaac (the Akedah, Genesis 22) \u2014 where Abraham\u2019s willingness to sacrifice his son tested and proved his absolute faith \u2014 is among the most profound and debated passages in world literature. Judaism traces its lineage through Isaac and Jacob; Islam traces its lineage through Ishmael (Ismail), son of Abraham and Hagar, and regards Abraham (Ibrahim) as the builder of the Kaaba in Mecca. Christianity sees Abraham as the father of faith (Romans 4, Galatians 3), justified by belief before the Law. His tomb at the Cave of Machpelah in Hebron is sacred to all three faiths and has been a site of pilgrimage and conflict for 4,000 years. No single individual\u2019s story has shaped more human beings\u2019 self-understanding of their relationship with God.",
    "died": "c. 1800 BCE (traditional)",
    "period": "c. 2000\u20131800 BCE (traditional)",
    "wikidataQid": "Q9190",
    "wikipediaUrl": "https://en.wikipedia.org/wiki/Abraham",
    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/4/46/Rembrandt_Abraham_and_Isaac_1634.jpg",
    "causes": [
        "Mesopotamian polytheistic civilization (Ur of the Chaldees) provided the religious context from which Abraham\u2019s radical monotheistic break emerged",
        "God\u2019s call to leave Ur and journey to Canaan (Genesis 12:1) initiated the covenantal relationship that defines Abrahamic religion",
        "The ancient Near Eastern practice of covenant-making provided the cultural framework for God\u2019s promises to Abraham"
    ],
    "effects": [
        "Founded the Abrahamic monotheistic tradition that encompasses Judaism, Christianity, and Islam (4+ billion adherents, 55% of humanity)",
        "The Abrahamic covenant (land, descendants, universal blessing) became the foundational narrative of biblical religion",
        "The binding of Isaac (Akedah) established the paradigm of absolute faith tested by sacrifice, central to all three Abrahamic faiths",
        "His journey from Mesopotamia to Canaan established the concept of the Promised Land, shaping Jewish identity for 4,000 years",
        "Islam\u2019s tradition that Abraham and Ishmael built the Kaaba in Mecca connects the Hajj pilgrimage to Abrahamic origins",
        "Paul\u2019s argument that Abraham was justified by faith (Romans 4) became the theological foundation of Protestant Christianity"
    ],
    "relationships": [
        rel("abraham", "Abraham", "ANCESTOR_OF", "moses", "Abraham\u2019s covenant was fulfilled through Moses\u2019s liberation of Israel from Egypt"),
        rel("abraham", "Abraham", "ANCESTOR_OF", "david", "David\u2019s kingship fulfilled the promise of national greatness to Abraham\u2019s descendants"),
        rel("abraham", "Abraham", "ANCESTOR_OF", "jesus-christ", "Jesus as the \u2018seed of Abraham\u2019 (Galatians 3:16) through whom all nations are blessed"),
        rel("abraham", "Abraham", "REVERED_BY", "muhammad", "Islam honors Ibrahim as the first Muslim and father of Ishmael, ancestor of the Arab peoples"),
        rel("abraham", "Abraham", "OCCURS_IN", "ancient-mesopotamia", "Born in Ur of the Chaldees; journeyed to Canaan via Haran"),
        rel("abraham", "Abraham", "OCCURS_IN", "ancient-israel", "Settled in Canaan (Hebron), where the covenant promises centered on the Promised Land"),
    ],
    "subjectHeadings": ["People \u2014 Patriarchs & Prophets \u2014 Mesopotamia/Canaan \u2014 Classical"],
    "subjects": ["Abrahamic Faiths", "Covenant", "Monotheism", "Patriarchs", "Genesis", "Promised Land", "Akedah", "Canaan", "Ur", "Faith"],
    "frameworks": ["DOCTRINE_DEVELOPMENT", "CAUSE_AND_EFFECT", "CULTURAL_DIFFUSION", "ETHICAL_FRAMEWORK", "RELIGIOUS_INSTITUTIONS"],
},

"homer": {
    "summary": "Homer (c. 8th century BCE) was the legendary Greek poet traditionally credited as the author of the Iliad and the Odyssey \u2014 the two foundational works of Western literature and the oldest surviving masterpieces of European poetry. Almost nothing certain is known of his life: ancient tradition held he was blind (a trope perhaps derived from the blind bard Demodocus in the Odyssey), born in Ionia (with seven cities claiming him: Smyrna, Chios, Colophon, Salamis, Rhodes, Argos, and Athens), and composed his epics through oral performance. The Iliad, set during the Trojan War, centers on the wrath of Achilles and explores honor, mortality, glory, and the human cost of war in 15,693 lines of dactylic hexameter. The Odyssey recounts Odysseus\u2019s ten-year journey home, weaving themes of cunning, fidelity, identity, and the longing for homecoming (nostos) into 12,110 lines. Together, these works provided the Greeks with their theology, ethics, and cultural identity \u2014 Alexander the Great slept with the Iliad under his pillow, and it served as the primary educational text for all Greek-speaking peoples for a millennium. The \u2018Homeric Question\u2019 \u2014 whether one poet or multiple oral tradition bearers composed these works \u2014 has been debated since antiquity. Milman Parry\u2019s oral-formulaic theory (1930s) demonstrated that the poems\u2019 formulaic phrases and epithets reflect centuries of oral performance tradition. Regardless of authorship, the Homeric epics remain the fountainhead of Western literature: Virgil\u2019s Aeneid, Dante\u2019s Commedia, Milton\u2019s Paradise Lost, Joyce\u2019s Ulysses, and countless other works descend from Homer\u2019s tradition.",
    "died": "",
    "period": "c. 8th century BCE",
    "wikidataQid": "Q6691",
    "wikipediaUrl": "https://en.wikipedia.org/wiki/Homer",
    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/1/1c/Homer_British_Museum.jpg",
    "causes": [
        "The Greek oral tradition of heroic poetry, stretching back to the Mycenaean Bronze Age (c. 1200 BCE), provided the material and performance tradition from which the Homeric epics emerged",
        "The Trojan War (c. 1200 BCE) and its aftermath generated the legendary cycle that the Iliad and Odyssey drew upon",
        "The invention of the Greek alphabet (c. 800 BCE), adapted from Phoenician script, may have enabled the epics\u2019 transcription from oral to written form"
    ],
    "effects": [
        "The Iliad and Odyssey became the foundational texts of Western literature and the primary educational texts of ancient Greece",
        "Greek theology, ethics, and cultural identity were shaped by Homeric depictions of gods, heroes, honor, and fate",
        "Alexander the Great carried the Iliad on campaign; Aristotle annotated it; Roman Virgil modeled the Aeneid upon it",
        "Every subsequent Western epic (Virgil, Dante, Milton, Joyce) descends from the Homeric tradition",
        "The oral-formulaic theory arising from Homeric scholarship (Parry, Lord) revolutionized the study of oral literature worldwide",
        "Archaeological excavation of Troy (Schliemann, 1870s) was directly inspired by Homer\u2019s descriptions, founding modern classical archaeology"
    ],
    "relationships": [
        rel("homer", "Homer", "AUTHORS", "iliad", "Traditionally credited as author of the Iliad, the oldest surviving work of Western literature"),
        rel("homer", "Homer", "AUTHORS", "odyssey", "Traditionally credited as author of the Odyssey, the foundational Western adventure narrative"),
        rel("homer", "Homer", "INFLUENCES", "aristotle", "Aristotle\u2019s Poetics analyzes Homeric epic as the basis of Western literary criticism"),
        rel("homer", "Homer", "INFLUENCES", "alexander-the-great", "Alexander carried the Iliad on campaign and modeled himself on Achilles"),
        rel("homer", "Homer", "OCCURS_IN", "ancient-greece", "Composed in Ionia/Greece during the Greek Archaic period (c. 8th century BCE)"),
    ],
    "subjectHeadings": ["People \u2014 Poets & Authors \u2014 Greece \u2014 Classical"],
    "subjects": ["Iliad", "Odyssey", "Greek Epic", "Trojan War", "Oral Tradition", "Western Literature", "Ancient Greece", "Poetry", "Mythology", "Heroic Age"],
    "frameworks": ["CULTURAL_DIFFUSION", "CAUSE_AND_EFFECT", "DOCTRINE_DEVELOPMENT", "SOCIAL_STRUCTURES", "LITERARY_TRADITION"],
},

"cyrus-the-great": {
    "summary": "Cyrus II (\u2018the Great,\u2019 c. 600\u2013530 BCE) was the founder of the Achaemenid Empire \u2014 the largest empire the world had yet seen, stretching from the Aegean Sea to the Indus River \u2014 and the first ruler in history to articulate a policy of religious tolerance, human rights, and cultural autonomy for conquered peoples, as recorded in the Cyrus Cylinder (539 BCE), often called the \u2018first declaration of human rights.\u2019 Born to Cambyses I of Anshan and Mandane of Media, he united the Persian and Median tribes, overthrew his grandfather Astyages of Media (550 BCE), conquered the fabulously wealthy Lydian Empire of Croesus (546 BCE), and captured Babylon without significant resistance (539 BCE) by diverting the Euphrates River. His treatment of Babylon was revolutionary: rather than destroying the city and deporting its people (the Assyrian model), he restored temples, honored local gods, and freed captive peoples \u2014 including the Jews, whom he permitted to return to Jerusalem and rebuild the Temple. For this act, the Hebrew Bible uniquely calls a non-Jewish king \u2018messiah\u2019 (anointed one, Isaiah 45:1). His empire\u2019s administrative innovations \u2014 satrapies (provincial governorships), the Royal Road, a postal system, standardized weights and coinage, and the principle of governance by consent rather than mere terror \u2014 became the model for all subsequent Middle Eastern empires. Thomas Jefferson and the American Founding Fathers studied Xenophon\u2019s Cyropaedia as a model of enlightened governance. The United Nations displayed a replica of the Cyrus Cylinder in 1971 as a symbol of human rights, and the Islamic Republic of Iran chose the Cyrus Cylinder\u2019s winged disc as the emblem of Iran Air.",
    "died": "c. 530 BCE",
    "period": "c. 600\u2013530 BCE",
    "wikidataQid": "Q7101",
    "wikipediaUrl": "https://en.wikipedia.org/wiki/Cyrus_the_Great",
    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Illustrerad_Verldshistoria_band_I_Ill_058.jpg",
    "causes": [
        "The Persian-Median tribal alliance and Cyrus\u2019s strategic revolt against Astyages unified the Iranian plateau under Persian leadership",
        "The Babylonian Empire\u2019s internal discontent under Nabonidus\u2019s unpopular religious reforms made Babylon vulnerable to conquest",
        "Zoroastrian ethical principles of truth (asha) and righteous governance provided the ideological framework for Cyrus\u2019s tolerant policies"
    ],
    "effects": [
        "Founded the Achaemenid Empire (550\u2013330 BCE), the largest empire the ancient world had seen, governing 44% of the world\u2019s population",
        "The Cyrus Cylinder (539 BCE) articulated the first known policy of religious tolerance and human rights",
        "Freed the Jewish captives in Babylon and authorized the rebuilding of the Jerusalem Temple (Ezra 1), earning the title \u2018messiah\u2019 in Isaiah 45:1",
        "Administrative innovations (satrapies, Royal Road, postal system, standardized coinage) became the template for all subsequent Near Eastern empires",
        "His model of governance by consent and cultural autonomy influenced Alexander the Great, the Roman Empire, and Enlightenment political thought",
        "The Cyrus Cylinder was displayed at the United Nations (1971) as a symbol of human rights and cultural tolerance"
    ],
    "relationships": [
        rel("cyrus-the-great", "Cyrus the Great", "ESTABLISHES", "achaemenid-empire", "Founded the Achaemenid Persian Empire (550 BCE), the largest empire the world had yet seen"),
        rel("cyrus-the-great", "Cyrus the Great", "CONQUERS", "babylon", "Captured Babylon (539 BCE) by diverting the Euphrates, ending the Neo-Babylonian Empire"),
        rel("cyrus-the-great", "Cyrus the Great", "FREES", "jewish-exile", "Freed the Jewish captives and authorized rebuilding the Jerusalem Temple (Ezra 1:1-4)"),
        rel("cyrus-the-great", "Cyrus the Great", "INFLUENCED_BY", "zoroaster", "Zoroastrian ethical principles shaped Cyrus\u2019s unprecedented policy of religious tolerance"),
        rel("cyrus-the-great", "Cyrus the Great", "INFLUENCES", "alexander-the-great", "Alexander honored Cyrus\u2019s tomb at Pasargadae and emulated his governance model"),
        rel("cyrus-the-great", "Cyrus the Great", "OCCURS_IN", "ancient-persia", "Ruled from Pasargadae and Ecbatana over the Persian heartland and conquered territories"),
    ],
    "subjectHeadings": ["People \u2014 Emperors & Rulers \u2014 Persia \u2014 Classical"],
    "subjects": ["Achaemenid Empire", "Cyrus Cylinder", "Religious Tolerance", "Human Rights", "Babylon", "Persia", "Jewish Exile", "Zoroastrianism", "Satrapies", "Ancient Iran"],
    "frameworks": ["POLITICAL_SYSTEMS", "CAUSE_AND_EFFECT", "ETHICAL_FRAMEWORK", "CULTURAL_DIFFUSION", "RELIGIOUS_INSTITUTIONS"],
},

}

# ============================================================
# APPLY ENRICHMENTS
# ============================================================

FILE_MAP = {
    "jesus-christ": "data/appwrite-export/entities/201-Class-201/201jesus-christ.json",
    "muhammad": "data/appwrite-export/entities/251-Class-251/251muhammad.json",
    "julius-caesar": "data/appwrite-export/entities/221-Class-221/221julius-caesar.json",
    "aristotle": "data/appwrite-export/entities/210-Class-210/21004-aristotle.json",
    "plato": "data/appwrite-export/entities/210-Class-210/21003-plato.json",
    "socrates": "data/appwrite-export/entities/210-Class-210/21002-socrates.json",
    "augustus": "data/appwrite-export/entities/221-Class-221/221augustus.json",
    "cleopatra": "data/appwrite-export/entities/221-Class-221/221cleopatra.json",
    "genghis-khan": "data/appwrite-export/entities/280-Class-280/280genghis-khan.json",
    "martin-luther": "data/appwrite-export/entities/201-Class-201/201martin-luther.json",
    "galileo-galilei": "data/appwrite-export/entities/201-Class-201/201galileo-galilei.json",
    "albert-einstein": "data/appwrite-export/entities/240-Class-240/240albert-einstein.json",
    "ashoka": "data/appwrite-export/entities/221-Class-221/221ashoka.json",
    "nelson-mandela": "data/appwrite-export/entities/222-Class-222/222nelson-mandela.json",
    "nikola-tesla": "data/appwrite-export/entities/240-Class-240/240nikola-tesla.json",
    "winston-churchill": "data/appwrite-export/entities/222-Class-222/222winston-churchill.json",
    "abraham-lincoln": "data/appwrite-export/entities/222-Class-222/222abraham-lincoln.json",
    "george-washington": "data/appwrite-export/entities/222-Class-222/222george-washington.json",
    "charlemagne": "data/appwrite-export/entities/221-Class-221/221charlemagne.json",
    "saladin": "data/appwrite-export/entities/221-Class-221/221saladin.json",
    "mahatma-gandhi": "data/appwrite-export/entities/205-Class-205/205mahatma-gandhi.json",
    "martin-luther-king-jr": "data/appwrite-export/entities/204-Class-204/204martin-luther-king-jr.json",
    "zoroaster": "data/appwrite-export/entities/262-Class-262/262zoroaster.json",
    "abraham": "data/appwrite-export/entities/251-Class-251/251abraham.json",
    "homer": "data/appwrite-export/entities/260-Class-260/26001-homer.json",
    "cyrus-the-great": "data/appwrite-export/entities/251-Class-251/251cyrus-the-great.json",
}

updated = 0
for slug, enrich in ENRICHMENTS.items():
    path = FILE_MAP.get(slug)
    if not path or not os.path.exists(path):
        print(f"SKIP {slug}: file not found ({path})")
        continue

    with open(path) as f:
        data = json.load(f)
    entity = data["entities"][0]

    # Build details
    old_dj = json.loads(entity.get("detailsJson", "{}"))
    new_dj = {
        "causes": enrich.get("causes", old_dj.get("causes", [])),
        "effects": enrich.get("effects", old_dj.get("effects", [])),
        "relationships": enrich.get("relationships", old_dj.get("relationships", [])),
        "places": old_dj.get("places", []),
        "texts": old_dj.get("texts", []),
        "externalLinks": old_dj.get("externalLinks", []),
        "tags": old_dj.get("tags", []),
        "thumbnailUrl": old_dj.get("thumbnailUrl", ""),
        "quote": old_dj.get("quote", ""),
        "legacySummary": old_dj.get("legacySummary", ""),
    }

    entity["summary"] = enrich["summary"]
    entity["detailsJson"] = json.dumps(new_dj, ensure_ascii=False)

    # Update metadata fields
    for key in ["died", "period", "wikidataQid", "wikipediaUrl", "imageUrl",
                 "subjectHeadings", "subjects", "frameworks"]:
        if key in enrich and enrich[key]:
            entity[key] = enrich[key]

    data["entities"][0] = entity
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    slen = len(entity["summary"])
    rlen = len(new_dj["relationships"])
    updated += 1
    print(f"OK {slug:30s} | summary={slen:4d} | rels={rlen} | causes={len(new_dj['causes'])} | effects={len(new_dj['effects'])}")

print(f"\n=== Updated {updated} entities ===")
