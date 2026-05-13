#!/usr/bin/env python3
"""
Batch 15 — 8 entities: Robert Joseph Pothier, Jean-Joseph Mounier,
Stephen de Segrave, Désiré Dalloz, Florencio García Goyena,
François Gayot de Pitaval, Diego Bautista Urbaneja, Antoine-Claire Thibaudeau
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

    # 1 — Robert Joseph Pothier (1699–1772)
    ("robert-joseph-pothier", {
        "summary": (
            "Robert Joseph Pothier (1699–1772) was the greatest French jurist of the 18th century, whose systematic "
            "treatises on private law — particularly the Traité des obligations (1761) — provided the conceptual "
            "architecture for the Napoleonic Civil Code (1804) and exercised decisive influence on both the French "
            "civil law tradition and the Anglo-American common law of contracts. Born in Orléans and trained in "
            "Roman law from childhood, he served as a judge in the Orléans presidency (présidence) and professor "
            "at the University of Orléans for over three decades while producing the most analytically rigorous "
            "body of private law scholarship of his era.\n\n"
            "His Traité des obligations synthesized Roman law, French customary law, and canon law into a coherent "
            "theory of contractual obligation that defined the categories — offer and acceptance, consideration, "
            "error, fraud, force, and conditions — that structured both the Code Napoléon's contract provisions "
            "and the English common law through the influence of Lord Mansfield and later William Murray. He also "
            "wrote treatises on sale, lease, partnership, maritime law, and criminal procedure, creating a "
            "comprehensive survey of private law that served as the primary scholarly reference for the "
            "commissioners who drafted the Code Napoléon between 1799 and 1804. Portalis, who led the drafting "
            "committee, explicitly acknowledged Pothier's authority throughout the process.\n\n"
            "Pothier's influence extended beyond France: his works were translated into English, Spanish, and "
            "Portuguese, shaping the civil law codifications of Louisiana, Quebec, and Latin America and "
            "contributing to the development of English commercial law through cases that cited his treatises "
            "as authoritative expositions of general principles. Chief Justice John Marshall cited Pothier in "
            "early American Supreme Court decisions on contracts.\n\n"
            "'He did not make the Code, but the Code could not have been made without him.' Pothier's systematic "
            "analysis of obligation remains the foundation of French private law scholarship."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "The foundational jurist of the Napoleonic Civil Code; his Traité des obligations (1761) provided the conceptual framework for French contract law and influenced both civil law codifications worldwide and Anglo-American commercial law.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The French ancien régime's fragmentation between Roman law (pays de droit écrit) and customary law (pays de droit coutumier) created demand for a systematic synthesis that Pothier supplied",
            "Thirty years as both a practicing judge and university professor gave Pothier the dual perspective to integrate doctrinal theory with practical application",
            "The Enlightenment's demand for rational, systematic legal science aligned with Pothier's methodological approach to organizing private law around coherent principles"
        ],
        "effects": [
            "His Traité des obligations directly provided the conceptual framework for the Napoleonic Civil Code's contract provisions, acknowledged explicitly by the Code's drafter Portalis",
            "Translated into English and cited by Lord Mansfield, Pothier's categories of contractual obligation shaped the development of English commercial law",
            "Influenced civil law codifications in Louisiana, Quebec, and Latin America through his systematic treatment of private law",
            "Chief Justice John Marshall cited Pothier in early American Supreme Court decisions, embedding his thinking in US constitutional and commercial law"
        ],
        "relationships": [
            {"entity": "Napoleonic Civil Code (Code Napoléon)", "relationship": "INFLUENCED", "note": "His Traité des obligations provided the direct conceptual framework for the Code's contract provisions (1804)"},
            {"entity": "Jean-Étienne-Marie Portalis", "relationship": "RELIED_UPON_BY", "note": "Portalis, chief drafter of the Code Napoléon, explicitly acknowledged Pothier's authority throughout the drafting process"},
            {"entity": "University of Orléans", "relationship": "TAUGHT_AT", "note": "Professor of law at the University of Orléans for over three decades alongside his judicial career"},
            {"entity": "Lord Mansfield", "relationship": "INFLUENCED", "note": "Mansfield cited Pothier's treatises in developing English commercial law, embedding his categories in common law"},
            {"entity": "Louisiana Civil Code", "relationship": "INFLUENCED", "note": "Pothier's systematic private law treatises shaped the Louisiana Civil Code and other French-derived civil law systems in the Americas"}
        ]
    }),

    # 2 — Jean-Joseph Mounier (1758–1806)
    ("jean-joseph-mounier", {
        "summary": (
            "Jean-Joseph Mounier (1758–1806) was a French lawyer, political theorist, and revolutionary leader "
            "who played a decisive role in the founding moments of the French Revolution before becoming one of "
            "its most eloquent moderate critics. Born in Grenoble and trained as an advocate, he made his "
            "political reputation during the pre-revolutionary crisis in Dauphiné, leading the Estates of "
            "Dauphiné's resistance to royal despotism (1788) and organizing the Assembly of Vizille — an event "
            "often described as the precursor to the Revolution — which demanded constitutional government and "
            "the recall of the Estates-General.\n\n"
            "In 1789, Mounier was elected to the Estates-General from Dauphiné and became one of the most "
            "important figures of the revolutionary opening months. He was elected president of the Third "
            "Estate and later of the National Assembly, and he is credited as the organizer of the Tennis "
            "Court Oath (June 20, 1789), in which the deputies swore not to dissolve until France had a "
            "constitution. He was the principal author of the Declaration of the Rights of Man and of the "
            "Citizen's drafting committee and advocated for a constitutional monarchy modeled on the English "
            "system, with a strong executive and a bicameral legislature.\n\n"
            "When the Revolution moved in a more radical direction in October 1789, Mounier resigned from the "
            "Assembly and eventually emigrated, condemning the mob violence of the October Days. He returned "
            "under Napoleon and served as prefect of the Ilm department in Weimar before dying in 1806. "
            "His writings on constitutional government, particularly De l'influence attribuée aux philosophes, "
            "aux francs-maçons, et aux illuminés sur la Révolution de France (1801), offered one of the "
            "earliest conservative analyses of where the Revolution had gone wrong.\n\n"
            "'He lit the fire of 1789 and then spent the rest of his life trying to understand why it "
            "burned down the house.' Mounier's constitutional liberalism was overwhelmed by the revolutionary "
            "radicalism he had helped unleash."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Organizer of the Tennis Court Oath and principal drafter of the Declaration of the Rights of Man (1789); one of the founding architects of the French Revolution who became its most articulate moderate critic.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The financial and constitutional crisis of the ancien régime in the 1780s, combined with provincial resistance to royal despotism, created the political environment for Mounier's emergence",
            "The Assembly of Vizille (1788) — which Mounier helped organize — established his reputation as a constitutional reformer before the national Revolution began",
            "The Third Estate's frustration with procedural subordination in the Estates-General provided the political opportunity for Mounier's leadership of the Tennis Court Oath"
        ],
        "effects": [
            "The Tennis Court Oath (June 20, 1789), which Mounier organized, was one of the defining acts of revolutionary commitment that made the National Assembly's survival politically irreversible",
            "His drafting work on the Declaration of the Rights of Man and of the Citizen established the foundational rights document of the French Republic",
            "His advocacy for a constitutional monarchy modeled on English institutions shaped the Anglophile constitutional debate of 1789 before being defeated by the more radical faction",
            "His émigré writings offered one of the first conservative analyses of the Revolution's causes and trajectory, influencing subsequent anti-revolutionary thought"
        ],
        "relationships": [
            {"entity": "French National Assembly", "relationship": "LED", "note": "Served as president of the Third Estate and the National Assembly in the crucial early months of the Revolution"},
            {"entity": "Tennis Court Oath", "relationship": "ORGANIZED", "note": "Organized the Tennis Court Oath (June 20, 1789), the revolutionary commitment that established the National Assembly's defiance of the king"},
            {"entity": "Declaration of the Rights of Man and of the Citizen", "relationship": "CO-DRAFTED", "note": "Served on the drafting committee for the Declaration of the Rights of Man (1789)"},
            {"entity": "Assembly of Vizille", "relationship": "LED", "note": "Led the pre-revolutionary Assembly of Vizille in Dauphiné (1788), a precursor to the national revolution"},
            {"entity": "Napoleon Bonaparte", "relationship": "SERVED_UNDER", "note": "Returned to France under Napoleon and served as prefect of the Ilm department in Weimar before his death"}
        ]
    }),

    # 3 — Stephen de Segrave (c. 1175–1241)
    ("stephen-de-segrave", {
        "summary": (
            "Stephen de Segrave (c. 1175–1241) was an English judge and royal minister who served as Chief "
            "Justiciar of England under King Henry III (1232–1234) — the most powerful legal and administrative "
            "office in the medieval English state, equivalent to a prime minister with full judicial authority. "
            "Rising from a Leicestershire landowning family, he entered royal service as a justice itinerant "
            "and built a distinguished judicial career on the rapidly developing common law circuits of the "
            "early 13th century, accumulating both legal expertise and royal favor.\n\n"
            "His appointment as Chief Justiciar in 1232 came during the troubled minority of Henry III — a period "
            "in which the baronial magnates were demanding greater influence over royal governance and the common "
            "law courts were establishing the institutional patterns that would define English legal procedure "
            "for centuries. Segrave administered the courts at Westminster and the general eyre (the royal "
            "judicial circuits that visited every county), managing the settlement of land disputes, criminal "
            "jurisdiction, and the enforcement of Magna Carta's provisions during a decade when Henry III's "
            "government was under intense baronial scrutiny.\n\n"
            "His tenure as Chief Justiciar was cut short in 1234 when he fell from royal favor during the "
            "political crisis in which Henry III dismissed the faction around Hubert de Burgh and the Poitevin "
            "advisors he had replaced them with. Segrave was accused of various misconduct charges and stripped "
            "of his position, though he continued to serve in other judicial capacities afterward. He founded "
            "a Cistercian abbey at Garendon, Leicestershire, as part of his religious patronage.\n\n"
            "His career illustrated both the opportunities and the dangers facing royal ministers in "
            "13th-century England: the Chief Justiciar's power was immense but entirely dependent on royal "
            "favor in an era of intense political competition."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Chief Justiciar of England under Henry III (1232–1234), administering the common law courts during the critical post-Magna Carta period when English legal procedure was establishing its foundational patterns.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The rapid development of English common law under Henry II and his sons created a professional judicial class from which able administrators like Segrave could rise to the highest offices",
            "Henry III's minority and the political instability of the early 13th century required experienced judges who could administer the common law courts with authority during periods of royal weakness",
            "The baronial pressure following Magna Carta (1215) made the Chief Justiciar's role of enforcing legal processes against royal prerogative especially important and politically charged"
        ],
        "effects": [
            "Administered the English common law courts and general eyre during the critical post-Magna Carta consolidation period (1232–1234)",
            "His tenure as Chief Justiciar occurred during the decisive decade when the institutional patterns of English common law procedure were being established for the long term",
            "His dismissal in 1234 during Henry III's political realignment illustrated the vulnerability of royal ministers to factional politics even at the highest levels of judicial office",
            "Founded Garendon Abbey as a Cistercian religious foundation, contributing to the monastic culture of 13th-century Leicestershire"
        ],
        "relationships": [
            {"entity": "Henry III of England", "relationship": "SERVED", "note": "Served as Chief Justiciar under Henry III (1232–1234), the most powerful administrative and judicial office in the realm"},
            {"entity": "Hubert de Burgh", "relationship": "SUCCEEDED", "note": "Appointed Chief Justiciar after Hubert de Burgh's fall from favor, during the political reorganization of Henry III's court"},
            {"entity": "Magna Carta", "relationship": "ENFORCED", "note": "Administered the common law courts during the period of Magna Carta's institutional consolidation"},
            {"entity": "English common law", "relationship": "ADMINISTERED", "note": "Oversaw the general eyre and Westminster courts during the formative period of English common law procedure"},
            {"entity": "Garendon Abbey", "relationship": "FOUNDED", "note": "Founded a Cistercian abbey at Garendon, Leicestershire, as a religious foundation"}
        ]
    }),

    # 4 — Désiré Dalloz (1795–1869)
    ("désiré-dalloz", {
        "summary": (
            "Désiré Dalloz (1795–1869) was a French jurist, politician, and legal publisher whose Répertoire de "
            "législation, de doctrine et de jurisprudence — published from the 1820s onward and continuously "
            "updated — systematized the jurisprudence of post-Napoleonic France in a way that transformed "
            "how lawyers, judges, and scholars accessed French law, and whose publishing house Dalloz remains "
            "to this day the most important legal publisher in France. Born in Septmoncel (Jura) and trained "
            "in law, he was admitted to the Paris bar and became both a practicing lawyer and a prolific "
            "compiler and editor of legal materials.\n\n"
            "His great achievement was the creation of a comprehensive, systematically indexed encyclopedia "
            "of French legal doctrine and jurisprudence — the Répertoire de législation, de doctrine et de "
            "jurisprudence (from 1824) and the Recueil Dalloz (from 1845), a digest of court decisions that "
            "organized the rapidly expanding body of French judicial decisions into accessible, annotated form. "
            "The Recueil Dalloz — which continues to be published to this day as the Recueil Dalloz — made "
            "him the founder of systematic French legal publishing and created an infrastructure of legal "
            "knowledge that was essential to the functioning of the Napoleonic legal system.\n\n"
            "He served as a deputy in the Legislative Assembly (1848–1851) during the Second Republic, "
            "representing his department of Jura. His combination of legal scholarship, systematic publishing, "
            "and political engagement made him a representative figure of the post-Revolutionary French "
            "legal profession, in which the law had become both a career and a civic vocation. He was "
            "assisted by his brother Armand Dalloz.\n\n"
            "'He built the library in which French lawyers have been working ever since.' The Dalloz publishing "
            "house he founded remains the indispensable reference for French legal practice almost two centuries later."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Founder of the Dalloz legal publishing house and creator of the Répertoire de législation and Recueil Dalloz — the comprehensive digest of French law and jurisprudence that remains the most important French legal reference tool to this day.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Napoleonic Code's systematization of French law created the need for equally systematic legal publishing to make the rapidly expanding body of jurisprudence accessible",
            "The explosion of French court decisions in the 19th century required professional indexing and annotation services that Dalloz's Recueil uniquely provided",
            "The growing French bar's demand for accessible, reliable legal references created both the commercial opportunity and the professional necessity for Dalloz's systematic compilations"
        ],
        "effects": [
            "The Recueil Dalloz (from 1845) created the standard model for annotated case law reporting in France, continuously published to the present day as Recueil Dalloz",
            "The Dalloz Répertoire became the standard systematic encyclopedia of French law, shaping how French lawyers organized and accessed legal knowledge",
            "The Dalloz publishing house he founded remains the leading French legal publisher, producing the Dalloz Code civil and dozens of other essential legal reference works",
            "His systematic approach to legal publishing was adopted and adapted across French-influenced legal systems in Belgium, Luxembourg, Quebec, and francophone Africa"
        ],
        "relationships": [
            {"entity": "Napoleonic Civil Code", "relationship": "SYSTEMATIZED", "note": "His publishing enterprise systematized access to the jurisprudence developing under the Code Napoléon"},
            {"entity": "Armand Dalloz", "relationship": "COLLABORATED_WITH", "note": "Worked with his brother Armand Dalloz in building the legal publishing enterprise"},
            {"entity": "French Legislative Assembly", "relationship": "MEMBER_OF", "note": "Served as deputy in the Legislative Assembly (1848–1851) during the Second Republic"},
            {"entity": "Recueil Dalloz", "relationship": "FOUNDED", "note": "Founded the Recueil Dalloz (1845), the annotated digest of French court decisions still published today"},
            {"entity": "French legal profession", "relationship": "SERVED", "note": "His publishing infrastructure became essential to the functioning of the French legal profession in the 19th century and beyond"}
        ]
    }),

    # 5 — Florencio García Goyena (1783–1855)
    ("florencio-garcía-goyena", {
        "summary": (
            "Florencio García Goyena (1783–1855) was a Spanish jurist, statesman, and legal scholar from Navarre "
            "who authored the foundational commentary on Spanish civil law codification and served as Minister "
            "of Justice during the critical years of 19th-century Spanish legal reform. A graduate in law from "
            "Salamanca, he pursued both a legal career and political engagement during the turbulent decades "
            "of Spanish constitutional struggle between absolutism and liberalism, eventually emerging as "
            "the leading legal scholar of the Spanish liberal constitutional tradition.\n\n"
            "His principal scholarly achievement was Concordancias, motivos y comentarios del Código Civil "
            "español (1852), a systematic commentary on the draft Spanish Civil Code of 1851 — the first "
            "comprehensive Spanish civil code project, known as the García Goyena Project or the Isabelline "
            "Code. This commentary compared the proposed Spanish code article by article with the French "
            "Civil Code (Code Napoléon, 1804), the Sardinian Civil Code (1838), the Louisiana Civil Code, "
            "and the Spanish historical law sources (the Siete Partidas, the Novísima Recopilación), "
            "creating a comparative legal encyclopedia of extraordinary scholarly value.\n\n"
            "Although the 1851 draft code was not enacted into law due to political opposition, it became "
            "the direct source for the eventual Spanish Civil Code of 1889. García Goyena's Concordancias "
            "remained the authoritative commentary on both the draft and the eventual code for decades, "
            "and the 1851 draft profoundly influenced the civil codes of Chile (1855), Bolivia, Ecuador, "
            "Colombia, and other Latin American states whose codes were modeled on the García Goyena "
            "project through Andrés Bello's Chilean code.\n\n"
            "'He wrote the blueprint for a law that waited forty years to be born.' García Goyena's "
            "1851 draft and Concordancias shaped the legal systems of Spain and most of Latin America."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Author of the foundational 1851 Spanish Civil Code draft (García Goyena Project) and its comparative commentary; his work directly shaped the eventual Spanish Civil Code (1889) and, through Andrés Bello's Chilean code, the civil law systems of most of Latin America.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The French Napoleonic model of civil law codification created pressure on 19th-century European states, including Spain, to modernize and systematize their private law",
            "Spain's volatile constitutional politics under Isabella II created periods of liberal government that provided the political window for García Goyena's codification project",
            "The fragmentation of Spanish private law among regional customs (fueros), royal ordinances, and the medieval Siete Partidas created urgent demand for a unified civil code"
        ],
        "effects": [
            "The 1851 García Goyena Project became the direct source for the eventual Spanish Civil Code (1889), with many provisions adopted verbatim",
            "His Concordancias (1852) remained the standard scholarly commentary on the draft code and the eventual code, shaping Spanish civil law interpretation for generations",
            "Through Andrés Bello's Chilean Civil Code (1855), which drew heavily on the García Goyena Project, his draft influenced the civil law systems of Chile, Colombia, Ecuador, Bolivia, and other Latin American states",
            "Served as Minister of Justice during the critical period of Spanish legal modernization, aligning executive authority with the scholarly codification project"
        ],
        "relationships": [
            {"entity": "Spanish Civil Code (1889)", "relationship": "PRECEDED", "note": "His 1851 draft code was the direct source for the eventual Spanish Civil Code promulgated in 1889"},
            {"entity": "Code Napoléon (1804)", "relationship": "COMPARED_WITH", "note": "His Concordancias systematically compared the 1851 Spanish draft with the Code Napoléon as its most important reference"},
            {"entity": "Andrés Bello", "relationship": "INFLUENCED", "note": "Bello's Chilean Civil Code (1855) drew heavily on the García Goyena Project, transmitting its influence to Latin American civil law"},
            {"entity": "University of Salamanca", "relationship": "EDUCATED_AT", "note": "Received his legal training at the University of Salamanca"},
            {"entity": "Queen Isabella II of Spain", "relationship": "SERVED_UNDER", "note": "Served as Minister of Justice under Isabella II during the liberal periods of her reign"}
        ]
    }),

    # 6 — François Gayot de Pitaval (1673–1743)
    ("françois-gayot-de-pitaval", {
        "summary": (
            "François Gayot de Pitaval (1673–1743) was a French advocate and journalist who created one of "
            "the most influential legal-literary genres in Western culture: the collected compendium of "
            "famous criminal cases. His Causes célèbres et intéressantes (20 volumes, 1734–1743) — a "
            "collection of dramatic French criminal trials drawn from court records and embellished with "
            "narrative commentary — pioneered 'true crime' literature two centuries before the term was "
            "coined and directly influenced the development of detective fiction, the roman judiciaire, "
            "and the popular legal journalism that has shaped public understanding of crime and justice "
            "ever since.\n\n"
            "Gayot de Pitaval was born in Lyon and worked as an advocate in Paris before turning to legal "
            "journalism and the popularization of notable trials. His Causes célèbres drew on actual French "
            "judicial records to narrate famous cases of murder, poisoning, fraud, adultery, and disputed "
            "succession — presented with vivid characterization of the accused, prosecution narratives, "
            "defense arguments, and judicial decisions. The work was instantly popular across Europe and "
            "was translated and adapted into German (where Friedrich Schiller was directly influenced by "
            "it for Kabale und Liebe), Dutch, English, and other languages.\n\n"
            "The German adaptation became the Neue Pitaval, a collection that ran for decades and was one "
            "of the most widely read works in 18th and 19th century Germany. Edgar Allan Poe, widely "
            "considered the father of detective fiction, acknowledged the Pitaval tradition as a predecessor "
            "to the analytical crime narrative. The genre of popular legal journalism — sensational accounts "
            "of trials for non-specialist readers — remains one of the most commercially successful forms "
            "of non-fiction writing, with Gayot de Pitaval as its founding practitioner.\n\n"
            "'He made the courthouse into a theatre and the accused into characters the public could not "
            "stop reading about.' Gayot de Pitaval's Causes célèbres created the genre of narrative "
            "crime writing that persists to this day."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Creator of the Causes célèbres (1734–1743), the founding work of 'true crime' literature; his 20-volume collection of famous French criminal cases influenced Friedrich Schiller, Edgar Allan Poe, and the entire subsequent tradition of popular legal narrative.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The French legal system's public trials and voluminous court records provided the raw material for a narrative account of famous cases accessible to popular audiences",
            "The growing French and European reading public of the 18th century had an appetite for dramatic non-fiction that Gayot de Pitaval was the first to systematically supply with legal narratives",
            "The tradition of trial pamphlets and judicial reportage in France created both the literary precedent and the commercial model that Gayot de Pitaval expanded into a systematic multivolume enterprise"
        ],
        "effects": [
            "Causes célèbres was immediately translated and adapted across Europe, becoming one of the most widely read legal-literary works of the 18th century",
            "The German Neue Pitaval adaptation influenced Friedrich Schiller and established the popular trial narrative as a major literary form in Germany",
            "The Pitaval tradition was acknowledged by Edgar Allan Poe as a precursor to the analytical crime narrative, linking it to the development of detective fiction",
            "Created the commercial and literary genre of 'true crime' writing — popular narrative accounts of real criminal cases — that remains one of the most durable forms of non-fiction publishing"
        ],
        "relationships": [
            {"entity": "Friedrich Schiller", "relationship": "INFLUENCED", "note": "The German Neue Pitaval adaptation influenced Schiller's literary development and his dramatic treatment of crime and justice"},
            {"entity": "Edgar Allan Poe", "relationship": "INFLUENCED", "note": "Poe acknowledged the Pitaval tradition as a predecessor to the analytical detective narrative that he pioneered"},
            {"entity": "French court system", "relationship": "DREW_FROM", "note": "His Causes célèbres drew on actual French judicial records and trial proceedings to narrate famous cases"},
            {"entity": "True crime literary genre", "relationship": "FOUNDED", "note": "His Causes célèbres is the founding work of the popular narrative crime writing genre"},
            {"entity": "Roman judiciaire", "relationship": "ANTICIPATED", "note": "His narrative treatment of criminal trials anticipated the French roman judiciaire (legal thriller fiction) genre"}
        ]
    }),

    # 7 — Diego Bautista Urbaneja (1782–1856)
    ("diego-bautista-urbaneja", {
        "summary": (
            "Diego Bautista Urbaneja (1782–1856) was a Venezuelan lawyer, constitutionalist, and statesman who "
            "played a prominent role in the legal and political development of Venezuela from its independence "
            "through the mid-19th century, serving twice as acting President of Venezuela and making foundational "
            "contributions to the country's constitutional and legal structures. Born in Barcelona (Venezuela) "
            "and trained in law at the Real y Pontificia Universidad de Caracas, he emerged as a legal scholar "
            "and advocate before the independence movement transformed the political landscape of South America.\n\n"
            "Urbaneja was active in the independence movement and its immediate aftermath, participating in the "
            "political life of Gran Colombia and then of Venezuela after its separation from Colombia in 1830. "
            "He was one of the legal architects of post-independence Venezuelan constitutionalism, working to "
            "adapt Spanish colonial law and republican constitutional theory to the specific conditions of the "
            "young Venezuelan state. He served as Minister of Interior and Justice in several Venezuelan "
            "governments, bringing legal rigor to the administration of the new republic.\n\n"
            "He served as acting President of Venezuela in 1833 and again briefly in 1847, occupying the "
            "highest executive office during transitional periods between elected presidents. His legal "
            "training and constitutional expertise made him a steadying presence in the volatile early "
            "decades of Venezuelan republicanism, when the country oscillated between competing factions "
            "of military caudillos and civilian constitutionalists. He was associated with the Conservative "
            "faction that sought stable, ordered governance rooted in legal institutions.\n\n"
            "His career illustrates the central role played by trained lawyers in building the institutional "
            "frameworks of newly independent Latin American states, providing legal continuity in societies "
            "disrupted by revolutionary warfare and political instability."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Venezuelan constitutionalist lawyer who served twice as acting President (1833, 1847) and was a foundational figure in post-independence Venezuelan legal and political institution-building.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Venezuelan independence (1821) created the need for trained lawyers to build republican legal institutions adapted from Spanish colonial law to the new constitutional order",
            "The political instability of early republican Venezuela — marked by competition between military caudillos and civilian constitutionalists — created recurring crises that required legal arbitration",
            "Legal training at the Real y Pontificia Universidad de Caracas gave Urbaneja the institutional credentials to serve both as legal drafter and political executive"
        ],
        "effects": [
            "Contributed to the constitutional and legal frameworks of post-independence Venezuela as Minister of Interior and Justice in multiple governments",
            "Served as acting President of Venezuela (1833, 1847), providing executive continuity during transitional periods in the volatile early republican era",
            "As a lawyer-statesman, represented the constitutionalist tradition in Venezuelan politics against the military caudillo tendency that dominated much of 19th-century Latin America",
            "His career model of the lawyer-politician contributed to the institutional culture of Venezuelan constitutionalism in the critical decades after independence"
        ],
        "relationships": [
            {"entity": "Venezuela", "relationship": "LED", "note": "Served as acting President of Venezuela in 1833 and 1847, and as Minister of Interior and Justice in multiple governments"},
            {"entity": "Gran Colombia", "relationship": "PARTICIPATED_IN_GOVERNANCE_OF", "note": "Active in the political life of Gran Colombia before Venezuela's separation in 1830"},
            {"entity": "Simón Bolívar", "relationship": "CONTEMPORARY_OF", "note": "Urbaneja's political career overlapped with the revolutionary era of Bolívar and the early Venezuelan republic"},
            {"entity": "University of Caracas", "relationship": "EDUCATED_AT", "note": "Received his legal training at the Real y Pontificia Universidad de Caracas"},
            {"entity": "Venezuelan constitution", "relationship": "SHAPED", "note": "Contributed as a legal architect to the constitutional frameworks of the early Venezuelan republic"}
        ]
    }),

    # 8 — Antoine-Claire Thibaudeau (1765–1854)
    ("antoine-claire-thibaudeau", {
        "summary": (
            "Antoine-Claire Thibaudeau (1765–1854) was a French lawyer, revolutionary politician, Napoleonic "
            "administrator, and memoirist whose extraordinarily long career — spanning from the ancien régime "
            "through the Third Republic — made him one of the most continuous firsthand witnesses to the "
            "political transformation of France across nine decades. Born in Poitiers into a legal family "
            "and trained as an avocat, he was elected to the National Convention in 1792 and, most "
            "significantly, voted for the death of Louis XVI in January 1793 — a vote that defined "
            "his political identity for the rest of his long life.\n\n"
            "As a Conventionnel, Thibaudeau served during the Terror without becoming a terrorist himself, "
            "surviving the political purges of Thermidor to serve in the Council of Five Hundred under the "
            "Directory. Under Napoleon, he transitioned from revolutionary legislator to imperial "
            "administrator with remarkable facility, serving as Prefect of the Gironde (Bordeaux), "
            "the Bouches-du-Rhône (Marseille), and later as President of the Tuscany department during "
            "the French occupation of Italy. He was exiled after the Bourbon Restoration (1815) as "
            "a regicide.\n\n"
            "Returning after the 1830 revolution, Thibaudeau devoted his final decades to writing "
            "his memoirs — published in multiple volumes as Mémoires sur la Convention et le Directoire "
            "(1824) and Mémoires sur le Consulat (1827) and Mémoires sur l'Empire — which became "
            "invaluable primary sources for the history of the French Revolution and Empire. Written "
            "with unusual frankness and self-awareness, his memoirs preserved insider accounts of "
            "the National Convention, the rise of Napoleon, and the operation of Napoleonic provincial "
            "administration that are still cited by historians.\n\n"
            "'He was old enough to have pleaded cases before a king and young enough to outlive "
            "his own memoirs.' Thibaudeau's ninety years spanned the entire arc of Revolutionary France."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "A Conventionnel who voted for Louis XVI's execution and served as Napoleonic prefect; his multi-volume memoirs of the Convention, Directory, Consulate, and Empire are invaluable firsthand primary sources for the history of Revolutionary and Napoleonic France.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Election to the National Convention in 1792 placed Thibaudeau at the center of the most dramatic political events in French history during his formative years as a lawyer",
            "His vote for Louis XVI's death in January 1793 irrevocably committed him to the Revolutionary cause and marked him as a regicide for the rest of his life",
            "Napoleon's need for legally trained administrators with Revolutionary credentials created the opportunities for Thibaudeau's subsequent career as imperial prefect"
        ],
        "effects": [
            "Served as Prefect of Gironde, Bouches-du-Rhône, and Tuscany, contributing to the Napoleonic administrative apparatus that modernized French provincial governance",
            "His memoirs (Mémoires sur la Convention, Mémoires sur le Consulat, Mémoires sur l'Empire) became primary sources for the history of Revolutionary and Napoleonic France",
            "As a regicide, his exile under the Bourbon Restoration (1815) and return under the July Monarchy (1830) illustrated the political fractures of post-Revolutionary France",
            "His career trajectory — from Revolutionary lawyer to imperial administrator to memoirist — represented a complete arc of the Revolutionary generation's adaptation to successive regimes"
        ],
        "relationships": [
            {"entity": "National Convention", "relationship": "MEMBER_OF", "note": "Served as a deputy in the National Convention (1792–1795), voting for the execution of Louis XVI"},
            {"entity": "Napoleon Bonaparte", "relationship": "SERVED_UNDER", "note": "Served as Napoleonic prefect in Gironde, Bouches-du-Rhône, and Tuscany during the Empire"},
            {"entity": "Louis XVI of France", "relationship": "VOTED_FOR_EXECUTION_OF", "note": "Voted for the death of Louis XVI in January 1793, defining him as a regicide"},
            {"entity": "Bourbon Restoration", "relationship": "EXILED_BY", "note": "Exiled after the Bourbon Restoration (1815) as a regicide; returned after the 1830 revolution"},
            {"entity": "French Revolution", "relationship": "DOCUMENTED", "note": "His multi-volume memoirs are invaluable firsthand accounts of the Convention, Directory, Consulate, and Empire"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 15)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
