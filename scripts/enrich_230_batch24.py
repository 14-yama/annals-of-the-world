#!/usr/bin/env python3
"""
Batch 24 — 8 entities: Giustina Rocca, Abu Saeed Mubarak Makhzoomi,
Omowumi Ogunrotimi, Sudhanshubala Hazra, Regina Guha, Publius Antistius,
Abbad ibn Abd Allah ibn al-Zubayr, Zaima Rahman
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

    # 1 — Giustina Rocca
    ("giustina-rocca", {
        "summary": (
            "Giustina Rocca was an Italian Renaissance lawyer, judge, and diplomat who "
            "has been described as among the world's earliest documented female lawyers "
            "— and who has been proposed as an inspiration for Shakespeare's character "
            "Portia in The Merchant of Venice, the fictional female lawyer who disguises "
            "herself as a male advocate to save her husband's friend from a legally "
            "binding bond of flesh. Rocca's actual career — in which she practiced law, "
            "served as a judge, and conducted diplomatic missions — was itself a remarkable "
            "transgression of the formal and informal prohibitions against women entering "
            "the legal profession that characterized medieval and Renaissance European law.\n\n"
            "The legal tradition of medieval and Renaissance Europe — rooted in Roman law "
            "and canon law — was formally closed to women. The Corpus Juris Civilis "
            "(Justinian's 6th-century codification) had been interpreted to prohibit "
            "women from appearing as advocates, and this prohibition was reinforced by "
            "canon law and by the social assumptions of European learned culture. Against "
            "this background, women who did practice law — whether as advocates, notaries, "
            "or judges — did so in exceptional circumstances that required unusual "
            "combinations of family connection, personal ability, local tolerance, and "
            "the absence of male competition.\n\n"
            "The tradition of learned Italian women — exemplified by figures like Novella "
            "d'Andrea (who reportedly lectured at Bologna in her father's place behind a "
            "veil, lest her beauty distract students) and Christine de Pizan (who wrote "
            "about women's intellectual capacity) — provided a cultural context within "
            "which exceptional women like Rocca could find some space. Italy's city-states, "
            "with their diverse legal environments and merchant cultures that valued "
            "commercial legal expertise, offered more flexibility than northern European "
            "feudal systems.\n\n"
            "Whether or not she was Shakespeare's direct inspiration for Portia, Giustina "
            "Rocca stands as a remarkable historical figure — a woman who practiced "
            "law, judged, and conducted diplomacy in an era when all three activities "
            "were formally reserved for men."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Italian Renaissance lawyer, judge, and diplomat claimed as one of history's earliest documented female legal practitioners and proposed as an inspiration for Shakespeare's Portia — a figure who transgressed formal prohibitions against women in law in medieval Europe.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Italian city-state environment of the Renaissance — with its commercial legal culture, humanist scholarship, and greater social diversity than northern feudal societies — created the exceptional conditions in which a woman like Rocca could practice law",
            "The tradition of Italian learned women — documented in Bologna's law faculty tradition (Novella d'Andrea, etc.) and in Italian humanist culture more broadly — provided the cultural precedents that made Rocca's legal career conceivable",
            "Her personal family connections, intellectual ability, and the specific circumstances of her local legal environment combined to create the rare opportunity for a woman to enter a profession formally closed to her sex"
        ],
        "effects": [
            "Her documented career as a female lawyer, judge, and diplomat established a historical precedent for women in law that scholars have invoked to trace the deep roots of women's legal advocacy",
            "The tradition that she inspired or represented contributed to the Renaissance cultural fascination with exceptional learned women — a fascination reflected in Shakespeare's creation of Portia",
            "Her story has been recovered by legal historians as evidence of the gap between formal legal prohibitions on women's legal practice and the actual exceptional practice that existed in specific circumstances",
            "The 'world's first female lawyer' tradition associated with her name has become a cultural touchstone in discussions of women's legal history"
        ],
        "relationships": [
            {"entity": "Shakespeare's Portia (Merchant of Venice)", "relationship": "PROPOSED_AS_INSPIRATION_FOR", "note": "Has been proposed as a real-life inspiration for Portia — Shakespeare's female lawyer who disguises herself as a male advocate"},
            {"entity": "Italian Renaissance legal culture", "relationship": "PRACTICED_WITHIN", "note": "Her legal career was embedded in the Italian Renaissance city-state legal culture that was the most learned and commercially sophisticated in Europe"},
            {"entity": "Women in medieval and Renaissance law", "relationship": "PIONEER_OF", "note": "One of the earliest documented women to practice law, judge, and conduct diplomacy — transgressing formal prohibitions against women in the legal profession"},
            {"entity": "Corpus Juris Civilis (Roman law tradition)", "relationship": "PRACTICED_DESPITE_PROHIBITION_IN", "note": "The Roman law tradition codified in the Corpus Juris Civilis was interpreted to prohibit women from legal advocacy — the formal barrier she overcame"},
            {"entity": "Bologna University legal tradition", "relationship": "CONNECTED_TO", "note": "Italy's legal culture, centered on Bologna's law faculty, produced several documented women scholars and practitioners including Rocca"}
        ]
    }),

    # 2 — Abu Saeed Mubarak Makhzoomi
    ("abu-saeed-mubarak-makhzoomi", {
        "summary": (
            "Abu Saeed Mubarak Makhzoomi (also known as Mubarak ibn Ali al-Makhzoomi; "
            "c. 1040–1119 CE) was a prominent Sufi mystic, Islamic theologian, and "
            "Hanbali jurist based in Baghdad who combined the disciplines of Islamic "
            "law (fiqh) and mysticism (tasawwuf) during the classical age of Abbasid "
            "intellectual culture. He was a disciple of the great Sufi master Abd "
            "al-Qadir al-Jilani — who would go on to become one of Islam's most "
            "venerated saints and the founder of the Qadiriyya Sufi order — making "
            "Makhzoomi part of the foundational generation of the Qadiri tradition. "
            "His dual identity as a scholar of Hanbali law and a Sufi mystic represented "
            "the synthesis of two intellectual traditions that were sometimes in tension "
            "in medieval Islamic thought.\n\n"
            "The Hanbali school of jurisprudence, founded by Ahmad ibn Hanbal (780–855 CE), "
            "was the most traditionally conservative of the four Sunni legal schools — "
            "emphasizing close adherence to hadith (prophetic tradition) and skepticism "
            "toward rational elaboration of law. Yet Hanbalism also had a Sufi dimension "
            "that is often overlooked: figures like Ibn al-Jawzi and the broader Baghdad "
            "Hanbali tradition accommodated mystical piety alongside legal conservatism. "
            "Makhzoomi's career as both Hanbali jurist and Sufi sheikh exemplifies this "
            "inner plurality of the Hanbali tradition.\n\n"
            "His location in Baghdad — the Abbasid caliphate's capital and the greatest "
            "center of Islamic learning in the 11th-12th centuries — placed him at the "
            "heart of the Islamic intellectual world. Baghdad's madrasas, mosques, and "
            "scholarly circles brought together jurists, theologians, philosophers, "
            "and mystics whose interactions shaped the classical synthesis of Islamic "
            "thought that was transmitted to subsequent generations.\n\n"
            "As a teacher and transmitter of religious knowledge, he participated in "
            "the isnad (chain of transmission) system through which Islamic scholarly "
            "tradition was preserved — each scholar's authority grounded in an "
            "unbroken chain of teachers reaching back to the Prophet."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Hanbali jurist and Sufi mystic in Abbasid Baghdad (c. 1040–1119); disciple of the great Abd al-Qadir al-Jilani; a figure in the foundational generation of the Qadiri Sufi order who embodied the synthesis of legal scholarship and mystical piety.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Abbasid Baghdad's position as the preeminent center of Islamic learning created the intellectual environment that produced the synthesis of Hanbali jurisprudence and Sufi mysticism that Makhzoomi embodied",
            "The Qadiri Sufi tradition — founded by his teacher Abd al-Qadir al-Jilani — provided the mystical framework within which Makhzoomi's spiritual formation occurred",
            "The Hanbali school's paradoxical combination of legal conservatism and Sufi accommodation in the Baghdad tradition created the intellectual space for scholars who combined both dimensions"
        ],
        "effects": [
            "His transmission of hadith and religious knowledge contributed to the scholarly chains (isnad) through which Islamic tradition was preserved and authenticated",
            "His dual role as Hanbali jurist and Sufi disciple contributed to the normalization of the combination of legal scholarship and mystical piety that characterized the Baghdad intellectual tradition",
            "As part of the foundational generation of the Qadiri order, he participated in the early formation of what would become one of Islam's most widespread Sufi brotherhoods",
            "His life and career were recorded in the biographical dictionaries (tabaqat) that document the transmission of Islamic scholarly tradition"
        ],
        "relationships": [
            {"entity": "Abd al-Qadir al-Jilani", "relationship": "DISCIPLE_OF", "note": "A disciple of the great Sufi master Abd al-Qadir al-Jilani — founder of the Qadiriyya — placing him in the foundational generation of the order"},
            {"entity": "Hanbali school of jurisprudence", "relationship": "PRACTITIONER_OF", "note": "A Hanbali jurist based in Baghdad — practicing in the most textually conservative of the four Sunni legal schools"},
            {"entity": "Abbasid Baghdad (Islamic intellectual center)", "relationship": "BASED_IN", "note": "Based in Abbasid Baghdad — the greatest center of Islamic learning in the 11th-12th centuries"},
            {"entity": "Qadiriyya Sufi order", "relationship": "ASSOCIATED_WITH_FOUNDING_GENERATION_OF", "note": "As a disciple of its founder Abd al-Qadir, he was part of the foundational community of what became the Qadiri order"},
            {"entity": "Islamic hadith transmission (isnad system)", "relationship": "PARTICIPATED_IN", "note": "His role as a scholar included participating in the hadith transmission chain that preserved and authenticated Islamic scholarly tradition"}
        ]
    }),

    # 3 — Omowumi Ogunrotimi
    ("omowumi-ogunrotimi", {
        "summary": (
            "Omowumi Ogunrotimi is a Nigerian lawyer, gender justice advocate, and social "
            "innovator who founded and leads the Gender Mobile Initiative — a nonprofit "
            "organization headquartered in Nigeria focused on eliminating gender-based "
            "violence through an innovative combination of policy advocacy, technology "
            "solutions, and public education. Her organization's approach — applying "
            "digital technology and mobile platforms to the challenge of reporting, "
            "documenting, and responding to gender-based violence — has made Gender "
            "Mobile one of the more innovative civil society organizations in Nigeria's "
            "gender justice space.\n\n"
            "Gender-based violence in Nigeria is a pervasive and severely underreported "
            "problem: surveys consistently find that the majority of GBV incidents — "
            "including intimate partner violence, sexual assault, and harassment — are "
            "never reported to authorities, due to a combination of stigma, distrust "
            "of police, lack of accessible reporting mechanisms, fear of retaliation, "
            "and inadequate legal protection for survivors. Ogunrotimi's approach targets "
            "these barriers through technology: mobile-based reporting tools, digital "
            "support networks for survivors, and data collection that documents the "
            "scale and patterns of GBV in ways that are difficult to ignore politically.\n\n"
            "Her work sits at the intersection of legal advocacy and technological "
            "innovation — the 'legal tech' dimension of social justice. By combining "
            "her legal training with digital platform development, she has created tools "
            "that extend access to legal recourse and support for GBV survivors who "
            "would otherwise have no accessible entry point into the formal justice system. "
            "This approach is particularly valuable in contexts — like many Nigerian "
            "states — where legal aid is scarce and police responsiveness to GBV is "
            "limited.\n\n"
            "Her career illustrates the growing significance of technology as a tool "
            "for gender justice in African civil society."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Nigerian lawyer and founder of Gender Mobile Initiative — a nonprofit combining technology, policy advocacy, and public education to combat gender-based violence in Nigeria; a pioneer of tech-enabled gender justice work in West Africa.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Nigeria's severe GBV underreporting crisis — driven by stigma, distrust of police, and inadequate legal protection — created the specific problem that Ogunrotimi's technology-based approach was designed to address",
            "The rapid penetration of mobile phone technology in Nigeria created the platform infrastructure for mobile-based GBV reporting and support tools",
            "Nigeria's weak formal legal aid system — particularly for GBV survivors — created the need for civil society organizations to develop informal technological pathways to legal recourse"
        ],
        "effects": [
            "Gender Mobile Initiative's mobile-based reporting tools have created new accessible entry points for Nigerian GBV survivors to document and report incidents",
            "The data collected through Gender Mobile's technology tools has contributed to the evidence base for GBV policy advocacy in Nigeria",
            "Her innovative combination of legal expertise and digital platform development has influenced thinking about tech-enabled legal empowerment in West African civil society",
            "Her career has demonstrated the potential of legally trained social innovators to create new institutional forms that extend access to justice beyond what conventional civil society organizations achieve"
        ],
        "relationships": [
            {"entity": "Gender Mobile Initiative", "relationship": "FOUNDED_AND_LEADS", "note": "Founder and Executive Director of Gender Mobile Initiative — a Nigerian nonprofit combining technology, policy, and education to combat GBV"},
            {"entity": "Nigerian GBV legal framework", "relationship": "ADVOCATES_FOR_ENFORCEMENT_OF", "note": "Her advocacy targets the implementation and enforcement of Nigeria's legal frameworks protecting GBV survivors"},
            {"entity": "Nigerian civil society gender justice community", "relationship": "MEMBER_OF", "note": "Part of Nigeria's civil society community working on gender-based violence prevention and survivor support"},
            {"entity": "Legal technology (legal-tech) movement", "relationship": "PIONEER_OF_IN_NIGERIA", "note": "Pioneered the application of mobile technology to legal empowerment and GBV reporting in Nigeria"},
            {"entity": "Violence Against Persons Prohibition (VAPP) Act Nigeria", "relationship": "ADVOCATES_FOR", "note": "Her advocacy supports the implementation of Nigeria's VAPP Act — the federal legislation addressing gender-based violence"}
        ]
    }),

    # 4 — Sudhanshubala Hazra
    ("sudhanshubala-hazra", {
        "summary": (
            "Sudhanshubala Hazra was an Indian lawyer and pioneer of women's legal "
            "education in colonial Bengal who fought a landmark campaign to enable "
            "women to enroll as lawyers in Indian courts — a campaign against the "
            "formal exclusion of women from the legal profession under colonial-era "
            "Indian law. As the adopted daughter of Madhusudhan Das — the eminent "
            "Oriya lawyer, politician, and Indian independence movement leader known "
            "as 'Madhubabu' who was a leading figure in early 20th-century Indian "
            "nationalism — and the sister of the noted educator and politician Sailabala "
            "Das, she was embedded in a family tradition of social reform and Indian "
            "intellectual life.\n\n"
            "The exclusion of women from the Indian legal profession was a specific "
            "manifestation of the broader colonial legal system's gender assumptions. "
            "Under the Legal Practitioners Act of 1879 and related provisions, "
            "women were effectively prohibited from being enrolled as advocates — "
            "reflecting both British legal culture and the social conservatism "
            "of the colonial administration. This exclusion was a profound barrier "
            "to Indian women's professional advancement in an era when the legal "
            "profession was one of the primary routes to social prestige, political "
            "influence, and economic independence for educated men.\n\n"
            "Hazra's campaign to change this — involving legal challenges, petitions, "
            "and public advocacy — was part of the broader Indian women's movement "
            "that made significant gains in the late 19th and early 20th centuries. "
            "Indian nationalist politics, with its advocacy for women's education and "
            "social reform, provided a supportive political context for her arguments "
            "that the legal prohibition on women advocates was unjust and anachronistic.\n\n"
            "Her family's connection to the Indian independence movement gave her "
            "advocacy additional political weight in a period when colonial legal "
            "structures were increasingly being challenged by both nationalist "
            "politicians and social reformers."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Indian pioneer lawyer who fought to enable women to enroll as advocates in colonial India; adopted daughter of independence leader Madhusudhan Das; a key figure in the early Indian women's legal empowerment movement.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Legal Practitioners Act of 1879 and its interpretation by colonial courts effectively excluded women from enrolling as advocates — creating the specific legal barrier that Hazra and other pioneers challenged",
            "The Indian nationalist movement's emphasis on women's education and social reform provided the political context and moral framework within which her advocacy for women's legal enrollment gained traction",
            "Her connection to her father Madhusudhan Das — a leading Indian independence movement figure and eminent lawyer — gave her advocacy professional credibility and political access"
        ],
        "effects": [
            "Her campaign contributed to the eventual dismantling of the colonial legal prohibition on women advocates in India — a change formalized through the Legal Practitioners (Women) Act of 1923",
            "Her struggle established historical precedents for women's right to enter the legal profession in the Indian context — contributing to the tradition that later feminist lawyers built upon",
            "Her career as a lawyer in the face of formal prohibition demonstrated the possibility of women practicing law — inspiring other Indian women to seek entry into the legal profession",
            "Her family's involvement in both the independence movement and women's professional advancement illustrates the connection between Indian nationalism and gender reform"
        ],
        "relationships": [
            {"entity": "Madhusudhan Das ('Madhubabu')", "relationship": "ADOPTED_DAUGHTER_OF", "note": "Adopted daughter of Madhusudhan Das — the eminent Oriya lawyer, politician, and Indian independence movement leader"},
            {"entity": "Sailabala Das", "relationship": "SISTER_OF", "note": "Sister of Sailabala Das — the noted Indian educator and politician"},
            {"entity": "Indian women's legal enrollment movement", "relationship": "PIONEER_OF", "note": "Fought a landmark campaign to enable women to enroll as lawyers in Indian courts — against formal colonial-era prohibition"},
            {"entity": "Legal Practitioners Act (India, 1879)", "relationship": "CHALLENGED", "note": "Challenged the colonial Legal Practitioners Act's interpretation that excluded women from legal enrollment"},
            {"entity": "Legal Practitioners (Women) Act (India, 1923)", "relationship": "CONTRIBUTED_TO_PASSAGE_OF", "note": "Her advocacy contributed to the eventual passage of the 1923 Act formally enabling women to enroll as advocates"}
        ]
    }),

    # 5 — Regina Guha
    ("regina-guha", {
        "summary": (
            "Regina Guha was an Indian lawyer and legal educator who in 1916 fought a "
            "notable legal case challenging the interpretation of colonial-era provisions "
            "that effectively prohibited women from practicing law in India — making her "
            "one of the documented pioneers of the Indian women's legal advocacy movement "
            "that eventually succeeded in overturning the formal exclusion of women from "
            "the Indian legal profession. Her 1916 case predates the Legal Practitioners "
            "(Women) Act of 1923 by seven years, making her a figure who challenged the "
            "exclusion while the formal prohibition was still fully in force.\n\n"
            "Colonial India's legal profession was governed by the Legal Practitioners "
            "Act of 1879, which had been interpreted to prohibit women from enrollment "
            "as advocates. This interpretation reflected both British legal culture — "
            "English women were not admitted to the bar until the Sex Disqualification "
            "(Removal) Act 1919 — and the social assumptions of the colonial "
            "administration regarding women's appropriate social roles. The exclusion "
            "was a significant barrier in an era when the legal profession was the "
            "primary route to professional prestige and political influence for "
            "educated Indians.\n\n"
            "Guha's 1916 case — whether a formal court challenge to her enrollment "
            "or a case in which she appeared despite the prohibition — placed her "
            "in a small cohort of Indian women who challenged the legal exclusion "
            "before formal change was legislated. This early challenge documented "
            "the absurdity of the prohibition at a time when Indian women's education "
            "was advancing rapidly and Indian nationalism was building its critique "
            "of colonial legal discrimination.\n\n"
            "She was also a teacher — bridging the worlds of legal practice and "
            "legal education in the tradition of the Indian lawyer-educator who "
            "contributed to building the institutions of Indian legal professionalism."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Indian pioneer lawyer and teacher who in 1916 challenged colonial-era legal provisions prohibiting women from practicing law — one of the documented early fighters for women's legal professional rights in India.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Legal Practitioners Act of 1879 and its colonial-era interpretation excluding women from legal enrollment created the specific legal barrier that Guha challenged in 1916",
            "The Indian women's education movement — which had significantly advanced women's access to formal education by the early 20th century — produced a generation of educated Indian women capable of challenging the legal profession's exclusions",
            "Indian nationalism's critique of colonial legal discrimination provided the political and moral framework within which Guha's challenge could be articulated as a matter of justice rather than mere personal ambition"
        ],
        "effects": [
            "Her 1916 challenge documented the formal exclusion of women from the Indian legal profession at a historically specific moment — building the evidentiary and moral case that contributed to the 1923 legislative change",
            "Her case established a legal precedent that subsequent advocates for women's legal rights in India could cite as an early formal challenge",
            "Her dual role as lawyer and teacher contributed to the development of Indian legal education and to the growing presence of women in Indian legal institutions",
            "Her career as a woman lawyer in the face of formal prohibition inspired other Indian women to seek entry into the legal profession"
        ],
        "relationships": [
            {"entity": "Legal Practitioners Act (India, 1879)", "relationship": "CHALLENGED_INTERPRETATION_OF", "note": "Fought a notable 1916 case challenging the colonial-era interpretation that prohibited women from practicing law"},
            {"entity": "Indian women's legal advocacy movement", "relationship": "PIONEER_OF", "note": "One of the documented early pioneers challenging women's exclusion from the Indian legal profession before the 1923 legislative reform"},
            {"entity": "Legal Practitioners (Women) Act (India, 1923)", "relationship": "CONTRIBUTED_TO_PASSAGE_OF", "note": "Her 1916 challenge, seven years before the 1923 Act, contributed to the legal and moral argument for formal reform"},
            {"entity": "Colonial Bengal legal profession", "relationship": "CHALLENGED_EXCLUSION_FROM", "note": "Challenged the exclusion of women from the colonial Bengal legal profession — the most intellectually active legal jurisdiction in British India"},
            {"entity": "Indian nationalist women's movement", "relationship": "CONNECTED_TO", "note": "Her legal advocacy was embedded in the broader Indian nationalist movement's push for women's education and professional rights"}
        ]
    }),

    # 6 — Publius Antistius
    ("publius-antistius", {
        "summary": (
            "Publius Antistius (fl. 88–82 BC) was a Roman orator, senator, and tribune "
            "of the plebs whose career flourished during one of the most violent and "
            "constitutionally disruptive periods in Roman history — the civil conflicts "
            "between the senatorial aristocrat Lucius Cornelius Sulla and the popular "
            "faction led by Gaius Marius, conflicts that would eventually produce Sulla's "
            "dictatorship and the proscriptions in which thousands of Roman citizens "
            "were killed. Antistius is notable for a remarkable speech that transformed "
            "his reputation and for his role in a politically significant legal proceeding "
            "involving the young Pompey.\n\n"
            "As tribune of the plebs in 88 BC — the same year Sulla marched his armies "
            "on Rome for the first time in Roman history — Antistius delivered what "
            "ancient sources describe as an exceptionally effective speech in opposition "
            "to the irregular candidacy of a prominent senator to the consulship. The "
            "speech was remarkable enough to transform him from a figure of poorly "
            "regarded obscurity to a political presence of some distinction — illustrating "
            "the power of oratory in Roman public life, where forensic and deliberative "
            "rhetoric were the primary tools of political advancement.\n\n"
            "In 86 BC, Antistius presided over a legal proceeding of considerable "
            "political significance: a court that acquitted the young Pompey (Gnaeus "
            "Pompeius, later 'the Great') of a charge of embezzlement of spoils taken "
            "in Picenum by Pompey's father. The political dynamics of the trial were "
            "complex — Pompey's family connections and personal charm were factors — "
            "and the acquittal demonstrated the degree to which Roman legal proceedings "
            "of the period were inseparable from personal and factional politics. "
            "Antistius subsequently gave his daughter in marriage to Pompey, "
            "cementing a personal alliance with one of Rome's rising military "
            "and political figures."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Roman senator, orator, and tribune of the plebs (88 BC) who presided over the acquittal of the young Pompey (86 BC) and whose remarkable oratory transformed his political career — a minor but documented figure in the tumultuous late Roman Republic.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Roman Republic's political crisis of 88–82 BC — the Sullan-Marian civil conflicts that disrupted Roman constitutional government — created the chaotic political environment in which Antistius's career was embedded",
            "Rome's oratorical culture — in which effective public speaking in the Forum or the courts was the primary mechanism of political advancement — created the context in which a single outstanding speech could transform a senator's reputation",
            "The political prosecution of the young Pompey on embezzlement charges — politically motivated in the factional conflicts of the period — created the legal proceeding over which he presided"
        ],
        "effects": [
            "His exceptional speech as tribune in 88 BC demonstrated the power of oratory in Roman political life — his career transformation from obscurity to distinction illustrates how rhetoric functioned as social capital in the Republic",
            "His acquittal of Pompey in 86 BC helped launch one of Rome's most consequential military and political careers — Pompey would go on to become 'the Great', conqueror of the Eastern Mediterranean, and rival of Julius Caesar",
            "His alliance with Pompey — cemented by the marriage of his daughter — illustrates the Roman practice of political alliance-building through familial connections",
            "His career is recorded in the sources of the late Republic (including Plutarch's Life of Pompey) as part of the documentation of Rome's tumultuous late Republican politics"
        ],
        "relationships": [
            {"entity": "Pompey the Great (Gnaeus Pompeius Magnus)", "relationship": "ACQUITTED_AND_ALLIED_WITH", "note": "Presided over the acquittal of the young Pompey on embezzlement charges in 86 BC, then gave his daughter in marriage to Pompey"},
            {"entity": "Roman Senate (late Republic)", "relationship": "MEMBER_OF", "note": "A senator of Rome who served as Tribune of the Plebs in 88 BC and presided over legal proceedings as a senior magistrate"},
            {"entity": "Lucius Cornelius Sulla", "relationship": "POLITICAL_CONTEMPORARY_OF", "note": "His career overlapped with the Sullan-Marian civil conflicts that disrupted the Roman Republic in the 80s BC"},
            {"entity": "Roman oratorical tradition", "relationship": "PRACTITIONER_OF", "note": "A Roman orator whose exceptionally effective speech as Tribune of the Plebs in 88 BC transformed his political reputation"},
            {"entity": "Roman legal proceedings (late Republic)", "relationship": "PRESIDED_OVER", "note": "Presided over a significant legal proceeding — the trial and acquittal of Pompey on embezzlement charges in 86 BC"}
        ]
    }),

    # 7 — Abbad ibn Abd Allah ibn al-Zubayr
    ("abbad-ibn-abd-allah-ibn-al-zubayr", {
        "summary": (
            "Abbad ibn Abd Allah ibn al-Zubayr al-Asadi was an early Islamic scholar, "
            "hadith narrator, and judge who lived during the formative first century of "
            "Islam — the era of the Tabi'un, the second generation of Muslims who learned "
            "from the Companions of the Prophet Muhammad but did not themselves know the "
            "Prophet directly. As the son of Abd Allah ibn al-Zubayr — the Islamic ruler "
            "who governed the Hejaz (Arabia) as a rival caliph to the Umayyads from "
            "683 to 692 CE — he served as judge in Mecca during his father's caliphate, "
            "a period of acute civil war in the nascent Islamic community.\n\n"
            "The First and Second Fitna (the Islamic civil wars) are among the most "
            "consequential events in Islamic history — dividing the community over the "
            "question of legitimate leadership in ways that produced the Sunni-Shia split "
            "and the Umayyad-Zubayrid rivalry. Abd Allah ibn al-Zubayr's counter-caliphate "
            "in Mecca was a serious challenge to Umayyad authority that controlled the "
            "holy cities of Mecca and Medina for nearly a decade. As his son and the "
            "judge of Mecca during this period, Abbad ibn Abd Allah was embedded in "
            "one of the most politically charged moments in early Islamic governance.\n\n"
            "His role as a hadith narrator — transmitting the sayings and practices "
            "of the Prophet through his own knowledge and through the reports of those "
            "who knew the Prophet or his Companions — made him part of the critical "
            "generation that preserved and transmitted the oral tradition that would "
            "become the hadith literature. The Tabi'un were crucial intermediaries "
            "in this process: their testimony about what they heard from the Companions "
            "formed essential links in the isnad chains that authenticated later hadith "
            "collections.\n\n"
            "His combination of legal authority as judge and scholarly authority as "
            "hadith transmitter exemplifies the integration of judicial and scholarly "
            "roles in early Islamic society."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Early Islamic judge, hadith narrator, and Tabi'un scholar; son of Abd Allah ibn al-Zubayr who served as judge of Mecca during his father's counter-caliphate (683–692 CE); a witness to the Second Fitna and the formative period of Islamic legal institutions.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Second Fitna — the civil war between the Umayyad caliphate and the Zubayrid counter-caliphate — created the political context in which his father ruled the Hejaz and he served as judge of Mecca",
            "The Tabi'un generation's critical role in preserving and transmitting the Prophet's legacy — as the generation that learned from the Companions — made scholars like Abbad essential links in the chain of Islamic knowledge transmission",
            "The emerging institutional need for judges in the rapidly expanding Islamic community's urban centers — Mecca, Medina, Kufa, Basra — created the administrative role he occupied in his father's caliphate"
        ],
        "effects": [
            "His hadith narrations became part of the corpus of early Islamic tradition — preserved in hadith collections and contributing to the scholarly record of prophetic sayings and practices",
            "His judicial service in Mecca during the Zubayrid period contributed to the administration of legal governance in the holy city during one of Islam's most politically turbulent early periods",
            "His family's resistance to Umayyad authority — and his service within it — was documented in the historical sources of the early Islamic period that preserve the memory of the Fitna",
            "As a member of the Tabi'un and son of a rival caliph, his person embodied both the scholarly and political dimensions of early Islamic community formation"
        ],
        "relationships": [
            {"entity": "Abd Allah ibn al-Zubayr (counter-caliph)", "relationship": "SON_OF", "note": "Son of Abd Allah ibn al-Zubayr — the Zubayrid counter-caliph who governed Mecca and the Hejaz in opposition to the Umayyads from 683–692 CE"},
            {"entity": "Mecca (as Zubayrid capital)", "relationship": "SERVED_AS_JUDGE_OF", "note": "Served as judge (qadi) in Mecca during his father's caliphate over the Hejaz"},
            {"entity": "Tabi'un (second generation of Muslims)", "relationship": "MEMBER_OF", "note": "A member of the Tabi'un — the second generation of Muslims who learned from the Companions of the Prophet but did not know the Prophet directly"},
            {"entity": "Islamic hadith transmission", "relationship": "CONTRIBUTOR_TO", "note": "A narrator of hadith whose transmissions contributed to the early Islamic scholarly tradition"},
            {"entity": "Second Fitna (Islamic civil war, 680–692 CE)", "relationship": "PARTICIPATED_IN", "note": "His judicial service was embedded in the Second Fitna — the civil war between the Umayyads and Zubayrids that shaped early Islamic political history"}
        ]
    }),

    # 8 — Zaima Rahman
    ("zaima-rahman", {
        "summary": (
            "Zaima Zarnaz Rahman (known as Zaima Rahman) is a Bangladeshi barrister "
            "and the daughter of Tarique Rahman — the acting Chairman of the Bangladesh "
            "Nationalist Party (BNP) and Prime Minister-in-waiting of the BNP political "
            "family — and the granddaughter of former Bangladeshi Prime Minister Khaleda "
            "Zia and former President Ziaur Rahman. Her family background places her "
            "at the center of Bangladesh's most consequential political dynasty outside "
            "the Awami League — a political inheritance of considerable weight in a "
            "country where elite family networks have dominated national politics since "
            "independence in 1971.\n\n"
            "Her legal training as a barrister — a qualification associated with English "
            "bar admission — gives her formal legal credentials that can both serve the "
            "BNP's organizational and legal needs and provide her with a professional "
            "identity beyond her political family. Bangladeshi politics has been deeply "
            "shaped by the rivalry between the two dominant dynasties: the Mujib-Hasina "
            "line (founding father Sheikh Mujibur Rahman's family, represented by Sheikh "
            "Hasina) and the Zia-Khaleda line (President Ziaur Rahman's family, represented "
            "by Khaleda Zia and Tarique Rahman). Zaima's generation represents the "
            "continuation of this dynastic politics into the 21st century.\n\n"
            "Bangladesh's political history since the 1990s has been characterized by "
            "intense rivalry between the BNP and the Awami League, punctuated by military "
            "interventions, political crises, and the imprisonments of both Khaleda Zia "
            "and Sheikh Hasina at different points. Her family's experience of political "
            "persecution — her father Tarique has lived in exile in London since 2008, "
            "and her grandmother Khaleda Zia has faced politically contested convictions "
            "— has defined the context of her legal career.\n\n"
            "'Politics in Bangladesh is inherited with the blood' — the observation "
            "of many analysts — is personified in the Rahman family's continuation "
            "through Zaima's generation."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Bangladeshi barrister; daughter of BNP acting chairman Tarique Rahman; granddaughter of Prime Minister Khaleda Zia and President Ziaur Rahman — part of Bangladesh's most influential political dynasty outside the Awami League.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Bangladesh's dynastic political culture — in which the BNP (Zia family) and Awami League (Mujib family) have alternated power since the 1990s — created the family political inheritance that defines her public significance",
            "Her family's forced political exile — with her father Tarique Rahman living in London since 2008 under politically contested legal charges — created the circumstances in which her legal training becomes practically significant for the family's political future",
            "Bangladesh's legal system's use against political opponents — with both Khaleda Zia and other BNP leaders facing convictions that many observers consider politically motivated — created the context in which legally trained family members matter"
        ],
        "effects": [
            "Her legal training provides the BNP political family with a legally credentialed next-generation figure capable of navigating both political and legal challenges",
            "Her existence as a publicly recognized figure of the Zia-Khaleda dynasty contributes to the continuation of Bangladesh's most influential opposition political family into a new generation",
            "Her English barrister training — like many elite South Asian politicians' legal qualifications — positions her for potential political entry in a tradition where legal credentials have served as political stepping stones",
            "Her family's political significance means her own career will be closely watched as an indicator of BNP's succession planning and generational transition"
        ],
        "relationships": [
            {"entity": "Tarique Rahman (BNP acting chairman)", "relationship": "DAUGHTER_OF", "note": "Daughter of Tarique Rahman — acting Chairman of the Bangladesh Nationalist Party and son of President Ziaur Rahman"},
            {"entity": "Khaleda Zia (former PM of Bangladesh)", "relationship": "GRANDDAUGHTER_OF", "note": "Granddaughter of former Bangladeshi Prime Minister Khaleda Zia — the BNP's founding leader after Ziaur Rahman's assassination"},
            {"entity": "Ziaur Rahman (former President of Bangladesh)", "relationship": "GRANDDAUGHTER_OF", "note": "Granddaughter of President Ziaur Rahman — founder of the Bangladesh Nationalist Party, assassinated in 1981"},
            {"entity": "Bangladesh Nationalist Party (BNP)", "relationship": "FAMILY_LEADS", "note": "Her family — the Zia dynasty — has led the BNP since its founding, making her part of Bangladesh's most significant political opposition dynasty"},
            {"entity": "Bangladesh dynastic political system", "relationship": "EMBEDDED_IN", "note": "Her political significance is inseparable from Bangladesh's dynastic two-party system in which the Zia and Mujib families have dominated since independence"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 24)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
