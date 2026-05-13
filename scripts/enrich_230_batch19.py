#!/usr/bin/env python3
"""
Batch 19 — 8 entities (imp=8 contemporary legal figures + 1 historical):
Diego Vigil y Cocaña, Leilani Farha, Nisha Rao, Samuel Nguiffo,
Saleh Nikbakht, Nana Oye Lithur, Funmi Falana, Zahara Nampewo
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

    # 1 — Diego Vigil y Cocaña (c.1794–c.1845) — last president, Federal Republic of Central America
    ("diego-vigil-y-cocaña", {
        "summary": (
            "Diego Vigil y Cocaña (c.1794–c.1845) was a Central American liberal politician and "
            "lawyer who presided over the final dissolution of one of the hemisphere's most ambitious "
            "republican experiments: the Federal Republic of Central America (1823–1839). As the last "
            "Supreme Chief (head of state) of the collapsing federation (1839–1840), he witnessed "
            "and presided over the final fragmentation of a state that had sought to unite present-day "
            "Guatemala, El Salvador, Honduras, Nicaragua, and Costa Rica into a single constitutional "
            "republic modeled on the United States — a project whose failure shaped the political "
            "landscape of Central America for the following two centuries.\n\n"
            "Vigil y Cocaña's political career spanned the turbulent decades of post-independence "
            "Central American politics. He served as chief of state of Honduras (1829) and of El "
            "Salvador, navigating the chronic conflicts between the liberal federalist faction led "
            "by General Francisco Morazán — who sought to maintain the federal union and impose "
            "liberal reforms — and the conservative regionalist forces backed by the Guatemalan "
            "elite and the Catholic Church hierarchy that sought state autonomy and the preservation "
            "of colonial social structures. By the time Vigil reached the federation's presidency, "
            "Morazán's power had collapsed and the federation was disintegrating into its constituent "
            "states.\n\n"
            "The failure of the Federal Republic of Central America — to which Vigil's presidency "
            "was the melancholy coda — became one of the defining cautionary tales of Latin American "
            "political history: an attempt at federal liberal republicanism undermined by fiscal "
            "incapacity, regional jealousies, military conflict, and the mobilization of the rural "
            "poor by conservative elites against liberal reforms. Morazán's Central American "
            "Federation became the great 'what might have been' of isthmus history.\n\n"
            "Vigil y Cocaña's position at the wreckage of the federation made him a figure of "
            "historical melancholy — the man holding the last pieces of an impossible republic "
            "as they finally came apart."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Last Supreme Chief of the Federal Republic of Central America (1839–1840), presiding over the final dissolution of the post-independence federal union; his presidency marked the end of the most ambitious republican experiment in Central American history.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The liberal federalist project of Francisco Morazán — which had sought to maintain a unified Central American republic against conservative regionalist fragmentation — collapsed militarily and politically by 1839, leaving Vigil to preside over the disintegration",
            "The chronic fiscal weakness of the Federal Republic, combined with military conflicts between the federation's liberal government and conservative regional elites backed by Guatemala and the Church, made the federation's failure structural",
            "The mobilization of the rural Guatemalan poor (the Carrera rebellion) against liberal reforms — secular land reorganization, the Livingston Code's attempt to introduce common law procedures — delivered the final blow to Morazán's federation"
        ],
        "effects": [
            "The dissolution of the federation under Vigil's brief presidency created five separate Central American republics — Guatemala, El Salvador, Honduras, Nicaragua, Costa Rica — a fragmentation that persists to the present day",
            "The failure of the federation became a defining reference point in Central American political culture: subsequent liberals repeatedly invoked Central American union as an unrealized ideal, inspiring multiple unification attempts throughout the 19th century",
            "The collapse illustrated the limits of liberal constitutionalism in early 19th-century Latin America when applied without adequate institutional foundations, fiscal capacity, or popular support",
            "Vigil's earlier service as chief of state in both Honduras and El Salvador illustrated the pattern of liberal politicians cycling through different state offices in the unstable Central American political system"
        ],
        "relationships": [
            {"entity": "Federal Republic of Central America", "relationship": "LAST_PRESIDENT_OF", "note": "Supreme Chief (head of state) of the Federal Republic of Central America (1839–1840), presiding over its final dissolution"},
            {"entity": "Francisco Morazán", "relationship": "SUCCEEDED_IN_COLLAPSE_OF", "note": "Vigil's brief presidency came after the military defeat and exile of Morazán, the federation's primary champion"},
            {"entity": "Honduras", "relationship": "GOVERNED", "note": "Served as chief of state of Honduras (1829)"},
            {"entity": "El Salvador", "relationship": "GOVERNED", "note": "Served as chief of state of El Salvador"},
            {"entity": "Central American liberal federalist movement", "relationship": "AFFILIATED_WITH", "note": "A committed liberal who supported the federalist project against conservative regionalist fragmentation"}
        ]
    }),

    # 2 — Leilani Farha (b. 1965)
    ("leilani-farha", {
        "summary": (
            "Leilani Farha (b. 1965) is a Canadian human rights lawyer whose six-year tenure as "
            "United Nations Special Rapporteur on adequate housing (2014–2020) made her one of the "
            "most influential international advocates for the recognition of housing as a fundamental "
            "human right — a campaign that placed her in direct confrontation with the global "
            "financial systems that treat housing primarily as an investment asset and profit center "
            "rather than as a social necessity. Appointed by the UN Human Rights Council, she brought "
            "unprecedented visibility to the structural drivers of the global housing crisis.\n\n"
            "In her UN role, Farha conducted country visits, issued reports, and engaged governments "
            "on housing rights violations globally. Her most influential contribution was her analysis "
            "of the 'financialization of housing' — the process by which global real estate has been "
            "transformed into an asset class for institutional investors (private equity funds, "
            "REITs, sovereign wealth funds), driving up prices in major cities worldwide, displacing "
            "lower-income residents, and making affordable housing increasingly inaccessible. Her "
            "2017 report on financialization to the UN General Assembly became a landmark document "
            "in international housing rights discourse.\n\n"
            "Following her UN tenure, she became Global Director of THE SHIFT — an international "
            "campaign she founded to reverse the commodification of housing and realize housing as "
            "a human right under international law. She has also been the subject of the 2021 "
            "documentary film 'Push' (directed by Fredrik Gertten), which brought her housing "
            "rights arguments to a global audience. She has worked to hold corporations and financial "
            "institutions accountable under international human rights law — an area of emerging "
            "legal development that challenges the conventional understanding of human rights as "
            "obligations of governments alone.\n\n"
            "'Housing is not a commodity — it is a human right.' Farha's demand challenged a "
            "global system in which the homes of the poor have become the investment vehicles "
            "of the wealthy."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "UN Special Rapporteur on adequate housing (2014–2020) who made the concept of 'financialization of housing' central to international human rights discourse; founder of THE SHIFT campaign for housing as a human right.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The global financialization of real estate from the 1980s onward — the transformation of housing into a global asset class — created the housing affordability crisis that motivated Farha's advocacy and provided the structural target for her UN investigations",
            "The UN Special Rapporteur mechanism provided an institutional platform from which a single lawyer could command global attention, conduct country visits, and issue reports with international legal authority",
            "The gap between the formal recognition of housing as a human right (Universal Declaration of Human Rights, ICESCR) and the reality of millions living in inadequate housing globally provided the mandate for her advocacy"
        ],
        "effects": [
            "Her 2017 UN report on the financialization of housing became a landmark international document that shifted the framing of the housing crisis from a supply problem to a human rights and economic structure problem",
            "THE SHIFT campaign she founded has engaged cities, civil society organizations, and UN bodies worldwide in efforts to move housing policy away from market-driven models",
            "The 2021 documentary 'Push' brought her housing rights arguments to a global public audience far beyond the UN system",
            "Her advocacy contributed to the growing movement to hold corporations and financial institutions accountable under international human rights law — extending human rights obligations beyond states"
        ],
        "relationships": [
            {"entity": "UN Human Rights Council", "relationship": "APPOINTED_BY", "note": "Appointed as UN Special Rapporteur on adequate housing by the UN Human Rights Council (2014–2020)"},
            {"entity": "THE SHIFT (housing rights campaign)", "relationship": "FOUNDED", "note": "Founded and became Global Director of THE SHIFT, an international campaign to realize housing as a human right"},
            {"entity": "Universal Declaration of Human Rights / ICESCR", "relationship": "APPLIED", "note": "Her advocacy drew on UDHR Article 25 and the ICESCR's recognition of the right to an adequate standard of living including housing"},
            {"entity": "Global financial system / real estate financialization", "relationship": "CHALLENGED", "note": "Her core argument challenged the financial system's treatment of housing as an investment asset rather than a social right"},
            {"entity": "Fredrik Gertten (documentary 'Push' 2021)", "relationship": "DOCUMENTED_BY", "note": "The documentary 'Push' (2021) brought her housing rights advocacy to a global audience"}
        ]
    }),

    # 3 — Nisha Rao (b. c.1993)
    ("nisha-rao", {
        "summary": (
            "Nisha Rao (b. c.1993) is a Pakistani transgender lawyer and human rights advocate "
            "who became internationally celebrated in 2020 as the first transgender person to "
            "graduate from law school in Pakistan — and subsequently to register as an advocate "
            "at the bar — in a country where transgender individuals (known locally as khwaja siras "
            "or hijras) have historically faced severe social stigma, family rejection, exclusion "
            "from education and formal employment, and physical violence. Her achievement was "
            "recognized globally as a landmark moment for transgender rights in South Asia.\n\n"
            "Rao's path to the law was marked by extraordinary obstacles. She was rejected by her "
            "family when she transitioned, lived in poverty in Karachi, and pursued her legal "
            "education despite the social exclusion, harassment, and discrimination that characterize "
            "the experience of transgender people in Pakistan's educational institutions. She "
            "graduated from the University of Karachi's law faculty, passed the Sindh Bar Council's "
            "examination, and was enrolled as an advocate — becoming the first transgender lawyer "
            "in Pakistan's history. Her story received major international media coverage and "
            "became a symbol of resistance against transgender discrimination in South Asia.\n\n"
            "Her legal practice focuses on the representation of Pakistan's transgender community "
            "— a population that has historically had no access to formal legal protection and "
            "whose interests have been ignored by the legal system. Pakistan's Transgender Persons "
            "(Protection of Rights) Act (2018) had provided a legal framework for transgender "
            "recognition, but enforcement remained weak and social discrimination persisted. "
            "Rao positioned herself as an advocate who could bridge the gap between formal legal "
            "rights and the lived reality of transgender people in Pakistan.\n\n"
            "Her achievement demonstrated that the barriers facing transgender people in "
            "professional and legal life are survivable — and turned her into an international "
            "icon for transgender rights in contexts of systemic discrimination."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "First transgender person to graduate from law school and register as an advocate in Pakistan (2020); her achievement became an international landmark for transgender rights in South Asia and a symbol of overcoming structural discrimination.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Pakistan's historic social marginalization of transgender people (khwaja siras/hijras) — exclusion from family, education, employment, and legal protection — created the structural discrimination that made Rao's achievement both necessary and extraordinary",
            "Pakistan's Transgender Persons (Protection of Rights) Act (2018) provided a legal framework for gender recognition that created the formal possibility of transgender participation in the legal profession",
            "Her personal determination to pursue legal education despite family rejection, poverty, and institutional discrimination — an individual achievement against systemic barriers"
        ],
        "effects": [
            "Her enrollment at the Sindh Bar became an international media story that raised global awareness of transgender rights in Pakistan and South Asia",
            "Her legal practice provides representation to Pakistan's transgender community — a population historically excluded from the legal system's protection",
            "Her example has inspired other transgender individuals in Pakistan to pursue higher education and professional careers in the face of discrimination",
            "Her story contributed to international pressure on Pakistan to enforce the Transgender Persons Act and improve the lived reality of transgender people beyond formal legal recognition"
        ],
        "relationships": [
            {"entity": "Sindh Bar Council", "relationship": "REGISTERED_WITH", "note": "Registered as an advocate with the Sindh Bar Council after graduating from the University of Karachi — first transgender person to do so in Pakistan"},
            {"entity": "University of Karachi (law faculty)", "relationship": "GRADUATED_FROM", "note": "Graduated from the University of Karachi law faculty in 2020, becoming the first transgender law graduate in Pakistan"},
            {"entity": "Pakistan Transgender Persons (Protection of Rights) Act 2018", "relationship": "OPERATES_UNDER", "note": "Her legal practice advances the protection of rights formally recognized by Pakistan's 2018 Transgender Act"},
            {"entity": "Pakistani transgender community (khwaja siras)", "relationship": "ADVOCATES_FOR", "note": "Focuses her legal practice on representing Pakistan's historically marginalized transgender community"},
            {"entity": "South Asian transgender rights movement", "relationship": "SYMBOL_OF", "note": "Her achievement made her an international symbol of transgender rights advancement in South Asia"}
        ]
    }),

    # 4 — Samuel Nguiffo (b. 1966)
    ("samuel-nguiffo", {
        "summary": (
            "Samuel Nguiffo (b. 1966) is a Cameroonian lawyer and environmental activist who "
            "has spent more than three decades defending the rights of Central Africa's indigenous "
            "forest communities — particularly the Baka and Bagyeli peoples of Cameroon's Congo "
            "Basin rainforest — against the extractive industries, large-scale infrastructure "
            "projects, and government forestry policies that threaten both the forest ecosystem "
            "and the communities whose cultures and livelihoods depend on it. He is the Secretary "
            "General of the Center for Environment and Development (CED) in Yaoundé, one of "
            "Central Africa's most respected environmental law organizations.\n\n"
            "Nguiffo's legal activism combines grassroots community organizing with international "
            "legal advocacy. At the national level, he has challenged Cameroonian forestry law "
            "through litigation, policy research, and public engagement — arguing for community "
            "forest rights and the legal recognition of indigenous land tenure in a country where "
            "the legal framework has historically treated forest land as state property available "
            "for commercial exploitation. At the international level, he has engaged the "
            "major multilateral development banks and international timber certification bodies "
            "to demand higher standards for indigenous community consultation and consent (FPIC) "
            "in projects affecting forest communities.\n\n"
            "In 1999, he was awarded the Goldman Environmental Prize — the world's most prestigious "
            "award for grassroots environmental activism — for his work protecting the tropical "
            "rainforests of Central Africa and the rights of the forest peoples who inhabit them. "
            "The Goldman Prize brought international attention to his work and established him as "
            "a globally recognized figure in environmental law and forest rights advocacy.\n\n"
            "Nguiffo's career has demonstrated that legal tools — community rights litigation, "
            "regulatory advocacy, international standards engagement — can serve as effective "
            "instruments for environmental protection in contexts where communities lack the "
            "political power to defend their interests through conventional means."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Cameroonian environmental lawyer and Goldman Environmental Prize laureate (1999); Secretary General of the Center for Environment and Development (CED); leading advocate for indigenous forest community rights in Central Africa's Congo Basin.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The systematic threat to Central Africa's Congo Basin rainforest from commercial logging, agro-industrial expansion, and infrastructure projects created the environmental and human rights crisis that motivated Nguiffo's career",
            "The absence of legal protection for indigenous forest community land rights under Cameroonian law — which treats forest land as state property — made legal advocacy essential for communities with no other political leverage",
            "International environmental rights frameworks and the Goldman Prize network provided both recognition and resources that amplified his advocacy beyond national borders"
        ],
        "effects": [
            "The Goldman Environmental Prize (1999) brought international recognition to the forest rights struggle in Cameroon and Central Africa, attracting global attention and resources",
            "CED's legal research and advocacy have contributed to improved community forestry provisions in Cameroonian law and to higher FPIC standards for development projects affecting forest communities",
            "His work established a model of environmental law practice in Africa that combines community rights litigation with international regulatory engagement",
            "His decades of advocacy helped build Central Africa's civil society infrastructure for environmental law, training a generation of environmental lawyers and community organizers"
        ],
        "relationships": [
            {"entity": "Center for Environment and Development (CED), Yaoundé", "relationship": "LEADS", "note": "Secretary General of CED, Cameroon's leading environmental law and forest rights organization"},
            {"entity": "Goldman Environmental Prize", "relationship": "AWARDED", "note": "Received the Goldman Environmental Prize in 1999 for protecting Central Africa's tropical rainforests and indigenous community rights"},
            {"entity": "Baka and Bagyeli peoples (Congo Basin)", "relationship": "ADVOCATES_FOR", "note": "His primary advocacy clients are the indigenous Baka and Bagyeli forest communities of Cameroon"},
            {"entity": "Congo Basin rainforest", "relationship": "DEFENDS", "note": "His career has been devoted to protecting the legal and environmental integrity of the Congo Basin — the world's second largest tropical rainforest"},
            {"entity": "Free, Prior and Informed Consent (FPIC) standard", "relationship": "ADVANCES", "note": "A leading voice for FPIC standards in Cameroonian and international law governing development projects affecting indigenous forest communities"}
        ]
    }),

    # 5 — Saleh Nikbakht (b. c.1955)
    ("saleh-nikbakht", {
        "summary": (
            "Saleh Nikbakht is an Iranian human rights lawyer who has dedicated his career to "
            "defending some of Iran's most politically vulnerable defendants — political prisoners, "
            "journalists, civil society activists, labor organizers, ethnic and religious minorities, "
            "and protesters — before the Islamic Republic's security-focused courts, where "
            "acquittals are rare and the pressure on defense lawyers to withdraw from sensitive "
            "cases is intense and often physical. As spokesman for the Society of Political "
            "Prisoners in Iran, he became one of the most publicly visible advocates for "
            "political prisoners' rights in the country.\n\n"
            "Nikbakht worked as defense counsel in a series of high-profile cases including "
            "those arising from the 2009 Green Movement — the mass protests against the disputed "
            "re-election of President Mahmoud Ahmadinejad that were met with mass arrests, "
            "torture, and executions. He defended activists, journalists, and opposition figures "
            "charged with national security offenses — the catch-all charges used by Iran's "
            "judiciary to criminalize political dissent. He also defended members of religious "
            "minorities including Baha'is who faced prosecution for their faith.\n\n"
            "His legal work exposed him to professional sanction and personal risk. Iranian "
            "human rights lawyers who defend political prisoners routinely face suspension of "
            "their law licenses, prosecution for their own advocacy, and imprisonment. Nikbakht "
            "navigated this environment while maintaining a public profile that made him a "
            "recognized voice internationally for Iran's political prisoners. His academic role "
            "as a law professor provided an additional platform for his analysis of the gap "
            "between Iran's formal legal framework and the treatment of political defendants.\n\n"
            "His career exemplified the courage required of lawyers who defend political clients "
            "in authoritarian systems — where the act of legal defense itself becomes an act "
            "of political resistance."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Iranian human rights lawyer and spokesman for the Society of Political Prisoners in Iran; defended political prisoners, journalists, religious minorities, and Green Movement activists before Iran's security courts.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Iran's Islamic Republic's use of national security laws and revolutionary courts to criminalize political dissent created the demand for defense lawyers willing to take politically dangerous cases",
            "The 2009 Green Movement's mass arrests created a wave of political defendants who needed legal representation in a system designed to convict rather than acquit them",
            "His personal commitment to legal principle over personal safety — a commitment shared by a small community of Iranian human rights lawyers including Nasrin Sotoudeh and Abdolfattah Soltani"
        ],
        "effects": [
            "His public role as spokesman for Iran's political prisoners gave an organized voice to a population otherwise isolated behind prison walls",
            "His defense work in high-profile cases — even when it did not produce acquittals — created a legal record, publicized the conditions of detention, and provided defendants with some procedural protection",
            "His exposure of the gap between Iran's formal legal framework and the actual treatment of political defendants contributed to international human rights reporting on Iran's judiciary",
            "His survival in a professional environment that has imprisoned and silenced many of his colleagues made him a symbol of the resilience of Iran's human rights legal community"
        ],
        "relationships": [
            {"entity": "Society of Political Prisoners in Iran", "relationship": "SPOKESPERSON_FOR", "note": "Served as spokesman for the Society of Political Prisoners, giving organized public voice to Iran's political prisoner population"},
            {"entity": "Iranian Green Movement (2009)", "relationship": "DEFENDED_VICTIMS_OF", "note": "Provided defense counsel for Green Movement activists arrested after the 2009 post-election protests"},
            {"entity": "Baha'i community of Iran", "relationship": "DEFENDED", "note": "Defended Baha'i defendants facing prosecution for their religious beliefs"},
            {"entity": "Iranian Revolutionary Courts", "relationship": "ARGUED_BEFORE", "note": "His practice brought him before Iran's Revolutionary Courts — the specialized courts used for national security and political cases"},
            {"entity": "Nasrin Sotoudeh / Iranian human rights legal community", "relationship": "PART_OF", "note": "Part of the small community of Iranian human rights lawyers who take political prisoner cases at significant personal risk"}
        ]
    }),

    # 6 — Nana Oye Lithur (b. c.1960)
    ("nana-oye-lithur", {
        "summary": (
            "Nana Oye Bampoe Addo (b. c.1960), widely known by her former name Nana Oye Lithur, "
            "is a Ghanaian human rights barrister and politician who has spent her career advocating "
            "for the rights of Ghana's most marginalized populations — women, children, people "
            "with disabilities, and LGBTQ+ individuals — in a country where the last of these "
            "positions has made her politically controversial. A lawyer by training and a prominent "
            "civil society figure, she became one of Ghana's most visible human rights voices "
            "before entering government under President John Mahama.\n\n"
            "Lithur's advocacy career focused on bringing Ghana's human rights framework into "
            "conformity with international standards — including through the African Commission on "
            "Human and Peoples' Rights and the UN human rights treaty bodies. She argued for the "
            "legal recognition and protection of marginalized groups under both Ghanaian law and "
            "African international human rights law. Her willingness to speak publicly about "
            "the rights of LGBTQ+ people in Ghana — where same-sex conduct is criminalized — "
            "placed her at the center of intense public controversy.\n\n"
            "From 2013 to 2017, she served as Ghana's Minister for Gender, Children and Social "
            "Protection under President John Mahama — a portfolio that placed her in charge of "
            "policy on women's rights, child welfare, and social safety nets. In her ministerial "
            "role she worked to expand Ghana's social protection programs and to strengthen "
            "enforcement of the Domestic Violence Act. She subsequently served in other senior "
            "government roles, including Deputy Chief of Staff (Administration) at the "
            "Presidency.\n\n"
            "Her career illustrated the tensions that arise when international human rights "
            "commitments — including protections for LGBTQ+ persons — encounter the social "
            "and religious conservatism of West African political culture."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Ghanaian human rights barrister and Minister for Gender, Children and Social Protection (2013–2017); a prominent advocate for women's rights, child welfare, and the controversial cause of LGBTQ+ rights in Ghana.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Ghana's constitutional commitment to human rights combined with the persistence of social discrimination against women, children, and minorities created the advocacy space that Lithur occupied for decades",
            "President Mahama's progressive political orientation created the political opportunity for Lithur's appointment as Minister for Gender, Children and Social Protection",
            "International human rights frameworks — particularly CEDAW, the African Charter, and the UN Convention on the Rights of the Child — provided the legal tools that anchored her advocacy"
        ],
        "effects": [
            "Her ministerial tenure (2013–2017) expanded Ghana's social protection programs and strengthened enforcement of the Domestic Violence Act",
            "Her public advocacy for LGBTQ+ rights — a position rare among senior Ghanaian politicians — generated national debate about the limits of human rights protection in conservative religious contexts",
            "Her career demonstrated that international human rights lawyering can translate into government policy when political alignment is achieved",
            "As a prominent woman in senior government and legal roles, she contributed to the visibility of women in Ghanaian public life"
        ],
        "relationships": [
            {"entity": "President John Mahama (Ghana)", "relationship": "SERVED_UNDER", "note": "Minister for Gender, Children and Social Protection under President Mahama (2013–2017)"},
            {"entity": "African Commission on Human and Peoples' Rights", "relationship": "ENGAGED_WITH", "note": "Engaged the African Commission in advocacy for the rights of marginalized populations under African human rights law"},
            {"entity": "LGBTQ+ rights in Ghana", "relationship": "ADVOCATED_FOR", "note": "One of Ghana's most prominent politicians to speak publicly for LGBTQ+ rights — a highly controversial position in Ghanaian public life"},
            {"entity": "Ghana Domestic Violence Act", "relationship": "ENFORCED_AS_MINISTER", "note": "Worked to strengthen enforcement of Ghana's Domestic Violence Act during her ministerial tenure"},
            {"entity": "Ghanaian civil society human rights community", "relationship": "MEMBER_OF", "note": "Built her reputation as a barrister and human rights advocate before entering government"}
        ]
    }),

    # 7 — Funmi Falana (b. c.1965)
    ("funmi-falana", {
        "summary": (
            "Funmi Falana, SAN (b. c.1965), is a Nigerian lawyer who holds the rank of Senior "
            "Advocate of Nigeria — the highest designation in the Nigerian legal profession, "
            "equivalent to the Queen's Counsel designation in Commonwealth systems — and is "
            "one of Nigeria's most prominent women's rights and civil liberties advocates. "
            "A partner in the law firm Falana & Falana — which she operates alongside her husband, "
            "the prominent human rights lawyer Femi Falana, SAN — she has built an independent "
            "record of advocacy across Nigeria's most important civil liberties issues.\n\n"
            "Her legal practice encompasses commercial litigation, constitutional law, and human "
            "rights advocacy with particular emphasis on the rights of women in Nigeria's legal "
            "system — including property rights, matrimonial law, and the right of women to "
            "participate equally in economic and civic life. She has litigated significant "
            "cases in Nigeria's federal courts and has been a vocal public advocate for legal "
            "reform on women's issues in a country where customary law, statutory law, and "
            "religious law interact in complex and sometimes contradictory ways.\n\n"
            "Falana's elevation to the rank of Senior Advocate of Nigeria placed her among a "
            "small and highly selective group of practitioners recognized by the Nigerian "
            "Supreme Court as having made exceptional contributions to the legal profession "
            "in advocacy and jurisprudence. As of recent years, fewer than 5% of Nigerian "
            "lawyers hold the SAN designation, making it a significant mark of distinction. "
            "Her visibility as a woman holding this rank has made her a role model for women "
            "entering the Nigerian legal profession.\n\n"
            "Together with her husband, she represents the most prominent public legal couple "
            "in Nigeria's human rights movement — a sustained multi-decade commitment "
            "to the use of law as a tool of civic liberation."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Nigerian Senior Advocate of Nigeria (SAN) and women's rights advocate; partner in the prominent civil liberties firm Falana & Falana; one of Nigeria's most visible women in the upper ranks of the legal profession.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Nigeria's gender-structured legal inequalities — in property rights, matrimonial law, and civic participation — created the advocacy agenda that shaped her career",
            "The tradition of civil liberties lawyering established by her husband Femi Falana and Nigeria's human rights bar provided the professional context in which she developed her own independent practice",
            "Nigeria's SAN designation system — which selectively elevates a small percentage of outstanding advocates — provided the professional recognition framework that validated her legal achievement"
        ],
        "effects": [
            "Her SAN rank made her one of the most senior women in the Nigerian legal profession and a visible model for women entering the field",
            "Her women's rights litigation contributed to the development of Nigerian jurisprudence on gender equality in property, matrimonial, and constitutional law",
            "Falana & Falana became one of Nigeria's most prominent human rights law firms, combining her and her husband's complementary advocacy to constitute a formidable civil liberties practice",
            "Her sustained public advocacy contributed to national conversations about gender equality in Nigerian law and civic life"
        ],
        "relationships": [
            {"entity": "Femi Falana, SAN", "relationship": "PARTNER_AND_SPOUSE_OF", "note": "Legal partner and spouse of Femi Falana SAN — together they constitute the most prominent legal couple in Nigeria's human rights movement"},
            {"entity": "Falana & Falana law firm", "relationship": "PARTNER_IN", "note": "Co-founded and serves as partner in the Falana & Falana civil liberties law firm"},
            {"entity": "Supreme Court of Nigeria", "relationship": "DESIGNATED_BY", "note": "The Senior Advocate of Nigeria (SAN) designation is conferred by the Supreme Court of Nigeria on outstanding advocates"},
            {"entity": "Nigerian women's rights movement", "relationship": "CONTRIBUTES_TO", "note": "A leading figure in the legal dimension of Nigerian women's rights advocacy, litigating cases on property rights, matrimonial law, and civic participation"},
            {"entity": "Nigerian legal profession", "relationship": "DISTINGUISHED_MEMBER_OF", "note": "Her SAN rank places her among the select upper tier of Nigeria's legal profession"}
        ]
    }),

    # 8 — Zahara Nampewo
    ("zahara-nampewo", {
        "summary": (
            "Dr. Zahara Nampewo is a Ugandan lawyer, human rights activist, and legal academic "
            "who serves as the Executive Director of the Human Rights and Peace Centre (HURIPEC) "
            "at Makerere University School of Law in Kampala — Uganda's and East Africa's most "
            "prominent human rights law research and education center. Her career bridges legal "
            "academia, human rights research, and policy advocacy on Uganda's most pressing "
            "rights challenges, including the treatment of marginalized communities, the "
            "conditions of Uganda's criminal justice and prison system, and the interface between "
            "customary law, religious law, and constitutional rights in East African legal contexts.\n\n"
            "Nampewo's academic and advocacy work addresses fundamental tensions in Uganda's "
            "legal system: the commitments made in Uganda's 1995 Constitution — one of Africa's "
            "most rights-expansive constitutional documents — and the practical realities of "
            "judicial capacity, legal culture, and political will. Her research has examined "
            "criminal justice reform, prison conditions, the rights of vulnerable populations, "
            "and the role of law in post-conflict reconciliation in the broader East African context.\n\n"
            "HURIPEC, which she leads, is a foundational institution of Uganda's human rights "
            "civil society — training human rights advocates, conducting policy research, and "
            "providing documentation of rights conditions that informs both domestic advocacy "
            "and international human rights reporting on Uganda. Under her leadership it has "
            "served as a bridge between Makerere's legal academia and Uganda's wider civil "
            "society organizations.\n\n"
            "Her work represents the emerging model of the African human rights legal academic "
            "who combines scholarly research with institutional leadership and practical "
            "advocacy — building the institutional infrastructure of the rule of law "
            "rather than only litigating individual cases."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Executive Director of HURIPEC at Makerere University School of Law; a leading Ugandan human rights lawyer and academic whose work bridges legal scholarship, criminal justice reform advocacy, and civil society capacity-building in East Africa.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Uganda's 1995 Constitution established one of Africa's most comprehensive rights frameworks, creating both the promise of rights protection and the gap between constitutional commitments and practical implementation that drives advocacy",
            "Makerere University's position as East Africa's premier academic institution gave HURIPEC the institutional credibility and student talent pool to become a regional center for human rights legal education",
            "The scale of Uganda's criminal justice challenges — overcrowded prisons, pre-trial detention, access to justice deficits — created the agenda for her research and advocacy work"
        ],
        "effects": [
            "Under her leadership, HURIPEC has trained a generation of Ugandan and East African human rights lawyers and advocates",
            "Her research contributions have informed domestic advocacy on criminal justice reform and the conditions of Uganda's prison system",
            "HURIPEC's documentation work provides the evidentiary base for international human rights reporting on Uganda by UN treaty bodies and international NGOs",
            "Her career model of the academic-activist has contributed to the development of East Africa's human rights legal academic tradition"
        ],
        "relationships": [
            {"entity": "Human Rights and Peace Centre (HURIPEC), Makerere University", "relationship": "DIRECTS", "note": "Executive Director of HURIPEC at Makerere University School of Law — East Africa's most prominent human rights law research center"},
            {"entity": "Makerere University School of Law", "relationship": "AFFILIATED_WITH", "note": "Based at Makerere University in Kampala, which provides HURIPEC's institutional home"},
            {"entity": "Uganda Constitution 1995", "relationship": "ENGAGES_WITH", "note": "Her research engages the implementation gap between Uganda's rights-expansive 1995 Constitution and the practical reality of rights protection"},
            {"entity": "Uganda criminal justice system", "relationship": "RESEARCHES_AND_ADVOCATES_ON", "note": "Criminal justice reform and prison conditions are a primary focus of her research and advocacy"},
            {"entity": "East African human rights civil society", "relationship": "CONTRIBUTES_TO", "note": "HURIPEC under her leadership is a foundational institution of Uganda's and East Africa's human rights civil society infrastructure"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 19)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
