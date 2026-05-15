#!/usr/bin/env python3
"""
Batch 96 — 8 entities: Harrison Gray Otis, John Hathorne,
Henry A. Foster, Robert H. Adams, Karl Georg von Wächter,
Lemuel Hastings Arnold, Jonathan Grout, Alexander O. Anderson
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

    ("harrison-gray-otis", {
        "summary": (
            "Harrison Gray Otis (1765–1848) was an American Federalist politician "
            "and orator from Massachusetts who served in the U.S. House (1797–1801), "
            "the U.S. Senate (1817–1822), and as Mayor of Boston (1829–1832). "
            "He was the last major Federalist political leader — the chairman of the "
            "Hartford Convention (1814), the controversial gathering of New England "
            "Federalists who opposed the War of 1812 and discussed constitutional "
            "amendments to limit southern and western power. The Hartford Convention "
            "was widely perceived — unfairly or not — as potentially treasonous, "
            "and its timing just before the news of the Battle of New Orleans "
            "destroyed the Federalist Party's credibility.\n\n"
            "He was a Boston Brahmin who represented the Federalist commercial elite "
            "through the party's final crisis.\n\n"
            "Despite the Hartford Convention stigma, he remained a respected "
            "Boston civic figure and was elected mayor.\n\n"
            "'The Hartford Convention killed the Federalist Party — and Otis presided over both.'"
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Last major Federalist political leader; chairman of the Hartford Convention (1814) that fatally damaged the party; Massachusetts Federalist congressman, senator, and Mayor of Boston (1829–1832); Boston Brahmin who presided over the Federalist Party's final crisis and collapse.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Federalist Party's New England base — Massachusetts's commercial and legal elite whose opposition to the War of 1812 and Jeffersonian agrarianism made the party's last stronghold — created the political environment for Otis's career",
            "The War of 1812's unpopularity in New England — the commercial disruption, the embargo's damage to trade, and the perceived southern and western benefits of the war — created the political pressure that led to the Hartford Convention",
            "The Hartford Convention's political calculation — the Federalists' belief that constitutional amendments could restore northeastern commercial power — created the political gamble that Otis presided over and that backfired catastrophically"
        ],
        "effects": [
            "His Hartford Convention chairmanship contributed to the effective end of the Federalist Party — the convention's perceived disloyalty combined with the Battle of New Orleans news destroyed the party's credibility",
            "His Boston mayoralty contributed to the city's governance — the post-Federalist civic career of a Brahmin who survived the party's collapse",
            "His career contributed to the documentation of the Federalist Party's final years — the leadership of the party through its last political crisis",
            "His Senate service contributed Massachusetts's Federalist perspective during the Era of Good Feelings"
        ],
        "relationships": [
            {"target": "hartford-convention", "verb": "CHAIRS", "note": "Chairman of the 1814 New England Federalist convention"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Massachusetts Congressman 1797–1801"},
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Massachusetts Senator 1817–1822"},
            {"target": "boston", "verb": "GOVERNS_AS_MAYOR", "note": "Mayor of Boston 1829–1832"},
            {"target": "federalist-party", "verb": "LEADS_INTO_COLLAPSE", "note": "Last major Federalist leader whose Hartford Convention chairmanship destroyed the party"}
        ]
    }),

    ("john-hathorne", {
        "summary": (
            "John Hathorne (1641–1717) was a Massachusetts colonial magistrate and "
            "judge who served as one of the presiding judges in the Salem witch trials "
            "of 1692 — one of the most notorious miscarriages of justice in American "
            "colonial history. Unlike his fellow judge Samuel Sewall, who later "
            "publicly repented his role, Hathorne never expressed remorse for the "
            "trials that resulted in the execution of twenty people. He was a Salem "
            "merchant and the great-great-grandfather of the novelist Nathaniel "
            "Hawthorne — who added the 'w' to the family name reportedly out of "
            "shame over his ancestor's role in the trials.\n\n"
            "The Salem witch trials have become one of the defining symbols of "
            "religious hysteria and judicial injustice — and Hathorne, as the "
            "most aggressive interrogator of the accused, stands as one of its "
            "primary villains.\n\n"
            "Nathaniel Hawthorne's novels — especially 'The Scarlet Letter' and "
            "'The House of the Seven Gables' — were shaped by his ancestor's guilt.\n\n"
            "He was the judge who never repented."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Presiding judge at the Salem witch trials (1692) — one of America's most notorious judicial injustices; executed twenty people; never publicly repented unlike colleague Samuel Sewall; great-great-grandfather of Nathaniel Hawthorne (who added 'w' to family name in shame); symbol of religious hysteria and judicial injustice.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Salem witch trials — the 1692 mass hysteria in Essex County Massachusetts that produced accusations, torture, and executions — created the judicial crisis that Hathorne presided over",
            "Puritan New England's religious culture — the Calvinist framework that made witchcraft a capital offense and the tight community social pressure that made accusation believable — created the cultural environment for the trials",
            "Colonial Massachusetts's legal framework — the lack of adequate legal protections for the accused and the court's acceptance of spectral evidence — created the procedural failures that allowed the executions"
        ],
        "effects": [
            "His Salem witch trial judgments contributed to the deaths of twenty people — the most notorious judicial executions in American colonial history",
            "His failure to repent contributed to his place as the trial's primary villain — the contrast with Sewall's public repentance made Hathorne's silence more damning",
            "His ancestry shaped Nathaniel Hawthorne's literary imagination — the guilt and darkness that pervades Hawthorne's major works traces to his ancestor's role in the trials",
            "His historical legacy contributed to the Salem witch trials' symbolic meaning — the cautionary tale about religious hysteria, judicial injustice, and the danger of mass accusation"
        ],
        "relationships": [
            {"target": "salem-witch-trials", "verb": "PRESIDES_OVER", "note": "Presiding judge in the 1692 witch trials"},
            {"target": "nathaniel-hawthorne", "verb": "ANCESTOR_OF", "note": "Great-great-grandfather of the novelist (who added 'w' in shame)"},
            {"target": "samuel-sewall", "verb": "CO-PRESIDES_WITH", "note": "Fellow judge who later repented while Hathorne did not"},
            {"target": "colonial-massachusetts", "verb": "SERVES_IN", "note": "Salem magistrate and merchant"},
            {"target": "puritan-new-england", "verb": "EXEMPLIFIES_FAILURES_OF", "note": "Symbol of Puritan judicial and religious excess"}
        ]
    }),

    ("henry-a-foster", {
        "summary": (
            "Henry D. Foster (1808–1880) was an American Democratic politician "
            "from Pennsylvania who served in the U.S. House (1843–1847 and "
            "1871–1873) and was a candidate for Governor of Pennsylvania. "
            "Pennsylvania's Democratic Party in the 1840s was shaped by the "
            "tensions between its Jacksonian heritage, its coal and iron "
            "industrial communities (protectionist), and its increasingly "
            "vocal antislavery wing. Foster represented the western Pennsylvania "
            "Democratic tradition — the Greensburg area's mix of farming, "
            "early industry, and strong Democratic partisanship.\n\n"
            "His two separated House terms — with a twenty-four-year gap — "
            "illustrate the interrupted political careers common in the "
            "competitive antebellum and Reconstruction-era Pennsylvania politics.\n\n"
            "He ran for Governor of Pennsylvania in 1866 but lost to Republican "
            "John White Geary.\n\n"
            "He was a western Pennsylvania Democratic Party stalwart."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Pennsylvania Democratic Congressman (1843–1847 and 1871–1873); gubernatorial candidate 1866; Greensburg western Pennsylvania Democratic politician; two separated congressional terms illustrating antebellum and Reconstruction Pennsylvania competitive politics; lost 1866 governor race to Republican John White Geary.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Pennsylvania's competitive Democratic-Republican politics — the state's mix of industrial protectionism, Jacksonian agrarianism, and partisan competition — created the environment for Foster's interrupted congressional career",
            "Western Pennsylvania's Democratic culture — the Greensburg area's farming and early industrial communities that reliably supported Democratic candidates — provided Foster's political base",
            "The 1866 gubernatorial contest — the post-Civil War Republican dominance that made Democratic victory difficult — created the context of Foster's unsuccessful gubernatorial campaign"
        ],
        "effects": [
            "His congressional service contributed Pennsylvania's western Democratic perspective to the national House",
            "His gubernatorial candidacy contributed to Pennsylvania's Democratic opposition in the Reconstruction era",
            "His career contributed to the documentation of western Pennsylvania's antebellum Democratic political culture",
            "His two separated terms contributed to the historical record of Pennsylvania's competitive congressional politics"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Pennsylvania Congressman 1843–1847 and 1871–1873"},
            {"target": "pennsylvania", "verb": "RUNS_FOR_GOVERNOR_OF", "note": "Unsuccessful Democratic gubernatorial candidate 1866"},
            {"target": "democratic-party-united-states", "verb": "MEMBER_OF", "note": "Pennsylvania Democratic Party stalwart"},
            {"target": "john-white-geary", "verb": "LOSES_TO", "note": "Defeated by Republican Geary in 1866 governor race"},
            {"target": "western-pennsylvania", "verb": "REPRESENTS", "note": "Greensburg western Pennsylvania political base"}
        ]
    }),

    ("robert-h-adams", {
        "summary": (
            "Robert Henry Adams (1792–1830) was an American Democratic politician "
            "from Mississippi who served as U.S. Senator (1830) — dying after "
            "just a few months in office. His brief Senate tenure — he died at "
            "thirty-eight — makes him a footnote to Mississippi's early political "
            "history, but it illustrates the high mortality rates and brief "
            "tenures that characterized early American political careers. "
            "Mississippi in 1830 was a young state, having achieved statehood "
            "only in 1817 — its cotton economy was booming on the back of "
            "enslaved labor, and its political class was the wealthy planter "
            "elite that dominated the Deep South's politics.\n\n"
            "He died the same year he was elected — one of the shortest Senate "
            "tenures in American history.\n\n"
            "He was a Natchez Mississippi lawyer and planter.\n\n"
            "He represented Mississippi's early planter political class."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Mississippi Democratic Senator (1830) who died after a few months in office — one of the shortest Senate tenures in American history; Natchez lawyer and planter; represented Mississippi's early cotton-boom planter political class; died at thirty-eight; illustrates the high mortality and brief tenures of early American politics.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Mississippi's early statehood cotton boom — the rapid economic growth of the cotton economy on enslaved labor that made Mississippi one of the fastest-growing antebellum states — created the planter political class that Adams represented",
            "The high mortality rates of the early republic — the disease burden, limited medicine, and physical demands of the period — created the pattern of early deaths that shortened many political careers",
            "Mississippi's Democratic political culture — the state's alignment with Jacksonian Democracy — created the political context of Adams's brief Senate appointment"
        ],
        "effects": [
            "His brief Senate tenure contributed to the historical record of Mississippi's founding political class",
            "His early death contributed to the pattern of political vacancies that shaped Mississippi's early Senate representation",
            "His career contributed to the documentation of Natchez's planter political elite",
            "His death illustrated the mortality risks that made early American political careers unpredictable"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Mississippi Senator 1830 — died after months in office"},
            {"target": "mississippi", "verb": "REPRESENTS", "note": "Natchez Mississippi planter-lawyer"},
            {"target": "democratic-party-united-states", "verb": "MEMBER_OF", "note": "Mississippi Jacksonian Democrat"},
            {"target": "natchez-mississippi", "verb": "BASED_IN", "note": "Natchez political and legal community"},
            {"target": "mississippi-cotton-economy", "verb": "REPRESENTS", "note": "Planter politician in the cotton boom era"}
        ]
    }),

    ("karl-georg-von-wächter", {
        "summary": (
            "Karl Georg von Wächter (1797–1880) was a German jurist and legal "
            "scholar who was one of the most important legal theorists of "
            "19th-century Germany. A professor at the universities of Tübingen "
            "and Leipzig, Wächter was a leading figure in the Historical School "
            "of Law — the movement founded by Savigny that argued legal systems "
            "should grow organically from national historical experience rather "
            "than being rationally constructed. He was particularly significant "
            "for his work on private international law (conflict of laws) and "
            "criminal law — his scholarship helped establish these as distinct "
            "legal disciplines.\n\n"
            "In his later career he served as a judge on the Reich Supreme Court "
            "(Reichsgericht) following German unification in 1871.\n\n"
            "He bridged the Romantic-era Historical School and the positivist "
            "Pandectist tradition that dominated German law in the later 19th century.\n\n"
            "He was one of the founders of modern German conflict-of-laws theory."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "German Historical School jurist and legal scholar; professor at Tübingen and Leipzig; foundational scholar of private international law (conflict of laws) and criminal law; served on the German Reichsgericht after 1871 unification; bridged Romantic Historical School and Pandectist positivism; founding figure of modern German conflict-of-laws theory.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Historical School of Law — Savigny's movement for organically grounded national legal systems rooted in historical development — created the intellectual tradition within which Wächter worked",
            "German legal education's professionalization — the 19th-century development of university legal scholarship as a rigorous academic discipline — created the institutional framework for Wächter's professorial career",
            "German unification's legal demands — the 1871 Empire's need for a unified national legal system — created the institutional role of the Reichsgericht that Wächter served"
        ],
        "effects": [
            "His private international law scholarship contributed to the theoretical foundations of modern conflict-of-laws doctrine",
            "His criminal law work contributed to German criminal jurisprudence — the scholarly foundation for later codification",
            "His Reichsgericht service contributed to the development of unified German judicial institutions after 1871",
            "His Historical School teaching contributed to the formation of German legal scholars who shaped the 19th and 20th centuries"
        ],
        "relationships": [
            {"target": "university-of-tübingen", "verb": "TEACHES_AT", "note": "Professor at Tübingen"},
            {"target": "university-of-leipzig", "verb": "TEACHES_AT", "note": "Professor at Leipzig"},
            {"target": "historical-school-of-law", "verb": "PARTICIPATES_IN", "note": "Leading Historical School jurist"},
            {"target": "reichsgericht", "verb": "SERVES_ON", "note": "German Reich Supreme Court judge after 1871"},
            {"target": "private-international-law", "verb": "FOUNDS_AS_DISCIPLINE", "note": "Foundational scholar of conflict-of-laws theory"}
        ]
    }),

    ("lemuel-hastings-arnold", {
        "summary": (
            "Lemuel Hastings Arnold (1792–1852) was an American Democratic politician "
            "from Rhode Island who served in the U.S. House (1845–1847) and as "
            "Governor of Rhode Island (1831–1833). His governorship came during "
            "a critical moment in Rhode Island's history — the years immediately "
            "preceding the Dorr Rebellion (1842), the constitutional crisis over "
            "Rhode Island's antiquated colonial charter that restricted voting "
            "to property owners. Arnold's term predated the rebellion, but "
            "the underlying issue of suffrage restriction was already creating "
            "political tension. Rhode Island was the last New England state "
            "still governed by its colonial charter rather than a modern "
            "state constitution.\n\n"
            "His House term came after the Dorr Rebellion's resolution — "
            "Rhode Island had adopted a new constitution in 1843 that "
            "somewhat expanded suffrage.\n\n"
            "He was a Providence Rhode Island politician.\n\n"
            "He represented Rhode Island's Democratic Party during its transitional period."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Rhode Island Governor (1831–1833) and Congressman (1845–1847); governorship preceding the Dorr Rebellion suffrage crisis; Rhode Island's antiquated colonial charter; Providence Democratic politician; served during Rhode Island's transition from colonial charter to modern constitutional government.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Rhode Island's colonial charter — the state's governance under the 1663 charter that restricted voting to property owners — created the political tension that preceded the Dorr Rebellion and shaped Arnold's political environment",
            "Rhode Island's Democratic Party development — the state's Jacksonian Democratic alignment within its restricted suffrage system — created the political base for Arnold's career",
            "The Dorr Rebellion's shadow — the growing popular agitation for expanded suffrage that would eventually produce the 1842 constitutional crisis — created the underlying tension of Arnold's governorship"
        ],
        "effects": [
            "His governorship contributed to Rhode Island's governance during the pre-Dorr Rebellion period",
            "His career contributed to the documentation of Rhode Island's political transition from colonial charter to modern constitution",
            "His House service contributed Rhode Island's Democratic perspective after the Dorr Rebellion's resolution",
            "His career contributed to the historical record of Rhode Island's Democratic leadership during a period of constitutional crisis"
        ],
        "relationships": [
            {"target": "rhode-island", "verb": "GOVERNS", "note": "Governor of Rhode Island 1831–1833"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Rhode Island Congressman 1845–1847"},
            {"target": "dorr-rebellion", "verb": "PRECEDES", "note": "Governor during the pre-rebellion suffrage tension"},
            {"target": "rhode-island-colonial-charter", "verb": "GOVERNS_UNDER", "note": "Governor under the antiquated 1663 colonial charter"},
            {"target": "democratic-party-united-states", "verb": "MEMBER_OF", "note": "Rhode Island Democratic politician"}
        ]
    }),

    ("jonathan-grout", {
        "summary": (
            "Jonathan Grout (1737–1807) was an American Democratic-Republican "
            "politician from Massachusetts who served in the First and Second "
            "Congresses (1789–1791) as one of Massachusetts's original representatives "
            "in the new federal government. The First Congress was among the "
            "most historically significant in American history — it established "
            "the Bill of Rights, created the federal judiciary through the "
            "Judiciary Act of 1789, established the executive departments, "
            "and set the precedents for how Congress would function. "
            "Grout was an Anti-Federalist who had opposed the Constitution's "
            "ratification — his presence in the First Congress represented "
            "the accommodation of Anti-Federalist concerns through the "
            "promise of a Bill of Rights.\n\n"
            "He was a Petersham Massachusetts lawyer and farmer.\n\n"
            "He was among the original Anti-Federalist members of the first Congress.\n\n"
            "He witnessed the founding of the federal government from the inside."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Massachusetts Anti-Federalist First and Second Congress member (1789–1791); original member of the First Congress that established the Bill of Rights, federal judiciary, and executive departments; Anti-Federalist who opposed ratification but served in the founding Congress; Petersham Massachusetts lawyer-farmer.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Massachusetts's Anti-Federalist tradition — the state's substantial opposition to the Constitution's ratification, rooted in fears of centralized power — created the political constituency that elected Anti-Federalist representatives to the First Congress",
            "The promise of a Bill of Rights — the accommodation that brought Anti-Federalists like Grout into support for the Constitution on the understanding that amendments would protect individual rights — created the political settlement that allowed the First Congress to function",
            "Massachusetts's farming communities — the rural districts that most feared federal taxation and centralized power — provided Grout's political base"
        ],
        "effects": [
            "His First Congress service contributed to the founding legislative work — the bills establishing the federal judiciary, executive departments, and the Bill of Rights",
            "His Anti-Federalist voice contributed to the pressure for the Bill of Rights — the accommodation of constitutional opponents that produced the first ten amendments",
            "His Massachusetts representation contributed to the new federal government's first sessions — the foundational debates that established congressional precedents",
            "His career contributed to the historical record of Anti-Federalist participation in the founding government"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Massachusetts Congressman in First and Second Congress 1789–1791"},
            {"target": "bill-of-rights", "verb": "CONTRIBUTES_TO_PASSAGE_OF", "note": "Anti-Federalist congressman whose concerns drove Bill of Rights adoption"},
            {"target": "judiciary-act-of-1789", "verb": "VOTES_ON", "note": "First Congress member during federal judiciary establishment"},
            {"target": "anti-federalists", "verb": "REPRESENTS", "note": "Anti-Federalist who opposed Constitution's ratification"},
            {"target": "first-congress", "verb": "SERVES_IN", "note": "Original member of the founding First Congress"}
        ]
    }),

    ("alexander-o-anderson", {
        "summary": (
            "Alexander Outlaw Anderson (1794–1869) was an American Democratic "
            "politician from Tennessee who served as U.S. Senator (1840–1841) — "
            "a brief appointment to complete an unexpired term. Tennessee in "
            "this period was divided between its Democratic areas (East Tennessee "
            "had strong Whig tendencies, West Tennessee was heavily Democratic "
            "due to its cotton culture) — a politically competitive state that "
            "would swing between parties. Anderson served during the transitional "
            "period of Van Buren's final year and Harrison's brief presidency.\n\n"
            "He was a Knoxville Tennessee lawyer who practiced at the Tennessee bar.\n\n"
            "His brief Senate appointment was a caretaker tenure completing "
            "the remainder of a term rather than a full independent election.\n\n"
            "He represented Tennessee's Democratic legal community in Knoxville."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Tennessee Democratic Senator (1840–1841); brief appointment to complete unexpired term during Van Buren-Harrison transition; Knoxville Tennessee lawyer; represented Tennessee's Democratic legal community; served during politically competitive Tennessee's Van Buren-era politics.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Tennessee's competitive Democratic-Whig politics — the state's divided political geography with Whig East Tennessee and Democratic West Tennessee — created the close political environment of Anderson's brief tenure",
            "The Van Buren administration's final year — the economic depression and the transition to Harrison's brief Whig presidency — created the political context of Anderson's Senate appointment",
            "Tennessee's Democratic legal community — the Knoxville lawyers who supported the Democratic Party — provided the professional base for Anderson's appointment"
        ],
        "effects": [
            "His brief Senate tenure contributed to the historical record of Tennessee's antebellum senatorial appointments",
            "His caretaker service contributed to Tennessee's Senate representation during the Van Buren-Harrison transition",
            "His career contributed to the documentation of Tennessee's Knoxville Democratic legal community",
            "His appointment contributed to the pattern of brief Senate tenures that characterized politically competitive states"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Tennessee Senator 1840–1841 — brief appointment"},
            {"target": "tennessee", "verb": "REPRESENTS", "note": "Knoxville Tennessee Democratic lawyer"},
            {"target": "democratic-party-united-states", "verb": "MEMBER_OF", "note": "Tennessee Jacksonian Democrat"},
            {"target": "martin-van-buren", "verb": "SERVES_DURING_FINAL_YEAR_OF", "note": "Senator during Van Buren's final presidential year"},
            {"target": "knoxville-tennessee", "verb": "BASED_IN", "note": "Knoxville legal and political community"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 96 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich(slug, data)
    print("Done.")
