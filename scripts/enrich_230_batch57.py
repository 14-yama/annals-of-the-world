#!/usr/bin/env python3
"""
Batch 57 — 8 entities: Paul Boudet, Pedro Domingo Murillo,
René-Édouard Caron, Robert Wright, Johann Samuel Traugott Gehler,
Jonas Galusha, Joseph Chalier, Benjamin Ames
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

    ("paul-boudet", {
        "summary": (
            "Paul Boudet (1777–1836) was a French jurist "
            "and politician who served as a member of "
            "the Chamber of Deputies and as a legal "
            "official under the Restoration and July "
            "Monarchy. His career represented the "
            "continuity of professional legal culture "
            "across France's successive post-Revolutionary "
            "regimes — the ability of trained lawyers "
            "and judicial administrators to maintain "
            "institutional positions through the "
            "Bourbon Restoration and the July "
            "Revolution of 1830.\n\n"
            "Boudet was trained in law and built "
            "his career within France's expanding "
            "administrative and judicial bureaucracy "
            "during the Napoleonic and Restoration "
            "periods. The Napoleonic Code and its "
            "associated legal institutions created "
            "an enormous demand for trained jurists "
            "who could staff the prefectural councils, "
            "courts of appeal, and legislative chambers "
            "of post-Revolutionary France.\n\n"
            "His service in the Chamber of Deputies "
            "placed him in the legislative body that "
            "navigated the constitutional tensions "
            "of the Restoration — the struggle "
            "between the Charter of 1814's "
            "constitutional monarchy and the "
            "ultra-royalist ambitions of Charles X's "
            "court, tensions that ultimately produced "
            "the July Revolution of 1830 and the "
            "more liberal regime of Louis-Philippe.\n\n"
            "His career illustrated the adaptability "
            "of France's legal professional class "
            "through the transformations of the "
            "Restoration era."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "French jurist and deputy under the Restoration and July Monarchy; representative of the professional legal class that maintained institutional continuity across France's successive post-Revolutionary regimes; served in the Chamber of Deputies during the constitutional tensions of the Restoration period.",
            "significanceCategory": "local"
        },
        "causes": [
            "The Napoleonic Code's creation of a unified French legal system — requiring an enormous corps of trained lawyers, judges, and administrative officials — produced the professional infrastructure in which Boudet built his legal career across the Napoleonic and Restoration periods",
            "The Bourbon Restoration's constitutional settlement — the Charter of 1814 establishing a constitutional monarchy with an elected Chamber of Deputies — created the legislative institution in which jurists and professional men like Boudet participated in the constrained parliamentary politics of post-Napoleonic France",
            "The political turbulence of the Restoration — the oscillation between liberal and ultra-royalist governments, the tensions over press freedom and electoral law that culminated in the July Revolution of 1830 — defined the constitutional environment in which Boudet's legislative service took place"
        ],
        "effects": [
            "His legislative service contributed to the Chamber of Deputies' functioning during the Restoration's most politically contested years — the debates over electoral law, press freedom, and the constitutional balance between royal prerogative and parliamentary representation",
            "His career illustrated the continuity of France's legal professional class across regime changes — demonstrating how trained jurists maintained their institutional positions and professional relevance regardless of which dynasty or constitution governed France",
            "His adaptation to the July Monarchy after 1830 illustrated the political flexibility of France's administrative and legal middle class — the professional strata that survived by serving the state's institutional needs rather than personal loyalty to particular regimes",
            "His legal career contributed to the development of French administrative and judicial practice during the critical post-Napoleonic generation — when the Napoleonic Code's principles were being applied to the social and economic realities of Restoration France"
        ],
        "relationships": [
            {"target": "chamber-of-deputies-france", "verb": "SERVES_IN", "note": "Deputy during the Restoration and July Monarchy"},
            {"target": "bourbon-restoration", "verb": "SERVES_DURING", "note": "Legal official under Restoration governance"},
            {"target": "july-monarchy", "verb": "SERVES_DURING", "note": "Continues career under Louis-Philippe"},
            {"target": "napoleonic-code", "verb": "APPLIES", "note": "Jurist trained within the Napoleonic legal system"},
            {"target": "charter-of-1814", "verb": "SERVES_UNDER", "note": "Deputy under the Restoration constitutional charter"}
        ]
    }),

    ("pedro-domingo-murillo", {
        "summary": (
            "Pedro Domingo Murillo (1757–1810) was a "
            "Bolivian revolutionary and one of the first "
            "martyrs of Latin American independence — "
            "a creole leader whose 1809 uprising in "
            "La Paz, Upper Peru (modern Bolivia) was "
            "one of the earliest insurrections against "
            "Spanish colonial rule in South America. "
            "Hanged by Spanish colonial authorities "
            "in January 1810, his final words — "
            "'I die, but the torch I have lit no "
            "one shall extinguish' — became a motto "
            "of the independence movements that "
            "continued his work and ultimately "
            "achieved liberation fifteen years later.\n\n"
            "Murillo was born in La Paz to a creole "
            "family and built a modest career as "
            "a merchant and minor official within "
            "the colonial system. The Enlightenment "
            "ideas spreading through Spanish America, "
            "the example of the North American "
            "independence (1776), and the chaos "
            "created by Napoleon's invasion of "
            "Spain (1808) — which left the empire "
            "without a legitimate monarch — "
            "created the ideological and political "
            "conditions for the 1809 uprising.\n\n"
            "On 16 July 1809, Murillo led the "
            "creole junta that overthrew Spanish "
            "authority in La Paz — proclaiming "
            "that Upper Peru's people had the "
            "right to self-governance. The uprising "
            "was suppressed within months, and "
            "Murillo was captured, tried for treason, "
            "and executed.\n\n"
            "He is venerated as a national hero "
            "of Bolivia, with the main square "
            "of La Paz named Plaza Murillo in his honor."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Bolivian revolutionary and first martyr of the Latin American independence movements; led the 1809 La Paz uprising — one of the earliest insurrections against Spanish colonial rule in South America; executed January 1810; his final words became a motto of independence; national hero of Bolivia with La Paz's main square named in his honor.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Napoleon's invasion of Spain (1808) and the placement of Joseph Bonaparte on the Spanish throne — which stripped the colonial empire of its legitimate monarchical authority and created a constitutional crisis that gave colonial creoles ideological justification for claiming self-governance in the name of the legitimate king Ferdinand VII",
            "The Enlightenment ideas circulating through Spanish America — natural rights philosophy, constitutional theory, and the examples of North American and French revolutionary republicanism — provided the ideological framework through which Murillo and his fellow conspirators conceptualized their right to self-governance",
            "The social and economic grievances of Upper Peru's creole population — restricted from the highest colonial offices, subjected to Bourbon administrative reforms that increased colonial taxation and administrative control, and resentful of the peninsulares' monopoly on power — created the constituency for a creole revolt against the viceregal system"
        ],
        "effects": [
            "His 1809 La Paz uprising was one of the first declarations of independence in Spanish South America — preceding the major independence movements by a decade and demonstrating that creole resistance to Spanish authority had genuine popular support in Upper Peru",
            "His execution and martyrdom provided a potent symbolic focus for the independence movements that followed — his famous final words became a rallying cry that framed the independence struggle as the continuation of his unfinished work",
            "His uprising and its suppression demonstrated both the initial military weakness of the independence movements and the determination of Spanish colonial authorities to maintain control — knowledge that informed the military strategies of later independence leaders like Bolívar and San Martín",
            "His legacy as a national hero shaped Bolivian national identity after independence — with Plaza Murillo in La Paz becoming the symbolic center of the Bolivian state and his image deployed as a founding figure of Bolivian nationhood"
        ],
        "relationships": [
            {"target": "bolivian-independence", "verb": "INITIATES", "note": "First martyr and insurrectionist of Bolivian independence"},
            {"target": "la-paz-junta-1809", "verb": "LEADS", "note": "Led the July 16, 1809 creole junta in La Paz"},
            {"target": "spanish-colonial-rule", "verb": "REVOLTS_AGAINST", "note": "Overthrew Spanish authority briefly before capture and execution"},
            {"target": "latin-american-independence-movements", "verb": "PRECEDES", "note": "1809 uprising preceded the major independence movements by a decade"},
            {"target": "napoleon-invasion-of-spain", "verb": "INSPIRED_BY", "note": "Colonial crisis created by Napoleon's 1808 invasion enabled the uprising"}
        ]
    }),

    ("rené-édouard-caron", {
        "summary": (
            "René-Édouard Caron (1800–1876) was a "
            "Canadian lawyer, politician, and jurist "
            "from Quebec who served as Mayor of "
            "Quebec City (1834–1836, 1840–1846), "
            "Speaker of the Legislative Council "
            "of the Province of Canada, and "
            "Lieutenant Governor of Quebec (1873–1876). "
            "His career traced the full arc of "
            "Canadian political development from "
            "the turbulent 1830s and the 1837–1838 "
            "Rebellions through Confederation in "
            "1867 and into the early Dominion era — "
            "making him one of Quebec's most "
            "enduring and adaptable political figures.\n\n"
            "Caron was born in Quebec City and "
            "trained as a lawyer before entering "
            "politics. His mayoralty of Quebec City "
            "placed him at the head of Canada's "
            "oldest and most historically significant "
            "city — the former capital of New France "
            "and still the symbolic and administrative "
            "heart of French Canada.\n\n"
            "He navigated the period of the 1837–1838 "
            "Lower Canada Rebellion and Lord Durham's "
            "controversial Report recommending the "
            "assimilation of French Canada — a "
            "political crisis that shaped the "
            "union of Upper and Lower Canada "
            "into the Province of Canada (1841).\n\n"
            "His later service as Lieutenant Governor "
            "of Quebec made him a key figure in "
            "the new Canadian federal framework "
            "after Confederation."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Quebec City Mayor (1834–1846), Speaker of the Legislative Council of Canada, and Lieutenant Governor of Quebec (1873–1876); navigated the 1837 Rebellions, the Durham Report, and Confederation; one of Quebec's most enduring political figures across the colonial, union, and Dominion eras.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The 1837–1838 Lower Canada Rebellion and the political crisis it generated — Lord Durham's controversial report recommending the assimilation of French Canada, the Act of Union 1841 merging Upper and Lower Canada — created the charged political environment in which Caron's mayoralty of Quebec City and his subsequent career in the Province of Canada's institutions took shape",
            "Quebec City's strategic importance as the former capital of New France and the symbolic center of French-Canadian identity — making its mayoralty a politically significant position that required managing the tensions between the French-Canadian majority and the British colonial administration — shaped the political challenges of Caron's mayoral tenures",
            "Canadian Confederation (1867) and the creation of the Dominion of Canada — with Quebec established as one of the four original provinces — created the new federal constitutional framework within which Caron's later career as Lieutenant Governor took place"
        ],
        "effects": [
            "His two mayoral tenures in Quebec City during the turbulent 1834–1846 period helped maintain civic order and administration in French Canada's most important city through the 1837 Rebellion, the Durham Report crisis, and the transition to the United Province of Canada",
            "His service as Speaker of the Legislative Council provided Quebec's French-Canadian political community with representation and voice in the Province of Canada's upper chamber — an important institutional presence during the contested politics of the union era",
            "His Lieutenant Governorship (1873–1876) helped establish the relationship between Quebec's provincial government and the federal Crown in the new Confederation framework — navigating the still-settling constitutional arrangements of the Dominion's first decade",
            "His long career contributed to the development of Quebec's political institutions from colonial municipality to confederation partner — making him a figure of institutional continuity in Quebec's transition from colonial to self-governing status"
        ],
        "relationships": [
            {"target": "quebec-city", "verb": "GOVERNS", "note": "Mayor of Quebec City 1834–1836 and 1840–1846"},
            {"target": "province-of-canada", "verb": "SERVES_IN", "note": "Speaker of the Legislative Council"},
            {"target": "quebec-province", "verb": "GOVERNS", "note": "Lieutenant Governor of Quebec 1873–1876"},
            {"target": "canadian-confederation-1867", "verb": "SERVES_THROUGH", "note": "Career spanned the Confederation era"},
            {"target": "lower-canada-rebellion-1837", "verb": "NAVIGATES", "note": "Mayor during the 1837 Rebellion crisis"}
        ]
    }),

    ("robert-wright", {
        "summary": (
            "Robert Wright (1752–1826) was an American "
            "lawyer and Democratic-Republican politician "
            "from Maryland who served in both houses "
            "of the U.S. Congress — as U.S. Senator "
            "(1801–1806) and as a member of the "
            "U.S. House of Representatives "
            "(1810–1817) — as well as Governor "
            "of Maryland (1806–1809). His career "
            "placed him among the Maryland "
            "Democratic-Republicans who supported "
            "Jefferson's and Madison's administrations "
            "through the party's most politically "
            "dominant era — the years between "
            "the defeat of Federalism and the "
            "party's own eventual fracture.\n\n"
            "Wright was born in Cecil County, Maryland "
            "and trained as a lawyer before entering "
            "Maryland's political life. Maryland's "
            "political culture in the early republic "
            "balanced between the coastal tobacco-"
            "planting elite, the emerging commercial "
            "interests of Baltimore, and the "
            "small-farming population of the interior "
            "— a diverse electorate that the "
            "Democratic-Republicans cultivated "
            "successfully after 1800.\n\n"
            "His Senate service (1801–1806) coincided "
            "with Jefferson's presidency — the "
            "Louisiana Purchase, the repeal of "
            "the Judiciary Act, and the first "
            "application of Jeffersonian fiscal "
            "and foreign policy principles. His "
            "governorship and subsequent House "
            "service spanned the Madison years "
            "and the War of 1812.\n\n"
            "He represented the Southern states'-rights "
            "wing of Jeffersonian Democracy."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Maryland Democratic-Republican politician who served as U.S. Senator (1801–1806), Governor of Maryland (1806–1809), and U.S. Representative (1810–1817); Jeffersonian politician through the Louisiana Purchase and War of 1812 eras; representative of the Southern Democratic-Republican tradition.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Democratic-Republican Party's electoral victory in 1800 — the 'Revolution of 1800' that brought Jefferson to the presidency and ended Federalist dominance — created the political environment in which Maryland's Democratic-Republican politicians like Wright could build careers across Senate, gubernatorial, and House offices",
            "Maryland's complex political geography — balancing slaveholding tobacco planters in the Chesapeake tidewater with Baltimore's commercial interests and the western counties' small farming population — shaped the coalitional politics that Democratic-Republicans had to navigate to maintain Maryland's support in national elections",
            "The War of 1812 and the Madison administration's foreign policy — particularly the trade embargo policies and the conflict with Britain — created the major legislative and executive challenges of Wright's gubernatorial and House-member years, requiring Maryland politicians to manage the war's economic impact on Maryland's Atlantic commerce"
        ],
        "effects": [
            "His Senate service contributed to the Jeffersonian legislative program — voting on the Louisiana Purchase, the repeal of the Federalist Judiciary Act, and the fiscal and commercial policies that defined Jefferson's first term",
            "His Maryland governorship managed the state's transition through the politically charged middle years of the Jeffersonian era — maintaining Democratic-Republican dominance in a state where Federalism had retained some strength",
            "His House service through 1817 contributed to the Madison Congress's navigation of the War of 1812 and the post-war Era of Good Feelings — the period of Democratic-Republican dominance preceding the party's eventual fracture into Jacksonian and National Republican factions",
            "His career contributed to Maryland's Democratic tradition — establishing the pattern of Southern state loyalty to Jeffersonian principles that would characterize Maryland's politics through the Jacksonian era"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Maryland Senator 1801–1806"},
            {"target": "maryland", "verb": "GOVERNS", "note": "Governor of Maryland 1806–1809"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Maryland Representative 1810–1817"},
            {"target": "thomas-jefferson", "verb": "SUPPORTS", "note": "Jeffersonian Democratic-Republican Senator"},
            {"target": "war-of-1812", "verb": "SERVES_DURING", "note": "Governor and Congressman through the War of 1812"}
        ]
    }),

    ("johann-samuel-traugott-gehler", {
        "summary": (
            "Johann Samuel Traugott Gehler (1751–1795) "
            "was a German physicist and natural "
            "philosopher whose major contribution "
            "to European science was the "
            "Physikalisches Wörterbuch (Physical "
            "Dictionary), a multi-volume systematic "
            "encyclopedia of physics and natural "
            "philosophy that became a standard "
            "reference work in German-speaking "
            "Europe in the late eighteenth century. "
            "This encyclopedic work systematized "
            "the rapidly expanding body of "
            "Enlightenment natural philosophy and "
            "made the physical sciences accessible "
            "to educated German readers at precisely "
            "the moment when natural philosophy "
            "was transforming into modern physics.\n\n"
            "Gehler was born in Leipzig and built "
            "his career there — at the University "
            "of Leipzig, one of the oldest and "
            "most distinguished universities "
            "in the Holy Roman Empire, whose "
            "faculties included major figures "
            "in German Enlightenment thought. "
            "His legal and natural philosophy "
            "training connected him to the "
            "broad Enlightenment culture "
            "of late eighteenth-century Leipzig.\n\n"
            "The Physikalisches Wörterbuch — "
            "published in multiple volumes "
            "between 1787 and 1795 — systematized "
            "the physical sciences in German at "
            "a time when French encyclopédistes "
            "had established the model of "
            "systematic scientific dictionaries "
            "but German equivalents were lacking.\n\n"
            "His work provided the German-speaking "
            "scientific community with a comprehensive "
            "reference to contemporary physics."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "German natural philosopher and author of the Physikalisches Wörterbuch (1787–1795) — a major systematic encyclopedia of physics in German that served as a standard reference for the German scientific community; contributed to the systematization and diffusion of Enlightenment natural philosophy in German-speaking Europe.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The French Encyclopédie's model of systematic scientific knowledge organization — demonstrating that comprehensive reference works could systematize and diffuse Enlightenment knowledge across educated society — inspired the German encyclopedic tradition in which Gehler's Physikalisches Wörterbuch represented the natural philosophy component",
            "The rapid expansion of experimental physics in the mid-to-late eighteenth century — the discoveries in electricity (Franklin, Volta), chemistry (Lavoisier), optics, and mechanics — created an overwhelming body of new knowledge that required systematic organization if educated scientists and practitioners were to master it",
            "The German Enlightenment's institutional culture — particularly the universities and learned societies of the Holy Roman Empire that valued systematic knowledge organization and encyclopedic scholarship — provided both the institutional home and the readership for Gehler's comprehensive physics reference work"
        ],
        "effects": [
            "The Physikalisches Wörterbuch became a standard reference work for German-speaking scientists, engineers, and educated readers in the late eighteenth and early nineteenth centuries — helping to systematize and diffuse the rapidly expanding body of natural philosophy",
            "His encyclopedic work contributed to the professionalization of German natural philosophy — providing the terminological standardization and conceptual organization that were prerequisites for physics to develop as a distinctly German scientific tradition in the early nineteenth century",
            "The work was later continued and expanded by other German scientists — indicating its importance as a foundational reference that remained relevant enough to warrant updating as the physical sciences continued to develop",
            "His career at Leipzig contributed to the development of natural philosophy education there — at a university that would later become one of the centers of nineteenth-century German physics education and research"
        ],
        "relationships": [
            {"target": "university-of-leipzig", "verb": "SERVES_AT", "note": "Natural philosopher at Leipzig"},
            {"target": "physikalisches-worterbuch", "verb": "AUTHORS", "note": "Compiled the major German physics encyclopedia (1787–1795)"},
            {"target": "german-enlightenment", "verb": "CONTRIBUTES_TO", "note": "Major German scientific encyclopedist"},
            {"target": "french-encyclopedie", "verb": "FOLLOWS_MODEL_OF", "note": "German physics dictionary modeled on French encyclopedic tradition"},
            {"target": "european-scientific-revolution", "verb": "SYSTEMATIZES", "note": "Organized rapidly expanding body of Enlightenment natural philosophy"}
        ]
    }),

    ("jonas-galusha", {
        "summary": (
            "Jonas Galusha (1753–1834) was an American "
            "Revolutionary War veteran and Democratic-"
            "Republican politician who served as "
            "Governor of Vermont for eight non-"
            "consecutive terms (1809–1813, 1815–1820) "
            "— making him one of the longest-serving "
            "governors in Vermont's early history. "
            "His political longevity reflected his "
            "deep roots in Vermont's Jeffersonian "
            "Republican culture and his ability "
            "to represent Vermont's rural, "
            "farming population against the "
            "commercial and Federalist interests "
            "associated with Vermont's mercantile towns.\n\n"
            "Galusha was born in Connecticut and "
            "served in the Continental Army during "
            "the Revolution before settling in "
            "Shaftsbury, Vermont. Vermont was "
            "an unusual state — admitted to the "
            "Union in 1791 as the first state "
            "after the original thirteen — "
            "with a strongly independent political "
            "culture shaped by the Green Mountain "
            "Boys tradition and a farming population "
            "suspicious of centralized authority.\n\n"
            "His gubernatorial tenures spanned "
            "the War of 1812 period — a war "
            "that was deeply unpopular in Vermont "
            "and other New England states, where "
            "the trade embargo devastated the "
            "commercial economy and where some "
            "Federalists flirted with the idea "
            "of secession at the Hartford Convention.\n\n"
            "His years in office cemented Democratic-"
            "Republican dominance in Vermont."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Vermont Governor for eight terms (1809–1820); Revolutionary War veteran and Jeffersonian Democratic-Republican; one of Vermont's longest-serving early governors; presided over Vermont during the War of 1812 — a period of commercial disruption and anti-war sentiment in New England.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Vermont's strongly Jeffersonian Republican political culture — rooted in its farming population's suspicion of centralized authority, its Green Mountain Boys tradition of local independence, and its hostility to the commercial Federalism associated with New England's merchant class — created the electoral constituency that repeatedly returned Galusha to the governorship",
            "The War of 1812 and the Jefferson-Madison trade embargo policies — which devastated Vermont's commercial economy dependent on British-Canadian trade, angered the farming population, and created political tensions between Republican loyalty to the national administration and Vermont's economic interests — defined the major challenges of Galusha's gubernatorial years",
            "Vermont's post-Revolutionary political culture's emphasis on citizen-soldier values and the veneration of Continental Army veterans — of which Galusha was one — gave Revolutionary War service a strong legitimating function in Vermont politics that sustained support for veteran politicians across multiple electoral cycles"
        ],
        "effects": [
            "His eight gubernatorial terms cemented Democratic-Republican dominance in Vermont during the critical years when the national party was achieving political dominance following the collapse of Federalism — ensuring that Vermont remained in the Jeffersonian coalition",
            "His governance of Vermont during the War of 1812 managed the state's difficult navigation between loyalty to the national Republican administration and Vermont's commercial interests — maintaining political order despite the war's economic disruption",
            "His long gubernatorial service contributed to the development of Vermont's state governmental institutions — the administrative practices, legislative relationships, and executive precedents that characterized Vermont's early statehood",
            "His political career contributed to the Vermont Democratic-Republican tradition that would eventually evolve into the Jacksonian Democratic and anti-Jacksonian Whig factions of the second American party system"
        ],
        "relationships": [
            {"target": "vermont", "verb": "GOVERNS", "note": "Governor of Vermont for eight terms 1809–1820"},
            {"target": "continental-army", "verb": "SERVES_IN", "note": "Revolutionary War veteran"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "Jeffersonian Democrat representing Vermont farming interests"},
            {"target": "war-of-1812", "verb": "GOVERNS_DURING", "note": "Vermont Governor during the unpopular War of 1812"},
            {"target": "thomas-jefferson", "verb": "SUPPORTS", "note": "Jeffersonian Republican loyal to Madison administration"}
        ]
    }),

    ("joseph-chalier", {
        "summary": (
            "Joseph Chalier (1747–1793) was a French "
            "Revolutionary radical and Jacobin agitator "
            "in Lyon who became known as the 'Lyon "
            "Robespierre' for his fierce democratic "
            "and egalitarian politics. His execution "
            "by Lyon's Girondin-aligned municipal "
            "government in July 1793 — before the "
            "Jacobin-led National Convention suppressed "
            "the Lyon federalist revolt — made him "
            "a martyr of Jacobin radicalism whose "
            "death was used to justify the brutal "
            "Jacobin repression of Lyon that followed: "
            "the systematic terror of Fouché and "
            "Collot d'Herbois that killed hundreds "
            "of Lyonnais.\n\n"
            "Chalier was born in the Piedmont region "
            "and built a career as a merchant before "
            "the Revolution transformed him into "
            "a radical political agitator. In Lyon, "
            "France's second city and a center of "
            "silk manufacturing, he championed "
            "the sans-culottes against the city's "
            "wealthy merchant oligarchy and "
            "advocated measures that went further "
            "left than even the Jacobin mainstream.\n\n"
            "When Lyon's Girondin-allied faction "
            "took control of the city government, "
            "Chalier was arrested, tried for "
            "sedition, and guillotined on "
            "16 July 1793.\n\n"
            "His martyrdom became the ideological "
            "justification for the Convention's "
            "savage retribution against Lyon."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "The 'Lyon Robespierre' — radical Jacobin leader in Lyon executed by the Girondin municipal government in July 1793; his martyrdom became the justification for the Jacobin Convention's brutal repression of Lyon, which killed hundreds; important figure in the Federalist revolt crisis and the Terror's application to provincial France.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Lyon's social tensions between the wealthy silk-manufacturing merchant oligarchy and the city's large working class of silk weavers (canuts) and urban poor — who suffered from wage suppression, price inflation, and the economic disruptions of the Revolutionary period — created the constituency for Chalier's radical Jacobin politics",
            "The Girondins' challenge to the Jacobin Convention's authority — the federalist revolt of 1793, in which provincial cities including Lyon, Marseille, and Bordeaux resisted the Paris Jacobins' centralization of Revolutionary authority — created the conflict within which Lyon's Girondin faction eliminated their radical Jacobin opponents including Chalier",
            "The Revolutionary radicalization process — in which the demands of the war against the European powers, the internal counter-revolution, and the food crisis drove successive governments further left while simultaneously creating violent factional conflicts — placed Chalier at the extreme end of Lyon's Revolutionary politics"
        ],
        "effects": [
            "His execution by Lyon's Girondin government became the ideological cornerstone of the Jacobin Convention's justification for the brutal Siege and Terror of Lyon — the systematic repression carried out by Fouché and Collot d'Herbois in 1793–1794, which killed an estimated 1,900 Lyonnais",
            "His martyrdom was deployed by the Jacobin Convention as evidence that the federalist revolt was not merely a political disagreement but a counter-revolutionary assault on the radical democracy that Chalier represented — justifying the most savage application of the Terror to any French provincial city",
            "His political career in Lyon documented the extreme radicalism that developed in major provincial French cities during the early Revolution — demonstrating that the social conflicts driving revolutionary politics were not merely a Parisian phenomenon but had deep roots in France's urban working class",
            "His name became one of the revolutionary martyrs celebrated in the civic cult of the Terror — his image used in propaganda alongside Marat to frame the Jacobin cause as the defense of the oppressed against their oppressors"
        ],
        "relationships": [
            {"target": "lyon", "verb": "LEADS_RADICALS_IN", "note": "'Lyon Robespierre' — radical Jacobin leader in France's second city"},
            {"target": "jacobin-club", "verb": "MEMBER_OF", "note": "Radical Jacobin agitator aligned with the Parisian Montagnards"},
            {"target": "girondin-faction", "verb": "OPPOSES", "note": "Executed by Lyon's Girondin-aligned municipal government"},
            {"target": "federalist-revolt-1793", "verb": "VICTIM_OF", "note": "Killed during the Lyon federalist revolt"},
            {"target": "terror-of-lyon", "verb": "MARTYR_FOR", "note": "Death used to justify Fouché and Collot's brutal repression of Lyon"}
        ]
    }),

    ("benjamin-ames", {
        "summary": (
            "Benjamin Ames (1788–1836) was an American "
            "politician from Maine who served as a "
            "Democratic-Republican member of the "
            "U.S. House of Representatives (1829–1831), "
            "representing a Maine district during "
            "the transition from the Era of Good "
            "Feelings to Jacksonian Democracy. His "
            "congressional career coincided with "
            "the opening of Andrew Jackson's first "
            "presidential term — the administration's "
            "battle against the Bank of the United "
            "States, the Indian Removal Act of 1830, "
            "and the emergence of the spoils system "
            "as an explicit principle of American "
            "patronage politics.\n\n"
            "Ames was born in Massachusetts and "
            "eventually settled in Maine — which "
            "became a separate state from Massachusetts "
            "in 1820 as part of the Missouri Compromise's "
            "Maine-Missouri paired admission that "
            "maintained the balance between free "
            "and slave states. Maine's early statehood "
            "was thus directly connected to the "
            "sectional compromises over slavery "
            "that would define American politics "
            "for the next four decades.\n\n"
            "His congressional service was brief "
            "— a single term — but placed him "
            "in the House during the initial "
            "Jacksonian legislative agenda's "
            "most consequential moments.\n\n"
            "He represented Maine's Democratic "
            "political tradition that aligned "
            "with Jacksonian populism and states' "
            "rights against the National Republican "
            "alternative."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Maine Democratic Congressman (1829–1831) serving during the opening of Jackson's presidency; member of the House during the Indian Removal Act and Bank War debates; representative of Maine's Jacksonian Democratic tradition in the new state's early political development.",
            "significanceCategory": "local"
        },
        "causes": [
            "Maine's creation as a separate state from Massachusetts in 1820 — as part of the Missouri Compromise that admitted Missouri as a slave state and Maine as a free state — established the new political framework in which Maine's independent congressional delegation, including Ames, would participate in national politics",
            "The Jacksonian Democratic coalition's organization in the late 1820s — mobilizing resentment at the 1824 'corrupt bargain' and building a populist electoral machine based on universal white male suffrage, anti-banking sentiment, and states' rights — created the political environment in which Ames's House service as a Democrat took place",
            "Jackson's first-term legislative agenda — the Indian Removal Act, the assault on the Bank of the United States, the spoils system, and the nullification controversy — defined the major political battles of Ames's congressional term"
        ],
        "effects": [
            "His congressional service contributed to Maine's representation in the Jacksonian Congress during the pivotal opening of Jackson's transformative presidency — a Congress that passed the Indian Removal Act and began the Bank War",
            "His brief career illustrated the rapid political transformation of New England during the Jacksonian period — as even traditionally Federalist New England states like Maine developed viable Jacksonian Democratic traditions competing with the National Republican alternative",
            "His alignment with Jacksonian Democracy contributed to Maine's Democratic political tradition — the foundation of the competitive two-party politics that made Maine a contested state in the presidential elections of the 1830s and 1840s",
            "His career represented the political generation that experienced the full transition from the first to the second American party system — entering politics in the Era of Good Feelings and serving through the emergence of Jacksonian mass democracy"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Maine Representative 1829–1831"},
            {"target": "maine", "verb": "REPRESENTS", "note": "Congressional representative from newly independent Maine"},
            {"target": "andrew-jackson", "verb": "SUPPORTS", "note": "Jacksonian Democrat in Jackson's first Congress"},
            {"target": "indian-removal-act-1830", "verb": "VOTES_ON", "note": "Congressman during the Indian Removal Act debates"},
            {"target": "missouri-compromise-1820", "verb": "POLITICAL_CONTEXT", "note": "Maine statehood created by Missouri Compromise that shaped his political era"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 57 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
