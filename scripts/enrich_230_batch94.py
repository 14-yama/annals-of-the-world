#!/usr/bin/env python3
"""
Batch 94 — 8 entities: Juan Mora Fernández, Thomas King Carroll,
Étienne Denis Pasquier, Alain-René Lesage, Hiland Hall,
Jared W. Williams, Daniel D. Tompkins, Henry Hubbard
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

    ("juan-mora-fernández", {
        "summary": (
            "Juan Mora Fernández (1784–1854) was a Costa Rican statesman who "
            "served as the first Head of State of Costa Rica (1824–1833) after "
            "independence from Spain. His nine-year leadership — the longest "
            "of any Costa Rican head of state in the 19th century — was "
            "foundational: he established the administrative, educational, and "
            "legal institutions of the new state. Costa Rica was then the "
            "smallest and most peripheral of Central America's new nations — "
            "sparsely populated, agricultural, with no significant indigenous "
            "population remaining and no wealthy colonial elite. Mora Fernández "
            "built the institutions of governance virtually from scratch.\n\n"
            "He established Costa Rica's first printing press and promoted "
            "public education — the foundations of the literate civic culture "
            "that would make Costa Rica exceptional in Central America.\n\n"
            "He was from a modest San José family — his leadership demonstrated "
            "that Costa Rica's founding generation was practical and democratic "
            "rather than aristocratic.\n\n"
            "He was the founding father of modern Costa Rica."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "First Head of State of Costa Rica (1824–1833); nine-year foundational leadership; established Costa Rica's administrative, educational, and legal institutions; introduced the first printing press; promoted public education that created Costa Rica's exceptional civic culture; founding father of modern Costa Rica.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Costa Rica's independence from Spain — the 1821 Central American independence that left Costa Rica as a peripheral, small, but functional new state — created the political vacuum that Mora Fernández's leadership filled",
            "Costa Rica's unique colonial heritage — the absence of a large indigenous population, gold, or encomienda system that had concentrated wealth elsewhere in Spanish America — created the relatively egalitarian social base for Mora Fernández's practical governance",
            "Central American Federation's instability — the Federal Republic of Central America's persistent political turbulence — created the pressure on Costa Rica to develop independent institutions under Mora Fernández's leadership"
        ],
        "effects": [
            "His nine-year leadership contributed to Costa Rica's foundational institutional development — the administrative, legal, and educational structures that shaped the nation",
            "His printing press introduction contributed to Costa Rica's civic culture — the foundation of the literacy and public education that made Costa Rica exceptional in Central American development",
            "His stable governance contributed to Costa Rica's reputation for peaceful institutional democracy — the founding precedent for the country's unusual political stability",
            "His leadership contributed to Central American political history — the example of effective small-state governance during a period of regional instability"
        ],
        "relationships": [
            {"target": "costa-rica", "verb": "LEADS", "note": "First Head of State of Costa Rica 1824–1833"},
            {"target": "central-american-independence", "verb": "BUILDS_UPON", "note": "Led Costa Rica in the independence era"},
            {"target": "costa-rica-education-system", "verb": "FOUNDS", "note": "Established public education system"},
            {"target": "federal-republic-of-central-america", "verb": "OPERATES_WITHIN", "note": "Costa Rican leader within the Central American Federation"},
            {"target": "san-josé-costa-rica", "verb": "LEADS_FROM", "note": "San José native and political base"}
        ]
    }),

    ("thomas-king-carroll", {
        "summary": (
            "Thomas King Carroll (1793–1873) was an American Democratic politician "
            "from Maryland who served as Governor of Maryland (1830–1831) — a "
            "single one-year term. Maryland in the early Jacksonian period was "
            "a competitive two-party state — its combination of Chesapeake Bay "
            "planter culture, Baltimore commercial interests, and western mountain "
            "communities created a mixed political economy that resisted easy "
            "partisan alignment. Carroll's brief governorship came at the "
            "beginning of the Jacksonian transformation — the emergence of the "
            "Democratic Party and the sharp partisan conflicts over banking, "
            "tariffs, and internal improvements.\n\n"
            "Maryland's proximity to Washington and its mixture of slave and "
            "free economy made it politically distinctive in the antebellum period.\n\n"
            "He was a wealthy Eastern Shore Maryland planter.\n\n"
            "He represented Maryland's Jacksonian Democratic planter class."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Maryland Democratic Governor (1830–1831); brief governorship at the beginning of the Jacksonian transformation; Eastern Shore Maryland planter; Maryland's competitive two-party state balancing Chesapeake planter culture, Baltimore commerce, and western communities; Jacksonian Democratic planter class.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Maryland's competitive political culture — the state's mixed economy of planter, commercial, and yeoman interests that created contested politics — created the environment for Carroll's Democratic governorship",
            "The Jacksonian Democratic coalition's emergence — the party organization that Jackson's supporters built around his 1828 victory — created the partisan context for Carroll's election",
            "Maryland's Eastern Shore planter class — the Chesapeake Bay planter community with its tobacco culture and slavery — provided the social base for Carroll's political career"
        ],
        "effects": [
            "His governorship contributed to Maryland's Jacksonian Democratic governance — the brief executive leadership during the party's formative period",
            "His Eastern Shore planter identity contributed to the documentation of Maryland's antebellum political culture",
            "His brief term contributed to Maryland's pattern of competitive gubernatorial politics — the close elections that reflected the state's divided political economy",
            "His career contributed to the historical record of Maryland's founding Democratic leadership in the Jacksonian transformation"
        ],
        "relationships": [
            {"target": "maryland", "verb": "GOVERNS", "note": "Governor of Maryland 1830–1831"},
            {"target": "andrew-jackson", "verb": "SUPPORTS", "note": "Jacksonian Democrat"},
            {"target": "democratic-party-united-states", "verb": "MEMBER_OF", "note": "Early Maryland Democratic Party member"},
            {"target": "eastern-shore-maryland", "verb": "REPRESENTS", "note": "Eastern Shore planter politician"},
            {"target": "chesapeake-bay-plantation-culture", "verb": "REPRESENTS", "note": "Maryland planter class governor"}
        ]
    }),

    ("étienne-denis-pasquier", {
        "summary": (
            "Étienne Denis Pasquier (1767–1862) was a French statesman and jurist "
            "who was one of the most remarkable political survivors of the Napoleonic "
            "and post-Napoleonic era. Serving successive regimes — Empire, Bourbon "
            "Restoration, and the July Monarchy — he held major offices under "
            "each, including Minister of Justice, Minister of Foreign Affairs, "
            "President of the Chamber of Peers, and Chancellor of France. "
            "His exceptional longevity (he died at 94) and his willingness to serve "
            "each successive regime without conspicuous ideological commitment made "
            "him both invaluable and somewhat cynically criticized as the "
            "quintessential political opportunist.\n\n"
            "His memoirs are a primary historical source for the Napoleonic and "
            "Restoration periods — the observations of a man who knew everyone "
            "and served everyone.\n\n"
            "Napoleon reportedly said: 'Pasquier can serve anyone — he serves France.'\n\n"
            "He was Chancellor of France and the longest-serving major statesman of his era."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "French Chancellor and supreme political survivor — served Napoleon's Empire, Bourbon Restoration, and July Monarchy; Minister of Justice, Foreign Affairs, President of Chamber of Peers, and Chancellor of France; lived to 94; his memoirs are primary sources for the era; quintessential example of the jurist-administrator who served successive regimes.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The French political instability of 1800–1850 — the successive regime changes from Empire to Restoration to July Monarchy — created the environment in which pragmatic statesman-administrators like Pasquier were repeatedly needed",
            "Pasquier's legal expertise — his training as a lawyer under the Old Regime and his magistracy experience — created the professional competence that made him indispensable across regimes",
            "The French bureaucratic continuity tradition — the preference for experienced administrators over ideologically committed officials — created the system that repeatedly recycled figures like Pasquier through major offices"
        ],
        "effects": [
            "His multiple ministerial roles contributed to French governance across the Empire, Restoration, and July Monarchy — the administrative continuity through political upheaval",
            "His memoirs contributed to historical scholarship on the Napoleonic and Restoration periods — primary source accounts from a participant-observer",
            "His Chancellor of France tenure contributed to the constitutional development of the French peerage system under the restored Bourbon and Orléanist monarchies",
            "His career contributed to the model of the French political administrator — the expert bureaucrat whose competence supersedes partisan loyalty"
        ],
        "relationships": [
            {"target": "napoleon-bonaparte", "verb": "SERVES_UNDER", "note": "Major official in the Napoleonic Empire"},
            {"target": "bourbon-restoration", "verb": "SERVES_IN", "note": "Minister of Justice and Foreign Affairs under the Restoration"},
            {"target": "july-monarchy", "verb": "SERVES_IN", "note": "Chancellor of France under Louis-Philippe"},
            {"target": "chamber-of-peers-france", "verb": "PRESIDES_OVER", "note": "President of the Chamber of Peers"},
            {"target": "france", "verb": "SERVES_AS_CHANCELLOR_OF", "note": "Chancellor of France — highest legal-ceremonial office"}
        ]
    }),

    ("alain-rené-lesage", {
        "summary": (
            "Alain-René Lesage (1668–1747) was a French novelist and dramatist "
            "whose novel 'Gil Blas de Santillane' (1715–1735) was one of the "
            "most widely read works of 18th-century European literature — "
            "a picaresque masterpiece that influenced Fielding, Smollett, "
            "Scott, and Dickens. Set in Spain but unmistakably French in its "
            "social satire, 'Gil Blas' follows a low-born hero through the "
            "levels of Spanish society, satirizing clergy, nobles, physicians, "
            "and courtiers with sharp wit. Lesage also wrote the enormously "
            "popular play 'Turcaret' (1709) — a devastating satire of "
            "financiers and nouveaux riches that became a classic of French comedy.\n\n"
            "His works represented a significant democratization of French "
            "literature — the picaresque form's emphasis on the adventures of "
            "low-born heroes rather than aristocratic subjects.\n\n"
            "He wrote without aristocratic patronage — a relatively independent author.\n\n"
            "'Gil Blas' was still being reprinted and translated two centuries after his death."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Author of 'Gil Blas de Santillane' (1715–1735) — one of the most widely read European novels of the 18th century; influenced Fielding, Smollett, Scott, and Dickens; author of 'Turcaret' (1709) — classic French comedy satirizing financiers; picaresque master who democratized French literary subjects; independent author without patronage.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The picaresque tradition — the Spanish literary form of the roguish low-born hero navigating society — created the genre model that Lesage adapted for French social satire",
            "French Enlightenment social criticism — the growing literary tradition of satirizing the church, nobility, and nouveau riche — created the cultural demand for the kind of wit that 'Gil Blas' and 'Turcaret' provided",
            "The expansion of the French reading public — the growing literate middle class that created a market for prose fiction — created the audience that made 'Gil Blas' a bestseller"
        ],
        "effects": [
            "His 'Gil Blas' contributed directly to the English novel's development — Fielding's 'Tom Jones', Smollett's 'Roderick Random', and the picaresque tradition in English literature",
            "His 'Turcaret' contributed to French theatrical tradition — the classic comedy of financial satire that influenced subsequent French playwrights",
            "His independent authorship contributed to the model of the professional literary author — the writer who supported himself by writing rather than depending on aristocratic patronage",
            "His social satire contributed to the Enlightenment's critique of privilege — the literary side of the philosophes' project of exposing the irrationality of hierarchical society"
        ],
        "relationships": [
            {"target": "gil-blas-de-santillane", "verb": "AUTHORS", "note": "Author of 1715–1735 picaresque masterpiece"},
            {"target": "turcaret", "verb": "AUTHORS", "note": "Author of 1709 comedy satirizing financiers"},
            {"target": "french-enlightenment-literature", "verb": "PARTICIPATES_IN", "note": "Major figure of early French Enlightenment fiction"},
            {"target": "picaresque-novel", "verb": "MASTERS", "note": "Pre-eminent French picaresque novelist"},
            {"target": "henry-fielding", "verb": "INFLUENCES", "note": "Direct influence on Fielding's Tom Jones and English novel"}
        ]
    }),

    ("hiland-hall", {
        "summary": (
            "Hiland Hall (1795–1885) was an American Whig and Republican politician "
            "and historian from Vermont who served in the U.S. House (1833–1843) "
            "and as Governor of Vermont (1858–1860). His decade in Congress "
            "covered the Bank War, the antislavery petition battles, and the "
            "nullification crisis — the defining confrontations of the Jacksonian "
            "era. His governorship came at the height of the sectional crisis: "
            "1858–1860 were the years of the Lincoln-Douglas debates, John Brown's "
            "raid on Harper's Ferry, and the countdown to the 1860 election that "
            "would trigger secession. Vermont's deep Republican culture made Hall's "
            "governorship an antislavery executive moment.\n\n"
            "He wrote a notable early history of Vermont — contributing to his "
            "state's historical memory as both a politician and a historian.\n\n"
            "He lived ninety years — his life spanning from early Vermont statehood "
            "through the Civil War to the Gilded Age.\n\n"
            "He was Vermont's most experienced Whig-to-Republican transition politician."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Vermont Whig/Republican Congressman (1833–1843) and Governor (1858–1860); decade in Congress during Bank War and nullification crisis; governorship during Lincoln-Douglas debates and John Brown's raid; Vermont historian; Whig-to-Republican transition politician; lived ninety years spanning early Vermont statehood to the Gilded Age.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Vermont's Whig and then Republican political culture — the state's antislavery alignment — created the political base for Hall's long public career",
            "The Jacksonian-era political crises — the Bank War and nullification debate — created the defining issues of Hall's congressional decade",
            "Vermont's strong Republican culture in the 1850s — the state's early Republican alignment after the Whig collapse — created the governorship opportunity during the most explosive years of the sectional crisis"
        ],
        "effects": [
            "His decade in Congress contributed Vermont's Whig antislavery perspective to the Bank War and nullification debates",
            "His governorship contributed to Vermont's antislavery executive leadership during the critical pre-Civil War years",
            "His Vermont history contributed to the documentation of the state's early history — the scholarly record of Vermont's founding",
            "His long life and combined career contributed to the historical memory of Vermont's political evolution from Whig to Republican"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Vermont Congressman 1833–1843"},
            {"target": "vermont", "verb": "GOVERNS", "note": "Governor of Vermont 1858–1860"},
            {"target": "republican-party-united-states", "verb": "MEMBER_OF", "note": "Anti-slavery Whig who became Republican"},
            {"target": "vermont-history", "verb": "DOCUMENTS", "note": "Author of notable early Vermont history"},
            {"target": "john-browns-raid", "verb": "GOVERNS_DURING", "note": "Governor during Harper's Ferry raid 1859"}
        ]
    }),

    ("jared-w-williams", {
        "summary": (
            "Jared Warner Williams (1796–1864) was an American Democratic politician "
            "from New Hampshire who served as U.S. Representative (1837–1841), "
            "U.S. Senator (1853–1854), and Governor of New Hampshire (1847–1849). "
            "His career spanned the late Jacksonian through the early "
            "sectional crisis period — from the Bank War's final years through "
            "the Kansas-Nebraska Act's passage. New Hampshire was a reliably "
            "Democratic state in the antebellum period, and Williams's career "
            "represented the state's Democratic establishment through the "
            "transition from the Bank War debates to the slavery expansion crisis.\n\n"
            "His brief Senate term (1853–1854) came at a critical moment — "
            "the months of the Kansas-Nebraska Act's passage that shattered "
            "the Democratic Party's northern coalition.\n\n"
            "He was a Lancaster New Hampshire lawyer.\n\n"
            "He held three major offices in New Hampshire's Democratic hierarchy."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "New Hampshire Democratic Congressman (1837–1841), Governor (1847–1849), and Senator (1853–1854); three major offices spanning Jacksonian era to Kansas-Nebraska crisis; brief Senate term during the Act's passage; Lancaster New Hampshire lawyer; New Hampshire Democratic establishment leader.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New Hampshire's reliably Democratic political culture — the state's Jacksonian Democratic alignment that persisted from the 1820s through the antebellum period — created the political base for Williams's three-office career",
            "The Kansas-Nebraska Act's political earthquake — the legislation that destroyed northern Democratic solidarity and created the Republican Party — created the crisis that coincided with Williams's Senate term",
            "New Hampshire's legal community — the Lancaster and Concord lawyers who formed the Democratic Party's political elite — provided the professional network for Williams's career"
        ],
        "effects": [
            "His three-office career contributed to New Hampshire's Democratic leadership documentation — the state's political elite during the Jacksonian and pre-Civil War periods",
            "His brief Senate term contributed New Hampshire's Democratic perspective to the Kansas-Nebraska crisis",
            "His governorship contributed to New Hampshire's executive governance during the post-Mexican War period",
            "His career contributed to the historical record of northern Democratic politicians who faced the party-shattering slavery debate"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "New Hampshire Senator 1853–1854"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "New Hampshire Congressman 1837–1841"},
            {"target": "new-hampshire", "verb": "GOVERNS", "note": "Governor of New Hampshire 1847–1849"},
            {"target": "kansas-nebraska-act", "verb": "SERVES_DURING", "note": "Senator during the Act's passage"},
            {"target": "democratic-party-united-states", "verb": "MEMBER_OF", "note": "New Hampshire Democratic establishment"}
        ]
    }),

    ("daniel-d-tompkins", {
        "summary": (
            "Daniel D. Tompkins (1774–1825) was an American Democratic-Republican "
            "politician from New York who served as Governor of New York (1807–1817) "
            "and Vice President of the United States under James Monroe (1817–1825). "
            "As Governor he managed New York's crucial War of 1812 mobilization — "
            "financing much of the state's military contribution out of his own "
            "credit and pocket, a sacrifice that damaged his personal finances "
            "and health irreparably. His Vice Presidency under Monroe coincided "
            "with the Era of Good Feelings — the one-party fusion politics of "
            "the post-war decade — but Tompkins's own political ambitions and "
            "financial troubles made his tenure difficult.\n\n"
            "He was one of New York's most popular governors and a potential "
            "presidential candidate, but his financial entanglement with New York's "
            "War of 1812 finances gradually destroyed his reputation and health.\n\n"
            "He died at fifty-one, exhausted and financially ruined.\n\n"
            "He was a tragedy of the founding generation — his public sacrifice uncompensated."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "New York Governor (1807–1817) and Vice President under Monroe (1817–1825); personally financed New York's War of 1812 mobilization — ruining his finances and health; Era of Good Feelings Vice President; potential presidential candidate whose War of 1812 sacrifice destroyed him; died at fifty-one; tragic founding generation figure.",
            "significanceCategory": "continental"
        },
        "causes": [
            "New York's central role in the War of 1812 — the state's crucial strategic position and the governor's responsibility for mobilizing troops and resources — created the massive financial burden that Tompkins personally shouldered",
            "The Era of Good Feelings political environment — the one-party fusion politics of Monroe's presidency — created both the Vice Presidential opportunity and the reduced political competition that nonetheless failed to repair Tompkins's reputation",
            "New York's Democratic-Republican political culture — the state's Jeffersonian tradition and its powerful political machine — created the base for Tompkins's gubernatorial success"
        ],
        "effects": [
            "His War of 1812 personal financing contributed to New York's successful military mobilization — at severe personal cost",
            "His Vice Presidency contributed to the Monroe administration's governance during the Era of Good Feelings",
            "His financial ruin contributed to the historical record of the sacrifices demanded of the founding generation's public servants",
            "His potential presidential candidacy's collapse contributed to the political vacuum that led to the fractured 1824 election"
        ],
        "relationships": [
            {"target": "new-york", "verb": "GOVERNS", "note": "Governor of New York 1807–1817"},
            {"target": "james-monroe", "verb": "SERVES_UNDER_AS_VP", "note": "Vice President of the United States 1817–1825"},
            {"target": "war-of-1812", "verb": "FINANCES_NEW_YORKS_CONTRIBUTION_TO", "note": "Personally financed New York's War of 1812 mobilization"},
            {"target": "era-of-good-feelings", "verb": "SERVES_DURING", "note": "Vice President during the one-party fusion era"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "New York Jeffersonian Republican"}
        ]
    }),

    ("henry-hubbard", {
        "summary": (
            "Henry Hubbard (1784–1857) was an American Democratic politician "
            "from New Hampshire who served as U.S. Representative (1817–1829), "
            "U.S. Senator (1835–1841), and Governor of New Hampshire (1841–1843). "
            "His combined congressional and gubernatorial career spanned the "
            "Era of Good Feelings through the heart of the Jacksonian period — "
            "nearly three decades of major office-holding. New Hampshire's "
            "reliably Democratic politics and Hubbard's alignment with the "
            "Jackson coalition gave him sustained electoral success through "
            "multiple state and federal offices. His Senate years covered "
            "the Bank War's final stages and the Van Buren administration.\n\n"
            "He was a Charlestown New Hampshire lawyer who represented the "
            "Connecticut River valley's Democratic communities.\n\n"
            "He held more years of combined major office than almost any other "
            "New Hampshire antebellum politician.\n\n"
            "He was New Hampshire's most experienced early Jacksonian Democrat."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "New Hampshire Democratic Congressman (1817–1829), Senator (1835–1841), and Governor (1841–1843); nearly three decades of major office; Jacksonian Democrat through Bank War and Van Buren era; Charlestown New Hampshire lawyer; most experienced early Jacksonian Democrat in New Hampshire.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New Hampshire's Democratic political culture — the state's strong Jacksonian alignment — created the sustained electoral base for Hubbard's nearly three-decade major office career",
            "The Bank War's political mobilization — Andrew Jackson's war against the Bank of the United States that galvanized Democratic voters — created the defining issue of Hubbard's Senate years",
            "New Hampshire's Connecticut River valley Democratic communities — the farming and commercial towns that reliably supported Democratic candidates — provided Hubbard's core constituency"
        ],
        "effects": [
            "His nearly three decades of major office contributed to New Hampshire's Democratic institutional development",
            "His Senate service contributed New Hampshire's Democratic voice to the Bank War debates",
            "His governorship contributed to New Hampshire's executive governance during the early Tyler administration period",
            "His combined career contributed to the historical documentation of New Hampshire's Jacksonian Democratic dominance"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "New Hampshire Congressman 1817–1829"},
            {"target": "us-senate", "verb": "SERVES_IN", "note": "New Hampshire Senator 1835–1841"},
            {"target": "new-hampshire", "verb": "GOVERNS", "note": "Governor of New Hampshire 1841–1843"},
            {"target": "andrew-jackson", "verb": "SUPPORTS", "note": "Jacksonian Democrat through the Bank War"},
            {"target": "bank-of-the-united-states", "verb": "OPPOSES", "note": "Democratic senator opposing recharter"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 94 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich(slug, data)
    print("Done.")
