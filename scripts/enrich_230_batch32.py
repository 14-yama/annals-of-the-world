#!/usr/bin/env python3
"""
Batch 32 — 8 entities: James Moore Wayne, David Daggett, Thomas Ford,
Samuel Holten, Thomas Clayton, David Wallace, George A. Waggaman,
John Hopkins Clarke
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

    # 1 — James Moore Wayne
    ("james-moore-wayne", {
        "summary": (
            "James Moore Wayne (1790–1867) was an American jurist and politician "
            "who served as an Associate Justice of the United States Supreme Court "
            "from 1835 to 1867 — one of the longest tenures in Supreme Court history. "
            "A Georgia-born lawyer who had served as Mayor of Savannah (1817–1819) "
            "and as a US Representative (1829–1835), Wayne was appointed to the Court "
            "by President Andrew Jackson and remained on it through the Civil War — "
            "one of only two Southern-born Justices to remain on the Union's Supreme "
            "Court rather than resign when their states seceded.\n\n"
            "Wayne participated in the Court's most consequential and controversial "
            "decisions of the antebellum era. He joined the majority in Dred Scott "
            "v. Sandford (1857) — the case in which Chief Justice Taney ruled that "
            "African Americans could not be citizens and that Congress had no "
            "authority to prohibit slavery in the territories. Wayne wrote his "
            "own concurrence, going even further than Taney in denying any "
            "congressional authority over slavery in the territories.\n\n"
            "When Georgia seceded in 1861, Wayne — unlike most of his fellow "
            "Southern justices — remained on the Court, choosing Union over his "
            "home state. The Confederate government declared him a traitor and "
            "confiscated his property. His son joined the Confederate Army while "
            "Wayne continued to serve as a Union Supreme Court Justice — another "
            "family divided by the Civil War's demands of loyalty.\n\n"
            "He served on the Court until his death in 1867, having witnessed the "
            "Civil War, the abolition of slavery that reversed the Dred Scott "
            "decision, and the beginning of Reconstruction."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "US Supreme Court Associate Justice (1835–1867) — 32-year tenure; Dred Scott majority/concurrence author (1857); Georgia-born justice who remained on the Union's Supreme Court when Georgia seceded — Confederate government confiscated his property; one of the longest-serving Justices in Court history.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Andrew Jackson's appointment policies — rewarding loyal Democratic politicians from the South with Supreme Court appointments — led to Wayne's elevation from congressman to Supreme Court Justice in 1835",
            "Georgia's secession in 1861 created the defining personal and professional crisis of Wayne's life — forcing the choice between his home state and his judicial office — which he resolved by remaining on the Union's Court",
            "The slavery controversy's escalation in the 1850s — and the Court's decision to use Dred Scott as a vehicle for the broadest possible ruling on slavery and congressional authority — created the context for Wayne's expansive proslavery concurrence"
        ],
        "effects": [
            "His Dred Scott concurrence — going even further than Taney in denying congressional authority over slavery — contributed to the most consequential judicial error in American history, helping push the country toward Civil War",
            "His decision to remain on the Union's Supreme Court when Georgia seceded provided an important precedent: that Supreme Court Justices' constitutional duties could supersede state loyalty — even at the cost of property confiscation by the Confederacy",
            "His 32-year tenure contributed to the development of American constitutional law across four decades — from the Jacksonian era through the Civil War and into early Reconstruction",
            "His son's service in the Confederate Army while Wayne served the Union created a family division that became a symbol of the Civil War's tearing apart of family loyalties — comparable to the Crittenden family's parallel division"
        ],
        "relationships": [
            {"entity": "Dred Scott v. Sandford (1857)", "relationship": "CONCURRENCE_AUTHOR_IN", "note": "Joined the majority and wrote a separate concurrence going even further than Taney — denying any congressional authority to prohibit slavery in the territories"},
            {"entity": "Andrew Jackson (US President)", "relationship": "APPOINTED_TO_SUPREME_COURT_BY", "note": "Appointed to the Supreme Court by Jackson in 1835 as a reward for his loyalty as a Southern Democratic congressman"},
            {"entity": "US Supreme Court (1835–1867)", "relationship": "ASSOCIATE_JUSTICE_32_YEARS", "note": "Served as Associate Justice for 32 years — one of the longest tenures in Court history — through the antebellum period, the Civil War, and early Reconstruction"},
            {"entity": "Georgia secession (1861)", "relationship": "REMAINED_ON_UNION_COURT_DESPITE", "note": "Refused to resign from the Supreme Court when Georgia seceded — the Confederate government declared him a traitor and confiscated his property"},
            {"entity": "Civil War (family division)", "relationship": "PERSONAL_SYMBOL_OF", "note": "His son served in the Confederate Army while Wayne served the Union Supreme Court — a family divided comparable to the Crittenden family's Civil War split"}
        ]
    }),

    # 2 — David Daggett
    ("david-daggett", {
        "summary": (
            "David Daggett (1764–1851) was a Connecticut Federalist lawyer, "
            "judge, and politician who combined a distinguished career in "
            "Connecticut politics with a position as one of the founding figures "
            "of legal education in the United States — serving as a Professor "
            "of Law at Yale College from 1824 to 1848 and as one of the founders "
            "of what became Yale Law School, while simultaneously holding "
            "judicial office on the Connecticut Supreme Court of Errors. "
            "His career connected the Federalist political tradition to the "
            "development of American legal education at one of its most formative "
            "institutions.\n\n"
            "Daggett's political career included service as a US Senator from "
            "Connecticut (1813–1819) and as Mayor of New Haven — but his most "
            "lasting significance came from his legal and academic work. As "
            "a Yale law professor and Connecticut Supreme Court judge simultaneously, "
            "he trained a generation of Connecticut lawyers while also contributing "
            "to the development of state constitutional law.\n\n"
            "His record on race relations was deeply problematic: he presided "
            "over the trial that blocked the establishment of Prudence Crandall's "
            "school for African American girls in Canterbury, Connecticut (1833–1834) "
            "— upholding the Connecticut Black Law that prohibited educating "
            "out-of-state African Americans — and he is also associated with "
            "the blocking of plans for the first college for African Americans "
            "in the United States.\n\n"
            "He remained intellectually active into his 80s, delivering lectures "
            "at Yale until he was 84 — an extraordinary career longevity in "
            "19th-century American academic and legal life."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Connecticut Federalist Senator (1813–1819), Mayor of New Haven, Connecticut Supreme Court of Errors judge, and Yale Law School founding professor (1824–1848); his legal rulings blocked early African American education in Connecticut; trained a generation of Connecticut lawyers.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Yale College's need for a formal law professorship — reflecting the professionalization of legal education in the early 19th century — created the academic position that became Daggett's most lasting legacy",
            "Connecticut's Federalist political culture — which dominated the state through the War of 1812 and into the 1820s — provided the political environment for Daggett's Senate career and his subsequent judicial appointments",
            "Connecticut's racial anxieties in the 1830s — and the legislature's passage of the Black Law in response to Prudence Crandall's school — created the legal context for Daggett's problematic ruling blocking African American education"
        ],
        "effects": [
            "His founding professorship at Yale Law School contributed to the institutionalization of legal education at one of America's most influential law schools — training a generation of Connecticut lawyers in the Federalist legal tradition",
            "His ruling upholding the Connecticut Black Law and blocking Prudence Crandall's school contributed to the suppression of African American educational access in antebellum Connecticut — a decision that had lasting negative consequences for racial equality",
            "His combined role as law professor and Supreme Court judge simultaneously modeled the integration of academic and judicial roles that would become more common in American legal culture",
            "His Senate service (1813–1819) contributed to Connecticut's representation in Washington during the War of 1812 — when Federalist New England was bitterly opposed to the conflict"
        ],
        "relationships": [
            {"entity": "Yale Law School (founding)", "relationship": "FOUNDING_PROFESSOR_OF_1824-1848", "note": "Served as Professor of Law at Yale College (1824–1848) — one of the founders of what became Yale Law School, training a generation of Connecticut lawyers"},
            {"entity": "Prudence Crandall's school / Connecticut Black Law (1833–1834)", "relationship": "PRESIDED_OVER_TRIAL_BLOCKING", "note": "Presided over the trial upholding the Connecticut Black Law — blocking Prudence Crandall's school for African American girls and suppressing early African American education"},
            {"entity": "Connecticut Supreme Court of Errors", "relationship": "JUDGE_OF", "note": "Served as a judge of the Connecticut Supreme Court of Errors — simultaneously with his Yale law professorship"},
            {"entity": "US Senate from Connecticut (1813–1819)", "relationship": "FEDERALIST_SENATOR", "note": "Served as US Senator from Connecticut (1813–1819) during the War of 1812 — representing a state bitterly opposed to the conflict"},
            {"entity": "New Haven, Connecticut", "relationship": "MAYOR_OF", "note": "Served as Mayor of New Haven — combining his judicial, academic, and municipal roles in the Connecticut Federalist tradition"}
        ]
    }),

    # 3 — Thomas Ford
    ("thomas-ford", {
        "summary": (
            "Thomas Ford (1800–1850) was a lawyer, judge, and the eighth Governor "
            "of Illinois (1842–1846), the first governor to have been raised in "
            "the state he governed. His administration coincided with one of "
            "the most dramatic episodes in Illinois history: the founding of Nauvoo "
            "by Joseph Smith and the Latter-day Saints, the escalating conflict "
            "between Mormon settlers and their Illinois neighbors, and — in June "
            "1844 — the murder of Joseph Smith and his brother Hyrum Smith while "
            "they were in state custody at Carthage Jail, Illinois. Ford had given "
            "the Smiths his personal guarantee of protection, and their murder "
            "while under state protection was one of the most controversial "
            "episodes of his administration.\n\n"
            "Beyond the Mormon crisis, Ford's administration addressed serious "
            "economic challenges: Illinois had accumulated an enormous public debt "
            "during the canal and railroad boom of the 1830s, and the Panic of 1837 "
            "had left the state near insolvency. Ford worked to restore the state's "
            "financial solvency — partially succeeding, though the debt burden "
            "remained a major problem.\n\n"
            "After leaving the governorship, Ford wrote 'A History of Illinois' "
            "(1854, published posthumously) — one of the most valuable primary "
            "sources for early Illinois history and for understanding the "
            "Mormon conflicts of the 1840s. Written with candor and self-criticism "
            "about his own administration, the book is unusual among 19th-century "
            "political memoirs for its honesty about political failure.\n\n"
            "He died in poverty in 1850, four years after leaving office — "
            "a reminder of the financial vulnerability of early American politicians."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Eighth Governor of Illinois (1842–1846); administration witnessed the murder of Joseph Smith and Hyrum Smith while in state custody (1844) — the most dramatic episode in early Illinois history; author of 'A History of Illinois' (1854) — a valuable primary source for early Illinois history and Mormon conflicts.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Illinois's decision to welcome the Latter-day Saints and the establishment of Nauvoo — which grew to be one of the largest cities in Illinois — created the religious and social conflict that dominated Ford's governorship",
            "The financial crisis inherited from the 1837 Panic and the failed internal improvements program created the economic challenge that Ford had to manage throughout his administration",
            "The Mormon-non-Mormon conflict's escalation — Joseph Smith's arrest, Ford's personal guarantee of protection, and the subsequent murder — created the governance failure that damaged Ford's historical reputation"
        ],
        "effects": [
            "The murder of Joseph Smith and Hyrum Smith while in state custody — despite Ford's personal protection guarantee — was one of the most consequential events in Latter-day Saint history, triggering the Mormon exodus from Illinois to Utah under Brigham Young",
            "The Mormon exodus from Nauvoo — triggered by the continuing conflict after Smith's murder — fundamentally reshaped Illinois demographics and indirectly led to the settling of Utah by the Latter-day Saints under Brigham Young",
            "His 'History of Illinois' (1854) provided an invaluable primary source for early Illinois history — unusual for its candid self-criticism of his own administration and for its detailed account of the Mormon crisis",
            "His partial success in restoring Illinois's financial solvency — reducing the debt burden while maintaining state services — contributed to Illinois's eventual economic recovery from the 1837 Panic's devastation"
        ],
        "relationships": [
            {"entity": "Joseph Smith / Murder at Carthage Jail (1844)", "relationship": "GOVERNOR_WHO_GUARANTEED_AND_FAILED_TO_PROVIDE_PROTECTION_FOR", "note": "Gave Joseph Smith his personal guarantee of protection — the murder of Smith and Hyrum Smith while in state custody was the most controversial failure of his administration"},
            {"entity": "Nauvoo, Illinois / Latter-day Saints exodus", "relationship": "GOVERNOR_DURING_CRISIS_THAT_TRIGGERED", "note": "His administration oversaw the Mormon-non-Mormon conflict that escalated into Smith's murder and ultimately the mass Mormon exodus from Illinois to Utah"},
            {"entity": "'A History of Illinois' (1854)", "relationship": "AUTHOR_OF", "note": "Wrote this valuable primary source history — published posthumously — notable for its candid self-criticism about his own administration and its account of the Mormon crisis"},
            {"entity": "Illinois state debt / Panic of 1837 financial crisis", "relationship": "GOVERNOR_WHO_PARTIALLY_RESTORED_SOLVENCY_AFTER", "note": "Inherited and partially addressed the massive state debt accumulated during the internal improvements boom — working to restore Illinois's fiscal stability"},
            {"entity": "Illinois governorship (first Illinois-raised governor)", "relationship": "FIRST_ILLINOIS-RAISED_GOVERNOR", "note": "The first Illinois governor to have been raised in the state he governed — representing the emergence of Illinois's native-born political leadership"}
        ]
    }),

    # 4 — Samuel Holten
    ("samuel-holten", {
        "summary": (
            "Samuel Holten (1738–1816) was an American Founding Father, physician, "
            "and politician from Danvers, Massachusetts, who participated in "
            "the founding events of the American republic across multiple "
            "institutional roles — serving as a delegate to the Second Continental "
            "Congress and signing the Articles of Confederation, as a member "
            "of the Massachusetts Provincial Congress, as a judge of the "
            "Court of Common Pleas, and as a US Representative in the First "
            "Congress (1793–1795). His career exemplified the pattern of "
            "Massachusetts Patriot leaders who combined professional roles "
            "(medicine) with public service across colonial, revolutionary, "
            "and early national institutions.\n\n"
            "Holten's participation in the Continental Congress was significant: "
            "he served multiple terms from 1778 to 1787 — one of the longest "
            "sustained participations in that body — and his signature on the "
            "Articles of Confederation made him one of the legal founders of "
            "the first American constitutional framework. Massachusetts's "
            "Continental Congress delegation was among the most active and "
            "influential, and Holten's long service contributed to that record.\n\n"
            "As a physician practicing in Danvers, Massachusetts, Holten represented "
            "the dual professional-political identity that was common among "
            "founding-era American leaders — educated men who combined a learned "
            "profession with civic leadership. Danvers was a significant "
            "Massachusetts community with deep roots in the colonial period, "
            "including its proximity to Salem and the legacy of the 1692 witch trials.\n\n"
            "His long public career — spanning the revolutionary and early "
            "national periods — made him one of the most experienced political "
            "figures in Essex County, Massachusetts."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Massachusetts Founding Father who signed the Articles of Confederation; multiple-term Continental Congress delegate (1778–1787); physician; Massachusetts Provincial Congress member; US Representative (1793–1795); one of the most experienced Essex County, Massachusetts political figures spanning the revolutionary and early national periods.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Massachusetts's central role in the American Revolution — and its large, active Continental Congress delegation — created the institutional framework in which Holten's long congressional service was possible and significant",
            "The Articles of Confederation's creation as the first American constitutional framework required representatives from each state to ratify — making Holten's signature a direct act of constitutional founding",
            "Danvers's active patriot community — and the tradition of educated Massachusetts professionals combining learned professions with civic leadership — created the local political culture that produced Holten's career"
        ],
        "effects": [
            "His signature on the Articles of Confederation — as one of Massachusetts's representatives — contributed to the ratification of the first American constitutional framework and to his status as a Founding Father",
            "His nine years of Continental Congress service (1778–1787) — one of the longest sustained participations in that body — contributed to the continuity of Massachusetts's representation during the most critical years of the founding period",
            "His US House service in the First Congress contributed to Massachusetts's representation in the first Congress under the new Constitution — providing continuity between the revolutionary and constitutional periods",
            "His career as a physician-politician exemplified the founding generation's model of educated professional leadership — in which medical, legal, and clerical training provided the social capital for political service"
        ],
        "relationships": [
            {"entity": "Articles of Confederation", "relationship": "SIGNER_OF", "note": "Signed the Articles of Confederation as one of Massachusetts's representatives — contributing to the ratification of the first American constitutional framework"},
            {"entity": "Second Continental Congress (1778–1787)", "relationship": "LONG-SERVING_MASSACHUSETTS_DELEGATE_TO", "note": "Served multiple terms in the Continental Congress (1778–1787) — one of the longest sustained participations in that body"},
            {"entity": "US House of Representatives (First Congress, 1793–1795)", "relationship": "REPRESENTATIVE_IN", "note": "Served as US Representative from Massachusetts in the early Congress — providing continuity between the revolutionary and constitutional institutional periods"},
            {"entity": "Massachusetts Provincial Congress", "relationship": "MEMBER_OF", "note": "Participated in the Massachusetts Provincial Congress during the revolutionary period — one of the key pre-independence colonial governing bodies"},
            {"entity": "Danvers, Massachusetts (colonial/revolutionary community)", "relationship": "LEADING_POLITICAL_FIGURE_OF", "note": "Essex County's most experienced political figure spanning the revolutionary and early national periods — practicing medicine and civic leadership in Danvers throughout his career"}
        ]
    }),

    # 5 — Thomas Clayton
    ("thomas-clayton", {
        "summary": (
            "Thomas Clayton (1777–1854) was a Delaware Federalist, National "
            "Republican, and Whig politician and jurist who served in nearly "
            "every significant legal and political office in Delaware and "
            "at the federal level — as Delaware Attorney General (1810–1820), "
            "as a US Representative (1815–1817), as a Delaware Superior Court "
            "judge, as Delaware's Chief Justice, and as a US Senator (1837–1847). "
            "His 40-year public career illustrated the remarkable staying power "
            "of the Delaware Federalist-to-Whig political tradition — as the "
            "small state's commercial and legal elite maintained its "
            "conservative political culture through multiple national party realignments.\n\n"
            "Delaware's unusual political character — a tiny, heavily agricultural "
            "state wedged between Pennsylvania and Maryland, with a strong "
            "commercial and professional elite in Wilmington — allowed established "
            "political families and legal figures to dominate state politics "
            "across party lines. Thomas Clayton was able to move from Federalism "
            "to National Republicanism to Whiggery as parties changed while "
            "maintaining the same social conservative political philosophy.\n\n"
            "His decade as Delaware Attorney General — from 1810 to 1820 — "
            "coincided with some of the most dramatic events in early American "
            "history: the War of 1812, the post-war nationalist surge, and "
            "the beginnings of the Era of Good Feelings. His US Senate tenure "
            "(1837–1847) coincided with the height of Whig Party competition "
            "with the Democrats — a period in which Delaware was consistently "
            "one of the most reliably Whig states in the nation.\n\n"
            "He was the father of John M. Clayton — Secretary of State under "
            "Zachary Taylor and negotiator of the Clayton-Bulwer Treaty (1850)."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Delaware Federalist-to-Whig political figure; Delaware AG (1810–1820), US Representative (1815–1817), Delaware Chief Justice, and US Senator (1837–1847); father of John M. Clayton (Secretary of State under Taylor, Clayton-Bulwer Treaty).",
            "significanceCategory": "regional"
        },
        "causes": [
            "Delaware's unusual political culture — a tiny commercial state with a dominant Wilmington elite — allowed established legal and political figures to maintain power across party realignments without losing their fundamental social conservative orientation",
            "His legal training and success as a Delaware lawyer — and his decade as Attorney General — built the professional reputation that sustained his subsequent political career",
            "The Federalist-to-Whig political transition in Delaware — as the party of commercial conservatism rebranded itself — created the path that allowed Clayton to move from Federalism through National Republicanism to Whiggery without losing power"
        ],
        "effects": [
            "His 40-year public career — spanning from Delaware AG through US Senator — contributed to the institutional continuity of Delaware's legal and political institutions across one of the most turbulent periods in American party history",
            "His decade as Delaware AG (1810–1820) contributed to the development of Delaware's legal framework during the War of 1812 and the post-war period",
            "His US Senate tenure (1837–1847) contributed to Delaware's representation in Washington during the height of the Whig Party era — when Delaware was one of the Whig Party's most reliable states",
            "His son John M. Clayton's career — Secretary of State and Clayton-Bulwer Treaty negotiator — extended the family's political influence into a second generation and into international diplomacy"
        ],
        "relationships": [
            {"entity": "Delaware Attorney General (1810–1820)", "relationship": "SERVED_DECADE_AS", "note": "Served for a decade as Delaware Attorney General — building the legal reputation that sustained his subsequent political career"},
            {"entity": "US Senate from Delaware (1837–1847)", "relationship": "SENATOR_FOR_A_DECADE", "note": "Served as US Senator from Delaware (1837–1847) — representing one of the Whig Party's most reliable states"},
            {"entity": "John M. Clayton (Secretary of State)", "relationship": "FATHER_OF", "note": "Father of John M. Clayton — Secretary of State under Zachary Taylor and negotiator of the Clayton-Bulwer Treaty (1850) — extending the family's influence into diplomacy"},
            {"entity": "Delaware Federalist-to-Whig political tradition", "relationship": "EMBODIMENT_OF", "note": "His career trajectory — Federalist → National Republican → Whig — illustrated Delaware's commercial conservative tradition maintaining itself across party realignments"},
            {"entity": "Delaware Chief Justice / Superior Court", "relationship": "SERVED_AS_JUDGE_AND_CHIEF_JUSTICE", "note": "Served as Delaware Superior Court judge and Chief Justice — combining judicial with legislative and executive service across his career"}
        ]
    }),

    # 6 — David Wallace
    ("david-wallace", {
        "summary": (
            "David Wallace (1799–1859) was an Indiana lawyer, politician, and "
            "jurist who served as the sixth Governor of Indiana (1837–1840) — "
            "presiding over the state during the economic catastrophe of the "
            "Panic of 1837 and its aftermath. An 1821 West Point graduate "
            "who turned to law and politics, Wallace was a Whig and a supporter "
            "of Henry Clay's American System — advocating internal improvements, "
            "protective tariffs, and a national bank. His governorship was dominated "
            "by the financial wreckage that Indiana's ambitious internal improvements "
            "program had created: the state had borrowed heavily to finance "
            "canals and railroads just as the Panic struck, leaving Indiana "
            "nearly bankrupt and unable to service its debts.\n\n"
            "Wallace's administration tried to navigate the fiscal crisis while "
            "maintaining enough of the internal improvements program to justify "
            "the debts already incurred — a nearly impossible political and "
            "financial challenge. He was unable to prevent the eventual collapse "
            "of the program, and the debt burden dominated Indiana politics for "
            "decades.\n\n"
            "After his governorship, Wallace served in the US House of "
            "Representatives (1841–1843) and then as a judge of the Marion County "
            "Circuit Court for more than a decade — maintaining a career in "
            "Indiana's legal and political institutions throughout the antebellum "
            "period. He was also known as an essayist and speaker.\n\n"
            "His son Lew Wallace — also born in Indiana — became one of the most "
            "famous Americans of the century: Civil War general, Governor of "
            "New Mexico Territory, and author of 'Ben-Hur: A Tale of the Christ' "
            "(1880) — one of the best-selling novels of the 19th century."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Indiana governor during the Panic of 1837 and the state's internal improvements financial crisis; West Point 1821; US Representative (1841–1843); father of Lew Wallace — Civil War general and author of 'Ben-Hur' (1880), one of the 19th century's best-selling novels.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Indiana's ambitious internal improvements program — borrowing heavily for canals and railroads — created the financial crisis that the Panic of 1837 turned into near-bankruptcy, defining the challenge of Wallace's governorship",
            "The Panic of 1837 — triggered by Jackson's Specie Circular and the contraction of credit — devastated state finances across the country, hitting Indiana's heavily indebted improvements program particularly hard",
            "His West Point training and subsequent legal career — which were more natural than military — created the professional trajectory that led to his political career in Indiana's competitive Whig-Democrat environment"
        ],
        "effects": [
            "His administration's struggle with Indiana's debt crisis contributed to the eventual collapse of the internal improvements program — and to the constitutional amendments and fiscal conservatism that Indiana adopted in the 1840s as a result",
            "His son Lew Wallace's fame — as Civil War general, New Mexico governor, and 'Ben-Hur' author — gave the Wallace family one of the most remarkable legacies in Indiana history",
            "His US House service (1841–1843) contributed to Indiana's Whig congressional representation during the brief Harrison/Tyler administration period",
            "His long circuit court career contributed to the development of Marion County's legal system — as Indiana's most populous county grew dramatically in the antebellum period"
        ],
        "relationships": [
            {"entity": "Panic of 1837 / Indiana internal improvements crisis", "relationship": "GOVERNOR_DURING", "note": "Presided over Indiana during the financial catastrophe — the state had borrowed heavily for improvements that the Panic left it unable to service"},
            {"entity": "Lew Wallace (Civil War general / 'Ben-Hur' author)", "relationship": "FATHER_OF", "note": "Father of Lew Wallace — Civil War general, Governor of New Mexico Territory, and author of 'Ben-Hur: A Tale of the Christ' (1880), one of the 19th century's best-selling novels"},
            {"entity": "Indiana governor (6th, 1837–1840)", "relationship": "GOVERNOR", "note": "Served as Indiana's sixth governor (1837–1840) — presiding over the state's worst fiscal crisis to that point"},
            {"entity": "Henry Clay / American System (Whig party)", "relationship": "WHIG_SUPPORTER_OF", "note": "An Indiana Whig who supported Clay's American System — the internal improvements program that created the debt crisis he had to manage as governor"},
            {"entity": "US Military Academy / West Point (1821 graduate)", "relationship": "GRADUATE_OF", "note": "Graduated from West Point in 1821 — before abandoning the military for law and politics in Indiana"}
        ]
    }),

    # 7 — George A. Waggaman
    ("george-a-waggaman", {
        "summary": (
            "George Augustus Waggaman (1790–1843) was a Maryland-born Louisiana "
            "lawyer and politician who served as a United States Senator from "
            "Louisiana (1831–1835) as a National Republican and Whig — a "
            "brief Senate career during the height of the Jacksonian-Whig "
            "political struggle. Born in Caroline County, Maryland, to a "
            "prominent family, he studied law, was admitted to the bar in 1811, "
            "and subsequently moved to New Orleans, where he established a "
            "successful legal practice and entered Louisiana's distinctive "
            "political culture.\n\n"
            "Louisiana's politics in the 1820s and 1830s was shaped by its "
            "unique Creole character — a French-Spanish civil law tradition, "
            "a large multilingual population, and fierce competition between "
            "Jacksonian Democrats and the anti-Jacksonian coalition that became "
            "the Whig Party. New Orleans was one of the United States' most "
            "cosmopolitan cities — its port made it the commercial hub of the "
            "Mississippi River trade — and its legal community attracted "
            "ambitious lawyers from across the country.\n\n"
            "Waggaman was appointed to fill a Senate vacancy in 1831 and served "
            "until 1835 — a single term during the most intense phase of the "
            "Jackson-Clay rivalry. As a National Republican/Whig, he was part "
            "of the minority opposition to Jackson's Democratic Party in "
            "Louisiana — a politically challenging position in a state that "
            "was moving toward Jacksonian Democracy.\n\n"
            "His brief Senate career ended without re-election, and he returned "
            "to legal practice in New Orleans — dying in 1843 before the "
            "Whig Party achieved its greatest successes with the Harrison "
            "and Taylor elections."
        ),
        "importanceScore": 5,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Louisiana National Republican/Whig US Senator (1831–1835); Maryland-born New Orleans lawyer who represented the Whig opposition in a Jacksonian-dominated Louisiana during the height of the Jackson-Clay political rivalry.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Louisiana's Senate vacancy in 1831 created the appointment opportunity that elevated Waggaman from New Orleans legal practice to the US Senate",
            "The Jackson-Clay political rivalry — and the formation of the National Republican/Whig coalition — created the political identity that defined Waggaman's brief Senate career as part of the minority opposition in Louisiana",
            "New Orleans's cosmopolitan legal culture — attracting ambitious lawyers from across the country — created the professional environment in which Waggaman established himself after moving from Maryland"
        ],
        "effects": [
            "His Senate service provided National Republican/Whig representation from Louisiana during the intense Jackson-Clay political contest — maintaining a minority opposition voice in a state moving toward Jacksonian dominance",
            "His brief Senate career contributed to Louisiana's representation in Washington during the most critical years of the Jacksonian era — the period of the Bank War and nullification crisis",
            "His legal career in New Orleans contributed to the development of Louisiana's complex civil law legal profession — which combined French civil law traditions with American common law practice",
            "His failure to win re-election illustrated the difficulty of sustaining National Republican/Whig politics in Louisiana — a state where Jacksonian Democracy had strong roots in both the Creole and Anglo-American populations"
        ],
        "relationships": [
            {"entity": "US Senate from Louisiana (1831–1835)", "relationship": "NATIONAL_REPUBLICAN/WHIG_SENATOR", "note": "Served as US Senator from Louisiana (1831–1835) as part of the National Republican/Whig opposition to Jacksonian Democrats"},
            {"entity": "New Orleans legal profession (1820s–1840s)", "relationship": "PROMINENT_MEMBER_OF", "note": "Established himself in New Orleans's cosmopolitan legal community — one of the most competitive and distinguished legal markets in the antebellum US"},
            {"entity": "Jackson-Clay political rivalry (1820s–1830s)", "relationship": "WHIG_OPPOSITION_PARTICIPANT_IN", "note": "As a National Republican/Whig senator, he represented the anti-Jackson opposition in Louisiana during the height of the Jackson-Clay rivalry"},
            {"entity": "Louisiana Creole civil law tradition", "relationship": "LAWYER_WITHIN", "note": "Practiced law in Louisiana's unique civil law tradition — which combined French and Spanish civil law with American common law"},
            {"entity": "Caroline County, Maryland (origins)", "relationship": "BORN_IN_AND_EDUCATED_IN", "note": "Born in Caroline County, Maryland, to a prominent family — admitted to the Maryland bar in 1811 before relocating to Louisiana"}
        ]
    }),

    # 8 — John Hopkins Clarke
    ("john-hopkins-clarke", {
        "summary": (
            "John Hopkins Clarke (1789–1870) was a Rhode Island lawyer and "
            "Democratic-Republican/Whig politician who served as a United States "
            "Senator from Rhode Island (1847–1853) — a single Senate term that "
            "coincided with some of the most consequential legislative debates "
            "in antebellum American history, including the Compromise of 1850. "
            "A Brown University graduate (1809) and Providence lawyer, Clarke "
            "had a distinguished legal career in Rhode Island before his "
            "elevation to the Senate at the age of 57.\n\n"
            "Rhode Island's politics in the antebellum period was shaped by the "
            "aftermath of the Dorr Rebellion of 1842 — the constitutional crisis "
            "in which Thomas Dorr led an armed uprising against Rhode Island's "
            "highly restricted suffrage system (which still used the 1663 colonial "
            "charter as its constitution), demanding universal white male suffrage. "
            "The rebellion was suppressed but led to the adoption of a new "
            "Rhode Island constitution in 1843 — and the subsequent political "
            "realignment created the context for Clarke's Senate career.\n\n"
            "His Senate tenure (1847–1853) coincided with the Compromise of 1850 "
            "— Henry Clay's last great compromise, which addressed the territorial "
            "questions raised by the Mexican-American War's land acquisitions. "
            "The compromise required each senator to navigate the most explosive "
            "sectional issues of the era — the expansion of slavery, the Fugitive "
            "Slave Act, and the admission of California as a free state.\n\n"
            "After his Senate term, Clarke returned to Providence legal practice "
            "and lived until 1870 — witnessing the Civil War and the emancipation "
            "that resolved the slavery questions his Senate career had addressed."
        ),
        "importanceScore": 5,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Rhode Island Whig US Senator (1847–1853) who served during the Compromise of 1850; Brown University graduate (1809); Providence lawyer whose single Senate term coincided with the most explosive sectional debates of the antebellum era.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Rhode Island's post-Dorr Rebellion political realignment — and the adoption of a new constitution in 1843 — created the political context for Clarke's Senate career in the reformed Rhode Island political system",
            "Clarke's established reputation as a Providence lawyer — and his standing in Rhode Island's political community — provided the credentials for his Senate appointment",
            "The Compromise of 1850's need for senators who could navigate the sectional crisis — from both North and South — created the political moment in which Clarke's single Senate term was defined by the most consequential legislative compromise of the era"
        ],
        "effects": [
            "His Senate service during the Compromise of 1850 contributed to Rhode Island's representation in the most consequential sectional legislative debate of the antebellum period",
            "His single-term Senate career contributed to the transition of Rhode Island's politics from the Dorr Rebellion era into the antebellum period — bridging the reformed Rhode Island constitution and the national sectional crisis",
            "His return to Providence legal practice after his Senate term contributed to Rhode Island's legal community through the Civil War era — a career that spanned from the Dorr Rebellion to the aftermath of the Civil War",
            "His Brown University education connected him to the network of Rhode Island's educated professional class — which dominated the state's politics and legal institutions throughout the 19th century"
        ],
        "relationships": [
            {"entity": "US Senate from Rhode Island (1847–1853)", "relationship": "WHIG_SENATOR", "note": "Served as US Senator from Rhode Island (1847–1853) during the most consequential sectional debates of the antebellum era"},
            {"entity": "Compromise of 1850", "relationship": "SENATOR_DURING_AND_VOTING_ON", "note": "His Senate tenure coincided with the Compromise of 1850 — Clay's last great compromise, addressing the territorial questions raised by the Mexican-American War"},
            {"entity": "Rhode Island post-Dorr Rebellion politics", "relationship": "SENATOR_IN_REFORMED_SYSTEM_AFTER", "note": "Rose to the Senate in the political context created by the Dorr Rebellion (1842) and the subsequent adoption of Rhode Island's new constitution (1843)"},
            {"entity": "Brown University (Providence, RI)", "relationship": "ALUMNUS_OF_1809", "note": "Brown University graduate (1809) — connecting him to Rhode Island's educated professional and political establishment"},
            {"entity": "Providence, Rhode Island (legal and political career)", "relationship": "LEGAL_AND_POLITICAL_BASE", "note": "Established himself as a Providence lawyer — the professional base from which he entered Rhode Island politics and eventually the US Senate"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 32)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
