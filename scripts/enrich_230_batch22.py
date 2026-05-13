#!/usr/bin/env python3
"""
Batch 22 — 8 entities: Monty Wilkinson, Paul S. Atkins, James Oladipo Williams,
Afrasiab Khattak, Rose Mwebaza, Salamatu Hussaini Suleiman, Seodi White, Alice Rwema
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/230-Class-230"
EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()


def enrich_entity(slug, data):
    fname = os.path.join(FOLDER, f"230{slug}.json")
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
    print(f"  ✓ {entity['name']} — sum={slen}c c={len(det.get('causes',[]))} "
          f"e={len(det.get('effects',[]))}")


ENTITIES = [

    # 1 — Monty Wilkinson
    ("monty-wilkinson", {
        "summary": (
            "Robert Montague 'Monty' Wilkinson is an American career lawyer who spent his "
            "entire professional life at the United States Department of Justice, rising from "
            "line attorney to the highest appointed position in the department when he served "
            "as Acting United States Attorney General from January 20 to March 11, 2021 — "
            "the fifty-one days between the Trump administration's end and the Senate "
            "confirmation of Merrick Garland as the Biden administration's permanent Attorney "
            "General. His brief tenure as acting head of the nation's premier law enforcement "
            "agency placed him at the apex of American federal law enforcement at an "
            "extraordinarily consequential moment: the immediate aftermath of the January 6, "
            "2021 storming of the US Capitol.\n\n"
            "Wilkinson's career represents the archetype of the career DOJ professional — the "
            "category of lawyer who serves across multiple administrations and provides "
            "institutional continuity in an agency where political appointees cycle through "
            "in four-to-eight-year windows. His role as Director of the Executive Office "
            "for United States Attorneys (EOUSA) — which he held from 2021 to 2023 — was "
            "perhaps even more institutionally significant than the brief acting AG tenure: "
            "the EOUSA manages the operations, budgets, and coordination of the ninety-four "
            "United States Attorney's offices that constitute the front line of federal "
            "prosecution across the country.\n\n"
            "The January 2021 transition was legally and politically fraught. He inherited "
            "an acting role in the context of the ongoing January 6 investigation — the "
            "largest criminal prosecution effort in American history — the conclusion of "
            "the Trump-era political conflicts over DOJ independence, and the need to "
            "stabilize an institution that had been destabilized by the previous "
            "administration's political pressures on federal prosecutors.\n\n"
            "His career illustrates the critical importance of career civil servants "
            "in maintaining institutional continuity within agencies where political "
            "leadership changes, conflicts, and crises can undermine the regular "
            "administration of justice."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Career DOJ lawyer who served as Acting US Attorney General (January 20 – March 11, 2021) during the Biden-Trump transition, overseeing the DOJ at the moment of the January 6 Capitol attack investigation's launch; later Director of EOUSA (2021–2023).",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Trump-Biden transition's institutional disruption — including the firing of the acting AG Jeff Rosen days before Trump left office — created the circumstances in which Wilkinson's acting appointment became the critical bridge to the Garland confirmation",
            "His decades-long career at DOJ built the institutional knowledge and credibility that made him a trusted choice for the acting role during an extraordinarily sensitive political moment",
            "The January 6, 2021 Capitol attack — which occurred on his first day as acting AG — immediately defined the agenda of his brief tenure as the largest criminal prosecution effort in American history was launched"
        ],
        "effects": [
            "His 51-day acting tenure provided institutional continuity at DOJ during the politically sensitive Biden-Trump transition and the launch of the January 6 investigation",
            "His subsequent EOUSA directorship shaped the management and operations of all 94 US Attorney's offices — the front line of federal prosecution — across his tenure",
            "The stability he provided helped prevent further political erosion of DOJ independence during the critical early days of the Biden administration",
            "His career illustrates the critical role of career civil servants in maintaining institutional continuity and professional standards in political institutions"
        ],
        "relationships": [
            {"entity": "United States Department of Justice", "relationship": "CAREER_SPENT_AT", "note": "Entire professional career spent at DOJ, rising to Acting Attorney General and EOUSA Director"},
            {"entity": "January 6, 2021 Capitol attack investigation", "relationship": "OVERSAW_LAUNCH_OF", "note": "Was Acting AG on January 20, 2021 — the investigation's key early phase was launched during his tenure"},
            {"entity": "Merrick Garland", "relationship": "PRECEDED_AS_ACTING_AG", "note": "Served as acting AG until Garland was confirmed by the Senate on March 10, 2021"},
            {"entity": "Executive Office for United States Attorneys (EOUSA)", "relationship": "DIRECTED", "note": "Director of EOUSA 2021–2023 — managing the operations and coordination of 94 US Attorney offices"},
            {"entity": "Biden administration DOJ transition", "relationship": "MANAGED", "note": "His acting tenure was the critical bridge period between Trump administration DOJ leadership and Biden's permanent AG"}
        ]
    }),

    # 2 — Paul S. Atkins
    ("paul-s-atkins", {
        "summary": (
            "Paul Stewart Atkins (b. 1958) is an American securities law attorney and financial "
            "regulator who has served twice in leadership positions at the US Securities and "
            "Exchange Commission: as a commissioner from 2002 to 2008 under President George "
            "W. Bush, and as Chair of the SEC since April 2025 under President Donald Trump — "
            "the latter appointment making him the first SEC chair with a strongly pro-crypto "
            "orientation and signaling a dramatic shift in US digital asset regulatory policy "
            "away from the aggressive enforcement approach of his predecessor Gary Gensler. "
            "A lifelong advocate of free-market principles and reduced regulatory burdens, "
            "his career has spanned securities law practice, SEC regulation, and financial "
            "regulatory consulting.\n\n"
            "During his first SEC tenure (2002–2008), Atkins was the most consistently "
            "dissenting commissioner — voting against numerous enforcement actions and "
            "rulemaking proposals that he considered to exceed the SEC's mandate or "
            "impose excessive costs on markets. His free-market philosophy led him to "
            "oppose many post-Enron Sarbanes-Oxley regulatory requirements as burdensome, "
            "positioning him as the voice of deregulatory conservatism on the commission "
            "during the George W. Bush era. After leaving the SEC in 2008, he founded "
            "Patomak Global Partners, a Washington-based financial regulatory consultancy "
            "that represented financial industry clients before federal regulators.\n\n"
            "His 2025 appointment as SEC Chair came at a moment when the cryptocurrency "
            "and digital asset industry was seeking relief from the Gensler-era enforcement "
            "actions that had treated most cryptocurrencies as unregistered securities. "
            "Atkins's known sympathy for digital assets — and his consultancy's past work "
            "with cryptocurrency clients — made his appointment the clearest possible signal "
            "of a policy reversal. His chairing of the SEC in the Trump second term "
            "represented a fundamental re-orientation of American securities regulation.\n\n"
            "His career illustrates the pendulum of American financial regulatory philosophy "
            "between deregulatory free-market conservatism and activist investor-protection "
            "enforcement."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "SEC Commissioner (2002–2008) and SEC Chair (2025–present); the most prominent advocate of free-market deregulatory philosophy in US securities law; his 2025 appointment as SEC chair marked a fundamental shift in US cryptocurrency regulatory policy.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The George W. Bush administration's commitment to deregulatory principles led to Atkins's first SEC appointment, where his dissenting votes expressed the free-market philosophy that the administration favored",
            "The Trump administration's second-term commitment to a crypto-friendly regulatory environment — reflecting the political significance of cryptocurrency advocacy — led directly to his 2025 appointment as SEC chair",
            "The cryptocurrency industry's multi-year legal battle against Gensler-era SEC enforcement actions created intense political pressure for a regulatory pivot that Atkins's appointment provided"
        ],
        "effects": [
            "His 2002–2008 SEC tenure established him as the most consistent voice for deregulatory conservatism on the commission, influencing the internal debate over Sarbanes-Oxley implementation",
            "His founding of Patomak Global Partners created a major financial regulatory consultancy that shaped regulatory strategy for financial industry clients across two administrations",
            "His 2025 appointment as SEC Chair initiated a fundamental reversal of US digital asset regulatory enforcement policy — withdrawing or settling many of the Gensler-era cryptocurrency enforcement actions",
            "His chairmanship represents a broader philosophical shift in American securities regulation toward reduced enforcement, lighter regulatory touch, and crypto-sector accommodation"
        ],
        "relationships": [
            {"entity": "US Securities and Exchange Commission (SEC)", "relationship": "COMMISSIONER_AND_CHAIR_OF", "note": "SEC Commissioner 2002–2008; SEC Chair from April 2025"},
            {"entity": "Gary Gensler (SEC Chair 2021–2025)", "relationship": "SUCCEEDED", "note": "Succeeded Gensler as SEC Chair, dramatically reversing Gensler's aggressive cryptocurrency enforcement approach"},
            {"entity": "Patomak Global Partners", "relationship": "FOUNDED", "note": "Founded Patomak Global Partners after leaving the SEC in 2008 — a financial regulatory consultancy that represented crypto and financial industry clients"},
            {"entity": "Cryptocurrency / digital asset industry", "relationship": "ADVOCATES_FOR", "note": "His 2025 SEC chairmanship was the clearest signal of a US regulatory pivot toward crypto industry accommodation"},
            {"entity": "Sarbanes-Oxley Act (2002)", "relationship": "DISSENTED_FROM_IMPLEMENTATION_OF", "note": "As SEC Commissioner, voted against many Sarbanes-Oxley implementation rules he considered excessively burdensome"}
        ]
    }),

    # 3 — James Oladipo Williams
    ("james-oladipo-williams", {
        "summary": (
            "James Oladipo Williams was a Nigerian jurist who served as a judge of the High "
            "Court of Lagos State from June 1, 1975 to his retirement on May 22, 1987 — "
            "a twelve-year judicial career during which he presided over some of the most "
            "consequential civil and commercial litigation in one of Africa's most dynamic "
            "legal jurisdictions. Lagos State's High Court — the principal trial court "
            "of Nigeria's commercial and financial capital — handled the full range of "
            "civil, commercial, criminal, and family law matters that arose from the "
            "enormous economic activity of Lagos, West Africa's largest city and "
            "Nigeria's commercial heart.\n\n"
            "Williams's judicial tenure began under the military government of General "
            "Murtala Muhammed and continued through the administrations of Olusegun "
            "Obasanjo, Shehu Shagari's Second Republic, the military government of "
            "Muhammadu Buhari, and into the early Babangida era — a period of enormous "
            "political turbulence in Nigerian history. Serving as a judge through "
            "multiple government changes tested judicial independence and required "
            "a commitment to legal professionalism that transcended political loyalty.\n\n"
            "His most remarkable legacy is familial: he is the father of Ayotunde Phillips, "
            "the 14th Chief Judge of Lagos State, and of Oluwafunmilayo Olajumoke Atilade, "
            "the 15th Chief Judge of Lagos State — a consecutive parent-and-two-children "
            "judicial dynasty that is extraordinarily rare in any legal system's history. "
            "Both daughters followed him into the law, rose through the Lagos State judiciary, "
            "and consecutively occupied the highest judicial position in Nigeria's most "
            "commercially significant state — a remarkable testament to a legal family "
            "tradition that he established.\n\n"
            "His career as judge and his daughters' achievement as Lagos Chief Judges "
            "represent three judicial generations of the Williams family's contribution "
            "to Nigerian legal life."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Lagos State High Court judge (1975–1987) and father of both the 14th and 15th Chief Judges of Lagos State — a consecutive judicial dynasty across two daughters that is extraordinarily rare in the history of any legal system.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Nigeria's post-independence legal system's need for trained judges in Lagos — the commercial capital — created the institutional context for Williams's appointment",
            "The Nigerian judicial tradition of elevating experienced lawyers to the bench — drawing from the bar's most distinguished practitioners — provided the professional pathway for his judicial career",
            "His own example and legal training provided the professional environment in which both his daughters developed their legal careers and eventually reached the pinnacle of the Lagos judiciary"
        ],
        "effects": [
            "His twelve-year judicial tenure shaped Lagos State High Court jurisprudence across a turbulent period of Nigerian political history — serving through multiple military and civilian governments",
            "The 14th and 15th Chief Judges of Lagos State (Ayotunde Phillips and Oluwafunmilayo Atilade) are his daughters — a consecutive judicial dynasty of extraordinary historical rarity",
            "His family's legal legacy represents a three-generation contribution to Nigerian judicial life — his own judgeship and his daughters' Chief Judgeships",
            "His career illustrated the possibilities of judicial professionalism during periods of Nigerian military rule — maintaining the independence and regularity of legal proceedings through political upheaval"
        ],
        "relationships": [
            {"entity": "Lagos State High Court", "relationship": "SERVED_AS_JUDGE_OF", "note": "Judge of the High Court of Lagos State from June 1, 1975 to May 22, 1987"},
            {"entity": "Ayotunde Phillips", "relationship": "FATHER_OF", "note": "Father of Ayotunde Phillips — the 14th Chief Judge of Lagos State"},
            {"entity": "Oluwafunmilayo Olajumoke Atilade", "relationship": "FATHER_OF", "note": "Father of Oluwafunmilayo Olajumoke Atilade — the 15th Chief Judge of Lagos State"},
            {"entity": "Lagos State judiciary", "relationship": "PART_OF_DYNASTY_IN", "note": "He and his two daughters (14th and 15th Lagos Chief Judges) constitute one of Nigeria's most remarkable legal dynasties"},
            {"entity": "Military Nigeria (1975–1987)", "relationship": "SERVED_UNDER", "note": "His judicial career spanned multiple Nigerian military governments — beginning under Murtala Muhammed and extending into the Babangida era"}
        ]
    }),

    # 4 — Afrasiab Khattak
    ("afrasiab-khattak", {
        "summary": (
            "Afrasiab Khattak (b. 1949) is a Pakistani secular Pashtun nationalist politician, "
            "socialist intellectual, and human rights activist who has spent his career "
            "advocating for the rights of Pakistan's Pashtun minority, defending civil "
            "liberties in one of the world's most security-focused states, and articulating "
            "a secular, progressive political vision for Pakistan's northwest that stands in "
            "direct opposition to both the Pakistani military establishment's security-driven "
            "political culture and the Islamist politics that have dominated parts of "
            "Khyber Pakhtunkhwa. He was a senior leader of the Awami National Party (ANP) "
            "— Pakistan's secular Pashtun nationalist party — and has served as Chair of the "
            "Human Rights Commission of Pakistan (HRCP) and as a Senator (2009–2014).\n\n"
            "Khattak's political identity was formed in opposition to Pakistani military "
            "authoritarianism and the establishment's policy of supporting Islamist "
            "political forces as a counterweight to secular Pashtun nationalism — a "
            "policy that, in his analysis, contributed directly to the rise of the "
            "Taliban in Afghanistan and the spread of extremism in Khyber Pakhtunkhwa. "
            "He has been a consistent critic of Pakistan's Inter-Services Intelligence "
            "and the military's interference in civilian politics, a stance that has "
            "made him a target of both establishment pressure and, during the Taliban's "
            "peak violence years, of Islamist violence.\n\n"
            "As Chair of the Human Rights Commission of Pakistan — Pakistan's most "
            "respected civil society human rights organization — he used the position "
            "to document enforced disappearances, extrajudicial killings, torture, "
            "and the persecution of religious minorities and journalists. His Senate "
            "service provided a platform for these concerns in the national legislature.\n\n"
            "His intellectual contributions — as a political analyst writing extensively "
            "on Pashtun nationalism, security policy, and democratic politics in South "
            "Asia — have made him one of the most significant progressive voices from "
            "Pakistan's northwestern frontier."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Pakistani secular Pashtun nationalist leader, Chair of the Human Rights Commission of Pakistan, and Senator (2009–2014); a leading intellectual critic of Pakistan's military establishment and a persistent advocate for civil liberties and minority rights.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Pakistani military's instrumentalization of Islamist political forces against secular Pashtun nationalism — creating the Taliban and fueling extremism in Khyber Pakhtunkhwa — drove Khattak's career as a critic of security-state politics",
            "Pakistan's pattern of enforced disappearances, extrajudicial killings, and persecution of journalists and activists created the human rights advocacy agenda that he pursued through the HRCP and his political career",
            "The Pashtun people's positioning between Pakistani state control and Afghan conflict — with Pashtun communities on both sides of the Durand Line suffering from the War on Terror — created the nationalist political cause he championed"
        ],
        "effects": [
            "His HRCP chairmanship documented Pakistan's human rights violations — enforced disappearances, torture, minority persecution — building the evidentiary record that international human rights organizations depend on",
            "His Senate service (2009–2014) provided a platform for Pashtun rights and secular democratic politics in the national legislature",
            "His intellectual critiques of the Pakistani military establishment's security policies have influenced Pakistani civil society and international understanding of the region's political dynamics",
            "The ANP's secular Pashtun nationalism, to which he contributed a significant intellectual voice, has represented a persistent alternative to both the military establishment and Islamist politics in KPK"
        ],
        "relationships": [
            {"entity": "Awami National Party (ANP)", "relationship": "SENIOR_LEADER_OF", "note": "Senior leader of the ANP — Pakistan's secular Pashtun nationalist party"},
            {"entity": "Human Rights Commission of Pakistan (HRCP)", "relationship": "FORMER_CHAIR_OF", "note": "Former Chair of the HRCP — Pakistan's most respected civil society human rights organization"},
            {"entity": "Senate of Pakistan", "relationship": "FORMER_MEMBER_OF", "note": "Senator from Khyber Pakhtunkhwa (2009–2014)"},
            {"entity": "Pakistan Inter-Services Intelligence (ISI)", "relationship": "PERSISTENT_CRITIC_OF", "note": "A persistent critic of the ISI and military establishment's interference in civilian politics and support for Islamist forces"},
            {"entity": "Taliban (Afghan)", "relationship": "DOCUMENTED_ORIGINS_OF", "note": "Has argued that Pakistan's establishment's Islamist-support policies directly contributed to the Taliban's rise — a controversial but influential analysis"}
        ]
    }),

    # 5 — Rose Mwebaza
    ("rose-mwebaza", {
        "summary": (
            "Rose Mwebaza is a Ugandan lawyer and international environmental law expert "
            "who serves as the Director of the Climate Technology Centre & Network (CTCN) "
            "— the United Nations-backed implementation arm of the UNFCCC Technology "
            "Mechanism — a position that places her at the center of the global effort "
            "to accelerate the deployment of clean technologies in developing countries "
            "as part of the world's response to climate change. The CTCN, co-hosted by "
            "the UN Environment Programme (UNEP) and the UN Industrial Development "
            "Organization (UNIDO) in Copenhagen, serves as the practical delivery vehicle "
            "for the technology transfer commitments made by developed countries under "
            "the UN Framework Convention on Climate Change.\n\n"
            "Mwebaza's legal and policy expertise is in environmental law, climate "
            "change governance, and sustainable development — areas where she has "
            "worked both at the national level in Uganda and at the international "
            "level in UN agencies. Her appointment to lead the CTCN represents the "
            "promotion of an African lawyer to the directorship of a major international "
            "climate institution — a significant moment in the diversification of "
            "global environmental governance leadership.\n\n"
            "The CTCN's mandate is to respond to technology-related requests from "
            "developing countries — providing technical assistance to design, deploy, "
            "and scale clean energy, climate adaptation, and low-carbon technologies "
            "appropriate to specific national contexts. This work spans from solar "
            "energy deployment and energy efficiency to climate-resilient agriculture "
            "and sustainable urban infrastructure, making the CTCN a key institution "
            "in the practical implementation of the Paris Agreement's technology goals.\n\n"
            "Her role also connects to UNEP's regional activities in Africa, where "
            "she has been engaged since 2023 — contributing to the environmental "
            "governance capacity of African states that are among the most climate-vulnerable "
            "in the world while being least responsible for the emissions that caused "
            "the crisis."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Ugandan lawyer and Director of the UN Climate Technology Centre & Network (CTCN) — the UNFCCC Technology Mechanism's implementation arm; a leading African environmental law expert in global climate governance.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Paris Agreement's technology transfer commitments created the institutional mandate for the CTCN — and the need for leadership that combined environmental law expertise with international development experience",
            "The UNFCCC Technology Mechanism's need for leadership that understood both the technical dimensions of climate technology and the legal and governance frameworks of developing countries shaped her qualification profile",
            "The growing international recognition that African leadership in global environmental institutions was both symbolically important and substantively valuable created the context for her appointment"
        ],
        "effects": [
            "Her leadership of the CTCN directs technical climate technology assistance to developing countries — enabling the practical technology deployment that makes the Paris Agreement's ambitions actionable",
            "As an African director of a major climate institution, she contributes to the diversification of global environmental governance leadership and to the representation of climate-vulnerable African perspectives",
            "Her UNEP regional engagement in Africa supports the environmental governance capacity of African states in the critical decade for climate action",
            "The CTCN's work under her leadership creates the institutional infrastructure through which the world's most climate-vulnerable countries can access the technologies they need for both mitigation and adaptation"
        ],
        "relationships": [
            {"entity": "Climate Technology Centre & Network (CTCN)", "relationship": "DIRECTS", "note": "Director of the CTCN — the UNFCCC Technology Mechanism's implementation arm, co-hosted by UNEP and UNIDO in Copenhagen"},
            {"entity": "UN Environment Programme (UNEP)", "relationship": "AFFILIATED_WITH", "note": "Also serves with UNEP's regional office for Africa since 2023"},
            {"entity": "UNFCCC Technology Mechanism", "relationship": "IMPLEMENTS", "note": "The CTCN she leads is the implementation arm of the UNFCCC Technology Mechanism, translating climate technology commitments into practical assistance"},
            {"entity": "Paris Agreement (2015)", "relationship": "IMPLEMENTS_TECHNOLOGY_PROVISIONS_OF", "note": "The CTCN's work implements the Paris Agreement's technology transfer and development commitments"},
            {"entity": "Developing country climate technology", "relationship": "FACILITATES", "note": "Her role involves providing technical assistance for clean technology deployment in climate-vulnerable developing countries"}
        ]
    }),

    # 6 — Salamatu Hussaini Suleiman
    ("salamatu-hussaini-suleiman", {
        "summary": (
            "Dr. Salamatu Hussaini Suleiman is a Nigerian lawyer, public administrator, "
            "and policy expert who has held some of the most consequential positions in "
            "West African regional governance, including serving as Commissioner for "
            "Political Affairs, Peace and Security at the Economic Community of West "
            "African States (ECOWAS) Commission from 2012 to 2016 — becoming the first "
            "woman to hold this portfolio, which oversees the most politically sensitive "
            "aspects of ECOWAS's work: conflict prevention, election monitoring, "
            "peacekeeping operations, and the mediation of political crises across "
            "West Africa's fifteen member states.\n\n"
            "Suleiman's career combines legal training with high-level public administration "
            "in Nigeria and at the regional ECOWAS level. She held two ministerial "
            "appointments in the Federal Government of Nigeria — positions in which she "
            "developed the policy experience in governance, security, and administration "
            "that prepared her for the ECOWAS role. Her appointment to the ECOWAS Commission "
            "reflected both Nigeria's dominant role in West African regional organization "
            "(as the largest economy and most powerful military in the region) and her "
            "personal professional qualifications.\n\n"
            "The ECOWAS Commissioner for Political Affairs, Peace and Security oversees "
            "the organization's most demanding work — deploying the ECOWAS Monitoring "
            "Group (ECOMOG) in peacekeeping roles, coordinating election observation "
            "missions, mediating coups and political crises (as occurred in several "
            "West African states during and after her tenure), and maintaining the "
            "regional diplomatic architecture that has been central to West African "
            "conflict resolution since the 1990s.\n\n"
            "Her career as a first — the first woman in the ECOWAS Political Affairs "
            "Commissioner role — placed her at the intersection of gender advancement "
            "and African regional governance at a critical moment in West Africa's "
            "political development."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Nigerian lawyer and first woman Commissioner for Political Affairs, Peace and Security at ECOWAS (2012–2016); oversaw conflict prevention, peacekeeping, and political crisis mediation across West Africa's fifteen member states.",
            "significanceCategory": "continental"
        },
        "causes": [
            "ECOWAS's role as West Africa's primary regional conflict management organization — tested by civil wars, coups, and political crises — created the institutional demand for the Political Affairs, Peace and Security Commissioner portfolio she occupied",
            "Nigeria's dominance in ECOWAS governance — reflecting its weight as the largest economy and military power — made the appointment of a Nigerian to a senior ECOWAS role a predictable outcome of regional political dynamics",
            "Her prior ministerial experience in Nigeria's Federal Government provided the administrative and policy credentials that qualified her for the ECOWAS Commission appointment"
        ],
        "effects": [
            "As the first woman to hold the ECOWAS Political Affairs, Peace and Security portfolio, she set a precedent for women's leadership in West African regional security governance",
            "Her four-year ECOWAS tenure (2012–2016) coincided with a period of significant West African political turbulence — including the Mali coup (2012), the Burkina Faso crisis, and Gambian political transition — requiring active regional diplomatic engagement",
            "Her career model of the Nigerian lawyer-minister who moves into regional African governance contributed to the pattern of Nigerian professionals leading West African institutional organizations",
            "Her ECOWAS service strengthened Nigeria's engagement with regional conflict prevention mechanisms during a period of elevated security challenges"
        ],
        "relationships": [
            {"entity": "ECOWAS Commission", "relationship": "COMMISSIONER_AT", "note": "Commissioner for Political Affairs, Peace and Security at the ECOWAS Commission (2012–2016)"},
            {"entity": "ECOWAS (Economic Community of West African States)", "relationship": "SERVED", "note": "First woman to hold the Political Affairs, Peace and Security portfolio at ECOWAS — overseeing conflict prevention, peacekeeping, and political mediation"},
            {"entity": "Federal Government of Nigeria", "relationship": "FORMER_MINISTER_IN", "note": "Held two ministerial appointments in the Federal Government of Nigeria before her ECOWAS role"},
            {"entity": "ECOMOG (ECOWAS Monitoring Group)", "relationship": "OVERSAW", "note": "The Political Affairs, Peace and Security portfolio oversees ECOMOG — West Africa's principal peacekeeping force"},
            {"entity": "West African conflict prevention architecture", "relationship": "CONTRIBUTED_TO", "note": "Her four-year ECOWAS tenure contributed to the regional diplomatic mechanisms for conflict prevention and crisis mediation"}
        ]
    }),

    # 7 — Seodi White
    ("seodi-white", {
        "summary": (
            "Seodi Venekai-Rudo White is a Malawian social development lawyer, women's "
            "rights activist, and global transactional legal professional who has built "
            "a multifaceted career combining legal advocacy on gender and development "
            "issues in Malawi with a specialized practice as a legal process outsourcing "
            "(LPO) consultant serving international clients from a Malawi base. "
            "Her hybrid career — bridging civil society advocacy with international "
            "commercial legal services — represents an emerging model of legal practice "
            "in Anglophone Africa where common law training can serve both local "
            "development needs and global commercial clients.\n\n"
            "White's social development legal practice has focused on women's rights "
            "in Malawi — a country where customary law, religious practice, and "
            "formal statutory law interact in complex ways that often disadvantage "
            "women in marriage, property, and family matters. Her advocacy has "
            "addressed the legal position of Malawian women in inheritance, "
            "gender-based violence protection, and the implementation of "
            "women's rights legislation. Malawi's legal system, a mix of "
            "English common law and customary law, creates significant "
            "disparities between formal legal rights and practical reality "
            "that require sustained civil society advocacy to bridge.\n\n"
            "Her global transactional law practice — providing legal process "
            "outsourcing services including contract drafting, contract "
            "management, legal support for management projects, and due "
            "diligence — represents the adaptation of African common law "
            "expertise to international commercial demand in an era when "
            "technology enables lawyers in Malawi to serve clients globally. "
            "This model reduces costs for international clients while creating "
            "professional opportunities for Malawian lawyers.\n\n"
            "Her career illustrates the potential for African lawyers to combine "
            "commitment to local social justice advocacy with participation in "
            "the global legal services market — a dual engagement that supports "
            "both their communities and their professional sustainability."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Malawian social development lawyer and women's rights activist who has pioneered a hybrid career combining gender justice advocacy with global transactional legal process outsourcing (LPO) services — a model for African lawyers in the global economy.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Malawi's complex legal landscape — where English common law, customary law, and statutory women's rights legislation interact with often contradictory effects — created the advocacy agenda for her social development legal work",
            "The global legal process outsourcing revolution — driven by technology and the search for cost-effective legal services — created the commercial opportunity for her transactional LPO practice",
            "Her legal training in the English common law tradition (Malawi's inheritance from British colonial governance) gave her the professional toolkit applicable to both local advocacy and international commercial practice"
        ],
        "effects": [
            "Her women's rights advocacy contributed to civil society pressure for the implementation of Malawi's gender equality legislation and for customary law reform affecting women's property and inheritance rights",
            "Her LPO practice demonstrated the feasibility of African lawyers providing high-quality international commercial legal services from an African location — a model with potential for the broader profession",
            "Her career as a Malawian woman lawyer combining advocacy and commercial practice provided a role model for younger Malawian women entering the legal profession",
            "Her work contributed to the development of Malawi's civil society capacity for gender justice advocacy"
        ],
        "relationships": [
            {"entity": "Malawian women's rights movement", "relationship": "ADVOCATE_IN", "note": "A women's rights activist working on gender justice issues within Malawi's complex legal landscape"},
            {"entity": "Malawian legal system (common law + customary law)", "relationship": "PRACTICES_WITHIN", "note": "Her social development work addresses the interaction of English common law and customary law as they affect women's rights in Malawi"},
            {"entity": "Global legal process outsourcing (LPO) industry", "relationship": "PARTICIPANT_IN", "note": "Established a global transactional LPO practice serving international clients through contract drafting, due diligence, and legal support"},
            {"entity": "African women's legal advocacy community", "relationship": "MEMBER_OF", "note": "Part of the broader community of African women lawyers who combine legal practice with gender justice advocacy"},
            {"entity": "Malawi common law tradition", "relationship": "TRAINED_IN", "note": "Her transactional legal expertise is rooted in the English common law tradition that Malawi inherited from British colonial governance"}
        ]
    }),

    # 8 — Alice Rwema
    ("alice-rwema", {
        "summary": (
            "Alice Rwema is a Rwandan lawyer and civil servant who has played a significant "
            "role in the governance and institutional development of Rwanda's energy sector, "
            "serving as Vice-Chairperson of the Board of Directors of the Rwanda Energy "
            "Group (REG) since August 2014 and as Company Secretary of REG since May 2017. "
            "The Rwanda Energy Group is the state parastatal responsible for energy "
            "generation, procurement, transmission, distribution, and export in Rwanda — "
            "making Rwema a key figure in the oversight and governance of an institution "
            "central to Rwanda's development ambitions.\n\n"
            "Rwanda's energy sector has been a centerpiece of the country's post-genocide "
            "national development strategy — the Vision 2020 and subsequent Vision 2050 "
            "frameworks prioritized universal electricity access as a foundation for "
            "economic growth and poverty reduction. Under REG's mandate, Rwanda has "
            "significantly expanded its electricity generation capacity (including "
            "hydropower, solar, and gas) and increased rural electrification rates "
            "substantially from their immediate post-genocide lows. Rwema's board "
            "and secretary roles place her in the governance structure that oversees "
            "this strategic development project.\n\n"
            "As Company Secretary, her responsibilities include ensuring that REG "
            "meets its corporate governance obligations — managing board communications, "
            "ensuring regulatory compliance, coordinating board meetings, and maintaining "
            "the institutional records and governance procedures that a major state-owned "
            "enterprise requires. This role combines legal expertise with corporate "
            "governance — a combination increasingly important as African state-owned "
            "enterprises seek to align with international best practices.\n\n"
            "Her career represents the model of the Rwandan legal professional who "
            "has contributed to the country's institutional development by applying "
            "legal expertise to the governance of its strategic economic institutions."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Rwandan lawyer serving as Vice-Chairperson of the Rwanda Energy Group board and REG Company Secretary; a legal professional central to the governance of Rwanda's strategic energy sector development.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Rwanda's post-genocide Vision 2020 national development strategy prioritized energy access as a foundation for economic recovery — creating the strategic importance of the Rwanda Energy Group that her governance work serves",
            "The corporate governance professionalization of Rwandan state-owned enterprises — reflecting Rwanda's broader institutional development agenda — created the need for legally trained company secretaries and board members",
            "Her legal training provided the professional foundation for the corporate governance and board oversight roles she plays in REG's institutional structure"
        ],
        "effects": [
            "Her board vice-chairperson role contributes to the governance oversight of an institution responsible for electricity generation and distribution across Rwanda — a critical development infrastructure",
            "Her company secretarial function ensures REG's compliance with corporate governance standards and regulatory requirements — supporting the institutional integrity of a major state enterprise",
            "Her career model illustrates how Rwandan legal professionals contribute to the country's development by serving in corporate governance roles in strategic state institutions",
            "Her long tenure in both roles (from 2014 and 2017 respectively) has provided institutional continuity in REG's governance structure"
        ],
        "relationships": [
            {"entity": "Rwanda Energy Group (REG)", "relationship": "BOARD_VICE-CHAIR_AND_SECRETARY_OF", "note": "Vice-Chairperson of the REG Board of Directors (from August 2014) and Company Secretary (from May 2017)"},
            {"entity": "Rwanda Vision 2020 / Vision 2050 development strategy", "relationship": "CONTRIBUTES_TO", "note": "REG, which she helps govern, is a key institution for Rwanda's energy access and economic development ambitions"},
            {"entity": "Rwandan government", "relationship": "CIVIL_SERVANT_OF", "note": "Serves as a civil servant in the governance structure of Rwanda's state energy sector"},
            {"entity": "Corporate governance of African state-owned enterprises", "relationship": "CONTRIBUTES_TO", "note": "Her company secretary and board role exemplifies the professionalization of corporate governance in Rwandan and African state enterprises"},
            {"entity": "Rwandan legal profession", "relationship": "MEMBER_OF", "note": "A trained lawyer who applies her legal expertise to corporate governance in the energy sector"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 22)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
