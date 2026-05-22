#!/usr/bin/env python3
"""
Batch 32 — 8 entities (Class 351): Major Academies of Science & Learned Societies
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()
FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/351-Class-351"
FILE_PREFIX = "351"


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

    ("academia-sinica", {
        "summary": (
            "Academia Sinica (中央研究院, est. 1928, Nanjing — relocated to Taipei, Taiwan, 1949) is the national academy of Taiwan and the preeminent research institution in the Chinese-speaking world — the highest academic authority in the Republic of China, responsible for conducting cutting-edge research across the natural sciences, humanities, and social sciences. Academia Sinica's relocation from mainland China to Taiwan (1949) — following the Nationalist government's retreat from the Communist victory — gave Taiwan the institutional core of modern Chinese scholarship.\n\n"
            "Academia Sinica was established in 1928 under Cai Yuanpei — one of China's greatest education reformers — as the national academy of the Republic of China, modelled on the Berlin Academy of Sciences. In its early decades at Nanjing, Academia Sinica conducted the foundational archaeological and anthropological research on Chinese civilisation — including the excavation of Anyang (the Shang Dynasty capital) and the discovery of oracle bones that confirmed the historicity of the earliest Chinese dynasty. The Anyang excavations (1928–1937) are among the most consequential archaeological discoveries of the 20th century.\n\n"
            "Academia Sinica's unique situation — as the 'Chinese national academy' operating in Taiwan while the People's Republic of China has the Chinese Academy of Sciences — makes it a politically significant institution: its role in preserving the intellectual heritage of the Republic of China tradition and its world-class research output have given Taiwan international scholarly prestige disproportionate to its political isolation."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Taiwan's national academy (est. 1928, Nanjing; relocated Taipei 1949); preeminent Chinese-speaking world research institution; Anyang excavations (Shang Dynasty capital, oracle bones 1928–1937) — among most consequential 20th-century archaeological discoveries; founded by Cai Yuanpei modelled on Berlin Academy; unique position as 'Chinese national academy' in Taiwan vs CAS in PRC; world-class research output giving Taiwan international scholarly prestige.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The founding of the Republic of China's national academy (1928) under Cai Yuanpei — China's greatest education reformer — was part of the Nationalist government's programme to build modern scientific institutions that would demonstrate China's claim to great-power status",
            "The Communist victory in the Chinese Civil War (1949) — and the Nationalist government's retreat to Taiwan — prompted the relocation of Academia Sinica's members, libraries, and Oracle Bone collections to Taipei, giving Taiwan the institutional core of Republican China's intellectual tradition",
            "The ROC government's determination to maintain Chinese cultural and scholarly authority from Taiwan — against the competing claims of the People's Republic of China — made Academia Sinica politically essential as the institutional embodiment of the ROC's claim to legitimate Chinese governance"
        ],
        "effects": [
            "The Anyang excavations (1928–1937) — discovering the Shang Dynasty capital and the oracle bone script — confirmed the historicity of China's oldest recorded dynasty and established the foundations of modern Chinese archaeology, Shang Dynasty studies, and the decipherment of oracle bone script",
            "Academia Sinica's relocation to Taiwan (1949) — bringing the oracle bone collections, archaeological records, and scholarly personnel that the Communist government left behind — gave Taiwan a unique position as the custodian of crucial aspects of Chinese civilisation's material heritage",
            "Academia Sinica's world-class research output — including genomics, materials science, mathematical physics, and Chinese history — has given Taiwan international scholarly prestige that contradicts its diplomatic isolation, demonstrating that scientific excellence can coexist with limited political recognition",
            "Academia Sinica's Institute of History and Philology — with its oracle bone, bronze inscription, and archaeological collections from the pre-1949 mainland — remains the single most important repository of Shang and Zhou Dynasty primary sources, making Academia Sinica indispensable to the study of early Chinese civilisation"
        ],
        "relationships": [
            {"entity": "Cai Yuanpei (founding president)", "relationship": "FOUNDED_AND_FIRST_PRESIDED_OVER_BY", "note": "Cai Yuanpei — China's greatest education reformer and architect of modern Chinese universities — founded Academia Sinica (1928) modelled on the Berlin Academy of Sciences"},
            {"entity": "Anyang excavations (Shang Dynasty capital, 1928–1937)", "relationship": "CONDUCTED_THE_FOUNDATIONAL", "note": "Academia Sinica's Anyang excavations discovered the Shang Dynasty capital and oracle bone script — among the most consequential archaeological discoveries of the 20th century"},
            {"entity": "Chinese Civil War (1949, Nationalist retreat to Taiwan)", "relationship": "RELOCATED_TO_TAIPEI_AS_RESULT_OF_THE", "note": "The Communist victory forced Academia Sinica's relocation to Taiwan — where it became the institutional core of the ROC's intellectual tradition"},
            {"entity": "Oracle bone collections (Shang Dynasty inscriptions)", "relationship": "PRIMARY_CUSTODIAN_OF_THE", "note": "Academia Sinica holds the most important oracle bone collections from pre-1949 mainland excavations — making it indispensable for early Chinese civilisation studies"},
            {"entity": "Chinese Academy of Sciences (PRC)", "relationship": "COUNTERPART_AND_RIVAL_NATIONAL_ACADEMY_TO_THE", "note": "Academia Sinica and the CAS represent the two national academies of the divided Chinese world — their parallel existence reflects the unresolved Chinese Civil War"}
        ],
    }),

    ("academy-of-athens", {
        "summary": (
            "The Academy of Athens (Ἀκαδημία Ἀθηνῶν, est. 1926, Athens, Greece — the national academy of Greece) is Greece's supreme scientific and cultural institution — the highest academic authority of the Greek state, responsible for the promotion of arts, letters, and sciences, and the custodian of the classical Hellenic intellectual tradition. The Academy of Athens is named for Plato's original Academy (founded c.387 BCE in the olive grove of Akademos outside Athens) — making it simultaneously one of the world's newest national academies and the institutional heir of the oldest named academy in Western philosophy.\n\n"
            "The Academy of Athens was established by royal decree in 1926 — as part of the Greek state's programme of national institution-building — and is housed in the Academy of Athens Building (designed by Theophil Hansen, 1885), one of the finest neoclassical buildings in the world, flanked by marble statues of Plato and Socrates. The building was designed as part of the 'Athens Trilogy' with the National Library and the University of Athens — an ensemble that attempted to give modern Greece visual continuity with its ancient heritage.\n\n"
            "The Academy of Athens's primary scholarly significance is in Greek language studies (the Modern Greek Language Dictionary), Byzantine studies, ancient history, and philosophy — the core disciplines of Greek national scholarly identity. Its 45 full members (in three classes: Natural Sciences, Letters and Fine Arts, Moral and Political Sciences) represent the highest recognition in Greek academic life."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Greece's national academy (est. 1926); named for Plato's Academy (c.387 BCE) — institutional heir of oldest named academy in Western philosophy; Academy of Athens Building (Theophil Hansen, 1885) — one of finest neoclassical buildings in world; 'Athens Trilogy' with National Library and University of Athens; Modern Greek Language Dictionary; 45 full members; centres on Greek language, Byzantine studies, ancient history, philosophy.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The Greek state's nation-building programme of the late 19th and early 20th centuries — establishing the institutions of a modern European state to express Greece's claim to be the heir of classical antiquity — drove the creation of the national academy as the supreme scholarly institution",
            "The 'Athens Trilogy' architectural programme (National Library, University of Athens, Academy of Athens — all by Theophil Hansen) expressed the modern Greek state's determination to give visual and institutional continuity to the link between ancient and modern Greece",
            "The Greek diaspora's scholarly tradition — including the Greek scholars who had maintained Hellenic learning through the Ottoman period in Constantinople and Venice — created the intellectual community that provided the Academy's first members and defined its scholarly programme"
        ],
        "effects": [
            "The Academy of Athens's Modern Greek Language Dictionary — the authoritative scholarly record of the Greek language — has established the standards of modern Greek orthography, vocabulary, and usage, making the Academy the guardian of the Greek language's scholarly tradition",
            "The Academy's research in Byzantine studies — preserving and publishing Byzantine manuscripts, iconographic traditions, and historical records — has made Athens the primary international centre for Byzantine civilisation scholarship, connecting modern Greece to its medieval Christian heritage",
            "The Academy of Athens Building's symbolic power — with its marble statues of Plato and Socrates flanking the entrance, and its fresco of the Muses on the ceiling — has made it the most powerful visual statement of modern Greece's claim to continuity with classical antiquity",
            "The Academy's international scholarly connections — including reciprocal agreements with national academies across Europe, the US, and China — have given Greek scholarship a formal network of international academic recognition disproportionate to Greece's size"
        ],
        "relationships": [
            {"entity": "Plato's Academy (founded c.387 BCE, Athens)", "relationship": "NAMED_FOR_AND_INSTITUTIONAL_HEIR_OF", "note": "The Academy of Athens (1926) is named for Plato's original Academy (c.387 BCE) — the oldest named academy in Western philosophy — claiming institutional continuity with the classical tradition"},
            {"entity": "Academy of Athens Building (Theophil Hansen, 1885)", "relationship": "HOUSED_IN_THE_MAGNIFICENT", "note": "The Academy of Athens Building — one of the finest neoclassical buildings in the world — was designed by Theophil Hansen as part of the 'Athens Trilogy' with the National Library and University"},
            {"entity": "Athens Trilogy (Hansen buildings)", "relationship": "CENTRAL_ELEMENT_OF_THE", "note": "The Academy, National Library, and University of Athens form the 'Athens Trilogy' — the architectural ensemble expressing modern Greece's institutional claim to classical heritage"},
            {"entity": "Byzantine studies (Greek scholarly tradition)", "relationship": "PRIMARY_INSTITUTIONAL_CENTRE_FOR", "note": "The Academy's Byzantine studies research has made Athens the international centre for Byzantine civilisation scholarship"},
            {"entity": "Modern Greek language (authoritative dictionary)", "relationship": "GUARDIAN_OF_THE_SCHOLARLY_STANDARDS_OF_THE", "note": "The Academy's Modern Greek Language Dictionary establishes the authoritative scholarly standards for modern Greek orthography and usage"}
        ],
    }),

    ("academy-of-sciences-of-the-ussr", {
        "summary": (
            "The Academy of Sciences of the USSR (Академия наук СССР, est. 1724, Saint Petersburg — founded by Peter the Great; reorganised as Soviet Academy 1925; continued as Russian Academy of Sciences from 1991) was the supreme scientific institution of the Soviet Union — the organisation that directed Soviet scientific research, trained Soviet scientists, and produced the scientific achievements that gave the USSR its superpower status: the Soviet atomic bomb (1949), the first Earth satellite Sputnik (1957), the first human spaceflight (Yuri Gagarin, 1961), and the Soviet nuclear arsenal.\n\n"
            "The Academy was founded by Peter the Great (1724) as part of his Westernisation programme — modelled on the academies of Paris, London, and Berlin — and brought to Russia the German and Swiss mathematicians (Euler, Bernoulli, Goldbach) and astronomers whose work put Russia on the European scientific map. The Academy's early decades were dominated by foreign scholars; by the 19th century it had become a Russian institution, producing Mendeleev (periodic table), Pavlov (Nobel 1904, conditioned reflexes), and Lobachevsky (non-Euclidean geometry).\n\n"
            "The Soviet restructuring of the Academy (1925) — making it the directing institution of all Soviet scientific research — turned it into a mobilised scientific-industrial organisation rather than a free learned society. The Stalinist purges killed some of its greatest scientists (Nikolai Vavilov, plant geneticist, starved to death in prison 1943) while also driving the extraordinary wartime mobilisation that produced Soviet nuclear and aerospace achievements."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Supreme scientific institution of USSR (est. 1724, Peter the Great; Soviet restructuring 1925; Russian Academy of Sciences from 1991); produced Soviet atomic bomb (1949), Sputnik (1957), Gagarin spaceflight (1961); brought Euler, Bernoulli, Goldbach to Russia; Mendeleev (periodic table), Pavlov (Nobel 1904); Stalinist purges killed Nikolai Vavilov (starved in prison, 1943); directed all Soviet scientific research; superpower-enabling institution.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Peter the Great's determination to modernise Russia through Western science — and his decision to create a scientific academy that would bring European mathematicians and astronomers to Russia — drove the founding of the Academy (1724) as the institutional vehicle for Russia's scientific Westernisation",
            "The Soviet state's recognition that scientific and technological capability was the foundation of military and industrial power — the 'science = socialism = victory' equation — drove the 1925 reorganisation of the Academy into the directing institution of all Soviet research",
            "The Cold War's transformation of science into a geopolitical competition — with each superpower's scientific achievements (atomic bomb, space race, nuclear missiles) as measures of systemic superiority — gave the Soviet Academy its extraordinary resources and political priority"
        ],
        "effects": [
            "The Soviet Academy's Manhattan Project equivalent — the Soviet atomic bomb programme (Project First Lightning) — produced the first Soviet nuclear test (1949, Joe 1) and was the foundational achievement that established the USSR as a nuclear superpower, ending the US monopoly and beginning the Cold War nuclear arms race",
            "Sputnik (4 October 1957) — the first artificial Earth satellite, a product of Academy-directed space research — triggered the Space Race and the US response (NASA founding, National Defense Education Act) that fundamentally reshaped American science, education, and defence priorities",
            "The Academy's research in theoretical physics — through the Landau school (Lev Landau, Nobel 1962), the Tamm-Sakharov group (hydrogen bomb), and Bogoliubov's quantum field theory — made Soviet theoretical physics competitive with Western physics throughout the Cold War, with Soviet contributions in condensed matter, plasma physics, and quantum mechanics",
            "Andrei Sakharov's trajectory — from Soviet hydrogen bomb designer to nuclear disarmament activist and human rights campaigner — and his eventual exile (1980) and return (1987) represents the Academy's most dramatic case of the tension between the Soviet state's instrumental use of science and individual scientists' moral agency"
        ],
        "relationships": [
            {"entity": "Peter the Great (founding patron)", "relationship": "FOUNDED_BY", "note": "Peter the Great founded the Academy (1724) to bring European science to Russia — part of his Westernisation programme, bringing Euler, Bernoulli, and other European scholars to St. Petersburg"},
            {"entity": "Soviet atomic bomb (1949, Joe 1)", "relationship": "INSTITUTIONAL_FRAMEWORK_FOR_THE_DEVELOPMENT_OF_THE", "note": "The Academy's mobilised research programme produced the Soviet atomic bomb (1949) — ending the US nuclear monopoly and establishing the USSR as a nuclear superpower"},
            {"entity": "Sputnik (1957, first artificial satellite)", "relationship": "INSTITUTIONAL_HOME_OF_THE_RESEARCH_THAT_PRODUCED", "note": "Sputnik (1957) — the most geopolitically significant scientific achievement of the 20th century — was a product of Academy-directed Soviet space research"},
            {"entity": "Andrei Sakharov (hydrogen bomb designer turned dissident)", "relationship": "EXPELLED_ITS_MOST_FAMOUS_DISSIDENT_MEMBER", "note": "Sakharov's trajectory from hydrogen bomb designer to human rights activist — and his Academy exile (1980) — represents the tension between Soviet scientific mobilisation and individual moral agency"},
            {"entity": "Nikolai Vavilov (plant geneticist, Stalinist victim)", "relationship": "MOST_FAMOUS_STALINIST_VICTIM_FROM", "note": "Nikolai Vavilov — the world's greatest plant geneticist — was arrested on Lysenko's denunciation and starved to death in prison (1943), representing the Academy's darkest Stalinist chapter"}
        ],
    }),

    ("pontifical-academy-of-sciences", {
        "summary": (
            "The Pontifical Academy of Sciences (Pontificia Academia Scientiarum, est. 1936, Vatican City — successor to the Accademia dei Lincei, 1603, and the Pontificia Accademia dei Nuovi Lincei, 1847) is the scientific academy of the Holy See — an international body of 80 appointed scientists (independent of nationality or religion) that advises the Pope and the Roman Catholic Church on scientific questions and promotes the free investigation of science and the relationship between science and faith. The Academy's membership has included 39 Nobel laureates.\n\n"
            "The Pontifical Academy of Sciences descends from the Accademia dei Lincei — the world's first modern scientific academy, founded in Rome in 1603 (Galileo was a member from 1611) — making it the institutional descendant of the organisation that published Galileo's telescopic observations and was eventually suppressed after his condemnation. This historical irony — that the institution that succeeded the body that witnessed Galileo's persecution now advocates for science and faith reconciliation — gives the Academy a particularly resonant symbolic history.\n\n"
            "The Academy's political significance has grown under John Paul II and Francis, who have used it as the vehicle for major Vatican statements on evolution (acceptance, 1996), climate change (2015 statement supporting the Paris Agreement), and nuclear disarmament. Pope Francis's 2015 statement on climate change — drawing on Academy scientific advice — was one of the most significant religious declarations on environmental policy in history."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Holy See's scientific academy (est. 1936); successor to Accademia dei Lincei (1603, world's first modern scientific academy — Galileo was member); 80 appointed scientists (39 Nobel laureates); no nationality/religion requirements; John Paul II acceptance of evolution (1996); Francis's climate change statement (2015, informed by Academy — supporting Paris Agreement); institutional heir of body that witnessed Galileo's persecution.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Catholic Church's need to demonstrate compatibility between scientific investigation and religious faith — especially after the Galileo affair's long shadow — drove the creation of an authoritative scientific advisory body that could provide credible scientific input to Vatican policy",
            "Pope Pius XI's recognition (1936) that the Church needed an international, non-sectarian scientific advisory body — with members chosen purely on scientific merit regardless of nationality or religion — created the Academy's distinctive secular-scientific identity within a religious institutional context",
            "The Accademia dei Lincei's suppression after Galileo's condemnation (1630s) and the Church's desire to reconnect with its founding tradition of scientific patronage drove the institutional lineage that led from the Lincei to the successive pontifical academies"
        ],
        "effects": [
            "Pope John Paul II's statement accepting evolution (1996) — delivered through the Academy — was the most significant Catholic pronouncement on Darwinian theory since the Modernist controversy, effectively ending the Church's institutional opposition to evolutionary biology and establishing that faith and evolution were compatible",
            "The Academy's 'Casina Pio IV' venue — the 16th-century Villa Pia in the Vatican Gardens — has become the site where leading scientists from around the world meet with Vatican officials, creating a unique physical space where scientific authority and religious authority interact",
            "Pope Francis's encyclical Laudato Si' (2015) — on care for the environment and climate change — drew heavily on Academy scientific advice and was the most significant religious document on climate change produced by any major institution, influencing the Paris Agreement negotiations",
            "The Academy's 39 Nobel laureate members — including Max Planck, Niels Bohr, Erwin Schrödinger, and Otto Hahn among historical members — have given the Catholic Church's scientific advisory body intellectual credibility that few national academies can match"
        ],
        "relationships": [
            {"entity": "Accademia dei Lincei (1603, world's first modern scientific academy)", "relationship": "INSTITUTIONAL_SUCCESSOR_TO_THE", "note": "The Pontifical Academy descends from the Accademia dei Lincei (1603) — the world's first modern scientific academy, of which Galileo was a member from 1611"},
            {"entity": "Pope John Paul II (evolution acceptance, 1996)", "relationship": "VEHICLE_FOR_JOHN_PAUL_IIS_ACCEPTANCE_OF_EVOLUTION_STATEMENT_BY", "note": "John Paul II's 1996 statement accepting Darwinian evolution — delivered through the Academy — was the most significant Catholic pronouncement on evolution since the Modernist controversy"},
            {"entity": "Laudato Si' (Pope Francis, 2015) and Paris Agreement", "relationship": "PROVIDED_SCIENTIFIC_FOUNDATION_FOR", "note": "Academy scientific advice informed Laudato Si' (2015) — the most significant religious document on climate change — which influenced the Paris Agreement negotiations"},
            {"entity": "Galileo Galilei (Accademia dei Lincei member, 1611)", "relationship": "INSTITUTIONAL_HEIR_OF_THE_ACADEMY_THAT_WITNESSED_PERSECUTION_OF", "note": "The historical irony that the Academy descends from the body that witnessed Galileo's persecution gives it resonant symbolic significance in science-faith relations"},
            {"entity": "Nobel Prize laureates (39 members over history)", "relationship": "MEMBERSHIP_INCLUDES_39", "note": "39 Nobel laureates — including Planck, Bohr, Schrödinger — have been Pontifical Academy members, giving it intellectual credibility matching the leading national academies"}
        ],
    }),

    ("royal-swedish-academy-of-sciences", {
        "summary": (
            "The Royal Swedish Academy of Sciences (Kungliga Vetenskapsakademien, est. 1739, Stockholm — founded by Linnaeus and four others) is the academy that awards the Nobel Prize in Physics and the Nobel Prize in Chemistry — the two most prestigious prizes in natural science — and is therefore, alongside the Swedish Academy (Literature) and the Norwegian Nobel Committee (Peace), the institution that defines the global canon of scientific achievement. The Royal Swedish Academy of Sciences has shaped the international recognition of scientific excellence for 120+ years.\n\n"
            "The Academy was founded in 1739 by Carl Linnaeus (father of modern taxonomy), together with four other natural scientists, as an explicitly practical institution — focused on the natural sciences in their application to Swedish economic development, distinct from the humanistic Royal Swedish Academy (which would later become the Swedish Academy). The Linnaean founding gave the Academy an empiricist, applied-science identity that distinguished it from the more courtly European academies. The Academy's journal, Acta Philosophica Suecica (later Acta Mathematica and other publications), was among the first peer-reviewed scientific journals.\n\n"
            "The Nobel Prize in Physics and Chemistry selection process — conducted annually by Nobel Committees appointed from the Academy — involves the most rigorous peer evaluation in science: thousands of nominations, multi-year expert reviews, and decisions that can take decades to recognise work whose significance has only become apparent in retrospect."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Awards Nobel Prize in Physics and Nobel Prize in Chemistry (since 1901); most prestigious natural science prizes in world; founded by Carl Linnaeus (1739); Linnaean empiricist applied-science founding identity; Nobel Committee selection — most rigorous peer evaluation in science; thousands of nominations, multi-year reviews; alongside Swedish Academy (Literature) and Norwegian Nobel Committee (Peace) defines global canon of scientific achievement.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Carl Linnaeus's founding vision — creating a practical academy focused on the natural sciences in their application to Swedish economic development — drove the establishment of the Royal Swedish Academy of Sciences (1739) with an empiricist, applied-science identity",
            "Alfred Nobel's will (1895) — designating the Royal Swedish Academy as the institution to award prizes in Physics and Chemistry — gave the Academy its global significance, transforming a Swedish national institution into the supreme arbiter of international scientific achievement",
            "The Academy's practical orientation and its tradition of recognising empirical scientific work — rather than the courtly humanistic traditions of other European academies — made it the natural choice for Nobel's prizes in the 'hard sciences'"
        ],
        "effects": [
            "The Nobel Prize in Physics (awarded since 1901) — recognising work from X-rays (Röntgen, 1901) to nuclear structure (Bohr, 1922), relativity implications (Einstein, 1921), quantum mechanics (Heisenberg, 1932), DNA repair (2015), gravitational waves (2017), and black holes (2020) — has defined the most important discoveries in physics history",
            "The Nobel Prize in Chemistry (awarded since 1901) — from the synthesis of organic compounds (Fischer, 1902) to radioactivity (Rutherford, 1908), chemical thermodynamics (Nernst, 1920), DNA structure elucidation (chemical contributions), and CRISPR (2020) — has defined the most important discoveries in chemistry history",
            "The Academy's Nobel selection decisions — and their occasional controversies (not awarding Lise Meitner for nuclear fission, not awarding Jocelyn Bell Burnell for pulsars, not awarding Fred Hoyle for stellar nucleosynthesis) — have generated as much scientific debate as the awards themselves, making the Nobel selection the primary site of debate about what constitutes fundamental scientific contribution",
            "The Linnaean tradition embedded in the Academy's founding — the empiricist, applied-science, biodiversity-focused approach that Linnaeus established — has given Sweden a disproportionate presence in international biology and ecology, from Linnaeus through Arrhenius (greenhouse effect) to Carleson (wavelet analysis)"
        ],
        "relationships": [
            {"entity": "Carl Linnaeus (founder and first member)", "relationship": "FOUNDED_BY", "note": "Linnaeus co-founded the Academy (1739) — his empiricist, applied-science vision gave it the practical identity that made it the natural home for Nobel's physics and chemistry prizes"},
            {"entity": "Nobel Prize in Physics (since 1901)", "relationship": "AWARDS_THE_ANNUAL", "note": "The Nobel Prize in Physics — the most prestigious prize in natural science — has been awarded by the Royal Swedish Academy since 1901"},
            {"entity": "Nobel Prize in Chemistry (since 1901)", "relationship": "AWARDS_THE_ANNUAL", "note": "The Nobel Prize in Chemistry has been awarded by the Royal Swedish Academy since 1901, defining the most important discoveries in chemistry history"},
            {"entity": "Alfred Nobel (will, 1895)", "relationship": "DESIGNATED_AS_PHYSICS_AND_CHEMISTRY_PRIZE_AWARDER_BY", "note": "Alfred Nobel's will designated the Royal Swedish Academy to award the Physics and Chemistry prizes — giving the Academy its global significance"},
            {"entity": "CRISPR Nobel Prize in Chemistry (2020, Doudna & Charpentier)", "relationship": "AWARDED_THE_TRANSFORMATIVE_CRISPR_PRIZE_TO", "note": "The 2020 Nobel Prize in Chemistry for CRISPR — awarded by the Royal Swedish Academy — recognised the most consequential biotechnology development since the discovery of DNA structure"}
        ],
    }),

    ("royal-society-of-edinburgh", {
        "summary": (
            "The Royal Society of Edinburgh (RSE, est. 1783, Edinburgh — founded by royal charter of George III) is Scotland's national academy and one of the leading learned societies in the world — the intellectual centre of the Scottish Enlightenment's institutional legacy and home to the tradition that produced Adam Smith, David Hume, James Watt, Joseph Black, and James Hutton. The RSE's founding in 1783 marked the institutionalisation of the Scottish Enlightenment — that extraordinary intellectual movement of the 18th century that gave the modern world economics, sociology, geology, thermodynamics, and the steam engine.\n\n"
            "The Royal Society of Edinburgh emerged from the 'Select Society' (1754) and the 'Philosophical Society of Edinburgh' — the informal networks through which the Scottish Enlightenment philosophers and scientists had been meeting. Its founding members included Adam Smith (The Wealth of Nations, 1776), Joseph Black (discoverer of carbon dioxide and latent heat), James Hutton (father of modern geology), William Robertson (historian), and Dugald Stewart (philosopher). This founding cohort represents the highest concentration of intellectual talent in any academy's founding membership in history.\n\n"
            "The RSE's continued significance as Scotland's national academy — its role in advocating for Scottish universities, Scottish science policy, and Scottish economic development — gives it relevance beyond its historical founding prestige."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Scotland's national academy (est. 1783, royal charter George III); institutional legacy of the Scottish Enlightenment; founding members: Adam Smith (Wealth of Nations), Joseph Black (CO₂ and latent heat), James Hutton (geology), William Robertson, Dugald Stewart; highest concentration of intellectual talent in any academy's founding membership; institutionalised the Enlightenment tradition that gave the world economics, sociology, geology, thermodynamics.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Scottish Enlightenment's informal networks (Select Society, 1754; Philosophical Society) had produced the intellectual revolution that gave the world The Wealth of Nations, the history of civil society, and the theory of the Earth — but lacked a permanent institutional home that could carry the tradition forward",
            "George III's royal charter (1783) — motivated by Scotland's desire for an institution comparable to the Royal Society of London that could represent Scottish intellectual achievement — created the RSE as Scotland's national academy",
            "The convergence in Edinburgh during the Enlightenment of Adam Smith's economics, Hutton's geology, Black's chemistry, and Hume's philosophy created the most productive intellectual environment in any European city — an environment the RSE was designed to institutionalise and continue"
        ],
        "effects": [
            "The RSE's institutionalisation of the Scottish Enlightenment tradition — maintaining continuous scholarly meetings, publishing the Transactions of the Royal Society of Edinburgh (from 1788), and electing Scotland's leading scholars — preserved the Enlightenment's interdisciplinary, empiricist tradition through the 19th and 20th centuries",
            "The RSE's founding tradition — combining natural philosophy, social science, economics, and humanities in a single institution — was the model for the interdisciplinary learned societies that emerged across Europe in the late 18th and early 19th centuries",
            "The RSE's role in Scottish science policy — including its advocacy for Scottish universities, research funding, and educational investment — has given it continuing influence on Scottish intellectual and economic development beyond its historical founding prestige",
            "The RSE's tradition of electing scientists, engineers, and humanists together — reflecting the Scottish Enlightenment's integration of natural and moral philosophy — has maintained the cross-disciplinary identity that distinguishes it from more specialised learned societies"
        ],
        "relationships": [
            {"entity": "Adam Smith (founding member)", "relationship": "INSTITUTIONALISED_THE_TRADITION_OF", "note": "Adam Smith — whose Wealth of Nations (1776) founded modern economics — was among the RSE's founding members, making the Academy the institutional home of his intellectual tradition"},
            {"entity": "James Hutton (father of modern geology)", "relationship": "FOUNDING_MEMBER_WHOSE_WORK_WAS_PRESENTED_TO_THE", "note": "James Hutton presented his Theory of the Earth to the RSE (1785) — one of the most important scientific presentations in history, founding modern geology"},
            {"entity": "Joseph Black (discoverer of carbon dioxide and latent heat)", "relationship": "FOUNDING_MEMBER_WHOSE_CHEMICAL_DISCOVERIES_WERE_CENTRAL_TO_THE", "note": "Joseph Black's discoveries of carbon dioxide and latent heat — among the most consequential 18th-century chemistry achievements — were developed in the milieu that produced the RSE"},
            {"entity": "Scottish Enlightenment (18th century)", "relationship": "INSTITUTIONAL_LEGACY_AND_EMBODIMENT_OF_THE", "note": "The RSE institutionalised the Scottish Enlightenment — the intellectual movement that gave the modern world economics, sociology, geology, and thermodynamics"},
            {"entity": "Royal Society of London (est. 1660)", "relationship": "SCOTTISH_NATIONAL_ACADEMY_COUNTERPART_TO_THE", "note": "The RSE was created partly as Scotland's counterpart to the Royal Society of London — representing Scottish intellectual achievement in parallel with the English academy"}
        ],
    }),

    ("linnean-society-of-london", {
        "summary": (
            "The Linnean Society of London (est. 1788, London — founded by Sir James Edward Smith, who purchased Carl Linnaeus's collections) is the world's oldest active biological society and the institution that holds the original collections and manuscripts of Carl Linnaeus — including the pressed plant specimens, insects, fish, and letters that form the foundation of modern biological nomenclature. The Linnean Society is also the institution where Charles Darwin and Alfred Russel Wallace first publicly presented the theory of natural selection (1 July 1858).\n\n"
            "The Society was founded by James Edward Smith, who purchased Linnaeus's entire collection (plants, animals, minerals, books, and correspondence) from Linnaeus's widow in 1784 — rescuing them from Sweden after the Swedish government failed to act quickly enough. Smith brought them to London, where the Linnean Society was established (1788) to house and develop Linnaeus's legacy. The Society's possession of Linnaeus's type specimens — the definitive physical examples against which all species names are validated — makes it the most important repository for biological nomenclature in the world.\n\n"
            "The joint Darwin-Wallace paper on natural selection — presented to the Linnean Society on 1 July 1858 — is the most important scientific presentation in the Society's history and one of the most consequential meetings in the history of science: the first public announcement of the theory that explains the origin of species."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's oldest active biological society (est. 1788); holds original Linnaeus collections (pressed specimens, insects, fish, manuscripts, correspondence) — foundation of biological nomenclature; James Edward Smith purchased Linnaeus's collections from widow (1784) bringing them to London; Darwin-Wallace joint paper on natural selection presented here (1 July 1858) — first public announcement of evolutionary theory; Linnaeus's type specimens — most important nomenclature repository in world.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "James Edward Smith's purchase of Linnaeus's entire collection (1784) — rescuing them from Sweden after the Swedish government's failure to act quickly enough — created the physical foundation for the Linnean Society, giving it the most important biological collection in the world",
            "The growth of the Linnaean classification system as the universal language of biology — making Linnaeus's original specimens the authoritative type specimens against which all species names must be validated — gave the Society's collection irreplaceable scientific importance",
            "The London scientific community's need for a dedicated biological learned society — distinct from the Royal Society's broader natural philosophy — drove the founding of a specialist institution that could focus on the systematic and taxonomic traditions that Linnaeus had established"
        ],
        "effects": [
            "The Society's hosting of the Darwin-Wallace joint paper (1 July 1858) — 'On the Tendency of Species to form Varieties; and on the Perpetuation of Varieties and Species by Natural Means of Selection' — was the most consequential scientific presentation of the 19th century, first announcing the theory of natural selection",
            "The Linnean Society's custody of Linnaeus's type specimens — the physical foundation of biological nomenclature — makes it the ultimate arbiter of species names, a function it continues to exercise in the resolution of taxonomic disputes 230 years after its founding",
            "The Society's Biological Journal of the Linnean Society and Botanical Journal of the Linnean Society are among the oldest continuously published scientific journals, providing the publication venue for 230 years of biological systematic research",
            "The Society's Darwin-Wallace commemoration tradition — and its physical possession of the 1858 papers — has made it the primary institutional site of Darwin scholarship and evolutionary biology history, attracting researchers from around the world"
        ],
        "relationships": [
            {"entity": "Carl Linnaeus (collections founder)", "relationship": "CUSTODIAN_OF_THE_COMPLETE_COLLECTIONS_OF", "note": "The Society holds Linnaeus's complete collections — pressed specimens, insects, fish, minerals, books, and 3,000 letters — the physical foundation of biological nomenclature"},
            {"entity": "Darwin-Wallace joint paper on natural selection (1 July 1858)", "relationship": "VENUE_OF_THE_FIRST_PUBLIC_PRESENTATION_OF", "note": "The joint Darwin-Wallace paper on natural selection was first presented to the Linnean Society (1858) — the most important scientific presentation of the 19th century"},
            {"entity": "Charles Darwin (On the Origin of Species, 1859)", "relationship": "INSTITUTIONAL_HOME_FOR_THE_FIRST_ANNOUNCEMENT_OF_THE_THEORY_OF", "note": "Darwin presented his natural selection theory here (1858) before the publication of On the Origin of Species (1859)"},
            {"entity": "Biological nomenclature (type specimens)", "relationship": "PRIMARY_CUSTODIAN_OF_THE_TYPE_SPECIMENS_FOUNDATIONAL_TO", "note": "The Society's Linnaeus type specimens — the physical examples against which all species names are validated — make it the most important nomenclature repository in the world"},
            {"entity": "Alfred Russel Wallace (co-discoverer of natural selection)", "relationship": "CO-PRESENTED_NATURAL_SELECTION_THEORY_ALONGSIDE_DARWIN_TO", "note": "Wallace's letter from Ternate — describing his independently derived theory of natural selection — was read alongside Darwin's paper at the Linnean Society (1858)"}
        ],
    }),

    ("geological-society-of-london", {
        "summary": (
            "The Geological Society of London (est. 1807, London — the world's oldest geological society) is the primary international geological learned society — the institution that founded the science of geology as a professional discipline, established the Geological Time Scale (the naming and definition of the geological periods from Cambrian to Quaternary), and published the foundational works of Charles Lyell, William Buckland, Roderick Murchison, and Adam Sedgwick. The Geological Society's Quarterly Journal is the longest continuously published Earth science journal in the world.\n\n"
            "The Geological Society was founded in 1807 by 13 gentlemen at the Freemasons' Tavern, London — the same year that James Hutton's theory of deep time was being consolidated into the foundational principle of modern geology. The Society's first decades saw the 'Great Devonian Controversy' (the debate over the Devonian and Silurian periods that established the method of resolving geological disputes through stratigraphic evidence), and the work of William Smith ('Strata' Smith) — who created the first geological map of England and Wales (1815) and demonstrated that geological strata could be correlated by their fossil contents.\n\n"
            "The Society's defining contribution was establishing the Geological Time Scale — the sequence of geological periods whose names (Cambrian, Ordovician, Silurian, Devonian, Carboniferous, Permian, Triassic, Jurassic, Cretaceous, Paleogene, Neogene, Quaternary) are the universal scientific language for Earth's 4.5-billion-year history."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's oldest geological society (est. 1807); founded geology as professional discipline; established Geological Time Scale (Cambrian through Quaternary — universal language of Earth's 4.5 billion year history); William Smith's first geological map of England and Wales (1815, strata correlated by fossils); Charles Lyell (Principles of Geology), Murchison (Silurian), Sedgwick (Cambrian); Quarterly Journal — longest continuously published Earth science journal.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The late 18th-century acceleration of mining, canal construction, and agricultural improvement in Britain — creating demand for understanding rock strata and their economic implications — drove the professionalisation of geology and the founding of an institution to organise geological knowledge",
            "James Hutton's theory of deep time (1788) and his demonstration that Earth's history required millions of years — combined with the stratigraphic work of William Smith — created the conceptual framework that needed an institutional home for its development and dissemination",
            "The London scientific community's recognition that geology — as a rapidly growing empirical science distinct from natural philosophy — needed its own learned society, separate from the Royal Society, to develop the specialised methods and vocabulary of the new discipline"
        ],
        "effects": [
            "The Geological Society's establishment of the Geological Time Scale — the naming and definition of geological periods from Cambrian to Quaternary — created the universal scientific language for Earth's history that all subsequent Earth science research uses, making it the most consequential institutional contribution to the vocabulary of natural science",
            "Charles Lyell's Principles of Geology (1830–1833) — developed and presented through the Geological Society — established uniformitarianism (the principle that geological processes were the same in the past as in the present) as the foundation of modern geology, directly influencing Darwin's development of evolutionary theory through deep time",
            "William Smith's geological map of England and Wales (1815) — the first national geological map — demonstrated that rock strata could be correlated by their fossil contents, establishing biostratigraphy and creating the foundation for the British coal, iron, and mineral extraction industries",
            "The Society's 'Great Devonian Controversy' (1830s–1840s) — the dispute between Murchison and Sedgwick that established the Devonian and Silurian periods — developed the methodological norms of geological dispute resolution through stratigraphic evidence, establishing the standards of geological argument still in use today"
        ],
        "relationships": [
            {"entity": "William Smith ('Strata' Smith)", "relationship": "PUBLISHED_THE_FOUNDATIONAL_GEOLOGICAL_MAP_THROUGH_THE", "note": "William Smith's first geological map (1815) — showing how strata can be correlated by fossil contents — was the most practically consequential geological work produced in the Society's early period"},
            {"entity": "Charles Lyell (Principles of Geology, 1830–1833)", "relationship": "PUBLICATION_VENUE_AND_INTELLECTUAL_HOME_FOR", "note": "Lyell developed and presented his Principles of Geology (1830–1833) through the Society — establishing uniformitarianism as the foundation of modern geology"},
            {"entity": "Geological Time Scale (Cambrian through Quaternary)", "relationship": "ESTABLISHED_THE", "note": "The Society's defining institutional contribution was establishing the Geological Time Scale — the universal scientific language for Earth's 4.5-billion-year history"},
            {"entity": "Charles Darwin (evolutionary theory, deep time)", "relationship": "LYELL'S UNIFORMITARIANISM (DEVELOPED THROUGH THE SOCIETY) DIRECTLY INFLUENCED", "note": "Lyell's Principles of Geology — developed through the Geological Society — directly influenced Darwin's concept of deep time as the framework for evolutionary change"},
            {"entity": "Roderick Murchison and Adam Sedgwick (Great Devonian Controversy)", "relationship": "SITE_OF_THE_METHODOLOGICALLY_FOUNDATIONAL", "note": "The Great Devonian Controversy (1830s–1840s) — resolved by stratigraphic evidence — established the methodological norms of geological dispute resolution still in use today"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 32 — {len(ENTITIES)} entities (Class 351: Major Academies of Science & Learned Societies)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
