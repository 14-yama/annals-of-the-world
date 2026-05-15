#!/usr/bin/env python3
"""
Batch 87 — 8 entities: Tomás de Anchorena, Armand-Gaston Camus,
John G. Jackson, Roger Ducos, Samuel Ashe, Simon Greenleaf,
Wilhelm Frimann Koren Christie, William Addams
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

    ("tomás-de-anchorena", {
        "summary": (
            "Tomás Manuel de Anchorena "
            "(1783–1847) was an "
            "Argentine lawyer, "
            "politician, and statesman "
            "who played a central "
            "role in the independence "
            "and early republican "
            "politics of the "
            "Río de la Plata. "
            "As a member of "
            "the 1813 Assembly "
            "and a delegate "
            "to the 1816 Congress "
            "of Tucumán — which "
            "declared Argentine "
            "independence on "
            "July 9, 1816 — "
            "Anchorena was "
            "a founding father "
            "of the Argentine nation. "
            "A wealthy Buenos Aires "
            "landowner, he was "
            "also a close ally "
            "of Juan Manuel "
            "de Rosas — the "
            "Federalist caudillo "
            "whose dominance "
            "of Buenos Aires "
            "province from "
            "the 1820s to 1852 "
            "shaped Argentina's "
            "formative political struggles.\n\n"
            "His family's estancia "
            "(ranch) wealth "
            "and his Buenos Aires "
            "commercial elite "
            "connections placed "
            "him among Argentina's "
            "most influential "
            "early political families.\n\n"
            "He held various "
            "high offices including "
            "governor of Buenos Aires.\n\n"
            "He was a founding "
            "father of Argentine "
            "nationhood."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Argentine founding father (1783–1847); delegate to the Congress of Tucumán that declared independence (July 9, 1816); 1813 Assembly member; close ally of Federalist caudillo Juan Manuel de Rosas; wealthy Buenos Aires landowning elite; governor of Buenos Aires province; central figure in Argentina's independence and early republican formation.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Argentine independence movement — the Río de la Plata's break from Spanish rule following the 1810 May Revolution and the subsequent drive toward formal independence — created the political context for Anchorena's role at the Congress of Tucumán",
            "The Buenos Aires Creole elite's political leadership — the wealthy landowners and merchants who dominated Río de la Plata politics and provided the leadership class for independence and early republican governance — created the social context for Anchorena's prominence",
            "The Unitarian-Federalist civil wars — the internal Argentine conflict between Buenos Aires Unitarians and provincial Federalists that shaped post-independence politics — aligned Anchorena with the Federalist Rosas faction through both ideological affinity and economic interest"
        ],
        "effects": [
            "His Congress of Tucumán participation contributed to the formal declaration of Argentine independence — one of the most consequential political decisions in Latin American history",
            "His Rosas alliance contributed to the Federalist political order that dominated Buenos Aires for three decades — the caudillo period that shaped Argentina's path to eventual national consolidation",
            "His elite Buenos Aires family's political engagement contributed to the oligarchic tradition that would shape Argentine politics through the 19th century",
            "His career contributed to the transition from colonial to republican governance in the Río de la Plata — the early Argentine state-building that his generation performed"
        ],
        "relationships": [
            {"target": "congress-of-tucuman-1816", "verb": "DELEGATES_TO", "note": "Declaration of Independence delegate"},
            {"target": "juan-manuel-de-rosas", "verb": "ALLIED_WITH", "note": "Close political ally of the Federalist caudillo"},
            {"target": "buenos-aires-province", "verb": "GOVERNS", "note": "Governor of Buenos Aires province"},
            {"target": "argentine-independence", "verb": "HELPS_DECLARE", "note": "Founding father who signed independence declaration"},
            {"target": "assembly-of-year-xiii", "verb": "SERVES_IN", "note": "1813 Assembly member"}
        ]
    }),

    ("armand-gaston-camus", {
        "summary": (
            "Armand-Gaston Camus "
            "(1740–1804) was a "
            "French lawyer, "
            "archivist, and "
            "revolutionary politician "
            "who served in the "
            "Estates-General of "
            "1789 and the National "
            "Assembly, and later "
            "became the first "
            "Director of the "
            "Archives Nationales "
            "— founding and "
            "organizing France's "
            "national archive system. "
            "An ardent Gallican "
            "Catholic who championed "
            "the Civil Constitution "
            "of the Clergy "
            "(1790), Camus "
            "was one of the "
            "most distinguished "
            "lawyers of pre-revolutionary "
            "France — the "
            "avocat au Conseil "
            "du Roi before "
            "becoming a revolutionary legislator. "
            "Captured by Austrian forces "
            "in 1792 when "
            "he was with "
            "Dumouriez's army "
            "to present "
            "a decree to "
            "the general, "
            "he spent four "
            "years as an "
            "Austrian prisoner "
            "before returning "
            "to France to "
            "organize the archives.\n\n"
            "His four-year "
            "Austrian captivity — "
            "one of the "
            "few National Assembly "
            "members captured "
            "by the enemy "
            "— was a remarkable biographical episode.\n\n"
            "The Archives Nationales "
            "he founded "
            "remains France's "
            "national memory institution.\n\n"
            "He was a pivotal "
            "figure in French "
            "archival history."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "French revolutionary politician (1740–1804) and founding Director of the Archives Nationales; Estates-General and National Assembly member; champion of the Civil Constitution of the Clergy; captured by Austria 1792 and held four years; Gallican Catholic lawyer who built France's national archival system — a cornerstone of French cultural memory.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The French Revolution — the political crisis of 1789 that transformed the royal lawyer and parliamentary advocate Camus into a revolutionary legislator in the Estates-General and National Assembly — created the context of his political career",
            "The Civil Constitution of the Clergy debate — the National Assembly's controversial reorganization of the French Catholic Church that Camus championed as a Gallican Catholic — engaged his combined legal and religious expertise",
            "Napoleon's administrative ordering of France — the Consulate's need to organize the revolutionary era's accumulated papers into a coherent national archive — created the institutional role that Camus would fill as the Archives Nationales' first director"
        ],
        "effects": [
            "His Archives Nationales directorship created France's national archive system — the institutional foundation for preserving French historical memory that remains one of the world's great archives",
            "His Civil Constitution of the Clergy advocacy contributed to the revolutionary reorganization of French Catholicism — one of the most consequential and controversial ecclesiastical reforms in French history",
            "His four-year Austrian captivity contributed to the historical record of the Revolution's diplomatic complications — the imprisoned commissioner becoming a symbol of the conflict between the Republic and the coalition powers",
            "His archival work contributed to the systematic organization and preservation of the documents generated by the revolutionary decade — enabling subsequent historical scholarship on the Revolution"
        ],
        "relationships": [
            {"target": "archives-nationales-france", "verb": "FOUNDS", "note": "First Director of France's national archive"},
            {"target": "estates-general-1789", "verb": "SERVES_IN", "note": "Estates-General and National Assembly member"},
            {"target": "civil-constitution-of-the-clergy", "verb": "CHAMPIONS", "note": "Gallican Catholic advocate for clerical reorganization"},
            {"target": "french-revolution", "verb": "PARTICIPATES_IN", "note": "Revolutionary lawyer-legislator"},
            {"target": "habsburg-austria", "verb": "CAPTURED_BY", "note": "Austrian prisoner 1792–1796"}
        ]
    }),

    ("john-g-jackson", {
        "summary": (
            "John George Jackson (1777–1825) "
            "was an American "
            "Democratic-Republican "
            "politician from Virginia/West Virginia "
            "who served in the "
            "U.S. House (1803–1811 "
            "and 1813–1817) — "
            "with a notable "
            "personal distinction: "
            "he was the brother-in-law "
            "of President James "
            "Madison, having "
            "married Madison's "
            "sister-in-law. "
            "A western Virginia "
            "congressman representing "
            "the trans-Allegheny "
            "region that would "
            "eventually become "
            "West Virginia, "
            "Jackson championed "
            "the interests of "
            "western settlers "
            "against the tidewater "
            "Virginia planter establishment. "
            "He was an enthusiastic "
            "supporter of the "
            "War of 1812 "
            "— the 'War Hawks' "
            "congressman "
            "whose frontier "
            "constituents welcomed "
            "war with Britain "
            "and wanted "
            "Canadian expansion.\n\n"
            "His brother-in-law "
            "connection to Madison "
            "gave him White House "
            "access that "
            "few frontier "
            "congressmen enjoyed.\n\n"
            "He was appointed "
            "a federal district "
            "judge after "
            "his congressional career.\n\n"
            "He was a Clarksburg "
            "Virginia (now West Virginia) "
            "lawyer."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Virginia Democratic-Republican Congressman (1803–1811 and 1813–1817); brother-in-law of President Madison; War Hawk supporting the War of 1812; western Virginia frontier champion against tidewater establishment; later federal district judge; represented the trans-Allegheny region that became West Virginia.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Western Virginia's frontier politics — the trans-Allegheny region's distinctive character as a frontier settlement area economically and culturally different from tidewater Virginia — created the political constituency for Jackson's western Virginia perspective",
            "Jackson's Madison family connection — his marriage into the Madison family network — gave him access and influence in the Jeffersonian circle that western Virginia congressmen rarely enjoyed",
            "The War of 1812 War Hawk movement — the group of young Jeffersonian Republicans who demanded war with Britain over impressment and commerce — created the political identity of Jackson's second House period as a frontier war enthusiast"
        ],
        "effects": [
            "His congressional service contributed western Virginia's frontier perspective to the Madison-era debates — the trans-Allegheny settler voice that differed from tidewater Virginia's planter establishment",
            "His War Hawk support contributed to the congressional coalition that pushed Madison toward declaring war in June 1812 — the frontier congressmen whose constituencies wanted British removal from the Northwest",
            "His federal judgeship contributed to the development of federal judicial institutions in western Virginia — organizing the courts of the trans-Allegheny region",
            "His career contributed to the political tradition of western Virginia's distinctiveness — the regional identity that would eventually produce West Virginia's separation from Virginia in 1863"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Virginia Congressman 1803–1811 and 1813–1817"},
            {"target": "james-madison", "verb": "RELATED_TO", "note": "Brother-in-law of President Madison"},
            {"target": "war-of-1812", "verb": "SUPPORTS", "note": "War Hawk congressman supporting the war"},
            {"target": "west-virginia", "verb": "REPRESENTS", "note": "Trans-Allegheny frontier congressman"},
            {"target": "federal-judiciary", "verb": "SERVES_IN", "note": "Federal district judge after congressional career"}
        ]
    }),

    ("roger-ducos", {
        "summary": (
            "Roger Ducos (1747–1816) "
            "was a French "
            "revolutionary politician "
            "who served as "
            "one of three "
            "Consuls in "
            "the French First "
            "Consulate — the "
            "triumvirate of "
            "Sieyès, Bonaparte, "
            "and Ducos that "
            "governed France "
            "for a few weeks "
            "after the 18 Brumaire "
            "coup (November 9, 1799). "
            "A Montagnard "
            "in the National "
            "Convention who "
            "voted for Louis XVI's death, "
            "Ducos survived "
            "the Thermidor "
            "reaction and continued "
            "in republican politics "
            "through the Directory. "
            "His role in the "
            "Brumaire coup "
            "was that of "
            "an enabler — "
            "he provided "
            "constitutional "
            "cover by resigning "
            "as a Director "
            "to trigger "
            "the emergency "
            "that Bonaparte "
            "could exploit. "
            "Within weeks "
            "he was replaced "
            "as a Consul "
            "by Cambacérès "
            "and Lebrun.\n\n"
            "His 18 Brumaire "
            "participation placed "
            "him at one of "
            "the most pivotal "
            "moments of "
            "modern history — "
            "the end of "
            "the First Republic "
            "and the birth "
            "of Napoleon's "
            "Consulate.\n\n"
            "He received "
            "an imperial "
            "title under Napoleon.\n\n"
            "He was a Gascon "
            "lawyer and "
            "revolutionary politician."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "French revolutionary politician (1747–1816); one of three Consuls after 18 Brumaire (1799); voted for Louis XVI's execution; National Convention Montagnard; Directory member whose resignation helped enable the Brumaire coup; directly participated in the transition from the First Republic to Napoleon's Consulate.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The 18 Brumaire coup — Napoleon Bonaparte's seizure of power on November 9, 1799 that required compliant politicians to resign from the Directory and legitimate the constitutional transition — created the moment for Ducos's role as the Consulate's third member",
            "Ducos's Thermidor survival and political flexibility — his ability to navigate from Montagnard revolutionary to Directory politician to Brumaire conspirator — reflected the political pragmatism that enabled his continued relevance",
            "The Directory's crisis — the structural weakness of the five-Director executive that the Brumaire conspirators exploited by engineering a constitutional emergency — created the mechanism through which Ducos's resignation contributed to Napoleon's seizure of power"
        ],
        "effects": [
            "His Consul role contributed to the transitional legitimacy of the Brumaire coup — the brief constitutional cover that enabled the transition from the Directory to the permanent Consulate",
            "His vote for Louis XVI's death contributed to the regicide that committed the Convention to the Republic's survival — one of the most consequential votes in French history",
            "His rapid replacement by more capable politicians illustrated the difference between transitional facilitators and substantive statesmen — Ducos was needed to enable the coup but not to govern afterward",
            "His career illustrated the political survival strategies of the revolutionary generation — the former Montagnards who navigated Thermidor, the Directory, and Brumaire by subordinating ideology to political survival"
        ],
        "relationships": [
            {"target": "french-consulate", "verb": "SERVES_AS_CONSUL_IN", "note": "One of three Consuls after 18 Brumaire"},
            {"target": "coup-of-18-brumaire", "verb": "PARTICIPATES_IN", "note": "Directory member whose resignation enabled the coup"},
            {"target": "napoleon-i", "verb": "ENABLES_RISE_OF", "note": "Co-Consul who facilitated Bonaparte's seizure of power"},
            {"target": "national-convention-france", "verb": "SERVES_IN", "note": "Montagnard Convention member"},
            {"target": "trial-of-louis-xvi", "verb": "VOTES_IN", "note": "Voted for the king's execution"}
        ]
    }),

    ("samuel-ashe", {
        "summary": (
            "Samuel Ashe (1725–1813) "
            "was an American "
            "lawyer, judge, and "
            "statesman from North "
            "Carolina who served "
            "as Governor of "
            "North Carolina "
            "(1795–1798) and "
            "Chief Justice "
            "of the North Carolina "
            "Superior Court. "
            "A veteran of the "
            "colonial and revolutionary "
            "era, Ashe participated "
            "in the resistance "
            "to the Stamp Act "
            "and the Regulator "
            "movement — "
            "the complex "
            "pre-revolutionary "
            "North Carolina "
            "frontier uprising "
            "against colonial "
            "taxation. His "
            "governorship spanned "
            "the turbulent "
            "mid-1790s — "
            "Jay's Treaty controversy, "
            "the XYZ Affair's "
            "approach, and "
            "the Quasi-War "
            "with France. "
            "North Carolina "
            "in this era "
            "was strongly "
            "Jeffersonian Republican "
            "— its planter-farmer "
            "electorate suspicious "
            "of the Federalist "
            "commercial and "
            "financial elite.\n\n"
            "His long career "
            "spanning from "
            "colonial resistance "
            "to the early "
            "republic illustrated "
            "the founding generation's "
            "complete arc.\n\n"
            "He died at 88 — "
            "one of the "
            "last survivors "
            "of the pre-revolutionary era.\n\n"
            "He was a North "
            "Carolina founding "
            "generation statesman."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "North Carolina Governor (1795–1798) and Chief Justice of the North Carolina Superior Court; veteran of colonial Stamp Act resistance and Regulator movement; Revolutionary era statesman; governorship during Jay's Treaty and Quasi-War crises; died at 88 as one of the last survivors of the pre-revolutionary generation.",
            "significanceCategory": "regional"
        },
        "causes": [
            "North Carolina's colonial political resistance — the province's strong anti-colonial tradition from the Stamp Act resistance through the Regulator movement — created the revolutionary credentials that shaped Ashe's career arc",
            "The Jeffersonian Republican dominance of North Carolina — the planter-farmer electorate's hostility to Federalist commercial policies — created the political environment for Ashe's gubernatorial election in the mid-1790s",
            "North Carolina's growing importance in American governance — the state's size and agricultural wealth making its governors significant regional figures — gave Ashe's governorship importance beyond local politics"
        ],
        "effects": [
            "His governorship contributed North Carolina's Jeffersonian perspective to the Jay's Treaty and Quasi-War crises — the state's resistance to Federalist foreign policy",
            "His Chief Justice service contributed to North Carolina's developing legal system — building the state judiciary in the generation after independence",
            "His Stamp Act and Regulator-era participation contributed to the pre-revolutionary resistance tradition — the colonial political activism that led to the Revolution",
            "His 88-year life contributed to the living memory of the founding era — one of the longest-lived founding generation statesmen whose lifespan bridged colonial and antebellum America"
        ],
        "relationships": [
            {"target": "north-carolina", "verb": "GOVERNS", "note": "Governor of North Carolina 1795–1798"},
            {"target": "north-carolina-superior-court", "verb": "LEADS", "note": "Chief Justice of North Carolina's superior court"},
            {"target": "stamp-act", "verb": "RESISTS", "note": "Colonial resistance participant"},
            {"target": "regulator-movement", "verb": "ENGAGES_WITH", "note": "North Carolina Regulator movement participant"},
            {"target": "jays-treaty", "verb": "GOVERNS_DURING", "note": "Governor during the Jay's Treaty controversy"}
        ]
    }),

    ("simon-greenleaf", {
        "summary": (
            "Simon Greenleaf (1783–1853) "
            "was an American "
            "legal scholar who "
            "served as Royall "
            "Professor of Law "
            "at Harvard Law School "
            "(1833–1848) and "
            "whose three-volume "
            "'Treatise on the "
            "Law of Evidence' "
            "(1842–1853) became "
            "the most authoritative "
            "American work on "
            "evidence law "
            "for the 19th century. "
            "Greenleaf transformed "
            "Harvard Law School "
            "alongside Joseph "
            "Story — the two "
            "professors who "
            "built the school "
            "into America's "
            "preeminent law "
            "school in the "
            "antebellum era. "
            "His 'Treatise on "
            "Evidence' was "
            "cited by courts "
            "across America "
            "and Britain for "
            "decades and shaped "
            "the development "
            "of Anglo-American "
            "evidence law. "
            "He also wrote "
            "a notable examination "
            "of the Gospels "
            "from a legal "
            "evidence perspective.\n\n"
            "His partnership "
            "with Joseph Story "
            "at Harvard built "
            "the case method "
            "and the scholarly "
            "tradition that "
            "made American "
            "legal education distinctive.\n\n"
            "He was Maine's "
            "Reporter of Decisions "
            "before moving to Harvard.\n\n"
            "'Facts are stubborn things.'"
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Harvard Law professor (1833–1848) and author of the 'Treatise on the Law of Evidence' (1842–1853) — the most authoritative American evidence law work of the 19th century; built Harvard Law School with Joseph Story; Maine's Reporter of Decisions; his evidence treatise shaped Anglo-American evidence law for generations.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Harvard Law School's development — the school's growth under Joseph Story into a serious graduate law school — created the institutional context in which Greenleaf's evidence scholarship could flourish and achieve its dominant influence",
            "The absence of an authoritative American evidence law treatise — the gap between American judicial practice and the available legal literature — created the need for the systematic treatment that Greenleaf's three volumes provided",
            "Greenleaf's Maine legal career — his years as Maine's Reporter of Decisions giving him comprehensive exposure to American judicial evidence practice — provided the empirical foundation for his treatise's authoritative treatment of American cases"
        ],
        "effects": [
            "His 'Treatise on Evidence' became the standard American authority on evidence law — the treatise that courts cited and practitioners relied on throughout the 19th century",
            "His Harvard professorship contributed to building the preeminent American law school — the Story-Greenleaf partnership that transformed Harvard Law into America's leading legal academic institution",
            "His evidence scholarship influenced the development of Anglo-American evidence rules — shaping the legal standards for testimony, documents, and proof across the common law world",
            "His Gospel examination from a legal evidence perspective contributed to the 19th-century intersection of legal and religious scholarship — an unusual contribution that illustrated the era's confidence in applying legal methodology to historical questions"
        ],
        "relationships": [
            {"target": "harvard-law-school", "verb": "TEACHES_AT", "note": "Royall Professor building Harvard Law 1833–1848"},
            {"target": "joseph-story", "verb": "COLLABORATES_WITH", "note": "Partner in building Harvard Law School"},
            {"target": "treatise-on-evidence", "verb": "AUTHORS", "note": "Author of the century's leading evidence law treatise"},
            {"target": "american-legal-education", "verb": "TRANSFORMS", "note": "Builder of the antebellum American law school model"},
            {"target": "maine-supreme-court", "verb": "SERVES", "note": "Maine Reporter of Decisions before Harvard"}
        ]
    }),

    ("wilhelm-frimann-koren-christie", {
        "summary": (
            "Wilhelm Frimann Koren "
            "Christie (1778–1849) "
            "was a Norwegian "
            "lawyer, politician, "
            "and constitutionalist "
            "who played a leading "
            "role in drafting "
            "the Norwegian Constitution "
            "of 1814 — one of "
            "the world's oldest "
            "and most liberal "
            "constitutions still "
            "in force. Christie "
            "served as president "
            "of the Constitutional "
            "Assembly at Eidsvoll "
            "in 1814 — the "
            "gathering of "
            "112 elected men "
            "who drafted the "
            "constitution in "
            "the brief window "
            "of Norwegian de facto "
            "independence between "
            "the end of Danish "
            "rule and the "
            "forced union "
            "with Sweden. "
            "He went on to "
            "serve as president "
            "of the Storting "
            "(Norwegian parliament) "
            "and as a judge "
            "on the Supreme Court.\n\n"
            "The Norwegian Constitution "
            "of May 17, 1814 "
            "— still celebrated "
            "as Norway's national day "
            "— is considered "
            "one of the most "
            "democratic constitutions "
            "of its era.\n\n"
            "He was Bergen's "
            "leading legal "
            "and political figure.\n\n"
            "'A free people must "
            "be governed by "
            "free laws.'"
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Norwegian constitutionalist (1778–1849) and president of the Eidsvoll Constitutional Assembly that drafted the Norwegian Constitution of May 17, 1814 — one of the world's oldest democracies still in force; president of the Storting; Supreme Court judge; Bergen's leading legal figure; Norwegian independence champion.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The collapse of Denmark-Norway following Napoleon's defeat — the 1814 Peace of Kiel that ceded Norway from Denmark to Sweden and created the brief window of Norwegian de facto independence — created the moment for the Eidsvoll Constitutional Assembly",
            "Christie's distinguished legal career and Bergen's political prominence — his standing as a leading Norwegian lawyer and Bergen's importance as Norway's commercial capital — made him a natural choice to preside over the constitutional assembly",
            "The liberal constitutional tradition — the Enlightenment and revolutionary era's legacy of written constitutions — provided the intellectual framework that Christie and the Eidsvoll assembly drew upon in creating Norway's liberal document"
        ],
        "effects": [
            "His Constitutional Assembly presidency contributed to the drafting of the Norwegian Constitution of 1814 — one of the most democratic constitutions of its era and one still in force today",
            "His Storting presidency contributed to the institutional development of Norway's parliament — establishing the legislative traditions of the new constitutional state",
            "His Supreme Court service contributed to the Norwegian judicial interpretation of the new constitution — building the jurisprudence of constitutional governance",
            "May 17, 1814 — the constitution's signing date — became Norway's national day, the most celebrated day in Norwegian history, a legacy Christie helped create"
        ],
        "relationships": [
            {"target": "norwegian-constitution-1814", "verb": "DRAFTS", "note": "President of the Eidsvoll assembly that drafted the constitution"},
            {"target": "eidsvoll-assembly", "verb": "PRESIDES_OVER", "note": "Constitutional Assembly president"},
            {"target": "storting", "verb": "PRESIDES_OVER", "note": "President of the Norwegian parliament"},
            {"target": "norwegian-independence", "verb": "CHAMPIONS", "note": "Constitutional independence leader"},
            {"target": "bergen-norway", "verb": "LEADS", "note": "Bergen's leading legal and political figure"}
        ]
    }),

    ("william-addams", {
        "summary": (
            "William Addams (1777–1858) "
            "was an American "
            "Democratic-Republican "
            "politician from "
            "Pennsylvania who "
            "served in the "
            "U.S. House of "
            "Representatives "
            "(1825–1829) during "
            "the Adams and "
            "early Jackson eras. "
            "Pennsylvania was "
            "the largest state "
            "in the Union "
            "and a crucial "
            "political battleground "
            "— its industrial "
            "workers, frontier "
            "farmers, and "
            "immigrant communities "
            "creating a distinctive "
            "political mix. "
            "Addams served "
            "during the contested "
            "1824 election's "
            "aftermath — the "
            "'Corrupt Bargain' "
            "that gave John "
            "Quincy Adams "
            "the presidency "
            "despite Jackson's "
            "plurality — "
            "and the subsequent "
            "political realignment "
            "that split "
            "Democratic-Republicans "
            "into Adams "
            "National Republicans "
            "and Jackson Democrats. "
            "His four years "
            "witnessed the "
            "death of the "
            "first American "
            "party system.\n\n"
            "Pennsylvania's "
            "industrial tariff "
            "interests made "
            "it a key battleground "
            "in the protective "
            "tariff debates "
            "of this era.\n\n"
            "He was a Reading "
            "Pennsylvania "
            "lawyer.\n\n"
            "He served during "
            "one of the "
            "most turbulent "
            "political realignments."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Pennsylvania Democratic-Republican Congressman (1825–1829); served during the 'Corrupt Bargain' aftermath and the collapse of the first party system; witnessed the split between Adams National Republicans and Jackson Democrats; Pennsylvania industrial tariff battleground politics; Reading lawyer.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The 1824 election's contested outcome — the 'Corrupt Bargain' that gave Adams the presidency through the House vote despite Jackson's popular and electoral plurality — created the angry political realignment that dominated the Congress in which Addams served",
            "Pennsylvania's industrial development — the state's growing iron and textile industries whose prosperity depended on protective tariffs — created the economic concerns that shaped Pennsylvania's congressional delegation's policy priorities",
            "The Democratic-Republican Party's fragmentation — the collapse of the first party system's single-party dominance into competing Adams and Jackson factions — created the political chaos of the 25th Congress in which Addams served"
        ],
        "effects": [
            "His House service contributed Pennsylvania's voice to the tariff and internal improvement debates that dominated the Adams administration — the industrial state's protective tariff interests",
            "His service during the party system's transformation contributed to the historical documentation of the realignment from first to second party systems",
            "His career illustrated the typical experience of middle-rank Pennsylvania congressmen during the Era of Good Feelings' collapse — elected during one party system and serving through its transformation",
            "His four years witnessed the Adams-Jackson split that would define American politics for the next three decades"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Pennsylvania Congressman 1825–1829"},
            {"target": "john-quincy-adams", "verb": "SERVES_UNDER", "note": "Congressman during Adams's presidency"},
            {"target": "corrupt-bargain-1824", "verb": "SERVES_AFTER", "note": "Congressman elected during the election's aftermath"},
            {"target": "pennsylvania", "verb": "REPRESENTS", "note": "Reading Pennsylvania lawyer-congressman"},
            {"target": "tariff-of-abominations", "verb": "DEBATES", "note": "Pennsylvania industrial tariff advocate"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 87 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
