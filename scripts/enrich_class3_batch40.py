#!/usr/bin/env python3
"""
Batch 40 — 8 entities (Class 381): Major World Universities (Part 2)
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
    print(f"  ✓ {entity['name']} — sum={slen}c c={len(det.get('causes', []))} e={len(det.get('effects', []))}")


ENTITIES = [

    ("columbia-university", {
        "summary": (
            "Columbia University (est. 1754, New York City — founded as King's College by royal charter of King George II, the fifth-oldest US university) is one of the world's most influential research universities — the home of the Pulitzer Prize (endowed by Joseph Pulitzer, whose bequest created the journalism school), the institution where the Manhattan Project's first nuclear reactor (CP-1 precursor, 1939) was designed, and the alma mater of 3 US Presidents (Alexander Hamilton, Barack Obama, Franklin D. Roosevelt) and 101 Nobel laureates. Columbia's position in New York City — the world's most influential media, finance, and cultural capital — has made it uniquely connected to global intellectual and cultural life.\n\n"
            "Columbia was founded in 1754 as King's College — and renamed Columbia after the American Revolution — on the grounds of Trinity Church in Lower Manhattan, before moving to its current Morningside Heights campus in 1897 (designed by McKim, Mead & White in the Beaux-Arts style). Columbia's growth into a world-class research university was driven by the founding of professional schools — the School of Law (1858), College of Physicians and Surgeons (1767, the oldest medical school in North America), School of Journalism (1912), and Graduate School of Business — and by its position as the primary New York City research university.\n\n"
            "Columbia's specific contributions include Enrico Fermi's nuclear fission experiments (1939), the invention of FM radio by Edwin Armstrong (1933), the development of streptomycin by Selman Waksman, and the Beat Generation's literary formation (Allen Ginsberg, Jack Kerouac, and the Columbia circle). Columbia's 1968 student occupation of the campus became one of the defining moments of the global 1968 student revolt."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Fifth-oldest US university (est. 1754 as King's College, George II charter); 3 US Presidents (Hamilton, Obama, FDR); 101 Nobel laureates; Pulitzer Prize (Joseph Pulitzer bequest, journalism school 1912); Enrico Fermi nuclear fission experiments (1939, Manhattan Project); FM radio invention (Edwin Armstrong 1933); streptomycin (Selman Waksman); Beat Generation (Ginsberg, Kerouac); 1968 student occupation — defining global student revolt moment; College of Physicians and Surgeons (1767, oldest North American medical school); Morningside Heights campus (McKim, Mead & White 1897).",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "King George II's royal charter (1754) — establishing King's College as the fifth American colonial college, intended to provide an educated Anglican professional class for New York — reflected the colonial competition between Anglican and Puritan educational institutions that drove the multiplication of American colleges",
            "Joseph Pulitzer's bequest (1912) — endowing the Columbia School of Journalism and the Pulitzer Prizes — was the most consequential single act of journalism philanthropy in history, creating the world's most prestigious journalism prizes and establishing Columbia as the primary institution for professional journalism education",
            "Columbia's New York City location — placing it at the centre of American media, finance, law, publishing, and cultural production — gave it a structural advantage over other Ivy League universities, whose graduates tend to gravitate toward New York regardless of where they studied, making Columbia the university most directly embedded in New York's economic and cultural machinery"
        ],
        "effects": [
            "The Pulitzer Prize — awarded annually since 1917 for achievements in journalism, letters, drama, and musical composition — is the most prestigious prize in American journalism and literature, and Columbia's administration of it makes the university the primary institutional arbiter of quality in American cultural production",
            "Enrico Fermi's nuclear fission experiments at Columbia (1939–1942) — demonstrating that uranium fission could produce a chain reaction — were the theoretical and experimental foundation for the Manhattan Project, making Columbia the site of some of the most consequential scientific work in military history",
            "The Beat Generation's formation at Columbia — with Allen Ginsberg, Jack Kerouac, and their circle developing the literary and cultural sensibility that would transform American culture in the 1950s–1960s — made Columbia the institutional origin of one of the most influential counter-cultural movements in American history",
            "Columbia's 1968 student occupation — in which students seized university buildings to protest the university's connections to the Institute for Defense Analyses and its proposed gym in Morningside Park — became one of the defining images of the global 1968 student revolt, influencing student movements from Paris to Tokyo"
        ],
        "relationships": [
            {"entity": "Pulitzer Prize (Joseph Pulitzer bequest, administered by Columbia)", "relationship": "ADMINISTERS_THE_MOST_PRESTIGIOUS_PRIZE_IN_AMERICAN_JOURNALISM_THROUGH_THE", "note": "The Pulitzer Prize — the most prestigious prize in American journalism and literature — makes Columbia the primary institutional arbiter of quality in American cultural production"},
            {"entity": "Enrico Fermi nuclear fission experiments (Columbia, 1939)", "relationship": "SITE_OF_THE_EXPERIMENTAL_FOUNDATION_OF_THE_MANHATTAN_PROJECT_THROUGH_THE", "note": "Fermi's Columbia experiments (1939) demonstrating nuclear chain reactions were the theoretical foundation for the Manhattan Project"},
            {"entity": "Beat Generation (Ginsberg, Kerouac, Columbia circle)", "relationship": "INSTITUTIONAL_ORIGIN_OF_THE", "note": "The Beat Generation's literary formation at Columbia made it the institutional origin of one of the most influential counter-cultural movements in American history"},
            {"entity": "Barack Obama (BA 1983, 44th US President)", "relationship": "ALMA_MATER_OF", "note": "Obama's Columbia BA (1983) is one of three US Presidents' connections to Columbia, reflecting the university's disproportionate production of American political leaders"},
            {"entity": "1968 student occupation (defining global student revolt moment)", "relationship": "SITE_OF_THE", "note": "Columbia's 1968 student occupation became one of the defining images of the global student revolt, influencing student movements from Paris to Tokyo"}
        ],
    }),

    ("humboldt-university-berlin", {
        "summary": (
            "Humboldt-Universität zu Berlin (est. 1810, Berlin — founded by Wilhelm von Humboldt and King Friedrich Wilhelm III of Prussia as the University of Berlin) is the founding institution of the modern research university — the revolutionary educational model, based on Wilhelm von Humboldt's concept of Bildung (holistic self-cultivation through research), that transformed the university from a teaching institution into a research institution and became the template for all subsequent research universities worldwide, including the American graduate school system. Humboldt Berlin is the alma mater of 29+ Nobel laureates, 3 popes, and some of the most consequential thinkers in European intellectual history.\n\n"
            "Wilhelm von Humboldt's educational reform (1810) — articulated in his memorandum 'On the Internal and External Organization of the Higher Scientific Institutions in Berlin' — established four revolutionary principles: the unity of teaching and research (professors should do research, not merely teach received knowledge); academic freedom (professors and students should pursue truth without government interference); Bildung as holistic self-cultivation (education should develop the whole person, not merely provide professional training); and the unity of all sciences (all disciplines are interconnected). These principles transformed the university worldwide.\n\n"
            "Humboldt Berlin's faculty and alumni include Georg Wilhelm Friedrich Hegel, Arthur Schopenhauer, Heinrich Heine, Karl Marx, Max Planck, Albert Einstein, Werner Heisenberg, Max Born, Otto Hahn (nuclear fission), and Theodor Mommsen — reflecting its position as the primary institutional source of the scientific and philosophical revolutions of the 19th and early 20th centuries."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Founding institution of the modern research university (est. 1810, Wilhelm von Humboldt); Humboldtian ideal — unity of teaching and research, academic freedom, Bildung, unity of all sciences; template for all subsequent research universities worldwide including American graduate school system; 29+ Nobel laureates; alumni: Hegel, Marx, Schopenhauer, Heine, Planck, Einstein, Heisenberg, Born, Otto Hahn (nuclear fission), Mommsen; 3 popes; primary institutional source of 19th–20th century scientific and philosophical revolutions.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Prussia's military defeat by Napoleon (1806–1807) and the destruction of the University of Halle — the main Prussian university — created the political need for a new university in Berlin, and Wilhelm von Humboldt's appointment as head of the Prussian education department gave him the opportunity to implement his radical educational vision",
            "Wilhelm von Humboldt's concept of Bildung — the idea that education should develop the whole person through engagement with knowledge, not merely provide professional training — was a philosophical response to the Enlightenment's fragmentation of knowledge into specialized professions and trades",
            "The Prussian state's willingness to fund a research-oriented university — providing permanent academic salaries, laboratory facilities, and research infrastructure — created the material conditions for the Humboldtian model's success and its replication in other German states"
        ],
        "effects": [
            "The Humboldtian research university model — unity of teaching and research, academic freedom, Bildung — was adopted by all major German universities in the 19th century, and then by American universities (Johns Hopkins was the first American university explicitly modelled on the German research university, 1876), transforming higher education worldwide",
            "Humboldt Berlin's concentration of the leading scientific minds of the 19th–20th centuries — Einstein, Planck, Heisenberg, Born, Hahn, Mommsen — made it the primary institutional source of the scientific revolutions (quantum mechanics, nuclear physics, historical scholarship) that transformed European and global intellectual life",
            "Otto Hahn's discovery of nuclear fission at Humboldt Berlin's Kaiser Wilhelm Institute for Chemistry (1938) — for which he received the Nobel Prize (1944) — was the most consequential scientific discovery of the 20th century, leading directly to the Manhattan Project and the nuclear age",
            "The American graduate school system — modelled explicitly on the German research university by Johns Hopkins (1876) and subsequently adopted by Harvard, Yale, Columbia, and all American research universities — is the direct institutional descendant of Humboldt's 1810 Berlin model, making Humboldt's educational philosophy the foundation of the global research university system"
        ],
        "relationships": [
            {"entity": "Wilhelm von Humboldt (founder 1810, Humboldtian ideal)", "relationship": "FOUNDED_BY_AND_HUMBOLDTIAN_UNIVERSITY_MODEL_CREATED_BY", "note": "Humboldt's 1810 founding memorandum — unity of teaching and research, academic freedom, Bildung — was the most consequential document in the history of university education"},
            {"entity": "American research universities (Johns Hopkins 1876, Humboldtian model)", "relationship": "FOUNDING_MODEL_FOR_THE", "note": "Johns Hopkins (1876) explicitly modelled itself on the Humboldtian research university — and all American graduate schools follow the Humboldt Berlin model"},
            {"entity": "Otto Hahn (nuclear fission, Kaiser Wilhelm Institute, 1938)", "relationship": "INSTITUTIONAL_HOME_OF_THE_DISCOVERY_OF", "note": "Hahn's discovery of nuclear fission (1938) at Humboldt's associated Kaiser Wilhelm Institute was the most consequential scientific discovery of the 20th century"},
            {"entity": "Max Planck, Einstein, Heisenberg, Born (quantum mechanics faculty)", "relationship": "INSTITUTIONAL_HOME_OF_THE_FOUNDING_FIGURES_OF", "note": "Humboldt Berlin's faculty in the 1910s–1930s — Planck, Einstein, Heisenberg, Born — made it the primary institutional source of the quantum mechanics revolution"},
            {"entity": "Hegel, Marx, Schopenhauer (philosophical alumni)", "relationship": "ALMA_MATER_OF_THE_MOST_CONSEQUENTIAL_PHILOSOPHERS_OF_THE_19TH_CENTURY", "note": "Hegel, Marx, and Schopenhauer — all associated with Humboldt Berlin — are the three most influential philosophers of the 19th century, whose ideas shaped politics, economics, and cultural theory worldwide"}
        ],
    }),

    ("peking-university", {
        "summary": (
            "Peking University (Beijing Daxue / Beida, est. 1898, Beijing — founded during the Hundred Days' Reform as the Imperial University of Peking) is China's most prestigious and historically influential university — the institution that served as the intellectual centre of the May Fourth Movement (1919), the New Culture Movement, and the Chinese Communist Party's intellectual formation, and that has remained China's most elite academic institution through imperial, republican, and communist eras. Peking University's role in modern Chinese history — as the university whose professors and students led the intellectual and political movements that created modern China — is without parallel in any other country's higher education system.\n\n"
            "Peking University was founded in 1898 during the Hundred Days' Reform — the abortive modernisation programme of the Guangxu Emperor — as the Imperial University of Peking, China's first modern national university. Under Cai Yuanpei's presidency (1916–1927), Peking University became the centre of the New Culture Movement, hosting Chen Duxiu (founder of the Chinese Communist Party), Li Dazhao (CCP co-founder), and Lu Xun (the greatest modern Chinese writer) on its faculty, and becoming the intellectual crucible of the May Fourth Movement.\n\n"
            "The May Fourth Movement (4 May 1919) — in which Peking University students demonstrated against the humiliating terms of the Treaty of Versailles that transferred German concessions in China to Japan — was the defining event of Chinese intellectual modernity, demanding 'Mr. Science and Mr. Democracy' and launching the cultural and political transformation of China that led to the founding of the CCP (1921) and the People's Republic (1949)."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "China's most prestigious and historically influential university (est. 1898, Hundred Days' Reform, Imperial University of Peking); Cai Yuanpei presidency (1916–1927) — Chen Duxiu (CCP founder), Li Dazhao (CCP co-founder), Lu Xun on faculty; May Fourth Movement (4 May 1919) — students demanded 'Mr. Science and Mr. Democracy', launched cultural/political transformation of China; intellectual centre of New Culture Movement; founding of CCP (1921); founding of People's Republic (1949); China's most elite institution through imperial, republican, and communist eras.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Hundred Days' Reform (1898) — the Guangxu Emperor's abortive modernisation programme, inspired by the Meiji Restoration and by Chinese reformers' recognition that China needed Western-style education — drove the founding of the Imperial University of Peking as China's first modern national university",
            "Cai Yuanpei's appointment as president (1916) — and his introduction of academic freedom, tolerance of diverse ideological tendencies (including early Marxism), and invitation to China's most radical intellectuals to join the faculty — transformed Peking University into the intellectual centre of the Chinese modernisation debate",
            "The Treaty of Versailles (1919) — which transferred German concessions in China to Japan rather than restoring Chinese sovereignty — created the political outrage that ignited the May Fourth Movement, with Peking University students as its primary organisers and Peking University faculty as its intellectual leaders"
        ],
        "effects": [
            "The May Fourth Movement (1919) — launched from Peking University — was the defining event of Chinese intellectual modernity, establishing science and democracy as China's modernisation goals and launching the cultural and political movements that created the Chinese Communist Party (1921) and shaped the People's Republic (1949)",
            "The Chinese Communist Party's intellectual formation — Chen Duxiu and Li Dazhao were Peking University faculty when they co-founded the CCP (1921) — makes Peking University the institutional origin of the communist movement that governed China for 75+ years, the most consequential connection between a university and a governing political party in modern history",
            "Peking University's maintenance of relative academic independence under the People's Republic — including the 1957 Hundred Flowers Campaign (in which Peking University faculty and students were encouraged to criticise the CCP before the Anti-Rightist Campaign reversed course) and the 1989 Tiananmen Square protests (which began at Peking University) — made it the primary institutional site of Chinese intellectual dissent",
            "Peking University's global ranking (consistently in the world's top 20 for computer science and mathematics) and its production of China's technological leadership — providing the faculty, researchers, and entrepreneurs who built Baidu, Lenovo, and other Chinese technology companies — makes it the institutional source of China's 21st-century technology ambitions"
        ],
        "relationships": [
            {"entity": "Hundred Days' Reform (1898, founding context)", "relationship": "FOUNDED_DURING_THE", "note": "The Guangxu Emperor's 1898 modernisation programme — China's first attempt at Western-style educational reform — drove the founding of the Imperial University of Peking"},
            {"entity": "May Fourth Movement (4 May 1919, students and faculty)", "relationship": "PRIMARY_INSTITUTIONAL_ORIGIN_OF_THE", "note": "The May Fourth Movement — demanding 'Mr. Science and Mr. Democracy' — was launched by Peking University students and faculty, defining Chinese intellectual modernity"},
            {"entity": "Chen Duxiu and Li Dazhao (CCP co-founders, Peking University faculty)", "relationship": "INSTITUTIONAL_HOME_OF_THE_FOUNDING_FACULTY_OF_THE_CHINESE_COMMUNIST_PARTY", "note": "Chen Duxiu and Li Dazhao were Peking University faculty when they co-founded the CCP (1921) — making Peking University the institutional origin of the Chinese communist movement"},
            {"entity": "Cai Yuanpei (president 1916–1927, academic freedom)", "relationship": "INTELLECTUAL_TRANSFORMATION_DRIVEN_BY_THE_PRESIDENCY_OF", "note": "Cai's introduction of academic freedom and tolerance of diverse ideologies — including early Marxism — transformed Peking University into the centre of China's modernisation debate"},
            {"entity": "1989 Tiananmen Square protests (began at Peking University)", "relationship": "PRIMARY_INSTITUTIONAL_SITE_OF_THE", "note": "The 1989 Tiananmen Square democracy movement — which began at Peking University — was the university's most recent expression of its role as the primary site of Chinese intellectual dissent"}
        ],
    }),

    ("lund-university", {
        "summary": (
            "Lund University (est. 1666, Lund, Sweden — founded after the region of Scania was ceded from Denmark to Sweden by the Treaty of Roskilde, 1658) is Scandinavia's most prestigious and largest university — with 40,000+ students, 8 faculties, and 8 Nobel laureates among its alumni and faculty. Lund's founding was a deliberate act of Swedish state-building in newly acquired territory: King Karl X Gustav founded it to 'Swedify' (Försvenska) the recently Danish province of Scania by establishing a Swedish-language university. Lund University has been the primary scientific institution of southern Sweden for 360 years and the primary institution of Scandinavian research collaboration.\n\n"
            "Lund was founded in 1666 — just eight years after the Treaty of Roskilde ceded Scania from Denmark — by royal charter, with the explicit purpose of training Swedish civil servants, clergy, and medical professionals for the newly Swedish province. The university's early faculties were Theology, Law, Medicine, and Philosophy — the standard quartet of the 17th-century European university. Lund's transformation into a research university in the 19th century — with the establishment of research institutes, natural history collections, and professional schools — was driven by the Humboldtian influence that transformed all Swedish universities.\n\n"
            "Lund's modern research strengths include the European Spallation Source (ESS, est. 2019, the world's most powerful neutron source, located in Lund) and MAX IV (the world's brightest synchrotron radiation laboratory, est. 2016), making Lund the site of two of the world's most powerful scientific research facilities and the primary node of European neutron and synchrotron research."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Scandinavia's most prestigious and largest university (est. 1666, Lund, Sweden); founded to 'Swedify' newly acquired Danish province of Scania after Treaty of Roskilde (1658); King Karl X Gustav royal charter; 40,000+ students, 8 faculties; 8 Nobel laureates; European Spallation Source (ESS, 2019, world's most powerful neutron source); MAX IV (world's brightest synchrotron radiation laboratory, 2016); primary node of European neutron and synchrotron research; 360 years of Scandinavian scientific leadership.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Treaty of Roskilde (1658) — ceding Scania from Denmark to Sweden — created the political need for a Swedish university to 'Swedify' the recently Danish province, educate Swedish civil servants and clergy, and assert Swedish cultural sovereignty over the newly acquired territory",
            "King Karl X Gustav's royal charter (1666) — establishing Lund University with royal patronage and permanent funding — reflected the 17th-century European pattern of using universities as instruments of state-building and cultural integration in conquered or disputed territories",
            "The European Spallation Source's selection of Lund (2009) — after a competitive bid from several European countries — was driven by Sweden's established scientific infrastructure, Lund University's research strengths in materials science and physics, and the existing MAX synchrotron facility, creating a research cluster that positioned Lund as a global node of materials science and neutron research"
        ],
        "effects": [
            "The European Spallation Source (ESS, 2019) and MAX IV (2016) — the world's most powerful neutron source and brightest synchrotron radiation laboratory respectively — have made Lund the primary destination for European materials science, condensed matter physics, and structural biology research, attracting 5,000+ researchers annually from 30+ countries",
            "Lund University's 360-year role as the primary educational institution of southern Sweden — training the civil servants, lawyers, doctors, clergy, and scientists of the region — has made it the primary institutional source of the Scanian professional class, demonstrating how universities serve as instruments of cultural and political integration",
            "Lund's international research collaborations — particularly through the ESS and MAX IV, which are funded by 15 European countries — have made it the primary model for how mid-sized European universities can punch above their weight in global research by hosting international large-scale research infrastructure",
            "Lund's founding as a Swedish cultural-political instrument in formerly Danish territory — and the university's subsequent success in integrating Scania into Swedish academic and professional culture — is one of the clearest examples of how universities function as instruments of national cultural policy"
        ],
        "relationships": [
            {"entity": "Treaty of Roskilde (1658, Scania ceded Denmark to Sweden)", "relationship": "POLITICAL_FOUNDATION_AND_DIRECT_CAUSE_OF_THE_FOUNDING_OF", "note": "The Treaty of Roskilde's cession of Scania created the state-building need that drove Lund's founding — to 'Swedify' the newly Danish province through education"},
            {"entity": "European Spallation Source (ESS, 2019, world's most powerful neutron source)", "relationship": "HOST_INSTITUTION_OF_THE", "note": "The ESS — the world's most powerful neutron source — positioned Lund as the global node of European neutron research, attracting 5,000+ researchers annually"},
            {"entity": "MAX IV (world's brightest synchrotron radiation laboratory, 2016)", "relationship": "HOST_INSTITUTION_OF_THE", "note": "MAX IV — the world's brightest synchrotron — together with ESS makes Lund the primary destination for European materials science and structural biology research"},
            {"entity": "King Karl X Gustav (royal charter founder, 1666)", "relationship": "FOUNDED_BY_ROYAL_CHARTER_OF", "note": "Karl X Gustav's 1666 charter — founding Lund to educate Swedish civil servants in the newly acquired Scanian province — reflected the 17th-century pattern of using universities as state-building instruments"},
            {"entity": "Scania province (formerly Danish, cultural integration mission)", "relationship": "FOUNDED_TO_CULTURALLY_INTEGRATE_THE", "note": "Lund's 360-year role as the primary educational institution of Scania is one of history's clearest examples of a university functioning as an instrument of national cultural policy"}
        ],
    }),

    ("ghent-university", {
        "summary": (
            "Ghent University (Universiteit Gent / UGent, est. 1817, Ghent, Belgium — founded by King William I of the Netherlands as one of three new state universities) is one of Europe's most innovative research universities — Belgium's largest university with 44,000+ students and the primary driver of Belgian scientific research in the life sciences, biotechnology, and social sciences. Ghent University was the first European university to become fully Dutch-language (1930), making it the primary institutional engine of the Flemish cultural movement that transformed Belgian politics, and its Institute for Biotechnology Ghent (VIB) is the most productive biotechnology research centre per capita in Europe.\n\n"
            "Ghent University was founded in 1817 — during the United Kingdom of the Netherlands — as one of three state universities (with Liège and Louvain) created by King William I to provide higher education for the new kingdom. Initially a French-language institution, Ghent became the battleground for the Flemish language movement's demand for Dutch-language university education — a campaign that succeeded in 1930 when Ghent became the first European university to switch entirely to the vernacular language of its student population.\n\n"
            "Ghent's research profile is distinctive for the concentration of top-level work across molecular biology, food science, pharmaceutical biotechnology, plant genetics, and social science — a breadth of excellence in life science applications that reflects Belgium's pharmaceutical and food industries. The VIB Centre for Plant Biology — which developed herbicide-resistant and pest-resistant genetically modified crops — has been among the world's most consequential agricultural biotechnology research centres."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "Europe's most innovative research universities; Belgium's largest university (est. 1817, King William I of Netherlands); 44,000+ students; first European university fully Dutch-language (1930) — primary institutional engine of Flemish cultural movement; VIB (Institute for Biotechnology Ghent) — most productive European biotechnology research centre per capita; molecular biology, food science, pharmaceutical biotechnology, plant genetics; VIB Centre for Plant Biology — herbicide-resistant and pest-resistant GM crops.",
            "significanceCategory": "regional"
        },
        "causes": [
            "King William I's founding of Ghent as a state university (1817) — intended to educate the professional class of the new United Kingdom of the Netherlands — placed higher education in Flanders in a French-language context that would become politically untenable as the Flemish cultural movement gathered strength",
            "The Flemish language movement's decades-long campaign for Dutch-language higher education in Flanders — which made Ghent the primary political battleground for Flemish linguistic rights — culminated in the 1930 language law that transformed Ghent into the first European university to operate entirely in the vernacular language of its student population",
            "Belgium's concentration of pharmaceutical, food processing, and chemical industries in the Ghent-Antwerp corridor — which created both the industrial demand for applied life science research and the commercial partnerships that funded biotechnology research — provided the material conditions for Ghent's distinctive strength in applied life sciences"
        ],
        "effects": [
            "Ghent's transformation into a Dutch-language university (1930) was the primary institutional driver of the Flemish cultural movement's legitimisation — demonstrating that Dutch could be the language of the highest intellectual achievement, and giving the Flemish movement its most powerful argument for full linguistic equality in Belgium",
            "The VIB Centre for Plant Biology's development of herbicide-resistant and pest-resistant genetically modified crops — which has been at the centre of global debates about agricultural biotechnology — made Ghent the primary European institutional voice in the GM crops controversy, with VIB research both advancing agricultural productivity and generating the scientific arguments in the public debate about biotechnology safety",
            "Ghent's partnership with the pharmaceutical and food industries of the Belgian-Dutch industrial corridor — including BASF, Bayer CropScience, and Janssen Pharmaceutica — has created a research translation model that produces more patent applications per faculty member than most European universities, demonstrating how proximity to industry concentration can maximise research commercialisation",
            "Ghent's development as a bilingual French/Dutch institution that became fully Dutch reflects the broader pattern of language politics in European universities — demonstrating how language choice in higher education can be a decisive factor in cultural and political identity formation"
        ],
        "relationships": [
            {"entity": "King William I of Netherlands (founder 1817, state university system)", "relationship": "FOUNDED_BY", "note": "William I's 1817 founding of three state universities — Ghent, Liège, Louvain — provided higher education for the new United Kingdom of the Netherlands"},
            {"entity": "Flemish language movement (Dutch-language university campaign)", "relationship": "PRIMARY_INSTITUTIONAL_BATTLEGROUND_AND_EVENTUAL_VICTORY_SITE_OF_THE", "note": "Ghent's 1930 transformation into a fully Dutch-language university was the Flemish movement's primary institutional victory — legitimising Dutch as a language of the highest academic achievement"},
            {"entity": "VIB (Institute for Biotechnology Ghent, most productive European per capita)", "relationship": "HOSTS_EUROPE'S_MOST_PRODUCTIVE_PER_CAPITA_BIOTECHNOLOGY_RESEARCH_CENTRE", "note": "The VIB — most productive European biotechnology centre per capita — reflects Ghent's distinctive strength in applied life science research"},
            {"entity": "VIB Centre for Plant Biology (GM crops research)", "relationship": "INSTITUTIONAL_HOME_OF_THE_LEADING_EUROPEAN_RESEARCH_ON", "note": "The VIB Plant Biology Centre's GM crop research made Ghent the primary European institutional voice in the agricultural biotechnology debate"},
            {"entity": "Belgian pharmaceutical and food industries (research partnership)", "relationship": "INDUSTRIAL_RESEARCH_TRANSLATION_MODEL_BUILT_WITH_THE", "note": "Ghent's partnership with Belgian-Dutch pharmaceutical and food companies creates more patent applications per faculty member than most European universities"}
        ],
    }),

    ("university-of-vienna", {
        "summary": (
            "The University of Vienna (Universität Wien, est. 1365, Vienna — founded by Rudolf IV, Duke of Austria, one of the oldest universities in the German-speaking world) is Austria's largest and most prestigious research university — the alma mater of 21 Nobel laureates, 15 heads of state, and the intellectual home of some of the most consequential intellectual movements in history: the Vienna Circle (logical positivism, 1920s–1930s), the Austrian School of Economics (Mises, Hayek, Schumpeter), Sigmund Freud's development of psychoanalysis, and the Second Vienna School of Music (Arnold Schoenberg, twelve-tone composition). The University of Vienna's 660-year history makes it the oldest German-language university after Prague.\n\n"
            "The University of Vienna was founded in 1365 by Rudolf IV, Duke of Austria — and reconstituted under Emperor Frederick III in 1384 — as part of the Habsburg dynasty's cultural competition with the Czech Luxembourgs who had founded the University of Prague (1348). Vienna's medieval reputation rested on its theology, law, and medicine faculties; its 19th-century transformation under Maria Theresa and Joseph II's reforms made it Austria's primary research university and the intellectual centre of the Habsburg Empire.\n\n"
            "Vienna's intellectual golden age (c.1870–1938) — producing the Vienna Circle, the Austrian School, Freud's psychoanalysis, Schoenberg's twelve-tone music, Wittgenstein's philosophy, and the Social Democratic Red Vienna housing and social programmes — was the most concentrated period of intellectual production in any European city outside Paris, making Vienna the primary generator of the ideas that shaped 20th-century intellectual culture."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Austria's largest and oldest research university (est. 1365, Rudolf IV, Duke of Austria); second-oldest German-language university; 21 Nobel laureates, 15 heads of state; Vienna Circle (logical positivism, 1920s–1930s — Schlick, Carnap, Neurath); Austrian School of Economics (Mises, Hayek, Schumpeter); Sigmund Freud (psychoanalysis); Second Vienna School (Schoenberg, twelve-tone composition); Wittgenstein; Red Vienna social programmes; Vienna intellectual golden age (c.1870–1938) — most concentrated European intellectual production outside Paris.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Rudolf IV's founding of the University of Vienna (1365) as part of the Habsburg dynasty's cultural competition with the Czech Luxembourgs who had founded Prague University (1348) — and the Habsburgs' desire to have their own prestigious university in Vienna — created the institutional foundation that would eventually make Vienna one of Europe's intellectual capitals",
            "The Habsburg Empire's multicultural intellectual environment — combining German, Czech, Hungarian, Italian, Jewish, and Slavic intellectual traditions in a single empire — created the uniquely cosmopolitan environment in which the Vienna Circle, Austrian School, and Freudian psychoanalysis all developed, drawing on diverse traditions that would have been impossible in a more culturally homogeneous environment",
            "The Jewish Enlightenment (Haskalah) and the Austrian Jews' disproportionate contribution to Viennese intellectual life — Freud, Wittgenstein, Schoenberg, Mahler, Schnitzler, Karl Kraus — created the conditions for Vienna's extraordinary intellectual density, with the subsequent destruction of this community by Nazism accounting for much of the abrupt end of Vienna's intellectual golden age after 1938"
        ],
        "effects": [
            "The Vienna Circle's logical positivism — developed in seminars at the University of Vienna (1924–1936, under Moritz Schlick, Rudolf Carnap, Otto Neurath) — was the dominant movement in 20th-century analytic philosophy, establishing the verification principle (the meaning of a statement is its method of verification) that shaped philosophy of science worldwide",
            "The Austrian School of Economics — founded at the University of Vienna (Carl Menger, 1871; Eugen Böhm-Bawerk; Ludwig von Mises, Friedrich Hayek, Joseph Schumpeter) — provided the theoretical foundations for market economics, subjective value theory, business cycle theory, and the critique of central planning that shaped 20th-century economic policy debates, particularly neoliberalism",
            "Sigmund Freud's development of psychoanalysis — created through his clinical practice and teaching at the University of Vienna — was one of the most consequential intellectual developments of the 20th century, transforming not only psychiatry but literature, art, cultural criticism, and popular psychology worldwide",
            "The expulsion of the Vienna Circle, Austrian School economists, and Jewish intellectuals by the Nazis (1938) — who dispersed to Oxford, Cambridge, Harvard, Chicago, and New York — transferred the concentrated intellectual traditions of Vienna to Anglo-American universities, making the Vienna intellectual legacy one of the primary foundations of post-WWII Anglo-American intellectual culture"
        ],
        "relationships": [
            {"entity": "Vienna Circle (logical positivism, 1920s–1930s — Schlick, Carnap, Neurath)", "relationship": "INTELLECTUAL_HOME_OF_THE", "note": "The Vienna Circle — dominant movement in 20th-century analytic philosophy — developed in University of Vienna seminars under Schlick, Carnap, and Neurath"},
            {"entity": "Austrian School of Economics (Menger, Mises, Hayek, Schumpeter)", "relationship": "INSTITUTIONAL_HOME_OF_THE", "note": "The Austrian School — subjective value theory, business cycle theory, critique of central planning — was founded at and developed through the University of Vienna"},
            {"entity": "Sigmund Freud (psychoanalysis, clinical practice and teaching at Vienna)", "relationship": "INSTITUTIONAL_CONTEXT_FOR_THE_DEVELOPMENT_OF_PSYCHOANALYSIS_BY", "note": "Freud's University of Vienna teaching and clinical practice provided the institutional context for psychoanalysis — one of the most consequential intellectual developments of the 20th century"},
            {"entity": "Rudolf IV, Duke of Austria (founder 1365)", "relationship": "FOUNDED_BY", "note": "Rudolf IV's 1365 founding — in Habsburg competition with Prague University (1348) — established the institutional foundation for Vienna's eventual intellectual dominance"},
            {"entity": "Nazi expulsions (1938) — dispersal of Vienna intellect to Anglo-American universities", "relationship": "INTELLECTUAL_LEGACY_DISPERSED_BY_THE", "note": "The 1938 Nazi expulsion of Vienna Circle and Austrian School intellectuals to Oxford, Harvard, and Chicago made the Vienna intellectual legacy a primary foundation of post-WWII Anglo-American intellectual culture"}
        ],
    }),

    ("duke-university", {
        "summary": (
            "Duke University (est. 1838, Durham, North Carolina — founded as Trinity College by Methodists, renamed Duke in 1924 after James Buchanan Duke's $40 million endowment) is one of the world's leading research universities — ranked among the top 10 in the United States and the top 25 globally, with particular strengths in medicine (Duke University Medical Center), law (Duke Law School), public policy (Sanford School of Public Policy), environmental science (Nicholas School), and the liberal arts. Duke's 15 Nobel laureates, $12 billion endowment, and its distinctive Gothic/Georgian campus architecture make it one of the most recognisable universities in the American South.\n\n"
            "Duke was named and funded by James Buchanan Duke, the tobacco and electricity magnate who transformed Trinity College into Duke University with his 1924 endowment — which established the Duke Endowment (a regional endowment benefiting hospitals, children's homes, and educational institutions in the Carolinas) alongside the university. Duke Medical Center — established in 1930 — became one of the world's leading medical research and treatment institutions, pioneering cardiac surgery (the first successful open-heart surgery using artificial heart-lung bypass, 1955) and cancer research.\n\n"
            "Duke's research profile is distinguished by its strength in biomedical sciences, environmental and energy policy, and global health — areas where its location in the Research Triangle Park (with UNC Chapel Hill and NC State) creates a uniquely concentrated research ecosystem. The Duke-Margolis Center for Health Policy and the Duke Nicholas Institute for Environmental Policy Solutions have been among the most influential think tanks in American health and environmental policy."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "One of world's leading research universities (est. 1838, Durham NC; renamed Duke 1924 after James Buchanan Duke's $40 million endowment); top 10 US, top 25 global; 15 Nobel laureates; $12 billion endowment; Duke Medical Center (1930, world leader); first open-heart surgery using artificial heart-lung bypass (1955); Duke Law School, Sanford School of Public Policy, Nicholas School; Research Triangle Park ecosystem (Duke, UNC Chapel Hill, NC State); Duke-Margolis Center for Health Policy; Gothic/Georgian campus.",
            "significanceCategory": "continental"
        },
        "causes": [
            "James Buchanan Duke's $40 million endowment (1924) — one of the largest philanthropic gifts in American history at the time — transformed Trinity College from a regional Methodist college into a nationally competitive research university, demonstrating the power of individual philanthropic investment to reshape institutional trajectories",
            "The Research Triangle's development (1950s–present) — with Duke, UNC Chapel Hill, NC State, and Research Triangle Park creating a concentrated technology, biomedical, and policy research ecosystem — provided the collaborative environment that amplified Duke's individual research strengths",
            "Duke Medical Center's location in a region underserved by major academic medical centres — and its commitment to providing tertiary medical care for the Carolinas — gave it both the patient volume and the healthcare infrastructure that medical research requires"
        ],
        "effects": [
            "Duke Medical Center's pioneering of open-heart surgery with artificial heart-lung bypass (1955, by Dr. Henry Bahnson) — the procedure that made complex cardiac surgery universally available — was one of the most consequential medical advances of the 20th century, enabling the routine treatment of heart disease that has saved hundreds of millions of lives",
            "Duke's contribution to the Research Triangle Park ecosystem — which has attracted $2+ billion in annual R&D investment and hosts 300+ companies including GlaxoSmithKline, IBM, Cisco, and hundreds of biotech startups — has been the primary driver of North Carolina's transformation from a tobacco-dependent economy to a technology and life science economy",
            "Duke's Sanford School of Public Policy — which trains a significant proportion of American foreign policy and development professionals — has been a primary institutional contributor to US public policy thinking, with alumni including James Baker III, Tony Blair's UK foreign policy advisors, and dozens of senior US government officials",
            "Duke's Gothic/Georgian campus architecture — designed by Horace Trumbauer and Julian Abele (one of the first African American architects to receive major institutional commissions) in the 1920s–1930s — is one of the most architecturally distinguished 20th-century American university campuses, and Julian Abele's commission is one of the most significant early examples of an African American architect receiving major institutional work"
        ],
        "relationships": [
            {"entity": "James Buchanan Duke (1924 endowment, $40 million)", "relationship": "TRANSFORMED_AND_RENAMED_BY_THE_PHILANTHROPY_OF", "note": "Duke's $40 million 1924 endowment — one of the largest in American history — transformed Trinity College into a nationally competitive research university"},
            {"entity": "Duke Medical Center (est. 1930, world-leading cardiac and cancer research)", "relationship": "OPERATES_THE", "note": "Duke Medical Center — pioneer of open-heart surgery with artificial heart-lung bypass (1955) — is one of the world's leading academic medical centres"},
            {"entity": "First open-heart surgery with artificial heart-lung bypass (1955, Dr. Bahnson)", "relationship": "SITE_OF_THE", "note": "Duke's 1955 open-heart surgery — making complex cardiac surgery universally available — was one of the most consequential medical advances of the 20th century"},
            {"entity": "Research Triangle Park (Duke, UNC Chapel Hill, NC State ecosystem)", "relationship": "PRIMARY_INSTITUTIONAL_ANCHOR_OF_THE", "note": "Duke's role in the Research Triangle Park ecosystem has driven North Carolina's transformation from tobacco-dependence to a technology and life science economy"},
            {"entity": "Julian Abele (African American architect, Duke campus design)", "relationship": "PRIMARY_CAMPUS_ARCHITECTURE_DESIGNED_BY", "note": "Julian Abele — one of the first African American architects to receive major institutional commissions — designed Duke's Gothic/Georgian campus, making it architecturally and historically distinctive"}
        ],
    }),

    ("university-of-melbourne", {
        "summary": (
            "The University of Melbourne (est. 1853, Melbourne, Victoria — Australia's second university and the University of Melbourne Act 1853) is Australia's most prestigious and globally ranked university — consistently ranked in the global top 30, with 7 Prime Ministers among its alumni, 10 Nobel laureates, and the primary producer of Australian professional and academic leadership in law, medicine, arts, science, and architecture. Melbourne's model of graduate professional education — the 'Melbourne Model' (introduced 2008), which requires an undergraduate degree before entry to professional programmes — has transformed Australian higher education.\n\n"
            "The University of Melbourne was established by an Act of Parliament in 1853 — just 18 years after the settlement of Melbourne — reflecting the extraordinary rapidity of the Victorian Gold Rush's transformation of Melbourne from a colonial settlement to a prosperous city capable of supporting a university. Melbourne's founding connection to the gold rush — and its position as the financial and cultural capital of colonial Victoria — gave it the resources and the civic ambition to build major academic and cultural institutions.\n\n"
            "Melbourne's specific contributions include the development of the Melbourne Model (2008 curriculum reform requiring undergraduate degree before professional entry, modelled on the American graduate school system), the discovery of Helicobacter pylori's role in peptic ulcers (Barry Marshall and Robin Warren, 1984, Nobel Prize 2005), and the Royal Melbourne Hospital's pioneering role in the development of COVID-19 and influenza vaccines. Melbourne is the primary institutional source of Australian cultural leadership: the Melbourne School of Design, the Melbourne Conservatorium of Music, and the Law Faculty have trained the cultural and professional elite."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Australia's most prestigious and globally ranked university (est. 1853, Melbourne); consistently global top 30; 7 Australian Prime Ministers, 10 Nobel laureates; Melbourne Model (2008, undergraduate prerequisite for professional entry, modelled on American graduate school system); Barry Marshall and Robin Warren — Helicobacter pylori discovery (1984, Nobel Prize 2005); Royal Melbourne Hospital COVID-19 and influenza vaccine development; primary institutional source of Australian professional and cultural leadership; established 18 years after Melbourne's settlement — gold rush foundation.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The Victorian Gold Rush (1851–1870) — which transformed Melbourne from a colonial settlement into one of the world's wealthiest cities within a decade — provided the financial resources and civic ambition that made founding a university possible within 18 years of Melbourne's establishment, creating one of the fastest university foundations relative to city age in history",
            "The Melbourne Act 1853 — which established the University of Melbourne as a non-denominational secular institution (unlike most contemporary universities in Britain, which had Anglican or Catholic foundations) — reflected the progressive values of Victoria's colonial society and created a university open to all students regardless of religious affiliation",
            "The Melbourne Model's introduction (2008) — requiring an undergraduate degree before entry to professional programmes (medicine, law, engineering) and modelled on the American graduate school system — was driven by the faculty's conviction that broad undergraduate education produced better professionals than early specialisation, and by the desire to create a research university with globally comparable graduate professional schools"
        ],
        "effects": [
            "The Melbourne Model (2008) — requiring undergraduate degrees before professional entry — has been partially adopted by other Australian universities and has influenced the national debate about the structure of Australian higher education, pushing the sector toward the American model of graduate professional education",
            "Barry Marshall and Robin Warren's discovery of Helicobacter pylori's role in peptic ulcers (Melbourne, 1984) — for which Marshall famously drank a culture of H. pylori to demonstrate its pathogenicity — overturned the medical consensus that ulcers were caused by stress and diet, winning the Nobel Prize (2005) and transforming the treatment of the most common gastrointestinal disease worldwide",
            "Melbourne's production of 7 Australian Prime Ministers — including Robert Menzies, Harold Holt, Malcolm Fraser, John Gorton, and others — reflects its position as the primary institutional source of Australian political leadership, with the Melbourne Law Faculty and the Faculty of Arts as the primary training grounds",
            "The Royal Melbourne Hospital's vaccine research programme — producing COVID-19 vaccines and annual influenza vaccines for the Australian and regional Pacific market — has made Melbourne a primary node in Australian and Pacific public health infrastructure, extending the university's medical research impact to regional health security"
        ],
        "relationships": [
            {"entity": "Victorian Gold Rush (1851–1870, founding resources and civic ambition)", "relationship": "FINANCIALLY_AND_CIVICALLY_ENABLED_BY_THE", "note": "The gold rush transformed Melbourne from a settlement to a wealthy city, providing the resources for a university just 18 years after Melbourne's founding — one of the fastest such foundations in history"},
            {"entity": "Melbourne Model (2008 curriculum reform, undergraduate prerequisite)", "relationship": "INTRODUCED_THE", "note": "The Melbourne Model — requiring undergraduate degrees before professional entry, modelled on the American graduate school system — has influenced the structure of Australian higher education"},
            {"entity": "Barry Marshall and Robin Warren (H. pylori, Melbourne 1984, Nobel 2005)", "relationship": "INSTITUTIONAL_HOME_OF_THE_DISCOVERY_OF_THE_ROLE_OF", "note": "Marshall and Warren's Melbourne discovery (1984) — that H. pylori causes peptic ulcers — overturned medical consensus and won the 2005 Nobel Prize, transforming the treatment of the most common gastrointestinal disease"},
            {"entity": "7 Australian Prime Ministers (Melbourne alumni)", "relationship": "PRIMARY_INSTITUTIONAL_SOURCE_OF_AUSTRALIAN_POLITICAL_LEADERSHIP_AS_ALMA_MATER_OF", "note": "Melbourne's 7 Prime Minister graduates make it the primary institutional source of Australian political leadership"},
            {"entity": "Melbourne Act 1853 (non-denominational secular institution)", "relationship": "ESTABLISHED_AS_NON-DENOMINATIONAL_BY_THE", "note": "The Melbourne Act's non-denominational foundation — unusual for 19th-century universities — reflected Victoria's progressive colonial society and created a university open to all regardless of religion"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 40 — {len(ENTITIES)} entities (Class 381: Major World Universities Part 2)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
