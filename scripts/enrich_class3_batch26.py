#!/usr/bin/env python3
"""
Batch 26 — 8 entities (Class 350): Famous Research Institutions & Laboratories
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()
FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/350-Class-350"
FILE_PREFIX = "350"


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

    ("bell-labs", {
        "summary": (
            "Bell Laboratories (originally Bell Telephone Laboratories, est. 1925, Murray Hill, New Jersey; now Nokia Bell Labs) is the most productive research institution in the history of technology — responsible for inventions that collectively define the modern world: the transistor (1947), the laser (1960), the Unix operating system (1969), the C programming language (1972), cellular telephony (1970s), the CCD image sensor (1969), information theory (Claude Shannon, 1948), and optical fibre communications. Bell Labs researchers have been awarded 9 Nobel Prizes — more than any private research institution in history.\n\n"
            "Bell Labs was created by AT&T as the research division of the American Bell telephone monopoly — a corporate research model that gave scientists extraordinary freedom and resources to pursue fundamental research without immediate commercial pressure. The transistor (invented by William Shockley, John Bardeen, and Walter Brattain, 1947) — the device that replaced the vacuum tube and enabled all modern electronics — is the single most consequential invention in 20th-century technology, making Bell Labs the birthplace of the semiconductor industry and the digital age.\n\n"
            "Claude Shannon's 'A Mathematical Theory of Communication' (1948) — developed at Bell Labs — founded information theory, the mathematical framework for digital communication that underlies all modern telecommunications, computing, and data storage. Unix and C — developed at Bell Labs by Ken Thompson and Dennis Ritchie (1969–1972) — are the operating system and programming language that became the foundation of the modern software industry, with derivatives (Linux, macOS, Android) running the majority of the world's computers and servers."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Most productive technology research institution in history (est. 1925); invented: transistor (1947), laser (1960), Unix (1969), C programming language (1972), CCD sensor (1969), cellular telephony, optical fibre, information theory (Shannon 1948); 9 Nobel Prizes — more than any private institution; transistor is single most consequential 20th-century invention; Shannon's information theory underlies all digital communication.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "AT&T's telephone monopoly — generating enormous revenues from a regulated natural monopoly — provided the financial base for a research institution with the resources to pursue fundamental science without immediate commercial pressure, creating the conditions for breakthrough research",
            "The AT&T system's practical need for better communications technologies — vacuum tubes that failed, wires that degraded, signals that needed amplification — created the applied research agenda that produced the transistor (replacing vacuum tubes) and information theory (improving signal transmission)",
            "The concentration of the world's leading physicists, mathematicians, and engineers at a single institution — including William Shockley, John Bardeen, Walter Brattain, Claude Shannon, Dennis Ritchie, Ken Thompson, and dozens of Nobel laureates — created the critical mass of intellectual talent that generated a disproportionate fraction of 20th-century technology innovation"
        ],
        "effects": [
            "The transistor (1947) — replacing the vacuum tube with a solid-state device — enabled the miniaturisation of electronics that produced every modern device: computers, smartphones, satellites, medical imaging, automotive electronics, and the internet infrastructure all depend on transistors",
            "Claude Shannon's information theory (1948) — defining the mathematical limits of data compression and transmission — is the intellectual foundation of all digital communications, making Bell Labs the birthplace of the conceptual framework on which the internet, mobile phones, and digital storage are built",
            "Unix and C (1969–1972) — the operating system and programming language developed at Bell Labs — became the foundation of the software industry: Linux (the dominant server operating system), macOS, iOS, and Android are all Unix descendants; C remains the most widely used programming language for system software",
            "The Bell Labs model of corporate fundamental research — scientists given freedom and resources to pursue basic science without immediate commercial objectives — became the aspiration for technology company research divisions (Google X, Microsoft Research, IBM Research) and demonstrated that private research institutions could rival universities in scientific productivity"
        ],
        "relationships": [
            {"entity": "AT&T (American Telephone & Telegraph)", "relationship": "FOUNDED_AND_FUNDED_BY", "note": "Bell Labs was created as the research arm of AT&T's telephone monopoly — providing the financial freedom that enabled fundamental research"},
            {"entity": "Transistor (1947 — Shockley, Bardeen, Brattain)", "relationship": "BIRTHPLACE_OF_THE", "note": "The transistor — the most consequential single invention of the 20th century — was invented at Bell Labs in 1947, earning its inventors the Nobel Prize"},
            {"entity": "Claude Shannon's Information Theory (1948)", "relationship": "BIRTHPLACE_OF", "note": "Shannon's 'Mathematical Theory of Communication' — the foundation of all digital communications — was developed at Bell Labs"},
            {"entity": "Unix and C programming language (1969–1972)", "relationship": "BIRTHPLACE_OF", "note": "Ken Thompson and Dennis Ritchie created Unix (1969) and C (1972) at Bell Labs — the operating system and language that became the foundation of the software industry"},
            {"entity": "Nobel Prizes in Physics (transistor, laser, telecommunications)", "relationship": "WON_9_OF_BY_RESEARCHERS_OF", "note": "Bell Labs researchers have won 9 Nobel Prizes — more than any private research institution — for the transistor, laser, CCD sensor, and information physics"}
        ],
    }),

    ("cold-spring-harbor-laboratory", {
        "summary": (
            "Cold Spring Harbor Laboratory (CSHL, est. 1890, Long Island, New York) is the world's most influential molecular biology research institution — the site where the human genome project was co-initiated (1986), where Barbara McClintock discovered transposable genetic elements ('jumping genes', 1948–1983 Nobel Prize), where James Watson and others pioneered recombinant DNA research, and where the standard techniques of molecular biology — including the polymerase chain reaction (PCR) development — were refined and disseminated through CSHL's legendary summer courses and symposia. CSHL has been associated with 8 Nobel Prizes.\n\n"
            "Founded as the Brooklyn Institute of Arts and Sciences' biological laboratory, Cold Spring Harbor became the centre of American genetics research in the 20th century. Its summer symposia — held since 1933 — are the primary forum for disseminating new discoveries in molecular biology and genetics, creating the intellectual community that shaped the DNA revolution. The laboratory's dark history includes its role in the American eugenics movement: its Eugenics Record Office (1910–1944) collected genealogical data to support immigration restrictions and sterilisation laws.\n\n"
            "The laboratory's 2003 completion of the Human Genome Project — co-initiated by James Watson as the first director of the NIH's Human Genome Project (1988–1992) before his resignation — makes Cold Spring Harbor one of the foundational institutions of 21st-century genomic medicine, whose breakthroughs are transforming oncology, inherited disease diagnosis, and personalised medicine."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "World's most influential molecular biology institution (est. 1890); 8 Nobel Prizes; Barbara McClintock's 'jumping genes' discovery (Nobel 1983); co-initiated Human Genome Project (1986); annual symposia since 1933 — primary forum for molecular biology community; dark history: Eugenics Record Office (1910–1944) supporting immigration restriction and sterilisation laws; foundation of 21st-century genomic medicine.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Long Island's natural environment — with its diverse coastal habitats — made Cold Spring Harbor ideal for biological research in the late 19th century, when natural history and comparative biology were the dominant research paradigms",
            "The transition from natural history to genetics research in the early 20th century — driven by the rediscovery of Mendel's laws (1900) and the rise of experimental biology — made Cold Spring Harbor's summer research model (bringing scientists together for intensive fieldwork and experiment) the perfect vehicle for the new genetics",
            "James Watson's appointment as laboratory director (1968) — and his transformation of CSHL from a declining summer research station into a year-round molecular biology powerhouse — was the pivotal institutional decision that made Cold Spring Harbor the centre of the DNA revolution"
        ],
        "effects": [
            "Barbara McClintock's discovery of transposable genetic elements ('jumping genes') at Cold Spring Harbor — initially dismissed for decades before winning the Nobel Prize in 1983 — is one of the most important discoveries in 20th-century biology, showing that genes move between chromosomal locations and fundamentally challenging the static model of genetics",
            "The Human Genome Project — co-initiated by Cold Spring Harbor — produced the first complete sequence of the human genome (2003), creating the foundation for 21st-century genomic medicine, personalised cancer therapy, and the CRISPR genetic editing revolution",
            "The annual Cold Spring Harbor Symposia (1933–present) — gathering the world's leading molecular biologists each summer — created the intellectual community that coordinated and accelerated the DNA revolution, from the discovery of DNA structure (1953) to the development of CRISPR (2012)",
            "The Eugenics Record Office (1910–1944) — the most important eugenics research institution in the US — provided the scientific legitimacy for immigration restriction legislation (1924) and sterilisation laws in 30 US states, demonstrating how scientific institutions can be mobilised for racial ideology"
        ],
        "relationships": [
            {"entity": "Barbara McClintock (Nobel Prize 1983)", "relationship": "RESEARCH_HOME_OF", "note": "McClintock spent most of her career at Cold Spring Harbor — discovering 'jumping genes' (transposable elements) that earned the Nobel Prize in 1983"},
            {"entity": "Human Genome Project (2003 completion)", "relationship": "CO-INITIATING_INSTITUTION_OF_THE", "note": "Cold Spring Harbor co-initiated the Human Genome Project (1986) — whose 2003 completion created the foundation for 21st-century genomic medicine"},
            {"entity": "Cold Spring Harbor Symposia (1933–present)", "relationship": "HOST_OF_DEFINING_ANNUAL_GATHERINGS_OF", "note": "The annual symposia — gathering leading molecular biologists since 1933 — coordinated the intellectual community of the DNA revolution"},
            {"entity": "American eugenics movement (Eugenics Record Office, 1910–1944)", "relationship": "INSTITUTIONAL_HOME_OF", "note": "The Eugenics Record Office at Cold Spring Harbor provided the scientific basis for US immigration restriction and sterilisation laws — a dark institutional history"},
            {"entity": "James Watson (Nobel Prize 1962)", "relationship": "TRANSFORMED_BY_DIRECTORSHIP_OF", "note": "Watson's directorship (1968–2004) transformed Cold Spring Harbor from a declining summer station into the world's leading molecular biology institution"}
        ],
    }),

    ("fermilab", {
        "summary": (
            "Fermi National Accelerator Laboratory (Fermilab, est. 1967, Batavia, Illinois) is the United States' primary high-energy particle physics laboratory and the discoverer of the bottom quark (1977) and the top quark (1995) — the last two of the six quarks in the Standard Model of particle physics to be discovered on American soil. Fermilab's Tevatron accelerator (1983–2011) was the world's highest-energy particle collider for two decades, producing discoveries that verified the Standard Model and searching for physics beyond it.\n\n"
            "The laboratory was founded in 1967 under director Robert Wilson — a physicist and sculptor whose buildings and the Fermilab campus are designed as works of art, creating the most aesthetically distinctive science campus in the world. Wilson's philosophy that science and art share a common commitment to beauty — expressed in his design of the Tevatron's circular berm, the Wilson Hall structure (15 storeys, modelled on Beauvais Cathedral), and the resident bison herd — established Fermilab's identity as a place where scientific and aesthetic values are explicitly integrated.\n\n"
            "Following the shutdown of the Tevatron (2011, superseded by CERN's LHC), Fermilab has focused on neutrino physics and the Deep Underground Neutrino Experiment (DUNE) — the most ambitious neutrino experiment in history, which will send a beam of neutrinos 1,300 kilometres through the earth from Fermilab to a detector in the Sanford Underground Research Facility in South Dakota."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "US primary high-energy physics lab (est. 1967); discovered bottom quark (1977) and top quark (1995) — completing the quark sector of the Standard Model; Tevatron — world's highest-energy collider for 20 years (1983–2011); Robert Wilson designed campus as integrated science-art environment including bison herd and Beauvais Cathedral-inspired Wilson Hall; DUNE neutrino experiment sends beam 1,300km through earth.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The United States' desire to maintain world leadership in high-energy particle physics — following the successes of European institutions and the establishment of CERN (1954) — drove the federal government to fund a new national particle physics laboratory west of the Alleghenies, accessible to midwestern universities",
            "Robert Wilson's appointment as founding director — and his insistence that the laboratory be designed as an aesthetically integrated scientific campus, not merely a collection of industrial buildings — created the distinctive character of Fermilab that has made it a model for the integration of scientific and aesthetic values",
            "The availability of the Batavia, Illinois site — with sufficient land for the Tevatron's 6.3-kilometre circumference — and the political support of Illinois's congressional delegation created the practical conditions for the world's most powerful accelerator"
        ],
        "effects": [
            "The discovery of the bottom quark (1977) and top quark (1995) at Fermilab completed the quark sector of the Standard Model of particle physics — the theoretical framework describing all known fundamental particles and forces — providing the experimental verification of the most comprehensive theory in physics",
            "The Tevatron's 20 years as the world's highest-energy collider made Fermilab the primary site for particle physics discoveries from the 1980s through 2010, producing data that verified the Standard Model's predictions and establishing the baseline against which new physics beyond the Standard Model is measured",
            "The DUNE experiment — sending a neutrino beam 1,300 km through the earth from Fermilab to South Dakota — represents the most ambitious attempt yet to understand neutrino oscillations and the matter-antimatter asymmetry that explains why the universe contains matter rather than nothing",
            "Robert Wilson's design of the Fermilab campus — the Wilson Hall building modelled on Beauvais Cathedral, the Tevatron's circular earthworks, the resident bison herd — established the precedent that a large scientific institution could integrate aesthetic beauty and natural landscape as explicit values alongside scientific excellence"
        ],
        "relationships": [
            {"entity": "Standard Model of particle physics", "relationship": "COMPLETED_QUARK_SECTOR_OF_THE", "note": "Fermilab's discovery of the bottom quark (1977) and top quark (1995) completed the quark sector of the Standard Model — the framework describing all fundamental particles"},
            {"entity": "Tevatron accelerator (1983–2011)", "relationship": "OPERATED_THE_WORLD'S_HIGHEST_ENERGY_COLLIDER", "note": "The Tevatron was the world's highest-energy collider for 20 years — producing the bottom and top quark discoveries and testing the Standard Model"},
            {"entity": "Robert Wilson (founding director)", "relationship": "CONCEIVED_AND_DESIGNED_BY", "note": "Wilson designed Fermilab as an integrated science-art campus — Wilson Hall, the bison herd, and the Tevatron berm creating the most aesthetically distinctive science campus in the world"},
            {"entity": "DUNE (Deep Underground Neutrino Experiment)", "relationship": "NEUTRINO_BEAM_SOURCE_FOR_THE", "note": "DUNE sends a Fermilab-generated neutrino beam 1,300km through the earth to South Dakota — the most ambitious neutrino experiment in history"},
            {"entity": "CERN (European Organisation for Nuclear Research)", "relationship": "SUPERSEDED_AS_WORLD'S_HIGHEST_ENERGY_COLLIDER_BY", "note": "CERN's LHC superseded the Tevatron (2011) — ending Fermilab's 20-year leadership in high-energy collider physics"}
        ],
    }),

    ("pasteur-institute", {
        "summary": (
            "The Pasteur Institute (Institut Pasteur, est. 1887, Paris, France) is the world's most historically significant biomedical research institution — founded by Louis Pasteur to develop the rabies vaccine (1885) and to pursue the germ theory of disease that Pasteur had spent his career establishing. The Institute is one of the founding institutions of modern microbiology, immunology, and vaccinology — disciplines whose discoveries constitute the scientific foundation of modern medicine. Pasteur Institute researchers have been awarded 10 Nobel Prizes in Physiology or Medicine.\n\n"
            "The Institute was founded by public subscription following Pasteur's dramatic public demonstration of the rabies vaccine (1885) — inoculating 9-year-old Joseph Meister, who had been bitten by a rabid dog, in the most celebrated experiment in the history of medicine. This public success funded a global institution: within ten years of its founding, the Pasteur Institute had established branches across the French colonial empire and beyond, creating the international Pasteur Network that today encompasses 33 institutes in 25 countries.\n\n"
            "The Pasteur Institute's greatest 20th-century discovery was the identification of HIV as the cause of AIDS (1983) by Luc Montagnier and Françoise Barré-Sinoussi — for which they received the Nobel Prize in 2008. The Institute also developed the BCG tuberculosis vaccine (1921), identified the Mycobacterium tuberculosis bacterium's mechanism of antibiotic resistance, and made foundational discoveries in bacterial genetics, molecular biology, and immunology. The Institute's 'Annals of the Pasteur Institute' (founded 1887) is one of the oldest journals of microbiology."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's most historically significant biomedical institution (est. 1887); founded by Louis Pasteur following rabies vaccine success (1885); 10 Nobel Prizes; discovered HIV as cause of AIDS (Montagnier, Barré-Sinoussi, 1983); developed BCG tuberculosis vaccine (1921); 33 institutes in 25 countries; founding institution of microbiology, immunology, and vaccinology as scientific disciplines.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Louis Pasteur's public demonstration of the rabies vaccine (1885) — inoculating Joseph Meister in the most celebrated medical experiment in history — generated a wave of international public donations that provided the founding capital for an institution dedicated to continuing Pasteur's vaccine research",
            "The germ theory of disease — the revolutionary understanding that specific microorganisms cause specific diseases, established by Pasteur against fierce opposition — created the scientific framework that made the Pasteur Institute's research programme possible and gave it global significance",
            "The French Third Republic's support for Pasteur's Institute — and the French colonial empire's need for medical institutions to combat tropical diseases — drove the establishment of Pasteur branches across Africa and Asia, creating the international network that makes the Pasteur Institute global in scope"
        ],
        "effects": [
            "The Pasteur Institute's confirmation of the germ theory — and its development of vaccines against rabies, diphtheria, typhoid, yellow fever, and tuberculosis — established the scientific basis of modern preventive medicine, demonstrating that microbial diseases are preventable through vaccination",
            "The discovery of HIV (1983) by Luc Montagnier and Françoise Barré-Sinoussi at the Pasteur Institute — announced in 1983 and confirmed against competing claims from the US NIH — initiated the global scientific response to the AIDS pandemic that has produced antiretroviral therapies saving 20 million lives",
            "The BCG vaccine for tuberculosis (developed by Calmette and Guérin, 1921) — still the primary tuberculosis vaccine used worldwide, given to approximately 100 million infants annually — is the Pasteur Institute's most widely deployed public health intervention",
            "The Pasteur Network (33 institutes in 25 countries) — created from the original Institut Pasteur branches — is the most extensive international network of biomedical research institutions in the developing world, providing microbiology and epidemiology capacity across Africa, Asia, and the Americas"
        ],
        "relationships": [
            {"entity": "Louis Pasteur", "relationship": "FOUNDED_BY_AND_NAMED_FOR", "note": "Pasteur founded the Institute (1887) following his rabies vaccine success — creating an institution dedicated to germ theory research and vaccine development"},
            {"entity": "Rabies vaccine (1885 — Joseph Meister)", "relationship": "FOUNDING_SCIENTIFIC_ACHIEVEMENT_OF", "note": "The 1885 rabies vaccine — inoculating 9-year-old Joseph Meister in the most celebrated medical experiment in history — funded and inspired the Institut Pasteur"},
            {"entity": "HIV/AIDS (1983 discovery)", "relationship": "DISCOVERY_SITE_OF_HIV_CAUSE_OF", "note": "Luc Montagnier and Françoise Barré-Sinoussi identified HIV at the Pasteur Institute (1983) — earning the Nobel Prize in 2008 and initiating the AIDS pandemic response"},
            {"entity": "BCG tuberculosis vaccine (1921)", "relationship": "DEVELOPED_THE", "note": "The BCG vaccine — still given to 100 million infants annually — was developed at the Pasteur Institute by Calmette and Guérin (1921)"},
            {"entity": "Pasteur International Network (33 institutes, 25 countries)", "relationship": "MOTHER_INSTITUTION_OF_THE", "note": "The Pasteur Network extends the Paris institute's mission across 33 branches in 25 countries — primarily in the developing world"}
        ],
    }),

    ("johns-hopkins-university", {
        "summary": (
            "Johns Hopkins University (est. 1876, Baltimore, Maryland) was the first research university in the United States — founded on the German research university model that combined teaching with original research, transforming American higher education from a collegiate system focused on classical instruction into a university system focused on the creation of new knowledge. Johns Hopkins's founding philosophy — that the purpose of a university is to advance knowledge, not merely transmit it — became the template for every subsequent American research university.\n\n"
            "The university was founded with a $7 million bequest from the merchant-philanthropist Johns Hopkins — the largest private charitable donation in American history to that date — and was designed by its first president Daniel Coit Gilman to model the German university tradition, with graduate training, research specialisation, and academic publishing as its central activities. The Johns Hopkins Medical School (est. 1893) — with its associated Johns Hopkins Hospital — created the model of evidence-based clinical medicine that defines modern medical education worldwide, producing 'The Principles and Practice of Medicine' (William Osler, 1892), the founding textbook of clinical medicine.\n\n"
            "The Flexner Report (1910) — commissioned by the Carnegie Foundation following Abraham Flexner's study of North American medical schools — used Johns Hopkins as the standard against which all other medical schools were evaluated, leading to the closure of 82 of the 155 American medical schools that existed in 1910 and establishing the Johns Hopkins model as the universal standard of medical education."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "First research university in the United States (est. 1876); introduced German research university model — teaching + original research combined; Johns Hopkins Medical School (1893) + Hospital created modern clinical medicine model; William Osler's 'Principles and Practice of Medicine' (1892) — founding clinical medicine textbook; Flexner Report (1910) used Hopkins as the gold standard, closing 82 of 155 US medical schools.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Johns Hopkins's $7 million bequest (1873) — specifying that a university and hospital be established on the German research model — provided both the financial foundation and the programmatic mandate for the first American research university",
            "Daniel Coit Gilman's first-hand knowledge of the German research university system (he had studied German higher education) — and his determination to transplant its combining of teaching and research to America — shaped the institutional model that transformed American higher education",
            "The intellectual inadequacy of American collegiate education in the mid-19th century — with its classical curriculum focused on character formation rather than scientific or scholarly research — created the demand for a new institutional model capable of producing original knowledge and training research scientists"
        ],
        "effects": [
            "Johns Hopkins established the research university as the dominant model for American higher education — its graduate school, its seminar system, its expectation of faculty research publications, and its professionalisation of academic disciplines became the template for Harvard, Yale, Columbia, and every subsequent American university's transformation into a research institution",
            "The Johns Hopkins Medical School's combination of a scientific medical curriculum, laboratory training, clinical rounds, and a teaching hospital — the model designed by William Welch, William Osler, William Halsted, and Howard Kelly — became the universal standard for medical education worldwide after the Flexner Report (1910)",
            "William Osler's 'Principles and Practice of Medicine' (1892) — written at Johns Hopkins — was the most influential medical textbook of the 20th century, shaping the clinical reasoning and diagnostic approach of generations of physicians and establishing evidence-based medicine as the foundation of clinical practice",
            "The Flexner Report (1910) — which used Hopkins as the gold standard — eliminated 82 of 155 American medical schools, concentrating medical education in institutions that could sustain the Hopkins model, and created the modern American medical education system with its high scientific and clinical standards"
        ],
        "relationships": [
            {"entity": "German research university model (19th century)", "relationship": "TRANSPLANTED_TO_AMERICA_BY", "note": "Hopkins imported the German model — combining teaching and original research — transforming American higher education from a collegiate to a research university system"},
            {"entity": "Daniel Coit Gilman (first president)", "relationship": "DESIGNED_AND_LAUNCHED_BY", "note": "Gilman's vision — shaped by his study of German universities — created the institutional model that made Hopkins the template for American research universities"},
            {"entity": "William Osler (Principles and Practice of Medicine, 1892)", "relationship": "AUTHORED_FOUNDING_CLINICAL_MEDICINE_TEXTBOOK_AT", "note": "Osler's textbook — written at Hopkins — was the most influential medical text of the 20th century, defining clinical reasoning for generations of physicians"},
            {"entity": "Flexner Report (1910)", "relationship": "GOLD_STANDARD_FOR_THE", "note": "The Flexner Report used Hopkins as the model medical school — its conclusions closed 82 of 155 US medical schools and established the Hopkins standard universally"},
            {"entity": "American research university system", "relationship": "FOUNDING_INSTITUTIONAL_MODEL_FOR_THE", "note": "Hopkins's founding philosophy — the university as a place for creating knowledge, not just transmitting it — became the template for all American research universities"}
        ],
    }),

    ("howard-hughes-medical-institute", {
        "summary": (
            "The Howard Hughes Medical Institute (HHMI, est. 1953, Chevy Chase, Maryland) is the largest private biomedical research philanthropic organisation in the United States — with an endowment of approximately $23 billion (2023) and annual research expenditure of over $900 million, making it the largest non-governmental funder of basic biomedical research in the world. HHMI supports approximately 300 'Investigator' scientists at universities and research institutions across the US — chosen for their exceptional creativity and long-term scientific promise.\n\n"
            "The Institute was founded by billionaire aviator and industrialist Howard Hughes (1905–1976), who transferred his controlling interest in Hughes Aircraft Company to the tax-exempt foundation in 1953 primarily as a tax avoidance strategy. After Hughes's death (1976) and subsequent litigation, the Institute was restructured as a genuine scientific philanthropic organisation under the directorship of Donald Fredrickson (1987), who transformed it into the most influential private funder of basic biomedical science in the world.\n\n"
            "HHMI's research model — funding the investigator rather than the project, providing long-term support that tolerates failure and encourages risk-taking — has produced an extraordinary concentration of Nobel laureates: HHMI Investigators have received 28 Nobel Prizes, 17 Lasker Awards, and 15 National Medals of Science. HHMI's emphasis on long-term investigator support, tolerance for risk, and freedom from short-term grant cycles has made it the counterweight to the NIH's project-focused grant system."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Largest private biomedical research funder in world (est. 1953); $23 billion endowment (2023); $900m+ annual research expenditure; ~300 Investigators at US universities; 28 Nobel Prizes by HHMI Investigators; founded by Howard Hughes as tax strategy, later transformed into genuine scientific philanthropy; funds investigator rather than project — tolerating failure and risk-taking; counterweight to NIH's short-term grant system.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Howard Hughes's transfer of Hughes Aircraft Company to the HHMI (1953) — primarily as a tax avoidance strategy to reduce estate taxes — accidentally created the endowment for what would become the world's largest private biomedical research funder",
            "The restructuring of HHMI after Hughes's death (1976) — under the legal direction of the IRS and the guidance of scientific advisors including Donald Fredrickson — transformed a tax shelter into a genuine philanthropic institution committed to funding the most creative basic biomedical research",
            "The failure of the NIH's project-based grant system to support long-term high-risk basic research — an increasing problem as NIH grants became shorter, more competitive, and more focused on near-term translational outcomes — created the institutional niche for HHMI's investigator model"
        ],
        "effects": [
            "HHMI's investigator model — providing long-term support to exceptional scientists regardless of specific project outcomes — has produced a concentration of Nobel laureates (28 prizes) and transformative discoveries that demonstrates the superiority of long-term investigator support over short-term project funding for frontier science",
            "HHMI's funding has been critical to several of the most important biomedical discoveries of the late 20th and early 21st centuries, including the discovery of the olfactory receptor family (Richard Axel and Linda Buck, Nobel 2004), the characterisation of G-protein-coupled signalling (Robert Lefkowitz, Nobel 2012), and work on CRISPR gene editing",
            "HHMI's Janelia Research Campus (Virginia, opened 2006) — a dedicated residential research campus for neuroscience and imaging — created a new institutional model combining the research culture of Bell Labs (long-term, collaborative, interdisciplinary) with the biomedical focus of a medical research institute",
            "HHMI's role as the largest private counterweight to NIH funding — providing research support with longer time horizons and greater risk tolerance — has maintained the capacity for the most ambitious and speculative basic biomedical science that drives the frontier of biological knowledge"
        ],
        "relationships": [
            {"entity": "Howard Hughes (billionaire aviator and industrialist)", "relationship": "FOUNDED_BY", "note": "Hughes founded HHMI (1953) initially as a tax avoidance strategy — inadvertently creating what would become the world's largest private biomedical research funder"},
            {"entity": "NIH (National Institutes of Health)", "relationship": "COMPLEMENTARY_COUNTERWEIGHT_TO_SHORT_TERM_GRANT_SYSTEM_OF", "note": "HHMI's long-term investigator model is the primary counterweight to NIH's project-based grant system — supporting risk-taking that NIH funding discourages"},
            {"entity": "Nobel Prizes in Physiology or Medicine (28 HHMI investigators)", "relationship": "28_PRIZES_WON_BY_INVESTIGATORS_SUPPORTED_BY", "note": "28 Nobel Prizes by HHMI Investigators — more than any private research philanthropy — validate the investigator-support model"},
            {"entity": "Janelia Research Campus (Virginia, 2006)", "relationship": "OPERATES_THE", "note": "HHMI's Janelia campus — a residential neuroscience and imaging research facility modelled on Bell Labs — is a new institutional model for frontier biomedical science"},
            {"entity": "CRISPR gene editing (21st century)", "relationship": "FUNDED_KEY_RESEARCH_LEADING_TO", "note": "HHMI funded several of the researchers whose work contributed to the development of CRISPR-Cas9 gene editing — the most transformative biotechnology of the 21st century"}
        ],
    }),

    ("mit-computer-science-and-artificial-intelligence-laboratory", {
        "summary": (
            "MIT's Computer Science and Artificial Intelligence Laboratory (CSAIL, est. 1959 as the Computation Center; current CSAIL name from 2003 merger of LCS and AI Lab) is the largest computer science research institution in the world, and the birthplace of some of the most consequential computing technologies ever developed: time-sharing computing (1961), the MULTICS operating system (1964–1969), the RSA public-key cryptography algorithm (1977), the World Wide Web browser Mosaic's conceptual ancestor, and dozens of fundamental AI and robotics advances. CSAIL faculty and alumni have founded over 100 technology companies worth $2 trillion.\n\n"
            "The Artificial Intelligence Laboratory (AI Lab, est. 1959 by Marvin Minsky and John McCarthy) was the founding institution of AI research — the place where the first AI programs were written, where LISP programming language was created (McCarthy, 1958), where the concept of the 'semantic web' was developed, and where early robotics research created the first mobile robots. The Laboratory for Computer Science (LCS, est. 1963) produced ARPANET-related work, the RSA cryptography algorithm (Rivest, Shamir, Adleman, 1977), and foundational networking research.\n\n"
            "CSAIL's current research covers robotics, machine learning, natural language processing, computer vision, theoretical computer science, and quantum computing — with 115 faculty members and 900+ researchers making it the largest laboratory at MIT. CSAIL's building (Ray and Maria Stata Center, designed by Frank Gehry, 2004) is one of the most celebrated works of 21st-century architecture, its deconstructivist towers symbolising the creative disorder of computing research."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Largest computer science research institution in world (est. 1959); birthplace of time-sharing computing (1961), MULTICS OS (1964), RSA cryptography (1977), LISP programming language (McCarthy 1958), foundational AI and robotics research; founded by Marvin Minsky and John McCarthy as the founding AI Lab; alumni founded 100+ companies worth $2 trillion; Frank Gehry's Stata Center (2004) — landmark 21st-century architecture.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "MIT's position as the primary US university for applied mathematics, electrical engineering, and physics — combined with its close relationship with the US military-industrial complex through DARPA and the Lincoln Laboratory — created the institutional environment that made it the natural home for the first computer science research",
            "The DARPA-funded AI research programme of the 1960s — driven by Cold War competition with the Soviet Union — provided the financial base for MIT's AI Lab to become the world's leading centre for artificial intelligence research",
            "Marvin Minsky and John McCarthy's founding vision for the AI Lab (1959) — that machine intelligence could be created within a generation — created the most ambitious long-term research agenda in computing history, establishing MIT's AI Lab as the institutional home of the AI research community"
        ],
        "effects": [
            "Time-sharing computing (MIT, 1961) — the invention that made multiple users share a single mainframe computer interactively — created the conceptual and technical foundation for modern interactive computing, the internet, and cloud computing",
            "The RSA cryptography algorithm (Rivest, Shamir, Adleman, 1977) — discovered at MIT's LCS — is the foundation of public-key cryptography that secures all modern internet transactions, from banking to email to messaging",
            "LISP (McCarthy, 1958) — the second-oldest programming language still in use — created the computational paradigm for symbolic AI research and influenced the development of functional programming, garbage collection, and many modern programming language features",
            "CSAIL's 100+ alumni companies — including Akamai Technologies, Dropbox, and dozens of AI startups — have generated $2 trillion in market value, making MIT's computer science research the most economically productive academic research programme in history"
        ],
        "relationships": [
            {"entity": "Marvin Minsky and John McCarthy (founders of AI Lab)", "relationship": "CO-FOUNDED_AI_LAB_BY", "note": "Minsky and McCarthy co-founded the MIT AI Lab (1959) — the founding institution of artificial intelligence research and the birthplace of LISP"},
            {"entity": "RSA cryptography algorithm (1977)", "relationship": "BIRTHPLACE_OF_THE", "note": "Rivest, Shamir, and Adleman discovered RSA at MIT's LCS (1977) — the foundation of public-key cryptography securing all modern internet transactions"},
            {"entity": "Time-sharing computing (MIT, 1961)", "relationship": "BIRTHPLACE_OF", "note": "MIT invented time-sharing (1961) — making interactive shared computing possible and creating the conceptual foundation for the modern internet"},
            {"entity": "Stata Center (Frank Gehry, 2004)", "relationship": "HOUSED_IN_THE_ARCHITECTURALLY_CELEBRATED", "note": "CSAIL's Ray and Maria Stata Center — designed by Frank Gehry — is one of the most celebrated works of 21st-century architecture"},
            {"entity": "LISP programming language (1958)", "relationship": "BIRTHPLACE_OF_THE", "note": "John McCarthy created LISP at MIT (1958) — the foundational AI programming language and the second oldest language still in use"}
        ],
    }),

    ("brookhaven-national-laboratory", {
        "summary": (
            "Brookhaven National Laboratory (BNL, est. 1947, Upton, Long Island, New York) is a US Department of Energy multipurpose national laboratory that has been the site of 7 Nobel Prize-winning discoveries, including the discovery of the muon neutrino (1962, Nobel 1988), the discovery of CP violation (1964, Nobel 1980), and research leading to discoveries in quantum chromodynamics. Brookhaven's National Synchrotron Light Source (NSLS) is one of the world's most productive X-ray and light source facilities, used by thousands of researchers annually for studies ranging from materials science to drug discovery.\n\n"
            "Brookhaven was established on the site of Camp Upton (a former World War I and II military base) to provide a major research facility for the northeastern United States universities after World War II — part of the US government's post-war investment in national science infrastructure. The laboratory operates the Relativistic Heavy Ion Collider (RHIC, operational 2000) — the world's first heavy-ion collider — which discovered the quark-gluon plasma, the state of matter that existed microseconds after the Big Bang, by colliding gold atoms at near light speed.\n\n"
            "Brookhaven's environmental history includes a significant radioactive water leak from its High Flux Beam Reactor (1996–2000) that led to community protests and the reactor's permanent shutdown — a landmark case in the interaction between large-scale national laboratories and the communities in which they are located. The laboratory is also one of the leading institutions in nuclear medicine, having developed the first technetium-99m generator, which provides the most widely used diagnostic radioisotope in modern nuclear medicine."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "US multipurpose national laboratory (est. 1947); 7 Nobel Prize-winning discoveries; discovered muon neutrino (1962) and CP violation (1964); RHIC (2000) — world's first heavy-ion collider — discovered quark-gluon plasma (matter microseconds after Big Bang); NSLS light source used by thousands annually; technetium-99m generator — most widely used diagnostic radioisotope; radioactive leak controversy (1996–2000).",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The post-World War II US government investment in national science infrastructure — and the need for a major research facility accessible to northeastern US universities — created the institutional mandate for Brookhaven, using the existing Camp Upton military base",
            "The Cold War competition with the Soviet Union in nuclear physics and particle research — and the availability of wartime nuclear physics expertise from the Manhattan Project — provided both the political motivation and the scientific workforce for Brookhaven's establishment",
            "The development of synchrotron X-ray light sources as the primary tool for materials science, structural biology, and drug discovery research — and the enormous capital cost of such facilities — created the natural role for a national laboratory providing shared access to world-class instrumentation"
        ],
        "effects": [
            "The discovery of the muon neutrino at Brookhaven (1962, Nobel 1988) established that neutrinos come in distinct flavours — opening the field of neutrino physics that has become one of the most active frontiers of particle physics",
            "The discovery of CP violation at Brookhaven (1964, Nobel 1980) — demonstrating that the universe is not perfectly symmetric between matter and antimatter — provided the theoretical foundation for understanding why the Big Bang produced a matter-dominated universe rather than equal amounts of matter and antimatter",
            "The RHIC collider's discovery of the quark-gluon plasma (2005) — matter in the state that existed in the first microseconds after the Big Bang — provided the first experimental window into the conditions of the early universe",
            "Brookhaven's development of the technetium-99m generator — the source of the most widely used diagnostic radioisotope in nuclear medicine, used in approximately 40 million medical procedures annually — made the laboratory a foundational contributor to modern medical diagnosis"
        ],
        "relationships": [
            {"entity": "Muon neutrino discovery (1962, Nobel 1988)", "relationship": "SITE_OF_THE", "note": "Brookhaven's discovery of the muon neutrino (1962) — showing that neutrinos come in distinct flavours — earned the Nobel Prize in 1988"},
            {"entity": "CP violation discovery (1964, Nobel 1980)", "relationship": "SITE_OF_THE", "note": "The CP violation discovery at Brookhaven (1964) — showing matter-antimatter asymmetry — earned the Nobel Prize in 1980 and explained why the universe contains matter"},
            {"entity": "RHIC (Relativistic Heavy Ion Collider, 2000)", "relationship": "OPERATES_THE", "note": "RHIC — the world's first heavy-ion collider — discovered the quark-gluon plasma at Brookhaven, the state of matter from the first microseconds after the Big Bang"},
            {"entity": "Technetium-99m generator (nuclear medicine)", "relationship": "DEVELOPED_THE_DIAGNOSTIC_RADIOISOTOPE_GENERATOR_FOR", "note": "Brookhaven developed the technetium-99m generator — used in 40 million medical procedures annually as the most widely used diagnostic radioisotope"},
            {"entity": "High Flux Beam Reactor water leak controversy (1996–2000)", "relationship": "SITE_OF_LANDMARK_COMMUNITY-LABORATORY_CONFLICT_OVER", "note": "The radioactive water leak controversy led to the reactor's shutdown — a landmark case in the relationship between national labs and host communities"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 26 — {len(ENTITIES)} entities (Class 350: Famous Research Institutions & Laboratories)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
