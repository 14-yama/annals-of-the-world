#!/usr/bin/env python3
"""
Batch 21 — 8 entities: Hasna Barkat Daoud, Shalu Nigam, Entisar Elsaeed,
Smaranda Olarinde, Vrinda Grover, Samah Subay, Zaha Hassan, Abiola Akiyode-Afolabi
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
          f"e={len(det.get('effects',[]))} r={len(det.get('relationships',[]))}")


ENTITIES = [

    # 1 — Hasna Barkat Daoud
    ("hasna-barkat-daoud", {
        "summary": (
            "Hasna Barkat Daoud is a Djiboutian lawyer and former government minister who "
            "represents the emerging generation of professionally trained legal practitioners "
            "and policy-makers in the Republic of Djibouti — a small nation in the Horn of "
            "Africa with a population of approximately one million, a French civil law "
            "inheritance, and strategic importance far beyond its size due to its position "
            "at the mouth of the Red Sea and its hosting of military bases from the United "
            "States, France, Japan, China, and Italy. Her legal career and ministerial service "
            "reflect Djibouti's efforts to build professional state institutions and a trained "
            "civil service in a country where the legal profession was historically very small.\n\n"
            "Djibouti's legal system combines French civil law — inherited from the colonial "
            "period as the Territory of the Afars and Issas before independence in 1977 — "
            "with Islamic law applicable in family and personal status matters, and with "
            "elements of customary law of the Issa Somali and Afar communities. Building "
            "a professional legal class that can navigate these multiple legal traditions "
            "and serve the state's growing institutional needs — including dispute resolution "
            "in matters relating to Djibouti's strategic port and commercial role — has been "
            "a priority for the government of President Ismail Omar Guelleh.\n\n"
            "Her service as a government minister placed her in the executive leadership "
            "of a government that has governed Djibouti since 1999 — a government that "
            "has maintained political stability while facing criticism for democratic "
            "governance deficits and civil society restrictions. Women in senior government "
            "roles in Djibouti, as across the Horn of Africa, remain underrepresented, "
            "making her ministerial tenure significant in the gender history of Djiboutian "
            "state leadership.\n\n"
            "Her career illustrates the dual role of the lawyer-minister in small developing "
            "states: using legal training not only for private practice but for state "
            "institution-building in a context where professional capacity is scarce "
            "and each individual's contribution matters significantly."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Djiboutian lawyer and government minister; a representative figure of Djibouti's small professional legal class who served in executive government in one of the Horn of Africa's most strategically significant small states.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Djibouti's strategic position at the mouth of the Red Sea — hosting multiple foreign military bases and serving as a key commercial port — created the institutional needs that professional lawyers like Barkat Daoud were trained to serve",
            "The post-independence Djiboutian state's need to build professional institutions from a small base created opportunities for trained lawyers to move into government service",
            "The French civil law tradition and the French educational system — Djibouti maintained strong ties to France after independence — provided the training framework for Djiboutian legal professionals"
        ],
        "effects": [
            "Her ministerial service contributed to the executive governance of the Djiboutian state in a period of sustained rule by President Guelleh's government",
            "As a woman in senior government, she contributed to the slow expansion of women's representation in Djiboutian state leadership",
            "Her career model of the lawyer who moves between legal practice and government service is a pattern important for small state institution-building",
            "Her service helped maintain the thin professional class of legally trained government administrators that sustains Djibouti's state functions"
        ],
        "relationships": [
            {"entity": "Government of Djibouti", "relationship": "SERVED_AS_MINISTER_IN", "note": "Served as a government minister under the Government of Djibouti"},
            {"entity": "President Ismail Omar Guelleh", "relationship": "SERVED_UNDER", "note": "Her ministerial service was within the long-running administration of President Ismail Omar Guelleh"},
            {"entity": "French civil law system (Djibouti)", "relationship": "TRAINED_IN", "note": "Djibouti's legal system is based on French civil law, in which she was professionally trained"},
            {"entity": "Djiboutian professional legal class", "relationship": "MEMBER_OF", "note": "Part of the small professionally trained legal community that serves Djibouti's state and private legal needs"},
            {"entity": "Women in Djiboutian government", "relationship": "REPRESENTATIVE_OF", "note": "Her ministerial role made her part of the small group of women in senior Djiboutian executive leadership"}
        ]
    }),

    # 2 — Shalu Nigam
    ("shalu-nigam", {
        "summary": (
            "Shalu Nigam is an Indian feminist lawyer, legal scholar, and author who has "
            "combined litigation, academic research, and public advocacy to challenge "
            "patriarchal legal structures in India — most notably as the petitioner in "
            "the landmark case Shalu Nigam v. Regional Passport Officer (decided 17 May 2016), "
            "in which the Delhi High Court held that applicants could be issued Indian passports "
            "without being required to provide their father's name — a ruling that recognized "
            "the rights of women and children in non-traditional family situations and struck "
            "a blow against the systemic inscription of paternal authority into official "
            "identity documents.\n\n"
            "The passport case arose from Nigam's personal experience: when she applied for "
            "a passport for herself and her daughter, she was required to provide the father's "
            "name — a requirement that excluded or humiliated single mothers, widows, women "
            "estranged from their fathers, and children from non-traditional family structures. "
            "By litigating this administrative requirement as a violation of constitutional "
            "rights — including the right to dignity, privacy, and equality — she transformed "
            "a personal grievance into a precedent that affected millions of Indian women "
            "and children who had previously been unable to obtain passports or faced "
            "severe bureaucratic obstacles in doing so.\n\n"
            "Beyond the passport case, Nigam is a prolific researcher and author in the "
            "feminist legal theory tradition, examining the ways Indian law — in family law, "
            "property rights, criminal law, and administrative procedures — embeds and "
            "reinforces patriarchal assumptions. She has published extensively on gender, "
            "law, and human rights, contributing to the growing body of Indian feminist "
            "jurisprudence that challenges both the formal structure and the practical "
            "operation of law in India.\n\n"
            "'I wanted a passport, and the government required my father's name. I realized "
            "this was about much more than a document — it was about whose name defines us.' "
            "Her transformation of that realization into legal precedent is a model of "
            "feminist legal activism."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Indian feminist lawyer and petitioner in Shalu Nigam v. Regional Passport Officer (2016) — the landmark case that removed the requirement for a father's name on Indian passport applications, affecting millions of women and children.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Indian passport application's requirement for a father's name — a bureaucratic inheritance of patriarchal assumptions about identity and family structure — created the specific administrative injustice that Nigam challenged",
            "India's feminist legal movement, which has used public interest litigation (PIL) as a tool for challenging discriminatory laws and practices since the 1980s, provided the legal framework within which her case was litigated",
            "Her personal experience as a woman required to name her father on an official identity document transformed an abstract legal question into a concrete personal grievance that she litigated to a precedent"
        ],
        "effects": [
            "Shalu Nigam v. Regional Passport Officer (2016) removed the father's name requirement from Indian passport applications — a ruling with practical impact on millions of Indian women and children in non-traditional family situations",
            "The case established a precedent for challenging patriarchal bureaucratic requirements as violations of constitutional rights to dignity, privacy, and equality",
            "Her academic writing has contributed to Indian feminist jurisprudence, providing scholarly analysis of the ways Indian law embeds gender hierarchy",
            "Her career model — combining personal litigation with academic research and public advocacy — has influenced younger Indian feminist lawyers"
        ],
        "relationships": [
            {"entity": "Delhi High Court", "relationship": "ARGUED_BEFORE", "note": "Petitioner in Shalu Nigam v. Regional Passport Officer, argued before the Delhi High Court in 2016"},
            {"entity": "Indian passport system (Ministry of External Affairs)", "relationship": "CHALLENGED", "note": "Her petition challenged the Indian passport system's requirement for applicants to provide their father's name"},
            {"entity": "Indian feminist legal movement", "relationship": "PART_OF", "note": "Her litigation and scholarship are embedded in the broader Indian feminist legal tradition that uses public interest litigation to challenge patriarchal law"},
            {"entity": "Indian Constitution (Articles 14, 19, 21)", "relationship": "INVOKED", "note": "Her passport case grounded feminist legal arguments in constitutional rights to equality, freedom, and dignity"},
            {"entity": "Indian feminist jurisprudence (academic tradition)", "relationship": "CONTRIBUTES_TO", "note": "Her academic writing on gender, law, and human rights contributes to the scholarly tradition of Indian feminist jurisprudence"}
        ]
    }),

    # 3 — Entisar Elsaeed
    ("entisar-elsaeed", {
        "summary": (
            "Entisar Elsaeed is an Egyptian women's rights activist, lawyer, and social "
            "entrepreneur who founded and directs the Cairo Foundation for Development and "
            "Law — an organization dedicated to combating female genital mutilation (FGM), "
            "supporting survivors of domestic violence, providing sexual and reproductive "
            "health education, and advancing women's legal rights in one of the region's "
            "most populous and socially conservative societies. Her work addresses some "
            "of Egypt's most entrenched gender-based human rights violations in a context "
            "where legal progress and social resistance coexist.\n\n"
            "FGM — the partial or total removal of the female external genitalia for "
            "non-medical reasons — affects approximately 87% of Egyptian women aged 15-49 "
            "according to recent surveys, making Egypt one of the countries with the highest "
            "FGM prevalence globally. Egypt criminalized FGM in 2008 and strengthened its "
            "prohibition in subsequent years, but enforcement has remained weak and social "
            "and religious legitimation of the practice — often performed by medical "
            "professionals — continues. Elsaeed's work addresses both the legal dimension "
            "(supporting prosecution, legal reform) and the community dimension (education, "
            "attitude change) of this complex and deeply embedded practice.\n\n"
            "Her foundation's work on domestic violence operates in a context where Egypt's "
            "legal frameworks for addressing intimate partner violence have been significantly "
            "weaker than in many comparable jurisdictions — the absence of a comprehensive "
            "domestic violence law until recent years left survivors with limited legal "
            "recourse. Providing legal support for survivors, documenting cases, and "
            "advocating for legislative reform have been central to the Foundation's work.\n\n"
            "Her career represents the intersection of legal expertise and civil society "
            "leadership that has driven the most effective human rights advocacy in the "
            "Arab world — combining litigation with education, documentation with advocacy, "
            "and legal professionalism with grassroots community work."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Egyptian women's rights activist and founder of the Cairo Foundation for Development and Law; a leading voice against FGM, domestic violence, and for sexual and reproductive health rights in one of the world's highest FGM-prevalence countries.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Egypt's very high FGM prevalence (approximately 87% of women aged 15-49) and the practice's deep social and religious embeddedness created the specific human rights crisis that motivated her advocacy",
            "Egypt's weak domestic violence legal framework — the absence of comprehensive protective legislation — created the legal advocacy gap that her foundation sought to fill",
            "The Arab Spring and its aftermath created both new opportunities and new pressures for women's rights advocacy in Egypt — a rapidly changing political environment in which civil society organizations played a critical role"
        ],
        "effects": [
            "Her foundation's campaigns against FGM have contributed to Egypt's evolving legal framework and enforcement approach to the practice",
            "Legal support for domestic violence survivors — in the absence of comprehensive protective legislation — has provided critical access to justice for women who had limited legal recourse",
            "Her work on sexual and reproductive health education has reached communities where such information was previously inaccessible due to social taboo",
            "Her career contributed to the development of Egyptian civil society's capacity for feminist legal activism — training advocates, documenting cases, and building institutional knowledge"
        ],
        "relationships": [
            {"entity": "Cairo Foundation for Development and Law", "relationship": "FOUNDED_AND_DIRECTS", "note": "Founder and director of the Cairo Foundation for Development and Law — dedicated to FGM eradication, domestic violence support, and women's rights"},
            {"entity": "Female genital mutilation (FGM) in Egypt", "relationship": "CAMPAIGNS_AGAINST", "note": "Her primary advocacy focus is combating FGM in Egypt, one of the world's highest-prevalence countries"},
            {"entity": "Egyptian domestic violence survivors", "relationship": "PROVIDES_LEGAL_SUPPORT_FOR", "note": "Her foundation provides legal support for survivors of domestic violence in a context of weak legal frameworks"},
            {"entity": "Egyptian women's rights movement", "relationship": "LEADER_IN", "note": "One of the leading voices in Egypt's women's rights civil society community"},
            {"entity": "Egyptian criminal law (FGM prohibition)", "relationship": "ADVOCATES_FOR_ENFORCEMENT_OF", "note": "Egypt criminalized FGM in 2008 but enforcement remains weak — her advocacy targets both legal reform and enforcement"}
        ]
    }),

    # 4 — Smaranda Olarinde
    ("smaranda-olarinde", {
        "summary": (
            "Professor Smaranda Olarinde is a Romanian-born Nigerian legal academic and "
            "institution-builder who has built one of the most distinguished careers in "
            "Nigerian legal education — serving as President of the Nigerian Association "
            "of Law Teachers (NALT), the peak professional body for law teachers in Nigeria, "
            "and as Vice-Chancellor of Afe Babalola University in Ado-Ekiti, one of Nigeria's "
            "leading private universities. Her career represents the transnational dimension "
            "of Nigerian legal education: a scholar of European origin who became a senior "
            "figure in Nigerian academic life and used that position to advance both legal "
            "scholarship and the institutional capacity of Nigerian law schools.\n\n"
            "After training in law in Romania and conducting early professional work including "
            "legal research at UNICEF offices in Oyo State and Niger State in the 1990s, "
            "she built her academic career in Nigeria — rising through the law faculty ranks "
            "to full professor and then to leadership positions that took her to the pinnacle "
            "of Nigerian legal academia. Her presidency of NALT placed her in charge of the "
            "professional community of Nigeria's law teachers at a time when Nigerian legal "
            "education was facing significant quality challenges — inadequate physical "
            "infrastructure, faculty shortages, curriculum modernization needs, and the "
            "pressure to integrate international law and new areas like technology law, "
            "environmental law, and human rights law into traditional curricula.\n\n"
            "Her appointment as Vice-Chancellor of Afe Babalola University — an institution "
            "known for its emphasis on law and legal education — extended her impact from "
            "professional association leadership to institutional governance. As vice-chancellor, "
            "she bore responsibility for the university's academic quality, research output, "
            "physical development, and its standing in the competitive Nigerian private "
            "university sector.\n\n"
            "Her career illustrates the contribution of international scholars to Nigerian "
            "academic life — a transnational dimension of Nigeria's legal education system "
            "that has been significant since independence."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Romanian-born Nigerian law professor, President of the Nigerian Association of Law Teachers (NALT), and Vice-Chancellor of Afe Babalola University; a significant figure in Nigerian legal education whose career bridges European and African academic traditions.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Nigeria's legal education system's need for experienced academic leadership — given challenges of faculty quality, curriculum modernization, and institutional development — created the environment in which her scholarly and administrative skills were valued",
            "Her early UNICEF research work in Nigeria connected her to the Nigerian legal and development community, building the professional networks that underpinned her subsequent academic career",
            "The growth of Nigeria's private university sector — which expanded significantly from the 2000s — created new institutional leadership opportunities for distinguished academics"
        ],
        "effects": [
            "Her presidency of NALT provided professional leadership for Nigeria's law teaching community at a critical moment in the development of Nigerian legal education",
            "Her Vice-Chancellorship at Afe Babalola University shaped the academic direction and institutional quality of one of Nigeria's prominent law-focused private universities",
            "Her career as a Romanian-born woman who reached the pinnacle of Nigerian legal academia demonstrated the transnational possibilities of the Nigerian academic system",
            "Her contributions to legal scholarship have advanced Nigerian jurisprudence in areas reflecting her international training and research interests"
        ],
        "relationships": [
            {"entity": "Nigerian Association of Law Teachers (NALT)", "relationship": "PRESIDENT_OF", "note": "President of NALT — the peak professional body for law teachers in Nigeria"},
            {"entity": "Afe Babalola University, Ado-Ekiti", "relationship": "VICE-CHANCELLOR_OF", "note": "Vice-Chancellor of Afe Babalola University — one of Nigeria's leading law-focused private universities"},
            {"entity": "UNICEF Nigeria", "relationship": "CONDUCTED_RESEARCH_FOR", "note": "Worked as legal researcher at UNICEF offices in Oyo State and Niger State in the 1990s — the professional work that first connected her to Nigeria"},
            {"entity": "Nigerian legal education system", "relationship": "SHAPED", "note": "Through NALT presidency and Vice-Chancellorship, she shaped the direction and quality of Nigerian legal education"},
            {"entity": "Romanian-Nigerian academic community", "relationship": "REPRESENTS", "note": "Represents the transnational dimension of Nigerian academia — a Romanian-born scholar who became a senior figure in Nigerian legal academic life"}
        ]
    }),

    # 5 — Vrinda Grover
    ("vrinda-grover", {
        "summary": (
            "Vrinda Grover is a New Delhi-based lawyer, researcher, and human rights advocate "
            "who has spent three decades representing some of India's most politically charged "
            "cases — including survivors of the 1984 anti-Sikh pogrom following Indira Gandhi's "
            "assassination, survivors of the 2002 Gujarat communal violence, victims of custodial "
            "torture, and women and child survivors of sexual violence — making her one of India's "
            "most distinguished and courageous human rights lawyers. Her practice at the "
            "intersection of gender justice, communal violence, and state accountability "
            "has brought her into some of the most difficult legal terrain in Indian democracy.\n\n"
            "Her work on the 1984 violence — the mass killings of Sikhs in New Delhi and other "
            "cities in the days following Indira Gandhi's assassination on 31 October 1984, "
            "in which an estimated 3,000-10,000 people were killed with the apparent complicity "
            "of Congress Party leaders — represents some of the most persistent legal advocacy "
            "in Indian history. For decades after the violence, survivors received neither justice "
            "nor adequate compensation. Grover has appeared in cases demanding accountability "
            "for the 1984 pogrom, facing political and institutional resistance that made "
            "convictions rare and partial.\n\n"
            "Her work on gender-based violence includes representing survivors in high-profile "
            "cases of rape and sexual assault, developing feminist legal arguments about "
            "rape law reform, and contributing to campaigns against the criminalization of "
            "consensual adult relationships. She has advocated for reading of constitutional "
            "rights to dignity, privacy, and equality into India's criminal law framework "
            "as it applies to sexual violence survivors.\n\n"
            "'Justice delayed is not justice — it is a second violence.' Grover's decades "
            "of persistence in cases where the state itself is the accused have exemplified "
            "the courage required of human rights lawyers in democratic systems that "
            "resist accountability."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Indian human rights lawyer who has represented survivors of the 1984 anti-Sikh pogrom, the 2002 Gujarat violence, and gender-based violence over three decades — one of India's most distinguished and courageous human rights advocates.",
            "significanceCategory": "continental"
        },
        "causes": [
            "India's failure to hold perpetrators of the 1984 Sikh pogrom and the 2002 Gujarat violence accountable created the demand for persistent legal advocacy that characterized Grover's career",
            "India's feminist legal movement and the public interest litigation tradition created the institutional framework within which gender justice cases could be brought before courts that had real constitutional power",
            "The intersection of communal violence, state complicity, and gender-based violence in Indian legal history created the specific combination of human rights challenges that define her practice"
        ],
        "effects": [
            "Her sustained advocacy in 1984 anti-Sikh pogrom cases over three decades contributed to the eventual conviction of Congress leader Sajjan Kumar in 2018 — one of the few accountability outcomes in those cases",
            "Her feminist legal arguments on rape law and sexual violence have contributed to the reform of Indian rape law and to feminist jurisprudence on survivor rights",
            "Her advocacy for victims of custodial torture has contributed to documentation and limited accountability for state violence against detainees",
            "Her career has inspired younger Indian human rights lawyers and demonstrated the possibility of sustained legal advocacy in cases the state would prefer to close"
        ],
        "relationships": [
            {"entity": "1984 anti-Sikh pogrom (India)", "relationship": "SEEKS_ACCOUNTABILITY_FOR", "note": "Has advocated for accountability for the 1984 anti-Sikh violence in Delhi and other cities over three decades"},
            {"entity": "2002 Gujarat communal violence", "relationship": "REPRESENTED_SURVIVORS_OF", "note": "Represented survivors of the 2002 Gujarat communal violence as part of her broader human rights practice"},
            {"entity": "Indian Supreme Court / High Courts", "relationship": "ARGUES_BEFORE", "note": "Her human rights cases have been argued before the Supreme Court and High Courts of India"},
            {"entity": "Indian feminist legal movement", "relationship": "LEADS_IN", "note": "A leading figure in the Indian feminist legal tradition, advocating for gender justice through litigation and legal reform"},
            {"entity": "Sajjan Kumar (1984 conviction)", "relationship": "CONTRIBUTED_TO_CONVICTION_OF", "note": "Her sustained advocacy contributed to the 2018 conviction of Congress leader Sajjan Kumar for his role in the 1984 anti-Sikh violence"}
        ]
    }),

    # 6 — Samah Subay
    ("samah-subay", {
        "summary": (
            "Samah Subay is a Yemeni human rights lawyer who has dedicated her work to "
            "documenting and seeking legal redress for one of the most devastating human "
            "rights crises of the 21st century's ongoing conflicts: the enforced disappearances, "
            "arbitrary detention, and torture of thousands of Yemeni civilians by parties "
            "to the Yemeni Civil War that began in 2015 — a conflict involving the Houthi "
            "movement, the internationally recognized Yemeni government, the Saudi-led "
            "military coalition, and various armed factions, all of whom have been credibly "
            "accused of serious human rights violations. Her particular focus is on the "
            "'disappeared' — individuals seized by armed groups and held in undisclosed "
            "locations without charge, trial, or family contact.\n\n"
            "The Yemeni Civil War has produced one of the world's worst humanitarian "
            "catastrophes — tens of thousands of deaths, millions displaced, and a "
            "systematic pattern of enforced disappearances, extrajudicial detention, "
            "and torture attributed to all major parties to the conflict. Subay's "
            "legal work focuses on providing families of disappeared persons with "
            "legal support to locate their loved ones — navigating the chaotic "
            "and opaque detention systems operated by the various conflict parties "
            "in a country where the formal legal system has largely collapsed and "
            "where lawyers who document abuses face serious personal risks.\n\n"
            "Her documentation work — recording the identities, circumstances, and "
            "detention conditions of disappeared persons — serves multiple purposes: "
            "providing families with information, building evidentiary records for "
            "future accountability proceedings, and generating the international "
            "documentation that human rights organizations and UN bodies need to "
            "characterize and publicize the scale of the enforced disappearance crisis.\n\n"
            "Operating as a human rights lawyer in conflict-affected Yemen requires "
            "extraordinary courage — in an environment where legal institutions "
            "have collapsed, where armed groups operate without accountability, "
            "and where lawyers who challenge the powerful face direct personal threats."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Yemeni human rights lawyer providing legal support to families of the disappeared in the Yemeni Civil War; her documentation work creates the evidentiary record of enforced disappearances for future accountability proceedings.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Yemeni Civil War (2015–present) and the systematic enforced disappearances carried out by all parties to the conflict — Houthis, Saudi-led coalition forces, and Yemeni government factions — created the human rights crisis that her work addresses",
            "The collapse of Yemen's formal legal system in the conflict left families of the disappeared with no institutional recourse, creating the need for civil society lawyers like Subay to provide informal legal support",
            "International human rights frameworks criminalizing enforced disappearance — including the International Convention for the Protection of All Persons from Enforced Disappearance — provided the legal standards that frame her documentation and advocacy"
        ],
        "effects": [
            "Her documentation of individual disappearance cases creates the evidentiary foundation for future accountability proceedings — whether before Yemeni courts (if restored), international tribunals, or the UN Panel of Experts on Yemen",
            "Her legal support for families of the disappeared provides them with agency in navigating the opaque detention systems of armed groups",
            "Her work contributes to the international human rights reporting on Yemen's enforced disappearance crisis — generating the documentation that UN bodies, ICRC, and international NGOs depend on",
            "Her continued operation as a human rights lawyer despite personal risk demonstrates the resilience of Yemeni civil society in the face of catastrophic conflict"
        ],
        "relationships": [
            {"entity": "Yemeni Civil War (2015–present)", "relationship": "WORKS_IN_CONTEXT_OF", "note": "Her human rights work directly addresses the enforced disappearances and arbitrary detention patterns created by the Yemeni Civil War"},
            {"entity": "Houthi movement (Ansar Allah)", "relationship": "DOCUMENTS_ABUSES_OF", "note": "Documents enforced disappearances attributed to the Houthi movement alongside abuses by other conflict parties"},
            {"entity": "Families of the disappeared (Yemen)", "relationship": "PROVIDES_LEGAL_SUPPORT_TO", "note": "Her primary clients are families of persons disappeared by armed groups in the Yemeni Civil War"},
            {"entity": "UN Panel of Experts on Yemen", "relationship": "CONTRIBUTES_DOCUMENTATION_TO", "note": "Her documentation work provides evidentiary material for international human rights reporting on Yemen"},
            {"entity": "International Convention Against Enforced Disappearance", "relationship": "APPLIES_STANDARDS_OF", "note": "Her advocacy invokes international legal standards prohibiting enforced disappearance as the framework for documenting abuses"}
        ]
    }),

    # 7 — Zaha Hassan
    ("zaha-hassan", {
        "summary": (
            "Zaha Hassan is a Palestinian-American human rights lawyer, political analyst, "
            "researcher, and author who has built an internationally recognized practice "
            "at the intersection of international human rights law, Palestinian self-determination, "
            "and peace negotiations — combining legal expertise with policy analysis to "
            "advocate for the rights of Palestinians in international forums and to contribute "
            "to scholarly understanding of the Israeli-Palestinian conflict's legal dimensions. "
            "She is a visiting fellow at the Carnegie Endowment for International Peace, one "
            "of the world's leading foreign policy research institutions.\n\n"
            "Hassan's legal work focuses on the application of international law — including "
            "international humanitarian law, human rights law, and the law of belligerent "
            "occupation — to the Israeli-Palestinian conflict. This includes analysis of "
            "Israeli settlement expansion, the legal status of the Gaza blockade, the "
            "rights of Palestinian refugees, and the legal dimensions of the various "
            "peace process frameworks that have been proposed and failed over three decades. "
            "Her writing on the international law dimensions of these questions has "
            "appeared in major policy publications and reached audiences in international "
            "diplomacy and civil society.\n\n"
            "Beyond legal analysis, she is a political analyst who comments on Palestinian "
            "governance, the Hamas-Fatah division, Palestinian institutional development, "
            "and the feasibility of the two-state solution — bringing legal precision to "
            "political debates that are often conducted in the absence of serious "
            "international law analysis. Her work acknowledges both Palestinian "
            "rights under international law and the political realities that constrain "
            "their realization.\n\n"
            "Her position at the Carnegie Endowment provides a platform for advocacy "
            "within the mainstream of American foreign policy discourse — a space "
            "where Palestinian legal and political perspectives have historically "
            "been underrepresented."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Palestinian-American human rights lawyer and Carnegie Endowment fellow who applies international humanitarian law and human rights law to the Israeli-Palestinian conflict; a leading voice for Palestinian legal rights in American foreign policy discourse.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Israeli-Palestinian conflict's complex international law dimensions — occupation law, humanitarian law, refugee rights, settlement law — created the need for legal expertise that could translate between law and policy discourse",
            "Palestinian underrepresentation in mainstream American foreign policy institutions created the need for credentialed Palestinian-American voices like Hassan's in policy research centers like Carnegie",
            "The persistent failure of the Oslo peace process and subsequent frameworks to produce a two-state solution has sustained the academic and advocacy demand for rigorous legal analysis of the conflict's parameters"
        ],
        "effects": [
            "Her legal analysis of Israeli settlement expansion, the Gaza blockade, and Palestinian refugee rights has contributed to international legal and policy discourse on the Israeli-Palestinian conflict",
            "Her Carnegie fellowship has provided a prestigious platform for Palestinian legal perspectives within mainstream American foreign policy discourse",
            "Her political analysis of Palestinian governance and institutional development has contributed to understanding of the internal Palestinian political dynamics that affect peace process viability",
            "Her work has helped bridge the gap between international law academics and foreign policy practitioners in the debate over Palestinian rights"
        ],
        "relationships": [
            {"entity": "Carnegie Endowment for International Peace", "relationship": "VISITING_FELLOW_AT", "note": "Visiting fellow at the Carnegie Endowment — one of the world's leading foreign policy research institutions"},
            {"entity": "Israeli-Palestinian conflict", "relationship": "ANALYZES_LEGAL_DIMENSIONS_OF", "note": "Her legal work focuses on the international law dimensions of the Israeli-Palestinian conflict — occupation law, settlement law, refugee rights, humanitarian law"},
            {"entity": "International humanitarian law (Geneva Conventions)", "relationship": "APPLIES", "note": "A primary framework for her analysis of Israeli military occupation and the laws of war as applied to the Palestinian territories"},
            {"entity": "Palestinian self-determination", "relationship": "ADVOCATES_FOR", "note": "Palestinian self-determination is the core political and legal right that frames her advocacy"},
            {"entity": "American foreign policy discourse on Israel/Palestine", "relationship": "PARTICIPANT_IN", "note": "Her Carnegie position makes her a voice for Palestinian legal perspectives within the mainstream of American foreign policy debate"}
        ]
    }),

    # 8 — Abiola Akiyode-Afolabi
    ("abiola-akiyode-afolabi", {
        "summary": (
            "Abiola Akiyode-Afolabi is a Nigerian lawyer and civil rights activist who "
            "founded and leads the Women Advocates Research and Documentation Centre (WARDC) "
            "— a Lagos-based non-governmental organization dedicated to advancing women's "
            "reproductive rights, maternal health, and gender justice in Nigeria through "
            "legal advocacy, policy research, community education, and litigation. "
            "Her career spans legal practice, academic teaching, civil society leadership, "
            "and policy advocacy in one of Africa's largest and most socially complex nations.\n\n"
            "WARDC's work addresses some of Nigeria's most acute gender justice challenges: "
            "the country has one of the world's highest rates of maternal mortality — "
            "driven by inadequate access to skilled birth attendance, unsafe abortion, "
            "and poor reproductive health services — while simultaneously maintaining "
            "legal frameworks that restrict women's bodily autonomy, particularly "
            "around abortion. Akiyode-Afolabi's organization has worked to document "
            "maternal mortality as a human rights issue, advocate for legal reform of "
            "Nigeria's restrictive abortion laws, and provide legal support for "
            "women whose reproductive rights have been violated.\n\n"
            "Her advocacy extends to broader gender justice issues including violence "
            "against women, women's political participation, and the enforcement of "
            "Nigeria's Violence Against Persons Prohibition (VAPP) Act — the federal "
            "legislation that criminalized gender-based violence but whose enforcement "
            "remains inconsistent across Nigeria's states. She has been a consistent "
            "voice in Nigerian civil society for the legislative and policy changes "
            "needed to bring Nigeria's legal framework into alignment with its "
            "international human rights commitments.\n\n"
            "Her career exemplifies the Nigerian model of the lawyer-activist who "
            "uses legal expertise not primarily in private practice but as a tool "
            "for civil society advocacy — building institutions, conducting research, "
            "and generating the evidence base for policy change."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Nigerian lawyer and founder of WARDC (Women Advocates Research and Documentation Centre); a leading advocate for women's reproductive rights, maternal health as a human right, and enforcement of the Violence Against Persons Prohibition Act in Nigeria.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Nigeria's extremely high maternal mortality rate — one of the world's highest — combined with restrictive abortion laws and inadequate reproductive health services created the specific human rights crisis that WARDC was founded to address",
            "Nigeria's passage of the Violence Against Persons Prohibition Act (VAPP) created new legal tools that required civil society organizations like WARDC to advocate for enforcement and implementation",
            "The Nigerian feminist legal movement's tradition of using civil society organizations as vehicles for legal advocacy and policy change provided the model that Akiyode-Afolabi followed in founding WARDC"
        ],
        "effects": [
            "WARDC has produced significant documentation of maternal mortality as a human rights issue in Nigeria, shifting the framing from a public health to a rights question",
            "Her advocacy has contributed to debates about reforming Nigeria's restrictive abortion laws — a politically sensitive issue in Nigeria's predominantly religious public culture",
            "Her legal support work has provided direct assistance to women whose reproductive rights and gender-based violence protections have been violated",
            "Her consistent advocacy for VAPP enforcement has contributed to the gradual expansion of the law's implementation across Nigerian states"
        ],
        "relationships": [
            {"entity": "Women Advocates Research and Documentation Centre (WARDC)", "relationship": "FOUNDED_AND_LEADS", "note": "Founder and Director of WARDC — a Lagos-based NGO dedicated to women's reproductive rights, maternal health, and gender justice in Nigeria"},
            {"entity": "Nigeria Violence Against Persons Prohibition (VAPP) Act", "relationship": "ADVOCATES_FOR_ENFORCEMENT_OF", "note": "A consistent advocate for the enforcement and state-by-state implementation of Nigeria's VAPP Act"},
            {"entity": "Nigerian maternal mortality crisis", "relationship": "DOCUMENTS_AND_CAMPAIGNS_AGAINST", "note": "Has documented Nigeria's high maternal mortality rate as a human rights issue, framing it as a failure of reproductive rights"},
            {"entity": "Nigerian feminist legal movement", "relationship": "PART_OF", "note": "A leading figure in the broader Nigerian feminist legal and civil society movement for women's rights"},
            {"entity": "Nigerian abortion law reform debate", "relationship": "PARTICIPANT_IN", "note": "A voice in Nigeria's politically sensitive debate about reforming restrictive abortion laws to protect women's reproductive rights"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 21)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
