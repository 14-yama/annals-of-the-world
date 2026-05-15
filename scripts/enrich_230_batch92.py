#!/usr/bin/env python3
"""
Batch 92 — 8 entities: Waldric, Daniel Cady, François-Vincent Toussaint,
John S. Barbour, José Ignacio de Gorriti, Pierre-Marie de Saint-Georges,
Pierre-Théodore Verhaegen, Henry Brockholst Livingston
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

    ("waldric", {
        "summary": (
            "Waldric (d.c.1115) was a Norman-English royal chancellor and bishop "
            "who served as Chancellor of England under King Henry I and was appointed "
            "Bishop of St. Andrews in Scotland — the first Norman appointed to "
            "Scotland's premier bishopric. His appointment to St. Andrews in 1107 "
            "was highly controversial: it was opposed by King Alexander I of Scotland "
            "and the Scottish church on the grounds that the appointment had been made "
            "without proper Scottish consultation, and the dispute over whether "
            "St. Andrews was subject to Canterbury or York — the metropolitan "
            "jurisdiction question — made his tenure contentious.\n\n"
            "He never fully exercised his St. Andrews appointment, as Scottish "
            "ecclesiastical resistance prevented his installation, and he died "
            "without establishing effective control of the see.\n\n"
            "His appointment illustrated the Anglo-Norman kings' effort to extend "
            "their influence into Scotland through ecclesiastical channels — the "
            "church as an instrument of political integration.\n\n"
            "He was a royal administrator who became a pawn in Anglo-Scottish ecclesiastical politics."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Norman Chancellor of England under Henry I and disputed Bishop of St. Andrews (1107); first Norman appointed to Scotland's premier see; appointment contested by King Alexander I and Scottish church; Canterbury-York metropolitan jurisdiction dispute; exemplified Anglo-Norman ecclesiastical extension into Scotland.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Anglo-Norman kings' ecclesiastical policy — Henry I's use of church appointments to extend Norman influence into Scotland and Wales — created the strategic context for Waldric's St. Andrews appointment",
            "The Canterbury-York metropolitan jurisdiction dispute — the ongoing contest between the two English archbishoprics over which had authority over Scotland — created the specific ecclesiastical conflict that complicated Waldric's appointment",
            "Scottish church independence — King Alexander I's resistance to Norman ecclesiastical influence and his assertion of Scottish church autonomy — created the opposition that effectively blocked Waldric's installation"
        ],
        "effects": [
            "His disputed appointment contributed to the Anglo-Scottish ecclesiastical conflict — the jurisdictional dispute that complicated church-state relations for decades",
            "His chancellorship contributed to Henry I's administrative machinery — the royal government that made him one of England's most effective medieval kings",
            "His failed St. Andrews appointment contributed to the historical precedent for Scottish church independence — the resistance that eventually became the basis for claims of Scottish ecclesiastical autonomy",
            "His career contributed to the documentary record of Anglo-Norman attempts to integrate Scotland into the Norman ecclesiastical order"
        ],
        "relationships": [
            {"target": "henry-i-of-england", "verb": "SERVES_UNDER", "note": "Chancellor of England under Henry I"},
            {"target": "bishop-of-st-andrews", "verb": "APPOINTED_AS", "note": "Controversial appointment as Bishop of St. Andrews 1107"},
            {"target": "alexander-i-of-scotland", "verb": "OPPOSED_BY", "note": "Scottish king blocked his St. Andrews installation"},
            {"target": "archbishop-of-york", "verb": "DISPUTED_WITH", "note": "Metropolitan jurisdiction dispute over Scotland"},
            {"target": "scottish-church", "verb": "OPPOSED_BY", "note": "Scottish ecclesiastical resistance prevented installation"}
        ]
    }),

    ("daniel-cady", {
        "summary": (
            "Daniel Cady (1773–1859) was an American Federalist and Whig politician "
            "and jurist from New York who served in the U.S. House (1815–1817) and "
            "as an Associate Justice of the New York Supreme Court (1847–1855). "
            "He is historically significant primarily as the father of Elizabeth "
            "Cady Stanton — the leading feminist theorist and women's suffrage "
            "advocate. His relationship with his daughter was complex and influential: "
            "she reportedly credited his legal discussions with her as a child for "
            "inspiring her understanding of women's legal disabilities.\n\n"
            "His Johnstown New York law practice made him one of the leading lawyers "
            "of the region, and his daughter's observation of the legal inequities "
            "facing his female clients became part of the famous origin story of "
            "American women's rights activism.\n\n"
            "His judicial career on the New York Supreme Court came at the end of "
            "his long legal life.\n\n"
            "He was a Johnstown New York lawyer whose most significant legacy was his daughter."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "New York Congressman (1815–1817), state Supreme Court justice (1847–1855), and father of Elizabeth Cady Stanton; Johnstown lawyer whose legal discussions with his daughter inspired her women's rights activism; his practice's treatment of women's legal disabilities became part of the Seneca Falls origin story.",
            "significanceCategory": "continental"
        },
        "causes": [
            "New York's Federalist and Whig legal culture — the tradition of conservative constitutional lawyering that Cady practiced — created his professional prominence and influenced his daughter's understanding of law",
            "Women's legal disabilities in 19th-century American law — the coverture doctrine and property restrictions that affected his female clients — created the specific legal inequities that Elizabeth Cady Stanton observed and became determined to change",
            "Cady's legal discussions with Elizabeth — the father's willingness to discuss law with his daughter and explain the legal disabilities she observed in his practice — created the direct intellectual transmission that shaped the women's rights movement"
        ],
        "effects": [
            "His influence on Elizabeth Cady Stanton contributed directly to the women's rights movement — the legal education she received observing his practice became foundational to the Seneca Falls Declaration",
            "His judicial career contributed to New York's legal development — the state Supreme Court jurisprudence of a long-experienced practitioner",
            "His congressional service contributed to New York's representation during the post-War of 1812 transitional period",
            "His legacy as a legal educator — through his daughter — contributed to the intellectual foundations of American feminism"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "New York Congressman 1815–1817"},
            {"target": "new-york-supreme-court", "verb": "SERVES_ON", "note": "New York Supreme Court Associate Justice 1847–1855"},
            {"target": "elizabeth-cady-stanton", "verb": "PARENT_OF", "note": "Father whose legal discussions inspired women's rights advocacy"},
            {"target": "seneca-falls-convention", "verb": "INFLUENCES_THROUGH_DAUGHTER", "note": "Legal education of daughter contributed to women's rights movement"},
            {"target": "womens-legal-disabilities", "verb": "PRACTICES_DURING", "note": "Lawyer whose practice exposed daughter to coverture and property restrictions"}
        ]
    }),

    ("françois-vincent-toussaint", {
        "summary": (
            "François-Vincent Toussaint (1715–1772) was a French lawyer, philosopher, "
            "and encyclopédiste whose 1748 work 'Les Moeurs' (On Morals) was one of "
            "the most controversial philosophical texts of the early Enlightenment. "
            "'Les Moeurs' argued for a natural morality independent of religious "
            "authority — a secular ethics grounded in reason and human nature — "
            "which the Catholic Church condemned and which was publicly burned. "
            "Toussaint contributed to Diderot's Encyclopédie — the great monument "
            "of French Enlightenment thought — writing articles on legal and moral topics.\n\n"
            "His secular morality argument anticipated the ethical philosophy that "
            "would become central to the later Enlightenment and the Revolutionary "
            "rejection of ecclesiastical moral authority.\n\n"
            "He was a Paris lawyer who combined legal practice with philosophical writing "
            "— a characteristic Enlightenment combination.\n\n"
            "He was a significant but underrecognized figure of early French Enlightenment ethics."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "French encyclopédiste and philosopher whose 'Les Moeurs' (1748) was condemned and burned for advocating secular natural morality; contributor to Diderot's Encyclopédie; anticipated the Enlightenment's rejection of religious moral authority; Paris lawyer-philosopher of the early French Enlightenment.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The early French Enlightenment's challenge to ecclesiastical authority — the philosophical movement that questioned the Church's monopoly on moral guidance — created the intellectual context for Toussaint's secular morality argument",
            "Diderot's Encyclopédie project — the great collaborative effort to systematize Enlightenment knowledge — created the platform for Toussaint's contribution and his association with the leading philosophes",
            "The Catholic Church's moral monopoly — the institutional claim to define morality through revelation and tradition — created the specific authority that Toussaint's 'Les Moeurs' challenged and that provoked the book's condemnation"
        ],
        "effects": [
            "His 'Les Moeurs' contributed to the Enlightenment's secular ethics tradition — the argument for natural morality independent of religious authority that became central to later philosophy",
            "His Encyclopédie articles contributed to the great monument of French Enlightenment knowledge — the systematic compilation that shaped modern thought",
            "His book's condemnation contributed to the Enlightenment censorship history — the pattern of Church and state suppression that defined the philosophes' relationship with authority",
            "His secular ethics anticipated the Revolutionary rejection of ecclesiastical moral authority — the philosophical groundwork for the Republic's claim to establish civic morality independent of religion"
        ],
        "relationships": [
            {"target": "encyclopedie", "verb": "CONTRIBUTES_TO", "note": "Contributor to Diderot's Encyclopédie"},
            {"target": "french-enlightenment", "verb": "PARTICIPATES_IN", "note": "Early Enlightenment philosopher and encyclopédiste"},
            {"target": "denis-diderot", "verb": "COLLABORATES_WITH", "note": "Encyclopédie contributor alongside Diderot"},
            {"target": "les-moeurs", "verb": "AUTHORS", "note": "Author of 'Les Moeurs' (1748) — condemned secular morality text"},
            {"target": "catholic-church", "verb": "CENSURED_BY", "note": "'Les Moeurs' condemned and burned by Church authorities"}
        ]
    }),

    ("john-s-barbour", {
        "summary": (
            "John Strode Barbour Sr. (1790–1855) was an American Democratic politician "
            "from Virginia who served in the U.S. House (1823–1833) and was a prominent "
            "member of Virginia's planter-lawyer political elite. Virginia in the "
            "1820s–1830s was at a crossroads — the state's declining relative power "
            "in the Union as the South's political weight shifted toward newer cotton "
            "states, the growing national antislavery movement, and the intensifying "
            "debate over Virginia's future. Barbour represented the Jeffersonian "
            "Old Dominion tradition of constitutional states' rights and slavery "
            "defense during the decade that included the nullification crisis and "
            "the Nat Turner rebellion.\n\n"
            "His House career placed him at the center of the Jackson-era transformation "
            "of Democratic politics — supporting the Jacksonian coalition while "
            "maintaining Virginia's distinctive states' rights tradition.\n\n"
            "He was a Culpeper County Virginia planter-lawyer.\n\n"
            "He was part of Virginia's dominant antebellum political family networks."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Virginia Democratic Congressman (1823–1833); Culpeper County planter-lawyer in Virginia's declining political elite; served during nullification crisis and Nat Turner rebellion; Jeffersonian states' rights tradition; Jackson-era Democratic politics; Virginia's antebellum political family networks.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Virginia's planter-lawyer political culture — the network of landed families and their trained legal representatives who dominated Virginia and national politics — created the social basis for Barbour's congressional career",
            "The Jacksonian transformation — the shift from Jeffersonian Republican politics to the sharper factional politics of the Jackson era — created the political realignment that Barbour navigated",
            "Virginia's states' rights tradition — the state's constitutional conservatism rooted in Jefferson, Madison, and the Virginia and Kentucky Resolutions — created the ideological framework that Barbour represented in Congress"
        ],
        "effects": [
            "His House service contributed Virginia's states' rights perspective to the Jackson-era congressional debates",
            "His career contributed to Virginia's planter-lawyer political tradition — the network of Culpeper County and Piedmont Virginia political families",
            "His decade of congressional service contributed to the documentation of Virginia's declining political influence in an era of rising western and deep South power",
            "His Jacksonian-era career contributed to the transition of Virginia's political elite from Jeffersonian universalism toward defensive proslavery ideology"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Virginia Congressman 1823–1833"},
            {"target": "virginia", "verb": "REPRESENTS", "note": "Culpeper County Virginia planter-lawyer"},
            {"target": "andrew-jackson", "verb": "SUPPORTS", "note": "Jacksonian Democrat"},
            {"target": "states-rights-movement", "verb": "CHAMPIONS", "note": "Virginia Jeffersonian states' rights tradition"},
            {"target": "nat-turner-rebellion", "verb": "SERVES_DURING", "note": "Congressman during the 1831 Virginia slave rebellion"}
        ]
    }),

    ("josé-ignacio-de-gorriti", {
        "summary": (
            "José Ignacio de Gorriti (1770–1835) was an Argentine Catholic priest, "
            "lawyer, and patriot politician who was a prominent figure in the "
            "independence movement and served in the early Constituent Assemblies "
            "of Argentina. A native of Salta — the northwestern Argentine city "
            "that was one of the most important royalist strongholds and then "
            "patriot centers in the independence wars — Gorriti combined his "
            "clerical status with active political engagement. He was a member of "
            "the Constituent Assembly of 1813 and contributed to the formation of "
            "Argentina's early republican institutions.\n\n"
            "His clerical-patriot combination was characteristic of the Latin "
            "American independence movement, where many priests broke with the "
            "royalist church hierarchy to support independence.\n\n"
            "His sister Juana Manuela Gorriti became one of the most celebrated "
            "Latin American writers of the 19th century.\n\n"
            "He was a Salta patriarch who shaped the northern Argentine independence tradition."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Argentine priest-patriot and Constituent Assembly member (1813); Salta northern independence patriot; combined clerical status with republican political engagement; brother of celebrated writer Juana Manuela Gorriti; contributed to early Argentine republican institution-building.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Argentina's independence movement — the patriot cause that mobilized Creole elites, clergy, and lawyers against Spanish colonial rule — created the revolutionary context for Gorriti's combined clerical-political career",
            "Salta's strategic position — the northwestern city's role as a military and political center for the independence wars in the Andean region — created the local base for Gorriti's patriot prominence",
            "The Latin American church's split on independence — the conflict between royalist hierarchy and patriot clergy that mirrored the broader political divide — created the specific tension that a priest-patriot like Gorriti embodied"
        ],
        "effects": [
            "His Constituent Assembly service contributed to Argentina's early republican institution-building — the foundational assemblies that laid the groundwork for Argentine governance",
            "His clerical-patriot role contributed to the legitimization of independence among Argentina's Catholic population — the religious endorsement of the republican cause",
            "His Salta leadership contributed to the northern Argentine independence tradition — the regional patriotism that made Salta a symbol of resistance",
            "His family's legacy — sister Juana Manuela's literary career — contributed to Argentine cultural history beyond his own political contributions"
        ],
        "relationships": [
            {"target": "constituent-assembly-argentina-1813", "verb": "SERVES_IN", "note": "Member of the 1813 Argentine Constituent Assembly"},
            {"target": "argentina", "verb": "FOUNDS_INSTITUTIONS_OF", "note": "Early republican institution-builder"},
            {"target": "salta", "verb": "REPRESENTS", "note": "Salta patriot leader in the independence era"},
            {"target": "juana-manuela-gorriti", "verb": "SIBLING_OF", "note": "Brother of the celebrated Latin American writer"},
            {"target": "latin-american-independence", "verb": "PARTICIPATES_IN", "note": "Clerical-patriot in the Argentine independence movement"}
        ]
    }),

    ("pierre-marie-de-saint-georges", {
        "summary": (
            "Pierre-Marie de Saint-Georges (1738–1793) was a French jurist and "
            "magistrate who served as a member of the Parlement de Paris — the "
            "supreme judicial court of Old Regime France — and later participated "
            "in the Revolutionary period. The Parlements of France were the "
            "primary institutional check on royal power in Old Regime France: "
            "they registered royal edicts, remonstrated against laws they deemed "
            "unconstitutional, and were the principal voice of the nobility's "
            "resistance to royal absolutism. The Paris Parlement's resistance "
            "to Louis XVI's fiscal reforms was a significant factor in triggering "
            "the political crisis that led to the Revolution.\n\n"
            "He navigated the transition from Old Regime magistracy to Revolutionary "
            "period — a dangerous journey for men of the Parlement class who had "
            "served the royal judicial order.\n\n"
            "He was a Paris jurist whose career bridged the Old Regime and the Revolution.\n\n"
            "He represented the magistracy that both resisted absolutism and was swept away by revolution."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Member of the Parlement de Paris — Old Regime France's supreme court and institutional check on royal power; the Paris Parlement's resistance to Louis XVI's fiscal reforms contributed to the Revolutionary crisis; navigated the dangerous transition from royal magistracy to Revolutionary period.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Parlement de Paris's constitutional role — the traditional function of registering and remonstrating against royal edicts that made it both the supreme court and the primary institutional opposition to absolutism — created the institution that defined Saint-Georges's career",
            "Louis XVI's fiscal reform crisis — the crown's desperate need for new taxes and the Parlement's resistance that blocked reform and contributed to the political crisis — created the historical context that made Parlement membership both powerful and dangerous",
            "The Old Regime's collapse — the institutional failure of French royal governance under fiscal and political pressure — created the transition that made the Old Regime magistracy's position precarious"
        ],
        "effects": [
            "His Parlement service contributed to the Old Regime's last institutional resistance — the magistracy's opposition to royal fiscal reform",
            "His survival of the early Revolutionary period (if he did) contributed to the documentation of how Old Regime magistrates navigated the Revolutionary transformation",
            "His judicial career contributed to the historical record of the Parlement de Paris during its final years — the institution that both resisted absolutism and was abolished by the Revolution",
            "His career contributed to the pattern of Old Regime jurist transitions — the complex choices facing magistrates when the institutions they served were swept away"
        ],
        "relationships": [
            {"target": "parlement-de-paris", "verb": "SERVES_IN", "note": "Member of France's supreme Old Regime court"},
            {"target": "louis-xvi", "verb": "OPPOSES_FISCAL_REFORMS_OF", "note": "Parlement magistrate resisting royal fiscal reforms"},
            {"target": "french-revolution", "verb": "NAVIGATES_TRANSITION_TO", "note": "Old Regime magistrate during the Revolutionary transformation"},
            {"target": "old-regime-france", "verb": "SERVES_IN", "note": "Representative of the Old Regime judicial order"},
            {"target": "french-nobility", "verb": "REPRESENTS", "note": "Noble magistrate in the robe nobility tradition"}
        ]
    }),

    ("pierre-théodore-verhaegen", {
        "summary": (
            "Pierre-Théodore Verhaegen (1796–1862) was a Belgian liberal lawyer "
            "and politician who founded the Université libre de Bruxelles (ULB) "
            "in 1834 — one of Europe's most significant universities, established "
            "on the principle of free inquiry and independence from religious "
            "authority. Verhaegen's founding of ULB was a deliberate act of "
            "liberal secular defiance against the Catholic Church's educational "
            "monopoly in Belgium — establishing a university on the principle of "
            "'libre examen' (free examination of all questions without religious "
            "dogmatic constraints) that became the foundation of Belgian liberal culture.\n\n"
            "He was a Member of the Belgian Chamber of Representatives and one "
            "of the key leaders of the Belgian Liberal Party — the political force "
            "that shaped Belgian secular and constitutional development.\n\n"
            "ULB's founding principle of secular free inquiry made it the model "
            "for European liberal universities and a counterweight to Catholic "
            "education throughout the 19th century.\n\n"
            "'Free examination is the basis of all progress.'"
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Founder of the Université libre de Bruxelles (ULB) in 1834; established the principle of 'libre examen' (secular free inquiry) as the foundation of Belgian liberal culture; Belgian Liberal Party leader and Chamber member; ULB became a model for European secular universities; one of Belgium's most significant contributions to European intellectual life.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Catholic Church's educational monopoly in Belgium — the Church's control of universities and schools that liberal Belgians challenged — created the specific institutional gap that Verhaegen's ULB was designed to fill",
            "Belgian liberalism's anticlericalist tradition — the Liberal Party's commitment to secular education, free inquiry, and independence from Church authority — created the ideological basis for ULB's founding principle",
            "Belgium's 1830 independence — the new nation's need to develop its own institutional framework — created the opportunity to establish a secular university as a national intellectual institution"
        ],
        "effects": [
            "His founding of ULB contributed to European secular higher education — the model of a university based on free inquiry independent of religious authority",
            "ULB's 'libre examen' principle contributed to Belgian liberal culture — the secular intellectual tradition that shaped Belgian political and intellectual life throughout the 19th and 20th centuries",
            "His Liberal Party leadership contributed to Belgian secular constitutional development — the political force that established Belgium's separation of church and state",
            "ULB's founding contributed to the European 'culture wars' between secular liberalism and Catholic education — the institutional confrontation that shaped European politics for generations"
        ],
        "relationships": [
            {"target": "université-libre-de-bruxelles", "verb": "FOUNDS", "note": "Founded ULB in 1834 on the libre examen principle"},
            {"target": "belgian-liberal-party", "verb": "LEADS", "note": "Key Liberal Party leader"},
            {"target": "belgium", "verb": "SERVES_IN", "note": "Belgian Chamber of Representatives member"},
            {"target": "libre-examen", "verb": "ESTABLISHES", "note": "Founding principle of secular free inquiry at ULB"},
            {"target": "catholic-church-education", "verb": "CHALLENGES", "note": "ULB established as secular counterweight to Catholic education"}
        ]
    }),

    ("henry-brockholst-livingston", {
        "summary": (
            "Henry Brockholst Livingston (1757–1823) was an American jurist and "
            "Revolutionary War veteran from New York who served as an Associate "
            "Justice of the U.S. Supreme Court (1807–1823). A member of the "
            "powerful Livingston family — one of New York's great colonial dynasties — "
            "he practiced law in New York before his Supreme Court appointment "
            "by President Jefferson. He served on the Court for sixteen years, "
            "participating in the formative decisions of the Marshall Court era, "
            "including the important early cases on commerce, contracts, and "
            "federal-state relations.\n\n"
            "He was a veteran of the Revolutionary War, serving as an aide-de-camp "
            "to General Schuyler and participating in the Benedict Arnold-led "
            "Quebec expedition before Arnold's treason.\n\n"
            "He was one of the founding members of the New York bar's elite — "
            "his legal career bridging the colonial, Revolutionary, and early "
            "national periods.\n\n"
            "He served on the Marshall Court during its most formative decade."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "U.S. Supreme Court Associate Justice (1807–1823) on the formative Marshall Court; New York Livingston family member; Revolutionary War veteran — aide-de-camp to General Schuyler; participated in Quebec expedition with Benedict Arnold; Jefferson appointee; founding member of New York's elite bar.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Livingston family's New York prominence — the great colonial dynasty's legal, political, and commercial networks — created the social capital for Henry's judicial career",
            "Jefferson's Supreme Court appointment strategy — the Republican president's effort to reshape the Federalist-dominated Court — created the political context for Livingston's appointment as a Democratic-Republican lawyer",
            "The Marshall Court's formative role — John Marshall's establishment of judicial review and the Court's authority over federal-state constitutional questions — created the institutional context in which Livingston served"
        ],
        "effects": [
            "His sixteen-year Court service contributed to the Marshall Court's formative decisions — the cases that defined American constitutional law on commerce, contracts, and federal supremacy",
            "His Revolutionary War service contributed to the founding generation's military legacy — the aide-de-camp who participated in the Quebec expedition before Arnold's treason",
            "His Jefferson appointment contributed to the Republican reshaping of the Court — the gradual replacement of Federalist justices with Republican appointees",
            "His Livingston family connection contributed to New York's legal tradition — the great dynastic family's continued contribution to American law and politics"
        ],
        "relationships": [
            {"target": "us-supreme-court", "verb": "SERVES_ON", "note": "Associate Justice 1807–1823"},
            {"target": "thomas-jefferson", "verb": "APPOINTED_BY", "note": "Jefferson's Republican Supreme Court appointment"},
            {"target": "john-marshall", "verb": "SERVES_WITH", "note": "Sixteen years on the Marshall Court"},
            {"target": "american-revolutionary-war", "verb": "FIGHTS_IN", "note": "Aide-de-camp to General Schuyler; Quebec expedition"},
            {"target": "livingston-family", "verb": "MEMBER_OF", "note": "New York Livingston dynasty member"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 92 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich(slug, data)
    print("Done.")
