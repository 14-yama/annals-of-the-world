#!/usr/bin/env python3
"""Create 6 missing historically important entities."""
import json, os

def slug_to_name(slug):
    MAP = {
        "constantine-i": "Constantine I", "attila": "Attila the Hun",
        "copernicus": "Nicolaus Copernicus", "machiavelli": "Niccolò Machiavelli",
        "queen-victoria": "Queen Victoria", "sigmund-freud": "Sigmund Freud",
        "edict-of-milan": "Edict of Milan", "council-of-nicaea": "Council of Nicaea",
        "byzantine-empire": "Byzantine Empire", "christianity": "Christianity",
        "roman-empire": "Roman Empire", "holy-roman-empire": "Holy Roman Empire",
        "julius-caesar": "Julius Caesar", "jesus-christ": "Jesus Christ",
        "genghis-khan": "Genghis Khan", "hun-empire": "Hun Empire",
        "western-roman-empire": "Western Roman Empire", "eastern-roman-empire": "Eastern Roman Empire",
        "germanic-tribes": "Germanic Tribes", "galileo-galilei": "Galileo Galilei",
        "isaac-newton": "Isaac Newton", "ptolemaic-model": "Ptolemaic Model",
        "scientific-revolution": "Scientific Revolution", "aristotle": "Aristotle",
        "karl-marx": "Karl Marx", "napoleon-italy": "Napoleon Bonaparte",
        "thomas-jefferson": "Thomas Jefferson", "florence": "Florence",
        "the-prince": "The Prince", "martin-luther": "Martin Luther",
        "renaissance": "Renaissance", "thomas-aquinas": "Thomas Aquinas",
        "republic-plato": "Republic (Plato)", "indian-mutiny": "Indian Mutiny",
        "sun-never-sets": "British Empire", "british-empire": "British Empire",
        "charles-darwin": "Charles Darwin", "industrial-revolution": "Industrial Revolution",
        "united-kingdom": "United Kingdom", "france": "France",
        "italy": "Italy", "germany": "Germany", "vienna": "Vienna",
        "poland": "Poland", "ancient-rome": "Ancient Rome",
        "carl-jung": "Carl Jung", "friedrich-nietzsche": "Friedrich Nietzsche",
        "interpretation-of-dreams": "The Interpretation of Dreams",
        "joseph-breuer": "Joseph Breuer", "austria": "Austria",
    }
    return MAP.get(slug, slug.replace("-", " ").title())

def rel(source, source_name, verb, target, context):
    return {
        "sourceSlug": source,
        "sourceName": source_name,
        "verb": verb,
        "targetSlug": target,
        "targetName": slug_to_name(target),
        "context": context
    }


# Template based on existing entity structure
def make_entity(slug, name, data):
    dj = {
        "causes": data["causes"],
        "effects": data["effects"],
        "relationships": data["relationships"],
        "places": [],
        "texts": [],
        "externalLinks": [],
        "tags": [],
        "thumbnailUrl": "",
        "quote": "",
        "legacySummary": "",
    }
    return {
        "slug": slug,
        "name": name,
        "label": "Person",
        "callNumber": data["callNumber"],
        "summary": data["summary"],
        "era": data["era"],
        "eraSlug": data["era"].lower().replace(" ", "-"),
        "eraDivision": None,
        "eraDivisionCode": None,
        "region": data.get("region", "Global"),
        "continent": data.get("continent", "Global"),
        "status": "published",
        "died": None,
        "founded": None,
        "period": data.get("period", ""),
        "wikidataQid": data.get("qid", ""),
        "wikipediaUrl": data.get("wiki", ""),
        "imageUrl": None,
        "detailsJson": json.dumps(dj, ensure_ascii=False),
        "subjectHeadings": data.get("subjectHeadings", []),
        "subjects": data.get("subjects", []),
        "frameworks": data.get("frameworks", []),
        "altNames": data.get("altNames", []),
        "importanceScore": data.get("importance", 85),
        "born": None,
        "startDate": None,
        "endDate": None,
    }


NEW_ENTITIES = {

"constantine-i": {
    "callNumber": "221.constantine-i",
    "era": "Classical",
    "region": "Mediterranean",
    "continent": "Europe",
    "period": "272–337 CE",
    "qid": "Q8413",
    "wiki": "https://en.wikipedia.org/wiki/Constantine_the_Great",
    "altNames": ["Constantine the Great", "Flavius Valerius Constantinus"],
    "importance": 95,
    "summary": (
        "Constantine I (c. 272–337 CE) was the first Roman emperor to convert to Christianity, whose Edict of Milan (313 CE), founding of Constantinople, and Council of Nicaea (325 CE) transformed both the Roman Empire and world history — making Christianity the dominant religion of Western civilization.\n\n"
        "Rising through civil wars after Diocletian's tetrarchy collapsed, he defeated Maxentius at the Battle of the Milvian Bridge (312 CE) — reportedly after seeing a cross in the sky with the words 'In this sign, conquer.' His Edict of Milan legalized Christianity throughout the empire after three centuries of intermittent persecution.\n\n"
        "He convened the Council of Nicaea (325 CE), which produced the Nicene Creed — Christianity's foundational statement of orthodoxy. He moved the capital to Byzantium, renamed Constantinople (modern Istanbul), creating the eastern capital that would endure for over 1,100 years as the Byzantine Empire.\n\n"
        "His conversion pivoted Western civilization from paganism to Christianity. The 'Constantinian shift' — the fusion of church and state power — shaped European politics for 1,500 years."
    ),
    "causes": [
        "The Crisis of the Third Century and Diocletian's tetrarchy created the political instability that enabled Constantine's rise through civil war",
        "Three centuries of Christian growth despite persecution created a large, organized community that Constantine could harness politically",
        "The strategic vulnerability of Rome and the empire's eastern wealth motivated the founding of Constantinople as a new capital"
    ],
    "effects": [
        "The Edict of Milan (313 CE) legalized Christianity, ending 300 years of persecution and enabling its explosive growth as the empire's dominant religion",
        "The Council of Nicaea (325 CE) established Christian orthodoxy (the Nicene Creed) and the model of imperial involvement in church governance",
        "Founded Constantinople (330 CE), which became the capital of the Byzantine Empire for 1,100 years",
        "The 'Constantinian shift' fused church and state, establishing the pattern of Christian political authority across Europe",
        "His conversion made Christianity the religion of power — transforming a persecuted sect into the Roman state religion within a generation",
        "The division between Rome and Constantinople laid the groundwork for the Great Schism (1054) between Catholic and Orthodox Christianity"
    ],
    "relationships": [
        rel("constantine-i", "Constantine I", "ISSUES", "edict-of-milan", "Legalized Christianity throughout the Roman Empire (313 CE)"),
        rel("constantine-i", "Constantine I", "CONVENES", "council-of-nicaea", "Convened the first ecumenical council to define Christian orthodoxy (325 CE)"),
        rel("constantine-i", "Constantine I", "FOUNDS", "constantinople", "Refounded Byzantium as Constantinople, the 'New Rome' (330 CE)"),
        rel("constantine-i", "Constantine I", "TRANSFORMS", "christianity", "Transformed Christianity from persecuted faith to imperial religion"),
        rel("constantine-i", "Constantine I", "RULES", "roman-empire", "First emperor to unite the empire after the tetrarchy's collapse"),
        rel("constantine-i", "Constantine I", "OCCURS_IN", "ancient-rome", "Ruled from multiple capitals including Rome, Trier, and Constantinople"),
    ],
    "subjectHeadings": ["People — Emperors & Rulers — Rome/Byzantium — Classical"],
    "subjects": ["Christianity", "Roman Empire", "Constantinople", "Edict of Milan", "Council of Nicaea", "Nicene Creed", "Byzantine Empire", "Conversion", "Church and State", "Late Antiquity"],
    "frameworks": ["POLITICAL_SYSTEMS", "CAUSE_AND_EFFECT", "DOCTRINE_DEVELOPMENT", "RELIGIOUS_INSTITUTIONS", "CULTURAL_DIFFUSION"],
},

"attila": {
    "callNumber": "280.attila",
    "era": "Medieval",
    "region": "Central Asia",
    "continent": "Europe",
    "period": "c. 406–453 CE",
    "qid": "Q36724",
    "wiki": "https://en.wikipedia.org/wiki/Attila",
    "altNames": ["Attila the Hun", "Flagellum Dei", "Scourge of God"],
    "importance": 85,
    "summary": (
        "Attila (c. 406–453 CE), known as the 'Scourge of God' (Flagellum Dei), was the ruler of the Hunnic Empire who terrorized both the Eastern and Western Roman Empires — the most feared conqueror of Late Antiquity and the embodiment of nomadic barbarian power.\n\n"
        "Ruling a vast steppe empire from the Ural Mountains to the Rhine, he extorted enormous tributes from Constantinople and invaded the Western Empire in 451 CE. His massive army — a polyglot horde of Huns, Goths, and Gepids — was stopped at the Battle of the Catalaunian Plains by a coalition led by the Roman general Aetius and Visigothic king Theodoric I.\n\n"
        "He invaded Italy in 452, sacking cities from Aquileia to Milan. Legend holds that Pope Leo I personally persuaded Attila to withdraw from Rome — one of the most famous encounters between spiritual and temporal power.\n\n"
        "He died suddenly on his wedding night (453 CE), reportedly of a nosebleed. His empire collapsed within a year. The refugees fleeing his Italian invasion are traditionally credited with founding Venice's lagoon settlements."
    ),
    "causes": [
        "The Hunnic migration westward from the Central Asian steppe displaced Germanic tribes and destabilized the Roman frontier",
        "The decline of Rome's military capacity and reliance on barbarian foederati created vulnerability to Hunnic extortion and invasion",
        "Attila's ruthless consolidation of power (murdering his brother Bleda) gave him sole command of the largest nomadic empire in European history"
    ],
    "effects": [
        "His invasions accelerated the fall of the Western Roman Empire by destroying cities, displacing populations, and straining imperial resources",
        "The Battle of the Catalaunian Plains (451 CE) was one of the last Roman victories and demonstrated the empire's dependence on barbarian allies",
        "Refugees fleeing his invasion of Italy are traditionally credited with founding Venice's lagoon settlements",
        "His sudden death (453) and the empire's immediate collapse demonstrated nomadic empires' dependence on charismatic leadership",
        "Pope Leo I's confrontation with Attila enhanced papal prestige and the idea of spiritual authority checking temporal power",
        "'Attila the Hun' became Western civilization's archetype of barbaric destruction — a metaphor still used today"
    ],
    "relationships": [
        rel("attila", "Attila the Hun", "THREATENS", "roman-empire", "Extorted and invaded both Eastern and Western Roman Empires"),
        rel("attila", "Attila the Hun", "DEFEATED_BY", "aetius", "Stopped at the Catalaunian Plains by the Roman general Aetius (451 CE)"),
        rel("attila", "Attila the Hun", "CONFRONTED_BY", "pope-leo-i", "Pope Leo I persuaded Attila to withdraw from Rome (452 CE)"),
        rel("attila", "Attila the Hun", "RULES", "hun-empire", "Ruler of the Hunnic Empire from the Urals to the Rhine"),
        rel("attila", "Attila the Hun", "OCCURS_IN", "hungary", "Ruled from the Hungarian plain, the traditional heartland of the Hunnic Empire"),
    ],
    "subjectHeadings": ["People — Conquerors & Rulers — Hunnic Empire — Medieval"],
    "subjects": ["Hunnic Empire", "Fall of Rome", "Catalaunian Plains", "Barbarian Invasions", "Late Antiquity", "Nomadic Empire", "Scourge of God", "Hungary", "Pope Leo I", "Venice"],
    "frameworks": ["MILITARY_HISTORY", "CAUSE_AND_EFFECT", "POLITICAL_SYSTEMS", "CULTURAL_DIFFUSION", "SOCIAL_STRUCTURES"],
},

"copernicus": {
    "callNumber": "210.copernicus",
    "era": "Early Modern",
    "region": "Northern Europe",
    "continent": "Europe",
    "period": "1473–1543",
    "qid": "Q619",
    "wiki": "https://en.wikipedia.org/wiki/Nicolaus_Copernicus",
    "altNames": ["Mikołaj Kopernik"],
    "importance": 92,
    "summary": (
        "Nicolaus Copernicus (1473–1543) was a Polish-Prussian astronomer and polymath whose heliocentric model — placing the Sun rather than the Earth at the center of the universe — launched the Scientific Revolution and fundamentally changed humanity's understanding of its place in the cosmos.\n\n"
        "A Renaissance man in the truest sense — canon lawyer, physician, economist, diplomat, and military strategist — he spent decades refining his astronomical observations in Frombork, Prussia. His masterwork, De revolutionibus orbium coelestium (On the Revolutions of the Celestial Spheres), was published in 1543, the year of his death.\n\n"
        "Though his model still used circular orbits (corrected by Kepler) and was initially no more accurate than the Ptolemaic system, the conceptual revolution was seismic: Earth was no longer the center. This 'Copernican Revolution' undermined 1,400 years of Aristotelian-Ptolemaic cosmology.\n\n"
        "Galileo's telescope confirmed his theory. Kepler refined it. Newton explained it. The 'Copernican principle' — that humanity occupies no privileged position — remains the foundational assumption of modern science."
    ),
    "causes": [
        "The accumulated errors and complexities of the Ptolemaic system over 14 centuries made astronomers receptive to alternative models",
        "The Renaissance revival of ancient Greek astronomical texts (including Aristarchus's heliocentric proposal) provided intellectual precedent",
        "Copernicus's position as a cathedral canon in Frombork gave him the financial stability and time for decades of astronomical research"
    ],
    "effects": [
        "The heliocentric model launched the Scientific Revolution — the most consequential intellectual transformation in human history",
        "Undermined 1,400 years of Aristotelian-Ptolemaic cosmology and the geocentric worldview that supported it",
        "Enabled Kepler's laws of planetary motion and Newton's universal gravitation — impossible under the Ptolemaic model",
        "Created profound theological controversy by displacing Earth (and humanity) from the center of Creation",
        "The 'Copernican principle' — no privileged observer — became the foundational assumption of modern cosmology",
        "Galileo, Kepler, and Newton all built directly on Copernicus's revolution, completing the transformation he began"
    ],
    "relationships": [
        rel("copernicus", "Nicolaus Copernicus", "CHALLENGES", "ptolemaic-model", "Replaced the 1,400-year-old Ptolemaic geocentric model with heliocentrism"),
        rel("copernicus", "Nicolaus Copernicus", "INFLUENCES", "galileo-galilei", "Galileo's telescope observations confirmed Copernicus's heliocentric model"),
        rel("copernicus", "Nicolaus Copernicus", "INFLUENCES", "isaac-newton", "Newton's universal gravitation explained why the Copernican model works"),
        rel("copernicus", "Nicolaus Copernicus", "INITIATES", "scientific-revolution", "His heliocentric model is widely regarded as the starting point of the Scientific Revolution"),
        rel("copernicus", "Nicolaus Copernicus", "OCCURS_IN", "poland", "Born in Toruń, worked in Frombork (Royal Prussia) throughout his career"),
    ],
    "subjectHeadings": ["People — Scientists & Astronomers — Poland — Early Modern"],
    "subjects": ["Heliocentrism", "Scientific Revolution", "Astronomy", "De Revolutionibus", "Ptolemaic Model", "Poland", "Renaissance", "Cosmology", "Copernican Revolution", "Kepler"],
    "frameworks": ["INNOVATION_AND_TECHNOLOGY", "CAUSE_AND_EFFECT", "DOCTRINE_DEVELOPMENT", "SCIENCE_AND_RELIGION", "CULTURAL_DIFFUSION"],
},

"machiavelli": {
    "callNumber": "205.machiavelli",
    "era": "Early Modern",
    "region": "Southern Europe",
    "continent": "Europe",
    "period": "1469–1527",
    "qid": "Q1399",
    "wiki": "https://en.wikipedia.org/wiki/Niccolò_Machiavelli",
    "altNames": ["Niccolò di Bernardo dei Machiavelli"],
    "importance": 88,
    "summary": (
        "Niccolò Machiavelli (1469–1527) was a Florentine diplomat, political philosopher, and writer whose treatise The Prince — a brutally pragmatic guide to acquiring and maintaining political power — founded modern political science and made 'Machiavellian' a synonym for cunning realpolitik.\n\n"
        "As Secretary to the Second Chancery of the Florentine Republic (1498–1512), he conducted diplomatic missions to France, the Papal States, and the Holy Roman Empire, observing power politics firsthand. When the Medici returned to power, he was arrested, tortured, and exiled.\n\n"
        "Written in exile, The Prince (1513, published posthumously 1532) argued that effective rulers must be prepared to act immorally when necessity demands — 'it is better to be feared than loved.' His Discourses on Livy championed republican government, revealing a more complex political thinker than The Prince alone suggests.\n\n"
        "His separation of politics from Christian morality created modern political theory. Every subsequent political philosopher — Hobbes, Locke, Rousseau, Marx — engaged with Machiavelli's challenge."
    ),
    "causes": [
        "The Italian Wars (1494–1559) — foreign invasions that devastated Italian city-states — demonstrated the brutal realities of power that Machiavelli analyzed",
        "Florence's republican experiment and the Medici's return taught Machiavelli the instability of regimes firsthand",
        "The Renaissance's rediscovery of Roman history (especially Livy) provided the classical framework for his political analysis"
    ],
    "effects": [
        "The Prince founded modern political science by separating political analysis from Christian morality",
        "'Machiavellian' entered every European language as a synonym for cunning, amoral statecraft",
        "His analysis of power, force, and deception became the foundational text of realpolitik — studied by every subsequent political leader",
        "The Discourses on Livy influenced republican theory from the American Founders to modern democratic thought",
        "His separation of ethics from politics created the framework for Hobbes, Locke, Montesquieu, and modern political philosophy",
        "His concept of virtù (political skill, not Christian virtue) revolutionized how leadership is understood"
    ],
    "relationships": [
        rel("machiavelli", "Niccolò Machiavelli", "AUTHORS", "the-prince", "The Prince (1513) — the foundational text of modern political science"),
        rel("machiavelli", "Niccolò Machiavelli", "INFLUENCES", "thomas-jefferson", "The Federalist Papers and American constitutionalism engaged with Machiavelli's republican theory"),
        rel("machiavelli", "Niccolò Machiavelli", "INFLUENCED_BY", "aristotle", "Drew on classical political philosophy, especially Aristotle's Politics"),
        rel("machiavelli", "Niccolò Machiavelli", "OCCURS_IN", "florence", "Served the Florentine Republic as diplomat and Secretary of the Second Chancery"),
        rel("machiavelli", "Niccolò Machiavelli", "CONTEMPORARY_OF", "martin-luther", "Both shaped early modern thought: Machiavelli in politics, Luther in religion"),
    ],
    "subjectHeadings": ["People — Political Philosophers — Florence — Early Modern"],
    "subjects": ["The Prince", "Political Science", "Realpolitik", "Florence", "Renaissance", "Republicanism", "Power", "Diplomacy", "Italian Wars", "Machiavellian"],
    "frameworks": ["POLITICAL_SYSTEMS", "CAUSE_AND_EFFECT", "ETHICAL_FRAMEWORK", "DOCTRINE_DEVELOPMENT", "SOCIAL_STRUCTURES"],
},

"queen-victoria": {
    "callNumber": "222.queen-victoria",
    "era": "Modern",
    "region": "Western Europe",
    "continent": "Europe",
    "period": "1819–1901",
    "qid": "Q9439",
    "wiki": "https://en.wikipedia.org/wiki/Queen_Victoria",
    "altNames": ["Alexandrina Victoria", "Empress of India"],
    "importance": 90,
    "summary": (
        "Queen Victoria (1819–1901) reigned for 63 years and 7 months — the second-longest reign in British history — presiding over the British Empire at its zenith, when it encompassed a quarter of the world's land and population. The 'Victorian era' became synonymous with industrial progress, imperial expansion, and moral earnestness.\n\n"
        "Ascending the throne at 18, she restored the monarchy's prestige after the scandals of her Hanoverian predecessors. Her marriage to Prince Albert (1840) became a model of domestic virtue. Albert's death (1861) sent her into prolonged mourning that nearly undermined public support for the monarchy.\n\n"
        "Under her reign, Britain industrialized, built railways across the globe, dominated world trade, and expanded an empire spanning Canada, Australia, India, and large parts of Africa. She became Empress of India in 1876. The Great Exhibition of 1851 showcased Britain's industrial supremacy to the world.\n\n"
        "Her nine children married into virtually every European royal house, earning her the title 'Grandmother of Europe.' She also transmitted hemophilia to the Spanish, German, and Russian royal families — a genetic legacy with political consequences reaching into World War I."
    ),
    "causes": [
        "The death of William IV without legitimate heirs placed the 18-year-old Victoria on the throne, beginning the longest reign in British history to that point",
        "The Industrial Revolution and British naval supremacy created the economic and military foundation for Victorian imperial expansion",
        "Constitutional monarchy evolved under Victoria's predecessors, defining the relationship between Crown and Parliament that shaped her reign"
    ],
    "effects": [
        "The 'Victorian era' became synonymous with British global dominance — a quarter of the world's land and people under British rule",
        "Her name became an adjective ('Victorian') describing the moral values, social norms, and cultural achievements of an entire age",
        "Her nine children married into European royalty, making her 'Grandmother of Europe' and linking the continent's royal houses",
        "The transmission of hemophilia through her descendants affected the Spanish, German, and Russian royal families with political consequences",
        "The Great Exhibition of 1851 and Victorian engineering (railways, telegraph, steam) transformed the global economy",
        "Her long mourning for Albert and eventual return to public life helped cement constitutional monarchy as Britain's enduring political model"
    ],
    "relationships": [
        rel("queen-victoria", "Queen Victoria", "RULES", "british-empire", "Presided over the British Empire at its zenith — a quarter of the world's land and population"),
        rel("queen-victoria", "Queen Victoria", "CONTEMPORARY_OF", "charles-darwin", "Darwin's On the Origin of Species (1859) was published during her reign, transforming Victorian thought"),
        rel("queen-victoria", "Queen Victoria", "CONTEMPORARY_OF", "abraham-lincoln", "Victoria's decision to keep Britain neutral during the US Civil War shaped the war's outcome"),
        rel("queen-victoria", "Queen Victoria", "OCCURS_IN", "united-kingdom", "Reigned from 1837–1901 as Queen of the United Kingdom and Empress of India"),
        rel("queen-victoria", "Queen Victoria", "GRANDMOTHER_OF", "european-royalty", "Her descendants sat on the thrones of Britain, Germany, Russia, Spain, and Scandinavia"),
    ],
    "subjectHeadings": ["People — Monarchs & Rulers — United Kingdom — Modern"],
    "subjects": ["British Empire", "Victorian Era", "Industrial Revolution", "Constitutional Monarchy", "Empress of India", "Great Exhibition", "Hemophilia", "European Royalty", "United Kingdom", "19th Century"],
    "frameworks": ["POLITICAL_SYSTEMS", "CAUSE_AND_EFFECT", "SOCIAL_STRUCTURES", "TRADE_AND_EXCHANGE", "CULTURAL_DIFFUSION"],
},

"sigmund-freud": {
    "callNumber": "210.sigmund-freud",
    "era": "Modern",
    "region": "Central Europe",
    "continent": "Europe",
    "period": "1856–1939",
    "qid": "Q9215",
    "wiki": "https://en.wikipedia.org/wiki/Sigmund_Freud",
    "altNames": ["Sigismund Schlomo Freud"],
    "importance": 88,
    "summary": (
        "Sigmund Freud (1856–1939) was an Austrian neurologist who founded psychoanalysis — the theory that unconscious desires, childhood experiences, and repressed memories drive human behavior — revolutionizing how humanity understands the mind and making him, alongside Darwin and Einstein, one of the three thinkers who most reshaped modern self-understanding.\n\n"
        "Born in Moravia to a Jewish family, he studied medicine in Vienna and began treating hysteria through 'talking cure' methods developed with Josef Breuer. The Interpretation of Dreams (1900) argued that dreams are 'the royal road to the unconscious,' introducing the id, ego, and superego.\n\n"
        "His concepts — the Oedipus complex, defense mechanisms, the unconscious, transference, and the talking cure — permeated 20th-century culture, influencing literature (Kafka, Joyce), art (Surrealism), film (Hitchcock), and child-rearing practices worldwide.\n\n"
        "Though many of his specific theories have been revised or rejected by modern psychology, his fundamental insight — that much of mental life operates below conscious awareness — is now confirmed by neuroscience. He fled Nazi-occupied Vienna in 1938 and died in London in 1939."
    ),
    "causes": [
        "The 19th-century 'nervous illness' epidemic and inadequacy of purely somatic medicine created demand for psychological approaches to mental suffering",
        "Vienna's unique intellectual culture — the intersection of medicine, philosophy, and liberal Jewish thought — provided the incubator for psychoanalysis",
        "Breuer's 'Anna O.' case and the observation that talking about traumatic memories could relieve symptoms inspired Freud's 'talking cure'"
    ],
    "effects": [
        "Founded psychoanalysis — the first systematic theory of the unconscious mind and the first 'talking cure' for psychological distress",
        "The Interpretation of Dreams (1900) introduced the concepts of id, ego, superego, and dream analysis that transformed psychology",
        "His concepts (unconscious, repression, defense mechanisms, Oedipus complex) permeated 20th-century culture, literature, and art",
        "The Surrealist movement, Kafka, Joyce, and Hitchcock all drew directly on Freudian theory",
        "His fundamental insight — that unconscious processes drive behavior — is confirmed by modern neuroscience and cognitive psychology",
        "His therapeutic model (patient on a couch, free association, transference) became the archetype of psychological treatment worldwide"
    ],
    "relationships": [
        rel("sigmund-freud", "Sigmund Freud", "AUTHORS", "interpretation-of-dreams", "The Interpretation of Dreams (1900) — the foundational text of psychoanalysis"),
        rel("sigmund-freud", "Sigmund Freud", "COLLABORATES_WITH", "joseph-breuer", "Developed the 'talking cure' with Breuer from their treatment of hysteria patients"),
        rel("sigmund-freud", "Sigmund Freud", "MENTOR_OF", "carl-jung", "Jung was Freud's chosen successor before their famous break over the nature of the unconscious"),
        rel("sigmund-freud", "Sigmund Freud", "INFLUENCED_BY", "charles-darwin", "Darwin's evolutionary theory influenced Freud's view of instinctual drives and human nature"),
        rel("sigmund-freud", "Sigmund Freud", "OCCURS_IN", "austria", "Lived and practiced in Vienna from 1860 until fleeing the Nazis in 1938"),
    ],
    "subjectHeadings": ["People — Psychologists & Thinkers — Austria — Modern"],
    "subjects": ["Psychoanalysis", "Unconscious Mind", "Dreams", "Vienna", "Talking Cure", "Id Ego Superego", "Oedipus Complex", "Defense Mechanisms", "Psychology", "Austria"],
    "frameworks": ["DOCTRINE_DEVELOPMENT", "CAUSE_AND_EFFECT", "SOCIAL_STRUCTURES", "CULTURAL_DIFFUSION", "SCIENCE_AND_RELIGION"],
},

}


# Create files
for slug, data in NEW_ENTITIES.items():
    division_code = data["callNumber"].split(".")[0]
    class_name = f"Class-{division_code}"
    dir_path = f"data/appwrite-export/entities/{division_code}-{class_name}"
    os.makedirs(dir_path, exist_ok=True)

    filename = f"{division_code}{slug}.json"
    filepath = os.path.join(dir_path, filename)

    entity = make_entity(slug, slug_to_name(slug), data)

    # Generate unique $id
    entity["$id"] = f"enriched_{slug.replace('-','_')}"
    entity["$sequence"] = None
    entity["$createdAt"] = "2025-01-01T00:00:00.000+00:00"
    entity["$updatedAt"] = "2025-01-01T00:00:00.000+00:00"

    output = {"entities": [entity]}
    with open(filepath, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    slen = len(entity["summary"])
    paras = entity["summary"].count("\n\n") + 1
    dj = json.loads(entity["detailsJson"])
    print(f"  CREATED {slug:25s} | {slen:4d}c | {paras}p | rels={len(dj['relationships'])} | {filepath}")

print(f"\nCreated {len(NEW_ENTITIES)} new entities")
