#!/usr/bin/env python3
"""
Batch 93 — 8 entities: Jacob Collamer, Noël du Fail, Abraham B. Venable,
Peleg Sprague, Elisha D. Cullen, Paul François Jean Nicolas Vicomte de Barras,
Elijah Paine, Honoré Muraire
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

    ("jacob-collamer", {
        "summary": (
            "Jacob Collamer (1791–1865) was an American Whig and Republican politician "
            "from Vermont who served as U.S. Representative (1843–1849), Postmaster "
            "General (1849–1850), and U.S. Senator (1855–1865). A Woodstock Vermont "
            "lawyer and jurist, Collamer's career bridged the Whig era through the "
            "founding of the Republican Party — he was one of the anti-slavery Whigs "
            "who helped create the Republican coalition in the 1850s. His Senate "
            "career coincided with the crisis decade leading to the Civil War: "
            "the Kansas-Nebraska Act, the Dred Scott decision, John Brown's raid, "
            "and Lincoln's election. Vermont's deep antislavery culture made Collamer "
            "one of the most consistent antislavery voices in the Senate.\n\n"
            "As Postmaster General under Zachary Taylor, he served briefly during "
            "the Compromise of 1850 controversy before the Taylor administration's "
            "sudden end.\n\n"
            "He was one of the founding Republican senators whose decade of service "
            "covered the Civil War's outbreak and early years.\n\n"
            "He was Vermont's most experienced antebellum senator."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Vermont Whig/Republican congressman, Postmaster General under Taylor, and Senator (1855–1865); antislavery Whig who helped found the Republican Party; Senate career through Kansas-Nebraska, Dred Scott, John Brown, and the Civil War; Woodstock Vermont lawyer and jurist; Vermont's most experienced antebellum senator.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Vermont's antislavery culture — the state's deep abolitionist tradition and Whig moral reform politics — created the political base for Collamer's antislavery career",
            "The Whig Party's collapse — the party's disintegration over the Kansas-Nebraska Act — created the political transition that Collamer navigated into the Republican Party",
            "The sectional crisis — the Kansas-Nebraska Act, the Dred Scott decision, and the growing conflict over slavery's expansion — created the defining political issues of Collamer's Senate years"
        ],
        "effects": [
            "His Senate career contributed Vermont's consistent antislavery voice to the Republican caucus through the Civil War's opening years",
            "His transition from Whig to Republican contributed to the founding coalition of the Republican Party — the antislavery Whigs who gave the new party its moral authority",
            "His Postmaster General tenure contributed to the Taylor administration's brief governance during the Compromise of 1850 crisis",
            "His long Senate career contributed to Vermont's representation during the most consequential decade in American history"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Vermont Senator 1855–1865"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Vermont Congressman 1843–1849"},
            {"target": "us-postmaster-general", "verb": "SERVES_AS", "note": "Postmaster General under Zachary Taylor 1849–1850"},
            {"target": "republican-party-united-states", "verb": "FOUNDS", "note": "Anti-slavery Whig co-founder of the Republican Party"},
            {"target": "zachary-taylor", "verb": "SERVES_UNDER", "note": "Cabinet member in Taylor administration"}
        ]
    }),

    ("noël-du-fail", {
        "summary": (
            "Noël du Fail (c.1520–1591) was a French lawyer, magistrate, and "
            "Renaissance author whose humorous prose works depicting Breton rural "
            "life were among the earliest examples of French regionalist literature. "
            "His 'Propos rustiques' (1547) and 'Baliverneries d'Eutrapel' (1548) "
            "captured the dialects, customs, and daily life of Breton peasants with "
            "an affectionate realism unusual for Renaissance literature. Du Fail "
            "served as a counselor in the Parlement de Bretagne — the supreme "
            "judicial court of the Duchy of Brittany — combining a distinguished "
            "legal career with his literary production.\n\n"
            "His writing predates and anticipates the broader French interest in "
            "regional vernacular culture that would become significant in the "
            "following century.\n\n"
            "He was a Breton lawyer-writer who gave the peasantry a literary voice.\n\n"
            "He is considered the first great writer of French regionalist literature."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "French Renaissance lawyer-author whose 'Propos rustiques' (1547) pioneered French regionalist literature depicting Breton rural life; Parlement de Bretagne counselor; earliest sympathetic literary portrayal of French peasant vernacular culture; considered the founding figure of French regionalist prose.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The French Renaissance's humanism — the movement's broadened interest in everyday life and vernacular language that expanded literary subject matter beyond classical and courtly themes — created the intellectual climate for du Fail's rural realism",
            "Brittany's distinctive culture — the duchy's Celtic heritage, separate legal traditions, and Breton language — created the rich regional material that du Fail drew on as a Breton magistrate-writer",
            "The expansion of French prose — the 16th century's development of French as a literary language capable of expressing everyday life — created the medium for du Fail's vernacular rural writing"
        ],
        "effects": [
            "His 'Propos rustiques' contributed to French regionalist literary tradition — the pioneering sympathetic depiction of rural peasant life that influenced later French realism",
            "His legal-literary career contributed to the tradition of French lawyer-writers — the magistrate-authors who combined judicial service with humanist literary production",
            "His Breton subject matter contributed to the preservation of 16th-century Breton rural culture — the documentary record of customs, dialects, and daily life that would otherwise be largely lost",
            "His Renaissance prose style contributed to the development of French vernacular literature — the expansion of prose's range to include everyday subject matter"
        ],
        "relationships": [
            {"target": "parlement-de-bretagne", "verb": "SERVES_IN", "note": "Counselor in the supreme Breton court"},
            {"target": "french-renaissance-literature", "verb": "PARTICIPATES_IN", "note": "Renaissance lawyer-author"},
            {"target": "propos-rustiques", "verb": "AUTHORS", "note": "Author of pioneering 1547 regionalist prose"},
            {"target": "brittany", "verb": "DEPICTS", "note": "Breton regional life and culture in his works"},
            {"target": "french-vernacular-literature", "verb": "ADVANCES", "note": "Early French prose depictions of rural vernacular life"}
        ]
    }),

    ("abraham-b-venable", {
        "summary": (
            "Abraham Bedford Venable (1758–1811) was an American Democratic-Republican "
            "politician from Virginia and North Carolina who served in the U.S. House "
            "(1791–1799) and then in the Virginia state legislature. A Virginia-born "
            "lawyer who moved to Prince Edward County, Venable was a Jeffersonian "
            "Republican in the early Congress — serving during the establishment of "
            "the federal government, the Hamilton financial program debates, the Jay "
            "Treaty controversy, and the XYZ Affair. Virginia's Republican politicians "
            "of this era were the most consistent opponents of Hamilton's centralizing "
            "fiscal vision.\n\n"
            "He was a planter-lawyer whose eight years in Congress covered the "
            "entire formative period of the federal government's first two terms.\n\n"
            "He later served as president of the Bank of Virginia — a significant "
            "post-congressional role in Virginia's financial institutions.\n\n"
            "He represented the Virginia Republican opposition to Hamiltonian Federalism."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Virginia Democratic-Republican Congressman (1791–1799) during the formative Federalist era; opposed Hamilton's financial program and Jay Treaty; later President of the Bank of Virginia; Prince Edward County planter-lawyer; represented Virginia's foundational Republican opposition to Hamiltonian Federalism.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Virginia's Republican political culture — the state's deep Jeffersonian tradition and opposition to Hamilton's centralizing fiscal program — created the political base for Venable's eight-year congressional career",
            "The Hamilton financial program debates — the fights over the national bank, assumption of state debts, and excise taxes — created the defining issues of Venable's early congressional years",
            "Virginia's planter-lawyer class — the network of landed families and trained lawyers who dominated the state's politics — provided the social basis for Venable's political career"
        ],
        "effects": [
            "His eight-year House service contributed Virginia's Republican opposition to the Hamilton financial program — the consistent votes against Federalist fiscal centralization",
            "His Bank of Virginia presidency contributed to Virginia's financial institutions — the post-congressional role combining financial and political influence",
            "His career contributed to the documentation of Virginia's founding Republican opposition — the early Congressional resistance that shaped Jeffersonian politics",
            "His Prince Edward County base contributed to the documentation of Virginia's Piedmont political culture in the founding era"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Virginia Congressman 1791–1799"},
            {"target": "alexander-hamilton", "verb": "OPPOSES", "note": "Republican opponent of Hamilton's financial program"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "Jeffersonian Virginia Republican"},
            {"target": "bank-of-virginia", "verb": "LEADS", "note": "Post-congressional President of the Bank of Virginia"},
            {"target": "virginia", "verb": "REPRESENTS", "note": "Prince Edward County planter-lawyer"}
        ]
    }),

    ("peleg-sprague", {
        "summary": (
            "Peleg Sprague (1793–1880) was an American politician and jurist from "
            "Maine who served as U.S. Representative (1825–1829), U.S. Senator "
            "(1829–1835), and then as a federal judge for the District of "
            "Massachusetts (1841–1865) with particular authority over admiralty "
            "and maritime law. His judicial career was the most significant part "
            "of his public service — he became one of the leading American "
            "admiralty judges of the 19th century, his decisions shaping maritime "
            "law during the era of rapid expansion of American shipping and commerce.\n\n"
            "His Senate years covered the height of the Jacksonian era — the Bank "
            "War, nullification crisis, and the transformation of American party "
            "politics from the Era of Good Feelings fusion to sharp Jacksonian "
            "confrontation.\n\n"
            "He was a Maine National Republican and then Whig — anti-Jackson "
            "throughout his political career.\n\n"
            "He was the defining figure of 19th-century American admiralty law."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Maine National Republican/Whig congressman and senator (1825–1835); District of Massachusetts federal judge (1841–1865) specializing in admiralty and maritime law; anti-Jacksonian senator during Bank War and nullification crisis; one of the leading 19th-century American admiralty judges.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Maine's separation from Massachusetts — the new state's 1820 independence creating its own congressional delegation — created the political opportunities for Sprague's career",
            "American maritime commerce expansion — the growth of shipping, whaling, and trade that made admiralty law increasingly important — created the judicial expertise that defined Sprague's long judicial career",
            "The anti-Jackson National Republican coalition — the political opposition to Jacksonian democracy — created Sprague's partisan alignment throughout his congressional years"
        ],
        "effects": [
            "His admiralty decisions contributed to American maritime law — the foundational jurisprudence that governed shipping, insurance, and maritime commerce for decades",
            "His Senate service contributed Maine's anti-Jackson perspective to the Bank War and nullification debates",
            "His long federal judicial career contributed to the federal judiciary's development of specialized admiralty expertise",
            "His combined congressional and judicial career contributed to Maine's political documentation — the state's representation in both legislative and judicial branches"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Maine Senator 1829–1835"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Maine Congressman 1825–1829"},
            {"target": "district-of-massachusetts", "verb": "SERVES_AS_JUDGE_OF", "note": "Federal district judge 1841–1865 — admiralty specialist"},
            {"target": "andrew-jackson", "verb": "OPPOSES", "note": "Anti-Jacksonian National Republican"},
            {"target": "american-admiralty-law", "verb": "SHAPES", "note": "Leading 19th-century admiralty law jurist"}
        ]
    }),

    ("elisha-d-cullen", {
        "summary": (
            "Elisha Dickerson Cullen (1799–1862) was an American Whig politician "
            "from Delaware who served in the U.S. House (1851–1855) during the "
            "most explosive years of the antebellum sectional crisis. Delaware's "
            "unique position — a slave state that remained in the Union throughout "
            "the Civil War and had an unusually small enslaved population by southern "
            "standards — gave its representatives a distinctive perspective on "
            "the slavery debates. Cullen's Whig term coincided with the aftermath "
            "of the Compromise of 1850 and the beginnings of the Kansas-Nebraska "
            "debate that would shatter the Whig Party.\n\n"
            "Delaware's commercial ties to Philadelphia and its border-state "
            "status made its Whig politicians particularly sensitive to the "
            "sectional tensions that the slavery debate was generating.\n\n"
            "He was a Georgetown Delaware lawyer and politician.\n\n"
            "He represented Delaware's complex border-state Whig political culture."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Delaware Whig Congressman (1851–1855) during the Compromise of 1850 aftermath and pre-Kansas-Nebraska crisis; Delaware's border-state Whig perspective; Georgetown Delaware lawyer; served during the Kansas-Nebraska debate that shattered the Whig Party; Delaware's unique status as a slave state with commercial ties to Philadelphia.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Delaware's border-state Whig culture — the state's unique position as a slave state with strong commercial ties to Philadelphia and the North — created the political environment for Cullen's moderate Whig career",
            "The Compromise of 1850 — the sectional compromise over California statehood and the Fugitive Slave Act — created the political context of Cullen's congressional years",
            "The Whig Party's internal tensions — the slavery debate's mounting pressure on the Whig coalition that would ultimately destroy the party — created the environment of Cullen's brief term"
        ],
        "effects": [
            "His congressional service contributed Delaware's border-state Whig perspective to the sectional debates of 1851–1855",
            "His career contributed to the documentation of Delaware's complex political culture — the slave state that remained pro-Union",
            "His Whig service contributed to the party's final years — the last Whig congressmen elected before the party's 1854 collapse",
            "His Georgetown Delaware base contributed to the documentation of Delaware's rural legal community in the antebellum period"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Delaware Congressman 1851–1855"},
            {"target": "delaware", "verb": "REPRESENTS", "note": "Georgetown Delaware Whig lawyer-politician"},
            {"target": "compromise-of-1850", "verb": "SERVES_DURING", "note": "Congressman during the sectional compromise aftermath"},
            {"target": "whig-party-united-states", "verb": "MEMBER_OF", "note": "Delaware Whig in the party's final years"},
            {"target": "kansas-nebraska-act", "verb": "SERVES_BEFORE", "note": "Congressional term ended just before the Whig-shattering Act"}
        ]
    }),

    ("paul-français-jean-nicolas-vicomte-de-barras", {
        "summary": (
            "Paul François Jean Nicolas, Vicomte de Barras (1755–1829) was a "
            "French Revolutionary politician who became the dominant figure of "
            "the Directory period (1795–1799) — effectively the most powerful "
            "man in France for four years. A Provençal nobleman who embraced "
            "the Revolution, Barras participated in Thermidor (the coup against "
            "Robespierre in July 1794), helped end the Terror, and then as one "
            "of five Directors controlled the government that tried to stabilize "
            "France between the Terror and Napoleon. He was notorious for his "
            "personal corruption, his flamboyant lifestyle, and his patronage — "
            "he introduced Napoleon Bonaparte to Joséphine de Beauharnais and "
            "was instrumental in Bonaparte's early military career.\n\n"
            "Napoleon's coup of 18 Brumaire (November 1799) ended the Directory "
            "and forced Barras into permanent retirement — the man who had been "
            "France's dominant politician for years ended as a pensioned exile.\n\n"
            "He was the quintessential figure of the corrupt, cynical Directory.\n\n"
            "'Power is always for sale — the question is the price.'"
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Dominant figure of the French Directory (1795–1799) — effectively France's most powerful man for four years; Thermidor coup participant who ended the Terror; introduced Napoleon to Joséphine; patronized Napoleon's early career; overthrown by Napoleon's 18 Brumaire coup; epitome of the corrupt, cynical Directory.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The French Revolution's radicalisation — the escalating violence of the Terror that alienated moderate revolutionaries — created the conditions for the Thermidor coup that Barras helped lead",
            "The Directory's institutional weakness — the five-man executive's structural vulnerabilities, the ongoing war with European coalitions, and France's economic exhaustion — created the political instability that Barras dominated through manipulation rather than principle",
            "Napoleon Bonaparte's ambition — the young Corsican general's military brilliance and political determination — created the force that ultimately overthrew Barras and the Directory at 18 Brumaire"
        ],
        "effects": [
            "His Thermidor participation contributed to ending the Terror — the coup that removed Robespierre and halted the guillotine's mass executions",
            "His Directory leadership contributed to France's post-Terror political stabilization — the corrupt but functional regime that held France together through four years of constitutional crisis",
            "His patronage of Napoleon contributed directly to one of history's most consequential careers — the military and romantic connections that launched Bonaparte's path to power",
            "His overthrow by Napoleon's 18 Brumaire coup contributed to the Directory's historical legacy as a failed experiment in republican governance"
        ],
        "relationships": [
            {"target": "french-directory", "verb": "LEADS", "note": "Dominant Director 1795–1799"},
            {"target": "thermidor-coup", "verb": "PARTICIPATES_IN", "note": "Co-led coup against Robespierre July 1794"},
            {"target": "napoleon-bonaparte", "verb": "PATRONIZES", "note": "Introduced Napoleon to Joséphine; patronized early career"},
            {"target": "reign-of-terror", "verb": "ENDS", "note": "Thermidor coup ended the Terror"},
            {"target": "coup-of-18-brumaire", "verb": "OVERTHROWN_BY", "note": "Napoleon's 1799 coup forced Barras into exile"}
        ]
    }),

    ("elijah-paine", {
        "summary": (
            "Elijah Paine (1757–1842) was an American Federalist politician and "
            "jurist from Vermont who served as U.S. Senator (1795–1801) and as "
            "a U.S. District Judge for the District of Vermont (1801–1842) — "
            "one of the longest-serving federal judges in early American history. "
            "His Senate years coincided with the Adams administration — the period "
            "of the Alien and Sedition Acts, the XYZ Affair, and the political "
            "crisis that ended with Jefferson's electoral victory in 1800. "
            "As a Federalist senator Paine was on the losing side of the 1800 "
            "revolution, but his judicial appointment — a midnight judge "
            "appointment before Adams left office — gave him four decades of "
            "continued federal service.\n\n"
            "His forty-one years on the Vermont federal bench made him one "
            "of the most significant figures in Vermont's early federal judiciary.\n\n"
            "He was a Royalton Vermont lawyer whose combined senatorial and "
            "judicial career spanned nearly fifty years of public service.\n\n"
            "He was Vermont's longest-serving early federal judge."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Vermont Federalist Senator (1795–1801) and District Judge (1801–1842) — forty-one years on the Vermont federal bench; Adams midnight judge appointment; Senate years during XYZ Affair and Alien and Sedition Acts; Royalton Vermont lawyer with nearly fifty years of combined public service.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Vermont's Federalist political culture — the state's initial Federalist orientation in the 1790s — created the political base for Paine's Senate election",
            "The Adams administration's midnight judge appointments — the Federalist strategy of filling judicial vacancies before Jefferson's inauguration — created the judicial appointment that gave Paine his four-decade bench career",
            "Vermont's federal judiciary needs — the district court requiring experienced jurists for a rapidly growing state — created the institutional demand that Paine's long tenure filled"
        ],
        "effects": [
            "His forty-one-year Vermont judicial career contributed to the development of Vermont's federal jurisprudence — the foundational decades of the district court's operation",
            "His midnight judge status contributed to the political controversy over the Adams administration's final judicial appointments",
            "His Senate service contributed Vermont's Federalist perspective to the Adams administration's political battles",
            "His combined career contributed to Vermont's political and judicial history — the documentation of the state's founding federal institutions"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Vermont Senator 1795–1801"},
            {"target": "us-district-court-vermont", "verb": "SERVES_AS_JUDGE_OF", "note": "District Judge 1801–1842 — forty-one years"},
            {"target": "john-adams", "verb": "APPOINTED_BY", "note": "Midnight judge appointment by Adams before 1801"},
            {"target": "federalist-party", "verb": "MEMBER_OF", "note": "Vermont Federalist senator"},
            {"target": "alien-and-sedition-acts", "verb": "SUPPORTS_DURING", "note": "Federalist senator during the Adams administration crisis"}
        ]
    }),

    ("honoré-muraire", {
        "summary": (
            "Honoré Muraire (1750–1837) was a French jurist, magistrate, and "
            "Napoleonic statesman who served as First President of the Cour de "
            "cassation (France's supreme court) and was ennobled by Napoleon "
            "as Comte Muraire. A lawyer from Provence who survived the "
            "Revolution despite his legal career under the Old Regime, Muraire "
            "rose through the Revolutionary and Napoleonic judicial systems "
            "to reach the highest judicial position in France. The Cour de "
            "cassation — established by the Revolutionary government — was "
            "France's supreme court for civil and criminal appeals, and its "
            "First President held the most prestigious judicial office in the "
            "French legal system.\n\n"
            "He was a quintessential example of the lawyer-jurist who navigated "
            "the Old Regime, Revolution, and Empire — surviving each transformation "
            "and rising in each.\n\n"
            "He was a Napoleonic imperial count from the legal nobility.\n\n"
            "He was one of the founding figures of modern French judicial institutions."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "First President of the Cour de cassation — France's supreme court — and Napoleonic Comte; Provençal lawyer who survived Revolution and rose through Napoleonic judicial system; one of the founding figures of modern French judicial institutions; exemplified the jurist-administrator who thrived across Old Regime, Revolution, and Empire.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The French Revolutionary judicial reform — the abolition of the Old Regime parlements and establishment of new courts including the Cour de cassation — created the institutional framework through which Muraire rose",
            "Napoleon's judicial consolidation — the Empire's establishment of a hierarchical judicial system with the Cour de cassation at its apex — created the supreme court position that Muraire eventually held",
            "The jurist-administrator tradition — the skilled lawyers who served successively under Old Regime, Republic, and Empire without apparent political contradiction — created the career path that Muraire exemplified"
        ],
        "effects": [
            "His Cour de cassation presidency contributed to the development of French supreme court jurisprudence — the foundational decisions that shaped modern French civil and criminal law",
            "His Napoleonic ennoblement contributed to the Empire's judicial nobility — the legal aristocracy that served as an arm of imperial governance",
            "His career contributed to the documentary record of French legal continuity through revolution — the survival of professional legal culture across catastrophic political change",
            "His Provençal background contributed to the integration of southern French legal traditions into the national judicial system"
        ],
        "relationships": [
            {"target": "cour-de-cassation", "verb": "LEADS_AS_FIRST_PRESIDENT", "note": "First President of France's supreme court"},
            {"target": "napoleon-bonaparte", "verb": "ENNOBLED_BY", "note": "Created Comte Muraire by Napoleon"},
            {"target": "french-empire", "verb": "SERVES_IN", "note": "Napoleonic judicial system's highest position"},
            {"target": "french-revolution", "verb": "SURVIVES", "note": "Old Regime lawyer who survived the Revolution"},
            {"target": "french-judicial-system", "verb": "SHAPES", "note": "Founding figure of modern French judicial institutions"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 93 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich(slug, data)
    print("Done.")
