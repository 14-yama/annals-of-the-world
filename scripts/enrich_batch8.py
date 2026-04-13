#!/usr/bin/env python3
"""
Batch 8: Enrich 14 worst PARTIAL/STUB entities + Create 6 missing high-importance entities.
Targets: entities <300c (highest priority) + critical missing figures.
"""
import json, glob, os, hashlib, time, urllib.request, urllib.error, urllib.parse

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

def find_doc_by_slug(slug):
    """Search Appwrite for a document by slug attribute."""
    q = json.dumps({"method": "equal", "attribute": "slug", "values": [slug]})
    url = f"{ENDPOINT}/databases/{DB}/collections/{COLLECTION}/documents?queries[]={urllib.parse.quote(q)}"
    req = urllib.request.Request(url, headers=headers())
    try:
        with urllib.request.urlopen(req) as r:
            data = json.loads(r.read())
            docs = data.get("documents", [])
            if docs:
                return docs[0]["$id"]
    except:
        pass
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

# ═══════════════════════════════════════════
# PART 1: ENRICH 14 WORST PARTIAL/STUB ENTITIES
# ═══════════════════════════════════════════

ENRICHMENTS = {
    "blaise-pascal": {
        "summary": "Blaise Pascal (1623\u20131662) was a French mathematician, physicist, inventor, and theologian who made foundational contributions across multiple fields before his death at age 39. His work on probability theory (with Fermat), hydraulic physics, and the first mechanical calculator places him among the most versatile minds of the 17th century.\n\nA child prodigy, Pascal wrote a treatise on conic sections at 16 and built the Pascaline\u2014the first working mechanical calculator\u2014at 19 to help his father with tax computations. His experiments with atmospheric pressure proved the existence of the vacuum (contra Aristotelian physics) and established what became Pascal's law in hydraulics.\n\nIn 1654, Pascal experienced a profound religious conversion during a 'night of fire' and largely abandoned mathematics for theology. His 'Pens\u00e9es' (published posthumously, 1670) remains one of the most celebrated works of French prose and Christian apologetics, containing the famous 'Pascal's Wager' argument for belief in God.\n\nPascal's legacy spans mathematics (Pascal's triangle, probability theory), physics (Pascal's law, the SI pressure unit), computing (the Pascaline, the Pascal programming language), and philosophy. As he wrote: 'The heart has its reasons which reason knows nothing of.'",
        "causes": ["French scientific renaissance under Mersenne's intellectual network", "Father's mathematical education and connections to Parisian scholars", "Personal religious crisis leading to philosophical transformation"],
        "effects": ["Co-founded probability theory with Fermat, enabling modern statistics", "Pascal's law became fundamental to hydraulic engineering", "Pens\u00e9es established new literary form merging philosophy and personal testimony"],
        "relationships": [
            {"sourceSlug": "blaise-pascal", "sourceName": "Blaise Pascal", "verb": "COLLABORATES_WITH", "targetSlug": "pierre-de-fermat", "targetName": "Pierre de Fermat", "context": "1654 correspondence founded mathematical probability theory"},
            {"sourceSlug": "blaise-pascal", "sourceName": "Blaise Pascal", "verb": "INFLUENCES", "targetSlug": "gottfried-wilhelm-leibniz", "targetName": "Gottfried Wilhelm Leibniz", "context": "Leibniz's calculator designs built directly on Pascal's Pascaline"},
            {"sourceSlug": "rene-descartes", "sourceName": "Ren\u00e9 Descartes", "verb": "INFLUENCES", "targetSlug": "blaise-pascal", "targetName": "Blaise Pascal", "context": "Descartes challenged Pascal's vacuum experiments; rival philosophical visions"},
            {"sourceSlug": "blaise-pascal", "sourceName": "Blaise Pascal", "verb": "CREATES", "targetSlug": "pensees", "targetName": "Pens\u00e9es", "context": "Posthumous fragments (1670) containing Pascal's Wager and Christian apologetics"},
            {"sourceSlug": "blaise-pascal", "sourceName": "Blaise Pascal", "verb": "OCCURS_IN", "targetSlug": "paris", "targetName": "Paris", "context": "Lived and worked in Paris; central to Mersenne's scientific circle"}
        ],
        "places": [{"name": "Paris, France", "role": "Scientific career"}, {"name": "Clermont-Ferrand, France", "role": "Birthplace"}, {"name": "Port-Royal, France", "role": "Jansenist religious community"}],
        "subjects": ["Mathematics", "Probability Theory", "Hydraulics", "Christian Apologetics", "France", "Mechanical Calculator", "Philosophy", "Physics"],
        "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS", "RELIGIOUS_INTERPRETATION"]
    },
    "nikita-khrushchev": {
        "summary": "Nikita Sergeyevich Khrushchev (1894\u20131971) was the leader of the Soviet Union from 1953 to 1964 whose 'Secret Speech' denouncing Stalin's crimes (1956) sent shockwaves through the communist world and initiated the era of de-Stalinisation. His tenure encompassed the most dangerous moments of the Cold War, including the Cuban Missile Crisis of October 1962.\n\nRising from Ukrainian peasant origins through Communist Party ranks, Khrushchev consolidated power after Stalin's death in 1953. His February 1956 speech to the 20th Party Congress\u2014detailing Stalin's purges, torture, and cult of personality\u2014was the most explosive political address of the 20th century, leading to the release of millions from the Gulag.\n\nKhrushchev pursued 'peaceful coexistence' with the West while presiding over the Space Race triumph of Sputnik (1957) and Gagarin's orbital flight (1961). But the Cuban Missile Crisis brought the world to the brink of nuclear annihilation before his secret negotiations with Kennedy secured a resolution.\n\nHis agricultural reforms failed, and the Party removed him in a 1964 coup. He spent his final years in forced retirement, dictating memoirs smuggled to the West. His legacy is paradoxical: the man who liberated millions from Stalin's terror also crushed the Hungarian Revolution of 1956 and built the Berlin Wall.",
        "causes": ["Stalin's death in 1953 creating a power vacuum", "Soviet leadership's collective fear of another Stalinist purge", "Cold War nuclear rivalries requiring diplomatic recalibration"],
        "effects": ["De-Stalinisation freed millions from Gulag and transformed Soviet society", "Cuban Missile Crisis resolution established nuclear arms control framework", "Sino-Soviet split fractured the global communist movement"],
        "relationships": [
            {"sourceSlug": "nikita-khrushchev", "sourceName": "Nikita Khrushchev", "verb": "SUCCEEDS", "targetSlug": "joseph-stalin", "targetName": "Joseph Stalin", "context": "Consolidated power after Stalin's 1953 death; denounced Stalin in 1956"},
            {"sourceSlug": "nikita-khrushchev", "sourceName": "Nikita Khrushchev", "verb": "PARTICIPATES_IN", "targetSlug": "cuban-missile-crisis", "targetName": "Cuban Missile Crisis", "context": "October 1962 nuclear standoff; secret negotiations with Kennedy averted war"},
            {"sourceSlug": "nikita-khrushchev", "sourceName": "Nikita Khrushchev", "verb": "INFLUENCES", "targetSlug": "yuri-gagarin", "targetName": "Yuri Gagarin", "context": "Khrushchev championed the Soviet space program that sent Gagarin to orbit"},
            {"sourceSlug": "nikita-khrushchev", "sourceName": "Nikita Khrushchev", "verb": "OCCURS_IN", "targetSlug": "moscow", "targetName": "Moscow", "context": "Led the Soviet Union from the Kremlin 1953-1964"},
            {"sourceSlug": "nikita-khrushchev", "sourceName": "Nikita Khrushchev", "verb": "CAUSES", "targetSlug": "berlin-wall", "targetName": "Berlin Wall", "context": "Authorised construction of the Berlin Wall in August 1961"}
        ],
        "places": [{"name": "Moscow, Russia", "role": "Kremlin leadership"}, {"name": "Kalinovka, Russia", "role": "Birthplace"}, {"name": "Havana, Cuba", "role": "Cuban Missile Crisis"}],
        "subjects": ["Cold War", "De-Stalinisation", "Cuban Missile Crisis", "Soviet Union", "Russia", "Space Race", "Nuclear Weapons", "Communism"],
        "frameworks": ["CAUSE_AND_EFFECT", "WORLD_SYSTEMS", "MARXIST_ANALYSIS"]
    },
    "pericles": {
        "summary": "Pericles (c. 495\u2013429 BCE) was an Athenian statesman, orator, and general who presided over Athens during its Golden Age\u2014the most brilliant period of artistic, intellectual, and democratic achievement in the ancient world. Under his leadership (c. 461\u2013429 BCE), Athens became the cultural capital of the Greek world and the birthplace of Western civilisation's defining institutions.\n\nPericles championed radical democracy, extending political participation to all male citizens regardless of wealth. He initiated the building programme that produced the Parthenon, the Propylaea, and the Erechtheion on the Acropolis\u2014financed controversially from the Delian League treasury meant for collective Greek defence against Persia.\n\nHis 'Funeral Oration' of 431 BCE, recorded by Thucydides, remains the most famous articulation of democratic ideals in Western literature: 'Our constitution is called a democracy because power is in the hands not of a minority but of the whole people.'\n\nPericles died of the plague that devastated Athens in 429 BCE during the Peloponnesian War he had helped provoke. His death marked the end of Athens' Golden Age. As Thucydides judged: 'In name it was a democracy, but in practice it was government by the first citizen.'",
        "causes": ["Athenian victory in the Persian Wars establishing imperial confidence", "Delian League treasury funding cultural programme", "Cleisthenes' democratic reforms creating institutional foundation"],
        "effects": ["Parthenon and Acropolis building programme defined Western architecture", "Funeral Oration became foundational text of democratic ideals", "Golden Age of Athens produced Sophocles, Euripides, Phidias, and Socrates"],
        "relationships": [
            {"sourceSlug": "pericles", "sourceName": "Pericles", "verb": "CREATES", "targetSlug": "parthenon", "targetName": "Parthenon", "context": "Commissioned Parthenon construction 447-432 BCE as centerpiece of Acropolis"},
            {"sourceSlug": "pericles", "sourceName": "Pericles", "verb": "INFLUENCES", "targetSlug": "socrates", "targetName": "Socrates", "context": "Pericles' Athens was the intellectual milieu that produced Socratic philosophy"},
            {"sourceSlug": "pericles", "sourceName": "Pericles", "verb": "PARTICIPATES_IN", "targetSlug": "peloponnesian-war", "targetName": "Peloponnesian War", "context": "Led Athens into war with Sparta 431 BCE; died of plague during the conflict"},
            {"sourceSlug": "pericles", "sourceName": "Pericles", "verb": "OCCURS_IN", "targetSlug": "athens", "targetName": "Athens", "context": "Led Athenian democracy and Golden Age c. 461-429 BCE"},
            {"sourceSlug": "pericles", "sourceName": "Pericles", "verb": "INFLUENCES", "targetSlug": "abraham-lincoln", "targetName": "Abraham Lincoln", "context": "Lincoln's Gettysburg Address echoed Pericles' Funeral Oration"}
        ],
        "places": [{"name": "Athens, Greece", "role": "Political and cultural leadership"}, {"name": "Acropolis, Athens", "role": "Building programme"}, {"name": "Delos, Greece", "role": "Delian League headquarters"}],
        "subjects": ["Athenian Democracy", "Golden Age of Athens", "Parthenon", "Classical Greece", "Greece", "Oratory", "Peloponnesian War", "Architecture"],
        "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS", "COMPARATIVE_CIVILIZATIONS"]
    },
    "fidel-castro": {
        "summary": "Fidel Alejandro Castro Ruz (1926\u20132016) was a Cuban revolutionary and statesman who overthrew the Batista dictatorship in 1959 and ruled Cuba as Prime Minister and then President for nearly five decades\u2014the longest-serving non-royal head of state in the 20th century. His communist revolution 90 miles from Florida became the defining flashpoint of the Cold War in the Western Hemisphere.\n\nTrained as a lawyer, Castro launched his revolution with the failed Moncada Barracks attack in 1953 (producing his famous defence speech: 'History will absolve me'). After exile in Mexico\u2014where he met Che Guevara\u2014he returned to Cuba with 82 guerrillas on the yacht Granma in 1956 and waged a guerrilla war from the Sierra Maestra that toppled Batista on January 1, 1959.\n\nCastro's alliance with the Soviet Union triggered the Bay of Pigs invasion (1961) and the Cuban Missile Crisis (1962), the closest the world came to nuclear war. He built Cuba's renowned healthcare and literacy systems while suppressing political opposition through a one-party state.\n\nSurviving over 600 CIA assassination attempts (by Cuban government count), Castro outlasted ten US presidents. He transferred power to his brother Ra\u00fal in 2008 and died in 2016. His legacy remains fiercely contested: revolutionary hero to some, authoritarian dictator to others.",
        "causes": ["Batista's corrupt US-backed dictatorship and Cuban inequality", "Latin American revolutionary tradition and anti-imperialism", "Cold War Soviet willingness to support anti-American movements"],
        "effects": ["Triggered Bay of Pigs and Cuban Missile Crisis", "Inspired revolutionary movements across Latin America and Africa", "Created enduring US-Cuba diplomatic standoff lasting 60+ years"],
        "relationships": [
            {"sourceSlug": "fidel-castro", "sourceName": "Fidel Castro", "verb": "COLLABORATES_WITH", "targetSlug": "che-guevara", "targetName": "Che Guevara", "context": "Met in Mexico 1955; Guevara joined the Cuban Revolution as key commander"},
            {"sourceSlug": "fidel-castro", "sourceName": "Fidel Castro", "verb": "PARTICIPATES_IN", "targetSlug": "cuban-missile-crisis", "targetName": "Cuban Missile Crisis", "context": "Hosted Soviet missiles provoking 1962 nuclear standoff with the US"},
            {"sourceSlug": "nikita-khrushchev", "sourceName": "Nikita Khrushchev", "verb": "COLLABORATES_WITH", "targetSlug": "fidel-castro", "targetName": "Fidel Castro", "context": "Soviet alliance and missile deployment that triggered 1962 crisis"},
            {"sourceSlug": "fidel-castro", "sourceName": "Fidel Castro", "verb": "OCCURS_IN", "targetSlug": "havana", "targetName": "Havana", "context": "Ruled Cuba from Havana 1959-2008"},
            {"sourceSlug": "fidel-castro", "sourceName": "Fidel Castro", "verb": "INFLUENCES", "targetSlug": "ho-chi-minh", "targetName": "Ho Chi Minh", "context": "Castro's guerrilla model influenced revolutionary movements worldwide"}
        ],
        "places": [{"name": "Havana, Cuba", "role": "Capital and seat of power"}, {"name": "Sierra Maestra, Cuba", "role": "Guerrilla headquarters"}, {"name": "Bir\u00e1n, Cuba", "role": "Birthplace"}],
        "subjects": ["Cuban Revolution", "Cold War", "Communism", "Guerrilla Warfare", "Cuba", "Bay of Pigs", "Latin America", "Anti-Imperialism"],
        "frameworks": ["CAUSE_AND_EFFECT", "WORLD_SYSTEMS", "MARXIST_ANALYSIS"]
    },
    "henry-viii": {
        "summary": "Henry VIII (1491\u20131547) was King of England from 1509 to 1547, best known for his six marriages and for breaking with the Roman Catholic Church to establish the Church of England\u2014a seismic event that reshaped English religion, politics, and identity for centuries. His reign transformed England from a medieval Catholic kingdom into a Protestant nation state.\n\nHenry's desire to annul his first marriage to Catherine of Aragon\u2014who failed to produce a male heir\u2014led him to reject papal authority when Pope Clement VII refused the annulment. The Act of Supremacy (1534) declared the monarch Supreme Head of the Church of England, launching the English Reformation and the Dissolution of the Monasteries that transferred vast ecclesiastical wealth to the Crown.\n\nSix marriages\u2014Catherine of Aragon (divorced), Anne Boleyn (beheaded), Jane Seymour (died), Anne of Cleves (divorced), Catherine Howard (beheaded), Catherine Parr (survived)\u2014produced three children who each ruled England: Edward VI, Mary I, and Elizabeth I.\n\nHenry's reign saw the execution of Thomas More, the rise and fall of Thomas Cromwell, and England's emergence as a naval power. He spent his father's fortune on wars and palaces, dying obese and ulcerous at 55. The Tudor dynasty he fought to perpetuate ended with his granddaughter-less daughter Elizabeth I.",
        "causes": ["Dynastic need for male heir driving annulment crisis", "Rise of Protestantism in Europe providing theological justification", "Papal dependence on Emperor Charles V preventing annulment"],
        "effects": ["English Reformation separated England permanently from Rome", "Dissolution of the Monasteries redistributed 25% of English land", "Act of Supremacy established monarch as head of Church of England"],
        "relationships": [
            {"sourceSlug": "henry-viii", "sourceName": "Henry VIII", "verb": "CAUSES", "targetSlug": "english-reformation", "targetName": "English Reformation", "context": "Act of Supremacy 1534 broke with Rome, establishing Church of England"},
            {"sourceSlug": "henry-viii", "sourceName": "Henry VIII", "verb": "INFLUENCES", "targetSlug": "elizabeth-i", "targetName": "Elizabeth I", "context": "Elizabeth, daughter of Anne Boleyn, completed the Protestant settlement"},
            {"sourceSlug": "henry-viii", "sourceName": "Henry VIII", "verb": "CAUSES", "targetSlug": "dissolution-of-monasteries", "targetName": "Dissolution of the Monasteries", "context": "Dissolved 800+ religious houses, transferring vast wealth to the Crown"},
            {"sourceSlug": "martin-luther", "sourceName": "Martin Luther", "verb": "INFLUENCES", "targetSlug": "henry-viii", "targetName": "Henry VIII", "context": "Lutheran Reformation provided theological framework for the English break with Rome"},
            {"sourceSlug": "henry-viii", "sourceName": "Henry VIII", "verb": "OCCURS_IN", "targetSlug": "london", "targetName": "London", "context": "Reigned from London; built Hampton Court and expanded royal palaces"}
        ],
        "places": [{"name": "London, England", "role": "Court and government"}, {"name": "Greenwich, England", "role": "Birthplace"}, {"name": "Hampton Court, England", "role": "Royal palace"}],
        "subjects": ["English Reformation", "Tudor Dynasty", "Church of England", "Six Wives", "England", "Monarchy", "Dissolution of Monasteries", "Religious Politics"],
        "frameworks": ["CAUSE_AND_EFFECT", "RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"]
    },
    "margaret-thatcher": {
        "summary": "Margaret Hilda Thatcher (1925\u20132013) was Prime Minister of the United Kingdom from 1979 to 1990\u2014the longest-serving British PM of the 20th century and the first woman to hold the office. Her radical free-market programme, dubbed 'Thatcherism,' transformed Britain's economy and redefined the global debate between state intervention and market liberalism.\n\nThe daughter of a Grantham grocer, Thatcher studied chemistry at Oxford before becoming a barrister and Conservative MP. As PM, she privatised state-owned industries (British Telecom, British Gas, British Steel), broke the power of trade unions in the bitter 1984\u201385 miners' strike, and deregulated financial markets in the 'Big Bang' of 1986.\n\nHer victory in the Falklands War (1982) cemented her public image as the 'Iron Lady'\u2014a Soviet nickname she embraced. Her close alliance with Ronald Reagan defined the Anglo-American relationship during the final decade of the Cold War, and their joint pressure helped accelerate the collapse of the Soviet Union.\n\nThatcher remains Britain's most polarising modern leader. Admirers credit her with reviving the British economy; critics blame her for deindustrialisation, rising inequality, and the destruction of mining communities. She was deposed by her own Conservative Party in 1990 over Europe policy and the unpopular poll tax.",
        "causes": ["1970s British economic decline, strikes, and 'Winter of Discontent'", "Monetarist economics of Hayek and Friedman providing ideological framework", "Cold War anti-communism and Anglo-American alliance"],
        "effects": ["Privatisation of state industries became global model (Thatcherism)", "Defeated miners' union, permanently reducing trade union power in Britain", "Close Reagan alliance helped end the Cold War"],
        "relationships": [
            {"sourceSlug": "margaret-thatcher", "sourceName": "Margaret Thatcher", "verb": "COLLABORATES_WITH", "targetSlug": "ronald-reagan", "targetName": "Ronald Reagan", "context": "Reagan-Thatcher alliance defined Anglo-American Cold War strategy"},
            {"sourceSlug": "margaret-thatcher", "sourceName": "Margaret Thatcher", "verb": "PARTICIPATES_IN", "targetSlug": "falklands-war", "targetName": "Falklands War", "context": "1982 Falklands victory cemented her 'Iron Lady' image"},
            {"sourceSlug": "margaret-thatcher", "sourceName": "Margaret Thatcher", "verb": "INFLUENCES", "targetSlug": "mikhail-gorbachev", "targetName": "Mikhail Gorbachev", "context": "Thatcher's early recognition of Gorbachev as reformer influenced Western policy"},
            {"sourceSlug": "margaret-thatcher", "sourceName": "Margaret Thatcher", "verb": "OCCURS_IN", "targetSlug": "london", "targetName": "London", "context": "Governed from 10 Downing Street 1979-1990"},
            {"sourceSlug": "adam-smith", "sourceName": "Adam Smith", "verb": "INFLUENCES", "targetSlug": "margaret-thatcher", "targetName": "Margaret Thatcher", "context": "Free-market economics of Smith, Hayek, and Friedman underpinned Thatcherism"}
        ],
        "places": [{"name": "London, England", "role": "Prime Minister at 10 Downing Street"}, {"name": "Grantham, England", "role": "Birthplace"}, {"name": "Falkland Islands", "role": "1982 war"}],
        "subjects": ["Thatcherism", "Privatisation", "Cold War", "Falklands War", "United Kingdom", "Free Market", "Trade Unions", "Women in Politics"],
        "frameworks": ["CAUSE_AND_EFFECT", "WORLD_SYSTEMS", "FEMINIST_PERSPECTIVE"]
    },
    "igor-stravinsky": {
        "summary": "Igor Fyodorovich Stravinsky (1882\u20131971) was a Russian-born composer whose 'The Rite of Spring' (1913) provoked a riot at its Paris premiere and launched the modernist revolution in music. Across seven decades, he reinvented his style three times\u2014from Russian nationalism to neoclassicism to serialism\u2014making him the most influential composer of the 20th century.\n\nBorn near St. Petersburg and trained under Rimsky-Korsakov, Stravinsky achieved fame with three ballets for Diaghilev's Ballets Russes: 'The Firebird' (1910), 'Petrushka' (1911), and 'The Rite of Spring' (1913). The Rite's savage rhythms, polytonal harmonies, and primitivist choreography were so shocking that the audience erupted in fistfights on opening night.\n\nAfter World War I, Stravinsky pivoted to neoclassicism\u2014drawing on Bach, Pergolesi, and Mozart in works like 'Pulcinella' (1920) and 'Symphony of Psalms' (1930). After 1950, he astonished the music world again by adopting the twelve-tone serial techniques of his former rival Schoenberg.\n\nStravinsky lived in Switzerland, France, and finally Los Angeles, becoming a US citizen in 1945. His total output\u2014ballets, symphonies, concertos, operas, and sacred music\u2014reshaped every dimension of musical composition. As he declared: 'I have learned throughout my life that the important thing is not what one likes or dislikes, but what one can renounce.'",
        "causes": ["Russian nationalist musical tradition (Rimsky-Korsakov's teaching)", "Diaghilev's Ballets Russes providing platform for avant-garde collaboration", "Modernist artistic movements in early 20th-century Paris"],
        "effects": ["'Rite of Spring' launched musical modernism and new rhythmic language", "Neoclassical period influenced entire mid-century compositional aesthetic", "Serial adoption demonstrated music's perpetual capacity for reinvention"],
        "relationships": [
            {"sourceSlug": "igor-stravinsky", "sourceName": "Igor Stravinsky", "verb": "CREATES", "targetSlug": "rite-of-spring", "targetName": "The Rite of Spring", "context": "1913 premiere provoked riot; launched modernist revolution in music"},
            {"sourceSlug": "pyotr-ilyich-tchaikovsky", "sourceName": "Pyotr Ilyich Tchaikovsky", "verb": "INFLUENCES", "targetSlug": "igor-stravinsky", "targetName": "Igor Stravinsky", "context": "Stravinsky called Tchaikovsky 'the most Russian of us all'; absorbed his orchestral mastery"},
            {"sourceSlug": "igor-stravinsky", "sourceName": "Igor Stravinsky", "verb": "INFLUENCES", "targetSlug": "leonard-bernstein", "targetName": "Leonard Bernstein", "context": "Stravinsky's rhythmic and tonal innovations shaped mid-century American music"},
            {"sourceSlug": "igor-stravinsky", "sourceName": "Igor Stravinsky", "verb": "OCCURS_IN", "targetSlug": "paris", "targetName": "Paris", "context": "Rite of Spring premiered at Th\u00e9\u00e2tre des Champs-\u00c9lys\u00e9es, May 29, 1913"},
            {"sourceSlug": "johann-sebastian-bach", "sourceName": "Johann Sebastian Bach", "verb": "INFLUENCES", "targetSlug": "igor-stravinsky", "targetName": "Igor Stravinsky", "context": "Bach's formal structures inspired Stravinsky's neoclassical period"}
        ],
        "places": [{"name": "Paris, France", "role": "Rite of Spring premiere and early career"}, {"name": "Oranienbaum, Russia", "role": "Birthplace"}, {"name": "Los Angeles, USA", "role": "Final home 1940-1969"}],
        "subjects": ["Modernism", "Ballet", "Rite of Spring", "Russian Music", "Neoclassicism", "Russia", "Composition", "Serialism"],
        "frameworks": ["CULTURAL_TRANSMISSION", "CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"]
    },
    "louis-xiv": {
        "summary": "Louis XIV (1638\u20131715), the 'Sun King,' was King of France for 72 years\u2014the longest reign in European history. His absolutist rule, magnificent court at Versailles, and aggressive foreign policy made France the dominant power in Europe and established the model of centralised monarchy that persisted until the French Revolution.\n\nBecoming king at age four, Louis endured the traumatic Fronde rebellions (1648\u20131653) that taught him to distrust the nobility. After Cardinal Mazarin's death in 1661, he famously declared 'L'\u00c9tat, c'est moi' ('I am the state') and ruled personally without a chief minister for 54 years.\n\nLouis built the Palace of Versailles\u2014transforming a hunting lodge into the most spectacular royal residence in history\u2014and relocated the entire French government there in 1682. He tamed the nobility by requiring their attendance at court, patronised Moli\u00e8re, Racine, and Lully, and made French the language of European diplomacy and culture.\n\nHis Revocation of the Edict of Nantes (1685) expelled 200,000 Huguenots, devastating French commerce. His wars of expansion united Europe against France in coalitions that drained the treasury. He died in 1715, bequeathing his five-year-old great-grandson an empire magnificent in culture but exhausted in finances.",
        "causes": ["Fronde rebellions traumatising the young king against noble independence", "Cardinal Mazarin's political education and death creating a power vacuum", "French economic and military strength as Europe's most populous state"],
        "effects": ["Versailles became model for royal courts across Europe", "French became the international language of diplomacy and culture", "Wars and Huguenot expulsion weakened France, setting stage for Revolution"],
        "relationships": [
            {"sourceSlug": "louis-xiv", "sourceName": "Louis XIV", "verb": "CREATES", "targetSlug": "palace-of-versailles", "targetName": "Palace of Versailles", "context": "Built 1661-1715; became seat of French government and model for European courts"},
            {"sourceSlug": "louis-xiv", "sourceName": "Louis XIV", "verb": "INFLUENCES", "targetSlug": "peter-the-great", "targetName": "Peter the Great", "context": "Peter visited Versailles and modeled his court reforms on Louis' absolutism"},
            {"sourceSlug": "louis-xiv", "sourceName": "Louis XIV", "verb": "CAUSES", "targetSlug": "french-revolution", "targetName": "French Revolution", "context": "His wars and absolutism created the fiscal crisis that eventually caused the Revolution"},
            {"sourceSlug": "louis-xiv", "sourceName": "Louis XIV", "verb": "OCCURS_IN", "targetSlug": "versailles", "targetName": "Versailles", "context": "Ruled from Versailles 1682-1715"},
            {"sourceSlug": "louis-xiv", "sourceName": "Louis XIV", "verb": "INFLUENCES", "targetSlug": "montesquieu", "targetName": "Montesquieu", "context": "Louis' absolutism inspired Montesquieu's separation of powers doctrine"}
        ],
        "places": [{"name": "Versailles, France", "role": "Royal court and government"}, {"name": "Saint-Germain-en-Laye, France", "role": "Birthplace"}, {"name": "Paris, France", "role": "Capital of realm"}],
        "subjects": ["Absolutism", "Versailles", "French Culture", "Sun King", "France", "Monarchy", "Baroque", "European Wars"],
        "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS", "WORLD_SYSTEMS"]
    },
    "francis-of-assisi": {
        "summary": "Francis of Assisi (c. 1181\u20131226), born Giovanni di Pietro di Bernardone, was an Italian friar and mystic who founded the Franciscan Order and became the most beloved saint in Christian history. His radical embrace of poverty, his love of nature, and his gentle charisma made him a figure who transcends religious boundaries.\n\nThe son of a wealthy cloth merchant, Francis lived as a carefree youth until a spiritual crisis during imprisonment after the Battle of Collestrada (1202). He renounced his inheritance in a dramatic public gesture, stripping naked before the bishop of Assisi and declaring God as his only father.\n\nFrancis wandered as a mendicant preacher, rebuilding ruined churches, caring for lepers, and attracting followers who became the Order of Friars Minor (Franciscans)\u2014approved by Pope Innocent III in 1209. His 'Canticle of the Sun' (c. 1224) is the earliest major work of Italian literature.\n\nIn 1224, Francis received the stigmata\u2014the wounds of Christ\u2014on Mount La Verna, the first recorded instance in Christian history. He died at 44, blind and in pain, and was canonised just two years later. In 1979, Pope John Paul II declared him patron saint of ecology. As G.K. Chesterton wrote: 'He was a poet whose whole life was a poem.'",
        "causes": ["Personal spiritual crisis and disillusionment with wealth", "12th-century reform movements seeking return to apostolic poverty", "Crusader-era encounter with Islam broadening his Christian vision"],
        "effects": ["Founded Franciscan Order, the largest religious order in Catholic history", "Canticle of the Sun inaugurated Italian vernacular literature", "Became patron saint of ecology, inspiring modern environmental spirituality"],
        "relationships": [
            {"sourceSlug": "francis-of-assisi", "sourceName": "Francis of Assisi", "verb": "CREATES", "targetSlug": "franciscan-order", "targetName": "Franciscan Order", "context": "Founded Order of Friars Minor, approved by Pope Innocent III in 1209"},
            {"sourceSlug": "francis-of-assisi", "sourceName": "Francis of Assisi", "verb": "INFLUENCES", "targetSlug": "pope-john-paul-ii", "targetName": "Pope John Paul II", "context": "John Paul II declared Francis patron saint of ecology in 1979"},
            {"sourceSlug": "francis-of-assisi", "sourceName": "Francis of Assisi", "verb": "INFLUENCES", "targetSlug": "dante-alighieri", "targetName": "Dante Alighieri", "context": "Dante devoted Paradiso XI to Francis, praising his marriage to Lady Poverty"},
            {"sourceSlug": "francis-of-assisi", "sourceName": "Francis of Assisi", "verb": "OCCURS_IN", "targetSlug": "assisi", "targetName": "Assisi", "context": "Born, preached, and died in Assisi; basilica built over his tomb"},
            {"sourceSlug": "jesus-of-nazareth", "sourceName": "Jesus of Nazareth", "verb": "INFLUENCES", "targetSlug": "francis-of-assisi", "targetName": "Francis of Assisi", "context": "Francis sought to literally imitate Christ's poverty and preaching"}
        ],
        "places": [{"name": "Assisi, Italy", "role": "Birthplace and ministry"}, {"name": "La Verna, Italy", "role": "Received the stigmata"}, {"name": "Rome, Italy", "role": "Papal approval of the order"}],
        "subjects": ["Franciscan Order", "Poverty", "Mysticism", "Italian Literature", "Italy", "Christianity", "Ecology", "Saints"],
        "frameworks": ["RELIGIOUS_INTERPRETATION", "CAUSE_AND_EFFECT", "CULTURAL_TRANSMISSION"]
    },
    "ibn-sina": {
        "summary": "Ibn Sina (c. 980\u20131037), known in the West as Avicenna, was a Persian polymath whose 'Canon of Medicine' was the standard medical textbook in Europe and the Islamic world for over 600 years\u2014the longest reign of any medical text in history. He is widely regarded as the father of early modern medicine and one of the most significant philosophers of the Islamic Golden Age.\n\nBorn in Afshana (modern Uzbekistan), Ibn Sina was a child prodigy who had memorised the entire Quran by age 10 and mastered medicine by 16. He served as court physician to multiple rulers across Central Asia and Persia, producing over 450 works on medicine, philosophy, astronomy, alchemy, and theology.\n\nThe 'Canon of Medicine' (al-Qanun fi al-Tibb, 1025) systematised Greek, Roman, and Islamic medical knowledge into five comprehensive volumes covering general medicine, pharmacology, organ-specific diseases, systemic conditions, and compound drugs. It introduced the concepts of quarantine, clinical trials, and risk factor analysis.\n\nHis philosophical masterwork 'The Book of Healing' (Kitab al-Shifa) synthesised Aristotelian and Neoplatonic philosophy with Islamic theology, profoundly influencing Thomas Aquinas and medieval European scholasticism. Ibn Sina died at 57 in Hamadan, where his tomb remains a pilgrimage site. His epitaph reads: 'The width of the earth was not enough for him.'",
        "causes": ["Islamic Golden Age patronage of science and translation movement", "Central Asian political instability requiring mobile court scholarship", "Synthesis of Greek (Galen, Hippocrates) and Islamic medical traditions"],
        "effects": ["Canon of Medicine was standard European medical text for 600+ years", "Established systematic clinical medicine and pharmacological methodology", "Philosophical synthesis influenced Aquinas and European scholasticism"],
        "relationships": [
            {"sourceSlug": "ibn-sina", "sourceName": "Ibn Sina", "verb": "CREATES", "targetSlug": "canon-of-medicine", "targetName": "Canon of Medicine", "context": "Completed c. 1025; standard medical textbook in Europe for 600 years"},
            {"sourceSlug": "ibn-sina", "sourceName": "Ibn Sina", "verb": "INFLUENCES", "targetSlug": "thomas-aquinas", "targetName": "Thomas Aquinas", "context": "Avicenna's Aristotelian synthesis shaped Aquinas's Scholastic philosophy"},
            {"sourceSlug": "aristotle", "sourceName": "Aristotle", "verb": "INFLUENCES", "targetSlug": "ibn-sina", "targetName": "Ibn Sina", "context": "Ibn Sina built his philosophical system on Aristotelian logic and metaphysics"},
            {"sourceSlug": "ibn-sina", "sourceName": "Ibn Sina", "verb": "OCCURS_IN", "targetSlug": "bukhara", "targetName": "Bukhara", "context": "Studied and practiced medicine in Bukhara under Samanid patronage"},
            {"sourceSlug": "hippocrates", "sourceName": "Hippocrates", "verb": "INFLUENCES", "targetSlug": "ibn-sina", "targetName": "Ibn Sina", "context": "Ibn Sina systematised and extended Hippocratic and Galenic medical traditions"}
        ],
        "places": [{"name": "Bukhara, Uzbekistan", "role": "Education and early career"}, {"name": "Isfahan, Iran", "role": "Most productive period"}, {"name": "Hamadan, Iran", "role": "Death and tomb"}],
        "subjects": ["Islamic Golden Age", "Medicine", "Philosophy", "Canon of Medicine", "Persia", "Pharmacology", "Scholasticism", "Central Asia"],
        "frameworks": ["CAUSE_AND_EFFECT", "CULTURAL_TRANSMISSION", "COMPARATIVE_CIVILIZATIONS"]
    },
    "niels-bohr": {
        "summary": "Niels Henrik David Bohr (1885\u20131962) was a Danish physicist who fundamentally reshaped our understanding of atomic structure and quantum mechanics. His 1913 model of the atom\u2014with electrons orbiting the nucleus in quantised energy levels\u2014earned him the Nobel Prize in Physics in 1922 and launched the quantum revolution that defines modern physics.\n\nBohr's atomic model solved the mystery of why atoms emit light at specific frequencies by applying Planck's quantum theory to Rutherford's nuclear model. He showed that electrons occupy discrete orbits and emit photons when jumping between them\u2014a breakthrough that explained the entire periodic table of elements.\n\nAt his Institute for Theoretical Physics in Copenhagen (founded 1921), Bohr mentored a generation of physicists\u2014Heisenberg, Pauli, Dirac, and Landau among them. The 'Copenhagen interpretation' of quantum mechanics, developed there, remains the standard framework for understanding quantum phenomena. His principle of complementarity (wave-particle duality) challenged classical logic itself.\n\nDuring World War II, Bohr escaped Nazi-occupied Denmark to Sweden in a fishing boat and joined the Allied atomic research effort. He later advocated for peaceful use of nuclear energy and international arms control. His conversations with Heisenberg in occupied Copenhagen (1941) remain among modern science's most debated episodes.",
        "causes": ["Planck's quantum theory and Rutherford's nuclear model providing building blocks", "Copenhagen's tradition of international scientific collaboration", "Crisis in classical physics' inability to explain atomic spectra"],
        "effects": ["Bohr model explained atomic spectra and the periodic table", "Copenhagen interpretation became standard framework of quantum mechanics", "Mentored generation of Nobel laureates at his Copenhagen institute"],
        "relationships": [
            {"sourceSlug": "max-planck", "sourceName": "Max Planck", "verb": "INFLUENCES", "targetSlug": "niels-bohr", "targetName": "Niels Bohr", "context": "Bohr applied Planck's quantisation to atomic structure in 1913"},
            {"sourceSlug": "niels-bohr", "sourceName": "Niels Bohr", "verb": "INFLUENCES", "targetSlug": "albert-einstein", "targetName": "Albert Einstein", "context": "Bohr-Einstein debates over quantum mechanics defined 20th-century physics"},
            {"sourceSlug": "niels-bohr", "sourceName": "Niels Bohr", "verb": "CREATES", "targetSlug": "bohr-model", "targetName": "Bohr Model", "context": "1913 atomic model with quantised electron orbits"},
            {"sourceSlug": "niels-bohr", "sourceName": "Niels Bohr", "verb": "OCCURS_IN", "targetSlug": "copenhagen", "targetName": "Copenhagen", "context": "Founded and led Institute for Theoretical Physics in Copenhagen"},
            {"sourceSlug": "niels-bohr", "sourceName": "Niels Bohr", "verb": "PARTICIPATES_IN", "targetSlug": "manhattan-project", "targetName": "Manhattan Project", "context": "Escaped Denmark 1943; consulted on Allied atomic weapons programme"}
        ],
        "places": [{"name": "Copenhagen, Denmark", "role": "Institute and career"}, {"name": "Copenhagen, Denmark", "role": "Birthplace"}, {"name": "Los Alamos, New Mexico", "role": "Manhattan Project consultation"}],
        "subjects": ["Quantum Mechanics", "Atomic Physics", "Bohr Model", "Nobel Prize", "Denmark", "Copenhagen Interpretation", "Nuclear Physics", "Complementarity"],
        "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS", "COMPARATIVE_CIVILIZATIONS"]
    },
    "xerxes-i": {
        "summary": "Xerxes I (c. 518\u2013465 BCE), known as Xerxes the Great, was the fourth Achaemenid King of Kings who ruled the largest empire the world had yet seen\u2014stretching from Libya to India. His massive invasion of Greece in 480 BCE, featuring the battles of Thermopylae and Salamis, became one of the defining conflicts in Western civilisation's founding narrative.\n\nSon of Darius I and grandson of Cyrus the Great, Xerxes inherited both an empire of 50 million subjects and his father's unfinished war against the Greek city-states. He assembled the largest military force of the ancient world\u2014ancient sources claim over one million troops, though modern scholars estimate 100,000\u2013300,000\u2014and famously bridged the Hellespont with a pontoon of boats.\n\nAt Thermopylae (August 480 BCE), 300 Spartans under King Leonidas held the narrow pass for three days before being overwhelmed. Xerxes burned Athens but suffered a devastating naval defeat at Salamis when Themistocles lured the Persian fleet into the narrow strait. After the follow-up defeat at Plataea (479 BCE), Xerxes withdrew to Persia.\n\nXerxes completed Persepolis\u2014the ceremonial capital begun by his father\u2014whose ruins remain among the most impressive archaeological sites of the ancient world. He was assassinated in a palace coup in 465 BCE. The Greek victories he suffered became foundational to the Western narrative of freedom triumphing over despotism.",
        "causes": ["Darius I's unfinished war against Greece requiring completion", "Achaemenid imperial ideology demanding universal dominion", "Ionian Revolt and Marathon defeat demanding Persian revenge"],
        "effects": ["Greek victories at Thermopylae and Salamis forged Western identity narrative", "Persian defeat ended Achaemenid expansion into Europe", "Completed Persepolis, the greatest ceremonial complex of the ancient Near East"],
        "relationships": [
            {"sourceSlug": "xerxes-i", "sourceName": "Xerxes I", "verb": "PARTICIPATES_IN", "targetSlug": "battle-of-thermopylae", "targetName": "Battle of Thermopylae", "context": "Fought and defeated Leonidas' 300 Spartans at Thermopylae, 480 BCE"},
            {"sourceSlug": "cyrus-the-great", "sourceName": "Cyrus the Great", "verb": "INFLUENCES", "targetSlug": "xerxes-i", "targetName": "Xerxes I", "context": "Xerxes inherited Cyrus's imperial vision and Achaemenid dynasty"},
            {"sourceSlug": "xerxes-i", "sourceName": "Xerxes I", "verb": "INFLUENCES", "targetSlug": "pericles", "targetName": "Pericles", "context": "Persian defeat enabled Athenian Golden Age that Pericles led"},
            {"sourceSlug": "xerxes-i", "sourceName": "Xerxes I", "verb": "OCCURS_IN", "targetSlug": "persepolis", "targetName": "Persepolis", "context": "Completed Persepolis ceremonial capital begun by Darius I"},
            {"sourceSlug": "xerxes-i", "sourceName": "Xerxes I", "verb": "PARTICIPATES_IN", "targetSlug": "battle-of-salamis", "targetName": "Battle of Salamis", "context": "Devastating naval defeat at Salamis ended Persian invasion of Greece"}
        ],
        "places": [{"name": "Persepolis, Iran", "role": "Ceremonial capital"}, {"name": "Thermopylae, Greece", "role": "Famous battle"}, {"name": "Susa, Iran", "role": "Administrative capital"}],
        "subjects": ["Achaemenid Empire", "Persian Wars", "Thermopylae", "Salamis", "Persia", "Ancient Greece", "Imperial Expansion", "Persepolis"],
        "frameworks": ["CAUSE_AND_EFFECT", "COMPARATIVE_CIVILIZATIONS", "STRUCTURAL_ANALYSIS"]
    },
    "ronald-reagan": {
        "summary": "Ronald Wilson Reagan (1911\u20132004) was the 40th President of the United States (1981\u20131989), a former Hollywood actor who became the most consequential conservative leader of the 20th century. His presidency restored American confidence after the malaise of the 1970s, launched the neoliberal revolution, and\u2014through massive military buildup and rhetorical confrontation\u2014helped bring about the end of the Cold War.\n\nReagan won the 1980 election in a landslide against Jimmy Carter, promising to cut taxes, reduce government, and confront the Soviet Union. His supply-side 'Reaganomics'\u2014combining large tax cuts with increased military spending\u2014reduced inflation but tripled the national debt. He survived an assassination attempt in 1981, quipping to surgeons: 'I hope you're all Republicans.'\n\nHis 1987 speech at the Berlin Wall\u2014'Mr. Gorbachev, tear down this wall!'\u2014became the defining moment of his presidency. The Strategic Defence Initiative ('Star Wars'), his arms buildup, and his willingness to negotiate with Gorbachev at Reykjavik (1986) are credited by many historians with hastening the Soviet collapse.\n\nReagan left office with the highest approval rating since FDR. The Iran-Contra affair and deregulation's long-term consequences remain controversial. He was diagnosed with Alzheimer's in 1994 and died in 2004. He transformed the Republican Party and American conservatism in ways that persist to this day.",
        "causes": ["1970s economic malaise, inflation, and Iranian hostage crisis", "Conservative intellectual movement (Buckley, Goldwater, Friedman)", "Cold War tensions and Soviet invasion of Afghanistan (1979)"],
        "effects": ["Supply-side economics and deregulation reshaped US economic policy", "Military buildup and diplomacy contributed to end of Cold War", "Transformed Republican Party into vehicle for ideological conservatism"],
        "relationships": [
            {"sourceSlug": "ronald-reagan", "sourceName": "Ronald Reagan", "verb": "COLLABORATES_WITH", "targetSlug": "margaret-thatcher", "targetName": "Margaret Thatcher", "context": "Reagan-Thatcher alliance defined Anglo-American Cold War strategy"},
            {"sourceSlug": "ronald-reagan", "sourceName": "Ronald Reagan", "verb": "INFLUENCES", "targetSlug": "mikhail-gorbachev", "targetName": "Mikhail Gorbachev", "context": "Reagan's military buildup and Reykjavik negotiations pressured Soviet reform"},
            {"sourceSlug": "ronald-reagan", "sourceName": "Ronald Reagan", "verb": "PARTICIPATES_IN", "targetSlug": "cold-war", "targetName": "Cold War", "context": "'Mr. Gorbachev, tear down this wall!' — Berlin, June 12, 1987"},
            {"sourceSlug": "ronald-reagan", "sourceName": "Ronald Reagan", "verb": "OCCURS_IN", "targetSlug": "washington-dc", "targetName": "Washington D.C.", "context": "40th President of the United States, 1981-1989"},
            {"sourceSlug": "adam-smith", "sourceName": "Adam Smith", "verb": "INFLUENCES", "targetSlug": "ronald-reagan", "targetName": "Ronald Reagan", "context": "Free-market economics of Smith, Hayek, and Friedman underpinned Reaganomics"}
        ],
        "places": [{"name": "Washington D.C., USA", "role": "Presidency 1981-1989"}, {"name": "Tampico, Illinois", "role": "Birthplace"}, {"name": "Berlin, Germany", "role": "Brandenburg Gate speech 1987"}],
        "subjects": ["Reaganomics", "Cold War", "Conservatism", "Deregulation", "United States", "Berlin Wall", "Supply-Side Economics", "Republican Party"],
        "frameworks": ["CAUSE_AND_EFFECT", "WORLD_SYSTEMS", "STRUCTURAL_ANALYSIS"]
    },
    "mikhail-gorbachev": {
        "summary": "Mikhail Sergeyevich Gorbachev (1931\u20132022) was the last leader of the Soviet Union, serving as General Secretary of the Communist Party from 1985 to 1991. His reforms of glasnost (openness) and perestroika (restructuring) inadvertently triggered the dissolution of the USSR and the end of the Cold War\u2014the most consequential geopolitical transformation since World War II.\n\nBorn to a peasant family in Stavropol, Gorbachev rose through party ranks as a reformer. Inheriting a stagnating economy and an unwinnable Afghan war, he pursued radical transparency (glasnost) in media and politics and economic restructuring (perestroika) to revitalise the Soviet system\u2014not to destroy it.\n\nHis decision not to use military force as Eastern European nations broke free in 1989\u2014Poland, Hungary, Czechoslovakia, East Germany\u2014was the most remarkable act of political restraint in modern history. The fall of the Berlin Wall on November 9, 1989 became the defining image of the Cold War's end. He won the Nobel Peace Prize in 1990.\n\nThe August 1991 coup attempt by hardliners failed but destroyed his authority. Boris Yeltsin emerged as Russia's leader, and the Soviet Union formally dissolved on December 25, 1991. Revered in the West as the man who ended the Cold War peacefully, Gorbachev was reviled by many Russians for presiding over imperial collapse. He died in 2022 at age 91.",
        "causes": ["Soviet economic stagnation and technological lag behind the West", "Afghan War draining Soviet military and economic resources", "Reagan's arms buildup increasing unsustainable defense spending pressure"],
        "effects": ["Glasnost and perestroika inadvertently dissolved the Soviet Union", "Non-intervention allowed peaceful 1989 revolutions across Eastern Europe", "Nobel Peace Prize 1990; ended the Cold War without nuclear conflict"],
        "relationships": [
            {"sourceSlug": "mikhail-gorbachev", "sourceName": "Mikhail Gorbachev", "verb": "CAUSES", "targetSlug": "fall-of-berlin-wall", "targetName": "Fall of the Berlin Wall", "context": "Non-intervention policy allowed the wall to fall, November 9, 1989"},
            {"sourceSlug": "ronald-reagan", "sourceName": "Ronald Reagan", "verb": "COLLABORATES_WITH", "targetSlug": "mikhail-gorbachev", "targetName": "Mikhail Gorbachev", "context": "Reykjavik and INF Treaty negotiations helped end the Cold War"},
            {"sourceSlug": "mikhail-gorbachev", "sourceName": "Mikhail Gorbachev", "verb": "CAUSES", "targetSlug": "dissolution-of-ussr", "targetName": "Dissolution of the Soviet Union", "context": "Reforms created conditions for Soviet dissolution, December 25, 1991"},
            {"sourceSlug": "mikhail-gorbachev", "sourceName": "Mikhail Gorbachev", "verb": "OCCURS_IN", "targetSlug": "moscow", "targetName": "Moscow", "context": "Led the Soviet Union from the Kremlin, 1985-1991"},
            {"sourceSlug": "nikita-khrushchev", "sourceName": "Nikita Khrushchev", "verb": "INFLUENCES", "targetSlug": "mikhail-gorbachev", "targetName": "Mikhail Gorbachev", "context": "Khrushchev's de-Stalinisation was model for Gorbachev's reform agenda"}
        ],
        "places": [{"name": "Moscow, Russia", "role": "Kremlin leadership"}, {"name": "Stavropol, Russia", "role": "Birthplace and early career"}, {"name": "Berlin, Germany", "role": "Wall fell under his watch"}],
        "subjects": ["Glasnost", "Perestroika", "Cold War", "Soviet Union", "Russia", "Berlin Wall", "Nobel Peace Prize", "Dissolution of USSR"],
        "frameworks": ["CAUSE_AND_EFFECT", "WORLD_SYSTEMS", "STRUCTURAL_ANALYSIS"]
    },
}

# ═══════════════════════════════════════════
# PART 2: CREATE 6 MISSING HIGH-IMPORTANCE ENTITIES
# ═══════════════════════════════════════════

NEW_ENTITIES = [
    {
        "slug": "oliver-cromwell",
        "name": "Oliver Cromwell",
        "label": "Person",
        "callNumber": "222.oliver-cromwell",
        "era": "Early Modern",
        "eraSlug": "early-modern",
        "eraDivision": "Early Modern",
        "eraDivisionCode": "940",
        "region": "Europe",
        "continent": "Europe",
        "status": "Published",
        "born": "1599-04-25",
        "died": "1658-09-03",
        "wikidataQid": "Q44279",
        "wikipediaUrl": "https://en.wikipedia.org/wiki/Oliver_Cromwell",
        "importanceScore": 8,
        "subjectHeadings": ["People \u2014 Heads of State \u2014 Europe \u2014 Early Modern"],
        "subjects": ["English Civil War", "Republic", "Puritanism", "Regicide", "England", "Military History", "Parliament", "Protectorate"],
        "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS", "RELIGIOUS_INTERPRETATION"],
        "summary": "Oliver Cromwell (1599\u20131658) was an English military and political leader who overthrew King Charles I, signed his death warrant, abolished the monarchy, and ruled England as Lord Protector from 1653 to 1658. The only commoner ever to become England's head of state, he remains one of the most controversial figures in British history.\n\nA Huntingdon gentleman and Puritan MP, Cromwell proved a military genius during the English Civil Wars. His New Model Army\u2014disciplined, meritocratic, and religiously fervent\u2014defeated the Royalists at Marston Moor (1644) and Naseby (1645), ending Charles I's cause. The king was tried and executed on January 30, 1649.\n\nAs Lord Protector, Cromwell dissolved Parliament, crushed Royalist resistance in Ireland (the massacres at Drogheda and Wexford remain deeply controversial), and established a republican government. He granted religious toleration to all Protestants and readmitted Jews to England for the first time since 1290.\n\nCromwell died of malaria and kidney disease on September 3, 1658. The Protectorate collapsed within two years. After the Restoration, his body was exhumed from Westminster Abbey, posthumously hanged, and his head displayed on a pike for 25 years. His legacy splits British opinion: liberator or dictator, parliamentarian or tyrant.",
        "detailsJson": {
            "causes": ["Stuart absolutism and conflict with Parliament over taxation", "Puritan religious conviction opposing Catholic-leaning monarchy", "English constitutional tradition of parliamentary sovereignty"],
            "effects": ["Execution of Charles I established precedent that no king is above the law", "English Republic demonstrated viability of non-monarchical government", "Conquest of Ireland created lasting sectarian divisions"],
            "relationships": [
                {"sourceSlug": "oliver-cromwell", "sourceName": "Oliver Cromwell", "verb": "CAUSES", "targetSlug": "execution-of-charles-i", "targetName": "Execution of Charles I", "context": "Signed death warrant; king beheaded January 30, 1649"},
                {"sourceSlug": "oliver-cromwell", "sourceName": "Oliver Cromwell", "verb": "PARTICIPATES_IN", "targetSlug": "english-civil-war", "targetName": "English Civil War", "context": "Led New Model Army to victory at Marston Moor and Naseby"},
                {"sourceSlug": "oliver-cromwell", "sourceName": "Oliver Cromwell", "verb": "INFLUENCES", "targetSlug": "george-washington", "targetName": "George Washington", "context": "Republican precedent influenced American revolutionary thought"},
                {"sourceSlug": "oliver-cromwell", "sourceName": "Oliver Cromwell", "verb": "OCCURS_IN", "targetSlug": "london", "targetName": "London", "context": "Ruled as Lord Protector from Whitehall Palace, 1653-1658"},
                {"sourceSlug": "john-locke", "sourceName": "John Locke", "verb": "INFLUENCES", "targetSlug": "oliver-cromwell", "targetName": "Oliver Cromwell", "context": "Civil War constitutional debates shaped Locke's political philosophy"}
            ],
            "places": [{"name": "London, England", "role": "Lord Protector"}, {"name": "Huntingdon, England", "role": "Birthplace"}, {"name": "Drogheda, Ireland", "role": "Controversial siege"}]
        }
    },
    {
        "slug": "gottfried-wilhelm-leibniz",
        "name": "Gottfried Wilhelm Leibniz",
        "label": "Person",
        "callNumber": "210.gottfried-wilhelm-leibniz",
        "era": "Early Modern",
        "eraSlug": "early-modern",
        "eraDivision": "Early Modern",
        "eraDivisionCode": "940",
        "region": "Europe",
        "continent": "Europe",
        "status": "Published",
        "born": "1646-07-01",
        "died": "1716-11-14",
        "wikidataQid": "Q9047",
        "wikipediaUrl": "https://en.wikipedia.org/wiki/Gottfried_Wilhelm_Leibniz",
        "importanceScore": 9,
        "subjectHeadings": ["People \u2014 Philosophers \u2014 Europe \u2014 Early Modern"],
        "subjects": ["Calculus", "Rationalism", "Binary System", "Monadology", "Germany", "Mathematics", "Philosophy", "Logic"],
        "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS", "COMPARATIVE_CIVILIZATIONS"],
        "summary": "Gottfried Wilhelm Leibniz (1646\u20131716) was a German polymath who independently invented calculus, developed the binary number system that underpins all modern computing, and constructed a philosophical system of extraordinary ambition. He is considered, alongside Newton, the most important mathematician of the 17th century and one of history's greatest universal geniuses.\n\nLeibniz's calculus notation\u2014the integral sign \u222b and the d/dx differential\u2014proved superior to Newton's and is the standard used by mathematicians today. The bitter priority dispute between Leibniz and Newton over calculus invention became the most famous controversy in the history of science.\n\nHis philosophical system centred on 'monads'\u2014simple, indivisible substances that constitute reality\u2014led him to declare this 'the best of all possible worlds' (satirised by Voltaire in 'Candide'). His binary arithmetic (1679), using only 0 and 1, was a purely theoretical curiosity that became the foundation of digital computing 250 years later.\n\nLeibniz also invented a mechanical calculator, founded the Berlin Academy of Sciences, and corresponded with over 1,100 people across Europe and China. He died neglected in Hanover, with only his secretary attending the funeral. As Denis Diderot observed: 'When one compares one's own small talents with those of Leibniz, one is tempted to throw away one's books and go die quietly.'",
        "detailsJson": {
            "causes": ["17th-century European scientific revolution and mathematical advances", "German university tradition in philosophy and logic", "Diplomatic career providing access to Europe's intellectual networks"],
            "effects": ["Calculus notation became universal mathematical standard", "Binary number system became foundation of all digital computing", "Monadology influenced German Idealism and modern logic"],
            "relationships": [
                {"sourceSlug": "gottfried-wilhelm-leibniz", "sourceName": "Gottfried Wilhelm Leibniz", "verb": "CREATES", "targetSlug": "calculus", "targetName": "Calculus", "context": "Independently invented calculus c. 1675; his notation became standard"},
                {"sourceSlug": "isaac-newton", "sourceName": "Isaac Newton", "verb": "COLLABORATES_WITH", "targetSlug": "gottfried-wilhelm-leibniz", "targetName": "Gottfried Wilhelm Leibniz", "context": "Calculus priority dispute became most famous scientific controversy"},
                {"sourceSlug": "gottfried-wilhelm-leibniz", "sourceName": "Gottfried Wilhelm Leibniz", "verb": "INFLUENCES", "targetSlug": "immanuel-kant", "targetName": "Immanuel Kant", "context": "Leibnizian rationalism shaped the tradition Kant synthesised"},
                {"sourceSlug": "blaise-pascal", "sourceName": "Blaise Pascal", "verb": "INFLUENCES", "targetSlug": "gottfried-wilhelm-leibniz", "targetName": "Gottfried Wilhelm Leibniz", "context": "Pascal's calculator inspired Leibniz's mechanical computing machine"},
                {"sourceSlug": "gottfried-wilhelm-leibniz", "sourceName": "Gottfried Wilhelm Leibniz", "verb": "OCCURS_IN", "targetSlug": "hanover", "targetName": "Hanover", "context": "Served as court advisor in Hanover 1676-1716"}
            ],
            "places": [{"name": "Hanover, Germany", "role": "Court advisor and death"}, {"name": "Leipzig, Germany", "role": "Birthplace"}, {"name": "Paris, France", "role": "Mathematical breakthrough period"}]
        }
    },
    {
        "slug": "alfred-hitchcock",
        "name": "Alfred Hitchcock",
        "label": "Person",
        "callNumber": "260.alfred-hitchcock",
        "era": "Contemporary",
        "eraSlug": "contemporary",
        "eraDivision": "Contemporary",
        "eraDivisionCode": "960",
        "region": "Europe",
        "continent": "Europe",
        "status": "Published",
        "born": "1899-08-13",
        "died": "1980-04-29",
        "wikidataQid": "Q7374",
        "wikipediaUrl": "https://en.wikipedia.org/wiki/Alfred_Hitchcock",
        "importanceScore": 8,
        "subjectHeadings": ["People \u2014 Artists & Creators \u2014 Europe \u2014 Contemporary"],
        "subjects": ["Cinema", "Suspense", "Film Direction", "Thriller", "England", "Hollywood", "Visual Storytelling", "Psycho"],
        "frameworks": ["CULTURAL_TRANSMISSION", "PSYCHOLOGICAL_ANALYSIS", "STRUCTURAL_ANALYSIS"],
        "summary": "Sir Alfred Joseph Hitchcock (1899\u20131980) was an English film director and producer who is widely regarded as the 'Master of Suspense' and one of the most influential filmmakers in cinema history. His career spanned six decades, 53 feature films, and both the British and American film industries, producing masterworks that defined the thriller genre.\n\nHitchcock pioneered visual storytelling techniques\u2014the tracking shot, subjective camera, montage editing, and the 'MacGuffin' plot device\u2014that are now fundamental to cinematic grammar. His British films, including 'The 39 Steps' (1935) and 'The Lady Vanishes' (1938), established his reputation before he moved to Hollywood in 1939.\n\nHis American masterpieces form the greatest sustained run of any director: 'Rear Window' (1954), 'Vertigo' (1958), 'North by Northwest' (1959), 'Psycho' (1960), and 'The Birds' (1963). 'Psycho's shower scene\u201478 camera setups for 45 seconds of screen time\u2014is the most analysed sequence in film history. 'Vertigo' was voted the greatest film ever made in the 2012 Sight & Sound poll.\n\nDespite five Academy Award nominations for Best Director, Hitchcock never won\u2014cinema's most famous oversight. His cameo appearances in his own films, his droll television introductions, and his rotund silhouette made him the most recognisable director in the world. As Fran\u00e7ois Truffaut declared: 'He is the only filmmaker whose name alone can sell a movie.'",
        "detailsJson": {
            "causes": ["German Expressionist cinema (Murnau, Lang) influencing visual style", "British music hall tradition shaping dark comic sensibility", "Hollywood studio system providing resources for ambitious productions"],
            "effects": ["Defined the thriller genre and visual language of suspense cinema", "Pioneered techniques (tracking shot, subjective camera) now standard in filmmaking", "Influenced Truffaut, De Palma, Spielberg, and every subsequent thriller director"],
            "relationships": [
                {"sourceSlug": "alfred-hitchcock", "sourceName": "Alfred Hitchcock", "verb": "CREATES", "targetSlug": "psycho-film", "targetName": "Psycho", "context": "1960 film revolutionised horror; shower scene is most analysed in cinema"},
                {"sourceSlug": "alfred-hitchcock", "sourceName": "Alfred Hitchcock", "verb": "INFLUENCES", "targetSlug": "steven-spielberg", "targetName": "Steven Spielberg", "context": "Hitchcock's suspense techniques and visual storytelling shaped Spielberg's cinema"},
                {"sourceSlug": "alfred-hitchcock", "sourceName": "Alfred Hitchcock", "verb": "OCCURS_IN", "targetSlug": "hollywood", "targetName": "Hollywood", "context": "Moved to Hollywood 1939; produced his greatest films there over four decades"},
                {"sourceSlug": "alfred-hitchcock", "sourceName": "Alfred Hitchcock", "verb": "CREATES", "targetSlug": "vertigo-film", "targetName": "Vertigo", "context": "1958 film voted greatest film ever made (Sight & Sound 2012)"},
                {"sourceSlug": "charlie-chaplin", "sourceName": "Charlie Chaplin", "verb": "INFLUENCES", "targetSlug": "alfred-hitchcock", "targetName": "Alfred Hitchcock", "context": "Both transformed cinema from entertainment to art; Chaplin inspired visual comedy elements"}
            ],
            "places": [{"name": "Hollywood, Los Angeles", "role": "Career from 1939"}, {"name": "Leytonstone, London", "role": "Birthplace"}, {"name": "Bel Air, Los Angeles", "role": "Home and death"}]
        }
    },
    {
        "slug": "gabriel-garcia-marquez",
        "name": "Gabriel Garc\u00eda M\u00e1rquez",
        "label": "Person",
        "callNumber": "261.gabriel-garcia-marquez",
        "era": "Contemporary",
        "eraSlug": "contemporary",
        "eraDivision": "Contemporary",
        "eraDivisionCode": "960",
        "region": "South America",
        "continent": "South America",
        "status": "Published",
        "born": "1927-03-06",
        "died": "2014-04-17",
        "wikidataQid": "Q5878",
        "wikipediaUrl": "https://en.wikipedia.org/wiki/Gabriel_Garc%C3%ADa_M%C3%A1rquez",
        "importanceScore": 8,
        "subjectHeadings": ["People \u2014 Authors & Writers \u2014 South America \u2014 Contemporary"],
        "subjects": ["Magical Realism", "Latin American Literature", "Nobel Prize", "One Hundred Years of Solitude", "Colombia", "Journalism", "Boom Literature", "Political Engagement"],
        "frameworks": ["CULTURAL_TRANSMISSION", "CAUSE_AND_EFFECT", "WORLD_SYSTEMS"],
        "summary": "Gabriel Garc\u00eda M\u00e1rquez (1927\u20132014) was a Colombian novelist, short-story writer, and journalist whose masterpiece 'One Hundred Years of Solitude' (1967) is the most translated and read novel in Spanish since 'Don Quixote.' He won the Nobel Prize in Literature in 1982 'for his novels and short stories, in which the fantastic and the realistic are combined in a richly composed world of imagination.'\n\nBorn in Aracataca, Colombia\u2014the model for the fictional Macondo\u2014Garc\u00eda M\u00e1rquez was raised by his maternal grandparents whose storytelling style blended the miraculous and the mundane. As a journalist, he covered politics across Latin America before publishing his early novels.\n\n'One Hundred Years of Solitude' traces seven generations of the Buend\u00eda family in Macondo, weaving Colombian history with levitations, rainstorms of flowers, and prophetic manuscripts. It sold over 50 million copies, launched the Latin American literary 'Boom,' and made magical realism a global literary movement.\n\nHis other masterworks\u2014'Love in the Time of Cholera' (1985), 'Chronicle of a Death Foretold' (1981), 'The Autumn of the Patriarch' (1975)\u2014confirmed his genius. A close friend of Fidel Castro, Garc\u00eda M\u00e1rquez used his fame to advocate for peace in Colombia and Latin America. He died in Mexico City in 2014, mourned as the greatest Latin American writer of the 20th century.",
        "detailsJson": {
            "causes": ["Colombian political violence ('La Violencia') shaping narrative material", "Grandmother's oral storytelling tradition blending reality and myth", "Kafka, Faulkner, and Borges providing literary models"],
            "effects": ["Made magical realism a global literary movement", "Latin American 'Boom' brought continent's literature to world audience", "Nobel Prize 1982; 'One Hundred Years' sold 50+ million copies"],
            "relationships": [
                {"sourceSlug": "gabriel-garcia-marquez", "sourceName": "Gabriel Garc\u00eda M\u00e1rquez", "verb": "CREATES", "targetSlug": "one-hundred-years-of-solitude", "targetName": "One Hundred Years of Solitude", "context": "Published 1967; most translated Spanish novel since Don Quixote"},
                {"sourceSlug": "gabriel-garcia-marquez", "sourceName": "Gabriel Garc\u00eda M\u00e1rquez", "verb": "COLLABORATES_WITH", "targetSlug": "fidel-castro", "targetName": "Fidel Castro", "context": "Close personal friendship; used fame to advocate for Latin American peace"},
                {"sourceSlug": "franz-kafka", "sourceName": "Franz Kafka", "verb": "INFLUENCES", "targetSlug": "gabriel-garcia-marquez", "targetName": "Gabriel Garc\u00eda M\u00e1rquez", "context": "Kafka's 'Metamorphosis' showed Garc\u00eda M\u00e1rquez that 'impossible things could be written'"},
                {"sourceSlug": "gabriel-garcia-marquez", "sourceName": "Gabriel Garc\u00eda M\u00e1rquez", "verb": "OCCURS_IN", "targetSlug": "bogota", "targetName": "Bogot\u00e1", "context": "Colombian political life and journalism based in Bogot\u00e1"},
                {"sourceSlug": "miguel-de-cervantes", "sourceName": "Miguel de Cervantes", "verb": "INFLUENCES", "targetSlug": "gabriel-garcia-marquez", "targetName": "Gabriel Garc\u00eda M\u00e1rquez", "context": "Don Quixote's blending of reality and imagination prefigured magical realism"}
            ],
            "places": [{"name": "Aracataca, Colombia", "role": "Birthplace and model for Macondo"}, {"name": "Mexico City, Mexico", "role": "Wrote masterpiece and died"}, {"name": "Bogot\u00e1, Colombia", "role": "Journalism career"}]
        }
    },
    {
        "slug": "werner-heisenberg",
        "name": "Werner Heisenberg",
        "label": "Person",
        "callNumber": "240.werner-heisenberg",
        "era": "Contemporary",
        "eraSlug": "contemporary",
        "eraDivision": "Contemporary",
        "eraDivisionCode": "960",
        "region": "Europe",
        "continent": "Europe",
        "status": "Published",
        "born": "1901-12-05",
        "died": "1976-02-01",
        "wikidataQid": "Q40904",
        "wikipediaUrl": "https://en.wikipedia.org/wiki/Werner_Heisenberg",
        "importanceScore": 8,
        "subjectHeadings": ["People \u2014 Scientists & Researchers \u2014 Europe \u2014 Contemporary"],
        "subjects": ["Quantum Mechanics", "Uncertainty Principle", "Matrix Mechanics", "Nobel Prize", "Germany", "Nuclear Physics", "Copenhagen Interpretation", "Philosophy of Science"],
        "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS", "COMPARATIVE_CIVILIZATIONS"],
        "summary": "Werner Karl Heisenberg (1901\u20131976) was a German theoretical physicist who created matrix mechanics\u2014the first complete mathematical formulation of quantum mechanics\u2014and discovered the uncertainty principle, one of the most profound insights in the history of science. He received the Nobel Prize in Physics in 1932 at age 31.\n\nHeisenberg's uncertainty principle (1927) demonstrated that the position and momentum of a particle cannot both be precisely known simultaneously\u2014not because of measurement limitations, but as a fundamental property of nature itself. This shattered the deterministic worldview of classical physics and reshaped philosophy, epistemology, and culture.\n\nWorking under Niels Bohr in Copenhagen, Heisenberg helped develop the Copenhagen interpretation of quantum mechanics, which remains the standard framework taught in physics. His matrix mechanics (1925), independently equivalent to Schr\u00f6dinger's wave mechanics, demonstrated that quantum phenomena could be described entirely through mathematical abstractions without classical analogies.\n\nHeisenberg's wartime role as head of Germany's nuclear energy project remains deeply controversial. His 1941 visit to Bohr in occupied Copenhagen\u2014dramatised in Michael Frayn's play 'Copenhagen'\u2014is one of science history's great mysteries. Whether he deliberately slowed the Nazi bomb programme or simply failed remains debated to this day.",
        "detailsJson": {
            "causes": ["Bohr's atomic model requiring mathematical formalisation", "Crisis in classical physics over wave-particle duality", "Copenhagen Institute's collaborative research environment"],
            "effects": ["Uncertainty principle overthrew classical determinism forever", "Matrix mechanics provided first rigorous formulation of quantum theory", "Nobel Prize 1932; profoundly influenced philosophy and epistemology"],
            "relationships": [
                {"sourceSlug": "niels-bohr", "sourceName": "Niels Bohr", "verb": "INFLUENCES", "targetSlug": "werner-heisenberg", "targetName": "Werner Heisenberg", "context": "Heisenberg developed matrix mechanics under Bohr's mentorship in Copenhagen"},
                {"sourceSlug": "werner-heisenberg", "sourceName": "Werner Heisenberg", "verb": "CREATES", "targetSlug": "uncertainty-principle", "targetName": "Uncertainty Principle", "context": "Published 1927; fundamental limit on simultaneous measurement precision"},
                {"sourceSlug": "max-planck", "sourceName": "Max Planck", "verb": "INFLUENCES", "targetSlug": "werner-heisenberg", "targetName": "Werner Heisenberg", "context": "Planck's quantisation was the foundation Heisenberg formalised mathematically"},
                {"sourceSlug": "werner-heisenberg", "sourceName": "Werner Heisenberg", "verb": "OCCURS_IN", "targetSlug": "copenhagen", "targetName": "Copenhagen", "context": "Developed matrix mechanics and Copenhagen interpretation at Bohr's institute"},
                {"sourceSlug": "werner-heisenberg", "sourceName": "Werner Heisenberg", "verb": "PARTICIPATES_IN", "targetSlug": "german-nuclear-programme", "targetName": "German Nuclear Programme", "context": "Led Germany's wartime nuclear energy project; controversial wartime role"}
            ],
            "places": [{"name": "Copenhagen, Denmark", "role": "Research breakthrough"}, {"name": "W\u00fcrzburg, Germany", "role": "Birthplace"}, {"name": "Munich, Germany", "role": "Education and later career"}]
        }
    },
    {
        "slug": "erwin-schrodinger",
        "name": "Erwin Schr\u00f6dinger",
        "label": "Person",
        "callNumber": "240.erwin-schrodinger",
        "era": "Contemporary",
        "eraSlug": "contemporary",
        "eraDivision": "Contemporary",
        "eraDivisionCode": "960",
        "region": "Europe",
        "continent": "Europe",
        "status": "Published",
        "born": "1887-08-12",
        "died": "1961-01-04",
        "wikidataQid": "Q9130",
        "wikipediaUrl": "https://en.wikipedia.org/wiki/Erwin_Schr%C3%B6dinger",
        "importanceScore": 8,
        "subjectHeadings": ["People \u2014 Scientists & Researchers \u2014 Europe \u2014 Contemporary"],
        "subjects": ["Quantum Mechanics", "Wave Mechanics", "Schrodinger Equation", "Nobel Prize", "Austria", "Theoretical Physics", "Wave Function", "Cat Paradox"],
        "frameworks": ["CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS", "COMPARATIVE_CIVILIZATIONS"],
        "summary": "Erwin Rudolf Josef Alexander Schr\u00f6dinger (1887\u20131961) was an Austrian-Irish theoretical physicist who developed wave mechanics\u2014the mathematical framework that describes quantum systems through wave functions\u2014earning him the Nobel Prize in Physics in 1933 (shared with Paul Dirac). His equation is to quantum mechanics what Newton's laws are to classical mechanics.\n\nThe Schr\u00f6dinger equation (1926) describes how the quantum state of a physical system changes over time. It provided a more intuitive alternative to Heisenberg's matrix mechanics and proved mathematically equivalent to it. The wave function (\u03c8) it produces contains all knowable information about a quantum system.\n\nHis famous 1935 thought experiment\u2014'Schr\u00f6dinger's cat,' simultaneously alive and dead inside a sealed box\u2014was designed to expose what he saw as the absurdity of the Copenhagen interpretation. Instead, it became the most famous illustration of quantum superposition and entered popular culture as a symbol of quantum weirdness.\n\nFleeing Nazi Austria in 1938, Schr\u00f6dinger settled in Dublin, where he spent 17 productive years at the Institute for Advanced Studies. His 1944 book 'What Is Life?' anticipated the discovery of DNA by proposing that genetic information is stored in an 'aperiodic crystal'\u2014directly inspiring Watson, Crick, and Wilkins. He returned to Vienna in 1956 and died there in 1961.",
        "detailsJson": {
            "causes": ["De Broglie's wave-particle duality hypothesis providing theoretical trigger", "Bohr-Sommerfeld atomic models requiring mathematical refinement", "Viennese tradition of theoretical physics (Boltzmann, Mach)"],
            "effects": ["Schr\u00f6dinger equation became fundamental equation of quantum mechanics", "Cat thought experiment became defining metaphor for quantum superposition", "'What Is Life?' inspired Watson and Crick's discovery of DNA structure"],
            "relationships": [
                {"sourceSlug": "erwin-schrodinger", "sourceName": "Erwin Schr\u00f6dinger", "verb": "CREATES", "targetSlug": "schrodinger-equation", "targetName": "Schr\u00f6dinger Equation", "context": "Published 1926; fundamental equation governing quantum mechanical systems"},
                {"sourceSlug": "niels-bohr", "sourceName": "Niels Bohr", "verb": "INFLUENCES", "targetSlug": "erwin-schrodinger", "targetName": "Erwin Schr\u00f6dinger", "context": "Bohr's atomic model inspired Schr\u00f6dinger's wave mechanical reformulation"},
                {"sourceSlug": "erwin-schrodinger", "sourceName": "Erwin Schr\u00f6dinger", "verb": "INFLUENCES", "targetSlug": "james-watson", "targetName": "James Watson", "context": "'What Is Life?' directly inspired Watson and Crick to pursue DNA structure"},
                {"sourceSlug": "erwin-schrodinger", "sourceName": "Erwin Schr\u00f6dinger", "verb": "OCCURS_IN", "targetSlug": "dublin", "targetName": "Dublin", "context": "Institute for Advanced Studies, Dublin 1939-1956"},
                {"sourceSlug": "max-planck", "sourceName": "Max Planck", "verb": "INFLUENCES", "targetSlug": "erwin-schrodinger", "targetName": "Erwin Schr\u00f6dinger", "context": "Planck's quantum theory provided the foundation for wave mechanics"}
            ],
            "places": [{"name": "Vienna, Austria", "role": "Birthplace and death"}, {"name": "Dublin, Ireland", "role": "17 years at Institute for Advanced Studies"}, {"name": "Zurich, Switzerland", "role": "Developed wave equation at University of Zurich"}]
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
    """Create or update entity in Appwrite. Handles hash-based, slug-based, and query-based lookups."""
    data = entity_to_appwrite(e)
    doc_id = slug_to_id(slug)

    # Try hash-based ID first
    existing = get_doc(doc_id)
    if existing:
        return update_doc(doc_id, data)

    # Try slug-based ID
    existing = get_doc(slug)
    if existing:
        return update_doc(slug, data)

    # Try query-based lookup (for legacy IDs like "ren_-descartes")
    found_id = find_doc_by_slug(slug)
    if found_id:
        return update_doc(found_id, data)

    # Create new
    ok = create_doc(doc_id, data)
    if not ok:
        # If hash collision, try slug as ID
        ok = create_doc(slug, data)
    return ok


# ═══ RUN ═══

print("=" * 60)
print("BATCH 8: 14 PARTIAL/STUB Enrichments + 6 New Entities")
print("=" * 60)

# Part 1: Enrich
print("\n--- PART 1: Enriching 14 PARTIAL/STUB entities ---")
enriched = 0
for slug, data in ENRICHMENTS.items():
    if enrich_entity(slug, data):
        print(f"  ENRICHED {slug}")
        enriched += 1
    else:
        print(f"  NOT FOUND {slug}")

# Part 2: Create new entities
print(f"\n--- PART 2: Creating 6 new entities ---")
created = 0
for entity_data in NEW_ENTITIES:
    slug = entity_data["slug"]
    create_new_entity(entity_data)
    print(f"  CREATED {slug}")
    created += 1

print(f"\nLocal: {enriched} enriched, {created} new entities created")

# Part 3: Sync all to Appwrite
print("\n--- PART 3: Syncing to Appwrite ---")

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
print(f"BATCH 8 COMPLETE: {enriched} enriched + {created} created = {enriched + created} total")
print(f"{'=' * 60}")
