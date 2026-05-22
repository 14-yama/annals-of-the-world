#!/usr/bin/env python3
"""
Batch 09 — 8 entities (Class 330): Major Corporations
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/330-Class-330"
FILE_PREFIX = "330"
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

    ("east-india-company", {
        "summary": (
            "The East India Company (EIC, 1600–1874) was an English and subsequently British joint-stock company that began as a trading enterprise and evolved into a sovereign power governing the Indian subcontinent — the most consequential corporate institution in history. Founded by royal charter of Queen Elizabeth I on 31 December 1600, the Company was granted a monopoly on English trade with the East Indies. Within a century it had established trading posts from Surat to Java; within two centuries it governed Bengal (from 1757) and administered a standing army larger than most European powers.\n\n"
            "The Company's transformation from trader to ruler is one of history's most dramatic institutional metamorphoses. Robert Clive's victory at the Battle of Plassey (1757) — using 3,000 Company soldiers to defeat Nawab Siraj ud-Daulah's 50,000-strong army through treachery and tactical superiority — gave the Company control of Bengal, one of the subcontinent's wealthiest regions. The Company subsequently extracted £30 million from Bengal in the decade following Plassey — contributing to Bengal's Great Famine (1769–1773) that killed an estimated 10 million people.\n\n"
            "The Indian Rebellion of 1857 — triggered by sepoys' (Indian soldiers') grievances, fear of religious pollution, and accumulated colonial injustices — ended Company rule: Parliament transferred sovereignty to the Crown (the Government of India Act, 1858). The EIC's commercial and governance model — joint-stock financing, territorial expansion, monopoly exploitation — pioneered corporate capitalism and colonial administration on a global scale."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "English/British joint-stock company (1600–1874) that became the sovereign ruler of the Indian subcontinent; Plassey (1757) gave it Bengal's governance; the Bengal Famine (1769–73) killed 10 million; the 1857 Rebellion ended Company rule; pioneered corporate capitalism and colonialism on a global scale.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The spice trade's extraordinary profitability — nutmeg, pepper, and cloves from Southeast Asia commanded prices 200x their Asian origin price in European markets — created the commercial incentive that drove European investment in East India companies",
            "The joint-stock company structure — spreading the financial risk of long ocean voyages across multiple investors — made the EIC viable where individual merchant finance was not, pioneering the corporate capitalism model",
            "Britain's growing naval power and the declining Mughal Empire's inability to enforce sovereignty over its coastal territories created the military and political conditions for the EIC's transition from trading company to governing power"
        ],
        "effects": [
            "The EIC's governance of India (1757–1858) created the administrative structures, legal systems, and economic extractive patterns that the British Raj (1858–1947) inherited — making the Company's institutional choices foundational to modern India and Pakistan",
            "The Bengal Famine (1769–1773) — killing an estimated 10 million people, one-third of Bengal's population, partly caused by the Company's revenue extraction and grain export policies — exemplifies the humanitarian consequences of corporate governance without accountability",
            "The EIC pioneered the joint-stock company as a vehicle for colonial expansion — its model was replicated by the Dutch VOC, the Hudson's Bay Company, the Virginia Company, and eventually by the modern multinational corporation",
            "The Indian Rebellion of 1857 — ending Company rule — triggered the British Parliament's assertion of sovereign responsibility for India, creating the direct colonial relationship of the British Raj that shaped the subcontinent's history until independence in 1947"
        ],
        "relationships": [
            {"entity": "Battle of Plassey (1757)", "relationship": "GAINED_BENGAL_GOVERNANCE_AT", "note": "Clive's victory at Plassey (1757) gave the EIC control of Bengal — beginning its transformation from trader to ruler"},
            {"entity": "Bengal Famine (1769–1773)", "relationship": "EXTRACTION_POLICIES_CONTRIBUTED_TO", "note": "The EIC's revenue extraction and grain export policies contributed to the Bengal Famine — killing an estimated 10 million people"},
            {"entity": "Indian Rebellion of 1857", "relationship": "RULE_ENDED_BY", "note": "The 1857 Rebellion ended Company rule — Parliament transferred sovereignty to the Crown (Government of India Act, 1858)"},
            {"entity": "Robert Clive", "relationship": "BENGAL_GOVERNANCE_ACQUIRED_THROUGH_VICTORY_OF", "note": "Robert Clive's victory at Plassey (1757) — defeating Siraj ud-Daulah through treachery and superior tactics — established the EIC's territorial empire"},
            {"entity": "British Raj (1858–1947)", "relationship": "ADMINISTRATIVE_PREDECESSOR_TO", "note": "The British Raj inherited the EIC's administrative structures, legal systems, and extractive patterns — making the Company foundational to colonial India"}
        ],
    }),

    ("ab-volvo", {
        "summary": (
            "AB Volvo is a Swedish multinational manufacturing company — one of the world's largest producers of trucks, buses, construction equipment, and marine and industrial engines. Founded in Gothenburg in 1927 by Gustaf Larson and Assar Gabrielsson (as a subsidiary of ball-bearing maker SKF), Volvo was originally a car manufacturer. The company's guiding design philosophy — 'safety first' — made it the pioneer of automotive safety technology: the three-point seat belt (1959, invented by Nils Bohlin) was the single most important automotive safety innovation in history, credited with saving over one million lives.\n\n"
            "Volvo's corporate evolution has been transformative: the car division was sold to Ford Motor Company (1999) and subsequently to Geely of China (2010), while AB Volvo retained trucks, buses, and construction equipment. The Volvo Group (AB Volvo) is now primarily a heavy transport and construction equipment company — the world's second-largest manufacturer of heavy trucks. Volvo's truck brands include Volvo, Renault Trucks, and Mack (US), while its construction equipment brands include Volvo CE and SDLG.\n\n"
            "Volvo's safety engineering legacy extends far beyond its corporate boundaries: the three-point belt (freely licensed by Volvo in 1959 to every car manufacturer) is now standard equipment in every car globally and has saved more than a million lives. The company's commitment to making safety innovations freely available to the industry reflects a distinctive Swedish corporate ethic that prioritised public benefit over competitive advantage."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Swedish manufacturing company (est. 1927); invented the three-point seat belt (1959) — freely licensed to all manufacturers, saving over 1 million lives; now the world's second-largest heavy truck manufacturer; Geely (China) owns Volvo Cars; the three-point belt is the single most consequential automotive safety innovation.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Gustaf Larson and Assar Gabrielsson's conviction that Swedish climatic and road conditions required a specifically Swedish car — sturdier and more reliable than imported vehicles — motivated the founding of Volvo as a domestic manufacturing enterprise",
            "Sweden's 20th-century engineering culture — emphasising safety, quality, and functionality over style — created the corporate DNA that produced the three-point seat belt and made Volvo synonymous with automotive safety",
            "The post-WWII Swedish economic model — combining industrial ambition with social democratic values — created the context in which Volvo's decision to freely license the seat belt was both commercially rational (building brand trust) and culturally consistent"
        ],
        "effects": [
            "The three-point seat belt (1959) — freely licensed by Volvo to every car manufacturer — is credited with saving over one million lives globally and reducing automotive fatalities by approximately 50% for front-seat passengers — the single most consequential automotive safety innovation",
            "Volvo's heavy truck division — particularly after the acquisition of Renault Trucks (2001) and Mack (1990) — made the company a dominant force in global freight transport, shaping the supply chains of every major economy",
            "Ford's acquisition of Volvo Cars (1999) and Geely's subsequent purchase (2010) demonstrated the globalisation of the automotive industry — with a Swedish brand passing from American to Chinese ownership while retaining its Swedish engineering identity",
            "Volvo's safety-first philosophy influenced the entire automotive industry: ABS braking, airbags, and crash safety standards all developed under the competitive pressure created by Volvo's safety marketing and engineering"
        ],
        "relationships": [
            {"entity": "Three-point seat belt", "relationship": "INVENTED_AND_FREELY_LICENSED", "note": "Nils Bohlin's three-point belt (1959) — invented at Volvo and freely licensed to all manufacturers — saved over 1 million lives"},
            {"entity": "Geely Automobile Holdings", "relationship": "VOLVO_CARS_ACQUIRED_BY", "note": "Geely (China) acquired Volvo Cars from Ford (2010) — while AB Volvo retained trucks, buses, and construction equipment"},
            {"entity": "Gothenburg, Sweden", "relationship": "FOUNDED_AND_HEADQUARTERED_IN", "note": "Volvo was founded in Gothenburg (1927) and remains headquartered there — a defining institution of Swedish industrial culture"},
            {"entity": "Renault Trucks", "relationship": "ACQUIRED", "note": "AB Volvo acquired Renault Trucks (2001) — making it the world's second-largest heavy truck manufacturer"},
            {"entity": "Global automotive safety standards", "relationship": "PIONEERED", "note": "Volvo's safety-first philosophy and freely licensed innovations set the standard for global automotive safety regulation"}
        ],
    }),

    ("alibaba-group", {
        "summary": (
            "Alibaba Group Holding Limited is a Chinese multinational technology and e-commerce conglomerate — the most consequential company in the history of Chinese capitalism and one of the world's largest corporations by market capitalisation. Founded in Hangzhou in 1999 by Jack Ma (Ma Yun) — a former English teacher who could not get a job at KFC — with 17 co-founders and ¥500,000 in seed capital, Alibaba built China's dominant e-commerce platforms (Alibaba.com B2B, Taobao consumer marketplace, Tmall premium retail), payment system (Alipay/Ant Financial), cloud computing (Alibaba Cloud), and logistics network (Cainiao).\n\n"
            "Alibaba's IPO on the New York Stock Exchange in September 2014 raised $25 billion — the largest IPO in history at the time — valuing the company at $231 billion and making Jack Ma China's richest man. The company subsequently diversified into cloud computing, digital media, and Southeast Asian markets. At its peak (2020), Alibaba had a market capitalisation of $850 billion. The company's ecosystem — connecting 1+ billion consumers, 10+ million merchants, and 100,000+ enterprises — is the most comprehensive digital commercial infrastructure in human history.\n\n"
            "The Chinese government's regulatory crackdown (2020–2021) — triggered partly by Jack Ma's public criticism of Chinese financial regulation — resulted in the cancellation of Ant Financial's $37 billion IPO (the world's largest planned IPO) and a $2.8 billion antitrust fine for Alibaba. Ma largely disappeared from public view. The episode illustrated both Alibaba's enormous commercial power and the ultimate limits of private business autonomy under the Chinese Communist Party."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Chinese technology conglomerate (est. 1999) — the most consequential company in Chinese capitalism history; 2014 NYSE IPO raised $25 billion (then-largest in history); connects 1 billion+ consumers; regulatory crackdown (2020–21) illustrated the limits of private business autonomy under CCP.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "China's rapid internet adoption in the late 1990s — combined with the underdevelopment of China's retail infrastructure and the absence of established consumer brands — created the market opportunity that Alibaba's e-commerce platforms captured",
            "Jack Ma's vision of connecting Chinese small and medium businesses to global buyers — through Alibaba.com's B2B platform — addressed the real inefficiency of China's fragmented manufacturing sector's access to international markets",
            "China's extraordinary economic growth (1990s–2000s) — creating hundreds of millions of new consumers and entrepreneurs — provided the demand base for Alibaba's platforms, while government support for domestic internet champions provided regulatory protection from foreign competition"
        ],
        "effects": [
            "Alibaba's 2014 IPO ($25 billion raised) validated China's technology sector as a global investment destination and marked the moment when Chinese technology companies became significant actors in global capital markets",
            "Alipay/Ant Financial's development of mobile payment infrastructure — reaching 1 billion users — made China the world's most cashless economy and pioneered the fintech revolution that has since spread globally",
            "Alibaba Cloud's growth made it Asia's largest and the world's fourth-largest cloud computing provider — competing with AWS, Azure, and Google Cloud — while providing the digital infrastructure for China's digital economy",
            "The CCP's regulatory crackdown on Alibaba (2020–2021) — cancelling Ant Financial's IPO, fining Alibaba $2.8 billion, and enforcing 'common prosperity' regulations — demonstrated that China's largest private companies operate within strict party-state constraints"
        ],
        "relationships": [
            {"entity": "Jack Ma (Ma Yun)", "relationship": "FOUNDED_BY", "note": "Jack Ma co-founded Alibaba (1999) — transforming himself from an English teacher to China's richest man and one of the most influential entrepreneurs in history"},
            {"entity": "Ant Financial (Alipay)", "relationship": "CREATED_DIGITAL_PAYMENT_ECOSYSTEM_THROUGH", "note": "Ant Financial/Alipay — Alibaba's payment affiliate — became China's dominant mobile payment system with 1 billion users"},
            {"entity": "New York Stock Exchange IPO (2014)", "relationship": "COMPLETED_RECORD_IPO_ON", "note": "Alibaba's 2014 NYSE IPO raised $25 billion — the largest IPO in history at the time"},
            {"entity": "Chinese Communist Party", "relationship": "REGULATORY_AUTHORITY_OF_CRACKED_DOWN_BY", "note": "The CCP's crackdown (2020–21) — cancelling Ant's IPO and fining Alibaba $2.8 billion — illustrated the limits of private business autonomy in China"},
            {"entity": "Alibaba Cloud", "relationship": "OPERATES", "note": "Alibaba Cloud is Asia's largest cloud computing provider — a key component of China's digital infrastructure"}
        ],
    }),

    ("apple-inc", {
        "summary": (
            "Apple Inc. is an American multinational technology company — the world's most valuable company by market capitalisation and one of the most consequential corporations in history. Founded in a garage in Los Altos, California in 1976 by Steve Jobs, Steve Wozniak, and Ronald Wayne, Apple pioneered personal computing with the Apple II (1977) and the Macintosh (1984) — the first mass-market computer with a graphical user interface. After near-bankruptcy in 1997, Steve Jobs's return and the iPod (2001), iTunes Store (2003), iPhone (2007), and App Store (2008) transformed Apple into the dominant force in consumer technology.\n\n"
            "The iPhone (2007) was the most consequential product launch in the history of consumer electronics — a device that combined a mobile phone, a music player, and an internet communicator in a touchscreen design that redefined human-computer interaction. The App Store (2008) created the modern app economy — now generating $1 trillion+ annually for app developers globally. Apple's transition to Apple Silicon (M1/M2 chips, 2020–) demonstrated that consumer-brand chip design could surpass Intel's decades of dominance.\n\n"
            "Apple became the first US company to reach a $1 trillion market capitalisation (2018) and subsequently $2 trillion (2020) and $3 trillion (2023). Its supply chain — centred on Foxconn's Chinese manufacturing — makes it the most powerful actor in global electronics manufacturing. Apple's privacy-focused brand positioning, its control of the iOS ecosystem, and its services revenue ($80+ billion annually) make it simultaneously a hardware company, a software platform, a media distribution company, and a financial services provider."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's most valuable company by market cap; the iPhone (2007) redefined human-computer interaction; the App Store (2008) created a $1 trillion+ app economy; first company to reach $1T (2018), $2T (2020), and $3T (2023) market cap; pioneered the PC revolution with the Apple II and Macintosh.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Steve Wozniak's engineering genius — designing the Apple II's architecture as a genuinely open, programmable computer accessible to hobbyists — and Steve Jobs's marketing vision created the product combination that launched the personal computing era",
            "The Macintosh's (1984) commercial development of Xerox PARC's graphical user interface research — the mouse, icons, windows — made computing accessible to non-technical users for the first time, creating the mass market for personal computers",
            "Steve Jobs's return (1997) and his focus on radical product simplification — eliminating the confusion of Apple's product line to focus on 4 products — created the conditions for the iPod-iTunes-iPhone sequence that redefined Apple as a consumer electronics company"
        ],
        "effects": [
            "The iPhone (2007) redefined human-computer interaction for billions of people — creating the smartphone era, the mobile internet economy, and the app ecosystem that has generated $1 trillion+ annually for app developers globally",
            "The App Store's (2008) 30% commission model — now contested by Epic, Spotify, and regulators globally — created the dominant distribution model for software, giving Apple extraordinary control over the most commercially valuable software distribution platform",
            "Apple's supply chain — with Foxconn as primary manufacturer — made China the global centre of consumer electronics manufacturing, shaping US-China trade relations and creating the geopolitical vulnerabilities exposed by the US-China technology competition",
            "Apple Silicon (M1/M2 chips, 2020–) demonstrated that consumer brand in-house chip design could surpass Intel's decades of x86 dominance — triggering a broader shift toward custom silicon across the technology industry"
        ],
        "relationships": [
            {"entity": "Steve Jobs", "relationship": "CO-FOUNDED_BY_AND_PRODUCT_VISION_DRIVEN_BY", "note": "Steve Jobs co-founded Apple (1976) and returned (1997) to drive the iPod-iPhone-iPad product sequence that made it the world's most valuable company"},
            {"entity": "iPhone (2007)", "relationship": "CREATED_MOST_CONSEQUENTIAL_CONSUMER_PRODUCT", "note": "The iPhone (2007) — combining phone, music player, and internet communicator in a touchscreen device — redefined consumer electronics and created the smartphone era"},
            {"entity": "App Store (2008)", "relationship": "LAUNCHED", "note": "The App Store (2008) created the modern app economy — now generating $1 trillion+ annually for developers globally"},
            {"entity": "Foxconn", "relationship": "PRIMARY_MANUFACTURING_PARTNER", "note": "Foxconn's Chinese manufacturing facilities produce the majority of Apple's hardware — making Apple the most powerful actor in global electronics manufacturing"},
            {"entity": "Macintosh (1984)", "relationship": "DEMOCRATISED_COMPUTING_THROUGH", "note": "The Macintosh (1984) made the graphical user interface — developed at Xerox PARC — accessible to mass-market consumers for the first time"}
        ],
    }),

    ("amazon-com", {
        "summary": (
            "Amazon.com, Inc. is an American multinational technology and e-commerce conglomerate — the world's largest online retailer and the dominant force in cloud computing through Amazon Web Services (AWS). Founded by Jeff Bezos in his garage in Bellevue, Washington in 1994 — initially as an online bookstore — Amazon expanded through Bezos's 'flywheel' strategy to become the world's most comprehensive consumer marketplace, the largest cloud infrastructure provider, and a significant force in streaming media, logistics, healthcare, and artificial intelligence.\n\n"
            "Amazon Web Services (AWS), launched in 2006, was the foundational innovation of the cloud computing era — enabling businesses to rent computing infrastructure at scale rather than purchasing their own servers. AWS generates approximately $90 billion in annual revenue (2023) and operates at margins far higher than Amazon's retail business — it is the most profitable cloud platform in the world and the infrastructure on which thousands of the most significant digital businesses (Netflix, Airbnb, NASA) depend.\n\n"
            "Amazon's transformation of retail — through 2-day Prime delivery, third-party marketplace, and Alexa voice interface — has fundamentally disrupted brick-and-mortar retail globally, contributing to the closure of tens of thousands of retail stores. Amazon's treatment of warehouse workers — characterised by intense productivity monitoring, high injury rates, and union suppression — has made it the most contested company in the debate about the future of work in the digital economy."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's largest online retailer; AWS (launched 2006) created cloud computing and underpins thousands of major digital businesses; Prime delivery transformed retail; Bezos's 'flywheel' strategy is the most influential business model of the digital era; Amazon disrupted global retail and created the cloud computing industry.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Jeff Bezos's identification of books as the ideal first product for online retail — infinite variety, standardised format, no need to physically inspect before purchase — gave Amazon the perfect initial market to test and develop its e-commerce capabilities",
            "Bezos's 'flywheel' strategy — using lower prices to attract customers, driving traffic to attract third-party sellers, expanding product selection to lower prices further, creating a self-reinforcing cycle — provided the theoretical framework for Amazon's expansion across categories",
            "The emergence of broadband internet (late 1990s) and the smartphone (2007) created the consumer infrastructure for mass e-commerce adoption that Amazon was positioned to capture"
        ],
        "effects": [
            "Amazon Web Services (AWS, 2006) created the cloud computing industry — enabling the digital economy's exponential growth by allowing businesses of any size to access enterprise-grade computing infrastructure without capital investment",
            "Amazon's retail disruption — two-day Prime delivery, infinite selection, competitive pricing — accelerated the decline of brick-and-mortar retail, contributing to the closure of tens of thousands of retail stores and the 'retail apocalypse' of the 2010s",
            "Jeff Bezos became the world's richest person (2017–2021) — Amazon's success concentrated wealth to a degree unprecedented in corporate history, making Amazon central to the debate about wealth inequality in the digital economy",
            "Alexa (Amazon Echo, 2014) pioneered the voice interface as a consumer product — launching the smart speaker category and demonstrating that conversational AI could be integrated into everyday domestic life"
        ],
        "relationships": [
            {"entity": "Jeff Bezos", "relationship": "FOUNDED_BY", "note": "Jeff Bezos founded Amazon (1994) in his garage — building it from an online bookstore to the world's most comprehensive consumer marketplace"},
            {"entity": "Amazon Web Services (AWS)", "relationship": "OPERATES", "note": "AWS (2006) created the cloud computing industry — underpinning thousands of major digital businesses and generating $90B+ annually"},
            {"entity": "Amazon Prime", "relationship": "TRANSFORMED_CONSUMER_EXPECTATIONS_WITH", "note": "Amazon Prime's 2-day delivery guarantee transformed consumer expectations of retail — driving mass adoption of e-commerce"},
            {"entity": "US retail industry", "relationship": "DISRUPTED", "note": "Amazon's retail dominance contributed to the closure of tens of thousands of brick-and-mortar stores — the 'retail apocalypse' of the 2010s"},
            {"entity": "Cloud computing industry", "relationship": "CREATED_WITH_AWS", "note": "AWS (2006) created the cloud computing industry — the foundational infrastructure of the modern digital economy"}
        ],
    }),

    ("alphabet-inc", {
        "summary": (
            "Alphabet Inc. is an American multinational technology conglomerate — the parent company of Google, YouTube, Waymo, DeepMind, and other ventures — and one of the world's most valuable corporations. Founded as Google in a Stanford University dorm room in 1998 by Larry Page and Sergey Brin, the company's PageRank algorithm for web search transformed how humanity accesses information. Alphabet was created in 2015 as a holding company restructuring to separate Google's core businesses from more speculative ventures (Waymo, Verily, etc.). Google Search processes 8.5 billion queries daily — approximately one search per person on earth.\n\n"
            "Google's dominance in search (92% global market share), digital advertising, mobile operating systems (Android, 72% of smartphones), and email (Gmail, 1.8 billion users) makes Alphabet the most powerful information intermediary in human history. Google Ads generates $200+ billion annually — capturing approximately 25% of all global advertising spending — by targeting advertisements based on search intent and behavioural data. This advertising model has fundamentally disrupted traditional print and broadcast media globally.\n\n"
            "DeepMind (acquired 2014) and Google Brain have produced landmark AI breakthroughs — AlphaGo (2016, first AI to defeat a world Go champion), AlphaFold (2020, protein structure prediction), and contributions to large language models — making Alphabet the dominant force in fundamental AI research. The company faces antitrust actions in the US, EU, and multiple jurisdictions for search monopoly and advertising practices."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Parent of Google — the world's most used search engine (8.5 billion queries/day, 92% market share); Android powers 72% of smartphones; Google Ads captures 25% of global advertising; DeepMind produced AlphaGo and AlphaFold; Alphabet is the most powerful information intermediary in human history.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Larry Page and Sergey Brin's PageRank algorithm — ranking web pages by the quality of links pointing to them rather than just keyword density — produced dramatically superior search results compared to existing engines, creating the user adoption that made Google dominant",
            "The explosion of web content in the late 1990s created an information retrieval problem of unprecedented scale — which Google's superior algorithm solved at precisely the moment of maximum demand",
            "Google's AdWords advertising model (2000) — charging advertisers per click rather than per impression, targeting ads to search intent — created the most efficient advertising system in history and the economic foundation for Alphabet's $2 trillion valuation"
        ],
        "effects": [
            "Google Search's 92% global market share means that Alphabet effectively controls humanity's primary information gateway — what appears (or does not appear) in search results shapes what information billions of people access, with profound consequences for democracy, commerce, and culture",
            "Android's 72% smartphone market share made Google's operating system the dominant platform of the mobile internet era — giving Alphabet unprecedented data collection capabilities and making it the primary intermediary between mobile users and the internet",
            "Google's advertising disruption — capturing 25% of global advertising spending — devastated traditional print and broadcast media, contributing to the collapse of newspaper advertising revenue and the resulting crisis of journalism globally",
            "DeepMind's AlphaFold (2020) — predicting protein structures with near-atomic accuracy — is potentially the most consequential scientific achievement of the 21st century, accelerating drug discovery and potentially enabling treatments for diseases from Alzheimer's to cancer"
        ],
        "relationships": [
            {"entity": "Google Search", "relationship": "OPERATES", "note": "Google Search (8.5B queries/day, 92% market share) is Alphabet's foundational product — the world's primary information gateway"},
            {"entity": "Larry Page", "relationship": "CO-FOUNDED_GOOGLE_BY", "note": "Larry Page (with Sergey Brin) co-founded Google (1998) — his PageRank algorithm created the superior search engine that became humanity's information gateway"},
            {"entity": "DeepMind", "relationship": "ACQUIRED_AND_OPERATES", "note": "DeepMind (acquired 2014) produced AlphaGo (2016) and AlphaFold (2020) — making Alphabet the dominant force in fundamental AI research"},
            {"entity": "Android operating system", "relationship": "OPERATES", "note": "Android (72% of smartphones) is Alphabet's mobile platform — giving it unprecedented data collection capabilities and mobile advertising dominance"},
            {"entity": "YouTube", "relationship": "ACQUIRED_AND_OPERATES", "note": "YouTube (acquired 2006) is the world's most used video platform — generating $30B+ annually and shaping global media culture"}
        ],
    }),

    ("microsoft-corporation", {
        "summary": (
            "Microsoft Corporation is an American multinational technology company — co-founded by Bill Gates and Paul Allen in Albuquerque, New Mexico in 1975 — that created the software layer of the personal computing revolution and subsequently became the world's most valuable company (as of 2024) through its dominance of enterprise software, cloud computing (Azure), and strategic AI investments. The company's founding insight — that software (operating systems) would be more valuable than hardware — was realised through the MS-DOS/Windows monopoly that made Microsoft the dominant force in personal computing for three decades.\n\n"
            "Windows (launched 1985, mass adoption with Windows 95 in 1995) became the operating system on 90%+ of personal computers globally — making it the most widely used software in history. Microsoft Office (Word, Excel, PowerPoint) created and dominated the productivity software category. The Microsoft antitrust case (US v. Microsoft, 2000) — finding that Microsoft had illegally maintained its operating system monopoly — was the most significant antitrust action in the technology industry until the Google and Apple cases two decades later.\n\n"
            "Under CEO Satya Nadella (from 2014), Microsoft transformed itself from a declining Windows-centric company to a cloud and AI powerhouse: Azure became the world's second-largest cloud platform, and Microsoft's $1 billion investment in OpenAI (2019) — expanded to $13 billion by 2023 — positioned it at the centre of the generative AI revolution. Microsoft Copilot (integrating GPT-4 into Office, Windows, and GitHub) is the most significant deployment of generative AI in enterprise software history."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Co-founded by Bill Gates (1975); Windows created the PC software monopoly; world's most valuable company (2024); $13B investment in OpenAI positions Microsoft at the centre of the generative AI revolution; Azure is the world's 2nd-largest cloud platform; Microsoft Office defined productivity software for 30 years.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Bill Gates's insight that IBM's decision to outsource the operating system for the IBM PC (1981) to Microsoft — which Gates had acquired from Tim Paterson for $50,000 — gave Microsoft the leverage to retain OS licensing rights that would create one of the most lucrative monopolies in business history",
            "The network effects of Windows — the more software was written for Windows, the more valuable Windows became to users; the more users ran Windows, the more software was written for it — created a self-reinforcing dominance that competitors could not break for three decades",
            "Satya Nadella's 'mobile-first, cloud-first' pivot (2014) — abandoning Microsoft's failed consumer hardware strategy to focus on Azure cloud and enterprise services — enabled Microsoft's transformation from a declining Windows company to a cloud and AI leader"
        ],
        "effects": [
            "Windows's dominance of personal computing (90%+ market share) made Microsoft the dominant software monopoly of the PC era — generating the profits that funded its research in databases, office software, server systems, and eventually cloud computing and AI",
            "Microsoft Office's spreadsheet (Excel), word processor (Word), and presentation software (PowerPoint) created the standard tools of global business communication — used by 1+ billion people — and became the default productivity software of the modern economy",
            "Microsoft's $13 billion investment in OpenAI and the integration of GPT-4 into Microsoft Copilot (2023) positioned Microsoft at the centre of the generative AI revolution — the most significant technology transformation since the smartphone",
            "The US v. Microsoft antitrust case (2000) — finding illegal monopoly maintenance — was the most significant technology antitrust action of the 20th century and established the legal precedents applied to Google, Apple, and Amazon in subsequent decades"
        ],
        "relationships": [
            {"entity": "Bill Gates", "relationship": "CO-FOUNDED_BY", "note": "Bill Gates (with Paul Allen) co-founded Microsoft (1975) — his acquisition of MS-DOS from Tim Paterson and retention of OS licensing rights created one of business history's most consequential deals"},
            {"entity": "Windows operating system", "relationship": "OPERATES", "note": "Windows — 90%+ global PC market share — was Microsoft's core monopoly and the dominant software of the personal computing era"},
            {"entity": "OpenAI", "relationship": "INVESTED_$13_BILLION_IN", "note": "Microsoft's $13B investment in OpenAI (2019–2023) positioned it at the centre of the generative AI revolution"},
            {"entity": "Microsoft Azure", "relationship": "OPERATES", "note": "Azure — world's second-largest cloud platform — is Microsoft's primary growth engine under Satya Nadella"},
            {"entity": "US v. Microsoft antitrust case (2000)", "relationship": "SUBJECT_OF_FOUNDATIONAL_ANTITRUST_ACTION", "note": "The US v. Microsoft case (2000) found illegal monopoly maintenance — the most significant technology antitrust action of the 20th century"}
        ],
    }),

    ("samsung-electronics", {
        "summary": (
            "Samsung Electronics Co., Ltd. is a South Korean multinational electronics company — a subsidiary of Samsung Group and the world's largest manufacturer of consumer electronics, semiconductors, and smartphone displays. Founded in 1969 (Samsung Group was founded in 1938 by Lee Byung-chul), Samsung Electronics is South Korea's most important company and the country's largest exporter, accounting for approximately 20% of South Korean exports. Samsung's trajectory — from a crude black-and-white television manufacturer to the world's largest smartphone manufacturer and semiconductor company — is the most dramatic corporate ascent in the history of industrial capitalism.\n\n"
            "Samsung became the world's largest smartphone manufacturer in 2012, surpassing Nokia and Apple — a position it has largely maintained. Its Galaxy smartphone series competes directly with Apple's iPhone globally. Samsung's semiconductor division — producing DRAM memory chips and NAND flash storage — makes it the world's largest semiconductor company by revenue, supplying chips to Apple, Qualcomm, NVIDIA, and other technology companies. Samsung Display is the dominant manufacturer of OLED screens, supplying displays to Apple's iPhone and other premium smartphones.\n\n"
            "Samsung's extraordinary industrial success is inseparable from South Korea's state-directed industrial development: the chaebol system — under which family-controlled conglomerates like Samsung received preferential government treatment — enabled Samsung's rapid scaling. Samsung's Lee family has faced repeated corruption convictions (most recently Lee Jae-yong in 2021) for payments to politicians — illustrating the systemic corruption embedded in the chaebol model."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "World's largest consumer electronics, semiconductor, and smartphone display manufacturer; South Korea's largest exporter (20% of exports); most dramatic corporate ascent in industrial history; world's largest semiconductor company; Samsung's success embodies South Korea's chaebol-led development model.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "South Korea's chaebol-led development model — state-directed capital allocation, preferential treatment, and export-focused industrial policy — gave Samsung the financial resources and market protection to achieve scale in capital-intensive semiconductor and display manufacturing",
            "Samsung's strategic 'fast follower' approach — rapidly improving on innovations pioneered by others through massive manufacturing investment and cost reduction — enabled it to dominate industries (memory chips, flat panels, smartphones) through manufacturing excellence rather than original invention",
            "The explosive growth of global consumer electronics demand (1980s–2010s) — personal computers, mobile phones, flat-screen TVs, smartphones — created the market that Samsung's vertically integrated manufacturing was perfectly positioned to capture"
        ],
        "effects": [
            "Samsung's dominance of global semiconductor manufacturing — particularly DRAM memory and NAND flash — makes it a critical supplier for every major technology company, creating geopolitical importance: Samsung's fabs in South Korea are strategically critical assets in the US-China technology competition",
            "Samsung's smartphone manufacturing — producing 300+ million units annually — made it the dominant global smartphone brand outside China, shaping consumer expectations and the competitive dynamics of the entire global smartphone market",
            "The Korean Wave (Hallyu) — the global spread of South Korean popular culture — was facilitated by Samsung's (and LG's) global brand presence, making Samsung both a beneficiary of and a contributor to South Korea's cultural diplomacy",
            "Samsung's repeated corruption convictions — the Lee family's payments to politicians in exchange for government support — are the most visible manifestation of the systemic corruption embedded in the chaebol model, influencing South Korea's ongoing debate about corporate governance reform"
        ],
        "relationships": [
            {"entity": "Lee Byung-chul", "relationship": "SAMSUNG_GROUP_FOUNDED_BY", "note": "Lee Byung-chul founded Samsung Group (1938) — the conglomerate that Samsung Electronics belongs to"},
            {"entity": "South Korean chaebol system", "relationship": "MOST_POWERFUL_EXAMPLE_OF", "note": "Samsung is the most powerful chaebol — the state-supported family conglomerate model that drove South Korea's industrial development"},
            {"entity": "Apple Inc.", "relationship": "SIMULTANEOUSLY_SUPPLIER_TO_AND_COMPETITOR_OF", "note": "Samsung supplies OLED displays and memory chips to Apple's iPhone while competing with it globally through the Galaxy line — the most complex supplier-competitor relationship in technology"},
            {"entity": "Global semiconductor industry", "relationship": "DOMINANT_MANUFACTURER_IN", "note": "Samsung is the world's largest semiconductor company — making it a critical supplier for the entire global technology industry"},
            {"entity": "South Korean economy", "relationship": "LARGEST_EXPORTER_OF", "note": "Samsung Electronics accounts for approximately 20% of South Korean exports — making it economically indispensable to the country"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 09 — {len(ENTITIES)} entities (Class 330: Major Corporations)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
