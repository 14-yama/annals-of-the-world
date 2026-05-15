#!/usr/bin/env python3
"""
Batch 84 — 8 entities: Charles Gérard Eyschen, Elisha Reynolds Potter,
Étienne de Joly, René-François Dumas, Thomas McKean Thompson McKennan,
André Antoine Bernard, Chauncey Goodrich, John Milton Niles
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

    ("charles-gérard-eyschen", {
        "summary": (
            "Charles Gérard Eyschen "
            "(1821–1886) was a "
            "Luxembourgish politician "
            "and lawyer who served "
            "in Luxembourg's "
            "Chamber of Deputies "
            "and helped develop "
            "the constitutional "
            "and legal framework "
            "of independent Luxembourg "
            "after the 1839 Treaty "
            "of London established "
            "Luxembourg's definitive "
            "boundaries and "
            "guaranteed its neutrality. "
            "Luxembourgish politics "
            "in this era were "
            "shaped by the grand duchy's "
            "complex position — "
            "nominally in personal "
            "union with the Netherlands "
            "under the House of Orange-Nassau "
            "yet constitutionally "
            "autonomous and neutral, "
            "part of the German "
            "Confederation yet "
            "culturally French. "
            "The 1848 revolutions "
            "brought a more liberal "
            "constitution to "
            "Luxembourg, creating "
            "the parliamentary "
            "framework within "
            "which Eyschen worked.\n\n"
            "His son Paul Eyschen "
            "would serve as "
            "Luxembourg's Prime "
            "Minister for "
            "a remarkable 27 years "
            "(1888–1915) — "
            "one of Europe's "
            "longest-serving prime ministers.\n\n"
            "His career contributed "
            "to Luxembourg's "
            "early constitutional "
            "governance.\n\n"
            "He was a significant "
            "Luxembourgish "
            "legal and political figure."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Luxembourgish politician and lawyer (1821–1886); contributed to Luxembourg's constitutional development after the 1839 Treaty of London; served in the Chamber of Deputies; father of Prime Minister Paul Eyschen (1888–1915); active during the 1848 liberal constitutional transformation; helped build Luxembourg's legal and parliamentary framework.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The 1839 Treaty of London — Luxembourg's partition and definitive settlement that established the Grand Duchy's boundaries, guaranteed its perpetual neutrality, and created the independent constitutional state — created the political framework for Eyschen's parliamentary career",
            "The 1848 liberal revolution's effect on Luxembourg — the wave of liberal constitutionalism that produced Luxembourg's 1848 constitution and established parliamentary governance — created the constitutional system within which Eyschen served",
            "Luxembourg's complex multinational position — its personal union with the Netherlands, its membership in the German Confederation, and its French cultural affinity — created the diplomatic and constitutional challenges that Luxembourgish politicians navigated"
        ],
        "effects": [
            "His parliamentary service contributed to Luxembourg's early constitutional governance — building the practical institutions of parliamentary democracy in the small grand duchy",
            "His family's political legacy — particularly through his son Paul Eyschen's 27-year prime ministership — extended his political influence far beyond his own career",
            "His legal work contributed to Luxembourg's developing jurisprudence — building the legal framework of a constitutionally independent state in the post-1839 period",
            "His career illustrated Luxembourg's political maturation — the development of a stable parliamentary culture in a state whose independence was only definitively settled in 1839"
        ],
        "relationships": [
            {"target": "luxembourg", "verb": "SERVES", "note": "Luxembourgish parliamentary politician"},
            {"target": "chamber-of-deputies-luxembourg", "verb": "SERVES_IN", "note": "Luxembourg Chamber of Deputies member"},
            {"target": "paul-eyschen", "verb": "FATHER_OF", "note": "Father of Luxembourg's 27-year prime minister"},
            {"target": "treaty-of-london-1839", "verb": "SERVES_AFTER", "note": "Post-partition Luxembourg constitutionalist"},
            {"target": "luxembourgish-constitutional-law", "verb": "DEVELOPS", "note": "Lawyer contributing to Luxembourg's legal framework"}
        ]
    }),

    ("elisha-reynolds-potter", {
        "summary": (
            "Elisha Reynolds Potter (1764–1835) "
            "was an American Federalist "
            "and later Democratic-Republican "
            "politician from Rhode "
            "Island who served "
            "in the U.S. House "
            "(1796–1797 and 1809–1815). "
            "A Rhode Island "
            "congressman serving "
            "across two distinct "
            "eras — the Washington "
            "Federalist period "
            "and the Madison "
            "War of 1812 era "
            "— Potter's combined "
            "service illustrated "
            "the partisan transformation "
            "of New England "
            "from Federalist "
            "to Jeffersonian "
            "Democratic-Republican "
            "allegiance. Rhode "
            "Island's resistance "
            "to the War of 1812 "
            "— the war was "
            "widely unpopular "
            "in New England's "
            "commercially-minded, "
            "anti-French maritime "
            "communities — "
            "was a defining "
            "feature of Potter's "
            "second House period.\n\n"
            "New England's "
            "Hartford Convention "
            "(1814–1815) — "
            "the gathering of "
            "Federalist New England "
            "states protesting "
            "the war — was "
            "the climax of "
            "the regional political "
            "crisis during "
            "Potter's service.\n\n"
            "His son Elisha Reynolds "
            "Potter Jr. would "
            "serve in Congress "
            "in the next generation.\n\n"
            "He was a South Kingstown "
            "Rhode Island planter-lawyer."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Rhode Island Federalist/Democratic-Republican Congressman (1796–1797 and 1809–1815); served during the Washington era and the War of 1812; Rhode Island's anti-war New England context; father of Congressman Elisha Reynolds Potter Jr.; South Kingstown planter-lawyer across two eras of American politics.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Federalist-Republican partisan transformation — the political realignment from Washington-era Federalism to Jeffersonian Republicanism that Potter navigated across his two periods of service — created the changing political identity of his career",
            "The War of 1812 — the conflict that was deeply unpopular in New England's maritime communities and that dominated Potter's second congressional term — created the defining political controversy of his later career",
            "Rhode Island's commercial maritime economy — the state's dependence on Atlantic trade and its consequent hostility to the embargo and war policies that disrupted maritime commerce — created the economic concerns that shaped Rhode Island's congressional delegation's political positions"
        ],
        "effects": [
            "His First Congress service contributed Rhode Island's voice to the Washington era's foundational legislation — serving during the establishment of the federal government's first institutions",
            "His War of 1812 service contributed to New England's anti-war congressional opposition — the House votes that reflected New England's commercial maritime communities' hostility to the conflict",
            "His family's political continuity — his son's subsequent congressional service — contributed to Rhode Island's tradition of planter-lawyer political dynasties",
            "His career illustrated the political transformation from Washington-era Federalism to Jeffersonian Republicanism that reshaped New England politics"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Rhode Island Congressman 1796–1797 and 1809–1815"},
            {"target": "war-of-1812", "verb": "SERVES_DURING", "note": "New England anti-war congressman"},
            {"target": "hartford-convention", "verb": "SERVES_DURING", "note": "Rhode Island congressman during New England's protest"},
            {"target": "elisha-reynolds-potter-jr", "verb": "FATHER_OF", "note": "Father of the next-generation Rhode Island congressman"},
            {"target": "rhode-island", "verb": "REPRESENTS", "note": "Rhode Island planter-lawyer congressman"}
        ]
    }),

    ("étienne-de-joly", {
        "summary": (
            "Étienne-Louis-Hector "
            "de Joly (1764–1831) "
            "was a French royalist "
            "lawyer and politician "
            "who served as Minister "
            "of Justice of France "
            "under Louis XVI — "
            "appointed in the "
            "desperate last weeks "
            "of the constitutional "
            "monarchy (July–August 1792). "
            "His ministerial "
            "appointment came "
            "during the final "
            "crisis of the Bourbon "
            "monarchy — between "
            "the Tuileries storming "
            "on August 10, 1792 "
            "and the official "
            "suspension of Louis XVI. "
            "De Joly survived "
            "the Terror, "
            "later practiced "
            "law under the "
            "Directory and Consulate, "
            "and participated "
            "in the Restoration's "
            "legal establishment.\n\n"
            "His brief Justice "
            "Ministry in the "
            "monarchy's last "
            "weeks placed him "
            "at one of the "
            "most dramatic "
            "turning points "
            "in French history "
            "— the final collapse "
            "of the ancien régime.\n\n"
            "His survival through "
            "the Terror — "
            "when many royalist "
            "ministers were "
            "guillotined — "
            "was itself remarkable.\n\n"
            "He was a distinguished "
            "French royalist "
            "and legal figure."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "French Minister of Justice under Louis XVI (July–August 1792); appointed during the final weeks of the Bourbon constitutional monarchy; survived the Terror; practiced law under the Directory, Consulate, and Restoration; served at the exact moment of the monarchy's collapse on August 10, 1792; royalist lawyer and ministerial figure.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The constitutional monarchy's crisis — the revolution's radicalization, the Brunswick Manifesto, and the mounting popular pressure against Louis XVI — created the desperate political context in which de Joly accepted the Justice Ministry in July 1792",
            "The August 10, 1792 Tuileries storming — the popular insurrection that suspended the king and ended the constitutional monarchy — terminated de Joly's brief ministry and began the republic",
            "De Joly's legal expertise and royalist loyalty — his standing as a Paris lawyer committed to the constitutional monarchy — made him a credible ministerial appointment in the final weeks of Louis XVI's government"
        ],
        "effects": [
            "His brief Justice Ministry served the constitutional monarchy at its moment of extinction — the final royalist cabinet that functioned until the August 10 insurrection",
            "His survival of the Terror contributed to the continuity of French legal culture — a royalist lawyer who survived the radical phase and returned to legal practice under subsequent regimes",
            "His participation in the Restoration's legal establishment contributed to the legal continuity between the ancien régime and the Bourbon return — royalist lawyers who bridged the revolutionary rupture",
            "His career illustrated the precariousness of ministerial service to Louis XVI — the extreme danger of serving the king in his final months and the diverse fates of those who did"
        ],
        "relationships": [
            {"target": "louis-xvi-of-france", "verb": "SERVES_UNDER", "note": "Minister of Justice in Louis XVI's final cabinet"},
            {"target": "french-constitutional-monarchy", "verb": "SERVES_IN", "note": "Justice Minister in the last weeks of constitutional monarchy"},
            {"target": "storming-of-the-tuileries", "verb": "SERVES_UNTIL", "note": "Ministry terminated by August 10, 1792 insurrection"},
            {"target": "french-revolution", "verb": "SERVES_DURING", "note": "Royalist minister at the monarchy's collapse"},
            {"target": "bourbon-restoration", "verb": "PARTICIPATES_IN", "note": "Royalist lawyer active in the Restoration"}
        ]
    }),

    ("rené-françois-dumas", {
        "summary": (
            "René-François Dumas "
            "(1757–1794) was a "
            "French revolutionary "
            "judge who served as "
            "Vice-President of "
            "the Revolutionary "
            "Tribunal of Paris "
            "— the court established "
            "by the Committee "
            "of Public Safety "
            "to prosecute enemies "
            "of the Revolution "
            "during the Terror. "
            "Dumas was one of "
            "the most zealous "
            "judicial instruments "
            "of Robespierre's Terror "
            "— presiding over "
            "the tribunal that "
            "sentenced thousands "
            "to the guillotine "
            "including Marie "
            "Antoinette (October 1793) "
            "and the Girondins. "
            "When Thermidor "
            "came in July 1794 "
            "and Robespierre "
            "fell, Dumas was "
            "executed along with "
            "his master — "
            "the Terrorist judicial "
            "apparatus consuming "
            "its own operators.\n\n"
            "His career illustrated "
            "the Terror's self-devouring "
            "logic — the judicial "
            "killers themselves "
            "killed when the "
            "political winds shifted.\n\n"
            "The Revolutionary "
            "Tribunal under "
            "Dumas and Fouquier-Tinville "
            "was one of the "
            "most lethal judicial "
            "bodies in history.\n\n"
            "He was guillotined "
            "on 10 Thermidor."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Vice-President of the Revolutionary Tribunal of Paris during the Terror; presided over trials of Marie Antoinette, the Girondins, and thousands of others; executed on 10 Thermidor along with Robespierre; one of the chief judicial instruments of the Terror; his career illustrated the Terror's self-destructive dynamic.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Robespierre's Committee of Public Safety — the Jacobin governing committee that established the Revolutionary Tribunal as the judicial arm of the Terror — created the institutional context for Dumas's role as its vice-president",
            "The Revolution's radicalization — the escalating crisis of 1793–1794 that pushed the Jacobins toward mass political violence to eliminate enemies real and imagined — created the political pressure that made the Tribunal's mass sentencing acceptable",
            "Dumas's own Jacobin conviction — his genuine ideological commitment to Robespierre's purified republic — drove his zealous participation rather than merely making him an unwilling instrument"
        ],
        "effects": [
            "His tribunal's sentencing contributed directly to the Terror's death toll — the thousands of executions that the Revolutionary Tribunal authorized during the most intense phase of 1793–1794",
            "His execution on Thermidor contributed to the end of the Terror — the killing of the terrorist apparatus itself that Thermidor accomplished in destroying Robespierre and his judicial instruments",
            "His career contributed to the historical understanding of the Terror's dynamic — the judicial machinery that enabled mass political violence and then was consumed by the same political logic",
            "The Revolutionary Tribunal he helped operate became one of history's most infamous judicial bodies — the legal machinery that gave the Terror its formal procedure while destroying its legitimacy"
        ],
        "relationships": [
            {"target": "revolutionary-tribunal-paris", "verb": "PRESIDES_OVER", "note": "Vice-President of the Terror's judicial body"},
            {"target": "maximilien-robespierre", "verb": "SERVES_UNDER", "note": "Judicial instrument of Robespierre's Committee"},
            {"target": "reign-of-terror", "verb": "IMPLEMENTS", "note": "Chief judicial executor of the Terror"},
            {"target": "marie-antoinette", "verb": "TRIES", "note": "Tribunal that sentenced the queen to death"},
            {"target": "thermidorian-reaction", "verb": "EXECUTED_BY", "note": "Guillotined on 10 Thermidor along with Robespierre"}
        ]
    }),

    ("thomas-mckean-thompson-mckennan", {
        "summary": (
            "Thomas McKean Thompson "
            "McKennan (1794–1852) "
            "was an American Whig "
            "politician from Pennsylvania "
            "who served in the "
            "U.S. House (1831–1839 "
            "and 1842–1843) and "
            "very briefly as "
            "Secretary of the "
            "Interior (1850) — "
            "resigning after "
            "only weeks due to "
            "ill health. As one "
            "of the first Secretaries "
            "of the Interior "
            "— the department "
            "was established "
            "in 1849 — McKennan's "
            "brief tenure was "
            "notable despite "
            "its length. His "
            "eight House years "
            "spanned the Jackson "
            "and Van Buren eras "
            "— serving as a "
            "Pennsylvania Whig "
            "during the Bank "
            "War, the nullification "
            "crisis, and the "
            "beginnings of the "
            "Texas annexation controversy.\n\n"
            "Pennsylvania's economic "
            "interests — its "
            "iron and coal industries "
            "that benefited from "
            "protective tariffs "
            "— made it one "
            "of the most Whig-friendly "
            "states in the Union.\n\n"
            "His Interior appointment "
            "was the culmination "
            "of a long Whig "
            "career during the "
            "Fillmore administration.\n\n"
            "He was a Washington "
            "County Pennsylvania "
            "lawyer."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Pennsylvania Whig Congressman (1831–1839 and 1842–1843) and briefly Secretary of the Interior (1850); one of the first Interior Secretaries; resigned due to ill health after weeks in office; eight House years during the Jackson-Van Buren era; Pennsylvania's iron-industry Whig tradition; Washington County lawyer.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Pennsylvania's protective tariff economy — the state's iron and coal industries whose prosperity depended on tariff protection — aligned Pennsylvania with Whig economic policy and created McKennan's political base",
            "The Whig Party's organizational strength in Pennsylvania — the anti-Jacksonian coalition that Pennsylvania's commercial and industrial interests supported — provided the institutional framework for McKennan's long congressional career",
            "The creation of the Interior Department — the new cabinet department established by Congress in 1849 to manage the nation's internal affairs — created the position McKennan briefly held"
        ],
        "effects": [
            "His eight House years contributed Pennsylvania's Whig perspective to the Jackson and Van Buren era debates — the Bank War, nullification, and early territorial controversies",
            "His brief Interior Secretary tenure contributed to the new department's early organization — even a few weeks of service in a new department's establishment helped shape its early direction",
            "His career contributed to Pennsylvania's Whig tradition — the industrial-state Whiggery that would flow directly into the Republican Party after 1854",
            "His Interior appointment illustrated the Fillmore administration's Whig patronage — the cabinet appointments that rewarded long-serving Whig congressmen"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Pennsylvania Congressman 1831–1839 and 1842–1843"},
            {"target": "us-department-of-the-interior", "verb": "BRIEFLY_HEADS", "note": "Secretary of the Interior 1850"},
            {"target": "whig-party-united-states", "verb": "MEMBER_OF", "note": "Pennsylvania Whig congressman"},
            {"target": "bank-war", "verb": "SERVES_DURING", "note": "Whig congressman during Jackson's Bank War"},
            {"target": "millard-fillmore", "verb": "SERVES_UNDER", "note": "Interior Secretary under Fillmore"}
        ]
    }),

    ("andré-antoine-bernard", {
        "summary": (
            "André-Antoine Bernard "
            "(1751–1818) was a "
            "French revolutionary "
            "politician who served "
            "in the National "
            "Convention representing "
            "a French department "
            "during the radical "
            "republican phase "
            "of the Revolution. "
            "Convention members "
            "of this era participated "
            "in the most consequential "
            "legislative decisions "
            "of modern European "
            "history — the vote "
            "on Louis XVI's "
            "execution (January 1793), "
            "the abolition of "
            "feudalism and privilege, "
            "the declaration "
            "of the Republic, "
            "and the emergency "
            "governance during "
            "the crisis of "
            "war and civil conflict. "
            "Bernard's voting "
            "position on the "
            "king's trial — "
            "whether to vote "
            "death or a lesser "
            "sentence — would "
            "have been the "
            "most consequential "
            "single vote of "
            "his political career.\n\n"
            "The National Convention "
            "was the most "
            "powerful legislative "
            "body in French "
            "history — concentrating "
            "executive, legislative, "
            "and judicial powers "
            "in a single body "
            "during the republic's "
            "most dangerous years.\n\n"
            "His survival through "
            "the Terror and "
            "into the Consulate "
            "illustrated the "
            "political endurance "
            "required of "
            "Convention members.\n\n"
            "He was a French "
            "revolutionary republican."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "French National Convention member (1751–1818); voted on Louis XVI's execution trial; participated in the radical republican governance during the Terror and war crisis; survived through the Consulate; representative of the Convention's complex middle membership who shaped the radical phase's decisions.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The French Revolution's radicalization — the fall of the monarchy in August 1792 and the proclamation of the First Republic — created the National Convention in which Bernard served during the Republic's most dangerous years",
            "The crisis of 1793 — the foreign invasion, the Vendée civil war, and the Girondin-Jacobin conflict — created the emergency context in which the Convention concentrated extraordinary powers and made life-or-death political decisions",
            "Bernard's own republican commitment — his willingness to serve in the Convention and participate in its most consequential votes — created the political identity that made him a participant in the radical phase"
        ],
        "effects": [
            "His vote on Louis XVI's execution contributed to one of the most consequential decisions in modern European history — the regicide that made the Republic's survival a matter of necessity and provoked the European coalition's total war against France",
            "His Convention service contributed to the legislative work that abolished feudalism, established republican institutions, and created the legal foundations of modern France",
            "His survival through the Terror and into the Consulate contributed to the human continuity between the radical and moderate phases of the Revolution",
            "His career illustrated the Convention's complex sociology — the hundreds of deputies who participated in its decisions without being the famous protagonists of its dramas"
        ],
        "relationships": [
            {"target": "national-convention-france", "verb": "SERVES_IN", "note": "National Convention member"},
            {"target": "trial-of-louis-xvi", "verb": "VOTES_IN", "note": "Convention member voting on the king's trial"},
            {"target": "french-first-republic", "verb": "HELPS_ESTABLISH", "note": "Convention republican establishing the Republic"},
            {"target": "reign-of-terror", "verb": "SERVES_DURING", "note": "Convention member during the Terror"},
            {"target": "french-revolution", "verb": "PARTICIPATES_IN", "note": "Revolutionary republican politician"}
        ]
    }),

    ("chauncey-goodrich", {
        "summary": (
            "Chauncey Goodrich (1759–1815) "
            "was an American Federalist "
            "politician from Connecticut "
            "who served in the "
            "U.S. House (1795–1801), "
            "U.S. Senate (1807–1815), "
            "and as Lieutenant "
            "Governor of Connecticut "
            "(1813–1815) — dying "
            "in office. "
            "A leading Connecticut "
            "Federalist, Goodrich "
            "was one of the most "
            "ardent opponents "
            "of the Jeffersonian "
            "and Madisonian administrations "
            "in New England — "
            "opposing the Louisiana "
            "Purchase's constitutional "
            "validity, supporting "
            "the Essex Junto "
            "disunionism, and "
            "opposing the War "
            "of 1812 as a destructive, "
            "unconstitutional "
            "war on commerce. "
            "He was a delegate "
            "to the Hartford Convention "
            "(1814–1815) — the "
            "notorious gathering "
            "of New England "
            "Federalists that "
            "discussed secession "
            "and produced constitutional "
            "amendments.\n\n"
            "His Hartford Convention "
            "participation contributed "
            "to the Federalist "
            "Party's political "
            "destruction — "
            "the convention's "
            "appearance of treason "
            "during a successful "
            "war ending discrediting "
            "the party permanently.\n\n"
            "He was a Yale-educated "
            "lawyer and the "
            "son-in-law of Noah Webster.\n\n"
            "He died weeks "
            "after the Hartford "
            "Convention ended."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Connecticut Federalist Congressman (1795–1801), Senator (1807–1815), and Lt. Governor (1813–1815); ardent opponent of Jefferson and Madison; delegate to the Hartford Convention (1814–1815) — the meeting that ended Federalist Party credibility; son-in-law of Noah Webster; died in office weeks after Hartford Convention.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Connecticut's Federalist political culture — the state's commercial and religious establishment that provided the strongest Federalist base in New England and whose interests aligned with Britain rather than France — created the political environment of Goodrich's career",
            "The War of 1812's impact on New England commerce — the war's devastating effect on maritime trade and New England's commercial economy — created the intense opposition that drove Federalists like Goodrich to the Hartford Convention",
            "The Federalist Party's existential crisis — the party's steady decline under Jefferson and Madison and the desperate search for institutional survival through constitutional amendments — created the political context of the Hartford Convention"
        ],
        "effects": [
            "His Hartford Convention participation contributed to the event that ended the Federalist Party — the convention's demands and apparent disloyalty discrediting Federalism as the War of 1812 ended victoriously",
            "His long Senate and House career contributed Connecticut's Federalist opposition voice to the Jeffersonian and Madisonian legislative battles — the minority that fought the Virginia Dynasty's policies",
            "His family connection to Noah Webster contributed to Connecticut's interconnected Federalist intellectual and political elite — the network of Yale-educated lawyers, clergy, and politicians who dominated the state",
            "His death in office — just weeks after the Hartford Convention — spared him from witnessing the complete collapse of the Federalist cause and the ridicule his convention participation brought"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Connecticut Senator 1807–1815"},
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Connecticut Congressman 1795–1801"},
            {"target": "hartford-convention", "verb": "ATTENDS", "note": "Connecticut Federalist delegate to the convention"},
            {"target": "noah-webster", "verb": "SON_IN_LAW_OF", "note": "Son-in-law of the American lexicographer"},
            {"target": "federalist-party", "verb": "LEADS", "note": "Leading Connecticut Federalist politician"}
        ]
    }),

    ("john-milton-niles", {
        "summary": (
            "John Milton Niles (1787–1856) "
            "was an American Democratic "
            "politician from Connecticut "
            "who served as a "
            "U.S. Senator (1835–1839 "
            "and 1843–1849) and "
            "briefly as Postmaster "
            "General under Martin "
            "Van Buren (1840–1841). "
            "A Connecticut Democrat — "
            "rare in Federalist-Whig "
            "Connecticut — Niles "
            "was a founder of "
            "the Hartford Times "
            "newspaper, a vehicle "
            "for Democratic "
            "politics in a "
            "Whig-dominated state. "
            "His Senate career "
            "spanned the Van "
            "Buren and Polk "
            "administrations "
            "— from the Specie "
            "Circular and Panic "
            "of 1837 through "
            "the Independent "
            "Treasury debates, "
            "the Texas annexation, "
            "and the Mexican-American "
            "War controversies.\n\n"
            "Connecticut's status "
            "as a competitive "
            "state — not the "
            "Democratic monolith "
            "that the Deep South "
            "was — made Niles's "
            "Senate career a genuine "
            "political achievement "
            "in adverse terrain.\n\n"
            "He was also an "
            "early biographer "
            "of John C. Calhoun "
            "— though the political "
            "distance between "
            "them was considerable.\n\n"
            "He was a Hartford "
            "lawyer, journalist, "
            "and Democratic politician."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Connecticut Democratic Senator (1835–1839 and 1843–1849) and Postmaster General under Van Buren (1840–1841); founder of the Hartford Times; served during the Panic of 1837, Independent Treasury debates, and Mexican-American War; Connecticut Democrat in a Whig-dominated state; early biographer of John C. Calhoun; Hartford lawyer and Democratic journalist-politician.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Jacksonian Democracy's national political appeal — Jackson's coalition-building across the Northeast that created viable Democratic organizations even in Federalist-Whig states like Connecticut — enabled Niles's Senate career as a Connecticut Democrat",
            "The Panic of 1837 — the economic crisis produced by Jackson's Specie Circular and Van Buren's Independent Treasury response — created the defining economic controversy of Niles's early Senate service",
            "The Hartford Times — the Democratic newspaper Niles founded that provided both a political vehicle and personal platform for Connecticut Democratic politics — created the institutional foundation for his political career"
        ],
        "effects": [
            "His Senate service contributed Connecticut's Democratic voice to the Van Buren and Polk era debates — rare in a state where Whigs dominated, his presence provided the Democratic perspective",
            "His Postmaster General service contributed to the postal patronage system — the party-based appointment of postmasters that was a crucial Democratic Party organizational tool",
            "His Hartford Times founding contributed to Connecticut's Democratic political culture — the newspaper infrastructure that sustained the party in adverse terrain",
            "His Calhoun biography contributed to the historical documentation of one of the most controversial figures in American political history — though his New England Democratic perspective differed sharply from Calhoun's Southern nullificationism"
        ],
        "relationships": [
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Connecticut Democratic Senator 1835–1839 and 1843–1849"},
            {"target": "us-postmaster-general", "verb": "SERVES_AS", "note": "Postmaster General under Van Buren 1840–1841"},
            {"target": "hartford-times", "verb": "FOUNDS", "note": "Democratic newspaper in Whig Connecticut"},
            {"target": "martin-van-buren", "verb": "SERVES_UNDER", "note": "Postmaster General in Van Buren's cabinet"},
            {"target": "connecticut", "verb": "REPRESENTS", "note": "Connecticut Democrat senator in a Whig state"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 84 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
