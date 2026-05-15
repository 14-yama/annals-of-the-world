#!/usr/bin/env python3
"""
Batch 91 — 8 entities: George Handley, James Lanman, Samuel Bell,
Charles Kilbourne Williams, John J. Milligan, Peter des Roches,
Return J. Meigs Jr., Samuel Maclay
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

    ("george-handley", {
        "summary": (
            "George Handley (1752–1793) was an American Revolutionary War officer and "
            "politician from Georgia who served as Governor of Georgia (1788–1789). "
            "A British-born immigrant who joined the American cause, Handley served "
            "in the Continental Army and distinguished himself in the southern "
            "campaigns — the brutal guerrilla warfare of the Georgia and South "
            "Carolina backcountry that was among the Revolution's most vicious "
            "fighting. After the war he entered Georgia politics, serving in the "
            "state legislature before his brief governorship.\n\n"
            "His governorship came at a transitional moment — between the Articles of "
            "Confederation and the new federal Constitution ratified in 1788. Georgia "
            "was among the first states to ratify the Constitution, and Handley's "
            "brief term bridged the old and new federal orders.\n\n"
            "He died young at forty-one — his early death preventing what might "
            "have been a longer political career.\n\n"
            "He was a British immigrant who became a Georgia Revolutionary hero."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Georgia Governor (1788–1789) at the Constitutional ratification moment; Continental Army officer in the brutal southern backcountry campaigns; British immigrant who joined the American cause; brief governorship bridging Articles of Confederation and new Constitution; died at forty-one.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Georgia's Revolutionary War experience — the brutal backcountry guerrilla warfare between Patriots and Loyalists that devastated the state — created both the military service and the political opportunity for officers like Handley",
            "The Constitutional ratification moment — Georgia's first-state ratification of the Constitution creating the transition from the Articles of Confederation — created the political context of Handley's brief governorship",
            "The British immigrant Patriot tradition — the substantial number of British-born colonists who joined the American cause — created the personal story of commitment and sacrifice that Handley exemplified"
        ],
        "effects": [
            "His governorship contributed to Georgia's governance during the critical constitutional transition of 1788–1789",
            "His military service contributed to Georgia's Revolutionary legacy — the southern campaign veterans who shaped the state's post-war political culture",
            "His British immigrant Patriot story contributed to the American founding narrative — the inclusive vision of the Revolution that welcomed committed immigrants",
            "His early death contributed to the pattern of Revolutionary-era mortality — the toll of war, disease, and hardship that shaped the founding generation"
        ],
        "relationships": [
            {"target": "georgia", "verb": "GOVERNS", "note": "Governor of Georgia 1788–1789"},
            {"target": "continental-army", "verb": "SERVES_IN", "note": "Continental Army officer in southern campaigns"},
            {"target": "american-revolutionary-war", "verb": "FIGHTS_IN", "note": "Revolutionary War veteran in brutal southern backcountry"},
            {"target": "us-constitution", "verb": "GOVERNS_DURING_RATIFICATION_OF", "note": "Governor when Georgia ratified the Constitution"},
            {"target": "georgia-legislature", "verb": "SERVES_IN", "note": "State legislator before governorship"}
        ]
    }),

    ("james-lanman", {
        "summary": (
            "James Lanman (1767–1841) was an American Democratic-Republican politician "
            "from Connecticut who served as U.S. Senator (1819–1825). Connecticut in "
            "this era was one of the last Federalist holdouts — the state's Congregationalist "
            "establishment, Yale-educated elite, and commercial ties to Britain had made "
            "it a Federalist bastion throughout the Jefferson and Madison years. By "
            "Lanman's Senate term, however, Connecticut was transitioning — the "
            "Federalist Party collapsing nationally and the state shifting toward "
            "the Era of Good Feelings fusion politics.\n\n"
            "His Senate years covered the Missouri Compromise (1820) — the defining "
            "sectional crisis that revealed the depth of the slavery divide. As a "
            "New England senator Lanman represented the region most opposed to "
            "slavery's expansion into new territories.\n\n"
            "He was a Norwich Connecticut lawyer who represented the state's "
            "transition from Federalist to Democratic-Republican politics.\n\n"
            "He contributed to Connecticut's representation during the Era of Good Feelings."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Connecticut Democratic-Republican Senator (1819–1825); served during Missouri Compromise and the transition from Federalist to Republican Connecticut; Norwich lawyer representing Connecticut's political transition; Era of Good Feelings senator from a former Federalist stronghold.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Connecticut's political transition — the state's shift from its Federalist bastion status as the national Federalist Party collapsed — created the political opening for Democratic-Republican candidates like Lanman",
            "The Missouri Compromise crisis of 1820 — the national sectional debate that Connecticut's New England perspective opposed — created the defining issue of Lanman's Senate years",
            "Connecticut's legal and commercial community — the Norwich and Hartford lawyers who formed the state's political elite — provided the professional base for Lanman's Senate career"
        ],
        "effects": [
            "His Senate service contributed Connecticut's New England perspective to the Missouri Compromise debates",
            "His career contributed to Connecticut's political transition documentation — the shift from Federalist dominance to competitive Democratic-Republican politics",
            "His Era of Good Feelings Senate service contributed to the fusion politics of the period — the weakened party competition that preceded Jacksonian polarization",
            "His Norwich Connecticut base contributed to the political documentation of eastern Connecticut's legal community"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Connecticut Senator 1819–1825"},
            {"target": "missouri-compromise", "verb": "VOTES_ON", "note": "New England senator during the 1820 sectional crisis"},
            {"target": "connecticut", "verb": "REPRESENTS", "note": "Norwich Connecticut lawyer-politician"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "Era of Good Feelings Democratic-Republican"},
            {"target": "federalist-party", "verb": "SUCCEEDS_IN_STATE", "note": "Democratic-Republican in a former Federalist stronghold"}
        ]
    }),

    ("samuel-bell", {
        "summary": (
            "Samuel Bell (1770–1850) was an American Democratic-Republican and "
            "National Republican politician from New Hampshire who served as Governor "
            "of New Hampshire (1819–1823) and U.S. Senator (1823–1835). His combined "
            "executive and legislative career spanned the Era of Good Feelings "
            "through the early Jacksonian period — the transformation from the "
            "one-party fusion politics of Monroe's era to the sharp partisan "
            "divisions of Jackson's. New Hampshire in this period was transitioning "
            "from Federalist competition to Democratic dominance, making Bell's "
            "National Republican/anti-Jackson alignment increasingly difficult.\n\n"
            "His Senate years covered the nullification crisis, the Bank War, and "
            "the emergence of the Whig Party from the anti-Jackson coalition — the "
            "central political conflicts of the 1820s and early 1830s.\n\n"
            "He was a Chester New Hampshire lawyer who served in multiple capacities "
            "over more than a decade of public service.\n\n"
            "He was among New Hampshire's most experienced antebellum politicians."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "New Hampshire Governor (1819–1823) and Senator (1823–1835); served from Era of Good Feelings through early Jacksonian period; anti-Jackson National Republican; Senate years covered nullification crisis and Bank War; Chester New Hampshire lawyer with over a decade of major office.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New Hampshire's transitional politics — the state's shift from Federalist competition to Democratic-Republican and eventually Democratic dominance — created the environment for Bell's extended political career",
            "The Era of Good Feelings fusion politics — the weakened party competition of Monroe's presidency — created the political opening for Bell's gubernatorial election",
            "The Jacksonian party transformation — the emergence of Jackson's Democratic coalition and the anti-Jackson National Republican and Whig opposition — created the partisan alignment that Bell joined against Jackson"
        ],
        "effects": [
            "His governorship contributed to New Hampshire's governance during the Era of Good Feelings",
            "His long Senate career contributed New Hampshire's anti-Jackson perspective to the nullification and Bank War debates",
            "His National Republican alignment contributed to the anti-Jackson coalition that eventually became the Whig Party",
            "His extended public service contributed to New Hampshire's political institutions — over a decade of gubernatorial and senatorial experience"
        ],
        "relationships": [
            {"target": "new-hampshire", "verb": "GOVERNS", "note": "Governor of New Hampshire 1819–1823"},
            {"target": "us-senate", "verb": "SERVES_IN", "note": "New Hampshire Senator 1823–1835"},
            {"target": "andrew-jackson", "verb": "OPPOSES", "note": "Anti-Jacksonian National Republican"},
            {"target": "nullification-crisis", "verb": "SERVES_DURING", "note": "Senator during the nullification crisis"},
            {"target": "national-republican-party", "verb": "MEMBER_OF", "note": "Anti-Jackson National Republican coalition"}
        ]
    }),

    ("charles-kilbourne-williams", {
        "summary": (
            "Charles Kilbourne Williams (1782–1853) was an American politician and "
            "jurist from Vermont who served as Governor of Vermont (1850–1852) and "
            "as a Vermont Supreme Court justice. His governorship came during the "
            "most explosive decade in American sectional history — the years of the "
            "Compromise of 1850, the Fugitive Slave Act, and the growing antislavery "
            "movement in Vermont, one of the most abolitionist states in the Union. "
            "Vermont's Whig culture — its Congregationalist moral reform tradition, "
            "its 1777 constitutional abolition of slavery, and its deep hostility "
            "to the Fugitive Slave Act — created the political environment of "
            "Williams's governorship.\n\n"
            "The Compromise of 1850 and Fugitive Slave Act were deeply unpopular "
            "in Vermont — the state whose hostility to the law became a national "
            "symbol of northern resistance.\n\n"
            "He was a Woodstock Vermont lawyer and jurist.\n\n"
            "He governed Vermont during the height of its antislavery ferment."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Vermont Governor (1850–1852) and Supreme Court justice; governorship during the Compromise of 1850 and Fugitive Slave Act; Vermont's intense antislavery culture and resistance to the Fugitive Slave Act; Woodstock lawyer governing the most abolitionist state during the sectional crisis.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Vermont's antislavery culture — the state's deep abolitionist tradition rooted in its 1777 constitutional abolition of slavery and Congregationalist moral reform — created the political environment that shaped Williams's governorship",
            "The Compromise of 1850's Fugitive Slave Act — the legislation requiring northern states to return escaped enslaved people to slaveholders — created the crisis that galvanized Vermont's resistance and defined Williams's gubernatorial period",
            "Vermont's Whig political tradition — the state's Whig/National Republican alignment that overlapped with antislavery moral reform — provided the partisan context of Williams's career"
        ],
        "effects": [
            "His governorship contributed to Vermont's institutional resistance to the Fugitive Slave Act — the state government's expression of the popular hostility to the law",
            "His administration contributed to Vermont's antislavery political culture — the gubernatorial leadership during the state's most intense abolitionist period",
            "His Supreme Court service contributed to Vermont's legal traditions — the judicial interpretation of the state's constitutional and statutory framework",
            "His career contributed to the documentation of New England's reaction to the Compromise of 1850 — the northern resistance that foreshadowed Republican Party formation"
        ],
        "relationships": [
            {"target": "vermont", "verb": "GOVERNS", "note": "Governor of Vermont 1850–1852"},
            {"target": "vermont-supreme-court", "verb": "SERVES_ON", "note": "Vermont Supreme Court justice"},
            {"target": "compromise-of-1850", "verb": "GOVERNS_DURING", "note": "Governor during the national sectional crisis"},
            {"target": "fugitive-slave-act-1850", "verb": "OPPOSES", "note": "Governor during Vermont's resistance to the Fugitive Slave Act"},
            {"target": "whig-party-united-states", "verb": "MEMBER_OF", "note": "Vermont Whig politician"}
        ]
    }),

    ("john-j-milligan", {
        "summary": (
            "John Jones Milligan (1795–1875) was an American Whig politician and "
            "lawyer from Delaware who served as U.S. Representative (1831–1839) "
            "during the Bank War and the heart of the Jacksonian era. Delaware's "
            "small size made each congressman especially significant — the state's "
            "tiny population meant its House delegation was among the smallest, "
            "and Milligan served for four consecutive terms making him one of "
            "Delaware's longest-serving antebellum House members. Delaware in "
            "this era remained commercially tied to Philadelphia's banking community "
            "and was deeply hostile to Jacksonian anti-bank ideology.\n\n"
            "His eight years in Congress covered the Bank War's climax — the "
            "recharter veto, the removal of deposits, and the eventual dissolution "
            "of the Bank of the United States. As a Whig, Milligan was a consistent "
            "defender of the Bank and opponent of Jackson.\n\n"
            "He was a Wilmington Delaware lawyer serving the commercial banking interests.\n\n"
            "He was one of Delaware's most consistent antebellum Whig voices."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Delaware Whig Congressman (1831–1839); four consecutive terms; defended the Bank of the United States against Jackson's veto; Delaware's commercial ties to Philadelphia banking; Wilmington lawyer representing the anti-Jacksonian commercial interest; one of Delaware's longest-serving antebellum House members.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Delaware's commercial banking culture — the state's deep ties to Philadelphia banking and the Bank of the United States that made Jacksonian anti-bank ideology especially threatening — created the political interest Milligan defended",
            "The Bank War's political polarization — Jackson's veto of the recharter and the removal of federal deposits that transformed American banking — created the defining issue of Milligan's congressional years",
            "Delaware's small-state Whig alignment — the tiny state's resistance to Jacksonian agrarian democracy in favor of commercial and banking interests — provided Milligan's consistent electoral base"
        ],
        "effects": [
            "His eight-year House tenure contributed Delaware's Whig opposition to the Bank War — the consistent vote against Jackson's banking policy",
            "His career contributed to the documentation of small-state commercial interests in antebellum congressional politics",
            "His four consecutive terms contributed to Delaware's legislative continuity — the stable representation that allowed sustained opposition to Jacksonian banking policies",
            "His Wilmington base contributed to the documentation of Delaware's commercial legal community in antebellum politics"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Delaware Congressman 1831–1839 — four terms"},
            {"target": "bank-of-the-united-states", "verb": "DEFENDS", "note": "Whig defender against Jackson's recharter veto"},
            {"target": "andrew-jackson", "verb": "OPPOSES", "note": "Anti-Jacksonian Whig opponent of banking policy"},
            {"target": "delaware", "verb": "REPRESENTS", "note": "Wilmington Delaware commercial lawyer"},
            {"target": "whig-party-united-states", "verb": "MEMBER_OF", "note": "Delaware Whig congressman"}
        ]
    }),

    ("peter-des-roches", {
        "summary": (
            "Peter des Roches (d.1238) was a medieval English bishop and statesman "
            "who served as Bishop of Winchester (1205–1238) and as Justiciar of England "
            "— effectively the chief minister and regent during the minority of Henry III. "
            "A Norman-born royal servant, des Roches was among the most powerful "
            "administrators of the reign of King John, managing royal finances and "
            "justice during the turbulent years of Magna Carta's sealing (1215) "
            "and the subsequent First Barons' War. He joined the royal side against "
            "the rebel barons and the French invasion.\n\n"
            "During Henry III's minority he served as a key member of the regency "
            "council, and briefly regained influence in the late 1220s-early 1230s "
            "before being ousted by baronial opposition.\n\n"
            "Winchester was the richest see in medieval England, and as bishop des "
            "Roches combined enormous ecclesiastical wealth with political power — "
            "a quintessential example of the medieval churchman-administrator.\n\n"
            "'In England it rains every day, but the King's thunderbolts are worse than rain.'"
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Bishop of Winchester (1205–1238) and Justiciar of England; key administrator during John's reign and Henry III's minority; managed royal finances during Magna Carta crisis; joined royal side in First Barons' War; Winchester — richest English see — combined ecclesiastical wealth with royal administrative power.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Norman-English administrative tradition — the system of using episcopal appointments to staff royal government that gave bishops like des Roches both ecclesiastical and administrative authority — created the institutional role he occupied",
            "King John's government — the pressures of losing Normandy, the Welsh and Scottish frontier conflicts, and the fiscal demands of warfare — created the administrative demands that required a capable Justiciar",
            "The Magna Carta crisis — the baronial rebellion, the sealing of Magna Carta in 1215, and the subsequent civil war — created the political crisis during which des Roches served as a loyalist royal minister"
        ],
        "effects": [
            "His Winchester bishopric contributed to the medieval English church's greatest administrative see — the richest episcopal foundation that combined religious and secular power",
            "His Justiciar service contributed to Henry III's minority government — the regency administration that maintained royal authority during the king's childhood",
            "His royal loyalist role in the First Barons' War contributed to the Crown's survival — the ecclesiastical and administrative support that helped defeat the baronial-French alliance",
            "His career contributed to the historical model of the medieval bishop-administrator — the prince of the church who served as an arm of royal government"
        ],
        "relationships": [
            {"target": "bishop-of-winchester", "verb": "SERVES_AS", "note": "Bishop of Winchester 1205–1238"},
            {"target": "henry-iii-of-england", "verb": "SERVES_AS_REGENT_FOR", "note": "Justiciar and regency council member during Henry's minority"},
            {"target": "king-john", "verb": "SERVES_UNDER", "note": "Key administrator during John's reign"},
            {"target": "magna-carta", "verb": "SERVES_DURING", "note": "Royal loyalist during Magna Carta crisis 1215"},
            {"target": "first-barons-war", "verb": "FIGHTS_IN", "note": "Joined royal side against rebel barons"}
        ]
    }),

    ("return-j-meigs-jr", {
        "summary": (
            "Return Jonathan Meigs Jr. (1764–1825) was an American Democratic-Republican "
            "politician from Ohio who served as Governor of Ohio (1810–1814), U.S. Senator "
            "(1808–1810), and Postmaster General of the United States (1814–1823). "
            "His unusual first name — inherited from his father — made him one of the "
            "most distinctively named politicians of the early republic. His governorship "
            "coincided with the War of 1812's western theater — the British-allied "
            "Indian confederacy's raids, the fall of Detroit, and the subsequent "
            "American campaigns that eventually secured the Ohio frontier. "
            "As Postmaster General he presided over the rapid expansion of the "
            "postal system as the United States grew.\n\n"
            "Ohio in this era was transforming from frontier state to major population "
            "center — growing faster than almost any state in the Union.\n\n"
            "Meigs County, Ohio, is named in his honor.\n\n"
            "He was a Marietta Ohio lawyer who rose to multiple major national offices."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Ohio Democratic-Republican Governor (1810–1814), Senator (1808–1810), and Postmaster General (1814–1823); governorship during War of 1812's western theater and fall of Detroit; Postmaster General during rapid postal expansion; Meigs County Ohio named in his honor; Marietta lawyer with three major national offices.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Ohio's frontier-to-state transformation — the rapid population growth that made Ohio a major state within a generation of statehood — created the political opportunities that Meigs's career exploited",
            "The War of 1812's western theater — the British-allied Indian confederacy, the fall of Detroit, and the frontier military emergency — created the crisis that defined Meigs's governorship",
            "Ohio's Democratic-Republican political culture — the frontier agrarianism and anti-Federalist sentiment that made Ohio reliably Republican — provided the political base for Meigs's three major offices"
        ],
        "effects": [
            "His governorship contributed to Ohio's defense during the War of 1812 — the executive management of the frontier military emergency",
            "His Postmaster General tenure contributed to the expansion of the American postal system — one of the federal government's most important nation-building institutions",
            "His three-office career contributed to Ohio's early political history — establishing the state's pattern of sending politicians to multiple major offices",
            "Meigs County's naming contributed to the documentation of Ohio's founding political figures — the landscape of county names memorializing the state's early leaders"
        ],
        "relationships": [
            {"target": "ohio", "verb": "GOVERNS", "note": "Governor of Ohio 1810–1814"},
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Ohio Senator 1808–1810"},
            {"target": "us-postmaster-general", "verb": "SERVES_AS", "note": "Postmaster General 1814–1823"},
            {"target": "war-of-1812", "verb": "GOVERNS_DURING", "note": "Governor during the western theater crisis"},
            {"target": "meigs-county-ohio", "verb": "NAMESAKE_OF", "note": "County named in his honor"}
        ]
    }),

    ("samuel-maclay", {
        "summary": (
            "Samuel Maclay (1741–1811) was an American Democratic-Republican politician "
            "from Pennsylvania who served as U.S. Senator (1795–1801) and as a member "
            "of the Pennsylvania state legislature. His brother William Maclay was one "
            "of Pennsylvania's original senators and is famous for his diary of the "
            "First Congress — making the Maclay brothers one of the most significant "
            "political families of the founding era. Samuel served during the Adams "
            "administration — the period of the Alien and Sedition Acts, the XYZ "
            "Affair, and the undeclared naval war with France that made the late "
            "1790s America's most politically turbulent decade since independence.\n\n"
            "Pennsylvania's Republican opposition to Adams's Federalist administration "
            "was fierce — and Samuel Maclay, like his brother, was a committed Republican.\n\n"
            "He was a Pennsylvanian Valley politician from the Susquehanna region "
            "whose family represented the frontier Republican tradition.\n\n"
            "He was part of the founding generation's most politically engaged families."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Pennsylvania Democratic-Republican Senator (1795–1801) during the Adams administration; served during Alien and Sedition Acts and XYZ Affair; brother of First Congress Senator William Maclay (famous diary); Susquehanna Valley frontier Republican tradition; part of the founding generation's most politically engaged families.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Pennsylvania's Republican political culture — the state's strong Jeffersonian Republican tradition rooted in its frontier communities, German immigrants, and opposition to Philadelphia Federalism — created the political base for the Maclay family",
            "The Adams administration's Federalist provocations — the Alien and Sedition Acts, the naval quasi-war with France, and the XYZ Affair — created the political crisis that galvanized Republican opposition during Maclay's Senate years",
            "The Maclay family's political tradition — his brother William's First Congress Senate service and famous diary — created the family's established place in Pennsylvania's founding political culture"
        ],
        "effects": [
            "His Senate service contributed Pennsylvania's Republican opposition to the Adams administration — the critical swing state's resistance to Federalist domestic and foreign policy",
            "His career contributed to the Maclay family's political legacy — the two brothers who together represented Pennsylvania in the Senate across the founding era",
            "His service during the Alien and Sedition Acts contributed to the Republican opposition that helped sweep Jefferson to power in 1800",
            "His Susquehanna Valley base contributed to the documentation of Pennsylvania's frontier Republican communities"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Pennsylvania Senator 1795–1801"},
            {"target": "john-adams", "verb": "OPPOSES", "note": "Republican senator opposing the Adams administration"},
            {"target": "alien-and-sedition-acts", "verb": "OPPOSES", "note": "Republican senator opposing Federalist repression"},
            {"target": "william-maclay", "verb": "SIBLING_OF", "note": "Brother of the First Congress senator and famous diarist"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "Pennsylvania Jeffersonian Republican"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 91 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich(slug, data)
    print("Done.")
