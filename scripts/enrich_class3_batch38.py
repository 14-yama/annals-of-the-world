#!/usr/bin/env python3
"""
Batch 38 — 8 entities (Class 364): Major Media & Press Institutions
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()
FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/364-Class-364"
FILE_PREFIX = "364"


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

    ("acta-diurna", {
        "summary": (
            "The Acta Diurna (Latin: 'Daily Acts', also Acta Populi or Acta Publica, est. c.59 BCE, Rome — decreed by Julius Caesar) was the world's first newspaper — the original public record of daily events in Rome, posted on whitened boards (alba) in public spaces throughout the city. The Acta Diurna reported on government decisions, military victories, births, deaths, marriages, gladiatorial games, prodigies, trials, and public events — providing Roman citizens with a daily digest of news in a format that anticipates modern journalism by two millennia.\n\n"
            "Julius Caesar decreed the Acta Diurna in 59 BCE — his first year as consul — as a political act: making the proceedings of the Senate public was a democratic gesture that undermined the Senate's aristocratic claim to exclusive deliberative authority. The Acta were written by scribes appointed by the government, posted at the Roman Forum and other public spaces, and later transcribed by professional letter-writers (actuarii) who sent copies to provincial governors and wealthy Romans throughout the Empire.\n\n"
            "The Acta Diurna's existence is known primarily through references in Cicero, Suetonius, Tacitus, Pliny the Elder, and Petronius — no original copy survives. Its historical significance lies in establishing the principle that governments have an obligation to make public records of their activities accessible to citizens — a principle that underlies the modern concept of freedom of information and the free press."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "World's first newspaper (est. c.59 BCE, Julius Caesar); posted on whitened boards (alba) at Roman Forum and public spaces; reported government decisions, military victories, births, deaths, gladiatorial games, trials; transcribed by actuarii for distribution throughout Empire; known through Cicero, Suetonius, Tacitus, Pliny the Elder, Petronius; no original survives; established principle of public government records — ancestor of freedom of information and free press concept; 2,000 years before modern newspapers.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Julius Caesar's political motivation — making Senate proceedings public to undermine aristocratic secrecy and appeal to the popular democratic sentiment of the Roman populace — drove his 59 BCE decree establishing the Acta Diurna",
            "The literacy and urban density of Rome — a city of 1 million people with a substantial literate population capable of reading public postings — created the audience that made a public news document meaningful and the scribal infrastructure capable of producing it",
            "The Roman Empire's need to communicate official decisions and news to provincial governors and Roman citizens throughout the Mediterranean — who could not attend the Forum — created the demand for the Acta's distribution through copying and courier systems"
        ],
        "effects": [
            "The Acta Diurna established the concept of daily public information as a government obligation — the principle that citizens have a right to know what their government is doing — that would eventually develop into the modern concept of freedom of information, the free press, and the right of public access to government records",
            "The Acta's format — a daily digest of official actions, public events, births, deaths, and popular entertainment — established the structural template of the newspaper: the combination of political news, official records, social announcements, and popular entertainment that characterises newspapers to the present day",
            "The network of actuarii (professional letter-writers) who copied and distributed the Acta throughout the Roman Empire established the first information distribution network — the prototype for the news wire services (Reuters, Associated Press) that would develop 1,900 years later",
            "Caesar's use of public information as a political tool — to build popular support by making aristocratic deliberations transparent — established the political logic of media control and information democratisation that has characterised every subsequent political media environment"
        ],
        "relationships": [
            {"entity": "Julius Caesar (decreed 59 BCE, first year as consul)", "relationship": "FOUNDED_BY_DECREE_OF", "note": "Caesar's 59 BCE decree establishing the Acta Diurna was a political act — making Senate proceedings public to appeal to democratic sentiment and undermine aristocratic secrecy"},
            {"entity": "Roman Forum (primary posting location)", "relationship": "POSTED_DAILY_AT_THE", "note": "The Acta were posted on whitened boards (alba) at the Roman Forum and other public spaces — making Rome's central civic space also its primary news medium"},
            {"entity": "Actuarii (professional copyists, distribution network)", "relationship": "DISTRIBUTED_THROUGH_THE_NETWORK_OF", "note": "The actuarii who copied and distributed the Acta throughout the Empire established the first information distribution network — prototype of modern news wire services"},
            {"entity": "Modern newspaper (structural descendant)", "relationship": "CONCEPTUAL_AND_STRUCTURAL_ANCESTOR_OF_THE", "note": "The Acta's format — political news, official records, social announcements, entertainment — established the structural template of the newspaper"},
            {"entity": "Freedom of information principle (modern legacy)", "relationship": "FOUNDING_PRECEDENT_FOR_THE", "note": "The Acta established the principle that citizens have a right to public government records — the founding precedent for modern freedom of information concepts"}
        ],
    }),

    ("reuters", {
        "summary": (
            "Reuters (est. 1851, London — founded by Paul Julius Reuter) is the world's most trusted international news agency — the organisation that established the modern concept of objective, impartial news reporting and created the global news wire infrastructure that distributes information to every media organisation on Earth. Reuters operates in 200 countries with 2,500+ journalists, covering news, financial markets, and video in 16 languages, and its financial data services (Reuters Terminal, now Refinitiv) are the primary information source for the global financial industry.\n\n"
            "Paul Julius Reuter founded his news agency in Aachen in 1849, initially using carrier pigeons to bridge the gap in the telegraph network between Brussels and Aachen — demonstrating from the start that speed of information delivery was commercially valuable. Moving to London in 1851, Reuters established itself as the primary agency for distributing news between Europe and America via the newly completed transatlantic telegraph cable, covering the American Civil War, the assassination of Abraham Lincoln, and the Franco-Prussian War.\n\n"
            "Reuters's foundational journalistic principle — 'Get there first with the truth' — was established by Reuter himself and distinguished Reuters from competitors who prioritised speed over accuracy. Reuters's coverage of the Battle of Solferino (1859), the American Civil War's telegraphed dispatches, and its Reuters World Service established the template for international wire service journalism that the Associated Press, AFP, and all subsequent news agencies followed."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's most trusted international news agency (est. 1851, Paul Julius Reuter); 200 countries, 2,500+ journalists, 16 languages; established modern concept of objective impartial news reporting; carrier pigeons to bridge telegraph gap (1849); transatlantic cable coverage (1866); American Civil War dispatches; 'Get there first with the truth' principle; Reuters Terminal/Refinitiv — primary financial industry information source; template for AP, AFP, and all subsequent news agencies.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Paul Julius Reuter's recognition (1849) that the gap in the telegraph network between Brussels and Aachen created a commercial opportunity — using carrier pigeons to bridge the gap and deliver financial news faster than any competitor — established both the business model and the technological entrepreneurialism that characterised Reuters",
            "The transatlantic telegraph cable (1866) created the technical infrastructure for global real-time news distribution — and Reuters's position as the primary news agency using this infrastructure gave it first-mover advantage in the international news market that it has never fully relinquished",
            "The 19th-century global financial system's demand for accurate, timely information about events affecting commodity prices, currency rates, and political stability — which only a professionally staffed, globally distributed news agency could provide — created the commercial market that sustained Reuters's growth"
        ],
        "effects": [
            "Reuters's establishment of objective, impartial reporting as the professional standard for news agencies — the principle that facts should be reported accurately regardless of political implications — created the journalistic ethic that became the foundation of modern professional journalism worldwide",
            "The Reuters terminal (now Refinitiv) — providing real-time financial data, news, and analytics to 300,000+ financial professionals worldwide — is the primary information infrastructure of the global financial industry, making Reuters's data services more economically significant than its news services",
            "Reuters's coverage of the American Civil War — providing European and world audiences with their primary source of information about the most significant military conflict of the 19th century — established the template for international war correspondence and the global news agency as the primary conduit for foreign news",
            "Reuters's model of a commercially funded, editorially independent global news agency — sustained by financial data services rather than political patronage — provided the institutional template for the information infrastructure of global democracy, demonstrating that accurate news could be a commercially viable service"
        ],
        "relationships": [
            {"entity": "Paul Julius Reuter (founder, carrier pigeons 1849, London 1851)", "relationship": "FOUNDED_BY", "note": "Reuter's 1849 carrier pigeon bridge and 1851 London founding established both the business model and the technological entrepreneurialism that characterised Reuters from the start"},
            {"entity": "Transatlantic telegraph cable (1866)", "relationship": "FIRST-MOVER_ADVANTAGE_IN_INTERNATIONAL_NEWS_PROVIDED_BY_THE", "note": "The transatlantic cable gave Reuters first-mover advantage in global real-time news distribution — an advantage it has never fully relinquished"},
            {"entity": "Reuters Terminal / Refinitiv (financial data services)", "relationship": "OPERATES_THE_PRIMARY_FINANCIAL_INDUSTRY_INFORMATION_INFRASTRUCTURE_OF_THE", "note": "The Reuters Terminal (now Refinitiv) provides real-time financial data to 300,000+ professionals — making Reuters's data services more economically significant than its journalism"},
            {"entity": "Objective journalism principle ('Get there first with the truth')", "relationship": "ESTABLISHED_THE_FOUNDATIONAL_JOURNALISTIC_ETHIC_OF", "note": "Reuter's 'Get there first with the truth' principle established objective reporting as the professional standard that became the foundation of modern journalism"},
            {"entity": "Associated Press, AFP (Reuters-model agencies)", "relationship": "DIRECT_INSTITUTIONAL_MODEL_FOR_THE", "note": "Reuters established the template for international wire service journalism that AP, AFP, and all subsequent news agencies followed"}
        ],
    }),

    ("associated-press", {
        "summary": (
            "The Associated Press (AP, est. 1846, New York — founded by 5 New York newspapers as a cooperative to share telegraphic news dispatches) is the world's oldest and largest news agency — the cooperative organisation that distributes news to 15,000 media outlets worldwide, reaching half the world's population daily. AP's cooperative model — owned by its 1,400+ member newspapers, who share content rather than compete for it — was a revolutionary business innovation that made comprehensive news coverage economically viable for small regional newspapers and established the infrastructure of American and global journalism.\n\n"
            "The Associated Press was founded in 1846 — during the Mexican-American War — when five New York newspapers (Herald, Sun, Tribune, Journal of Commerce, and Courier and Enquirer) agreed to share the cost of telegraphic dispatches from the war front. The cooperative model — in which member newspapers share reporting costs and distribute standardised content — allowed AP to provide comprehensive coverage that no single newspaper could afford alone, while its requirement that all reporting be factual and politically neutral (to serve both Republican and Democratic member papers equally) established objective journalism as an institutional requirement.\n\n"
            "AP's historic scoops include the first news of Lincoln's assassination (1865), the first confirmed reports of the atomic bombing of Hiroshima (1945), and the first photographic documentation of the My Lai massacre (1972). AP photographers have won 55 Pulitzer Prizes — more than any other news organisation."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's oldest and largest news agency (est. 1846, 5 New York newspapers cooperative); 15,000 media outlets, half world's population daily; cooperative model — owned by 1,400+ member newspapers; founded during Mexican-American War; required political neutrality to serve both Republican and Democratic papers — institutionalised objective journalism; first news of Lincoln's assassination (1865); first confirmation of Hiroshima bombing (1945); My Lai massacre photos (1972); 55 Pulitzer Prizes — most of any news organisation.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Mexican-American War's creation of the demand for rapid telegraphic news dispatches — and five New York newspapers' recognition that they could reduce costs and expand coverage by sharing dispatch costs — drove the cooperative founding that created the AP model",
            "The telegraph's transformation of news economics — making speed of information delivery commercially decisive, but also making individual telegraph costs prohibitive for small newspapers — created the structural imperative for cooperative news sharing that the AP model answered",
            "The AP's requirement for political neutrality in reporting — imposed because the cooperative served both Republican and Democratic member papers who would cancel their membership if AP was politically biased — institutionalised objective journalism as a structural requirement rather than an ethical aspiration"
        ],
        "effects": [
            "The AP's cooperative model — which allowed small regional newspapers to access comprehensive national and international news at affordable shared costs — democratised news access across the United States, making it possible for every county seat newspaper to carry comprehensive national coverage alongside local news",
            "AP's requirement for political neutrality — serving both Republican and Democratic papers — institutionalised objective journalism as the professional standard for American news reporting, shaping the journalistic culture of the entire American news industry for 175 years",
            "AP's 55 Pulitzer Prizes — the most of any news organisation — reflect its consistent production of the most impactful journalism in American history, from Edward Kennedy's scoop on Germany's WWII surrender to Nick Ut's Pulitzer-winning photograph of the 'Napalm Girl' from the Vietnam War",
            "The AP's global expansion — distributing to 15,000 media outlets in 300 locations worldwide — created the global news infrastructure that makes international events immediately accessible to regional newspapers in every country, establishing the homogenising effect of standardised international news reporting on global public consciousness"
        ],
        "relationships": [
            {"entity": "Five New York newspapers (Herald, Sun, Tribune, 1846 cooperative founders)", "relationship": "FOUNDED_AS_COOPERATIVE_BY_THE", "note": "AP was founded (1846) when 5 New York newspapers agreed to share telegraphic dispatch costs from the Mexican-American War — the original cooperative model"},
            {"entity": "Objective journalism (AP structural requirement for political neutrality)", "relationship": "PRIMARY_INSTITUTIONAL_FORCE_INSTITUTIONALISING", "note": "AP's requirement for political neutrality — to serve both Republican and Democratic members — institutionalised objective journalism as an American professional standard"},
            {"entity": "Lincoln assassination (first AP dispatch 1865)", "relationship": "FIRST_ORGANISATION_TO_REPORT_THE", "note": "AP's first news of Lincoln's assassination (1865) established the template for AP's role as the primary source for breaking national news"},
            {"entity": "My Lai massacre photographs (Nick Ut, Pulitzer Prize)", "relationship": "DISTRIBUTED_THE_DEFINING_PHOTOGRAPHIC_DOCUMENTATION_OF_THE", "note": "AP's distribution of Nick Ut's photographs — including the 'Napalm Girl' — shaped American public opinion on the Vietnam War"},
            {"entity": "15,000 global media outlets (AP distribution reach)", "relationship": "DISTRIBUTES_NEWS_TO", "note": "AP's distribution to 15,000 outlets worldwide — reaching half the world's population — makes it the primary infrastructure of global news dissemination"}
        ],
    }),

    ("cnn", {
        "summary": (
            "CNN (Cable News Network, est. 1 June 1980, Atlanta, Georgia — founded by Ted Turner) was the world's first 24-hour news channel and the organisation that invented the concept of cable news — transforming television news from a brief evening broadcast into a continuous, global information environment. CNN's 1991 Gulf War coverage — the first live televised war, with CNN's Baghdad bureau reporting missile strikes as they happened — established the 'CNN effect': the idea that real-time television coverage of crises forces governments to respond in ways they might not otherwise, permanently altering the relationship between media and foreign policy.\n\n"
            "Ted Turner launched CNN on 1 June 1980 — with Peter Arnett, Bernard Shaw, and Daniel Schorr as founding anchors — against the fierce scepticism of the established television networks (NBC, CBS, ABC) who dismissed the concept of 24-hour news. CNN's first major test was the Challenger space shuttle disaster (1986), when CNN was the only network with live coverage at the moment of the explosion; its Gulf War coverage in 1991 demonstrated that real-time news from a war zone could reach global audiences simultaneously.\n\n"
            "CNN's innovations include the 24-hour news cycle, the news anchor as global personality, the breaking news chyron (the moving text bar at the bottom of the screen), the live satellite cross, and the concept of news as competitive entertainment — innovations that have shaped global television news for 40 years and inspired the Fox News, MSNBC, BBC News 24, Al Jazeera, and Sky News models."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's first 24-hour news channel (est. 1 June 1980, Ted Turner, Atlanta); invented cable news concept; 1991 Gulf War — first live televised war, 'CNN effect'; Challenger disaster (1986, only live network); Peter Arnett, Bernard Shaw founding anchors; 24-hour news cycle invention; breaking news chyron; live satellite cross; model for Fox News, MSNBC, BBC News 24, Al Jazeera, Sky News; transformed relationship between real-time media and foreign policy.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Ted Turner's television entrepreneurialism — and his conviction that a 24-hour cable news service could succeed commercially where the established networks' brief evening broadcasts left audiences under-served — drove the founding of CNN against the near-universal scepticism of the broadcasting establishment",
            "The development of cable television infrastructure in the United States (1970s–1980s) — which created the distribution capacity for specialised channels beyond the three major networks — provided the technical platform that made CNN's 24-hour service viable",
            "The 1991 Gulf War's creation of global demand for real-time information about a military conflict covered by embedded journalists with satellite uplinks — which CNN was uniquely positioned to provide — demonstrated CNN's unique value proposition and established the 'CNN effect' as a geopolitical reality"
        ],
        "effects": [
            "The 'CNN effect' — the impact of real-time television coverage on government decision-making — transformed foreign policy by creating public pressure for response to crises that might otherwise be managed quietly; the Rwandan genocide, Somalia, Bosnia, and Kosovo were all shaped by the presence or absence of CNN-era real-time coverage",
            "CNN's 24-hour news cycle created the 'news as entertainment' format that Fox News, MSNBC, and all subsequent cable news operations adopted — transforming news into a competitive attention economy where breaking news, personality-driven anchors, and partisan analysis replaced the objective evening broadcast model",
            "CNN's international expansion — CNN International now reaches 450 million+ households in 200 countries — was the first genuinely global news network, creating a shared information environment for the global elite and establishing English as the de facto language of international television news",
            "The breaking news innovations CNN introduced — the chyron (bottom-of-screen text bar), the live satellite cross, the split screen interview, the 24-hour news anchor format — have been adopted by every television news organisation worldwide, making CNN the primary formal innovator in the history of television journalism"
        ],
        "relationships": [
            {"entity": "Ted Turner (founder, 1 June 1980)", "relationship": "FOUNDED_BY", "note": "Turner's launch of CNN (1980) against universal network scepticism invented the 24-hour news channel and cable news concept"},
            {"entity": "1991 Gulf War (first live televised war, 'CNN effect')", "relationship": "ESTABLISHED_THE_CNN_EFFECT_THROUGH_REAL-TIME_COVERAGE_OF_THE", "note": "CNN's 1991 Gulf War coverage — reporting Baghdad missile strikes live — was the first live televised war and established the 'CNN effect' as a geopolitical reality"},
            {"entity": "Challenger disaster (28 January 1986, only live coverage)", "relationship": "ONLY_NETWORK_WITH_LIVE_COVERAGE_OF_THE", "note": "CNN's live coverage of the Challenger explosion — as the only network present at launch — was the organisation's first major demonstration of the 24-hour news format's advantage"},
            {"entity": "Fox News, MSNBC, Al Jazeera (CNN-model channels)", "relationship": "DIRECT_INSTITUTIONAL_MODEL_FOR", "note": "Fox News, MSNBC, BBC News 24, Al Jazeera, and Sky News all adopted the CNN 24-hour cable news model"},
            {"entity": "CNN International (450 million+ households, 200 countries)", "relationship": "OPERATES_THE_FIRST_GENUINELY_GLOBAL_NEWS_NETWORK_THROUGH", "note": "CNN International — reaching 450 million+ households — was the first genuinely global news network and established English as the de facto language of international television news"}
        ],
    }),

    ("the-guardian", {
        "summary": (
            "The Guardian (est. 1821, Manchester — founded by John Edward Taylor as the Manchester Guardian) is one of the world's most influential liberal newspapers — the British newspaper that broke the phone hacking scandal that destroyed Rupert Murdoch's News of the World (2011), published the Snowden NSA surveillance revelations (2013), co-published the Panama Papers (2016) and Paradise Papers (2018), and maintains an editorial independence protected by the Scott Trust (est. 1936) that prevents it from ever being sold to a commercial owner. The Guardian has 12 million daily readers and is the world's most widely read English-language quality newspaper by digital traffic.\n\n"
            "The Manchester Guardian was founded in 1821 by John Edward Taylor and a group of Manchester merchants who wanted a liberal, Nonconformist voice in the Manchester press in the aftermath of the Peterloo Massacre (1819). Under C.P. Scott's legendary editorship (1872–1929, 57 years), the Manchester Guardian became one of the world's great liberal newspapers — Scott's 1921 centenary essay ('Comment is free, but facts are sacred') established the ethical foundation of liberal journalism. The Guardian moved to London in 1959 and became the Guardian in 1959.\n\n"
            "The Scott Trust — established in 1936 to prevent the Guardian from being sold to commercial or political interests — is the unique institutional structure that has allowed the Guardian to maintain editorial independence against the commercial pressures that have compromised most newspaper proprietors. The Scott Trust's model of a non-profit owner committed to editorial independence has been cited as the ideal structure for public interest journalism in the digital age."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "One of world's most influential liberal newspapers (est. 1821, Manchester Guardian, John Edward Taylor); founded after Peterloo Massacre (1819); C.P. Scott 57-year editorship (1872–1929) — 'Comment is free, but facts are sacred' (1921); Scott Trust (est. 1936, editorial independence structure); phone hacking scandal that destroyed News of the World (2011); Snowden NSA surveillance revelations (2013); Panama Papers (2016); Paradise Papers (2018); 12 million daily readers — world's most widely read English-language quality newspaper by digital traffic.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Peterloo Massacre (1819) — in which Manchester cavalry killed 15 and injured 700 peaceful reform demonstrators — created the political outrage that drove John Edward Taylor and Manchester liberal merchants to found the Manchester Guardian as a voice for Nonconformist liberal opinion against both Tory government repression and radical agitation",
            "C.P. Scott's 57-year editorship (1872–1929) — which combined editorial excellence with moral seriousness, supported Irish Home Rule, women's suffrage, and opposition to the Boer War — established the Guardian's identity as the voice of British liberal conscience, creating the institutional reputation that sustained it through the 20th century",
            "The Scott Trust's establishment (1936) — ensuring the Guardian could never be sold to a commercial or political owner — provided the institutional structure that allowed the Guardian to maintain editorial independence when all its competitors were bought by proprietors with commercial or political agendas"
        ],
        "effects": [
            "The Guardian's phone hacking investigation (2010–2011) — revealing that News of the World journalists had hacked the phones of murder victims, terror victims, and members of the Royal Family — destroyed the 168-year-old News of the World, triggered the Leveson Inquiry into press standards, and permanently damaged Rupert Murdoch's political influence in Britain",
            "The Guardian's publication of Edward Snowden's NSA surveillance revelations (2013) — revealing that the US and UK governments had built a global mass surveillance programme — was the most significant journalism story of the digital age, generating the international debate about digital privacy, government surveillance, and encryption that continues to shape technology policy",
            "The Panama Papers (2016) and Paradise Papers (2018) — collaborative investigations co-published by the Guardian and 400+ news organisations worldwide — revealed the global offshore finance industry that enables tax avoidance by corporations and wealthy individuals, triggering parliamentary investigations, law changes, and public debate about fiscal justice in 50+ countries",
            "C.P. Scott's 'Comment is free, but facts are sacred' (1921) — the clearest statement of the separation between factual reporting and editorial opinion — has become the foundational text of liberal journalism ethics, cited in journalism schools worldwide and embedded in the Guardian's institutional identity"
        ],
        "relationships": [
            {"entity": "Peterloo Massacre (1819, founding catalyst)", "relationship": "FOUNDED_IN_RESPONSE_TO_THE", "note": "The Peterloo Massacre's political outrage drove Taylor and Manchester liberal merchants to found the Manchester Guardian as a voice for Nonconformist liberal opinion"},
            {"entity": "C.P. Scott (editor 1872–1929, 'Comment is free, but facts are sacred')", "relationship": "EDITORIAL_IDENTITY_ESTABLISHED_BY", "note": "Scott's 57-year editorship established the Guardian's identity as the voice of British liberal conscience and produced the foundational text of liberal journalism ethics"},
            {"entity": "Scott Trust (est. 1936, editorial independence structure)", "relationship": "EDITORIALLY_INDEPENDENT_THROUGH_THE", "note": "The Scott Trust — preventing commercial sale — is the unique institutional structure that has allowed the Guardian to maintain editorial independence when competitors were bought by commercial proprietors"},
            {"entity": "Snowden NSA surveillance revelations (2013)", "relationship": "PUBLISHED_THE_MOST_SIGNIFICANT_JOURNALISM_STORY_OF_THE_DIGITAL_AGE", "note": "The Guardian's Snowden revelations — NSA global mass surveillance — generated the international debate about digital privacy and government surveillance that continues to shape technology policy"},
            {"entity": "Panama Papers (2016, 400+ news organisations)", "relationship": "CO-PUBLISHED_THE_LARGEST_COLLABORATIVE_JOURNALISM_PROJECT_IN_HISTORY", "note": "The Panama Papers — co-published by the Guardian and 400+ news organisations — revealed global offshore finance enabling tax avoidance, triggering law changes in 50+ countries"}
        ],
    }),

    ("national-geographic-society", {
        "summary": (
            "The National Geographic Society (NGS, est. 1888, Washington, D.C. — founded by 33 explorers, scientists, and thinkers at the Cosmos Club) is the world's most influential geography and science education organisation — the institution that has published the most widely read science magazine in history (National Geographic, circulation peak 12 million in 1990s), funded 14,000+ scientific expeditions and research projects, and created the visual vocabulary through which the 20th and 21st centuries understand the natural world. The yellow border frame of National Geographic magazine is one of the most recognised visual identities on Earth.\n\n"
            "The National Geographic Society was founded on 27 January 1888 at the Cosmos Club in Washington by 33 men — including Alexander Graham Bell (who would become its second president), Gardiner Greene Hubbard (first president), and explorers, scientists, and government officials — with the mission 'to increase and diffuse geographic knowledge.' The Society began publishing the National Geographic Magazine in October 1888 — initially a dry scientific journal — before transforming under Gilbert Hovey Grosvenor's editorship (1899–1954) into the visually spectacular magazine that became synonymous with exploration, natural history, and the world's cultures.\n\n"
            "National Geographic's photography — the first colour photographs of the American West, the first underwater photographs, the April 1985 'Afghan Girl' cover by Steve McCurry — has created the iconic images through which the world understands geography, wildlife, and human diversity. The Society has funded expeditions including Jacques Cousteau's ocean exploration, Jane Goodall's chimpanzee research, and the discovery of Machu Picchu."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's most influential geography and science education organisation (est. 27 January 1888, Cosmos Club); 33 founders including Alexander Graham Bell; 14,000+ funded expeditions; National Geographic Magazine (12 million circulation peak, 1990s) — most widely read science magazine in history; yellow border — one of world's most recognised visual identities; 'Afghan Girl' cover (April 1985, Steve McCurry); Jacques Cousteau, Jane Goodall, Machu Picchu funded; first colour photos of American West; first underwater photography.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The late 19th century's extraordinary geographical exploration — the scramble for the poles, the mapping of Africa, the exploration of the American West — created both the scientific demand for a geographical learned society and the public appetite for exploration narratives that National Geographic would satisfy",
            "Alexander Graham Bell's transformation of the National Geographic Magazine (under his son-in-law Gilbert Hovey Grosvenor's editorship) from a dry scientific journal into a visually spectacular popular magazine — adding photographs and accessible writing — created the editorial model that made National Geographic the world's most widely read science magazine",
            "The Society's non-profit status and mission-driven funding model — directing membership fees directly into scientific expeditions, research, and education — created the institutional credibility that attracted the world's greatest explorers, scientists, and photographers to associate their work with the National Geographic brand"
        ],
        "effects": [
            "National Geographic's visual journalism — from the first colour photographs of the American West to the 'Afghan Girl' cover (1985) — created the photographic vocabulary through which 20th-century Western audiences understood geography, wildlife, and human diversity, shaping the visual culture of natural history and international understanding",
            "The National Geographic Society's funding of Jane Goodall's chimpanzee research at Gombe (from 1962) — which established the methodology and public profile of primatology — was essential to the breakthrough research that transformed human understanding of animal behaviour and cognition",
            "National Geographic's television channel (est. 1997) — now reaching 450 million+ households in 170 countries — has extended the Society's visual journalism into documentary film, with programmes including 'Cosmos' (Carl Sagan, 1980; Neil deGrasse Tyson, 2014) reaching the largest audiences of any science documentary series in television history",
            "The Society's education programmes — reaching 50 million+ students annually — have established geography, natural history, and cultural diversity as school curriculum subjects, with National Geographic maps, atlases, and educational materials defining how generations of students visualise the world"
        ],
        "relationships": [
            {"entity": "Alexander Graham Bell (second president, editorial transformation)", "relationship": "EDITORIAL_TRANSFORMATION_DRIVEN_BY", "note": "Bell's transformation of the National Geographic Magazine — adding photographs and accessible writing — created the visual journalism model that made it the world's most widely read science magazine"},
            {"entity": "National Geographic Magazine (12 million circulation peak)", "relationship": "PUBLISHES_THE", "note": "National Geographic Magazine — with its yellow border and 12 million circulation peak — is the most widely read science magazine in history and one of the world's most recognised visual brands"},
            {"entity": "Jane Goodall (Gombe chimpanzee research, funded by NGS)", "relationship": "FUNDED_THE_BREAKTHROUGH_PRIMATOLOGY_RESEARCH_OF", "note": "NGS funding of Goodall's Gombe research (from 1962) was essential to the breakthrough work that transformed human understanding of primate behaviour and cognition"},
            {"entity": "'Afghan Girl' (Steve McCurry, April 1985 cover)", "relationship": "PUBLISHED_THE_MOST_ICONIC_MAGAZINE_COVER_IN_SCIENCE_JOURNALISM_HISTORY", "note": "Steve McCurry's 'Afghan Girl' (1985) — the most reproduced magazine cover in history — exemplifies National Geographic's visual journalism at its most impactful"},
            {"entity": "Jacques Cousteau (ocean exploration, funded by NGS)", "relationship": "FUNDED_AND_PROMOTED_THE_OCEAN_EXPLORATION_WORK_OF", "note": "NGS funding and publication of Cousteau's ocean exploration brought the underwater world to public consciousness and established marine biology as a public science"}
        ],
    }),

    ("nature-portfolio", {
        "summary": (
            "Nature Portfolio (formerly Nature Publishing Group, est. 1869, London — founded by Norman Lockyer) is the world's most prestigious scientific publisher — the publisher of Nature (the world's most cited scientific journal, with an impact factor of 64.8), Nature Medicine, Nature Genetics, Nature Climate Change, and 60+ specialist journals that represent the pinnacle of scientific peer review and publication. A paper in Nature or its sister journals is the highest status achievement in scientific publishing; Nature's peer review and editorial selection processes are the de facto quality control system for the most important scientific discoveries of each generation.\n\n"
            "Nature was founded in 1869 by Norman Lockyer — a solar spectroscopist who co-discovered helium and became the magazine's first editor (40 years) — with the mission 'to place before the general public the grand results of scientific work and scientific discovery.' Nature has published the papers describing the discovery of the structure of DNA (Watson and Crick, 25 April 1953), the first papers on HIV (1983), the cloning of Dolly the sheep (1997), the first draft of the human genome (2001), and the detection of gravitational waves (2016).\n\n"
            "Nature's impact factor (64.8) — the average number of times each paper is cited in the two years following publication — is the highest of any multidisciplinary science journal, making a Nature publication the most influential single act in the career of most research scientists. Nature's influence on scientific priorities, funding decisions, and public understanding of science is immeasurable."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's most prestigious scientific publisher (est. 1869, Norman Lockyer); Nature — world's most cited scientific journal (impact factor 64.8); published Watson and Crick DNA double helix (25 April 1953); HIV discovery (1983); Dolly the sheep cloning (1997); first draft of human genome (2001); detection of gravitational waves (2016); 60+ specialist journals; peer review as de facto quality control for most important scientific discoveries; Nature publication = highest status achievement in scientific career.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Norman Lockyer's founding vision (1869) — that a general scientific journal could communicate 'the grand results of scientific work' to an educated public and to scientists working across disciplines — created the editorial model that distinguished Nature from purely specialist journals",
            "The 20th century's accelerating pace of scientific discovery — and the need for a high-prestige, peer-reviewed publication that could validate and publicise the most important findings across all scientific disciplines — created the demand for exactly the editorial model Nature had established",
            "The competitive dynamics of scientific careers — in which publication in high-impact journals determines research funding, academic appointments, and professional recognition — created the status economy in which a Nature publication became the primary marker of scientific excellence"
        ],
        "effects": [
            "The publication of Watson and Crick's DNA double helix paper (25 April 1953, Nature, vol. 171, p. 737) — the most consequential single scientific publication of the 20th century — established Nature as the journal of record for the most important scientific discoveries and demonstrated the power of peer review to validate transformative research",
            "Nature's impact factor system — measuring a journal's influence by the average citations per paper — has driven the 'publish or perish' culture of modern academic science, creating both the incentive for high-quality research and the perverse incentive for high-profile findings that replication studies have often failed to confirm",
            "Nature's editorial selection process — accepting less than 8% of submitted papers — has made it the primary quality filter for the most important scientific discoveries, giving Nature's editors disproportionate influence over the direction of scientific research and public understanding of scientific progress",
            "Nature's open access and data sharing policies — which Nature championed early — have shaped the global movement toward open science, accelerating the pace of scientific discovery by making research findings freely available and reproducible"
        ],
        "relationships": [
            {"entity": "Norman Lockyer (founder and first editor 1869–1919, 40 years)", "relationship": "FOUNDED_AND_SHAPED_BY", "note": "Lockyer's 40-year editorship established Nature's mission and editorial model — communicating grand scientific results to an educated public and across disciplines"},
            {"entity": "Watson and Crick DNA double helix (25 April 1953, Nature)", "relationship": "PUBLISHED_THE_MOST_CONSEQUENTIAL_SCIENTIFIC_PAPER_OF_THE_20TH_CENTURY", "note": "The Watson-Crick DNA paper (1953) — the most consequential scientific publication of the 20th century — established Nature as the journal of record for transformative discoveries"},
            {"entity": "Impact factor system (Nature's primary quality metric)", "relationship": "PRIMARY_INSTITUTION_IN_THE_DEVELOPMENT_OF_THE", "note": "Nature's impact factor — measuring citations per paper — has driven the 'publish or perish' culture of modern academic science, shaping scientific career incentives worldwide"},
            {"entity": "Gravitational waves detection (2016, LIGO team)", "relationship": "PUBLISHED_THE_PRIMARY_ANNOUNCEMENT_OF_THE", "note": "Nature's publication of the gravitational wave detection (2016) — one of the most consequential experimental physics results in history — demonstrated its continuing role as the journal of record for transformative discoveries"},
            {"entity": "Human Genome Project first draft (2001, Nature consortium)", "relationship": "CO-PUBLISHED_THE_FIRST_DRAFT_OF_THE", "note": "Nature published the public consortium's first draft of the human genome (2001) — the most comprehensive biological sequence data then assembled, establishing the foundation of genomic medicine"}
        ],
    }),

    ("bbc-radio", {
        "summary": (
            "BBC Radio (est. 1922, London — the broadcasting service of the British Broadcasting Corporation) is the world's oldest and most influential national radio broadcaster — the organisation that established the public service broadcasting model, invented the documentary format, created the concept of the radio drama, and has produced 100 years of cultural, educational, and journalistic broadcasting that has shaped British and global culture. The BBC's World Service (est. 1932) — broadcasting in 42 languages to 350 million listeners weekly — is the world's largest international broadcaster and the primary source of independent news for populations living under authoritarian governments.\n\n"
            "The BBC was founded on 18 October 1922 as the British Broadcasting Company — a consortium of radio manufacturers — before being reconstituted as the British Broadcasting Corporation (chartered 1927) under its first Director-General John Reith, who established the BBC's foundational mission: 'to inform, educate, and entertain.' Reith's insistence that the BBC should serve the entire population equally — not just entertainment-seeking commercial audiences — established public service broadcasting as an institutional principle that has influenced broadcasting in every democracy.\n\n"
            "BBC Radio's cultural achievements include the invention of the radio documentary (Hilda Matheson), the radio drama (Lance Sieveking), BBC Radio 4's 'The Archers' (the world's longest-running radio drama, since 1951), and Radio 1's role in the development of British popular music culture (introducing punk, indie, rave, and grime to mass audiences). The BBC World Service's broadcasts to Nazi-occupied Europe during WWII were described by Winston Churchill as 'among our most potent weapons.'"
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's oldest and most influential national radio broadcaster (est. 18 October 1922); John Reith 'inform, educate, entertain' public service broadcasting principle; BBC World Service (est. 1932, 42 languages, 350 million weekly listeners) — world's largest international broadcaster; primary independent news source for authoritarian-governed populations; WWII broadcasts to Nazi-occupied Europe — Churchill 'most potent weapons'; The Archers (world's longest-running radio drama, since 1951); Radio 1 — British popular music culture; public service broadcasting model adopted worldwide.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "John Reith's founding vision — that broadcasting should serve the entire population equally, providing education and culture alongside entertainment, and that commercial considerations should not dictate programming — established the public service broadcasting principle that distinguished the BBC from the American commercial model",
            "The British government's decision to charter the BBC as a public corporation funded by the licence fee (1927) — rather than allowing commercial advertising — created the financial model that enabled the BBC to pursue public interest programming without commercial pressure",
            "WWII's creation of the demand for trustworthy international broadcasting — as an alternative to Nazi propaganda for occupied European populations — gave the BBC World Service its unique historical role as the world's most trusted international broadcaster, a reputation that has sustained it for 90 years"
        ],
        "effects": [
            "The BBC's public service broadcasting model — 'to inform, educate, and entertain' without commercial pressure — has been adopted by public broadcasters in 50+ countries (CBC, ABC Australia, France Télévisions, ARD, NHK, etc.), establishing the institutional template for democratic public media worldwide",
            "The BBC World Service's broadcasts to authoritarian states — from Nazi-occupied Europe to the Soviet bloc to contemporary authoritarian countries — have been the primary source of independent international news for 90 years, making the BBC a primary instrument of democratic information against authoritarian information control",
            "BBC Radio 4 — with its unique combination of news analysis (Today programme), drama (The Archers), arts (Front Row), documentary (In Our Time), and comedy (I'm Sorry I Haven't a Clue) — has been the primary cultural influence on the intellectual and cultural identity of educated British adults for 80 years",
            "The BBC's investment in British music — from BBC Radio 1's 1960s launch (making British pop accessible to all) to Radio 6 Music's championing of alternative music — has been a major driver of British popular music culture, with BBC sessions and chart shows shaping the careers of the Beatles, David Bowie, punk, Britpop, and grime"
        ],
        "relationships": [
            {"entity": "John Reith (first Director-General, 'inform, educate, entertain')", "relationship": "PUBLIC_SERVICE_BROADCASTING_PRINCIPLE_ESTABLISHED_BY", "note": "Reith's founding vision — serving the entire population equally without commercial pressure — established the public service broadcasting model adopted by 50+ countries worldwide"},
            {"entity": "BBC World Service (est. 1932, 42 languages, 350 million listeners)", "relationship": "OPERATES_THE_WORLD'S_LARGEST_INTERNATIONAL_BROADCASTER_THROUGH_THE", "note": "The BBC World Service — broadcasting to 350 million listeners in 42 languages — is the world's most trusted international broadcaster and primary independent news source for populations under authoritarian rule"},
            {"entity": "WWII broadcasts to Nazi-occupied Europe (Churchill 'potent weapons')", "relationship": "SERVED_AS_PRIMARY_INFORMATION_WEAPON_AGAINST_NAZI_OCCUPATION_THROUGH_ITS", "note": "Churchill's description of BBC broadcasts as 'among our most potent weapons' reflects the BBC's unique role as a trusted information source in Nazi-occupied Europe"},
            {"entity": "The Archers (world's longest-running radio drama, since 1951)", "relationship": "PRODUCES_THE", "note": "The Archers — the world's longest-running radio drama (since 1951) — is the BBC's most durable cultural achievement and a unique social document of British rural life"},
            {"entity": "Public service broadcasting model (adopted worldwide)", "relationship": "CREATED_AND_PRIMARY_MODEL_FOR_THE", "note": "The BBC's public service broadcasting model — 'inform, educate, entertain' without commercial pressure — has been adopted by public broadcasters in 50+ countries"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 38 — {len(ENTITIES)} entities (Class 364: Major Media & Press Institutions)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
