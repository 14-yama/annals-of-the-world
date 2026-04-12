#!/usr/bin/env python3
"""
Batch 7: Enrich 10 worst STUBs + Create 10 missing high-importance entities.
Priority: P0 stubs first, then P1 missing notable figures.
"""
import json, glob, os, hashlib, time, urllib.request, urllib.error

ENDPOINT = "https://fra.cloud.appwrite.io/v1"
PROJECT  = "66509ba7003618a05af6"
DB       = "annals_world_db"
API_KEY  = "standard_a5dc3fada7d64812f42510400b8dab6d43ee3cca0417d0074cc71fd75ed6ac8db18a1d1e20446aab2e05d5be7d27d1908117fca2c79f3181e34e9f5e3a680e5f399e3e786387e9ccf2234c09ea45ffabad96c817457bf3549059b445433a80783ac03dac408185e8d6ccc46521f0dcae60dd15ffe73eddca9db4001a146ea3fd"
COLLECTION = "entities"
BASE = "data/appwrite-export/entities"

def slug_to_id(slug):
    return hashlib.sha256(slug.encode()).hexdigest()[:20]

def headers():
    return {
        "Content-Type": "application/json",
        "X-Appwrite-Project": PROJECT,
        "X-Appwrite-Key": API_KEY,
    }

def get_doc(doc_id):
    url = f"{ENDPOINT}/databases/{DB}/collections/{COLLECTION}/documents/{doc_id}"
    req = urllib.request.Request(url, headers=headers())
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError:
        return None

def create_doc(doc_id, data):
    url = f"{ENDPOINT}/databases/{DB}/collections/{COLLECTION}/documents"
    body = json.dumps({"documentId": doc_id, "data": data}).encode()
    req = urllib.request.Request(url, data=body, headers=headers(), method="POST")
    try:
        with urllib.request.urlopen(req) as r: return True
    except urllib.error.HTTPError as e:
        print(f"    CREATE ERROR: {e.code} {e.read().decode()[:200]}")
        return False

def update_doc(doc_id, data):
    url = f"{ENDPOINT}/databases/{DB}/collections/{COLLECTION}/documents/{doc_id}"
    body = json.dumps({"data": data}).encode()
    req = urllib.request.Request(url, data=body, headers=headers(), method="PATCH")
    try:
        with urllib.request.urlopen(req) as r: return True
    except urllib.error.HTTPError as e:
        print(f"    UPDATE ERROR: {e.code} {e.read().decode()[:200]}")
        return False

def delete_doc(doc_id):
    url = f"{ENDPOINT}/databases/{DB}/collections/{COLLECTION}/documents/{doc_id}"
    req = urllib.request.Request(url, headers=headers(), method="DELETE")
    try:
        with urllib.request.urlopen(req) as r: return True
    except urllib.error.HTTPError:
        return False

# ═══════════════════════════════════════════
# PART 1: ENRICH 10 WORST STUBS
# ═══════════════════════════════════════════

ENRICHMENTS = {
    "richard-wagner": {
        "summary": "Richard Wagner (1813\u20131883) was a German composer, conductor, and polemicist who revolutionised opera through his concept of the Gesamtkunstwerk\u2014the 'total work of art' unifying music, drama, poetry, and visual spectacle. His influence on Western music is rivalled only by Bach and Beethoven.\n\nWagner's mature operas\u2014'Tristan und Isolde' (1865), 'Die Meisteringer von N\u00fcrnberg' (1868), and the four-opera cycle 'Der Ring des Nibelungen' (1876)\u2014shattered conventional tonality and dramatic structure. 'Tristan' introduced chromatic harmonies so radical that they pointed directly toward the dissolution of tonal music in the 20th century.\n\nTo stage his vision, Wagner designed and built the Bayreuth Festspielhaus, a purpose-built opera house with a hidden orchestra pit that opened in 1876 for the first complete 'Ring' cycle. The Bayreuth Festival continues annually to this day.\n\nWagner's anti-Semitic writings and his posthumous adoption by the Nazi regime remain deeply controversial. Yet his musical innovations\u2014the leitmotif system, through-composed opera, and expanded orchestral palette\u2014reshaped film scoring, symphonic music, and theatrical practice worldwide.",
        "causes": ["Beethoven's symphonic expansion of musical expression", "German Romantic literary and philosophical tradition (Schopenhauer)", "Weber's pioneering German Romantic opera"],
        "effects": ["Dissolved conventional tonality, paving the way for Schoenberg and atonality", "Created the leitmotif system adopted by all subsequent film scoring", "Built Bayreuth Festspielhaus and established the Wagner Festival tradition"],
        "relationships": [
            {"sourceSlug": "richard-wagner", "sourceName": "Richard Wagner", "verb": "INFLUENCES", "targetSlug": "igor-stravinsky", "targetName": "Igor Stravinsky", "context": "Stravinsky reacted against Wagnerian excess, defining modernist aesthetics"},
            {"sourceSlug": "ludwig-van-beethoven", "sourceName": "Ludwig van Beethoven", "verb": "INFLUENCES", "targetSlug": "richard-wagner", "targetName": "Richard Wagner", "context": "Wagner saw himself as Beethoven's successor in expanding symphonic drama"},
            {"sourceSlug": "richard-wagner", "sourceName": "Richard Wagner", "verb": "CREATES", "targetSlug": "ring-cycle", "targetName": "Der Ring des Nibelungen", "context": "Four-opera cycle composed 1848-1874, premiered Bayreuth 1876"},
            {"sourceSlug": "richard-wagner", "sourceName": "Richard Wagner", "verb": "OCCURS_IN", "targetSlug": "bayreuth", "targetName": "Bayreuth", "context": "Built the Festspielhaus and established the annual Bayreuth Festival"},
            {"sourceSlug": "richard-wagner", "sourceName": "Richard Wagner", "verb": "INFLUENCES", "targetSlug": "giuseppe-verdi", "targetName": "Giuseppe Verdi", "context": "Wagner and Verdi defined rival operatic traditions: German vs. Italian"}
        ],
        "places": [{"name": "Bayreuth, Germany", "role": "Festival and opera house"}, {"name": "Leipzig, Germany", "role": "Birthplace"}, {"name": "Venice, Italy", "role": "Death"}],
        "subjects": ["Opera", "German Romanticism", "Leitmotif", "Gesamtkunstwerk", "Germany", "Music History", "Bayreuth Festival", "Composition"],
        "frameworks": ["CULTURAL_TRANSMISSION", "CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
        # Fix: Current entry says "Romanian-born German novelist" — completely wrong person
        "fix_name": "Richard Wagner",
        "fix_label": "Person",
        "fix_callNumber": "263.richard-wagner",
        "fix_division": "263-Class-263",
        "fix_old_division": "201-Class-201",
    },
    "victor-hugo": {
        "summary": "Victor Hugo (1802\u20131885) was a French poet, novelist, and dramatist who dominated French literature for over sixty years. His novels 'Les Mis\u00e9rables' (1862) and 'The Hunchback of Notre-Dame' (1831) are among the most widely read works in world literature, and his poetry collections established him as France's greatest Romantic poet.\n\nHugo's literary career began early\u2014he published his first poetry collection at 20 and his play 'Hernani' (1830) triggered a battle between Classicists and Romantics that defined French cultural politics. His preface to 'Cromwell' (1827) became the manifesto of the French Romantic movement.\n\nA fierce republican, Hugo spent 19 years in political exile (1851\u20131870) on the Channel Islands after opposing Napoleon III's coup d'\u00e9tat. During exile he wrote 'Les Mis\u00e9rables,' whose portrayal of poverty, injustice, and redemption made it one of the most influential novels ever written.\n\nHugo's funeral in 1885 drew two million mourners\u2014the largest public gathering in French history to that date. His advocacy for the abolition of the death penalty, universal suffrage, and free education made him a prophet of social justice. As Andr\u00e9 Gide quipped when asked to name France's greatest poet: 'Victor Hugo\u2014h\u00e9las!'",
        "causes": ["French Romantic literary movement and reaction against Classicism", "Napoleonic era upheaval and post-Revolutionary political instability", "Personal experience of poverty and political exile"],
        "effects": ["Defined French Romantic movement through poetry, drama, and fiction", "'Les Miserables' became foundational text of social justice literature", "Campaign against death penalty influenced European abolition movements"],
        "relationships": [
            {"sourceSlug": "victor-hugo", "sourceName": "Victor Hugo", "verb": "INFLUENCES", "targetSlug": "charles-dickens", "targetName": "Charles Dickens", "context": "Both used fiction as vehicle for social reform; mutual admiration"},
            {"sourceSlug": "victor-hugo", "sourceName": "Victor Hugo", "verb": "CREATES", "targetSlug": "les-miserables", "targetName": "Les Misérables", "context": "Published 1862, became definitive novel of social justice"},
            {"sourceSlug": "napoleon-bonaparte", "sourceName": "Napoleon Bonaparte", "verb": "INFLUENCES", "targetSlug": "victor-hugo", "targetName": "Victor Hugo", "context": "Napoleonic era shaped Hugo's political consciousness and literary themes"},
            {"sourceSlug": "victor-hugo", "sourceName": "Victor Hugo", "verb": "OCCURS_IN", "targetSlug": "paris", "targetName": "Paris", "context": "Born, lived, and died in Paris; the city is central to his works"},
            {"sourceSlug": "victor-hugo", "sourceName": "Victor Hugo", "verb": "PARTICIPATES_IN", "targetSlug": "french-romanticism", "targetName": "French Romanticism", "context": "His preface to Cromwell (1827) was the Romantic movement's manifesto"}
        ],
        "places": [{"name": "Paris, France", "role": "Birthplace and creative home"}, {"name": "Guernsey, Channel Islands", "role": "Political exile 1855-1870"}, {"name": "Brussels, Belgium", "role": "Early exile"}],
        "subjects": ["French Literature", "Romanticism", "Social Justice", "Poetry", "France", "Political Exile", "Novel", "Death Penalty Abolition"],
        "frameworks": ["CULTURAL_TRANSMISSION", "CAUSE_AND_EFFECT", "WORLD_SYSTEMS"]
    },
    "nero": {
        "summary": "Nero Claudius Caesar Augustus Germanicus (37\u201368 CE) was the fifth Roman emperor, ruling from 54 to 68 CE as the last of the Julio-Claudian dynasty. His reign began promisingly under the guidance of Seneca and Burrus but descended into tyranny, persecution, and the Great Fire of Rome that devastated the city in 64 CE.\n\nAdopted by Emperor Claudius and tutored by the Stoic philosopher Seneca, Nero initially pursued moderate governance. His early reign (the quinquennium Neronis) was later praised by Trajan as the finest period of imperial government. But after murdering his mother Agrippina in 59 CE and disposing of his advisors, Nero's rule grew increasingly erratic.\n\nThe Great Fire of July 64 CE destroyed ten of Rome's fourteen districts. Nero blamed Christians for the fire, launching the first imperial persecution\u2014tradition holds that both Peter and Paul were martyred during this campaign. He used the cleared land to build his extravagant Domus Aurea (Golden House).\n\nFacing a military revolt in 68 CE, the Senate declared Nero a public enemy. He fled Rome and committed suicide, reportedly saying: 'Qualis artifex pereo'\u2014'What an artist dies in me!' His death ended the Julio-Claudian dynasty and plunged Rome into the Year of the Four Emperors.",
        "causes": ["Julio-Claudian dynastic succession and Agrippina's political maneuvering", "Seneca's Stoic influence on early moderate governance", "Growing imperial autocracy and elimination of senatorial checks"],
        "effects": ["First Roman persecution of Christians after Great Fire of 64 CE", "End of the Julio-Claudian dynasty, triggering Year of the Four Emperors", "Became archetypal tyrant in Western historical imagination"],
        "relationships": [
            {"sourceSlug": "nero", "sourceName": "Nero", "verb": "SUCCEEDS", "targetSlug": "augustus-caesar", "targetName": "Augustus Caesar", "context": "Last emperor of the Julio-Claudian dynasty founded by Augustus"},
            {"sourceSlug": "nero", "sourceName": "Nero", "verb": "CAUSES", "targetSlug": "christian-persecution", "targetName": "Christian Persecution", "context": "Launched first imperial persecution of Christians after 64 CE fire"},
            {"sourceSlug": "nero", "sourceName": "Nero", "verb": "OCCURS_IN", "targetSlug": "rome", "targetName": "Rome", "context": "Emperor in Rome 54-68 CE; Great Fire destroyed much of the city"},
            {"sourceSlug": "seneca", "sourceName": "Seneca", "verb": "INFLUENCES", "targetSlug": "nero", "targetName": "Nero", "context": "Seneca tutored young Nero and guided his early moderate policies"},
            {"sourceSlug": "nero", "sourceName": "Nero", "verb": "PARTICIPATES_IN", "targetSlug": "great-fire-of-rome", "targetName": "Great Fire of Rome", "context": "Used the fire's aftermath to build the Domus Aurea and persecute Christians"}
        ],
        "places": [{"name": "Rome, Italy", "role": "Imperial capital"}, {"name": "Antium, Italy", "role": "Birthplace"}, {"name": "Domus Aurea, Rome", "role": "Palace built after the fire"}],
        "subjects": ["Roman Empire", "Julio-Claudian Dynasty", "Christian Persecution", "Great Fire of Rome", "Tyranny", "Italy", "Ancient Rome", "Imperial Succession"],
        "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS", "PSYCHOLOGICAL_ANALYSIS"]
    },
    "justinian-i": {
        "summary": "Justinian I (c. 482\u2013565 CE) was Byzantine Emperor from 527 to 565 whose ambitious reign reshaped law, architecture, and the boundaries of the Roman world. His codification of Roman law\u2014the Corpus Juris Civilis (534 CE)\u2014became the foundation of legal systems across Europe and remains the basis of civil law in dozens of countries today.\n\nBorn a Latin-speaking peasant in Illyria, Justinian rose through his uncle Justin I's patronage. With his formidable wife Theodora\u2014a former actress\u2014he pursued three grand projects: reconquering the lost Western Roman territories, systematizing Roman law, and building architectural monuments.\n\nHis general Belisarius reconquered North Africa from the Vandals (533\u2013534), Italy from the Ostrogoths (535\u2013554), and southern Spain from the Visigoths, briefly reuniting much of the old Roman Empire. Justinian commissioned the Hagia Sophia (537), whose revolutionary dome remained the world's largest cathedral for nearly a thousand years.\n\nThe Plague of Justinian (541\u2013542)\u2014the first recorded bubonic plague pandemic\u2014killed an estimated 25\u201350 million people and devastated his empire's economy and military. Despite this catastrophe, Justinian's legal and architectural legacy endured far beyond Byzantium. As the historian Procopius recorded: 'He transformed the whole state of the Romans.'",
        "causes": ["Continuation of Roman imperial tradition through Byzantine succession", "Theodora's political partnership and influence on religious policy", "Availability of military genius in generals Belisarius and Narses"],
        "effects": ["Corpus Juris Civilis became foundation of European civil law systems", "Hagia Sophia established Byzantine architectural paradigm for 1,000 years", "Reconquests temporarily reunited much of the Roman Empire"],
        "relationships": [
            {"sourceSlug": "justinian-i", "sourceName": "Justinian I", "verb": "CREATES", "targetSlug": "corpus-juris-civilis", "targetName": "Corpus Juris Civilis", "context": "Codified 1,000 years of Roman law into systematic legal corpus, 534 CE"},
            {"sourceSlug": "justinian-i", "sourceName": "Justinian I", "verb": "CREATES", "targetSlug": "hagia-sophia", "targetName": "Hagia Sophia", "context": "Commissioned construction 532-537, largest cathedral for nearly 1,000 years"},
            {"sourceSlug": "justinian-i", "sourceName": "Justinian I", "verb": "OCCURS_IN", "targetSlug": "constantinople", "targetName": "Constantinople", "context": "Ruled from Constantinople as Byzantine Emperor 527-565 CE"},
            {"sourceSlug": "constantine-i", "sourceName": "Constantine I", "verb": "INFLUENCES", "targetSlug": "justinian-i", "targetName": "Justinian I", "context": "Constantine's Christian Roman model inspired Justinian's imperial vision"},
            {"sourceSlug": "justinian-i", "sourceName": "Justinian I", "verb": "INFLUENCES", "targetSlug": "napoleon-bonaparte", "targetName": "Napoleon Bonaparte", "context": "Napoleonic Code modeled on Justinian's Corpus Juris Civilis"}
        ],
        "places": [{"name": "Constantinople, Turkey", "role": "Imperial capital"}, {"name": "Tauresium, North Macedonia", "role": "Birthplace"}, {"name": "Ravenna, Italy", "role": "Reconquered Western capital"}],
        "subjects": ["Byzantine Empire", "Roman Law", "Corpus Juris Civilis", "Hagia Sophia", "Reconquest", "Plague", "Architecture", "Legal History"],
        "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS", "WORLD_SYSTEMS"]
    },
    "jane-austen": {
        "summary": "Jane Austen (1775\u20131817) was an English novelist whose six completed works\u2014including 'Pride and Prejudice' (1813), 'Sense and Sensibility' (1811), and 'Emma' (1815)\u2014are regarded as foundational texts of the English literary canon. Her incisive social comedy, psychological realism, and ironic narrative voice transformed the novel from romance into a vehicle for exploring moral philosophy and human nature.\n\nAusten wrote in the confined world of the English rural gentry, yet her scope was universal. Her plots revolve around courtship, marriage, and money\u2014the central preoccupations of women whose social standing depended entirely on whom they married. Within these constraints, she created characters of extraordinary psychological depth.\n\nPublishing anonymously ('By a Lady'), Austen earned modest recognition during her lifetime. She died at 41, probably from Addison's disease, leaving 'Persuasion' and 'Northanger Abbey' published posthumously. Her nephew's 1870 'Memoir' sparked a Victorian rediscovery that has never abated.\n\nSir Walter Scott wrote of her: 'That young lady has a talent for describing the involvements of feelings and characters of ordinary life which is to me the most wonderful I ever met with.' Today she is among the most widely read, adapted, and studied authors in the English language.",
        "causes": ["18th-century English novel tradition (Richardson, Fielding, Burney)", "Georgian gentry social structure and marriage economy", "Enlightenment emphasis on reason, moral judgment, and individual character"],
        "effects": ["Pioneered the novel of manners and psychological realism in English fiction", "Influenced the Bronte sisters, George Eliot, Henry James, and Virginia Woolf", "Became one of the most adapted authors in film and television history"],
        "relationships": [
            {"sourceSlug": "jane-austen", "sourceName": "Jane Austen", "verb": "INFLUENCES", "targetSlug": "virginia-woolf", "targetName": "Virginia Woolf", "context": "Woolf praised Austen as 'the most perfect artist among women'"},
            {"sourceSlug": "jane-austen", "sourceName": "Jane Austen", "verb": "CREATES", "targetSlug": "pride-and-prejudice", "targetName": "Pride and Prejudice", "context": "Published 1813, became most popular English novel of social comedy"},
            {"sourceSlug": "jane-austen", "sourceName": "Jane Austen", "verb": "OCCURS_IN", "targetSlug": "bath", "targetName": "Bath", "context": "Lived in Bath 1801-1806, setting of Northanger Abbey and Persuasion"},
            {"sourceSlug": "jane-austen", "sourceName": "Jane Austen", "verb": "INFLUENCES", "targetSlug": "charles-dickens", "targetName": "Charles Dickens", "context": "Austen's social observation pioneered the tradition Dickens expanded"},
            {"sourceSlug": "jane-austen", "sourceName": "Jane Austen", "verb": "PARTICIPATES_IN", "targetSlug": "english-novel", "targetName": "English Novel Tradition", "context": "Transformed the novel from romance into psychological realism"}
        ],
        "places": [{"name": "Steventon, Hampshire", "role": "Birthplace and early life"}, {"name": "Chawton, Hampshire", "role": "Final home and most productive period"}, {"name": "Bath, England", "role": "Residence and novel setting"}],
        "subjects": ["English Literature", "Novel of Manners", "Regency Era", "Social Comedy", "England", "Women Writers", "Psychological Realism", "Marriage"],
        "frameworks": ["CULTURAL_TRANSMISSION", "FEMINIST_PERSPECTIVE", "STRUCTURAL_ANALYSIS"]
    },
    "montesquieu": {
        "summary": "Charles-Louis de Secondat, Baron de Montesquieu (1689\u20131755) was a French philosopher and political theorist whose masterwork 'The Spirit of the Laws' (1748) articulated the principle of separation of powers that became the structural foundation of modern democratic government, most directly shaping the United States Constitution.\n\nBorn into Bordeaux's legal aristocracy, Montesquieu served as president of the local parlement before turning to philosophy. His satirical 'Persian Letters' (1721) used fictional Persian travelers to critique French society, establishing him as a leading figure of the early Enlightenment.\n\n'The Spirit of the Laws'\u2014the product of 20 years' research\u2014analyzed how climate, geography, religion, and custom shape political institutions. Its central argument\u2014that liberty requires the separation of legislative, executive, and judicial powers\u2014was read by every American Founding Father and is explicitly embedded in Articles I, II, and III of the US Constitution.\n\nMontesquieu's comparative method\u2014studying real governments rather than imagining ideal ones\u2014founded modern political science and comparative law. Madison, Hamilton, and Jefferson cited him more than any other philosopher. As Voltaire acknowledged: 'Mankind had lost its title deeds; Montesquieu found them.'",
        "causes": ["English constitutional monarchy model observed during 1729-1731 visit", "French absolutism under Louis XIV demonstrating dangers of concentrated power", "Classical republican tradition from Aristotle, Polybius, and Cicero"],
        "effects": ["Separation of powers doctrine became foundation of US Constitution", "Founded comparative political science and sociology of law", "Influenced every major democratic constitution of the 18th-19th centuries"],
        "relationships": [
            {"sourceSlug": "montesquieu", "sourceName": "Montesquieu", "verb": "INFLUENCES", "targetSlug": "george-washington", "targetName": "George Washington", "context": "Separation of powers shaped the constitutional framework Washington upheld"},
            {"sourceSlug": "montesquieu", "sourceName": "Montesquieu", "verb": "INFLUENCES", "targetSlug": "john-locke", "targetName": "John Locke", "context": "Built on Locke's theory of government while adding comparative method"},
            {"sourceSlug": "montesquieu", "sourceName": "Montesquieu", "verb": "CREATES", "targetSlug": "spirit-of-the-laws", "targetName": "The Spirit of the Laws", "context": "Published 1748, articulated separation of powers doctrine"},
            {"sourceSlug": "montesquieu", "sourceName": "Montesquieu", "verb": "OCCURS_IN", "targetSlug": "bordeaux", "targetName": "Bordeaux", "context": "Born and served as parlement president in Bordeaux"},
            {"sourceSlug": "voltaire", "sourceName": "Voltaire", "verb": "COLLABORATES_WITH", "targetSlug": "montesquieu", "targetName": "Montesquieu", "context": "Both central figures of the French Enlightenment, mutual intellectual exchange"}
        ],
        "places": [{"name": "Bordeaux, France", "role": "Birth and legal career"}, {"name": "Paris, France", "role": "Intellectual life and publication"}, {"name": "London, England", "role": "Study of English constitutional system"}],
        "subjects": ["Separation of Powers", "Political Philosophy", "French Enlightenment", "Constitutional Law", "France", "Comparative Politics", "US Constitution", "Democracy"],
        "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS", "COMPARATIVE_CIVILIZATIONS"]
    },
    "robert-koch": {
        "summary": "Robert Koch (1843\u20131910) was a German physician and microbiologist who founded modern bacteriology and proved the germ theory of disease through rigorous experimental methods. His discovery of the tuberculosis bacillus (1882) and cholera bacillus (1883) saved millions of lives and earned him the Nobel Prize in Physiology or Medicine in 1905.\n\nWorking initially as a rural district physician, Koch developed techniques for isolating pure bacterial cultures using solid media (gelatin, then agar plates)\u2014methods still used in every microbiology laboratory today. His famous 'Koch's Postulates' (1884) established the logical framework for proving that a specific microorganism causes a specific disease.\n\nKoch's announcement of the tuberculosis bacillus on March 24, 1882 was called 'the most important event in the history of medicine.' TB was then killing one in seven Europeans. He later discovered the cholera vibrio during an expedition to Egypt and India, enabling targeted public health interventions.\n\nHis Berlin laboratory became the global training ground for a generation of microbiologists, including Emil von Behring, Paul Ehrlich, and Kitasato Shibasaburo. Koch's rigorous methods transformed medicine from speculation into experimental science. World Tuberculosis Day (March 24) commemorates his landmark discovery.",
        "causes": ["Pasteur's germ theory providing theoretical framework", "Advances in microscopy and staining techniques (aniline dyes)", "European tuberculosis and cholera epidemics creating urgent need"],
        "effects": ["Founded modern bacteriology as a scientific discipline", "Koch's Postulates established standard for proving disease causation", "Nobel Prize 1905; methods still used in every microbiology lab worldwide"],
        "relationships": [
            {"sourceSlug": "louis-pasteur", "sourceName": "Louis Pasteur", "verb": "INFLUENCES", "targetSlug": "robert-koch", "targetName": "Robert Koch", "context": "Pasteur's germ theory provided the framework Koch proved experimentally"},
            {"sourceSlug": "robert-koch", "sourceName": "Robert Koch", "verb": "INFLUENCES", "targetSlug": "florence-nightingale", "targetName": "Florence Nightingale", "context": "Koch's germ theory validated Nightingale's hygiene-based nursing reforms"},
            {"sourceSlug": "robert-koch", "sourceName": "Robert Koch", "verb": "CREATES", "targetSlug": "kochs-postulates", "targetName": "Koch's Postulates", "context": "Published 1884, logical framework for proving microbial disease causation"},
            {"sourceSlug": "robert-koch", "sourceName": "Robert Koch", "verb": "OCCURS_IN", "targetSlug": "berlin", "targetName": "Berlin", "context": "Koch's Berlin laboratory trained a generation of world-leading microbiologists"},
            {"sourceSlug": "robert-koch", "sourceName": "Robert Koch", "verb": "PARTICIPATES_IN", "targetSlug": "nobel-prize", "targetName": "Nobel Prize", "context": "Won Nobel Prize in Physiology or Medicine 1905 for tuberculosis research"}
        ],
        "places": [{"name": "Berlin, Germany", "role": "Laboratory and career"}, {"name": "Clausthal, Germany", "role": "Birthplace"}, {"name": "Calcutta, India", "role": "Cholera research expedition"}],
        "subjects": ["Bacteriology", "Germ Theory", "Tuberculosis", "Cholera", "Nobel Prize", "Germany", "Public Health", "Medical Science"],
        "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS", "COMPARATIVE_CIVILIZATIONS"]
    },
    "virginia-woolf": {
        "summary": "Virginia Woolf (1882\u20131941) was an English writer and modernist pioneer whose novels\u2014including 'Mrs Dalloway' (1925), 'To the Lighthouse' (1927), and 'Orlando' (1928)\u2014revolutionised narrative technique through stream-of-consciousness prose that mapped the interior landscape of human thought with unprecedented precision.\n\nBorn into the intellectual aristocracy of Victorian London (her father was Sir Leslie Stephen, editor of the Dictionary of National Biography), Woolf suffered from recurring mental illness throughout her life. She and her husband Leonard founded the Hogarth Press in 1917, which published T.S. Eliot's 'The Waste Land' and her own experimental novels.\n\nHer essay 'A Room of One's Own' (1929) argued that women's literary achievement required financial independence and private space\u2014a foundational text of feminist literary criticism. 'Three Guineas' (1938) connected patriarchy, fascism, and war in a prescient analysis that anticipated second-wave feminism by decades.\n\nWoolf was central to the Bloomsbury Group\u2014the London intellectual circle that included John Maynard Keynes, E.M. Forster, and Lytton Strachey. She drowned herself in the River Ouse on March 28, 1941, leaving a note to Leonard: 'I don't think two people could have been happier than we have been.'",
        "causes": ["Victorian literary culture and access to father's extensive library", "Bloomsbury Group intellectual community and artistic experimentation", "Personal experience of mental illness shaping interior narrative technique"],
        "effects": ["Pioneered stream-of-consciousness technique in English fiction", "'A Room of One's Own' became foundational text of feminist literary criticism", "Influenced every subsequent modernist and postmodernist novelist"],
        "relationships": [
            {"sourceSlug": "virginia-woolf", "sourceName": "Virginia Woolf", "verb": "PARTICIPATES_IN", "targetSlug": "bloomsbury-group", "targetName": "Bloomsbury Group", "context": "Central member alongside Keynes, Forster, Strachey, and Bell"},
            {"sourceSlug": "virginia-woolf", "sourceName": "Virginia Woolf", "verb": "INFLUENCES", "targetSlug": "simone-de-beauvoir", "targetName": "Simone de Beauvoir", "context": "Woolf's feminist essays anticipated and influenced de Beauvoir's 'The Second Sex'"},
            {"sourceSlug": "jane-austen", "sourceName": "Jane Austen", "verb": "INFLUENCES", "targetSlug": "virginia-woolf", "targetName": "Virginia Woolf", "context": "Woolf praised Austen as 'the most perfect artist among women'"},
            {"sourceSlug": "virginia-woolf", "sourceName": "Virginia Woolf", "verb": "OCCURS_IN", "targetSlug": "london", "targetName": "London", "context": "Born, lived, worked, and published in London; the city is central to Mrs Dalloway"},
            {"sourceSlug": "virginia-woolf", "sourceName": "Virginia Woolf", "verb": "CREATES", "targetSlug": "mrs-dalloway", "targetName": "Mrs Dalloway", "context": "Published 1925, pioneered stream-of-consciousness narrative in English"}
        ],
        "places": [{"name": "London, England", "role": "Lifelong home and literary setting"}, {"name": "Rodmell, Sussex", "role": "Country home and death"}, {"name": "St Ives, Cornwall", "role": "Childhood inspiration for To the Lighthouse"}],
        "subjects": ["Modernism", "Stream of Consciousness", "Feminist Criticism", "Bloomsbury Group", "England", "Mental Health", "Publishing", "English Literature"],
        "frameworks": ["FEMINIST_PERSPECTIVE", "CULTURAL_TRANSMISSION", "PSYCHOLOGICAL_ANALYSIS"]
    },
    "max-planck": {
        "summary": "Max Karl Ernst Ludwig Planck (1858\u20131947) was a German theoretical physicist who originated quantum theory\u2014the most revolutionary scientific framework of the 20th century. His discovery that energy is emitted in discrete packets called 'quanta' (1900) overturned classical physics and earned him the Nobel Prize in Physics in 1918.\n\nFaced with the 'ultraviolet catastrophe'\u2014classical physics' failure to explain black-body radiation\u2014Planck proposed that electromagnetic energy could only be emitted in quantised form: E = h\u03bd (energy equals Planck's constant times frequency). He introduced this as a mathematical trick, not realising he had launched a revolution.\n\nPlanck's constant (h = 6.626 \u00d7 10\u207b\u00b3\u2074 J\u00b7s) became one of the fundamental constants of nature, appearing in virtually every equation of quantum mechanics. Einstein used it to explain the photoelectric effect (1905), Bohr used it for his atomic model (1913), and Heisenberg built his uncertainty principle upon it.\n\nPlanck endured extraordinary personal tragedy: his eldest son died in World War I, his twin daughters died in childbirth, and his second son Erwin was executed by the Nazis in 1945 for involvement in the July 20 plot against Hitler. The Max Planck Society, Germany's premier research organization, bears his name.",
        "causes": ["Black-body radiation problem (ultraviolet catastrophe) in classical physics", "Boltzmann's statistical mechanics and thermodynamic tradition", "19th-century German physics research culture"],
        "effects": ["Originated quantum theory, the foundational framework of modern physics", "Planck's constant became a fundamental constant of nature", "Nobel Prize 1918; Max Planck Society became Germany's leading research organization"],
        "relationships": [
            {"sourceSlug": "max-planck", "sourceName": "Max Planck", "verb": "INFLUENCES", "targetSlug": "albert-einstein", "targetName": "Albert Einstein", "context": "Einstein used Planck's quantisation to explain the photoelectric effect in 1905"},
            {"sourceSlug": "max-planck", "sourceName": "Max Planck", "verb": "INFLUENCES", "targetSlug": "niels-bohr", "targetName": "Niels Bohr", "context": "Bohr used Planck's constant in his 1913 atomic model"},
            {"sourceSlug": "max-planck", "sourceName": "Max Planck", "verb": "CREATES", "targetSlug": "quantum-theory", "targetName": "Quantum Theory", "context": "Proposed energy quantisation in 1900, founding quantum physics"},
            {"sourceSlug": "max-planck", "sourceName": "Max Planck", "verb": "OCCURS_IN", "targetSlug": "berlin", "targetName": "Berlin", "context": "Professor at University of Berlin 1889-1928, center of his career"},
            {"sourceSlug": "max-planck", "sourceName": "Max Planck", "verb": "PARTICIPATES_IN", "targetSlug": "nobel-prize", "targetName": "Nobel Prize", "context": "Won Nobel Prize in Physics 1918 for quantum theory"}
        ],
        "places": [{"name": "Berlin, Germany", "role": "University career"}, {"name": "Kiel, Germany", "role": "Birthplace"}, {"name": "Gottingen, Germany", "role": "Final years"}],
        "subjects": ["Quantum Theory", "Theoretical Physics", "Planck Constant", "Nobel Prize", "Germany", "Black-Body Radiation", "Modern Physics", "Thermodynamics"],
        "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS", "COMPARATIVE_CIVILIZATIONS"]
    },
    "henry-v": {
        "summary": "Henry V (1386\u20131422) was King of England from 1413 to 1422 and the warrior-king whose stunning victory at the Battle of Agincourt (1415) against overwhelming French odds made him a legendary figure in English history. His military campaigns during the Hundred Years' War brought England closer to conquering France than at any other time.\n\nThe eldest son of Henry IV, he proved himself in combat during the Welsh revolt of Owain Glynd\u0175r, where he was wounded by an arrow to the face at the Battle of Shrewsbury (1403) at age 16. As king, he reunited a divided English nobility and launched his invasion of France in August 1415.\n\nAt Agincourt on October 25, 1415, Henry's exhausted, dysentery-ravaged army of roughly 6,000\u2014mostly longbowmen\u2014defeated a French force of 12,000\u201336,000. The victory was so decisive that it forced the Treaty of Troyes (1420), which made Henry heir to the French throne and regent of France.\n\nHenry died of dysentery during the siege of Meaux on August 31, 1422, aged just 35\u2014only two months before the French king Charles VI. His infant son Henry VI inherited two kingdoms but held neither. Shakespeare's 'Henry V' immortalised the king's speech before Agincourt: 'We few, we happy few, we band of brothers.'",
        "causes": ["Lancastrian dynasty's need to legitimise rule through military glory", "Hundred Years' War dynastic claims to the French throne", "English longbow military superiority over French heavy cavalry"],
        "effects": ["Treaty of Troyes made English king heir to French throne", "Agincourt became foundational English national myth", "Shakespeare's dramatisation cemented Henry V as the ideal English king"],
        "relationships": [
            {"sourceSlug": "henry-v", "sourceName": "Henry V", "verb": "PARTICIPATES_IN", "targetSlug": "hundred-years-war", "targetName": "Hundred Years' War", "context": "Led English campaign in France 1415-1422, won Battle of Agincourt"},
            {"sourceSlug": "henry-v", "sourceName": "Henry V", "verb": "INFLUENCES", "targetSlug": "william-shakespeare", "targetName": "William Shakespeare", "context": "Shakespeare's 'Henry V' immortalised his Agincourt speech"},
            {"sourceSlug": "henry-v", "sourceName": "Henry V", "verb": "OCCURS_IN", "targetSlug": "agincourt", "targetName": "Agincourt", "context": "Decisive English victory October 25, 1415"},
            {"sourceSlug": "henry-v", "sourceName": "Henry V", "verb": "CAUSES", "targetSlug": "treaty-of-troyes", "targetName": "Treaty of Troyes", "context": "Military victories forced France to accept Henry as heir to the throne"},
            {"sourceSlug": "joan-of-arc", "sourceName": "Joan of Arc", "verb": "REVERSES", "targetSlug": "henry-v", "targetName": "Henry V", "context": "Joan's campaigns undid Henry's conquests after his death"}
        ],
        "places": [{"name": "Agincourt, France", "role": "Famous 1415 battle"}, {"name": "Monmouth, Wales", "role": "Birthplace"}, {"name": "Meaux, France", "role": "Death during siege"}],
        "subjects": ["Hundred Years War", "Medieval England", "Agincourt", "Military History", "England", "France", "Shakespeare", "Monarchy"],
        "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS", "COMPARATIVE_CIVILIZATIONS"]
    },
}

# ═══════════════════════════════════════════
# PART 2: CREATE 10 MISSING HIGH-IMPORTANCE ENTITIES
# ═══════════════════════════════════════════

NEW_ENTITIES = [
    {
        "slug": "rene-descartes",
        "name": "Ren\u00e9 Descartes",
        "label": "Person",
        "callNumber": "210.rene-descartes",
        "era": "Early Modern",
        "eraSlug": "early-modern",
        "eraDivision": "Early Modern",
        "eraDivisionCode": "940",
        "region": "Europe",
        "continent": "Europe",
        "status": "Published",
        "born": "1596-03-31",
        "died": "1650-02-11",
        "wikidataQid": "Q9191",
        "wikipediaUrl": "https://en.wikipedia.org/wiki/Ren%C3%A9_Descartes",
        "importanceScore": 9,
        "subjectHeadings": ["People \u2014 Philosophers \u2014 Europe \u2014 Early Modern"],
        "subjects": ["Rationalism", "Cartesian Philosophy", "Mathematics", "Analytical Geometry", "Mind-Body Problem", "France", "Scientific Method", "Enlightenment"],
        "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS", "COMPARATIVE_CIVILIZATIONS"],
        "summary": "Ren\u00e9 Descartes (1596\u20131650) was a French philosopher, mathematician, and scientist who is regarded as the father of modern Western philosophy. His declaration 'Cogito, ergo sum' ('I think, therefore I am') became the foundational certainty upon which he rebuilt all knowledge, and his method of systematic doubt revolutionised epistemology.\n\nDescartes invented analytical geometry\u2014the Cartesian coordinate system that unified algebra and geometry\u2014enabling the mathematical description of physical space that made Newton's physics possible. His 'Discourse on the Method' (1637) established the framework for scientific reasoning that persists to this day.\n\nHis mind-body dualism\u2014the radical separation of thinking substance (res cogitans) from extended substance (res extensa)\u2014framed three centuries of philosophical debate and profoundly influenced medicine, psychology, and cognitive science.\n\nDescartes spent most of his productive career in the Dutch Republic, seeking intellectual freedom. He died in Stockholm at age 53, having accepted an invitation from Queen Christina of Sweden. As Bertrand Russell wrote: 'He may justly be called the founder of modern philosophy.'",
        "detailsJson": {
            "causes": ["Scholastic philosophy's inability to answer sceptical challenges", "Galileo's mathematical approach to natural philosophy", "Dutch Republic's intellectual freedom from Catholic censorship"],
            "effects": ["Founded modern rationalist philosophy and epistemology", "Invented analytical geometry enabling Newton's mathematical physics", "Mind-body dualism shaped all subsequent philosophy of mind"],
            "relationships": [
                {"sourceSlug": "rene-descartes", "sourceName": "Ren\u00e9 Descartes", "verb": "INFLUENCES", "targetSlug": "baruch-spinoza", "targetName": "Baruch Spinoza", "context": "Spinoza's philosophy was a radical extension of Cartesian rationalism"},
                {"sourceSlug": "rene-descartes", "sourceName": "Ren\u00e9 Descartes", "verb": "INFLUENCES", "targetSlug": "isaac-newton", "targetName": "Isaac Newton", "context": "Cartesian coordinate system enabled Newton's mathematical physics"},
                {"sourceSlug": "rene-descartes", "sourceName": "Ren\u00e9 Descartes", "verb": "INFLUENCES", "targetSlug": "immanuel-kant", "targetName": "Immanuel Kant", "context": "Descartes' rationalism was one pole of the debate Kant sought to resolve"},
                {"sourceSlug": "rene-descartes", "sourceName": "Ren\u00e9 Descartes", "verb": "CREATES", "targetSlug": "discourse-on-method", "targetName": "Discourse on the Method", "context": "Published 1637, established scientific reasoning framework"},
                {"sourceSlug": "rene-descartes", "sourceName": "Ren\u00e9 Descartes", "verb": "OCCURS_IN", "targetSlug": "amsterdam", "targetName": "Amsterdam", "context": "Lived and worked in the Dutch Republic 1628-1649"}
            ],
            "places": [{"name": "La Haye en Touraine, France", "role": "Birthplace"}, {"name": "Amsterdam, Netherlands", "role": "Most productive period"}, {"name": "Stockholm, Sweden", "role": "Death"}]
        }
    },
    {
        "slug": "baruch-spinoza",
        "name": "Baruch Spinoza",
        "label": "Person",
        "callNumber": "210.baruch-spinoza",
        "era": "Early Modern",
        "eraSlug": "early-modern",
        "eraDivision": "Early Modern",
        "eraDivisionCode": "940",
        "region": "Europe",
        "continent": "Europe",
        "status": "Published",
        "born": "1632-11-24",
        "died": "1677-02-21",
        "wikidataQid": "Q35802",
        "wikipediaUrl": "https://en.wikipedia.org/wiki/Baruch_Spinoza",
        "importanceScore": 8,
        "subjectHeadings": ["People \u2014 Philosophers \u2014 Europe \u2014 Early Modern"],
        "subjects": ["Rationalism", "Pantheism", "Ethics", "Dutch Golden Age", "Netherlands", "Jewish Philosophy", "Determinism", "Political Philosophy"],
        "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS", "RELIGIOUS_INTERPRETATION"],
        "summary": "Baruch Spinoza (1632\u20131677) was a Dutch philosopher of Portuguese-Jewish origin whose 'Ethics' (1677)\u2014written in geometric proof form\u2014is one of the most rigorous and radical works in Western philosophy. Excommunicated by the Amsterdam Sephardic community at age 23, he spent his life quietly grinding optical lenses while constructing a philosophical system that identified God with Nature.\n\nSpinoza's monism\u2014the doctrine that there is only one substance (God/Nature) with infinite attributes\u2014demolished the Cartesian mind-body split and anticipated modern scientific naturalism. His denial of free will, miracles, and personal divine providence made 'Spinozism' synonymous with atheism for over a century.\n\nHis 'Theologico-Political Treatise' (1670) was the first systematic argument for freedom of thought and separation of church and state, making him a forerunner of liberal democracy and biblical scholarship.\n\nHegel called him 'the crucial point of modern philosophy: either Spinozism or no philosophy.' Einstein, asked if he believed in God, replied: 'I believe in Spinoza's God, who reveals himself in the lawful harmony of all that exists.' Spinoza died at 44 of lung disease, likely from glass dust inhaled while grinding lenses.",
        "detailsJson": {
            "causes": ["Cartesian rationalism as philosophical starting point", "Sephardic Jewish community's intellectual traditions in Amsterdam", "Dutch Republic's relative tolerance and freedom of thought"],
            "effects": ["Pantheism influenced Romantic movement and German Idealism", "Freedom of thought arguments foundational to liberal democracy", "Einstein and modern physicists embraced Spinoza's deterministic naturalism"],
            "relationships": [
                {"sourceSlug": "rene-descartes", "sourceName": "Ren\u00e9 Descartes", "verb": "INFLUENCES", "targetSlug": "baruch-spinoza", "targetName": "Baruch Spinoza", "context": "Spinoza radicalised Cartesian rationalism into monist system"},
                {"sourceSlug": "baruch-spinoza", "sourceName": "Baruch Spinoza", "verb": "INFLUENCES", "targetSlug": "albert-einstein", "targetName": "Albert Einstein", "context": "Einstein declared belief in 'Spinoza's God'"},
                {"sourceSlug": "baruch-spinoza", "sourceName": "Baruch Spinoza", "verb": "INFLUENCES", "targetSlug": "immanuel-kant", "targetName": "Immanuel Kant", "context": "Spinoza's rationalism was essential context for Kant's critical philosophy"},
                {"sourceSlug": "baruch-spinoza", "sourceName": "Baruch Spinoza", "verb": "CREATES", "targetSlug": "ethics-spinoza", "targetName": "Ethics", "context": "Published posthumously 1677, geometric-proof philosophy masterwork"},
                {"sourceSlug": "baruch-spinoza", "sourceName": "Baruch Spinoza", "verb": "OCCURS_IN", "targetSlug": "the-hague", "targetName": "The Hague", "context": "Lived and worked in The Hague from 1670 until death in 1677"}
            ],
            "places": [{"name": "Amsterdam, Netherlands", "role": "Birthplace and excommunication"}, {"name": "The Hague, Netherlands", "role": "Final home and death"}, {"name": "Leiden, Netherlands", "role": "University connections"}]
        }
    },
    {
        "slug": "miguel-de-cervantes",
        "name": "Miguel de Cervantes",
        "label": "Person",
        "callNumber": "260.miguel-de-cervantes",
        "era": "Early Modern",
        "eraSlug": "early-modern",
        "eraDivision": "Early Modern",
        "eraDivisionCode": "940",
        "region": "Europe",
        "continent": "Europe",
        "status": "Published",
        "born": "1547-09-29",
        "died": "1616-04-22",
        "wikidataQid": "Q5682",
        "wikipediaUrl": "https://en.wikipedia.org/wiki/Miguel_de_Cervantes",
        "importanceScore": 9,
        "subjectHeadings": ["People \u2014 Authors & Writers \u2014 Europe \u2014 Early Modern"],
        "subjects": ["Spanish Literature", "Don Quixote", "Golden Age Spain", "Novel", "Spain", "Satire", "Chivalric Romance", "World Literature"],
        "frameworks": ["CULTURAL_TRANSMISSION", "CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"],
        "summary": "Miguel de Cervantes Saavedra (1547\u20131616) was a Spanish novelist, poet, and playwright whose 'Don Quixote' (Part I, 1605; Part II, 1615) is widely considered the first modern novel and the most influential work of fiction in the Spanish language. It has been translated into more languages than any book except the Bible.\n\nCervantes led a life as adventurous as his fiction. He fought at the Battle of Lepanto (1571), where he lost the use of his left hand, earning the nickname 'el manco de Lepanto.' He was captured by Barbary pirates and spent five years as a slave in Algiers before being ransomed.\n\nReturning to Spain impoverished, he worked as a tax collector and was imprisoned at least twice. He began 'Don Quixote' reportedly while in jail. The novel's genius lay in its layered irony: a delusional knight-errant tilting at windmills became a profound meditation on reality, fiction, idealism, and the human condition.\n\nCervantes died on April 22, 1616\u2014one day before Shakespeare. The Cervantes Prize (Premio Cervantes) is the most prestigious award in Spanish-language literature. As Dostoyevsky wrote: 'Don Quixote is the most profound and most lasting work of all literature.'",
        "detailsJson": {
            "causes": ["Spanish Golden Age literary and cultural flowering", "Personal experience of war, captivity, and poverty", "Chivalric romance tradition he both parodied and transcended"],
            "effects": ["Invented the modern novel through unreliable narration and metafiction", "Don Quixote became the most translated fictional work after the Bible", "Established Spanish as a major world literary language"],
            "relationships": [
                {"sourceSlug": "miguel-de-cervantes", "sourceName": "Miguel de Cervantes", "verb": "CREATES", "targetSlug": "don-quixote", "targetName": "Don Quixote", "context": "Published 1605/1615, considered the first modern novel"},
                {"sourceSlug": "miguel-de-cervantes", "sourceName": "Miguel de Cervantes", "verb": "INFLUENCES", "targetSlug": "fyodor-dostoevsky", "targetName": "Fyodor Dostoevsky", "context": "Dostoevsky called Don Quixote 'the most profound work of all literature'"},
                {"sourceSlug": "miguel-de-cervantes", "sourceName": "Miguel de Cervantes", "verb": "INFLUENCES", "targetSlug": "william-shakespeare", "targetName": "William Shakespeare", "context": "Contemporaries who died within days of each other; both transformed their literatures"},
                {"sourceSlug": "miguel-de-cervantes", "sourceName": "Miguel de Cervantes", "verb": "OCCURS_IN", "targetSlug": "madrid", "targetName": "Madrid", "context": "Lived and wrote in Madrid; died and buried there"},
                {"sourceSlug": "miguel-de-cervantes", "sourceName": "Miguel de Cervantes", "verb": "PARTICIPATES_IN", "targetSlug": "battle-of-lepanto", "targetName": "Battle of Lepanto", "context": "Fought and was wounded at Lepanto 1571, lost use of left hand"}
            ],
            "places": [{"name": "Madrid, Spain", "role": "Home and death"}, {"name": "Alcala de Henares, Spain", "role": "Birthplace"}, {"name": "Algiers, Algeria", "role": "Five years' captivity"}]
        }
    },
    {
        "slug": "johann-wolfgang-von-goethe",
        "name": "Johann Wolfgang von Goethe",
        "label": "Person",
        "callNumber": "260.johann-wolfgang-von-goethe",
        "era": "Early Modern",
        "eraSlug": "early-modern",
        "eraDivision": "Early Modern",
        "eraDivisionCode": "940",
        "region": "Europe",
        "continent": "Europe",
        "status": "Published",
        "born": "1749-08-28",
        "died": "1832-03-22",
        "wikidataQid": "Q5879",
        "wikipediaUrl": "https://en.wikipedia.org/wiki/Johann_Wolfgang_von_Goethe",
        "importanceScore": 9,
        "subjectHeadings": ["People \u2014 Authors & Writers \u2014 Europe \u2014 Early Modern"],
        "subjects": ["German Literature", "Romanticism", "Weimar Classicism", "Faust", "Germany", "Poetry", "Natural Science", "Enlightenment"],
        "frameworks": ["CULTURAL_TRANSMISSION", "CAUSE_AND_EFFECT", "COMPARATIVE_CIVILIZATIONS"],
        "summary": "Johann Wolfgang von Goethe (1749\u20131832) was a German writer, statesman, and polymath who is regarded as the greatest figure in German literature and one of the most towering intellects of the modern era. His two-part dramatic poem 'Faust' (1808/1832) is considered the supreme achievement of German literature.\n\nGoethe's 'The Sorrows of Young Werther' (1774) made him an overnight sensation across Europe, inspiring a wave of suicides and launching the Sturm und Drang literary movement. As privy councillor and minister in Weimar, he managed a duchy while producing poetry, drama, novels, and scientific works across six decades.\n\nBeyond literature, Goethe made significant contributions to natural science: his 'Theory of Colours' (1810) challenged Newton's optics, his botanical studies anticipated evolutionary theory, and he discovered the human intermaxillary bone. He corresponded with virtually every major intellectual of his age, from Schiller to Napoleon.\n\nNapoleon, upon meeting him, reportedly said: 'Voil\u00e0 un homme!' ('There is a man!'). Goethe's final words\u2014'Mehr Licht!' ('More light!')\u2014became symbolic of the Enlightenment project he embodied. His influence pervades German culture, philosophy, music, and science.",
        "detailsJson": {
            "causes": ["German Enlightenment (Aufklarung) intellectual tradition", "Sturm und Drang literary movement's emphasis on emotion and nature", "Weimar court patronage providing lifelong creative support"],
            "effects": ["Defined German literary language and national cultural identity", "'Faust' influenced Berlioz, Liszt, Wagner, Mann, and modern philosophy", "Theory of Colours influenced Impressionist painters and phenomenology"],
            "relationships": [
                {"sourceSlug": "johann-wolfgang-von-goethe", "sourceName": "Johann Wolfgang von Goethe", "verb": "COLLABORATES_WITH", "targetSlug": "friedrich-schiller", "targetName": "Friedrich Schiller", "context": "Weimar Classicism partnership 1794-1805, defining German literary culture"},
                {"sourceSlug": "johann-wolfgang-von-goethe", "sourceName": "Johann Wolfgang von Goethe", "verb": "INFLUENCES", "targetSlug": "ludwig-van-beethoven", "targetName": "Ludwig van Beethoven", "context": "Beethoven set Goethe's poetry to music and sought his friendship"},
                {"sourceSlug": "johann-wolfgang-von-goethe", "sourceName": "Johann Wolfgang von Goethe", "verb": "CREATES", "targetSlug": "faust-goethe", "targetName": "Faust", "context": "Two-part dramatic poem (1808/1832), supreme achievement of German literature"},
                {"sourceSlug": "johann-wolfgang-von-goethe", "sourceName": "Johann Wolfgang von Goethe", "verb": "OCCURS_IN", "targetSlug": "weimar", "targetName": "Weimar", "context": "Lived and served as minister in Weimar from 1775 until death in 1832"},
                {"sourceSlug": "napoleon-bonaparte", "sourceName": "Napoleon Bonaparte", "verb": "COLLABORATES_WITH", "targetSlug": "johann-wolfgang-von-goethe", "targetName": "Johann Wolfgang von Goethe", "context": "Napoleon met Goethe at Erfurt 1808, awarded him the Legion of Honour"}
            ],
            "places": [{"name": "Weimar, Germany", "role": "Lifelong home and court service"}, {"name": "Frankfurt, Germany", "role": "Birthplace"}, {"name": "Rome, Italy", "role": "Transformative Italian journey 1786-1788"}]
        }
    },
    {
        "slug": "frederic-chopin",
        "name": "Fr\u00e9d\u00e9ric Chopin",
        "label": "Person",
        "callNumber": "263.frederic-chopin",
        "era": "Modern",
        "eraSlug": "modern",
        "eraDivision": "Modern",
        "eraDivisionCode": "950",
        "region": "Europe",
        "continent": "Europe",
        "status": "Published",
        "born": "1810-03-01",
        "died": "1849-10-17",
        "wikidataQid": "Q1268",
        "wikipediaUrl": "https://en.wikipedia.org/wiki/Fr%C3%A9d%C3%A9ric_Chopin",
        "importanceScore": 8,
        "subjectHeadings": ["People \u2014 Musicians & Composers \u2014 Europe \u2014 Modern"],
        "subjects": ["Romantic Music", "Piano", "Poland", "France", "Nocturne", "Polonaise", "Composition", "Nationalism"],
        "frameworks": ["CULTURAL_TRANSMISSION", "CAUSE_AND_EFFECT", "PSYCHOLOGICAL_ANALYSIS"],
        "summary": "Fr\u00e9d\u00e9ric Chopin (1810\u20131849) was a Polish composer and virtuoso pianist of the Romantic era who wrote primarily for solo piano. His compositions\u2014including 27 \u00e9tudes, 21 nocturnes, 16 polonaises, and 4 ballades\u2014transformed the instrument's expressive possibilities and remain central to the piano repertoire.\n\nBorn near Warsaw, Chopin was a child prodigy who gave his first public concert at age seven. After the failed November Uprising of 1830 against Russian rule, he settled permanently in Paris, becoming the darling of Parisian salons while nursing a profound homesickness for Poland that infuses his polonaises and mazurkas with patriotic yearning.\n\nChopin preferred intimate salon performances to large concert halls. His ten-year relationship with the novelist George Sand (1838\u20131847) coincided with his most productive period. He revolutionised piano technique through innovations in pedalling, rubato, and finger independence that expanded the instrument's tonal palette.\n\nDying of tuberculosis at 39, Chopin requested that his heart be removed and returned to Poland\u2014it is now enshrined in a pillar at the Church of the Holy Cross in Warsaw. Schumann described his music perfectly: 'Hats off, gentlemen\u2014a genius.'",
        "detailsJson": {
            "causes": ["Polish national musical tradition and folk dance forms (mazurka, polonaise)", "November Uprising of 1830 and Polish exile diaspora", "Parisian salon culture and Romantic movement artistic networks"],
            "effects": ["Revolutionised piano technique and expanded the instrument's expressive range", "His polonaises and mazurkas became symbols of Polish national identity", "Influenced Liszt, Debussy, Scriabin, and all subsequent piano composers"],
            "relationships": [
                {"sourceSlug": "frederic-chopin", "sourceName": "Fr\u00e9d\u00e9ric Chopin", "verb": "COLLABORATES_WITH", "targetSlug": "franz-liszt", "targetName": "Franz Liszt", "context": "Close friends in Paris; Liszt championed Chopin's music and wrote his biography"},
                {"sourceSlug": "frederic-chopin", "sourceName": "Fr\u00e9d\u00e9ric Chopin", "verb": "INFLUENCES", "targetSlug": "ludwig-van-beethoven", "targetName": "Ludwig van Beethoven", "context": "Built on Beethoven's piano sonata tradition while creating intimate forms"},
                {"sourceSlug": "frederic-chopin", "sourceName": "Fr\u00e9d\u00e9ric Chopin", "verb": "OCCURS_IN", "targetSlug": "paris", "targetName": "Paris", "context": "Lived and composed in Paris from 1831 until death in 1849"},
                {"sourceSlug": "johann-sebastian-bach", "sourceName": "Johann Sebastian Bach", "verb": "INFLUENCES", "targetSlug": "frederic-chopin", "targetName": "Fr\u00e9d\u00e9ric Chopin", "context": "Chopin studied and revered Bach's Well-Tempered Clavier as his daily practice"},
                {"sourceSlug": "frederic-chopin", "sourceName": "Fr\u00e9d\u00e9ric Chopin", "verb": "PARTICIPATES_IN", "targetSlug": "polish-diaspora", "targetName": "Polish Diaspora", "context": "Exile after 1830 uprising; his music became symbol of Polish identity"}
            ],
            "places": [{"name": "Paris, France", "role": "Adopted home and career"}, {"name": "Zelazowa Wola, Poland", "role": "Birthplace"}, {"name": "Majorca, Spain", "role": "Winter with George Sand, composed Preludes"}]
        }
    },
    {
        "slug": "george-orwell",
        "name": "George Orwell",
        "label": "Person",
        "callNumber": "260.george-orwell",
        "era": "Contemporary",
        "eraSlug": "contemporary",
        "eraDivision": "Contemporary",
        "eraDivisionCode": "960",
        "region": "Europe",
        "continent": "Europe",
        "status": "Published",
        "born": "1903-06-25",
        "died": "1950-01-21",
        "wikidataQid": "Q3335",
        "wikipediaUrl": "https://en.wikipedia.org/wiki/George_Orwell",
        "importanceScore": 9,
        "subjectHeadings": ["People \u2014 Authors & Writers \u2014 Europe \u2014 Contemporary"],
        "subjects": ["Dystopian Fiction", "Political Satire", "Totalitarianism", "English Literature", "England", "Spanish Civil War", "Journalism", "Socialism"],
        "frameworks": ["CAUSE_AND_EFFECT", "WORLD_SYSTEMS", "STRUCTURAL_ANALYSIS"],
        "summary": "George Orwell (1903\u20131950), born Eric Arthur Blair, was an English novelist, essayist, and critic whose works 'Animal Farm' (1945) and 'Nineteen Eighty-Four' (1949) are the two most influential political novels of the 20th century. His name became an adjective\u2014'Orwellian'\u2014denoting the surveillance state, propaganda, and linguistic manipulation he warned against.\n\nOrwell served as an Imperial Police officer in Burma, fought with the POUM militia in the Spanish Civil War (where he was shot through the throat), and lived deliberately among the poor in Paris and London. These experiences forged his commitment to democratic socialism and his hatred of totalitarianism in all forms.\n\n'Animal Farm' (1945) satirised the Soviet revolution as a farmyard fable. 'Nineteen Eighty-Four' (1949)\u2014written while dying of tuberculosis on the Scottish island of Jura\u2014gave the world Big Brother, doublethink, thoughtcrime, and Newspeak. The novel has sold over 50 million copies and surges in sales whenever authoritarianism rises.\n\nOrwell's six rules for clear writing ('Politics and the English Language,' 1946) remain the gold standard for prose style. As Christopher Hitchens wrote: 'He faced the totalitarian threat with an understanding that was superior to that of the professionals.'",
        "detailsJson": {
            "causes": ["British colonial experience in Burma (1922-1927)", "Spanish Civil War combat experience against fascism", "Rise of Stalinist totalitarianism and Nazi propaganda"],
            "effects": ["'Orwellian' entered global vocabulary for authoritarian surveillance", "'1984' and 'Animal Farm' shaped Cold War political consciousness", "Established political clarity as the highest literary virtue"],
            "relationships": [
                {"sourceSlug": "george-orwell", "sourceName": "George Orwell", "verb": "CREATES", "targetSlug": "nineteen-eighty-four", "targetName": "Nineteen Eighty-Four", "context": "Published 1949, defining dystopian novel of the 20th century"},
                {"sourceSlug": "george-orwell", "sourceName": "George Orwell", "verb": "PARTICIPATES_IN", "targetSlug": "spanish-civil-war", "targetName": "Spanish Civil War", "context": "Fought with POUM militia in Catalonia 1936-1937, shot through throat"},
                {"sourceSlug": "joseph-stalin", "sourceName": "Joseph Stalin", "verb": "INFLUENCES", "targetSlug": "george-orwell", "targetName": "George Orwell", "context": "Stalin's purges and propaganda directly inspired Animal Farm and 1984"},
                {"sourceSlug": "george-orwell", "sourceName": "George Orwell", "verb": "OCCURS_IN", "targetSlug": "london", "targetName": "London", "context": "London setting of 1984; Orwell lived and died in London"},
                {"sourceSlug": "george-orwell", "sourceName": "George Orwell", "verb": "INFLUENCES", "targetSlug": "margaret-thatcher", "targetName": "Margaret Thatcher", "context": "Orwell's anti-totalitarian legacy influenced Cold War political thought across the spectrum"}
            ],
            "places": [{"name": "London, England", "role": "Home and literary setting"}, {"name": "Jura, Scotland", "role": "Wrote 1984"}, {"name": "Barcelona, Spain", "role": "Spanish Civil War service"}]
        }
    },
    {
        "slug": "ho-chi-minh",
        "name": "Ho Chi Minh",
        "label": "Person",
        "callNumber": "222.ho-chi-minh",
        "era": "Contemporary",
        "eraSlug": "contemporary",
        "eraDivision": "Contemporary",
        "eraDivisionCode": "960",
        "region": "Asia",
        "continent": "Asia",
        "status": "Published",
        "born": "1890-05-19",
        "died": "1969-09-02",
        "wikidataQid": "Q36014",
        "wikipediaUrl": "https://en.wikipedia.org/wiki/Ho_Chi_Minh",
        "importanceScore": 8,
        "subjectHeadings": ["People \u2014 Heads of State \u2014 Asia \u2014 Contemporary"],
        "subjects": ["Vietnamese Independence", "Communism", "Decolonisation", "Vietnam War", "Vietnam", "Anti-Colonialism", "Cold War", "Guerrilla Warfare"],
        "frameworks": ["CAUSE_AND_EFFECT", "WORLD_SYSTEMS", "MARXIST_ANALYSIS"],
        "summary": "Ho Chi Minh (1890\u20131969) was a Vietnamese revolutionary leader who founded the Viet Minh, defeated French colonialism, and established the Democratic Republic of Vietnam. His pursuit of Vietnamese independence and reunification shaped the most consequential Cold War conflict, the Vietnam War (1955\u20131975).\n\nBorn Nguyen Sinh Cung in central Vietnam, he travelled the world for 30 years\u2014working as a kitchen hand in London, a photo retoucher in Paris, and a Comintern agent in Moscow and China. In Paris, he petitioned the Versailles Peace Conference for Vietnamese self-determination; ignored, he became a founding member of the French Communist Party (1920).\n\nReturning to Vietnam in 1941, he founded the Viet Minh independence movement. His forces defeated the French at the decisive Battle of Dien Bien Phu (1954), ending nearly a century of French colonial rule. As president of North Vietnam, he led resistance against American military intervention until his death in 1969.\n\nHo's declaration of Vietnamese independence on September 2, 1945 deliberately quoted the American Declaration of Independence and the French Declaration of the Rights of Man. He died six years before Saigon fell and Vietnam was reunified. The former Saigon was renamed Ho Chi Minh City in his honour.",
        "detailsJson": {
            "causes": ["French colonial exploitation of Vietnam (1887-1954)", "Versailles Conference's refusal of Vietnamese self-determination", "Marxist-Leninist theory of anti-colonial national liberation"],
            "effects": ["Defeated French colonialism at Dien Bien Phu (1954)", "Inspired global anti-colonial and anti-imperialist movements", "Vietnam War became defining Cold War conflict, reshaping US foreign policy"],
            "relationships": [
                {"sourceSlug": "ho-chi-minh", "sourceName": "Ho Chi Minh", "verb": "CAUSES", "targetSlug": "vietnam-war", "targetName": "Vietnam War", "context": "His independence movement led to the Vietnam War after the French defeat"},
                {"sourceSlug": "ho-chi-minh", "sourceName": "Ho Chi Minh", "verb": "PARTICIPATES_IN", "targetSlug": "battle-of-dien-bien-phu", "targetName": "Battle of Dien Bien Phu", "context": "Viet Minh victory ended French colonial rule in Vietnam, 1954"},
                {"sourceSlug": "karl-marx", "sourceName": "Karl Marx", "verb": "INFLUENCES", "targetSlug": "ho-chi-minh", "targetName": "Ho Chi Minh", "context": "Marxist-Leninist theory provided ideological framework for Vietnamese revolution"},
                {"sourceSlug": "ho-chi-minh", "sourceName": "Ho Chi Minh", "verb": "OCCURS_IN", "targetSlug": "hanoi", "targetName": "Hanoi", "context": "Led North Vietnam from Hanoi 1945-1969"},
                {"sourceSlug": "ho-chi-minh", "sourceName": "Ho Chi Minh", "verb": "INFLUENCES", "targetSlug": "fidel-castro", "targetName": "Fidel Castro", "context": "Ho's anti-colonial guerrilla model influenced revolutionary movements worldwide"}
            ],
            "places": [{"name": "Hanoi, Vietnam", "role": "Capital and presidential seat"}, {"name": "Nghe An Province, Vietnam", "role": "Birthplace"}, {"name": "Paris, France", "role": "Political awakening and party founding"}]
        }
    },
    {
        "slug": "stephen-hawking",
        "name": "Stephen Hawking",
        "label": "Person",
        "callNumber": "240.stephen-hawking",
        "era": "Contemporary",
        "eraSlug": "contemporary",
        "eraDivision": "Contemporary",
        "eraDivisionCode": "960",
        "region": "Europe",
        "continent": "Europe",
        "status": "Published",
        "born": "1942-01-08",
        "died": "2018-03-14",
        "wikidataQid": "Q17714",
        "wikipediaUrl": "https://en.wikipedia.org/wiki/Stephen_Hawking",
        "importanceScore": 8,
        "subjectHeadings": ["People \u2014 Scientists & Researchers \u2014 Europe \u2014 Contemporary"],
        "subjects": ["Theoretical Physics", "Cosmology", "Black Holes", "Hawking Radiation", "England", "Disability", "Science Communication", "General Relativity"],
        "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS", "COMPARATIVE_CIVILIZATIONS"],
        "summary": "Stephen William Hawking (1942\u20132018) was an English theoretical physicist and cosmologist whose work on black holes, singularity theorems, and the nature of time made him the most celebrated scientist since Einstein. Diagnosed with motor neurone disease at 21 and given two years to live, he survived for 55 more years, communicating through a speech synthesiser that became one of the most recognisable voices in the world.\n\nHawking's singularity theorems (with Roger Penrose, 1970) proved that black holes are a necessary consequence of general relativity. His greatest discovery\u2014Hawking radiation (1974)\u2014showed that black holes emit thermal radiation and eventually evaporate, uniting quantum mechanics, thermodynamics, and general relativity in a single result.\n\n'A Brief History of Time' (1988) sold over 25 million copies, making cosmology accessible to general readers and establishing Hawking as the world's most famous living scientist. He held the Lucasian Chair of Mathematics at Cambridge\u2014Newton's former position\u2014from 1979 to 2009.\n\nHawking became a cultural icon: appearing on 'The Simpsons,' 'Star Trek,' and 'The Big Bang Theory.' He died on March 14, 2018\u2014Pi Day and the anniversary of Einstein's birth. His ashes were interred in Westminster Abbey between Newton and Darwin.",
        "detailsJson": {
            "causes": ["Penrose's work on gravitational singularities in general relativity", "Wheeler and Bekenstein's early black hole thermodynamics", "Personal determination to work despite progressive motor neurone disease"],
            "effects": ["Hawking radiation unified quantum mechanics and general relativity", "'A Brief History of Time' made cosmology a popular subject worldwide", "Became iconic symbol of human triumph over physical limitation"],
            "relationships": [
                {"sourceSlug": "stephen-hawking", "sourceName": "Stephen Hawking", "verb": "CREATES", "targetSlug": "hawking-radiation", "targetName": "Hawking Radiation", "context": "Predicted in 1974 that black holes emit thermal radiation and evaporate"},
                {"sourceSlug": "albert-einstein", "sourceName": "Albert Einstein", "verb": "INFLUENCES", "targetSlug": "stephen-hawking", "targetName": "Stephen Hawking", "context": "Hawking's work extended Einstein's general relativity to black hole physics"},
                {"sourceSlug": "stephen-hawking", "sourceName": "Stephen Hawking", "verb": "OCCURS_IN", "targetSlug": "cambridge", "targetName": "Cambridge", "context": "Lucasian Professor at Cambridge 1979-2009, Newton's former chair"},
                {"sourceSlug": "stephen-hawking", "sourceName": "Stephen Hawking", "verb": "CREATES", "targetSlug": "brief-history-of-time", "targetName": "A Brief History of Time", "context": "Published 1988, sold 25 million copies, popularising cosmology"},
                {"sourceSlug": "isaac-newton", "sourceName": "Isaac Newton", "verb": "INFLUENCES", "targetSlug": "stephen-hawking", "targetName": "Stephen Hawking", "context": "Hawking held Newton's Lucasian Chair and extended gravitational physics"}
            ],
            "places": [{"name": "Cambridge, England", "role": "Career and Lucasian Chair"}, {"name": "Oxford, England", "role": "Birthplace and undergraduate"}, {"name": "Westminster Abbey, London", "role": "Burial between Newton and Darwin"}]
        }
    },
    {
        "slug": "j-robert-oppenheimer",
        "name": "J. Robert Oppenheimer",
        "label": "Person",
        "callNumber": "240.j-robert-oppenheimer",
        "era": "Contemporary",
        "eraSlug": "contemporary",
        "eraDivision": "Contemporary",
        "eraDivisionCode": "960",
        "region": "North America",
        "continent": "North America",
        "status": "Published",
        "born": "1904-04-22",
        "died": "1967-02-18",
        "wikidataQid": "Q131538",
        "wikipediaUrl": "https://en.wikipedia.org/wiki/J._Robert_Oppenheimer",
        "importanceScore": 8,
        "subjectHeadings": ["People \u2014 Scientists & Researchers \u2014 North America \u2014 Contemporary"],
        "subjects": ["Nuclear Physics", "Manhattan Project", "Atomic Bomb", "Cold War", "United States", "Los Alamos", "Science Ethics", "McCarthyism"],
        "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS", "WORLD_SYSTEMS"],
        "summary": "J. Robert Oppenheimer (1904\u20131967) was an American theoretical physicist who directed the Los Alamos Laboratory and led the Manhattan Project that developed the first nuclear weapons during World War II. His role as 'father of the atomic bomb' made him the most consequential\u2014and most conflicted\u2014scientist of the 20th century.\n\nA prodigy educated at Harvard, Cambridge, and G\u00f6ttingen, Oppenheimer made contributions to quantum mechanics, cosmic ray theory, and neutron star physics before being recruited to lead the Manhattan Project in 1942. He assembled the greatest concentration of scientific talent in history at Los Alamos, New Mexico.\n\nAfter witnessing the Trinity test on July 16, 1945, Oppenheimer famously recalled the Bhagavad Gita: 'Now I am become Death, the destroyer of worlds.' The bombs dropped on Hiroshima and Nagasaki killed over 200,000 people and ended World War II, but also launched the nuclear arms race.\n\nOppenheimer opposed the development of the hydrogen bomb on moral and strategic grounds. In 1954, during the McCarthy era, the AEC revoked his security clearance in a humiliating hearing. He was posthumously rehabilitated in 2022. His story remains the defining parable of science, power, and moral responsibility.",
        "detailsJson": {
            "causes": ["Discovery of nuclear fission by Hahn and Strassmann (1938)", "World War II urgency and fear of Nazi atomic weapons program", "Roosevelt's authorisation of the Manhattan Project (1942)"],
            "effects": ["Atomic bombs ended World War II and launched the nuclear age", "Nuclear arms race defined Cold War geopolitics for 45 years", "His story became the central parable of scientific ethics and responsibility"],
            "relationships": [
                {"sourceSlug": "j-robert-oppenheimer", "sourceName": "J. Robert Oppenheimer", "verb": "CREATES", "targetSlug": "manhattan-project", "targetName": "Manhattan Project", "context": "Directed Los Alamos Laboratory, built the first atomic bombs 1942-1945"},
                {"sourceSlug": "albert-einstein", "sourceName": "Albert Einstein", "verb": "INFLUENCES", "targetSlug": "j-robert-oppenheimer", "targetName": "J. Robert Oppenheimer", "context": "Einstein's E=mc2 and letter to Roosevelt initiated the chain leading to the bomb"},
                {"sourceSlug": "j-robert-oppenheimer", "sourceName": "J. Robert Oppenheimer", "verb": "CAUSES", "targetSlug": "hiroshima", "targetName": "Hiroshima", "context": "Atomic bomb developed under his direction dropped on Hiroshima August 6, 1945"},
                {"sourceSlug": "j-robert-oppenheimer", "sourceName": "J. Robert Oppenheimer", "verb": "OCCURS_IN", "targetSlug": "los-alamos", "targetName": "Los Alamos", "context": "Directed the Los Alamos Laboratory 1943-1945"},
                {"sourceSlug": "enrico-fermi", "sourceName": "Enrico Fermi", "verb": "COLLABORATES_WITH", "targetSlug": "j-robert-oppenheimer", "targetName": "J. Robert Oppenheimer", "context": "Fermi's Chicago Pile-1 reactor produced the plutonium for the bomb"}
            ],
            "places": [{"name": "Los Alamos, New Mexico", "role": "Manhattan Project laboratory"}, {"name": "New York City, USA", "role": "Birthplace"}, {"name": "Princeton, New Jersey", "role": "IAS directorship post-war"}]
        }
    },
    {
        "slug": "pyotr-ilyich-tchaikovsky",
        "name": "Pyotr Ilyich Tchaikovsky",
        "label": "Person",
        "callNumber": "263.pyotr-ilyich-tchaikovsky",
        "era": "Modern",
        "eraSlug": "modern",
        "eraDivision": "Modern",
        "eraDivisionCode": "950",
        "region": "Europe",
        "continent": "Europe",
        "status": "Published",
        "born": "1840-05-07",
        "died": "1893-11-06",
        "wikidataQid": "Q7315",
        "wikipediaUrl": "https://en.wikipedia.org/wiki/Pyotr_Ilyich_Tchaikovsky",
        "importanceScore": 8,
        "subjectHeadings": ["People \u2014 Musicians & Composers \u2014 Europe \u2014 Modern"],
        "subjects": ["Romantic Music", "Russian Music", "Ballet", "Symphony", "Russia", "Swan Lake", "Nutcracker", "Composition"],
        "frameworks": ["CULTURAL_TRANSMISSION", "CAUSE_AND_EFFECT", "PSYCHOLOGICAL_ANALYSIS"],
        "summary": "Pyotr Ilyich Tchaikovsky (1840\u20131893) was a Russian composer of the Romantic era whose works\u2014including the ballets 'Swan Lake' (1877), 'The Sleeping Beauty' (1890), and 'The Nutcracker' (1892)\u2014are among the most frequently performed compositions in the classical repertoire worldwide.\n\nTrained at the St. Petersburg Conservatory, Tchaikovsky fused Western European musical forms with Russian melodic sensibility. His six symphonies, three piano concertos, and the Violin Concerto in D major combine structural sophistication with an emotional directness that appeals to audiences universally. The 1812 Overture, with its cannon fire, remains one of the most recognisable pieces of classical music.\n\nTchaikovsky's personal life was marked by inner turmoil. His brief, disastrous marriage in 1877 and the patronage of Nadezhda von Meck\u2014a wealthy widow who supported him financially for 13 years on condition they never meet\u2014reflected his struggle with his homosexuality in a deeply conservative society.\n\nHe died in St. Petersburg at age 53, days after the premiere of his Sixth Symphony ('Path\u00e9tique')\u2014a work of devastating emotional power that he considered his finest. Whether he died of cholera or suicide remains debated. Stravinsky called him 'the most Russian of us all.'",
        "detailsJson": {
            "causes": ["Russian musical nationalism and the 'Mighty Handful' influence", "Western European symphonic and balletic traditions via conservatory training", "Patronage of Nadezhda von Meck providing financial freedom (1877-1890)"],
            "effects": ["Elevated ballet from entertainment to high art through Swan Lake, Sleeping Beauty, Nutcracker", "1812 Overture and Nutcracker became globally recognised cultural touchstones", "Influenced Rachmaninoff, Stravinsky, and all subsequent Russian composers"],
            "relationships": [
                {"sourceSlug": "pyotr-ilyich-tchaikovsky", "sourceName": "Pyotr Ilyich Tchaikovsky", "verb": "INFLUENCES", "targetSlug": "igor-stravinsky", "targetName": "Igor Stravinsky", "context": "Stravinsky called Tchaikovsky 'the most Russian of us all' and absorbed his orchestral technique"},
                {"sourceSlug": "ludwig-van-beethoven", "sourceName": "Ludwig van Beethoven", "verb": "INFLUENCES", "targetSlug": "pyotr-ilyich-tchaikovsky", "targetName": "Pyotr Ilyich Tchaikovsky", "context": "Tchaikovsky built on Beethoven's symphonic tradition while adding Russian melodic character"},
                {"sourceSlug": "pyotr-ilyich-tchaikovsky", "sourceName": "Pyotr Ilyich Tchaikovsky", "verb": "CREATES", "targetSlug": "swan-lake", "targetName": "Swan Lake", "context": "Composed 1875-1876, premiered 1877, became definitive Romantic ballet"},
                {"sourceSlug": "pyotr-ilyich-tchaikovsky", "sourceName": "Pyotr Ilyich Tchaikovsky", "verb": "OCCURS_IN", "targetSlug": "st-petersburg", "targetName": "St. Petersburg", "context": "Studied, premiered major works, and died in St. Petersburg"},
                {"sourceSlug": "pyotr-ilyich-tchaikovsky", "sourceName": "Pyotr Ilyich Tchaikovsky", "verb": "CREATES", "targetSlug": "nutcracker-ballet", "targetName": "The Nutcracker", "context": "Composed 1891-1892, premiered December 1892, became Christmas tradition"}
            ],
            "places": [{"name": "St. Petersburg, Russia", "role": "Training, premieres, and death"}, {"name": "Votkinsk, Russia", "role": "Birthplace"}, {"name": "Klin, Russia", "role": "Country home and composition retreat"}]
        }
    },
]

# ═══════════════════════════════════════════
# EXECUTION
# ═══════════════════════════════════════════

def enrich_entity(slug, data):
    """Find and enrich an existing entity file."""
    for f in glob.glob(f"{BASE}/**/*{slug}*.json", recursive=True):
        try:
            d = json.load(open(f))
            e = d["entities"][0]
            if e["slug"] != slug:
                continue
        except:
            continue

        # Special: fix wrong data for richard-wagner
        if "fix_name" in data:
            e["name"] = data["fix_name"]
            e["label"] = data["fix_label"]
            e["callNumber"] = data["fix_callNumber"]
            e["subjectHeadings"] = ["People — Musicians & Composers — Europe — Modern"]

        e["summary"] = data["summary"]

        dj = e.get("detailsJson", "")
        if isinstance(dj, str) and dj:
            try: details = json.loads(dj)
            except: details = {}
        elif isinstance(dj, dict):
            details = dj
        else:
            details = {}

        details["causes"] = data.get("causes", details.get("causes", []))
        details["effects"] = data.get("effects", details.get("effects", []))
        details["relationships"] = data.get("relationships", details.get("relationships", []))
        details["places"] = data.get("places", details.get("places", []))
        e["detailsJson"] = json.dumps(details, ensure_ascii=False)

        if "subjects" in data:
            e["subjects"] = data["subjects"]
        if "frameworks" in data:
            e["frameworks"] = data["frameworks"]

        # Handle directory move for richard-wagner
        if "fix_division" in data and data["fix_old_division"] in f:
            new_dir = os.path.join(BASE, data["fix_division"])
            os.makedirs(new_dir, exist_ok=True)
            new_path = os.path.join(new_dir, f'{data["fix_callNumber"].split(".")[0]}{slug}.json')
            with open(new_path, "w") as fh:
                json.dump(d, fh, indent=2, ensure_ascii=False)
                fh.write("\n")
            os.remove(f)
            print(f"    Moved {os.path.basename(f)} -> {os.path.basename(new_path)}")
            return True

        with open(f, "w") as fh:
            json.dump(d, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        return True
    return False


def create_new_entity(entity_data):
    """Create a new entity JSON file."""
    slug = entity_data["slug"]
    cn = entity_data["callNumber"]
    div_code = cn.split(".")[0]
    div_dir = f"{div_code}-Class-{div_code}"
    dirpath = os.path.join(BASE, div_dir)
    os.makedirs(dirpath, exist_ok=True)
    filepath = os.path.join(dirpath, f"{div_code}{slug}.json")

    # Serialize detailsJson
    dj = entity_data.get("detailsJson", {})
    if isinstance(dj, dict):
        dj = json.dumps(dj, ensure_ascii=False)

    doc = {
        "entities": [{
            "slug": slug,
            "name": entity_data["name"],
            "label": entity_data["label"],
            "callNumber": cn,
            "summary": entity_data["summary"],
            "era": entity_data.get("era", ""),
            "eraSlug": entity_data.get("eraSlug", ""),
            "eraDivision": entity_data.get("eraDivision", ""),
            "eraDivisionCode": entity_data.get("eraDivisionCode", ""),
            "region": entity_data.get("region", ""),
            "continent": entity_data.get("continent", ""),
            "status": "Published",
            "born": entity_data.get("born", ""),
            "died": entity_data.get("died", ""),
            "founded": "",
            "period": "",
            "wikidataQid": entity_data.get("wikidataQid", ""),
            "wikipediaUrl": entity_data.get("wikipediaUrl", ""),
            "imageUrl": "",
            "detailsJson": dj,
            "subjectHeadings": entity_data.get("subjectHeadings", []),
            "subjects": entity_data.get("subjects", []),
            "frameworks": entity_data.get("frameworks", []),
            "altNames": [],
            "importanceScore": entity_data.get("importanceScore", 5),
            "startDate": None,
            "endDate": None,
            "$id": slug,
        }]
    }

    with open(filepath, "w") as fh:
        json.dump(doc, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    return True


def entity_to_appwrite(e):
    dj = e.get("detailsJson", {})
    if isinstance(dj, dict):
        dj = json.dumps(dj, ensure_ascii=False)
    return {
        "slug": e["slug"],
        "name": e["name"],
        "label": e.get("label", ""),
        "callNumber": e.get("callNumber", ""),
        "era": e.get("era", ""),
        "summary": e.get("summary", ""),
        "continent": e.get("continent", ""),
        "region": e.get("region", ""),
        "subjects": e.get("subjects", []),
        "subjectHeadings": e.get("subjectHeadings", []),
        "detailsJson": dj,
    }


def upsert_to_appwrite(slug, e):
    """Create or update entity in Appwrite."""
    data = entity_to_appwrite(e)
    doc_id = slug_to_id(slug)

    existing = get_doc(doc_id) or get_doc(slug)
    if existing:
        did = doc_id if get_doc(doc_id) else slug
        return update_doc(did, data)
    else:
        return create_doc(doc_id, data)


# ═══ RUN ═══

print("=" * 60)
print("BATCH 7: 10 STUB Enrichments + 10 New Entities")
print("=" * 60)

# Part 1: Enrich stubs
print("\n--- PART 1: Enriching 10 worst STUBs ---")
enriched = 0
for slug, data in ENRICHMENTS.items():
    if enrich_entity(slug, data):
        print(f"  ENRICHED {slug}")
        enriched += 1
    else:
        print(f"  NOT FOUND {slug}")

# Part 2: Create new entities
print(f"\n--- PART 2: Creating 10 new entities ---")
created = 0
for entity_data in NEW_ENTITIES:
    slug = entity_data["slug"]
    create_new_entity(entity_data)
    print(f"  CREATED {slug}")
    created += 1

print(f"\nLocal: {enriched} enriched, {created} new entities created")

# Part 3: Sync all to Appwrite
print("\n--- PART 3: Syncing to Appwrite ---")

# Build slug→entity index for everything we touched
all_slugs = list(ENRICHMENTS.keys()) + [e["slug"] for e in NEW_ENTITIES]
slug_entities = {}
for f in glob.glob(f"{BASE}/**/*.json", recursive=True):
    try:
        d = json.load(open(f))
        e = d["entities"][0]
        if e["slug"] in all_slugs:
            slug_entities[e["slug"]] = e
    except:
        pass

sync_ok = 0
sync_fail = 0
for slug in all_slugs:
    if slug not in slug_entities:
        print(f"  SKIP {slug} (file not found)")
        continue
    e = slug_entities[slug]
    if upsert_to_appwrite(slug, e):
        sync_ok += 1
    else:
        sync_fail += 1
        print(f"  SYNC FAIL {slug}")
    time.sleep(0.15)

print(f"Appwrite: {sync_ok} synced, {sync_fail} failed")
print(f"\n{'=' * 60}")
print(f"BATCH 7 COMPLETE: {enriched} enriched + {created} created = {enriched + created} total")
print(f"{'=' * 60}")
