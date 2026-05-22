#!/usr/bin/env python3
"""
Batch 42 — 8 entities (Class 381): Global South & International Universities
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()
FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/381-Class-381"
FILE_PREFIX = "381"


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

    ("national-autonomous-university-of-mexico", {
        "summary": (
            "The National Autonomous University of Mexico (UNAM — Universidad Nacional Autónoma de México, est. 1551 as the Royal and Pontifical University of Mexico, refounded 1910, Mexico City) is Latin America's largest and most prestigious university — with 360,000+ students, 40,000+ academic staff, and 11 Nobel Prize-affiliated alumni, and the institutional source of more Mexican presidents, cabinet ministers, and cultural figures than any other institution. UNAM's central campus in southern Mexico City — the Ciudad Universitaria — is a UNESCO World Heritage Site (2007), with murals by Diego Rivera, David Alfaro Siqueiros, and Juan O'Gorman covering the main library and stadium.\n\n"
            "UNAM was founded in 1551 as the Royal and Pontifical University of Mexico — the second university established in the Americas (after the University of San Marcos, Lima, 1551) — and refounded as the National University of Mexico in 1910 during the Centennial celebrations of Mexican Independence, with full autonomy granted in 1929 after a student strike that became a landmark in the history of academic freedom in Latin America. The university's autonomy — from government interference in academic appointments, curriculum, and student admissions — remains the most jealously defended principle in Mexican academic culture.\n\n"
            "UNAM's Ciudad Universitaria campus (built 1950–1954, designed by Mario Pani and Enrique del Moral with murals by Rivera, Siqueiros, and O'Gorman) is the world's largest concentration of Mexican muralism in an architectural context, integrating public art and academic space in a model that influenced Latin American campus design. UNAM produces 12% of all Mexican scientific research and 50% of all Mexican PhD graduates, making it the disproportionate engine of Mexican intellectual production."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Latin America's largest and most prestigious university (est. 1551 Royal and Pontifical University of Mexico, refounded 1910); 360,000+ students, 40,000+ staff; 11 Nobel Prize-affiliated alumni; source of Mexican presidents, cabinet ministers, cultural figures; Ciudad Universitaria UNESCO World Heritage Site (2007) — murals by Diego Rivera, Siqueiros, O'Gorman; autonomy granted 1929 after student strike — landmark in Latin American academic freedom; 12% of Mexican scientific research, 50% of all Mexican PhD graduates; second university in Americas (after Lima 1551).",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The 1910 Centennial of Mexican Independence — and the Porfirian government's desire to demonstrate Mexico's modernity and educational progress — drove the refounding of the National University as a modern research institution, with Justo Sierra's vision of a university combining liberal arts, professional education, and research",
            "The 1929 student strike — in which students demanded university autonomy from government interference in academic appointments and admissions — created the legal framework for UNAM's independence that has been the defining principle of Mexican academic culture, enabling the university to maintain academic freedom through the PRI's 71-year authoritarian rule",
            "The 1950–1954 construction of the Ciudad Universitaria — funded by the Mexican state under President Miguel Alemán — was the largest single architectural project in Mexican history, concentrating the university on a single purpose-built campus and demonstrating the state's commitment to using education as the primary vehicle of national development"
        ],
        "effects": [
            "UNAM's production of 12% of all Mexican scientific research — from an institution with less than 1% of the national research budget — makes it the most productive research university per funding unit in Latin America, and the disproportionate engine of Mexican intellectual production across all disciplines",
            "UNAM's political role — as the primary training ground for Mexican politicians, lawyers, and public intellectuals — made it the institutional source of the critique of the PRI's authoritarian rule, with the 1968 Tlatelolco massacre of UNAM students (at the Plaza de las Tres Culturas) being one of the defining political traumas of modern Mexico",
            "The Ciudad Universitaria murals — Diego Rivera's stadium mosaics, Siqueiros's Rectory building reliefs, and O'Gorman's Central Library mosaic (the world's largest mosaic, covering a 10-story building with pre-Columbian and colonial imagery) — integrated public art and academic architecture in a model that influenced campus design across Latin America",
            "UNAM's open-access model — charging no tuition (or minimal fees) to all Mexican students who pass its entrance exam — has made it the primary mechanism of social mobility in Mexico, producing the professional class from families who could not otherwise afford university education, at the cost of chronic underfunding and the inability to increase revenue through tuition"
        ],
        "relationships": [
            {"entity": "Ciudad Universitaria (UNESCO World Heritage Site 2007, Rivera/Siqueiros/O'Gorman murals)", "relationship": "OCCUPIES_THE", "note": "UNAM's Ciudad Universitaria — integrating muralism with academic architecture — is the world's largest concentration of Mexican muralism and a UNESCO World Heritage Site"},
            {"entity": "1929 student strike (autonomy, landmark in Latin American academic freedom)", "relationship": "AUTONOMY_ESTABLISHED_THROUGH_THE", "note": "The 1929 student strike — winning university autonomy — is the landmark event in Latin American academic freedom, enabling UNAM to maintain independence through 71 years of PRI authoritarian rule"},
            {"entity": "1968 Tlatelolco massacre (UNAM students, political trauma)", "relationship": "INSTITUTIONAL_CONTEXT_FOR_THE_STUDENT_VICTIMS_OF_THE", "note": "The Tlatelolco massacre of UNAM students was one of the defining political traumas of modern Mexico, marking the limits of the PRI's tolerance of academic freedom"},
            {"entity": "Diego Rivera / David Alfaro Siqueiros / Juan O'Gorman (muralists, Ciudad Universitaria)", "relationship": "PATRON_OF_THE_LARGEST_CONCENTRATION_OF_MEXICAN_MURALISM_BY", "note": "UNAM commissioned Rivera, Siqueiros, and O'Gorman to integrate muralism into its campus architecture — the world's largest concentration of Mexican muralism"},
            {"entity": "Justo Sierra (refounding visionary 1910, liberal education model)", "relationship": "INTELLECTUAL_VISION_OF_THE_MODERN_INSTITUTION_PROVIDED_BY", "note": "Sierra's vision of a university combining liberal arts, professional education, and research shaped UNAM's academic identity at its 1910 refounding"}
        ],
    }),

    ("lomonosov-moscow-state-university", {
        "summary": (
            "Lomonosov Moscow State University (MGU — Moskovskiy Gosudarstvennyy Universitet imeni M.V. Lomonosova, est. 1755, Moscow — founded by Empress Elizabeth of Russia at the initiative of Mikhail Lomonosov and Ivan Shuvalov) is Russia's oldest and most prestigious university — the alma mater of 11+ Nobel laureates and the primary institutional source of Russian and Soviet scientific, political, and cultural leadership. MGU's Stalinist neoclassical main building (built 1949–1953) — the 240-metre Shukhov tower-dwarfing skyscraper on Sparrow Hills — is the tallest university building in the world and one of the Seven Sisters of Stalinist architecture.\n\n"
            "MGU was founded in 1755 — the first Russian university outside the imperial capitals, and the most accessible to non-noble Russians — by Empress Elizabeth at the initiative of Mikhail Lomonosov (Russia's first great scientist, mathematician, and poet), who had petitioned for a university that would admit students from non-noble backgrounds. MGU's democratic founding spirit — educated serfs could theoretically attend — distinguished it from the St. Petersburg Academy of Sciences and the privileged court educational institutions.\n\n"
            "Under the Soviet period, MGU was transformed into the primary production machine for the USSR's scientific and technical elite — its physics faculty (which trained Kapitsa, Landau, Tamm, Sakharov, and Zeldovich) was the primary institutional source of Soviet nuclear, quantum, and condensed matter physics, and its mathematics faculty produced some of the 20th century's greatest mathematicians (Kolmogorov, Gelfand, Bogolyubov)."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Russia's oldest and most prestigious university (est. 1755, Moscow, founded by Empress Elizabeth at Lomonosov's initiative); 11+ Nobel laureates; Stalinist neoclassical main building (1949–1953, 240m, tallest university building in world, Seven Sisters); Mikhail Lomonosov founder — first Russian university admitting non-nobles; physics faculty trained Kapitsa, Landau, Tamm, Sakharov, Zeldovich — primary source Soviet nuclear/quantum physics; mathematics faculty: Kolmogorov, Gelfand; primary institutional source Russian/Soviet scientific and political leadership.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Mikhail Lomonosov's petition to Empress Elizabeth (1754) — arguing that Russia needed a university accessible to non-noble students, unlike the elite academies — drove MGU's founding with the democratic admission principle that distinguished it from Russian court educational institutions",
            "The Stalinist state's investment in MGU as the primary production machine for the Soviet scientific and technical elite — building the extraordinary main building (1949–1953) and concentrating the best physics and mathematics faculty — reflected Stalin's recognition that scientific education was the foundation of Soviet military and economic power",
            "The Soviet physics establishment's concentration at MGU — with Landau, Tamm, Kapitsa, Sakharov, and Zeldovich all associated with the university — was driven by the state's direction of the best scientific talent to Moscow, creating the intellectual density that produced the Soviet atomic bomb, hydrogen bomb, and the theoretical foundations of Soviet nuclear physics"
        ],
        "effects": [
            "MGU's physics faculty's training of Andrei Sakharov (the father of the Soviet hydrogen bomb, and later the USSR's most prominent human rights dissident), Igor Tamm, and Lev Landau — who together provided the theoretical foundation for Soviet nuclear physics — was one of the most consequential concentrations of scientific talent in the history of warfare",
            "Andrei Sakharov's transformation from MGU-trained nuclear physicist to human rights dissident — using his scientific prestige to challenge Soviet nuclear policy and authoritarian governance — is one of the most dramatic examples of how a university's training of exceptional individuals can produce unexpected political consequences",
            "MGU's Stalinist neoclassical main building — the 240-metre skyscraper on Sparrow Hills (Lenin Hills), dominating Moscow's skyline and visible from 30+ kilometres — is the most architecturally significant university building of the 20th century, combining Stalinist monumental ambition with neoclassical and Gothic Revival elements in a form that became the symbol of Soviet scientific ambition",
            "MGU's global standing — consistently ranked among the world's top 100 universities — has been maintained through the post-Soviet period despite Russia's economic difficulties, demonstrating the durability of academic institutions built on exceptional talent concentration even when their broader political-economic context has transformed"
        ],
        "relationships": [
            {"entity": "Mikhail Lomonosov (founder initiative, Russia's first great scientist)", "relationship": "FOUNDED_AT_THE_INITIATIVE_OF_AND_NAMED_AFTER", "note": "Lomonosov's petition to Empress Elizabeth — arguing for a university admitting non-nobles — drove MGU's founding with the democratic admission principle that distinguished it from Russian court institutions"},
            {"entity": "Andrei Sakharov (MGU physics, hydrogen bomb / human rights dissident)", "relationship": "TRAINING_GROUND_OF", "note": "Sakharov's transformation from MGU-trained nuclear physicist to human rights dissident is one of the most dramatic examples of a university's unexpected political consequences"},
            {"entity": "Lev Landau (theoretical physics, Landau Institute)", "relationship": "INSTITUTIONAL_HOME_OF_THE_THEORETICAL_PHYSICS_OF", "note": "Landau's MGU affiliation was part of the concentration of Soviet theoretical physics talent that produced the USSR's nuclear and condensed matter physics capabilities"},
            {"entity": "Stalinist main building (1949–1953, 240m, tallest university building, Seven Sisters)", "relationship": "SYMBOLIC_ARCHITECTURAL_CENTRE_IS_THE", "note": "MGU's Stalinist neoclassical skyscraper — the tallest university building in the world — is the most architecturally significant university building of the 20th century"},
            {"entity": "Empress Elizabeth of Russia (founder 1755, Lomonosov petition)", "relationship": "FOUNDED_BY_IMPERIAL_DECREE_OF", "note": "Elizabeth's 1755 founding decree — responding to Lomonosov's petition — established the first Russian university accessible to non-noble students"}
        ],
    }),

    ("university-of-cape-town", {
        "summary": (
            "The University of Cape Town (UCT, est. 1829, Cape Town, South Africa — founded as the South African College, granted university status 1918) is Africa's highest-ranked university — consistently ranked among the world's top 200 institutions and the first African university in global rankings — the alma mater of J.M. Coetzee (Nobel Prize in Literature 2003), Christiaan Barnard (first human heart transplant surgeon, trained at UCT's Groote Schuur Hospital), and dozens of African heads of state and ministers, and the primary site of the anti-apartheid student movement that helped bring down white minority rule.\n\n"
            "UCT was founded in 1829 as the South African College — a college for English-speaking settler boys in the Cape Colony — and transformed into a university in 1918. UCT was the first South African university to admit Black students (1920), creating decades of tension between the university's liberal academic traditions and the apartheid state's racial segregation laws (which formally ended only in 1948 with the election of the National Party, though UCT resisted the Extension of University Education Act for years).\n\n"
            "UCT's Groote Schuur Hospital became world-famous on 3 December 1967 when Christiaan Barnard performed the world's first human-to-human heart transplant — on Louis Washkansky — in a nine-hour operation that made headlines worldwide and transformed cardiac surgery from an experimental technique to a clinical reality. UCT's 2015 student protests — the 'Rhodes Must Fall' and 'Fees Must Fall' movements — became the models for student decolonisation movements worldwide."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Africa's highest-ranked university (est. 1829, Cape Town; university status 1918); first African university in global top 200 rankings; J.M. Coetzee (Nobel Literature 2003); Christiaan Barnard (world's first human heart transplant, Groote Schuur Hospital 3 December 1967); first South African university to admit Black students (1920); anti-apartheid student movement; 'Rhodes Must Fall' and 'Fees Must Fall' (2015) — global models for student decolonisation movements.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Cape Colony's British educational tradition — and the settler community's need for a higher education institution that did not require sending children to Britain — drove the founding of the South African College (1829) and its eventual transformation into a university (1918)",
            "UCT's liberal academic tradition — which led it to admit Black students in 1920 and to resist the apartheid state's segregation laws for years after the National Party's election (1948) — was rooted in the Cape Colony's relatively more liberal racial tradition and the influence of a succession of liberal vice-chancellors who prioritised academic freedom over political compliance",
            "Christiaan Barnard's career trajectory — trained at UCT's medical school and Groote Schuur Hospital before completing his surgical training in the United States — positioned him to attempt the world's first heart transplant with the institutional support of UCT and Groote Schuur, combining American surgical techniques with South African institutional backing"
        ],
        "effects": [
            "Christiaan Barnard's world's first human heart transplant (3 December 1967, Groote Schuur Hospital) — performed on Louis Washkansky, who survived 18 days — transformed cardiac surgery from an experimental technique to a clinical goal, inspiring 100+ heart transplant operations in the following year and establishing the global heart transplant programme that has since saved hundreds of thousands of lives",
            "UCT's 'Rhodes Must Fall' movement (2015) — which campaigned for the removal of the statue of Cecil Rhodes from UCT's campus and for the decolonisation of the university curriculum — sparked similar movements at Oxford (Rhodes Must Fall Oxford), Harvard, Yale, and across the Global North, becoming the template for the global wave of decolonisation activism that transformed universities' engagement with colonial history",
            "UCT's role as Africa's highest-ranked university — producing the continent's academic leadership in medicine, science, law, and social science — has made it the primary institutional source of Africa's professional and intellectual elite, with its graduates occupying senior positions in governments, international organisations, and academia across the continent",
            "UCT's anti-apartheid student movement — including the defiance of apartheid legislation, the refusal to comply with the Extension of University Education Act, and the provision of academic space for the articulation of anti-apartheid arguments — contributed to the ideological undermining of apartheid and the formation of the post-apartheid political leadership"
        ],
        "relationships": [
            {"entity": "Christiaan Barnard (world's first human heart transplant, Groote Schuur 1967)", "relationship": "TRAINING_GROUND_AND_INSTITUTIONAL_HOME_OF", "note": "Barnard's UCT training and Groote Schuur base enabled the world's first heart transplant — one of the most consequential medical events of the 20th century"},
            {"entity": "J.M. Coetzee (Nobel Prize in Literature 2003, UCT alumnus and professor)", "relationship": "ALMA_MATER_AND_ACADEMIC_HOME_OF", "note": "Coetzee — UCT alumnus and long-serving professor — is Africa's only Nobel Laureate in Literature born in the country of the university that trained him"},
            {"entity": "Rhodes Must Fall movement (2015, global decolonisation template)", "relationship": "ORIGIN_SITE_OF_THE", "note": "UCT's 2015 Rhodes Must Fall campaign — removing Cecil Rhodes' statue and demanding curriculum decolonisation — became the template for similar movements at Oxford, Harvard, and worldwide"},
            {"entity": "Groote Schuur Hospital (UCT teaching hospital, heart transplant site)", "relationship": "OPERATES_THE_TEACHING_HOSPITAL_WHERE_THE_WORLD'S_FIRST_HEART_TRANSPLANT_OCCURRED", "note": "Groote Schuur Hospital — UCT's teaching hospital — was the site of Barnard's 1967 heart transplant, making UCT the institutional origin of the global heart transplant programme"},
            {"entity": "Apartheid state (Extension of University Education Act, resistance)", "relationship": "PRIMARY_SITE_OF_INSTITUTIONAL_RESISTANCE_TO_THE_RACIAL_SEGREGATION_LAWS_OF_THE", "note": "UCT's resistance to apartheid segregation laws — admitting Black students and defying the Extension of University Education Act — made it the primary site of institutional anti-apartheid resistance in South African higher education"}
        ],
    }),

    ("university-of-nairobi", {
        "summary": (
            "The University of Nairobi (UoN, est. 1956 as the Royal Technical College of East Africa, full university status 1970, Nairobi, Kenya) is East Africa's oldest and most prestigious university — the primary training institution for Kenya's professional, academic, and political leadership since independence (1963), the alma mater of multiple Kenyan presidents and cabinet ministers, and the primary centre for East African research in medicine, agriculture, and social sciences. The University of Nairobi's School of Medicine — and its associated Kenyatta National Hospital — is the primary healthcare training and tertiary care facility for Kenya and the East African Community.\n\n"
            "UoN's predecessor, the Royal Technical College of East Africa (1956), was established to provide higher education for East Africa without requiring students to travel to Britain — a colonial educational investment in the final decade before independence. After independence, UoN rapidly expanded to absorb the educational aspirations of Kenya's new professional class, adding faculties of law, medicine, agriculture, engineering, and the social sciences, and establishing itself as the primary vehicle for the educated nationalism that defined Kenyan post-independence development.\n\n"
            "UoN's academic environment produced Ngũgĩ wa Thiong'o — the world's most prominent African novelist and one of the most frequently nominated candidates for the Nobel Prize in Literature — who taught at the university until his 1977 arrest and subsequent exile. UoN's English Department under James Ngugi/Ngũgĩ was the site of the foundational debates in African literary theory about the language of African literature."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "East Africa's oldest and most prestigious university (est. 1956 as Royal Technical College, full university 1970, Nairobi Kenya); primary training institution for Kenyan/East African professional, academic, and political leadership; alma mater of Kenyan presidents and cabinet ministers; School of Medicine / Kenyatta National Hospital — primary East African healthcare training and tertiary care; Ngũgĩ wa Thiong'o taught here (1977 arrest and exile); foundational debates in African literary theory on language of African literature.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Royal Technical College's establishment (1956) — as a colonial educational investment in the final decade before East African independence — reflected Britain's belated recognition that it needed to train an East African professional class that could administer the region after decolonisation",
            "Kenya's independence (1963) and the Kenyan state's educational expansion policy — which tripled university enrolment in the first decade of independence — drove UoN's rapid growth from a small technical college to a comprehensive research university, responding to the aspirations of the educated class that independence had created",
            "Ngũgĩ wa Thiong'o's appointment to the English Department — and his subsequent debate about whether African literature should be written in African languages (Gikuyu, Swahili) rather than in English — transformed UoN's English Department into the primary site of the foundational debates in African literary and postcolonial theory"
        ],
        "effects": [
            "UoN's School of Medicine and Kenyatta National Hospital — the primary teaching hospital and tertiary care facility for Kenya and the East African Community — have trained the doctors, nurses, and public health professionals who have managed Kenya's healthcare system through independence, AIDS epidemic, and COVID-19, making UoN's medical school the most important healthcare institution in East Africa",
            "Ngũgĩ wa Thiong'o's debates at UoN about the language of African literature — culminating in his decision to write exclusively in Gikuyu after 1977 and his foundational essay 'Decolonising the Mind' (1986) — transformed the global debate about postcolonial literature, inspiring African writers across the continent to engage seriously with the question of indigenous language and colonial language",
            "Ngũgĩ's 1977 arrest and detention (under the Public Security Act, after the Gikuyu-language play Ngaahika Ndeenda was performed) and subsequent exile — and UoN's capitulation to government pressure in not defending his academic freedom — demonstrated both the political importance of African literary culture and the limits of university autonomy in postcolonial states",
            "UoN's role as the alma mater of Kenya's political and professional leadership — from Daniel arap Moi's government through the Kibaki and Odinga eras — has made it the primary institutional source of the post-independence Kenyan state's bureaucratic and professional class, with the concentration of power among UoN graduates creating both a technocratic meritocracy and, critics argue, an educational oligarchy"
        ],
        "relationships": [
            {"entity": "Ngũgĩ wa Thiong'o (novelist, professor 1967–1977, 'Decolonising the Mind')", "relationship": "ACADEMIC_HOME_AND_SITE_OF_ARREST_OF", "note": "Ngũgĩ's debates at UoN about the language of African literature — and his 1977 arrest — made the university the primary site of foundational African literary theory"},
            {"entity": "Kenyatta National Hospital (UoN teaching hospital, East African tertiary care)", "relationship": "OPERATES_THE_PRIMARY_EAST_AFRICAN_HEALTHCARE_TRAINING_INSTITUTION", "note": "The KNH — UoN's teaching hospital — is the primary tertiary care and healthcare training facility for Kenya and the East African Community"},
            {"entity": "Royal Technical College of East Africa (1956, colonial predecessor)", "relationship": "SUCCESSOR_INSTITUTION_TO_THE", "note": "UoN grew from the 1956 Royal Technical College — a late colonial educational investment in East African professional training"},
            {"entity": "Kenya independence (1963, educational expansion driver)", "relationship": "RAPID_EXPANSION_DRIVEN_BY_THE_ASPIRATIONS_OF_THE_POST-INDEPENDENCE_PROFESSIONAL_CLASS_OF", "note": "Kenya's independence drove UoN's transformation from a small technical college to East Africa's premier research university"},
            {"entity": "East African Community (healthcare and research regional role)", "relationship": "PRIMARY_ACADEMIC_AND_MEDICAL_TRAINING_INSTITUTION_FOR_THE", "note": "UoN's regional role — training doctors, lawyers, and researchers for Kenya and East Africa — makes it the primary institutional anchor of the East African Community's professional infrastructure"}
        ],
    }),

    ("university-of-ibadan", {
        "summary": (
            "The University of Ibadan (UI, est. 1948 as University College Ibadan, full university status 1962, Ibadan, Nigeria) is West Africa's oldest and most historically significant university — the first university in Nigeria, founded as a colonial educational investment in the final decade before Nigerian independence, and the alma mater of Wole Soyinka (Nobel Prize in Literature 1986, the first African to win the prize), Chinua Achebe, J.P. Clark, Christopher Okigbo, and virtually the entire first generation of Nigerian and West African literature. The University of Ibadan was the crucible of the African literary renaissance that transformed world literature.\n\n"
            "University College Ibadan was established in 1948 as a college of the University of London — providing degree courses under London's external degree system — in a deliberate colonial policy of training Nigerians for the administrative and professional roles they would need after independence. Ibadan's early faculty included some of Britain's leading academics, and the combination of a rigorous Oxford/Cambridge-influenced curriculum with the proximity to Yoruba cultural traditions created the unique intellectual environment that produced the Ibadan literary school.\n\n"
            "The Ibadan literary school — the group of writers who studied or taught at the University of Ibadan in the 1950s–1960s, including Soyinka, Achebe, Clark, Okigbo, and later Ben Okri and Buchi Emecheta — produced the body of work that established Anglophone African literature as a major world literary tradition, challenging the representation of Africa in Western fiction and creating the postcolonial literary canon that has shaped global literature since the 1960s."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "West Africa's oldest and most historically significant university (est. 1948 as University College Ibadan, full university 1962, Nigeria); first university in Nigeria; alma mater of Wole Soyinka (Nobel Literature 1986, first African laureate), Chinua Achebe (Things Fall Apart), J.P. Clark, Christopher Okigbo; Ibadan literary school — crucible of Anglophone African literature and postcolonial literary canon; colonial University of London external degrees; established African literature as major world literary tradition.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Elliot Commission (1945) — which recommended the establishment of university colleges in British West African colonies — drove the founding of University College Ibadan as the first and highest-status institution, designed to produce the administrative and professional class that would govern Nigeria after independence",
            "The combination of a rigorous University of London curriculum with the proximity of Ibadan to Yoruba cultural traditions and oral literature — and the presence of faculty who encouraged African students to engage with their own cultural heritage in literary form — created the unique intellectual environment that produced the Ibadan literary school",
            "Chinua Achebe's Things Fall Apart (1958) — written while Achebe was working at Nigerian Broadcasting Corporation after his Ibadan education — was the founding text of the Anglophone African literary tradition, demonstrating that African experience could be the subject of world-class literary fiction and inspiring the generation of writers who followed"
        ],
        "effects": [
            "The Ibadan literary school's body of work — Achebe's Things Fall Apart (1958, 50+ million copies sold, the most widely read African novel), Soyinka's plays, Okigbo's poetry — established Anglophone African literature as a major world literary tradition, challenging the representation of Africa in Western colonial fiction (Conrad, Cary) and creating the postcolonial literary canon",
            "Wole Soyinka's Nobel Prize in Literature (1986) — the first African Nobel in Literature — validated the Ibadan literary school's achievement and confirmed that African literature had achieved world-class status, inspiring subsequent African Nobel laureates (Naguib Mahfouz 1988, Nadine Gordimer 1991, Coetzee 2003, Doris Lessing 2007)",
            "The University of Ibadan's model — a colonial institution that became the crucible of anti-colonial and postcolonial literature — demonstrated how educational institutions established for colonial purposes can be appropriated by colonised peoples to produce cultural products that challenge the colonial order, a pattern repeated in universities across the formerly colonised world",
            "Ibadan's role as the primary training ground for Nigerian academic and professional life — with its graduates occupying positions across government, medicine, law, and academia — made it the institutional source of Nigeria's post-independence professional class, with all the consequences (both positive and problematic) of concentrating educational capital in a single institution"
        ],
        "relationships": [
            {"entity": "Wole Soyinka (Nobel Prize in Literature 1986, first African laureate)", "relationship": "ALMA_MATER_OF", "note": "Soyinka's Ibadan education was the formation of the playwright and poet who became the first African Nobel Laureate in Literature"},
            {"entity": "Chinua Achebe (Things Fall Apart 1958, founding text of Anglophone African literature)", "relationship": "ALMA_MATER_OF_THE_AUTHOR_OF_THE_FOUNDING_TEXT_OF", "note": "Achebe's Ibadan education — and the intellectual environment of the Ibadan literary school — shaped the author of Things Fall Apart, the most widely read African novel"},
            {"entity": "Ibadan literary school (Soyinka, Achebe, Clark, Okigbo, Okri)", "relationship": "INSTITUTIONAL_CRUCIBLE_OF_THE", "note": "The Ibadan literary school — virtually the entire first generation of Nigerian literature — was formed by the unique intellectual environment of the University of Ibadan"},
            {"entity": "University of London (external degrees, colonial curriculum model)", "relationship": "FOUNDED_AS_A_COLLEGE_OF_THE", "note": "Ibadan's University of London college status — providing degrees under the external degree system — combined colonial rigour with proximity to Yoruba cultural traditions"},
            {"entity": "Nigerian independence (1963, alma mater of professional class)", "relationship": "PRIMARY_TRAINING_INSTITUTION_FOR_THE_PROFESSIONAL_CLASS_OF_POST-INDEPENDENCE", "note": "Ibadan trained the doctors, lawyers, academics, and civil servants who governed Nigeria after independence, making it the institutional source of Nigeria's post-colonial professional class"}
        ],
    }),

    ("seoul-national-university", {
        "summary": (
            "Seoul National University (SNU — Gukgnip Seoul Daehakgyo, est. 1946, Seoul, South Korea — founded by the United States Army Military Government as the national university of the newly liberated Korea) is South Korea's most prestigious research university — the apex of the intensely competitive Korean educational system, the primary producer of Korea's government, corporate, and academic elite, and an institution whose social role — as the gateway to Korea's highest professional positions — has made it simultaneously the engine of Korean development and the primary symbol of Korea's high-stakes educational culture. SNU alumni hold a disproportionate share of positions in Korean government, the chaebol, and academia.\n\n"
            "SNU was established in 1946 by the US Army Military Government in Korea as the Gukgnip Seoul Daehakgyo — merging ten existing colonial-era Japanese educational institutions to create a comprehensive national university — and became the primary vehicle for Korea's post-liberation educational reconstruction. Through the Korean War devastation (1950–1953) and the subsequent military dictatorships, SNU maintained its position as Korea's intellectual centre, training the technocratic elite who directed the Korean economic miracle.\n\n"
            "SNU's connection to the Korean economic miracle — Samsung, Hyundai, LG, and virtually all major chaebol have SNU graduates in senior positions, and the Ministry of Finance and Ministry of Science have historically been dominated by SNU alumni — makes it the primary educational institution of one of the world's most dramatic economic transformations: from one of the world's poorest countries (GDP per capita $67, 1953) to a high-income economy in a single generation."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "South Korea's most prestigious research university (est. 1946, Seoul, US Army Military Government); apex of Korean educational system; primary producer of Korean government, corporate, and academic elite; alumni dominate government ministries and chaebol (Samsung, Hyundai, LG); connected to Korean economic miracle (GDP per capita $67 in 1953 to high-income economy); established from 10 colonial-era Japanese institutions; survived Korean War (1950–1953); technocratic elite trained SNU — primary symbol of Korea's high-stakes educational culture.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The US Army Military Government's founding of SNU (1946) — merging ten Japanese colonial educational institutions into a single comprehensive national university — reflected the American educational model of a flagship state university as the primary vehicle for post-war reconstruction and democratic governance",
            "The Korean state's investment in education as the primary vehicle for national development — reflected in SNU's consistently expanding budget through the military dictatorships of Park Chung-hee and Chun Doo-hwan — created the pipeline of technically trained professionals who directed the export-led industrialisation of the Korean economic miracle",
            "The intense competition for SNU admission — driven by employers' informal preference for SNU graduates, which creates a structural incentive for families to invest extraordinary resources in preparation — has made SNU the apex of the Korean educational competition, concentrating the highest-achieving students from across Korea and reinforcing the institution's position"
        ],
        "effects": [
            "SNU's disproportionate production of Korea's government, corporate, and academic elite — with SNU graduates holding a majority of senior positions in the Ministry of Finance, Bank of Korea, and the chaebol's executive ranks — has been both the primary mechanism of Korea's technocratic development model and the source of persistent criticism about SNU's monopoly on Korean social mobility",
            "The Korean educational culture — characterised by the hagwon (private tutoring academy) industry, the emphasis on university entrance exam performance, and the enormous family investment in children's education — was in part produced by competition for SNU admission, making SNU both the reflection and the driver of Korea's educational intensity",
            "SNU's research output — particularly in semiconductors, biotechnology, and engineering — has been a primary contributor to Korea's technological capabilities, with SNU-Samsung, SNU-Hyundai, and SNU-government research partnerships producing the applied research that enabled Korean companies to compete globally in electronics, shipbuilding, and automotive sectors",
            "The 2014 Sewol ferry disaster's political aftermath — in which SNU professors and alumni were prominent both in the crisis management and the subsequent investigation and criticism — demonstrated how SNU's dominance of Korean public life means that every major Korean political event is, in some sense, an SNU event"
        ],
        "relationships": [
            {"entity": "Korean economic miracle (chaebol, Samsung/Hyundai/LG, technocratic elite)", "relationship": "PRIMARY_EDUCATIONAL_SOURCE_OF_THE_TECHNOCRATIC_ELITE_OF_THE", "note": "SNU's disproportionate production of chaebol executives and government ministers made it the primary educational institution of one of history's most dramatic economic transformations"},
            {"entity": "US Army Military Government in Korea (founder 1946)", "relationship": "ESTABLISHED_BY_THE", "note": "The US AMGIK's 1946 founding — merging 10 Japanese colonial institutions — established SNU as Korea's comprehensive national university on the American flagship state university model"},
            {"entity": "Korean War (1950–1953, survival and reconstruction)", "relationship": "SURVIVED_THE_DEVASTATION_OF_THE", "note": "SNU's survival of Korean War devastation and rapid reconstruction reflected the Korean state's commitment to education as the foundation of national reconstruction"},
            {"entity": "Hagwon / Korean educational culture (SNU admission competition driver)", "relationship": "APEX_INSTITUTION_WHOSE_COMPETITION_DRIVES_THE", "note": "SNU's position as the apex of Korean higher education — with employer preference for SNU graduates — is a primary driver of Korea's intense educational culture and hagwon industry"},
            {"entity": "Korean government ministries (Finance, Science — SNU alumni dominance)", "relationship": "PRIMARY_TRAINING_INSTITUTION_OF_THE_ALUMNI_DOMINATING_SOUTH_KOREAN", "note": "SNU alumni's dominance of the Ministry of Finance, Bank of Korea, and senior government positions reflects the university's role as the primary gateway to Korean public life"}
        ],
    }),

    ("cairo-university", {
        "summary": (
            "Cairo University (CU — Jāmiʻat Al-Qāhirah, est. 1908 as the Egyptian University, Giza/Cairo) is the Arab world's most prestigious and historically influential university — the primary institutional source of Egyptian and Arab nationalist, liberal, and Islamist intellectual movements of the 20th century, the alma mater of three Nobel laureates (Naguib Mahfouz in Literature 1988, Anwar Sadat and Yasser Arafat among its political alumni), and the institution where virtually the entire Egyptian political, cultural, and intellectual elite of the 20th century was educated. Cairo University was the primary forum for the debates that shaped modern Arab intellectual and political life.\n\n"
            "Cairo University was founded in 1908 — during the final years of the Khedivate of Egypt — by Egyptian nationalists including Princess Fatima Ismail (who donated her jewellery to fund it) and Ahmed Lutfi el-Sayed, as the first secular, Egyptian-controlled university, independent of both the British colonial administration and Al-Azhar's religious control. Its faculty included both Egyptian intellectuals and European scholars, creating the distinctive combination of Islamic and Western academic traditions that shaped 20th-century Egyptian thought.\n\n"
            "The Muslim Brotherhood's intellectual formation — including Hassan al-Banna, Sayyid Qutb, and the Islamist intellectual tradition — was substantially shaped by Cairo University's debates, as Islamism emerged partly as a response to the Westernisation and secularism promoted by Cairo University's liberal faculty. This means that Cairo University was simultaneously the primary vehicle for Arab liberal nationalism and the primary institutional context for the emergence of political Islam."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Arab world's most prestigious and historically influential university (est. 1908, Giza/Cairo); primary institutional source of Egyptian/Arab nationalist, liberal, and Islamist intellectual movements; 3 Nobel laureates (Naguib Mahfouz Literature 1988; Sadat and Arafat political alumni); founded by Princess Fatima Ismail (jewellery donation) and Ahmed Lutfi el-Sayed; first secular Egyptian-controlled university; Muslim Brotherhood intellectual formation (Banna, Qutb) emerged partly as response to Cairo University's liberal faculty; simultaneously vehicle for Arab liberal nationalism and context for political Islam emergence.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Egyptian nationalists' recognition that Egypt needed a secular, Egyptian-controlled university — independent of both British colonial administration and Al-Azhar's religious authority — drove the founding of the Egyptian University (1908), with Princess Fatima Ismail's jewellery donation providing the founding capital for an institution that the colonial administration would not fund",
            "The 1919 Egyptian Revolution and the subsequent constitutional monarchy — which created both the political framework for independent Egyptian institutions and the demand for the educated professionals who could staff them — drove Cairo University's rapid expansion and its central role in the formation of the Egyptian nationalist movement",
            "The tension between Cairo University's secular, Western-influenced liberal tradition and Al-Azhar's religious authority — which had been Egypt's primary educational institution since 970 CE — created the intellectual competition that produced both Cairo University's most important liberal graduates (Taha Hussein, Naguib Mahfouz) and the Islamist reactions (Sayyid Qutb, Hassan al-Banna) that shaped 20th-century Arab politics"
        ],
        "effects": [
            "Naguib Mahfouz's Nobel Prize in Literature (1988) — the first Arabic-language Nobel in Literature — validated Cairo University's role as the primary institutional context for the modern Arabic literary tradition, and Mahfouz's Cairo Trilogy (1956–1957, set in Cairo's old quarters) remains the foundational work of modern Arabic fiction",
            "Sayyid Qutb's radicalization — from Cairo University-educated literary critic and education official to the most influential theorist of Islamist revolution — is the most consequential intellectual trajectory in the history of political Islam, with his prison writings (Milestones / Ma'alim fi al-Tariq, 1964) becoming the foundational text of Al-Qaeda, Islamic State, and the global jihadist movement",
            "Cairo University's training of virtually the entire Egyptian professional class — doctors, lawyers, engineers, civil servants, military officers — through the mid-20th century made it the primary vehicle for Egypt's modernisation, and its graduates occupied all senior positions in Nasser's, Sadat's, and Mubarak's governments",
            "The 2011 Egyptian Revolution — which began with protests at Tahrir Square, adjacent to Cairo University — was in part a product of the university's tradition of political engagement and its training of the professional middle class whose expectations of the Mubarak government had not been met"
        ],
        "relationships": [
            {"entity": "Naguib Mahfouz (Nobel Literature 1988, first Arabic-language laureate)", "relationship": "ALMA_MATER_OF", "note": "Mahfouz — Cairo University philosophy graduate — won the first Arabic-language Nobel in Literature, validating the university's role in the modern Arabic literary tradition"},
            {"entity": "Sayyid Qutb (Cairo University educated, Islamist revolutionary theorist)", "relationship": "INTELLECTUAL_FORMATION_SITE_OF_THE_MOST_INFLUENTIAL_THEORIST_OF_THE", "note": "Qutb's Cairo University education and subsequent radicalization produced the foundational texts of the global jihadist movement (Milestones, 1964)"},
            {"entity": "Princess Fatima Ismail (jewellery donation, founding patron 1908)", "relationship": "FOUNDED_WITH_THE_PATRONAGE_OF", "note": "Fatima Ismail's jewellery donation provided the founding capital for the first secular Egyptian-controlled university, independent of colonial and religious authority"},
            {"entity": "1919 Egyptian Revolution (nationalist expansion driver)", "relationship": "INSTITUTIONAL_VEHICLE_FOR_THE_PROFESSIONAL_FORMATION_OF_THE_LEADERS_OF_THE", "note": "The 1919 Revolution — and the subsequent constitutional monarchy — drove Cairo University's rapid expansion as the primary source of Egyptian nationalist professionals"},
            {"entity": "2011 Egyptian Revolution (Tahrir Square, Cairo University adjacent)", "relationship": "INSTITUTIONAL_CONTEXT_FOR_THE_EDUCATED_PROFESSIONAL_CLASS_WHOSE_MOBILISATION_DROVE_THE", "note": "The 2011 Revolution — at Tahrir Square adjacent to Cairo University — was partly a product of the university's tradition of political engagement and its training of the disappointed professional middle class"}
        ],
    }),

    ("makerere-university", {
        "summary": (
            "Makerere University (est. 1922 as a technical school, full university status 1949, Kampala, Uganda — the oldest and most prestigious university in East and Central Africa) was, for much of the 20th century, the University of East Africa — the single university serving Uganda, Kenya, and Tanganyika (Tanzania) — and produced virtually the entire first generation of post-independence East African professional, political, and intellectual leadership. Makerere's alumni include Milton Obote (Uganda's first president), Julius Nyerere (Tanzania's founding president), and Nobel Peace Prize laureate Wangari Maathai.\n\n"
            "Makerere was established in 1922 as a small technical school teaching carpentry and crafts; it progressively expanded through colleges of education, agriculture, engineering, and medicine, becoming the only university college serving Uganda, Kenya, and Tanganyika. From 1949 to 1970, Makerere operated as a college of the University of London (later the University of East Africa), providing degrees under the London external degree system and attracting distinguished British faculty alongside East African students.\n\n"
            "Makerere's 'golden age' (1960s–1970s) — when it was one of Africa's finest universities, attracting distinguished scholars and hosting the emerging East African literary tradition — was followed by catastrophic decline under Idi Amin's dictatorship (1971–1979), which destroyed the university's international faculty, academic freedom, and physical infrastructure. Makerere's partial recovery since the 1980s represents one of the most dramatic examples of institutional resilience in African academic history."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Oldest and most prestigious university in East and Central Africa (est. 1922, Kampala Uganda; full university 1949); sole university serving Uganda, Kenya, and Tanganyika 1949–1970; produced first generation of post-independence East African leadership; Milton Obote (Uganda's first president), Julius Nyerere (Tanzania's founding president), Wangari Maathai (Nobel Peace Prize 2004); 'golden age' 1960s–1970s; catastrophic decline under Idi Amin (1971–1979); institutional resilience — partial recovery demonstrates African academic persistence.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The British colonial administration's recognition (1920s) that East Africa needed a single institution capable of training the professional class for three territories — Uganda, Kenya, and Tanganyika — drove the founding and expansion of Makerere from a technical school into a comprehensive university college, avoiding the duplication costs of three separate institutions",
            "The University of London's external degree system — which allowed Makerere to offer London degrees without being a fully independent university — provided the academic credibility that attracted distinguished British scholars and enabled Makerere's graduates to compete in British and international academic and professional environments",
            "Idi Amin's coup (1971) and the expulsion of the Ugandan Asian community (1972) — which destroyed the commercial and professional class that had supported Makerere's development — was followed by systematic harassment of foreign faculty, academic repression, and physical destruction of university infrastructure that ended Makerere's golden age and produced a generation-long institutional decline"
        ],
        "effects": [
            "Makerere's production of virtually the entire first generation of East African post-independence leadership — including Milton Obote (Uganda), Julius Nyerere (Tanzania), and the professional classes who staffed Kenya, Uganda, and Tanzania's governments — made it the primary institutional source of the East African political order, and the university whose quality most directly affected the governance capacity of three countries",
            "Wangari Maathai's Makerere education — one of the first women in the university's history — was the formation of the environmental activist and Nobel Peace Prize laureate (2004) whose Green Belt Movement planted 51+ million trees across Kenya, making Makerere the educational origin of one of Africa's most consequential environmental movements",
            "The Idi Amin period's destruction of Makerere — including the departure of most international faculty, the harassment of Ugandan academics, and the physical degradation of the university — is the most dramatic example of how an authoritarian government can rapidly destroy a world-class academic institution, with consequences for East African intellectual and professional capacity that lasted for decades",
            "Makerere's partial recovery since the 1980s — and its return to some international standing, particularly in public health research and HIV/AIDS studies — represents one of Africa's most important stories of institutional resilience, demonstrating both how difficult it is to rebuild destroyed academic institutions and how much persistence can achieve"
        ],
        "relationships": [
            {"entity": "Julius Nyerere (Tanzania's founding president, Makerere alumnus)", "relationship": "ALMA_MATER_OF_THE_FOUNDING_PRESIDENT_OF_TANZANIA", "note": "Nyerere's Makerere education — and Makerere's role as the sole university for all of East Africa — made it the primary institutional source of post-independence East African political leadership"},
            {"entity": "Wangari Maathai (Nobel Peace Prize 2004, Green Belt Movement founder)", "relationship": "ALMA_MATER_OF", "note": "Maathai's Makerere education — as one of the university's first women graduates — was the formation of the environmental activist who won Africa's first female Nobel Peace Prize"},
            {"entity": "Idi Amin (1971–1979 dictatorship, destruction of Makerere)", "relationship": "INSTITUTION_CATASTROPHICALLY_DAMAGED_BY_THE_DICTATORSHIP_OF", "note": "Amin's destruction of Makerere's faculty, academic freedom, and infrastructure is the most dramatic example of how an authoritarian government can rapidly destroy a world-class university"},
            {"entity": "University of London external degree system (1949–1970 academic model)", "relationship": "ACADEMIC_CREDIBILITY_PROVIDED_BY_OPERATING_AS_A_COLLEGE_OF_THE", "note": "The London external degree model gave Makerere the credibility to attract distinguished scholars and graduates who competed internationally"},
            {"entity": "HIV/AIDS research programme (post-1980s recovery, public health)", "relationship": "SITE_OF_INTERNATIONALLY_SIGNIFICANT_POST-RECOVERY_RESEARCH_ON", "note": "Makerere's HIV/AIDS research programme — developed after Amin's destruction — is one of the most important examples of institutional recovery and the contribution it enables"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 42 — {len(ENTITIES)} entities (Class 381: Global South & International Universities)")
    for slug, data in ENTITIES:
        print(f"\n\u2192 {slug}")
        enrich_entity(slug, data)
    print("\n\u2713 Done")
