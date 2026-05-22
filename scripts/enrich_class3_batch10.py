#!/usr/bin/env python3
"""
Batch 10 — 8 entities (Class 330): Major Corporations (continued)
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

    ("boeing", {
        "summary": (
            "The Boeing Company is an American multinational aerospace and defence corporation — the world's largest aerospace company by revenue for much of its history — and one of the defining industrial enterprises of the 20th century. Founded in Seattle, Washington in 1916 by William E. Boeing, the company built its reputation through landmark aircraft: the B-17 Flying Fortress (WWII strategic bomber), the B-52 Stratofortress (the backbone of US nuclear deterrence since 1952), the 707 (the aircraft that inaugurated the jet age of commercial aviation, 1958), and the 747 'Jumbo Jet' (1969), which democratised mass air travel.\n\n"
            "The Boeing 747 (1969) was arguably the most consequential commercial aircraft in history: its 400-passenger capacity and intercontinental range made mass tourism economically viable, transforming global travel, trade, and cultural exchange. Boeing's commercial aircraft division — producing the 737, 747, 767, 777, and 787 families — competed with Airbus in a global duopoly that controlled virtually all commercial aircraft manufacturing for large passenger planes from the 1970s onward.\n\n"
            "Boeing's 737 MAX crisis (2018–2020) — following two crashes (Lion Air, October 2018; Ethiopian Airlines, March 2019) that killed 346 people, caused by the MCAS flight control software — is the most consequential aircraft safety scandal in aviation history. The 20-month grounding cost Boeing $20 billion and exposed systematic failures in Boeing's safety culture following its 1997 merger with McDonnell Douglas. It reshaped global aviation safety regulation and triggered deep scrutiny of the FAA's regulatory relationship with Boeing."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "World's largest aerospace company for most of its history; the 707 inaugurated jet age (1958); the 747 democratised mass air travel (1969); the 737 MAX crashes (2018–19, 346 dead) are aviation history's most consequential safety scandal; backbone of US military aviation from WWII to present.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "William Boeing's vision — combining a passion for flight with Seattle's timber industry wealth — created the financial foundation and manufacturing expertise for what became the world's most important aerospace company",
            "WWII government contracts — particularly the B-17 Flying Fortress and B-29 Superfortress — gave Boeing the scale, manufacturing capacity, and engineering expertise to dominate post-war commercial aviation",
            "The US government's investment in jet propulsion technology during the Cold War (B-52 programme) gave Boeing the jet engine experience that enabled the 707's commercial development — the first successful US commercial jet airliner"
        ],
        "effects": [
            "The Boeing 747 (1969) democratised international air travel — its 400-passenger capacity and range lowered ticket prices sufficiently to make intercontinental travel accessible to the middle class, transforming global tourism, immigration, and cultural exchange",
            "Boeing's commercial aircraft duopoly with Airbus — controlling virtually all large commercial aircraft manufacturing — means that Boeing's production decisions affect the economic viability of airlines, tourism industries, and air freight globally",
            "The 737 MAX crisis (2018–2020) — 346 deaths, 20-month global grounding, $20B cost — exposed systematic failures in Boeing's safety culture and the FAA's regulatory capture, triggering the most significant reform of aviation safety regulation since the crash of ValuJet 592 (1996)",
            "Boeing's defence division — producing the B-52 (still in service 70+ years after introduction), AH-64 Apache helicopter, and F-15 fighter — has been the backbone of US military aviation, making it central to US national security for eight decades"
        ],
        "relationships": [
            {"entity": "Boeing 747", "relationship": "DESIGNED_AND_MANUFACTURED", "note": "The 747 (1969) — Boeing's most consequential commercial aircraft — democratised mass air travel by making intercontinental flights economically accessible to the middle class"},
            {"entity": "737 MAX crisis (2018–2020)", "relationship": "CAUSED_BY_SAFETY_FAILURES_OF", "note": "The 737 MAX crashes (346 dead, 20-month grounding) exposed systematic safety culture failures at Boeing and the FAA"},
            {"entity": "Airbus", "relationship": "GLOBAL_COMMERCIAL_AIRCRAFT_DUOPOLY_WITH", "note": "Boeing and Airbus control virtually all large commercial aircraft manufacturing — a global duopoly that shapes the economics of global aviation"},
            {"entity": "US military aviation", "relationship": "BACKBONE_MANUFACTURER_OF", "note": "Boeing's defence division — B-52, AH-64 Apache, F-15 — has been central to US military aviation for eight decades"},
            {"entity": "Global commercial aviation industry", "relationship": "FOUNDATIONAL_MANUFACTURER_OF", "note": "Boeing's 707, 747, 777, and 787 aircraft defined successive eras of commercial aviation — shaping the global tourism and freight economy"}
        ],
    }),

    ("bp", {
        "summary": (
            "BP plc (originally British Petroleum; formerly Anglo-Persian Oil Company, 1909) is a British multinational oil and gas company — one of the world's six largest oil companies ('supermajors') and a defining institution of 20th-century petroleum capitalism. Founded as the Anglo-Persian Oil Company following William Knox D'Arcy's discovery of oil in Persia (Iran) in 1908 — the first major oil strike in the Middle East — BP's history is inseparable from the political history of the Middle East, British imperialism, and the global energy system.\n\n"
            "BP's history includes landmark moments in oil company power and controversy: the 1953 Iranian coup (Operation Ajax/Boot) — organised by the CIA and MI6 partly in response to Iran's nationalisation of the Anglo-Iranian Oil Company under Prime Minister Mohammad Mosaddegh — restored the Shah to power and returned oil revenues to Western companies. The 1970 Libyan nationalisation, the 1973 Arab oil embargo, and the 1979 Iranian Revolution progressively eroded Western oil company control of Middle Eastern reserves.\n\n"
            "The Deepwater Horizon oil spill (April 2010) — caused by BP's offshore drilling operation in the Gulf of Mexico — released 4.9 million barrels of crude oil over 87 days, the largest marine oil spill in history, causing catastrophic environmental damage to the Gulf Coast ecosystem and costing BP $65 billion in cleanup costs, fines, and legal settlements. The disaster reshaped global offshore drilling regulation and made BP the most scrutinised example of corporate environmental responsibility failure."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "British oil supermajor; Anglo-Persian Oil Company (founded 1909) made the first Middle Eastern oil strike; 1953 Iranian coup (CIA/MI6 partly protecting BP's interests); Deepwater Horizon (2010) — largest marine oil spill in history, $65B cost — is the defining corporate environmental disaster of the 21st century.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "William Knox D'Arcy's oil concession from the Persian Shah (1901) and his discovery of oil at Masjed Soleiman (1908) created the foundation of Middle Eastern petroleum production — which the Anglo-Persian Oil Company (BP's predecessor) was positioned to exploit",
            "The British government's 51% acquisition of the Anglo-Persian Oil Company (1914, on Winston Churchill's recommendation) — to secure fuel oil for the Royal Navy's conversion from coal — made BP both a commercial enterprise and a strategic national asset",
            "The post-WWII global demand for petroleum — fuelling the automobile era, the petrochemical industry, and post-war economic growth — created the market conditions in which BP's Middle Eastern oil reserves generated enormous wealth"
        ],
        "effects": [
            "The 1953 Iranian coup (Operation Ajax) — in which the CIA and MI6, acting partly to protect the Anglo-Iranian Oil Company's nationalised assets, overthrew democratically elected PM Mosaddegh — is the paradigmatic case of Western oil company interests shaping Middle Eastern political history",
            "BP's progressive loss of Middle Eastern oil reserves (1973–1979) — through nationalisation and the Iranian Revolution — forced its transformation from a Middle Eastern oil producer to a global exploration company, pioneering North Sea oil (Forties field, 1970) and Alaskan oil (Prudhoe Bay, 1969)",
            "The Deepwater Horizon disaster (2010) — 4.9 million barrels, $65 billion cost — is the defining corporate environmental disaster of the 21st century, triggering the most comprehensive offshore drilling regulatory reform in US history",
            "BP's 'Beyond Petroleum' rebranding (2000) — committing to diversification into solar and wind energy — was one of the earliest major oil company acknowledgements of climate change, though critics argued it was primarily a PR exercise without substantive strategic change"
        ],
        "relationships": [
            {"entity": "Anglo-Persian Oil Company (1909)", "relationship": "EVOLVED_FROM", "note": "BP evolved from the Anglo-Persian Oil Company (1909) — founded after D'Arcy's discovery of oil at Masjed Soleiman"},
            {"entity": "1953 Iranian coup (Operation Ajax)", "relationship": "INTERESTS_CONTRIBUTED_TO", "note": "The CIA/MI6 coup that overthrew Mosaddegh (1953) was partly motivated by protecting Anglo-Iranian Oil Company's nationalised assets — illustrating oil company power in Cold War geopolitics"},
            {"entity": "Deepwater Horizon oil spill (2010)", "relationship": "RESPONSIBLE_FOR", "note": "BP's Deepwater Horizon platform caused the largest marine oil spill in history (4.9M barrels, $65B cost) — the defining corporate environmental disaster of the 21st century"},
            {"entity": "North Sea oil industry", "relationship": "PIONEERED", "note": "BP's Forties field (1970) pioneered North Sea oil production — offsetting the loss of Middle Eastern reserves"},
            {"entity": "Iranian nationalisation of oil (1951)", "relationship": "ASSETS_NATIONALISED_BY", "note": "Iran's 1951 nationalisation of Anglo-Iranian Oil Company's assets — and the subsequent coup restoring the Shah — is BP's most politically consequential moment"}
        ],
    }),

    ("toyota-motor-corporation", {
        "summary": (
            "Toyota Motor Corporation is a Japanese multinational automobile manufacturer — the world's largest automaker by production volume since 2012 (surpassing General Motors after 77 years of GM dominance) — and the company whose 'Toyota Production System' (TPS) revolutionised industrial manufacturing globally. Founded in 1937 by Kiichiro Toyoda as a spin-off of the Toyoda Automatic Loom Works, Toyota transformed Japanese manufacturing from post-WWII poverty to global industrial leadership within 30 years.\n\n"
            "The Toyota Production System — developed by Taiichi Ohno and Eiji Toyoda from the 1950s onward — invented lean manufacturing: just-in-time production (parts arrive exactly when needed, eliminating inventory), kaizen (continuous incremental improvement), and jidoka (automation with human intelligence to stop production at defects). TPS was adopted globally as 'lean manufacturing' and transformed industrial production across automotive, aerospace, healthcare, and service industries. It is arguably the most influential management system in industrial history.\n\n"
            "Toyota's Prius (1997) — the world's first mass-produced hybrid electric vehicle — pioneered the hybrid powertrain that became the dominant intermediate technology between conventional internal combustion and full electric vehicles. By 2023, Toyota had sold 20+ million hybrid vehicles globally. Toyota's conservative approach to battery electric vehicles (BEVs) — betting on hybrids and hydrogen fuel cells rather than BEVs — put it at odds with Tesla's disruption of the automobile industry and has become the central debate in the automotive industry's electric transition."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's largest automaker since 2012; Toyota Production System (lean manufacturing) is the most influential management system in industrial history; Prius (1997) was the first mass-produced hybrid; TPS transformed industrial production across automotive, aerospace, healthcare globally.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Kiichiro Toyoda's determination to build a Japanese automobile industry — following his 1929 study tour of US and European factories — created the enterprise that would eventually surpass its American competitors, demonstrating that industrial determination and systematic improvement could overcome late-starter disadvantage",
            "Japan's post-WWII resource scarcity — limited capital, limited space, limited materials — forced Toyota to develop manufacturing systems that eliminated waste, which paradoxically created the most efficient production system in industrial history",
            "Taiichi Ohno's visit to US supermarkets (1956) — observing how supermarkets restocked shelves exactly when products were consumed, pulling supply based on demand — inspired the just-in-time production pull system that became the core of TPS"
        ],
        "effects": [
            "The Toyota Production System / lean manufacturing — adopted globally across automotive, aerospace, healthcare, and service industries — is arguably the most influential management innovation since Frederick Taylor's scientific management, improving manufacturing efficiency worldwide",
            "Toyota's quality revolution — its vehicles' superior reliability compared to US and European competitors in the 1970s–1980s — led directly to the decline of the American 'Big Three' automakers and the rise of Japanese automotive dominance, reshaping the global automotive industry",
            "The Prius hybrid (1997) — the first commercially successful mass-produced hybrid vehicle — pioneered the hybrid powertrain that became the dominant intermediate technology globally and put Toyota 20 years ahead in electrification experience",
            "Toyota's global supply chain — particularly its dependence on Taiwanese TSMC chips (revealed by chip shortages in 2021) — exposed the vulnerabilities of just-in-time manufacturing to global supply chain disruptions, triggering a fundamental reassessment of lean manufacturing's risk profile"
        ],
        "relationships": [
            {"entity": "Toyota Production System (TPS)", "relationship": "INVENTED", "note": "TPS — invented by Taiichi Ohno and Eiji Toyoda — is the foundational management system of lean manufacturing, adopted globally across industries"},
            {"entity": "Toyota Prius", "relationship": "PIONEERED_HYBRID_MASS_MARKET_WITH", "note": "The Prius (1997) was the world's first mass-produced hybrid vehicle — Toyota sold 20+ million hybrids globally by 2023"},
            {"entity": "Global automobile industry", "relationship": "LARGEST_PRODUCER_IN", "note": "Toyota surpassed GM in 2012 as the world's largest automaker — ending 77 years of GM dominance"},
            {"entity": "Taiichi Ohno", "relationship": "MANUFACTURING_PHILOSOPHY_CREATED_BY", "note": "Taiichi Ohno developed TPS — lean manufacturing, just-in-time, kaizen — making Toyota's production system the most influential in industrial history"},
            {"entity": "Japanese automotive industry", "relationship": "FLAGSHIP_ENTERPRISE_OF", "note": "Toyota is Japan's most important industrial enterprise and the symbol of Japanese manufacturing excellence's defeat of American automotive dominance"}
        ],
    }),

    ("shell-plc", {
        "summary": (
            "Shell plc (formerly Royal Dutch Shell) is a British-Dutch multinational oil and gas company — one of the world's six oil 'supermajors' and consistently one of the two or three largest corporations by revenue globally. Formed in 1907 by the merger of Royal Dutch Petroleum and Shell Transport and Trading, Shell's history spans the full arc of the petroleum age — from early 20th-century Dutch East Indies oil to North Sea gas to Nigerian delta oil to liquefied natural gas (LNG) to 21st-century energy transition debates.\n\n"
            "Shell's operations in the Niger Delta (1950s–present) represent one of the most damaging corporate environmental records in history: 40 years of oil spills — estimated at 1.5 million tons of crude oil across the delta, more than 10 times the Exxon Valdez spill — devastated the ecological and economic livelihoods of the Ogoni, Ijaw, and other Niger Delta peoples. The execution of Ogoni activist Ken Saro-Wiwa (1995) — following his campaign against Shell's environmental damage — focused international attention on corporate accountability in resource extraction.\n\n"
            "The Dutch court's ruling (2021) ordering Shell to reduce its carbon emissions by 45% by 2030 — the first time a court ordered a company to reduce emissions to meet climate targets — was the most significant corporate climate liability ruling in history, establishing legal precedent for shareholder and civil society climate litigation against energy companies globally."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Oil supermajor; Niger Delta operations caused 1.5M tons of oil spills (10x Exxon Valdez) over 40 years; Ken Saro-Wiwa's 1995 execution focused global attention on corporate environmental accountability; 2021 Dutch court climate ruling — ordering 45% emissions reduction — is the most significant corporate climate liability case in history.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The 1907 merger of Royal Dutch Petroleum (with Indonesian oil reserves) and Shell Transport and Trading (with tanker fleet and marketing network) created an integrated oil major that combined production, transport, and distribution — establishing the vertical integration model that all major oil companies adopted",
            "Shell's discovery and development of major oil reserves in the Dutch East Indies, the Gulf of Mexico, the North Sea, and Nigeria gave it the diversified production portfolio that insulated it from any single national political risk",
            "The post-WWII global automobile and petrochemical boom created the demand for petroleum products that made Shell — with its global production, refining, and retail network — one of the world's most valuable companies for the second half of the 20th century"
        ],
        "effects": [
            "Shell's Niger Delta operations (1950s–present) — 40 years of oil spills estimated at 1.5 million tons, devastating the delta ecosystem — represent one of the most damaging corporate environmental records in history, and Ken Saro-Wiwa's execution (1995) made Shell the symbol of corporate impunity in resource extraction",
            "Shell's LNG (liquefied natural gas) technology development — pioneering LNG production and transport since the 1960s — created the global LNG industry that now supplies energy to Japan, South Korea, China, and Europe, making Shell foundational to global energy security",
            "The 2021 Dutch court ruling ordering Shell to reduce emissions by 45% by 2030 established the legal precedent that corporations can be ordered by courts to comply with climate commitments — triggering similar litigation against other energy companies globally",
            "Shell's 2021 restructuring — reincorporating as a UK company (Shell plc), dropping 'Royal Dutch' from its name — was partly driven by legal uncertainty created by the Dutch climate ruling, demonstrating how climate litigation is reshaping global energy company governance"
        ],
        "relationships": [
            {"entity": "Niger Delta oil spills", "relationship": "RESPONSIBLE_FOR_40_YEARS_OF", "note": "Shell's Niger Delta operations caused an estimated 1.5 million tons of oil spills over 40 years — one of the most damaging corporate environmental records in history"},
            {"entity": "Ken Saro-Wiwa", "relationship": "ENVIRONMENTAL_CAMPAIGN_AGAINST_PRECEDED_EXECUTION_OF", "note": "Ken Saro-Wiwa's campaign against Shell's Niger Delta environmental damage led to his execution (1995) — focusing international attention on corporate accountability"},
            {"entity": "2021 Dutch climate court ruling", "relationship": "SUBJECT_OF_LANDMARK_CLIMATE_LIABILITY_RULING", "note": "The Dutch court ordered Shell to cut emissions 45% by 2030 — the first court order requiring a company to meet climate targets, establishing global legal precedent"},
            {"entity": "Global LNG industry", "relationship": "PIONEERED", "note": "Shell's LNG technology development created the global LNG industry — now supplying energy to Japan, South Korea, China, and Europe"},
            {"entity": "Royal Dutch Petroleum", "relationship": "FORMED_BY_MERGER_WITH", "note": "Shell was formed by the 1907 merger of Royal Dutch Petroleum and Shell Transport and Trading"}
        ],
    }),

    ("volkswagen-group", {
        "summary": (
            "Volkswagen AG is a German multinational automobile manufacturer — Europe's largest automaker and the world's second-largest by production volume — whose corporate history encompasses the Nazi-era Beetle, the post-war German economic miracle, and the Dieselgate scandal (2015), the most significant corporate fraud in automotive history. Founded in 1937 by the Nazi German Labour Front to produce an affordable 'People's Car' (Volkswagen) designed by Ferdinand Porsche, the original Beetle became one of the most produced cars in history (21+ million units), while the post-war VW company became the symbol of West Germany's economic recovery.\n\n"
            "The Volkswagen Group today encompasses 12 automotive brands — Volkswagen, Audi, Porsche, SEAT, ŠKODA, Lamborghini, Bentley, Bugatti, Ducati, MAN, and others — making it the most diverse automotive conglomerate by brand prestige range. Its total annual production of 9+ million vehicles makes it consistently the world's first or second-largest automaker, competing with Toyota for global leadership.\n\n"
            "The 'Dieselgate' scandal (September 2015) — in which VW was found to have installed 'defeat device' software in 11 million diesel vehicles globally to cheat emissions tests, with actual emissions up to 40× the legal nitrogen oxide limit — is the most consequential corporate fraud in automotive history. The scandal cost VW $35+ billion in fines, settlements, and vehicle buybacks, destroyed its reputation for engineering integrity, and accelerated the global automotive industry's transition away from diesel toward electric vehicles."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Europe's largest automaker; Beetle was the post-war symbol of German economic recovery; Dieselgate (2015) — 11 million vehicles with defeat devices, 40× emissions, $35B cost — is the most consequential corporate fraud in automotive history and accelerated the global shift to electric vehicles.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Adolf Hitler's vision of a mass-market 'People's Car' — affordable German transportation for the working class — created the original Volkswagen project and the Wolfsburg factory, which Ferdinand Porsche designed the Beetle to serve",
            "The British Army's decision to restart Volkswagen production in the ruins of post-war Wolfsburg (1945) — despite British automobile industry opposition — saved the company and enabled it to become the engine of West Germany's Wirtschaftswunder",
            "VW's expansion into the premium segment — acquiring Audi (1965), SEAT, ŠKODA, Bentley, Lamborghini, and Porsche over the following decades — transformed it from a mass-market manufacturer to a multi-brand conglomerate spanning the entire automotive price range"
        ],
        "effects": [
            "The Volkswagen Beetle — 21+ million units produced between 1938 and 2003 — became one of the most produced and culturally significant cars in history, symbolising both German industrial capacity and the counterculture of the 1960s",
            "Dieselgate (2015) — the most consequential automotive fraud in history — cost VW $35+ billion, triggered criminal prosecutions of executives, and permanently damaged European diesel's reputation, accelerating the global transition from diesel to electric vehicles",
            "VW's post-Dieselgate electric vehicle commitment — pledging €35 billion in EV investment and planning to become the world's largest EV manufacturer — transformed the global automotive EV transition from a Tesla-led niche to a mainstream industry shift",
            "VW's Wolfsburg headquarters city — with 100,000+ VW employees in a city of 120,000 — makes it the most company-dependent major city in Europe, with VW's fortunes directly determining the economic and social trajectory of an entire urban community"
        ],
        "relationships": [
            {"entity": "Ferdinand Porsche", "relationship": "BEETLE_DESIGNED_BY", "note": "Ferdinand Porsche designed the original VW Beetle — creating both the People's Car and the Porsche sports car brand"},
            {"entity": "Dieselgate scandal (2015)", "relationship": "PERPETRATED", "note": "VW's defeat device fraud (11 million vehicles, 40× emissions, $35B cost) is the most consequential corporate fraud in automotive history"},
            {"entity": "West German Wirtschaftswunder", "relationship": "SYMBOL_AND_DRIVER_OF", "note": "Post-war VW's recovery and growth was the symbol of West Germany's economic miracle — demonstrating German industrial capacity's revival"},
            {"entity": "Global electric vehicle transition", "relationship": "ACCELERATED_BY_DIESELGATE_AND_COMMITMENT_OF", "note": "VW's Dieselgate damaged diesel's reputation and its subsequent €35B EV commitment accelerated the global automotive transition to electric vehicles"},
            {"entity": "Audi AG", "relationship": "OWNS", "note": "Audi — acquired by VW in 1965 — is VW Group's premium brand cornerstone, contributing the largest share of the group's profit margins"}
        ],
    }),

    ("general-electric", {
        "summary": (
            "General Electric Company (GE) is an American multinational conglomerate — one of the longest-running and most influential corporations in US history — founded in 1892 by the merger of Thomas Edison's Edison General Electric and Thomson-Houston Electric Company. For much of the 20th century, GE was simultaneously the world's leading manufacturer of electrical equipment, jet engines, medical imaging devices, power turbines, locomotives, and financial services — a level of diversification that made it the paradigmatic case study for both conglomerate management and, in its fall, the limits of conglomerate strategies.\n\n"
            "GE's influence on American business culture under CEO Jack Welch (1981–2001) was profound: Welch's management philosophy — '20-70-10' forced ranking (top 20% rewarded, bottom 10% fired annually), shareholder value maximisation, and aggressive acquisition — became the dominant US management orthodoxy of the 1980s–1990s. GE Capital (its financial arm) grew to provide 40%+ of GE's profits by the 2000s — a concentration in financial services that nearly destroyed the company in the 2008 financial crisis.\n\n"
            "GE's stock price fell 74% from 2000 to 2018, as successive CEOs failed to reverse declining competitiveness in core markets and GE Capital's legacy losses. GE's 2021 announcement to break into three companies (healthcare, aviation/power, energy transition) represents the formal end of the conglomerate model that Welch built — and the most significant corporate dissolution in 20th-century business history."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "American industrial conglomerate founded 1892 (Edison + Thomson-Houston merger); Jack Welch's management philosophy dominated US business 1981–2001; GE Capital nearly destroyed it in 2008; 2021 break-up announced — the formal end of the conglomerate model; GE jet engines power 60%+ of commercial aircraft globally.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The 1892 merger of Thomas Edison's electrical companies with Thomson-Houston created the first US industrial conglomerate with a research laboratory — GE's Schenectady lab pioneered everything from X-ray machines to silicones to jet engines, establishing the corporate R&D model",
            "Jack Welch's strategic philosophy — diversifying into financial services through GE Capital as a more profitable complement to industrial manufacturing — appeared vindicated by GE's stock performance throughout the 1990s, making GE Capital the template for industrial conglomerates seeking financial returns",
            "Post-WWII industrial dominance — GE's jet engines (powering US military aircraft), nuclear power plants, electrical infrastructure, and medical devices made it the foundational supplier of multiple critical industries — created a position of market power that sustained the conglomerate for 60 years"
        ],
        "effects": [
            "Jack Welch's management philosophy — '20-70-10' forced ranking, shareholder value maximisation, GE Capital expansion — became the dominant US corporate management orthodoxy of the 1980s–1990s, directly influencing how thousands of American corporations managed people and strategy",
            "GE Aviation's jet engine dominance — powering 60%+ of commercial aircraft globally — makes GE a foundational supplier of global aviation, and its CFM International joint venture with Safran the world's most widely-deployed jet engine manufacturer",
            "GE Capital's near-collapse in 2008 — requiring a $139 billion Federal Reserve emergency credit facility — demonstrated that industrial conglomerates' expansion into financial services created systemic risk that threatened both the company and the broader financial system",
            "GE's announced break-up (2021) into three separate companies marks the definitive end of the diversified industrial conglomerate as a viable business model — confirming that the conglomerate strategy Welch championed ultimately destroyed more value than it created"
        ],
        "relationships": [
            {"entity": "Thomas Edison", "relationship": "FOUNDED_FROM_COMPANIES_OF", "note": "GE was founded in 1892 by merging Edison General Electric with Thomson-Houston — making Edison's electrical innovations the company's foundation"},
            {"entity": "Jack Welch", "relationship": "MANAGEMENT_PHILOSOPHY_DOMINATED_BY", "note": "Welch (CEO 1981–2001) created the management orthodoxy that dominated US business — forced ranking, shareholder value, GE Capital expansion"},
            {"entity": "GE Capital", "relationship": "FINANCIAL_ARM_THAT_NEARLY_DESTROYED", "note": "GE Capital provided 40%+ of GE's profits before 2008, then required a $139B Federal Reserve bailout — nearly destroying the company"},
            {"entity": "GE Aviation (jet engines)", "relationship": "OPERATES", "note": "GE Aviation's jet engines power 60%+ of commercial aircraft — making GE a foundational supplier of global aviation"},
            {"entity": "2008 financial crisis", "relationship": "NEAR-COLLAPSE_CAUSED_BY_EXPOSURE_TO", "note": "GE Capital's financial services exposure required a $139B Federal Reserve emergency facility in 2008 — demonstrating systemic risk from industrial-financial conglomerates"}
        ],
    }),

    ("visa-inc", {
        "summary": (
            "Visa Inc. is an American multinational financial services company — the world's largest payment network by transaction volume — that operates the global payment infrastructure enabling credit, debit, and prepaid card transactions between consumers, merchants, and financial institutions in 200+ countries. Founded in 1958 as BankAmericard (a credit card programme of Bank of America), spun off as Visa in 1976, and listed on the New York Stock Exchange in 2008 in one of the largest IPOs in US history ($17.9 billion), Visa processes approximately $15 trillion in transaction volume annually.\n\n"
            "Visa's business model is one of the most profitable in financial services history: Visa itself does not issue cards or extend credit (that is done by its member banks) — it provides the network infrastructure and charges transaction fees on every payment processed, generating approximately $32 billion in annual revenue (2023) from what is essentially a fee on every commercial transaction in the developed world. This toll-booth model, combined with the network effects of Visa's global acceptance, has created a near-unassailable competitive position.\n\n"
            "Visa's network effects — the fact that Visa acceptance makes every merchant more valuable to Visa cardholders, and every Visa cardholder makes every merchant more valuable by accepting Visa — created a self-reinforcing two-sided network that is the most studied example of platform economics in financial services. Visa's duopoly with Mastercard (together processing 90%+ of global card transactions) is the defining infrastructure of the modern payment economy."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "World's largest payment network by transaction volume ($15T annually); processes payments in 200+ countries; toll-booth model on global commerce; duopoly with Mastercard controls 90%+ of global card transactions; the foundational infrastructure of the modern payment economy.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Bank of America's 1958 BankAmericard — the first general-purpose credit card, mailed unsolicited to 60,000 Fresno, California residents — created the consumer credit card model that evolved into Visa, providing the infrastructure for mass consumer credit",
            "The network effects of card payment systems — the more merchants accept Visa, the more valuable Visa cards become to consumers; the more consumers carry Visa, the more valuable Visa acceptance becomes to merchants — created the self-reinforcing dynamics that made Visa and Mastercard the dominant payment platforms",
            "The separation of Visa from Bank of America (1976) and its subsequent structure as a bank cooperative allowed competing banks to jointly operate the network — overcoming the competitive conflicts that would have prevented a single bank's proprietary payment network from achieving global scale"
        ],
        "effects": [
            "Visa's payment infrastructure (200+ countries, $15T annual volume) has become the backbone of global commerce — making cashless payments the dominant form of consumer transaction in the developed world and increasingly in developing markets",
            "Visa's toll-booth model — charging fees on every transaction without bearing credit risk — is one of the most profitable business models in financial services history, generating extraordinary returns on capital from infrastructure scale advantages",
            "The Visa/Mastercard duopoly (90%+ of global card transactions) has created the dominant financial infrastructure of the modern economy — their interchange fees, transaction data, and acceptance networks are the foundation on which fintech companies, e-commerce platforms, and emerging payment systems are built",
            "Visa's digital payment infrastructure enabled the e-commerce revolution — Amazon, Alibaba, and every online retailer depend on Visa's payment rails — making Visa the invisible infrastructure of the digital economy"
        ],
        "relationships": [
            {"entity": "Bank of America", "relationship": "ORIGINATED_AS_BANKAMERICARD_OF", "note": "Visa originated as Bank of America's BankAmericard (1958) — the first general-purpose credit card programme"},
            {"entity": "Mastercard", "relationship": "GLOBAL_PAYMENT_DUOPOLY_WITH", "note": "Visa and Mastercard together process 90%+ of global card transactions — an infrastructure duopoly central to the modern payment economy"},
            {"entity": "Global e-commerce", "relationship": "FOUNDATIONAL_PAYMENT_INFRASTRUCTURE_FOR", "note": "Visa's payment rails enable e-commerce globally — every online retailer depends on Visa's infrastructure"},
            {"entity": "Fintech industry", "relationship": "PAYMENT_INFRASTRUCTURE_BUILT_UPON_BY", "note": "Most fintech companies (Stripe, Square, PayPal) process payments through Visa/Mastercard rails — making Visa foundational to the fintech ecosystem"},
            {"entity": "NYSE IPO (2008)", "relationship": "LISTED_IN_LARGEST_US_IPO_AT_TIME_ON", "note": "Visa's 2008 IPO ($17.9 billion) was the largest in US history at the time — reflecting the extraordinary value of its payment network monopoly"}
        ],
    }),

    ("meta-platforms", {
        "summary": (
            "Meta Platforms, Inc. (formerly Facebook, Inc.) is an American multinational technology company — the operator of Facebook, Instagram, WhatsApp, and Messenger — and the world's dominant social media company, with approximately 3.9 billion monthly active users across its family of apps. Founded by Mark Zuckerberg at Harvard University in 2004, Facebook expanded from a college social network to the world's largest social media platform — reshaping human communication, political discourse, advertising, and social interaction on a global scale.\n\n"
            "Meta's advertising model — using detailed behavioural data (friendships, interests, location, content consumed) to target advertisements with unprecedented precision — generates approximately $130 billion in annual advertising revenue. This model's power depends on maximum user engagement, which Meta's algorithm maximises by amplifying emotionally provocative content — generating concerns about Facebook's role in political polarisation, misinformation, ethnic violence (Myanmar, 2017), and psychological harm to teenage girls.\n\n"
            "The Cambridge Analytica scandal (2018) — in which the political data firm harvested personal data from 87 million Facebook users to target political advertising for the Trump campaign (2016) and Brexit referendum — triggered the most significant regulatory response to social media in history: the EU's GDPR enforcement, the US Congressional hearings, and state-level privacy legislation. Mark Zuckerberg's 2021 pivot to 'the metaverse' — rebranding Facebook as Meta and investing $40+ billion in virtual reality — is the most expensive corporate strategic bet in technology history."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's dominant social media company; 3.9 billion monthly users across Facebook, Instagram, WhatsApp, Messenger; Cambridge Analytica scandal (2018) triggered global data privacy regulation; role in Myanmar genocide and political polarisation; Zuckerberg's $40B metaverse bet is technology's most expensive strategic gamble.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Mark Zuckerberg's insight that the social graph — mapping human relationships — would be the most valuable data asset in the digital economy created the strategic foundation for Facebook's expansion from college social network to global platform",
            "Facebook's mobile-first adaptation (2010–2012) — rebuilding its platform for smartphone users as desktop usage declined — positioned it to capture the mobile social media market and acquire Instagram (2012, $1 billion) and WhatsApp (2014, $19 billion) before they could become competitors",
            "The network effects of social media — each additional user makes the platform more valuable to all existing users — created self-reinforcing dynamics that made Facebook's position nearly unassailable once it achieved critical mass"
        ],
        "effects": [
            "Facebook's role in the 2016 US presidential election — Cambridge Analytica's data-driven targeting, Russian disinformation campaigns, and the platform's echo-chamber dynamics — made it the central case study in the debate about social media's impact on democracy",
            "The Cambridge Analytica scandal (2018) triggered the EU's GDPR enforcement against Facebook, US Congressional hearings, and state-level privacy legislation — the most significant regulatory response to social media, reshaping global data privacy law",
            "Facebook's failure to moderate content in Myanmar (2017) — where hate speech against the Rohingya on Facebook contributed to ethnic cleansing — is the most extreme documented case of social media platform failures enabling mass atrocity",
            "Instagram's impact on teenage girls' mental health — documented in internal Facebook research that the company suppressed — is the central case study in the debate about social media's psychological harms, triggering US Congressional action and regulatory proposals globally"
        ],
        "relationships": [
            {"entity": "Mark Zuckerberg", "relationship": "FOUNDED_AND_LEADS", "note": "Zuckerberg founded Facebook (2004) at Harvard and has led it from college social network to 3.9 billion user global platform"},
            {"entity": "Cambridge Analytica scandal (2018)", "relationship": "AT_CENTRE_OF", "note": "Cambridge Analytica's harvesting of 87 million Facebook users' data for political targeting triggered global data privacy regulatory reform"},
            {"entity": "Myanmar Rohingya genocide (2017)", "relationship": "CONTENT_FAILURES_CONTRIBUTED_TO", "note": "Facebook's failure to moderate hate speech against the Rohingya in Myanmar contributed to ethnic cleansing — the most extreme documented case of platform failure enabling mass atrocity"},
            {"entity": "Instagram", "relationship": "ACQUIRED", "note": "Facebook acquired Instagram (2012, $1B) — preventing its most significant potential competitor and creating the dominant photo-sharing platform"},
            {"entity": "WhatsApp", "relationship": "ACQUIRED", "note": "Facebook acquired WhatsApp (2014, $19B) — the world's largest messaging platform (2B+ users) — preventing another potential competitor"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 10 — {len(ENTITIES)} entities (Class 330: Major Corporations continued)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
