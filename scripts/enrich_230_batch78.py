#!/usr/bin/env python3
"""
Batch 78 — 8 entities: Joaquín Abarca, John Alsop King, José María Alfaro Zamora,
Albert C. Greene, Timothy Jenkins, Hans Hagerup Falbe, Jean-Baptiste Gay vicomte de Martignac,
John Catron
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

    ("joaquín-abarca", {
        "summary": (
            "Joaquín Abarca (1782–1844) "
            "was a Spanish Catholic bishop "
            "and ultra-conservative "
            "politician who served "
            "as Bishop of León "
            "and was one of the "
            "most vocal supporters "
            "of the Carlist cause "
            "in 19th-century Spain "
            "— the legitimist movement "
            "that championed Don "
            "Carlos's claim to "
            "the Spanish throne "
            "against the liberal "
            "constitutional monarchy "
            "of Queen Isabella II. "
            "His political activity "
            "made him one of the "
            "most politically engaged "
            "bishops of the Spanish "
            "hierarchy's ultra-royalist "
            "wing.\n\n"
            "Abarca was a founder "
            "and key figure in "
            "El Restaurador — "
            "the leading Carlist "
            "newspaper — using "
            "journalism as a "
            "weapon in the "
            "political and "
            "religious conflict.\n\n"
            "The First Carlist War "
            "(1833–1839) — the "
            "civil war between "
            "Carlists and Isabellinos "
            "that devastated Spain — "
            "was the conflict "
            "that his Carlist "
            "advocacy helped "
            "provoke and sustain.\n\n"
            "He represented the "
            "alliance of throne "
            "and altar in "
            "its most extreme form."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Spanish Bishop of León and Carlist political leader (1782–1844); co-founder of El Restaurador, the leading Carlist newspaper; ultra-royalist champion of Don Carlos against liberal constitutional monarchy; his advocacy contributed to the First Carlist War (1833–1839); represented the throne-and-altar alliance at its most extreme.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Spanish succession crisis — Ferdinand VII's 1830 pragmatic sanction abolishing Salic Law to allow his daughter Isabella to succeed him, and the Carlist challenge that this liberal concession provoked — created the political crisis around which Abarca's Carlist advocacy organized",
            "The Spanish Church's ultra-royalist culture — the Catholic hierarchy's deep identification with absolute monarchy and its fear of liberal constitutionalism as a threat to Church property, education, and institutional power — created the clerical perspective from which Abarca's Carlist politics emerged",
            "The First Carlist War's media dimension — the need for Carlist propaganda and political journalism to mobilize support and articulate the legitimist cause — created the context for El Restaurador that Abarca helped found"
        ],
        "effects": [
            "His Carlist advocacy contributed to the First Carlist War — the civil conflict that claimed hundreds of thousands of Spanish lives and established the Carlist-Liberal division as the defining fault line of 19th-century Spanish politics",
            "El Restaurador that he co-founded contributed to the Carlist media infrastructure — the newspapers, pamphlets, and publications that sustained the legitimist cause through the civil war and beyond",
            "His clerical Carlism contributed to the Spanish Church's political alignment — the identification of the Catholic hierarchy's most conservative elements with the Carlist cause that shaped Spanish Church-state relations for generations",
            "His career illustrated the 'throne and altar' alliance at its most extreme — the unity of ultra-royalist politics and Counter-Reformation Catholicism that defined one pole of Spanish political life throughout the 19th century"
        ],
        "relationships": [
            {"target": "carlist-movement", "verb": "LEADS", "note": "Bishop and Carlist political leader"},
            {"target": "el-restaurador", "verb": "FOUNDS", "note": "Co-founder of leading Carlist newspaper"},
            {"target": "first-carlist-war", "verb": "ADVOCATES_FOR", "note": "Contributed to the Carlist cause that triggered the war"},
            {"target": "don-carlos", "verb": "SUPPORTS", "note": "Clerical champion of the Carlist pretender"},
            {"target": "spanish-catholic-church", "verb": "LEADS", "note": "Bishop of León and ultra-royalist churchman"}
        ]
    }),

    ("john-alsop-king", {
        "summary": (
            "John Alsop King (1788–1867) "
            "was an American Whig and "
            "Republican politician from "
            "New York who served in "
            "the U.S. House of Representatives "
            "(1819–1821 and 1849–1851) "
            "and as Governor of New York "
            "(1857–1859) — the first "
            "Republican governor "
            "of New York. His father "
            "was Rufus King — the "
            "Federalist senator and "
            "presidential candidate "
            "— placing John Alsop "
            "King in the transition "
            "generation between "
            "the Federalist founding "
            "generation and the "
            "antislavery Republican "
            "Party.\n\n"
            "As New York's first "
            "Republican governor, "
            "King presided over "
            "America's most populous "
            "and commercially powerful "
            "state at the moment "
            "the Republican Party "
            "was consolidating "
            "its political organization "
            "and its antislavery platform.\n\n"
            "His governorship "
            "(1857–1859) coincided "
            "with the Dred Scott "
            "decision and the "
            "Lecompton Constitution "
            "controversy — the "
            "most explosive "
            "slavery-extension "
            "debates of the decade "
            "before the Civil War.\n\n"
            "His family represented "
            "the continuity between "
            "Federalism and "
            "Republican antislavery."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "First Republican Governor of New York (1857–1859); son of Federalist senator Rufus King; U.S. Congressman (1819–1821 and 1849–1851); presided over New York during the Dred Scott decision and Lecompton Constitution crisis; represented the continuity from Federalism through Whiggery to Republicanism; governed America's most powerful state at a crucial moment.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Republican Party's rise — the new antislavery party's rapid growth from 1854 that made it competitive in Northern states like New York by 1856 — created the party organization that enabled King to become the first Republican governor of New York",
            "The Kansas-Nebraska Act's political earthquake — the destruction of the Missouri Compromise in 1854 that shattered the Whig Party and created the Free Soil-Republican coalition — created the political realignment that gave King his party",
            "King's family standing — the son of Federalist senator Rufus King, with access to New York's highest social and political circles — provided the prestige and connections that underpinned his long political career across three different party affiliations"
        ],
        "effects": [
            "His Republican governorship established the party's governing credibility in New York — demonstrating that the new antislavery party could win and govern the largest Northern state",
            "His governorship during the Dred Scott decision and Lecompton controversy contributed New York's institutional voice to the national crisis over slavery extension — New York's response being crucial to the Republican Party's national positioning",
            "His career bridging Federalism, Whiggery, and Republicanism contributed to the political continuity between the founding era's moderate nationalism and the Civil War era's antislavery nationalism",
            "His family's legacy — the King family's continuity from Rufus King's Constitutional Convention participation through John Alsop King's Republican governorship — illustrated the multigenerational nature of American political dynasties"
        ],
        "relationships": [
            {"target": "new-york", "verb": "GOVERNS", "note": "First Republican Governor of New York 1857–1859"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Congressman 1819–1821 and 1849–1851"},
            {"target": "republican-party-united-states", "verb": "MEMBER_OF", "note": "First Republican governor of New York"},
            {"target": "rufus-king", "verb": "SON_OF", "note": "Son of Federalist senator and presidential candidate"},
            {"target": "dred-scott-decision", "verb": "GOVERNS_DURING", "note": "New York governor when Dred Scott was decided"}
        ]
    }),

    ("josé-maría-alfaro-zamora", {
        "summary": (
            "José María Alfaro Zamora "
            "(1794–1856) was a Costa "
            "Rican politician who "
            "served as Head of State "
            "of Costa Rica (1842–1844) "
            "during the turbulent "
            "post-independence period "
            "when Costa Rica was "
            "establishing its institutions "
            "after the collapse of the "
            "Central American Federation. "
            "Costa Rica in this era "
            "was one of the smallest "
            "and most isolated of "
            "the Central American "
            "states — its population "
            "concentrated in the "
            "Central Valley, its "
            "economy based on subsistence "
            "agriculture and the "
            "emerging coffee sector "
            "that would transform "
            "the country in subsequent decades.\n\n"
            "Alfaro's tenure came "
            "after Francisco Morazán "
            "— the Central American "
            "liberal hero — briefly "
            "seized power in Costa Rica "
            "in 1842 before being "
            "overthrown and executed.\n\n"
            "Alfaro governed during "
            "the difficult process "
            "of building Costa "
            "Rica's state institutions "
            "after the Central "
            "American Federation's dissolution.\n\n"
            "He was part of Costa "
            "Rica's founding generation "
            "of political leaders."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Costa Rican Head of State (1842–1844); governed during the turbulent post-independence period after the Central American Federation's collapse and after Morazán's execution; part of Costa Rica's founding generation building state institutions; governed as the coffee economy was beginning to transform the country.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Central American Federation's collapse — the dissolution of the regional political union that had linked Costa Rica, Guatemala, El Salvador, Honduras, and Nicaragua since independence — created the need for each state to build its own institutions",
            "Francisco Morazán's overthrow and execution in Costa Rica (1842) — the brief seizure of power by the liberal Central American hero and his subsequent execution — created the political crisis that preceded Alfaro's governance",
            "Costa Rica's isolation and small size — the relatively small, isolated Central Valley population and the lack of the violent caste conflicts and indigenous-mestizo tensions that plagued other Central American states — created the relatively stable conditions in which Costa Rica's founding institutions developed"
        ],
        "effects": [
            "His governance contributed to Costa Rica's post-federation institution-building — establishing the governmental practices and political norms of the emerging independent state",
            "His administration oversaw the beginning of Costa Rica's coffee transformation — the period when coffee cultivation in the Central Valley was beginning to generate the commercial wealth that would fund Costa Rica's distinctive development path",
            "His governance helped establish Costa Rica's pattern of relatively stable civilian rule — the tradition of peaceful political transitions that would make Costa Rica exceptional among Central American states",
            "His career contributed to Costa Rica's founding generation — the political leaders who built the institutions of a small, peaceful state in the violent context of post-colonial Central America"
        ],
        "relationships": [
            {"target": "costa-rica", "verb": "GOVERNS", "note": "Head of State 1842–1844"},
            {"target": "central-american-federation", "verb": "GOVERNS_AFTER_COLLAPSE_OF", "note": "Led Costa Rica after the federation dissolved"},
            {"target": "francisco-morazán", "verb": "SUCCEEDS_AFTER", "note": "Governed after Morazán's overthrow and execution"},
            {"target": "costa-rican-coffee-economy", "verb": "OVERSEES_BEGINNING_OF", "note": "Governed during the coffee transformation's early phase"},
            {"target": "central-america", "verb": "LEADS_WITHIN", "note": "Costa Rican founding-era political leader"}
        ]
    }),

    ("albert-c-greene", {
        "summary": (
            "Albert Collins Greene (1792–1863) "
            "was an American Whig "
            "politician from Rhode Island "
            "who served in the U.S. "
            "Senate (1845–1851) and "
            "as Rhode Island's Attorney "
            "General. His Senate career "
            "placed him in the chamber "
            "during some of the most "
            "consequential years "
            "of American antebellum "
            "politics — the Texas "
            "annexation, the Mexican-American "
            "War, the Wilmot Proviso "
            "debate, the California "
            "gold rush, and the "
            "Compromise of 1850 "
            "that attempted to "
            "settle the slavery "
            "extension controversy. "
            "As a Rhode Island "
            "Whig, he represented "
            "a small but commercially "
            "significant state "
            "whose textile manufacturing "
            "had commercial ties "
            "to both Northern "
            "free labor and Southern cotton.\n\n"
            "Rhode Island's political "
            "significance in this "
            "era included the "
            "Dorr Rebellion (1842) "
            "— the constitutional "
            "crisis over suffrage "
            "expansion that had "
            "already convulsed "
            "the state before "
            "Greene's Senate term.\n\n"
            "His Attorney General "
            "service contributed "
            "to Rhode Island's "
            "legal development.\n\n"
            "He was a Providence "
            "lawyer and politician."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Rhode Island Whig Senator (1845–1851) and Attorney General; served during the Mexican-American War, Wilmot Proviso debates, and Compromise of 1850; represented Rhode Island's textile manufacturing interests in the antebellum slavery debates; governed after the Dorr Rebellion had convulsed Rhode Island's politics.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Rhode Island's textile manufacturing economy — the state's early industrial development and its commercial connections to both Northern manufacturing and Southern cotton — created the economic perspective from which Greene navigated the antebellum slavery debates",
            "The Dorr Rebellion's political aftermath — the 1842 constitutional crisis over suffrage expansion that had forced Rhode Island to extend voting rights — created the reformed political system within which Greene's Senate career operated",
            "The Mexican-American War and its consequences — the massive territorial acquisition from Mexico that immediately raised the slavery extension question in the Wilmot Proviso and Compromise of 1850 debates — created the major policy controversies of Greene's Senate tenure"
        ],
        "effects": [
            "His Senate service contributed Rhode Island's perspective to the Compromise of 1850 debates — the small New England manufacturing state's voice in the negotiations over slavery extension into Mexican cession territory",
            "His vote on the Compromise of 1850 contributed to the national resolution — or attempted resolution — of the slavery extension controversy that had been opened by the Mexican-American War",
            "His Attorney General service contributed to Rhode Island's legal development — the professional legal culture of a small but commercially significant manufacturing state",
            "His career illustrated Rhode Island's complex position — a small Northern industrial state with commercial ties to the South navigating the antebellum slavery debates from a position of economic ambivalence"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Rhode Island Whig Senator 1845–1851"},
            {"target": "compromise-of-1850", "verb": "VOTES_ON", "note": "Senator during the slavery compromise debates"},
            {"target": "mexican-american-war", "verb": "SERVES_DURING", "note": "Senator during the war and its territorial consequences"},
            {"target": "rhode-island", "verb": "REPRESENTS", "note": "Rhode Island Whig senator and attorney general"},
            {"target": "dorr-rebellion", "verb": "SERVES_AFTER", "note": "Senator after Rhode Island's constitutional crisis"}
        ]
    }),

    ("timothy-jenkins", {
        "summary": (
            "Timothy Jenkins (1799–1859) "
            "was an American Democratic "
            "politician from New York "
            "who served in the U.S. "
            "House of Representatives "
            "(1845–1851 and 1853–1855) "
            "during the antebellum "
            "slavery debates. A New "
            "York Democrat representing "
            "a rural Upstate district, "
            "Jenkins navigated the "
            "complex factional politics "
            "of New York Democracy "
            "in an era when the party "
            "was divided between the "
            "Barnburner antislavery "
            "faction and the Hunker "
            "pro-compromise wing — "
            "a division that eventually "
            "fractured the party "
            "over the Wilmot "
            "Proviso and the "
            "Free Soil movement.\n\n"
            "His congressional service "
            "placed him in the House "
            "during the Mexican-American "
            "War, the 1848 Free Soil "
            "Party challenge, the "
            "Compromise of 1850, "
            "and the Kansas-Nebraska "
            "Act debates that shattered "
            "American political "
            "alignments.\n\n"
            "Upstate New York's "
            "rural Democratic "
            "tradition — distinct "
            "from both the New York "
            "City Tammany machine "
            "and the antislavery "
            "reformers — created "
            "a distinctive political "
            "constituency.\n\n"
            "He was a Oneida "
            "County lawyer "
            "and politician."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "New York Democratic Congressman (1845–1851 and 1853–1855); served during Mexican-American War, Free Soil movement, Compromise of 1850, and Kansas-Nebraska Act debates; navigated New York's Barnburner-Hunker factional divisions; Upstate rural Democratic tradition distinct from Tammany; Oneida County lawyer and politician.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New York's Barnburner-Hunker Democratic split — the factional conflict within the Democratic Party over slavery extension that divided New York Democrats and eventually drove the Barnburners into the 1848 Free Soil Party — created the challenging political environment of Jenkins's congressional career",
            "The Mexican-American War's political consequences — the massive territorial acquisition and the Wilmot Proviso debate over whether slavery would be permitted in the new territories — created the defining controversy of Jenkins's first House term",
            "Upstate New York's rural Democratic tradition — the agricultural counties' political culture that was distinct from both the urban Tammany machine and the antislavery reform politics of the canal corridor — created the distinctive constituency Jenkins represented"
        ],
        "effects": [
            "His House service contributed New York's rural Democratic perspective to the antebellum slavery debates — votes on the Wilmot Proviso, the Compromise of 1850, and the Kansas-Nebraska Act from the Upstate New York Democratic tradition",
            "His navigation of the Barnburner-Hunker split contributed to the complex factional maneuvering within New York Democracy — the compromises and alignments that sustained the party through the era's political earthquakes",
            "His return to Congress (1853–1855) placed him in the House during the Kansas-Nebraska Act debates — the legislation that destroyed the Missouri Compromise and shattered the Democratic Party's Northern wing",
            "His career illustrated the pressures on Northern Democrats in the antebellum era — caught between their party's Southern wing's slavery demands and their Northern constituents' growing antislavery sentiment"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "New York Congressman 1845–1851 and 1853–1855"},
            {"target": "kansas-nebraska-act", "verb": "VOTES_ON", "note": "Congressman during the Kansas-Nebraska Act debates"},
            {"target": "compromise-of-1850", "verb": "VOTES_ON", "note": "House member during the compromise debates"},
            {"target": "democratic-party-united-states", "verb": "MEMBER_OF", "note": "New York Hunker/rural Democrat"},
            {"target": "new-york", "verb": "REPRESENTS", "note": "Upstate Oneida County Democratic congressman"}
        ]
    }),

    ("hans-hagerup-falbe", {
        "summary": (
            "Hans Hagerup Falbe "
            "(1772–1850) was a Norwegian "
            "politician and civil "
            "servant who served "
            "as a member of the "
            "Norwegian Storting "
            "(parliament) and "
            "contributed to "
            "the early institutional "
            "development of "
            "Norway's constitutional "
            "system after the "
            "Constitution of 1814. "
            "As a member of the "
            "generation that "
            "established Norway's "
            "parliamentary institutions "
            "under Swedish union, "
            "Falbe was part of "
            "the Storting's effort "
            "to assert Norwegian "
            "constitutional autonomy "
            "while operating within "
            "the union framework "
            "that Sweden imposed "
            "after the 1814 "
            "independence attempt.\n\n"
            "Norway's early Storting "
            "politics were characterized "
            "by the tension between "
            "Norwegian constitutional "
            "self-assertion and "
            "Swedish royal authority "
            "— a conflict that "
            "would eventually "
            "produce Norway's "
            "full independence "
            "in 1905.\n\n"
            "Falbe's civil service "
            "contributions "
            "helped build "
            "Norway's administrative "
            "institutions in "
            "the post-1814 era.\n\n"
            "He was a founding-era "
            "Norwegian civic figure."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Norwegian Storting member and civil servant (1772–1850); contributed to the early institutional development of Norway's constitutional system after 1814; part of the generation asserting Norwegian parliamentary autonomy within Swedish union; founding-era civic figure of the Norwegian constitutional state.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Norwegian Constitution of 1814 — the founding document that established the Storting and defined the constitutional framework Falbe operated within — created the institutional basis for his parliamentary participation",
            "The Swedish-Norwegian union's political tensions — the ongoing conflict between Norwegian constitutional self-assertion and Swedish royal authority that defined the political challenge of the union period — created the political environment of Falbe's Storting service",
            "Norway's civil service needs — the need to build administrative institutions for a newly constituted state that had been governed as a Danish province for centuries — created the administrative work that Falbe's civil service career addressed"
        ],
        "effects": [
            "His Storting participation contributed to the early development of Norwegian parliamentary practice — the accumulated decisions and procedures that shaped how Norway's legislature operated within the union framework",
            "His civil service contributions helped build Norway's administrative institutions — the bureaucratic structures needed to govern a self-constituting state with limited experience of independent administration",
            "His career contributed to the Norwegian constitutional tradition — the accumulated practice of Norwegian self-governance that would sustain the Storting's autonomy through the union period and ultimately to independence in 1905",
            "His generation's political work — the founding-era Norwegians who built parliamentary practice while asserting constitutional rights — created the institutional foundations that made 1905 independence viable"
        ],
        "relationships": [
            {"target": "storting", "verb": "SERVES_IN", "note": "Norwegian parliament member"},
            {"target": "norwegian-constitution-1814", "verb": "OPERATES_UNDER", "note": "Parliamentary service under the 1814 constitution"},
            {"target": "swedish-norwegian-union", "verb": "SERVES_WITHIN", "note": "Norwegian autonomy advocate within Swedish union"},
            {"target": "norway", "verb": "SERVES", "note": "Norwegian civil servant and founding-era politician"},
            {"target": "norwegian-storting-autonomy", "verb": "CONTRIBUTES_TO", "note": "Early Storting assertion of constitutional rights"}
        ]
    }),

    ("jean-baptiste-gay-vicomte-de-martignac", {
        "summary": (
            "Jean-Baptiste Gay, vicomte "
            "de Martignac (1778–1832) "
            "was a French conservative "
            "liberal statesman of the "
            "Restoration era who served "
            "as President of the Council "
            "(Prime Minister) of France "
            "(1828–1829) under King "
            "Charles X — a brief but "
            "significant ministry "
            "in which Martignac "
            "attempted to steer a "
            "moderate constitutional "
            "course between the "
            "ultraroyalist reaction "
            "and the liberal opposition. "
            "His ministry replaced "
            "the hated ultraroyalist "
            "Villèle government and "
            "tried to reconcile "
            "the Restoration monarchy "
            "with the constitutional "
            "liberalism that "
            "French public opinion increasingly demanded.\n\n"
            "Martignac's moderate "
            "constitutional program "
            "— including press "
            "freedom concessions "
            "and liberal measures "
            "— was too liberal "
            "for Charles X, who "
            "dismissed him in 1829 "
            "and replaced him "
            "with the reactionary "
            "Polignac ministry "
            "that directly provoked "
            "the July Revolution of 1830.\n\n"
            "He was an elegant "
            "orator, a Bordeaux "
            "lawyer, and the "
            "last minister of "
            "the Bourbon Restoration "
            "who might have saved it.\n\n"
            "'He served better "
            "than Charles X deserved.'"
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "French Prime Minister (1828–1829) under Charles X; attempted moderate constitutional middle course between ultraroyalism and liberalism; dismissed and replaced by Polignac ministry that directly provoked the July Revolution of 1830; last chance for the Bourbon Restoration to survive; brilliant Bordeaux orator and lawyer; his dismissal sealed the Restoration's fate.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Charles X's ultraroyalist succession — Louis XVIII's more pragmatic Restoration was replaced by his more doctrinaire brother Charles X who reinstated ultraroyalist policies — created the political crisis that forced the appointment of Martignac as a moderating alternative",
            "The Villèle government's unpopularity — the long ultraroyalist ministry's censorship, clerical influence, and compensation of the emigrant nobles made it deeply hated by liberal France — created the political pressure that brought Martignac to power",
            "French constitutionalism's growth — the expanding educated middle class's commitment to the Charter of 1814 and its rights guarantees — created the liberal political force that Martignac's moderate ministry attempted to accommodate"
        ],
        "effects": [
            "His moderate ministry contributed the last attempt to reconcile the Bourbon Restoration with French liberal constitutionalism — demonstrating that a moderate course was possible even if Charles X refused to sustain it",
            "His dismissal and replacement by the Polignac ultra-reactionary ministry directly contributed to the July Revolution of 1830 — Charles X's rejection of Martignac's moderation set France on the collision course that ended the Bourbon Restoration",
            "His press freedom concessions contributed to the brief flowering of relatively free political discourse in the late Restoration — the publications and political debate that energized the liberal opposition",
            "His career illustrated the tragic pattern of French moderate constitutionalism — the moderate ministers who could have saved the Bourbon monarchy being rejected by kings who preferred reaction until revolution claimed them"
        ],
        "relationships": [
            {"target": "charles-x-of-france", "verb": "SERVES_UNDER", "note": "Prime Minister under Charles X 1828–1829"},
            {"target": "july-revolution-1830", "verb": "PRECEDES", "note": "His dismissal led directly to Polignac and the revolution"},
            {"target": "polignac-ministry", "verb": "REPLACED_BY", "note": "Polignac's reaction replaced his moderation"},
            {"target": "bourbon-restoration", "verb": "ATTEMPTS_TO_SAVE", "note": "Last moderate minister of the Restoration"},
            {"target": "french-constitutionalism", "verb": "ADVOCATES_FOR", "note": "Constitutional liberal within the Restoration framework"}
        ]
    }),

    ("john-catron", {
        "summary": (
            "John Catron (c.1786–1865) "
            "was an American jurist "
            "from Tennessee who served "
            "as an Associate Justice "
            "of the U.S. Supreme Court "
            "(1837–1865) — appointed "
            "by President Andrew Jackson "
            "in one of his final acts "
            "in office. His nearly "
            "28-year Supreme Court "
            "tenure spanned some "
            "of the most consequential "
            "constitutional decisions "
            "in American history, "
            "including Dred Scott v. "
            "Sandford (1857) — one "
            "of the most catastrophic "
            "decisions in American "
            "legal history, in which "
            "Catron wrote a concurrence "
            "supporting the majority's "
            "denial of Black citizenship "
            "and the unconstitutionality "
            "of the Missouri Compromise.\n\n"
            "Catron was a Unionist "
            "despite being a slaveholder "
            "— during the Civil War "
            "he remained loyal to "
            "the Union even as his "
            "home state Tennessee "
            "seceded, continuing "
            "to serve on the "
            "Supreme Court throughout "
            "the war.\n\n"
            "He had previously "
            "served as the first "
            "Chief Justice of "
            "the Tennessee Supreme Court.\n\n"
            "He was a self-made "
            "frontier lawyer "
            "who rose to the "
            "highest court."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "U.S. Supreme Court Associate Justice (1837–1865); appointed by Jackson; wrote concurrence in Dred Scott v. Sandford (1857) supporting denial of Black citizenship; Unionist slaveholder who remained loyal to the Union when Tennessee seceded; first Chief Justice of the Tennessee Supreme Court; 28-year tenure spanning Jackson through the Civil War.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Jackson's judicial appointments — the outgoing president's last-minute expansion of the Supreme Court from seven to nine justices in the Judiciary Act of 1837 created the seats that Jackson filled with loyalists like Catron",
            "Catron's Tennessee legal career — his frontier self-made legal career in Tennessee, including his service as the state's first Chief Justice — provided the credentials and Jackson's personal knowledge for his Supreme Court appointment",
            "The slavery extension controversy — the escalating national crisis over slavery's territorial reach that culminated in the Dred Scott decision — created the constitutional question that produced Catron's most controversial judicial contribution"
        ],
        "effects": [
            "His Dred Scott concurrence contributed to one of the most catastrophic decisions in American legal history — the ruling that denied Black citizenship and invalidated the Missouri Compromise, accelerating the sectional crisis toward civil war",
            "His Civil War Unionism contributed to the Supreme Court's continuity — remaining loyal to the Union when his state seceded, Catron ensured the Supreme Court maintained its institutional function throughout the war",
            "His Tennessee jurisprudence — both as state Chief Justice and as a federal circuit judge in the antebellum South — contributed to the legal development of the western frontier states",
            "His career illustrated the complex position of border-state Unionists — slaveholders who rejected secession but had participated in the legal framework that protected slavery, including the Dred Scott catastrophe"
        ],
        "relationships": [
            {"target": "us-supreme-court", "verb": "SERVES_ON", "note": "Associate Justice 1837–1865"},
            {"target": "dred-scott-v-sandford", "verb": "WRITES_CONCURRENCE_IN", "note": "Supported majority's denial of Black citizenship"},
            {"target": "andrew-jackson", "verb": "APPOINTED_BY", "note": "Jackson's last Supreme Court appointment"},
            {"target": "tennessee-supreme-court", "verb": "SERVES_AS_CHIEF_JUSTICE_OF", "note": "First Chief Justice of Tennessee Supreme Court"},
            {"target": "american-civil-war", "verb": "SERVES_DURING", "note": "Unionist justice serving through Confederate Tennessee"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 78 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
