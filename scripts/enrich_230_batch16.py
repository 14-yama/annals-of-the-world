#!/usr/bin/env python3
"""
Batch 16 — 8 entities: Antoine-Louis Séguier, Augustin-Alexandre Darthé,
Jacob Radcliff, Jean-Baptiste Cavaignac, Nathan Sanford, Ether Shepley,
Walter Livingston, Étienne Pavillon
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
          f"e={len(det.get('effects',[]))} r={len(det.get('relationships',[]))}")


ENTITIES = [

    # 1 — Antoine-Louis Séguier (1726–1792)
    ("antoine-louis-séguier", {
        "summary": (
            "Antoine-Louis Séguier (1726–1792) was one of the most powerful legal officials of pre-Revolutionary "
            "France, serving as Avocat général (Attorney General) at the Parlement de Paris — the highest court "
            "of the ancien régime — for over three decades. A member of the illustrious Séguier legal dynasty "
            "that had provided France with chancellors, presidents, and magistrates since the 16th century, "
            "he became the most prominent judicial voice opposing the French philosophes and the encyclopedist "
            "movement, issuing formal prosecutorial briefs that made him the chief legal antagonist of the "
            "French Enlightenment.\n\n"
            "His remonstrances and réquisitoires (prosecutorial demands) against works of the philosophes were "
            "the official legal mechanism through which the Parlement sought to suppress Enlightenment publishing. "
            "Most notably, he issued the réquisitoire against Jean-Jacques Rousseau's Émile (1762), which led to "
            "the book's condemnation and burning and Rousseau's flight from France. He also filed briefs against "
            "the Encyclopédie and other philosophe publications, making him the principal legal instrument of "
            "the Catholic establishment's campaign against the Enlightenment in France. These actions brought "
            "him the fierce satirical attacks of Voltaire, Diderot, and their circle.\n\n"
            "When Chancellor Maupeou reorganized the Parlements in 1771 — abolishing the traditional magistracy "
            "and replacing it with royally appointed judges — Séguier was one of the few senior officials who "
            "cooperated with the reform, earning the condemnation of his fellow magistrates who went on strike. "
            "When the old Parlements were restored by Louis XVI in 1774, Séguier returned to his position. "
            "He died in 1792, just before the Revolution would have consumed him along with the institution "
            "he had served.\n\n"
            "Séguier illustrates the paradox of the ancien régime legal system: its most senior officials "
            "were simultaneously the agents of royal justice and the opponents of Enlightenment reform, "
            "using the law to defend the very order that was about to be overthrown."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Avocat général at the Parlement de Paris for three decades; issued the réquisitoire against Rousseau's Émile (1762) and prosecutorial briefs against the Encyclopédie — the chief legal antagonist of the French Enlightenment philosophes.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Parlement de Paris's institutional role as both the highest court and a censor of publications made its Avocat général the key figure in the campaign against Enlightenment literature",
            "The Catholic establishment's alarm at the religious and political radicalism of the Encyclopédie and philosophe movement drove the Parlement's prosecutorial response",
            "His membership in the Séguier legal dynasty — which provided France with chancellors and presidents of Parlement — gave him the social position and institutional authority for the Avocat général's role"
        ],
        "effects": [
            "His réquisitoire against Rousseau's Émile (1762) led to the book's condemnation and burning and Rousseau's arrest warrant and exile from France",
            "His briefs against the Encyclopédie and philosophe publications created the legal record of the ancien régime's official hostility to the Enlightenment",
            "His cooperation with Maupeou's 1771 reform (at the cost of his colleagues' condemnation) illustrated both his royalist loyalty and the deep divisions within the old magistracy",
            "He became the target of sustained satirical attacks by Voltaire, Diderot, and the philosophes — making him a literary as well as legal figure of the Enlightenment conflict"
        ],
        "relationships": [
            {"entity": "Parlement de Paris", "relationship": "SERVED_IN", "note": "Served as Avocat général at the Parlement de Paris for over three decades"},
            {"entity": "Jean-Jacques Rousseau", "relationship": "PROSECUTED", "note": "Issued the réquisitoire that led to the condemnation and burning of Rousseau's Émile (1762) and Rousseau's exile"},
            {"entity": "Encyclopédie", "relationship": "OPPOSED", "note": "Filed prosecutorial briefs against the Encyclopédie as part of the Parlement's campaign against philosophe publishing"},
            {"entity": "Voltaire", "relationship": "SATIRIZED_BY", "note": "Became the target of sustained satirical attacks by Voltaire and the philosophes as the chief legal opponent of the Enlightenment"},
            {"entity": "Chancellor Maupeou", "relationship": "COOPERATED_WITH", "note": "Cooperated with Maupeou's 1771 Parlement reform despite the opposition of most senior magistrates"}
        ]
    }),

    # 2 — Augustin-Alexandre Darthé (1769–1797)
    ("augustin-alexandre-darthé", {
        "summary": (
            "Augustin-Alexandre Darthé (1769–1797) was a French Revolutionary lawyer and political activist "
            "who became one of the most radical figures of the Revolutionary era as a leading conspirator in "
            "Gracchus Babeuf's Conspiracy of Equals (Conjuration des Égaux, 1796) — the first organized "
            "modern communist-style revolutionary conspiracy, which aimed to overthrow the Directory and "
            "establish a society based on the complete abolition of private property and equal distribution "
            "of all goods and labor. His execution alongside Babeuf in 1797 made him one of the founding "
            "martyrs of the socialist revolutionary tradition.\n\n"
            "Born in Guise (Aisne) and trained as a lawyer, Darthé was drawn into the Revolution's most "
            "radical currents. By 1795–1796, as the Directory government consolidated power after the "
            "Terror, Darthé had become one of the principal organizers of the Equals' secret insurrectionary "
            "committee — the Insurrectionary Committee (Comité insurrecteur) — which planned to seize "
            "control of the Paris National Guard, distribute arms to the poor quarters of the city, and "
            "launch an uprising to overthrow the Directory. The conspiracy's program, articulated in the "
            "Manifesto of the Equals (attributed largely to Sylvain Maréchal), called for the abolition "
            "of private property and the establishment of a community of goods and equal labor.\n\n"
            "The conspiracy was betrayed to the police by an informer in May 1796, and Babeuf, Darthé, "
            "and dozens of others were arrested. Tried before the High Court at Vendôme (1797), Babeuf "
            "and Darthé were both condemned to death. In a dramatic final act, they stabbed themselves "
            "with concealed daggers in the courtroom upon hearing the death sentence — but survived their "
            "self-inflicted wounds and were guillotined the following day, May 27, 1797.\n\n"
            "'He and Babeuf died as they had planned their conspiracy — together, and defiantly.' "
            "Darthé's execution with Babeuf inaugurated a tradition of revolutionary socialist martyrdom "
            "that echoed through 19th and 20th-century political culture."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "A principal organizer of Babeuf's Conspiracy of Equals (1796) — the first modern communist revolutionary conspiracy — executed with Babeuf in 1797 after their dramatic self-stabbing in the courtroom at Vendôme; a founding martyr of the socialist tradition.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Directory's conservative consolidation after Thermidor, restoring property rights and curtailing the Terror's radical social measures, radicalized Darthé and others toward Babeuf's more extreme program",
            "Mass poverty and food shortages in 1795–1796 Paris created the social crisis that Babeuf's conspiracy sought to exploit for a revolutionary insurrection",
            "The sans-culotte tradition of direct democratic action and economic equality provided the political culture from which the Conspiracy of Equals drew its recruits and ideology"
        ],
        "effects": [
            "His execution alongside Babeuf (May 27, 1797) created one of the founding martyrdom narratives of the European socialist movement",
            "The Conspiracy of Equals was documented by his fellow conspirator Filippo Buonarroti in Buonarroti's Conspiracy for Equality (1828), which became one of the most influential texts of 19th-century revolutionary socialism",
            "The program of the Conspiracy of Equals — abolition of private property, equal distribution of goods and labor — anticipated key themes of 19th-century socialism and communism",
            "The conspiracy's detection and trial demonstrated the power of informant infiltration against revolutionary organizations, influencing both subsequent police surveillance and revolutionary counter-intelligence practice"
        ],
        "relationships": [
            {"entity": "Gracchus Babeuf", "relationship": "CO-CONSPIRATOR_WITH", "note": "Principal co-conspirator with Babeuf in the Conspiracy of Equals; executed alongside him on May 27, 1797"},
            {"entity": "Conspiracy of Equals (Conjuration des Égaux)", "relationship": "ORGANIZED", "note": "One of the principal organizers of the Insurrectionary Committee of the Conspiracy of Equals"},
            {"entity": "Filippo Buonarroti", "relationship": "CONTEMPORARY_OF", "note": "Buonarroti, fellow conspirator, documented the Conspiracy of Equals in his 1828 book that spread Babeuf's and Darthé's legacy"},
            {"entity": "French Directory", "relationship": "OPPOSED", "note": "The Directory's conservative rule was the primary target of the Conspiracy's planned insurrection"},
            {"entity": "High Court of Vendôme", "relationship": "TRIED_BY", "note": "Tried before the Haute Cour de Vendôme in 1797 and condemned to death for his role in the conspiracy"}
        ]
    }),

    # 3 — Jacob Radcliff (1764–1844)
    ("jacob-radcliff", {
        "summary": (
            "Jacob Radcliff (1764–1844) was an American jurist, politician, and civic leader from New York "
            "who served in multiple capacities at the intersection of law and governance during the formative "
            "decades of the American republic, including as Mayor of New York City (1810–1811 and 1815), "
            "Associate Justice of the New York State Supreme Court, and trustee of Columbia College. Born "
            "in Rhinebeck, New York, to a family with Revolutionary connections, he graduated from Princeton "
            "College (College of New Jersey) and studied law in New York.\n\n"
            "Radcliff practiced law in New York City before entering the judiciary, serving on the New York "
            "State Supreme Court as an Associate Justice (the New York Supreme Court was then the state's "
            "principal trial court for important cases). He left the bench to serve twice as Mayor of New "
            "York City, administering the rapidly growing metropolis during the years when New York was "
            "establishing the institutions and infrastructure of a major commercial city. During his "
            "mayoralty, New York was completing its transition from colonial port to American commercial "
            "capital, with rapidly expanding population and commerce.\n\n"
            "He was a trustee of Columbia College for decades, contributing to the development of the "
            "institution that would become Columbia University. Columbia's law faculty was developing "
            "during this period as one of the first professional law schools in the United States, and "
            "trustee oversight was critical to its institutional development. His career illustrated "
            "the characteristic early American pattern of the lawyer-statesman who moved fluidly between "
            "the bench, political office, and civic institutional leadership.\n\n"
            "His long life (1764–1844) spanned from the Revolutionary generation through the Jacksonian "
            "era, making him a living connection between the founding generation's legal culture and "
            "the more professionalized legal world of the 19th century."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "American jurist and twice Mayor of New York City (1810–1811, 1815), serving during New York's transformation into the nation's leading commercial city; trustee of Columbia College during its institutional development.",
            "significanceCategory": "local"
        },
        "causes": [
            "Princeton College education and legal training in New York City equipped Radcliff with the credentials for both judicial and civic leadership in early American legal culture",
            "New York City's rapid growth into the most commercially dynamic city in the United States created demand for experienced legal-administrative leadership that Radcliff provided as mayor",
            "The characteristic American pattern of the lawyer-statesman — who served on the bench, in elected office, and in civic institutions — shaped Radcliff's multi-role career"
        ],
        "effects": [
            "Served as Mayor of New York City (1810–1811 and 1815) during the critical period of New York's transformation from colonial port to American commercial capital",
            "As Associate Justice of the New York State Supreme Court, contributed to the development of early American commercial and property law jurisprudence",
            "Decades of trusteeship at Columbia College supported the institutional development of what would become Columbia University and its law faculty",
            "His career model of the lawyer-mayor-trustee exemplified the civic role of legal professionals in shaping early American urban institutions"
        ],
        "relationships": [
            {"entity": "New York City", "relationship": "GOVERNED", "note": "Served as Mayor of New York City in 1810–1811 and again in 1815"},
            {"entity": "New York State Supreme Court", "relationship": "SERVED_ON", "note": "Served as Associate Justice of the New York State Supreme Court"},
            {"entity": "Columbia College (Columbia University)", "relationship": "TRUSTEE_OF", "note": "Served as trustee of Columbia College for decades, supporting its institutional development"},
            {"entity": "Princeton College", "relationship": "EDUCATED_AT", "note": "Graduated from the College of New Jersey (Princeton) and subsequently trained in law in New York"},
            {"entity": "Early American legal profession", "relationship": "EXEMPLIFIED", "note": "His career as lawyer, judge, mayor, and college trustee exemplified the lawyer-statesman ideal of the early republic"}
        ]
    }),

    # 4 — Jean-Baptiste Cavaignac (1762–1829)
    ("jean-baptiste-cavaignac", {
        "summary": (
            "Jean-Baptiste Cavaignac (1762–1829) was a French lawyer, Conventionnel, and military administrator "
            "whose Revolutionary commitments made him a regicide — one of the deputies who voted for the "
            "execution of Louis XVI in January 1793 — and whose family would produce some of the most "
            "significant political and military figures of 19th-century France. Born in Gourdon (Lot), "
            "he trained as a lawyer and entered politics with the Revolution, being elected to the National "
            "Convention (1792–1795) representing the Lot department.\n\n"
            "As a Conventionnel, Cavaignac voted for the death of Louis XVI — a vote that committed him "
            "irrevocably to the Revolutionary cause and later to permanent exile under the Bourbon "
            "Restoration. He served in military administrative roles during the Convention, particularly "
            "in the suppression of the Federalist revolts and in missions to the Pyrenean departments. "
            "He continued to serve in administrative capacities under the Directory and remained politically "
            "active as a republican through the Consulate and Empire periods, though he was excluded from "
            "the highest positions by his regicide status.\n\n"
            "When the Bourbon Restoration came in 1815, Cavaignac, as a regicide, was forced into exile. "
            "He died in Brussels in 1829, never returning to France under the Restoration monarchy. "
            "The political legacy of his family proved far more consequential than his own career: "
            "his son Louis-Eugène Cavaignac (1802–1857) became the general who brutally suppressed "
            "the Paris workers' uprising in June 1848 and was the first presidential candidate of "
            "the Second Republic (losing to Louis-Napoleon Bonaparte); and his other son Godefroy "
            "Cavaignac (1801–1845) was a leading liberal republican politician of the July Monarchy.\n\n"
            "The Cavaignac family's trajectory — from Revolutionary regicide to Republican general — "
            "traced the complex inheritance of the Revolution across generations of French political life."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "A French Revolutionary Conventionnel who voted for Louis XVI's execution; his family's legacy — General Louis-Eugène Cavaignac (suppressor of June 1848) and Godefroy Cavaignac (liberal politician) — shaped 19th-century French republican politics.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Election to the National Convention in 1792 placed Cavaignac at the center of Revolutionary politics during its most radical phase",
            "His vote for Louis XVI's death in January 1793 irrevocably committed him to the Republican cause and defined his political identity — and his family's — for generations",
            "The fragmentation of French political life after 1815 between regicides-in-exile and Bourbon loyalists shaped the family environment in which his sons became leading republicans"
        ],
        "effects": [
            "Voted for the execution of Louis XVI (January 1793), becoming a regicide whose death sentence under the Bourbon Restoration forced him into permanent exile",
            "His exile transmitted a strong republican and anti-monarchical political identity to his sons Louis-Eugène and Godefroy",
            "His son Louis-Eugène Cavaignac became the general who suppressed the June Days (1848) and the first major presidential candidate of the Second Republic",
            "His son Godefroy Cavaignac became a leading liberal republican politician of the July Monarchy, continuing the family's republican political tradition"
        ],
        "relationships": [
            {"entity": "National Convention", "relationship": "MEMBER_OF", "note": "Elected to the National Convention in 1792, representing the Lot department"},
            {"entity": "Louis XVI of France", "relationship": "VOTED_FOR_EXECUTION_OF", "note": "Voted for the death of Louis XVI in January 1793, making him a regicide"},
            {"entity": "Louis-Eugène Cavaignac", "relationship": "FATHER_OF", "note": "Father of General Louis-Eugène Cavaignac, who suppressed the June Days (1848) and was first presidential candidate of the Second Republic"},
            {"entity": "Godefroy Cavaignac", "relationship": "FATHER_OF", "note": "Father of Godefroy Cavaignac, a leading liberal republican politician of the July Monarchy"},
            {"entity": "Bourbon Restoration", "relationship": "EXILED_BY", "note": "Forced into exile after 1815 as a regicide; died in Brussels in 1829 without returning to France"}
        ]
    }),

    # 5 — Nathan Sanford (1777–1838)
    ("nathan-sanford", {
        "summary": (
            "Nathan Sanford (1777–1838) was an American lawyer, statesman, and jurist from New York who "
            "occupied several of the most important legal and political positions in the early American "
            "republic, including United States Senator, United States District Attorney for New York, "
            "and Chancellor of New York — the highest judicial office in the state. Educated at Yale "
            "College (class of 1797) and trained in law under Aaron Burr — one of the most prominent "
            "lawyers and politicians of the era — Sanford combined legal expertise with a long career "
            "in Democratic-Republican and later Jacksonian Democratic politics.\n\n"
            "He served as United States District Attorney for the District of New York from 1803 to 1815, "
            "a period that encompassed the Jefferson and Madison administrations, the Embargo Act, and "
            "the War of 1812. As the chief federal prosecutor for New York, he oversaw the enforcement "
            "of federal trade restrictions and prosecution of violations during the turbulent years of "
            "Anglo-American conflict. He was elected United States Senator from New York (1815–1821), "
            "serving in the Senate during the Era of Good Feelings and the congressional debates over "
            "the Missouri Compromise.\n\n"
            "His most legally significant position was Chancellor of New York (1823–1826), the presiding "
            "judge of the New York Court of Chancery — the highest equity court in the state. This "
            "was a position of enormous legal authority: New York's Court of Chancery produced "
            "landmark equity decisions and James Kent (his predecessor) had just completed his "
            "celebrated Commentaries on American Law while serving in this role. Sanford returned "
            "to the Senate (1826–1831) and was briefly considered for the Vice-Presidency.\n\n"
            "He was a delegate to the New York State Constitutional Convention of 1821, which "
            "expanded suffrage and reformed the state's judiciary."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "US Senator, US District Attorney for New York, and Chancellor of New York — the state's highest equity judge — trained by Aaron Burr; a significant figure in early American legal and political history during the formative Jeffersonian and Jacksonian eras.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Yale College education and legal training under Aaron Burr — the most politically prominent New York lawyer of the era — provided the professional credentials for Sanford's rapid advancement",
            "New York's position as the most commercially important state in the early republic created demand for experienced federal prosecutors and legislators who could manage the complex legal questions of trade and finance",
            "Democratic-Republican political connections during the Jefferson and Madison administrations supported his appointment as US District Attorney and his subsequent Senate elections"
        ],
        "effects": [
            "As US District Attorney (1803–1815), enforced the Embargo Act and War of 1812 trade restrictions that were central to Jefferson's and Madison's foreign policy",
            "As Chancellor of New York (1823–1826), administered the highest equity court in the state, succeeding James Kent who had just transformed American equity jurisprudence",
            "His two Senate terms made him a participant in the major legislative debates of the early republic, including the Missouri Compromise discussions",
            "As a delegate to the 1821 New York State Constitutional Convention, contributed to the reform of New York's suffrage requirements and judicial structure"
        ],
        "relationships": [
            {"entity": "Aaron Burr", "relationship": "STUDIED_LAW_UNDER", "note": "Trained as a lawyer under Aaron Burr, one of the most prominent New York lawyers and politicians of the early republic"},
            {"entity": "Yale University", "relationship": "EDUCATED_AT", "note": "Graduated from Yale College in 1797"},
            {"entity": "US Senate", "relationship": "MEMBER_OF", "note": "Served as US Senator from New York in two terms: 1815–1821 and 1826–1831"},
            {"entity": "New York Court of Chancery", "relationship": "PRESIDED_OVER", "note": "Served as Chancellor of New York (1823–1826), presiding over the highest equity court in the state"},
            {"entity": "James Kent", "relationship": "SUCCEEDED", "note": "Succeeded James Kent as Chancellor of New York; Kent had just completed his landmark Commentaries on American Law in the role"}
        ]
    }),

    # 6 — Ether Shepley (1786–1877)
    ("ether-shepley", {
        "summary": (
            "Ether Shepley (1786–1877) was a Maine lawyer, politician, and jurist whose remarkably long "
            "career — spanning from the War of 1812 era through the Reconstruction period — encompassed "
            "United States Senate service, and senior positions on the Maine Supreme Judicial Court, "
            "including Chief Justice. Born in Groton, Massachusetts, he received his education locally "
            "and studied law before being admitted to the bar and relocating to Maine (then still a "
            "district of Massachusetts, becoming a state in 1820).\n\n"
            "Shepley built a successful legal practice in Saco, Maine, and became a prominent "
            "Democratic-Republican and later Jacksonian Democrat in Maine politics. He served as "
            "a United States Senator from Maine (1833–1836), resigning his Senate seat to accept "
            "appointment to the Maine Supreme Judicial Court as an Associate Justice — a choice "
            "that reflected the prestige and permanence of judicial office compared to the political "
            "volatility of the Senate. On the Maine bench, he rose to become Chief Justice "
            "(1848–1855), presiding over the court during the antebellum period when Maine law "
            "was developing its distinctive character.\n\n"
            "His tenure as Chief Justice of the Maine Supreme Judicial Court coincided with some "
            "of the most important years of antebellum Maine legal development, including "
            "questions of maritime law (critical for Maine's extensive seafaring and fishing "
            "economy), land title disputes, and commercial law. He was highly regarded as a "
            "careful, methodical judge who produced clearly reasoned decisions. He lived to "
            "the extraordinary age of 91, outliving most of his political and judicial contemporaries.\n\n"
            "His career illustrated both the characteristic American pattern of movement between "
            "legislative and judicial office and the profound legal development of the New England "
            "states in the generation following statehood."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "US Senator from Maine and Chief Justice of the Maine Supreme Judicial Court (1848–1855); his long legal career contributed to the development of Maine law during the critical antebellum period.",
            "significanceCategory": "local"
        },
        "causes": [
            "Maine's separation from Massachusetts as a new state (1820) created the need to build a robust state judiciary from the ground up, providing opportunities for able lawyers like Shepley",
            "Jacksonian Democratic political networks in Maine supported Shepley's Senate election and his subsequent transition to the judiciary",
            "Maine's extensive maritime economy — fishing, shipbuilding, and coastal trade — created a distinctive body of maritime and commercial legal questions for the Supreme Judicial Court"
        ],
        "effects": [
            "Served as US Senator from Maine (1833–1836) before choosing the bench over continued political career",
            "As Chief Justice of the Maine Supreme Judicial Court (1848–1855), presided over the development of Maine law during the critical antebellum period",
            "His decisions in maritime, land title, and commercial law contributed to the distinctive body of Maine jurisprudence that shaped New England legal culture",
            "His very long life (91 years) made him a living institutional memory of Maine legal development from statehood through the Civil War era"
        ],
        "relationships": [
            {"entity": "US Senate", "relationship": "MEMBER_OF", "note": "Served as US Senator from Maine (1833–1836) before resigning to accept judicial appointment"},
            {"entity": "Maine Supreme Judicial Court", "relationship": "SERVED_ON", "note": "Served as Associate Justice and then Chief Justice (1848–1855) of the Maine Supreme Judicial Court"},
            {"entity": "Maine", "relationship": "SHAPED_LAW_OF", "note": "Contributed to the development of Maine's distinctive legal culture through his Senate service and decades on the bench"},
            {"entity": "Jacksonian Democratic Party", "relationship": "AFFILIATED_WITH", "note": "Democratic political connections supported his Senate career before his transition to the judiciary"},
            {"entity": "New England legal culture", "relationship": "CONTRIBUTED_TO", "note": "His judicial decisions in maritime, commercial, and property law contributed to the broader New England legal tradition"}
        ]
    }),

    # 7 — Walter Livingston (1740–1797)
    ("walter-livingston", {
        "summary": (
            "Walter Livingston (1740–1797) was an American merchant, lawyer, and politician from New York's "
            "most powerful dynastic family — the Livingston manor family — who served in the Continental "
            "Congress during the Confederation era and played a significant role in New York state politics "
            "during the founding decades of the American republic. Born at Livingston Manor, the vast "
            "Hudson River estate that dominated the political economy of Columbia County, he was part "
            "of the generation of Livingstons who bridged the transition from colonial gentry to "
            "American republic.\n\n"
            "The Livingston family was one of the great dynasties of early American history: Walter's "
            "cousins and relatives included Robert R. Livingston (Chancellor of New York, who "
            "administered the oath of office to George Washington and later negotiated the Louisiana "
            "Purchase), Philip Livingston (signer of the Declaration of Independence), and William "
            "Livingston (Governor of New Jersey). Walter himself served as a delegate to the "
            "Continental Congress (1784–1785), participating in the national government during "
            "the critical Confederation period between independence and the Constitution.\n\n"
            "He also served as a member of the New York State Assembly and was involved in the "
            "commercial and legal life of New York during the transition to statehood and the "
            "early republic. As a merchant-lawyer, he participated in both the commercial networks "
            "that made New York the financial center of the new nation and the legal-political "
            "structures of the Livingston manor's extensive landholdings and tenant relationships. "
            "The anti-rent tradition — in which manor tenants disputed the feudal terms of their "
            "leases — was beginning to emerge as a political issue during his lifetime.\n\n"
            "His career illustrated the central role of the New York landowning gentry in both "
            "the commerce and the governance of the early American republic, and the Livingston "
            "family's particular dominance of New York's revolutionary and founding political leadership."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Continental Congress delegate and New York politician from the Livingston manor dynasty — one of the most influential families in early American history — whose relatives included Chancellor Robert R. Livingston and Philip Livingston (signatory of the Declaration of Independence).",
            "significanceCategory": "local"
        },
        "causes": [
            "Membership in the Livingston manor dynasty — one of the most politically and commercially powerful families in colonial and early republican New York — provided the social capital for Continental Congress service",
            "The Confederation period's need for experienced property owners and merchants in the Continental Congress created the political opportunity for Livingston's service",
            "The Hudson River Valley's gentry culture of commercial farming, merchant trading, and manor politics shaped Livingston's career as both a merchant and a public official"
        ],
        "effects": [
            "Continental Congress service (1784–1785) contributed to the national government during the critical Confederation period when the Articles of Confederation were being tested",
            "New York State Assembly service contributed to the legal and political infrastructure of New York during its transition from colony to state",
            "The Livingston family's collective political dominance of New York — through Walter, Robert R., Philip, and others — shaped the legal and political institutions of the early republic",
            "His participation in the manor economy contributed to the landholding arrangements that would generate the anti-rent controversies of the 1840s"
        ],
        "relationships": [
            {"entity": "Continental Congress", "relationship": "DELEGATE_TO", "note": "Served as a delegate to the Continental Congress (1784–1785) during the Confederation period"},
            {"entity": "Robert R. Livingston", "relationship": "RELATIVE_OF", "note": "Related to Robert R. Livingston, Chancellor of New York, who administered Washington's oath and negotiated the Louisiana Purchase"},
            {"entity": "Philip Livingston", "relationship": "RELATIVE_OF", "note": "Related to Philip Livingston, signer of the Declaration of Independence"},
            {"entity": "New York State Assembly", "relationship": "MEMBER_OF", "note": "Served in the New York State Assembly during the early republic"},
            {"entity": "Livingston Manor", "relationship": "HEIR_TO", "note": "Born and raised at Livingston Manor, the vast Hudson River estate that dominated Columbia County's political economy"}
        ]
    }),

    # 8 — Étienne Pavillon (1632–1705)
    ("étienne-pavillon", {
        "summary": (
            "Étienne Pavillon (1632–1705) was a French lawyer, poet, and wit of the grand siècle who "
            "combined a legal career in Paris with a distinguished place in the literary culture of "
            "Louis XIV's France, culminating in election to the Académie française (1691) — the "
            "most prestigious literary institution in France. Born in Paris to a bourgeois family "
            "with legal connections, he trained as a lawyer and practiced at the Paris bar before "
            "his literary talents brought him into the circle of the Parisian salons and literary "
            "society of the late 17th century.\n\n"
            "Pavillon was celebrated in his time primarily for his satirical verses, bons mots, "
            "and epistolary wit — the graceful, occasionally pointed social verse that circulated "
            "in manuscript and in salon conversation before being collected and published. He was "
            "associated with the Epicurean circle around the poet Charles de Saint-Évremond and "
            "the libertine literary tradition of mid-17th-century France, writing in a register "
            "of polished, ironic wit that valued urbanity over sentiment. His verse often "
            "reflected the milieu of Parisian legal and salon culture — the world of lawyers "
            "who were also men of letters.\n\n"
            "His election to the Académie française in 1691 recognized both his poetic standing "
            "and his social position within the literary establishment of Louis XIV's France. "
            "The Académie in this period was the central arbiter of French linguistic and literary "
            "standards, engaged in the long process of completing its Dictionnaire — and Pavillon "
            "participated in the institutional work of the academy alongside his literary activities. "
            "He died in 1705, a respected though minor figure whose career illustrated the close "
            "integration of legal practice and literary culture in 17th-century France.\n\n"
            "Pavillon embodied the lawyer-poet type — the homme de lettres who never fully left the "
            "bar — that was characteristic of educated French professional culture in the classical era."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "A French lawyer-poet of the grand siècle, elected to the Académie française (1691); his career illustrated the close integration of legal practice and literary culture in Louis XIV's France.",
            "significanceCategory": "local"
        },
        "causes": [
            "The integration of legal practice and literary culture in 17th-century France created a milieu in which lawyers were also expected to participate in salon literary culture and verse composition",
            "The Parisian salon culture of the mid-to-late 17th century provided the institutional setting — the Hôtels and literary circles — in which Pavillon's wit and verse gained recognition",
            "The Académie française's role as arbiter of French literary standards and its active search for distinguished members from across professional life created the path for Pavillon's election"
        ],
        "effects": [
            "Election to the Académie française (1691) recognized his place in the literary establishment of Louis XIV's France and gave him institutional participation in the academy's linguistic work",
            "His satirical verses and bons mots circulated in manuscript and salon culture, contributing to the tradition of polished French social verse of the grand siècle",
            "His career as lawyer-poet illustrated the permeable boundary between legal and literary professional culture in classical France, a pattern that influenced subsequent generations",
            "His association with the libertine Epicurean circle around Saint-Évremond connected him to the broader tradition of French classical literary skepticism"
        ],
        "relationships": [
            {"entity": "Académie française", "relationship": "MEMBER_OF", "note": "Elected to the Académie française in 1691, the most prestigious literary institution in France"},
            {"entity": "Charles de Saint-Évremond", "relationship": "ASSOCIATED_WITH", "note": "Part of the Epicurean literary circle around Saint-Évremond, which valued urbanity, wit, and skepticism"},
            {"entity": "Louis XIV", "relationship": "CONTEMPORARY_OF", "note": "His literary career flourished during the reign of Louis XIV, the great patron of French classical culture"},
            {"entity": "Paris bar", "relationship": "PRACTICED_AT", "note": "Practiced as a lawyer at the Paris bar before his literary reputation grew to prominence"},
            {"entity": "French classical literary culture", "relationship": "CONTRIBUTED_TO", "note": "Contributed satirical verse and bons mots to the salon literary culture of 17th-century France"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 16)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
