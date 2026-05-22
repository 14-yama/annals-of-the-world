#!/usr/bin/env python3
"""
Batch 08 — 8 entities (Class 313): Government/Cabinet institutions
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/313-Class-313"
FILE_PREFIX = "313"
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

    ("batavian-republic", {
        "summary": (
            "The Batavian Republic (1795–1806) was the French-client republic established in the Netherlands following the French Revolutionary Army's invasion and the flight of Stadtholder William V. Named after the Batavi — the ancient Germanic tribe of the Rhine delta celebrated in Dutch national mythology — the Batavian Republic was the first formally republican government of the Netherlands, replacing the centuries-old Dutch Republic's oligarchic regent system.\n\n"
            "The Batavian Republic was established with genuine Dutch revolutionary enthusiasm: the Patriots — a reform movement that had been suppressed by Prussian military intervention in 1787 — embraced the French alliance as liberation. The republic adopted a written constitution (1798) — one of Europe's first modern constitutions — establishing civil equality, freedom of religion, and representative government. Jews and Catholics were granted full civil rights for the first time. The republic nationalised the formerly provincial Dutch institutions into a centralised unitary state.\n\n"
            "Napoleon transformed the Batavian Republic into the Kingdom of Holland (1806) under his brother Louis Bonaparte, then annexed the Netherlands directly into France (1810–1813). The republic's constitutional and administrative reforms — centralisation, civil equality, a national tax system — proved durable: they survived Napoleon's fall and shaped the Kingdom of the Netherlands established at the Congress of Vienna (1815), providing the modern Dutch state's institutional foundations."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "French-client republic in the Netherlands (1795–1806); one of Europe's first modern constitutions (1798); granted civil equality to Jews and Catholics; centralised the formerly provincial Dutch state; its administrative reforms provided the institutional foundations of the modern Kingdom of the Netherlands.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The French Revolutionary Army's invasion of the Netherlands (1795) — enabled by the exceptional winter that froze the Dutch waterways, neutralising the Dutch defensive flooding strategy — overthrew the Orangist Stadtholder and enabled the Dutch Patriots to establish a republic",
            "The Dutch Patriot movement (suppressed in 1787 by Prussian intervention) had developed a systematic reform programme — inspired by American and French revolutionary ideas — that was waiting for the political opportunity the French invasion provided",
            "The Dutch Republic's fundamental institutional contradiction — a federal oligarchy in which a handful of regent families controlled urban governments while claiming to represent popular sovereignty — had created the reform impulse that the revolution channelled"
        ],
        "effects": [
            "The Batavian Constitution (1798) — one of Europe's first written constitutions — established civil equality, freedom of religion, and representative government, granting full civil rights to Jews and Catholics for the first time in Dutch history",
            "The Batavian Republic's centralisation of the formerly provincial Dutch state — creating national institutions for taxation, education, and administration — provided the institutional template for the modern Dutch state that emerged from the Napoleonic period",
            "The annexation of the Netherlands into France (1810) introduced French law (the Napoleonic Code), the metric system, and conscription — institutions that, selectively, persisted after 1813 and shaped the modern Netherlands",
            "The Batavian Republic's emancipation of Dutch Jews — granting full civil rights in 1796 — created the legal equality that made the Netherlands home to one of Europe's most integrated Jewish communities, until the Holocaust devastated Dutch Jewry in 1940–1945"
        ],
        "relationships": [
            {"entity": "French Revolutionary Republic", "relationship": "ESTABLISHED_UNDER_SPONSORSHIP_OF", "note": "The Batavian Republic was established following the French Revolutionary Army's invasion (1795) — a French-client state of the revolutionary period"},
            {"entity": "Dutch Patriot movement", "relationship": "POLITICAL_PROGRAMME_IMPLEMENTED_BY", "note": "The Dutch Patriots — suppressed in 1787 — implemented their reform programme through the Batavian Republic"},
            {"entity": "Kingdom of Holland", "relationship": "TRANSFORMED_INTO_BY_NAPOLEON", "note": "Napoleon transformed the Batavian Republic into the Kingdom of Holland (1806) under his brother Louis Bonaparte"},
            {"entity": "Dutch Republic (Seven United Provinces)", "relationship": "ABOLISHED_AND_SUCCEEDED", "note": "The Batavian Republic abolished the Dutch Republic's centuries-old oligarchic structure and replaced it with a unitary republic"},
            {"entity": "Kingdom of the Netherlands (1815)", "relationship": "INSTITUTIONAL_FOUNDATIONS_PROVIDED_FOR", "note": "The Batavian Republic's constitutional and administrative reforms — centralisation, civil equality — provided the institutional foundations of the modern Kingdom of the Netherlands"}
        ],
    }),

    ("aristocratic-republic-of-poland", {
        "summary": (
            "The Polish-Lithuanian Commonwealth (1569–1795) — often called the Noble Republic or Aristocratic Republic of Poland — was one of the largest and most unusual political entities in European history: an elective monarchy in which the king was elected by the entire Polish and Lithuanian nobility (szlachta), with royal power severely constrained by noble prerogatives and the requirement of unanimity (the liberum veto) for any legislation. At its peak in the 17th century, the Commonwealth encompassed Poland, Lithuania, Latvia, Estonia, Belarus, Ukraine, and parts of Russia — stretching from the Baltic to the Black Sea.\n\n"
            "The Commonwealth's constitutional system was simultaneously its cultural glory and political disaster: the szlachta's legal equality ('Golden Freedom'), the tolerance of religious minorities that made 16th-century Poland a refuge for Protestant, Orthodox, Jewish, and Armenian communities, and the vibrant parliamentary culture of the Sejm were admired across Europe. But the liberum veto — which allowed any single noble to dissolve the parliament and annul all its decisions — made effective governance impossible and was exploited by foreign powers (especially Russia and Prussia) to paralyse Polish legislation.\n\n"
            "The Commonwealth was partitioned three times (1772, 1793, 1795) by Russia, Prussia, and Austria, who absorbed its territories. The last partition (1795) erased Poland from the map of Europe for 123 years. The Commonwealth's legacy — its constitutional traditions, its intellectual culture (Copernicus, Jan Sobieski), and the Constitution of 3 May 1791 (Europe's first modern written constitution) — shaped Polish national identity through its long absence."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Polish-Lithuanian Commonwealth (1569–1795) — the Noble Republic; elective monarchy; remarkable religious tolerance; Constitution of 3 May 1791 was Europe's first modern written constitution; three partitions (1772–1795) erased Poland for 123 years; its legacy shaped Polish national identity.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Union of Lublin (1569) — merging the Kingdom of Poland and the Grand Duchy of Lithuania — created the Commonwealth as a unified constitutional state with a joint Sejm (parliament), providing the institutional framework for the Noble Republic",
            "The Jagiellonian dynasty's extinction (1572) created the first royal election — establishing the principle of an elective monarchy that became the Commonwealth's constitutional foundation and ultimately its greatest weakness",
            "The szlachta's (nobility's) resistance to royal absolutism — rooted in the Nihil Novi constitution (1505) that prohibited the king from legislating without noble consent — established the political tradition that evolved into the Commonwealth's Noble Republic system"
        ],
        "effects": [
            "The liberum veto — the right of any single noble to dissolve parliament — became increasingly weaponised in the 17th–18th centuries, paralysing Polish governance and making the Commonwealth vulnerable to foreign manipulation and partition",
            "The Constitution of 3 May 1791 — abolishing the liberum veto, establishing a hereditary constitutional monarchy, and granting rights to townspeople — was Europe's first modern written constitution, reflecting Enlightenment political thought and inspiring democratic movements across Europe",
            "The three partitions of Poland (1772, 1793, 1795) — by Russia, Prussia, and Austria — erased Poland from the European map for 123 years (1795–1918), making the partitions the defining trauma of Polish national memory and political consciousness",
            "The Commonwealth's remarkable religious tolerance — making 16th-century Poland a refuge for Protestants, Orthodox Christians, Jews, and Armenians — created the most religiously diverse country in Europe and the largest Jewish community in the world, whose legacy shaped Poland's complex religious history"
        ],
        "relationships": [
            {"entity": "Union of Lublin (1569)", "relationship": "CREATED_BY", "note": "The Union of Lublin (1569) merged Poland and Lithuania into the Commonwealth — establishing the Noble Republic's institutional framework"},
            {"entity": "Constitution of 3 May 1791", "relationship": "ISSUED", "note": "The Commonwealth issued Europe's first modern written constitution (3 May 1791) — abolishing the liberum veto and establishing constitutional monarchy"},
            {"entity": "Liberum veto", "relationship": "PARALYSED_BY", "note": "The liberum veto — allowing any single noble to dissolve parliament — paralysed Commonwealth governance and was exploited by foreign powers"},
            {"entity": "Partitions of Poland (1772–1795)", "relationship": "ELIMINATED_BY", "note": "Three partitions (1772, 1793, 1795) by Russia, Prussia, and Austria erased the Commonwealth from the map — Poland's defining national trauma"},
            {"entity": "Polish szlachta (nobility)", "relationship": "GOVERNED_BY_AND_FOR", "note": "The szlachta's 'Golden Freedom' — legal equality among nobles and severe constraints on royal power — defined the Commonwealth's political character"}
        ],
    }),

    ("cabinet-of-the-united-kingdom", {
        "summary": (
            "The Cabinet of the United Kingdom is the senior decision-making body of the British government — a committee of the most senior ministers of the Crown, presided over by the Prime Minister, that collectively determines government policy. The Cabinet system evolved from the 17th-century practice of monarchs consulting a small inner circle of Privy Councillors, developing through the Whig-dominated ministries of the early 18th century into the modern convention that the Cabinet collectively advises the monarch while being accountable to the House of Commons.\n\n"
            "The British Cabinet model was one of the most influential constitutional innovations in modern governance history: the principles of collective cabinet responsibility (all ministers publicly support cabinet decisions), ministerial accountability to Parliament, and the Prime Minister's coordinating authority created the 'Westminster system' that was exported across the British Empire and adopted by India, Australia, Canada, New Zealand, and dozens of other states. The Westminster system is now the most widely-adopted model of parliamentary government in the world.\n\n"
            "The Cabinet's evolution reflects the fundamental transformation of British governance from royal absolutism to parliamentary democracy: from Charles II's 'Cabal' ministry (1668–1674) — the nickname that may have given 'cabinet' its political meaning — through Robert Walpole's innovation of collective ministry (1721–1742) to the modern Cabinet's comprehensive oversight of Britain's nuclear deterrent, foreign policy, and economic strategy."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Senior decision-making body of the UK government; its evolution created the Westminster system — now the most widely-adopted model of parliamentary government in the world; adopted by India, Australia, Canada, and dozens of other states; collective cabinet responsibility is its most influential constitutional innovation.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Charles II's practice of consulting a small inner committee of the Privy Council ('the Cabal', 1668–1674) — bypassing the full Privy Council — established the precedent of an inner cabinet of senior ministers distinct from the broader advisory body",
            "Robert Walpole's 21-year ministry (1721–1742) consolidated the convention that the chief minister (Prime Minister) must maintain majority support in the House of Commons — linking cabinet government to parliamentary accountability",
            "The Glorious Revolution (1688) and its constitutional settlement — establishing parliamentary supremacy over the Crown — created the political framework in which Cabinet government, accountable to Parliament rather than the monarch, became the logical form of executive organisation"
        ],
        "effects": [
            "The Westminster system — Cabinet collective responsibility, Prime Minister coordinating authority, ministerial accountability to Parliament — was exported across the British Empire and is now the governing model for approximately 60 countries including India, Australia, Canada, New Zealand, and most Commonwealth nations",
            "The convention of collective cabinet responsibility — all ministers publicly support cabinet decisions or resign — created the constitutional principle that party discipline and collective governance are inseparable in parliamentary government",
            "The British Cabinet's role in managing the two World Wars — from Asquith's War Committee (1914) to Churchill's War Cabinet (1940–1945) — demonstrated that parliamentary cabinet government could mobilise national resources as effectively as authoritarian regimes",
            "The Cabinet's evolution demonstrates the 'unwritten constitution' model — a constitutional system based on conventions, precedents, and statutes rather than a single codified document — that has been both admired and criticised as a model of constitutional governance"
        ],
        "relationships": [
            {"entity": "Prime Minister of the United Kingdom", "relationship": "CHAIRED_BY", "note": "The Prime Minister chairs the Cabinet and coordinates its collective decision-making — the office and institution co-evolved"},
            {"entity": "Westminster system", "relationship": "CREATED_MODEL_FOR", "note": "The British Cabinet created the Westminster system — adopted by approximately 60 countries including India, Australia, Canada, and most Commonwealth nations"},
            {"entity": "Robert Walpole", "relationship": "MODERN_CONVENTION_ESTABLISHED_BY", "note": "Robert Walpole (1721–1742) consolidated the convention of parliamentary accountability for cabinet government — he is regarded as Britain's first Prime Minister"},
            {"entity": "House of Commons", "relationship": "ACCOUNTABLE_TO", "note": "Cabinet collective responsibility — all ministers are collectively accountable to the House of Commons — is the Cabinet's defining constitutional principle"},
            {"entity": "Glorious Revolution (1688)", "relationship": "CONSTITUTIONAL_FOUNDATION_PROVIDED_BY", "note": "The Glorious Revolution's establishment of parliamentary supremacy created the framework in which Cabinet government, accountable to Parliament, became the natural executive form"}
        ],
    }),

    ("council-of-ministers-of-the-soviet-union", {
        "summary": (
            "The Council of Ministers of the Soviet Union (1946–1991) was the highest executive and administrative organ of the Soviet state — the formal government of the USSR, responsible for implementing Communist Party decisions and administering the state economy, defence, and foreign policy. Its chairman (Premier) was formally the head of government, though actual power resided in the Politburo of the Communist Party. Notable chairmen included Vyacheslav Molotov, Georgy Malenkov, Nikita Khrushchev (1958–1964), Alexei Kosygin, and Nikolai Ryzhkov.\n\n"
            "The Council of Ministers was the formal institutional centre of Soviet governmental administration — a massive bureaucratic apparatus managing the world's largest planned economy, the Soviet military-industrial complex, and the administrative apparatus of 15 union republics. Its relationship to the Politburo was constitutionally subordinate but practically complex: some party leaders (Stalin, Khrushchev) held both positions simultaneously, while others — particularly Alexei Kosygin (Premier 1964–1980) — exercised significant autonomous authority in economic management.\n\n"
            "The Council of Ministers was renamed the Cabinet of Ministers in 1991 as part of Gorbachev's constitutional reforms, and was dissolved following the August Coup and Soviet collapse. Its successor, the Government of the Russian Federation, inherited much of its administrative structure and personnel — demonstrating the durability of Soviet institutional patterns in post-Soviet Russia."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Highest executive organ of the Soviet state (1946–1991); managed the world's largest planned economy; its chairmen included Molotov, Khrushchev, and Kosygin; its administrative structure was inherited by the Government of the Russian Federation — Soviet institutional patterns persisting in post-Soviet Russia.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The October Revolution (1917) and the subsequent Bolshevik consolidation created the Soviet state structure — initially the Council of People's Commissars (Sovnarkom, 1917–1946) renamed the Council of Ministers in 1946 — as the formal government distinct from the party apparatus",
            "Stalin's concentration of both party (General Secretary) and government (Chairman of Council of Ministers from 1941) authority in himself created the template of dual party-state power that shaped the Council of Ministers' subordinate relationship to the Politburo",
            "The Soviet command economy — central planning through GOSPLAN, sector ministries, and five-year plans — required an administrative apparatus of enormous complexity that the Council of Ministers provided, managing every sector of the USSR's economy from steel production to bread pricing"
        ],
        "effects": [
            "The Council of Ministers administered the world's largest planned economy for 45 years — its successes (rapid industrialisation, space programme, military parity with the US) and failures (chronic consumer goods shortages, agricultural crisis) shaped the 20th century's political economy debate",
            "Alexei Kosygin's economic reforms (1965) — introducing profit incentives and enterprise autonomy within the socialist framework — were the most significant attempt to reform the Soviet command economy, and their partial failure influenced later assessments of Soviet reformability",
            "The Council of Ministers' administrative personnel and institutional structures were largely inherited by the Government of the Russian Federation after the Soviet collapse — making the Soviet administrative tradition foundational to post-Soviet Russian governance",
            "The Council of Ministers' model — a formal government subordinate to a ruling party's executive committee — was replicated across the Warsaw Pact states, China, Vietnam, Cuba, and other communist states, becoming the standard administrative structure of 20th-century communist governance"
        ],
        "relationships": [
            {"entity": "Politburo of the Communist Party of the Soviet Union", "relationship": "SUBORDINATE_TO_IN_ACTUAL_POWER", "note": "The Council of Ministers was formally the highest executive organ but actual power resided in the Politburo — the party's supreme decision-making body"},
            {"entity": "Alexei Kosygin", "relationship": "MOST_SIGNIFICANT_ECONOMIC_ADMINISTRATOR_OF", "note": "Kosygin (Premier 1964–1980) was the Council's most significant economic administrator — his 1965 reforms were the most serious attempt to reform the Soviet planned economy"},
            {"entity": "Joseph Stalin", "relationship": "CONCENTRATED_PARTY_AND_GOVERNMENT_POWER_UNDER", "note": "Stalin served as both General Secretary and Chairman of Council of Ministers (from 1941) — establishing the template of dual party-state leadership"},
            {"entity": "Soviet command economy (GOSPLAN)", "relationship": "ADMINISTRATIVE_AUTHORITY_OVER", "note": "The Council of Ministers administered the Soviet command economy through GOSPLAN and sector ministries — managing every sector of the USSR's economic life"},
            {"entity": "Government of the Russian Federation", "relationship": "ADMINISTRATIVE_SUCCESSOR_TO", "note": "The Government of the Russian Federation inherited much of the Council of Ministers' administrative structure — Soviet institutional patterns persisting in post-Soviet Russia"}
        ],
    }),

    ("cabinet-of-india", {
        "summary": (
            "The Union Cabinet of India is the highest decision-making body of the Indian government — a council of senior ministers presided over by the Prime Minister that collectively determines the policy of the world's largest democracy. Constitutionally established under Article 75 of the Indian Constitution (1950), the Cabinet is collectively responsible to the Lok Sabha (lower house of Parliament) and operates on the Westminster system inherited from British colonial governance. The Cabinet is supported by the Cabinet Secretariat — one of the most powerful bureaucratic institutions in the Indian administrative system.\n\n"
            "The Indian Cabinet system has been exercised by Prime Ministers whose tenures have shaped modern India: Jawaharlal Nehru (1947–1964) established India's non-aligned foreign policy and state-led development model; Indira Gandhi (1966–1984) declared the Emergency (1975–1977) and introduced constitutional amendments that concentrated power in the executive; P.V. Narasimha Rao (1991–1996) under Finance Minister Manmohan Singh liberalised India's economy, beginning the transformation from a socialist mixed economy to a market economy.\n\n"
            "The Cabinet's collective decision-making has been repeatedly tested by coalition politics: from 1989 to 2014, no single party won a parliamentary majority, requiring coalition cabinets of 15–25 parties whose internal negotiations defined Indian governance. Narendra Modi's BJP majority governments (2014–present) restored single-party Cabinet dominance — demonstrating the Cabinet's different character under majority versus coalition conditions."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Highest decision-making body of the world's largest democracy (est. 1950); Nehru's Cabinet established non-alignment and state-led development; Rao-Singh Cabinet (1991) liberalised India's economy; the Cabinet system governs 1.4 billion people and is one of the most consequential applications of the Westminster model.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Indian Constitution (1950) — drawing on the Westminster model while adapting it to India's federal, multi-linguistic, and multi-religious context — established the Cabinet system as the constitutional centre of executive authority in an independent India",
            "British colonial governance's institutional legacy — the Indian Civil Service, parliamentary procedure, and cabinet government conventions — provided the administrative infrastructure that India's post-independence leadership inherited and adapted",
            "The Indian independence movement's democratic commitments — Nehru's personal vision of parliamentary democracy, the Congress Party's constitutional traditions — created the political culture that made the Westminster cabinet model the natural choice for independent India"
        ],
        "effects": [
            "Nehru's Cabinet (1947–1964) — implementing the Nehruvian development model of state-led industrialisation, five-year plans, and non-alignment — shaped India's economic and foreign policy for the following three decades",
            "The Rao-Singh Cabinet's economic liberalisation (1991) — dismantling the 'License Raj', reducing import tariffs, and deregulating key industries — began India's transformation into a major emerging economy, lifting hundreds of millions out of poverty over the following decades",
            "India's experience of coalition Cabinet government (1989–2014) — managing 20+ party coalitions — developed unique institutional practices for multi-party executive governance that have influenced comparative constitutional scholarship",
            "The Indian Cabinet system's 75-year operation in the world's most demographically complex democracy provides the most important test case for the Westminster model's adaptability — demonstrating that parliamentary cabinet government can function in a federal, multi-religious state of 1.4 billion people"
        ],
        "relationships": [
            {"entity": "Prime Minister of India", "relationship": "PRESIDED_OVER_BY", "note": "The Prime Minister chairs the Union Cabinet — the office and institution are constitutionally and practically inseparable"},
            {"entity": "Jawaharlal Nehru", "relationship": "FIRST_AND_MOST_FORMATIVE_PRIME_MINISTER_OF", "note": "Nehru's 17-year tenure (1947–1964) established India's non-aligned foreign policy, state-led development model, and Cabinet governance traditions"},
            {"entity": "1991 Indian economic liberalisation", "relationship": "DECIDED_BY", "note": "The Rao Cabinet — with Finance Minister Manmohan Singh — decided India's 1991 liberalisation, beginning its economic transformation"},
            {"entity": "Indian Constitution (1950)", "relationship": "CONSTITUTIONALLY_ESTABLISHED_BY", "note": "Article 75 of the Indian Constitution (1950) established the Cabinet system — constitutionally mandating collective responsibility to the Lok Sabha"},
            {"entity": "Westminster system", "relationship": "MOST_SIGNIFICANT_APPLICATION_OF", "note": "India's Cabinet is the most significant application of the Westminster system — governing 1.4 billion people in the world's largest democracy"}
        ],
    }),

    ("federal-council-of-switzerland", {
        "summary": (
            "The Federal Council of Switzerland (Bundesrat/Conseil fédéral) is the seven-member collegial executive of the Swiss Confederation — one of the world's most distinctive governmental institutions, combining collective presidency with ministerial responsibility in a permanent power-sharing arrangement among Switzerland's major political parties. Established by the Swiss Federal Constitution of 1848, the Federal Council operates on the 'magic formula' — an informal power-sharing convention established in 1959 — distributing the seven council seats proportionally among the four largest parties.\n\n"
            "The Federal Council's collegial structure — seven equal members who make decisions collectively, with a rotating annual presidency that confers no extra power — is unique among modern democracies. This design reflects Switzerland's deep commitment to consensus governance and its linguistic diversity (German, French, Italian, Romansh speakers share executive power). The Federal President, elected annually by the Federal Assembly, is 'first among equals' rather than a head of government in the conventional sense.\n\n"
            "Switzerland's Federal Council model has proven remarkably stable: the same four parties have shared power since 1959, and the country has navigated two world wars, the Cold War, and the digital revolution without significant governmental crisis. The model is the institutional embodiment of Swiss 'concordance democracy' — a form of consociational governance that manages linguistic, religious, and regional diversity through permanent power-sharing."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Seven-member collegial executive of Switzerland (est. 1848); unique 'magic formula' power-sharing among four parties since 1959; rotating annual presidency; the institutional embodiment of Swiss concordance democracy — managing linguistic and religious diversity through permanent power-sharing.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The 1848 Swiss Federal Constitution — transforming the Swiss Confederation from a loose alliance of cantons into a modern federal state — created the Federal Council as the constitutional executive, designed to balance cantonal sovereignty with federal authority",
            "Switzerland's linguistic, religious, and regional diversity — German, French, Italian; Protestant, Catholic; rural, urban — required a collegial executive that could represent all communities, making the power-sharing council model the natural constitutional solution",
            "The 1848 constitution's drafters drew on the United States Constitution (bicameral parliament, federal structure) while creating a distinctly Swiss executive — rejecting a single president in favour of collegial governance that reflected Swiss democratic traditions"
        ],
        "effects": [
            "The 'magic formula' (1959) — distributing Federal Council seats as 2 FDP + 2 CVP + 2 SP + 1 SVP (modified in 2003 to include SVP) — created the world's most stable example of permanent multi-party executive power-sharing, maintaining governmental stability for over 60 years",
            "Switzerland's Federal Council model influenced debates about consociational democracy — theorised by Arend Lijphart — and became the primary empirical reference for scholars studying how power-sharing arrangements manage deeply divided societies",
            "Switzerland's neutrality — maintained through two world wars — was partly made possible by the Federal Council's collegial structure, which prevented any single political faction from capturing foreign policy",
            "The Federal Council's administrative efficiency in managing Switzerland's complex federalism — 26 cantons with significant autonomy, four national languages, extensive direct democracy through referenda — provides a model for multi-level governance in diverse polities"
        ],
        "relationships": [
            {"entity": "Swiss Federal Constitution (1848)", "relationship": "ESTABLISHED_BY", "note": "The Federal Council was established by the 1848 Swiss Federal Constitution — transforming Switzerland from a confederation into a modern federal state"},
            {"entity": "Magic formula (Zauberformel, 1959)", "relationship": "GOVERNED_BY_POWER-SHARING_CONVENTION_OF", "note": "The 1959 'magic formula' distributes Federal Council seats proportionally among Switzerland's four major parties — creating permanent multi-party power-sharing"},
            {"entity": "Swiss neutrality", "relationship": "FOREIGN_POLICY_MAINTAINED_BY", "note": "The Federal Council's collegial structure prevented any single faction from capturing foreign policy — enabling Switzerland's perpetual neutrality through two world wars"},
            {"entity": "Consociational democracy", "relationship": "PRIMARY_EMPIRICAL_EXAMPLE_OF", "note": "Switzerland's Federal Council is the primary empirical reference for consociational democracy theory — studied as the model of permanent power-sharing in diverse societies"},
            {"entity": "Swiss direct democracy", "relationship": "COMBINED_WITH", "note": "The Federal Council operates alongside Switzerland's extensive direct democracy (referenda, initiatives) — making Swiss governance a unique combination of executive power-sharing and popular sovereignty"}
        ],
    }),

    ("government-of-france", {
        "summary": (
            "The Government of France (Gouvernement de la République française) — the executive branch headed by the Prime Minister — is the operational government of one of Europe's oldest and most influential states. France's governmental history is uniquely complex: since the Revolution (1789), France has experienced 5 republics, 2 empires, 2 monarchical restorations, and the Vichy regime — more governmental changes than any other major European democracy. The current Fifth Republic (1958) was designed by Charles de Gaulle to create stable executive governance through a semi-presidential system.\n\n"
            "The Fifth Republic's semi-presidential structure — with an elected President holding executive authority over foreign policy and defence, and a Prime Minister managing domestic governance and answerable to the National Assembly — created a distinctive 'dual executive' that has been studied as a model for post-authoritarian and post-conflict constitution-writing. The system was tested by 'cohabitation' (1986–1988, 1993–1995, 1997–2002) — periods when the President and Prime Minister were from opposing political parties.\n\n"
            "France's government has been one of the most globally influential executive systems in history: the Napoleonic Code (civil law system adopted by 70+ countries), the Declaration of the Rights of Man (1789), the French administrative model (prefects, grandes écoles, centralised state), and French foreign policy doctrine of 'grandeur' (independent nuclear deterrent, permanent UN Security Council seat, la Francophonie) all project French governmental traditions globally."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Executive branch of one of Europe's most historically influential states; 5 republics, 2 empires since 1789; the Fifth Republic (1958) created the semi-presidential 'dual executive' model adopted globally; the Napoleonic Code governs 70+ countries; France's governmental traditions project globally through la Francophonie and UN Security Council.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The French Revolution (1789) — overthrowing the Ancien Régime's royal absolutism — created the first French Republic and initiated France's turbulent cycle of republican, imperial, and monarchical regimes, establishing the Revolutionary tradition of governmental reinvention as a response to political crisis",
            "Charles de Gaulle's design of the Fifth Republic (1958) — responding to the Fourth Republic's governmental instability (25 governments in 12 years) and the Algerian crisis — created the semi-presidential system by strengthening the elected presidency while retaining parliamentary accountability for the government",
            "Napoleon Bonaparte's administrative revolution (1799–1814) — the Napoleonic Code, prefectural system, Conseil d'État, grandes écoles — created the centralised administrative state that all subsequent French governments have operated within"
        ],
        "effects": [
            "The Napoleonic Code (1804) — codifying civil law in 2,281 articles — became the model for civil law systems in 70+ countries, from Louisiana and Quebec to Japan, Turkey, and most of Latin America, making French legal tradition the world's most widely adopted",
            "The Fifth Republic's semi-presidential system has been adopted or adapted by Russia, many post-Soviet states, and numerous post-colonial African states — making France's 1958 constitutional design one of the most internationally influential constitutional models of the 20th century",
            "France's concept of the 'activist state' — state-directed economic planning (Commissariat au Plan), nationalisation of strategic industries, and the grandes écoles technocratic elite — provided an alternative model of capitalist development that influenced European and developing world economic policy throughout the post-war period",
            "France's permanent UN Security Council seat, independent nuclear deterrent, and la Francophonie (covering 54 countries and 300 million French speakers) make the French government one of the most globally powerful executives in the world — punching above its demographic weight through institutional and cultural leverage"
        ],
        "relationships": [
            {"entity": "French Revolution (1789)", "relationship": "FIRST_REPUBLIC_CREATED_BY", "note": "The French Revolution created the First Republic (1792) — beginning France's cycle of governmental transformation that has produced 5 republics, 2 empires, and 2 monarchical restorations"},
            {"entity": "Charles de Gaulle", "relationship": "FIFTH_REPUBLIC_DESIGNED_BY", "note": "De Gaulle designed the Fifth Republic (1958) — the semi-presidential system that has provided France's most stable republican governance"},
            {"entity": "Napoleonic Code (1804)", "relationship": "PRODUCED_AND_ADOPTED_IN_70_COUNTRIES", "note": "The Napoleonic Code — the French government's most globally influential institutional export — governs civil law in 70+ countries"},
            {"entity": "UN Security Council", "relationship": "PERMANENT_MEMBER_OF", "note": "France's permanent UN Security Council seat gives the French government veto power over the international security order"},
            {"entity": "La Francophonie", "relationship": "CULTURAL-POLITICAL_NETWORK_PROJECTED_THROUGH", "note": "La Francophonie (54 countries, 300 million speakers) is the French government's most effective instrument of global cultural and political influence"}
        ],
    }),

    ("government-of-germany", {
        "summary": (
            "The Federal Government of Germany (Bundesregierung) — the executive body headed by the Federal Chancellor (Bundeskanzler) — governs the Federal Republic of Germany, Europe's largest economy and most populous democracy. The Basic Law (Grundgesetz, 1949) — Germany's post-war constitution — designed the government specifically to prevent the governmental instabilities that had contributed to the Weimar Republic's collapse and the rise of Hitler. Its key innovations: the 'constructive vote of no confidence' (parliament can only remove a chancellor by simultaneously electing a successor) and the requirement that parties exceed a 5% threshold to enter parliament.\n\n"
            "The post-war Federal Republic's governance represents one of history's most successful exercises in constitutional engineering: from the rubble of Nazi defeat (1945), West Germany built the world's third-largest economy within 15 years (Wirtschaftswunder), became a founding member of the European Community (1957), and completed reunification (1990) — all under the Basic Law's stable governmental framework. Six Federal Chancellors — Adenauer, Erhard, Kiesinger, Brandt, Schmidt, Kohl — built the Federal Republic's institutions.\n\n"
            "Angela Merkel's 16-year chancellorship (2005–2021) made her the most consequential German Chancellor since Helmut Kohl — navigating the 2008 financial crisis, the Eurozone crisis, the 2015 refugee crisis, and Brexit while maintaining Germany's position as Europe's indispensable power. Germany's governmental model — coalition cabinets, federalism, constitutional court oversight — is studied globally as a model of post-authoritarian democratic consolidation."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Executive government of Europe's largest economy; the Basic Law (1949) is studied globally as the model of post-authoritarian constitutional engineering; Wirtschaftswunder (1950s–60s), reunification (1990), and Merkel's 16-year chancellorship demonstrate the Basic Law's success; Germany's governmental model is the primary reference for post-authoritarian democratic consolidation.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The catastrophic failure of the Weimar Republic — whose constitutional weaknesses (proportional representation without threshold, unlimited presidential emergency powers, destructive vote of no confidence) enabled Hitler's rise — made the Basic Law's constitutional engineers determined to design institutional safeguards against democratic breakdown",
            "The Allied occupation powers (US, UK, France) shaped the Basic Law's federalism and individual rights provisions — particularly the US emphasis on decentralisation and judicial review — embedding Western democratic values in the constitutional structure",
            "Konrad Adenauer's strategic decision to anchor West Germany firmly in the Western alliance (NATO, 1955; European Community founding, 1957) rather than seek neutral reunification provided the geopolitical framework that enabled the Wirtschaftswunder and West German stability"
        ],
        "effects": [
            "The Wirtschaftswunder (Economic Miracle, 1950s–1960s) — the fastest sustained economic recovery in modern history — transformed West Germany from a defeated, divided country into Europe's dominant economy within 15 years, demonstrating that democratic governance and market economics could coexist with rapid development",
            "German reunification (1990) — achieved through Helmut Kohl's diplomacy and the Basic Law's flexibility — absorbed 16 million East Germans and the GDR's economic infrastructure into the Federal Republic, the largest political integration in post-war European history",
            "The German constitutional model — 5% parliamentary threshold, constructive vote of no confidence, constitutional court oversight, federalism — has been adopted or adapted by more than a dozen post-communist and post-authoritarian states as a model for democratic consolidation",
            "Germany's role as Europe's indispensable power — contributing the most to the EU budget, anchoring the euro, and providing diplomatic leadership in crises from the Balkans to Ukraine — reflects the Federal Government's evolution from post-war pariah to continental leader"
        ],
        "relationships": [
            {"entity": "Basic Law of Germany (Grundgesetz, 1949)", "relationship": "CONSTITUTIONALLY_ESTABLISHED_BY", "note": "The Basic Law (1949) created the Federal Government's institutional structure — designed specifically to prevent Weimar's failures"},
            {"entity": "Konrad Adenauer", "relationship": "FIRST_AND_FOUNDATIONAL_CHANCELLOR", "note": "Adenauer (1949–1963) anchored Germany in NATO and the European Community — establishing the geopolitical framework for the Wirtschaftswunder"},
            {"entity": "Angela Merkel", "relationship": "LONGEST-SERVING_POST-WAR_CHANCELLOR", "note": "Merkel (2005–2021) — 16 years as Chancellor — navigated multiple crises and made Germany Europe's indispensable power"},
            {"entity": "German reunification (1990)", "relationship": "ADMINISTRATED", "note": "The Federal Government under Kohl negotiated and implemented German reunification (1990) — the largest political integration in post-war European history"},
            {"entity": "European Union", "relationship": "LARGEST_BUDGET_CONTRIBUTOR_AND_DIPLOMATIC_ANCHOR_OF", "note": "Germany is the EU's largest economy and budget contributor — the Federal Government is the EU's indispensable diplomatic and economic anchor"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 08 — {len(ENTITIES)} entities (Class 313: Government/Cabinet Institutions)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
