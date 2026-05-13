#!/usr/bin/env python3
"""
Batch 18 — 8 entities: Jean de La Bruyère, Álvaro Gómez Becerra,
Georges Antoine Chabot, David Barton, François Buzot, Ludwig Hassenpflug,
James Mercer, Elias Kane
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

    # 1 — Jean de La Bruyère (1645–1696)
    ("jean-de-la-bruyère", {
        "summary": (
            "Jean de La Bruyère (1645–1696) was a French philosopher, moralist, and satirist whose "
            "Les Caractères ou les Mœurs de ce siècle (1688) stands as one of the masterpieces of "
            "French classical literature — a collection of maxims, philosophical reflections, and "
            "sharply drawn portraits of social types that dissected the vanity, ambition, hypocrisy, "
            "and superficiality of Louis XIV's France with a precision that made it an instant "
            "literary sensation and a permanent monument of moral psychology. Trained in law at "
            "Orléans and holding the purchased office of trésorier de France (treasury clerk), "
            "he entered the Condé household in 1684 as tutor to Louis, Duke of Bourbon, grand-grandson "
            "of the Grand Condé — and it was from this privileged vantage point inside one of "
            "France's greatest noble houses that he observed the society he would portray.\n\n"
            "Les Caractères began as a translation of Theophrastus's ancient Greek Characters — "
            "the philosopher's sketches of human personality types — to which La Bruyère appended "
            "his own observations. The work grew through nine editions in his lifetime, each adding "
            "new portraits, until it had become a vast panorama of French society: the court, the "
            "bourgeoisie, the Church, the city, the financial world. His portraits — of the flatterer, "
            "the social climber, the pedant, the miser, the fashionable woman, the financier who "
            "grows rich on public misery — combined with his maxims on subjects from friendship to "
            "ambition to religious devotion, created a complete map of the moral landscape of "
            "the Grand Siècle.\n\n"
            "His election to the Académie française in 1693 was bitterly contested — his enemies "
            "argued that a moralist whose subjects might recognize themselves was no proper member "
            "— and his reception speech, which mounted a defense of the Ancients over the Moderns "
            "in the Querelle des Anciens et des Modernes, provoked further controversy. He died in "
            "1696, at the peak of his reputation.\n\n"
            "'Everything has been said, and we come too late now that men have been living and "
            "thinking for seven thousand years.' La Bruyère's opening maxim set the tone for a "
            "work that turned legal precision into literary art."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Author of Les Caractères (1688), one of the masterpieces of French classical literature; his sharply satirical portraits of human social types in Louis XIV's France made him the defining moral psychologist of the Grand Siècle.",
            "significanceCategory": "continental"
        },
        "causes": [
            "His position as tutor in the Condé household gave him intimate access to the highest levels of French aristocratic society — the raw material for Les Caractères — combined with the outsider perspective of a lawyer-turned-observer",
            "The tradition of French moral reflection — Montaigne's Essays, Pascal's Pensées, La Rochefoucauld's Maximes — provided the literary genre within which Les Caractères found its place and audience",
            "The social contradictions of Louis XIV's France — the enormous gap between courtly splendor and popular misery, between public piety and private vice — provided the moral landscape his portraits mapped"
        ],
        "effects": [
            "Les Caractères became one of the most widely read French literary works of the late 17th century, going through nine editions in La Bruyère's lifetime and influencing subsequent French moral philosophy",
            "His psychological portraits of social types influenced later literary traditions including the novel of manners, the essayistic tradition, and the moral psychology of the French Enlightenment",
            "His Académie française reception speech staked out a position in the Querelle des Anciens et des Modernes in favor of the Ancients, contributing to one of the major literary debates of the era",
            "His maxim on language — 'Le style, c'est l'homme même' (style is the man himself) — became one of the most widely cited statements in literary criticism"
        ],
        "relationships": [
            {"entity": "Condé family (House of Bourbon-Condé)", "relationship": "EMPLOYED_BY", "note": "Served as tutor to Louis, Duke of Bourbon (Condé household), from 1684; the Condé court provided the social milieu for Les Caractères"},
            {"entity": "Theophrastus", "relationship": "TRANSLATED", "note": "Les Caractères began as a translation of Theophrastus's ancient Greek Characters, to which La Bruyère appended his own portraits"},
            {"entity": "Académie française", "relationship": "MEMBER_OF", "note": "Elected to the Académie française in 1693, despite fierce opposition; his reception speech engaged the Querelle des Anciens et des Modernes"},
            {"entity": "La Rochefoucauld", "relationship": "CONTINUED_TRADITION_OF", "note": "His Caractères followed in the French classical tradition of the maxim established by La Rochefoucauld"},
            {"entity": "Querelle des Anciens et des Modernes", "relationship": "PARTICIPATED_IN", "note": "His Académie reception speech sided with the Ancients against the Moderns in this major literary dispute"}
        ]
    }),

    # 2 — Álvaro Gómez Becerra (1771–1855)
    ("álvaro-gómez-becerra", {
        "summary": (
            "Álvaro Gómez Becerra (1771–1855) was a Spanish liberal lawyer, statesman, and jurist who "
            "served in many of the highest legal and political offices in Spain during the turbulent "
            "decades of constitutional struggle between absolute monarchy and liberalism in the early "
            "19th century, including multiple terms as Minister of Justice and a brief tenure as Prime "
            "Minister (1843). Born in Badajoz into a legal family, he trained as a lawyer and became "
            "involved in Spanish liberal constitutional politics during the crisis of the Napoleonic "
            "occupation and its aftermath.\n\n"
            "Gómez Becerra was a committed liberal constitutionalist — a member of the faction that "
            "supported the Constitution of 1812 (the Cadiz Constitution) against Bourbon absolutism "
            "— and his career suffered the reversals typical of Spanish liberal politicians of his "
            "generation: prosecution and exile under the absolutist periods and rehabilitation and "
            "high office during the constitutional periods. He served multiple times as Minister "
            "of Justice under both the Moderate Liberal and Progressive factions that competed for "
            "power during the reign of Isabella II, playing a central role in the legal reforms of "
            "the Spanish state.\n\n"
            "His brief period as Prime Minister (January–May 1843) came near the end of the regency "
            "of General Espartero, just before the progressive coalition that had supported Espartero "
            "collapsed and the moderates took power. He was associated with the progressive liberal "
            "faction throughout his career. His legal career and ministerial service made him one "
            "of the most experienced legal practitioners in the Spanish liberal state during its "
            "formative decades — a transitional figure between the pre-constitutional legal world "
            "and the 19th-century Spanish constitutional order.\n\n"
            "Gómez Becerra embodied the liberal lawyer-statesman type that was central to 19th-century "
            "Spanish constitutional politics: committed to constitutional governance and legal reform "
            "but operating in a political environment of chronic instability and military intervention."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Spanish liberal lawyer and statesman who served multiple terms as Minister of Justice and briefly as Prime Minister (1843); a committed constitutionalist whose career spanned the turbulent liberal-absolutist conflicts of early 19th-century Spain.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Napoleonic occupation of Spain (1808-1813) and the Cadiz Constitution (1812) created the liberal constitutionalist political identity that shaped Gómez Becerra's entire career",
            "The chronic instability of Spanish constitutional politics under Ferdinand VII and Isabella II — oscillating between absolutism and liberalism — repeatedly returned liberal lawyers to and removed them from power",
            "Spain's need for experienced legal administrators during its constitutional periods created demand for lawyer-politicians like Gómez Becerra who combined legal expertise with liberal political credentials"
        ],
        "effects": [
            "Multiple terms as Minister of Justice contributed to the development of Spain's liberal legal institutions during the formative decades of the constitutional state",
            "His tenure as Prime Minister (January–May 1843) was part of the final phase of Espartero's regency before the moderate liberal takeover",
            "His career model of the liberal lawyer-statesman who suffered exile under absolutism and returned to high office under constitutional regimes was characteristic of his generation",
            "His long legal and political career helped maintain institutional continuity in Spain's liberal legal traditions across the repeated reversals of the period"
        ],
        "relationships": [
            {"entity": "Isabella II of Spain", "relationship": "SERVED_UNDER", "note": "Served multiple terms as Minister of Justice under Isabella II's reign"},
            {"entity": "General Espartero", "relationship": "SERVED_UNDER", "note": "Was Prime Minister (January–May 1843) during the final phase of Espartero's regency"},
            {"entity": "Spanish Constitution of 1812", "relationship": "SUPPORTED", "note": "A committed supporter of the Cadiz Constitution, which defined his liberal constitutionalist political identity"},
            {"entity": "Spanish progressive liberal faction", "relationship": "AFFILIATED_WITH", "note": "Associated with the progressive liberal faction throughout his career"},
            {"entity": "Spanish liberal state", "relationship": "SHAPED", "note": "Multiple ministerial terms shaped the legal institutions of the Spanish liberal constitutional state"}
        ]
    }),

    # 3 — Georges Antoine Chabot (1758–1819)
    ("georges-antoine-chabot", {
        "summary": (
            "Georges Antoine Chabot (1758–1819), known as Chabot de Lallier, was a French jurist and "
            "legal commentator who played an important role in the transition from ancien régime law "
            "to the Napoleonic legal system, serving as a senior judge and producing one of the "
            "foundational commentaries on the Napoleonic Civil Code. Born in Lallier (Isère) and "
            "trained as a lawyer in the old French legal system, he navigated the revolutionary "
            "reorganization of the French courts and emerged as a respected authority on the new "
            "civil law.\n\n"
            "His most significant scholarly contribution was the Commentaire sur la loi des successions "
            "(Commentary on the Law of Succession) and other systematic treatments of key provisions "
            "of the Code civil — the areas of property law, family law, and inheritance that were "
            "among the most practically important and technically complex of the new code's provisions. "
            "Chabot's commentaries were valued for their practical clarity and their systematic "
            "organization of the code's provisions with reference to the legislative history and the "
            "debates of the Council of State that had produced the final text.\n\n"
            "He served as président de chambre (presiding judge of a chamber) in the Paris Court of "
            "Appeals, one of the most important judicial positions in the Napoleonic court hierarchy. "
            "In this capacity he participated in the development of the early jurisprudence of the "
            "Napoleonic courts, applying the Code civil to the full range of civil disputes that "
            "came before the Paris appeals court. His combination of judicial office and legal "
            "commentary — writing about the law he was also applying — made him a characteristic "
            "figure of the early Napoleonic legal profession.\n\n"
            "Chabot de Lallier represented the type of the continuity judge-scholar who bridged "
            "the revolutionary disruption: trained under the old law, serving under the new."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "A French judge and legal commentator who produced systematic commentary on the Napoleonic Civil Code's succession and property law provisions; president of a chamber in the Paris Court of Appeals during the foundational years of Napoleonic jurisprudence.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Napoleonic Civil Code's enactment (1804) created immediate demand for systematic commentaries that could explain the new law to practitioners trained under the old legal system",
            "His position as a Paris Court of Appeals judge gave him both the institutional authority and the practical experience with the Code's application that informed his scholarly commentary",
            "The transition from the multiple regional legal systems of the ancien régime to the unified Napoleonic Code required experienced jurists to bridge the conceptual gap — a role Chabot filled"
        ],
        "effects": [
            "His Commentaire on succession law became a standard reference for practitioners applying the Code civil's inheritance provisions in the early 19th century",
            "His judicial decisions as président de chambre in the Paris Court of Appeals contributed to the early jurisprudence developing under the Napoleonic Code",
            "His scholarly work participated in establishing the practice of doctrinal commentary on the Code civil that became the dominant mode of French legal scholarship",
            "His career illustrated the continuity of legal personnel across the revolutionary divide — judges trained under the old law applying and explaining the new"
        ],
        "relationships": [
            {"entity": "Napoleonic Civil Code (Code Napoléon)", "relationship": "COMMENTED_ON", "note": "Produced systematic commentaries on the Civil Code's succession and property law provisions"},
            {"entity": "Paris Court of Appeals", "relationship": "SERVED_AS_JUDGE_IN", "note": "Served as président de chambre (presiding judge of a chamber) in the Paris Court of Appeals"},
            {"entity": "French legal commentary tradition", "relationship": "CONTRIBUTED_TO", "note": "His commentaries contributed to establishing the doctrinal commentary tradition that dominated 19th-century French legal scholarship"},
            {"entity": "Council of State (Conseil d'État)", "relationship": "DREW_FROM", "note": "His commentaries referenced the legislative debates of the Council of State that produced the Code civil"},
            {"entity": "Ancien régime French law", "relationship": "BRIDGED_WITH_NAPOLEONIC_CODE", "note": "Trained under the old legal system, he helped practitioners navigate the transition to the new Napoleonic Code"}
        ]
    }),

    # 4 — David Barton (1783–1837)
    ("david-barton", {
        "summary": (
            "David Barton (1783–1837) was an American lawyer, judge, and politician who was among the "
            "most prominent figures in Missouri's transition from territory to state, serving as the "
            "first Attorney General of the Missouri Territory, as a judge, and then as one of the "
            "first two United States Senators from Missouri (1821–1831) following Missouri's admission "
            "to the Union. His decade in the Senate made him one of Missouri's founding federal "
            "legislators and a significant participant in the national political debates of the "
            "early Jacksonian era.\n\n"
            "Born in Sullivan County, North Carolina (later Tennessee), Barton moved to the Missouri "
            "Territory as a young lawyer around 1809, at a time when Missouri was being rapidly settled "
            "and its territorial institutions were being established. He built a legal career and a "
            "political reputation that earned him election as the first Attorney General of the Missouri "
            "Territory (1813–1817) — the chief legal officer of the territory — and subsequently as a "
            "judge. When Missouri achieved statehood in 1821 and held its first senatorial elections, "
            "Barton was elected as one of Missouri's inaugural two senators, alongside Thomas Hart "
            "Benton — another founding figure of Missouri's political tradition.\n\n"
            "During his Senate tenure (1821–1831), Barton participated in the great debates of the "
            "Era of Good Feelings and the Jacksonian transition — including debates over internal "
            "improvements, tariff policy, and the emerging political realignment that created the "
            "Democratic and Whig parties. Missouri's geographic position as the gateway to the West "
            "and the South made its senators significant voices in national debates over westward "
            "expansion and slavery policy (Missouri had entered as a slave state through the Missouri "
            "Compromise of 1820). He eventually fell out with Andrew Jackson and the Democratic "
            "mainstream, losing his Senate seat after one decade.\n\n"
            "Barton's career illustrated the founding generation of trans-Appalachian American "
            "legal and political leadership — lawyers who followed the frontier westward and "
            "built the institutions of the new states."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "First Attorney General of the Missouri Territory and one of Missouri's inaugural two US Senators (1821–1831); a founding figure of Missouri's state legal and political institutions following the Missouri Compromise.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Missouri Territory's rapid post-1803 settlement created demand for trained lawyers who could build territorial legal institutions from scratch — the opportunity Barton seized as territorial Attorney General",
            "Missouri Compromise (1820) and Missouri's admission as a slave state created the political environment for Barton's election as an inaugural senator",
            "The pattern of westward migration by ambitious young lawyers following the frontier expansion of the early republic brought Barton from Tennessee to Missouri, where legal expertise was scarce and valued"
        ],
        "effects": [
            "As first Attorney General of the Missouri Territory, helped establish the legal framework of what would become one of the key gateway states of American westward expansion",
            "His decade as US Senator (1821–1831) made him a participant in the foundational debates of Jacksonian America — including tariff policy, internal improvements, and the emerging party realignment",
            "Together with Thomas Hart Benton, he represented Missouri in the Senate during the critical decade following statehood, shaping the state's national political identity",
            "His eventual break with Jacksonian Democrats illustrated the factional conflicts that reshaped American political parties in the 1820s-1830s"
        ],
        "relationships": [
            {"entity": "Missouri", "relationship": "FOUNDED_LEGAL_INSTITUTIONS_OF", "note": "First Attorney General of the Missouri Territory and inaugural US Senator; a founding figure of Missouri's legal and political institutions"},
            {"entity": "Thomas Hart Benton", "relationship": "COLLEAGUE_OF", "note": "Served alongside Benton as one of Missouri's first two US Senators; both were founding figures of Missouri's Senate delegation"},
            {"entity": "US Senate", "relationship": "MEMBER_OF", "note": "US Senator from Missouri (1821–1831), one of the state's two inaugural senators"},
            {"entity": "Missouri Compromise (1820)", "relationship": "PRECEDED_ELECTION_BY", "note": "Missouri's admission to the Union through the Missouri Compromise created the senatorial elections that sent Barton to Washington"},
            {"entity": "Andrew Jackson", "relationship": "FELL_OUT_WITH", "note": "Eventually broke with Andrew Jackson and the Jacksonian mainstream, ending his Senate career after one term"}
        ]
    }),

    # 5 — François Buzot (1760–1794)
    ("françois-buzot", {
        "summary": (
            "François Nicolas Léonard Buzot (1760–1794) was a French lawyer, orator, and Girondin "
            "political leader whose passionate advocacy for constitutional governance, provincial "
            "autonomy, and the rule of law — combined with his legendary romantic attachment to "
            "Manon Roland, wife of the Girondin minister Roland — made him one of the most compelling "
            "and tragic figures of the French Revolution's moderate republican generation. Born in "
            "Évreux (Normandy) to a legal family and trained as an advocate, he was elected to the "
            "Estates-General in 1789 and rapidly established himself as one of the most principled "
            "and eloquent deputies of the National Assembly.\n\n"
            "In the early Revolution, Buzot distinguished himself by demanding the abolition of "
            "lettres de cachet (royal arrest warrants), trial by jury, and the independence of "
            "the judiciary from royal control — demands that reflected his legal training and his "
            "conviction that the Revolution must above all establish the rule of law. He became "
            "a leading figure in the Girondin faction — the loose coalition of provincial republican "
            "deputies who favored decentralized federalist governance and opposed the Parisian "
            "mob's increasing influence over national politics. His attacks on Marat and Danton "
            "were among the most direct of any Girondin deputy.\n\n"
            "His profound but almost certainly unconsummated romantic attachment to Manon Roland "
            "— revealed in their correspondence and his posthumous memoirs — became one of the "
            "great emotional dramas of the Revolutionary period, with both dying within days of "
            "each other in 1794. After the Girondin proscription (June 2, 1793), Buzot fled to "
            "Normandy, tried to organize resistance, and eventually made his way to the Gironde. "
            "He was found dead in a field near Saint-Émilion in June 1794 — whether murdered "
            "or having died by suicide remained uncertain.\n\n"
            "'He wanted to give France laws, and France gave him death.' Buzot's tragedy "
            "personified the destruction of the lawyer's vision of rational, constitutional order "
            "by the revolutionary passion it had helped unleash."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "A leading Girondin lawyer and orator who advocated for the rule of law, jury trial, and judicial independence in 1789; his romantic attachment to Madame Roland and his death in June 1794 made him one of the most poignant figures of the Girondin tragedy.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Legal training and advocacy at the Évreux bar gave Buzot the legal principles — jury trial, judicial independence, habeas corpus — that defined his early Revolutionary demands",
            "The Girondin faction's conviction that the Revolution must establish constitutional governance rather than Parisian mass rule shaped Buzot's political identity and his opposition to the Montagnards",
            "His emotional bond with Manon Roland, wife of the Girondin minister Roland, deepened his personal investment in the Girondin cause and his despair at its destruction"
        ],
        "effects": [
            "His early advocacy for lettres de cachet abolition, jury trial, and judicial independence contributed to the legal reforms of the National Assembly's first years",
            "As a leading Girondin orator, his attacks on Marat and Danton sharpened the factional conflict that ultimately led to the Girondin proscription and the Terror",
            "His Mémoires, published posthumously, became an important primary source on the Girondin movement and on the emotional culture of the moderate republican tradition",
            "His death alongside Guadet, Barbaroux, and Pétion in the aftermath of the Girondin proscription made the Girondins a permanent symbol of the Revolution's destruction of its own moderate architects"
        ],
        "relationships": [
            {"entity": "Girondin faction", "relationship": "LED", "note": "A principal leader and orator of the Girondin faction in the National Convention"},
            {"entity": "Manon Roland", "relationship": "ROMANTICALLY_ATTACHED_TO", "note": "His profound romantic attachment to Madame Roland — revealed in their correspondence and his memoirs — became one of the most celebrated emotional dramas of the Revolution"},
            {"entity": "Jean-Paul Marat", "relationship": "OPPOSED", "note": "Made some of the most direct attacks on Marat in Convention debates, sharpening the factional conflict that led to the Girondin proscription"},
            {"entity": "Estates-General / National Assembly (France)", "relationship": "MEMBER_OF", "note": "Elected to the Estates-General from Évreux in 1789 and served through the National Assembly and Convention"},
            {"entity": "Reign of Terror", "relationship": "VICTIM_OF", "note": "Found dead near Saint-Émilion in June 1794 after a year in hiding following the Girondin proscription"}
        ]
    }),

    # 6 — Ludwig Hassenpflug (1794–1862)
    ("ludwig-hassenpflug", {
        "summary": (
            "Hans Daniel Ludwig Friedrich Hassenpflug (1794–1862) was a German conservative lawyer "
            "and statesman who served as Minister of State in Hesse-Kassel and became one of the "
            "most controversial political figures of the German constitutional conflicts of the "
            "1840s–1850s — a byword for reactionary bureaucratic conservatism among German liberals "
            "who dubbed him 'Hassenfuss' (Hate-foot) in their satirical press. Born in Hanau and "
            "educated in law, he built his career in the Hessian bureaucracy and married a sister "
            "of Felix and Fanny Mendelssohn — a biographical detail that connected the arch-conservative "
            "statesman to the most celebrated cultural family of German-Jewish Romanticism.\n\n"
            "Hassenpflug served as Hessian Minister of State (effectively prime minister) in three "
            "separate periods, and his political career was defined by his determined opposition "
            "to constitutional liberalism — his attempts to curtail the constitutional rights of "
            "the Hessian diet (parliament) and rule by electoral ordinance rather than parliamentary "
            "vote made him the embodiment of Hessian reactionary governance. During the 1848 "
            "revolution, he initially appeared to accept constitutional constraints before "
            "returning to reactionary policies, provoking a severe constitutional crisis in "
            "Hesse-Kassel in 1850 that required Austrian and Prussian intervention through "
            "the German Confederation to resolve in the Elector's favor.\n\n"
            "The 1850 Hessian constitutional crisis — in which Hassenpflug's attempts to govern "
            "without a constitutional budget led to the military's refusal to enforce his orders "
            "and ultimately to federal intervention — was one of the most significant test cases "
            "of the question of whether the German Confederation could enforce order in member "
            "states against constitutional resistance. The crisis was resolved in the direction "
            "of conservative authority, crushing the Hessian liberal movement.\n\n"
            "'Hassenpflug' became a German liberal political term meaning reactionary despotism "
            "— a dubious immortality for a man who saw himself as defending legitimate order "
            "against revolutionary excess."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Hessian Minister of State whose reactionary governance provoked the 1850 Hessian constitutional crisis — requiring German Confederation intervention — making him the arch-symbol of bureaucratic conservatism in German liberal political culture.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The German constitutional struggle of the Vormärz period — between Elector-backed conservatism and liberal parliamentary demands — created the political environment in which Hassenpflug's reactionary policies became nationally significant",
            "The 1848 revolutionary crisis temporarily dislodged reactionary ministries across Germany, but the conservative reaction of 1849-1850 enabled Hassenpflug's return to power",
            "Austrian and Prussian determination to crush German constitutional liberalism after 1848 provided Hassenpflug with the external support he needed to maintain reactionary governance despite domestic opposition"
        ],
        "effects": [
            "The 1850 Hessian constitutional crisis he provoked became a significant test case of German Confederation authority over member states' internal constitutional conflicts",
            "His policies contributed to the crushing of Hessian constitutional liberalism in the early 1850s, delaying democratic reform in Hesse-Kassel",
            "His name became a German liberal political synonym for reactionary bureaucratic despotism — 'Hassenpflug' entered the political vocabulary as a byword for anti-constitutional governance",
            "His connection to the Mendelssohn family illustrated the paradoxical social integration of Jewish families into German aristocratic-bureaucratic culture even as political conservatism dominated public life"
        ],
        "relationships": [
            {"entity": "Hesse-Kassel", "relationship": "GOVERNED", "note": "Served three terms as Hessian Minister of State, dominating the political life of Hesse-Kassel with reactionary conservatism"},
            {"entity": "Felix Mendelssohn", "relationship": "BROTHER-IN-LAW_OF", "note": "Married a sister of Felix and Fanny Mendelssohn, connecting the conservative statesman to Germany's most celebrated musical-literary family"},
            {"entity": "German Confederation", "relationship": "BACKED_BY", "note": "Austrian and Prussian backing through the German Confederation allowed Hassenpflug to maintain conservative governance against Hessian liberal opposition"},
            {"entity": "German liberal movement (Vormärz)", "relationship": "OPPOSED", "note": "His arch-conservative policies made him the primary target of Hessian and German liberal political anger"},
            {"entity": "1850 Hessian constitutional crisis", "relationship": "CAUSED", "note": "His attempt to govern without a constitutional budget provoked the 1850 Hessian crisis that required federal military intervention"}
        ]
    }),

    # 7 — James Mercer (1736–1793)
    ("james-mercer", {
        "summary": (
            "James Mercer (1736–1793) was a Virginia lawyer, military officer, planter, and jurist "
            "who served in multiple capacities during the colonial, Revolutionary, and early national "
            "periods of American history — as a member of the Virginia House of Burgesses, a delegate "
            "to the Continental Congress, and a judge of the Virginia General Court. A member of the "
            "prominent Mercer family of Stafford County (his brother was General Hugh Mercer, killed "
            "at Princeton in 1777), he combined the roles of lawyer, planter, and public servant "
            "that defined the Virginia gentry's civic culture.\n\n"
            "Mercer studied law and built his practice in Fredericksburg, Virginia, while also "
            "serving as an officer in the French and Indian War — the military experience that "
            "was a formative element for the Virginia gentry of his generation. He served in the "
            "Virginia House of Burgesses in the years of colonial political awakening that preceded "
            "the Revolution, participating in the legislative culture that produced Patrick Henry, "
            "Thomas Jefferson, and George Washington. He was a delegate to the Continental Congress "
            "(1779–1780) during the difficult middle years of the Revolutionary War, contributing "
            "to the deliberations of the national government at a moment of severe military and "
            "financial crisis.\n\n"
            "His appointment as a judge of the Virginia General Court — the principal court of "
            "the Commonwealth of Virginia in its early years — placed him in the role of applying "
            "the common law tradition to the legal questions of the new American republic. Virginia's "
            "courts in the post-Revolutionary period were developing the distinctive American "
            "common law jurisprudence that would eventually influence the entire nation through "
            "figures like John Marshall (who practiced before these same courts). Mercer "
            "participated in this formative judicial culture until his death in 1793.\n\n"
            "His career illustrated the civic multifunctionality of the Virginia legal gentry: "
            "the same men who argued cases, commanded militia, deliberated in Congress, and "
            "decided disputes from the bench."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Virginia lawyer, Continental Congress delegate (1779–1780), and judge of the Virginia General Court; a representative figure of the Virginia legal gentry who served across the colonial, Revolutionary, and early national periods.",
            "significanceCategory": "local"
        },
        "causes": [
            "Virginia's plantation gentry culture required legal training, military service, and civic engagement as complementary aspects of elite masculine identity — shaping Mercer's multifaceted career",
            "The Revolutionary crisis drew Virginia's legal professionals into Continental Congress service as the legal and political frameworks of the new nation required construction from scratch",
            "Virginia's post-Revolutionary need to build state judicial institutions using common law precedent created the role Mercer filled on the Virginia General Court"
        ],
        "effects": [
            "Continental Congress service (1779–1780) contributed to the deliberations of the national government during a severe mid-war crisis of finance and military capability",
            "His judicial service on the Virginia General Court contributed to the development of early Virginia state jurisprudence in the formative post-Revolutionary decade",
            "His family's Revolutionary history — his brother Hugh Mercer was killed at Princeton — connected him to the sacrificial narrative of Virginia's contribution to American independence",
            "His career model of the lawyer-soldier-legislator-judge exemplified the civic republican ideal of the Virginia gentry"
        ],
        "relationships": [
            {"entity": "Hugh Mercer", "relationship": "BROTHER_OF", "note": "His brother General Hugh Mercer was killed at the Battle of Princeton (1777), a celebrated Revolutionary War martyr"},
            {"entity": "Continental Congress", "relationship": "DELEGATE_TO", "note": "Virginia delegate to the Continental Congress (1779–1780)"},
            {"entity": "Virginia General Court", "relationship": "SERVED_AS_JUDGE_OF", "note": "Appointed judge of the Virginia General Court, the Commonwealth's principal court in the early national period"},
            {"entity": "Virginia House of Burgesses", "relationship": "MEMBER_OF", "note": "Served in the Virginia House of Burgesses during the colonial period of political awakening before the Revolution"},
            {"entity": "French and Indian War", "relationship": "SERVED_IN", "note": "Served as a military officer in the French and Indian War, the formative military experience of his generation of Virginia gentry"}
        ]
    }),

    # 8 — Elias Kane (1794–1835)
    ("elias-kane", {
        "summary": (
            "Elias Kent Kane (1794–1835) was an American lawyer and politician who held some of the "
            "most consequential positions in early Illinois history, serving as the first Secretary "
            "of State of Illinois and as a United States Senator at a time when Illinois was an "
            "infant state on the northwestern frontier, still defining its institutions and its "
            "position on the most contentious questions facing the American republic. Born in New "
            "York City and trained in law in Tennessee, he arrived in Illinois territory in 1814 "
            "and rapidly became one of the most prominent members of its small legal community.\n\n"
            "When Illinois achieved statehood in 1818, Kane was appointed as the first Secretary "
            "of State — the chief administrative officer of the new state government — a position "
            "he held until 1822. In this role he helped establish the administrative procedures "
            "and record-keeping systems of the fledgling state. He subsequently built his political "
            "career as a Jacksonian Democrat and was elected to the United States Senate (1825–1835), "
            "where he served for a full decade until his death in office at age 40 — one of the "
            "youngest senators to die in office in American history.\n\n"
            "As a senator, Kane was an active participant in the Jacksonian political revolution "
            "that reshaped American democracy — the expansion of voting rights, the spoils system, "
            "the Bank War, and the debates over public land policy that were of particular importance "
            "to western states like Illinois, where land distribution was the central economic and "
            "political question. Illinois's rapid growth from frontier territory to significant "
            "state during his decade in the Senate made him one of the architects of its national "
            "political identity.\n\n"
            "Kane's early death at 40 cut short a career that might have made him one of the major "
            "figures of Jacksonian Democracy. His career illustrated the rapid rise possible for "
            "able lawyers on the American frontier and the fragility of health in early 19th-century "
            "American political life."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "First Secretary of State of Illinois and US Senator (1825–1835); a foundational figure in Illinois's early state institutions who died in office at age 40 during the height of the Jacksonian era.",
            "significanceCategory": "local"
        },
        "causes": [
            "Illinois's transition from territory to state (1818) created founding positions — including Secretary of State — that went to the most capable members of the small territorial legal community",
            "Jacksonian Democratic politics in Illinois were shaped by the concerns of frontier settlers — public land policy, banking, and western infrastructure — that Kane championed in the Senate",
            "The rapid migration of lawyers from the East and South to Illinois territory gave able young lawyers like Kane opportunities for prominence not available in more established states"
        ],
        "effects": [
            "As first Secretary of State (1818–1822), helped establish the administrative foundations of the new Illinois state government",
            "His decade as US Senator (1825–1835) represented Illinois's interests during the critical Jacksonian era when the Bank War, land policy, and democratic reform reshaped American politics",
            "His early death in office opened his Senate seat to a new generation of Illinois politicians in the rapidly evolving Jacksonian-Whig party competition",
            "His career trajectory from frontier lawyer to founding state official to US Senator illustrated the rapid political mobility available in early frontier states"
        ],
        "relationships": [
            {"entity": "Illinois", "relationship": "FOUNDED_INSTITUTIONS_OF", "note": "First Secretary of State of Illinois (1818–1822), helping establish the administrative foundations of the new state"},
            {"entity": "US Senate", "relationship": "MEMBER_OF", "note": "US Senator from Illinois (1825–1835), serving a full decade before dying in office at age 40"},
            {"entity": "Andrew Jackson", "relationship": "SUPPORTED", "note": "An active Jacksonian Democrat who supported Jackson's political program including the Bank War and public land policy"},
            {"entity": "Jacksonian Democratic Party", "relationship": "AFFILIATED_WITH", "note": "Jacksonian Democrat whose Senate career was aligned with Jackson's political revolution"},
            {"entity": "Illinois frontier society", "relationship": "SHAPED_LAW_OF", "note": "One of the key legal and political figures of early Illinois who helped define the state's institutional foundations and national political identity"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 18)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
