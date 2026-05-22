#!/usr/bin/env python3
"""
Batch 33 — 8 entities (Class 352): Research Centers & National Laboratories
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()
FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/352-Class-352"
FILE_PREFIX = "352"


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

    ("ames-research-center", {
        "summary": (
            "NASA Ames Research Center (est. 1939, Moffett Field, California — founded by NACA as Ames Aeronautical Laboratory) is one of NASA's 10 field centres and one of the world's leading research institutions for aerospace, astrobiology, supercomputing, and human factors research. Located at the heart of Silicon Valley, Ames has been the bridge between NASA's aeronautics mission and the technology ecosystem that gave birth to the digital economy — its proximity to Stanford, Berkeley, and the emerging tech industry made it a crucial node in the knowledge networks that produced Silicon Valley's technological culture.\n\n"
            "Ames was founded (1939) as the second laboratory of the National Advisory Committee for Aeronautics (NACA) — the precursor to NASA — to focus on wind tunnel aerodynamics research that would improve American military aircraft during World War II. Ames wind tunnels set the standards for American fighter and bomber design. After NASA's founding (1958), Ames became the centre for re-entry physics — developing the heat shields that protected Apollo astronauts during atmospheric re-entry — and for planetary science, managing the Pioneer and Galileo missions.\n\n"
            "Ames's contemporary significance spans three domains: the NASA Advanced Supercomputing Division (home of the Pleiades supercomputer, one of the world's most powerful scientific computers), the NASA Astrobiology Institute (leading the search for life in the universe), and its role as the technical partner for NASA's Commercial Crew and Commercial Cargo programmes — connecting NASA to the SpaceX and Boeing partnerships that have reshaped space access."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "NASA field centre (est. 1939, NACA Ames Aeronautical Laboratory); wind tunnels set WWII American fighter/bomber standards; Apollo re-entry heat shields; Pioneer and Galileo planetary missions; NASA Advanced Supercomputing Division (Pleiades supercomputer); NASA Astrobiology Institute; Silicon Valley bridge between NASA and tech ecosystem; Commercial Crew/Cargo partner (SpaceX/Boeing).",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The US military's urgent need for wind tunnel facilities to test and improve American fighter and bomber aircraft in preparation for potential involvement in World War II drove NACA to establish a second laboratory (1939) — at Moffett Field, near Stanford, with superior Bay Area climate for year-round aeronautical testing",
            "The California location — near Stanford and Berkeley, and on land shared with the US Navy's Moffett Field airship base — created the institutional environment that linked NACA/NASA research to California's emerging technology ecosystem",
            "NASA's post-Apollo reorientation toward planetary science, aeronautics, and computational research gave Ames a distinctive identity within the NASA system — focused on fundamental research and new mission concepts rather than the launch operations of Kennedy or Marshall"
        ],
        "effects": [
            "Ames's development of ablative heat shield technology for the Apollo Command Module — based on research into atmospheric re-entry physics in Ames wind tunnels — was the critical engineering breakthrough that made safe lunar mission return possible, directly enabling the Apollo programme's success",
            "The Pioneer 10 and Pioneer 11 spacecraft (Ames-managed) — the first spacecraft to pass through the asteroid belt and fly by Jupiter and Saturn — established NASA's planetary exploration programme and are the first human-made objects to leave the solar system",
            "Ames's proximity to and collaboration with Silicon Valley — including its role in the development of early computing and networking technology, and its hosting of NASA's computational infrastructure — made it a node in the knowledge networks that produced the internet, GPS, and digital computing",
            "The NASA Astrobiology Institute (headquartered at Ames) — coordinating global research on the origin and evolution of life — has made Ames the centre of one of the most profound scientific questions: whether life exists elsewhere in the universe"
        ],
        "relationships": [
            {"entity": "NACA (National Advisory Committee for Aeronautics)", "relationship": "FOUNDED_AS_SECOND_LABORATORY_OF", "note": "Ames was founded (1939) as NACA's second wind tunnel facility — focused on aerodynamics research for American military aircraft"},
            {"entity": "Apollo programme (re-entry heat shields)", "relationship": "PROVIDED_CRITICAL_HEAT_SHIELD_TECHNOLOGY_FOR_THE", "note": "Ames's re-entry physics research produced the ablative heat shield technology that protected Apollo astronauts during atmospheric re-entry"},
            {"entity": "Pioneer 10 and Pioneer 11 spacecraft", "relationship": "MANAGED_THE", "note": "Ames managed Pioneer 10 and Pioneer 11 — the first spacecraft to pass through the asteroid belt and fly by Jupiter, and the first human-made objects leaving the solar system"},
            {"entity": "NASA Astrobiology Institute", "relationship": "HEADQUARTERS_OF_THE", "note": "The NASA Astrobiology Institute — coordinating global research on the origin and evolution of life — is headquartered at Ames"},
            {"entity": "Silicon Valley (technology ecosystem)", "relationship": "POSITIONED_AT_THE_HEART_OF_THE", "note": "Ames's location in Moffett Field — at the heart of Silicon Valley — made it a bridge between NASA's aerospace research and the technology ecosystem that produced the digital economy"}
        ],
    }),

    ("bhabha-atomic-research-centre", {
        "summary": (
            "Bhabha Atomic Research Centre (BARC, est. 1954, Mumbai, India — founded by Homi J. Bhabha as the Atomic Energy Establishment, Trombay) is India's primary nuclear research institution and the scientific organisation that developed India's nuclear weapons programme — producing India's first nuclear device ('Smiling Buddha', tested 18 May 1974) and the subsequent Pokhran-II tests (1998, 'Operation Shakti'). BARC's programme gave India membership in the exclusive nuclear weapons club and permanently transformed South Asian security dynamics.\n\n"
            "BARC was founded by Homi J. Bhabha — the charismatic physicist who convinced Nehru that nuclear science was essential for Indian development — and supported by Nehru's 'atoms for peace' vision that combined civilian nuclear power development with the technical infrastructure that could also support weapons capability. Bhabha's 'three-stage' nuclear programme (thorium-based) was designed for a country with limited uranium but vast thorium reserves, giving India a long-term energy strategy linked to its nuclear infrastructure.\n\n"
            "BARC's scientific and technological achievements span civilian and military domains: the Dhruva and CIRUS research reactors, nuclear power plant design, isotope production for medical use, food irradiation technology, and the nuclear weapons design that produced India's nuclear deterrent. BARC's 18,000 scientists and engineers make it one of the largest research organisations in Asia."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "India's primary nuclear research institution (est. 1954, Homi J. Bhabha); India's first nuclear device — 'Smiling Buddha' (18 May 1974, Pokhran); Pokhran-II 'Operation Shakti' (1998); gave India nuclear weapons status — transformed South Asian security; Nehru's 'atoms for peace' three-stage thorium programme; Dhruva and CIRUS reactors; 18,000 scientists — one of largest research organisations in Asia.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Homi J. Bhabha's vision — that nuclear science would drive Indian industrial development and give India great-power scientific credibility — combined with Nehru's enthusiasm for science as the instrument of national modernisation to create the institutional and political foundation for BARC",
            "The 1962 Sino-Indian War and China's first nuclear test (1964) — demonstrating that India's neighbour and rival had achieved nuclear weapons capability — dramatically accelerated India's determination to develop its own nuclear deterrent, giving BARC's weapons programme political urgency",
            "India's rejection of the Nuclear Non-Proliferation Treaty (NPT, 1968) as discriminatory — preserving the nuclear monopoly of the five permanent Security Council members — freed India from treaty constraints and enabled BARC to pursue the full nuclear weapons development programme"
        ],
        "effects": [
            "India's first nuclear test — 'Smiling Buddha' (18 May 1974, Pokhran, Rajasthan) — announced India as the world's sixth nuclear power and the first new nuclear state since the NPT (1968), permanently altering the global nuclear order and triggering Pakistan's determination to develop its own nuclear weapons",
            "The Pokhran-II tests (Operation Shakti, May 1998) — five tests including thermonuclear devices — confirmed India as a fully fledged nuclear weapons state, triggered the US sanctions, and prompted Pakistan's reciprocal Chagai tests (within weeks) — establishing the South Asian nuclear deterrent balance that continues to define regional security",
            "BARC's civilian nuclear power technology — including the CANDU-derived pressurised heavy water reactors that form India's nuclear power fleet — has contributed to India's energy security and established India as one of the few countries with a fully indigenous nuclear power capability from reactor design to fuel cycle",
            "Bhabha's three-stage thorium programme — designed to exploit India's vast thorium reserves as the long-term foundation of the nuclear power programme — remains India's strategic nuclear energy vision, with BARC continuing to develop thorium-based reactor technology"
        ],
        "relationships": [
            {"entity": "Homi J. Bhabha (founder and first director)", "relationship": "FOUNDED_AND_FIRST_DIRECTED_BY", "note": "Bhabha — India's most important nuclear scientist — founded BARC (1954) and designed the three-stage thorium programme that guides India's nuclear energy strategy"},
            {"entity": "Jawaharlal Nehru (political patron)", "relationship": "POLITICALLY_ENABLED_AND_CHAMPIONED_BY", "note": "Nehru's 'atoms for peace' vision and his close relationship with Bhabha gave BARC the political support and resources for its early development"},
            {"entity": "Smiling Buddha (India's first nuclear test, 18 May 1974)", "relationship": "SCIENTIFIC_INSTITUTION_THAT_DESIGNED_AND_PRODUCED_THE", "note": "BARC produced India's first nuclear device — 'Smiling Buddha' (1974) — announcing India as the world's sixth nuclear power"},
            {"entity": "Pokhran-II tests (Operation Shakti, May 1998)", "relationship": "PRODUCED_THE_THERMONUCLEAR_DEVICES_TESTED_IN", "note": "BARC's nuclear weapons designs were tested in the Pokhran-II series (1998) — confirming India as a fully fledged nuclear weapons state"},
            {"entity": "Pakistan's Chagai tests (1998)", "relationship": "NUCLEAR_TESTS_TRIGGERED_PAKISTAN'S_RECIPROCAL", "note": "India's Pokhran-II tests (1998) directly triggered Pakistan's Chagai nuclear tests (within weeks) — establishing South Asia's nuclear deterrent balance"}
        ],
    }),

    ("slac-national-accelerator-laboratory", {
        "summary": (
            "SLAC National Accelerator Laboratory (est. 1962, Menlo Park, California — Stanford Linear Accelerator Center, operated by Stanford University for the US Department of Energy) is one of the world's premier particle physics research facilities — home of the world's longest linear particle accelerator (3.2 km) and the site of Nobel Prize-winning discoveries in particle physics that reshaped the Standard Model of fundamental particles. SLAC's particle beam experiments demonstrated the quark structure of the proton — confirming the quark model of matter.\n\n"
            "SLAC's 3.2-kilometre linear accelerator — when completed in 1966, the world's largest linear accelerator — became the instrument for the SLAC-MIT deep inelastic scattering experiments (1967–1973) that revealed the proton's internal structure. These experiments — conducted by Jerome Friedman, Henry Kendall, and Richard Taylor — demonstrated that protons contained point-like constituents (quarks), earning the Nobel Prize in Physics (1990) and establishing the quark model as the physical reality underlying the Standard Model of particle physics.\n\n"
            "SLAC has generated 6 Nobel Prizes in Physics and has transformed multiple times: from an electron accelerator (1960s–1980s) to a synchrotron radiation facility (Stanford Synchrotron Radiation Lightsource — the world's first facility dedicated to synchrotron light) to the world's first hard X-ray free-electron laser (LCLS, 2009) — producing X-ray pulses a billion times brighter than conventional X-ray sources."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's longest linear accelerator (3.2 km, est. 1962, Menlo Park); SLAC-MIT deep inelastic scattering experiments (1967–1973) revealed quark structure of proton — Friedman, Kendall, Taylor Nobel Prize 1990; confirmed quark model — Standard Model foundation; 6 Nobel Prizes in Physics from SLAC; Stanford Synchrotron Radiation Lightsource (world's first dedicated synchrotron); LCLS (2009) — world's first hard X-ray free-electron laser.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The post-war American investment in large-scale particle accelerators — driven by the AEC and the scientific community's recognition that probing subnuclear structure required higher energies than existing accelerators could provide — drove the design and construction of SLAC's 3.2-km linear accelerator",
            "Stanford's strategic decision to build the largest linear accelerator in the world — rather than a synchrotron — gave SLAC a unique experimental tool that enabled the deep inelastic scattering experiments that revealed quark structure",
            "The Department of Energy's national laboratory system — concentrating large-scale scientific infrastructure at federally funded facilities operated by universities — created the institutional model for SLAC as a DOE national laboratory managed by Stanford"
        ],
        "effects": [
            "The SLAC-MIT deep inelastic scattering experiments (1967–1973) — revealing that protons contain point-like constituents (quarks) — are among the most consequential particle physics discoveries of the 20th century, confirming the quark model and establishing the experimental foundation for Quantum Chromodynamics (QCD)",
            "SLAC's discovery of the J/ψ particle (November 1974, simultaneously with BNL — the 'November Revolution' in particle physics) confirmed the existence of the charm quark and the correctness of the Standard Model — earning Burton Richter the 1976 Nobel Prize in Physics",
            "The Stanford Synchrotron Radiation Lightsource (SSRL) — the world's first dedicated synchrotron radiation facility — pioneered the use of synchrotron light for materials science, structural biology, and chemistry, enabling the determination of thousands of protein structures and establishing the field of structural genomics",
            "The LCLS (Linac Coherent Light Source, 2009) — the world's first hard X-ray free-electron laser — produces X-ray pulses a billion times brighter than conventional sources, enabling the filming of chemical reactions and protein dynamics in real time — a breakthrough for structural biology and chemistry"
        ],
        "relationships": [
            {"entity": "Quark model (Standard Model of particle physics)", "relationship": "PROVIDED_EXPERIMENTAL_CONFIRMATION_OF_THE_FUNDAMENTAL", "note": "SLAC's deep inelastic scattering experiments (1967–1973) confirmed that protons contain quarks — providing the experimental foundation for the Standard Model's quark sector"},
            {"entity": "Jerome Friedman, Henry Kendall, Richard Taylor (Nobel 1990)", "relationship": "SITE_OF_THE_EXPERIMENTS_THAT_WON", "note": "The SLAC-MIT deep inelastic scattering experiments — conducted at SLAC — earned Friedman, Kendall, and Taylor the 1990 Nobel Prize in Physics"},
            {"entity": "J/ψ particle discovery (November Revolution, 1974)", "relationship": "CO-SITE_OF_THE_SIMULTANEOUS_DISCOVERY_OF_THE", "note": "SLAC's simultaneous discovery of the J/ψ particle (with BNL, November 1974) confirmed the charm quark and the Standard Model — earning Richter the 1976 Nobel"},
            {"entity": "Stanford Synchrotron Radiation Lightsource (SSRL)", "relationship": "HOME_OF_THE_WORLD'S_FIRST_DEDICATED", "note": "SSRL — the world's first dedicated synchrotron radiation facility — pioneered synchrotron light for materials science and structural biology"},
            {"entity": "LCLS (Linac Coherent Light Source, 2009)", "relationship": "HOME_OF_THE_WORLD'S_FIRST_HARD_X-RAY_FREE-ELECTRON_LASER", "note": "LCLS (2009) — the world's first hard X-ray free-electron laser — produces X-ray pulses a billion times brighter than conventional sources"}
        ],
    }),

    ("university-of-copenhagen-niels-bohr-institute", {
        "summary": (
            "The Niels Bohr Institute (NBI, est. 1920, Copenhagen, Denmark — founded by Niels Bohr at the University of Copenhagen) is one of the most historically significant physics research institutes in the world — the birthplace of the Copenhagen Interpretation of quantum mechanics, the intellectual home of the foundational revolution in physics of the 1920s–1930s, and the institute that gathered Werner Heisenberg, Wolfgang Pauli, Paul Dirac, Erwin Schrödinger, Max Born, and Lise Meitner in the seminars that created modern quantum theory.\n\n"
            "Niels Bohr founded the Institute for Theoretical Physics (renamed the Niels Bohr Institute after his death in 1965) in 1920 — with support from the Carlsberg Foundation and the Danish government — as the world's first institute exclusively dedicated to theoretical physics. The Institute's 'golden decade' (1920s) saw the development of quantum mechanics: Heisenberg's matrix mechanics (1925), Schrödinger's wave mechanics (1926), Born's probability interpretation, Dirac's equation (1928), and the Copenhagen Interpretation — the philosophical framework for quantum mechanics that remains the dominant interpretation of quantum theory.\n\n"
            "The Niels Bohr Institute continues as a world-class research institution, contributing to the ATLAS experiment at CERN (Higgs boson discovery, 2012), gravitational wave astronomy, and the development of quantum computing. Its historical significance as the birthplace of quantum mechanics makes it, alongside CERN and the Institute for Advanced Study, one of the three most historically significant physics institutions of the 20th century."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Birthplace of Copenhagen Interpretation of quantum mechanics (est. 1920, Niels Bohr); first institute exclusively dedicated to theoretical physics; 'golden decade' 1920s: Heisenberg matrix mechanics, Schrödinger wave mechanics, Born probability interpretation, Dirac equation, Copenhagen Interpretation developed here; Bohr, Heisenberg, Pauli, Dirac, Schrödinger, Born, Meitner gathered for foundational seminars; continued contribution to CERN (Higgs boson, 2012); historically alongside CERN and IAS as most significant 20th-century physics institutions.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Niels Bohr's visionary recognition — after his 1913 atomic model and the subsequent quantum crisis in physics — that theoretical physics needed a dedicated institute where the world's best physicists could gather for extended collaborative work, distinct from the traditional university setting",
            "The Carlsberg Foundation's generous patronage — reflecting Denmark's tradition of private foundation support for science — provided the financial foundation that made the Institute independent and attractive to visiting physicists from across Europe",
            "The post-World War I context — with European physics at a moment of revolutionary ferment, facing the apparent contradictions of the old quantum theory — created the intellectual urgency that drew the most talented physicists of the generation (Heisenberg, Pauli, Dirac, Born) to Bohr's seminars"
        ],
        "effects": [
            "The Copenhagen Interpretation of quantum mechanics — developed at the Niels Bohr Institute through the dialogues of Bohr, Heisenberg, Born, and Pauli — established the philosophical framework for quantum theory that has been the dominant interpretation for 90 years, defining how physicists understand the meaning of quantum measurement and wave function collapse",
            "Heisenberg's development of matrix mechanics (1925) and the uncertainty principle (1927) — developed during his time at the Niels Bohr Institute — established the mathematical and philosophical foundations of quantum mechanics, earning Heisenberg the Nobel Prize in Physics (1932)",
            "The Bohr-Einstein debate — the famous exchange between Bohr and Einstein about the completeness of quantum mechanics, conducted partly through the Institute's seminar tradition — is the most consequential philosophical debate in 20th-century physics, shaping the development of quantum foundations",
            "The Institute's WWII history — Niels Bohr's escape from Nazi-occupied Denmark (1943) and his subsequent role in the Manhattan Project — and the Institute's post-war role in European nuclear physics (contributing to the founding of CERN, 1954) links it to the key institutional moments of 20th-century physics"
        ],
        "relationships": [
            {"entity": "Niels Bohr (founder and central figure)", "relationship": "FOUNDED_AND_CENTRED_ON_THE_WORK_OF", "note": "Bohr founded the Institute (1920) and his model of the atom, complementarity principle, and Copenhagen Interpretation are the central intellectual achievements that define the Institute's historical significance"},
            {"entity": "Copenhagen Interpretation of quantum mechanics", "relationship": "BIRTHPLACE_OF_THE", "note": "The Copenhagen Interpretation — the philosophical framework for quantum mechanics that remains the dominant interpretation — was developed at the NBI through the dialogues of Bohr, Heisenberg, and Born"},
            {"entity": "Werner Heisenberg (uncertainty principle)", "relationship": "HOME_OF_HEISENBERGS_DEVELOPMENT_OF", "note": "Heisenberg developed matrix mechanics (1925) and the uncertainty principle (1927) during his time at the Niels Bohr Institute"},
            {"entity": "Bohr-Einstein debate (quantum foundations)", "relationship": "CENTRE_OF_THE", "note": "The Bohr-Einstein debate — the most consequential philosophical debate in 20th-century physics — was conducted partly through the Institute's seminar tradition"},
            {"entity": "CERN (est. 1954, Geneva)", "relationship": "CONTRIBUTED_TO_THE_FOUNDING_OF", "note": "Bohr and the Niels Bohr Institute played a founding role in establishing CERN (1954) — the European particle physics laboratory — as part of the post-war internationalisation of science"}
        ],
    }),

    ("ibm-thomas-j-watson-research-center", {
        "summary": (
            "IBM Thomas J. Watson Research Center (est. 1961, Yorktown Heights, New York — IBM's primary research division, expanded from various earlier IBM research sites) is the world's largest industrial research organisation — the institution responsible for many of the most significant technological developments in computing history: the DRAM memory chip (1966), the relational database (Edgar Codd, 1970), reduced instruction set computing (RISC, 1980), magnetic stripe card, fractals (Benoit Mandelbrot), and the development of quantum computing and AI systems including Deep Blue (chess) and Watson (Jeopardy!).\n\n"
            "Watson Research Center emerged from IBM's recognition in the 1950s–1960s that the company's long-term competitive advantage depended on fundamental research — not just product development. IBM created a research division that attracted the world's best scientists with the freedom to pursue fundamental research, resulting in an extraordinary concentration of Nobel laureates (6 Nobel Prizes in Physics and Chemistry from IBM Research scientists) and transformative inventions.\n\n"
            "Watson Research Center's contemporary significance lies in its leadership of IBM's quantum computing programme (IBM Quantum Network, quantum supremacy research), AI research (successors to Watson), and materials science — areas where IBM is among the global leaders. The Watson center represents the industrial research model at its most ambitious: a corporation maintaining a world-class pure research institution within a profit-driven enterprise."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's largest industrial research organisation (est. 1961); DRAM chip (1966); relational database (Edgar Codd, 1970 — foundation of all modern databases); RISC architecture (1980); magnetic stripe card; fractals (Benoit Mandelbrot); Deep Blue beats Kasparov (chess, 1997); Watson wins Jeopardy! (2011); 6 Nobel Prizes from IBM Research scientists; IBM Quantum Network (quantum computing); extraordinary industrial research model.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "IBM's recognition in the 1950s–1960s that the company's long-term competitive advantage in the rapidly evolving computing industry depended on fundamental research — not merely incremental product development — drove Thomas J. Watson Jr.'s commitment to building a world-class industrial research organisation",
            "IBM's dominant market position in the early computing industry (controlling 70%+ of the mainframe market) gave it the financial resources to support fundamental research that would not generate immediate commercial returns — an investment strategy that would eventually produce transformative innovations",
            "The post-Sputnik era's valorisation of scientific research and the competition for scientific talent drove IBM to offer research scientists the freedom to pursue fundamental research questions — matching the academic environment of universities while providing superior experimental resources"
        ],
        "effects": [
            "Edgar Codd's development of the relational database model at IBM Research (1970) — based on relational algebra — is one of the most consequential computing innovations in history, establishing the conceptual foundation for all modern database management systems (Oracle, MySQL, PostgreSQL, SQL Server) that underpin the global digital economy",
            "The DRAM chip (Robert Dennard, IBM Research, 1966) — the fundamental memory technology that stores data in a capacitor — became the basis of all modern computer memory, from the first personal computers to contemporary smartphones and servers",
            "Benoit Mandelbrot's development of fractal geometry at IBM Research — combining his position at IBM with his mathematical work — produced a fundamental mathematical framework with applications from financial modelling to materials science, antenna design, and computer graphics",
            "Deep Blue's defeat of World Chess Champion Garry Kasparov (1997) was the first time a computer defeated a reigning world chess champion under standard tournament conditions — a landmark in artificial intelligence and human-computer interaction that permanently changed perceptions of machine cognition"
        ],
        "relationships": [
            {"entity": "Relational database model (Edgar Codd, 1970)", "relationship": "BIRTHPLACE_OF_THE", "note": "Edgar Codd developed the relational database model at IBM Research (1970) — the conceptual foundation for all modern database management systems"},
            {"entity": "DRAM chip (Robert Dennard, 1966)", "relationship": "SITE_OF_THE_INVENTION_OF_THE", "note": "IBM Research invented the DRAM chip (1966) — the fundamental memory technology that became the basis of all modern computer memory"},
            {"entity": "Deep Blue (chess, defeat of Kasparov 1997)", "relationship": "BUILT_BY_AND_SITE_OF", "note": "Deep Blue — which defeated Kasparov (1997) in the first computer victory over a reigning world chess champion — was developed at IBM Research"},
            {"entity": "Benoit Mandelbrot (fractal geometry)", "relationship": "HOME_INSTITUTION_OF_THE_DEVELOPMENT_OF", "note": "Mandelbrot developed fractal geometry at IBM Research — a fundamental mathematical framework with applications across science, finance, and computing"},
            {"entity": "IBM Quantum Network (quantum computing programme)", "relationship": "LEADS_THE", "note": "Watson Research Center leads IBM's quantum computing programme — making IBM one of the global leaders in quantum hardware and algorithm development"}
        ],
    }),

    ("berkman-klein-center-for-internet-society-at-harvard-university", {
        "summary": (
            "The Berkman Klein Center for Internet & Society at Harvard University (est. 1997, Cambridge, Massachusetts — founded by Charles Nesson and Jonathan Zittrain) is the world's leading academic institution for internet law, digital rights, and internet governance research — the organisation that has shaped the legal, ethical, and policy frameworks for the internet age. Berkman Klein has been the intellectual home of the most influential academic voices on internet freedom, surveillance, net neutrality, digital copyright, and artificial intelligence ethics.\n\n"
            "Founded in 1997 — at the earliest stage of the commercial internet, when the legal and social implications of a globally networked society were just beginning to emerge — the Berkman Center was the first major academic institution to treat the internet as a subject requiring serious scholarly attention. Its founding figures — Charles Nesson, Lawrence Lessig, Jonathan Zittrain, and Yochai Benkler — produced the intellectual frameworks for the internet era: Lessig's 'Code is Law' (the idea that software architecture has regulatory force), Zittrain's 'The Future of the Internet and How to Stop It', and Benkler's 'The Wealth of Networks'.\n\n"
            "Berkman Klein's contemporary focus has expanded from pure internet law to artificial intelligence ethics, algorithmic accountability, and the governance of AI systems — areas where it collaborates with MIT Media Lab, Google, Microsoft, and leading civil society organisations to develop frameworks that could govern AI's impact on democracy, privacy, and human rights."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "World's leading academic institution for internet law, digital rights, and internet governance (est. 1997); first major academic institution to treat the internet as serious scholarly subject; Lawrence Lessig ('Code is Law', Creative Commons); Jonathan Zittrain ('Future of the Internet'); Yochai Benkler ('Wealth of Networks'); shaped legal/ethical/policy frameworks for internet age; AI ethics, algorithmic accountability; net neutrality, digital rights, surveillance frameworks.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The 1990s explosion of the commercial internet — creating urgent legal and social questions about jurisdiction, privacy, intellectual property, and free speech in a globally networked environment — created the demand for an academic institution that could develop the conceptual frameworks for governing the new medium",
            "Charles Nesson's and Jonathan Zittrain's vision of an open, interdisciplinary research centre that could bring together legal scholars, computer scientists, social scientists, and civil society actors to develop internet governance frameworks drove the founding of the Berkman Center at Harvard Law School",
            "Harvard's position at the intersection of law, computer science, policy, and international affairs — combined with Cambridge's proximity to MIT and the Boston technology ecosystem — made it the natural location for an institution that needed to bridge technical and legal expertise"
        ],
        "effects": [
            "Lawrence Lessig's 'Code is Law' framework — developed at Berkman — established the foundational insight that software architecture has regulatory power: that the design of digital systems shapes human behaviour as powerfully as legal rules, fundamentally reshaping how lawyers, policymakers, and technologists think about digital governance",
            "Lessig's Creative Commons — conceptualised through Berkman's research on copyright and the digital commons — has licensed over 2 billion works worldwide, creating the legal infrastructure for the open content movement and establishing an alternative to all-rights-reserved copyright for the digital age",
            "Berkman Klein's research on internet freedom — including the 'Mapping the Arab Spring' project and the Global Network Initiative — has provided the analytical frameworks for understanding how authoritarian governments censor and surveil the internet, shaping the policies of governments, civil society, and technology companies",
            "Berkman Klein's AI ethics programme — including its work on algorithmic accountability, AI bias, and the governance of large language models — has positioned it as the leading academic institution for developing frameworks to govern AI's impact on democracy and human rights"
        ],
        "relationships": [
            {"entity": "Lawrence Lessig (Code is Law, Creative Commons)", "relationship": "INTELLECTUAL_HOME_OF", "note": "Lessig's 'Code is Law' framework and Creative Commons — developed at Berkman — are the most influential conceptual contributions to internet governance and digital rights"},
            {"entity": "Creative Commons (2 billion licensed works)", "relationship": "INTELLECTUAL_ORIGIN_AND_FOUNDING_HOME_OF", "note": "Creative Commons — the legal infrastructure for the open content movement — was conceptualised through Berkman's research and has licensed over 2 billion works worldwide"},
            {"entity": "Jonathan Zittrain (The Future of the Internet)", "relationship": "CO-FOUNDED_AND_SHAPED_BY", "note": "Zittrain's 'The Future of the Internet and How to Stop It' — developed at Berkman — is one of the most influential academic works on digital technology policy"},
            {"entity": "AI ethics and algorithmic accountability research", "relationship": "LEADING_ACADEMIC_INSTITUTION_FOR", "note": "Berkman Klein's AI ethics programme — developing frameworks for algorithmic accountability and AI governance — positions it as the leading academic institution for AI governance research"},
            {"entity": "Arab Spring (internet freedom mapping)", "relationship": "ANALYTICAL_FRAMEWORKS_PROVIDED_FOR_UNDERSTANDING_THE", "note": "Berkman's 'Mapping the Arab Spring' project provided frameworks for understanding how authoritarian governments censor the internet — shaping civil society and technology company policies"}
        ],
    }),

    ("khan-research-laboratories", {
        "summary": (
            "Khan Research Laboratories (KRL, est. 1976, Kahuta, Pakistan — founded by A.Q. Khan with the initial mission of uranium enrichment for Pakistan's nuclear weapons programme) is the scientific organisation responsible for Pakistan's nuclear weapons capability — producing the uranium-enriched material for Pakistan's first nuclear devices (tested 28 May 1998, Chagai), establishing Pakistan as the world's first Muslim-majority nuclear state, and transforming South Asian and global security dynamics. KRL also became the centre of the world's most dangerous nuclear proliferation network: the A.Q. Khan network.\n\n"
            "A.Q. Khan founded KRL after stealing classified uranium enrichment centrifuge designs from URENCO (Almelo, Netherlands) in 1975 — where he had worked as a metallurgist — and returning to Pakistan with the technical knowledge needed to build a uranium enrichment capability. KRL's gas centrifuge programme — based on stolen Western designs — gave Pakistan the technical path to nuclear weapons that PAEC's plutonium programme had failed to complete quickly enough. The laboratory was named after Khan and remained his personal fiefdom for two decades.\n\n"
            "KRL's most consequential — and most dangerous — legacy is the A.Q. Khan nuclear proliferation network: the systematic transfer of nuclear weapons technology (centrifuge designs, weapon designs, components) to Libya, Iran, and North Korea in exchange for payments channelled through intermediaries. The Khan network represents the largest nuclear proliferation operation in history, distributing the most dangerous knowledge on Earth to the most dangerous regimes."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Pakistan's nuclear weapons capability (est. 1976, A.Q. Khan); uranium enrichment based on stolen URENCO centrifuge designs (Almelo, Netherlands, 1975); Pakistan's first nuclear tests — Chagai (28 May 1998) — first Muslim-majority nuclear state; transformed South Asian and global security; A.Q. Khan nuclear proliferation network — centrifuge designs, weapon designs sold to Libya, Iran, North Korea — largest nuclear proliferation operation in history.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "India's 'Smiling Buddha' nuclear test (1974) — which revealed Pakistan's existential vulnerability to an Indian nuclear threat — drove Pakistan's determination to develop nuclear weapons, creating the political urgency that gave A.Q. Khan his mission and institutional authority",
            "A.Q. Khan's theft of URENCO centrifuge designs (1975) — and his return to Pakistan with the technical knowledge to build a gas centrifuge uranium enrichment programme — gave Pakistan a faster path to nuclear weapons than the plutonium route pursued by PAEC, making KRL the primary nuclear weapons path",
            "Pakistan's security elite's determination to develop a nuclear deterrent against India — and the willingness of Prime Minister Bhutto to accept Khan's terms for leading the weapons programme ('eat grass' if necessary) — gave KRL political protection and resources that insulated it from international pressure for over two decades"
        ],
        "effects": [
            "Pakistan's Chagai nuclear tests (28 May 1998) — five devices tested in a single day — announced Pakistan as the world's first Muslim-majority nuclear state and the seventh nuclear weapons state, permanently transforming South Asian security dynamics and establishing the subcontinent's nuclear deterrent balance",
            "The A.Q. Khan proliferation network — which sold centrifuge designs, uranium hexafluoride, weapons designs, and components to Libya, Iran, and North Korea — advanced each country's nuclear weapons programme by years and represents the most consequential act of nuclear proliferation in history",
            "Libya's nuclear programme (dismantled 2003-2004 after Khan network exposure) — and the related discovery of the full scope of the Khan network — triggered the most significant nuclear non-proliferation crisis since the Cold War, exposing the fragility of the NPT regime and leading to the Proliferation Security Initiative",
            "North Korea's receipt of P-2 centrifuge designs from the Khan network — which accelerated Pyongyang's uranium enrichment path to nuclear weapons — has contributed to North Korea's nuclear arsenal, making KRL indirectly responsible for one of the most dangerous contemporary nuclear threats"
        ],
        "relationships": [
            {"entity": "A.Q. Khan (founder and director)", "relationship": "FOUNDED_BY_AND_PERSONAL_DOMAIN_OF", "note": "Khan founded KRL based on stolen URENCO centrifuge designs and directed it for two decades — making it his personal fiefdom and the instrument of both Pakistan's nuclear deterrent and global proliferation"},
            {"entity": "Pakistan's Chagai nuclear tests (28 May 1998)", "relationship": "PRODUCED_THE_ENRICHED_URANIUM_THAT_ENABLED_THE", "note": "KRL's enriched uranium — produced by the centrifuge programme — was the material for Pakistan's Chagai tests (1998), announcing Pakistan as the first Muslim-majority nuclear state"},
            {"entity": "A.Q. Khan nuclear proliferation network (Libya, Iran, North Korea)", "relationship": "SOURCE_OF_THE_TECHNOLOGY_SOLD_BY_THE", "note": "KRL's centrifuge designs, weapon designs, and components were sold to Libya, Iran, and North Korea — the largest nuclear proliferation operation in history"},
            {"entity": "URENCO (Almelo, Netherlands)", "relationship": "TECHNOLOGY_BASE_STOLEN_FROM", "note": "Khan stole URENCO's centrifuge designs while working there (1975) — the technical theft that gave Pakistan its uranium enrichment capability"},
            {"entity": "India's Smiling Buddha test (1974)", "relationship": "STRATEGIC_URGENCY_DRIVEN_BY_THE", "note": "India's 1974 nuclear test drove Pakistan's determination to develop nuclear weapons — the existential threat that gave KRL its mission and political protection"}
        ],
    }),

    ("future-of-humanity-institute", {
        "summary": (
            "The Future of Humanity Institute (FHI, est. 2005, Oxford University — founded by Nick Bostrom) was one of the world's leading research institutions for existential risk, artificial intelligence safety, and long-term futures — the academic organisation that established the intellectual frameworks for thinking rigorously about threats that could permanently curtail humanity's future. FHI produced the academic foundations of the AI safety movement, the effective altruism movement's engagement with existential risk, and the governance frameworks for advanced AI systems. (FHI closed in April 2024 following funding disputes with Oxford.)\n\n"
            "Nick Bostrom founded FHI based on his earlier work on existential risk — the possibility that certain technological developments or natural events could permanently and catastrophically reduce humanity's long-term potential. FHI's research agenda centred on: (1) AI safety — developing technical and governance frameworks for ensuring advanced AI systems remain aligned with human values; (2) biosecurity — assessing the risks of engineered pandemics and dual-use biological research; (3) nuclear security and geopolitical catastrophic risk; and (4) the long-term future — philosophical work on human enhancement, space colonisation, and transhumanism.\n\n"
            "FHI's most consequential output was Nick Bostrom's Superintelligence: Paths, Dangers, Strategies (2014) — the book that brought AI safety into mainstream academic and policy discourse, was read by Elon Musk, Bill Gates, and Sam Altman, and catalysed the founding of AI safety organisations including OpenAI, the Machine Intelligence Research Institute, and the Centre for Human-Compatible AI."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Leading existential risk and AI safety research institution (est. 2005, Oxford, Nick Bostrom; closed April 2024); established intellectual frameworks for existential risk and AI safety; Nick Bostrom's Superintelligence (2014) — catalysed AI safety movement, read by Musk/Gates/Altman; contributed to founding of OpenAI, MIRI, CHAI; effective altruism movement's existential risk engagement; biosecurity and nuclear catastrophic risk research; foundational institution of 21st-century AI governance discourse.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Nick Bostrom's earlier theoretical work on existential risk — particularly his 'Astronomical Waste' paper (2003) and the simulation argument — created the intellectual agenda that drove the founding of FHI as a dedicated research institution for long-term futures and catastrophic risks",
            "The acceleration of AI capabilities in the early 2000s — with increasingly powerful machine learning systems raising questions about the long-term trajectory of AI development — created the scientific urgency that justified a dedicated research programme on AI safety and alignment",
            "The effective altruism movement's adoption of existential risk as its primary cause — driven partly by FHI research and the work of FHI-affiliated philosophers — created the funding and community support for existential risk research institutions"
        ],
        "effects": [
            "Nick Bostrom's Superintelligence: Paths, Dangers, Strategies (2014) — FHI's most influential output — catalysed the mainstream discourse on AI safety, was read by technology leaders including Elon Musk, Bill Gates, and Sam Altman, and directly contributed to the founding of OpenAI (2015), the Machine Intelligence Research Institute, and the Centre for Human-Compatible AI",
            "FHI's research on AI governance — particularly Toby Ord's The Precipice (2020) and the concept of 'existential risk' as a policy priority — provided the intellectual frameworks for the EU AI Act, the UK AI Safety Institute, and the Bletchley Park AI Safety Summit (2023)",
            "FHI's biosecurity research — developing frameworks for assessing the risks of engineered pandemics and dual-use biological research — established the academic foundation for pandemic preparedness research and the governance frameworks for biotechnology risk assessment",
            "FHI's closure (April 2024) — following funding disputes with Oxford University — itself became a signal event in AI safety discourse, raising questions about the institutional sustainability of existential risk research and the relationship between academia and the AI safety movement"
        ],
        "relationships": [
            {"entity": "Nick Bostrom (founder, Superintelligence 2014)", "relationship": "FOUNDED_BY_AND_CENTRED_ON_THE_WORK_OF", "note": "Bostrom founded FHI (2005) and his Superintelligence (2014) — the most influential academic work on AI safety — catalysed the AI safety movement"},
            {"entity": "Superintelligence (Bostrom, 2014)", "relationship": "PRODUCED_THE_FIELD-DEFINING_WORK", "note": "FHI produced Superintelligence (2014) — which catalysed mainstream AI safety discourse and contributed to the founding of OpenAI, MIRI, and CHAI"},
            {"entity": "OpenAI (founded 2015)", "relationship": "INTELLECTUAL_CATALYST_FOR_THE_FOUNDING_OF", "note": "FHI's AI safety research — and Superintelligence's influence on Musk and Altman — was a direct intellectual catalyst for OpenAI's founding (2015)"},
            {"entity": "EU AI Act and UK AI Safety Institute", "relationship": "INTELLECTUAL_FRAMEWORKS_CONTRIBUTED_TO_THE", "note": "FHI's research on AI governance and existential risk provided intellectual foundations for the EU AI Act and the UK AI Safety Institute"},
            {"entity": "Effective altruism movement (existential risk focus)", "relationship": "PRIMARY_ACADEMIC_PARTNER_OF_THE", "note": "FHI was the primary academic institution for the effective altruism movement's existential risk agenda — through Toby Ord's The Precipice (2020) and FHI-affiliated philosophers"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 33 — {len(ENTITIES)} entities (Class 352: Research Centers & National Laboratories)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
