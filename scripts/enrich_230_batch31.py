#!/usr/bin/env python3
"""
Batch 31 — 8 entities: Hugh Lawson White, Theodore Sedgwick, Fisher Ames,
Jonathan Trumbull Sr., John Rowan, Moses Gill, John Baptiste Charles Lucas,
Jeremiah B. Howell
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

    # 1 — Hugh Lawson White
    ("hugh-lawson-white", {
        "summary": (
            "Hugh Lawson White (1773–1840) was a Tennessee jurist and Democratic "
            "statesman who served as a justice of the Tennessee Supreme Court, as "
            "a US Senator from Tennessee for nearly two decades (1825–1840), and "
            "as one of the Whig presidential candidates in the unusual multi-candidate "
            "election of 1836 — in which the Whig strategy was to run different "
            "regional candidates to prevent Van Buren from winning an electoral "
            "majority and throw the election to the House. White carried Tennessee "
            "and Georgia, winning 26 electoral votes against Van Buren's 170.\n\n"
            "White's political career was remarkable for its trajectory: he began "
            "as one of Andrew Jackson's closest Tennessee allies and friends — he "
            "was Jackson's preferred successor to the Senate — and then broke "
            "bitterly with Jackson over the question of Martin Van Buren's succession "
            "to the presidency. Jackson wanted Van Buren; White felt that he, "
            "as the longer-serving Tennessean, was more deserving. The break was "
            "personal and permanent — White ran against Van Buren as a Whig while "
            "Jackson campaigned against him — illustrating the personal nature "
            "of Jacksonian political loyalties.\n\n"
            "Before his Senate career, White had been one of Tennessee's most "
            "distinguished legal minds: he served on the Tennessee Supreme Court "
            "and was a founding trustee of the University of East Tennessee "
            "(now the University of Tennessee). His legal reputation and his "
            "long friendship with Jackson gave him a political standing that "
            "survived even their bitter break.\n\n"
            "He resigned from the Senate in 1840 — denounced by the Tennessee "
            "legislature as a traitor to the Jacksonian cause — and died later "
            "that year, ending a career of considerable political distinction."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Tennessee senator (1825–1840) and 1836 Whig presidential candidate (won 26 electoral votes against Van Buren); Tennessee Supreme Court justice; originally Andrew Jackson's closest Tennessee ally before a bitter political break over Van Buren's succession.",
            "significanceCategory": "regional"
        },
        "causes": [
            "His long friendship with Andrew Jackson — and his position as one of Tennessee's most respected legal and political figures — established the political standing from which he ran for president",
            "Jackson's insistence on Martin Van Buren as his chosen presidential successor — over the claims of White and other Tennesseans — created the bitter personal-political break that drove White to run as a Whig presidential candidate",
            "The Whig Party's unusual 1836 strategy of running multiple regional candidates — designed to deny Van Buren an electoral majority and throw the election to the House — created the mechanism for White's candidacy as the Southern Whig standard-bearer"
        ],
        "effects": [
            "His 26 electoral votes in the 1836 election — carried by winning Tennessee and Georgia — demonstrated the durability of Southern Jacksonian resentment against Van Buren and the effectiveness of regional Whig candidates in their home states",
            "His bitter break with Jackson became emblematic of the personal intensity of Jacksonian political loyalties — and of how quickly former allies could become enemies when personal ambition and presidential succession collided",
            "His resignation from the Senate under Tennessee legislative pressure in 1840 — denounced as a traitor to Jacksonianism — illustrated the iron discipline that Jackson maintained over Democratic party loyalty in his home state",
            "His presidency of the Tennessee Supreme Court and trusteeship of East Tennessee University contributed to Tennessee's developing legal and educational institutions"
        ],
        "relationships": [
            {"entity": "Andrew Jackson (US President)", "relationship": "FORMER_ALLY_AND_BITTER_OPPONENT_OF", "note": "Originally Jackson's closest Tennessee ally; broke bitterly with Jackson over Van Buren's succession — Jackson campaigned against him in 1836"},
            {"entity": "1836 US presidential election (Whig multi-candidate strategy)", "relationship": "WHIG_CANDIDATE_IN", "note": "One of multiple Whig presidential candidates in 1836 — won 26 electoral votes by carrying Tennessee and Georgia against Van Buren's 170"},
            {"entity": "Tennessee Supreme Court", "relationship": "JUSTICE_OF", "note": "Served as a justice of the Tennessee Supreme Court — establishing his reputation as one of Tennessee's leading legal minds"},
            {"entity": "US Senate from Tennessee (1825–1840)", "relationship": "NEARLY_20-YEAR_MEMBER_OF", "note": "Served as US Senator from Tennessee (1825–1840) — before his resignation under legislative censure for breaking with Jacksonian Democrats"},
            {"entity": "Martin Van Buren (US President)", "relationship": "PRESIDENTIAL_OPPONENT_OF_1836", "note": "Ran as Whig candidate against Van Buren in 1836 — the presidential election in which Jackson chose Van Buren over White as his Democratic heir"}
        ]
    }),

    # 2 — Theodore Sedgwick
    ("theodore-sedgwick", {
        "summary": (
            "Theodore Sedgwick (1746–1813) was a Massachusetts Federalist lawyer, "
            "judge, and statesman who held some of the most important positions in "
            "the early American constitutional government — serving as a delegate "
            "to the Continental Congress, as a US Representative (1789–1796, "
            "1799–1801), as Speaker of the US House of Representatives (1799–1801), "
            "as a US Senator (1796–1799), and as President pro tempore of the Senate. "
            "His career made him one of the most experienced legislators in the "
            "founding generation — a man who had served at the highest levels of "
            "both chambers of Congress.\n\n"
            "Sedgwick was one of the most committed Federalists in Congress — "
            "a partisan of Alexander Hamilton's nationalist economic program and "
            "a fierce opponent of Democratic-Republicanism. As Speaker during "
            "the 6th Congress (1799–1801), he presided over Congress during the "
            "critical election of 1800 — the 'Revolution of 1800' — in which "
            "Jefferson's Democratic-Republicans swept the Federalists from power. "
            "His speakership coincided with the deepest partisan crisis of the "
            "early republic.\n\n"
            "Before his congressional career, Sedgwick had been involved in one "
            "of the most significant early American legal cases: in Brom and Bett "
            "v. Ashley (1781) — the Massachusetts case in which an enslaved woman "
            "known as Mum Bett (Elizabeth Freeman) successfully sued for her "
            "freedom under the Massachusetts Constitution of 1780 — Sedgwick was "
            "her attorney. The case was a landmark in the gradual abolition of "
            "slavery in Massachusetts.\n\n"
            "He later served as a justice of the Massachusetts Supreme Judicial "
            "Court (1802–1813), completing a career of extraordinary range."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Massachusetts Federalist Speaker of the US House (1799–1801); US Senator and President pro tempore; Continental Congress delegate; attorney for Mum Bett (Elizabeth Freeman) in Brom and Bett v. Ashley (1781) — the case that helped end slavery in Massachusetts; Massachusetts Supreme Judicial Court justice.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Massachusetts's dominant Federalist political culture — shaped by the commercial and professional elite of Boston and the Connecticut River Valley — created the political base for Sedgwick's long legislative career",
            "His successful legal practice and his involvement in significant early cases — including Mum Bett's freedom suit — established his reputation as one of Massachusetts's leading lawyers before his political career",
            "The partisan intensity of the Federalist-Republican conflict of the 1790s — culminating in the Revolution of 1800 — created the political environment in which Sedgwick's commitment to Federalism defined his legislative career"
        ],
        "effects": [
            "His representation of Mum Bett (Elizabeth Freeman) in her freedom suit — and the court's ruling that the Massachusetts Constitution's declaration that all men are born free prohibited slavery — contributed to the effective end of slavery in Massachusetts",
            "His speakership during the Revolution of 1800 — presiding over Congress during the most consequential election in early American history — placed him at the center of the constitutional crisis of Jefferson's election and the presidential tie with Burr",
            "His long career in both chambers of Congress contributed to the institutional development of the early Congress — as one of the most experienced legislators of the founding generation",
            "His Massachusetts Supreme Judicial Court service contributed to the state's post-revolutionary legal development — extending his career from legislative to judicial service in the tradition of founding-era Massachusetts lawyers"
        ],
        "relationships": [
            {"entity": "Elizabeth Freeman (Mum Bett)", "relationship": "ATTORNEY_FOR_IN_FREEDOM_SUIT", "note": "Represented Mum Bett (Elizabeth Freeman) in Brom and Bett v. Ashley (1781) — the Massachusetts case that effectively ended slavery in the state"},
            {"entity": "US House of Representatives (Speakership)", "relationship": "SPEAKER_OF_1799-1801", "note": "Served as Speaker of the US House (6th Congress, 1799–1801) — presiding during the Revolution of 1800 and Jefferson's controversial election"},
            {"entity": "Federalist Party (Massachusetts)", "relationship": "LEADING_FIGURE_OF", "note": "One of Massachusetts's most committed Federalists — supporting Hamilton's nationalist program and opposing Democratic-Republicanism"},
            {"entity": "Revolution of 1800 (Jefferson's election)", "relationship": "SPEAKER_DURING", "note": "Presided as Speaker over Congress during the Revolution of 1800 — the election that swept Federalists from power and brought Jefferson to the presidency"},
            {"entity": "Massachusetts Supreme Judicial Court", "relationship": "JUSTICE_OF_1802-1813", "note": "Served as a Massachusetts Supreme Judicial Court justice (1802–1813) — extending his career into the judiciary after the Federalists lost Congressional power"}
        ]
    }),

    # 3 — Fisher Ames
    ("fisher-ames", {
        "summary": (
            "Fisher Ames (1758–1808) was a Massachusetts Federalist lawyer and "
            "congressman whose brief but brilliant congressional career — and whose "
            "extraordinary rhetorical and literary gifts — made him one of the "
            "most admired political minds of the early American republic. A "
            "Harvard graduate who studied law and established himself in Boston's "
            "legal circles, Ames served in the US House of Representatives for "
            "four terms (1789–1797) as a close ally of Alexander Hamilton and "
            "one of the most effective Federalist voices in the first Congresses. "
            "His speech in favor of the Jay's Treaty appropriations (1796) — "
            "widely regarded as one of the greatest speeches in congressional "
            "history — saved the treaty from House opposition that threatened "
            "to deny the appropriations needed to implement it.\n\n"
            "Ames's congressional career coincided with the most consequential "
            "years of the early republic — the debates over Hamilton's financial "
            "program, the formation of the party system, the French Revolutionary "
            "wars' impact on American foreign policy, and the Jay's Treaty "
            "controversy. In all of these debates, Ames was one of the most "
            "eloquent and intellectually rigorous Federalist voices — opposing "
            "Democratic-Republican populism with a sophisticated conservative "
            "political philosophy rooted in English Whig constitutionalism.\n\n"
            "His post-congressional writing — including essays collected in 'Works "
            "of Fisher Ames' — provided some of the most brilliant defenses of "
            "Federalist political theory in the early republic: eloquent, learned, "
            "and deeply pessimistic about what he saw as the inevitable triumph "
            "of democratic passion over republican order. He predicted that "
            "American democracy would degenerate into mob rule with remarkable "
            "prescience for someone writing in the 1790s.\n\n"
            "His death at 50 cut short a career that might have produced even "
            "more significant political philosophy."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Massachusetts Federalist congressman (1789–1797) and intellectual; his Jay's Treaty appropriations speech (1796) is considered one of the greatest in congressional history; brilliant defender of Federalist constitutional theory; his political essays predicted the dangers of democratic excess with extraordinary intellectual power.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Massachusetts's Federalist commercial culture — and the influence of Hamilton's nationalist economic program — created the political environment in which Ames's Federalism found its intellectual home and political base",
            "The Jay's Treaty controversy (1795–1796) — and the House Democrats' attempt to deny the appropriations needed to implement it — created the constitutional crisis that produced Ames's greatest speech and his most celebrated congressional moment",
            "The formation of the American party system in the 1790s — the emergence of the Federalist-Republican divide — created the political conflict that shaped Ames's congressional career and later political writing"
        ],
        "effects": [
            "His Jay's Treaty speech (1796) — saving the treaty from House opposition — contributed to the successful implementation of the treaty with Britain and to the constitutional precedent that appropriations debates could not be used to overturn a treaty",
            "His political essays and writings provided the most sophisticated intellectual defense of Federalist political theory in the early republic — shaping conservative American political thought for generations",
            "His intellectual legacy influenced the Whig tradition that succeeded Federalism — his themes of order, constitutional restraint, and the dangers of democratic passion were recycled by subsequent conservative political thinkers",
            "His promotion of the Constitution at Massachusetts's ratification convention (1788) helped build the case for ratification in a state with significant Anti-Federalist sentiment — contributing to Massachusetts's ultimately close vote for adoption"
        ],
        "relationships": [
            {"entity": "Jay's Treaty (1794) / Jay's Treaty appropriations debate (1796)", "relationship": "SAVED_WITH_FAMOUS_SPEECH", "note": "His speech in favor of the Jay's Treaty appropriations (1796) — widely regarded as the greatest congressional speech of the era — saved the treaty from House opposition"},
            {"entity": "Alexander Hamilton / Federalist Party", "relationship": "CLOSE_ALLY_AND_INTELLECTUAL_CHAMPION_OF", "note": "One of Hamilton's closest congressional allies — the most intellectually rigorous Federalist voice in the early House"},
            {"entity": "Federalist constitutional theory (political essays)", "relationship": "MOST_BRILLIANT_LITERARY_DEFENDER_OF", "note": "His post-congressional essays provided the most sophisticated and pessimistic defense of Federalist political theory — predicting the dangers of democratic excess"},
            {"entity": "US House of Representatives (1789–1797)", "relationship": "FEDERALIST_MEMBER_OF_FOUR_TERMS", "note": "Served four terms in the House (1789–1797) — contributing to the major debates of the early republic from the Federalist perspective"},
            {"entity": "Massachusetts Constitutional ratification convention (1788)", "relationship": "PROMOTED_CONSTITUTION_AT", "note": "Promoted the Constitution's adoption at Massachusetts's ratification convention — building the case for ratification in a state with significant Anti-Federalist sentiment"}
        ]
    }),

    # 4 — Jonathan Trumbull Sr.
    ("jonathan-trumbull", {
        "summary": (
            "Jonathan Trumbull Sr. (1710–1785) was an American statesman from "
            "Connecticut who holds the unique historical distinction of being the "
            "only person to serve as governor of both a British colony and an American "
            "state — and the only colonial governor to actively support American "
            "independence from his position as governor. As Colonial Governor of "
            "Connecticut (1769–1776) and then Governor of the new State of "
            "Connecticut (1776–1784), he provided extraordinary political continuity "
            "during the Revolution — and his sustained support for Washington "
            "and the Continental Army made him one of Washington's most trusted "
            "political allies.\n\n"
            "Connecticut under Trumbull was one of the most steadfastly Patriot "
            "colonies: its population was deeply Puritan in orientation, its "
            "militia tradition was strong, and Trumbull's personal commitment "
            "to independence was unequivocal. He organized Connecticut's "
            "extraordinary contributions to the Continental Army — Connecticut "
            "provided more troops and supplies proportionally than almost any "
            "other colony — and his war board at Lebanon, Connecticut became "
            "a crucial supply and logistics center for Washington's campaigns.\n\n"
            "Washington's affectionate nickname for Trumbull was 'Brother Jonathan' "
            "— and the phrase 'Brother Jonathan' became a generic term for "
            "the typical American in the early republic (comparable to 'Uncle Sam' "
            "in later periods). Trumbull's sons were also distinguished figures: "
            "Jonathan Trumbull Jr. became Governor of Connecticut and Speaker "
            "of the US House, while John Trumbull became one of America's "
            "most celebrated historical painters.\n\n"
            "His singular position as the only colonial governor who actively "
            "supported independence makes him one of the most important "
            "political figures of the Revolutionary period."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Only governor of both a British colony and a US state; only colonial governor to actively support American independence; Connecticut governor 1769–1784; Washington's 'Brother Jonathan' and most trusted political ally; father of Jonathan Trumbull Jr. (Governor + House Speaker) and painter John Trumbull.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Connecticut's distinctive Puritan political culture — with its long tradition of self-governance under the colonial charter — provided the political foundation for Trumbull's sustained Patriot leadership from his position as colonial governor",
            "Washington's need for reliable state governors who could organize and sustain the material support of the Continental Army — supplies, troops, and logistics — made Trumbull's Connecticut operation indispensable",
            "Connecticut's geographic position — inland, with a strong militia tradition and a Puritan population deeply hostile to British taxation — made it one of the most committed Patriot colonies and gave Trumbull's governorship unusual political durability"
        ],
        "effects": [
            "His 15-year combined governorship (colonial + state, 1769–1784) provided extraordinary political continuity through the most disruptive period in Connecticut's history — from colonial governance through independence and the Revolutionary War",
            "Connecticut's proportionally larger contribution of troops and supplies to the Continental Army — organized through Trumbull's war board at Lebanon — was a critical material contribution to the war effort",
            "Washington's 'Brother Jonathan' — his affectionate nickname for Trumbull — became a generic term for the typical American in the early republic, connecting Trumbull's personal identity to America's emerging national self-image",
            "His sons' distinguished careers — Jonathan Jr. as governor and House Speaker, John Trumbull as historical painter — made the Trumbull family one of Connecticut's most distinguished political and cultural dynasties"
        ],
        "relationships": [
            {"entity": "George Washington (Continental Army commander)", "relationship": "MOST_TRUSTED_STATE_GOVERNOR_AND_POLITICAL_ALLY_OF", "note": "Washington's 'Brother Jonathan' — his most trusted state political ally, who organized Connecticut's extraordinary support for the Continental Army"},
            {"entity": "Continental Army (logistics and supply)", "relationship": "PRIMARY_STATE_ORGANIZER_OF_CONNECTICUT_CONTRIBUTION_TO", "note": "Organized Connecticut's disproportionately large contributions of troops and supplies — and ran the Lebanon, CT war board that was a crucial logistics center"},
            {"entity": "Connecticut (colonial and state governorship)", "relationship": "GOVERNOR_1769-1784", "note": "The only governor of both a British colony and an American state — providing 15 years of continuous political leadership through the Revolution"},
            {"entity": "Jonathan Trumbull Jr. (Governor + House Speaker)", "relationship": "FATHER_OF", "note": "Father of Jonathan Trumbull Jr. — who served as Governor of Connecticut and Speaker of the US House — continuing the family's political dynasty"},
            {"entity": "John Trumbull (historical painter)", "relationship": "FATHER_OF", "note": "Father of John Trumbull — who became one of America's most celebrated historical painters, famous for his portraits of the founding generation"}
        ]
    }),

    # 5 — John Rowan
    ("john-rowan", {
        "summary": (
            "John Rowan (1773–1843) was a Kentucky lawyer, jurist, and politician "
            "whose career touched nearly every level of Kentucky's and the "
            "nation's legal and political institutions — serving in the Kentucky "
            "General Assembly, as a US Representative (1807–1809), as Secretary "
            "of State of Kentucky (1804–1806), as a judge of the Kentucky Court "
            "of Appeals (the state's highest court), and as a US Senator from "
            "Kentucky (1825–1831). He was educated in law by George Muter — a "
            "former Kentucky Attorney General — and became one of the leading "
            "members of the Kentucky bar.\n\n"
            "His career took place against the backdrop of the 'New Court–Old "
            "Court' controversy — one of the most severe constitutional crises "
            "in Kentucky's history. In the 1820s, a debt-relief and banking "
            "controversy produced a split in Kentucky's judiciary: the existing "
            "Kentucky Court of Appeals (the 'Old Court') was challenged by "
            "a rival 'New Court' created by the legislature after the Old Court "
            "struck down debt relief legislation. For two years (1823–1826), "
            "Kentucky had two competing court systems — each claiming to be "
            "the legitimate supreme court of the state. Rowan was associated "
            "with the Old Court faction.\n\n"
            "Rowan's personal history is also connected to dueling culture: "
            "he was involved in a celebrated duel with Dr. James Chambers in "
            "1801 in which Chambers died — an incident that illustrated the "
            "still-powerful hold of the honor culture in frontier Kentucky.\n\n"
            "His home — Federal Hill in Bardstown, Kentucky — became one of "
            "the most celebrated antebellum Kentucky estates, and the building "
            "that inspired Stephen Foster's 'My Old Kentucky Home' song (1853) "
            "is traditionally identified with Federal Hill."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Kentucky lawyer, US Representative (1807–1809), Kentucky Court of Appeals judge, and US Senator (1825–1831); key figure in the 'New Court–Old Court' controversy of the 1820s; his home Federal Hill in Bardstown is traditionally associated with Stephen Foster's 'My Old Kentucky Home' (1853).",
            "significanceCategory": "regional"
        },
        "causes": [
            "Kentucky's frontier legal culture — and the state's need for lawyers educated in the common law tradition — created the professional environment in which Rowan's legal career developed under Muter's mentorship",
            "The New Court–Old Court controversy — the constitutional crisis over debt relief legislation in the 1820s — created the judicial political conflict that defined Rowan's Old Court alignment",
            "Kentucky's competitive political culture and honor-culture dueling tradition — which persisted well into the 19th century — shaped the personal incident (the 1801 duel) that defined part of Rowan's personal history"
        ],
        "effects": [
            "His involvement in the New Court–Old Court controversy — one of the most severe constitutional crises in any state's history — contributed to the resolution of the two-court crisis and to the development of judicial authority in Kentucky",
            "His US Senate service (1825–1831) contributed to Kentucky's representation in Washington during the critical period of the Jacksonian political realignment",
            "Federal Hill's association with Stephen Foster's 'My Old Kentucky Home' (1853) — whether or not Foster literally stayed there — gave the Rowan estate a lasting cultural significance as one of the most famous homes in Kentucky",
            "His involvement in the 1801 duel with Dr. Chambers — which resulted in Chambers's death — illustrated the personal cost of Kentucky's honor-culture and contributed to growing public unease about dueling"
        ],
        "relationships": [
            {"entity": "New Court–Old Court controversy (Kentucky, 1820s)", "relationship": "OLD_COURT_ADHERENT_DURING", "note": "Aligned with the Old Court faction during Kentucky's constitutional crisis — when two competing supreme courts claimed legitimacy in the state simultaneously"},
            {"entity": "Kentucky Court of Appeals", "relationship": "JUDGE_OF", "note": "Served as a judge of the Kentucky Court of Appeals — the state's highest court — before and during the New Court–Old Court controversy"},
            {"entity": "US Senate from Kentucky (1825–1831)", "relationship": "SENATOR", "note": "Served as US Senator from Kentucky (1825–1831) during the Jacksonian political realignment"},
            {"entity": "Federal Hill / 'My Old Kentucky Home'", "relationship": "OWNER_OF_ESTATE_ASSOCIATED_WITH", "note": "Owner of Federal Hill in Bardstown, Kentucky — traditionally identified as the inspiration for Stephen Foster's 'My Old Kentucky Home' (1853)"},
            {"entity": "Dueling culture (frontier Kentucky, 1801)", "relationship": "PARTICIPANT_IN_CELEBRATED_DUEL", "note": "Involved in a celebrated 1801 duel with Dr. James Chambers — in which Chambers died — illustrating Kentucky's honor-culture dueling tradition"}
        ]
    }),

    # 6 — Moses Gill
    ("moses-gill", {
        "summary": (
            "Moses Gill (1734–1800) was an American merchant and politician from "
            "Princeton, Massachusetts, who served as Lieutenant Governor of "
            "Massachusetts (1794–1800) and briefly as Acting Governor (1799–1800) "
            "— the only acting governor in Massachusetts history to die in office. "
            "A successful merchant who had become one of the most prosperous men "
            "in Worcester County, Gill's career illustrated the path of wealthy "
            "Massachusetts merchants into political prominence during the post-revolutionary "
            "era — a pattern in which commercial success provided the social capital "
            "and financial independence necessary for elected office.\n\n"
            "Gill had a strong Patriot record during the Revolutionary War: he was "
            "an active supporter of the American cause, and his personal connections "
            "to the Massachusetts Patriot leadership gave him standing in the "
            "post-war Federalist political establishment. He served in the Massachusetts "
            "General Court (legislature) and accumulated local office experience "
            "before his elevation to Lieutenant Governor.\n\n"
            "His brief Acting Governorship (1799–1800) — triggered by the death "
            "or incapacity of the sitting governor — ended when Gill himself died "
            "in office in 1800, making him the only Massachusetts acting governor "
            "to die while holding the office. This double succession — the acting "
            "governor dying before the regularly elected governor could take office "
            "— was an unusual constitutional moment in Massachusetts history.\n\n"
            "His Princeton estate (Temple Farm) was one of the finest in Worcester "
            "County and reflected the material success that underpinned his "
            "political career."
        ),
        "importanceScore": 5,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Massachusetts merchant and Lieutenant Governor (1794–1800) who served as Acting Governor (1799–1800) — the only acting governor in Massachusetts history to die in office; a prosperous Worcester County merchant whose Patriot record provided the foundation for his political career.",
            "significanceCategory": "regional"
        },
        "causes": [
            "His success as a merchant in Worcester County — making him one of the most prosperous men in the region — provided the social capital and financial independence that enabled his political career",
            "Massachusetts's post-revolutionary Federalist political culture — in which successful merchants and professionals were the natural leaders of the Commonwealth — created the political environment for Gill's elevation to state office",
            "The death or incapacity of the sitting governor created the vacancy that elevated Gill to Acting Governor — and his own subsequent death in office created the unusual double succession"
        ],
        "effects": [
            "His death as Acting Governor created an unusual constitutional moment in Massachusetts history — triggering the process by which the regularly elected governor's succession had to be managed",
            "His Patriot record during the Revolution and his subsequent political career contributed to the pattern of Massachusetts merchant-statesmen who combined commercial success with public service in the post-revolutionary era",
            "His estate at Temple Farm in Princeton illustrated the material prosperity that underpinned the Massachusetts Federalist political elite — and the connection between commercial success and political prominence",
            "The double succession his death triggered — an acting governor dying in office — was one of the more unusual constitutional moments in early Massachusetts state history"
        ],
        "relationships": [
            {"entity": "Massachusetts Lieutenant Governorship (1794–1800)", "relationship": "LIEUTENANT_GOVERNOR", "note": "Served as Lieutenant Governor of Massachusetts (1794–1800) — the position from which he was elevated to Acting Governor"},
            {"entity": "Massachusetts Acting Governorship (1799–1800)", "relationship": "ONLY_ACTING_GOVERNOR_TO_DIE_IN_OFFICE", "note": "Served as Acting Governor (1799–1800) — the only acting governor in Massachusetts history to die in office"},
            {"entity": "Worcester County, Massachusetts (merchant elite)", "relationship": "MOST_PROMINENT_MERCHANT_IN", "note": "One of the most prosperous merchants in Worcester County — his commercial success provided the foundation for his political career"},
            {"entity": "Massachusetts Patriot cause (Revolutionary War)", "relationship": "ACTIVE_SUPPORTER_OF", "note": "Active supporter of the American Patriot cause during the Revolutionary War — establishing the political credentials for his post-war career"},
            {"entity": "Temple Farm (Princeton, Massachusetts)", "relationship": "OWNER_OF", "note": "Owner of Temple Farm in Princeton — one of the finest estates in Worcester County, reflecting the material prosperity that underpinned his political career"}
        ]
    }),

    # 7 — John Baptiste Charles Lucas
    ("john-baptiste-charles-lucas", {
        "summary": (
            "John Baptiste Charles Lucas (1758–1842) was a French-born American "
            "politician and jurist whose remarkable life story began with a meeting "
            "with Benjamin Franklin in France — Franklin's letter of introduction "
            "brought Lucas to America — and culminated in a career as a US "
            "Representative from Pennsylvania and then as one of the founding "
            "judges of the Louisiana Territory's court system. His story "
            "illustrated the cosmopolitan character of the early American republic, "
            "which attracted educated Europeans who became full participants "
            "in the new nation's legal and political institutions.\n\n"
            "Born in Normandy, Lucas was inspired by the democratic ideals he "
            "encountered through Franklin — who was then serving as American "
            "minister to France — and immigrated to the United States, where "
            "he studied law and established himself in Pennsylvania politics "
            "as a Democratic-Republican. He served in the US House of Representatives "
            "from Pennsylvania (1803–1805) and was known for his opposition to "
            "the Federalist establishment and his alignment with Jefferson's "
            "agrarian democratic vision.\n\n"
            "After the Louisiana Purchase (1803), Lucas was appointed by Jefferson "
            "as a judge of the new Louisiana Territory and as a member of the "
            "Board of Land Commissioners — the body responsible for adjudicating "
            "land titles under the complex legacy of French and Spanish land "
            "grants in the acquired territory. His role in Louisiana's land "
            "claims adjudication was both crucial and deeply controversial: he "
            "was known for skepticism toward large claimants and for strict "
            "interpretation of the documentary evidence for land grants.\n\n"
            "He served as a Louisiana judge for more than two decades, becoming "
            "one of the most significant figures in early Louisiana legal history."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "French-born American politician; met Benjamin Franklin in France; US Representative from Pennsylvania (1803–1805); appointed by Jefferson as a founding judge of Louisiana Territory and member of the Board of Land Commissioners — adjudicating the complex legacy of French and Spanish land grants after the Louisiana Purchase.",
            "significanceCategory": "regional"
        },
        "causes": [
            "His encounter with Benjamin Franklin in France — and Franklin's letter of introduction — created the direct personal connection to American democracy that motivated his immigration and his subsequent American career",
            "The Louisiana Purchase (1803) — which acquired an enormous territory with a complex legacy of French and Spanish land grants — created the need for experienced judges and land commissioners who could adjudicate the tangled claims",
            "His Democratic-Republican alignment — and his opposition to the Federalist establishment — made him a natural Jefferson appointee for the Louisiana judicial and administrative positions"
        ],
        "effects": [
            "His service as a founding judge of Louisiana Territory — and as a Board of Land Commissioners member — contributed to the legal resolution of the complex French and Spanish land grant claims that were the most contested legal issue in the newly acquired territory",
            "His more than two decades of Louisiana judicial service made him one of the most significant figures in early Louisiana legal history — shaping the development of Louisiana's unique civil law system in the American context",
            "His story — French-born, inspired by Franklin, becoming an American congressman and Louisiana founding judge — illustrated the cosmopolitan character of the early American republic and its ability to integrate educated European immigrants",
            "His strict approach to land grant evidence created controversy but also established a legal standard that protected the territorial government's interests against fraudulent or inflated claims"
        ],
        "relationships": [
            {"entity": "Benjamin Franklin (American statesman/minister to France)", "relationship": "INSPIRED_BY_AND_INTRODUCED_TO_AMERICA_BY", "note": "Met Franklin in France — Franklin's letter of introduction brought Lucas to America and launched his American career"},
            {"entity": "Louisiana Purchase (1803)", "relationship": "FOUNDING_JUDICIAL_FIGURE_IN_AFTERMATH_OF", "note": "Appointed founding judge of Louisiana Territory after the Purchase — responsible for adjudicating the complex French and Spanish land grant legacy"},
            {"entity": "Board of Land Commissioners (Louisiana Territory)", "relationship": "MEMBER_OF", "note": "Served on the Board of Land Commissioners — adjudicating the complex, often contested claims to land under French and Spanish grants in the acquired territory"},
            {"entity": "Thomas Jefferson (US President)", "relationship": "APPOINTEE_OF_FOR_LOUISIANA_POSITIONS", "note": "Appointed by Jefferson as Louisiana Territory judge and land commissioner — his Democratic-Republican alignment made him a trusted Jeffersonian appointee"},
            {"entity": "US House of Representatives from Pennsylvania (1803–1805)", "relationship": "DEMOCRATIC-REPUBLICAN_MEMBER_OF", "note": "Served as US Representative from Pennsylvania (1803–1805) — known for his opposition to the Federalist establishment and his Jeffersonian democratic alignment"}
        ]
    }),

    # 8 — Jeremiah B. Howell
    ("jeremiah-b-howell", {
        "summary": (
            "Jeremiah Brown Howell (1771–1822) was a Rhode Island lawyer and "
            "Democratic-Republican politician who served as United States Senator "
            "from Rhode Island (1811–1817). A graduate of the College of Rhode "
            "Island (now Brown University) in 1789, he studied law, was admitted "
            "to the bar, and established himself in Providence legal and "
            "political circles before his appointment to fill a Senate vacancy "
            "in 1811. His senatorial tenure coincided with the War of 1812 — "
            "one of the most contentious political conflicts in early American "
            "history — during which New England's Federalist-dominated legislatures "
            "generally opposed the war while Democratic-Republicans supported it.\n\n"
            "Rhode Island's distinctive political culture — with its traditions of "
            "local autonomy, commercial independence, and Charter government dating "
            "to Roger Williams — created an unusual political environment for "
            "Democratic-Republican politicians like Howell. The state's commercial "
            "maritime economy was devastated by the war's trade disruptions, "
            "and even Democratic-Republicans faced pressure from commercial "
            "interests who opposed the conflict.\n\n"
            "Howell's Senate career was significant for Rhode Island because it "
            "maintained the state's Democratic-Republican representation in the "
            "Senate during the height of Federalist dominance in New England — "
            "providing a minority political voice in a region that was overwhelmingly "
            "aligned against the Madison administration's war policy.\n\n"
            "He served a single Senate term and did not seek re-election, returning "
            "to legal practice in Providence after 1817."
        ),
        "importanceScore": 5,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Rhode Island Democratic-Republican US Senator (1811–1817) during the War of 1812; Brown University graduate (1789); provided Democratic-Republican representation in the Senate from one of New England's most Federalist states during the war controversy.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Rhode Island's Senate vacancy in 1811 created the appointment opportunity that elevated Howell from Providence legal practice to the US Senate",
            "The War of 1812's political polarization — splitting New England Federalists from national Democratic-Republicans — created the context in which Howell's Senate service was a Democratic-Republican minority voice in a Federalist region",
            "His Brown University legal education and his established Providence legal career provided the credentials for his Senate appointment"
        ],
        "effects": [
            "His Senate service provided Democratic-Republican representation from Rhode Island during the critical War of 1812 period — maintaining a minority political presence in the Senate from New England's most commercially vulnerable state",
            "His single-term tenure contributed to Rhode Island's early statehood Senate representation during the critical period of the Jeffersonian-to-Jacksonian transition",
            "His return to legal practice after his Senate term reflected the typical pattern of early American politicians who moved between professional practice and legislative service without building permanent national political careers",
            "His tenure illustrated Rhode Island's unusual political position during the War of 1812 — a state whose commercial maritime economy made it deeply skeptical of the war even among Democratic-Republicans"
        ],
        "relationships": [
            {"entity": "US Senate from Rhode Island (1811–1817)", "relationship": "SENATOR", "note": "Served as US Senator from Rhode Island (1811–1817) — providing Democratic-Republican representation from one of New England's most commercially oriented and Federalist states"},
            {"entity": "War of 1812 (Senate debates)", "relationship": "DEMOCRATIC-REPUBLICAN_VOICE_DURING", "note": "His Senate tenure coincided with the War of 1812 — during which New England Federalists generally opposed the war while he maintained Democratic-Republican alignment"},
            {"entity": "College of Rhode Island (Brown University)", "relationship": "ALUMNUS_OF_1789", "note": "Graduate of the College of Rhode Island (now Brown University) in 1789 — establishing his educational credentials for the legal and political career that followed"},
            {"entity": "Rhode Island Democratic-Republican minority", "relationship": "SENATOR_REPRESENTING", "note": "Represented Rhode Island's Democratic-Republican minority in the Senate — a politically isolated position in the most Federalist region of the country during the War of 1812"},
            {"entity": "Providence, Rhode Island (legal profession)", "relationship": "LEGAL_CAREER_BASE", "note": "Established himself in Providence legal and political circles before and after his Senate service — returning to legal practice after 1817"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 31)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
