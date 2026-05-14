#!/usr/bin/env python3
"""
Batch 56 — 8 entities: Pierre Philippeaux, William Cox Ellis,
Charles Douglas 3rd Duke of Queensberry, Dominique-Joseph Garat,
Erasmus Finx, Gustave Chaix d'Est-Ange, James Iredell Jr., James Lisle Gillis
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

    # 1 — Pierre Philippeaux
    ("pierre-philippeaux", {
        "summary": (
            "Pierre Philippeaux (1756–1794) was a French "
            "lawyer and Dantonist Revolutionary politician "
            "who served in the National Convention and "
            "became one of the Indulgents — the faction "
            "around Georges Danton that advocated "
            "moderation, an end to the Terror, and "
            "negotiated peace with France's enemies — "
            "a position that led directly to his "
            "arrest, trial, and execution on the "
            "guillotine alongside Danton in April 1794. "
            "His career traced the arc from early "
            "revolutionary commitment through political "
            "opposition to the Committee of Public Safety "
            "and execution under the very Terror he "
            "had helped establish.\n\n"
            "Philippeaux was born in Le Mans and trained "
            "as a lawyer before 1789. The Revolution "
            "drew him into politics as a representative "
            "of the Sarthe department — one of the "
            "western departments on the frontier of "
            "the Vendée, the great counter-revolutionary "
            "Catholic royalist uprising that consumed "
            "western France from 1793 onward.\n\n"
            "His experience in the Vendée — where he "
            "was sent as a représentant en mission — "
            "made him a critic of the military commanders "
            "directing the brutal republican repression. "
            "His pamphlets attacking the generals "
            "and the Committee's mismanagement of "
            "the Vendée war earned him enemies "
            "among the radical Jacobins.\n\n"
            "When he aligned with the Dantonists "
            "calling for moderation and an end "
            "to the Terror, he sealed his fate. "
            "He was arrested in March 1794, tried "
            "before the Revolutionary Tribunal, "
            "and executed with Danton on 5 April 1794."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "French Dantonist politician and member of the National Convention; représentant en mission in the Vendée who became a critic of the Terror's military management; executed alongside Danton in April 1794 as an Indulgent; his career traced the fatal arc from revolutionary commitment to opposition to the Committee of Public Safety.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The radical Jacobin Committee of Public Safety's intensification of the Terror — which eliminated moderate voices, suppressed political criticism, and prosecuted anyone who questioned the Revolutionary government's military and political management — created the environment in which Philippeaux's pamphlets criticizing the Vendée commanders became acts of political suicide",
            "The Vendée counter-revolution (1793–1796) — the massive Catholic royalist uprising in western France that threatened to destroy the Republic — confronted Philippeaux as représentant en mission with the brutal realities of republican military repression and convinced him that the war was being mismanaged by self-serving generals",
            "Georges Danton's Indulgent faction — which argued that the Terror had gone too far, that peace negotiations were necessary, and that revolutionary moderation was both morally justified and strategically wise — provided the political home in which Philippeaux aligned himself against the Robespierrist Committee of Public Safety"
        ],
        "effects": [
            "His execution alongside Danton on 5 April 1794 was part of the elimination of the Dantonist faction — the last significant moderate grouping within the Convention capable of challenging the Committee of Public Safety — which cleared the way for the most extreme phase of the Terror before Thermidor",
            "His pamphlets criticizing the Vendée military commanders contributed to the public debate about the Republic's management of the counter-revolution — a debate that, while suppressed during the Terror, documented the brutality and mismanagement that historians later used to analyze the republican repression",
            "His fate illustrated the fatal logic of the Terror: the same radical commitment that had driven Philippeaux to support revolutionary policies could be turned against him when his criticism of those policies made him a target — no revolutionary was safe from the Revolutionary Tribunal",
            "His alignment with Danton placed him among the historical moderates of the French Revolution — figures who argued, unsuccessfully, that revolutionary ideals could be better served by peace than by endless Terror — making him a figure of retrospective sympathy in the historiography of the Revolution"
        ],
        "relationships": [
            {"target": "georges-danton", "verb": "ALLIED_WITH", "note": "Member of the Dantonist Indulgent faction"},
            {"target": "national-convention", "verb": "SERVES_IN", "note": "Deputy of the National Convention"},
            {"target": "committee-of-public-safety", "verb": "OPPOSES", "note": "Critic of Robespierre's Committee who was executed"},
            {"target": "vendee-war", "verb": "MISSION_IN", "note": "Représentant en mission criticizing Vendée military management"},
            {"target": "french-revolution-terror", "verb": "VICTIM_OF", "note": "Executed on the guillotine April 5, 1794"}
        ]
    }),

    # 2 — William Cox Ellis
    ("william-cox-ellis", {
        "summary": (
            "William Cox Ellis (1787–1871) was an American "
            "lawyer and Democratic politician from "
            "Pennsylvania who served in the U.S. House "
            "of Representatives (1823–1825), representing "
            "a Pennsylvania district during the late "
            "Jeffersonian era. His brief congressional "
            "service came during the Era of Good Feelings "
            "and the transition toward the Jacksonian "
            "party realignment — a moment when the "
            "old Democratic-Republican Party was "
            "fracturing into competing factions "
            "that would eventually become the "
            "Jacksonian Democrats and the Adams-Clay "
            "National Republicans.\n\n"
            "Ellis was born in Pennsylvania and built "
            "a legal career before entering Congress. "
            "His single term in the House (1823–1825) "
            "coincided with the extraordinary presidential "
            "election of 1824 — the 'corrupt bargain' "
            "election in which Andrew Jackson won "
            "the most popular and electoral votes "
            "but lost the presidency to John Quincy "
            "Adams through the contingent election "
            "in the House of Representatives. This "
            "election and its aftermath defined "
            "the partisan environment of Ellis's "
            "congressional service.\n\n"
            "His Pennsylvania background placed him "
            "in a state that was politically contested "
            "between the emerging Jacksonian Democratic "
            "coalition and the Adams-Clay National "
            "Republicans — Pennsylvania's industrial "
            "and agricultural interests were divided "
            "between tariff protection (which Clay's "
            "American System offered) and Jacksonian "
            "populism.\n\n"
            "His career represented the transitional "
            "politics of the mid-1820s."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Pennsylvania Democratic-Republican Congressman (1823–1825) serving during the Era of Good Feelings' collapse and the 1824 'corrupt bargain' election; representative of the transitional politics as the first American party system gave way to the Jacksonian era.",
            "significanceCategory": "local"
        },
        "causes": [
            "The Era of Good Feelings and the collapse of Federalist opposition — which concentrated power within the Democratic-Republican Party and made Pennsylvania Congressional seats competitive within single-party factional contests — created the political environment in which Ellis won his House seat",
            "The 1824 presidential election and the 'corrupt bargain' controversy — in which Adams's selection by the House over popular-vote leader Jackson enraged Jacksonian supporters and created the factional split that produced the second American party system — defined the political drama of Ellis's congressional term",
            "Pennsylvania's complex economic interests — combining growing industrial manufacturing in the east with agricultural interests in the west, all dependent on federal tariff policy — shaped the political calculations of Pennsylvania congressmen like Ellis who had to navigate between competing economic constituencies"
        ],
        "effects": [
            "His congressional service contributed to Pennsylvania's representation in the federal debates of the early 1820s — including tariff policy, internal improvements, and the emerging sectional tensions that the Missouri Compromise of 1820 had not permanently resolved",
            "His single-term career illustrated the political volatility of the transitional 1823–1825 period — when the old party system was dissolving and congressmen who had entered politics as Democratic-Republicans found themselves having to choose between Jackson and Adams factions",
            "His career contributed to the development of Pennsylvania's Democratic political tradition that aligned with Jacksonian populism — a tradition that made Pennsylvania a key swing state in the presidential elections of the 1820s–1840s",
            "His post-congressional legal career in Pennsylvania contributed to the state's legal profession during a period of rapid economic development and the growing complexity of commercial and property law that Pennsylvania's industrialization required"
        ],
        "relationships": [
            {"target": "us-house-of-representatives", "verb": "SERVES_IN", "note": "Pennsylvania Congressman 1823–1825"},
            {"target": "democratic-republican-party", "verb": "MEMBER_OF", "note": "Democratic-Republican transitioning to Jacksonian era"},
            {"target": "election-of-1824", "verb": "SERVES_DURING", "note": "Congressman during the corrupt bargain presidential election"},
            {"target": "pennsylvania", "verb": "REPRESENTS", "note": "Pennsylvania district Congressional representative"},
            {"target": "andrew-jackson", "verb": "SUPPORTS", "note": "Pennsylvania Democrat aligned with Jacksonian populism"}
        ]
    }),

    # 3 — Charles Douglas, 3rd Duke of Queensberry
    ("charles-douglas-3rd-duke-of-queensberry", {
        "summary": (
            "Charles Douglas, 3rd Duke of Queensberry "
            "(1698–1778), was a Scottish nobleman "
            "who served as a Scottish representative "
            "peer in the British Parliament and as "
            "a figure at the Hanoverian court. He "
            "is best remembered as the patron of "
            "the poet John Gay — providing the "
            "financial and social support that "
            "allowed Gay to continue his literary "
            "work after his satirical masterpiece "
            "The Beggar's Opera (1728) made him "
            "simultaneously famous and politically "
            "targeted. His wife Catherine Hyde, "
            "Duchess of Queensberry, was among "
            "the most celebrated social figures "
            "of the era and a central figure "
            "in Gay's circle.\n\n"
            "The Queensberry dukedom was one of "
            "Scotland's most ancient and distinguished "
            "noble titles, and Charles Douglas "
            "inherited its social prestige while "
            "also adapting to the post-1707 reality "
            "of Union with England. His family's "
            "prominence in Scottish society made "
            "his Queensberry House in Edinburgh "
            "a center of aristocratic culture.\n\n"
            "His wife's championing of John Gay — "
            "whose Beggar's Opera was a savage "
            "satire on Walpole's government and "
            "the corruptions of political life "
            "— brought the Queensberrys into "
            "political tension with the Walpole "
            "administration, which briefly "
            "barred the Duchess from court.\n\n"
            "The couple's literary patronage "
            "placed them among the most important "
            "cultural patrons of Georgian England's "
            "Augustan literary culture."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Scottish nobleman and patron of John Gay; 3rd Duke of Queensberry who, with his wife Catherine Hyde, provided essential support to the author of The Beggar's Opera (1728) against Walpole's political pressure; Scottish representative peer in post-Union Britain; important figure in the cultural patronage networks of Georgian England.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The patronage system of Georgian England — in which wealthy aristocrats supported poets, playwrights, and artists financially and socially in exchange for dedication of works and cultural prestige — made Charles Douglas and his wife Catherine Hyde essential supporters for John Gay once the political controversy around The Beggar's Opera made official court patronage unavailable",
            "The Beggar's Opera's satirical attack on Robert Walpole's government (1728) — which was enormously popular but politically controversial — created the situation in which Gay needed aristocratic protection against political retaliation, making the Queensberrys' friendship and patronage financially and socially essential",
            "The post-1707 Union between Scotland and England — which created Scottish representative peers as the mechanism for Scottish noble participation in the British Parliament — defined Charles Douglas's political role as a Scottish nobleman operating within the new British constitutional framework"
        ],
        "effects": [
            "His and his wife's patronage of John Gay allowed the poet to continue working and living comfortably after the political controversy of The Beggar's Opera — contributing to Gay's later works and sustaining one of the most important satirical voices of the Georgian Augustan literary period",
            "The Queensberry household's cultural and social standing gave Gay access to the highest levels of aristocratic society — a social position that supported both his creative work and his personal well-being after the difficulties the Beggar's Opera created",
            "The political tension between the Queensberrys and the Walpole administration over Gay's patronage — leading to the Duchess's brief exclusion from court — illustrated how aristocratic cultural patronage could intersect with political conflict in eighteenth-century England",
            "The couple's fame as Gay's patrons gave them a lasting place in English literary history — their names preserved in the literary biography of one of the era's most celebrated poets"
        ],
        "relationships": [
            {"target": "john-gay", "verb": "PATRONIZES", "note": "Essential patron of the Beggar's Opera author"},
            {"target": "catherine-hyde-duchess-of-queensberry", "verb": "MARRIED_TO", "note": "Husband of the celebrated patroness and socialite"},
            {"target": "beggar's-opera", "verb": "SUPPORTS_AUTHOR_OF", "note": "Patron when Walpole's government targeted Gay"},
            {"target": "robert-walpole", "verb": "OPPOSES", "note": "Aristocratic patron opposed to Walpole's political persecution of Gay"},
            {"target": "british-parliament", "verb": "SERVES_IN", "note": "Scottish representative peer in the House of Lords"}
        ]
    }),

    # 4 — Dominique-Joseph Garat
    ("dominique-joseph-garat", {
        "summary": (
            "Dominique-Joseph Garat (1749–1833) was a "
            "French philosophe, journalist, and politician "
            "whose career spanned the Ancien Régime, "
            "the French Revolution, the Consulate, "
            "and the Restoration — a remarkable "
            "survival across the successive political "
            "regimes that destroyed so many of his "
            "contemporaries. A noted writer and "
            "intellectual of the Enlightenment tradition, "
            "he served as Minister of the Interior "
            "and Minister of Justice under the "
            "Revolutionary government and is "
            "remembered above all for the "
            "devastating personal task of "
            "informing Louis XVI that the National "
            "Convention had condemned him to death.\n\n"
            "Born in the Basque country, Garat "
            "was educated in Paris and established "
            "himself as a writer and journalist — "
            "contributing to the Encyclopédie méthodique "
            "and the Journal de Paris before 1789. "
            "He was elected to the Estates-General "
            "and the National Assembly, where he "
            "participated in the constitutional "
            "debates of the early Revolution.\n\n"
            "As Minister of Justice and Interior "
            "under the First Republic, Garat "
            "was the official who read the death "
            "sentence to Louis XVI on the eve "
            "of his execution (January 1793) — "
            "a moment he described in haunting "
            "detail in his memoirs. He survived "
            "the Terror and continued his career "
            "under Napoleon, receiving a senatorship.\n\n"
            "His philosophical writings on the theory "
            "of ideas connected him to Condillac's "
            "sensationalist tradition."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "French Enlightenment philosophe and politician who served as Minister of the Interior and Justice under the Revolution; the official who informed Louis XVI of his death sentence (January 1793); survivor of the Terror, Senator under Napoleon, member of the Institut de France; writer in the Condillacian philosophical tradition who spanned all regimes from Ancien Régime to Restoration.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The French Enlightenment's creation of a class of professional writers, journalists, and philosophes — who combined philosophical writing with journalism, political commentary, and public intellectual roles — formed Garat as both a thinker and a political operative who was drawn into Revolutionary politics when his intellectual credentials made him useful to the new regime",
            "The French Revolution's transformation of the philosophes' abstract constitutional theories into practical governance — requiring intellectuals like Garat to take on ministerial roles for which their philosophical training ill-prepared them — placed him as Minister of Justice at the moment of Louis XVI's execution",
            "The Terror's logic of political survival — which required intellectual politicians who had served in compromised positions to constantly prove their revolutionary credentials — shaped Garat's cautious navigation of the period that killed so many of his contemporaries"
        ],
        "effects": [
            "His delivery of the death sentence to Louis XVI — reading the Convention's condemnation to the king on 19 January 1793 — made him an eyewitness to and participant in one of the most symbolically charged moments of the French Revolution, and his later written account became an important historical document",
            "His ministerial service contributed to the Revolutionary government's administrative machinery during the Terror — helping manage the Interior and Justice departments during the period of maximum political violence",
            "His survival through the Terror and continued career under Napoleon — receiving a Senate seat and membership in the Institut de France — demonstrated the capacity of flexible intellectuals to adapt to successive regimes, a survival that provided continuity between Revolutionary and Napoleonic administrative culture",
            "His philosophical writings in the Condillacian tradition contributed to the late Enlightenment's development of sensationalist epistemology — the theory that all knowledge derives from sensory experience — that influenced the Idéologues who shaped early Napoleonic cultural policy"
        ],
        "relationships": [
            {"target": "louis-xvi", "verb": "DELIVERS_DEATH_SENTENCE_TO", "note": "Minister of Justice who read the death sentence to Louis XVI"},
            {"target": "french-revolution", "verb": "SERVES_IN", "note": "Minister of Interior and Justice under the Republic"},
            {"target": "national-convention", "verb": "SERVES_UNDER", "note": "Ministerial official under the Revolutionary Convention"},
            {"target": "napoleon-bonaparte", "verb": "SERVES_UNDER", "note": "Senator under the Napoleonic regime"},
            {"target": "condillac-enlightenment", "verb": "EXTENDS", "note": "Philosopher in the sensationalist tradition of Condillac"}
        ]
    }),

    # 5 — Erasmus Finx
    ("erasmus-finx", {
        "summary": (
            "Erasmus Finx (1649–1714) was a German "
            "jurist and legal scholar who contributed "
            "to the development of German legal science "
            "in the late seventeenth and early eighteenth "
            "centuries. Working within the tradition "
            "of German academic jurisprudence — which "
            "combined Roman civil law with the emerging "
            "body of natural law theory — Finx "
            "produced legal writings that engaged "
            "with the foundational questions of "
            "law, obligation, and sovereignty that "
            "preoccupied the Holy Roman Empire's "
            "lawyers in the aftermath of the "
            "Thirty Years' War.\n\n"
            "Finx was trained in the German university "
            "tradition of academic law — the faculties "
            "of law at German universities that trained "
            "the jurists who staffed the imperial "
            "courts, the territorial chanceries, "
            "and the councils of the German princes. "
            "His academic career placed him within "
            "the learned legal culture of the "
            "Holy Roman Empire.\n\n"
            "The period of Finx's career — the decades "
            "after the Peace of Westphalia (1648) — "
            "was a formative era for German legal "
            "thought. The peace settlement had "
            "established new principles of religious "
            "toleration and territorial sovereignty "
            "that required legal systematization. "
            "Natural law theorists from Grotius "
            "and Pufendorf onward were transforming "
            "the legal-philosophical landscape "
            "in which Finx worked.\n\n"
            "His scholarly output contributed to "
            "the dense literature of German academic "
            "jurisprudence that shaped the training "
            "of lawyers across the Holy Roman Empire."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "German jurist and legal scholar working in the post-Westphalia era of German legal development; contributed to the academic jurisprudence that trained lawyers across the Holy Roman Empire; worked at the intersection of Roman civil law and emerging natural law theory in the formative decades of German legal science.",
            "significanceCategory": "local"
        },
        "causes": [
            "The Peace of Westphalia (1648) and its establishment of new principles of religious toleration, territorial sovereignty, and imperial law — requiring systematic legal explanation and integration into the existing Roman-canonical legal framework — created the jurisprudential challenges that engaged German legal scholars of Finx's generation",
            "The natural law revolution in European jurisprudence — from Grotius's De Jure Belli ac Pacis (1625) through Pufendorf's systematization of natural law — transformed the theoretical foundations of German legal science and provided the intellectual framework within which Finx's legal writings engaged with questions of obligation and sovereignty",
            "The Holy Roman Empire's system of academic legal education — in which university law faculties trained the bureaucratic and judicial personnel for hundreds of territorial governments — created the institutional demand for legal textbooks, commentaries, and dissertations that German academic jurists like Finx supplied"
        ],
        "effects": [
            "His legal writings contributed to the academic jurisprudential literature that trained German lawyers — the dense, learned output of German law faculties that systematized Roman, canonical, and natural law into the practical legal knowledge required by imperial courts and territorial governments",
            "His work contributed to the development of German legal science in the post-Westphalia era — the systematic elaboration of the legal principles governing the Holy Roman Empire's complex constitutional order",
            "His career illustrated the important but largely anonymous role of second-rank academic jurists in building the legal culture of the Holy Roman Empire — men whose detailed scholarly work sustained the legal training system even if their individual contributions were overshadowed by the great systematizers like Pufendorf",
            "The tradition of academic jurisprudence he contributed to fed into the eighteenth-century German legal science that eventually produced Savigny's historical school — making the labors of less celebrated jurists like Finx part of the intellectual genealogy of modern German law"
        ],
        "relationships": [
            {"target": "holy-roman-empire", "verb": "SERVES_IN", "note": "German jurist within the imperial legal culture"},
            {"target": "german-jurisprudence", "verb": "CONTRIBUTES_TO", "note": "Academic legal writer in post-Westphalia Germany"},
            {"target": "natural-law-tradition", "verb": "ENGAGES_WITH", "note": "Jurist at intersection of Roman law and natural law theory"},
            {"target": "peace-of-westphalia-1648", "verb": "FOLLOWS_FROM", "note": "Legal scholar working in aftermath of Westphalia's legal settlement"},
            {"target": "samuel-pufendorf", "verb": "CONTEMPORARY_WITH", "note": "German jurist contemporary with the great natural law systematizers"}
        ]
    }),

    # 6 — Gustave Chaix d'Est-Ange
    ("gustave-chaix-dest-ange", {
        "summary": (
            "Gustave Chaix d'Est-Ange (1800–1876) was "
            "a French lawyer, jurist, and legal scholar "
            "who became one of the most eminent members "
            "of the Paris bar in the mid-nineteenth "
            "century — celebrated as a courtroom advocate "
            "and as a contributor to French civil law "
            "scholarship. His legal career spanned "
            "the July Monarchy, the Second Republic, "
            "the Second Empire, and the early Third "
            "Republic — an extraordinary longevity "
            "that gave him prominence across four "
            "distinct French political regimes.\n\n"
            "Chaix d'Est-Ange established himself "
            "as one of the leading civil lawyers "
            "of Paris — a city whose bar was the "
            "most prestigious in France and whose "
            "senior advocates commanded enormous "
            "social prestige and professional fees. "
            "His reputation as a courtroom advocate "
            "was built on cases involving "
            "the great civil, commercial, and "
            "political controversies of the era.\n\n"
            "He also served as President of the "
            "Conseil d'État under Napoleon III — "
            "the supreme administrative court that "
            "was both the highest court for administrative "
            "disputes and an advisory council to "
            "the executive. This appointment gave "
            "him authority over the central "
            "institution of French administrative law.\n\n"
            "His contributions to legal scholarship "
            "and the dignity of the French bar "
            "earned him election to the Académie "
            "des sciences morales et politiques."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Eminent French civil lawyer and President of the Conseil d'État under Napoleon III; one of the most celebrated advocates at the Paris bar across four political regimes; member of the Académie des sciences morales et politiques; contributor to French civil and administrative law in the mid-nineteenth century.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Paris bar's prestige as the premier legal institution in France — and its system of training brilliant advocates through apprenticeship and competition — provided the institutional pathway through which Chaix d'Est-Ange built the courtroom reputation that eventually made him one of its most celebrated members",
            "Napoleon III's Second Empire (1852–1870) and its transformation of French governmental institutions — which made the Conseil d'État a more powerful administrative body serving the imperial executive — created the position in which Chaix d'Est-Ange's combination of legal excellence and political reliability could earn him the Presidency of the Conseil",
            "The nineteenth century's elaboration of French civil law — the Napoleonic Code's application to an increasingly complex commercial and industrial society generating endless legal disputes — created the demand for sophisticated civil lawyers that Chaix d'Est-Ange supplied with distinction"
        ],
        "effects": [
            "His Presidency of the Conseil d'État shaped French administrative law during the critical Second Empire period — the institution whose decisions determined the boundaries between state power and individual rights in the world's most administratively centralized major state",
            "His Paris bar career contributed to the development of French courtroom advocacy in the mid-nineteenth century — helping establish the standards of forensic eloquence and legal argumentation that defined the Paris bar's reputation across Europe",
            "His election to the Académie des sciences morales et politiques recognized his contribution to French legal scholarship — connecting legal practice to the broader intellectual culture of French social science",
            "His career across four political regimes illustrated the capacity of distinguished French lawyers to maintain professional eminence regardless of political change — a pattern of legal continuity that provided institutional stability through the turbulent transitions of nineteenth-century French political life"
        ],
        "relationships": [
            {"target": "conseil-detat-france", "verb": "PRESIDES_OVER", "note": "President of the Conseil d'État under Napoleon III"},
            {"target": "napoleon-iii", "verb": "SERVES_UNDER", "note": "Senior legal official of the Second Empire"},
            {"target": "paris-bar", "verb": "LEADS", "note": "Eminent civil advocate at the Paris bar"},
            {"target": "academie-des-sciences-morales-et-politiques", "verb": "MEMBER_OF", "note": "Elected to leading French intellectual institution"},
            {"target": "french-civil-law", "verb": "ADVANCES", "note": "Major contributor to French civil law scholarship and advocacy"}
        ]
    }),

    # 7 — James Iredell Jr.
    ("james-iredell-jr", {
        "summary": (
            "James Iredell Jr. (1788–1853) was an American "
            "lawyer and politician from North Carolina "
            "who served as Governor of North Carolina "
            "(1827–1828) and as a U.S. Senator (1828–1831). "
            "Son of Associate Justice James Iredell Sr. — "
            "one of the original Supreme Court Justices "
            "appointed by President Washington in 1790 — "
            "James Iredell Jr. extended his father's "
            "distinguished legal family into the "
            "next generation's political life.\n\n"
            "Iredell Jr. was born in Edenton, North "
            "Carolina — the town where his father had "
            "practiced law and built his reputation "
            "as a colonial and early republican lawyer "
            "and Federalist statesman. He was educated "
            "at Princeton (then College of New Jersey) "
            "and the College of William and Mary "
            "before studying law and entering North "
            "Carolina's legal and political world.\n\n"
            "His governorship (1827–1828) and Senate "
            "service (1828–1831) placed him in North "
            "Carolina leadership during the transition "
            "from the Era of Good Feelings to the "
            "Jacksonian two-party system — a politically "
            "tumultuous period when the old "
            "Democratic-Republican coalition was "
            "fracturing and North Carolina was "
            "becoming a Jacksonian Democratic stronghold.\n\n"
            "He served as a Democrat — aligning with "
            "Jackson's states'-rights populism "
            "rather than the Adams-Clay National "
            "Republican tradition of his father's "
            "Federalist generation."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Governor of North Carolina (1827–1828) and U.S. Senator (1828–1831); son of Supreme Court Justice James Iredell Sr.; extended a distinguished legal and political family into the Jacksonian era; aligned with Jacksonian Democracy despite his Federalist father's legacy.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Iredell family's distinguished legal and political tradition — founded by Justice James Iredell Sr.'s service as one of Washington's original Supreme Court appointments — gave James Jr. both the social capital and the educational connections to build a political career in North Carolina's governing class",
            "North Carolina's transition to Jacksonian Democracy — as the state's voters aligned with Andrew Jackson's populist coalition rather than the Adams-Clay National Republicans — defined the partisan environment in which Iredell Jr. built his political career as a Democrat despite his Federalist family heritage",
            "The Edenton, North Carolina legal and social world — where the Iredell family was deeply embedded in the state's eastern planter-lawyer culture — provided the professional base and political connections from which James Jr. launched his gubernatorial and Senate careers"
        ],
        "effects": [
            "His governorship contributed to North Carolina's executive governance during the critical transition period between the Era of Good Feelings and Jacksonian party politics — managing state affairs as North Carolina's political culture realigned toward Democratic dominance",
            "His Senate service (1828–1831) coincided with the first years of the Jackson presidency — the administration's battles over the national bank, tariffs, and Indian removal — making him part of the Democratic majority that supported Jackson's transformative policy agenda",
            "His career demonstrated the generational shift in the Iredell family's political identity — from the Federalist nationalism of his father's generation to the states'-rights Jacksonian Democracy of his own, illustrating how families could span the transition between the first and second American party systems",
            "His career extended the Iredell family's political legacy in North Carolina legal and political culture — sustaining the family's prominence in eastern North Carolina across two generations and contributing to the state's development of a professional legal-political governing class"
        ],
        "relationships": [
            {"target": "north-carolina", "verb": "GOVERNS", "note": "Governor of North Carolina 1827–1828"},
            {"target": "us-senate", "verb": "SERVES_IN", "note": "North Carolina Senator 1828–1831"},
            {"target": "james-iredell-sr", "verb": "CHILD_OF", "note": "Son of original Supreme Court Justice Iredell Sr."},
            {"target": "andrew-jackson", "verb": "SUPPORTS", "note": "Jacksonian Democrat aligning with Jackson's presidency"},
            {"target": "democratic-party-united-states", "verb": "MEMBER_OF", "note": "Jacksonian Democrat despite Federalist family heritage"}
        ]
    }),

    # 8 — James Lisle Gillis
    ("james-lisle-gillis", {
        "summary": (
            "James Lisle Gillis (1792–1848) was a "
            "Canadian-born American jurist who served "
            "as Chief Justice of the Michigan Supreme "
            "Court during the formative period of "
            "Michigan statehood. His judicial career "
            "placed him at the center of Michigan's "
            "institutional development as a state — "
            "establishing the legal precedents, "
            "court procedures, and common law "
            "traditions of one of the Great Lakes "
            "states during its critical early decades.\n\n"
            "Michigan achieved statehood in 1837 — "
            "following several years of boundary "
            "disputes with Ohio over the Toledo Strip "
            "that ended with Michigan ceding the strip "
            "and receiving the Upper Peninsula as "
            "compensation. Gillis served on the "
            "Michigan Supreme Court during the "
            "rapid settlement of the state that "
            "followed statehood, as waves of New "
            "England and New York immigrants poured "
            "into the lower peninsula and as Detroit "
            "grew from a frontier town into a "
            "regional commercial center.\n\n"
            "As Chief Justice, Gillis was responsible "
            "for establishing Michigan's common law "
            "jurisprudence — adapting the English "
            "and New England legal traditions to "
            "the specific needs of a rapidly growing "
            "frontier state with enormous land "
            "speculation, rapid commercial development, "
            "and the complex legal questions generated "
            "by Michigan's timber, copper, and "
            "agricultural economies.\n\n"
            "His judicial decisions helped build "
            "the legal foundation of Michigan's "
            "commercial and property law."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Chief Justice of the Michigan Supreme Court during the formative period of Michigan statehood (post-1837); established Michigan's common law jurisprudence during the rapid frontier settlement era; judicial founder of one of the Great Lakes states' legal systems.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Michigan's achievement of statehood in 1837 — following the Toledo War boundary dispute with Ohio — created the state judicial institutions that required capable jurists to establish the legal frameworks governing a rapidly growing frontier society",
            "The massive wave of New England and New York immigration into Michigan's lower peninsula in the 1830s–1840s — driven by cheap land prices and the opening of the Erie Canal — generated the legal disputes over land titles, commercial contracts, and property rights that the Michigan Supreme Court under Gillis had to adjudicate",
            "Michigan's frontier economy — encompassing land speculation, timber, copper mining, and commercial agriculture — generated complex and novel legal questions about property rights, commercial obligations, and corporate liability that required sophisticated judicial responses from the nascent Michigan Supreme Court"
        ],
        "effects": [
            "His Chief Justice tenure established Michigan's common law foundations — the body of precedent governing property, contracts, torts, and commercial law that would guide Michigan courts for decades and provide the legal infrastructure for the state's economic development",
            "His judicial decisions contributed to the adaptation of English and New England common law traditions to the specific conditions of a Great Lakes frontier state — creating a distinctively Michigan jurisprudence that balanced frontier economic dynamism with the rule of law",
            "His court's work during the formative statehood period helped establish Michigan's judiciary as an institution capable of managing the complex legal disputes generated by rapid settlement — demonstrating that frontier American states could build functioning judicial systems quickly",
            "His legal legacy contributed to the development of the Great Lakes legal culture that would later support Michigan's emergence as a major industrial state — the commercial and property law frameworks he helped establish were built upon by subsequent generations of Michigan jurists"
        ],
        "relationships": [
            {"target": "michigan-supreme-court", "verb": "LEADS", "note": "Chief Justice of the Michigan Supreme Court"},
            {"target": "michigan", "verb": "SERVES_IN", "note": "Judicial founder of Michigan's legal system"},
            {"target": "michigan-statehood-1837", "verb": "FOLLOWS_FROM", "note": "Chief Justice in the formative post-statehood period"},
            {"target": "michigan-common-law", "verb": "ESTABLISHES", "note": "Built Michigan's foundational legal precedents"},
            {"target": "great-lakes-states", "verb": "REPRESENTS", "note": "Judicial figure in the Great Lakes frontier legal culture"}
        ]
    }),

]

if __name__ == "__main__":
    print(f"Batch 56 — enriching {len(ENTITIES)} entities")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
