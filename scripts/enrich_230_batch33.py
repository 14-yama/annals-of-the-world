#!/usr/bin/env python3
"""
Batch 33 — 8 entities: Richard Mentor Johnson, Levi Woodbury, James Hamilton Jr.,
John Francis Mercer, William Hull, Francis Nash, Richard Bellingham,
Daniel Elliott Huger
editorId: vscode-copilot
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

    # 1 — Richard Mentor Johnson
    ("richard-mentor-johnson", {
        "summary": (
            "Richard Mentor Johnson (1780–1850) was an American lawyer, soldier, "
            "and politician from Kentucky who served as the ninth Vice President "
            "of the United States (1837–1841) under Martin Van Buren — the only "
            "Vice President in American history to be elected by the United States "
            "Senate rather than by the Electoral College, after no candidate received "
            "an electoral majority in the 1836 vice-presidential race. Johnson is "
            "also historically distinctive for his domestic arrangements: he openly "
            "lived with and had children by Julia Chinn, an enslaved woman he "
            "had inherited, whom he treated as a common-law wife until her death "
            "in 1833 — a relationship that cost him significant political support "
            "in the South.\n\n"
            "Before his vice-presidency, Johnson had a distinguished legislative "
            "career as a US Representative (1807–1819) and US Senator (1819–1829, "
            "1833–1837) from Kentucky — and a dramatic military career as a "
            "colonel of the Kentucky Mounted Volunteers in the War of 1812. "
            "He commanded the Kentucky forces at the Battle of the Thames "
            "(October 5, 1813) — where the British-Indian coalition was defeated "
            "and Tecumseh was killed. Johnson claimed personal credit for killing "
            "Tecumseh, and though this claim was disputed, his political allies "
            "used it effectively: the campaign slogan 'Rumpsey Dumpsey, Rumpsey "
            "Dumpsey, Colonel Johnson killed Tecumseh' became one of the most "
            "memorable in early American political history.\n\n"
            "Johnson was a genuine democratic reformer: he championed the abolition "
            "of imprisonment for debt — one of the most progressive reforms of "
            "the early 19th century — and supported Sunday mail delivery as "
            "a defense of the separation of church and state.\n\n"
            "His open relationship with Julia Chinn — and his recognition of "
            "their mixed-race daughters — made him one of the most unusual "
            "and controversial figures in the Jacksonian political establishment."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "9th US Vice President (1837–1841) — the only VP elected by the Senate; claimed credit for killing Tecumseh at the Battle of the Thames (1813); longtime Kentucky congressman/senator; championed abolition of imprisonment for debt; openly recognized his mixed-race family by Julia Chinn (enslaved) — the most controversial domestic arrangement of any US VP.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The 1836 VP electoral deadlock — in which Whig candidates split the electoral vote so that no VP candidate won a majority — created the constitutional mechanism that sent the VP election to the Senate, making Johnson's Senate election unique in American history",
            "The Battle of the Thames (1813) and his claimed killing of Tecumseh — which became a campaign rallying cry — gave Johnson the military-hero reputation that sustained his political career across multiple decades",
            "Kentucky's Jacksonian Democratic culture — and Johnson's deep roots in Kentucky politics as a congressional stalwart — created the political base from which his VP career launched"
        ],
        "effects": [
            "His sole-Senate VP election created a unique constitutional precedent — demonstrating the 12th Amendment's mechanism for Senate VP selection and illustrating the dangers of Whig multi-candidate VP strategies",
            "His championing of the abolition of imprisonment for debt — which contributed to legislative reform across multiple states — was one of the most progressive economic reforms of the early 19th century",
            "His claimed killing of Tecumseh — and the battle cry it generated — made his career one of the most famous examples of military reputation as political capital in early American history",
            "His open recognition of his mixed-race daughters' legitimacy — and his attempts to introduce them to Kentucky society — was one of the most unusually progressive personal positions on racial recognition of any antebellum US politician"
        ],
        "relationships": [
            {"entity": "US Senate (VP election, 1837)", "relationship": "ONLY_VP_ELECTED_BY", "note": "The only Vice President in American history elected by the Senate — after no candidate won an electoral majority in the 1836 VP race"},
            {"entity": "Battle of the Thames (1813) / Tecumseh's death", "relationship": "CLAIMED_CREDIT_FOR_KILLING_TECUMSEH_AT", "note": "Commanded Kentucky Mounted Volunteers at the Battle of the Thames and claimed personal credit for killing Tecumseh — his most celebrated political-military credential"},
            {"entity": "Martin Van Buren (8th US President)", "relationship": "VICE_PRESIDENT_UNDER", "note": "Served as VP under Van Buren (1837–1841) — the only Senate-elected VP in American history"},
            {"entity": "Abolition of imprisonment for debt (reform movement)", "relationship": "LEADING_CONGRESSIONAL_CHAMPION_OF", "note": "Championed the abolition of imprisonment for debt in Congress — one of the most significant progressive economic reforms of the early 19th century"},
            {"entity": "Julia Chinn (enslaved common-law partner)", "relationship": "OPENLY_RECOGNIZED_FAMILY_WITH", "note": "Lived openly with Julia Chinn (an enslaved woman he inherited) as a common-law wife — recognizing their mixed-race daughters — the most controversial domestic arrangement of any US VP"}
        ]
    }),

    # 2 — Levi Woodbury
    ("levi-woodbury", {
        "summary": (
            "Levi Woodbury (1789–1851) was a New Hampshire Democratic politician "
            "and jurist who achieved the extraordinary distinction of serving in "
            "all three branches of the federal government — as Associate Justice "
            "of the Supreme Court (1845–1851), as Secretary of the Navy "
            "(1831–1834), as Secretary of the Treasury (1834–1841), as a US "
            "Senator from New Hampshire (1825–1831, 1841–1845), and as Governor "
            "of New Hampshire (1823–1824). He was one of only a handful of "
            "Americans in history to hold significant office in the legislative, "
            "executive, and judicial branches of the federal government.\n\n"
            "Woodbury's career spanned the Jacksonian political era from beginning "
            "to end: he served in the Treasury under both Andrew Jackson and "
            "Martin Van Buren — navigating the Bank War (the destruction of the "
            "Second Bank of the United States), the Panic of 1837 (the worst "
            "economic crisis to that point in American history), and the "
            "introduction of the Independent Treasury system (which separated "
            "federal funds from private banks). His Treasury tenure coincided "
            "with two of the most consequential economic events in early American "
            "financial history.\n\n"
            "As a Supreme Court Associate Justice, Woodbury's tenure was brief "
            "(1845–1851) but significant: his concurrence in Jones v. Van Zandt "
            "(1847) upheld the Fugitive Slave Act of 1793 — a decision that "
            "contributed to the abolitionist anger that eventually produced the "
            "stronger Fugitive Slave Act of 1850. He was considered a serious "
            "candidate for the Democratic presidential nomination in 1848.\n\n"
            "His death in 1851 cut short what might have been a more significant "
            "judicial career at the Court."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "One of the very few Americans to hold significant office in all three federal branches: Associate Justice (1845–1851), Secretary of the Treasury (1834–1841, managing the Panic of 1837), Secretary of the Navy (1831–1834), US Senator, and Governor of New Hampshire.",
            "significanceCategory": "continental"
        },
        "causes": [
            "New Hampshire's Democratic political culture — and its reputation for producing capable administrators — created the political base for Woodbury's long career across multiple federal offices",
            "Jackson's destruction of the Second Bank of the United States and the subsequent Panic of 1837 created the Treasury crisis that defined Woodbury's most consequential executive role",
            "The Jacksonian Democratic Party's need for loyal, capable administrators who could manage the complex financial and diplomatic institutions of the federal government — and Woodbury's demonstrated competence — drove his repeated appointments"
        ],
        "effects": [
            "His Treasury management of the Panic of 1837 — and his implementation of the Independent Treasury system — contributed to the long-term restructuring of American federal finance away from private bank partnership",
            "His Jones v. Van Zandt concurrence upholding the Fugitive Slave Act (1847) contributed to the legal framework that abolitionists fought — and to the political anger that helped fuel the Compromise of 1850's stronger Fugitive Slave Act",
            "His career as a multi-branch federal official contributed to the institutional development of all three branches of government during the most formative period of American constitutional development",
            "His serious 1848 presidential candidacy — cut short by his death in 1851 — suggested that his career trajectory might have culminated in the Democratic presidential nomination had he lived"
        ],
        "relationships": [
            {"entity": "US Supreme Court (Associate Justice, 1845–1851)", "relationship": "ASSOCIATE_JUSTICE", "note": "Served as Associate Justice (1845–1851) — including the Jones v. Van Zandt decision upholding the Fugitive Slave Act"},
            {"entity": "US Treasury (Secretary, 1834–1841)", "relationship": "SECRETARY_DURING_PANIC_OF_1837", "note": "Secretary of the Treasury through the Panic of 1837 and the introduction of the Independent Treasury system — two of the most consequential Jacksonian economic events"},
            {"entity": "Second Bank of the United States / Bank War", "relationship": "TREASURY_SECRETARY_DURING_DESTRUCTION_OF", "note": "Managed the Treasury during Jackson's Bank War — the destruction of the Second Bank of the United States and the restructuring of federal finance"},
            {"entity": "Independent Treasury system", "relationship": "IMPLEMENTOR_OF", "note": "Oversaw the introduction of the Independent Treasury system — separating federal funds from private banks — the major financial legacy of the Van Buren administration"},
            {"entity": "All three branches of US federal government", "relationship": "ONE_OF_FEW_AMERICANS_TO_SERVE_SIGNIFICANTLY_IN_ALL_THREE", "note": "Served in the judicial (SCOTUS), executive (Navy + Treasury), and legislative (Senate) branches — one of the very few Americans to hold major offices in all three"}
        ]
    }),

    # 3 — James Hamilton Jr.
    ("james-hamilton", {
        "summary": (
            "James Hamilton Jr. (1786–1857) was a South Carolina politician and "
            "a leading architect of the Nullification Crisis — the constitutional "
            "confrontation of 1832–1833 in which South Carolina asserted the "
            "right of states to nullify federal law. As Governor of South Carolina "
            "(1830–1832), Hamilton organized the political machinery that transformed "
            "John C. Calhoun's abstract doctrine of nullification into a concrete "
            "political program: he presided over the state conventions, coordinated "
            "the nullifier majority, and helped draft the South Carolina Ordinance "
            "of Nullification (November 1832) — which declared the federal tariffs "
            "of 1828 and 1832 void within South Carolina.\n\n"
            "Hamilton had earlier served in the US House (1822–1829) as a "
            "states' rights Democrat — a firebrand who had fought a duel with "
            "Virginia congressman John Randolph in 1826. He was one of the "
            "most aggressive Southern sectionalists of the early Jacksonian "
            "period, pushing the nullification doctrine harder than even Calhoun "
            "sometimes wanted to go.\n\n"
            "The Nullification Crisis was resolved by Henry Clay's Compromise "
            "Tariff of 1833 — and President Jackson's Force Bill, which asserted "
            "federal authority to collect tariffs by force. South Carolina "
            "repealed its nullification ordinance but also symbolically nullified "
            "the Force Bill. Hamilton's role in organizing the Crisis made him "
            "one of the most important figures in the antebellum Southern "
            "sectionalist movement — a rehearsal for the secession crisis of 1860.\n\n"
            "After the Crisis, Hamilton became a Texas independence promoter "
            "and financial agent — dying in 1857 when his steamship sank off "
            "the coast of Texas, years before the Confederacy that his nullification "
            "theories helped inspire came into being."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "South Carolina Governor (1830–1832) and leading organizer of the Nullification Crisis — drafted the Ordinance of Nullification (1832) that triggered the confrontation with Jackson; US Representative (1822–1829); his nullification advocacy was a direct rehearsal for the secession crisis of 1860.",
            "significanceCategory": "continental"
        },
        "causes": [
            "South Carolina's planters' rage at the 'Tariff of Abominations' (1828) — which they believed would destroy the South's agricultural export economy by protecting Northern manufacturers — created the economic grievance that Hamilton transformed into the nullification movement",
            "John C. Calhoun's development of nullification theory — in the South Carolina Exposition and Protest (1828) — provided the constitutional framework that Hamilton then organized into a concrete political program as governor",
            "The absence of Jackson's expected opposition to nullification — and Jackson's eventual willingness to seek the Force Bill — created the constitutional confrontation that Hamilton had been organizing toward"
        ],
        "effects": [
            "The South Carolina Ordinance of Nullification — which Hamilton helped organize and draft — triggered the first major constitutional crisis over states' rights vs. federal authority in American history, establishing the template for later secessionism",
            "Jackson's Force Bill — asserting federal authority to enforce tariff collection by military force — was a direct response to Hamilton's nullification movement, establishing the most aggressive federal constitutional position against states' rights to that point",
            "The Compromise Tariff of 1833 — Clay's resolution that allowed both sides to claim partial victory — resolved the immediate crisis but left the underlying constitutional question of nullification unresolved, bequeathing it to the 1860s",
            "Hamilton's nullification precedent became the constitutional and political template for the secession crisis of 1860 — the nullifiers of 1832 were the ideological ancestors of the secessionists of 1861"
        ],
        "relationships": [
            {"entity": "South Carolina Ordinance of Nullification (1832)", "relationship": "ORGANIZER_AND_CO-DRAFTER_OF", "note": "As governor, organized the political machinery and helped draft the Ordinance of Nullification — declaring federal tariffs void in South Carolina"},
            {"entity": "John C. Calhoun (nullification theorist)", "relationship": "ORGANIZATIONAL_EXECUTOR_OF_DOCTRINE_OF", "note": "Transformed Calhoun's abstract nullification theory into a concrete political program — sometimes pushing harder than Calhoun himself"},
            {"entity": "Andrew Jackson / Force Bill (1833)", "relationship": "NULLIFICATION_ORGANIZER_THAT_TRIGGERED", "note": "His nullification organization triggered Jackson's Force Bill — the most aggressive assertion of federal authority over states' rights to that point in American history"},
            {"entity": "South Carolina governorship (1830–1832)", "relationship": "GOVERNOR_DURING_NULLIFICATION_CRISIS", "note": "Used the governorship to organize the nullification movement — presiding over the state conventions that produced the Ordinance of Nullification"},
            {"entity": "Secession crisis of 1860 / Civil War", "relationship": "NULLIFICATION_REHEARSAL_FOR", "note": "The nullification he organized was the direct constitutional and political precedent for the secession of 1860–1861 — the nullifiers of 1832 were the ideological ancestors of the Confederacy"}
        ]
    }),

    # 4 — John Francis Mercer
    ("john-francis-mercer", {
        "summary": (
            "John Francis Mercer (1759–1821) was an American Founding Father "
            "and politician from Virginia and Maryland — a Revolutionary War "
            "officer, Continental Congress delegate, delegate to the Constitutional "
            "Convention of 1787, and Governor of Maryland (1801–1803). "
            "He is particularly notable for attending the Constitutional Convention "
            "in Philadelphia but leaving before its completion and refusing to sign "
            "the Constitution — one of the sixteen delegates who either left early "
            "or refused to sign — because he believed it concentrated too much "
            "power in the federal government and insufficient power in the states "
            "and in the people.\n\n"
            "Mercer's Anti-Federalist position at the Constitutional Convention "
            "was part of a broader pattern of Virginia-connected politicians who "
            "believed the new Constitution was dangerously centralizing. He shared "
            "these concerns with George Mason and Elbridge Gerry (the other two "
            "major non-signers present at the close of the Convention). His "
            "subsequent career reflected these convictions: he served in Maryland "
            "as a Democratic-Republican governor who emphasized states' rights.\n\n"
            "Before the Convention, Mercer had served as an officer in the Continental "
            "Army — fighting under the Marquis de Lafayette and participating "
            "in several Virginia campaigns — and as a delegate to the Continental "
            "Congress. His military service gave him the standing of a "
            "Revolutionary patriot even as his Constitutional Convention refusal "
            "placed him among the opponents of the new framework.\n\n"
            "He moved from Virginia to Maryland in the 1780s, where he established "
            "himself as a plantation owner and politician — eventually rising to "
            "the governorship."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Virginia/Maryland Founding Father; Revolutionary War officer under Lafayette; delegate to the Constitutional Convention (1787) who left without signing — opposing federal power concentration; Continental Congress delegate; Governor of Maryland (1801–1803).",
            "significanceCategory": "regional"
        },
        "causes": [
            "His Revolutionary War service — and his Continental Congress experience — established his standing as a founding-era patriot with legitimate concerns about how the new constitutional framework would distribute power",
            "His Anti-Federalist convictions — shared with Mason and Gerry — created the principled grounds on which he refused to sign the Constitution: he believed it concentrated too much power in the federal government at the expense of states and the people",
            "His move from Virginia to Maryland in the 1780s created a new political base — and the Democratic-Republican alignment of Maryland's political culture allowed him to rise to the governorship as a states' rights politician"
        ],
        "effects": [
            "His refusal to sign the Constitution was part of the broader Anti-Federalist opposition that eventually secured the Bill of Rights — the Anti-Federalists' demand for explicit rights protections produced the most important constitutional additions to the document",
            "His Continental Congress service contributed to the governance of the Articles of Confederation period — the founding framework whose weaknesses the Constitution was designed to address",
            "His gubernatorial career in Maryland contributed to the state's Democratic-Republican political development in the early national period",
            "His life story — from Virginia family to Maryland plantation to Maryland governor — illustrated the geographic mobility of the founding generation's planter class across the Chesapeake region"
        ],
        "relationships": [
            {"entity": "Constitutional Convention (1787)", "relationship": "DELEGATE_WHO_LEFT_WITHOUT_SIGNING", "note": "Attended the Constitutional Convention but refused to sign the Constitution — opposing the concentration of federal power over states and the people"},
            {"entity": "Marquis de Lafayette / Continental Army", "relationship": "OFFICER_UNDER_DURING_REVOLUTION", "note": "Served as a Continental Army officer under the Marquis de Lafayette — fighting in Virginia campaigns during the Revolutionary War"},
            {"entity": "Maryland governorship (1801–1803)", "relationship": "GOVERNOR", "note": "Served as Governor of Maryland (1801–1803) as a Democratic-Republican — reflecting his states' rights political philosophy"},
            {"entity": "Anti-Federalist movement (George Mason, Elbridge Gerry)", "relationship": "ALLIED_WITH_AT_CONSTITUTIONAL_CONVENTION", "note": "Shared the Anti-Federalist position of Mason and Gerry — the most significant non-signers of the Constitution — in opposing the Constitution's centralization"},
            {"entity": "Continental Congress", "relationship": "DELEGATE_TO", "note": "Served as a Continental Congress delegate before the Constitutional Convention — contributing to the governance of the Articles of Confederation period"}
        ]
    }),

    # 5 — William Hull
    ("william-hull", {
        "summary": (
            "William Hull (1753–1825) was an American military officer, "
            "politician, and territorial governor whose career ended in one "
            "of the most catastrophic military disasters in American history: "
            "the surrender of Fort Detroit to British forces on August 16, 1812 "
            "— without firing a shot — in the opening weeks of the War of 1812. "
            "A decorated Revolutionary War veteran who had served with distinction "
            "under Washington, Hull had been appointed Governor of Michigan "
            "Territory (1805–1812) and commanded the American forces in the Northwest "
            "at the war's outbreak, charged with invading Canada. Instead, "
            "threatened by British general Isaac Brock and by the Shawnee warrior "
            "Tecumseh's forces, Hull surrendered the entire American northwest "
            "defense without resistance — handing the British control of the "
            "Detroit frontier and causing a nationwide shock.\n\n"
            "Hull's surrender was the most humiliating American military failure "
            "of the war — a disgrace that cost the United States months of "
            "strategic recovery and left the northwestern frontier vulnerable. "
            "He was subsequently court-martialed, found guilty of cowardice "
            "and neglect of duty, and sentenced to death — though President "
            "Madison pardoned him in recognition of his Revolutionary War service.\n\n"
            "Before this catastrophe, Hull had had a genuinely distinguished career: "
            "he fought at Trenton, Saratoga, Brandywine, and Monmouth during "
            "the Revolution — earning a genuine military reputation — and served "
            "in the Massachusetts legislature and as a Massachusetts state judge "
            "before his Michigan appointment.\n\n"
            "His story is one of the most dramatic examples of Revolutionary "
            "War heroism not preparing a commander for 19th-century warfare."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Michigan Territory governor (1805–1812) and Revolutionary War veteran who surrendered Fort Detroit (August 16, 1812) without firing a shot — the most catastrophic American military failure of the War of 1812; court-martialed and sentenced to death (pardoned by Madison).",
            "significanceCategory": "regional"
        },
        "causes": [
            "His genuine Revolutionary War heroism — serving at Trenton, Saratoga, Brandywine, and Monmouth — gave him a military reputation that earned his Michigan appointment but did not prepare him for the different strategic challenges of the 1812 campaign",
            "Isaac Brock's effective bluffing strategy — which convinced Hull that he faced overwhelming forces — and Tecumseh's psychological intimidation exploited Hull's excessive caution and his fear of the consequences of defeat for Detroit's civilian population",
            "The American Northwest's vulnerability — isolated frontier territory with uncertain supply lines and limited regular troops — made Hull's position strategically very difficult regardless of his personal qualities"
        ],
        "effects": [
            "The surrender of Fort Detroit was the most humiliating American military failure of the War of 1812 — shocking the nation, leaving the Northwest vulnerable, and requiring months of strategic recovery",
            "His court-martial and death sentence — subsequently pardoned by Madison — established the precedent that surrender without resistance could constitute military cowardice subject to capital punishment",
            "The strategic consequences of his surrender — British control of the Detroit frontier through much of 1812–1813 — gave the British and their Native American allies control of the Northwest until Oliver Hazard Perry's Lake Erie victory and the Battle of the Thames (1813)",
            "The shock of his surrender directly motivated the more aggressive American military posture that eventually produced the victories of 1813 — a negative example that shaped subsequent American military command decisions"
        ],
        "relationships": [
            {"entity": "Surrender of Fort Detroit (August 16, 1812)", "relationship": "RESPONSIBLE_COMMANDER_FOR_CATASTROPHIC", "note": "Surrendered Fort Detroit to British general Isaac Brock without firing a shot — the most humiliating American military failure of the War of 1812"},
            {"entity": "Isaac Brock (British general)", "relationship": "CAPITULATED_TO_BLUFFING_OF", "note": "Surrendered to Isaac Brock's effective bluffing strategy — which convinced Hull he faced overwhelming forces when Brock was actually outnumbered"},
            {"entity": "Revolutionary War (Trenton, Saratoga, Brandywine, Monmouth)", "relationship": "DECORATED_VETERAN_OF", "note": "Served with genuine distinction in the Revolutionary War — fighting at Trenton, Saratoga, Brandywine, and Monmouth before his Michigan appointment"},
            {"entity": "Michigan Territory governorship (1805–1812)", "relationship": "GOVERNOR_AND_MILITARY_COMMANDER", "note": "Served as Michigan Territory governor (1805–1812) — combining territorial governance with command of the Northwest's military forces at the war's outbreak"},
            {"entity": "Court-martial / President Madison pardon", "relationship": "SUBJECT_OF_DEATH_SENTENCE_THEN_PARDON", "note": "Court-martialed, found guilty of cowardice and neglect of duty, and sentenced to death — pardoned by Madison in recognition of his Revolutionary War service"}
        ]
    }),

    # 6 — Francis Nash
    ("francis-nash", {
        "summary": (
            "Francis Nash (c.1742–1777) was a North Carolina lawyer, politician, "
            "and Continental Army general whose short but distinguished military "
            "career ended at the Battle of Germantown (October 4, 1777) — when "
            "he was mortally wounded by a British cannonball while leading his "
            "brigade during Washington's assault on the British positions at "
            "Germantown, Pennsylvania. He died three days later, becoming one "
            "of the most senior American officers to die in the Revolutionary War.\n\n"
            "Before the war, Nash had established himself as a prominent North "
            "Carolina lawyer and politician — serving in the colonial legislature "
            "and becoming involved in the complex conflict known as the Regulator "
            "movement (1768–1771), in which backcountry North Carolinians rebelled "
            "against corrupt colonial officials. Nash served with Governor William "
            "Tryon's militia against the Regulators at the Battle of Alamance "
            "(1771) — a complicated position, since many of the Regulators' "
            "grievances about elite corruption were legitimate, even if their "
            "methods were extralegal.\n\n"
            "When the Revolutionary War began, Nash transferred his loyalties to "
            "the Patriot cause, rising to the rank of Brigadier General in the "
            "Continental Army. He commanded North Carolina troops in multiple "
            "campaigns — including the Philadelphia campaign of 1777 that "
            "culminated at Germantown.\n\n"
            "His death in battle secured him a lasting memorial legacy: "
            "Nash County in North Carolina and Nashville, Tennessee — the "
            "capital of Tennessee — are both named after him."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "North Carolina Continental Army Brigadier General; served in the Regulator crisis (1771) and the Revolutionary War; mortally wounded at the Battle of Germantown (1777) — one of the most senior American officers to die in the war; Nash County NC and Nashville, Tennessee named in his honor.",
            "significanceCategory": "regional"
        },
        "causes": [
            "North Carolina's volatile colonial politics — the Regulator movement's backcountry grievances, and the subsequent Revolutionary War alignment — created the political and military context in which Nash moved from colonial militia officer to Continental Army general",
            "Washington's Philadelphia campaign of 1777 — including the aggressive but failed assault on Germantown — created the military context in which Nash's brigade was deployed and in which Nash was mortally wounded",
            "North Carolina's need for experienced military commanders who could organize and lead its Continental Army troops — and Nash's standing as a prominent lawyer-politician with military experience — made his elevation to brigadier general natural"
        ],
        "effects": [
            "His death at Germantown — one of the most senior American officers to die in the war — was a significant loss to the Continental Army and to North Carolina's Revolutionary War leadership",
            "Nashville, Tennessee — the capital of a major state — was named in his honor: one of the most enduring American memorials to a Revolutionary War general",
            "Nash County in North Carolina also preserved his memory — giving him a dual geographic legacy that few Revolutionary War figures matched",
            "His death was part of the broader pattern of significant officer losses at Germantown — the battle that, though a defeat, demonstrated the Continental Army's growing tactical capability"
        ],
        "relationships": [
            {"entity": "Battle of Germantown (1777)", "relationship": "MORTALLY_WOUNDED_LEADING_BRIGADE_AT", "note": "Mortally wounded by a British cannonball while leading his brigade at Germantown — dying three days later as one of the most senior American casualties of the war"},
            {"entity": "Nashville, Tennessee (capital city naming)", "relationship": "NAMESAKE_OF", "note": "Nashville, Tennessee — the capital of Tennessee — was named in his honor, one of the most significant geographic memorials to a Revolutionary War figure"},
            {"entity": "North Carolina Continental Army brigade", "relationship": "COMMANDER_OF", "note": "Commanded North Carolina's Continental Army troops in multiple campaigns — including the Philadelphia campaign of 1777 that ended at Germantown"},
            {"entity": "Regulator movement / Battle of Alamance (1771)", "relationship": "SERVED_IN_COLONIAL_MILITIA_AGAINST", "note": "Served with Governor Tryon's militia against the Regulators at Alamance (1771) — a complex episode given the Regulators' legitimate grievances about colonial corruption"},
            {"entity": "Nash County, North Carolina", "relationship": "NAMESAKE_OF", "note": "Nash County in North Carolina was named in his honor — giving him a dual geographic legacy alongside Nashville, Tennessee"}
        ]
    }),

    # 7 — Richard Bellingham
    ("richard-bellingham", {
        "summary": (
            "Richard Bellingham (1592–1672) was an English-born colonial magistrate "
            "and lawyer who became one of the most significant political figures "
            "of early Massachusetts Bay Colony — serving as its Governor multiple "
            "times (1641, 1654–1655, 1665–1672) and as a deputy governor, magistrate, "
            "and assistant across more than four decades of colonial governance. "
            "Born in Lincolnshire, England, he trained as a lawyer and served "
            "in the English Parliament before emigrating to Massachusetts in 1634. "
            "He is historically notable as the last surviving signatory of the "
            "Massachusetts Bay Company charter — dying in 1672 as the oldest "
            "surviving link to the colony's original founding legal document.\n\n"
            "Bellingham was a polarizing figure in early Massachusetts Bay Colony "
            "politics. His 1641 marriage to Penelope Pelham — conducted by himself "
            "without the proper banns and while she was still contracted to another "
            "man — caused a significant legal scandal that he narrowly escaped "
            "by refusing to be tried (as a magistrate, he would have had to "
            "try himself). His governance style was autocratic and frequently "
            "in conflict with the more moderate positions of figures like John "
            "Winthrop.\n\n"
            "He was a strong defender of Puritan orthodoxy and an opponent of "
            "the liberalizing tendencies that gradually appeared in Massachusetts "
            "over the decades — aligning himself with the stricter, more "
            "theocratic wing of the colonial leadership. His final governorship "
            "(1665–1672) coincided with increasing pressure from the English "
            "Crown on Massachusetts's autonomy — and he died during this "
            "period of constitutional uncertainty as the colony's most senior "
            "surviving founding figure."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Multiple-time Governor of Massachusetts Bay Colony (1641, 1654–1655, 1665–1672); last surviving signatory of the Massachusetts Bay Company charter; English-trained lawyer who emigrated to Massachusetts in 1634; 38+ years of colonial governance; a polarizing figure who defended Puritan orthodoxy.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Massachusetts Bay Colony's need for legally trained colonial governors — Bellingham's English parliamentary and legal training made him one of the most qualified early colonists for governance roles",
            "The Massachusetts Bay Company's founding mission to establish a Puritan colony in the New World — and Bellingham's deep Puritan convictions — created the alignment between his personal beliefs and the colony's founding purposes",
            "The increasing pressure from the English Crown on Massachusetts Bay Colony's autonomy in the 1660s — Bellingham's final governorship period — created the constitutional challenge that he had to navigate as the colony's most senior surviving founding figure"
        ],
        "effects": [
            "His 38+ years of colonial governance contributed to Massachusetts Bay Colony's institutional development across its most formative period — from its earliest settlement phase through the Restoration crisis",
            "As the last surviving signatory of the Massachusetts Bay Company charter, Bellingham's death in 1672 marked the end of the founding generation's direct institutional connection to the colony's legal founding document",
            "His defense of Puritan orthodoxy contributed to the theocratic character of early Massachusetts governance — resisting the liberalizing pressures that appeared as the colony matured",
            "His controversial 1641 marriage — and his autocratic refusal to subject himself to prosecution as a magistrate — illustrated the tensions between personal behavior and the legal accountability that the colony's governance required"
        ],
        "relationships": [
            {"entity": "Massachusetts Bay Colony governorship", "relationship": "MULTIPLE-TIMES_GOVERNOR_OF", "note": "Served as Governor of Massachusetts Bay Colony in 1641, 1654–1655, and 1665–1672 — with extensive deputy governor and magistrate service between terms"},
            {"entity": "Massachusetts Bay Company charter (colonial founding document)", "relationship": "LAST_SURVIVING_SIGNATORY_OF", "note": "Died in 1672 as the last surviving signatory of the Massachusetts Bay Company charter — the colony's founding legal document"},
            {"entity": "Puritan orthodoxy (Massachusetts Bay Colony)", "relationship": "DEFENDER_OF_AGAINST_LIBERALIZING_PRESSURES", "note": "Aligned with the stricter, more theocratic wing of Massachusetts governance — defending Puritan orthodoxy against the liberalizing tendencies that gradually appeared"},
            {"entity": "English Crown pressure on Massachusetts autonomy (1660s)", "relationship": "FINAL_GOVERNOR_DURING", "note": "His final governorship (1665–1672) coincided with increasing English Crown pressure on Massachusetts Bay Colony's autonomy — the Restoration crisis for Puritan governance"},
            {"entity": "John Winthrop (Massachusetts Bay Colony leadership)", "relationship": "FREQUENTLY_IN_CONFLICT_WITH", "note": "His autocratic style and strict Puritan positions frequently put him in conflict with the more moderate positions of Winthrop and other colonial leaders"}
        ]
    }),

    # 8 — Daniel Elliott Huger
    ("daniel-elliott-huger", {
        "summary": (
            "Daniel Elliott Huger (1779–1854) was a South Carolina planter, lawyer, "
            "and politician from Berkeley County who served as a United States "
            "Senator from South Carolina (1843–1845) — a brief single-term Senate "
            "career at the height of the Whig-Democrat sectional struggle. The son "
            "of Daniel Huger (a Continental Congressman and US Representative), "
            "he was part of South Carolina's established planter-gentry political "
            "dynasty — one of the state's most prominent colonial and revolutionary "
            "families.\n\n"
            "Huger's political career played out against the backdrop of South "
            "Carolina's intense sectionalist politics in the antebellum period — "
            "the era of nullification, states' rights, and the growing sectional "
            "conflict over slavery and tariffs that would eventually produce the "
            "Confederacy. He served in the South Carolina state legislature and "
            "as a state circuit court judge before his Senate appointment — "
            "a career path typical of South Carolina's legal-political elite.\n\n"
            "His brief Senate term (1843–1845) placed him in Congress during a "
            "consequential period: the Tyler administration's annexation of Texas "
            "was being debated, and the Democrats and Whigs were locked in fierce "
            "competition over the sectional implications of territorial expansion. "
            "As a South Carolinian, Huger's position on Texas annexation and "
            "the extension of slavery was predictable: South Carolina's planter "
            "class strongly supported annexation and the extension of slave territory.\n\n"
            "He was the last of his family's distinguished line of South Carolina "
            "congressional representation — a closing chapter of the Huger "
            "family's multigenerational political service."
        ),
        "importanceScore": 5,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "South Carolina US Senator (1843–1845); son of Continental Congressman Daniel Huger; second-generation Huger family congressional representation; planter-gentry politician from Berkeley County who served during the Texas annexation debates.",
            "significanceCategory": "regional"
        },
        "causes": [
            "His father Daniel Huger's distinguished Continental Congress and US House career established the family political legacy that Daniel Elliott inherited and continued",
            "South Carolina's planter-gentry political culture — in which established families dominated state politics through a combination of social prestige, plantation wealth, and legal training — created the conditions for Huger's political advancement",
            "The vacancy created by South Carolina's political circumstances in 1843 — and Huger's standing as a jurist and planter from one of the state's most distinguished families — created the appointment opportunity"
        ],
        "effects": [
            "His brief Senate service contributed to South Carolina's representation in Washington during the Texas annexation debate — one of the most consequential territorial and sectional issues of the antebellum period",
            "His career closed the Huger family's long record of South Carolina federal political service — spanning from the Continental Congress through the antebellum Senate",
            "His South Carolina Senate service was part of the broader pattern of Southern planter-gentry politicians who maintained the states' rights, pro-slavery political consensus that defined the antebellum South's federal representatives",
            "His legal career — as circuit court judge before his Senate service — contributed to South Carolina's developing legal system in the antebellum period"
        ],
        "relationships": [
            {"entity": "Daniel Huger (Continental Congressman / US Representative)", "relationship": "SON_OF", "note": "Son of Daniel Huger — Continental Congressman and US Representative — continuing the family's multigenerational South Carolina political legacy"},
            {"entity": "US Senate from South Carolina (1843–1845)", "relationship": "SENATOR", "note": "Served as US Senator from South Carolina (1843–1845) during the Texas annexation debate and the height of the antebellum sectional struggle"},
            {"entity": "Texas annexation debate (1843–1845)", "relationship": "SENATOR_DURING", "note": "His Senate term coincided with the Texas annexation debate — supporting annexation as a South Carolina planter aligned with the extension of slave territory"},
            {"entity": "South Carolina planter-gentry political dynasty (Huger family)", "relationship": "SECOND-GENERATION_CLOSING_CHAPTER_OF", "note": "The last of the Huger family's distinguished line of federal congressional representation — spanning from the Continental Congress to the antebellum Senate"},
            {"entity": "South Carolina circuit court judiciary", "relationship": "JUDGE_BEFORE_SENATE_SERVICE", "note": "Served as a South Carolina circuit court judge before his Senate appointment — the typical career path of the state's legal-political elite"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 33)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
