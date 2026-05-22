#!/usr/bin/env python3
"""
Batch 43 — 8 entities (Class 393): Intelligence & Security Agencies
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()
FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/393-Class-393"
FILE_PREFIX = "393"


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

    ("federal-bureau-of-investigation", {
        "summary": (
            "The Federal Bureau of Investigation (FBI, est. 1908 as the Bureau of Investigation, renamed 1935, Washington D.C. — the primary federal law enforcement and domestic intelligence agency of the United States) is the most powerful domestic intelligence and law enforcement agency in the Western world — combining criminal investigation, counterterrorism, counterintelligence, and cybercrime functions within a single organisation of 35,000+ employees. The FBI's history is inseparable from J. Edgar Hoover's 48-year directorship (1924–1972) — during which it became the most powerful law enforcement agency in American history, using surveillance, blackmail, and political manipulation to shape American politics for half a century.\n\n"
            "The FBI was founded in 1908 as a small investigative bureau within the Department of Justice, primarily for investigating land fraud and antitrust cases. Under J. Edgar Hoover — who became director in 1924 at age 29 — the Bureau of Investigation (renamed FBI in 1935) transformed from a minor federal agency into the pre-eminent law enforcement institution in the United States, with Hoover's combination of genuine investigative expertise and ruthless political manipulation making the FBI simultaneously the most effective and most politically dangerous agency in American government.\n\n"
            "Hoover's COINTELPRO programme (1956–1971) — which used illegal surveillance, infiltration, disinformation, and blackmail against civil rights leaders (MLK, Malcolm X), Black Power movements, the American Communist Party, and anti-Vietnam War groups — is the most documented case of a democratic government using its intelligence apparatus to undermine domestic political movements, and the primary reason why the FBI's history remains a contested terrain in American political culture."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Primary US federal law enforcement and domestic intelligence agency (est. 1908 Bureau of Investigation, renamed 1935 FBI); 35,000+ employees; J. Edgar Hoover directorship (1924–1972, 48 years) — most powerful law enforcement figure in American history; COINTELPRO (1956–1971) — illegal surveillance, blackmail against MLK, Black Power, American Communist Party, anti-Vietnam War groups; Watergate (1972); post-9/11 counterterrorism transformation; most documented case of democratic government using intelligence apparatus against domestic political movements.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Theodore Roosevelt's desire to create a permanent federal investigative capacity — responding to the growing sophistication of land fraud, antitrust violations, and interstate crime that crossed state boundaries and exceeded the capacity of local law enforcement — drove the founding of the Bureau of Investigation (1908) over Congressional opposition",
            "J. Edgar Hoover's appointment as director (1924) — and his rapid development of a centralised fingerprint database, professionalised investigative methodology, and political intelligence files on government officials — transformed the Bureau from a minor federal agency into an institution whose director had more durable political power than any president he served under",
            "The post-9/11 intelligence failures — including the CIA-FBI information sharing failures that contributed to the successful attacks — drove the FBI's transformation from primarily a law enforcement agency to primarily a counterterrorism and intelligence agency, with the largest restructuring in its history (2001–2004)"
        ],
        "effects": [
            "COINTELPRO's disruption of the civil rights and Black Power movements — including surveillance of Martin Luther King Jr., the FBI's letter urging him to commit suicide, the infiltration of the Black Panther Party, and the murder of Fred Hampton by Chicago police with FBI cooperation — was the most consequential use of state intelligence power against domestic political movements in American history, shaping the trajectory of the civil rights movement",
            "The FBI's investigation of Watergate (1972–1974) — and the leaking of information to Bob Woodward by FBI Associate Director Mark Felt (Deep Throat) — was the key factor in the exposure of the Nixon administration's crimes, demonstrating that the FBI's political independence (even imperfect) was essential to the constitutional order",
            "The FBI's post-9/11 transformation — from a criminal investigation agency to a counterterrorism and intelligence agency with 2,000+ intelligence analysts, bulk phone record collection, and FISA warrants targeting thousands of US persons — fundamentally changed the relationship between the federal government and the civil liberties of American citizens",
            "The FBI's role in the 2016 election — with Director Comey's public announcement of a reopened investigation into Hillary Clinton's emails 11 days before the election — demonstrated how a director's unilateral decisions could have direct, measurable effects on election outcomes, raising questions about the appropriate relationship between law enforcement and electoral politics"
        ],
        "relationships": [
            {"entity": "J. Edgar Hoover (director 1924–1972, 48 years, political surveillance and blackmail)", "relationship": "POLITICAL_POWER_DEFINED_FOR_48_YEARS_BY_THE_DIRECTORSHIP_OF", "note": "Hoover's 48-year directorship made the FBI the most powerful law enforcement agency in American history — combining genuine investigative excellence with ruthless political manipulation"},
            {"entity": "COINTELPRO (1956–1971, illegal surveillance of MLK, Black Power, civil rights)", "relationship": "CONDUCTED_THE_DOMESTIC_INTELLIGENCE_ABUSE_PROGRAMME", "note": "COINTELPRO — the most documented case of a democratic government using intelligence against domestic political movements — was the FBI's most consequential and most condemned programme"},
            {"entity": "Martin Luther King Jr. (FBI surveillance target, COINTELPRO)", "relationship": "MOST_PROMINENT_TARGET_OF_ILLEGAL_DOMESTIC_SURVEILLANCE_BY_THE", "note": "The FBI's surveillance, infiltration, and harassment of King — including the letter urging suicide — is the clearest example of COINTELPRO's political objectives"},
            {"entity": "Watergate / Deep Throat / Mark Felt (FBI Associate Director, Nixon investigation)", "relationship": "CENTRAL_INVESTIGATIVE_ROLE_IN_THE", "note": "The FBI's Watergate investigation — and Felt's Deep Throat leaks — were the key factor in exposing the Nixon administration's crimes"},
            {"entity": "9/11 attacks (2001, FBI counterterrorism transformation)", "relationship": "FUNDAMENTAL_INSTITUTIONAL_TRANSFORMATION_DRIVEN_BY_INTELLIGENCE_FAILURES_OF_THE", "note": "9/11 drove the FBI's largest restructuring — from criminal investigation to counterterrorism and intelligence focus — fundamentally changing its relationship with civil liberties"}
        ],
    }),

    ("mossad", {
        "summary": (
            "Mossad (HaMossad leModiʿin uleTafkidim Meyuḥadim — the Institute for Intelligence and Special Operations, est. 1949, Tel Aviv — the foreign intelligence service of the State of Israel) is widely regarded as one of the world's most effective intelligence agencies — responsible for the assassination of Palestinian Liberation Organization leaders, the capture of Adolf Eichmann (1960), the Operation Wrath of God targeted killings of the Black September operatives responsible for the 1972 Munich massacre, and the Stuxnet cyber-sabotage of Iran's nuclear programme (2010). Mossad's reputation for operational effectiveness — sustained over 75 years — is disproportionate to Israel's size.\n\n"
            "Mossad was founded in 1949 — just one year after Israeli independence — under Prime Minister David Ben-Gurion, who made intelligence a foundational component of Israeli national security doctrine from the state's first year. Mossad's early operations included the capture of Adolf Eichmann in Buenos Aires (1960) — brought to Israel for trial and execution — which was the most consequential intelligence operation in the history of the Nuremberg principles and the global effort to hold Holocaust perpetrators accountable.\n\n"
            "Mossad's operational culture — emphasising human intelligence (HUMINT), improvisation, small teams, and willingness to operate in denied environments — has made it the model for intelligence services that face asymmetric threats and resource constraints. Its failures — the 1973 Yom Kippur War intelligence failure (the worst intelligence failure in Israeli history), the botched Lillehammer affair (1973, killing a Moroccan waiter mistaken for a Black September operative), and the Hamas intelligence failures of October 7, 2023 — demonstrate the limits of even highly effective intelligence agencies."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Israel's foreign intelligence service (est. 1949, Tel Aviv, David Ben-Gurion); widely regarded as world's most effective intelligence agency; capture of Adolf Eichmann in Buenos Aires (1960) — trial and execution; Operation Wrath of God (targeted killings after 1972 Munich massacre); Stuxnet cyber-sabotage of Iran's nuclear programme (2010); HUMINT-focused operational culture — model for intelligence services facing asymmetric threats; failures: Yom Kippur War (1973), Lillehammer affair (1973), October 7 2023 Hamas attacks.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Israel's founding in 1948 — in a hostile regional environment, with existential security threats from all neighbouring states — made intelligence the most critical component of Israeli national security from the first year of statehood, driving the founding of Mossad (1949) as a permanent foreign intelligence service",
            "The Holocaust's demonstration that the Jewish people could not rely on any external power for protection — and that intelligence about hostile intentions was critical to survival — created the psychological and political foundation for Israel's intelligence culture, in which Mossad's motto 'By way of deception, thou shalt do war' reflects a profound distrust of any source of information other than one's own",
            "The 1972 Munich massacre — in which Black September murdered 11 Israeli Olympic athletes — created the political mandate for Operation Wrath of God, Mossad's targeted killing programme against the perpetrators, which established the doctrine of targeted assassination as a legitimate counterterrorism tool that was subsequently adopted by the United States after 9/11"
        ],
        "effects": [
            "The Eichmann capture (1960) and trial — bringing the primary administrator of the Holocaust's logistics to justice 15 years after the end of the war — was the most consequential assertion of the Nuremberg principles in the postwar era, demonstrating that war crimes perpetrators could be found and held accountable regardless of the passage of time or their relocation to sympathetic countries",
            "Operation Wrath of God (1972–1988) — Mossad's targeted killing of the Black September operatives responsible for the Munich massacre — established targeted assassination as a tool of counterterrorism, setting the precedent for the United States' post-9/11 drone assassination programme and the global normalisation of state-sponsored targeted killing",
            "The Stuxnet worm (2010) — developed by Israel and the United States to sabotage Iran's Natanz uranium enrichment centrifuges — was the first state-sponsored cyberweapon to cause physical destruction, destroying 1,000+ Iranian centrifuges and setting the precedent for cyber warfare as a complement to conventional and nuclear deterrence",
            "The Hamas attacks of October 7, 2023 — which killed 1,200 Israelis in the worst intelligence failure in Israeli history since the 1973 Yom Kippur War — demonstrated that even highly effective intelligence agencies can be blind-sided by an adversary who accepts operational security at the cost of tactical complexity, with consequences for Israeli security doctrine and the credibility of intelligence-driven defence"
        ],
        "relationships": [
            {"entity": "Capture of Adolf Eichmann (Buenos Aires 1960, Nuremberg principles)", "relationship": "CONDUCTED_THE_OPERATION_THAT_BROUGHT_TO_JUSTICE_THE_ADMINISTRATOR_OF_THE_HOLOCAUST", "note": "Mossad's 1960 capture of Eichmann — the primary logistics administrator of the Holocaust — was the most consequential assertion of the Nuremberg principles in the postwar era"},
            {"entity": "Operation Wrath of God (targeted killings, 1972 Munich massacre response)", "relationship": "EXECUTED_THE", "note": "Operation Wrath of God established targeted assassination as a counterterrorism tool — setting the precedent for the US post-9/11 drone assassination programme"},
            {"entity": "Stuxnet worm (2010, first state-sponsored cyberweapon causing physical destruction)", "relationship": "CO-DEVELOPER_OF_THE", "note": "Stuxnet — the first cyberweapon causing physical destruction — set the precedent for cyber warfare as a complement to conventional deterrence"},
            {"entity": "David Ben-Gurion (Israeli founder, Mossad founder 1949)", "relationship": "FOUNDED_BY_AND_INTELLIGENCE_DOCTRINE_SHAPED_BY", "note": "Ben-Gurion's founding of Mossad in Israel's first year reflected his conviction that intelligence was the most critical component of Israeli national security"},
            {"entity": "October 7 2023 Hamas attacks (worst Israeli intelligence failure since 1973)", "relationship": "WORST_INSTITUTIONAL_INTELLIGENCE_FAILURE_SINCE_1973_YOM_KIPPUR_WAR_AS_A_RESULT_OF_THE", "note": "October 7 demonstrated that even highly effective intelligence agencies can be blind-sided, with devastating consequences for Israeli security doctrine"}
        ],
    }),

    ("national-security-agency", {
        "summary": (
            "The National Security Agency (NSA, est. 1952, Fort Meade, Maryland — the signals intelligence and cryptanalysis agency of the United States Department of Defense) is the world's largest intelligence agency by budget and workforce — with approximately 40,000 employees, a classified budget estimated at $10+ billion annually, and the most powerful signals intelligence (SIGINT) collection and analysis infrastructure in the world. The NSA's existence was itself classified until 1975; it was known informally as 'No Such Agency' for its first two decades. The NSA's mass surveillance programmes — revealed by Edward Snowden in 2013 — are the most consequential intelligence disclosure in history.\n\n"
            "The NSA was founded in 1952 by President Truman to centralize signals intelligence — codebreaking, interception of communications, and electronic surveillance — which had been divided among the military services during World War II. The NSA's foundational mission was the SIGINT collection that supported Cold War nuclear deterrence — intercepting Soviet military communications, tracking Soviet missile tests, and providing strategic warning of Soviet intentions. The NSA's massive expansion after 9/11 — and particularly the creation of the PRISM, XKeyscore, and bulk phone record collection programmes — fundamentally changed its relationship with domestic and foreign civil liberties.\n\n"
            "Edward Snowden's disclosure of NSA programmes in 2013 — revealing that the NSA collected bulk telephone metadata on all Americans (under the PATRIOT Act Section 215 authority), monitored the internet communications of 250 million people annually (PRISM), and had placed surveillance 'backdoors' in commercial encryption products — was the most significant intelligence disclosure in history, triggering a global debate about surveillance, privacy, and the boundaries of intelligence collection that has not been resolved."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's largest intelligence agency (est. 1952, Fort Meade Maryland, President Truman); ~40,000 employees, $10+ billion classified budget; SIGINT collection and cryptanalysis; 'No Such Agency' — existence classified until 1975; Snowden disclosures (2013) — most consequential intelligence disclosure in history; PRISM (250M internet communications/year), XKeyscore, bulk phone record collection (all Americans); global surveillance debate; NSA's SIGINT supported Cold War nuclear deterrence; PATRIOT Act Section 215 authority.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "President Truman's 1952 founding directive — creating the NSA to centralise the SIGINT capabilities that had been divided among the Army Security Agency, Navy Security Group, and Air Force Security Service — reflected the lesson of Pearl Harbor (1941) that fragmented intelligence collection produced dangerous intelligence gaps",
            "The Cold War's creation of an existential SIGINT imperative — in which the accurate assessment of Soviet nuclear capabilities, intentions, and military movements was the foundation of the US deterrence posture — drove the NSA's expansion from a small codebreaking organisation to the world's largest intelligence agency in a single generation",
            "The 9/11 attacks and the PATRIOT Act (2001) — which dramatically expanded the legal authorities for domestic surveillance and created the Section 215 bulk phone record collection authority — drove the NSA's post-9/11 transformation from a foreign SIGINT agency to a domestic-foreign surveillance hybrid with access to the communications of millions of Americans"
        ],
        "effects": [
            "The Snowden disclosures (2013) — revealing the NSA's bulk collection of all American phone records, the PRISM programme monitoring 250 million internet communications annually, and the placement of backdoors in commercial encryption — triggered the most significant public debate about surveillance and privacy since Watergate, resulting in the USA FREEDOM Act (2015), the invalidation of the Safe Harbor data transfer agreement, and the European Court of Justice's Schrems decisions",
            "The NSA's SIGINT support for Cold War nuclear deterrence — providing strategic warning of Soviet military movements, tracking missile tests, and assessing Soviet nuclear capabilities — was the intelligence foundation of the US deterrence posture, contributing to the 40-year nuclear standoff that avoided direct US-Soviet military conflict",
            "The Dual_EC_DRBG vulnerability — which the NSA is alleged to have inserted into the NIST random number generation standard — if confirmed, represents the most consequential cybersecurity compromise in the history of encryption standards, potentially enabling the NSA to decrypt communications secured by NIST-approved cryptographic systems worldwide",
            "The global surveillance architecture revealed by Snowden — the Five Eyes alliance's (US-UK-Canada-Australia-New Zealand) integration of SIGINT collection, the NSA's access to the major internet companies' data under PRISM, and the global cable tapping infrastructure — has permanently changed governments', companies', and individuals' assumptions about the privacy of digital communications"
        ],
        "relationships": [
            {"entity": "Edward Snowden (2013 disclosures, most consequential intelligence leak in history)", "relationship": "PROGRAMMES_REVEALED_TO_THE_PUBLIC_BY", "note": "Snowden's 2013 disclosures — PRISM, bulk phone records, XKeyscore — triggered the most significant public debate about surveillance and privacy since Watergate"},
            {"entity": "PRISM programme (250M internet communications/year, post-9/11)", "relationship": "OPERATES_THE", "note": "PRISM's collection of 250 million internet communications annually — from Google, Facebook, Microsoft, Apple — was the most comprehensive surveillance system in history"},
            {"entity": "Five Eyes alliance (US-UK-Canada-Australia-New Zealand SIGINT sharing)", "relationship": "PRIMARY_SIGINT_CONTRIBUTOR_TO_THE", "note": "The NSA's centrality to the Five Eyes alliance — sharing SIGINT with the UK, Canada, Australia, and New Zealand — created the global surveillance architecture revealed by Snowden"},
            {"entity": "PATRIOT Act (2001) / Section 215 bulk phone record authority", "relationship": "POST-9/11_SURVEILLANCE_EXPANSION_ENABLED_BY_THE", "note": "The PATRIOT Act's Section 215 authority gave the NSA legal cover for bulk collection of all American phone records — one of the most sweeping domestic surveillance programmes in history"},
            {"entity": "President Truman (founding directive 1952, SIGINT centralisation)", "relationship": "FOUNDED_BY_THE_DIRECTIVE_OF", "note": "Truman's 1952 directive — centralising fragmented SIGINT capabilities — created the institutional foundation for the world's largest intelligence agency"}
        ],
    }),

    ("secret-intelligence-service", {
        "summary": (
            "The Secret Intelligence Service (SIS, commonly MI6 — Military Intelligence, Section 6, est. 1909, London — the foreign intelligence service of the United Kingdom) is one of the world's oldest and most historically influential intelligence agencies — the institutional source of the tradecraft, terminology, and cultural mythology of modern espionage, the agency that produced the 'Cambridge Five' (the most consequential Western intelligence penetration by Soviet intelligence), and the subject of Ian Fleming's James Bond novels, which transformed the public perception of intelligence globally. SIS has operated continuously for over 115 years across two world wars, the Cold War, and the War on Terror.\n\n"
            "SIS was founded in 1909 as the Foreign Section of the Secret Service Bureau — established by the Committee of Imperial Defence in response to growing concerns about German espionage in Britain — under the direction of Captain Mansfield Cumming, who signed his correspondence with the letter 'C' in green ink (a tradition maintained by all subsequent directors). The 'C' designation has entered the permanent vocabulary of British intelligence culture.\n\n"
            "The Cambridge Five (Kim Philby, Donald Maclean, Guy Burgess, Anthony Blunt, John Cairncross) — all recruited as Soviet agents at Cambridge University in the 1930s and subsequently placed in senior positions in SIS, the Foreign Office, and GCHQ — were the most successful penetration of a Western intelligence service in history, compromising British and American intelligence operations for decades and demonstrating the vulnerability of intelligence agencies to ideologically motivated insiders."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's oldest continuously operating foreign intelligence service (est. 1909 London, Foreign Section Secret Service Bureau); Captain Mansfield Cumming 'C' (green ink, tradition maintained by all directors); Cambridge Five (Philby, Maclean, Burgess, Blunt, Cairncross) — most successful penetration of Western intelligence by Soviet intelligence; Ian Fleming's James Bond novels — transformed global public perception of intelligence; WWI, WWII, Cold War, War on Terror; institutional source of espionage tradecraft and cultural mythology.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Committee of Imperial Defence's recognition (1909) that Germany's growing military and espionage capabilities required a permanent British secret service — rather than ad hoc intelligence collection — drove the founding of the Secret Service Bureau, with the Foreign Section (SIS) and Home Section (later MI5) as complementary domestic and foreign intelligence services",
            "The two World Wars' demonstration of intelligence's critical role in military operations — SIS's pre-WWI German penetration, the wartime code-breaking at Bletchley Park (formally separate but closely connected to SIS), and WWII special operations — established intelligence as a permanent component of British foreign policy, driving SIS's post-war institutionalisation and budget expansion",
            "The Cambridge Five's penetration — in which five Cambridge-educated British officials recruited as Soviet agents in the 1930s compromised British and American intelligence operations for decades — was the product of the specific social circumstances of Oxbridge recruitment, class loyalty, and ideological disillusionment that characterised the British upper class in the 1930s"
        ],
        "effects": [
            "The Cambridge Five's compromise of SIS — Kim Philby's position as Head of the SIS Soviet Section and SIS liaison to the CIA (1949–1951) gave the KGB advance warning of every British and American intelligence operation against the Soviet Union for a decade — was the most consequential intelligence penetration in the history of the Cold War, potentially costing hundreds of intelligence agents their lives",
            "Ian Fleming's James Bond novels (Casino Royale, 1953 — the first of 14 novels) — drawing on Fleming's wartime Naval Intelligence experience and his knowledge of SIS — created the cultural mythology of British espionage that has shaped the global public perception of intelligence for 70 years, making 'Bond, James Bond' the most recognised fictional character in intelligence culture",
            "SIS's Cold War HUMINT operations — including the recruitment of Oleg Gordievsky (KGB London station chief, recruited by SIS, providing critical intelligence from 1974 to 1985) — produced some of the most valuable intelligence in the Cold War, influencing British and American assessments of Soviet intentions at critical moments including the 1983 Able Archer nuclear war scare",
            "The Vauxhall Cross headquarters (1994, designed by Terry Farrell, the first purpose-built SIS headquarters) — which was blown up in a James Bond film (Skyfall, 2012) — is one of the most recognisable intelligence agency buildings in the world, demonstrating how the boundary between SIS's real institutional identity and its Bond-driven cultural mythology has effectively dissolved"
        ],
        "relationships": [
            {"entity": "Cambridge Five (Philby, Maclean, Burgess, Blunt, Cairncross — Soviet penetration)", "relationship": "MOST_CONSEQUENTIALLY_COMPROMISED_WESTERN_INTELLIGENCE_SERVICE_THROUGH_THE", "note": "Philby's position as Head of the Soviet Section — compromised by KGB since the 1930s — was the most consequential intelligence penetration of the Cold War"},
            {"entity": "Ian Fleming (James Bond novels, Casino Royale 1953 — Naval Intelligence background)", "relationship": "INSTITUTIONAL_INSPIRATION_FOR_THE_CULTURAL_MYTHOLOGY_CREATED_BY", "note": "Fleming's Bond novels — drawing on his SIS connections — created the cultural mythology of British espionage that has shaped global public perception for 70 years"},
            {"entity": "Oleg Gordievsky (KGB London station chief, SIS double agent 1974–1985)", "relationship": "RECRUITED_AND_HANDLED_THE_MOST_VALUABLE_COLD_WAR_INTELLIGENCE_SOURCE", "note": "Gordievsky's 11-year intelligence provision — warning of the Able Archer scare and Soviet intentions — was one of SIS's most consequential Cold War intelligence operations"},
            {"entity": "Captain Mansfield Cumming ('C', green ink tradition, first director)", "relationship": "INSTITUTIONAL_CULTURE_AND_'C' DESIGNATION_ESTABLISHED_BY_THE_FIRST_DIRECTOR", "note": "Cumming's 'C' designation — signed in green ink, continued by all subsequent directors — is the founding cultural convention of SIS"},
            {"entity": "Vauxhall Cross headquarters (1994, Terry Farrell, Bond film Skyfall)", "relationship": "HEADQUARTERS_LOCATED_AT", "note": "SIS's purpose-built Vauxhall Cross HQ — recognisable from Skyfall — demonstrates how SIS's real institutional identity and Bond mythology have dissolved into each other"}
        ],
    }),

    ("research-and-analysis-wing", {
        "summary": (
            "The Research and Analysis Wing (RAW, est. 1968, New Delhi — the foreign intelligence service of India, founded by Prime Minister Indira Gandhi and the first director R.N. Kao after the intelligence failures of the 1965 Indo-Pakistani War) is India's primary external intelligence agency — responsible for HUMINT collection, technical intelligence, counter-intelligence, and covert operations outside India's borders. RAW's most consequential operation was its critical role in the 1971 Bangladesh Liberation War — supporting the Mukti Bahini guerrillas, training and equipping 100,000+ Bengali fighters, and providing the intelligence that enabled India's decisive 13-day military victory that created Bangladesh.\n\n"
            "RAW was founded in 1968 after the Intelligence Bureau (established 1887, primarily domestic) proved inadequate for the foreign intelligence challenges India faced after independence — particularly the 1962 Sino-Indian War (a catastrophic intelligence failure) and the 1965 Indo-Pakistani War. Rameshwar Nath Kao — RAW's founding director (1968–1977) — built the agency from scratch, establishing close relationships with the KGB and Israeli intelligence (Mossad) for training and technical support.\n\n"
            "RAW's operational history includes the 1971 Bangladesh operation (the most successful intelligence-military coordination in Indian history), the 1974 and 1998 Indian nuclear tests (for which RAW provided the technical intelligence that enabled Pakistan's tests to be monitored), and covert operations in Sri Lanka (support for the Tamil Tigers, subsequently reversed), Nepal, and Afghanistan. RAW's close relationship with Mossad has been one of the most consequential intelligence partnerships in the Indo-Pacific."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "India's primary external intelligence agency (est. 1968, New Delhi, Indira Gandhi, R.N. Kao founding director); founded after 1962 Sino-Indian War intelligence failure and 1965 Indo-Pakistani War; 1971 Bangladesh Liberation War — most consequential intelligence-military coordination in Indian history; Mukti Bahini (100,000+ Bengali fighters trained/equipped); 13-day Indian military victory creating Bangladesh; KGB and Mossad training relationships; 1974 and 1998 nuclear tests intelligence; Sri Lanka/Tamil Tigers operations; RAW-Mossad partnership — most consequential Indo-Pacific intelligence alliance.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The catastrophic intelligence failure of the 1962 Sino-Indian War — in which India's political leadership had no accurate intelligence about Chinese military capabilities or intentions — and the inadequacy of the Intelligence Bureau's foreign intelligence collection drove the decision to create a separate foreign intelligence service",
            "Indira Gandhi's recognition that India needed a intelligence capability specifically tied to her political office — rather than the Intelligence Bureau's traditional reporting chain — drove the founding of RAW under R.N. Kao, a trusted Intelligence Bureau officer, with RAW reporting directly to the Prime Minister",
            "The 1971 Bangladesh crisis — in which the Pakistani army's brutal suppression of the Bengali independence movement created both a refugee crisis (10 million refugees into India) and a strategic opportunity to permanently weaken Pakistan — created the operational imperative for RAW's first major operation, which demonstrated the agency's value and established its institutional reputation"
        ],
        "effects": [
            "The 1971 Bangladesh operation — in which RAW trained, equipped, and coordinated the Mukti Bahini guerrilla force, provided intelligence for India's military operations, and helped precipitate the Pakistani military collapse — was the most successful intelligence-military coordination in Indian history, creating Bangladesh and fundamentally changing South Asian geopolitics",
            "RAW's role in the 1971 war established India's intelligence capability as a serious regional force, demonstrating that a developing country intelligence service — 3 years old and still building its capabilities — could successfully execute a complex covert operation that changed the political map of Asia",
            "The RAW-Mossad intelligence partnership — one of the most consequential intelligence relationships in the Indo-Pacific — has provided India with access to Israeli surveillance technology, cyber capabilities, and counterterrorism expertise, while giving Israel access to Indian regional intelligence on Pakistan, Iran, and the broader South Asian-Persian Gulf region",
            "RAW's involvement in Sri Lanka — initially supporting the Liberation Tigers of Tamil Eelam (Tamil Tigers) in the 1970s–1980s, then reversing course after the LTTE assassination of Rajiv Gandhi (1991) — is one of the most consequential intelligence policy reversals in Indian history, demonstrating the risks of supporting non-state armed groups as strategic proxies"
        ],
        "relationships": [
            {"entity": "1971 Bangladesh Liberation War (most consequential RAW operation)", "relationship": "DECISIVE_INTELLIGENCE-MILITARY_ROLE_IN_THE", "note": "RAW's 1971 Bangladesh operation — training Mukti Bahini, coordinating with Indian military — was the most successful intelligence-military coordination in Indian history, creating Bangladesh"},
            {"entity": "R.N. Kao (founding director 1968–1977, institutional builder)", "relationship": "INSTITUTIONAL_CHARACTER_ESTABLISHED_BY_THE_FOUNDING_DIRECTOR", "note": "Kao's 9-year founding directorship — building RAW's HUMINT networks, KGB relationships, and Mossad partnerships — established the agency's operational identity"},
            {"entity": "Indira Gandhi (Prime Minister, founder, RAW reporting directly to PM)", "relationship": "FOUNDED_BY_THE_POLITICAL_DIRECTION_OF", "note": "Gandhi's decision to found RAW with direct PM reporting chain — rather than through the Intelligence Bureau's existing hierarchy — reflected her desire for a personal intelligence capability"},
            {"entity": "Mossad (RAW-Mossad intelligence partnership, Indo-Pacific)", "relationship": "MOST_CONSEQUENTIAL_INTELLIGENCE_PARTNERSHIP_WITH_THE", "note": "The RAW-Mossad partnership provides India with Israeli surveillance and cyber capabilities while giving Israel access to South Asian-Persian Gulf regional intelligence"},
            {"entity": "Mukti Bahini (Bengali guerrillas trained by RAW, 100,000+ fighters)", "relationship": "TRAINED, EQUIPPED, AND COORDINATED_THE", "note": "RAW's training of 100,000+ Mukti Bahini fighters was the operational core of the 1971 Bangladesh operation that changed the political map of South Asia"}
        ],
    }),

    ("ministerium-f\u00fcr-staatssicherheit", {
        "summary": (
            "The Ministry for State Security (Ministerium für Staatssicherheit, Stasi, est. 1950, East Berlin — the secret police and intelligence service of the German Democratic Republic, established under Soviet guidance) was the most totalitarian domestic surveillance apparatus ever built — with 91,000 full-time employees and 189,000 unofficial informants in a population of 17 million, giving the GDR the highest ratio of surveillance to population in history. The Stasi's methods — systematic psychological manipulation ('Zersetzung'), file-keeping on 6 million of East Germany's 17 million citizens, and the cultivation of informants within families, churches, and workplaces — represent the model totalitarian surveillance state.\n\n"
            "The Stasi was founded in 1950, one year after the GDR's founding, under the direct supervision of Soviet KGB advisors — many of the Stasi's founding officers had trained with the KGB, and the Stasi's organisational structure, interrogation methods, and surveillance philosophy were directly derived from Soviet security practices. Under Erich Mielke's leadership (1957–1989, 32 years), the Stasi expanded from a small security service into the comprehensive surveillance apparatus that monitored virtually every aspect of East German life.\n\n"
            "The Stasi's Zersetzung ('corrosion') tactics — which aimed to psychologically destroy dissidents without arrest, through anonymous threats, relationship sabotage, career destruction, and systematic gaslighting — were among the most psychologically sophisticated methods of political control ever developed, producing lasting trauma in survivors that has been the subject of significant psychiatric research."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Most totalitarian domestic surveillance apparatus ever built (est. 1950, East Berlin GDR); 91,000 full-time employees, 189,000 unofficial informants, 17 million population — highest surveillance-to-population ratio in history; files on 6 million citizens; Erich Mielke directorship (1957–1989, 32 years); Zersetzung ('corrosion') psychological destruction tactics — anonymous threats, relationship sabotage, gaslighting; Soviet KGB model; 1989 collapse and file opening — lasting trauma, transitional justice, privacy law reform; model totalitarian surveillance state.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Soviet occupation zone's need for a domestic security apparatus modelled on the KGB — to prevent the reassertion of bourgeois politics, monitor potential Western intelligence penetration, and control the population of a state whose legitimacy was contested — drove the founding of the Stasi in 1950 under direct Soviet supervision",
            "Erich Mielke's appointment as director (1957) — and his systematic expansion of the informal informant network (Inoffizielle Mitarbeiter, IM) to 189,000 by 1989 — reflected his conviction that the only way to prevent East German society from being subverted by Western influence was to monitor it comprehensively, creating the highest surveillance ratio in history",
            "The Berlin Wall's construction (1961) — which ended the mass emigration that had been depleting the GDR of its educated professional class — created the conditions for the Stasi's expansion, as the Wall removed the emigration safety valve and forced the Stasi to control an unwilling population that could no longer leave"
        ],
        "effects": [
            "The Stasi's Zersetzung tactics — systematic psychological destruction of dissidents through anonymous threats, relationship sabotage, career interference, and gaslighting — produced lasting psychiatric damage in survivors, and the subsequent documentation of these methods has been the primary evidence for the psychological harm that state surveillance can cause, influencing psychiatric research on institutional trauma",
            "The Stasi files' opening after German reunification (1990) — the most comprehensive release of state security service records in history — enabled millions of East Germans to discover that their colleagues, friends, and family members had been Stasi informants, creating a massive social trauma that shaped the post-reunification social psychology of eastern Germany for decades",
            "The Stasi's comprehensive documentation of its own operations — keeping meticulous records of its surveillance activities, informant networks, and psychological operations — paradoxically became the primary evidence for the accountability and prosecution of Stasi officers after reunification, and the primary historical record of life under a totalitarian surveillance state",
            "The Stasi as a model for subsequent surveillance states — NSA bulk collection programmes, China's Social Credit System, and authoritarian domestic surveillance systems worldwide have been compared to the Stasi's methods, making it the reference point in all debates about state surveillance, privacy, and the boundaries of acceptable intelligence collection"
        ],
        "relationships": [
            {"entity": "Erich Mielke (director 1957–1989, 32 years, IM expansion)", "relationship": "SYSTEMATIC_EXPANSION_INTO_MOST_TOTALITARIAN_SURVEILLANCE_APPARATUS_UNDER_THE_DIRECTORSHIP_OF", "note": "Mielke's 32-year expansion of the Stasi — particularly the 189,000-strong informal informant network — created history's highest surveillance-to-population ratio"},
            {"entity": "Zersetzung tactics (psychological destruction, gaslighting, relationship sabotage)", "relationship": "DEVELOPER_OF_THE_MOST_PSYCHOLOGICALLY_SOPHISTICATED_POLITICAL_CONTROL_METHOD_IN_HISTORY", "note": "Zersetzung — aimed at psychologically destroying dissidents without arrest — produced lasting trauma and has become the reference point for research on state psychological violence"},
            {"entity": "Stasi files opening (1990, German reunification, social trauma)", "relationship": "COMPREHENSIVE_RECORDS_OPENED_AFTER_THE_COLLAPSE_OF_THE_GDR_TO_REVEAL_THE", "note": "The files' opening — enabling millions to discover family informants — created massive social trauma and is the primary historical record of life under totalitarian surveillance"},
            {"entity": "Soviet KGB (model and training source, founding officers)", "relationship": "ORGANISATIONAL_MODEL, TRAINING, AND_FOUNDING_SUPERVISION_PROVIDED_BY_THE", "note": "The KGB provided the Stasi's founding organisational model, trained its founding officers, and supervised its early operations — making the Stasi a direct institutional descendant of Soviet security practice"},
            {"entity": "East Germany / GDR (17 million population, state the Stasi served)", "relationship": "DOMESTIC_SURVEILLANCE_APPARATUS_OF_THE", "note": "The Stasi's monitoring of 6 million of the GDR's 17 million citizens — the highest surveillance ratio in history — defined East German social life for 40 years"}
        ],
    }),

    ("government-communications-headquarters", {
        "summary": (
            "Government Communications Headquarters (GCHQ, est. 1919 as the Government Code and Cypher School — GC&CS, renamed GCHQ in 1946, Cheltenham/London — the signals intelligence and cybersecurity agency of the United Kingdom) is the UK's primary signals intelligence collection agency and the institutional successor to the most consequential code-breaking achievement in history: the breaking of the Nazi Enigma cipher at Bletchley Park during World War II. GCHQ's wartime contribution — cracking Enigma and providing Ultra intelligence to Allied commanders — is credited by historians with shortening World War II by 2–4 years.\n\n"
            "GCHQ traces its institutional ancestry to Room 40 (the Admiralty's WWI codebreaking unit) and the Government Code and Cypher School (founded 1919, initially at Admiralty Arch, later moved to Bletchley Park). During WWII, Bletchley Park's codebreakers — including Alan Turing, Gordon Welchman, Hugh Alexander, and Dilly Knox — broke the German Enigma cipher and the Lorenz cipher (used for Hitler's strategic communications), providing intelligence (Ultra) that Churchill called 'the golden eggs' and the goose that never cackled.\n\n"
            "GCHQ's modern identity — as the UK's primary cyber intelligence and cybersecurity agency — was revealed by the Snowden disclosures (2013), which showed that GCHQ's TEMPORA programme had tapped the transatlantic fibre-optic cables to collect bulk internet data, GCHQ had collaborated with the NSA on the PRISM programme, and GCHQ's offensive cyber capabilities included the JTRIG unit's social media manipulation operations."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "UK's primary SIGINT and cybersecurity agency (est. 1919 as Government Code and Cypher School; renamed GCHQ 1946, Cheltenham); institutional successor to Bletchley Park (Enigma/Ultra WWII codebreaking); Alan Turing, Gordon Welchman, Hugh Alexander, Dilly Knox — Enigma breaking credited with shortening WWII by 2–4 years; Churchill called Ultra 'the golden eggs'; TEMPORA programme (transatlantic cable tapping); Snowden disclosures (2013) — NSA-GCHQ PRISM collaboration; JTRIG social media manipulation; Five Eyes SIGINT alliance.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Room 40's WWI codebreaking success — particularly the decryption of the Zimmermann Telegram (1917), which revealed Germany's offer to Mexico of US territory in exchange for entering the war against the United States — demonstrated the strategic value of signals intelligence and drove the founding of a permanent peacetime codebreaking institution (GC&CS, 1919)",
            "The Nazi adoption of the Enigma cipher machine — which German military planners believed was unbreakable — created both the intelligence challenge and the opportunity that drove the Bletchley Park codebreaking effort, with Alan Turing's bombe machine providing the automated cryptanalytic tool that made Enigma's daily key changes manageable",
            "The Snowden disclosures' revelation of GCHQ's capabilities — and the absence of any effective UK legislative oversight of GCHQ's bulk collection programmes — drove the Investigatory Powers Act 2016 ('the Snoopers' Charter'), which provided retrospective legal authorisation for GCHQ's existing collection activities while establishing a new judicial oversight framework"
        ],
        "effects": [
            "The Bletchley Park Enigma decryption (1941–1945) — providing Ultra intelligence that guided Allied strategy in the Atlantic U-boat war, the North African campaign, and the D-Day deception operations — is credited by most historians with shortening WWII by 2–4 years, potentially saving 14–21 million additional lives and vindicating the strategic value of signals intelligence",
            "Alan Turing's bombe machine (1940) — the electro-mechanical device that automated the search for Enigma daily key settings — was the conceptual precursor to modern computing, establishing the principle that complex pattern recognition problems could be solved by programmable machines, making Bletchley Park the institutional origin of the digital computer",
            "The Snowden disclosures' revelation of GCHQ's TEMPORA programme — tapping the transatlantic fibre-optic cables to collect bulk internet data on hundreds of millions of people globally — was the most significant disclosure of UK intelligence capabilities since WWII, fundamentally changing the UK's legal framework for intelligence collection and creating a new public debate about GCHQ's domestic accountability",
            "GCHQ's National Cyber Security Centre (NCSC, est. 2016) — the UK's primary cybersecurity defence organisation — has become the model for government cybersecurity agencies worldwide, demonstrating how SIGINT capabilities developed for offensive intelligence collection can be repurposed for defensive cybersecurity at national scale"
        ],
        "relationships": [
            {"entity": "Bletchley Park / Enigma / Ultra (WWII codebreaking, shortened war by 2–4 years)", "relationship": "INSTITUTIONAL_SUCCESSOR_TO_THE_WWII_CODEBREAKING_OPERATION_AT", "note": "Bletchley Park's Enigma decryption — GCHQ's institutional ancestor — is credited with shortening WWII by 2–4 years, the most consequential intelligence achievement in history"},
            {"entity": "Alan Turing (bombe machine, Enigma decryption, computing precursor)", "relationship": "INSTITUTIONAL_HOME_OF_THE_WARTIME_WORK_OF", "note": "Turing's bombe machine — the conceptual precursor to modern computing — was developed at Bletchley Park, making GCHQ's wartime precursor the institutional origin of the digital computer"},
            {"entity": "Zimmermann Telegram (1917, Room 40 decryption, US entry WWI)", "relationship": "INSTITUTIONAL_ANCESTOR'S_MOST_CONSEQUENTIAL_WWII_PRECURSOR_OPERATION_WAS_THE_DECRYPTION_OF_THE", "note": "Room 40's decryption of the Zimmermann Telegram — revealing Germany's offer to Mexico — drove US entry into WWI and demonstrated the strategic value that led to GCHQ's founding"},
            {"entity": "TEMPORA programme (transatlantic cable tapping, Snowden 2013)", "relationship": "OPERATES_THE", "note": "TEMPORA's bulk internet data collection — revealed by Snowden in 2013 — was the most significant disclosure of UK intelligence capabilities since WWII"},
            {"entity": "National Cyber Security Centre (NCSC, est. 2016, cybersecurity defence)", "relationship": "PARENT_ORGANISATION_OF_THE", "note": "The NCSC — GCHQ's defensive cybersecurity arm — has become the model for government cybersecurity agencies worldwide, demonstrating the repurposing of SIGINT for national defence"}
        ],
    }),

    ("canadian-security-intelligence-service", {
        "summary": (
            "The Canadian Security Intelligence Service (CSIS, est. 1984, Ottawa — created by the CSIS Act 1984 to replace the Royal Canadian Mounted Police Security Service, which had been discredited by a series of illegal operations against Quebec separatists and left-wing organisations) is Canada's primary domestic intelligence service — responsible for investigating threats to national security, including espionage, terrorism, and foreign interference. CSIS's creation — separating intelligence collection from law enforcement — was one of the most significant intelligence reform programmes in Western democratic history.\n\n"
            "CSIS was created in 1984 after the McDonald Commission (1977–1981) — established after revelations that the RCMP Security Service had conducted over 400 illegal operations, including burning a barn to prevent a Quebec separatist meeting, forging documents, opening mail, and breaking into the Parti Québécois headquarters — recommended separating intelligence collection from law enforcement. The McDonald Commission's report was the most comprehensive public examination of intelligence service misconduct in any Western democracy.\n\n"
            "CSIS's modern challenges include Chinese intelligence operations in Canada (which CSIS's leaked intelligence assessments described as the most comprehensive foreign interference campaign in Canadian history), the 2020 disclosure that China had targeted Canadian politicians with election interference operations, and the post-2001 counterterrorism expansion that raised civil liberties concerns about CSIS's surveillance powers under the Anti-terrorism Act."
        ),
        "importanceScore": 7,
        "historicalSignificance": {
            "significanceScore": 7,
            "significanceNarrative": "Canada's primary domestic intelligence service (est. 1984, Ottawa, CSIS Act); created after RCMP Security Service illegal operations (McDonald Commission 1977–1981 — 400+ illegal operations including barn burning, mail opening, PQ break-ins); McDonald Commission — most comprehensive public examination of intelligence misconduct in any Western democracy; separation of intelligence from law enforcement — most significant Western intelligence reform; Chinese foreign interference (2020–present); Anti-terrorism Act surveillance powers; Five Eyes member.",
            "significanceCategory": "regional"
        },
        "causes": [
            "The RCMP Security Service's 400+ illegal operations — including burning a barn to prevent a Quebec separatist meeting, forging documents, opening mail, and breaking into the Parti Québécois headquarters — were the proximate cause of the McDonald Commission (1977) and subsequently CSIS's founding as a separate civilian intelligence service",
            "The McDonald Commission's foundational recommendation that intelligence collection and law enforcement should be separated into distinct organisations — reflecting the concern that combining the two functions created institutional pressure to use intelligence methods for law enforcement purposes without judicial oversight — drove the CSIS Act's creation of a civilian intelligence service distinct from the RCMP",
            "Canada's position as a Five Eyes member — sharing intelligence with the US, UK, Australia, and New Zealand — created both the expectation that Canada would have a sophisticated domestic intelligence capability and the resource pressure to develop CSIS to the standard of its partners"
        ],
        "effects": [
            "CSIS's creation as a civilian intelligence service — with parliamentary oversight through the Security Intelligence Review Committee (SIRC) — became the model for intelligence service reform in other Western democracies that had experienced comparable scandals, demonstrating how public inquiries and democratic accountability mechanisms can reshape intelligence institutions",
            "The McDonald Commission's public examination of RCMP illegal operations — the most comprehensive public account of intelligence service misconduct in any Western democracy at the time — established the standard for intelligence oversight that influenced subsequent reform in the UK (the Intelligence Services Act 1994), Australia, and New Zealand",
            "CSIS's Chinese foreign interference disclosures (2020–2023) — leaked to Canadian media, revealing China's targeting of Canadian politicians and elections — triggered the Hogue Commission (2023–2024), Canada's first public inquiry into foreign electoral interference, demonstrating how intelligence service warnings about foreign interference can shape domestic politics when they become public",
            "CSIS's post-9/11 expansion — under the Anti-terrorism Act (2001), which gave CSIS new powers to investigate and disrupt terrorism — raised civil liberties concerns from the Muslim-Canadian community and civil liberties organisations, creating an ongoing tension between CSIS's counterterrorism mandate and Charter rights"
        ],
        "relationships": [
            {"entity": "McDonald Commission (1977–1981, RCMP illegal operations, intelligence reform)", "relationship": "CREATED_AS_A_DIRECT_RESULT_OF_THE_RECOMMENDATIONS_OF_THE", "note": "The McDonald Commission's finding of 400+ RCMP illegal operations directly drove CSIS's creation — one of the most significant intelligence reforms in Western democratic history"},
            {"entity": "RCMP Security Service (predecessor, barn burning, Quebec separatist surveillance)", "relationship": "REPLACED_THE_DISCREDITED", "note": "CSIS replaced the RCMP Security Service — whose illegal operations against Quebec separatists triggered the McDonald Commission — separating intelligence from law enforcement"},
            {"entity": "Chinese foreign interference (2020–present, Hogue Commission 2023)", "relationship": "PRIMARY_DOMESTIC_INTELLIGENCE_SERVICE_INVESTIGATING_AND_WARNING_ABOUT_THE", "note": "CSIS's leaked Chinese interference assessments triggered Canada's first public inquiry into foreign electoral interference"},
            {"entity": "Five Eyes alliance (Canada's SIGINT and intelligence sharing)", "relationship": "CANADA'S_PRIMARY_DOMESTIC_INTELLIGENCE_CONTRIBUTOR_TO_THE", "note": "CSIS's membership in the Five Eyes — sharing intelligence with US, UK, Australia, New Zealand — created expectations for Canadian intelligence capability that drove CSIS's institutional development"},
            {"entity": "Anti-terrorism Act 2001 (CSIS powers expansion, civil liberties tensions)", "relationship": "EXPANDED_MANDATE_AND_POWERS_UNDER_THE", "note": "The Anti-terrorism Act's post-9/11 CSIS expansion raised ongoing civil liberties concerns, creating tension between counterterrorism mandate and Charter rights"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 43 — {len(ENTITIES)} entities (Class 393: Intelligence & Security Agencies)")
    for slug, data in ENTITIES:
        print(f"\n\u2192 {slug}")
        enrich_entity(slug, data)
    print("\n\u2713 Done")
