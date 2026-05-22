#!/usr/bin/env python3
"""
Batch 29 — 8 entities (Class 321): Famous Courts, Councils & Tribunals
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()
FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/321-Class-321"
FILE_PREFIX = "321"


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

    ("star-chamber", {
        "summary": (
            "The Star Chamber (Camera Stellata, est. c.1487 — formalized under Henry VII; abolished 1641) was the royal prerogative court of England — meeting in a room in Westminster whose ceiling was decorated with gold stars — that became the symbol of arbitrary, secretive, and oppressive royal justice. The Star Chamber operated without a jury, applied torture, could impose any punishment short of death, and was used by the Crown (especially under the Tudors and Stuarts) to prosecute nobles and commoners who were too powerful or politically sensitive to be tried before ordinary courts.\n\n"
            "The Star Chamber was originally created to provide speedy, impartial justice that was free from the corruption and intimidation that plagued ordinary courts — nobles with large retinues could intimidate jurors and subvert local justice. Under Henry VII and Henry VIII, the Star Chamber was genuinely useful: it prosecuted powerful lords who abused lower courts and enforced law that local courts could not. Under the early Stuarts (James I and especially Charles I), however, the Star Chamber became the instrument of political repression — prosecuting critics of royal policy, Puritan pamphleteers, and opponents of Ship Money.\n\n"
            "The Long Parliament abolished the Star Chamber (July 1641) as one of its first acts against Charles I's personal rule — a decision that expressed Parliament's determination to end royal prerogative justice. The term 'Star Chamber proceedings' entered the English language as a metaphor for any secret, arbitrary, and oppressive judicial process, and remains in use in legal and political discourse."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Royal prerogative court of England (est. c.1487; abolished 1641); no jury, could use torture, any punishment short of death; used by Tudors and Stuarts for political repression; Long Parliament abolished it (1641) as act against Charles I's personal rule; 'Star Chamber proceedings' entered English language as metaphor for arbitrary oppressive justice; gold star-decorated ceiling gave it its name.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The corruption and intimidation of ordinary English courts by powerful nobles — who could subvert juries and buy local justice — created the demand for a royal court free from local pressures that could enforce law against the powerful",
            "Henry VII's determination to reduce the political power of the nobility — which had made the Wars of the Roses possible — drove the use of the Star Chamber to prosecute powerful lords who abused their local authority",
            "The early Stuart kings' belief in the divine right of kings — and their determination to govern without parliamentary interference — transformed the Star Chamber from an impartial prerogative court into the instrument of political repression against critics of royal policy"
        ],
        "effects": [
            "The Long Parliament's abolition of the Star Chamber (1641) — one of its first acts against Charles I's personal rule — was a defining moment in the constitutional conflict that led to the English Civil War, expressing Parliament's determination to end royal prerogative justice",
            "The term 'Star Chamber proceedings' entered the English language and legal vocabulary as the archetype of arbitrary, secretive, and oppressive justice — used in legal and political discourse for 380 years to describe any proceeding that violates the principles of open courts and fair trial",
            "The Star Chamber's abolition established the principle that royal prerogative cannot override common law rights — a constitutional principle that shaped the development of English constitutionalism and the Bill of Rights (1689), contributing to the rule of law tradition",
            "The Star Chamber's persecution of Puritan pamphleteers and critics of royal policy — including the brutal punishments of William Prynne (ears cropped), Henry Burton, and John Bastwick — created martyrs for the parliamentary cause and galvanised opposition to Charles I's personal rule"
        ],
        "relationships": [
            {"entity": "Henry VII (Tudor monarch)", "relationship": "FORMALISED_BY_AS_INSTRUMENT_AGAINST_NOBLE_POWER", "note": "Henry VII formalised the Star Chamber (c.1487) as a royal court to prosecute powerful nobles who corrupted local justice"},
            {"entity": "Charles I (English Civil War context)", "relationship": "USED_AS_INSTRUMENT_OF_POLITICAL_REPRESSION_BY", "note": "Charles I used the Star Chamber to prosecute Puritan critics and Ship Money opponents — transforming a useful court into a tyranny symbol"},
            {"entity": "Long Parliament (abolition 1641)", "relationship": "ABOLISHED_BY_THE", "note": "The Long Parliament abolished the Star Chamber in July 1641 — one of its first acts against Charles I's personal rule, triggering the English Civil War context"},
            {"entity": "English Civil War (1642–1651)", "relationship": "ABOLITION_AS_EARLY_TRIGGER_FOR_CONSTITUTIONAL_CONFLICT_LEADING_TO", "note": "The Star Chamber's abolition was part of Parliament's constitutional challenge to royal prerogative that escalated into the English Civil War"},
            {"entity": "Rule of law (English constitutional tradition)", "relationship": "NEGATIVE_PRECEDENT_THAT_SHAPED", "note": "The Star Chamber's arbitrary justice — and Parliament's abolition of it — established the rule of law principle that royal prerogative cannot override common law rights"}
        ],
    }),

    ("conciergerie", {
        "summary": (
            "The Conciergerie (est. as royal palace c.1299; converted to prison c.1370; most notorious period 1793–1795) in Paris, France, is the former royal palace and medieval prison that became the primary holding facility for prisoners of the French Revolution's Reign of Terror — most famously Marie Antoinette, who was held here for 76 days before her execution in October 1793. The Conciergerie is now a national monument and museum preserving the most evocative physical space of the Terror.\n\n"
            "The Conciergerie was built as a royal residence — the Palais de la Cité — by Philip IV of France (the Fair) in the early 14th century, and became the royal administrative centre that gave the 'concierge' (keeper) his title. After the royal court moved to the Louvre and Vincennes, the Palais de la Cité became the principal law courts and prison of Paris. During the Reign of Terror (June 1793–July 1794), approximately 2,780 people were brought to the Conciergerie before being sent to the guillotine — including Marie Antoinette, Georges Danton, Camille Desmoulins, Antoine Lavoisier, and Maximilien Robespierre himself.\n\n"
            "The Conciergerie's medieval halls — the Salle des Gens d'Armes (Hall of Men-at-Arms, built 1302, the largest surviving medieval hall in Europe) — and the preserved cell of Marie Antoinette make it one of the most powerful historical sites in France. The building's history — from royal palace to law courts to the antechamber of the guillotine — encapsulates the trajectory of the French Revolution."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Medieval royal palace and French Revolution prison (est. c.1299); primary holding facility for Reign of Terror (1793–1795); 2,780 prisoners held before guillotine including Marie Antoinette (76 days), Danton, Lavoisier, Robespierre; Salle des Gens d'Armes (1302) — largest surviving medieval hall in Europe; Marie Antoinette's preserved cell; now national museum.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Philip IV's construction of the Palais de la Cité (c.1299) — the largest royal residence in medieval Europe — created the great halls and administrative infrastructure that later became Paris's principal law courts and prison",
            "The French Revolution's Reign of Terror (June 1793–July 1794) — and the Revolutionary Tribunal's production of hundreds of condemnations daily — created the demand for a large, central holding facility in Paris where prisoners could be kept before their trials and executions",
            "The Conciergerie's location on the Île de la Cité — at the heart of Paris, adjacent to the Revolutionary Tribunal in the Palais de Justice — made it the natural antechamber for prisoners condemned by the Tribunal, with the proximity reducing the time between judgment and execution"
        ],
        "effects": [
            "The Conciergerie's holding of Marie Antoinette (76 days, August–October 1793) — and her departure for the guillotine from its gates — made it the physical embodiment of the Revolution's destruction of the monarchy, transforming a medieval administrative building into one of the most powerful historical sites of the modern age",
            "The 2,780 prisoners held at the Conciergerie before guillotine execution during the Terror — including some of the Revolution's own leaders (Danton, Robespierre, the Girondins) — made the building a physical record of the Terror's indiscriminate violence and the most visited destination for understanding the Revolution's dark turn",
            "The Salle des Gens d'Armes (1302) — the largest surviving medieval hall in Europe, with its four aisles of Gothic columns — is the most important surviving example of medieval royal administrative architecture, preserving the physical scale and ambition of Philip IV's Paris",
            "The Conciergerie's status as a national monument — preserving Marie Antoinette's cell, the prisoners' records, and the medieval halls — makes it the primary physical site for confronting the moral complexity of the French Revolution: the same building that made Europe's greatest queen a prisoner also processed men like Antoine Lavoisier (executed while making seminal contributions to chemistry)"
        ],
        "relationships": [
            {"entity": "Marie Antoinette (Queen of France)", "relationship": "MOST_FAMOUS_PRISONER_HELD_BEFORE_GUILLOTINE_AT", "note": "Marie Antoinette was held at the Conciergerie for 76 days (August–October 1793) before her execution — making it the physical site of the monarchy's destruction"},
            {"entity": "Reign of Terror (June 1793–July 1794)", "relationship": "PRIMARY_HOLDING_FACILITY_DURING_THE", "note": "2,780 prisoners were held at the Conciergerie during the Terror before being sent to the guillotine by the Revolutionary Tribunal"},
            {"entity": "Philip IV of France (Philip the Fair)", "relationship": "BUILT_AS_ROYAL_PALACE_BY", "note": "Philip IV built the Palais de la Cité (c.1299) — the origin of the Conciergerie — as the largest royal residence in medieval Europe"},
            {"entity": "Revolutionary Tribunal (1793–1795)", "relationship": "ANTECHAMBER_FOR_PRISONERS_OF_THE", "note": "The Conciergerie's proximity to the Revolutionary Tribunal in the Palais de Justice made it the antechamber from which condemned prisoners were sent to the guillotine"},
            {"entity": "Salle des Gens d'Armes (1302)", "relationship": "CONTAINS_THE_LARGEST_SURVIVING_MEDIEVAL_HALL_IN_EUROPE", "note": "The Salle des Gens d'Armes — built 1302, four aisles of Gothic columns — is the largest surviving medieval hall in Europe and the architectural heart of the Conciergerie"}
        ],
    }),

    ("council-of-ten", {
        "summary": (
            "The Council of Ten (Consiglio dei Dieci, est. 1310, Venice) was the secret intelligence and security council of the Venetian Republic — the most feared and effective secret government body in European history, responsible for state security, intelligence gathering, surveillance, and the administration of justice in cases touching on state security. The Ten's combination of broad executive powers, secret proceedings, anonymous denunciations, and swift punishment made Venice the most effectively governed state in medieval and Renaissance Europe — and the model for subsequent intelligence and security organisations.\n\n"
            "The Council of Ten was created as an emergency measure following the Querini-Tiepolo conspiracy (1310) — a failed aristocratic coup attempt against the Venetian Republic — and became permanent because its effectiveness made it indispensable. Its three-member inner council (the Capi dei Dieci) rotated monthly, its deliberations were entirely secret, and its authority extended over the entire machinery of state security: intelligence gathering, diplomatic communications, the surveillance of noble families, and the administration of summary justice.\n\n"
            "The Ten's most famous instrument was the bocche di leone (lion's mouth) — stone letter boxes mounted on walls throughout Venice and in other subject cities, through which citizens could deposit anonymous accusations against other citizens. The boxes were inscribed 'for secret denunciations against anyone who concealed favours or services, or colluded to hide the true revenues of the State.' While the Ten formally required that anonymous accusations be corroborated by two witnesses, the combination of anonymity and power made the bocche symbols of surveillance and fear."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Venetian secret security council (est. 1310); most feared and effective secret government body in European history; created after Querini-Tiepolo coup attempt (1310); secret proceedings, anonymous denunciations via bocche di leone (lion's mouth letter boxes); swift summary justice; broad executive powers over state security and intelligence; monthly rotation of inner council (Capi dei Dieci); model for subsequent intelligence organisations.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Querini-Tiepolo conspiracy (1310) — the most dangerous attempt to overthrow the Venetian Republic — demonstrated the need for a permanent security body with emergency executive powers and the authority to act quickly and secretly against threats to the state",
            "Venice's unique position as a maritime empire — dependent on the security of its trade routes, the loyalty of its subject cities, and the intelligence about rival city-states and the Ottoman Empire — created the operational need for a professional secret intelligence and security organisation",
            "The Venetian Republic's patrician oligarchy — governing through multiple overlapping councils to prevent any single family or faction from seizing power — created the political need for a security body that could monitor the patriciate itself for treasonous activity and foreign corruption"
        ],
        "effects": [
            "The Council of Ten's effectiveness as a secret security organisation — combining intelligence gathering, surveillance, summary justice, and executive action — established the model for the modern intelligence and security state, with its combination of broad mandate, secret operation, and swift punishment",
            "The bocche di leone (lion's mouth) denunciation boxes — allowing anonymous accusations to be deposited for the Ten's attention throughout Venice — created one of the earliest documented systems of mass surveillance and denunciation, anticipating the mechanisms of modern authoritarian surveillance states",
            "The Ten's administration of Venetian diplomacy — including the development of the resident ambassadorial system, where diplomats reported intelligence on host governments — established the foundations of modern diplomatic intelligence gathering",
            "The Council of Ten's centuries-long effectiveness — allowing Venice to maintain its republican independence and commercial empire while surrounded by larger powers — made it the primary historical model for subsequent discussions of how states can use intelligence to compensate for military weakness"
        ],
        "relationships": [
            {"entity": "Venetian Republic (Serenissima)", "relationship": "PRIMARY_SECURITY_ORGAN_OF_THE", "note": "The Council of Ten was the most powerful body in the Venetian Republic — responsible for state security, intelligence, surveillance, and summary justice in security matters"},
            {"entity": "Querini-Tiepolo conspiracy (1310)", "relationship": "CREATED_IN_RESPONSE_TO_THE", "note": "The failed Querini-Tiepolo coup attempt (1310) created the emergency that produced the Council of Ten — initially temporary, made permanent due to its effectiveness"},
            {"entity": "Bocche di leone (lion's mouth denunciation boxes)", "relationship": "OPERATED_THE_FAMOUS_ANONYMOUS_DENUNCIATION_SYSTEM_OF", "note": "Stone letter boxes throughout Venice allowed anonymous accusations — creating one of history's earliest documented mass surveillance and denunciation systems"},
            {"entity": "Venetian diplomatic intelligence system", "relationship": "ADMINISTERED_THE_FOUNDATIONS_OF_THE", "note": "The Ten administered Venice's resident ambassadorial intelligence system — establishing the foundations of modern diplomatic intelligence gathering"},
            {"entity": "Modern intelligence and security organisations (historical model)", "relationship": "HISTORICAL_MODEL_FOR", "note": "The Ten's combination of secret operation, broad mandate, surveillance, and swift punishment established the archetype for modern intelligence and security organisations"}
        ],
    }),

    ("council-of-troubles", {
        "summary": (
            "The Council of Troubles (Raad van Beroerten, est. 1567, Spanish Netherlands; also known as the 'Council of Blood' or 'Blood Council') was the special tribunal established by the Duke of Alba (Fernando Álvarez de Toledo) to suppress the Protestant revolt in the Spanish Netherlands — trying, condemning, and executing thousands of Calvinist rebels, nobles, and burghers in a campaign of judicial terror that became the primary catalyst for the Dutch Revolt and the eventual independence of the Netherlands. The Council's extraordinary severity — executing approximately 1,000 people and confiscating the property of 10,000 more — transformed a religious dispute into a national independence movement.\n\n"
            "Alba created the Council of Troubles in September 1567 — shortly after his arrival with 10,000 Spanish troops — to try those accused of heresy, rebellion, and lèse-majesté in the iconoclast riots (Beeldenstorm) of 1566 and the subsequent Calvinist agitation. The Council bypassed the existing legal system entirely, operating under military jurisdiction and denying defendants the rights guaranteed by the privileges of the Netherlands. Its most dramatic act was the execution of the Counts Egmont and Hoorn (June 1568) — both loyal Catholic nobles who had served Philip II faithfully — demonstrating that no Netherlander was safe from the Council's reach.\n\n"
            "The Council's severity backfired catastrophically: rather than crushing the revolt, it united the previously fragmented Dutch provinces — Catholic, Calvinist, Lutheran, and Anabaptist — in a common cause against Spanish tyranny. William of Orange's response to the executions of Egmont and Hoorn became the founding moment of Dutch national consciousness."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Spanish Netherlands special tribunal (est. 1567); Duke of Alba's instrument of judicial terror; ~1,000 executions, 10,000 property confiscations; executed Counts Egmont and Hoorn (June 1568) — loyal Catholic nobles demonstrating no Netherlander was safe; bypassed existing legal system; catalysed Dutch national consciousness; transformed religious revolt into independence movement; Eighty Years' War origins.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Beeldenstorm (Iconoclast Fury, August 1566) — Calvinist mobs destroying Catholic church imagery throughout the Netherlands — created the crisis that Philip II used to justify sending Alba with extraordinary powers to restore Spanish authority",
            "Philip II's determination to suppress Protestantism throughout his empire — and his belief that the Netherlands required military force rather than the concessions proposed by Margaret of Parma — drove the appointment of the uncompromising Alba rather than a conciliatory governor",
            "Alba's own military character — shaped by decades of warfare — and his contempt for civilian legal proceedings drove the creation of a military tribunal that bypassed the Netherlands' existing legal privileges and treated the revolt as a military problem requiring military solutions"
        ],
        "effects": [
            "The Council of Troubles' execution of Counts Egmont and Hoorn (1568) — both loyal Catholic nobles who had defended Philip II — convinced the Netherlands that no degree of loyalty or Catholicism would protect them from Spanish tyranny, transforming a primarily Calvinist revolt into a broadly based national independence movement",
            "The Eighty Years' War (1568–1648) — the Dutch War of Independence — was directly triggered by the Council of Troubles' severity, making the Blood Council the primary catalyst for the creation of the Dutch Republic (1581) and the 17th-century Dutch Golden Age",
            "Alba's Council of Troubles became the primary historical symbol of tyrannical occupation — cited for 400 years in discussions of legal rights, religious liberty, and resistance to arbitrary authority — establishing 'the Council of Blood' as a byword for judicial terror",
            "The Dutch Act of Abjuration (1581) — the first declaration of independence from a hereditary monarch — cited Alba's tyranny and the Council of Blood as the justification for rejecting Philip II's sovereignty, influencing the American Declaration of Independence (1776) in its structure and arguments"
        ],
        "relationships": [
            {"entity": "Duke of Alba (Fernando Álvarez de Toledo)", "relationship": "CREATED_AND_PRESIDED_OVER_BY", "note": "Alba created the Council of Troubles (1567) as the instrument of judicial terror to suppress the Dutch revolt — earning it the name 'Council of Blood'"},
            {"entity": "Counts Egmont and Hoorn (executed 1568)", "relationship": "MOST_FAMOUS_VICTIMS_OF_THE", "note": "The execution of Egmont and Hoorn — loyal Catholic nobles — demonstrated the Council's reach and galvanised Dutch national consciousness against Spanish tyranny"},
            {"entity": "Eighty Years' War (Dutch War of Independence, 1568–1648)", "relationship": "PRIMARY_CATALYST_FOR_THE", "note": "The Council's severity transformed a religious revolt into a national independence movement — directly triggering the Eighty Years' War"},
            {"entity": "Dutch Act of Abjuration (1581)", "relationship": "CITED_AS_JUSTIFICATION_FOR_RESISTANCE_IN_THE", "note": "The Act of Abjuration cited Alba's tyranny and the Council of Blood as justification for rejecting Philip II's sovereignty — influencing the American Declaration of Independence"},
            {"entity": "Philip II of Spain", "relationship": "AUTHORISED_BY_AS_INSTRUMENT_OF_SPANISH_RELIGIOUS_POLICY", "note": "Philip II authorised Alba's extraordinary powers — and approved the Council of Troubles — as part of his determination to suppress Protestantism throughout his empire"}
        ],
    }),

    ("chambers-of-reunion", {
        "summary": (
            "The Chambers of Reunion (Chambres de Réunion, est. 1679–1684, France) were special courts established by Louis XIV to identify territories that had historically been part of French feudal dependencies and therefore were 'due' to France under the terms of various peace treaties — a legal pretext for a programme of annexation that expanded France's eastern frontier by incorporating Strasbourg (1681), Luxembourg (briefly), and numerous smaller territories. The Chambers of Reunion are the most audacious example of the use of legal procedure as a weapon of territorial aggrandisement in European history.\n\n"
            "Louis XIV created chambers in the parlements of Metz, Brisach, Besançon, and Tournai, charging them with researching the historical dependencies of territories France had received under previous treaties (Westphalia 1648, Nijmegen 1678). The Chambers' decisions were predetermined — they invariably found that the territories in question were historical French dependencies — and French troops occupied each territory as soon as the chamber issued its judgment. The most significant annexation was Strasbourg (September 1681) — an imperial free city of 20,000 people that was occupied without war while Louis XIV was nominally at peace with the Holy Roman Empire.\n\n"
            "The Chambers of Reunion represent the perfection of 'lawfare' — the use of legal procedure as an instrument of political and territorial aggrandisement — creating a template that has been cited in modern international law discussions of annexation and territorial claims based on historical legal arguments."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Louis XIV's special annexation courts (est. 1679–1684); most audacious use of legal procedure for territorial aggrandisement in European history; four chambers in Metz, Brisach, Besançon, Tournai; predetermined verdicts finding territories as French historical dependencies; annexed Strasbourg (1681) without war; occupied while nominally at peace; precedent for 'lawfare' — legal procedure as territorial weapon.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Louis XIV's determination to expand France's eastern frontier — securing the Rhine as a defensible natural border — drove the search for a legal mechanism that could justify territorial annexations without openly violating the Peace of Nijmegen (1678)",
            "The inherently ambiguous language of feudal dependency in medieval European territorial arrangements — where 'appurtenances' and 'dependencies' could be interpreted broadly or narrowly — provided the legal raw material for the Chambers' systematic reinterpretation of treaty terms in France's favour",
            "The Holy Roman Empire's weakness — divided among hundreds of principalities with no effective central army — made it unable to resist France's legal annexations with military force, creating the political conditions for Louis's lawfare strategy"
        ],
        "effects": [
            "The annexation of Strasbourg (1681) — France's most significant gain from the Chambers of Reunion — incorporated the largest free city on the Rhine into France, establishing the permanent French character of Alsace that has shaped Franco-German relations for 340 years",
            "The Chambers of Reunion established the template for 'lawfare' — the use of legal institutions and historical research as weapons of territorial annexation — creating a model that has been cited in 20th and 21st century discussions of territorial claims based on historical legal arguments",
            "The outrage provoked by Louis's Chambers of Reunion — and the Revocation of the Edict of Nantes (1685) — created the broad European coalition (the League of Augsburg, 1686) that fought France in the Nine Years' War (1688–1697), demonstrating that judicial aggression could produce military counter-coalitions",
            "Strasbourg's annexation began the cultural transformation of Alsace from German-speaking imperial territory to a bilingual Franco-German borderland — establishing the 'Alsace question' that would be central to Franco-German relations from 1681 through World War II and the post-war European integration"
        ],
        "relationships": [
            {"entity": "Louis XIV (Sun King)", "relationship": "CREATED_AS_TERRITORIAL_INSTRUMENT_BY", "note": "Louis XIV created the Chambers of Reunion (1679–1684) to provide legal justifications for annexing territories along France's eastern frontier"},
            {"entity": "Strasbourg (annexation 1681)", "relationship": "MOST_SIGNIFICANT_ANNEXATION_ACHIEVED_BY", "note": "The Chambers' most consequential decision was the annexation of Strasbourg (1681) — incorporating the largest Rhine free city into France and establishing Alsace's French character"},
            {"entity": "Peace of Nijmegen (1678)", "relationship": "LEGAL_PRETEXT_EXPLOITED_UNDER_THE_TERMS_OF_THE", "note": "The Chambers reinterpreted the 'appurtenances' clauses of the Peace of Nijmegen to claim that hundreds of territories were French historical dependencies"},
            {"entity": "League of Augsburg (1686) and Nine Years' War (1688–1697)", "relationship": "PROVOCATIONS_CONTRIBUTING_TO_FORMATION_OF", "note": "Louis's Chambers of Reunion outraged European powers — contributing to the formation of the League of Augsburg coalition that fought France 1688–1697"},
            {"entity": "Alsace question (Franco-German relations)", "relationship": "INITIATED_THE_CENTURIES-LONG", "note": "Strasbourg's 1681 annexation began the Alsace question that would dominate Franco-German relations from 1681 through World War II"}
        ],
    }),

    ("european-court", {
        "summary": (
            "The European Court of Justice (ECJ, est. 1952, Luxembourg — originally the ECSC Court of Justice; current name from Treaty of Rome 1957) is the supreme judicial institution of the European Union — the court that interprets EU law, settles disputes between EU institutions and member states, and ensures the uniform application of EU law across all 27 member states. The ECJ has been the most powerful supranational court in history, issuing judgments that have expanded EU competence, established the supremacy and direct effect of EU law, and fundamentally transformed the constitutional relationship between member states and the EU.\n\n"
            "The ECJ's two foundational doctrines — established by judges creating new law rather than interpreting existing treaty text — are the supremacy of EU law over national law (Van Gend en Loos, 1963; Costa v. ENEL, 1964) and the direct effect of EU law in national courts (Van Gend en Loos, 1963). These doctrines — not explicitly in the founding treaties — were created by the ECJ judges themselves, transforming the EU from a traditional international organisation (where treaty obligations are between states) into a constitutional order (where individuals can claim rights directly under EU law against their own governments).\n\n"
            "The ECJ's activist jurisprudence has repeatedly expanded EU competence beyond what member states intended — expanding the internal market, striking down national environmental and product regulations, enforcing fundamental rights, and interpreting EU competition law in ways that have shaped European corporate behaviour. The court's willingness to expand EU law at the expense of national law has made it both the EU's most powerful integrating force and the most controversial EU institution among national governments."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Supreme judicial institution of EU (est. 1952); most powerful supranational court in history; created supremacy of EU law over national law (Costa v. ENEL 1964); created direct effect doctrine (Van Gend en Loos 1963); judge-made constitutional doctrines not explicit in founding treaties; 27 member states; activist jurisprudence expanding EU competence; most powerful integrating force and most controversial EU institution.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The founders' ambiguity about the legal relationship between EU treaties and national law — leaving unanswered whether EU law or national law should prevail in cases of conflict — created the judicial vacuum that the ECJ filled with its supremacy and direct effect doctrines",
            "The ECJ judges' commitment to the 'teleological' (purposive) method of legal interpretation — interpreting EU law in light of the integration objectives of the treaties — drove them to read EU legal competences expansively rather than literally, consistently favouring deeper integration",
            "The ECJ's unique position as the court of a legal system with no enforcement mechanism of its own — relying on national courts to apply EU law — drove the development of direct effect as the mechanism for making EU law enforceable without needing the Commission or Council to act in every case"
        ],
        "effects": [
            "The supremacy doctrine (Costa v. ENEL, 1964) — holding that EU law takes precedence over national law in cases of conflict, including national constitutions — fundamentally transformed the relationship between EU members and the EU from international law (states retain sovereignty) to constitutional law (citizens are directly subject to EU authority)",
            "The direct effect doctrine (Van Gend en Loos, 1963) — allowing individuals to invoke EU law rights directly before national courts — created a system in which 500 million EU citizens can enforce EU rights against their own governments, making every national court an EU court and every EU citizen a potential litigant against their state",
            "The ECJ's expansion of the internal market through the Cassis de Dijon (1979) and Dassonville (1974) judgments — establishing mutual recognition and prohibiting national restrictions on trade — created the legal foundations of the EU Single Market that the 1986 Single European Act formally completed",
            "The ECJ's fundamental rights jurisprudence — developing an EU Charter of Fundamental Rights that the ECJ has interpreted expansively — has created an EU human rights order that operates alongside (and sometimes conflicts with) the European Convention on Human Rights and national constitutional rights frameworks"
        ],
        "relationships": [
            {"entity": "Van Gend en Loos (1963) — direct effect doctrine", "relationship": "CREATED_THE_FOUNDATIONAL_DOCTRINE_OF_DIRECT_EFFECT_IN", "note": "Van Gend en Loos (1963) established that individuals can invoke EU law directly before national courts — the foundational doctrine of the EU constitutional order"},
            {"entity": "Costa v. ENEL (1964) — supremacy of EU law", "relationship": "ESTABLISHED_SUPREMACY_OF_EU_LAW_OVER_NATIONAL_LAW_IN", "note": "Costa v. ENEL (1964) established that EU law takes precedence over national law — the most consequential single judgment in European legal history"},
            {"entity": "EU Single Market (legal foundation)", "relationship": "PROVIDED_JUDICIAL_FOUNDATION_FOR_THE", "note": "Dassonville (1974) and Cassis de Dijon (1979) judgments established mutual recognition and prohibited national trade restrictions — creating the legal foundation of the EU Single Market"},
            {"entity": "European Union (constitutional order)", "relationship": "SUPREME_JUDICIAL_INSTITUTION_OF_THE", "note": "The ECJ's supremacy and direct effect doctrines transformed the EU from an international organisation into a constitutional order — making the ECJ its supreme court"},
            {"entity": "National constitutional courts (EU member states)", "relationship": "IN_CONSTITUTIONAL_DIALOGUE_AND_TENSION_WITH", "note": "The ECJ's supremacy claims are challenged by German, Polish, and other national constitutional courts — creating ongoing constitutional dialogue about the limits of EU supremacy"}
        ],
    }),

    ("international-court", {
        "summary": (
            "The International Court of Justice (ICJ, est. 1945, The Hague — successor to the Permanent Court of International Justice, 1920) is the primary judicial organ of the United Nations — the world's principal court for settling legal disputes between states and providing advisory opinions on international law questions referred by UN bodies. The ICJ's 15 judges are elected by the UN General Assembly and Security Council, and the Court exercises jurisdiction over contentious cases between states that have accepted its jurisdiction.\n\n"
            "The ICJ is one of the oldest international courts — its predecessor, the Permanent Court of International Justice (PCIJ, 1920–1946), was the first permanent international court — and has adjudicated some of the most consequential disputes in international law: the Corfu Channel case (1949, first ICJ judgment), the Nicaragua v. United States case (1986, finding the US illegally mined Nicaragua's harbours), the Genocide Convention cases (Bosnia v. Serbia; Gambia v. Myanmar), and the Wall in the Occupied Palestinian Territory advisory opinion (2004).\n\n"
            "The ICJ's fundamental limitation is its lack of enforcement power: its judgments are binding in international law but the Security Council is the enforcement mechanism, and the P5 veto means that judgments against major powers (including the US, Russia, and China) cannot be enforced. The US withdrew its acceptance of compulsory jurisdiction (1985) after the Nicaragua judgment, and Russia ignored the ICJ's order to suspend its Ukraine invasion (2022). Despite these limitations, the ICJ remains the supreme authority on public international law and its judgments shape state behaviour through diplomatic and reputational consequences."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Primary UN judicial organ (est. 1945); principal court for settling disputes between states; successor to PCIJ (1920); Nicaragua v. US (1986) — US illegally mined harbours; Genocide Convention cases (Bosnia/Serbia, Gambia/Myanmar); Wall in OPT advisory opinion (2004); 15 judges elected by UN GA and SC; no enforcement power — P5 veto blocks enforcement; US withdrew compulsory jurisdiction (1985); Russia ignored Ukraine order (2022).",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The League of Nations' creation of the Permanent Court of International Justice (1920) — the first attempt at a permanent international court for state disputes — established the institutional model that the UN continued with the ICJ",
            "The UN Charter's commitment to the peaceful settlement of disputes — and the recognition that a permanent court was needed to provide authoritative interpretations of international law — drove the creation of the ICJ as the UN's principal judicial organ",
            "The post-World War II consensus on international law as the alternative to war — and the recognition that states needed a forum where disputes could be resolved through legal argument rather than force — created the political support for a court with compulsory jurisdiction over accepting states"
        ],
        "effects": [
            "The Nicaragua v. United States case (1986) — finding the US guilty of violating international law by mining Nicaragua's harbours and supporting the Contras — established that even superpowers are subject to international law, even if the P5 veto prevents enforcement",
            "The Genocide Convention cases — Bosnia and Herzegovina v. Serbia and Montenegro (2007) and Gambia v. Myanmar (2019) — established the ICJ as the primary forum for holding states accountable for genocide, directly applying the Genocide Convention's 'responsibility to prevent and punish' obligation",
            "The Wall in the Occupied Palestinian Territory advisory opinion (2004) — finding Israel's security barrier illegal under international law — is the most politically significant ICJ advisory opinion, shaping international discussions of the Israeli-Palestinian conflict and international humanitarian law",
            "The ICJ's accumulated jurisprudence — interpreting the UN Charter, the Vienna Convention on the Law of Treaties, the Genocide Convention, and customary international law — has created the primary authoritative corpus of international law, making it the supreme reference for international lawyers worldwide"
        ],
        "relationships": [
            {"entity": "Permanent Court of International Justice (PCIJ, 1920–1946)", "relationship": "SUCCESSOR_TO_THE", "note": "The ICJ succeeded the PCIJ — continuing the first permanent international court tradition with updated UN institutional backing"},
            {"entity": "Nicaragua v. United States (1986)", "relationship": "ADJUDICATED_THE_LANDMARK", "note": "The ICJ found the US guilty of illegally mining Nicaragua's harbours — establishing that superpowers are subject to international law, even without enforcement"},
            {"entity": "Gambia v. Myanmar (Genocide Convention)", "relationship": "ADJUDICATING_GENOCIDE_ACCOUNTABILITY_IN", "note": "The Gambia v. Myanmar case — applying the Genocide Convention to Rohingya persecution — is the ICJ's most current major genocide accountability proceeding"},
            {"entity": "Wall in Occupied Palestinian Territory (advisory opinion, 2004)", "relationship": "ISSUED_MOST_POLITICALLY_SIGNIFICANT_ADVISORY_OPINION_ON_THE", "note": "The 2004 Wall advisory opinion — finding Israel's security barrier illegal — is the most politically significant ICJ opinion and central to international discussions of the Israeli-Palestinian conflict"},
            {"entity": "UN Security Council (enforcement mechanism)", "relationship": "DEPENDS_ON_FOR_ENFORCEMENT_BUT_BLOCKED_BY_P5_VETO_OF", "note": "The ICJ has no direct enforcement power — the Security Council is supposed to enforce its judgments, but P5 members use their veto to block enforcement against themselves"}
        ],
    }),

    ("supreme-court-united-states", {
        "summary": (
            "The Supreme Court of the United States (SCOTUS, est. 1789 — Article III of US Constitution; first session 2 February 1790) is the highest court in the United States federal judiciary — the final interpreter of the US Constitution and federal law, with the power of judicial review over federal and state legislation. The Supreme Court's decisions have shaped American society more than any other institution except perhaps the Presidency: from Marbury v. Madison (1803, establishing judicial review) to Dred Scott (1857, striking down the Missouri Compromise), to Brown v. Board of Education (1954, desegregating schools), to Roe v. Wade (1973, abortion rights) and Dobbs v. Jackson (2022, overturning Roe).\n\n"
            "The Supreme Court's power of judicial review — the authority to strike down federal and state laws as unconstitutional — was not explicit in the Constitution but was asserted by Chief Justice John Marshall in Marbury v. Madison (1803), in what is arguably the single most consequential judicial decision in history. This self-created power transformed the Court from the 'least dangerous branch' (Hamilton's prediction in Federalist No. 78) into arguably the most powerful branch of government on constitutional questions.\n\n"
            "The Court's 9 justices serve lifetime appointments — giving Supreme Court nominations enormous political stakes, as each appointment shapes the law for decades. The Senate's role in confirming justices (and blocking Obama's Merrick Garland nomination in 2016) has made the Supreme Court the most contested political prize in American politics, with the 2020s Court reflecting a 6-3 conservative supermajority that has overturned decades of liberal precedent on abortion, voting rights, and administrative law."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Highest US federal court (est. 1789); power of judicial review asserted by John Marshall in Marbury v. Madison (1803); shaped US society: Dred Scott (1857), Brown v. Board (1954), Roe v. Wade (1973), Dobbs (2022); 9 justices with lifetime appointments; Merrick Garland nomination blocked (2016); 6-3 conservative supermajority (2020s) overturning liberal precedent on abortion, voting rights, administrative law.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The US Constitution's Article III — creating a federal judiciary with a Supreme Court — established the institutional framework without explicitly granting judicial review power, creating the ambiguity that Marshall resolved in Marbury v. Madison",
            "The Framers' distrust of majority rule — and their commitment to protecting minority rights and constitutional limits on government — created the theoretical rationale for an unelected court with the power to strike down popular legislation",
            "The US political system's weak party discipline — making legislative solutions to constitutional questions politically difficult — has repeatedly created the demand for Supreme Court resolution of contested social and political questions that democratic majorities could not resolve"
        ],
        "effects": [
            "Marbury v. Madison (1803) — Marshall's assertion of judicial review — transformed the Supreme Court from a minor institution into the final arbiter of constitutional meaning, making the US the first constitutional democracy where an unelected court can invalidate legislation passed by elected representatives",
            "Brown v. Board of Education (1954) — the unanimous decision that racial segregation in public schools violated the Equal Protection Clause — was the single most transformative judicial decision in American social history, catalysing the Civil Rights Movement and ending the legal framework of segregation",
            "Roe v. Wade (1973) and its overturning in Dobbs v. Jackson Women's Health Organization (2022) — the most significant doctrinal reversal in Court history — demonstrate that constitutional rights previously considered settled can be eliminated by a changed Court composition, making the Court's political composition the central question of American politics",
            "The Supreme Court's power to shape law through its constitutional interpretations — on civil rights, voting rights, abortion, gun control, administrative law, and federalism — has made it the central battlefield of American political conflict, with presidential elections fought partly over their implications for Court composition"
        ],
        "relationships": [
            {"entity": "Marbury v. Madison (1803 — judicial review)", "relationship": "ASSERTED_POWER_OF_JUDICIAL_REVIEW_IN", "note": "Marshall's Marbury v. Madison (1803) created the power of judicial review — the most consequential self-created judicial power in legal history"},
            {"entity": "Brown v. Board of Education (1954)", "relationship": "ISSUED_THE_TRANSFORMATIVE_DESEGREGATION_RULING_IN", "note": "Brown (1954) — unanimously ruling racial segregation unconstitutional — catalysed the Civil Rights Movement and was the most transformative judicial decision in American social history"},
            {"entity": "Roe v. Wade (1973) and Dobbs v. Jackson (2022)", "relationship": "ISSUED_AND_OVERTURNED_ABORTION_RIGHTS_PRECEDENT_IN", "note": "Roe (1973) created a constitutional abortion right; Dobbs (2022) overturned it — the most dramatic doctrinal reversal in Court history"},
            {"entity": "US Senate confirmation power (Supreme Court nominations)", "relationship": "COMPOSITION_DETERMINED_THROUGH_THE", "note": "The Senate's role in confirming justices — and blocking Merrick Garland (2016) — has made Court nomination the central battlefield of US political conflict"},
            {"entity": "US Constitution (Article III)", "relationship": "CREATED_BY_THE_AUTHORITY_OF", "note": "Article III of the Constitution established the Supreme Court — though without explicitly granting judicial review, the power Marshall asserted in Marbury"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 29 — {len(ENTITIES)} entities (Class 321: Famous Courts, Councils & Tribunals)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
