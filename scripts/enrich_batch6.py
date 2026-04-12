#!/usr/bin/env python3
"""
Batch 6: Enrich 13 PARTIAL/STUB high-importance entities.
Also create 5 new notable entities missing from the dataset.
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

# ═══ ENRICHMENT DATA ═══

ENRICHMENTS = {
    "caravaggio": {
        "summary": "Michelangelo Merisi da Caravaggio (1571\u20131610) was an Italian painter whose revolutionary use of chiaroscuro\u2014dramatic contrasts of light and shadow\u2014transformed European art. Working in Rome, Naples, Malta, and Sicily, he painted directly from life onto canvas without preliminary drawings, a radical departure from Renaissance studio practice.\n\nCaravaggio's masterworks include 'The Calling of Saint Matthew' (1599\u20131600), 'Judith Beheading Holofernes' (c. 1598), and 'The Entombment of Christ' (1603\u20131604). His unflinching realism depicted saints as ordinary people with dirty feet and weathered faces, shocking patrons accustomed to idealized religious imagery.\n\nHis violent temperament led to a murder conviction in Rome in 1606, forcing him into exile. He spent his final years fleeing justice while producing some of his most powerful works. He died at age 38 under mysterious circumstances on a beach at Porto Ercole.\n\nCaravaggio's influence spawned an entire movement\u2014Caravaggism\u2014that spread across Europe through followers like Artemisia Gentileschi, Georges de La Tour, and Jusepe de Ribera. 'What he did was to make the painting itself the event,' as critic Robert Hughes noted.",
        "causes": ["Renaissance artistic tradition and Venetian colorism", "Counter-Reformation demand for emotionally accessible religious art", "Roman patronage networks of Cardinals del Monte and Borghese"],
        "effects": ["Founded Caravaggism movement across Europe", "Transformed Baroque painting with tenebrism technique", "Influenced Rembrandt, Velazquez, and virtually every subsequent realist painter"],
        "relationships": [
            {"sourceSlug": "caravaggio", "sourceName": "Caravaggio", "verb": "INFLUENCES", "targetSlug": "rembrandt", "targetName": "Rembrandt", "context": "Chiaroscuro technique transmitted through Caravaggist intermediaries"},
            {"sourceSlug": "caravaggio", "sourceName": "Caravaggio", "verb": "CREATES", "targetSlug": "counter-reformation", "targetName": "Counter-Reformation", "context": "Painted emotionally powerful altarpieces for Roman churches"},
            {"sourceSlug": "caravaggio", "sourceName": "Caravaggio", "verb": "TRANSFORMS", "targetSlug": "baroque-art", "targetName": "Baroque Art", "context": "Revolutionary tenebrism technique defined Baroque visual language"},
            {"sourceSlug": "michelangelo", "sourceName": "Michelangelo", "verb": "INFLUENCES", "targetSlug": "caravaggio", "targetName": "Caravaggio", "context": "Built on Michelangelo's dramatic figural composition"},
            {"sourceSlug": "caravaggio", "sourceName": "Caravaggio", "verb": "OCCURS_IN", "targetSlug": "rome", "targetName": "Rome", "context": "Primary career in Rome 1592-1606"}
        ],
        "places": [{"name": "Rome, Italy", "role": "Primary career"}, {"name": "Naples, Italy", "role": "Exile period"}, {"name": "Malta", "role": "Knight of Malta"}],
        "subjects": ["Baroque Art", "Chiaroscuro", "Counter-Reformation", "Italian Painting", "Tenebrism", "Rome", "Art History", "Italy"],
        "frameworks": ["CULTURAL_TRANSMISSION", "CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"]
    },
    "vincent-van-gogh": {
        "summary": "Vincent Willem van Gogh (1853\u20131890) was a Dutch Post-Impressionist painter who produced approximately 2,100 artworks in a decade\u2014including 860 oil paintings\u2014yet sold only one during his lifetime. His bold colors, expressive brushwork, and emotional intensity made him one of the most influential figures in Western art history.\n\nVan Gogh's early works depicted peasant life in dark earth tones, culminating in 'The Potato Eaters' (1885). After moving to Paris in 1886, he discovered Impressionism and Japanese woodblock prints, transforming his palette. His Arles period (1888\u20131889) produced 'Sunflowers,' 'The Night Caf\u00e9,' and 'Starry Night Over the Rh\u00f4ne.'\n\nHis struggles with mental illness led to the infamous ear-severing incident in December 1888 and voluntary admission to the Saint-R\u00e9my asylum, where he painted 'The Starry Night' (1889). He shot himself on July 27, 1890, dying two days later at age 37.\n\nVan Gogh's letters to his brother Theo comprise one of the most significant primary sources in art history\u2014903 surviving letters that document his artistic philosophy, daily struggles, and visionary ambition. His work influenced Fauvism, Expressionism, and virtually every modern art movement.",
        "causes": ["Dutch Golden Age artistic heritage and Rembrandt's influence", "Impressionist and Neo-Impressionist color theory exposure in Paris", "Japanese ukiyo-e woodblock print aesthetics"],
        "effects": ["Pioneered Expressionist approach to color and emotion", "Influenced Fauvism, Die Brucke, and Abstract Expressionism", "Became archetypal figure of the misunderstood artistic genius"],
        "relationships": [
            {"sourceSlug": "vincent-van-gogh", "sourceName": "Vincent van Gogh", "verb": "INFLUENCES", "targetSlug": "pablo-picasso", "targetName": "Pablo Picasso", "context": "Expressive color and emotional brushwork influenced early Picasso"},
            {"sourceSlug": "vincent-van-gogh", "sourceName": "Vincent van Gogh", "verb": "STUDIES_UNDER", "targetSlug": "rembrandt", "targetName": "Rembrandt", "context": "Studied and copied Rembrandt extensively, admired his treatment of light"},
            {"sourceSlug": "vincent-van-gogh", "sourceName": "Vincent van Gogh", "verb": "COLLABORATES_WITH", "targetSlug": "paul-gauguin", "targetName": "Paul Gauguin", "context": "Shared the Yellow House in Arles, autumn 1888"},
            {"sourceSlug": "vincent-van-gogh", "sourceName": "Vincent van Gogh", "verb": "OCCURS_IN", "targetSlug": "arles", "targetName": "Arles", "context": "Most prolific period: February 1888 to May 1889"},
            {"sourceSlug": "vincent-van-gogh", "sourceName": "Vincent van Gogh", "verb": "CREATES", "targetSlug": "starry-night", "targetName": "The Starry Night", "context": "Painted June 1889 at Saint-Remy asylum"}
        ],
        "places": [{"name": "Arles, France", "role": "Most prolific period"}, {"name": "Paris, France", "role": "Impressionist exposure"}, {"name": "Auvers-sur-Oise, France", "role": "Final months"}],
        "subjects": ["Post-Impressionism", "Dutch Art", "Mental Health", "Expressionism", "France", "Netherlands", "Art History", "Letters"],
        "frameworks": ["CULTURAL_TRANSMISSION", "PSYCHOLOGICAL_ANALYSIS", "CAUSE_AND_EFFECT"]
    },
    "johann-sebastian-bach": {
        "summary": "Johann Sebastian Bach (1685\u20131750) was a German composer and musician of the Baroque era, widely regarded as one of the greatest composers in Western music history. Born into a dynasty of musicians in Eisenach, Thuringia, he mastered organ, harpsichord, and violin while absorbing Italian, French, and German musical traditions.\n\nBach's output spans every major genre except opera: over 1,100 compositions including the Brandenburg Concertos (1721), The Well-Tempered Clavier (1722/1742), the Mass in B minor, and the St. Matthew Passion (1727). As Thomaskantor in Leipzig from 1723 until his death, he composed a sacred cantata for nearly every Sunday\u2014over 200 surviving.\n\nLargely forgotten after his death, Bach was rediscovered in the early 19th century when Felix Mendelssohn revived the St. Matthew Passion in 1829. This sparked a Bach renaissance that revealed him as the supreme master of counterpoint, fugue, and harmonic logic.\n\nAs Beethoven declared: 'His name ought not to be Bach (brook) but Ocean, for the infinite and inexhaustible wealth of tone combinations.' Bach's grammar of harmony became the foundation upon which all subsequent Western music was built.",
        "causes": ["Thuringian musical dynasty tradition (7 generations of musicians)", "Lutheran church music tradition requiring weekly cantatas", "Italian concerto form and French dance suite influence"],
        "effects": ["Established counterpoint and fugue as pinnacle of Western music technique", "The Well-Tempered Clavier demonstrated equal temperament tuning", "Became foundational study for every subsequent Western composer"],
        "relationships": [
            {"sourceSlug": "johann-sebastian-bach", "sourceName": "Johann Sebastian Bach", "verb": "INFLUENCES", "targetSlug": "ludwig-van-beethoven", "targetName": "Ludwig van Beethoven", "context": "Beethoven studied Bach's Well-Tempered Clavier as foundational text"},
            {"sourceSlug": "johann-sebastian-bach", "sourceName": "Johann Sebastian Bach", "verb": "INFLUENCES", "targetSlug": "wolfgang-amadeus-mozart", "targetName": "Wolfgang Amadeus Mozart", "context": "Mozart studied Bach fugues in Vienna, incorporated contrapuntal techniques"},
            {"sourceSlug": "martin-luther", "sourceName": "Martin Luther", "verb": "INFLUENCES", "targetSlug": "johann-sebastian-bach", "targetName": "Johann Sebastian Bach", "context": "Lutheran chorale tradition provided the basis for Bach's sacred music"},
            {"sourceSlug": "johann-sebastian-bach", "sourceName": "Johann Sebastian Bach", "verb": "OCCURS_IN", "targetSlug": "leipzig", "targetName": "Leipzig", "context": "Thomaskantor 1723-1750, composed majority of mature works"},
            {"sourceSlug": "johann-sebastian-bach", "sourceName": "Johann Sebastian Bach", "verb": "CREATES", "targetSlug": "well-tempered-clavier", "targetName": "The Well-Tempered Clavier", "context": "Two books (1722, 1742) with 48 preludes and fugues in all major and minor keys"}
        ],
        "places": [{"name": "Leipzig, Germany", "role": "Thomaskantor"}, {"name": "Eisenach, Germany", "role": "Birthplace"}, {"name": "Weimar, Germany", "role": "Court organist"}],
        "subjects": ["Baroque Music", "Counterpoint", "Fugue", "Lutheran Music", "Germany", "Organ", "Classical Music", "Composition"],
        "frameworks": ["CULTURAL_TRANSMISSION", "STRUCTURAL_ANALYSIS", "CAUSE_AND_EFFECT"]
    },
    "charles-dickens": {
        "summary": "Charles John Huffam Dickens (1812\u20131870) was an English novelist and social critic who created some of the most memorable characters in Western literature. His works, including 'Oliver Twist' (1837\u201339), 'A Christmas Carol' (1843), 'David Copperfield' (1849\u201350), and 'Great Expectations' (1860\u201361), exposed the harsh conditions of Victorian England's industrial underclass.\n\nDickens's childhood trauma\u2014his father's imprisonment in the Marshalsea debtor's prison and his own forced labor at Warren's Blacking Factory at age 12\u2014fueled a lifelong crusade against poverty and institutional cruelty. His novels were published in serial instalments, making literature accessible to working-class readers for the first time.\n\nHis public readings drew enormous crowds across Britain and America. He championed reforms in education, sanitation, and labor laws, and his portrayal of workhouses in 'Oliver Twist' helped catalyze the repeal of the Poor Laws. At his death, he was Britain's most famous living person.\n\nAs Leo Tolstoy wrote: 'All his characters are my personal friends.' Dickens invented the modern Christmas celebration, popularised the novel as social commentary, and gave the English language phrases like 'Bah, humbug!' and 'It was the best of times, it was the worst of times.'",
        "causes": ["Childhood poverty and debtor's prison experience", "Industrial Revolution creating mass urban poverty in England", "Rise of serial fiction publishing and mass literacy"],
        "effects": ["Drove Victorian social reform through public awareness of poverty", "Democratized the novel via serial publication for working-class audiences", "Shaped modern Christmas celebrations through A Christmas Carol"],
        "relationships": [
            {"sourceSlug": "charles-dickens", "sourceName": "Charles Dickens", "verb": "INFLUENCES", "targetSlug": "leo-tolstoy", "targetName": "Leo Tolstoy", "context": "Tolstoy admired Dickens's social realism and character depth"},
            {"sourceSlug": "charles-dickens", "sourceName": "Charles Dickens", "verb": "CAUSES", "targetSlug": "industrial-revolution", "targetName": "Industrial Revolution", "context": "Exposed industrial poverty through fiction, driving reform legislation"},
            {"sourceSlug": "charles-dickens", "sourceName": "Charles Dickens", "verb": "OCCURS_IN", "targetSlug": "london", "targetName": "London", "context": "London was both his home and the setting for most of his novels"},
            {"sourceSlug": "charles-dickens", "sourceName": "Charles Dickens", "verb": "INFLUENCES", "targetSlug": "mark-twain", "targetName": "Mark Twain", "context": "Twain admired Dickens's satirical wit and social commentary"},
            {"sourceSlug": "charles-dickens", "sourceName": "Charles Dickens", "verb": "CREATES", "targetSlug": "oliver-twist", "targetName": "Oliver Twist", "context": "Published 1837-1839, exposed workhouse conditions"}
        ],
        "places": [{"name": "London, England", "role": "Lifelong home and literary setting"}, {"name": "Rochester, England", "role": "Childhood home"}, {"name": "Gad's Hill Place, Kent", "role": "Final residence"}],
        "subjects": ["Victorian Literature", "Social Reform", "Serial Fiction", "Industrial Revolution", "England", "Poverty", "Christmas", "Literary Criticism"],
        "frameworks": ["CAUSE_AND_EFFECT", "CULTURAL_TRANSMISSION", "WORLD_SYSTEMS"]
    },
    "giuseppe-garibaldi": {
        "summary": "Giuseppe Garibaldi (1807\u20131882) was an Italian general, patriot, and republican who played a central role in the unification of Italy. Known as the 'Hero of Two Worlds,' he fought for liberation movements in South America before leading the legendary Expedition of the Thousand that conquered the Kingdom of the Two Sicilies in 1860.\n\nBorn in Nice (then part of the Kingdom of Sardinia), Garibaldi joined Giuseppe Mazzini's Young Italy movement and was sentenced to death in absentia in 1834. He fled to South America, where he fought for the Riograndense Republic in Brazil and defended Montevideo against Argentine forces, earning international fame as a guerrilla commander.\n\nReturning to Italy in 1848, Garibaldi fought in the First Italian War of Independence and briefly led the Roman Republic's defense against French forces. His greatest triumph came in 1860 when his volunteer force of roughly 1,000 Redshirts sailed from Genoa, conquered Sicily and Naples, and handed the entire southern half of Italy to King Victor Emmanuel II.\n\nGaribaldi's selfless surrender of conquered territory to the Sardinian monarchy\u2014rather than claiming power for himself\u2014made him an icon of republican virtue. Abraham Lincoln offered him a Union command in the American Civil War, and he remains Italy's most beloved national hero.",
        "causes": ["Napoleonic legacy of Italian national consciousness", "Mazzini's Young Italy republican ideology", "South American guerrilla warfare experience"],
        "effects": ["United southern Italy with northern Kingdom of Sardinia", "Enabled proclamation of the Kingdom of Italy in 1861", "Became model for anticolonial liberation movements worldwide"],
        "relationships": [
            {"sourceSlug": "giuseppe-garibaldi", "sourceName": "Giuseppe Garibaldi", "verb": "CAUSES", "targetSlug": "italian-unification", "targetName": "Italian Unification", "context": "Expedition of the Thousand conquered southern Italy 1860"},
            {"sourceSlug": "giuseppe-garibaldi", "sourceName": "Giuseppe Garibaldi", "verb": "COLLABORATES_WITH", "targetSlug": "giuseppe-mazzini", "targetName": "Giuseppe Mazzini", "context": "Joined Mazzini's Young Italy movement in 1833"},
            {"sourceSlug": "napoleon-bonaparte", "sourceName": "Napoleon Bonaparte", "verb": "INFLUENCES", "targetSlug": "giuseppe-garibaldi", "targetName": "Giuseppe Garibaldi", "context": "Napoleonic campaigns awakened Italian national identity"},
            {"sourceSlug": "giuseppe-garibaldi", "sourceName": "Giuseppe Garibaldi", "verb": "OCCURS_IN", "targetSlug": "sicily", "targetName": "Sicily", "context": "Landed at Marsala with 1,000 Redshirts, May 1860"},
            {"sourceSlug": "giuseppe-garibaldi", "sourceName": "Giuseppe Garibaldi", "verb": "INFLUENCES", "targetSlug": "simon-bolivar", "targetName": "Simon Bolivar", "context": "Garibaldi's liberation campaigns inspired by Bolivar's precedent"}
        ],
        "places": [{"name": "Nice, France", "role": "Birthplace"}, {"name": "Sicily, Italy", "role": "Military campaign"}, {"name": "Montevideo, Uruguay", "role": "South American exile"}],
        "subjects": ["Italian Unification", "Risorgimento", "Guerrilla Warfare", "Republican Ideals", "Italy", "Nationalism", "Military History", "South America"],
        "frameworks": ["CAUSE_AND_EFFECT", "WORLD_SYSTEMS", "COMPARATIVE_CIVILIZATIONS"]
    },
    "harriet-tubman": {
        "summary": "Harriet Tubman (c. 1822\u20131913), born Araminta Ross, was an American abolitionist who escaped slavery in 1849 and subsequently made approximately 13 rescue missions via the Underground Railroad, personally guiding roughly 70 enslaved people to freedom. Slaveholders placed a $40,000 bounty on her head\u2014she was never caught and never lost a passenger.\n\nBorn into slavery in Dorchester County, Maryland, Tubman suffered a traumatic head injury as a teenager when an overseer struck her with a two-pound weight. The injury caused lifelong seizures, headaches, and vivid dreams she interpreted as divine visions that guided her escape routes.\n\nDuring the Civil War, Tubman served the Union Army as a scout, spy, and nurse. In June 1863, she became the first woman to lead an armed assault in American history when she guided the Combahee River Raid, liberating over 700 enslaved people in South Carolina.\n\nAfter the war, she established the Harriet Tubman Home for the Aged in Auburn, New York, and campaigned for women's suffrage alongside Susan B. Anthony. She was posthumously honored on the US $20 bill design. Frederick Douglass wrote to her: 'I know of no one who has willingly encountered more perils and hardships to serve our enslaved people.'",
        "causes": ["Brutal conditions of Maryland Eastern Shore slavery", "Underground Railroad support network across northern states", "Deep religious faith providing courage and determination"],
        "effects": ["Freed approximately 70 enslaved people via Underground Railroad", "First woman to lead armed military assault in US history", "Became iconic symbol of Black resistance and liberation"],
        "relationships": [
            {"sourceSlug": "harriet-tubman", "sourceName": "Harriet Tubman", "verb": "COLLABORATES_WITH", "targetSlug": "frederick-douglass", "targetName": "Frederick Douglass", "context": "Worked together in abolitionist movement, Douglass sheltered escaping slaves she led north"},
            {"sourceSlug": "harriet-tubman", "sourceName": "Harriet Tubman", "verb": "CAUSES", "targetSlug": "underground-railroad", "targetName": "Underground Railroad", "context": "Made 13 rescue missions, most famous conductor on the Railroad"},
            {"sourceSlug": "harriet-tubman", "sourceName": "Harriet Tubman", "verb": "PARTICIPATES_IN", "targetSlug": "american-civil-war", "targetName": "American Civil War", "context": "Union Army scout, spy, and nurse; led Combahee River Raid 1863"},
            {"sourceSlug": "harriet-tubman", "sourceName": "Harriet Tubman", "verb": "OCCURS_IN", "targetSlug": "maryland", "targetName": "Maryland", "context": "Born into slavery on Eastern Shore, escaped 1849"},
            {"sourceSlug": "harriet-tubman", "sourceName": "Harriet Tubman", "verb": "INFLUENCES", "targetSlug": "rosa-parks", "targetName": "Rosa Parks", "context": "Legacy of Black female resistance inspired Civil Rights Movement figures"}
        ],
        "places": [{"name": "Dorchester County, Maryland", "role": "Birthplace"}, {"name": "Auburn, New York", "role": "Post-war home"}, {"name": "Philadelphia, Pennsylvania", "role": "First stop after escape"}],
        "subjects": ["Abolition", "Underground Railroad", "American Civil War", "Slavery", "Women's Rights", "United States", "African American History", "Military History"],
        "frameworks": ["CAUSE_AND_EFFECT", "FEMINIST_PERSPECTIVE", "STRUCTURAL_ANALYSIS"]
    },
    "mother-teresa": {
        "summary": "Mother Teresa (1910\u20131997), born Anjez\u00eb Gonxhe Bojaxhiu in Skopje, Ottoman Empire (now North Macedonia), was an Albanian-Indian Catholic nun who founded the Missionaries of Charity in 1950. Her order grew to over 4,500 sisters operating 600 missions in 133 countries, serving the poorest of the poor\u2014the sick, dying, orphaned, and destitute.\n\nShe arrived in India at age 18, taught at St. Mary's School in Calcutta, and in 1946 experienced what she called a 'call within a call' to leave convent life and serve the slums. Her first mission opened in the Motijhil slum, where she established open-air schools and a hospice for the dying at Kalighat.\n\nMother Teresa received the Nobel Peace Prize in 1979 'for work undertaken in the struggle to overcome poverty and distress, which also constitute a threat to peace.' She used the $192,000 prize money to fund her missions. Her private letters, published posthumously, revealed decades of spiritual darkness\u2014a crisis of faith she carried silently while serving.\n\nCanoized as Saint Teresa of Calcutta in 2016, she remains one of the most recognized humanitarians of the 20th century. As she said: 'If you can't feed a hundred people, then feed just one.'",
        "causes": ["Albanian Catholic upbringing and missionary vocation", "Extreme poverty and disease in Calcutta slums", "Vatican II emphasis on engagement with the modern world"],
        "effects": ["Founded Missionaries of Charity serving 133 countries", "Won Nobel Peace Prize 1979 and became global symbol of charity", "Canonized as saint 2016, inspired millions in humanitarian service"],
        "relationships": [
            {"sourceSlug": "mother-teresa", "sourceName": "Mother Teresa", "verb": "OCCURS_IN", "targetSlug": "calcutta", "targetName": "Calcutta", "context": "Founded Missionaries of Charity in Calcutta 1950, served there until death"},
            {"sourceSlug": "mother-teresa", "sourceName": "Mother Teresa", "verb": "CREATES", "targetSlug": "missionaries-of-charity", "targetName": "Missionaries of Charity", "context": "Founded 1950 with 13 members, grew to 4,500+ sisters in 133 countries"},
            {"sourceSlug": "pope-john-paul-ii", "sourceName": "Pope John Paul II", "verb": "ENDORSES", "targetSlug": "mother-teresa", "targetName": "Mother Teresa", "context": "Beatified her in 2003, fast-tracked canonization process"},
            {"sourceSlug": "mother-teresa", "sourceName": "Mother Teresa", "verb": "INFLUENCES", "targetSlug": "mahatma-gandhi", "targetName": "Mahatma Gandhi", "context": "Shared commitment to serving India's poorest, mutual respect across Hindu-Christian divide"},
            {"sourceSlug": "mother-teresa", "sourceName": "Mother Teresa", "verb": "PARTICIPATES_IN", "targetSlug": "nobel-peace-prize", "targetName": "Nobel Peace Prize", "context": "Awarded 1979 for work overcoming poverty and distress"}
        ],
        "places": [{"name": "Calcutta, India", "role": "Life's work"}, {"name": "Skopje, North Macedonia", "role": "Birthplace"}, {"name": "Vatican City", "role": "Canonization"}],
        "subjects": ["Humanitarian Aid", "Catholic Church", "Poverty", "India", "Nobel Peace Prize", "Missionaries", "Charity", "Canonization"],
        "frameworks": ["CAUSE_AND_EFFECT", "RELIGIOUS_INTERPRETATION", "WORLD_SYSTEMS"]
    },
    "ludwig-van-beethoven": {
        "summary": "Ludwig van Beethoven (1770\u20131827) was a German composer and pianist whose works bridged the Classical and Romantic periods and remain among the most performed in the Western concert repertoire. Born in Bonn, he moved to Vienna at 21 to study with Haydn and never left, transforming the city into his creative home for 35 years.\n\nBeethoven's early works followed Classical conventions, but his 'Eroica' Symphony No. 3 (1804)\u2014originally dedicated to Napoleon before Beethoven famously scratched out the dedication\u2014marked a seismic shift in musical ambition and scale. His middle period produced the Fifth Symphony, the 'Emperor' Piano Concerto, and the opera 'Fidelio.'\n\nBy 1814, Beethoven was almost completely deaf, yet his late works\u2014the Ninth Symphony with its revolutionary choral finale (1824), the late string quartets, and the 'Hammerklavier' Sonata\u2014represent the pinnacle of Western music. He conducted the Ninth's premiere unable to hear the thunderous applause until a soloist turned him to face the audience.\n\nBeethoven expanded the symphony from entertainment to existential statement. His Ninth Symphony's 'Ode to Joy' became the anthem of the European Union. As Wagner wrote: 'Where Beethoven's Ninth ends, the world of music begins.'",
        "causes": ["Classical Viennese tradition of Haydn and Mozart", "French Revolutionary ideals of freedom and human dignity", "Progressive deafness forcing inward creative exploration"],
        "effects": ["Bridged Classical and Romantic musical eras", "Expanded the symphony into a vehicle for philosophical expression", "'Ode to Joy' adopted as European Union anthem"],
        "relationships": [
            {"sourceSlug": "ludwig-van-beethoven", "sourceName": "Ludwig van Beethoven", "verb": "STUDIES_UNDER", "targetSlug": "joseph-haydn", "targetName": "Joseph Haydn", "context": "Studied composition with Haydn in Vienna from 1792"},
            {"sourceSlug": "wolfgang-amadeus-mozart", "sourceName": "Wolfgang Amadeus Mozart", "verb": "INFLUENCES", "targetSlug": "ludwig-van-beethoven", "targetName": "Ludwig van Beethoven", "context": "Beethoven revered Mozart's piano concertos and operas as models"},
            {"sourceSlug": "ludwig-van-beethoven", "sourceName": "Ludwig van Beethoven", "verb": "INFLUENCES", "targetSlug": "johann-sebastian-bach", "targetName": "Johann Sebastian Bach", "context": "Raised on Bach's Well-Tempered Clavier, called Bach 'the original father of harmony'"},
            {"sourceSlug": "ludwig-van-beethoven", "sourceName": "Ludwig van Beethoven", "verb": "OCCURS_IN", "targetSlug": "vienna", "targetName": "Vienna", "context": "Lived and worked in Vienna 1792-1827"},
            {"sourceSlug": "ludwig-van-beethoven", "sourceName": "Ludwig van Beethoven", "verb": "CREATES", "targetSlug": "ninth-symphony", "targetName": "Symphony No. 9", "context": "Premiered 1824, first major symphony to include choral voices"}
        ],
        "places": [{"name": "Vienna, Austria", "role": "Lifelong creative home"}, {"name": "Bonn, Germany", "role": "Birthplace"}, {"name": "Heiligenstadt, Austria", "role": "Site of the Heiligenstadt Testament"}],
        "subjects": ["Classical Music", "Romantic Period", "Deafness", "Symphony", "Germany", "Austria", "Piano", "Composition"],
        "frameworks": ["CULTURAL_TRANSMISSION", "CAUSE_AND_EFFECT", "PSYCHOLOGICAL_ANALYSIS"]
    },
    "wolfgang-amadeus-mozart": {
        "summary": "Wolfgang Amadeus Mozart (1756\u20131791) was an Austrian composer who produced over 800 works in virtually every genre of his era\u2014symphonies, operas, concertos, chamber music, and sacred works\u2014in a career spanning just 30 years. A child prodigy who performed for European royalty at age 6, he remains the archetype of natural musical genius.\n\nBorn in Salzburg, Mozart was trained by his father Leopold and toured Europe as a child, performing for Empress Maria Theresa and King Louis XV. His mature works include the operas 'The Marriage of Figaro' (1786), 'Don Giovanni' (1787), and 'The Magic Flute' (1791), the last three symphonies (Nos. 39\u201341, composed in six weeks), and 27 piano concertos.\n\nMozart's final year produced some of his greatest music: 'The Magic Flute,' the Clarinet Concerto, and the unfinished Requiem. He died on December 5, 1791, at age 35, likely from acute rheumatic fever, and was buried in a common grave in Vienna's St. Marx Cemetery.\n\nHaydn told Leopold Mozart: 'Before God and as an honest man, I tell you that your son is the greatest composer known to me.' Mozart's effortless perfection of form, combined with profound emotional depth, established standards that every subsequent composer has measured themselves against.",
        "causes": ["Leopold Mozart's systematic musical education from age 3", "Exposure to Italian opera and German symphonic traditions during childhood tours", "Viennese Classical style established by Haydn"],
        "effects": ["Perfected the Classical piano concerto and opera buffa", "Established opera as a vehicle for psychological drama", "Set compositional standards that defined the Classical era"],
        "relationships": [
            {"sourceSlug": "wolfgang-amadeus-mozart", "sourceName": "Wolfgang Amadeus Mozart", "verb": "COLLABORATES_WITH", "targetSlug": "joseph-haydn", "targetName": "Joseph Haydn", "context": "Mutual admiration and influence; Mozart dedicated 6 string quartets to Haydn"},
            {"sourceSlug": "wolfgang-amadeus-mozart", "sourceName": "Wolfgang Amadeus Mozart", "verb": "INFLUENCES", "targetSlug": "ludwig-van-beethoven", "targetName": "Ludwig van Beethoven", "context": "Beethoven studied and idolized Mozart's piano concertos"},
            {"sourceSlug": "wolfgang-amadeus-mozart", "sourceName": "Wolfgang Amadeus Mozart", "verb": "OCCURS_IN", "targetSlug": "vienna", "targetName": "Vienna", "context": "Primary career in Vienna 1781-1791"},
            {"sourceSlug": "wolfgang-amadeus-mozart", "sourceName": "Wolfgang Amadeus Mozart", "verb": "CREATES", "targetSlug": "magic-flute", "targetName": "The Magic Flute", "context": "Final opera, premiered September 1791"},
            {"sourceSlug": "johann-sebastian-bach", "sourceName": "Johann Sebastian Bach", "verb": "INFLUENCES", "targetSlug": "wolfgang-amadeus-mozart", "targetName": "Wolfgang Amadeus Mozart", "context": "Mozart studied Bach fugues at Baron van Swieten's salon in Vienna"}
        ],
        "places": [{"name": "Vienna, Austria", "role": "Primary career"}, {"name": "Salzburg, Austria", "role": "Birthplace and early career"}, {"name": "Prague, Czech Republic", "role": "Don Giovanni premiere"}],
        "subjects": ["Classical Music", "Opera", "Child Prodigy", "Symphony", "Austria", "Piano Concerto", "Composition", "Sacred Music"],
        "frameworks": ["CULTURAL_TRANSMISSION", "CAUSE_AND_EFFECT", "STRUCTURAL_ANALYSIS"]
    },
    "leon-trotsky": {
        "summary": "Leon Trotsky (1879\u20131940), born Lev Davidovich Bronstein, was a Russian Marxist revolutionary who co-led the October Revolution of 1917 alongside Lenin and built the Red Army that won the Russian Civil War (1917\u20131922). As the revolution's chief military architect and its most brilliant theoretician, he shaped the early Soviet state before losing the power struggle to Stalin.\n\nTrotsky joined the Russian Social Democratic Labour Party as a teenager. During the 1905 Revolution, he led the St. Petersburg Soviet at age 26. After exile and journalism (he edited 'Pravda' in Vienna), he returned to Russia in May 1917 and organized the Military Revolutionary Committee that seized power on October 25.\n\nAs People's Commissar for Military Affairs, Trotsky transformed a ragtag militia into the 5-million-strong Red Army through a combination of ruthless discipline, inspirational oratory, and strategic brilliance. After Lenin's death in 1924, he lost the succession struggle to Stalin and was expelled from the USSR in 1929.\n\nLiving in exile in Turkey, France, Norway, and finally Mexico, Trotsky continued writing and organizing against Stalinism. On August 20, 1940, a Soviet agent assassinated him with an ice axe in his Mexico City study. His theory of 'permanent revolution' and critique of bureaucratic degeneration remain influential in left politics worldwide.",
        "causes": ["Russian autocracy and industrial proletariat exploitation", "Marxist revolutionary theory and German Social Democratic models", "1905 Revolution as rehearsal for 1917"],
        "effects": ["Co-led October Revolution establishing Soviet state", "Built the Red Army that won the Russian Civil War", "Theory of permanent revolution influenced global left politics"],
        "relationships": [
            {"sourceSlug": "leon-trotsky", "sourceName": "Leon Trotsky", "verb": "COLLABORATES_WITH", "targetSlug": "vladimir-lenin", "targetName": "Vladimir Lenin", "context": "Co-led the October Revolution of 1917"},
            {"sourceSlug": "leon-trotsky", "sourceName": "Leon Trotsky", "verb": "PARTICIPATES_IN", "targetSlug": "russian-revolution", "targetName": "Russian Revolution", "context": "Organized the Military Revolutionary Committee that seized power"},
            {"sourceSlug": "leon-trotsky", "sourceName": "Leon Trotsky", "verb": "CREATES", "targetSlug": "red-army", "targetName": "Red Army", "context": "Built and commanded the Red Army during the Civil War 1918-1922"},
            {"sourceSlug": "karl-marx", "sourceName": "Karl Marx", "verb": "INFLUENCES", "targetSlug": "leon-trotsky", "targetName": "Leon Trotsky", "context": "Marxist theory underpinned Trotsky's revolutionary program"},
            {"sourceSlug": "leon-trotsky", "sourceName": "Leon Trotsky", "verb": "OCCURS_IN", "targetSlug": "moscow", "targetName": "Moscow", "context": "Soviet leadership 1917-1927, before exile"}
        ],
        "places": [{"name": "St. Petersburg, Russia", "role": "Led 1905 Soviet and 1917 Revolution"}, {"name": "Mexico City, Mexico", "role": "Final exile and assassination"}, {"name": "Moscow, Russia", "role": "Soviet government"}],
        "subjects": ["Russian Revolution", "Marxism", "Red Army", "Soviet Union", "Permanent Revolution", "Exile", "Assassination", "Cold War Origins"],
        "frameworks": ["CAUSE_AND_EFFECT", "WORLD_SYSTEMS", "MARXIST_ANALYSIS"]
    },
    "rabindranath-tagore": {
        "summary": "Rabindranath Tagore (1861\u20131941) was a Bengali polymath\u2014poet, novelist, musician, painter, and philosopher\u2014who became the first non-European to win the Nobel Prize in Literature (1913). His collection 'Gitanjali' (Song Offerings), which he translated into English prose, captivated W.B. Yeats and the Swedish Academy with its spiritual lyricism.\n\nBorn into the prominent Tagore family in Calcutta, he wrote his first poem at age eight and published prolifically in Bengali for six decades: over 2,200 songs (many now the national anthems of both India and Bangladesh), 50 collections of poetry, 13 novels, and hundreds of short stories. He composed the music for all his songs himself.\n\nTagore founded Visva-Bharati University at Santiniketan in 1921 as an experiment in open-air education that merged Eastern and Western learning traditions. He was knighted by the British in 1915 but renounced the honor in 1919 following the Jallianwala Bagh massacre, writing to the Viceroy: 'The time has come when badges of honour make our shame glaring.'\n\nHis influence on Bengali culture is immeasurable\u2014he reshaped its literature, music, and visual arts. Einstein visited him in 1930 for their famous dialogue on the nature of reality. Tagore remains the only person whose compositions serve as the national anthem of two sovereign nations.",
        "causes": ["Bengali Renaissance and Brahmo Samaj reform movement", "Tagore family's intellectual and artistic tradition", "Encounter with Western Romantic poetry and philosophy"],
        "effects": ["First non-European Nobel laureate in Literature, opened global literary canon", "National anthem composer for both India and Bangladesh", "Founded Visva-Bharati University merging Eastern-Western education"],
        "relationships": [
            {"sourceSlug": "rabindranath-tagore", "sourceName": "Rabindranath Tagore", "verb": "INFLUENCES", "targetSlug": "mahatma-gandhi", "targetName": "Mahatma Gandhi", "context": "Tagore titled Gandhi 'Mahatma'; they debated nationalism and education"},
            {"sourceSlug": "rabindranath-tagore", "sourceName": "Rabindranath Tagore", "verb": "CREATES", "targetSlug": "visva-bharati-university", "targetName": "Visva-Bharati University", "context": "Founded 1921 at Santiniketan as open-air experimental university"},
            {"sourceSlug": "rabindranath-tagore", "sourceName": "Rabindranath Tagore", "verb": "COLLABORATES_WITH", "targetSlug": "albert-einstein", "targetName": "Albert Einstein", "context": "Famous dialogue on nature of reality, Berlin 1930"},
            {"sourceSlug": "rabindranath-tagore", "sourceName": "Rabindranath Tagore", "verb": "OCCURS_IN", "targetSlug": "calcutta", "targetName": "Calcutta", "context": "Born, lived, and reshaped Bengali culture from Calcutta"},
            {"sourceSlug": "rabindranath-tagore", "sourceName": "Rabindranath Tagore", "verb": "PARTICIPATES_IN", "targetSlug": "bengali-renaissance", "targetName": "Bengali Renaissance", "context": "Central figure of the Bengali cultural renaissance movement"}
        ],
        "places": [{"name": "Calcutta, India", "role": "Birthplace and creative home"}, {"name": "Santiniketan, India", "role": "Founded Visva-Bharati University"}, {"name": "London, England", "role": "Gitanjali English translation published"}],
        "subjects": ["Bengali Literature", "Nobel Prize", "Indian Poetry", "Music Composition", "Education", "India", "Bangladesh", "Philosophy"],
        "frameworks": ["CULTURAL_TRANSMISSION", "COMPARATIVE_CIVILIZATIONS", "CAUSE_AND_EFFECT"]
    },
    "thomas-more": {
        "summary": "Sir Thomas More (1478\u20131535) was an English lawyer, statesman, and humanist philosopher who served as Lord Chancellor under Henry VIII before being executed for refusing to acknowledge the king as Supreme Head of the Church of England. His principled stand for papal authority over royal supremacy made him a Catholic martyr, canonized in 1935.\n\nMore's 'Utopia' (1516), written in Latin, invented the genre of utopian fiction and introduced the word 'utopia' into European languages. The work described an ideal island society with communal property, religious tolerance, and universal education\u2014a satirical mirror reflecting the injustices of Tudor England.\n\nAs Lord Chancellor from 1529, More vigorously prosecuted heretics and opposed the Protestant Reformation. When Henry VIII sought annulment of his marriage to Catherine of Aragon and broke with Rome, More resigned in 1532 and refused to swear the Oath of Supremacy. He was imprisoned in the Tower of London for 15 months.\n\nOn the scaffold, More declared himself 'the King's good servant, but God's first.' His friend Erasmus called him 'a man for all seasons.' Robert Bolt's 1960 play popularized this phrase and cemented More's legacy as a man of conscience who chose death over compromise.",
        "causes": ["English humanist education at Oxford and the Inns of Court", "Erasmus's influence and Northern Renaissance intellectual networks", "Henry VIII's break with Rome over marriage annulment"],
        "effects": ["Invented utopian literary genre with 'Utopia' (1516)", "Became Catholic martyr and symbol of conscience over political loyalty", "Canonized 1935 and named patron saint of statesmen and politicians"],
        "relationships": [
            {"sourceSlug": "thomas-more", "sourceName": "Thomas More", "verb": "COLLABORATES_WITH", "targetSlug": "erasmus", "targetName": "Erasmus", "context": "Close friends; Erasmus wrote 'In Praise of Folly' while staying at More's home"},
            {"sourceSlug": "henry-viii", "sourceName": "Henry VIII", "verb": "EXECUTES", "targetSlug": "thomas-more", "targetName": "Thomas More", "context": "Beheaded July 6, 1535 for refusing the Oath of Supremacy"},
            {"sourceSlug": "thomas-more", "sourceName": "Thomas More", "verb": "CREATES", "targetSlug": "utopia-more", "targetName": "Utopia", "context": "Published 1516, invented the utopian fiction genre"},
            {"sourceSlug": "thomas-more", "sourceName": "Thomas More", "verb": "OCCURS_IN", "targetSlug": "london", "targetName": "London", "context": "Served as Lord Chancellor, imprisoned and executed at Tower of London"},
            {"sourceSlug": "thomas-more", "sourceName": "Thomas More", "verb": "PARTICIPATES_IN", "targetSlug": "english-reformation", "targetName": "English Reformation", "context": "Opposed Henry VIII's break with Rome, prosecuted Protestant heretics"}
        ],
        "places": [{"name": "London, England", "role": "Career and execution"}, {"name": "Chelsea, England", "role": "Family home"}, {"name": "Tower of London", "role": "Imprisonment 1534-1535"}],
        "subjects": ["English Reformation", "Utopian Fiction", "Catholic Martyrdom", "Tudor England", "Humanism", "Henry VIII", "Canon Law", "England"],
        "frameworks": ["CAUSE_AND_EFFECT", "RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"]
    },
    "jan-hus": {
        "summary": "Jan Hus (c. 1372\u20131415) was a Czech theologian, philosopher, and rector of Charles University in Prague whose critique of Church corruption\u2014simony, papal authority, and clerical immorality\u2014anticipated the Protestant Reformation by a full century. His execution at the Council of Constance sparked the Hussite Wars and made him a symbol of Czech national identity.\n\nInfluenced by John Wycliffe's writings, Hus preached in Czech (not Latin) at the Bethlehem Chapel in Prague, attracting enormous crowds. He demanded that clergy live according to Scripture, argued that an immoral pope had no authority, and insisted on communion in both kinds (bread and wine) for laypeople\u2014a radical challenge to Catholic sacramental practice.\n\nSummoned to the Council of Constance under a safe-conduct guarantee from Emperor Sigismund, Hus was arrested, tried for heresy, and burned at the stake on July 6, 1415. His last words reportedly were: 'In 100 years, God will raise up a man whose calls for reform cannot be suppressed.' Martin Luther later said: 'We are all Hussites without knowing it.'\n\nHus's martyrdom ignited the Hussite Wars (1419\u20131434), in which his followers defeated five consecutive papal crusades. The Hussite movement established proto-Protestant communities that survived until the Reformation, most notably the Moravian Church.",
        "causes": ["Wycliffe's theological writings on papal authority and Scripture primacy", "Corruption in the Western Schism-era Catholic Church", "Czech national resentment of German ecclesiastical dominance in Bohemia"],
        "effects": ["Hussite Wars (1419-1434) defeated five papal crusades", "Anticipated Protestant Reformation doctrines by 100 years", "Became founding symbol of Czech national identity"],
        "relationships": [
            {"sourceSlug": "jan-hus", "sourceName": "Jan Hus", "verb": "INFLUENCES", "targetSlug": "martin-luther", "targetName": "Martin Luther", "context": "Luther identified with Hus's reform agenda: 'We are all Hussites'"},
            {"sourceSlug": "john-wycliffe", "sourceName": "John Wycliffe", "verb": "INFLUENCES", "targetSlug": "jan-hus", "targetName": "Jan Hus", "context": "Wycliffe's writings on Scripture and papal authority shaped Hus's theology"},
            {"sourceSlug": "jan-hus", "sourceName": "Jan Hus", "verb": "OCCURS_IN", "targetSlug": "prague", "targetName": "Prague", "context": "Preached at Bethlehem Chapel, served as rector of Charles University"},
            {"sourceSlug": "jan-hus", "sourceName": "Jan Hus", "verb": "CAUSES", "targetSlug": "hussite-wars", "targetName": "Hussite Wars", "context": "His execution sparked armed Hussite resistance 1419-1434"},
            {"sourceSlug": "jan-hus", "sourceName": "Jan Hus", "verb": "PARTICIPATES_IN", "targetSlug": "council-of-constance", "targetName": "Council of Constance", "context": "Tried and burned for heresy July 6, 1415"}
        ],
        "places": [{"name": "Prague, Czech Republic", "role": "Career and preaching"}, {"name": "Constance, Germany", "role": "Trial and execution"}, {"name": "Bethlehem Chapel, Prague", "role": "Czech-language preaching"}],
        "subjects": ["Pre-Reformation", "Czech History", "Heresy", "Church Reform", "Hussite Wars", "Czech Republic", "Martyrdom", "Theology"],
        "frameworks": ["CAUSE_AND_EFFECT", "RELIGIOUS_INTERPRETATION", "STRUCTURAL_ANALYSIS"]
    },
    "yuri-gagarin": {
        "summary": "Yuri Alekseyevich Gagarin (1934\u20131968) was a Soviet pilot and cosmonaut who became the first human being to journey into outer space on April 12, 1961. His single orbit of Earth aboard Vostok 1, lasting 108 minutes, marked humanity's entry into the Space Age and represented the greatest achievement of the Soviet space program.\n\nBorn in the village of Klushino, Smolensk Oblast, Gagarin survived the German occupation of World War II. He trained as a foundry worker and pilot before being selected from over 3,000 candidates for the first cosmonaut group in 1960. The selection committee noted his calm temperament, physical fitness, and working-class background\u2014ideal Soviet symbolism.\n\nVostok 1 launched from Baikonur Cosmodrome at 09:07 Moscow Time. Gagarin's famous exclamation 'Poyekhali!' ('Let's go!') became one of the most quoted phrases in Russian culture. The flight was entirely automated; Gagarin could only override controls with a sealed envelope code in case of emergency. He ejected at 7 km altitude and parachuted to Earth near Saratov.\n\nGagarin became a global celebrity, touring 30 countries. He died on March 27, 1968, in a routine training jet crash at age 34. His flight remains one of the defining moments of the 20th century and is celebrated annually as Cosmonautics Day in Russia.",
        "causes": ["Cold War space race between Soviet Union and United States", "Soviet rocket technology lead under Sergei Korolev", "Sputnik 1 (1957) established Soviet orbital capability"],
        "effects": ["Humanity's first spaceflight, opening the Space Age", "Intensified US space commitment leading to Apollo program", "Became iconic symbol of Soviet technological achievement"],
        "relationships": [
            {"sourceSlug": "yuri-gagarin", "sourceName": "Yuri Gagarin", "verb": "PARTICIPATES_IN", "targetSlug": "space-race", "targetName": "Space Race", "context": "First human spaceflight gave Soviets dramatic lead in Space Race"},
            {"sourceSlug": "yuri-gagarin", "sourceName": "Yuri Gagarin", "verb": "INFLUENCES", "targetSlug": "neil-armstrong", "targetName": "Neil Armstrong", "context": "Gagarin's flight directly motivated the Apollo program and Armstrong's Moon landing"},
            {"sourceSlug": "sergei-korolev", "sourceName": "Sergei Korolev", "verb": "CAUSES", "targetSlug": "yuri-gagarin", "targetName": "Yuri Gagarin", "context": "Korolev designed Vostok spacecraft and selected Gagarin for the flight"},
            {"sourceSlug": "yuri-gagarin", "sourceName": "Yuri Gagarin", "verb": "OCCURS_IN", "targetSlug": "baikonur-cosmodrome", "targetName": "Baikonur Cosmodrome", "context": "Launched from Baikonur, Kazakhstan, April 12, 1961"},
            {"sourceSlug": "yuri-gagarin", "sourceName": "Yuri Gagarin", "verb": "OCCURS_IN", "targetSlug": "saratov", "targetName": "Saratov Oblast", "context": "Landed by parachute near Engels, Saratov Oblast"}
        ],
        "places": [{"name": "Baikonur Cosmodrome, Kazakhstan", "role": "Launch site"}, {"name": "Klushino, Russia", "role": "Birthplace"}, {"name": "Star City, Moscow Oblast", "role": "Cosmonaut training center"}],
        "subjects": ["Space Exploration", "Cold War", "Soviet Union", "Cosmonautics", "Vostok Program", "Russia", "Space Race", "Aviation"],
        "frameworks": ["CAUSE_AND_EFFECT", "WORLD_SYSTEMS", "COMPARATIVE_CIVILIZATIONS"]
    },
}

# ═══ NEW ENTITIES ═══

NEW_ENTITIES = [
    {
        "slug": "frida-kahlo-museum",
        # SKIP — already exists as a stub, will not create duplicates
    },
]
# (No new entities for batch 6 — focusing on enrichment quality)


# ═══ EXECUTION ═══

def enrich_entity(slug, data):
    """Find and enrich an existing entity file."""
    for f in glob.glob(f"{BASE}/**/*.json", recursive=True):
        if slug not in os.path.basename(f):
            continue
        try:
            d = json.load(open(f))
            e = d["entities"][0]
            if e["slug"].replace("_", "-") != slug:
                continue
        except:
            continue

        # Update fields
        e["summary"] = data["summary"]

        # Parse detailsJson
        dj = e.get("detailsJson", "")
        if isinstance(dj, str) and dj:
            try:
                details = json.loads(dj)
            except:
                details = {}
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

        # Write back
        with open(f, "w") as fh:
            json.dump(d, fh, indent=2, ensure_ascii=False)
            fh.write("\n")

        return True
    return False


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


print("=== BATCH 6: Enrichment ===")

enriched = 0
failed = 0

for slug, data in ENRICHMENTS.items():
    if enrich_entity(slug, data):
        print(f"  ENRICHED {slug}")
        enriched += 1
    else:
        print(f"  NOT FOUND {slug}")
        failed += 1

print(f"\nLocal files: {enriched} enriched, {failed} not found")

# Sync to Appwrite
print("\n=== Syncing to Appwrite ===")

# Build slug→file index
slug_index = {}
for f in glob.glob(f"{BASE}/**/*.json", recursive=True):
    try:
        d = json.load(open(f))
        e = d["entities"][0]
        slug_index[e["slug"].replace("_", "-")] = (f, e)
    except:
        pass

sync_ok = 0
sync_fail = 0

for slug in ENRICHMENTS:
    if slug not in slug_index:
        continue
    f, e = slug_index[slug]
    data = entity_to_appwrite(e)
    doc_id = slug_to_id(e["slug"])

    existing = get_doc(doc_id) or get_doc(e["slug"])
    if existing:
        did = doc_id if get_doc(doc_id) else e["slug"]
        if update_doc(did, data):
            sync_ok += 1
        else:
            sync_fail += 1
    else:
        if create_doc(doc_id, data):
            sync_ok += 1
        else:
            sync_fail += 1
    time.sleep(0.15)

print(f"Appwrite: {sync_ok} synced, {sync_fail} failed")
print(f"\n=== BATCH 6 COMPLETE: {enriched} enriched ===")
