#!/usr/bin/env python3
"""
Batch 50 — 8 entities (Class 354): Famous Hospitals
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()
FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/354-Class-354"
FILE_PREFIX = "354"


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

    ("vienna-general-hospital", {
        "summary": (
            "The Vienna General Hospital (Allgemeines Krankenhaus der Stadt Wien — AKH Wien — est. 1784, Vienna, Austria, by Emperor Joseph II as part of his Josephine reforms of Austrian healthcare) is one of the most historically important hospitals in the world — as the primary site of the Vienna Medical School (Wiener Medizinische Schule) in the 19th century, it was the institution where Ignaz Semmelweis discovered handwashing as the preventive for childbed fever (1847), Carl von Rokitansky pioneered systematic pathological anatomy, and Joseph Škoda developed modern clinical medicine — making Vienna General Hospital the single institution most responsible for establishing medicine as a scientific discipline.\n\n"
            "Emperor Joseph II's 1784 establishment of the Vienna General Hospital — part of his enlightened absolutist programme of institutional reform that also secularised the Austrian state and reformed the legal system — brought together a maternity ward, an insane asylum, an orphanage, and a general hospital in a single large complex, creating the institutional density that enabled systematic medical research through large patient numbers.\n\n"
            "The hospital's most historically significant contribution to medicine was Ignaz Semmelweis's 1847 discovery — in the hospital's First Obstetric Clinic — that childbed fever (puerperal sepsis) was caused by doctors carrying 'cadaverous particles' from the pathology laboratory to the delivery room on unwashed hands, and that handwashing with chlorinated lime solution reduced maternal mortality from 10–35% to under 2%. Semmelweis's discovery — rejected by the medical establishment for 20 years and vindicated only by Pasteur's germ theory — is the foundation of modern hospital hygiene."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Most historically important site for the development of medicine as science (est. 1784 Vienna, Emperor Joseph II Josephine reforms); Ignaz Semmelweis (childbed fever prevention by handwashing 1847, germ theory precursor, rejected then vindicated by Pasteur); Carl von Rokitansky (systematic pathological anatomy); Joseph Škoda (modern clinical medicine); Vienna Medical School (Wiener Medizinische Schule) 19th-century preeminence; foundation of modern hospital hygiene; 10–35% to <2% maternal mortality reduction from handwashing.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Emperor Joseph II's Josephine reforms (1781–1789) — his enlightened absolutist programme of institutional reform that secularised the Austrian state, reformed the legal system, and restructured healthcare — provided both the financial resources and the political will to create a large centralised hospital that could concentrate medical expertise and patient volumes for systematic research",
            "The Enlightenment's empirical scientific programme — applied to medicine through the Vienna Medical School's emphasis on systematic observation, pathological anatomy, and clinical examination — created the intellectual environment that enabled Semmelweis, Rokitansky, and Škoda to develop the empirical methods that made medicine a science rather than a tradition",
            "The hospital's institutional density — combining a maternity ward, general hospital, and pathology laboratory in a single complex, with Rokitansky performing 30,000+ autopsies — created the systematic data about disease that enabled the Vienna Medical School's research breakthrough"
        ],
        "effects": [
            "Semmelweis's handwashing discovery (1847) — though rejected for 20 years and vindicated only after his death and Pasteur's germ theory confirmation — established the principle of antiseptic technique that is the foundation of all modern surgical and hospital hygiene practice, ultimately saving hundreds of millions of lives through the prevention of nosocomial infections",
            "The Vienna Medical School's 19th-century preeminence — attracting medical students from across Europe and America who then carried Vienna's empirical methods back to their home institutions — made Vienna General Hospital the primary vehicle for the diffusion of scientific medicine worldwide, with American, British, and German medicine all deeply influenced by the Viennese tradition",
            "Rokitansky's systematic pathological anatomy — performed in the hospital's pathology laboratory on 30,000+ cadavers — created the empirical foundation for understanding disease as a physical process in the body's tissues, replacing the humoral theory that had dominated medicine for two millennia with the cellular pathology that is the basis of all modern medical diagnosis",
            "The Vienna Medical School's influence on American medicine — through the many American physicians who studied in Vienna in the late 19th and early 20th centuries and returned to found American medical schools and hospitals — created the direct lineage between Viennese scientific medicine and the American academic medicine that became the global standard in the 20th century"
        ],
        "relationships": [
            {"entity": "Ignaz Semmelweis (handwashing discovery 1847, childbed fever prevention, germ theory precursor)", "relationship": "SITE_OF_THE_WORLD-CHANGING_MEDICAL_DISCOVERY_OF", "note": "Semmelweis's 1847 discovery — in the hospital's First Obstetric Clinic — reduced maternal mortality from 35% to under 2% and is the foundation of modern hospital hygiene"},
            {"entity": "Vienna Medical School (Wiener Medizinische Schule, 19th-century global medical education centre)", "relationship": "INSTITUTIONAL_SITE_OF_THE_19TH-CENTURY_PREEMINENCE_OF_THE", "note": "Vienna General Hospital's patient volumes and pathology laboratory made it the primary site for the Vienna Medical School's research that established medicine as a science"},
            {"entity": "Carl von Rokitansky (30,000+ autopsies, systematic pathological anatomy, disease as physical process)", "relationship": "INSTITUTIONAL_SITE_OF_THE_30,000+ AUTOPSY_RESEARCH_OF", "note": "Rokitansky's pathological anatomy research — performed in the hospital's laboratory — replaced humoral theory with cellular pathology as the basis of medical diagnosis"},
            {"entity": "Emperor Joseph II (Josephine reforms 1781–1789, enlightened absolutism, hospital founding)", "relationship": "FOUNDED_BY_THE_ENLIGHTENED_ABSOLUTIST_HEALTHCARE_REFORMS_OF", "note": "Joseph II's Josephine reforms — creating the institutional density of the Vienna General Hospital complex — provided the conditions for the 19th-century medical research revolution"},
            {"entity": "Antiseptic technique and hospital hygiene (foundation of modern surgical practice, Semmelweis principle)", "relationship": "BIRTHPLACE_OF_THE_FOUNDATIONAL_DISCOVERY_UNDERLYING", "note": "Semmelweis's handwashing discovery at Vienna General Hospital is the foundation of all modern antiseptic surgical and hospital hygiene practice"}
        ],
    }),

    ("al-shifa-hospital", {
        "summary": (
            "Al-Shifa Hospital (Arabic: مستشفى الشفاء — 'The Hospital of Healing' — est. 1946, Gaza City, Gaza Strip) is the largest hospital in the Gaza Strip and the primary medical facility serving approximately 2 million Palestinians — providing emergency, surgical, paediatric, and specialist services to a population experiencing one of the world's most severe and prolonged humanitarian crises. Al-Shifa has been repeatedly at the centre of international attention for its role as a functioning hospital during Gaza's successive military operations (2008–2009, 2012, 2014, 2021, and the 2023–present conflict), becoming a symbol of both Palestinian civilian healthcare and the humanitarian impact of urban warfare on medical facilities.\n\n"
            "Al-Shifa's founding in 1946 — during the final years of the British Mandate for Palestine — predates the creation of Israel and the Palestinian refugee crisis of 1948 (the Nakba), making it one of the few Palestinian institutions with continuous existence across the Nakba, the Egyptian administration of Gaza (1948–1967), the Israeli occupation (1967–2005), and the Hamas administration (2007–present). The hospital's continuous operation through successive conflicts has made it the most resilient Palestinian civilian institution.\n\n"
            "The hospital's role in successive conflicts — operating under bombardment, with fuel shortages, staff casualties, and patient populations including both civilians and combatants — has made Al-Shifa a focal point for international humanitarian law debates about the protection of medical facilities in conflict zones, with the hospital's status under international law contested in the 2023–2024 conflict."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Largest hospital in Gaza Strip (est. 1946, Gaza City, British Mandate period); primary medical facility for 2M Palestinians; operational through 1948 Nakba, Egyptian administration (1948–1967), Israeli occupation (1967–2005), Hamas administration (2007–present), successive military operations (2008–9, 2012, 2014, 2021, 2023–present); international humanitarian law focal point — medical facility protection in urban warfare; Palestinian civilian healthcare symbol; most resilient Palestinian civilian institution.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The British Mandate for Palestine's 1946 establishment of a modern hospital in Gaza City — part of the Mandate's public health infrastructure — created the institutional foundation that persisted through the Nakba, the Egyptian occupation, the Israeli occupation, and the Hamas administration, surviving as the primary healthcare institution of the Palestinian population in Gaza",
            "Gaza's chronic poverty and blockade — maintained by Israel since 2007 and Egypt intermittently — has created a healthcare system entirely dependent on humanitarian aid and the functioning of Al-Shifa Hospital, as the population's poverty and the restrictions on equipment and medicine make private healthcare inaccessible to most Gazans",
            "The successive military operations in Gaza (2008–2024) — in an urban environment of extreme population density — have repeatedly placed Al-Shifa at the centre of conflict, both because of its location in Gaza City and because of the humanitarian law significance of military operations near a functioning hospital"
        ],
        "effects": [
            "Al-Shifa's continuous operation through successive conflicts — treating casualties from both military operations and the underlying health crisis of the blockaded population — has maintained the primary healthcare infrastructure for Gaza's 2 million residents through conditions that would have caused most hospital systems to collapse",
            "The hospital's role in international humanitarian law debates — particularly regarding the application of Article 19 of the Geneva Conventions to attacks on medical facilities — has made Al-Shifa the most prominent contemporary test case for the international law protecting hospitals in conflict zones, with legal experts and international courts citing the Gaza conflicts as precedents",
            "Al-Shifa's symbolic significance — as the most visible Palestinian civilian institution and the location of some of the most internationally covered humanitarian crises — has made it a focal point for international advocacy for Palestinian rights and international humanitarian law compliance, with the hospital's fate closely tracked by international media and humanitarian organisations",
            "The health crisis produced by Al-Shifa's repeated damage and fuel shortages — with newborns dying in incubators during power outages and patients dying from lack of medicines — has documented the humanitarian impact of the Gaza blockade and military operations in terms that have driven international political pressure on all parties to the conflict"
        ],
        "relationships": [
            {"entity": "Gaza Strip Palestinian population (2 million people, primary healthcare service)", "relationship": "PRIMARY_MEDICAL_FACILITY_SERVING_THE", "note": "Al-Shifa is the primary — and often only accessible — healthcare institution for Gaza's 2 million Palestinians"},
            {"entity": "Geneva Conventions Article 19 (medical facility protection in conflict zones, international humanitarian law)", "relationship": "MOST_PROMINENT_CONTEMPORARY_TEST_CASE_FOR_THE_APPLICATION_OF", "note": "Al-Shifa's repeated targeting or proximity to military operations has made it the primary contemporary test case for international humanitarian law's protection of medical facilities"},
            {"entity": "British Mandate for Palestine (est. 1946 founding authority, public health infrastructure)", "relationship": "FOUNDED_BY_THE_PUBLIC_HEALTH_PROGRAMME_OF_THE", "note": "The British Mandate's 1946 hospital founding created the institutional foundation that has survived through all subsequent political changes"},
            {"entity": "Israeli blockade of Gaza (2007–present, medicine/equipment shortages, humanitarian crisis)", "relationship": "HEALTHCARE_CAPACITY_SEVERELY_CONSTRAINED_BY_THE", "note": "The Gaza blockade's restrictions on medicine, equipment, and fuel have made Al-Shifa's continuous operation a sustained humanitarian achievement under extreme constraint"},
            {"entity": "International humanitarian law protection of medical facilities (Article 19, urban warfare precedents)", "relationship": "CENTRAL_INSTITUTIONAL_SUBJECT_OF_CONTEMPORARY_DEBATES_ABOUT", "note": "Al-Shifa's experience during Gaza's conflicts is the primary contemporary reference case for international debates about protecting hospitals in urban warfare"}
        ],
    }),

    ("all-india-institute-of-medical-sciences-new-delhi", {
        "summary": (
            "All India Institute of Medical Sciences New Delhi (AIIMS New Delhi — est. 1956, New Delhi, by Act of Parliament, with founding support from the Government of New Zealand and the Rockefeller Foundation) is India's premier medical institution — functioning simultaneously as a teaching hospital, a postgraduate medical research university, and the standard-setting institution for medical education and clinical practice across India. AIIMS New Delhi's MBBS admissions process — accepting approximately 100 students annually from 1 million+ applicants — makes it the most competitive undergraduate programme in the world, with an acceptance rate below 0.01%.\n\n"
            "AIIMS New Delhi was founded on the recommendation of the Health Survey and Development Committee (Bhore Committee, 1946) — which recognised that India's independence required a world-class medical institution to train medical leaders, conduct research into the diseases prevalent in the Indian subcontinent, and set standards for all Indian medical education. The founding model — combining undergraduate medical education, postgraduate specialist training, and hospital-based research in a single autonomous institution — has been replicated through the expansion to 25 AIIMS across India.\n\n"
            "AIIMS New Delhi's clinical excellence — with 10,000+ patients per day in its outpatient department, the most complex surgical cases referred from across India, and specialist departments that are frequently the only accessible option for life-threatening conditions in a country of 1.4 billion people — makes it both the most important medical institution in India and a symbol of the gap between the quality of the best Indian medical care and the healthcare accessible to the majority of India's population."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "India's premier medical institution (est. 1956 New Delhi, Act of Parliament, NZ/Rockefeller Foundation support); most competitive undergraduate programme in world (<0.01% acceptance rate, 1M+ applicants for 100 MBBS seats); Bhore Committee (1946) founding recommendation; 10,000+ patients/day outpatient; teaching hospital, postgraduate research university, medical education standard-setter; 25 AIIMS replication across India; symbol of India's best medical care; most complex surgical cases from across India; 1.4 billion people's healthcare leadership.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Bhore Committee's 1946 report — which recognised that India's independence required world-class medical leadership and that no existing institution provided the combination of undergraduate education, specialist training, and research at the standard required — provided the policy foundation for AIIMS New Delhi's establishment",
            "International support for India's post-independence development — with the Government of New Zealand funding the construction and the Rockefeller Foundation supporting the initial faculty and research programmes — provided both the financial resources and the technical assistance that enabled AIIMS to be established at international quality standards from its founding",
            "Independent India's determination to develop world-class public institutions — in medicine, science (IITs), and management (IIMs) — as symbols of national capability and vehicles for developing the professional leadership that a democratic nation of 400 million required, drove the investment in AIIMS as the flagship medical institution"
        ],
        "effects": [
            "AIIMS New Delhi's graduates — who occupy leadership positions in Indian medicine, medical research, and global health organisations — have been the primary vehicle for diffusing clinical excellence and research capacity throughout the Indian healthcare system, with AIIMS alumni serving as department heads, medical school deans, and policy leaders across India",
            "The AIIMS model's replication — with 25 AIIMS now operating across India — has begun to extend world-class medical education beyond New Delhi, though the new institutions have not yet achieved the research depth and clinical quality of the original, demonstrating both the success of the model and the difficulty of replicating institutional excellence",
            "AIIMS New Delhi's treatment of the most complex medical cases in India — providing specialist care that would otherwise be inaccessible to patients from across a country of 1.4 billion — has saved hundreds of thousands of lives by providing surgical and medical expertise unavailable elsewhere in India, making it the last resort for patients with the most serious conditions",
            "AIIMS New Delhi's research output — including significant contributions to Indian epidemiology, tropical medicine, and clinical trials — has shaped Indian health policy and contributed to the global understanding of diseases particularly prevalent in South Asia, making it the most important institution for research into the health conditions affecting the world's most populous country"
        ],
        "relationships": [
            {"entity": "Bhore Committee Health Survey and Development Committee (1946 recommendation, founding policy basis)", "relationship": "FOUNDED_ON_THE_RECOMMENDATION_OF_THE", "note": "The Bhore Committee's recognition that India needed a world-class medical institution provided the policy basis for AIIMS's establishment"},
            {"entity": "Government of New Zealand (construction funding, international support for India's development)", "relationship": "CONSTRUCTION_FUNDED_BY_THE", "note": "New Zealand's funding of AIIMS's construction reflected the international support for India's post-independence development of world-class public institutions"},
            {"entity": "Rockefeller Foundation (initial faculty and research programme support)", "relationship": "INITIAL_FACULTY_AND_RESEARCH_SUPPORTED_BY_THE", "note": "The Rockefeller Foundation's support enabled AIIMS to establish at international quality standards from its founding"},
            {"entity": "25 AIIMS national network (model replication, AIIMS expansion programme across India)", "relationship": "ORIGINAL_INSTITUTION_WHOSE_MODEL_HAS_BEEN_REPLICATED_IN", "note": "AIIMS New Delhi's model has been replicated in 25 AIIMS across India, beginning to extend world-class medical education beyond the capital"},
            {"entity": "India's post-independence institution-building (IITs, IIMs, AIIMS — national capability symbols)", "relationship": "FLAGSHIP_MEDICAL_INSTITUTION_OF_INDIA'S_POST-INDEPENDENCE", "note": "AIIMS New Delhi — alongside IITs and IIMs — represents India's determination to develop world-class public institutions as symbols of national capability"}
        ],
    }),

    ("central-hospital-of-wuhan", {
        "summary": (
            "The Central Hospital of Wuhan (武汉市中心医院 — est. 1880s as Putai Hospital, Wuhan, Hubei Province, China) is the hospital at the centre of the COVID-19 pandemic's emergence — where Dr. Li Wenliang (ophthalmologist, 33) first attempted to warn colleagues about a SARS-like illness in December 2019, was summoned by police for 'making false comments,' and subsequently died of COVID-19 in February 2020, becoming the first martyr of the pandemic and a symbol of the cost of suppressing medical whistleblowers. The Central Hospital of Wuhan treated some of the first COVID-19 patients in December 2019, losing multiple doctors and nurses to the disease.\n\n"
            "The hospital's role in the COVID-19 origin story — receiving the first cluster of patients with an unexplained pneumonia in late November/early December 2019, from whom the samples that identified SARS-CoV-2 were obtained — makes it the primary institutional site of the pandemic's earliest documented events. Li Wenliang's attempt on December 30, 2019, to warn his medical school classmates about seven patients with SARS-like symptoms — the WeChat message that became the first public documentation of the emerging outbreak — initiated the sequence of events that brought COVID-19 to global attention.\n\n"
            "Li Wenliang's death on February 7, 2020 — at the age of 33, less than six weeks after being reprimanded by Wuhan police and forced to sign a statement retracting his warning — triggered one of the largest expressions of public grief and anger in China since Tiananmen Square (1989), with millions of Chinese citizens expressing outrage at the suppression of early warnings and his memorial creating the most intense episode of censorship pressure on Weibo and WeChat during the early pandemic."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Hospital at centre of COVID-19 pandemic's emergence (est. 1880s Wuhan Hubei Province); Dr. Li Wenliang (ophthalmologist 33, December 30 2019 WeChat warning, police reprimand, COVID-19 death February 7 2020, first pandemic martyr); first COVID-19 patient cluster (November/December 2019); SARS-CoV-2 identification samples source; largest Chinese public grief since Tiananmen 1989; medical whistleblower suppression cost symbol; multiple doctors and nurses lost to COVID-19; pandemic origin site.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The emergence of SARS-CoV-2 in Wuhan in late 2019 — with the first cluster of patients presenting at the Central Hospital of Wuhan with unexplained pneumonia symptoms — created the circumstances under which the hospital became the institutional site of the pandemic's earliest documented events",
            "China's institutional culture of information control — and the specific pressure on healthcare professionals not to spread 'false information' about sensitive health events — created the environment in which Li Wenliang was reprimanded for attempting to warn colleagues, suppressing early warning information that might have allowed faster containment",
            "The concentration of COVID-19 cases at the Central Hospital of Wuhan — and the hospital's resulting losses among medical staff, including Li Wenliang — created the personal stories of sacrifice and institutional suppression that shaped global perception of the pandemic's early management in China"
        ],
        "effects": [
            "Li Wenliang's death and the public reaction — triggering one of the largest expressions of public grief and anger in China since Tiananmen Square, with millions mourning and criticising the suppression of his warning — forced the Chinese government to posthumously clear him of wrongdoing and created lasting public consciousness about the importance of protecting medical whistleblowers",
            "The Central Hospital of Wuhan's role as the site of the first COVID-19 patient cluster — and the samples from those patients that identified SARS-CoV-2 — made it the institutional location most associated with the pandemic's origin, with the hospital at the centre of the geopolitical controversy about the pandemic's emergence",
            "Li Wenliang's whistleblower case became a global reference point for the importance of protecting medical whistleblowers — cited in WHO reports, national pandemic preparedness reviews, and medical ethics discussions worldwide as the key early-warning failure that may have delayed the global response to COVID-19",
            "The pandemic's spread from Wuhan — beginning with the cases at the Central Hospital of Wuhan — made the hospital the starting point for a chain of events that killed 7+ million people globally (WHO estimate), disrupted the global economy, and transformed social behaviour and health policy worldwide, making the Central Hospital of Wuhan the institution most closely associated with the 21st century's most consequential public health crisis"
        ],
        "relationships": [
            {"entity": "Dr. Li Wenliang (ophthalmologist, December 2019 warning, police reprimand, February 2020 death, pandemic martyr)", "relationship": "INSTITUTIONAL_SITE_OF_THE_MEDICAL_CAREER_AND_DEATH_OF", "note": "Li Wenliang's warning, reprimand, and death at the Central Hospital of Wuhan made the institution the site of the pandemic's first and most powerful human story"},
            {"entity": "COVID-19 pandemic (SARS-CoV-2, first cluster December 2019, 7M+ global deaths)", "relationship": "INSTITUTIONAL_SITE_OF_THE_EARLIEST_DOCUMENTED_PATIENT_CLUSTER_OF_THE", "note": "The Central Hospital of Wuhan received the first cluster of COVID-19 patients in late 2019, making it the primary institutional site of the pandemic's earliest events"},
            {"entity": "SARS-CoV-2 identification (December 2019 samples, novel coronavirus identification)", "relationship": "INSTITUTIONAL_SOURCE_OF_THE_PATIENT_SAMPLES_USED_IN_THE", "note": "Samples from the hospital's first COVID-19 patients were used to identify SARS-CoV-2 as a novel coronavirus"},
            {"entity": "Medical whistleblower protection (Li Wenliang case, WHO pandemic preparedness reference)", "relationship": "INSTITUTIONAL_SITE_OF_THE_MOST_CITED_CONTEMPORARY_CASE_FOR_THE_IMPORTANCE_OF", "note": "Li Wenliang's suppression at the Central Hospital of Wuhan became the global reference case for medical whistleblower protection in pandemic preparedness"},
            {"entity": "Chinese public grief and censorship (largest since Tiananmen 1989, Weibo/WeChat suppression)", "relationship": "INSTITUTIONAL_ASSOCIATION_TRIGGERING_THE", "note": "Li Wenliang's death triggered the largest expression of Chinese public grief and anger since Tiananmen, creating intense censorship pressure on Chinese social media"}
        ],
    }),

    ("the-royal-london-hospital", {
        "summary": (
            "The Royal London Hospital (est. 1740 as the London Infirmary, Royal London since 1990, Whitechapel, East London — relocated to its new £1 billion purpose-built premises in 2012) is one of the oldest and largest teaching hospitals in Britain — a founding teaching hospital of Barts and The London School of Medicine and Dentistry, the hospital that treated the victims of the Jack the Ripper murders (1888), the hospital where John Merrick (the 'Elephant Man') lived from 1886 until his death in 1890, and one of the UK's busiest trauma centres. The hospital's location in Whitechapel — historically one of the poorest districts of London — reflects its mission to serve the East End's working-class and immigrant population.\n\n"
            "The London Infirmary was founded in 1740 by a group of seven subscribers who met in a tavern in Featherstone Street — beginning with a rented house in Moorfields and moving to its famous Whitechapel Road buildings in 1757 — as one of the wave of voluntary hospitals established in 18th-century London to provide medical care for the poor who could not afford private physicians. The hospital's founding reflected the Enlightenment's philanthropic impulse to extend medical care beyond the wealthy.\n\n"
            "The hospital's most famous patient — John Merrick, the 'Elephant Man' — lived in the hospital's basement from 1886 to 1890 under the protection of Frederick Treves, and his story (told in Treves's The Elephant Man and Other Reminiscences, 1923, and later in David Lynch's film, 1980) made the Royal London Hospital the most culturally resonant hospital in the world, with Merrick's skeleton and effects still held in the hospital's museum."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "One of oldest and largest British teaching hospitals (est. 1740 as London Infirmary, Royal London since 1990, Whitechapel East London); John Merrick 'Elephant Man' (lived hospital 1886–1890, Frederick Treves, David Lynch film 1980); Jack the Ripper murder victims treated 1888; founding teaching hospital Barts and The London School of Medicine; £1B new premises 2012; UK's busiest trauma centres; Whitechapel working-class and immigrant population service; 18th-century voluntary hospital philanthropy.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The 18th-century voluntary hospital movement — driven by Enlightenment philanthropy and the recognition that London's rapidly growing poor working-class population had no access to medical care — prompted the founding of the London Infirmary in 1740 by seven subscribers who provided both the funds and the governance for a hospital serving the East End's poor",
            "Whitechapel's position as the entry point for successive waves of immigrants into London — Huguenots, Irish, Jews, and later Bangladeshis — and the extreme poverty of the East End's working class created the concentrated medical need that made the Royal London's Whitechapel location the most appropriate site for a hospital serving the genuinely poor",
            "Frederick Treves's decision to bring John Merrick to the hospital (1886) — protecting him from the exploitation of the freak show circuit — reflected the hospital's culture of humanitarian medicine that extended compassion beyond clinical treatment, creating the association with Merrick that has made the Royal London Hospital the most culturally resonant hospital in Britain"
        ],
        "effects": [
            "The Royal London Hospital's treatment of the Jack the Ripper murder victims (1888) — with hospital records providing some of the most detailed contemporary documentation of the victims — made it a significant institutional source for historical research into the Whitechapel murders, which remain the most studied unsolved murders in history",
            "John Merrick's story — told through Treves's memoir and David Lynch's celebrated 1980 film — made the Royal London Hospital a pilgrimage site for cultural history, with the hospital museum's preservation of Merrick's skeleton and effects providing the material basis for the ongoing scholarly and popular interest in his life",
            "The Royal London Hospital's role as one of the UK's busiest trauma centres — serving East London's population, including some of the UK's most deprived communities and highest rates of violent trauma — has made it the primary acute care institution for a population whose healthcare needs reflect the persistent inequality of East London",
            "The hospital's contribution to Barts and The London School of Medicine — one of the UK's largest medical schools, training a significant proportion of British doctors — has made it an important institution for British medical education, extending its impact beyond its direct patient care to the training of the medical workforce"
        ],
        "relationships": [
            {"entity": "John Merrick / The Elephant Man (1886–1890 residence, Frederick Treves, David Lynch film 1980)", "relationship": "INSTITUTIONAL_HOME_AND_PLACE_OF_DEATH_OF", "note": "Merrick's residence at the Royal London under Treves's protection — and the film it inspired — made the hospital the most culturally resonant in Britain"},
            {"entity": "Frederick Treves (surgeon, Merrick protector, The Elephant Man and Other Reminiscences 1923)", "relationship": "INSTITUTIONAL_HOME_OF_THE_SURGICAL_CAREER_OF", "note": "Treves's protection of Merrick — and his memoir — created the Royal London's most enduring cultural association"},
            {"entity": "Jack the Ripper murders (Whitechapel 1888, victims treated at Royal London, historical records)", "relationship": "TREATED_THE_VICTIMS_OF_THE", "note": "The Royal London's treatment of Ripper victims — and its historical records — make it a significant institutional source for research into the 1888 Whitechapel murders"},
            {"entity": "Barts and The London School of Medicine and Dentistry (founding teaching hospital)", "relationship": "FOUNDING_TEACHING_HOSPITAL_OF", "note": "The Royal London's role as a founding teaching hospital of Barts and The London School has made it an important institution for British medical education"},
            {"entity": "East London immigrant and working-class population service (Whitechapel, Huguenots, Irish, Jews, Bangladeshis)", "relationship": "FOUNDED_FOR_AND_CONTINUES_TO_SERVE_THE", "note": "The Royal London's Whitechapel location — serving successive immigrant and working-class communities — reflects its founding mission of medical care for London's poor"}
        ],
    }),

    ("bellevue-hospital-center", {
        "summary": (
            "Bellevue Hospital Center (est. 1736, New York City — America's oldest public hospital, originally a six-bed infirmary on the site of the Public Workhouse and House of Correction in Lower Manhattan, now a 844-bed Level I Trauma Centre at First Avenue and 27th Street in Manhattan) is the most historically important hospital in the United States — the first American hospital to establish a medical school (New York University School of Medicine, connected via the Bellevue Hospital Medical College founded 1861), the first to establish a nursing school (1873), the first to use the ambulance service (1869), and the hospital that has treated the city's most complex, dangerous, and vulnerable cases for nearly 300 years, including serial killers, US presidents, and the victims of every major New York disaster.\n\n"
            "Bellevue's particular role in American medical history is its status as the primary hospital for the 'undesirable' — the homeless, the mentally ill, the addicted, the immigrant, the criminal — providing care that no private hospital would offer and creating the tradition of American public hospital medicine that distinguishes the US from universal health systems. Bellevue's psychiatric ward — the oldest in America — has housed some of the most famous mental patients in American history, including David Berkowitz (Son of Sam) and Norman Mailer.\n\n"
            "The hospital's eight surviving historical buildings — including the Bellevue Psychiatric Hospital (1931, Art Deco, converted to luxury apartments) and the original 1816 almshouse — document nearly 300 years of American public medicine, and the hospital's location on the East River has made it the primary receiving facility for every major Manhattan disaster from the Triangle Shirtwaist fire (1911) to the 9/11 attacks (2001)."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "America's oldest public hospital (est. 1736 New York City, 844-bed Level I Trauma Centre); first US hospital with medical school (Bellevue Hospital Medical College 1861, linked to NYU School of Medicine); first nursing school (1873); first ambulance service (1869); primary hospital for homeless/mentally ill/addicted/immigrant/criminal — American public hospital tradition; psychiatric ward (oldest in US, David Berkowitz, Norman Mailer); Triangle Shirtwaist fire victims (1911), 9/11 attacks (2001) receiving facility; 300 years of American public medicine.",
            "significanceCategory": "continental"
        },
        "causes": [
            "New York City's rapid growth as the primary American port of entry for immigrants — bringing waves of European immigrants, many arriving sick, destitute, or mentally ill — created the concentrated medical need that drove Bellevue's development from a six-bed infirmary into one of the world's largest and most complex public hospitals",
            "The American tradition of private medicine — in which hospitals were founded by and for the paying middle and upper classes — created the gap in medical provision for the poor, the mentally ill, and the criminal that Bellevue filled as a public institution funded by the city of New York, establishing the tradition of American public hospital medicine",
            "New York City's position as the most complex and dangerous urban environment in 19th and 20th-century America — with industrial disasters, epidemics, violent crime, and mass casualty events — created the clinical demand that drove Bellevue's development of the emergency and trauma medicine innovations (ambulance service, emergency surgery) that became standard American hospital practice"
        ],
        "effects": [
            "Bellevue's first ambulance service (1869) — dispatching horse-drawn wagons to emergency calls from a centralised hospital — created the model for pre-hospital emergency medicine that became the foundation of all subsequent American emergency medical services, ultimately evolving into the 911 emergency call system and paramedic services",
            "Bellevue Hospital Medical College's 1861 founding — and its connection to New York University School of Medicine — created the institutional model for hospital-based medical education that became the standard American approach, eventually displacing the proprietary medical schools and establishing the teaching hospital as the primary vehicle for medical training",
            "Bellevue's nursing school (1873) — one of the first three American nursing schools, inspired by Florence Nightingale's model — established the profession of trained nursing in the United States, producing the workforce that transformed hospital care from custodial attendance to skilled medical support",
            "Bellevue's treatment of the victims of every major New York disaster — from the Triangle Shirtwaist fire (146 dead, 1911) to 9/11 (2001) — has made it the primary institutional memory of New York's mass casualty events, with the hospital's records and the experiences of its staff providing the documentary foundation for the history of urban disaster medicine"
        ],
        "relationships": [
            {"entity": "First American ambulance service (1869, horse-drawn emergency wagon, 911 emergency service precursor)", "relationship": "ORIGINATOR_OF_THE", "note": "Bellevue's 1869 ambulance service — the first in America — created the model that evolved into the modern emergency medical services system"},
            {"entity": "Bellevue Hospital Medical College (1861, linked to NYU School of Medicine, teaching hospital model)", "relationship": "ESTABLISHED_THE_FIRST_HOSPITAL-LINKED_MEDICAL_SCHOOL_IN_AMERICA_THROUGH_THE", "note": "Bellevue's medical college — the first hospital-based medical school in America — established the teaching hospital model that became the standard for American medical education"},
            {"entity": "First American nursing school (1873, Florence Nightingale model, professional nursing establishment)", "relationship": "ESTABLISHED_ONE_OF_THE_FIRST_THREE_AMERICAN_NURSING_SCHOOLS_IN_AMERICA_AT", "note": "Bellevue's 1873 nursing school — inspired by Nightingale's model — established professional trained nursing in the United States"},
            {"entity": "Triangle Shirtwaist fire victims (1911, 146 dead, Bellevue primary receiving hospital)", "relationship": "PRIMARY_RECEIVING_HOSPITAL_FOR_THE_VICTIMS_OF_THE", "note": "Bellevue's treatment of Triangle Shirtwaist victims — and all subsequent major New York disasters — makes it the institutional memory of urban disaster medicine"},
            {"entity": "American public hospital tradition (care for homeless/mentally ill/addicted/immigrant — gap private medicine left)", "relationship": "PRIMARY_HISTORICAL_EXEMPLAR_AND_DEFINING_INSTITUTION_OF_THE", "note": "Bellevue's nearly 300-year role as the hospital for those private medicine would not serve defines the American public hospital tradition"}
        ],
    }),

    ("jewish-hospital-berlin", {
        "summary": (
            "The Jewish Hospital Berlin (Jüdisches Krankenhaus Berlin — est. 1756, Berlin, by the Jewish community of Berlin — at its current site in Wedding since 1914) is the oldest Jewish hospital in Germany, the hospital that survived the Nazi period intact as the only Jewish institution to continue operating throughout the Third Reich (1933–1945), and one of the most historically significant hospitals in Europe — simultaneously serving as a hospital, an old-age home, a collection point for Jews destined for deportation, and a Gestapo office, in a microcosm of the contradictions of Jewish survival under National Socialism.\n\n"
            "The Jewish Hospital's survival through the Nazi period — described in Daniel B. Silver's 2003 book 'Refuge in Hell: How Berlin's Jewish Hospital Outlasted the Nazis' — represents one of the most remarkable institutional survival stories of the Holocaust. The hospital continued operating because it served 'mixed-race' (Mischlinge) patients, the Jewish spouses of non-Jewish Germans (protected by intermarriage), and hospital staff — categories of Jews temporarily protected from deportation under Nazi racial law. By the time the war ended, approximately 800 Jews were living in the hospital complex.\n\n"
            "The Jewish Hospital today continues to operate as a general hospital serving the Wedding district of Berlin, with its history — including the Gestapo deportation collection point that operated within its walls — memorialised in an on-site museum and archive. It is one of the few German institutions that directly confronts its own history of operating under National Socialism."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Oldest Jewish hospital in Germany (est. 1756 Berlin, Wedding site since 1914); only Jewish institution operating throughout Nazi Third Reich (1933–1945); survival because served Mischlinge (mixed-race), intermarried Jewish spouses, hospital staff; Gestapo deportation collection point within hospital walls; 800 Jews living in complex at war's end; Daniel B. Silver 'Refuge in Hell: How Berlin's Jewish Hospital Outlasted the Nazis' (2003); on-site museum memorialising Holocaust within institutional walls; most remarkable Holocaust institutional survival.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The complexity of Nazi racial law — which created multiple categories of Jews with different legal status, including 'Mischlinge' (people of mixed Jewish and non-Jewish ancestry) and the Jewish spouses of non-Jewish Germans protected by intermarriage — created the legal gap that allowed the Jewish Hospital to continue operating, as its patient and staff population included categories temporarily exempt from deportation",
            "The Nazi regime's pragmatic management of its own racial categories — maintaining the hospital because it provided medical care for Jews who were temporarily exempted from deportation, and because closing it would have required the regime to either provide alternative care for these patients or immediately deport them in ways that might have created political complications — explains why the institution was tolerated",
            "The Jewish community of Berlin's 260-year-old investment in the hospital — which had built it into one of Berlin's leading medical institutions by the early 20th century — created both the physical facilities and the institutional prestige that made the hospital worth maintaining even under the Nazi regime"
        ],
        "effects": [
            "The Jewish Hospital's survival as a functioning institution — providing refuge for approximately 800 Jews at the war's end — saved lives that would otherwise have been lost to deportation and extermination, making it one of the most effective German institutions of Jewish survival during the Holocaust",
            "The hospital's role as a Gestapo deportation collection point — where Jews were assembled before being transported to the death camps — while simultaneously providing medical care to those temporarily exempted from deportation, created a documented microcosm of the contradictions of Jewish life under National Socialism that is of extraordinary historical value",
            "The Jewish Hospital's on-site museum and archive — documenting its own history as both a refuge and a deportation point — represents one of the most honest and direct confrontations with the Holocaust within a German institution, contributing to the culture of German Erinnerungskultur (memory culture) that distinguishes Germany's approach to its Nazi past",
            "The hospital's continuation as a general hospital in Wedding today — serving a diverse Berlin population in a district that has changed from a Jewish community to a working-class and immigrant neighbourhood — embodies the transformation of Berlin's Jewish institutional heritage into a universally accessible public resource"
        ],
        "relationships": [
            {"entity": "Holocaust and Nazi persecution of Jews (1933–1945, only Jewish institution continuously operating)", "relationship": "SOLE_JEWISH_INSTITUTION_TO_OPERATE_CONTINUOUSLY_THROUGHOUT_THE", "note": "The Jewish Hospital's survival as the only continuously operating Jewish institution through the Nazi period is its most historically significant characteristic"},
            {"entity": "Nazi racial law Mischlinge categories (mixed-race and intermarried Jews, temporary deportation exemption)", "relationship": "INSTITUTIONAL_SURVIVAL_ENABLED_BY_THE_EXEMPTIONS_IN", "note": "The Mischlinge and intermarriage exemptions in Nazi racial law created the legal gap that allowed the hospital to continue operating"},
            {"entity": "Daniel B. Silver ('Refuge in Hell' 2003, institutional survival account)", "relationship": "SUBJECT_OF_THE_DEFINITIVE_HISTORICAL_ACCOUNT", "note": "Silver's 2003 book documents the remarkable story of the Jewish Hospital's survival through the Third Reich"},
            {"entity": "Gestapo deportation collection point (operated within hospital walls, Jews assembled for extermination)", "relationship": "CONTAINED_A_GESTAPO", "note": "The Gestapo's operation of a deportation collection point within the hospital walls creates the extraordinary historical contradiction of simultaneous refuge and deportation site"},
            {"entity": "German Erinnerungskultur (memory culture, Holocaust confrontation, on-site museum)", "relationship": "NOTABLE_INSTITUTIONAL_EXEMPLAR_OF", "note": "The hospital's on-site museum — confronting its own history as both refuge and deportation point — is one of Germany's most direct institutional confrontations with the Nazi past"}
        ],
    }),

    ("sisters-of-charity-hospital", {
        "summary": (
            "Sisters of Charity Hospital (est. 1848, Buffalo, New York — founded by the Sisters of Charity of Saint Elizabeth, a Roman Catholic religious institute — part of the Catholic Health System which includes five hospitals and multiple healthcare facilities in Western New York) is the oldest hospital in Buffalo, the primary institution that established Catholic hospital healthcare in Western New York, and a representative institution of the 19th-century Catholic nursing sisters' movement that created the first systematically organised nursing care in American history.\n\n"
            "The Sisters of Charity Hospital was founded in 1848 — three years before Florence Nightingale's nursing reforms (1853–1856) — as part of the Catholic religious nursing movement that created hospitals across the American frontier, serving immigrant Catholic populations (predominantly Irish and German) in rapidly growing industrial cities. The Sisters of Charity's nursing model — with trained religious women providing both medical care and spiritual support — was the only organised nursing system in North America before Nightingale's reforms, and the Catholic hospital network they built became the foundation of American hospital infrastructure in the Midwest and West.\n\n"
            "Sisters of Charity Hospital today operates as part of the Catholic Health System, with campuses in Buffalo and Cheektowaga, providing acute care, emergency services, and specialist healthcare to Western New York's population — and continuing the 175+ year tradition of mission-driven healthcare for the poor and underserved that the Sisters of Charity established at their 1848 founding."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Oldest hospital in Buffalo NY (est. 1848, Sisters of Charity of Saint Elizabeth, Roman Catholic religious institute); 19th-century Catholic nursing sisters' movement — first systematically organised nursing in America (predating Nightingale's reforms 1853–1856); Irish and German immigrant Catholic population service; American frontier hospital building — Catholic network — Midwest and West hospital infrastructure foundation; part of Catholic Health System (five hospitals, Western New York); 175+ year mission-driven healthcare for poor and underserved.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The mass immigration of Catholic Irish and German populations to American industrial cities in the 1840s — driven by the Irish famine (1845–1849) and German political upheaval (1848) — created a concentrated Catholic population in Buffalo with urgent healthcare needs and the religious community infrastructure to support the founding of a Catholic hospital",
            "The Catholic religious nursing movement's pre-Nightingale model of organised healthcare — with religious women providing both medical care and spiritual support under the direction of religious institutes — created the institutional form that the Sisters of Charity of Saint Elizabeth applied in founding the Buffalo hospital, three years before Nightingale's landmark nursing reforms",
            "Buffalo's position as a rapidly growing industrial city at the terminus of the Erie Canal — the primary conduit for immigration and commerce into the American Midwest — created both the population growth that drove healthcare demand and the immigrant Catholic community that the Sisters of Charity's founding mission was designed to serve"
        ],
        "effects": [
            "Sisters of Charity Hospital's 175+ years of continuous operation — through Buffalo's industrial boom, decline, and post-industrial transformation — has maintained healthcare provision for some of Buffalo's most deprived communities, embodying the Catholic healthcare mission of service to the poor and underserved across dramatic changes in the city's economic and demographic character",
            "The Catholic hospital network's contribution to American healthcare infrastructure — with the Sisters of Charity and similar religious institutes building hospitals across the American frontier ahead of any public or private provision — established the Catholic hospital system as the primary healthcare provider in many American communities, a position that Catholic Health System and similar networks maintain today",
            "The 19th-century Catholic nursing sisters' pre-Nightingale nursing model — providing organised, trained nursing care before Nightingale's secular nursing reforms created an alternative model — established the institutional precedent for organised nursing in America and influenced the subsequent development of both Catholic and secular nursing practice",
            "Sisters of Charity Hospital's integration into the Catholic Health System — operating alongside four other Western New York Catholic hospitals — represents the consolidation of the 19th-century Catholic hospital movement into the large Catholic health systems that today operate the largest private hospital network in the United States"
        ],
        "relationships": [
            {"entity": "Sisters of Charity of Saint Elizabeth (founding religious institute, Roman Catholic nursing order)", "relationship": "FOUNDED_AND_ORIGINALLY_STAFFED_BY_THE", "note": "The Sisters of Charity of Saint Elizabeth's nursing mission — providing organised medical and spiritual care — created the hospital and defined its Catholic healthcare identity"},
            {"entity": "19th-century Catholic nursing movement (pre-Nightingale organised nursing, American frontier hospitals)", "relationship": "REPRESENTATIVE_INSTITUTION_OF_THE", "note": "Sisters of Charity Hospital exemplifies the Catholic religious nursing movement that built America's first organised hospital nursing system — predating Nightingale's reforms"},
            {"entity": "Irish famine immigration (1845–1849, Catholic immigrant population, Buffalo industrial city)", "relationship": "FOUNDING_PARTLY_DRIVEN_BY_THE_HEALTHCARE_NEEDS_OF_THE_FAMINE_IMMIGRANT_POPULATIONS_INCLUDING_THE", "note": "The Irish famine's mass Catholic immigration to Buffalo — the Erie Canal terminus — created the population need that drove the hospital's 1848 founding"},
            {"entity": "Catholic Health System (five hospitals, Western New York, institutional parent)", "relationship": "COMPONENT_HOSPITAL_OF_THE", "note": "Sisters of Charity Hospital's integration into the Catholic Health System represents the consolidation of the 19th-century Catholic hospital movement into modern health systems"},
            {"entity": "Florence Nightingale nursing reforms (1853–1856, secular nursing model, preceded by Catholic nursing sisters)", "relationship": "FOUNDING_PREDATED_THE_LANDMARK", "note": "Sisters of Charity Hospital's 1848 founding — three years before Nightingale's reforms — demonstrates that Catholic religious nursing sisters created organised nursing in America before Nightingale's secular model"}
        ],
    }),

]


if __name__ == "__main__":
    print(f"Batch 50 \u2014 {len(ENTITIES)} entities (Class 354: Famous Hospitals)")
    for slug, data in ENTITIES:
        print(f"\n\u2192 {slug}")
        enrich_entity(slug, data)
    print("\n\u2713 Done")
