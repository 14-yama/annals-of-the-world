#!/usr/bin/env python3
"""
Batch 13 — 8 entities: Achille Grassi, Elio Lampridio Cerva, Bettisia Gozzadini,
Ibn Abd al-Malik al-Marrakushi, Stephanos Sahlikis, Bahlool,
Jan II Carondelet, Rabghuzi
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

    # 1 — Achille Grassi (c. 1463–1523)
    ("achille-grassi", {
        "summary": (
            "Achille Grassi (c. 1463–1523) was an Italian bishop, cardinal, and humanist ecclesiastic whose career "
            "exemplified the intersection of papal diplomacy, conciliar reform, and Renaissance patronage under the "
            "tumultuous pontificates of Alexander VI, Julius II, and Leo X. Born into a noble Bolognese family with strong "
            "ties to the papacy, he studied canon law and rose through curial service before being appointed Bishop of "
            "Bologna (1504–1511) by Pope Julius II, the most powerful ecclesiastical see in northern Italy and a strategic "
            "linchpin of the Papal States' authority in the Po Valley.\n\n"
            "As Bishop of Bologna, Grassi administered a major university city during a period of intense political "
            "tension — Julius II was simultaneously engaged in the League of Cambrai wars, and Bologna's loyalty to "
            "Rome was essential to the papal military strategy in Italy. Grassi was elevated to the cardinalate in 1511 "
            "by Julius II, who recognized his administrative competence and personal loyalty, and he participated in the "
            "Fifth Lateran Council (1512–1517) — the reforming council convened partly in response to the schismatic "
            "Council of Pisa convened by Louis XII of France. He was appointed Cardinal-Bishop of Ostia and served as "
            "Dean of the College of Cardinals.\n\n"
            "As Dean of the Sacred College and Cardinal Camerlengo, Grassi played an important constitutional role in "
            "the administration of the papacy during sede vacante periods. He was a noted patron of humanist scholars "
            "and maintained connections with the scholarly culture centered on the Roman curia. His tomb in the church "
            "of Sant'Angelo in the Vatican bears testimony to his position among the leading prelates of the High "
            "Renaissance papacy.\n\n"
            "'A prince of the Church who served three popes through the years when Christendom began to fracture.' "
            "Grassi witnessed the opening of the Protestant Reformation but died before its full consequences became "
            "clear, his long career spanning the cusp of an era."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Cardinal Dean of the Sacred College under Julius II and Leo X; participated in the Fifth Lateran Council (1512–1517) as the church wrestled with reform pressures that would shortly produce the Protestant Reformation.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Julius II's aggressive reconstruction of papal authority in northern Italy required loyal and competent bishops in strategic sees like Bologna",
            "The schismatic Council of Pisa (1511) convened by Louis XII of France necessitated a counter-council (Fifth Lateran, 1512–1517) in which Grassi participated as a leading cardinal",
            "The Bolognese noble family's long curial connections provided the social and institutional networks for Grassi's rapid ascent"
        ],
        "effects": [
            "Administered Bologna as bishop during the critical League of Cambrai wars, maintaining the city's loyalty to the Papal States",
            "Participated in the Fifth Lateran Council (1512–1517), contributing to the reform decrees that preceded but failed to preempt the Protestant Reformation",
            "As Cardinal Dean and Camerlengo, exercised important constitutional functions in the administration of the papacy during sede vacante periods",
            "His patronage network contributed to the Roman humanist culture that characterized the High Renaissance papacy"
        ],
        "relationships": [
            {"entity": "Pope Julius II", "relationship": "APPOINTED_BY", "note": "Julius II appointed Grassi Bishop of Bologna (1504) and later Cardinal (1511)"},
            {"entity": "Fifth Lateran Council", "relationship": "PARTICIPATED_IN", "note": "Grassi was among the cardinals who attended the Fifth Lateran Council (1512–1517)"},
            {"entity": "College of Cardinals", "relationship": "DEAN_OF", "note": "Served as Dean of the Sacred College of Cardinals"},
            {"entity": "Pope Leo X", "relationship": "SERVED_UNDER", "note": "Continued to serve as a senior cardinal under Leo X (1513–1521)"},
            {"entity": "Council of Pisa (1511)", "relationship": "OPPOSED", "note": "The schismatic Council of Pisa convened by Louis XII precipitated the Fifth Lateran Council in which Grassi participated"}
        ]
    }),

    # 2 — Elio Lampridio Cerva / Ilija Crijević (1463–1520)
    ("elio-lampridio-cerva", {
        "summary": (
            "Elio Lampridio Cerva (1463–1520), born Ilija Crijević in the Republic of Ragusa (Dubrovnik), was the most "
            "accomplished Latin poet of the Croatian Renaissance and one of the finest Neo-Latin lyricists of 15th-century "
            "Europe. His extraordinary command of classical Latin metres — especially the Horatian ode, the elegiac couplet, "
            "and the Catullan lyric — combined with his humanist education in Rome earned him the title of poeta laureatus "
            "under Pope Sixtus IV, the highest honor available to a Renaissance poet.\n\n"
            "Crijević studied in Rome during the pontificate of Sixtus IV, moving in the circle of the Roman Academy led "
            "by Pomponio Leto, which cultivated classical Latin literature and staged Latin theatre. His years in Rome "
            "exposed him to the full vitality of Italian Renaissance humanism, and he returned to Ragusa transformed — "
            "bringing Neo-Latin literary standards that elevated the cultural output of the small Adriatic republic to "
            "European levels. Back in Ragusa, he served as the city's chancellor and secretary, giving speeches and "
            "composing official Latin correspondence while continuing to write Latin poetry of exceptional elegance. "
            "His Latin odes in the Horatian mode celebrated the beauty of Ragusa, lamented the Ottoman threat to the "
            "Adriatic world, and explored themes of love, friendship, and mortality with classical refinement.\n\n"
            "Crijević was the center of a vibrant humanist circle in Ragusa that included his younger compatriots "
            "such as Jakov Bunić (Jacobus Bonus) and Damjan Beneša (Damianus Benessa), establishing Ragusa as a "
            "significant node of Renaissance Latin culture in the eastern Adriatic. His works were praised by "
            "contemporaries across Italy and circulated in manuscript among humanist scholars.\n\n"
            "'He made the Latin tongue sing of Dubrovnik as if Horace himself had moved to the Adriatic.' "
            "Crijević remains the founding figure of Croatian Renaissance Latin literature."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Crowned poet laureate under Sixtus IV and the most accomplished Neo-Latin lyricist of the Croatian Renaissance, he established Ragusa (Dubrovnik) as a center of European humanist Latin culture.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Roman Academy of Pomponio Leto provided the intellectual environment for Crijević's Neo-Latin literary formation during his years in Rome under Sixtus IV",
            "Ragusa's mercantile wealth and political independence from Ottoman and Venetian overlords enabled the cultivation of Italian Renaissance humanism in the eastern Adriatic",
            "The Croatian tradition of Latin learning in Dalmatian cities like Split and Ragusa provided the foundation for Crijević's exceptional classical education"
        ],
        "effects": [
            "Established the standard of Neo-Latin lyric poetry in Croatia that influenced subsequent generations of Ragusan humanists including Jakov Bunić and Damjan Beneša",
            "His appointment as poet laureate by Sixtus IV placed Croatian Renaissance letters on the European humanist map",
            "As chancellor and secretary of Ragusa, elevated the republic's official Latin prose to the standards of Italian humanist chancelleries",
            "Founded the Ragusan humanist circle that made Dubrovnik a significant center of European Renaissance culture in the eastern Mediterranean"
        ],
        "relationships": [
            {"entity": "Pope Sixtus IV", "relationship": "LAUREATED_BY", "note": "Crowned poet laureate by Pope Sixtus IV in Rome, the highest contemporary honor for a Latin poet"},
            {"entity": "Pomponio Leto", "relationship": "ASSOCIATED_WITH", "note": "Moved in the circle of the Roman Academy led by Pomponio Leto during his years in Rome"},
            {"entity": "Republic of Ragusa", "relationship": "SERVED", "note": "Served as chancellor and secretary of Ragusa, writing official Latin correspondence and speeches"},
            {"entity": "Jakov Bunić", "relationship": "MENTORED", "note": "Crijević was the elder figure of the Ragusan humanist circle that included younger poets like Bunić"},
            {"entity": "Marko Marulić", "relationship": "CONTEMPORARY_OF", "note": "Both were the leading Croatian humanist Latin writers of the late 15th century, Crijević in Ragusa, Marulić in Split"}
        ]
    }),

    # 3 — Bettisia Gozzadini (fl. c. 1237–1242)
    ("bettisia-gozzadini", {
        "summary": (
            "Bettisia Gozzadini (fl. c. 1237–1242) was a Bolognese noblewomen and jurist who is among the earliest "
            "documented women to have lectured on law at a medieval university, reportedly teaching canon and civil law "
            "at the University of Bologna from around 1239 — a remarkable achievement in an era when women were largely "
            "excluded from formal academic learning. A member of the noble Gozzadini family of Bologna, she reportedly "
            "studied law privately before obtaining permission to lecture at the university, possibly through the influence "
            "of family connections.\n\n"
            "Medieval accounts of her teaching describe an unusual arrangement: because the presence of a woman in the "
            "lecture hall was considered potentially disruptive to the male students, Bettisia reportedly either wore a "
            "veil while lecturing or taught from behind a curtain — physical accommodations that acknowledged both her "
            "exceptional intellectual achievement and the social norms of 13th-century Bologna. These details, while "
            "preserved in later medieval chronicles and humanist accounts, reflect the extraordinary nature of her "
            "presence in the university environment.\n\n"
            "The University of Bologna had an unusual openness to women scholars by medieval standards — the glossatrix "
            "tradition that produced Novella d'Andrea in the 14th century and Bettisia in the 13th suggests an "
            "institutional culture more accommodating of learned women than most European universities of the period. "
            "Whether Bettisia received a formal teaching appointment or lectured under informal arrangements, her presence "
            "at Bologna in the mid-13th century established a precedent that influenced later women scholars and was "
            "subsequently celebrated in humanist accounts of Bologna's intellectual heritage.\n\n"
            "'She stood behind the curtain and taught a roomful of men the laws of a civilization that scarcely knew "
            "what to do with her.' Bettisia Gozzadini remains a landmark figure in the long history of women in the law."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "One of the earliest documented women to lecture on law at a medieval university (Bologna, c. 1239), Bettisia Gozzadini is a pioneering figure in the history of women in legal education.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The University of Bologna's tradition of legal learning — Europe's oldest university and center of the glossator tradition — created an exceptionally intellectually stimulating environment",
            "The noble Gozzadini family's wealth and connections provided the social capital that enabled Bettisia's unusual access to legal education",
            "Bologna's institutional culture was more receptive to learned women than most European universities, as evidenced by the subsequent careers of Novella d'Andrea and other women scholars"
        ],
        "effects": [
            "Established a precedent for women's participation in legal scholarship at Bologna that influenced subsequent generations, including Novella d'Andrea in the 14th century",
            "Her teaching career was recorded and celebrated in humanist accounts of Bolognese intellectual culture, ensuring that her name entered the documentary record",
            "Contributed to the tradition of the glossator school that made Bologna the center of European legal education in the High Middle Ages",
            "Her example was cited by Renaissance humanists as evidence of women's intellectual capacity, contributing to early feminist arguments"
        ],
        "relationships": [
            {"entity": "University of Bologna", "relationship": "LECTURED_AT", "note": "Reportedly taught canon and civil law at Bologna from c. 1239, one of the earliest documented women to do so"},
            {"entity": "Gozzadini family", "relationship": "MEMBER_OF", "note": "Her noble Bolognese family connections provided the social capital enabling her access to legal education"},
            {"entity": "Novella d'Andrea", "relationship": "PRECEDED", "note": "Bettisia preceded Novella d'Andrea as a model of the woman jurist at Bologna in the glossator tradition"},
            {"entity": "Glossator legal tradition", "relationship": "PARTICIPATED_IN", "note": "Lectured within the glossator school that made Bologna the center of European legal education"},
            {"entity": "Giovanni d'Andrea", "relationship": "PRECEDED_GENERATION_OF", "note": "Bettisia's tradition at Bologna preceded and influenced the era of Giovanni d'Andrea, whose daughter Novella also lectured"}
        ]
    }),

    # 4 — Ibn Abd al-Malik al-Marrakushi (1237–1303)
    ("ibn-abd-al-malik-al-marrakushi", {
        "summary": (
            "Ibn Abd al-Malik al-Marrakushi (1237–1303) was a Moroccan Islamic scholar, judge, historian, and biographer "
            "whose encyclopedic Al-Dhayl wa-l-Takmila ('The Appendix and Completion') constitutes one of the most "
            "important biographical dictionaries of Andalusian and Maghrebi scholars ever compiled, preserving biographical "
            "information about thousands of scholars, jurists, grammarians, poets, and mystics from al-Andalus and Morocco "
            "across the 12th and 13th centuries. Born in Marrakesh under the Almohad dynasty and active during the "
            "Marinid period, he combined judicial service with extraordinary biographical scholarship.\n\n"
            "Al-Dhayl wa-l-Takmila was conceived as a continuation and completion of the major biographical dictionaries "
            "of al-Andalus — particularly Ibn Bashkuwal's Kitab al-Sila and Ibn al-Abbar's Takmila — extending their "
            "coverage to include figures of the late Almohad and early Marinid periods. The work runs to eight volumes "
            "and contains entries on approximately 5,000 individuals, making it a uniquely comprehensive record of the "
            "scholarly class of the western Islamic world at a critical historical juncture: the period of the Reconquista's "
            "acceleration and the collapse of Andalusian civilization in its traditional form. Many of the scholars "
            "he documented were themselves refugees from the advancing Christian kingdoms.\n\n"
            "His work is valuable not only as a biographical dictionary but as a social history: his entries contain "
            "information about scholars' origins, movements, teachers, students, works, and deaths that allows modern "
            "historians to trace the intellectual networks of western Islamic civilization with unusual precision. "
            "He served as a judge in several Moroccan cities and also traveled to the eastern Islamic world, where "
            "he studied with scholars in Egypt and the Levant, broadening his network.\n\n"
            "'He counted the scholars of a vanishing world before they were lost.' Al-Marrakushi's biographical "
            "dictionary remains an irreplaceable source for the history of Islamic scholarship in the medieval Maghreb and Andalus."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "His Al-Dhayl wa-l-Takmila is an encyclopedic biographical dictionary of ~5,000 Andalusian and Maghrebi scholars, an irreplaceable primary source for the intellectual history of the western Islamic world in the 12th–13th centuries.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Reconquista's acceleration and the collapse of Almohad power created an urgency to document the scholarly culture of al-Andalus before its further disruption",
            "The tradition of Andalusian biographical dictionaries (Ibn Bashkuwal, Ibn al-Abbar) provided the scholarly framework that al-Marrakushi extended and completed",
            "His judicial career across multiple Moroccan cities gave him access to local scholarly communities and archival resources essential to his biographical project"
        ],
        "effects": [
            "Al-Dhayl wa-l-Takmila preserved biographical information on approximately 5,000 scholars, making it an irreplaceable source for the history of medieval Andalusian and Maghrebi scholarship",
            "His work enabled modern historians to reconstruct the intellectual networks of western Islamic civilization during the critical transition from Almohad to Marinid rule",
            "The biographical dictionary tradition he continued influenced subsequent Moroccan and Andalusian scholars, contributing to the preservation of Islamic scholarly culture",
            "Many scholars he documented would otherwise be entirely unknown, making his work a unique record of the broader learned class beyond the most prominent figures"
        ],
        "relationships": [
            {"entity": "Almohad Dynasty", "relationship": "BORN_UNDER", "note": "Born in Marrakesh under the Almohad dynasty; his biographical work documented the Almohad scholarly world"},
            {"entity": "Marinid Dynasty", "relationship": "SERVED_UNDER", "note": "Active as a judge and scholar under the Marinid rulers who succeeded the Almohads in Morocco"},
            {"entity": "Ibn Bashkuwal", "relationship": "CONTINUED_WORK_OF", "note": "Al-Dhayl wa-l-Takmila was conceived as a continuation of Ibn Bashkuwal's Kitab al-Sila"},
            {"entity": "Ibn al-Abbar", "relationship": "CONTINUED_WORK_OF", "note": "Also continued and complemented Ibn al-Abbar's Takmila in the biographical dictionary tradition"},
            {"entity": "Al-Andalus", "relationship": "DOCUMENTED", "note": "His biographical dictionary focused on scholars from al-Andalus, preserving their memory during the Reconquista's acceleration"}
        ]
    }),

    # 5 — Stephanos Sahlikis (c. 1331–c. 1391)
    ("stephanos-sahlikis", {
        "summary": (
            "Stephanos Sahlikis (c. 1331–c. 1391) was a Cretan notary, lawyer, and vernacular Greek poet whose satirical "
            "poems — written in the demotic Greek of 14th-century Crete — represent some of the most vivid and personal "
            "literary documents of the Venetian-ruled eastern Mediterranean. Born in Handax (modern Heraklion), he worked "
            "as a notary in the Venetian colonial administration of Crete, combining legal practice with a literary vocation "
            "that produced an unusual body of verse: autobiographical, satirical, moralistic, and darkly humorous accounts "
            "of his own life, including arrest, imprisonment, and the social world of late medieval Crete.\n\n"
            "Sahlikis's most remarkable work is a long poem conventionally called the 'Erotopaegnia' or 'tale of whoring,' "
            "which narrates in vivid detail his experiences with prostitutes and criminals in Handax, including the people "
            "he encountered in prison, the squalor and violence of the city's underworld, and the moral lessons he drew "
            "from these encounters. Combined with other verse narratives about his imprisonment and social disgrace, these "
            "poems constitute an extraordinary document of urban life in a Venetian colonial city — a perspective almost "
            "entirely absent from official records. He also wrote animal fables and moralistic allegories.\n\n"
            "His poetry represents an important early example of vernacular Greek literary production under Venetian "
            "Crete — a tradition that would eventually flower in the magnificent Cretan Renaissance of the 16th–17th "
            "centuries, culminating in Vitsentzos Kornaros's epic romance Erotokritos (c. 1600). Sahlikis's use of "
            "demotic Greek for serious literary purposes, his autobiographical candor, and his satirical engagement "
            "with social reality anticipated the later Cretan literary tradition by two centuries.\n\n"
            "'He wrote as a man who had sat in a Venetian jail and survived it, and gave the demotic Greek language "
            "a literature worthy of its speakers.' Sahlikis remains one of the most original voices in medieval Greek poetry."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Pioneer of vernacular Greek literary production in Venetian Crete; his autobiographical and satirical poems are unique documents of 14th-century colonial urban life and anticipated the Cretan Renaissance by two centuries.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Venetian colonial Crete's multilingual literary environment encouraged Greek vernacular writing as a distinct cultural practice separate from official Latin",
            "The Byzantine demotic Greek literary tradition — particularly the vernacular romances of 14th-century Byzantium — provided Sahlikis with literary models for vernacular verse",
            "His personal experience of imprisonment and social disgrace gave him the autobiographical material and moral urgency that animated his poetry"
        ],
        "effects": [
            "His vernacular Greek poetry established a precedent for serious literary production in demotic Greek in Venetian Crete, anticipating the 16th–17th century Cretan Renaissance",
            "His autobiographical poems preserved firsthand observations of life in Handax's urban underworld — prisons, prostitution, social hierarchies — unavailable from official records",
            "His work contributed to the Cretan literary tradition that would eventually produce Vitsentzos Kornaros's Erotokritos (c. 1600), one of the masterpieces of Greek literature",
            "His use of demotic Greek for satirical and moralistic verse influenced subsequent Cretan poets who balanced vernacular accessibility with literary ambition"
        ],
        "relationships": [
            {"entity": "Republic of Venice", "relationship": "SERVED_UNDER", "note": "Worked as a notary in the Venetian colonial administration of Crete"},
            {"entity": "Cretan Renaissance", "relationship": "ANTICIPATED", "note": "His vernacular Greek literary work anticipated the 16th–17th century Cretan literary Renaissance by two centuries"},
            {"entity": "Vitsentzos Kornaros", "relationship": "ANTICIPATED_WORK_OF", "note": "Sahlikis's vernacular tradition contributed to the literary culture that produced Kornaros's Erotokritos (c. 1600)"},
            {"entity": "Venetian Crete", "relationship": "DOCUMENTED", "note": "His poetry is a unique literary document of urban and social life in colonial Handax (Heraklion)"},
            {"entity": "Byzantine vernacular literature", "relationship": "INFLUENCED_BY", "note": "The Byzantine demotic romance tradition provided models for his vernacular Greek literary practice"}
        ]
    }),

    # 6 — Bahlool / Bahlul Dana (d. c. 800–820 CE)
    ("bahlool", {
        "summary": (
            "Bahlul Dana (Bahlool, d. c. 800–820 CE), given name Wāhab ibn Amr, was an 8th-century Islamic scholar, "
            "judge, and spiritual companion to Imam Musa al-Kadhim (the seventh Imam in Shia Islam) who became "
            "famous across the Islamic world as the archetypal 'wise fool' — a figure whose apparent madness concealed "
            "deep spiritual wisdom and whose satirical sayings cut through the pretensions of caliphal court and "
            "clerical establishment alike. He lived during the reign of the Abbasid Caliph Harun al-Rashid "
            "(786–809 CE), and his encounters with Harun al-Rashid, the caliph's queen Zubaydah, and the jurist Abu "
            "Hanifa are among the most celebrated anecdotes in Islamic adab literature.\n\n"
            "According to tradition, Bahlul was trained as a qadi (judge) but feigned madness to avoid accepting "
            "judicial appointments from the Abbasid court — because accepting would require imposing the caliph's will "
            "rather than God's justice. His 'madness' was thus a form of principled refusal: by acting as a majnun "
            "(divine madman), he secured a social space in which he could speak truth to power without the consequences "
            "that honest criticism would otherwise bring. He reportedly wandered the streets of Baghdad on a stick "
            "horse, visited cemeteries to meditate on mortality, and engaged caliphs, scholars, and beggars with "
            "equally devastating wit.\n\n"
            "His sayings — preserved in Arabic and Persian collections — address themes of justice, mortality, the "
            "vanity of worldly power, hypocrisy of the religious establishment, and the superiority of spiritual "
            "over temporal authority. In Shia tradition, his association with Imam Musa al-Kadhim gave him particular "
            "religious significance as a companion of the Imam who preserved his teachings through the form of "
            "apparent folly. His figure circulated widely in Sufi and folk Islamic literature throughout the "
            "medieval and early modern Islamic world.\n\n"
            "'I prefer the company of graves to the company of courtiers,' he reportedly told Harun al-Rashid, "
            "'for the dead do not flatter.' Bahlul's wisdom through foolishness made him an enduring archetype "
            "of Islamic moral satire."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "The archetypal Islamic 'wise fool' whose sayings and encounters with Harun al-Rashid became foundational texts of Arabic and Persian adab literature, preserving moral criticism of caliphal power in the form of satirical anecdote.",
            "significanceCategory": "regional"
        },
        "causes": [
            "Abbasid caliphal court culture created both the demand for court entertainers and the social space in which a 'divine fool' could speak truth without direct political consequence",
            "Shia tradition's position as a minority under Abbasid rule encouraged indirect, encrypted forms of political and religious critique such as the wise fool persona",
            "Islamic adab literary culture, which valued wit, wisdom, and moral exempla, provided the medium through which Bahlul's sayings were preserved and transmitted"
        ],
        "effects": [
            "Bahlul's sayings and encounters were preserved in Arabic and Persian adab collections, becoming standard material in Islamic moral and satirical literature",
            "His archetype of the 'wise fool' influenced Sufi literature, Persian classical poetry (especially the tradition of the 'majnun' mystic), and Islamic moral narrative across the medieval period",
            "His association with Imam Musa al-Kadhim gave him a specific role in Shia devotional and literary tradition as a companion who preserved the Imam's teachings",
            "The Bahlul figure was transmitted into Ottoman Turkish and Urdu literary traditions, making him one of the most widely disseminated characters in pre-modern Islamic folklore"
        ],
        "relationships": [
            {"entity": "Imam Musa al-Kadhim", "relationship": "COMPANION_OF", "note": "A close companion of the seventh Shia Imam, Musa al-Kadhim, whose teachings he reportedly preserved through his apparent madness"},
            {"entity": "Harun al-Rashid", "relationship": "CONTEMPORARY_OF", "note": "His most famous encounters and witty exchanges were with the Abbasid Caliph Harun al-Rashid"},
            {"entity": "Abu Hanifa", "relationship": "ENGAGED_WITH", "note": "Several famous anecdotes record Bahlul's satirical exchanges with the jurist Abu Hanifa"},
            {"entity": "Sufi literary tradition", "relationship": "INFLUENCED", "note": "The Bahlul archetype of the 'divine fool' who speaks spiritual truth became a model in Sufi literature"},
            {"entity": "Islamic adab literature", "relationship": "TRANSMITTED_THROUGH", "note": "His sayings were preserved and transmitted through the adab collections that constituted medieval Islamic literary culture"}
        ]
    }),

    # 7 — Jan II Carondelet (c. 1469–1544)
    ("jan-ii-carondelet", {
        "summary": (
            "Jean II Carondelet (c. 1469–1544) was a Burgundian Catholic cleric, jurist, statesman, and humanist "
            "intellectual who served as one of the most powerful advisors to Charles V, Holy Roman Emperor, and as "
            "President of the Great Council of Malines and the Council of Flanders — the supreme legal and "
            "administrative bodies of the Habsburg Netherlands. A member of the distinguished Carondelet family of "
            "Burgundian nobility (his brother Ferry de Carondelet was Archbishop of Besançon), he combined legal "
            "training at the University of Louvain with a career at the heart of Habsburg governance.\n\n"
            "Carondelet was a humanist intellectual in close contact with Desiderius Erasmus — he was a patron and "
            "friend of Erasmus, who dedicated several works to him and whose correspondence with Jean II survives as "
            "evidence of their intellectual friendship. He was also the subject of one of the most celebrated portraits "
            "of the Northern Renaissance: the Diptych of Jean de Carondelet (c. 1517) by Jan Gossaert (Mabuse), "
            "in which Carondelet is depicted in a devotional diptych with the Virgin and Child in a style that "
            "combined Italian Renaissance spatial depth with Flemish detailed naturalism.\n\n"
            "As President of the Council of Flanders and a key figure in the legal administration of the Habsburg "
            "Netherlands, Carondelet helped govern one of the most commercially dynamic and legally sophisticated "
            "societies in early 16th-century Europe. He navigated the emergence of Protestant reform in the "
            "Netherlands and the complex jurisdictional negotiations between the Habsburg central authority and "
            "the privileged city-states of the Low Countries. His humanist sympathies and connection to Erasmus "
            "placed him in the reforming Catholic mainstream that sought internal renewal without schism.\n\n"
            "'He governed a world at the hinge of ages — medieval Burgundy becoming Habsburg empire — and did so "
            "with a scholar's precision and a lawyer's caution.' Carondelet's portrait by Gossaert remains one "
            "of the finest images of Renaissance humanism in the north."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Key legal administrator of the Habsburg Netherlands under Charles V; patron and correspondent of Erasmus; subject of Jan Gossaert's Diptych of Jean de Carondelet (c. 1517), one of the finest portraits of the Northern Renaissance.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Burgundian family tradition of legal-ecclesiastical service in the Low Countries provided the social foundation for Carondelet's rapid rise in Habsburg administrative structures",
            "Charles V's consolidation of Habsburg governance in the Netherlands required experienced legal administrators who could navigate the complex jurisdictional landscape of the Low Countries",
            "The Northern humanist culture centered on Erasmus and the Louvain university circle shaped Carondelet's intellectual identity and his role as humanist patron"
        ],
        "effects": [
            "As President of the Great Council of Malines and the Council of Flanders, helped administer one of Europe's most commercially significant and legally complex territories",
            "His patronage of Erasmus contributed to the intellectual culture of reforming Catholicism that characterized the educated Habsburg ruling class in the Netherlands",
            "The Gossaert diptych (c. 1517) commissioned in his honor is one of the masterpieces of early Netherlandish portraiture, documenting the synthesis of Italian and Northern Renaissance art",
            "His legal administration helped navigate the early phases of religious controversy in the Netherlands before the full impact of the Protestant Reformation"
        ],
        "relationships": [
            {"entity": "Charles V, Holy Roman Emperor", "relationship": "SERVED", "note": "Served as one of Charles V's most trusted legal advisors and a President of the Great Council of Malines"},
            {"entity": "Erasmus of Rotterdam", "relationship": "PATRONIZED", "note": "Friend and patron of Erasmus, who dedicated works to him; their correspondence documents a significant intellectual friendship"},
            {"entity": "Jan Gossaert (Mabuse)", "relationship": "DEPICTED_BY", "note": "Subject of Gossaert's Diptych of Jean de Carondelet (c. 1517), one of the masterpieces of Northern Renaissance portraiture"},
            {"entity": "Ferry de Carondelet", "relationship": "BROTHER_OF", "note": "His brother Ferry de Carondelet was Archbishop of Besançon and another important Habsburg diplomat"},
            {"entity": "Great Council of Malines", "relationship": "PRESIDED_OVER", "note": "Served as President of the Great Council of Malines, the supreme court of the Habsburg Netherlands"}
        ]
    }),

    # 8 — Rabghuzi (fl. c. 1310)
    ("rabghuzi", {
        "summary": (
            "Naṣīr al-Dīn ibn Burhān al-Dīn Rabghūzī (fl. c. 1310 CE) was a Turkic-speaking judge and writer "
            "active under the Chagatai Khanate in Central Asia who produced the Qiṣaṣ-i Rabghūzī ('Stories of the "
            "Prophets According to Rabghūzī'), completed in 1310 CE in the Khwarazm region and recognized as the "
            "earliest surviving substantial literary work in the Chagatai Turkish language — the literary ancestor "
            "of modern Uzbek and the dominant written language of Central Asia for five centuries. His work "
            "inaugurated the Chagatai literary tradition that would later include the poetry of Ali-Shir Nava'i "
            "and the memoirs of Babur.\n\n"
            "The Qiṣaṣ-i Rabghūzī is a prose retelling of the stories of Islamic prophets from Adam to Muhammad, "
            "dedicated to a Chagatai official named Nasir Bek. Drawing heavily on the Arabic Qiṣaṣ al-Anbiyā "
            "tradition (especially the work of al-Kisā'ī) and on the Persian prophetic story tradition, Rabghūzī "
            "rendered these materials into Chagatai Turkish in a prose style that balanced religious fidelity with "
            "narrative liveliness. His work includes stories not found in the Quran but widely circulated in "
            "Islamic tradition — legendary accounts of prophets' lives, miracles, and moral exempla.\n\n"
            "His achievement was both linguistic and cultural: by demonstrating that Islamic religious literature "
            "could be rendered in the vernacular Turkic language with the same seriousness previously reserved "
            "for Arabic and Persian, Rabghūzī legitimized Chagatai Turkish as a vehicle for Islamic literary "
            "culture. This opened the path for the extraordinary development of Chagatai literature over the "
            "following two centuries. The Qiṣaṣ-i Rabghūzī was copied and circulated across the Timurid and "
            "early Ottoman worlds and remains a foundational text of Uzbek literary heritage.\n\n"
            "'He turned the holy stories into the language of the steppe and gave the Turkic peoples a literature "
            "of their own.' Rabghūzī's Qiṣaṣ marks the birth of Chagatai Turkish as a literary language."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Author of the Qiṣaṣ-i Rabghūzī (1310), the earliest surviving major literary work in Chagatai Turkish — the linguistic ancestor of modern Uzbek — inaugurating a literary tradition that continued through Ali-Shir Nava'i to Babur.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Chagatai Khanate's Turkic ruling culture created institutional demand for Islamic religious literature in the vernacular Turkic language rather than Arabic or Persian",
            "The Islamic Qiṣaṣ al-Anbiyā tradition — stories of the prophets — provided the religious literary material that Rabghūzī rendered into Chagatai Turkish",
            "Central Asian Islamization under the Mongol successor khanates created a new reading public for Islamic devotional literature in the regional vernacular Turkic"
        ],
        "effects": [
            "The Qiṣaṣ-i Rabghūzī (1310) established Chagatai Turkish as a legitimate vehicle for serious Islamic literary and religious production, inaugurating a major literary tradition",
            "His work opened the path for the development of Chagatai literature that culminated in Ali-Shir Nava'i's poetry in the Timurid period and Babur's memoirs in the 16th century",
            "The text was widely copied and circulated across Central Asia, Timurid Iran, and the early Ottoman world, spreading the Chagatai literary standard",
            "His model of rendering Arabic Islamic religious content into Turkic vernacular influenced subsequent Central Asian religious writers in both Chagatai and related Turkic dialects"
        ],
        "relationships": [
            {"entity": "Chagatai Khanate", "relationship": "SERVED_UNDER", "note": "Served as a judge under the Chagatai Khanate, which ruled Central Asia in the early 14th century"},
            {"entity": "Ali-Shir Nava'i", "relationship": "PRECEDED", "note": "Rabghūzī's Qiṣaṣ inaugurated the Chagatai literary tradition that Nava'i brought to its classical peak in the 15th century"},
            {"entity": "Babur", "relationship": "PRECEDED", "note": "Rabghūzī's tradition contributed to the Chagatai literary culture in which Babur wrote his famous memoirs"},
            {"entity": "Qiṣaṣ al-Anbiyā tradition (al-Kisā'ī)", "relationship": "DREW_FROM", "note": "The Qiṣaṣ-i Rabghūzī was substantially based on the Arabic prophetic stories tradition, especially al-Kisā'ī"},
            {"entity": "Chagatai Turkish literature", "relationship": "FOUNDED", "note": "Recognized as the author of the earliest surviving major literary work in the Chagatai Turkish language"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 13)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
