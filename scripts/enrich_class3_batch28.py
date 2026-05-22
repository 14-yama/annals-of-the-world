#!/usr/bin/env python3
"""
Batch 28 — 8 entities (Class 371 + 372): International Bodies & Economic Communities
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()

BASE = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities"


def enrich_entity(class_prefix, slug, data):
    folder = os.path.join(BASE, f"{class_prefix}-Class-{class_prefix}")
    fname = os.path.join(folder, f"{class_prefix}{slug}.json")
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


# (class_prefix, slug, data)
ENTITIES = [

    ("371", "united-nations", {
        "summary": (
            "The United Nations (UN, est. 1945, San Francisco — Charter signed 26 June 1945, entered into force 24 October 1945) is the primary international organisation for maintaining international peace and security, developing friendly relations among nations, and promoting social progress, human rights, and economic development. With 193 member states — representing virtually every sovereign nation on earth — the UN is the closest existing approximation to a world government. Its principal organs are the General Assembly, the Security Council, the Secretariat, the International Court of Justice, the Economic and Social Council, and the Trusteeship Council.\n\n"
            "The UN was founded after World War II to replace the failed League of Nations (1919–1946) and prevent a third world war. Its founding document — the Charter of the United Nations — enshrines the sovereign equality of member states, the prohibition on the use of force except in self-defence or with Security Council authorisation, and the promotion of human rights and international law. The five permanent members of the Security Council (P5 — US, UK, France, Russia, China) each hold veto power over Security Council resolutions — a reflection of the power politics of 1945 that has both enabled and frustrated the UN's security function.\n\n"
            "The UN system — encompassing 15 specialised agencies (WHO, UNESCO, FAO, IMF, World Bank, etc.) and numerous programmes — is the primary vehicle for multilateral cooperation across every domain of international public policy, from climate change (UNFCCC, Paris Agreement) to nuclear non-proliferation (IAEA) to refugee protection (UNHCR). The Universal Declaration of Human Rights (1948) — adopted by the UN General Assembly — is the most widely endorsed normative document in history."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Primary international organisation (est. 1945); 193 member states; Charter prohibits use of force; P5 Security Council veto; replaced failed League of Nations; Universal Declaration of Human Rights (1948); 15 specialised agencies including WHO, UNESCO, IMF, World Bank; Paris Climate Agreement under UNFCCC; closest existing approximation to world government.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The catastrophic failure of the League of Nations — unable to prevent Japanese aggression in Manchuria (1931), Italian aggression in Ethiopia (1935), or German aggression in Europe (1938–1939) — demonstrated the need for a stronger international institution with the US as a member and with genuine enforcement powers",
            "World War II's 70–85 million deaths — and the Holocaust's systematic extermination of 6 million Jews — created the political consensus among the Allied powers for an international organisation capable of preventing future wars and protecting human rights",
            "Franklin Roosevelt's vision of the 'Four Policemen' (US, UK, USSR, China) maintaining post-war order — and his success in bringing Churchill and Stalin into the UN founding framework — provided the political architecture that made the UN viable despite the emerging Cold War"
        ],
        "effects": [
            "The UN's Universal Declaration of Human Rights (1948) — adopted unanimously by the General Assembly — created the normative foundation for international human rights law, generating 9 core human rights treaties, the International Criminal Court, and the concept of Responsibility to Protect (R2P)",
            "The UN's specialised agency system — WHO, UNESCO, FAO, UNHCR, UNICEF, UNDP — is the primary multilateral infrastructure for global public goods, coordinating responses to pandemics, famines, refugee crises, and development challenges that no single state could address alone",
            "The UN's decolonisation norm — enshrined in General Assembly Resolution 1514 (1960) — accelerated the end of European colonial empires and expanded UN membership from 51 founding states (1945) to 193 (2011), transforming the organisation from a primarily Western institution into a genuinely global one",
            "The P5 veto's paralysis of the Security Council during the Cold War — and its resurgence in the Ukraine war (Russia's veto blocking action) — has driven repeated reform proposals (including the 'Uniting for Peace' resolution) but the P5 have successfully blocked all structural changes to their privileged position"
        ],
        "relationships": [
            {"entity": "League of Nations (1919–1946)", "relationship": "SUCCESSOR_TO_THE_FAILED", "note": "The UN was designed to correct the failures of the League of Nations — most critically by including the US and by giving the P5 enforcement authority through the Security Council"},
            {"entity": "Universal Declaration of Human Rights (1948)", "relationship": "ADOPTED_THE", "note": "The UDHR — adopted unanimously by the UN General Assembly in 1948 — is the normative foundation of international human rights law"},
            {"entity": "UN Security Council (P5 veto)", "relationship": "GOVERNED_THROUGH_THE_STRUCTURE_OF", "note": "The P5 permanent members (US, UK, France, Russia, China) hold veto power — reflecting 1945 power politics and both enabling and blocking UN action"},
            {"entity": "Paris Agreement (UNFCCC, 2015)", "relationship": "INSTITUTIONAL_FRAMEWORK_FOR_THE", "note": "The Paris Agreement — the global climate framework — was negotiated under the UN Framework Convention on Climate Change"},
            {"entity": "UNESCO, WHO, UNHCR, UNICEF (specialised agencies)", "relationship": "OVERSEES_15_SPECIALISED_AGENCIES_INCLUDING", "note": "The UN's 15 specialised agencies coordinate global action on health, education, culture, refugee protection, and development"}
        ],
    }),

    ("371", "european-economic-area", {
        "summary": (
            "The European Economic Area (EEA, est. 1994) is the agreement that extends the EU's Single Market to three non-EU European states — Norway, Iceland, and Liechtenstein — creating the largest integrated economic area in the world. EEA members participate in the EU's four fundamental freedoms (free movement of goods, services, capital, and people) without being EU members, giving them access to the Single Market at the cost of accepting EU regulations in which they have no formal vote. The EEA encompasses approximately 450 million people and $16 trillion in GDP.\n\n"
            "The EEA was created as the pathway for European Free Trade Association (EFTA) members that wanted access to the EU Single Market without full EU membership. Norway — which twice rejected EU membership in referenda (1972, 1994) — was the primary driver of the EEA model, as Norway's oil and fishing wealth created both the desire for Single Market access and the political resistance to full membership. The EEA Agreement gives Norway access to the EU's banking, financial services, and product markets — but excludes EU agricultural and fisheries policies.\n\n"
            "The EEA became highly relevant to the Brexit debate: the 'Norway model' was extensively discussed as a post-Brexit option for the UK, as it would have maintained Single Market access while allowing the UK to leave formal EU institutions. The UK ultimately rejected the Norway model because it would require accepting EU freedom of movement and EU regulations without a UK vote — precisely the concerns that drove the Brexit vote."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Extends EU Single Market to Norway, Iceland, Liechtenstein (est. 1994); largest integrated economic area (~450 million people, $16 trillion GDP); 'four freedoms' without EU membership; Norway twice rejected EU membership (1972, 1994); 'Norway model' extensively discussed during Brexit; excludes EU agricultural and fisheries policies; regulations accepted without formal vote.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Norway's double rejection of EU membership in referenda (1972, 1994) — driven by fisheries protection concerns, agricultural policy differences, and sovereignty anxieties — created the demand for an intermediate arrangement that gave Norway Single Market access without full membership",
            "The EU's Single Market programme (1986–1993) — eliminating internal trade barriers and creating the world's largest integrated market — made access to the Single Market economically essential for EFTA members who traded primarily with EU countries",
            "The EFTA countries' desire to avoid the political commitments of EU membership (common foreign policy, monetary union, EU governance obligations) while gaining economic access drove the negotiation of the EEA as a 'market access without political union' framework"
        ],
        "effects": [
            "Norway's EEA membership — giving it access to the EU's financial services, product standards, and labour markets — has made the Norwegian economy highly integrated with the EU while preserving Norwegian control over fisheries, agriculture, and monetary policy",
            "The 'Norwegian model' of EEA membership became the primary template for discussions of 'soft Brexit' — the UK remaining in the Single Market without EU membership — and its ultimate rejection by the UK illustrated the political limits of the EEA model (accepting regulations without voting on them)",
            "The EEA's exclusion of fisheries and agriculture from the four freedoms — giving Norway control over its fishing zone — became the primary model for subsequent discussions of how EU integration could be calibrated to protect national strategic interests",
            "Liechtenstein's EEA membership — despite sharing borders only with Switzerland (a non-EEA state) — created a unique situation where a micro-state of 38,000 people participates in the world's largest economic area, demonstrating the flexibility of the EEA model"
        ],
        "relationships": [
            {"entity": "EU Single Market (four freedoms)", "relationship": "EXTENDS_THE_FOUR_FREEDOMS_OF_THE", "note": "The EEA gives Norway, Iceland, and Liechtenstein access to the EU's Single Market — free movement of goods, services, capital, and people — without EU membership"},
            {"entity": "Norway (EU membership rejections 1972, 1994)", "relationship": "PRIMARY_BENEFICIARY_OF_AS_ALTERNATIVE_TO_EU_FOR", "note": "Norway twice rejected EU membership but uses the EEA to access the Single Market — illustrating the EEA's role as the 'market without political union' model"},
            {"entity": "Brexit (UK leaving EU, 2020)", "relationship": "NORWEGIAN_MODEL_DISCUSSED_AS_ALTERNATIVE_DURING", "note": "The 'Norway model' was extensively discussed as a post-Brexit option before the UK chose a harder Brexit that sacrificed Single Market access"},
            {"entity": "EFTA (European Free Trade Association)", "relationship": "CREATED_FOR_MEMBERS_OF", "note": "The EEA was designed for EFTA members (Norway, Iceland, Liechtenstein) wanting Single Market access without full EU membership"},
            {"entity": "EU fisheries and agricultural policies", "relationship": "EXPLICITLY_EXCLUDES_THE", "note": "The EEA excludes EU agricultural and fisheries policies — giving Norway control over its fishing zone, the primary reason for its EU membership rejections"}
        ],
    }),

    ("371", "organisation-for-european-economic-co-operation", {
        "summary": (
            "The Organisation for European Economic Co-operation (OEEC, est. 1948, Paris — reorganised as OECD 1961) was the international body created to administer the Marshall Plan (European Recovery Programme, 1948–1952) — the US programme providing $13 billion ($160 billion in 2023 dollars) to reconstruct Western Europe after World War II — and to coordinate the economic recovery and trade liberalisation of Western European countries. The OEEC became the model for post-war multilateral economic cooperation and the institutional ancestor of the OECD.\n\n"
            "The OEEC was created at the insistence of US Secretary of State George Marshall and Under-Secretary William Clayton — who required that the European recipients of Marshall Plan aid coordinate their recovery plans collectively rather than receiving bilateral US transfers. This requirement for European collective planning forced the political cooperation that eventually produced the European Coal and Steel Community (1951) and the European Economic Community (1957), making the OEEC an inadvertent catalyst for European integration.\n\n"
            "The OEEC's transformation into the OECD (Organisation for Economic Co-operation and Development, 1961) — expanding membership to include the US, Canada, and eventually Japan, South Korea, and other non-European developed economies — created the primary club of developed market democracies. The OECD's Programme for International Student Assessment (PISA) has become the most influential measure of educational achievement worldwide, and its global tax transparency initiatives (BEPS, Common Reporting Standard) are reshaping international tax governance."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Created to administer Marshall Plan (est. 1948); $13 billion Marshall Plan ($160 billion 2023) coordinated through OEEC; US requirement for collective European planning inadvertently catalysed European integration (ECSC 1951, EEC 1957); reorganised as OECD (1961) — club of developed market democracies; PISA — most influential global education ranking; BEPS and Common Reporting Standard reshaping international tax governance.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "George Marshall's 'Marshall Plan' speech (June 1947) — offering US economic aid contingent on European collective planning — created the political framework that required European countries to cooperate in distributing aid rather than receiving bilateral transfers",
            "The Cold War's division of Europe — and the US commitment to preventing Western Europe's economic collapse from driving it toward communism — provided the geopolitical rationale for the unprecedented $13 billion aid programme",
            "The European countries' recognition that post-war reconstruction required trade liberalisation and currency convertibility — not just financial transfers — drove the OEEC to become a forum for trade policy coordination that laid the groundwork for the European common market"
        ],
        "effects": [
            "The Marshall Plan's requirement for collective European planning — administered through the OEEC — forced the political habits of European economic cooperation that produced the European Coal and Steel Community (1951), the European Economic Community (1957), and ultimately the European Union, making the OEEC the inadvertent catalyst for European integration",
            "The OECD's development as the primary club of developed market democracies — and its peer review model of policy evaluation — created the concept of 'developed country' as a distinct category of states sharing economic, institutional, and democratic characteristics",
            "The OECD's PISA (Programme for International Student Assessment) — launched 2000, testing 15-year-olds in reading, mathematics, and science across 80 countries — has become the world's most influential measure of educational achievement, driving major educational reform debates in underperforming countries",
            "The OECD's Base Erosion and Profit Shifting (BEPS) initiative — addressing multinational tax avoidance — produced the Global Minimum Corporate Tax agreement (15% minimum, 2021), the most significant reform of international corporate taxation in 100 years"
        ],
        "relationships": [
            {"entity": "Marshall Plan (European Recovery Programme, 1948–1952)", "relationship": "ADMINISTRATIVE_BODY_FOR_THE", "note": "The OEEC was created to coordinate collective European receipt of Marshall Plan aid — $13 billion for post-war reconstruction"},
            {"entity": "George Marshall and Dean Acheson (architects of Marshall Plan)", "relationship": "CREATED_AT_INSISTENCE_OF", "note": "Marshall and Clayton insisted that European Marshall Plan recipients cooperate collectively through the OEEC rather than receiving bilateral US transfers"},
            {"entity": "OECD (Organisation for Economic Co-operation and Development, 1961)", "relationship": "REORGANISED_INTO_THE", "note": "The OEEC became the OECD (1961) by expanding to include the US, Canada, and other non-European developed economies — creating the club of market democracies"},
            {"entity": "European Coal and Steel Community (ECSC, 1951)", "relationship": "INADVERTENT_CATALYST_FOR_EUROPEAN_INTEGRATION_LEADING_TO", "note": "The OEEC's requirement for collective European economic planning created the habits of cooperation that produced the ECSC and EEC"},
            {"entity": "Global Minimum Corporate Tax (2021, 15%)", "relationship": "DELIVERED_THROUGH_OECD_BEPS_PROCESS_OF", "note": "The OECD's BEPS initiative produced the 15% global minimum corporate tax (2021) — the most significant international tax reform in a century"}
        ],
    }),

    ("371", "arab-maghreb-union", {
        "summary": (
            "The Arab Maghreb Union (AMU, est. 1989, Marrakech) is the regional economic integration organisation of the five North African Arab states — Morocco, Algeria, Tunisia, Libya, and Mauritania — established with the ambition of creating a North African common market comparable to the European Community. The AMU is one of the most failed international organisations in the world: since its founding in 1989, it has held only three heads of state summits (1990, 1991, 1994) — the last more than 30 years ago — and has achieved almost none of its economic integration goals due to the intractable Algeria-Morocco dispute over the Western Sahara.\n\n"
            "The AMU was founded during a brief window of regional détente — when Algeria and Morocco temporarily improved relations — with the ambition of creating a North African common market that would have enabled the region's 100 million people (now 200 million) to participate as a unified bloc in the emerging post-Cold War globalisation. The Western Sahara dispute — Morocco's annexation of the territory in 1975, resisted by the Polisario Front backed by Algeria — immediately froze AMU operations, and the Algerian-Moroccan border has been closed since 1994.\n\n"
            "The AMU's failure represents one of the most costly examples of regional integration failure in the developing world: economists estimate that the lack of North African economic integration costs the region $5–10 billion annually in foregone trade and investment, making the Sahara countries among the least economically integrated regions in the world."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "North African regional body (est. 1989); 5 member states (Morocco, Algeria, Tunisia, Libya, Mauritania); only 3 heads of state summits in 35 years (1990, 1991, 1994); frozen by Algeria-Morocco dispute over Western Sahara; Algerian-Moroccan border closed since 1994; economists estimate $5–10 billion annual cost of failed integration; most failed regional organisation in the world.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The brief détente between Algeria and Morocco in the late 1980s — and the regional desire to create a North African counterpart to the European Community — created the political window for the AMU's founding at Marrakech (1989)",
            "The Cold War's end and the demonstration of European integration's economic benefits — creating the pressure for developing regions to form their own economic blocs — drove the Maghreb states to establish the AMU despite their unresolved political disputes",
            "Morocco's annexation of Western Sahara (1975) — and Algeria's support for the Polisario Front's independence claim — created the fundamental political conflict that made sustained AMU cooperation impossible once the founding summit's goodwill dissipated"
        ],
        "effects": [
            "The AMU's failure — demonstrating that political disputes (Western Sahara) can completely paralyse a regional organisation even when economic integration would benefit all members — has become a case study in the priority of political over economic logic in regional integration",
            "The absence of North African economic integration — economists estimate $5–10 billion in annual foregone trade — has made the Maghreb one of the least economically integrated regions in the world, despite geographic proximity, shared language and culture, and complementary economies",
            "The Algerian-Moroccan border closure (1994–present) — the longest sustained border closure between neighbouring states in the developing world — has prevented the creation of a North African economic hub that could have attracted European investment and reduced the migration pressures that drive North African emigration to Europe",
            "The AMU's paralysis has made the EU the primary external economic partner of each Maghreb state individually — through bilateral association agreements — rather than collective regional integration, perpetuating hub-and-spoke dependence on Europe rather than South-South regional integration"
        ],
        "relationships": [
            {"entity": "Western Sahara dispute (Morocco vs. Polisario Front/Algeria)", "relationship": "PARALYSED_BY_THE", "note": "The AMU's failure to function is primarily caused by the Algeria-Morocco dispute over Western Sahara — making it the defining example of how political disputes prevent economic integration"},
            {"entity": "Algeria-Morocco (border closed 1994)", "relationship": "FAILED_DUE_TO_CONFLICT_BETWEEN_ITS_TWO_LARGEST_MEMBERS", "note": "The Algeria-Morocco border — closed since 1994 — has made any AMU economic integration impossible for 30 years"},
            {"entity": "European Union (bilateral association agreements)", "relationship": "REPLACED_BY_BILATERAL_EU_AGREEMENTS_FOLLOWING_FAILURE_OF", "note": "Each Maghreb state's separate EU association agreement has substituted for AMU integration — perpetuating hub-and-spoke European dependence"},
            {"entity": "Marrakech (1989 founding summit)", "relationship": "FOUNDED_AT", "note": "The AMU was established at the Marrakech summit (1989) — the only founding summit that produced substantive institutional commitments"},
            {"entity": "North African economic integration (unrealised)", "relationship": "INSTITUTIONAL_VEHICLE_FOR_UNREALISED", "note": "The AMU was designed to create a North African common market — its failure has cost the region an estimated $5–10 billion annually in foregone trade"}
        ],
    }),

    ("371", "covax", {
        "summary": (
            "COVAX (COVID-19 Vaccines Global Access, est. 2020, Geneva — co-led by CEPI, Gavi, and WHO) is the multilateral vaccine procurement and distribution mechanism created during the COVID-19 pandemic to ensure equitable global access to COVID-19 vaccines, based on the principle that every country — regardless of wealth — should have access to vaccines before lower-risk groups in wealthier countries. COVAX aimed to deliver 2 billion vaccine doses to 92 low- and middle-income countries (LMICs) by the end of 2021.\n\n"
            "COVAX was the most ambitious multilateral public health procurement initiative in history, mobilising $10.4 billion in donor pledges and negotiating advance purchase agreements with multiple vaccine manufacturers. At its peak ambition, COVAX represented a radical departure from the historical pattern of pandemic vaccine access — in which wealthy countries contracted vaccines first and developing countries waited years. However, COVAX missed its 2021 delivery targets severely: it aimed to deliver 2 billion doses by end-2021 but delivered only 900 million, due to export restrictions by India (after a devastating Delta wave), US and European 'vaccine hoarding', and logistical challenges.\n\n"
            "COVAX's partial failure — delivering too few vaccines too late to achieve herd immunity in LMICs before the Omicron variant emerged — is a case study in the structural inequalities of global health governance: wealthy countries prioritised domestic booster campaigns over COVAX deliveries, India's Serum Institute export ban eliminated COVAX's primary supplier, and the US, UK, and EU all delayed releasing contracted doses to COVAX until their domestic populations were vaccinated."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "COVID-19 vaccine equity mechanism (est. 2020); most ambitious multilateral vaccine procurement in history; $10.4 billion donor pledges; 2 billion dose target for 92 LMICs by end-2021; delivered only 900 million doses — 55% of target; India export ban (Serum Institute), Western 'vaccine hoarding' delayed deliveries; first systematic attempt at pandemic vaccine equity; structural inequality of global health governance exposed.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The COVID-19 pandemic's demonstration that emerging infectious diseases are inherently global threats — requiring global solutions — created the political consensus for a multilateral vaccine procurement mechanism that transcended national vaccine nationalism",
            "The historical pattern of pandemic vaccine inequity — H1N1 (2009) vaccines reached developing countries only after the pandemic ended — created the normative basis for designing COVAX as an explicit equity mechanism committed to parallel access rather than sequential delivery",
            "CEPI's (Coalition for Epidemic Preparedness Innovations) pre-existing relationships with vaccine manufacturers — and Gavi's established procurement mechanisms for childhood vaccines in LMICs — provided the institutional infrastructure on which COVAX was rapidly constructed in 2020"
        ],
        "effects": [
            "COVAX's 900 million dose delivery — despite falling far short of its target — represented the largest multilateral vaccine procurement in history and established the principle of global vaccine equity as a recognised norm of international public health governance",
            "COVAX's partial failure — and the analysis showing that early equitable vaccination would have prevented new variants (including Delta and Omicron) that ultimately reinfected wealthy countries — provided the empirical evidence for pandemic preparedness reforms arguing that vaccine equity is in wealthy countries' self-interest",
            "The COVAX experience drove the negotiation of the WHO's Pandemic Treaty (ongoing) — which includes provisions for mandatory vaccine sharing, technology transfer, and advance purchase commitments that attempt to institutionalise the equity principles COVAX sought but failed to fully achieve",
            "India's export ban on Serum Institute doses (April 2021) — eliminating COVAX's primary supply source during India's devastating Delta wave — demonstrated that even LMICs with vaccine manufacturing capacity will prioritise domestic needs over international commitments during severe domestic outbreaks"
        ],
        "relationships": [
            {"entity": "COVID-19 pandemic (2020–2022)", "relationship": "CREATED_IN_RESPONSE_TO_THE", "note": "COVAX was established (2020) as the multilateral mechanism to ensure equitable global access to COVID-19 vaccines during the pandemic"},
            {"entity": "WHO (World Health Organization)", "relationship": "CO-LED_BY_ALONGSIDE_CEPI_AND_GAVI", "note": "COVAX is co-led by WHO, CEPI, and Gavi — combining the WHO's normative authority with CEPI's R&D expertise and Gavi's LMIC procurement experience"},
            {"entity": "Serum Institute of India (primary COVAX supplier)", "relationship": "PRIMARY_SUPPLY_SOURCE_DISRUPTED_BY_EXPORT_BAN_FROM", "note": "India's ban on Serum Institute vaccine exports (April 2021) eliminated COVAX's primary supplier during India's Delta wave — cutting 50% of planned 2021 deliveries"},
            {"entity": "WHO Pandemic Treaty (ongoing negotiations)", "relationship": "LESSONS_OF_FAILURE_DRIVE_EQUITY_PROVISIONS_IN_THE", "note": "COVAX's partial failure has driven WHO Pandemic Treaty provisions for mandatory vaccine sharing and technology transfer"},
            {"entity": "Global health equity norm (vaccine access)", "relationship": "ESTABLISHED_AS_RECOGNISED_NORM_OF", "note": "Despite partial failure, COVAX established global vaccine equity as a recognised norm of international public health governance for the first time"}
        ],
    }),

    ("372", "european-coal-and-steel-community", {
        "summary": (
            "The European Coal and Steel Community (ECSC, est. 1951 — Treaty of Paris; dissolved 2002) was the first supranational European institution — the original nucleus from which the European Union grew. Created to pool the French and German coal and steel industries (the materials of war) under joint supranational authority, the ECSC was the Schuman Plan's response to the question of how to make another Franco-German war materially impossible: if both nations' steel production was under common authority, neither could secretly rearm for war against the other.\n\n"
            "The ECSC was proposed by French Foreign Minister Robert Schuman (9 May 1950 — 'Europe Day') and designed by the economist Jean Monnet — who conceived of the 'Monnet method' of European integration: beginning with a small, functional, and economically beneficial project that creates its own logic for further integration. The ECSC's six founding members (France, West Germany, Italy, Belgium, the Netherlands, Luxembourg) became the founding six of the EEC and the EU — demonstrating that the Schuman Declaration's functional approach to European integration would prove durable.\n\n"
            "The ECSC's High Authority — the first genuine supranational governing body, with authority over the coal and steel sectors that superseded national sovereignty — created the institutional precedent for the European Commission, the EU's executive body. The ECSC dissolved in 2002 (its 50-year treaty having expired), with its functions absorbed by the European Community."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "First supranational European institution (est. 1951); original nucleus of the EU; Robert Schuman Plan (9 May 1950 — 'Europe Day'); Jean Monnet's design — 'Monnet method' of functional integration; pooled French-German coal and steel to make war materially impossible; ECSC High Authority — first genuine supranational body, precedent for EU Commission; six founding members became EU founding six; dissolved 2002 (50-year treaty expired).",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The question of German rearmament after World War II — and France's determination that Germany must not secretly rearm for future war — created the political necessity for Schuman's proposal to place both nations' steel production under joint authority, making preparation for mutual war materially impossible",
            "Jean Monnet's 'functionalist' theory of integration — that supranational cooperation should begin with specific economic sectors rather than grand constitutional projects — provided the design principle for a practical, limited first step that could succeed where the broader European Defence Community would fail",
            "The US pressure on Western Europe to integrate — driven by the Marshall Plan requirement for collective planning and Cold War concerns about Western European fragmentation before Soviet power — provided the external incentive that made French acceptance of German steel production politically feasible"
        ],
        "effects": [
            "The ECSC's High Authority — the first supranational institution with genuine authority over member states' economic sectors — created the institutional precedent for the European Commission, demonstrating that national governments could delegate sovereignty to a supranational body without collapsing",
            "The ECSC's success — creating a genuine common market for coal and steel that reduced prices and increased output — validated the functionalist approach to integration and created the political confidence for the broader EEC common market (Treaty of Rome, 1957)",
            "The Schuman Declaration (9 May 1950) — proposing the ECSC as the first step toward 'a European federation indispensable to the preservation of peace' — is celebrated as 'Europe Day', the founding moment of the European project and the normative origin of the EU's peace mission",
            "The ECSC's pooling of war-materials production — coal and steel — under joint Franco-German authority completed the psychological reconciliation between France and Germany that made the subsequent political union possible: by sharing the infrastructure of warfare, France and Germany were acknowledging mutual trust"
        ],
        "relationships": [
            {"entity": "Schuman Declaration (9 May 1950 — 'Europe Day')", "relationship": "CREATED_BY_THE", "note": "Robert Schuman's declaration (9 May 1950) proposed the ECSC — the founding moment of European integration, celebrated as 'Europe Day'"},
            {"entity": "Jean Monnet (designer of ECSC)", "relationship": "DESIGNED_BY", "note": "Monnet's 'functionalist' approach — starting with a specific economic sector — designed the ECSC as the first step toward European federation"},
            {"entity": "European Economic Community (EEC, Treaty of Rome, 1957)", "relationship": "INSTITUTIONAL_NUCLEUS_THAT_EVOLVED_INTO_THE", "note": "The ECSC's six founding members and institutions became the founding six and institutional template for the EEC (1957) and EU"},
            {"entity": "European Commission (EU executive body)", "relationship": "HIGH_AUTHORITY_IS_INSTITUTIONAL_PRECEDENT_OF_THE", "note": "The ECSC's High Authority — the first genuine supranational executive — was the direct institutional precedent for the European Commission"},
            {"entity": "Franco-German reconciliation (post-WWII)", "relationship": "MATERIAL_FOUNDATION_FOR", "note": "By pooling coal and steel production, the ECSC made Franco-German war materially impossible and created the economic foundation for political reconciliation"}
        ],
    }),

    ("372", "benelux", {
        "summary": (
            "Benelux (est. 1944 — Benelux Customs Union Treaty, London; operational 1948; reformed as Benelux Union 1960, modernised 2010, Brussels) is the economic and political union of Belgium, the Netherlands, and Luxembourg — the world's first successful regional economic integration, pre-dating the ECSC and EEC and serving as the prototype for the broader European integration project. The word 'Benelux' (coined 1944) is the first portmanteau name for a regional organisation — a naming convention subsequently adopted for ASEAN, MERCOSUR, BRICS, and dozens of other regional bodies.\n\n"
            "The Benelux Customs Union was negotiated while Belgium, the Netherlands, and Luxembourg were still under Nazi occupation — their governments-in-exile in London signed the 1944 treaty. This remarkable act of forward planning — designing a post-war economic union while under occupation — reflected the three countries' recognition that their small economies required collective integration to compete with larger neighbours. The Benelux countries were among the six founding members of the ECSC (1951) and the EEC (1957), making Benelux the inner nucleus of European integration.\n\n"
            "The Benelux Union provides a laboratory for studying European integration: Belgium and the Netherlands have maintained separate national identities while achieving near-complete economic integration, demonstrating that sovereignty and integration are compatible. The Benelux Union's reformed 2010 treaty focused on transboundary cooperation — police cooperation, infrastructure, environmental policy — that the EU had not yet achieved, making Benelux a laboratory for deeper-than-EU integration."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "World's first successful regional economic integration (est. 1944); prototype for European integration; negotiated by governments-in-exile in London while under Nazi occupation (1944); coined the 'portmanteau name' convention for regional organisations; ECSC and EEC founding members; laboratory for studying European integration; 2010 reform achieving deeper-than-EU transboundary cooperation.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The three countries' governments-in-exile in London recognised during the Nazi occupation (1940–1945) that their small, open economies were too vulnerable without integration — and that post-war reconstruction would require collective trade liberalisation and economic cooperation",
            "The three countries' geographic compactness and economic complementarity — Belgium's industrial production, Netherlands' trade and ports, Luxembourg's steel — created natural economic integration that formal Customs Union rules could formalise and protect",
            "The post-World War I experience of Belgian and Dutch isolation — and the failure of the interwar international economic order to prevent the Great Depression's trade barriers — convinced the governments-in-exile that integration was the only path to post-war prosperity"
        ],
        "effects": [
            "The Benelux Customs Union (1948) — eliminating tariffs between the three countries and creating common external tariffs — was the world's first successful regional economic integration, demonstrating that the theoretical promise of customs union theory could be achieved in practice",
            "The Benelux model — and the three countries' subsequent role as founding members of the ECSC and EEC — made them the primary advocates for deeper European integration and the political mediators between France and Germany in the early EU, giving small states an outsized influence on European integration",
            "The portmanteau name 'Benelux' — combining the first syllables of Belgium, Netherlands, Luxembourg — was the first geographic portmanteau name for a regional organisation, a naming convention subsequently adopted worldwide (ASEAN, MERCOSUR, BRICS, ALBA, etc.)",
            "The Benelux Union's 2010 modernised treaty — focusing on police cooperation, border management, and environmental policy that exceeded EU standards — established Benelux as a laboratory for deeper integration than the EU had achieved, pioneering the 'coalition of the willing' model within EU frameworks"
        ],
        "relationships": [
            {"entity": "European Coal and Steel Community (ECSC, 1951)", "relationship": "FOUNDING_MEMBERS_PROVIDING_INNER_NUCLEUS_OF", "note": "Belgium, Netherlands, and Luxembourg were among the six founding members of the ECSC — their Benelux integration serving as the inner nucleus of European integration"},
            {"entity": "Benelux Customs Union Treaty (London, 1944)", "relationship": "ESTABLISHED_BY_THE", "note": "The 1944 London treaty — signed by governments-in-exile while under Nazi occupation — created the world's first modern regional economic integration agreement"},
            {"entity": "European integration (prototype)", "relationship": "SERVED_AS_PROTOTYPE_FOR", "note": "The Benelux Customs Union (1944) pre-dated and prototyped the ECSC (1951) and EEC (1957) — making it the founding experiment of the European integration project"},
            {"entity": "Portmanteau geographical names for regional organisations", "relationship": "COINED_THE_CONVENTION_OF", "note": "The word 'Benelux' (1944) was the first portmanteau name for a regional body — a naming convention subsequently adopted for ASEAN, MERCOSUR, BRICS, and dozens of others"},
            {"entity": "Benelux Union (2010 reform)", "relationship": "MODERNISED_AS_THE", "note": "The 2010 reformed Benelux Union — focusing on police cooperation, infrastructure, and environment — achieved deeper-than-EU integration, making it a laboratory for European integration's future"}
        ],
    }),

    ("372", "latin-american-free-trade-association", {
        "summary": (
            "The Latin American Free Trade Association (LAFTA, est. 1960 — Treaty of Montevideo; reorganised as LAIA/ALADI 1980, Montevideo) was the first major Latin American trade integration organisation — bringing together seven (later eleven) South American and Mexican economies in a framework intended to create a Latin American common market. LAFTA was the Latin American parallel to the European Economic Community (both established in the late 1950s-early 1960s), sharing the same theoretical framework (economic integration theory) but producing very different outcomes: while the EEC succeeded, LAFTA largely failed to achieve genuine trade liberalisation.\n\n"
            "LAFTA was created during the 'development economics' era — when ECLA (UN Economic Commission for Latin America), led by Raúl Prebisch, was advocating import substitution industrialisation (ISI) and intra-regional trade as the alternatives to Latin America's dependence on commodity exports to wealthy countries. LAFTA was intended to create a large enough market for Latin American manufactures to achieve economies of scale — making the region's infant industries competitive without needing to penetrate wealthy-country markets.\n\n"
            "LAFTA's failure — due to the incompatibility of national industrialisation strategies, currency inconvertibility, and political instability in member states — led to its reorganisation as LAIA (Latin American Integration Association/ALADI, 1980), a more flexible framework of bilateral agreements within a multilateral umbrella. LAIA/ALADI remains the primary Latin American trade integration framework, though MERCOSUR, the Andean Community, and CAFTA have become more practically significant."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "First major Latin American trade integration body (est. 1960); inspired by EEC model; Raúl Prebisch and ECLA theoretical basis (import substitution industrialisation); created to give Latin American manufactures a large enough market for economies of scale; failed to achieve genuine trade liberalisation; reorganised as LAIA/ALADI (1980); MERCOSUR, Andean Community emerged as more successful alternatives.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Raúl Prebisch's 'centre-periphery' theory (ECLA, 1950) — arguing that commodity-exporting periphery countries face structural terms-of-trade decline relative to industrial centre countries — provided the theoretical basis for import substitution industrialisation and Latin American economic integration as an alternative development strategy",
            "The simultaneous formation of the European Economic Community (1957) — which threatened to divert trade from Latin America toward European preferential markets — created the defensive logic for Latin American trade bloc formation",
            "The United Nations Economic Commission for Latin America (ECLA/CEPAL)'s advocacy for import substitution industrialisation — which required a larger market than any single Latin American country could provide — drove the formation of LAFTA as the vehicle for regional market creation"
        ],
        "effects": [
            "LAFTA's failure — due to the incompatibility of national ISI strategies, currency inconvertibility, and the political instability of member states — demonstrated that regional trade integration requires deeper political commitment and institutional capacity than a trade treaty alone can create",
            "LAFTA's reorganisation as LAIA/ALADI (1980) created the more flexible framework of bilateral agreements within a multilateral umbrella that became the basis for MERCOSUR (1991), the Andean Community (originally Andean Pact, 1969), and subsequent Latin American integration initiatives",
            "The ECLA/CEPAL school's development economics framework — Prebisch's centre-periphery theory, import substitution industrialisation, and regional integration — became the primary alternative to neoclassical development economics, influencing development policy across Latin America and the Global South",
            "LAFTA's experience — demonstrating the difficulty of trade integration when member states have conflicting national industrialisation strategies — provided the negative lesson that shaped MERCOSUR's more politically committed approach and the emphasis on political will as a prerequisite for regional integration"
        ],
        "relationships": [
            {"entity": "Raúl Prebisch and ECLA/CEPAL (centre-periphery theory)", "relationship": "THEORETICALLY_GROUNDED_IN_WORK_OF", "note": "LAFTA was grounded in Prebisch's ECLA economic framework — import substitution industrialisation requiring a larger regional market than individual countries could provide"},
            {"entity": "European Economic Community (EEC, 1957)", "relationship": "INSPIRED_BY_AND_DEFENSIVE_RESPONSE_TO_THE", "note": "LAFTA was inspired by the EEC model and created partly as a defensive response to the EEC's preferential trade arrangements threatening Latin American exports"},
            {"entity": "LAIA/ALADI (Latin American Integration Association, 1980)", "relationship": "REORGANISED_INTO_THE", "note": "LAFTA's failure led to its reorganisation as LAIA/ALADI (1980) — a more flexible framework of bilateral agreements within a multilateral umbrella"},
            {"entity": "MERCOSUR (Southern Common Market, 1991)", "relationship": "INSTITUTIONAL_ANCESTOR_OF", "note": "MERCOSUR (1991) — the most successful Latin American trade integration — grew out of the LAIA framework that replaced LAFTA"},
            {"entity": "Import substitution industrialisation (ISI)", "relationship": "INSTITUTIONAL_VEHICLE_FOR_REGIONAL_MARKET_CREATION_FOR", "note": "LAFTA was intended to create the large regional market that ISI's infant industries needed to achieve economies of scale — linking trade integration to development strategy"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 28 — {len(ENTITIES)} entities (Class 371 + 372: International Bodies & Economic Communities)")
    for cls, slug, data in ENTITIES:
        print(f"\n→ {cls}/{slug}")
        enrich_entity(cls, slug, data)
    print("\n✓ Done")
