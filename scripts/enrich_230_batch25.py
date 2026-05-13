#!/usr/bin/env python3
"""
Batch 25 — 8 entities: Roger B. Taney, Guadalupe Victoria, Adam Loftus,
Langdon Cheves, John P. Kennedy, John Harvie, Thomas Todd, Mary Ekpere-Eta
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

    # 1 — Roger B. Taney
    ("roger-b-taney", {
        "summary": (
            "Roger Brooke Taney (1777–1864) was an American lawyer, statesman, and jurist "
            "who served as the fifth Chief Justice of the United States from 1836 until "
            "his death — a 28-year tenure second in length only to John Marshall's, "
            "during which he presided over the Supreme Court in the most constitutionally "
            "consequential period in American history before the Civil War. He is "
            "principally remembered — and condemned — for delivering the majority opinion "
            "in Dred Scott v. Sandford (1857), a catastrophically wrong decision in which "
            "the Court ruled that African Americans could not be US citizens, that Congress "
            "lacked the power to prohibit slavery in the territories, and that the Missouri "
            "Compromise was unconstitutional — a ruling that inflamed the sectional crisis, "
            "accelerated the path to the Civil War, and has been consistently ranked as one "
            "of the worst decisions in Supreme Court history.\n\n"
            "Before his Chief Justiceship, Taney had a distinguished career: he served as "
            "US Attorney General (1831–1833) under Andrew Jackson, and as Secretary of the "
            "Treasury (1833–1834), where he was instrumental in carrying out Jackson's "
            "political war on the Second Bank of the United States — withdrawing federal "
            "deposits from the Bank before its charter expired, an act for which the Senate "
            "censured him. His appointment as Chief Justice by Jackson in 1836 was part "
            "of Jackson's legacy project to stamp a Jacksonian Democratic philosophy on "
            "the federal judiciary.\n\n"
            "As Chief Justice, Taney's contributions were not entirely in the direction "
            "of Dred Scott. He wrote important opinions on commerce, corporate law, and "
            "states' rights that shaped 19th-century constitutional doctrine. After the "
            "outbreak of the Civil War, he controversially challenged Lincoln's suspension "
            "of habeas corpus in Ex parte Merryman (1861), asserting that only Congress "
            "could suspend the writ — a position that, while legally cogent, put him on "
            "the wrong side of the Union's war effort.\n\n"
            "Taney's legacy is deeply divided: a legal technician of real ability whose "
            "Dred Scott opinion — written with evident racial animus — disgraced the "
            "Court he led and contributed to a national catastrophe."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Fifth Chief Justice of the United States (1836–1864); author of the Dred Scott decision (1857) — the most consequential and universally condemned ruling in US Supreme Court history, ruling that African Americans could not be US citizens and that Congress could not prohibit slavery in territories; previously Jackson's AG and Treasury Secretary.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Andrew Jackson's political project — destroying the Second Bank of the United States and installing Jacksonian Democratic philosophy throughout the federal government — drove Taney's political appointments and eventually his Chief Justiceship",
            "The intensifying sectional crisis over slavery and the status of free versus slave territory in the United States created the constitutional tinderbox that his Dred Scott ruling ignited",
            "The Southern slaveholder class's need for judicial validation of slavery's permanence and constitutionally protected status shaped the ideological context in which the Dred Scott majority opinion was written"
        ],
        "effects": [
            "The Dred Scott decision (1857) — which he authored — declared the Missouri Compromise unconstitutional and ruled African Americans could not be citizens, inflaming sectional tensions and accelerating the path to the Civil War",
            "His service as Jackson's Treasury Secretary and his removal of federal deposits from the Second Bank effectively destroyed the Bank — reshaping American financial history by ending the era of a central banking institution",
            "His Ex parte Merryman opinion (1861) challenging Lincoln's suspension of habeas corpus established an important precedent on civil liberties in wartime — even though Lincoln effectively ignored it during the war",
            "His long Chief Justiceship shaped 19th-century US constitutional doctrine on commerce, corporate law, and the division of federal-state authority in lasting ways that preceded and survived the Dred Scott catastrophe"
        ],
        "relationships": [
            {"entity": "Dred Scott v. Sandford (1857)", "relationship": "WROTE_MAJORITY_OPINION_IN", "note": "Author of the majority opinion in Dred Scott — ruling African Americans could not be US citizens and Congress could not prohibit slavery in territories"},
            {"entity": "Andrew Jackson (US President)", "relationship": "APPOINTED_BY_AND_SERVED", "note": "Served as Jackson's Attorney General and Treasury Secretary; appointed to Chief Justiceship by Jackson in 1836"},
            {"entity": "Second Bank of the United States", "relationship": "INSTRUMENTAL_IN_DESTROYING", "note": "As Treasury Secretary, withdrew federal deposits from the Second Bank — carrying out Jackson's political war on the institution"},
            {"entity": "John Marshall (predecessor Chief Justice)", "relationship": "SUCCEEDED_AS_CHIEF_JUSTICE", "note": "Succeeded John Marshall as Chief Justice in 1836; his tenure (28 years) was the second longest in Court history after Marshall's"},
            {"entity": "Abraham Lincoln (US President)", "relationship": "CONTESTED_WITH", "note": "Challenged Lincoln's suspension of habeas corpus in Ex parte Merryman (1861) — asserting only Congress could suspend the writ"}
        ]
    }),

    # 2 — Guadalupe Victoria
    ("guadalupe-victoria", {
        "summary": (
            "Guadalupe Victoria (1786–1843), born José Miguel Ramón Adaucto Fernández y "
            "Félix, was a Mexican independence fighter and statesman who served as the "
            "first President of the United Mexican States (1824–1829) — the man who "
            "presided over the creation of the Mexican federal republic and the translation "
            "of the independence movement's ideals into constitutional governance. "
            "His choice of the name Guadalupe Victoria — combining the patron saint of "
            "Mexico with the Spanish word for 'victory' — symbolized both his Catholic "
            "heritage and his military goals.\n\n"
            "Victoria had been one of the most resilient guerrilla fighters of the Mexican "
            "War of Independence. Unlike other independence leaders who were captured and "
            "executed by Spanish forces, Victoria survived by hiding in the mountains and "
            "jungles of Veracruz for years — refusing to surrender even when the independence "
            "movement appeared to be defeated. When Agustín de Iturbide proclaimed the "
            "Plan de Iguala in 1821 — proposing independence under a constitutional monarchy "
            "— Victoria initially supported it, and Mexico achieved independence from Spain. "
            "When Iturbide declared himself Emperor Agustín I in 1822, Victoria turned "
            "against him and participated in the republican rebellion that overthrew "
            "the empire and established the First Mexican Republic.\n\n"
            "As the republic's first president, Victoria oversaw the drafting and implementation "
            "of the Constitution of 1824 — a federal constitution modeled partly on the "
            "United States Constitution that established the structure of Mexico's "
            "constitutional government. His administration negotiated recognition of "
            "Mexican independence from foreign powers, abolished the Inquisition, "
            "and made significant policy decisions about Mexico's relationship with its "
            "former colonial master and its new republican neighbors.\n\n"
            "He is the only Mexican president in the early republican period to complete "
            "his full term in office — a distinction that reflects both his political skill "
            "and the extraordinary political instability of Mexico's 19th-century history."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "First President of Mexico (1824–1829) and the only early Mexican president to complete his full term; resilient independence fighter who survived the Spanish reconquest attempt; presided over the Constitution of 1824 and Mexico's recognition as an independent state.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Mexican War of Independence (1810–1821) and Spain's brutal suppression of the independence movement — which killed most independence leaders — created the guerrilla survival strategy that defined Victoria's path through the conflict",
            "Agustín de Iturbide's monarchical ambition — declaring himself Emperor in 1822 after independence was achieved — created the republican opposition that brought Victoria to power as the republic's first president",
            "The influence of the US Constitution and Enlightenment republican theory on Mexican political thought provided the ideological framework for the Constitution of 1824 that Victoria's presidency implemented"
        ],
        "effects": [
            "His presidency established the First Mexican Republic — creating the constitutional federal structure that, however unstable, defined Mexico's republican tradition",
            "The Constitution of 1824, implemented under his presidency, was Mexico's foundational republican constitutional document — a framework for federal governance that influenced all subsequent Mexican constitutional development",
            "His successful completion of his full four-year presidential term — unique among early Mexican presidents — established a precedent for constitutional succession in a politically unstable environment",
            "His abolition of the Inquisition and policies on foreign recognition helped define the modern secular and internationally recognized Mexican state"
        ],
        "relationships": [
            {"entity": "First Mexican Republic", "relationship": "FIRST_PRESIDENT_OF", "note": "First President of the United Mexican States (1824–1829) — the first head of state of Mexico as an independent republic"},
            {"entity": "Mexican Constitution of 1824", "relationship": "IMPLEMENTED", "note": "His presidency implemented the Constitution of 1824 — Mexico's foundational federal republican constitutional document"},
            {"entity": "Agustín de Iturbide (Emperor Agustín I)", "relationship": "OPPOSED_AND_OVERTHREW", "note": "Initially supported Iturbide's independence plan but opposed his imperial ambition and participated in the republican rebellion that overthrew him"},
            {"entity": "Mexican War of Independence (1810–1821)", "relationship": "FIGHTER_IN", "note": "A resilient guerrilla fighter in the Mexican independence struggle who survived Spanish suppression by hiding in the Veracruz jungles"},
            {"entity": "Mexican independence from Spain (1821)", "relationship": "HELPED_ACHIEVE", "note": "One of the military and political leaders who brought about Mexican independence from Spain in 1821"}
        ]
    }),

    # 3 — Adam Loftus
    ("adam-loftus", {
        "summary": (
            "Adam Loftus (c. 1533–1605) was an English-born clergyman and colonial "
            "administrator who played a foundational role in the Elizabethan Protestant "
            "plantation of Ireland — serving successively as Church of Ireland Archbishop "
            "of Armagh (1563–1567), Archbishop of Dublin (1567–1605), and Lord Chancellor "
            "of Ireland (1581–1605), and as the first Provost of Trinity College Dublin "
            "(1592–1594). His career combined ecclesiastical leadership with political "
            "administration in a way that made him one of the most powerful men in "
            "Elizabethan Ireland — and one of the most controversial, accused by his "
            "contemporaries of corruption, nepotism, and torture.\n\n"
            "Loftus arrived in Ireland in the early Elizabethan period as part of the "
            "English Protestant establishment's effort to impose the Reformation on "
            "a predominantly Catholic Irish population. His role as Archbishop was to "
            "extend Protestantism throughout the Irish Church — a project that met "
            "determined resistance from the Old English Catholic community and the "
            "Gaelic Irish population. As both the senior churchman and the Lord Chancellor "
            "(the highest legal officer in Ireland), he combined ecclesiastical and "
            "judicial authority in a single person — an unusual concentration of power "
            "that made him essential to the English colonial project in Ireland.\n\n"
            "His founding role at Trinity College Dublin — established in 1592 by royal "
            "charter as Ireland's first university — was his most enduring institutional "
            "contribution. Trinity was conceived as a Protestant institution: a university "
            "to train English Protestant clergy and administrators for Ireland, competing "
            "with the Catholic continental colleges that educated Irish clergy who returned "
            "as Counter-Reformation missionaries. Trinity's foundation is thus inseparable "
            "from the broader Protestant colonial project in Ireland.\n\n"
            "His legacy is deeply ambivalent: an institution-builder (Trinity College) "
            "whose methods included documented use of torture in the 1584 case of "
            "Dermot Hurley, the Catholic Archbishop of Cashel."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Elizabethan Church of Ireland Archbishop of Dublin, Lord Chancellor of Ireland, and first Provost of Trinity College Dublin (founded 1592); a central figure in the Protestant plantation of Ireland — combining ecclesiastical and judicial authority in the colonial project.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Queen Elizabeth I's determination to extend the English Reformation to Ireland — imposing Protestant ecclesiastical authority on a predominantly Catholic population — drove the appointment of figures like Loftus to senior Church of Ireland roles",
            "The English colonial project in Ireland — the plantation system that sought to replace Gaelic Irish landholders with Protestant English settlers — created the political context in which Loftus exercised combined ecclesiastical and legal authority",
            "The Counter-Reformation's strength in Ireland — with Catholic clergy trained in continental seminaries returning as missionaries — created the Protestant institutional response that included founding Trinity College Dublin"
        ],
        "effects": [
            "His founding of Trinity College Dublin (1592) as Ireland's first university created an institution that has educated generations of Irish leaders — despite its Protestant colonial origins, it became central to Irish intellectual life",
            "His 38-year archbishopric (1567–1605) shaped the development of the Church of Ireland during the critical Elizabethan period — embedding Protestant ecclesiastical structures even as they failed to convert most of the Irish population",
            "His simultaneous hold on the Lord Chancellorship and the Archbishopric concentrated civil and ecclesiastical authority in a single figure — a model of colonial governance that characterized Elizabethan Ireland",
            "His documented use of torture in 1584 (in the Dermot Hurley case) illustrated the violence underlying the Elizabethan colonial project in Ireland"
        ],
        "relationships": [
            {"entity": "Trinity College Dublin", "relationship": "FIRST_PROVOST_OF", "note": "First Provost of Trinity College Dublin (1592–1594) — founded by royal charter as Ireland's first university on his initiative"},
            {"entity": "Church of Ireland", "relationship": "ARCHBISHOP_OF_DUBLIN_IN", "note": "Church of Ireland Archbishop of Dublin (1567–1605) — the senior Protestant ecclesiastical authority in Ireland"},
            {"entity": "Lord Chancellor of Ireland", "relationship": "SERVED_AS", "note": "Lord Chancellor of Ireland (1581–1605) — combining the highest legal office with his archbishopric"},
            {"entity": "Elizabethan Protestant plantation of Ireland", "relationship": "AGENT_OF", "note": "Central agent of the Elizabethan Protestant colonial project in Ireland — imposing Reformation ecclesiastical structures on a Catholic population"},
            {"entity": "Dermot Hurley (Catholic Archbishop of Cashel, executed 1584)", "relationship": "ORDERED_TORTURE_OF", "note": "Ordered the torture of Dermot Hurley in 1584 — a controversial case that illustrates the violence of the Elizabethan colonial project"}
        ]
    }),

    # 4 — Langdon Cheves
    ("langdon-cheves", {
        "summary": (
            "Langdon Cheves (1776–1857) was an American lawyer, politician, and banker "
            "from South Carolina who had three distinct and distinguished phases of public "
            "life: as a US Congressman and War Hawk who helped push the United States "
            "into the War of 1812; as Speaker of the House of Representatives; and as "
            "the president of the Second Bank of the United States who stabilized the "
            "institution after the financial crisis of 1819 by implementing severe "
            "contractionary policies that earned him both credit for saving the Bank "
            "and blame for deepening the economic distress of American debtors.\n\n"
            "In Congress (1810–1815), Cheves was a leader among the 'War Hawk' faction "
            "— the group of southern and western congressmen who pushed for war with "
            "Britain over maritime rights violations and the impressment of American "
            "sailors, and who believed that war would lead to the conquest of Canada "
            "and the end of British support for Native American resistance. He chaired "
            "the Committee on Naval Affairs and helped prepare the young republic's navy "
            "for the war that the Hawks were demanding. He briefly served as Speaker "
            "of the House (succeeding Henry Clay who had resigned to join the peace "
            "negotiating team) before returning to South Carolina.\n\n"
            "His most consequential role came as president of the Second Bank of the "
            "United States (1819–1823), appointed when the Bank was near collapse after "
            "reckless lending. Cheves implemented a brutal contraction: calling in loans, "
            "restricting credit, and stabilizing the Bank's balance sheet at the cost "
            "of widespread bankruptcy and distress among American farmers and debtors. "
            "He succeeded in saving the Bank but at a severe social cost — contributing "
            "to the political backlash against the Bank that Andrew Jackson would "
            "later exploit to destroy it.\n\n"
            "His career spans the formative period of American financial and political "
            "history — from the early republic through the Jacksonian era."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "American War Hawk congressman, Speaker of the House, and president of the Second Bank of the United States (1819–1823); his severe credit contraction saved the Bank but deepened the 1819 panic's distress — a central figure in the early republic's financial and political history.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The War of 1812 and the War Hawk faction's pressure for conflict with Britain over maritime rights — reflecting the aggressive nationalism of the post-1812 American South and West — drove his most visible congressional role",
            "The Panic of 1819 and the near-collapse of the Second Bank of the United States — resulting from its reckless lending during the post-war boom — created the crisis that brought him to the Bank presidency",
            "The early republic's lack of sophisticated financial regulation and the Bank's mismanagement under previous leadership created the institutional disaster he was brought in to address"
        ],
        "effects": [
            "His credit contraction as Bank president (1819–1823) stabilized the Second Bank of the United States — preventing its collapse — but deepened the Panic of 1819's impact on debtors, farmers, and state banks",
            "His War Hawk leadership contributed to the congressional push that produced the War of 1812 — including expanding the US Navy's capacity that would prove important in the conflict",
            "His Speakership of the House (briefly, after Clay resigned) placed him at the head of the legislative branch at a critical moment",
            "The political backlash against the Bank's contraction — which he implemented — contributed to the Jacksonian populism that would eventually destroy the Bank entirely in the 1830s"
        ],
        "relationships": [
            {"entity": "Second Bank of the United States", "relationship": "PRESIDENT_OF", "note": "President of the Second Bank of the United States (1819–1823); implemented severe credit contraction to stabilize the near-collapsed institution"},
            {"entity": "War of 1812", "relationship": "CONTRIBUTED_TO_OUTBREAK_OF", "note": "A leading War Hawk congressman whose Committee on Naval Affairs leadership helped prepare the republic for the War of 1812"},
            {"entity": "US House of Representatives", "relationship": "SPEAKER_OF", "note": "Served briefly as Speaker of the House of Representatives — succeeding Henry Clay who resigned to join the peace negotiations"},
            {"entity": "Henry Clay", "relationship": "SUCCEEDED_AS_SPEAKER", "note": "Succeeded Henry Clay as Speaker when Clay resigned to join the peace negotiating team that concluded the War of 1812"},
            {"entity": "Panic of 1819 (US financial crisis)", "relationship": "MANAGED_INSTITUTIONAL_RESPONSE_TO", "note": "Appointed Bank president during the Panic of 1819; his credit contraction addressed the Bank's crisis while deepening the national economic distress"}
        ]
    }),

    # 5 — John P. Kennedy
    ("john-p-kennedy", {
        "summary": (
            "John Pendleton Kennedy (1795–1870) was an American novelist, lawyer, Whig "
            "politician, and statesman from Maryland who combined a distinguished literary "
            "career with substantial public service — including serving as US Secretary "
            "of the Navy (1852–1853) under President Millard Fillmore, as a Maryland "
            "Congressman, and as an influential advocate for federal investment in "
            "scientific exploration and technological innovation, including his support "
            "for Samuel Morse's telegraph and Charles Wilkes's US Exploring Expedition. "
            "He is one of the few significant figures in 19th-century American public "
            "life to have made lasting contributions to both literature and statecraft.\n\n"
            "As a novelist, Kennedy is best remembered for Swallow Barn (1832) — a "
            "romanticized portrayal of Virginia plantation life — and Horse-Shoe Robinson "
            "(1835), a Revolutionary War novel that was widely read and influenced "
            "subsequent American historical fiction. His literary work was embedded in "
            "the Southern Whig tradition that sought to reconcile regional cultural "
            "identity with American nationalism, and his fiction helped construct the "
            "romanticized image of the antebellum South that both appealed to contemporary "
            "readers and has been criticized by later historians as whitewashing slavery.\n\n"
            "His most consequential government act was as Navy Secretary: he authorized "
            "Matthew Perry's expedition to Japan (1852–1854) — the diplomatic mission "
            "that forced Japan's opening to Western commerce through the threat of "
            "American naval power, ending Japan's two centuries of relative isolation "
            "and beginning the process that would lead to the Meiji Restoration. This "
            "single executive decision placed him at the origin of one of the most "
            "consequential diplomatic and historical transformations of the 19th century.\n\n"
            "His earlier congressional advocacy for Samuel Morse's telegraph — securing "
            "federal funding for the first telegraph line in 1843 — helped launch the "
            "communications revolution that transformed 19th-century American society."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "US Secretary of the Navy (1852–53) who authorized Matthew Perry's Japan expedition — opening Japan to Western commerce; Maryland Congressman who secured federal funding for Morse's telegraph; also a significant American novelist (Swallow Barn, 1832).",
            "significanceCategory": "continental"
        },
        "causes": [
            "The United States' commercial and strategic interest in the Pacific — including trade with China and whaling operations that needed Japanese ports — drove the Navy Department's planning for a Japan expedition",
            "American Whig political culture's embrace of internal improvements, technological investment, and commercial expansion created the ideological framework within which Kennedy's advocacy for telegraphs and scientific expeditions was rooted",
            "The Southern literary tradition and the antebellum romanticization of plantation life shaped the literary content of his novels — embedded in his Chesapeake Maryland political and social world"
        ],
        "effects": [
            "His authorization of Matthew Perry's Japan expedition (1852) led directly to the Convention of Kanagawa (1854) — opening Japan to Western commerce and beginning the transformation that produced the Meiji Restoration",
            "His congressional advocacy secured federal funding for Samuel Morse's first telegraph line in 1843 — contributing to the launch of the communications revolution that transformed American society",
            "His novels (Swallow Barn, 1832) helped construct the romanticized image of antebellum Virginia plantation life — contributing to the cultural representation of the slaveholding South",
            "His support for the US Wilkes Exploring Expedition (1838–1842) contributed to the expansion of American scientific and geographic knowledge of the Pacific"
        ],
        "relationships": [
            {"entity": "Matthew Perry's Japan Expedition (1852–1854)", "relationship": "AUTHORIZED", "note": "As Navy Secretary, authorized Matthew Perry's expedition that opened Japan to Western commerce through the threat of naval power"},
            {"entity": "Samuel Morse / US telegraph system", "relationship": "SECURED_FEDERAL_FUNDING_FOR", "note": "As Congressman, advocated for and secured federal funding for Morse's first telegraph line in 1843 — helping launch the communications revolution"},
            {"entity": "President Millard Fillmore", "relationship": "SERVED_UNDER_AS_NAVY_SECRETARY", "note": "Served as Secretary of the Navy (1852–1853) in President Fillmore's administration"},
            {"entity": "Swallow Barn (novel, 1832)", "relationship": "AUTHORED", "note": "Author of Swallow Barn — a significant early American novel romanticizing Virginia plantation life"},
            {"entity": "American Whig Party", "relationship": "POLITICIAN_OF", "note": "A Maryland Whig politician whose public career expressed Whig values of internal improvements, commerce, and scientific investment"}
        ]
    }),

    # 6 — John Harvie
    ("john-harvie", {
        "summary": (
            "John Harvie (1742–1807) was a Virginia lawyer, planter, and Founding Father "
            "who served as a delegate to the Second Continental Congress (1777–1778), "
            "where he signed the Articles of Confederation — the first constitutional "
            "framework of the United States — and served as the fourth mayor of "
            "Richmond, Virginia. His career at the intersection of colonial and "
            "revolutionary Virginia society illustrates the networks of personal "
            "connection, land, and law that defined Virginia's Founding generation.\n\n"
            "Harvie's family connections were remarkable: his father, Colonel John "
            "Harvie Sr., was Thomas Jefferson's guardian following the death of "
            "Jefferson's father Peter, making the younger Harvie a childhood friend "
            "and lifelong associate of the Declaration's author. Jefferson and Harvie "
            "moved in the same elite Virginia legal and planter circles, and Harvie's "
            "career exemplifies the integration of legal practice, plantation ownership, "
            "land speculation, and political service that characterized the Virginia "
            "gentry class that dominated early American politics.\n\n"
            "His service in the Continental Congress came at a critical moment — 1777 "
            "was the year of Valley Forge, Burgoyne's surrender at Saratoga, and the "
            "drafting of the Articles of Confederation, the first formal constitution "
            "of the United States. His signature on the Articles placed him among the "
            "founders of the constitutional framework that governed the United States "
            "until the Constitution of 1787 replaced it. As mayor of Richmond — which "
            "became Virginia's capital in 1780 — he participated in the local governance "
            "of a city that would become central to Virginia and later Confederate history.\n\n"
            "He also conducted negotiations with Native American peoples — a dimension "
            "of early Virginia political life that reflects both the frontier character "
            "of colonial Virginia and the complex land relations between colonists "
            "and Native communities."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Virginia Founding Father and signer of the Articles of Confederation (1777); childhood friend of Thomas Jefferson; fourth Mayor of Richmond; a representative figure of the Virginia gentry class that shaped early American politics.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The American Revolution and the Continental Congress's need for delegates from Virginia — the largest and most politically influential of the colonies — brought Harvie into national politics",
            "The Virginia gentry class's integration of law, land, and politics — the social system of the tobacco-plantation economy — formed the social world in which his career was embedded",
            "His family's close connection to the Jefferson family — his father as Jefferson's guardian — gave him personal and professional ties to the most influential figure in Virginia revolutionary politics"
        ],
        "effects": [
            "His signature on the Articles of Confederation placed him among the formal founders of the first US constitutional framework — the legal basis of the United States government until the 1787 Constitution",
            "His mayoral service in Richmond contributed to the governance of what would become Virginia's capital city during the Revolutionary period",
            "His diplomatic negotiations with Native American peoples contributed to the early republic's land relations with Native communities in Virginia's frontier regions",
            "As a childhood friend and associate of Thomas Jefferson, his personal and professional networks were embedded in the founding generation's most significant relationships"
        ],
        "relationships": [
            {"entity": "Second Continental Congress", "relationship": "DELEGATE_TO", "note": "Delegate to the Second Continental Congress (1777–1778); signed the Articles of Confederation"},
            {"entity": "Articles of Confederation", "relationship": "SIGNED", "note": "Signed the Articles of Confederation — the first constitutional framework of the United States — in 1777"},
            {"entity": "Thomas Jefferson", "relationship": "CHILDHOOD_FRIEND_AND_ASSOCIATE_OF", "note": "His father was Jefferson's guardian after Jefferson's father died; he and Jefferson were childhood friends and lifelong associates"},
            {"entity": "Richmond, Virginia", "relationship": "FOURTH_MAYOR_OF", "note": "Fourth Mayor of Richmond, Virginia — which became the state capital in 1780"},
            {"entity": "Virginia gentry class (Founding era)", "relationship": "MEMBER_OF", "note": "A representative member of the Virginia planter-lawyer gentry class that dominated the founding generation of American politics"}
        ]
    }),

    # 7 — Thomas Todd
    ("thomas-todd", {
        "summary": (
            "Thomas Todd (1765–1826) was an American lawyer and jurist who served as "
            "an Associate Justice of the Supreme Court of the United States from 1807 "
            "to 1826 — appointed by President Thomas Jefferson as one of the first "
            "justices from the trans-Appalachian western states, representing the "
            "expanding frontier West in an era when Kentucky's admission as a state "
            "(1792) had begun the process of incorporating the west into the national "
            "political system. His 19-year tenure on the Court produced only a handful "
            "of written opinions, leading contemporaries to describe him as one of "
            "the Court's less active members — a description that may reflect both "
            "the limited opportunity he had to write (the Court handled fewer cases "
            "than later) and his frequent absences due to the difficulty of traveling "
            "from Kentucky to Washington.\n\n"
            "Before joining the Supreme Court, Todd had built a substantial legal "
            "career in Kentucky — a frontier state that was generating enormous "
            "volumes of land title litigation as the competing claims of Virginia "
            "land grants, pre-emption rights, and Native American territories "
            "were sorted out through the courts. He served as clerk to the Kentucky "
            "legislature and then as a judge on the Kentucky Court of Appeals, rising "
            "to Chief Justice of that court before Jefferson elevated him to the "
            "Supreme Court. His deep expertise in land law — from his Kentucky experience "
            "— was his most distinctive professional contribution.\n\n"
            "His handful of Supreme Court opinions dealt substantially with land "
            "title questions — a legal domain of enormous practical importance in "
            "an era when the settlement of the American West depended on resolving "
            "overlapping and contradictory land claims from colonial-era grants, "
            "state grants, and congressional land ordinances.\n\n"
            "He was the first Supreme Court Justice from west of the Appalachians — "
            "a geographical milestone reflecting the Court's gradual incorporation "
            "of the expanding republic."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Associate Justice of the US Supreme Court (1807–1826); the first Justice from west of the Appalachians; a Kentucky land law expert whose Court service represented the frontier West's entry into the federal judicial system.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Kentucky's admission as a state (1792) and the enormous volume of land title litigation it generated — as competing claims from Virginia grants, pre-emption rights, and federal ordinances collided — shaped Todd's legal expertise and career",
            "President Jefferson's desire to represent the trans-Appalachian West on the Supreme Court — reflecting the political importance of the frontier states to Jeffersonian Republican politics — drove Todd's appointment",
            "The Kentucky Court of Appeals experience Todd brought — as Chief Justice of Kentucky's highest court — provided the judicial record that justified his elevation to the national bench"
        ],
        "effects": [
            "His Supreme Court appointment made him the first Justice from west of the Appalachians — establishing the precedent that the frontier states would be represented on the national court",
            "His opinions on land law questions — drawn from his deep Kentucky expertise — contributed to the development of federal jurisprudence on the land title disputes that were central to western settlement",
            "His 19-year tenure provided continuity on the Marshall Court — the most consequential period in early American constitutional history — even if his written contribution was limited",
            "His career model — from frontier lawyer to state judge to Supreme Court Justice — established a pathway for western legal talent to reach the national bench"
        ],
        "relationships": [
            {"entity": "US Supreme Court (Marshall Court era)", "relationship": "ASSOCIATE_JUSTICE_OF", "note": "Associate Justice of the US Supreme Court (1807–1826); part of the Marshall Court — the most constitutionally formative era in early American judicial history"},
            {"entity": "President Thomas Jefferson", "relationship": "APPOINTED_BY", "note": "Appointed to the Supreme Court by President Jefferson in 1807 — as one of Jefferson's few Supreme Court appointments"},
            {"entity": "Kentucky Court of Appeals", "relationship": "FORMER_CHIEF_JUSTICE_OF", "note": "Served as Chief Justice of the Kentucky Court of Appeals before his elevation to the Supreme Court"},
            {"entity": "Kentucky land title litigation", "relationship": "EXPERT_IN", "note": "His legal expertise was in land law — the dominant legal issue in frontier Kentucky generated by competing land grant claims"},
            {"entity": "Trans-Appalachian western states (US)", "relationship": "FIRST_JUDICIAL_REPRESENTATIVE_OF", "note": "The first Supreme Court Justice from west of the Appalachian Mountains — representing the frontier West's incorporation into national legal institutions"}
        ]
    }),

    # 8 — Mary Ekpere-Eta
    ("mary-ekpere-eta", {
        "summary": (
            "Mary Ekpere-Eta is a Nigerian barrister, women's rights activist, and public "
            "administrator who serves as Director General of the National Centre for Women "
            "Development (NCWD) in Abuja — the Nigerian federal institution mandated to "
            "promote gender equality, women's economic empowerment, and women's political "
            "participation across Nigeria's federal and state systems. As DG of the NCWD, "
            "she leads the institutional embodiment of Nigeria's commitment to the "
            "Beijing Platform for Action and related international women's development "
            "frameworks, translating these global commitments into national programs.\n\n"
            "The National Centre for Women Development was established in 1986 and has "
            "operated as the federal government's principal institutional vehicle for "
            "women's development policy — conducting research, advocacy, training, and "
            "program implementation on issues ranging from women's economic participation "
            "and education to gender-based violence prevention and women's political "
            "representation. Its mandate spans all 36 states and the FCT, making it "
            "a national institution with significant reach into the diversity of "
            "Nigeria's social and cultural landscape.\n\n"
            "Ekpere-Eta's legal training as a barrister provides the professional "
            "foundation for her administrative leadership of a center whose work "
            "necessarily engages legal frameworks — the Violence Against Persons "
            "Prohibition Act, the Child Rights Act, marriage and family law, and "
            "the constitutional equality guarantees that define the formal framework "
            "within which women's development work operates.\n\n"
            "Her career represents the pathway of the legally trained woman who moves "
            "from legal practice into public institutional leadership in the government "
            "sector — using legal expertise in service of broader social change "
            "within government rather than through civil society advocacy."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Nigerian barrister and Director General of the National Centre for Women Development (NCWD) in Abuja — the federal government's principal institution for women's economic empowerment, gender equality, and political participation programs across Nigeria.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Nigeria's ratification of the Convention on the Elimination of All Forms of Discrimination Against Women (CEDAW) and endorsement of the Beijing Platform for Action created the international framework that the NCWD — which she leads — is mandated to implement",
            "Nigeria's pervasive gender inequality — in economic participation, education, political representation, and violence against women — created the development agenda that the NCWD addresses",
            "Her legal training as a barrister provided the professional foundation for public institutional leadership in a center whose work is necessarily embedded in legal frameworks and rights-based approaches"
        ],
        "effects": [
            "Her DG leadership of the NCWD shapes the federal government's institutional approach to women's development — setting programmatic priorities, coordinating with state-level women's development centers, and implementing national gender policies",
            "Her work has contributed to Nigeria's reporting on and implementation of its international gender equality commitments (CEDAW, Beijing Platform, SDG 5)",
            "The NCWD's programs on women's economic empowerment, political participation, and gender-based violence prevention reach women across Nigeria's 36 states under her institutional direction",
            "Her career model — a legally trained woman who uses that training in senior government institutional leadership — contributes to the representation of women in senior federal government positions"
        ],
        "relationships": [
            {"entity": "National Centre for Women Development (NCWD)", "relationship": "DIRECTOR_GENERAL_OF", "note": "Director General of the NCWD — the Nigerian federal government's principal institution for women's development, gender equality, and empowerment programs"},
            {"entity": "Federal Ministry of Women Affairs (Nigeria)", "relationship": "REPORTS_TO", "note": "The NCWD she leads operates under the Federal Ministry of Women Affairs as Nigeria's principal women's development institution"},
            {"entity": "CEDAW (Convention on the Elimination of All Forms of Discrimination Against Women)", "relationship": "IMPLEMENTS_NATIONAL_COMMITMENTS_TO", "note": "Her institutional work implements Nigeria's international gender equality commitments, including CEDAW and the Beijing Platform for Action"},
            {"entity": "Violence Against Persons Prohibition (VAPP) Act Nigeria", "relationship": "WORKS_WITHIN_FRAMEWORK_OF", "note": "The NCWD's GBV prevention programs operate within the legal framework of Nigeria's VAPP Act"},
            {"entity": "Nigerian women's institutional development sector", "relationship": "LEADER_IN", "note": "As DG of the principal federal women's development institution, she is a key figure in Nigeria's institutional gender equality sector"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 25)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
