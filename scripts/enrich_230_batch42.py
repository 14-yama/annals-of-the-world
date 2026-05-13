#!/usr/bin/env python3
"""
Batch 42 — 8 entities: George Walton, Richard Hutson, John Alexander Cocke,
Martin D. Hardin, Josiah J. Evans, William Bellinger Bulloch,
Levi Lincoln Jr., Jeremiah Smith
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

    # 1 — George Walton
    ("george-walton", {
        "summary": (
            "George Walton (c.1749–1804) was a Georgia lawyer, "
            "planter, and Founding Father — one of three Georgia "
            "signers of the Declaration of Independence alongside "
            "Button Gwinnett and Lyman Hall. Born in Virginia, "
            "he moved to Georgia as a young man, studied law, and "
            "built a successful legal practice in colonial Savannah "
            "before joining the Patriot cause.\n\n"
            "His Revolutionary War career combined political "
            "leadership with a dramatic military episode: while "
            "simultaneously serving as a Continental Congress delegate "
            "and a Georgia militia colonel, he was wounded in the leg "
            "and captured by British forces during the Siege of "
            "Savannah in December 1778 — one of the most catastrophic "
            "American defeats of the southern campaign, in which "
            "the British retook Georgia. He spent months as a "
            "British prisoner before being exchanged.\n\n"
            "After the war, he served twice as Governor of Georgia — "
            "briefly in 1779 (nominally, while still in captivity) "
            "and again in 1789–1790 — and as a US Senator (1795–1796) "
            "completing an unexpired term. But his longest and most "
            "significant post-war role was as a Georgia Superior "
            "Court judge, a position he held through most of the "
            "1790s, where he contributed to building Georgia's "
            "early state judiciary.\n\n"
            "His Declaration signing remains his most historically "
            "significant act — cementing Georgia's commitment to "
            "the independence cause at a time when the colony "
            "had the smallest European population and the most "
            "precarious revolutionary organization of any of the "
            "thirteen."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Georgia signer of the Declaration of Independence (1776), alongside Button Gwinnett and Lyman Hall; wounded and captured during the Siege of Savannah (December 1778); twice Governor of Georgia (1779, 1789–1790); US Senator (1795–1796); Georgia Superior Court judge; one of the founding generation's most militarily tested political figures.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Georgia's small and fragile Patriot organization — the colony had the least developed revolutionary infrastructure of any of the thirteen — required figures of Walton's legal and social standing to take on multiple simultaneous roles as Continental Congress delegate, militia officer, and state executive to sustain the revolution",
            "The British southern strategy — which shifted military focus to Georgia and the Carolinas in 1778–1779 — created the military crisis that led to the Siege of Savannah and Walton's capture, transforming him from a political figure into a military prisoner of war",
            "Georgia's need for experienced legal and judicial figures after the Revolution — in a state whose professional class had been severely disrupted by the war and Loyalist emigration — created the demand for Walton's judicial service that occupied most of his post-war career"
        ],
        "effects": [
            "His Declaration signing in 1776 committed Georgia permanently to the independence cause — a crucial signal given the colony's small Patriot population and the vulnerability that would be demonstrated when the British retook Savannah in December 1778",
            "His capture and imprisonment at the Siege of Savannah (1778) made him one of the most visible American political prisoners of the Revolutionary War — a prominent Continental Congress delegate taken prisoner in the field, whose eventual exchange was a diplomatic and political event",
            "His two gubernatorial terms contributed to Georgia's early state governance — providing executive leadership in the difficult years of Reconstruction after British occupation and the subsequent reorganization of Georgia's revolutionary institutions",
            "His decade of service as Georgia Superior Court judge contributed to the early establishment of Georgia's state judiciary — building the legal infrastructure of a state that had been severely disrupted by the Revolutionary War's southern campaign"
        ],
        "relationships": [
            {"entity": "Declaration of Independence (Georgia signer, 1776)", "relationship": "SIGNER", "note": "Signed the Declaration of Independence as one of Georgia's three signers — alongside Button Gwinnett and Lyman Hall — committing the colony to the independence cause"},
            {"entity": "Siege of Savannah (December 1778) / British recapture of Georgia", "relationship": "WOUNDED_AND_CAPTURED_AT", "note": "Was wounded in the leg and captured by British forces during the Siege of Savannah in December 1778 — spending months as a British prisoner before exchange"},
            {"entity": "Governor of Georgia (1779 nominally, 1789–1790 actively)", "relationship": "TWICE_GOVERNOR", "note": "Served twice as Governor of Georgia — nominally in 1779 while still in British captivity, and actively in 1789–1790 after the war"},
            {"entity": "US Senate from Georgia (1795–1796, unexpired term)", "relationship": "SENATOR", "note": "Served as US Senator from Georgia (1795–1796) completing an unexpired term — one of several post-war public positions"},
            {"entity": "Georgia Superior Court (judge through most of 1780s–1790s)", "relationship": "JUDGE", "note": "Served as Georgia Superior Court judge through most of the 1780s–1790s — his longest continuous post-war service, contributing to Georgia's early state judiciary"}
        ]
    }),

    # 2 — Richard Hutson
    ("richard-hutson", {
        "summary": (
            "Richard Hutson (1747–1795) was a South Carolina Founding "
            "Father — a Charleston lawyer, judge, and planter who "
            "served in the Continental Congress (1778–1779), as "
            "Lieutenant Governor of South Carolina, and as a judge "
            "of the state's court system. The son of a Congregationalist "
            "minister, he was born in 1747 in St. George's Parish, "
            "educated at Princeton (the College of New Jersey), "
            "admitted to the South Carolina bar, and built a "
            "successful Charleston legal practice.\n\n"
            "His Continental Congress service in 1778–1779 came "
            "during one of the war's most consequential strategic "
            "shifts: the British were intensifying their southern "
            "strategy and South Carolina was about to become a "
            "major theater of operations. Hutson was part of the "
            "South Carolina delegation navigating the Congress "
            "as the Siege of Savannah (1778) and the subsequent "
            "fall of Charleston (1780) unfolded.\n\n"
            "His service as Lieutenant Governor of South Carolina "
            "placed him at the center of the state's post-war "
            "political reconstruction — a period of intense "
            "factional conflict between competing Patriot groups "
            "and the difficult social and economic reorganization "
            "after British occupation. He later served as a judge "
            "of the state court of equity — contributing to the "
            "legal reconstruction of post-war South Carolina.\n\n"
            "He is one of the less celebrated South Carolina "
            "Founding Fathers — overshadowed by the Rutledges, "
            "Pinckneys, and Laurens — but his career illustrates "
            "the depth of South Carolina's revolutionary elite, "
            "which was the largest and most professionally accomplished "
            "in the South."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "South Carolina Founding Father; Princeton-educated Charleston lawyer; Continental Congress delegate (1778–1779) during the critical period of the British southern strategy; Lieutenant Governor of South Carolina; South Carolina state judge; son of a Congregationalist minister whose family was rooted in Charleston's most distinguished religious community.",
            "significanceCategory": "regional"
        },
        "causes": [
            "South Carolina's need for experienced Charleston lawyers to represent the state in the Continental Congress during the British southern strategy's intensification in 1778–1779 created the demand for figures like Hutson with the professional and social standing to serve effectively",
            "The Princeton-educated cohort of South Carolina revolutionary leaders — who shared educational networks with the northern founding generation — provided the intellectual and institutional connections that shaped Hutson's political career",
            "South Carolina's post-war political reconstruction — and its need for judges and administrators who had served the Patriot cause — created the judicial positions that occupied the later phase of Hutson's career"
        ],
        "effects": [
            "His Continental Congress service (1778–1779) contributed to South Carolina's representation during the critical period of the British southern campaign — helping to articulate the state's interests as the war shifted to the South and South Carolina became a primary theater",
            "His Lieutenant Governor service contributed to South Carolina's post-war political reconstruction — managing the difficult transition from British occupation to Patriot-controlled governance in one of the war's most disrupted states",
            "His judicial service contributed to the legal reconstruction of post-war South Carolina — establishing the court system's authority and procedures in a state whose legal infrastructure had been severely disrupted by the Revolutionary War",
            "His career illustrated the depth of South Carolina's revolutionary leadership class — a professional and planting elite that was large enough to staff Continental Congress, state executive, and state judiciary positions simultaneously during the war's most demanding years"
        ],
        "relationships": [
            {"entity": "Continental Congress (South Carolina delegate, 1778–1779)", "relationship": "DELEGATE", "note": "Served as a South Carolina Continental Congress delegate (1778–1779) during the critical shift in the British war strategy toward the South"},
            {"entity": "Lieutenant Governor of South Carolina (post-war)", "relationship": "LIEUTENANT_GOVERNOR", "note": "Served as Lieutenant Governor of South Carolina — contributing to the post-war political reconstruction of a state that had been under British occupation"},
            {"entity": "South Carolina state court of equity (judge)", "relationship": "JUDGE", "note": "Served as a judge of the South Carolina court of equity — contributing to the legal reconstruction of post-war South Carolina"},
            {"entity": "Princeton / College of New Jersey (educated)", "relationship": "EDUCATED_AT", "note": "Educated at Princeton — part of the Princeton-educated cohort of South Carolina revolutionary leaders who shared educational networks with the northern founding generation"},
            {"entity": "Charleston legal and planting elite (South Carolina revolutionary class)", "relationship": "MEMBER_OF", "note": "A member of Charleston's professional and planting elite — the large and accomplished revolutionary leadership class that could staff multiple institutional roles simultaneously during the war"}
        ]
    }),

    # 3 — John Alexander Cocke
    ("john-alexander-cocke", {
        "summary": (
            "John Alexander Cocke (1772–1854) was a Tennessee "
            "militia general and politician who commanded the Eastern "
            "Division of Tennessee's forces during the Creek War "
            "(1813–1814) — and whose military service created one "
            "of the most bitter personal conflicts of Andrew Jackson's "
            "military career. Cocke and Jackson clashed directly "
            "over the enlistment and discharge of Tennessee militia "
            "troops: Cocke, acting on his own authority, discharged "
            "a significant number of militia whose enlistment status "
            "was disputed — an action Jackson viewed as insubordinate "
            "and damaging to the campaign. Jackson had Cocke "
            "court-martialed for mutiny; he was ultimately acquitted.\n\n"
            "Despite this violent breach with the man who would "
            "become the most powerful American politician of the "
            "1820s–1830s, Cocke went on to a substantial congressional "
            "career: he represented Tennessee's 2nd district in "
            "the US House of Representatives from 1819 to 1827, "
            "serving four terms and building a political reputation "
            "independent of Jackson's patronage network. He also "
            "served multiple terms in both the Tennessee Senate "
            "and the Tennessee House of Representatives, including "
            "two terms as Speaker of the Tennessee House.\n\n"
            "His congressional career coincided with the rise "
            "of Jacksonian politics — a politically awkward "
            "situation that he navigated by focusing on Tennessee's "
            "local and sectional interests rather than aligning "
            "himself with or against Jackson's national movement.\n\n"
            "He retired from Congress in 1827 and returned to "
            "his Tennessee estate, where he lived until 1854 — "
            "outliving Jackson by nine years."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Tennessee militia general; commanded Eastern Division during Creek War (1813–1814); had violent military conflict with Andrew Jackson — court-martialed for mutiny but acquitted; US Representative from Tennessee (1819–1827, 4 terms); Speaker of Tennessee House; his Jackson conflict illustrates the personal costs of crossing the future president.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Creek War's demanding frontier logistics — and the chronic difficulty of maintaining Tennessee militia forces in the field for extended periods under disputed enlistment terms — created the conditions for the conflict between Cocke and Jackson over troop discharges",
            "Jackson's absolute insistence on military discipline and his refusal to tolerate any independent action by subordinate commanders — the character trait that made him a militarily effective if personally terrifying commander — created the inevitable clash with Cocke's independent command decisions",
            "Tennessee's frontier political culture — which valued military service and personal honor as the foundations of political credibility — made Cocke's subsequent congressional career possible despite his Jackson conflict, because the Creek War acquittal preserved his honor and his standing with Tennessee voters"
        ],
        "effects": [
            "His court-martial and acquittal in the Creek War created one of the earliest documented cases of an Andrew Jackson subordinate successfully resisting Jackson's military authority — contributing to the historical documentation of Jackson's command style and its conflicts with independent officers",
            "His four-term congressional career (1819–1827) contributed to Tennessee's representation in the House during the Missouri Compromise debates and the beginning of the Jacksonian political transformation that would dominate the next decade",
            "His two terms as Speaker of the Tennessee House — combined with his state Senate service — contributed to Tennessee's early legislative institutional development in the period before Jacksonian democracy transformed the state's political culture",
            "His decades-long survival despite his bitter conflict with Jackson — living until 1854, nine years after Jackson's death — illustrated that political figures who challenged Jackson could survive professionally if they had independent institutional bases and the resilience to weather his displeasure"
        ],
        "relationships": [
            {"entity": "Andrew Jackson / Creek War conflict (court-martial for mutiny, acquitted)", "relationship": "COURT-MARTIALED_BY_AND_ACQUITTED", "note": "Had a violent military conflict with Andrew Jackson during the Creek War — Jackson court-martialed him for mutiny over disputed militia discharges, but he was acquitted"},
            {"entity": "Creek War (1813–1814) / Eastern Division of Tennessee forces", "relationship": "COMMANDED_EASTERN_DIVISION_DURING", "note": "Commanded the Eastern Division of Tennessee's militia forces during the Creek War — serving alongside but conflicting with Jackson's overall command"},
            {"entity": "US House of Representatives from Tennessee 2nd district (1819–1827, 4 terms)", "relationship": "4-TERM_CONGRESSMAN", "note": "Served four terms as US Representative from Tennessee's 2nd district (1819–1827) — building a congressional career independent of Jackson's patronage network"},
            {"entity": "Tennessee House of Representatives (Speaker, two terms)", "relationship": "TWO-TERM_SPEAKER_OF", "note": "Served as Speaker of the Tennessee House of Representatives for two terms — contributing to Tennessee's early legislative institutional development"},
            {"entity": "Tennessee state legislature (Senate and House, multiple terms)", "relationship": "MULTI-TERM_LEGISLATOR", "note": "Served multiple terms in both the Tennessee Senate and House — building the state political foundation for his subsequent congressional career"}
        ]
    }),

    # 4 — Martin D. Hardin
    ("martin-d-hardin", {
        "summary": (
            "Martin D. Hardin (1780–1823) was a Kentucky lawyer "
            "and politician who served as US Senator from Kentucky "
            "(1816–1817) — completing the unexpired term of a "
            "deceased senator — and previously as Kentucky Secretary "
            "of State. Born in Pennsylvania, his family migrated "
            "to Kentucky and he studied law under the distinguished "
            "George Nicholas, the Virginia constitutional lawyer who "
            "had moved to Kentucky and become the principal architect "
            "of the first Kentucky Constitution.\n\n"
            "His legal mentorship under George Nicholas — one of "
            "the most significant figures in early Kentucky legal "
            "and political history — gave Hardin both constitutional "
            "training and access to the network of Virginia-Kentucky "
            "gentry that dominated early Kentucky politics. "
            "He practiced law in Richmond, Kentucky, and contributed "
            "to the development of Kentucky's early legal culture.\n\n"
            "His Senate appointment (1816–1817) was brief — completing "
            "only a few months of an unexpired term — but his earlier "
            "service as Kentucky Secretary of State (1810–1816) "
            "was more substantive, placing him at the administrative "
            "center of Kentucky's state government during the War "
            "of 1812 era. His cousin Benjamin Hardin later became "
            "a prominent Kentucky US Representative — part of the "
            "broader Hardin family's contribution to Kentucky "
            "political life.\n\n"
            "He died in 1823 at age 43 — his career cut short "
            "before he could fully realize the potential that "
            "his legal training and family connections suggested."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Kentucky US Senator (1816–1817, completing unexpired term); Kentucky Secretary of State (1810–1816); studied law under George Nicholas — principal architect of the first Kentucky Constitution; his cousin Benjamin Hardin was a future US Representative; died aged 43 with a career cut short.",
            "significanceCategory": "regional"
        },
        "causes": [
            "His legal training under George Nicholas — one of the most distinguished constitutional lawyers of the early republic, who had moved from Virginia to Kentucky to draft its first constitution — provided Hardin with both professional excellence and the network connections that supported his political career",
            "Kentucky's early political structure — dominated by Virginia-origin gentry families who had migrated across the mountains — created the social framework in which the Hardin family's connections and legal reputation could translate into political positions",
            "The vacancy in Kentucky's US Senate seat created by a sitting senator's death — and the governor's power of appointment to fill the vacancy — created the opening that brought Hardin briefly to the US Senate in 1816"
        ],
        "effects": [
            "His service as Kentucky Secretary of State (1810–1816) contributed to the administrative management of Kentucky's state government during the War of 1812 — a period of significant military mobilization and political tension on the western frontier",
            "His brief Senate appointment (1816–1817) contributed to Kentucky's representation in Congress during the transition from the Era of Good Feelings to the Jacksonian political realignment",
            "His legal career in Richmond, Kentucky — building on his training under George Nicholas — contributed to the development of central Kentucky's legal culture in the early republic period",
            "The Hardin family's multiple contributions to early Kentucky political life — through Martin's secretarial and Senate service and his cousin Benjamin's later congressional career — illustrated the importance of family networks in shaping the political geography of early western states"
        ],
        "relationships": [
            {"entity": "US Senate from Kentucky (1816–1817, completing unexpired term)", "relationship": "SENATOR", "note": "Served as US Senator from Kentucky (1816–1817) — appointed to complete the unexpired term of a deceased senator"},
            {"entity": "George Nicholas (law teacher, principal architect of first Kentucky Constitution)", "relationship": "STUDIED_LAW_UNDER", "note": "Studied law under George Nicholas — the Virginia constitutional lawyer who moved to Kentucky and became the principal drafter of the first Kentucky Constitution"},
            {"entity": "Kentucky Secretary of State (1810–1816)", "relationship": "SECRETARY_OF_STATE", "note": "Served as Kentucky Secretary of State (1810–1816) — placed at the administrative center of Kentucky's state government during the War of 1812 era"},
            {"entity": "Benjamin Hardin (cousin, future US Representative from Kentucky)", "relationship": "COUSIN_OF", "note": "Cousin of Benjamin Hardin — a future prominent Kentucky US Representative who studied law in Martin's office — illustrating the Hardin family's multigenerational contribution to Kentucky political life"},
            {"entity": "Early Kentucky legal and political culture (Virginia-origin gentry)", "relationship": "PRACTITIONER_AND_POLITICAL_FIGURE_IN", "note": "A practitioner of early Kentucky law within the Virginia-origin gentry network that dominated the state's early political culture — his career shaped by the family and legal connections of the state's founding generation"}
        ]
    }),

    # 5 — Josiah J. Evans
    ("josiah-j-evans", {
        "summary": (
            "Josiah James Evans (1786–1858) was a South Carolina "
            "lawyer and Democratic politician who served as US "
            "Senator from South Carolina from 1853 until his death "
            "in 1858 — five years of antebellum Senate service "
            "during the most fraught period of the sectional crisis "
            "before the Civil War. Born in Marlborough District, "
            "South Carolina, he graduated third in his class from "
            "South Carolina College in 1808, studied law under his "
            "brother-in-law, and built a career as a state judge "
            "before his Senate election.\n\n"
            "His Senate tenure (1853–1858) placed him at the center "
            "of American political history's most intense five years: "
            "the Kansas-Nebraska Act controversy (1854), the Bleeding "
            "Kansas period of guerrilla violence (1856), the "
            "Preston Brooks caning of Charles Sumner on the Senate "
            "floor (1856), and the Dred Scott decision (1857) — "
            "all events in which South Carolina's senators were "
            "expected to take and defend firm proslavery positions.\n\n"
            "As a South Carolina Democrat in the Pierce and early "
            "Buchanan era, Evans was a reliable voice for Southern "
            "interests in the Senate debates over territorial "
            "expansion and the status of slavery — supporting the "
            "South's position that enslaved people could be brought "
            "into any territory without congressional restriction.\n\n"
            "He died in May 1858 — three years before the Civil "
            "War broke out — as the crisis he had witnessed was "
            "accelerating toward the irreversible."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "US Senator from South Carolina (1853–1858, died in office); antebellum proslavery Democrat; his Senate tenure encompassed the Kansas-Nebraska Act, Bleeding Kansas, the Preston Brooks caning of Sumner, and the Dred Scott decision; South Carolina College graduate (class of 1808, third in class); career state judge before Senate.",
            "significanceCategory": "regional"
        },
        "causes": [
            "South Carolina's political culture of planter-class governance — and its need for reliable proslavery voices in the Senate during the sectional crisis's escalation — created the demand for senators like Evans who could articulate the state's position in the Kansas-Nebraska debates",
            "His South Carolina College education and subsequent legal career — including his state judicial service — provided the professional credentials that made him a credible Senate candidate for a state that valued legal and judicial distinction in its political leaders",
            "The Pierce administration's Democratic coalition — and its southern wing's dominance in the early 1850s — created the political environment in which Evans's election as a South Carolina senator was straightforward given his legal and judicial standing"
        ],
        "effects": [
            "His Senate service contributed to South Carolina's proslavery representation during the Kansas-Nebraska crisis (1854) — the pivotal legislative event that reopened the territorial slavery question and accelerated the sectional crisis toward Civil War",
            "His presence in the Senate during the Preston Brooks caning of Charles Sumner (1856) — an event in which a South Carolina congressman attacked a Massachusetts senator on the Senate floor — placed him as a witness to one of the most symbolically violent moments of the antebellum crisis",
            "His death in 1858 — before the Civil War — spared him from having to decide between secession and union, but his five years of Senate service had contributed to the entrenchment of South Carolina's proslavery political positions that made secession inevitable",
            "His graduation from South Carolina College (third in the class of 1808) and subsequent legal career illustrated the pattern of South Carolina's planter-class political elite: college education, legal training, state judicial service, and eventual Senate election as the capstone of a distinguished career"
        ],
        "relationships": [
            {"entity": "US Senate from South Carolina (1853–1858, died in office)", "relationship": "SENATOR", "note": "Served as US Senator from South Carolina from 1853 until his death in May 1858 — five years encompassing the most intense phase of the antebellum sectional crisis"},
            {"entity": "Kansas-Nebraska Act (1854) / Bleeding Kansas crisis", "relationship": "SENATOR_DURING", "note": "Served in the Senate during the Kansas-Nebraska Act debates (1854) and the Bleeding Kansas guerrilla conflict — a reliable proslavery voice for South Carolina's position"},
            {"entity": "Preston Brooks caning of Charles Sumner (Senate floor, 1856)", "relationship": "SENATOR_PRESENT_DURING", "note": "Present in the Senate during the Preston Brooks caning of Charles Sumner in 1856 — one of the most violent symbolic moments of the antebellum crisis"},
            {"entity": "Dred Scott decision (1857)", "relationship": "SENATOR_DURING", "note": "Served in the Senate when the Dred Scott decision was handed down in 1857 — the Supreme Court ruling that declared Congress had no power to restrict slavery in the territories"},
            {"entity": "South Carolina College (class of 1808, graduated third)", "relationship": "EDUCATED_AT", "note": "Graduated third in his class from South Carolina College in 1808 — part of the educated planter-class elite that the college supplied to South Carolina's political life"}
        ]
    }),

    # 6 — William Bellinger Bulloch
    ("william-bellinger-bulloch", {
        "summary": (
            "William Bellinger Bulloch (1777–1852) was a Georgia "
            "planter and politician who served as a US Senator "
            "from Georgia in 1813 — completing the unexpired "
            "term of a deceased senator. He was the youngest son "
            "of Governor Archibald Bulloch (7th Governor of Georgia, "
            "1776–1777) and is primarily significant for his place "
            "in one of the most remarkable genealogical networks "
            "in American political history: the Bulloch-Roosevelt "
            "family that connected Georgia's revolutionary era "
            "to the 20th-century White House.\n\n"
            "Through his family connections, William Bellinger "
            "Bulloch was the uncle of James Stephens Bulloch, "
            "the great-uncle of James Dunwoody Bulloch (Confederate "
            "Secret Service agent who procured the CSS Alabama), "
            "and the great-uncle of Martha Bulloch — who married "
            "Theodore Roosevelt Sr. and became the mother of "
            "President Theodore Roosevelt Jr. He was also the "
            "great-granduncle of Eleanor Roosevelt.\n\n"
            "His own Senate career was brief — completing only "
            "months of an unexpired term — but his membership "
            "in the Bulloch family dynasty made him a figure "
            "in Georgia's most politically and genealogically "
            "significant antebellum family. The Bullochs' "
            "Revolutionary origins (through Governor Archibald), "
            "Confederate military service (through James Dunwoody), "
            "and White House connection (through Martha Bulloch "
            "Roosevelt) represented one of the most layered "
            "American family histories.\n\n"
            "He lived to 75, one of the last survivors of the "
            "Georgia revolutionary generation's second cohort."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Georgia US Senator (1813, completing unexpired term); youngest son of Governor Archibald Bulloch (7th Georgia Governor); uncle of James Stephens Bulloch; great-uncle of Martha Bulloch Roosevelt (mother of President Theodore Roosevelt Jr.) and of Confederate agent James Dunwoody Bulloch; great-granduncle of Eleanor Roosevelt; member of the extraordinary Bulloch-Roosevelt genealogical network.",
            "significanceCategory": "regional"
        },
        "causes": [
            "His birth as the youngest son of Governor Archibald Bulloch — one of Georgia's founding political figures — gave him the social standing and family connections that made his brief Senate appointment possible",
            "Georgia's pattern of filling Senate vacancies from the established planter-political elite — the network of revolutionary-era families from which the Bulloch family drew its standing — created the institutional mechanism for his brief Senate service",
            "The Bulloch family's deep roots in Georgia's revolutionary and antebellum planting elite created the genealogical network that connected William Bellinger's career to the larger family's extraordinary subsequent history"
        ],
        "effects": [
            "His brief Senate service (1813) contributed to Georgia's representation in Congress during the War of 1812 — a period of significant national significance for a state whose Gulf Coast position made it adjacent to the theater of operations",
            "His place as youngest son of Governor Archibald Bulloch made him a generational link in the Bulloch family dynasty — between the revolutionary governor and the antebellum generation that produced Martha Bulloch Roosevelt and James Dunwoody Bulloch",
            "The Bulloch family's combined history — from Archibald's Revolutionary governorship through William Bellinger's Senate service, James Dunwoody's Confederate agency, Martha Bulloch's marriage into the Roosevelt family, and Eleanor Roosevelt's 20th-century prominence — represented an extraordinary 150-year arc of American history through a single Georgia family",
            "His 75-year lifespan (1777–1852) made him a witness to the full span of American history from the Revolution through the antebellum crisis — a living connection between Georgia's founding generation and the era that produced the Civil War"
        ],
        "relationships": [
            {"entity": "US Senate from Georgia (1813, completing unexpired term)", "relationship": "SENATOR", "note": "Served briefly as US Senator from Georgia in 1813 — completing the unexpired term of a deceased senator"},
            {"entity": "Governor Archibald Bulloch (father, 7th Georgia Governor)", "relationship": "YOUNGEST_SON_OF", "note": "Youngest son of Governor Archibald Bulloch — the 7th Governor of Georgia (1776–1777) and the family's revolutionary founding figure"},
            {"entity": "Martha Bulloch Roosevelt (great-niece, mother of President Theodore Roosevelt Jr.)", "relationship": "GREAT-UNCLE_OF", "note": "Great-uncle of Martha Bulloch Roosevelt — who married Theodore Roosevelt Sr. and became the mother of President Theodore Roosevelt Jr., connecting the Bulloch family to the White House"},
            {"entity": "James Dunwoody Bulloch (great-nephew, Confederate CSS Alabama agent)", "relationship": "GREAT-UNCLE_OF", "note": "Great-uncle of James Dunwoody Bulloch — the Confederate Secret Service agent in Europe who procured the CSS Alabama, Theodore Roosevelt's uncle on his mother's side"},
            {"entity": "Eleanor Roosevelt (great-great-grandniece, First Lady)", "relationship": "GREAT-GREAT-GRANDUNCLE_OF", "note": "Great-great-granduncle of Eleanor Roosevelt — the First Lady who was Theodore Roosevelt's niece, extending the Bulloch genealogical network to the 20th century White House"}
        ]
    }),

    # 7 — Levi Lincoln Jr.
    ("levi-lincoln-jr", {
        "summary": (
            "Levi Lincoln Jr. (1782–1868) was a Massachusetts lawyer "
            "and politician — the son of Levi Lincoln Sr. (Jefferson's "
            "Attorney General) and elder brother of Enoch Lincoln "
            "(6th Governor of Maine) — who served as the 13th "
            "Governor of Massachusetts from 1825 to 1834, holding "
            "the longest consecutive gubernatorial tenure in "
            "Massachusetts history at nine years. He was subsequently "
            "elected to the US Congress (1834–1841), completing "
            "a public career that made the Lincoln family one of "
            "New England's most significant political dynasties.\n\n"
            "His nine-year governorship was remarkable for its "
            "institutional achievement: he was the first Governor "
            "of Massachusetts since John Hancock to be elected "
            "to so many consecutive terms — a record that still "
            "stands as the longest uninterrupted gubernatorial "
            "tenure in Massachusetts. His administration spanned "
            "the turbulent transition from National Republican "
            "to Whig politics, the Jacksonian transformation "
            "of American democracy, and the early stirrings "
            "of antislavery agitation in Massachusetts.\n\n"
            "Lincoln was a National Republican who evolved into "
            "a Whig — a political trajectory that represented "
            "Massachusetts's mainstream from the 1820s through "
            "the 1840s. He was a moderate, institutionally-minded "
            "politician who focused on Massachusetts's economic "
            "development — particularly its early industrialization "
            "and transportation infrastructure — rather than "
            "ideological confrontation.\n\n"
            "He lived to 86, dying in 1868 — the year the "
            "14th Amendment was ratified — having witnessed "
            "American history from the Jefferson presidency "
            "through the Civil War's resolution."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "13th Governor of Massachusetts (1825–1834) — longest consecutive gubernatorial tenure in Massachusetts history, nine years; US Congressman (1834–1841); son of Jefferson's Attorney General Levi Lincoln Sr.; elder brother of Maine Governor Enoch Lincoln; National Republican/Whig; his family represented one of New England's most significant 19th-century political dynasties.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Massachusetts's National Republican and later Whig political culture — which valued institutional stability, economic development, and moderate opposition to Jacksonian democracy — created the political environment in which Lincoln's nine consecutive terms as governor were possible",
            "The Lincoln family's deep roots in Massachusetts-Maine political life — his father as Jefferson's Attorney General, his brother as Maine's governor — provided the family networks and political credibility that supported Levi Jr.'s unprecedented gubernatorial tenure",
            "Massachusetts's early industrialization and the need for a governor who could manage the political and economic transitions of the factory system, canal building, and railroad development — without antagonizing either the manufacturing interests or the agricultural constituency — created the moderating role that Lincoln's administration filled"
        ],
        "effects": [
            "His nine consecutive gubernatorial terms (1825–1834) provided Massachusetts with unprecedented executive continuity through the political transformation from National Republican to Whig politics and the economic transition from commerce to industry",
            "His administration contributed to Massachusetts's early industrial development — supervising infrastructure projects, canal building, and the early railroad legislation that transformed the state's economy during the 1820s–1830s",
            "His subsequent congressional service (1834–1841) contributed to Massachusetts's House representation during the early Whig-Jacksonian battles over banking, tariffs, and antislavery agitation",
            "The Lincoln family's three-generational political achievement — Levi Sr. as Jefferson's AG, Enoch as Maine's governor, Levi Jr. as Massachusetts's longest-serving governor — represented one of the most sustained contributions by a single family to New England's early republican governance"
        ],
        "relationships": [
            {"entity": "13th Governor of Massachusetts (1825–1834, nine consecutive terms)", "relationship": "LONGEST_CONSECUTIVE_GOVERNOR", "note": "Served nine consecutive terms as Massachusetts's 13th Governor (1825–1834) — the longest uninterrupted gubernatorial tenure in Massachusetts history"},
            {"entity": "Levi Lincoln Sr. (father, Jefferson's Attorney General)", "relationship": "SON_OF", "note": "Son of Levi Lincoln Sr. — Jefferson's Attorney General (1801–1805) — whose political legacy and family connections supported Levi Jr.'s unprecedented gubernatorial tenure"},
            {"entity": "Enoch Lincoln (younger brother, 6th Governor of Maine, died in office 1829)", "relationship": "ELDER_BROTHER_OF", "note": "Elder brother of Enoch Lincoln — who served as Maine's 6th Governor and died in office in 1829 at age 40, the Lincoln family's parallel New England governorships"},
            {"entity": "National Republican / Whig Party (Massachusetts, 1820s–1840s)", "relationship": "LEADER_OF_IN_MASSACHUSETTS", "note": "A leading Massachusetts National Republican who evolved into a Whig — representing the state's mainstream moderate politics through the Jacksonian transformation"},
            {"entity": "US House of Representatives from Massachusetts (1834–1841)", "relationship": "CONGRESSMAN_AFTER_GOVERNORSHIP", "note": "Served in Congress (1834–1841) after his record-breaking governorship — continuing his public service in the House during the early Whig-Jacksonian battles"}
        ]
    }),

    # 8 — Jeremiah Smith
    ("jeremiah-smith", {
        "summary": (
            "Jeremiah Smith (1759–1842) was a New Hampshire Federalist "
            "lawyer and jurist who built one of the most varied "
            "legal and political careers of the founding era — "
            "serving as US Representative from New Hampshire "
            "(1791–1797), US Attorney for New Hampshire (1797–1800), "
            "judge of the US Circuit Court for the First Circuit "
            "(1801–1802), Chief Justice of the New Hampshire "
            "Superior Court of Judicature (1802–1809, 1813–1816), "
            "and 6th Governor of New Hampshire (1809–1810). "
            "Born in Peterborough, New Hampshire, he served "
            "briefly in the Revolutionary War, graduated from "
            "Harvard in 1780, and studied law.\n\n"
            "His congressional career (1791–1797) placed him among "
            "the Federalist majority of the early republic — "
            "supporting Hamilton's financial program, the Jay Treaty, "
            "and the Washington and Adams administrations' "
            "foreign policy during the contentious 1790s. "
            "His subsequent judicial career — spanning more than "
            "a decade on the New Hampshire Supreme Court — was "
            "his most sustained contribution to American law.\n\n"
            "Smith's reputation as a jurist was high in the early "
            "national period: he was known as a learned and "
            "principled judge who contributed to the development "
            "of New Hampshire common law through hundreds of "
            "decisions. He was a contemporary and close professional "
            "associate of Daniel Webster, who began his legal career "
            "in New Hampshire during Smith's tenure.\n\n"
            "His Federalist politics became increasingly anachronistic "
            "as Jacksonian democracy transformed New England, "
            "but he remained a respected legal elder statesman "
            "into his eighties — dying in 1842 at age 82."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "New Hampshire Federalist; US Representative (1791–1797); US Attorney for NH (1797–1800); Circuit judge (1801–1802); 6th Governor of New Hampshire (1809–1810); Chief Justice of NH Superior Court/Supreme Judicial Court (1802–1809, 1813–1816); Daniel Webster's professional contemporary; career spanning founding era through Jacksonian period.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New Hampshire's Federalist political environment in the 1790s — and the Federalist majority's control of congressional and federal appointment processes — created the career pathway that took Smith from congressman to US attorney to federal circuit judge",
            "The early American republic's need for legally trained Federalist judges who could build the common law tradition in the new state court systems — a process that required decades of consistent judicial work — created the sustained demand for Smith's judicial service in New Hampshire",
            "Harvard's role as the training ground for New England's legal and political elite in the founding era — and the network of Harvard-educated Federalists who dominated New England's professional world in the 1790s–1810s — provided the institutional connections that supported Smith's multi-role career"
        ],
        "effects": [
            "His six-plus years as Chief Justice of the New Hampshire Supreme Court contributed to the development of New Hampshire common law through hundreds of decisions — building the legal precedents that shaped New Hampshire jurisprudence for decades",
            "His brief governorship (1809–1810) provided New Hampshire with a Federalist executive during the final years of Federalist viability in New England — contributing to the state's governance during the transition from the early republic to the Jeffersonian era",
            "His professional relationship with Daniel Webster — whose early New Hampshire legal career overlapped with Smith's judicial tenure — contributed to Webster's formation as a lawyer and his early exposure to the constitutional arguments that would make Webster the greatest advocate of his era",
            "His 51-year career of public service (1791–1842) — from the First Congress to the eve of the Polk presidency — made him one of the longest-serving public figures of the founding and antebellum eras, a living connection between the Revolutionary generation and the Jacksonian world"
        ],
        "relationships": [
            {"entity": "6th Governor of New Hampshire (1809–1810)", "relationship": "6TH_GOVERNOR", "note": "Served as 6th Governor of New Hampshire (1809–1810) — a Federalist executive in the final years of Federalist viability in New England"},
            {"entity": "Chief Justice of New Hampshire Superior Court / Supreme Judicial Court (1802–1809, 1813–1816)", "relationship": "CHIEF_JUSTICE", "note": "Served as Chief Justice of New Hampshire's highest court for two extended periods — contributing to the development of New Hampshire common law through hundreds of decisions"},
            {"entity": "Daniel Webster (professional contemporary and associate)", "relationship": "JUDICIAL_CONTEMPORARY_AND_PROFESSIONAL_ASSOCIATE_OF", "note": "A professional contemporary and close associate of Daniel Webster — whose early New Hampshire legal career overlapped with Smith's judicial tenure and was influenced by his judicial example"},
            {"entity": "US House of Representatives from New Hampshire (Federalist, 1791–1797)", "relationship": "CONGRESSMAN", "note": "Served as Federalist US Representative from New Hampshire (1791–1797) — supporting Hamilton's financial program and the Washington and Adams foreign policies"},
            {"entity": "US Circuit Court for the First Circuit (judge, 1801–1802)", "relationship": "CIRCUIT_JUDGE", "note": "Served as a federal circuit court judge (1801–1802) — part of the Adams administration's last-minute Federalist judicial appointments before Jefferson took office"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 42)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
