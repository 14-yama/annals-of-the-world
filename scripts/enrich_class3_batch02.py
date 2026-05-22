#!/usr/bin/env python3
"""
Batch 02 — 8 entities (Class 311): Scottish Parliament, First Zionist Congress,
Cortes (Spain), Hungarian Parliament, Frankfurt Parliament,
First Triumvirate, Second Triumvirate, Indian National Congress
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

    ("scottish-parliament", {
        "summary": (
            "The Scottish Parliament (Pàrlamaid na h-Alba) is the devolved legislature of Scotland, established by the Scotland Act (1998) and opening in 1999 following a referendum in which 74% of Scottish voters approved devolution. It consists of 129 Members of the Scottish Parliament (MSPs) elected by a mixed-member proportional system — combining 73 constituency MSPs (first-past-the-post) with 56 regional MSPs (proportional lists) — designed to prevent the absolute majorities that characterise Westminster elections.\n\n"
            "The Parliament's devolved powers include health, education, justice, housing, transport, and aspects of taxation — making it responsible for the day-to-day governance of 5.5 million people. Since 2007 the Scottish National Party has dominated Scottish politics, and the Parliament became the arena for the 2014 independence referendum (55% No), which the SNP subsequently challenged citing Brexit (2016), in which Scotland voted 62% Remain. The Parliament's relationship with Westminster — managing the boundary between devolved and reserved powers — has been one of the UK's most dynamic constitutional questions.\n\n"
            "The Parliament's 1999 opening represented the most significant constitutional change in Scotland since the Acts of Union (1707), which had dissolved the original Scottish Parliament after 300 years. Its design incorporates proportional representation, gender-sensitive procedures, and a commitment to civic participation that influenced devolved institution design in Wales, Northern Ireland, and discussions about federal reform elsewhere."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Devolved legislature of Scotland established 1999; manages health, education, justice, and taxation for 5.5 million people; arena for the 2014 independence referendum; its mixed-member proportional design influenced devolved institution design across the UK.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Scotland Act (1998) — passed by Blair's New Labour government — fulfilled a manifesto commitment to Scottish devolution following the 1979 failed referendum and decades of Scottish political pressure for self-governance",
            "The 1997 devolution referendum (74% Yes) gave the Parliament democratic legitimacy; 63% also voted to give it tax-varying powers — reflecting Scottish dissatisfaction with Thatcher-era policies applied without Scottish mandate",
            "The decline of Conservative support in Scotland through the 1980s–90s — including the imposition of the Poll Tax in Scotland a year before England — created the political consensus across Labour, Liberal Democrats, and SNP for a devolved legislature"
        ],
        "effects": [
            "The Parliament has differentiated Scottish public policy from England's in significant ways: free prescriptions, free personal care for the elderly, and no tuition fees — demonstrating how devolution creates policy laboratories within a union state",
            "The 2014 Scottish independence referendum — held under an Edinburgh Agreement between the Scottish and UK governments — was the most significant constitutional vote in UK history, narrowly preserving the Union at 55% No",
            "Brexit (2016), in which Scotland voted 62% Remain despite the UK voting Leave, re-energised the independence movement and made the Parliament the arena for Scotland's contested relationship with both Westminster and the EU",
            "The Parliament's mixed-member proportional system has produced consistently more diverse representation than Westminster — including record female representation and the first Green-SNP coalition government in the UK (2021)"
        ],
        "relationships": [
            {"entity": "Scotland Act (1998)", "relationship": "ESTABLISHED_BY", "note": "The Scotland Act (1998) created the Scottish Parliament and defined its devolved powers"},
            {"entity": "2014 Scottish Independence Referendum", "relationship": "ARENA_FOR", "note": "The Parliament was the primary arena for the 2014 independence referendum — the most significant constitutional vote in UK history"},
            {"entity": "Scottish National Party (SNP)", "relationship": "GOVERNING_PARTY_SINCE_2007", "note": "The SNP has been the Parliament's dominant party since 2007, making independence its primary legislative agenda"},
            {"entity": "Acts of Union (1707)", "relationship": "REPLACED_DISSOLVED_PARLIAMENT_CREATED_BY", "note": "The 1999 Parliament replaced the original Scottish Parliament dissolved by the Acts of Union (1707) — reversing 292 years of legislative union"},
            {"entity": "Brexit (2016)", "relationship": "CONSTITUTIONAL_TENSION_CREATED_BY", "note": "Brexit — which Scotland voted against 62-38% — re-energised independence demands channelled through the Parliament"}
        ],
    }),

    ("first-zionist-congress", {
        "summary": (
            "The First Zionist Congress, convened by Theodor Herzl in Basel, Switzerland on 29–31 August 1897, was the founding assembly of the World Zionist Organization and the event that transformed Zionism from a literary and intellectual movement into an organised political programme with an institutional structure. Attended by 208 delegates from 17 countries, it adopted the Basel Programme — declaring that 'Zionism seeks to establish a home for the Jewish people in Palestine secured under public law' — and created the institutional machinery of the Zionist movement: an annual congress, a general council, and an executive.\n\n"
            "Herzl wrote in his diary after Basel: 'In Basel I founded the Jewish state. If I said this aloud today, I would be answered by universal laughter. Perhaps in five years, and certainly in fifty, everyone will perceive it.' His prediction was fulfilled almost exactly: on May 14, 1948 — 50 years and 9 months after the First Congress — the State of Israel declared independence. The Congress established the institutional DNA of the Zionist movement: its commitment to diplomacy, its secular-nationalist character, and its focus on Palestine rather than other proposed Jewish homelands.\n\n"
            "The First Zionist Congress was one of the most consequential single political meetings of the 20th century. The movement it institutionalised produced the Balfour Declaration (1917), the British Mandate for Palestine, the Holocaust-era rescue organisations, the 1948 Declaration of Independence, and ultimately the State of Israel — reshaping the Middle East and international politics to the present day."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Founded the World Zionist Organization (1897); adopted the Basel Programme calling for a Jewish homeland; Herzl predicted a Jewish state within 50 years — fulfilled in 1948; one of the most consequential single political meetings of the 20th century.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Theodor Herzl's The Jewish State (1896) — responding to the Dreyfus Affair and the persistence of European antisemitism — provided the intellectual blueprint and Herzl's organisational drive provided the convening energy for the Congress",
            "The acceleration of European antisemitism in the 1880s–1890s — including Russian pogroms, the Dreyfus Affair in France, and the rise of political antisemitism in Austria and Germany — demonstrated to Herzl that Jewish integration in Europe was impossible",
            "The failure of prior Zionist societies (Hovevei Zion) to achieve significant results demonstrated that an internationally organised political movement with an institutional structure was required — the gap the Congress was created to fill"
        ],
        "effects": [
            "The World Zionist Organization created at the Congress became the institutional vehicle for all subsequent Zionist diplomacy — ultimately securing the Balfour Declaration (1917), negotiating the British Mandate, and organising Holocaust-era aliyah",
            "The Basel Programme — 'a home for the Jewish people in Palestine secured under public law' — defined the Zionist political goal for 51 years until its achievement with Israel's independence declaration (1948)",
            "The Congress established the Jewish National Fund (1901) and the Anglo-Palestine Bank (1903) — the financial institutions that funded land purchase and settlement in Palestine for the following five decades",
            "The movement institutionalised at Basel produced a chain of events — Balfour Declaration (1917), UN Partition Plan (1947), Israel's independence (1948) — that fundamentally reshaped the Middle East and created one of the most enduring geopolitical conflicts of modern history"
        ],
        "relationships": [
            {"entity": "Theodor Herzl", "relationship": "CONVENED_BY", "note": "Herzl conceived and convened the First Zionist Congress — transforming Zionism from a literary movement to an organised political programme"},
            {"entity": "World Zionist Organization", "relationship": "FOUNDED", "note": "The Congress founded the World Zionist Organization — the institutional vehicle for all subsequent Zionist diplomacy"},
            {"entity": "Basel Programme", "relationship": "ADOPTED", "note": "The Congress adopted the Basel Programme — declaring Zionism's goal as 'a home for the Jewish people in Palestine secured under public law'"},
            {"entity": "Balfour Declaration (1917)", "relationship": "MOVEMENT_THAT_SECURED", "note": "The WZO founded at Basel ultimately secured the Balfour Declaration (1917) — the first major-power endorsement of Zionist aims"},
            {"entity": "State of Israel", "relationship": "INSTITUTIONAL_PRECURSOR_TO", "note": "The institutional movement created at Basel produced the State of Israel (1948) — fulfilling Herzl's 50-year prediction"}
        ],
    }),

    ("cortes", {
        "summary": (
            "The Cortes Generales is the bicameral national legislature of Spain, consisting of the Congress of Deputies (350 seats) and the Senate (265 seats). The institution traces its origins to the medieval Castilian Cortes — among the earliest representative assemblies in Europe, with documented meetings from 1188 — and was reconstituted in its modern form by the Spanish Constitution of 1978, which restored democracy after 40 years of Francoist dictatorship. The Congress of Deputies holds primary legislative authority; the Senate serves as a territorial chamber representing Spain's 17 autonomous communities.\n\n"
            "The medieval Cortes (from the Latin curia regis, the royal court) were called by Castilian, Aragonese, and Navarrese monarchs to vote taxation and provide counsel. The 1188 León Cortes — sometimes called the world's first parliament — is recognised by UNESCO as part of the Memory of the World Register. The modern Cortes was central to Spain's Transition to Democracy (1975–1978) following Franco's death, passing the Law for Political Reform (1976) and the Constitution (1978) that transformed Spain from a dictatorship into a parliamentary monarchy.\n\n"
            "The Cortes has since managed Spain's entry into NATO (1982), accession to the European Community (1986), and the ongoing tensions between central government and Catalonia's independence movement — making it the primary arena for Spain's constitutional evolution in the democratic era."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Spanish national legislature tracing origins to the 1188 León Cortes (among the world's earliest parliaments); reconstituted under the 1978 Constitution restoring democracy after 40 years of Francoism; managed Spain's transition to democracy, NATO accession, and EU integration.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The medieval Castilian monarchy's need to vote taxation and gain noble and clerical consent created the Cortes as a mechanism of estate representation — with the 1188 León Cortes recognised as among the world's earliest parliamentary meetings",
            "Francisco Franco's death (1975) and the regime's recognition that liberalisation was necessary to maintain stability created the political conditions for the democratic transition managed through the Cortes",
            "The 1976 Law for Political Reform — passed by Franco's own Francoist Cortes as a self-dissolution mechanism — was the constitutional device that transformed the body from a dictatorial rubber-stamp into the democratic legislature of the 1978 Constitution"
        ],
        "effects": [
            "The 1978 Spanish Constitution — passed by the Cortes through broad cross-party consensus — established Spain as a parliamentary monarchy and created the system of autonomous communities that has governed Spain ever since",
            "Spain's accession to the European Community (1986) — ratified by the Cortes — transformed Spain from a peripheral dictatorship into a core EU member, its most significant geopolitical reorientation since the loss of the Americas",
            "The Cortes's management of the Catalan independence crisis (2017–present) — approving Article 155 direct rule and subsequent negotiations — has been the central constitutional confrontation of 21st-century Spanish democracy",
            "The 1188 León Cortes — recognised by UNESCO's Memory of the World Register as the earliest documented parliament — gives Spain's legislative tradition one of the oldest institutional pedigrees in the world"
        ],
        "relationships": [
            {"entity": "Spanish Constitution (1978)", "relationship": "CREATED_BY", "note": "The 1978 Constitution — drafted and passed by the Cortes — established modern democratic Spain"},
            {"entity": "Francisco Franco", "relationship": "OPERATED_UNDER_DICTATORSHIP_OF", "note": "The Francoist Cortes (1939–1977) was a rubber-stamp legislature; its Law for Political Reform (1976) enabled democratic transition"},
            {"entity": "European Community", "relationship": "RATIFIED_ACCESSION_TO", "note": "The Cortes ratified Spain's accession to the European Community (1986) — Spain's most significant post-WWII geopolitical decision"},
            {"entity": "Catalan independence movement", "relationship": "MANAGES_CONSTITUTIONAL_TENSION_WITH", "note": "The Cortes approved Article 155 direct rule over Catalonia (2017) — the most serious constitutional crisis in modern Spanish democracy"},
            {"entity": "León Cortes (1188)", "relationship": "TRACES_ORIGINS_TO", "note": "The 1188 León Cortes — among the world's earliest documented parliaments — is the institutional ancestor of the modern Cortes Generales"}
        ],
    }),

    ("hungarian-parliament", {
        "summary": (
            "The Hungarian Parliament (Országgyűlés), seated in the neo-Gothic Parliament Building on the banks of the Danube in Budapest — one of the largest parliament buildings in the world — is the unicameral national legislature of Hungary, tracing its institutional origins to the Hungarian Diet of the medieval Kingdom of Hungary (founded 1000 CE). The modern parliament was established by the April Laws (1848), which created a responsible government elected by Hungarian citizens during the revolutionary upheaval that swept Europe that year.\n\n"
            "Hungary's parliamentary history is punctuated by constitutional ruptures: the Compromise (Ausgleich) of 1867 created the Austro-Hungarian Dual Monarchy, giving Hungary a co-equal parliament alongside Austria; the post-WWI Treaty of Trianon (1920) reduced Hungary to one-third of its former territory, creating a trauma that defined 20th-century Hungarian politics. Communist rule (1949–1989) suspended parliamentary democracy; its restoration in 1989–1990 was one of the most significant transformations of the post-Cold War era.\n\n"
            "Since 2010 the Parliament has operated under the Fundamental Law (2011) promulgated by Viktor Orbán's Fidesz government, which has been criticised by the EU, Council of Europe, and Venice Commission for concentrating power, weakening judicial independence, and restricting press freedom — making the Hungarian Parliament a central case study in the debate about democratic backsliding within the EU."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "National legislature of Hungary tracing origins to the medieval Diet (1000 CE); established as modern parliament in 1848; shaped by the Ausgleich (1867) and Trianon (1920); restored in 1989; under Orbán since 2010 it has become the EU's central case study in democratic backsliding.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The 1848 European revolutionary wave — particularly the Hungarian March Revolution led by Kossuth and Petőfi — forced the Habsburg court to grant Hungary a responsible government and modern parliament through the April Laws",
            "The Compromise (Ausgleich) of 1867 — negotiated after Austria's defeat by Prussia (1866) — created the Dual Monarchy, giving Hungary co-equal status and a sovereign parliament within the Habsburg Empire",
            "The collapse of communism (1989) and the Round Table negotiations between the Communist Party and the democratic opposition produced Hungary's peaceful transition — the Parliament voting its own dissolution and calling free elections in March–April 1990"
        ],
        "effects": [
            "The Parliament Building (completed 1904) — designed by Imre Steindl, modelled on Westminster — became one of Europe's most iconic civic monuments, symbolising Hungary's ambition for great-power status within the Dual Monarchy",
            "The Treaty of Trianon (1920) — which the Parliament fiercely protested — reduced Hungary's territory by 72% and its population by 64%, creating a revisionist nationalism that led Hungary into alliance with Nazi Germany and shaped its 20th-century history",
            "Hungary's 1989 parliamentary transition — including the Round Table negotiations and the October amendment to the constitution — became a model for other Central European countries undergoing peaceful democratic transformation",
            "The Orbán government's Fundamental Law (2011) — passed with a two-thirds supermajority by the Parliament — triggered EU Article 7 proceedings (2018) and became the EU's primary case study in how democratic backsliding can occur within a functioning electoral system"
        ],
        "relationships": [
            {"entity": "April Laws (1848)", "relationship": "MODERN_FORM_ESTABLISHED_BY", "note": "The April Laws (1848) created Hungary's responsible parliamentary government during the revolutionary upheaval"},
            {"entity": "Austro-Hungarian Compromise (Ausgleich, 1867)", "relationship": "CO-EQUAL_PARLIAMENT_CREATED_BY", "note": "The Ausgleich created the Dual Monarchy giving Hungary a sovereign parliament co-equal with Austria's"},
            {"entity": "Treaty of Trianon (1920)", "relationship": "TERRITORY_REDUCED_BY", "note": "Trianon (1920) reduced Hungary to one-third of its former territory — a trauma the Parliament memorialised and which shaped Hungary's 20th-century politics"},
            {"entity": "Viktor Orbán", "relationship": "CONTROLLED_BY_GOVERNMENT_OF", "note": "Orbán's Fidesz government (2010–present) used the Parliament's two-thirds supermajority to pass the Fundamental Law (2011) and concentrate executive power"},
            {"entity": "European Union Article 7 Proceedings", "relationship": "SUBJECT_OF", "note": "The EU invoked Article 7 proceedings against Hungary (2018) due to concerns about the Parliament's legislation on judicial independence and press freedom"}
        ],
    }),

    ("frankfurt-parliament", {
        "summary": (
            "The Frankfurt Parliament (Frankfurter Nationalversammlung), which met in the Paulskirche (St Paul's Church) in Frankfurt from May 1848 to June 1849, was the first freely elected national parliament for all of Germany and the central institution of the 1848 German Revolution. Elected by universal male suffrage in March 1848, it assembled 809 delegates — predominantly lawyers, academics, and civil servants (the 'professors' parliament') — with the task of drafting a liberal constitution for a unified German state.\n\n"
            "The Parliament produced the Frankfurt Constitution (March 1849), which guaranteed fundamental rights, established a constitutional monarchy, and offered the imperial crown to Frederick William IV of Prussia. His refusal to accept 'a crown from the gutter' — offered by a revolutionary assembly rather than the princes — was the decisive moment of failure. Without Prussian military support, the Parliament lacked the power to enforce its decisions against the restored absolutist princes, and it was forcibly dissolved in May–June 1849.\n\n"
            "The Frankfurt Parliament's failure set Germany's path toward unification 'from above' under Bismarck and Prussian military power (1866–1871) rather than 'from below' through liberal democratic revolution. Its catalogue of fundamental rights was incorporated into the Basic Law of the Federal Republic of Germany (1949) — making the Frankfurt Parliament a direct constitutional ancestor of modern German democracy despite its own failure."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "First freely elected all-German parliament (1848); produced the Frankfurt Constitution with fundamental rights; its failure after Frederick William IV rejected the imperial crown set Germany's path toward Bismarckian unification from above; its fundamental rights catalogue became an ancestor of the Basic Law (1949).",
            "significanceCategory": "continental"
        },
        "causes": [
            "The March Revolution of 1848 — ignited by the Paris February Revolution and fanned by economic crisis and nationalist agitation — forced the German princes to permit free elections, creating the political space for the Parliament to convene",
            "The absence of a Prussian or Austrian dominant power willing to support liberal unification from above left the Parliament dependent on moral authority and deliberation rather than military force — the structural weakness that proved fatal",
            "The 1848 revolutionary wave that swept Europe from Paris to Vienna to Berlin created a brief window of weakened royal authority during which the liberal middle classes could attempt to seize the constitutional initiative"
        ],
        "effects": [
            "Frederick William IV's rejection of the imperial crown (April 1849) determined that German unification would come through Prussian military power and Bismarck's Realpolitik rather than liberal constitutionalism — shaping Germany's path from 1866 to 1945",
            "The Frankfurt Constitution's catalogue of fundamental rights — drafted after extraordinary deliberation by the finest legal minds in Germany — was incorporated into the Basic Law (1949), making it a direct constitutional ancestor of modern German democracy",
            "The Parliament's failure discredited liberal gradualism in German politics and strengthened the case for revolutionary tactics — influencing both socialist and nationalist radical traditions for the next century",
            "The Paulskirche became a permanent symbol of German democratic aspirations: the Frankfurt Constitution's centenary (1948) was marked by the drafting of the Basic Law in the same spirit, and the Paulskirche Peace Prize remains Germany's most prestigious literary award"
        ],
        "relationships": [
            {"entity": "March Revolution (1848)", "relationship": "CREATED_BY", "note": "The March Revolution of 1848 forced the German princes to permit the free elections that produced the Parliament"},
            {"entity": "Frederick William IV of Prussia", "relationship": "OFFERED_IMPERIAL_CROWN_TO", "note": "The Parliament offered Frederick William IV the imperial crown (April 1849); his refusal was the Parliament's decisive moment of failure"},
            {"entity": "Frankfurt Constitution (1849)", "relationship": "PRODUCED", "note": "The Parliament produced the Frankfurt Constitution — the first liberal democratic constitution for a unified Germany"},
            {"entity": "German Basic Law (1949)", "relationship": "FUNDAMENTAL_RIGHTS_INCORPORATED_INTO", "note": "The fundamental rights catalogue of the Frankfurt Constitution was incorporated into the Basic Law (1949) — the constitution of modern Germany"},
            {"entity": "Otto von Bismarck", "relationship": "GERMAN_UNIFICATION_ACHIEVED_INSTEAD_BY", "note": "Bismarck's Realpolitik achieved German unification from above (1866–1871) — the path opened by the Frankfurt Parliament's failure"}
        ],
    }),

    ("first-triumvirate", {
        "summary": (
            "The First Triumvirate was the informal political alliance formed in 60 BCE between Julius Caesar, Pompey the Great, and Marcus Licinius Crassus — three of the most powerful men in the late Roman Republic. Unlike the later Second Triumvirate, it had no legal constitutional basis: it was a private agreement to pool political resources, neutralise mutual enemies, and advance each member's ambitions against the Senate's conservative faction (the optimates). The alliance was sealed by Pompey's marriage to Caesar's daughter Julia.\n\n"
            "The Triumvirate secured Caesar's consulship (59 BCE), from which he used his authority to pass popular land reform laws over senatorial opposition and secure the command in Gaul that made him the richest and most militarily powerful man in Rome. Pompey received ratification of his eastern settlements and land for his veterans; Crassus secured contracts for the equestrian tax-farming class. The alliance's public exposure — when Crassus's agent revealed the arrangement — caused a political scandal but also demonstrated its power.\n\n"
            "The Triumvirate dissolved progressively: with Julia's death (54 BCE), the personal bond between Caesar and Pompey dissolved; with Crassus's death at Carrhae (53 BCE), the three-way balance was lost. The Senate's pressure on Pompey to abandon Caesar produced the ultimatum that crossed the Rubicon — starting the civil war (49 BCE) that ended the Republic."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Informal alliance of Caesar, Pompey, and Crassus (60 BCE) that dominated the late Republic; secured Caesar's Gallic command; its dissolution produced the civil war that crossed the Rubicon and ended the Roman Republic, leading directly to the Principate.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Senate's (optimates') blocking of all three men's legislative goals — Pompey's eastern settlements, Crassus's tax-farming contracts, Caesar's land bill — created the shared grievance that made the alliance logical",
            "Caesar's political genius in identifying that Pompey's military prestige combined with Crassus's financial resources combined with his own popular support and legal skill created an unstoppable political combination",
            "The structural crisis of the late Republic — where military commanders with loyal professional armies had accumulated personal power beyond what republican institutions could contain — made private political alliances more powerful than formal constitutional bodies"
        ],
        "effects": [
            "Caesar's Gallic command (58–51 BCE) — secured by the Triumvirate's political arrangements — gave him the military victories, wealth, and loyal veteran army that made him the most powerful individual in the Roman world, enabling the civil war",
            "The Triumvirate's decade of dominance (60–53 BCE) demonstrated that the late Republic's formal institutions — the Senate, the magistracies, the assemblies — had been captured by personal political alliances, accelerating their legitimacy crisis",
            "The alliance's collapse and the subsequent Caesar-Pompey civil war (49–45 BCE) ended the Roman Republic and produced the Augustan Principate — the foundational transition that transformed Rome from a republic into an empire",
            "The Triumvirate established the template for ruling Rome through informal political combinations rather than formal constitutional structures — a model that Augustus would later perfect through the Principate's fiction of restored republican government"
        ],
        "relationships": [
            {"entity": "Julius Caesar", "relationship": "MEMBER_OF", "note": "Caesar was the political genius of the Triumvirate — using it to secure his Gallic command and the wealth and armies that made him supreme"},
            {"entity": "Pompey the Great", "relationship": "MEMBER_OF", "note": "Pompey contributed his unmatched military prestige and veteran army — receiving ratification of his eastern settlements in return"},
            {"entity": "Marcus Licinius Crassus", "relationship": "MEMBER_OF", "note": "Crassus contributed his vast wealth and equestrian networks — receiving tax-farming contracts for the eastern provinces in return"},
            {"entity": "Roman Senate (optimates)", "relationship": "FORMED_TO_OVERCOME_OPPOSITION_OF", "note": "The Triumvirate was created to bypass the Senate's conservative (optimate) faction that had blocked all three members' legislative goals"},
            {"entity": "Gallic Wars (58–51 BCE)", "relationship": "COMMAND_SECURED_FOR_CAESAR_BY", "note": "The Triumvirate's political arrangements secured Caesar's proconsular command in Gaul — the foundation of his subsequent dominance"}
        ],
    }),

    ("second-triumvirate", {
        "summary": (
            "The Second Triumvirate was the legal political alliance formed in October 43 BCE between Octavian (the future Augustus), Mark Antony, and Marcus Aemilius Lepidus — the three men who divided control of the Roman world after Julius Caesar's assassination and defeated his killers at the Battle of Philippi (42 BCE). Unlike the First Triumvirate, it was formally constituted by law (the Lex Titia) as a 'commission for the organisation of the state' (tresviri rei publicae constituendae) with consular power for five years — giving it a legal basis its predecessor lacked.\n\n"
            "The Triumvirate's most notorious act was the proscriptions of 43 BCE — a list of political enemies condemned to death and whose property was confiscated — which killed approximately 300 senators and 2,000 equestrians, including Cicero, whose hands and head were displayed on the Rostra. The wealth from the proscriptions financed the armies that defeated Brutus and Cassius at Philippi.\n\n"
            "After Philippi the three divided the Roman world: Octavian took the West, Antony the East, Lepidus Africa. The alliance progressively fractured as Octavian and Antony's rivalry intensified — culminating in the Battle of Actium (31 BCE) where Octavian defeated the combined forces of Antony and Cleopatra. Octavian's subsequent transformation into Augustus (27 BCE) ended the Republic and began the Principate."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Legal ruling commission of Octavian, Antony, and Lepidus (43–33 BCE); defeated Caesar's assassins at Philippi; conducted the proscriptions killing Cicero; its dissolution at Actium (31 BCE) left Octavian supreme, enabling the Principate and ending the Roman Republic.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Caesar's assassination (44 BCE) left a power vacuum among his heirs — Octavian, Antony, and Lepidus each controlled armies and territories, making formal alliance more stable than continued civil war among themselves",
            "The senatorial faction's (liberators') control of the eastern provinces and armies under Brutus and Cassius required a unified command among Caesar's heirs to mount an effective military response",
            "The Lex Titia (November 43 BCE) gave the Triumvirate legal constitutional standing — distinguishing it from the First Triumvirate's informal arrangement and allowing it to exercise magistrate-level authority without annual election"
        ],
        "effects": [
            "The proscriptions of 43 BCE — killing 300 senators and 2,000 equestrians including Cicero — effectively destroyed the political class of the late Republic, eliminating the human network that republican institutions required to function",
            "The Battle of Philippi (42 BCE) defeated the republican cause — with the deaths of Brutus and Cassius, the last military option for restoring the Republic was extinguished, making the Principate effectively inevitable",
            "The Battle of Actium (31 BCE) — Octavian's defeat of Antony and Cleopatra — left him the sole ruler of the Roman world, enabling his transformation into Augustus (27 BCE) and the establishment of the Principate",
            "Octavian's victory and the Triumvirate's dissolution produced the Pax Romana — 200 years of relative peace and prosperity across the Mediterranean world under imperial rule"
        ],
        "relationships": [
            {"entity": "Octavian (Augustus)", "relationship": "MEMBER_OF_AND_ULTIMATE_BENEFICIARY", "note": "Octavian used the Triumvirate to defeat his rivals and ultimately became sole ruler of Rome as Augustus (27 BCE)"},
            {"entity": "Mark Antony", "relationship": "MEMBER_OF", "note": "Antony controlled the East and Egypt through Cleopatra; his defeat at Actium (31 BCE) left Octavian supreme"},
            {"entity": "Marcus Aemilius Lepidus", "relationship": "MEMBER_OF", "note": "Lepidus controlled Africa but was gradually sidelined; Octavian stripped him of his triumviral powers in 36 BCE"},
            {"entity": "Proscriptions of 43 BCE", "relationship": "ORDERED", "note": "The Triumvirate's proscriptions killed ~300 senators and 2,000 equestrians including Cicero — effectively destroying the republican political class"},
            {"entity": "Battle of Actium (31 BCE)", "relationship": "DISSOLVED_AT", "note": "Octavian's victory over Antony and Cleopatra at Actium ended the Triumvirate and left him sole ruler of Rome"}
        ],
    }),

    ("indian-national-congress", {
        "summary": (
            "The Indian National Congress (INC), founded in Bombay on 28 December 1885 by Allan Octavian Hume (a retired British civil servant) and 72 delegates, was the principal organisation of the Indian independence movement and subsequently the dominant political party of independent India for three decades. Beginning as a moderate body seeking greater Indian representation in imperial administration, it was transformed under Bal Gangadhar Tilak and then Mohandas Gandhi into a mass movement demanding complete independence (Purna Swaraj).\n\n"
            "Gandhi's leadership (1920–1947) revolutionised the Congress: non-cooperation (1920–22), the Salt March and Civil Disobedience (1930), Quit India (1942) — each mobilising millions of Indians through nonviolent mass action. The Congress negotiated independence with the British Labour government and India's first Prime Minister Jawaharlal Nehru, who led Congress governments from 1947 to 1964, establishing India's constitutional democracy, mixed economy, and Non-Aligned Movement foreign policy.\n\n"
            "The Congress remained India's dominant party through 1984 — with Indira Gandhi's 1971 landslide and her Emergency (1975–77) marking its authoritarian turn — before declining under regional and caste-based parties. The Congress legacy is the world's largest democracy: the framework of secular constitutionalism, universal suffrage, and federal-parliamentary governance that has governed 1.4 billion people since 1950."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Founded 1885; principal organisation of Indian independence under Gandhi; negotiated independence (1947); governed India through Nehru (1947–64) establishing constitutional democracy, the mixed economy, and Non-Aligned Movement; its legacy is the world's largest democracy.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Allan Octavian Hume's initiative — supported by Viceroy Dufferin's calculation that a moderate Indian political organisation would provide a safety valve for growing nationalist sentiment — created the Congress as a loyal reformist body",
            "The Partition of Bengal (1905) by Lord Curzon — dividing the province on communal lines to weaken nationalist organisation — radicalised the Congress and produced the Swadeshi movement, transforming it from a reformist body into a proto-independence organisation",
            "Gandhi's return from South Africa (1915) and his development of satyagraha (nonviolent resistance) as a mass political technique transformed the Congress from an elite deliberative body into a genuinely popular movement capable of mobilising millions"
        ],
        "effects": [
            "Gandhi's nonviolent mass campaigns — Non-Cooperation (1920), Civil Disobedience (1930), Quit India (1942) — demonstrated that nonviolent resistance could challenge imperial power, directly inspiring Martin Luther King Jr., Nelson Mandela, and independence movements across Asia and Africa",
            "The Congress's negotiations produced the Indian Independence Act (1947) — ending 190 years of British rule over the subcontinent — but also the Partition of British India into India and Pakistan, which accompanied independence with communal violence killing 200,000–2 million people",
            "Nehru's Congress governments (1947–1964) established the constitutional architecture of India: parliamentary democracy, fundamental rights, secular federalism, and the planning commission — creating the institutional framework of the world's largest democracy",
            "The Congress model of a broad-tent, ideologically diverse national independence party that transitioned into a governing party was emulated by independence movements across Africa and Asia — from the ANC to TANU to the Kuomintang"
        ],
        "relationships": [
            {"entity": "Mohandas Gandhi", "relationship": "TRANSFORMED_INTO_MASS_MOVEMENT_BY", "note": "Gandhi's leadership (1920–47) transformed the Congress from an elite body into the mass independence movement that achieved Indian independence"},
            {"entity": "Jawaharlal Nehru", "relationship": "FIRST_PRIME_MINISTER_FROM", "note": "Nehru led Congress governments from 1947 to 1964, establishing India's constitutional democracy and Non-Aligned Movement foreign policy"},
            {"entity": "Indian Independence Act (1947)", "relationship": "NEGOTIATED", "note": "The Congress negotiated independence with the British Labour government — ending 190 years of British rule"},
            {"entity": "Salt March (1930)", "relationship": "ORGANISED", "note": "The Congress under Gandhi organised the Salt March (1930) — the iconic act of civil disobedience that galvanised world opinion against British rule"},
            {"entity": "Non-Aligned Movement", "relationship": "FOREIGN_POLICY_FOUNDED_BY", "note": "Nehru's Congress government co-founded the Non-Aligned Movement (1955) — India's Cold War-era foreign policy framework"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 02 — {len(ENTITIES)} entities (Class 311: Historic Assemblies & Congresses)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
