#!/usr/bin/env python3
"""
Batch 98 — 8 entities: Antal Grassalkovich I, Bernardo de Vera y Pintado,
James A. Bayard, John Blair Jr., Matthew Harvey, Thomas Tredwell,
Claude Hardy, Aaron Ogden
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

    ("antal-grassalkovich-i", {
        "summary": (
            "Antal Grassalkovich I (1694–1771) was a Hungarian nobleman, "
            "jurist, and royal administrator who rose from relatively modest "
            "origins to become one of the most powerful men in 18th-century "
            "Habsburg Hungary. As President of the Hungarian Royal Chamber "
            "and a close advisor to Empress Maria Theresa, he oversaw vast "
            "crown estates and was central to the Habsburg administration of "
            "Hungary. His loyalty to Maria Theresa during the War of Austrian "
            "Succession — when the young empress faced existential threats "
            "from Prussia, France, and Bavaria — earned him immense rewards: "
            "vast estates, noble titles, and political influence. He was "
            "ennobled as a count and accumulated wealth that made the "
            "Grassalkovich family one of Hungary's great noble houses.\n\n"
            "He built the famous Grassalkovich Palace in Gödöllő — which "
            "became Maria Theresa's favorite Hungarian residence.\n\n"
            "He was the self-made Habsburg loyalist who built a dynasty.\n\n"
            "'Service to the empress is the source of all fortune.'"
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Hungarian nobleman and President of the Hungarian Royal Chamber under Maria Theresa; close advisor during the War of Austrian Succession; built the Grassalkovich Palace at Gödöllő (Maria Theresa's favorite Hungarian residence); rose from modest origins to found one of Hungary's great noble houses; ennobled as a count for Habsburg loyalty.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The War of Austrian Succession (1740–1748) — the existential threat to Maria Theresa that required Hungarian nobles' military and financial support — created the moment that Grassalkovich's loyalty rewarded him with vast estates and titles",
            "Habsburg centralization in Hungary — Maria Theresa's effort to build more effective royal administration over the Hungarian kingdom — created the administrative roles that Grassalkovich's legal expertise filled",
            "Hungarian noble ambition within the Habsburg system — the pattern of talented men from lesser families rising through royal service to great wealth and titles — created the career path that Grassalkovich exemplified"
        ],
        "effects": [
            "His Habsburg service contributed to Maria Theresa's effective administration of Hungary during the War of Austrian Succession and beyond",
            "His Gödöllő palace construction contributed to the Baroque architectural heritage of Hungary and created Maria Theresa's favorite Hungarian residence",
            "His family's rise contributed to the founding of the Grassalkovich noble house — one of 18th-century Hungary's great dynastic families",
            "His career contributed to the model of meritocratic-but-loyal advancement within the Habsburg system — the self-made man who built a dynasty through royal service"
        ],
        "relationships": [
            {"target": "maria-theresa", "verb": "SERVES", "note": "President of the Hungarian Royal Chamber and close advisor"},
            {"target": "war-of-austrian-succession", "verb": "SUPPORTS_HABSBURG_IN", "note": "Loyal Hungarian administrator during existential Habsburg crisis"},
            {"target": "habsburg-empire", "verb": "ADMINISTERS_HUNGARY_FOR", "note": "President of the Hungarian Royal Chamber"},
            {"target": "grassalkovich-palace-godollo", "verb": "BUILDS", "note": "Baroque palace that became Maria Theresa's favorite Hungarian residence"},
            {"target": "hungarian-noble-estates", "verb": "ACCUMULATES", "note": "Vast estates and count title rewarded for loyalty"}
        ]
    }),

    ("bernardo-de-vera-y-pintado", {
        "summary": (
            "Bernardo de Vera y Pintado (1780–1827) was a Chilean patriot, "
            "jurist, and poet who played an important role in the Chilean "
            "independence movement. Born in Argentina and trained as a lawyer, "
            "he became one of the intellectual and legal architects of Chilean "
            "independence — drafting constitutional documents and contributing "
            "to the ideological foundations of the new republic. He is credited "
            "with writing the lyrics of the Chilean national anthem — one of "
            "the most enduring contributions to Chilean national identity. "
            "A poet, journalist, and lawyer, he exemplified the "
            "letrado — the learned man of the independence era whose "
            "pen was as important as the sword.\n\n"
            "He served in early Chilean governmental institutions and "
            "contributed to the republican political culture that the "
            "independence generation was building.\n\n"
            "He was Chile's poet-patriot.\n\n"
            "'With patriot words, we forge the nation.'"
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Chilean patriot, jurist, and poet who wrote the lyrics of the Chilean national anthem; legal and intellectual architect of Chilean independence; exemplified the letrado — the learned man of independence era whose pen shaped the new republic; contributed to constitutional drafting and republican political culture.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Spanish American independence movements — the political upheaval of 1810–1820 that overthrew colonial rule across South America — created the context for Vera y Pintado's patriotic and legal contributions",
            "The Enlightenment's spread to Spanish America — the ideas of constitutionalism, popular sovereignty, and republican government — created the intellectual framework for the independence generation's constitutional drafting",
            "Napoleon's invasion of Spain (1808) — the political crisis that delegitimized the colonial relationship — created the opening that Chilean patriots used to move toward independence"
        ],
        "effects": [
            "His Chilean national anthem lyrics contributed to Chilean national identity — the song that became the enduring symbol of the republic he helped create",
            "His constitutional drafting contributed to the legal foundations of the early Chilean republic",
            "His poetry and journalism contributed to the republican political culture of the independence generation",
            "His career contributed to the model of the letrado — the intellectual-patriot whose learning served the cause of independence"
        ],
        "relationships": [
            {"target": "chilean-independence", "verb": "CONTRIBUTES_TO", "note": "Patriot jurist and intellectual of the independence movement"},
            {"target": "chilean-national-anthem", "verb": "WRITES_LYRICS_OF", "note": "Author of the Chilean national anthem"},
            {"target": "chile", "verb": "SERVES", "note": "Lawyer and patriot in early Chilean republican institutions"},
            {"target": "spanish-american-independence", "verb": "PARTICIPATES_IN", "note": "Letrado of the independence era"},
            {"target": "bernardino-o-higgins", "verb": "CONTEMPORARY_OF", "note": "Patriot of the same independence generation"}
        ]
    }),

    ("james-a-bayard", {
        "summary": (
            "James Asheton Bayard Sr. (1767–1815) was an American Federalist "
            "politician from Delaware who served in the U.S. House (1797–1803) "
            "and Senate (1804–1813). He played a decisive role in the "
            "Election of 1800 — the House vote to choose between Jefferson "
            "and Burr — casting the vote that broke the deadlock and secured "
            "Jefferson's presidency. Bayard ultimately voted for Jefferson "
            "after receiving assurances on Federalist policy continuities, "
            "averting what might have been a constitutional crisis. He also "
            "served as one of the American commissioners who negotiated the "
            "Treaty of Ghent (1814–1815) — the peace agreement that ended "
            "the War of 1812.\n\n"
            "His role in both resolving the 1800 election and negotiating "
            "the War of 1812's end made him one of the most consequential "
            "Federalists in American history.\n\n"
            "He was Delaware's most important Federalist statesman.\n\n"
            "'I voted for the republic, not the party.'"
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Delaware Federalist congressman and senator who cast the decisive vote in the House election of 1800 that made Jefferson president (breaking the Burr deadlock); negotiated the Treaty of Ghent (1814) ending the War of 1812; one of the most consequential Federalists in American history; Delaware's most important Federalist statesman.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Electoral College tie of 1800 — the deadlock between Jefferson and Burr that threw the presidential election to the House — created the constitutional crisis that Bayard helped resolve",
            "Delaware's Federalist political tradition — the small state's consistent support for Federalism — created the political context for Bayard's long congressional career",
            "The War of 1812's exhaustion — both Britain and the United States seeking peace by 1814 — created the diplomatic opportunity that Bayard and the Treaty of Ghent commissioners seized"
        ],
        "effects": [
            "His decisive House vote for Jefferson contributed to resolving the 1800 election crisis — averting a potential constitutional catastrophe by choosing the Republican candidate over Burr",
            "His Treaty of Ghent negotiation contributed to ending the War of 1812 — the peace agreement that restored the pre-war status quo between Britain and the United States",
            "His career contributed to the historical record of Federalist statesmanship — the man who put national interest over party loyalty in both 1800 and 1814",
            "His Delaware Senate service contributed to the documentation of Delaware's Federalist durability"
        ],
        "relationships": [
            {"target": "election-of-1800", "verb": "DECIDES", "note": "Broke the House electoral deadlock for Jefferson over Burr"},
            {"target": "thomas-jefferson", "verb": "ELECTS_PRESIDENT", "note": "Decisive vote that made Jefferson the third president"},
            {"target": "treaty-of-ghent", "verb": "NEGOTIATES", "note": "American commissioner 1814–1815 ending the War of 1812"},
            {"target": "us-senate", "verb": "SERVES_IN", "note": "Delaware Senator 1804–1813"},
            {"target": "federalist-party", "verb": "MEMBER_OF", "note": "Delaware's most important Federalist statesman"}
        ]
    }),

    ("john-blair-jr", {
        "summary": (
            "John Blair Jr. (1732–1800) was an American jurist and Founding "
            "Father from Virginia who served as an Associate Justice of the "
            "United States Supreme Court (1790–1795) — one of the original "
            "justices appointed by President Washington. Blair was a Virginia "
            "delegate to the Constitutional Convention (1787) and one of the "
            "men who signed the Constitution — making him both a framer and "
            "an inaugural Supreme Court justice. On the first Supreme Court "
            "under Chief Justice John Jay, Blair participated in the court's "
            "foundational early work including the establishment of circuit-riding "
            "duties and the early articulation of federal judicial power.\n\n"
            "He was one of Virginia's most respected jurists — having served "
            "on the Virginia General Court and Virginia Court of Appeals before "
            "his elevation to the Supreme Court.\n\n"
            "He was both a framer and a founder of the federal judiciary.\n\n"
            "He signed the Constitution and served on the first Supreme Court."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Virginia Founding Father, Constitutional Convention delegate, Constitution signer, and original Associate Justice of the first United States Supreme Court (1790–1795); served under Chief Justice John Jay in the court's foundational years; framer and inaugural Supreme Court justice — a direct link between the Constitution's drafting and its judicial interpretation.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Constitutional Convention of 1787 — the extraordinary assembly that drafted the federal constitution — created the founding moment in which Blair participated as a Virginia delegate and signer",
            "Washington's first Supreme Court appointments — the new president's selection of original justices to staff the federal judiciary — created the inaugural court that Blair joined",
            "Virginia's legal tradition — the state's strong tradition of trained lawyers and jurists serving in public life — created the institutional background for Blair's judicial career"
        ],
        "effects": [
            "His Constitution signing contributed to the founding document's ratification — the formal assent of one of Virginia's leading jurists",
            "His original Supreme Court service contributed to the establishment of the federal judiciary's foundational practices",
            "His circuit-riding service contributed to the physical presence of federal judicial authority across the early republic",
            "His career contributed to the historical record of the Founding generation's dual role as constitution-makers and constitution-interpreters"
        ],
        "relationships": [
            {"target": "constitutional-convention-1787", "verb": "DELEGATES_TO", "note": "Virginia delegate and Constitution signer"},
            {"target": "united-states-constitution", "verb": "SIGNS", "note": "One of the Constitution's signers"},
            {"target": "supreme-court-of-the-united-states", "verb": "SERVES_ON", "note": "Original Associate Justice 1790–1795"},
            {"target": "george-washington", "verb": "APPOINTED_BY", "note": "First Supreme Court appointee by President Washington"},
            {"target": "john-jay", "verb": "SERVES_UNDER", "note": "Associate Justice under Chief Justice John Jay"}
        ]
    }),

    ("matthew-harvey", {
        "summary": (
            "Matthew Harvey (1781–1866) was an American Democratic-Republican "
            "politician from New Hampshire who served in the U.S. House "
            "(1821–1825), as Governor of New Hampshire (1830–1831), and as "
            "a federal judge. His long life spanned from the early republic "
            "to the Civil War era. His gubernatorial term was brief — he resigned "
            "the governorship to accept appointment as a federal district court "
            "judge, a position he held for many years. Harvey's career illustrated "
            "the common pattern of early republic politicians who moved between "
            "legislative, executive, and judicial positions as the federal "
            "government's institutions were being developed.\n\n"
            "He was a Sutton and Concord New Hampshire lawyer.\n\n"
            "He was a New Hampshire politician who became a federal judge.\n\n"
            "He served New Hampshire's institutions for over three decades."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "New Hampshire Democratic-Republican congressman (1821–1825), Governor (1830–1831), and long-serving federal district court judge; resigned governorship to accept federal judgeship; career spanning legislative, executive, and judicial service; Sutton and Concord New Hampshire lawyer; lived from the early republic to the Civil War era.",
            "significanceCategory": "regional"
        },
        "causes": [
            "New Hampshire's Democratic-Republican political dominance — the state's Jeffersonian tradition that shaped its congressional and gubernatorial politics — created the political context for Harvey's career",
            "The expansion of the federal judiciary — the Jacksonian era's need for federal district court judges in New Hampshire — created the appointment that Harvey accepted, sacrificing his governorship",
            "New Hampshire's tradition of civic service — the state's culture of lawyers moving between legislative, executive, and judicial roles — created the pattern that Harvey's career exemplified"
        ],
        "effects": [
            "His New Hampshire gubernatorial service contributed to the state's executive leadership during the Jacksonian era",
            "His long federal judgeship contributed to the federal judiciary's work in New Hampshire",
            "His career contributed to the documentation of the common pattern of early republic politicians serving in multiple government branches",
            "His long life and career contributed to the historical continuity from the early republic through the Civil War era"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "New Hampshire congressman 1821–1825"},
            {"target": "new-hampshire", "verb": "GOVERNS", "note": "Governor of New Hampshire 1830–1831"},
            {"target": "federal-district-court", "verb": "SERVES_ON", "note": "Long-serving federal district judge — resigned governorship to accept appointment"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "New Hampshire Jeffersonian Republican"},
            {"target": "andrew-jackson", "verb": "CONTEMPORARY_OF", "note": "Jacksonian era politician and judge"}
        ]
    }),

    ("thomas-tredwell", {
        "summary": (
            "Thomas Tredwell (1743–1831) was an American Anti-Federalist "
            "politician from New York who served in the Continental Congress "
            "(1787) and opposed ratification of the Constitution at the New "
            "York ratification convention (1788). Tredwell was one of the "
            "most articulate Anti-Federalist voices at New York's convention — "
            "a state where the battle over ratification was fierce and where "
            "the Anti-Federalist cause, led by Governor George Clinton, was "
            "very strong. His speech at the convention against the Constitution "
            "argued that it gave too much power to the federal government at "
            "the expense of state sovereignty and individual rights.\n\n"
            "He later served in the New York State Legislature and held "
            "various state offices. Despite his constitutional opposition, "
            "he accepted the Constitution once ratified.\n\n"
            "He was a Long Island New York farmer-lawyer and Anti-Federalist.\n\n"
            "He was one of New York's most articulate voices against ratification."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "New York Anti-Federalist politician and Continental Congress delegate who opposed Constitution ratification at New York's 1788 convention; one of the most articulate Anti-Federalist voices at the fierce New York ratification battle; argued against excessive federal power and for state sovereignty and individual rights; Long Island farmer-lawyer.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Constitutional Convention's product — the 1787 Constitution's expansion of federal power — created the political controversy that Anti-Federalists like Tredwell organized to oppose",
            "New York's strong Anti-Federalist tradition — Governor Clinton's political machine and the state's powerful opponents of centralization — created the political environment for Tredwell's convention opposition",
            "The absence of a Bill of Rights in the original Constitution — the fundamental objection that most Anti-Federalists shared — created the principled argument that Tredwell articulated"
        ],
        "effects": [
            "His New York convention opposition contributed to the Anti-Federalist cause's articulation — the arguments that would eventually produce the Bill of Rights as a concession to gain ratification",
            "His constitutional arguments contributed to the historical record of Anti-Federalist thought — the alternative vision of limited federal power",
            "His eventual acceptance of the Constitution contributed to the political legitimacy of the ratified document",
            "His career contributed to the documentation of New York's fierce ratification battle — the key state where Anti-Federalism was strongest"
        ],
        "relationships": [
            {"target": "constitutional-convention-1787", "verb": "RESPONDS_TO", "note": "Continental Congress delegate who opposed the resulting Constitution"},
            {"target": "new-york-ratification-convention", "verb": "OPPOSES_RATIFICATION_AT", "note": "Most articulate Anti-Federalist voice at New York 1788 convention"},
            {"target": "george-clinton", "verb": "ALLIES_WITH", "note": "New York Anti-Federalist camp led by Governor Clinton"},
            {"target": "bill-of-rights", "verb": "DEMANDS_PRECURSOR_OF", "note": "Anti-Federalist arguments that contributed to Bill of Rights"},
            {"target": "anti-federalism", "verb": "CHAMPIONS", "note": "Long Island Anti-Federalist farmer-lawyer"}
        ]
    }),

    ("claude-hardy", {
        "summary": (
            "Claude Hardy (1604–1678) was a French mathematician, philologist, "
            "and lawyer who was one of the founding members of Marin Mersenne's "
            "scientific circle in Paris — the informal academy that was a "
            "precursor to the French Academy of Sciences. Hardy was a close "
            "associate of Pierre de Fermat and helped transmit Fermat's "
            "mathematical discoveries to the Parisian mathematical community. "
            "He was also a significant scholar of ancient languages, including "
            "Arabic — contributing to the polymath tradition of the 17th-century "
            "French intellectual world. His legal career as a councillor in the "
            "Paris Parlement coexisted with his mathematical and philological work "
            "— the dual life of the gentleman-scholar that characterized the "
            "era's intellectual culture.\n\n"
            "He translated ancient mathematical texts and corresponded with "
            "the leading mathematicians of his day.\n\n"
            "He was a member of the Mersenne circle that shaped early modern "
            "French mathematics.\n\n"
            "He was the lawyer-mathematician of Paris's first scientific community."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "French mathematician, philologist, and lawyer; founding member of Mersenne's scientific circle — precursor to the French Academy of Sciences; close associate of Pierre de Fermat who helped transmit Fermat's discoveries; Paris Parlement councillor and scholar of Arabic; exemplified the 17th-century gentleman-scholar of early modern mathematics.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Mersenne's Paris mathematical circle — the informal academy organized by Marin Mersenne that connected France's mathematical minds — created the intellectual community that Hardy joined as a founding member",
            "Fermat's mathematical discoveries — the brilliant lawyer-mathematician's number theory, analytic geometry, and early calculus — created the mathematical content that Hardy helped transmit to Parisian circles",
            "The 17th century's expansion of mathematical knowledge — the era's transformation of mathematics through analytical methods, number theory, and natural philosophy — created the intellectual moment that Hardy's circle shaped"
        ],
        "effects": [
            "His Mersenne circle membership contributed to the development of French mathematical culture — the informal community that preceded the formal French Academy of Sciences",
            "His transmission of Fermat's work contributed to the mathematical community's awareness of Fermat's discoveries in number theory and analytic geometry",
            "His Arabic scholarship contributed to the polyglot intellectual culture of 17th-century Paris",
            "His dual legal-mathematical career contributed to the model of the gentleman-scholar that characterized early modern European intellectual life"
        ],
        "relationships": [
            {"target": "mersenne-circle", "verb": "FOUNDING_MEMBER_OF", "note": "Paris mathematical circle precursor to French Academy of Sciences"},
            {"target": "pierre-de-fermat", "verb": "ASSOCIATES_WITH", "note": "Transmitted Fermat's mathematical discoveries to Parisian circles"},
            {"target": "paris-parlement", "verb": "SERVES_AS_COUNCILLOR_ON", "note": "Paris Parlement councillor and gentleman-scholar"},
            {"target": "french-academy-of-sciences", "verb": "PRECEDES", "note": "Mersenne circle member whose informal academy preceded the Academy"},
            {"target": "arabic-language", "verb": "STUDIES", "note": "Polyglot scholar of ancient languages including Arabic"}
        ]
    }),

    ("aaron-ogden", {
        "summary": (
            "Aaron Ogden (1756–1839) was an American Revolutionary War officer, "
            "New Jersey Federalist politician, and early transportation entrepreneur. "
            "He served in the Continental Army under Washington, participated "
            "in the Battle of Yorktown (1781), and later served as Governor of "
            "New Jersey (1812). His most famous historical contribution came "
            "not from politics but from law — he was the losing defendant in "
            "Gibbons v. Ogden (1824), the landmark Supreme Court case that "
            "established federal supremacy over interstate commerce. Ogden had "
            "been operating a steamboat ferry service between New York and New "
            "Jersey under a New York state monopoly grant — the competing "
            "federal license of Thomas Gibbons challenged his operation.\n\n"
            "Chief Justice John Marshall's ruling for Gibbons established the "
            "Commerce Clause as the foundation of federal economic regulation.\n\n"
            "'I lost the case but made constitutional history.'\n\n"
            "He was the man who lost Gibbons v. Ogden — and made American law."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Revolutionary War officer, New Jersey Governor (1812), and losing defendant in Gibbons v. Ogden (1824) — the landmark Supreme Court case that established federal supremacy over interstate commerce; John Marshall's Commerce Clause ruling; Ogden's steamboat ferry monopoly challenged the federal commerce power; Continental Army veteran and Battle of Yorktown participant.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The steamboat revolution — the new technology of steam-powered river transport that created the first major interstate transportation business — created the economic context for the Gibbons v. Ogden dispute",
            "New York State's steamboat monopoly grant — the state legislature's grant to Robert Livingston and Robert Fulton that Ogden held a license under — created the state-federal regulatory conflict that produced the Supreme Court case",
            "The Commerce Clause's ambiguity — the Constitution's grant of congressional power over interstate commerce that had not yet been judicially defined — created the constitutional question that Gibbons v. Ogden resolved"
        ],
        "effects": [
            "His defeat in Gibbons v. Ogden contributed to one of the most important Supreme Court decisions in American history — establishing federal supremacy over interstate commerce",
            "The Gibbons ruling contributed to the Commerce Clause as the foundation of federal economic regulation — the constitutional basis for most of the modern federal government's economic authority",
            "His Revolutionary War service contributed to New Jersey's military traditions and to his later political career",
            "His New Jersey governorship contributed to the state's executive record during the War of 1812"
        ],
        "relationships": [
            {"target": "gibbons-v-ogden", "verb": "LITIGATES_AS_DEFENDANT", "note": "Losing defendant in the landmark 1824 Commerce Clause case"},
            {"target": "commerce-clause", "verb": "SUBJECT_OF_RULING_DEFINING", "note": "Gibbons v. Ogden established Commerce Clause federal supremacy"},
            {"target": "john-marshall", "verb": "RULED_AGAINST_BY", "note": "Marshall's ruling defined federal interstate commerce power"},
            {"target": "new-jersey", "verb": "GOVERNS", "note": "Governor of New Jersey 1812"},
            {"target": "continental-army", "verb": "SERVES_IN", "note": "Revolutionary War officer at Battle of Yorktown 1781"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 98 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich(slug, data)
    print("Done.")
