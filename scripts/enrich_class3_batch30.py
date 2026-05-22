#!/usr/bin/env python3
"""
Batch 30 — 8 entities (Class 333): Diverse Institutions — Theatre, Film, Economic Bodies, Universities
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()
FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/333-Class-333"
FILE_PREFIX = "333"


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

    ("bolshoi-theatre", {
        "summary": (
            "The Bolshoi Theatre (est. 1776, Moscow — current building opened 1825; last major renovation 2011) is the most prestigious opera and ballet institution in Russia and one of the supreme cultural institutions of the world — home to the Bolshoi Ballet and Bolshoi Opera companies, the preeminent practitioners of the Russian classical ballet tradition and the Russian operatic repertoire. The Bolshoi's neoclassical building — with its iconic Apollo quadriga above the columned portico — is the defining image of Russian cultural grandeur.\n\n"
            "The Bolshoi was founded under Empress Catherine the Great as the Imperial Moscow Theatre — the counterpart to the Mariinsky Theatre (Imperial Ballet) in Saint Petersburg. The current Bolshoi building (1825) — designed by Osip Bove and Andrei Mikhailov — was the largest theatre in Russia and one of the largest in the world at its opening. The theatre's history is intertwined with Russian cultural nationalism: the premieres of Tchaikovsky's Swan Lake (1877), Glinka's A Life for the Tsar (Russian opera's founding work), and dozens of canonical Russian ballets and operas have all occurred on its stage.\n\n"
            "The Bolshoi Ballet is the most technically demanding and stylistically influential ballet company in the world, defining the 'Bolshoi style' — characterised by bold athleticism, dramatic intensity, and spectacular theatrical scale — that has shaped global ballet training and performance for over a century."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Russia's premier opera and ballet institution (est. 1776); current building 1825 (Bove/Mikhailov design); premiered Swan Lake (Tchaikovsky, 1877), Glinka's A Life for the Tsar; Bolshoi Ballet — most technically demanding and stylistically influential ballet company in world; 'Bolshoi style' (bold athleticism, dramatic intensity) shaped global ballet; iconic Apollo quadriga; last major renovation 2011.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "Catherine the Great's cultural programme — establishing imperial theatre companies in Moscow and St. Petersburg to demonstrate Russia's claim to European cultural parity — drove the founding of the Imperial Moscow Theatre (1776) that became the Bolshoi",
            "Moscow's role as Russia's cultural and commercial capital — providing the audiences, patronage, and nationalist sentiment for Russian opera and ballet — created the institutional foundation for the Bolshoi's growth into the preeminent Russian performing arts institution",
            "The 19th-century Russian nationalist cultural movement — which sought to create distinctively Russian artistic forms as alternatives to Italian and French models — drove the Bolshoi's development of the Russian ballet and operatic repertoire that became its defining identity"
        ],
        "effects": [
            "The Bolshoi's premiere of Swan Lake (1877) — Tchaikovsky's first ballet, initially a failure that was rehabilitated after his death — established the canonical Russian ballet repertoire (Swan Lake, Sleeping Beauty, The Nutcracker) that has become the foundation of global classical ballet",
            "The Bolshoi Ballet's international tours during the Soviet era (from 1956) — bringing Galina Ulanova, Maya Plisetskaya, Rudolf Nureyev, and Mikhail Baryshnikov to Western stages — had enormous cultural and soft power significance during the Cold War, demonstrating Soviet artistic achievement to Western audiences",
            "The 'Bolshoi style' of ballet — characterised by bold athleticism, dramatic intensity, and spectacular theatrical scale — became the dominant global influence on ballet training and performance, shaping ballet companies from the Paris Opera to the American Ballet Theatre",
            "The Bolshoi's defectors — Rudolf Nureyev (1961), Natalia Makarova (1970), Mikhail Baryshnikov (1974) — were among the most significant cultural defections of the Cold War, each transforming Western ballet while becoming symbols of Soviet artistic repression"
        ],
        "relationships": [
            {"entity": "Bolshoi Ballet (company)", "relationship": "HOME_INSTITUTION_OF_THE", "note": "The Bolshoi Theatre is the home of the Bolshoi Ballet — the world's most technically demanding and stylistically influential ballet company"},
            {"entity": "Tchaikovsky (Swan Lake premiere, 1877)", "relationship": "SITE_OF_THE_PREMIERE_OF_SWAN_LAKE_BY", "note": "The Bolshoi Theatre premiered Tchaikovsky's Swan Lake (1877) — establishing the canonical Russian ballet repertoire"},
            {"entity": "Catherine the Great (Imperial Moscow Theatre founding)", "relationship": "FOUNDED_AS_IMPERIAL_THEATRE_BY", "note": "Catherine the Great's cultural programme founded the Imperial Moscow Theatre (1776) that became the Bolshoi"},
            {"entity": "Soviet cultural diplomacy (Cold War)", "relationship": "INSTRUMENT_OF_CULTURAL_SOFT_POWER_DURING", "note": "Bolshoi tours from 1956 demonstrated Soviet artistic achievement during the Cold War — and defections (Nureyev, Baryshnikov) became symbols of Soviet artistic repression"},
            {"entity": "Russian nationalist cultural movement (19th century)", "relationship": "INSTITUTIONAL_HEART_OF_THE", "note": "The Bolshoi developed the distinctively Russian ballet and operatic repertoire that expressed Russian nationalist cultural identity"}
        ],
    }),

    ("cannes-film-festival", {
        "summary": (
            "The Cannes Film Festival (Festival de Cannes, est. 1946 — held annually in May, Palais des Festivals, Cannes, France) is the world's most prestigious and influential film festival — the primary market and artistic showcase for international cinema, where the Palme d'Or (awarded by an international jury) is the most coveted prize in world cinema. Cannes defines global art cinema: a Palme d'Or transforms a director's career, and the festival's selection effectively defines the canon of 'serious cinema' for any given year.\n\n"
            "Cannes was conceived in 1939 — as an explicitly democratic alternative to the Venice Film Festival, which had been captured by Mussolini and Hitler's propaganda — but the first festival was cancelled at the outbreak of World War II. The first full festival (1946) established Cannes as the primary venue where Hollywood and European art cinema intersected. The festival's prestige was built by the French New Wave filmmakers (Godard, Truffaut, Resnais) who used Cannes to launch careers, and by the festival's willingness to award the Palme d'Or to politically controversial films.\n\n"
            "Cannes is not only an artistic festival but the world's largest film market (Marché du Film) — where approximately 4,000 films are bought and sold annually, $1 billion in distribution deals are made, and the global film industry transacts its commercial business. The combination of artistic prestige and commercial significance makes Cannes the single most important event in the global film industry calendar."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "World's most prestigious film festival (est. 1946); Palme d'Or — most coveted prize in world cinema; conceived 1939 as democratic alternative to Mussolini/Hitler-captured Venice festival; French New Wave filmmakers (Godard, Truffaut) launched careers at Cannes; largest film market (Marché du Film, ~4,000 films sold, $1 billion deals annually); defines global art cinema canon; intersection of Hollywood and European art cinema.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The capture of the Venice Film Festival by Italian and German fascist propaganda (1938) — when Mussolini's government used the festival to promote fascist cinema and the Nazi film Olympia won a prize — drove the French government and Jean Zay (Culture Minister) to create an independent international film festival at Cannes",
            "France's claim to leadership in world cinema — rooted in the Lumière brothers' invention of cinema (1895) and the tradition of French film artistry — created the national will to host the world's premier film festival as a French cultural institution",
            "The post-World War II expansion of global cinema audiences — and the growth of art cinema as a culturally prestigious alternative to Hollywood genre filmmaking — created the market for a festival that could identify and champion non-Hollywood cinema"
        ],
        "effects": [
            "The French New Wave's Cannes premieres (The 400 Blows, Hiroshima Mon Amour, 1959) — and the festival's subsequent championing of directors from around the world — established Cannes as the definitive launchpad for international art cinema directors, transforming it from a national cultural event into a global cinema institution",
            "The Palme d'Or's cultural authority — transforming the careers of Fellini, Bergman, Kurosawa, Coppola, Tarantino, and Haneke (all Palme d'Or winners or major Cannes presences) — makes Cannes the primary arbiter of cinematic prestige worldwide, directly influencing critical reception, awards season positioning, and box office",
            "The Marché du Film — held simultaneously with the festival — has become the world's largest film market, where the global film industry's commercial transactions are concentrated in a single week, making Cannes both the artistic and commercial capital of world cinema",
            "Cannes' 1968 revolt — when Godard, Truffaut, and other filmmakers shut down the festival in solidarity with the May 68 student uprising — established the festival as a site of political expression and artistic resistance, linking cinema to broader social movements"
        ],
        "relationships": [
            {"entity": "Palme d'Or (most coveted prize in world cinema)", "relationship": "AWARDS_THE_ANNUAL", "note": "The Palme d'Or — awarded by an international jury — is the most prestigious prize in world cinema, transforming directors' careers and defining the art cinema canon"},
            {"entity": "Venice Film Festival (1938 fascist capture)", "relationship": "CREATED_AS_DEMOCRATIC_ALTERNATIVE_TO_THE", "note": "Cannes was conceived (1939) explicitly as an alternative to the Venice Film Festival after Mussolini's government used it for fascist propaganda"},
            {"entity": "French New Wave (Godard, Truffaut, Resnais)", "relationship": "LAUNCHED_THE_CAREERS_OF_THE", "note": "The French New Wave filmmakers used Cannes (especially 1959) as the primary launch platform for their revolutionary cinema"},
            {"entity": "Marché du Film (film market)", "relationship": "HOSTS_THE_WORLDS_LARGEST_FILM_MARKET", "note": "The Marché du Film — held simultaneously with the festival — transacts approximately $1 billion in distribution deals annually, making Cannes the commercial capital of world cinema"},
            {"entity": "May 1968 (Cannes revolt)", "relationship": "SITE_OF_THE_FAMOUS_FESTIVAL_SHUTDOWN_DURING", "note": "Godard and Truffaut shut down Cannes in 1968 in solidarity with the May 68 uprising — establishing the festival as a site of political expression"}
        ],
    }),

    ("european-economic-community", {
        "summary": (
            "The European Economic Community (EEC, est. 1957 — Treaty of Rome, signed 25 March 1957; operational 1 January 1958; renamed European Community 1993; absorbed into EU 2009) was the primary organisation of European economic integration — the 'Common Market' that created the customs union, common agricultural policy, and foundation for the European Single Market. The EEC transformed Western Europe from a collection of rival nation-states into the world's largest trading bloc and the most successful regional economic integration in history.\n\n"
            "The EEC was created by the six founding ECSC members (France, West Germany, Italy, Belgium, the Netherlands, Luxembourg) following the Messina Conference (1955) and the Spaak Report — which identified the customs union as the most feasible path to deeper integration following the failure of the European Defence Community (1954). The Treaty of Rome also created Euratom (European Atomic Energy Community) simultaneously, reflecting the 1950s assumption that nuclear power would be the dominant energy source of the future.\n\n"
            "The EEC's Common Agricultural Policy (CAP) — consuming 70% of the EEC budget in its early decades — protected European farmers through price supports and production subsidies, creating one of the most expensive and politically durable policies in integration history. The EEC's customs union (completing 1968 — 18 months ahead of schedule) eliminated internal tariffs and created a common external tariff wall, transforming Europe's trade patterns and making intra-EEC trade the primary driver of member-state economic growth."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Primary European economic integration body (est. 1957, Treaty of Rome); 'Common Market'; customs union completed 1968 (18 months ahead); Common Agricultural Policy (CAP) — 70% of early budget; world's largest trading bloc; most successful regional economic integration in history; Messina Conference (1955), Spaak Report design; EEC + Euratom created simultaneously; renamed EC (1993), absorbed into EU (2009); 6 founding members became EU founding 27.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The failure of the European Defence Community (1954) — when the French National Assembly rejected the supranational army proposal — drove European integrationists to redirect their ambitions toward economic integration, which was less threatening to national sovereignty than military integration",
            "The Messina Conference (1955) and the Spaak Report — commissioned by the six ECSC foreign ministers — identified the customs union as the most practically feasible path to deeper integration, providing the blueprint for the Treaty of Rome",
            "The US's Marshall Plan requirement for European economic cooperation — and Washington's continuing pressure for European integration as a Cold War strategy — provided the external incentive that maintained political support for the EEC despite French Gaullist resistance to supranationalism"
        ],
        "effects": [
            "The EEC's customs union (completed 1968) — eliminating internal tariffs and creating a common external tariff wall — transformed European trade patterns, making intra-EEC trade the primary driver of member-state growth and creating the economic interdependence that made future political union feasible",
            "The EEC's enlargement (from 6 to 9 in 1973 with UK, Ireland, Denmark; to 10 with Greece 1981; to 12 with Portugal and Spain 1986; to 15 as EU by 1995) created an expanding Common Market that progressively excluded non-member states — driving the UK's repeated applications and eventual accession and creating the 'magnet effect' of EEC membership",
            "The EEC's Common Agricultural Policy (CAP) — providing price supports and production subsidies to European farmers — created the most expensive and politically durable food policy in world history, producing 'butter mountains' and 'wine lakes' of surplus food while protecting European agriculture from global competition",
            "The EEC's institutional architecture — Commission (proposing legislation), Council (deciding legislation), Parliament (scrutinising), Court of Justice (interpreting) — became the institutional template for the European Union and the model for subsequent regional integration experiments worldwide"
        ],
        "relationships": [
            {"entity": "Treaty of Rome (25 March 1957)", "relationship": "ESTABLISHED_BY_THE", "note": "The Treaty of Rome (1957) created the EEC — signed by the six ECSC founding members and operational from 1 January 1958"},
            {"entity": "European Coal and Steel Community (ECSC, 1951)", "relationship": "BUILT_UPON_THE_INSTITUTIONAL_FOUNDATION_OF_THE", "note": "The EEC's six founding members were the ECSC founding six — building on the ECSC's institutional model for the broader common market"},
            {"entity": "Common Agricultural Policy (CAP)", "relationship": "CREATED_AND_ADMINISTERED_THE", "note": "The EEC's CAP — consuming 70% of the early budget — was the most expensive and politically durable EU policy, protecting European agriculture through price supports and production subsidies"},
            {"entity": "European Union (Treaty of Maastricht, 1993)", "relationship": "RENAMED_AND_ABSORBED_INTO_THE", "note": "The EEC became the European Community (1993) and was absorbed into the European Union by the Treaty of Lisbon (2009)"},
            {"entity": "UK accession (1973) and Brexit (2020)", "relationship": "JOINED_THE_EEC_IN_1973_AND_LEFT_THE_EU_IN_2020_IN", "note": "The UK's accession to the EEC (1973) — after two de Gaulle vetoes — and Brexit (2020) bookend the most dramatic membership history in EU history"}
        ],
    }),

    ("german-bundestag", {
        "summary": (
            "The Bundestag (est. 1949, West Germany; current building the Reichstag, Berlin — restored and reopened 1999) is the federal parliament of Germany — the lower house of the German federal legislature, which enacts federal law, elects the Federal Chancellor, and exercises parliamentary oversight of the federal government. The Bundestag is the most powerful lower house in Europe: Germany's chancellor requires Bundestag confidence, and coalition negotiations following elections produce the binding agreements that determine German government policy.\n\n"
            "The Bundestag was established by the Basic Law (Grundgesetz) of the Federal Republic of Germany (1949) — the constitutional document that West Germany's founders deliberately called a 'Basic Law' rather than a 'Constitution' to signal its temporary character until German reunification. The Bundestag met initially in Bonn (1949–1999), moving to Berlin and the restored Reichstag building (Sir Norman Foster's glass dome reconstruction) after German reunification (1990) and the German capital's return to Berlin.\n\n"
            "The Bundestag's electoral system — a mixed-member proportional system combining single-member constituencies with party list seats — is designed to combine local representation with proportional representation, preventing the pure proportionality of Weimar Germany (which produced extreme fragmentation) while avoiding the pure majoritarian distortions of the British system. The 5% threshold for list seats prevents small parties from entering parliament — a direct lesson from the Weimar Republic's proliferation of parties."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Federal parliament of Germany (est. 1949); most powerful lower house in Europe; elects Federal Chancellor; established by Basic Law (Grundgesetz, 1949) — deliberately 'Basic Law' not 'Constitution' signalling temporariness; met in Bonn (1949–1999), moved to restored Reichstag (Norman Foster glass dome, 1999) after reunification (1990); mixed-member proportional electoral system; 5% threshold preventing Weimar-style fragmentation.",
            "significanceCategory": "continental"
        },
        "causes": [
            "The catastrophic failure of the Weimar Republic's parliamentary democracy (1919–1933) — destroyed by political extremism, extreme proportional representation producing ungovernable fragmentation, and the absence of constructive no-confidence votes — drove the Basic Law's designers to create a parliament with strong chancellor stability (constructive vote of no confidence) and a 5% threshold",
            "The Allied occupation of West Germany — and the Western Allies' determination that German democracy be rebuilt on stable, anti-totalitarian foundations — shaped the Basic Law's creation of the Bundestag as a parliament with institutional checks designed to prevent the extremist abuse that brought Hitler to power",
            "German reunification (1990) — and the decision to move the federal capital from Bonn back to Berlin — drove the transformation of the Reichstag (symbol of both Weimar democracy and Nazi destruction of democracy) into the Bundestag's permanent seat, deliberately symbolising German democratic continuity"
        ],
        "effects": [
            "The Bundestag's constructive vote of no confidence — requiring that a chancellor can only be removed if an alternative chancellor can simultaneously be elected — has produced remarkable governmental stability in Germany: only one successful constructive no-confidence vote in 75 years (1982, Helmut Schmidt replaced by Helmut Kohl)",
            "Germany's coalition governments — requiring negotiated coalition agreements between parties — have produced the most programmatic and policy-coherent governments in Europe, with coalition agreements functioning as binding policy contracts rather than vague post-election power-sharing deals",
            "The Bundestag's Norman Foster-restored Reichstag building — with its glass dome open to the public, symbolising transparency and public access to parliamentary democracy — has become one of the most visited buildings in Europe and the architectural embodiment of German democratic renewal",
            "The Bundestag's growing size — expanding with each election due to proportional 'overhang' seats — reached 736 members in 2021 (the world's largest directly elected lower house by seat count), triggering a 2023 electoral reform capping it at 630 seats"
        ],
        "relationships": [
            {"entity": "Basic Law (Grundgesetz, 1949)", "relationship": "ESTABLISHED_BY_THE", "note": "The Basic Law (1949) created the Bundestag — designed to correct the Weimar Republic's parliamentary failures while signalling German democratic renewal"},
            {"entity": "Weimar Republic (1919–1933)", "relationship": "DESIGNED_TO_CORRECT_FAILURES_OF_THE", "note": "The Bundestag's 5% threshold and constructive no-confidence vote were explicit corrections of Weimar's extreme fragmentation and governmental instability"},
            {"entity": "German reunification (1990)", "relationship": "UNIFIED_GERMANY PARLIAMENT FOLLOWING", "note": "The Bundestag absorbed East German representatives after reunification (1990) and moved from Bonn to the restored Reichstag in Berlin (1999)"},
            {"entity": "Reichstag building (Norman Foster restoration, 1999)", "relationship": "MEETS_IN_THE_RESTORED", "note": "Sir Norman Foster's glass dome restoration of the Reichstag — reopened 1999 — made the Bundestag's seat the architectural symbol of German democratic renewal"},
            {"entity": "German coalition government (CDU/CSU, SPD, Greens, FDP)", "relationship": "PRODUCES_COALITION_GOVERNMENTS_THROUGH_THE", "note": "Coalition negotiations following Bundestag elections produce binding coalition agreements that determine German government policy — the most programmatic governing model in Europe"}
        ],
    }),

    ("european-atomic-energy-community", {
        "summary": (
            "The European Atomic Energy Community (Euratom, est. 1957 — Treaty of Rome signed 25 March 1957; operational 1 January 1958) is the supranational organisation created alongside the EEC to coordinate nuclear energy development in the six founding European states — creating a common market for nuclear materials, developing shared nuclear research, and establishing the framework for nuclear safety and security across the founding member states. Euratom remains in force today, making it one of the longest-lived international organisations.\n\n"
            "Euratom was created from the same 'Messina spirit' that produced the EEC — the belief that atomic energy was the energy of the future and that European countries could not individually afford the research and infrastructure costs of the nuclear age. The Spaak Report recommended Euratom alongside the EEC, and both treaties were signed simultaneously in Rome (1957). Euratom's creation reflected the 1950s expectation that nuclear power would dominate 20th-century energy — an expectation shaped by the US Atoms for Peace programme (1953) and the construction of the first commercial nuclear plants.\n\n"
            "Euratom's significance has declined from its original ambition: de Gaulle's independent French nuclear programme undermined collective nuclear development, and the rise of renewable energy has reduced nuclear power's centrality. However, Euratom remains the legal framework for nuclear safety regulation across the EU, the management of nuclear materials safeguards, and — since Brexit — the framework for the UK-EU nuclear cooperation agreement."
        ),
        "importanceScore": 8,
        "historicalSignificance": {
            "significanceScore": 8,
            "significanceNarrative": "European nuclear energy community (est. 1957, Treaty of Rome); created alongside EEC in same signing ceremony; Spaak Report recommendation; 1950s belief nuclear power would dominate future (Atoms for Peace programme 1953); de Gaulle's independent French nuclear programme undermined collective ambition; still in force — one of longest-lived international organisations; legal framework for EU nuclear safety, materials safeguards, UK-EU nuclear cooperation (post-Brexit).",
            "significanceCategory": "continental"
        },
        "causes": [
            "The 1950s belief — reflected in the US Atoms for Peace programme (1953) and the construction of the first commercial nuclear plants — that atomic energy would dominate future energy production, creating the rationale for a European collective nuclear development organisation",
            "The Spaak Report's recommendation (1956) that Euratom be created alongside the EEC — based on the analysis that individual European states could not afford the R&D costs of competitive nuclear energy programmes — provided the blueprint for the simultaneous creation of both institutions",
            "The desire to prevent German nuclear weapons development — and to manage German nuclear energy within a framework of European oversight — gave France the political motivation to support Euratom as a mechanism for channelling German nuclear ambitions into civilian energy under collective control"
        ],
        "effects": [
            "Euratom's Joint Research Centre (JRC) — established under Euratom to develop collective nuclear research — became one of Europe's most significant scientific research institutions, surviving Euratom's declining nuclear ambitions to become a broad EU research body",
            "De Gaulle's development of the Force de Frappe (independent French nuclear deterrent) outside Euratom's collective framework undermined the original vision of collective European nuclear development — demonstrating that national sovereignty on defence matters could not be pooled even within the Euratom framework",
            "Euratom's nuclear safeguards system — inspecting nuclear materials across EU member states to ensure civilian use and prevent weapons proliferation — remains the primary nuclear non-proliferation verification mechanism in Europe, operating alongside the IAEA",
            "Brexit's implications for Euratom — the UK was automatically removed from Euratom when it left the EU, requiring a new UK-Euratom nuclear cooperation agreement — illustrated how deeply integrated nuclear energy governance was with EU membership, and how Euratom's legal reach extends beyond the EU's borders"
        ],
        "relationships": [
            {"entity": "Treaty of Rome (25 March 1957)", "relationship": "CREATED_BY_THE_SAME_TREATY_THAT_CREATED_THE_EEC", "note": "Euratom and the EEC were created by treaties signed simultaneously in Rome (25 March 1957) — reflecting the 1950s dual ambition for economic and nuclear integration"},
            {"entity": "Atoms for Peace programme (US, 1953)", "relationship": "CREATION_INSPIRED_BY_THE_CONTEXT_OF_THE", "note": "Eisenhower's Atoms for Peace programme (1953) created the international framework for civilian nuclear energy that made Euratom's collective nuclear development vision politically feasible"},
            {"entity": "French Force de Frappe (independent nuclear deterrent)", "relationship": "COLLECTIVE_AMBITION_UNDERMINED_BY_DE_GAULLES", "note": "De Gaulle's development of France's independent nuclear deterrent outside Euratom's framework undermined the original vision of collective European nuclear development"},
            {"entity": "Brexit (UK leaving EU, 2020)", "relationship": "REQUIRED_NEW_UK-EURATOM_NUCLEAR_COOPERATION_AGREEMENT_FOLLOWING", "note": "Brexit automatically removed the UK from Euratom — requiring a new UK-Euratom nuclear cooperation agreement and demonstrating nuclear energy governance's deep integration with EU membership"},
            {"entity": "Joint Research Centre (JRC)", "relationship": "ESTABLISHED_THE", "note": "Euratom's Joint Research Centre became one of Europe's most significant scientific research institutions — surviving Euratom's declining nuclear ambitions to become a broad EU research body"}
        ],
    }),

    ("international-air-transport-association", {
        "summary": (
            "The International Air Transport Association (IATA, est. 1945, Havana, Cuba — reconstituted from the earlier International Air Traffic Association, 1919) is the trade association and regulatory body of the world's commercial airlines — setting the standards for airline safety, security, ticketing, baggage, aircraft turnaround, and interoperability that make the global aviation system function. IATA's 290 member airlines carry 83% of global air traffic, and its standards — from the IATA Resolution on interline ticketing to the IATA Safety Audit for Ground Operations (ISAGO) — are the invisible infrastructure of modern aviation.\n\n"
            "IATA was founded in Havana (April 1945) just before the end of World War II — when it was clear that post-war aviation would rapidly expand and that technical standards for intercontinental air travel needed to be established. Its first major achievement was establishing the interline agreement: the system by which a passenger can book a journey on multiple airlines using a single ticket, with revenue automatically shared between carriers — the technical foundation of the 'hub and spoke' global aviation network.\n\n"
            "IATA's standard-setting role extends across every aspect of airline operations: the two-letter airline codes (BA, AF, LH), three-letter airport codes (LHR, CDG, JFK), the global distribution systems for ticket booking, the standardisation of aircraft loading procedures (ULD containers), and the IATA Operational Safety Audit (IOSA) — the primary safety certification for international airlines. Airlines without IOSA certification cannot interline with most major carriers."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "World's principal airline industry body (est. 1945, Havana); 290 member airlines carrying 83% of global air traffic; interline agreement — technical foundation of global aviation network; two-letter airline codes (BA, AF, LH), three-letter airport codes (LHR, CDG, JFK); IATA Operational Safety Audit (IOSA); global distribution systems for ticket booking; ULD container standardisation; invisible infrastructure of modern aviation.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The post-World War II expansion of commercial aviation — and the recognition that intercontinental air travel would grow rapidly — created the need for international technical standards and commercial agreements that would allow airlines of different countries to exchange passengers, baggage, and revenue seamlessly",
            "The Chicago Convention (1944) — establishing the legal framework for international civil aviation under the International Civil Aviation Organization (ICAO) — created the governmental framework within which a non-governmental airline industry body was needed to establish commercial and operational standards",
            "The wartime experience of the early 1920s airline industry — in which the absence of interoperability standards created operational chaos — provided the negative lesson that drove IATA's founders to prioritise technical and commercial standardisation from the outset"
        ],
        "effects": [
            "IATA's interline agreement — allowing passengers to travel on multiple airlines with a single ticket, with revenue automatically shared — created the global 'hub and spoke' aviation network, making it possible to travel anywhere in the world on a single itinerary through a combination of carriers",
            "IATA's standardised two-letter airline codes and three-letter airport codes — now the universal language of global aviation — are used in every reservation system, departure board, and air traffic control communication worldwide, making IATA's standards the invisible infrastructure of the global travel industry",
            "IATA's Operational Safety Audit (IOSA) — the primary international safety certification for airlines — has driven global aviation safety improvements: the IOSA-certified airline fatality rate is 12 times lower than the non-IOSA rate, making IOSA the most effective safety intervention in aviation history",
            "IATA's role as the aviation industry's primary negotiating body with governments — on aviation taxes, carbon pricing, slot allocation, and route rights — gives the airline industry collective leverage in policy discussions that individual carriers could not achieve, shaping global aviation policy"
        ],
        "relationships": [
            {"entity": "International Civil Aviation Organization (ICAO)", "relationship": "COMMERCIAL_COUNTERPART_TO_THE_GOVERNMENTAL", "note": "IATA is the airline industry's non-governmental standard-setting body — complementing ICAO's governmental framework for international civil aviation"},
            {"entity": "Interline agreement (global aviation network foundation)", "relationship": "ESTABLISHED_THE", "note": "IATA's interline agreement — allowing single-ticket travel on multiple airlines with automatic revenue sharing — is the commercial foundation of the global hub-and-spoke aviation network"},
            {"entity": "IATA Operational Safety Audit (IOSA)", "relationship": "ADMINISTERS_THE_GLOBAL_AIRLINE_SAFETY_CERTIFICATION", "note": "IOSA certification — the primary international airline safety audit — has driven global safety improvements: IOSA-certified airlines have 12× lower fatality rates"},
            {"entity": "Global Distribution Systems (Amadeus, Sabre, Travelport)", "relationship": "STANDARDS_ENABLING_THE", "note": "IATA's standardised airline and airport codes are the backbone of the global distribution systems through which airlines sell tickets worldwide"},
            {"entity": "Chicago Convention (1944) and ICAO", "relationship": "CREATED_IN_CONTEXT_OF_THE", "note": "IATA was reconstituted (1945) in the context of the Chicago Convention (1944) that created ICAO — providing the commercial standards that complemented ICAO's governmental framework"}
        ],
    }),

    ("khmer-rouge", {
        "summary": (
            "The Khmer Rouge (Khmer Rouges — 'Red Khmers', est. c.1968 — formally the Communist Party of Kampuchea; ruled Cambodia as Democratic Kampuchea 1975–1979; defeated by Vietnamese invasion January 1979) was the Maoist revolutionary movement that seized power in Cambodia in April 1975 and carried out one of the most extreme and lethal genocides in 20th-century history, killing between 1.5 and 2 million people — approximately 25% of Cambodia's population — in four years through execution, starvation, forced labour, and disease during its radical agrarian revolution.\n\n"
            "Led by Pol Pot (Saloth Sar) and a small inner circle educated in Paris, the Khmer Rouge implemented 'Year Zero' — the most radical social transformation ever attempted: evacuating all cities within days of taking power (forcing 2 million people from Phnom Penh in three days), abolishing money, schools, hospitals, religion, and private property, executing anyone associated with the previous government, the educated classes, ethnic minorities, and anyone wearing glasses (a perceived sign of education). Cambodia was renamed 'Democratic Kampuchea' and the calendar was reset to Year Zero.\n\n"
            "The Vietnamese invasion (January 1979) toppled the Khmer Rouge — but the movement continued as a guerrilla force in the jungle for two decades, retaining Cambodia's UN seat (with US and Chinese support during the Cold War) until 1993. The Extraordinary Chambers in the Courts of Cambodia (ECCC) — established in 2006 — has convicted four senior leaders including Nuon Chea and Khieu Samphan for crimes against humanity and genocide."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Cambodian Maoist genocide movement (est. c.1968; ruled 1975–1979); 1.5–2 million dead — ~25% of Cambodia's population; 'Year Zero' — evacuated all cities (2 million from Phnom Penh in 3 days), abolished money/schools/hospitals/religion/private property; execution of educated classes, ethnic minorities, glasses-wearers; defeated by Vietnamese invasion (1979); retained UN seat (with US/Chinese Cold War support) until 1993; ECCC convictions of Nuon Chea, Khieu Samphan.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "US bombing of Cambodia (1969–1973) — Operation Menu and Operation Freedom Deal, dropping more bombs on Cambodia than the Allies dropped in the entire Pacific theatre of World War II — devastated the Cambodian countryside, killed hundreds of thousands, destroyed the Lon Nol government's legitimacy, and drove rural Cambodians into the Khmer Rouge's arms",
            "Pol Pot and the Paris-educated Khmer Rouge leadership's fusion of Maoist revolutionary theory with Khmer cultural nationalism — and their romanticisation of the Angkor empire as a model of agrarian civilisation superior to Western modernity — drove the 'Year Zero' ideology of returning Cambodia to a pure agrarian society",
            "The Lon Nol coup (1970) — backed by the US — that overthrew Prince Sihanouk destabilised Cambodia, giving the Khmer Rouge the political opportunity to position themselves as the legitimate resistance and allowing Sihanouk to endorse them from Beijing, dramatically expanding their recruitment"
        ],
        "effects": [
            "The Cambodian genocide (1975–1979) — killing 25% of Cambodia's population — was the highest per capita death toll of any 20th-century genocide, creating a generational trauma that continues to shape Cambodian society, politics, and culture 50 years later",
            "The Vietnamese invasion that toppled the Khmer Rouge (1979) — and Vietnam's subsequent occupation of Cambodia (1979–1989) — triggered a proxy war between Vietnam (backed by the USSR) and China (which continued supporting the Khmer Rouge), creating a decade of regional conflict and humanitarian crisis",
            "The Khmer Rouge's retention of Cambodia's UN seat (1979–1993) — with US and Chinese support — despite its genocide and defeat is a damning case study in Cold War geopolitics overriding human rights, where strategic interests prevented international accountability for genocide for 14 years",
            "The Extraordinary Chambers in the Courts of Cambodia (ECCC, 2006–2022) — established by the UN and Cambodian government — produced the first genocide convictions for Khmer Rouge leaders, but its slow pace (only 4 convictions in 16 years, with most perpetrators dying before trial) raised fundamental questions about the effectiveness of delayed international criminal justice"
        ],
        "relationships": [
            {"entity": "Pol Pot (Saloth Sar — Khmer Rouge leader)", "relationship": "LED_BY", "note": "Pol Pot's 'Year Zero' ideology — fusing Maoist theory with Khmer cultural nationalism — drove the Cambodian genocide's extreme radicalism"},
            {"entity": "US bombing of Cambodia (1969–1973, Operations Menu and Freedom Deal)", "relationship": "RISE_TO_POWER_FACILITATED_BY_DEVASTATION_CAUSED_BY", "note": "US bombing dropped more explosives on Cambodia than in the entire Pacific WWII theatre — destroying rural communities and driving Cambodians into the Khmer Rouge's arms"},
            {"entity": "Vietnamese invasion of Cambodia (January 1979)", "relationship": "RULE_ENDED_BY_THE", "note": "Vietnam's invasion (1979) toppled the Khmer Rouge government — but Pol Pot's forces continued as a jungle guerrilla force for two decades"},
            {"entity": "Extraordinary Chambers in the Courts of Cambodia (ECCC, 2006)", "relationship": "PROSECUTED_FOR_GENOCIDE_AND_CRIMES_AGAINST_HUMANITY_BY_THE", "note": "The ECCC convicted four Khmer Rouge leaders (Nuon Chea, Khieu Samphan) for crimes against humanity and genocide — the first accountability for the Cambodian genocide"},
            {"entity": "Cold War geopolitics (US-China-Vietnam proxy conflict)", "relationship": "RETENTION_OF_UN_SEAT_ENABLED_BY", "note": "US and Chinese Cold War interests in opposing Vietnam led both to support the defeated Khmer Rouge's retention of Cambodia's UN seat until 1993 — overriding accountability for genocide"}
        ],
    }),

    ("leiden-university", {
        "summary": (
            "Leiden University (Universiteit Leiden, est. 1575, Leiden, Netherlands — the oldest university in the Netherlands, founded by William of Orange) is one of Europe's leading research universities, renowned for its role in the Scientific Revolution, the Dutch Golden Age of learning, and its continuous tradition of scholarship from the 16th century to the present. Leiden's early faculty included René Descartes, Christiaan Huygens, Rembrandt van Rijn (as a student), Baruch Spinoza (studied informally), and the early anatomists who founded the Leiden tradition of medical education.\n\n"
            "Leiden was founded by William of Orange in 1575 as a reward to the citizens of Leiden for their heroic resistance to the Spanish siege (1573–1574) — during which roughly one-third of the city's population died of plague and starvation before the Sea Beggars relieved the siege by cutting the dikes. The citizens could choose between a tax exemption and a university; they chose the university. This origin story — a university as a reward for heroic resistance — gave Leiden a distinctive founding identity as an institution of civil freedom and scholarly independence.\n\n"
            "Leiden's Botanical Garden (Hortus Botanicus, est. 1590 — one of the oldest botanical gardens in the world) and its early anatomy theatre (Theatrum Anatomicum, 1594) were foundational institutions of the Scientific Revolution. The Leiden tradition of comparative anatomy — developed by the Boerhaave school of medicine — established clinical medical education as the model for European medical training."
        ),
        "importanceScore": 9,
        "historicalSignificance": {
            "significanceScore": 9,
            "significanceNarrative": "Oldest Dutch university (est. 1575); founded by William of Orange as reward for Leiden's heroic resistance to Spanish siege (1573–1574); citizens chose university over tax exemption; faculty included Descartes, Huygens; Rembrandt and Spinoza studied there; Hortus Botanicus (1590, one of world's oldest botanical gardens); Theatrum Anatomicum (1594); Boerhaave school of medicine — model for European clinical medical training; centre of Dutch Golden Age learning.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Spanish siege of Leiden (1573–1574) — during which approximately one-third of the city's population died of plague and starvation before the Sea Beggars' relief — created the heroic civic narrative that William of Orange rewarded with a university, giving Leiden its unique founding identity",
            "William of Orange's political strategy of creating a Protestant intellectual centre in the newly independent Netherlands — capable of training the Reformed clergy, lawyers, and physicians that the Dutch Republic needed — drove the university's founding and its early emphasis on theology, law, and medicine",
            "The Dutch Golden Age's combination of commercial wealth, religious tolerance (relative to Catholic Europe), and civic humanism created the cultural and economic conditions for Leiden's rapid growth into one of Europe's leading universities — attracting scholars fleeing religious persecution elsewhere"
        ],
        "effects": [
            "Leiden's medical school — developed by Herman Boerhaave (1668–1738) into the model of clinical medical education — established bedside teaching and systematic clinical observation as the foundations of medical training, creating the 'Leiden model' adopted by Edinburgh, Vienna, and eventually all European medical schools",
            "Leiden's Hortus Botanicus (1590) — among the world's oldest botanical gardens — was the primary site for the introduction of tulips to Europe (Carolus Clusius, 1594), initiating the tulip mania (Tulpenmanie, 1636–1637) and establishing the Netherlands as the centre of European horticulture",
            "Leiden's tradition of humanist scholarship — including the study of Arabic, Persian, and Chinese manuscripts in its Oriental collections — established the philological foundations of comparative linguistics and Oriental studies, making Leiden the primary European centre for the study of Islamic and Asian civilisations",
            "Leiden's alumni include 16 Nobel laureates (including Heike Kamerlingh Onnes for superconductivity, Pieter Zeeman for the Zeeman effect), 6 Dutch Prime Ministers, and René Descartes — making it one of the most impactful universities in intellectual history relative to its size"
        ],
        "relationships": [
            {"entity": "William of Orange (founding patron)", "relationship": "FOUNDED_BY", "note": "William of Orange founded Leiden University (1575) as a reward to citizens for heroic resistance to the Spanish siege — giving the university its founding identity as an institution of civic freedom"},
            {"entity": "Spanish siege of Leiden (1573–1574)", "relationship": "FOUNDING_ORIGIN_IN_AFTERMATH_OF_THE", "note": "Leiden's citizens chose a university over a tax exemption as reward for surviving the siege — creating the university's distinctive founding narrative"},
            {"entity": "Herman Boerhaave (1668–1738, clinical medicine)", "relationship": "HOME_INSTITUTION_OF_THE_INFLUENTIAL", "note": "Boerhaave's Leiden medical school — establishing bedside clinical teaching — became the model for European medical education, adopted by Edinburgh, Vienna, and all major medical schools"},
            {"entity": "Hortus Botanicus Leiden (est. 1590)", "relationship": "HOME_OF_THE", "note": "The Hortus Botanicus — among the world's oldest botanical gardens — was the site of tulip introduction to Europe (Clusius, 1594), initiating Dutch tulip mania"},
            {"entity": "Dutch Golden Age (17th century)", "relationship": "INTELLECTUAL_CENTRE_OF_THE", "note": "Leiden's combination of scholarly tolerance, commercial wealth, and Reformed tradition made it the primary intellectual centre of the Dutch Golden Age"}
        ],
    }),

]

if __name__ == "__main__":
    print(f"Batch 30 — {len(ENTITIES)} entities (Class 333: Theatre, Film, Economic Bodies, Universities)")
    for slug, data in ENTITIES:
        print(f"\n→ {slug}")
        enrich_entity(slug, data)
    print("\n✓ Done")
