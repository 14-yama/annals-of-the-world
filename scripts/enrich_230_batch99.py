#!/usr/bin/env python3
"""
Batch 99 — 8 entities: Abiel Foster, Adolf III of Nassau-Wiesbaden,
Aedanus Burke, Alexander Buckner, Alexander Martin, Alexander Porter,
Alexander Smyth, Alfred Iverson Sr.
"""
import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/230-Class-230"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()


def enrich(slug, data):
    fname = os.path.join(FOLDER, f"230{slug}.json")
    if not os.path.exists(fname):
        print(f"  SKIP: {fname}"); return
    with open(fname, "r", encoding="utf-8") as f:
        doc = json.load(f)
    entity = doc["entities"][0]
    dj = entity.get("detailsJson", "{}")
    det = json.loads(dj) if isinstance(dj, str) else dj
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
    print(f"  ✓ {entity['name']} — sum={slen}c c={len(det.get('causes',[]))} e={len(det.get('effects',[]))}")


ENTITIES = [

    ("abiel-foster", {
        "summary": (
            "Abiel Foster (1735–1806) was an American Federalist politician and "
            "Congregationalist minister from New Hampshire who served in both "
            "the Continental Congress (1783–1785) and later in the U.S. House "
            "of Representatives (1789–1791 and 1795–1803). His dual career as "
            "a minister and congressman exemplified the New England tradition "
            "of clerical civic engagement — the Congregationalist minister as "
            "a natural community leader who also served in politics. He served "
            "in the Continental Congress during the Confederation period — the "
            "years between the Revolution and the Constitution — and then "
            "returned to serve in the First Congress under the new constitution.\n\n"
            "His Canterbury New Hampshire ministry and congressional service "
            "made him one of the state's most consistent public figures across "
            "the revolutionary and founding eras.\n\n"
            "He was one of New Hampshire's earliest congressional voices.\n\n"
            "He was the minister-congressman of the founding era."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "New Hampshire Federalist Congregationalist minister-congressman who served in both the Continental Congress (1783–1785) and U.S. House (1789–1791 and 1795–1803); dual clerical and political career; served through the Confederation period, Constitutional transition, and early republic; Canterbury New Hampshire pastor.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New Hampshire's Congregationalist tradition — the state's culture of clerical civic leadership that made ministers natural candidates for public office — created the background for Foster's dual career",
            "The Confederation period's political needs — the Continental Congress's requirement for delegates from all states — created the opportunity for Foster's first national service",
            "New Hampshire's Federalist politics — the state's support for the new Constitution and Federalist governance — created the political context for Foster's congressional career under the new government"
        ],
        "effects": [
            "His Continental Congress service contributed to the Confederation period's legislative work",
            "His First Congress participation contributed to the establishment of the new federal government's institutions",
            "His long congressional career contributed to New Hampshire's consistent representation across the founding and early republic eras",
            "His dual clerical-political career contributed to the New England model of civic ministry — the minister who also served in government"
        ],
        "relationships": [
            {"target": "continental-congress", "verb": "SERVES_IN", "note": "New Hampshire delegate 1783–1785"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "New Hampshire congressman 1789–1791 and 1795–1803"},
            {"target": "first-congress", "verb": "SERVES_IN", "note": "Member of the First Congress under the new Constitution"},
            {"target": "federalist-party", "verb": "MEMBER_OF", "note": "New Hampshire Federalist politician"},
            {"target": "congregationalism", "verb": "SERVES_AS_MINISTER_OF", "note": "Canterbury New Hampshire Congregationalist pastor"}
        ]
    }),

    ("adolf-iii-of-nassau-wiesbaden", {
        "summary": (
            "Adolf III of Nassau-Wiesbaden (c. 1353–1420) was a German "
            "nobleman and count who ruled the County of Nassau-Wiesbaden "
            "in the late 14th and early 15th centuries. His county was one "
            "of several Nassau territories created by the partition of the "
            "Nassau comital house — the medieval practice of dividing "
            "territories among heirs that produced multiple Nassau branches. "
            "Nassau-Wiesbaden, situated in the Rhine-Main region, was a "
            "strategically important county whose rulers navigated the "
            "complex politics of the Holy Roman Empire — the relationships "
            "between counts, princes, the Emperor, and the Rhine cities.\n\n"
            "The late 14th century saw the Western Schism (1378–1417) "
            "dividing the Catholic Church — a crisis that affected all "
            "German princes who had to choose between competing popes.\n\n"
            "He was a Rhenish count ruling during the Western Schism era.\n\n"
            "He was a Nassau count in the Rhine-Main region."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Count of Nassau-Wiesbaden in the Rhine-Main region (c. 1353–1420); ruled during the Western Schism era (1378–1417); one of several Nassau territorial branches created by comital partitions; navigated Holy Roman Empire's complex county-prince-emperor relationships; Rhenish count of the late medieval period.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Nassau house's territorial partition — the medieval practice of dividing comital territories among heirs — created the multiple Nassau branches including Nassau-Wiesbaden that Adolf III ruled",
            "The Holy Roman Empire's political complexity — the empire's layered relationships between emperors, princes, and counts — created the political environment that Nassau-Wiesbaden's rulers had to navigate",
            "The Western Schism (1378–1417) — the division of the Catholic Church between competing popes — created the religious-political crisis that all German princes including Adolf III had to manage"
        ],
        "effects": [
            "His county rule contributed to the governance of Nassau-Wiesbaden during the late medieval period",
            "His Nassau-Wiesbaden line contributed to the eventual consolidation of Nassau territories into later Nassau principalities",
            "His Rhine-Main presence contributed to the regional political landscape of the Holy Roman Empire's Rhenish territories",
            "His rule during the Western Schism era contributed to the historical record of German comital responses to the church's division"
        ],
        "relationships": [
            {"target": "nassau-wiesbaden", "verb": "RULES", "note": "Count of Nassau-Wiesbaden c. 1353–1420"},
            {"target": "holy-roman-empire", "verb": "OPERATES_WITHIN", "note": "Rhenish count in the imperial political system"},
            {"target": "western-schism", "verb": "NAVIGATES_DURING", "note": "Ruled during the Catholic Church's schism 1378–1417"},
            {"target": "house-of-nassau", "verb": "MEMBER_OF", "note": "Nassau-Wiesbaden branch of the Nassau comital house"},
            {"target": "rhine-main-region", "verb": "GOVERNS_IN", "note": "Strategically placed Rhine-Main county"}
        ]
    }),

    ("aedanus-burke", {
        "summary": (
            "Aedanus Burke (1743–1802) was an Irish-born American Anti-Federalist "
            "politician and judge from South Carolina who served in the First "
            "Congress (1789–1791) and was one of the original architects of the "
            "Society of the Cincinnati controversy. Burke published a famous "
            "pamphlet in 1783 attacking the Society of the Cincinnati — the "
            "hereditary military fraternity formed by Continental Army officers — "
            "as an American aristocracy that threatened republican equality. "
            "His pamphlet ignited a nationwide debate and contributed to the "
            "Society's reform. In the First Congress, he was an outspoken "
            "critic of government ceremony, titles, and aristocratic pretension — "
            "opposing the formal titles proposed for the President.\n\n"
            "He also served as a South Carolina circuit court judge for many years.\n\n"
            "He was the Irish-born republican who fought against American aristocracy.\n\n"
            "'In republics, hereditary honor corrupts liberty.'"
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Irish-born South Carolina Anti-Federalist congressman (First Congress, 1789–1791) and judge; famous 1783 pamphlet attacking the Society of the Cincinnati as a nascent American aristocracy; ignited nationwide debate that led to the Society's reform; First Congress opponent of presidential titles and aristocratic ceremony; South Carolina circuit court judge.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Society of the Cincinnati's formation (1783) — the hereditary military fraternity formed by Continental Army officers — created the aristocratic threat to republican equality that Burke's pamphlet attacked",
            "Irish republican tradition — Burke's Irish origins and his experience of British aristocratic hierarchy — created the political sensibility that made him the most outspoken American opponent of hereditary privilege",
            "The First Congress's ceremonial debates — the question of what titles and formalities the new republican government should adopt — created the political battles that Burke fought in the House"
        ],
        "effects": [
            "His Cincinnati pamphlet contributed to the nationwide debate that led to the Society's reform — the removal of hereditary membership for non-firstborn sons",
            "His First Congress opposition to titles contributed to the republican simplicity that characterized the Washington administration's public culture",
            "His career contributed to the Anti-Federalist tradition of vigilance against aristocratic forms in republican government",
            "His South Carolina judgeship contributed to the state's legal institutions during the early republic"
        ],
        "relationships": [
            {"target": "first-congress", "verb": "SERVES_IN", "note": "Anti-Federalist South Carolina congressman 1789–1791"},
            {"target": "society-of-the-cincinnati", "verb": "ATTACKS", "note": "1783 pamphlet attacking the Society as American aristocracy"},
            {"target": "south-carolina", "verb": "REPRESENTS", "note": "Irish-born South Carolina politician and judge"},
            {"target": "anti-federalism", "verb": "CHAMPIONS", "note": "Anti-Federalist opponent of aristocratic forms in the republic"},
            {"target": "george-washington", "verb": "CRITICIZES_CEREMONIES_OF", "note": "Opposed formal presidential titles proposed in First Congress"}
        ]
    }),

    ("alexander-buckner", {
        "summary": (
            "Alexander Buckner (1785–1833) was an American Democratic politician "
            "from Missouri who served as U.S. Senator (1831–1833). Missouri was "
            "a frontier slave state that had entered the Union in 1821 after the "
            "Missouri Compromise — the sectional bargain that admitted Missouri "
            "as a slave state alongside Maine as a free state. Buckner's Senate "
            "career was cut short by his early death — he served only two years "
            "before dying in office. He was a Cape Girardeau Missouri lawyer "
            "whose brief Senate service gave Missouri representation during the "
            "Jacksonian era's early political transformations.\n\n"
            "Missouri's early Senate delegations were shaped by its frontier "
            "character and its position as the gateway to the trans-Mississippi "
            "West — the starting point for western expansion.\n\n"
            "He was a Missouri frontier Democrat who died in office.\n\n"
            "He served briefly in the Jacksonian Senate."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Missouri Democratic Senator (1831–1833) who died in office; Cape Girardeau Missouri lawyer; Missouri entered as slave state after the 1821 Compromise; brief Senate career during Jacksonian era; gateway-state senator representing the frontier trans-Mississippi West.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Missouri's 1821 statehood — the Missouri Compromise's admission of Missouri as a slave state — created the frontier state whose first Senate delegations Buckner joined",
            "Jacksonian democratic expansion — the broadening of political participation that characterized the 1820s–1830s — created the political culture in which Missouri Democrats like Buckner operated",
            "Missouri's frontier character — the gateway state's rapid settlement and its position as the departure point for western expansion — created the political environment of Buckner's brief Senate career"
        ],
        "effects": [
            "His Senate service contributed Missouri's Jacksonian Democratic voice to the early 1830s Congress",
            "His early death contributed to Missouri's need for Senate replacements in the volatile early statehood period",
            "His Cape Girardeau origins contributed to the frontier lawyer-politician tradition in Missouri's early Senate representation",
            "His brief career contributed to the historical record of Missouri's first-generation Senate delegations"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Missouri Senator 1831–1833 — died in office"},
            {"target": "missouri", "verb": "REPRESENTS", "note": "Cape Girardeau Missouri Democratic lawyer"},
            {"target": "missouri-compromise", "verb": "REPRESENTS_STATE_ADMITTED_UNDER", "note": "Senator from Missouri admitted under the 1821 Compromise"},
            {"target": "democratic-party-united-states", "verb": "MEMBER_OF", "note": "Jacksonian Democrat"},
            {"target": "andrew-jackson", "verb": "CONTEMPORARY_OF", "note": "Jacksonian era Missouri senator"}
        ]
    }),

    ("alexander-martin", {
        "summary": (
            "Alexander Martin (1740–1807) was an American Patriot politician "
            "and Continental Congress delegate from North Carolina who served "
            "as Governor of North Carolina twice (1782–1785 and 1789–1792) and "
            "as U.S. Senator (1793–1799). Martin was a delegate to the "
            "Constitutional Convention (1787) though he departed early without "
            "signing the Constitution. His two governorships framed North "
            "Carolina's transition from revolutionary state to federal republic — "
            "his first term came during the immediate post-Revolutionary period "
            "and his second during the new Constitution's ratification era. "
            "His Senate career followed, giving him a comprehensive service "
            "across legislative, executive, and constitutional founding roles.\n\n"
            "He was a Guilford County North Carolina planter and politician.\n\n"
            "He was North Carolina's most consistent political leader of the founding era.\n\n"
            "He governed North Carolina through its transition to the republic."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "North Carolina Patriot politician, twice Governor (1782–1785 and 1789–1792), U.S. Senator (1793–1799), and Constitutional Convention delegate (departed without signing); governed North Carolina through the Revolutionary aftermath and the constitutional transition; comprehensive founding-era service across all branches; Guilford County planter.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The American Revolution's political transformation — the creation of new state governments that needed experienced leaders — created the political context for Martin's first governorship in the immediate post-Revolutionary period",
            "The Constitutional Convention's framing process — the 1787 assembly that Martin attended though he departed without signing — created the constitutional moment Martin witnessed",
            "North Carolina's delayed ratification — the state's Anti-Federalist resistance that required two ratification conventions — created the political environment that Martin navigated as governor during the constitutional transition"
        ],
        "effects": [
            "His two governorships contributed to North Carolina's governance through the critical transition from revolutionary state to constitutional republic",
            "His Constitutional Convention attendance contributed to the historical record of North Carolina's founding-era participation",
            "His Senate service contributed North Carolina's voice to the new federal government's first years",
            "His comprehensive career contributed to the model of founding-era statesmanship — serving across all levels and branches of government"
        ],
        "relationships": [
            {"target": "north-carolina", "verb": "GOVERNS", "note": "Twice Governor 1782–1785 and 1789–1792"},
            {"target": "constitutional-convention-1787", "verb": "ATTENDS", "note": "Convention delegate who departed without signing"},
            {"target": "us-senate", "verb": "SERVES_IN", "note": "North Carolina Senator 1793–1799"},
            {"target": "american-revolution", "verb": "SERVES_DURING", "note": "Patriot politician and founding-era leader"},
            {"target": "continental-congress", "verb": "SERVES_IN", "note": "North Carolina Continental Congress delegate"}
        ]
    }),

    ("alexander-porter", {
        "summary": (
            "Alexander Porter (1785–1844) was an Irish-born American Whig "
            "politician and judge from Louisiana who served as U.S. Senator "
            "(1833–1837 and 1843–1844) and as an Associate Justice of the "
            "Louisiana Supreme Court (1821–1833). His Irish birth and "
            "Louisiana career made him one of the most distinctive figures "
            "in antebellum southern politics — Louisiana's French, Spanish, "
            "and American legal traditions created a unique legal environment "
            "that Porter helped shape as a Supreme Court justice. His Senate "
            "career came later, representing Louisiana's Whig commercial "
            "interests — the sugar planters and New Orleans merchants who "
            "supported the protective tariff that the Whig Party championed.\n\n"
            "He was an Attakapas region Louisiana planter and jurist.\n\n"
            "He was the Irish-born Louisiana jurist who shaped civil law.\n\n"
            "He brought common law to Louisiana's mixed legal tradition."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Irish-born Louisiana Whig Senator (1833–1837 and 1843–1844) and Louisiana Supreme Court Associate Justice (1821–1833); shaped Louisiana's unique mixed civil and common law tradition; represented Louisiana's sugar planter and New Orleans merchant Whig commercial interests; Attakapas region planter; brought common law training to a civil law state.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Louisiana's unique mixed legal tradition — the combination of French civil law, Spanish colonial law, and American common law — created the distinctive legal environment that Porter as a Supreme Court justice helped synthesize",
            "Louisiana's Whig commercial interests — the sugar planters and New Orleans merchants who supported the protective tariff — created the political base for Porter's Senate career",
            "Irish emigration to the American South — the flow of Irish lawyers and professionals to the antebellum United States — created the pattern that Porter exemplified: the Irish-born professional who rose to the top of a southern state's legal and political system"
        ],
        "effects": [
            "His Louisiana Supreme Court service contributed to the development of Louisiana's mixed civil-common law jurisprudence",
            "His Senate service contributed Louisiana's Whig commercial perspective to the antebellum Senate debates over tariffs and economic policy",
            "His career contributed to the model of Irish-born professionals rising to prominence in antebellum southern states",
            "His Louisiana legal work contributed to the codification and interpretation of Louisiana's unique legal heritage"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Louisiana Senator 1833–1837 and 1843–1844"},
            {"target": "louisiana-supreme-court", "verb": "SERVES_AS_JUSTICE_ON", "note": "Associate Justice 1821–1833"},
            {"target": "louisiana", "verb": "REPRESENTS", "note": "Attakapas region Irish-born planter and jurist"},
            {"target": "whig-party-united-states", "verb": "MEMBER_OF", "note": "Louisiana Whig commercial interests — sugar planters and merchants"},
            {"target": "louisiana-civil-law", "verb": "SHAPES", "note": "Helped synthesize civil and common law in Louisiana's mixed tradition"}
        ]
    }),

    ("alexander-smyth", {
        "summary": (
            "Alexander Smyth (1765–1830) was an Irish-born American military "
            "officer and Virginia Democratic-Republican congressman who became "
            "infamous for his failed command during the War of 1812. As a "
            "brigadier general commanding U.S. forces at the Niagara front, "
            "Smyth twice called for an invasion of Canada (November 1812) and "
            "twice cancelled it at the last moment — earning the contempt of his "
            "officers and the public ridicule of the press. His failed invasions "
            "were among the most embarrassing American military failures of the "
            "war. He later served in the U.S. House of Representatives "
            "(1817–1825 and 1827–1830) representing Virginia.\n\n"
            "His military disgrace contrasted with his later successful "
            "congressional career — Virginia's voters apparently forgave "
            "his Niagara failures.\n\n"
            "He was the general who never invaded Canada.\n\n"
            "'His proclamations were bolder than his actions.'"
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Irish-born Virginia brigadier general infamous for twice cancelling planned invasions of Canada at Niagara (November 1812) — among the most embarrassing American military failures of the War of 1812; later Virginia Democratic-Republican congressman (1817–1825 and 1827–1830); his failed command became a byword for military incompetence.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The War of 1812's Niagara front — the U.S. military's strategy of invading Canada through the Niagara corridor — created the theater of operations where Smyth's incompetence was exposed",
            "The U.S. Army's early war weaknesses — the poor training, disorganized logistics, and incompetent senior command that plagued the early War of 1812 — created the systemic failures that Smyth exemplified",
            "American military overconfidence — the early war assumption that Canada would be easily conquered — created the inflated proclamations that Smyth issued and then failed to back with action"
        ],
        "effects": [
            "His failed Niagara invasions contributed to the pattern of American military incompetence that characterized the early War of 1812",
            "His public ridicule contributed to the political pressure for military reform — the lessons learned from early war failures",
            "His later congressional career contributed Virginia's Democratic-Republican voice to post-war politics",
            "His career contributed to the historical record of the War of 1812's catalog of military failures and the political resilience of disgraced commanders"
        ],
        "relationships": [
            {"target": "war-of-1812", "verb": "FAILS_TO_COMMAND_IN", "note": "Niagara front commander who twice cancelled Canada invasions"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Virginia congressman 1817–1825 and 1827–1830"},
            {"target": "niagara-frontier", "verb": "COMMANDS_AT", "note": "Failed to invade Canada from Niagara November 1812"},
            {"target": "virginia", "verb": "REPRESENTS", "note": "Irish-born Virginia Democratic-Republican politician"},
            {"target": "us-army", "verb": "SERVES_IN", "note": "Brigadier general in the U.S. Regular Army"}
        ]
    }),

    ("alfred-iverson-sr", {
        "summary": (
            "Alfred Iverson Sr. (1798–1873) was an American Democratic politician "
            "from Georgia who served in the U.S. House (1847–1849) and as U.S. "
            "Senator (1855–1861). His Senate career was defined by the slavery "
            "crisis — he was one of Georgia's most outspoken defenders of "
            "slavery and southern rights. He resigned from the Senate in January "
            "1861 when Georgia seceded from the Union, delivering a farewell "
            "speech that predicted the Civil War and expressed confidence in "
            "the Confederate cause. His son Alfred Iverson Jr. became a "
            "Confederate general.\n\n"
            "He was a Columbus Georgia lawyer and planter whose career "
            "traced the arc of Georgia's antebellum politics — from "
            "Democratic nationalism through states' rights sectionalism "
            "to secession.\n\n"
            "He was one of Georgia's fire-eating secessionists.\n\n"
            "'Georgia leaves — and we will make good her cause with blood.'"
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Georgia Democratic Senator (1855–1861) and fire-eating secessionist who resigned on Georgia's secession January 1861; outspoken defender of slavery and southern rights; farewell speech predicting the Civil War; father of Confederate General Alfred Iverson Jr.; Columbus Georgia lawyer-planter tracing arc from Democratic nationalism to secession.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Georgia's antebellum plantation economy — the cotton and slave economy that made Georgia's political class fierce defenders of slavery — created the political culture that produced Iverson's fire-eating secessionism",
            "The sectional crisis of the 1850s — the Kansas-Nebraska Act, Bleeding Kansas, the Republican Party's rise, and the breakdown of compromise — created the escalating political pressure that pushed Iverson and Georgia toward secession",
            "The Republican Party's 1860 victory — Lincoln's election on an anti-slavery-extension platform — created the immediate trigger that Georgia and Iverson used to justify secession"
        ],
        "effects": [
            "His Senate secessionist advocacy contributed to Georgia's secession decision in January 1861",
            "His farewell speech contributed to the historical record of the Confederate cause's self-presentation — the arguments secessionists made for leaving the Union",
            "His son's Confederate generalship contributed to the Iverson family's military legacy in the Civil War",
            "His career contributed to the documentation of Georgia's arc from antebellum Democratic politics to secession and Confederacy"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Georgia Senator 1855–1861 — resigned on secession"},
            {"target": "georgia", "verb": "REPRESENTS", "note": "Columbus Georgia planter and fire-eating secessionist"},
            {"target": "confederate-states-of-america", "verb": "SUPPORTS_FOUNDING_OF", "note": "Resigned Senate on Georgia's secession January 1861"},
            {"target": "slavery", "verb": "DEFENDS", "note": "Outspoken Senate defender of slavery and southern rights"},
            {"target": "secession-crisis", "verb": "PARTICIPATES_IN", "note": "Fire-eating secessionist during the 1850s sectional crisis"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 99 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich(slug, data)
    print("Done.")
