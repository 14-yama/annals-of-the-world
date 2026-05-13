#!/usr/bin/env python3
"""
Batch 17 — 8 entities: Philippe-Antoine Merlin de Douai, Isaac René Guy
Le Chapelier, Marguerite-Élie Guadet, Guy Coquille, Eustathios Rhomaios,
Ahasverus Fritsch, Louis Marie de la Haye Vicomte de Cormenin, Jacob Burnet
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

    # 1 — Philippe-Antoine Merlin de Douai (1754–1838)
    ("philippe-antoine-merlin-de-douai", {
        "summary": (
            "Philippe-Antoine Merlin, known as Merlin de Douai (1754–1838), was one of the most prolific "
            "and politically powerful jurists of the French Revolutionary and Napoleonic eras — serving as "
            "Minister of Justice, one of the five Directors who governed France (1797–1799), and Procureur "
            "général of the Cour de Cassation. The combination of legislative, executive, and judicial "
            "authority concentrated in his career made him the legal architect of post-Revolutionary France's "
            "transition from the chaos of the Terror to the ordered governance of the Consulate and Empire.\n\n"
            "Born near Douai and trained as a lawyer, he was elected to the Estates-General in 1789 and "
            "became one of the most active legal draftsmen of the National Assembly. He voted for the death "
            "of Louis XVI in January 1793 — a vote that committed him to the Revolutionary cause and would "
            "later force his exile. As Minister of Justice (1795–1797), he oversaw the post-Thermidor "
            "reconstruction of the French court system and began the systematic compilation that became "
            "his greatest scholarly legacy: the Répertoire universel et raisonné de jurisprudence — "
            "a massive multi-volume encyclopedia of French legal doctrine that systematized the "
            "entire body of French law, old and new, with rigorous doctrinal analysis. This work "
            "went through multiple editions and remained a standard legal reference for decades.\n\n"
            "As a Director (October 1797–June 1799), he was one of the five men who governed the French "
            "republic before Napoleon's coup, navigating the complex factional politics of the late "
            "Directory. Under the Consulate and Empire, he served as Procureur général (Attorney General) "
            "of the Cour de Cassation — the supreme court of the French judicial system — where he "
            "played a central role in developing the court's jurisprudence under the Napoleonic Code.\n\n"
            "'He wrote the law when others were making the revolution, then applied it when others "
            "were making the empire.' Merlin de Douai was the quintessential Revolutionary lawyer-statesman."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Minister of Justice, Director of France (1797–1799), and Procureur général of the Cour de Cassation; his Répertoire universel de jurisprudence systematized all French law and shaped Napoleonic legal development.",
            "significanceCategory": "continental"
        },
        "causes": [
            "His legal training and election to the Estates-General in 1789 placed him at the center of the Revolutionary legislative process at its most creative moment",
            "His vote for Louis XVI's death and post-Thermidor ministerial appointments made him one of the key figures in consolidating the Revolutionary legal order after the Terror",
            "The urgent need to systematize the vast body of Revolutionary legislation into a coherent legal reference drove his compilation of the Répertoire universel de jurisprudence"
        ],
        "effects": [
            "As Minister of Justice (1795–1797), oversaw the post-Thermidor reconstruction of the French court system that bridged the Terror and the Consulate",
            "The Répertoire universel et raisonné de jurisprudence became the standard reference for French legal doctrine for decades, shaping how lawyers and judges understood the law",
            "As Director (1797–1799), participated in the governance of France during the final years of the Directory before Napoleon's coup — one of five men who effectively ruled France",
            "As Procureur général of the Cour de Cassation under Napoleon, shaped the supreme court's jurisprudence applying the Napoleonic Code in its formative decades"
        ],
        "relationships": [
            {"entity": "French Directory", "relationship": "MEMBER_OF", "note": "One of five Directors governing France (October 1797–June 1799), effectively a ruler of the French republic"},
            {"entity": "Répertoire universel et raisonné de jurisprudence", "relationship": "AUTHORED", "note": "Compiled the massive multi-volume legal encyclopedia that systematized all French law, old and new"},
            {"entity": "Cour de Cassation", "relationship": "SERVED_AS_ATTORNEY_GENERAL_OF", "note": "Served as Procureur général of the Cour de Cassation under Napoleon, shaping its foundational jurisprudence"},
            {"entity": "Louis XVI of France", "relationship": "VOTED_FOR_EXECUTION_OF", "note": "Voted for Louis XVI's death in January 1793, committing himself to the Revolutionary cause"},
            {"entity": "Napoleonic Civil Code", "relationship": "APPLIED", "note": "As Procureur général of the Cour de Cassation, supervised the development of jurisprudence applying the Napoleonic Code"}
        ]
    }),

    # 2 — Isaac René Guy Le Chapelier (1754–1794)
    ("isaac-rené-guy-le-chapelier", {
        "summary": (
            "Isaac René Guy Le Chapelier (1754–1794) was a Breton lawyer and revolutionary politician "
            "whose most enduring contribution to French — and through French influence, to Western — legal "
            "history was the Loi Le Chapelier (Le Chapelier Law) of June 14, 1791: one of the most "
            "consequential pieces of labor legislation in modern legal history, which prohibited all "
            "workers' corporations, trade guilds, professional associations, and collective bargaining "
            "in France. The law effectively banned trade unions for 73 years (until 1864) and became "
            "the foundational legal statement of the doctrine that labor relations were a purely "
            "individual matter between worker and employer, with no legitimate collective dimension.\n\n"
            "Born in Rennes into a legal family, Le Chapelier was trained as an advocate and became "
            "a leading figure in Breton political life before the Revolution. He was elected to the "
            "Estates-General in 1789 and co-founded the Breton Club, which became the Jacobin Club — "
            "the most influential political organization of the Revolution. He was elected president "
            "of the National Assembly on July 14, 1789 — the very day of the storming of the Bastille "
            "— placing him in the chair as the president of the revolutionary legislature at the "
            "defining moment of the Revolution.\n\n"
            "His law of June 1791 suppressed both workers' and employers' associations in the name "
            "of individual liberty and free contract — the argument that any coalition of workers "
            "to fix wages was an attack on individual freedom. The law was bitterly condemned by "
            "19th-century socialists (including Marx) as the foundational act of bourgeois legal "
            "oppression of the working class. Le Chapelier himself grew increasingly moderate and "
            "was arrested during the Terror and guillotined in April 1794.\n\n"
            "'He was the Bastille's president on the day it fell, and the unions' executioner "
            "two years later.' Le Chapelier's contradictory career embodied the Revolution's "
            "tension between political liberty and economic freedom."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Author of the Le Chapelier Law (1791) — which banned trade unions in France for 73 years and became the foundational legal statement of the individual labor contract doctrine — and president of the National Assembly on Bastille Day 1789.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Revolutionary rejection of the Old Regime's corporate bodies — guilds, corporations, Parlements — created the ideological framework for banning all intermediate associations between individuals and the state",
            "Employers' fears of wage-fixing conspiracies among Parisian workers in 1791 provided the immediate practical trigger for the Le Chapelier Law",
            "Enlightenment economic thinking — particularly the physiocrat and proto-liberal view that free individual contract was the natural and rational basis for economic relations — provided the ideological foundation for the law"
        ],
        "effects": [
            "The Le Chapelier Law banned trade unions and collective bargaining in France for 73 years, until 1864, profoundly shaping the development of French labor relations and the socialist political tradition",
            "The law became a foundational object of socialist criticism — Marx and later thinkers cited it as the paradigm case of bourgeois law serving capital against labor",
            "Similar legislation was adopted in other European states influenced by French Revolutionary law, extending the individual labor contract doctrine across the continent",
            "Le Chapelier's execution in 1794 exemplified the Terror's destruction of the moderate revolutionary generation that had created the foundational legislative architecture"
        ],
        "relationships": [
            {"entity": "Le Chapelier Law (Loi Le Chapelier, 1791)", "relationship": "AUTHORED", "note": "Proposed and sponsored the June 14, 1791 law banning workers' associations and collective bargaining in France"},
            {"entity": "Jacobin Club", "relationship": "CO-FOUNDED", "note": "Co-founded the Breton Club that became the Jacobin Club, the most powerful Revolutionary political organization"},
            {"entity": "National Assembly (France)", "relationship": "PRESIDED_OVER", "note": "Elected president of the National Assembly on July 14, 1789 — the day of the Bastille's storming"},
            {"entity": "Karl Marx", "relationship": "CRITICIZED_BY", "note": "Marx and later socialists cited the Le Chapelier Law as the foundational act of bourgeois legal oppression of the working class"},
            {"entity": "Reign of Terror", "relationship": "EXECUTED_BY", "note": "Arrested and guillotined in April 1794 during the Terror as his moderate republicanism was judged counterrevolutionary"}
        ]
    }),

    # 3 — Marguerite-Élie Guadet (1755–1794)
    ("marguerite-élie-guadet", {
        "summary": (
            "Marguerite-Élie Guadet (1755–1794) was a French lawyer, Girondin orator, and Revolutionary "
            "politician from the Gironde who became one of the most eloquent voices of the moderate republican "
            "faction in the National Convention — and one of the most prominent victims of the Jacobin "
            "purge that destroyed the Girondins in 1793–1794. Born in Saint-Émilion into a legal family "
            "and trained as an advocate at the Bordeaux bar, he represented the Girondin heartland in "
            "both the Legislative Assembly (1791) and the National Convention (1792).\n\n"
            "Guadet was known above all for his oratorical gifts — his speeches were considered among "
            "the finest of the Revolutionary period, combining legal precision with rhetorical force. "
            "He was closely associated with the Girondin leadership including Brissot, Vergniaud, "
            "and Condorcet, and served as the faction's attack orator — particularly skilled at "
            "denouncing the Jacobin and Montagnard leadership in parliamentary debate. His attacks "
            "on Marat and Robespierre were among the most direct and forceful of any Girondin deputy.\n\n"
            "When the Jacobins organized the popular uprising of June 2, 1793, which purged the "
            "Girondin deputies from the Convention and placed them under arrest, Guadet managed "
            "to escape from Paris and flee to his native Gironde. He went into hiding in Saint-Émilion, "
            "sheltered by his family, while attempting to organize Girondin resistance — the Federalist "
            "revolts that briefly challenged Jacobin authority in Bordeaux, Lyon, and other cities. "
            "He was eventually discovered and arrested in June 1794 and guillotined.\n\n"
            "Guadet's career embodied the Girondin tragedy: provincial lawyers of genuine republican "
            "conviction, outmaneuvered by the Jacobin alliance with Parisian popular radicalism and "
            "unable to match Robespierre's political ruthlessness."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "A leading Girondin orator and lawyer in the National Convention, known for his powerful rhetorical attacks on Marat and Robespierre; escaped the June 1793 Girondin purge before being captured and guillotined in 1794.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Bordeaux's commercial and legal culture produced a distinctive brand of moderate republicanism — legal, constitutional, and suspicious of Parisian radical centralism — that shaped Guadet's politics",
            "The Girondins' parliamentary dominance in early 1792 created the political stage for Guadet's oratorical talent and his attacks on the emerging Jacobin leadership",
            "The June 1793 Jacobin coup against the Girondins resulted from their inability to match the Montagnards' alliance with Parisian sectional activism — a structural failure Guadet's oratory could not overcome"
        ],
        "effects": [
            "His flight to Saint-Émilion and participation in organizing the Girondin Federalist resistance (1793) contributed to the brief challenge to Jacobin authority in the provincial cities",
            "His execution in 1794 was part of the systematic destruction of the moderate republican Girondin generation that the Jacobin Terror pursued",
            "His reputation as an orator was preserved in Revolutionary memoirs and later histories as one of the finest speakers of the Convention period",
            "The Girondin cause he represented — constitutional, federalist, and suspicious of Parisian mass radicalism — remained a reference point for moderate republican politics throughout 19th-century France"
        ],
        "relationships": [
            {"entity": "Girondin faction", "relationship": "LED", "note": "One of the leading deputies and primary attack orator of the Girondin faction in the National Convention"},
            {"entity": "Maximilien Robespierre", "relationship": "OPPOSED", "note": "Made some of the most direct and forceful parliamentary attacks on Robespierre and the Jacobin leadership"},
            {"entity": "Jean-Paul Marat", "relationship": "OPPOSED", "note": "Famous for his attacks on Marat in Convention debates before the Girondin proscription"},
            {"entity": "National Convention", "relationship": "MEMBER_OF", "note": "Deputy in the National Convention representing the Gironde, after service in the Legislative Assembly"},
            {"entity": "Reign of Terror", "relationship": "EXECUTED_BY", "note": "Captured in Saint-Émilion after a year in hiding and guillotined in June 1794"}
        ]
    }),

    # 4 — Guy Coquille (1523–1603)
    ("guy-coquille", {
        "summary": (
            "Guy Coquille (1523–1603), also known by the Latinized name Conchyleus, was a French jurist "
            "from Nivernais who became one of the most authoritative interpreters of French customary law "
            "in the 16th century — a period when French legal scholars were systematically analyzing and "
            "rationalizing the regional customary legal traditions that governed most of France outside the "
            "pays de droit écrit (Roman law zone). His works on Nivernais custom and on French public law "
            "placed him among the leading figures of the French humanist jurisprudence movement.\n\n"
            "Trained in law and returning to practice in Nivernais, Coquille combined the role of local "
            "barrister and administrator with systematic legal scholarship. His Institution au droit des "
            "Français (published posthumously, 1607) was a systematic introduction to the entirety of "
            "French law — one of the first attempts to present French private law as a coherent whole "
            "rather than a collection of regional customs. He also wrote extensively on the Coutume de "
            "Nivernois (Nivernais customary law), providing an annotated edition and commentary that "
            "served both local practitioners and national scholars.\n\n"
            "His works on French public law — particularly his writings on the Estates-General, the "
            "rights of the French nobility, and the nature of royal authority — engaged with the "
            "constitutional debates of the Wars of Religion period. Like other monarchomachs of his "
            "era, he argued for limitations on royal absolutism and for the constitutional role of "
            "the Estates, contributing to the constitutional theory of the French ancien régime. "
            "He was broadly sympathetic to the Catholic League in the Wars of Religion but maintained "
            "his scholarly independence.\n\n"
            "'He gave the customs of his province the dignity of doctrine.' Coquille's scholarly "
            "treatment of Nivernais custom demonstrated that regional French law could be analyzed "
            "with the same rigor as Roman law."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "A leading 16th-century French customary law scholar who systematized Nivernais custom and wrote the Institution au droit des Français — one of the first comprehensive accounts of French private law — while engaging with constitutional debates of the Wars of Religion era.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The French humanist jurisprudence movement (mos gallicus) sought to apply humanist philological and historical methods to the study of both Roman law and French custom, creating the intellectual context for Coquille's scholarship",
            "The Wars of Religion's constitutional crisis — with competing theories of royal authority and the rights of the Estates — created urgent demand for systematic accounts of French public law",
            "Nivernais's position as a region with well-developed customary law and an active local legal culture gave Coquille the material and the professional context for his customary law scholarship"
        ],
        "effects": [
            "The Institution au droit des Français (1607) provided one of the first systematic accounts of French private law as a coherent whole, influencing subsequent attempts at codification",
            "His Coutume de Nivernois commentary became the standard legal reference for Nivernais practitioners and a model for regional customary law scholarship",
            "His constitutional writings contributed to the French monarchomach tradition — the theory that royal authority had constitutional limits and that the Estates represented the French nation",
            "His humanist approach to customary law demonstrated that regional legal traditions could be treated with the same scholarly rigor as Roman law texts"
        ],
        "relationships": [
            {"entity": "French customary law tradition", "relationship": "SYSTEMATIZED", "note": "One of the leading systematizers of French regional customary law in the 16th century"},
            {"entity": "Nivernais", "relationship": "SERVED_IN", "note": "Practiced law and held administrative office in Nivernais, making it the subject of his most important customary law scholarship"},
            {"entity": "François Hotman", "relationship": "CONTEMPORARY_OF", "note": "Contemporary of the leading monarchomach jurists including Hotman, whose constitutional theories overlapped with Coquille's"},
            {"entity": "Wars of Religion (France)", "relationship": "ENGAGED_WITH", "note": "His constitutional writings engaged with the legal and political controversies of the Wars of Religion period"},
            {"entity": "Estates-General (France)", "relationship": "THEORIZED", "note": "Wrote on the constitutional role of the Estates-General as a limitation on royal absolutism"}
        ]
    }),

    # 5 — Eustathios Rhomaios (late 10th – early 11th century)
    ("eustathios-rhomaios", {
        "summary": (
            "Eustathios Rhomaios (fl. c. 990–1034 CE) was a senior Byzantine judge and jurist whose "
            "collection of legal decisions — known as the Peira ('Trials' or 'Decisions') — constitutes "
            "one of the most important primary sources for Byzantine private law in its classical period, "
            "providing detailed insight into how the law of property, inheritance, contract, and commercial "
            "relations was actually applied in the imperial courts of Constantinople. He served as a "
            "senior judicial official (holding the title of epi tou hippodromou, a high court position) "
            "and was associated with the legal revival under the Macedonian emperors.\n\n"
            "The Peira was compiled by Eustathios's student Theodore Bestes, who collected and organized "
            "the master's judicial decisions and opinions into a systematic treatise — a format that "
            "reflected the Byzantine pedagogical tradition of transmitting legal knowledge through "
            "collections of actual decisions rather than purely doctrinal treatises. The work covers "
            "the law of property (real and personal), inheritance and succession, commercial transactions, "
            "maritime law, and procedural matters, revealing the sophisticated interplay between the "
            "classical Roman law preserved in Justinian's Corpus Juris Civilis (especially the Basilica, "
            "the Byzantine Greek version) and the customary practice of Byzantine courts.\n\n"
            "Eustathios's decisions in the Peira are notable for their pragmatism: they reveal a legal "
            "system that used classical Roman doctrine as a framework but applied it flexibly to the "
            "commercial and social realities of 11th-century Byzantium, including the complex property "
            "arrangements of the Byzantine aristocracy and the commercial practices of Constantinople's "
            "merchants. The Peira is thus a crucial document both for Byzantine legal history and for "
            "the broader history of how Roman law was transmitted and adapted in the medieval world.\n\n"
            "Eustathios embodied the Byzantine ideal of the jurist as servant of the emperor's justice: "
            "his decisions mediated between ancient law and present reality in the empire's courts."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Byzantine senior judge whose collected decisions (the Peira) are one of the most important primary sources for Byzantine private law practice — revealing how Roman law was applied in the courts of 11th-century Constantinople.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Macedonian dynasty's legal revival — which produced the Basilica (a Greek condensation of the Justinianic legal corpus) and revived systematic legal education in Constantinople — created the scholarly environment for Eustathios's judicial career",
            "The Byzantine court system's need for senior judges who could apply the complex inherited Roman legal tradition to contemporary disputes produced the role that Eustathios filled",
            "The Byzantine pedagogical tradition of collecting and studying the decisions of authoritative judges provided the institutional context for the Peira's compilation by Theodore Bestes"
        ],
        "effects": [
            "The Peira became one of the most important primary sources for Byzantine private law, documenting how the Justinianic corpus was applied in actual 11th-century court decisions",
            "His decisions documented the interplay between classical Roman law doctrine and Byzantine commercial and aristocratic legal practice, revealing the evolution of law in practice",
            "The Peira influenced subsequent Byzantine legal scholarship and was cited by later Byzantine jurists and commentators",
            "His work contributed to the preservation and practical application of Roman legal tradition in Byzantium during the period when the West had largely abandoned systematic Roman law"
        ],
        "relationships": [
            {"entity": "Theodore Bestes", "relationship": "DOCUMENTED_BY", "note": "Theodore Bestes, his student, compiled and organized the Peira from Eustathios's judicial decisions and opinions"},
            {"entity": "Basilica (Byzantine law)", "relationship": "APPLIED", "note": "His decisions applied the Basilica — the Byzantine Greek condensation of Justinian's legal corpus — to contemporary cases"},
            {"entity": "Byzantine Empire", "relationship": "SERVED", "note": "Served as a senior judicial official in the courts of Constantinople under the Macedonian dynasty"},
            {"entity": "Macedonian dynasty", "relationship": "FLOURISHED_UNDER", "note": "His judicial career occurred during the legal revival of the Macedonian emperors who sponsored the Basilica compilation"},
            {"entity": "Corpus Juris Civilis", "relationship": "INTERPRETED", "note": "His decisions interpreted and applied the Justinianic legal corpus in its Byzantine form to the social realities of 11th-century Constantinople"}
        ]
    }),

    # 6 — Ahasverus Fritsch (1629–1701)
    ("ahasverus-fritsch", {
        "summary": (
            "Ahasverus Fritsch (1629–1701) was a German jurist, legal scholar, court official, and "
            "Lutheran hymn writer of the Baroque era — a characteristic combination of legal expertise, "
            "administrative service, and religious devotion that exemplified the learned professional "
            "culture of the smaller German courts of the 17th century. Born in Mühlhausen, Thuringia, "
            "he received an extensive education in law and served as Chancellor (Kanzler) of the county "
            "of Schwarzburg-Rudolstadt, one of the small Protestant German territories, for much of "
            "his career.\n\n"
            "As Chancellor, Fritsch was responsible for the legal administration of the territory — "
            "drafting ordinances, managing the territorial court, advising the count, and handling the "
            "complex jurisdictional relationships between the county and the Holy Roman Empire's "
            "overlapping legal and administrative structures. This practical experience informed his "
            "legal scholarship, which covered administrative law, common law, commercial law, and social "
            "policy. His works addressed practical legal questions including the regulation of taverns, "
            "the control of vagrancy and begging, and the organization of rural policing — the kind "
            "of police administrative law (Polizeiwissenschaft) that was becoming a systematic discipline "
            "in German territories during the late 17th century.\n\n"
            "Alongside his legal career, Fritsch was a productive Lutheran religious writer, composing "
            "hymns and devotional works that were used in Protestant church services. This dual career "
            "as jurist and hymn writer was not unusual in the culture of Baroque German Lutheranism, "
            "where legal scholarship and religious devotion were understood as complementary aspects "
            "of a godly civic life. His hymns, though largely forgotten outside specialists, contributed "
            "to the rich tradition of Lutheran congregational singing.\n\n"
            "Fritsch illustrated the distinctive culture of the German territorial jurist: deeply "
            "embedded in local administrative life, contributing to the emerging discipline of police "
            "law, and integrating legal service with religious devotion."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "German territorial Chancellor and legal scholar who contributed to the emerging discipline of police administrative law (Polizeiwissenschaft) in 17th-century German states, combining legal expertise with Lutheran hymn writing.",
            "significanceCategory": "local"
        },
        "causes": [
            "The legal culture of smaller German Protestant territories required trained chancellors who could manage the overlap between territorial, imperial, and church law — a role Fritsch filled in Schwarzburg-Rudolstadt",
            "The emerging discipline of Polizeiwissenschaft (police administrative law) in German territorial governance created demand for systematic legal scholarship on regulation and social control",
            "Lutheran Baroque culture's integration of professional duty and religious devotion created the environment in which a territorial chancellor could also be a hymn writer"
        ],
        "effects": [
            "His administrative legal writings contributed to the development of German Polizeiwissenschaft — the systematic treatment of administrative regulation as a legal discipline",
            "His practical legal works on tavern regulation, vagrancy, and rural policing provided models for territorial legal administration in similar small German states",
            "His hymns contributed to the tradition of Lutheran congregational music in Thuringia during the Baroque era",
            "His career model of the territorial chancellor-scholar-hymn-writer exemplified the integrated professional-religious culture of 17th-century German Lutheranism"
        ],
        "relationships": [
            {"entity": "County of Schwarzburg-Rudolstadt", "relationship": "SERVED_AS_CHANCELLOR_OF", "note": "Served as Chancellor (Kanzler) of Schwarzburg-Rudolstadt, responsible for legal administration and court oversight"},
            {"entity": "Holy Roman Empire", "relationship": "OPERATED_WITHIN", "note": "His legal administration navigated the complex jurisdictional relationships between the county and the Holy Roman Empire"},
            {"entity": "Lutheran Church", "relationship": "CONTRIBUTED_TO", "note": "Composed Lutheran hymns and devotional works used in Protestant church services"},
            {"entity": "Polizeiwissenschaft (German administrative law)", "relationship": "CONTRIBUTED_TO", "note": "His practical legal writings on social regulation contributed to the emerging German discipline of police administrative law"},
            {"entity": "Thuringia", "relationship": "ASSOCIATED_WITH", "note": "Born in Mühlhausen and spent his career in the Thuringian Protestant territories"}
        ]
    }),

    # 7 — Louis Marie de la Haye, Vicomte de Cormenin (1788–1868)
    ("louis-marie-de-la-haye-vicomte-de-cormenin", {
        "summary": (
            "Louis Marie de la Haye, Vicomte de Cormenin (1788–1868) was a French jurist, political "
            "pamphleteer, constitutional drafter, and orator critic whose career spanned from the "
            "Napoleonic era through the Second Empire — making him a continuous presence in French "
            "public law and political culture for over five decades. Trained as a lawyer and entering "
            "public service under Napoleon, he combined systematic legal scholarship on administrative "
            "law with ferociously popular political pamphlets under the pseudonym 'Timon' that attacked "
            "administrative despotism and financial corruption in the governments of the Restoration "
            "and July Monarchy.\n\n"
            "His legal scholarship made him one of the foundational figures of French droit administratif "
            "(administrative law) as an academic discipline. His Droit administratif (multiple editions "
            "from 1822) was the first systematic treatise on French administrative law as a distinct "
            "field, analyzing the principles and procedures of the Conseil d'État and the administrative "
            "courts that had developed under Napoleon. This was a genuinely creative legal contribution: "
            "administrative law was not yet recognized as a distinct discipline, and Cormenin's "
            "systematic treatment helped establish it as one.\n\n"
            "His pamphlets as 'Timon' — particularly Questions scandaleuses d'un jacobin (1829) and "
            "subsequent political writings — attacked government officials and financial privileges "
            "with a populist, ironic wit that made them enormously popular. His Livre des orateurs "
            "(1838), a collection of profiles of great French parliamentary orators with sharp critical "
            "analysis, became one of the most widely read political books of the July Monarchy. "
            "In 1848, he was the principal drafter of the French Constitution of the Second Republic "
            "— a constitution that established universal male suffrage and direct presidential election, "
            "creating the electoral mechanism that would bring Louis-Napoleon Bonaparte to power.\n\n"
            "'He built the frame of the Republic and sharpened the blade that cut it down.' "
            "Cormenin's constitution of 1848 created the conditions for Napoleon III's coup."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "One of the foundational figures of French administrative law (droit administratif); principal drafter of the French Constitution of 1848 (which introduced universal male suffrage and direct presidential election); author of the popular Livre des orateurs.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Napoleonic administrative state created a new body of administrative law and practice — the Conseil d'État, the prefectoral system — that required systematic legal analysis, which Cormenin supplied",
            "The July Monarchy's political culture of parliamentary oratory, press satire, and financial scandal created both the audience and the target for his 'Timon' pamphlets",
            "The 1848 Revolution's demand for a new republican constitution created the opportunity for Cormenin's crowning contribution as the principal drafter of the Second Republic's founding document"
        ],
        "effects": [
            "His Droit administratif treatise established French administrative law as a systematic academic discipline, providing the framework for subsequent development of the Conseil d'État jurisprudence",
            "His constitution of 1848 introduced universal male suffrage and direct presidential election in France — the electoral architecture that allowed Louis-Napoleon to win the presidency and eventually establish the Second Empire",
            "The Livre des orateurs (1838) was one of the most widely read political books of the July Monarchy, shaping public understanding of parliamentary oratory and political style",
            "His 'Timon' pamphlets attacking financial privilege and administrative despotism contributed to the popular culture of political satire that mobilized opposition to the July Monarchy"
        ],
        "relationships": [
            {"entity": "French Constitution of 1848", "relationship": "DRAFTED", "note": "Principal drafter of the French Second Republic constitution (1848), introducing universal male suffrage and direct presidential election"},
            {"entity": "Droit administratif (French administrative law)", "relationship": "FOUNDED", "note": "His Droit administratif treatise (from 1822) established French administrative law as a systematic academic discipline"},
            {"entity": "Louis-Napoleon Bonaparte (Napoleon III)", "relationship": "ENABLED", "note": "His 1848 constitution's direct presidential election mechanism enabled Louis-Napoleon's election and eventual coup"},
            {"entity": "Conseil d'État (France)", "relationship": "SYSTEMATIZED", "note": "His administrative law scholarship systematized the principles and procedures of the Conseil d'État"},
            {"entity": "Livre des orateurs", "relationship": "AUTHORED", "note": "His Livre des orateurs (1838) — profiles of French parliamentary orators — was one of the most popular political books of the July Monarchy"}
        ]
    }),

    # 8 — Jacob Burnet (1770–1853)
    ("jacob-burnet", {
        "summary": (
            "Jacob Burnet (1770–1853) was an American jurist and statesman who played a foundational "
            "role in establishing the legal and political institutions of the Northwest Territory and "
            "the state of Ohio, serving as a judge of the Northwest Territory courts, Associate Justice "
            "of the Ohio Supreme Court, and United States Senator from Ohio (1828–1831). Born in Newark, "
            "New Jersey, and educated at Nassau Hall (Princeton College, class of 1791), he studied law "
            "in New York before moving west to Cincinnati in 1796, where he would spend the rest of "
            "his long career as one of the city's leading legal and civic figures.\n\n"
            "Burnet's arrival in Cincinnati in the 1790s coincided with the transformation of the "
            "Northwest Territory from a frontier military zone into an organized territorial government "
            "moving toward statehood. He was appointed a judge of the Northwest Territory courts — "
            "one of the territorial judges who applied the law of the Ordinance of 1787 and established "
            "the judicial institutions of the future states of Ohio, Indiana, Illinois, Michigan, and "
            "Wisconsin. This role made him one of the founding legal architects of what became the "
            "most democratically organized territory in early American history.\n\n"
            "After Ohio's statehood (1803), Burnet served as an Associate Justice of the Ohio Supreme "
            "Court (1821–1828), contributing to the development of Ohio's state law during the critical "
            "early period of judicial institution-building. He entered the Senate in 1828 at the age "
            "of 58, representing the National Republican (later Whig) faction against the rising "
            "Jacksonian Democrats. His Notes on the Early Settlement of the North-Western Territory "
            "(1847), written in his seventies, became an invaluable historical memoir of the "
            "territorial period by a direct participant.\n\n"
            "'He helped civilize the wilderness with law before it was a state.' Burnet's career "
            "illustrated the essential role of territorial judges in transforming frontier territory "
            "into legal communities."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "A foundational legal figure of the Northwest Territory and early Ohio — territorial judge, Ohio Supreme Court justice, and US Senator — whose Notes on the Early Settlement of the North-Western Territory (1847) is a key primary source for territorial legal history.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Northwest Ordinance of 1787's establishment of a territorial government with appointed judges created the institutional role that Burnet filled as one of the Northwest Territory's early judicial officers",
            "The frontier conditions of the Northwest Territory in the 1790s required judges who could establish legal institutions from scratch, applying the Ordinance's framework to a rapidly evolving society",
            "Princeton education and New York legal training gave Burnet the credentials and professional network for appointment to the territorial judiciary"
        ],
        "effects": [
            "As a Northwest Territory judge, helped establish the judicial institutions and legal precedents that shaped the future states of Ohio, Indiana, and Illinois",
            "As an Ohio Supreme Court justice (1821–1828), contributed to the foundational development of Ohio state law during the critical early decades of statehood",
            "His Senate service (1828–1831) represented Ohio's legal-professional class in the national debate over the Jacksonian-Whig realignment of American politics",
            "Notes on the Early Settlement of the North-Western Territory (1847) became an invaluable firsthand memoir of the territorial period, preserved in historical scholarship as a primary source"
        ],
        "relationships": [
            {"entity": "Northwest Territory", "relationship": "SERVED_AS_JUDGE_OF", "note": "Appointed as a judge of the Northwest Territory courts, one of the founding legal architects of the territory's judicial institutions"},
            {"entity": "Ohio Supreme Court", "relationship": "SERVED_ON", "note": "Associate Justice of the Ohio Supreme Court (1821–1828)"},
            {"entity": "US Senate", "relationship": "MEMBER_OF", "note": "US Senator from Ohio (1828–1831), representing the National Republican faction"},
            {"entity": "Princeton University (Nassau Hall)", "relationship": "EDUCATED_AT", "note": "Graduated from Nassau Hall (Princeton College) in 1791"},
            {"entity": "Cincinnati, Ohio", "relationship": "SHAPED_LAW_OF", "note": "Moved to Cincinnati in 1796 and spent his career as one of the city's leading legal and civic figures"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 17)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
