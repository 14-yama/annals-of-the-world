#!/usr/bin/env python3
"""
Batch 23 — 8 entities: Tirana Hassan, Pamela Coke-Hamilton, Agather Atuhaire,
Aisha Dikko, Joyce Bawah Mogtari, Elsie Addo Awadzi, Thelma Ekiyor, Ali Zaidi
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

    # 1 — Tirana Hassan
    ("tirana-hassan", {
        "summary": (
            "Tirana Hassan is an Australian lawyer, social worker, and human rights leader "
            "who has served as Executive Director of Human Rights Watch (HRW) since 2022 — "
            "one of the most powerful positions in international human rights advocacy, "
            "at the head of an organization with 2,000+ staff across 90 countries and an "
            "annual budget exceeding $100 million, whose research and reporting drives "
            "accountability for governments, militaries, and armed groups worldwide. "
            "Before leading HRW, she held increasingly senior roles at Amnesty International, "
            "culminating in serving as Crisis Response Director — coordinating Amnesty's "
            "emergency response to acute human rights crises globally.\n\n"
            "Hassan's professional formation was in humanitarian response — the work of "
            "deploying to conflict zones and crises to investigate violations, document "
            "abuses, and push for accountability in real time. Her decades of frontline "
            "human rights investigation work across multiple continents gave her direct "
            "experience of the most acute human rights crises of the late 20th and "
            "early 21st centuries: she has led investigations into war crimes, mass "
            "atrocities, and systematic human rights violations in conflict zones from "
            "Africa to the Middle East to Asia. This field experience distinguishes "
            "her from human rights leaders who came primarily from legal or academic "
            "traditions.\n\n"
            "As HRW Executive Director, she has overseen the organization's response to "
            "some of the most consequential human rights crises of the early 2020s — "
            "the Russian invasion of Ukraine, the Hamas attacks of October 7, 2023, "
            "and Israel's subsequent military campaign in Gaza. Her leadership has "
            "navigated intensely controversial terrain where HRW's documentation "
            "of all parties' violations attracted criticism from multiple political "
            "directions.\n\n"
            "Her appointment as an Australian woman of immigrant background to lead "
            "the world's most prominent human rights organization — a role previously "
            "held by figures like Kenneth Roth — signals the generational and "
            "geographic diversification of global human rights leadership."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Executive Director of Human Rights Watch since 2022 — one of the most powerful positions in international human rights advocacy; previously Amnesty International Crisis Response Director; overseeing HRW's response to the Ukraine war, Gaza conflict, and global human rights crises.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Human Rights Watch's institutional mandate — founded in 1978, grown to 2,000+ staff — created the organization she leads; her decades of frontline humanitarian investigation work at Amnesty International built the expertise that qualified her for the directorship",
            "The intensification of global conflict and human rights crises in the early 2020s — the Russian invasion of Ukraine (2022), the October 7, 2023 Hamas attacks and Israeli military campaign — created the high-stakes environment she navigated in her first years as director",
            "The global human rights movement's need for leadership combining field investigation experience with organizational management capability shaped the selection criteria that brought her to HRW's directorship"
        ],
        "effects": [
            "Her leadership of HRW has shaped the world's most influential human rights organization's response to the defining human rights crises of the early 2020s — including documentation of war crimes in Ukraine and in Gaza",
            "Her appointment from Amnesty International's Crisis Response directorship brought an operational, field-focused perspective to HRW leadership — potentially influencing the organization's balance between investigation and advocacy",
            "As an Australian woman of immigrant background leading HRW, her appointment contributed to the geographic and demographic diversification of global human rights organizational leadership",
            "Her navigation of HRW's documentation of Israeli military conduct in Gaza — under intense political pressure from both pro-Israeli and pro-Palestinian advocacy communities — defined one of the most contested chapters in HRW's history"
        ],
        "relationships": [
            {"entity": "Human Rights Watch (HRW)", "relationship": "EXECUTIVE_DIRECTOR_OF", "note": "Executive Director of HRW since 2022 — leading one of the world's most influential human rights organizations"},
            {"entity": "Amnesty International", "relationship": "FORMERLY_SERVED_AT", "note": "Spent decades at Amnesty International including as Crisis Response Director before moving to lead HRW"},
            {"entity": "Russian invasion of Ukraine (2022)", "relationship": "OVERSAW_HRW_DOCUMENTATION_OF", "note": "Her HRW leadership has covered the organization's extensive documentation of war crimes in Ukraine since the 2022 Russian invasion"},
            {"entity": "Israel-Gaza conflict (2023–present)", "relationship": "OVERSAW_HRW_DOCUMENTATION_OF", "note": "Led HRW's documentation of violations by Hamas, Israel, and other parties in the 2023-24 Gaza war — one of the most politically contested human rights reporting efforts in HRW's history"},
            {"entity": "Kenneth Roth (predecessor HRW ED)", "relationship": "SUCCEEDED", "note": "Succeeded Kenneth Roth who led HRW for 29 years (1993–2022)"}
        ]
    }),

    # 2 — Pamela Coke-Hamilton
    ("pamela-coke-hamilton", {
        "summary": (
            "Pamela Rosemarie Coke-Hamilton is a Jamaican international trade lawyer, "
            "economist, and development expert who has served as Executive Director of "
            "the International Trade Centre (ITC) since 2020 — leading the joint "
            "WTO/UNCTAD agency that is the primary multilateral body supporting the "
            "trade and export development needs of small and medium-sized enterprises "
            "in developing and least-developed countries. Her appointment as ITC's "
            "first female Executive Director placed a Caribbean woman lawyer at the "
            "head of one of the key institutions of the multilateral trade system.\n\n"
            "Before the ITC, Coke-Hamilton had an extensive career in Caribbean trade "
            "policy — serving as Director of Trade in Services, Business Facilitation "
            "and Consumer Policy at the Caribbean Community (CARICOM) Secretariat, "
            "where she was a central figure in shaping CARICOM's trade negotiations "
            "with external partners including the European Union (the CARIFORUM-EU "
            "Economic Partnership Agreement) and in developing the Caribbean Single "
            "Market and Economy (CSME). Her expertise combined international trade "
            "law with practical economic development — the challenge of translating "
            "trade agreements into actual economic benefits for small Caribbean states.\n\n"
            "The ITC's mandate — helping SMEs in developing countries connect to global "
            "value chains, access market opportunities, meet quality and standards "
            "requirements, and build the institutional capacity for trade development "
            "— gives her a platform to advance the trade dimension of sustainable "
            "development. Her leadership focuses particularly on trade's role in "
            "economic inclusion: ensuring that the gains from trade reach women-owned "
            "businesses, small agricultural producers, and enterprises in the world's "
            "most marginalized economies.\n\n"
            "As the first woman and first Caribbean national to lead the ITC, "
            "her tenure represents a significant diversification in the leadership "
            "of multilateral economic institutions."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Jamaican trade lawyer; first woman and first Caribbean national to lead the International Trade Centre (ITC) since 2020; former CARICOM trade policy director; a leading Caribbean voice in the multilateral trade system.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Caribbean states' need for sophisticated trade negotiation expertise — as small open economies highly dependent on trade agreements — drove the development of her expertise in trade law and Caribbean economic policy",
            "The CARIFORUM-EU Economic Partnership Agreement negotiations — a landmark trade deal between the EU and Caribbean states concluded in 2008 — was a central experience that shaped her understanding of trade law in a development context",
            "The ITC's mandate as the WTO/UNCTAD's SME-focused trade development agency created the institutional framework in which her combination of trade law expertise and development focus found its global expression"
        ],
        "effects": [
            "As ITC Executive Director, she has shaped the multilateral organization's approach to inclusive trade — particularly trade's benefits for women entrepreneurs, small producers, and least-developed countries",
            "As the first woman and first Caribbean national to lead the ITC, her appointment diversified the leadership of a key multilateral economic institution",
            "Her CARICOM career shaped Caribbean trade negotiation strategy in agreements with major partners, contributing to the economic framework within which Caribbean states engage the global economy",
            "Her advocacy for inclusive trade — ensuring trade gains reach SMEs, women-owned businesses, and marginalized communities — has influenced ITC's programmatic priorities"
        ],
        "relationships": [
            {"entity": "International Trade Centre (ITC)", "relationship": "EXECUTIVE_DIRECTOR_OF", "note": "Executive Director of the ITC since 2020 — the first woman and first Caribbean national in the role"},
            {"entity": "Caribbean Community (CARICOM) Secretariat", "relationship": "FORMERLY_DIRECTED_TRADE_POLICY_AT", "note": "Served as Director of Trade in Services, Business Facilitation and Consumer Policy at the CARICOM Secretariat"},
            {"entity": "CARIFORUM-EU Economic Partnership Agreement", "relationship": "SHAPED", "note": "Was a key Caribbean trade official involved in shaping the CARIFORUM-EU EPA — a landmark trade agreement between the EU and Caribbean states"},
            {"entity": "WTO (World Trade Organization)", "relationship": "LEADS_JOINT_AGENCY_WITH", "note": "The ITC she leads is a joint agency of the WTO and UNCTAD"},
            {"entity": "Caribbean Single Market and Economy (CSME)", "relationship": "CONTRIBUTED_TO", "note": "Her CARICOM work contributed to developing the institutional framework for the Caribbean Single Market and Economy"}
        ]
    }),

    # 3 — Agather Atuhaire
    ("agather-atuhaire", {
        "summary": (
            "Agather Atuhaire is a Ugandan lawyer, journalist, and human rights activist "
            "whose career has combined legal expertise with investigative journalism to "
            "produce accountability reporting on corruption, abuse of power, and human "
            "rights violations in Uganda — work that has earned her the European Union "
            "Human Rights Defenders Award and the US Secretary of State's International "
            "Women of Courage Award, two of the most prestigious international "
            "recognitions for civil society activism. Her investigative focus on "
            "the Parliament of Uganda — an institution that has attracted considerable "
            "criticism for financial mismanagement, abuse of parliamentary privileges, "
            "and self-enrichment — has generated significant public discourse and "
            "accountability pressure.\n\n"
            "Atuhaire's particular strength is the combination of legal training "
            "and investigative journalism — bringing legal analysis to public interest "
            "reporting in a way that goes beyond surface-level description to identify "
            "the legal frameworks that officials are violating, the institutional "
            "mechanisms being abused, and the specific legal remedies available to "
            "citizens. This approach has made her reporting both more technically "
            "credible and more legally actionable than conventional investigative "
            "journalism in the Ugandan context.\n\n"
            "Her work has been conducted in a politically difficult environment: "
            "Uganda under President Yoweri Museveni's long rule (since 1986) has "
            "maintained significant restrictions on media freedom and civil society "
            "space, and journalists who report critically on powerful institutions "
            "face professional and personal risks. Her international recognition "
            "has provided some protection while also amplifying the international "
            "visibility of Uganda's civil society challenges.\n\n"
            "Her career illustrates the powerful intersection of legal and journalistic "
            "skills in accountability work — a combination increasingly important "
            "in African civil society as countries seek to hold powerful actors "
            "to account through public documentation and legal challenge."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Ugandan lawyer-journalist whose investigative work on parliamentary corruption and human rights earned the EU Human Rights Defenders Award and US Secretary of State's International Women of Courage Award; a leading accountability journalist in Museveni-era Uganda.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Uganda's Parliament's documented record of financial mismanagement, self-dealing, and abuse of parliamentary privileges created the accountability journalism agenda that defines her investigative career",
            "The combination of legal training with investigative journalism — rare in the Ugandan context — gave her investigative work a technical credibility and legal precision that conventional journalism lacks",
            "Uganda's restricted civil society environment under Museveni's long rule created both the need for courageous accountability journalism and the personal risks that have defined her career"
        ],
        "effects": [
            "Her investigative reporting on Uganda's Parliament has generated public discourse and accountability pressure on an institution that had largely escaped sustained investigative scrutiny",
            "Her EU Human Rights Defenders Award and US Secretary of State's International Women of Courage Award amplified international awareness of Uganda's civil society challenges and provided protection for her continued work",
            "Her career model — combining law and journalism for accountability work — has influenced younger Ugandan civil society practitioners",
            "Her visibility as an internationally recognized Ugandan journalist has helped sustain international attention to Uganda's governance and human rights situation"
        ],
        "relationships": [
            {"entity": "Parliament of Uganda", "relationship": "INVESTIGATES_ACCOUNTABILITY_OF", "note": "Her investigative journalism has focused particularly on corruption, financial mismanagement, and abuse of power in Uganda's Parliament"},
            {"entity": "EU Human Rights Defenders Award", "relationship": "RECIPIENT_OF", "note": "Recipient of the European Union Human Rights Defenders Award for her civil society and accountability journalism work"},
            {"entity": "US Secretary of State's International Women of Courage Award", "relationship": "RECIPIENT_OF", "note": "Recipient of the US Secretary of State's International Women of Courage Award — a top US recognition for women civil society leaders"},
            {"entity": "Uganda civil society and press freedom community", "relationship": "PART_OF", "note": "A leading figure in Uganda's civil society and media accountability community operating under the restrictions of Museveni's long-running government"},
            {"entity": "President Yoweri Museveni (Uganda)", "relationship": "REPORTS_CRITICALLY_ON_INSTITUTIONS_OF", "note": "Her accountability journalism targets institutions within Uganda's political system under Museveni's governance since 1986"}
        ]
    }),

    # 4 — Aisha Dikko
    ("aisha-dikko", {
        "summary": (
            "Aisha Dikko is a Nigerian lawyer who served as Attorney General and Commissioner "
            "of Justice for Kaduna State — one of Nigeria's largest and most strategically "
            "significant states, with a population exceeding 10 million and a position in "
            "the middle belt that has made it a recurring site of intercommunal violence "
            "between farming and herding communities. She was sworn into office on "
            "12 July 2019 under Governor Nasir Ahmad el-Rufai, whose administration "
            "pursued significant structural reforms in governance, education, and "
            "security in Kaduna State.\n\n"
            "The office of state Attorney General and Commissioner of Justice is one "
            "of the most consequential legal positions in Nigeria's federal system — "
            "combining the roles of chief legal advisor to the state government, "
            "chief prosecutor, and political appointee responsible for managing "
            "state legal affairs. In Kaduna State, this position carried particular "
            "weight during el-Rufai's tenure because the state was a focal point "
            "of some of Nigeria's most serious security and governance challenges: "
            "the Kaduna-Birnin-Gwari corridor banditry crisis, intercommunal violence "
            "in the Southern Kaduna region, and the governance reform agenda that "
            "el-Rufai pursued often in contentious political circumstances.\n\n"
            "Her service as state AG involved legal advice on the constitutionality "
            "of the governor's policy initiatives, prosecution of security-related "
            "offenses, management of state litigation, and representation of the "
            "state government's legal positions in disputes with other governmental "
            "actors. In a state experiencing acute security challenges, the AG's "
            "office plays a critical role in both the prosecution of criminal cases "
            "and the legal framing of government security responses.\n\n"
            "Her appointment as a woman to the AG/CJ position in one of Nigeria's "
            "major northern states was itself a notable achievement in an environment "
            "where women's representation in senior legal and governmental positions "
            "in northern Nigeria remains limited."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Nigerian lawyer who served as Attorney General and Commissioner of Justice of Kaduna State from July 2019 under Governor Nasir Ahmad el-Rufai — one of Nigeria's most consequential state governments during a period of acute security and governance challenges.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Governor Nasir Ahmad el-Rufai's governance reform agenda for Kaduna State — one of the most ambitious and controversial state-level reform programs in Nigeria — required a state AG who could legally support and defend significant policy changes",
            "Kaduna State's acute security challenges — intercommunal violence in Southern Kaduna, banditry in the Birnin-Gwari corridor — created the legal advocacy agenda in which the AG's office operated",
            "The limited representation of women in senior legal and governmental positions in northern Nigeria made her appointment as a female state AG notable in the regional context"
        ],
        "effects": [
            "Her service as Kaduna State AG provided the legal institutional support for el-Rufai's governance reform agenda — including legal advice on constitutionality, state prosecutions, and government litigation",
            "Her office's management of security-related prosecutions contributed to Kaduna State's legal response to the intercommunal violence and banditry crises of the period",
            "As a woman appointed to the AG position in a major northern Nigerian state, she contributed to the gradual expansion of women's representation in senior governmental positions in northern Nigeria",
            "Her tenure contributed to the institutional development of the Kaduna State Ministry of Justice during a period of significant governmental reform"
        ],
        "relationships": [
            {"entity": "Kaduna State Government", "relationship": "ATTORNEY_GENERAL_OF", "note": "Attorney General and Commissioner of Justice for Kaduna State, sworn in July 12, 2019"},
            {"entity": "Governor Nasir Ahmad el-Rufai", "relationship": "APPOINTED_BY_AND_SERVED_UNDER", "note": "Appointed by and served under Governor el-Rufai — one of Nigeria's most reform-oriented and controversial state governors"},
            {"entity": "Kaduna State security crises (intercommunal violence / banditry)", "relationship": "MANAGED_LEGAL_RESPONSE_TO", "note": "Her AG tenure coincided with Kaduna State's acute security challenges requiring legal prosecution and governance response"},
            {"entity": "Kaduna State Ministry of Justice", "relationship": "HEADED", "note": "As AG/CJ she headed the Kaduna State Ministry of Justice — the state's principal legal institution"},
            {"entity": "Women in northern Nigerian state government", "relationship": "REPRESENTATIVE_OF", "note": "Her appointment as a female AG in a major northern Nigerian state was notable given the limited representation of women in senior northern Nigerian governmental positions"}
        ]
    }),

    # 5 — Joyce Bawah Mogtari
    ("joyce-bawah-mogtari", {
        "summary": (
            "Joyce Bawah Mogtari is a Ghanaian lawyer, politician, and mediator who has "
            "held senior positions in Ghana's National Democratic Congress (NDC) government, "
            "including serving as Deputy Minister of Transport and as Special Aide to "
            "President John Dramani Mahama — positions that reflect the pattern of the "
            "trained lawyer who moves between legal practice, government service, "
            "and political party roles in Ghana's competitive democratic politics. "
            "An experienced mediator with a practice that spans both domestic and "
            "international dispute resolution, she brings legal and diplomatic skills "
            "to both governmental service and political advocacy.\n\n"
            "Her work as Deputy Minister of Transport placed her in one of Ghana's "
            "most economically significant ministries — overseeing the regulatory, "
            "policy, and infrastructure dimensions of a transport sector critical "
            "to a fast-growing West African economy. The transport portfolio includes "
            "road, rail, aviation, and maritime transport, and in Ghana's context "
            "involves managing significant infrastructure investment decisions, "
            "regulatory frameworks for private transport operators, and the "
            "international transport agreements that govern Ghana's air and "
            "maritime connections.\n\n"
            "Her role as Special Aide to President Mahama — one of the most intimate "
            "advisory positions in government — reflects the trusted relationship "
            "between a skilled legal and political professional and a president who "
            "has relied on capable advisors across his political career. Mahama, "
            "who served as President 2012–2017 and was re-elected in 2024, has "
            "been one of the central figures of contemporary Ghanaian politics, "
            "and Mogtari's proximity to his office placed her close to the center "
            "of Ghanaian political decision-making.\n\n"
            "Her career illustrates the fluid movement between legal practice, "
            "government service, and political role that characterizes many "
            "of Ghana's most capable public lawyers."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Ghanaian lawyer and NDC politician; Deputy Minister of Transport and Special Aide to President John Dramani Mahama; an experienced international mediator at the intersection of law, government, and Ghanaian democratic politics.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Ghana's competitive democratic politics — with the NDC and NPP alternating in power — created the political environment in which NDC-aligned legal professionals like Mogtari move between government service and party advocacy",
            "President Mahama's reliance on capable legal and political advisors throughout his career created the demand for her skills as Special Aide",
            "Ghana's transport sector's strategic importance for economic development — as a gateway economy with significant infrastructure investment needs — created the substantive policy portfolio she served in as Deputy Minister"
        ],
        "effects": [
            "Her Deputy Minister tenure contributed to transport sector policy and regulatory management during an important period of Ghanaian infrastructure development",
            "Her mediation work — both domestic and international — has contributed to dispute resolution in contexts ranging from commercial to community-level conflicts",
            "Her Special Aide role made her a participant in Ghanaian presidential decision-making — contributing legal and political judgment to President Mahama's advisory circle",
            "Her career pattern of lawyer-turned-politician-turned-presidential-advisor illustrates the pathway through which legal training translates into governmental influence in Ghanaian politics"
        ],
        "relationships": [
            {"entity": "President John Dramani Mahama", "relationship": "SPECIAL_AIDE_TO", "note": "Serves as Special Aide to President John Dramani Mahama — a position of close advisory proximity to the Ghanaian head of state"},
            {"entity": "Ghana Ministry of Transport", "relationship": "FORMER_DEPUTY_MINISTER_OF", "note": "Served as Deputy Minister of Transport — overseeing transport policy, regulation, and infrastructure investment"},
            {"entity": "National Democratic Congress (NDC, Ghana)", "relationship": "AFFILIATED_WITH", "note": "An NDC-aligned politician whose governmental service has occurred under NDC administrations"},
            {"entity": "International mediation practice", "relationship": "PRACTICES", "note": "An experienced mediator in both domestic and international dispute resolution contexts"},
            {"entity": "Ghanaian legal-political professional class", "relationship": "MEMBER_OF", "note": "Part of the class of Ghanaian lawyers who move fluidly between legal practice, government service, and political party roles"}
        ]
    }),

    # 6 — Elsie Addo Awadzi
    ("elsie-addo-awadzi", {
        "summary": (
            "Mrs. Elsie Addo Awadzi is a Ghanaian international economic and financial "
            "lawyer who serves as the 2nd Deputy Governor of the Bank of Ghana — appointed "
            "by President Nana Addo Dankwa Akufo-Addo in February 2018 — making her the "
            "second woman to hold that position in the bank's history. She is also the "
            "elected Chairperson of the Alliance for Financial Inclusion (AFI), a global "
            "network of central bank regulators from over 80 developing and emerging "
            "economies focused on financial inclusion policy. Her career at the "
            "intersection of international finance law, central banking, and financial "
            "inclusion makes her one of West Africa's most distinguished international "
            "financial law practitioners.\n\n"
            "Before her Bank of Ghana appointment, Awadzi built an impressive international "
            "career in financial regulation — working at the International Monetary Fund "
            "(IMF) in Washington DC, where she was a legal expert in the IMF's Legal "
            "Department, advising member countries on the legal aspects of financial "
            "sector regulation, banking supervision, and financial system reform. "
            "Her IMF work gave her expertise in the global financial regulatory "
            "architecture that she has applied in her Bank of Ghana role.\n\n"
            "As 2nd Deputy Governor, she has been responsible for financial sector "
            "stability oversight, regulatory supervision of Ghana's banking sector, "
            "and the technical aspects of monetary policy implementation. Her tenure "
            "coincided with a significant banking sector restructuring in Ghana — "
            "including the consolidation and recapitalization of the banking sector "
            "that the Bank of Ghana undertook in 2017–2018 to address systemic "
            "weaknesses exposed after years of regulatory forbearance.\n\n"
            "Her leadership of the AFI network — advocating for regulatory frameworks "
            "that extend financial services to the unbanked — has made her a global "
            "voice for financial inclusion as a development priority."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Ghanaian international financial lawyer; 2nd Deputy Governor of the Bank of Ghana (2018–present); Chairperson of the Alliance for Financial Inclusion (AFI); former IMF Legal Department expert; a leading West African figure in financial sector regulation and financial inclusion.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Ghana's need to strengthen banking sector regulation and oversight — particularly following the banking crisis that required significant sector restructuring in 2017–2018 — created the demand for her international financial regulation expertise",
            "Her IMF Legal Department experience gave her the technical expertise in international financial law and banking supervision that qualified her for the Bank of Ghana's 2nd Deputy Governor role",
            "The global financial inclusion movement's recognition that central bank regulatory frameworks are critical determinants of whether the unbanked can access formal financial services created the AFI chairmanship mandate she leads"
        ],
        "effects": [
            "Her Bank of Ghana tenure has contributed to banking sector regulation, financial stability oversight, and the implementation of the 2017–2018 banking sector recapitalization and restructuring",
            "Her AFI chairmanship has amplified Ghana's and Africa's voice in global financial inclusion policy — advocating for regulatory frameworks that extend financial services to underserved populations",
            "As one of the most senior women in Ghanaian financial sector governance, she has contributed to the gradual expansion of women's leadership in West African central banking",
            "Her IMF-to-central-bank career trajectory illustrates the pathway through which expertise developed in multilateral institutions can strengthen developing country regulatory capacity"
        ],
        "relationships": [
            {"entity": "Bank of Ghana", "relationship": "2ND_DEPUTY_GOVERNOR_OF", "note": "2nd Deputy Governor of the Bank of Ghana since February 2018; the second woman to hold that position"},
            {"entity": "Alliance for Financial Inclusion (AFI)", "relationship": "CHAIRPERSON_OF", "note": "Elected Chairperson of the AFI — a global network of central bank regulators from 80+ developing economies focused on financial inclusion"},
            {"entity": "International Monetary Fund (IMF)", "relationship": "FORMERLY_SERVED_AT", "note": "Former legal expert in the IMF Legal Department, advising member countries on financial sector regulation and banking law"},
            {"entity": "President Nana Akufo-Addo (Ghana)", "relationship": "APPOINTED_BY", "note": "Appointed as 2nd Deputy Governor of the Bank of Ghana by President Akufo-Addo in February 2018"},
            {"entity": "Ghana banking sector restructuring (2017–2018)", "relationship": "OVERSAW_REGULATORY_ASPECTS_OF", "note": "Her Bank of Ghana tenure coincided with the significant recapitalization and restructuring of Ghana's banking sector"}
        ]
    }),

    # 7 — Thelma Ekiyor
    ("thelma-ekiyor", {
        "summary": (
            "Thelma Arimiebi Ekiyor is a Nigerian lawyer, social entrepreneur, and impact "
            "investor who has built a career at the intersection of peacebuilding, women's "
            "economic empowerment, and impact finance in West Africa and globally — moving "
            "from civil society leadership in conflict resolution and women's peacebuilding "
            "to leadership roles in impact investment organizations focused on women "
            "entrepreneurs. Her career trajectory reflects the evolution of international "
            "development thinking from grant-based civil society work to market-based "
            "approaches to social change.\n\n"
            "Ekiyor's early career was in peacebuilding — supporting women's participation "
            "in peace processes in West Africa, a region that experienced devastating "
            "civil conflicts in Liberia, Sierra Leone, and Côte d'Ivoire from the 1990s "
            "through the 2000s. Her work on women and peacebuilding addressed the "
            "dual agenda of protecting women from conflict-related sexual violence "
            "and ensuring their meaningful participation in peace negotiations — "
            "an agenda articulated in UN Security Council Resolution 1325 (2000) "
            "but rarely implemented in practice without sustained civil society "
            "pressure. This early work gave her expertise in conflict-affected "
            "environments and the specific challenges facing women in West African "
            "post-conflict societies.\n\n"
            "She later transitioned to impact investing — the practice of directing "
            "capital toward enterprises that generate both financial returns and "
            "measurable social impact. Her focus on women entrepreneurs reflects "
            "the growing evidence that investing in women-led businesses produces "
            "significant development multipliers: women reinvest a higher proportion "
            "of income in their families and communities than men, making women's "
            "economic empowerment a high-leverage development intervention.\n\n"
            "Her career spanning civil society, peacebuilding, and impact finance "
            "reflects the complex pathways through which African development "
            "professionals have responded to changing development paradigms."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Nigerian lawyer and impact investor focused on women entrepreneurs; formerly a peacebuilding practitioner supporting women's participation in West African peace processes; a figure at the intersection of conflict resolution, women's economic empowerment, and impact finance.",
            "significanceCategory": "continental"
        },
        "causes": [
            "West Africa's devastating civil conflicts in Liberia, Sierra Leone, and Côte d'Ivoire created the peacebuilding context in which her early career was shaped — particularly the gendered dimensions of conflict and the exclusion of women from peace processes",
            "UN Security Council Resolution 1325 (2000) on Women, Peace and Security created the international framework that legitimized her women-in-peacebuilding advocacy work",
            "The impact investing movement's growing emphasis on gender-lens investing — directing capital toward women entrepreneurs and women-led businesses — created the professional transition opportunity from civil society to impact finance"
        ],
        "effects": [
            "Her peacebuilding work in West Africa contributed to the implementation of women's peace and security frameworks in a region that experienced severe civil conflicts",
            "Her transition to impact investing has channeled capital toward women-led businesses — contributing to women's economic empowerment through market-based mechanisms",
            "Her career trajectory from civil society to impact finance has made her a model for African development professionals navigating the evolution of development approaches",
            "Her advocacy for women entrepreneurs in the impact investing space has contributed to the growing global attention to gender-lens investing as a strategy for sustainable development"
        ],
        "relationships": [
            {"entity": "Women's peacebuilding in West Africa", "relationship": "FORMERLY_LED", "note": "Built her early career supporting women's participation in peacebuilding processes in Liberia, Sierra Leone, and Côte d'Ivoire"},
            {"entity": "UN Security Council Resolution 1325 (Women, Peace and Security)", "relationship": "IMPLEMENTED_FRAMEWORKS_OF", "note": "Her peacebuilding work implemented the gender, peace, and security frameworks articulated in UNSCR 1325"},
            {"entity": "Impact investing for women entrepreneurs", "relationship": "PRACTICES", "note": "Transitioned from civil society to impact investing focused on women-led businesses and women's economic empowerment"},
            {"entity": "West African development community", "relationship": "MEMBER_OF", "note": "A significant figure in the West African professional development community bridging civil society, peacebuilding, and finance"},
            {"entity": "Gender-lens investing movement", "relationship": "CONTRIBUTOR_TO", "note": "Her impact investing focus on women entrepreneurs contributes to the global gender-lens investing movement"}
        ]
    }),

    # 8 — Ali Zaidi
    ("ali-zaidi", {
        "summary": (
            "Ali A. Zaidi is a Pakistani-American lawyer and climate policy expert who "
            "served as the second United States National Climate Advisor under President "
            "Joe Biden from 2022 to 2025 — one of the most powerful climate policy "
            "positions in the US government, coordinating the implementation of the "
            "Biden administration's landmark climate agenda including the Inflation "
            "Reduction Act (IRA), the largest climate investment in American history. "
            "As National Climate Advisor, he chaired the National Climate Task Force "
            "and was the White House's principal coordinator of climate policy "
            "implementation across the federal government.\n\n"
            "Zaidi came to the White House with deep executive branch climate policy "
            "experience: he had served in the Obama administration in multiple roles "
            "including as Deputy Director for Energy Policy on the Domestic Policy "
            "Council and as Associate Director for Natural Resources, Energy, and "
            "Science at the Office of Management and Budget — positions that gave "
            "him intimate knowledge of how the federal government's budget and "
            "regulatory apparatus could be used to drive clean energy deployment. "
            "After the Obama years, he served as New York's Deputy Secretary for "
            "Energy and Environment under Governor Andrew Cuomo, working on New "
            "York State's ambitious climate policy agenda.\n\n"
            "His tenure as National Climate Advisor saw him drive the implementation "
            "of the IRA's historic $369 billion in climate and clean energy "
            "investments — coordinating with the Treasury Department, EPA, Department "
            "of Energy, and other agencies to develop the rules, incentives, and "
            "programs that would determine how those investments reached the "
            "economy. He also represented the US at international climate negotiations, "
            "working alongside Special Presidential Envoy John Kerry.\n\n"
            "As one of the most senior Pakistani-American officials in recent US "
            "government history, his career also represents the contributions of "
            "South Asian diaspora professionals to American public service."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Pakistani-American lawyer and US National Climate Advisor under President Biden (2022–2025); coordinated implementation of the Inflation Reduction Act — the largest climate investment in US history; former Obama administration energy policy official.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Biden administration's decision to make climate policy a central governing priority — including passage of the Inflation Reduction Act — created the demand for senior climate policy coordination that the National Climate Advisor role was designed to provide",
            "His extensive Obama-era federal government experience in energy and environmental policy made him uniquely qualified to navigate the interagency coordination required to implement the IRA's historic investments",
            "New York's ambitious state-level climate policy agenda — which he helped develop as Deputy Secretary for Energy and Environment — gave him experience with implementation challenges that proved directly applicable to his federal role"
        ],
        "effects": [
            "As National Climate Advisor, he drove the implementation of the Inflation Reduction Act's $369 billion in climate and clean energy investments — coordinating the interagency process that determined how those historic investments reached the economy",
            "His tenure helped establish the institutional mechanisms for US climate policy implementation — including the National Climate Task Force that coordinates climate action across the federal government",
            "His representation of the US at international climate negotiations contributed to the Biden administration's re-engagement with global climate diplomacy after the Trump-era withdrawal from the Paris Agreement",
            "His career as a senior Pakistani-American official contributed to the representation of South Asian diaspora professionals in US government leadership"
        ],
        "relationships": [
            {"entity": "Biden White House National Climate Advisor", "relationship": "SERVED_AS", "note": "Second US National Climate Advisor under President Biden (2022–2025); chaired the National Climate Task Force"},
            {"entity": "Inflation Reduction Act (2022)", "relationship": "COORDINATED_IMPLEMENTATION_OF", "note": "Coordinated the interagency implementation of the IRA's $369 billion in climate and clean energy investments across the federal government"},
            {"entity": "Obama administration", "relationship": "FORMERLY_SERVED_IN", "note": "Served in multiple Obama administration energy and climate roles including Deputy Director for Energy Policy (Domestic Policy Council) and OMB Associate Director"},
            {"entity": "New York State (energy and environment policy)", "relationship": "FORMERLY_SERVED_IN", "note": "Served as New York's Deputy Secretary for Energy and Environment under Governor Andrew Cuomo"},
            {"entity": "John Kerry (Special Presidential Envoy for Climate)", "relationship": "WORKED_ALONGSIDE", "note": "Coordinated US climate policy implementation with Special Presidential Envoy John Kerry in the Biden administration"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 23)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
