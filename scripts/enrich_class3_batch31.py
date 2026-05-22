#!/usr/bin/env python3
"""
Batch 31 — 8 entities (Class 360): Universities & Learned Academies
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()
FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/360-Class-360"
FILE_PREFIX = "360"


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
    print(f"  ✓ {entity['name']} — sum={slen}c c={len(det.get('causes', []))} e={len(det.get('effects', []))}")


ENTITIES = [

    ("al-azhar-university", {
        "summary": (
            "Al-Azhar University (Jāmiʿat al-Azhar, est. 970–972 CE, Cairo, Egypt — founded by the Fatimid Caliph al-Muizz) is the oldest continuously operating university in the world and the supreme religious authority of Sunni Islam — simultaneously a mosque, a university, and the institution that has defined Islamic theological scholarship for over 1,000 years. Al-Azhar's fatwas (religious rulings) are accepted across the Islamic world as authoritative interpretations of Sunni Islam, and its graduates hold the highest religious offices from Morocco to Indonesia.\n\n"
            "Al-Azhar was founded by the Fatimid Ismaili Shia dynasty as a mosque-university — first intended to spread Ismaili doctrine — but was converted to Sunni learning by Saladin (1171) after he overthrew the Fatimid Caliphate and became the preeminent Sunni religious institution. Al-Azhar's curriculum — traditionally memorisation of the Quran, hadith sciences, Sharia law, Arabic grammar, and classical Islamic philosophy — preserved the classical Islamic scholarly tradition through the Mongol destruction of Baghdad (1258) and the Ottoman conquest of Egypt (1517).\n\n"
            "Al-Azhar's 20th-century modernisation under Nasser (1961 reform) added faculties of medicine, engineering, and science alongside the traditional Islamic sciences, transforming it from a purely religious institution into a comprehensive university with 500,000 students worldwide. Al-Azhar's pronouncements on contemporary issues — terrorism, women's rights, interfaith dialogue — carry enormous weight across the 1.8 billion-strong Sunni Muslim world."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Oldest continuously operating university (est. 970–972 CE); supreme religious authority of Sunni Islam; founded by Fatimid Caliphs; converted to Sunni learning by Saladin (1171); preserved Islamic scholarship through Mongol destruction of Baghdad (1258); 500,000 students worldwide; fatwas authoritative across 1.8 billion Sunni Muslims; 1961 Nasser reform added medicine/engineering/science faculties.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Fatimid Caliphate's founding of Cairo (969 CE) and the establishment of al-Azhar as a mosque-university (970–972 CE) was part of a deliberate strategy to spread Ismaili Shia Islam from a new Egyptian capital that would rival the Abbasid Sunni Caliphate in Baghdad",
            "Saladin's overthrow of the Fatimid Caliphate (1171) and conversion of al-Azhar to Sunni learning was part of his campaign to restore Sunni orthodoxy across the Islamic world — transforming the institution from a Shia mission centre into Sunni Islam's premier scholarly establishment",
            "The Mongol destruction of Baghdad and the Abbasid Caliphate (1258) eliminated the primary rival centre of Islamic learning — leaving al-Azhar as the preeminent surviving institution of Islamic scholarship and endowing it with undisputed authority across the Sunni world"
        ],
        "effects": [
            "Al-Azhar's preservation of the classical Islamic scholarly tradition — through the Mongol invasions, Crusades, Ottoman conquest, French occupation, and British colonialism — makes it the primary custodian of 1,000+ years of continuous Islamic intellectual tradition",
            "Al-Azhar's graduates hold the highest religious offices across the Sunni Islamic world — Grand Muftis, Shaykh al-Islams, Ministers of Religious Affairs — making Al-Azhar the institution that trains Islamic religious leadership for 50+ Muslim-majority countries",
            "Al-Azhar's condemnations of terrorism — including the 2017 Al-Azhar document on renewal of religious discourse — carry authoritative weight across the Sunni world that no other institution can match, making it the primary Islamic voice against extremist interpretations",
            "Al-Azhar's 1961 reform under Nasser — adding secular faculties — created one of the world's largest universities (500,000 students) while preserving the Islamic scholarly core, demonstrating a path for integrating modern education within traditional Islamic institutional frameworks"
        ],
        "relationships": [
            {"entity": "Fatimid Caliphate (Ismaili Shia rulers of Egypt)", "relationship": "FOUNDED_BY_THE", "note": "Al-Azhar was founded by the Fatimid Caliph al-Muizz (970–972 CE) as a mosque-university to spread Ismaili Shia doctrine from Cairo"},
            {"entity": "Saladin (Salah ad-Din Yusuf ibn Ayyub)", "relationship": "CONVERTED_TO_SUNNI_LEARNING_BY", "note": "Saladin's overthrow of the Fatimids (1171) converted al-Azhar to Sunni learning — transforming it into Sunni Islam's supreme scholarly institution"},
            {"entity": "Mongol destruction of Baghdad (1258)", "relationship": "BECAME_PREEMINENT_SURVIVING_ISLAMIC_INSTITUTION_AFTER_THE", "note": "The Mongol destruction of Baghdad eliminated al-Azhar's primary rival — leaving it as the undisputed preeminent institution of Sunni Islamic scholarship"},
            {"entity": "Gamal Abdel Nasser (1961 Al-Azhar reform)", "relationship": "MODERNISED_AND_EXPANDED_BY", "note": "Nasser's 1961 reform added secular faculties (medicine, engineering, science) — transforming Al-Azhar from a purely religious institution into a comprehensive university with 500,000 students"},
            {"entity": "Sunni Islam (1.8 billion believers)", "relationship": "SUPREME_RELIGIOUS_AUTHORITY_FOR", "note": "Al-Azhar's fatwas are authoritative across the 1.8 billion-strong Sunni Muslim world — its pronouncements on terrorism, women's rights, and interfaith dialogue carry global weight"}
        ],
    }),

    ("charles-university", {
        "summary": (
            "Charles University (Universitas Carolina, est. 1348, Prague — founded by Holy Roman Emperor Charles IV) is the oldest university in Central Europe and one of the oldest surviving universities in the world, ranking among the historically significant institutions of European intellectual life. Founded by Emperor Charles IV as the first university in the Holy Roman Empire north of the Alps, Charles University was designed to provide Central Europe with a centre of learning comparable to Paris, Bologna, and Oxford — ending the need for Czech and German scholars to travel to France or Italy for advanced education.\n\n"
            "Charles University was founded with four faculties — theology, law, medicine, and the liberal arts — following the model of the University of Paris, and was given the same privileges as Paris, Bologna, and Salerno by papal bull and imperial charter. The university became the centre of the Hussite reform movement: Jan Hus served as rector (1409–1410) and used his position to promote John Wyclif's reforming theology, igniting the Hussite Wars (1419–1436) that made Bohemia the first territory in Europe to successfully resist Catholic orthodoxy — a century before Luther.\n\n"
            "Charles University's history mirrors Central Europe's turbulent trajectory: flourishing under the Habsburgs, declining during German national conflicts, surviving Nazi occupation (closed 1939–1945), enduring Communist control (1948–1989), and re-emerging as a leading research university after the Velvet Revolution."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Oldest university in Central Europe (est. 1348); first university in Holy Roman Empire north of Alps; founded by Emperor Charles IV; Jan Hus as rector (1409–1410) — Hussite reform movement launched here; Hussite Wars (1419–1436) — first successful resistance to Catholic orthodoxy; closed by Nazis (1939–1945); Communist control (1948–1989); re-emerged after Velvet Revolution (1989).",
            "significanceCategory": "continental"
        },
        "causes": [
            "Emperor Charles IV's ambition to make Prague the cultural and intellectual capital of the Holy Roman Empire — his 'golden era of Czech history' project — drove the founding of a university that would elevate Prague to the rank of Paris and Rome",
            "Central Europe's intellectual dependence on Italian and French universities — requiring Czech, German, and Polish scholars to travel to Bologna, Paris, and Oxford for advanced learning — created the practical demand for a regional university that could serve the Holy Roman Empire's intellectual needs",
            "The papal and imperial charters' grant of the same privileges as Paris (ability to confer degrees, extraterritorial status for students and faculty) gave Charles University immediate legitimacy and attracted students from across the German-speaking world"
        ],
        "effects": [
            "Jan Hus's use of Charles University as the platform for his Hussite reforming theology — and his execution for heresy (1415) despite the Emperor's safe-conduct — triggered the Hussite Wars (1419–1436), making Bohemia the first territory to successfully resist Catholic orthodoxy and establishing the precedent for Luther's Reformation a century later",
            "Charles University's role as the intellectual centre of Czech national consciousness — from Jan Hus through the Czech National Revival of the 19th century to the Prague Spring (1968) and Velvet Revolution (1989) — makes it the primary institutional expression of Czech cultural identity",
            "The 'Kutná Hora Decree' (1409) — in which Charles IV's grandson Wenceslaus IV gave Czech scholars three votes in the university against one for Germans — triggered the mass exodus of German scholars to Leipzig, directly causing the founding of the University of Leipzig (1409)",
            "Charles University's closure by Nazi Germany (1939) — and the execution of student leaders on 17 November 1939 — established 17 November as International Students' Day, commemorated globally as a day of student rights"
        ],
        "relationships": [
            {"entity": "Emperor Charles IV (Holy Roman Emperor)", "relationship": "FOUNDED_BY", "note": "Charles IV founded the university (1348) as part of his programme to make Prague the cultural capital of the Holy Roman Empire"},
            {"entity": "Jan Hus (Hussite reformer, rector 1409–1410)", "relationship": "PLATFORM_FOR_THE_REFORMING_MOVEMENT_OF", "note": "Jan Hus used his position as Charles University rector to promote Wyclif's theology — launching the Hussite movement and the first successful resistance to Catholic orthodoxy"},
            {"entity": "Hussite Wars (1419–1436)", "relationship": "INTELLECTUAL_INCUBATOR_OF_THE_MOVEMENT_THAT_TRIGGERED_THE", "note": "The Hussite movement — launched from Charles University — triggered the Hussite Wars, making Bohemia the first territory to resist Catholic orthodoxy"},
            {"entity": "University of Leipzig (est. 1409)", "relationship": "GERMAN_SCHOLARS' EXODUS LEADS TO FOUNDING OF THE", "note": "The Kutná Hora Decree (1409) giving Czech scholars voting advantage triggered the German scholars' exodus that directly caused the founding of Leipzig University"},
            {"entity": "Velvet Revolution (1989)", "relationship": "INSTITUTIONAL_VOICE_OF_CZECH_INTELLECTUAL_RESISTANCE_THROUGH_TO_THE", "note": "Charles University's role in Czech national consciousness — from Hus through the Prague Spring to the Velvet Revolution — makes it the primary institution of Czech cultural identity"}
        ],
    }),

    ("tartu-university", {
        "summary": (
            "The University of Tartu (est. 1632, Tartu, Estonia — founded by Swedish King Gustavus Adolphus as Academia Gustaviana) is the national university of Estonia and the oldest continuously operating university in the Baltic region — a key institution in Baltic intellectual and national identity, and the spiritual home of the Estonian national awakening of the 19th century. Founded during the Swedish Empire's period of Baltic domination, Tartu became the primary university of Baltic intellectual life under Swedish, Russian, and ultimately Estonian rule.\n\n"
            "The university was founded by Gustavus Adolphus of Sweden (1632) — who expanded Swedish power across the Baltic and sought to bring Lutheran Reformation education to his new Baltic territories. Tartu operated intermittently under Swedish rule, was refounded by Russian Tsar Alexander I (1802) as a German-language university, and became the intellectual centre of the 19th-century Baltic German scholarly tradition — home to Karl Ernst von Baer (who discovered the mammalian ovum), Georg Friedrich Bernhard Riemann (studied here), and Wilhelm Ostwald (chemist, Nobel 1909).\n\n"
            "Tartu's most politically significant period was the 19th-century Estonian national awakening: the university's German-language faculty indirectly stimulated Estonian-language scholarship by training the Baltic German philologists who first systematically studied Estonian — and Estonian students at Tartu became the leaders of the national awakening that ultimately produced independent Estonia."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "National university of Estonia and oldest Baltic university (est. 1632); founded by Gustavus Adolphus of Sweden; refounded by Alexander I (1802) as German-language university; Karl Ernst von Baer discovered mammalian ovum here; Wilhelm Ostwald (Nobel 1909); 19th-century Estonian national awakening incubated at Tartu; intellectual home of Baltic intellectual tradition under Swedish, Russian, and Estonian rule.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Swedish King Gustavus Adolphus's programme to bring Lutheran Reformation education to Swedish-controlled Baltic territories — part of his broader strategy of building a Baltic empire centred on evangelical Christianity — drove the founding of Academia Gustaviana (1632)",
            "Russian Tsar Alexander I's 1802 refounding of Tartu as a German-language Baltic university was part of his Enlightenment-era programme of educational modernisation — and his strategy of using Baltic German elites as loyal administrators of the Russian Empire's western borderlands",
            "The Baltic German scholarly tradition — which made Tartu a centre of 19th-century natural science, philology, and law — created an institutional environment where Estonian-language scholars could emerge and ultimately lead the national awakening"
        ],
        "effects": [
            "Karl Ernst von Baer's discovery of the mammalian ovum at Tartu (1827) — establishing the cell theory of reproduction — was one of the most significant biological discoveries of the 19th century, establishing Tartu as a world-class research institution",
            "Tartu's role as the intellectual incubator of Estonian national consciousness — through the Estonian Students' Society (1870) and Estonian-language scholarship — made it the spiritual home of the national awakening that produced Estonian independence (1918)",
            "The Tartu Peace Treaty (1920) — signed at the University of Tartu between Soviet Russia and the newly independent Republic of Estonia — was the diplomatic instrument of Estonian independence, making the university the site of the most significant moment in Estonian national history",
            "During the Soviet period, Tartu's Semiotics School — led by Yuri Lotman — became one of the most influential intellectual movements in 20th-century humanities, with Lotman's semiosphere theory shaping cultural studies worldwide"
        ],
        "relationships": [
            {"entity": "Gustavus Adolphus of Sweden (founding patron)", "relationship": "FOUNDED_AS_ACADEMIA_GUSTAVIANA_BY", "note": "Gustavus Adolphus founded the university (1632) as part of Sweden's Baltic empire-building and Lutheran educational programme"},
            {"entity": "Karl Ernst von Baer (biologist, ovum discovery)", "relationship": "SITE_OF_THE_DISCOVERY_OF_THE_MAMMALIAN_OVUM_BY", "note": "Von Baer's discovery of the mammalian ovum at Tartu (1827) established the university as a world-class research institution"},
            {"entity": "Estonian national awakening (19th century)", "relationship": "INTELLECTUAL_INCUBATOR_OF_THE", "note": "Tartu's Estonian Students' Society (1870) and Baltic German philologists trained there became the leaders of the Estonian national awakening"},
            {"entity": "Tartu Peace Treaty (1920)", "relationship": "NAMESAKE_SITE_OF_THE", "note": "The Tartu Peace Treaty (1920) — establishing Estonian independence from Soviet Russia — was signed at the university, making it the site of Estonia's founding moment"},
            {"entity": "Yuri Lotman and Tartu-Moscow Semiotic School", "relationship": "HOME_OF_THE_GLOBALLY_INFLUENTIAL", "note": "Lotman's semiosphere theory — developed at Tartu — shaped 20th-century cultural studies worldwide"}
        ],
    }),

    ("vilnius-university", {
        "summary": (
            "Vilnius University (Vilniaus universitetas, est. 1579, Vilnius — founded by Jesuit Order with royal charter from King Stephen Báthory of Poland-Lithuania) is the oldest university in the Baltic states and one of the oldest in Northern Europe — the primary institution of Lithuanian intellectual and national identity, and historically the most important centre of learning in the Polish-Lithuanian Commonwealth. Its founding by the Jesuits made it a key institution of the Counter-Reformation in Eastern Europe.\n\n"
            "Vilnius University was founded by the Society of Jesus (Jesuits) as a college in 1569 and elevated to university status by royal charter (1579) from Stephen Báthory — the Polish-Lithuanian king who used the Jesuits as an instrument of Catholic reconquest against Lithuanian Protestantism and Russian Orthodoxy. For two centuries, Vilnius University was the primary institution of learning for the Polish-Lithuanian Commonwealth's multi-confessional intellectual elite, training scholars, clergy, and statesmen across a vast territory from the Baltic to the Black Sea.\n\n"
            "Vilnius University's modern importance is as the intellectual centre of Lithuanian national consciousness: closed by Tsarist Russia (1832) after the November Uprising, reopened in 1919, closed by Soviet occupation (1939–1943), and re-emerging after Lithuania's independence (1990). Its astronomical observatory (est. 1753) — one of the oldest in Eastern Europe — and its historic baroque library represent one of the great architectural and scholarly ensembles of the region."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Oldest Baltic university (est. 1579); Jesuit-founded Counter-Reformation instrument; royal charter from Stephen Báthory; primary institution of Polish-Lithuanian Commonwealth; closed by Tsarist Russia (1832) after November Uprising; reopened 1919; closed by Soviet occupation (1939–1943); re-emerged after Lithuanian independence (1990); astronomical observatory (1753) — oldest in Eastern Europe; baroque library ensemble.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Jesuit Order's Counter-Reformation strategy in Eastern Europe — using universities as instruments of Catholic intellectual reconquest against Protestant Reformation movements and Russian Orthodoxy — drove the founding of Vilnius College (1569) and its elevation to university status (1579)",
            "Stephen Báthory's political need for an institution that could train Catholic clergy, lawyers, and administrators for the vast Polish-Lithuanian Commonwealth — and his use of the Jesuits as cultural shock-troops of the Counter-Reformation — drove the royal charter and endowment of the university",
            "Lithuania's position on the cultural frontier between Catholic Western Europe and Orthodox Eastern Europe — and the Reformation's strong presence in Lithuanian noble families — created the intellectual battlefield context that made the Jesuit university both politically urgent and intellectually significant"
        ],
        "effects": [
            "Vilnius University's Jesuit curriculum — combining classical humanism with Catholic theology and Counter-Reformation apologetics — trained the intellectual elite of the Polish-Lithuanian Commonwealth for two centuries, shaping the cultural and religious landscape of Eastern Europe",
            "The Tsarist closure of Vilnius University (1832) — following the November Uprising — was part of Russia's systematic policy of cultural suppression of Polish-Lithuanian culture, accelerating the Lithuanian national awakening by making Vilnius's intellectual tradition a site of resistance",
            "Vilnius University's astronomical observatory (1753) — one of the oldest in Eastern Europe, with a continuous tradition of astronomical observation — made Vilnius a centre of Enlightenment science in the Commonwealth and trained a succession of significant astronomers",
            "The reopening of Vilnius University as a Lithuanian-language institution (1919) — and its role in training the leaders of independent Lithuania — made it the primary institution of Lithuanian national statehood, linking the 16th-century Commonwealth tradition to modern Lithuanian independence"
        ],
        "relationships": [
            {"entity": "Society of Jesus (Jesuits)", "relationship": "FOUNDED_AND_ADMINISTERED_INITIALLY_BY_THE", "note": "The Jesuits founded Vilnius College (1569) and received the university charter (1579) — making it a key Jesuit Counter-Reformation educational institution"},
            {"entity": "Stephen Báthory (King of Poland-Lithuania)", "relationship": "ROYAL_CHARTER_GRANTED_BY", "note": "Stephen Báthory granted the royal charter elevating Vilnius College to university status (1579) — using the Jesuits as instruments of Catholic intellectual reconquest"},
            {"entity": "Polish-Lithuanian Commonwealth", "relationship": "PRIMARY_INTELLECTUAL_INSTITUTION_OF_THE", "note": "For two centuries, Vilnius University was the primary centre of learning for the Polish-Lithuanian Commonwealth's multi-confessional intellectual elite"},
            {"entity": "Tsarist Russia (closure 1832)", "relationship": "CLOSED_BY_AS_ACT_OF_CULTURAL_SUPPRESSION_BY", "note": "Russia closed Vilnius University (1832) after the November Uprising — part of systematic suppression of Polish-Lithuanian culture"},
            {"entity": "Lithuanian independence (1990)", "relationship": "RE-EMERGED_AS_PRIMARY_NATIONAL_INSTITUTION_AFTER_THE", "note": "Vilnius University's reopening after Lithuanian independence (1990) represented the revival of Lithuania's intellectual tradition after Soviet occupation"}
        ],
    }),

    ("thammasat-university", {
        "summary": (
            "Thammasat University (มหาวิทยาลัยธรรมศาสตร์, est. 1934, Bangkok, Thailand — founded by Pridi Phanomyong) is Thailand's premier institution of law, political science, and social sciences — founded as the 'University of Moral Sciences' by Pridi Phanomyong, one of the democratic revolutionaries who ended absolute monarchy in Thailand in 1932. Thammasat's founding as an open-access university for democracy distinguishes it from the royalist Chulalongkorn University — a distinction that has made it the intellectual centre of Thai democratic politics for 90 years.\n\n"
            "Pridi Phanomyong founded Thammasat (1934) as a university open to all citizens — modelled on the French democratic ideal of the open university — with the explicit mission of training citizens for democratic governance. Its original name ('University of Moral Sciences') and its admission policy (anyone could enrol, regardless of prior education) embodied the democratic revolution's ideals. Pridi himself became a legendary figure: a democrat, anti-Japanese resistance leader, and Prime Minister who was later forced into exile by conservative royalist forces.\n\n"
            "Thammasat's history is inseparable from Thai democratic struggles: the 14 October 1973 uprising (students overflowed from Thammasat onto Ratchadamnoen Avenue, toppling the military dictatorship), the 6 October 1976 massacre (right-wing paramilitary groups killed students inside the Thammasat campus — one of the darkest events in modern Thai history), and the 1992 Black May protests all centre on Thammasat."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Thailand's premier law and political science university (est. 1934); founded by Pridi Phanomyong — democratic revolutionary who ended absolute monarchy; 'University of Moral Sciences' — open to all citizens; intellectual centre of Thai democratic politics; 14 October 1973 uprising (toppled military dictatorship) originated here; 6 October 1976 massacre (right-wing paramilitary killed students on campus — darkest event in modern Thai history); 1992 Black May protests.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The 1932 Siamese Revolution — ending the absolute monarchy of Rama VII and establishing a constitutional monarchy — created the political environment that allowed Pridi Phanomyong to found a democratic university explicitly committed to training citizens for self-governance",
            "Pridi's vision of Thai democracy — modelled on French republican ideals — drove the founding of an open-access university that would give common citizens access to legal and political education, challenging the elite educational monopoly of Chulalongkorn University",
            "The absence of a Thai institution capable of training democratic public servants, lawyers, and politicians in the new constitutional system created the practical demand for a university of 'moral sciences' (law, politics, economics) for the new constitutional order"
        ],
        "effects": [
            "Thammasat's role as the intellectual centre of Thai democratic politics — producing generations of lawyers, politicians, civil society leaders, and activists — has made it the primary institutional expression of Thai democratic aspirations, in permanent tension with military and royalist power",
            "The 14 October 1973 uprising — when Thammasat students led the popular movement that toppled the Thanom Kittikachorn military dictatorship — was the most significant democratic victory in Thai history, making Thammasat the site of Thailand's democratic breakthrough",
            "The 6 October 1976 massacre — when right-wing paramilitaries lynched and burned students inside the Thammasat campus in one of the most horrifying acts of political violence in Southeast Asian history — became the defining trauma of Thai democratic politics, shaping a generation of activists who went to the jungle to join the Communist Party of Thailand",
            "Pridi Phanomyong's legacy at Thammasat — his founding vision of open, democratic education — has made the university the primary site of Thai democratic memory and the institutional counter-weight to royalist and military power in Thai political culture"
        ],
        "relationships": [
            {"entity": "Pridi Phanomyong (founding figure)", "relationship": "FOUNDED_BY", "note": "Pridi Phanomyong — democratic revolutionary, anti-Japanese resistance leader, and Prime Minister — founded Thammasat (1934) as Thailand's democratic university"},
            {"entity": "1932 Siamese Revolution (ending absolute monarchy)", "relationship": "FOUNDED_IN_DEMOCRATIC_CONTEXT_OF_THE", "note": "Thammasat was founded two years after the 1932 revolution that ended absolute monarchy — embodying the democratic revolution's educational ideals"},
            {"entity": "14 October 1973 uprising (toppling military dictatorship)", "relationship": "SITE_AND_INSTITUTIONAL_INCUBATOR_OF_THE", "note": "The 1973 uprising — which toppled the Thanom military dictatorship — originated at Thammasat, making the university Thailand's democratic breakthrough site"},
            {"entity": "6 October 1976 massacre", "relationship": "SITE_OF_THE_DARKEST_EVENT_IN_MODERN_THAI_HISTORY", "note": "Right-wing paramilitaries killed students inside the Thammasat campus on 6 October 1976 — one of the most horrifying acts of political violence in Southeast Asian history"},
            {"entity": "Chulalongkorn University (royalist institution)", "relationship": "DEMOCRATIC_COUNTERPART_AND_RIVAL_OF", "note": "Thammasat's democratic, open-access ethos distinguishes it from the royalist Chulalongkorn University — a distinction that has structured Thai political culture"}
        ],
    }),

    ("zaytouna-university", {
        "summary": (
            "The University of Ez-Zitouna (Jāmiʿat al-Zaytūna, est. 737 CE, Tunis, Tunisia — founded as the Great Mosque of Tunis; university functions from the 8th century) is one of the oldest universities in the Islamic world and historically the most important centre of Islamic learning in North Africa and the Maghreb — training generations of Muslim scholars, theologians, and jurists who shaped Maliki jurisprudence across the Islamic West (al-Andalus, Morocco, Tunisia, Algeria, Libya, and sub-Saharan West Africa).\n\n"
            "Ez-Zitouna ('the Olive Tree mosque') was founded in 737 CE and developed Islamic university functions from the 8th century — teaching Quran, hadith sciences, Maliki fiqh (jurisprudence), Arabic grammar, and the Islamic sciences in the traditional mosque-university format predating the European university. The theologian Ibn Khaldun — the founder of the philosophy of history and sociology — studied at Ez-Zitouna, as did generations of North African and sub-Saharan scholars who carried Maliki legal thought across the Islamic world.\n\n"
            "Ez-Zitouna was secularised and marginalised by Tunisia's post-independence president Habib Bourguiba (1958) — who dismantled its traditional curriculum in favour of a French-model state education system — but it was revived under various names and now exists as the University of Ez-Zitouna, specialising in Islamic sciences. Its historical significance as the Maghreb's al-Azhar — and its role in shaping Maliki Islam across North and West Africa — makes it one of the formative institutions of Islamic intellectual history."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "One of the oldest universities in the Islamic world (est. 737 CE); most important centre of Islamic learning in North Africa and Maghreb; Ibn Khaldun (founder of sociology/philosophy of history) studied here; shaped Maliki jurisprudence across al-Andalus, Morocco, Tunisia, Algeria, Libya, sub-Saharan West Africa; secularised by Bourguiba (1958); revived as University of Ez-Zitouna; 'Maghreb's al-Azhar'.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Arab conquest of North Africa (7th century) and the establishment of Tunis as a major city of the Maghreb created the need for a centre of Islamic learning that could train the scholars and jurists necessary to administer and teach the expanding Muslim community",
            "The Maliki school of jurisprudence's strong presence in North Africa — and the need for a regional centre of Maliki legal education — drove Ez-Zitouna's development as the premier institution of Maliki fiqh training in the Islamic West",
            "The Aghlabid and later Hafsid dynasties' patronage of Ez-Zitouna as a prestige institution of their rule — providing endowments, appointing senior scholars, and sending their sons there — drove its growth into the Maghreb's preeminent scholarly institution"
        ],
        "effects": [
            "Ibn Khaldun's education at Ez-Zitouna — and his use of the Maghrebi scholarly tradition in developing his theory of history (the Muqaddimah, 1377) — gave Ez-Zitouna an indirect foundational role in the development of sociology, historiography, and the philosophy of history",
            "Ez-Zitouna's training of Maliki scholars who spread across al-Andalus, Morocco, and sub-Saharan West Africa established Maliki jurisprudence as the dominant legal school of the Islamic West — shaping the legal cultures of 10+ Muslim-majority countries",
            "Bourguiba's secularisation and marginalisation of Ez-Zitouna (1958) — replacing it with French-model state education — created the cultural disconnect between modern Tunisian elites and traditional Islamic learning that many historians have linked to the vulnerability of Tunisian society to Salafi extremism in the 2000s-2010s",
            "Ez-Zitouna's revival after the Arab Spring and its continued role as a centre of Maliki Islamic education has made it a focal point of debates about the relationship between Islamic tradition and democratic governance in post-revolutionary Tunisia"
        ],
        "relationships": [
            {"entity": "Ibn Khaldun (founder of sociology and philosophy of history)", "relationship": "EDUCATED_THE_FORMATIVE_MIND_OF", "note": "Ibn Khaldun studied at Ez-Zitouna — where the Maghrebi scholarly tradition shaped the intellectual framework he used to develop the Muqaddimah (1377)"},
            {"entity": "Maliki jurisprudence (dominant legal school of Islamic West)", "relationship": "PRIMARY_INSTITUTION_FOR_TRAINING_IN", "note": "Ez-Zitouna's training of Maliki scholars established Maliki fiqh as the dominant legal school across the Islamic West — al-Andalus, Morocco, Tunisia, Algeria, West Africa"},
            {"entity": "Al-Azhar University (Cairo)", "relationship": "NORTH_AFRICAN_COUNTERPART_AND_HISTORICAL_PARALLEL_TO", "note": "Ez-Zitouna is the 'Maghreb's al-Azhar' — the equivalent mosque-university tradition in North Africa to al-Azhar's role in Egypt and the Mashriq"},
            {"entity": "Habib Bourguiba (Tunisian president, secularisation 1958)", "relationship": "SECULARISED_AND_MARGINALISED_BY", "note": "Bourguiba's 1958 educational reforms dismantled Ez-Zitouna's traditional curriculum — replacing it with French-model state education in his modernisation programme"},
            {"entity": "Arab Spring and post-revolutionary Tunisia (2011)", "relationship": "REVIVAL_CONTESTED_IN_CONTEXT_OF_THE", "note": "Ez-Zitouna's post-Arab Spring revival has made it a focal point of debates about Islamic tradition and democratic governance in Tunisia"}
        ],
    }),

    ("swedish-academy", {
        "summary": (
            "The Swedish Academy (Svenska Akademien, est. 1786, Stockholm — founded by King Gustav III) is the learned society that awards the Nobel Prize in Literature — the world's most prestigious literary prize — and is therefore the single most powerful institution in global literary recognition. Founded with 18 members (a number that never changes) to cultivate 'purity, vigour, and majesty' of the Swedish language, the Academy's 232-year tradition of awarding the Nobel Prize makes it the supreme arbiter of world literary achievement.\n\n"
            "Gustav III founded the Swedish Academy in 1786, explicitly modelling it on the Académie française (established 1635) as part of his programme of Swedish cultural nationalisation during the Gustavian Enlightenment. The Academy was charged with producing a Swedish dictionary, a Swedish grammar, and maintaining the standards of the Swedish language — but its primary lasting significance has been the award of the Nobel Prize in Literature, which it has given annually (with interruptions) since 1901, selecting from every language and literary tradition worldwide.\n\n"
            "The Academy's 2018 sexual harassment scandal — in which accusations against a member's husband Jean-Claude Arnault created an internal crisis that caused seven members to resign and the Academy to postpone the 2018 Nobel Prize in Literature (awarded retrospectively in 2019) — was the most serious institutional crisis in its history, prompting a reform of its statutes that for the first time allowed members to resign."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Awards the Nobel Prize in Literature — world's most prestigious literary prize (since 1901); founded by Gustav III (1786) modelled on Académie française; 18 permanent members (number never changes); supreme arbiter of world literary achievement; 2018 sexual harassment scandal — seven members resigned, 2018 Nobel postponed (first postponement since WWII); statutes reformed to allow member resignation for first time.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Gustav III's Gustavian Enlightenment programme — his determination to elevate Sweden to cultural parity with France and create a Swedish national literary identity — drove the founding of the Swedish Academy (1786) modelled explicitly on the Académie française",
            "Alfred Nobel's will (1895) — specifying that the prize for literature should be awarded by 'the Academy in Stockholm' — gave the Swedish Academy its global significance, transforming a Swedish language institution into the supreme arbiter of world literature",
            "The Swedish Academy's independence from government control — guaranteed by its royal charter — made it an acceptable choice for Nobel's prize mechanism: Nobel wanted an independent institution, not a government-controlled one"
        ],
        "effects": [
            "The Nobel Prize in Literature — awarded annually by the Swedish Academy since 1901 — is the world's most powerful literary recognition: a Nobel Prize transforms a writer's global reach, translation into dozens of languages, and permanent place in the world literary canon",
            "The Swedish Academy's selections have shaped the world literary canon: its choices (Yeats, Faulkner, Camus, García Márquez, Toni Morrison, Mo Yan, Herta Müller, Peter Handke) have defined which writers are considered the greatest of their generation and which literary traditions are globally recognised",
            "The Academy's controversial omissions — never awarding Tolstoy, Ibsen, Proust, Joyce, Kafka, Borges, Nabokov, or Chekhov — have generated as much literary debate as its awards, establishing the Nobel selection process as the world's most discussed literary judgment",
            "The 2018 scandal and reform — forcing the first change to the Academy's statutes in 232 years — demonstrated that even the most prestigious and tradition-bound institutions face accountability for misconduct, and produced a restructured Academy more open to external scrutiny"
        ],
        "relationships": [
            {"entity": "Nobel Prize in Literature (annual, since 1901)", "relationship": "AWARDS_THE", "note": "The Swedish Academy awards the Nobel Prize in Literature — the world's most prestigious literary prize — making it the supreme arbiter of world literary achievement"},
            {"entity": "Alfred Nobel (will, 1895)", "relationship": "DESIGNATED_AS_PRIZE-AWARDING_INSTITUTION_BY", "note": "Alfred Nobel's will designated 'the Academy in Stockholm' to award the literature prize — giving the Swedish Academy its global significance"},
            {"entity": "Académie française (1635)", "relationship": "MODELLED_ON_THE", "note": "Gustav III founded the Swedish Academy (1786) explicitly modelling it on the Académie française — as part of the Gustavian Enlightenment programme"},
            {"entity": "Gustav III of Sweden (founding patron)", "relationship": "FOUNDED_BY", "note": "Gustav III founded the Swedish Academy (1786) as part of his programme of Swedish cultural nationalisation and Gustavian Enlightenment"},
            {"entity": "2018 Nobel Prize in Literature postponement", "relationship": "POSTPONED_THE_FIRST_TIME_SINCE_WWII_DUE_TO_INTERNAL_CRISIS_OF_THE", "note": "The 2018 sexual harassment scandal caused seven resignations and the postponement of the 2018 Nobel Prize — the first postponement since World War II"}
        ],
    }),

    ("founding-of-krak\u00f3w-university", {
        "summary": (
            "The Jagiellonian University (Universitas Iagellonica, est. 1364, Kraków, Poland — founded by King Casimir III 'the Great') is the oldest university in Poland and one of the oldest continuously operating universities in the world, ranking as the preeminent institution of Polish intellectual and scientific life. Founded by Casimir the Great — the king who 'found Poland built of wood and left it built of stone' — the Jagiellonian University was the first university in Central-Eastern Europe after Prague (1348), created to provide Poland with trained administrators, lawyers, and clergy.\n\n"
            "The Jagiellonian University is most famous as the alma mater of Nicolaus Copernicus (studied here c.1491–1495), whose heliocentric theory — developed at Frombork and published in De revolutionibus orbium coelestium (1543) — initiated the Scientific Revolution. Copernicus's connection to Kraków and the Jagiellonian University makes it one of the most historically significant alumni connections in the history of science. The university is also the alma mater of Pope John Paul II (Karol Wojtyła, studied theology here 1945–1946).\n\n"
            "The Jagiellonian University's history mirrors Poland's turbulent national trajectory: closed and reorganised under Habsburg and Prussian influence, surviving the Partitions, the Nazi occupation (November 1939 — Sonderaktion Krakau, when the Nazis arrested 183 professors in a lecture hall), Communist control, and re-emerging as a leading European research university after 1989."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Oldest university in Poland (est. 1364); one of oldest continuously operating universities in world; founded by Casimir III the Great; alma mater of Copernicus (studied c.1491–1495) — who initiated the Scientific Revolution; alma mater of Pope John Paul II; Sonderaktion Krakau — Nazis arrested 183 professors in lecture hall (1939); survived Partitions, Nazi occupation, Communist control; re-emerged as leading European university post-1989.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "King Casimir III the Great's ambition to provide Poland with trained lawyers, administrators, and clergy — and his determination to prevent Polish scholars from needing to study at Prague or Paris — drove the founding petition to Pope Urban V for a university at Kraków (1364)",
            "The Jagiellonian dynasty's revival of the university (1400) — refounding it with a new theology faculty (without which Pope Urban V had refused to grant it full university status) — gave the university the complete curriculum that made it a genuinely competitive European institution",
            "Kraków's position as the royal capital of Poland and the cultural centre of Polish-Lithuanian culture — and its proximity to the astronomical traditions of the Silesian and Bohemian universities — created the intellectual environment that attracted Copernicus and shaped his education in astronomy"
        ],
        "effects": [
            "Nicolaus Copernicus's education at the Jagiellonian University (c.1491–1495) — where he studied mathematics, astronomy, and philosophy under professors who taught the Ptolemaic system — provided the training that enabled his eventual development of heliocentrism, making Kraków an indirect origin of the Scientific Revolution",
            "The Nazi Sonderaktion Krakau (6 November 1939) — in which SS and Gestapo officers arrested 183 Jagiellonian University professors under the pretext of a lecture on 'German plans for Polish science' — was the most dramatic act of intellectual genocide in the Nazi occupation of Poland, resulting in the death of many professors in concentration camps",
            "Karol Wojtyła's (Pope John Paul II) formative education in philosophy and theology at the Jagiellonian University shaped his phenomenological approach to Catholic ethics — the intellectual foundation of Veritatis Splendor (1993) and the Theology of the Body — making Kraków a formative site of 20th-century Catholic thought",
            "The Jagiellonian University's survival through the Partitions, Nazi occupation, and Communist control — maintaining Polish scholarly tradition through every external attempt to suppress or distort it — makes it the primary institutional symbol of Polish intellectual continuity and national resilience"
        ],
        "relationships": [
            {"entity": "Casimir III the Great (King of Poland, founder)", "relationship": "FOUNDED_BY", "note": "Casimir III the Great founded the university (1364) — the first in Poland and the second in Central-Eastern Europe after Prague — to provide Poland with trained professionals"},
            {"entity": "Nicolaus Copernicus (studied c.1491–1495)", "relationship": "EDUCATED_THE_FUTURE_AUTHOR_OF_THE_HELIOCENTRIC_THEORY", "note": "Copernicus studied at the Jagiellonian University (c.1491–1495) — receiving the astronomical and mathematical training that underpinned the heliocentric theory"},
            {"entity": "De revolutionibus orbium coelestium (1543, heliocentric theory)", "relationship": "INTELLECTUAL_ORIGINS_ROOTED_IN_THE_EDUCATION_OF_ITS_AUTHOR_AT", "note": "Copernicus's heliocentric work — which initiated the Scientific Revolution — had intellectual roots in his Jagiellonian University education"},
            {"entity": "Sonderaktion Krakau (1939, Nazi arrest of 183 professors)", "relationship": "TARGETED_BY_THE_NAZI", "note": "The Nazi arrest of 183 professors in a lecture hall (1939) was the most dramatic act of intellectual genocide in the Nazi occupation of Poland"},
            {"entity": "Pope John Paul II (Karol Wojtyła)", "relationship": "ALMA_MATER_OF", "note": "Karol Wojtyła studied theology at the Jagiellonian University (1945–1946) — where his phenomenological approach to Catholic ethics was shaped"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 31 — {len(ENTITIES)} entities (Class 360: Universities & Learned Academies)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
