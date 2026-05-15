#!/usr/bin/env python3
"""
Batch 86 — 8 entities: James Iver McKay, John Wales, Robert B. Dickey,
Ephraim H. Foster, Claude-Ambroise Régnier, Jonathan Robinson,
John Ruggles, Judah Dana
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

    ("james-iver-mckay", {
        "summary": (
            "James Iver McKay (1793–1853) "
            "was an American Democratic "
            "politician from North Carolina "
            "who served in the U.S. "
            "House of Representatives "
            "(1831–1849) — eighteen "
            "continuous years "
            "making him one of "
            "North Carolina's "
            "most prominent "
            "antebellum congressmen. "
            "Chairman of the "
            "powerful House Ways "
            "and Means Committee "
            "(1843–1847) during "
            "the Polk administration, "
            "McKay was a central "
            "figure in the "
            "Walker Tariff of 1846 — "
            "the significant "
            "reduction of protective "
            "tariffs that was "
            "a major Democratic "
            "economic policy achievement. "
            "The Walker Tariff "
            "lowered rates from "
            "the Whig-era levels "
            "and reflected "
            "Southern and "
            "Democratic free-trade "
            "preferences over "
            "Northern protective interests.\n\n"
            "His Ways and Means "
            "chairmanship during "
            "the Mexican-American "
            "War also involved "
            "managing war financing.\n\n"
            "His eighteen years "
            "represented North "
            "Carolina's Democratic "
            "agricultural interests "
            "consistently.\n\n"
            "He was a Bladen "
            "County lawyer-planter."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "North Carolina Democratic Congressman (1831–1849); Chairman of Ways and Means (1843–1847); key figure in the Walker Tariff of 1846 — a major Democratic free-trade achievement; managed war financing during the Mexican-American War; eighteen continuous House years representing Southern Democratic agricultural interests.",
            "significanceCategory": "regional"
        },
        "causes": [
            "North Carolina's Democratic planter-farmer political culture — the state's agricultural economy that opposed protective tariffs as raising prices on imported goods that planters consumed — created McKay's long career as a free-trade Democratic congressman",
            "The Polk administration's free-trade mandate — the 1844 Democratic platform's commitment to reducing Whig-era tariffs — created the political moment for McKay's Ways and Means chairmanship and the Walker Tariff",
            "The Southern Democratic coalition — the alliance of Southern planters and Northern urban workers that dominated Democratic politics and consistently favored lower tariffs over Northern industrial protection — provided the legislative majority for the Walker Tariff"
        ],
        "effects": [
            "His Ways and Means chairmanship produced the Walker Tariff of 1846 — a significant reduction of protective tariff rates that governed U.S. trade policy for over a decade",
            "His eighteen House years contributed North Carolina's voice to the antebellum Democratic agenda — territorial expansion, free trade, and states' rights",
            "His war financing work during the Mexican-American War contributed to the fiscal management of one of the most consequential conflicts in American territorial expansion",
            "His free-trade championship contributed to the Democratic economic tradition that differentiated the party from Whig protectionism — a distinction that would persist in American politics for generations"
        ],
        "relationships": [
            {"target": "us-house-ways-and-means-committee", "verb": "CHAIRS", "note": "Ways and Means Chairman 1843–1847"},
            {"target": "walker-tariff-1846", "verb": "LEGISLATES", "note": "Key architect of the 1846 tariff reduction"},
            {"target": "james-k-polk", "verb": "SERVES_UNDER", "note": "Congressional ally of the Polk administration"},
            {"target": "north-carolina", "verb": "REPRESENTS", "note": "Eighteen-year North Carolina Democratic congressman"},
            {"target": "mexican-american-war", "verb": "FINANCES", "note": "Ways and Means chair during war financing"}
        ]
    }),

    ("john-wales", {
        "summary": (
            "John Wales (1783–1863) "
            "was an American Whig "
            "politician from Delaware "
            "who served briefly "
            "in the U.S. Senate "
            "(1849–1851), appointed "
            "to fill a vacancy. "
            "Delaware's political "
            "scene was dominated "
            "by two great families — "
            "the Bayards and "
            "others — with "
            "the state's tiny "
            "electorate making "
            "it a uniquely "
            "personal political "
            "arena where family "
            "connections and "
            "business relationships "
            "mattered as much "
            "as party labels. "
            "Wales served "
            "during the Fillmore "
            "administration "
            "— the period after "
            "Taylor's death "
            "when the Compromise "
            "of 1850's various "
            "measures were "
            "being legislated. "
            "Delaware's position "
            "as a border slave "
            "state with strong "
            "Northern economic "
            "ties made its "
            "senators important "
            "swing votes "
            "on sectional issues.\n\n"
            "His brief appointed "
            "term placed him "
            "at the center "
            "of the Compromise "
            "of 1850 debates "
            "— the critical "
            "moment when the "
            "sectional crisis "
            "was temporarily resolved.\n\n"
            "He was a Wilmington "
            "Delaware businessman "
            "and Whig politician.\n\n"
            "He was a figure "
            "of Delaware's "
            "Whig establishment."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Delaware Whig Senator (1849–1851), appointed to fill vacancy; served during the Compromise of 1850 debates; Delaware border-state swing vote; Fillmore administration period; Wilmington businessman representing Delaware's mercantile Whig establishment.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Delaware's Whig establishment — the state's merchant and professional elite whose commercial economy aligned with Whig protectionism and national development policies — created the political environment for Wales's Senate appointment",
            "The vacancy that created Wales's appointment — a sitting senator's death or resignation requiring the governor to appoint a replacement — created the specific mechanism of his Senate service",
            "The Compromise of 1850's sectional crisis — the divisive set of measures over slavery, territorial organization, and the Fugitive Slave Act that required every senator's vote — created the critical political context of Wales's brief term"
        ],
        "effects": [
            "His Senate vote contributed to the Compromise of 1850 legislative process — the border-state Whig perspective on the measures that temporarily resolved the sectional crisis",
            "His appointed service contributed to the continuity of Delaware's Senate representation — filling the gap until an election could produce a new full-term senator",
            "His career contributed to Delaware's Whig merchant-class political tradition — the commercial interests that defined the small state's political culture",
            "His brief Senate tenure illustrated the appointed senator's role — the placeholder who served in critical historical moments without having been elected to full terms"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Delaware Senator 1849–1851 by appointment"},
            {"target": "compromise-of-1850", "verb": "VOTES_ON", "note": "Senator during the critical Compromise debates"},
            {"target": "whig-party-united-states", "verb": "MEMBER_OF", "note": "Delaware Whig senator"},
            {"target": "millard-fillmore", "verb": "SERVES_UNDER", "note": "Senator during the Fillmore administration"},
            {"target": "delaware", "verb": "REPRESENTS", "note": "Border-state senator representing Delaware's Whig establishment"}
        ]
    }),

    ("robert-b-dickey", {
        "summary": (
            "Robert B. Dickey "
            "(1786–1869) was an "
            "American Democratic "
            "politician from "
            "Pennsylvania who "
            "served in the U.S. "
            "House of Representatives "
            "(1853–1855) during "
            "the Pierce administration. "
            "Pennsylvania's "
            "Democratic Party "
            "in the 1850s "
            "was being torn "
            "apart by the sectional "
            "crisis — the state's "
            "industrial workers "
            "and protective "
            "tariff interests "
            "aligning with the "
            "North while "
            "the party's "
            "Buchanan wing "
            "sought compromise "
            "with the South. "
            "Dickey served "
            "during the Congress "
            "that followed "
            "the Compromise "
            "of 1850 and preceded "
            "the Kansas-Nebraska Act — "
            "a period of "
            "deceptive calm "
            "before the sectional "
            "storm broke. "
            "Pennsylvania's "
            "position as the "
            "nation's largest "
            "iron-producing state "
            "made its congressional "
            "delegation central "
            "to tariff debates.\n\n"
            "His two-year "
            "House term contributed "
            "Pennsylvania's "
            "Democratic perspective "
            "during the Pierce presidency.\n\n"
            "He was an Allegheny "
            "County Pennsylvania "
            "lawyer.\n\n"
            "He served during "
            "the last phase "
            "of antebellum "
            "Democratic dominance."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Pennsylvania Democratic Congressman (1853–1855) during the Pierce administration; served during the calm before the Kansas-Nebraska Act storm; Pennsylvania's iron-industry tariff debates; Allegheny County lawyer representing western Pennsylvania's Democratic interests.",
            "significanceCategory": "local"
        },
        "causes": [
            "Pennsylvania's Democratic Party organization — the state machine that managed the complex coalition of immigrant workers, Catholic voters, and anti-tariff constituencies in Pennsylvania's cities — created the political infrastructure for Dickey's nomination and election",
            "The post-Compromise calm — the deceptive period of relative sectional quiet between 1850 and 1854 when Democrats could still win in Pennsylvania without being forced to choose sides on slavery — created the political window for Dickey's election",
            "Pennsylvania's western district politics — Allegheny County's industrial and legal community that generated Democratic candidates — provided the local context for Dickey's congressional career"
        ],
        "effects": [
            "His House service contributed Pennsylvania's Democratic votes to the Pierce administration's agenda — the tariff, internal improvements, and territorial debates of the 33rd Congress",
            "His brief term contributed to the documentation of Pennsylvania's Democratic representation before the party fractured on sectional lines",
            "His career illustrated the typical pattern of single-term Pennsylvania Democratic congressmen in the antebellum era — elected during favorable political moments and serving briefly before party realignment",
            "His Pennsylvania Democratic career contributed to the pre-Republican period of Allegheny County politics — the region that would become reliably Republican after 1854"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Pennsylvania Congressman 1853–1855"},
            {"target": "franklin-pierce", "verb": "SERVES_DURING", "note": "Congressman during Pierce's presidency"},
            {"target": "democratic-party-united-states", "verb": "MEMBER_OF", "note": "Pennsylvania Democrat"},
            {"target": "pennsylvania", "verb": "REPRESENTS", "note": "Western Pennsylvania congressman"},
            {"target": "kansas-nebraska-act", "verb": "SERVES_BEFORE", "note": "Congressman during the antebellum sectional calm"}
        ]
    }),

    ("ephraim-h-foster", {
        "summary": (
            "Ephraim Hubbard Foster "
            "(1794–1854) was an "
            "American Whig politician "
            "from Tennessee who "
            "served in the U.S. "
            "Senate (1838–1839 "
            "and 1843–1845) and "
            "in the Tennessee "
            "state legislature. "
            "A Tennessee Whig "
            "— which meant "
            "opposing Andrew Jackson "
            "in Jackson's own state "
            "— Foster was part "
            "of the exceptional "
            "Whig presence in "
            "Tennessee that "
            "the Deep South "
            "lacked. Foster "
            "was a protégé of "
            "John Bell and "
            "an ally of John "
            "J. Crittenden in "
            "the Tennessee "
            "Whig network. "
            "Tennessee's split "
            "between Jacksonian "
            "and Whig politics "
            "— unusual in "
            "the South — "
            "reflected the "
            "state's division "
            "between Middle "
            "Tennessee's planter "
            "aristocracy and "
            "East Tennessee's "
            "Unionist mountain communities.\n\n"
            "His two non-consecutive "
            "Senate terms "
            "contributed Tennessee's "
            "Whig opposition "
            "voice to the "
            "Van Buren and "
            "Tyler administrations.\n\n"
            "He was a Nashville "
            "lawyer and Tennessee "
            "Whig leader.\n\n"
            "He helped create "
            "the Whig Party "
            "in Tennessee."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Tennessee Whig Senator (1838–1839 and 1843–1845); helped create the Whig Party in Tennessee — unusual in the South; Nashville lawyer opposing Jackson in his own state; ally of John Bell and John J. Crittenden; Tennessee's division between Jacksonian planters and Unionist mountain communities.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Anti-Jackson Tennessee politics — the significant minority of Tennesseans who opposed Jackson despite his origin in the state, particularly in Middle Tennessee's planter aristocracy that felt Jackson's democracy threatened property and order — created the political constituency for Foster's Whig career",
            "John Bell's Tennessee Whig organization — the network that Bell led against Jackson's Democratic machine in Tennessee — provided the institutional framework for Foster's Senate elections",
            "Tennessee's geographic political division — the state's contrast between the Jackson-supporting frontier west and the more conservative middle and east — created the political space for a viable Tennessee Whig party"
        ],
        "effects": [
            "His Senate service contributed Tennessee's Whig opposition to the Van Buren and Tyler administrations — the Southern Whig perspective on economic policy, Indian removal, and states' rights",
            "His Whig party-building work contributed to creating and sustaining the party in Tennessee — one of the few Southern states with a genuine two-party system in the antebellum era",
            "His career contributed to the tradition of Tennessee Unionist conservatism — the strain that would make East Tennessee strongly Unionist during the Civil War",
            "His alliance with Bell contributed to Tennessee's Whig-Constitutional Union tradition — the political culture that kept Tennessee the last Southern state to consider secession in 1861"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Tennessee Senator 1838–1839 and 1843–1845"},
            {"target": "whig-party-united-states", "verb": "HELPS_BUILD", "note": "Helped create Tennessee's Whig Party"},
            {"target": "john-bell", "verb": "ALLIED_WITH", "note": "Tennessee Whig network ally of John Bell"},
            {"target": "tennessee", "verb": "REPRESENTS", "note": "Nashville lawyer opposing Jackson in his home state"},
            {"target": "martin-van-buren", "verb": "OPPOSES", "note": "Whig Senate opposition during Van Buren presidency"}
        ]
    }),

    ("claude-ambroise-régnier", {
        "summary": (
            "Claude-Ambroise Régnier "
            "(1746–1814) was "
            "a French jurist "
            "and statesman who "
            "served Napoleon "
            "as Minister of "
            "Justice (1802–1813) "
            "and was created "
            "Duke of Massa. "
            "One of Napoleon's "
            "most trusted legal "
            "administrators, "
            "Régnier oversaw "
            "the Justice Ministry "
            "during the critical "
            "period when the "
            "Napoleonic Code "
            "was being implemented "
            "and when Napoleon's "
            "imperial judiciary "
            "was being constructed. "
            "The Ministry of "
            "Justice under "
            "Régnier managed "
            "the appointment "
            "of judges, the "
            "organization of "
            "courts, and the "
            "supervision of "
            "the legal profession "
            "across an empire "
            "that stretched "
            "from Iberia to Poland.\n\n"
            "His eleven-year "
            "Justice Ministry "
            "was one of the "
            "longest in Napoleonic "
            "service — overseeing "
            "the implementation "
            "of the Code Civil, "
            "the Code of Criminal "
            "Procedure, and "
            "the Penal Code.\n\n"
            "He was made "
            "a Senator and "
            "elevated to the "
            "imperial nobility.\n\n"
            "He was a key "
            "architect of "
            "Napoleonic judicial governance."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Napoleon's Minister of Justice (1802–1813) and Duke of Massa; eleven-year ministry overseeing implementation of the Napoleonic Code, Code of Criminal Procedure, and Penal Code; organized the judiciary across Napoleon's empire; Senator and imperial noble; one of the longest-serving and most trusted Napoleonic ministers.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Napoleon's state-building project — the First Consul's and then Emperor's drive to create coherent institutions for the new French state and empire — required a trusted jurist to manage the Justice Ministry through the critical codification period",
            "The Napoleonic codification effort — the series of legal codes (Civil, Criminal Procedure, Commercial, Penal) that Napoleon commissioned — required a Justice Ministry that could coordinate the drafting commissions, secure legislative approval, and implement the codes",
            "Régnier's legal expertise and political reliability — his combination of juristic competence and personal loyalty to Napoleon — made him the ideal minister to oversee the judiciary across an expanding empire"
        ],
        "effects": [
            "His eleven-year Justice Ministry oversaw the implementation of the Napoleonic codes — the legal framework that transformed France's law and spread across Europe with French conquest",
            "His judicial organization across the empire contributed to the administrative infrastructure that maintained French imperial governance — appointing judges, organizing courts, and ensuring legal uniformity",
            "His ministry contributed to the Napoleonic noble creation — building a new imperial aristocracy from the revolution's survivors and Napoleon's talented administrators",
            "His long service contributed to the stability of Napoleonic legal institutions — the continuity of the Justice Ministry through the empire's greatest years and its first defeats"
        ],
        "relationships": [
            {"target": "napoleon-i", "verb": "SERVES_UNDER", "note": "Minister of Justice 1802–1813"},
            {"target": "napoleonic-code", "verb": "IMPLEMENTS", "note": "Justice Ministry overseeing Code Civil implementation"},
            {"target": "napoleonic-empire", "verb": "ADMINISTERS", "note": "Organized judiciary across the empire"},
            {"target": "duke-of-massa", "verb": "ELEVATED_TO", "note": "Created Duke of Massa by Napoleon"},
            {"target": "french-imperial-judiciary", "verb": "BUILDS", "note": "Constructed Napoleon's imperial court system"}
        ]
    }),

    ("jonathan-robinson", {
        "summary": (
            "Jonathan Robinson (1756–1819) "
            "was an American "
            "Democratic-Republican "
            "politician from Vermont "
            "who served in the "
            "U.S. Senate (1807–1815) — "
            "eight years spanning "
            "the Jefferson second "
            "term, the Madison "
            "era, and the War "
            "of 1812. Vermont's "
            "political identity "
            "was complex — "
            "the state was "
            "both New England "
            "(with all the "
            "Federalist commercial "
            "and religious tendencies "
            "that implied) "
            "and frontier "
            "(with the democratic "
            "populism of settlers "
            "recently independent "
            "from both New York "
            "and New Hampshire "
            "land grant disputes). "
            "Robinson navigated "
            "Vermont's divided "
            "politics through "
            "his eight Senate years "
            "— serving through "
            "the Embargo, "
            "the Non-Intercourse Acts, "
            "and the War of 1812 "
            "while Vermont's "
            "geography made "
            "it one of the "
            "most active smuggling "
            "states on the "
            "Canadian border.\n\n"
            "Vermont's famous "
            "Canadian border "
            "smuggling during "
            "the Embargo illustrated "
            "the state's pragmatic "
            "frontier economics.\n\n"
            "He had previously "
            "served as Vermont's "
            "Chief Justice.\n\n"
            "He was a Bennington "
            "County lawyer."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Vermont Democratic-Republican Senator (1807–1815) and former Chief Justice; eight Senate years spanning the Embargo, Non-Intercourse Acts, and War of 1812; Vermont's divided New England/frontier politics; served during Vermont's notorious Canadian border smuggling under the Embargo; Bennington County lawyer.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Vermont's political complexity — the state's frontier democratic culture that made it receptive to Jeffersonian Republican ideals despite its New England location — created the political identity of Robinson's Democratic-Republican Senate career",
            "The Jefferson-Madison commercial restriction policies — the Embargo and Non-Intercourse Acts that Vermont's border geography made practically impossible to enforce — created the recurring tensions Robinson navigated as Vermont's senator",
            "Robinson's judicial reputation — his prior service as Vermont Chief Justice — provided the professional credibility that made him a credible Senate choice for a state that valued legal expertise in its federal representatives"
        ],
        "effects": [
            "His Senate service contributed Vermont's Democratic-Republican voice to the Jefferson and Madison era debates — the Green Mountain State's perspective on commerce, embargo, and war",
            "His navigation of Vermont's Embargo tensions contributed to the practical compromise that a senator from a smuggling border state required — acknowledging the law while accommodating constituents who violated it",
            "His Chief Justice experience contributed to the legal quality of Vermont's Senate representation — the judicial perspective on constitutional questions that senators with legal backgrounds brought",
            "His War of 1812 service contributed to Vermont's conflicted wartime politics — the state that geographically could not easily sustain the war's northern frontier operations"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Vermont Senator 1807–1815"},
            {"target": "vermont-supreme-court", "verb": "LEADS", "note": "Former Vermont Chief Justice"},
            {"target": "embargo-act", "verb": "SERVES_DURING", "note": "Vermont border-state senator during the Embargo"},
            {"target": "war-of-1812", "verb": "SERVES_DURING", "note": "Vermont senator during the northern border war"},
            {"target": "vermont", "verb": "REPRESENTS", "note": "Frontier Democratic-Republican from New England Vermont"}
        ]
    }),

    ("john-ruggles", {
        "summary": (
            "John Ruggles (1789–1874) "
            "was an American "
            "Democratic politician "
            "from Maine who "
            "served in the U.S. "
            "Senate (1835–1841) "
            "and holds a unique "
            "distinction: he "
            "is generally credited "
            "as the primary founder "
            "of the U.S. Patent "
            "Office's modern system — "
            "the man who "
            "introduced legislation "
            "that created the "
            "Patent Office in "
            "its modern form "
            "in 1836 and was "
            "awarded U.S. Patent "
            "No. 1 under "
            "the new system. "
            "The 1836 Patent Act "
            "— one of the most "
            "consequential pieces "
            "of legislation in "
            "American economic "
            "history — established "
            "the examination "
            "system that replaced "
            "the previous "
            "registration system, "
            "ensuring that patents "
            "were only granted "
            "for genuine inventions.\n\n"
            "The American patent "
            "system he helped "
            "create became "
            "one of the cornerstones "
            "of American economic "
            "innovation and "
            "technological leadership.\n\n"
            "He was also "
            "a Maine inventor "
            "himself — one "
            "of the few senators "
            "who held a patent.\n\n"
            "He was a Thomaston "
            "Maine lawyer and inventor."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Maine Democratic Senator (1835–1841); primary founder of the modern U.S. Patent Office — introduced the Patent Act of 1836 establishing the examination system; awarded U.S. Patent No. 1 under the new system; his patent reform contributed to American technological innovation for generations; Thomaston Maine lawyer-inventor.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The failures of the old patent registration system — the 1790 and 1793 Patent Acts that granted patents without examination, leading to overlapping, invalid, and unenforceable patents that suppressed rather than encouraged innovation — created the urgent need for reform that Ruggles addressed",
            "America's industrial takeoff — the growing number of inventors and innovations in the early 19th century that overwhelmed the existing system and demanded a more rigorous, credible patent grant process — created the political urgency for Ruggles's patent reform",
            "Ruggles's own experience as an inventor — his personal understanding of the patent system's deficiencies from the inventor's perspective — motivated his legislative reform and gave it practical credibility"
        ],
        "effects": [
            "His Patent Act of 1836 created the modern U.S. Patent Office examination system — the institutional foundation for American intellectual property protection that enabled generations of technological innovation",
            "His reform distinguished American patent law from the old registration system — establishing the principle that patents must be examined and only granted for genuinely novel inventions",
            "The patent system he established contributed to America's extraordinary technological development — the legal infrastructure that incentivized invention by ensuring inventors could protect and profit from their innovations",
            "U.S. Patent No. 1 he received became a historical symbol — the first patent under the modern system that would eventually grant millions of patents representing the full breadth of American ingenuity"
        ],
        "relationships": [
            {"target": "us-patent-office", "verb": "FOUNDS_MODERN", "note": "Primary architect of the Patent Act of 1836 and modern patent system"},
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Maine Senator 1835–1841"},
            {"target": "patent-act-1836", "verb": "INTRODUCES", "note": "Principal legislative architect of the 1836 patent reform"},
            {"target": "american-innovation-system", "verb": "ENABLES", "note": "Patent system that underpinned American technological leadership"},
            {"target": "maine", "verb": "REPRESENTS", "note": "Maine Democratic senator and inventor"}
        ]
    }),

    ("judah-dana", {
        "summary": (
            "Judah Dana (1772–1845) "
            "was an American "
            "Democratic-Republican "
            "politician from Maine "
            "who served in the "
            "U.S. Senate (1836–1837), "
            "appointed to fill "
            "a vacancy. Maine's "
            "early statehood "
            "politics were "
            "shaped by the "
            "state's 1820 separation "
            "from Massachusetts — "
            "part of the Missouri "
            "Compromise that "
            "admitted Missouri "
            "as a slave state "
            "and Maine as "
            "a free state "
            "to preserve the "
            "Senate's sectional "
            "balance. As one "
            "of Maine's early "
            "senators, Dana "
            "served in the "
            "Jackson-Van Buren "
            "era — the period "
            "of the Bank War, "
            "the Specie Circular, "
            "and the emerging "
            "sectional tensions "
            "over slavery's expansion. "
            "Maine's Democratic "
            "politics were "
            "strongly Jacksonian "
            "— the frontier "
            "state's loggers "
            "and farmers aligned "
            "with Jackson's "
            "populism over "
            "Whig commercialism.\n\n"
            "His brief appointed "
            "term contributed "
            "Maine's Democratic "
            "voice to the "
            "early Van Buren period.\n\n"
            "He had previously "
            "served as a "
            "Maine state legislator.\n\n"
            "He was an Oxford "
            "County Maine lawyer."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Maine Democratic-Republican Senator (1836–1837) by appointment; served during the Jackson-Van Buren Bank War era; Maine's statehood context from the Missouri Compromise; Oxford County lawyer contributing Maine's Democratic Jacksonian voice; brief but historically situated tenure.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Maine's statehood from the Missouri Compromise — the 1820 creation of Maine as a free state to balance Missouri's slave statehood — created the constitutional and sectional context of Maine's early Senate representation",
            "The vacancy that created Dana's appointment — a sitting senator's departure requiring the governor to appoint a temporary replacement — created the mechanism of his brief Senate service",
            "Maine's Jacksonian Democratic culture — the frontier state's small farmers and loggers whose anti-elitist populism aligned naturally with Jackson's democratic movement — created the political environment for Dana's Democratic Senate appointment"
        ],
        "effects": [
            "His brief Senate service contributed Maine's Democratic Jacksonian vote to the Van Buren era's opening debates — the Bank War aftermath and the Specie Circular controversy",
            "His appointment contributed to the continuity of Maine's Senate representation during a vacancy — the practical function of appointed senators in maintaining state representation",
            "His career contributed to the documentation of Maine's early statehood politics — the Democratic tradition that shaped the state's antebellum political culture",
            "His service illustrated Maine's role as the free-state counterpart of Missouri — the northern frontier state that the Missouri Compromise created as a permanent part of the free-state Senate bloc"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Maine Senator 1836–1837 by appointment"},
            {"target": "missouri-compromise", "verb": "SERVES_IN_STATE_CREATED_BY", "note": "Senator from Maine created by Missouri Compromise"},
            {"target": "martin-van-buren", "verb": "SERVES_UNDER", "note": "Senator during Van Buren's early administration"},
            {"target": "democratic-party-united-states", "verb": "MEMBER_OF", "note": "Maine Jacksonian Democrat"},
            {"target": "maine", "verb": "REPRESENTS", "note": "Early Maine statehood senator"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 86 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
