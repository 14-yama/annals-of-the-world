#!/usr/bin/env python3
"""
Batch 4: Enrich 25 existing stub/partial entities + create 10 new notable entities.
"""
import json, glob, os, hashlib

BASE = "data/appwrite-export/entities"

def slug_to_id(slug):
    return hashlib.sha256(slug.encode()).hexdigest()[:20]

def enrich_entity(slug, data):
    """Find entity file by slug and update it with enriched data."""
    for f in glob.glob(f"{BASE}/**/*.json", recursive=True):
        if slug.replace("-", "") not in os.path.basename(f).replace("-", ""):
            continue
        try:
            d = json.load(open(f))
            e = d["entities"][0]
            if e["slug"].replace("_", "-") == slug:
                for k, v in data.items():
                    e[k] = v
                d["entities"][0] = e
                with open(f, "w") as fh:
                    json.dump(d, fh, indent=2, ensure_ascii=False)
                print(f"  ENRICHED {slug} ({len(data.get('summary',''))}c)")
                return True
        except:
            pass
    print(f"  NOT FOUND: {slug}")
    return False

def create_entity(data):
    """Create a new entity JSON file."""
    slug = data["slug"]
    call = data["callNumber"]
    class_code = call.split(".")[0]
    div_dir = f"{BASE}/{class_code}-Class-{class_code}"
    os.makedirs(div_dir, exist_ok=True)
    filepath = f"{div_dir}/{class_code}{slug}.json"

    doc = {
        "_meta": {"classCode": class_code, "divisionCode": f"{class_code}{slug}", "count": 1},
        "entities": [data]
    }
    with open(filepath, "w") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    print(f"  CREATED {slug} ({len(data.get('summary',''))}c) → {filepath}")

# ════════════════════════════════════════════════════════════════════════
# ENRICHMENTS (25 entities)
# ════════════════════════════════════════════════════════════════════════
enrichments = [
    ("alan-turing", {
        "summary": "Alan Turing (1912–1954) was a British mathematician, logician, and cryptanalyst who is widely regarded as the father of theoretical computer science and artificial intelligence. His 1936 paper 'On Computable Numbers' introduced the concept of the Turing machine, a mathematical model that formalized the notion of algorithmic computation.\n\nDuring World War II, Turing worked at Bletchley Park where he led the effort to crack the German Enigma cipher. His work on the Bombe machine is estimated to have shortened the war by two years and saved millions of lives.\n\nIn 1950, Turing proposed the 'Turing Test' as a measure of machine intelligence, a concept that remains central to AI research. He was prosecuted in 1952 for homosexuality under British law, chemically castrated, and died of cyanide poisoning in 1954. He received a posthumous royal pardon in 2013.",
        "subjects": ["Computer Science", "Cryptography", "World War II", "Artificial Intelligence", "Mathematics", "United Kingdom", "Bletchley Park", "Enigma"],
        "subjectHeadings": ["People — Scientists — United Kingdom — Modern"],
        "detailsJson": {
            "causes": ["Cambridge mathematical tradition", "Hilbert's Entscheidungsproblem challenge", "German Enigma encryption during WWII"],
            "effects": ["Foundation of theoretical computer science", "Allied victory accelerated by Enigma decryption", "Turing Test became AI benchmark", "Posthumous pardon inspired LGBTQ+ rights discourse", "ACM Turing Award named in his honor"],
            "relationships": [
                {"sourceSlug": "alan-turing", "sourceName": "Alan Turing", "verb": "INFLUENCES", "targetSlug": "computer-science", "targetName": "Computer Science", "context": "Founded theoretical computer science with the Turing machine concept"},
                {"sourceSlug": "alan-turing", "sourceName": "Alan Turing", "verb": "OCCURS_IN", "targetSlug": "united-kingdom", "targetName": "United Kingdom", "context": "Born in London, worked at Bletchley Park and Manchester"},
                {"sourceSlug": "alan-turing", "sourceName": "Alan Turing", "verb": "INFLUENCES", "targetSlug": "world-war-ii", "targetName": "World War II", "context": "Cracked Enigma cipher, shortening the war by an estimated two years"},
                {"sourceSlug": "alan-turing", "sourceName": "Alan Turing", "verb": "INFLUENCES", "targetSlug": "artificial-intelligence", "targetName": "Artificial Intelligence", "context": "Proposed the Turing Test in 1950 as measure of machine intelligence"},
                {"sourceSlug": "alan-turing", "sourceName": "Alan Turing", "verb": "CAUSES", "targetSlug": "digital-revolution", "targetName": "Digital Revolution", "context": "His theoretical work laid groundwork for programmable computers"}
            ]
        }
    }),
    ("ada-lovelace", {
        "summary": "Ada Lovelace (1815–1852), born Augusta Ada Byron, was a British mathematician and writer recognized as the first computer programmer. The daughter of poet Lord Byron and mathematician Anne Isabella Milbanke, she combined her parents' literary imagination with mathematical rigor.\n\nIn 1843, Lovelace translated Luigi Menabrea's article on Charles Babbage's Analytical Engine, adding extensive notes that were three times longer than the original text. Her 'Note G' contained what is considered the first algorithm intended for machine processing — a method to compute Bernoulli numbers.\n\nLovelace foresaw that computers could go beyond mere calculation, envisioning machines that could compose music and manipulate symbols. The U.S. Department of Defense named the Ada programming language (1980) in her honor.",
        "subjects": ["Computer Science", "Mathematics", "Women in Science", "Victorian Era", "United Kingdom", "Analytical Engine", "Programming"],
        "subjectHeadings": ["People — Scientists — United Kingdom — Modern"],
        "detailsJson": {
            "causes": ["Mathematical education from Anne Isabella Milbanke", "Collaboration with Charles Babbage on the Analytical Engine", "Intellectual environment of Victorian scientific circles"],
            "effects": ["First published computer algorithm (Note G)", "Visionary concept of general-purpose computing", "Ada programming language named in her honor (1980)", "Inspiration for women in STEM fields"],
            "relationships": [
                {"sourceSlug": "ada-lovelace", "sourceName": "Ada Lovelace", "verb": "INFLUENCES", "targetSlug": "computer-science", "targetName": "Computer Science", "context": "Wrote the first algorithm for machine computation"},
                {"sourceSlug": "ada-lovelace", "sourceName": "Ada Lovelace", "verb": "OCCURS_IN", "targetSlug": "united-kingdom", "targetName": "United Kingdom", "context": "Lived and worked in England throughout her life"},
                {"sourceSlug": "ada-lovelace", "sourceName": "Ada Lovelace", "verb": "INFLUENCES", "targetSlug": "alan-turing", "targetName": "Alan Turing", "context": "Her vision of general-purpose computation anticipated Turing's universal machine"}
            ]
        }
    }),
    ("archimedes", {
        "summary": "Archimedes of Syracuse (c. 287–212 BCE) was a Greek mathematician, physicist, engineer, and astronomer who is considered the greatest mathematician of antiquity and one of the greatest of all time. He anticipated modern calculus by using the method of exhaustion to calculate areas under curves and volumes of solids.\n\nHis contributions include the Archimedes' principle of buoyancy (legend has him shouting 'Eureka!' in his bath), the Archimedean screw for raising water, and formulas for the areas and volumes of spheres and cylinders. He calculated pi to remarkable precision and invented war machines that held off the Roman siege of Syracuse for two years.\n\nArchimedes was killed by a Roman soldier during the fall of Syracuse in 212 BCE, reportedly while working on a mathematical diagram. His tomb bore the figure of a sphere inscribed in a cylinder, honoring his proof that their volume ratio is 2:3.",
        "subjects": ["Mathematics", "Physics", "Engineering", "Classical Greece", "Syracuse", "Sicily", "Buoyancy", "Calculus"],
        "subjectHeadings": ["People — Scientists — Greece — Classical"],
        "detailsJson": {
            "causes": ["Alexandrian mathematical tradition", "Greek scientific culture in Syracuse", "Patronage of King Hiero II of Syracuse"],
            "effects": ["Foundation of hydrostatics and statics", "Method of exhaustion anticipated integral calculus", "Archimedean screw still used worldwide", "Inspired Renaissance mathematicians like Galileo", "Pi calculation methods advanced mathematics"],
            "relationships": [
                {"sourceSlug": "archimedes", "sourceName": "Archimedes", "verb": "OCCURS_IN", "targetSlug": "syracuse", "targetName": "Syracuse", "context": "Lived and died in Syracuse, Sicily"},
                {"sourceSlug": "archimedes", "sourceName": "Archimedes", "verb": "INFLUENCES", "targetSlug": "galileo-galilei", "targetName": "Galileo Galilei", "context": "Galileo called Archimedes 'superhuman' and built on his work in mechanics"},
                {"sourceSlug": "archimedes", "sourceName": "Archimedes", "verb": "INFLUENCES", "targetSlug": "isaac-newton", "targetName": "Isaac Newton", "context": "Newton's calculus formalized methods Archimedes pioneered"},
                {"sourceSlug": "archimedes", "sourceName": "Archimedes", "verb": "INFLUENCES", "targetSlug": "euclid", "targetName": "Euclid", "context": "Built upon Euclidean geometry in his mathematical proofs"}
            ]
        }
    }),
    ("marie-curie", {
        "summary": "Marie Curie (1867–1934), born Maria Skłodowska in Warsaw, was a Polish-French physicist and chemist who conducted pioneering research on radioactivity. She was the first woman to win a Nobel Prize, the first person to win Nobel Prizes in two different sciences (Physics 1903, Chemistry 1911), and the first woman professor at the University of Paris.\n\nWith her husband Pierre Curie, she discovered two elements — polonium (named for her native Poland) and radium — by processing tons of pitchblende ore by hand. After Pierre's death in 1906, she continued their work alone, developing mobile X-ray units ('petites Curies') that saved countless lives during World War I.\n\nCurie died of aplastic anemia caused by prolonged radiation exposure. Her notebooks remain so radioactive they must be stored in lead-lined boxes. She shattered gender barriers in science and remains the most iconic female scientist in history.",
        "subjects": ["Physics", "Chemistry", "Radioactivity", "Nobel Prize", "Women in Science", "Poland", "France", "Radium"],
        "subjectHeadings": ["People — Scientists — France — Modern"],
        "detailsJson": {
            "causes": ["Polish intellectual tradition despite Russian partition", "Paris scientific community at the Sorbonne", "Discovery of X-rays by Röntgen inspired radiation research"],
            "effects": ["Discovery of radioactivity transformed physics and chemistry", "Polonium and radium added to periodic table", "Mobile X-ray units saved lives in World War I", "Opened doors for women in science globally", "Radiation research led to cancer treatment methods"],
            "relationships": [
                {"sourceSlug": "marie-curie", "sourceName": "Marie Curie", "verb": "OCCURS_IN", "targetSlug": "france", "targetName": "France", "context": "Conducted her groundbreaking research at the University of Paris"},
                {"sourceSlug": "marie-curie", "sourceName": "Marie Curie", "verb": "INFLUENCES", "targetSlug": "nuclear-physics", "targetName": "Nuclear Physics", "context": "Her radioactivity research opened the field of nuclear physics"},
                {"sourceSlug": "marie-curie", "sourceName": "Marie Curie", "verb": "OCCURS_IN", "targetSlug": "poland", "targetName": "Poland", "context": "Born Maria Skłodowska in Warsaw, named polonium for her homeland"},
                {"sourceSlug": "marie-curie", "sourceName": "Marie Curie", "verb": "INFLUENCES", "targetSlug": "world-war-i", "targetName": "World War I", "context": "Developed mobile X-ray units that served on the Western Front"}
            ]
        }
    }),
    ("otto-von-bismarck", {
        "summary": "Otto von Bismarck (1815–1898) was a Prussian-German statesman who unified the German states into the German Empire in 1871 and served as its first Chancellor until 1890. Known as the 'Iron Chancellor,' he masterminded three wars — against Denmark (1864), Austria (1866), and France (1870–71) — to forge a unified Germany under Prussian leadership.\n\nBismarck pioneered Realpolitik — pragmatic diplomacy driven by power rather than ideology. He engineered the complex alliance system that maintained European peace for two decades, pioneered the world's first welfare state with health insurance (1883), accident insurance (1884), and old-age pensions (1889).\n\nDismissed by Kaiser Wilhelm II in 1890, Bismarck warned that his carefully balanced alliance system would collapse without skilled management. His prediction proved tragically accurate: 24 years later, Europe plunged into World War I.",
        "subjects": ["Germany", "Prussian History", "Unification", "Realpolitik", "Diplomacy", "Welfare State", "Franco-Prussian War", "Modern Europe"],
        "subjectHeadings": ["People — Political Leaders — Germany — Modern"],
        "detailsJson": {
            "causes": ["Prussian militarism and Junker class tradition", "Failure of 1848 liberal revolutions", "Growing German nationalism after Napoleonic Wars"],
            "effects": ["Unified German Empire created in 1871", "Alliance system maintained European peace 1871–1890", "First modern welfare state inspired social policy globally", "Power vacuum after dismissal contributed to WWI", "Realpolitik doctrine influenced 20th-century diplomacy"],
            "relationships": [
                {"sourceSlug": "otto-von-bismarck", "sourceName": "Otto von Bismarck", "verb": "CAUSES", "targetSlug": "german-unification", "targetName": "German Unification", "context": "Engineered unification through three wars culminating in 1871 proclamation at Versailles"},
                {"sourceSlug": "otto-von-bismarck", "sourceName": "Otto von Bismarck", "verb": "OCCURS_IN", "targetSlug": "germany", "targetName": "Germany", "context": "First Chancellor of the unified German Empire 1871–1890"},
                {"sourceSlug": "otto-von-bismarck", "sourceName": "Otto von Bismarck", "verb": "INFLUENCES", "targetSlug": "world-war-i", "targetName": "World War I", "context": "His alliance system collapsed after his dismissal, leading to war"},
                {"sourceSlug": "otto-von-bismarck", "sourceName": "Otto von Bismarck", "verb": "INFLUENCES", "targetSlug": "napoleon-italy", "targetName": "Napoleon III", "context": "Provoked France into the Franco-Prussian War through Ems Dispatch"}
            ]
        }
    }),
    ("vladimir-lenin", {
        "summary": "Vladimir Ilyich Lenin (1870–1924) was a Russian revolutionary, politician, and political theorist who served as the first head of Soviet Russia (1917–1924). Born Vladimir Ulyanov, he was radicalized after his brother's execution for plotting to assassinate the Tsar, and became the leader of the Bolshevik faction of the Russian Social Democratic Labour Party.\n\nLenin led the October Revolution of 1917, overthrowing the Provisional Government and establishing the world's first socialist state. He implemented war communism during the Russian Civil War (1918–1921), then pivoted to the New Economic Policy (NEP) in 1921 to prevent economic collapse.\n\nHis theoretical contributions — the vanguard party, democratic centralism, imperialism as capitalism's highest stage — shaped communist movements worldwide for decades. After a series of strokes, he died in 1924; his embalmed body remains displayed in Moscow's Red Square.",
        "subjects": ["Russia", "Communism", "Russian Revolution", "Soviet Union", "Marxism", "Bolsheviks", "Political Theory", "Cold War Origins"],
        "subjectHeadings": ["People — Political Leaders — Russia — Modern"],
        "detailsJson": {
            "causes": ["Execution of brother Alexander Ulyanov radicalized him", "Marxist theory adapted to Russian conditions", "Tsarist autocracy and World War I exhaustion created revolutionary conditions"],
            "effects": ["October Revolution established first socialist state", "Soviet model inspired communist revolutions worldwide", "Cold War bipolar world order", "Vanguard party theory adopted by revolutionary movements globally", "Russian Civil War and war communism killed millions"],
            "relationships": [
                {"sourceSlug": "vladimir-lenin", "sourceName": "Vladimir Lenin", "verb": "CAUSES", "targetSlug": "russian-revolution", "targetName": "Russian Revolution", "context": "Led the October Revolution overthrowing the Provisional Government"},
                {"sourceSlug": "vladimir-lenin", "sourceName": "Vladimir Lenin", "verb": "OCCURS_IN", "targetSlug": "russia", "targetName": "Russia", "context": "Founded the Soviet state and governed from Moscow 1917–1924"},
                {"sourceSlug": "vladimir-lenin", "sourceName": "Vladimir Lenin", "verb": "INFLUENCES", "targetSlug": "joseph-stalin", "targetName": "Joseph Stalin", "context": "Stalin succeeded Lenin but betrayed his final testament warning"},
                {"sourceSlug": "vladimir-lenin", "sourceName": "Vladimir Lenin", "verb": "INFLUENCES", "targetSlug": "mao-zedong", "targetName": "Mao Zedong", "context": "Leninist party model adopted by Chinese Communist Party"},
                {"sourceSlug": "vladimir-lenin", "sourceName": "Vladimir Lenin", "verb": "INFLUENCES", "targetSlug": "karl-marx", "targetName": "Karl Marx", "context": "Adapted Marxist theory to Russian conditions with Leninism"}
            ]
        }
    }),
    ("neil-armstrong", {
        "summary": "Neil Alden Armstrong (1930–2012) was an American astronaut and aeronautical engineer who became the first human to walk on the Moon on July 20, 1969. As commander of Apollo 11, he spoke the immortal words: 'That's one small step for [a] man, one giant leap for mankind.'\n\nBefore NASA, Armstrong was a naval aviator who flew 78 combat missions in the Korean War, then became a test pilot at Edwards Air Force Base, flying the X-15 rocket plane to the edge of space. He narrowly survived the Gemini 8 mission (1966) when a thruster malfunction sent his capsule into a dangerous spin.\n\nAfter Apollo 11, Armstrong largely withdrew from public life, teaching aerospace engineering at the University of Cincinnati. He remained a deeply private figure who saw himself as an engineer rather than a celebrity, famously declining most autograph requests to prevent forgery.",
        "subjects": ["Space Exploration", "Apollo Program", "Moon Landing", "NASA", "United States", "Cold War", "Aviation", "Korean War"],
        "subjectHeadings": ["People — Explorers — United States — Contemporary"],
        "detailsJson": {
            "causes": ["Space Race between USA and Soviet Union", "Kennedy's 1961 Moon commitment", "Armstrong's exceptional piloting skills from Korean War and X-15 program"],
            "effects": ["First human Moon landing inspired global wonder", "Proved human space exploration was possible", "Apollo program advanced computing and materials science", "Cultural symbol of American achievement", "Space exploration became permanent human endeavor"],
            "relationships": [
                {"sourceSlug": "neil-armstrong", "sourceName": "Neil Armstrong", "verb": "OCCURS_IN", "targetSlug": "united-states", "targetName": "United States", "context": "American astronaut born in Wapakoneta, Ohio"},
                {"sourceSlug": "neil-armstrong", "sourceName": "Neil Armstrong", "verb": "INFLUENCES", "targetSlug": "space-exploration", "targetName": "Space Exploration", "context": "First moonwalk proved human interplanetary travel was achievable"},
                {"sourceSlug": "neil-armstrong", "sourceName": "Neil Armstrong", "verb": "OCCURS_IN", "targetSlug": "cold-war", "targetName": "Cold War", "context": "Moon landing was decisive American victory in the Space Race"}
            ]
        }
    }),
    ("rembrandt", {
        "summary": "Rembrandt Harmenszoon van Rijn (1606–1669) was a Dutch painter and printmaker who is generally regarded as the greatest artist of the Dutch Golden Age and one of the most important painters in European history. He produced approximately 300 paintings, 300 etchings, and 2,000 drawings during his prolific career.\n\nRembrandt mastered the use of light and shadow (chiaroscuro) to create profound psychological depth. His masterpieces include 'The Night Watch' (1642), 'The Anatomy Lesson of Dr. Nicolaes Tulp' (1632), and over 80 self-portraits that form a uniquely intimate autobiography spanning four decades.\n\nDespite immense fame, Rembrandt's lavish spending and art collecting led to bankruptcy in 1656. He continued painting masterpieces in poverty until his death in 1669. His influence on Western art — from portraiture to etching technique — remains incalculable.",
        "subjects": ["Dutch Golden Age", "Painting", "Art History", "Netherlands", "Chiaroscuro", "Baroque", "Portraiture", "Printmaking"],
        "subjectHeadings": ["People — Artists — Netherlands — Early Modern"],
        "detailsJson": {
            "causes": ["Dutch Golden Age prosperity created art market", "Leiden artistic tradition and Pieter Lastman's mentorship", "Protestant culture favored portraiture over religious commissions"],
            "effects": ["Defined Dutch Golden Age painting style", "Revolutionized etching as an art form", "Self-portrait tradition influenced all subsequent Western art", "Chiaroscuro technique influenced Romantic and later painters"],
            "relationships": [
                {"sourceSlug": "rembrandt", "sourceName": "Rembrandt", "verb": "OCCURS_IN", "targetSlug": "netherlands", "targetName": "Netherlands", "context": "Worked primarily in Leiden and Amsterdam during the Dutch Golden Age"},
                {"sourceSlug": "rembrandt", "sourceName": "Rembrandt", "verb": "INFLUENCES", "targetSlug": "vincent-van-gogh", "targetName": "Vincent van Gogh", "context": "Van Gogh deeply admired Rembrandt's self-portraits and emotional depth"},
                {"sourceSlug": "rembrandt", "sourceName": "Rembrandt", "verb": "INFLUENCES", "targetSlug": "caravaggio", "targetName": "Caravaggio", "context": "Both masters of chiaroscuro, Rembrandt refined Caravaggio's dramatic lighting"}
            ]
        }
    }),
    ("thomas-hobbes", {
        "summary": "Thomas Hobbes (1588–1679) was an English philosopher best known for his 1651 masterwork 'Leviathan,' which laid the foundation for modern political philosophy. He argued that in the 'state of nature,' human life would be 'solitary, poor, nasty, brutish, and short,' and that people must surrender freedoms to a sovereign authority through a social contract to avoid perpetual war.\n\nHobbes witnessed the English Civil War firsthand — an experience that profoundly shaped his conviction that strong central authority was essential to prevent societal collapse. He spent years in exile in Paris, where he tutored the future Charles II.\n\nHis materialist philosophy — holding that everything, including thought and consciousness, is matter in motion — was revolutionary and controversial. Hobbes influenced Locke, Rousseau, and the entire social contract tradition that underpins modern democratic theory.",
        "subjects": ["Political Philosophy", "Social Contract", "English Civil War", "Leviathan", "Materialism", "England", "Enlightenment", "Sovereignty"],
        "subjectHeadings": ["People — Philosophers — England — Early Modern"],
        "detailsJson": {
            "causes": ["English Civil War demonstrated dangers of political chaos", "Renaissance humanism and classical education", "Galileo's mechanistic worldview inspired materialist philosophy"],
            "effects": ["Social contract theory became foundation of modern political philosophy", "Influenced Locke and Rousseau's competing social contract theories", "Materialist philosophy pioneered secular approach to politics", "Sovereignty theory shaped absolutist and later democratic thought"],
            "relationships": [
                {"sourceSlug": "thomas-hobbes", "sourceName": "Thomas Hobbes", "verb": "INFLUENCES", "targetSlug": "john-locke", "targetName": "John Locke", "context": "Locke's social contract theory directly responded to Hobbes"},
                {"sourceSlug": "thomas-hobbes", "sourceName": "Thomas Hobbes", "verb": "INFLUENCES", "targetSlug": "jean-jacques-rousseau", "targetName": "Jean-Jacques Rousseau", "context": "Rousseau's social contract challenged Hobbes' pessimistic view of human nature"},
                {"sourceSlug": "thomas-hobbes", "sourceName": "Thomas Hobbes", "verb": "OCCURS_IN", "targetSlug": "united-kingdom", "targetName": "United Kingdom", "context": "English philosopher who lived through the Civil War"}
            ]
        }
    }),
    ("jean-jacques-rousseau", {
        "summary": "Jean-Jacques Rousseau (1712–1778) was a Genevan philosopher, writer, and composer whose ideas profoundly influenced the Enlightenment, the French Revolution, and modern political and educational theory. His opening line in 'The Social Contract' (1762) — 'Man is born free, and everywhere he is in chains' — became a battle cry for revolutionaries.\n\nRousseau argued that civilization corrupts humanity's natural goodness, a radical departure from Hobbes. His 'Discourse on Inequality' (1755) traced how private property created social hierarchy and oppression. In 'Emile' (1762), he pioneered child-centered education, arguing children should learn through experience rather than rote memorization.\n\nParadoxically, Rousseau abandoned his own five children to foundling homes. His Confessions (published posthumously) created the modern autobiographical genre. His concept of the 'general will' became both the intellectual engine of democratic movements and, critics argue, a justification for totalitarianism.",
        "subjects": ["Philosophy", "French Revolution", "Social Contract", "Education", "Enlightenment", "Geneva", "France", "Romanticism"],
        "subjectHeadings": ["People — Philosophers — France — Early Modern"],
        "detailsJson": {
            "causes": ["Genevan republican tradition", "Enlightenment intellectual ferment in Paris", "Personal experience of social inequality as a wandering youth"],
            "effects": ["Inspired French Revolution's ideological foundations", "Child-centered education theory transformed pedagogy globally", "Romantic movement drew on his celebration of nature and emotion", "'General will' concept shaped democratic theory", "Autobiography as literary genre"],
            "relationships": [
                {"sourceSlug": "jean-jacques-rousseau", "sourceName": "Jean-Jacques Rousseau", "verb": "INFLUENCES", "targetSlug": "french-revolution", "targetName": "French Revolution", "context": "His social contract theory directly inspired revolutionary ideals"},
                {"sourceSlug": "jean-jacques-rousseau", "sourceName": "Jean-Jacques Rousseau", "verb": "OCCURS_IN", "targetSlug": "france", "targetName": "France", "context": "Lived and wrote primarily in Paris and rural France"},
                {"sourceSlug": "jean-jacques-rousseau", "sourceName": "Jean-Jacques Rousseau", "verb": "INFLUENCES", "targetSlug": "immanuel-kant", "targetName": "Immanuel Kant", "context": "Kant said Rousseau taught him to respect the common man"},
                {"sourceSlug": "jean-jacques-rousseau", "sourceName": "Jean-Jacques Rousseau", "verb": "INFLUENCES", "targetSlug": "karl-marx", "targetName": "Karl Marx", "context": "Marx built on Rousseau's critique of private property and inequality"}
            ]
        }
    }),
    ("michelangelo", {
        "summary": "Michelangelo di Lodovico Buonarroti Simoni (1475–1564) was an Italian sculptor, painter, architect, and poet of the High Renaissance, considered one of the greatest artists of all time. His works — the Pietà (1499), David (1504), and the Sistine Chapel ceiling (1508–1512) — represent the pinnacle of Renaissance art.\n\nMichelangelo spent four years painting the Sistine Chapel ceiling alone, creating over 300 figures depicting scenes from Genesis. He later painted 'The Last Judgment' (1536–1541) on the altar wall. As architect of St. Peter's Basilica from 1546, he designed the iconic dome that dominates Rome's skyline to this day.\n\nA perfectionist who destroyed works he deemed unworthy, Michelangelo believed sculpture was the art of 'liberating the figure imprisoned in the marble.' He lived to 88 — extraordinary for his era — working until days before his death, with his last known sculpture left deliberately unfinished.",
        "subjects": ["Renaissance Art", "Sculpture", "Painting", "Architecture", "Italy", "Sistine Chapel", "Florence", "Rome"],
        "subjectHeadings": ["People — Artists — Italy — Early Modern"],
        "detailsJson": {
            "causes": ["Medici patronage in Florence", "Italian Renaissance cultural flowering", "Classical Greek and Roman artistic models"],
            "effects": ["Sistine Chapel ceiling became most famous painting in the world", "David sculpture became symbol of Florence and Renaissance humanism", "St. Peter's dome defined Roman architecture", "Mannerist and Baroque art directly descended from his style", "Established sculptor-artist as cultural hero"],
            "relationships": [
                {"sourceSlug": "michelangelo", "sourceName": "Michelangelo", "verb": "OCCURS_IN", "targetSlug": "italy", "targetName": "Italy", "context": "Worked in Florence and Rome throughout his career"},
                {"sourceSlug": "michelangelo", "sourceName": "Michelangelo", "verb": "INFLUENCES", "targetSlug": "caravaggio", "targetName": "Caravaggio", "context": "Caravaggio's dramatic figural style was influenced by Michelangelo's muscular forms"},
                {"sourceSlug": "michelangelo", "sourceName": "Michelangelo", "verb": "INFLUENCES", "targetSlug": "leonardo-da-vinci", "targetName": "Leonardo da Vinci", "context": "Rivals who pushed each other to greater heights in Renaissance Florence"},
                {"sourceSlug": "michelangelo", "sourceName": "Michelangelo", "verb": "INFLUENCES", "targetSlug": "pablo-picasso", "targetName": "Pablo Picasso", "context": "Picasso studied Michelangelo's figural distortions as precedent"}
            ]
        }
    }),
    ("leo-tolstoy", {
        "summary": "Count Lev Nikolayevich Tolstoy (1828–1910) was a Russian writer widely regarded as one of the greatest novelists of all time. His epic masterworks 'War and Peace' (1869) and 'Anna Karenina' (1877) are considered pinnacles of world literature, combining sweeping historical narrative with profound psychological insight.\n\n'War and Peace' follows five aristocratic families through Napoleon's invasion of Russia with over 500 characters, while 'Anna Karenina' explores love, hypocrisy, and moral redemption in Russian society. Tolstoy drew from his own military experience in the Crimean War for his vivid battle descriptions.\n\nIn later life, Tolstoy underwent a spiritual crisis that led him to reject organized religion, aristocratic privilege, and private property. His philosophy of nonviolent resistance directly influenced Mahatma Gandhi and Martin Luther King Jr. He died at a remote railway station in 1910, fleeing his estate in a final act of renunciation.",
        "subjects": ["Russian Literature", "Novel", "Philosophy", "Nonviolence", "Russia", "War and Peace", "Christianity", "Social Reform"],
        "subjectHeadings": ["People — Artists — Russia — Modern"],
        "detailsJson": {
            "causes": ["Russian aristocratic education and Crimean War experience", "Russian literary tradition of Pushkin and Gogol", "Spiritual crisis in 1870s led to moral philosophy"],
            "effects": ["War and Peace redefined the novel form", "Tolstoyan nonviolence influenced Gandhi and MLK", "Anna Karenina set standard for psychological realism", "Inspired numerous literary movements worldwide"],
            "relationships": [
                {"sourceSlug": "leo-tolstoy", "sourceName": "Leo Tolstoy", "verb": "OCCURS_IN", "targetSlug": "russia", "targetName": "Russia", "context": "Lived at Yasnaya Polyana estate and wrote about Russian society"},
                {"sourceSlug": "leo-tolstoy", "sourceName": "Leo Tolstoy", "verb": "INFLUENCES", "targetSlug": "mahatma-gandhi", "targetName": "Mahatma Gandhi", "context": "Gandhi corresponded with Tolstoy and adopted his nonviolent philosophy"},
                {"sourceSlug": "leo-tolstoy", "sourceName": "Leo Tolstoy", "verb": "INFLUENCES", "targetSlug": "fyodor-dostoevsky", "targetName": "Fyodor Dostoevsky", "context": "Two giants of Russian literature who admired each other's work"},
                {"sourceSlug": "leo-tolstoy", "sourceName": "Leo Tolstoy", "verb": "INFLUENCES", "targetSlug": "martin-luther-king-jr", "targetName": "Martin Luther King Jr.", "context": "King cited Tolstoy's nonviolent philosophy as inspiration"}
            ]
        }
    }),
    ("deng-xiaoping", {
        "summary": "Deng Xiaoping (1904–1997) was a Chinese revolutionary and statesman who served as the paramount leader of China from 1978 to 1989. Though he never held the title of head of state, Deng was the architect of China's economic reforms that transformed a impoverished agrarian nation into the world's second-largest economy.\n\nDeng introduced the 'Reform and Opening Up' policy (1978), establishing Special Economic Zones, allowing private enterprise, and welcoming foreign investment — all while maintaining the Chinese Communist Party's political monopoly. His pragmatic philosophy was captured in his famous phrase: 'It doesn't matter whether a cat is black or white, as long as it catches mice.'\n\nThe contradictions of Deng's legacy are stark: he lifted hundreds of millions out of poverty while ordering the Tiananmen Square crackdown (June 4, 1989) that killed hundreds to thousands of pro-democracy protesters. He remains China's most consequential leader after Mao.",
        "subjects": ["China", "Economic Reform", "Communism", "Tiananmen Square", "Cold War", "Special Economic Zones", "Modernization", "Asia"],
        "subjectHeadings": ["People — Political Leaders — China — Contemporary"],
        "detailsJson": {
            "causes": ["Cultural Revolution devastation discredited Maoist economics", "Deng's three political purges gave him pragmatic resilience", "East Asian tiger economies demonstrated market success"],
            "effects": ["China's GDP grew from $150B to $1.2T under his reforms", "Hundreds of millions lifted out of poverty", "Special Economic Zones model copied worldwide", "Tiananmen crackdown set precedent for authoritarian modernization", "China's rise as global superpower"],
            "relationships": [
                {"sourceSlug": "deng-xiaoping", "sourceName": "Deng Xiaoping", "verb": "OCCURS_IN", "targetSlug": "china", "targetName": "China", "context": "Paramount leader who transformed China's economy 1978–1989"},
                {"sourceSlug": "deng-xiaoping", "sourceName": "Deng Xiaoping", "verb": "INFLUENCES", "targetSlug": "mao-zedong", "targetName": "Mao Zedong", "context": "Reversed Mao's economic policies while maintaining party control"},
                {"sourceSlug": "deng-xiaoping", "sourceName": "Deng Xiaoping", "verb": "CAUSES", "targetSlug": "tiananmen-square", "targetName": "Tiananmen Square", "context": "Ordered military crackdown on pro-democracy protesters June 1989"}
            ]
        }
    }),
    ("vasco-da-gama", {
        "summary": "Vasco da Gama (c. 1460–1524) was a Portuguese explorer who became the first European to reach India by sea, rounding the Cape of Good Hope in 1497–1498. His discovery of the sea route to Asia opened direct maritime trade between Europe and the lucrative spice markets of the East, fundamentally altering global commerce.\n\nDa Gama's first voyage (1497–1499) with four ships and 170 men was one of the most ambitious in exploration history. After rounding Africa, he reached Calicut (modern Kozhikode) on India's Malabar Coast in May 1498. The voyage lost two ships and over half its crew, but the spices brought back covered the expedition's cost sixty times over.\n\nHe made three voyages to India and was appointed Viceroy of Portuguese India in 1524, dying of malaria in Cochin shortly after arrival. His route shattered Venice's Mediterranean spice monopoly and launched the Portuguese Empire.",
        "subjects": ["Exploration", "Portugal", "India", "Spice Trade", "Age of Discovery", "Maritime History", "Cape of Good Hope", "Colonialism"],
        "subjectHeadings": ["People — Explorers — Portugal — Early Modern"],
        "detailsJson": {
            "causes": ["Portuguese maritime tradition under Prince Henry the Navigator", "Ottoman control of overland spice routes created incentive", "Bartolomeu Dias' rounding of Cape of Good Hope (1488) proved route feasible"],
            "effects": ["Direct Europe-India sea trade bypassed Ottoman middlemen", "Portuguese Empire became first global maritime empire", "Venice's spice monopoly broken", "European colonization of Asia began", "Global trade networks permanently reconfigured"],
            "relationships": [
                {"sourceSlug": "vasco-da-gama", "sourceName": "Vasco da Gama", "verb": "OCCURS_IN", "targetSlug": "portugal", "targetName": "Portugal", "context": "Portuguese explorer who sailed for the Crown"},
                {"sourceSlug": "vasco-da-gama", "sourceName": "Vasco da Gama", "verb": "OCCURS_IN", "targetSlug": "india", "targetName": "India", "context": "Reached Calicut on India's Malabar Coast in 1498"},
                {"sourceSlug": "vasco-da-gama", "sourceName": "Vasco da Gama", "verb": "INFLUENCES", "targetSlug": "christopher-columbus", "targetName": "Christopher Columbus", "context": "Both opened new maritime routes that reshaped global trade"},
                {"sourceSlug": "vasco-da-gama", "sourceName": "Vasco da Gama", "verb": "INFLUENCES", "targetSlug": "ferdinand-magellan", "targetName": "Ferdinand Magellan", "context": "Da Gama's success inspired Magellan's circumnavigation attempt"}
            ]
        }
    }),
    ("james-cook", {
        "summary": "Captain James Cook (1728–1779) was a British explorer, navigator, and cartographer who made three voyages to the Pacific Ocean, mapping vast stretches of previously uncharted territory. He was the first European to make contact with the eastern coastline of Australia (1770) and the Hawaiian Islands (1778), and performed the first circumnavigation of New Zealand.\n\nCook's scientific approach to exploration was revolutionary. He virtually eliminated scurvy on long voyages through dietary measures, charted coastlines with unprecedented accuracy, and carried naturalists and astronomers who made groundbreaking discoveries. His 1769 observation of the Transit of Venus from Tahiti advanced astronomical understanding of the solar system.\n\nCook was killed by Hawaiian islanders at Kealakekua Bay in February 1779 during his third voyage. His charts were so accurate they remained in use into the 20th century, and his voyages opened the Pacific to European colonization for better and worse.",
        "subjects": ["Exploration", "Pacific Ocean", "Australia", "New Zealand", "Navigation", "British Empire", "Cartography", "Hawaii"],
        "subjectHeadings": ["People — Explorers — United Kingdom — Early Modern"],
        "detailsJson": {
            "causes": ["British Admiralty's need for Pacific charts", "Royal Society's quest for Transit of Venus observation", "Cook's exceptional navigational skills from North Sea merchant fleet"],
            "effects": ["European mapping of Pacific and Australian coastlines", "British colonization of Australia and New Zealand", "Scientific expedition model adopted by future explorers", "Hawaiian and Pacific island cultures permanently altered", "Scurvy prevention advanced naval medicine"],
            "relationships": [
                {"sourceSlug": "james-cook", "sourceName": "James Cook", "verb": "OCCURS_IN", "targetSlug": "united-kingdom", "targetName": "United Kingdom", "context": "British naval captain who sailed for the Royal Navy"},
                {"sourceSlug": "james-cook", "sourceName": "James Cook", "verb": "OCCURS_IN", "targetSlug": "australia", "targetName": "Australia", "context": "First European to chart Australia's east coast in 1770"},
                {"sourceSlug": "james-cook", "sourceName": "James Cook", "verb": "INFLUENCES", "targetSlug": "roald-amundsen", "targetName": "Roald Amundsen", "context": "Cook's polar explorations inspired later Antarctic expeditions"}
            ]
        }
    }),
    ("roald-amundsen", {
        "summary": "Roald Engelbregt Gravning Amundsen (1872–1928) was a Norwegian explorer who led the first expedition to reach the South Pole on December 14, 1911, beating Robert Falcon Scott's British team by 34 days. He was also the first to traverse the Northwest Passage by ship (1903–1906) and is generally considered the most successful polar explorer in history.\n\nAmundsen's South Pole success rested on meticulous preparation, Inuit survival techniques (dog sleds, fur clothing), and a relentless focus on efficiency. While Scott's team perished on their return journey, all five members of Amundsen's party returned safely.\n\nIn 1926, Amundsen led the first verified expedition over the North Pole by airship (the Norge), making him the first person to reach both poles. He disappeared in 1928 while flying a rescue mission for the airship Italia in the Arctic, his body never recovered.",
        "subjects": ["Polar Exploration", "South Pole", "Norway", "Northwest Passage", "Arctic", "Antarctic", "Navigation", "Adventure"],
        "subjectHeadings": ["People — Explorers — Norway — Modern"],
        "detailsJson": {
            "causes": ["Norwegian polar tradition of Fridtjof Nansen", "Adoption of Inuit survival techniques", "Rivalry with Robert Falcon Scott"],
            "effects": ["First confirmed South Pole expedition", "First Northwest Passage transit", "Demonstrated value of indigenous knowledge in exploration", "Polar exploration became symbol of national prestige"],
            "relationships": [
                {"sourceSlug": "roald-amundsen", "sourceName": "Roald Amundsen", "verb": "OCCURS_IN", "targetSlug": "norway", "targetName": "Norway", "context": "Norwegian explorer who became national hero"},
                {"sourceSlug": "roald-amundsen", "sourceName": "Roald Amundsen", "verb": "INFLUENCES", "targetSlug": "neil-armstrong", "targetName": "Neil Armstrong", "context": "Amundsen's polar achievements inspired later exploration milestones"}
            ]
        }
    }),
    ("zheng-he", {
        "summary": "Zheng He (1371–1433) was a Chinese mariner, explorer, and diplomat who commanded seven epic voyages (1405–1433) across the Indian Ocean with fleets of up to 300 ships and 28,000 men — the largest naval expeditions in history before World War I. His treasure ships measured up to 120 meters long, dwarfing anything in contemporary European navies.\n\nBorn Ma He into a Muslim Hui family in Yunnan, he was captured as a boy during the Ming conquest, castrated, and placed in the service of Prince Zhu Di, who became the Yongle Emperor. Zheng He's voyages reached Southeast Asia, India, the Persian Gulf, and the East African coast, establishing Chinese diplomatic and trade networks across 30 nations.\n\nAfter the Yongle Emperor's death, the Confucian bureaucracy halted the voyages and destroyed most records. China turned inward just decades before European exploration began, one of history's great 'what-ifs' — had the voyages continued, China might have colonized the world.",
        "subjects": ["China", "Maritime Exploration", "Indian Ocean", "Ming Dynasty", "Naval History", "Diplomacy", "Africa", "Southeast Asia"],
        "subjectHeadings": ["People — Explorers — China — Medieval"],
        "detailsJson": {
            "causes": ["Yongle Emperor's desire to project Ming power abroad", "Zheng He's personal loyalty from years of service", "Muslim heritage facilitated diplomacy in Islamic ports"],
            "effects": ["Chinese diplomatic networks across 30+ nations", "Largest pre-modern naval expeditions in history", "China's maritime retreat after 1433 changed global history", "Southeast Asian Chinese diaspora communities established"],
            "relationships": [
                {"sourceSlug": "zheng-he", "sourceName": "Zheng He", "verb": "OCCURS_IN", "targetSlug": "china", "targetName": "China", "context": "Ming Dynasty admiral who sailed from Nanjing"},
                {"sourceSlug": "zheng-he", "sourceName": "Zheng He", "verb": "INFLUENCES", "targetSlug": "vasco-da-gama", "targetName": "Vasco da Gama", "context": "Zheng He's Indian Ocean routes predated da Gama's by nearly a century"},
                {"sourceSlug": "zheng-he", "sourceName": "Zheng He", "verb": "INFLUENCES", "targetSlug": "christopher-columbus", "targetName": "Christopher Columbus", "context": "China's maritime retreat left the Indian Ocean open for European exploration"}
            ]
        }
    }),
    ("francis-bacon", {
        "summary": "Francis Bacon (1561–1626) was an English philosopher, statesman, and essayist who is widely regarded as the father of the scientific method. His 'Novum Organum' (1620) proposed systematic empirical investigation based on inductive reasoning, replacing the Aristotelian deductive approach that had dominated European thought for nearly two millennia.\n\nBacon served as Attorney General and Lord Chancellor of England under James I, but was convicted of bribery in 1621 and banned from public office. He devoted his remaining years to philosophy and science, producing works that laid the intellectual foundation for the Scientific Revolution.\n\nHis classification of knowledge influenced the Encyclopédie of Diderot and d'Alembert, and his vision of science as a collaborative, institutional enterprise anticipated modern research universities. Bacon died of pneumonia in 1626, reportedly caught while stuffing a chicken with snow to test the preservative effects of cold.",
        "subjects": ["Scientific Method", "Philosophy", "Empiricism", "England", "Enlightenment", "Renaissance", "Inductive Reasoning", "Novum Organum"],
        "subjectHeadings": ["People — Philosophers — England — Early Modern"],
        "detailsJson": {
            "causes": ["Renaissance recovery of classical texts", "Criticism of Aristotelian scholasticism", "English intellectual ferment under Elizabeth I and James I"],
            "effects": ["Scientific method based on empirical observation and induction", "Foundation for the Royal Society and institutional science", "Influenced Encyclopédie's knowledge classification", "Shaped Enlightenment emphasis on evidence-based reasoning"],
            "relationships": [
                {"sourceSlug": "francis-bacon", "sourceName": "Francis Bacon", "verb": "INFLUENCES", "targetSlug": "isaac-newton", "targetName": "Isaac Newton", "context": "Newton's experimental method embodied Bacon's empirical vision"},
                {"sourceSlug": "francis-bacon", "sourceName": "Francis Bacon", "verb": "OCCURS_IN", "targetSlug": "united-kingdom", "targetName": "United Kingdom", "context": "English Lord Chancellor and philosopher"},
                {"sourceSlug": "francis-bacon", "sourceName": "Francis Bacon", "verb": "INFLUENCES", "targetSlug": "voltaire", "targetName": "Voltaire", "context": "Voltaire championed Bacon's empiricism to French audiences in Letters on England"}
            ]
        }
    }),
    ("erasmus", {
        "summary": "Desiderius Erasmus of Rotterdam (1466–1536) was a Dutch Renaissance humanist, Catholic priest, and theologian who was the most influential scholar of the Northern Renaissance. His satirical masterpiece 'In Praise of Folly' (1509) mocked the corruption of the Catholic Church, and his Greek New Testament (1516) provided the textual basis for Protestant Bible translations.\n\nErasmus corresponded with virtually every major intellectual in Europe — his network of over 3,000 surviving letters constitutes the first pan-European 'Republic of Letters.' He advocated reform within the Catholic Church through education and moral persuasion rather than schism, earning him criticism from both Catholics and Protestants.\n\nWhen Martin Luther's Reformation erupted in 1517, Erasmus initially sympathized but ultimately refused to join, famously declaring: 'I laid a hen's egg; Luther hatched a bird of quite a different kind.' His commitment to moderation in an age of extremism made him both admired and distrusted by all sides.",
        "subjects": ["Renaissance Humanism", "Reformation", "Netherlands", "Catholic Church", "Biblical Scholarship", "Satire", "Education", "Latin Literature"],
        "subjectHeadings": ["People — Philosophers — Netherlands — Early Modern"],
        "detailsJson": {
            "causes": ["Northern Renaissance humanism and classical learning revival", "Printing press enabled wide distribution of his works", "Catholic Church corruption created demand for reform voices"],
            "effects": ["Greek New Testament enabled Protestant Bible translations", "In Praise of Folly undermined Church authority through satire", "Republic of Letters established model for scholarly networks", "Educational reforms influenced European universities for centuries"],
            "relationships": [
                {"sourceSlug": "erasmus", "sourceName": "Erasmus", "verb": "INFLUENCES", "targetSlug": "martin-luther", "targetName": "Martin Luther", "context": "Erasmus's biblical scholarship and Church criticism paved way for Reformation"},
                {"sourceSlug": "erasmus", "sourceName": "Erasmus", "verb": "OCCURS_IN", "targetSlug": "netherlands", "targetName": "Netherlands", "context": "Born in Rotterdam, known as Erasmus of Rotterdam"},
                {"sourceSlug": "erasmus", "sourceName": "Erasmus", "verb": "INFLUENCES", "targetSlug": "thomas-more", "targetName": "Thomas More", "context": "Close friend; wrote In Praise of Folly while staying at More's house"}
            ]
        }
    }),
    ("john-calvin", {
        "summary": "John Calvin (1509–1564) was a French theologian, pastor, and reformer who became the most important figure in the second generation of the Protestant Reformation. His magnum opus, 'Institutes of the Christian Religion' (1536, expanded to 1559), provided Protestantism with its most comprehensive and systematic theology.\n\nFrom 1541 until his death, Calvin effectively governed Geneva as a theocratic republic, transforming the city into what John Knox called 'the most perfect school of Christ since the apostles.' He established the Geneva Academy (1559), which trained Protestant ministers who spread Reformed theology across Europe.\n\nCalvinism's doctrines — predestination, the sovereignty of God, and the 'Protestant work ethic' — profoundly shaped Western culture. Max Weber argued that Calvinist theology drove the development of capitalism. Calvin's influence extends to the Puritans, the Dutch Reformed Church, Scottish Presbyterianism, and the founding ethos of America.",
        "subjects": ["Reformation", "Theology", "Geneva", "Predestination", "Protestantism", "France", "Switzerland", "Calvinism"],
        "subjectHeadings": ["People — Religious Figures — Switzerland — Early Modern"],
        "detailsJson": {
            "causes": ["Martin Luther's Reformation created Protestant theological space", "French humanist education at University of Paris", "Persecution of French Protestants drove Calvin to Geneva"],
            "effects": ["Reformed tradition became second major branch of Protestantism", "Geneva model of church governance widely adopted", "Protestant work ethic thesis linked Calvinism to capitalism", "Puritan movements shaped England and colonial America", "Predestination doctrine sparked centuries of theological debate"],
            "relationships": [
                {"sourceSlug": "john-calvin", "sourceName": "John Calvin", "verb": "OCCURS_IN", "targetSlug": "switzerland", "targetName": "Switzerland", "context": "Governed Geneva as a theocratic republic 1541–1564"},
                {"sourceSlug": "john-calvin", "sourceName": "John Calvin", "verb": "INFLUENCES", "targetSlug": "martin-luther", "targetName": "Martin Luther", "context": "Calvin systematized Reformed theology building on Luther's break with Rome"},
                {"sourceSlug": "john-calvin", "sourceName": "John Calvin", "verb": "INFLUENCES", "targetSlug": "american-revolution", "targetName": "American Revolution", "context": "Calvinist principles of resistance to tyranny influenced American founding"}
            ]
        }
    }),
    ("florence-nightingale", {
        "summary": "Florence Nightingale (1820–1910) was a British social reformer, statistician, and the founder of modern nursing. During the Crimean War (1854–1856), she organized care for wounded soldiers at Scutari, reducing the death rate from 42% to 2% through sanitation reforms — earning her the name 'The Lady with the Lamp.'\n\nNightingale was a pioneering statistician who invented the polar area diagram (a form of pie chart) to demonstrate that most British soldiers were dying from preventable diseases rather than combat wounds. Her 1859 book 'Notes on Nursing' established nursing as a respectable profession for women.\n\nShe spent 50 years as an invalid after the Crimean War but continued to influence public health policy from her bed, reforming military hospitals, Indian sanitation, and workhouse care. In 1907 she became the first woman to receive the Order of Merit. The WHO designated May 12 (her birthday) as International Nurses Day.",
        "subjects": ["Nursing", "Public Health", "Crimean War", "Statistics", "Women's History", "United Kingdom", "Sanitation", "Medicine"],
        "subjectHeadings": ["People — Scientists — United Kingdom — Modern"],
        "detailsJson": {
            "causes": ["Privileged education unusual for women of her era", "Crimean War exposed catastrophic military hospital conditions", "Personal calling to nursing despite family opposition"],
            "effects": ["Modern nursing profession established", "Hospital sanitation reforms saved millions of lives", "Pioneered use of statistics in public health", "Military medical care permanently reformed", "International Nurses Day celebrates her legacy"],
            "relationships": [
                {"sourceSlug": "florence-nightingale", "sourceName": "Florence Nightingale", "verb": "OCCURS_IN", "targetSlug": "united-kingdom", "targetName": "United Kingdom", "context": "British reformer who transformed nursing and public health"},
                {"sourceSlug": "florence-nightingale", "sourceName": "Florence Nightingale", "verb": "INFLUENCES", "targetSlug": "red-cross", "targetName": "Red Cross", "context": "Her Crimean War work inspired international humanitarian medical organizations"},
                {"sourceSlug": "florence-nightingale", "sourceName": "Florence Nightingale", "verb": "INFLUENCES", "targetSlug": "marie-curie", "targetName": "Marie Curie", "context": "Both pioneered contributions to medicine during wartime as women"}
            ]
        }
    }),
    ("thomas-edison", {
        "summary": "Thomas Alva Edison (1847–1931) was an American inventor and businessman who developed many devices that greatly influenced life around the world, holding 1,093 US patents — more than any individual in American history. His most famous inventions include the practical incandescent light bulb (1879), the phonograph (1877), and the motion picture camera (1891).\n\nEdison established the first industrial research laboratory at Menlo Park, New Jersey (1876), creating the model for modern R&D labs. His 'invention factory' systematized the process of innovation, employing dozens of researchers to develop inventions on an industrial scale. He famously said: 'Genius is one percent inspiration and ninety-nine percent perspiration.'\n\nBeyond individual inventions, Edison built the first commercial electrical power distribution system (Pearl Street Station, 1882), launching the electrical age. His bitter rivalry with Nikola Tesla in the 'War of Currents' (AC vs DC) shaped the modern power grid, though Tesla's alternating current ultimately prevailed.",
        "subjects": ["Invention", "Electricity", "United States", "Light Bulb", "Phonograph", "Industrial Revolution", "Research Laboratory", "Technology"],
        "subjectHeadings": ["People — Scientists — United States — Modern"],
        "detailsJson": {
            "causes": ["Self-education and voracious reading", "Telegraphy experience provided electrical knowledge", "American entrepreneurial culture after Civil War"],
            "effects": ["Practical electric lighting transformed daily life worldwide", "Industrial research laboratory model adopted globally", "Phonograph launched the recorded music industry", "Motion picture camera created cinema", "Pearl Street Station launched commercial electricity"],
            "relationships": [
                {"sourceSlug": "thomas-edison", "sourceName": "Thomas Edison", "verb": "OCCURS_IN", "targetSlug": "united-states", "targetName": "United States", "context": "American inventor who worked in Menlo Park and West Orange, New Jersey"},
                {"sourceSlug": "thomas-edison", "sourceName": "Thomas Edison", "verb": "INFLUENCES", "targetSlug": "nikola-tesla", "targetName": "Nikola Tesla", "context": "Edison and Tesla's War of Currents shaped the modern electrical grid"},
                {"sourceSlug": "thomas-edison", "sourceName": "Thomas Edison", "verb": "CAUSES", "targetSlug": "industrial-revolution", "targetName": "Industrial Revolution", "context": "Electrical lighting and power extended industrial productivity beyond daylight"}
            ]
        }
    }),
    ("wright-brothers", {
        "summary": "Wilbur Wright (1867–1912) and Orville Wright (1871–1948) were American aviation pioneers who achieved the first sustained, controlled, powered heavier-than-air flight on December 17, 1903, at Kitty Hawk, North Carolina. Their first flight lasted 12 seconds and covered 120 feet; by the fourth flight that day, Wilbur flew 852 feet in 59 seconds.\n\nThe brothers' success rested on systematic engineering rather than reckless daring. They built a wind tunnel to test over 200 wing shapes, invented three-axis control (pitch, roll, yaw) that remains the basis of all fixed-wing aircraft, and designed their own lightweight engine when none available met their specifications.\n\nWithin a decade of Kitty Hawk, aircraft were being used in World War I. Within a lifetime, they enabled globalization, mass tourism, and intercontinental warfare. Orville lived to see Chuck Yeager break the sound barrier in 1947 — just 44 years after that first 12-second flight.",
        "subjects": ["Aviation", "United States", "Engineering", "Kitty Hawk", "Flight", "Industrial Revolution", "Transportation", "Technology"],
        "subjectHeadings": ["People — Scientists — United States — Modern"],
        "detailsJson": {
            "causes": ["Bicycle mechanics provided engineering and manufacturing skills", "Otto Lilienthal's glider experiments inspired them", "Systematic wind tunnel testing gave scientific foundation"],
            "effects": ["Powered flight launched the aviation age", "Three-axis control became standard for all aircraft", "Enabled aerial warfare in World War I within a decade", "Foundation for airline industry and global connectivity", "Space exploration ultimately descended from their achievement"],
            "relationships": [
                {"sourceSlug": "wright-brothers", "sourceName": "Wright Brothers", "verb": "OCCURS_IN", "targetSlug": "united-states", "targetName": "United States", "context": "American brothers from Dayton, Ohio who flew at Kitty Hawk, North Carolina"},
                {"sourceSlug": "wright-brothers", "sourceName": "Wright Brothers", "verb": "INFLUENCES", "targetSlug": "world-war-i", "targetName": "World War I", "context": "Aircraft became weapons within a decade of first flight"},
                {"sourceSlug": "wright-brothers", "sourceName": "Wright Brothers", "verb": "INFLUENCES", "targetSlug": "neil-armstrong", "targetName": "Neil Armstrong", "context": "Armstrong carried a piece of the Wright Flyer to the Moon in 1969"}
            ]
        }
    }),
    ("frederick-douglass", {
        "summary": "Frederick Douglass (1818–1895), born Frederick Augustus Washington Bailey, was an American social reformer, abolitionist, orator, writer, and statesman who escaped from slavery to become the most prominent African American voice of the 19th century. His autobiography 'Narrative of the Life of Frederick Douglass' (1845) became a bestseller that galvanized the abolitionist movement.\n\nDouglass taught himself to read as a child slave in Maryland, escaped to the North in 1838, and became a powerful orator for the Massachusetts Anti-Slavery Society. His 1852 speech 'What to the Slave Is the Fourth of July?' remains one of the greatest orations in American history.\n\nDuring the Civil War, Douglass recruited African American soldiers for the Union Army and advised President Lincoln. He later served as U.S. Marshal for the District of Columbia and Minister to Haiti — the highest government positions held by an African American in the 19th century.",
        "subjects": ["Abolitionism", "Slavery", "United States", "Civil War", "African American History", "Oratory", "Civil Rights", "Autobiography"],
        "subjectHeadings": ["People — Activists — United States — Modern"],
        "detailsJson": {
            "causes": ["Personal experience of slavery in Maryland", "Self-education through secretly learning to read", "Abolitionist networks in the North after his escape"],
            "effects": ["Narrative of Frederick Douglass galvanized abolitionist movement", "Recruited African American soldiers for Union Army", "Highest-ranking Black government official of 19th century", "Inspired civil rights movement of 20th century"],
            "relationships": [
                {"sourceSlug": "frederick-douglass", "sourceName": "Frederick Douglass", "verb": "OCCURS_IN", "targetSlug": "united-states", "targetName": "United States", "context": "Escaped slavery to become America's leading abolitionist voice"},
                {"sourceSlug": "frederick-douglass", "sourceName": "Frederick Douglass", "verb": "INFLUENCES", "targetSlug": "abraham-lincoln", "targetName": "Abraham Lincoln", "context": "Advised Lincoln on emancipation and Black military service"},
                {"sourceSlug": "frederick-douglass", "sourceName": "Frederick Douglass", "verb": "INFLUENCES", "targetSlug": "martin-luther-king-jr", "targetName": "Martin Luther King Jr.", "context": "Douglass's oratory and activism paved the way for 20th century civil rights"},
                {"sourceSlug": "frederick-douglass", "sourceName": "Frederick Douglass", "verb": "INFLUENCES", "targetSlug": "harriet-tubman", "targetName": "Harriet Tubman", "context": "Both were escaped slaves who became prominent abolitionists"}
            ]
        }
    }),
    ("ibn-battuta", {
        "summary": "Abu Abdullah Muhammad Ibn Battuta (1304–1368/1369) was a Moroccan scholar and explorer who undertook the most extensive pre-modern journey ever recorded, traveling approximately 120,000 kilometers over 29 years — three times the distance covered by Marco Polo. His 'Rihla' (Journey) provides an unparalleled firsthand account of the 14th-century Islamic world.\n\nIbn Battuta departed Tangier in 1325 at age 21, ostensibly for the Hajj to Mecca, but didn't return for nearly three decades. He visited every Muslim country of his time, plus Constantinople, Sri Lanka, the Maldives, Sumatra, and China, serving variously as a judge, ambassador, and merchant along the way.\n\nHis account describes the Black Death in Syria, the court of the Delhi Sultanate, the gold of Mali's Mansa Musa, and the vast Mongol steppe. Dictated to Ibn Juzayy upon his return to Fez, the Rihla provides irreplaceable documentation of medieval Islamic civilization at its height.",
        "subjects": ["Exploration", "Morocco", "Islamic World", "Medieval Travel", "Rihla", "Mecca", "Mali", "India"],
        "subjectHeadings": ["People — Explorers — Morocco — Medieval"],
        "detailsJson": {
            "causes": ["Islamic tradition of travel for learning (rihla)", "Vast dar al-Islam network of hospitality for scholars", "Personal ambition and curiosity from Tangier's cosmopolitan culture"],
            "effects": ["Most extensive pre-modern travelogue ever recorded", "Irreplaceable documentation of 14th-century Islamic world", "Descriptions of Mali, India, and China enrich historical knowledge", "Inspired later European Age of Exploration"],
            "relationships": [
                {"sourceSlug": "ibn-battuta", "sourceName": "Ibn Battuta", "verb": "OCCURS_IN", "targetSlug": "morocco", "targetName": "Morocco", "context": "Born in Tangier, departed and returned to Morocco"},
                {"sourceSlug": "ibn-battuta", "sourceName": "Ibn Battuta", "verb": "INFLUENCES", "targetSlug": "marco-polo", "targetName": "Marco Polo", "context": "Two greatest medieval travelers — Ibn Battuta covered three times Marco Polo's distance"},
                {"sourceSlug": "ibn-battuta", "sourceName": "Ibn Battuta", "verb": "OCCURS_IN", "targetSlug": "india", "targetName": "India", "context": "Served as judge in the Delhi Sultanate for eight years"}
            ]
        }
    }),
    ("tim-berners-lee", {
        "summary": "Sir Timothy John Berners-Lee (born 1955) is a British computer scientist who invented the World Wide Web in 1989, arguably the most transformative technological innovation since the printing press. Working at CERN in Geneva, he wrote the first web browser, web server, and the foundational protocols (HTTP, HTML, URLs) that make the web possible.\n\nBerners-Lee's genius lay not just in technical invention but in his decision to make the web free and open. He convinced CERN to release the technology royalty-free in 1993, ensuring universal access. Had he patented his invention, he could have become the wealthiest person in history; instead, he prioritized universal access to information.\n\nHe founded the World Wide Web Consortium (W3C) in 1994 to maintain open web standards and was appointed to the Order of Merit by Queen Elizabeth II in 2007. He continues to advocate for net neutrality and against the centralization of web power by tech giants through his Web Foundation.",
        "subjects": ["World Wide Web", "Computer Science", "Internet", "CERN", "United Kingdom", "Open Source", "Technology", "Information Age"],
        "subjectHeadings": ["People — Scientists — United Kingdom — Contemporary"],
        "detailsJson": {
            "causes": ["CERN's need for document sharing between physicists", "Hypertext concept pioneered by Ted Nelson and Douglas Engelbart", "Internet infrastructure (TCP/IP) already existed as foundation"],
            "effects": ["World Wide Web transformed global communication", "E-commerce revolution created trillion-dollar economy", "Social media reshaped politics and culture", "Open web standards prevented proprietary control", "Digital divide became new form of inequality"],
            "relationships": [
                {"sourceSlug": "tim-berners-lee", "sourceName": "Tim Berners-Lee", "verb": "CAUSES", "targetSlug": "digital-revolution", "targetName": "Digital Revolution", "context": "The World Wide Web is the primary interface of the digital revolution"},
                {"sourceSlug": "tim-berners-lee", "sourceName": "Tim Berners-Lee", "verb": "OCCURS_IN", "targetSlug": "united-kingdom", "targetName": "United Kingdom", "context": "British scientist, born in London"},
                {"sourceSlug": "tim-berners-lee", "sourceName": "Tim Berners-Lee", "verb": "INFLUENCES", "targetSlug": "alan-turing", "targetName": "Alan Turing", "context": "Built on Turing's theoretical foundations of computation"}
            ]
        }
    }),
]

# ════════════════════════════════════════════════════════════════════════
# NEW ENTITIES (10 notable figures MISSING from dataset)
# ════════════════════════════════════════════════════════════════════════
new_entities = [
    {
        "slug": "ludwig-van-beethoven",
        "name": "Ludwig van Beethoven",
        "label": "Person",
        "callNumber": "263.ludwig-van-beethoven",
        "era": "Early Modern",
        "summary": "Ludwig van Beethoven (1770–1827) was a German composer and pianist who bridged the Classical and Romantic periods of Western music. Born in Bonn and settling in Vienna, he produced nine symphonies, five piano concertos, 32 piano sonatas, and one opera that redefined musical expression and form.\n\nBeethoven began losing his hearing around age 28, yet composed his greatest works — including the Ninth Symphony with its revolutionary choral finale 'Ode to Joy' — while profoundly deaf. His 1802 'Heiligenstadt Testament' reveals his despair at encroaching deafness and his resolve to continue creating.\n\nHis music elevated the composer from court servant to autonomous artist. The Third Symphony ('Eroica,' 1804), originally dedicated to Napoleon, marked the birth of Romantic music. His influence pervades every subsequent classical composer, and 'Ode to Joy' was adopted as the anthem of the European Union.",
        "continent": "Europe", "region": "Western Europe",
        "subjects": ["Classical Music", "Romanticism", "Germany", "Vienna", "Symphony", "Deafness", "Piano", "European Culture"],
        "subjectHeadings": ["People — Artists — Germany — Early Modern"],
        "detailsJson": {
            "causes": ["Mozart and Haydn's Viennese Classical tradition", "French Revolution's ideals of liberty and heroism", "Personal struggle with deafness drove emotional depth"],
            "effects": ["Bridged Classical and Romantic musical eras", "Established composer as autonomous creative genius", "Ninth Symphony's Ode to Joy became EU anthem", "Expanded symphonic form and emotional range permanently", "Piano sonatas remain cornerstone of keyboard repertoire"],
            "relationships": [
                {"sourceSlug": "ludwig-van-beethoven", "sourceName": "Ludwig van Beethoven", "verb": "OCCURS_IN", "targetSlug": "germany", "targetName": "Germany", "context": "Born in Bonn, composed primarily in Vienna"},
                {"sourceSlug": "ludwig-van-beethoven", "sourceName": "Ludwig van Beethoven", "verb": "INFLUENCES", "targetSlug": "johann-sebastian-bach", "targetName": "Johann Sebastian Bach", "context": "Bach's counterpoint was foundational to Beethoven's compositional technique"},
                {"sourceSlug": "ludwig-van-beethoven", "sourceName": "Ludwig van Beethoven", "verb": "INFLUENCES", "targetSlug": "french-revolution", "targetName": "French Revolution", "context": "Eroica Symphony originally dedicated to Napoleon embodied revolutionary ideals"}
            ]
        }
    },
    {
        "slug": "wolfgang-amadeus-mozart",
        "name": "Wolfgang Amadeus Mozart",
        "label": "Person",
        "callNumber": "263.wolfgang-amadeus-mozart",
        "era": "Early Modern",
        "summary": "Wolfgang Amadeus Mozart (1756–1791) was an Austrian composer who produced over 600 works in virtually every genre of his era, achieving a perfection of form and expression that remains unsurpassed. A child prodigy who performed before European royalty at age six, he composed his first symphony at eight and his first opera at twelve.\n\nMozart's output includes 41 symphonies, 27 piano concertos, and operas that revolutionized the art form — 'The Marriage of Figaro' (1786), 'Don Giovanni' (1787), and 'The Magic Flute' (1791) remain among the most performed operas in the world. His Requiem in D Minor, left unfinished at his death, is shrouded in mystery.\n\nDespite his genius, Mozart died at 35 in Vienna, impoverished and buried in an unmarked communal grave. His music combines technical brilliance with profound emotional depth — Tchaikovsky called it 'the musical Christ.' He composed more masterpieces in his short life than most artists could in several lifetimes.",
        "continent": "Europe", "region": "Central Europe",
        "subjects": ["Classical Music", "Opera", "Austria", "Vienna", "Child Prodigy", "Symphony", "Piano", "Requiem"],
        "subjectHeadings": ["People — Artists — Austria — Early Modern"],
        "detailsJson": {
            "causes": ["Father Leopold Mozart's rigorous musical training", "Salzburg and Vienna's rich musical culture", "Patronage system of European courts"],
            "effects": ["Perfected Classical musical forms", "Revolutionized opera with complex characters and ensembles", "Piano concerto genre reached its apex", "Influenced every subsequent classical composer", "Requiem became most famous unfinished work in music"],
            "relationships": [
                {"sourceSlug": "wolfgang-amadeus-mozart", "sourceName": "Wolfgang Amadeus Mozart", "verb": "OCCURS_IN", "targetSlug": "austria", "targetName": "Austria", "context": "Born in Salzburg, lived and died in Vienna"},
                {"sourceSlug": "wolfgang-amadeus-mozart", "sourceName": "Wolfgang Amadeus Mozart", "verb": "INFLUENCES", "targetSlug": "ludwig-van-beethoven", "targetName": "Ludwig van Beethoven", "context": "Beethoven studied with Haydn and idolized Mozart's piano concertos"},
                {"sourceSlug": "wolfgang-amadeus-mozart", "sourceName": "Wolfgang Amadeus Mozart", "verb": "INFLUENCES", "targetSlug": "johann-sebastian-bach", "targetName": "Johann Sebastian Bach", "context": "Mozart's discovery of Bach's fugues profoundly influenced his late style"}
            ]
        }
    },
    {
        "slug": "dante-alighieri",
        "name": "Dante Alighieri",
        "label": "Person",
        "callNumber": "260.dante-alighieri",
        "era": "Medieval",
        "summary": "Dante Alighieri (c. 1265–1321) was an Italian poet, writer, and philosopher whose 'Divine Comedy' is considered the greatest literary work composed in the Italian language and one of the greatest poems ever written. The three-part epic — Inferno, Purgatorio, and Paradiso — journeys through the afterlife with Virgil and Beatrice as guides.\n\nDante's revolutionary decision to write in Tuscan vernacular rather than Latin democratized literature and effectively created the modern Italian language. His political involvement in Florence's Guelph-Ghibelline conflict led to his exile in 1302, and he never returned to his beloved city, dying in Ravenna.\n\nThe Divine Comedy synthesized classical mythology, Christian theology, and contemporary politics into a unified vision of cosmic justice. T.S. Eliot called Dante and Shakespeare 'the two greatest poets in the Western world.' Florence still petitions Ravenna for his bones — 700 years after his exile.",
        "continent": "Europe", "region": "Southern Europe",
        "subjects": ["Italian Literature", "Poetry", "Divine Comedy", "Florence", "Medieval Theology", "Italian Language", "Exile", "Christianity"],
        "subjectHeadings": ["People — Artists — Italy — Medieval"],
        "detailsJson": {
            "causes": ["Florentine political factionalism and exile", "Love for Beatrice Portinari inspired poetic vision", "Classical education in Virgil and Aristotle"],
            "effects": ["Divine Comedy created modern Italian language from Tuscan dialect", "Most influential poem in Western literature", "Shaped European conceptions of afterlife for centuries", "Model for encyclopedic literary works", "Florence's cultural identity permanently defined"],
            "relationships": [
                {"sourceSlug": "dante-alighieri", "sourceName": "Dante Alighieri", "verb": "OCCURS_IN", "targetSlug": "italy", "targetName": "Italy", "context": "Florentine poet exiled to Ravenna where he completed the Divine Comedy"},
                {"sourceSlug": "dante-alighieri", "sourceName": "Dante Alighieri", "verb": "INFLUENCES", "targetSlug": "william-shakespeare", "targetName": "William Shakespeare", "context": "Two pillars of Western literature who shaped their national languages"},
                {"sourceSlug": "dante-alighieri", "sourceName": "Dante Alighieri", "verb": "INFLUENCES", "targetSlug": "michelangelo", "targetName": "Michelangelo", "context": "Michelangelo's Last Judgment was deeply influenced by Dante's Inferno"}
            ]
        }
    },
    {
        "slug": "fyodor-dostoevsky",
        "name": "Fyodor Dostoevsky",
        "label": "Person",
        "callNumber": "260.fyodor-dostoevsky",
        "era": "Modern",
        "summary": "Fyodor Mikhailovich Dostoevsky (1821–1881) was a Russian novelist, journalist, and philosopher whose psychological novels — 'Crime and Punishment' (1866), 'The Idiot' (1869), 'Demons' (1872), and 'The Brothers Karamazov' (1880) — explored the depths of the human psyche with unprecedented intensity.\n\nDostoevsky was sentenced to death in 1849 for involvement with a socialist circle, experiencing a mock execution before his sentence was commuted to four years of hard labor in Siberia. This trauma, combined with his epilepsy and gambling addiction, infused his fiction with visceral psychological authenticity.\n\nHis exploration of free will, guilt, suffering, and the existence of God anticipated existentialism, psychoanalysis, and modernist literature. Nietzsche called him 'the only psychologist from whom I have anything to learn.' Einstein declared 'The Brothers Karamazov' the most significant literary work he had ever encountered.",
        "continent": "Europe", "region": "Eastern Europe",
        "subjects": ["Russian Literature", "Novel", "Psychology", "Russia", "Existentialism", "Christianity", "Philosophy", "Crime and Punishment"],
        "subjectHeadings": ["People — Artists — Russia — Modern"],
        "detailsJson": {
            "causes": ["Mock execution and Siberian exile shaped worldview", "Russian literary tradition of Pushkin and Gogol", "Epilepsy and gambling addiction provided psychological insight"],
            "effects": ["Anticipated Freudian psychoanalysis in literature", "Influenced existentialist philosophy of Sartre and Camus", "Crime and Punishment created the psychological thriller genre", "Brothers Karamazov set standard for philosophical fiction"],
            "relationships": [
                {"sourceSlug": "fyodor-dostoevsky", "sourceName": "Fyodor Dostoevsky", "verb": "OCCURS_IN", "targetSlug": "russia", "targetName": "Russia", "context": "Russian novelist who lived in St. Petersburg and experienced Siberian exile"},
                {"sourceSlug": "fyodor-dostoevsky", "sourceName": "Fyodor Dostoevsky", "verb": "INFLUENCES", "targetSlug": "sigmund-freud", "targetName": "Sigmund Freud", "context": "Freud acknowledged Dostoevsky's unprecedented psychological insights"},
                {"sourceSlug": "fyodor-dostoevsky", "sourceName": "Fyodor Dostoevsky", "verb": "INFLUENCES", "targetSlug": "leo-tolstoy", "targetName": "Leo Tolstoy", "context": "Two giants of Russian literature exploring morality from opposite perspectives"}
            ]
        }
    },
    {
        "slug": "rosa-parks",
        "name": "Rosa Parks",
        "label": "Person",
        "callNumber": "270.rosa-parks",
        "era": "Contemporary",
        "summary": "Rosa Louise McCauley Parks (1913–2005) was an American civil rights activist known as 'the mother of the civil rights movement.' On December 1, 1955, in Montgomery, Alabama, she refused to surrender her bus seat to a white passenger, sparking the Montgomery Bus Boycott — a 381-day protest that became a pivotal moment in the American civil rights movement.\n\nParks was not merely a tired seamstress who spontaneously refused to move — she was a trained NAACP activist, secretary of the Montgomery chapter since 1943. She had attended the Highlander Folk School, which trained civil rights organizers. Her arrest was a strategic act of resistance within a planned movement.\n\nThe boycott propelled the 26-year-old Martin Luther King Jr. to national prominence and resulted in a Supreme Court ruling that bus segregation was unconstitutional (Browder v. Gayle, 1956). Parks received the Presidential Medal of Freedom (1996) and the Congressional Gold Medal (1999). Upon her death in 2005, she became the first woman to lie in honor in the U.S. Capitol.",
        "continent": "North America", "region": "North America",
        "subjects": ["Civil Rights", "United States", "Segregation", "Montgomery Bus Boycott", "African American History", "Activism", "NAACP", "Alabama"],
        "subjectHeadings": ["People — Activists — United States — Contemporary"],
        "detailsJson": {
            "causes": ["Jim Crow segregation in the American South", "NAACP training and organizing experience", "Highlander Folk School civil rights education"],
            "effects": ["Montgomery Bus Boycott lasted 381 days", "Supreme Court ruled bus segregation unconstitutional", "Propelled Martin Luther King Jr. to national leadership", "Became icon of civil rights movement", "First woman to lie in honor at U.S. Capitol"],
            "relationships": [
                {"sourceSlug": "rosa-parks", "sourceName": "Rosa Parks", "verb": "CAUSES", "targetSlug": "civil-rights-movement", "targetName": "Civil Rights Movement", "context": "Her refusal sparked the Montgomery Bus Boycott, a pivotal civil rights event"},
                {"sourceSlug": "rosa-parks", "sourceName": "Rosa Parks", "verb": "OCCURS_IN", "targetSlug": "united-states", "targetName": "United States", "context": "American civil rights activist in Montgomery, Alabama"},
                {"sourceSlug": "rosa-parks", "sourceName": "Rosa Parks", "verb": "INFLUENCES", "targetSlug": "martin-luther-king-jr", "targetName": "Martin Luther King Jr.", "context": "The boycott her arrest triggered launched King's leadership career"}
            ]
        }
    },
    {
        "slug": "queen-elizabeth-ii",
        "name": "Queen Elizabeth II",
        "label": "Person",
        "callNumber": "221.queen-elizabeth-ii",
        "era": "Contemporary",
        "summary": "Queen Elizabeth II (1926–2022) was Queen of the United Kingdom and other Commonwealth realms from 1952 until her death in 2022, making her the longest-reigning British monarch (70 years) and the second-longest-reigning sovereign in world history. She ascended the throne at 25 upon the death of her father, King George VI.\n\nElizabeth presided over the transformation of the British Empire into the Commonwealth of Nations, navigating decolonization, the Cold War, the Troubles in Northern Ireland, and the digital revolution. She maintained political neutrality through 15 Prime Ministers from Winston Churchill to Liz Truss.\n\nHer personal discipline and sense of duty made her a symbol of stability in turbulent times. During COVID-19/lockdowns, her 'We will meet again' address drew 24 million viewers. At her funeral on September 19, 2022, an estimated 4 billion people watched worldwide — the most-viewed broadcast in history.",
        "continent": "Europe", "region": "Northern Europe",
        "subjects": ["British Monarchy", "United Kingdom", "Commonwealth", "Decolonization", "Cold War", "Longest-Reigning Monarch", "Windsor Dynasty", "Modern History"],
        "subjectHeadings": ["People — Monarchs — United Kingdom — Contemporary"],
        "detailsJson": {
            "causes": ["Abdication of Edward VIII brought her father to throne", "Death of George VI in 1952 at her age 25", "British constitutional monarchy tradition"],
            "effects": ["Longest-reigning British monarch at 70 years", "Guided transition from Empire to Commonwealth", "Became symbol of stability across seven decades", "Funeral was most-watched broadcast in history", "Modernized monarchy for the media age"],
            "relationships": [
                {"sourceSlug": "queen-elizabeth-ii", "sourceName": "Queen Elizabeth II", "verb": "OCCURS_IN", "targetSlug": "united-kingdom", "targetName": "United Kingdom", "context": "Queen of the United Kingdom 1952–2022"},
                {"sourceSlug": "queen-elizabeth-ii", "sourceName": "Queen Elizabeth II", "verb": "INFLUENCES", "targetSlug": "winston-churchill", "targetName": "Winston Churchill", "context": "Churchill was her first Prime Minister, mentoring the young queen"},
                {"sourceSlug": "queen-elizabeth-ii", "sourceName": "Queen Elizabeth II", "verb": "INFLUENCES", "targetSlug": "nelson-mandela", "targetName": "Nelson Mandela", "context": "Welcomed South Africa back to the Commonwealth after apartheid ended"}
            ]
        }
    },
    {
        "slug": "pope-john-paul-ii",
        "name": "Pope John Paul II",
        "label": "Person",
        "callNumber": "250.pope-john-paul-ii",
        "era": "Contemporary",
        "summary": "Pope John Paul II (1920–2005), born Karol Józef Wojtyła in Wadowice, Poland, was head of the Catholic Church from 1978 to 2005 — the second-longest pontificate in modern history. He was the first non-Italian pope in 455 years and played a pivotal role in ending communism in Eastern Europe.\n\nAs a young man in Nazi-occupied Poland, Wojtyła studied in an underground seminary and worked in a quarry. His election as pope in 1978 galvanized the Polish Solidarity movement. His 1979 visit to Poland drew millions and is credited with sparking the chain of events that led to the fall of the Berlin Wall in 1989.\n\nJohn Paul II survived an assassination attempt in 1981, visited 129 countries (more than all previous popes combined), and made unprecedented outreach to Judaism, Islam, and other faiths. He was canonized as Saint John Paul II in 2014, just nine years after his death — one of the fastest canonizations in modern Catholic history.",
        "continent": "Europe", "region": "Southern Europe",
        "subjects": ["Catholic Church", "Poland", "Cold War", "Solidarity", "Vatican", "Communism", "Interfaith Dialogue", "Papacy"],
        "subjectHeadings": ["People — Religious Figures — Vatican — Contemporary"],
        "detailsJson": {
            "causes": ["Experience under Nazi and Soviet oppression shaped worldview", "Polish Catholic identity as resistance to communism", "Second Vatican Council's modernizing spirit"],
            "effects": ["Galvanized Solidarity movement in Poland", "Contributed to fall of communism in Eastern Europe", "Unprecedented interfaith dialogue with Judaism and Islam", "Visited 129 countries, most-traveled pope in history", "Canonized in 2014 as Catholic saint"],
            "relationships": [
                {"sourceSlug": "pope-john-paul-ii", "sourceName": "Pope John Paul II", "verb": "INFLUENCES", "targetSlug": "solidarity-movement", "targetName": "Solidarity Movement", "context": "His 1979 Poland visit galvanized the Solidarity trade union"},
                {"sourceSlug": "pope-john-paul-ii", "sourceName": "Pope John Paul II", "verb": "OCCURS_IN", "targetSlug": "vatican-city", "targetName": "Vatican City", "context": "Led the Catholic Church from Vatican City 1978–2005"},
                {"sourceSlug": "pope-john-paul-ii", "sourceName": "Pope John Paul II", "verb": "CAUSES", "targetSlug": "fall-of-communism", "targetName": "Fall of Communism", "context": "His support for Polish resistance helped trigger the collapse of Soviet bloc"}
            ]
        }
    },
    {
        "slug": "mother-teresa",
        "name": "Mother Teresa",
        "label": "Person",
        "callNumber": "253.mother-teresa",
        "era": "Contemporary",
        "summary": "Mother Teresa (1910–1997), born Anjezë Gonxhe Bojaxhiu in Skopje (then Ottoman Empire, now North Macedonia), was an Albanian-Indian Catholic nun and missionary who founded the Missionaries of Charity in Kolkata (Calcutta), India, in 1950. The order grew to over 4,500 nuns operating 610 missions in 123 countries.\n\nMother Teresa dedicated her life to serving 'the poorest of the poor,' establishing hospices, orphanages, and clinics for those with leprosy, HIV/AIDS, and tuberculosis. She received the Nobel Peace Prize in 1979, using the ceremony to advocate against abortion rather than deliver a conventional acceptance speech.\n\nHer legacy is paradoxical: revered as a living saint by millions, she was criticized by Christopher Hitchens and others for prioritizing suffering over medical treatment and for accepting donations from corrupt regimes. After her death, published letters revealed decades of spiritual doubt — 'Where is my faith? Even deep down... there is nothing but emptiness and darkness.' She was canonized as Saint Teresa of Calcutta in 2016.",
        "continent": "Asia", "region": "South Asia",
        "subjects": ["Charity", "Catholic Church", "India", "Nobel Peace Prize", "Kolkata", "Missionaries of Charity", "Poverty", "Humanitarianism"],
        "subjectHeadings": ["People — Religious Figures — India — Contemporary"],
        "detailsJson": {
            "causes": ["Albanian Catholic upbringing in Ottoman Skopje", "Call to serve the poorest during 1946 'train experience'", "Extreme poverty in post-independence Kolkata"],
            "effects": ["Missionaries of Charity grew to 610 missions in 123 countries", "Nobel Peace Prize 1979", "Became global symbol of charitable service", "Canonized as Catholic saint in 2016", "Sparked debate about charity vs. systemic change"],
            "relationships": [
                {"sourceSlug": "mother-teresa", "sourceName": "Mother Teresa", "verb": "OCCURS_IN", "targetSlug": "india", "targetName": "India", "context": "Spent 69 years in India serving the poor of Kolkata"},
                {"sourceSlug": "mother-teresa", "sourceName": "Mother Teresa", "verb": "INFLUENCES", "targetSlug": "pope-john-paul-ii", "targetName": "Pope John Paul II", "context": "John Paul II fast-tracked her beatification process"},
                {"sourceSlug": "mother-teresa", "sourceName": "Mother Teresa", "verb": "INFLUENCES", "targetSlug": "mahatma-gandhi", "targetName": "Mahatma Gandhi", "context": "Both served India's poor through different philosophies of nonviolence and charity"}
            ]
        }
    },
    {
        "slug": "harriet-tubman",
        "name": "Harriet Tubman",
        "label": "Person",
        "callNumber": "270.harriet-tubman",
        "era": "Modern",
        "summary": "Harriet Tubman (c. 1822–1913), born Araminta Ross into slavery in Dorchester County, Maryland, was an American abolitionist and political activist who escaped slavery in 1849 and subsequently made approximately 13 missions to rescue over 70 enslaved people via the Underground Railroad. She was known as 'Moses' for leading her people to freedom.\n\nTubman carried a pistol on her rescue missions — not for slave catchers, but to discourage any fugitive from turning back and endangering the group. She never lost a single passenger. During the Civil War, she became the first woman to lead an armed assault in U.S. history, commanding the Combahee River Raid (1863) that freed over 700 enslaved people.\n\nAfter the war, Tubman advocated for women's suffrage alongside Susan B. Anthony and established a home for elderly African Americans in Auburn, New York. In 2016, the U.S. Treasury announced plans to place her portrait on the $20 bill — replacing Andrew Jackson, a slaveholder.",
        "continent": "North America", "region": "North America",
        "subjects": ["Underground Railroad", "Abolitionism", "United States", "Slavery", "Civil War", "Women's History", "African American History", "Maryland"],
        "subjectHeadings": ["People — Activists — United States — Modern"],
        "detailsJson": {
            "causes": ["Born into slavery in Maryland", "Traumatic head injury from overseer gave her visions", "Network of abolitionists supported Underground Railroad"],
            "effects": ["Rescued 70+ enslaved people in 13 missions", "First woman to lead armed assault in U.S. military history", "Became icon of American freedom and resistance", "Selected for U.S. $20 bill", "Established home for elderly African Americans"],
            "relationships": [
                {"sourceSlug": "harriet-tubman", "sourceName": "Harriet Tubman", "verb": "OCCURS_IN", "targetSlug": "united-states", "targetName": "United States", "context": "American abolitionist who operated the Underground Railroad"},
                {"sourceSlug": "harriet-tubman", "sourceName": "Harriet Tubman", "verb": "INFLUENCES", "targetSlug": "frederick-douglass", "targetName": "Frederick Douglass", "context": "Both escaped slavery to become leading abolitionists"},
                {"sourceSlug": "harriet-tubman", "sourceName": "Harriet Tubman", "verb": "INFLUENCES", "targetSlug": "abraham-lincoln", "targetName": "Abraham Lincoln", "context": "Served as spy and scout for Union Army during Civil War"},
                {"sourceSlug": "harriet-tubman", "sourceName": "Harriet Tubman", "verb": "INFLUENCES", "targetSlug": "rosa-parks", "targetName": "Rosa Parks", "context": "Tubman's courage paved the way for 20th-century civil rights activism"}
            ]
        }
    },
    {
        "slug": "giuseppe-garibaldi",
        "name": "Giuseppe Garibaldi",
        "label": "Person",
        "callNumber": "270.giuseppe-garibaldi",
        "era": "Modern",
        "summary": "Giuseppe Garibaldi (1807–1882) was an Italian general, patriot, and republican who played a central role in the unification of Italy (Risorgimento). Known as the 'Hero of the Two Worlds' for his military campaigns in South America and Europe, he is considered one of the greatest guerrilla warfare commanders in history.\n\nGaribaldi's most famous achievement was the Expedition of the Thousand (1860), in which he led 1,089 red-shirted volunteers to conquer the Kingdom of the Two Sicilies — a nation of 9 million people defended by a 25,000-strong army. He then surrendered his conquests to King Victor Emmanuel II, sacrificing personal power for Italian unity.\n\nHis charisma, military genius, and selfless dedication made him one of the most admired figures of the 19th century. Abraham Lincoln offered him a Union Army command during the American Civil War. Victor Hugo called him a 'hero of humanity.' His red-shirted volunteers became a model for revolutionary movements worldwide.",
        "continent": "Europe", "region": "Southern Europe",
        "subjects": ["Italian Unification", "Risorgimento", "Italy", "Guerrilla Warfare", "Republicanism", "South America", "Expedition of the Thousand", "Nationalism"],
        "subjectHeadings": ["People — Activists — Italy — Modern"],
        "detailsJson": {
            "causes": ["Italian nationalist sentiment after Congress of Vienna", "Mazzini's republican ideals inspired him", "South American guerrilla warfare experience honed military skills"],
            "effects": ["Conquered Kingdom of Two Sicilies with 1,089 volunteers", "United southern Italy with northern Piedmont-Sardinia", "Red-shirt movement became model for revolutionary guerrillas", "Italian unification completed under Victor Emmanuel II"],
            "relationships": [
                {"sourceSlug": "giuseppe-garibaldi", "sourceName": "Giuseppe Garibaldi", "verb": "CAUSES", "targetSlug": "italian-unification", "targetName": "Italian Unification", "context": "Conquered southern Italy enabling unification under Victor Emmanuel II"},
                {"sourceSlug": "giuseppe-garibaldi", "sourceName": "Giuseppe Garibaldi", "verb": "OCCURS_IN", "targetSlug": "italy", "targetName": "Italy", "context": "Italian patriot who fought for national unification"},
                {"sourceSlug": "giuseppe-garibaldi", "sourceName": "Giuseppe Garibaldi", "verb": "INFLUENCES", "targetSlug": "che-guevara", "targetName": "Che Guevara", "context": "Garibaldi's guerrilla warfare tactics inspired later revolutionaries"},
                {"sourceSlug": "giuseppe-garibaldi", "sourceName": "Giuseppe Garibaldi", "verb": "INFLUENCES", "targetSlug": "otto-von-bismarck", "targetName": "Otto von Bismarck", "context": "Italian unification model paralleled German unification under Bismarck"}
            ]
        }
    },
]

# ════════════════════════════════════════════════════════════════════════
# EXECUTE
# ════════════════════════════════════════════════════════════════════════
print("=== ENRICHMENTS (25 entities) ===")
enriched_count = 0
for slug, data in enrichments:
    if enrich_entity(slug, data):
        enriched_count += 1

print(f"\n  Successfully enriched: {enriched_count}/{len(enrichments)}")

print("\n=== NEW ENTITIES (10 entities) ===")
# First check none of these already exist
existing_slugs = set()
for f in glob.glob(f"{BASE}/**/*.json", recursive=True):
    try:
        d = json.load(open(f))
        existing_slugs.add(d["entities"][0]["slug"].replace("_", "-"))
    except:
        pass

created_count = 0
for entity in new_entities:
    norm = entity["slug"].replace("_", "-")
    if norm in existing_slugs:
        print(f"  SKIP (exists): {entity['slug']}")
    else:
        create_entity(entity)
        created_count += 1

print(f"\n  Created: {created_count}/{len(new_entities)}")
print(f"\n=== BATCH 4 COMPLETE: {enriched_count} enriched, {created_count} created ===")
