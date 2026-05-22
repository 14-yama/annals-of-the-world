#!/usr/bin/env python3
"""
Batch 01 — 8 entities (Class 311): British Parliament, Roman Senate,
Athenian Assembly, Althing, Continental Congress, European Commission,
European Council, Council of the European Union
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/311-Class-311"
FILE_PREFIX = "311"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()


def enrich_entity(slug, data):
    fname = os.path.join(FOLDER, f"{FILE_PREFIX}{slug}.json")
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
    print(f"  ✓ {entity['name']} — sum={slen}c c={len(det.get('causes', []))} e={len(det.get('effects', []))}")


ENTITIES = [

    ("british-parliament", {
        "summary": (
            "The Parliament of the United Kingdom, seated at Westminster in London, is one of the oldest and most influential legislatures in the world. Tracing its origins to the Magna Carta (1215) and Simon de Montfort's Parliament of 1265, it evolved over centuries from a royal advisory council into the supreme legislative authority of the state. The Glorious Revolution of 1688 and the Bill of Rights (1689) definitively established parliamentary sovereignty — the principle that Parliament, not the Crown, held ultimate legal authority.\n\n"
            "Parliament is bicameral: the elected House of Commons controls legislation and finance, while the appointed House of Lords acts as a revising chamber. The Reform Acts (1832, 1867, 1884) progressively extended the franchise; the Parliament Acts (1911, 1949) stripped the Lords of their legislative veto. By the 20th century Parliament had abolished the slave trade (1807), established the NHS and welfare state (1945–51), and managed two world wars — making it the arena where Britain's defining national decisions have been contested and resolved.\n\n"
            "The Westminster Model — responsible government, collective cabinet accountability, the loyal opposition — has been adopted by over 50 former British colonies, making the British Parliament the most widely replicated constitutional template in history."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "The world's most emulated parliament; established parliamentary sovereignty over the Crown (1689); abolished the slave trade (1807); created the NHS (1946); its Westminster Model adopted by 50+ nations.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Magna Carta (1215) established that the Crown could not levy taxes without baronial consent — the foundational principle from which Parliament evolved",
            "Simon de Montfort's Parliament (1265) first included elected knights and burgesses alongside nobles and clergy — establishing representative government for the commons",
            "The Glorious Revolution (1688) and Bill of Rights (1689) permanently established parliamentary sovereignty — making Parliament supreme over the Crown in legislation and taxation"
        ],
        "effects": [
            "The Westminster Model of parliamentary government — responsible ministry, collective cabinet accountability, the loyal opposition — was adopted by 50+ former British colonies and became the world's most widely replicated constitutional framework",
            "The Abolition of the Slave Trade Act (1807) and Slavery Abolition Act (1833) — both passed by Parliament — ended British participation in and then the institution of chattel slavery across the Empire",
            "The Parliament Acts (1911, 1949) transformed the House of Lords from co-equal chamber to revising body, completing the transition from aristocratic to democratic government",
            "The post-WWII Parliament (1945–51) created the NHS, nationalised key industries, and established the welfare state — a model of social democracy that influenced governance across Western Europe"
        ],
        "relationships": [
            {"entity": "Magna Carta (1215)", "relationship": "EVOLVED_FROM", "note": "Parliament evolved from the principle in Magna Carta that the Crown required consent to levy taxes"},
            {"entity": "Bill of Rights (1689)", "relationship": "SOVEREIGNTY_ESTABLISHED_BY", "note": "The Bill of Rights (1689) established parliamentary sovereignty following the Glorious Revolution"},
            {"entity": "Westminster Model", "relationship": "ORIGINATED", "note": "The Westminster Model of parliamentary government originated in British parliamentary conventions and was adopted by 50+ nations"},
            {"entity": "Abolition of the Slave Trade Act (1807)", "relationship": "PASSED", "note": "Parliament passed the Abolition of the Slave Trade Act — ending British participation in the transatlantic slave trade"},
            {"entity": "National Health Service", "relationship": "CREATED_VIA_LEGISLATION", "note": "Parliament created the NHS through the National Health Service Act (1946) — establishing universal free healthcare"}
        ],
    }),

    ("roman-senate", {
        "summary": (
            "The Roman Senate (Senatus Romanus) was the governing council of ancient Rome from its legendary origins under Romulus (c. 753 BCE) through the fall of the Western Empire (476 CE). During the Republic (509–27 BCE) it was the dominant institution of Roman governance — controlling state finances, foreign policy, provincial administration, and the assignment of military commands. Its 300–600 members were former magistrates who served for life, giving the Senate the institutional memory and continuity that annual elected magistrates could not provide.\n\n"
            "The Senate's authority rested on its control of the treasury (aerarium), its power to assign consular provinces, and its ability to issue senatus consulta (decrees) that directed policy without formal legislative status. After Cannae (216 BCE), where Rome lost 70,000 soldiers to Hannibal in a single day, the Senate's refusal to negotiate with the Carthaginian general became a founding myth of Roman republican virtue. The Senate's decline began with the Gracchi (133–121 BCE) and culminated when Augustus (27 BCE) reduced it to an honorific chamber while retaining its forms.\n\n"
            "The Senate's institutional legacy is profound: its deliberative procedures, its concept of collective governance by senior magistrates, and its Latin vocabulary of public life directly shaped the medieval Papal Curia, Renaissance republics, and the explicitly named United States Senate."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Governing council of Rome for nearly a millennium; controlled the finances and provinces of the Republic; its post-Cannae resilience became a founding myth; directly inspired the US Senate and modern republican upper chambers.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The expulsion of the kings (509 BCE) transferred supreme authority to the Senate — which became the permanent institutional continuity of Rome across the annual rotation of elected magistrates",
            "Rome's military expansion across Italy (4th–3rd centuries BCE) generated tribute and territory requiring central administration — cementing Senate control of finances and provincial assignment",
            "The Punic Wars (264–146 BCE) demonstrated the Senate's strategic capacity: its resilience after Cannae (216 BCE) — refusing to negotiate despite catastrophic losses — proved that collective institutional authority could outlast individual military disaster"
        ],
        "effects": [
            "The Senate's institutional form — a deliberative body of senior magistrates controlling public finances — became the template for upper houses in Western republics, including the US Senate (explicitly named after the Roman model)",
            "The Senate's failure to manage the crises of 133–27 BCE — the Gracchi, Marius, Sulla, Caesar — became a case study in republican institutional decay, shaping political theory from Polybius and Cicero to Machiavelli and Madison",
            "Rome's senatorial class produced Latin literature — Cicero, Sallust, Livy, Tacitus — that defined Western historical and political writing for two millennia",
            "The Senate's survival as a formal institution under the Principate established the model of ruling through traditional institutions while emptying them of real power — replicated by authoritarian regimes throughout history"
        ],
        "relationships": [
            {"entity": "Roman Republic", "relationship": "GOVERNING_COUNCIL_OF", "note": "The Senate was the dominant governing institution of the Roman Republic (509–27 BCE)"},
            {"entity": "Julius Caesar", "relationship": "ASSASSINATED_MEMBER_OF", "note": "Conservative senators (led by Brutus and Cassius) assassinated Caesar on the Ides of March (44 BCE) — triggering the civil wars that ended the Republic"},
            {"entity": "Augustus", "relationship": "REDUCED_TO_HONORIFIC_BY", "note": "Augustus preserved the Senate's forms while transferring real power to himself — establishing the Principate"},
            {"entity": "United States Senate", "relationship": "NAMESAKE_MODEL_FOR", "note": "The US Senate was explicitly named and modelled after the Roman Senate — the Founders' primary classical reference for republican governance"},
            {"entity": "Hannibal Barca", "relationship": "REFUSED_TO_NEGOTIATE_WITH", "note": "After Cannae (216 BCE) the Senate famously refused to negotiate — a decision that became the founding myth of Roman republican virtue"}
        ],
    }),

    ("athenian-assembly", {
        "summary": (
            "The Athenian Assembly (Ekklesia) was the principal democratic institution of classical Athens, open to all adult male citizens and holding sovereign authority over legislation, war, foreign policy, and elections. Its foundations were laid by Solon (594 BCE) and radically transformed by Cleisthenes (508 BCE), who reorganised the citizen body into ten artificial tribes cutting across regional loyalties — creating a genuinely citywide demos capable of collective deliberation. At its peak under Pericles (461–429 BCE), the Assembly met 40 times per year on the Pnyx hill, with quorums of 6,000 citizens required for major decisions.\n\n"
            "The Assembly institutionalised the principle that the demos (people) was sovereign — a radical departure from the aristocratic, monarchic, and priestly governance models of the ancient world. It voted for the Periclean building programme (447–432 BCE) that produced the Parthenon, authorised the Sicilian Expedition (415 BCE) that proved catastrophic, and used ostracism to exile dangerous citizens — pioneering democratic mechanisms for managing political risk.\n\n"
            "The Assembly was the primary subject of analysis for Plato, Aristotle, and Thucydides — making it the foundational case study of democratic political philosophy. Every subsequent democratic institution, from the Roman assemblies to the French Assemblée Nationale to the UN General Assembly, traces its conceptual lineage to the Athenian model of citizen sovereignty."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "First fully institutionalised democratic assembly in recorded history; established citizen sovereignty (demos); directly inspired Aristotle, Plato, and all democratic political theory; the conceptual ancestor of every modern democratic legislature.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Solon's reforms (594 BCE) opened the Assembly to all free Athenian men regardless of birth, replacing aristocratic dominance with broader citizen participation — the foundational step toward democratic deliberation",
            "Cleisthenes' reforms (508 BCE) reorganised citizens into ten artificial tribes cutting across regional loyalties — creating a genuinely citywide demos capable of collective democratic decision-making",
            "The Persian Wars (490–479 BCE) and the naval empire empowered lower-class Athenians (thetes) who rowed the fleet — giving them the military leverage to demand and exercise full democratic participation"
        ],
        "effects": [
            "The principle of popular sovereignty — that the demos rather than kings, priests, or aristocrats held ultimate authority — was first institutionalised in the Athenian Assembly, making it the conceptual foundation of all subsequent democratic theory",
            "The Assembly's catastrophic vote for the Sicilian Expedition (415–413 BCE) — resulting in total military disaster — became the foundational case study for warnings about demagogy and popular irrationality, directly shaping Plato's critique of democracy",
            "The Periclean building programme (447–432 BCE) — voted by the Assembly — produced the Parthenon and Athenian monuments that defined Western aesthetic ideals for two millennia",
            "The ostracism procedure pioneered by the Assembly — democratic exile of dangerous citizens — became a template for managing political risk in republics, from Roman proscriptions to modern recall elections"
        ],
        "relationships": [
            {"entity": "Cleisthenes", "relationship": "REFORMED_AND_EMPOWERED_BY", "note": "Cleisthenes' 508 BCE reforms transformed the Assembly from a ceremonial body into the sovereign democratic institution of Athens"},
            {"entity": "Pericles", "relationship": "DIRECTED_UNDER_LEADERSHIP_OF", "note": "Under Pericles (461–429 BCE) the Assembly reached its democratic apex — building the Parthenon and directing the Athenian Empire"},
            {"entity": "Sicilian Expedition (415–413 BCE)", "relationship": "VOTED_FOR", "note": "The Assembly voted for the Sicilian Expedition — a catastrophic overextension that became the canonical case study of democratic failure"},
            {"entity": "Aristotle", "relationship": "ANALYSED_IN_POLITICS_BY", "note": "Aristotle's Politics analysed the Athenian Assembly as the primary example of pure democracy — establishing political science vocabulary used ever since"},
            {"entity": "Parthenon", "relationship": "COMMISSIONED_CONSTRUCTION_OF", "note": "The Assembly voted to fund the Periclean building programme that produced the Parthenon (447–432 BCE)"}
        ],
    }),

    ("althing-the-worlds-oldest-surviving-parl", {
        "summary": (
            "The Althing (Alþingi) of Iceland, founded in 930 CE, is the world's oldest surviving parliament, predating the English Parliament by over three centuries. Established by Norse settlers at Þingvellir — a dramatic rift valley where the Eurasian and North American tectonic plates diverge — it served as the supreme legislative and judicial assembly of the Icelandic Commonwealth (930–1262 CE). This was a stateless society governed entirely by law, deliberation, and social pressure, with no executive monarch or standing army.\n\n"
            "The Althing convened for two weeks each summer, bringing together the 36–39 chieftains (goðar) and their followers to legislate, adjudicate disputes, and conduct Iceland's social business. The lawspeaker (lögsögumaðr) — elected for three-year terms — recited the entire law code from memory each session: a living institutional memory preserving legal continuity before widespread literacy. The conversion of Iceland to Christianity (1000 CE) was decided by the Althing through pragmatic compromise — one of the most peaceful religious transitions in medieval Europe.\n\n"
            "Dissolved when Iceland submitted to Norwegian rule (1262) and suspended under Danish rule (1800–1845), the Althing was revived in 1845 and became the parliament of the independent Republic of Iceland (1944). Its 1,094-year unbroken symbolic continuity makes it the world's foremost institutional symbol of parliamentary longevity."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "World's oldest surviving parliament (founded 930 CE); governed the Icelandic Commonwealth as a stateless legal order; decided Iceland's conversion to Christianity (1000 CE) peacefully; its symbolic continuity to the present makes it the world's foremost example of parliamentary longevity.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Norse settlement of Iceland (874–930 CE) created a dispersed farming society with no king or central authority — making a periodic assembly of all chieftains the only viable mechanism for collective governance and dispute resolution",
            "The goðar institution — hereditary chieftain-priests whose followers voluntarily attached themselves — created the social structure that the Althing formalised into a functioning legal order without an executive branch",
            "The Norwegian Thing tradition of periodic assemblies for law-speaking and dispute resolution provided the institutional model that Icelandic settlers radically developed into the fully legislative Althing"
        ],
        "effects": [
            "The Althing's successful governance of Iceland as a stateless legal order (930–1262) became the primary historical example cited by political theorists arguing that ordered society is possible without a state — a recurring reference from 19th-century anarchism to modern libertarian political philosophy",
            "The peaceful conversion of Iceland to Christianity (1000 CE) — decided by the Althing through pragmatic compromise — became a celebrated example of democratic religious decision-making in contrast to the forced conversions of the Carolingian period",
            "The Althing's revival (1845) and its role in Icelandic independence (1944) established a template for post-colonial restoration of indigenous institutions, influencing constitutional continuity debates in decolonising nations",
            "The 2010–2013 crowdsourced constitutional process commissioned by the Althing — where citizens collaboratively drafted a new constitution via social media — became a globally watched experiment in participatory constitutional design"
        ],
        "relationships": [
            {"entity": "Icelandic Commonwealth (930–1262)", "relationship": "GOVERNING_BODY_OF", "note": "The Althing was the supreme legislative and judicial institution of the Icelandic Commonwealth — a stateless society governed by law and deliberation"},
            {"entity": "Þingvellir", "relationship": "MET_AT", "note": "The Althing convened at Þingvellir — now a UNESCO World Heritage Site and Iceland's national park"},
            {"entity": "Conversion of Iceland to Christianity (1000 CE)", "relationship": "DECIDED_BY", "note": "The Althing's pragmatic 1000 CE decision to adopt Christianity was one of the most peaceful religious transitions in medieval Europe"},
            {"entity": "Republic of Iceland", "relationship": "PARLIAMENT_OF", "note": "The Althing became the parliament of the modern Republic of Iceland (1944), providing symbolic continuity from the Viking Age"},
            {"entity": "Norwegian Thing tradition", "relationship": "EVOLVED_FROM", "note": "The Althing evolved from the Norwegian Thing tradition of periodic assemblies for law-speaking and dispute resolution"}
        ],
    }),

    ("continental-congress", {
        "summary": (
            "The Continental Congress (1774–1789) was the governing body of the thirteen American colonies and subsequently of the United States during the American Revolution and the Confederation period. The First Continental Congress (September–October 1774) coordinated colonial resistance to British taxation; the Second Continental Congress (1775–1789) served as the de facto national government throughout the Revolutionary War — raising the Continental Army, appointing George Washington as its commander, managing diplomacy with France, and issuing the currency that financed the war.\n\n"
            "Its two most consequential acts were the Declaration of Independence (July 4, 1776) — which severed the colonies' allegiance to Britain and proclaimed universal natural rights — and the Articles of Confederation (1777/1781), which created the United States' first constitutional framework. The Articles' structural weaknesses (Congress could not tax, regulate commerce, or compel the states) eventually drove the Constitutional Convention of 1787 and the replacement of the Confederation Congress with the modern federal legislature.\n\n"
            "The Declaration of Independence became one of the most reproduced political documents in history — a template for decolonisation movements across two centuries. Jefferson's proclamation that 'all men are created equal' and endowed with 'unalienable rights' to 'life, liberty, and the pursuit of happiness' became the universal vocabulary of democratic aspiration."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Governing body of the American Revolution; issued the Declaration of Independence (1776); appointed Washington commander-in-chief; the Articles' weaknesses produced the US Constitution; the Declaration became a global template for independence movements across two centuries.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "British taxation without colonial representation — the Stamp Act (1765), Townshend Acts (1767), and Intolerable Acts (1774) — created the political crisis that made an intercolonial coordinating body necessary",
            "The colonial tradition of provincial assemblies — each colony had experience of self-governance — provided the institutional experience and personnel for the Congress's deliberative procedures",
            "The Intolerable Acts (1774), which closed Boston Harbor and revoked Massachusetts's charter, unified the thirteen colonies behind a common grievance and provided the immediate catalyst for the First Continental Congress"
        ],
        "effects": [
            "The Declaration of Independence (July 4, 1776) proclaimed the universal right to self-governance and became the most influential document of the democratic revolution — directly inspiring the French Declaration of the Rights of Man (1789), Latin American independence declarations, and the UN Declaration of Human Rights (1948)",
            "The Congress's appointment of Washington as commander-in-chief established the precedent of civilian control of the military — a principle constitutionalised in the US Constitution and adopted by democracies worldwide",
            "The failure of the Articles of Confederation directly produced the Constitutional Convention of 1787 and the world's oldest surviving written national constitution",
            "The Continental Congress's success validated the revolutionary principle that colonial subjects could legitimately establish their own governments — inspiring independence movements in Haiti (1804), Spanish America (1810s–1820s), and the global decolonisation movements of the 20th century"
        ],
        "relationships": [
            {"entity": "Declaration of Independence (1776)", "relationship": "ADOPTED", "note": "The Second Continental Congress adopted the Declaration of Independence on July 4, 1776 — the founding document of the United States"},
            {"entity": "George Washington", "relationship": "APPOINTED_AS_COMMANDER", "note": "The Congress appointed Washington as commander-in-chief of the Continental Army in June 1775 — establishing civilian control of the military"},
            {"entity": "Articles of Confederation", "relationship": "DRAFTED_AND_OPERATED_UNDER", "note": "The Congress drafted the Articles of Confederation (1777) and governed under them — exposing structural weaknesses that produced the US Constitution"},
            {"entity": "Constitutional Convention (1787)", "relationship": "REPLACED_BY", "note": "The Constitutional Convention of 1787 replaced the Confederation Congress with the modern federal legislature"},
            {"entity": "French Revolution", "relationship": "DECLARATION_INSPIRED", "note": "The Declaration of Independence (1776) directly inspired the French Declaration of the Rights of Man (1789)"}
        ],
    }),

    ("european-commission", {
        "summary": (
            "The European Commission is the executive body and sole initiator of legislation for the European Union, established under the Treaty of Rome (1957). Its 27 Commissioners — one per member state — are appointed by the European Council and approved by the European Parliament for five-year terms, with the President of the Commission serving as the EU's chief executive. Its unique constitutional power is the exclusive right of legislative initiative: no EU law can proceed without a Commission proposal.\n\n"
            "The Commission manages the €185B EU budget, negotiates international trade agreements on behalf of all member states, enforces competition law (including €8.25B in fines against Google, 2017–2019), and acts as 'guardian of the treaties' — taking member states to the Court of Justice for violations. Its digital regulation agenda — GDPR (2018), Digital Markets Act, Digital Services Act — has made the EU the world's primary regulator of technology platforms, a phenomenon legal scholars call the 'Brussels Effect': EU rules becoming de facto global standards.\n\n"
            "The Commission's institutional design reflects the post-WWII logic of European integration: embedding a supranational executive with independent enforcement powers was intended to make war between European nations structurally impossible by creating shared governance over the economic resources that had fuelled two world wars."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Executive body and sole legislative initiator of the EU; enforces competition law against major corporations; proposed GDPR and the European Green Deal; the 'Brussels Effect' makes EU rules de facto global standards — the world's most powerful supranational executive.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Schuman Declaration (1950) and the Treaty of Paris (1951) establishing the ECSC created the institutional prototype — a supranational body with independent authority over coal and steel — that became the Commission",
            "Post-WWII consensus that national sovereignty had enabled two devastating world wars led the six founding nations to accept a supranational executive with genuine enforcement powers — the novel institutional innovation the Commission represents",
            "The Treaty of Rome (1957) formalised the Commission's exclusive right of legislative initiative — ensuring EU legislation would be driven by a body representing the common European interest rather than national governments"
        ],
        "effects": [
            "The Commission's competition enforcement — including €8.25B in fines against Google (2017–2019) and €13B demanded from Apple (2016) — established European antitrust standards as effective constraints on global technology companies",
            "The GDPR (2018) — proposed by the Commission — became the world's most influential privacy law, with companies worldwide adapting data practices to EU standards rather than those of their home jurisdictions",
            "The European Green Deal (2019) set a net-zero 2050 target for the EU — the world's most ambitious binding climate framework, influencing the US Inflation Reduction Act and climate pledges globally",
            "The Commission's single market enforcement has created the world's largest integrated market of 450 million people — the economic foundation for Europe's post-war prosperity"
        ],
        "relationships": [
            {"entity": "Treaty of Rome (1957)", "relationship": "ESTABLISHED_BY", "note": "The Treaty of Rome formally established the European Commission as the EU's executive and legislative initiator"},
            {"entity": "GDPR (2018)", "relationship": "PROPOSED", "note": "The Commission proposed GDPR — now the world's most influential privacy law and a global template for digital rights"},
            {"entity": "European Green Deal", "relationship": "INITIATED", "note": "The Commission launched the European Green Deal (2019) — the EU's comprehensive net-zero climate framework"},
            {"entity": "Google", "relationship": "FINED_IN_COMPETITION_ENFORCEMENT", "note": "The Commission fined Google €8.25B across three landmark competition cases (2017–2019)"},
            {"entity": "European Parliament", "relationship": "SUBJECT_TO_APPROVAL_AND_ACCOUNTABILITY_TO", "note": "The Commission must be approved by and is accountable to the European Parliament"}
        ],
    }),

    ("european-council", {
        "summary": (
            "The European Council is the EU institution that defines the union's overall political direction and priorities, consisting of the heads of state or government of all 27 member states meeting under a permanent President. Established informally in 1974 and gaining legal status as an EU institution under the Lisbon Treaty (2007), it sets the strategic agenda — enlargement, treaty changes, multi-year budget frameworks, crisis responses — but does not legislate. Decisions are typically taken by consensus, giving each leader a de facto veto over the EU's strategic direction.\n\n"
            "In practice, the European Council has been the decisive arena for the EU's most consequential decisions: the eurozone crisis bailout packages (2010–2012), the migration crisis framework (2015), the €750B NextGenerationEU COVID recovery fund (2020), and the united response to Russia's invasion of Ukraine (2022). The 2020 agreement on joint EU debt issuance — the NextGenerationEU fund — represented the most significant expansion of EU financial solidarity since the euro itself.\n\n"
            "The European Council embodies the intergovernmental dimension of EU governance, where national heads of government retain ultimate authority. Its relationship with the supranational Commission reflects the fundamental tension between national sovereignty and supranational authority that has defined European integration since 1957."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Supreme strategic decision-making body of 27 EU heads of state; agreed eurozone bailouts (2010–12), €750B NextGenerationEU (2020), and unified Ukraine response (2022); the intergovernmental counterweight to the supranational Commission.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The oil crisis (1973–74) and breakdown of the Bretton Woods system created strategic challenges requiring coordination at head-of-government level — the summit meetings that became the European Council",
            "The inadequacy of the Council of Ministers for strategic decision-making led French President Giscard d'Estaing to propose regular summits of heads of state, formalised at the 1974 Paris Summit",
            "The Maastricht (1992) and Lisbon (2007) treaties progressively formalised the European Council, creating a permanent presidency and granting it treaty-based status"
        ],
        "effects": [
            "The European Council's 2010–2012 bailout packages — agreed under intense pressure among 27 heads of government — determined the austerity terms for Greece, Ireland, Portugal, Spain, and Cyprus, directly affecting tens of millions of citizens",
            "The 2020 agreement on the €750B NextGenerationEU fund — the EU's first-ever joint debt issuance — was a historic step toward fiscal federalism, representing the most significant expansion of EU solidarity since the euro",
            "The European Council's united response to Russia's invasion of Ukraine (2022) — coordinated sanctions, weapons decisions, Ukrainian EU candidacy — demonstrated the institution's capacity to coordinate geopolitical responses at crisis speed",
            "The European Council's enlargement decisions — admitting 16 new members since 1973 — transformed the EU from a Western European club into a pan-European institution of 450 million people"
        ],
        "relationships": [
            {"entity": "Lisbon Treaty (2007)", "relationship": "GIVEN_FORMAL_STATUS_BY", "note": "The Lisbon Treaty gave the European Council formal treaty-based status and created the permanent presidency"},
            {"entity": "European Commission", "relationship": "SETS_STRATEGIC_AGENDA_FOR", "note": "The European Council sets political priorities that the Commission implements through legislation"},
            {"entity": "Eurozone crisis (2010–2012)", "relationship": "MANAGED_RESPONSE_TO", "note": "The European Council agreed the ESM and bailout terms for five member states during the sovereign debt crisis"},
            {"entity": "NextGenerationEU", "relationship": "AGREED", "note": "The European Council agreed the €750B NextGenerationEU fund (July 2020) — the EU's first joint debt issuance"},
            {"entity": "Ukraine", "relationship": "GRANTED_EU_CANDIDATE_STATUS_TO", "note": "The European Council granted Ukraine EU candidate status in June 2022 — the fastest ever candidacy decision"}
        ],
    }),

    ("council-of-the-european-union", {
        "summary": (
            "The Council of the European Union (the 'Council of Ministers') is one of the two principal legislative bodies of the EU, representing the governments of all 27 member states. It shares legislative power with the European Parliament and holds sole authority over EU foreign and security policy, taxation, and treaty changes. The Council meets in ten configurations — each bringing together the relevant national ministers — making it a uniquely fluid legislature whose composition shifts depending on subject matter: ECOFIN for finance, FAC for foreign affairs, AGRIFISH for agriculture.\n\n"
            "Voting rules are the Council's most consequential feature: most decisions require a qualified majority (55% of states representing 65% of population), but sensitive areas require unanimity — giving each member state a veto. This QMV/unanimity boundary has been the central battleground of EU institutional reform for decades. The Council Presidency rotates every six months, allowing even the smallest member states to set the EU agenda.\n\n"
            "The Council's 150+ working parties — where national officials negotiate the technical details of legislation before ministers meet — mean that approximately 70–80% of EU law is agreed at official rather than ministerial level, creating powerful transnational networks of national bureaucrats that form the hidden architecture of European governance."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "One of two EU co-legislators representing 27 national governments; controls EU foreign policy via unanimity; its QMV/unanimity boundary defines the central tension in EU institutional design; its 150+ working parties are where most EU legislation is actually negotiated.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Treaty of Rome (1957) established the Council of Ministers as the EEC's primary decision-making body — reflecting the founding vision that national governments should hold primary legislative authority",
            "The Empty Chair Crisis (1965–66) — France's boycott of Council meetings under de Gaulle — produced the Luxembourg Compromise, which established an informal unanimity convention that shaped Council voting culture for decades",
            "The Single European Act (1986) extended qualified majority voting to single market legislation — breaking the unanimity paralysis that had blocked EU legislation through the 1970s and accelerating the completion of the internal market"
        ],
        "effects": [
            "The Council's QMV system has produced the world's largest integrated regulatory framework — 27 nations governing a €16T single market under a shared legal order",
            "The unanimity requirement for foreign policy has limited the EU's geopolitical coherence — fuelling decades of debate about QMV extension that continue through the Conference on the Future of Europe",
            "The rotating six-month presidency allows even the smallest member states (Malta, Luxembourg, Cyprus) to set the EU agenda — a uniquely egalitarian model of international governance",
            "The Council working party system has created a transnational bureaucratic network of 5,000+ national officials who regularly collaborate in Brussels, forming institutional relationships that transcend national boundaries"
        ],
        "relationships": [
            {"entity": "European Parliament", "relationship": "CO-LEGISLATES_WITH", "note": "The Council co-legislates with the European Parliament — the two chambers of the world's only supranational legislature"},
            {"entity": "European Commission", "relationship": "RECEIVES_LEGISLATIVE_PROPOSALS_FROM", "note": "The Council can only act on legislative proposals from the Commission — the EU's system of exclusive executive initiative"},
            {"entity": "Luxembourg Compromise (1966)", "relationship": "VOTING_CULTURE_SHAPED_BY", "note": "The 1966 Luxembourg Compromise established the informal unanimity convention that paralysed Council decision-making for two decades"},
            {"entity": "Single European Act (1986)", "relationship": "REFORMED_BY", "note": "The Single European Act extended QMV to single market legislation — accelerating European integration"},
            {"entity": "COREPER", "relationship": "PREPARED_BY", "note": "The Committee of Permanent Representatives prepares all Council meetings — where the majority of EU legislative compromises are actually reached"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 01 — {len(ENTITIES)} entities (Class 311: Major Legislative Bodies)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
