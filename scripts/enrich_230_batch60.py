#!/usr/bin/env python3
"""
Batch 60 — 8 entities: Charles-Jean-Baptiste Amyot, Samuel E. Smith,
Geoffrey Rufus, Samuel Dickinson Hubbard, Stephen Allen,
Anne du Bourg, Claude Bazin de Bezons, Guillaume van Volxem
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

    ("charles-jean-baptiste-amyot", {
        "summary": (
            "Charles-Jean-Baptiste Amyot (1747–1820) "
            "was a French jurist and official who "
            "served as a senior magistrate and "
            "legal administrator during the Ancien "
            "Régime, the Revolution, and the "
            "Napoleonic period. His career exemplified "
            "the continuity of France's professional "
            "legal class through the revolutionary "
            "transformation — trained jurists who "
            "maintained their institutional positions "
            "and expertise across the successive "
            "regimes that replaced each other "
            "between 1789 and 1815.\n\n"
            "Amyot was trained in law under the "
            "Ancien Régime's traditional legal "
            "education system — the royal courts, "
            "the parlements, and the legal culture "
            "of Old Regime France that the "
            "Revolution dismantled and replaced "
            "with a new rationalized legal system "
            "based on the Napoleonic Code.\n\n"
            "His survival through the Terror "
            "— unlike many of his juridical "
            "contemporaries who were caught in "
            "the political violence — allowed "
            "him to continue his legal career "
            "into the Napoleonic period, "
            "contributing to the new administrative "
            "and judicial institutions that "
            "Napoleon built on the Revolution's "
            "foundations.\n\n"
            "His career represented the crucial "
            "continuity function that trained "
            "lawyers provided — maintaining "
            "legal culture and institutional "
            "memory through transformative change."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "French jurist and legal administrator who maintained his career across the Ancien Régime, Revolution, and Napoleonic period; exemplified the continuity of France's professional legal class through revolutionary transformation; contributed to the administrative institutions of successive French regimes.",
            "significanceCategory": "local"
        },
        "causes": [
            "The Ancien Régime's system of legal education and the parlements' professional culture — training lawyers in the complex Roman-canonical jurisprudence of Old Regime France — formed Amyot's legal expertise and professional identity before the Revolution dismantled these institutions",
            "The Revolution's survival logic — which required trained legal professionals to staff the new administrative and judicial institutions — created the continuing demand for Amyot's expertise even as the old courts were abolished and replaced with the Revolutionary and Napoleonic legal systems",
            "Napoleon's deliberate use of trained Ancien Régime officials — retaining lawyers, administrators, and technical experts who had served the old regime but could make themselves useful to the new — gave careers like Amyot's a pathway through the revolutionary disruption into the Napoleonic administrative state"
        ],
        "effects": [
            "His legal career contributed to the administrative continuity that France required to function through the massive institutional disruptions of the Revolution — providing the trained personnel who staffed the new judicial institutions even as the old ones were abolished",
            "His Napoleonic-era service contributed to the development of the new administrative and judicial institutions — the prefectural system, the new courts, and the administrative culture that the Napoleonic Code required to function effectively",
            "His career illustrated the importance of the professional legal class in maintaining institutional continuity — demonstrating that trained lawyers' technical expertise made them valuable regardless of which political regime held power",
            "His survival through the Terror demonstrated the capacity of France's administrative professionals to navigate the most dangerous political environment of the era — using professional utility and political caution to avoid the fate of those judicial professionals who were too closely identified with the Ancien Régime"
        ],
        "relationships": [
            {"target": "ancien-regime-france", "verb": "TRAINED_UNDER", "note": "Legal professional formed in the Old Regime legal system"},
            {"target": "french-revolution", "verb": "SURVIVES", "note": "Jurist who maintained his career through the Terror"},
            {"target": "napoleonic-code", "verb": "APPLIES", "note": "Contributed to Napoleonic legal and administrative institutions"},
            {"target": "napoleonic-france", "verb": "SERVES_IN", "note": "Senior official in the Napoleonic administrative system"},
            {"target": "french-legal-continuity", "verb": "REPRESENTS", "note": "Embodied the professional legal class's cross-regime continuity"}
        ]
    }),

    ("samuel-e-smith", {
        "summary": (
            "Samuel Emerson Smith (1788–1860) was "
            "an American Democratic politician from "
            "Maine who served as Governor of Maine "
            "(1831–1834) and as a member of the U.S. "
            "House of Representatives (1821–1833). "
            "His political career spanned the "
            "transition from the Era of Good Feelings "
            "to Jacksonian Democracy — a devoted "
            "supporter of Andrew Jackson who aligned "
            "himself firmly with the new Democratic "
            "Party that Jackson's populist coalition "
            "was forging in the late 1820s.\n\n"
            "Smith was born in New Hampshire and "
            "settled in Maine — which had become "
            "a separate state in 1820 as part "
            "of the Missouri Compromise. His House "
            "service began immediately after Maine "
            "achieved statehood and coincided with "
            "the pivotal political realignment "
            "of the 1820s — the collapse of the "
            "Democratic-Republican Party into "
            "Adams and Jackson factions, the "
            "'corrupt bargain' election of 1824, "
            "and the emergence of the second "
            "American party system.\n\n"
            "His governorship of Maine (1831–1834) "
            "coincided with the opening of Jackson's "
            "second term — the Bank War, the nullification "
            "crisis, and the consolidation of "
            "Jacksonian Democracy as the dominant "
            "force in American politics.\n\n"
            "He represented Maine's emerging "
            "Jacksonian Democratic tradition."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Maine Democratic Governor (1831–1834) and Congressman (1821–1833); Jacksonian Democrat representing Maine's alignment with Jackson's populist coalition; served through the Bank War and nullification crisis; key figure in Maine's early statehood political development.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Maine's creation as a separate state in 1820 — as part of the Missouri Compromise's paired admission of Maine and Missouri — established the new political framework in which Smith built his congressional and gubernatorial career, beginning his House service in Maine's very first congressional election",
            "Andrew Jackson's political coalition and the 1824 'corrupt bargain' controversy — which galvanized Jacksonian Democrats across the country including Maine — provided the political identity around which Smith organized his governorship",
            "Jackson's second-term agenda — the Bank War's destruction of the Second Bank of the United States, the nullification crisis with South Carolina, and the Democratic Party's consolidation as the vehicle of populist politics — defined the major issues of Smith's gubernatorial tenure"
        ],
        "effects": [
            "His governorship managed Maine's affairs during the politically charged years of Jackson's presidency — maintaining Jacksonian Democratic governance in New England's most reliably Democratic state",
            "His long House tenure contributed to Maine's congressional representation during the state's first decade — building the political institutions and precedents of a newly independent state's federal relationship",
            "His career contributed to Maine's Democratic political tradition — helping establish the Jacksonian coalition in a state that became one of the Northeast's more reliably Democratic in the antebellum period",
            "His career illustrated the rapid political development of new American states — Maine's ability to generate experienced federal legislators and a governor within its first decade of statehood demonstrated the vitality of democratic institution-building on the American frontier"
        ],
        "relationships": [
            {"target": "maine", "verb": "GOVERNS", "note": "Governor of Maine 1831–1834"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Maine Representative 1821–1833"},
            {"target": "andrew-jackson", "verb": "SUPPORTS", "note": "Jacksonian Democrat and Jackson ally"},
            {"target": "bank-war", "verb": "GOVERNS_DURING", "note": "Governor during Jackson's Bank War"},
            {"target": "democratic-party-united-states", "verb": "MEMBER_OF", "note": "Founding Jacksonian Democrat in Maine"}
        ]
    }),

    ("geoffrey-rufus", {
        "summary": (
            "Geoffrey Rufus (died 1141) was a "
            "medieval English churchman and royal "
            "official who served as Lord Chancellor "
            "of England under Henry I and as "
            "Bishop of Durham (1133–1141). His "
            "career exemplified the dual role "
            "of senior churchman and royal administrator "
            "that characterized the Anglo-Norman "
            "ecclesiastical culture — men of learning "
            "and administrative ability who served "
            "simultaneously as royal ministers "
            "and as princes of the Church.\n\n"
            "Geoffrey was a royal clerk who rose "
            "through the administrative machinery "
            "of Henry I's government — one of "
            "the most effective administrative "
            "monarchies in medieval Europe. "
            "As Chancellor, he managed the royal "
            "writing office and served as one "
            "of the king's principal ministers, "
            "helping to produce the enormous "
            "volume of writs, charters, and "
            "administrative documents that "
            "Henry I's government generated.\n\n"
            "His reward was the wealthy and "
            "politically significant bishopric "
            "of Durham — the prince-bishopric "
            "whose bishop held exceptional "
            "palatine authority over the "
            "northeast of England as a buffer "
            "against Scotland.\n\n"
            "His death in 1141 came during "
            "the Anarchy — the civil war between "
            "Stephen and Matilda that followed "
            "Henry I's death."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Lord Chancellor of England under Henry I and Bishop of Durham (1133–1141); exemplary royal administrator-churchman of the Anglo-Norman period; holder of the palatine bishopric that guarded England's northeast against Scotland; served through the Norman administrative achievement and died during the Anarchy.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Henry I's administrative monarchy — the most sophisticated royal government in twelfth-century Europe, with a professional chancery, a systematized exchequer, and a corps of royal clerks who combined administrative service with ecclesiastical careers — created the institutional pathway through which Geoffrey rose from royal clerk to Chancellor to Bishop",
            "The Anglo-Norman tradition of using senior churchmen as royal administrators — exploiting their literacy, organizational skills, and canon law expertise in the royal government while rewarding them with bishoprics — defined the career model that Geoffrey exemplified",
            "The strategic importance of the Durham bishopric — whose palatine authority extended royal power into the dangerous northeast, providing military defense against Scotland and internal order in a frontier region — made it a reward worth granting to trusted royal servants like Geoffrey"
        ],
        "effects": [
            "His chancellorship contributed to Henry I's administrative achievements — the systematization of royal governance that made England the most administratively capable kingdom in twelfth-century Europe and created the institutional foundations that later Plantagenet kings built upon",
            "His Durham bishopric maintained the palatine see's function as both ecclesiastical center and regional government of the northeast — sustaining the church-state integration that made the Bishop of Durham one of the most powerful figures in northern England",
            "His career contributed to the development of English administrative culture — the professional chancery training and governmental techniques that his generation of royal clerks developed became foundational to the Common Law tradition",
            "His death during the Anarchy (1141) illustrated the political disruption that Henry I's succession crisis caused — the collapse of the administrative monarchy's stability that Geoffrey had served affected all levels of English governance"
        ],
        "relationships": [
            {"target": "henry-i-england", "verb": "SERVES", "note": "Lord Chancellor under Henry I"},
            {"target": "bishop-of-durham", "verb": "HOLDS", "note": "Bishop of Durham 1133–1141"},
            {"target": "durham-palatinate", "verb": "GOVERNS", "note": "Palatine bishop governing England's northeast"},
            {"target": "anglo-norman-church", "verb": "PART_OF", "note": "Anglo-Norman ecclesiastical administrator-bishop"},
            {"target": "the-anarchy", "verb": "DIES_DURING", "note": "Died during the civil war of Stephen and Matilda"}
        ]
    }),

    ("samuel-dickinson-hubbard", {
        "summary": (
            "Samuel Dickinson Hubbard (1799–1855) "
            "was an American Whig politician from "
            "Connecticut who served as a member "
            "of the U.S. House of Representatives "
            "(1845–1847) and as Postmaster General "
            "of the United States (1852–1853) "
            "under President Millard Fillmore. "
            "His appointment as Postmaster General "
            "came during the final years of the "
            "Whig Party — the administration of "
            "Fillmore (the last Whig president) "
            "that was grappling with the sectional "
            "crisis over slavery and the legacy "
            "of the Compromise of 1850.\n\n"
            "Hubbard was born in Middletown, "
            "Connecticut and built a business "
            "and legal career before entering "
            "politics. Connecticut's Whig tradition "
            "— rooted in the state's commercial "
            "and manufacturing interests, its "
            "moral reform culture, and its "
            "opposition to Jacksonian Democratic "
            "populism — provided the political "
            "environment for Hubbard's career.\n\n"
            "As Postmaster General, Hubbard "
            "managed the largest federal department "
            "in terms of employees and geographic "
            "reach — the postal system that was "
            "the primary instrument of federal "
            "presence in communities across "
            "the rapidly expanding United States.\n\n"
            "The Whig Party's collapse after "
            "the 1852 election ended his "
            "governmental career."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Connecticut Whig Congressman (1845–1847) and Postmaster General under Fillmore (1852–1853); managed the largest federal department in the final Whig administration; career ended with the Whig Party's collapse; representative of Connecticut's manufacturing-commercial Whig tradition.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Connecticut's Whig political tradition — the manufacturing state's commercial interests' alignment with Henry Clay's American System of protective tariffs and federal internal improvements — created the political constituency that supported Hubbard's Whig career",
            "The Fillmore administration's need for reliable Whig appointees to staff the cabinet departments — as the party faced its terminal sectional crisis over slavery — created the appointment opportunity that made Hubbard Postmaster General",
            "The United States Post Office's enormous expansion in the antebellum period — as mail routes multiplied across the rapidly settling West and postal employment grew to tens of thousands — created the administrative challenges that the Postmaster General had to manage"
        ],
        "effects": [
            "His Postmaster Generalship managed the United States Post Office during a period of rapid expansion — extending postal routes into new territories and managing the postal system's growth as the nation's most widely distributed federal institution",
            "His tenure contributed to the postal administration of the Fillmore years — the period of the Compromise of 1850's implementation and the final Whig administration's attempt to maintain sectional equilibrium",
            "The Whig Party's collapse after the 1852 election — triggered by the Kansas-Nebraska Act and the impossibility of maintaining a national coalition that included both Southern slaveholders and Northern moral reformers — ended Hubbard's governmental career as a party politician",
            "His career illustrated Connecticut's commercial Whig tradition — the manufacturing state's political culture that supported protective tariffs, federal enterprise, and moral reform against Jacksonian laissez-faire and Democratic populism"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Connecticut Representative 1845–1847"},
            {"target": "us-postmaster-general", "verb": "SERVES_AS", "note": "Postmaster General under Fillmore 1852–1853"},
            {"target": "millard-fillmore", "verb": "SERVES_UNDER", "note": "Cabinet member in the last Whig administration"},
            {"target": "whig-party", "verb": "MEMBER_OF", "note": "Connecticut Whig politician"},
            {"target": "compromise-of-1850", "verb": "SERVES_DURING", "note": "Postmaster General during Compromise of 1850 implementation"}
        ]
    }),

    ("stephen-allen", {
        "summary": (
            "Stephen Allen (1767–1852) was an "
            "American businessman, public servant, "
            "and politician from New York who "
            "served as Mayor of New York City "
            "(1821–1824) and as a New York state "
            "legislator. His mayoralty came "
            "during a pivotal period in New York "
            "City's history — the construction "
            "of the Erie Canal (1817–1825) that "
            "would transform New York from a "
            "major Atlantic port to the dominant "
            "commercial entrepôt of the entire "
            "American continent.\n\n"
            "Allen was born in New York and "
            "built his fortune in the sailmaking "
            "trade — a business that served "
            "the growing New York shipping "
            "industry. His business success "
            "translated into public service "
            "as a trustee and director of "
            "various city institutions, "
            "and eventually into political "
            "office as mayor.\n\n"
            "His mayoralty coincided with "
            "the final years of Erie Canal "
            "construction and the city's "
            "preparation for the flood of "
            "commerce that the canal would "
            "bring from the Great Lakes "
            "interior. The canal's opening "
            "in 1825 — celebrated with the "
            "'Wedding of the Waters' ceremony "
            "where canal water was poured "
            "into New York harbor — transformed "
            "New York City into America's "
            "commercial metropolis.\n\n"
            "He died aboard the steamship "
            "Henry Clay in a famous 1852 "
            "race that ended in disaster."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Mayor of New York City (1821–1824) during the final construction of the Erie Canal; sailmaking businessman and public servant who presided over New York's transformation into America's commercial metropolis; died in the Henry Clay steamboat disaster of 1852.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New York City's explosive commercial growth in the early nineteenth century — driven by its superior natural harbor, growing shipping industry, and the developing trade connections to the American interior — created the prosperous business environment in which sailmakers like Allen could build the fortunes that gave them civic prominence",
            "The Erie Canal project (authorized 1817, completed 1825) — Governor DeWitt Clinton's transformative infrastructure project that connected the Hudson River to Lake Erie — was the defining public works project of Allen's mayoral era, promising to make New York the dominant commercial center of the continent",
            "New York City's political culture of business-oriented civic leadership — in which successful merchants and craftsmen served as mayors and aldermen, bringing their commercial expertise to city governance — created the pathway through which Allen moved from sailmaking success to civic leadership"
        ],
        "effects": [
            "His mayoralty presided over New York City's governance during the critical years immediately preceding the Erie Canal's completion — managing city administration during the period when New York was preparing for the commercial transformation the canal would bring",
            "His civic leadership contributed to the development of New York's municipal institutions — the mayor's office, the common council, and the public services that a rapidly growing city required",
            "His death in the Henry Clay steamboat disaster (1852) — a famous race between steamboats that ended in a boiler explosion killing dozens — linked him to one of the era's most publicized transportation disasters, contributing to the public debate about steamboat safety regulation",
            "His career illustrated the civic culture of early nineteenth-century New York — successful craftsmen and merchants who translated business success into public service, building the institutional infrastructure of what would become America's largest and most commercially dominant city"
        ],
        "relationships": [
            {"target": "new-york-city", "verb": "GOVERNS", "note": "Mayor of New York City 1821–1824"},
            {"target": "erie-canal", "verb": "SERVES_DURING_CONSTRUCTION", "note": "Mayor during the final years of Erie Canal construction"},
            {"target": "dewitt-clinton", "verb": "CONTEMPORANEOUS_WITH", "note": "Mayor during the era of Erie Canal champion DeWitt Clinton"},
            {"target": "new-york-state", "verb": "SERVES_IN", "note": "New York state legislator"},
            {"target": "new-york-sailmaking-trade", "verb": "WORKS_IN", "note": "Built fortune as New York sailmaker before political career"}
        ]
    }),

    ("anne-du-bourg", {
        "summary": (
            "Anne du Bourg (1521–1559) was a French "
            "humanist lawyer and Protestant martyr "
            "who served as a member of the Parlement "
            "of Paris and whose trial and execution "
            "by burning became one of the defining "
            "moments of the French Reformation. "
            "A councillor in the Parlement — "
            "the highest court in France — he "
            "publicly challenged King Henry II "
            "in open court to stop the persecution "
            "of Protestants. This unprecedented "
            "act of judicial defiance led to his "
            "arrest, a sensational trial that "
            "engaged all of Europe's Protestant "
            "and Catholic opinion, and his "
            "execution by burning on 23 December "
            "1559.\n\n"
            "Du Bourg was educated in humanist "
            "legal scholarship at Toulouse and "
            "Orléans before appointment to the "
            "Parlement of Paris — the most "
            "prestigious legal institution in "
            "France. His conversion to Calvinism "
            "placed him among the growing "
            "number of educated Frenchmen who "
            "were drawn to Protestant reform "
            "in the 1540s and 1550s.\n\n"
            "His famous confrontation with Henry II "
            "in April 1559 — during an extraordinary "
            "session of the Parlement called "
            "to discuss persecution policy — "
            "shocked the court and the country. "
            "His execution transformed him "
            "into a Protestant martyr whose "
            "death inflamed Huguenot opinion "
            "and contributed to the conditions "
            "producing the Wars of Religion."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "French Calvinist lawyer and Parlement of Paris councillor who publicly challenged Henry II's persecution of Protestants in open court (1559); executed by burning December 23, 1559; his martyrdom inflamed Huguenot opinion and contributed to the conditions producing the French Wars of Religion.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The spread of Calvinism in France — the rapid growth of Protestant congregations (the Huguenots) among France's educated and artisan classes in the 1540s–1550s — created the social base for a Reformation movement that the French Crown was increasingly desperate to suppress",
            "Henry II's intensification of anti-Protestant persecution — the notorious Chambre Ardente (Burning Chamber) that executed hundreds of Protestants — created the political context for Du Bourg's courageous confrontation with the king, speaking directly to the monarch in the Parlement's assembly",
            "The humanist legal tradition at Paris — which valued scholarly freedom, natural law reasoning, and the rule of law over arbitrary royal will — provided the intellectual framework within which Du Bourg conceptualized his defiance of royal persecution as a legal and moral duty"
        ],
        "effects": [
            "His execution on 23 December 1559 transformed him into the most celebrated Protestant martyr in France — his death by burning after a highly publicized trial made him a symbol of French Protestant resistance and contributed to the radicalization of Huguenot opinion",
            "His martyrdom contributed to the conditions producing the French Wars of Religion (1562–1598) — his death and the injustice perceived in his trial inflamed Protestant opinion and deepened the sectarian conflict that his execution was intended to suppress",
            "His trial's sensational publicity — followed across Europe by Protestant and Catholic readers — made his case a cause célèbre of the Reformation era, contributing to the international Protestant discourse about martyrdom, resistance, and the duty to oppose tyrannical persecution",
            "His famous courtroom speech challenging Henry II — preserved in contemporary accounts and martyrologies — became a model text for later Protestant justifications of resistance to royal authority, contributing to the development of Calvinist political theology"
        ],
        "relationships": [
            {"target": "parlement-of-paris", "verb": "SERVES_IN", "note": "Councillor in France's highest court"},
            {"target": "henry-ii-france", "verb": "CONFRONTS", "note": "Publicly challenged the king's Protestant persecution in open court"},
            {"target": "french-calvinism", "verb": "CONVERTS_TO", "note": "Calvinist Huguenot jurist and martyr"},
            {"target": "french-wars-of-religion", "verb": "MARTYRDOM_CONTRIBUTES_TO", "note": "Execution inflamed Huguenot opinion ahead of the Wars of Religion"},
            {"target": "protestant-martyrs", "verb": "BECOMES", "note": "Executed by burning December 23, 1559"}
        ]
    }),

    ("claude-bazin-de-bezons", {
        "summary": (
            "Claude Bazin de Bezons (1617–1684) was "
            "a French royal official and intendant "
            "who served Louis XIV as the Intendant "
            "of Languedoc (1673–1685) — one of the "
            "most important provincial intendancies "
            "in France. The intendants were the "
            "king's personal agents in the provinces, "
            "bypassing the traditional provincial "
            "estates and local courts to impose "
            "royal authority directly — the "
            "institutional instrument of "
            "Louis XIV's centralizing absolutism.\n\n"
            "Languedoc was one of the most "
            "challenging provinces to govern "
            "in Bourbon France — a pays d'états "
            "with its own provincial Estates "
            "that jealously guarded local "
            "privileges, a large Protestant "
            "population that had been targeted "
            "by royal persecution since the "
            "revocation of the Edict of Nantes "
            "(1685), and the massive public works "
            "project of the Canal du Midi.\n\n"
            "Bazin de Bezons oversaw the "
            "completion of the Canal du Midi "
            "(1681) — Pierre-Paul Riquet's "
            "extraordinary engineering achievement "
            "connecting the Atlantic to the "
            "Mediterranean. His intendancy thus "
            "encompassed the final phase of "
            "one of the seventeenth century's "
            "greatest infrastructure projects.\n\n"
            "His administration exemplified "
            "the Colbertian intendant at the "
            "height of Louis XIV's power."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Intendant of Languedoc (1673–1685) under Louis XIV; oversaw the completion of the Canal du Midi (1681) — one of the seventeenth century's greatest engineering achievements; administered Languedoc during the approach to the Revocation of the Edict of Nantes; key figure in Louis XIV's absolutist provincial administration.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Louis XIV's absolutist program of centralization — replacing the power of provincial governors, parlements, and estates with royal intendants who reported directly to Versailles — created the office that Bazin de Bezons filled as the king's direct representative in Languedoc",
            "Colbert's economic program of state-directed commercial development — which included the Canal du Midi as a major infrastructure investment designed to facilitate French internal trade and reduce dependence on Atlantic and Mediterranean shipping routes controlled by foreign powers — provided the context for Bazin de Bezons's intendancy",
            "Languedoc's special governance challenges — its Protestant minority, its powerful Estates, its geographic remoteness from Paris, and its role in France's Mediterranean trade — made the intendancy one of the most demanding provincial posts in France"
        ],
        "effects": [
            "His oversight of the Canal du Midi's completion in 1681 — one of the greatest engineering projects of the seventeenth century, connecting the Atlantic and Mediterranean through 241 kilometers of canal and 91 locks — made his intendancy responsible for one of France's most lasting public works achievements",
            "His administration of Languedoc during the approach to the Revocation of the Edict of Nantes (1685) contributed to the implementation of royal religious policy in a province with a significant Protestant minority",
            "His intendancy demonstrated the effectiveness of Louis XIV's absolutist administrative system — the intendant as the king's direct agent bypassing local institutions and ensuring royal policy implementation in even the most recalcitrant provinces",
            "His career contributed to the development of the intendant system as the model of French provincial administration — the template that later French administrative culture, including Napoleon's prefects, built upon"
        ],
        "relationships": [
            {"target": "louis-xiv", "verb": "SERVES", "note": "Royal intendant directly serving the Sun King"},
            {"target": "languedoc", "verb": "GOVERNS", "note": "Intendant of Languedoc 1673–1685"},
            {"target": "canal-du-midi", "verb": "OVERSEES_COMPLETION", "note": "Intendant during Canal du Midi's 1681 completion"},
            {"target": "jean-baptiste-colbert", "verb": "IMPLEMENTS_POLICY_OF", "note": "Colbertian intendant executing royal economic program"},
            {"target": "edict-of-nantes-revocation", "verb": "PRECEDES", "note": "Administered Languedoc immediately before the Revocation"}
        ]
    }),

    ("guillaume-van-volxem", {
        "summary": (
            "Guillaume van Volxem (1754–1837) was "
            "a Belgian jurist, politician, and "
            "public official who navigated the "
            "extraordinary political transformations "
            "that Belgium experienced between "
            "the 1780s and the 1830s — from "
            "Habsburg Austrian rule through "
            "French Revolutionary conquest, "
            "Napoleonic integration, the post-1815 "
            "Kingdom of the Netherlands, and "
            "finally to Belgian independence "
            "in 1830. His long career across "
            "five distinct political regimes "
            "represented the adaptive pragmatism "
            "of the Belgian professional classes "
            "who maintained their social positions "
            "by serving successive governing "
            "authorities.\n\n"
            "Van Volxem was born in Brussels "
            "and trained as a lawyer in the "
            "Habsburg administrative tradition "
            "before the French Revolutionary "
            "armies conquered the Austrian "
            "Netherlands in 1794. The French "
            "occupation abolished the old "
            "Habsburg institutions and imposed "
            "French revolutionary law — including "
            "the Napoleonic Code — on the "
            "Belgian territories.\n\n"
            "His legal expertise allowed him "
            "to maintain his professional "
            "position through French, Dutch, "
            "and Belgian governance — serving "
            "in judicial and administrative "
            "capacities under each regime.\n\n"
            "He lived long enough to see the "
            "Belgian Revolution of 1830 and "
            "the establishment of the independent "
            "Kingdom of Belgium."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Belgian jurist who maintained a legal career across five distinct political regimes (Habsburg Austria, French Revolution, Napoleon, Kingdom of the Netherlands, Belgian independence); representative of the Belgian professional class's adaptive pragmatism through the turbulent 1780s–1830s; contributed to the institutional continuity that bridged Belgian regimes.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The French Revolutionary conquest of the Austrian Netherlands (1794) and its integration into the French Republic — replacing Habsburg institutions with French revolutionary law, dissolving old courts, and imposing the Napoleonic Code — created the political environment in which Van Volxem's legal career had to adapt or perish",
            "The post-1815 Vienna settlement's creation of the Kingdom of the Netherlands — uniting Belgium with Holland under William I of Orange in a politically controversial arrangement that many Belgians resisted — created the further political transformation that Van Volxem's career had to navigate",
            "The Belgian Revolution of 1830 — the uprising against Dutch rule that established Belgium as an independent constitutional monarchy — was the final regime change of Van Volxem's long career, producing the state he served in his final years"
        ],
        "effects": [
            "His legal career across five regimes contributed to the institutional continuity of Belgian judicial and administrative culture — maintaining legal expertise and professional practice through the successive institutional disruptions of the 1790s–1830s",
            "His adaptation to French law under the Napoleonic Code contributed to the deep penetration of French legal culture into Belgian institutional life — a legacy that shaped Belgian law long after the French occupation ended",
            "His service under the Kingdom of the Netherlands contributed to Belgian administrative culture during the 1815–1830 period — helping maintain the institutions that would be carried forward into independent Belgium",
            "His long life — from Habsburg Belgium to independent Belgium — made him a living embodiment of the extraordinary political transformations that his generation of Belgians experienced, bridging the pre-Revolutionary and post-Revolutionary worlds"
        ],
        "relationships": [
            {"target": "austrian-netherlands", "verb": "SERVES_IN", "note": "Legal professional under Habsburg Austrian rule"},
            {"target": "napoleonic-france", "verb": "SERVES_UNDER", "note": "Adapted career to French Revolutionary and Napoleonic governance"},
            {"target": "kingdom-of-netherlands", "verb": "SERVES_IN", "note": "Official under William I's Kingdom of the Netherlands"},
            {"target": "belgian-revolution-1830", "verb": "SURVIVES_TO", "note": "Witnessed Belgian independence as an octogenarian"},
            {"target": "brussels", "verb": "LIVES_IN", "note": "Brussels-born jurist throughout his long career"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 60 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
