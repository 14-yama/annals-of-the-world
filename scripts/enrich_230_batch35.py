#!/usr/bin/env python3
"""
Batch 35 — 8 entities: Aaron Burr, Thaddeus Stevens, Thomas Holliday Hicks,
Wilson Lumpkin, Aaron V. Brown, Samuel Hopkins, Increase Sumner, Charles Smith Olden
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

    # 1 — Aaron Burr
    ("aaron-burr", {
        "summary": (
            "Aaron Burr Jr. (1756–1836) was an American politician, military "
            "officer, and lawyer who served as the third Vice President of the "
            "United States (1801–1805) under Thomas Jefferson — and who became "
            "one of the most notorious figures in American history, remembered "
            "above all for killing Alexander Hamilton in a pistol duel at "
            "Weehawken, New Jersey on July 11, 1804. The duel, sparked by "
            "Hamilton's persistent opposition to Burr's political ambitions, "
            "ended the life of the first Secretary of the Treasury and "
            "effectively destroyed Burr's career — charging him with murder "
            "in New York and New Jersey and making him a political pariah.\n\n"
            "Before the duel, Burr had been a towering political figure: "
            "a Columbia College-educated Revolutionary War officer who served "
            "with distinction at Quebec (1775) and Monmouth (1778), a US Senator "
            "from New York (1791–1797), and the man who nearly became President "
            "of the United States in 1800 — when the Electoral College tied "
            "73–73 between Jefferson and Burr, sending the election to the House "
            "of Representatives, which required 36 ballots to elect Jefferson. "
            "Hamilton's opposition in that crisis — his preference for Jefferson "
            "over Burr — was the proximate cause of Burr's lifelong hatred.\n\n"
            "After the duel, Burr continued his career with characteristic "
            "audacity: he organized a mysterious 'western conspiracy' (1806–1807) "
            "whose true purpose — separating western territories from the US, "
            "conquering Mexico, or both — remains debated. President Jefferson "
            "had him arrested for treason. Chief Justice John Marshall's trial "
            "in Richmond acquitted Burr when Marshall held that 'levying war' "
            "required actual assembled troops — a landmark constitutional "
            "definition of treason.\n\n"
            "His trial set the constitutional standard for treason in the United "
            "States — a precedent as consequential, in its way, as the duel."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "3rd US Vice President (1801–1805); killed Alexander Hamilton in the Weehawken duel (July 11, 1804); tied with Jefferson in the 1800 presidential Electoral College — 73–73, requiring 36 House ballots; acquitted of treason (1807) after Marshall's landmark constitutional definition; a dominant figure in both political achievement and political destruction.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The 1800 Electoral College tie — 73 votes each for Jefferson and Burr — created the constitutional crisis that made Burr a near-President, gave Hamilton the pivotal role in denying him the presidency, and planted the seed of the fatal enmity that produced the 1804 duel",
            "Hamilton's systematic opposition to Burr's political ambitions — at both the 1800 House vote and the 1804 New York gubernatorial race — made Hamilton's destruction Burr's obsessive political goal, culminating in the duel challenge",
            "The cultural code of honor in early American politics — particularly in New York and New Jersey's Federalist and Republican elite — created the dueling culture in which Hamilton's insults to Burr's character demanded a formal pistol challenge under the dueling code"
        ],
        "effects": [
            "Hamilton's death removed the most brilliant financial and political mind of the Federalist Party — ending the only career in early American politics that might have sustained Federalist dominance, and leaving the party without its indispensable intellect",
            "The 1804 duel ended Burr's own career — murder charges in two states destroyed his political viability and transformed him from a near-President to a fugitive, making the duel the most politically self-destructive act in American political history",
            "Chief Justice Marshall's acquittal ruling in the 1807 treason trial — holding that 'levying war' required actually assembled troops — set the constitutional definition of treason that has governed American law ever since",
            "The 12th Amendment (1804) — adopted before Burr even dueled Hamilton, directly responding to the 1800 Electoral College crisis Burr had created — required separate presidential and vice-presidential ballots, preventing any future electoral tie between running mates"
        ],
        "relationships": [
            {"entity": "Alexander Hamilton (Weehawken duel, July 11, 1804)", "relationship": "KILLED_IN_DUEL", "note": "Shot and killed Alexander Hamilton at Weehawken, NJ on July 11, 1804 — the most consequential duel in American history, ending Hamilton's career and destroying Burr's"},
            {"entity": "1800 presidential election / House runoff (36 ballots)", "relationship": "TIED_WITH_JEFFERSON_IN_ELECTORAL_COLLEGE_OF", "note": "Tied with Jefferson 73–73 in the 1800 Electoral College — triggering the House runoff that required 36 ballots to elect Jefferson and produced the 12th Amendment"},
            {"entity": "Aaron Burr treason trial (1807) / Chief Justice Marshall", "relationship": "ACQUITTED_DEFENDANT_IN_LANDMARK_RULING_OF", "note": "Acquitted of treason by Marshall's landmark ruling — which held that 'levying war' required actually assembled troops, setting the constitutional standard for treason"},
            {"entity": "12th Amendment (1804)", "relationship": "1800_ELECTORAL_TIE_THAT_TRIGGERED", "note": "The 1800 Electoral College crisis he created — a 73–73 tie with Jefferson — directly triggered the 12th Amendment requiring separate presidential and vice-presidential ballots"},
            {"entity": "US Vice Presidency under Jefferson (1801–1805)", "relationship": "THIRD_VICE_PRESIDENT", "note": "Served as 3rd VP under Jefferson (1801–1805) — having nearly become President instead, and being systematically marginalized by Jefferson throughout the term"}
        ]
    }),

    # 2 — Thaddeus Stevens
    ("thaddeus-stevens", {
        "summary": (
            "Thaddeus Stevens (1792–1868) was a Pennsylvania Radical Republican "
            "congressman who was the most powerful legislator in the United States "
            "during the Civil War and Reconstruction eras — the driving force "
            "behind the most transformative legislative program in American "
            "history. Known as 'The Great Commoner,' Stevens used his position "
            "as House Ways and Means Committee chairman and then House Judiciary "
            "Committee chairman to shape the financing of the Civil War, the "
            "passage of the 13th, 14th, and 15th Amendments, the "
            "Reconstruction Acts (1867), and the impeachment of President "
            "Andrew Johnson (1868) — the first presidential impeachment in "
            "American history.\n\n"
            "Stevens was a lifelong and uncompromising enemy of slavery: "
            "a Pennsylvanian who had grown up in Vermont near the Canadian "
            "border, he defended escaped slaves in court for free throughout "
            "his career and was one of the founders of the Republican Party "
            "in Pennsylvania. His Reconstruction vision — 'Radical Reconstruction' "
            "— called for treating the former Confederate states as conquered "
            "provinces, confiscating planter land and redistributing it to "
            "freed people ('forty acres and a mule'), and guaranteeing Black "
            "political equality through federal power. Congress enacted most "
            "of this program over Johnson's vetoes.\n\n"
            "Stevens's personal life was as unconventional as his politics: "
            "his housekeeper Lydia Hamilton Smith — a free Black woman — "
            "was widely understood to be his common-law partner, a relationship "
            "Stevens neither confirmed nor denied. He requested burial in "
            "an integrated Lancaster, Pennsylvania cemetery because he could "
            "not rest in a segregated one — a final statement of his convictions.\n\n"
            "He died two months after the Johnson acquittal, having devoted "
            "his last year to the impeachment effort."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "The most powerful legislator during Civil War and Reconstruction; drove passage of 13th, 14th, 15th Amendments; authored the Reconstruction Acts (1867); led Andrew Johnson's impeachment (1868) — first presidential impeachment in US history; lifelong uncompromising abolitionist; Radical Reconstruction's architect.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Pennsylvania's growing anti-slavery movement and the Republican Party's founding coalition created the political base from which Stevens's Radical Republican leadership emerged — his Pennsylvania constituency consistently supported his most radical positions",
            "Andrew Johnson's systematic dismantling of Reconstruction — restoring former Confederate leaders to power, vetoing civil rights legislation, and allowing Southern states to pass Black Codes — created the confrontation with Congress that Stevens organized into the Radical Reconstruction program and eventually the impeachment",
            "The Union's military victory and the constitutional opportunity it created — the ability to rewrite the South's fundamental institutions through constitutional amendments and military occupation — created the legislative moment Stevens exploited with maximum effectiveness"
        ],
        "effects": [
            "The 13th, 14th, and 15th Amendments — which he drove through Congress — permanently abolished slavery, established birthright citizenship and equal protection, and guaranteed Black male suffrage: the most transformative constitutional additions in American history",
            "The Reconstruction Acts of 1867 — which he authored — divided the former Confederacy into five military districts and required Black suffrage as a condition of readmission, creating the brief period of Black political participation and governance that produced 16 Black congressmen and 2 Black US senators",
            "Johnson's impeachment (1868) — which Stevens organized and managed — established the constitutional limits of presidential resistance to congressional Reconstruction, even though Johnson survived by one vote in the Senate",
            "His vision of land redistribution — 'forty acres and a mule' — was never enacted, but its failure condemned freed people to sharecropping and economic dependency that undermined the political gains his amendments created: the most consequential legislative failure of Reconstruction"
        ],
        "relationships": [
            {"entity": "13th, 14th, 15th Amendments (Reconstruction Amendments)", "relationship": "PRIMARY_CONGRESSIONAL_DRIVER_OF", "note": "The most powerful force in Congress driving the three Reconstruction Amendments — permanently abolishing slavery, establishing equal citizenship, and guaranteeing Black male suffrage"},
            {"entity": "Reconstruction Acts (1867)", "relationship": "AUTHOR_OF", "note": "Authored the Reconstruction Acts — dividing the former Confederacy into military districts and requiring Black suffrage as a condition of readmission"},
            {"entity": "Andrew Johnson impeachment (1868)", "relationship": "ORGANIZER_AND_MANAGER_OF", "note": "Organized and managed the first presidential impeachment in American history — Johnson survived by one Senate vote, but the process established constitutional limits on presidential Reconstruction resistance"},
            {"entity": "Lydia Hamilton Smith (common-law partner)", "relationship": "COMPANION_OF", "note": "His housekeeper Lydia Hamilton Smith — a free Black woman — was widely understood to be his common-law partner, a relationship consistent with his lifelong commitment to racial equality"},
            {"entity": "Radical Republican Party / Reconstruction program", "relationship": "LEGISLATIVE_ARCHITECT_OF", "note": "The dominant legislative architect of Radical Reconstruction — treating the former Confederate states as conquered provinces requiring constitutional transformation before readmission"}
        ]
    }),

    # 3 — Thomas Holliday Hicks
    ("thomas-holliday-hicks", {
        "summary": (
            "Thomas Holliday Hicks (1798–1865) was the Governor of Maryland "
            "(1858–1862) whose crucial decisions in the weeks after Fort Sumter "
            "kept Maryland in the Union — a choice that may have saved Washington, "
            "D.C. itself. When pro-Confederate Marylanders rioted against Union "
            "troops in Baltimore on April 19, 1861 — in the Pratt Street Riot, "
            "the first Civil War bloodshed — and when Confederate sympathizers "
            "in the Maryland legislature demanded he call a special session to "
            "consider secession, Hicks refused. He delayed, obstructed, and "
            "eventually convened the legislature in Unionist Frederick instead "
            "of secessionist-leaning Annapolis — ensuring that the secession "
            "vote never had the votes to pass.\n\n"
            "Hicks's decision was consequential beyond measure: Maryland "
            "surrounded Washington on three sides (with Virginia on the fourth), "
            "and a Confederate Maryland would have isolated the capital, "
            "potentially requiring its abandonment. Lincoln had himself "
            "authorized the suspension of habeas corpus in Maryland and "
            "ordered the arrest of secessionist leaders — recognizing that "
            "Maryland's loyalty was the Union's most critical early vulnerability.\n\n"
            "Before the war, Hicks had been a Know-Nothing governor — a member "
            "of the nativist party that briefly dominated American politics "
            "in the 1850s. He was a slaveholder himself, and his Unionism "
            "was not about slavery's abolition — it was about his conviction "
            "that secession was unconstitutional and catastrophic.\n\n"
            "He later served as a US Senator from Maryland (1862–1865), dying "
            "in office in February 1865 — two months before the war's end."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Maryland Governor (1858–1862) whose refusal to call the legislature into special session after Fort Sumter kept Maryland in the Union — preserving Washington D.C.'s viability as the Union capital; Know-Nothing turned Unionist; US Senator (1862–1865, died in office); a single governor's decisions that shaped the entire Civil War.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Maryland's geographic position — surrounding Washington D.C. on three sides — made the state's loyalty the most critical single variable in the Civil War's opening weeks: a Confederate Maryland would have isolated the capital",
            "The Pratt Street Riot (April 19, 1861) — in which Baltimore mobs attacked Massachusetts troops passing through the city — created the immediate secession pressure that Hicks's refusal to convene the legislature was specifically designed to delay and defuse",
            "Hicks's personal Unionist convictions — his belief that secession was unconstitutional regardless of his views on slavery — created the moral framework that allowed him to resist the enormous Confederate pressure to call a secession vote"
        ],
        "effects": [
            "His refusal to call the legislature preserved Washington D.C. as the Union capital — a Confederate Maryland would have required the capital's abandonment and might have made Union victory logistically impossible in the war's critical early months",
            "Lincoln's suspension of habeas corpus in Maryland — and the arrest of secessionist state legislators — was made possible by Hicks's cooperation: together, they ensured the Maryland legislature could never muster a secession majority",
            "Maryland's retention in the Union contributed to the entire strategic geography of the Civil War: the Confederacy fought the war without its largest northern state, and Confederate invasions of the North (Antietam, Gettysburg) had to cross hostile rather than friendly Maryland territory",
            "His career demonstrated how a single official's decisions at a critical moment — refusing to convene a legislature, delaying a vote, choosing the right meeting location — can determine the outcome of a war"
        ],
        "relationships": [
            {"entity": "Maryland secession crisis (April–May 1861)", "relationship": "GOVERNOR_WHO_PREVENTED_SECESSION_DURING", "note": "Refused to call the Maryland legislature into special session — preventing the secession vote that Confederate sympathizers were demanding after Fort Sumter"},
            {"entity": "Washington D.C. (Union capital viability)", "relationship": "UNIONIST_DECISIONS_THAT_PRESERVED_CAPITAL_AT", "note": "His decisions kept Maryland in the Union — preserving Washington D.C.'s viability as the Union capital, as a Confederate Maryland would have surrounded and isolated it"},
            {"entity": "Pratt Street Riot / Baltimore (April 19, 1861)", "relationship": "GOVERNOR_DURING_FIRST_CIVIL_WAR_BLOODSHED_OF", "note": "Was governor when Baltimore mobs attacked Massachusetts troops in the Pratt Street Riot — the first Civil War bloodshed — and faced immediate Confederate pressure to convene a secession vote"},
            {"entity": "Abraham Lincoln / habeas corpus suspension in Maryland", "relationship": "COOPERATING_UNIONIST_WITH_WHOSE_AID_LINCOLN_ARRESTED_SECESSIONISTS", "note": "Cooperated with Lincoln's suspension of habeas corpus in Maryland — together ensuring the legislature could never muster a secession majority"},
            {"entity": "US Senate from Maryland (1862–1865)", "relationship": "SENATOR_WHO_DIED_IN_OFFICE", "note": "Served as US Senator from Maryland (1862–1865) after his governorship — dying in office in February 1865, two months before the war's end"}
        ]
    }),

    # 4 — Wilson Lumpkin
    ("wilson-lumpkin", {
        "summary": (
            "Wilson Lumpkin (1783–1870) was a Georgia planter, attorney, and "
            "politician who served two terms as Governor of Georgia (1831–1835) "
            "and as a US Senator (1837–1841) — and who is primarily remembered "
            "as a fervent advocate and executor of the forced removal of the "
            "Creek and Cherokee peoples from Georgia. His governorship coincided "
            "exactly with the Georgia-federal confrontation over Cherokee removal: "
            "Georgia had passed laws extending state jurisdiction over Cherokee "
            "territory, the Cherokee had appealed to the US Supreme Court "
            "(producing Marshall's two landmark Cherokee cases), and Jackson "
            "was refusing to enforce the Court's orders in their favor.\n\n"
            "Lumpkin's position was unambiguous and aggressive: he supported "
            "Georgia's extension of authority over Cherokee lands, defied "
            "the Supreme Court's rulings in Cherokee Nation v. Georgia (1831) "
            "and Worcester v. Georgia (1832), and pushed for the removal "
            "that Jackson's Indian Removal Act (1830) had authorized. "
            "The removal he advocated culminated in the Trail of Tears "
            "(1838–1839) — in which over 4,000 Cherokee died during the "
            "forced march to Oklahoma — after his governorship had ended.\n\n"
            "Atlanta's predecessor city Marthasville was originally named "
            "after his daughter Martha. When it was incorporated as Atlanta "
            "in 1847, the name changed — but Lumpkin County, Georgia preserves "
            "his memory, and Dahlonega (the center of Georgia's 1828 gold "
            "rush, which accelerated Cherokee removal) is its county seat.\n\n"
            "He lived to 87 — long enough to see the Confederacy he had "
            "helped build destroyed."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Georgia Governor (1831–1835) during the Cherokee removal crisis; aggressive advocate of Indian removal who defied Supreme Court rulings in Cherokee Nation v. Georgia (1831) and Worcester v. Georgia (1832); Atlanta's predecessor city Marthasville named for his daughter; Lumpkin County Georgia named for him.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Georgia's 1828 gold rush in the Cherokee territory — and the planters' hunger for the rich agricultural land the Cherokee occupied — created the economic and political pressure for removal that Lumpkin's governorship organized",
            "Jackson's Indian Removal Act (1830) and his refusal to enforce Marshall's Supreme Court rulings in favor of the Cherokee created the federal-state alignment that gave Lumpkin's removal policy its political backing",
            "Georgia's legislative extension of state jurisdiction over Cherokee territory — stripping the Cherokee of legal rights under Georgia law — created the constitutional confrontation with the Supreme Court that Lumpkin presided over as governor"
        ],
        "effects": [
            "The Trail of Tears (1838–1839) — the forced removal of over 16,000 Cherokee, of whom over 4,000 died — was the direct consequence of the removal program that Lumpkin and Jackson had organized during his governorship",
            "The Cherokee removal opened millions of acres of northwestern Georgia to white settlement and plantation agriculture — transforming the state's economic geography and accelerating the Cotton Kingdom's expansion",
            "The Worcester v. Georgia (1832) defiance — Georgia's refusal to comply with Marshall's ruling and Jackson's refusal to enforce it — established the dangerous precedent of states defying Supreme Court constitutional rulings with presidential acquiescence",
            "Atlanta (originally Marthasville, named for his daughter) became the railroad hub and later the capital of the New South — a city whose origin was inseparable from the Cherokee removal that cleared the land it was built on"
        ],
        "relationships": [
            {"entity": "Cherokee removal / Trail of Tears (1838–1839)", "relationship": "ADVOCATE_AND_ENABLER_OF", "note": "His governorship organized the political and legal framework for Cherokee removal — which culminated in the Trail of Tears after his term ended"},
            {"entity": "Worcester v. Georgia (1832) / Cherokee Nation v. Georgia (1831)", "relationship": "GEORGIA_GOVERNOR_WHO_DEFIED_SUPREME_COURT_RULINGS_IN", "note": "Defied Marshall's rulings recognizing Cherokee sovereignty — with Jackson's acquiescence — establishing the dangerous precedent of states ignoring Supreme Court constitutional orders"},
            {"entity": "Jackson's Indian Removal Act (1830)", "relationship": "STATE-LEVEL_ENFORCER_OF", "note": "Coordinated Georgia's removal policy with Jackson's Indian Removal Act — the federal-state partnership that made removal possible despite federal constitutional prohibitions"},
            {"entity": "Atlanta (originally Marthasville, named for daughter Martha)", "relationship": "CITY_NAMED_FOR_HIS_DAUGHTER_PREDECESSOR_OF", "note": "Atlanta's predecessor city Marthasville was named after his daughter Martha Lumpkin — connecting his removal legacy to Georgia's future commercial capital"},
            {"entity": "Lumpkin County, Georgia / Dahlonega gold rush (1828)", "relationship": "COUNTY_NAMESAKE_LINKED_TO", "note": "Lumpkin County preserves his memory — its county seat Dahlonega was the center of Georgia's 1828 gold rush that accelerated Cherokee removal"}
        ]
    }),

    # 5 — Aaron V. Brown
    ("aaron-v-brown", {
        "summary": (
            "Aaron Venable Brown (1795–1859) was a Tennessee Democratic politician "
            "and lawyer who served as the 11th Governor of Tennessee (1845–1847), "
            "as a US Representative (1839–1845, three terms), and as the 19th "
            "United States Postmaster General (1857–1859) under President "
            "James Buchanan — dying in office in March 1859 after barely two "
            "years in the role. A close ally of James K. Polk — his law partner "
            "and college friend at the University of North Carolina — Brown "
            "was one of the most prominent Tennessee Jacksonian Democrats "
            "of the antebellum era.\n\n"
            "Brown's governorship coincided with the final years of the "
            "Mexican-American War crisis — Polk's presidency — and his "
            "Tennessee constituency was passionately expansionist. As Postmaster "
            "General under Buchanan, Brown presided over one of the most "
            "consequential expansions in postal history: the introduction "
            "of the Butterfield Overland Mail (1857) — a 2,800-mile stagecoach "
            "mail route from St. Louis to San Francisco that was the fastest "
            "regular communication link between the East and the newly acquired "
            "California before the transcontinental telegraph (1861). "
            "The Butterfield route passed through the South — a routing "
            "decision that itself became politically controversial.\n\n"
            "Brown was also a slaveholder whose proslavery views were central "
            "to his political identity. He had been close to Polk from their "
            "shared North Carolina college days — a friendship that shaped "
            "his entire political career and gave him access to the Polk "
            "administration's inner circle.\n\n"
            "He died suddenly in March 1859 — two years before the Civil War "
            "whose coming he had contributed to by supporting Southern rights."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Tennessee Governor (1845–1847); US Postmaster General (1857–1859, died in office); established the Butterfield Overland Mail stagecoach route (2,800 miles, St. Louis to San Francisco); James K. Polk's law partner and closest political ally; prominent Jacksonian Tennessee Democrat.",
            "significanceCategory": "regional"
        },
        "causes": [
            "His close friendship and law partnership with James K. Polk — dating from their UNC college days — gave him access to the inner circle of Tennessee Jacksonian politics and to the Polk presidential administration",
            "California's admission as a state (1850) and the West's rapid growth created the urgent need for reliable mail communication between East and West that Brown's Butterfield Overland Mail contract was designed to address",
            "Tennessee's passionate Jacksonian Democratic tradition — expansionist, states' rights, pro-slavery — created the political culture in which Brown's career was built and sustained"
        ],
        "effects": [
            "The Butterfield Overland Mail (1857) — which he organized as Postmaster General — was the fastest regular communication link between the East and California before the transcontinental telegraph (1861), linking the nation across 2,800 miles of frontier territory",
            "His Southern routing of the Butterfield route became politically controversial — Northern critics argued the southern path through Texas and New Mexico was chosen for political rather than practical reasons, reflecting the sectional tensions of the Buchanan era",
            "His death in office in 1859 — two years before the Civil War — removed one of the most prominent Tennessee proslavery Democrats from the political landscape at the moment when compromise was still theoretically possible",
            "His career demonstrated the centrality of personal friendship networks in antebellum politics — his connection to Polk from their college days shaped his entire political trajectory"
        ],
        "relationships": [
            {"entity": "James K. Polk (11th President)", "relationship": "LAW_PARTNER_AND_CLOSEST_POLITICAL_ALLY_OF", "note": "Polk's law partner and college friend from their University of North Carolina days — a friendship that gave Brown access to the inner circle of Tennessee Jacksonian politics and the Polk administration"},
            {"entity": "Butterfield Overland Mail (1857)", "relationship": "POSTMASTER_GENERAL_WHO_ESTABLISHED", "note": "Established the Butterfield Overland Mail — a 2,800-mile St. Louis to San Francisco stagecoach route, the fastest East-West communication link before the transcontinental telegraph"},
            {"entity": "Tennessee governorship (1845–1847)", "relationship": "11TH_GOVERNOR", "note": "Served as 11th Governor of Tennessee (1845–1847) — Polk's closest Tennessee ally during Polk's presidency"},
            {"entity": "US Postmaster General (1857–1859, under Buchanan)", "relationship": "19TH_POSTMASTER_GENERAL_DIED_IN_OFFICE", "note": "Served as 19th US Postmaster General under Buchanan (1857–1859) — dying in office in March 1859 after establishing the Butterfield Overland Mail"},
            {"entity": "Jacksonian Democratic Party (Tennessee)", "relationship": "PROMINENT_LEADER_OF", "note": "One of the most prominent Tennessee Jacksonian Democrats of the antebellum era — combining expansionist nationalism with pro-slavery states' rights"}
        ]
    }),

    # 6 — Samuel Hopkins
    ("samuel-hopkins", {
        "summary": (
            "Samuel Hopkins (1753–1819) was a Kentucky lawyer, soldier, and "
            "politician who had one of the most varied careers of any figure "
            "in the early American republic — serving in the Continental Army "
            "on the staff of George Washington during the Revolutionary War, "
            "settling in Kentucky after the war, serving multiple terms in the "
            "Kentucky legislature, and representing Kentucky's 5th congressional "
            "district in the US House (1813–1815) during the War of 1812. "
            "He also served as a general in the Kentucky militia during the War "
            "of 1812 — leading expeditions against Native American communities "
            "in the Indiana and Illinois territories.\n\n"
            "Hopkins was part of the generation of Revolutionary War veterans "
            "who carried Washington's army experience into the early republic's "
            "western frontier politics — the soldier-politicians who settled "
            "Virginia's former land grants in Kentucky and Tennessee and built "
            "the first institutions of American governance in the trans-Appalachian "
            "West. His Washington staff service gave him a social distinction "
            "that opened Kentucky's legislative and congressional doors.\n\n"
            "His War of 1812 militia expeditions — leading Kentucky volunteers "
            "against Native American communities allied with the British in the "
            "Northwest — placed him in the broader military conflict that also "
            "featured William Henry Harrison's Tippecanoe campaign and the "
            "Battle of the Thames. His expeditions had mixed results but "
            "contributed to the American military pressure on the Northwest frontier.\n\n"
            "Hopkins County, Kentucky is named in his honor — preserving his "
            "memory in the western Kentucky region he helped settle."
        ),
        "importanceScore": 5,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Kentucky Revolutionary War veteran (Washington's staff); Kentucky congressman (1813–1815) during War of 1812; Kentucky militia general; Hopkins County Kentucky named for him; soldier-politician of the founding western frontier generation.",
            "significanceCategory": "regional"
        },
        "causes": [
            "His Continental Army service on Washington's staff during the Revolutionary War established the social credentials and military experience that opened Kentucky's political doors after his post-war western migration",
            "Kentucky's frontier politics — dominated by Revolutionary War veterans who had received Virginia land grants — created the political community in which Hopkins's soldier-statesman credentials were most valued",
            "The War of 1812's frontier dimension — the British-Native American alliance in the Northwest — created the military context in which his Kentucky militia generalship found its operational role"
        ],
        "effects": [
            "His War of 1812 militia expeditions contributed to the American military pressure on the Northwest frontier — part of the broader campaign that eventually destroyed the British-Native American alliance with the Battle of the Thames",
            "His congressional service during the War of 1812 provided Kentucky's representation in Washington during the most important military conflict of the early republic's western experience",
            "Hopkins County, Kentucky — named in his honor — preserved his memory in the western Kentucky region he helped settle and develop",
            "His career exemplified the soldier-statesman pattern of the founding frontier generation — Revolutionary War veterans who translated military service under Washington into political standing in the trans-Appalachian West"
        ],
        "relationships": [
            {"entity": "Continental Army / George Washington's staff", "relationship": "STAFF_OFFICER_UNDER_DURING_REVOLUTION", "note": "Served on Washington's staff during the Revolutionary War — the social distinction that launched his post-war Kentucky political career"},
            {"entity": "Kentucky (US House, 1813–1815)", "relationship": "CONGRESSIONAL_REPRESENTATIVE_DURING_WAR_OF_1812", "note": "Represented Kentucky's 5th congressional district (1813–1815) — serving in Congress during the War of 1812"},
            {"entity": "Kentucky militia (War of 1812, NW frontier expeditions)", "relationship": "GENERAL_COMMANDING_EXPEDITIONS_IN", "note": "Led Kentucky militia expeditions against British-allied Native American communities in Indiana and Illinois territories during the War of 1812"},
            {"entity": "Hopkins County, Kentucky", "relationship": "NAMESAKE_OF", "note": "Hopkins County in western Kentucky is named in his honor — preserving his memory in the region he helped settle"},
            {"entity": "Trans-Appalachian western frontier politics (Kentucky)", "relationship": "FOUNDING_SOLDIER-STATESMAN_OF", "note": "Part of the generation of Revolutionary War veterans who carried Washington's army experience into the early republic's western frontier politics"}
        ]
    }),

    # 7 — Increase Sumner
    ("increase-sumner", {
        "summary": (
            "Increase Sumner (1746–1799) was a Massachusetts lawyer, jurist, "
            "and politician who served as the fifth Governor of Massachusetts "
            "(1797–1799) — dying in office in June 1799 after only two years "
            "as governor. A Harvard-educated lawyer, Sumner had served in "
            "Massachusetts's provisional government during the Revolutionary "
            "War and subsequently built a distinguished judicial career on "
            "the Massachusetts Supreme Judicial Court (1782–1797) — rising "
            "to Associate Justice before his election as governor.\n\n"
            "Sumner was the father of Charles Pinckney Sumner — and through "
            "him, the grandfather of Charles Sumner — the Massachusetts "
            "antislavery senator who was beaten with a cane on the Senate floor "
            "by South Carolina's Preston Brooks in 1856 in one of the most "
            "notorious incidents in American political history. The family "
            "lineage from Increase Sumner through his grandson Charles Sumner "
            "traced a path from Federalist judicial Massachusetts to Radical "
            "Republican abolitionism.\n\n"
            "Increase Sumner's gubernatorial tenure coincided with the "
            "Quasi-War with France (1798–1800) — the undeclared naval war "
            "triggered by the XYZ Affair — and with the Adams administration's "
            "Alien and Sedition Acts. As a Federalist governor of a Federalist "
            "state, Sumner generally supported Adams's foreign policy positions "
            "during this contentious period.\n\n"
            "His death in office at 52 cut short what might have been a more "
            "prominent gubernatorial career at a crucial moment in Massachusetts "
            "and national politics."
        ),
        "importanceScore": 5,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "5th Governor of Massachusetts (1797–1799, died in office); Massachusetts Supreme Judicial Court associate justice; grandfather of Charles Sumner (the abolitionist senator beaten on the Senate floor in 1856); Federalist jurist during the Quasi-War and Alien and Sedition Acts.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Harvard's legal education and Massachusetts's Federalist judicial culture created the professional environment in which Sumner's distinguished SJC career was built — elevating him to the governorship",
            "Massachusetts's Federalist political dominance in the late 1790s — and its support for Adams's foreign policy during the Quasi-War — created the political alignment that Sumner's governorship represented",
            "His SJC tenure — 15 years as an associate justice — gave him the judicial standing and institutional reputation that translated into gubernatorial electability in Federalist Massachusetts"
        ],
        "effects": [
            "His gubernatorial tenure provided Massachusetts's executive leadership during the Quasi-War with France — supporting Adams's foreign policy at a moment of genuine naval conflict with a European power",
            "His death in office at 52 removed Massachusetts's Federalist governor at a critical moment — creating a succession that affected the state's political development in the critical election year of 1800",
            "His son Charles Pinckney Sumner and grandson Charles Sumner carried the family's public service tradition from Federalist judicial Massachusetts all the way to Radical Republican abolitionism — one of the most dramatic political lineage transformations in American history",
            "His 15-year SJC tenure contributed to the development of Massachusetts's legal system during the critical post-Revolutionary period when American common law was being systematically developed from English precedents"
        ],
        "relationships": [
            {"entity": "Massachusetts governorship (1797–1799, died in office)", "relationship": "5TH_GOVERNOR_DIED_IN_OFFICE", "note": "Served as 5th Governor of Massachusetts (1797–1799) — dying in office in June 1799 after only two years"},
            {"entity": "Charles Sumner (abolitionist senator, grandson)", "relationship": "GRANDFATHER_OF", "note": "Grandfather of Charles Sumner — the Massachusetts abolitionist senator who was beaten with a cane on the Senate floor by Preston Brooks in 1856"},
            {"entity": "Massachusetts Supreme Judicial Court (1782–1797)", "relationship": "ASSOCIATE_JUSTICE", "note": "Served as Associate Justice of the Massachusetts SJC for 15 years — the judicial career that established his public standing before his governorship"},
            {"entity": "Quasi-War with France (1798–1800) / XYZ Affair", "relationship": "FEDERALIST_GOVERNOR_DURING", "note": "His governorship coincided with the Quasi-War and Adams's Alien and Sedition Acts — supporting Adams's Federalist foreign policy as governor"},
            {"entity": "Federalist Party (Massachusetts, late 1790s)", "relationship": "PROMINENT_FEDERALIST_GOVERNOR_OF", "note": "Led Massachusetts's executive branch during the height of Federalist political dominance in the late 1790s"}
        ]
    }),

    # 8 — Charles Smith Olden
    ("charles-smith-olden", {
        "summary": (
            "Charles Smith Olden (1799–1876) was a New Jersey merchant, banker, "
            "and politician who served as the 19th Governor of New Jersey "
            "(1860–1863) — the only opposition-party governor to serve in the "
            "critical first years of the Civil War while managing the immense "
            "pressure of a border state with strong Democratic and Confederate-sympathy "
            "constituencies. As a Constitutional Unionist elected in 1859 — "
            "when the nation was fragmenting into four-party chaos — Olden "
            "governed a state that was deeply divided between its industrial "
            "north (pro-Lincoln) and its agricultural south (strongly Democratic "
            "and peace-sympathizing).\n\n"
            "Despite his Constitutional Unionist affiliation — and his personal "
            "preference for a negotiated peace and opposition to emancipation — "
            "Olden consistently supported the Union war effort: he worked to "
            "meet New Jersey's troop quotas, cooperated with federal requisitions, "
            "and kept the state formally on the Union side despite intense "
            "Democratic pressure for a peace settlement. His position was "
            "a constant balancing act between supporting Lincoln's war aims "
            "and placating a state legislature and population deeply skeptical "
            "of those aims.\n\n"
            "Olden had previously served as an Associate Justice of the New "
            "Jersey Supreme Court (1852–1859) — bringing a judicial temperament "
            "to the executive office. He was also a trustee of the College "
            "of New Jersey (later Princeton University) — maintaining the "
            "educated gentleman-statesman tradition of New Jersey's governing class.\n\n"
            "After his governorship, he returned to private business — his "
            "Civil War tenure never attracting the national attention it deserved."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "19th Governor of New Jersey (1860–1863); Constitutional Unionist who consistently supported the Union war effort despite his state's strong Democratic/peace-sympathizing constituencies; NJ Supreme Court Associate Justice; Princeton trustee; governed New Jersey through the Civil War's critical first years.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New Jersey's deeply divided Civil War politics — industrial north pro-Lincoln, agricultural south strongly Democratic and peace-sympathizing — created the governing challenge that Olden navigated through his entire wartime tenure",
            "The 1859 Constitutional Unionist political moment — the four-party fragmentation that produced Lincoln's 1860 election — created the electoral opening that allowed a non-partisan Constitutional Unionist to win New Jersey's governorship",
            "His NJ Supreme Court tenure gave him the judicial temperament and institutional reputation that made him an acceptable compromise candidate for New Jersey's fragmented political electorate"
        ],
        "effects": [
            "His consistent support for Union war aims — meeting troop quotas, cooperating with federal requisitions — kept New Jersey formally in the Union's active military contribution despite its Democratic legislature's resistance",
            "His balancing of Unionist executive action with Democratic political accommodation contributed to the pattern of border-state and divided-state governance that kept the Union's industrial base intact",
            "His Constitutional Unionist identification — distinct from both Republican and Democratic parties — illustrated the political complexity of Civil War governance in states where neither major party commanded a clear majority",
            "New Jersey's continued Union contribution under his tenure — providing troops, tax revenue, and industrial output — was part of the Union's economic foundation for winning the war"
        ],
        "relationships": [
            {"entity": "New Jersey governorship (1860–1863)", "relationship": "19TH_GOVERNOR_DURING_CIVIL_WAR", "note": "Governed New Jersey through the Civil War's first three years — balancing Unionist war aims against his state's strong Democratic and peace-sympathizing constituencies"},
            {"entity": "Constitutional Unionist Party (1860)", "relationship": "ELECTED_GOVERNOR_AS", "note": "Won the New Jersey governorship as a Constitutional Unionist — the four-party political moment of 1859–1860 when the existing party system was fragmenting"},
            {"entity": "New Jersey Supreme Court (Associate Justice, 1852–1859)", "relationship": "ASSOCIATE_JUSTICE_BEFORE_GOVERNORSHIP", "note": "Served as NJ Supreme Court Associate Justice (1852–1859) — bringing judicial temperament to the executive office"},
            {"entity": "College of New Jersey / Princeton University", "relationship": "TRUSTEE_OF", "note": "Served as trustee of the College of New Jersey (later Princeton University) — reflecting the gentleman-statesman tradition of New Jersey's governing class"},
            {"entity": "Union war effort / New Jersey troop quotas", "relationship": "CONSISTENT_SUPPORTER_DESPITE_PEACE-SYMPATHIZING_STATE", "note": "Consistently met troop quotas and cooperated with federal requisitions — supporting Lincoln's war aims despite intense Democratic pressure for peace settlement"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 35)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
