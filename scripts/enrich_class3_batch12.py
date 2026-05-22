#!/usr/bin/env python3
"""
Batch 12 — 8 entities (Class 332): Stock Exchanges & Financial Markets
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/332-Class-332"
FILE_PREFIX = "332"
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

    ("amsterdam-stock-exchange", {
        "summary": (
            "The Amsterdam Stock Exchange (Amsterdamsche Beurs, est. 1602) is the world's oldest stock exchange — founded in Amsterdam to trade shares in the Dutch East India Company (VOC), the world's first publicly traded joint-stock company. The Amsterdam Beurs pioneered the fundamental architecture of modern financial markets: publicly traded shares, secondary market trading, options contracts, futures, short selling, and margin trading were all invented or systematised in 17th-century Amsterdam. It remained the world's most sophisticated financial market for most of the 17th and early 18th centuries.\n\n"
            "The Amsterdam exchange's innovations were inseparable from the Dutch Golden Age: the VOC's 1602 IPO raised 6.5 million guilders from 1,143 investors — creating the first widely-held corporate equity — and the subsequent secondary market in VOC shares created the world's first stock market in the modern sense. Joseph de la Vega's 'Confusion de Confusiones' (1688) — describing Amsterdam's market practices — is the oldest book on stock trading and reveals a market remarkably sophisticated in its techniques and participant psychology.\n\n"
            "The Amsterdam Beurs merged with other Dutch exchanges to form Euronext Amsterdam, which subsequently merged with the Paris Bourse, Brussels exchange, and Lisbon exchange to form Euronext — now the largest European stock exchange group. The Amsterdam exchange's 400-year history spans the full arc of modern capitalism: from VOC share trading to sovereign bond markets to modern derivatives to algorithmic trading."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's oldest stock exchange (est. 1602); invented publicly traded shares (VOC IPO), secondary markets, options, futures, short selling, and margin trading; the foundational institution of modern financial capitalism; Joseph de la Vega's 'Confusion de Confusiones' (1688) is the oldest stock trading manual.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Dutch East India Company (VOC) founding in 1602 — merging competing Dutch spice trading companies — required capital on a scale that no individual merchant or family could provide, creating the necessity for a mechanism to pool capital from multiple investors and trade the resulting shares",
            "Amsterdam's position as Europe's dominant commercial and financial centre in the early 17th century — with sophisticated merchant networks, reliable contract enforcement, and a culture of commercial trust — provided the institutional and social foundation for financial market innovation",
            "The Dutch Republic's political stability and commercial law — providing reliable property rights and contract enforcement — created the trust environment in which investors would commit capital to long-duration trading ventures whose returns were years in the future"
        ],
        "effects": [
            "The Amsterdam Beurs pioneered every major financial market instrument — publicly traded shares, secondary market trading, options, futures, short selling, margin trading — that constitutes the architecture of modern financial markets, making it the foundational institution of financial capitalism",
            "The Dutch East India Company's 1602 IPO — raising 6.5 million guilders from 1,143 investors — created the world's first widely-held corporate equity, establishing the principle that productive enterprises could be owned collectively by thousands of unrelated investors",
            "The Dutch financial innovation model — Amsterdam's financial techniques — spread to London (through Dutch-English financial transmission following William III's accession, 1688) and subsequently to the world, making Amsterdam the origin of modern global financial markets",
            "Joseph de la Vega's 'Confusion de Confusiones' (1688) — describing VOC share trading practices — documents the full repertoire of modern market psychology and technique 300 years before they were 'rediscovered' by modern finance, demonstrating the historical depth of financial market behaviour"
        ],
        "relationships": [
            {"entity": "Dutch East India Company (VOC)", "relationship": "FOUNDED_TO_TRADE_SHARES_OF", "note": "The Amsterdam Beurs was founded in 1602 to trade VOC shares — the first publicly traded joint-stock company"},
            {"entity": "Dutch Golden Age", "relationship": "FINANCIAL_HEART_OF", "note": "The Amsterdam Beurs was the financial centre of the Dutch Golden Age — enabling the capital mobilisation that funded global Dutch commercial expansion"},
            {"entity": "London Stock Exchange", "relationship": "FINANCIAL_TECHNIQUES_TRANSMITTED_TO", "note": "Amsterdam's financial innovations spread to London (via William III's Dutch-English connection) — making London the heir to Amsterdam's financial supremacy"},
            {"entity": "Euronext", "relationship": "MERGED_INTO", "note": "The Amsterdam Beurs merged into Euronext — the pan-European exchange group — continuing its 400-year trading heritage"},
            {"entity": "Modern financial markets", "relationship": "INVENTED_FOUNDATIONAL_INSTRUMENTS_OF", "note": "Amsterdam invented publicly traded shares, secondary markets, options, futures, and short selling — the complete architecture of modern financial markets"}
        ],
    }),

    ("london-stock-exchange", {
        "summary": (
            "The London Stock Exchange (LSE, est. 1801, with antecedents to 1571 and informal trading since 1698) is one of the world's oldest and most historically significant stock exchanges — the financial market at the centre of the British Empire's global capital mobilisation for three centuries. The Royal Exchange (1571, founded by Thomas Gresham) provided London's first formal commercial meeting place; Jonathan's Coffee House (1698) hosted informal share trading; and the formalisation of the Stock Exchange (1801) created the institutional infrastructure of the world's second-largest stock market.\n\n"
            "The LSE's most historically consequential role was financing the British Empire and British industrialisation: from 18th-century government bonds (gilts) that financed British wars to the 19th-century railway mania (London raised capital for railways across five continents) to 20th-century colonial infrastructure bonds. In the late 19th century, London was unquestionably the world's dominant financial market — its bond market financed the construction of global infrastructure (Argentine railways, Indian irrigation, Egyptian cotton) that shaped developing countries' economic trajectories.\n\n"
            "The 1986 'Big Bang' deregulation — abolishing fixed commissions, allowing foreign membership, and introducing electronic trading — transformed the LSE from a gentleman's club of fixed-fee stockbrokers to a globalised electronic exchange, making London the dominant European financial centre and one of the world's most important capital markets. The LSE merged with Borsa Italiana (2007) and attempted (ultimately unsuccessful) mergers with Deutsche Börse."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "World's oldest and historically most influential stock exchange after Amsterdam; financed the British Empire, British industrialisation, and global railway construction; 1986 Big Bang deregulation made London the dominant European financial centre; the LSE's gilt market funded British wars from Napoleonic to WWII.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Thomas Gresham's Royal Exchange (1571) — modelled on Antwerp's Bourse — provided London's first formal commercial meeting place, creating the institutional foundation for London's financial market development",
            "The British government's growing need for debt financing — particularly from the Nine Years' War (1694) onward — created demand for a liquid government bond (gilt) market, which required an organised exchange for secondary trading",
            "London's position as the centre of the British Empire's global commercial network — with merchants, insurers, and financiers concentrated in the City — created the density of financial activity that made a centralised exchange economically rational"
        ],
        "effects": [
            "The LSE's gilt market funded every major British military campaign from the Napoleonic Wars to WWII — demonstrating that access to liquid capital markets is a decisive strategic advantage in industrial-era warfare",
            "London's global capital export through the LSE (1870s–1914) — financing railways, utilities, and infrastructure across five continents — was the largest transfer of capital in history to that date, shaping the economic development trajectories of Argentina, India, Australia, and dozens of other countries",
            "The 1986 Big Bang deregulation — abolishing fixed commissions, allowing foreign members, introducing electronic SEAQ trading — transformed London from a restricted domestic exchange into the dominant European financial centre, contributing to the City of London's 21st-century position as Europe's financial capital",
            "The LSE's Alternative Investment Market (AIM, 1995) — a lighter-regulated market for smaller companies — became the world's most active small-cap market, demonstrating that graduated regulatory frameworks can extend capital market access to smaller enterprises"
        ],
        "relationships": [
            {"entity": "Royal Exchange (1571)", "relationship": "ANTECEDENT_INSTITUTION", "note": "Thomas Gresham's Royal Exchange (1571) was the LSE's antecedent — London's first formal commercial meeting place"},
            {"entity": "British Empire", "relationship": "PRIMARY_CAPITAL_MARKET_FOR", "note": "The LSE was the financial market at the centre of British imperial capital mobilisation — financing colonial infrastructure across five continents"},
            {"entity": "Big Bang deregulation (1986)", "relationship": "TRANSFORMED_BY", "note": "The 1986 Big Bang — abolishing fixed commissions, allowing foreign members, introducing electronic trading — made London Europe's dominant financial centre"},
            {"entity": "Amsterdam Stock Exchange", "relationship": "INHERITED_FINANCIAL_SUPREMACY_FROM", "note": "London inherited Amsterdam's financial supremacy in the early 18th century — via Dutch-English financial transmission following William III's accession"},
            {"entity": "New York Stock Exchange", "relationship": "COMPETED_FOR_GLOBAL_FINANCIAL_LEADERSHIP_WITH", "note": "LSE and NYSE competed for global financial leadership — London dominant to 1914, NYSE dominant since"}
        ],
    }),

    ("new-york-stock-exchange", {
        "summary": (
            "The New York Stock Exchange (NYSE, est. 1792) is the world's largest stock exchange by market capitalisation ($25+ trillion) — the financial institution at the centre of American capitalism and the primary capital market for the world's largest economy. Founded under the Buttonwood Agreement (signed by 24 stockbrokers under a buttonwood tree on Wall Street, 17 May 1792), the NYSE formalised New York's securities trading and became the primary market for the successive waves of American industrialisation: canals, railroads, steel, oil, automobiles, and technology.\n\n"
            "The NYSE's most historically consequential moments define the arc of American financial history: the Wall Street Crash (October 1929) — when the Dow Jones Industrial Average fell 25% in two days — triggered the Great Depression; the post-WWII bull market (1945–1966) financed American economic dominance; the 1980s Bull Market under Reagan validated shareholder capitalism; and the dot-com bubble (1995–2000) and 2008 financial crisis tested the exchange's ability to function under extreme stress.\n\n"
            "The NYSE's floor trading culture — the 'open outcry' auction system, specialist firms, and trading floor itself — was the defining image of American capitalism for two centuries. Electronic trading and the 2005 merger with Archipelago Exchange transformed it from a physical market to a hybrid electronic-floor exchange. NYSE is now part of Intercontinental Exchange (ICE), having merged in 2013."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's largest stock exchange by market cap ($25T+); 1929 Wall Street Crash triggered the Great Depression; primary capital market for American industrialisation from railroads to tech; the defining institution of US financial capitalism; Buttonwood Agreement (1792) founding — 230+ years of continuous operation.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Buttonwood Agreement (1792) — 24 New York stockbrokers agreeing to trade only with each other and to maintain fixed commissions — created the organised market structure that replaced informal Wall Street trading, establishing New York as America's primary financial market",
            "The US federal government's post-Revolutionary War debt issuance — requiring a market for trading government bonds — provided the initial demand for a formal securities market that the NYSE's founding members were designed to serve",
            "New York's geographic position — the largest port and commercial centre in the young United States — created the concentration of merchants, insurers, and financiers that made a centralised securities market economically viable"
        ],
        "effects": [
            "The Wall Street Crash (October 1929) — Dow Jones fell 89% from peak to trough, 1929–1932 — triggered the Great Depression by destroying wealth, freezing credit, and collapsing investment, demonstrating that stock market crashes can be the proximate cause of macroeconomic catastrophe",
            "The NYSE's financing of American industrialisation — railroads (1840s–1860s), steel (1890s), oil (1900s), automobiles (1920s), and technology (1990s–2000s) — made it the primary mechanism of American capital allocation, shaping the country's industrial development trajectory",
            "The NYSE's post-WWII global dominance — becoming the primary listing venue for international corporations — reflected and reinforced American economic hegemony, making New York the world's dominant financial centre for the second half of the 20th century",
            "The NYSE's listing of hundreds of Chinese companies (Alibaba, JD.com, etc.) and subsequent US-China tensions over Chinese company delisting illustrates how the exchange has become a theatre for US-China geopolitical competition in financial markets"
        ],
        "relationships": [
            {"entity": "Buttonwood Agreement (1792)", "relationship": "FOUNDED_UNDER", "note": "The NYSE was founded under the Buttonwood Agreement — 24 New York stockbrokers agreeing to a fixed-commission organised market"},
            {"entity": "Wall Street Crash (1929)", "relationship": "LOCATION_OF_MARKET_COLLAPSE_THAT_TRIGGERED", "note": "The 1929 crash on the NYSE — Dow Jones fell 89% — triggered the Great Depression, the defining event in the NYSE's history"},
            {"entity": "American industrialisation", "relationship": "PRIMARY_CAPITAL_MARKET_FOR", "note": "The NYSE financed successive waves of American industrialisation — from canals and railroads to steel, oil, automobiles, and technology"},
            {"entity": "Intercontinental Exchange (ICE)", "relationship": "ACQUIRED_BY", "note": "NYSE merged with ICE (2013) — making the world's largest stock exchange part of a derivatives and exchange conglomerate"},
            {"entity": "NASDAQ", "relationship": "COMPETED_WITH_FOR_TECHNOLOGY_LISTINGS", "note": "NYSE and NASDAQ competed for technology company listings — NASDAQ becoming the technology company's preferred venue from the 1970s onward"}
        ],
    }),

    ("nasdaq", {
        "summary": (
            "NASDAQ (National Association of Securities Dealers Automated Quotations, est. 1971) is an American stock exchange — the world's second-largest by market capitalisation and the exchange most associated with the technology sector — that was the world's first electronic stock market, replacing the physical floor trading that characterised traditional exchanges. NASDAQ's founding by the NASD (1971) introduced fully automated, screen-based securities trading — the technological innovation that would eventually transform every stock exchange globally.\n\n"
            "NASDAQ became the preferred listing venue for technology companies because of its lower listing requirements (compared to NYSE) and its culture of innovation: Apple (1980), Microsoft (1986), Intel, Oracle, Amazon (1997), Google (2004), and Meta (2012) all chose NASDAQ. The NASDAQ Composite Index — tracking all NASDAQ-listed companies — became the primary benchmark for technology sector performance, and the dot-com bubble's inflation and collapse (1995–2000) — when the NASDAQ Composite rose 400% then fell 78% — is the definitive case study in speculative asset price bubbles.\n\n"
            "NASDAQ's technological architecture — electronic limit order book trading, anonymous matching, microsecond execution — created the model that all modern electronic exchanges adopted, while its market maker system created competition among dealers that lowered trading costs for investors. NASDAQ's merger with OMX (2008) and acquisitions of the Nordic/Baltic exchanges created the world's most geographically diverse exchange group."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "World's first electronic stock market (est. 1971); preferred listing venue for Apple, Microsoft, Amazon, Google, Meta; the dot-com bubble collapse (NASDAQ -78%, 2000–2002) is the definitive speculative bubble case study; NASDAQ's electronic architecture was adopted by every major exchange globally.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The US securities industry's recognition (early 1970s) that the over-the-counter market — where securities were traded informally by phone between dealers — could be made more transparent and efficient through automated quotation technology created the political will for NASDAQ's founding",
            "The SEC's Maloney Act (1938) — creating a framework for self-regulatory organisations in the securities industry — provided the legal foundation for the NASD to create and operate an automated quotation system",
            "The rapid development of computer and telecommunications technology in the late 1960s — making real-time electronic price quotation and order routing technically feasible — created the technological opportunity that NASDAQ's founders seized"
        ],
        "effects": [
            "NASDAQ's electronic trading model — automated order routing, electronic limit order book, microsecond execution — was adopted globally and transformed every major stock exchange, effectively ending floor trading as the dominant market mechanism by the 2010s",
            "NASDAQ's role as the preferred venue for technology company IPOs — Apple, Microsoft, Intel, Amazon, Google, Meta — made it the capital market engine of the digital economy, allocating hundreds of billions of dollars to technology sector growth",
            "The dot-com bubble and collapse (NASDAQ Composite: +400% to 5,048 in March 2000, then -78% to 1,114 by October 2002) is the definitive modern case study in speculative asset price bubbles — studied in every finance curriculum globally",
            "NASDAQ's market maker competition model — multiple competing dealers quoting prices rather than a single specialist — created price competition that significantly reduced the bid-ask spread for investors, demonstrating that exchange market structure choices have direct consequences for retail investor costs"
        ],
        "relationships": [
            {"entity": "Technology sector (US)", "relationship": "PRIMARY_CAPITAL_MARKET_FOR", "note": "NASDAQ is the preferred listing venue for technology companies — Apple, Microsoft, Amazon, Google, Meta — making it the capital market engine of the digital economy"},
            {"entity": "Dot-com bubble (1995–2002)", "relationship": "BENCHMARK_INDEX_INFLATED_AND_COLLAPSED_DURING", "note": "NASDAQ Composite rose 400% then fell 78% during the dot-com bubble — the definitive modern speculative bubble case study"},
            {"entity": "Electronic trading", "relationship": "PIONEERED_AND_GLOBALISED", "note": "NASDAQ invented fully electronic stock trading (1971) — the model adopted by every major exchange globally, ending physical floor trading as the dominant mechanism"},
            {"entity": "New York Stock Exchange", "relationship": "COMPETES_WITH", "note": "NASDAQ and NYSE compete for technology company listings — NASDAQ dominating technology from the 1980s onward"},
            {"entity": "OMX exchange group", "relationship": "MERGED_WITH", "note": "NASDAQ merged with OMX (2008) — creating a pan-Atlantic exchange group spanning North America and Nordic/Baltic markets"}
        ],
    }),

    ("bombay-stock-exchange", {
        "summary": (
            "The Bombay Stock Exchange (BSE, est. 1875) is Asia's oldest stock exchange and India's largest — the primary capital market institution in the world's most populous country and a major emerging market exchange. Founded under a banyan tree on Dalal Street, Mumbai, by stockbroker Premchand Roychand and the Native Share & Stock Brokers' Association, the BSE became India's primary capital market institution — financing the Bombay cotton industry, Indian railways, and subsequently the modern Indian corporate sector.\n\n"
            "The BSE's SENSEX (Sensitive Index, est. 1986) — tracking 30 major BSE-listed companies — is the most watched benchmark of Indian economic sentiment globally. The BSE's market capitalisation of $4+ trillion (2023) reflects India's emergence as a major investment destination and its rapid economic growth. The BSE underwent a landmark demutualisation (2005) — transforming from a broker-owned cooperative into a publicly listed company — reflecting the modernisation of Asian exchange governance.\n\n"
            "The BSE's history reflects the full arc of Indian capitalism: from Premchand Roychand's 19th-century share mania (the 'Back Bay Reclamation' speculative bubble of 1865) through the post-independence state-directed economy's constraints on equity markets to the post-1991 liberalisation boom that transformed the BSE into a globally significant exchange. Today the BSE competes with the National Stock Exchange (NSE, est. 1992) — which now exceeds BSE in trading volume."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Asia's oldest stock exchange (est. 1875); India's primary capital market; $4T+ market cap; SENSEX is the global benchmark for Indian economic sentiment; BSE's history spans India's colonial to postcolonial to liberalised economic trajectory.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Mumbai's (Bombay's) position as India's commercial capital — the centre of the cotton trade, the textile industry, and the British colonial commercial network — created the concentration of merchants, brokers, and capital that made a formal stock exchange viable",
            "The 1860s cotton boom — driven by the American Civil War's disruption of US cotton supply — created speculative stock trading activity in Mumbai that the informal tree-based trading system could not adequately support, motivating formalisation",
            "British colonial India's development of commercial infrastructure — railways, telegraph, courts — provided the institutional environment (contract enforcement, communications) required for organised capital markets to function"
        ],
        "effects": [
            "The BSE's SENSEX (1986) became the primary global benchmark for Indian economic performance — closely watched by global investors as India emerged as a major investment destination in the 1990s and 2000s",
            "The BSE's post-1991 liberalisation growth — as the Indian economy opened to private investment — made it a major emerging market exchange, attracting global portfolio investment and enabling Indian corporate expansion",
            "BSE demutualisation (2005) and listing — transforming from a broker cooperative to a publicly listed exchange — provided the governance model for Asian exchange modernisation",
            "The competition between BSE and NSE (est. 1992) — which exceeded BSE in trading volume — is the most significant example of competitive exchange market structure in emerging markets, demonstrating that competition between exchanges can drive innovation and lower trading costs"
        ],
        "relationships": [
            {"entity": "Dalal Street, Mumbai", "relationship": "LOCATED_ON", "note": "BSE is located on Dalal Street, Mumbai — the address synonymous with Indian financial markets"},
            {"entity": "SENSEX", "relationship": "OPERATES_BENCHMARK_INDEX", "note": "BSE's SENSEX (30-company index, est. 1986) is the primary global benchmark for Indian economic performance"},
            {"entity": "National Stock Exchange of India (NSE)", "relationship": "COMPETES_WITH", "note": "NSE (est. 1992) now exceeds BSE in trading volume — the most significant emerging market exchange competition"},
            {"entity": "Indian economic liberalisation (1991)", "relationship": "TRANSFORMED_BY", "note": "The 1991 liberalisation opened India to private investment — dramatically expanding BSE's role as a capital market"},
            {"entity": "Premchand Roychand", "relationship": "FOUNDED_BY", "note": "Premchand Roychand co-founded the BSE (1875) — the pioneering Indian stockbroker who established Asia's oldest exchange"}
        ],
    }),

    ("shanghai-stock-exchange", {
        "summary": (
            "The Shanghai Stock Exchange (SSE, est. 1990) is China's largest stock exchange and the world's third-largest by market capitalisation ($7+ trillion) — the primary capital market institution of the world's second-largest economy. Founded in December 1990 as part of Deng Xiaoping's market reform programme — one of the Communist Party's most significant ideological departures, since stock markets are quintessential capitalist institutions — the SSE reopened Chinese equity markets that had been closed since the Communist revolution (1949).\n\n"
            "The SSE's founding represented one of the most consequential ideological compromises in political-economic history: the Chinese Communist Party, committed to a 'socialist market economy', established a stock exchange as an instrument of capital allocation — reconciling market pricing with state ownership through the device of 'A-shares' (traded domestically in RMB, restricted to Chinese investors) and 'B-shares' (traded in foreign currency, accessible to foreigners). The SSE Composite Index (established 1990) became the benchmark for Chinese market sentiment.\n\n"
            "The SSE's extraordinary volatility — the Chinese stock market fell 50%+ in 2015 over 3 months, prompting the government to ban large shareholders from selling and use state funds to purchase stocks — demonstrates the tension between market mechanisms and state control that characterises China's 'socialist market economy'. The SSE is the primary listing venue for Chinese state-owned enterprises — the largest SOEs in the world by revenue."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "China's largest stock exchange (est. 1990, $7T+ market cap); one of the most ideologically consequential CCP decisions — establishing a stock market under socialism; primary listing venue for Chinese SOEs; 2015 market crash (−50%) demonstrated tension between market mechanisms and state control.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Deng Xiaoping's market reform programme — establishing special economic zones, allowing private enterprise, and eventually accepting equity markets as instruments of capital allocation — created the ideological and political framework for the SSE's founding",
            "China's post-1978 economic opening created state-owned enterprises that needed capital — which bank lending alone could not efficiently provide — motivating the establishment of equity markets as a capital allocation mechanism",
            "The Communist Party's pragmatic decision that 'socialism with Chinese characteristics' could incorporate market pricing mechanisms — the 'socialist market economy' concept — provided the ideological legitimation for establishing a stock exchange"
        ],
        "effects": [
            "The SSE's establishment (1990) reopened Chinese equity markets after 41 years of Communist closure — representing one of history's most consequential ideological compromises and establishing the institutional foundation for China's emergence as a major capital market",
            "The SSE's listing of Chinese SOEs (Industrial and Commercial Bank of China, PetroChina, SAIC Motor) provided the world's most important testing ground for state-owned enterprise equity governance — demonstrating both the possibilities and limitations of partial privatisation",
            "The 2015 market crash (SSE Composite fell 50%+ in 3 months) — and the government's unprecedented intervention (banning sales, using state funds to buy stocks) — demonstrated the fundamental tension between market pricing and state control that characterises Chinese equity markets",
            "The SSE's Stock Connect programmes with Hong Kong (2014–) — allowing qualified foreign investors to access A-shares and Chinese investors to access HK stocks — began integrating Chinese equity markets into the global financial system, with profound implications for global portfolio allocation"
        ],
        "relationships": [
            {"entity": "Deng Xiaoping", "relationship": "MARKET_REFORMS_THAT_ENABLED_FOUNDING_DRIVEN_BY", "note": "Deng's market reform programme created the ideological and political conditions for establishing a stock exchange under Communist Party rule"},
            {"entity": "Chinese state-owned enterprises", "relationship": "PRIMARY_LISTING_VENUE_FOR", "note": "The SSE is the primary listing venue for China's largest SOEs — Industrial and Commercial Bank of China, PetroChina — the world's largest state-owned enterprises"},
            {"entity": "2015 Chinese stock market crash", "relationship": "LOCATION_OF", "note": "The 2015 crash (SSE Composite -50% in 3 months) and government intervention demonstrated the tension between market mechanisms and state control"},
            {"entity": "Shanghai-Hong Kong Stock Connect", "relationship": "INTEGRATES_INTO_GLOBAL_MARKETS_THROUGH", "note": "The Stock Connect programme (2014) began integrating Chinese equity markets into the global financial system"},
            {"entity": "Chinese Communist Party", "relationship": "CONTROLS_REGULATORY_FRAMEWORK_OF", "note": "The CCP controls the SSE's regulatory framework — the CSRC — reflecting the party-state's ultimate authority over Chinese capital markets"}
        ],
    }),

    ("chicago-board-of-trade", {
        "summary": (
            "The Chicago Board of Trade (CBOT, est. 1848) is the world's oldest futures and options exchange — the institution that invented standardised commodity futures contracts, creating the foundation of the modern derivatives market. Founded by 82 Chicago merchants to address the chaotic and inefficient trading of agricultural commodities in a booming Midwestern market hub, the CBOT introduced the standardised forward contract (1865) — the 'futures contract' — specifying quantity, quality, and delivery date for grain, allowing buyers and sellers to hedge price risk months in advance.\n\n"
            "The CBOT's futures contracts solved a fundamental problem of agricultural markets: farmers and grain merchants faced ruinous price volatility between harvest and delivery. Standardised futures allowed farmers to 'lock in' prices before harvest and merchants to hedge inventories — transferring price risk to speculators willing to bear it in exchange for profit potential. This mechanism — price discovery through futures trading — became the pricing mechanism for agricultural commodities globally.\n\n"
            "The CBOT merged with the Chicago Mercantile Exchange (CME) in 2007 to form CME Group — the world's largest derivatives exchange group, handling $1 quadrillion (notional) in annual derivatives trading. The futures market has expanded far beyond agriculture: financial futures (interest rates, stock indices, foreign exchange) — introduced at the CME in 1972 and subsequently at the CBOT — transformed futures from an agricultural hedging tool to the foundational mechanism of global financial risk management."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "World's oldest futures exchange (est. 1848); invented the standardised futures contract (1865) — the foundational instrument of the derivatives market; futures pricing now sets agricultural commodity prices globally; merged with CME (2007) to form the world's largest derivatives group ($1 quadrillion notional annual trading).",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Chicago's position as the hub of Midwestern grain marketing — connected by rail to East Coast markets and by water to Great Lakes shipping — created the commercial concentration of grain traders, merchants, and speculators that made a centralised exchange viable",
            "The chaos of 19th-century grain markets — with each transaction negotiated individually, wildly variable quality standards, and no mechanism for price discovery — created the commercial incentive to develop standardised contracts that reduced transaction costs",
            "The rapid development of the Midwest's agricultural economy after the Illinois Central Railroad's extension (1856) — dramatically increasing grain volumes flowing through Chicago — created the market scale that justified the administrative infrastructure of a futures exchange"
        ],
        "effects": [
            "The standardised futures contract (1865) — CBOT's most consequential innovation — created the mechanism for transferring price risk from producers (who need stable prices) to speculators (who accept risk for profit), making agricultural markets more efficient globally",
            "CBOT futures pricing became the global reference price for corn, wheat, and soybeans — prices quoted in Chicago set the prices at which farmers in Brazil, Argentina, Australia, and the US plant, grow, and sell their crops, making the CBOT the most consequential institution in global food price determination",
            "Financial futures (interest rate futures, 1977 at CBOT; stock index futures, 1982 at CME) expanded the futures mechanism to financial markets — creating the instruments that now allow every major bank, pension fund, and corporation to hedge interest rate, equity, and currency risk",
            "The CME Group (CBOT + CME merger, 2007) — handling $1 quadrillion in annual notional derivatives volume — is the most systemically important exchange group in the global financial system, processing more notional value than all equity markets combined"
        ],
        "relationships": [
            {"entity": "Standardised futures contract (1865)", "relationship": "INVENTED", "note": "CBOT invented the standardised futures contract (1865) — the foundational instrument of the $1 quadrillion global derivatives market"},
            {"entity": "Global agricultural commodity prices", "relationship": "PRICING_BENCHMARK_FOR", "note": "CBOT futures prices for corn, wheat, and soybeans set global agricultural reference prices — affecting farmers from Brazil to Australia"},
            {"entity": "Chicago Mercantile Exchange", "relationship": "MERGED_WITH_TO_FORM_CME_GROUP", "note": "CBOT and CME merged (2007) to form CME Group — the world's largest derivatives exchange group"},
            {"entity": "CME Group", "relationship": "MERGED_INTO", "note": "CME Group (est. 2007 by CBOT-CME merger) handles $1 quadrillion in annual notional derivatives — the world's largest derivatives exchange group"},
            {"entity": "Chicago, Illinois", "relationship": "FOUNDED_IN_AND_CENTRAL_TO_COMMERCIAL_IDENTITY_OF", "note": "The CBOT is inseparable from Chicago's identity as America's commodity and futures trading capital"}
        ],
    }),

    ("new-york-mercantile-exchange", {
        "summary": (
            "The New York Mercantile Exchange (NYMEX, est. 1872) is the world's largest physical commodity futures exchange — the primary market for pricing crude oil, natural gas, heating oil, gasoline, and other energy commodities globally. Originally founded as the Butter and Cheese Exchange of New York, NYMEX evolved through a series of product expansions before introducing crude oil futures (1983) — the innovation that made it the price-setting institution for the world's most traded commodity and the most important commercial energy price in the global economy.\n\n"
            "The NYMEX crude oil futures contract (West Texas Intermediate, WTI) — introduced in 1983 — became the global benchmark for crude oil pricing, with 'NYMEX WTI' quoted as the reference price by oil producers, refiners, airlines, and governments worldwide. The WTI futures price is the single most important commercial commodity price in the global economy — affecting the costs of transportation, heating, electricity, petrochemicals, and fertilisers globally. OPEC's production decisions are measured against NYMEX WTI prices.\n\n"
            "NYMEX merged with COMEX (1994) and was subsequently acquired by CME Group (2008), becoming the energy and metals trading division of the world's largest derivatives exchange. The 2020 oil price crash — when WTI futures briefly traded at negative $37/barrel (the first negative oil price in history) — demonstrated the extraordinary volatility of energy commodity prices during demand collapses."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "World's largest physical commodity futures exchange; WTI crude oil futures (est. 1983) set the global oil price benchmark; 2020 negative oil price ($-37/barrel) was the most dramatic commodity market event in history; NYMEX prices directly affect transportation, heating, electricity, and petrochemical costs globally.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The 1970s oil price shocks (OPEC embargo 1973, Iranian Revolution 1979) — creating extreme oil price volatility — created the need for a risk management instrument that allowed oil users (airlines, refiners, utilities) to hedge against price uncertainty, motivating the development of oil futures",
            "The deregulation of US oil prices (1981) — ending price controls and allowing market pricing — created the price volatility that made hedging necessary and made New York the natural location for a futures exchange to serve the major oil refiners and traders concentrated in the northeastern US",
            "The success of agricultural futures at the CBOT demonstrated the commercial viability of standardised commodity futures contracts — providing the model that NYMEX applied to oil and other energy commodities"
        ],
        "effects": [
            "The WTI crude oil futures contract (1983) created the global oil price benchmark — making the NYMEX trading floor the location where the world's most important commodity price was determined, affecting every economy globally",
            "NYMEX energy futures enabled hedging of energy price risk by airlines, utilities, refiners, and shipping companies — reducing the financial impact of oil price volatility on the broader economy",
            "The 2020 negative oil price (WTI at -$37/barrel on 20 April 2020) — caused by storage capacity exhaustion as COVID-19 collapsed demand — demonstrated the extraordinary tail risks in physical commodity derivatives and triggered regulatory review of futures market mechanics",
            "Natural gas futures at NYMEX (Henry Hub, est. 1990) became the global natural gas benchmark — particularly important as the US became the world's largest LNG exporter, making Henry Hub prices globally relevant"
        ],
        "relationships": [
            {"entity": "WTI crude oil futures contract", "relationship": "OPERATES_GLOBAL_BENCHMARK", "note": "NYMEX WTI crude oil futures (est. 1983) set the global oil price benchmark — the most important commercial commodity price in the world"},
            {"entity": "OPEC", "relationship": "PRODUCTION_DECISIONS_MEASURED_AGAINST_BENCHMARK_OF", "note": "OPEC's production decisions are calibrated against NYMEX WTI prices — making NYMEX central to global energy geopolitics"},
            {"entity": "2020 oil price crash (negative prices)", "relationship": "BENCHMARK_REACHED_NEGATIVE_PRICE_ON", "note": "WTI fell to -$37/barrel on 20 April 2020 — the most dramatic commodity market event in history"},
            {"entity": "CME Group", "relationship": "ACQUIRED_BY", "note": "CME Group acquired NYMEX (2008) — making energy and metals futures part of the world's largest derivatives exchange group"},
            {"entity": "1973 OPEC oil embargo", "relationship": "PRICE_VOLATILITY_TRIGGERED_FUTURES_MARKET_DEVELOPMENT", "note": "The 1973 oil embargo's price volatility created the demand for oil price hedging instruments that NYMEX's crude oil futures (1983) addressed"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 12 — {len(ENTITIES)} entities (Class 332: Stock Exchanges & Financial Markets)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
