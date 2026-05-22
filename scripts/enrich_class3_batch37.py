#!/usr/bin/env python3
"""
Batch 37 — 8 entities (Class 381): World-Famous Universities
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()
FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/381-Class-381"
FILE_PREFIX = "381"


def enrich_entity(slug, data):
    fname = os.path.join(FOLDER, f"{FILE_PREFIX}{slug}.json")
    if not os.path.exists(fname):
        print(f"  SKIP (not found): {fname}"); return
    with open(fname, "r", encoding="utf-8") as f:
        doc = json.load(f)
    entity = doc["entities"][0]
    det = json.loads(entity.get("detailsJson", "{}"))
    edit_log = det.get("_editLog", [])
    for field in ("summary", "importanceScore", "historicalSignificance"):
        if field in data:
            old = entity.get(field)
            entity[field] = data[field]
            edit_log.append({"timestamp": NOW, "editorId": EDITOR_ID, "field": field,
                             "oldValue": str(old)[:300], "newValue": str(data[field])[:300]})
    for field in ("causes", "effects", "relationships"):
        if field in data:
            old = det.get(field, [])
            det[field] = data[field]
            edit_log.append({"timestamp": NOW, "editorId": EDITOR_ID, "field": field,
                             "oldValue": json.dumps(old)[:300], "newValue": json.dumps(data[field])[:300]})
    det["_editLog"] = edit_log
    det["_unsyncedEdits"] = True
    entity["_unsyncedEdits"] = True
    entity["detailsJson"] = json.dumps(det, ensure_ascii=False)
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    slen = len(entity.get("summary", ""))
    print(f"  ✓ {entity['name']} — sum={slen}c c={len(det.get('causes', []))} e={len(det.get('effects', []))}")


ENTITIES = [

    ("harvard-university", {
        "summary": (
            "Harvard University (est. 1636, Cambridge, Massachusetts — the oldest university in the United States, founded by the Massachusetts Bay Colony) is the world's most prestigious and influential research university — the alma mater of 8 U.S. presidents, 161 Nobel laureates (the most of any university), 14 Turing Award winners, and 62 billionaires. With an endowment of $51 billion (the world's largest university endowment), Harvard has shaped American governance, law, medicine, business, and science more than any other single educational institution.\n\n"
            "Harvard was founded in 1636 — just six years after the Massachusetts Bay Colony's establishment — by Puritan settlers who wanted to ensure an educated ministry for their religious commonwealth. Named after John Harvard (1607–1638), who bequeathed his library and half his estate to the college, Harvard evolved from a Puritan divinity school into a secular university through the 17th–19th centuries. Charles W. Eliot's presidency (1869–1909) — which abolished fixed curricula, introduced the elective system, and transformed Harvard from a regional college into a research university — was the defining institutional transformation.\n\n"
            "Harvard's impact on American and global institutions is immeasurable: the Harvard Law School has trained generations of American lawyers and judges; the Harvard Business School's MBA case method has shaped business education worldwide; the Harvard Medical School is the world's most influential medical research institution; and the Kennedy School of Government trains global policy leaders."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's most prestigious and influential research university (est. 1636, oldest US university); 8 US presidents, 161 Nobel laureates (most of any university), 14 Turing Award winners, 62 billionaires; $51 billion endowment (world's largest); Charles W. Eliot presidency (1869–1909) — elective system, research university transformation; Harvard Law, Business (MBA case method), Medical School; Kennedy School; shaped American governance, law, medicine, business, science.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Puritan settlers' conviction that an educated ministry was essential for their religious commonwealth — and their decision to establish a college just six years after the Massachusetts Bay Colony's founding — created Harvard as the primary educational institution of colonial New England",
            "John Harvard's bequest (1638) — of his library (400 books) and half his estate (£779) to the college — provided both the financial foundation and the name for the institution, representing one of the most consequential acts of private educational philanthropy in American history",
            "Charles W. Eliot's 40-year presidency (1869–1909) — which abolished fixed curricula, introduced the elective system, established graduate and professional schools, and recruited the leading scholars in each field — transformed Harvard from a regional New England college into the world's leading research university"
        ],
        "effects": [
            "Harvard's educational model — the residential college system, the elective curriculum, the graduate school structure, the case method in business education — has been adopted by American universities worldwide, making Harvard the primary model for the modern American university",
            "The Harvard Business School's MBA case method (est. 1908) — which teaches business through analysis of real business situations — has been adopted by business schools worldwide and trained the generation of business leaders who shaped the 20th-century American and global economy",
            "Harvard's concentration of Nobel laureates (161), US presidents (8), and influential alumni across law, medicine, government, finance, and academia has created a self-reinforcing network of global institutional influence that no other university has achieved, making Harvard's alumni network one of the most powerful informal institutions in world governance",
            "Harvard's endowment management — pioneering the 'Harvard model' of endowment investment in alternative assets (private equity, venture capital, real assets) under David Swensen-era management — transformed university endowment investment worldwide, creating the model adopted by Yale, Princeton, and university endowments globally"
        ],
        "relationships": [
            {"entity": "Massachusetts Bay Colony (founded Harvard 1636)", "relationship": "FOUNDED_BY_THE", "note": "Harvard was founded by the Massachusetts Bay Colony (1636) — six years after the colony's establishment — as a divinity school for Puritan ministers"},
            {"entity": "Charles W. Eliot (president 1869–1909, research university transformation)", "relationship": "TRANSFORMED_INTO_A_RESEARCH_UNIVERSITY_BY", "note": "Eliot's 40-year presidency — abolishing fixed curricula, introducing the elective system, establishing graduate schools — was the defining transformation of Harvard into a world-leading research university"},
            {"entity": "Harvard Business School (MBA case method, 1908)", "relationship": "INCLUDES_THE_GLOBALLY_INFLUENTIAL", "note": "The HBS MBA case method — adopted worldwide — has shaped business education and the training of global business leaders more than any other single educational innovation"},
            {"entity": "161 Nobel laureates (most of any university)", "relationship": "ALMA_MATER_OR_INSTITUTIONAL_HOME_OF", "note": "Harvard's 161 Nobel laureates — more than any other university — reflect its position as the world's leading concentration of research excellence"},
            {"entity": "$51 billion endowment (world's largest)", "relationship": "SUSTAINED_BY_THE", "note": "Harvard's $51 billion endowment — the world's largest — provides the financial foundation for its research, faculty, and financial aid programmes"}
        ],
    }),

    ("university-of-oxford", {
        "summary": (
            "The University of Oxford (est. c.1096–1167, Oxford, England — the oldest English-speaking university in the world) is the most prestigious university in the UK and one of the two most influential universities in the world (with Cambridge) — the alma mater of 28 British Prime Ministers, 72 Nobel laureates, and a disproportionate share of British scientific, literary, and governmental achievement over 900 years. Oxford's collegiate system — 44 autonomous colleges, each with its own endowment, facilities, and character — is the foundational model for collegiate universities worldwide.\n\n"
            "Oxford's origins are obscure — teaching existed at Oxford from at least 1096, and the university grew rapidly after Henry II banned English students from attending the University of Paris (1167). The first colleges — University College (c.1249), Balliol (c.1263), Merton (c.1264) — were founded as residential communities for scholars, establishing the collegiate structure that remains Oxford's defining institutional feature. Oxford's tutorial system — weekly one-to-one or small-group sessions between students and their tutors — is the most intensive undergraduate teaching method in the world.\n\n"
            "Oxford's contributions to science include the discovery of penicillin (Howard Florey and Ernst Chain, 1940, building on Alexander Fleming's work), the development of the Oxford-AstraZeneca COVID-19 vaccine (2020–2021), and the work of Roger Bannister (first 4-minute mile, 1954), Tim Berners-Lee (World Wide Web, 1989), and Stephen Hawking (theoretical cosmology). Oxford's literary alumni include J.R.R. Tolkien, C.S. Lewis, Oscar Wilde, W.H. Auden, and Philip Pullman."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Oldest English-speaking university (est. c.1096–1167); 28 British Prime Ministers, 72 Nobel laureates; collegiate system (44 colleges) — foundational model for collegiate universities worldwide; tutorial system — most intensive undergraduate teaching method; penicillin discovery (Howard Florey and Ernst Chain, 1940); Oxford-AstraZeneca COVID-19 vaccine (2020–2021); Tim Berners-Lee (World Wide Web, 1989); J.R.R. Tolkien, C.S. Lewis, Oscar Wilde literary alumni.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Henry II's ban on English students attending the University of Paris (1167) — driving students back to England and concentrating them in Oxford — was the political act that transformed Oxford from a teaching centre into a university, demonstrating how political disruption can create institutional foundations",
            "The foundation of the first residential colleges (University College c.1249, Balliol c.1263, Merton c.1264) — as endowed communities that provided scholars with housing, meals, and community — established the collegiate structure that became Oxford's defining institutional innovation and the model for Cambridge and other collegiate universities",
            "The Church of England's long connection with Oxford — which made it the training ground for the educated clergy, lawyers, and administrators of the English state — gave Oxford a privileged position in English institutional life that was self-reinforcing: those trained at Oxford went on to control the institutions that funded Oxford"
        ],
        "effects": [
            "Oxford's tutorial system — weekly one-to-one or small-group sessions requiring students to defend written arguments before a specialist — has produced a distinctive intellectual culture of debate, rigour, and independent thinking that has made Oxford graduates disproportionately influential in British public life",
            "The discovery of penicillin as a usable antibiotic (Howard Florey and Ernst Chain, Oxford, 1940) — building on Alexander Fleming's 1928 observation — is one of the most consequential medical discoveries in history, saving an estimated 200 million lives by enabling the treatment of bacterial infections that had previously been fatal",
            "The Oxford-AstraZeneca COVID-19 vaccine (developed 2020–2021) — which was licensed at cost for developing countries and administered to 3 billion+ people worldwide — is the most widely administered vaccine in history, making Oxford the university at the centre of the most significant public health achievement of the 21st century",
            "Oxford's 900-year production of British political leaders — 28 Prime Ministers, including four consecutive ones (Blair, Brown, Cameron, May) — has made it the single most powerful institutional source of British governance, with Oxford's PPE (Philosophy, Politics, and Economics) degree uniquely positioning graduates for political leadership"
        ],
        "relationships": [
            {"entity": "Henry II (ban on English students at Paris, 1167)", "relationship": "POLITICAL_ACT_THAT_ACCELERATED_THE_FOUNDING_OF", "note": "Henry II's 1167 ban on English students attending Paris concentrated students in Oxford — transforming it from a teaching centre into a university"},
            {"entity": "Penicillin (Howard Florey and Ernst Chain, Oxford 1940)", "relationship": "SITE_OF_THE_DEVELOPMENT_OF_PENICILLIN_AS_A_USABLE_ANTIBIOTIC", "note": "Florey and Chain's Oxford work (1940) — developing Fleming's penicillin observation into a usable antibiotic — is one of the most consequential medical discoveries in history"},
            {"entity": "Oxford-AstraZeneca COVID-19 vaccine (2020–2021, 3 billion+ administered)", "relationship": "DEVELOPED_THE_MOST_WIDELY_ADMINISTERED_VACCINE_IN_HISTORY", "note": "The Oxford-AstraZeneca vaccine — licensed at cost for developing countries — was administered to 3 billion+ people and is the most widely administered vaccine in history"},
            {"entity": "Collegiate system (44 colleges)", "relationship": "FOUNDED_AND_PERFECTED_THE", "note": "Oxford's 44 autonomous colleges — each with its own endowment and character — are the foundational model for collegiate universities worldwide"},
            {"entity": "28 British Prime Ministers (Oxford graduates)", "relationship": "PRIMARY_INSTITUTIONAL_SOURCE_OF_BRITISH_POLITICAL_LEADERSHIP", "note": "Oxford's 28 Prime Minister graduates — including four consecutive ones — make it the single most powerful institutional source of British political governance"}
        ],
    }),

    ("massachusetts-institute-of-technology", {
        "summary": (
            "The Massachusetts Institute of Technology (MIT, est. 1861, Cambridge, Massachusetts — founded by William Barton Rogers) is the world's most influential science and technology university — the primary institutional source of the technologies that define the digital age, with alumni and faculty responsible for inventing the World Wide Web (Tim Berners-Lee, CERN), RSA encryption (Rivest, Shamir, Adleman), radar technology (MIT Radiation Laboratory), ARPANET (contributing institutions), and fundamental advances in artificial intelligence, robotics, quantum computing, and biotechnology. MIT's 97 Nobel laureates, 26 Turing Award winners, and 26 MacArthur Fellows reflect its unparalleled concentration of scientific talent.\n\n"
            "MIT was founded in 1861 — on the eve of the Civil War — by William Barton Rogers, a geologist who believed that scientific and technical education should be practical rather than classical: MIT's motto Mens et Manus ('Mind and Hand') embodies Rogers's conviction that scientific knowledge should be combined with hands-on application. MIT moved to its current Cambridge campus in 1916, opposite Harvard, creating the most concentrated node of scientific talent in the world — the 'Mind Mile' where MIT and Harvard have produced more Nobel laureates per square mile than anywhere else on Earth.\n\n"
            "MIT's Media Lab (est. 1985), Computer Science and Artificial Intelligence Laboratory (CSAIL), and Lincoln Laboratory have been the primary institutional sources of the technologies that define the 21st-century digital economy, from touchscreen interfaces to autonomous vehicles to natural language processing."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's most influential science and technology university (est. 1861, William Barton Rogers); 97 Nobel laureates, 26 Turing Award winners; World Wide Web (Tim Berners-Lee, CERN), RSA encryption, radar technology (WWII MIT Radiation Laboratory), ARPANET contributions; AI, robotics, quantum computing, biotechnology; MIT Media Lab (1985), CSAIL; 'Mens et Manus' motto; Cambridge opposite Harvard — world's most concentrated science talent node; 30+ companies founded by MIT alumni per year; $18 billion endowment.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "William Barton Rogers's founding vision — that scientific and technical education should be practical and applied (Mens et Manus: 'Mind and Hand') rather than classical — created MIT's distinctive culture of combining theoretical rigour with hands-on engineering that distinguishes it from purely research-focused institutions",
            "The US government's WWII investment in MIT's Radiation Laboratory (1940–1945) — which developed radar technology and employed 4,000 scientists — gave MIT the scale, funding, and government relationships that made it the primary institutional partner for US national security technology, establishing the template for university-government-industry partnerships",
            "The concentration of MIT and Harvard within a mile of each other in Cambridge — creating the world's most dense node of scientific talent — produced the collaborative intellectual environment, cross-fertilisation of ideas, and venture capital infrastructure that made the Route 128 technology corridor and then Silicon Valley (by Stanford alumni following the MIT model) possible"
        ],
        "effects": [
            "MIT's alumni and faculty have founded 30,000+ companies that generate $2 trillion in annual revenues — including Qualcomm, Raytheon, Analog Devices, iRobot, and hundreds of biotechnology companies — making MIT's commercialisation impact on the American economy larger than most countries' entire GDP",
            "The MIT Radiation Laboratory's development of radar technology (1940–1945) — producing 150 radar systems that were decisive in WWII, from detecting incoming aircraft to guiding anti-submarine warfare — was MIT's most consequential single contribution to national security and demonstrated the university's capacity for wartime scientific mobilisation",
            "MIT's Artificial Intelligence Laboratory (est. 1959, now CSAIL) — founded by Marvin Minsky and John McCarthy — was the primary institutional source of AI research for four decades, training the generation of researchers who built the theoretical foundations that underlie contemporary machine learning",
            "The MIT-derived venture capital model — MIT alumni creating companies, MIT licensing technology to industry, MIT faculty taking equity in startups — has been adopted by universities worldwide as the template for commercialising academic research, transforming the relationship between universities and the technology industry"
        ],
        "relationships": [
            {"entity": "William Barton Rogers (founder 1861, 'Mens et Manus')", "relationship": "FOUNDED_BY", "note": "Rogers's founding vision — practical scientific education combining Mind and Hand — established MIT's distinctive culture that distinguishes it from purely classical research universities"},
            {"entity": "MIT Radiation Laboratory (WWII radar, 1940–1945)", "relationship": "SITE_OF_THE_DECISIVE_WARTIME_CONTRIBUTION_OF", "note": "The MIT Radiation Laboratory's radar development (1940–1945) — 150 radar systems decisive in WWII — was MIT's most consequential single contribution to national security"},
            {"entity": "MIT AI Laboratory / CSAIL (est. 1959, Minsky and McCarthy)", "relationship": "FOUNDED_THE_PRIMARY_INSTITUTIONAL_SOURCE_OF_ARTIFICIAL_INTELLIGENCE_RESEARCH_IN_THE_US", "note": "The MIT AI Lab (1959) — founded by Minsky and McCarthy — was the primary institutional source of AI research for four decades"},
            {"entity": "Route 128 technology corridor (MIT-spawned ecosystem)", "relationship": "PRIMARY_INSTITUTIONAL_SOURCE_OF_THE", "note": "MIT alumni and faculty spinoffs created the Route 128 technology corridor — and the MIT model was adopted by Stanford to create Silicon Valley"},
            {"entity": "RSA encryption (Rivest, Shamir, Adleman, MIT 1977)", "relationship": "INSTITUTIONAL_HOME_OF_THE_INVENTION_OF", "note": "RSA public-key encryption — invented at MIT (1977) — is the foundational technology of internet security, protecting all encrypted communications worldwide"}
        ],
    }),

    ("stanford-university", {
        "summary": (
            "Stanford University (est. 1885, Stanford, California — founded by Leland Stanford Sr. and Jane Stanford in memory of their son Leland Stanford Jr.) is the most economically impactful university in history — the institutional source of Silicon Valley and the technology companies that have reshaped the global economy. Stanford alumni have founded Google, Hewlett-Packard, Netflix, Yahoo, WhatsApp, Instagram, LinkedIn, Nike, and thousands of other companies, generating an estimated $2.7 trillion in annual revenues. With 83 Nobel laureates and a $37 billion endowment, Stanford's influence on the global technology industry is unmatched.\n\n"
            "Stanford was founded in 1885 — and opened in 1891 — on Leland Stanford Sr.'s farm ('The Farm', as students still call it) in Palo Alto, California, initially as a tuition-free university. The decision by Frederick Terman (Dean of Engineering, later Provost, 1940s–1960s) to encourage faculty and students to commercialise their research and start companies in the nearby orchards and farms was the founding act of Silicon Valley: William Hewlett and David Packard's garage startup (HP, 1939) was the first result; Google, Yahoo, and thousands of others followed.\n\n"
            "Stanford's distinctive contribution to American higher education is its creation of the university-industry partnership model — the idea that universities should not merely train students and publish research but should actively commercialise intellectual property, take equity in faculty startups, and create economic value through technology transfer — a model now adopted worldwide."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Most economically impactful university in history (est. 1885/opened 1891); institutional source of Silicon Valley; Google, HP, Netflix, Yahoo, WhatsApp, Instagram, LinkedIn, Nike founders; $2.7 trillion estimated alumni company revenues; 83 Nobel laureates, $37 billion endowment; Frederick Terman (Dean/Provost) created university-industry partnership model; William Hewlett and David Packard (HP, 1939, garage startup) — first Silicon Valley company; university-industry commercialisation model adopted worldwide.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Frederick Terman's decision (1940s–1960s) to actively encourage Stanford faculty and students to start companies near campus — taking equity stakes, providing startup space, and building industry connections — was the founding act of Silicon Valley, transforming Stanford from an academically respected regional university into the engine of the world's most important technology ecosystem",
            "Leland Stanford Sr.'s founding gift of 8,180 acres ('The Farm') — providing Stanford with an enormous land asset that generated the real estate income and flexible campus space that enabled the Stanford Research Park and technology transfer infrastructure — gave Stanford a physical and financial foundation for commercial development that few universities possessed",
            "California's frontier culture — its openness to risk-taking, its distance from East Coast academic traditionalism, and its mid-20th century defense industry infrastructure — created the cultural and industrial environment in which Stanford's commercialisation strategy could flourish"
        ],
        "effects": [
            "Silicon Valley — the global center of technology innovation, generating $3.5 trillion in market capitalisation among its major companies — is Stanford's most consequential creation: without Terman's commercialisation strategy and the HP garage startup model, the technology ecosystem that transformed the global economy would not have developed in its current form",
            "The Stanford university-industry partnership model — universities licensing intellectual property to industry, taking equity in faculty startups, building corporate research parks on campus land — has been adopted by universities worldwide, transforming the relationship between academic research and commercial application",
            "Google (founded by Sergey Brin and Larry Page as a Stanford research project) — with a market capitalisation of $1.7 trillion — is the most economically valuable company in history to emerge directly from university research, making Stanford the institutional origin of the dominant information utility of the 21st century",
            "Stanford's d.school (Hasso Plattner Institute of Design, est. 2004) — which popularised 'design thinking' as a methodology for innovation — has influenced product design, business strategy, and educational philosophy worldwide, with design thinking curricula adopted in thousands of schools and corporations"
        ],
        "relationships": [
            {"entity": "Frederick Terman (Dean/Provost, Silicon Valley architect)", "relationship": "SILICON_VALLEY_ECOSYSTEM_CREATED_BY_THE_COMMERCIALISATION_STRATEGY_OF", "note": "Terman's decision to encourage faculty and students to start companies — taking equity, providing space, building industry connections — was the founding act of Silicon Valley"},
            {"entity": "Hewlett-Packard (HP, William Hewlett and David Packard, 1939)", "relationship": "INSTITUTIONAL_ORIGIN_OF_THE_FIRST_SILICON_VALLEY_COMPANY", "note": "HP — founded in Hewlett's Packard's garage (1939) as Stanford engineering alumni — was the first Silicon Valley company and the prototype for university research commercialisation"},
            {"entity": "Google (Brin and Page, Stanford research project)", "relationship": "INSTITUTIONAL_SOURCE_OF_THE_FOUNDING_RESEARCH_PROJECT_OF", "note": "Google emerged directly from Brin and Page's Stanford doctoral research — making Stanford the institutional origin of the most economically valuable company in history"},
            {"entity": "Silicon Valley (global technology ecosystem)", "relationship": "PRIMARY_INSTITUTIONAL_SOURCE_OF_THE", "note": "Silicon Valley is Stanford's most consequential creation — without Terman's strategy and the HP model, the technology ecosystem that transformed the global economy would not exist in its current form"},
            {"entity": "Leland Stanford Sr. (founder, land endowment)", "relationship": "FOUNDED_BY", "note": "Stanford Sr.'s founding gift of 8,180 acres ('The Farm') gave Stanford the physical and financial foundation for the technology transfer infrastructure that created Silicon Valley"}
        ],
    }),

    ("princeton-university", {
        "summary": (
            "Princeton University (est. 1746, Princeton, New Jersey — the fourth-oldest US university, founded as the College of New Jersey) is one of the most academically excellent and influential universities in the world — the home of Albert Einstein (Institute for Advanced Study, adjacent to Princeton, 1933–1955), John Nash (Nobel Prize in Economics, subject of 'A Beautiful Mind'), Alan Turing (who completed his doctoral work at Princeton under Alonzo Church), and the site of some of the most consequential mathematical and physical discoveries of the 20th century. Princeton's 69 Nobel laureates, $34 billion endowment, and its reputation for the highest undergraduate-to-faculty ratio in the Ivy League make it unique among American research universities.\n\n"
            "Princeton was founded in 1746 as the College of New Jersey — the fourth college in colonial America — by evangelical Presbyterians seeking to train ministers for the Great Awakening. Under Woodrow Wilson's presidency (1902–1910), Princeton was transformed into a modern research university — Wilson introduced the preceptorial tutorial system and attempted (unsuccessfully) to abolish the eating clubs that divided Princeton's social life — before Wilson's election as New Jersey Governor (1910) and US President (1912).\n\n"
            "Princeton's specific contributions to 20th-century science include the development of the atomic bomb at the nearby Princeton laboratories (contributing to the Manhattan Project), John Wheeler's work on black holes and general relativity, and the Princeton mathematics department's role in 20th-century pure mathematics — including Andrew Wiles's proof of Fermat's Last Theorem (1994)."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Fourth-oldest US university (est. 1746, College of New Jersey); Albert Einstein (Institute for Advanced Study, 1933–1955); John Nash (Nobel Economics, 'A Beautiful Mind'); Alan Turing (doctoral work, under Alonzo Church); Andrew Wiles (Fermat's Last Theorem, 1994); 69 Nobel laureates; $34 billion endowment; Woodrow Wilson (president 1902–1910, preceptorial system); highest undergraduate-to-faculty ratio in Ivy League; Manhattan Project contributing institutions.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Princeton's foundation (1746) by evangelical Presbyterians — in the context of the Great Awakening's challenge to established Congregationalist Harvard and Anglican William and Mary — reflected the religious diversity of colonial American higher education and the competition between Protestant denominations for educational influence",
            "The flight of European Jewish academics from Nazi Germany (1933) — which brought Albert Einstein, John von Neumann, Kurt Gödel, and others to Princeton's Institute for Advanced Study (adjacent to the university) — concentrated the greatest gathering of mathematical and theoretical physics talent in history within a mile of Princeton's campus",
            "Woodrow Wilson's presidency (1902–1910) — introducing the preceptorial tutorial system, recruiting young faculty as intellectual companions for students, and attempting to restructure Princeton's social life — established Princeton's distinctive combination of research excellence and intimate undergraduate teaching"
        ],
        "effects": [
            "The Institute for Advanced Study — technically independent but adjacent to Princeton and intellectually intertwined with it — hosted Albert Einstein (1933–1955), John von Neumann, Kurt Gödel, and the greatest concentration of mathematical talent in history, producing work that shaped 20th-century physics, logic, and computer science",
            "John Nash's game theory work at Princeton (1948–1951) — developing the Nash equilibrium concept — transformed economics, political science, and evolutionary biology, with applications in everything from market design to nuclear deterrence strategy, earning Nash the Nobel Prize in Economics (1994) and popularised in the film 'A Beautiful Mind'",
            "Andrew Wiles's proof of Fermat's Last Theorem (Princeton, 1994) — solving the most famous unsolved problem in mathematics after 358 years — was the most celebrated mathematical achievement of the 20th century, representing the culmination of a research programme that drew on seven years of secret work",
            "Princeton's graduate programme in mathematics and theoretical physics — producing an extraordinary concentration of Fields Medal winners, Nobel laureates, and MacArthur Fellows — has made it the world's most consistently excellent institution for pure mathematics, maintaining this position for over a century"
        ],
        "relationships": [
            {"entity": "Institute for Advanced Study (adjacent, Einstein 1933–1955)", "relationship": "INTELLECTUALLY_INTERTWINED_WITH_THE", "note": "The IAS — technically independent but adjacent to Princeton — hosted Einstein, von Neumann, and Gödel, creating the greatest concentration of mathematical talent in history"},
            {"entity": "Albert Einstein (at IAS 1933–1955)", "relationship": "ASSOCIATED_WITH_THROUGH_THE_IAS", "note": "Einstein's residence at the IAS (1933–1955) — after fleeing Nazi Germany — made Princeton the permanent home of the 20th century's most famous scientist"},
            {"entity": "John Nash (Nash equilibrium, doctoral work)", "relationship": "SITE_OF_THE_DOCTORAL_WORK_OF", "note": "Nash's Princeton doctoral work (1948–1951) — developing the Nash equilibrium — transformed economics and political science and earned the Nobel Prize"},
            {"entity": "Andrew Wiles (Fermat's Last Theorem, 1994)", "relationship": "SITE_OF_THE_PROOF_OF_FERMAT'S_LAST_THEOREM_BY", "note": "Wiles's proof of Fermat's Last Theorem (Princeton, 1994) — after 358 years unsolved — was the most celebrated mathematical achievement of the 20th century"},
            {"entity": "Woodrow Wilson (president 1902–1910, later US President)", "relationship": "TRANSFORMED_INTO_MODERN_RESEARCH_UNIVERSITY_BY", "note": "Wilson's Princeton presidency (1902–1910) — preceptorial system, graduate school reforms — established Princeton's combination of research excellence and intimate undergraduate teaching, before his political career"}
        ],
    }),

    ("yale-university", {
        "summary": (
            "Yale University (est. 1701, New Haven, Connecticut — the third-oldest US university, founded by Congregationalist ministers) is one of the most prestigious and influential universities in the world — the alma mater of 5 US Presidents (including both Bushes and Bill Clinton), 65 Nobel laureates, and the source of some of the most influential cultural and intellectual traditions in American life: the Yale School of Drama (US theatre training), the Yale Whiffenpoofs (oldest collegiate a cappella group), Skull and Bones (the most influential secret society in American political life), and the Yale Law School (the most selective law school in the US and the training ground for the American legal elite).\n\n"
            "Yale was founded in 1701 as the Collegiate School of Connecticut — by Congregationalist ministers who felt that Harvard had become too liberal — before being renamed Yale in 1718 in gratitude for Elihu Yale's gift of goods worth £562 and 417 books. Yale's evolution into a research university was driven by the Sheffield Scientific School (1847) and President Timothy Dwight's reforms, and by the Morrill Land Grant Act of 1862, which pushed American universities toward scientific and practical education.\n\n"
            "Yale's cultural contributions extend beyond academic research: the Yale University Press (est. 1908) is one of the world's largest university presses; the Yale University Art Gallery (est. 1832) is the oldest university art museum in the Western Hemisphere; and the Beinecke Rare Book Library holds one of the world's great collections of rare books and manuscripts, including the Gutenberg Bible and the Voynich Manuscript."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Third-oldest US university (est. 1701, Congregationalist ministers); 5 US Presidents (both Bushes, Clinton); 65 Nobel laureates; Yale Law School — most selective US law school, trains American legal elite; Yale School of Drama; Skull and Bones (most influential US secret society); Yale University Art Gallery (oldest Western Hemisphere university art museum, est. 1832); Beinecke Rare Book Library (Gutenberg Bible, Voynich Manuscript); Yale University Press (1908); $41 billion endowment; David Swensen's endowment investment model — adopted worldwide.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Congregationalist ministers' founding of the Collegiate School (1701) as a response to Harvard's perceived theological liberalism — wanting a university that would remain orthodox in Puritan Calvinism — reflected the religious sectarianism that drove the multiplication of colonial American colleges",
            "Elihu Yale's naming gift (1718) — goods, books, and a portrait worth £562 — established the practice of naming American universities after major donors, creating the tradition that would define American philanthropic higher education",
            "David Swensen's Yale Endowment model (1985–2021) — which pioneered investment in alternative assets (private equity, venture capital, real assets, hedge funds) rather than traditional stocks and bonds, generating 12%+ annual returns — was adopted by university endowments worldwide, transforming endowment management and providing Yale with the financial resources for its academic ambitions"
        ],
        "effects": [
            "Yale Law School — the most selective law school in the United States (acceptance rate ~8%) — has trained a disproportionate share of the American legal elite, including Supreme Court justices Ruth Bader Ginsburg, Sonia Sotomayor, Clarence Thomas, Brett Kavanaugh, and Amy Coney Barrett, as well as both Bushes and Clinton and Hillary Clinton",
            "David Swensen's Yale Endowment model — pioneering alternative asset investment (private equity, venture capital, real assets) — generated 12%+ annual returns for 35 years and was adopted by Harvard, Princeton, and university endowments worldwide, transforming institutional investment and creating the asset class known as 'the endowment model'",
            "Yale's Skull and Bones secret society — founded 1832, with membership including both Bush Presidents, John Kerry, and many CIA directors — has been the most consistently powerful informal network in American political and intelligence community life, demonstrating the long-term institutional power of elite university secret societies",
            "The Beinecke Rare Book Library — holding the Gutenberg Bible, the Voynich Manuscript, and 150 million+ items — is one of the world's greatest rare book collections and the primary research destination for the history of the book and textual scholarship"
        ],
        "relationships": [
            {"entity": "Yale Law School (most selective US law school)", "relationship": "INCLUDES_THE", "note": "Yale Law School — training Supreme Court justices, US Presidents, and the American legal elite — is the most influential single institution in the American legal system"},
            {"entity": "David Swensen (endowment model, 1985–2021)", "relationship": "ENDOWMENT_MANAGEMENT_REVOLUTIONISED_BY", "note": "Swensen's alternative asset endowment model — 12%+ annual returns, adopted worldwide — transformed institutional investment and provided Yale's financial foundation"},
            {"entity": "Skull and Bones (secret society, est. 1832)", "relationship": "INSTITUTIONAL_HOME_OF_THE_MOST_INFLUENTIAL", "note": "Skull and Bones — with both Bush Presidents, Kerry, and CIA directors among members — has been the most consistently powerful informal network in American political life"},
            {"entity": "Beinecke Rare Book Library (Gutenberg Bible, Voynich Manuscript)", "relationship": "HOUSES_THE_WORLD-RENOWNED", "note": "The Beinecke — holding the Gutenberg Bible and the Voynich Manuscript — is one of the world's greatest rare book collections"},
            {"entity": "5 US Presidents (both Bushes, Clinton)", "relationship": "ALMA_MATER_OF", "note": "Yale's 5 US Presidential graduates — including both Bush Presidents and Bill Clinton — make it the third most consequential presidential alma mater (after Harvard's 8 and William and Mary's 4)"}
        ],
    }),

    ("university-of-bologna", {
        "summary": (
            "The University of Bologna (Università di Bologna, est. 1088, Bologna, Italy — the oldest university in the world) is the founding institution of the Western university tradition — the original model from which all subsequent universities (Oxford, Cambridge, Paris, Salamanca, Harvard, and 25,000+ others) are descended. Founded in 1088 as a school of law in the prosperous Lombard city of Bologna, the university's 936-year continuous history makes it a unique cultural institution — the living embodiment of the Western intellectual tradition's continuity from medieval Christendom to the present day.\n\n"
            "Bologna's founding in 1088 was driven by the demand for expert legal education — specifically the study of Justinian's Corpus Juris Civilis (529 CE) — that the 11th-century revival of Roman law created. Irnerius (c.1050–1125) was the first great Bologna legal scholar, and his glosses on Justinian established the method of textual analysis that became the foundation of medieval legal scholarship. The University of Bologna established the 'studium generale' model — a community of scholars with the right to grant degrees recognised throughout Christendom — that was replicated across Europe.\n\n"
            "Bologna's alumni include Pope Alexander V, Dante Alighieri (student), Thomas Becket, Erasmus of Rotterdam, Copernicus (Nicolas Copernicus studied astronomy and mathematics at Bologna 1496–1500), and numerous medieval popes, emperors, and scholars. The university's motto — 'Alma Mater Studiorum' ('Nourishing Mother of Studies') — reflects its self-conscious identity as the source of the Western university tradition."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Oldest university in the world (est. 1088, Bologna, Italy); founding institution of the Western university tradition; 936 years continuous history; 'studium generale' model replicated across Europe; Irnerius (c.1050–1125) — first great Bologna legal scholar, glosses on Justinian's Corpus Juris Civilis; alumni: Dante Alighieri (student), Thomas Becket, Erasmus, Copernicus (1496–1500); Pope Alexander V; 'Alma Mater Studiorum' motto; 87,000 students; model for all 25,000+ subsequent universities.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The 11th-century revival of Roman law — driven by the recovery and study of Justinian's Corpus Juris Civilis (529 CE), which provided the legal framework for the emerging Italian city-states and the Holy Roman Empire — created the demand for expert legal education that Bologna's founding scholars answered",
            "Bologna's position as a prosperous, independent Lombard city-state — with a merchant class that needed legal expertise for commercial contracts and a political community that needed trained lawyers for diplomatic and administrative roles — provided the financial demand and political support for a permanent community of legal scholars",
            "The medieval Church's need for trained canon lawyers — who could navigate the complex intersection of Roman law and Church law — created a parallel demand for Bologna's legal education, making the university simultaneously a civil and ecclesiastical institution"
        ],
        "effects": [
            "The University of Bologna's 'studium generale' model — a community of scholars with the right to grant degrees recognised throughout Christendom — was replicated in Paris (c.1150), Oxford (c.1167), Cambridge (1209), Salamanca (1218), Padua (1222), and eventually in every European country, creating the Western university system that educates 250 million students worldwide",
            "The Bologna Process (1999) — in which 29 European countries signed the Bologna Declaration to create a common European higher education area — used Bologna's name to symbolise the unity of the Western university tradition, creating the European Credit Transfer System (ECTS) and standardising degree structures across Europe",
            "Copernicus's study of astronomy and mathematics at Bologna (1496–1500) — where he worked with the astronomer Domenico Maria Novara and observed the occultation of Aldebaran by the Moon — contributed to his development of the heliocentric theory that he would publish in De revolutionibus (1543), making Bologna a link in the chain of the Scientific Revolution",
            "The model of student-controlled universities — Bologna was initially governed by students who hired and fired professors, set their salaries, and controlled the curriculum — established an alternative governance model to the master-controlled Paris model that influenced the development of student rights and academic governance for centuries"
        ],
        "relationships": [
            {"entity": "Justinian's Corpus Juris Civilis (529 CE, legal foundation)", "relationship": "FOUNDED_TO_TEACH_AND_INTERPRET_THE", "note": "Bologna's founding (1088) was driven by demand for expert interpretation of Justinian's Corpus Juris Civilis — the revival of Roman law that needed trained legal scholars"},
            {"entity": "Irnerius (c.1050–1125, first great Bologna scholar)", "relationship": "INTELLECTUAL_TRADITION_ESTABLISHED_BY", "note": "Irnerius's glosses on Justinian established the method of textual analysis that became the foundation of medieval legal scholarship"},
            {"entity": "Copernicus (studied astronomy at Bologna 1496–1500)", "relationship": "SITE_OF_ASTRONOMICAL_STUDIES_OF", "note": "Copernicus's Bologna studies (1496–1500) — working with Domenico Maria Novara — contributed to his development of the heliocentric theory"},
            {"entity": "'Studium generale' model (replicated in Oxford, Paris, Cambridge)", "relationship": "CREATED_THE", "note": "Bologna's studium generale model — degrees recognised throughout Christendom — was replicated in Paris, Oxford, Cambridge, and eventually in 25,000+ universities worldwide"},
            {"entity": "Bologna Process (1999, European Higher Education Area)", "relationship": "SYMBOLIC_NAME_INSPIRATION_FOR_THE", "note": "The Bologna Process (1999) — creating the European Higher Education Area — used Bologna's name to symbolise the unity of the Western university tradition"}
        ],
    }),

    ("eth-zurich", {
        "summary": (
            "ETH Zurich (Eidgenössische Technische Hochschule Zürich, est. 1855, Zurich, Switzerland — founded by the Swiss Confederation) is Europe's premier science and technology university and the world's premier continental European science institution — the alma mater of Albert Einstein (BA and doctoral studies), the home of 22 Nobel laureates, and the primary source of Swiss scientific and technological excellence. Einstein called it 'the most stimulating intellectual environment I have ever encountered'; the university where he failed his entrance exam, then graduated, then was rejected for a faculty position before winning the Nobel Prize.\n\n"
            "ETH Zurich was founded in 1855 — by an Act of the Swiss Federal Parliament — as a Swiss Federal Polytechnic School intended to train engineers, scientists, and mathematicians for the industrialising Swiss economy. Gottfried Semper (the architect who designed the Opera House in Dresden) designed the main building. The university's early strength in engineering and chemistry drove the development of the Swiss chemical industry (Roche, Ciba-Geigy, Sandoz) and the watchmaking and precision engineering industries.\n\n"
            "ETH Zurich's 22 Nobel laureates include Albert Einstein (Physics 1921), Wilhelm Röntgen (Physics 1901, for X-rays), and Peter Debye (Chemistry 1936). Its current research strengths include robotics (ETH's ANYmal robot is the world's leading legged robot), materials science, quantum computing, and climate science — with the ETH Zurich Institute for Atmospheric and Climate Science being Europe's premier climate research institution."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Europe's premier science and technology university (est. 1855, Swiss Confederation); Albert Einstein (BA and doctoral studies, called it 'most stimulating intellectual environment'); 22 Nobel laureates including Einstein (Physics 1921), Wilhelm Röntgen (Physics 1901, X-rays), Peter Debye (Chemistry 1936); primary source of Swiss scientific excellence; ANYmal robot (world's leading legged robot); ETH Zurich Institute for Atmospheric and Climate Science (Europe's premier climate research institution); Swiss chemical industry (Roche, Ciba-Geigy, Sandoz) development.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Swiss Federal Parliament's founding of ETH Zurich (1855) — motivated by the recognition that Swiss industrialisation required trained engineers and scientists, and that a federal polytechnic school could serve the multilingual Swiss Confederation — created the institutional foundation for Swiss scientific excellence",
            "The concentration of Swiss precision engineering, chemical, and watchmaking industries in the ETH Zurich catchment area — which provided both the demand for technically trained graduates and the industrial partnerships for applied research — created the commercial ecosystem that sustained ETH's excellence",
            "The European tradition of academic excellence in German-speaking countries — Vienna, Berlin, Munich, Göttingen — provided ETH with the intellectual context, faculty recruitment opportunities, and scholarly standards that made it the equal of the great German research universities despite being much newer"
        ],
        "effects": [
            "Albert Einstein's studies at ETH Zurich (1896–1900) — where he first encountered Maxwell's electromagnetic theory, studied thermodynamics, and formed the intellectual foundations for his 1905 'miracle year' papers — made ETH Zurich a direct contributor to the Special Theory of Relativity, the most consequential scientific achievement of the 20th century",
            "Wilhelm Röntgen's discovery of X-rays (1895, at Würzburg but deeply connected to the German-Swiss scientific community ETH epitomised) — and ETH's subsequent development of medical imaging and materials analysis through X-ray techniques — contributed to one of the most consequential medical diagnostic technologies in history",
            "ETH Zurich's research on climate science — producing the landmark assessment of global temperature trends that contributed to IPCC reports — has made it a primary institutional voice in the global climate debate, with ETH researchers among the most cited climate scientists",
            "The Swiss chemical companies (Roche, Novartis, Ciba-Geigy, Sandoz) that emerged from the ETH Zurich scientific ecosystem now generate $100 billion+ in annual pharmaceutical revenues, making ETH the institutional source of the world's most pharmaceutically intensive industrial economy per capita"
        ],
        "relationships": [
            {"entity": "Albert Einstein (BA and doctoral studies, 1896–1900 and 1905)", "relationship": "ALMA_MATER_AND_INTELLECTUAL_FORMATION_OF", "note": "Einstein's ETH studies (1896–1900) provided the intellectual foundation for his 1905 miracle year papers — making ETH a direct contributor to the Special Theory of Relativity"},
            {"entity": "Wilhelm Röntgen (X-rays, 1895 — German-Swiss scientific community)", "relationship": "INSTITUTIONAL_CONTRIBUTOR_TO_THE_SCIENTIFIC_TRADITION_OF", "note": "Röntgen's 1895 X-ray discovery reflects the German-Swiss scientific community that ETH Zurich exemplified and sustained"},
            {"entity": "Roche, Novartis, Ciba-Geigy (Swiss pharmaceutical companies)", "relationship": "PRIMARY_INSTITUTIONAL_SOURCE_OF_THE_SCIENTIFIC_TALENT_THAT_FOUNDED_THE", "note": "ETH Zurich's chemistry and materials science programmes created the scientific talent base for the Swiss pharmaceutical industry — now generating $100 billion+ annually"},
            {"entity": "ETH Zurich climate science research (IPCC contributions)", "relationship": "EUROPE'S_PRIMARY_INSTITUTIONAL_CONTRIBUTOR_TO", "note": "ETH Zurich's climate science research — contributing to IPCC reports and global temperature assessments — makes it Europe's premier climate research institution"},
            {"entity": "ANYmal robot (world's leading legged robot)", "relationship": "DEVELOPED_THE", "note": "ETH Zurich's ANYmal — the world's leading legged robot, used for infrastructure inspection and emergency response — reflects ETH's world-leading robotics research programme"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 37 — {len(ENTITIES)} entities (Class 381: World-Famous Universities)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
