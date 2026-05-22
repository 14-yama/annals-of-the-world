#!/usr/bin/env python3
"""
Batch 03 — 8 entities (Class 311): Guardian Council, Schmalkaldic League,
Rump Parliament, Loya Jirga, Rajya Sabha, Bundesrat,
Senate (US), National Assembly (French)
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

    ("guardian-council", {
        "summary": (
            "The Guardian Council (Shora-ye Negahban) is a twelve-member constitutional body of the Islamic Republic of Iran that serves as a combined constitutional court, clerical supervisory authority, and electoral vetting body. Established by the Constitution of 1979, it consists of six Islamic jurists appointed by the Supreme Leader and six civil lawyers approved by the Parliament (Majlis). Its powers are uniquely broad: it reviews all legislation for conformity with Islamic law and the Constitution, and holds the authority to disqualify candidates for the Parliament, Presidency, and Assembly of Experts.\n\n"
            "The Council's candidate vetting power — used to disqualify thousands of reform-minded candidates in elections since 1992 — has been the primary mechanism through which Iran's Supreme Leader has maintained the dominance of hardline conservative factions despite popular demand for reform. In the 2004 parliamentary elections, the Council disqualified over 2,000 candidates including 80 sitting MPs; in the 2021 presidential election it disqualified all reformist candidates, producing a hardliner field.\n\n"
            "The Guardian Council represents the 'velayat-e faqih' (guardianship of the Islamic jurist) principle — the constitutional doctrine that Khomeini used to create a clerical supervisory layer over all democratic institutions. Its existence makes Iran's political system a hybrid of republican elections and clerical veto — a novel constitutional form with no direct precedent in Islamic jurisprudence or comparative constitutional law."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Constitutional guardian and electoral vetter of Iran; reviews all legislation for Islamic conformity; disqualifies thousands of candidates per election cycle; the primary mechanism for clerical control over Iran's nominally democratic institutions; embodies Khomeini's velayat-e faqih principle.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Ayatollah Khomeini's doctrine of velayat-e faqih (guardianship of the Islamic jurist) — the theological justification for clerical authority over the state — required an institutional mechanism to enforce Islamic compliance on all legislation and officials",
            "The Iranian Revolution (1979) created a hybrid constitutional system combining republican elections with clerical supervision — requiring a body like the Guardian Council to manage the inherent tension between democratic and theocratic legitimacy",
            "The drafting of the 1979 Constitution by Khomeini's allies gave the Council its broad powers precisely to prevent the liberal and leftist factions who had also participated in the revolution from using democratic majorities to redirect the state away from Islamic governance"
        ],
        "effects": [
            "The Guardian Council's candidate vetting has fundamentally altered the political character of every Iranian election since 1992, systematically excluding reformists and producing a political field dominated by regime-loyal conservatives",
            "The 1997 and 2001 elections of Mohammed Khatami — whose reformist candidates passed vetting — and the subsequent disqualification of reformists in 2004 and 2012 demonstrated the Council's role as the principal valve regulating Iran's political temperature",
            "The Council's disqualification of all significant presidential candidates in 2021 — producing Ebrahim Raisi's low-turnout election (48.8%, a record low) — signalled a regime decision to abandon electoral legitimacy in favour of hardline consolidation",
            "The Guardian Council model — a clerical supervisory body with veto power over legislation and candidate qualification — has influenced constitutional design debates in other Muslim-majority states seeking to embed Islamic compliance mechanisms in democratic frameworks"
        ],
        "relationships": [
            {"entity": "Supreme Leader of Iran", "relationship": "SIX_JURISTS_APPOINTED_BY", "note": "The Supreme Leader appoints six of the Council's twelve jurists — giving him structural control over the body"},
            {"entity": "Velayat-e faqih", "relationship": "EMBODIES_PRINCIPLE_OF", "note": "The Guardian Council is the institutional embodiment of Khomeini's velayat-e faqih doctrine — clerical guardianship over the Islamic state"},
            {"entity": "Iranian Constitution (1979)", "relationship": "ESTABLISHED_BY", "note": "The 1979 Constitution created the Guardian Council as a twelve-member body reviewing legislation and vetting candidates"},
            {"entity": "Iranian Parliament (Majlis)", "relationship": "REVIEWS_LEGISLATION_OF", "note": "All Majlis legislation must be reviewed by the Guardian Council for Islamic and constitutional compliance before becoming law"},
            {"entity": "2009 Iranian presidential election", "relationship": "VALIDATED_DISPUTED_RESULT_OF", "note": "The Guardian Council's validation of Ahmadinejad's disputed 2009 reelection triggered the Green Movement protests — the largest political demonstrations in Iran since 1979"}
        ],
    }),

    ("schmalkaldic-league", {
        "summary": (
            "The Schmalkaldic League (Schmalkaldischer Bund) was a defensive military alliance of Protestant princes and cities of the Holy Roman Empire, founded at the town of Schmalkalden in Thuringia on 27 February 1531. Led by Elector John Frederick I of Saxony and Landgrave Philip I of Hesse, it was formed in response to the Diet of Augsburg (1530), where Emperor Charles V had refused to accept the Lutheran Augsburg Confession and demanded return to Catholic practice — threatening Protestant territories with imperial military force.\n\n"
            "At its peak, the League included most major Protestant territories: Saxony, Hesse, Brunswick, Württemberg, and the imperial cities of Strasbourg, Frankfurt, Ulm, Augsburg, and Bremen. It operated as a proto-state structure — with a diet that passed legislation, a military command system, and diplomatic relations with France, England, and the Ottoman Empire (which Henry VIII and Francis I were equally eager to cultivate against the Habsburgs). The League provided 15 years of strategic deterrence that allowed Lutheran churches to consolidate and spread.\n\n"
            "The League was defeated in the Schmalkaldic War (1546–47) — Charles V's most successful military campaign — at the Battle of Mühlberg (April 1547), where both John Frederick and Philip were captured. However, the military victory proved politically inconclusive: the Augsburg Interim (1548) failed to force re-Catholicisation, and the Peace of Augsburg (1555) ultimately recognised the principle of cuius regio, eius religio — giving Protestant princes the right to determine their territories' religion."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Protestant military alliance (1531–47) that deterred Habsburg re-Catholicisation for 15 years; defeated at Mühlberg (1547) but its failure led to the Peace of Augsburg (1555) recognising Protestant princes' right to determine their territories' religion — the first European religious freedom settlement.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Diet of Augsburg (1530) — where Charles V rejected the Lutheran Augsburg Confession and threatened military enforcement of Catholic conformity — created the immediate threat that made a Protestant defensive alliance necessary",
            "The Ottoman threat to Vienna (siege of 1529) gave Protestant princes leverage: Charles V needed their military cooperation against the Turks and could not easily wage simultaneous war against them and the Protestants",
            "Philip of Hesse's diplomatic skill in building the coalition — negotiating between Lutheran and Zwinglian factions who disagreed on theology, and between princes and imperial cities who had different institutional interests — created the broad alliance"
        ],
        "effects": [
            "The League's 15 years of strategic deterrence (1531–1546) gave Lutheran churches time to institutionalise — establishing church orders, schools, trained clergy, and theological consistency that made Lutheranism irreversible even after military defeat",
            "The League's defeat at Mühlberg (1547) and the subsequent Augsburg Interim's failure demonstrated that military force could not reverse the Reformation — making the Peace of Augsburg (1555) and its cuius regio, eius religio principle inevitable",
            "The Peace of Augsburg (1555) — the direct political consequence of the Schmalkaldic War — established the first European legal framework for religious pluralism, recognising that a Christian empire could contain two legitimate confessions",
            "The League's diplomatic strategy — seeking alliance with France, England, and the Ottomans against the Habsburgs — established the template of pan-European Protestant diplomacy that shaped the Wars of Religion and the Thirty Years' War"
        ],
        "relationships": [
            {"entity": "Martin Luther", "relationship": "PROTESTANT_CHURCHES_DEFENDED_BY", "note": "The League provided the military deterrence that protected Lutheran territories and churches during the critical consolidation period"},
            {"entity": "Charles V, Holy Roman Emperor", "relationship": "FORMED_AGAINST_MILITARY_THREAT_OF", "note": "The League was formed in response to Charles V's 1530 demand for return to Catholic practice — threatening Protestant territories with imperial force"},
            {"entity": "Peace of Augsburg (1555)", "relationship": "POLITICAL_CONSEQUENCES_LED_TO", "note": "The failure of Charles V's military victory to force re-Catholicisation produced the Peace of Augsburg — the first European religious freedom settlement"},
            {"entity": "Battle of Mühlberg (1547)", "relationship": "DEFEATED_AT", "note": "The League's military defeat at Mühlberg (1547) captured its two leading princes but proved politically inconclusive"},
            {"entity": "Ottoman Empire", "relationship": "SOUGHT_ALLIANCE_WITH", "note": "The League negotiated with the Ottomans (as did France) to create a second front against the Habsburgs — the first Protestant diplomatic outreach to a non-Christian power"}
        ],
    }),

    ("rump-parliament", {
        "summary": (
            "The Rump Parliament was the name given to the English Parliament after Colonel Thomas Pride's Purge (6 December 1648) removed 186 Presbyterian MPs who opposed putting King Charles I on trial, leaving 60–70 Independent (Puritan) members — the 'rump' — who proceeded with the trial and execution of the King. It was one of the most radical acts in English constitutional history: the Parliament sitting in judgment of and executing a monarch, explicitly invoking the sovereign authority of 'the people of England' over their king.\n\n"
            "The Rump Parliament (December 1648 – April 1653) abolished the monarchy and the House of Lords, declared England a Commonwealth, established the High Court of Justice that tried Charles I, and enacted legislation centralising power in the House of Commons alone. It was forcibly dissolved by Oliver Cromwell in April 1653 when negotiations over its dissolution stalled — Cromwell entering the chamber with soldiers and declaring 'You have sat too long for any good you have been doing lately.' It was briefly recalled in 1659–1660 before the Restoration.\n\n"
            "The Rump Parliament's execution of Charles I — and the constitutional logic that a Parliament acting in the people's name could judge and punish a king — was the most radical assertion of parliamentary sovereignty of the 17th century. Though the Restoration reversed its republican experiments, the Rump's constitutional arguments became the intellectual foundation for the Bill of Rights (1689), the American and French Revolutions, and modern theories of popular sovereignty."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Remnant parliament after Pride's Purge (1648) that tried and executed Charles I; abolished monarchy and Lords; declared England a Commonwealth; its constitutional arguments for parliamentary sovereignty over the Crown were foundational for the Bill of Rights (1689) and democratic revolution theory.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Pride's Purge (December 6, 1648) — Colonel Pride's military exclusion of 186 Presbyterian MPs who opposed the King's trial — was the constitutional coup that created the Rump as an instrument of radical Independents and the New Model Army",
            "Charles I's continuing negotiations with the Scots and Presbyterian faction during his imprisonment — despite military defeat in the Civil War — convinced Cromwell and the Independents that no negotiated settlement was possible and only trial could resolve the crisis",
            "The New Model Army's political radicalisation — shaped by the Agitators and Leveller movements — created military pressure for a radical solution to the constitutional crisis that more conservative MPs were unwilling to take"
        ],
        "effects": [
            "The execution of Charles I (January 30, 1649) established the revolutionary precedent that a monarch could be held legally accountable by his subjects — a constitutional logic that directly influenced the trial of Louis XVI (1793) and the development of head-of-state accountability in democratic theory",
            "The Rump's abolition of the monarchy and House of Lords — creating England as a Commonwealth — established the first republican government of a major European state, providing the institutional template for subsequent republican experiments",
            "Cromwell's forced dissolution of the Rump (1653) with the words 'You have sat too long' established the constitutional problem of legislative impotence and executive action that recurs throughout democratic history — from Bonaparte's 18 Brumaire to 20th-century executive-legislative conflicts",
            "The Rump's constitutional arguments — that Parliament acting in the people's name was superior to the Crown — were the intellectual foundation of the Bill of Rights (1689), which permanently established parliamentary sovereignty without the revolutionary rupture of regicide"
        ],
        "relationships": [
            {"entity": "Charles I of England", "relationship": "TRIED_AND_EXECUTED", "note": "The Rump Parliament constituted the High Court of Justice that tried and executed Charles I on January 30, 1649"},
            {"entity": "Oliver Cromwell", "relationship": "DISSOLVED_BY", "note": "Cromwell forcibly dissolved the Rump in April 1653 — entering with soldiers when it refused to set a dissolution date"},
            {"entity": "Pride's Purge (1648)", "relationship": "CREATED_BY", "note": "The Rump was created by Colonel Pride's military exclusion of 186 MPs — the most blatant military intervention in English parliamentary history"},
            {"entity": "English Commonwealth (1649–1660)", "relationship": "ESTABLISHED", "note": "The Rump abolished the monarchy and Lords and declared England a Commonwealth — the first republican government of a major European state"},
            {"entity": "Bill of Rights (1689)", "relationship": "CONSTITUTIONAL_ARGUMENTS_FOUNDATION_FOR", "note": "The Rump's arguments for parliamentary sovereignty over the Crown became the intellectual foundation for the Bill of Rights (1689)"}
        ],
    }),

    ("loya-jirga", {
        "summary": (
            "The Loya Jirga (Pashto: 'Grand Assembly') is Afghanistan's traditional grand council — a convocation of tribal elders, religious leaders, and community representatives that has served as the supreme consultative authority for major national decisions for centuries. Its origins lie in the Pashtun jirga tradition of collective decision-making through consensus among tribal elders, but the Loya Jirga has functioned at a national scale since at least the establishment of the Durrani Empire (1747) by Ahmad Shah Durrani, who was himself elected at a Loya Jirga.\n\n"
            "Major Loya Jirgas include: the 1964 Loya Jirga that approved King Zahir Shah's liberal constitution; the 2002 Emergency Loya Jirga that established Hamid Karzai's transitional authority after the Taliban's fall; the 2003–04 Constitutional Loya Jirga that drafted and approved Afghanistan's post-2001 constitution; and repeated consultative Jirgas on peace negotiations with the Taliban. The institution has survived monarchies, communist coups, Soviet occupation, civil war, and Taliban rule — demonstrating extraordinary institutional resilience.\n\n"
            "The Loya Jirga occupies a unique position: it is simultaneously a traditional tribal mechanism and a constitutional institution recognised in Afghan law. Its legitimacy derives from customary authority (jirga tradition) rather than elections — making it the primary vehicle through which decisions affecting all Afghans can gain traditional legitimacy even when formal institutions have collapsed."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Afghanistan's traditional grand council of tribal elders; elected Ahmad Shah Durrani in 1747; approved the 1964 constitution; established Karzai's transitional authority (2002) and approved the post-2001 constitution (2003–04); one of the world's most enduring traditional governance institutions.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Pashtun jirga tradition of tribal collective decision-making by consensus — emphasising unanimity and elder authority over individual power — provided the institutional template that was scaled up to the national Loya Jirga",
            "Afghanistan's ethnic, tribal, and regional fragmentation — Pashtun, Tajik, Hazara, Uzbek, and other communities with distinct traditions — made a traditional consensus-based assembly more culturally legitimate than imposed electoral institutions for major constitutional decisions",
            "The weakness of central state authority in Afghanistan's mountainous geography — which has always required negotiated accommodation between the centre and peripheral tribal communities — gave the Loya Jirga its enduring role as the mechanism for achieving national consensus"
        ],
        "effects": [
            "The 2002 Emergency Loya Jirga — convened under UN auspices after the Taliban's fall — established Hamid Karzai as transitional leader and provided the traditional legitimacy for the new post-Taliban order that foreign military force alone could not supply",
            "The 2003–04 Constitutional Loya Jirga produced Afghanistan's post-2001 constitution — a compromise document balancing Islamic law, customary practice, and liberal democratic rights that governed (imperfectly) for 17 years until the 2021 Taliban takeover",
            "The Taliban's use of consultative shuras (related assemblies) alongside their refusal to convene a genuine Loya Jirga after 2021 illustrated both the institution's continued legitimacy and the Taliban's selective use of traditional forms to avoid genuine power-sharing",
            "The Loya Jirga model — a traditional assembly granting legitimacy to major constitutional decisions — has influenced nation-building and transitional justice frameworks in Afghanistan and post-conflict constitutional design globally"
        ],
        "relationships": [
            {"entity": "Ahmad Shah Durrani", "relationship": "ELECTED_AT_LOYA_JIRGA", "note": "Ahmad Shah Durrani was elected at a Loya Jirga in 1747 — founding the Durrani Empire and establishing the assembly's national legitimacy"},
            {"entity": "Hamid Karzai", "relationship": "SELECTED_TRANSITIONAL_LEADER_AS", "note": "The 2002 Emergency Loya Jirga selected Karzai as transitional leader — providing traditional legitimacy for the post-Taliban order"},
            {"entity": "Afghan Constitution (2004)", "relationship": "APPROVED", "note": "The 2003–04 Constitutional Loya Jirga drafted and approved Afghanistan's post-2001 constitution"},
            {"entity": "Taliban", "relationship": "TRADITIONAL_LEGITIMACY_CLAIMED_BY_BUT_NOT_CONVENED", "note": "The Taliban has used related shura assemblies but refused to convene a genuine Loya Jirga after 2021 — illustrating the institution's continued symbolic power"},
            {"entity": "Pashtun jirga tradition", "relationship": "SCALED_FROM", "note": "The Loya Jirga scaled the Pashtun jirga tradition of tribal consensus decision-making to the national level"}
        ],
    }),

    ("rajya-sabha", {
        "summary": (
            "The Rajya Sabha ('Council of States') is the upper house of India's bicameral Parliament, the permanent chamber that is never fully dissolved. Established by the Constitution of India (1950) and convening for the first time on 3 April 1952, it consists of 245 members: 233 elected by state and union territory assemblies through proportional representation and 12 nominated by the President for distinction in literature, science, art, and social service. Its primary role is as a revising chamber and representative of India's federal states.\n\n"
            "Unlike the Lok Sabha (lower house), the Rajya Sabha cannot be dissolved by the President — one-third of its members retire every two years, giving it continuity across political changes. It has equal legislative power with the Lok Sabha except on money bills (which the Lok Sabha can pass over Rajya Sabha objections) and can introduce and pass most legislation independently. Its composition — elected by state assemblies rather than directly — means it often reflects different political configurations than the Lok Sabha, providing a genuine check on federal overreach.\n\n"
            "The Rajya Sabha has been the institutional arena for some of India's most significant constitutional debates: the Emergency (1975–77), the 42nd Amendment, federalism disputes between the Centre and states, and more recently the passage of controversial constitutional amendments including the abrogation of Article 370 (Jammu and Kashmir's special status) in 2019."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "India's permanent upper house (1952); represents federal states; permanent chamber that cannot be dissolved; has been the arena for major constitutional debates including the Emergency, federalism disputes, and the Article 370 abrogation (2019).",
            "significanceCategory": "regional"
        },
        "causes": [
            "India's constitutional framers — drawing on the Westminster model and the US Senate — recognised that a permanent revising chamber representing federal states was necessary to balance the Lok Sabha's direct popular mandate and prevent majoritarian overreach",
            "India's vast federal diversity — 28 states with distinct languages, cultures, and political traditions — required an upper house where states had guaranteed representation independent of central government majorities",
            "The experience of colonial legislative councils, where nominated upper chambers had served as checks on elected lower chambers, informed the Rajya Sabha's design — though converted from nomination to indirect election to provide democratic legitimacy"
        ],
        "effects": [
            "The Rajya Sabha's permanent character has provided constitutional continuity during politically turbulent periods — including the Emergency (1975–77) — when the Lok Sabha's term was extended through constitutional amendment",
            "The Rajya Sabha's role in reviewing and amending legislation has produced improvements to major bills — serving as an effective legislative check particularly when different coalitions control the two houses",
            "The passage of the Article 370 abrogation (August 2019) through the Rajya Sabha — where the BJP lacked a majority but secured votes from nominated members and regional allies — illustrated how the chamber's composition can be managed for politically sensitive decisions",
            "The Rajya Sabha's 12 nominated members — drawn from arts, literature, science, and public service — have included distinguished figures including musicians, scientists, and scholars who have enriched Indian parliamentary discourse"
        ],
        "relationships": [
            {"entity": "Constitution of India (1950)", "relationship": "ESTABLISHED_BY", "note": "The Constitution of India (1950) created the Rajya Sabha as India's permanent upper house"},
            {"entity": "Lok Sabha", "relationship": "UPPER_HOUSE_COMPLEMENTING", "note": "The Rajya Sabha is the upper house that complements and revises legislation passed by the directly elected Lok Sabha"},
            {"entity": "Indian Emergency (1975–1977)", "relationship": "CONSTITUTIONAL_CONTINUITY_MAINTAINED_DURING", "note": "The Rajya Sabha's permanent character maintained constitutional continuity when Indira Gandhi's government extended the Lok Sabha's term during the Emergency"},
            {"entity": "Article 370 abrogation (2019)", "relationship": "PASSED", "note": "The Rajya Sabha passed the Article 370 abrogation (August 2019) — revoking Jammu and Kashmir's special constitutional status"},
            {"entity": "Indian federalism", "relationship": "INSTITUTIONAL_GUARDIAN_OF", "note": "The Rajya Sabha's composition — elected by state assemblies — makes it the constitutional guardian of India's federal structure"}
        ],
    }),

    ("senate", {
        "summary": (
            "The United States Senate is the upper chamber of the US Congress, consisting of 100 senators — two from each of the fifty states — serving six-year staggered terms. Established by Article I of the Constitution (1789) and directly inspired by the Roman Senate, it was designed by the Constitutional Convention as the 'cooling saucer' of American democracy — a deliberate counterweight to the more populist House of Representatives, with exclusive powers over treaty ratification, presidential appointments, and impeachment trials.\n\n"
            "The Senate's distinctive features — equal representation for all states regardless of population, the filibuster (requiring 60 votes to end debate), and the advice-and-consent power over executive and judicial appointments — make it the world's most powerful legislative upper chamber and one of the most countermajoritarian institutions in any democracy. Two senators from Wyoming (pop. 580,000) have equal power to two senators from California (pop. 39 million).\n\n"
            "The Senate has been the arena for American history's most consequential legislative battles: the Missouri Compromise (1820), the 14th Amendment (1868), the rejection of the League of Nations (1919), the Civil Rights Act (1964), and the impeachment trials of three presidents (Andrew Johnson 1868, Bill Clinton 1999, Donald Trump 2020/2021). Its confirmation power over Supreme Court justices has made it the most important external check on the judicial branch."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Upper chamber of the US Congress since 1789; world's most powerful legislative upper house; 100 senators (2 per state) with exclusive treaty, appointment, and impeachment powers; arena for the Missouri Compromise, Civil Rights Act, League of Nations rejection, and three presidential impeachments.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Connecticut Compromise at the Constitutional Convention (1787) resolved the deadlock between large and small states by creating a bicameral legislature — a lower house based on population and an upper house with equal state representation",
            "The Framers' concern about majority tyranny — shaped by their reading of Polybius, Montesquieu, and the failures of the Continental Congress — led them to design the Senate as a deliberate check on popular passions: the 'cooling saucer' metaphor attributed to Washington",
            "The explicit model of the Roman Senate — whose institutional continuity and deliberative character the Founders admired — shaped both the Senate's name and its intended role as a body of senior statesmen providing counsel to the nation"
        ],
        "effects": [
            "The Senate's equal state representation — two senators per state regardless of population — has given disproportionate structural power to small, rural, and conservative states throughout American history, shaping legislative outcomes on everything from slavery to healthcare",
            "The Senate's rejection of the Treaty of Versailles and the League of Nations (1919–1920) — by 49-35, short of the required two-thirds majority — prevented US membership in the international organisation that might have deterred WWII, making it one of the most consequential votes in American history",
            "The Senate's filibuster — requiring 60 votes to end debate — has shaped American social policy by giving minority parties effective veto power over legislation, producing the legislative gridlock that characterises contemporary US politics",
            "The Senate's Supreme Court confirmation power has made it the decisive external check on the federal judiciary: its role in confirming or blocking nominees has shaped American constitutional law for 235 years"
        ],
        "relationships": [
            {"entity": "US Constitution (1789)", "relationship": "ESTABLISHED_BY", "note": "Article I of the Constitution (1789) established the Senate as the upper chamber of Congress"},
            {"entity": "Roman Senate", "relationship": "NAMED_AND_MODELLED_AFTER", "note": "The US Senate was explicitly named after and partly modelled on the Roman Senate — the Founders' primary classical reference for republican governance"},
            {"entity": "Treaty of Versailles", "relationship": "REJECTED_RATIFICATION_OF", "note": "The Senate rejected the Treaty of Versailles (1919–20) — preventing US membership in the League of Nations and reshaping 20th-century world history"},
            {"entity": "Civil Rights Act (1964)", "relationship": "PASSED_AFTER_HISTORIC_DEBATE", "note": "The Senate's passage of the Civil Rights Act (1964) — after a 60-day filibuster — was the most significant civil rights legislation since Reconstruction"},
            {"entity": "Connecticut Compromise (1787)", "relationship": "CREATED_BY", "note": "The Connecticut Compromise at the Constitutional Convention (1787) created the Senate as the resolution to the large-state vs. small-state deadlock"}
        ],
    }),

    ("national-assembly", {
        "summary": (
            "The French National Assembly (Assemblée nationale) is the lower house of the French Parliament — the directly elected 577-member chamber that holds primary legislative authority in the Fifth Republic. But in world history the name is inseparable from the revolutionary body of June 1789, when the Estates-General's Third Estate, locked out of their meeting hall, gathered at the royal tennis court and declared themselves the National Assembly — the supreme representative body of the French nation, subordinate to no king.\n\n"
            "The Tennis Court Oath (June 20, 1789) — where the deputies swore to remain assembled until they had given France a constitution — was the founding act of the French Revolution and one of the most dramatic moments in the history of representative government. The National Assembly (later Constituent Assembly) drafted the Declaration of the Rights of Man and Citizen (August 1789) — the Enlightenment's most influential political document — and the Constitution of 1791 that transformed France into a constitutional monarchy.\n\n"
            "The modern Fifth Republic's National Assembly, created by de Gaulle's 1958 Constitution, is directly elected under a two-round majority system and holds the power to censure and remove the government. Its relationship with the Senate and the directly elected President creates the 'cohabitation' dynamic unique to French semi-presidentialism — where the President and Prime Minister may belong to opposing parties."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "The 1789 National Assembly was the founding institution of the French Revolution; the Tennis Court Oath declared national sovereignty over royal authority; drafted the Declaration of the Rights of Man (1789); the modern Assembly is the primary legislature of France's Fifth Republic.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Crown's fiscal crisis (1789) — France was bankrupt after supporting the American Revolution — forced Louis XVI to convene the Estates-General for the first time since 1614, creating the political opening the Third Estate transformed into revolution",
            "The Enlightenment ideas of Rousseau, Montesquieu, and Locke — popular sovereignty, natural rights, the social contract — had convinced the educated bourgeoisie that legitimate government required the consent of the governed rather than royal or clerical authority",
            "The Crown's decision to lock the Third Estate out of their meeting hall (June 20, 1789) — rather than defusing the crisis — forced the deputies to the tennis court, producing the oath that declared their authority supreme and initiated the Revolution"
        ],
        "effects": [
            "The Declaration of the Rights of Man and Citizen (August 1789) — drafted by the National Assembly — became the foundational document of modern liberal democracy, directly influencing the US Bill of Rights, the UN Declaration of Human Rights (1948), and constitutions worldwide",
            "The National Assembly's abolition of feudal privileges (August 4, 1789) — in a single night of noble self-sacrifice — dismantled France's entire social hierarchy and provided the model for revolutionary land reform across Europe and the Americas",
            "The French Revolutionary and Napoleonic Wars (1792–1815) — originating from the revolution the National Assembly initiated — spread revolutionary principles of nationalism, popular sovereignty, and legal equality across Europe, reshaping the continent's political order",
            "The Fifth Republic's National Assembly — elected under a two-round majority system — has produced 'cohabitation' governments (1986, 1993, 1997) where President and Prime Minister are from opposing parties, demonstrating the creative tensions of semi-presidentialism"
        ],
        "relationships": [
            {"entity": "Tennis Court Oath (1789)", "relationship": "FOUNDED_THROUGH", "note": "The Tennis Court Oath (June 20, 1789) declared the Third Estate the National Assembly — supreme representative of the French nation"},
            {"entity": "Declaration of the Rights of Man and Citizen (1789)", "relationship": "DRAFTED_AND_ADOPTED", "note": "The National Assembly drafted and adopted the Declaration — one of the most influential political documents in history"},
            {"entity": "Louis XVI", "relationship": "SOVEREIGNTY_CLAIMED_AGAINST", "note": "The National Assembly declared its authority supreme over the Crown — the revolutionary assertion that national sovereignty superseded royal authority"},
            {"entity": "French Constitution of 1958", "relationship": "CURRENT_FORM_ESTABLISHED_BY", "note": "The 1958 Constitution of the Fifth Republic established the modern National Assembly and its relationship with the Senate and President"},
            {"entity": "Estates-General (1789)", "relationship": "TRANSFORMED_FROM", "note": "The National Assembly was constituted from the Third Estate of the Estates-General after they declared themselves the supreme representative body"}
        ],
    }),

    ("bundesrat", {
        "summary": (
            "The German Bundesrat ('Federal Council') is the constitutional body through which Germany's sixteen Länder (states) participate in federal legislation and administration. It is not directly elected: each Land government sends between 3 and 6 votes (depending on population) cast as a bloc by that Land's government — making it a chamber of state governments rather than individual senators. It must approve all federal legislation affecting state powers, state finances, or constitutional amendments — giving it a structural veto over a substantial proportion of all federal legislation.\n\n"
            "The Bundesrat traces its institutional lineage to the Frankfurt Constitution of 1849 and especially the Bundesrat of the German Empire (1871), where Bismarck designed it as a federal council of state governments to balance Prussian dominance with the interests of other German kingdoms and principalities. The Weimar Republic and the post-1945 Basic Law both retained the institution, though with evolving powers. The post-1945 Bundesrat was designed to prevent the centralisation of power that had enabled the Nazi seizure of the state.\n\n"
            "The Bundesrat has become most significant as a political arena when the federal government and the majority of state governments are controlled by opposing parties — creating 'divided government' that can block federal legislation and force cross-party compromise. This dynamic has made it a central element of German consensus democracy (Konsensdemokratie)."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "German federal chamber representing 16 state governments; must approve legislation affecting states and constitutional amendments; traces origins to the 1871 Imperial Bundesrat; designed post-1945 to prevent centralisation; key mechanism of German consensus democracy.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Germany's federal structure — a union of previously sovereign states with distinct administrative traditions — required a constitutional chamber giving state governments direct participation in federal legislation affecting their powers",
            "Bismarck's 1871 constitutional design gave the Bundesrat (representing state governments) primacy alongside the elected Reichstag — reflecting his preference for executive federalism over parliamentary democracy",
            "The post-1945 Basic Law's designers deliberately strengthened the Bundesrat as a check on federal power, responding to the Weimar Republic's vulnerability to central executive seizure and the Nazi experience of Gleichschaltung (coordination) that had eliminated state autonomy"
        ],
        "effects": [
            "The Bundesrat's veto power over legislation affecting state interests has produced Germany's distinctive brand of consensus politics — forcing federal governments to negotiate with state-level oppositions and producing broader legislative compromises than majoritarian systems allow",
            "The Bundesrat's role in ratifying constitutional amendments (requiring two-thirds majority) has made Germany's Basic Law remarkably stable — with only the emergency constitutional provisions changed fundamentally since 1949",
            "Bundesrat blocking of federal legislation during divided-government periods (1999–2003, 2010–2013) has been both praised as a check on federal overreach and criticised as creating policy gridlock — driving reform debates about the distribution of federal and state competencies",
            "The Bundesrat model — state governments directly represented in federal legislation — has influenced constitutional design in post-communist Central European states and in EU institutional debates about national government representation"
        ],
        "relationships": [
            {"entity": "German Basic Law (1949)", "relationship": "ESTABLISHED_IN_CURRENT_FORM_BY", "note": "The Basic Law (1949) established the post-war Bundesrat as a check on federal power following the Nazi experience"},
            {"entity": "German Länder (16 states)", "relationship": "REPRESENTS", "note": "The Bundesrat represents the governments of Germany's 16 Länder — each casting 3–6 votes as a bloc"},
            {"entity": "German Empire Bundesrat (1871)", "relationship": "INSTITUTIONAL_ANCESTOR", "note": "Bismarck's 1871 Imperial Bundesrat — the federal council of German state governments — is the direct institutional ancestor"},
            {"entity": "German Bundestag", "relationship": "FEDERAL_CO-LEGISLATOR_WITH", "note": "The Bundesrat co-legislates with the directly elected Bundestag — sharing power over legislation affecting state interests"},
            {"entity": "German federalism", "relationship": "INSTITUTIONAL_GUARDIAN_OF", "note": "The Bundesrat is the constitutional mechanism through which German federalism is protected from central government overreach"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 03 — {len(ENTITIES)} entities (Class 311: Assemblies, Councils & Upper Houses)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
