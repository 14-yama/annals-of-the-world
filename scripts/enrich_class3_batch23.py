#!/usr/bin/env python3
"""
Batch 23 — 8 entities (Class 340): Global Religious Traditions & Communities
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()
FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/340-Class-340"
FILE_PREFIX = "340"


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

    ("anglican-communion", {
        "summary": (
            "The Anglican Communion (est. 1867, formally; origins in English Reformation 1534) is a worldwide fellowship of 85 million Christians in 42 member churches and 6 regional councils across 165 countries — the third-largest Christian denomination in the world after the Roman Catholic Church and the Eastern Orthodox Church. Founded on the Church of England's break from Rome under Henry VIII (1534), the Anglican tradition holds a distinctive theological position as a 'middle way' (via media) between Roman Catholicism and continental Protestantism, combining Catholic liturgical tradition with Protestant scriptural authority.\n\n"
            "The Communion is held together by the Archbishop of Canterbury as its spiritual head (though without canonical authority over member churches), the Lambeth Conference of all Anglican bishops (held every ten years since 1867), the Primates' Meeting, and the Anglican Consultative Council. The 1867 Lambeth Conference established the structure of a communion of autonomous churches in full communion with Canterbury — a constitutional model of voluntary association that has been increasingly tested by theological disagreements over women's ordination and LGBTQ+ inclusion.\n\n"
            "The Anglican Communion's global spread — largely through British colonial expansion — makes it one of the most geographically diverse Christian bodies: its largest national churches are now in Nigeria (18 million), Uganda (12 million), and Tanzania (5 million) rather than England, creating a demographic shift that has given the Global South churches increasing theological and political weight in Communion-wide debates."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "85 million Christians in 165 countries (est. formally 1867; origins in English Reformation 1534); third-largest Christian denomination; theological 'via media' between Catholic and Protestant; Lambeth Conference every 10 years since 1867; largest national churches now in Nigeria and Uganda; increasingly tested by LGBTQ+ and women's ordination debates.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Henry VIII's break from Rome (1534) — driven primarily by the political need for a divorce from Catherine of Aragon rather than theological conviction — created the Church of England as an independent national church that evolved a distinctively Anglican theological identity over the following century",
            "The Elizabethan Settlement (1559–1563) — establishing the 'via media' between Roman Catholic and continental Protestant theology through the Thirty-Nine Articles and the Book of Common Prayer — defined the theological character of Anglicanism as a tradition that sought to comprehend multiple theological positions within a single liturgical framework",
            "British imperial expansion across the 18th and 19th centuries — carrying Anglican missionaries and colonial churches to Africa, Asia, the Americas, and the Pacific — created the global spread of Anglican Christianity that transformed the Church of England's national institution into a worldwide communion"
        ],
        "effects": [
            "The Anglican Communion's 'via media' theological tradition — claiming to represent the authentic Catholic and Reformed tradition — influenced 20th-century ecumenical dialogue, making Anglican churches key partners in the World Council of Churches and bilateral ecumenical agreements with Roman Catholics, Lutherans, and Orthodox churches",
            "The demographic shift from a European-centred to a Global South-centred Communion — with Nigeria, Uganda, and Tanzania having larger Anglican populations than England — represents the most significant shift in the global centre of gravity of any major Christian denomination",
            "The theological controversies over women's ordination and LGBTQ+ inclusion — producing schisms (the formation of ACNA in North America, 2009) and threats of fracture — have made the Anglican Communion the central arena for the debate about the relationship between traditional Christian moral theology and modern liberal values",
            "The Book of Common Prayer — the liturgical backbone of Anglican worship since 1549 — shaped English prose style and created a shared liturgical experience across 85 million Anglicans, making it one of the most influential books in English cultural history"
        ],
        "relationships": [
            {"entity": "Archbishop of Canterbury", "relationship": "SPIRITUAL_HEAD_IS_THE", "note": "The Archbishop of Canterbury is the symbolic head of the Anglican Communion — without canonical authority over member churches"},
            {"entity": "Church of England", "relationship": "MOTHER_CHURCH_AND_ORIGINATOR_OF", "note": "The Church of England — established by Henry VIII's break from Rome (1534) — is the mother church and originator of the worldwide Anglican Communion"},
            {"entity": "Lambeth Conference (1867–present)", "relationship": "CONSTITUTIONAL_GATHERING_OF", "note": "The Lambeth Conference — held every 10 years since 1867 — is the primary instrument of Anglican Communion-wide decision-making"},
            {"entity": "Church of Nigeria (Anglican)", "relationship": "LARGEST_NATIONAL_MEMBER_CHURCH_OF", "note": "Nigeria's Anglican Church (18 million members) is the largest national church in the Communion — larger than the Church of England itself"},
            {"entity": "Book of Common Prayer (1549)", "relationship": "LITURGICAL_FOUNDATION_OF", "note": "The Book of Common Prayer — shaping English prose and Anglican worship since 1549 — is the theological and liturgical backbone of the Communion"}
        ],
    }),

    ("eastern-orthodox-church", {
        "summary": (
            "The Eastern Orthodox Church (Greek: Ἐκκλησία τῶν Ὀρθοδόξων, est. formally 1054; origins in early Christianity) is a communion of 14 autocephalous (self-governing) churches with approximately 260 million members worldwide — the second-largest Christian denomination in the world after the Roman Catholic Church. The Orthodox tradition claims direct apostolic succession from the early Christian church and the Seven Ecumenical Councils (325–787 CE), and defines Christian orthodoxy through the Nicene-Constantinopolitan Creed without the Roman Catholic addition of the filioque clause — the theological difference that precipitated the Great Schism of 1054.\n\n"
            "The Orthodox Communion is held together by the Ecumenical Patriarch of Constantinople (currently Patriarch Bartholomew I) as the 'first among equals' (primus inter pares) — without the monarchical authority of the Pope — and by shared liturgical tradition: the Byzantine Rite, the Divine Liturgy of Saint John Chrysostom, and the liturgical year that structures Orthodox Christian life across 14 national churches. The largest Orthodox churches are the Russian Orthodox Church (100–150 million members), the Romanian Orthodox Church (18 million), and the Serbian Orthodox Church (7 million).\n\n"
            "The Orthodox Church's 20th-century history was dominated by the Soviet persecution of religion (1917–1991) — which attempted to eliminate Orthodox Christianity through the execution of clergy, destruction of churches, and suppression of religious practice — and by the subsequent Orthodox religious revival in Russia and Eastern Europe after the Soviet collapse. The Russian Orthodox Church's close relationship with the Putin government has made it a subject of controversy in the 21st century, particularly over its support for the Russian invasion of Ukraine."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "260 million members — second-largest Christian denomination (est. Great Schism 1054; origins in early Christianity); 14 autocephalous churches; claims apostolic succession from 7 Ecumenical Councils (325–787 CE); Great Schism 1054 split Western and Eastern Christianity; Russian Orthodox Church (150m members) survived Soviet persecution (1917–1991); Byzantine Rite shared across all member churches.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Great Schism of 1054 — precipitated by the filioque controversy (Rome's addition of a clause to the Nicene Creed), disputes over papal authority, and political tensions between Constantinople and Rome — formally separated Eastern and Western Christianity after centuries of increasing divergence",
            "The Byzantine Empire's patronage of the Orthodox Church (313–1453 CE) — creating the symbiosis of imperial power and Orthodox Christianity known as Caesaropapism — established the Church's identity as the religious pillar of Byzantine civilisation and subsequently of Orthodox Slavic civilisations",
            "The Mongol invasion and the fall of Constantinople (1453) — and the subsequent rise of Moscow as the 'Third Rome' — transferred the centre of Orthodox Christianity from Byzantium to Russia, creating the Russian Orthodox Church as the largest and most politically powerful Orthodox institution"
        ],
        "effects": [
            "The Orthodox Church's transmission of Byzantine civilisation — theology, iconography, liturgy, ecclesiastical architecture — to Russia, Serbia, Bulgaria, Romania, and Georgia created the religious and cultural foundation of the Eastern European and Slavic world",
            "The Russian Orthodox Church's survival of Soviet persecution (execution of tens of thousands of clergy, destruction of thousands of churches, 1917–1941) and subsequent revival after 1991 is one of the most remarkable institutional recoveries in the history of religious institutions",
            "The Orthodox theological tradition — particularly its emphasis on apophatic theology, theosis (divinisation), and the icon as windows to the divine — has shaped Eastern European art, architecture, music, and literary culture in ways that remain distinctively different from Western Christian cultural production",
            "The rupture between the Russian Orthodox Church and the Ecumenical Patriarchate over the autocephaly of the Ukrainian Orthodox Church (2018–2019) has created the most serious division within Orthodoxy since the Great Schism, reflecting the geopolitical conflict between Russia and Ukraine in ecclesiastical form"
        ],
        "relationships": [
            {"entity": "Great Schism of 1054", "relationship": "FORMALLY_ESTABLISHED_AS_SEPARATE_COMMUNION_BY", "note": "The Great Schism — precipitated by the filioque controversy and papal authority disputes — formally separated Eastern and Western Christianity"},
            {"entity": "Ecumenical Patriarch of Constantinople", "relationship": "PRIMUS_INTER_PARES_IS_THE", "note": "The Ecumenical Patriarch is 'first among equals' — without papal authority — holding the 14 autocephalous Orthodox churches in fellowship"},
            {"entity": "Russian Orthodox Church", "relationship": "LARGEST_MEMBER_CHURCH_IS_THE", "note": "The Russian Orthodox Church (100–150 million members) is the largest Orthodox church — surviving Soviet persecution to become the dominant institution of Russian national identity"},
            {"entity": "Byzantine Empire", "relationship": "PATRON_STATE_RELATIONSHIP_WITH", "note": "Byzantine imperial patronage (313–1453 CE) shaped the Orthodox Church's theology, art, architecture, and political theory"},
            {"entity": "Ukrainian Orthodox Church autocephaly (2019)", "relationship": "DEEPEST_RECENT_DIVISION_CAUSED_BY", "note": "The 2018–2019 grant of autocephaly to the Ukrainian Orthodox Church — opposed by Moscow — created the most serious Orthodox schism since 1054"}
        ],
    }),

    ("coptic-orthodox-church", {
        "summary": (
            "The Coptic Orthodox Church (ϯⲉⲕⲕⲗⲏⲥⲓⲁ ⲛ̀ⲣⲉⲙⲛ̀ⲭⲏⲙⲓ, est. traditionally 42 CE by Saint Mark; formally established as an independent patriarchate by the Council of Chalcedon 451 CE) in Egypt is the indigenous Christian church of Egypt — one of the oldest Christian communities in the world, claiming direct apostolic foundation by Saint Mark the Evangelist (42 CE) — with approximately 10–15 million members in Egypt (10–12% of the population) and a diaspora of 2–3 million worldwide. The Copts are the largest Christian minority in the Middle East and Africa.\n\n"
            "The Coptic Church's separation from the Byzantine and Roman churches at the Council of Chalcedon (451 CE) — over the Miaphysite Christology of 'one nature' of Christ — established it as the originator of Oriental Orthodox Christianity, a communion that includes the Ethiopian, Eritrean, Syriac, Armenian, and Malankara Orthodox churches. The Coptic language — the direct descendant of ancient Egyptian, written in a modified Greek alphabet — is preserved as the liturgical language of the church, making Coptic services the closest living connection to the language of pharaonic Egypt.\n\n"
            "The Coptic Church produced the Desert Fathers — Anthony the Great (the father of Christian monasticism), Pachomius (the founder of communal monasticism), and the monastic movement of the Egyptian desert (3rd–5th centuries CE) — whose tradition of ascetic withdrawal and community formation became the foundation of Christian monasticism worldwide. The Coptic Church has survived 1,600 years of Muslim-majority rule in Egypt, maintaining a continuous Christian presence that predates the Arab conquest by 600 years."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Founded traditionally by Saint Mark (42 CE); largest Christian minority in the Middle East (10–15m in Egypt); originator of Oriental Orthodox Christianity after Council of Chalcedon (451 CE); Coptic language is direct descendant of ancient Egyptian; produced the Desert Fathers — Anthony the Great and Pachomius, founders of Christian monasticism; 1,600 years of survival under Muslim majority rule.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Saint Mark's missionary activity in Alexandria (c.42 CE) — establishing the first Christian community in Egypt — created the foundation of a church that would become one of the most theologically significant in early Christianity",
            "The Council of Chalcedon (451 CE) and the Coptic Church's rejection of its Dyophysite Christology — adhering to Miaphysitism (one nature of Christ) against the Greek and Latin churches — created the definitive separation that established the Coptic Church as an independent Oriental Orthodox tradition",
            "The Egyptian desert's harsh conditions and the tradition of ascetic withdrawal already present in Jewish and pagan Egyptian spiritual practice created the cultural environment in which Anthony the Great and Pachomius developed Christian monasticism"
        ],
        "effects": [
            "The Desert Fathers' monasticism — developed in the Egyptian desert from the 3rd century CE — became the foundation of Christian monasticism worldwide: the Rule of Saint Benedict, the Cistercians, the Franciscans, and every subsequent Christian monastic tradition trace their lineage to the Coptic Desert Fathers",
            "The Coptic Church's preservation of the Coptic language — the direct descendant of ancient Egyptian — as its liturgical language means that Coptic services are the closest living linguistic connection to pharaonic Egypt, making Coptic Christianity a living link to one of the world's oldest civilisations",
            "The Coptic Church's 1,600-year survival under Muslim-majority rule — including periods of persecution under Fatimid, Mamluk, and Ottoman rule — makes it the primary example of a Christian minority community's sustained existence in a predominantly Muslim society",
            "The Oriental Orthodox Communion — the Coptic, Ethiopian, Eritrean, Syriac, Armenian, and Malankara churches — constitutes approximately 60 million Christians worldwide, all sharing the Miaphysite Christology that the Council of Chalcedon condemned"
        ],
        "relationships": [
            {"entity": "Saint Mark the Evangelist", "relationship": "FOUNDED_TRADITIONALLY_BY", "note": "The Coptic Church claims Saint Mark (42 CE) as its founder — making it one of the oldest apostolically founded Christian churches"},
            {"entity": "Council of Chalcedon (451 CE)", "relationship": "SEPARATED_FROM_ROMAN-BYZANTINE_CHURCHES_BY", "note": "The Coptic Church's rejection of Chalcedonian Dyophysitism established it as the originator of Oriental Orthodox Christianity"},
            {"entity": "Anthony the Great (Father of Christian monasticism)", "relationship": "PRODUCED_THE_FOUNDER_OF_CHRISTIAN_MONASTICISM", "note": "Anthony the Great — the Egyptian Coptic ascetic — is the father of Christian monasticism, whose example shaped all subsequent monastic traditions"},
            {"entity": "Christian monasticism (worldwide)", "relationship": "ORIGINATOR_OF", "note": "The Desert Fathers of Egypt — Anthony, Pachomius — created Christian monasticism that became the foundation of all subsequent monastic traditions"},
            {"entity": "Oriental Orthodox Communion", "relationship": "FOUNDING_CHURCH_OF", "note": "The Coptic Church is the founding church of Oriental Orthodoxy — the communion of Miaphysite churches including Ethiopian, Armenian, and Syriac Orthodox"}
        ],
    }),

    ("ethiopian-orthodox-tewahedo-church", {
        "summary": (
            "The Ethiopian Orthodox Tewahedo Church (የኢትዮጵያ ኦርቶዶክስ ተዋሕዶ ቤተ ክርስቲያን, est. 4th century CE; traditionally founded by Frumentius, c.330 CE) is the largest Oriental Orthodox church in Africa — with approximately 45–55 million members making it the largest Oriental Orthodox communion and one of the oldest Christian churches in the world. Ethiopia and Eritrea are among the only countries where Christianity was adopted as a state religion before Rome (the Ethiopian Aksumite Empire converted c.330 CE under King Ezana, a generation before the Edict of Thessalonica in 380 CE).\n\n"
            "The Ethiopian Church's theological distinctiveness — its Tewahedo (Miaphysite) Christology, its use of Ge'ez as a liturgical language, its observance of both Old and New Testament law (the Saturday Sabbath, dietary laws, circumcision, the Ark of the Covenant as the supreme focus of worship), and its claim to possess the original Ark of the Covenant in Axum — reflects a Christianity shaped by close proximity to Judaism and to the ancient Kingdom of Israel through the Solomonic dynasty.\n\n"
            "The Ethiopian Church's 45-million-strong membership — growing rapidly — makes it one of the fastest-growing Christian churches in the world. Its tradition of church painting (the characteristic large-eyed Ethiopian style), its 81-book Biblical canon (the largest of any Christian denomination, including the books of Enoch and Jubilees), its debteras (trained liturgical scholars), and its 20,000+ churches across Ethiopia constitute one of the world's richest and most ancient Christian civilisations."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Largest Oriental Orthodox church (45–55m members); one of oldest Christian state churches — Ethiopia adopted Christianity c.330 CE, before Rome's Edict of Thessalonica (380 CE); claims possession of the Ark of the Covenant in Axum; 81-book Biblical canon — largest of any denomination; traditional observance of Old Testament law (Sabbath, dietary laws, circumcision); one of world's richest and oldest Christian civilisations.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The conversion of King Ezana of the Aksumite Empire (c.330 CE) by the Syriac missionary Frumentius — who was shipwrecked off the Red Sea coast and rose to become the royal tutor and eventually bishop — created one of the first Christian state religions in the world, a generation before the Roman Empire's adoption of Christianity",
            "The Ethiopian Church's close proximity to the Jewish communities of the Horn of Africa — including the Beta Israel (Ethiopian Jews) whose traditions significantly influenced Ethiopian Christianity — created a church that preserved Jewish practices (Saturday Sabbath, dietary laws, circumcision) not found in other Christian traditions",
            "The claim to possess the Ark of the Covenant at Axum — brought to Ethiopia by Menelik I, the legendary son of King Solomon and the Queen of Sheba — created a theological and national mythology that gave the Ethiopian Church its distinctive relationship to the Hebrew Bible"
        ],
        "effects": [
            "The Ethiopian Orthodox Church's early adoption of Christianity (c.330 CE) before Rome established Ethiopia as the earliest surviving example of a Christian state, making it a model for the relationship between monarchy and Christianity that predates Constantine's conversion by a generation",
            "The Church's 81-book Biblical canon — including the books of Enoch, Jubilees, and 1 and 2 Meqabyan — preserves texts excluded from other Christian canons, making Ethiopia the primary repository of these early Jewish and Christian literary traditions",
            "The Ethiopian Church's resistance to the European missionary project — the Ethiopian church successfully expelled Jesuit missionaries in the 17th century and maintained its indigenous traditions — makes it the primary example of African Christianity that developed on its own terms without European mediation",
            "The debteras system — the trained liturgical scholars who preserve the church's musical, poetic, and homiletic traditions — constitutes one of the world's oldest continuously transmitted oral scholarly traditions, preserving liturgical knowledge across 80 generations"
        ],
        "relationships": [
            {"entity": "King Ezana of the Aksumite Empire", "relationship": "ESTABLISHED_AS_STATE_RELIGION_BY", "note": "Ezana's conversion (c.330 CE) — making the Aksumite Empire one of the first Christian states — established the Ethiopian Church's extraordinary antiquity"},
            {"entity": "Ark of the Covenant (Axum)", "relationship": "CLAIMS_POSSESSION_OF_THE", "note": "The Ethiopian Church claims the Ark of the Covenant is held in the Church of Our Lady Mary of Zion in Axum — the supreme focus of Ethiopian Christian worship"},
            {"entity": "Coptic Orthodox Church", "relationship": "HISTORICALLY_UNDER_METROPOLITAN_OF", "note": "The Ethiopian Church was historically under the authority of the Coptic Patriarch — achieving autocephaly only in 1959"},
            {"entity": "Solomonic dynasty (Ethiopia)", "relationship": "ROYAL_CHURCH_OF", "note": "The Ethiopian Church's mythology of Menelik I (son of Solomon and Queen of Sheba) links it to the Solomonic dynasty that ruled Ethiopia until 1974"},
            {"entity": "Book of Enoch and Ethiopian Biblical canon", "relationship": "PRIMARY_PRESERVING_TRADITION_OF", "note": "The Ethiopian 81-book Biblical canon — including Enoch and Jubilees — preserves texts lost to other Christian traditions"}
        ],
    }),

    ("sufism", {
        "summary": (
            "Sufism (تصوف, Tasawwuf, Islamic mysticism, est. as a distinct tradition c.8th–9th centuries CE) is the mystical and esoteric dimension of Islam — a tradition of spiritual practice centred on the direct personal experience of God (fana, annihilation of the self in God), organised into brotherhoods (tariqas) and transmitted through master-disciple chains (silsilas). With approximately 100–200 million practitioners worldwide in hundreds of distinct orders, Sufism is one of the most widespread forms of Islamic religious practice and the primary means by which Islam spread across Africa, Central Asia, South Asia, and Southeast Asia.\n\n"
            "The great Sufi orders — Qadiriyya (founded by Abd al-Qadir al-Jilani, Baghdad, 12th century), Naqshbandiyya (founded by Bahauddin Naqshband, Central Asia, 14th century), Chishtiyya (founded in South Asia, 12th century), Mevleviyya (the 'Whirling Dervishes', founded by Rumi's followers in Anatolia, 13th century), and Tijaniyya (founded in West Africa, 18th century) — are the institutional vehicles through which Islamic mystical practice reached virtually every Muslim community in the world. The Sufi order was the primary instrument of Islamic expansion beyond the Arab heartlands.\n\n"
            "Sufism produced the greatest Islamic poets — Rumi (13th century), Hafez (14th century), and Ibn Arabi (13th century) — whose works constitute the most celebrated body of religious poetry in Islamic civilisation. The Mevlevi Sema (whirling ceremony) — the Sufi ritual dance of the Mevlevi order — is recognised by UNESCO as Intangible Cultural Heritage and is the most widely known Sufi ritual in the world."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Islamic mysticism with 100–200 million practitioners worldwide (est. as distinct tradition c.8th–9th centuries CE); primary vehicle for spread of Islam beyond Arab heartlands into Africa, Central Asia, South Asia, Southeast Asia; major orders include Qadiriyya, Naqshbandiyya, Chishtiyya, Mevleviyya, Tijaniyya; produced Rumi, Hafez, Ibn Arabi — greatest Islamic poets; Mevlevi Sema UNESCO Intangible Cultural Heritage.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The early Islamic ascetic reaction to the worldly wealth and power that followed the rapid Arab conquests (7th–8th centuries CE) — a movement of renunciation (zuhd) that sought the spiritual core of Islam against the perceived corruption of imperial politics — gave birth to Sufism as a distinct spiritual tradition",
            "The influence of Neoplatonic philosophy and Gnostic traditions — transmitted through the translation movement of the 8th–9th centuries — provided Sufism with the conceptual vocabulary (fana, wayfaring, the stages of the soul) that shaped its distinctive mystical theology",
            "The political instability of the Abbasid caliphate and the subsequent fragmentation of the Islamic world drove many Muslims to seek spiritual authority in the Sufi sheikh rather than in corrupt political rulers, giving the Sufi order its institutional vitality"
        ],
        "effects": [
            "The Sufi tariqas were the primary vehicle for Islamic expansion beyond the Arab heartlands: the Qadiriyya in West Africa, the Naqshbandiyya in Central Asia and China, the Chishtiyya in South Asia, and the Mevleviyya in the Ottoman Empire spread Islam through peaceful spiritual transmission rather than conquest",
            "Sufism's greatest poets — Rumi, Hafez, Ibn Arabi, Sadi — produced the most celebrated body of Islamic religious literature, whose influence on Persian, Turkish, Urdu, and Arabic poetry is comparable to Dante's influence on European literature",
            "The Wahhabi/Salafi movements of the 18th–21st centuries — defining themselves in explicit opposition to Sufi 'innovation' and 'saint worship' — represent the most significant internal Islamic conflict over religious practice, making Sufism the terrain on which the battle for the soul of contemporary Islam is fought",
            "The Mevlevi Sema ceremony — the whirling of the dervishes — became the most internationally recognised form of Islamic spiritual practice, creating a bridge between Islamic mysticism and global audiences through its combination of music, movement, and contemplation"
        ],
        "relationships": [
            {"entity": "Rumi (Jalal ad-Din Muhammad Rumi)", "relationship": "GREATEST_POET_OF", "note": "Rumi — the 13th-century Sufi mystic of the Mevlevi order — produced the most celebrated Islamic religious poetry, read by 300 million people annually"},
            {"entity": "Major Sufi orders (Qadiriyya, Naqshbandiyya, Chishtiyya, Mevleviyya, Tijaniyya)", "relationship": "INSTITUTIONAL_VEHICLE_OF", "note": "The major tariqas are the organisational infrastructure through which Sufism spread Islam across every Muslim community outside the Arab heartlands"},
            {"entity": "Islamic expansion (Sub-Saharan Africa, Central Asia, South Asia, Southeast Asia)", "relationship": "PRIMARY_VEHICLE_OF", "note": "Sufi missionaries — not Arab armies — were responsible for spreading Islam across the non-Arab Muslim world"},
            {"entity": "Wahhabi/Salafi movement", "relationship": "DEFINED_ITSELF_IN_OPPOSITION_TO", "note": "The Wahhabi/Salafi movements define themselves by opposition to Sufi 'innovation' — making Sufism the terrain of the contemporary Islamic internal conflict over orthodoxy"},
            {"entity": "Mevlevi Sema (Whirling Dervishes)", "relationship": "MOST_INTERNATIONALLY_RECOGNISED_RITUAL_OF", "note": "The Mevlevi whirling ceremony — UNESCO Intangible Cultural Heritage — is the most widely known Sufi spiritual practice globally"}
        ],
    }),

    ("al-azhar-al-sharif", {
        "summary": (
            "Al-Azhar (الأزهر الشريف, The Most Resplendent, est. 970–972 CE) in Cairo, Egypt, is the oldest continuously operating Islamic university in the world and the most authoritative institution of Sunni Islamic scholarship — the primary source of religious rulings (fatwas) for the world's 1.9 billion Sunni Muslims. Founded by the Fatimid Caliph al-Mu'izz as a Shia institution, it was converted to Sunni Islam by Saladin in 1171 CE and has since served as the supreme authority on Sunni Islamic jurisprudence, theology, and Quranic sciences.\n\n"
            "Al-Azhar's Grand Sheikh — currently Ahmad al-Tayyeb (since 2010) — is considered the most authoritative religious figure in Sunni Islam, comparable in global reach (if not in institutional authority) to the Pope in Roman Catholicism. The university enrolls approximately 500,000 students in Egypt and manages a network of affiliated institutions across the Islamic world. Al-Azhar's curriculum — integrating traditional Islamic sciences (fiqh, hadith, tafsir, Arabic grammar) with modern academic disciplines — produces the religious scholars who staff mosques, courts, and educational institutions across the Arab world and beyond.\n\n"
            "Al-Azhar's role in Egyptian and Arab politics has been contested across its 1,050-year history: it was the institution that gave religious legitimacy to the Ottoman conquest of Egypt (1517), that endorsed Nasser's Arab nationalism (1960s), that debated (and eventually condemned) extremist movements, and that has been increasingly associated with the Egyptian state under el-Sisi. Its complex relationship with political authority — simultaneously legitimising and constraining — makes it one of the most studied institutions in the sociology of religion."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Oldest continuously operating Islamic university in the world (est. 970–972 CE); primary authority on Sunni Islam for 1.9 billion Sunni Muslims; Grand Sheikh is most authoritative Sunni religious figure; 500,000 students enrolled; founded Fatimid/Shia, converted to Sunni by Saladin (1171 CE); complex political legitimising role through Ottoman conquest, Egyptian nationalism, and contemporary Egyptian state.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Fatimid Caliph al-Mu'izz's establishment of al-Azhar (970–972 CE) as the primary mosque and university of the new Fatimid capital Cairo — intended to propagate Ismaili Shia Islam — created the institution that would, after Saladin's conversion of Egypt to Sunni Islam (1171), become the supreme authority of Sunni scholarship",
            "Saladin's conversion of al-Azhar to Sunni scholarship (1171 CE) — removing the Ismaili professors and replacing them with Shafi'i and Maliki Sunni scholars — established the institutional foundation for al-Azhar's role as the primary authority of Sunni religious learning",
            "The Ottoman conquest of Egypt (1517) — which transferred al-Azhar's financial endowments (awqaf) from the Mamluk sultans to the Ottoman state — created the economic base that enabled the institution to continue operating independently of individual political rulers"
        ],
        "effects": [
            "Al-Azhar's Grand Sheikh's religious rulings — widely disseminated across the Islamic world through media, education, and mosque networks — shape the religious understanding and practice of a billion Sunni Muslims on questions of jurisprudence, family law, bioethics, and political theology",
            "The al-Azhar model of Islamic education — integrating traditional Quranic sciences with modern academic disciplines — became the template for Islamic universities across the Muslim world, from Indonesia to Morocco, making it the institutional origin of modern Islamic higher education",
            "Al-Azhar's position on extremist violence — its condemnations of the Islamic State (2014–2015) and subsequent declarations — have significant international weight in debates about the theological legitimacy of jihadist violence, making it a key institution in counter-extremism efforts",
            "The historic al-Azhar Mosque (distinct from the university) — the fifth mosque built in Egypt and the oldest surviving Fatimid mosque — is one of the most important architectural monuments in Cairo, preserving the visual record of Fatimid Islamic art"
        ],
        "relationships": [
            {"entity": "Fatimid Caliphate", "relationship": "FOUNDED_BY_THE", "note": "Al-Azhar was established by the Fatimid Caliph al-Mu'izz (970–972 CE) as the principal mosque and university of the new Fatimid capital Cairo"},
            {"entity": "Saladin (Salah ad-Din Yusuf ibn Ayyub)", "relationship": "CONVERTED_TO_SUNNI_INSTITUTION_BY", "note": "Saladin converted al-Azhar from Shia to Sunni scholarship (1171 CE) — transforming it into the primary authority of Sunni Islamic learning"},
            {"entity": "Grand Sheikh of Al-Azhar", "relationship": "SPIRITUAL_AUTHORITY_CENTERED_ON_THE", "note": "The Grand Sheikh — currently Ahmad al-Tayyeb — is the most authoritative religious figure in Sunni Islam"},
            {"entity": "Sunni Islamic jurisprudence (fiqh)", "relationship": "PRIMARY_GLOBAL_AUTHORITY_ON", "note": "Al-Azhar's fatwas on Sunni jurisprudence, theology, and Quranic sciences shape the religious understanding of 1.9 billion Sunni Muslims"},
            {"entity": "Islamic higher education (global network)", "relationship": "INSTITUTIONAL_MODEL_FOR", "note": "The al-Azhar model of integrating traditional Islamic sciences with modern academic disciplines is the template for Islamic universities worldwide"}
        ],
    }),

    ("church-of-england", {
        "summary": (
            "The Church of England (est. 1534 CE, break from Rome; definitively established under Elizabeth I 1559–1563) is the established church of England — the oldest and largest Anglican church, with approximately 1 million regular worshippers, 16,000 churches, and 26 million baptised members in England. As the mother church of the worldwide Anglican Communion (85 million members), its theological decisions and constitutional structure have global consequences for Anglican Christianity. The monarch of England is the Supreme Governor of the Church of England — the most distinctive feature of the English established church.\n\n"
            "The Church of England was established by Henry VIII's Act of Supremacy (1534) — breaking from Rome primarily to enable Henry's divorce from Catherine of Aragon — and was theologically shaped by Thomas Cranmer's Book of Common Prayer (1549, 1552) and the Thirty-Nine Articles (1563). The Elizabethan Settlement created the 'via media' — the middle way between Rome and Geneva — that has defined Anglican theological identity: Catholic in its liturgical tradition (bishops, sacraments, apostolic succession) and Protestant in its rejection of papal authority and its emphasis on Scripture.\n\n"
            "The Church of England's contribution to English culture is impossible to overstate: the Book of Common Prayer (1549–1662) shaped English prose style alongside the King James Bible; the parish system created the administrative infrastructure of English local government; Westminster Abbey and St Paul's Cathedral are the primary stages of British national ritual; and the Church's engagement with science, literature, and public life produced the Anglican intellectual tradition that includes Newton, Darwin, and C.S. Lewis."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Established church of England (est. 1534 CE); mother church of 85 million-member Anglican Communion; 'via media' theology — Catholic liturgy with Protestant scriptural authority; Book of Common Prayer shaped English prose; monarch as Supreme Governor — most distinctive constitutional feature; 16,000 churches; Newton, Darwin, C.S. Lewis products of Anglican intellectual tradition.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Henry VIII's desire for a divorce from Catherine of Aragon — denied by Pope Clement VII under political pressure from Catherine's nephew Charles V — and the political ambition to appropriate the Church's wealth created the occasion for the break from Rome (1534)",
            "Thomas Cranmer's theological genius — creating the Book of Common Prayer, the Thirty-Nine Articles, and the English liturgical tradition — transformed Henry VIII's political schism into a distinctively English theological reformation",
            "Elizabeth I's Elizabethan Settlement (1559–1563) — rejecting both the Catholic restoration of Mary I and the Calvinist demands of the Puritans — established the 'via media' that made the Church of England a broad church capable of accommodating diverse theological positions"
        ],
        "effects": [
            "The Book of Common Prayer (1549–1662) — creating a distinctive English language liturgy — shaped English prose style alongside the King James Bible, making Anglican Christianity one of the two primary forces in English literary culture",
            "The Church of England's parish system — 16,000 parishes covering every community in England — created the administrative infrastructure of English local governance, with parish records constituting the primary source for English genealogical and demographic history before civil registration (1837)",
            "The Church of England's role as the mother church of the worldwide Anglican Communion transformed a national institution into a global one — with the consequences of English colonial expansion (Anglican churches in North America, Africa, Australia) returning to reshape the mother church through the Global South's theological conservatism",
            "The Church of England's established status — the monarch as Supreme Governor, 26 bishops in the House of Lords — makes religion constitutionally embedded in the English state in a way unique among major democracies, creating permanent tensions between secular democratic governance and religious constitutional tradition"
        ],
        "relationships": [
            {"entity": "Henry VIII (King of England)", "relationship": "FOUNDER_VIA_ACT_OF_SUPREMACY_BY", "note": "Henry VIII's Act of Supremacy (1534) — breaking from Rome to enable his divorce — established the Church of England"},
            {"entity": "Book of Common Prayer (1549–1662)", "relationship": "THEOLOGICAL_AND_LITURGICAL_FOUNDATION_OF", "note": "Cranmer's Book of Common Prayer shaped English liturgy and prose style — the most influential English religious text after the Bible"},
            {"entity": "Anglican Communion", "relationship": "MOTHER_CHURCH_OF_THE", "note": "The Church of England is the mother church of the worldwide Anglican Communion (85 million members in 165 countries)"},
            {"entity": "Monarch of England (Supreme Governor)", "relationship": "SUPREME_GOVERNOR_IS_THE", "note": "The English monarch as Supreme Governor — the most distinctive constitutional feature of the established Church of England"},
            {"entity": "Elizabethan Settlement (1559–1563)", "relationship": "DEFINITIVELY_ESTABLISHED_BY_THE", "note": "Elizabeth I's Settlement created the 'via media' — Catholic liturgical tradition with Protestant scriptural authority — that defines Anglican theology"}
        ],
    }),

    ("theosophical-society", {
        "summary": (
            "The Theosophical Society (est. 1875, New York) is a modern spiritual organisation founded by Helena Petrovna Blavatsky (1831–1891), Henry Steel Olcott (1832–1907), and William Quan Judge — whose philosophy of Theosophy ('Divine Wisdom') attempted to synthesise Eastern and Western religious traditions, ancient occultism, and modern science into a universal spiritual framework. Though its current membership is relatively small (approximately 30,000 active members globally), the Theosophical Society had an extraordinary disproportionate influence on the spiritual, intellectual, and cultural history of the late 19th and early 20th centuries.\n\n"
            "Theosophy's core claims — that all religions share a common esoteric core, that the cosmos is governed by universal spiritual laws, that human souls reincarnate toward ultimate spiritual perfection, and that there exists a 'Brotherhood of Masters' (Mahatmas) who guide humanity's spiritual evolution — were the intellectual foundation for the Western occult revival, the New Age movement, modern neo-paganism, and numerous alternative spiritual traditions. Blavatsky's two major works — 'Isis Unveiled' (1877) and 'The Secret Doctrine' (1888) — are the founding texts of the modern Western esoteric tradition.\n\n"
            "The Theosophical Society's headquarters in Adyar, Chennai (India, from 1882) made it one of the first major Western institutions to treat Asian religious and philosophical traditions (Hinduism, Buddhism, Jainism) as equal or superior sources of wisdom to Western religion and science — a perspective that significantly influenced the Hindu and Buddhist revival movements of the late 19th century and the transmission of these traditions to the West."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Founded 1875 by H.P. Blavatsky, H.S. Olcott, and W.Q. Judge; founded in New York, relocated to Adyar, Chennai 1882; foundational influence on Western occult revival, New Age movement, modern neo-paganism; 'The Secret Doctrine' (1888) — founding text of modern Western esoteric tradition; treated Asian religions as superior spiritual sources — significantly influenced Hindu and Buddhist revivals; Olcott co-founded the Buddhist revival in Sri Lanka.",
            "significanceCategory": "continental"
        },
        "causes": [
            "Helena Blavatsky's direct encounter with the crisis of Victorian religious doubt — the conflict between Darwinian science and traditional Christianity — drove her synthesis of Eastern religion, ancient occultism, and universal spirituality as an alternative to both orthodox religion and scientific materialism",
            "The Victorian fascination with spiritualism (contacting the dead), Oriental mysticism, and ancient secret knowledge created a cultural market for the Theosophical synthesis of Eastern and Western esoteric traditions",
            "Henry Steel Olcott's encounter with the Buddhist revival movement in Sri Lanka (from 1880) — and his subsequent co-founding of the Sri Lanka Buddhist movement — gave the Theosophical Society its distinctive role as a bridge between Western spiritual seekers and Asian religious traditions"
        ],
        "effects": [
            "The Theosophical Society's introduction of karma, reincarnation, and chakras to Western spiritual vocabulary transformed Western popular spirituality — these concepts, derived from Hindu and Buddhist sources via Theosophy, became the backbone of the 20th-century New Age movement and contemporary Western spirituality",
            "Henry Steel Olcott's work in Sri Lanka — reviving Buddhist education, establishing schools, and designing the Buddhist flag (1885) — made him a founder of the Buddhist revival movement that resisted British colonial and Christian missionary dominance of Sri Lankan culture",
            "Annie Besant's leadership of the Theosophical Society (from 1907) and her subsequent leadership of the Indian National Congress (1917) created a bridge between Theosophy and Indian nationalism, making the Theosophical Society an unlikely contributor to the Indian independence movement",
            "The Theosophical Society's early championing of Asian religions as equal or superior to Western traditions — in the context of high imperialism — created a counter-current to colonial civilisational hierarchy that significantly influenced 20th-century multiculturalism and the academic study of comparative religion"
        ],
        "relationships": [
            {"entity": "Helena Petrovna Blavatsky", "relationship": "FOUNDED_BY", "note": "Blavatsky co-founded the Theosophical Society (1875) and authored its foundational texts — 'Isis Unveiled' (1877) and 'The Secret Doctrine' (1888)"},
            {"entity": "Henry Steel Olcott", "relationship": "CO-FOUNDED_AND_LED_BUDDHIST_REVIVAL_WITH", "note": "Olcott co-founded the Society and led the Buddhist revival in Sri Lanka — designing the Buddhist flag and establishing Buddhist schools"},
            {"entity": "New Age spirituality (20th century)", "relationship": "INTELLECTUAL_ANCESTOR_OF", "note": "Theosophy's karma, reincarnation, and chakras vocabulary became the backbone of 20th-century New Age spirituality"},
            {"entity": "Hindu and Buddhist revival movements (late 19th century)", "relationship": "SIGNIFICANT_INFLUENCE_ON", "note": "The Society's headquarters in Adyar, Chennai and its championing of Asian religions significantly influenced the Hindu and Buddhist revival movements"},
            {"entity": "Annie Besant", "relationship": "LED_BY_AFTER_BLAVATSKY", "note": "Annie Besant led the Society from 1907 and the Indian National Congress in 1917 — creating a bridge between Theosophy and Indian nationalism"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 23 — {len(ENTITIES)} entities (Class 340: Global Religious Traditions & Communities)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
