#!/usr/bin/env python3
"""
Batch 2: Reformat summaries with paragraph breaks + enrich more entities.
- Adds \\n\\n paragraph breaks to all 29 previously enriched entities
- Enriches 15 more historically important entities with rich paragraphed summaries
"""
import json, os

def slug_to_name(slug):
    MAP = {
        "abraham": "Abraham", "moses": "Moses", "jesus-christ": "Jesus Christ",
        "muhammad": "Muhammad", "buddha": "Buddha", "confucius": "Confucius",
        "julius-caesar": "Julius Caesar", "aristotle": "Aristotle",
        "plato": "Plato", "socrates": "Socrates", "augustus": "Augustus",
        "cleopatra": "Cleopatra VII", "genghis-khan": "Genghis Khan",
        "martin-luther": "Martin Luther", "galileo-galilei": "Galileo Galilei",
        "albert-einstein": "Albert Einstein", "ashoka": "Ashoka",
        "nelson-mandela": "Nelson Mandela", "nikola-tesla": "Nikola Tesla",
        "winston-churchill": "Winston Churchill", "abraham-lincoln": "Abraham Lincoln",
        "george-washington": "George Washington", "charlemagne": "Charlemagne",
        "saladin": "Saladin", "mahatma-gandhi": "Mahatma Gandhi",
        "martin-luther-king-jr": "Martin Luther King Jr.",
        "zoroaster": "Zoroaster", "homer": "Homer",
        "cyrus-the-great": "Cyrus the Great", "david": "King David",
        "solomon": "King Solomon", "sun-tzu": "Sun Tzu",
        "alexander-the-great": "Alexander the Great",
        "isaac-newton": "Isaac Newton", "napoleon-bonaparte": "Napoleon Bonaparte",
        "leonardo-da-vinci": "Leonardo da Vinci", "pythagoras": "Pythagoras",
        "hippocrates": "Hippocrates", "michelangelo": "Michelangelo",
        "thomas-edison": "Thomas Edison", "laozi": "Laozi",
        "william-shakespeare": "William Shakespeare",
        "charles-darwin": "Charles Darwin", "paul-the-apostle": "Paul the Apostle",
        "joan-of-arc": "Joan of Arc", "christopher-columbus": "Christopher Columbus",
        "karl-marx": "Karl Marx", "thomas-jefferson": "Thomas Jefferson",
        "herodotus": "Herodotus", "marco-polo": "Marco Polo",
        "hannibal": "Hannibal Barca", "constantine-i": "Constantine I",
        "roman-republic": "Roman Republic", "roman-empire": "Roman Empire",
        "achaemenid-empire": "Achaemenid Empire", "persian-empire": "Persian Empire",
        "mongol-empire": "Mongol Empire", "ottoman-empire": "Ottoman Empire",
        "holy-roman-empire": "Holy Roman Empire", "catholic-church": "Catholic Church",
        "ancient-greece": "Ancient Greece", "ancient-rome": "Ancient Rome",
        "ancient-egypt": "Ancient Egypt", "ancient-india": "Ancient India",
        "ancient-china": "Ancient China", "ancient-israel": "Ancient Israel",
        "renaissance": "Renaissance", "reformation": "Protestant Reformation",
        "french-revolution": "French Revolution", "industrial-revolution": "Industrial Revolution",
        "united-states": "United States", "united-kingdom": "United Kingdom",
        "south-africa": "South Africa", "india": "India",
        "florence": "Florence", "athens": "Athens", "rome": "Rome",
        "mecca": "Mecca", "medina": "Medina", "jerusalem": "Jerusalem",
        "princeton": "Princeton", "paris": "Paris", "london": "London",
        "stratford-upon-avon": "Stratford-upon-Avon", "galapagos": "Galápagos",
        "the-origin-of-species": "On the Origin of Species",
        "principia-mathematica": "Principia Mathematica",
        "the-prince": "The Prince", "the-art-of-war": "The Art of War",
        "iliad": "Iliad", "odyssey": "Odyssey", "quran": "Quran",
        "republic-plato": "Republic (Plato)", "das-kapital": "Das Kapital",
        "communist-manifesto": "The Communist Manifesto",
        "first-folio": "First Folio", "hamlet": "Hamlet",
        "sistine-chapel": "Sistine Chapel", "mona-lisa": "Mona Lisa",
        "last-supper": "The Last Supper",
        "declaration-of-independence": "Declaration of Independence",
        "american-revolution": "American Revolution",
        "battle-of-cannae": "Battle of Cannae",
        "punic-wars": "Punic Wars", "carthage": "Carthage",
        "hundred-years-war": "Hundred Years' War", "france": "France",
        "england": "England", "gaul": "Gaul",
        "silk-road": "Silk Road", "kublai-khan": "Kublai Khan",
        "yuan-dynasty": "Yuan Dynasty", "china": "China", "venice": "Venice",
        "first-crusade": "First Crusade", "third-crusade": "Third Crusade",
        "council-of-nicaea": "Council of Nicaea",
        "edict-of-milan": "Edict of Milan",
        "byzantine-empire": "Byzantine Empire",
        "christianity": "Christianity", "pagan-rome": "Pagan Rome",
        "thomas-aquinas": "Thomas Aquinas",
        "niccolo-machiavelli": "Niccolò Machiavelli",
        "frederick-engels": "Frederick Engels",
        "russian-revolution": "Russian Revolution",
        "soviet-union": "Soviet Union",
        "edmund-halley": "Edmund Halley",
        "robert-hooke": "Robert Hooke",
        "gottfried-leibniz": "Gottfried Leibniz",
        "scientific-revolution": "Scientific Revolution",
    }
    return MAP.get(slug, slug.replace("-", " ").title())


def rel(source_slug, source_name, verb, target_slug, context):
    return {
        "sourceSlug": source_slug,
        "sourceName": source_name,
        "verb": verb,
        "targetSlug": target_slug,
        "targetName": slug_to_name(target_slug),
        "context": context
    }


# ================================================================
# STEP 1: Paragraph-break reformats for all 29 previously enriched
# ================================================================

PARAGRAPH_REFORMATS = {

"jesus-christ": (
    "Jesus of Nazareth (c. 4 BCE – c. 30 CE) is the central figure of Christianity, acknowledged by over 2.4 billion adherents as the Son of God, the Messiah prophesied in the Hebrew scriptures, and the incarnation of the divine Logos. Born in Bethlehem during the reign of Herod the Great, raised in Nazareth, he emerged at age 30 with a public ministry of teaching, healing, and radical reinterpretation of Jewish Law that lasted approximately three years.\n\n"
    "His Sermon on the Mount articulated the Beatitudes, the Lord's Prayer, and an ethic of enemy-love that reshaped Western moral philosophy. He selected twelve apostles, performed miracles attested by multiple independent traditions, and proclaimed the Kingdom of God — a present-and-coming divine reign accessible to the poor, the outcast, and the repentant.\n\n"
    "His triumphal entry into Jerusalem, cleansing of the Temple, and Last Supper precipitated his arrest, trial before Pontius Pilate, and crucifixion on Golgotha. His followers proclaimed his bodily resurrection on the third day — the foundational claim of Christianity. Within three centuries, the faith he founded transformed from a persecuted Jewish sect into the official religion of the Roman Empire.\n\n"
    "The calendar pivots on his birth (Anno Domini). His teachings on forgiveness, human dignity, sacrificial love, and the separation of religious and political authority shaped Western concepts of human rights, charity, education, and law."
),

"muhammad": (
    "Muhammad ibn Abdullah (c. 570–632 CE) was the founder of Islam, regarded by 1.9 billion Muslims as the final prophet in the Abrahamic tradition. Born in Mecca to the Quraysh tribe, orphaned early, he became a merchant known for exceptional honesty (al-Amin, 'the Trustworthy').\n\n"
    "At age 40, during meditation in the Cave of Hira, he received the first Quranic revelation from the angel Jibril: 'Recite, in the name of your Lord who created.' For 23 years he received revelations compiled into the Quran — a masterwork of Arabic prose codifying theology, law, ethics, and governance.\n\n"
    "Persecuted in Mecca, he led the Hijra to Medina in 622 CE — the event that begins the Islamic calendar. There he established the Constitution of Medina, unified warring Arab tribes, and built a community governed by divine law. After the Battle of Badr and the bloodless Conquest of Mecca (630 CE), he united the Arabian Peninsula under Islam.\n\n"
    "Within a century of his death, the Rashidun and Umayyad caliphates had spread Islam from Spain to Central Asia — the fastest expansion of any religion in history."
),

"julius-caesar": (
    "Gaius Julius Caesar (100–44 BCE) was a Roman military commander, statesman, and dictator whose conquest of Gaul, crossing of the Rubicon, and centralization of power ended the Roman Republic and laid the foundation for the Roman Empire. Born to the patrician gens Julia, he rose through the cursus honorum and formed the First Triumvirate with Pompey and Crassus.\n\n"
    "His Gallic Wars (58–50 BCE) conquered modern France, Belgium, and parts of Germany and Britain, while his Commentarii de Bello Gallico became a masterpiece of Latin prose. When the Senate ordered him to disband his army, he crossed the Rubicon (49 BCE) with 'alea iacta est,' triggering civil war.\n\n"
    "Named dictator perpetuo in 44 BCE, he enacted sweeping reforms: the Julian calendar, land redistribution, citizenship expansion, and debt relief. His assassination on the Ides of March by Brutus, Cassius, and 58 senators — perhaps history's most famous political murder — triggered the wars that destroyed the Republic.\n\n"
    "His adopted heir Octavian (Augustus) became Rome's first emperor. The month of July and the title 'Caesar' (becoming Kaiser and Tsar) immortalize his legacy."
),

"aristotle": (
    "Aristotle (384–322 BCE) was a Greek philosopher and polymath whose works constitute the first comprehensive system of Western philosophy — encompassing logic, metaphysics, ethics, politics, biology, physics, rhetoric, and poetics. Born in Stagira to the physician Nicomachus, he entered Plato's Academy at 17 and studied there for 20 years.\n\n"
    "After tutoring Alexander the Great, he founded the Lyceum in Athens, where his 'Peripatetics' became antiquity's premier research institution. His Organon created formal logic — the syllogism remained the foundation of reasoning for over 2,000 years until Frege's modern predicate logic.\n\n"
    "His Nicomachean Ethics defined eudaimonia as the highest good. His biological works classified over 500 species, founding zoology. His Poetics defined tragedy and the dramatic unities governing Western theater for centuries.\n\n"
    "Transmitted through Arabic translations by Averroes and Avicenna, his works were synthesized with Christian theology by Thomas Aquinas — making him simply 'The Philosopher' in Scholastic thought."
),

"plato": (
    "Plato (c. 428–348 BCE) was an Athenian philosopher whose dialogues, Academy, and Theory of Forms established the foundation of Western philosophy, metaphysics, and political theory. Born to Athenian aristocracy, he became Socrates's most brilliant student.\n\n"
    "Socrates's execution in 399 BCE transformed Plato's life. After traveling to Egypt, Italy, and Syracuse, he founded the Academy (c. 387 BCE) — the Western world's first institution of higher learning, which operated for over 900 years.\n\n"
    "His 36 dialogues explored justice (Republic), love (Symposium), the soul's immortality (Phaedo), and reality's nature (Timaeus). The Theory of Forms posited that the physical world is a shadow of eternal, perfect Ideas — most famously illustrated in the Allegory of the Cave.\n\n"
    "Alfred North Whitehead declared that 'the European philosophical tradition consists of a series of footnotes to Plato.' His influence permeates Christian theology, Islamic philosophy, Renaissance humanism, and modern political theory."
),

"socrates": (
    "Socrates (c. 470–399 BCE) was an Athenian philosopher whose relentless questioning of assumptions, refusal to write, and voluntary death by hemlock made him the founding martyr of Western philosophy. Son of a stonemason and midwife, he served with distinction as a hoplite at Potidaea, Delium, and Amphipolis.\n\n"
    "Rather than pursue wealth, he spent his life in the agora engaging citizens in the 'Socratic method' — cross-examination that exposed contradictions in conventional wisdom. He claimed to know only that he knew nothing, and the Oracle at Delphi declared him the wisest man in Athens.\n\n"
    "His insistence that 'the unexamined life is not worth living' and that virtue is knowledge laid Western ethics' foundations. Though he wrote nothing, Plato, Xenophon, and Aristophanes preserved his teachings.\n\n"
    "In 399 BCE, Athens convicted him of impiety and corrupting youth. He refused exile, drank hemlock, and died surrounded by disciples — an act of principled civil disobedience that has inspired thinkers from Seneca to Martin Luther King Jr."
),

"augustus": (
    "Augustus (63 BCE – 14 CE), born Octavian, was the first Roman Emperor and founder of the Principate. Adopted as Julius Caesar's heir at 18, he defeated every rival: forming the Second Triumvirate, defeating Brutus at Philippi, and crushing Antony and Cleopatra at the Battle of Actium (31 BCE).\n\n"
    "In 27 BCE the Senate awarded him 'Augustus' ('the Revered One'). He crafted a constitutional fiction: officially restoring the Republic while accumulating sole power. His 41-year reign inaugurated the Pax Romana — two centuries of unprecedented peace and cultural achievement.\n\n"
    "He reformed taxation, established the Praetorian Guard, built a professional army, sponsored Virgil's Aeneid, and transformed Rome from brick to marble. The Res Gestae Divi Augusti remains one of antiquity's most important political documents.\n\n"
    "Jesus of Nazareth was born during his census (Luke 2:1). The month of August bears his name, and the title 'Augustus' became the standard for all subsequent Roman emperors."
),

"cleopatra": (
    "Cleopatra VII Philopator (69–30 BCE) was the last active ruler of Ptolemaic Egypt — a polyglot diplomat, naval commander, and political strategist whose alliances with Julius Caesar and Mark Antony made her the most powerful woman in the ancient Mediterranean. She was the first Ptolemaic ruler in 300 years to learn Egyptian, speaking nine languages total.\n\n"
    "Deposed by her brother-husband Ptolemy XIII, she was restored to power through alliance with Caesar. She bore him a son (Caesarion) and later formed a political-romantic alliance with Mark Antony, whose Donations of Alexandria challenged Rome directly.\n\n"
    "Their combined forces fell at Actium (31 BCE). Rather than be paraded in Octavian's triumph, she died by her own hand. With her death, 3,000 years of Egyptian pharaonic rule ended and Egypt became a Roman province.\n\n"
    "Subject of over 200 films, Shakespeare's masterpiece, and countless operas — she remains one of the most depicted women in world history."
),

"genghis-khan": (
    "Genghis Khan (Temujin, c. 1162–1227 CE) founded the Mongol Empire — the largest contiguous land empire in history, stretching from Korea to Hungary. Born to a minor chieftain who was murdered when Temujin was nine, he endured kidnapping, enslavement, and betrayal before unifying the Mongol and Turkic tribes.\n\n"
    "Proclaimed 'Universal Ruler' in 1206, he created the Yasa legal code imposing discipline, religious tolerance, and meritocratic advancement. His military innovations — decimal organization, composite bow cavalry, psychological warfare, and siege engineering — created the medieval world's most effective fighting force.\n\n"
    "He systematically conquered the Xi Xia, Jin Dynasty, and Khwarazmian Empire. Though his campaigns killed an estimated 40 million people (10% of the world's population), the resulting Pax Mongolica reopened the Silk Road.\n\n"
    "This enabled direct Europe-China contact, the westward transfer of gunpowder, printing, and the compass, and Marco Polo's famous journey. A 2003 genetic study estimated 16 million men alive today carry his Y-chromosome."
),

"martin-luther": (
    "Martin Luther (1483–1546) was a German Augustinian friar whose Ninety-Five Theses (1517), doctrine of justification by faith alone, and German Bible translation ignited the Protestant Reformation — the most consequential schism in Western Christianity.\n\n"
    "Tormented by divine righteousness, he experienced his 'Tower Experience' (c. 1515) — the revelation that salvation comes through faith, not works. On October 31, 1517, he challenged the sale of indulgences, and Gutenberg's press spread his protest across Europe within weeks.\n\n"
    "At the Diet of Worms (1521), he refused to recant: 'Here I stand; I can do no other.' In Wartburg Castle he translated the New Testament into German in 11 weeks — a literary masterpiece that standardized the German language.\n\n"
    "His five solas catalyzed all Protestant churches and indirectly contributed to the Wars of Religion, the Peace of Westphalia, sovereign nation-states, and the Enlightenment's emphasis on individual conscience."
),

"galileo-galilei": (
    "Galileo Galilei (1564–1642) was an Italian astronomer, physicist, and mathematician — the 'father of modern science' (Einstein). In 1609, he built a telescope and turned it skyward, discovering Jupiter's four largest moons, Venus's phases, sunspots, lunar craters, and the Milky Way's individual stars.\n\n"
    "These observations, published in Sidereus Nuncius (1610), provided the first empirical evidence for Copernicus's heliocentric model and demolished 1,400 years of Aristotelian-Ptolemaic cosmology.\n\n"
    "His Dialogue Concerning the Two Chief World Systems (1632) was so persuasive that the Inquisition convicted him of heresy (1633), forcing recantation and house arrest. Legend holds he muttered 'Eppur si muove' ('And yet it moves').\n\n"
    "During house arrest, though blind, he produced his greatest work: Two New Sciences (1638), laying the foundations of kinematics and materials science. Stephen Hawking was born exactly 300 years after Galileo's death."
),

"albert-einstein": (
    "Albert Einstein (1879–1955) was a German-born theoretical physicist whose theories of relativity and mass-energy equivalence (E=mc²) fundamentally reconceived space, time, gravity, and energy — making him the most influential physicist since Newton.\n\n"
    "While working as a patent clerk in Bern, he published four revolutionary papers in his annus mirabilis (1905): on the photoelectric effect, Brownian motion, special relativity, and mass-energy equivalence. His general relativity (1915) reimagined gravity as spacetime curvature.\n\n"
    "Arthur Eddington's 1919 solar eclipse confirmation made Einstein a global celebrity overnight. Fleeing Nazi Germany in 1933, he joined Princeton's Institute for Advanced Study. His 1939 letter to Roosevelt helped launch the Manhattan Project.\n\n"
    "The photoelectric effect earned the 1921 Nobel Prize. General relativity predicted gravitational lensing, black holes, and gravitational waves — all confirmed experimentally. TIME named him Person of the Century (1999)."
),

"ashoka": (
    "Ashoka Maurya (c. 304–232 BCE) was the third Maurya emperor, ruling the largest empire in Indian history. His transformation from ruthless conqueror to champion of non-violence after the devastating Kalinga War represents one of history's most dramatic moral conversions.\n\n"
    "Kalinga (c. 261 BCE) cost 100,000 dead and 150,000 deported. Horrified, Ashoka embraced Buddhism and devoted 30 years to dhamma (righteousness). His Edicts — over 30 rock and pillar inscriptions, India's oldest deciphered texts — proclaimed religious tolerance, non-violence, animal welfare, and care for the poor.\n\n"
    "He sent Buddhist missionaries to Sri Lanka, Central Asia, Egypt, and Greece — the first systematic international missionary effort. His four-lion capital at Sarnath became India's national emblem; the Ashoka Chakra adorns the Indian flag.\n\n"
    "H.G. Wells wrote: 'Amidst the tens of thousands of names of monarchs, the name of Ashoka shines, and shines almost alone, a star.'"
),

"nelson-mandela": (
    "Nelson Mandela (1918–2013) was a South African anti-apartheid revolutionary who served as the country's first Black president (1994–1999), transforming a nation on the brink of racial civil war into a multiracial democracy through unprecedented reconciliation.\n\n"
    "As leader of the ANC's armed wing Umkhonto we Sizwe, he organized sabotage campaigns against apartheid. Sentenced to life imprisonment at the Rivonia Trial (1964), he spent 27 years in prison — 18 on Robben Island — yet emerged without bitterness.\n\n"
    "Released in 1990 (watched by 600 million), he negotiated with de Klerk to dismantle apartheid, sharing the 1993 Nobel Peace Prize. As president, he established the Truth and Reconciliation Commission — a model adopted by over 40 countries.\n\n"
    "He wore the Springbok jersey at the 1995 Rugby World Cup, unifying a divided nation through sport. He remains the world's most celebrated symbol of resistance to oppression and the power of forgiveness."
),

"nikola-tesla": (
    "Nikola Tesla (1856–1943) was a Serbian-American inventor whose alternating current polyphase power system, induction motor, and Tesla coil electrified the modern world and won the 'War of Currents' against Edison's direct current.\n\n"
    "Born in the Austrian Empire to a Serbian priest, Tesla experienced vivid visions and eidetic memory. After emigrating to the US in 1884 with four cents, his partnership with Edison soured over AC vs. DC. Allied with George Westinghouse, their AC system triumphed at the 1893 World's Columbian Exposition and Niagara Falls (1896).\n\n"
    "He held over 300 patents spanning radio, X-ray imaging, remote control, neon lighting, and wireless communication. His Wardenclyffe Tower envisioned worldwide wireless energy transmission decades ahead of its time.\n\n"
    "Despite his genius, he died nearly penniless. The SI unit tesla bears his name. Elon Musk named Tesla, Inc. in his honor."
),

"winston-churchill": (
    "Sir Winston Churchill (1874–1965) served as Prime Minister during World War II — widely regarded as the greatest wartime leader of the 20th century and the man who rallied the free world against Nazi tyranny when Britain stood alone.\n\n"
    "After a 'wilderness years' decade warning against appeasing Hitler, he became PM on May 10, 1940 — the day Germany invaded France. His speeches ('We shall fight on the beaches,' 'Their finest hour,' 'Never was so much owed by so many to so few') sustained British morale during the Blitz.\n\n"
    "He forged the Anglo-American alliance with Roosevelt, navigated partnership with Stalin, and helped plan D-Day. He coined 'Iron Curtain' in his Fulton speech (1946), defining the Cold War.\n\n"
    "He won the Nobel Prize in Literature (1953) for his six-volume The Second World War. In a 2002 BBC poll, Britons voted him the Greatest Briton of all time."
),

"abraham-lincoln": (
    "Abraham Lincoln (1809–1865) was the 16th US President who preserved the Union during the Civil War, abolished slavery, and redefined American democracy — by scholarly consensus, the greatest American president.\n\n"
    "Born in a log cabin, largely self-educated, he rose from rail-splitter to lawyer to president. His 1860 election triggered Southern secession. He navigated the bloodiest American conflict (750,000 dead) with moral clarity, political cunning, and rhetorical genius.\n\n"
    "The Emancipation Proclamation (1863) transformed the war into a crusade against bondage, freeing 3.5 million people. His Gettysburg Address — 272 words in three minutes — remains America's most quoted speech, redefining the nation as 'dedicated to the proposition that all men are created equal.'\n\n"
    "Assassinated five days after Lee's surrender, he became America's first martyred president. The Lincoln Memorial stands as the republic's most sacred civic shrine."
),

"george-washington": (
    "George Washington (1732–1799) was Commander-in-Chief of the Continental Army, president of the Constitutional Convention, and first US President — the indispensable figure in creating the American republic.\n\n"
    "Appointed commander in 1775, he held the Continental Army together through devastating retreats, near-mutinies, and Valley Forge's frozen encampment. His victories at Trenton and Yorktown won independence.\n\n"
    "His greatest act was political: voluntarily relinquishing power twice. After the war he returned to Mount Vernon; after two presidential terms he retired — King George III reportedly called this 'the greatest man in the world.' His Farewell Address warned against foreign entanglements and political factions.\n\n"
    "He freed his slaves in his will — the only slave-owning Founder to do so. 'First in war, first in peace, and first in the hearts of his countrymen.'"
),

"charlemagne": (
    "Charlemagne (c. 747–814 CE) was King of the Franks, King of the Lombards, and Emperor of the Romans — the first recognized emperor in Western Europe since Rome's fall (476 CE). His Christmas Day coronation by Pope Leo III (800 CE) created the entity that became the Holy Roman Empire.\n\n"
    "Through 53 campaigns, he united most of Western Europe: modern France, Germany, the Low Countries, Switzerland, Austria, and northern Italy. His forced conversion of the Saxons (772–804 CE) remains controversial.\n\n"
    "Yet his Carolingian Renaissance revived learning: palace schools under Alcuin of York, Carolingian minuscule (the script that became modern lowercase letters), classical text preservation in monastic scriptoria, and educational reform across Europe.\n\n"
    "He is the common ancestor of virtually every European royal house. Napoleon called himself 'the Charlemagne of the modern era.'"
),

"saladin": (
    "Saladin (1137–1193 CE) was a Kurdish Muslim sultan who unified Egypt and Syria and recaptured Jerusalem from the Crusaders in 1187 — becoming the most celebrated Muslim military leader of the medieval period and a byword for chivalry even among Christian enemies.\n\n"
    "The Battle of Hattin (1187) destroyed the Crusader army. He recaptured Jerusalem, but unlike the Crusaders' 1099 massacre, he spared the civilian population — an act that stunned Christendom.\n\n"
    "During the Third Crusade against Richard the Lionheart, the two earned mutual respect: when Richard fell ill, Saladin sent his personal physician. Their 1192 treaty allowed Christian pilgrims access while maintaining Muslim sovereignty.\n\n"
    "Dante placed him among virtuous pagans in the Inferno — one of the rare figures revered equally by both sides of a religious conflict."
),

"mahatma-gandhi": (
    "Mohandas Karamchand Gandhi (1869–1948), known as Mahatma ('Great Soul'), led India's independence from British rule through non-violent civil disobedience (satyagraha) — a strategy that inspired freedom movements worldwide.\n\n"
    "In South Africa (1893–1914), he developed satyagraha ('truth-force') against racial discrimination. Back in India, his campaigns — the Non-Cooperation Movement, the Salt March (1930), and Quit India (1942) — mobilized millions through fasting, boycotts, and peaceful protest.\n\n"
    "The Salt March — a 240-mile walk to make salt in defiance of the British monopoly — became history's most iconic act of civil disobedience. Though he never held office, his moral authority was decisive in achieving independence (August 15, 1947).\n\n"
    "Assassinated in 1948, his philosophy directly influenced Martin Luther King Jr., Nelson Mandela, and the Dalai Lama. The United Nations declared October 2 the International Day of Non-Violence."
),

"martin-luther-king-jr": (
    "Martin Luther King Jr. (1929–1968) was the most visible leader of the American civil rights movement, whose non-violent resistance, soaring oratory, and moral courage dismantled legal segregation in the United States.\n\n"
    "The Montgomery Bus Boycott (1955–56) thrust the 26-year-old pastor into national leadership. Over the next decade, he led campaigns in Albany, Birmingham, and Selma, was jailed 29 times, and survived multiple assassination attempts. His 'Letter from Birmingham Jail' argued that injustice anywhere threatens justice everywhere.\n\n"
    "His 'I Have a Dream' speech (August 28, 1963) at the Lincoln Memorial — before 250,000 people — is the greatest American speech of the 20th century. His leadership produced the Civil Rights Act (1964) and Voting Rights Act (1965).\n\n"
    "He received the Nobel Peace Prize (1964) at age 35. Assassinated in Memphis on April 4, 1968, he became a martyr for human rights. The federal holiday on the third Monday of January honors his legacy."
),

"zoroaster": (
    "Zoroaster (Zarathustra, c. 1500–1000 BCE) was an ancient Iranian prophet who founded Zoroastrianism — the first major monotheistic religion, whose concepts of heaven, hell, judgment, angels, demons, and the cosmic struggle between good and evil profoundly influenced Judaism, Christianity, and Islam.\n\n"
    "He received visions from Ahura Mazda ('Wise Lord') and composed the Gathas — 17 hymns among the most ancient religious texts in any Indo-European language. He radically reformed polytheism by elevating Ahura Mazda as supreme deity locked in battle with Angra Mainyu.\n\n"
    "This ethical dualism — free-will choice between good and evil with afterlife consequences — was revolutionary. Under the Achaemenid Empire, Zoroastrianism became the state religion of the largest empire the world had yet seen.\n\n"
    "Jewish concepts of Satan, angels, resurrection, and apocalypse developed under Persian-Zoroastrian influence. The Magi priesthood gave English the word 'magic' and features in the Christian nativity narrative."
),

"abraham": (
    "Abraham (c. 2000–1800 BCE) is the founding patriarch of Judaism, Christianity, and Islam — making him the most theologically consequential figure in monotheism's history, father of a lineage claiming over 4 billion adherents (55% of humanity).\n\n"
    "Born in Ur of the Chaldees, he received God's call to journey to Canaan, abandoning Mesopotamian polytheism for radical monotheism. God's covenant (Genesis 15, 17) promised land, descendants as numerous as stars, and universal blessing.\n\n"
    "The binding of Isaac (the Akedah, Genesis 22) — where Abraham's willingness to sacrifice his son proved absolute faith — is among world literature's most profound passages. Judaism traces lineage through Isaac; Islam through Ishmael.\n\n"
    "Christianity sees Abraham as the father of faith (Romans 4). His tomb at Machpelah in Hebron is sacred to all three faiths. No single individual's story has shaped more people's understanding of their relationship with God."
),

"homer": (
    "Homer (c. 8th century BCE) was the legendary Greek poet credited as author of the Iliad and the Odyssey — the two foundational works of Western literature and the oldest surviving masterpieces of European poetry.\n\n"
    "The Iliad, set during the Trojan War, explores honor, mortality, and war's human cost in 15,693 lines. The Odyssey recounts Odysseus's ten-year journey home, weaving cunning, fidelity, and homecoming into 12,110 lines. Together they provided Greeks with theology, ethics, and cultural identity.\n\n"
    "Alexander the Great slept with the Iliad under his pillow. The 'Homeric Question' — one poet or many oral tradition bearers? — has been debated since antiquity. Milman Parry's oral-formulaic theory demonstrated the poems' roots in centuries of performance tradition.\n\n"
    "Virgil's Aeneid, Dante's Commedia, Milton's Paradise Lost, and Joyce's Ulysses all descend from Homer. Schliemann's excavation of Troy (1870s), directly inspired by Homer, founded classical archaeology."
),

"cyrus-the-great": (
    "Cyrus the Great (c. 600–530 BCE) founded the Achaemenid Empire — the largest empire the world had yet seen — and was the first ruler to articulate a policy of religious tolerance and human rights, recorded in the Cyrus Cylinder (539 BCE), often called the 'first declaration of human rights.'\n\n"
    "He united Persian and Median tribes, overthrew Media, conquered Lydian Croesus, and captured Babylon by diverting the Euphrates. His treatment of Babylon was revolutionary: he restored temples, honored local gods, and freed captive peoples — including the Jews, permitted to rebuild the Jerusalem Temple.\n\n"
    "For this, the Hebrew Bible uniquely calls a non-Jewish king 'messiah' (Isaiah 45:1). His administrative innovations — satrapies, the Royal Road, postal system, and governance by consent — became the model for all subsequent Near Eastern empires.\n\n"
    "Thomas Jefferson studied Xenophon's Cyropaedia as a governance model. The United Nations displayed the Cyrus Cylinder (1971) as a symbol of human rights."
),

"moses": (
    "Moses (c. 1391–1271 BCE, traditional dating) was the Hebrew prophet, lawgiver, and liberator who led the Israelites out of Egyptian bondage (the Exodus), received the Torah on Mount Sinai, and established the covenant relationship between God and Israel that defines Judaism.\n\n"
    "Found as an infant in a basket on the Nile and raised in Pharaoh's household, he fled after killing an Egyptian taskmaster. At the burning bush (Exodus 3), God commissioned him to confront Pharaoh and deliver Israel. The ten plagues — climaxing in the death of the firstborn and the first Passover — compelled Pharaoh to release the Israelites.\n\n"
    "At Sinai, Moses received the Ten Commandments and the Torah — the foundational legal, ethical, and ritual code of Judaism. He mediated between God and Israel for 40 years of wilderness wandering, organizing twelve tribes into a nation.\n\n"
    "He died within sight of the Promised Land on Mount Nebo. Judaism, Christianity, and Islam honor him as prophet. Western legal tradition from Roman law through the Magna Carta traces its ethical foundations to the Mosaic code."
),

"buddha": (
    "Siddhartha Gautama (c. 563–483 BCE), known as the Buddha ('the Awakened One'), was an Indian spiritual teacher who founded Buddhism — now the world's fourth-largest religion with over 500 million adherents. Born a prince of the Shakya clan in Lumbini (modern Nepal), he renounced royal privilege at age 29.\n\n"
    "After six years of ascetic practice and meditation, he attained enlightenment (bodhi) under the Bodhi tree at Bodh Gaya. His Four Noble Truths diagnosed suffering's cause (craving) and prescribed the Eightfold Path as its cure — a 'Middle Way' between extreme asceticism and sensual indulgence.\n\n"
    "For 45 years he traveled across the Gangetic plain, teaching the Dharma to all castes and establishing the Sangha (monastic community) — one of the world's oldest continuous institutions. His teachings were compiled into the Tripitaka.\n\n"
    "Emperor Ashoka's conversion (c. 260 BCE) transformed Buddhism from a regional movement into a world religion. Zen, Theravada, Mahayana, and Vajrayana traditions carry his teachings from Sri Lanka to Japan."
),

"confucius": (
    "Confucius (Kong Qiu, 551–479 BCE) was a Chinese philosopher, teacher, and political theorist whose ethical system — built on ren (benevolence), li (ritual propriety), and junzi (the exemplary person) — shaped East Asian civilization for 2,500 years and continues to influence over 1.5 billion people.\n\n"
    "Born in the state of Lu during the Spring and Autumn Period, he spent years as a wandering teacher seeking a ruler who would implement his vision of moral governance. His disciples compiled his teachings in the Analerta (Lunyu) — aphorisms on virtue, learning, filial piety, and righteous rule.\n\n"
    "Confucius taught that social harmony flows from moral self-cultivation: a sovereign must govern by virtue, not force. He established the 'Five Relationships' (ruler-subject, parent-child, husband-wife, elder-younger, friend-friend) as society's ethical architecture.\n\n"
    "The imperial examination system, based on Confucian texts, governed Chinese bureaucratic selection for over 1,300 years. His thought permeates East Asian cultures, legal traditions, and family structures to this day."
),

}


# ================================================================
# STEP 2: New enrichments for entities that need it
# ================================================================

NEW_ENRICHMENTS = {

"alexander-the-great": {
    "path": "data/appwrite-export/entities/221-Class-221/221alexander-the-great.json",
    "summary": (
        "Alexander III of Macedon (356–323 BCE) was a military genius and empire-builder who conquered the largest territory of any individual in ancient history — from Greece to Egypt to the borders of India — in just 13 years of relentless campaigning, dying undefeated at age 32.\n\n"
        "Tutored by Aristotle, he inherited Philip II's formidable Macedonian army and crossed the Hellespont in 334 BCE. His victories at Granicus, Issus, and Gaugamela shattered the Persian Empire of Darius III. He founded over 20 cities (most named Alexandria), the greatest being Alexandria in Egypt — the ancient world's intellectual capital.\n\n"
        "His conquests spread Greek language, culture, and philosophy across the Near East and Central Asia, inaugurating the Hellenistic Age — a 300-year cultural fusion of Greek, Persian, Egyptian, and Indian traditions that transformed the ancient world.\n\n"
        "He died in Babylon in 323 BCE (fever, possibly typhoid or poisoning). His empire fractured among his generals (the Diadochi), but the Hellenistic kingdoms they founded carried Greek civilization to the doorstep of China and the banks of the Nile."
    ),
    "causes": [
        "Philip II of Macedon's military reforms (the sarissa phalanx, Companion cavalry) and political unification of Greece created the instrument Alexander inherited",
        "Aristotle's tutoring gave Alexander intellectual ambition, a love of Homer, and the vision of a cosmopolitan empire",
        "The internal weakness of the Achaemenid Persian Empire under Darius III provided the strategic opening for invasion"
    ],
    "effects": [
        "Conquered the largest territory of any individual in antiquity: Greece, Egypt, Persia, Central Asia, and northwest India",
        "Inaugurated the Hellenistic Age — 300 years of Greek-Eastern cultural fusion that shaped the Mediterranean and Near East",
        "Founded Alexandria in Egypt, the ancient world's greatest center of learning (the Library and Museum)",
        "The spread of Greek (Koine) as a lingua franca enabled early Christianity's rapid Mediterranean expansion",
        "His undefeated military record (never lost a battle) made him the benchmark for all subsequent conquerors",
        "The Diadochi Wars and successor kingdoms reshaped the political map from Greece to Afghanistan"
    ],
    "relationships": [
        rel("alexander-the-great", "Alexander the Great", "STUDENT_OF", "aristotle", "Aristotle tutored Alexander from age 13 to 16, shaping his intellectual horizons"),
        rel("alexander-the-great", "Alexander the Great", "SUCCEEDS", "philip-ii-of-macedon", "Inherited Philip II's army and Greek hegemony after his father's assassination (336 BCE)"),
        rel("alexander-the-great", "Alexander the Great", "DEFEATS", "achaemenid-empire", "Destroyed the Achaemenid Persian Empire at Gaugamela (331 BCE)"),
        rel("alexander-the-great", "Alexander the Great", "INFLUENCED_BY", "homer", "Slept with the Iliad under his pillow and modeled himself on Achilles"),
        rel("alexander-the-great", "Alexander the Great", "INFLUENCED_BY", "cyrus-the-great", "Honored Cyrus's tomb at Pasargadae and adopted Persian royal customs"),
        rel("alexander-the-great", "Alexander the Great", "OCCURS_IN", "ancient-greece", "Born in Pella, Macedonia; conquered from Greece to India"),
    ],
    "subjectHeadings": ["People — Conquerors & Military Leaders — Macedon — Classical"],
    "subjects": ["Hellenistic Age", "Macedon", "Persian Empire", "Alexandria", "Conquest", "Gaugamela", "Ancient Greece", "Military Genius", "Diadochi", "Cultural Fusion"],
    "frameworks": ["MILITARY_HISTORY", "CAUSE_AND_EFFECT", "CULTURAL_DIFFUSION", "POLITICAL_SYSTEMS", "SOCIAL_STRUCTURES"],
},

"isaac-newton": {
    "path": "data/appwrite-export/entities/210-Class-210/210isaac-newton.json",
    "summary": (
        "Sir Isaac Newton (1643–1727) was an English mathematician, physicist, and astronomer whose Principia Mathematica (1687) unified terrestrial and celestial mechanics under the law of universal gravitation — the single most important scientific work ever published, laying the foundation for classical physics that stood unchallenged for over 200 years.\n\n"
        "Born prematurely in Woolsthorpe Manor, Lincolnshire, during the English Civil War, he entered Cambridge's Trinity College in 1661. During the 'plague years' (1665–66), he independently developed calculus, discovered the composition of white light through prism experiments, and formulated his theory of gravitation — perhaps the most productive two years in scientific history.\n\n"
        "The Principia's three laws of motion and universal gravitation explained everything from falling apples to planetary orbits.His Opticks revealed light's spectral nature. He served as Warden and Master of the Royal Mint and president of the Royal Society.\n\n"
        "Newton's mechanics enabled the Industrial Revolution, space exploration, and modern engineering. Einstein's relativity superseded his framework only at extreme scales. 'If I have seen further, it is by standing on the shoulders of giants.'"
    ),
    "causes": [
        "The Scientific Revolution (Copernicus, Kepler, Galileo) provided the heliocentric framework and laws of motion that Newton unified into a single mathematical system",
        "The plague closure of Cambridge (1665–66) gave Newton isolation for the most productive period of scientific work in history",
        "Edmond Halley's encouragement and financial support spurred Newton to write and publish the Principia"
    ],
    "effects": [
        "Universal gravitation unified terrestrial and celestial mechanics for the first time, establishing classical physics",
        "Co-invented calculus (independently of Leibniz), the foundational mathematical tool of all modern science and engineering",
        "His three laws of motion became the basis of mechanical engineering and enabled the Industrial Revolution",
        "The Principia's mathematical approach to nature established the model for all subsequent physics",
        "His optical experiments revealed light's spectral composition, founding the science of spectroscopy",
        "Newtonian mechanics enabled modern space travel — Apollo 11's trajectory was calculated using his equations"
    ],
    "relationships": [
        rel("isaac-newton", "Isaac Newton", "BUILDS_ON", "galileo-galilei", "Newton's first law built directly on Galileo's principle of inertia"),
        rel("isaac-newton", "Isaac Newton", "SUPERSEDED_BY", "albert-einstein", "Einstein's relativity superseded Newtonian mechanics at extreme velocities and gravitational fields"),
        rel("isaac-newton", "Isaac Newton", "PUBLISHES", "principia-mathematica", "Published Philosophiæ Naturalis Principia Mathematica (1687), unifying mechanics and gravitation"),
        rel("isaac-newton", "Isaac Newton", "RIVALS", "gottfried-leibniz", "The calculus priority dispute with Leibniz became science's most famous intellectual feud"),
        rel("isaac-newton", "Isaac Newton", "OCCURS_IN", "united-kingdom", "Born in Lincolnshire, taught at Cambridge, served as Master of the Royal Mint in London"),
        rel("isaac-newton", "Isaac Newton", "INFLUENCES", "scientific-revolution", "Completed the Scientific Revolution that Copernicus and Galileo had begun"),
    ],
    "subjectHeadings": ["People — Scientists & Mathematicians — England — Early Modern"],
    "subjects": ["Gravitation", "Calculus", "Principia", "Optics", "Classical Physics", "Laws of Motion", "Scientific Revolution", "Cambridge", "Mathematics", "England"],
    "frameworks": ["INNOVATION_AND_TECHNOLOGY", "CAUSE_AND_EFFECT", "CULTURAL_DIFFUSION", "DOCTRINE_DEVELOPMENT", "SCIENCE_AND_RELIGION"],
},

"napoleon-italy": {
    "path": "data/appwrite-export/entities/220-Class-220/220napoleon-italy.json",
    "summary": (
        "Napoleon Bonaparte (1769–1821) was a Corsican-born French military commander and emperor whose conquests reshaped Europe, spread the ideals of the French Revolution, established the Napoleonic Code, and made him — alongside Caesar and Alexander — one of history's three greatest military figures.\n\n"
        "Rising from minor Corsican nobility through artillery brilliance in the Revolutionary Wars, he seized power in the coup of 18 Brumaire (1799) and crowned himself Emperor in 1804. His Grande Armée won stunning victories at Austerlitz, Jena, and Wagram, dominating continental Europe from Spain to the Russian border.\n\n"
        "The Napoleonic Code (1804) — standardizing civil law, abolishing feudal privilege, and establishing equality before the law — became the legal foundation of over 70 countries. He reorganized German states, abolished the Holy Roman Empire, and sparked the nationalist movements that reshaped 19th-century Europe.\n\n"
        "His catastrophic invasion of Russia (1812) and final defeat at Waterloo (1815) ended the Napoleonic era. Exiled to Saint Helena, he died in 1821. His tomb at Les Invalides in Paris remains France's most visited monument."
    ),
    "name": "Napoleon Bonaparte",
    "causes": [
        "The French Revolution (1789) destroyed the ancien régime and created political chaos that enabled military strongmen to seize power",
        "Napoleon's artillery genius during the Italian campaigns (1796–97) and Egyptian expedition established his military reputation and political ambitions",
        "The weakness and corruption of the Directory government created the opening for the 18 Brumaire coup (1799)"
    ],
    "effects": [
        "The Napoleonic Code (1804) standardized civil law across Europe and became the legal foundation of over 70 countries worldwide",
        "Reorganized the political map of Europe: abolished the Holy Roman Empire, created the Confederation of the Rhine, and sparked 19th-century nationalism",
        "The Napoleonic Wars (1803–1815) killed an estimated 3–6 million people and reshaped European borders at the Congress of Vienna",
        "Spread revolutionary ideals (equality, meritocracy, secularism) across Europe, permanent disrupting aristocratic order",
        "His invasion of Spain triggered independence movements across Latin America (Bolívar, San Martín)",
        "The Continental System's economic warfare inadvertently accelerated British industrial supremacy"
    ],
    "relationships": [
        rel("napoleon-italy", "Napoleon Bonaparte", "PRODUCT_OF", "french-revolution", "Rose to power through the political chaos created by the French Revolution"),
        rel("napoleon-italy", "Napoleon Bonaparte", "INFLUENCES", "simon-bolivar", "Napoleon's invasion of Spain triggered Latin American independence movements"),
        rel("napoleon-italy", "Napoleon Bonaparte", "MODELS_ON", "julius-caesar", "Consciously modeled himself on Caesar — even crowning himself emperor"),
        rel("napoleon-italy", "Napoleon Bonaparte", "MODELS_ON", "charlemagne", "Called himself 'the Charlemagne of the modern era' and revived the imperial ideal"),
        rel("napoleon-italy", "Napoleon Bonaparte", "OPPOSES", "united-kingdom", "The Napoleonic Wars were fundamentally a 22-year struggle against British naval and economic power"),
        rel("napoleon-italy", "Napoleon Bonaparte", "OCCURS_IN", "france", "Born in Corsica, ruled France as First Consul (1799) and Emperor (1804–1814/15)"),
    ],
    "subjectHeadings": ["People — Emperors & Military Leaders — France — Modern"],
    "subjects": ["Napoleonic Code", "French Revolution", "Grande Armée", "Waterloo", "Continental Europe", "Imperial France", "Military Strategy", "Nationalism", "Legal Reform", "France"],
    "frameworks": ["MILITARY_HISTORY", "CAUSE_AND_EFFECT", "POLITICAL_SYSTEMS", "LEGAL_INTERPRETATION", "CULTURAL_DIFFUSION"],
},

"joan-of-arc": {
    "path": "data/appwrite-export/entities/204-Class-204/204joan-of-arc.json",
    "summary": (
        "Joan of Arc (Jeanne d'Arc, c. 1412–1431) was a French peasant girl who, claiming divine visions from Saints Michael, Catherine, and Margaret, led the French army to a series of victories during the Hundred Years' War — turning the tide of the conflict and enabling the coronation of Charles VII.\n\n"
        "Born in Domrémy, she convinced the Dauphin to give her command of troops at age 17. Her relief of the Siege of Orléans (May 1429) — accomplished in just nine days — was the war's decisive turning point, earning her the epithet 'the Maid of Orléans.'\n\n"
        "Captured by Burgundian forces, sold to the English, and tried by a pro-English ecclesiastical court, she was convicted of heresy and burned at the stake in Rouen on May 30, 1431, at age 19. She maintained her faith and her voices to the end.\n\n"
        "Rehabilitated by the Church in 1456 and canonized as a saint in 1920, she became France's greatest national heroine and an enduring symbol of courage, faith, and female empowerment — inspiring figures from Napoleon to Simone de Beauvoir."
    ),
    "causes": [
        "The Hundred Years' War's devastating French losses (Agincourt, Treaty of Troyes) and English occupation of northern France created a desperate need for a morale-galvanizing figure",
        "Joan's mystical visions from Saints Michael, Catherine, and Margaret compelled her to seek out the Dauphin and offer military service",
        "The weakness of the Dauphin Charles VII and the fractured French political landscape opened space for an unconventional savior figure"
    ],
    "effects": [
        "The relief of Orléans (1429) reversed the Hundred Years' War's momentum, beginning the French reconquest",
        "Enabled the coronation of Charles VII at Reims (July 1429), legitimizing the French monarchy",
        "Her trial and execution (1431) became one of history's most infamous miscarriages of justice, later overturned by papal tribunal (1456)",
        "Canonized as a Catholic saint (1920), she became France's patron saint and ultimate national symbol",
        "Her story challenged medieval gender norms and became a foundational narrative for women's empowerment",
        "Inspired centuries of literature, art, and music: Shakespeare, Schiller, Twain, Shaw, and Anouilh all dramatized her life"
    ],
    "relationships": [
        rel("joan-of-arc", "Joan of Arc", "LEADS", "siege-of-orleans", "Led the French army to relieve the Siege of Orléans in 9 days (May 1429)"),
        rel("joan-of-arc", "Joan of Arc", "CROWNS", "charles-vii", "Enabled Charles VII's coronation at Reims Cathedral (July 1429)"),
        rel("joan-of-arc", "Joan of Arc", "OCCURS_IN", "hundred-years-war", "Fought during the critical phase of the Hundred Years' War (1429–1431)"),
        rel("joan-of-arc", "Joan of Arc", "OCCURS_IN", "france", "Born in Domrémy, fought across northern France, burned at Rouen"),
        rel("joan-of-arc", "Joan of Arc", "CANONIZED_BY", "catholic-church", "Canonized as a saint in 1920 by Pope Benedict XV"),
    ],
    "subjectHeadings": ["People — Military Leaders & Saints — France — Medieval"],
    "subjects": ["Hundred Years' War", "Orléans", "France", "Visions", "Martyrdom", "Canonization", "Female Leadership", "Medieval", "Heresy Trial", "Charles VII"],
    "frameworks": ["MILITARY_HISTORY", "CAUSE_AND_EFFECT", "RELIGIOUS_INSTITUTIONS", "GENDER_AND_SOCIETY", "CULTURAL_DIFFUSION"],
},

"christopher-columbus": {
    "path": "data/appwrite-export/entities/240-Class-240/240christopher-columbus.json",
    "summary": (
        "Christopher Columbus (1451–1506) was a Genoese navigator whose four transatlantic voyages (1492–1504), funded by Spain's Ferdinand and Isabella, initiated sustained European contact with the Americas — the most consequential encounter between civilizations in human history.\n\n"
        "Convinced he could reach Asia by sailing west (underestimating Earth's circumference by 25%), he landed in the Bahamas on October 12, 1492 — a date that reshaped every aspect of global history. He explored Cuba, Hispaniola, and parts of Central and South America across four voyages.\n\n"
        "The 'Columbian Exchange' that followed transformed biology, agriculture, and demographics worldwide: Europe received potatoes, maize, tomatoes, and tobacco; the Americas received horses, cattle, wheat — and devastating diseases (smallpox, measles) that killed an estimated 90% of indigenous populations.\n\n"
        "His legacy is deeply contested: celebrated as a bold explorer who connected hemispheres, condemned for initiating the colonization, enslavement, and decimation of indigenous peoples. He never realized he had reached a 'New World,' dying still believing he had found a route to Asia."
    ),
    "causes": [
        "The fall of Constantinople (1453) and Ottoman control of overland trade routes created economic incentive to find alternative sea routes to Asia",
        "Portuguese advances in navigation (Prince Henry, Bartolomeu Dias) and Spanish Reconquista completion (1492) created the maritime and political context",
        "Columbus's underestimation of Earth's size and overestimation of Asia's eastern extent convinced him a westward voyage was feasible"
    ],
    "effects": [
        "Initiated sustained European contact with the Americas, permanently connecting the world's hemispheres",
        "The Columbian Exchange transformed global agriculture and biology — potatoes, maize, and tomatoes reshaped European and Asian diets",
        "European diseases (smallpox, measles) killed an estimated 90% of indigenous American populations — the largest demographic catastrophe in history",
        "Triggered the Spanish colonization of the Americas, the transatlantic slave trade, and five centuries of European global dominance",
        "His four voyages launched the Age of Exploration and the creation of the first truly global economy",
        "The 'discovery' narrative became deeply contested in the context of indigenous rights and colonial legacy"
    ],
    "relationships": [
        rel("christopher-columbus", "Christopher Columbus", "FUNDED_BY", "ferdinand-and-isabella", "Ferdinand II and Isabella I of Spain funded his 1492 voyage after years of lobbying"),
        rel("christopher-columbus", "Christopher Columbus", "INITIATES", "columbian-exchange", "His voyages initiated the biological, agricultural, and demographic exchange between hemispheres"),
        rel("christopher-columbus", "Christopher Columbus", "OCCURS_IN", "spain", "Sailed under the Spanish flag, commissioned by the Spanish Crown"),
        rel("christopher-columbus", "Christopher Columbus", "OCCURS_IN", "caribbean", "First landfall: Bahamas (Oct 12, 1492); explored Cuba, Hispaniola, Central/South America"),
        rel("christopher-columbus", "Christopher Columbus", "INFLUENCED_BY", "marco-polo", "Columbus owned a heavily annotated copy of Marco Polo's Travels, which inspired his westward voyage"),
    ],
    "subjectHeadings": ["People — Explorers & Navigators — Italy/Spain — Early Modern"],
    "subjects": ["Age of Exploration", "Columbian Exchange", "Americas", "Navigation", "Spain", "1492", "Colonization", "Transatlantic", "Indigenous Peoples", "New World"],
    "frameworks": ["CULTURAL_DIFFUSION", "CAUSE_AND_EFFECT", "TRADE_AND_EXCHANGE", "POLITICAL_SYSTEMS", "ENVIRONMENTAL_HISTORY"],
},

"karl-marx": {
    "path": "data/appwrite-export/entities/202-Class-202/202karl-marx.json",
    "summary": (
        "Karl Marx (1818–1883) was a German philosopher, economist, and revolutionary whose analysis of capitalism, theory of historical materialism, and vision of communist society made him the most influential social thinker of the modern era — his ideas shaped the politics of over one-third of humanity in the 20th century.\n\n"
        "Born in Trier, Prussia, to a Jewish family that converted to Protestantism, he studied law and philosophy before turning to radical journalism. Expelled from Germany and France, he settled in London (1849), where he spent decades in the British Museum researching Das Kapital.\n\n"
        "With Friedrich Engels, he published The Communist Manifesto (1848), declaring that 'the history of all hitherto existing society is the history of class struggles.' Das Kapital (1867) analyzed capitalism's internal contradictions — surplus value extraction, the tendency of the rate of profit to fall, and recurring crises.\n\n"
        "His ideas inspired the Russian Revolution (1917), the Chinese Revolution (1949), and socialist movements worldwide. Whether as inspiration or cautionary tale, Marx's analysis of inequality, alienation, and capitalism's dynamics remains central to 21st-century political and economic debate."
    ),
    "causes": [
        "The Industrial Revolution's brutal factory conditions, child labor, and urban poverty created the material conditions Marx analyzed",
        "Hegel's dialectical philosophy provided the intellectual framework Marx 'turned upside down' into historical materialism",
        "The failure of the 1848 European revolutions radicalized Marx and demonstrated the need for systematic revolutionary theory"
    ],
    "effects": [
        "Historical materialism and class analysis became foundational frameworks in sociology, political science, and economics",
        "The Communist Manifesto (1848) and Das Kapital (1867) became the theoretical foundation of socialist and communist movements worldwide",
        "Directly inspired the Russian Revolution (1917), Chinese Revolution (1949), and Cuban Revolution (1959)",
        "Marxist-Leninist states governed over one-third of humanity during the Cold War era",
        "His critique of alienation and commodity fetishism continues to influence 21st-century debates about inequality and technology",
        "Both supporters and critics engage with Marx — making him the most discussed social thinker in modern intellectual history"
    ],
    "relationships": [
        rel("karl-marx", "Karl Marx", "COLLABORATES_WITH", "frederick-engels", "Engels co-authored the Communist Manifesto and financially supported Marx's research for decades"),
        rel("karl-marx", "Karl Marx", "AUTHORS", "das-kapital", "Published Das Kapital Vol. 1 (1867) — his masterwork analyzing capitalism's internal contradictions"),
        rel("karl-marx", "Karl Marx", "AUTHORS", "communist-manifesto", "Co-wrote The Communist Manifesto (1848) with Engels — 'Workers of the world, unite!'"),
        rel("karl-marx", "Karl Marx", "INFLUENCES", "russian-revolution", "Marxist theory became the ideological foundation of the Bolshevik Revolution (1917)"),
        rel("karl-marx", "Karl Marx", "BUILDS_ON", "hegel", "Inverted Hegel's idealist dialectic into 'dialectical materialism'"),
        rel("karl-marx", "Karl Marx", "OCCURS_IN", "united-kingdom", "Lived in London from 1849 until death, researching at the British Museum"),
    ],
    "subjectHeadings": ["People — Philosophers & Economists — Germany/UK — Modern"],
    "subjects": ["Communism", "Das Kapital", "Class Struggle", "Historical Materialism", "Capitalism", "Revolution", "Socialism", "Alienation", "Political Economy", "Industrial Revolution"],
    "frameworks": ["POLITICAL_SYSTEMS", "CAUSE_AND_EFFECT", "SOCIAL_STRUCTURES", "DOCTRINE_DEVELOPMENT", "TRADE_AND_EXCHANGE"],
},

"thomas-jefferson": {
    "path": "data/appwrite-export/entities/201-Class-201/201thomas-jefferson.json",
    "summary": (
        "Thomas Jefferson (1743–1826) was the principal author of the Declaration of Independence, third President of the United States (1801–1809), and one of the most intellectually gifted of the Founding Fathers — an architect, scientist, philosopher, diplomat, and slaveholder whose contradictions mirror America's own.\n\n"
        "His Declaration (1776) — 'We hold these truths to be self-evident, that all men are created equal' — articulated the philosophical foundation of American democracy and inspired democratic revolutions worldwide. As president, he purchased Louisiana from Napoleon (1803), doubling the nation's size.\n\n"
        "He founded the University of Virginia, designed Monticello, championed religious freedom (Virginia Statute for Religious Freedom), and amassed the library that became the Library of Congress. His Notes on the State of Virginia remains a masterwork of Enlightenment natural history.\n\n"
        "Yet he enslaved over 600 people across his lifetime and fathered children with Sally Hemings. His legacy embodies America's foundational tension between democratic ideals and the institution of slavery."
    ),
    "causes": [
        "Enlightenment philosophy (Locke, Montesquieu, Scottish moral sense theory) provided the intellectual framework Jefferson translated into America's founding documents",
        "British colonial overreach (taxation, Coercive Acts) created the political crisis that required a Declaration of Independence",
        "Virginia's planter aristocracy class produced educated, politically engaged men who led the independence movement"
    ],
    "effects": [
        "The Declaration of Independence (1776) provided the philosophical foundation for American democracy and inspired revolutions worldwide",
        "The Louisiana Purchase (1803) doubled US territory, opening the continent to westward expansion",
        "The Virginia Statute for Religious Freedom (1786) established the principle of church-state separation that became the First Amendment",
        "Founded the University of Virginia (1819), the first American university designed around secular education",
        "His personal library (6,487 volumes) became the foundation of the Library of Congress — the world's largest library",
        "His contradictions as a slaveholder who wrote 'all men are created equal' define America's ongoing reckoning with race"
    ],
    "relationships": [
        rel("thomas-jefferson", "Thomas Jefferson", "AUTHORS", "declaration-of-independence", "Principal author of the Declaration of Independence (1776)"),
        rel("thomas-jefferson", "Thomas Jefferson", "CONTEMPORARY_OF", "george-washington", "Served as Washington's Secretary of State and succeeded him as a Founding Father of the Republic"),
        rel("thomas-jefferson", "Thomas Jefferson", "INFLUENCES", "abraham-lincoln", "Lincoln invoked Jefferson's 'all men are created equal' to justify emancipation"),
        rel("thomas-jefferson", "Thomas Jefferson", "OCCURS_IN", "united-states", "Born in Virginia, served as president from 1801–1809, died at Monticello"),
        rel("thomas-jefferson", "Thomas Jefferson", "PURCHASES", "louisiana-territory", "Purchased Louisiana from Napoleon (1803), doubling US territory"),
        rel("thomas-jefferson", "Thomas Jefferson", "FOUNDS", "university-of-virginia", "Founded the University of Virginia (1819) as a secular institution of higher learning"),
    ],
    "subjectHeadings": ["People — Presidents & Thinkers — USA — Early Modern"],
    "subjects": ["Declaration of Independence", "Louisiana Purchase", "Founding Fathers", "Virginia", "Monticello", "Religious Freedom", "Enlightenment", "Library of Congress", "Slavery", "United States"],
    "frameworks": ["POLITICAL_SYSTEMS", "CAUSE_AND_EFFECT", "ETHICAL_FRAMEWORK", "CULTURAL_DIFFUSION", "SOCIAL_STRUCTURES"],
},

"paul-the-apostle": {
    "path": "data/appwrite-export/entities/252-Class-252/252paul-the-apostle.json",
    "summary": (
        "Paul the Apostle (c. 5–64 CE), born Saul of Tarsus, was a Pharisee-turned-apostle whose missionary journeys, theological letters, and radical inclusion of Gentiles transformed Christianity from a Jewish sect into a universal world religion — making him, after Jesus, the most influential figure in Christian history.\n\n"
        "A Roman citizen and Pharisaic scholar, he initially persecuted Christians. His dramatic conversion on the Damascus road (c. 33 CE) — a blinding light and the risen Christ's voice — redirected his life. He undertook three missionary journeys across Asia Minor, Greece, and the Mediterranean, founding churches in Corinth, Ephesus, Philippi, and Thessalonica.\n\n"
        "His 13 epistles (Romans, Corinthians, Galatians, etc.) constitute nearly half the New Testament and developed Christianity's core doctrines: justification by faith, the body of Christ (the Church), grace transcending law, and the equality of Jew and Gentile, slave and free, male and female (Galatians 3:28).\n\n"
        "Tradition holds he was beheaded in Rome under Nero (c. 64 CE). His theology shaped Augustine, Luther, Calvin, Wesley, and every subsequent Christian thinker. Romans alone has launched more theological revolutions than any other text."
    ),
    "causes": [
        "The early Church's explosive growth in Jerusalem and the question of Gentile inclusion created the theological crisis Paul resolved",
        "His Pharisaic education under Gamaliel and Roman citizenship uniquely equipped him to bridge Jewish and Greco-Roman worlds",
        "His Damascus road conversion experience (c. 33 CE) redirected him from persecutor to Christianity's greatest missionary"
    ],
    "effects": [
        "Transformed Christianity from a Jewish sect into a universal religion by arguing that Gentiles need not follow Mosaic Law",
        "His epistles developed core Christian doctrines: justification by faith, grace, the Church as Christ's body, and spiritual gifts",
        "Founded Christian communities across the Roman Empire that became the organizational foundation of the early Church",
        "His letter to the Romans became the theological foundation of Augustine's, Luther's, and Calvin's reformations",
        "Galatians 3:28 ('neither Jew nor Gentile, slave nor free, male nor female') became a foundational text for equality movements",
        "His method of writing pastoral letters to distant congregations established the epistle as a Christian literary form"
    ],
    "relationships": [
        rel("paul-the-apostle", "Paul the Apostle", "COMMISSIONED_BY", "jesus-christ", "The risen Christ commissioned Paul on the Damascus road (Acts 9)"),
        rel("paul-the-apostle", "Paul the Apostle", "INFLUENCES", "martin-luther", "Luther's reading of Romans (justification by faith) ignited the Protestant Reformation"),
        rel("paul-the-apostle", "Paul the Apostle", "AUTHORS", "epistle-to-the-romans", "The Epistle to the Romans — Christianity's most influential theological document"),
        rel("paul-the-apostle", "Paul the Apostle", "OCCURS_IN", "roman-empire", "Traveled and preached across the Roman Empire from Jerusalem to Rome"),
        rel("paul-the-apostle", "Paul the Apostle", "CONTEMPORARY_OF", "peter-the-apostle", "Both apostles led the early Church; tradition says both martyred in Rome under Nero"),
    ],
    "subjectHeadings": ["People — Apostles & Missionaries — Roman Empire — Classical"],
    "subjects": ["Christianity", "Epistles", "Gentile Mission", "Justification by Faith", "Damascus Road", "Roman Empire", "Apostle", "Theology", "Missionary Journeys", "New Testament"],
    "frameworks": ["DOCTRINE_DEVELOPMENT", "CAUSE_AND_EFFECT", "CULTURAL_DIFFUSION", "RELIGIOUS_INSTITUTIONS", "ETHICAL_FRAMEWORK"],
},

"david": {
    "path": "data/appwrite-export/entities/762-Class-762/762david.json",
    "summary": (
        "King David (c. 1040–970 BCE) was the second king of Israel, warrior, poet, and central figure of the Hebrew Bible whose reign united the twelve tribes, established Jerusalem as the capital, and founded the royal dynasty from which Judaism and Christianity expected the Messiah.\n\n"
        "A shepherd from Bethlehem, he entered history by slaying the Philistine giant Goliath (1 Samuel 17). As Saul's court musician and warrior, then fugitive, then king of Judah, he gradually united all Israel under his rule. His conquest of Jerusalem from the Jebusites created the political and spiritual capital of the Jewish people.\n\n"
        "Tradition attributes 73 of the 150 Psalms to David — some of the most beautiful poetry in world literature. His reign is remembered as Israel's golden age, yet the Bible unflinchingly records his moral failures: adultery with Bathsheba, the murder of Uriah, and family tragedies.\n\n"
        "God's covenant with David (2 Samuel 7) — promising his dynasty would endure forever — became the theological foundation for Messianic expectation. Christianity identifies Jesus as 'Son of David,' fulfilling this covenant."
    ),
    "causes": [
        "The failure of King Saul's reign and Israel's need for a unifying king who could defeat the Philistines created the political vacuum David filled",
        "The Philistine military threat to Israel's survival required a capable warrior-king",
        "Samuel's prophetic anointing of David as God's chosen king (1 Samuel 16) initiated his path to the throne"
    ],
    "effects": [
        "United the twelve tribes of Israel into a single kingdom with Jerusalem as its eternal capital",
        "The Davidic covenant (2 Samuel 7) established the Messianic expectation that shaped Judaism and Christianity for 3,000 years",
        "The Psalms attributed to David became the most widely used worship literature in human history",
        "Jerusalem as 'the City of David' became sacred to Judaism, Christianity, and Islam",
        "His dynasty ruled Judah for over 400 years (c. 1000–586 BCE) — the longest royal line in Israelite history",
        "Christianity identifies Jesus as 'Son of David,' tracing his genealogy through David to fulfill Messianic prophecy"
    ],
    "relationships": [
        rel("david", "King David", "SUCCEEDS", "saul", "Became king of Israel after Saul's death, uniting the twelve tribes"),
        rel("david", "King David", "ANCESTOR_OF", "solomon", "Solomon succeeded David and built the First Temple in Jerusalem"),
        rel("david", "King David", "ANCESTOR_OF", "jesus-christ", "Jesus identified as 'Son of David' in the Messianic genealogy (Matthew 1:1)"),
        rel("david", "King David", "DESCENDANT_OF", "abraham", "David fulfilled the Abrahamic promise of a great nation and blessed lineage"),
        rel("david", "King David", "OCCURS_IN", "ancient-israel", "Ruled united Israel from Jerusalem (c. 1010–970 BCE)"),
        rel("david", "King David", "CAPTURES", "jerusalem", "Conquered Jerusalem from the Jebusites, making it Israel's eternal capital"),
    ],
    "subjectHeadings": ["People — Kings & Rulers — Israel — Classical"],
    "subjects": ["Kingdom of Israel", "Jerusalem", "Psalms", "Davidic Covenant", "Messiah", "Goliath", "Bethlehem", "Hebrew Bible", "Warrior-King", "Ancient Israel"],
    "frameworks": ["POLITICAL_SYSTEMS", "CAUSE_AND_EFFECT", "DOCTRINE_DEVELOPMENT", "CULTURAL_DIFFUSION", "RELIGIOUS_INSTITUTIONS"],
},

"solomon": {
    "path": "data/appwrite-export/entities/221-Class-221/221solomon.json",
    "summary": (
        "King Solomon (c. 990–931 BCE) was the third king of Israel, son of David and Bathsheba, whose legendary wisdom, vast wealth, international diplomacy, and construction of the First Temple in Jerusalem made his reign the apex of ancient Israel's power and cultural achievement.\n\n"
        "God offered Solomon anything he wished; he chose wisdom. His judgment between two mothers claiming the same child (1 Kings 3:16–28) became the archetypal story of wise adjudication. Tradition attributes Proverbs, Ecclesiastes, and the Song of Solomon to him — three books spanning wisdom literature, existential philosophy, and love poetry.\n\n"
        "He built the First Temple (c. 957 BCE) — the central sanctuary of Israelite worship — and a magnificent palace complex. His trade networks extended from Ophir (gold) to Tarshish (silver), and his alliance with Hiram of Tyre and the Queen of Sheba's visit demonstrated Israel's international prestige.\n\n"
        "Yet his 700 wives and 300 concubines (many from foreign alliances) led him into idolatry. After his death, the kingdom split into Israel and Judah — a division that defined Jewish history for centuries."
    ),
    "causes": [
        "David's military conquests and political unification created the stable, prosperous kingdom Solomon inherited",
        "The Davidic covenant's promise of an enduring dynasty provided religious legitimacy for Solomon's reign",
        "Strategic marriages with foreign princesses secured diplomatic alliances but introduced foreign religious practices"
    ],
    "effects": [
        "Built the First Temple in Jerusalem (c. 957 BCE), the central sanctuary of Israelite worship for 370 years",
        "His legendary wisdom made 'the wisdom of Solomon' a universal proverb and inspired three biblical books",
        "Israel reached its territorial and economic peak under his reign — controlling trade routes from Egypt to Mesopotamia",
        "His foreign alliances and polygamy introduced idolatry that provoked the prophetic critique leading to the kingdom's division",
        "The division of the kingdom after his death (c. 931 BCE) into Israel and Judah shaped all subsequent Jewish history",
        "The First Temple's destruction (586 BCE) and the hope for its rebuilding became central to Jewish identity and Messianic hope"
    ],
    "relationships": [
        rel("solomon", "King Solomon", "SON_OF", "david", "Succeeded his father David as king and fulfilled the promise to build the Temple"),
        rel("solomon", "King Solomon", "BUILDS", "first-temple", "Built the First Temple in Jerusalem (c. 957 BCE), Israel's central sanctuary"),
        rel("solomon", "King Solomon", "OCCURS_IN", "ancient-israel", "Ruled united Israel at its territorial and economic peak"),
        rel("solomon", "King Solomon", "ALLIED_WITH", "hiram-of-tyre", "Alliance with Hiram of Tyre provided materials and craftsmen for the Temple"),
        rel("solomon", "King Solomon", "VISITED_BY", "queen-of-sheba", "The Queen of Sheba's visit to test Solomon's wisdom demonstrated Israel's international prestige"),
    ],
    "subjectHeadings": ["People — Kings & Rulers — Israel — Classical"],
    "subjects": ["First Temple", "Wisdom", "Jerusalem", "Proverbs", "Ecclesiastes", "Song of Solomon", "Ancient Israel", "Trade", "Queen of Sheba", "Kingdom Division"],
    "frameworks": ["POLITICAL_SYSTEMS", "CAUSE_AND_EFFECT", "DOCTRINE_DEVELOPMENT", "TRADE_AND_EXCHANGE", "RELIGIOUS_INSTITUTIONS"],
},

"hannibal": {
    "path": "data/appwrite-export/entities/280-Class-280/280hannibal.json",
    "summary": (
        "Hannibal Barca (247–183 BCE) was a Carthaginian general whose crossing of the Alps with war elephants and tactical masterpiece at the Battle of Cannae made him Rome's greatest enemy and one of the finest military commanders in history.\n\n"
        "Son of Hamilcar Barca, who made young Hannibal swear eternal enmity to Rome, he launched the Second Punic War (218–201 BCE) by marching an army of 50,000 soldiers and 37 elephants from Spain across the Pyrenees, through Gaul, and over the Alps in winter — one of military history's most audacious feats.\n\n"
        "At Cannae (216 BCE), he annihilated a Roman army of 86,000 in a double-envelopment maneuver that killed 50,000–70,000 Romans in a single day — the worst defeat in Roman history and a battle still studied at every military academy worldwide.\n\n"
        "He campaigned in Italy for 15 years without major defeat but could never capture Rome itself. Recalled to Africa, he was finally defeated by Scipio Africanus at Zama (202 BCE). He spent his final years advising Rome's enemies before taking poison. Napoleon, Wellington, and Patton all studied his campaigns."
    ),
    "causes": [
        "Carthage's loss in the First Punic War (264–241 BCE) and Rome's seizure of Sardinia and Corsica created the desire for revenge that Hamilcar instilled in young Hannibal",
        "The Barcid family's conquest of Spain (237–219 BCE) provided Hannibal with the army, treasury, and staging ground for invading Italy",
        "Rome's aggressive expansion into Carthaginian spheres of influence made renewed conflict inevitable"
    ],
    "effects": [
        "The Battle of Cannae (216 BCE) — 50,000–70,000 Romans killed in one day — became the supreme example of tactical destruction by double envelopment",
        "15 years of campaigning in Italy devastated the Italian countryside and demonstrated that Rome could be beaten on its own soil",
        "Rome's eventual victory transformed it from a regional Italian power to the dominant Mediterranean empire",
        "His campaigns forced Rome to develop the strategic doctrine of attrition warfare (Fabian strategy) that influenced all subsequent military thought",
        "The destruction of Carthage (146 BCE) in the Third Punic War resulted partly from the trauma Hannibal inflicted on Rome",
        "Military academies worldwide still study Cannae as the textbook example of the battle of annihilation"
    ],
    "relationships": [
        rel("hannibal", "Hannibal Barca", "OPPOSES", "roman-republic", "Rome's greatest enemy during the Second Punic War (218–201 BCE)"),
        rel("hannibal", "Hannibal Barca", "DEFEATED_BY", "scipio-africanus", "Scipio defeated Hannibal at Zama (202 BCE), ending the Second Punic War"),
        rel("hannibal", "Hannibal Barca", "OCCURS_IN", "carthage", "Carthaginian general, son of Hamilcar Barca"),
        rel("hannibal", "Hannibal Barca", "CROSSES", "alps", "Led 50,000 soldiers and 37 elephants across the Alps in winter (218 BCE)"),
        rel("hannibal", "Hannibal Barca", "WINS", "battle-of-cannae", "Cannae (216 BCE): double envelopment destroyed 86,000 Romans — worst Roman defeat in history"),
        rel("hannibal", "Hannibal Barca", "INFLUENCES", "napoleon-italy", "Napoleon studied Hannibal's Alpine crossing and tactical brilliance extensively"),
    ],
    "subjectHeadings": ["People — Military Commanders — Carthage — Classical"],
    "subjects": ["Second Punic War", "Cannae", "Alpine Crossing", "Carthage", "Rome", "War Elephants", "Military Genius", "Zama", "Mediterranean", "Tactics"],
    "frameworks": ["MILITARY_HISTORY", "CAUSE_AND_EFFECT", "POLITICAL_SYSTEMS", "CULTURAL_DIFFUSION", "TRADE_AND_EXCHANGE"],
},

"sun-tzu": {
    "path": "data/appwrite-export/entities/210-Class-210/210sun-tzu.json",
    "summary": (
        "Sun Tzu (c. 544–496 BCE) was a Chinese military strategist and philosopher traditionally credited as author of The Art of War — the most influential treatise on military strategy ever written, studied by commanders, executives, and strategists for 2,500 years.\n\n"
        "Believed to have served as a general under King Helü of Wu during the Spring and Autumn period, his historical existence is debated. What is certain is that The Art of War's 13 chapters distill warfare into timeless principles: 'All warfare is based on deception,' 'The supreme art of war is to subdue the enemy without fighting,' and 'Know the enemy and know yourself; in a hundred battles you will never be in peril.'\n\n"
        "The text emphasizes intelligence, flexibility, psychological warfare, and avoiding prolonged conflict. It treats war as an extension of statecraft, advocating strategic calculation over brute force — a philosophy that anticipated modern concepts of asymmetric warfare, information operations, and deterrence theory.\n\n"
        "Every major military tradition has adopted Sun Tzu: Napoleon, Mao Zedong, Ho Chi Minh, and Norman Schwarzkopf all cited him. In the 21st century, The Art of War is required reading at West Point, studied in business schools worldwide, and has sold over 100 million copies."
    ),
    "causes": [
        "The Spring and Autumn period's constant interstate warfare among Chinese states created the demand for systematic military theory",
        "Confucian and Daoist philosophical traditions emphasizing harmony, adaptation, and strategic thinking influenced Sun Tzu's approach",
        "King Helü of Wu's ambition to dominate rival states provided the patron and context for Sun Tzu's military service"
    ],
    "effects": [
        "The Art of War became the most influential military treatise in history, studied continuously for 2,500 years",
        "His principle 'subdue the enemy without fighting' anticipates modern concepts of deterrence, soft power, and information warfare",
        "Chinese, Japanese, Korean, and Vietnamese military traditions adopted his principles as foundational doctrine",
        "20th-century leaders (Mao, Ho Chi Minh, Giáp) applied Sun Tzu's guerrilla principles to defeat conventionally superior forces",
        "The text crossed into business strategy in the 1980s, becoming a bestseller in corporate management literature",
        "Required reading at Western military academies (West Point, Sandhurst) alongside Clausewitz's On War"
    ],
    "relationships": [
        rel("sun-tzu", "Sun Tzu", "AUTHORS", "the-art-of-war", "Traditionally credited with writing The Art of War — 13 chapters of military strategy"),
        rel("sun-tzu", "Sun Tzu", "INFLUENCES", "napoleon-italy", "Napoleon reportedly studied Sun Tzu's principles of deception and maneuver"),
        rel("sun-tzu", "Sun Tzu", "INFLUENCES", "mao-zedong", "Mao's guerrilla warfare doctrine drew heavily on Sun Tzu's principles"),
        rel("sun-tzu", "Sun Tzu", "CONTEMPORARY_OF", "confucius", "Both lived during the Spring and Autumn period in 6th–5th century BCE China"),
        rel("sun-tzu", "Sun Tzu", "OCCURS_IN", "ancient-china", "Served (traditionally) as general under King Helü of Wu during the Spring and Autumn period"),
    ],
    "subjectHeadings": ["People — Military Strategists — China — Classical"],
    "subjects": ["The Art of War", "Military Strategy", "Deception", "Ancient China", "Spring and Autumn", "Wu", "Asymmetric Warfare", "Sun Tzu", "Statecraft", "Philosophy"],
    "frameworks": ["MILITARY_HISTORY", "CAUSE_AND_EFFECT", "POLITICAL_SYSTEMS", "CULTURAL_DIFFUSION", "DOCTRINE_DEVELOPMENT"],
},

"william-shakespeare": {
    "path": "data/appwrite-export/entities/262-Class-262/262william-shakespeare.json",
    "summary": (
        "William Shakespeare (1564–1616) was an English playwright, poet, and actor whose 37 plays, 154 sonnets, and narrative poems constitute the greatest body of work in the English language — and arguably in all of world literature.\n\n"
        "Born in Stratford-upon-Avon to a glove-maker, he married Anne Hathaway at 18, then appeared in London's theatrical scene by 1592. Writing for the Lord Chamberlain's Men (later the King's Men) at the Globe Theatre, he produced tragedies (Hamlet, Macbeth, King Lear, Othello), comedies (A Midsummer Night's Dream, Twelfth Night), histories (Henry V, Richard III), and romances (The Tempest).\n\n"
        "He invented over 1,700 words still used in English (assassination, lonely, generous, eyeball), coined phrases that became common speech ('break the ice,' 'wild goose chase,' 'heart of gold'), and explored the full range of human experience with unmatched psychological depth.\n\n"
        "The First Folio (1623), compiled by his colleagues seven years after his death, preserved 18 plays that would otherwise have been lost. Ben Jonson's tribute — 'He was not of an age, but for all time' — has proven prophetic: Shakespeare is the most performed, translated, and studied author in human history."
    ),
    "causes": [
        "The Elizabethan theatrical boom — public playhouses, royal patronage, and a literate urban audience — created the conditions for Shakespeare's career",
        "The English Renaissance's rediscovery of classical literature (Ovid, Plutarch, Seneca) provided the source material he transformed",
        "London's explosive growth and social diversity provided the human material for his unmatched understanding of character"
    ],
    "effects": [
        "Created the greatest body of work in the English language: 37 plays that define Western drama's canon",
        "Invented over 1,700 English words and countless phrases that remain in everyday use 400+ years later",
        "His plays' psychological depth — Hamlet's indecision, Lear's madness, Othello's jealousy — established the modern understanding of character",
        "The First Folio (1623) preserved 18 plays that would otherwise be lost, becoming the most important book in English literature",
        "Shakespeare is the most performed, translated, and studied author in world history — staged in every country on Earth",
        "His influence on the English language is second only to the King James Bible"
    ],
    "relationships": [
        rel("william-shakespeare", "William Shakespeare", "CONTEMPORARY_OF", "galileo-galilei", "Both born in 1564: Shakespeare transformed literature as Galileo transformed science"),
        rel("william-shakespeare", "William Shakespeare", "INFLUENCED_BY", "homer", "Drew on classical sources (Troilus and Cressida from Homer's Iliad tradition)"),
        rel("william-shakespeare", "William Shakespeare", "AUTHORS", "hamlet", "Hamlet (c. 1600) — the most performed and analyzed play in world literature"),
        rel("william-shakespeare", "William Shakespeare", "OCCURS_IN", "england", "Born in Stratford-upon-Avon, wrote for London's Globe Theatre, died in Stratford"),
        rel("william-shakespeare", "William Shakespeare", "INFLUENCES", "english-language", "Invented 1,700+ words and countless idioms that shaped modern English"),
    ],
    "subjectHeadings": ["People — Playwrights & Poets — England — Early Modern"],
    "subjects": ["Drama", "English Literature", "Globe Theatre", "Hamlet", "Sonnets", "First Folio", "Elizabethan", "Poetry", "Tragedy", "Comedy"],
    "frameworks": ["CULTURAL_DIFFUSION", "CAUSE_AND_EFFECT", "SOCIAL_STRUCTURES", "LITERARY_TRADITION", "DOCTRINE_DEVELOPMENT"],
},

"marco-polo": {
    "path": "data/appwrite-export/entities/202-Class-202/202marco-polo.json",
    "summary": (
        "Marco Polo (1254–1324) was a Venetian merchant and explorer whose 24-year journey along the Silk Road to the court of Kublai Khan in China produced The Travels of Marco Polo — the work that introduced Europe to the wonders of East Asia and inspired the Age of Exploration.\n\n"
        "Departing Venice at age 17 with his father Niccolò and uncle Maffeo, he traveled overland through Persia, Central Asia, and the Gobi Desert to reach Kublai Khan's summer palace at Shangdu (Xanadu). He spent 17 years in the service of the Mongol emperor, traveling widely through China, Burma, and Southeast Asia.\n\n"
        "His account — dictated to Rustichello da Pisa while imprisoned in Genoa — described paper money, coal burning, the imperial postal system, and Chinese civilization's advanced technology. Medieval Europeans called it Il Milione ('The Million') and dismissed it as fantasy.\n\n"
        "Yet Columbus carried an annotated copy on his 1492 voyage. The book remains the most influential travel narrative ever written, opening European imaginations to the wealth of Asia and directly inspiring the voyages that connected the world."
    ),
    "causes": [
        "The Pax Mongolica under Kublai Khan made safe overland travel from Europe to China possible for the first time in history",
        "The Polo family's trading connections and Kublai Khan's curiosity about Europeans brought Marco to the Mongol court",
        "Venice's position as the Mediterranean's premier trading republic created a merchant culture of long-distance travel"
    ],
    "effects": [
        "The Travels introduced Europe to Chinese technology, paper money, coal, and the vast wealth of East Asia",
        "Columbus carried an annotated copy of Marco Polo's Travels on his 1492 voyage — directly inspiring the Age of Exploration",
        "Stimulated European desire for Asian luxury goods (silk, spices, porcelain) that drove the search for sea routes to the East",
        "His descriptions of Kublai Khan's court and Chinese administration amazed Europeans and challenged their assumptions of superiority",
        "The book became the most influential travel narrative in history, translated into every major European language",
        "'Marco Polo' became synonymous with exploration and adventure in Western culture"
    ],
    "relationships": [
        rel("marco-polo", "Marco Polo", "SERVES", "kublai-khan", "Spent 17 years in the service of Kublai Khan's Mongol court in China"),
        rel("marco-polo", "Marco Polo", "TRAVELS", "silk-road", "Traveled the Silk Road from Venice to China and back (1271–1295)"),
        rel("marco-polo", "Marco Polo", "INFLUENCES", "christopher-columbus", "Columbus carried an annotated copy of Polo's Travels on his 1492 voyage"),
        rel("marco-polo", "Marco Polo", "ENABLED_BY", "genghis-khan", "The Mongol Empire's Pax Mongolica made safe transcontinental travel possible"),
        rel("marco-polo", "Marco Polo", "OCCURS_IN", "venice", "Born and raised in Venice, the Mediterranean's premier trading republic"),
    ],
    "subjectHeadings": ["People — Explorers & Merchants — Venice — Medieval"],
    "subjects": ["Silk Road", "Kublai Khan", "China", "Venice", "Exploration", "Travel Narrative", "Trade", "Mongolia", "Age of Exploration", "Pax Mongolica"],
    "frameworks": ["TRADE_AND_EXCHANGE", "CAUSE_AND_EFFECT", "CULTURAL_DIFFUSION", "INNOVATION_AND_TECHNOLOGY", "SOCIAL_STRUCTURES"],
},

"herodotus": {
    "path": "data/appwrite-export/entities/205-Class-205/205herodotus.json",
    "summary": (
        "Herodotus (c. 484–425 BCE) was a Greek historian from Halicarnassus whose Histories — the first large-scale narrative work of historical inquiry — earned him Cicero's title 'the Father of History.' His systematic investigation of the Greco-Persian Wars established history as a discipline distinct from mythology.\n\n"
        "Traveling widely through the Mediterranean, Egypt, Mesopotamia, and Scythia, he gathered eyewitness accounts, local traditions, and his own observations. His Histories (9 books) chronicle the rise of the Persian Empire, the cultures of Egypt, Babylon, and Scythia, and the Greek victories at Marathon, Thermopylae, Salamis, and Plataea.\n\n"
        "His method — autopsia (personal observation), oral testimony, and critical comparison of conflicting accounts — pioneered historical methodology. He distinguished between what he saw himself, what witnesses reported, and what he considered unreliable.\n\n"
        "Though criticized by Thucydides for credulity, modern archaeology has confirmed many of his claims once dismissed as fabrication. He remains the primary source for the Persian Wars and an invaluable ethnographer of the ancient world."
    ),
    "causes": [
        "The Greek victory in the Persian Wars (490–479 BCE) created the defining event that Herodotus sought to explain and preserve",
        "Greek intellectual culture's emphasis on rational inquiry (inherited from the Milesian philosophers) provided the methodological framework",
        "Extensive personal travel through Egypt, Persia, and Scythia gave Herodotus first-hand material unavailable to armchair writers"
    ],
    "effects": [
        "Established history as a systematic discipline of inquiry, earning the title 'Father of History' from Cicero",
        "The Histories became the primary source for the Greco-Persian Wars and ancient Near Eastern cultures",
        "His ethnographic descriptions of Egypt, Babylon, and Scythia provided invaluable evidence confirmed by modern archaeology",
        "Pioneered the methodology of critical comparison of sources, distinguishing eyewitness from hearsay",
        "Inspired Thucydides (who criticized but built upon him) and every subsequent Western historian",
        "His narrative style — weaving cultural digression into military history — created the model for engaging historical writing"
    ],
    "relationships": [
        rel("herodotus", "Herodotus", "INFLUENCES", "thucydides", "Thucydides built upon (and criticized) Herodotus's methodology in his History of the Peloponnesian War"),
        rel("herodotus", "Herodotus", "AUTHORS", "the-histories", "Wrote the Histories — the first large-scale historical narrative in Western literature"),
        rel("herodotus", "Herodotus", "OCCURS_IN", "ancient-greece", "Born in Halicarnassus (Asia Minor), traveled widely, and presented his work at Athens"),
        rel("herodotus", "Herodotus", "CONTEMPORARY_OF", "socrates", "Both active in the 5th century BCE during Athens' golden age"),
        rel("herodotus", "Herodotus", "CHRONICLES", "persian-wars", "The Histories chronicle the Greco-Persian Wars from Marathon to Plataea"),
    ],
    "subjectHeadings": ["People — Historians & Writers — Greece — Classical"],
    "subjects": ["History", "Persian Wars", "Egypt", "Ethnography", "Halicarnassus", "Ancient Greece", "Marathon", "Thermopylae", "Methodology", "Herodotus"],
    "frameworks": ["CULTURAL_DIFFUSION", "CAUSE_AND_EFFECT", "DOCTRINE_DEVELOPMENT", "SOCIAL_STRUCTURES", "MILITARY_HISTORY"],
},

}


# ================================================================
# APPLY STEP 1: Paragraph breaks for all 29
# ================================================================

ENRICHED_FILES = {
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
    "moses": "data/appwrite-export/entities/251-Class-251/251moses.json",
    "buddha": "data/appwrite-export/entities/251-Class-251/251buddha.json",
    "confucius": "data/appwrite-export/entities/210-Class-210/21005-confucius.json",
}

print("=" * 60)
print("STEP 1: Adding paragraph breaks to 29 entities")
print("=" * 60)

step1_ok = 0
for slug, new_summary in PARAGRAPH_REFORMATS.items():
    path = ENRICHED_FILES.get(slug)
    if not path or not os.path.exists(path):
        print(f"  SKIP {slug}: not found")
        continue
    with open(path) as f:
        data = json.load(f)
    entity = data["entities"][0]
    entity["summary"] = new_summary
    data["entities"][0] = entity
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    paras = new_summary.count("\n\n") + 1
    step1_ok += 1
    print(f"  OK {slug:30s} | {len(new_summary):4d}c | {paras} paragraphs")

print(f"\nStep 1 complete: {step1_ok} entities reformatted with paragraph breaks\n")


# ================================================================
# APPLY STEP 2: Enrich new entities
# ================================================================

print("=" * 60)
print("STEP 2: Enriching 15 more entities")
print("=" * 60)

step2_ok = 0
for slug, enrich in NEW_ENRICHMENTS.items():
    path = enrich["path"]
    if not os.path.exists(path):
        print(f"  SKIP {slug}: file not found ({path})")
        continue

    with open(path) as f:
        data = json.load(f)
    entity = data["entities"][0]

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

    # Update name if provided (e.g., napoleon-italy -> Napoleon Bonaparte)
    if "name" in enrich:
        entity["name"] = enrich["name"]

    for key in ["subjectHeadings", "subjects", "frameworks"]:
        if key in enrich and enrich[key]:
            entity[key] = enrich[key]

    data["entities"][0] = entity
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    slen = len(entity["summary"])
    rlen = len(new_dj["relationships"])
    paras = entity["summary"].count("\n\n") + 1
    step2_ok += 1
    print(f"  OK {slug:30s} | {slen:4d}c | {paras}p | rels={rlen} | causes={len(new_dj['causes'])} | effects={len(new_dj['effects'])}")

print(f"\nStep 2 complete: {step2_ok} entities enriched\n")
print(f"TOTAL: {step1_ok + step2_ok} entities updated")
