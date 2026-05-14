#!/usr/bin/env python3
"""
Batch 59 — 8 entities: Franklin Davenport, William de Mandeville 3rd Earl of Essex,
William Harper, Benjamin Ruggles, Charles Goldsborough, David Meriwether,
George Gordon 2nd Earl of Huntly, Nicholas Fish
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

    ("franklin-davenport", {
        "summary": (
            "Franklin Davenport (1755–1832) was an "
            "American Federalist politician from "
            "New Jersey who served as a U.S. Senator "
            "(1798–1799), a U.S. Representative "
            "(1799–1801), and a judge of the New Jersey "
            "Superior Court. His congressional career "
            "fell entirely within the Adams administration's "
            "most politically charged years — the period "
            "of the XYZ Affair, the Quasi-War with France, "
            "the Alien and Sedition Acts, and the "
            "election of 1800 that ended Federalist "
            "dominance.\n\n"
            "Davenport was born in Connecticut "
            "and settled in New Jersey, where "
            "he built a legal career before "
            "entering politics. New Jersey's "
            "political culture in the 1790s "
            "reflected the Federalist strength "
            "of the mid-Atlantic states — "
            "a state that backed Washington and "
            "Adams's administrations.\n\n"
            "His Senate appointment (filling "
            "a vacancy in 1798) placed him "
            "in the body during the peak of "
            "the Quasi-War crisis — when Adams's "
            "administration was building the "
            "Navy, passing the Alien and Sedition "
            "Acts, and managing the undeclared "
            "naval war with France. His subsequent "
            "House service extended through "
            "the election of 1800.\n\n"
            "His judicial career on the New Jersey "
            "Superior Court after his congressional "
            "service contributed to New Jersey's "
            "legal development in the early republic."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "New Jersey Federalist Senator (1798–1799) and Representative (1799–1801) during the Quasi-War and Alien and Sedition Acts; New Jersey Superior Court judge; served during the peak of Adams administration crisis and the pivotal election of 1800.",
            "significanceCategory": "local"
        },
        "causes": [
            "The Quasi-War crisis with France (1798–1800) — the undeclared naval war that resulted from the XYZ Affair and the Directory's treatment of American diplomats — created the emergency political environment in which Davenport's Senate appointment occurred and the Alien and Sedition Acts were passed",
            "New Jersey's Federalist political tradition — its mid-Atlantic commercial interests aligned with Hamilton's financial system and Adams's diplomacy — produced the political constituency that supported Davenport's congressional career as a Federalist",
            "The election of 1800 and Jefferson's defeat of Adams — the 'Revolution of 1800' that ended Federalist national dominance and began three decades of Democratic-Republican rule — was the defining political fact of Davenport's congressional career, ending with the defeat of the party he served"
        ],
        "effects": [
            "His Senate and House service contributed to New Jersey's Federalist representation during the critical Adams years — supporting the naval buildup, the Alien and Sedition Acts, and the constitutional crisis of the election of 1800",
            "His post-congressional judicial career on the New Jersey Superior Court contributed to New Jersey's legal development during the early Jeffersonian period — maintaining Federalist legal values on the bench after the party's electoral defeat",
            "His career illustrated the fate of many Federalist politicians after 1800 — finding refuge in judicial appointments after electoral defeat as the Federalist party declined from national dominance to regional opposition",
            "His service during the Quasi-War illustrated New Jersey's role in the broader Federalist coalition that supported Adams's foreign policy — the mid-Atlantic and New England Federalist states that backed the naval war with France"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "New Jersey Senator 1798–1799"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "New Jersey Representative 1799–1801"},
            {"target": "federalist-party", "verb": "MEMBER_OF", "note": "Federalist politician in the Adams era"},
            {"target": "quasi-war-france", "verb": "SERVES_DURING", "note": "Congressman during the undeclared naval war with France"},
            {"target": "alien-and-sedition-acts", "verb": "SERVES_DURING", "note": "Senator during the passage of the Alien and Sedition Acts"}
        ]
    }),

    ("william-de-mandeville-3rd-earl-of-essex", {
        "summary": (
            "William de Mandeville, 3rd Earl of Essex "
            "(c. 1150–1189), was an Anglo-Norman "
            "magnate and royal official who served "
            "as Chief Justiciar of England under "
            "Henry II and as co-regent during "
            "Richard I's absence on the Third "
            "Crusade (1190). One of the most "
            "powerful men in England during the "
            "final years of Henry II's reign, "
            "he combined military command, "
            "administrative authority, and "
            "diplomatic service — a model of "
            "the professional royal administrator "
            "that the Angevin kings relied upon "
            "to govern their vast empire.\n\n"
            "The Mandeville family was one of "
            "the great Anglo-Norman baronial "
            "dynasties whose fortunes were "
            "intimately tied to the Crown. "
            "William de Mandeville served Henry II "
            "in multiple capacities — on diplomatic "
            "missions to the continent, as a "
            "military commander, and as one of "
            "the king's senior justiciars administering "
            "England's legal and governmental system.\n\n"
            "His appointment as co-regent by "
            "Richard I before the king departed "
            "on the Third Crusade in 1190 placed "
            "him among England's most powerful "
            "men — though he died in November 1189 "
            "before Richard had even departed, "
            "leaving his co-regency role to others.\n\n"
            "His death ended the direct Mandeville "
            "male line, and the Earldom of Essex "
            "passed to other families."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Chief Justiciar of England under Henry II and designated co-regent under Richard I for the Third Crusade; powerful Anglo-Norman magnate whose career exemplified the Angevin administrative state; death ended the Mandeville male line and the Earldom of Essex.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Angevin administrative revolution under Henry II — the systematic development of royal administrative institutions including the common law courts, the exchequer, and the justiciars who governed England in the king's name — created the institutional context in which Mandeville's administrative career flourished as a senior royal servant",
            "The Third Crusade's requirement that Richard I leave England for an extended campaign in the Holy Land — necessitating the appointment of trusted regents to govern in his absence — created the appointment that elevated Mandeville to co-regent status, though he died before the crusade departed",
            "The Anglo-Norman baronial system's integration of great magnates into royal governance — using their military power, local authority, and social prestige in the king's service in exchange for honors and rewards — defined the relationship between the Crown and magnates like Mandeville that made the Angevin administrative state function"
        ],
        "effects": [
            "His service as Chief Justiciar under Henry II contributed to the development of England's common law administration — the expanding royal court system and legal procedures that transformed English governance in the twelfth century",
            "His designated co-regency appointment illustrated Richard I's governance style — delegating English administration to trusted magnates while pursuing his crusading ambitions — and established the precedent for the regency councils that governed England during his absence",
            "His death ending the Mandeville male line contributed to the redistribution of one of England's greatest baronial lordships — the Essex earldom's passage to other families illustrating the fluid nature of aristocratic inheritance in the twelfth century",
            "His career exemplified the professional royal administrator who combined military command, judicial authority, and diplomatic service — the model of magnate service to the Crown that the Angevin kings systematically developed as an alternative to feudal obligation"
        ],
        "relationships": [
            {"target": "henry-ii-england", "verb": "SERVES", "note": "Chief Justiciar under Henry II"},
            {"target": "richard-i-england", "verb": "SERVES", "note": "Designated co-regent for Richard I's Third Crusade"},
            {"target": "third-crusade", "verb": "PREPARES_FOR", "note": "Named co-regent before the crusade's departure"},
            {"target": "angevin-empire", "verb": "ADMINISTERS", "note": "Senior official of the Angevin administrative state"},
            {"target": "earldom-of-essex", "verb": "HOLDS", "note": "3rd Earl of Essex whose death ended the Mandeville line"}
        ]
    }),

    ("william-harper", {
        "summary": (
            "William Harper (1790–1847) was a South "
            "Carolina jurist, politician, and pro-"
            "slavery theorist whose legal and "
            "intellectual career made him one "
            "of the most important architects "
            "of the antebellum South's ideology. "
            "He served as Chancellor of South "
            "Carolina (1828–1847), as a U.S. "
            "Senator (1826), and as Speaker of "
            "the South Carolina legislature — "
            "but his most historically significant "
            "contribution was the Memoir on Slavery "
            "(1837), a systematic philosophical "
            "defense of slavery as a positive "
            "good that influenced the entire "
            "generation of Southern pro-slavery "
            "thinkers.\n\n"
            "Harper was born in Antigua and "
            "educated at South Carolina College "
            "before building his legal and "
            "political career in the state that "
            "was the intellectual heart of the "
            "Southern defense of slavery. South "
            "Carolina's nullification crisis "
            "(1832–1833) — the constitutional "
            "confrontation with Jackson's administration "
            "over the tariff — placed Harper "
            "in the front ranks of the state "
            "rights movement.\n\n"
            "His Memoir on Slavery presented "
            "slavery not as a necessary evil "
            "to be tolerated but as a positive "
            "social institution beneficial to "
            "both masters and enslaved — a "
            "philosophical reversal that became "
            "the cornerstone of the South's "
            "defense of the institution.\n\n"
            "His legal and intellectual career "
            "made South Carolina the ideological "
            "center of pro-slavery thought."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "South Carolina jurist, Senator, and pro-slavery theorist; author of the Memoir on Slavery (1837) — one of the most influential defenses of slavery as a 'positive good'; Chancellor of South Carolina; South Carolina nullification movement participant; intellectual architect of the antebellum South's pro-slavery ideology.",
            "significanceCategory": "continental"
        },
        "causes": [
            "South Carolina's development as the intellectual center of Southern pro-slavery ideology — driven by the state's large enslaved population, its rice and cotton plantation economy, and its leading political figures' determination to defend slavery against Northern antislavery criticism — created the cultural environment in which Harper's Memoir on Slavery was produced and celebrated",
            "The nullification crisis (1832–1833) and John C. Calhoun's elaboration of states' rights doctrine — which challenged federal authority over tariff policy and established the constitutional framework for Southern resistance to federal power — provided the political context for Harper's broader ideology of Southern distinctiveness and the positive defense of slavery",
            "The growing Northern antislavery movement — the American Anti-Slavery Society (founded 1833), abolitionist newspapers like The Liberator, and the political pressure for slavery's restriction — created the polemical challenge that Harper's Memoir on Slavery was designed to answer systematically"
        ],
        "effects": [
            "His Memoir on Slavery (1837) became one of the foundational texts of the antebellum South's positive-good defense of slavery — shifting the Southern response to abolitionism from defensive apology to ideological assertion that slavery was beneficial for civilization, and influencing the entire generation of pro-slavery writers including John C. Calhoun",
            "His legal career as South Carolina Chancellor contributed to South Carolina's judicial development — issuing decisions that defined the legal status of enslaved people in South Carolina law",
            "His participation in South Carolina's nullification movement contributed to the constitutional doctrine that states could nullify federal law — the doctrinal foundation that Southern secessionists later invoked to justify secession",
            "His intellectual legacy helped shape the South's collective self-understanding in the antebellum decades — the pro-slavery ideology he articulated provided the ideological foundation for the Confederate cause and the Lost Cause mythology that followed"
        ],
        "relationships": [
            {"target": "south-carolina", "verb": "SERVES", "note": "Chancellor of South Carolina and state legislator"},
            {"target": "memoir-on-slavery-1837", "verb": "AUTHORS", "note": "Authored influential defense of slavery as a positive good"},
            {"target": "nullification-crisis", "verb": "PARTICIPATES_IN", "note": "South Carolina nullification movement figure"},
            {"target": "john-c-calhoun", "verb": "ALLIED_WITH", "note": "South Carolina states' rights theorist aligned with Calhoun"},
            {"target": "pro-slavery-ideology", "verb": "ADVANCES", "note": "Key intellectual architect of the antebellum South's slavery defense"}
        ]
    }),

    ("benjamin-ruggles", {
        "summary": (
            "Benjamin Ruggles (1783–1857) was an "
            "American Democratic-Republican politician "
            "from Ohio who served as a U.S. Senator "
            "(1815–1833) — a remarkably long Senate "
            "tenure of eighteen years that placed "
            "him in the Senate through the entire "
            "Era of Good Feelings, the collapse "
            "of the first party system, and the "
            "emergence of Jacksonian Democracy. "
            "His long Senate service made him one "
            "of Ohio's most senior early federal "
            "legislators.\n\n"
            "Ruggles was born in Connecticut and "
            "migrated to Ohio — the typical migration "
            "pattern of New Englanders who poured "
            "into Ohio's Western Reserve in the "
            "early nineteenth century. The Western "
            "Reserve — northeastern Ohio — was "
            "settled predominantly by Connecticut "
            "Yankees who brought their Congregational "
            "religious culture and Federalist "
            "political traditions westward, "
            "creating a distinctive New England "
            "enclave in the Ohio frontier.\n\n"
            "His eighteen years in the Senate "
            "spanned the Madison years, the "
            "Monroe Era of Good Feelings, "
            "the contested 1824 election, "
            "and the first Jackson term — "
            "a period of enormous partisan "
            "transformation in which the "
            "Democratic-Republican party "
            "fractured and the second party "
            "system of Democrats and Whigs emerged.\n\n"
            "His longevity made him a major figure "
            "in Ohio's early federal politics."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Ohio Democratic-Republican Senator (1815–1833) for eighteen years; Connecticut-born Western Reserve politician who served through the Era of Good Feelings, the 1824 election, and the Jacksonian transition; one of Ohio's most senior early federal legislators.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Ohio's rapid population growth through New England and mid-Atlantic migration — particularly the Connecticut Western Reserve's settlement by Yankees who brought their political traditions to northeastern Ohio — created the political constituency for Democratic-Republican politicians like Ruggles who embodied the New England-Ohio settler community",
            "The Era of Good Feelings and the dominance of a single national party (the Democratic-Republicans) — which made Senate service a matter of factional competition within the party rather than partisan conflict between parties — shaped the political environment of Ruggles's early Senate years",
            "The collapse of the first party system and the 1824 election's factional chaos — the emergence of Adams, Jackson, Crawford, and Clay factions within the Democratic-Republican coalition — defined the political turbulence of Ruggles's later Senate years"
        ],
        "effects": [
            "His eighteen-year Senate tenure made him one of Ohio's most important voices in the federal government during the state's formative period — the decades when Ohio grew from a frontier state to one of the largest and most politically significant states in the Union",
            "His Senate service contributed to Ohio's representation in the major legislative debates of the 1815–1833 period — including the Missouri Compromise, the American System tariff debates, and the early Bank War",
            "His career illustrated the typical Western Reserve political trajectory — New England migrants who brought Federalist cultural values to Ohio before adapting them to the Democratic-Republican and eventually Whig frameworks",
            "His longevity in the Senate contributed to the development of Ohio's political institutions — establishing patterns of federal representation and senatorial service that successive Ohio politicians built upon"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Ohio Senator 1815–1833 for eighteen years"},
            {"target": "ohio", "verb": "REPRESENTS", "note": "Ohio's Western Reserve Connecticut-Yankee politician"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "Jeffersonian Democratic-Republican"},
            {"target": "missouri-compromise-1820", "verb": "VOTES_ON", "note": "Senator during the Missouri Compromise debates"},
            {"target": "era-of-good-feelings", "verb": "SERVES_DURING", "note": "Senator through the peak of Era of Good Feelings"}
        ]
    }),

    ("charles-goldsborough", {
        "summary": (
            "Charles Goldsborough (1765–1834) was "
            "a Maryland Federalist politician who "
            "served as Governor of Maryland "
            "(1818–1819) and as a member of the "
            "U.S. House of Representatives "
            "(1805–1817). His career represented "
            "Maryland's Federalist tradition — "
            "one of the last states where Federalism "
            "maintained electoral viability "
            "into the 1810s — and his governorship "
            "was notable as one of the final "
            "Federalist governorships in American "
            "history before the party's complete "
            "national collapse.\n\n"
            "Goldsborough was born to a prominent "
            "Maryland family in the Eastern Shore "
            "region — the Chesapeake Bay's eastern "
            "peninsula that had long been Maryland's "
            "most aristocratic and politically "
            "conservative region, dominated by "
            "large tobacco planters with strong "
            "ties to British commercial culture "
            "and Federalist political values.\n\n"
            "His twelve years in the House "
            "(1805–1817) spanned the Jefferson "
            "and Madison administrations — "
            "a period of Democratic-Republican "
            "dominance nationally but persistent "
            "Federalist resistance in Maryland. "
            "His votes against the War of 1812 "
            "reflected Maryland's Eastern Shore "
            "Federalism's opposition to the "
            "war that threatened the Chesapeake's "
            "commercial economy.\n\n"
            "His brief governorship (1818–1819) "
            "represented the last gasp of Federalist "
            "state-level power in Maryland."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Maryland Federalist Governor (1818–1819) and Congressman (1805–1817); one of the last Federalist governors in American history; Maryland Eastern Shore aristocratic politician representing the final phase of Federalist state-level power; voted against the War of 1812.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Maryland's Eastern Shore Federalist tradition — rooted in the large tobacco-planting gentry's British cultural orientation, commercial ties to British merchants, and conservative political values — created the persistent Federalist constituency that sustained Goldsborough's long House career and eventual governorship even as the party collapsed nationally",
            "The War of 1812's devastating impact on the Chesapeake economy — the British naval blockade, the burning of Washington in 1814, and the disruption of the tobacco and grain trade that Maryland's Eastern Shore depended upon — intensified Federalist opposition in Maryland and gave Goldsborough's anti-war position local credibility",
            "Maryland's competitive two-party politics — one of the few states where Federalists maintained genuine electoral competition with Democratic-Republicans into the 1810s — created the partisan environment in which Goldsborough could win both congressional and gubernatorial races"
        ],
        "effects": [
            "His twelve-year House tenure contributed to the Federalist minority's legislative voice during the Jefferson and Madison years — opposing the Louisiana Purchase's constitutional implications, the trade embargo, and the War of 1812 from a principled constitutional-commercial standpoint",
            "His governorship represented one of the last examples of Federalist state-level executive power in American history — demonstrating Federalism's ability to win individual state elections even as the national party ceased to be competitive for the presidency",
            "His career illustrated the Eastern Shore Chesapeake political culture — the aristocratic, commercially oriented, British-connected world that made the Maryland Eastern Shore one of Federalism's last regional strongholds",
            "His post-political longevity — living until 1834 — made him a witness to the complete transformation of American party politics from Federalist-Republican competition through the Era of Good Feelings to the Jacksonian Democratic era"
        ],
        "relationships": [
            {"target": "maryland", "verb": "GOVERNS", "note": "Governor of Maryland 1818–1819"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Maryland Representative 1805–1817"},
            {"target": "federalist-party", "verb": "MEMBER_OF", "note": "One of the last Federalist governors in America"},
            {"target": "war-of-1812", "verb": "OPPOSES", "note": "Anti-war Federalist during the War of 1812"},
            {"target": "maryland-eastern-shore", "verb": "REPRESENTS", "note": "Eastern Shore aristocratic Federalist politician"}
        ]
    }),

    ("david-meriwether", {
        "summary": (
            "David Meriwether (1800–1893) was an "
            "American politician and explorer from "
            "Kentucky who served as Governor of "
            "New Mexico Territory (1853–1856) and "
            "as a U.S. Senator from Kentucky "
            "(1852). His remarkable career combined "
            "frontier exploration — he traveled "
            "the Great Plains and Rocky Mountains "
            "in his youth — with political service "
            "in Kentucky and then executive "
            "leadership in the newly organized "
            "New Mexico Territory during the "
            "critical early years of American "
            "governance in the Southwest.\n\n"
            "Meriwether was born in Virginia and "
            "raised in Kentucky before undertaking "
            "extensive travels in the trans-"
            "Mississippi West as a young man. "
            "These frontier experiences — including "
            "contact with numerous Native American "
            "peoples — gave him practical knowledge "
            "of the West that later proved relevant "
            "to his territorial governorship.\n\n"
            "His appointment as Governor of New "
            "Mexico Territory by President Pierce "
            "placed him at the head of one of "
            "the most complex territories in "
            "the United States — a region with "
            "a large Hispanic population, "
            "numerous Native American nations, "
            "and complex land tenure questions "
            "inherited from Spanish and Mexican "
            "law.\n\n"
            "He lived to 93 — one of the longest-"
            "lived American territorial governors "
            "— dying in 1893."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Governor of New Mexico Territory (1853–1856) and briefly U.S. Senator from Kentucky (1852); frontier explorer with pre-political experience in the trans-Mississippi West; administered one of the most complex American territories — with Hispanic, Native American, and settler populations — in the critical early U.S. governance period.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Mexican-American War (1846–1848) and the Treaty of Guadalupe Hidalgo's acquisition of New Mexico — creating a vast new territory with a large Hispanic Catholic population, complex Spanish land grants, and numerous Native American nations — generated the administrative challenges that Governor Meriwether's tenure had to address",
            "The Gadsden Purchase (1853) — which added southern New Mexico and Arizona to the United States shortly before Meriwether's appointment — further complicated New Mexico Territory's governance by adding additional land with uncertain boundaries and contested ownership",
            "Meriwether's frontier experience with Native American peoples during his youthful western travels — giving him practical knowledge of Plains and Mountain Indian cultures — made him a more capable frontier diplomat than most appointed territorial governors"
        ],
        "effects": [
            "His governorship established American administrative structures in New Mexico Territory during the critical first decade of U.S. governance — managing the complex transition from Mexican to American legal and institutional frameworks while maintaining relations with both the Hispanic population and Native American nations",
            "His negotiations with New Mexico's Native American peoples — attempting to establish reservation agreements with Apache and Navajo groups — contributed to the early U.S. policy framework in the Southwest, though most of these agreements were not ratified by Congress",
            "His tenure contributed to the development of New Mexico's territorial governance institutions — the legal, administrative, and political structures that would eventually support the Territory's evolution toward statehood",
            "His extraordinary longevity — living to 1893, 37 years after his governorship ended — made him a living historical bridge between the Mexican-era Southwest and the industrialized, transcontinental-railroad-connected America of the Gilded Age"
        ],
        "relationships": [
            {"target": "new-mexico-territory", "verb": "GOVERNS", "note": "Governor of New Mexico Territory 1853–1856"},
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Kentucky Senator briefly in 1852"},
            {"target": "franklin-pierce", "verb": "APPOINTED_BY", "note": "Pierce administration territorial appointee"},
            {"target": "treaty-of-guadalupe-hidalgo", "verb": "ADMINISTERS_AFTERMATH_OF", "note": "Governed the territory acquired from Mexico"},
            {"target": "gadsden-purchase-1853", "verb": "GOVERNS_DURING", "note": "Governor during New Mexico's Gadsden Purchase addition"}
        ]
    }),

    ("george-gordon-2nd-earl-of-huntly", {
        "summary": (
            "George Gordon, 2nd Earl of Huntly "
            "(c. 1440–1501), was a Scottish nobleman "
            "and royal official who served as Lord "
            "High Chancellor of Scotland under "
            "James III and James IV — one of the "
            "most powerful positions in the Scottish "
            "kingdom. The Gordons of Huntly were "
            "the dominant noble family of northern "
            "Scotland — their power based in "
            "Aberdeenshire and Strathbogie — "
            "and George Gordon's chancellorship "
            "gave them unprecedented influence "
            "at the royal court alongside their "
            "regional dominance in the north.\n\n"
            "His career spanned one of the most "
            "turbulent periods in Scottish history "
            "— the reign of James III, whose "
            "favorites and foreign policy alienated "
            "the Scottish nobility and eventually "
            "led to his murder at the Battle of "
            "Sauchieburn (1488); and the early "
            "reign of James IV, the most "
            "brilliant of the Stewart kings.\n\n"
            "Huntly's position as Chancellor "
            "required him to navigate the "
            "dangerous politics of a kingdom "
            "where royal authority and noble "
            "power were in constant tension. "
            "He participated in the coup against "
            "James III and subsequently served "
            "the new king James IV.\n\n"
            "The Gordon family's power in northern "
            "Scotland was built significantly "
            "during his tenure as the dominant "
            "magnate of the northeast."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Lord High Chancellor of Scotland under James III and James IV; dominant noble of northern Scotland and patriarch of the Gordon power in Aberdeenshire; participated in the 1488 coup against James III; navigated the transition to James IV's brilliant reign.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Stewart kings' strategy of using great northern magnates to control the highland periphery — granting the Gordons of Huntly exceptional authority in Aberdeenshire in exchange for military service and political loyalty — created the basis for the family's regional power that George Gordon inherited and extended",
            "James III's political crises — his unpopular favorites, contentious foreign policy, and alienation of the Scottish nobility — created the factional politics in which Huntly had to operate as Chancellor while navigating between royal authority and noble opposition that eventually led to James III's overthrow",
            "The Scottish kingdom's governance challenges in the north — managing the Gaelic-speaking highlands, the Norse-influenced islands, and the persistent problems of noble violence and jurisdictional conflict — required a powerful northern magnate like Huntly to exercise royal authority in regions where the Crown could not govern directly"
        ],
        "effects": [
            "His chancellorship contributed to the governance of Scotland during the unstable reign of James III — maintaining royal administrative functions despite the political turbulence caused by the king's controversial favorites and foreign policy",
            "His participation in the 1488 coup that ended James III's reign and his subsequent service to James IV demonstrated the Gordon family's ability to adapt to political change — maintaining their influence through the regime transition that killed James III and brought his son to power",
            "His tenure as Chancellor and regional magnate built the Gordon family's power in northern Scotland to its greatest extent — establishing the foundation for the family's continued dominance in Aberdeenshire through the sixteenth century",
            "The Gordon family's northern dominance that he consolidated became one of the key features of Scottish political geography — their power later becoming important in the Scottish Reformation controversies when the Gordons remained Catholic while most Scottish nobility accepted Protestantism"
        ],
        "relationships": [
            {"target": "scotland", "verb": "SERVES", "note": "Lord High Chancellor of Scotland under James III and James IV"},
            {"target": "james-iii-scotland", "verb": "SERVES_UNDER", "note": "Chancellor during James III's controversial reign"},
            {"target": "james-iv-scotland", "verb": "SERVES_UNDER", "note": "Continued service under James IV after 1488 coup"},
            {"target": "gordon-family", "verb": "LEADS", "note": "2nd Earl of Huntly and patriarch of Gordon power"},
            {"target": "aberdeenshire", "verb": "DOMINATES", "note": "Dominant magnate of northern Scotland"}
        ]
    }),

    ("nicholas-fish", {
        "summary": (
            "Nicholas Fish (1758–1833) was an "
            "American soldier, lawyer, and Federalist "
            "politician from New York who served "
            "as a Continental Army officer during "
            "the Revolutionary War — rising to "
            "the rank of Lieutenant Colonel and "
            "serving in several major campaigns — "
            "and later as a New York state official "
            "and prominent Federalist Party leader. "
            "His military service placed him "
            "in the company of Alexander Hamilton "
            "and other New York Federalists who "
            "shaped the state's post-Revolutionary "
            "politics.\n\n"
            "Fish was born in New York City and "
            "served in the Continental Army from "
            "1775 through the war's end, seeing "
            "action at the battles of Brandywine, "
            "Germantown, Monmouth, and the Sullivan "
            "Campaign against the Iroquois (1779). "
            "His friendship with Alexander Hamilton "
            "dated from their shared service in "
            "the Revolutionary army.\n\n"
            "After the war he built a legal career "
            "in New York City and became a leading "
            "figure in New York's Federalist Party "
            "— one of Hamilton's circle of "
            "New York Federalists who supported "
            "the Constitution, the financial "
            "system, and the policies of the "
            "Washington and Adams administrations.\n\n"
            "His son Hamilton Fish became one "
            "of New York's most important "
            "politicians of the next generation."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Continental Army Lieutenant Colonel who served at Brandywine, Germantown, Monmouth, and Sullivan Campaign; Hamilton's friend and New York Federalist leader; his son Hamilton Fish became one of New York's most distinguished politicians; representative of the Revolutionary generation's transition into Federalist politics.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The American Revolutionary War and New York's role as the central theater of British and American military operations — with campaigns at Long Island, Manhattan, Brandywine, Monmouth, and the Sullivan expedition against the Iroquois — created the military service through which Fish built his reputation as a Continental Army officer",
            "Alexander Hamilton's circle of New York Federalists — the network of lawyers, merchants, and former officers who supported Hamilton's financial system, the Constitution, and Federalist political principles — provided the social and political world in which Fish became a major figure",
            "New York's complex post-Revolutionary politics — the factional battles between Hamilton's Federalists, the Clinton faction, and eventually the Burr and Livingston interests — created the political environment in which Fish operated as a Federalist in one of the most contested states in the early republic"
        ],
        "effects": [
            "His military career contributed to the Continental Army's campaigns in the Middle Atlantic theater — his service at Brandywine, Germantown, and Monmouth placing him among the officers who sustained Washington's army through its most difficult years",
            "His participation in the Sullivan Campaign against the Iroquois (1779) contributed to the systematic destruction of the Six Nations' villages in New York and Pennsylvania — a campaign that permanently broke Iroquois power in the region and opened the territory to American settlement",
            "His Federalist political career contributed to Hamilton's New York network — the professional and political connections that shaped New York's policies and helped maintain Federalist strength in the state through the early republic",
            "His family's legacy was continued and amplified by his son Hamilton Fish — who served as Governor of New York, U.S. Senator, and Secretary of State under Grant — making Nicholas Fish the patriarch of one of New York's most distinguished political families"
        ],
        "relationships": [
            {"target": "continental-army", "verb": "SERVES_IN", "note": "Lieutenant Colonel in the Revolutionary War"},
            {"target": "alexander-hamilton", "verb": "ALLIED_WITH", "note": "Hamilton's friend and New York Federalist associate"},
            {"target": "federalist-party", "verb": "MEMBER_OF", "note": "New York Federalist Party leader"},
            {"target": "sullivan-campaign-1779", "verb": "SERVES_IN", "note": "Participated in the campaign against the Iroquois"},
            {"target": "hamilton-fish", "verb": "PARENT_OF", "note": "Father of Governor and Secretary of State Hamilton Fish"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 59 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
