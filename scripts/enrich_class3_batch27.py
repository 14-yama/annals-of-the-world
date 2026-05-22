#!/usr/bin/env python3
"""
Batch 27 — 8 entities (Class 370): Major International Organizations
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()
FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/370-Class-370"
FILE_PREFIX = "370"


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

    ("african-union", {
        "summary": (
            "The African Union (AU, est. 2002, Addis Ababa, Ethiopia — successor to the Organisation of African Unity, 1963) is the continental organisation of 55 African member states, the largest by membership of any regional body in the world, committed to African political and economic integration, the promotion of peace and security, and the defence of human rights across the continent. The AU's founding was driven by the vision of Pan-African unity articulated by Kwame Nkrumah (Ghana), Julius Nyerere (Tanzania), and other independence-era leaders — the belief that Africa's colonial fragmentation into 54 states could only be overcome through continental federation.\n\n"
            "The AU's predecessor — the Organisation of African Unity (OAU, 1963–2002) — was the product of Africa's decolonisation wave and created the principle of African state sovereignty and non-interference that shaped post-colonial African politics. The OAU's fundamental weakness was its refusal to intervene in human rights abuses by member states — it was sardonically called the 'Dictators' Club' for its tolerance of Idi Amin, Bokassa, and Mugabe. The AU's Constitutive Act (2001) explicitly rejected the OAU's non-interference principle and permitted AU intervention in cases of genocide, war crimes, and crimes against humanity.\n\n"
            "The AU operates the African Peace and Security Architecture (APSA) — including standby forces for peacekeeping, the Peace and Security Council, and the Continental Early Warning System — and administers the African Continental Free Trade Area (AfCFTA, operational 2021), which is the world's largest free trade area by number of participating countries (54) and the most ambitious African economic integration project since the OAU."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Continental organisation of 55 African states (est. 2002); successor to OAU (1963–2002); largest regional body by membership; Constitutive Act permits AU intervention in genocide and war crimes — rejecting OAU's non-interference principle; African Peace and Security Architecture (APSA); AfCFTA (2021) — world's largest free trade area by number of countries; Pan-African unity vision of Nkrumah and Nyerere.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The failure of the OAU's non-interference principle — illustrated by its refusal to criticise Idi Amin's atrocities in Uganda, the Rwandan genocide (1994), and other mass atrocities by member states — created the political consensus for a successor organisation with the mandate to intervene in extreme cases",
            "The Libyan leader Muammar Gaddafi's financial and political advocacy for a stronger African Union — his proposal for a 'United States of Africa' and his funding of AU operations — provided both the political momentum and financial resources for the transformation of the OAU into the AU",
            "The African Continental Free Trade Area's economic logic — that Africa's 54 fragmented markets could not attract investment or achieve economies of scale without integration — drove the economic agenda that has become the AU's primary post-peacekeeping focus"
        ],
        "effects": [
            "The AU's Constitutive Act's 'right of intervention' clause — permitting AU intervention in genocide, war crimes, and crimes against humanity — established a new norm of African collective security that transcends state sovereignty, challenging the Westphalian principle that governed OAU practice",
            "The African Peace and Security Architecture (APSA) — with its standby forces deployed in Somalia, the Sahel, and the CAR — has made the AU the primary security provider for African conflicts, taking on peacekeeping roles previously borne by the UN and unilateral Western interventions",
            "The AfCFTA (African Continental Free Trade Area, 2021) — with 54 participating countries, 1.3 billion people, and $3.4 trillion in combined GDP — is the world's largest free trade area by number of countries and represents the most ambitious African economic integration project since decolonisation",
            "The AU's refusal to endorse the ICC arrest warrants against sitting African heads of state (Omar al-Bashir, Sudan) — and its repeated calls for African withdrawal from the ICC — created a fundamental confrontation between African state sovereignty and the international criminal justice system"
        ],
        "relationships": [
            {"entity": "Organisation of African Unity (OAU, 1963–2002)", "relationship": "SUCCESSOR_TO_THE", "note": "The AU (2002) succeeded the OAU (1963) — explicitly rejecting its non-interference principle and claiming the right to intervene in genocide and war crimes"},
            {"entity": "Pan-African unity movement (Nkrumah, Nyerere)", "relationship": "INSTITUTIONAL_EXPRESSION_OF", "note": "The AU embodies the Pan-African unity vision — Nkrumah's 'United States of Africa' dream institutionalised through 55 member states' continental organisation"},
            {"entity": "AfCFTA (African Continental Free Trade Area, 2021)", "relationship": "ADMINISTERS_THE", "note": "The AfCFTA — the world's largest free trade area by country count — is the AU's primary current economic integration project"},
            {"entity": "African Peace and Security Architecture (APSA)", "relationship": "OPERATES_THE", "note": "The APSA — standby forces, Peace and Security Council, Early Warning System — is the AU's continental security framework deployed in Somalia, the Sahel, and the CAR"},
            {"entity": "Rwandan genocide (1994)", "relationship": "FAILURE_TO_PREVENT_PROMPTED_REFORM_INTO", "note": "The OAU's failure to prevent or stop the Rwandan genocide (1994) was a key driver of the decision to create the AU with explicit intervention rights"}
        ],
    }),

    ("bank-for-international-settlements", {
        "summary": (
            "The Bank for International Settlements (BIS, est. 1930, Basel, Switzerland) is the world's oldest international financial institution — the 'central bank for central banks' — founded to manage Germany's World War I reparations payments and now serving as the primary forum for central bank cooperation, financial stability monitoring, and the setting of global banking regulatory standards. The BIS hosts the Basel Committee on Banking Supervision, which issues the Basel Accords (Basel I, 1988; Basel II, 2004; Basel III, 2010) — the international capital standards that govern the capital adequacy requirements of every major bank in the world.\n\n"
            "The BIS was established by the Young Plan (1930) to administer Germany's reparations payments under the Dawes Plan — a function it quickly outgrew as the reparations system collapsed with the Great Depression. Its role pivoted to providing banking services to central banks and facilitating central bank cooperation, creating the institutional infrastructure for the international monetary system. The BIS's monthly Board meetings in Basel — attended by the governors of the world's major central banks — are the primary forum for informal coordination of global monetary policy.\n\n"
            "The BIS became controversial during World War II for accepting Nazi gold — including gold melted down from the teeth of Holocaust victims — and for continuing to operate transfers between Allied and Axis central banks. A US Treasury proposal to liquidate the BIS after the war was blocked by European central bankers; the BIS survived and became the institutional backbone of the post-war Bretton Woods system and the subsequent international financial architecture."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "World's oldest international financial institution (est. 1930); 'central bank for central banks'; founded to manage WWI reparations (Young Plan); Basel Committee on Banking Supervision — issues Basel Accords (I/II/III) governing capital requirements of every major bank worldwide; hosts monthly central bank governors' meetings — primary forum for global monetary policy coordination; accepted Nazi gold during WWII including from Holocaust victims; survived US liquidation proposal (1944).",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Young Plan (1929) — revising Germany's World War I reparations schedule — required an international institution to administer the payments, creating the BIS as the administrative vehicle for the largest transfer of financial obligations in modern history",
            "The collapse of the gold standard and the Great Depression (1929–1933) — which made Germany's reparations payments impossible — eliminated the BIS's original mandate and forced it to reinvent itself as a central bank cooperation forum",
            "The Basel Committee's creation (1974) — following the collapse of Bankhaus Herstatt (Germany) and Franklin National Bank (USA) in currency settlement failures — gave the BIS the regulatory standard-setting function that is now its primary practical importance"
        ],
        "effects": [
            "The Basel Accords (I/II/III) — developed by the Basel Committee hosted at the BIS — are the international capital adequacy standards that govern the lending capacity and financial stability of every major bank in the world, directly shaping the quantity of credit available to the global economy",
            "The BIS's monthly Board meetings — bringing together the governors of the world's major central banks for informal coordination — create the only permanent forum for the discreet coordination of global monetary policy outside the formal IMF framework",
            "The BIS's acceptance of Nazi gold during World War II — including gold melted from Holocaust victims' possessions at German concentration camps — created a permanent controversy about the neutrality of international financial institutions and their responsibility for the uses of the assets they handle",
            "The BIS's survival of the US Treasury's liquidation proposal (Bretton Woods, 1944) — blocked by European central bankers who preferred it to the IMF as a more technocratic institution — established the principle that international financial institutions can outlive their original mandates by acquiring new functions"
        ],
        "relationships": [
            {"entity": "Basel Committee on Banking Supervision", "relationship": "HOSTS_THE", "note": "The BIS hosts the Basel Committee — which issues the Basel Accords governing capital requirements of every major bank in the world"},
            {"entity": "Basel Accords (I/II/III)", "relationship": "INSTITUTIONAL_HOME_FOR_DEVELOPMENT_OF_THE", "note": "The Basel I (1988), Basel II (2004), and Basel III (2010) international banking standards were developed through BIS-hosted processes"},
            {"entity": "Young Plan (1929 — WWI reparations revision)", "relationship": "FOUNDED_TO_ADMINISTER_THE", "note": "The BIS was created by the Young Plan (1929) to manage Germany's revised WWI reparations payments — the world's largest financial transfer obligation"},
            {"entity": "Nazi gold controversy (WWII)", "relationship": "CENTRE_OF_CONTROVERSY_FOR_ACCEPTING", "note": "The BIS accepted Nazi gold during WWII — including gold from Holocaust victims — creating permanent controversy about international financial institution neutrality"},
            {"entity": "Bretton Woods conference (1944)", "relationship": "SURVIVED_LIQUIDATION_PROPOSAL_AT", "note": "US Treasury proposed liquidating the BIS at Bretton Woods (1944) — blocked by European central bankers who preserved it as the IMF's institutional complement"}
        ],
    }),

    ("brics", {
        "summary": (
            "BRICS (est. as concept 2001 by Goldman Sachs economist Jim O'Neill; first formal summit 2009, Yekaterinburg, Russia; expanded to BRICS+ 2024) is the grouping of major emerging market economies — originally Brazil, Russia, India, China, and South Africa — that was created as an investment thesis (the four largest emerging markets with the fastest-growing GDPs) and became a geopolitical bloc representing the Global South's challenge to the Western-dominated international order. BRICS members collectively represent approximately 40% of the world's population, 26% of global GDP (nominal), and 31% of global GDP (PPP).\n\n"
            "The BRICS concept was invented by Goldman Sachs economist Jim O'Neill in a 2001 research paper ('Building Better Global Economic BRICs') as a description of the four largest emerging market economies — Brazil, Russia, India, China — with the fastest-growing GDPs. South Africa joined in 2010. The first formal BRICS summit (2009) transformed the investment concept into a diplomatic forum, and subsequent summits have established the BRICS as the primary institutional voice of the Global South challenging the dominance of Western-dominated institutions (IMF, World Bank, G7).\n\n"
            "The New Development Bank (NDB, est. 2014, Shanghai) — the BRICS multilateral development bank — was established as an alternative to the World Bank for infrastructure financing in developing countries. The BRICS+ expansion (2024) admitted Iran, Saudi Arabia, UAE, Egypt, Ethiopia, and Argentina (though Argentina subsequently withdrew), creating a group representing 45% of the world's population. BRICS has become the primary institutional expression of multipolar world order — the geopolitical shift away from US hegemony."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Major emerging economy grouping (concept 2001; formal summits 2009–); 40% of world population, 26% global GDP nominal; invented as Goldman Sachs investment thesis by Jim O'Neill (2001); primary institutional voice of Global South; New Development Bank (2014, Shanghai) — alternative to World Bank; BRICS+ expansion (2024) admitted Iran, Saudi Arabia, UAE, Egypt, Ethiopia; geopolitical expression of multipolar world order.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Jim O'Neill's 2001 Goldman Sachs research paper — identifying Brazil, Russia, India, and China as the four emerging markets with the highest growth trajectories — created the conceptual framework that four governments then adopted as the basis for a diplomatic bloc",
            "The 2008 global financial crisis — which severely damaged Western economic prestige and demonstrated the fragility of the US-led financial system — accelerated BRICS leaders' desire to create alternative institutions that reduced their dependence on Western-dominated organisations",
            "China's rise as the world's second-largest economy — and the failure of the G7/G8 to give China, India, and Brazil seats commensurate with their economic weight — created the institutional incentive for the BRICS to develop as an alternative forum for global economic governance"
        ],
        "effects": [
            "The New Development Bank (NDB, 2014) — the BRICS multilateral development bank with $100 billion in initial capital — is the most significant challenge to the World Bank's monopoly on multilateral infrastructure financing in the Global South since the World Bank's founding",
            "The BRICS+ expansion (2024) — admitting 6 new members including Saudi Arabia, UAE, and Iran — significantly increased the group's economic and geopolitical weight, creating a bloc that controls a substantial fraction of the world's oil production and represents the primary institutional alternative to the G7",
            "BRICS summits have established the normative vocabulary for multipolar world order — including calls for reforming the IMF's voting system, denominating commodity trade in non-dollar currencies, and creating alternatives to the SWIFT payment system — that have shaped the global governance debate",
            "India's role in BRICS — maintaining strategic autonomy between Russia/China and the Western bloc — has made the grouping increasingly complicated, as India's economic interests, democratic values, and territorial conflicts with China create fundamental tensions within the 'emerging market solidarity' narrative"
        ],
        "relationships": [
            {"entity": "Jim O'Neill (Goldman Sachs economist)", "relationship": "CONCEPTUALISED_BY", "note": "O'Neill's 2001 paper 'Building Better Global Economic BRICs' invented the concept that became the BRICS diplomatic bloc"},
            {"entity": "New Development Bank (NDB, Shanghai, 2014)", "relationship": "ESTABLISHED_THE", "note": "BRICS created the NDB (2014) — a multilateral development bank with $100bn capital as an alternative to the World Bank for Global South infrastructure"},
            {"entity": "G7/G8 (Western major economies forum)", "relationship": "PRINCIPAL_GEOPOLITICAL_COUNTERWEIGHT_TO", "note": "BRICS was explicitly conceived as an alternative power centre to the G7's Western-dominated global governance"},
            {"entity": "BRICS+ expansion (2024 — Saudi Arabia, Iran, UAE, Egypt, Ethiopia)", "relationship": "EXPANDED_TO_INCLUDE_IN", "note": "The 2024 BRICS+ expansion — adding 6 new members including major oil producers — significantly expanded the bloc's geopolitical weight"},
            {"entity": "Multipolar world order (post-US hegemony)", "relationship": "PRIMARY_INSTITUTIONAL_EXPRESSION_OF", "note": "BRICS summits have become the primary forum for articulating and advancing the narrative of multipolar world order against US-led international institutions"}
        ],
    }),

    ("international-monetary-fund", {
        "summary": (
            "The International Monetary Fund (IMF, est. 1944, Bretton Woods, New Hampshire — operational 1945, Washington DC) is the world's primary international monetary institution — founded to prevent the competitive currency devaluations and protectionist policies that contributed to the Great Depression (1929–1933), and now serving as the lender of last resort for sovereign nations facing financial crises and the primary monitor of the global economy. The IMF has 190 member countries and manages approximately $1 trillion in loan capacity.\n\n"
            "The IMF was created at the Bretton Woods Conference (July 1944) by John Maynard Keynes (UK) and Harry Dexter White (US) to provide a rules-based international monetary order with fixed exchange rates, convertibility of currencies to gold, and an international fund for countries in balance-of-payments difficulties. The Bretton Woods system of fixed exchange rates collapsed in 1971 (Nixon Shock), transforming the IMF from an exchange rate manager into a crisis lender — its primary function in the subsequent decades of the oil shocks (1970s), Latin American debt crisis (1980s), Asian financial crisis (1997–98), global financial crisis (2008–09), and COVID-19 recession (2020).\n\n"
            "The IMF's 'structural adjustment' conditions — requiring fiscal austerity, privatisation, trade liberalisation, and financial deregulation in exchange for emergency lending — became the most controversial element of international economic policy from the 1980s onwards. The 'Washington Consensus' (John Williamson, 1989) codified the IMF's policy prescriptions, which critics argued imposed economic hardship on the poorest populations of debtor countries while protecting international creditors."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's primary international monetary institution (est. 1944); 190 member countries; $1 trillion loan capacity; founded by Keynes and Harry Dexter White at Bretton Woods (1944); Bretton Woods fixed exchange rate system collapsed 1971 (Nixon Shock); IMF became crisis lender for Latin American debt (1980s), Asian financial crisis (1997), GFC (2008), COVID (2020); 'Washington Consensus' structural adjustment conditions — most controversial international economic policy instrument.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Great Depression (1929–1933) — and the competitive currency devaluations and trade barriers that countries adopted, deepening the global economic collapse — demonstrated the need for an international institution to coordinate monetary and trade policy and provide emergency financing",
            "John Maynard Keynes's vision of an 'International Clearing Union' — a supranational institution that would recycle trade surpluses from creditor to debtor nations — and Harry Dexter White's more modest US proposal created the intellectual framework for the IMF at Bretton Woods",
            "The US government's determination to design the post-war international economic order to prevent the protectionist fragmentation of the 1930s — and to ensure the dollar's central role in the new system — drove the creation of the IMF as the guardian of a rules-based international monetary order"
        ],
        "effects": [
            "The Bretton Woods system (1945–1971) — with the IMF as its institutional guardian — maintained fixed exchange rates and provided macroeconomic stability during the 'golden age of capitalism' (1945–1973), enabling the fastest period of economic growth in modern history",
            "The IMF's crisis lending programmes (Latin America 1980s, Asia 1997, global 2008, COVID 2020) — with their structural adjustment conditions requiring austerity, privatisation, and deregulation — have been the primary instrument of Western economic influence over developing country policy, enabling debt relief while imposing contested policy prescriptions",
            "The 'Washington Consensus' — the IMF/World Bank policy agenda of fiscal austerity, privatisation, and trade liberalisation — dominated international development economics from 1989 to 2008, producing both periods of growth and severe social costs, and generating a fundamental debate about the relationship between economic liberalisation and development",
            "The IMF's voting system — weighting votes by financial contribution (quota), giving the US 17.4% of votes and effective veto power — has been the primary source of developing-country complaints about the institution's legitimacy, driving the formation of alternative institutions (BRICS NDB, Asian Infrastructure Investment Bank)"
        ],
        "relationships": [
            {"entity": "Bretton Woods Conference (1944)", "relationship": "CREATED_AT_THE", "note": "The IMF was established at the Bretton Woods Conference (1944) by John Maynard Keynes (UK) and Harry Dexter White (US) to govern the post-war international monetary system"},
            {"entity": "Washington Consensus (structural adjustment)", "relationship": "PRIMARY_INSTITUTIONAL_ENFORCER_OF_THE", "note": "The IMF's structural adjustment conditions — fiscal austerity, privatisation, trade liberalisation — became the 'Washington Consensus' development policy from 1989"},
            {"entity": "Asian financial crisis (1997–98)", "relationship": "PRIMARY_CRISIS_LENDER_DURING_THE", "note": "The IMF's emergency lending during the Asian financial crisis (1997) — with controversial austerity conditions — was its most debated post-Cold War intervention"},
            {"entity": "Nixon Shock (1971 — end of Bretton Woods system)", "relationship": "ORIGINAL_MANDATE_TRANSFORMED_BY_THE", "note": "Nixon's suspension of dollar-gold convertibility (1971) ended the Bretton Woods fixed exchange rate system — transforming the IMF from exchange rate manager to crisis lender"},
            {"entity": "John Maynard Keynes (UK)", "relationship": "CO-DESIGNED_BY", "note": "Keynes's Bretton Woods proposals — modified by White's US counter-proposals — created the IMF's institutional architecture"}
        ],
    }),

    ("united-nations-peacekeeping", {
        "summary": (
            "United Nations Peacekeeping (est. 1948, first mission — United Nations Truce Supervision Organization, UNTSO, in Palestine) is the primary multilateral instrument for managing international and intra-state armed conflicts — deploying military, police, and civilian personnel to zones of conflict under UN Security Council mandates, with the consent of host governments. From 1948 to 2023, the UN has conducted 71 peacekeeping operations, deploying over 2 million military and police personnel from 125 countries. As of 2023, approximately 87,000 personnel are deployed in 12 active peacekeeping operations.\n\n"
            "UN peacekeeping was invented in 1956 by Canadian Foreign Minister Lester Pearson during the Suez Crisis — when the UK and France vetoed Security Council action after their military intervention, Pearson proposed a UN Emergency Force (UNEF) that could separate the combatants without using the Security Council's Article 42 enforcement powers. Pearson won the Nobel Peace Prize (1957) for this invention. The 'Pearson doctrine' of peacekeeping — neutral, with host consent, without enforcement — became the standard model for Cold War peacekeeping.\n\n"
            "The post-Cold War period (1990–present) produced both the greatest expansion of UN peacekeeping and its most catastrophic failures: the genocide in Rwanda (1994, under UNAMIR), where General Roméo Dallaire's requests for authority to protect civilians were denied; the Srebrenica massacre (1995, under UNPROFOR), where Dutch peacekeepers failed to prevent the killing of 8,000 Muslim men and boys; and the collapse of peacekeeping in Somalia (1993). These failures produced the Brahimi Report (2000) — the foundational reform of UN peacekeeping doctrine."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Primary multilateral conflict management instrument (est. 1948); 71 operations (1948–2023); 2 million personnel deployed from 125 countries; invented by Lester Pearson during 1956 Suez Crisis (Nobel Peace Prize 1957); catastrophic failures: Rwanda genocide (1994 — 800,000 killed), Srebrenica massacre (1995 — 8,000 killed); Brahimi Report (2000) — foundational peacekeeping reform; 87,000 personnel in 12 active operations (2023).",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Cold War's paralysis of the UN Security Council — with US and Soviet vetoes preventing collective security enforcement — created the need for a 'Chapter VI and a half' peacekeeping mechanism that could deploy neutrally without crossing into enforcement action",
            "Lester Pearson's diplomatic creativity during the Suez Crisis (1956) — proposing UNEF as a way to give UK and France a face-saving exit while separating the combatants — invented the peacekeeping model that substituted neutral interposition for Security Council enforcement",
            "The post-Cold War proliferation of intra-state conflicts (civil wars, ethnic cleansing, state collapse) in the 1990s — in Yugoslavia, Rwanda, Somalia, Sierra Leone, and Liberia — created an unprecedented demand for peacekeeping deployments that overwhelmed UN capacity"
        ],
        "effects": [
            "UN peacekeeping's failure in Rwanda (1994) — where 800,000 people were killed while UNAMIR's requests for protection authority were denied — and in Srebrenica (1995) — where 8,000 Muslim men and boys were killed within a UN 'safe zone' — demonstrated the catastrophic consequences of applying neutral peacekeeping doctrine to ongoing genocides",
            "The Responsibility to Protect (R2P) doctrine — adopted by the UN General Assembly (2005) — was the direct normative response to the Rwanda and Srebrenica failures, establishing that sovereignty does not protect states from international intervention when they commit or permit mass atrocities",
            "UN peacekeeping has been the mechanism through which decolonised and Global South states have contributed to international security — with Bangladesh, Ethiopia, India, Pakistan, and Rwanda among the largest troop contributors — transforming the UN from a Western-dominated institution into a genuinely multilateral security provider",
            "The Brahimi Report (2000) — produced after the peacekeeping failures of the 1990s — reformed peacekeeping doctrine by requiring 'robust' mandates, pre-deployment planning, and the right to use force to protect civilians, establishing the modern framework for complex peacekeeping operations"
        ],
        "relationships": [
            {"entity": "Lester Pearson (Canadian Foreign Minister, Nobel 1957)", "relationship": "INVENTED_BY", "note": "Pearson invented UN peacekeeping during the 1956 Suez Crisis — proposing UNEF as a neutral interposition force — and won the Nobel Peace Prize for this invention"},
            {"entity": "Rwandan genocide (1994 — UNAMIR failure)", "relationship": "CATASTROPHICALLY_FAILED_TO_PREVENT_THE", "note": "UNAMIR's failure to protect civilians during the Rwandan genocide (800,000 killed) was the defining failure of UN peacekeeping and drove fundamental reform"},
            {"entity": "Srebrenica massacre (1995 — UNPROFOR failure)", "relationship": "FAILED_TO_PREVENT_THE", "note": "Dutch UN peacekeepers failed to prevent the killing of 8,000 Muslim men within a UN 'safe zone' at Srebrenica — a defining peacekeeping failure"},
            {"entity": "Responsibility to Protect (R2P) doctrine (2005)", "relationship": "FAILURES_PROMPTED_ADOPTION_OF_THE", "note": "Rwanda and Srebrenica failures drove the adoption of R2P (2005) — establishing international responsibility to protect civilians from mass atrocities"},
            {"entity": "Brahimi Report (UN peacekeeping reform, 2000)", "relationship": "REFORMED_BY_THE", "note": "The Brahimi Report (2000) reformed UN peacekeeping doctrine — requiring robust mandates, pre-deployment planning, and right to use force to protect civilians"}
        ],
    }),

    ("western-european-union", {
        "summary": (
            "The Western European Union (WEU, est. 1954, Brussels — from the Brussels Treaty Organisation, 1948; dissolved 2011) was the European mutual defence organisation that preceded and complemented NATO during the Cold War, and served as the primary framework for European defence integration before its functions were absorbed by the European Union's Common Security and Defence Policy (CSDP). The WEU was established to provide a European alternative to NATO — addressing French concerns about German rearmament within a European framework and British concerns about a continental defence community without UK involvement.\n\n"
            "The WEU was created from the Brussels Treaty (1948) — the mutual defence pact of the UK, France, Belgium, the Netherlands, and Luxembourg — which was subsequently expanded to include West Germany and Italy (1954) following the failure of the European Defence Community (EDC) project. Article V of the WEU Treaty — establishing collective defence — was actually stronger than NATO's Article 5, committing members to 'all the military and other aid and assistance in their power', while NATO's Article 5 required only 'such action as it deems necessary'.\n\n"
            "The WEU's practical significance was limited during the Cold War by NATO's dominance, but it provided the institutional framework for European defence cooperation that became increasingly important after the Cold War. The WEU's operational role — conducting the Petersberg Tasks (humanitarian, rescue, peacekeeping, and crisis management operations) — was transferred to the EU in 2003, and the organisation was formally dissolved in 2011."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "European mutual defence organisation (est. 1954 from Brussels Treaty 1948; dissolved 2011); predecessor to EU's Common Security and Defence Policy; established to address French concerns about German rearmament in a European framework; WEU Article V collective defence — stronger than NATO's Article 5; operational Petersberg Tasks transferred to EU (2003); dissolved when functions absorbed into EU.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The failure of the European Defence Community (EDC) project (1954) — rejected by the French National Assembly — forced a reconfiguration of European defence integration that preserved a European framework (the WEU) while using NATO for the actual military integration, solving the German rearmament problem within a European institutional structure",
            "France's desire to maintain a distinctly European defence identity — separate from NATO's US-dominated command structure — drove the creation of a WEU with an Article V collective defence commitment that was formally independent of, though operationally dependent on, NATO",
            "The Cold War's division of Europe — and the Soviet threat that created the absolute priority of NATO's nuclear deterrence — limited the WEU's practical significance for 40 years, making it a dormant institutional framework waiting for the post-Cold War moment when European defence autonomy became politically feasible"
        ],
        "effects": [
            "The WEU's institutional framework — with its assembly, secretary general, and collective defence architecture — provided the template for the EU's Common Security and Defence Policy (CSDP) when European defence integration moved from the WEU to the EU in 1999–2011",
            "The Petersberg Tasks (1992) — defined by the WEU to include humanitarian missions, rescue operations, peacekeeping, and crisis management — became the legal basis for EU military operations after the WEU transferred its operational functions to the EU in 2003",
            "The WEU's managed dissolution (2011) — the first deliberate winding-up of a major international organisation — established the precedent that international organisations can be dissolved by member-state agreement when their functions have been absorbed by other institutions",
            "The UK's membership of the WEU (as a non-EU member of a European defence community) established the institutional precedent for British participation in European security structures that became relevant in the Brexit negotiations about future UK-EU defence cooperation"
        ],
        "relationships": [
            {"entity": "Brussels Treaty (1948)", "relationship": "GREW_FROM_THE", "note": "The WEU developed from the Brussels Treaty's mutual defence pact of the UK, France, Belgium, the Netherlands, and Luxembourg"},
            {"entity": "European Defence Community (failed project, 1954)", "relationship": "CREATED_AS_SUBSTITUTE_FOR_THE_FAILED", "note": "The WEU was created (1954) when the French National Assembly rejected the European Defence Community — providing an alternative European defence framework"},
            {"entity": "NATO (North Atlantic Treaty Organization)", "relationship": "EUROPEAN_COMPLEMENT_TO", "note": "The WEU provided a European defence identity alongside NATO — with a stronger collective defence obligation but no independent military command"},
            {"entity": "EU Common Security and Defence Policy (CSDP)", "relationship": "INSTITUTIONAL_PREDECESSOR_OF_THE", "note": "The WEU's functions — Petersberg Tasks, collective defence framework — were absorbed by the EU's CSDP in 1999–2011, making the WEU the institutional precursor of EU defence"},
            {"entity": "Petersberg Tasks (1992 — humanitarian and crisis management operations)", "relationship": "DEFINED_THE", "note": "The WEU's 1992 Petersberg Declaration defined the tasks (humanitarian, peacekeeping, crisis management) that became the basis for EU military operations"}
        ],
    }),

    ("world-health-organization", {
        "summary": (
            "The World Health Organization (WHO, est. 1948, Geneva, Switzerland) is the United Nations' specialised agency for international public health — the primary global body for setting health standards, coordinating responses to public health emergencies, and monitoring the burden of disease worldwide. The WHO's 194 member states collectively represent universal global health governance, with the WHO coordinating the eradication of smallpox (1980) — the only human disease to have been eradicated — and the global vaccination and disease surveillance programmes that have saved hundreds of millions of lives.\n\n"
            "The WHO led one of the greatest achievements in medical history: the eradication of smallpox (1967–1980) — a disease that had killed 300–500 million people in the 20th century alone, was defeated by an 11-year vaccination campaign that made smallpox the only infectious disease of humans ever to be eradicated from the natural world. The eradication was formally certified in 1980, when WHO Director-General Halfdan Mahler announced that 'the world and all its peoples have won freedom from smallpox'.\n\n"
            "The COVID-19 pandemic (2020–2022) severely damaged the WHO's reputation and exposed fundamental weaknesses in global health governance: Taiwan's early warnings about person-to-person transmission were reportedly suppressed due to China's political pressure on the WHO; the WHO's delay in declaring COVID-19 a public health emergency of international concern (PHEIC); and US President Trump's withdrawal of the US from the WHO (announced 2020, reversed by Biden 2021). The pandemic also revealed the WHO's deep dependence on voluntary contributions from member states and private donors, limiting its operational independence."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "UN specialised agency for global public health (est. 1948); 194 member states; led smallpox eradication (1967–1980) — only human disease ever eradicated, 300–500 million 20th-century deaths prevented; COVID-19 pandemic (2020) exposed WHO weaknesses: China political pressure on Taiwan's early warnings, delayed PHEIC declaration, US withdrawal; voluntary contribution funding limits independence.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The catastrophic influenza pandemic of 1918–1919 (the 'Spanish flu', 50–100 million deaths) — and the absence of any international body capable of coordinating the response — demonstrated the need for a permanent international public health institution",
            "The creation of the United Nations system (1945) — and the commitment to creating specialised agencies for international governance of health, labour, food, and education — provided the political framework for establishing the WHO as the UN's health agency",
            "The post-World War II consensus on international cooperation as the solution to shared global problems — including infectious disease, which respects no national borders — drove universal membership and the WHO's establishment as the authoritative voice of international health science"
        ],
        "effects": [
            "The eradication of smallpox (1980) — the WHO's greatest achievement — demonstrated that a globally coordinated vaccination campaign could eliminate an infectious disease from the natural world, establishing the template for subsequent eradication efforts against polio, measles, and guinea worm disease",
            "The WHO's International Health Regulations (IHR) — the binding international legal framework governing national responses to public health emergencies — are the primary mechanism through which the WHO can require national governments to report disease outbreaks and take containment measures",
            "The COVID-19 pandemic's exposure of WHO weaknesses — political influence on its independence, inadequate emergency powers, voluntary funding model — has generated the most serious reform debate in the organisation's history, potentially resulting in a new Pandemic Treaty with stronger WHO emergency authorities",
            "WHO's global disease burden statistics — the Global Burden of Disease study — provide the primary evidence base for global health policy, determining how international health funding is allocated and which diseases receive research investment, making the WHO's epidemiological function foundational to global health priorities"
        ],
        "relationships": [
            {"entity": "Smallpox eradication campaign (1967–1980)", "relationship": "LED_THE", "note": "The WHO coordinated the global vaccination campaign that eradicated smallpox (certified 1980) — the greatest achievement in the history of public health"},
            {"entity": "COVID-19 pandemic (2020–2022)", "relationship": "COORDINATED_GLOBAL_RESPONSE_TO_THE_WHILE_EXPOSED_WEAKNESSES_BY", "note": "The COVID-19 pandemic both tested and severely damaged the WHO's reputation — exposing political influence on its independence and the weakness of its emergency authorities"},
            {"entity": "International Health Regulations (IHR)", "relationship": "ADMINISTERS_THE_BINDING_FRAMEWORK_OF_THE", "note": "The IHR — the primary binding international legal framework for global health emergencies — requires WHO members to report outbreaks and take containment measures"},
            {"entity": "United Nations system (specialised agencies)", "relationship": "HEALTH_SPECIALISED_AGENCY_OF_THE", "note": "WHO is the UN's health specialised agency — the equivalent in public health of what the IMF is in finance and the ILO is in labour"},
            {"entity": "1918 influenza pandemic ('Spanish flu')", "relationship": "CATASTROPHIC_PRECEDENT_THAT_DEMONSTRATED_NEED_FOR", "note": "The Spanish flu's 50–100 million deaths — with no international coordinating body — demonstrated the need for the WHO's creation"}
        ],
    }),

    ("world-trade-organization", {
        "summary": (
            "The World Trade Organization (WTO, est. 1995, Geneva, Switzerland — successor to GATT, 1947) is the primary international body governing global trade rules — providing the multilateral legal framework for $25 trillion in annual merchandise and services trade, adjudicating trade disputes between member governments through its Dispute Settlement Body (DSB), and hosting multilateral trade negotiations. The WTO's 164 member countries represent 98% of world trade.\n\n"
            "The WTO succeeded the General Agreement on Tariffs and Trade (GATT, 1947) — the post-World War II trade liberalisation framework — following the Uruguay Round of trade negotiations (1986–1994), which created the WTO as a permanent institution with legally binding dispute settlement, expanded coverage to services (GATS), and intellectual property (TRIPS). The WTO's dispute settlement mechanism — which allows member states to challenge other members' trade policies and win binding rulings — is the most effective multilateral enforcement mechanism in international law.\n\n"
            "The WTO's Doha Development Round (launched 2001) — intended to reduce agricultural subsidies and manufacturing tariffs in a way that would benefit developing countries — failed to reach agreement and remains uncompleted, representing the most significant failure of multilateral trade negotiation since the GATT era. The rise of bilateral and regional free trade agreements (EU, NAFTA, TPP, RCEP) as alternatives to multilateral WTO deals, and the US under Trump (2017–2021) blocking WTO Appellate Body appointments (effectively disabling dispute settlement), have raised fundamental questions about the WTO's continued relevance."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Primary multilateral trade governance body (est. 1995); 164 members representing 98% of world trade; $25 trillion annual trade governed; successor to GATT (1947); Uruguay Round (1986–1994) created WTO with binding dispute settlement; GATS (services) and TRIPS (intellectual property) — expanded trade law scope; Doha Round (2001) uncompleted failure; US blocked Appellate Body (2017–2021) — crisis of multilateral trade governance.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The GATT's institutional inadequacy — it was a treaty, not an organisation, with no permanent secretariat empowered to enforce rulings — created the demand for the WTO as a permanent institution with binding legal authority",
            "The Uruguay Round's (1986–1994) recognition that 20th-century trade increasingly involved services, intellectual property, and investment — not just goods — drove the WTO's expanded mandate beyond GATT's goods-only framework",
            "The post-Cold War consensus on globalisation as the path to development — and the demonstration that export-led growth had lifted hundreds of millions out of poverty in East Asia — created the political momentum for a stronger multilateral trade institution"
        ],
        "effects": [
            "The WTO's Dispute Settlement Body — issuing binding rulings on trade disputes with the authority to authorise retaliatory measures — is the most effective enforcement mechanism in international law, enabling small countries to win trade rulings against the US, EU, and China",
            "China's accession to the WTO (2001) — the most significant expansion of the multilateral trading system since its founding — integrated 1.3 billion people into global trade rules, accelerating China's export-led growth and its rise to become the world's largest goods trader",
            "The TRIPS Agreement (WTO intellectual property rules) — requiring WTO members to provide 20-year patent protection — became the most controversial element of WTO governance, as it extended patent protection to pharmaceutical drugs and enabled drug companies to restrict generic medicine access in developing countries",
            "The WTO's crisis (2017–2021) — created by the US blocking Appellate Body appointments — disabled the dispute settlement system and raised fundamental questions about the US commitment to multilateral trade rules, accelerating the shift toward bilateral and regional trade agreements"
        ],
        "relationships": [
            {"entity": "GATT (General Agreement on Tariffs and Trade, 1947)", "relationship": "SUCCESSOR_TO_THE", "note": "The WTO (1995) succeeded GATT (1947) — replacing a treaty with a permanent institution and adding binding dispute settlement, services (GATS), and intellectual property (TRIPS)"},
            {"entity": "Uruguay Round (1986–1994)", "relationship": "CREATED_BY_THE", "note": "The Uruguay Round of multilateral trade negotiations created the WTO — expanding trade law from goods to services and intellectual property"},
            {"entity": "China WTO accession (2001)", "relationship": "TRANSFORMED_BY_ADMISSION_OF_CHINA_INTO", "note": "China's WTO accession (2001) was the most significant integration into the multilateral trading system — accelerating China's export-led growth and rise as world's largest goods trader"},
            {"entity": "TRIPS Agreement (pharmaceutical patents)", "relationship": "ADMINISTERS_THE_MOST_CONTESTED_ELEMENT_OF_THROUGH", "note": "TRIPS's extension of patent protection to pharmaceuticals became the most contested WTO provision — restricting generic medicine access in developing countries"},
            {"entity": "Doha Development Round (2001 — uncompleted)", "relationship": "FAILED_TO_COMPLETE_THE", "note": "The Doha Round — intended to reduce agricultural subsidies and benefit developing countries — is the WTO's most significant failure, remaining uncompleted since 2001"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 27 — {len(ENTITIES)} entities (Class 370: Major International Organizations)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
