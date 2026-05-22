#!/usr/bin/env python3
"""
Batch 48 — 8 entities (Class 322): Famous Business Schools
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()
FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/322-Class-322"
FILE_PREFIX = "322"


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
    print(f"  \u2713 {entity['name']} \u2014 sum={slen}c c={len(det.get('causes', []))} e={len(det.get('effects', []))}")


ENTITIES = [

    ("harvard-business-school", {
        "summary": (
            "Harvard Business School (HBS — est. 1908, Boston, Massachusetts, part of Harvard University) is the world's most influential business school — having produced more Fortune 500 CEOs (20%+), US presidents, senators, and cabinet secretaries than any other business school, graduating 900+ MBAs annually, and pioneering the case method of business education that is now the standard pedagogy for the world's leading business schools. HBS's annual budget exceeds $750 million, its endowment exceeds $4 billion, and its MBA programme is consistently ranked among the world's top two.\n\n"
            "Harvard Business School was founded in 1908 by Harvard University — the first business school in the United States to grant the MBA degree — with the explicit mission of developing 'business leaders who make a difference in the world.' HBS's most consequential institutional innovation was the case method — adapted from Harvard Law School's case study approach by Dean Wallace Donham (1919) — which teaches students through the analysis of real business situations, putting students in the role of decision-makers rather than passive recipients of principles.\n\n"
            "HBS alumni include Michael Bloomberg (founder, Bloomberg LP), Mitt Romney (Bain Capital co-founder, US presidential candidate), Sheryl Sandberg (Facebook COO), Jamie Dimon (JPMorgan CEO), and George W. Bush (44th US President) — demonstrating the extraordinary density of influential graduates that makes HBS the single most powerful alumni network in the world of business and politics."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "World's most influential business school (est. 1908, Harvard University Boston); 20%+ of Fortune 500 CEOs; case method of business education originator (Dean Wallace Donham 1919 — standard pedagogy worldwide); first US business school granting MBA; $750M+ annual budget, $4B+ endowment; 900+ MBAs annually; alumni: Michael Bloomberg, Mitt Romney, Sheryl Sandberg, Jamie Dimon, George W. Bush; most powerful alumni network in business and politics.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The late 19th century's emergence of large-scale corporations — Standard Oil, Carnegie Steel, J.P. Morgan's banking empire — created a new class of complex organisational problems that required professional management education beyond what law, engineering, or economics programmes provided, driving Harvard's decision to create a professional business school",
            "Dean Wallace Donham's adaptation of the case method (1919) — inspired by Harvard Law School's case study approach and the belief that business decisions could not be taught through abstract principles but required students to develop judgment through the analysis of real situations — created the pedagogical innovation that made HBS's educational model the global standard",
            "Harvard University's institutional prestige and financial resources — combined with the location in Boston, the primary financial and intellectual centre of early 20th-century America — created the network effects that made HBS the preferred destination for the most ambitious students and the most influential employers"
        ],
        "effects": [
            "The case method's global adoption — by INSEAD, Wharton, Stanford GSB, London Business School, and virtually every major business school worldwide — has made the Harvard case study the standard format for business education globally, with HBS Publishing selling 14+ million case studies annually, making Harvard the intellectual backbone of global business education",
            "HBS's alumni network — the most powerful in the world of business and politics — has created the social capital infrastructure through which a disproportionate share of Fortune 500 decisions, political appointments, and major capital allocations are made by people who share the same educational experience, values, and professional network",
            "HBS's research output — including foundational work in organisational behaviour, strategy (Michael Porter's Competitive Strategy, 1980), innovation (Clayton Christensen's The Innovator's Dilemma, 1997), and leadership — has shaped the vocabulary and conceptual framework through which business decisions are made globally",
            "The MBA degree's global spread — from a uniquely American qualification in 1908 to the standard credential for global business leadership — has been driven primarily by the prestige of HBS's programme, creating the global market for graduate management education that has produced hundreds of business schools worldwide"
        ],
        "relationships": [
            {"entity": "Case method of business education (Dean Wallace Donham 1919 innovation, global standard pedagogy)", "relationship": "ORIGINATOR_AND_PRIMARY_PROPAGATOR_OF_THE", "note": "HBS's case method — adapted from Harvard Law by Donham in 1919 — became the global standard for business education, with 14M+ case studies sold annually"},
            {"entity": "Michael Porter (Competitive Strategy 1980, Five Forces framework, strategy field creation)", "relationship": "INSTITUTIONAL_HOME_OF_THE_SCHOLARSHIP_OF", "note": "Porter's Competitive Strategy — published from HBS — defined the academic discipline of competitive strategy and became the most influential business book of the 20th century"},
            {"entity": "Clayton Christensen (The Innovator's Dilemma 1997, disruptive innovation theory)", "relationship": "INSTITUTIONAL_HOME_OF_THE_SCHOLARSHIP_OF", "note": "Christensen's disruptive innovation theory — developed at HBS — became the most influential framework for analysing technological change and business transformation"},
            {"entity": "Fortune 500 CEO pipeline (20%+ of CEOs, most powerful business alumni network)", "relationship": "PRIMARY_EDUCATIONAL_INSTITUTION_FOR", "note": "HBS's production of 20%+ of Fortune 500 CEOs makes it the single most important educational institution in the world of corporate leadership"},
            {"entity": "Harvard University (est. 1636, institutional parent, Boston Massachusetts)", "relationship": "GRADUATE_PROFESSIONAL_SCHOOL_WITHIN", "note": "HBS's position within Harvard — the world's most prestigious university — provides the institutional prestige and financial resources that sustain its global dominance"}
        ],
    }),

    ("insead", {
        "summary": (
            "INSEAD (Institut Européen d'Administration des Affaires — est. 1957, Fontainebleau, France; with campuses in Fontainebleau, Singapore, and Abu Dhabi) is the most international of the world's elite business schools — with students from 100+ nationalities in each MBA cohort, faculty from 50+ countries, and the explicit mission of creating 'globally conscious business leaders.' INSEAD was the first non-American business school to break into the top tier of global business school rankings, and its focus on cross-cultural business — rather than the American corporate experience that dominated HBS and Wharton — created the template for truly international business education.\n\n"
            "INSEAD was founded in 1957 by a group of European businesspeople who recognised that European economic integration — underway through the creation of the European Economic Community (1957) — would require business leaders who could operate across national cultures, languages, and legal systems. The school's location at Fontainebleau (near Paris) and its multilingual requirement (MBA students must speak three languages) reflected this cross-cultural vision.\n\n"
            "INSEAD's one-year MBA — distinctive in a market dominated by two-year American programmes — and its three-campus global model (France, Singapore, Abu Dhabi) have made it the preferred choice for the most internationally mobile business professionals, attracting students who are more interested in global careers than in access to the American corporate pipeline. The INSEAD MBA is consistently ranked #1 globally by the Financial Times."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Most international elite business school (est. 1957, Fontainebleau France; Fontainebleau/Singapore/Abu Dhabi campuses); students from 100+ nationalities, faculty from 50+; three-language requirement; first non-American business school in global top tier; one-year MBA (distinctive vs US two-year); European Economic Community founding context (1957); Financial Times #1 global MBA consistently; template for truly international business education.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The European Economic Community's founding (1957 — Treaty of Rome, simultaneous with INSEAD's establishment) — creating the framework for European economic integration — drove the demand for business leaders who could operate across European national cultures, languages, and legal systems, providing the strategic rationale for INSEAD's cross-cultural educational model",
            "The recognition by INSEAD's founders that American business schools' dominance — with their focus on the American corporate experience and the HBS case method — left a gap in education for international business careers outside the American market, creating the opportunity for a distinctively European and international business school",
            "The postwar reconstruction of European economies — and the emergence of multinational corporations operating across the newly integrating European market — created the commercial demand for managers with international skills that INSEAD was designed to supply"
        ],
        "effects": [
            "INSEAD's model of international business education — multilingual requirements, multicultural cohorts, and a curriculum focused on cross-cultural management — became the template for a wave of international business schools (London Business School's global focus, Wharton's international programmes), driving the internationalisation of business education globally",
            "INSEAD's Singapore campus (opened 2000) — the first major European business school to establish a significant Asian presence — positioned INSEAD at the intersection of European and Asian business networks at the moment of Asia's greatest economic ascent, making it the preferred school for executives managing European-Asian business relationships",
            "INSEAD's one-year MBA — which allows internationally mobile executives to pause their careers for one year rather than two — became the model for a series of one-year MBA programmes at other schools, challenging the HBS/Wharton two-year model and creating a significant market segment for accelerated graduate management education",
            "INSEAD's research in cross-cultural management — particularly the work of Geert Hofstede (Cultures and Organizations, 1991, five dimensions of national culture) conducted partly in the INSEAD context — created the foundational framework for cross-cultural business research that is the primary academic basis for international management education"
        ],
        "relationships": [
            {"entity": "European Economic Community (Treaty of Rome 1957, simultaneous founding context)", "relationship": "FOUNDED_IN_DIRECT_RESPONSE_TO_THE_INTEGRATION_DEMANDS_OF_THE", "note": "INSEAD's 1957 founding — simultaneous with the Treaty of Rome — was the direct educational response to European economic integration's need for cross-cultural business leaders"},
            {"entity": "Three-language requirement (MBA multilingual qualification standard)", "relationship": "DISTINCTIVE_MULTILINGUAL_EDUCATIONAL_STANDARD_REQUIRING", "note": "INSEAD's three-language requirement — unique among elite business schools — operationalises its cross-cultural mission and distinguishes its graduates"},
            {"entity": "INSEAD Singapore campus (opened 2000, European-Asian business network intersection)", "relationship": "EXPANDED_GLOBALLY_WITH_ITS_ASIA-PACIFIC_CAMPUS_AT", "note": "INSEAD Singapore — the first major European business school Asian campus — positioned INSEAD at the European-Asian business network intersection during Asia's greatest economic ascent"},
            {"entity": "Geert Hofstede (Cultures and Organizations 1991, national culture dimensions framework)", "relationship": "INSTITUTIONAL_CONTEXT_FOR_SOME_OF_THE_CROSS-CULTURAL_RESEARCH_OF", "note": "Hofstede's national culture dimensions framework — the foundational theory of cross-cultural management — was developed partly in INSEAD's intellectual context"},
            {"entity": "Financial Times MBA Rankings (#1 global MBA, consistently)", "relationship": "CONSISTENTLY_RANKED_GLOBALLY_FIRST_BY_THE", "note": "INSEAD's consistent Financial Times #1 ranking reflects its position as the dominant institution for truly international business education"}
        ],
    }),

    ("the-wharton-school", {
        "summary": (
            "The Wharton School of the University of Pennsylvania (est. 1881, Philadelphia — the world's first collegiate business school, founded by Joseph Wharton, the Bethlehem Steel industrialist) is the oldest business school in the world and one of the most influential — having established the academic legitimacy of business as a university discipline, pioneered finance as an academic field, and produced a remarkable concentration of Wall Street and financial leadership including Warren Buffett (attended 1947–1949, did not graduate), Donald Trump (BEcon 1968), Elon Musk (attended), and the largest concentration of hedge fund founders and investment bank CEOs of any school.\n\n"
            "The Wharton School was founded in 1881 by Joseph Wharton — the industrial philanthropist who built Bethlehem Steel into one of America's greatest industrial enterprises — with the explicit mission of educating young men in the principles of business and finance as an academic discipline equal to law, medicine, and engineering. This founding vision — business education as rigorous academic study rather than apprenticeship — established the template for all subsequent collegiate business education.\n\n"
            "Wharton's particular strength is finance — it is the world's leading institution for financial economics research (Fama-French three-factor model was developed partly through Wharton faculty influence; the Black-Scholes options pricing model has Wharton connections) and produces a disproportionate share of Wall Street's leadership. The Wharton Finance Department's concentration of Nobel Prize connections (multiple faculty with close ties to Economics laureates) makes it the world's most influential academic finance institution."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "World's first collegiate business school (est. 1881, University of Pennsylvania Philadelphia, Joseph Wharton founder); business education as academic discipline originator; leading institution for financial economics research; Warren Buffett (attended 1947–1949), Donald Trump (BEcon 1968); largest concentration of Wall Street leadership; Fama-French three-factor model, Black-Scholes connections; Nobel Prize faculty connections in economics; template for all collegiate business education.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Joseph Wharton's conviction — derived from his experience building Bethlehem Steel — that American business and industrial management required educated professionals with systematic knowledge of economics, accounting, and business principles rather than simply apprenticeship training, drove his 1881 donation to the University of Pennsylvania to create the first collegiate business school",
            "The emergence of large-scale American industrial corporations in the post-Civil War period — railroads, steel, oil, finance — created the demand for management professionals with systematic business knowledge that no existing university programme supplied, providing the commercial rationale for Wharton's founding",
            "The University of Pennsylvania's location in Philadelphia — the commercial and financial centre of 19th-century America, with close connections to Wall Street and the emerging American financial system — created the network that made the Wharton School the natural home for finance as an academic discipline"
        ],
        "effects": [
            "Wharton's establishment of business as a legitimate university discipline (1881) — against the prevailing view that business was a practical skill learned through apprenticeship, not academic study — created the institutional template for the wave of collegiate business schools that followed, including HBS (1908), eventually producing the 800+ AACSB-accredited business schools that now provide the standard qualification for business leadership",
            "Wharton's concentration on finance as an academic discipline — producing the research, teaching, and graduate talent that drives Wall Street — has made it the primary academic institution for the financial services industry, with Wharton alumni disproportionately represented in investment banking, hedge funds, and private equity leadership",
            "The Wharton Finance Department's research output — including significant contributions to asset pricing theory, portfolio theory, and financial derivatives — has shaped the theoretical foundations of modern financial markets, with implications for the trillions of dollars of global capital allocation that uses these frameworks",
            "Wharton's MBA programme — consistently ranked among the world's top three — has created the alumni network that dominates American financial services, with Wharton alumni managing a disproportionate share of global capital and occupying leadership positions in the institutions that shape the global financial system"
        ],
        "relationships": [
            {"entity": "Joseph Wharton (Bethlehem Steel founder, 1881 founding donation, business as academic discipline)", "relationship": "FOUNDED_BY_THE_PHILANTHROPIC_DONATION_OF", "note": "Joseph Wharton's conviction that business required academic study — not apprenticeship — created the first collegiate business school and the template for all subsequent business education"},
            {"entity": "University of Pennsylvania (est. 1740, institutional parent, Philadelphia)", "relationship": "SCHOOL_WITHIN", "note": "Penn's location in Philadelphia — 19th-century America's commercial centre — provided the network environment that made Wharton the natural home for finance as an academic discipline"},
            {"entity": "Warren Buffett (attended Wharton 1947–1949, investment philosophy partially shaped here)", "relationship": "EARLY_EDUCATIONAL_INSTITUTION_OF_THE_WORLD'S_MOST_CELEBRATED_INVESTOR", "note": "Warren Buffett's time at Wharton — though he ultimately graduated from Nebraska — exposed him to the finance education that contributed to his investment philosophy"},
            {"entity": "Wall Street and financial services leadership pipeline (hedge funds, investment banks, private equity)", "relationship": "PRIMARY_ACADEMIC_INSTITUTION_FOR_THE", "note": "Wharton's disproportionate representation in Wall Street leadership makes it the primary academic institution for the global financial services industry"},
            {"entity": "Financial economics research (Fama-French model, Black-Scholes connections, Nobel Prize faculty)", "relationship": "LEADING_ACADEMIC_INSTITUTION_FOR", "note": "Wharton's financial economics research — including connections to foundational models like Fama-French and Black-Scholes — makes it the world's most influential academic finance institution"}
        ],
    }),

    ("mit-sloan-school-of-management", {
        "summary": (
            "MIT Sloan School of Management (est. 1914 as MIT's Course XV (Economics and Business Administration), renamed in 1952 after Alfred P. Sloan Jr., the General Motors CEO who donated $10 million — the largest donation to a business school to that date) is the business school of the Massachusetts Institute of Technology — and its connection to MIT's science and engineering culture has made it the world's leading institution at the intersection of technology, innovation, and management. MIT Sloan faculty have produced some of the most influential management theories of the 20th century, including System Dynamics, the Balanced Scorecard, and the foundational theory of organisational learning.\n\n"
            "MIT Sloan's distinctive educational culture — shaped by MIT's engineering and quantitative orientation — emphasises analytical rigour, data-driven decision-making, and the application of scientific methods to management problems. The MIT Operations Research group's work (1940s–1950s) — applying linear programming and mathematical optimisation to logistics and production — created the academic foundation for operations management and supply chain management as academic disciplines.\n\n"
            "MIT Sloan's most globally influential contribution to management theory is System Dynamics — developed by Jay Forrester at MIT Sloan in the 1950s–1960s, and popularised in Peter Senge's The Fifth Discipline (1990, MIT Sloan) — which models the dynamic behaviour of complex systems and is the theoretical foundation for the global sustainability simulation models, including the Club of Rome's Limits to Growth (1972). MIT Sloan also produced the Balanced Scorecard (Robert Kaplan, with David Norton, 1992) — the most widely implemented management performance system in the world."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Business school of MIT (est. 1914, renamed 1952 after Alfred P. Sloan Jr., $10M donation); technology-innovation-management intersection; System Dynamics (Jay Forrester 1950s–1960s, Peter Senge's The Fifth Discipline 1990) — Club of Rome Limits to Growth foundation; Balanced Scorecard (Robert Kaplan and David Norton 1992, most widely implemented management system); operations research foundation (1940s–1950s, linear programming, supply chain management); analytical rigour and quantitative management approach.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "MIT's science and engineering culture — and its wartime operations research work (1940s) applying mathematical optimisation to logistics and production — created the quantitative management orientation that distinguishes MIT Sloan from the case-method-dominated HBS and Wharton, and that produced the analytical management research tradition",
            "Alfred P. Sloan Jr.'s $10 million donation (1952) — the largest to a business school to that date — provided the resources for the transformation from a department into a full graduate school, and Sloan's experience at General Motors (where he invented the multidivisional organisational structure that became the standard for large corporations) shaped the school's interest in organisational management",
            "The proximity of MIT Sloan to MIT's engineering, computer science, and physics departments — providing access to the mathematical and computational methods that underpin System Dynamics, operations research, and quantitative finance — created the interdisciplinary environment that has produced MIT Sloan's most distinctive intellectual contributions"
        ],
        "effects": [
            "System Dynamics' application to global sustainability modelling — through Donella Meadows and the Club of Rome's Limits to Growth (1972, based on MIT Sloan's World3 model) — brought the concept of planetary boundaries and resource limits to global public attention, becoming the foundational academic analysis of sustainable development and influencing every subsequent generation of environmental policy thinking",
            "The Balanced Scorecard (Kaplan and Norton, 1992) — which measures organisational performance across financial, customer, internal process, and learning/growth dimensions rather than financial metrics alone — has been adopted by 50%+ of Fortune 500 companies and the governments of multiple nations, becoming the world's most widely implemented management performance system",
            "MIT Sloan's operations research tradition — and its influence on the development of supply chain management as an academic and professional discipline — has shaped the logistics and operations of global commerce, with MIT Sloan techniques embedded in the supply chain management systems of the world's largest corporations",
            "Peter Senge's The Fifth Discipline (1990, MIT Sloan) — which popularised the concept of the 'learning organisation' and the application of System Dynamics to business management — became one of the best-selling management books in history, translating MIT Sloan's academic research into practitioner vocabulary and making 'systems thinking' a standard management concept"
        ],
        "relationships": [
            {"entity": "Alfred P. Sloan Jr. (General Motors CEO, $10M donation 1952, multidivisional structure inventor)", "relationship": "NAMED_AFTER_AND_INSTITUTIONALLY_SHAPED_BY_THE_DONATION_OF", "note": "Sloan's donation — and his GM multidivisional structure — shaped MIT Sloan's interest in large-scale organisational management"},
            {"entity": "System Dynamics (Jay Forrester 1950s, Peter Senge The Fifth Discipline 1990, Limits to Growth)", "relationship": "ORIGINATING_INSTITUTION_OF", "note": "System Dynamics — developed at MIT Sloan by Forrester — is the theoretical foundation for the Club of Rome's Limits to Growth and Peter Senge's learning organisation"},
            {"entity": "Balanced Scorecard (Robert Kaplan and David Norton 1992, 50%+ Fortune 500 adoption)", "relationship": "ORIGINATING_INSTITUTION_OF_THE_WORLD'S_MOST_WIDELY_IMPLEMENTED_MANAGEMENT_PERFORMANCE_SYSTEM", "note": "Kaplan and Norton's Balanced Scorecard — developed at MIT Sloan — has been adopted by 50%+ of Fortune 500 companies and multiple national governments"},
            {"entity": "Limits to Growth report (Club of Rome 1972, World3 model, planetary boundaries concept)", "relationship": "ACADEMIC_FOUNDATION_OF_THE_MIT_SYSTEM_DYNAMICS_GROUP_WHOSE_WORLD3_MODEL_UNDERPINNED_THE", "note": "The Limits to Growth's World3 model — built on MIT Sloan's System Dynamics — brought planetary boundaries to global attention"},
            {"entity": "MIT (Massachusetts Institute of Technology, quantitative engineering culture, interdisciplinary access)", "relationship": "MANAGEMENT_SCHOOL_OF", "note": "MIT's quantitative engineering culture and interdisciplinary environment have produced MIT Sloan's distinctive analytical management research tradition"}
        ],
    }),

    ("kellogg-school-of-management", {
        "summary": (
            "Kellogg School of Management (est. 1908 as Northwestern University's School of Commerce, renamed in 1979 after John L. Kellogg — son of the Kellogg cereal company founder — who donated $10 million) is one of the world's leading business schools, consistently ranked among the global top five, and the school most closely identified with marketing and organisational behaviour as academic disciplines. Kellogg's collaborative culture — emphasising teamwork, interpersonal skills, and a 'nice people' reputation in contrast to the more competitive cultures of HBS and Wharton — has made it the preferred school for executives pursuing careers in marketing, consumer goods, healthcare, and technology.\n\n"
            "Kellogg's academic strength in marketing — producing foundational research in consumer behaviour, brand equity, and pricing strategy — has made it the primary academic institution for the consumer goods industry, with Kellogg alumni disproportionately represented in the marketing leadership of companies from Procter & Gamble to Apple. Philip Kotler (S.C. Johnson Distinguished Professor of International Marketing at Kellogg) — the author of Marketing Management (1967, the most widely used marketing textbook in the world, translated into 57 languages) — is the single most influential academic in the history of marketing, and his association with Kellogg defines its academic identity.\n\n"
            "Kellogg's cooperative culture — in which students are selected partly for interpersonal skills and required to do extensive group work — has created an alumni network known for mutual support and collaborative leadership, producing a distinctive graduate culture that differentiates Kellogg alumni in organisational leadership positions."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Top-five global business school (est. 1908 Northwestern University, renamed 1979 after John L. Kellogg, $10M donation); leading institution for marketing as academic discipline; Philip Kotler (Marketing Management 1967, most widely used marketing textbook, 57 languages — world's most influential marketing academic); consumer goods industry leadership pipeline; collaborative 'nice people' culture vs HBS/Wharton; organisational behaviour research strength; Chicago location, Northwestern University institutional parent.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Northwestern University's Chicago location — surrounded by the world's largest concentration of consumer goods companies, financial services firms, and industrial corporations — created the commercial environment that drove Kellogg's specialisation in marketing, management, and the disciplines most relevant to consumer-facing businesses",
            "Philip Kotler's joining of Kellogg's faculty (1962) — and his subsequent development of marketing as a systematic academic discipline through Marketing Management (1967) and 50+ subsequent books — created the intellectual identity that made Kellogg the world's leading institution for marketing education",
            "John L. Kellogg's $10 million donation (1979) — and the strategic decision to rename the school — provided the resources and identity that enabled Kellogg to invest in the faculty hiring and programme development that elevated it into the global top five"
        ],
        "effects": [
            "Philip Kotler's Marketing Management — developed and refined through 50+ years of Kellogg teaching — has been translated into 57 languages and used in virtually every MBA marketing curriculum worldwide, making Kellogg's marketing intellectual tradition the global standard for marketing education",
            "Kellogg's cooperative culture — selecting for interpersonal skills and emphasising group work — has created a graduate cohort that prioritises collaborative leadership over competitive individual performance, producing a distinctive organisational leadership style that is particularly effective in matrix organisations and team-based work environments",
            "Kellogg's healthcare management programme — one of the world's strongest — has produced a disproportionate share of hospital system executives, healthcare company leadership, and health policy professionals, making it the primary business school for the healthcare sector",
            "Kellogg's marketing research tradition — and its production of marketing leadership for consumer goods companies from P&G to Apple — has shaped the marketing strategies of the companies whose brands are most visible in global consumer culture, embedding Kellogg's academic frameworks in the practical marketing decisions that affect billions of consumers"
        ],
        "relationships": [
            {"entity": "Philip Kotler (Marketing Management 1967, 57 languages, world's most influential marketing academic)", "relationship": "INTELLECTUAL_IDENTITY_DEFINED_BY_THE_SCHOLARSHIP_OF", "note": "Kotler's Marketing Management — developed through 50+ years of Kellogg teaching — made Kellogg the world's leading institution for marketing education"},
            {"entity": "Northwestern University (Evanston Illinois, institutional parent, Chicago commercial environment)", "relationship": "SCHOOL_WITHIN", "note": "Northwestern's Chicago location — surrounded by consumer goods and financial services companies — drove Kellogg's specialisation in marketing and management"},
            {"entity": "Consumer goods industry leadership pipeline (P&G, Apple, healthcare companies)", "relationship": "PRIMARY_BUSINESS_SCHOOL_FOR_THE", "note": "Kellogg alumni's disproportionate representation in consumer goods marketing leadership makes it the primary business school for the consumer-facing business sector"},
            {"entity": "John L. Kellogg (cereal company family, $10M donation 1979, school renaming)", "relationship": "NAMED_AFTER_THE_DONOR", "note": "John L. Kellogg's 1979 donation — and the strategic renaming — provided the resources and identity that elevated Kellogg to the global top five"},
            {"entity": "Collaborative culture in business education (teamwork selection, group work, alumni mutual support)", "relationship": "PRIMARY_INSTITUTIONAL_EXEMPLAR_OF", "note": "Kellogg's cooperative culture — selecting for interpersonal skills — has created a distinctive graduate cohort known for collaborative leadership"}
        ],
    }),

    ("haas-school-of-business", {
        "summary": (
            "Haas School of Business (est. 1898, University of California Berkeley — the oldest business school at a public university in the United States, renamed in 1989 after Walter A. Haas Jr. of Levi Strauss & Co., whose family donated $23.7 million) is the business school of UC Berkeley — and its location in the Bay Area, adjacent to Silicon Valley, has made it the most influential business school in the world for technology entrepreneurship, with more tech startup founders per class than any other school. Haas is consistently ranked among the global top ten, with particular strength in entrepreneurship, real estate, and sustainability.\n\n"
            "Haas's 'Defining Leadership Principles' — Question the Status Quo, Confidence Without Attitude, Students Always, and Beyond Yourself — define a distinctive culture that diverges deliberately from the hierarchical prestige culture of HBS and Wharton, emphasising intellectual humility, collaborative innovation, and social responsibility. This culture reflects the Bay Area's startup ethos and has created a graduate cohort that is particularly effective in the flat, mission-driven organisations of the technology sector.\n\n"
            "Haas's Bay Area location provides unparalleled access to the Silicon Valley ecosystem — UC Berkeley graduates founded companies including Apple (Steve Wozniak, BS EE 1986), Intel (Gordon Moore, PhD Chemistry 1954), and numerous venture-backed startups — and the Haas School's entrepreneurship programme has contributed to the founding culture that makes UC Berkeley the world's most prolific university for technology company founders."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Oldest business school at US public university (est. 1898, UC Berkeley); Bay Area / Silicon Valley tech entrepreneurship influence; Walter A. Haas Jr. (Levi Strauss, $23.7M donation, renamed 1989); Defining Leadership Principles (Question the Status Quo, Confidence Without Attitude, Students Always, Beyond Yourself); Apple co-founder Steve Wozniak, Intel co-founder Gordon Moore — UC Berkeley alumni; global top-ten ranking; sustainability and social responsibility emphasis; flat startup-culture graduate cohort.",
            "significanceCategory": "continental"
        },
        "causes": [
            "UC Berkeley's Bay Area location — in the epicentre of the technology industry, with close proximity to Silicon Valley's venture capital ecosystem and the technology companies that define the modern global economy — created the commercial environment that shaped Haas's distinctive technology entrepreneurship focus",
            "Walter A. Haas Jr.'s $23.7 million donation (1989) — from the Levi Strauss & Co. fortune, reflecting a company culture of social responsibility and ethical business — drove both the school's renaming and its distinctively values-driven approach to business education",
            "The University of California's public mission — providing excellent education at lower cost than private competitors, attracting a more diverse student body — created the inclusive meritocratic culture that, combined with Bay Area startup values, produced Haas's distinctive 'Confidence Without Attitude' culture"
        ],
        "effects": [
            "Haas's contribution to the Silicon Valley ecosystem — through alumni founders, faculty research in entrepreneurship and innovation, and the placement of graduates in technology company leadership — has made it the primary academic institution for the industry that has most transformed the global economy in the past half-century",
            "Haas's sustainability focus — including one of the world's strongest programs in sustainable business and impact investing — has positioned it as the leading business school for the ESG (Environmental, Social, Governance) movement, producing the graduate cohort that is reshaping corporate sustainability practices",
            "The Haas culture's emphasis on intellectual humility and collaborative innovation — the 'Confidence Without Attitude' principle — has produced a graduate cohort that is particularly effective in the flat, fast-moving organisations of the technology sector, where the authoritative leadership styles valued at HBS can be counterproductive",
            "Haas's status as the oldest business school at a public university — and its consistent global top-ten ranking at a fraction of the cost of private competitors — has demonstrated that excellent business education can be delivered at scale by public institutions, influencing the development of other public university business schools worldwide"
        ],
        "relationships": [
            {"entity": "University of California Berkeley (public university, meritocratic culture, Bay Area location)", "relationship": "SCHOOL_WITHIN", "note": "UC Berkeley's public mission and Bay Area location shaped Haas's distinctive meritocratic, technology-entrepreneurship-focused culture"},
            {"entity": "Silicon Valley technology ecosystem (Apple, Intel, venture capital, tech startup founding culture)", "relationship": "EMBEDDED_IN_THE_GEOGRAPHIC_CENTRE_OF_THE", "note": "Haas's Bay Area proximity to Silicon Valley makes it the most influential business school for technology entrepreneurship"},
            {"entity": "Walter A. Haas Jr. (Levi Strauss, $23.7M donation 1989, social responsibility values)", "relationship": "NAMED_AFTER_AND_VALUE-SHAPED_BY_THE_DONATION_OF", "note": "Haas's social responsibility and ethical business emphasis reflects the Levi Strauss values of its naming donor"},
            {"entity": "Defining Leadership Principles (Question Status Quo, Confidence Without Attitude, Students Always)", "relationship": "DISTINCTIVE_CULTURE_DEFINED_BY_THE", "note": "Haas's four leadership principles — creating a culture that diverges from HBS prestige hierarchy — produce a graduate cohort particularly effective in startup-culture organisations"},
            {"entity": "ESG and sustainable business education (impact investing, corporate sustainability leadership)", "relationship": "LEADING_BUSINESS_SCHOOL_FOR", "note": "Haas's sustainability focus has positioned it as the primary business school for the ESG movement reshaping corporate practice"}
        ],
    }),

    ("london-school-of-business-and-finance", {
        "summary": (
            "London School of Business and Finance (LSBF — est. 2003, London) is a private higher education institution offering professional finance and business qualifications — particularly ACCA (Association of Chartered Certified Accountants) and CIMA (Chartered Institute of Management Accountants) preparation courses — serving a predominantly international student population seeking professional qualifications recognised in the global financial services industry. LSBF operates as part of the Global University Systems (GUS) network and delivers programmes through both its London campus and online platforms.\n\n"
            "LSBF occupies a distinctive niche in British business education — focusing on professional qualification preparation for internationally mobile finance professionals rather than the MBA market served by London Business School and Imperial College Business School. Its student body — primarily drawn from Asia, Africa, and the Middle East — reflects the global demand for ACCA and CIMA qualifications as credentials for the financial services industry outside the Anglophone core.\n\n"
            "The institution's growth reflects the broader globalisation of professional financial qualifications — as ACCA and CIMA have become recognised credentials for finance professionals worldwide, the demand for preparation courses accessible to international students at London's geographic and financial centre has created a significant market segment that LSBF has served since 2003."
        ),
        "importanceScore": 5,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "Private higher education institution (est. 2003, London, Global University Systems network); professional finance qualification preparation (ACCA, CIMA); predominantly international student body (Asia, Africa, Middle East); global demand for professional financial qualifications — ACCA and CIMA credentials worldwide; London financial centre location; online platform delivery; niche in British business education distinct from MBA market.",
            "significanceCategory": "local"
        },
        "causes": [
            "The globalisation of ACCA and CIMA professional qualifications — which became recognised credentials for finance professionals worldwide from the 1990s onwards — created a growing international market for preparation courses delivered at London, the world's leading financial centre",
            "The demand from internationally mobile finance professionals — particularly from Asia, Africa, and the Middle East — for London-based professional qualification preparation that would provide both the credential and the London network for careers in the global financial services industry",
            "The growth of online professional education from the early 2000s — which LSBF has embraced as a primary delivery channel — created the opportunity to serve the global ACCA and CIMA market at scale beyond the London campus's geographic reach"
        ],
        "effects": [
            "LSBF's contribution to the globalisation of professional financial qualifications — by making ACCA and CIMA preparation accessible to international students in London — has helped establish these British qualifications as global credentials, contributing to the internationalisation of financial professional standards",
            "The institution's predominantly international student body — from Asia, Africa, and the Middle East — has made it a significant contributor to the global network of finance professionals trained in London, extending the reach of British financial education beyond the traditional Anglo-American elite pipeline",
            "LSBF's online platform expansion — delivering professional qualification preparation to students who cannot travel to London — has contributed to the democratisation of access to professional financial education, reducing the geographic barrier to ACCA and CIMA qualifications for students in developing markets"
        ],
        "relationships": [
            {"entity": "ACCA (Association of Chartered Certified Accountants, primary qualification offered)", "relationship": "PRIMARY_PROFESSIONAL_QUALIFICATION_PREPARATION_INSTITUTION_FOR_THE", "note": "ACCA preparation is LSBF's primary educational offering and commercial rationale"},
            {"entity": "Global University Systems (GUS network, institutional parent)", "relationship": "COMPONENT_INSTITUTION_OF_THE", "note": "LSBF operates within the Global University Systems network of international higher education providers"},
            {"entity": "London financial centre (geographic location, international student attraction, network access)", "relationship": "BENEFITS_FROM_THE_GEOGRAPHIC_LOCATION_OF_THE", "note": "London's position as the world's leading financial centre drives the demand for LSBF's London-based professional qualification preparation"},
            {"entity": "CIMA (Chartered Institute of Management Accountants, qualification offered)", "relationship": "PREPARATION_COURSES_OFFERED_FOR_THE_QUALIFICATIONS_OF_THE", "note": "CIMA preparation — alongside ACCA — defines LSBF's professional qualification focus"},
            {"entity": "International finance professional qualifications globalisation (ACCA/CIMA as global credentials)", "relationship": "BENEFICIARY_OF_THE", "note": "LSBF's growth reflects the broader globalisation of ACCA and CIMA as recognised credentials for finance professionals worldwide"}
        ],
    }),

    ("stern-school-of-business", {
        "summary": (
            "NYU Stern School of Business (est. 1900 as the School of Commerce, Accounts and Finance, renamed in 1988 after Leonard N. Stern who donated $30 million) is one of the world's leading business schools — ranked consistently in the global top fifteen — and, through its New York City location, the business school most embedded in the world's largest financial centre. NYU Stern's particular strengths are finance (it is one of the world's leading academic institutions for financial economics), real estate (its Schack Institute of Real Estate is the most influential in the field), and global business (its stern.nyu.edu location in lower Manhattan gives students unparalleled access to Wall Street and the New York financial ecosystem).\n\n"
            "NYU Stern's finance faculty have produced some of the most influential economic thinking of the contemporary era — Nouriel Roubini (who predicted the 2008 financial crisis with remarkable accuracy), Aswath Damodaran (whose corporate valuation models are the practical standard for investment banking and private equity), and Edward Altman (who developed the Z-score bankruptcy prediction model used by financial institutions worldwide) have all been Stern faculty.\n\n"
            "NYU Stern's location — in Greenwich Village, Manhattan, within walking distance of Wall Street, the Federal Reserve Bank of New York, and the major investment banks — creates an educational environment of unique commercial immediacy, with students attending lectures by industry practitioners and taking internships at the institutions that define the global financial system."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Top-fifteen global business school (est. 1900 NYU, renamed 1988 after Leonard Stern $30M donation); Wall Street proximity — unparalleled financial services access; Nouriel Roubini (predicted 2008 financial crisis), Aswath Damodaran (corporate valuation models, investment banking standard), Edward Altman (Z-score bankruptcy prediction); Schack Institute of Real Estate (most influential); global finance leadership pipeline; lower Manhattan Greenwich Village location; financial economics research strength.",
            "significanceCategory": "continental"
        },
        "causes": [
            "New York University's location in Manhattan — the centre of American and global finance — created the geographic proximity to Wall Street, investment banks, and financial regulators that makes NYU Stern uniquely positioned to produce graduates with both academic training and direct exposure to the world's most important financial institutions",
            "Leonard N. Stern's $30 million donation (1988) — from the Hartz Mountain Corporation pet products fortune — provided the resources to rebuild NYU Stern's facilities and faculty, enabling the investment in research and educational quality that elevated it to its current global standing",
            "The emergence of New York as the world's dominant financial centre from the 1970s onwards — with the deregulation of the financial services industry, the growth of derivatives markets, and the internationalisation of capital flows — created both the commercial demand for finance-educated graduates and the research agenda that Stern's faculty have addressed"
        ],
        "effects": [
            "Nouriel Roubini's prediction of the 2008 financial crisis — developed through his NYU Stern research and published in multiple academic papers before the crisis — gave Stern global visibility as a centre for critical financial analysis, demonstrating the value of academic economic research in understanding systemic financial risk",
            "Aswath Damodaran's corporate valuation models and textbooks — freely available on his NYU Stern website and used by virtually every investment bank, private equity firm, and corporate finance department in the world — have made NYU Stern the de facto academic standard for practical corporate valuation, embedding Stern's intellectual framework in trillions of dollars of financial decisions",
            "Edward Altman's Z-score bankruptcy prediction model — developed at NYU Stern and now used by financial institutions worldwide for credit analysis and risk assessment — is the most widely used academic financial model in practical banking, making Stern's research the direct input to banking risk management globally",
            "NYU Stern's real estate programme — through the Schack Institute and its New York City location — has produced the most influential academic research on urban real estate markets, directly informing policy decisions about housing, commercial development, and urban planning in the world's largest cities"
        ],
        "relationships": [
            {"entity": "Nouriel Roubini (NYU Stern faculty, 2008 financial crisis prediction, systemic risk analysis)", "relationship": "INSTITUTIONAL_HOME_OF_THE_SCHOLARSHIP_OF", "note": "Roubini's pre-crisis prediction — developed through Stern research — gave the school global visibility as a centre for critical financial analysis"},
            {"entity": "Aswath Damodaran (corporate valuation models, investment banking standard, freely available tools)", "relationship": "INSTITUTIONAL_HOME_OF_THE_SCHOLARSHIP_OF", "note": "Damodaran's valuation models — the de facto standard for practical corporate finance worldwide — have made Stern's intellectual framework the input to trillions in financial decisions"},
            {"entity": "Edward Altman (Z-score bankruptcy prediction model, banking risk management standard)", "relationship": "INSTITUTIONAL_HOME_OF_THE_SCHOLARSHIP_OF", "note": "Altman's Z-score — developed at Stern — is the most widely used academic financial model in practical banking"},
            {"entity": "Wall Street and Federal Reserve Bank of New York (geographic proximity, commercial immediacy)", "relationship": "GEOGRAPHIC_PROXIMITY_TO_THE_WORLD'S_MOST_IMPORTANT_FINANCIAL_INSTITUTIONS_INCLUDING", "note": "Stern's walking-distance proximity to Wall Street and the Federal Reserve creates an educational environment of unique commercial immediacy"},
            {"entity": "Leonard N. Stern (Hartz Mountain Corporation, $30M donation 1988, school renaming)", "relationship": "NAMED_AFTER_THE_DONOR", "note": "Stern's 1988 donation provided the resources that elevated NYU Stern to its current global standing"}
        ],
    }),

]


if __name__ == "__main__":
    print(f"Batch 48 \u2014 {len(ENTITIES)} entities (Class 322: Famous Business Schools)")
    for slug, data in ENTITIES:
        print(f"\n\u2192 {slug}")
        enrich_entity(slug, data)
    print("\n\u2713 Done")
