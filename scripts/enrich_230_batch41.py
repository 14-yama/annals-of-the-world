#!/usr/bin/env python3
"""
Batch 41 — 8 entities: John P. Gaines, Juan de Canaveris, Charles Jared Ingersoll,
Albion Parris, Morgan Lewis, Charles Loyseau, Richard Bland Lee, Enoch Lincoln
editorId: vscode-copilot
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

    # 1 — John P. Gaines
    ("john-p-gaines", {
        "summary": (
            "John Pollard Gaines (1795–1857) was an American military "
            "officer, Whig politician, and Kentucky enslaver — best "
            "known today as the enslaver of Margaret Garner, whose "
            "1856 act of killing her daughter rather than see her "
            "returned to slavery inspired Toni Morrison's novel "
            "'Beloved.' Born in Virginia, Gaines served in the "
            "Mexican-American War, was captured at the Battle of "
            "Canada Alamosa (1846) and held prisoner for months "
            "before exchange. His military service earned him "
            "election as a Whig to the US House of Representatives "
            "from Kentucky (1847–1849).\n\n"
            "Gaines was then appointed Governor of Oregon Territory "
            "(1850–1853) — a long posting that took him far from "
            "his Kentucky plantation, which he left under overseer "
            "management. The enslaved people held there — including "
            "Margaret Garner, her husband Simon, and their children "
            "— remained bound to his property under Kentucky law "
            "even as Gaines himself governed a free territory.\n\n"
            "Margaret Garner's story reached its terrible climax in "
            "January 1856, three years after Gaines had returned to "
            "Kentucky: she and her family escaped across the frozen "
            "Ohio River to Cincinnati. When federal marshals and "
            "Gaines's agents arrived to return them under the "
            "Fugitive Slave Act, Garner killed her two-year-old "
            "daughter with a butcher knife and attempted to kill her "
            "other children rather than see them taken back to slavery. "
            "Her trial was a national sensation and her story became "
            "the moral center of Toni Morrison's 'Beloved' (1987).\n\n"
            "Gaines died in 1857 as the nation moved toward the "
            "Civil War that would resolve what his property in human "
            "beings had helped crystallize."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Kentucky Whig congressman (1847–1849); Governor of Oregon Territory (1850–1853); enslaver of Margaret Garner — whose 1856 act of killing her daughter rather than see her returned to slavery inspired Toni Morrison's 'Beloved' (1987); captured at the Battle of Canada Alamosa in the Mexican-American War.",
            "significanceCategory": "regional"
        },
        "causes": [
            "His Mexican-American War service and capture at the Battle of Canada Alamosa (1846) — and the heroic narrative of his imprisonment and exchange — provided the political capital that earned him election to Congress and his subsequent appointment as Oregon territorial governor",
            "The Fugitive Slave Act of 1850 — which required the return of escaped enslaved people even from free states — was the legal mechanism that made Margaret Garner's recapture in Cincinnati legally enforceable and created the crisis that produced her act of infanticide",
            "The slave economy of antebellum Kentucky — and its dependence on enslaved labor even for modest planters — created the property relations that made Gaines the enslaver of Margaret Garner and her family, binding them to his economic interests across the continent"
        ],
        "effects": [
            "Margaret Garner's 1856 act — killing her daughter rather than see her returned to Gaines's slavery — became the most widely discussed individual act of resistance in the antebellum slavery debate, reprinted in abolitionist newspapers across the North and cited as evidence of slavery's dehumanizing logic",
            "Toni Morrison's 'Beloved' (1987) — inspired by Garner's story — became one of the most celebrated American novels of the 20th century, winning the Pulitzer Prize for Fiction in 1988 and permanently embedding Margaret Garner's name in American literary history, with Gaines serving as the institutional background of her enslavement",
            "His Oregon Territory governorship (1850–1853) placed him among the early territorial administrators of the Pacific Northwest — contributing to the governance of a territory that would become one of the most significant states of the American West",
            "The Garner case's national attention in 1856 contributed to the escalating sectional crisis: abolitionists used it as a concrete illustration of slavery's moral catastrophe, and its coverage in Northern newspapers strengthened the antislavery coalition in the elections that would produce Lincoln's presidency"
        ],
        "relationships": [
            {"entity": "Margaret Garner (enslaved; killed her daughter rather than return to slavery, 1856)", "relationship": "ENSLAVER_OF", "note": "Held Margaret Garner and her family in slavery on his Kentucky plantation — her 1856 escape to Cincinnati and killing of her daughter to prevent return to Gaines's slavery inspired Toni Morrison's 'Beloved'"},
            {"entity": "Toni Morrison's 'Beloved' (1987, Pulitzer Prize fiction)", "relationship": "ENSLAVER_WHOSE_PROPERTY_INSPIRED", "note": "His ownership of Margaret Garner provided the historical basis for the enslavement in Toni Morrison's 'Beloved' — the Pulitzer Prize-winning novel about a mother's act of love and horror"},
            {"entity": "Governor of Oregon Territory (1850–1853)", "relationship": "GOVERNOR", "note": "Served as Governor of Oregon Territory (1850–1853) while his Kentucky plantation — and the enslaved people held there — remained under overseer management"},
            {"entity": "Fugitive Slave Act (1850) / Garner recapture attempt (January 1856)", "relationship": "PROPERTY-HOLDER_WHOSE_AGENTS_INVOKED", "note": "Gaines's agents invoked the Fugitive Slave Act to recapture Margaret Garner in Cincinnati in January 1856 — triggering her act of killing her daughter rather than return to Kentucky"},
            {"entity": "US House of Representatives from Kentucky (Whig, 1847–1849)", "relationship": "CONGRESSMAN", "note": "Served as Whig US Representative from Kentucky (1847–1849) — elected partly on his Mexican-American War service and capture at the Battle of Canada Alamosa"}
        ]
    }),

    # 2 — Juan de Canaveris
    ("juan-de-canaveris", {
        "summary": (
            "Juan de Canaveris (c.1765–c.1835) was a Piedmontese-born "
            "lawyer and colonial official who served in Buenos Aires "
            "as an accounting officer in the Tribunal de Cuentas "
            "(Accounting Tribunal) of the Viceroyalty of Río de "
            "la Plata — and who achieved the rare distinction of "
            "being the only Italian-origin vecino (resident) of "
            "Buenos Aires to actively support the May Revolution "
            "of 1810, the revolutionary movement that launched "
            "Argentina's path to independence.\n\n"
            "Born in the Kingdom of Sardinia (Piedmont), Canaveris "
            "emigrated to the Río de la Plata and built a career "
            "within the Spanish colonial administrative apparatus, "
            "rising to a position of significant financial responsibility "
            "in the Tribunal de Cuentas — the institution responsible "
            "for auditing and controlling the viceroyalty's finances. "
            "His high social standing within colonial Buenos Aires "
            "made his revolutionary sympathies an unusual and "
            "specifically noted feature of the historical record.\n\n"
            "The May Revolution of May 1810 — which established "
            "the Primera Junta as Buenos Aires's first autonomous "
            "government — was led overwhelmingly by criollo "
            "(American-born Spanish) elites. Canaveris's participation "
            "as a vecino of Italian descent who formally supported "
            "the revolutionary government in the critical May days "
            "was distinctive enough to be recorded as the sole "
            "Italian-origin participant in the founding moment.\n\n"
            "His career illustrates the cosmopolitan character of "
            "late colonial Buenos Aires — a port city where Genoese, "
            "Basque, Catalan, Irish, and other non-Castilian "
            "European professionals built careers within the "
            "Spanish colonial system."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Piedmontese-born lawyer and accounting officer in the Tribunal de Cuentas of the Viceroyalty of Río de la Plata; the only Italian-origin vecino of Buenos Aires documented as a supporter of the May Revolution of 1810 that launched Argentine independence; illustrates the cosmopolitan character of late colonial Buenos Aires.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The May Revolution's ideological framework — drawing on Enlightenment principles and the precedent of the American and French Revolutions — was broad enough to attract support from European-born professionals like Canaveris who had built careers within the colonial system but saw opportunity in the new revolutionary order",
            "Canaveris's position in the Tribunal de Cuentas — giving him insider knowledge of the viceroyalty's fiscal machinery and political networks — created the institutional awareness that made his alignment with the revolutionary government potentially valuable to the Primera Junta",
            "Buenos Aires's cosmopolitan character as a port city and administrative capital of the Río de la Plata — with significant Genoese, Basque, and other non-Castilian European commercial and professional communities — created the social environment in which a Piedmontese official could achieve high status and participate in the colony's revolutionary moment"
        ],
        "effects": [
            "His documented support for the May Revolution contributed to the founding coalition of the Primera Junta — and his status as the sole Italian-origin supporter among the Buenos Aires vecinos made him a specifically noted figure in the historical documentation of Argentina's founding moment",
            "His career in the Tribunal de Cuentas contributed to the financial administration of the Viceroyalty of Río de la Plata during its transition from colonial rule to revolutionary autonomy — providing institutional continuity in the accounting and fiscal oversight apparatus",
            "His example illustrated that the Argentine independence movement was not purely a criollo ethnic project but could attract the support of European-born professionals of non-Spanish origin who had built careers in the colonial system and saw the revolutionary government as a legitimate successor",
            "His Piedmontese origins and Buenos Aires career contributed to the early history of Italian-descent communities in the Río de la Plata — communities that would become enormously significant in Argentine population and culture through 19th-century immigration"
        ],
        "relationships": [
            {"entity": "May Revolution of 1810 / Primera Junta (Argentine independence founding)", "relationship": "SOLE_ITALIAN-ORIGIN_VECINO_SUPPORTER_OF", "note": "The only Italian-origin resident of Buenos Aires documented as a formal supporter of the May Revolution — his support specifically noted in historical records as distinctive given the revolution's overwhelmingly criollo leadership"},
            {"entity": "Tribunal de Cuentas of the Viceroyalty of Río de la Plata (Buenos Aires)", "relationship": "ACCOUNTING_OFFICER", "note": "Served as accounting officer in the Tribunal de Cuentas — the institution responsible for auditing the viceroyalty's finances — a position of significant financial responsibility in colonial Buenos Aires"},
            {"entity": "Viceroyalty of Río de la Plata / late colonial Buenos Aires", "relationship": "HIGH-STATUS_COLONIAL_OFFICIAL", "note": "Achieved high social status within the viceroyalty's colonial administrative structure — making his revolutionary sympathies a specifically noted departure from the expected loyalty of senior colonial officials"},
            {"entity": "Italian / Piedmontese emigrant community in colonial Río de la Plata", "relationship": "NOTABLE_EARLY_MEMBER_OF", "note": "A notable early representative of the Italian-origin professional community in Buenos Aires — precursor to the massive Italian immigration that would transform Argentina in the 19th century"},
            {"entity": "Criollo revolutionary elite (Buenos Aires May 1810)", "relationship": "NON-CRIOLLO_SUPPORTER_OF", "note": "Supported the overwhelmingly criollo revolutionary movement as a European-born professional — illustrating the Buenos Aires revolution's capacity to attract broader European participation beyond its Spanish-descent core"}
        ]
    }),

    # 3 — Charles Jared Ingersoll
    ("charles-jared-ingersoll", {
        "summary": (
            "Charles Jared Ingersoll (1782–1862) was an American "
            "lawyer, author, and Democratic politician from "
            "Philadelphia who served multiple non-consecutive terms "
            "as US Representative from Pennsylvania (1813–1815, "
            "1841–1849) — one of the most durable Jacksonian Democratic "
            "figures in Pennsylvania congressional history. "
            "He was also one of the few Jacksonian-era politicians "
            "to achieve genuine recognition as a writer and literary "
            "figure alongside his political career.\n\n"
            "His most famous literary work was 'Inchiquin, the Jesuit's "
            "Letters' (1810) — a fictional epistolary defense of "
            "American culture written under the persona of a Mexican "
            "Jesuit traveling in the United States. The 'Inchiquin' "
            "letters argued forcefully against British condescension "
            "toward American civilization, provoking a transatlantic "
            "controversy when British critics responded with "
            "counter-attacks. The work established Ingersoll as "
            "an early champion of cultural American nationalism.\n\n"
            "His congressional career spanned the War of 1812 — "
            "as a War Hawk who supported aggressive prosecution "
            "of the conflict — and the Jacksonian-Whig battles "
            "over banking and tariffs. He was a firm backer of "
            "Andrew Jackson and Martin Van Buren and an opponent "
            "of the Second Bank of the United States. He also "
            "served as US District Attorney for Eastern Pennsylvania "
            "(1815–1829) — building his legal career between "
            "congressional stints.\n\n"
            "He wrote extensively in his later years — historical "
            "and biographical works on the War of 1812 — and remained "
            "an active Democrat into his 70s, dying in 1862 "
            "as the Civil War he had long feared tore the nation apart."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Pennsylvania Democratic congressman (1813–1815, 1841–1849); author of 'Inchiquin, the Jesuit's Letters' (1810) — an early American cultural nationalist manifesto that provoked transatlantic controversy; US District Attorney for Eastern Pennsylvania (1815–1829); War of 1812 War Hawk; Jacksonian Democrat aligned with Jackson and Van Buren.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The War of 1812's political polarization — between War Hawks who saw the conflict as a necessary assertion of American sovereignty and Federalists who opposed it — created the partisan environment that drove Ingersoll's initial congressional election and his War Hawk legislative positions",
            "The post-Revolutionary cultural anxiety about American civilization's standing relative to Britain — manifest in British travelers' condescending accounts of American manners, culture, and institutions — provided the intellectual provocation that Ingersoll's 'Inchiquin' letters were designed to refute",
            "Philadelphia's position as Pennsylvania's commercial and cultural capital — and its Federalist-to-Democratic political evolution from the 1790s through the Jacksonian era — created the urban professional constituency that sustained Ingersoll's multiple congressional campaigns"
        ],
        "effects": [
            "'Inchiquin, the Jesuit's Letters' (1810) contributed to the early American cultural nationalist debate — establishing a template for American literary self-defense against British cultural condescension that influenced later American literary nationalism",
            "His War of 1812 congressional service — as a War Hawk supporter of aggressive prosecution — contributed to the political coalition that sustained Madison's war policy through its most difficult years",
            "His 14-year tenure as US District Attorney for Eastern Pennsylvania (1815–1829) shaped federal law enforcement in Pennsylvania's most populous district during the era of the Second Bank controversy and early industrial development",
            "His political history writings on the War of 1812 — including multi-volume accounts published in his later career — contributed to the documentary record of a conflict whose historiography was actively contested between American and British nationalist interpretations"
        ],
        "relationships": [
            {"entity": "US House of Representatives from Pennsylvania (1813–1815, 1841–1849)", "relationship": "MULTI-TERM_DEMOCRATIC_CONGRESSMAN", "note": "Served multiple non-consecutive terms in Congress — as a War Hawk (1813–1815) and as a Jacksonian Democrat (1841–1849)"},
            {"entity": "'Inchiquin, the Jesuit's Letters' (1810)", "relationship": "AUTHOR_OF", "note": "Authored the fictional epistolary defense of American culture — written under a Mexican Jesuit persona — that provoked a transatlantic controversy and established him as a cultural American nationalist"},
            {"entity": "Andrew Jackson / Jacksonian Democratic movement", "relationship": "FIRM_POLITICAL_SUPPORTER_OF", "note": "A committed Jacksonian Democrat — backing Jackson, Van Buren, and the Democratic coalition's opposition to the Second Bank and Whig economic nationalism"},
            {"entity": "US District Attorney for Eastern Pennsylvania (1815–1829)", "relationship": "FEDERAL_PROSECUTOR", "note": "Served as US District Attorney for Eastern Pennsylvania for 14 years — building his legal career and federal institutional ties between congressional stints"},
            {"entity": "War of 1812 / War Hawk congressional faction", "relationship": "WAR_HAWK_SUPPORTER_OF", "note": "Served as a War Hawk in the 13th Congress — supporting aggressive prosecution of the War of 1812 against British impressment and maritime interference"}
        ]
    }),

    # 4 — Albion Parris
    ("albion-parris", {
        "summary": (
            "Albion Keith Parris (1788–1857) had one of the most "
            "varied public careers of any figure in early 19th-century "
            "American history — spanning nearly every branch of both "
            "state and federal government across four decades. Born "
            "in Hebron, Maine (then part of Massachusetts), he served "
            "successively as US Representative from the District of "
            "Maine (1815–1818), 5th Governor of Maine (1822–1827), "
            "US Senator from Maine (1827–1828), Associate Justice "
            "of the Maine Supreme Judicial Court (1828–1836), US "
            "District Judge for the District of Maine (1836–1844), "
            "and 2nd Comptroller of the US Treasury (1836–1850).\n\n"
            "His governorship (1822–1827) was the most politically "
            "prominent phase of his career: he led Maine through "
            "its first years as an independent state — separated "
            "from Massachusetts in 1820 as part of the Missouri "
            "Compromise — and presided over the state's early "
            "economic development during the Era of Good Feelings "
            "and the beginning of the Jacksonian political "
            "realignment. He was a Democratic-Republican aligned "
            "with the Crawford faction before transitioning to "
            "Jacksonian Democracy.\n\n"
            "His subsequent careers as federal judge and Comptroller "
            "represented a transition from elected politician to "
            "appointed official — transforming him from a partisan "
            "figure into a federal institutional servant whose "
            "longevity in office (14 years as Comptroller) outlasted "
            "multiple administrations.\n\n"
            "His career illustrated the career patterns of the early "
            "American republic in which a single capable lawyer "
            "could move fluidly between state and federal executive, "
            "legislative, and judicial positions over a lifetime."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "5th Governor of Maine (1822–1827); US Representative from District of Maine (1815–1818); US Senator from Maine (1827–1828); Associate Justice of Maine Supreme Judicial Court; US District Judge for Maine; 2nd Comptroller of the US Treasury (1836–1850); career spanning nearly every branch of state and federal government.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Maine's separation from Massachusetts in 1820 — as part of the Missouri Compromise — created the new state's need for experienced political and legal figures who could build its institutional apparatus from scratch, elevating Parris's career opportunities dramatically",
            "The Era of Good Feelings' factional collapse — and the transition from Crawford Democratic-Republicanism to Jacksonian Democracy — required New England politicians like Parris to navigate shifting alliances that determined career trajectories in the new party system",
            "Parris's Dartmouth education and legal training — combined with his early congressional service — provided the credentials and connections that made him eligible for the successive gubernatorial, senatorial, judicial, and federal appointive positions that characterized his unusually varied career"
        ],
        "effects": [
            "His five-year governorship (1822–1827) provided Maine with experienced executive leadership during its critical founding decade — establishing administrative patterns and political precedents for the new state's governance",
            "His 14-year tenure as 2nd Comptroller of the US Treasury (1836–1850) contributed to the federal financial administration apparatus during the most turbulent decades of American economic history — including the Panic of 1837, the era of independent treasury debates, and the Mexican-American War",
            "His career trajectory — from congressman to governor to senator to judge to federal comptroller — illustrated the fluid movement between branches that characterized early American political careers and the relative absence of rigid separation between executive, legislative, and judicial roles in the founding era",
            "Maine's early political consolidation under Parris's governorship contributed to the state's rapid development as a timber and maritime economy — and its political alignment as a Jacksonian state that would remain strongly Democratic through much of the antebellum era"
        ],
        "relationships": [
            {"entity": "5th Governor of Maine (1822–1827)", "relationship": "5TH_GOVERNOR", "note": "Served as Maine's 5th governor (1822–1827) — providing executive leadership during the state's founding decade after its 1820 separation from Massachusetts"},
            {"entity": "2nd Comptroller of the US Treasury (1836–1850)", "relationship": "14-YEAR_FEDERAL_COMPTROLLER", "note": "Served as 2nd Comptroller of the US Treasury for 14 years — contributing to federal financial administration through the Panic of 1837 and Mexican-American War era"},
            {"entity": "Maine separation from Massachusetts (1820 Missouri Compromise)", "relationship": "POLITICAL_CAREER_LAUNCHED_BY_FOUNDING_OF", "note": "Maine's separation from Massachusetts in 1820 — as part of the Missouri Compromise — created the new state whose institutional needs elevated Parris's political career"},
            {"entity": "US House of Representatives from District of Maine (1815–1818)", "relationship": "CONGRESSMAN", "note": "Served as US Representative from the District of Maine when it was still part of Massachusetts — establishing his national political presence before Maine statehood"},
            {"entity": "Maine Supreme Judicial Court / US District Court for Maine", "relationship": "SUCCESSIVE_JUDGE_ON", "note": "Served successively as Associate Justice of the Maine Supreme Judicial Court (1828–1836) and US District Judge for Maine (1836–1844) — transitioning from political to judicial career"}
        ]
    }),

    # 5 — Morgan Lewis
    ("morgan-lewis", {
        "summary": (
            "Morgan Lewis (1754–1844) was an American lawyer, "
            "politician, and military officer — son of Francis Lewis, "
            "a New York signer of the Declaration of Independence — "
            "who served as New York State Attorney General (1791–1795), "
            "Chief Justice of the New York Supreme Court (1801–1804), "
            "4th Governor of New York (1804–1807), and Major General "
            "in both the Revolutionary War and the War of 1812. "
            "His life spanned nine decades — from the eve of the "
            "Revolution to the eve of the Civil War — making him "
            "one of the last surviving figures of the founding "
            "generation when he died in 1844 at age 89.\n\n"
            "His governorship (1804–1807) was associated with the "
            "Clintonian Democratic-Republican faction and was partly "
            "defined by its origins in the aftermath of Aaron Burr's "
            "political destruction: Lewis was elected as the "
            "anti-Burrite candidate in 1804, the same year that "
            "Alexander Hamilton was killed in the Burr-Hamilton duel. "
            "His administration navigated New York's rapid commercial "
            "expansion and the fragmentation of the First Party "
            "System during Jefferson's second term.\n\n"
            "His War of 1812 service as a Major General on the "
            "Niagara frontier included participation in the April "
            "1813 capture of York (Toronto) — the first significant "
            "American offensive success of the northern campaign. "
            "Despite a mixed military record, he remained a respected "
            "elder statesman of New York's establishment through "
            "the Jacksonian era.\n\n"
            "'I have served my country,' he said near the end of "
            "his life, 'in two wars and through most of its history' "
            "— a literal statement for a man born in 1754."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "4th Governor of New York (1804–1807); son of Declaration of Independence signer Francis Lewis; NY Attorney General (1791–1795); Chief Justice of NY Supreme Court (1801–1804); Major General in both the Revolutionary War and War of 1812 (participated in capture of York/Toronto, 1813); lived 1754–1844, spanning Revolution to eve of Civil War.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The collapse of Aaron Burr's political faction in New York — following the 1804 Burr-Hamilton duel and Burr's subsequent criminal indictment — created the political opening that allowed the Clintonian Democratic-Republican faction (and Lewis as their candidate) to win the 1804 New York gubernatorial election",
            "His distinguished Revolutionary War service — and his family's extraordinary position as the son of a Declaration signer — provided the political capital and social connections that supported his legal and judicial career in New York's competitive professional elite",
            "The War of 1812's need for experienced officers with Revolutionary War service — and the northern frontier's strategic demands on the Niagara corridor — created the military role that brought Lewis back to active command at nearly 60 years of age"
        ],
        "effects": [
            "His governorship (1804–1807) contributed to New York's political development during the critical period of the First Party System's collapse and the Jeffersonian consolidation — governing the nation's most populous and commercially dynamic state at a moment of intense factional conflict",
            "His War of 1812 participation in the capture of York (Toronto) in April 1813 — the first significant American offensive success on the northern frontier — contributed to the strategic momentum that eventually produced the 1814 campaign season's mixed results",
            "His eight-decade career of public service — from Revolutionary War officer through governor, attorney general, chief justice, and War of 1812 major general — illustrated the cumulative depth of the founding generation's institutional contributions to American governance",
            "His 89-year lifespan (1754–1844) made him a living historical memory: he could personally connect the Jacksonian Americans of the 1840s to events before the Revolution — a human bridge across nine decades of American history"
        ],
        "relationships": [
            {"entity": "4th Governor of New York (1804–1807)", "relationship": "4TH_GOVERNOR", "note": "Served as 4th Governor of New York (1804–1807) — elected as the anti-Burrite Clintonian Democratic-Republican in the aftermath of the Burr-Hamilton duel"},
            {"entity": "Francis Lewis (father, Declaration of Independence signer, New York)", "relationship": "SON_OF", "note": "Son of Francis Lewis — New York's signer of the Declaration of Independence — whose family position provided Morgan Lewis's political and social foundation"},
            {"entity": "Aaron Burr / Burr-Hamilton duel (1804) political consequences", "relationship": "POLITICAL_BENEFICIARY_OF_BURR'S_DESTRUCTION", "note": "Elected governor in 1804 as the anti-Burrite candidate — his election directly benefiting from Burr's political destruction following the Hamilton duel"},
            {"entity": "Capture of York (Toronto), April 1813 / War of 1812 northern campaign", "relationship": "MAJOR_GENERAL_COMMANDING_DURING", "note": "Served as Major General on the Niagara frontier — participating in the April 1813 capture of York (Toronto), the first significant American offensive success of the northern War of 1812 campaign"},
            {"entity": "New York Attorney General (1791–1795) / Chief Justice of NY Supreme Court (1801–1804)", "relationship": "SUCCESSIVE_LEGAL_POSITIONS_HELD", "note": "Served as NY Attorney General (1791–1795) and then Chief Justice of the NY Supreme Court (1801–1804) — building the judicial career that positioned him for the governorship"}
        ]
    }),

    # 6 — Charles Loyseau
    ("charles-loyseau", {
        "summary": (
            "Charles Loyseau (1564–1627) was a French jurist, "
            "lawyer at the Parlement of Paris, and local judge "
            "whose 'Traité des ordres et simples dignités' "
            "(A Treatise on Orders and Simple Dignities, 1610) "
            "is one of the most important analytical works on "
            "the social and legal structure of Old Regime France — "
            "a detailed theoretical account of French society "
            "organized according to its hierarchical orders, "
            "offices, and dignities that remains indispensable "
            "to historians of early modern Europe.\n\n"
            "Writing during the reign of Henry IV — in the "
            "aftermath of the Wars of Religion and during the "
            "consolidation of Bourbon absolutist monarchy — "
            "Loyseau analyzed French society as a system of "
            "orders (états) and offices that derived their "
            "authority from the crown. His treatise classified "
            "the social hierarchy from princes of the blood "
            "through the nobility, the clergy, and the various "
            "grades of the third estate — providing the most "
            "systematic legal-philosophical analysis of French "
            "social structure before the Revolution.\n\n"
            "His analytical framework — in which social rank "
            "was understood as a hierarchy of offices conferring "
            "dignities rather than purely a hierarchy of birth — "
            "reflected the legal humanist tradition's attempt "
            "to understand French society as a rational system "
            "grounded in royal authority. His other major work, "
            "'Traité des seigneuries' (Treatise on Lordships), "
            "analyzed the structure of seigneurial authority "
            "in the French countryside.\n\n"
            "Loyseau's works are primary sources for understanding "
            "how educated Frenchmen of the early 17th century "
            "theorized their own social world — and how they "
            "justified and explained the hierarchical order "
            "that the Revolution would destroy in 1789."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "French jurist (1564–1627); lawyer at the Parlement of Paris; author of the 'Traité des ordres et simples dignités' (1610) — a systematic analysis of Old Regime French social hierarchy and the theory of orders, offices, and dignities; indispensable primary source for historians of early modern France; also authored 'Traité des seigneuries'.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Wars of Religion (1562–1598) and the subsequent Bourbon consolidation under Henry IV created the political context in which French jurists like Loyseau sought to systematize the legal and social foundations of the monarchy — developing theoretical frameworks that could justify and explain the reassertion of royal authority",
            "The legal humanist tradition in France — which combined Roman law analysis with historical research into French customary law and institutional structures — provided the intellectual framework within which Loyseau's analysis of orders and dignities was developed",
            "The social disruptions of the Wars of Religion — which had called into question the traditional hierarchy of estates and created new forms of social mobility — provided the practical social context that made systematic analysis of the order system both necessary and intellectually urgent for French legal thinkers of the early 17th century"
        ],
        "effects": [
            "His 'Traité des ordres et simples dignités' (1610) became one of the foundational texts for understanding Old Regime French social structure — cited by historians from the 17th century to the present as the most comprehensive legal-philosophical account of the orders system before the Revolution",
            "His theoretical framework — analyzing French society as a system of royal-derived offices and dignities rather than purely birth-based hierarchy — contributed to the legal culture of absolute monarchy that shaped French governance from the early 17th century through 1789",
            "His works provided the intellectual vocabulary through which contemporaries and subsequent historians have understood the French Old Regime's social structure: the language of 'orders,' 'estates,' 'dignities,' and 'offices' that appears throughout the literature of the Ancien Régime",
            "The gap between Loyseau's orderly theoretical framework and the actual social chaos that led to the 1789 Revolution makes his works particularly valuable as historical sources — they document the ideology of a system even as the system itself was generating the contradictions that would destroy it"
        ],
        "relationships": [
            {"entity": "'Traité des ordres et simples dignités' (1610)", "relationship": "AUTHOR_OF", "note": "Authored the definitive early 17th-century analysis of French social hierarchy — classifying the orders, offices, and dignities from princes to third estate in the most systematic legal-philosophical account of Old Regime France"},
            {"entity": "Parlement of Paris / French legal humanist tradition", "relationship": "LAWYER_AND_SCHOLAR_WITHIN", "note": "Practiced as a lawyer at the Parlement of Paris and worked within the French legal humanist tradition — combining Roman law with analysis of French customary institutions"},
            {"entity": "Henry IV / Bourbon consolidation of French absolutism (1598–1610)", "relationship": "JURIST_THEORIZING_SOCIAL_ORDER_UNDER", "note": "Wrote during Henry IV's reign — in the aftermath of the Wars of Religion — developing the theoretical framework for French absolutism's social hierarchy"},
            {"entity": "Old Regime French social structure (orders, estates, dignities)", "relationship": "FOREMOST_SYSTEMATIC_ANALYST_OF", "note": "The foremost systematic analyst of Old Regime French social structure — his framework of orders, offices, and dignities providing the vocabulary through which historians understand the Ancien Régime"},
            {"entity": "'Traité des seigneuries' (Treatise on Lordships)", "relationship": "AUTHOR_OF", "note": "Also authored the 'Traité des seigneuries' — a systematic analysis of seigneurial authority in the French countryside that complemented his analysis of the orders system"}
        ]
    }),

    # 7 — Richard Bland Lee
    ("richard-bland-lee", {
        "summary": (
            "Richard Bland Lee (1761–1827) was a Virginia planter, "
            "congressman, and DC jurist — a member of the "
            "distinguished Lee family of Virginia and younger brother "
            "of both Major General Henry 'Light-Horse Harry' Lee "
            "and Charles Lee (Attorney General under John Adams). "
            "Born at Leesylvania in Prince William County, he served "
            "in the Virginia House of Delegates before being elected "
            "to the First and Second Congresses (1789–1793) as a "
            "Federalist from Virginia.\n\n"
            "His most historically significant act came in 1790: "
            "he was one of the few Virginia representatives who voted "
            "for the Residence Act — the compromise legislation that "
            "moved the national capital from Philadelphia to a "
            "permanent site on the Potomac River. His vote was part "
            "of the Compromise of 1790 — the grand bargain between "
            "Hamilton and Jefferson in which the South accepted "
            "Hamilton's federal assumption of state debts in exchange "
            "for the capital being placed on the Potomac.\n\n"
            "His Potomac vote came at considerable political cost: "
            "Virginia voters resented his support for federal "
            "assumption of state debts, and he was defeated for "
            "re-election partly on that basis — illustrating the "
            "political risks that accompanied the Compromise of 1790 "
            "for Virginia representatives who supported Hamilton's "
            "financial program.\n\n"
            "After leaving Congress he served in various legal roles "
            "in Virginia and DC, eventually becoming a Judge of "
            "the Orphans' Court in the District of Columbia — the "
            "capital he had helped place on the Potomac."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Virginia Federalist congressman (1789–1793); voted for the Residence Act (1790) placing the national capital on the Potomac — part of the Compromise of 1790; younger brother of 'Light-Horse Harry' Lee and Attorney General Charles Lee; lost re-election partly over his support for Hamilton's assumption plan; Judge of DC Orphans' Court.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Compromise of 1790 — Hamilton's grand bargain with Jefferson and Madison trading federal assumption of state debts for the capital site on the Potomac — created the political opportunity for Virginia representatives who wanted the Potomac capital enough to accept the financial arrangement",
            "His Lee family identity — and his connections to both the military and legal Lee brothers who were prominent in the Federalist establishment — gave him the social standing and political relationships that supported his congressional career",
            "Virginia's political culture of planter-class governance — in which Federalist-aligned gentry families like the Lees could win congressional seats in the late 1780s — provided the electoral environment for his congressional career before Jeffersonian Republicanism transformed Virginia politics"
        ],
        "effects": [
            "His vote for the Residence Act (1790) contributed to securing the Potomac site for the national capital — a decision that created Washington, DC, and shaped the geographical orientation of American federal government for more than two centuries",
            "His defeat for re-election — partly attributable to voter anger at his support for Hamilton's assumption plan — illustrated the political costs that the Compromise of 1790 imposed on Virginia Federalists who prioritized the Potomac capital over anti-assumption sentiment",
            "His career as a moderate Virginia Federalist illustrated the brief window in which Virginia's planter class could support Federalist policies before Jeffersonian Republicanism made Federalism politically toxic in the state",
            "His eventual judicial service as Judge of the DC Orphans' Court connected his personal stake in the Potomac capital decision to his later professional life — he became a judge in the very city whose founding he had helped legislate"
        ],
        "relationships": [
            {"entity": "Residence Act of 1790 / Compromise of 1790 (Potomac capital decision)", "relationship": "VIRGINIA_CONGRESSMAN_WHO_VOTED_FOR", "note": "Voted for the Residence Act (1790) placing the national capital on the Potomac — part of the Compromise of 1790 trading assumption for capital site — at considerable political cost in Virginia"},
            {"entity": "Henry 'Light-Horse Harry' Lee (older brother, Major General)", "relationship": "YOUNGER_BROTHER_OF", "note": "Younger brother of Major General Henry 'Light-Horse Harry' Lee — one of the most celebrated cavalry commanders of the Revolutionary War and father of Robert E. Lee"},
            {"entity": "Charles Lee (older brother, US Attorney General under John Adams)", "relationship": "YOUNGER_BROTHER_OF", "note": "Younger brother of Charles Lee — US Attorney General under John Adams (1795–1801) — the Lee family's representation of Virginia in the Federalist executive branch"},
            {"entity": "US House of Representatives from Virginia (Federalist, First and Second Congresses, 1789–1793)", "relationship": "FEDERALIST_CONGRESSMAN", "note": "Served in the First and Second Congresses (1789–1793) as a Virginia Federalist — one of the small minority of Virginia representatives aligned with Hamilton's financial program"},
            {"entity": "Judge of the DC Orphans' Court", "relationship": "POST-CONGRESSIONAL_JUDICIAL_SERVICE", "note": "Served as Judge of the Orphans' Court in the District of Columbia — the capital city he had helped legislate into existence with his Residence Act vote"}
        ]
    }),

    # 8 — Enoch Lincoln
    ("enoch-lincoln", {
        "summary": (
            "Enoch Lincoln (1788–1829) was an American politician, "
            "orator, and poet from a distinguished Massachusetts-Maine "
            "political family — the son of Levi Lincoln Sr. (Jefferson's "
            "Attorney General) and younger brother of Levi Lincoln Jr. "
            "(later Governor of Massachusetts). Enoch himself served "
            "as US Representative from Massachusetts and Maine and "
            "as the 6th Governor of Maine from 1827 until his death "
            "in office in 1829 at age 40 — one of the youngest "
            "American governors to die in office.\n\n"
            "Born in Worcester, Massachusetts, Enoch graduated from "
            "Harvard in 1807, studied law, and entered politics "
            "in the same period that Maine's statehood movement "
            "was building toward the Missouri Compromise separation "
            "of 1820. He was elected to Congress as a representative "
            "of the new state of Maine after separation and served "
            "several terms before winning the governorship in 1827 "
            "during the intense political realignment as the "
            "Democratic-Republican Party fractured into Jacksonian "
            "and National Republican factions.\n\n"
            "Lincoln was known throughout his career for unusual "
            "intellectual gifts: he was a gifted orator praised "
            "by contemporaries as among the most eloquent speakers "
            "in New England, and he was a published poet who "
            "contributed verse to periodicals — qualities rare "
            "among American politicians of his era. His early "
            "death in October 1829 — from tuberculosis, the "
            "era's most common killer of young professional men — "
            "was widely mourned in Maine political circles.\n\n"
            "His brother Levi Jr. later served three terms as "
            "Governor of Massachusetts, completing the family's "
            "extraordinary New England political dynasty."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "6th Governor of Maine (1827–1829, died in office at 40); son of Levi Lincoln Sr. (Jefferson's Attorney General); younger brother of Levi Lincoln Jr. (Governor of Massachusetts); US Representative from both Massachusetts and Maine; gifted orator and published poet; his early death mourned as a loss of unusual political talent for Maine.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Maine's separation from Massachusetts in 1820 — as part of the Missouri Compromise — created the new state whose political institutions needed founding and whose representation Lincoln's congressional career helped establish",
            "The Lincoln family's deep roots in Massachusetts-Maine political life — his father as Jefferson's Attorney General, his brother as future Governor of Massachusetts — provided the family networks and political connections that supported Enoch's rapid political rise",
            "The Jacksonian political realignment of 1824–1828 — which fragmented the Democratic-Republican Party into competing factions — created the fluid electoral environment in which Lincoln's 1827 gubernatorial victory became possible"
        ],
        "effects": [
            "His governorship (1827–1829) provided Maine's young state with executive leadership during the transition from Monrovian Era politics to Jacksonian Democracy — a politically turbulent period that required careful navigation of competing national factions",
            "His death in office in October 1829 — from tuberculosis at age 40 — created a succession that tested Maine's constitutional provisions for gubernatorial succession in only the state's ninth year of existence",
            "His literary reputation — as a gifted orator and published poet — contributed to the cultural life of early Maine and the tradition of literary political figures in the Lincoln family whose intellectual distinction was unusual among antebellum American politicians",
            "The Lincoln family's combined contributions — Levi Sr. as Jefferson's Attorney General, Enoch as Maine governor, Levi Jr. as Massachusetts governor — represented one of the most significant political dynasties in New England's early 19th-century history"
        ],
        "relationships": [
            {"entity": "6th Governor of Maine (1827–1829, died in office)", "relationship": "6TH_GOVERNOR", "note": "Served as Maine's 6th Governor (1827–1829) — dying in office from tuberculosis at age 40, one of the youngest American governors to die in office"},
            {"entity": "Levi Lincoln Sr. (father, Jefferson's Attorney General)", "relationship": "SON_OF", "note": "Son of Levi Lincoln Sr. — Jefferson's Attorney General (1801–1805) — whose political connections and family standing supported Enoch's career in Maine and Massachusetts"},
            {"entity": "Levi Lincoln Jr. (older brother, Governor of Massachusetts)", "relationship": "YOUNGER_BROTHER_OF", "note": "Younger brother of Levi Lincoln Jr. — who later served three terms as Governor of Massachusetts — completing the Lincoln family's extraordinary New England political dynasty"},
            {"entity": "US House of Representatives from Massachusetts and Maine", "relationship": "CONGRESSMAN_FROM_BOTH", "note": "Served as US Representative from Massachusetts (before Maine statehood) and from Maine (after separation in 1820) — one of the few politicians to represent both states"},
            {"entity": "Maine statehood (1820 Missouri Compromise separation)", "relationship": "POLITICAL_CAREER_BUILT_WITHIN_FOUNDING_INSTITUTIONS_OF", "note": "His congressional and gubernatorial career was built within the institutional founding of Maine after its 1820 separation from Massachusetts as part of the Missouri Compromise"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 41)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
