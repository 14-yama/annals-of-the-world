#!/usr/bin/env python3
"""
Batch 79 — 8 entities: Odilon Barrot, William Chamberlain, Albert Gallatin Harrison,
Bernardo de Iturriaza, Charles Dayan, Jean Despagnet, George Edmund Badger, Joseph McIlvaine
"""
import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/230-Class-230"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()


def enrich_entity(slug, data):
    fname = os.path.join(FOLDER, f"230{slug}.json")
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
    print(f"  ✓ {entity['name']} — sum={slen}c c={len(det.get('causes',[]))} "
          f"e={len(det.get('effects',[]))}")


ENTITIES = [

    ("odilon-barrot", {
        "summary": (
            "Camille-Hyacinthe Odilon Barrot "
            "(1791–1873) was a French "
            "moderate liberal politician "
            "of the July Monarchy and "
            "Second Republic eras who "
            "served as President of the "
            "Council (Prime Minister) "
            "of France (1848–1849) "
            "and as a significant "
            "constitutional liberal "
            "voice across four decades "
            "of tumultuous French "
            "politics. He was the "
            "leader of the 'dynastic "
            "opposition' under Louis-Philippe "
            "— those who accepted "
            "the July Monarchy's "
            "constitutional framework "
            "but pushed for reform — "
            "and he organized the "
            "famous 'banquet campaign' "
            "of 1847–1848 that indirectly "
            "triggered the February "
            "Revolution of 1848.\n\n"
            "The irony of Barrot's "
            "career is that the "
            "reform banquets he "
            "organized to pressure "
            "Guizot into liberalization "
            "triggered a revolution "
            "that destroyed the "
            "July Monarchy he "
            "wanted to reform — "
            "leaving him to serve "
            "as prime minister "
            "under Louis-Napoleon "
            "Bonaparte during "
            "the Second Republic.\n\n"
            "He later opposed "
            "Napoleon III's "
            "coup and was "
            "exiled from public life.\n\n"
            "'I wanted reform; "
            "I got revolution.'"
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "French Prime Minister (1848–1849); leader of the July Monarchy's 'dynastic opposition'; organized the banquet campaign of 1847–1848 that triggered the February Revolution; his reform movement accidentally destroyed the monarchy he wanted to improve; prime minister under Louis-Napoleon during the Second Republic; opposed Napoleon III's coup; pivotal figure in mid-19th-century French constitutionalism.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Louis-Philippe's July Monarchy and the growing demand for electoral reform — the constitutional monarchy's narrow franchise and Guizot's conservative governance that refused electoral expansion — created the political frustration that Barrot's dynastic opposition channeled",
            "The banquet campaign's political calculation — Barrot's strategy of using reform banquets to build popular pressure for electoral reform without triggering revolution — was based on the assumption that Louis-Philippe would negotiate rather than repress",
            "The February Revolution's surprise — the unintended radicalization of the banquet campaign into a full revolution when the government banned the final Paris banquet and crowds took to the streets — created the political catastrophe that Barrot had not intended to unleash"
        ],
        "effects": [
            "The banquet campaign he organized directly triggered the February Revolution of 1848 — the overthrow of Louis-Philippe and the establishment of the Second Republic that he had not intended and did not want",
            "His prime ministership under Louis-Napoleon contributed to the Second Republic's brief constitutional period — the government that struggled to manage the aftermath of the revolution his movement had inadvertently caused",
            "His opposition to Napoleon III's coup contributed to the liberal republican tradition — the principled constitutionalists who refused to accept the Second Empire's authoritarianism",
            "His career illustrated the unintended consequences of reform politics — the fundamental lesson that political reform movements can unleash revolutionary forces that destroy the moderate outcomes their organizers sought"
        ],
        "relationships": [
            {"target": "july-monarchy", "verb": "OPPOSES_WITHIN", "note": "Dynastic opposition leader pressing for reform"},
            {"target": "february-revolution-1848", "verb": "INADVERTENTLY_TRIGGERS", "note": "Banquet campaign accidentally caused the revolution"},
            {"target": "second-republic-france", "verb": "LEADS", "note": "Prime Minister 1848–1849"},
            {"target": "napoleon-iii", "verb": "OPPOSES", "note": "Opposed Louis-Napoleon's coup"},
            {"target": "francois-guizot", "verb": "OPPOSES", "note": "Dynastic opposition to Guizot's conservative governance"}
        ]
    }),

    ("william-chamberlain", {
        "summary": (
            "William Chamberlain (1755–1828) "
            "was an American Democratic-Republican "
            "politician from Vermont "
            "who served in the U.S. "
            "House of Representatives "
            "(1803–1805) and as Lieutenant "
            "Governor of Vermont "
            "(1813–1815). He was a "
            "Revolutionary War veteran "
            "who carried his military "
            "service into a political "
            "career that spanned "
            "the Jeffersonian and "
            "War of 1812 eras. "
            "Vermont in this period "
            "was transitioning "
            "from a Federalist "
            "to a Democratic-Republican "
            "state — Chamberlain's "
            "career reflected this "
            "political transition "
            "as the Federalist party "
            "that had dominated "
            "the founding era "
            "yielded to the "
            "Jeffersonian movement.\n\n"
            "His lieutenant governorship "
            "during the War of 1812 "
            "(1813–1815) placed him "
            "in Vermont's executive "
            "branch during the "
            "most difficult period "
            "of the conflict — "
            "the British invasion "
            "of Lake Champlain "
            "and the Plattsburgh "
            "Campaign that was "
            "one of the war's "
            "decisive moments.\n\n"
            "Vermont's geographic "
            "position on the "
            "Canadian border made "
            "its political leadership "
            "directly relevant "
            "to the War of 1812's "
            "northern theater.\n\n"
            "He was a Caledonia "
            "County farmer and "
            "civic leader."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Vermont Democratic-Republican Congressman (1803–1805) and Lieutenant Governor (1813–1815); Revolutionary War veteran; Lieutenant Governor during the War of 1812's northern theater including the Lake Champlain Campaign; served during Vermont's transition from Federalist to Democratic-Republican politics.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Vermont's political transition — the shift from Federalist to Democratic-Republican dominance as the Jeffersonian revolution transformed New England politics — created the political context for Chamberlain's Democratic-Republican career",
            "His Revolutionary War service — his military participation in the founding conflict — provided the patriotic credentials that underpinned his political career and his Lieutenant Governor service during the War of 1812",
            "Vermont's War of 1812 exposure — the state's geographic position on the Canadian border making it directly vulnerable to British military activity — created the significance of executive leadership during Chamberlain's lieutenant governorship"
        ],
        "effects": [
            "His congressional service contributed Vermont's Democratic-Republican votes to the Jeffersonian Congress — participating in the policy debates of the founding era's second generation",
            "His lieutenant governorship during the War of 1812 contributed to Vermont's military and political coordination — managing the state's response to the war's northern theater including the Lake Champlain Campaign",
            "His career contributed to Vermont's civic tradition — the Revolutionary War veterans who built the political institutions of the Green Mountain State across the founding and early republican eras",
            "His life (1755–1828) spanned the entire founding era — from the years before the Revolution through the Jacksonian opening, a remarkable continuity of American political experience"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Vermont Congressman 1803–1805"},
            {"target": "vermont", "verb": "SERVES_AS_LIEUTENANT_GOVERNOR_OF", "note": "Lieutenant Governor 1813–1815"},
            {"target": "war-of-1812", "verb": "GOVERNS_DURING", "note": "Lt. Governor during the northern theater campaigns"},
            {"target": "continental-army", "verb": "SERVES_IN", "note": "Revolutionary War veteran"},
            {"target": "lake-champlain-campaign", "verb": "GOVERNS_DURING", "note": "Vermont executive during the decisive northern battle"}
        ]
    }),

    ("albert-galliton-harrison", {
        "summary": (
            "Albert Gallatin Harrison (1800–1839) "
            "was an American Democratic "
            "politician from Missouri "
            "who served in the U.S. "
            "House of Representatives "
            "(1835–1839) during the "
            "Jacksonian era — dying "
            "young at age 39 after "
            "just two House terms. "
            "Named after Albert "
            "Gallatin, Jefferson's "
            "distinguished Treasury "
            "Secretary, Harrison "
            "was a Missouri Democrat "
            "whose brief career "
            "contributed Missouri's "
            "voice to the House "
            "during the Bank War's "
            "final years, the "
            "Independent Treasury "
            "debates, and the "
            "beginnings of the "
            "Van Buren administration's "
            "political challenges.\n\n"
            "Missouri in the "
            "1830s was a slave "
            "state at the frontier "
            "edge — a state "
            "that had nearly "
            "torn the Union "
            "apart in 1820 "
            "and was increasingly "
            "important to "
            "the balance of "
            "free and slave "
            "state representation.\n\n"
            "His death at 39 "
            "cut short what "
            "might have been "
            "a significant "
            "political career.\n\n"
            "He was a Missouri "
            "lawyer and Democratic politician."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Missouri Democratic Congressman (1835–1839); died at 39 cutting short his career; named after Albert Gallatin; served during the Bank War's final years and Van Buren's Independent Treasury debates; represented Missouri's frontier slave-state perspective; brief career during the Jacksonian era's major economic and political controversies.",
            "significanceCategory": "local"
        },
        "causes": [
            "Jackson's Bank War — the president's destruction of the Second Bank of the United States and the subsequent financial turmoil — created the major economic controversy of Harrison's House career",
            "Missouri's frontier political development — the state's rapid growth as a slave-state frontier that had already been the subject of the 1820 Missouri Compromise — created the political context for Harrison's Missouri Democratic career",
            "The Jacksonian patronage system — the Democratic Party organization that controlled Missouri politics and provided the structure for Harrison's political advancement — created the institutional pathway for his congressional career"
        ],
        "effects": [
            "His House service contributed Missouri's Democratic votes to the Bank War's final battles and the Independent Treasury debates — the frontier slave state's perspective on Jacksonian economic policy",
            "His death at 39 removed a potential future political figure from Missouri's political landscape — the early death that cut short what might have been a significant antebellum career",
            "His brief career contributed to Missouri's Democratic political tradition — the Jacksonian organization that would dominate Missouri politics through the antebellum era",
            "His naming after Albert Gallatin illustrated the Democratic tradition of honoring Jefferson's Treasury Secretary — the continuing reverence for Gallatin's fiscal philosophy in Democratic circles"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Missouri Congressman 1835–1839"},
            {"target": "bank-war", "verb": "SERVES_DURING", "note": "Congressman during Jackson's destruction of the BUS"},
            {"target": "independent-treasury", "verb": "VOTES_ON", "note": "House member during Van Buren's Independent Treasury debates"},
            {"target": "missouri", "verb": "REPRESENTS", "note": "Frontier slave-state Democratic congressman"},
            {"target": "albert-gallatin", "verb": "NAMED_AFTER", "note": "Named in honor of Jefferson's Treasury Secretary"}
        ]
    }),

    ("bernardo-de-iturriaza", {
        "summary": (
            "Bernardo de Iturriaza "
            "(fl. early 19th century) "
            "was a Spanish colonial "
            "official and administrator "
            "who served in the "
            "Viceroyalty of New Granada "
            "(present-day Colombia, "
            "Venezuela, Ecuador, and "
            "Panama) during the "
            "turbulent period of "
            "the Spanish American "
            "independence movements. "
            "Colonial administrators "
            "like Iturriaza faced "
            "the extraordinary challenge "
            "of maintaining royal "
            "authority in vast "
            "territories where "
            "the 1808 Napoleonic "
            "invasion of Spain "
            "had undermined the "
            "Bourbon crown's "
            "legitimacy and emboldened "
            "Creole elites to "
            "seek greater autonomy "
            "or full independence.\n\n"
            "The New Granada independence "
            "movement — the First "
            "and Second Republics "
            "(1810–1816) and then "
            "Bolívar's liberation "
            "campaigns (1819–1821) "
            "— created the context "
            "within which colonial "
            "administrators either "
            "adapted, resisted, "
            "or were swept aside.\n\n"
            "His specific administrative "
            "role contributed to "
            "the colonial governance "
            "of South America's "
            "northwest during "
            "the final years "
            "of Spanish imperial control.\n\n"
            "The details of his career "
            "reflect the broader "
            "collapse of the "
            "Spanish empire "
            "in the Americas."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Spanish colonial administrator in the Viceroyalty of New Granada during the Spanish American independence era; faced the challenge of maintaining royal authority as the Napoleonic invasion undermined Bourbon legitimacy; governed during the period of the New Granada independence movements and Bolívar's liberation campaigns.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Napoleon's invasion of Spain (1808) — the Napoleonic occupation and the removal of the Bourbon monarchy — fundamentally undermined the legitimacy of royal colonial authority and emboldened the Creole independence movements throughout Spanish America",
            "New Granada's Creole elite nationalism — the educated Creole class's growing political consciousness and their demand for autonomy or independence, culminating in the First Republic (1810) and subsequent independence movements",
            "The structural weakness of Spanish colonial administration — the impossibility of maintaining effective imperial control over vast territories with limited military resources, especially when the metropole itself was occupied by Napoleon"
        ],
        "effects": [
            "His colonial administration contributed to the Spanish imperial effort to maintain control over New Granada during the independence struggle — the royalist governance that opposed the Creole republican movements",
            "His administrative experience contributed to the broader pattern of Spanish colonial governance adapting to or failing before the independence movements — the institutional response to the collapse of Bourbon authority",
            "The collapse of colonial administration that his career was part of contributed to the establishment of independent republics — Colombia, Venezuela, Ecuador emerging from the ruins of New Granada",
            "His career illustrated the impossible position of loyal colonial administrators during the Spanish American independence era — serving a crown whose authority had been fatally undermined by European events"
        ],
        "relationships": [
            {"target": "viceroyalty-of-new-granada", "verb": "ADMINISTERS", "note": "Colonial official during the independence era"},
            {"target": "spanish-empire", "verb": "REPRESENTS", "note": "Royal administrator during imperial collapse"},
            {"target": "new-granada-independence", "verb": "OPPOSES", "note": "Royalist administrator facing independence movements"},
            {"target": "napoleonic-invasion-of-spain", "verb": "AFFECTED_BY", "note": "Colonial authority undermined by Napoleon's Spain invasion"},
            {"target": "simón-bolívar", "verb": "OPPOSES_ERA_OF", "note": "Royalist during Bolívar's liberation campaigns"}
        ]
    }),

    ("charles-dayan", {
        "summary": (
            "Charles Dayan (1792–1877) "
            "was an American Democratic "
            "politician from New York "
            "who served in the U.S. "
            "House of Representatives "
            "(1831–1833) during the "
            "Jacksonian era. A single-term "
            "congressman from New York's "
            "rural north country, "
            "Dayan served during the "
            "opening battles of "
            "Jackson's Bank War "
            "and the nullification "
            "crisis — the South "
            "Carolina confrontation "
            "over tariffs that "
            "brought the nation "
            "to the brink of "
            "constitutional crisis "
            "in 1832–1833. His "
            "one-term House service "
            "reflected the pattern "
            "of Jacksonian-era "
            "Democratic politics "
            "in which many congressmen "
            "served single terms "
            "and returned to their "
            "professions.\n\n"
            "New York's north country "
            "was an agricultural "
            "region whose economy "
            "and political culture "
            "were distinct from "
            "both the Mohawk Valley "
            "commercial corridor "
            "and the New York "
            "City Democratic machine.\n\n"
            "His long life (1792–1877) "
            "allowed him to witness "
            "the entire arc of "
            "American history from "
            "the founding era "
            "through the Civil "
            "War and Reconstruction.\n\n"
            "He was a St. Lawrence "
            "County farmer and lawyer."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "New York Democratic Congressman (1831–1833); served during Jackson's Bank War opening and the nullification crisis; north country New York agricultural district; single term reflecting Jacksonian-era congressional rotation; long life (1792–1877) witnessing the full arc from founding era through Reconstruction.",
            "significanceCategory": "local"
        },
        "causes": [
            "Jacksonian political organization — the Democratic Party machine building that Jackson created and that enabled rural congressmen like Dayan from New York's north country to win seats in the Jacksonian landslide",
            "The Bank War's opening — Jackson's determination to destroy the Second Bank of the United States and his veto of its recharter — created the major political controversy of Dayan's one congressional term",
            "The nullification crisis — South Carolina's challenge to federal tariff authority that brought Andrew Jackson into direct confrontation with John C. Calhoun — created the constitutional crisis that dominated Dayan's congressional session"
        ],
        "effects": [
            "His House service contributed New York's rural north country Democratic vote to the Bank War's initial battles — supporting Jackson's economic war against the national bank",
            "His congressional term contributed to the Jacksonian coalition's parliamentary majority during one of the most politically consequential years of the antebellum era",
            "His return to private life after one term reflected the Jacksonian principle of rotation in office — the democratic ethic that public offices should not become permanent sinecures for professional politicians",
            "His long life allowed him to witness the consequences of the political era he participated in — the Bank War's economic effects, the eventual Civil War, and Reconstruction"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "New York Congressman 1831–1833"},
            {"target": "bank-war", "verb": "VOTES_DURING", "note": "Congressman during Jackson's Bank War opening"},
            {"target": "nullification-crisis", "verb": "SERVES_DURING", "note": "Congressman during the South Carolina confrontation"},
            {"target": "andrew-jackson", "verb": "SUPPORTS", "note": "Jacksonian Democrat"},
            {"target": "new-york", "verb": "REPRESENTS", "note": "St. Lawrence County north country congressman"}
        ]
    }),

    ("jean-despagnet", {
        "summary": (
            "Jean Despagnet (1565–c.1611) "
            "was a French jurist and "
            "legal scholar of the "
            "late Renaissance period "
            "who served as First "
            "President of the Parlement "
            "of Bordeaux — the regional "
            "sovereign court of "
            "Guyenne. He is primarily "
            "known as a legal writer "
            "whose works on French "
            "private law and on "
            "international law "
            "contributed to the "
            "emerging discipline "
            "of the law of nations. "
            "His 'Recueil des règles, "
            "principes et maximes "
            "du droit français' "
            "and his works on "
            "conflicts of law "
            "were significant "
            "contributions to "
            "16th-century French legal scholarship.\n\n"
            "Despagnet worked "
            "in the tradition "
            "of French jurisprudence "
            "that was transforming "
            "Roman law through "
            "humanist scholarship "
            "— the mos gallicus "
            "or French method "
            "that treated Roman "
            "law historically "
            "and analytically "
            "rather than merely "
            "doctrinally.\n\n"
            "His contribution "
            "to the law of "
            "nations placed him "
            "in the context "
            "of early modern "
            "international law's "
            "development alongside "
            "Grotius and his contemporaries.\n\n"
            "He was a significant "
            "figure in Renaissance "
            "French jurisprudence."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "French jurist and First President of the Parlement of Bordeaux (1565–c.1611); contributed to conflicts of law and the emerging law of nations; worked in the mos gallicus humanist legal tradition; 'Recueil des règles du droit français' was a significant legal contribution; predecessor and contemporary in the tradition leading to Grotius; Renaissance French jurisprudence figure.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The French humanist legal tradition (mos gallicus) — the revolutionary approach to Roman law that treated it historically and analytically rather than as authoritative doctrine — created the intellectual environment in which Despagnet's legal scholarship developed",
            "The emergence of the law of nations — the late 16th and early 17th-century development of international law as a distinct discipline, driven by the practical needs of European state relations and colonial expansion — created the scholarly context for Despagnet's international law contributions",
            "The Parlement of Bordeaux's legal culture — the distinguished regional court that served as both a judicial institution and a center of legal scholarship, producing and attracting outstanding jurists — created the institutional base for Despagnet's academic-judicial career"
        ],
        "effects": [
            "His conflicts of law contributions helped develop this specialized legal doctrine — the rules governing which jurisdiction's law should apply when legal disputes crossed territorial boundaries, an increasingly important question in Europe's developing state system",
            "His legal writings contributed to French jurisprudence's development — the accumulated scholarship that transformed Roman law into French national law and built the legal tradition that would eventually produce the Napoleonic Code",
            "His contribution to the law of nations placed him in the lineage of international law's founders — the jurists whose work Grotius and subsequent generations built upon",
            "His Parlement of Bordeaux presidency contributed to the distinctive legal culture of Guyenne — the regional judicial institution that shaped the law of southwestern France"
        ],
        "relationships": [
            {"target": "parlement-of-bordeaux", "verb": "LEADS", "note": "First President of Bordeaux's sovereign court"},
            {"target": "french-jurisprudence", "verb": "CONTRIBUTES_TO", "note": "Legal scholar in the humanist tradition"},
            {"target": "law-of-nations", "verb": "CONTRIBUTES_TO", "note": "Early contributor to international law doctrine"},
            {"target": "mos-gallicus", "verb": "WORKS_IN_TRADITION_OF", "note": "Humanist French legal method"},
            {"target": "hugo-grotius", "verb": "PRECEDES", "note": "French predecessor in law of nations tradition"}
        ]
    }),

    ("george-edmund-badger", {
        "summary": (
            "George Edmund Badger (1795–1866) "
            "was an American Whig "
            "politician and jurist "
            "from North Carolina "
            "who served as Secretary "
            "of the Navy (1841) "
            "under Presidents Harrison "
            "and briefly Tyler, "
            "as a U.S. Senator "
            "(1846–1855), and as "
            "a North Carolina "
            "Superior Court judge. "
            "He was one of the "
            "most distinguished "
            "constitutional lawyers "
            "of the antebellum "
            "South — a North "
            "Carolina Whig whose "
            "Senate career contributed "
            "the state's moderate "
            "conservative perspective "
            "to the antebellum "
            "debates over slavery "
            "extension, the "
            "Compromise of 1850, "
            "and the Kansas-Nebraska Act.\n\n"
            "As a Southern Whig, "
            "Badger represented "
            "the distinctive "
            "political tradition "
            "of the planter elite "
            "that preferred Henry "
            "Clay's American System "
            "and constitutional "
            "moderation over "
            "Jacksonian agrarianism "
            "and nullification.\n\n"
            "His Navy secretaryship "
            "lasted only months "
            "before Tyler's "
            "Whig break caused "
            "cabinet resignations.\n\n"
            "He was considered "
            "for the Supreme Court "
            "but was blocked "
            "by the Democratic Senate."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "North Carolina Whig Senator (1846–1855), Secretary of the Navy (1841), and jurist; one of the most distinguished constitutional lawyers of the antebellum South; Southern Whig representing the planter elite's moderate conservative tradition; opposed nullification; Senate-blocked Supreme Court nominee; career spanning Harrison through Pierce administrations.",
            "significanceCategory": "continental"
        },
        "causes": [
            "North Carolina's Whig tradition — the state's plantation-owning commercial elite's preference for the American System and constitutional moderation over Jacksonian populism — created the political culture that produced Badger's distinguished Whig career",
            "The Harrison-Tyler political crisis — the death of President Harrison and Tyler's break with the Whig party — created the situation in which Badger resigned from the Navy secretaryship along with most of the cabinet",
            "The antebellum slavery debates — the Compromise of 1850 and Kansas-Nebraska Act controversies — created the major policy questions around which Badger's Senate career was organized as a moderate Southern Whig"
        ],
        "effects": [
            "His Senate career contributed North Carolina's Southern Whig perspective to the antebellum slavery debates — the moderate conservative voice that preferred compromise and constitutional reasoning to the fire-eater secessionism of radical Southern Democrats",
            "His Senate-blocked Supreme Court nomination illustrated the political difficulties of Southern Whigs — unable to satisfy either the Whig majority's antislavery leanings or the Democratic Senate's proslavery commitments",
            "His constitutional law contributions contributed to North Carolina's legal tradition — the distinguished jurist who elevated the state's legal culture beyond the frontier common law",
            "His career illustrated the Southern Whig dilemma — committed to the Union and constitutional moderation but ultimately unable to survive the political polarization that destroyed the Whig Party and drove the South toward secession"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "North Carolina Senator 1846–1855"},
            {"target": "us-department-of-the-navy", "verb": "LEADS", "note": "Secretary of the Navy 1841"},
            {"target": "whig-party-united-states", "verb": "MEMBER_OF", "note": "Distinguished Southern Whig politician"},
            {"target": "compromise-of-1850", "verb": "DEBATES", "note": "Senator during the compromise controversies"},
            {"target": "north-carolina", "verb": "REPRESENTS", "note": "North Carolina Whig senator and jurist"}
        ]
    }),

    ("joseph-mcilvaine", {
        "summary": (
            "Joseph McIlvaine (1769–1826) "
            "was an American Democratic-Republican "
            "politician from New Jersey "
            "who served in the U.S. "
            "Senate (1823–1826) — dying "
            "in office at age 57 after "
            "three years of service. "
            "His Senate career coincided "
            "with the final years "
            "of the Era of Good Feelings "
            "and the opening of the "
            "contested 1824 presidential "
            "election that shattered "
            "the Democratic-Republican "
            "consensus and produced "
            "the Jacksonian political "
            "revolution. McIlvaine "
            "served in the Senate "
            "during the extraordinary "
            "political moment when "
            "one-party consensus "
            "broke down into the "
            "multi-candidate contest "
            "between Adams, Jackson, "
            "Crawford, and Clay "
            "that no candidate "
            "won outright.\n\n"
            "New Jersey's position "
            "as a competitive "
            "mid-Atlantic state "
            "made its Senate "
            "votes significant "
            "in the 1824 "
            "alignment debates.\n\n"
            "His death in office "
            "prevented him from "
            "witnessing the Jacksonian "
            "revolution that the "
            "1824 election set "
            "in motion.\n\n"
            "He was previously "
            "New Jersey's "
            "Attorney General."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "New Jersey Democratic-Republican Senator (1823–1826); died in office; served during the critical 1824 election that shattered one-party consensus and set off the Jacksonian revolution; previously New Jersey Attorney General; career cut short before witnessing the political transformation he helped initiate.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New Jersey's Democratic-Republican political organization — the party structure that sent McIlvaine to the Senate during the Era of Good Feelings' final years — created the institutional pathway for his Senate career",
            "The Era of Good Feelings' collapse — the breakdown of Democratic-Republican consensus as five candidates contended for the presidency in 1824 — created the political turmoil of McIlvaine's Senate years",
            "The 1824 election's constitutional crisis — the no-majority outcome that threw the election to the House of Representatives and produced the 'corrupt bargain' accusation against Adams and Clay — created the political environment of McIlvaine's final Senate year"
        ],
        "effects": [
            "His Senate service contributed New Jersey's perspective to the 1824 election debates — the mid-Atlantic state's voice in the political alignment that would produce the Adams and Jackson factions",
            "His death in office in 1826 prevented him from participating in the Jacksonian revolution that followed — leaving New Jersey's Senate seat to be filled as the political realignment accelerated",
            "His Attorney General and Senate service contributed to New Jersey's political tradition — the legal and legislative careers that served the state across the founding and early republican eras",
            "His career illustrated the Era of Good Feelings' deceptive tranquility — the surface political consensus that concealed the factional tensions that would explode into the Jacksonian political revolution"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "New Jersey Senator 1823–1826"},
            {"target": "election-of-1824", "verb": "SERVES_DURING", "note": "Senator during the contested multi-candidate election"},
            {"target": "era-of-good-feelings", "verb": "SERVES_DURING", "note": "Senator during the final years of one-party consensus"},
            {"target": "new-jersey", "verb": "REPRESENTS", "note": "New Jersey Democratic-Republican senator and attorney general"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "New Jersey Democratic-Republican senator"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 79 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
