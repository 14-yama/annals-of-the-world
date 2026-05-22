#!/usr/bin/env python3
"""
Batch 11 — 8 entities (Class 331): Central Banks & Major Banks
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/331-Class-331"
FILE_PREFIX = "331"
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

    ("bank-of-england", {
        "summary": (
            "The Bank of England (est. 1694) is the central bank of the United Kingdom and one of the oldest central banks in the world — founded to finance the Nine Years' War against Louis XIV's France, it pioneered the institutional model of a government-backed central bank that became the template for central banking globally. Its governor and monetary policy committee now control interest rates for the world's fifth-largest economy, managing inflation, financial stability, and the pound sterling.\n\n"
            "The Bank of England's evolution from royal war-finance instrument to modern inflation-targeting central bank traces the full arc of modern monetary history: it held the world's largest gold reserve and managed the Gold Standard's international enforcement from the 1820s to 1931; it was nationalised by Clement Attlee's Labour government in 1946; and it was granted operational independence from the Treasury (setting its own interest rates) by Chancellor Gordon Brown in 1997 — in what was regarded as the most significant monetary policy reform in 50 years.\n\n"
            "The Bank of England's response to the 2008 financial crisis — cutting rates to 0.5% (then a 314-year low), launching £375 billion in quantitative easing, and rescuing Northern Rock, HBOS, and Royal Bank of Scotland — demonstrated that modern central banking requires not only monetary policy authority but the capacity to act as lender of last resort to the financial system at crisis scale."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's second-oldest central bank (est. 1694); pioneered the central banking model adopted globally; managed the Gold Standard's international enforcement (1820s–1931); granted independence 1997; its 2008 crisis response (QE, bank rescues) shaped modern central banking practice.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "William III's need to finance the Nine Years' War against Louis XIV — and the English government's inability to borrow at affordable rates — led Scottish banker William Paterson to propose a bank that would lend £1.2 million to the Crown in exchange for a royal charter, creating the Bank of England's founding compromise between public purpose and private profit",
            "The 'financial revolution' of late 17th-century England — development of government bonds, a secondary securities market, and institutional investors — created the financial ecosystem in which the Bank of England could function as the hub of state borrowing",
            "England's increasing commercial and imperial power in the 18th century created demand for a stable monetary system and reliable credit — which the Bank of England provided, enabling Britain's Industrial Revolution by lowering the cost of capital"
        ],
        "effects": [
            "The Bank of England's model — a private bank with a government charter, acting as banker to the state and lender of last resort — became the template for central banking globally, directly inspiring the creation of the Federal Reserve (1913), the Bundesbank, and virtually every modern central bank",
            "The Bank's management of the Gold Standard (1819–1931) — establishing sterling as the world's reserve currency and London as the global financial centre — shaped the international monetary system for over a century",
            "Gordon Brown's 1997 grant of Bank of England independence — considered the most important UK monetary policy reform since 1945 — created the institutional model of independent inflation-targeting central banks that the IMF recommended globally",
            "The Bank's 2008 crisis response — £375 billion QE, near-zero interest rates, bank bailouts — pioneered unconventional monetary policy tools that central banks worldwide subsequently adopted"
        ],
        "relationships": [
            {"entity": "Nine Years' War (1688–1697)", "relationship": "FOUNDED_TO_FINANCE", "note": "The Bank of England was founded (1694) to provide £1.2 million to finance William III's war against Louis XIV"},
            {"entity": "Gold Standard", "relationship": "INTERNATIONAL_ENFORCER_OF", "note": "The Bank of England managed the Gold Standard (1819–1931) — the international monetary system that made sterling the world's reserve currency"},
            {"entity": "Federal Reserve System", "relationship": "INSTITUTIONAL_MODEL_FOR", "note": "The Federal Reserve (1913) was directly modelled on the Bank of England — the template for central banking globally"},
            {"entity": "2008 financial crisis (UK)", "relationship": "MANAGED_THROUGH_QE_AND_BANK_RESCUES", "note": "The Bank's £375B QE programme and bank rescues pioneered unconventional monetary policy tools adopted globally"},
            {"entity": "Gordon Brown", "relationship": "GRANTED_INDEPENDENCE_BY", "note": "Chancellor Gordon Brown's 1997 decision to grant the Bank operational independence is the most significant UK monetary reform since 1945"}
        ],
    }),

    ("federal-reserve-system", {
        "summary": (
            "The Federal Reserve System ('the Fed') is the central bank of the United States — the world's most powerful monetary authority — established by the Federal Reserve Act (1913) following the Panic of 1907 to provide the US with a central banking system and a more flexible currency. The Fed's mandate combines price stability (inflation targeting) and maximum employment — a 'dual mandate' unique among major central banks. Its decisions on interest rates, money supply, and financial regulation affect every economy in the world, since the US dollar is the global reserve currency.\n\n"
            "The Fed's most consequential moments trace the arc of 20th-century economic history: its contractionary monetary policy during the Great Depression (1929–1933) — raising rates and contracting the money supply — is now understood as the central cause of the Depression's catastrophic depth (Milton Friedman's 'Great Contraction'). Paul Volcker's 'Volcker shock' (1979–1982) — raising the federal funds rate to 20% to break the inflationary spiral — caused the worst US recession since the Depression but permanently established the Fed's inflation-fighting credibility.\n\n"
            "The Fed's response to the 2008 financial crisis — cutting rates to near-zero, launching $4 trillion in quantitative easing, and creating emergency facilities to backstop the entire financial system — was the most aggressive central bank intervention in history. Ben Bernanke, the architect of the response, won the Nobel Prize in Economics (2022) partly for his academic work on the Depression, which directly informed his crisis response."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's most powerful monetary authority; dual mandate (price stability + maximum employment); Fed's Great Depression policy failures deepened the Depression; Volcker shock (1979–82) broke the inflationary spiral; 2008 crisis response ($4T QE) was the most aggressive central bank intervention in history.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Panic of 1907 — a severe banking crisis in which J.P. Morgan personally organised the financial system's bailout in the absence of any central authority — demonstrated that the US lacked the institutional capacity to manage financial panics, creating the political impetus for the Federal Reserve Act (1913)",
            "The US's fragmented banking system — with 25,000+ independent banks and no central lending facility — created chronic instability that the Fed was designed to overcome by providing a 'lender of last resort' for the banking system",
            "Woodrow Wilson's political compromise — distributing the Federal Reserve into 12 regional banks rather than a single central institution — addressed populist suspicion of Wall Street centralisation while creating the hybrid public-private structure that still characterises the Fed"
        ],
        "effects": [
            "The Fed's contractionary policy during the Great Depression (1929–1933) — allowing the money supply to contract by one-third — is now considered the central cause of the Depression's severity, directly informing the central banking principle that monetary policy must be expansionary during financial crises",
            "The Volcker shock (1979–1982) — federal funds rate raised to 20%, causing the worst US recession since the Depression — permanently broke the inflationary psychology of the 1970s and established the Fed's inflation-fighting credibility that has anchored US monetary policy since",
            "The Fed's 2008 crisis response — near-zero rates, $4 trillion QE, emergency facilities backing commercial paper, money markets, and mortgage securities — prevented the financial system's collapse and pioneered unconventional monetary tools that central banks globally subsequently adopted",
            "The dollar's status as the world's reserve currency — maintained partly by confidence in the Fed's institutional credibility — gives the Fed extraordinary global influence: its interest rate decisions affect borrowing costs, capital flows, and exchange rates for every emerging market economy"
        ],
        "relationships": [
            {"entity": "Panic of 1907", "relationship": "ESTABLISHED_IN_RESPONSE_TO", "note": "The Fed was established (1913) in direct response to the Panic of 1907 — which demonstrated the US banking system's vulnerability without a central lender of last resort"},
            {"entity": "Great Depression (1929–1939)", "relationship": "POLICY_FAILURES_DEEPENED", "note": "The Fed's contractionary policy (1929–33) deepened the Depression — the foundational lesson in central banking that monetary policy must be expansionary in financial crises"},
            {"entity": "Paul Volcker", "relationship": "VOLCKER_SHOCK_ENGINEERED_BY", "note": "Volcker's 20% interest rate (1979–82) broke the inflationary spiral — establishing the Fed's inflation-fighting credibility at the cost of the worst US recession since the Depression"},
            {"entity": "2008 global financial crisis", "relationship": "SYSTEMIC_RESPONSE_LED_BY", "note": "Bernanke's Fed response (near-zero rates, $4T QE, emergency facilities) prevented financial system collapse — the most aggressive central bank intervention in history"},
            {"entity": "US dollar reserve currency status", "relationship": "INSTITUTIONAL_CREDIBILITY_UNDERPINS", "note": "The dollar's global reserve currency status depends on confidence in the Fed's institutional credibility — making the Fed's decisions globally consequential"}
        ],
    }),

    ("world-bank", {
        "summary": (
            "The World Bank Group is an international financial institution — headquartered in Washington, DC — that provides loans and grants to governments of low and middle-income countries for capital projects and development programmes. Founded at the Bretton Woods Conference (July 1944) alongside the International Monetary Fund, the World Bank was originally designed to finance the reconstruction of Europe following WWII. Its mandate evolved into international development financing — becoming the world's largest development finance institution, with $100+ billion in annual commitments.\n\n"
            "The World Bank's intellectual and policy influence has been as significant as its financial role: it has been the world's most influential development policy institution, promoting (and revising) development theories across eight decades — from post-war reconstruction (1944–1960) to infrastructure investment (1960s) to poverty reduction (McNamara era, 1968–1981) to structural adjustment programmes (1980s–1990s, the 'Washington Consensus') to governance and social development (1990s–present). Its structural adjustment conditions (market liberalisation, privatisation, austerity) applied to African and Latin American borrowers in the 1980s are the most contested development policy interventions in modern economic history.\n\n"
            "The World Bank's operations have generated sustained criticism: its infrastructure projects (dams, highways) have displaced millions of people; its structural adjustment conditions imposed severe social costs on poor populations; and its governance structure — giving US and European shareholders effective veto power — has been criticised as reflecting colonial power dynamics rather than development effectiveness."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's largest development finance institution (est. Bretton Woods 1944); $100B+ annual commitments; the Washington Consensus structural adjustment programmes (1980s–90s) are the most contested development policy interventions in economic history; McNamara's poverty-focused era (1968–81) redefined development economics.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Bretton Woods Conference (1944) — convened by 44 Allied nations to design the post-war international economic order — created the World Bank and IMF as the institutional pillars of a new international monetary and development system",
            "The post-WWII development consensus — that poor countries needed capital (which they could not access at reasonable rates in private markets) to invest in the infrastructure and industry required for economic development — provided the intellectual justification for the World Bank's development lending mandate",
            "US strategic interests in the Cold War — using development lending to prevent poor countries from turning to Soviet-bloc alternatives — provided the political motivation for US support of robust World Bank financing in the 1950s–1960s"
        ],
        "effects": [
            "The Washington Consensus structural adjustment programmes (1980s–1990s) — requiring market liberalisation, privatisation, and fiscal austerity as conditions for loans — are the most contested development policy intervention in modern economic history, credited with fiscal stabilisation in some countries and devastating social impacts in others",
            "Robert McNamara's World Bank presidency (1968–1981) — shifting focus from infrastructure to poverty reduction, rural development, and primary education — redefined development economics and the World Bank's mission, influencing development policy globally",
            "The World Bank's annual World Development Report — providing the definitive data and analytical framework for development economics — is the most influential annual publication in development economics, shaping how governments and donors think about poverty, growth, and development",
            "The World Bank's infrastructure lending — roads, dams, power plants — enabled economic development in dozens of countries, but also displaced millions of people (particularly dam construction) and contributed to environmental degradation, making its environmental and social safeguard policies a major arena of civil society advocacy"
        ],
        "relationships": [
            {"entity": "Bretton Woods Conference (1944)", "relationship": "ESTABLISHED_BY", "note": "The World Bank was established at Bretton Woods (1944) alongside the IMF — as the institutional pillar of the post-war international development system"},
            {"entity": "International Monetary Fund", "relationship": "FOUNDED_ALONGSIDE_AS_BRETTON_WOODS_TWIN", "note": "The World Bank and IMF were created together at Bretton Woods — designed as complementary institutions (development finance vs monetary stability)"},
            {"entity": "Washington Consensus", "relationship": "IMPLEMENTED_THROUGH_STRUCTURAL_ADJUSTMENT", "note": "The World Bank implemented Washington Consensus policies (market liberalisation, privatisation, austerity) through structural adjustment loans — the most contested development policy intervention in economic history"},
            {"entity": "Robert McNamara", "relationship": "MOST_TRANSFORMATIVE_PRESIDENT", "note": "McNamara (1968–1981) reoriented the World Bank from infrastructure to poverty reduction — redefining development economics globally"},
            {"entity": "Global development finance", "relationship": "LARGEST_INSTITUTION_IN", "note": "The World Bank is the world's largest development finance institution — $100B+ annual commitments shaping development investment globally"}
        ],
    }),

    ("international-monetary-fund", {
        "summary": (
            "The International Monetary Fund (IMF) is an international organisation — headquartered in Washington, DC — that promotes international monetary cooperation, exchange rate stability, and balanced growth of international trade, and provides financial assistance to member countries experiencing balance-of-payments crises. Founded at the Bretton Woods Conference (1944) alongside the World Bank, the IMF has 190 member countries and approximately $1 trillion in available financial resources.\n\n"
            "The IMF's conditional lending — providing emergency financing to countries in crisis on condition that they implement economic reforms (fiscal consolidation, monetary tightening, structural adjustment) — has made it the most powerful institution in international financial governance, and the most controversial. IMF programmes in Mexico (1994), Asia (1997–1998), Russia (1998), Argentina (2001–2002), and Greece (2010–2018) shaped the economic and political trajectories of billions of people — while generating intense debate about whether IMF conditionality achieves its stated objectives or imposes unnecessary austerity on vulnerable populations.\n\n"
            "The IMF's intellectual evolution reflects the arc of post-war economic thought: from enforcing the Bretton Woods fixed exchange rate system (1944–1971) to managing the floating exchange rate era to promoting capital account liberalisation (1990s) to acknowledging (in a landmark 2016 IMF paper) that 'neoliberalism' may have been 'oversold' — a remarkable institutional self-critique that reflected the profession's post-2008 reassessment."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "International monetary institution (est. Bretton Woods 1944); 190 member countries; $1T available resources; IMF conditionality shaped the economic trajectories of Mexico, Asia, Russia, Argentina, Greece; 2016 IMF paper acknowledging 'neoliberalism oversold' was a landmark institutional self-critique.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The interwar monetary chaos — competitive devaluations, trade protectionism, and the Gold Standard's deflationary pressures during the Depression — demonstrated the catastrophic costs of uncoordinated national monetary policies, motivating the Bretton Woods architects to design an institution for international monetary coordination",
            "John Maynard Keynes's 'bancor' proposal — for an international clearing union with a new supranational currency — and Harry Dexter White's US Treasury plan competed at Bretton Woods; the IMF reflected White's compromise, giving the US a dominant institutional position while providing the multilateral framework Keynes sought",
            "The post-WWII US hegemony — the dollar's dominance as the global reserve currency (backed by the Bretton Woods dollar-gold link) — required an international institution to manage the stability of the dollar-centred monetary system"
        ],
        "effects": [
            "The IMF's management of the 1997 Asian financial crisis — requiring contractionary fiscal and monetary policies in Thailand, Indonesia, and South Korea in exchange for bailout funding — is the most studied case of IMF conditionality, credited by its critics with deepening the crisis and by its defenders with restoring confidence",
            "The IMF's Special Drawing Rights (SDR) — an international reserve asset created in 1969 — provided supplementary liquidity to the global monetary system and established the precedent for international monetary assets independent of any single currency",
            "The 2016 IMF staff paper ('Neoliberalism: Oversold?') — acknowledging that capital account liberalisation and fiscal consolidation may have increased inequality and vulnerability rather than promoting growth — represented a landmark institutional self-critique of the economic orthodoxy the IMF had promoted for three decades",
            "IMF surveillance — its annual country consultations (Article IV) and global economic assessments (World Economic Outlook) — is the most authoritative periodic assessment of the world economy, influencing government policies and market expectations globally"
        ],
        "relationships": [
            {"entity": "Bretton Woods Conference (1944)", "relationship": "ESTABLISHED_BY", "note": "The IMF was established at Bretton Woods (1944) to manage the post-war fixed exchange rate system and provide emergency balance-of-payments financing"},
            {"entity": "1997 Asian financial crisis", "relationship": "CONDITIONALITY_INTERVENTIONS_SHAPED", "note": "IMF conditionality in Thailand, Indonesia, and South Korea during the 1997 crisis is the most debated case of whether IMF intervention deepened or resolved financial crises"},
            {"entity": "Bretton Woods system (fixed exchange rates)", "relationship": "MANAGED_UNTIL_COLLAPSE_IN_1971", "note": "The IMF managed the Bretton Woods fixed exchange rate system from 1944 until Nixon's closing of the gold window (1971) ended the system"},
            {"entity": "John Maynard Keynes", "relationship": "BRETTON_WOODS_DESIGN_SHAPED_BY_PROPOSAL_OF", "note": "Keynes's 'bancor' proposal shaped the IMF's design — though the US Treasury's White plan dominated, Keynes's multilateral framework was preserved"},
            {"entity": "World Bank", "relationship": "FOUNDED_ALONGSIDE_AS_BRETTON_WOODS_TWIN", "note": "The IMF and World Bank were created together at Bretton Woods — complementary institutions for monetary stability and development finance"}
        ],
    }),

    ("european-central-bank", {
        "summary": (
            "The European Central Bank (ECB) is the central bank for the Eurozone — the 20 EU member states that use the euro — and one of the world's most important monetary institutions. Established in Frankfurt on 1 June 1998 and assuming monetary policy responsibility when the euro was launched (1 January 1999), the ECB is unique among major central banks: it manages monetary policy for a currency union covering 20 sovereign states with divergent economies, without a corresponding political or fiscal union.\n\n"
            "The ECB's primary mandate — price stability (inflation below but close to 2%) — is narrower than the Federal Reserve's dual mandate (price stability + maximum employment). This institutional focus on inflation was shaped by Germany's hyperinflation trauma (1923) and the Bundesbank's disciplinary legacy. ECB President Mario Draghi's 2012 commitment — 'whatever it takes' to preserve the euro — is the single most powerful statement in central banking history, ending the Eurozone sovereign debt crisis purely through a credible commitment without requiring a single bond purchase.\n\n"
            "The ECB's unconventional monetary policies (negative interest rates, asset purchases, targeted long-term refinancing operations) since 2015 represent the most ambitious monetary policy experiment in history — managing divergent economic conditions across 20 economies simultaneously. Christine Lagarde's ECB (from 2019) has navigated COVID-19 emergency asset purchases (€1.85 trillion PEPP) and the fastest interest rate increase cycle in the ECB's history (2022–2023) in response to post-pandemic inflation."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Central bank for 20 Eurozone nations (est. 1998); manages monetary policy for a currency union without fiscal union — the most ambitious monetary experiment in history; Draghi's 'whatever it takes' (2012) ended the Eurozone crisis without firing a shot; manages the world's second-largest reserve currency.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Maastricht Treaty (1992) — committing EU member states to a path toward monetary union — created the institutional framework for the ECB and the euro, reflecting the European project's conviction that economic integration required monetary unification",
            "Germany's demand for an independent, inflation-focused central bank — shaped by the hyperinflation trauma of 1923 — determined the ECB's institutional design: its primary mandate of price stability and its independence from political instruction mirror the Bundesbank model",
            "The European Exchange Rate Mechanism's (ERM) crises (1992–1993) — when speculative currency attacks forced sterling and lira devaluations — demonstrated that fixed exchange rates without monetary union were vulnerable to market attack, strengthening the case for full monetary union"
        ],
        "effects": [
            "Mario Draghi's 'whatever it takes' speech (July 2012) — committing the ECB to unlimited government bond purchases if necessary to preserve the euro — ended the Eurozone sovereign debt crisis and demonstrated that credible central bank commitment can substitute for actual monetary intervention",
            "The ECB's negative interest rate policy (2014–2022) — the first major central bank to adopt negative deposit rates — was the most radical peacetime monetary policy experiment in European history, testing the limits of conventional monetary theory",
            "The ECB's management of the COVID-19 Pandemic Emergency Purchase Programme (PEPP, €1.85 trillion) demonstrated the ECB's capacity for flexible large-scale intervention despite its constitutional constraints",
            "The ECB's fundamental challenge — managing monetary policy for economies as divergent as Germany and Greece within a single interest rate — is the defining test case for the theory that optimal currency areas require fiscal union, not just monetary union"
        ],
        "relationships": [
            {"entity": "Euro (common currency)", "relationship": "MONETARY_AUTHORITY_FOR", "note": "The ECB manages monetary policy for the euro — the world's second-largest reserve currency — covering 20 EU member states"},
            {"entity": "Mario Draghi", "relationship": "'WHATEVER_IT_TAKES'_COMMITMENT_MADE_BY", "note": "Draghi's 2012 'whatever it takes' commitment ended the Eurozone crisis — the single most powerful statement in central banking history"},
            {"entity": "Eurozone sovereign debt crisis (2010–2015)", "relationship": "MANAGED_THROUGH_CREDIBLE_COMMITMENT", "note": "The ECB ended the Eurozone crisis through Draghi's 'whatever it takes' commitment — monetary credibility as a substitute for actual intervention"},
            {"entity": "Deutsche Bundesbank", "relationship": "INSTITUTIONAL_MODEL_BASED_ON", "note": "The ECB's mandate and independence were modelled on the Bundesbank — reflecting Germany's hyperinflation trauma and inflation-fighting credibility"},
            {"entity": "Maastricht Treaty (1992)", "relationship": "CREATED_BY", "note": "The Maastricht Treaty (1992) established the legal framework for the ECB and the euro — committing EU member states to monetary union"}
        ],
    }),

    ("bank-of-china", {
        "summary": (
            "Bank of China (中国银行) is one of China's four major state-owned commercial banks — and the oldest and most internationally oriented of China's major banks, founded in 1912 following the fall of the Qing Dynasty to manage China's foreign exchange and international banking. Now one of the world's largest banks by assets (top 5 globally), the Bank of China is the primary institution for Chinese foreign exchange operations, international trade financing, and cross-border RMB settlement — making it central to China's strategy of internationalising the renminbi.\n\n"
            "The Bank of China's history spans the full arc of Chinese modern history: from financing Sun Yat-sen's Republic (1912) through the Nationalist government, surviving (and being nationalised under) the Communist revolution (1949), serving as the PRC's sole authorised foreign exchange bank during the Mao era, and transforming into a globally competitive commercial bank through China's post-1978 economic opening and its partial IPO (2006). With $3.5+ trillion in total assets, it is now systematically important to the global financial system.\n\n"
            "The Bank of China's Belt and Road Initiative (BRI) financing — providing loans for infrastructure projects across 70+ countries — makes it one of the primary instruments of Chinese economic diplomacy, funding ports (Hambantota), railways (Kenya Standard Gauge Railway), and power plants globally. Its participation in BRI financing has brought scrutiny from Western governments concerned about Chinese 'debt-trap diplomacy'."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "China's oldest major bank (est. 1912); top-5 globally by assets ($3.5T+); primary instrument for RMB internationalisation; Belt and Road financing across 70+ countries; most internationally oriented of China's four major state banks; central to China's global financial influence strategy.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The fall of the Qing Dynasty (1912) and the establishment of the Republic of China created the need for a modern banking institution to manage government finances, foreign exchange, and international trade — filling the institutional void left by the collapse of the imperial financial system",
            "China's early 20th-century need for foreign exchange management — to service its foreign debt, manage trade finance, and conduct diplomatic payments — required a specialised institution with international banking capabilities that the Bank of China was designed to provide",
            "China's post-1978 economic opening — creating the need for trade finance, foreign currency management, and international banking services as Chinese enterprises entered global markets — transformed the Bank of China from a restricted foreign exchange institution into a fully commercial global bank"
        ],
        "effects": [
            "The Bank of China's role as the primary institution for RMB internationalisation — establishing RMB clearing centres globally, facilitating cross-border RMB settlements — makes it central to China's strategy of reducing global dependence on the US dollar",
            "Bank of China's Belt and Road financing (70+ countries) — funding infrastructure projects across Asia, Africa, and Europe — is one of the primary instruments of Chinese economic diplomacy and a major factor in developing countries' debt structures",
            "The Bank of China's partial IPO (Hong Kong, 2006) — raising $11.2 billion at the time one of the largest IPOs in history — marked China's integration of its banking sector into global capital markets and established Bank of China as an internationally recognised financial institution",
            "The Bank of China's London branch (est. 1929) and international network make it the primary institution connecting Chinese and Western financial markets — playing a critical role in Chinese-Western trade and investment flows"
        ],
        "relationships": [
            {"entity": "Republic of China (Sun Yat-sen)", "relationship": "FOUNDED_TO_SERVE", "note": "Bank of China was founded in 1912 to manage the finances of the new Republic of China — following the fall of the Qing Dynasty"},
            {"entity": "Belt and Road Initiative", "relationship": "PRIMARY_FINANCING_BANK_FOR", "note": "Bank of China's BRI financing across 70+ countries makes it a primary instrument of Chinese economic diplomacy"},
            {"entity": "RMB internationalisation", "relationship": "PRIMARY_INSTITUTIONAL_VEHICLE_FOR", "note": "Bank of China leads China's strategy of internationalising the RMB — establishing clearing centres and facilitating cross-border RMB settlements globally"},
            {"entity": "People's Republic of China", "relationship": "NATIONALISED_BY_AND_STATE-OWNED_BY", "note": "Bank of China was nationalised under the PRC (1949) — it remains state-owned as one of China's four major commercial banks"},
            {"entity": "Global banking system", "relationship": "TOP-5_INSTITUTION_IN", "note": "With $3.5T+ in assets, Bank of China is a globally systemically important financial institution"}
        ],
    }),

    ("jpmorgan-chase", {
        "summary": (
            "JPMorgan Chase & Co. is the largest US bank by assets and one of the world's most systemically important financial institutions — the product of a century of mergers beginning with J.P. Morgan's original bank (founded 1871) and culminating in the 2000 merger of Chase Manhattan and J.P. Morgan & Co., followed by acquisitions of Bank One (2004), Bear Stearns (2008), and Washington Mutual (2008). JPMorgan Chase manages $3.9+ trillion in assets and operates across investment banking, commercial banking, financial services, and asset management in 100+ countries.\n\n"
            "J.P. Morgan (the man) was perhaps the most powerful private banker in American history: he financed the creation of US Steel (1901, the world's first billion-dollar corporation), organised the banking system's bailout during the Panic of 1907, and exercised such dominance over American finance that his power prompted the creation of the Federal Reserve (1913) specifically to prevent any private individual from being indispensable to the US financial system. His legacy institution has since become what the Federal Reserve was designed to prevent — too big to fail.\n\n"
            "JPMorgan Chase under CEO Jamie Dimon (from 2005) navigated the 2008 financial crisis as arguably the strongest major bank — acquiring Bear Stearns (at the Fed's urging) and Washington Mutual while competitors collapsed — and has since faced $30+ billion in regulatory fines for misconduct across multiple jurisdictions. The 'London Whale' trading loss ($6.2 billion, 2012) demonstrated that even the best-managed large bank retains systemic tail risks."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Largest US bank ($3.9T+ assets); J.P. Morgan (the man) financed US Steel (1901) and organised the 1907 Panic bailout; his dominance prompted the Fed's creation; Jamie Dimon's JPMorgan navigated 2008 by acquiring Bear Stearns and WaMu; $30B+ in regulatory fines reflects the challenges of governing globally systemic banks.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "J.P. Morgan's financial genius and his unique position as the creditor and organiser of American corporate consolidation in the Gilded Age — financing railroads, utilities, and industrial mergers — created the dominant American investment bank that became the model for American finance",
            "The 1999 repeal of the Glass-Steagall Act (which had separated commercial and investment banking since 1933) enabled the merger of Chase Manhattan (commercial banking) and J.P. Morgan & Co. (investment banking) in 2000 — creating the universal banking model that JPMorgan Chase embodies",
            "The 2008 financial crisis consolidation — JPMorgan's acquisition of Bear Stearns (at the Fed's urging, for $10/share vs a prior peak of $170) and Washington Mutual — made an already large bank dramatically larger, illustrating how crises concentrate the banking system"
        ],
        "effects": [
            "JPMorgan's 2008 acquisitions (Bear Stearns, Washington Mutual) — made possible by the government's backing — made it the largest US bank, demonstrating that the 'too big to fail' problem created by the crisis made the largest survivors even bigger",
            "Jamie Dimon's management of JPMorgan Chase — $30+ billion in regulatory fines for mortgage fraud, sanctions violations, and market manipulation alongside strong financial performance — is the central case study in whether large bank governance can be regulated effectively",
            "JPMorgan's dominance in investment banking (consistent top-3 globally in M&A advisory, underwriting, and trading) means its bankers shape the capital allocation decisions of the world's largest corporations — making it a powerful actor in global economic development",
            "J.P. Morgan's organisation of the 1907 Panic bailout — using his personal credibility and financial network to stop the crisis — directly motivated the Federal Reserve Act (1913), establishing that private financial power at systemic scale requires public institutional counterweight"
        ],
        "relationships": [
            {"entity": "J.P. Morgan (John Pierpont Morgan)", "relationship": "FOUNDED_BY_AND_NAMED_AFTER", "note": "J.P. Morgan founded the original bank (1871) — his Gilded Age financial dominance created both the institution and the need for the Federal Reserve"},
            {"entity": "Federal Reserve System", "relationship": "PRIVATE_POWER_PROMPTED_CREATION_OF", "note": "J.P. Morgan's dominance over American finance during the 1907 Panic motivated Congress to create the Federal Reserve — preventing any private individual from being financially indispensable"},
            {"entity": "Bear Stearns acquisition (2008)", "relationship": "ACQUIRED_IN_CRISIS_WITH_GOVERNMENT_BACKING", "note": "JPMorgan acquired Bear Stearns (2008, $10/share, previously $170) at the Fed's urging — preventing a disorderly collapse"},
            {"entity": "Jamie Dimon", "relationship": "MOST_SIGNIFICANT_MODERN_CEO", "note": "Jamie Dimon (CEO from 2005) navigated the 2008 crisis as arguably the strongest major bank, building JPMorgan into the largest US financial institution"},
            {"entity": "US Steel (1901)", "relationship": "FINANCING_OF_FIRST_BILLION-DOLLAR_CORPORATION_PROVIDED_BY_PREDECESSOR", "note": "J.P. Morgan financed the creation of US Steel (1901) — the world's first billion-dollar corporation — demonstrating the original bank's role in American industrial consolidation"}
        ],
    }),

    ("goldman-sachs", {
        "summary": (
            "Goldman Sachs Group, Inc. is an American multinational investment bank and financial services company — the most prestigious and profitable investment bank in the world for much of the late 20th and early 21st centuries — whose alumni network has produced Federal Reserve chairs (Janet Yellen served on its board), Treasury Secretaries (Robert Rubin, Hank Paulson), central bank governors (Mario Draghi, Mark Carney), and heads of government (Mario Monti, Lucas Papademos) with a frequency that critics call 'Government Sachs'. Founded in New York in 1869 by Marcus Goldman, it grew from a commercial paper business to the dominant force in global investment banking.\n\n"
            "Goldman's profits during the 2008 financial crisis — while selling mortgage-backed securities to clients it privately described as 'shitty deals' — and its subsequent $550 million SEC settlement (2010) made it the central symbol of Wall Street's ethical failures. Goldman's role in Greece's Eurozone entry (2001) — helping the government structure currency swaps that masked the true size of the deficit — contributed to the Greek sovereign debt crisis (2010–2018) and became a landmark case of investment bank advisory contributing to sovereign financial deception.\n\n"
            "Goldman's 1Malaysia Development Berhad (1MDB) scandal — in which Goldman raised $6.5 billion in bond sales for the Malaysian state fund that became the vehicle for the largest financial fraud in history — resulted in a $5 billion settlement (2020) and became the defining corporate governance scandal of the 2010s."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "World's most prestigious investment bank; 'Government Sachs' alumni include Fed chairs, Treasury Secretaries, central bank governors, and PMs; 2008 crisis mortgage scandal; Greece Eurozone entry currency swap deception; 1MDB fraud ($6.5B bonds, $5B settlement) — the largest financial fraud in history.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Marcus Goldman's commercial paper discount business (1869) — buying merchants' promissory notes at a discount and reselling them to banks — established the core Goldman business model of financial intermediation that evolved into investment banking",
            "Goldman's partnership structure — until its 1999 IPO, a private partnership of senior bankers who shared profits — created an exceptionally strong alignment of interests and a culture of intense talent recruitment that made it the destination for the best Wall Street talent for a century",
            "The post-WWII expansion of corporate mergers, acquisitions, and international capital markets created the demand for sophisticated investment banking services that Goldman — with its analytical culture and relationship networks — was positioned to dominate"
        ],
        "effects": [
            "Goldman's 2008 crisis behaviour — selling mortgage securities it privately described as 'shitty deals' — became the defining case study of investment bank conflicts of interest, leading to the Dodd-Frank Act's Volcker Rule (prohibiting proprietary trading) and reshaping global bank regulation",
            "The 'Government Sachs' phenomenon — Goldman alumni's dominance of senior government financial positions — has made Goldman the central case study in the debate about regulatory capture and the revolving door between Wall Street and Washington",
            "Goldman's Greece Eurozone currency swaps (2001) — helping Greece structure transactions that concealed the true deficit size — contributed to the Greek sovereign debt crisis (2010–2018) that nearly destroyed the Eurozone, exemplifying investment bank advisory responsibility in sovereign finance",
            "The 1MDB scandal ($6.5 billion raised, $5 billion settlement) was the largest financial fraud in corporate history and the most consequential Goldman controversy — demonstrating the systemic risks of investment banks enabling state corruption in emerging markets"
        ],
        "relationships": [
            {"entity": "2008 global financial crisis", "relationship": "PROFITED_WHILE_SELLING_TOXIC_SECURITIES_DURING", "note": "Goldman's 2008 crisis behaviour — selling mortgage securities it described internally as 'shitty deals' — led to the $550M SEC settlement and Dodd-Frank regulation"},
            {"entity": "Greek sovereign debt crisis (2010–2018)", "relationship": "CURRENCY_SWAP_DECEPTION_CONTRIBUTED_TO", "note": "Goldman's 2001 currency swaps helping Greece mask its deficit contributed to the Greek debt crisis — exemplifying investment bank advisory responsibility"},
            {"entity": "1MDB scandal", "relationship": "BOND_SALES_AT_CENTRE_OF", "note": "Goldman raised $6.5B for 1MDB (2012–2013), resulting in a $5B settlement — the defining Goldman controversy and largest financial fraud in corporate history"},
            {"entity": "US Treasury Department", "relationship": "ALUMNI_REVOLVING_DOOR_WITH", "note": "Goldman alumni Robert Rubin and Hank Paulson both served as Treasury Secretary — exemplifying the 'Government Sachs' alumni network"},
            {"entity": "Mario Draghi", "relationship": "GOLDMAN_ALUMNI_INCLUDED", "note": "Mario Draghi worked at Goldman's London office before becoming ECB President — one of many Goldman alumni who shaped global financial governance"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 11 — {len(ENTITIES)} entities (Class 331: Central Banks & Major Banks)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
