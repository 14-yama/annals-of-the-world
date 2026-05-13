#!/usr/bin/env python3
"""
Batch 20 — 8 entities: Blanche Azoulay, Khadija Abeba, Maddalena Buonsignori,
Qinisile Mabuza, Dorothy Ufot, Maria de Fátima Coronel, Yusuf Haji Nur,
Mohammad Tajul Islam
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

    # 1 — Blanche Azoulay (c.1880s–?)
    ("blanche-azoulay", {
        "summary": (
            "Blanche Azoulay (dates uncertain) was a pioneering Algerian Jewish lawyer who became "
            "the first woman admitted to the Bar of Algiers in 1908 — an achievement that placed "
            "her among the earliest women lawyers in the French colonial world and in the history "
            "of North African legal practice. Her admission came just eight years after France "
            "itself legally opened the legal profession to women (1900), and in a colonial context "
            "where the intersection of French republican law, colonial racial hierarchies, and the "
            "deep social conservatism of both European settler and Muslim Algerian communities made "
            "the achievement of professional distinction as a woman doubly exceptional.\n\n"
            "As a member of Algeria's Sephardic Jewish community — Algerian Jews had been granted "
            "French citizenship by the Crémieux Decree of 1870, which distinguished them legally "
            "from Muslim Algerians who remained subject to indigenous status (statut personnel) "
            "— she had access to the French educational system and to French bar examination "
            "procedures. Her admission to the Bar of Algiers in 1908 represented both a personal "
            "achievement and a marker of the particular position of Algerian Jews in the colonial "
            "legal order: formally citizens with French professional rights, but members of a "
            "community that would itself become a target of colonial antisemitism during the "
            "Vichy period.\n\n"
            "The history of women in law in the French colonial world is poorly documented, "
            "making Azoulay's position as a documented pioneer of exceptional historical value. "
            "She preceded the admission of most women to other North African and Middle Eastern "
            "bars by decades, and her career illustrates both the possibilities and the "
            "contradictions of colonial modernity — the extension of metropolitan rights "
            "frameworks to colonial subjects at the intersection of gender, religion, and race.\n\n"
            "Her achievement placed her in the global history of women who broke the bar's "
            "gender exclusion — a process that moved at different speeds across different "
            "legal systems between 1890 and 1950."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "First woman admitted to the Bar of Algiers (1908), making her one of the earliest women lawyers in the French colonial world and in North African legal history; her achievement reflects the particular legal position of Algerian Jews under the Crémieux Decree.",
            "significanceCategory": "continental"
        },
        "causes": [
            "France's legal opening of the legal profession to women (1900) created the formal possibility for women in French-governed Algeria to seek bar admission",
            "The Crémieux Decree (1870) granting French citizenship to Algerian Jews gave her access to French educational and professional frameworks not available to Muslim Algerians",
            "The wave of pioneering women lawyers in French-speaking jurisdictions in the early 20th century — including Jeanne Chauvin in France (1900) — created the precedents on which Azoulay built"
        ],
        "effects": [
            "Her 1908 admission to the Bar of Algiers established a precedent for women in North African and colonial French legal practice",
            "As the first documented woman lawyer in Algeria, she became part of the global history of women who broke legal profession gender barriers",
            "Her career illustrates the contradictions of colonial legal modernity: the extension of French republican professional rights to women in a colonial context of racial hierarchy",
            "The Algerian Jewish community's position — citizens with French professional rights, distinct from Muslim Algerians in indigenous status — is illustrated through her particular ability to access the bar"
        ],
        "relationships": [
            {"entity": "Bar of Algiers", "relationship": "FIRST_FEMALE_MEMBER_OF", "note": "Admitted to the Bar of Algiers in 1908 as its first woman member — a landmark in North African legal history"},
            {"entity": "Crémieux Decree (1870)", "relationship": "BENEFICIARY_OF", "note": "The Crémieux Decree's grant of French citizenship to Algerian Jews gave her access to the French educational and professional systems"},
            {"entity": "French colonial Algeria", "relationship": "PRACTICED_LAW_IN", "note": "Her legal career was conducted within the colonial legal system of French Algeria"},
            {"entity": "History of women in the legal profession", "relationship": "PIONEER_OF", "note": "One of the earliest women admitted to a bar in North Africa and the French colonial world"},
            {"entity": "Algerian Jewish community (Sephardic)", "relationship": "MEMBER_OF", "note": "Her ability to access the French bar was mediated through the particular French citizenship status of Algerian Jews"}
        ]
    }),

    # 2 — Khadija Abeba
    ("khadija-abeba", {
        "summary": (
            "Khadija Abeba is a Djiboutian jurist who serves as President of the Supreme Court "
            "of Djibouti — the republic of Djibouti's highest judicial authority — and who holds "
            "the distinction of being the country's highest-ranking female official, occupying "
            "the third position in the constitutional order of the Republic of Djibouti, a "
            "small nation in the Horn of Africa with a French civil law and Islamic law "
            "inheritance that gained independence from France in 1977. Her elevation to the "
            "presidency of the Supreme Court represents a landmark in a judiciary that, like "
            "most in East Africa and the Arab world, has historically been dominated by men.\n\n"
            "Djibouti's legal system reflects the country's unique position at the intersection "
            "of French legal tradition (inherited from the colonial period), Islamic law (the "
            "dominant religion of the Somali and Afar populations), and the political structures "
            "of an independent republic that has been governed by the Issa Somali-dominated "
            "People's Rally for Progress since independence. The Supreme Court of Djibouti "
            "serves as both the highest court of appeal and the constitutional arbiter — "
            "functions that in many civil law systems are separated between an ordinary supreme "
            "court and a constitutional court.\n\n"
            "As President of the Supreme Court, Abeba oversees the interpretation and application "
            "of Djiboutian law in its most consequential cases, including constitutional questions "
            "and significant civil and criminal appeals. Her position in the constitutional order "
            "also gives her a formal role in national leadership succession — in many civil "
            "law republics, the president of the supreme court holds a role in the line of "
            "presidential succession.\n\n"
            "Her leadership represents the gradual opening of Djibouti's highest institutions "
            "to women and the professionalization of judicial governance in one of Africa's "
            "strategically important small states — a republic whose geography at the mouth "
            "of the Red Sea gives it outsized geopolitical significance."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "President of the Supreme Court of Djibouti and the country's highest-ranking female official; holds the third position in Djibouti's constitutional order — a landmark for women's judicial leadership in the Horn of Africa.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Djibouti's French civil law inheritance created a professional judicial system with formal routes to the highest judicial office that could, in principle, be open to women",
            "The gradual advancement of women in Djiboutian professional and political life over the post-independence decades created the pathway for women to reach senior judicial positions",
            "Regional and international pressure for women's inclusion in African judicial systems — including from the African Union's gender parity commitments — contributed to the environment in which her appointment was possible"
        ],
        "effects": [
            "Her position as President of the Supreme Court makes her the highest-ranking female official in the Djiboutian constitutional order — a landmark for women's representation in East African legal institutions",
            "Her leadership of the Supreme Court shapes the interpretation and application of Djiboutian law across constitutional and appellate matters",
            "Her appointment signals the opening of Djibouti's highest judicial position to women — a precedent for the broader Horn of Africa region",
            "Her constitutional rank (third in the state order) gives her a formal role in national leadership succession and state ceremonial functions"
        ],
        "relationships": [
            {"entity": "Supreme Court of Djibouti", "relationship": "PRESIDES_OVER", "note": "President of the Supreme Court of Djibouti — the republic's highest judicial authority"},
            {"entity": "Republic of Djibouti", "relationship": "HIGHEST_RANKING_FEMALE_OFFICIAL_OF", "note": "Third in the constitutional order of the Republic of Djibouti as Supreme Court president — the country's highest-ranking female official"},
            {"entity": "French civil law tradition", "relationship": "OPERATES_WITHIN", "note": "Djibouti's legal system is based on French civil law inherited from the colonial period, within which she practices judicial leadership"},
            {"entity": "Horn of Africa judicial community", "relationship": "PART_OF", "note": "Her judicial leadership positions her as a significant figure in the development of the Horn of Africa's judicial institutions"},
            {"entity": "Women in African judicial leadership", "relationship": "PIONEER_OF", "note": "Her position as a female supreme court president in the Horn of Africa represents a landmark for women's judicial leadership in the region"}
        ]
    }),

    # 3 — Maddalena Buonsignori (fl. 14th century)
    ("maddalena-buonsignori", {
        "summary": (
            "Maddalena Buonsignori (fl. 14th century) was one of the exceptionally rare women "
            "to hold a teaching position in law at the medieval University of Bologna — "
            "the world's oldest continuously operating university and the institution that "
            "invented European legal education when Irnerius began teaching Justinian's Corpus "
            "Juris Civilis there around 1088. Bologna's law faculty had, by the 13th and 14th "
            "centuries, become the most prestigious legal school in the Latin world, drawing "
            "students from across Europe who would return home to build legal careers in royal "
            "courts, episcopal chanceries, and civic governments.\n\n"
            "The medieval University of Bologna produced a handful of women associated with "
            "legal teaching — an extraordinary fact in an intellectual world that almost "
            "universally excluded women from academic roles. The most famous was Novella "
            "d'Andrea (c.1312–1333), daughter of the great canonist Giovanni d'Andrea, who "
            "according to tradition lectured at Bologna (reportedly behind a screen so that her "
            "beauty would not distract the students — a detail that may be legendary). "
            "Maddalena Buonsignori belonged to this small group of women who crossed the "
            "threshold into the law faculty's intellectual world.\n\n"
            "The Buonsignori name was associated with the Sienese merchant banking family that "
            "had been one of the dominant financial houses of the 13th-century Mediterranean — "
            "the Gran Tavola dei Buonsignori, which collapsed spectacularly around 1307. A woman "
            "of this family holding a legal teaching position at Bologna in the 14th century "
            "would represent the intersection of mercantile wealth and legal learning that "
            "characterized the Italian urban professional world of the high medieval period.\n\n"
            "Her position in the legal history of women is as a member of an almost inconceivably "
            "small group — women who entered the most formally exclusionary professional space "
            "of medieval intellectual life and left a trace of their names in the historical record."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "A 14th-century woman who held a teaching position in law at the University of Bologna — the world's oldest law school — one of a tiny number of medieval women to enter the formally exclusionary space of academic legal education.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The University of Bologna's extraordinary prestige as the center of European legal learning created the exceptional institutional environment in which a small number of women could, through family connections or exceptional ability, gain access to academic roles",
            "The Italian urban commercial world of the high medieval period — in which wealthy mercantile families invested in learning as a form of social capital — created the social conditions in which educated women of elite families could occasionally cross into academic spaces",
            "The tradition of Bolognese women in legal learning — established by earlier figures like Bettisia Gozzadini and Novella d'Andrea — created precedents, however fragile, for women's participation in the law faculty"
        ],
        "effects": [
            "Her position as a woman teaching law at Bologna placed her in the tiny historical record of medieval women legal scholars — a group whose existence challenges the assumption of total female exclusion from medieval intellectual life",
            "The fact of her teaching contributed, however marginally, to the tradition that women could hold academic legal positions — a tradition that would eventually, after centuries, become the norm",
            "The survival of her name in historical sources preserved evidence of women's participation in medieval legal education that would otherwise be entirely invisible",
            "Her existence complicates the standard narrative of the medieval university as a space of absolute male exclusivity"
        ],
        "relationships": [
            {"entity": "University of Bologna (law faculty)", "relationship": "TAUGHT_AT", "note": "Held a teaching position in law at the University of Bologna — the medieval world's most prestigious law school"},
            {"entity": "Novella d'Andrea", "relationship": "CONTEMPORARY_WITH", "note": "Belongs to the small group of 14th-century Bolognese women associated with legal teaching, alongside Novella d'Andrea"},
            {"entity": "Buonsignori family (Siena)", "relationship": "POSSIBLY_AFFILIATED_WITH", "note": "The Buonsignori surname connects her to the prominent Sienese merchant banking family whose Gran Tavola collapsed around 1307"},
            {"entity": "Medieval canon and civil law tradition", "relationship": "TEACHER_OF", "note": "Taught within the Bolognese tradition of Roman civil law and/or canon law that formed the backbone of medieval legal education"},
            {"entity": "History of women in legal education", "relationship": "PIONEER_OF", "note": "One of a tiny group of medieval women who held legal teaching positions — her existence is a landmark in the history of women in the legal profession"}
        ]
    }),

    # 4 — Qinisile Mabuza (b. c.1955)
    ("qinisile-mabuza", {
        "summary": (
            "Qinisile Mabuza is a Liswati jurist who holds the distinction of being the first "
            "female attorney in Eswatini (then the Kingdom of Swaziland) — a distinction she "
            "achieved in 1978 — and subsequently the first female judge appointed in Eswatini, "
            "making her a foundational figure in the gender history of the legal profession in "
            "one of Africa's most traditionally governed societies. Eswatini (renamed from "
            "Swaziland in 2018) is an absolute monarchy whose political and legal culture "
            "combines Roman-Dutch common law and Swati customary law within a system that "
            "concentrates authority in the king — making the advancement of women into its "
            "formal legal institutions all the more remarkable.\n\n"
            "Her admission as attorney in 1978 came during the reign of King Sobhuza II, in a "
            "country that had gained independence from Britain in 1968 and was developing "
            "its legal profession from a very small base. As the first woman in the profession, "
            "she not only broke a gender barrier but helped build the country's legal "
            "institutional capacity during its critical post-independence decades. The bar "
            "was a small professional community where each practitioner's skills mattered "
            "significantly, and her subsequent elevation to the judiciary extended her "
            "contribution from legal practice to judicial governance.\n\n"
            "As the first female judge in Eswatini, she participated in the development of "
            "the country's jurisprudence at the intersection of Roman-Dutch law, Swati "
            "customary law, and constitutional principles — a complex interaction that "
            "raised fundamental questions about the rights of women under customary marriage "
            "and property arrangements that are a central challenge to gender equality across "
            "sub-Saharan Africa's dual legal systems.\n\n"
            "Her career arc — from first female attorney to first female judge — represents "
            "one of the longest-standing 'firsts' in African legal gender history, spanning "
            "the critical decades of Eswatini's post-independence legal development."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "First female attorney (1978) and first female judge in Eswatini; a foundational figure in the gender history of the legal profession in one of Africa's most traditionally governed monarchies.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Eswatini's post-independence legal development — building a professional bar from a small base after 1968 — created opportunities for exceptional individuals regardless of gender to enter a profession that needed practitioners",
            "The Roman-Dutch common law tradition that Eswatini inherited from British colonial governance provided a relatively open professional admission framework compared to more socially restrictive systems",
            "Her personal determination to enter a profession from which women had been absent — combined with the gradual expansion of women's access to higher education across post-colonial Africa"
        ],
        "effects": [
            "Her 1978 admission as Eswatini's first female attorney established the precedent for women's participation in the country's legal profession",
            "Her subsequent appointment as the first female judge extended the precedent from the bar to the judiciary — the more powerful and consequential arm of the legal system",
            "Her judicial career contributed to the development of Eswatini jurisprudence on the interaction between Roman-Dutch law and Swati customary law, including on questions of women's rights",
            "Her career became a reference point in the regional history of women's advancement in the legal professions of southern Africa"
        ],
        "relationships": [
            {"entity": "Eswatini legal profession (bar)", "relationship": "FIRST_FEMALE_MEMBER_OF", "note": "First woman admitted as an attorney in Eswatini (then Swaziland) in 1978"},
            {"entity": "Eswatini judiciary", "relationship": "FIRST_FEMALE_JUDGE_OF", "note": "First female judge appointed in Eswatini — extending the gender breakthrough from the bar to the judiciary"},
            {"entity": "Kingdom of Eswatini (Swaziland)", "relationship": "SERVED_LEGAL_INSTITUTIONS_OF", "note": "Her entire career served the legal institutions of Eswatini during the critical post-independence decades"},
            {"entity": "Roman-Dutch law and Swati customary law", "relationship": "APPLIED", "note": "Her judicial career involved applying the complex intersection of Roman-Dutch and Swati customary law that defines Eswatini's dual legal system"},
            {"entity": "Women in African legal professions", "relationship": "PIONEER_OF", "note": "Her 'firsts' in Eswatini make her a significant figure in the regional history of women's entry into African legal institutions"}
        ]
    }),

    # 5 — Dorothy Ufot (SAN)
    ("dorothy-ufot", {
        "summary": (
            "Dorothy Udeme Ufot, SAN, is a Nigerian commercial lawyer who holds the rank of "
            "Senior Advocate of Nigeria — the highest designation in the Nigerian legal profession, "
            "equivalent to the Queen's Counsel title in Commonwealth systems — and who carries "
            "the additional distinction of being the first woman from Akwa Ibom State in the "
            "south-south Niger Delta region of Nigeria to be elevated to this elite rank. "
            "Her specialty in commercial law — corporate transactions, commercial arbitration, "
            "banking law, and corporate restructuring — positions her in the most technically "
            "demanding and economically significant area of Nigerian legal practice.\n\n"
            "The Senior Advocate of Nigeria designation is conferred by the Legal Practitioners "
            "Privileges Committee, chaired by the Chief Justice of Nigeria, on the basis of "
            "outstanding advocacy and jurisprudential contribution. As of recent years, fewer "
            "than 700 Nigerian lawyers hold the SAN rank out of a bar of over 100,000 "
            "practitioners — making the designation a mark of significant professional distinction. "
            "The scarcity of women among SAN designees reflects both historical and ongoing "
            "barriers to women's advancement to the highest levels of the Nigerian legal profession.\n\n"
            "Ufot's commercial law practice places her at the intersection of Nigeria's "
            "corporate and financial sectors — areas of increasing importance as Nigeria "
            "develops its capital markets, banking system, and international commercial "
            "arbitration capacity. Commercial lawyers at the SAN level in Nigeria handle "
            "significant international transactions, represent multinational corporations, "
            "and participate in the international arbitration proceedings that resolve "
            "major commercial disputes involving Nigerian parties.\n\n"
            "As the first female SAN from Akwa Ibom State, she broke a regional gender "
            "barrier within the already exclusive SAN community — becoming a role model "
            "for women lawyers from the Niger Delta region and contributing to the "
            "geographic and gender diversification of Nigeria's legal elite."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Nigerian commercial lawyer elevated to Senior Advocate of Nigeria (SAN); first woman from Akwa Ibom State to achieve this elite designation, placing her at the intersection of commercial law and women's advancement in Nigeria's legal profession.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Nigeria's SAN designation system — which selectively elevates a small percentage of outstanding advocates — created the professional recognition framework through which exceptional commercial lawyers like Ufot can be distinguished",
            "The growing complexity of Nigeria's commercial and financial sectors created increasing demand for specialized commercial lawyers of the highest caliber",
            "Women's gradual advancement through Nigeria's legal profession — still heavily male-dominated at the SAN level — created the context in which being 'first' from Akwa Ibom remained a meaningful achievement"
        ],
        "effects": [
            "Her SAN designation established her as one of Nigeria's most accomplished commercial lawyers and opened senior briefs typically reserved for male silks",
            "As the first female SAN from Akwa Ibom State, she created a regional precedent for women's achievement at the pinnacle of the Nigerian legal profession",
            "Her commercial law practice contributed to the development of Nigerian jurisprudence in corporate, banking, and commercial arbitration law",
            "Her visibility as a female SAN commercial lawyer contributed to the gradual diversification of the SAN community and mentoring of younger women in commercial legal practice"
        ],
        "relationships": [
            {"entity": "Senior Advocate of Nigeria (SAN) community", "relationship": "MEMBER_OF", "note": "Elevated to SAN — the highest designation in the Nigerian legal profession, held by fewer than 700 of 100,000+ Nigerian lawyers"},
            {"entity": "Akwa Ibom State (Nigeria)", "relationship": "FIRST_FEMALE_SAN_FROM", "note": "The first woman from Akwa Ibom State in Nigeria's Niger Delta region to be elevated to Senior Advocate of Nigeria"},
            {"entity": "Nigerian commercial law and arbitration", "relationship": "SPECIALIZES_IN", "note": "Commercial law specialty — corporate transactions, banking law, and commercial arbitration — makes her a leading figure in Nigeria's most economically significant legal practice area"},
            {"entity": "Legal Practitioners Privileges Committee (Nigeria)", "relationship": "RECOGNIZED_BY", "note": "The SAN designation is conferred by the Legal Practitioners Privileges Committee, chaired by the Chief Justice of Nigeria"},
            {"entity": "Nigerian women in the legal profession", "relationship": "ROLE_MODEL_FOR", "note": "Her achievement as a female commercial SAN makes her a model for women advancing in Nigeria's male-dominated upper legal ranks"}
        ]
    }),

    # 6 — Maria de Fátima Coronel
    ("maria-de-fátima-coronel", {
        "summary": (
            "Maria de Fátima Coronel is a Cape Verdean lawyer and jurist who served as President "
            "of the Supreme Court of Justice of Cape Verde from November 2015 until her retirement "
            "in December 2020 — holding the position of the country's highest judicial officer "
            "during a period in which Cape Verde continued to consolidate its reputation as one "
            "of West Africa's most stable multiparty democracies with a functioning rule of law. "
            "Her leadership of the Supreme Court made her the highest-ranking female judicial "
            "officer in Cape Verdean history.\n\n"
            "Cape Verde's legal system is rooted in the Portuguese civil law tradition — a legacy "
            "of its colonial period as a Portuguese island territory — combined with the "
            "post-independence constitutional framework established after the 1975 declaration "
            "of independence from Portugal. The Supreme Court of Justice of Cape Verde serves as "
            "both the highest court of appeal in ordinary civil and criminal matters and, in "
            "certain configurations, as the Constitutional Court — making its president one of "
            "the most influential figures in Cape Verdean legal governance.\n\n"
            "Cape Verde's political and legal development has been widely noted as exceptional "
            "in the West African context: peaceful transitions of power between parties, "
            "independent judiciary, press freedom, and relatively low levels of corruption have "
            "made it one of Africa's highest-rated countries on governance and democracy indexes. "
            "The Supreme Court's role in this environment — providing constitutional oversight "
            "and final appellate jurisdiction — carries real institutional weight that is sometimes "
            "absent in less stable African judicial systems.\n\n"
            "Coronel's five-year tenure as Supreme Court president contributed to the "
            "institutionalization of judicial independence in Cape Verde and to the "
            "precedent of women's leadership at the apex of the Cape Verdean legal system."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "President of the Supreme Court of Justice of Cape Verde (2015–2020); highest-ranking female judicial officer in Cape Verdean history; her leadership came during Cape Verde's consolidation as West Africa's most stable democracy.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Cape Verde's post-independence constitutional development — building judicial institutions from the foundation of Portuguese civil law and the 1975 independence framework — created the Supreme Court presidency as a significant institutional position",
            "Cape Verde's exceptional political stability and democratic consolidation in the West African context gave the Supreme Court genuine institutional weight and made its presidency consequential",
            "Women's gradual advancement in Cape Verde's professional and legal institutions — reflecting the country's relatively progressive gender equality record — created the pathway for her appointment"
        ],
        "effects": [
            "Her five-year tenure (2015–2020) contributed to the stability and independence of Cape Verde's Supreme Court during an important period in the country's judicial development",
            "As the first woman to lead the Cape Verdean Supreme Court, she established a landmark for women's judicial leadership in one of West Africa's most respected legal systems",
            "Her leadership reinforced Cape Verde's reputation for institutional quality and judicial independence that distinguishes it in the West African governance landscape",
            "Her retirement in 2020 marked the end of a significant chapter in Cape Verdean judicial history"
        ],
        "relationships": [
            {"entity": "Supreme Court of Justice of Cape Verde", "relationship": "PRESIDED_OVER", "note": "President of the Supreme Court of Justice of Cape Verde from November 2015 to December 2020"},
            {"entity": "Republic of Cape Verde", "relationship": "HIGHEST_JUDICIAL_OFFICER_OF", "note": "As Supreme Court president, she was Cape Verde's highest-ranking judicial official during her 2015–2020 tenure"},
            {"entity": "Portuguese civil law tradition", "relationship": "OPERATES_WITHIN", "note": "Cape Verde's legal system is rooted in the Portuguese civil law tradition inherited from its colonial period"},
            {"entity": "West African democratic governance", "relationship": "CONTRIBUTED_TO", "note": "Her judicial leadership contributed to Cape Verde's exceptional reputation for judicial independence and democratic governance in West Africa"},
            {"entity": "Women in African judicial leadership", "relationship": "LANDMARK_FIGURE_IN", "note": "Her position as the first female Supreme Court president in Cape Verdean history makes her a significant figure in the history of women's judicial leadership in Africa"}
        ]
    }),

    # 7 — Yusuf Haji Nur
    ("yusuf-haji-nur", {
        "summary": (
            "Yusuf Haji Nur was a Somali politician, lawyer, and jurist whose career encompassed "
            "some of the most demanding institutional roles in the fragile governance environment "
            "of post-civil-war Somalia — including service as Chief Justice of Puntland, the "
            "semi-autonomous northeastern region of Somalia, and briefly as acting President of "
            "Puntland (2001). His career illustrated the fusion of legal and political roles "
            "that characterized institution-building in a context where the formal state had "
            "largely collapsed and new governance structures were being constructed from minimal "
            "foundations.\n\n"
            "Puntland — officially the Puntland State of Somalia — declared itself an autonomous "
            "administration in 1998, during the period of Somali state collapse following the "
            "fall of the Siad Barre regime in 1991. Unlike the Republic of Somaliland (the "
            "northwest, which declared independence), Puntland declared itself an autonomous "
            "region that would remain part of a future federal Somalia, while building its "
            "own governmental institutions in the interim. Establishing functional courts and "
            "a basic rule of law was central to Puntland's self-legitimation project.\n\n"
            "As Chief Justice of Puntland (2001, and again 2016–2019), Nur led the construction "
            "of a functioning judicial system in a context of extreme institutional fragility — "
            "lacking reliable state revenue, physical security, a trained legal corps, or "
            "established precedent. His service as acting President of Puntland in 2001 — "
            "the constitutional position that the Chief Justice would occupy in presidential "
            "succession — illustrated the overlapping roles that characterize governance in "
            "fragile state environments.\n\n"
            "His career represented the rare figure of the Somali lawyer-statesman who "
            "committed to rebuilding institutions in one of the world's most difficult "
            "legal and political environments."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Chief Justice of Puntland (2001 and 2016–2019) and acting President of Puntland (2001); a Somali lawyer-statesman who helped construct judicial institutions in post-collapse Puntland under conditions of extreme institutional fragility.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Somalia's state collapse following the fall of Siad Barre (1991) created the vacuum in which Puntland's autonomous administration emerged (1998), requiring the construction of new judicial institutions from minimal foundations",
            "Puntland's self-legitimation project — presenting itself as a stable governance experiment that could be a model for Somali federal reconstruction — made the establishment of functioning courts a political as well as legal necessity",
            "The small pool of trained lawyers in post-collapse Somalia meant that experienced legal professionals like Nur occupied multiple overlapping roles in the fragile governance structure"
        ],
        "effects": [
            "His service as Chief Justice contributed to the establishment of a functioning judicial system in Puntland during its critical early years — a necessary foundation for any governance order",
            "His acting presidential role demonstrated the constitutional succession mechanisms that Puntland was building and showed that formal institutional procedures could function even in fragile environments",
            "His two separate periods as Chief Justice (2001 and 2016–2019) spanned a significant portion of Puntland's institutional history, providing continuity in the judiciary",
            "His career contributed to the emerging model of Somali autonomous regional governance that influenced discussions of federal reconstruction in Somalia as a whole"
        ],
        "relationships": [
            {"entity": "Puntland State of Somalia", "relationship": "SERVED_AS_CHIEF_JUSTICE_AND_ACTING_PRESIDENT_OF", "note": "Chief Justice of Puntland (2001, 2016–2019) and acting President of Puntland (2001) — combining judicial leadership with constitutional succession"},
            {"entity": "Puntland Supreme Court", "relationship": "LED", "note": "Led the Puntland judiciary as Chief Justice — a role that involved constructing judicial institutions under conditions of extreme institutional fragility"},
            {"entity": "Post-collapse Somali governance", "relationship": "CONTRIBUTED_TO", "note": "His career was dedicated to building functional governance and judicial institutions in post-civil-war Somalia"},
            {"entity": "Somali federal reconstruction", "relationship": "PART_OF", "note": "Puntland's governance experiment, which he helped lead judicially, was a key component of the broader Somali federal reconstruction process"},
            {"entity": "Abdullahi Yusuf Ahmed (Puntland president)", "relationship": "SERVED_UNDER_AND_SUCCEEDED_BRIEFLY", "note": "The Puntland constitutional order placed the Chief Justice in presidential succession, leading to his brief acting presidency"}
        ]
    }),

    # 8 — Mohammad Tajul Islam
    ("mohammad-tajul-islam", {
        "summary": (
            "Mohammad Tajul Islam is a Bangladeshi lawyer and human rights advocate who served "
            "as the Chief Prosecutor of Bangladesh's International Crimes Tribunal (ICT) — the "
            "specialized judicial body established by the Government of Bangladesh in 2010 to try "
            "individuals accused of genocide, crimes against humanity, war crimes, and other "
            "atrocities committed during the Bangladesh Liberation War of 1971, one of the "
            "20th century's most devastating episodes of mass violence. In this role he bore "
            "primary responsibility for prosecuting the cases that sought to deliver justice "
            "for what Bangladeshis call the '1971 genocide' — the systematic killing, sexual "
            "violence, and destruction carried out by the Pakistani military and its local "
            "collaborators during the nine-month liberation war.\n\n"
            "The Bangladesh Liberation War (March–December 1971) resulted in the death of "
            "between 300,000 and 3 million people (estimates vary widely), the rape of an "
            "estimated 200,000–400,000 women, and the displacement of 10 million refugees "
            "into India — one of the most catastrophic episodes of violence in South Asian "
            "history. The primary perpetrators included units of the Pakistani military, "
            "but the ICT's prosecutions focused primarily on members of the Razakar, al-Badr, "
            "and al-Shams militias — Bangladeshi collaborators, many of them affiliated with "
            "the Jamaat-e-Islami party — who assisted Pakistani forces in identifying and "
            "killing members of the Hindu community, Bengali intellectuals, and independence supporters.\n\n"
            "As Chief Prosecutor, Islam managed the most politically and legally consequential "
            "prosecutions in Bangladeshi legal history — cases that resulted in the conviction "
            "and execution of several senior figures including former Jamaat-e-Islami leaders. "
            "The ICT's proceedings attracted significant international scrutiny, with some "
            "human rights organizations criticizing procedural aspects while Bangladeshi "
            "civil society largely supported the project of accountability.\n\n"
            "His role placed him at the center of one of the most complex challenges in "
            "transitional justice: prosecuting mass atrocities after a 40-year delay, "
            "against defendants who had subsequently held political power, in a politically "
            "charged domestic environment."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Chief Prosecutor of Bangladesh's International Crimes Tribunal (2010s); led the prosecutions of individuals accused of genocide and crimes against humanity during the 1971 Bangladesh Liberation War — the most consequential transitional justice proceedings in South Asian history.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The 1971 Bangladesh Liberation War's massive scale of atrocity — estimated 300,000–3 million killed, 200,000–400,000 women raped — created the historical demand for justice that the ICT was established to provide four decades later",
            "The political decision by the Sheikh Hasina government (Awami League) in 2010 to establish the ICT and pursue prosecutions of 1971 collaborators — many affiliated with the opposition Jamaat-e-Islami — created the institutional context for his role",
            "Bangladesh's failure to prosecute 1971 crimes in the immediate post-independence period — due to political instability, the 1975 coups, and the subsequent political rehabilitation of collaborators — made the 40-year delay that Islam's prosecutions ultimately sought to remedy"
        ],
        "effects": [
            "The ICT's prosecutions under his leadership resulted in the conviction and execution of several senior Jamaat-e-Islami figures — producing the first judicial accountability for 1971 atrocities in Bangladeshi history",
            "The ICT proceedings generated significant national and international debate about transitional justice standards, the procedural fairness of the tribunal, and the distinction between genuine accountability and political prosecution",
            "The convictions and executions sparked major domestic protests by Jamaat-e-Islami supporters and counter-protests by civil society groups demanding maximum sentences — the Shahbag protests of 2013",
            "His role contributed to Bangladesh's developing body of domestic international criminal law and to the broader South Asian discourse on accountability for mass atrocity"
        ],
        "relationships": [
            {"entity": "International Crimes Tribunal (Bangladesh)", "relationship": "CHIEF_PROSECUTOR_OF", "note": "Chief Prosecutor of the ICT — the specialized tribunal established in 2010 to try 1971 liberation war atrocity crimes"},
            {"entity": "Bangladesh Liberation War 1971", "relationship": "PROSECUTED_CRIMES_OF", "note": "Led prosecutions of the genocide, crimes against humanity, and war crimes committed during the 1971 liberation war"},
            {"entity": "Jamaat-e-Islami Bangladesh", "relationship": "PROSECUTED_LEADERS_OF", "note": "ICT prosecutions focused heavily on former Razakar/al-Badr militia members affiliated with Jamaat-e-Islami"},
            {"entity": "Sheikh Hasina / Awami League government", "relationship": "SERVED_UNDER", "note": "The ICT was established under Sheikh Hasina's Awami League government, which created the prosecutorial mandate he carried out"},
            {"entity": "Shahbag protests (2013)", "relationship": "INFLUENCED_BY_PROSECUTIONS_OF", "note": "The ICT verdicts he prosecuted sparked the 2013 Shahbag protests demanding maximum punishment for convicted war criminals"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 20)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
