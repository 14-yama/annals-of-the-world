#!/usr/bin/env python3
"""
Batch 89 — 8 entities: Joseph Hopkinson, Manuel Vicente Maza,
Samuel White, Andrew Butler, John Fairfield, William Leigh Brent,
Benjamin W. Leigh, David Brydie Mitchell
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

    ("joseph-hopkinson", {
        "summary": (
            "Joseph Hopkinson (1770–1842) was an American Federalist lawyer, jurist, "
            "and cultural figure from Pennsylvania who wrote the patriotic song 'Hail, "
            "Columbia' (1798) and served as a U.S. Representative (1815–1819) before "
            "his appointment as a federal judge. His father Francis Hopkinson was a "
            "signer of the Declaration of Independence — placing Joseph in Philadelphia's "
            "foremost legal and cultural elite across two revolutionary generations. "
            "His 'Hail, Columbia' — written as an unofficial national anthem at a "
            "moment of intense Anglo-French maritime conflict — became one of the "
            "most performed patriotic songs of the early republic.\n\n"
            "As a lawyer Hopkinson was one of Philadelphia's most eminent practitioners — "
            "appearing in major federal cases and helping establish the early American bar's "
            "professional standards. His House service came during the Era of Good Feelings "
            "Federalist twilight.\n\n"
            "He served as federal district judge for eastern Pennsylvania from 1828 until "
            "his death, bringing the same erudition to the bench that had distinguished "
            "his legal career.\n\n"
            "He was also a founder of the Philadelphia Museum and a patron of the arts."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Philadelphia Federalist lawyer and jurist who wrote 'Hail, Columbia' (1798); son of Declaration signer Francis Hopkinson; U.S. Representative (1815–1819); federal district judge for eastern Pennsylvania (1828–1842); founder of the Philadelphia Museum; major figure of Philadelphia's legal and cultural elite.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Philadelphia's Federalist cultural elite — the city's leading lawyers, literati, and patriots who formed the most sophisticated urban intellectual environment in the early republic — created the milieu of Hopkinson's life and career",
            "The Quasi-War crisis of 1798 — the undeclared naval conflict with France that produced intense patriotic sentiment and demand for rallying music — created the specific moment that prompted Hopkinson to write 'Hail, Columbia'",
            "His father Francis Hopkinson's legacy — the Declaration signer's cultural and legal prominence — gave Joseph access to Philadelphia's highest circles from birth and shaped the patriotic sensibility that produced his famous song"
        ],
        "effects": [
            "'Hail, Columbia' contributed to American patriotic culture — becoming one of the early republic's most performed anthems and serving as an unofficial national song for over a century",
            "His federal district judgeship contributed to Pennsylvania's legal development — the careful jurisprudence that made the eastern Pennsylvania federal court a model",
            "His legal career contributed to the professionalization of the American bar — his advocacy and scholarship helping establish standards for Philadelphia's premier law practice",
            "His cultural patronage contributed to Philadelphia's arts institutions — the Philadelphia Museum and other cultural organizations that made the city America's cultural capital"
        ],
        "relationships": [
            {"target": "hail-columbia", "verb": "CREATES", "note": "Wrote the patriotic song 'Hail, Columbia' (1798)"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Pennsylvania Congressman 1815–1819"},
            {"target": "francis-hopkinson", "verb": "SON_OF", "note": "Son of Declaration of Independence signer"},
            {"target": "federal-judiciary", "verb": "SERVES_IN", "note": "Federal district judge eastern Pennsylvania 1828–1842"},
            {"target": "federalist-party", "verb": "MEMBER_OF", "note": "Philadelphia Federalist lawyer and politician"}
        ]
    }),

    ("manuel-vicente-maza", {
        "summary": (
            "Manuel Vicente Maza (1779–1839) was an Argentine lawyer and politician "
            "who served as President of the Legislature of Buenos Aires and was a "
            "prominent figure in the complex factional politics of post-independence "
            "Argentina. His career unfolded during the most turbulent decades of "
            "Argentine political history — the civil wars, caudillo rivalries, and "
            "federalism-unitarianism conflicts that followed independence from Spain. "
            "He was closely connected to the Rosas regime — the authoritarian government "
            "of Juan Manuel de Rosas that dominated Buenos Aires from the early 1830s — "
            "serving as a legal and political ally.\n\n"
            "His assassination in 1839 — along with that of his son — was one of the "
            "most dramatic political murders of the Rosas era, illustrating the violent "
            "factional environment of Buenos Aires politics.\n\n"
            "Maza's career represented the lawyer-politician class that tried to navigate "
            "the chaotic transition from colonial to republican governance in the Río de la Plata.\n\n"
            "He was a Buenos Aires lawyer at the center of Argentina's post-independence crises."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Argentine lawyer and President of the Buenos Aires Legislature; ally of Juan Manuel de Rosas; assassinated in 1839 along with his son in one of the era's most dramatic political murders; career navigated the civil wars and caudillo rivalries of post-independence Argentina.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Argentina's post-independence political chaos — the civil wars, federalism-unitarianism conflicts, and caudillo rivalries that prevented stable national governance — created the violent factional environment in which Maza's career and death were embedded",
            "The Rosas regime's authoritarian consolidation — Juan Manuel de Rosas's domination of Buenos Aires politics that required legal and political allies — created the basis for Maza's prominent position as a Rosas ally",
            "The lawyer-politician class's role in Argentine politics — the trained legal professionals who served as intermediaries between caudillo power and institutional governance — created the professional niche that Maza occupied"
        ],
        "effects": [
            "His assassination contributed to the political atmosphere of terror in the Rosas era — the murder of prominent allies and opponents that characterized Buenos Aires factional politics",
            "His death contributed to the historical documentation of Argentine political violence — the cycle of assassination and reprisal that marked the Rosas decades",
            "His career contributed to the Buenos Aires legislative tradition — the institutional forms that persisted even under caudillo pressure",
            "The circumstances of his murder contributed to the eventual delegitimization of the Rosas regime — the political violence that alienated educated Buenos Aires society"
        ],
        "relationships": [
            {"target": "buenos-aires-legislature", "verb": "LEADS", "note": "President of the Buenos Aires Legislature"},
            {"target": "juan-manuel-de-rosas", "verb": "ALLIES_WITH", "note": "Political ally of the Buenos Aires caudillo"},
            {"target": "argentina", "verb": "SERVES_IN", "note": "Post-independence Argentine lawyer and politician"},
            {"target": "argentine-civil-wars", "verb": "NAVIGATES", "note": "Career embedded in post-independence factional conflicts"},
            {"target": "rio-de-la-plata", "verb": "PRACTICES_IN", "note": "Buenos Aires lawyer in the post-independence transition"}
        ]
    }),

    ("samuel-white", {
        "summary": (
            "Samuel White (1770–1809) was an American Federalist politician from Delaware "
            "who served as U.S. Senator (1801–1809). Delaware in this era was the smallest "
            "state in the Union and one of the most reliably Federalist — its tiny population, "
            "commercial ties to Philadelphia, and conservative gentry culture making it a "
            "holdout against Jeffersonian Republican dominance. White served during the "
            "entire Jefferson administration — opposing the Louisiana Purchase, the "
            "Embargo Act, and other Jeffersonian initiatives from the Federalist "
            "minority position.\n\n"
            "He was a Dover Delaware lawyer who represented the commercial and legal "
            "interests of a small state acutely aware of its vulnerability to national "
            "majorities. His Senate service ended with his death in office at thirty-nine.\n\n"
            "Delaware's Federalist Senate delegation during the Jefferson years was among "
            "the most consistent opponents of Republican expansion of federal power.\n\n"
            "He was one of the last Federalist senators from any state to die in office."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Delaware Federalist Senator (1801–1809); served during the entire Jefferson administration opposing the Louisiana Purchase and Embargo Act; Delaware's reliably Federalist Senate delegation; Dover lawyer representing small-state commercial interests; died in office at thirty-nine.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Delaware's Federalist political culture — the tiny state's commercial ties to Philadelphia, conservative gentry, and resistance to Jeffersonian agrarian democracy — created the political base for White's Senate career",
            "The Jefferson administration's Republican transformation — the Louisiana Purchase, Embargo Act, and expanded federal power — created the policy agenda that White consistently opposed as a Federalist senator",
            "Delaware's small-state vulnerability — the state's awareness that its tiny population made it susceptible to national majorities overriding its interests — shaped the defensive Federalism that White represented"
        ],
        "effects": [
            "His Senate opposition contributed to the Federalist critique of Jeffersonian expansion — the minority voice against the Louisiana Purchase and Embargo Act",
            "His career contributed to Delaware's Federalist tradition — the small state's resistance to Republican dominance that persisted longer than in most states",
            "His death in office contributed to the Federalist succession crisis in Delaware — the challenge of maintaining party organization as the Federalist Party declined nationally",
            "His Senate service contributed to the historical record of Federalist opposition during the Jefferson years — the minority dissent that documented constitutional concerns about Republican policies"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Delaware Senator 1801–1809"},
            {"target": "thomas-jefferson", "verb": "OPPOSES", "note": "Federalist opponent of Jefferson administration"},
            {"target": "louisiana-purchase", "verb": "OPPOSES", "note": "Voted against Louisiana Purchase"},
            {"target": "federalist-party", "verb": "MEMBER_OF", "note": "Delaware Federalist senator"},
            {"target": "delaware", "verb": "REPRESENTS", "note": "Senator from the nation's smallest reliably Federalist state"}
        ]
    }),

    ("andrew-butler", {
        "summary": (
            "Andrew Pickens Butler (1796–1857) was an American Democratic politician "
            "and jurist from South Carolina who served as U.S. Senator (1846–1857) "
            "and was one of the most prominent proslavery advocates in the antebellum "
            "Senate. He is most famous as the target of Senator Charles Sumner's "
            "'The Crime Against Kansas' speech (1856), in which Sumner denounced him "
            "in highly personal terms — an assault that contributed to the caning of "
            "Sumner by Butler's cousin, Representative Preston Brooks, on the Senate floor.\n\n"
            "Butler was a leading defender of slavery's expansion and Southern rights — "
            "a co-author of the Kansas-Nebraska Act alongside Stephen Douglas, and an "
            "ardent opponent of any federal restriction on slavery. His Senate career "
            "spanned the most explosive decade of the sectional crisis.\n\n"
            "The Sumner-Brooks caning incident became a defining polarizing event of "
            "the 1856 sectional crisis — galvanizing both proslavery and antislavery sentiment.\n\n"
            "He was a Camden South Carolina lawyer and judge."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "South Carolina Democratic Senator (1846–1857) and proslavery advocate; co-author of the Kansas-Nebraska Act; target of Sumner's 'Crime Against Kansas' speech (1856); his cousin Preston Brooks caned Sumner on the Senate floor — a defining polarizing event of the sectional crisis; Camden lawyer and judge.",
            "significanceCategory": "continental"
        },
        "causes": [
            "South Carolina's proslavery ideology — the state's radical defense of slavery as a positive good and its resistance to any federal restriction — created the political environment that made Butler a leading champion of Southern rights",
            "The Kansas-Nebraska Act's passage — the 1854 legislation that reopened the question of slavery's expansion into the territories and that Butler co-authored — created the flashpoint that led to 'Bleeding Kansas' and Sumner's attack",
            "The sectional crisis's intensification — the decade of escalating conflict over slavery that made the Senate chamber itself a site of violent confrontation — created the environment in which the Sumner-Brooks caning could occur"
        ],
        "effects": [
            "The Sumner-Brooks caning contributed to sectional polarization — galvanizing Northern antislavery opinion against Southern 'Slave Power' violence and rallying Southern opinion around Southern honor",
            "His Kansas-Nebraska Act co-authorship contributed to the destruction of the Second Party System — the legislation that broke the Whig Party and accelerated the formation of the Republican Party",
            "His proslavery Senate career contributed to South Carolina's radical secession ideology — the political tradition that culminated in South Carolina's first-state secession in 1860",
            "The Sumner assault contributed to the radicalization of both sections — the single event that most graphically illustrated the breakdown of civil political discourse in the antebellum Senate"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "South Carolina Senator 1846–1857"},
            {"target": "kansas-nebraska-act", "verb": "CO_AUTHORS", "note": "Co-author of the 1854 Kansas-Nebraska Act"},
            {"target": "charles-sumner", "verb": "ATTACKED_BY", "note": "Target of Sumner's 'Crime Against Kansas' speech 1856"},
            {"target": "preston-brooks", "verb": "DEFENDED_BY", "note": "Cousin who caned Sumner on the Senate floor"},
            {"target": "proslavery-movement", "verb": "CHAMPIONS", "note": "Leading proslavery advocate and Southern rights defender"}
        ]
    }),

    ("john-fairfield", {
        "summary": (
            "John Fairfield (1797–1847) was an American Democratic politician from Maine "
            "who served as U.S. Representative (1835–1838), Governor of Maine (1838–1843), "
            "and U.S. Senator (1843–1847). His career was shaped by the most dangerous "
            "Anglo-American border crisis of the antebellum era — the Aroostook War "
            "(1838–1839), a bloodless conflict over the disputed Maine-New Brunswick "
            "boundary that brought the United States and Britain to the brink of war. "
            "As governor, Fairfield dispatched state militia to assert Maine's claim to "
            "the Aroostook Valley — making him a central figure in the confrontation that "
            "Congress responded to by authorizing 50,000 troops.\n\n"
            "The Webster-Ashburton Treaty (1842) resolved the boundary dispute, giving "
            "Maine much of what it claimed. Fairfield's aggressive defense of Maine's "
            "territorial claims was popular domestically.\n\n"
            "He died in office as Senator in 1847, at the height of his political career.\n\n"
            "He was a Saco Maine lawyer who rose from obscurity to three major offices."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Maine Democratic Governor (1838–1843), Congressman (1835–1838), and Senator (1843–1847); central figure in the Aroostook War (1838–1839) — the bloodless Anglo-American border crisis; dispatched militia to assert Maine's territorial claim; his confrontation preceded the Webster-Ashburton Treaty (1842); died in office as Senator.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Maine-New Brunswick boundary dispute — the unresolved colonial-era boundary between Maine and British New Brunswick that left ownership of the valuable Aroostook Valley timber lands contested — created the territorial conflict that defined Fairfield's governorship",
            "Maine's demographic and economic growth — the state's rapid development creating population pressure on its northern boundary regions and demand for the timber lands in the disputed territory — created the urgency of Maine's territorial claim",
            "Anglo-American tensions of the 1830s — the broader diplomatic friction between Britain and the United States over Canadian boundary issues, the Caroline Affair, and other incidents — created the volatile context in which the Aroostook conflict could escalate dangerously"
        ],
        "effects": [
            "His aggressive assertion of Maine's territorial claims contributed to the Webster-Ashburton Treaty negotiations — the diplomatic resolution that gave Maine much of the disputed Aroostook territory",
            "The Aroostook crisis contributed to Anglo-American boundary diplomacy — the Webster-Ashburton Treaty that resolved multiple disputed boundaries and established an era of improved relations",
            "His governorship contributed to Maine's political culture — the assertive defense of state territorial rights that resonated with Maine voters",
            "His Senate career contributed Maine's Democratic perspective to the critical antebellum decade — the years of the Mexican War and the intensifying slavery debate"
        ],
        "relationships": [
            {"target": "maine", "verb": "GOVERNS", "note": "Governor of Maine 1838–1843"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Maine Congressman 1835–1838"},
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Maine Senator 1843–1847"},
            {"target": "aroostook-war", "verb": "LEADS_DURING", "note": "Governor who dispatched militia in the 1838–1839 border crisis"},
            {"target": "webster-ashburton-treaty", "verb": "PRECEDES", "note": "His confrontation drove the boundary negotiations"}
        ]
    }),

    ("william-leigh-brent", {
        "summary": (
            "William Leigh Brent (1784–1848) was an American Democratic-Republican "
            "politician from Louisiana who served in the U.S. House (1823–1829). "
            "Louisiana's congressional delegation in this era was among the most "
            "colorful in the Union — the state's unique French Creole culture, its "
            "civil law tradition inherited from France and Spain, its large free Black "
            "population, and its plantation economy creating a distinctive society "
            "that distinguished it from all other American states. Brent represented "
            "this complex Creole-planter society during the Era of Good Feelings and "
            "the early years of the Jacksonian transformation.\n\n"
            "Louisiana's transition from Creole-dominated to Anglo-American-dominated "
            "politics in the 1820s–1830s created the tensions that shaped Brent's "
            "political career — the contest between the old French-Spanish Creole elite "
            "and the incoming American settlers.\n\n"
            "He was a St. Martinville Louisiana lawyer representing the Creole tradition.\n\n"
            "He contributed to Louisiana's early congressional representation."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Louisiana Democratic-Republican Congressman (1823–1829); represented Louisiana's unique French Creole culture and civil law tradition in Congress; served during the Era of Good Feelings transition to Jacksonian politics; St. Martinville lawyer representing the Creole-planter society.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Louisiana's unique Creole culture — the French-Spanish colonial heritage that gave Louisiana distinctive laws, language, and social structures — created the society Brent represented in Congress",
            "Louisiana statehood (1812) and its early congressional representation — the need to navigate between the Creole elite and incoming American settlers — created the political challenge of Louisiana's early congressional delegation",
            "The Era of Good Feelings political fluidity — the period of weakened party competition and personal political networks — created the environment in which Brent built his congressional career"
        ],
        "effects": [
            "His congressional service contributed Louisiana's Creole perspective to Congress — the representation of the state's distinctive civil law and cultural traditions in national deliberations",
            "His career contributed to Louisiana's early partisan history — the transition from Creole-dominated Democratic-Republican politics toward the Jacksonian party system",
            "His St. Martinville base contributed to the documentation of Cajun Country's political representation in the early republic",
            "His congressional career contributed to Louisiana's gradual integration into American national politics while preserving elements of its distinctive Creole identity"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Louisiana Congressman 1823–1829"},
            {"target": "louisiana", "verb": "REPRESENTS", "note": "Congressman from the Creole-culture state"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "Era of Good Feelings Democratic-Republican"},
            {"target": "louisiana-creole-culture", "verb": "REPRESENTS", "note": "Lawyer from the French-Spanish Creole tradition"},
            {"target": "jacksonian-era", "verb": "SERVES_DURING", "note": "Congressional career during the Jacksonian transition"}
        ]
    }),

    ("benjamin-w-leigh", {
        "summary": (
            "Benjamin Watkins Leigh (1781–1849) was an American Whig politician and "
            "lawyer from Virginia who served as U.S. Senator (1834–1836) and was one "
            "of Virginia's most eminent constitutional lawyers. He was a staunch "
            "states' rights conservative — opposing Andrew Jackson's nationalism, "
            "the Force Bill during the nullification crisis, and any expansion of "
            "federal power over the states. Virginia's constitutional tradition, "
            "which traced its roots to Jefferson and Madison, made it the intellectual "
            "heartland of states' rights theory, and Leigh was among its most "
            "sophisticated exponents.\n\n"
            "He represented Virginia at the 1829–1830 Virginia Constitutional Convention — "
            "the gathering that debated reforming Virginia's colonial-era constitution "
            "in light of the democratic pressures of the Jacksonian age.\n\n"
            "He resigned from the Senate in 1836 in protest of Virginia's legislative "
            "instructions directing him to vote for the Benton expunging resolution "
            "— refusing to yield his senatorial independence.\n\n"
            "He was a Richmond Virginia lawyer of the first rank."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Virginia Whig Senator (1834–1836) and eminent constitutional lawyer; states' rights conservative opposing Force Bill and Jacksonian nationalism; delegate to the 1829–1830 Virginia Constitutional Convention; resigned from Senate over legislative instruction to vote for Benton expunging resolution; Richmond lawyer of the first rank.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Virginia's states' rights constitutional tradition — the state's deep commitment to limited federal power rooted in Jefferson and Madison's compact theory of the Constitution — created the intellectual environment for Leigh's constitutional conservatism",
            "The nullification crisis — South Carolina's assertion that states could nullify federal law, and Jackson's Force Bill response — created the constitutional confrontation that defined Leigh's Senate years",
            "The Virginia Constitutional Convention of 1829–1830 — the effort to reform Virginia's colonial-era franchise and representation — created the platform for Leigh's constitutional expertise"
        ],
        "effects": [
            "His Senate opposition to the Force Bill contributed to Virginia's states' rights tradition — the consistent opposition to federal coercion that shaped Virginia's political identity",
            "His resignation over legislative instructions contributed to the debate over senatorial independence — the constitutional question of whether senators must follow state legislative instructions",
            "His 1829–1830 Convention service contributed to Virginia's constitutional development — the unsuccessful effort to modernize Virginia's franchise that persisted as a grievance",
            "His constitutional scholarship contributed to the development of American states' rights theory — the rigorous legal arguments for state sovereignty against federal expansion"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Virginia Senator 1834–1836"},
            {"target": "nullification-crisis", "verb": "OPPOSES_RESPONSE_TO", "note": "Opponent of the Force Bill during nullification crisis"},
            {"target": "andrew-jackson", "verb": "OPPOSES", "note": "States' rights opponent of Jacksonian nationalism"},
            {"target": "virginia-constitutional-convention-1829", "verb": "ATTENDS", "note": "Delegate to the 1829–1830 Virginia Convention"},
            {"target": "states-rights-movement", "verb": "CHAMPIONS", "note": "Virginia's most sophisticated states' rights constitutional lawyer"}
        ]
    }),

    ("david-brydie-mitchell", {
        "summary": (
            "David Brydie Mitchell (1766–1837) was an American Democratic-Republican "
            "politician from Georgia who served as Governor of Georgia (1809–1813 and "
            "1815–1817) — twice — and as U.S. Representative (1793–1795). His two "
            "governorships bracketed the War of 1812, during which Georgia faced "
            "Creek and Seminole threats on its southern frontier. After leaving the "
            "governorship he served as Agent to the Creek Nation (1817–1821) — a "
            "federal appointment to manage relations with the Creek people whose "
            "lands Georgia coveted.\n\n"
            "His tenure as Creek Agent was controversial — he was accused of "
            "complicity in the illegal slave trade, smuggling enslaved Africans "
            "through Creek territory in violation of the 1807 slave trade prohibition. "
            "He was removed from office in 1821.\n\n"
            "Georgia's frontier politics in this era were shaped by land hunger, "
            "the Creek and Seminole wars, and the relentless pressure for Indian removal.\n\n"
            "He was a Savannah Georgia lawyer who became one of the state's dominant politicians."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Georgia Governor twice (1809–1813, 1815–1817) and Congressman; Agent to the Creek Nation (1817–1821); governorships during the War of 1812 and Creek frontier conflicts; removed as Creek Agent for alleged complicity in illegal slave trade; Savannah lawyer and dominant Georgia politician.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Georgia's frontier land hunger — the relentless pressure from Georgia settlers for Creek and Seminole lands on the state's southern frontier — created the political dynamic that shaped Mitchell's governorships and his Creek Agent appointment",
            "The War of 1812's southern theater — the Creek War and British-allied Seminole raids that threatened Georgia's frontier — created the military crises Mitchell managed as governor",
            "The 1807 slave trade prohibition — the federal ban on importing enslaved Africans — created the illegal traffic that Mitchell was accused of facilitating as Creek Agent, illustrating the contradiction between law and Georgia's labor demands"
        ],
        "effects": [
            "His two governorships contributed to Georgia's defense during the War of 1812 and the Creek conflicts — the executive management of frontier military emergencies",
            "His Creek Agent service contributed to the federal-Creek relationship in the critical decade before the Indian Removal Act — the years when Georgia's land pressure was most intense",
            "His removal for slave trade violations contributed to the documentation of illegal slave trade activity in the Lower South — the enforcement failure that allowed continued smuggling despite the 1807 prohibition",
            "His career contributed to Georgia's political history as a dominant figure across three decades of state politics"
        ],
        "relationships": [
            {"target": "georgia", "verb": "GOVERNS", "note": "Governor of Georgia 1809–1813 and 1815–1817"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Georgia Congressman 1793–1795"},
            {"target": "creek-nation", "verb": "SERVES_AS_AGENT_TO", "note": "U.S. Agent to the Creek Nation 1817–1821"},
            {"target": "war-of-1812", "verb": "GOVERNS_DURING", "note": "Governor during War of 1812 southern theater"},
            {"target": "transatlantic-slave-trade", "verb": "IMPLICATED_IN", "note": "Removed as Creek Agent for alleged illegal slave trade complicity"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 89 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich(slug, data)
    print("Done.")
