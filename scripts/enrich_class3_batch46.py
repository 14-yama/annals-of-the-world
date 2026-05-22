#!/usr/bin/env python3
"""
Batch 46 — 8 entities (Class 391): Famous Armies
editorId: vscode-copilot
"""
import json, os
from datetime import datetime, timezone

EDITOR_ID = "vscode-copilot"
NOW = datetime.now(timezone.utc).isoformat()
FOLDER = "/home/manasa151/annals-of-the-world/data/appwrite-export/entities/391-Class-391"
FILE_PREFIX = "391"


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

    ("roman-army", {
        "summary": (
            "The Roman Army (exercitus Romanus — from the archaic citizen-militia of the Roman Kingdom through the late imperial legions, c. 753 BCE–476 CE) was the most effective military institution in the ancient Western world and the primary vehicle through which Rome expanded from a city-state to an empire controlling the entire Mediterranean basin. At its peak under Septimius Severus (c. 200 CE), the Roman Army comprised 450,000+ professional soldiers — structured into 30 legions supported by auxiliary cohorts — and had conquered territories from Britain to Mesopotamia, leaving a military legacy that shaped every subsequent Western army.\n\n"
            "The Roman Army evolved through distinct phases: the citizen-militia of the Roman Republic (mobilised annually, fighting in the manipular formation); the professional legions of the late Republic (Marian reforms of 107 BCE — Gaius Marius abolished the property qualification for military service, creating a professional army loyal to its commander rather than the state, directly enabling the civil wars); and the standing imperial army (from Augustus, 27 BCE — 25 legions permanently deployed at fixed bases with career soldiers on 25-year service). The Marian reforms are among the most consequential administrative decisions in Roman history — the shift from a citizen-soldier army to a professional force was the primary structural precondition for the late Republic's military dictators.\n\n"
            "The Roman legionary's standard equipment — the pilum (weighted javelin), gladius (short stabbing sword), lorica segmentata (segmented armour), scutum (curved rectangular shield), and caligae (hobnailed boots) — together with the legion's tactical flexibility and engineering capability (building a camp every night, constructing siege works, bridging rivers) made the Roman Army the most consistently effective military force in the Mediterranean world for 500+ years."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Most effective military institution of ancient Western world (c. 753 BCE–476 CE); 450,000+ professional soldiers at peak (Septimius Severus, c. 200 CE); 30 legions, Britain to Mesopotamia; Marian reforms (107 BCE, Gaius Marius — professional army, property qualification abolished, commander loyalty) — direct structural precondition for late Republic civil wars; Augustus standing imperial army (27 BCE, 25 legions); pilum, gladius, lorica segmentata, scutum; 500+ years of consistent military dominance; shaped every subsequent Western army.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Roman Republic's territorial expansion — requiring armies in multiple theatres simultaneously and for increasingly extended periods — overwhelmed the capacity of the citizen-militia system, where property-owning citizens served seasonally and were needed for their farms, creating the political demand for military reform",
            "The Marian reforms (107 BCE) — in which Gaius Marius abolished the property qualification for military service, providing equipment from the state and creating a professional force — transformed the Roman Army from a citizen-militia into a professional body loyal to its commanding general rather than the state, directly enabling the late Republic's military dictators (Sulla, Caesar, Pompey)",
            "The Roman Army's tactical superiority — particularly the flexible manipular formation (replacing the Greek phalanx's rigid line) and the legion's engineering and logistical capability — over the armies of Rome's enemies created positive feedback: military success enabled territorial expansion, which provided the economic resources for larger armies"
        ],
        "effects": [
            "The Roman Army's conquest of the Mediterranean basin — creating the Pax Romana (27 BCE–180 CE, approximately 200 years of relative peace within the empire's borders) — created the political and economic conditions for the greatest period of economic integration and cultural exchange in the ancient world, with free trade, a single currency, and standardised law across an enormous territory",
            "The Marian reforms' creation of a professional army loyal to its commander rather than the state directly enabled the late Republic's military dictators (Sulla, Caesar, Antony) to use their armies for political purposes — making the fall of the Republic and the transition to the Principate a structural consequence of military reform",
            "The Roman Army's engineering legacy — roads (75,000+ km of paved roads), aqueducts, fortifications (Hadrian's Wall), bridges, and the standardised Roman camp layout — shaped the physical infrastructure of Europe for centuries, with Roman roads remaining in use for 1,000+ years after the fall of Rome",
            "The Roman Army's model — professional career soldiers, standardised equipment and training, integrated engineering capability, logistical infrastructure, and disciplined hierarchical command — became the template for every subsequent European army from the Byzantine Empire to the early modern professional armies of the 16th–17th centuries"
        ],
        "relationships": [
            {"entity": "Gaius Marius (Marian reforms 107 BCE, professional army, property qualification abolished)", "relationship": "FUNDAMENTALLY_RESTRUCTURED_BY_THE_MILITARY_REFORMS_OF", "note": "Marius's reforms — creating a professional army loyal to its commander — were the primary structural precondition for the late Republic's civil wars"},
            {"entity": "Augustus (Principate, 27 BCE, standing imperial army 25 legions)", "relationship": "REFORMED_INTO_PERMANENT_STANDING_FORCE_BY", "note": "Augustus's creation of the permanent standing army — 25 legions at fixed bases, 25-year service careers — defined the imperial Roman military"},
            {"entity": "Pax Romana (27 BCE–180 CE, 200 years of relative peace within empire borders)", "relationship": "PRIMARY_MILITARY_GUARANTEE_OF_THE", "note": "The Roman Army's conquest and pacification of the Mediterranean basin created the conditions for the Pax Romana — the greatest period of economic integration in the ancient world"},
            {"entity": "Roman engineering (75,000+ km roads, aqueducts, Hadrian's Wall, bridges)", "relationship": "BUILDER_OF_THE_PRIMARY_ENGINEERING_INFRASTRUCTURE_OF_THE_ROMAN_EMPIRE_INCLUDING", "note": "The Roman Army's engineering capability — roads, aqueducts, fortifications, bridges — shaped European infrastructure for centuries after Rome's fall"},
            {"entity": "Roman Republic civil wars (Sulla, Caesar, Pompey — Marian reforms consequence)", "relationship": "MARIAN_REFORMS_OF_WHICH_CREATED_THE_STRUCTURAL_CONDITIONS_FOR_THE", "note": "The Marian reforms' professional army loyal to its commander rather than the state directly enabled the civil wars that ended the Republic"}
        ],
    }),

    ("british-army", {
        "summary": (
            "The British Army (est. 1707 as the unified army of Great Britain — though tracing its origins to the English standing army established by the Restoration Parliament in 1661 and the English Civil War New Model Army of 1645) is one of the oldest and most globally experienced professional armies in history, having served in every inhabited continent and shaped the political history of an empire that at its peak (1920) controlled 24% of the world's land surface. The British Army's regimental system — the most enduring organisational innovation in military history — created institutional identity and fighting spirit through loyalty to a regiment's history rather than abstract nationality.\n\n"
            "The British Army's defining campaigns include the Seven Years' War (1756–1763, establishing British global dominance over France), the Napoleonic Wars (1803–1815, the Peninsular War and Waterloo), the Crimean War (1854–1856, the scandal that created modern military nursing through Florence Nightingale), and the First and Second World Wars. At its peak in 1918, the British Army deployed 4 million men — the largest in British history — across France, the Middle East, East Africa, and India.\n\n"
            "The British Army's most consequential institutional legacy is the regimental system — in which soldiers serve for life in a regiment with its own history, badges, traditions, and regional identity — which was adopted by most Commonwealth armies and creates the battlefield cohesion that military psychologists identify as the primary determinant of fighting effectiveness. The British Army's experience of colonial warfare — from the Indian Mutiny (1857) to the Boer War (1899–1902) and Malaya (1948–1960) — also produced the Counter-Insurgency (COIN) doctrine that continues to shape Western military practice."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "One of oldest and most globally experienced professional armies (est. 1707 as Great Britain unified army; English standing army 1661, New Model Army 1645); British Empire peak 1920 — 24% of world's land surface; regimental system — most enduring organisational innovation in military history; Seven Years' War (global dominance over France), Napoleonic Wars (Waterloo), Crimea (Florence Nightingale), WWI 4 million men peak; Counter-Insurgency (COIN) doctrine from colonial warfare; served on every inhabited continent.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The English Civil War's New Model Army (1645) — Parliament's professional standing army, with officers promoted by merit rather than social rank and soldiers recruited nationally — created the institutional template for the British standing army, demonstrating that a professional merit-based military could consistently defeat aristocratic armies",
            "The Restoration Parliament's creation of the English standing army (1661) — as Charles II's response to the political vulnerability demonstrated by the Civil War and the republican period — established the permanent military institution that became the British Army, funded by parliamentary vote and accountable to Parliament rather than the Crown alone",
            "Britain's 18th-century commercial and imperial expansion — creating colonial possessions, trade routes, and commercial interests across multiple continents that required military protection — drove the British Army's global deployment and the development of the expeditionary military tradition that defined British strategic culture"
        ],
        "effects": [
            "The British Army's decisive role in the Seven Years' War (1756–1763) — defeating France in North America, India, the Caribbean, and Europe simultaneously — established Britain as the dominant global colonial power, creating the British Empire that would reach its peak extent in 1920 and define the political map of the 20th century",
            "The regimental system — maintained through every subsequent period of military reform — created the institutional cohesion that military psychologists identify as the primary determinant of battlefield effectiveness, and was adopted by most Commonwealth armies, establishing a model of military organisation that has survived for 350+ years",
            "The Crimean War's exposure of military medical inadequacy — and Florence Nightingale's reform of military nursing and hospital hygiene — transformed military and civilian medicine, establishing the modern nursing profession and the evidence-based approach to hospital infection control that has saved millions of lives",
            "The British Army's Counter-Insurgency (COIN) doctrine — developed through colonial warfare (Indian Mutiny, Boer War, Malaya, Aden, Northern Ireland) — became the foundational doctrine of Western military practice in the post-colonial era, directly influencing US COIN strategy in Vietnam, Iraq, and Afghanistan"
        ],
        "relationships": [
            {"entity": "New Model Army (1645, English Civil War, professional merit-based military template)", "relationship": "INSTITUTIONAL_ORIGINS_IN_THE", "note": "Parliament's New Model Army — officers by merit, national recruitment — created the institutional template for the British standing army"},
            {"entity": "Seven Years' War (1756–1763, British global dominance over France established)", "relationship": "DECISIVE_MILITARY_INSTRUMENT_OF_THE", "note": "The British Army's simultaneous victories over France in North America, India, the Caribbean, and Europe established Britain as the dominant global colonial power"},
            {"entity": "British regimental system (organisational innovation, Commonwealth adoption)", "relationship": "ORIGINATOR_OF_THE", "note": "The regimental system — lifetime service in a regiment with its own history and identity — is the most enduring organisational innovation in military history, adopted across the Commonwealth"},
            {"entity": "Florence Nightingale (Crimean War nursing reform, modern nursing profession origins)", "relationship": "MILITARY_MEDICAL_INADEQUACY_EXPOSED_BY_WHICH_DROVE_THE_NURSING_REFORMS_OF", "note": "The Crimean War's exposure of British military medical failures drove Nightingale's reform that created the modern nursing profession"},
            {"entity": "Counter-Insurgency doctrine (COIN, colonial warfare origins, Western military practice)", "relationship": "ORIGINATOR_OF_THE", "note": "The British Army's COIN doctrine — developed through colonial warfare — became the foundational doctrine of Western military practice in the post-colonial era"}
        ],
    }),

    ("red-army", {
        "summary": (
            "The Red Army (Raboche-Krestyanskaya Krasnaya Armiya, Workers' and Peasants' Red Army — est. 1918, reorganised 1946 as the Soviet Army) was the military force of Soviet Russia and later the Soviet Union — growing from a revolutionary improvisation of 1918 to a force of 34 million men mobilised during the Second World War, suffering 8.7 million military deaths, and ultimately destroying 80% of Germany's Wehrmacht in the Eastern Front campaign that was the decisive theatre of the Second World War. The Red Army's victory over Nazi Germany — achieved at a cost that dwarfs all other WWII military operations — is the defining military achievement of the 20th century.\n\n"
            "The Red Army was created by Leon Trotsky (People's Commissar of War, 1918–1924) from the disintegrating Tsarist Army and armed workers' militia — using former Tsarist officers under political commissar oversight, conscription, and a centralised command structure — to fight the Russian Civil War (1918–1922) against the White Army and 14 foreign interventionist forces simultaneously. Trotsky's achievement — creating an effective army from revolutionary chaos in two years — is one of the most remarkable administrative feats in military history.\n\n"
            "The Red Army's performance in Operation Bagration (June–August 1944) — destroying Army Group Centre (28 German divisions) in the most complete tactical encirclement in military history — demonstrated the complete Soviet military maturation from the catastrophic 1941 defeats, and the subsequent advance to Berlin (1944–1945) ended Nazi Germany. The Red Army's post-war occupation of Eastern Europe created the military basis for the Soviet bloc and the Cold War."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Military force of Soviet Russia/USSR (est. 1918); 34 million mobilised WWII; 8.7 million military deaths; destroyed 80% of Germany's Wehrmacht — Eastern Front decisive theatre of WWII; Leon Trotsky creator (1918–1924, from revolutionary chaos, former Tsarist officers under commissars); Russian Civil War (1918–1922) — 14 interventionist forces; Operation Bagration (June–August 1944 — Army Group Centre destroyed, 28 divisions, greatest encirclement in military history); Berlin advance (1944–1945); Soviet bloc creation — Cold War military basis.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Russian Revolution (1917) and the collapse of the Tsarist Army — which disintegrated through mass desertion, officer assassinations by revolutionary soldiers, and the general breakdown of military discipline following the February and October Revolutions — created the political necessity of creating a new military force from scratch to defend the Soviet state",
            "Leon Trotsky's decision to employ former Tsarist officers under political commissar oversight — controversial within the Bolshevik movement but militarily essential — provided the professional military expertise that created an effective fighting force from revolutionary volunteers and conscripts",
            "Germany's 1941 Operation Barbarossa — the largest military operation in history, killing or capturing 3.8 million Soviet soldiers in six months — paradoxically created the conditions for the Red Army's eventual decisive superiority through the industrial mobilisation, doctrinal learning, and leadership selection it forced on the Soviet state"
        ],
        "effects": [
            "The Red Army's destruction of 80% of the Wehrmacht's military strength on the Eastern Front (1941–1945) — at a cost of 8.7 million military deaths and 26+ million Soviet civilian and military total deaths — was the decisive contribution to the defeat of Nazi Germany, making the Eastern Front the central military theatre of the Second World War by any measure of forces engaged, casualties, or strategic consequence",
            "The Red Army's post-war occupation of Eastern Europe — installing communist governments in Poland, Czechoslovakia, Hungary, Romania, Bulgaria, and East Germany — created the Soviet bloc whose existence defined the Cold War, including the Berlin Wall, the Warsaw Pact, and the nuclear competition that structured international relations for 45 years",
            "Operation Bagration's demonstration of the 'deep battle' tactical concept — simultaneous attacks at multiple points along a broad front, denying the enemy the ability to concentrate reserves — became the doctrinal foundation of Soviet and subsequent Russian military thinking, and directly influenced NATO's AirLand Battle doctrine of the 1980s",
            "The Red Army's creation by Trotsky — and its institutionalisation as a professional conscript army with a political commissar system — established the model for subsequent communist military forces (Chinese People's Liberation Army, Vietnamese People's Army, Cuban Revolutionary Armed Forces), spreading the Soviet military-political model across the communist world"
        ],
        "relationships": [
            {"entity": "Leon Trotsky (creator 1918–1924, People's Commissar of War, former Tsarist officers policy)", "relationship": "CREATED_AND_BUILT_INTO_EFFECTIVE_FORCE_BY", "note": "Trotsky's creation of the Red Army from revolutionary chaos — using former Tsarist officers under commissar oversight — is one of the most remarkable military administrative achievements in history"},
            {"entity": "Eastern Front WWII (1941–1945, 80% of Wehrmacht destroyed, decisive theatre)", "relationship": "PRIMARY_MILITARY_FORCE_OF_THE", "note": "The Red Army's destruction of 80% of Germany's Wehrmacht — at a cost of 8.7M military deaths — made the Eastern Front the decisive theatre of the Second World War"},
            {"entity": "Operation Bagration (June–August 1944, Army Group Centre destroyed, greatest encirclement)", "relationship": "GREATEST_OFFENSIVE_TRIUMPH_WAS", "note": "Bagration — destroying 28 German divisions and Army Group Centre — was the most complete tactical encirclement in military history and demonstrated complete Red Army military maturation"},
            {"entity": "Soviet bloc Eastern Europe (post-WWII occupation, Cold War creation)", "relationship": "MILITARY_BASIS_FOR_THE_CREATION_OF_THE", "note": "The Red Army's post-war occupation of Eastern Europe — installing communist governments — created the Soviet bloc that defined the Cold War"},
            {"entity": "Operation Barbarossa (1941, 3.8M Soviet POWs, paradoxical Soviet military development)", "relationship": "INITIAL_CATASTROPHIC_DEFEAT_BY_THE_GERMAN", "note": "Barbarossa's devastation paradoxically drove the Soviet military industrialisation and doctrinal learning that produced the Red Army's eventual decisive superiority"}
        ],
    }),

    ("imperial-japanese-army", {
        "summary": (
            "The Imperial Japanese Army (Dai-Nippon Teikoku Rikugun — est. 1871, formally constituted under the Meiji Emperor, dissolved 1945) was the land force of Imperial Japan — which grew from a modernised conscript force (modelled on the German Imperial Army) to a force of 6 million men by 1945, conquering the largest land empire in Asia since the Mongols (from Manchuria to New Guinea, 1937–1942), and committing some of the most extensively documented war crimes of the 20th century (Nanjing Massacre, Bataan Death March, Unit 731 biological warfare programme) while simultaneously demonstrating tactical and operational capabilities that consistently surprised its adversaries.\n\n"
            "The Imperial Japanese Army was created from the Meiji government's decision to abolish the samurai class's military monopoly (1873 — universal conscription replacing the feudal warrior caste) and construct a European-style professional army. The Prussian military model — adopted after the Franco-Prussian War demonstrated its superiority — provided the organisational template, with German officers advising and Japanese officers trained in Germany. The army's early victories (Sino-Japanese War 1894–1895, Russo-Japanese War 1904–1905 — defeating a European Great Power for the first time in modern history) created the myth of Japanese military invincibility.\n\n"
            "The Imperial Japanese Army's strategic culture — centred on offensive spirit (seishin), contempt for surrender (bushido warrior code adapted to military context), and institutional independence from civilian control — produced both the tactical aggression that won rapid early victories and the catastrophic strategic decision-making (refusal to accept defeat, no surrender policy) that extended the Pacific War and resulted in the atomic bombings of Hiroshima and Nagasaki."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Land force of Imperial Japan (est. 1871 Meiji era, dissolved 1945); 6 million men by 1945; largest Asian land empire since Mongols (Manchuria to New Guinea, 1937–1942); Prussian military model, German officers; Sino-Japanese War (1894–1895), Russo-Japanese War (1904–1905) — first defeat of European Great Power by Asian nation; Nanjing Massacre, Bataan Death March, Unit 731 biological warfare; Meiji universal conscription (1873) replacing samurai monopoly; no-surrender policy — atomic bombings of Hiroshima and Nagasaki.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Meiji Restoration's modernisation programme — recognising that Japan's survival as an independent nation required a modern European-style military — drove the creation of a conscript army on the Prussian model, replacing the feudal samurai class with a national conscript force that drew on all social classes",
            "The Russo-Japanese War's demonstration of Japanese military effectiveness (1904–1905) — the first defeat of a European Great Power by an Asian nation in the modern era — created a strategic culture of military confidence that consistently underestimated adversaries and overestimated Japanese offensive capability",
            "The institutional independence of the Japanese military from civilian control — embedded in the Meiji Constitution's provision that the military reported directly to the Emperor rather than the cabinet — created the structural conditions for the military's domination of Japanese politics in the 1930s and the decisions that led to war with China and the United States"
        ],
        "effects": [
            "The Imperial Japanese Army's conquest of East and Southeast Asia (1937–1942) — occupying China, Southeast Asia, and the Pacific islands — ended the European colonial empires in Asia more effectively than any nationalist movement had achieved, accelerating decolonisation and the emergence of independent Asian states (Indonesia, Vietnam, Burma, India) in the postwar period",
            "The Imperial Japanese Army's war crimes — the Nanjing Massacre (1937, 200,000+ Chinese civilians killed), the Bataan Death March (1942), the comfort women system, and Unit 731's biological warfare experiments — created lasting historical and diplomatic disputes between Japan and China, Korea, and the Philippines that continue to shape East Asian geopolitics",
            "The Imperial Japanese Army's no-surrender strategic culture — producing kamikaze attacks, Iwo Jima and Okinawa casualties, and the projected 1 million Allied casualties for a mainland invasion — directly drove the US decision to use atomic bombs at Hiroshima and Nagasaki, making the IJA's strategic culture a proximate cause of the nuclear age's opening",
            "The Imperial Japanese Army's rapid defeat of European colonial forces in 1941–1942 — the fall of Singapore, the capture of the Dutch East Indies, the defeat of the French in Indochina — permanently shattered the myth of European racial and military superiority in Asia, creating the psychological conditions for the postwar decolonisation of South and Southeast Asia"
        ],
        "relationships": [
            {"entity": "Meiji Restoration (1868, universal conscription 1873, Prussian model adoption)", "relationship": "CREATED_AS_PART_OF_THE_MILITARY_MODERNISATION_OF_THE", "note": "The Meiji Restoration's abolition of the samurai military monopoly and creation of universal conscription on the Prussian model created the institutional foundation of the Imperial Japanese Army"},
            {"entity": "Russo-Japanese War (1904–1905, first defeat of European Great Power by Asian nation)", "relationship": "EARLY_DEFINITIVE_VICTORY_OVER_RUSSIA_THAT_ESTABLISHED_ITS_GLOBAL_REPUTATION_IN_THE", "note": "The Russo-Japanese War — the first defeat of a European Great Power by an Asian nation — created the strategic overconfidence that characterised the IJA's subsequent decisions"},
            {"entity": "Nanjing Massacre (1937, 200,000+ Chinese civilians killed)", "relationship": "PERPETRATOR_OF_THE", "note": "The IJA's Nanjing Massacre — killing 200,000+ Chinese civilians — is the most extensively documented Japanese war crime and continues to shape Sino-Japanese relations"},
            {"entity": "Unit 731 (biological warfare programme, Manchuria, human experimentation)", "relationship": "INSTITUTIONAL_SPONSOR_OF_THE_BIOLOGICAL_WARFARE_PROGRAMME", "note": "Unit 731's biological warfare experiments — conducted on Chinese, Russian, and Allied prisoners — are among the most extensively documented war crimes of the 20th century"},
            {"entity": "Atomic bombings of Hiroshima and Nagasaki (August 1945, no-surrender policy consequence)", "relationship": "NO-SURRENDER_STRATEGIC_CULTURE_OF_WHICH_WAS_PROXIMATE_CAUSE_OF_THE", "note": "The IJA's no-surrender doctrine — projecting 1M Allied casualties for mainland invasion — directly drove the US decision to use atomic bombs, making the IJA's strategic culture a proximate cause of the nuclear age"}
        ],
    }),

    ("prussian-army", {
        "summary": (
            "The Prussian Army (Preußische Armee — formally constituted under the Great Elector Frederick William of Brandenburg in the 1650s–1660s, reaching its apogee under Frederick the Great (1740–1786), and transformed into the German Army through the Austro-Prussian War (1866) and Franco-Prussian War (1870–1871)) was the most influential military institution in modern European history — establishing the professional general staff system, the Auftragstaktik (mission tactics) doctrine, the systematic training and promotion by merit rather than social rank, and the combined-arms operational concept that shaped every subsequent European and American army. The Prussian Army won the decisive wars that created the German Empire and defined the European balance of power.\n\n"
            "The Prussian Army's defining achievement was not tactical brilliance (though Frederick the Great's oblique order at Leuthen, 1757, was one of the finest tactical operations in military history) but institutional innovation: Gerhard von Scharnhorst and August von Gneisenau's reforms after the catastrophic defeats to Napoleon (Jena-Auerstedt, 1806) created the modern general staff system — a permanent body of highly trained officers doing continuous peacetime operational planning, selecting and developing leaders, and managing the army's institutional knowledge. This innovation was adopted by every major army.\n\n"
            "The Prussian Army's Auftragstaktik (mission tactics) — giving junior officers clear objectives and the authority to make independent decisions in pursuit of those objectives — proved decisive in the rapid wars against Austria (1866) and France (1870–1871), and became the doctrinal foundation of German military practice through two World Wars and the tactical template for NATO's AirLand Battle doctrine."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Most influential military institution in modern European history (Brandenburg 1650s–German Army 1871); modern general staff system originator (Scharnhorst and Gneisenau post-Jena reforms 1806); Auftragstaktik (mission tactics) — NATO AirLand Battle doctrine foundation; Frederick the Great (1740–1786), oblique order at Leuthen (1757); Austro-Prussian War (1866) and Franco-Prussian War (1870–1871) — German Empire creation; adopted by every major European and American army; combined-arms operational concept originator.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Great Elector Frederick William's creation of a permanent standing army (1655–1660) — funded by war taxes and maintained in peacetime — broke with the mercenary army tradition and established the institutional foundation of a permanent Prussian state military force loyal to the Hohenzollern dynasty",
            "The catastrophic Prussian defeat at Jena-Auerstedt (1806) — where Napoleon destroyed the Prussian Army in a single day, demonstrating the bankruptcy of 18th-century linear tactics — created the political and institutional pressure for Scharnhorst and Gneisenau's radical military reforms, which produced the modern general staff system",
            "Frederick the Great's military genius — and his systematic development of the oblique attack as a tactical tool for defeating larger forces — created the tradition of operational ingenuity and tactical initiative that became the defining culture of Prussian and German military thinking"
        ],
        "effects": [
            "The Prussian general staff system — a permanent body of continuously planning officers who managed institutional military knowledge, selected and developed leaders, and prepared operational plans in peacetime — was adopted by every major army in the 19th and 20th centuries, becoming the universal model for military organisation and the primary vehicle for professionalising military leadership",
            "The Prussian Army's victories in the Austro-Prussian War (1866) and Franco-Prussian War (1870–1871) — achieved through the general staff's railway mobilisation planning, combined-arms tactics, and the Dreyse needle gun — created the German Empire (1871) and established Germany as the dominant Continental power, directly causing the alliance system that produced the First World War",
            "The Auftragstaktik doctrine — granting junior officers the authority to act independently within a commander's intent — was adopted by the German Army in WWI and WWII as the doctrinal basis of Blitzkrieg, and was subsequently adopted by NATO (AirLand Battle doctrine, 1982) as the standard for Western military tactics in the Cold War",
            "The Prussian Army's educational system — the Kriegsakademie (War Academy) producing the most professionally educated officers in Europe — became the model for military education worldwide, establishing the principle that military leadership required systematic intellectual development rather than merely practical experience"
        ],
        "relationships": [
            {"entity": "Modern general staff system (Scharnhorst and Gneisenau post-Jena reforms 1806)", "relationship": "ORIGINATOR_OF_THE", "note": "Scharnhorst and Gneisenau's post-Jena reforms created the modern general staff — a permanent body of continuously planning officers — adopted by every major army"},
            {"entity": "Battle of Leuthen (1757, Frederick the Great, oblique order, greatest 18th-century tactical operation)", "relationship": "GREATEST_TACTICAL_ACHIEVEMENT_WAS_THE", "note": "Frederick the Great's oblique order at Leuthen — defeating an Austrian force twice the Prussian size — is considered the finest tactical operation of the 18th century"},
            {"entity": "Austro-Prussian War and Franco-Prussian War (1866, 1870–1871, German Empire creation)", "relationship": "DECISIVE_MILITARY_INSTRUMENT_IN_THE_WARS_THAT_CREATED_THE_GERMAN_EMPIRE", "note": "The Prussian Army's victories in 1866 and 1870–1871 — achieved through general staff planning and Auftragstaktik — created the German Empire"},
            {"entity": "Auftragstaktik doctrine (mission tactics, Blitzkrieg basis, NATO AirLand Battle)", "relationship": "ORIGINATOR_AND_PRIMARY_PRACTITIONER_OF_THE", "note": "Auftragstaktik — developed by the Prussian Army and refined into Blitzkrieg — became the doctrinal foundation of NATO's AirLand Battle doctrine"},
            {"entity": "Battle of Jena-Auerstedt (1806, Napoleon's destruction of Prussian Army, reforms catalyst)", "relationship": "DESTROYED_BY_NAPOLEON_AT_THE", "note": "The Prussian Army's destruction at Jena-Auerstedt created the political pressure for Scharnhorst's reforms that produced the modern general staff system"}
        ],
    }),

    ("united-states-army", {
        "summary": (
            "The United States Army (est. 1775 as the Continental Army — the first US military institution, created by the Second Continental Congress and commanded by George Washington — becoming the standing US Army in 1784) is the world's most powerful land force in the contemporary era — with 485,000+ active duty soldiers, 1 million+ Reserve and National Guard personnel, and an annual budget of $185+ billion — and has been the decisive military instrument of American global power since the Spanish-American War (1898). The US Army has participated in every major conflict of the 20th and 21st centuries, from the Western Front in WWI to Iraq and Afghanistan.\n\n"
            "The US Army's defining institutional characteristic is the combination of massive industrial capability with doctrinal adaptability — the ability to rapidly expand from a small standing force to a mass army (from 189,000 in December 1941 to 8.3 million in 1945), equip it with standardised mass-produced equipment, and develop effective doctrine through operational experience. The US Army's WWII expansion — the greatest military industrial mobilisation in history — is the primary reason for the Allied victory in Europe and the Pacific.\n\n"
            "The US Army's post-WWII evolution — from the conventional warfare dominance of the Cold War period, through the asymmetric challenges of Vietnam (1965–1973), the Goldwater-Nichols doctrinal reform (1986), the Gulf War (1991 — the first major demonstration of the Air-Land Battle doctrine), to the Counter-Insurgency (COIN) focus of Iraq and Afghanistan — demonstrates the continuous institutional adaptation that has kept it the world's most capable land force."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's most powerful contemporary land force (est. 1775 Continental Army, George Washington commander; 485,000+ active duty, $185B+ budget); WWII mobilisation — 189,000 to 8.3 million soldiers (December 1941–1945), greatest military industrial mobilisation in history; Spanish-American War (1898, global power instrument); WWI Western Front, WWII Europe and Pacific, Korean War, Vietnam (1965–1973), Gulf War 1991 (AirLand Battle doctrine debut), Iraq and Afghanistan COIN; Goldwater-Nichols reform (1986); primary reason for Allied victory WWII.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The American Revolution's need for a unified military force — replacing the 13 colonies' individual militias with a continental army that could fight the British Army over a multi-year campaign — drove the creation of the Continental Army (1775) and the institutional foundation of the US military",
            "American industrial capacity — developed through the 19th century and reaching its peak in the 20th — created the material basis for the US Army's WWII mobilisation, with American industrial production outpacing all Axis nations' combined output and making the US Army the best-equipped mass army in history",
            "The Cold War's strategic competition with the Soviet Union — requiring the United States to maintain a large standing force in Western Europe for the first time in peacetime — transformed the US Army from a traditionally small standing force that expanded in wartime to a large permanent institution, fundamentally changing American military culture"
        ],
        "effects": [
            "The US Army's WWII mobilisation — expanding from 189,000 to 8.3 million soldiers (1941–1945) and deploying across North Africa, Europe, and the Pacific — was the decisive factor in the Allied defeat of Nazi Germany and Imperial Japan, making the US Army the primary military instrument of the 20th century's defining conflict",
            "The US Army's post-WWII occupation of Germany and Japan — through the GI Bill, the Marshall Plan, and the occupation governance — shaped the reconstruction of both nations into democratic, market-economy states, creating the geopolitical framework that defined the second half of the 20th century",
            "The Gulf War's demonstration of the AirLand Battle doctrine (1991) — the first major test of joint air-ground operations since WWII, with Coalition forces destroying the world's fourth-largest army in 100 hours of ground combat — established the US Army's conventional dominance and set the template for 21st-century US military operations",
            "The US Army's Counter-Insurgency doctrine — developed through the hard experience of Iraq and Afghanistan and codified in FM 3-24 (the 'Petraeus manual', 2006) — became the most widely studied military doctrine of the 21st century, influencing Western military thinking about the relationship between military force and political legitimacy"
        ],
        "relationships": [
            {"entity": "George Washington (Continental Army commander, 1775, Revolution)", "relationship": "FIRST_COMMANDING_GENERAL_AND_INSTITUTIONAL_FOUNDER_WAS", "note": "Washington's creation and command of the Continental Army — maintaining it through defeats and harsh winters — is the founding act of the US Army"},
            {"entity": "WWII Allied victory (8.3M US soldiers, greatest military industrial mobilisation)", "relationship": "DECISIVE_MILITARY_INSTRUMENT_OF_THE", "note": "The US Army's WWII mobilisation — the greatest in history — was the decisive factor in the Allied defeat of Nazi Germany and Imperial Japan"},
            {"entity": "Gulf War 1991 (AirLand Battle doctrine debut, 100-hour ground campaign)", "relationship": "FIRST_MAJOR_OPERATIONAL_TEST_OF_ITS_AIRDLAND_BATTLE_DOCTRINE_WAS_THE", "note": "The Gulf War's 100-hour ground campaign — destroying the world's fourth-largest army — demonstrated US Army conventional dominance"},
            {"entity": "FM 3-24 Counter-Insurgency manual (2006, Petraeus, most studied 21st-century military doctrine)", "relationship": "ORIGINATOR_OF_THE", "note": "The US Army's FM 3-24 COIN manual — developed from Iraq and Afghanistan experience — became the most widely studied military doctrine of the 21st century"},
            {"entity": "Marshall Plan and GI Bill (post-WWII occupation governance, Germany and Japan reconstruction)", "relationship": "OCCUPATION_GOVERNANCE_CONTEXT_FOR_THE", "note": "The US Army's occupation of Germany and Japan — alongside the Marshall Plan and GI Bill — shaped both nations' reconstruction into democratic states"}
        ],
    }),

    ("french-army", {
        "summary": (
            "The French Army (Armée de Terre — with institutional origins in the permanent royal army created by Charles VII in the 1440s, and the national conscript army of the French Revolution, 1792) has been the dominant land force in Western European military history for 400 years — responsible for the most important military innovations of the pre-industrial era (the systematic use of artillery as an offensive arm; Vauban's fortification science; the corps system; the combined-arms divisional organisation), the creation of mass conscript warfare through the levée en masse (1793), and the Napoleonic operational system that transformed European warfare.\n\n"
            "The French Army's defining military moment was the Napoleonic era (1799–1815) — when under Napoleon Bonaparte it conquered most of continental Europe, reaching from Portugal to Moscow, implementing the corps system that allowed independent march and combined battle, and demonstrating the 'strategy of the central position' (defeating superior forces in detail by concentrating against each separately). The Napoleonic system became the template for 19th-century warfare, studied by every subsequent military leader from Clausewitz to Grant.\n\n"
            "The French Army's post-Napoleonic history is defined by two catastrophic defeats — the Franco-Prussian War (1870–1871, the fall of the Second Empire) and the Fall of France (May–June 1940, the German defeat in six weeks) — that bracket the defining experience of the First World War, where the French Army bore the brunt of the Western Front (1.5 million French military deaths) and demonstrated both extraordinary defensive resilience (Verdun, 1916 — 300,000 casualties in 10 months) and the limitations of the offensive spirit doctrine."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "Dominant land force in Western European military history for 400 years; corps system and divisional combined-arms organisation originators; levée en masse (1793, mass conscript warfare); Vauban fortification science; Napoleonic operational system (1799–1815) — template for 19th-century warfare; Franco-Prussian War (1870–1871), WWI Western Front (1.5M French military deaths), Verdun (1916, 300,000 casualties), Fall of France (1940, six-week defeat); Charles VII permanent royal army (1440s); strategic innovations studied by Clausewitz to Grant.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Hundred Years' War's demonstration that feudal levies were inadequate for sustained professional warfare — and Charles VII's creation of the first permanent royal army (1445–1448, the compagnies d'ordonnance) — established the institutional basis for the French standing army that would dominate European warfare for four centuries",
            "The French Revolution's levée en masse (1793) — mobilising the entire French nation for military service, generating 800,000 soldiers from a population of 28 million — created the first true mass national army, overwhelming the professional armies of the ancien régime through sheer weight of numbers and revolutionary motivational cohesion",
            "Napoleon Bonaparte's military genius — and his systematic exploitation of the divisional and corps system that allowed armies to march dispersed and concentrate for battle — created the Napoleonic operational system that demonstrated the decisive superiority of manoeuvre warfare over the linear tactics of 18th-century professional armies"
        ],
        "effects": [
            "The French Army's corps system — allowing an army to march dispersed across multiple roads, living off the land, and concentrate for battle within 24 hours — was adopted by every major army in the 19th century, transforming the operational level of war and making possible the rapid manoeuvre campaigns that characterised 19th-century European warfare",
            "The levée en masse (1793) — creating the first mass national conscript army — transformed warfare from a professional specialised activity into a national enterprise, with enormous consequences for the scale of subsequent conflicts: the wars of the 19th and 20th centuries would be fought by national conscript armies measured in millions rather than the professional armies measured in tens of thousands",
            "The Battle of Verdun (1916) — where the French Army held the strategically critical fortress city against the largest German offensive of the First World War at a cost of 300,000 casualties — demonstrated the extraordinary resilience of the French national will and became the defining French military experience of the 20th century, shaping French strategic culture through de Gaulle and the nuclear deterrent",
            "Vauban's fortification science — developed in the service of Louis XIV's French Army and systematised in his Traité de l'attaque et de la défense des places (1704) — established the engineering principles of siege warfare that governed fortress construction and attack for 150 years, with Vauban's 'trace italienne' star fort design built from Brazil to Quebec"
        ],
        "relationships": [
            {"entity": "Napoleon Bonaparte (Napoleonic Wars 1799–1815, corps system exploitation, Europe conquest)", "relationship": "GREATEST_OPERATIONAL_COMMANDER_AND_DEFINING_FIGURE_WAS", "note": "Napoleon's exploitation of the corps system — allowing dispersed march and concentrated battle — created the operational template for 19th-century warfare"},
            {"entity": "Levée en masse (1793, French Revolution, mass conscript warfare creation)", "relationship": "ORIGINATOR_OF_MASS_NATIONAL_CONSCRIPT_WARFARE_THROUGH_THE", "note": "The levée en masse — mobilising 800,000 French soldiers — transformed warfare from a professional activity into a national enterprise, shaping all subsequent major conflicts"},
            {"entity": "Battle of Verdun (1916, 300,000 casualties, French resilience)", "relationship": "DEFINING_DEFENSIVE_ACHIEVEMENT_WAS_THE", "note": "Verdun — held against Germany's largest offensive at 300,000 casualties — became the defining French military experience of the 20th century"},
            {"entity": "Vauban (fortification science, Louis XIV, Traité de l'attaque, star fort design)", "relationship": "FORTIFICATION_SYSTEM_DEVELOPED_IN_SERVICE_TO_THE", "note": "Vauban's fortification science — developed for Louis XIV's French Army — governed fortress construction worldwide for 150 years"},
            {"entity": "Corps system (march dispersed, concentrate for battle, 19th-century warfare template)", "relationship": "ORIGINATOR_AND_PRIMARY_DEVELOPER_OF_THE", "note": "The French Army's corps system — adopted by every major 19th-century army — transformed the operational level of war"}
        ],
    }),

    ("peoples-liberation-army-ground-force", {
        "summary": (
            "The People's Liberation Army Ground Force (PLAGF — the land component of the People's Liberation Army of the People's Republic of China, reorganised as an independent service branch in 2016) is the world's largest standing army by personnel — with approximately 965,000 active soldiers — and the primary land defence force of the world's most populous nation. The PLA traces its origins to the Nanchang Uprising (1 August 1927), regarded as the founding date of the People's Liberation Army, and fought the Chinese Civil War, the Korean War, the Sino-Indian War, and the Sino-Vietnamese War before transforming into a modern mechanised force.\n\n"
            "The People's Liberation Army was created by the Chinese Communist Party as its military arm during the Chinese Civil War (1927–1949) — fighting the Japanese invasion (1937–1945) and the Chinese Nationalist (Kuomintang) forces simultaneously. Mao Zedong's doctrinal innovation — 'People's War' (guerrilla tactics, political mobilisation of the peasantry, dispersal then concentration against weakened enemies) — provided the strategic framework that defeated the militarily superior Nationalist forces and drove Japanese forces from large areas of China.\n\n"
            "The PLAGF's transformation since the 1990s — from a mass infantry force (4 million soldiers in 1991) to a smaller, more technologically advanced mechanised force emphasising joint operations, information warfare, and rapid power projection — represents the most ambitious military modernisation programme in the world, driven by the observed performance of the US Army in the Gulf War (1991) and the strategic imperative of Taiwan contingency planning."
        ),
        "importanceScore": 10,
        "historicalSignificance": {
            "significanceScore": 10,
            "significanceNarrative": "World's largest standing army (est. Nanchang Uprising 1927; 965,000 active soldiers); Mao Zedong's People's War doctrine (guerrilla tactics, peasant mobilisation); Chinese Civil War (1927–1949), Korean War (Chinese intervention 1950–1953), Sino-Indian War (1962), Sino-Vietnamese War (1979); Taiwan contingency planning; military modernisation since Gulf War 1991 observation; reorganised as independent service 2016; 4 million soldiers reduced to 965,000 modern mechanised force; PRC founding military instrument.",
            "significanceCategory": "world-changing"
        },
        "causes": [
            "The Chinese Communist Party's need for a military arm during the Chinese Civil War — following the Kuomintang's Shanghai Massacre (1927), which drove the CCP from the cities into the countryside and necessitated the creation of a guerrilla army — drove the founding of the PLA at the Nanchang Uprising (1 August 1927)",
            "Mao Zedong's 'People's War' doctrine — the theoretical framework for using political mobilisation of the peasantry and guerrilla warfare to compensate for material inferiority — provided the strategic guidance that allowed the PLA to defeat the better-equipped Nationalist forces and the Japanese Army in a 22-year campaign",
            "The People's Republic of China's strategic vulnerability — surrounded by potentially hostile powers (the US in Korea, Taiwan, India, the Soviet Union after 1960) — drove the continuous military development that transformed the PLA from a guerrilla force into a conventional army and ultimately into a modern mechanised force"
        ],
        "effects": [
            "The PLA's victory in the Chinese Civil War (1949) — creating the People's Republic of China and expelling the Nationalist government to Taiwan — was the event that established the political framework of East Asia for the subsequent 75 years, creating the Taiwan question that remains one of the most significant potential flashpoints in contemporary international relations",
            "The PLA's intervention in the Korean War (October 1950) — driving UN forces back from the Chinese border and ultimately forcing the armistice that established the Korean demilitarised zone — demonstrated that the new People's Republic of China could resist the United States militarily, establishing the strategic context for the Cold War in Asia",
            "The PLA's Sino-Indian War (1962) — in which Chinese forces rapidly defeated Indian Army units in the Himalayas — created the strategic rivalry between the world's two most populous nations that continues to shape South Asian geopolitics, including the nuclear competition and the continuing border disputes in Ladakh and Arunachal Pradesh",
            "The PLA's modernisation programme since the 1990s — reducing personnel from 4 million to 965,000 while massively increasing capability — represents the most ambitious military transformation in history, with implications for the balance of power in East Asia and the potential for conflict over Taiwan that constitute the primary military planning concern of the US and its allies"
        ],
        "relationships": [
            {"entity": "Nanchang Uprising (1 August 1927, PLA founding date)", "relationship": "FOUNDING_DATE_AT_THE", "note": "The Nanchang Uprising — the CCP's first armed revolt against the Kuomintang — is the official founding date of the People's Liberation Army"},
            {"entity": "Mao Zedong's People's War doctrine (guerrilla tactics, peasant mobilisation)", "relationship": "STRATEGIC_AND_DOCTRINAL_FOUNDATION_ESTABLISHED_BY", "note": "Mao's People's War — political mobilisation of the peasantry plus guerrilla tactics — provided the framework for the PLA's defeat of militarily superior Nationalist and Japanese forces"},
            {"entity": "People's Republic of China (1949, civil war victory, Taiwan question creation)", "relationship": "PRIMARY_MILITARY_INSTRUMENT_OF_THE_FOUNDING_OF_THE", "note": "The PLA's civil war victory created the PRC and the Taiwan question that remains East Asia's most significant potential flashpoint"},
            {"entity": "Korean War Chinese intervention (October 1950, UN forces pushed back, armistice)", "relationship": "CONDUCTED_THE_DECISIVE_CHINESE_INTERVENTION_IN_THE", "note": "The PLA's Korean War intervention — driving UN forces back from the Chinese border — demonstrated that the new PRC could resist the United States militarily"},
            {"entity": "Gulf War 1991 (US Army performance, PLAGF modernisation catalyst)", "relationship": "MILITARY_MODERNISATION_PROGRAMME_CATALYSED_BY_THE_OBSERVED_US_ARMY_PERFORMANCE_IN_THE", "note": "The US Army's Gulf War performance drove the PLA's post-1991 modernisation — the most ambitious military transformation in history"}
        ],
    }),

]


if __name__ == "__main__":
    print(f"Batch 46 \u2014 {len(ENTITIES)} entities (Class 391: Famous Armies)")
    for slug, data in ENTITIES:
        print(f"\n\u2192 {slug}")
        enrich_entity(slug, data)
    print("\n\u2713 Done")
