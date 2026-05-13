#!/usr/bin/env python3
"""
Batch 26 — 8 entities: Francis Scott Key, William Cushing, Oliver Wolcott,
Rufus Choate, Rawlins Lowndes, Cristóbal Mendoza, François Hotman,
José de Antequera y Castro
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

    # 1 — Francis Scott Key
    ("francis-scott-key", {
        "summary": (
            "Francis Scott Key (1779–1843) was an American lawyer, poet, and government "
            "official from Frederick, Maryland, who is best remembered as the author of "
            "'Defence of Fort M'Henry' (1814) — the poem set to a popular British drinking "
            "tune that became, a century later, the national anthem of the United States: "
            "The Star-Spangled Banner. Key composed the poem during the night and morning "
            "of September 13–14, 1814, while detained aboard a British ship in Baltimore "
            "Harbor during the British naval bombardment of Fort McHenry — watching "
            "through the night to see whether the fort would survive, and writing his "
            "relief in verse when the American flag was still flying at dawn.\n\n"
            "Key's professional career was primarily as a lawyer — he was a prominent "
            "Washington DC attorney who argued more than 100 cases before the US Supreme "
            "Court and served as US Attorney for the District of Columbia (1833–1841) under "
            "President Andrew Jackson. His legal practice combined federal litigation with "
            "Washington DC political connections, and his role as US Attorney put him in "
            "charge of federal prosecutions in the capital during a significant period. "
            "He was also a committed Episcopalian and lay church leader who helped found "
            "the American Colonization Society — an organization that advocated for the "
            "voluntary emigration of freed Black Americans to Africa, which Key supported "
            "as a slaveholder who believed this solution could resolve the contradiction "
            "between slavery and American republican ideals.\n\n"
            "His involvement in the trial of Richard Lawrence — who had attempted to "
            "assassinate President Andrew Jackson in 1835 — was one of his more notable "
            "legal moments. He personally conducted the prosecution, and Lawrence's "
            "acquittal on grounds of insanity established one of the earliest uses of "
            "the insanity defense in American law.\n\n"
            "The contradiction between his authorship of a hymn to American liberty and "
            "his role as a slaveholder has made him a contested figure in American memory."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Author of 'Defence of Fort M'Henry' (1814) — the poem that became the US national anthem 'The Star-Spangled Banner'; US Attorney for DC (1833–41); prominent Washington lawyer who prosecuted the Richard Lawrence insanity case (1835) — an early landmark in American insanity defense jurisprudence.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The British bombardment of Fort McHenry during the War of 1812 — specifically Key's unique position detained on a British vessel watching the attack — created the precise circumstances that produced his poem",
            "His prior negotiations with the British as a private citizen (seeking to secure the release of a captured American physician) placed him in British captivity during the battle that inspired the poem",
            "The deeply felt American patriotism of the post-Revolutionary generation — of which Key was part — provided the emotional framework that transformed a specific military observation into a national hymn"
        ],
        "effects": [
            "His poem 'Defence of Fort M'Henry' (1814) became, through public adoption and eventual legislation, the national anthem of the United States — among the most recognized pieces of American cultural identity",
            "His prosecution of Richard Lawrence (1835) — acquitted on an insanity defense — contributed to one of the earliest significant uses of the insanity defense in American criminal law, establishing a precedent that remains contentious",
            "His role as US Attorney for DC under Jackson placed him in the federal prosecutorial establishment during the Jacksonian era — including involvement in politically sensitive cases",
            "His support for the American Colonization Society — a solution to slavery that his contemporaries debated intensely — reflected the moral contradictions of the slaveholding class's engagement with emancipation questions"
        ],
        "relationships": [
            {"entity": "The Star-Spangled Banner (US national anthem)", "relationship": "AUTHORED", "note": "Author of 'Defence of Fort M'Henry' (1814) — the poem set to music that became the US national anthem"},
            {"entity": "Bombardment of Fort McHenry (September 1814)", "relationship": "WITNESSED_FROM_BRITISH_SHIP", "note": "Composed his poem during the British naval bombardment of Fort McHenry while detained aboard a British vessel in Baltimore Harbor"},
            {"entity": "Andrew Jackson (US President)", "relationship": "SERVED_UNDER_AS_US_ATTORNEY", "note": "Served as US Attorney for the District of Columbia (1833–1841) under President Jackson"},
            {"entity": "Richard Lawrence assassination attempt (1835)", "relationship": "PROSECUTED", "note": "Prosecuted Richard Lawrence for the attempted assassination of President Jackson in 1835 — Lawrence's acquittal on insanity grounds was an early landmark in American insanity defense law"},
            {"entity": "American Colonization Society", "relationship": "CO-FOUNDED_AND_SUPPORTED", "note": "Supported the American Colonization Society's project of 'solving' slavery through the voluntary emigration of freed Black Americans to Liberia — a deeply problematic 'solution' he endorsed as a slaveholder"}
        ]
    }),

    # 2 — William Cushing
    ("william-cushing", {
        "summary": (
            "William Cushing (1732–1810) was an American lawyer and jurist from "
            "Massachusetts who served as one of the original six Associate Justices of "
            "the United States Supreme Court — confirmed by the Senate on September 26, "
            "1789, just two days after the Court itself was established by the Judiciary "
            "Act — and who served on the Court for 20 years and 11 months, the longest "
            "tenure among the Court's inaugural members. He declined, for reasons of "
            "health, a nomination to succeed John Jay as Chief Justice in 1795, a "
            "position that went instead to Oliver Ellsworth.\n\n"
            "Before his federal appointment, Cushing had a distinguished career in "
            "Massachusetts colonial and revolutionary law. He served as a justice and "
            "then Chief Justice of the Massachusetts Superior Court — the colony's and "
            "then state's highest court — and was one of the few colonial judges to "
            "remain on the bench through the Revolution rather than having to choose "
            "exile or resistance. His tenure in that role included presiding over the "
            "'slavery cases' of 1783 — Commonwealth v. Jennison — in which the court "
            "ruled that the Massachusetts Constitution's declaration that 'all men are "
            "born free and equal' effectively abolished slavery in Massachusetts. This "
            "decision made Massachusetts the first American state where slavery was "
            "judicially declared incompatible with the state constitution.\n\n"
            "On the federal bench, Cushing was part of the Marshall Court's precursor "
            "— the foundational period of the Supreme Court under Chief Justices Jay "
            "and Ellsworth — when the Court was establishing its procedures, authority, "
            "and jurisprudential identity. His long service provided essential continuity "
            "across the transition from Jay to Ellsworth to Marshall.\n\n"
            "He was the last American judge to wear a full wig — a practice he maintained "
            "from colonial times that became the subject of mockery in the new republic."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "One of the original six Associate Justices of the US Supreme Court (1789–1810); the longest-serving inaugural member; presided over Commonwealth v. Jennison (1783) which judicially abolished slavery in Massachusetts — the first such judicial ruling in any American state.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Constitution's establishment of the federal judiciary and the Judiciary Act of 1789 — which created the Supreme Court — produced the institution to which President Washington appointed him as one of the original six justices",
            "The Massachusetts Constitution of 1780's declaration that 'all men are born free and equal' created the legal basis for the Jennison slavery ruling he presided over — making his judicial ruling possible",
            "His established reputation as a Massachusetts jurist and his continuity on the bench through the Revolution made him a natural choice for Washington's foundational Supreme Court appointments"
        ],
        "effects": [
            "His role in Commonwealth v. Jennison (1783) effectively abolished slavery in Massachusetts through judicial interpretation — the first judicial abolition of slavery in any American state, predating legislative abolition in most northern states",
            "His 20-year tenure as an inaugural Supreme Court Justice provided the continuity that helped stabilize the Court's procedures and authority during its foundational period",
            "His declination of the Chief Justice nomination in 1795 — for health reasons — led to Oliver Ellsworth's appointment, shaping the trajectory of the Court's leadership before Marshall",
            "His long service across the Jay, Ellsworth, and Marshall Courts made him a unique link between the Court's earliest years and its definitive constitutional formation"
        ],
        "relationships": [
            {"entity": "US Supreme Court (founding era)", "relationship": "INAUGURAL_ASSOCIATE_JUSTICE_OF", "note": "One of the original six Associate Justices of the Supreme Court; confirmed September 26, 1789 — among the Court's founding members"},
            {"entity": "Commonwealth v. Jennison (Massachusetts, 1783)", "relationship": "PRESIDED_OVER", "note": "Presided over the case in which the Massachusetts court ruled that the state constitution's equality clause abolished slavery — the first judicial abolition in any American state"},
            {"entity": "President George Washington", "relationship": "APPOINTED_BY", "note": "Appointed to the Supreme Court by President Washington in 1789 as part of the Court's founding membership"},
            {"entity": "Chief Justice nomination (1795)", "relationship": "DECLINED", "note": "Declined Washington's nomination to become Chief Justice in 1795 for health reasons — Oliver Ellsworth was appointed instead"},
            {"entity": "Massachusetts slavery abolition (1783)", "relationship": "JUDICIAL_INSTRUMENT_OF", "note": "His court's ruling in Commonwealth v. Jennison judicially abolished slavery in Massachusetts through constitutional interpretation in 1783"}
        ]
    }),

    # 3 — Oliver Wolcott Jr.
    ("oliver-wolcott", {
        "summary": (
            "Oliver Wolcott Jr. (1760–1833) was an American statesman who served as the "
            "second United States Secretary of the Treasury (1795–1800) — succeeding "
            "Alexander Hamilton, whose financial system he administered and defended "
            "through the turbulent final years of the Federalist era — and subsequently "
            "as the 24th Governor of Connecticut (1817–1827), where he presided over "
            "significant constitutional reform. His career spans the critical transition "
            "from the Federalist first administration through the collapse of Federalist "
            "power and into the Era of Good Feelings.\n\n"
            "As Treasury Secretary under Presidents Washington and John Adams, Wolcott's "
            "primary task was implementing and defending the Hamiltonian financial system "
            "— the First Bank of the United States, the federal assumption of state debts, "
            "and the revenue administration built during Hamilton's tenure. He was a loyal "
            "Hamiltonian Federalist who managed the Treasury during the XYZ Affair "
            "diplomatic crisis with France, the Quasi-War naval conflict, and the political "
            "battles over taxation that produced the Whiskey Rebellion's aftermath. "
            "His Treasury tenure coincided with some of the most dramatic moments in "
            "early American foreign and financial policy.\n\n"
            "He left the Treasury in 1800 — eventually transitioning to the Republican "
            "Party — and later served ten years as Connecticut's governor, during which "
            "he championed the state's 1818 constitution. Connecticut's 1818 constitution "
            "was a landmark: it eliminated the property qualification for voting, "
            "disestablished the Congregational church as the state church, and replaced "
            "the colonial-era Fundamental Orders with a modern republican constitution — "
            "making Wolcott's gubernatorial tenure consequential for Connecticut's "
            "democratic development.\n\n"
            "His father, Oliver Wolcott Sr., was a signer of the Declaration of Independence "
            "— making him a member of one of Connecticut's founding political families."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Second US Secretary of the Treasury (1795–1800), succeeding Hamilton and administering the Hamiltonian financial system through the XYZ Affair and Quasi-War; Governor of Connecticut (1817–27) who championed the state's landmark 1818 constitution disestablishing the church and extending voting rights.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Alexander Hamilton's establishment of the Hamiltonian financial system — the First Bank, federal debt assumption, and revenue administration — created the institutional framework that Wolcott inherited and administered as Treasury Secretary",
            "The Federalist-Republican political conflict of the 1790s — over financial policy, foreign relations with France, and constitutional interpretation — shaped the political environment in which his Treasury tenure operated",
            "Connecticut's constitutional reform movement — seeking to replace the colonial Fundamental Orders with a modern republican constitution — created the gubernatorial opportunity that produced his most lasting domestic legacy"
        ],
        "effects": [
            "His administration of the Treasury through the XYZ Affair and Quasi-War maintained American financial stability during diplomatic crisis with France — protecting the revenue system that funded the US government",
            "His championship of the Connecticut Constitution of 1818 eliminated the state's church establishment, extended voting rights by removing property qualifications, and modernized Connecticut's constitutional framework — a landmark in New England democratic development",
            "His transition from Federalism to the Republican Party reflected — and contributed to — the collapse of Federalism as a viable national party in the early 19th century",
            "His long tenure administering Hamilton's financial system helped normalize federal financial institutions — particularly the First Bank — through the transition between administrations"
        ],
        "relationships": [
            {"entity": "Alexander Hamilton", "relationship": "SUCCEEDED_AS_TREASURY_SECRETARY", "note": "Succeeded Hamilton as Secretary of the Treasury in 1795; administered and defended the Hamiltonian financial system"},
            {"entity": "First Bank of the United States", "relationship": "ADMINISTERED_AS_TREASURY_SECRETARY", "note": "As Treasury Secretary, administered the First Bank of the United States — the cornerstone of the Hamiltonian financial system"},
            {"entity": "Connecticut Constitution of 1818", "relationship": "CHAMPIONED_AS_GOVERNOR", "note": "As Governor of Connecticut, championed the 1818 constitution that disestablished the Congregational church and eliminated property voting qualifications"},
            {"entity": "Presidents Washington and Adams", "relationship": "SERVED_UNDER_AS_TREASURY_SECRETARY", "note": "Served as Treasury Secretary under both President Washington and President Adams (1795–1800)"},
            {"entity": "XYZ Affair and Quasi-War (1797–1800)", "relationship": "MANAGED_TREASURY_DURING", "note": "Managed the Treasury through the XYZ Affair diplomatic crisis and Quasi-War naval conflict with France"}
        ]
    }),

    # 4 — Rufus Choate
    ("rufus-choate", {
        "summary": (
            "Rufus Choate (1799–1859) was an American lawyer, orator, and Whig politician "
            "from Massachusetts who is regarded as one of the greatest lawyers in American "
            "history — a forensic genius who argued more than a thousand cases across "
            "virtually every branch of the law, was renowned for his extraordinary powers "
            "of jury persuasion, and who served as Daniel Webster's political heir and "
            "successor both in legal practice and in the Massachusetts Whig political "
            "tradition. His legal career, centered in Boston, established him as the "
            "preeminent American advocate of his generation.\n\n"
            "Choate's legal genius was especially celebrated in jury work — the art of "
            "persuasion before a lay tribunal. He was a pioneer of techniques designed "
            "to engage jury emotion and narrative sympathy alongside legal argument, "
            "bringing to American legal advocacy an understanding of rhetoric and "
            "psychology that went beyond the mere marshaling of facts and law. His "
            "closing arguments were regarded as masterpieces of forensic rhetoric, "
            "drawing on deep learning in classical oratory (he read Greek and Latin "
            "fluently), English literature, and history to craft arguments that "
            "combined legal analysis with literary power.\n\n"
            "Politically, Choate was a conservative Whig who believed in the Union, "
            "in the institutional stability of the common law, and in the Whig tradition "
            "of commercial nationalism that he inherited from Daniel Webster. He served "
            "briefly as a US Senator from Massachusetts (1841–1845), filling the seat "
            "vacated when Webster became Secretary of State — but the Senate was not "
            "his true arena, and he returned to the bar where his talents were more "
            "at home.\n\n"
            "His famous — if probably apocryphal — remark about the US Constitution "
            "being 'a glittering and sounding generality' illustrated the common law "
            "lawyer's preference for settled practice over abstract principle."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Regarded as one of the greatest American lawyers of the 19th century; argued over 1,000 cases; pioneered psychological jury techniques; Daniel Webster's political heir and successor in Massachusetts Whig politics; US Senator from Massachusetts (1841–1845).",
            "significanceCategory": "continental"
        },
        "causes": [
            "The American legal system's centrality of the jury trial — and the premium it placed on oral forensic advocacy — created the professional environment in which Choate's extraordinary oratorical gifts could flourish",
            "Daniel Webster's legal and political mentorship — and Choate's conscious positioning as Webster's successor in the Massachusetts Whig tradition — shaped his professional identity and political role",
            "The classical educational tradition that Choate received — with its deep grounding in Greek and Latin oratory — provided the rhetorical toolkit that distinguished him from contemporaries"
        ],
        "effects": [
            "His thousand-plus cases and legendary courtroom advocacy shaped the development of American legal practice — particularly in the techniques of jury persuasion and forensic rhetoric that he pioneered",
            "His Senate career (1841–1845) continued the Massachusetts Whig tradition of Webster — even if the Senate was not his natural arena — and influenced Massachusetts political development",
            "His conservative Whig political philosophy — emphasizing institutional continuity, common law stability, and commercial nationalism — contributed to the ideological tradition that resisted the radicalism of both abolitionism and secession",
            "His reputation attracted eminent young lawyers to study and observe his practice — contributing to the formation of a generation of American legal practitioners"
        ],
        "relationships": [
            {"entity": "Daniel Webster", "relationship": "POLITICAL_AND_LEGAL_HEIR_OF", "note": "Regarded as Daniel Webster's heir and successor in Massachusetts Whig politics and in the Boston legal practice — filled Webster's Senate seat when Webster became Secretary of State"},
            {"entity": "US Senate (Massachusetts)", "relationship": "SENATOR_FROM", "note": "Served as US Senator from Massachusetts (1841–1845) — filling the seat vacated when Webster became Secretary of State"},
            {"entity": "American jury trial tradition", "relationship": "TRANSFORMED_THROUGH_ADVOCACY", "note": "A pioneer of psychological jury persuasion techniques — arguing over 1,000 cases and transforming the craft of American forensic advocacy"},
            {"entity": "Massachusetts Whig Party", "relationship": "LEADING_FIGURE_OF", "note": "The leading figure of the Massachusetts conservative Whig tradition after Webster — combining legal eminence with political conservatism"},
            {"entity": "Classical rhetoric tradition (Greek and Latin)", "relationship": "PRACTITIONER_OF", "note": "Drew on deep classical education in Greek and Latin oratory to craft closing arguments that combined legal analysis with literary power"}
        ]
    }),

    # 5 — Rawlins Lowndes
    ("rawlins-lowndes", {
        "summary": (
            "Rawlins Lowndes (1721–1800) was a South Carolina lawyer, planter, and "
            "statesman who served as President (Governor) of South Carolina during the "
            "Revolutionary War (1778–1779) — the highest executive office in the state — "
            "and who became a significant Anti-Federalist voice opposing the ratification "
            "of the Constitution of 1787, arguing that the new federal system threatened "
            "South Carolina's interests, particularly its slaveholder economy and its "
            "political autonomy. Born in the Bahamas and educated in South Carolina, he "
            "was one of the leading figures of the South Carolina legal and planter "
            "establishment that dominated colonial and early republican politics.\n\n"
            "Lowndes had a paradoxical relationship with the American Revolution: he "
            "was elected to South Carolina's colonial legislature and became involved "
            "in the patriot cause, but he was deeply ambivalent about independence "
            "from Britain, opposing it until it became the decisive course. Once "
            "independence was taken, he committed to the patriot cause — including "
            "serving as President (Governor) during the critical period of British "
            "invasion of the South, when South Carolina faced the most severe military "
            "threat of any American state.\n\n"
            "His most historically significant role was his opposition to the "
            "Constitution of 1787 at the South Carolina ratifying convention. "
            "Lowndes argued that the Constitution's provisions on commerce (giving "
            "Congress power to regulate trade by simple majority) threatened southern "
            "economic interests, and that the Constitutional arrangement would "
            "progressively shift power to the more populous northern states at the "
            "expense of the south. These arguments — strikingly prescient about the "
            "sectional tensions that would eventually produce the Civil War — made him "
            "the most prominent South Carolinian voice of constitutional Anti-Federalism.\n\n"
            "South Carolina nonetheless ratified, and Lowndes's fears proved prophetic "
            "over the following decades."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "President (Governor) of South Carolina during the Revolutionary War (1778–79); the most prominent South Carolina Anti-Federalist at the 1788 ratifying convention — presciently arguing the Constitution would shift power northward at the expense of southern slave-state interests.",
            "significanceCategory": "regional"
        },
        "causes": [
            "South Carolina's position as one of the wealthiest colonies — dependent on slave labor and the plantation economy — created the specific economic and political concerns that shaped his Anti-Federalism",
            "The British invasion of the American South during the Revolutionary War — which placed South Carolina at the center of the southern theater — created the political crisis his gubernatorial tenure had to navigate",
            "The Constitutional Convention's commerce provisions — giving Congress simple-majority power to regulate trade — created the specific constitutional provision that Lowndes attacked as threatening southern economic interests"
        ],
        "effects": [
            "His Anti-Federalist arguments at the South Carolina ratifying convention — specifically about northern commercial domination — documented the sectional fears that would become the central conflict of 19th-century American politics",
            "His gubernatorial leadership during the Revolutionary War's southern phase provided political continuity for South Carolina at the moment of maximum military threat",
            "His legal and political career modeled the South Carolina planter-lawyer-statesman type that dominated southern American politics for generations — the integrated elite who combined plantation ownership with legal practice and political office",
            "His constitutional opposition — even in defeat — helped shape the Anti-Federalist tradition in South Carolina that would resurface in John C. Calhoun's nullification doctrine and states' rights arguments"
        ],
        "relationships": [
            {"entity": "South Carolina (Revolutionary War era)", "relationship": "PRESIDENT_OF", "note": "President (Governor) of South Carolina (1778–1779) during the Revolutionary War period of maximum British military threat to the state"},
            {"entity": "US Constitution ratification (1788)", "relationship": "OPPOSED_AT_SOUTH_CAROLINA_CONVENTION", "note": "Led Anti-Federalist opposition at the South Carolina ratifying convention — arguing the Constitution would shift power northward at southern expense"},
            {"entity": "South Carolina planter-lawyer class", "relationship": "MEMBER_AND_LEADER_OF", "note": "A leading member of the South Carolina planter-lawyer establishment that dominated colonial and early republican politics"},
            {"entity": "American Anti-Federalist movement", "relationship": "PROMINENT_VOICE_OF_IN_SOUTH", "note": "The most prominent South Carolinian Anti-Federalist — whose sectional arguments proved prescient about the coming North-South conflict"},
            {"entity": "American Revolutionary War (southern theater)", "relationship": "GOVERNOR_DURING", "note": "Served as Governor during the British invasion of the South — the most militarily dangerous period for South Carolina"}
        ]
    }),

    # 6 — Cristóbal Mendoza
    ("cristóbal-mendoza", {
        "summary": (
            "José Cristóbal Hurtado de Mendoza y Montilla (1772–1829), known as Cristóbal "
            "Mendoza, was a Venezuelan lawyer, politician, writer, and academic who served "
            "as the first official President of Venezuela (1811–1812) — the first head of "
            "state of Venezuela as an independent republic, presiding over the turbulent "
            "early months of Venezuelan sovereignty as the young republic faced internal "
            "division and Spanish counter-revolution. A Merida-born jurist educated in "
            "Caracas and Santo Domingo, he combined legal expertise with the republican "
            "ideals of the Enlightenment that drove the Latin American independence movements.\n\n"
            "Venezuela's declaration of independence on July 5, 1811 — the first among "
            "the Spanish American colonies — made it a pioneering act in the broader "
            "Latin American independence movement. Mendoza's presidency, however, "
            "coincided with the catastrophic Venezuelan earthquake of March 26, 1812 — "
            "which killed between 10,000 and 20,000 people, destroyed Caracas and "
            "other pro-independence cities, and was exploited by Royalist clergy as "
            "divine punishment for the republic's revolt against Spain. The earthquake "
            "severely undermined the republic's legitimacy and military capability, "
            "contributing directly to the First Republic's collapse when Simón Bolívar "
            "and Francisco de Miranda signed the Convention of La Victoria in July 1812.\n\n"
            "Mendoza was part of the generation of creole lawyers and intellectuals whose "
            "Enlightenment education — in Roman law, natural rights theory, and republican "
            "political philosophy — provided the ideological foundation for the independence "
            "movements. His academic and legal work before and after the First Republic "
            "reflected the intellectual culture of the Venezuelan Enlightenment.\n\n"
            "His legacy as the first Venezuelan president is historically significant even "
            "if his brief presidency was overwhelmed by natural disaster and Spanish "
            "military reconquest."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "First President of Venezuela (1811–1812); presided over the Venezuelan First Republic during the catastrophic 1812 earthquake and the Spanish Royalist reconquest; a leading creole lawyer-intellectual of the Venezuelan Enlightenment and independence generation.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Venezuelan independence movement — the first among the Spanish American colonies to declare independence in 1811 — created the new republic that Mendoza led as its first president",
            "The Enlightenment education of the Venezuelan creole elite — in Roman law, natural rights philosophy, and republican theory — provided the ideological foundation that made independence conceivable and gave leaders like Mendoza their republican political framework",
            "The Venezuelan earthquake of March 26, 1812 — which struck the pro-independence cities hardest — severely weakened the First Republic's military and political capacity, directly contributing to its collapse"
        ],
        "effects": [
            "His presidency established the institutional form of Venezuela's first independent republic — creating the presidency, the government structure, and the political processes of Venezuelan sovereignty",
            "The collapse of the First Republic during his presidency — due to the earthquake's devastating impact and the Spanish military reconquest — set the stage for Bolívar's subsequent campaigns to achieve Venezuelan independence",
            "His role as the first president of the first Spanish American colony to declare independence made him a pioneer figure in the broader Latin American independence movement",
            "His academic and legal work contributed to the intellectual tradition of the Venezuelan Enlightenment that prepared the ground for independence"
        ],
        "relationships": [
            {"entity": "Venezuelan Declaration of Independence (July 5, 1811)", "relationship": "FIRST_PRESIDENT_FOLLOWING", "note": "First President of Venezuela following the July 5, 1811 declaration of independence — the first among the Spanish American colonies"},
            {"entity": "Venezuelan earthquake of 1812", "relationship": "PRESIDENT_DURING", "note": "Was president when the devastating March 26, 1812 earthquake struck — killing tens of thousands and severely weakening the First Republic"},
            {"entity": "Simón Bolívar", "relationship": "CONTEMPORARY_AND_FELLOW_PATRIOT", "note": "A contemporary of Bolívar in the Venezuelan independence movement; Bolívar would continue the struggle for independence after the First Republic's collapse"},
            {"entity": "Francisco de Miranda", "relationship": "SERVED_UNDER_REPUBLIC_WITH", "note": "Part of the Venezuelan First Republic that included Francisco de Miranda — who signed the capitulation at La Victoria in July 1812 ending the First Republic"},
            {"entity": "Latin American independence movements", "relationship": "PIONEER_OF", "note": "Led the first Spanish American republic — making Venezuela's First Republic a pioneering act in the broader Latin American independence wave"}
        ]
    }),

    # 7 — François Hotman
    ("françois-hotman", {
        "summary": (
            "François Hotman (1524–1590) was a French Protestant lawyer, legal humanist, "
            "and political theorist who was one of the most significant legal scholars "
            "of the 16th century — a Huguenot refugee whose scholarly career was shaped "
            "by the French Wars of Religion, and whose political thought contributed "
            "foundational ideas to the development of European constitutionalism. "
            "He has been called 'one of the first modern revolutionaries' for his "
            "arguments that popular sovereignty, not royal absolutism, was the "
            "legitimate basis of French government.\n\n"
            "His masterwork, Francogallia (1573), was published the year after the "
            "St. Bartholomew's Day Massacre — in which thousands of Huguenots were "
            "killed by Catholic forces — and was explicitly a response to that catastrophe. "
            "Drawing on humanist historical scholarship, Hotman argued that the ancient "
            "Franks had possessed a constitutional assembly (the Champ de Mai) with "
            "supreme authority over French governance — and that the French monarchy's "
            "claim to absolute sovereignty was a historical usurpation of this popular "
            "constitutional government. Francogallia was thus both a work of legal history "
            "and a political manifesto for constitutional resistance to royal tyranny.\n\n"
            "As a legal humanist, Hotman contributed to the development of the mos "
            "gallicus — the French humanist approach to Roman law that sought to recover "
            "the historical context of the Justinian Corpus Juris rather than applying "
            "it as timeless positive law. His Anti-Tribonian (1567) was a radical attack "
            "on the dominance of Roman law in French legal education, arguing that French "
            "law should be reformed on the basis of French custom rather than the "
            "antiquated Roman compilation.\n\n"
            "As a Calvinist who corresponded with Calvin himself and fled France for "
            "the Reformed cities of Geneva, Basel, and Strasbourg multiple times, "
            "his life embodied the Huguenot intellectual diaspora."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "French Protestant legal humanist and constitutional theorist (1524–1590); author of Francogallia (1573) — a foundational text of European constitutionalism arguing for popular sovereignty against royal absolutism; correspondent of Calvin; pioneered the humanist approach to Roman law (mos gallicus).",
            "significanceCategory": "continental"
        },
        "causes": [
            "The French Wars of Religion — and particularly the St. Bartholomew's Day Massacre (1572) — provided the immediate political catastrophe that prompted the writing of Francogallia and made the political case for constitutional resistance to royal tyranny",
            "The Protestant Reformation's challenge to both ecclesiastical and royal authority created the intellectual and political context in which Hotman's constitutionalist arguments were embedded",
            "The legal humanist movement's application of philological and historical scholarship to Roman law created the scholarly methodology — the mos gallicus — that Hotman used to make historical arguments for constitutional government"
        ],
        "effects": [
            "Francogallia (1573) became a foundational text of European constitutionalism — contributing to the 'monarchomach' tradition of thought that argued rulers could be legitimately resisted when they violated the constitutional rights of the people",
            "His Anti-Tribonian (1567) contributed to the reform of French legal education away from mechanical application of Roman law toward historically informed French customary law",
            "His constitutionalist arguments influenced later theorists of popular sovereignty and resistance theory — contributing intellectual foundations to the English and French revolutionary traditions",
            "His Huguenot refugee career — moving between Geneva, Basel, Strasbourg, and France — embodied the Protestant intellectual diaspora that transmitted Reformed ideas across Europe"
        ],
        "relationships": [
            {"entity": "Francogallia (1573)", "relationship": "AUTHORED", "note": "Author of Francogallia — the foundational constitutionalist text arguing that French government derived from ancient popular constitutional assemblies rather than royal absolutism"},
            {"entity": "St. Bartholomew's Day Massacre (1572)", "relationship": "RESPONDED_TO_IN_SCHOLARSHIP", "note": "Francogallia was published the year after the Massacre — a direct scholarly and political response to the killing of thousands of Huguenots"},
            {"entity": "John Calvin", "relationship": "CORRESPONDENT_OF", "note": "A Calvinist who corresponded with Calvin himself and was embedded in the Reformed theological and political tradition"},
            {"entity": "French Wars of Religion (1562–1598)", "relationship": "INTELLECTUAL_FIGURE_OF", "note": "His career and his most important works were shaped by the French Wars of Religion — as a Huguenot repeatedly forced into exile"},
            {"entity": "Mos gallicus (French humanist legal method)", "relationship": "LEADING_THEORIST_OF", "note": "A leading practitioner and advocate of the mos gallicus — the humanist approach to Roman law that sought historical context rather than timeless positive law"}
        ]
    }),

    # 8 — José de Antequera y Castro
    ("josé-de-antequera-y-castro", {
        "summary": (
            "José de Antequera y Castro (1690–1731) was a Panamanian-born Spanish colonial "
            "lawyer, judge, and insurgent leader who became the central figure in the "
            "Paraguayan Comuneros Revolt (1721–1735) — one of the most significant "
            "anti-colonial uprisings in South American history before the late 18th-century "
            "independence movements, and a precursor to the broader Latin American "
            "resistance to Spanish colonial rule. A trained jurist who worked with "
            "the Real Audiencia of Charcas, he traveled to Paraguay to investigate "
            "corruption allegations against the colonial governor, deposed him, and "
            "then seized the governorship himself — claiming authority from the "
            "'will of the people' against the power of the Spanish colonial hierarchy.\n\n"
            "The Comuneros Revolt that Antequera led drew inspiration from the tradition "
            "of the Spanish comuneros — the 16th-century urban commons who had resisted "
            "the authority of the Habsburg crown — and articulated a doctrine of "
            "popular sovereignty that was remarkable for its period. His argument that "
            "the local community had the right to depose a corrupt governor and replace "
            "him with a figure chosen by popular will anticipated the constitutional "
            "arguments that would fuel the independence movements a century later.\n\n"
            "The Spanish colonial hierarchy — including the Jesuits, who had extensive "
            "mission territories in Paraguay and opposed Antequera — moved against him "
            "politically and militarily. He was captured, tried for treason against the "
            "Spanish crown, and executed in Lima in 1731. His execution did not end the "
            "Comuneros Revolt, which continued under other leaders until the mid-1730s "
            "and was eventually suppressed, but his popular sovereignty arguments left "
            "a lasting mark on Spanish colonial political thought.\n\n"
            "He remains a significant figure in Paraguayan national history — honored "
            "as a proto-independence fighter."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Panamanian-born Spanish colonial jurist who led the Paraguayan Comuneros Revolt (1721–1735) — one of the most significant anti-colonial uprisings in South American history; articulated popular sovereignty doctrine against colonial authority; executed for treason in Lima 1731; a proto-independence figure in Paraguayan history.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The corruption and misrule of the Spanish colonial governor of Paraguay — which brought Antequera as an investigative judge — created the immediate trigger for the conflict that became the Comuneros Revolt",
            "The tradition of the Spanish comuneros — the 16th-century commons who resisted Habsburg authority — provided the historical and conceptual vocabulary that Antequera drew upon to justify popular resistance to colonial governors",
            "The Jesuit missions' political and economic power in Paraguay — which the Comuneros challenged — created the powerful institutional opposition that helped the Spanish colonial hierarchy suppress the revolt"
        ],
        "effects": [
            "The Paraguayan Comuneros Revolt he led became one of the most significant anti-colonial uprisings in South American history — a precursor to the independence movements that would succeed a century later",
            "His articulation of popular sovereignty against colonial authority — that the local community had the right to depose a corrupt governor — contributed to the political thought that would fuel Latin American independence",
            "His execution in Lima (1731) became a symbol of colonial brutality against popular resistance — enhancing rather than diminishing his legacy as a proto-independence figure",
            "The Comuneros Revolt he initiated continued for years after his death — his popular sovereignty arguments providing the ideological fuel for continued resistance by subsequent leaders"
        ],
        "relationships": [
            {"entity": "Paraguayan Comuneros Revolt (1721–1735)", "relationship": "LED", "note": "Led the Paraguayan Comuneros Revolt — one of the most significant anti-colonial uprisings in South American history before the independence era"},
            {"entity": "Real Audiencia of Charcas (Spanish colonial court)", "relationship": "AGENT_OF", "note": "Originally traveled to Paraguay as a judge of the Real Audiencia of Charcas to investigate colonial governor corruption"},
            {"entity": "Jesuits in Paraguay (Reductions)", "relationship": "OPPOSED_BY", "note": "The Jesuit missions' political power in Paraguay made them opponents of the Comuneros Revolt — they supported the Spanish colonial hierarchy against Antequera"},
            {"entity": "Spanish colonial system in South America", "relationship": "CHALLENGED", "note": "His popular sovereignty arguments challenged the legitimacy of Spanish colonial governance — anticipating independence movement ideologies"},
            {"entity": "Latin American independence movements", "relationship": "PRECURSOR_TO", "note": "A proto-independence figure whose Comuneros Revolt and popular sovereignty arguments were precursors to the independence movements that followed a century later"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 26)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
