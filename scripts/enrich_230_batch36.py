#!/usr/bin/env python3
"""
Batch 36 — 8 entities: William Branch Giles, John Breckinridge, Richard Bassett,
Willie Person Mangum, Benjamin Wade, Andrew Allen, William Duer, Nathaniel Chipman
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

    # 1 — Benjamin Wade
    ("benjamin-wade", {
        "summary": (
            "Benjamin Franklin 'Bluff' Wade (1800–1878) was an Ohio Radical "
            "Republican US Senator (1851–1869) who came within a single Senate "
            "vote of becoming President of the United States — the man who would "
            "have succeeded Andrew Johnson had the 1868 impeachment conviction "
            "succeeded. As Senate president pro tempore during the trial, Wade "
            "was next in the presidential line of succession, having helped "
            "organize the very impeachment that would have elevated him to "
            "the presidency — a constitutional conflict of interest that may "
            "have contributed to his vote-counting difficulties.\n\n"
            "Wade was one of the most militant and uncompromising Radical "
            "Republicans in Congress — a fierce anti-slavery advocate who had "
            "delivered one of the most provocative abolitionist speeches in "
            "Senate history in the 1850s, and who co-authored the Wade-Davis "
            "Bill (1864) with Henry Winter Davis — the most stringent "
            "congressional Reconstruction plan, which Lincoln pocket-vetoed. "
            "The Wade-Davis Manifesto that followed was one of the sharpest "
            "public attacks on a president by members of his own party in "
            "American history.\n\n"
            "Known as 'Bluff' Wade for his blunt, combative style — he routinely "
            "responded to death threats by saying he would meet any challenger "
            "in the street — Wade was one of the most personally fearless "
            "politicians of the era. He came from abolitionist northeastern "
            "Ohio and had practiced law while actively helping escaped slaves.\n\n"
            "His defeat for re-election in 1869 — after Johnson's acquittal "
            "and the Republican machine's consolidation around Grant — ended "
            "a career that had come extraordinarily close to the presidency."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Ohio Radical Republican senator (1851–1869); Senate president pro tem during Johnson's impeachment — one Senate vote away from becoming President; co-authored the Wade-Davis Bill (1864); Wade-Davis Manifesto was the sharpest attack on Lincoln by a member of his own party; uncompromising abolitionist.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Ohio's abolitionist northeastern culture — rooted in Western Reserve communities with strong New England Puritan connections and active Underground Railroad networks — created the constituency that sustained Wade's uncompromising anti-slavery positions throughout his career",
            "Andrew Johnson's systematic dismantling of Reconstruction — restoring Confederate leaders, vetoing civil rights legislation, refusing to protect freed people — created the confrontation that Wade helped organize into the impeachment",
            "Lincoln's pocket veto of the Wade-Davis Bill — and Lincoln's preference for lenient Reconstruction terms — created the conflict between the president and the Radical Republican congressional wing that Wade most aggressively represented"
        ],
        "effects": [
            "Johnson's acquittal by one Senate vote denied Wade the presidency — and the near-miss shaped the subsequent history of Reconstruction, as the acquittal preserved Johnson's ability to continue dismantling the Radical program",
            "The Wade-Davis Bill (1864) — even pocket-vetoed by Lincoln — established the congressional standard for Reconstruction that eventually became the Radical Reconstruction Acts of 1867, influencing the postwar settlement even in its vetoed form",
            "The Wade-Davis Manifesto's sharp attack on Lincoln established a precedent for congressional challenges to presidential Reconstruction authority — contributing to the constitutional confrontation between Congress and the executive that defined the entire Reconstruction era",
            "His career demonstrated the constitutional anomaly of a Senate president pro tem who might become president after helping organize the very impeachment that would elevate him — a conflict of interest embedded in the impeachment mechanism itself"
        ],
        "relationships": [
            {"entity": "Andrew Johnson impeachment (1868) / one-vote acquittal", "relationship": "SENATE_PRESIDENT_PRO_TEM_WHO_WOULD_HAVE_SUCCEEDED_JOHNSON", "note": "As Senate president pro tem, was next in the presidential line of succession — one Senate vote away from becoming President after helping organize the very impeachment that would have elevated him"},
            {"entity": "Wade-Davis Bill (1864) / Wade-Davis Manifesto", "relationship": "CO-AUTHOR_AND_MANIFESTO_SIGNATORY_OF", "note": "Co-authored the Wade-Davis Bill with Henry Winter Davis — the most stringent congressional Reconstruction plan, pocket-vetoed by Lincoln; the subsequent Manifesto was the sharpest attack on Lincoln by his own party"},
            {"entity": "Radical Republican Party / Ohio abolitionist constituency", "relationship": "MOST_MILITANT_SENATE_VOICE_OF", "note": "The most uncompromising Radical Republican voice in the Senate — representing Ohio's abolitionist Western Reserve culture and routinely meeting personal threats with characteristic combativeness"},
            {"entity": "Abraham Lincoln (pocket veto of Wade-Davis Bill)", "relationship": "MOST_OUTSPOKEN_CONGRESSIONAL_CRITIC_OF", "note": "His Wade-Davis Manifesto was the sharpest public attack on Lincoln by a member of his own party — rooted in the confrontation over lenient vs. stringent Reconstruction terms"},
            {"entity": "US Senate from Ohio (1851–1869)", "relationship": "SENATOR", "note": "Served as Ohio's US Senator (1851–1869) — one of the longest and most consequential anti-slavery Senate careers of the Civil War era"}
        ]
    }),

    # 2 — John Breckinridge
    ("john-breckinridge", {
        "summary": (
            "John Breckinridge (1760–1806) was a Virginia-born Kentucky lawyer, "
            "planter, politician, and Attorney General of the United States "
            "(1805–1806) under President Jefferson — and the primary author "
            "of the Kentucky Resolutions of 1798, one of the most consequential "
            "and controversial political documents in American history. "
            "Written in response to Adams's Alien and Sedition Acts, "
            "the Kentucky Resolutions (drafted by Jefferson, introduced and "
            "revised by Breckinridge) asserted the right of states to nullify "
            "federal laws they deemed unconstitutional — establishing the "
            "nullification doctrine that John C. Calhoun would weaponize "
            "30 years later in the Nullification Crisis of 1832.\n\n"
            "Breckinridge served in both the Virginia and Kentucky state "
            "legislatures, as a US Senator from Kentucky (1801–1805), and "
            "as Jefferson's Attorney General from 1805 until his death "
            "in December 1806 at only 46 — cut off in the middle of what "
            "would likely have been a more prominent national career. "
            "He was a close ally and personal friend of Jefferson, who "
            "trusted him with some of the most sensitive constitutional "
            "and political work of the early republic.\n\n"
            "As Jefferson's Senate floor leader, Breckinridge managed "
            "the Louisiana Purchase Treaty's ratification in 1803 — "
            "a constitutionally complex process that required suppressing "
            "Jefferson's own doubts about whether the Constitution authorized "
            "the purchase. His grandfather was the grandfather of John C. "
            "Breckinridge — the Confederate general and 1860 vice-presidential "
            "candidate — giving the Breckinridge family a multigenerational "
            "presence at the center of American political history."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Primary author (and introducer) of the Kentucky Resolutions (1798) — the foundational nullification doctrine document; Jefferson's Senate floor leader who managed the Louisiana Purchase ratification (1803); Jefferson's Attorney General (1805–1806, died in office); Kentucky senator and Virginia/Kentucky planter-politician.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Adams's Alien and Sedition Acts — which both Jefferson and Madison believed were unconstitutional assaults on free speech and states' rights — created the political emergency that produced the Kentucky and Virginia Resolutions that Breckinridge introduced",
            "Jefferson's trust in Breckinridge — and Breckinridge's position as Jefferson's closest Senate ally — created the channel through which Jefferson's most politically sensitive documents were formally introduced and managed in the Kentucky legislature and the US Senate",
            "Kentucky's frontier political culture — with its deep skepticism of federal power and its strong Virginia-emigrant constitutional tradition — created the receptive environment for the nullification doctrine Breckinridge introduced"
        ],
        "effects": [
            "The Kentucky Resolutions — which he introduced and shaped — established the nullification doctrine that became the constitutional foundation for Calhoun's Nullification Crisis (1832) and ultimately for Southern secession (1860–1861)",
            "His management of the Louisiana Purchase Treaty ratification (1803) — suppressing Jefferson's own constitutional doubts — ensured the largest land acquisition in American history was ratified despite genuine constitutional ambiguity",
            "His early death at 46 removed one of Jefferson's most trusted constitutional and political allies at the moment when his influence on the early republic was at its height",
            "The Breckinridge family's multigenerational political legacy — from the Kentucky Resolutions (1798) through John C. Breckinridge's 1860 vice-presidential candidacy and Confederate generalship — traced one of the most consequential family arcs in American political history"
        ],
        "relationships": [
            {"entity": "Kentucky Resolutions (1798) — nullification doctrine", "relationship": "PRIMARY_AUTHOR_AND_INTRODUCER_OF", "note": "Introduced and revised Jefferson's Kentucky Resolutions — establishing the nullification doctrine that Calhoun weaponized in 1832 and that provided the constitutional framework for Southern secession"},
            {"entity": "Thomas Jefferson (President, political ally)", "relationship": "CLOSEST_SENATE_FLOOR_LEADER_AND_CONSTITUTIONAL_AGENT_OF", "note": "Jefferson's most trusted Senate ally — introduced the Kentucky Resolutions, managed the Louisiana Purchase ratification, and served as Jefferson's Attorney General"},
            {"entity": "Louisiana Purchase Treaty ratification (1803)", "relationship": "SENATE_FLOOR_LEADER_MANAGING_RATIFICATION_OF", "note": "Managed the Louisiana Purchase Treaty's Senate ratification — suppressing Jefferson's own constitutional doubts about whether the purchase was authorized"},
            {"entity": "John C. Calhoun / Nullification Crisis (1832)", "relationship": "DOCTRINAL_PREDECESSOR_OF", "note": "His Kentucky Resolutions established the nullification doctrine that Calhoun deployed in the 1832 crisis — making him the intellectual ancestor of the most dangerous antebellum constitutional confrontation"},
            {"entity": "Jefferson's Attorney General (1805–1806, died in office)", "relationship": "ATTORNEY_GENERAL_WHO_DIED_IN_OFFICE", "note": "Served as Jefferson's Attorney General (1805–1806) — dying in December 1806 at 46, cutting off one of the early republic's most consequential careers"}
        ]
    }),

    # 3 — William Branch Giles
    ("william-branch-giles", {
        "summary": (
            "William Branch Giles (1762–1830) was a Virginia Democratic-Republican "
            "politician who served as Jefferson's most combative floor leader "
            "in the House of Representatives (1790–1798, 1801–1803), as a "
            "US Senator from Virginia (1804–1815), and as the 24th Governor "
            "of Virginia (1827–1830). He was known throughout his career for "
            "aggressive, partisan political combat — twice attempting to remove "
            "Federalist cabinet officers through congressional censure, and "
            "leading the effort to impeach John Marshall and the entire "
            "Federalist-dominated federal judiciary in 1803–1804.\n\n"
            "Giles's most extraordinary political initiative was his 1804 "
            "attempt to impeach the entire Federalist federal judiciary — "
            "not for specific misconduct, but simply because Federalists "
            "controlled it and Jefferson's party wanted Democratic-Republican "
            "judges. His proposal — a naked assertion of congressional power "
            "to remove judges for political reasons — failed, but the "
            "debate forced Marshall to define the boundaries of judicial "
            "independence, contributing to the consolidation of Marshall's "
            "position that judges could only be removed for actual misconduct.\n\n"
            "Giles's political career reflected the Jeffersonian-Madisonian "
            "tradition's most aggressive anti-Federalist wing: he led "
            "congressional attacks on Hamilton's financial program in the "
            "1790s, tried to censure Hamilton himself over the national "
            "bank, and sustained this combative style throughout his career. "
            "His later career became increasingly idiosyncratic: he opposed "
            "Madison's War of 1812 despite being a Democratic-Republican, "
            "and spent his final years as governor of Virginia in declining health.\n\n"
            "His career exemplified the Jeffersonian tradition's internal "
            "tensions between principled states' rights and naked partisanship."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Jefferson's most combative House floor leader; twice attempted congressional censure of Federalist cabinet officers; led 1804 attempt to impeach the entire Federalist federal judiciary; Virginia governor (1827–1830); US Senator (1804–1815); the Jeffersonian tradition's most aggressive anti-Federalist combatant.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Virginia's deeply anti-Federalist political culture — and its tradition of aggressive states' rights opposition to federal power concentration — created the political environment that made Giles's combative partisanship a career asset rather than a liability",
            "Jefferson's need for a congressional floor leader willing to engage in the most aggressive partisan attacks on Hamilton's financial program and Federalist power — creating the role that Giles occupied throughout the 1790s",
            "The Jeffersonian majority's frustration with Marshall's Federalist judiciary — which continued to issue rulings that countered Jefferson's constitutional vision — created the political impetus for Giles's extraordinary 1804 judicial impeachment proposal"
        ],
        "effects": [
            "His 1804 judicial impeachment effort — though defeated — forced the constitutional debate about judicial independence that helped consolidate Marshall's position that judges could only be removed for actual misconduct, not political reasons",
            "His congressional attacks on Hamilton's financial program in the 1790s — censure motions, floor speeches, factional organizing — contributed to the political pressure that constrained Hamilton's program and strengthened the emerging Democratic-Republican opposition",
            "His career trajectory — from Jefferson's most useful floor combatant to an increasingly isolated eccentric who opposed Madison's war — illustrated the difficulty of sustaining principled states' rights positions as circumstances changed and party loyalties evolved",
            "Virginia's governorship under his direction (1827–1830) continued the state's Democratic-Republican governance in the period immediately preceding the Jacksonian political revolution"
        ],
        "relationships": [
            {"entity": "Thomas Jefferson (legislative floor leader)", "relationship": "MOST_AGGRESSIVE_HOUSE_FLOOR_LEADER_FOR", "note": "Jefferson's most combative floor leader in the House — attacking Hamilton's program, attempting to censure cabinet officers, organizing Jeffersonian opposition"},
            {"entity": "Federal judiciary impeachment attempt (1804)", "relationship": "PROPOSER_OF_UNPRECEDENTED", "note": "Proposed impeaching the entire Federalist federal judiciary for political reasons — a naked partisan power grab that failed but forced the constitutional debate about judicial independence"},
            {"entity": "John Marshall / Federalist judiciary independence", "relationship": "MOST_AGGRESSIVE_CONGRESSIONAL_OPPONENT_OF", "note": "Led the effort to impeach Marshall's Federalist judiciary — forcing Marshall to define judicial independence against congressional removal for political reasons"},
            {"entity": "Alexander Hamilton's financial program (censure attempts)", "relationship": "LED_CONGRESSIONAL_ATTACKS_ON", "note": "Led congressional attacks on Hamilton's financial program in the 1790s — censure motions and floor opposition that made him Jefferson's indispensable legislative combatant"},
            {"entity": "Virginia governorship (1827–1830)", "relationship": "24TH_GOVERNOR", "note": "Served as 24th Governor of Virginia (1827–1830) — ending a long political career that had run from the early republic through the Jacksonian era"}
        ]
    }),

    # 4 — Richard Bassett
    ("richard-bassett", {
        "summary": (
            "Richard Bassett (1745–1815) was a Delaware lawyer, politician, "
            "and one of the Founding Fathers of the United States — a signer "
            "of the Constitution at the 1787 Philadelphia Convention, "
            "a Delaware delegate to the Constitutional Convention, the first "
            "Chief Justice of Delaware (1793–1799), Governor of Delaware "
            "(1799–1801), and a US Senator from Delaware (1789–1793). "
            "He was one of only a handful of men who signed the Constitution "
            "and subsequently held the full range of judicial, executive, "
            "and legislative office in the new government they had created.\n\n"
            "Bassett's most remarkable personal transformation was his conversion "
            "to Methodism in the early 1780s under the influence of Francis "
            "Asbury — the itinerant Methodist bishop who was bringing the "
            "evangelical movement to the American frontier. Under Asbury's "
            "influence, Bassett became a Methodist of deep conviction and "
            "eventually an abolitionist — a striking evolution for a "
            "Delaware slaveholder who had signed a constitution that "
            "protected slavery. He freed his own enslaved people and "
            "became a supporter of manumission — an unusually progressive "
            "position for a prominent Federalist politician in a border state.\n\n"
            "His conversion to Methodism also made him a patron of the "
            "early Methodist movement in America: he hosted Methodist "
            "gatherings at his Delaware estate and supported the "
            "institutional development of American Methodism in its "
            "formative decades.\n\n"
            "Bassett's life illustrated the rare intersection of Founding-era "
            "constitutional authority with evangelical religious transformation "
            "and anti-slavery conviction."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Delaware Founding Father; signer of the US Constitution (1787); Delaware's first US Senator (1789–1793); Governor of Delaware (1799–1801); first Chief Justice of Delaware; converted to Methodism under Francis Asbury and became an abolitionist — a rare Founding Father who freed his enslaved people.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Delaware's small-state politics — and its need for experienced, respected legal talent in the Constitutional Convention — made Bassett's participation as a delegate essential to securing Delaware's constitutional interests",
            "Francis Asbury's Methodist evangelicalism — and its emphasis on personal transformation, anti-slavery conviction, and frontier egalitarianism — provided the religious framework that converted Bassett from slaveholder to abolitionist in the 1780s",
            "The Constitutional Convention's need for delegates committed to the federal framework — and Delaware's particular interest in equal Senate representation — created the context in which Bassett signed the Constitution"
        ],
        "effects": [
            "His signing of the Constitution contributed to Delaware's ratification as the first state — 'The First State' — on December 7, 1787, establishing the precedent of unanimous convention-to-ratification speed",
            "His conversion to Methodism and his manumission of his enslaved people demonstrated that Founding-era slaveholders could be personally transformed by evangelical conviction — one of the rare examples of a Constitution-signer becoming an active abolitionist",
            "His patronage of Francis Asbury and the early Methodist movement contributed to American Methodism's institutional establishment during its most formative decades",
            "His career as Delaware's first senator, first chief justice, and governor demonstrated the institutional range that a single talented Founding-era lawyer could contribute to a newly created state's governmental architecture"
        ],
        "relationships": [
            {"entity": "US Constitution (Constitutional Convention, 1787)", "relationship": "SIGNER_AND_DELAWARE_DELEGATE", "note": "Signed the Constitution as a Delaware delegate — contributing to Delaware becoming the first state to ratify on December 7, 1787"},
            {"entity": "Francis Asbury (Methodist bishop)", "relationship": "CONVERT_AND_PATRON_OF", "note": "Converted to Methodism under Asbury's influence — becoming a supporter of the early American Methodist movement and hosting Methodist gatherings at his Delaware estate"},
            {"entity": "Slavery / manumission (Delaware, 1780s–1800s)", "relationship": "ABOLITIONIST_WHO_FREED_ENSLAVED_PEOPLE", "note": "Freed his own enslaved people and became a supporter of manumission — a remarkable evolution from slaveholder to abolitionist for a Founding Father in a border state"},
            {"entity": "Delaware (first US Senator, first Chief Justice, Governor)", "relationship": "FOUNDING_INSTITUTIONAL_ARCHITECT_OF", "note": "Served as Delaware's first US Senator, its first Chief Justice, and its Governor — holding the full range of the state's highest offices in the new constitutional republic"},
            {"entity": "Delaware ratification (December 7, 1787, 'The First State')", "relationship": "SIGNER_WHOSE_CONVENTION_VOTE_ENABLED", "note": "His Constitution signature contributed to Delaware's unanimous ratification on December 7, 1787 — establishing 'The First State' distinction"}
        ]
    }),

    # 5 — Willie Person Mangum
    ("willie-person-mangum", {
        "summary": (
            "Willie Person Mangum (1792–1861) was a North Carolina Whig "
            "politician and planter who served as a US Senator from North "
            "Carolina (1831–1836, 1840–1853) and as President pro tempore "
            "of the United States Senate (1842–1845) — placing him briefly "
            "in the presidential line of succession during a period when "
            "Vice President had died in office and no acting president existed. "
            "He was one of the founders and leading figures of the Whig Party, "
            "helped organize the North Carolina anti-Jacksonian coalition, "
            "and received South Carolina's 11 electoral votes in the 1836 "
            "presidential election — part of the Whig strategy of running "
            "multiple regional candidates to deny Van Buren an Electoral "
            "College majority.\n\n"
            "Mangum's first Senate term (1831–1836) ended when his vote "
            "against Andrew Jackson's Proclamation to South Carolina — "
            "during the Nullification Crisis — and his growing opposition "
            "to Jackson on multiple fronts made him persona non grata with "
            "North Carolina's Jacksonian Democratic legislature, which "
            "declined to re-elect him. He resigned rather than follow "
            "the legislature's instructions to vote for Jackson's policies.\n\n"
            "His second Senate tenure (1840–1853) was more successful: "
            "as Senate president pro tem under Tyler — whose cabinet had "
            "resigned and whose vice presidency was vacant — Mangum was "
            "technically the second in the presidential line of succession "
            "for three years, an unusual constitutional position in the "
            "Tyler administration's institutional chaos.\n\n"
            "He was a moderate who opposed secession before 1860 "
            "but ultimately sided with the Confederacy when war came."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "North Carolina Whig senator (1831–1836, 1840–1853); Senate president pro tem (1842–1845, second in line for succession during Tyler's vacant-VP administration); Whig Party co-founder; received 11 SC electoral votes in 1836; resigned rather than follow legislature's Jacksonian instructions.",
            "significanceCategory": "regional"
        },
        "causes": [
            "His growing opposition to Jackson — on nullification, the Bank War, and multiple other fronts — aligned him with the emerging Whig coalition and made re-election by a Jacksonian legislature impossible in his first term",
            "Tyler's break with the Whig Party — and the resignation of Tyler's entire cabinet — created the institutional chaos in which Mangum's Senate president pro tem role placed him in the presidential line of succession for three years",
            "North Carolina's antebellum political culture — divided between Jacksonian Democrats and the emerging Whig coalition — created the competitive political environment that Mangum navigated across his long Senate career"
        ],
        "effects": [
            "His resignation from the Senate (1836) rather than following Jacksonian legislative instructions contributed to the developing constitutional debate about whether senators were bound by their state legislatures' instructions — a question that the 17th Amendment (direct election) would eventually resolve",
            "His Senate president pro tem tenure during Tyler's vacant-VP administration placed him in the unusual constitutional position of being two heartbeats from the presidency — contributing to the debate about vice-presidential succession that eventually produced clearer constitutional mechanisms",
            "His role as a Whig Party co-founder contributed to North Carolina's Whig political development — one of the Southern states where the Whig Party maintained competitive strength against Jacksonian Democracy",
            "His reception of South Carolina's 11 electoral votes in 1836 was part of the Whig multi-candidate strategy — a constitutional gamble that failed when Van Buren won enough electoral votes to avoid a House runoff"
        ],
        "relationships": [
            {"entity": "US Senate president pro tem (1842–1845)", "relationship": "SENATE_PRESIDENT_PRO_TEM_IN_PRESIDENTIAL_LINE_OF_SUCCESSION", "note": "Served as Senate president pro tem during Tyler's vacant-VP administration — placing him second in the presidential line of succession for three years"},
            {"entity": "Whig Party (North Carolina founding)", "relationship": "CO-FOUNDER_AND_LEADING_FIGURE", "note": "One of the founders and leading figures of the Whig Party in North Carolina — organizing the anti-Jacksonian coalition"},
            {"entity": "Andrew Jackson (Nullification Crisis / Senate resignation)", "relationship": "RESIGNED_SENATE_SEAT_RATHER_THAN_FOLLOW_INSTRUCTIONS_OF", "note": "Resigned from the Senate (1836) rather than follow the Jacksonian legislature's instructions — a stand for senatorial independence over legislative mandate"},
            {"entity": "1836 presidential election (South Carolina 11 electoral votes)", "relationship": "WHIG_CANDIDATE_WHO_RECEIVED_SC_ELECTORAL_VOTES_IN", "note": "Received South Carolina's 11 electoral votes in the 1836 presidential election — part of the Whig strategy of running multiple regional candidates to deny Van Buren a majority"},
            {"entity": "John Tyler administration (vacant vice presidency)", "relationship": "SENATE_PRESIDENT_PRO_TEM_DURING_CONSTITUTIONAL_ANOMALY_OF", "note": "Served as Senate pro tem during Tyler's VP vacancy — the constitutional anomaly that made him second in succession for three years of institutional chaos"}
        ]
    }),

    # 6 — William Duer
    ("william-duer", {
        "summary": (
            "William Duer (1743–1799) was a British-born American financier, "
            "speculator, and Federalist politician who was Assistant Secretary "
            "of the Treasury under Alexander Hamilton (1789–1790) and who "
            "precipitated the Panic of 1792 — the first major financial "
            "market crash in American history. Born in England and educated "
            "at Eton, Duer came to America in the 1760s, served in the "
            "Continental Congress, attended the New York constitutional "
            "convention, and wrote as 'Philo-Publius' in support of ratifying "
            "the Constitution.\n\n"
            "Duer's financial career was characterized by extraordinary "
            "ambition and catastrophic risk: he used his Treasury position "
            "to obtain inside information about government securities, "
            "speculated massively in bank stocks and federal bonds using "
            "borrowed money, and organized a speculative conspiracy with "
            "business partner Alexander Macomb to corner the market in "
            "government securities. When the scheme collapsed in March 1792, "
            "it triggered a financial panic — sharp market crashes in New "
            "York and Philadelphia — that Hamilton had to stabilize through "
            "open-market operations (Treasury purchases of government securities "
            "to support their price) — the first use of monetary policy "
            "tools in American history.\n\n"
            "Duer was arrested for debt in 1792 and spent the remaining seven "
            "years of his life in debtors' prison — dying there in 1799. "
            "Hamilton, who had been personally close to Duer, was furious "
            "at the scandal and the political damage it caused his Treasury "
            "program. The Panic of 1792 illustrated both the dangers of "
            "insider trading at the government's financial institutions "
            "and the necessity of central bank stabilization mechanisms.\n\n"
            "His spectacular career and even more spectacular collapse "
            "made him one of the most cautionary figures in American "
            "financial history."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Hamilton's first Assistant Secretary of the Treasury (1789–1790); precipitated the Panic of 1792 — the first American financial market crash; wrote as 'Philo-Publius' supporting ratification; Continental Congress delegate; his collapse forced Hamilton to invent open-market monetary policy to stabilize markets.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Hamilton's Treasury program — establishing the Bank of the United States, funding the national debt, and creating a market in government securities — created the financial infrastructure that Duer then exploited for insider trading and speculative manipulation",
            "Duer's access to Treasury inside information — from his position as Hamilton's Assistant Secretary — gave him the information advantage that enabled his market-cornering scheme to grow far beyond sustainable levels",
            "The absence of regulatory frameworks governing insider trading, market manipulation, and financial speculation in the new American republic — the institutional void that Duer's collapse revealed and that subsequent generations would slowly fill"
        ],
        "effects": [
            "The Panic of 1792 — the first American financial market crash — demonstrated the systemic risk of speculative excess in the newly created federal financial markets and forced Hamilton to develop the first American open-market monetary policy operations",
            "Hamilton's Treasury response to the 1792 panic — using government purchases of securities to support their price — was the first use of central banking stabilization techniques in American history, anticipating by a century the Federal Reserve's core functions",
            "Duer's insider trading scandal — and the political damage it caused Hamilton's Treasury program — contributed to the political erosion of Federalist financial credibility and strengthened the Jeffersonian critique of Hamilton's system",
            "His seven years in debtors' prison — and his death there in 1799 — made the Panic of 1792 one of the most dramatic personal collapses in American financial history, a cautionary tale that shaped early American attitudes toward financial speculation"
        ],
        "relationships": [
            {"entity": "Panic of 1792 (first American financial market crash)", "relationship": "PRECIPITATOR_OF", "note": "His market-cornering scheme with Macomb collapsed in March 1792 — triggering the Panic of 1792, the first major American financial market crash"},
            {"entity": "Alexander Hamilton (Treasury Secretary / political casualty)", "relationship": "ASSISTANT_SECRETARY_WHOSE_CRASH_POLITICALLY_DAMAGED", "note": "Hamilton's first Assistant Secretary of the Treasury — whose insider trading scandal and market collapse caused significant political damage to Hamilton's Treasury program"},
            {"entity": "Open-market monetary policy (Treasury response, 1792)", "relationship": "CRASH_THAT_FORCED_INVENTION_OF", "note": "His panic forced Hamilton to use Treasury purchases of government securities to stabilize prices — the first use of open-market operations in American history, anticipating Federal Reserve techniques"},
            {"entity": "Continental Congress / New York constitutional convention", "relationship": "DELEGATE_TO", "note": "Served in the Continental Congress and attended New York's constitutional ratification convention — writing as 'Philo-Publius' in support of ratification"},
            {"entity": "Debtors' prison (New York, 1792–1799)", "relationship": "DIED_IN_AFTER_MARKET_COLLAPSE", "note": "Arrested for debt in 1792 after his speculative scheme collapsed — spending the remaining seven years of his life in debtors' prison until his death in 1799"}
        ]
    }),

    # 7 — Andrew Allen
    ("andrew-allen", {
        "summary": (
            "Andrew Allen (1740–1825) was a Philadelphia lawyer, provincial "
            "official, and Continental Congress delegate who became one of the "
            "most prominent American Loyalists of the Revolutionary War — "
            "a man who had initially supported colonial rights, served in the "
            "Second Continental Congress (1775–1776), and then reversed course "
            "and joined the British side in 1776, spending the rest of his "
            "life in exile in Britain. His trajectory — from colonial rights "
            "advocate to Loyalist exile — illustrated the ambivalent path "
            "of many wealthy Philadelphia elites who found independence too "
            "radical a step.\n\n"
            "Allen came from one of Pennsylvania's most distinguished and "
            "influential families: his father William Allen was Pennsylvania's "
            "chief justice and one of the wealthiest men in the colonies. "
            "Andrew served as Pennsylvania's last colonial attorney general "
            "(1769–1776) under the Crown — a position that gave him both "
            "legal prestige and political standing that he chose to preserve "
            "through Loyalism rather than sacrifice through revolution.\n\n"
            "His defection to the British in 1776 — shortly after serving "
            "in the Continental Congress — was a significant blow to the "
            "Patriot cause in Pennsylvania, reflecting the genuine ambivalence "
            "of much of Pennsylvania's wealthy elite toward independence. "
            "His property was confiscated, and he spent the remainder "
            "of his long life — dying at 85 in 1825 — in England, "
            "never returning to America.\n\n"
            "His life embodied the most painful choice of the Revolution: "
            "loyalty to established order versus the revolutionary rupture "
            "that created a new nation."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Pennsylvania's last colonial attorney general; Second Continental Congress delegate (1775–1776) who defected to the British in 1776 — one of the most prominent American Loyalists; son of Pennsylvania Chief Justice William Allen; property confiscated; died in English exile in 1825.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Pennsylvania's wealthy mercantile elite's deep ambivalence about independence — they had enough investment in the existing colonial order that revolutionary rupture threatened more than it promised — created the environment in which Allen's Loyalist choice was possible and comprehensible",
            "His family's deep Crown connections — his father William Allen was Pennsylvania's chief justice and one of its wealthiest men — created the social and economic ties to the existing order that made independence feel like destruction rather than liberation",
            "The Second Continental Congress's increasingly radical direction in 1775–1776 — toward independence rather than reconciliation — crossed the line beyond which Allen was willing to follow"
        ],
        "effects": [
            "His defection to the British in 1776 was a significant symbolic blow to the Patriot cause in Pennsylvania — demonstrating the genuine Loyalist sympathies among the colony's wealthy elite and weakening the unified-resistance narrative",
            "The confiscation of his family's property — and the exile of multiple Allen family members — illustrated the revolutionary transformation of Pennsylvania's social hierarchy that independence produced, sweeping away one of the colony's most prominent families",
            "His life in English exile until 1825 — outliving the Revolution by more than 40 years, dying in a world in which America had become an established independent republic — illustrated the poignant historical position of the Loyalist exiles",
            "His Continental Congress service before his defection demonstrated the genuine uncertainty about independence that characterized even the most politically engaged Americans in 1775–1776"
        ],
        "relationships": [
            {"entity": "Second Continental Congress (1775–1776)", "relationship": "DELEGATE_WHO_SUBSEQUENTLY_DEFECTED_TO_BRITISH", "note": "Served in the Second Continental Congress (1775–1776) — then defected to the British in 1776, becoming one of the most prominent American Loyalists"},
            {"entity": "Pennsylvania colonial attorney general (1769–1776)", "relationship": "LAST_COLONIAL_ATTORNEY_GENERAL_OF", "note": "Served as Pennsylvania's last colonial attorney general under the Crown — choosing to preserve this position through Loyalism rather than sacrifice it through revolution"},
            {"entity": "William Allen (Pennsylvania chief justice, father)", "relationship": "SON_OF", "note": "Son of William Allen — Pennsylvania's chief justice and one of the wealthiest colonists — whose family connections made Loyalism a natural inheritance"},
            {"entity": "American Loyalism / Philadelphia elite Loyalism", "relationship": "MOST_PROMINENT_CONTINENTAL_CONGRESS_DELEGATE_TO_BECOME", "note": "The most prominent Continental Congress delegate to subsequently defect to the British — illustrating the ambivalence of Philadelphia's wealthy elite toward independence"},
            {"entity": "English exile (1776–1825)", "relationship": "SPENT_REMAINDER_OF_LIFE_IN", "note": "Spent the remaining 49 years of his life in English exile after the Revolution — his property confiscated, never returning to America"}
        ]
    }),

    # 8 — Nathaniel Chipman
    ("nathaniel-chipman", {
        "summary": (
            "Nathaniel Chipman (1752–1843) was a Vermont lawyer, judge, "
            "and politician who was one of the most significant founding figures "
            "of Vermont — as Chief Justice of the Vermont Supreme Court "
            "(1789–1791, 1796–1803), as a US Senator from Vermont (1797–1803), "
            "and as one of the principal legal architects of Vermont's "
            "transition from independent republic to American statehood. "
            "A Yale College graduate and Continental Army veteran, Chipman "
            "settled in Tinmouth, Vermont after the war and became "
            "Vermont's leading lawyer-statesman in its earliest decades.\n\n"
            "Vermont's political status was unique in early America: "
            "it had been an independent republic from 1777 to 1791 — "
            "the Vermont Republic — before joining the United States as "
            "the 14th state. Chipman was a key figure in the legal and "
            "political negotiations that managed this transition, "
            "advocating for Vermont's admission and helping to draft "
            "the legal frameworks that integrated Vermont's existing "
            "legal system into the American constitutional order.\n\n"
            "He was also a political theorist of some distinction: "
            "his 'Sketches of the Principles of Government' (1793) "
            "was one of the first systematic attempts to analyze "
            "the constitutional principles of the new American republic "
            "from a Vermont perspective — an underappreciated contribution "
            "to early American political thought. He revised it as "
            "'Principles of Government' (1833) — still writing at 81.\n\n"
            "He lived to 91 — one of the longest-lived founding-generation "
            "statesmen — writing and revising his constitutional theory "
            "into extreme old age."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Vermont founding statesman; Chief Justice of the Vermont Supreme Court (1789–1803); US Senator from Vermont (1797–1803); key figure in Vermont's transition from independent republic to 14th state; author of 'Sketches of the Principles of Government' (1793) — an early American constitutional theory; lived to 91.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Vermont's unique political position — as an independent republic from 1777 to 1791 that needed to negotiate its transition to American statehood — created the legal and political challenges that Chipman's expertise was most needed to address",
            "Yale's legal and intellectual training — combined with Continental Army service — gave Chipman the credentials that made him Vermont's leading lawyer-statesman in its formative decades",
            "Vermont's need for experienced legal architects who could integrate its distinctive legal system and land titles (the New Hampshire grants controversy) into the American constitutional framework"
        ],
        "effects": [
            "His leadership in managing Vermont's transition from independent republic to American statehood (1791) contributed to the legal frameworks that allowed Vermont's existing institutions to be preserved within the American constitutional order",
            "His 'Sketches of the Principles of Government' (1793) was one of the first systematic American constitutional theories written outside the major coastal cities — contributing to the intellectual development of American constitutional thought from a frontier state perspective",
            "His Vermont Supreme Court tenure contributed to the development of Vermont's distinctive legal system — integrating common law precedents with Vermont's particular history of land grants, independent republic governance, and New England Puritan legal tradition",
            "His longevity — living to 91 and revising his constitutional theory at 81 — made him one of the few founding-generation statesmen who witnessed the full arc from Revolutionary War through Jacksonian democracy to the antebellum era"
        ],
        "relationships": [
            {"entity": "Vermont Republic (1777–1791) / Vermont statehood (1791)", "relationship": "KEY_LEGAL_ARCHITECT_OF_TRANSITION_FROM_REPUBLIC_TO", "note": "Key figure in managing Vermont's transition from independent republic to 14th state — advocating for admission and drafting legal frameworks for institutional integration"},
            {"entity": "Vermont Supreme Court (Chief Justice, 1789–1803)", "relationship": "CHIEF_JUSTICE", "note": "Served as Chief Justice of the Vermont Supreme Court (1789–1791, 1796–1803) — Vermont's leading jurist during its first two decades of statehood"},
            {"entity": "'Sketches of the Principles of Government' (1793)", "relationship": "AUTHOR_OF", "note": "Authored one of the first systematic American constitutional theories from a frontier state perspective — revised at 81 as 'Principles of Government' (1833)"},
            {"entity": "US Senate from Vermont (1797–1803)", "relationship": "SENATOR", "note": "Served as Vermont's US Senator (1797–1803) — representing the new state in Washington during the critical transition from Federalist to Jeffersonian governance"},
            {"entity": "Continental Army / Yale College (Vermont founding generation)", "relationship": "VETERAN_AND_ALUMNUS_WHO_FOUNDED_VERMONT_LEGAL_INSTITUTIONS", "note": "Continental Army veteran and Yale graduate who settled in Vermont and built its legal and judicial institutions in the years immediately following the Revolution"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 36)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
