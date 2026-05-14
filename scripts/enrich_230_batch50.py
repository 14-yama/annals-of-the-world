#!/usr/bin/env python3
"""
Batch 50 — 8 entities: Jacob Roll, Andreas Rogert, Jonas Anton Hielm,
Henrik Anker Bjerregaard, Jacques-Charles Dupont de l'Eure,
Pierre Louis de Lacretelle, Sylvester Jordan, Philo C. Fuller
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

    # 1 — Jacob Roll
    ("jacob-roll", {
        "summary": (
            "Jacob Roll (1776–1831) was a Norwegian "
            "lawyer and politician who served "
            "as President of the Norwegian Storting "
            "(Parliament) in three separate sessions "
            "(1825, 1827, and 1829) — the presiding "
            "officer of the parliamentary chamber "
            "that governed Norway's constitutional "
            "development after the Constitution "
            "of 1814 established the kingdom's "
            "new democratic framework. His "
            "Storting presidencies placed him "
            "at the apex of Norway's parliamentary "
            "life during the formative decade "
            "when the young constitutional "
            "order was being tested against "
            "royal prerogative and union "
            "pressures from Sweden.\n\n"
            "Norway's post-1814 constitutional "
            "history was marked by persistent "
            "tension between the Storting — "
            "which claimed legislative supremacy "
            "under the constitution — and "
            "the Swedish crown, which sought "
            "to limit Norwegian autonomy "
            "within the Kalmar-style union. "
            "The presiding officer of the "
            "Storting was a key institutional "
            "figure in these confrontations, "
            "managing the parliamentary "
            "procedures through which "
            "Norway's constitutional "
            "independence was defended.\n\n"
            "His legal career ran alongside "
            "his parliamentary service — "
            "the combination of legal "
            "expertise and political "
            "engagement that characterized "
            "the Norwegian governing class "
            "emerging after 1814. The new "
            "Norwegian constitutional order "
            "required lawyers who understood "
            "both the constitutional text "
            "and the political dynamics "
            "of the Swedish-Norwegian union.\n\n"
            "His three Storting presidencies "
            "across six years of the 1820s "
            "made him one of the most "
            "prominent parliamentary figures "
            "of the early Norwegian "
            "constitutional period — "
            "a decade crucial for establishing "
            "the practical norms and "
            "precedents of Norwegian "
            "parliamentary governance."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "President of the Norwegian Storting (1825, 1827, 1829) — three sessions in the formative decade of Norwegian constitutional governance; his presidencies coincided with the Storting's persistent assertion of legislative supremacy against Swedish crown prerogative; a leading parliamentary figure of the early Norwegian constitutional order established by the Constitution of 1814.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Norwegian Constitution of 1814 (Grunnloven) — which established Norway's parliamentary system as the foundational document of a new constitutional order — created the Storting as the central institution of Norwegian governance and the Storting presidency as its most visible leadership role",
            "The ongoing tension between the Norwegian Storting and the Swedish crown within the Swedish-Norwegian union (1814–1905) — with the Storting asserting Norwegian constitutional autonomy and the crown seeking to limit it — created the politically charged environment in which the Storting presidency required both legal expertise and political skill",
            "Norway's need for a governing class of legally trained politicians who could operate the new constitutional machinery — combining legal understanding of the 1814 constitution's provisions with the political judgment to navigate the union tensions — created the demand for figures like Roll who bridged legal and parliamentary roles"
        ],
        "effects": [
            "His three Storting presidencies contributed to the consolidation of Norwegian parliamentary practices in the critical first decades after 1814 — establishing the procedural norms and institutional precedents that governed how the Storting operated its constitutional mandate",
            "His leadership of the Storting during the 1820s contributed to the parliamentary dimension of Norway's ongoing constitutional confrontation with Swedish crown prerogative — the period when the Storting was most aggressively asserting its legislative independence",
            "His combined legal and parliamentary career contributed to the formation of Norway's post-1814 governing class — the cohort of lawyers and jurists who staffed the constitutional institutions that the 1814 framework established and whose professional culture shaped Norwegian political development for generations",
            "His prominence as a three-term Storting president contributed to the institutional legitimacy of the Norwegian parliament — demonstrating that the Storting's leadership could be stable, professional, and capable of asserting Norwegian constitutional autonomy against the pressures of the Swedish union"
        ],
        "relationships": [
            {"entity": "Norwegian Storting (Parliament) — President (1825, 1827, 1829)", "relationship": "PRESIDENT_OF", "note": "Served as President of the Norwegian Storting in three sessions (1825, 1827, 1829) — the presiding officer of Norway's parliament during the formative decade of its constitutional development"},
            {"entity": "Norwegian Constitution of 1814 (Grunnloven) / post-1814 constitutional order", "relationship": "PARLIAMENTARY_LEADER_WITHIN", "note": "A leading parliamentary figure operating within the constitutional framework established by Norway's Constitution of 1814 — presiding over the Storting that was the constitution's central institution"},
            {"entity": "Swedish-Norwegian union (1814–1905) / Storting vs. Swedish crown tension", "relationship": "STORTING_PRESIDENT_DURING_CONSTITUTIONAL_TENSIONS", "note": "Led the Storting during the 1820s — the decade of most acute tension between Norwegian parliamentary autonomy and Swedish crown prerogative within the union"},
            {"entity": "Norwegian post-1814 governing class / legal-parliamentary culture", "relationship": "MEMBER_OF", "note": "A member of the Norwegian governing class that combined legal expertise with parliamentary engagement — the cohort of legally trained politicians who staffed Norway's new constitutional institutions"},
            {"entity": "Norwegian constitutional precedent / parliamentary norms (1814–1830s)", "relationship": "CONTRIBUTOR_TO", "note": "Contributed to the establishment of Norwegian parliamentary norms and procedural precedents — his three presidencies helping consolidate the practical governance of the Storting's constitutional mandate"}
        ]
    }),

    # 2 — Andreas Rogert
    ("andreas-rogert", {
        "summary": (
            "Andreas Rogert (1760–1828) was a "
            "Norwegian jurist and politician who "
            "signed the Norwegian Constitution "
            "as a member of the Constitutional "
            "Assembly at Eidsvoll (May 17, 1814) "
            "— making him one of the 112 men "
            "whose signatures on the Grunnloven "
            "established Norway as an independent "
            "constitutional state. The Eidsvoll "
            "Assembly, convened in the spring "
            "of 1814 during the brief window "
            "of Norwegian sovereignty between "
            "Danish cession and Swedish union, "
            "produced one of the world's most "
            "enduring constitutions, still in "
            "force in amended form today.\n\n"
            "The constitutional assembly was "
            "convened in a moment of compressed "
            "political urgency: following "
            "the Treaty of Kiel (January 1814) "
            "by which Denmark ceded Norway "
            "to Sweden, Crown Prince Christian "
            "Frederik convoked a constitutional "
            "assembly to establish Norwegian "
            "sovereignty before Swedish "
            "military pressure could enforce "
            "the cession. The 112 delegates "
            "who met at Eidsvoll from April "
            "to May 1814 drafted a constitution "
            "in seven weeks — one of the "
            "most rapid constitutional "
            "drafting processes in history.\n\n"
            "Rogert's legal expertise "
            "contributed to the assembly's "
            "work — the Eidsvoll delegates "
            "included Norway's leading "
            "lawyers and jurists who "
            "understood constitutional "
            "structures, legal principles, "
            "and the European constitutional "
            "models (particularly the "
            "American and French constitutions) "
            "from which Norway's Grunnloven "
            "drew its inspiration.\n\n"
            "As an Eidsvoll man — "
            "'Eidsvollsmann' in Norwegian "
            "— Rogert joined the company "
            "of figures who are remembered "
            "in Norwegian national memory "
            "as the founders of the modern "
            "Norwegian state."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Signatory of the Norwegian Constitution (May 17, 1814) as a member of the Eidsvoll Constitutional Assembly — one of the 112 Eidsvollsmenn whose signatures created the Grunnloven, still in force today; Norwegian jurist; the Eidsvoll Assembly produced one of the world's most enduring constitutions in seven weeks of deliberation.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Treaty of Kiel (January 1814) by which Denmark ceded Norway to Sweden — and Crown Prince Christian Frederik's convocation of a constitutional assembly to establish Norwegian sovereignty before Swedish military enforcement — created the political urgency that produced the Eidsvoll assembly of which Rogert was a member",
            "Norway's constitutional moment of 1814 — the brief window between Danish cession and Swedish union when Norwegian sovereignty could be asserted — created the extraordinary historical opportunity that the Eidsvoll delegates seized, producing a constitution in seven weeks that has endured for over two centuries",
            "The Norwegian educated class's knowledge of European constitutional models — particularly the American Constitution of 1787 and the French constitutional experiments — gave the Eidsvoll delegates the intellectual resources to draft a sophisticated constitutional document in the compressed time available"
        ],
        "effects": [
            "His signature on the Norwegian Constitution of May 17, 1814 contributed to the founding document of modern Norway — the Grunnloven that has remained Norway's fundamental law (in amended form) for over two centuries, making May 17 Norway's national day",
            "His participation in the Eidsvoll Assembly contributed to the seven-week constitutional drafting process that produced one of the world's most durable constitutional texts — incorporating Enlightenment principles of parliamentary sovereignty, separation of powers, and individual rights into a document tailored to Norwegian conditions",
            "His status as an Eidsvollsmann contributed to the Norwegian national mythology of founding — the 112 signatories of the 1814 constitution occupying a place in Norwegian historical memory comparable to the American Founding Fathers",
            "His legal expertise contributed to the Eidsvoll Assembly's practical capacity to produce a workable constitutional text — the jurists and lawyers among the 112 delegates providing the technical legal knowledge needed to translate the assembly's political principles into durable constitutional language"
        ],
        "relationships": [
            {"entity": "Norwegian Constitution of May 17, 1814 (Grunnloven) — signatory, Eidsvoll Assembly", "relationship": "SIGNATORY_OF", "note": "Signed the Norwegian Constitution (May 17, 1814) as a member of the Eidsvoll Constitutional Assembly — one of the 112 Eidsvollsmenn who created the Grunnloven that remains Norway's fundamental law"},
            {"entity": "Eidsvoll Constitutional Assembly (April–May 1814, 112 delegates)", "relationship": "DELEGATE_TO", "note": "A delegate to the Eidsvoll Constitutional Assembly — the extraordinary body that drafted Norway's constitution in seven weeks during the spring of 1814"},
            {"entity": "Treaty of Kiel (1814) / Crown Prince Christian Frederik / Norwegian sovereignty crisis", "relationship": "CONSTITUTIONAL_RESPONDER_TO", "note": "His constitutional participation responded to the sovereignty crisis created by the Treaty of Kiel — the assembly's work asserting Norwegian independence before Swedish military enforcement of the Danish cession"},
            {"entity": "Norwegian national day (May 17 / Syttende mai) / Norwegian founding mythology", "relationship": "FOUNDING_FIGURE_OF", "note": "One of the Eidsvollsmenn — the 112 constitutional founders who are remembered in Norwegian national memory as the creators of the modern Norwegian state, celebrated on May 17"},
            {"entity": "Norwegian Supreme Court / post-1814 judicial institutions", "relationship": "JURIST_WITHIN", "note": "A Norwegian jurist whose legal expertise contributed to the constitutional drafting process — the legally trained delegates who provided the technical knowledge needed to produce a workable constitutional text"}
        ]
    }),

    # 3 — Jonas Anton Hielm
    ("jonas-anton-hielm", {
        "summary": (
            "Jonas Anton Hielm (1782–1848) was "
            "a Norwegian lawyer and politician "
            "who served as a member of the "
            "Norwegian Storting and contributed "
            "to Norwegian legal development "
            "in the early decades after the "
            "Constitution of 1814. He is "
            "remembered particularly for "
            "his prominent role in the "
            "'adelsdebatt' (nobility debate) "
            "— the Storting's controversy "
            "over the constitutional clause "
            "abolishing inherited noble "
            "privilege in Norway, one of "
            "the most significant class-political "
            "struggles of the early Norwegian "
            "constitutional order.\n\n"
            "The Norwegian Constitution's "
            "Article 23 had abolished the "
            "old Danish-Norwegian nobility "
            "system, but the question of "
            "how to interpret and implement "
            "this abolition — particularly "
            "regarding existing noble families "
            "and their claims to title and "
            "privilege — became a sustained "
            "political controversy in the "
            "Storting of the 1820s. Hielm "
            "was among the Storting members "
            "who advocated a strict, "
            "democratic interpretation "
            "of the nobility abolition.\n\n"
            "His legal career contributed "
            "to the development of Norwegian "
            "law during the transitional "
            "period when Norway was building "
            "its independent legal institutions "
            "— moving from the inherited "
            "Dano-Norwegian legal framework "
            "to a distinctively Norwegian "
            "legal culture consistent with "
            "the 1814 constitutional order. "
            "Norwegian lawyers of his "
            "generation had to adapt "
            "Danish precedents to the "
            "new constitutional framework.\n\n"
            "His combined legal and "
            "parliamentary career exemplified "
            "the integration of professional "
            "legal practice with political "
            "engagement that characterized "
            "the Norwegian governing "
            "class of the early "
            "constitutional period."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "Norwegian lawyer and Storting member; prominent in the 'adelsdebatt' (nobility debate) — the Storting's constitutional controversy over abolishing inherited noble privilege; contributed to Norwegian legal development in the post-1814 constitutional period; his career exemplified the legal-parliamentary integration of Norway's early constitutional governing class.",
            "significanceCategory": "local"
        },
        "causes": [
            "The Norwegian Constitution of 1814's abolition of hereditary noble privilege — Article 23's democratic rejection of the Dano-Norwegian aristocratic system — created the political controversy over implementation that became the 'adelsdebatt', in which Hielm was a prominent voice for strict egalitarian interpretation",
            "Norway's transition from Dano-Norwegian legal heritage to an independent constitutional legal order — requiring lawyers who could adapt inherited legal frameworks to the new constitutional context — created the professional challenge that shaped Hielm's legal career in the early decades after 1814",
            "The Norwegian Storting's position as the primary arena for class-political conflicts in the post-1814 constitutional order — in a society without a strong aristocracy but with significant social stratification between urban professionals, rural farmers, and the administrative class — created the political context in which the nobility debate had broader significance"
        ],
        "effects": [
            "His advocacy in the nobility debate contributed to the Storting's gradual affirmation of a democratic, egalitarian interpretation of the constitutional abolition of noble privilege — one of the class-political dimensions of Norway's post-1814 constitutional development",
            "His legal career contributed to the development of Norwegian jurisprudence in the transitional period — helping to build the body of legal practice and precedent through which Norway adapted inherited Dano-Norwegian law to the requirements of the new constitutional order",
            "His parliamentary service contributed to the Storting's institutional development in the formative decades after 1814 — the period when the practical norms and precedents of Norwegian parliamentary governance were being established",
            "His integrated legal-parliamentary career contributed to the culture of the Norwegian governing class — demonstrating the combination of professional legal expertise and political engagement that characterized the cohort who staffed Norway's early constitutional institutions"
        ],
        "relationships": [
            {"entity": "Norwegian Storting / nobility debate (adelsdebatt, constitutional abolition of noble privilege)", "relationship": "PROMINENT_ADVOCATE_IN", "note": "Prominent in the Storting's 'adelsdebatt' — the constitutional controversy over implementing the abolition of inherited noble privilege, in which Hielm advocated a strict egalitarian interpretation"},
            {"entity": "Norwegian Constitution of 1814 (Grunnloven) / Article 23 nobility abolition", "relationship": "CONSTITUTIONAL_INTERPRETER_OF", "note": "A constitutional interpreter of the 1814 Grunnloven's nobility abolition provisions — contributing to the Storting's political struggle over implementing the constitution's democratic principles"},
            {"entity": "Norwegian legal development / Dano-Norwegian legal heritage transition", "relationship": "CONTRIBUTOR_TO", "note": "Contributed to Norwegian legal development in the post-1814 transitional period — adapting inherited Dano-Norwegian legal frameworks to the requirements of the new constitutional order"},
            {"entity": "Norwegian early constitutional governing class (legal-parliamentary culture)", "relationship": "MEMBER_OF", "note": "A member of Norway's early constitutional governing class — the cohort of legally trained politicians whose integrated professional and political careers shaped the post-1814 Norwegian state"},
            {"entity": "Class politics in early Norwegian constitutional society / Storting democratic culture", "relationship": "VOICE_FOR", "note": "A voice for democratic egalitarianism in the Storting's class-political debates — his nobility debate advocacy representing the democratic wing of Norway's post-1814 political culture"}
        ]
    }),

    # 4 — Henrik Anker Bjerregaard
    ("henrik-anker-bjerregaard", {
        "summary": (
            "Henrik Anker Bjerregaard (1792–1842) "
            "was a Norwegian poet, dramatist, "
            "and judge — born in Christiania "
            "(present-day Oslo) — whose most "
            "enduring creation was the patriotic "
            "poem 'Sønner av Norge' (Sons of Norway, "
            "1820), which became one of the most "
            "beloved songs of Norwegian national "
            "romanticism and remains performed "
            "at patriotic occasions today. "
            "He also wrote the National Theater "
            "prize-winning play 'Til Sæters' "
            "(To the Mountain Pasture, 1825) "
            "and other dramatic and lyric works "
            "that contributed to the flowering "
            "of Norwegian cultural nationalism "
            "in the decades after 1814.\n\n"
            "'Sønner av Norge' — 'Sons of "
            "Norway, a valiant people / "
            "Loyal to our ancient oath / "
            "We will make our country "
            "glorious' — expressed the "
            "patriotic spirit of the "
            "generation that had grown "
            "up with the 1814 constitution "
            "and felt the new Norwegian "
            "national identity with "
            "particular intensity. It "
            "became part of the cultural "
            "repertory of Norwegian "
            "national celebration.\n\n"
            "Bjerregaard's judicial career "
            "ran alongside his literary "
            "production — he served as "
            "a judge in the Norwegian "
            "court system, embodying "
            "the dual professional life "
            "characteristic of educated "
            "Norwegians who combined "
            "legal service with "
            "cultural production in "
            "the early constitutional "
            "period. His legal career "
            "gave him an institutional "
            "position from which to "
            "participate in Norway's "
            "public life.\n\n"
            "His literary work contributed "
            "to the broader Norwegian "
            "national romantic movement "
            "that sought to develop "
            "a distinctively Norwegian "
            "cultural identity — drawing "
            "on folk tradition, landscape, "
            "and patriotic sentiment "
            "to distinguish Norway's "
            "culture from the Danish "
            "tradition that had dominated "
            "the previous centuries."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 6,
            "significanceNarrative": "Norwegian poet, dramatist, and judge; author of 'Sønner av Norge' (1820) — one of the most beloved patriotic songs of Norwegian national romanticism, still performed today; wrote 'Til Sæters' (1825) and other works contributing to Norwegian cultural nationalism after 1814; his literary career expressed the patriotic spirit of the generation that grew up with the Norwegian constitution.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Norwegian Constitution of 1814 and the new Norwegian national identity it generated — combined with the cultural project of developing distinctively Norwegian art, literature, and music to complement the new political independence — created the nationalist cultural movement in which Bjerregaard's patriotic poetry found its audience",
            "The Norwegian national romantic movement's search for cultural expressions that could distinguish Norwegian identity from the Danish tradition that had dominated Norwegian culture for centuries — using folk motifs, landscape, and patriotic sentiment as the raw material for a new national literary tradition — shaped the aesthetic framework of Bjerregaard's poetry",
            "The Swedish-Norwegian union's ambiguous status — Norway's constitutional autonomy maintained but the union with Sweden constraining full independence — created the patriotic cultural energy that made poems like 'Sønner av Norge' emotionally resonant, expressing national pride in a situation of incomplete sovereignty"
        ],
        "effects": [
            "His 'Sønner av Norge' (1820) contributed to Norwegian national romantic culture — becoming one of the most beloved patriotic songs of the post-1814 generation and remaining part of the cultural repertory of Norwegian national celebration into the present day",
            "His dramatic works contributed to the development of Norwegian theater in the early constitutional period — 'Til Sæters' and other plays contributing to a repertory of Norwegian national drama that supported the new country's cultural institutions",
            "His dual career as judge and literary figure contributed to the cultural model of the educated Norwegian professional who combined institutional service with national cultural production — a characteristic pattern of the early constitutional period that gave Norway's cultural movement its institutional grounding",
            "His literary work contributed to Norwegian national romanticism's project of cultural nation-building — the movement that used poetry, drama, folk art, and music to develop a distinctively Norwegian cultural identity that supported and reinforced the political independence established in 1814"
        ],
        "relationships": [
            {"entity": "'Sønner av Norge' (Sons of Norway, 1820) — beloved Norwegian patriotic song", "relationship": "AUTHOR_OF", "note": "Wrote 'Sønner av Norge' (1820) — one of the most beloved patriotic songs of Norwegian national romanticism, expressing the post-1814 generation's national pride and still performed at patriotic occasions"},
            {"entity": "'Til Sæters' (To the Mountain Pasture, 1825) and other dramatic works", "relationship": "AUTHOR_OF", "note": "Wrote 'Til Sæters' (1825) and other dramatic works — contributing to the repertory of Norwegian national theater in the early constitutional period"},
            {"entity": "Norwegian national romanticism / cultural nation-building after 1814", "relationship": "CONTRIBUTOR_TO", "note": "A contributor to Norwegian national romanticism's cultural nation-building project — using patriotic poetry and drama to develop the distinctively Norwegian cultural identity that complemented the 1814 political independence"},
            {"entity": "Norwegian constitutional period (post-1814) / cultural-judicial integration", "relationship": "DUAL_CAREER_FIGURE_OF", "note": "Embodied the dual career pattern of educated early constitutional Norwegians — combining legal judicial service with literary production, characteristic of the post-1814 governing and cultural class"},
            {"entity": "Danish cultural dominance in Norway / Norwegian cultural distinctiveness", "relationship": "CULTURAL_ALTERNATIVE_TO", "note": "A figure of Norwegian cultural distinctiveness — his patriotic poetry contributing to the project of distinguishing Norwegian cultural identity from the Danish tradition that had dominated Norwegian cultural life for centuries"}
        ]
    }),

    # 5 — Jacques-Charles Dupont de l'Eure
    ("jacques-charles-dupont-de-leure", {
        "summary": (
            "Jacques-Charles Dupont de l'Eure "
            "(1767–1855) was a French lawyer "
            "and statesman who achieved the "
            "remarkable distinction of heading "
            "the French Provisional Government "
            "at age 80 in 1848 — his election "
            "as President of the Provisional "
            "Government of February 1848 "
            "representing France's homage "
            "to its oldest and most respected "
            "republican elder statesman. "
            "His career spanned the full "
            "arc of French political history "
            "from the Revolution to the "
            "Second Republic: lawyer before "
            "the Revolution, deputy under "
            "Napoleon, liberal opposition "
            "leader under the Restoration, "
            "Minister of Justice under "
            "Louis-Philippe, and president "
            "of the Provisional Government "
            "at the moment of the July "
            "Monarchy's fall.\n\n"
            "As President of the Chamber "
            "of Deputies under Louis-Philippe "
            "and Minister of Justice "
            "(1830–1831, the first ministry "
            "of the July Monarchy), he was "
            "one of the most senior figures "
            "of French liberalism — "
            "a personal friend of Lafayette "
            "and a consistent voice for "
            "constitutional liberty against "
            "royal prerogative. His longevity "
            "and his consistent liberal "
            "record made him a symbol "
            "of republican continuity.\n\n"
            "The 1848 Provisional Government — "
            "which he chaired at 80, surrounded "
            "by Lamartine, Ledru-Rollin, "
            "and other republican leaders "
            "— declared the Second Republic, "
            "abolished slavery in the "
            "French colonies (a measure "
            "Dupont de l'Eure strongly "
            "supported), and organized "
            "the elections for the "
            "National Constituent Assembly. "
            "His age and reputation "
            "gave the government "
            "its symbolic legitimacy.\n\n"
            "'He is liberty itself' — "
            "Lamartine's characterization "
            "of Dupont de l'Eure captured "
            "his iconic status as the "
            "embodiment of French "
            "liberal constitutionalism "
            "across six decades."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "President of the French Provisional Government (February–May 1848) at age 80; Minister of Justice (1830–1831, first ministry of the July Monarchy); President of the Chamber of Deputies; liberal opposition leader under the Restoration; personal friend of Lafayette; a career spanning the Revolution, Napoleon, Restoration, July Monarchy, and Second Republic; his 1848 Provisional Government abolished slavery in French colonies.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The fall of the July Monarchy (February 1848) and the revolutionary establishment of the Second Republic — the barricades of February 1848 that overthrew Louis-Philippe — created the political moment in which the Provisional Government needed symbolic legitimacy, and Dupont de l'Eure's decades of consistent republican liberalism made him the natural choice as its president at 80",
            "Dupont de l'Eure's extraordinary political longevity — spanning from pre-revolutionary legal practice through Napoleon, the Restoration, and the July Monarchy as a consistent liberal voice — gave him a symbolic authority that no other living French politician possessed: he had been fighting for constitutional liberty since before the Revolution",
            "The 1830 July Revolution that brought Louis-Philippe to power — in which Dupont de l'Eure played a significant role as one of the leading liberal parliamentarians — had already demonstrated his capacity to be a pivotal figure at moments of French political transition, making his 1848 role a pattern he had established earlier"
        ],
        "effects": [
            "His presidency of the French Provisional Government of 1848 contributed to the establishment of the Second French Republic — his symbolic authority lending legitimacy to a revolutionary government that needed to demonstrate its commitment to constitutional order and liberal values rather than radical Jacobinism",
            "The Provisional Government's abolition of slavery in the French colonies (1848) — a measure Dupont de l'Eure supported — contributed to one of the most significant humanitarian acts of 19th-century French governance, freeing hundreds of thousands of enslaved people in the French colonial world",
            "His 60-year career of liberal constitutional advocacy contributed to the continuity of French liberal political culture across the most turbulent period of French history — from the Revolution through Napoleon, the Restoration, the July Monarchy, and the Second Republic",
            "His role as a living symbol of republican continuity — 'liberty itself' in Lamartine's phrase — contributed to the legitimizing ideology of the 1848 revolution, connecting the Second Republic to the liberal constitutional traditions that France had been fighting to establish since 1789"
        ],
        "relationships": [
            {"entity": "President of the French Provisional Government (February–May 1848)", "relationship": "PRESIDENT_OF", "note": "Chaired the French Provisional Government of 1848 at age 80 — the revolutionary body that declared the Second Republic, abolished colonial slavery, and organized elections for the National Constituent Assembly"},
            {"entity": "French Second Republic (1848) / abolition of slavery in French colonies", "relationship": "HEAD_OF_GOVERNMENT_THAT_PROCLAIMED_AND_ABOLISHED", "note": "Led the government that proclaimed the Second French Republic and oversaw the abolition of slavery in the French colonies — one of the most significant humanitarian acts of 19th-century French governance"},
            {"entity": "July Monarchy / Minister of Justice (1830–1831) / President of Chamber of Deputies", "relationship": "MINISTER_AND_CHAMBER_PRESIDENT_UNDER", "note": "Served as Minister of Justice (1830–1831, first ministry of the July Monarchy) and as President of the Chamber of Deputies — among the most senior liberal political figures of the Orleanist regime"},
            {"entity": "Lafayette / French liberal parliamentary opposition (Restoration and July Monarchy)", "relationship": "ALLY_AND_FRIEND_OF", "note": "A personal friend of Lafayette and consistent ally in the liberal parliamentary opposition — his decades of liberal constitutional advocacy making him a symbol of republican continuity"},
            {"entity": "Alphonse de Lamartine / 1848 revolutionary generation ('liberty itself')", "relationship": "SYMBOLIC_ELDER_STATESMAN_FOR", "note": "Called 'liberty itself' by Lamartine — his symbolic authority as France's oldest republican elder statesman giving the 1848 Provisional Government its legitimacy and connecting the Second Republic to six decades of liberal constitutional tradition"}
        ]
    }),

    # 6 — Pierre Louis de Lacretelle
    ("pierre-louis-de-lacretelle", {
        "summary": (
            "Pierre Louis de Lacretelle (1751–1824), "
            "known as Lacretelle l'aîné (the elder) "
            "to distinguish him from his brother, "
            "was a French lawyer, political writer, "
            "and journalist who achieved prominence "
            "before the Revolution as an advocate "
            "at the Metz bar — his eloquent "
            "courtroom pleas and journalistic "
            "writing making him a recognized "
            "figure of the Enlightenment "
            "legal-literary culture — and "
            "contributed to the political "
            "journalism of the Revolutionary "
            "and Napoleonic eras. He was "
            "elected to the Institut de France.\n\n"
            "His pre-Revolutionary legal career "
            "was marked by his advocacy in "
            "politically sensitive cases that "
            "intersected with Enlightenment "
            "reform debates — the Metz bar "
            "was one of the most intellectually "
            "active in France, its advocates "
            "known for writing published "
            "briefs (mémoires judiciaires) "
            "that turned courtroom cases "
            "into public debates about "
            "law, justice, and reform. "
            "His legal writing contributed "
            "to this tradition.\n\n"
            "During the Revolution and "
            "its aftermath, he worked "
            "as a journalist and political "
            "writer — contributing to "
            "the political press that "
            "was one of the Revolution's "
            "most significant institutions. "
            "His brother Jean-Charles-Dominique "
            "de Lacretelle was a historian "
            "and also a member of the "
            "Institut, making the "
            "Lacretelle brothers one "
            "of the notable literary-intellectual "
            "families of the era.\n\n"
            "His combined legal, journalistic, "
            "and political writing career "
            "exemplified the 18th-century "
            "French pattern of the "
            "homme de lettres who moved "
            "between courtroom advocacy, "
            "political journalism, and "
            "literary production — "
            "a career pattern characteristic "
            "of the generation that "
            "bridged the Ancien Régime "
            "and the revolutionary new order."
        ),
        "importanceScore": 6,
        "historicalSignificance": {
            "significanceScore": 5,
            "significanceNarrative": "French lawyer, political writer, and journalist; advocate at the Metz bar (pre-Revolution); member of the Institut de France; political journalist during the Revolutionary and Napoleonic eras; his combined legal-journalistic-literary career exemplified the 18th-century French homme de lettres pattern; brother of historian Jean-Charles-Dominique de Lacretelle, making the Lacretelles one of the notable intellectual families of the era.",
            "significanceCategory": "local"
        },
        "causes": [
            "The Metz bar's tradition of published judicial briefs (mémoires judiciaires) — the practice of turning courtroom cases into public political and legal debates through widely distributed pamphlet-style briefs — created the intellectual environment in which Lacretelle's legal writing served simultaneously as advocacy and Enlightenment reform literature",
            "The Enlightenment's transformation of French intellectual culture — blending legal, philosophical, journalistic, and political writing into the figure of the homme de lettres — created the career model that Lacretelle embodied: a lawyer who was simultaneously an Enlightenment writer and public intellectual",
            "The French Revolution's creation of an unprecedented political press — the explosion of newspapers, pamphlets, and political journals that turned France's political life into a vast public discourse — created the journalistic arena in which Lacretelle's writing career found its Revolutionary-era expression"
        ],
        "effects": [
            "His Metz bar advocacy contributed to the tradition of French judicial eloquence that was one of the Enlightenment era's most significant intellectual genres — published courtroom briefs that functioned as both legal documents and political essays, shaping public opinion on law and justice",
            "His political journalism contributed to the Revolutionary press's role in shaping French political culture — the journalistic writing that translated the Revolution's political debates into public discourse accessible to educated readers",
            "His Institut de France membership contributed to the institutionalization of his intellectual reputation — his election placing him within the formal structure of French learned culture that the Institut represented",
            "His career alongside his brother Jean-Charles-Dominique de Lacretelle contributed to the Lacretelle family's position as one of the notable intellectual families of the transitional generation — the brothers' complementary legal-journalistic and historical careers representing the breadth of the period's intellectual life"
        ],
        "relationships": [
            {"entity": "Metz bar / French judicial eloquence tradition (published mémoires judiciaires)", "relationship": "ADVOCATE_AND_CONTRIBUTOR_TO", "note": "An advocate at the Metz bar — one of France's most intellectually active legal communities, where published courtroom briefs served as both legal documents and Enlightenment reform essays"},
            {"entity": "Institut de France (member)", "relationship": "MEMBER_OF", "note": "Elected to the Institut de France — his membership placing him within the formal structure of French learned culture that the Institut represented"},
            {"entity": "French Revolutionary political press / political journalism", "relationship": "CONTRIBUTOR_TO", "note": "Contributed to the French Revolutionary political press — the journalistic writing that turned the Revolution's debates into public discourse accessible to educated readers"},
            {"entity": "Jean-Charles-Dominique de Lacretelle (brother, historian, also Institut member)", "relationship": "BROTHER_OF", "note": "Brother of historian Jean-Charles-Dominique de Lacretelle — also an Institut member, the Lacretelle brothers representing the intellectual breadth of the period"},
            {"entity": "French Enlightenment homme de lettres tradition / legal-literary culture", "relationship": "EXEMPLAR_OF", "note": "An exemplar of the Enlightenment French homme de lettres — the intellectual who combined legal advocacy, political journalism, and literary production in a career pattern characteristic of the 18th-century transitional generation"}
        ]
    }),

    # 7 — Sylvester Jordan
    ("sylvester-jordan", {
        "summary": (
            "Franz Sylvester Jordan (1792–1861) "
            "was a German lawyer, constitutional "
            "theorist, and liberal politician "
            "from Tirol who became one of the "
            "most significant figures of German "
            "Vormärz constitutional liberalism — "
            "serving as a law professor at the "
            "University of Marburg and contributing "
            "to the drafting of the Kurhessian "
            "constitution (the constitution of "
            "Electoral Hesse, 1831), one of the "
            "most progressive German state "
            "constitutions of the era. His "
            "liberal constitutional advocacy "
            "led to his arrest and prosecution "
            "in 1839 — the period of "
            "Metternich's conservative "
            "reaction — charges from which "
            "he was ultimately acquitted "
            "after years of legal proceedings.\n\n"
            "The Kurhessian constitution of "
            "1831, which Jordan helped draft, "
            "was one of the landmarks of "
            "German liberal constitutionalism "
            "— establishing representative "
            "institutions, civil liberties, "
            "and constitutional limits on "
            "monarchical power in a German "
            "state during the period when "
            "Metternich's Carlsbad Decrees "
            "were suppressing liberal movements "
            "across the German Confederation. "
            "It became a model for reformers "
            "in other German states.\n\n"
            "His persecution under the "
            "reactionary political climate "
            "of the 1830s–1840s — arrested "
            "on charges related to his "
            "constitutional advocacy — "
            "made him a symbol of liberal "
            "martyrdom in the Vormärz era, "
            "the period of simmering "
            "liberal-nationalist pressure "
            "that culminated in the "
            "Revolutions of 1848.\n\n"
            "He participated in the "
            "Frankfurt National Assembly "
            "(1848–1849) — the great "
            "attempt to create a unified "
            "German nation-state through "
            "parliamentary means — "
            "representing the liberal "
            "constitutional tradition "
            "he had championed throughout "
            "his career."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "German Vormärz liberal constitutional theorist; law professor at University of Marburg; co-drafter of the Kurhessian constitution (1831) — one of the most progressive German state constitutions of the era; arrested for liberal advocacy (1839), acquitted after years of proceedings; participant in the Frankfurt National Assembly (1848); his persecution made him a symbol of Vormärz liberal martyrdom.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The post-Napoleonic German constitutional crisis — the tension between the liberal constitutionalism promised by the German princes during the wars against Napoleon and the Metternich conservative reaction represented by the Carlsbad Decrees (1819) — created the political environment in which Jordan's constitutional advocacy was both urgently needed and politically dangerous",
            "The Kurhessian political situation of the early 1830s — which allowed for a relatively progressive constitutional settlement compared to other German states — created the opportunity for Jordan's constitutional expertise to be applied in drafting one of the era's most significant German state constitutions",
            "The Metternich system's identification of liberal constitutional professors as politically dangerous — leading to the 1839 prosecution of Jordan and other German constitutional liberals — created the pattern of liberal martyrdom that Jordan's case exemplified and that built liberal political networks across the German states"
        ],
        "effects": [
            "His contribution to the Kurhessian constitution of 1831 contributed to German liberal constitutionalism — one of the most significant German state constitutional documents of the era, establishing representative institutions and civil liberties that served as a model for reformers elsewhere",
            "His arrest and prosecution contributed to the narrative of liberal martyrdom under Metternich's conservative system — his case becoming part of the Vormärz liberal canon of political persecution that mobilized support for constitutional reform across the German states",
            "His Frankfurt National Assembly participation contributed to the 1848–1849 attempt to create a unified German constitutional state — his presence representing the generation of liberal constitutionalists whose decades of Vormärz advocacy had prepared the intellectual foundations for the revolutionary moment",
            "His Marburg law professorship contributed to the training of a generation of German lawyers in constitutional liberal principles — the academic dimension of his career spreading constitutional ideas through the university system that complemented his political advocacy"
        ],
        "relationships": [
            {"entity": "Kurhessian constitution of 1831 (Electoral Hesse, progressive German state constitution)", "relationship": "CO-DRAFTER_OF", "note": "Helped draft the Kurhessian constitution of 1831 — one of the most progressive German state constitutions of the era, establishing representative institutions and civil liberties in a period of Metternich reaction"},
            {"entity": "University of Marburg law professorship / German constitutional legal education", "relationship": "PROFESSOR_AT", "note": "Taught constitutional law at the University of Marburg — training a generation of German lawyers in liberal constitutional principles through his academic career"},
            {"entity": "Arrest and prosecution (1839) / Metternich conservative reaction / liberal martyrdom", "relationship": "VICTIM_OF", "note": "Arrested for his liberal constitutional advocacy in 1839 — becoming a symbol of liberal martyrdom under Metternich's system, ultimately acquitted after years of proceedings"},
            {"entity": "Frankfurt National Assembly (1848–1849) / German liberal nationalism", "relationship": "DELEGATE_TO", "note": "Participated in the Frankfurt National Assembly (1848–1849) — the great parliamentary attempt to create a unified German nation-state, representing the liberal constitutional tradition he had championed for decades"},
            {"entity": "German Vormärz liberalism / Carlsbad Decrees resistance", "relationship": "LEADING_FIGURE_OF", "note": "A leading figure of German Vormärz liberalism — his constitutional scholarship, drafting contributions, and political persecution making him one of the era's most significant liberal constitutionalists"}
        ]
    }),

    # 8 — Philo C. Fuller
    ("philo-c-fuller", {
        "summary": (
            "Philo Case Fuller (1787–1855) was "
            "a New York lawyer and politician "
            "who served as a US Representative "
            "from New York (1833–1835, "
            "Twenty-third Congress), elected "
            "on the Anti-Masonic ticket "
            "that won significant support "
            "in New York's western counties "
            "following the 1826 Morgan Affair "
            "— the disappearance of William "
            "Morgan after he threatened to "
            "expose Masonic secrets, which "
            "sparked a national political "
            "movement and launched the "
            "Anti-Masonic Party as the "
            "first third party in American "
            "political history. Fuller "
            "practiced law in Genesee "
            "County, New York.\n\n"
            "The Anti-Masonic movement "
            "in New York was particularly "
            "intense in the western "
            "counties — the area of "
            "the Morgan Affair — where "
            "Anti-Masonic candidates "
            "swept local elections and "
            "sent representatives to "
            "Congress. Fuller's "
            "congressional election "
            "represented the western "
            "New York Anti-Masonic "
            "surge at its peak.\n\n"
            "His congressional term "
            "fell in the period when "
            "the Anti-Masonic Party "
            "was transitioning into "
            "the Whig coalition — "
            "the consolidation of "
            "anti-Jacksonian forces "
            "that merged Anti-Masons, "
            "National Republicans, "
            "and other anti-Jackson "
            "elements into the Whig "
            "Party that would contest "
            "the presidency from 1836. "
            "Fuller's own political "
            "transition followed "
            "this pattern.\n\n"
            "His career exemplified "
            "the volatility of the "
            "Jacksonian era's political "
            "landscape — in which "
            "new parties could emerge "
            "rapidly around specific "
            "political triggers, "
            "win congressional "
            "seats, and then dissolve "
            "into broader coalitions "
            "within a decade."
        ),
        "importanceScore": 5,
        "historicalSignificance": {
            "significanceScore": 4,
            "significanceNarrative": "New York Anti-Masonic US Representative (1833–1835, 23rd Congress); Genesee County lawyer; elected on the Anti-Masonic ticket in western New York following the 1826 Morgan Affair that launched American third-party politics; his congressional term fell during the Anti-Masonic Party's transition into the Whig coalition; his career illustrated the Jacksonian era's rapid political party formation and dissolution.",
            "significanceCategory": "local"
        },
        "causes": [
            "The 1826 Morgan Affair — the disappearance and presumed murder of William Morgan in western New York after he threatened to expose Masonic secrets — created the political explosion that launched the Anti-Masonic Party and generated the wave of western New York Anti-Masonic electoral victories that included Fuller's congressional election",
            "Western New York's social and political culture — a region of intense evangelical Protestant religious activism (the 'burned-over district') where the perceived elite privilege of Masonic secrecy resonated with democratic egalitarian values — created the specific regional constituency from which Anti-Masonic political success emerged",
            "The Jacksonian era's dynamic party system — in which anti-Jackson forces were seeking organizational vehicles for opposition and the Anti-Masonic Party offered both a genuine grievance and a political platform — created the opportunity for Anti-Masonic candidates like Fuller to win congressional seats that contributed to the eventual Whig coalition"
        ],
        "effects": [
            "His congressional election contributed to the Anti-Masonic Party's brief but historically significant congressional presence — one of the first third-party movements in American history to win substantial legislative representation and demonstrate that a major new party could challenge the two-party system",
            "His political transition from Anti-Masonic to Whig contributed to the consolidation of the Whig coalition — the pattern of Anti-Masonic politicians merging with National Republicans and other anti-Jacksonians that created the Whig Party as a viable national political organization",
            "His Genesee County legal career contributed to western New York's legal and political development — the professional infrastructure of the rapidly growing region that was transforming from frontier settlement to established agricultural and commercial society",
            "His career exemplified the Anti-Masonic political phenomenon — demonstrating how the Morgan Affair's political energy was channeled into electoral politics, generating congressional representation for the first significant American third-party movement"
        ],
        "relationships": [
            {"entity": "US House of Representatives from New York (1833–1835, 23rd Congress, Anti-Masonic)", "relationship": "REPRESENTATIVE", "note": "Served as US Representative from New York (1833–1835) — elected on the Anti-Masonic ticket in western New York, one of the first third-party movements to achieve substantial congressional representation"},
            {"entity": "Anti-Masonic Party / 1826 Morgan Affair (western New York political context)", "relationship": "CONGRESSIONAL_REPRESENTATIVE_OF", "note": "A congressional representative of the Anti-Masonic political movement — his election driven by the Morgan Affair's political explosion in western New York where Anti-Masonic candidates swept elections"},
            {"entity": "Whig Party coalition (Anti-Masonic transition, 1830s)", "relationship": "TRANSITIONED_TO", "note": "Transitioned from Anti-Masonic to Whig — the political trajectory characteristic of Anti-Masonic politicians who merged into the broader Whig coalition against Jacksonian Democracy"},
            {"entity": "Western New York / Genesee County / 'burned-over district' evangelical culture", "relationship": "LAWYER_AND_REPRESENTATIVE_FROM", "note": "A Genesee County lawyer representing western New York's distinctive political culture — the 'burned-over district' of intense evangelical Protestantism where Anti-Masonic politics found its most fervent support"},
            {"entity": "Jacksonian era third-party politics / American party system development", "relationship": "PARTICIPANT_IN", "note": "A participant in the Jacksonian era's dynamic party system — his career illustrating how new parties could emerge around specific political triggers, win congressional seats, and dissolve into broader coalitions within a decade"}
        ]
    }),
]


if __name__ == "__main__":
    print(f"Enriching {len(ENTITIES)} entities (Batch 50)...")
    for slug, data in ENTITIES:
        enrich_entity(slug, data)
    print("Done.")
