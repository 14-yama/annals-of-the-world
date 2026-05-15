#!/usr/bin/env python3
"""
Batch 74 — 8 entities: Dudley Chase, Epaphroditus Ransom, George Hancock,
John Black, John Rutherfoord, Jonathan Brace, Garret Dorset Wall, Thomas Chilton
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

    ("dudley-chase", {
        "summary": (
            "Dudley Chase (1771–1846) "
            "was an American Democratic-Republican "
            "politician from Vermont who "
            "served as a U.S. Senator "
            "(1813–1817 and 1825–1831) "
            "— his two non-consecutive "
            "Senate stints spanning "
            "the War of 1812 era "
            "through the Era of Good "
            "Feelings and into the "
            "opening of the Jacksonian "
            "era. A nephew of Supreme "
            "Court Chief Justice "
            "Salmon P. Chase's father, "
            "Chase came from one of "
            "New England's most "
            "distinguished legal "
            "and political families.\n\n"
            "His first Senate term "
            "(1813–1817) coincided "
            "with the War of 1812's "
            "final phase — the "
            "New England states' "
            "Hartford Convention "
            "protests, the British "
            "burning of Washington, "
            "and the eventual peace "
            "at Ghent — a period "
            "when New England "
            "Federalists were "
            "deeply hostile to "
            "the war.\n\n"
            "His second Senate "
            "term (1825–1831) "
            "covered the Adams "
            "administration and "
            "the opening of "
            "Jacksonian democracy.\n\n"
            "He was a prominent "
            "Vermont jurist "
            "and civic leader."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Vermont Democratic-Republican Senator (1813–1817 and 1825–1831); two non-consecutive terms spanning the War of 1812 through the Jacksonian era; served during the Hartford Convention protests and the Adams administration; prominent Vermont jurist from the Chase legal-political family.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Vermont's New England political culture — the state's combination of Federalist and Democratic-Republican traditions, its strong antislavery sentiment, and its New England civic culture — created the political environment for Chase's career",
            "The War of 1812's New England opposition — the Hartford Convention's protests against the war, the New England states' refusal to provide militia, and the region's commercial ties to Britain — created the political context for Chase's first Senate term",
            "Vermont's legal culture — the state's tradition of distinguished legal families contributing to both the bench and political offices — provided the family and professional background for Chase's dual legal-political career"
        ],
        "effects": [
            "His War of 1812 era Senate service contributed Vermont's Democratic-Republican perspective to the contentious debates over the war's conduct and peace terms — navigating the tension between national loyalty and New England's commercial interests",
            "His Adams era Senate term contributed Vermont's voice to the transition from Monroe's Era of Good Feelings to Jackson's populist democracy — the political realignment that would permanently reshape American party politics",
            "His career contributed to the Chase family's distinguished tradition of Vermont legal and political service — a tradition that would later include his nephew Salmon P. Chase's extraordinary career as Governor, Senator, Treasury Secretary, and Chief Justice",
            "His two Senate stints illustrated Vermont's consistent political engagement — the small state's disproportionate contribution to national politics through its quality of political leadership"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Vermont Senator 1813–1817 and 1825–1831"},
            {"target": "war-of-1812", "verb": "SERVES_DURING", "note": "Senator during the controversial war"},
            {"target": "hartford-convention", "verb": "SERVES_DURING", "note": "Senator during New England's anti-war protests"},
            {"target": "john-quincy-adams", "verb": "SERVES_DURING", "note": "Senator during the Adams administration"},
            {"target": "vermont", "verb": "REPRESENTS", "note": "Vermont Democratic-Republican senator"}
        ]
    }),

    ("epaphroditus-ransom", {
        "summary": (
            "Epaphroditus Ransom (1798–1859) "
            "was an American Democratic "
            "politician from Michigan "
            "who served as Governor "
            "of Michigan (1848–1850) "
            "during the critical aftermath "
            "of the Mexican-American "
            "War and the national "
            "debate over slavery "
            "in the newly acquired "
            "territories. His governorship "
            "coincided with the "
            "1848 election in which "
            "former President Van "
            "Buren ran as the "
            "Free Soil candidate "
            "— splitting the Democratic "
            "vote in New York and "
            "contributing to Zachary "
            "Taylor's victory.\n\n"
            "Michigan had been "
            "admitted to the Union "
            "in 1837 — one of "
            "the youngest states "
            "in the Union during "
            "Ransom's governorship "
            "— and its political "
            "culture was still "
            "forming, with "
            "strong connections "
            "to New England "
            "migration and "
            "antislavery sentiment.\n\n"
            "He served as a "
            "Michigan Supreme "
            "Court justice before "
            "his governorship.\n\n"
            "He was a significant "
            "figure in Michigan's "
            "early statehood era."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Governor of Michigan (1848–1850) and Supreme Court justice; served during the Free Soil election of 1848 and the Compromise of 1850 debates; governed Michigan during its early statehood formation period; Democrat in a state with strong antislavery sentiment from New England migration.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Michigan's early statehood development — admitted in 1837, the state was still building its institutions and political culture during Ransom's governorship — creating the opportunity for a founding-generation political figure",
            "The Free Soil election of 1848 — Van Buren's third-party candidacy splitting the Democratic vote and electing Taylor — created the political context for Ransom's governorship and the threat to Democratic unity in a state with strong antislavery sentiment",
            "Michigan's New England migration — the large number of settlers from New England who brought their antislavery political culture to Michigan — created the political environment that put pressure on Democrats to address the slavery extension question"
        ],
        "effects": [
            "His governorship contributed to Michigan's institutional development — building the state governmental infrastructure of one of the Union's newer states during a period of rapid population growth",
            "His term governed Michigan through the Compromise of 1850 debates — the crisis that temporarily settled the slavery in the territories question by admitting California as a free state but imposing the Fugitive Slave Act",
            "His Michigan Supreme Court service contributed to the development of Michigan's legal system — the early jurisprudence of a new state establishing its legal traditions",
            "His career illustrated the challenge facing Northern Democrats in the late 1840s — trying to maintain party loyalty while governing states whose antislavery constituencies were increasingly hostile to the Southern slavery extension demands"
        ],
        "relationships": [
            {"target": "michigan", "verb": "GOVERNS", "note": "Governor 1848–1850"},
            {"target": "michigan-supreme-court", "verb": "SERVES_ON", "note": "Michigan Supreme Court Justice"},
            {"target": "free-soil-party", "verb": "SERVES_DURING", "note": "Governor during the Free Soil election of 1848"},
            {"target": "compromise-of-1850", "verb": "GOVERNS_DURING", "note": "Governor through the compromise debates"},
            {"target": "democratic-party-united-states", "verb": "MEMBER_OF", "note": "Michigan Democrat navigating antislavery pressures"}
        ]
    }),

    ("george-hancock", {
        "summary": (
            "George Hancock (1754–1820) "
            "was an American Revolutionary "
            "War soldier and politician "
            "from Virginia who served "
            "in the U.S. House of "
            "Representatives (1793–1797) "
            "as a member of the "
            "Federalist Party — "
            "one of the relatively "
            "small number of Virginians "
            "who aligned with Hamilton's "
            "Federalists rather than "
            "Jefferson's emerging "
            "Democratic-Republican "
            "opposition. He was "
            "an uncle by marriage "
            "of the explorer "
            "William Clark — "
            "the military officer "
            "who co-led the Lewis "
            "and Clark Expedition "
            "(1804–1806).\n\n"
            "Hancock's Federalist "
            "alignment in a heavily "
            "Democratic-Republican "
            "Virginia reflected "
            "the commercial and "
            "military interests "
            "of his class of "
            "Virginia gentry — "
            "those who had seen "
            "the value of effective "
            "national government "
            "during the Revolutionary "
            "War.\n\n"
            "His House service "
            "coincided with the "
            "Jay Treaty controversy "
            "and the Whiskey Rebellion "
            "— the defining controversies "
            "of the mid-1790s.\n\n"
            "He was a significant "
            "figure in early "
            "Virginia Republican-era "
            "politics."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Virginia Federalist Congressman (1793–1797); Revolutionary War soldier; uncle by marriage of William Clark of the Lewis and Clark Expedition; served during the Jay Treaty controversy and Whiskey Rebellion; one of the minority of Virginians who aligned with Hamilton's Federalists rather than Jefferson's Democratic-Republicans.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Virginia's social and political diversity — the tension between the Tidewater gentry's commercial and nationalist instincts that generated some Federalist support and the broader Virginia Jeffersonian tradition — created the minority Federalist position that Hancock occupied",
            "The Revolutionary War experience — Hancock's military service and the lessons learned about the need for effective national government — contributed to his Federalist political alignment despite Virginia's strong Jeffersonian current",
            "The founding era's political formation — the first years of the new constitutional republic when the Federalist-Democratic Republican party split was forming and the Washington administration's policies were defining the political landscape — created the context for Hancock's congressional career"
        ],
        "effects": [
            "His Federalist House service contributed Virginia's minority Federalist voice to the Jay Treaty and Whiskey Rebellion debates — the controversies that helped solidify the Federalist-Republican party division",
            "His family connection to William Clark — whose Lewis and Clark Expedition opened the American West — contributed to the network of Revolutionary-era Virginia families who shaped the early Republic",
            "His career illustrated Virginia Federalism's weakness — the minority position that could not survive the Jeffersonian ascendancy that drove Federalists from Virginia politics after 1800",
            "His service in the founding generation's Congress contributed to establishing the precedents and norms of the new constitutional government's legislative branch"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Virginia Congressman 1793–1797"},
            {"target": "federalist-party-united-states", "verb": "MEMBER_OF", "note": "Minority Virginia Federalist"},
            {"target": "william-clark", "verb": "FAMILY_OF", "note": "Uncle by marriage of Lewis and Clark co-leader"},
            {"target": "jay-treaty", "verb": "SERVES_DURING", "note": "Congressman during the Jay Treaty controversy"},
            {"target": "whiskey-rebellion", "verb": "SERVES_DURING", "note": "Congressman during the Whiskey Rebellion"}
        ]
    }),

    ("john-black", {
        "summary": (
            "John Black (1781–1845) "
            "was an American Democratic "
            "politician from Mississippi "
            "who served in the U.S. "
            "Senate (1826–1838) — "
            "a twelve-year tenure "
            "spanning the final years "
            "of the Era of Good "
            "Feelings, the Jacksonian "
            "revolution, and into "
            "the Van Buren administration. "
            "Mississippi was a "
            "frontier slave state "
            "whose rapid growth "
            "in the cotton era "
            "made it one of the "
            "most economically "
            "dynamic regions of "
            "the antebellum South.\n\n"
            "Black's Senate tenure "
            "covered the major "
            "Jacksonian battles "
            "— the Bank War, the "
            "Nullification Crisis, "
            "the Indian Removal "
            "Act, and the beginning "
            "of the abolition "
            "controversy. Mississippi's "
            "rapid growth through "
            "cotton agriculture "
            "and slave labor "
            "gave Black's Senate "
            "voice a significant "
            "economic perspective "
            "on national policy.\n\n"
            "Mississippi had been "
            "admitted to the Union "
            "in 1817 — still a "
            "young state during "
            "the early part of "
            "Black's Senate tenure.\n\n"
            "He was a lawyer "
            "before entering politics."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Mississippi Democratic Senator (1826–1838); twelve-year tenure spanning Jacksonian battles — the Bank War, Nullification Crisis, Indian Removal, and abolition controversy; represented Mississippi's cotton economy and slave society; served as Mississippi matured from frontier territory to major cotton state.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Mississippi's cotton boom — the explosive growth of cotton agriculture on newly cleared land worked by enslaved people that made Mississippi one of the wealthiest and fastest-growing states in the Union during Black's Senate tenure — created the economic power behind his political voice",
            "The Jacksonian revolution — Andrew Jackson's populist politics, his Bank War, and his Indian Removal policy that reshaped American political culture — created the major policy context for Black's Senate career",
            "Mississippi's frontier politics — the rough-and-tumble democracy of a young state with strong land speculation interests, cotton planter elites, and Scots-Irish settler culture — shaped the political environment Black navigated"
        ],
        "effects": [
            "His twelve-year Senate tenure contributed Mississippi's voice to the Jacksonian era's defining battles — the Bank War debates, the Nullification Crisis response, and the Indian Removal Act that cleared lands for cotton agriculture",
            "His Senate service contributed to the political infrastructure of Mississippi's early statehood — helping establish the patterns of representation that would make the Mississippi Delta one of the wealthiest and most politically powerful regions of the antebellum South",
            "His career contributed to the Southern Democratic coalition that Jackson assembled — the combination of frontier democracy, slaveholder interests, and anti-bank sentiment that dominated American politics through the 1830s",
            "His death in 1845 placed him among the Jacksonian generation who built the Democratic Party coalition but did not live to see the slavery extension crisis that would eventually destroy it"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Mississippi Senator 1826–1838"},
            {"target": "andrew-jackson", "verb": "SUPPORTS", "note": "Jacksonian Democrat from Mississippi"},
            {"target": "bank-war", "verb": "PARTICIPATES_IN", "note": "Senator during the Bank of the United States controversy"},
            {"target": "indian-removal-act", "verb": "SERVES_DURING", "note": "Senator during Indian Removal that cleared land for cotton"},
            {"target": "mississippi", "verb": "REPRESENTS", "note": "Mississippi's cotton economy senator"}
        ]
    }),

    ("john-rutherfoord", {
        "summary": (
            "John Rutherfoord (1778–1866) "
            "was an American Democratic-Republican "
            "and later Whig politician "
            "from Virginia who served "
            "in the U.S. House of "
            "Representatives (1817–1819) "
            "and as Acting Governor "
            "of Virginia (1841–1842). "
            "His remarkably long life "
            "(1778–1866) spanned from "
            "the founding era to "
            "the Civil War — he was "
            "born while the "
            "Revolutionary War was "
            "still being fought "
            "and died a year after "
            "the war ended.\n\n"
            "His Acting Governorship "
            "of Virginia came during "
            "the Tyler administration "
            "— Tyler himself was "
            "a Virginian — and "
            "during the politically "
            "complex period when "
            "Virginia's political "
            "culture was navigating "
            "the transition from "
            "Whig to Democrat "
            "to eventually secessionist.\n\n"
            "Virginia's political "
            "significance in the "
            "antebellum era was "
            "enormous — the "
            "Mother of Presidents, "
            "the largest Southern "
            "state, and the "
            "center of the "
            "Southern political "
            "tradition.\n\n"
            "He lived to witness "
            "both the founding "
            "era and the Civil War."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Virginia Congressman (1817–1819) and Acting Governor (1841–1842); remarkably long life (1778–1866) spanning the Revolutionary War era to after the Civil War; served during the Tyler administration's Virginia political context; witnessed Virginia's political evolution from founding era to secession.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Virginia's dominant political position in the early Republic — the state that produced Washington, Jefferson, Madison, Monroe, and John Tyler, and that dominated national politics through the Virginia Dynasty — created the political environment for Rutherfoord's career",
            "The Era of Good Feelings — the Monroe administration's brief political consensus that made Democratic-Republican affiliation the default for Virginia politicians — provided the political framework for Rutherfoord's House tenure",
            "Virginia's complex Whig-Democrat transition — the political evolution from the Virginia Dynasty's Democratic-Republicanism through a Whig phase to eventual Democratic and then secessionist alignment — created the shifting political landscape of Rutherfoord's long life"
        ],
        "effects": [
            "His Acting Governorship contributed to Virginia's governance during the Tyler era — administering the largest Southern state during one of the most politically chaotic periods of antebellum history",
            "His career contributed to Virginia's political tradition — the pattern of distinguished Virginia gentry participating in both state and national political offices across long careers",
            "His extraordinary lifespan (1778–1866) made him a living link between the founding era and the Civil War — personally witnessing the birth, growth, and near-dissolution of the republic",
            "His political service illustrated Virginia's transition from national dominance in the founding era to regional leadership in the secessionist era — the long decline of Virginian national political power"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Virginia Congressman 1817–1819"},
            {"target": "virginia", "verb": "GOVERNS", "note": "Acting Governor of Virginia 1841–1842"},
            {"target": "john-tyler", "verb": "CONTEMPORANEOUS_WITH", "note": "Virginia political contemporary of Tyler's presidency"},
            {"target": "era-of-good-feelings", "verb": "SERVES_DURING", "note": "Congressman during Monroe's political consensus"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "Virginia Democratic-Republican politician"}
        ]
    }),

    ("jonathan-brace", {
        "summary": (
            "Jonathan Brace (1754–1837) "
            "was an American Federalist "
            "politician from Connecticut "
            "who served in the U.S. "
            "House of Representatives "
            "(1797–1799) during the "
            "Adams administration "
            "and the quasi-war with "
            "France — one of the "
            "most politically intense "
            "periods of the early "
            "republic. A Connecticut "
            "Federalist, Brace "
            "represented the "
            "Standing Order — "
            "Connecticut's established "
            "Congregationalist "
            "church-state alliance "
            "that made the state "
            "one of the most "
            "reliably Federalist "
            "in the Union.\n\n"
            "His House term coincided "
            "with the Adams administration's "
            "quasi-war with France "
            "— the undeclared naval "
            "conflict that produced "
            "the XYZ Affair, the "
            "Alien and Sedition "
            "Acts, and the "
            "first serious test "
            "of the new republic's "
            "foreign policy capacity.\n\n"
            "Connecticut's Federalist "
            "tradition was among "
            "the most durable "
            "in the nation — "
            "the state maintained "
            "Federalist governance "
            "through the War "
            "of 1812 and the "
            "Hartford Convention.\n\n"
            "He was a prominent "
            "Hartford civic leader."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Connecticut Federalist Congressman (1797–1799); served during the Adams quasi-war with France, the XYZ Affair, and the Alien and Sedition Acts; representative of Connecticut's Standing Order Federalism; part of the founding generation's critical foreign policy debates.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Connecticut's Standing Order — the established alliance between the Congregationalist church, the Harvard/Yale-educated legal elite, and the Federalist Party that made Connecticut one of the most hierarchically organized and Federalist states in the Union — created the political culture that produced Brace's career",
            "The quasi-war with France — the diplomatic crisis arising from French privateering against American shipping and the XYZ Affair — created the intense foreign policy controversy of Brace's House tenure",
            "The Adams administration's Alien and Sedition Acts — the partisan legislation aimed at suppressing Democratic-Republican opposition — created the defining political controversy of Brace's congressional service"
        ],
        "effects": [
            "His House service contributed Connecticut's Federalist votes to the Adams administration's foreign policy debates — supporting the naval buildup, the quasi-war measures, and the controversial Alien and Sedition Acts",
            "His career contributed to Connecticut's Federalist tradition — the Standing Order politics that would persist through the Hartford Convention and represent the most enduring Federalism in the nation",
            "His service illustrated the founding generation's foreign policy challenges — the new republic's attempt to maintain neutrality while navigating the Napoleonic Wars' disruption of Atlantic trade",
            "His death in 1837 placed him among the extraordinarily long-lived founding generation who witnessed the full arc from the Adams quasi-war through the Jacksonian era's democratic transformation"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Connecticut Congressman 1797–1799"},
            {"target": "federalist-party-united-states", "verb": "MEMBER_OF", "note": "Connecticut Standing Order Federalist"},
            {"target": "quasi-war", "verb": "SERVES_DURING", "note": "Congressman during undeclared war with France"},
            {"target": "alien-and-sedition-acts", "verb": "SERVES_DURING", "note": "Congressman during partisan Alien and Sedition legislation"},
            {"target": "connecticut", "verb": "REPRESENTS", "note": "Connecticut's Federalist civic leader"}
        ]
    }),

    ("garret-dorset-wall", {
        "summary": (
            "Garret Dorset Wall (1783–1850) "
            "was an American Democratic "
            "politician from New Jersey "
            "who served as a U.S. Senator "
            "(1835–1841) during the "
            "Van Buren administration "
            "and the Panic of 1837. "
            "Wall was a prominent "
            "New Jersey Democrat whose "
            "Senate career aligned "
            "with the hard-money "
            "Jacksonian tradition "
            "— supporting the "
            "Independent Treasury "
            "and opposing the "
            "re-chartering of the "
            "Bank of the United States.\n\n"
            "New Jersey's political "
            "history was complex "
            "in the antebellum era "
            "— a relatively small "
            "state with significant "
            "commercial interests "
            "tied to both New York "
            "City and Philadelphia "
            "markets, genuine "
            "two-party competition, "
            "and an early antislavery "
            "tradition (New Jersey "
            "had been one of "
            "the first states "
            "to enact gradual "
            "emancipation).\n\n"
            "His Senate service "
            "covered the major "
            "Jacksonian battles "
            "— the Bank War "
            "aftermath and "
            "the Panic of 1837 "
            "policy responses.\n\n"
            "He was a New Jersey "
            "lawyer before politics."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "New Jersey Democratic Senator (1835–1841); hard-money Jacksonian supporting the Independent Treasury; served during the Van Buren presidency and the Panic of 1837; part of New Jersey's complex antebellum politics in a state with commercial ties to both New York and Philadelphia.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New Jersey's commercial geography — the state's position between New York City and Philadelphia, with significant merchant and manufacturing interests tied to both markets, created the economic interests that shaped Wall's Jacksonian Democratic politics",
            "The Bank War's aftermath — Andrew Jackson's destruction of the Second Bank of the United States and the establishment of the pet-bank system — created the banking policy context that the Van Buren administration inherited and that Wall supported through the Independent Treasury",
            "New Jersey's Democratic tradition — the party organization that channeled the state's egalitarian farming and artisan constituencies into the Democratic coalition — provided the political infrastructure for Wall's Senate career"
        ],
        "effects": [
            "His Senate service contributed New Jersey's Democratic votes to the Van Buren administration's economic policy — supporting the Independent Treasury as the Democratic response to the Panic of 1837",
            "His hard-money alignment contributed to the Jacksonian Democratic coalition's economic policy positions — the anti-bank, pro-specie tradition that defined Democratic financial policy through the antebellum era",
            "His career contributed to New Jersey's Democratic political tradition — the party organization that, despite genuine Whig competition, established Democratic dominance in key New Jersey constituencies",
            "His death in 1850 placed him among the Jacksonian generation who shaped the antebellum Democratic Party but did not live to see the slavery extension crisis's final resolution"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "New Jersey Senator 1835–1841"},
            {"target": "martin-van-buren", "verb": "SUPPORTS", "note": "Jacksonian Democrat serving during Van Buren presidency"},
            {"target": "independent-treasury", "verb": "SUPPORTS", "note": "Hard-money Democrat backing Independent Treasury"},
            {"target": "panic-of-1837", "verb": "SERVES_DURING", "note": "Senator during the economic depression"},
            {"target": "new-jersey", "verb": "REPRESENTS", "note": "New Jersey Democratic senator"}
        ]
    }),

    ("thomas-chilton", {
        "summary": (
            "Thomas Chilton (1798–1854) "
            "was an American Whig "
            "politician and Baptist "
            "minister from Kentucky "
            "who served in the U.S. "
            "House of Representatives "
            "(1827–1835) and is "
            "perhaps best remembered "
            "as a close friend and "
            "collaborator of Davy "
            "Crockett — he helped "
            "Crockett write his "
            "celebrated autobiography, "
            "'A Narrative of the "
            "Life of David Crockett "
            "of the State of Tennessee' "
            "(1834), one of the "
            "most famous memoirs "
            "in American political "
            "history. The Crockett "
            "autobiography is a "
            "foundational text of "
            "American frontier "
            "mythology — its tall-tale "
            "humor and anti-Jackson "
            "politics shaped the "
            "popular image of "
            "the American frontiersman.\n\n"
            "Chilton was a Tennessee "
            "anti-Jackson Whig "
            "before moving to "
            "Kentucky, and his "
            "friendship with "
            "Crockett reflected "
            "their shared anti-Jacksonian "
            "political alignment.\n\n"
            "His Baptist ministry "
            "combined with his "
            "legal-political career "
            "in the tradition "
            "of the frontier "
            "preacher-politician.\n\n"
            "He died in 1854 in "
            "Owensboro, Kentucky."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Kentucky Whig Congressman (1827–1835) and Baptist minister; collaborated with Davy Crockett on his celebrated 1834 autobiography — a foundational text of American frontier mythology; anti-Jacksonian Whig whose political and literary collaboration with Crockett shaped popular American frontier imagery.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The anti-Jackson political movement — the coalition of former Federalists, National Republicans, and Jackson opponents that coalesced into the Whig Party — created the political alignment shared by Chilton and Crockett that underpinned their collaboration",
            "Davy Crockett's political career and need for literary support — Crockett's national fame and his opposition to Jackson's Indian removal policy created the demand for a celebrity memoir that Chilton helped provide through his literary assistance",
            "Frontier Baptist religious culture — the Methodist and Baptist Protestant evangelical movement that was the dominant religious culture of the American frontier — provided the spiritual and social context for Chilton's combination of ministry and politics"
        ],
        "effects": [
            "His collaboration on the Crockett autobiography contributed one of the most culturally significant American memoirs — a text that shaped the popular image of the American frontiersman for generations and became a foundational narrative of American mythology",
            "The Crockett autobiography he helped write contributed to the anti-Jackson political propaganda of the Whig Party — Crockett's stories of frontier egalitarianism and opposition to Jackson's high-handed policies served Whig electoral purposes",
            "His Congressional service contributed Kentucky's Whig perspective to the Bank War debates and the Indian Removal controversy — the major policy battles of the Jackson era",
            "His combination of Baptist ministry and political service illustrated the frontier preacher-politician tradition — the pattern of religious leaders who wielded political influence in Kentucky and Tennessee's evangelical Protestant communities"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Kentucky Congressman 1827–1835"},
            {"target": "davy-crockett", "verb": "COLLABORATES_WITH", "note": "Helped Crockett write his 1834 autobiography"},
            {"target": "whig-party-united-states", "verb": "MEMBER_OF", "note": "Anti-Jacksonian Whig politician"},
            {"target": "kentucky", "verb": "REPRESENTS", "note": "Kentucky Whig congressman and Baptist minister"},
            {"target": "american-frontier-mythology", "verb": "CONTRIBUTES_TO", "note": "Crockett autobiography collaborator shaping frontier imagery"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 74 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
