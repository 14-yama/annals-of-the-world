#!/usr/bin/env python3
"""
Batch 97 — 8 entities: John Pope, Paine Wingate, Francisco Javier Mina,
Thomas Butler King, David Stewart, Theodore Frelinghuysen,
Thorkild Fjeldsted, William H. Wells
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

    ("john-pope", {
        "summary": (
            "John Pope (1770–1845) was an American Democratic-Republican and "
            "Democratic politician from Kentucky who served as U.S. Senator "
            "(1807–1813) and as Governor of Arkansas Territory (1829–1835). "
            "His Senate years coincided with the War of 1812's political "
            "buildup — the congressional debates over trade restrictions, "
            "impressment, and the mounting confrontation with Britain that "
            "the War Hawks were pushing toward war. Pope was from Kentucky — "
            "the western state whose frontier spirit and British-allied Indian "
            "raids made it one of the most pro-war regions in the nation.\n\n"
            "His Arkansas territorial governorship came later — the period "
            "of Arkansas's development as a territory before its 1836 "
            "statehood. Arkansas in this era was a frontier cotton territory "
            "whose economy and society were being shaped by the rapid "
            "expansion of plantation slavery.\n\n"
            "He was a Springfield Kentucky lawyer who held major offices "
            "in two different states and territories.\n\n"
            "He was a Kentucky frontier Democrat who governed an Arkansas frontier territory."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Kentucky Democratic-Republican Senator (1807–1813) and Governor of Arkansas Territory (1829–1835); Senate years during War of 1812 buildup; Arkansas territorial governor during pre-statehood cotton expansion; Springfield Kentucky lawyer with offices in two different states and territories.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Kentucky's frontier political culture — the western state's pro-war sentiment, fear of British-allied Indian raids, and Jeffersonian agrarian democracy — created the political environment for Pope's Senate career",
            "Arkansas Territory's frontier development — the rapid settlement and plantation expansion in the pre-statehood territory — created the administrative challenges Pope faced as territorial governor",
            "The War of 1812's political buildup — the years of trade restrictions, impressment, and the War Hawks' congressional advocacy — created the defining issue of Pope's Senate years"
        ],
        "effects": [
            "His Senate service contributed Kentucky's western pro-war perspective to the War of 1812 debates",
            "His Arkansas territorial governorship contributed to the territory's governance during its frontier development phase",
            "His career contributed to the documentation of frontier Democratic politics in two different western and southern territories",
            "His combined Senate and territorial career contributed to the historical record of the early republic's expansion into the Mississippi Valley and beyond"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Kentucky Senator 1807–1813"},
            {"target": "arkansas-territory", "verb": "GOVERNS", "note": "Governor of Arkansas Territory 1829–1835"},
            {"target": "war-of-1812", "verb": "SERVES_BEFORE", "note": "Senator during the War of 1812 buildup"},
            {"target": "kentucky", "verb": "REPRESENTS", "note": "Springfield Kentucky Democratic-Republican"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "Jeffersonian Kentucky Republican"}
        ]
    }),

    ("paine-wingate", {
        "summary": (
            "Paine Wingate (1739–1838) was an American Federalist politician "
            "and clergyman from New Hampshire who served in the First and Second "
            "Congresses (1789–1793) as both a Senator (1789–1793) and briefly "
            "as a Representative (1793). He was one of the original United States "
            "senators — serving in the very first Senate — and lived to ninety-nine, "
            "making him the longest-lived member of the First Congress. A "
            "Congregationalist minister before entering politics, Wingate "
            "brought a clerical perspective to the founding Senate.\n\n"
            "He served during the establishment of the federal government — "
            "the first Senate's foundational work on the Bill of Rights, the "
            "Judiciary Act of 1789, and the creation of the executive departments.\n\n"
            "He was a Stratham New Hampshire clergyman and farmer.\n\n"
            "His ninety-nine-year life spanned from the colonial era to the "
            "age of the Mexican War."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "New Hampshire Federalist original First Congress Senator (1789–1793); one of the first United States senators; Congregationalist minister; lived to ninety-nine — longest-lived First Congress member; served during Bill of Rights and Judiciary Act; Stratham New Hampshire clergyman-farmer.",
            "significanceCategory": "continental"
        },
        "causes": [
            "New Hampshire's Federalist political culture — the state's support for the new Constitution and its commercial and legal establishment — created the political context for Wingate's Senate election",
            "The First Congress's foundational moment — the establishment of the federal government's basic institutions — created the historical significance of Wingate's Senate years",
            "New Hampshire's Congregationalist religious culture — the tradition of clerical civic engagement — created the background for a minister's entry into politics"
        ],
        "effects": [
            "His First Congress Senate service contributed to the establishment of the federal government's foundational institutions",
            "His presence in the first Senate contributed to the historical record of the founding legislative generation",
            "His ninety-nine-year life contributed to the historical continuity — the living link between the founding era and the mid-19th century",
            "His clerical background contributed to the Congregationalist-civic tradition that shaped New England's public life"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "New Hampshire original First Congress Senator 1789–1793"},
            {"target": "first-congress", "verb": "SERVES_IN", "note": "One of the original United States senators"},
            {"target": "bill-of-rights", "verb": "SERVES_DURING_PASSAGE_OF", "note": "First Senate member during Bill of Rights adoption"},
            {"target": "federalist-party", "verb": "MEMBER_OF", "note": "New Hampshire Federalist politician"},
            {"target": "new-hampshire", "verb": "REPRESENTS", "note": "Stratham New Hampshire clergyman-farmer"}
        ]
    }),

    ("francisco-javier-mina", {
        "summary": (
            "Francisco Javier Mina (1789–1817) was a Spanish guerrilla fighter "
            "and liberal revolutionary whose extraordinary career took him from "
            "fighting Napoleon's French occupation of Spain (1808–1814) to "
            "leading a liberal insurgent expedition to Mexico to fight for "
            "independence (1816–1817). As a guerrilla leader in Navarre during "
            "the Peninsular War, Mina led one of the most effective resistance "
            "forces against Napoleon's occupation — his mobile tactics, his "
            "popular support, and his personal courage made him a hero of "
            "Spanish resistance. After Napoleon's defeat, he opposed the "
            "restoration of absolutism under Ferdinand VII and eventually "
            "joined the liberal cause in Mexico.\n\n"
            "He was captured and executed in Mexico at twenty-eight — a short "
            "life of extraordinary intensity that made him a hero in both "
            "Spain and Mexico.\n\n"
            "'For freedom and the constitution — I fight in two worlds.'\n\n"
            "He was the warrior who fought for liberalism on two continents."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Spanish guerrilla hero of the Peninsular War and liberal revolutionary who fought for Mexican independence; one of the most effective guerrilla leaders against Napoleon's occupation of Spain (1808–1814); executed in Mexico at twenty-eight after a liberalist expedition; hero of both Spanish resistance and Mexican independence movements.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Napoleon's French occupation of Spain — the Peninsular War that created the conditions for guerrilla resistance — created the military context for Mina's extraordinary career as a Navarrese guerrilla leader",
            "Ferdinand VII's restoration of absolutism — the Spanish king's repudiation of the liberal constitution of 1812 after Napoleon's defeat — created the political reason for Mina's turn from Spanish patriot to liberal exile and revolutionary",
            "Mexico's independence movement — the ongoing insurgency against Spanish colonial rule — created the cause that Mina joined, leading an expedition to the new world"
        ],
        "effects": [
            "His Peninsular War guerrilla leadership contributed to Napoleon's defeat in Spain — the effective resistance that drained French resources and morale",
            "His Mexican expedition contributed to the independence movement's international dimension — the European liberal who crossed the Atlantic to fight for colonial liberation",
            "His execution contributed to his martyrdom — making him a symbolic hero for both Spanish liberals and Mexican patriots",
            "His career contributed to the liberal internationalism of the early 19th century — the idea that the fight for constitutional government was a universal cause transcending national boundaries"
        ],
        "relationships": [
            {"target": "peninsular-war", "verb": "FIGHTS_IN", "note": "Guerrilla leader in Navarre against French occupation"},
            {"target": "napoleon-bonaparte", "verb": "RESISTS", "note": "Most effective Spanish guerrilla resistance commander"},
            {"target": "mexican-independence", "verb": "FIGHTS_FOR", "note": "Led liberal expedition to Mexico 1816–1817"},
            {"target": "ferdinand-vii", "verb": "OPPOSES", "note": "Opposed absolutist restoration after Napoleon's defeat"},
            {"target": "spanish-liberalism", "verb": "CHAMPIONS", "note": "Liberal constitutional cause in Spain and Mexico"}
        ]
    }),

    ("thomas-butler-king", {
        "summary": (
            "Thomas Butler King (1800–1864) was an American Whig and states' rights "
            "politician from Georgia who served in the U.S. House (1839–1843 and "
            "1845–1850) and played a key role in California's admission to the "
            "Union. In 1849 President Taylor sent King to California as a special "
            "agent — he helped organize California's constitutional convention "
            "and the process that led to California's 1850 statehood application. "
            "California's admission as a free state — one of the most explosive "
            "sectional issues of the era — was in part shaped by King's mission.\n\n"
            "He later served as a Confederate treasury official after Georgia's "
            "secession — his career illustrating the tragic path of the southern "
            "Whig who became a secessionist.\n\n"
            "He was a Brunswick Georgia Sea Islands planter.\n\n"
            "He was the man who helped bring California into the Union."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Georgia Whig congressman and Taylor administration agent who organized California's 1850 constitutional convention and statehood process; his California mission helped bring the free state into the Union, triggering the sectional Compromise of 1850; Brunswick Georgia Sea Islands planter who became a Confederate official; tragic path from Whig to secessionist.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The California Gold Rush — the 1848 discovery and the resulting mass migration that required rapid territorial organization — created the political urgency that led to King's California mission",
            "The slavery expansion crisis — the fundamental question of whether California would enter as a free or slave state — created the sectional stakes of King's California mission",
            "Taylor's California strategy — the Whig president's decision to skip the territorial phase and bring California directly to statehood — created the specific mission that King was sent to organize"
        ],
        "effects": [
            "His California mission contributed to California's constitutional convention and 1850 statehood — the organized process that admitted the state as free, triggering the Compromise of 1850",
            "California's free state admission contributed to the Compromise of 1850's sectional crisis — the Senate debates that produced the compromise package",
            "His later Confederate service contributed to the historical record of southern Whig secessionists — the men who broke from their Unionist tradition to join the Confederacy",
            "His career contributed to the documentation of the Zachary Taylor administration's California policy"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Georgia Congressman 1839–1843 and 1845–1850"},
            {"target": "zachary-taylor", "verb": "SERVES_AS_AGENT_FOR", "note": "Taylor's special agent to California 1849"},
            {"target": "california-statehood", "verb": "ORGANIZES", "note": "Helped organize California's constitutional convention and statehood"},
            {"target": "compromise-of-1850", "verb": "CONTRIBUTES_TO", "note": "California mission triggered the sectional Compromise"},
            {"target": "confederate-states-of-america", "verb": "SERVES_IN", "note": "Confederate treasury official after Georgia's secession"}
        ]
    }),

    ("david-stewart", {
        "summary": (
            "David Stewart (1800–1858) was an American Whig politician from "
            "Maryland who served briefly as U.S. Senator (1849–1850) — an "
            "appointment to fill a vacancy. Maryland's antebellum politics were "
            "competitive and often characterized by brief, appointment-based "
            "Senate tenures as the parties maneuvered for advantage. Stewart's "
            "brief Senate appointment came during the Compromise of 1850 debates — "
            "the most intense sectional crisis since Missouri, involving California "
            "statehood, the Fugitive Slave Act, and the Texas boundary.\n\n"
            "Maryland's border-state position — a slave state with strong ties "
            "to both North and South — made its senators particularly sensitive "
            "to the compromise politics that Whig Senator Henry Clay was "
            "orchestrating in Washington.\n\n"
            "He was a Baltimore merchant and businessman.\n\n"
            "He was a brief Maryland Whig senator during a critical national moment."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Maryland Whig Senator (1849–1850) — brief appointment during Compromise of 1850 debates; Baltimore merchant; border-state senator during the most intense sectional crisis since Missouri; Maryland's competitive antebellum politics; served during California statehood and Fugitive Slave Act debates.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Maryland's competitive antebellum politics — the state's two-party competition that produced frequent Senate vacancies and brief appointment-based tenures — created the context for Stewart's short Senate service",
            "The Compromise of 1850's political pressure — the sectional crisis that demanded border-state senators take positions on California, slavery, and fugitive slave enforcement — created the political environment of Stewart's brief tenure",
            "Maryland's border-state position — the slave state with strong commercial ties to Baltimore's northern trade — created the political sensitivities that shaped Stewart's brief senatorial role"
        ],
        "effects": [
            "His brief Senate service contributed to the historical record of Maryland's antebellum political appointments",
            "His border-state representation contributed Maryland's perspective to the Compromise of 1850 debates",
            "His Baltimore merchant background contributed to the documentation of commercial interests in Maryland's antebellum political class",
            "His brief tenure contributed to the pattern of Maryland's competitive Senate representation"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Maryland Senator 1849–1850 — brief appointment"},
            {"target": "compromise-of-1850", "verb": "SERVES_DURING", "note": "Senator during the sectional compromise debates"},
            {"target": "maryland", "verb": "REPRESENTS", "note": "Baltimore merchant politician"},
            {"target": "whig-party-united-states", "verb": "MEMBER_OF", "note": "Maryland Whig senator"},
            {"target": "fugitive-slave-act-1850", "verb": "SERVES_DURING_DEBATE_OF", "note": "Senator during the Fugitive Slave Act controversy"}
        ]
    }),

    ("theodore-frelinghuysen", {
        "summary": (
            "Theodore Frelinghuysen (1787–1862) was an American Whig politician, "
            "reformer, and evangelical Christian leader from New Jersey who served "
            "as U.S. Senator (1829–1835) and was the Whig vice presidential "
            "candidate in 1844. Known as 'The Christian Statesman,' Frelinghuysen "
            "was the era's most prominent evangelical Christian in national politics "
            "— a dedicated advocate for Sunday schools, Bible societies, "
            "temperance, and anti-Indian removal. His 1830 Senate speech opposing "
            "Jackson's Indian Removal Act was one of the most powerful moral "
            "arguments against the forced removal of the Cherokee and other "
            "southeastern tribes.\n\n"
            "He later served as President of Rutgers College (1850–1862) — "
            "continuing his lifelong commitment to education and religious "
            "moral reform.\n\n"
            "'The Christian Statesman' was Henry Clay's running mate in 1844.\n\n"
            "He was the conscience of Whig evangelical reform politics."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "New Jersey Whig Senator (1829–1835) and 1844 vice presidential candidate with Henry Clay; 'The Christian Statesman' — the most prominent evangelical Christian in national politics; powerful 1830 Senate speech opposing Jackson's Indian Removal Act; President of Rutgers College (1850–1862); leader of Sunday school, Bible society, and temperance movements.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Second Great Awakening — the evangelical Protestant revival that mobilized millions of Americans for moral reform causes — created the religious movement that Frelinghuysen led in the political sphere",
            "Jackson's Indian Removal Act — the forced removal of southeastern tribes that Frelinghuysen opposed on moral and constitutional grounds — created the defining Senate confrontation of his career",
            "The Whig Party's evangelical wing — the overlap between Whig anti-Jacksonian politics and evangelical moral reform — created the political alignment that made Frelinghuysen both a senator and a vice presidential candidate"
        ],
        "effects": [
            "His Indian Removal Act opposition contributed to the historical record of congressional resistance to Jackson's removal policy — the most powerful moral argument against the Cherokee removal",
            "His evangelical reform leadership contributed to the Bible society, Sunday school, and temperance movements — the institutional mobilization of Protestant reform",
            "His 1844 vice presidential candidacy contributed to the Whig Party's appeal to evangelical Protestant voters",
            "His Rutgers presidency contributed to higher education's evangelical tradition — the college president who embodied the union of Christian faith and learning"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "New Jersey Senator 1829–1835"},
            {"target": "indian-removal-act", "verb": "OPPOSES", "note": "Powerful Senate speech against forced removal 1830"},
            {"target": "henry-clay", "verb": "RUNS_WITH", "note": "Whig vice presidential candidate with Clay in 1844"},
            {"target": "rutgers-college", "verb": "LEADS_AS_PRESIDENT", "note": "President of Rutgers College 1850–1862"},
            {"target": "second-great-awakening", "verb": "LEADS_POLITICAL_EXPRESSION_OF", "note": "'The Christian Statesman' — evangelical reform leader"}
        ]
    }),

    ("thorkild-fjeldsted", {
        "summary": (
            "Thorkild Fjeldsted (1779–1853) was a Norwegian jurist and judge who "
            "served as a judge on the Norwegian Supreme Court (Høyesterett) in the "
            "decades following Norwegian independence in 1814. The Norwegian "
            "Constitution of 1814 — one of the most liberal constitutions of its "
            "era — established an independent judiciary including the Supreme Court "
            "as a cornerstone of the new constitutional order. Fjeldsted served "
            "on the court during the formative period when Norwegian constitutional "
            "jurisprudence was being established — the interpretation of the 1814 "
            "constitution's provisions and the definition of judicial independence "
            "within the new political system.\n\n"
            "Norway in this period was in union with Sweden under the Kiel Treaty "
            "while maintaining its own constitution — a dual status that created "
            "complex constitutional questions.\n\n"
            "He was a Danish-born jurist who served Norwegian constitutional institutions.\n\n"
            "He was a founding figure of Norwegian constitutional jurisprudence."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Norwegian Supreme Court (Høyesterett) judge during the formative post-1814 constitutional era; served during the establishment of Norwegian constitutional jurisprudence; Norwegian Constitution of 1814 — one of the most liberal of its era; Denmark-born jurist serving Norwegian institutions during Swedish union; founding figure of Norwegian judicial independence.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Norwegian Constitution of 1814 — one of the most liberal constitutions of its era, establishing judicial independence and the Supreme Court — created the institutional framework that Fjeldsted served",
            "Norwegian independence from Denmark (1814) — the political transformation that created a new Norwegian state — created the need for Norwegian judges to staff the new constitutional institutions",
            "The Swedish-Norwegian union's constitutional complexity — the dual status under the Kiel Treaty that required defining the boundaries of Norwegian judicial independence — created the constitutional questions that shaped Fjeldsted's jurisprudence"
        ],
        "effects": [
            "His Supreme Court service contributed to the development of Norwegian constitutional jurisprudence — the interpretation of the 1814 constitution's provisions",
            "His judicial career contributed to the establishment of Norwegian judicial independence — the institutional practice of an independent court in a new constitutional state",
            "His service contributed to the historical record of Norwegian constitutional development in the post-1814 era",
            "His Danish origin in Norwegian service contributed to the documentation of Scandinavian institutional transfers during the constitutional era"
        ],
        "relationships": [
            {"target": "norwegian-supreme-court", "verb": "SERVES_ON", "note": "Høyesterett judge in the post-1814 constitutional era"},
            {"target": "norwegian-constitution-1814", "verb": "INTERPRETS", "note": "Supreme Court judge interpreting the 1814 constitution"},
            {"target": "norway", "verb": "SERVES", "note": "Norwegian constitutional institution judge"},
            {"target": "sweden-norway-union", "verb": "SERVES_DURING", "note": "Judge during the Swedish-Norwegian personal union"},
            {"target": "norwegian-independence-1814", "verb": "SERVES_IN_AFTERMATH_OF", "note": "Founding era judge after Norwegian constitutional independence"}
        ]
    }),

    ("william-h-wells", {
        "summary": (
            "William Hill Wells (1769–1829) was an American Federalist politician "
            "from Delaware who served in the U.S. Senate (1799–1804 and 1813–1817). "
            "His two separate Senate tenures gave Delaware consistent Federalist "
            "representation through the Adams and Madison administrations. Delaware's "
            "small size made it a Federalist stronghold long after other states "
            "had shifted to Jeffersonian Republicanism — the state's commercial "
            "ties to Philadelphia and its small, tight-knit political elite "
            "sustained Federalist politics through the first decade of the "
            "19th century. His second Senate term covered the War of 1812's "
            "final years — the war that the Federalist Party had opposed.\n\n"
            "He was a Dagsboro Delaware lawyer and politician.\n\n"
            "He was one of the last Federalist senators from Delaware.\n\n"
            "He represented Delaware's Federalist durability in a Republican era."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Delaware Federalist Senator in two non-consecutive terms (1799–1804 and 1813–1817); Delaware's Federalist durability in a Republican era; Dagsboro lawyer; served through Adams and Madison administrations; second term during War of 1812's final years — the war the Federalists opposed; one of the last Federalist senators from Delaware.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Delaware's Federalist political durability — the small state's commercial elite's sustained commitment to Federalism long after most states had shifted to Republicanism — created the political base for Wells's two Senate terms",
            "Delaware's commercial ties to Philadelphia — the economic relationship that made Delaware's merchant class ideologically aligned with Federalist commercial policy — created the consistent support for Federalist senators",
            "The War of 1812's political polarization — the Federalist opposition to the war that Delaware's commercial elite shared — created the defining issue of Wells's second Senate term"
        ],
        "effects": [
            "His two Senate terms contributed to Delaware's consistent Federalist representation through the Adams and Madison eras",
            "His second term service contributed Delaware's Federalist opposition to the War of 1812",
            "His career contributed to the documentation of Delaware's unusually durable Federalism — the last stronghold of the party in the early 19th century",
            "His two non-consecutive terms contributed to the pattern of Delaware's small-state Senate representation"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Delaware Senator 1799–1804 and 1813–1817"},
            {"target": "federalist-party", "verb": "MEMBER_OF", "note": "Delaware Federalist politician — one of the last"},
            {"target": "delaware", "verb": "REPRESENTS", "note": "Dagsboro Delaware Federalist lawyer"},
            {"target": "war-of-1812", "verb": "OPPOSES", "note": "Federalist senator opposing the war in second term"},
            {"target": "john-adams", "verb": "SUPPORTS_ADMINISTRATION_OF", "note": "Federalist senator during Adams presidency"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 97 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich(slug, data)
    print("Done.")
